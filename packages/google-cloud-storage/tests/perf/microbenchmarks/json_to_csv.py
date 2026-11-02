import argparse
import csv
import json
import logging

import numpy as np

MB = 1024 * 1024


def _process_benchmark_result(bench, headers, extra_info_headers, stats_headers):
    """
    Process a single benchmark result and prepare it for CSV reporting.

    This function extracts relevant statistics and metadata from a benchmark
    run, calculates derived metrics like percentiles and throughput, and
    formats it as a dictionary.

    Args:
        bench (dict): The dictionary for a single benchmark from the JSON output.
        headers (list): The list of all header names for the CSV.
        extra_info_headers (list): Headers from the 'extra_info' section.
        stats_headers (list): Headers from the 'stats' section.

    """
    row = {h: "" for h in headers}
    row["name"] = bench.get("name", "")
    row["group"] = bench.get("group", "")

    extra_info = bench.get("extra_info", {})

    # Populate extra_info and stats
    for key in extra_info_headers:
        row[key] = extra_info.get(key)
    for key in stats_headers:
        row[key] = bench.get("stats", {}).get(key)

    # Handle threads/coros mapping
    if "threads" in row:
        row["threads"] = extra_info.get("num_coros", extra_info.get("coros"))

    # Calculate percentiles
    timings = bench.get("stats", {}).get("data")
    if timings:
        row["p90"] = np.percentile(timings, 90)
        row["p95"] = np.percentile(timings, 95)
        row["p99"] = np.percentile(timings, 99)

    # Calculate max throughput
    file_size = extra_info.get("file_size_bytes", extra_info.get("file_size", 0))
    num_files = extra_info.get("num_files", 1)
    total_bytes = file_size * num_files

    min_time = bench.get("stats", {}).get("min")
    if min_time and min_time > 0:
        row["max_throughput_mb_s"] = (total_bytes / min_time) / MB
    else:
        row["max_throughput_mb_s"] = 0.0

    return row


def _generate_report(json_path, csv_path):
    """Generate a CSV summary report from the pytest-benchmark JSON output.

    Args:
        json_path (str): The path to the JSON file containing benchmark results.
        csv_path (str): The path where the CSV report will be saved.

    Returns:
        str: The path to the generated CSV report file.

    """
    logging.info(f"Generating CSV report from {json_path}")

    with open(json_path, "r") as f:
        data = json.load(f)

    benchmarks = data.get("benchmarks", [])
    if not benchmarks:
        logging.warning("No benchmarks found in the JSON file.")
        return

    # headers order - name	group	block_size	bucket_name	bucket_type	chunk_size	cpu_max_global	file_size	mem_max	net_throughput_mb_s	num_files	pattern	processes	rounds	threads	vcpus	min	max	mean	median	stddev	p90	p95	p99	max_throughput_mb_s
    # if there are any other column keep it at the afterwards.
    ordered_headers = [
        "name",
        "group",
        "block_size",
        "bucket_name",
        "bucket_type",
        "chunk_size",
        "cpu_max_global",
        "file_size",
        "mem_max",
        "net_throughput_mb_s",
        "num_files",
        "pattern",
        "processes",
        "rounds",
        "threads",
        "vcpus",
        "min",
        "max",
        "mean",
        "median",
        "stddev",
        "p90",
        "p95",
        "p99",
        "max_throughput_mb_s",
    ]

    # Gather all available headers from the data
    all_available_headers = set(["name", "group"])
    stats_headers = ["min", "max", "mean", "median", "stddev"]
    custom_headers = ["p90", "p95", "p99", "max_throughput_mb_s"]

    all_available_headers.update(stats_headers)
    all_available_headers.update(custom_headers)

    extra_info_keys = set()
    for bench in benchmarks:
        if "extra_info" in bench and isinstance(bench["extra_info"], dict):
            extra_info_keys.update(bench["extra_info"].keys())
    all_available_headers.update(extra_info_keys)

    # Construct the final header list
    final_headers = list(ordered_headers)

    # Add any headers from the data that are not in the ordered list
    for header in sorted(list(all_available_headers)):
        if header not in final_headers:
            final_headers.append(header)

    # We still need the full list of extra_info headers for _process_benchmark_result
    extra_info_headers = sorted(list(extra_info_keys))

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(final_headers)

        for bench in benchmarks:
            row = _process_benchmark_result(
                bench, final_headers, extra_info_headers, stats_headers
            )
            writer.writerow([row.get(h, "") for h in final_headers])

    logging.info(f"CSV report generated at {csv_path}")
    return csv_path


def main():
    """
    Converts a JSON benchmark file to a CSV file.

    The CSV file will contain the 'name' of each benchmark and all fields
    from the 'extra_info' section.
    """
    parser = argparse.ArgumentParser(description="Convert benchmark JSON to CSV.")
    parser.add_argument(
        "--input_file",
        nargs="?",
        default="output.json",
        help="Path to the input JSON file (default: output.json)",
    )
    parser.add_argument(
        "--output_file",
        nargs="?",
        default="output.csv",
        help="Path to the output CSV file (default: output.csv)",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        _generate_report(args.input_file, args.output_file)
        print(f"Successfully converted {args.input_file} to {args.output_file}")
    except FileNotFoundError:
        logging.error(f"Error: Input file not found at {args.input_file}")
    except json.JSONDecodeError:
        logging.error(f"Error: Could not decode JSON from {args.input_file}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
