#!/usr/bin/env python3
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
"""
Automated Dependency Version Scanner
Scans a repository for references to specific dependency versions.
"""

import argparse
import csv
import datetime
import fnmatch
import os
import re
import sys
from typing import Dict, List, Tuple, Any, Optional
import yaml


def _safe_read_file(
    file_path: str, 
    required: bool = True, 
    description: str = "file",
    silent_missing: bool = False
) -> Optional[str]:
    """
    Safely reads file content and handles common file errors.
    
    Args:
        file_path: Path to the file.
        required: If True, exits the program with code 1 on read failure.
                  If False, prints a warning (or ignores) and returns None.
        description: Description of the file type for error logging.
        silent_missing: If True, silently ignores FileNotFoundError (returns None).
        
    Returns:
        The file content string, or None if reading failed/was ignored.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        if silent_missing:
            return None
        if required:
            print(f"Error: {description.capitalize()} not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"Warning: {description.capitalize()} not found: {file_path}", file=sys.stderr)
            return None
    except PermissionError:
        if required:
            print(f"Error: Permission denied reading {description}: {file_path}", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"Warning: Permission denied reading {description}: {file_path}", file=sys.stderr)
            return None
    except (IOError, ValueError) as e:
        if required:
            print(f"Error reading {description} {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"Warning: Error reading {description} {file_path}: {e}", file=sys.stderr)
            return None


class ConfigManager:
    """
    Handles loading, validation, and interpolation of the regex configuration rules.
    
    Uses template-based regex configurations from a YAML file and interpolates them
    with dependency properties and computed version segments (e.g., major, minor) to 
    generate active regex search patterns dynamically.
    """
    
    def __init__(self, config_path: str, dependency: str, version: str):
        """
        Initializes the configuration manager.
        
        Args:
            config_path: Path to the YAML configuration file containing regex templates.
            dependency: Name of the dependency to search for (e.g., "python", "protobuf").
            version: Specific target version string to search for (e.g., "3.7", "4.25.8").
        """
        self.config_path = config_path
        self.dependency = dependency
        self.version = version
        self.variables = self._compute_variables()
        
    def _compute_variables(self) -> Dict[str, str]:
        """
        Parses the version string and computes variables for template interpolation.
        
        Splits the version string by '.' and generates segments like major, minor,
        patch, minor+1, and minor-1. These variables are used in regex templates
        (e.g., `{minor_plus_one}` to search for Python 3.8 when EOLing 3.7).
        
        Examples:
            If version is "3.7" and dependency is "python":
                vars = {
                    "name": "python",
                    "version": "3.7",
                    "major": "3",
                    "minor": "7",
                    "minor_plus_one": "8",
                    "minor_minus_one": "6"
                }
            If version is "4.25.8" and dependency is "protobuf":
                vars = {
                    "name": "protobuf",
                    "version": "4.25.8",
                    "major": "4",
                    "minor": "25",
                    "patch": "8",
                    "minor_plus_one": "26",
                    "minor_minus_one": "24"
                }
                
        Returns:
            A dictionary mapping variable placeholder names to their resolved string values.
        """
        vars = {
            "name": self.dependency,
            "version": self.version,
        }
        
        parts = self.version.split('.')
        if len(parts) >= 1:
            vars["major"] = parts[0]
        if len(parts) >= 2:
            vars["minor"] = parts[1]
            try:
                vars["minor_plus_one"] = str(int(parts[1]) + 1)
            except ValueError:
                vars["minor_plus_one"] = parts[1]
            try:
                vars["minor_minus_one"] = str(int(parts[1]) - 1)
            except ValueError:
                vars["minor_minus_one"] = parts[1]
        if len(parts) >= 3:
            vars["patch"] = parts[2]
            
        return vars
        
    def load_config(self) -> List[Dict[str, str]]:
        """Load and resolve rules from config."""
        content = _safe_read_file(self.config_path, required=True, description="config file")
        try:
            config = yaml.safe_load(content)
        except yaml.YAMLError as e:
            print(f"Error parsing config file: {e}", file=sys.stderr)
            sys.exit(1)
            
        rules_list = config.get("rules", [])
        resolved_rules = []
        
        for rule_group in rules_list:
            name = rule_group.get("name")
            applies_to = rule_group.get("applies_to", [])
            
            # Filter by dependency
            if applies_to and self.dependency not in applies_to:
                continue
                
            templates = rule_group.get("rules", [])
            
            for template in templates:
                try:
                    resolved_pattern = template.strip().format(**self.variables)
                    resolved_rules.append({
                        "name": name,
                        "pattern": resolved_pattern,
                        "dependency": self.dependency,
                        "version": self.version
                    })
                except KeyError as e:
                    print(f"Warning: Missing variable for interpolation in rule {name}: {e}", file=sys.stderr)
                except ValueError as e:
                    print(f"Warning: Invalid format string in rule {name}: {e}", file=sys.stderr)
                
        return resolved_rules

def scan_file(file_path: str, compiled_rules: List[Dict[str, re.Pattern]]) -> List[Dict[str, Any]]:
    """
    Scan a single file for matching patterns.
    
    Args:
        file_path: Path to the file to scan.
        compiled_rules: A list of dictionaries containing 'name' and 'pattern' (compiled regex).
        
    Returns:
        A list of dictionaries containing match details.
    """
    results = []
            
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            skip_next = False
            for line_num, line in enumerate(f, 1):
                if skip_next:
                    skip_next = False
                    continue
                if "version-scanner: ignore-next-line" in line:
                    skip_next = True
                    continue
                if "version-scanner: ignore" in line and "version-scanner: ignore-rule" not in line and "version-scanner: ignore-next-line" not in line:
                    continue
                for rule in compiled_rules:
                    match = rule["pattern"].search(line)
                    if match:
                        version = rule.get("version")
                        if version:
                            pragma_pattern = rf"version-scanner\s*:\s*ignore-rule\s*=\s*{re.escape(str(rule['name']))}\s*:\s*{re.escape(str(version))}"
                            if re.search(pragma_pattern, line, re.IGNORECASE):
                                continue
                        results.append({
                            "rule_name": rule["name"],
                            "line_number": line_num,
                            "matched_string": match.group(0).strip(),
                            "context_line": line.strip(),
                            "dependency": rule.get("dependency", ""),
                            "version": rule.get("version", "")
                        })
    except IOError as e:
        print(f"Warning: Could not read file {file_path}: {e}", file=sys.stderr)
        
    return results


def _truncate_context(context: str, matched: str) -> str:
    """Safely truncates context around the match location to prevent overflow."""
    if len(context) > 500:
        match_start = context.find(matched)
        if match_start != -1:
            start = max(0, match_start - 200)
            end = min(len(context), match_start + len(matched) + 200)
            prefix = "..." if start > 0 else ""
            suffix = "..." if end < len(context) else ""
            return prefix + context[start:end] + suffix
        else:
            return context[:500] + "..."
    return context


def _wrap_sheet_hyperlink(url: str, label: str) -> str:
    """Wraps a URL and label into a Google Sheets HYPERLINK formula.

    This ensures that when output is imported into spreadsheet software, the
    resulting cells contain clickable hyperlinks pointing directly to GitHub file
    locations and line numbers.
    """
    return f'=HYPERLINK("{url}", "{label}")'


def _wrap_sheet_string(value: str) -> str:
    """Wraps a string value inside a spreadsheet string formula to prevent float parsing.

    This forces spreadsheet software (such as Google Sheets) to treat numeric
    string patterns (like python runtime version "3.10") as literal strings,
    preventing auto-truncation to floats (which would display "3.1"). Double
    quotes inside the value are escaped by doubling them to avoid formula syntax
    errors on import.
    """
    if value is None:
        return ""
    escaped_value = value.replace('"', '""')
    return f'="{escaped_value}"' if value else ""


def _safe_int(value: Any, default: int = 0) -> int:
    """Safely converts a value to an integer, falling back to a default value.

    Used primarily during raw data formatting for spreadsheet ingestion. If a
    value (like a line number) is missing or contains non-integer text (e.g. empty
    strings for filename-only matches), this avoids crashing the scanner.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def format_for_raw_csv(match: Dict[str, Any]) -> Dict[str, Any]:
    """Prepares a full raw dataset (n + x columns) with clean text values."""
    file_name = match.get("file_name")
    if not file_name and match.get("file_path"):
        file_name = os.path.basename(match.get("file_path"))
    return {
        "file_name": file_name or "",
        "file_path": match.get("file_path", ""),
        "package_name": match.get("package_name", ""),
        "rule_name": match.get("rule_name", ""),
        "line_number": _safe_int(match.get("line_number")),
        "matched_string": match.get("matched_string", ""),
        "context_line": _truncate_context(match.get("context_line", ""), match.get("matched_string", "")),
        "dependency": match.get("dependency", ""),
        "version": match.get("version", "")
    }


def format_for_spreadsheet(
    match: Dict[str, Any], 
    github_repo: str = None, 
    branch: str = "main"
) -> Dict[str, Any]:
    """Builds on top of raw CSV but applies Sheets-specific formulas."""
    formatted = format_for_raw_csv(match)
    
    # Override fields with spreadsheet formatting
    if github_repo:
        file_path = match.get("repo_path", match.get("file_path", ""))
        line_number = match.get("line_number", "")
        url = f"{github_repo}/blob/{branch}/{file_path}#L{line_number}"
        formatted["line_number"] = _wrap_sheet_hyperlink(url, str(line_number))
        
    formatted["matched_string"] = _wrap_sheet_string(match.get("matched_string", ""))
    return formatted


def format_for_console(match: Dict[str, Any]) -> str:
    """Prepares a slim, readable string representation (n columns) for stdout/logs."""
    file_path = match.get("file_path", "")
    line_number = match.get("line_number", "")
    rule_name = match.get("rule_name", "")
    matched_string = match.get("matched_string", "")
    return f"  {file_path}:{line_number} [{rule_name}] {matched_string}"



def get_match_counts(matches: List[Dict[str, Any]]) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Aggregate matches by rule and by package.
    """
    rule_counts = {}
    package_counts = {}
    for m in matches:
        r = m.get("rule_name")
        p = m.get("package_name")
        rule_counts[r] = rule_counts.get(r, 0) + 1
        package_counts[p] = package_counts.get(p, 0) + 1
    return rule_counts, package_counts


def print_summary_table(rule_counts: Dict[str, int], package_counts: Dict[str, int]) -> None:
    """
    Print a summary table to the console.
    """
    print("\n=== Scan Summary ===")
    print(f"{'Rule Name':<30} {'Matches':<10}")
    print("-" * 42)
    for rule, count in sorted(rule_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{rule:<30} {count:<10}")
        
    print(f"\n{'Package Name':<40} {'Matches':<10}")
    print("-" * 52)
    sorted_packages = sorted(package_counts.items(), key=lambda x: x[1], reverse=True)
    for pkg, count in sorted_packages[:10]:
        display_name = pkg if pkg else '[Root/None]'
        print(f"{display_name:<40} {count:<10}")
        
    if len(sorted_packages) > 10:
        print(f'... and {len(sorted_packages) - 10} more packages.')


def load_ignore_file(file_path: str) -> List[str]:
    """
    Read ignore paths from a file.
    """
    ignore_dirs = []
    content = _safe_read_file(file_path, required=False, silent_missing=True)
    if content:
        for line in content.splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                ignore_dirs.append(line)
    return ignore_dirs


def write_csv_report(
    output_path: str, 
    matches: List[Dict[str, Any]]
) -> None:
    """
    Write the collected matches to a CSV file.
    
    Args:
        output_path: Path to the output CSV file.
        matches: A list of dictionaries containing match details.
    """
    fieldnames = ["file_name", "file_path", "package_name", "rule_name", "dependency", "version", "line_number", "matched_string", "context_line"]
    
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for match in matches:
                formatted_match = format_for_raw_csv(match)
                # Ensure only specified fields are written
                row = {field: formatted_match.get(field, "") for field in fieldnames}
                writer.writerow(row)
                
        print(f"\nReport written to: {output_path}")
    except IOError as e:
        print(f"Error writing CSV report: {e}", file=sys.stderr)


def upload_to_drive(csv_path: str, matches: List[Dict[str, Any]], github_repo: str = None, branch: str = "main") -> str:
    """
    Upload matches to a Google Sheet in Drive.
    """
    print("\nUploading to Google Drive...")
    try:
        import google.auth
        from googleapiclient.discovery import build
    except ImportError:
        print("Error: Google API client packages are missing. Please run 'pip install -r requirements.txt' to enable upload functionality.", file=sys.stderr)
        return ""
        
    try:
        credentials, project = google.auth.default(
            scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
        )
        
        service = build('sheets', 'v4', credentials=credentials)
        
        # Create a new spreadsheet
        title = os.path.basename(csv_path).replace('.csv', '')
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet, fields='spreadsheetUrl,spreadsheetId').execute()
        url = spreadsheet.get('spreadsheetUrl')
        spreadsheet_id = spreadsheet.get('spreadsheetId')
        
        # Prepare data
        values = [["file_name", "file_path", "package_name", "rule_name", "dependency", "version", "line_number", "matched_string", "context_line"]]
        for m in matches:
            formatted_m = format_for_spreadsheet(m, github_repo=github_repo, branch=branch)
            values.append([
                formatted_m.get("file_name", ""),
                formatted_m.get("file_path", ""),
                formatted_m.get("package_name", ""),
                formatted_m.get("rule_name", ""),
                formatted_m.get("dependency", ""),
                formatted_m.get("version", ""),
                str(formatted_m.get("line_number", "")),
                formatted_m.get("matched_string", ""),
                formatted_m.get("context_line", "")
            ])
            
        body = {
            'values': values
        }
        
        # Update values
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range='Sheet1!A1',
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        
        print(f"Successfully uploaded to Google Sheet: {url}")
        return url
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error uploading to Google Drive: {e}", file=sys.stderr)
        return ""


def read_package_file(file_path: str) -> List[str]:
    """
    Read package paths from a file.
    
    Args:
        file_path: Path to the package file.
        
    Returns:
        A list of package paths.
    """
    packages = []
    content = _safe_read_file(file_path, required=True, description="package file")
    if content:
        for line in content.splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                packages.append(line)
    return packages


def _preprocess_ignore_patterns(ignore_patterns: List[str]) -> List[Tuple[str, str]]:
    """Preprocesses ignore patterns into a classified list for faster matching.

    Args:
        ignore_patterns: A list of raw ignore patterns from .scannerignore.

    Returns:
        A list of tuples (type, pattern) where type is 'anchored', 'subpath', or 'filename'.
    """
    if not ignore_patterns:
        return []
    
    preprocessed = []
    for pattern in ignore_patterns:
        pattern_lower = pattern.lower()
        if '/' in pattern:
            if pattern_lower.startswith('/'):
                preprocessed.append(('anchored', pattern_lower[1:]))
            else:
                preprocessed.append(('subpath', pattern_lower))
        else:
            preprocessed.append(('filename', pattern_lower))
    return preprocessed


def _should_ignore(rel_path: str, name: str, preprocessed_patterns: List[Tuple[str, str]]) -> bool:
    """Check if a file or directory matches any of the ignore patterns.
    
    Directories and files can be ignored by providing an ignore pattern in the 
    .scannerignore file.

    Args:
        rel_path: The relative path of the file or directory from the scan root.
        name: The name of the file or directory (basename).
        preprocessed_patterns: A list of preprocessed ignore patterns.
        
    Returns:
        True if the file or directory should be ignored, False otherwise.
    """
    if not preprocessed_patterns:
        return False
    name_lower = name.lower()
    rel_path_norm = rel_path.replace(os.sep, '/').lower()
    
    for p_type, p_val in preprocessed_patterns:
        if p_type == 'anchored':
            if fnmatch.fnmatchcase(rel_path_norm, p_val):
                return True
        elif p_type == 'subpath':
            if fnmatch.fnmatchcase(rel_path_norm, p_val) or fnmatch.fnmatchcase(rel_path_norm, f"*/{p_val}"):
                return True
        elif p_type == 'filename':
            if fnmatch.fnmatchcase(name_lower, p_val):
                return True
    return False


def scan_repository(
    root_path: str,
    rules: List[Dict[str, Any]],
    target_packages: List[str] = None,
    ignore_dirs: List[str] = None,
    version_string: str = None,
    targets: List[Tuple[str, str]] = None
) -> List[Dict[str, Any]]:
    """
    Scans the repository directory tree applying resolved regex patterns to files.
    
    Walks the directory structure starting at the root path, checking filenames and
    file contents line-by-line against compiled patterns. Supports case-insensitive
    directory/file ignore patterns, dynamic package filter checks for layout-agnostic
    subfolders, and filename-based version string matching.
    
    Args:
        root_path: Absolute or relative path to the directory tree root to scan.
        rules: A list of dictionaries containing 'name' (rule name) and 'pattern' 
               (regex search pattern string).
        target_packages: Optional list of specific subdirectory paths to restrict scanning
                         (e.g., ['packages/pkg_a', 'generated/pkg_b']). If None or empty,
                         performs a full recursive scan of the repository.
        ignore_dirs: Optional list of directory names or glob-like files to ignore (case-insensitive).
        version_string: Optional target version string (e.g. "3.7") to scan for in filenames.
        targets: Optional list of (dependency, version) tuples.
        
    Returns:
        A list of dictionaries detailing each match.
    """
    results = []
    
    filename_targets = []
    if targets:
        filename_targets = targets
    elif version_string:
        dep = rules[0].get("dependency") if rules else None
        filename_targets = [(dep, version_string)]
        
    # Compile patterns once here
    compiled_rules = []
    for rule in rules:
        try:
            compiled_rules.append({
                "name": rule["name"],
                "pattern": re.compile(rule["pattern"], re.IGNORECASE),
                "dependency": rule.get("dependency", ""),
                "version": rule.get("version", "")
            })
        except re.error as e:
            print(f"Error compiling regex for rule {rule['name']}: {e}", file=sys.stderr)
            continue
            
    # Preprocess ignore patterns once
    preprocessed_ignores = _preprocess_ignore_patterns(ignore_dirs)

    print(f"\nScanning repository: {root_path}")
    if target_packages:
        print(f"Filtering for packages: {target_packages}")
        
    for root, dirs, files in os.walk(root_path):
        rel_root = os.path.relpath(root, root_path)
        
        # Helper to construct relative path for ignore matching
        def get_rel_path(name):
            return name if rel_root == "." else os.path.join(rel_root, name)
            
        # Prune ignore directories (case-insensitive)
        dirs[:] = [
            d for d in dirs 
            if not _should_ignore(get_rel_path(d), d, preprocessed_ignores)
        ]
        
        # Filter ignore files (case-insensitive)
        files = [
            f for f in files 
            if not _should_ignore(get_rel_path(f), f, preprocessed_ignores)
        ]
        
        # Layout-agnostic generic subdirectory filtering
        if target_packages:
            norm_targets = {os.path.normpath(tp) for tp in target_packages}
            is_valid_path = False
            for target in norm_targets:
                if (rel_root == "." or 
                    rel_root == target or 
                    rel_root.startswith(target + os.sep) or 
                    target.startswith(rel_root + os.sep)):
                    is_valid_path = True
                    break
            if not is_valid_path:
                # Skip searching this directory and all its descendants
                dirs[:] = []
                continue
                
        for file in files:
            file_path = os.path.join(root, file)
            matches = scan_file(file_path, compiled_rules)
            
            # Add filename match if applicable
            for dep, ver in filename_targets:
                if ver and ver in file:
                    matches.append({
                        "rule_name": "filename_match",
                        "line_number": 0,
                        "matched_string": ver,
                        "context_line": f"Filename contains {ver}",
                        "dependency": dep or "",
                        "version": ver
                    })
            
            # Compute display path and package name
            rel_file_path = os.path.relpath(file_path, root_path)
            
            package_name = ""
            path_parts = rel_file_path.split(os.sep)
            # Assume package name is the folder directly under standard package root directories
            package_roots = {"packages", "generated", "handwritten", "third_party"}
            if len(path_parts) >= 2 and path_parts[0] in package_roots:
                package_name = path_parts[1]
                
            root_parts = os.path.abspath(root_path).split(os.sep)
            if len(root_parts) >= 2:
                prefix = os.path.join(root_parts[-2], root_parts[-1])
                display_path = os.path.join(prefix, rel_file_path)
            else:
                display_path = rel_file_path
                
            for m in matches:
                m["file_name"] = file
                m["file_path"] = display_path
                m["repo_path"] = rel_file_path
                m["package_name"] = package_name
                results.append(m)
                
    return results


def parse_matrix_file(file_path: str) -> List[Tuple[str, str]]:
    """
    Parses a YAML matrix file into a list of (dependency, version) tuples.
    """
    content = _safe_read_file(file_path, required=True, description="matrix file")
    try:
        raw_matrix = yaml.safe_load(content)
    except Exception as e:
        print(f"Error parsing matrix YAML mapping: {e}", file=sys.stderr)
        sys.exit(1)
        
    if not isinstance(raw_matrix, dict):
        print("Error: Matrix file content must resolve to a YAML mapping", file=sys.stderr)
        sys.exit(1)
        
    targets = []
    for dep, versions in raw_matrix.items():
        if isinstance(versions, list):
            for v in versions:
                if v is None or isinstance(v, (dict, list)):
                    print(f"Error: Invalid version '{v}' for dependency '{dep}'", file=sys.stderr)
                    sys.exit(1)
                if not isinstance(v, str):
                    print(f"Error: Version '{v}' for dependency '{dep}' must be specified as a quoted string to prevent YAML parsing issues (e.g., 3.10 parsed as 3.1).", file=sys.stderr)
                    sys.exit(1)
                targets.append((str(dep), v))
        elif isinstance(versions, str):
            targets.append((str(dep), versions))
        else:
            print(f"Error: Invalid version '{versions}' for dependency '{dep}'. Versions must be specified as quoted strings.", file=sys.stderr)
            sys.exit(1)
            
    return targets


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_config = os.path.join(script_dir, "regex_pattern_config.yaml")
    
    parser = argparse.ArgumentParser(
        description="Scan repository for references to specific dependency versions."
    )
    
    parser.add_argument(
        "-d", "--dependency",
        help="Name of the dependency (e.g., python, protobuf)"
    )
    
    parser.add_argument(
        "-v", "--version",
        help="Specific version to search for (e.g., 3.7, 4.25.8)"
    )
    
    parser.add_argument(
        "-m", "--matrix-file",
        help="Path to a YAML file containing target dependencies and versions."
    )
    
    parser.add_argument(
        "-p", "--path",
        default=".",
        help="Root directory to scan (defaults to current directory)"
    )
    

    
    package_group = parser.add_mutually_exclusive_group()
    
    package_group.add_argument(
        "--package",
        help="Specific subdirectory filter (useful for monorepos)"
    )
    
    package_group.add_argument(
        "--package-file",
        help="Path to a file containing a list of package directories to scan"
    )
    
    parser.add_argument(
        "--config",
        default=default_config,
        help="Path to the regex configuration file (defaults to scripts/version_scanner/regex_pattern_config.yaml)"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Path to the output CSV file (defaults to <dependency>-<version>-<timestamp>.csv)"
    )
    
    parser.add_argument(
        "--github-repo",
        default="https://github.com/googleapis/google-cloud-python",
        help="GitHub repository URL base (defaults to https://github.com/googleapis/google-cloud-python)"
    )
    
    parser.add_argument(
        "--branch",
        default="main",
        help="GitHub branch for links (defaults to main)"
    )
    
    parser.add_argument(
        "--upload",
        action="store_true",
        help="Upload results to a Google Sheet in Drive"
    )
    
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print the full CSV report to stdout instead of/in addition to writing to a file"
    )
    
    parser.add_argument(
        "--soft-fail",
        action="store_true",
        help="Exit with code 0 even if matches are found (useful during development and testing runs)"
    )
    
    args = parser.parse_args()
    
    # Validation of required inputs
    has_matrix_file = bool(args.matrix_file)
    if has_matrix_file:
        if args.dependency or args.version:
            parser.error("Cannot specify -d/--dependency or -v/--version when using -m/--matrix-file")
    else:
        if not (args.dependency and args.version):
            parser.error("Must specify both -d/--dependency and -v/--version when not using -m/--matrix-file")
        
    targets = []
    if has_matrix_file:
        targets = parse_matrix_file(args.matrix_file)
    else:
        targets = [(args.dependency, args.version)]
        
    if not targets:
        print("Error: No targets resolved to scan.", file=sys.stderr)
        sys.exit(1)
        
    # Resolve target packages if filtering is requested
    target_packages = []
    if args.package:
        # If the folder exists under root path as-is, use it. Otherwise fallback to packages/ prefix.
        if os.path.exists(os.path.join(args.path, args.package)):
            target_packages.append(args.package)
        else:
            target_packages.append(os.path.join("packages", args.package))
    elif args.package_file:
        target_packages = read_package_file(args.package_file)
        
    if has_matrix_file:
        print("Starting scan for multiple targets:")
        for dep, ver in targets:
            print(f"  - {dep}: {ver}")
    else:
        print(f"Starting scan for dependency: {args.dependency} version: {args.version}")
    print(f"Root path: {args.path}")
    print("Targets to scan:")
    if target_packages:
        for pkg in target_packages:
            print(f"  - {os.path.join(args.path, pkg)}")
    else:
        print(f"  - {args.path} (all packages)")
    print(f"Using config: {args.config}")
    
    # Load and resolve rules
    rules = []
    for dep, ver in targets:
        config_manager = ConfigManager(args.config, dep, ver)
        rules.extend(config_manager.load_config())
    


            
    # Load ignore file from script directory (Option A)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ignore_file_path = os.path.join(script_dir, ".scannerignore")
    ignore_dirs = load_ignore_file(ignore_file_path)
    if ignore_dirs:
        print(f"Loaded {len(ignore_dirs)} ignore patterns from {ignore_file_path}")
        
    # Scan repository
    all_matches = scan_repository(
        args.path,
        rules,
        target_packages,
        ignore_dirs,
        version_string=(None if has_matrix_file else args.version),
        targets=targets
    )
    
    print(f"\nFound {len(all_matches)} matches.")
    display_matches = all_matches if args.stdout else all_matches[:10]
    for m in display_matches:
        print(format_for_console(m))
        
    if not args.stdout and len(all_matches) > 10:
        print(f"  ... and {len(all_matches) - 10} more matches.")
        
    # Get and print summary counts
    rule_counts, package_counts = get_match_counts(all_matches)
    print_summary_table(rule_counts, package_counts)
        
    # Write report
    if args.output:
        output_path = args.output
    else:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(script_dir, "results")
        os.makedirs(results_dir, exist_ok=True)
        if has_matrix_file:
            base_name = os.path.splitext(os.path.basename(args.matrix_file))[0]
            output_path = os.path.join(results_dir, f"{base_name}-{timestamp}.csv")
        else:
            output_path = os.path.join(results_dir, f"{args.dependency}-{args.version}-{timestamp}.csv")
        
    write_csv_report(output_path, all_matches)
    
    if args.upload:
        upload_to_drive(output_path, all_matches, github_repo=args.github_repo, branch=args.branch)


            
    # Distinct exit codes for CI/CD
    if all_matches and not args.soft_fail:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
