# Python SDK Import Profiler: Documentation & Breakdown

This document provides a comprehensive guide to the `import_profiler` scripts, directory files, and how to analyze the generated import trace logs to target optimization areas.

---

## 1. File Guide & Directory Structure
The profiling tool is located in the [scripts/import_profiler/](./) directory:

* **[profiler.py](./profiler.py)**: The core executable script. It is designed as a single-file, self-spawning harness that performs process-isolated importing benchmarks and generates trace logs.

---

## 2. Profiler Mechanism (`profiler.py`)

**Objective**
The Profiler functions as a process-isolated verification harness designed to capture before-and-after metrics across three distinct vectors: Initialization Latency (ms), Peak Memory Usage (MB), and Dynamic Code Volume (Loaded Modules & Lines of Code).

**Usage**

Run this command to collect the metrics:
```bash
python profiler.py --module <target_module> --iterations <N>
```

**Expected Output**
```text
--- Results for <target_module> (<N> iterations) ---
Code Volume (Deterministic):
  Loaded Modules: <count>
  Loaded Lines:   <count>
Time (ms):
  P50 (Median): <time>
  P90:          <time>
  P99:          <time>
RAM (MB):
  P50 (Median): <memory>
  P90:          <memory>
  P99:          <memory>
```

---

## 3. How to Interpret Python `-X importtime` Trace Logs
When running with the `--trace` flag, the script captures the raw stderr trace produced by Python's `-X importtime` option. The trace looks like this:

```
import time: self [us] | cumulative | imported package
import time:       536 |        536 |   _io
import time:      1077 |       2385 | _frozen_importlib_external
import time:    773659 |     793010 |                   google.cloud.compute_v1.types.compute
```

### Explaining the Fields:
1. **`self [us]` (Microseconds):** The time spent importing the module itself, *excluding* any time spent importing its child dependencies.
2. **`cumulative` (Microseconds):** The total time spent loading the module *including* all nested imports. This represents the total wait time introduced by this line.
3. **Hierarchy Indentation:** Indented packages are sub-imports triggered by the parent module. A package with higher indentation is loaded deeper in the call stack.

---

## 4. Execution Reference
Ensure you are in the correct pyenv virtual environment where packages are installed in editable mode:

```bash
# 1. Run the profiler to get baseline/optimized outcomes (e.g. 5 iterations)
PYENV_VERSION=py312 python profiler.py --module=google.cloud.compute --iterations=5
PYENV_VERSION=py312 python profiler.py --module=google.cloud.aiplatform --iterations=5

# 2. Run the profiler to generate trace logs
PYENV_VERSION=py312 python profiler.py --module=google.cloud.compute --trace
PYENV_VERSION=py312 python profiler.py --module=google.cloud.aiplatform --trace
```
