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

"""Hermetic unit tests for :mod:`google.cloud.storage.asyncio._uds.runtime`.

The ``gcs-core-server`` daemon, the ``grpc.aio`` channel and the shared-memory
regions are replaced by in-process fakes, so every branch of :class:`UdsRuntime`
(startup, session creation, token refresh, region pooling, shutdown) runs without
spawning processes or touching the network.
"""

import asyncio
import datetime
import importlib.util
import os
import threading
import time
from types import SimpleNamespace

import grpc
import pytest
from google.api_core import client_options as client_options_lib
from google.auth.credentials import AnonymousCredentials

from google.cloud.storage import __version__
from google.cloud.storage.asyncio._uds import _config, runtime
from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError

TARGET = "unix:/tmp/fake-gcs-core.sock"
SLOT = 1024
ALL_FEATURES = ("bidi-read", "bidi-write", "bidi-read-shm", "bidi-write-shm")
EXPIRY = datetime.datetime(2030, 1, 2, 3, 4, 5)
EXPIRY_UNIX = 1893553445


def _rpc_error(code=grpc.StatusCode.UNAVAILABLE, details="server down"):
    return grpc.aio.AioRpcError(
        code, grpc.aio.Metadata(), grpc.aio.Metadata(), details=details
    )


def _server_info(features=ALL_FEATURES):
    return pb.ServerInfo(
        server_version="9.9",
        features=list(features),
        shm_region_size=4 * SLOT,
        shm_slot_size=SLOT,
    )


class _FakeManager:
    """Stand-in for :class:`ServerManager` (no binary, no spawning)."""

    mode = "shared"

    def __init__(self, endpoint=None, universe_domain=None):
        self.endpoint = endpoint
        self.universe_domain = universe_domain
        self.ensure_threads = []

    def ensure_server(self):
        self.ensure_threads.append(threading.current_thread())
        return TARGET

    def shm_socket_path(self, target):
        return target + ".shm"


class _FakeChannel:
    """Stand-in for a ``grpc.aio.Channel``; unary RPCs dispatch to ``handlers``."""

    def __init__(self, target, options, handlers):
        self.target = target
        self.options = dict(options)
        self.handlers = handlers
        self.requests = []
        self.closed = False

    def unary_unary(self, method, request_serializer, response_deserializer):
        name = method.rsplit("/", 1)[1]

        async def invoke(request, timeout=None):
            self.requests.append((name, request, timeout))
            return await self.handlers[name](request)

        return invoke

    def stream_stream(self, method, request_serializer, response_deserializer):
        return method

    async def close(self):
        self.closed = True


class _Creds:
    """Minimal ``google.auth`` credentials double."""

    def __init__(self, valid=False, token=None, expiry=EXPIRY, error=None):
        self.valid = valid
        self.token = token
        self.expiry = expiry
        self.error = error
        self.refreshes = 0

    def refresh(self, request):
        if self.error is not None:
            raise self.error
        self.refreshes += 1
        self.token = f"tok-{self.refreshes}"
        self.valid = True


class _FakeRegion:
    def __init__(self, closed=False, free=True):
        self.closed = closed
        self.free = free

    def all_free(self):
        return self.free

    def close(self):
        self.closed = True


@pytest.fixture
def env(monkeypatch):
    """Isolated runtime registry + fake daemon / channel factories."""
    monkeypatch.setattr(runtime, "_instances", {})
    monkeypatch.setattr(runtime, "_locks", {})
    for name in (
        _config.ENV_SOCKET,
        _config.ENV_SHM,
        _config.ENV_TOPOLOGY,
        runtime.ENV_MAX_REGIONS,
        "GOOGLE_CLOUD_UNIVERSE_DOMAIN",
    ):
        monkeypatch.delenv(name, raising=False)

    state = SimpleNamespace(channels=[], managers=[], mode="shared")

    async def get_server_info(request):
        return _server_info()

    async def create_session(request):
        return pb.CreateSessionResponse(session_id="sess-1")

    async def stats(request):
        return pb.StatsResponse()

    state.handlers = {
        "GetServerInfo": get_server_info,
        "CreateSession": create_session,
        "Stats": stats,
    }

    def make_manager(endpoint=None, universe_domain=None):
        manager = _FakeManager(endpoint, universe_domain)
        manager.mode = state.mode
        state.managers.append(manager)
        return manager

    def make_channel(target, options):
        channel = _FakeChannel(target, options, state.handlers)
        state.channels.append(channel)
        return channel

    monkeypatch.setattr(runtime, "ServerManager", make_manager)
    monkeypatch.setattr(runtime.grpc.aio, "insecure_channel", make_channel)
    return state


def _new_runtime(endpoint=None, anonymous=False, credentials=None, quota=None):
    return runtime.UdsRuntime(
        asyncio.get_running_loop(), endpoint, anonymous, credentials, quota
    )


def _wire_unary(rt, env):
    """Attaches the unary stubs of a fake channel without running ``_start``."""
    channel = _FakeChannel(TARGET, (), env.handlers)
    rt.channel = channel
    for attr, name in (
        ("_create_session", "CreateSession"),
        ("_update_token", "UpdateToken"),
        ("_stats", "Stats"),
    ):
        setattr(rt, attr, channel.unary_unary("/svc/" + name, None, None))
    return channel


# ------------------------------------------------------------------ module / config


def test_import_without_register_at_fork(monkeypatch):
    """Platforms without ``os.register_at_fork`` can still import the module."""
    monkeypatch.delattr(os, "register_at_fork")
    spec = importlib.util.spec_from_file_location(
        "_uds_runtime_without_fork_hooks", runtime.__file__
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module._instances == {}
    assert module.REQUIRED_FEATURES == runtime.REQUIRED_FEATURES


def test_client_config_dict_options():
    creds = AnonymousCredentials()
    client = SimpleNamespace(
        _credentials=creds,
        _client_options={"api_endpoint": "localhost:9", "quota_project_id": "qp"},
    )
    assert runtime._client_config(client) == ("http://localhost:9", True, creds, "qp")


def test_client_config_object_options():
    creds = _Creds()
    client = SimpleNamespace(
        _credentials=creds,
        _client_options=client_options_lib.ClientOptions(quota_project_id="qp2"),
    )
    assert runtime._client_config(client) == (None, False, creds, "qp2")


def test_client_config_without_options():
    assert runtime._client_config(object()) == (None, False, None, None)


# ------------------------------------------------------------------ lookup


@pytest.mark.asyncio
async def test_get_concurrent_callers_share_one_runtime(env, monkeypatch):
    started = []

    async def fake_start(self):
        started.append(self)
        await asyncio.sleep(0)  # let the second caller queue up on the lock

    monkeypatch.setattr(runtime.UdsRuntime, "_start", fake_start)
    creds = _Creds()
    client = SimpleNamespace(_credentials=creds, _client_options=None)

    first, second = await asyncio.gather(
        runtime.get_runtime(client), runtime.get_runtime(client)
    )
    assert first is second
    assert started == [first]
    assert first.credentials is creds
    assert await runtime.get_runtime(client) is first

    # A closed runtime is replaced on the next lookup.
    first.closed = True
    replacement = await runtime.get_runtime(client)
    assert replacement is not first
    assert started == [first, replacement]


# ------------------------------------------------------------------ startup


@pytest.mark.asyncio
async def test_start_shared_daemon_anonymous_session(env, monkeypatch):
    monkeypatch.setenv("GOOGLE_CLOUD_UNIVERSE_DOMAIN", "example.com")
    rt = _new_runtime(anonymous=True)
    await rt._start()

    (manager,) = env.managers
    assert manager.endpoint is None
    assert manager.universe_domain == "example.com"
    # The shared daemon is ensured from an executor thread.
    assert manager.ensure_threads != [threading.current_thread()]
    assert rt.target == TARGET
    assert rt.shm_path == TARGET + ".shm"

    (channel,) = env.channels
    assert channel.target == TARGET
    assert channel.options["grpc.default_authority"] == "localhost"
    assert rt.bidi_read == "/gcscore.v1.GcsCore/BidiReadObject"
    assert rt.bidi_write == "/gcscore.v1.GcsCore/BidiWriteObject"
    assert rt.server_info == _server_info()
    assert rt.user_agent == f"gcloud-python/{__version__} uds/9.9"

    (_, session_req, timeout) = channel.requests[1]
    assert session_req == pb.CreateSessionRequest(anonymous=True)
    assert timeout == 30
    assert rt.session_id == "sess-1"
    assert rt.metadata == (("x-session", "sess-1"),)
    assert rt._refresh_task is None

    assert await rt.stats() == pb.StatsResponse()
    assert channel.requests[-1] == ("Stats", pb.StatsRequest(), 10)
    await rt.close()
    assert channel.closed


@pytest.mark.asyncio
async def test_start_child_daemon_is_ensured_on_loop_thread(env):
    env.mode = "child"
    rt = _new_runtime()
    await rt._start()
    (manager,) = env.managers
    assert manager.ensure_threads == [threading.current_thread()]
    # No credentials, no endpoint: nothing to create a session for.
    assert [name for name, _, _ in env.channels[0].requests] == ["GetServerInfo"]
    assert rt.session_id is None
    await rt.close()


@pytest.mark.asyncio
async def test_start_get_server_info_failure(env):
    async def get_server_info(request):
        raise _rpc_error()

    env.handlers["GetServerInfo"] = get_server_info
    rt = _new_runtime()
    with pytest.raises(CoreSdkUnavailableError, match="GetServerInfo on .* failed"):
        await rt._start()
    assert rt.closed
    assert env.channels[0].closed


@pytest.mark.asyncio
async def test_start_server_missing_required_features(env):
    async def get_server_info(request):
        return _server_info(features=("bidi-read",))

    env.handlers["GetServerInfo"] = get_server_info
    rt = _new_runtime()
    with pytest.raises(CoreSdkUnavailableError, match="lacks required features"):
        await rt._start()
    assert rt.closed
    assert env.channels[0].closed


# ------------------------------------------------------------------ sessions


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "anonymous, endpoint, attached, expected",
    [
        (
            True,
            "http://h:1",
            False,
            pb.CreateSessionRequest(anonymous=True, endpoint="http://h:1"),
        ),
        (
            False,
            "https://h:1",
            True,
            pb.CreateSessionRequest(endpoint="https://h:1"),
        ),
        (False, "https://h:1", False, None),
        (False, None, True, None),
    ],
    ids=["anonymous-endpoint", "adc-attached-endpoint", "adc-spawned", "adc-default"],
)
async def test_maybe_create_session_without_credentials(
    env, monkeypatch, anonymous, endpoint, attached, expected
):
    if attached:
        monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/attached.sock")
    rt = _new_runtime(endpoint=endpoint, anonymous=anonymous)
    channel = _wire_unary(rt, env)
    await rt._maybe_create_session()
    if expected is None:
        assert channel.requests == []
        assert rt.session_id is None
    else:
        assert channel.requests == [("CreateSession", expected, 30)]
        assert rt.session_id == "sess-1"
    assert rt._refresh_task is None


@pytest.mark.asyncio
@pytest.mark.parametrize("attached", [True, False], ids=["attached", "spawned"])
async def test_maybe_create_session_with_credentials(env, monkeypatch, attached):
    if attached:
        monkeypatch.setenv(_config.ENV_SOCKET, "/tmp/attached.sock")
    creds = _Creds()
    rt = _new_runtime(endpoint="https://h:1", credentials=creds, quota="qp")
    channel = _wire_unary(rt, env)
    await rt._maybe_create_session()

    ((name, req, _),) = channel.requests
    assert name == "CreateSession"
    assert req.access_token == "tok-1"
    assert req.expiry_unix_secs == EXPIRY_UNIX
    assert req.quota_project == "qp"
    assert req.endpoint == ("https://h:1" if attached else "")
    assert rt.metadata == (("x-session", "sess-1"),)

    task = rt._refresh_task
    assert task is not None and not task.done()
    await rt.close()  # cancels the refresh loop; no channel-less errors
    with pytest.raises(asyncio.CancelledError):
        await task
    assert channel.closed


@pytest.mark.asyncio
async def test_create_session_failure(env):
    async def create_session(request):
        raise _rpc_error(grpc.StatusCode.PERMISSION_DENIED, "nope")

    env.handlers["CreateSession"] = create_session
    rt = _new_runtime(anonymous=True)
    channel = _wire_unary(rt, env)
    with pytest.raises(CoreSdkUnavailableError, match="CreateSession failed"):
        await rt._maybe_create_session()
    assert rt.closed
    assert channel.closed


# ------------------------------------------------------------------ tokens


@pytest.mark.asyncio
async def test_fetch_token_reuses_valid_token_without_expiry():
    creds = _Creds(valid=True, token="cached", expiry=None)
    rt = _new_runtime(credentials=creds)
    assert await rt._fetch_token() == ("cached", 0)
    assert creds.refreshes == 0


@pytest.mark.asyncio
async def test_fetch_token_force_refreshes():
    creds = _Creds(valid=True, token="cached")
    rt = _new_runtime(credentials=creds)
    assert await rt._fetch_token(force=True) == ("tok-1", EXPIRY_UNIX)
    assert creds.refreshes == 1


@pytest.mark.asyncio
async def test_fetch_token_refresh_failure():
    rt = _new_runtime(credentials=_Creds(error=RuntimeError("metadata server down")))
    with pytest.raises(
        CoreSdkUnavailableError, match="cannot obtain an access token: metadata"
    ):
        await rt._fetch_token()


@pytest.fixture
def fast_sleep(monkeypatch):
    """Records ``asyncio.sleep`` delays and turns them into immediate yields."""
    real_sleep = asyncio.sleep
    delays = []

    async def sleep(delay):
        delays.append(delay)
        await real_sleep(0)

    monkeypatch.setattr(asyncio, "sleep", sleep)
    return delays


@pytest.mark.asyncio
async def test_refresh_loop_pushes_new_token_until_closed(env, fast_sleep):
    creds = _Creds(valid=True, token="old")
    rt = _new_runtime(credentials=creds)
    channel = _wire_unary(rt, env)
    rt.session_id = "sess-1"
    updates = []

    async def update_token(request):
        updates.append(request)
        if len(updates) == 2:
            rt.closed = True
        return pb.Empty()

    env.handlers["UpdateToken"] = update_token
    await asyncio.wait_for(rt._refresh_loop(0), 5)

    assert updates == [
        pb.UpdateTokenRequest(
            session_id="sess-1", access_token="tok-1", expiry_unix_secs=EXPIRY_UNIX
        ),
        pb.UpdateTokenRequest(
            session_id="sess-1", access_token="tok-2", expiry_unix_secs=EXPIRY_UNIX
        ),
    ]
    assert [timeout for _, _, timeout in channel.requests] == [30, 30]
    # No expiry => 5 minutes; known expiry => 5 minutes before it.
    assert fast_sleep[0] == 300.0
    assert fast_sleep[1] == pytest.approx(EXPIRY_UNIX - time.time() - 300, abs=60)


@pytest.mark.asyncio
async def test_refresh_loop_propagates_cancellation(env, fast_sleep):
    rt = _new_runtime(credentials=_Creds())
    _wire_unary(rt, env)
    rt.session_id = "sess-1"
    entered = asyncio.Event()

    async def update_token(request):
        entered.set()
        await asyncio.Event().wait()  # never answers

    env.handlers["UpdateToken"] = update_token
    task = asyncio.ensure_future(rt._refresh_loop(int(time.time()) + 60))
    await asyncio.wait_for(entered.wait(), 5)
    assert fast_sleep == [30.0]  # clamped to the 30 s minimum
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task


# ------------------------------------------------------------------ regions


def _shm_runtime(features=ALL_FEATURES):
    rt = _new_runtime()
    rt.server_info = _server_info(features)
    rt.shm_path = TARGET + ".shm"
    return rt


@pytest.mark.asyncio
async def test_shm_enabled(env, monkeypatch):
    rt = _new_runtime()
    assert not rt.shm_enabled  # no server info yet
    rt.server_info = _server_info()
    assert rt.shm_enabled
    monkeypatch.setenv(_config.ENV_SHM, " Off ")
    assert not rt.shm_enabled


@pytest.mark.asyncio
async def test_read_region_is_connected_once_and_cached(env, monkeypatch):
    connects = []

    def connect(path, slot_size, writable):
        connects.append((path, slot_size, writable))
        return _FakeRegion()

    monkeypatch.setattr(runtime, "ShmRegion", SimpleNamespace(connect=connect))
    rt = _shm_runtime()
    region = await rt.read_region()
    assert await rt.read_region() is region
    assert connects == [(TARGET + ".shm", SLOT, False)]
    assert rt._live_regions == 1

    region.closed = True  # e.g. torn down by the server => reconnect
    rt._live_regions = 0
    assert await rt.read_region() is not region
    assert len(connects) == 2


@pytest.mark.asyncio
async def test_read_region_respects_region_limit(env, monkeypatch):
    monkeypatch.setenv(runtime.ENV_MAX_REGIONS, "1")
    rt = _shm_runtime()
    assert rt._max_regions == 1
    rt._live_regions = 1
    assert await rt.read_region() is None


@pytest.mark.asyncio
async def test_read_region_failure_falls_back_to_inline_for_good(env, monkeypatch):
    connects = []

    def connect(path, slot_size, writable):
        connects.append(path)
        raise CoreSdkUnavailableError("no memfd for you")

    monkeypatch.setattr(runtime, "ShmRegion", SimpleNamespace(connect=connect))
    rt = _shm_runtime()
    assert await rt.read_region() is None
    assert rt._read_region_failed
    assert await rt.read_region() is None
    assert len(connects) == 1
    assert rt._live_regions == 0


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "features", [ALL_FEATURES[:3], ()], ids=["no-write-shm", "no-shm"]
)
async def test_lease_write_region_disabled(env, features):
    rt = _shm_runtime(features)
    assert await rt.lease_write_region() is None


@pytest.mark.asyncio
async def test_lease_write_region_pooling(env, monkeypatch):
    connects = []

    def connect(path, slot_size, writable):
        connects.append((path, slot_size, writable))
        return _FakeRegion()

    monkeypatch.setattr(runtime, "WriteRegion", SimpleNamespace(connect=connect))
    rt = _shm_runtime()
    rt._max_regions = 3

    fresh = await rt.lease_write_region()
    assert connects == [(TARGET + ".shm", SLOT, True)]
    assert rt._live_regions == 1

    # Idle pool: reusable regions are handed out again, stale ones discarded.
    good, busy, dead = _FakeRegion(), _FakeRegion(free=False), _FakeRegion(closed=True)
    rt._idle_write_regions = [good, busy, dead]
    rt._live_regions = 3
    assert await rt.lease_write_region() is good
    assert busy.closed
    assert rt._live_regions == 2  # only the still-open busy region was counted
    assert rt._idle_write_regions == []

    rt._live_regions = 3
    assert await rt.lease_write_region() is None  # region limit reached
    assert len(connects) == 1

    rt.return_write_region(None, reusable=True)
    rt.return_write_region(fresh, reusable=True)
    assert rt._idle_write_regions == [fresh]
    rt.return_write_region(good, reusable=False)
    assert good.closed
    assert rt._live_regions == 2


@pytest.mark.asyncio
async def test_lease_write_region_connect_failure(env, monkeypatch):
    def connect(path, slot_size, writable):
        raise CoreSdkUnavailableError("no memfd for you")

    monkeypatch.setattr(runtime, "WriteRegion", SimpleNamespace(connect=connect))
    rt = _shm_runtime()
    assert await rt.lease_write_region() is None
    assert rt._live_regions == 0


# ------------------------------------------------------------------ shutdown


@pytest.mark.asyncio
async def test_close_releases_everything(env):
    rt = _shm_runtime()
    channel = _wire_unary(rt, env)
    refresh = asyncio.ensure_future(asyncio.Event().wait())
    idle, read = _FakeRegion(), _FakeRegion()
    rt._refresh_task = refresh
    rt._idle_write_regions = [idle]
    rt._read_region = read
    rt._live_regions = 2

    await rt.close()
    assert rt.closed
    assert idle.closed and read.closed
    assert rt._idle_write_regions == [] and rt._read_region is None
    assert rt._live_regions == 0
    assert channel.closed
    with pytest.raises(asyncio.CancelledError):
        await refresh

    # Returning a region to a closed runtime discards it.
    late = _FakeRegion()
    rt.return_write_region(late, reusable=True)
    assert late.closed and rt._idle_write_regions == []


@pytest.mark.asyncio
async def test_close_without_channel(env):
    rt = _new_runtime()
    await rt.close()
    assert rt.closed


@pytest.mark.asyncio
async def test_close_all_only_closes_runtimes_of_the_running_loop(env):
    ours = _new_runtime()
    other_loop = asyncio.new_event_loop()
    try:
        theirs = runtime.UdsRuntime(other_loop, None, False, None, None)
        runtime._instances.update({"ours": ours, "theirs": theirs})
        await runtime.close_all()
        assert runtime._instances == {"theirs": theirs}
        assert ours.closed
        assert not theirs.closed
    finally:
        other_loop.close()
