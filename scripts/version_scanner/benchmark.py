# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import random
import subprocess
import sys
import tempfile
import time
from typing import List, Dict

def get_package_subset(packages_dir: str, count: int) -> List[str]:
    """
    Get a randomized subset of package names from the specified directory.
    
    Args:
        packages_dir: Path to the directory containing packages.
        count: Number of packages to return.
        
    Returns:
        A list of package directory names.
    """
    all_packages = [d for d in os.listdir(packages_dir) if os.path.isdir(os.path.join(packages_dir, d))]
        
    if count >= len(all_packages):
        return all_packages
        
    return random.sample(all_packages, count)

def run_benchmark(
    scanner_path: str,
    root_path: str,
    package_file: str,
    dependency: str,
    version: str
) -> float:
    """
    Run the scanner and return the duration in seconds.
    """
    cmd = [
        "python3", scanner_path,
        "-d", dependency,
        "-v", version,
        "-p", root_path,
        "--package-file", package_file
    ]
    
    start_time = time.perf_counter()
    
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running benchmark: {e}")
        return -1.0
        
    duration = time.perf_counter() - start_time
    return duration

def run_benchmarks(
    scanner_path: str,
    root_path: str,
    packages_dir: str,
    counts: List[int],
    dependency: str,
    version: str
) -> Dict[int, float]:
    """Runs benchmarks for specified counts and returns a dict of results."""
    results = {}
    
    for count in counts:
        subset = get_package_subset(packages_dir, count)
        print(f"  Testing {len(subset)} packages (e.g., {subset[:3]}...)")
        
        # Create temp package file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            for pkg in subset:
                f.write(f"packages/{pkg}\n")
            pkg_file = f.name
                
        try:
            duration = run_benchmark(scanner_path, root_path, pkg_file, dependency, version)
            results[count] = duration
        finally:
            # Clean up
            if os.path.exists(pkg_file):
                os.remove(pkg_file)
            
    return results

def main():
    parser = argparse.ArgumentParser(description="Benchmark the version scanner.")
    
    parser.add_argument(
        "-s", "--scanner-path",
        default="version_scanner.py",
        help="Path to version_scanner.py"
    )
    
    parser.add_argument(
        "-r", "--root-path",
        required=True,
        help="Path to the monorepo root directory"
    )
    
    parser.add_argument(
        "-p", "--packages-dir",
        help="Path to packages directory (defaults to <root-path>/packages)"
    )
    
    parser.add_argument(
        "-d", "--dependency",
        default="python",
        help="Dependency to search for"
    )
    
    parser.add_argument(
        "-v", "--version",
        default="3.7",
        help="Version to search for"
    )
    
    parser.add_argument(
        "-c", "--counts",
        default="1,10,50",
        help="Comma-separated list of package counts to test"
    )
    
    args = parser.parse_args()
    
    packages_dir = args.packages_dir or os.path.join(args.root_path, "packages")
    
    if not os.path.exists(packages_dir):
        print(f"Error: Packages directory not found: {packages_dir}", file=sys.stderr)
        sys.exit(1)
        
    counts = [int(c) for c in args.counts.split(',')]
    
    all_packages = [d for d in os.listdir(packages_dir) if os.path.isdir(os.path.join(packages_dir, d))]
        
    total_packages = len(all_packages)
    
    print(f"Found {total_packages} packages in {packages_dir}")
    
    # Filter counts that are greater than total packages
    counts = [c for c in counts if c <= total_packages]
    # Add total if not already there
    if total_packages not in counts:
        counts.append(total_packages)
        
    print(f"Running benchmarks for counts: {counts}")
    
    results = run_benchmarks(
        scanner_path=args.scanner_path,
        root_path=args.root_path,
        packages_dir=packages_dir,
        counts=counts,
        dependency=args.dependency,
        version=args.version
    )
    
    print("\nBenchmark Results:")
    print(f"{'Packages':<10} | {'Time (seconds)':<15}")
    print("-" * 30)
    for count, duration in results.items():
        print(f"{count:<10} | {duration:<15.4f}")

if __name__ == "__main__":
    main()
