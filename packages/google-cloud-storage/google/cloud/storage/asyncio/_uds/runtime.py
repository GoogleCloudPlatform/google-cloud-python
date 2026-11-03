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

"""Per-process / per-event-loop runtime for the gRPC-over-UDS backend.

A :class:`UdsRuntime` owns the ``grpc.aio`` channel to ``gcs-core-server``, the
negotiated :class:`ServerInfo`, the optional credential-lending session, the
process-wide read region and a pool of per-writer write regions.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
import weakref
from typing import Dict, List, Optional, Tuple

import grpc

from google.cloud.storage.asyncio._uds import _config
from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError
from google.cloud.storage.asyncio._uds.server_manager import ServerManager
from google.cloud.storage.asyncio._uds.shm import ShmRegion, WriteRegion

logger = logging.getLogger(__name__)

_SERVICE = "/gcscore.v1.GcsCore/"
_MAX_MSG = 64 * 1024 * 1024
REQUIRED_FEATURES = ("bidi-read", "bidi-write")
ENV_MAX_REGIONS = "GOOGLE_CLOUD_STORAGE_UDS_MAX_REGIONS"

_instances: Dict[tuple, "UdsRuntime"] = {}
_locks: Dict[tuple, asyncio.Lock] = {}


def _reset_after_fork() -> None:  # pragma: NO COVER - exercised in forked children
    _instances.clear()
    _locks.clear()


if hasattr(os, "register_at_fork"):
    os.register_at_fork(after_in_child=_reset_after_fork)


def _client_config(client) -> Tuple[Optional[str], bool, object, Optional[str]]:
    """Returns ``(normalized_endpoint, anonymous, credentials, quota_project)``."""
    from google.auth import credentials as auth_credentials

    creds = getattr(client, "_credentials", None)
    anonymous = isinstance(creds, auth_credentials.AnonymousCredentials)
    options = getattr(client, "_client_options", None)
    endpoint = _config.normalize_endpoint(_config.api_endpoint_of(options), anonymous)
    quota = None
    if isinstance(options, dict):
        quota = options.get("quota_project_id")
    elif options is not None:
        quota = getattr(options, "quota_project_id", None)
    return endpoint, anonymous, creds, quota


class UdsRuntime:
    """Connection to one ``gcs-core-server`` for one event loop in one process."""

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        endpoint: Optional[str],
        anonymous: bool,
        credentials,
        quota_project: Optional[str],
    ) -> None:
        self._loop_ref = weakref.ref(loop)
        self.pid = os.getpid()
        self.endpoint = endpoint
        self.anonymous = anonymous
        self.credentials = credentials
        self.quota_project = quota_project
        self.channel: Optional[grpc.aio.Channel] = None
        self.server_info: Optional[pb.ServerInfo] = None
        self.target: Optional[str] = None
        self.shm_path: Optional[str] = None
        self.session_id: Optional[str] = None
        self.metadata: Tuple[Tuple[str, str], ...] = ()
        self.user_agent = ""
        self.closed = False
        self._read_region: Optional[ShmRegion] = None
        self._read_region_failed = False
        self._idle_write_regions: List[WriteRegion] = []
        self._live_regions = 0
        self._max_regions = int(os.environ.get(ENV_MAX_REGIONS, "16") or 16)
        self._refresh_task: Optional[asyncio.Task] = None
        self.manager: Optional[ServerManager] = None

    # ------------------------------------------------------------------ lookup

    @classmethod
    async def get(cls, client) -> "UdsRuntime":
        loop = asyncio.get_running_loop()
        endpoint, anonymous, creds, quota = _client_config(client)
        explicit = None if (creds is None or anonymous) else id(creds)
        key = (os.getpid(), id(loop), endpoint, anonymous, explicit, quota)
        rt = _instances.get(key)
        if rt is not None and rt._usable(loop):
            return rt
        lock = _locks.get(key)
        if lock is None or getattr(lock, "_uds_loop", None) is not loop:
            lock = asyncio.Lock()
            lock._uds_loop = loop  # type: ignore[attr-defined]
            _locks[key] = lock
        async with lock:
            rt = _instances.get(key)
            if rt is not None and rt._usable(loop):
                return rt
            rt = cls(loop, endpoint, anonymous, None if explicit is None else creds, quota)
            await rt._start()
            _instances[key] = rt
            return rt

    def _usable(self, loop) -> bool:
        return (
            not self.closed
            and self.pid == os.getpid()
            and self._loop_ref() is loop
            and not loop.is_closed()
        )

    # ------------------------------------------------------------------ startup

    async def _start(self) -> None:
        loop = asyncio.get_running_loop()
        universe = os.environ.get("GOOGLE_CLOUD_UNIVERSE_DOMAIN") or None
        self.manager = ServerManager(endpoint=self.endpoint, universe_domain=universe)
        if self.manager.mode == "child":
            # PR_SET_PDEATHSIG fires when the spawning *thread* exits, so a 1:1 child
            # daemon is spawned from the (long-lived) event-loop thread, not an executor.
            self.target = self.manager.ensure_server()
        else:
            self.target = await loop.run_in_executor(None, self.manager.ensure_server)
        self.shm_path = self.manager.shm_socket_path(self.target)
        self.channel = grpc.aio.insecure_channel(
            self.target,
            options=[
                ("grpc.default_authority", "localhost"),
                ("grpc.max_receive_message_length", _MAX_MSG),
                ("grpc.max_send_message_length", _MAX_MSG),
                ("grpc.http2.lookahead_bytes", 4 * 1024 * 1024),
            ],
        )
        self._get_server_info = self.channel.unary_unary(
            _SERVICE + "GetServerInfo",
            request_serializer=pb.Empty.SerializeToString,
            response_deserializer=pb.ServerInfo.FromString,
        )
        self._create_session = self.channel.unary_unary(
            _SERVICE + "CreateSession",
            request_serializer=pb.CreateSessionRequest.SerializeToString,
            response_deserializer=pb.CreateSessionResponse.FromString,
        )
        self._update_token = self.channel.unary_unary(
            _SERVICE + "UpdateToken",
            request_serializer=pb.UpdateTokenRequest.SerializeToString,
            response_deserializer=pb.Empty.FromString,
        )
        self._stats = self.channel.unary_unary(
            _SERVICE + "Stats",
            request_serializer=pb.StatsRequest.SerializeToString,
            response_deserializer=pb.StatsResponse.FromString,
        )
        self.bidi_read = self.channel.stream_stream(
            _SERVICE + "BidiReadObject",
            request_serializer=pb.BidiReadObjectRequest.SerializeToString,
            response_deserializer=pb.BidiReadObjectResponse.FromString,
        )
        self.bidi_write = self.channel.stream_stream(
            _SERVICE + "BidiWriteObject",
            request_serializer=pb.BidiWriteObjectRequest.SerializeToString,
            response_deserializer=pb.BidiWriteObjectResponse.FromString,
        )
        try:
            self.server_info = await self._get_server_info(pb.Empty(), timeout=15)
        except grpc.aio.AioRpcError as exc:
            await self.close()
            raise CoreSdkUnavailableError(
                f"GetServerInfo on {self.target} failed: {exc.code()} {exc.details()}"
            ) from exc
        missing = [f for f in REQUIRED_FEATURES if f not in self.server_info.features]
        if missing:
            await self.close()
            raise CoreSdkUnavailableError(
                f"gcs-core-server {self.server_info.server_version} lacks required "
                f"features {missing} (has {list(self.server_info.features)})"
            )
        from google.cloud.storage import __version__

        self.user_agent = (
            f"gcloud-python/{__version__} uds/{self.server_info.server_version}"
        )
        await self._maybe_create_session()

    async def _maybe_create_session(self) -> None:
        req = None
        expiry = 0
        attached = bool(os.environ.get(_config.ENV_SOCKET))
        if self.anonymous:
            req = pb.CreateSessionRequest(anonymous=True)
            if self.endpoint:
                req.endpoint = self.endpoint
        elif self.credentials is not None:
            token, expiry = await self._fetch_token()
            req = pb.CreateSessionRequest(
                access_token=token,
                expiry_unix_secs=expiry,
                quota_project=self.quota_project or "",
            )
            if self.endpoint and attached:
                req.endpoint = self.endpoint
        elif self.endpoint and attached:
            # Pre-started daemon: select the endpoint per session (shared daemon ADC).
            req = pb.CreateSessionRequest(endpoint=self.endpoint)
        if req is None:
            return
        try:
            resp = await self._create_session(req, timeout=30)
        except grpc.aio.AioRpcError as exc:
            await self.close()
            raise CoreSdkUnavailableError(
                f"CreateSession failed: {exc.code()} {exc.details()}"
            ) from exc
        self.session_id = resp.session_id
        self.metadata = (("x-session", resp.session_id),)
        if self.credentials is not None:
            self._refresh_task = asyncio.get_running_loop().create_task(
                self._refresh_loop(expiry)
            )

    async def _fetch_token(self, force: bool = False) -> Tuple[str, int]:
        import calendar

        import google.auth.transport.requests

        creds = self.credentials

        def _refresh():
            if force or not getattr(creds, "valid", False) or not getattr(creds, "token", None):
                creds.refresh(google.auth.transport.requests.Request())
            expiry = getattr(creds, "expiry", None)
            exp = calendar.timegm(expiry.utctimetuple()) if expiry is not None else 0
            return creds.token, exp

        try:
            return await asyncio.get_running_loop().run_in_executor(None, _refresh)
        except Exception as exc:
            raise CoreSdkUnavailableError(f"cannot obtain an access token: {exc}") from exc

    async def _refresh_loop(self, expiry: int) -> None:
        while not self.closed:
            delay = 300.0 if not expiry else max(30.0, expiry - time.time() - 300)
            await asyncio.sleep(delay)
            try:
                token, expiry = await self._fetch_token(force=True)
                await self._update_token(
                    pb.UpdateTokenRequest(
                        session_id=self.session_id,
                        access_token=token,
                        expiry_unix_secs=expiry,
                    ),
                    timeout=30,
                )
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # pragma: NO COVER - best effort
                logger.warning("UDS session token refresh failed: %s", exc)

    # ------------------------------------------------------------------ regions

    @property
    def shm_enabled(self) -> bool:
        if os.environ.get(_config.ENV_SHM, "").strip().lower() in ("off", "0", "false"):
            return False
        info = self.server_info
        return bool(
            info is not None
            and info.shm_region_size >= info.shm_slot_size > 0
            and "bidi-read-shm" in info.features
        )

    async def read_region(self) -> Optional[ShmRegion]:
        """Returns the process-wide read region (``None`` => inline payloads)."""
        if self._read_region is not None and not self._read_region.closed:
            return self._read_region
        if self._read_region_failed or not self.shm_enabled:
            return None
        if self._live_regions >= self._max_regions:
            return None
        try:
            region = await asyncio.get_running_loop().run_in_executor(
                None,
                lambda: ShmRegion.connect(
                    self.shm_path, self.server_info.shm_slot_size, writable=False
                ),
            )
        except CoreSdkUnavailableError as exc:
            logger.warning("UDS read region unavailable, using inline payloads: %s", exc)
            self._read_region_failed = True
            return None
        self._read_region = region
        self._live_regions += 1
        return region

    async def lease_write_region(self) -> Optional[WriteRegion]:
        """Leases a write region for one writer (``None`` => inline payloads)."""
        if not self.shm_enabled or "bidi-write-shm" not in self.server_info.features:
            return None
        while self._idle_write_regions:
            region = self._idle_write_regions.pop()
            if not region.closed and region.all_free():
                return region
            self._discard(region)
        if self._live_regions >= self._max_regions:
            return None
        try:
            region = await asyncio.get_running_loop().run_in_executor(
                None,
                lambda: WriteRegion.connect(
                    self.shm_path, self.server_info.shm_slot_size, writable=True
                ),
            )
        except CoreSdkUnavailableError as exc:
            logger.warning("UDS write region unavailable, using inline payloads: %s", exc)
            return None
        self._live_regions += 1
        return region

    def return_write_region(self, region: Optional[WriteRegion], reusable: bool) -> None:
        if region is None:
            return
        if reusable and not self.closed and not region.closed and region.all_free():
            self._idle_write_regions.append(region)
        else:
            self._discard(region)

    def _discard(self, region: ShmRegion) -> None:
        if not region.closed:
            region.close()
            self._live_regions = max(0, self._live_regions - 1)

    async def stats(self) -> pb.StatsResponse:
        return await self._stats(pb.StatsRequest(), timeout=10)

    async def close(self) -> None:
        self.closed = True
        if self._refresh_task is not None:
            self._refresh_task.cancel()
        for r in self._idle_write_regions:
            self._discard(r)
        self._idle_write_regions.clear()
        if self._read_region is not None:
            self._discard(self._read_region)
            self._read_region = None
        if self.channel is not None:
            await self.channel.close()


async def get_runtime(client) -> UdsRuntime:
    """Returns the runtime for ``client`` (attaching to / spawning the daemon)."""
    return await UdsRuntime.get(client)


async def close_all() -> None:
    """Closes every runtime bound to the running loop (tests / shutdown)."""
    loop = asyncio.get_running_loop()
    for key, rt in list(_instances.items()):
        if rt._loop_ref() is loop:
            _instances.pop(key, None)
            await rt.close()
