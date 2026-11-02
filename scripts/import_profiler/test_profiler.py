# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import csv
import json
import os
import subprocess
import sys
from unittest.mock import MagicMock, mock_open, patch


import pytest

# Ensure scripts/import_profiler is in sys.path
sys.path.insert(0, os.path.dirname(__file__))

import profiler
from profiler import (
    NO_CPU_PINNING,
    _run_worker_and_parse,
    find_module_from_package,
    get_rss_mb,
    run_master,
    run_worker,
)

# =====================================================================
# 1. UTILITY FUNCTIONS TESTS
# =====================================================================


def test_get_rss_mb():
    """Verifies get_rss_mb returns a float representing megabytes if available."""
    rss = get_rss_mb()
    assert isinstance(rss, float)
    assert rss >= 0.0


@patch("os.walk")
@patch("os.remove")
@patch("shutil.rmtree")
def test_clean_bytecode(mock_rmtree, mock_remove, mock_walk):
    """Verifies clean_bytecode successfully cleans bytecode files & caches."""
    clean_bytecode_helper = getattr(profiler, "clean_bytecode", None)
    if clean_bytecode_helper is None:
        pytest.skip("clean_bytecode is not exported at the module level.")

    mock_walk.return_value = [
        ("/test_dir", ["__pycache__"], ["test.pyc", "test.py"])
    ]
    clean_bytecode_helper()
    assert mock_remove.called or mock_rmtree.called


def test_find_module_from_package_resolves():
    """Verifies resolving of packages to modules if helper is exported."""
    with patch(
        "importlib.metadata.files",
        return_value=["google/cloud/storage/__init__.py"],
    ), patch(
        "importlib.util.find_spec", 
        return_value=True
    ):
        res = find_module_from_package("google-cloud-storage")
        assert res == "google.cloud.storage"


def test_find_module_from_package_fallback():
    """Verifies fallback transforms work correctly if helper is exported."""
    with patch("importlib.util.find_spec", side_effect=lambda mod: mod == "my_dummy_mod"):
        res = find_module_from_package("my-dummy-mod")
        assert res == "my_dummy_mod"


@patch("subprocess.run")
def test_run_trace(mock_run):
    """Verifies that run_trace executes python with -X importtime and writes logs."""
    run_trace_helper = getattr(profiler, "run_trace", None)
    if run_trace_helper is None:
        pytest.skip("run_trace is not exported at the module level.")

    # Mock subprocess output
    mock_run.return_value = MagicMock(
        stdout="", stderr="importtime: dummy trace output", returncode=0
    )

    with patch("builtins.open", mock_open()) as mock_file, patch(
        "builtins.print"
    ):
        run_trace_helper("math")

        # Verify that subprocess was invoked with -X importtime
        called_cmd = mock_run.call_args[0][0]
        assert "-X" in called_cmd
        assert "importtime" in called_cmd

        # Verify that it attempted to write the trace log file
        assert mock_file.called


# =====================================================================
# 2. WORKER TESTS (run_worker)
# =====================================================================


def test_run_worker_with_skip_line_count(capsys):
    """Verifies worker returns -1 for loaded_lines when flag is active."""
    dummy_module = "sys"
    run_worker(dummy_module, skip_line_count=True)
    captured = capsys.readouterr()

    assert "__METRICS__:" in captured.out
    metrics_line = [
        l for l in captured.out.splitlines() if l.startswith("__METRICS__:")
    ][0]
    metrics = json.loads(metrics_line.split("__METRICS__:", 1)[1])

    assert metrics["loaded_lines"] == -1


def test_run_worker_counts_lines_correctly(capsys):
    """Verifies worker correctly resolves paths and counts raw lines."""
    dummy_module = "math"
    mock_module = MagicMock()
    mock_module.__file__ = "/mock/path/dummy_module.py"
    dummy_content = "import os\nprint('hello')\nx = 1\n"

    class CustomModulesDict(dict):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._call_count = 0

        def keys(self):
            self._call_count += 1
            if self._call_count == 1:
                return {"math"}
            return {"math", "dummy_test_mod"}

    fake_modules = CustomModulesDict(
        {"math": sys.modules["math"], "dummy_test_mod": mock_module}
    )

    with patch("sys.modules", fake_modules), patch(
        "builtins.open", mock_open(read_data=dummy_content)
    ), patch("profiler.importlib.invalidate_caches"):

        run_worker(dummy_module, skip_line_count=False)
        captured = capsys.readouterr()

        metrics_line = [
            l for l in captured.out.splitlines() if l.startswith("__METRICS__:")
        ][0]
        metrics = json.loads(metrics_line.split("__METRICS__:", 1)[1])

        assert metrics["loaded_lines"] == 3


# =====================================================================
# 3. PARSER TESTS (_run_worker_and_parse)
# =====================================================================


def test_run_worker_and_parse_success():
    """Verifies master extracts metrics JSON block from worker stdout."""
    mock_stdout = (
        '__METRICS__:{"time_ms": 15.5, "peak_ram_mb": 12.0, "rss_ram_mb":'
        ' 10.0, "loaded_modules": 22, "loaded_lines": 120}\n'
    )
    mock_process = MagicMock(stdout=mock_stdout, stderr="")

    with patch("subprocess.run", return_value=mock_process):
        data = _run_worker_and_parse(["python", "profiler.py"])
        assert data["time_ms"] == 15.5
        assert data["loaded_lines"] == 120


def test_run_worker_and_parse_forwards_stderr(capsys):
    """Verifies worker stderr warnings are forwarded to master's stderr."""
    mock_stdout = (
        '__METRICS__:{"time_ms": 10.0, "peak_ram_mb": 12.0, "rss_ram_mb":'
        ' 10.0, "loaded_modules": 22, "loaded_lines": 120}'
    )
    mock_stderr = "DeprecationWarning: some_pkg is deprecated"
    mock_process = MagicMock(stdout=mock_stdout, stderr=mock_stderr)

    with patch("subprocess.run", return_value=mock_process):
        _run_worker_and_parse(["python", "profiler.py"])
        captured = capsys.readouterr()
        assert "DeprecationWarning: some_pkg is deprecated" in captured.err


# =====================================================================
# 4. MASTER COORDINATION & BENCHMARK INTEGRATIONS
# =====================================================================


@patch("profiler._run_worker_and_parse")
def test_run_master_skips_line_count_and_restores_metrics(mock_parse):
    """Verifies master appends --skip-line-count and restores metrics."""
    run_data_1 = {
        "loaded_modules": 5,
        "loaded_lines": 1000,
        "time_ms": 50.0,
        "peak_ram_mb": 10.0,
        "rss_ram_mb": 8.0,
    }
    run_data_2 = {
        "loaded_modules": 5,
        "loaded_lines": -1,
        "time_ms": 40.0,
        "peak_ram_mb": 10.0,
        "rss_ram_mb": 8.0,
    }
    mock_parse.side_effect = [run_data_1, run_data_2]

    with patch("builtins.print"), patch("sys.stderr"):
        run_master(
            iterations=2,
            target_module="dummy_mod",
            cpu=NO_CPU_PINNING,
            clear_cache=False,
        )

        second_cmd_args = mock_parse.call_args_list[1][0][0]
        assert "--skip-line-count" in second_cmd_args
        assert run_data_2["loaded_lines"] == 1000


@patch("profiler._run_worker_and_parse")
def test_run_master_checks_non_deterministic_behavior(mock_parse, capsys):
    """Verifies warnings are printed upon non-deterministic module loads."""
    mock_parse.side_effect = [
        {
            "loaded_modules": 50,
            "loaded_lines": 500,
            "time_ms": 10.0,
            "peak_ram_mb": 1.0,
            "rss_ram_mb": 1.0,
        },
        {
            "loaded_modules": 55,
            "loaded_lines": -1,
            "time_ms": 10.0,
            "peak_ram_mb": 1.0,
            "rss_ram_mb": 1.0,
        },
    ]

    run_master(
        iterations=2,
        target_module="dummy_mod",
        cpu=NO_CPU_PINNING,
        clear_cache=False,
    )
    captured = capsys.readouterr()
    assert "WARNING: Non-deterministic import behavior!" in captured.err


@patch("profiler._run_worker_and_parse")
def test_run_master_with_cpu_pinning(mock_parse):
    """Verifies taskset command configuration on Linux platforms."""
    mock_parse.return_value = {
        "loaded_modules": 10,
        "loaded_lines": 500,
        "time_ms": 12.0,
        "peak_ram_mb": 1.0,
        "rss_ram_mb": 1.0,
    }

    with patch("sys.platform", "linux"), patch("builtins.print"), patch(
        "sys.stderr"
    ):
        run_master(
            iterations=1, target_module="dummy_mod", cpu=1, clear_cache=False
        )

        args = mock_parse.call_args[0][0]
        assert "taskset" in args
        assert "1" in args


@patch("profiler._run_worker_and_parse")
def test_run_master_writes_csv_and_diffs_baseline(mock_parse, tmp_path):
    """Verifies benchmark results CSV writing, reading, and thresholds comparison."""
    mock_parse.return_value = {
        "loaded_modules": 10,
        "loaded_lines": 500,
        "time_ms": 12.0,
        "peak_ram_mb": 1.0,
        "rss_ram_mb": 1.0,
    }

    csv_file = tmp_path / "results.csv"
    baseline_file = tmp_path / "baseline.csv"

    # Write mock baseline CSV data
    with open(baseline_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "iteration",
                "time_ms",
                "peak_ram_mb",
                "rss_ram_mb",
                "loaded_modules",
                "loaded_lines",
            ]
        )
        writer.writerow([1, 10.0, 1.0, 1.0, 10, 500])

    with patch("builtins.print"):
        run_master(
            iterations=1,
            target_module="dummy_mod",
            cpu=NO_CPU_PINNING,
            csv_path=str(csv_file),
            diff_baseline=str(baseline_file),
            diff_threshold=50.0,
            clear_cache=False,
        )

    assert csv_file.exists()


def test_validate_module_name_valid():
    """Verifies validate_module_name passes valid identifiers."""
    from profiler import validate_module_name
    assert validate_module_name("google.cloud.storage") == "google.cloud.storage"


def test_validate_module_name_invalid():
    """Verifies validate_module_name raises ArgumentTypeError for invalid identifiers."""
    import argparse
    from profiler import validate_module_name
    with pytest.raises(argparse.ArgumentTypeError):
        validate_module_name("google.cloud; rm -rf /")


@patch("subprocess.run")
def test_run_cprofile(mock_run):
    """Verifies run_cprofile executes cProfile subprocess."""
    from profiler import run_cprofile
    mock_run.return_value = MagicMock(returncode=0)
    with patch("pstats.Stats"), patch("builtins.print"):
        run_cprofile("math")
    assert mock_run.called


@patch("multiprocessing.get_context")
def test_run_mprofile(mock_context):
    """Verifies run_mprofile spawns process for memory snapshot."""
    from profiler import run_mprofile
    mock_proc = MagicMock(exitcode=0)
    mock_context.return_value.Process.return_value = mock_proc
    with patch("builtins.print"):
        run_mprofile("math")
    assert mock_proc.start.called
    assert mock_proc.join.called


# =====================================================================
# 5. ADDITIONAL COVERAGE TESTS FOR 100% COVERAGE
# =====================================================================


def test_run_worker_file_path_edge_cases(capsys):
    dummy_module = "math"

    mod_none = MagicMock()
    mod_none.__file__ = None

    mod_pyc = MagicMock()
    mod_pyc.__file__ = "/mock/path/dummy.pyc"

    mod_pyc_err = MagicMock()
    mod_pyc_err.__file__ = "/mock/path/invalid.pyc"

    mod_os_err = MagicMock()
    mod_os_err.__file__ = "/mock/path/os_error.py"

    fake_modules = {
        "math": sys.modules["math"],
        "mod_none": mod_none,
        "mod_pyc": mod_pyc,
        "mod_pyc_err": mod_pyc_err,
        "mod_os_err": mod_os_err,
    }

    class CustomModulesDict(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._call_count = 0

        def keys(self):
            self._call_count += 1
            if self._call_count == 1:
                return {"math"}
            return {"math", "mod_none", "mod_pyc", "mod_pyc_err", "mod_os_err", "mod_key_err"}

        def __getitem__(self, key):
            if key == "mod_key_err":
                raise KeyError("mod_key_err")
            return super().__getitem__(key)

    def mock_source_from_cache(path):
        if "invalid" in path:
            raise ValueError("Invalid pyc path")
        return path.replace(".pyc", ".py")

    def mock_open_func(file_path, *args, **kwargs):
        if "os_error" in str(file_path):
            raise OSError("Permission denied")
        return mock_open(read_data="x = 1\n")(file_path, *args, **kwargs)

    with patch("sys.modules", CustomModulesDict(fake_modules)), \
         patch("importlib.util.source_from_cache", side_effect=mock_source_from_cache), \
         patch("builtins.open", side_effect=mock_open_func), \
         patch("profiler.importlib.invalidate_caches"):
        run_worker(dummy_module, skip_line_count=False)
        captured = capsys.readouterr()
        assert "WARNING: Failed to read lines" in captured.err


def test_run_worker_attribute_error(capsys):
    dummy_module = "math"

    class ModNoFile:
        @property
        def __file__(self):
            raise AttributeError("No __file__")

    class CustomModulesDict(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._call_count = 0

        def keys(self):
            self._call_count += 1
            if self._call_count == 1:
                return {"math"}
            return {"math", "mod_no_file"}

    fake_modules = CustomModulesDict({"math": sys.modules["math"], "mod_no_file": ModNoFile()})
    with patch("sys.modules", fake_modules), patch("profiler.importlib.invalidate_caches"):
        run_worker(dummy_module, skip_line_count=False)


def test_run_worker_and_parse_no_metrics_tag():
    mock_process = MagicMock(stdout="No metrics tag output\n", stderr="some stderr")
    with patch("subprocess.run", return_value=mock_process):
        with pytest.raises(ValueError, match="Worker did not output metrics JSON"):
            _run_worker_and_parse(["python", "profiler.py"])


def test_run_worker_and_parse_invalid_json():
    mock_process = MagicMock(stdout="__METRICS__:{invalid_json}\n", stderr="stderr info")
    with patch("subprocess.run", return_value=mock_process):
        with pytest.raises(json.JSONDecodeError):
            _run_worker_and_parse(["python", "profiler.py"])


def test_run_worker_and_parse_missing_key():
    mock_process = MagicMock(stdout='__METRICS__:{"time_ms": 10.0}\n', stderr="")
    with patch("subprocess.run", return_value=mock_process):
        with pytest.raises(KeyError, match="Missing key"):
            _run_worker_and_parse(["python", "profiler.py"])


def test_print_outputs_multiple_and_empty():
    from profiler import _print_outputs
    with patch("builtins.print") as mock_print:
        _print_outputs("math", 1, 10, 500, [], [], [])
        _print_outputs("math", 2, 10, 500, [10.0, 12.0], [1.0, 2.0], [1.0, 2.0])
        assert mock_print.called




def test_run_master_invalid_iterations():
    with pytest.raises(ValueError, match="Number of iterations must be at least 1"):
        run_master(0, "math")


def test_run_master_non_linux_cpu_pinning(capsys):
    with patch("sys.platform", "darwin"), patch("profiler._run_worker_and_parse") as mock_parse:
        mock_parse.return_value = {
            "loaded_modules": 5, "loaded_lines": 100, "time_ms": 10.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
        }
        run_master(1, "math", cpu=0, clear_cache=False)
        captured = capsys.readouterr()
        assert "WARNING: CPU pinning is only supported on Linux" in captured.out


def test_run_master_taskset_not_found():
    with patch("sys.platform", "linux"), patch("profiler._run_worker_and_parse", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            run_master(1, "math", cpu=0, clear_cache=False)


def test_run_master_called_process_error():
    err = subprocess.CalledProcessError(1, ["cmd"], stderr="Worker crashed")
    with patch("profiler._run_worker_and_parse", side_effect=err), patch("sys.stderr"):
        with pytest.raises(subprocess.CalledProcessError):
            run_master(1, "math", cpu=NO_CPU_PINNING, clear_cache=False)


@patch("profiler._run_worker_and_parse")
def test_run_master_diff_baseline_missing(mock_parse, capsys):
    mock_parse.return_value = {
        "loaded_modules": 5, "loaded_lines": 100, "time_ms": 10.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
    }
    code = run_master(1, "math", cpu=NO_CPU_PINNING, diff_baseline="/nonexistent/baseline.csv", clear_cache=False)
    captured = capsys.readouterr()
    assert "WARNING: Baseline CSV" in captured.out
    assert code == 0


@patch("profiler._run_worker_and_parse")
def test_run_master_diff_baseline_exceeds_absolute_within_relative(mock_parse, tmp_path, capsys):
    mock_parse.return_value = {
        "loaded_modules": 5, "loaded_lines": 100, "time_ms": 110.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
    }
    baseline_file = tmp_path / "baseline.csv"
    with open(baseline_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Iteration", "Time (ms)", "RAM", "RSS"])
        writer.writerow([1, 100.0, 1.0, 1.0])

    code = run_master(1, "math", cpu=NO_CPU_PINNING, diff_baseline=str(baseline_file), diff_threshold=5.0, clear_cache=False)
    captured = capsys.readouterr()
    assert "SUCCESS: Import time regression" in captured.out
    assert code == 0


@patch("profiler._run_worker_and_parse")
def test_run_master_diff_baseline_exceeds_both_thresholds(mock_parse, tmp_path, capsys):
    mock_parse.return_value = {
        "loaded_modules": 5, "loaded_lines": 100, "time_ms": 150.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
    }
    baseline_file = tmp_path / "baseline.csv"
    with open(baseline_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Iteration", "Time (ms)", "RAM", "RSS"])
        writer.writerow([1, 100.0, 1.0, 1.0])

    code = run_master(1, "math", cpu=NO_CPU_PINNING, diff_baseline=str(baseline_file), diff_threshold=5.0, clear_cache=False)
    captured = capsys.readouterr()
    assert "FAILURE: Import time regression" in captured.out
    assert code == 1


@patch("profiler._run_worker_and_parse")
def test_run_master_fail_threshold_bypassed(mock_parse, tmp_path, capsys):
    mock_parse.return_value = {
        "loaded_modules": 5, "loaded_lines": 100, "time_ms": 200.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
    }
    baseline_file = tmp_path / "baseline.csv"
    with open(baseline_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Iteration", "Time (ms)", "RAM", "RSS"])
        writer.writerow([1, 150.0, 1.0, 1.0])

    code = run_master(1, "math", cpu=NO_CPU_PINNING, fail_threshold=100.0, diff_baseline=str(baseline_file), diff_threshold=100.0, clear_cache=False)
    captured = capsys.readouterr()
    assert "Bypassing absolute backstop failure" in captured.out
    assert code == 0


@patch("profiler._run_worker_and_parse")
def test_run_master_fail_threshold_passed_and_failed(mock_parse, capsys):
    # Test passed fail_threshold
    mock_parse.return_value = {
        "loaded_modules": 5, "loaded_lines": 100, "time_ms": 50.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
    }
    code_pass = run_master(1, "math", cpu=NO_CPU_PINNING, fail_threshold=100.0, clear_cache=False)
    captured_pass = capsys.readouterr()
    assert "SUCCESS: Median import time" in captured_pass.out
    assert code_pass == 0

    # Test failed fail_threshold
    mock_parse.return_value = {
        "loaded_modules": 5, "loaded_lines": 100, "time_ms": 200.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0
    }
    code_fail = run_master(1, "math", cpu=NO_CPU_PINNING, fail_threshold=100.0, clear_cache=False)
    captured_fail = capsys.readouterr()
    assert "FAILURE: Median import time" in captured_fail.out
    assert code_fail == 1


@patch("subprocess.run")
def test_run_trace_failed(mock_run, capsys):
    from profiler import run_trace
    mock_run.return_value = MagicMock(returncode=1, stdout="out", stderr="err")
    with patch("builtins.open", mock_open()):
        run_trace("math")
    captured = capsys.readouterr()
    assert "WARNING: Import failed" in captured.err


@patch("subprocess.run")
def test_run_cprofile_failed(mock_run, capsys):
    from profiler import run_cprofile
    mock_run.return_value = MagicMock(returncode=1, stderr="cprofile err")
    run_cprofile("math")
    captured = capsys.readouterr()
    assert "Error generating cProfile data" in captured.err


def test_mprofile_worker():
    from profiler import _mprofile_worker
    with patch("builtins.print"):
        _mprofile_worker("math")


@patch("multiprocessing.get_context")
def test_run_mprofile_failed(mock_context, capsys):
    from profiler import run_mprofile
    mock_proc = MagicMock(exitcode=1)
    mock_context.return_value.Process.return_value = mock_proc
    run_mprofile("math")
    captured = capsys.readouterr()
    assert "Error generating memory snapshot" in captured.err


def test_find_module_from_package_metadata_init():
    with patch("importlib.metadata.files", return_value=["foo/bar/__init__.py"]), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("foo-bar")
        assert res == "foo.bar"


def test_find_module_from_package_metadata_test_utils():
    with patch("importlib.metadata.files", return_value=["test_utils/__init__.py"]), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("google-cloud-testutils")
        assert res == "test_utils"


def test_find_module_from_package_setuptools():
    sys.modules.setdefault("setuptools", MagicMock())
    def mock_isfile(path):
        return "my_pkg" in path
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("profiler.os.path.exists", return_value=True), \
         patch("profiler.os.path.isdir", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["google", "google.cloud", "tests.dummy", "my_pkg"]), \
         patch("profiler.os.path.isfile", side_effect=mock_isfile), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("my-pkg")
        assert res == "my_pkg"


def test_find_module_from_package_setuptools_test_utils():
    sys.modules.setdefault("setuptools", MagicMock())
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("profiler.os.path.exists", return_value=True), \
         patch("profiler.os.path.isdir", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["test_utils", "tests"]) as mock_find, \
         patch("profiler.os.path.isfile", return_value=True), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("google-cloud-testutils")
        assert res == "test_utils"
        mock_find.assert_called_once_with(where="src")


def test_find_module_from_package_setuptools_not_file_and_exception():
    sys.modules.setdefault("setuptools", MagicMock())
    def mock_isfile(path):
        if "a_pkg" in path:
            return False
        return True

    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["a_pkg", "my_pkg"]), \
         patch("os.path.isfile", side_effect=mock_isfile), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("my-pkg")
        assert res == "my_pkg"

def test_find_module_from_package_oserror_handling(capsys):
    sys.modules.setdefault("setuptools", MagicMock())
    def mock_isfile(path):
        if "bad_pkg" in path:
            raise OSError("Permission denied")
        return False

    def mock_listdir(path):
        if "bad_pkg" in path:
            raise OSError("Access denied")
        return ["mod.py"]

    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["bad_pkg", "good_pkg"]), \
         patch("os.path.isfile", side_effect=mock_isfile), \
         patch("os.listdir", side_effect=mock_listdir), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("my-pkg")
        assert res == "good_pkg"

    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("setuptools.find_namespace_packages", side_effect=RuntimeError("setuptools failure")):
        res = find_module_from_package("my-pkg")
        assert res == "my.pkg"
        captured = capsys.readouterr()
        assert "WARNING: Package discovery failed: setuptools failure" in captured.err


def test_find_module_from_package_namespace_package_no_init():
    sys.modules.setdefault("setuptools", MagicMock())
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["google.api"]), \
         patch("os.path.isfile", return_value=False), \
         patch("os.listdir", return_value=["http_pb2.py"]), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("googleapis-common-protos")
        assert res == "google.api"


def test_find_module_from_package_src_layout():
    sys.modules.setdefault("setuptools", MagicMock())
    def mock_isdir(path):
        return path == "src" or path == "."
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", side_effect=mock_isdir), \
         patch("setuptools.find_namespace_packages", return_value=["google_crc32c"]), \
         patch("os.path.isfile", return_value=True), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("google-crc32c")
        assert res == "google_crc32c"


def test_find_module_from_package_exception_in_find_spec():
    sys.modules.setdefault("setuptools", MagicMock())
    def mock_find_spec(mod):
        raise Exception("Find spec error")

    # Exception during metadata lookup falls back
    with patch("importlib.metadata.files", return_value=["foo/bar/__init__.py"]), \
         patch("importlib.util.find_spec", side_effect=mock_find_spec), \
         patch("setuptools.find_namespace_packages", side_effect=Exception):
        res = find_module_from_package("foo-bar")
        assert res == "foo.bar"

    # Exception during setuptools __init__.py lookup falls back
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["foo_bar"]), \
         patch("os.path.isfile", return_value=True), \
         patch("importlib.util.find_spec", side_effect=mock_find_spec):
        res = find_module_from_package("foo-bar")
        assert res == "foo.bar"

    # Exception during setuptools namespace package lookup falls back
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["foo_bar"]), \
         patch("os.path.isfile", return_value=False), \
         patch("os.listdir", return_value=["mod.py"]), \
         patch("importlib.util.find_spec", side_effect=mock_find_spec):
        res = find_module_from_package("foo-bar")
        assert res == "foo.bar"



def test_cli_main_options():
    import runpy

    profiler_path = profiler.__file__

    # Test --module CLI
    with patch("sys.argv", ["profiler.py", "--module=math", "--iterations=1"]), \
         patch("profiler._run_worker_and_parse", return_value={"loaded_modules": 1, "loaded_lines": 10, "time_ms": 1.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0}), \
         patch("builtins.print"):
        with pytest.raises(SystemExit) as exc:
            runpy.run_path(profiler_path, run_name="__main__")
        assert exc.value.code == 0

    # Test --package CLI
    with patch("sys.argv", ["profiler.py", "--package=math", "--iterations=1"]), \
         patch("profiler._run_worker_and_parse", return_value={"loaded_modules": 1, "loaded_lines": 10, "time_ms": 1.0, "peak_ram_mb": 1.0, "rss_ram_mb": 1.0}), \
         patch("builtins.print"):
        with pytest.raises(SystemExit) as exc:
            runpy.run_path(profiler_path, run_name="__main__")
        assert exc.value.code == 0

    # Test --worker CLI
    with patch("sys.argv", ["profiler.py", "--module=math", "--worker", "--skip-line-count"]), \
         patch("builtins.print"):
        runpy.run_path(profiler_path, run_name="__main__")

    # Test --trace CLI
    with patch("sys.argv", ["profiler.py", "--module=math", "--trace"]), \
         patch("subprocess.run") as mock_run, \
         patch("builtins.open", mock_open()), \
         patch("builtins.print"):
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        runpy.run_path(profiler_path, run_name="__main__")

    # Test --cprofile CLI
    with patch("sys.argv", ["profiler.py", "--module=math", "--cprofile"]), \
         patch("subprocess.run") as mock_run, \
         patch("pstats.Stats"), \
         patch("builtins.print"):
        mock_run.return_value = MagicMock(returncode=0)
        runpy.run_path(profiler_path, run_name="__main__")

    # Test --mprofile CLI
    with patch("sys.argv", ["profiler.py", "--module=math", "--mprofile"]), \
         patch("multiprocessing.get_context") as mock_ctx, \
         patch("builtins.print"):
        mock_proc = MagicMock(exitcode=0)
        mock_ctx.return_value.Process.return_value = mock_proc
        runpy.run_path(profiler_path, run_name="__main__")


def test_should_process_namespace_package():
    from profiler import _should_process_namespace_package

    # Standard non-library top-level directories should NOT be processed
    assert _should_process_namespace_package("tests", "google-cloud-storage") is False
    assert _should_process_namespace_package("samples", "google-cloud-storage") is False
    assert _should_process_namespace_package("test_utils", "google-cloud-storage") is False
    assert _should_process_namespace_package("test_helpers", "google-cloud-storage") is False

    # Exception: Target package explicitly contains the top-level directory name (e.g. google-cloud-testutils -> test_utils)
    assert _should_process_namespace_package("test_utils", "google-cloud-testutils") is True

    # Valid library package top-level should be processed
    assert _should_process_namespace_package("google", "google-cloud-storage") is True
    assert _should_process_namespace_package("my_library", "my-library") is True


def test_find_module_from_package_testutils():
    """Verifies that google-cloud-testutils correctly resolves to test_utils namespace package."""
    sys.modules.setdefault("setuptools", MagicMock())
    def mock_isfile(path):
        return "test_utils" in path
    with patch("importlib.metadata.files", side_effect=Exception), \
         patch("profiler.os.path.exists", return_value=True), \
         patch("profiler.os.path.isdir", return_value=True), \
         patch("setuptools.find_namespace_packages", return_value=["google", "google.cloud", "tests", "test_utils"]) as mock_find, \
         patch("profiler.os.path.isfile", side_effect=mock_isfile), \
         patch("importlib.util.find_spec", return_value=True):
        res = find_module_from_package("google-cloud-testutils")
        assert res == "test_utils"
        mock_find.assert_called_once_with(where="src")




