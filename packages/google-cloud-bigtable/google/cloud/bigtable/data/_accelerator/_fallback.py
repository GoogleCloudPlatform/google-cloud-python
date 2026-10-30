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
#
"""Client-side fallback policy for accelerator-routed RPCs.

A daemon that cannot open any sessions replies ``UNIMPLEMENTED``, and the routing
layer transparently retries the call on the native client. The first
``UNIMPLEMENTED`` reply trips a sticky breaker so a persistently-degraded daemon
stops being dialed at all. A daemon whose subprocess has died mid-flight trips
the breaker immediately — it will never recover.

The same breaker also carries a reversible "degraded" flag, set by the health
monitor when the daemon is up but too starved to answer its own health check;
see :class:`AcceleratorBreaker`.

Any other gRPC error is a real, daemon-served result the native client would
reproduce (the daemon owns retries, so it has already exhausted them), so it is
translated to the corresponding ``google.api_core`` exception and raised without
falling back.

This module is plain sync-only logic shared verbatim by the async and generated
sync clients; ``grpc.RpcError`` is the common base of both ``grpc.RpcError`` and
``grpc.aio.AioRpcError``, so no CrossSync branching is needed here.
"""

from __future__ import annotations

import logging
import threading
from typing import TYPE_CHECKING

from google.api_core import exceptions as core_exceptions
from grpc import RpcError, StatusCode

from google.cloud.bigtable.data.exceptions import InvalidChunk

if TYPE_CHECKING:
    from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

_LOGGER = logging.getLogger(__name__)


class _AcceleratorFallback(Exception):
    """Internal signal that an accelerator attempt should be retried natively.

    Never escapes the data target method that raises it: the method catches it
    and falls through to the native code path.
    """


class AcceleratorBreaker:
    """Tracks accelerator health and decides when to stop using it.

    One instance per Table. Thread-safe so the generated sync client can share a
    Table across threads. There are two independent reasons to bypass, and they
    differ in whether they can be undone:

    * **Tripped** — permanent. The first ``UNIMPLEMENTED`` reply (the daemon
      understands the RPC shape but has no working sessions), or an explicit
      :meth:`trip` when the daemon subprocess is found dead. Neither condition
      recovers, so the accelerator is abandoned for the life of the Table.
    * **Degraded** — reversible. Set by the health monitor when the daemon stops
      answering its own health check promptly (see
      ``_async/_accelerator_health.py``). A daemon starved of CPU recovers when
      the load that starved it goes away, so this must clear again — routing
      permanently away from the accelerator on one bad minute would be a far
      worse outcome than the slow calls it avoided.

    Keeping the two flags separate is what makes that safe: :meth:`set_degraded`
    can never resurrect an accelerator that :meth:`trip` has given up on. Each
    flag is its own :class:`threading.Event`, so :meth:`bypass` — which runs on
    every routed RPC — stays a pair of lock-free reads. The two are never read
    as a pair: either one being set already means bypass.
    """

    def __init__(self):
        self._tripped = threading.Event()
        self._degraded = threading.Event()
        self._trip_lock = threading.Lock()

    def bypass(self) -> bool:
        """Whether the accelerator should be skipped for calls made right now."""
        return self._tripped.is_set() or self._degraded.is_set()

    def trip(self) -> bool:
        """Permanently bypass the accelerator (e.g. the daemon process died).

        Returns ``True`` on the first call that transitions the breaker to
        tripped, and ``False`` if it was already tripped.
        """
        if self._tripped.is_set():
            return False
        with self._trip_lock:
            if self._tripped.is_set():
                return False
            self._tripped.set()
            return True

    @property
    def is_tripped(self) -> bool:
        """Whether the accelerator has been permanently abandoned."""
        return self._tripped.is_set()

    @property
    def is_degraded(self) -> bool:
        """Whether the accelerator is currently being skipped for poor health."""
        return self._degraded.is_set()

    def set_degraded(self, degraded: bool) -> None:
        """Start or stop bypassing the accelerator for poor health.

        Reversible, and orthogonal to :meth:`trip`: clearing it does not undo a
        permanent trip.
        """
        if degraded:
            self._degraded.set()
        else:
            self._degraded.clear()


def _grpc_code(exc: BaseException) -> StatusCode | None:
    """Best-effort extraction of a gRPC status code from an exception.

    Handles both ``grpc.RpcError`` (status via a ``code()`` method) and
    ``google.api_core.exceptions.GoogleAPICallError`` (status stored on the
    ``grpc_status_code`` attribute), returning ``None`` for anything else.
    """
    code = getattr(exc, "code", None)
    if callable(code):
        try:
            return code()
        except Exception:
            return None
    grpc_status = getattr(exc, "grpc_status_code", None)
    if isinstance(grpc_status, StatusCode):
        return grpc_status
    return None


def handle_accelerator_error(
    exc: BaseException,
    *,
    daemon: "AcceleratorDaemon | None",
    breaker: AcceleratorBreaker,
    is_idempotent: bool = True,
) -> None:
    """Classify an exception raised by an accelerator-routed RPC.

    Always raises. Either raises :class:`_AcceleratorFallback` to tell the caller
    to retry on the native path, or raises the translated ``google.api_core``
    exception for the caller to propagate:

    * daemon subprocess dead -> trip the breaker; fall back if idempotent, else
      translate and raise (a mid-flight crash may have already committed)
    * ``UNIMPLEMENTED`` -> trip the breaker, fall back immediately
    * any other gRPC error -> translate and raise
    * a non-gRPC exception -> re-raise unchanged (never masked as a fallback)
    """
    # TODO(accelerator): emit a metric here (e.g. a fallback/error counter keyed
    # by reason: dead-daemon / unimplemented / translated-error) once client-side
    # accelerator metrics are wired up.
    # A dead subprocess can surface as a channel error under any status code, so
    # check liveness first: the "daemon died mid-flight" case always wins and is
    # never recoverable.
    if daemon is not None and not daemon.is_running:
        if breaker.trip():
            _LOGGER.warning(
                "Accelerator daemon is no longer running; permanently falling back "
                "to the native Bigtable client for this table."
            )
            _LOGGER.debug("Accelerator daemon failure details", exc_info=exc)
        if not is_idempotent:
            if isinstance(exc, RpcError):
                raise core_exceptions.from_grpc_error(exc) from exc
            raise exc
        raise _AcceleratorFallback() from exc
    if isinstance(exc, InvalidChunk):
        _LOGGER.warning(
            "Accelerator daemon returned an invalid ReadRows chunk; permanently "
            "falling back to the native Bigtable client for this table.",
            exc_info=exc,
        )
        breaker.trip()
        raise _AcceleratorFallback() from exc
    if not isinstance(exc, RpcError):
        # A bug in our own merge machinery, not a daemon result. Do not mask it
        # as a fallback; let it propagate unchanged.
        raise exc
    if _grpc_code(exc) == StatusCode.UNIMPLEMENTED:
        # The daemon only replies UNIMPLEMENTED once it has no working sessions,
        # a persistent condition, so trip the breaker and fall back immediately
        # rather than re-dialing on every subsequent call.
        if breaker.trip():
            _LOGGER.warning(
                "Accelerator daemon replied UNIMPLEMENTED; permanently falling back "
                "to the native Bigtable client for this table."
            )
        raise _AcceleratorFallback() from exc
    raise core_exceptions.from_grpc_error(exc) from exc
