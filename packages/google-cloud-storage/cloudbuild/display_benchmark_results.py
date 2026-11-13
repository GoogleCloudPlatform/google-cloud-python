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

    print("\n" + "=" * 88)
    print("                 GCS DIRECTPATH READ BENCHMARK PERFORMANCE RESULTS")
    print("=" * 88)
    header = f"| {'Workload Pattern':<36} | {'Avg Throughput':<17} | {'Network Bandwidth':<22} | {'CPU Usage':<9} |"
    print(header)
    print("|" + "-" * 38 + "|" + "-" * 19 + "|" + "-" * 24 + "|" + "-" * 11 + "|")
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
        print(
            f"| {name:<36} | {str(avg_mib) + ' MiB/s':<17} | {net_str:<22} | {str(cpu):<9} |"
        )
    print("=" * 88 + "\n")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/report/bench_result.json"
    display_results(path)
