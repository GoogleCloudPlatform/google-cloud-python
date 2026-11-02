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

import csv
import os
import subprocess
import pytest

def test_integration_scan(tmp_path):
    # Paths to real tools
    scanner_path = os.path.abspath("version_scanner.py")
    config_path = os.path.abspath("regex_pattern_config.yaml")
    
    # Static data directory
    data_dir = os.path.abspath("tests/data")
    
    # Run the scanner in the tmp_path so the output file is created there
    cmd = [
        "python3", scanner_path,
        "-d", "python",
        "-v", "3.7",
        "-p", data_dir,
        "--config", config_path,
        "-o", "scanner_report.csv",
        "--soft-fail"
    ]
    
    result = subprocess.run(cmd, cwd=tmp_path, capture_output=True, text=True, check=True)
    
    report_file = tmp_path / "scanner_report.csv"
    assert report_file.exists(), f"Report file not found. Stderr: {result.stderr}"
    
    with open(report_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    # We expect at least some matches when we build the data directory
    assert len(rows) > 0
