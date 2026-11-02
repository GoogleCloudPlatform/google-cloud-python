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

import os
import pytest
from unittest.mock import patch
from benchmark import get_package_subset, run_benchmark, run_benchmarks

def test_get_package_subset(tmp_path):
    # Create mock packages directory
    packages_dir = tmp_path / "packages"
    packages_dir.mkdir()
    
    for i in range(10):
        (packages_dir / f"pkg_{i}").mkdir()
        
    # Test getting a subset of 5
    subset = get_package_subset(str(packages_dir), 5)
    assert len(subset) == 5
    for pkg in subset:
        assert pkg.startswith("pkg_")
        
def test_get_package_subset_all(tmp_path):
    packages_dir = tmp_path / "packages"
    packages_dir.mkdir()
    
    for i in range(5):
        (packages_dir / f"pkg_{i}").mkdir()
        
    # Test getting all
    subset = get_package_subset(str(packages_dir), 10) # Request more than available
    assert len(subset) == 5 # Should return all available

def test_run_benchmark(tmp_path):
    # Create a dummy package file
    package_file = tmp_path / "packages.txt"
    package_file.write_text("pkg1\n")
    
    # Create dummy package directory
    packages_dir = tmp_path / "packages"
    packages_dir.mkdir()
    (packages_dir / "pkg1").mkdir()
    (packages_dir / "pkg1" / "test.py").write_text("version = '3.7'\n")
    
    scanner_path = "version_scanner.py"
    
    duration = run_benchmark(
        scanner_path=scanner_path,
        root_path=str(tmp_path),
        package_file=str(package_file),
        dependency="python",
        version="3.7"
    )
    
    assert isinstance(duration, float)
    assert duration >= 0

# Test run_benchmarks
@patch('benchmark.run_benchmark')
def test_run_benchmarks(mock_run, tmp_path):
    mock_run.return_value = 1.5
    
    packages_dir = tmp_path / "packages"
    packages_dir.mkdir()
    for i in range(5):
        (packages_dir / f"pkg_{i}").mkdir()
        
    results = run_benchmarks(
        scanner_path="dummy.py",
        root_path=str(tmp_path),
        packages_dir=str(packages_dir),
        counts=[1, 3],
        dependency="python",
        version="3.7"
    )
    
    assert len(results) == 2
    assert results[1] == 1.5
    assert results[3] == 1.5
    assert mock_run.call_count == 2
