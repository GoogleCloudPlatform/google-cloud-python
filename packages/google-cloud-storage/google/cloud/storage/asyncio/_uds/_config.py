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

"""Activation gating for the private gRPC-over-UDS (Rust Core SDK) backend.

Three modes:

* ``off`` (default): the existing pure-Python GAPIC path; the heavy ``_uds`` runtime
  modules are never imported.
* ``auto`` (``GOOGLE_CLOUD_STORAGE_UDS=auto``): use the Rust ``gcs-core-server`` when
  possible, fall back to GAPIC (with one log line) on unsupported platforms, a missing
  binary, a capability mismatch or unsupported ``Blob`` attributes.
* ``force`` (``--force-use-core-sdk`` on the command line, ``-X gcs_force_use_core_sdk``,
  ``GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK=1`` or ``GOOGLE_CLOUD_STORAGE_UDS=on``):
  use the Rust Core SDK and raise :class:`CoreSdkUnavailableError` instead of ever
  falling back to GAPIC.

The Rust Core SDK only supports gRPC CloudPath, so enforcing DirectPath while the UDS
backend is enabled (``auto`` or ``force``) raises :class:`CoreSdkUnavailableError`.

This module is intentionally lightweight (stdlib only) because it is consulted on
every ``open()`` even when the backend is disabled.
"""

from __future__ import annotations

import logging
import os
import sys
from typing import Optional

logger = logging.getLogger(__name__)

FORCE_FLAG = "--force-use-core-sdk"
FORCE_XOPTION = "gcs_force_use_core_sdk"
ENV_FORCE = "GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK"
ENV_MODE = "GOOGLE_CLOUD_STORAGE_UDS"
ENV_SOCKET = "GOOGLE_CLOUD_STORAGE_UDS_SOCKET"
ENV_BINARY = "GOOGLE_CLOUD_STORAGE_UDS_BINARY"
ENV_TOPOLOGY = "GOOGLE_CLOUD_STORAGE_UDS_MODE"
ENV_SHM = "GOOGLE_CLOUD_STORAGE_UDS_SHM"
ENV_PREWARM = "GOOGLE_CLOUD_STORAGE_UDS_PREWARM"
ENV_DIRECT_PATH_XDS = "GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS"

DIRECT_PATH_SCHEMES = ("google-c2p:///", "google-c2p-experimental:///")

_TRUE = ("1", "true", "yes", "on")

# Blob attributes that unmodified google-cloud-storage `OpenAppendableObject` cannot set.
UNSUPPORTED_BLOB_ATTRS = ("acl", "retention", "temporary_hold", "event_based_hold")


def _core_errors():
    from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError

    return CoreSdkUnavailableError


def is_force_core_sdk() -> bool:
    """Returns ``True`` if the strict fail-closed Rust Core SDK mode is requested."""
    if FORCE_FLAG in sys.argv:
        return True
    if FORCE_XOPTION in getattr(sys, "_xoptions", {}):
        return True
    if os.environ.get(ENV_FORCE, "").strip().lower() in _TRUE:
        return True
    return os.environ.get(ENV_MODE, "").strip().lower() in ("on", "force")


def uds_mode() -> str:
    """Returns ``"off"``, ``"auto"`` or ``"force"``."""
    if is_force_core_sdk():
        return "force"
    if os.environ.get(ENV_MODE, "").strip().lower() == "auto":
        return "auto"
    return "off"


def is_enabled() -> bool:
    """Returns ``True`` if the UDS backend is enabled (``auto`` or ``force``)."""
    return uds_mode() != "off"


def add_core_sdk_cli_flags(parser) -> None:
    """Registers ``--force-use-core-sdk`` on an ``argparse.ArgumentParser``.

    The flag itself is detected from ``sys.argv`` by :func:`is_force_core_sdk`; this
    helper only keeps ``argparse``-based applications and benchmarks from rejecting it as
    an unrecognized argument.
    """
    parser.add_argument(
        FORCE_FLAG,
        dest="force_use_core_sdk",
        action="store_true",
        default=False,
        help=(
            "Route Cloud Storage bidi reads/writes through the Rust Core SDK "
            "(gcs-core-server over a Unix domain socket) and fail instead of "
            "falling back to the pure-Python gRPC path."
        ),
    )


def direct_path_xds_env_enabled() -> bool:
    return os.environ.get(ENV_DIRECT_PATH_XDS, "").strip().lower() in ("1", "true")


def is_direct_path_endpoint(endpoint: Optional[str]) -> bool:
    return bool(endpoint) and endpoint.strip().lower().startswith(DIRECT_PATH_SCHEMES)


def api_endpoint_of(client_options) -> Optional[str]:
    if client_options is None:
        return None
    if isinstance(client_options, dict):
        return client_options.get("api_endpoint")
    return getattr(client_options, "api_endpoint", None)


def direct_path_enforcement_reason(
    attempt_direct_path_explicit: bool, client_options
) -> Optional[str]:
    """Returns why DirectPath is enforced, or ``None`` if it is not."""
    if attempt_direct_path_explicit:
        return "AsyncGrpcClient(attempt_direct_path=True) was passed explicitly"
    endpoint = api_endpoint_of(client_options)
    if is_direct_path_endpoint(endpoint):
        return f"api_endpoint={endpoint!r} selects DirectPath"
    if direct_path_xds_env_enabled():
        return f"{ENV_DIRECT_PATH_XDS} is set"
    return None


def check_direct_path_not_enforced(
    attempt_direct_path_explicit: bool, client_options
) -> None:
    """Raises ``CoreSdkUnavailableError`` if DirectPath is enforced while UDS is enabled."""
    if not is_enabled():
        return
    reason = direct_path_enforcement_reason(attempt_direct_path_explicit, client_options)
    if reason:
        raise _core_errors()(
            f"DirectPath is enforced ({reason}) but the Rust Core SDK UDS backend "
            f"(mode={uds_mode()!r}) only supports gRPC CloudPath. Use "
            "AsyncGrpcClient(attempt_direct_path=False) or disable the UDS backend."
        )


def normalize_endpoint(endpoint: Optional[str], anonymous: bool = False) -> Optional[str]:
    """Normalizes a custom ``api_endpoint`` into a URL understood by the Rust SDK.

    * ``None`` / empty -> ``None`` (default ``https://storage.googleapis.com``)
    * DirectPath schemes -> ``CoreSdkUnavailableError`` (never silently downgraded)
    * ``http://`` / ``https://`` -> unchanged
    * bare ``host:port`` -> ``https://host:port`` (``http://`` for anonymous clients,
      matching the insecure channel ``AsyncGrpcClient`` builds for
      ``AnonymousCredentials``, e.g. testbench / local mocks)
    """
    if not endpoint:
        return None
    e = endpoint.strip()
    if is_direct_path_endpoint(e):
        raise _core_errors()(
            f"api_endpoint={endpoint!r} selects DirectPath; the Rust Core SDK UDS "
            "backend only supports gRPC CloudPath."
        )
    if e.startswith(("http://", "https://")):
        return e.rstrip("/")
    if e.startswith("dns:///"):
        e = e[len("dns:///") :]
    return ("http://" if anonymous else "https://") + e.rstrip("/")


def platform_supported() -> bool:
    return sys.platform.startswith("linux") or sys.platform == "darwin"


def unsupported_blob_attrs(blob) -> list:
    """Returns the loaded ``Blob`` attributes the Rust SDK writer cannot set."""
    if blob is None:
        return []
    found = []
    acl = getattr(blob, "acl", None)
    if acl is not None and getattr(acl, "loaded", False) and list(acl):
        found.append("acl")
    if getattr(blob, "retention", None):
        if any(v is not None for v in dict(blob.retention).values()):
            found.append("retention")
    if getattr(blob, "temporary_hold", None) is not None:
        found.append("temporary_hold")
    if getattr(blob, "event_based_hold", None) is not None:
        found.append("event_based_hold")
    return found


def should_use_uds(client) -> bool:
    """Decides whether ``client``'s bidi operations go through the Rust Core SDK.

    * ``off``: ``False``.
    * Enforced DirectPath (``auto`` and ``force``): raises ``CoreSdkUnavailableError``.
    * ``force``: raises ``CoreSdkUnavailableError`` for non-``AsyncGrpcClient`` clients,
      unsupported platforms or a missing ``gcs-core-server`` binary; else ``True``.
    * ``auto``: ``False`` (with one log line) in those cases; else ``True``.
    """
    mode = uds_mode()
    if mode == "off":
        return False

    from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient

    err = _core_errors()
    if not isinstance(client, AsyncGrpcClient):
        if mode == "force":
            raise err(
                f"--force-use-core-sdk requires an AsyncGrpcClient, got {type(client)!r}"
            )
        return False

    check_direct_path_not_enforced(
        getattr(client, "_direct_path_enforced", False),
        getattr(client, "_client_options", None),
    )

    if not platform_supported():
        if mode == "force":
            raise err(
                f"the Rust Core SDK UDS backend is not supported on {sys.platform}"
            )
        _log_fallback_once(f"unsupported platform {sys.platform}")
        return False

    if os.environ.get(ENV_SOCKET):
        return True

    from google.cloud.storage.asyncio._uds import server_manager

    try:
        server_manager.resolve_binary()
    except err as exc:
        if mode == "force":
            raise
        _log_fallback_once(str(exc))
        return False
    return True


_fallback_logged = False


def _log_fallback_once(reason: str) -> None:
    global _fallback_logged
    if not _fallback_logged:
        _fallback_logged = True
        logger.warning(
            "GOOGLE_CLOUD_STORAGE_UDS=auto: falling back to the pure-Python gRPC "
            "path (%s).",
            reason,
        )


def log_fallback(reason: str) -> None:
    """Logs an ``auto``-mode fallback (once per process)."""
    _log_fallback_once(reason)
