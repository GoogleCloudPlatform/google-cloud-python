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
import re
from unittest import mock
from unittest.mock import patch
import pytest
import yaml
from version_scanner import (
    ConfigManager, 
    scan_file, 
    write_csv_report,
    _truncate_context,
    _wrap_sheet_hyperlink,
    _wrap_sheet_string,
    _safe_int,
    format_for_raw_csv,
    format_for_spreadsheet,
    format_for_console
)

@pytest.fixture
def sample_match():
    return {
        "file_name": "setup.py",
        "file_path": "google-cloud-python/main/packages/pkg_a/setup.py",
        "repo_path": "packages/pkg_a/setup.py",
        "package_name": "pkg_a",
        "rule_name": "python_requires_check",
        "line_number": "123",
        "matched_string": "3.7",
        "context_line": "python_requires = '>=3.7'",
        "dependency": "python",
        "version": "3.7"
    }


@pytest.mark.parametrize(
    "exception_to_raise, required, silent_missing, expected_exit, expected_output, expected_return",
    [
        (None, True, False, False, None, "file content"),  # Success
        (FileNotFoundError(), True, True, False, None, None),  # Silent missing FileNotFoundError
        (FileNotFoundError(), True, False, True, "Error: Test_desc not found", None),  # Required FileNotFoundError
        (FileNotFoundError(), False, False, False, "Warning: Test_desc not found", None),  # Optional FileNotFoundError
        (PermissionError(), True, False, True, "Error: Permission denied reading test_desc", None),  # Required PermissionError
        (PermissionError(), False, False, False, "Warning: Permission denied reading test_desc", None),  # Optional PermissionError
        (IOError("disk full"), True, False, True, "Error reading test_desc", None),  # Required IOError
        (IOError("disk full"), False, False, False, "Warning: Error reading test_desc", None),  # Optional IOError
        (ValueError("invalid bytes"), True, False, True, "Error reading test_desc", None),  # Required ValueError
        (ValueError("invalid bytes"), False, False, False, "Warning: Error reading test_desc", None),  # Optional ValueError
    ]
)
def test_safe_read_file_scenarios(
    capsys, exception_to_raise, required, silent_missing, expected_exit, expected_output, expected_return
):
    from version_scanner import _safe_read_file
    
    if exception_to_raise:
        mock_open = mock.mock_open()
        mock_open.side_effect = exception_to_raise
    else:
        mock_open = mock.mock_open(read_data="file content")
        
    with patch("builtins.open", mock_open):
        if expected_exit:
            with pytest.raises(SystemExit) as excinfo:
                _safe_read_file("dummy.txt", required=required, description="test_desc", silent_missing=silent_missing)
            assert excinfo.value.code == 1
        else:
            res = _safe_read_file("dummy.txt", required=required, description="test_desc", silent_missing=silent_missing)
            assert res == expected_return
            
    if expected_output:
        captured = capsys.readouterr()
        assert expected_output in captured.err


# Test ConfigManager
@pytest.mark.parametrize("dependency, version, expected", [
    (
        "python", 
        "3.7", 
        {"name": "python", "version": "3.7", "major": "3", "minor": "7", "minor_plus_one": "8", "minor_minus_one": "6"}
    ),
    (
        "protobuf", 
        "4.25.8", 
        {"name": "protobuf", "version": "4.25.8", "major": "4", "minor": "25", "patch": "8", "minor_plus_one": "26", "minor_minus_one": "24"}
    ),
    (
        "foo", 
        "3", 
        {"name": "foo", "version": "3", "major": "3"}
    ),
])
def test_compute_variables(dependency, version, expected):
    cm = ConfigManager("dummy_path", dependency, version)
    vars = cm._compute_variables()
    assert vars == expected

# Test scan_file
def test_scan_file_positive(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("python_requires = '>=3.7'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]")}
    ]
    
    results = scan_file(str(test_file), rules)
    assert len(results) == 1
    assert results[0]["rule_name"] == "python_requires_check"
    assert results[0]["line_number"] == 1
    assert results[0]["matched_string"] == "python_requires = '>=3.7'"

def test_scan_file_negative(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("python_requires = '>=3.8'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]")}
    ]
    
    results = scan_file(str(test_file), rules)
    assert len(results) == 0

def test_scan_file_ignores_pragma(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("python_requires = '>=3.7'  # version-scanner: ignore\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]")}
    ]
    
    results = scan_file(str(test_file), rules)
    assert len(results) == 0


def test_scan_file_ignores_targeted_pragma(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("python_requires = '>=3.7'  # version-scanner: ignore-rule=python_requires_check:3.7\n")
    
    rules = [
        {
            "name": "python_requires_check", 
            "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]"),
            "version": "3.7"
        }
    ]
    
    results = scan_file(str(test_file), rules)
    assert len(results) == 0


def test_scan_file_handles_non_string_rule_name_and_version(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("python_requires = '>=3.7'  # version-scanner: ignore-rule=123:3.7\n")
    
    rules = [
        {
            "name": 123,  # Integer rule name
            "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]"),
            "version": 3.7 # Float version
        }
    ]
    
    # This should not raise TypeError
    results = scan_file(str(test_file), rules)
    assert len(results) == 0



def test_scan_file_does_not_ignore_mismatched_targeted_pragma(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("python_requires = '>=3.7'  # version-scanner: ignore-rule=python_requires_check:3.8\n")
    
    rules = [
        {
            "name": "python_requires_check", 
            "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]"),
            "version": "3.7"
        }
    ]
    
    results = scan_file(str(test_file), rules)
    assert len(results) == 1

def test_scan_file_ignores_next_line(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("# version-scanner: ignore-next-line\npython_requires = '>=3.7'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]")}
    ]
    
    results = scan_file(str(test_file), rules)
    assert len(results) == 0

def test_scan_repository_flags_filename(tmp_path):
    test_file = tmp_path / "test-3.9.txt"
    test_file.write_text("clean content\n")
    
    rules = []
    
    from version_scanner import scan_repository
    results = scan_repository(str(tmp_path), rules, version_string="3.9")
    
    assert len(results) == 1
    assert results[0]["rule_name"] == "filename_match"
    assert results[0]["matched_string"] == "3.9"

# Test directory scan simulation
def test_directory_scan(tmp_path):
    # Create dummy files
    p1 = tmp_path / "pkg1"
    p1.mkdir()
    f1 = p1 / "setup.py"
    f1.write_text("python_requires = '>=3.7'\n")
    
    p2 = tmp_path / "pkg2"
    p2.mkdir()
    f2 = p2 / "clean.py"
    f2.write_text("print('Hello')\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": re.compile(r"python_requires\s*=\s*['\"]>=3\.7['\"]")}
    ]
    
    results = []
    for root, dirs, files in os.walk(tmp_path):
        for file in files:
            file_path = os.path.join(root, file)
            results.extend(scan_file(file_path, rules))
            
    assert len(results) == 1
    assert results[0]["rule_name"] == "python_requires_check"

# Test write_csv_report
def test_write_csv_report(tmp_path):
    output_file = tmp_path / "report.csv"
    matches = [
        {
            "file_path": "./setup.py",
            "rule_name": "python_requires_check",
            "line_number": 1,
            "matched_string": "python_requires = '>=3.7'",
            "context_line": "python_requires = '>=3.7'",
            "dependency": "python",
            "version": "3.7"
        }
    ]
    
    write_csv_report(str(output_file), matches)
    
    assert output_file.exists()
    
    with open(output_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    assert len(rows) == 1
    assert rows[0]["file_name"] == "setup.py"
    assert rows[0]["file_path"] == "./setup.py"
    assert rows[0]["rule_name"] == "python_requires_check"
    assert rows[0]["line_number"] == "1"
    assert rows[0]["matched_string"] == "python_requires = '>=3.7'"
    assert rows[0]["context_line"] == "python_requires = '>=3.7'"
    assert rows[0]["dependency"] == "python"
    assert rows[0]["version"] == "3.7"


def test_load_config(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("""
rules:
  - name: test_rule
    rules:
      - python{version}
""")
    
    cm = ConfigManager(str(config_file), "python", "3.7")
    rules = cm.load_config()
    
    assert len(rules) == 1
    assert rules[0]["name"] == "test_rule"
    assert rules[0]["pattern"] == "python3.7"


@pytest.mark.parametrize("template, expected_warning", [
    ("python{missing_var}", "Warning: Missing variable for interpolation"),
    ("python{version", "Warning: Invalid format string"),
])
def test_load_config_error_handling(tmp_path, capsys, template, expected_warning):
    config_file = tmp_path / "config.yaml"
    config_file.write_text(f"""
rules:
  - name: test_rule
    rules:
      - {template}
""")
    
    cm = ConfigManager(str(config_file), "python", "3.7")
    rules = cm.load_config()
    
    assert len(rules) == 0
    
    captured = capsys.readouterr()
    assert expected_warning in captured.err


def test_load_config_permission_error(tmp_path, capsys):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("rules: []")
    
    cm = ConfigManager(str(config_file), "python", "3.7")
    
    with patch("builtins.open", side_effect=PermissionError("Permission denied")):
        with pytest.raises(SystemExit) as excinfo:
            cm.load_config()
            
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Permission denied reading config file" in captured.err
def test_main_package_file_permission_error(tmp_path, capsys):
    package_file = tmp_path / "packages.txt"
    package_file.write_text("packages/pkg_a")
    
    test_args = ["version_scanner.py", "-d", "python", "-v", "3.7", "--package-file", str(package_file)]
    
    real_open = open
    def side_effect(file, *args, **kwargs):
        if str(file) == str(package_file):
            raise PermissionError("Permission denied")
        return real_open(file, *args, **kwargs)
        
    with patch("sys.argv", test_args):
        with patch("builtins.open", side_effect=side_effect):
            with pytest.raises(SystemExit) as excinfo:
                from version_scanner import main
                main()
                
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Permission denied reading package file" in captured.err
def test_main_package_file_not_found(capsys):
    test_args = ["version_scanner.py", "-d", "python", "-v", "3.7", "--package-file", "non_existent_file.txt"]
    
    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit) as excinfo:
            from version_scanner import main
            main()
            
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Package file not found" in captured.err



def test_get_match_counts():
    from version_scanner import get_match_counts
    
    matches = [
        {"rule_name": "rule1", "package_name": "pkg1"},
        {"rule_name": "rule1", "package_name": "pkg2"},
        {"rule_name": "rule2", "package_name": "pkg1"},
    ]
    
    rule_counts, package_counts = get_match_counts(matches)
    
    assert rule_counts == {"rule1": 2, "rule2": 1}
    assert package_counts == {"pkg1": 2, "pkg2": 1}


def test_scan_file_removes_newline_from_match(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("Python 3.7\n")
    
    rules = [
        {"name": "explicit_version_string", "pattern": re.compile(r"(?:['\"]|\s|^)3\.7(\.\d+)?(?:['\"]|\s|$)")}
    ]
    
    from version_scanner import scan_file
    results = scan_file(str(test_file), rules)
    
    assert len(results) == 1
    assert "\n" not in results[0]["matched_string"]



def test_scan_repository_ignores_version_scanner(tmp_path):
    vs_dir = tmp_path / "version_scanner"
    vs_dir.mkdir()
    f = vs_dir / "test.py"
    f.write_text("python_requires = '>=3.7'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": "python_requires\\s*=\\s*['\"]>=3\\.7['\"]"}
    ]
    
    from version_scanner import scan_repository
    results = scan_repository(str(tmp_path), rules, ignore_dirs=['version_scanner'])
    
    assert len(results) == 0


def test_scan_repository_wildcard_ignores(tmp_path):
    # Create files
    (tmp_path / "test.jpg").write_text("dummy version 3.7\n")
    (tmp_path / "test.py").write_text("python_requires = '>=3.7'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": "python_requires\\s*=\\s*['\"]>=3\\.7['\"]"},
        {"name": "explicit_version_string", "pattern": "3\\.7"}
    ]
    
    from version_scanner import scan_repository
    # Without ignore
    results = scan_repository(str(tmp_path), rules)
    assert len(results) >= 2
    
    # With wildcard ignore for *.jpg
    results_ignored = scan_repository(str(tmp_path), rules, ignore_dirs=["*.jpg"])
    # test.jpg should be ignored completely
    for match in results_ignored:
        assert not match["file_path"].endswith("test.jpg")


DEFAULT_IGNORE_PATTERNS = [".git", "*.jpg", "packages/pkg_a/.nox", "*.egg-info"]

@pytest.mark.parametrize(
    "rel_path, name, ignore_patterns, expected",
    [
        pytest.param(".git", ".git", DEFAULT_IGNORE_PATTERNS, True, id="exact_match"),
        pytest.param(".GIT", ".GIT", DEFAULT_IGNORE_PATTERNS, True, id="case_insensitive_match"),
        pytest.param("some/path/image.jpg", "image.jpg", DEFAULT_IGNORE_PATTERNS, True, id="wildcard_subpath_match"),
        pytest.param("image.JPG", "image.JPG", DEFAULT_IGNORE_PATTERNS, True, id="wildcard_case_insensitive_match"),
        pytest.param("packages/pkg_a/.nox", ".nox", DEFAULT_IGNORE_PATTERNS, True, id="subpath_exact_match"),
        pytest.param("google_cloud_pubsub.egg-info", "google_cloud_pubsub.egg-info", DEFAULT_IGNORE_PATTERNS, True, id="wildcard_directory_match"),
        pytest.param("setup.py", "setup.py", DEFAULT_IGNORE_PATTERNS, False, id="no_match"),
        pytest.param("packages", "packages", ["/packages"], True, id="anchored_root_match"),
        pytest.param("some/other/packages", "packages", ["/packages"], False, id="anchored_root_nested_no_match"),
    ]
)
def test__should_ignore(rel_path, name, ignore_patterns, expected):
    from version_scanner import _should_ignore, _preprocess_ignore_patterns
    preprocessed = _preprocess_ignore_patterns(ignore_patterns)
    assert _should_ignore(rel_path, name, preprocessed) is expected


def test_load_ignore_file(tmp_path):
    from version_scanner import load_ignore_file
    
    ignore_file = tmp_path / ".scannerignore"
    ignore_file.write_text("dir1\n# comment\n  \ndir2\n")
    
    ignore_dirs = load_ignore_file(str(ignore_file))
    
    assert ignore_dirs == ["dir1", "dir2"]

@mock.patch('version_scanner.load_ignore_file')
@mock.patch('version_scanner.scan_repository')
def test_main_loads_ignore_from_script_dir(mock_scan, mock_load_ignore):
    mock_load_ignore.return_value = []
    mock_scan.return_value = []
    
    test_args = ["version_scanner.py", "-d", "python", "-v", "3.7"]
    
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with pytest.raises(SystemExit):
            main()
        
    mock_load_ignore.assert_called_once()
    args, kwargs = mock_load_ignore.call_args
    path = args[0]
    assert ".scannerignore" in path
    assert "scripts/version_scanner" in path


try:
    # Ruff linter F401: Imported solely to detect Google API Client library presence for test skipping
    import googleapiclient  # noqa: F401
    HAS_GOOGLE_API = True
except ImportError:
    HAS_GOOGLE_API = False

@pytest.mark.skipif(not HAS_GOOGLE_API, reason="Requires googleapiclient")
@mock.patch('googleapiclient.discovery.build')
@mock.patch('google.auth.default')
def test_upload_to_drive(mock_auth, mock_build):
    """Test the ability to upload results to drive for visibility in gSheets."""
    from unittest import mock
    
    mock_creds = mock.Mock()
    mock_creds.universe_domain = "googleapis.com"
    mock_creds.create_scoped.return_value = mock_creds
    
    mock_auth_http = mock.Mock()
    mock_auth_http.credentials = mock_creds
    mock_creds.authorize.return_value = mock_auth_http
    
    mock_auth.return_value = (mock_creds, "project-id")
    
    mock_sheets = mock.Mock()
    mock_build.return_value = mock_sheets
    
    mock_spreadsheets = mock.Mock()
    mock_sheets.spreadsheets.return_value = mock_spreadsheets
    
    mock_create = mock.Mock()
    mock_spreadsheets.create.return_value = mock_create
    mock_create.execute.return_value = {"spreadsheetUrl": "http://example.com"}
    
    mock_values = mock.Mock()
    mock_spreadsheets.values.return_value = mock_values
    mock_update = mock.Mock()
    mock_values.update.return_value = mock_update
    mock_update.execute.return_value = {}
    
    from version_scanner import upload_to_drive
    
    matches = [{"rule_name": "r1", "package_name": "p1", "file_path": "f1", "line_number": 1, "matched_string": "s1", "context_line": "c1"}]
    
    url = upload_to_drive("test.csv", matches, github_repo="https://github.com/user/repo")
    
    assert url == "http://example.com"
    mock_spreadsheets.create.assert_called_once()
    
    # Verify that update was called with hyperlink formula
    mock_values.update.assert_called_once()
    args, kwargs = mock_values.update.call_args
    body = kwargs.get('body', {})
    values = body.get('values', [])
    assert len(values) > 1
    assert "HYPERLINK" in values[1][6] # line_number is at index 6


def test_regex_examples_from_config():
    """Test that examples in config match at least one rule in the group."""
    config_path = "regex_pattern_config.yaml"
    
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        pytest.fail(f"Config file not found: {config_path}")
        
    rules_list = config.get("rules", [])
    
    # Base variables for interpolation (simulate target version 3.7)
    base_vars = {
        "major": "3",
        "minor": "7",
        "version": "3.7",
        "minor_plus_one": "8",
        "minor_minus_one": "6"
    }
    
    for rule_group in rules_list:
        name = rule_group.get("name")
        examples = rule_group.get("examples", [])
        templates = rule_group.get("rules", [])
        
        if not examples or not templates:
            continue
            
        # Resolve target dependency name based on applies_to metadata, falling back to protobuf
        applies_to = rule_group.get("applies_to", [])
        dep_name = applies_to[0] if applies_to else "protobuf"
        vars = {**base_vars, "name": dep_name}
            
        compiled_patterns = []
        for template in templates:
            try:
                resolved = template.strip().format(**vars)
                compiled_patterns.append(re.compile(resolved, re.IGNORECASE))
            except KeyError:
                continue
                
        for example in examples:
            matched = False
            for pattern in compiled_patterns:
                if pattern.search(example):
                    matched = True
                    break
            assert matched, f"Example '{example}' in group '{name}' did not match any pattern."


def test_regex_negative_cases():
    """Verify regex patterns prevent false positives (lookaheads, patch bounds) and support whitespace."""
    config_path = "regex_pattern_config.yaml"
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        
    rules_list = config.get("rules", [])
    
    # Target version 3.7
    vars = {
        "name": "protobuf",
        "major": "3",
        "minor": "7",
        "version": "3.7",
        "minor_plus_one": "8",
        "minor_minus_one": "6"
    }
    
    # Find specific rule groups
    dep_req_group = next(r for r in rules_list if r["name"] == "dependency_requirement")
    python_cmd_group = next(r for r in rules_list if r["name"] == "explicit_python_command")
    python_req_group = next(r for r in rules_list if r["name"] == "python_requires")
    sys_info_group = next(r for r in rules_list if r["name"] == "sys_version_info")
    
    # 1. Verify dependency_requirement looks ahead correctly (no partial match)
    dep_pattern = re.compile(dep_req_group["rules"][0].strip().format(**vars), re.IGNORECASE)
    assert dep_pattern.search("protobuf==3.7")
    assert not dep_pattern.search("protobuf==3.72")
    
    # 2. Verify explicit_python_command negative lookahead
    cmd_pattern = re.compile(python_cmd_group["rules"][0].strip().format(**vars), re.IGNORECASE)
    assert cmd_pattern.search("python3.7")
    assert not cmd_pattern.search("python3.72")
    
    # 3. Verify python_requires optional patch limits boundary rules to .0
    # Boundary rule 1: >=3.7 (python_requires = '>=3.7.0' is OK, but >=3.7.1 is not equivalent and should be skipped)
    req_ge_pattern = re.compile(python_req_group["rules"][1].strip().format(**vars), re.IGNORECASE)
    assert req_ge_pattern.search("python_requires = '>=3.7'")
    assert req_ge_pattern.search("python_requires = '>=3.7.0'")
    assert not req_ge_pattern.search("python_requires = '>=3.7.1'")
    
    # 4. Verify sys_version_info[1] allows optional whitespace
    # Matches sys.version_info[ 1 ]
    sys_sub_pattern = re.compile(sys_info_group["rules"][10].strip().format(**vars), re.IGNORECASE)  # sys.version_info[1] == 7
    assert sys_sub_pattern.search("sys.version_info[1] == 7")
    assert sys_sub_pattern.search("sys.version_info[ 1 ] == 7")
    assert sys_sub_pattern.search("sys.version_info[1 ] == 7")
    assert sys_sub_pattern.search("sys.version_info[ 1] == 7")


def test_main_exit_code_1():
    """Test that main() calls sys.exit(1) when matches are found."""
    # We can mock scan_repository to return a dummy match
    test_args = ['version_scanner.py', '-d', 'python', '-v', '3.7']
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with mock.patch('version_scanner.scan_repository', return_value=[{'file_path': 'test', 'line_number': 1, 'matched_string': '3.7', 'rule_name': 'test'}]):
            with pytest.raises(SystemExit) as excinfo:
                main()
            assert excinfo.value.code == 1


def test_main_soft_fail_exit_code_0():
    """Test that main() calls sys.exit(0) when matches are found but --soft-fail is set."""
    test_args = ['version_scanner.py', '-d', 'python', '-v', '3.7', '--soft-fail']
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with mock.patch('version_scanner.scan_repository', return_value=[{'file_path': 'test', 'line_number': 1, 'matched_string': '3.7', 'rule_name': 'test'}]):
            with pytest.raises(SystemExit) as excinfo:
                main()
            assert excinfo.value.code == 0


def test_main_stdout(capsys):
    """Test that --stdout prints the CSV output to stdout."""
    test_args = ['version_scanner.py', '-d', 'python', '-v', '3.7', '--stdout']
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with mock.patch('version_scanner.scan_repository', return_value=[{'file_path': 'test.py', 'line_number': 1, 'matched_string': '3.7', 'rule_name': 'test'}]):
            with pytest.raises(SystemExit):
                main()
    
    captured = capsys.readouterr()
    assert "test.py:1 [test] 3.7" in captured.out


def test_main_without_stdout_limits_output(capsys):
    """Test that main() without --stdout prints only 10 matches and shows a suffix."""
    test_args = ['version_scanner.py', '-d', 'python', '-v', '3.7']
    matches = [{'file_path': f'test_{i}.py', 'line_number': i, 'matched_string': '3.7', 'rule_name': 'test'} for i in range(15)]
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with mock.patch('version_scanner.scan_repository', return_value=matches):
            with pytest.raises(SystemExit):
                main()
    
    captured = capsys.readouterr()
    # Should only print first 10 matches
    for i in range(10):
        assert f"test_{i}.py:{i} [test] 3.7" in captured.out
    for i in range(10, 15):
        assert f"test_{i}.py:{i} [test] 3.7" not in captured.out
    assert "... and 5 more matches." in captured.out


def test_main_with_stdout_prints_all(capsys):
    """Test that main() with --stdout prints all matches without limiting."""
    test_args = ['version_scanner.py', '-d', 'python', '-v', '3.7', '--stdout']
    matches = [{'file_path': f'test_{i}.py', 'line_number': i, 'matched_string': '3.7', 'rule_name': 'test'} for i in range(15)]
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with mock.patch('version_scanner.scan_repository', return_value=matches):
            with pytest.raises(SystemExit):
                main()
    
    captured = capsys.readouterr()
    # Should print all 15 matches
    for i in range(15):
        assert f"test_{i}.py:{i} [test] 3.7" in captured.out
    assert "... and 5 more matches." not in captured.out


def test_main_does_not_print_rules(capsys):
    """Test that main() does not print the list of loaded rules to stdout."""
    test_args = ['version_scanner.py', '-d', 'python', '-v', '3.7']
    with mock.patch('sys.argv', test_args):
        from version_scanner import main
        with mock.patch('version_scanner.scan_repository', return_value=[]):
            with pytest.raises(SystemExit):
                main()
    captured = capsys.readouterr()
    assert "explicit_version_string" not in captured.out


def test_scan_file_truncation_bug(tmp_path):
    """Test that searching for 3.1 does NOT match 3.10 (truncation bug)."""
    # Create a file with 3.10
    test_file = tmp_path / "test_file.py"
    test_file.write_text("python_requires = '>=3.10'\npython3.10\nPython310\n")
    
    from version_scanner import ConfigManager, scan_file
    
    # Init config for 3.1
    config_manager = ConfigManager("regex_pattern_config.yaml", "python", "3.1")
    rules = config_manager.load_config()
    import re
    compiled_rules = [{"name": r["name"], "pattern": re.compile(r["pattern"], re.IGNORECASE)} for r in rules]
    
    # It should not match anything because all strings are 3.10, not 3.1
    matches = scan_file(str(test_file), compiled_rules)
    assert len(matches) == 0, f"Expected 0 matches for 3.1 in 3.10 content, but got {len(matches)}: {matches}"


def test_scan_repository_layout_agnostic(tmp_path):
    # Create directories under different roots
    p1 = tmp_path / "generated" / "pkg_gen"
    p1.mkdir(parents=True)
    (p1 / "setup.py").write_text("python_requires = '>=3.7'\n")
    
    p2 = tmp_path / "handwritten" / "pkg_hand"
    p2.mkdir(parents=True)
    (p2 / "setup.py").write_text("python_requires = '>=3.7'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": "python_requires\\s*=\\s*['\"]>=3\\.7['\"]"}
    ]
    
    from version_scanner import scan_repository
    
    # Scan only handwritten package
    results = scan_repository(
        str(tmp_path), 
        rules, 
        target_packages=["handwritten/pkg_hand"]
    )
    
    assert len(results) == 1
    assert results[0]["package_name"] == "pkg_hand"
    assert "handwritten/pkg_hand/setup.py" in results[0]["file_path"]


def test_scan_repository_package_name_roots(tmp_path):
    # Create directories under various package roots
    p1 = tmp_path / "third_party" / "pkg_third"
    p1.mkdir(parents=True)
    (p1 / "setup.py").write_text("python_requires = '>=3.7'\n")
    
    rules = [
        {"name": "python_requires_check", "pattern": "python_requires\\s*=\\s*['\"]>=3\\.7['\"]"}
    ]
    
    from version_scanner import scan_repository
    
    results = scan_repository(str(tmp_path), rules)
    
    assert len(results) == 1
    assert results[0]["package_name"] == "pkg_third"
    assert "third_party/pkg_third/setup.py" in results[0]["file_path"]


# --- Decoupled Formatters Tests (TDD) ---

def test_truncate_context():
    # Context shorter than 500 characters shouldn't be truncated
    assert _truncate_context("short context", "short") == "short context"
    
    # Context longer than 500 characters should be truncated around the matched string
    matched = "TARGET_VERSION"
    long_prefix = "a" * 300
    long_suffix = "b" * 300
    long_context = long_prefix + matched + long_suffix
    
    truncated = _truncate_context(long_context, matched)
    assert len(truncated) <= 500
    assert matched in truncated
    assert truncated.startswith("...")
    assert truncated.endswith("...")

def test_wrap_sheet_hyperlink():
    assert _wrap_sheet_hyperlink("https://github.com/foo", "12") == '=HYPERLINK("https://github.com/foo", "12")'

def test_wrap_sheet_string():
    assert _wrap_sheet_string("3.10") == '="3.10"'
    assert _wrap_sheet_string('python_requires = ">=3.7"') == '="python_requires = "">=3.7"""'
    assert _wrap_sheet_string("") == ""
    assert _wrap_sheet_string(None) == ""

def test_safe_int():
    assert _safe_int("123") == 123
    assert _safe_int("") == 0
    assert _safe_int(None) == 0
    assert _safe_int("abc") == 0

def test_format_for_raw_csv_handles_empty_line_number(sample_match):
    sample_match["line_number"] = ""
    formatted = format_for_raw_csv(sample_match)
    assert formatted["line_number"] == 0

def test_format_for_raw_csv(sample_match):
    formatted = format_for_raw_csv(sample_match)
    
    assert formatted["file_name"] == "setup.py"
    assert formatted["file_path"] == "google-cloud-python/main/packages/pkg_a/setup.py"
    assert formatted["package_name"] == "pkg_a"
    assert formatted["rule_name"] == "python_requires_check"
    assert formatted["line_number"] == 123  # Int conversion
    assert formatted["matched_string"] == "3.7"  # No formula wrapping
    assert formatted["context_line"] == "python_requires = '>=3.7'"
    assert formatted["dependency"] == "python"
    assert formatted["version"] == "3.7"

def test_format_for_raw_csv_fallback_filename(sample_match):
    del sample_match["file_name"]
    formatted = format_for_raw_csv(sample_match)
    assert formatted["file_name"] == "setup.py"

def test_format_for_spreadsheet(sample_match):
    # Without github_repo
    formatted_no_repo = format_for_spreadsheet(sample_match)
    assert formatted_no_repo["file_name"] == "setup.py"
    assert formatted_no_repo["line_number"] == 123
    assert formatted_no_repo["matched_string"] == '="3.7"'  # Decimal protection formula
    assert formatted_no_repo["dependency"] == "python"
    assert formatted_no_repo["version"] == "3.7"
    
    # With github_repo
    formatted_repo = format_for_spreadsheet(sample_match, github_repo="https://github.com/user/repo", branch="main")
    expected_url = "https://github.com/user/repo/blob/main/packages/pkg_a/setup.py#L123"
    assert formatted_repo["line_number"] == f'=HYPERLINK("{expected_url}", "123")'
    assert formatted_repo["matched_string"] == '="3.7"'

def test_format_for_console(sample_match):
    log_str = format_for_console(sample_match)
    assert "google-cloud-python/main/packages/pkg_a/setup.py:123" in log_str
    assert "[python_requires_check]" in log_str
    assert "3.7" in log_str
    assert "python_requires = " not in log_str  # Slim format doesn't print context line


def test_parse_matrix_file(tmp_path):
    from version_scanner import parse_matrix_file
    yaml_file = tmp_path / "matrix.yaml"
    yaml_file.write_text("""
python:
  - "3.7"
  - "3.8"
protobuf: "4.25.8"
""")
    targets = parse_matrix_file(str(yaml_file))
    assert targets == [("python", "3.7"), ("python", "3.8"), ("protobuf", "4.25.8")]

@pytest.mark.parametrize(
    "file_content, file_exists",
    [
        (None, False),                  # File not found
        ("invalid: {", True),           # Invalid YAML
        ("- not_a_mapping", True),      # Invalid structure (list instead of map)
        ("python:\n  - null", True),    # Invalid version type (null/None value)
        ("python:\n  - 3.10", True),    # Invalid version type (float instead of string in list)
        ("python: 3.10", True),         # Invalid version type (float instead of string)
    ]
)
def test_parse_matrix_file_failures(tmp_path, file_content, file_exists):
    from version_scanner import parse_matrix_file
    
    if file_exists:
        yaml_file = tmp_path / "matrix_failures.yaml"
        yaml_file.write_text(file_content)
        path = str(yaml_file)
    else:
        path = "nonexistent_file.yaml"
        
    with pytest.raises(SystemExit) as excinfo:
        parse_matrix_file(path)
    assert excinfo.value.code == 1

def test_scan_repository_multi_targets(tmp_path):
    # Setup files in tmp repository
    file1 = tmp_path / "packages" / "pkg1" / "setup.py"
    file1.parent.mkdir(parents=True)
    file1.write_text("python_requires = '>=3.7'\n")
    
    file2 = tmp_path / "packages" / "pkg2" / "requirements.txt"
    file2.parent.mkdir(parents=True)
    file2.write_text("protobuf==4.25.8\n")
    
    # Let's mock a config file with rules for both python and protobuf
    config_file = tmp_path / "regex_pattern_config.yaml"
    config_file.write_text("""
rules:
  - name: python_requires_check
    applies_to:
      - python
    rules:
      - python_requires\\s*=\\s*['\"]>={version}['\"]
  - name: protobuf_check
    applies_to:
      - protobuf
    rules:
      - protobuf=={version}
""")
    
    from version_scanner import ConfigManager, scan_repository
    
    targets = [("python", "3.7"), ("protobuf", "4.25.8")]
    rules = []
    for dep, ver in targets:
        cm = ConfigManager(str(config_file), dep, ver)
        rules.extend(cm.load_config())
        
    results = scan_repository(str(tmp_path), rules, targets=targets)
    
    # We should have 2 matches
    assert len(results) == 2
    
    # Match for python
    python_match = [r for r in results if r["dependency"] == "python"]
    assert len(python_match) == 1
    assert python_match[0]["version"] == "3.7"
    assert python_match[0]["rule_name"] == "python_requires_check"
    
    # Match for protobuf
    protobuf_match = [r for r in results if r["dependency"] == "protobuf"]
    assert len(protobuf_match) == 1
    assert protobuf_match[0]["version"] == "4.25.8"
    assert protobuf_match[0]["rule_name"] == "protobuf_check"


@pytest.mark.parametrize(
    "args, expected_error_msg",
    [
        # Mixing -m/--matrix-file with -d or -v
        (['version_scanner.py', '-m', 'matrix.yaml', '-d', 'python'], "Cannot specify -d/--dependency or -v/--version when using -m/--matrix-file"),
        (['version_scanner.py', '-m', 'matrix.yaml', '-v', '3.7'], "Cannot specify -d/--dependency or -v/--version when using -m/--matrix-file"),
        (['version_scanner.py', '-m', 'matrix.yaml', '-d', 'python', '-v', '3.7'], "Cannot specify -d/--dependency or -v/--version when using -m/--matrix-file"),
        # Missing either -d or -v when not using -m
        (['version_scanner.py', '-d', 'python'], "Must specify both -d/--dependency and -v/--version when not using -m/--matrix-file"),
        (['version_scanner.py', '-v', '3.7'], "Must specify both -d/--dependency and -v/--version when not using -m/--matrix-file"),
        (['version_scanner.py'], "Must specify both -d/--dependency and -v/--version when not using -m/--matrix-file"),
    ]
)
def test_main_cli_validation(capsys, args, expected_error_msg):
    from version_scanner import main
    with mock.patch('sys.argv', args):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code == 2
        captured = capsys.readouterr()
        assert expected_error_msg in captured.err

