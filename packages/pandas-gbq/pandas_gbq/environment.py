# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


import importlib
import json
import os
import pathlib

Path = pathlib.Path


# The identifier for GCP VS Code extension
# https://cloud.google.com/code/docs/vscode/install
GOOGLE_CLOUD_CODE_EXTENSION_NAME = "googlecloudtools.cloudcode"


# The identifier for BigQuery Jupyter notebook plugin
# https://cloud.google.com/bigquery/docs/jupyterlab-plugin
BIGQUERY_JUPYTER_PLUGIN_NAME = "bigquery_jupyter_plugin"


def _is_vscode_extension_installed(extension_id: str) -> bool:
    """
    Checks if a given Visual Studio Code extension is installed.

    Args:
        extension_id: The ID of the extension (e.g., "ms-python.python").

    Returns:
        True if the extension is installed, False otherwise.
    """
    try:
        # Determine the user's VS Code extensions directory.
        user_home = Path.home()
        vscode_extensions_dir = user_home / ".vscode" / "extensions"

        # Check if the extensions directory exists.
        if not vscode_extensions_dir.exists():
            return False

        # Iterate through the subdirectories in the extensions directory.
        for item in vscode_extensions_dir.iterdir():
            # Ignore non-directories.
            if not item.is_dir():
                continue

            # Directory must start with the extension ID.
            if not item.name.startswith(extension_id + "-"):
                continue

            # As a more robust check, the manifest file must exist.
            manifest_path = item / "package.json"
            if not manifest_path.exists() or not manifest_path.is_file():
                continue

            # Finally, the manifest file must be a valid json
            with open(manifest_path, "r", encoding="utf-8") as f:
                json.load(f)

            return True
    except Exception:
        pass

    return False


def _is_package_installed(package_name: str) -> bool:
    """
    Checks if a Python package is installed.

    Args:
        package_name: The name of the package to check (e.g., "requests", "numpy").

    Returns:
        True if the package is installed, False otherwise.
    """
    try:
        importlib.import_module(package_name)
        return True
    except Exception:
        return False


def is_vscode() -> bool:
    return os.getenv("VSCODE_PID") is not None


def is_jupyter() -> bool:
    return os.getenv("JPY_PARENT_PID") is not None


def is_vscode_google_cloud_code_extension_installed() -> bool:
    return _is_vscode_extension_installed(GOOGLE_CLOUD_CODE_EXTENSION_NAME)


def is_jupyter_bigquery_plugin_installed() -> bool:
    return _is_package_installed(BIGQUERY_JUPYTER_PLUGIN_NAME)
