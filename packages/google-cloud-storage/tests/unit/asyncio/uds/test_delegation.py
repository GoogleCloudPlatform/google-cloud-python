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
"""Delegation / activation tests for the opt-in gRPC-over-UDS backend.

Verifies that the public async classes keep their exact public signatures, that
the default ``off`` mode never touches the UDS runtime, that ``auto`` falls back
to GAPIC and that ``force`` (``--force-use-core-sdk``) fails closed.
"""

import datetime
import inspect
import json
import os
import re
import subprocess
import sys
import textwrap
from io import BytesIO
from unittest import mock
from unittest.mock import AsyncMock

import grpc
import pytest
from google.api_core import exceptions
from google.api_core.client_options import ClientOptions
from google.auth import credentials as auth_credentials

from google.cloud import _storage_v2
from google.cloud.storage.asyncio import async_grpc_client
from google.cloud.storage.asyncio._uds import _config
from google.cloud.storage.asyncio._uds import errors as uds_errors
from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.exceptions import DataCorruption

_MRD_MOD = "google.cloud.storage.asyncio.async_multi_range_downloader"
_AAOW_MOD = "google.cloud.storage.asyncio.async_appendable_object_writer"
_RUNTIME_GET = "google.cloud.storage.asyncio._uds.runtime.get_runtime"
_MiB = 1024 * 1024

# Snapshot of the public API at origin/main (captured from `git show
# origin/main:<path>`); the UDS backend must not change any of it.
_EXPECTED_PUBLIC_API = {
    AsyncGrpcClient: {
        "__init__": "(self, credentials=None, client_info=None, client_options=None, *, attempt_direct_path=True, attempt_direct_path_xds_over_interconnect=False, enable_metrics=None, enable_debug_metrics=None)",
        "metrics_enabled": "property",
        "debug_metrics_enabled": "property",
        "grpc_client": "property",
        "delete_object": "async (self, bucket_name, object_name, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, metadata=(), timeout=None, retry=None, **kwargs)",
        "get_object": "async (self, bucket_name, object_name, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, soft_deleted=None, metadata=(), timeout=None, retry=None, **kwargs)",
    },
    AsyncMultiRangeDownloader: {
        "create_mrd": "classmethod (cls, client: 'AsyncGrpcClient', bucket_name: 'str', object_name: 'str', generation: 'Optional[int]' = None, read_handle: 'Optional[_storage_v2.BidiReadHandle]' = None, retry_policy: 'Optional[AsyncRetry]' = None, metadata: 'Optional[List[Tuple[str, str]]]' = None, **kwargs) -> 'AsyncMultiRangeDownloader'",
        "__init__": "(self, client: 'AsyncGrpcClient', bucket_name: 'str', object_name: 'str', generation: 'Optional[int]' = None, read_handle: 'Optional[_storage_v2.BidiReadHandle]' = None, **kwargs) -> 'None'",
        "__aenter__": "async (self)",
        "__aexit__": "async (self, exc_type, exc_val, exc_tb)",
        "open": "async (self, retry_policy: 'Optional[AsyncRetry]' = None, metadata: 'Optional[List[Tuple[str, str]]]' = None) -> 'None'",
        "download_ranges": "async (self, read_ranges: 'List[Tuple[int, int, Union[IO[bytes], bytearray, memoryview]]]', lock: 'Optional[asyncio.Lock]' = None, retry_policy: 'Optional[AsyncRetry]' = None, metadata: 'Optional[List[Tuple[str, str]]]' = None, enable_checksum: 'bool' = True, accepts_memoryview: 'bool' = False) -> 'None'",
        "close": "async (self)",
        "is_stream_open": "property",
        "object_metadata": "property",
    },
    AsyncAppendableObjectWriter: {
        "__init__": "(self, client: google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient, bucket_name: str, object_name: str, generation: Optional[int] = None, write_handle: Optional[google.cloud._storage_v2.types.storage.BidiWriteHandle] = None, writer_options: Optional[dict] = None, storage_class: Optional[str] = None, preconditions: Optional[google.cloud.storage.asyncio.async_appendable_object_writer.Preconditions] = None)",
        "from_blob": "classmethod (cls, client: google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient, blob: google.cloud.storage.blob.Blob, write_handle: Optional[google.cloud._storage_v2.types.storage.BidiWriteHandle] = None, writer_options: Optional[dict] = None, preconditions: Optional[google.cloud.storage.asyncio.async_appendable_object_writer.Preconditions] = None, generation=<object object>) -> 'AsyncAppendableObjectWriter'",
        "state_lookup": "async (self) -> int",
        "open": "async (self, retry_policy: Optional[google.api_core.retry.retry_unary_async.AsyncRetry] = None, metadata: Optional[List[Tuple[str, str]]] = None) -> None",
        "append": "async (self, data: bytes, retry_policy: Optional[google.api_core.retry.retry_unary_async.AsyncRetry] = None, metadata: Optional[List[Tuple[str, str]]] = None, enable_checksum: bool = True) -> None",
        "simple_flush": "async (self) -> None",
        "flush": "async (self) -> int",
        "close": "async (self, finalize_on_close=False, full_object_checksum: Optional[int] = None, retry_policy: Optional[google.api_core.retry.retry_unary_async.AsyncRetry] = None) -> Union[int, google.cloud._storage_v2.types.storage.Object]",
        "finalize": "async (self, full_object_checksum: Optional[int] = None, retry_policy: Optional[google.api_core.retry.retry_unary_async.AsyncRetry] = None) -> google.cloud._storage_v2.types.storage.Object",
        "is_stream_open": "property",
        "append_from_string": "async (self, data: str)",
        "append_from_stream": "async (self, stream_obj)",
        "append_from_file": "async (self, file_obj: _io.BufferedReader, block_size: int = 16777216)",
    },
}

_HEAVY_MODULES = (
    "google.cloud.storage.asyncio._uds.runtime",
    "google.cloud.storage.asyncio._uds.shm",
    "google.cloud.storage.asyncio._uds.server_manager",
    "google.cloud.storage.asyncio._uds.read_session",
    "google.cloud.storage.asyncio._uds.write_session",
    "google.cloud.storage.asyncio._uds.gcscore_pb2",
)


def _public_members(cls):
    out = {}
    for name, value in vars(cls).items():
        if name.startswith("_") and name not in ("__init__", "__aenter__", "__aexit__"):
            continue
        if isinstance(value, property):
            out[name] = "property"
        elif isinstance(value, classmethod):
            out[name] = "classmethod " + str(inspect.signature(value.__func__))
        elif callable(value):
            prefix = "async " if inspect.iscoroutinefunction(value) else ""
            out[name] = prefix + str(inspect.signature(value))
    # Sentinel defaults (e.g. ``from_blob(generation=_marker)``) repr with an address.
    return {
        name: re.sub(r"<object object at 0x[0-9a-f]+>", "<object object>", sig)
        for name, sig in out.items()
    }


# ------------------------------------------------------------------- fixtures


@pytest.fixture
def uds_env(monkeypatch):
    """Clears every UDS knob; returns a helper to select a mode."""
    for key in (
        _config.ENV_FORCE,
        _config.ENV_MODE,
        _config.ENV_SOCKET,
        _config.ENV_BINARY,
        _config.ENV_TOPOLOGY,
        _config.ENV_SHM,
        _config.ENV_PREWARM,
        _config.ENV_DIRECT_PATH_XDS,
        "GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT",
    ):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setattr(sys, "argv", [a for a in sys.argv if a != _config.FORCE_FLAG])
    monkeypatch.delitem(sys._xoptions, _config.FORCE_XOPTION, raising=False)
    monkeypatch.setattr(_config, "_fallback_logged", False)
    monkeypatch.setitem(sys.modules, "google_cloud_storage_core", None)
    # No gcs-core-server on PATH unless a test puts one there.
    monkeypatch.setenv("PATH", "/nonexistent-uds-test-path")

    def select(mode):
        if mode == "auto":
            monkeypatch.setenv(_config.ENV_MODE, "auto")
        elif mode == "force":
            monkeypatch.setenv(_config.ENV_FORCE, "1")
        else:
            assert mode == "off"

    return select


@pytest.fixture
def storage_client_cls():
    with mock.patch("google.cloud._storage_v2.StorageAsyncClient") as cls:
        cls.get_transport_class.return_value = mock.MagicMock()
        yield cls


def _make_client(storage_client_cls, **kwargs):
    kwargs.setdefault("credentials", mock.Mock(spec=auth_credentials.Credentials))
    return AsyncGrpcClient(**kwargs)


def _channel_kwargs(storage_client_cls):
    transport_cls = storage_client_cls.get_transport_class.return_value
    return transport_cls.create_channel.call_args.kwargs


@pytest.fixture
def read_stream_cls():
    with mock.patch(f"{_MRD_MOD}._AsyncReadObjectStream") as cls:
        stream = cls.return_value
        stream.open = AsyncMock()
        stream.close = AsyncMock()
        stream.generation_number = 1
        stream.persisted_size = 10
        stream.read_handle = b"h"
        stream.object_metadata = mock.Mock()
        yield cls


@pytest.fixture
def write_stream_cls():
    with mock.patch(f"{_AAOW_MOD}._AsyncWriteObjectStream") as cls:
        stream = cls.return_value
        stream.open = AsyncMock()
        stream.close = AsyncMock()
        stream.send = AsyncMock()
        stream.recv = AsyncMock()
        stream.is_stream_open = False
        stream.persisted_size = 0
        stream.generation_number = 1
        stream.write_handle = None
        yield cls


def _mock_client():
    client = mock.MagicMock()
    client.grpc_client = AsyncMock()
    return client


# ------------------------------------------------------------ public API snapshot


@pytest.mark.parametrize("cls", list(_EXPECTED_PUBLIC_API), ids=lambda c: c.__name__)
def test_public_signatures_unchanged(cls):
    assert _public_members(cls) == _EXPECTED_PUBLIC_API[cls]


def test_async_grpc_client_signature_reports_attempt_direct_path_true():
    param = inspect.signature(AsyncGrpcClient.__init__).parameters[
        "attempt_direct_path"
    ]
    assert param.default is True
    assert param.kind is inspect.Parameter.KEYWORD_ONLY


# ------------------------------------------------------------------ off mode


def test_off_mode_never_imports_uds_runtime_modules(tmp_path):
    env = {
        k: v
        for k, v in os.environ.items()
        if not k.startswith("GOOGLE_CLOUD_STORAGE_UDS")
        and k not in (_config.ENV_FORCE, _config.ENV_DIRECT_PATH_XDS)
    }
    code = textwrap.dedent(
        """
        import asyncio, json, sys
        from unittest import mock
        from google.api_core.client_options import ClientOptions
        from google.auth import credentials
        from google.cloud.storage.asyncio import async_appendable_object_writer as w
        from google.cloud.storage.asyncio import async_multi_range_downloader as r
        from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient

        client = AsyncGrpcClient(
            credentials=credentials.AnonymousCredentials(),
            client_options=ClientOptions(api_endpoint="localhost:1"),
        )
        assert w._uds_selected(client) is False
        assert r._uds_selected(client) is False
        assert w._uds_selected(mock.MagicMock()) is False

        async def main():
            mrd = r.AsyncMultiRangeDownloader(client, "b", "o")
            writer = w.AsyncAppendableObjectWriter(client, "b", "o")
            assert mrd._uds is None and writer._uds is None

        asyncio.run(main())
        print(json.dumps(sorted(m for m in sys.modules if "._uds" in m)))
        """
    )
    out = subprocess.run(
        [sys.executable, "-c", code],
        env=env,
        cwd=str(tmp_path),
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert out.returncode == 0, out.stderr
    loaded = set(json.loads(out.stdout.strip().splitlines()[-1]))
    assert not loaded & set(_HEAVY_MODULES), loaded


def test_off_mode_keeps_direct_path_default(uds_env, storage_client_cls):
    uds_env("off")
    client = _make_client(storage_client_cls)
    assert _channel_kwargs(storage_client_cls)["attempt_direct_path"] is True
    assert client._direct_path_enforced is False


def test_off_mode_allows_explicit_direct_path(uds_env, storage_client_cls, monkeypatch):
    uds_env("off")
    client = _make_client(storage_client_cls, attempt_direct_path=True)
    assert _channel_kwargs(storage_client_cls)["attempt_direct_path"] is True
    assert client._direct_path_enforced is True
    _make_client(
        storage_client_cls,
        client_options={"api_endpoint": "google-c2p:///storage.googleapis.com"},
    )
    monkeypatch.setenv(_config.ENV_DIRECT_PATH_XDS, "true")
    _make_client(storage_client_cls)


# ------------------------------------------------------------- mode detection


@pytest.mark.parametrize(
    "how,expected",
    [
        ("none", "off"),
        ("argv", "force"),
        ("xoption", "force"),
        ("env_force_1", "force"),
        ("env_force_true", "force"),
        ("env_force_0", "off"),
        ("uds_on", "force"),
        ("uds_force", "force"),
        ("uds_auto", "auto"),
        ("uds_off", "off"),
        ("uds_garbage", "off"),
    ],
)
def test_uds_mode_detection(uds_env, monkeypatch, how, expected):
    if how == "argv":
        monkeypatch.setattr(sys, "argv", sys.argv + [_config.FORCE_FLAG])
    elif how == "xoption":
        monkeypatch.setitem(sys._xoptions, _config.FORCE_XOPTION, True)
    elif how.startswith("env_force_"):
        monkeypatch.setenv(_config.ENV_FORCE, how[len("env_force_") :])
    elif how.startswith("uds_"):
        monkeypatch.setenv(_config.ENV_MODE, how[len("uds_") :].upper())
    assert _config.uds_mode() == expected
    assert _config.is_enabled() is (expected != "off")
    assert _config.is_force_core_sdk() is (expected == "force")


def test_add_core_sdk_cli_flags_registers_flag():
    import argparse

    parser = argparse.ArgumentParser()
    _config.add_core_sdk_cli_flags(parser)
    assert parser.parse_args([]).force_use_core_sdk is False
    assert parser.parse_args([_config.FORCE_FLAG]).force_use_core_sdk is True


# ----------------------------------------------------------- should_use_uds


def test_should_use_uds_off_is_false_for_any_client(uds_env, storage_client_cls):
    uds_env("off")
    assert _config.should_use_uds(_mock_client()) is False
    assert _config.should_use_uds(_make_client(storage_client_cls)) is False


def test_should_use_uds_auto_non_grpc_client_falls_back(uds_env):
    uds_env("auto")
    assert _config.should_use_uds(_mock_client()) is False


def test_should_use_uds_auto_missing_binary_falls_back_and_logs_once(
    uds_env, storage_client_cls, caplog
):
    uds_env("auto")
    client = _make_client(storage_client_cls)
    with caplog.at_level("WARNING", logger=_config.logger.name):
        assert _config.should_use_uds(client) is False
        assert _config.should_use_uds(client) is False
    fallbacks = [r for r in caplog.records if "falling back" in r.getMessage()]
    assert len(fallbacks) == 1


def test_should_use_uds_auto_with_binary_or_socket(
    uds_env, storage_client_cls, monkeypatch, tmp_path
):
    uds_env("auto")
    client = _make_client(storage_client_cls)
    exe = tmp_path / "gcs-core-server"
    exe.write_text("#!/bin/sh\n")
    exe.chmod(0o755)
    monkeypatch.setenv("PATH", str(tmp_path))
    assert _config.should_use_uds(client) is True
    monkeypatch.setenv("PATH", "/nonexistent-uds-test-path")
    monkeypatch.setenv(_config.ENV_SOCKET, str(tmp_path / "attached.sock"))
    assert _config.should_use_uds(client) is True  # attach mode needs no binary


@pytest.mark.parametrize("how", ["argv", "xoption", "env_force", "uds_on"])
def test_force_missing_binary_raises(uds_env, storage_client_cls, monkeypatch, how):
    if how == "argv":
        monkeypatch.setattr(sys, "argv", sys.argv + [_config.FORCE_FLAG])
    elif how == "xoption":
        monkeypatch.setitem(sys._xoptions, _config.FORCE_XOPTION, True)
    elif how == "env_force":
        monkeypatch.setenv(_config.ENV_FORCE, "1")
    else:
        monkeypatch.setenv(_config.ENV_MODE, "on")
    client = _make_client(storage_client_cls)
    with pytest.raises(CoreSdkUnavailableError, match="binary not found"):
        _config.should_use_uds(client)


def test_force_non_grpc_client_raises(uds_env):
    uds_env("force")
    with pytest.raises(CoreSdkUnavailableError, match="requires an AsyncGrpcClient"):
        _config.should_use_uds(_mock_client())


def test_unsupported_platform(uds_env, storage_client_cls, monkeypatch):
    uds_env("force")
    client = _make_client(storage_client_cls)
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    monkeypatch.setattr(sys, "platform", "win32")
    with pytest.raises(CoreSdkUnavailableError, match="not supported on win32"):
        _config.should_use_uds(client)
    monkeypatch.setenv(_config.ENV_MODE, "auto")
    monkeypatch.delenv(_config.ENV_FORCE)
    assert _config.should_use_uds(client) is False


def test_platform_supported():
    assert _config.platform_supported() is True  # Linux test hosts


# ------------------------------------------------------- DirectPath enforcement


@pytest.mark.parametrize("mode", ["auto", "force"])
@pytest.mark.parametrize(
    "kwargs,env",
    [
        ({"attempt_direct_path": True}, None),
        (
            {
                "client_options": {
                    "api_endpoint": "google-c2p:///storage.googleapis.com"
                }
            },
            None,
        ),
        (
            {
                "client_options": ClientOptions(
                    api_endpoint="google-c2p:///storage.googleapis.com"
                )
            },
            None,
        ),
        (
            {
                "client_options": {
                    "api_endpoint": "google-c2p-experimental:///storage.googleapis.com"
                }
            },
            None,
        ),
        ({}, "1"),
        ({}, "true"),
        ({"attempt_direct_path_xds_over_interconnect": True}, None),
    ],
    ids=[
        "explicit-true",
        "c2p-dict",
        "c2p-options",
        "c2p-experimental",
        "xds-env-1",
        "xds-env-true",
        "interconnect",
    ],
)
def test_direct_path_enforced_raises_when_uds_enabled(
    uds_env, storage_client_cls, monkeypatch, mode, kwargs, env
):
    uds_env(mode)
    if env is not None:
        monkeypatch.setenv(_config.ENV_DIRECT_PATH_XDS, env)
    with pytest.raises(CoreSdkUnavailableError, match="CloudPath"):
        _make_client(storage_client_cls, **kwargs)


@pytest.mark.parametrize("mode", ["auto", "force"])
def test_cloudpath_clients_succeed_when_uds_enabled(uds_env, storage_client_cls, mode):
    uds_env(mode)
    client = _make_client(storage_client_cls)
    assert _channel_kwargs(storage_client_cls)["attempt_direct_path"] is False
    assert client._direct_path_enforced is False
    _make_client(storage_client_cls, attempt_direct_path=False)
    assert _channel_kwargs(storage_client_cls)["attempt_direct_path"] is False
    _config.check_direct_path_not_enforced(False, {"api_endpoint": "localhost:8080"})


def test_should_use_uds_rechecks_direct_path_on_existing_client(
    uds_env, storage_client_cls, monkeypatch
):
    uds_env("off")
    client = _make_client(storage_client_cls, attempt_direct_path=True)
    uds_env("auto")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    with pytest.raises(CoreSdkUnavailableError, match="DirectPath is enforced"):
        _config.should_use_uds(client)


# ----------------------------------------------------- MRD delegation (open)


@pytest.mark.asyncio
@pytest.mark.parametrize("mode", ["off", "auto"])
async def test_mrd_mock_client_uses_gapic(uds_env, read_stream_cls, mode):
    uds_env(mode)
    with mock.patch.object(
        AsyncMultiRangeDownloader, "_open_uds", AsyncMock()
    ) as open_uds:
        mrd = await AsyncMultiRangeDownloader.create_mrd(_mock_client(), "b", "o")
    open_uds.assert_not_awaited()
    read_stream_cls.assert_called_once()
    assert mrd._uds is None and mrd.is_stream_open


@pytest.mark.asyncio
async def test_mrd_auto_missing_binary_falls_back_to_gapic(
    uds_env, storage_client_cls, read_stream_cls
):
    uds_env("auto")
    mrd = await AsyncMultiRangeDownloader.create_mrd(
        _make_client(storage_client_cls), "b", "o"
    )
    read_stream_cls.assert_called_once()
    assert mrd._uds is None


@pytest.mark.asyncio
async def test_mrd_auto_runtime_unavailable_falls_back(
    uds_env, storage_client_cls, read_stream_cls, monkeypatch
):
    uds_env("auto")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    get_rt = AsyncMock(side_effect=CoreSdkUnavailableError("socket gone"))
    with mock.patch(_RUNTIME_GET, get_rt):
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            _make_client(storage_client_cls), "b", "o"
        )
    get_rt.assert_awaited_once()
    read_stream_cls.assert_called_once()
    assert mrd._uds is None


@pytest.mark.asyncio
async def test_mrd_force_runtime_unavailable_raises(
    uds_env, storage_client_cls, read_stream_cls, monkeypatch
):
    uds_env("force")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    with mock.patch(
        _RUNTIME_GET, AsyncMock(side_effect=CoreSdkUnavailableError("socket gone"))
    ):
        with pytest.raises(CoreSdkUnavailableError, match="socket gone"):
            await AsyncMultiRangeDownloader.create_mrd(
                _make_client(storage_client_cls), "b", "o"
            )
    read_stream_cls.assert_not_called()


@pytest.mark.asyncio
async def test_mrd_force_missing_binary_raises_without_gapic(
    uds_env, storage_client_cls, read_stream_cls
):
    uds_env("force")
    client = _make_client(storage_client_cls)
    with pytest.raises(CoreSdkUnavailableError):
        await AsyncMultiRangeDownloader.create_mrd(client, "b", "o")
    read_stream_cls.assert_not_called()
    client.grpc_client.bidi_read_object.assert_not_called()


@pytest.mark.asyncio
async def test_mrd_force_mock_client_raises_without_gapic(uds_env, read_stream_cls):
    uds_env("force")
    with pytest.raises(CoreSdkUnavailableError):
        await AsyncMultiRangeDownloader.create_mrd(_mock_client(), "b", "o")
    read_stream_cls.assert_not_called()


def _fake_read_session(resource):
    session = mock.MagicMock()
    session.open = AsyncMock(return_value=resource)
    session.download_ranges = AsyncMock()
    session.close = AsyncMock()
    session.object_metadata = object()
    return session


@pytest.mark.asyncio
async def test_mrd_uds_open_download_close_delegate(
    uds_env, storage_client_cls, read_stream_cls, monkeypatch
):
    uds_env("force")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    resource = pb.ObjectResource(
        bucket="b", name="o", generation=42, size=1234, finalized=True, crc32c=99
    )
    session = _fake_read_session(resource)
    with (
        mock.patch(_RUNTIME_GET, AsyncMock(return_value=mock.Mock())),
        mock.patch(
            "google.cloud.storage.asyncio._uds.read_session.UdsReadSession",
            return_value=session,
        ) as session_cls,
    ):
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            _make_client(storage_client_cls),
            "b",
            "o",
            metadata=[("x-goog-user-project", "p")],
        )
    read_stream_cls.assert_not_called()
    assert session_cls.call_args.kwargs["metadata"] == [("x-goog-user-project", "p")]
    assert mrd._uds is session
    assert (
        mrd.generation,
        mrd.persisted_size,
        mrd.is_finalized,
        mrd.full_obj_server_crc32c,
    ) == (42, 1234, True, 99)
    assert mrd.object_metadata is session.object_metadata
    ranges = [(0, 10, BytesIO())]
    await mrd.download_ranges(ranges)
    session.download_ranges.assert_awaited_once_with(ranges)
    await mrd.close()
    session.close.assert_awaited_once()
    assert mrd._uds is None and not mrd.is_stream_open


@pytest.mark.asyncio
async def test_mrd_uds_unfinalized_object_has_no_crc(
    uds_env, storage_client_cls, read_stream_cls, monkeypatch
):
    uds_env("force")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    session = _fake_read_session(
        pb.ObjectResource(generation=7, size=5, finalized=False, crc32c=1)
    )
    with (
        mock.patch(_RUNTIME_GET, AsyncMock(return_value=mock.Mock())),
        mock.patch(
            "google.cloud.storage.asyncio._uds.read_session.UdsReadSession",
            return_value=session,
        ),
    ):
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            _make_client(storage_client_cls), "b", "o"
        )
    assert mrd.is_finalized is False and mrd.full_obj_server_crc32c is None


@pytest.mark.asyncio
async def test_mrd_uds_data_corruption_closes_stream(
    uds_env, storage_client_cls, read_stream_cls, monkeypatch
):
    uds_env("force")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    session = _fake_read_session(
        pb.ObjectResource(generation=1, size=5, finalized=True)
    )
    session.download_ranges.side_effect = DataCorruption(None, "bad crc")
    with (
        mock.patch(_RUNTIME_GET, AsyncMock(return_value=mock.Mock())),
        mock.patch(
            "google.cloud.storage.asyncio._uds.read_session.UdsReadSession",
            return_value=session,
        ),
    ):
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            _make_client(storage_client_cls), "b", "o"
        )
    with pytest.raises(DataCorruption):
        await mrd.download_ranges([(0, 5, BytesIO())])
    session.close.assert_awaited_once()
    assert not mrd.is_stream_open


# -------------------------------------------------- writer delegation (open)


@pytest.mark.asyncio
@pytest.mark.parametrize("mode", ["off", "auto"])
async def test_writer_mock_client_uses_gapic(uds_env, write_stream_cls, mode):
    uds_env(mode)
    writer = AsyncAppendableObjectWriter(_mock_client(), "b", "o")
    with mock.patch.object(
        AsyncAppendableObjectWriter, "_open_uds", AsyncMock()
    ) as open_uds:
        await writer.open()
    open_uds.assert_not_awaited()
    write_stream_cls.assert_called_once()
    assert writer._uds is None


@pytest.mark.asyncio
async def test_writer_auto_missing_binary_falls_back_to_gapic(
    uds_env, storage_client_cls, write_stream_cls
):
    uds_env("auto")
    writer = AsyncAppendableObjectWriter(_make_client(storage_client_cls), "b", "o")
    await writer.open()
    write_stream_cls.assert_called_once()
    assert writer._uds is None


@pytest.mark.asyncio
async def test_writer_force_missing_binary_raises_without_gapic(
    uds_env, storage_client_cls, write_stream_cls
):
    uds_env("force")
    writer = AsyncAppendableObjectWriter(_make_client(storage_client_cls), "b", "o")
    with pytest.raises(CoreSdkUnavailableError):
        await writer.open()
    write_stream_cls.assert_not_called()


@pytest.mark.asyncio
async def test_writer_force_unsupported_platform_raises(
    uds_env, storage_client_cls, write_stream_cls, monkeypatch
):
    uds_env("force")
    writer = AsyncAppendableObjectWriter(_make_client(storage_client_cls), "b", "o")
    monkeypatch.setattr(sys, "platform", "win32")
    with pytest.raises(CoreSdkUnavailableError, match="win32"):
        await writer.open()
    write_stream_cls.assert_not_called()


def _blob_with_hold():
    from google.cloud.storage.blob import Blob
    from google.cloud.storage.bucket import Bucket

    blob = Blob("o", bucket=Bucket(client=None, name="b"))
    blob.temporary_hold = True
    return blob


@pytest.mark.asyncio
async def test_writer_force_unsupported_blob_attrs_raise(
    uds_env, storage_client_cls, write_stream_cls, monkeypatch
):
    uds_env("force")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    writer = AsyncAppendableObjectWriter.from_blob(
        _make_client(storage_client_cls), _blob_with_hold()
    )
    get_rt = AsyncMock()
    with mock.patch(_RUNTIME_GET, get_rt):
        with pytest.raises(CoreSdkUnavailableError, match="temporary_hold"):
            await writer.open()
    get_rt.assert_not_awaited()
    write_stream_cls.assert_not_called()


@pytest.mark.asyncio
async def test_writer_auto_unsupported_blob_attrs_fall_back(
    uds_env, storage_client_cls, write_stream_cls, monkeypatch
):
    uds_env("auto")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    writer = AsyncAppendableObjectWriter.from_blob(
        _make_client(storage_client_cls), _blob_with_hold()
    )
    get_rt = AsyncMock()
    with mock.patch(_RUNTIME_GET, get_rt):
        await writer.open()
    get_rt.assert_not_awaited()
    write_stream_cls.assert_called_once()
    assert writer._uds is None


def _writer_with_session(storage_client_cls, flush_interval=4 * _MiB):
    writer = AsyncAppendableObjectWriter(
        mock.MagicMock(),
        "b",
        "o",
        writer_options={"FLUSH_INTERVAL_BYTES": flush_interval},
    )
    session = mock.MagicMock()
    session.append = AsyncMock()
    persisted = iter(range(1, 100))
    session.flush = AsyncMock(side_effect=lambda: next(persisted) * _MiB)
    session.close = AsyncMock(return_value=77)
    session.finalize = AsyncMock(
        return_value=pb.ObjectResource(
            bucket="projects/_/buckets/b", name="o", generation=3, size=10
        )
    )
    session.has_unflushed_bytes = mock.Mock(return_value=False)
    session.last_persisted_size = 5
    writer._uds = session
    writer._is_stream_open = True
    writer.offset = 0
    writer.persisted_size = 0
    return writer, session


@pytest.mark.asyncio
async def test_writer_uds_open_sets_state(
    uds_env, storage_client_cls, write_stream_cls, monkeypatch
):
    uds_env("force")
    monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/irrelevant.sock")
    session = mock.MagicMock()
    session.open = AsyncMock(return_value=(55, 1024))
    with (
        mock.patch(_RUNTIME_GET, AsyncMock(return_value=mock.Mock())),
        mock.patch(
            "google.cloud.storage.asyncio._uds.write_session.UdsWriteSession",
            return_value=session,
        ),
    ):
        writer = AsyncAppendableObjectWriter(
            _make_client(storage_client_cls), "b", "o", generation=0
        )
        await writer.open(metadata=[("x-goog-user-project", "qp")])
    write_stream_cls.assert_not_called()
    spec = session.open.call_args.args[0]
    assert spec.bucket == "b" and spec.object == "o"
    assert spec.HasField("if_generation_match") and spec.if_generation_match == 0
    assert not spec.HasField("reopen_generation")
    assert spec.quota_project == "qp"
    assert writer._uds is session
    assert (writer.generation, writer.persisted_size, writer.offset) == (55, 1024, 1024)
    assert writer.is_stream_open


def test_writer_uds_open_spec_reopen_and_blob_attrs():
    writer = AsyncAppendableObjectWriter(
        mock.MagicMock(),
        "b",
        "o",
        generation=9,
        write_handle=_storage_v2.BidiWriteHandle(handle=b"wh"),
    )
    writer._routing_token = "rt"
    spec = writer._uds_open_spec(None)
    assert spec.reopen_generation == 9
    assert spec.write_handle == b"wh"
    assert spec.routing_token == "rt"
    assert not spec.HasField("if_generation_match")

    from google.cloud.storage.blob import Blob
    from google.cloud.storage.bucket import Bucket

    blob = Blob("o", bucket=Bucket(client=None, name="b"))
    blob.content_type = "text/plain"
    blob.cache_control = "no-cache"
    blob.metadata = {"k": "v"}
    blob.custom_time = datetime.datetime(
        2026, 1, 2, 3, 4, 5, 6000, tzinfo=datetime.timezone.utc
    )
    creator = AsyncAppendableObjectWriter.from_blob(mock.MagicMock(), blob)
    creator.storage_class = "STANDARD"
    spec = creator._uds_open_spec(None)
    assert not spec.HasField("reopen_generation")
    assert spec.attrs.content_type == "text/plain"
    assert spec.attrs.cache_control == "no-cache"
    assert dict(spec.attrs.metadata) == {"k": "v"}
    assert spec.attrs.storage_class == "STANDARD"
    expected = int(blob.custom_time.timestamp())
    assert (spec.attrs.custom_time_secs, spec.attrs.custom_time_nanos) == (
        expected,
        6000 * 1000,
    )


@pytest.mark.asyncio
async def test_writer_uds_append_honours_flush_interval(storage_client_cls):
    writer, session = _writer_with_session(storage_client_cls, flush_interval=4 * _MiB)
    await writer.append(b"\0" * (10 * _MiB))
    sizes = [len(c.args[0]) for c in session.append.await_args_list]
    assert sizes == [4 * _MiB, 4 * _MiB, 2 * _MiB]
    assert session.flush.await_count == 2
    assert writer.offset == 10 * _MiB
    assert writer.bytes_appended_since_last_flush == 2 * _MiB
    assert writer.persisted_size == 2 * _MiB  # value returned by the 2nd flush
    await writer.append(b"")  # empty append is a no-op
    assert session.append.await_count == 3


@pytest.mark.asyncio
async def test_writer_uds_state_lookup_flush_and_close(storage_client_cls):
    writer, session = _writer_with_session(storage_client_cls)
    assert await writer.state_lookup() == 5  # last persisted size, no flush needed
    session.flush.assert_not_awaited()
    session.has_unflushed_bytes.return_value = True
    assert await writer.state_lookup() == 1 * _MiB
    assert await writer.flush() == 2 * _MiB
    assert writer.offset == 2 * _MiB
    await writer.simple_flush()
    assert session.flush.await_count == 3
    assert await writer.close() == 77
    session.close.assert_awaited_once()
    assert writer._uds is None and not writer.is_stream_open


@pytest.mark.asyncio
async def test_writer_uds_finalize_and_close_finalize(storage_client_cls):
    writer, session = _writer_with_session(storage_client_cls)
    obj = await writer.close(finalize_on_close=True, full_object_checksum=123)
    session.finalize.assert_awaited_once_with(123)
    assert isinstance(obj, _storage_v2.Object)
    assert (obj.name, obj.generation, obj.size) == ("o", 3, 10)
    assert writer.persisted_size == 10 and writer.object_resource is obj
    assert writer._uds is None and not writer.is_stream_open


# --------------------------------------------------------------- helpers


@pytest.mark.parametrize(
    "endpoint,anonymous,expected",
    [
        (None, False, None),
        ("", False, None),
        ("https://storage.googleapis.com/", False, "https://storage.googleapis.com"),
        ("http://localhost:9000", False, "http://localhost:9000"),
        ("localhost:9000", False, "https://localhost:9000"),
        ("localhost:9000", True, "http://localhost:9000"),
        (" storage.example.com:443/ ", False, "https://storage.example.com:443"),
        (
            "dns:///storage.googleapis.com:443",
            False,
            "https://storage.googleapis.com:443",
        ),
        ("https://private.googleapis.com", True, "https://private.googleapis.com"),
    ],
)
def test_normalize_endpoint(endpoint, anonymous, expected):
    assert _config.normalize_endpoint(endpoint, anonymous) == expected


@pytest.mark.parametrize(
    "endpoint",
    [
        "google-c2p:///storage.googleapis.com",
        "GOOGLE-C2P-EXPERIMENTAL:///storage.googleapis.com",
    ],
)
def test_normalize_endpoint_rejects_direct_path(endpoint):
    with pytest.raises(CoreSdkUnavailableError, match="DirectPath"):
        _config.normalize_endpoint(endpoint)


def test_core_sdk_unavailable_error_hierarchy():
    err = CoreSdkUnavailableError("nope")
    assert isinstance(err, exceptions.GoogleAPICallError)
    assert isinstance(err, ValueError)
    assert isinstance(err, RuntimeError)
    assert err.message == "nope"
    assert "nope" in str(err)


def test_unsupported_blob_attrs():
    from google.cloud.storage.blob import Blob
    from google.cloud.storage.bucket import Bucket

    assert _config.unsupported_blob_attrs(None) == []
    blob = Blob("o", bucket=Bucket(client=None, name="b"))
    assert _config.unsupported_blob_attrs(blob) == []
    blob.temporary_hold = False  # explicitly set (even False) cannot be honoured
    blob.event_based_hold = True
    assert _config.unsupported_blob_attrs(blob) == [
        "temporary_hold",
        "event_based_hold",
    ]


def _aio_error(code, details="boom"):
    return grpc.aio.AioRpcError(code, grpc.aio.Metadata(), grpc.aio.Metadata(), details)


def test_to_api_exception_mapping():
    assert isinstance(
        uds_errors.to_api_exception(_aio_error(grpc.StatusCode.NOT_FOUND)),
        exceptions.NotFound,
    )
    assert isinstance(
        uds_errors.to_api_exception(_aio_error(grpc.StatusCode.INVALID_ARGUMENT)),
        exceptions.InvalidArgument,
    )
    assert isinstance(
        uds_errors.to_api_exception(_aio_error(grpc.StatusCode.UNAVAILABLE)),
        exceptions.ServiceUnavailable,
    )
    corrupt = uds_errors.to_api_exception(
        _aio_error(grpc.StatusCode.DATA_LOSS, "crc32c mismatch")
    )
    assert isinstance(corrupt, DataCorruption)
    already = exceptions.NotFound("x")
    assert uds_errors.to_api_exception(already) is already
    other = KeyError("x")
    assert uds_errors.to_api_exception(other) is other


def test_range_error_to_exception_mapping():
    oor = uds_errors.range_error_to_exception(
        pb.RangeError(
            range_id=1, code=grpc.StatusCode.OUT_OF_RANGE.value[0], message="past EOF"
        )
    )
    assert isinstance(oor, exceptions.OutOfRange) and "past EOF" in str(oor)
    assert isinstance(
        uds_errors.range_error_to_exception(pb.RangeError(code=5, message="gone")),
        exceptions.NotFound,
    )
    assert isinstance(
        uds_errors.range_error_to_exception(
            pb.RangeError(checksum_mismatch=True, message="crc")
        ),
        DataCorruption,
    )
    assert isinstance(
        uds_errors.range_error_to_exception(
            pb.RangeError(code=grpc.StatusCode.DATA_LOSS.value[0])
        ),
        DataCorruption,
    )
    assert isinstance(
        uds_errors.range_error_to_exception(pb.RangeError(code=999)), exceptions.Unknown
    )


def test_object_from_resource_json_and_typed_fallback():
    assert uds_errors.object_from_resource(None) is None
    as_json = uds_errors.object_from_resource(
        pb.ObjectResource(
            object_json=json.dumps(
                {
                    "bucket": "projects/_/buckets/b",
                    "name": "o",
                    "generation": "5",
                    "size": "12",
                    "someNewField": 1,
                }
            )
        )
    )
    assert (as_json.bucket, as_json.name, as_json.generation, as_json.size) == (
        "projects/_/buckets/b",
        "o",
        5,
        12,
    )
    typed = uds_errors.object_from_resource(
        pb.ObjectResource(
            bucket="b", name="o", generation=6, size=3, crc32c=0, metadata={"a": "b"}
        )
    )
    assert (typed.name, typed.generation, typed.size) == ("o", 6, 3)
    assert typed.checksums.crc32c == 0  # presence of crc32c=0 is preserved
    assert dict(typed.metadata) == {"a": "b"}
    no_crc = uds_errors.object_from_resource(pb.ObjectResource(name="o"))
    assert (
        "checksums" not in _storage_v2.Object.to_dict(no_crc)
        or not no_crc.checksums.crc32c
    )


def test_prewarm_is_opt_in(uds_env, storage_client_cls, monkeypatch):
    uds_env("auto")
    with mock.patch.object(async_grpc_client, "_prewarm_uds") as prewarm:
        _make_client(storage_client_cls)
        prewarm.assert_not_called()
        monkeypatch.setenv(_config.ENV_PREWARM, "1")
        client = _make_client(storage_client_cls)
        prewarm.assert_called_once_with(client)
