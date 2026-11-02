import sys
import json
import time
import subprocess
import statistics
import tracemalloc
import importlib
import importlib.util
import csv
import os
import shutil
import multiprocessing

NO_CPU_PINNING = -1

def clean_bytecode():
    """Recursively deletes all __pycache__ directories and .pyc files to ensure disk-level cold starts."""
    print("Sweeping directory to delete __pycache__ and force bytecode recompilation...")
    count = 0
    # Walk the directory avoiding hidden directories (e.g. .git, .venv, .nox)
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))
            dirs.remove('__pycache__')
            count += 1
        for f in files:
            if f.endswith('.pyc'):
                os.remove(os.path.join(root, f))
                count += 1
    print(f"Cleared {count} cached bytecode locations.")

def get_rss_mb():
    """Gets current Resident Set Size (physical memory) in MB. Linux only."""
    try:
        with open('/proc/self/statm', 'r') as f:
            rss_pages = int(f.read().split()[1])
            page_size = os.sysconf('SC_PAGE_SIZE')
            return (rss_pages * page_size) / (1024 * 1024)
    except Exception:
        return 0.0

def run_worker(target_module, skip_line_count=False):
    """Performs ONE import and returns metrics."""
    tracemalloc.start()
    importlib.invalidate_caches()
    sys.path_importer_cache.clear()
    rss_before = get_rss_mb()
    modules_before = set(sys.modules.keys())
    
    # We start the high-resolution timer from *inside* the already-booted worker process.
    # This explicitly isolates the pure import latency and entirely omits the 
    # 10ms-50ms Python VM interpreter startup overhead that would skew the metrics.
    start_time = time.perf_counter()
    
    # --- TARGET IMPORT ---
    importlib.import_module(target_module)
    # ---------------------
    
    end_time = time.perf_counter()
    rss_after = get_rss_mb()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    modules_after = set(sys.modules.keys())
    new_modules = modules_after - modules_before
    
    loaded_lines = 0
    if not skip_line_count:
        for m in new_modules:
            try:
                file_path = sys.modules[m].__file__
                if not file_path:
                    continue

                if file_path.endswith('.pyc'):
                    try:
                        file_path = importlib.util.source_from_cache(file_path)
                    except ValueError:
                        # Raised if the .pyc path does not follow standard PEP 3147/488 conventions.
                        # We pass silently because the unresolved file_path will still end in '.pyc', 
                        # meaning the subsequent '.endswith('.py')' check will fail and safely skip 
                        # trying to count lines in a binary file.
                        pass
                if file_path.endswith('.py'):
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            loaded_lines += sum(1 for _ in f)
                    except OSError as e:
                        print(f"WARNING: Failed to read lines from {file_path}: {e}", file=sys.stderr)
            except KeyError:
                # Module disappeared from sys.modules during execution
                pass
            except AttributeError:
                # Module has no __file__ attribute (likely a C-extension or built-in)
                pass
    else:
        loaded_lines = -1
    
    # Output to stdout for the Master to capture
    metrics = {
        "time_ms": (end_time - start_time) * 1000,
        "peak_ram_mb": peak / (1024 * 1024),
        "rss_ram_mb": rss_after - rss_before,
        "loaded_modules": len(new_modules),
        "loaded_lines": loaded_lines
    }
    print(f"__METRICS__:{json.dumps(metrics)}")

def _run_worker_and_parse(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr)
    try:
        lines = result.stdout.strip().splitlines()
        data = None
        for line in reversed(lines):
            if line.startswith("__METRICS__:"):
                data = json.loads(line[len("__METRICS__:"):])
                break
        if data is None:
            raise ValueError("Worker did not output metrics JSON.")
        for key in ("time_ms", "peak_ram_mb", "rss_ram_mb", "loaded_modules", "loaded_lines"):
            if key not in data:
                raise KeyError(f"Missing key '{key}' in worker output")
        return data
    except (json.JSONDecodeError, IndexError, KeyError, ValueError) as parse_err:
        print(f"Error parsing worker output: {parse_err}", file=sys.stderr)
        print(f"Worker stdout:\n{result.stdout}", file=sys.stderr)
        print(f"Worker stderr:\n{result.stderr}", file=sys.stderr)
        raise parse_err

def _print_outputs(target_module, iterations, loaded_modules_val, loaded_lines_val,
                   times, memories, rss_memories):
    """Helper method to format and print the final benchmark results."""
    def _format_stats(title, data, fmt):
        if not data:
            return ""
        n = len(data)
        p50 = statistics.median(data)
        min_val = min(data)
        max_val = max(data)
        std_dev = statistics.stdev(data) if n > 1 else 0.0

        stats_lines = [
            f"{title} [N={n}]:",
            f"  Min:    {min_val:{fmt}}",
            f"  P50:    {p50:{fmt}}",
            f"  Max:    {max_val:{fmt}}"
        ]
        if n > 1:
            stats_lines.append(f"  StdDev:    {std_dev:{fmt}}")
        return "\n".join(stats_lines) + "\n"

    final_output = f"""
--- Results for {target_module} ({iterations} iterations) ---
Code Volume (Deterministic):
  Loaded Modules: {loaded_modules_val}
  Loaded Lines:   {loaded_lines_val}
{_format_stats("Time (ms)", times, ".2f")}{_format_stats("Tracemalloc RAM (MB)", memories, ".4f")}{_format_stats("Physical RSS RAM (MB)", rss_memories, ".4f")}"""
    print(final_output.strip())

def run_master(iterations, target_module, cpu=0, csv_path=None, clear_cache=True, fail_threshold=None, diff_baseline=None, diff_threshold=None):
    """Orchestrates the benchmark."""
    if iterations < 1:
        raise ValueError("Number of iterations must be at least 1.")
    times, memories, rss_memories = [], [], []
    loaded_modules_val, loaded_lines_val = 0, 0
    
    print(f"Profiling start... Running {iterations} cold-start iterations for {target_module}.")
    
    if clear_cache:
        clean_bytecode()
        python_exe = [sys.executable, "-B"] # -B prevents writing .pyc files so every iteration reads raw .py
    else:
        python_exe = [sys.executable]
        
    if cpu != NO_CPU_PINNING:
        if not sys.platform.startswith("linux"):
            print("WARNING: CPU pinning is only supported on Linux. Falling back to unpinned execution.")
            cpu = NO_CPU_PINNING
        else:
            print(f"CPU Pinning enabled: Pinning processes to core {cpu} using taskset.")
    else:
        print("CPU Pinning disabled.")
    
    for i in range(iterations):
        # Build command line
        cmd = []
        if cpu != NO_CPU_PINNING:
            cmd += ["taskset", "-c", str(cpu)]
        
        cmd += python_exe + [__file__, "--worker", f"--module={target_module}"]
        if i > 0:
            cmd += ["--skip-line-count"]
        
        try:
            data = _run_worker_and_parse(cmd)
            times.append(data["time_ms"])
            memories.append(data["peak_ram_mb"])
            rss_memories.append(data["rss_ram_mb"])
            print(f"Iteration {i+1}/{iterations} completed in {data['time_ms']:.2f} ms")
            if i > 0 and loaded_modules_val != data["loaded_modules"]:
                print(f"WARNING: Non-deterministic import behavior! Iteration {i+1} loaded {data['loaded_modules']} modules (expected {loaded_modules_val}).", file=sys.stderr)
            
            loaded_modules_val = data["loaded_modules"]
            if data["loaded_lines"] == -1:
                data["loaded_lines"] = loaded_lines_val
            else:
                loaded_lines_val = data["loaded_lines"]
        except FileNotFoundError as e:
            if cpu != NO_CPU_PINNING and cmd and cmd[0] == "taskset":
                print("ERROR: 'taskset' command not found. CPU pinning is enabled but taskset is not installed. "
                      "Install taskset or disable pinning by passing --cpu=-1.", file=sys.stderr)
            raise e
        except subprocess.CalledProcessError as e:
            print(f"Error in worker process:\n{e.stderr}", file=sys.stderr)
            raise e
        
    if iterations > 1:
        times = times[1:]
        memories = memories[1:]
        rss_memories = rss_memories[1:]
        iterations -= 1
        print("Discarded the first iteration as a cache burn-in run.")

    # Write CSV if requested
    if csv_path:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Iteration", "Time (ms)", "Tracemalloc RAM (MB)", "RSS Physical RAM (MB)"])
            for idx, (t, m, r) in enumerate(zip(times, memories, rss_memories)):
                writer.writerow([idx + 1, f"{t:.2f}", f"{m:.4f}", f"{r:.4f}"])
        print(f"Raw metrics successfully exported to CSV: {csv_path}")

    p50_time = statistics.median(times) if times else 0.0

    _print_outputs(
        target_module, iterations, loaded_modules_val, loaded_lines_val,
        times, memories, rss_memories
    )

    exit_code = 0
    final_messages = []

    baseline_p50 = None
    if diff_baseline:
        if os.path.exists(diff_baseline):
            baseline_times = []
            with open(diff_baseline, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    baseline_times.append(float(row[1]))
            if baseline_times:
                baseline_p50 = statistics.median(baseline_times)
            
            if baseline_p50 is not None:
                diff = p50_time - baseline_p50
                
                diff_msg = (
                    f"--- Diff vs Baseline ---\n"
                    f"Baseline Median: {baseline_p50:.2f} ms\n"
                    f"Current Median:  {p50_time:.2f} ms\n"
                    f"Difference:      {diff:+.2f} ms"
                )
                final_messages.append(diff_msg)
                
                relative_diff_threshold = 0.15 * baseline_p50
                if diff > diff_threshold and diff > relative_diff_threshold:
                    final_messages.append(
                        f"FAILURE: Import time regression of {diff:.2f} ms exceeds both the absolute threshold ({diff_threshold} ms) "
                        f"and the relative threshold ({relative_diff_threshold:.2f} ms, 15% of baseline Median)."
                    )
                    exit_code = 1
                else:
                    if diff > diff_threshold:
                        final_messages.append(f"SUCCESS: Import time regression of {diff:.2f} ms exceeds absolute threshold ({diff_threshold} ms) but is within relative threshold ({relative_diff_threshold:.2f} ms, 15%).")
                    else:
                        final_messages.append("SUCCESS: Import time diff is within acceptable thresholds.")
        else:
            final_messages.append(f"WARNING: Baseline CSV {diff_baseline} not found. Skipping diff check.")

    if fail_threshold is not None:
        if p50_time > fail_threshold:
            if baseline_p50 is not None and baseline_p50 > fail_threshold:
                final_messages.append(f"WARNING: Median import time ({p50_time:.2f} ms) exceeds the absolute failure threshold ({fail_threshold} ms), but the baseline ({baseline_p50:.2f} ms) also exceeded it. Bypassing absolute backstop failure.")
            else:
                final_messages.append(f"FAILURE: Median import time ({p50_time:.2f} ms) exceeds the failure threshold ({fail_threshold} ms).")
                exit_code = 1
        else:
            final_messages.append(f"SUCCESS: Median import time ({p50_time:.2f} ms) is within the failure threshold ({fail_threshold} ms).")

    if final_messages:
        print("\n" + "\n".join(final_messages))
        
    if exit_code == 0:
        print("\nSession import_profiler was successful.")
    else:
        print("\nSession import_profiler failed.")
    return exit_code


def run_trace(target_module):
    """Generates importtime trace log and writes it to a file."""
    trace_file = f"import_trace_{target_module.replace('.', '_')}.log"
    print(f"Generating importtime trace log for {target_module} -> {trace_file}...")
    
    # We run: python -X importtime -c "import importlib; importlib.import_module(...)"
    result = subprocess.run(
        [sys.executable, "-X", "importtime", "-c", f"import importlib; importlib.import_module({json.dumps(target_module)})"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"WARNING: Import failed with exit code {result.returncode}. The trace log may be incomplete or contain errors.", file=sys.stderr)
        if result.stdout:
            print(f"Worker stdout:\n{result.stdout}", file=sys.stderr)
        if result.stderr:
            print(f"Worker stderr:\n{result.stderr}", file=sys.stderr)
            
    with open(trace_file, "w", encoding="utf-8") as f:
        f.write(result.stderr)
        
    print(f"Trace log successfully written to {trace_file}")

def run_cprofile(target_module):
    """Runs cProfile in a clean subprocess to capture stack traces for latency."""
    import pstats
    
    prof_file = f"cprofile_{target_module.replace('.', '_')}.prof"
    print(f"Generating cProfile data for {target_module} -> {prof_file}...")
    
    # Run profiling in a clean subprocess to ensure cold-start
    result = subprocess.run(
        [sys.executable, "-m", "cProfile", "-o", prof_file, "-c", f"import importlib; importlib.import_module({json.dumps(target_module)})"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error generating cProfile data:\n{result.stderr}", file=sys.stderr)
        return

    print(f"cProfile stats successfully written to {prof_file}")
    
    # Print top bottlenecks
    print("\n--- Top 15 functions by cumulative time ---")
    ps = pstats.Stats(prof_file).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats(15)

def _mprofile_worker(target_module):
    import tracemalloc
    tracemalloc.start()
    importlib.import_module(target_module)
    snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()
    top_stats = snapshot.statistics('lineno')
    print("\n--- Top 15 memory allocations by line ---")
    for stat in top_stats[:15]:
        print(stat)

def run_mprofile(target_module):
    """Runs tracemalloc snapshot in a clean subprocess to see where memory is allocated."""
    print(f"Generating tracemalloc memory snapshot for {target_module}...")
    
    # Use 'spawn' to ensure a completely clean python process without inherited module caches
    ctx = multiprocessing.get_context("spawn")
    p = ctx.Process(target=_mprofile_worker, args=(target_module,))
    p.start()
    p.join()
    
    if p.exitcode != 0:
        print(f"Error generating memory snapshot, process exited with code {p.exitcode}", file=sys.stderr)

def validate_module_name(module_name):
    """Validates that the input is a structurally valid Python module identifier to prevent arbitrary code execution."""
    import argparse
    if not all(part.isidentifier() for part in module_name.split('.')):
        raise argparse.ArgumentTypeError(f"'{module_name}' is not a valid Python module identifier.")
    return module_name

IGNORED_TOP_LEVEL_NAMES = {
    "tests", "samples", "examples", "benchmark", "benchmarks", "third_party",
    "testing", "test_utils", "docs", "build", "dist", "bin", "ci", "scripts",
    "cloudbuild", "notebooks", "assets", "scratch", "specs"
}
IGNORED_NAME_PREFIXES = (
    "test_", "tests_", "sample_", "samples_", "bench_", "benchmarks_",
    "example_", "examples_", "doc_", "docs_", "notebook_", "notebooks_"
)


def _should_process_namespace_package(top_level: str, target_pkg: str) -> bool:
    """Determines if a discovered top-level directory should be processed.

    Args:
        top_level: Top-level directory component of the package (e.g. 'tests' or 'google').
        target_pkg: The distribution package being profiled (e.g. 'google-cloud-storage').

    Returns:
        True if the top-level directory should be processed, False otherwise.
    """
    is_excluded_candidate = (
        top_level in IGNORED_TOP_LEVEL_NAMES
        or top_level.startswith(IGNORED_NAME_PREFIXES)
    )

    if is_excluded_candidate:
        normalized_target_pkg = target_pkg.replace("-", "").replace("_", "").lower()
        normalized_top_level = top_level.replace("-", "").replace("_", "").lower()
        # Note: If the top-level folder name is part of the target package name
        # (e.g. top_level='test_utils' when target_pkg='google-cloud-testutils'), then it should be processed.
        return normalized_top_level in normalized_target_pkg

    return True  # Not a candidate for exclusion, process it.


def _is_path_allowed(path_obj, pkg_norm: str) -> bool:
    """Checks if a path object is allowed based on ignored directory rules."""
    from pathlib import Path
    parts = Path(path_obj).parts
    return all(
        part not in IGNORED_TOP_LEVEL_NAMES
        or part.replace("-", "").replace("_", "").lower() in pkg_norm
        for part in parts
    )


def find_module_from_package(pkg):
    import importlib.metadata
    import importlib.util
    from pathlib import Path

    # 1. Try to use importlib.metadata.files (works for standard installations from PyPI/wheels)
    try:
        files = importlib.metadata.files(pkg)
        if files:
            pkg_norm = pkg.replace("-", "").replace("_", "").lower()
            init_files = [
                str(f) for f in files
                if Path(f).name == '__init__.py'
                and '__pycache__' not in Path(f).parts
                and _is_path_allowed(f, pkg_norm)
            ]
            if init_files:
                from pathlib import Path
                shortest_init = min(init_files, key=lambda p: len(Path(p).parts))
                parts = Path(shortest_init).parent.parts
                mod = '.'.join(parts)
                try:
                    if importlib.util.find_spec(mod):
                        return mod
                except Exception:
                    pass
    except Exception:
        pass

    # 2. Try setuptools.find_namespace_packages() in current directory (works for editable installs in source trees)
    try:
        import setuptools
        import os
        if os.path.exists('setup.py') or os.path.exists('pyproject.toml'):
            where_dir = "src" if os.path.isdir("src") else "."
            abs_where_dir = os.path.abspath(where_dir)
            if abs_where_dir not in sys.path:
                sys.path.insert(0, abs_where_dir)
            pkgs = setuptools.find_namespace_packages(where=where_dir)
            filtered = []
            for p in pkgs:
                top = p.split(".")[0]
                if _should_process_namespace_package(top, pkg):
                    filtered.append(p)

            # First preference: packages containing __init__.py
            for p in sorted(filtered, key=len):
                path = os.path.join(where_dir, p.replace('.', os.sep))
                try:
                    if os.path.isfile(os.path.join(path, '__init__.py')):
                        try:
                            if importlib.util.find_spec(p):
                                return p
                        except Exception:
                            pass
                except OSError:
                    continue

            # Second preference: namespace packages containing .py files (e.g. googleapis-common-protos -> google.api)
            for p in sorted(filtered, key=len):
                path = os.path.join(where_dir, p.replace('.', os.sep))
                try:
                    if os.path.isdir(path) and any(f.endswith('.py') for f in os.listdir(path)):
                        try:
                            if importlib.util.find_spec(p):
                                return p
                        except Exception:
                            pass
                except OSError:
                    continue
    except Exception as e:
        print(f"WARNING: Package discovery failed: {e}", file=sys.stderr)

    # 3. Fallback to basic string manipulation heuristics
    candidates = [
        pkg.replace('-', '.'),
        '.'.join(pkg.split('-')[:-1]) + '_' + pkg.split('-')[-1] if '-' in pkg else pkg,
        pkg.replace('-', '_')
    ]
    for mod in candidates:
        try:
            if importlib.util.find_spec(mod):
                return mod
        except Exception:
            pass
    return candidates[0]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Python SDK Import Profiler")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--module", type=validate_module_name, help="Target module to profile")
    group.add_argument("--package", help="Target package name to profile (auto-detects module)")
    parser.add_argument("--iterations", type=int, default=50, help="Number of iterations")
    default_cpu = 0 if sys.platform.startswith("linux") else NO_CPU_PINNING
    parser.add_argument("--cpu", type=int, default=default_cpu, help="CPU core to pin to (or -1 for no pinning)")
    parser.add_argument("--csv", help="Path to export CSV results")
    parser.add_argument("--trace", action="store_true", help="Generate importtime trace log")
    parser.add_argument("--cprofile", action="store_true", help="Run cProfile")
    parser.add_argument("--mprofile", action="store_true", help="Run tracemalloc memory snapshot")
    parser.add_argument("--keep-pycache", action="store_true", help="Preserve __pycache__ and allow bytecode execution (Default: False, script automatically sweeps __pycache__ for true cold-starts)")
    parser.add_argument("--fail-threshold", type=float, help="Fail the profiling if the Median time exceeds this threshold (in ms).")
    parser.add_argument("--diff-baseline", help="Path to a baseline CSV file to compare against.")
    parser.add_argument("--diff-threshold", type=float, default=100.0, help="Fail if Median time exceeds baseline Median by this many ms.")
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--skip-line-count", action="store_true", help=argparse.SUPPRESS)
    
    args = parser.parse_args()
    
    target_module = args.module
    if args.package:
        target_module = find_module_from_package(args.package)
    
    if args.worker:
        run_worker(target_module, skip_line_count=args.skip_line_count)
    elif args.trace:
        if not args.keep_pycache: clean_bytecode()
        run_trace(target_module)
    elif args.cprofile:
        if not args.keep_pycache: clean_bytecode()
        run_cprofile(target_module)
    elif args.mprofile:
        if not args.keep_pycache: clean_bytecode()
        run_mprofile(target_module)
    else:
        sys.exit(run_master(args.iterations, target_module, args.cpu, args.csv, not args.keep_pycache, args.fail_threshold, args.diff_baseline, args.diff_threshold))