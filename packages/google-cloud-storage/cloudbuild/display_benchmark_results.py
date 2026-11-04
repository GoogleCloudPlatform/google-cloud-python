# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper script to format and display GCS benchmark performance results."""

import json
import os
import sys


def display_results(result_path: str) -> None:
    """Reads benchmark JSON result and prints a formatted summary table."""
    if not os.path.exists(result_path):
        print(
            f"ERROR: Benchmark result file not found at {result_path}", file=sys.stderr
        )
        sys.exit(1)

    with open(result_path) as f:
        data = json.load(f)

    if not isinstance(data, dict):
        print(
            "ERROR: Invalid JSON structure in benchmark result file.", file=sys.stderr
        )
        sys.exit(1)

    benchmarks = data.get("benchmarks", [])
    if not isinstance(benchmarks, list) or not benchmarks:
        print("No benchmarks found in result file.")
        sys.exit(0)

    rows = []
    for b in benchmarks:
        if not isinstance(b, dict):
            continue
        name = (
            b.get("name", "")
            .replace("test_downloads_multi_proc_multi_coro[", "")
            .replace("]", "")
        )
        extra = b.get("extra_info", {})
        if not isinstance(extra, dict):
            extra = {}
        avg_mib = extra.get("avg_throughput_mib_s", "N/A")
        net_mb = extra.get("net_throughput_mb_s")
        if net_mb:
            try:
                net_str = (
                    f"{float(net_mb):,.1f} MB/s ({float(net_mb) * 0.008:.1f} Gbps)"
                )
            except Exception:
                net_str = str(net_mb)
        else:
            net_str = "N/A"
        cpu = extra.get("cpu_max_global", "N/A")
        rows.append((name, f"{avg_mib} MiB/s", net_str, str(cpu)))

    if not rows:
        print("No benchmarks found in result file.")
        sys.exit(0)

    name_width = max([36] + [len(row[0]) for row in rows])
    avg_width = max([17] + [len(row[1]) for row in rows])
    net_width = max([22] + [len(row[2]) for row in rows])
    cpu_width = max([9] + [len(row[3]) for row in rows])
    table_width = name_width + avg_width + net_width + cpu_width + 13

    print("\n" + "=" * table_width)
    print("GCS DIRECTPATH READ BENCHMARK PERFORMANCE RESULTS".center(table_width))
    print("=" * table_width)
    header = (
        f"| {'Workload Pattern':<{name_width}} "
        f"| {'Avg Throughput':<{avg_width}} "
        f"| {'Network Bandwidth':<{net_width}} "
        f"| {'CPU Usage':<{cpu_width}} |"
    )
    print(header)
    print(
        "|"
        + "-" * (name_width + 2)
        + "|"
        + "-" * (avg_width + 2)
        + "|"
        + "-" * (net_width + 2)
        + "|"
        + "-" * (cpu_width + 2)
        + "|"
    )
    for name, avg_str, net_str, cpu_str in rows:
        print(
            f"| {name:<{name_width}} "
            f"| {avg_str:<{avg_width}} "
            f"| {net_str:<{net_width}} "
            f"| {cpu_str:<{cpu_width}} |"
        )
    print("=" * table_width + "\n")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/report/bench_result.json"
    display_results(path)
