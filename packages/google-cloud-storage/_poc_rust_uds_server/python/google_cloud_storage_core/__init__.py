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

"""Locator for the bundled ``gcs-core-server`` executable (no FFI)."""

from __future__ import annotations

import os
import shutil
import sys
import sysconfig
from typing import Iterator, Optional

__all__ = ["binary_path", "__version__"]

_DIST_NAME = "google-cloud-storage-core"
_BIN_NAME = "gcs-core-server" + (".exe" if sys.platform == "win32" else "")

try:
    from importlib.metadata import PackageNotFoundError, distribution, version

    try:
        __version__ = version(_DIST_NAME)
    except PackageNotFoundError:  # pragma: NO COVER - running from a source tree
        __version__ = "0.0.0"
except ImportError:  # pragma: NO COVER - Python < 3.8
    __version__ = "0.0.0"


def _candidates() -> Iterator[str]:
    # 1. Files recorded for the installed distribution (wheel `.data/scripts`).
    try:
        dist = distribution(_DIST_NAME)
        for f in dist.files or ():
            if f.name == _BIN_NAME:
                yield str(f.locate())
    except Exception:  # pragma: NO COVER - metadata unavailable
        pass
    # 2. Script directories of the running interpreter's install schemes.
    schemes = {sysconfig.get_default_scheme()} if hasattr(sysconfig, "get_default_scheme") else set()
    if hasattr(sysconfig, "get_preferred_scheme"):
        schemes.add(sysconfig.get_preferred_scheme("user"))
    for scheme in schemes:
        try:
            yield os.path.join(sysconfig.get_path("scripts", scheme), _BIN_NAME)
        except KeyError:  # pragma: NO COVER
            continue
    yield os.path.join(os.path.dirname(sys.executable), _BIN_NAME)
    # 3. Next to this package (editable / vendored layouts).
    yield os.path.join(os.path.dirname(os.path.abspath(__file__)), _BIN_NAME)


def binary_path() -> Optional[str]:
    """Returns the absolute path of the bundled ``gcs-core-server`` (or ``None``)."""
    for path in _candidates():
        if path and os.path.isfile(path) and os.access(path, os.X_OK):
            return os.path.abspath(path)
    found = shutil.which(_BIN_NAME)
    return os.path.abspath(found) if found else None
