# Copyright 2017 Google Inc.
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

"""Shared utilities used by both downloads and uploads.

This utilities are explicitly catered to ``requests``-like transports.
"""

import time
from contextvars import ContextVar

from google.cloud.storage import _helpers as _storage_helpers
from google.cloud.storage import _opentelemetry_metrics
from google.cloud.storage.exceptions import InvalidResponse

_SINGLE_GET_CHUNK_SIZE = 8192
# The number of seconds to wait to establish a connection
# (connect() call on socket). Avoid setting this to a multiple of 3 to not
# Align with TCP Retransmission timing. (typically 2.5-3s)
_DEFAULT_CONNECT_TIMEOUT = 61
# The number of seconds to wait between bytes sent from the server.
_DEFAULT_READ_TIMEOUT = 60


class _MediaAttemptState(object):
    """Tracks timing and HTTP metadata for a single physical media attempt."""

    def __init__(self, recorder, method, fallback_url, streaming=False):
        self.recorder = recorder
        self.method = method
        self.url = fallback_url
        self.streaming = streaming
        self.attempt_start = time.perf_counter()
        self.header_duration = None
        self.response = None
        self.ttfb_recorded = False


_MEDIA_ATTEMPT_STATE = ContextVar("_gcs_media_attempt_state", default=None)


def resolve_transport_recorder(transport):
    """Resolves the active ``_MetricsRecorder`` for a media ``transport``."""
    if _storage_helpers._SUPPRESS_INTERNAL_METRICS.get():
        return None
    recorder = _storage_helpers._ACTIVE_METRICS_RECORDER.get()
    if recorder is not None and getattr(recorder, "standard_enabled", False) is True:
        return recorder
    recorder = getattr(transport, "_gcs_metrics_recorder", None)
    if recorder is not None and getattr(recorder, "standard_enabled", False) is True:
        return recorder
    return None


def record_streaming_ttfb():
    """Records TTFB upon receipt of the first streamed payload chunk."""
    state = _MEDIA_ATTEMPT_STATE.get()
    if (
        state is not None
        and not state.ttfb_recorded
        and _extract_status_code(state.response) is not None
    ):
        state.ttfb_recorded = True
        state.recorder.record_ttfb(
            time.perf_counter() - state.attempt_start,
            network_path="cloudpath",
        )


def transport_request(transport, method, url, **kwargs):
    """Executes ``transport.request`` while capturing per-attempt timing metadata."""
    state = _MEDIA_ATTEMPT_STATE.get()
    if state is None:
        return transport.request(method, url, **kwargs)

    state.method = method
    state.url = url
    state.attempt_start = time.perf_counter()
    response = transport.request(method, url, **kwargs)
    state.header_duration = time.perf_counter() - state.attempt_start
    state.response = response
    if (
        not state.streaming
        and not state.ttfb_recorded
        and _extract_status_code(response) is not None
    ):
        state.ttfb_recorded = True
        state.recorder.record_ttfb(state.header_duration, network_path="cloudpath")
    return response


def _extract_status_code(response):
    """Returns an integer HTTP status code from ``response`` if valid."""
    raw_sc = getattr(response, "status_code", None)
    if isinstance(raw_sc, int) and not isinstance(raw_sc, bool):
        return raw_sc
    return None


class RequestsMixin(object):
    """Mix-in class implementing ``requests``-specific behavior.

    These are methods that are more general purpose, with implementations
    specific to the types defined in ``requests``.
    """

    @staticmethod
    def _get_status_code(response):
        """Access the status code from an HTTP response.

        Args:
            response (~requests.Response): The HTTP response object.

        Returns:
            int: The status code.
        """
        return response.status_code

    @staticmethod
    def _get_headers(response):
        """Access the headers from an HTTP response.

        Args:
            response (~requests.Response): The HTTP response object.

        Returns:
            ~requests.structures.CaseInsensitiveDict: The header mapping (keys
            are case-insensitive).
        """
        return response.headers

    @staticmethod
    def _get_body(response):
        """Access the response body from an HTTP response.

        Args:
            response (~requests.Response): The HTTP response object.

        Returns:
            bytes: The body of the ``response``.
        """
        if getattr(response, "_content", None) is False:
            chunks = []
            for chunk in response.iter_content(
                chunk_size=_SINGLE_GET_CHUNK_SIZE, decode_unicode=False
            ):
                record_streaming_ttfb()
                chunks.append(chunk)
            record_streaming_ttfb()
            response._content = b"".join(chunks)
            response._content_consumed = True
        else:
            record_streaming_ttfb()
        return response.content


class RawRequestsMixin(RequestsMixin):
    @staticmethod
    def _get_body(response):
        """Access the response body from an HTTP response.

        Args:
            response (~requests.Response): The HTTP response object.

        Returns:
            bytes: The body of the ``response``.
        """
        if response._content is False:
            chunks = []
            for chunk in response.raw.stream(
                _SINGLE_GET_CHUNK_SIZE, decode_content=False
            ):
                record_streaming_ttfb()
                chunks.append(chunk)
            record_streaming_ttfb()
            response._content = b"".join(chunks)
            response._content_consumed = True
        else:
            record_streaming_ttfb()
        return response._content


def wait_and_retry(
    func,
    retry_strategy,
    transport=None,
    method=None,
    url=None,
    streaming=False,
):
    """Attempts to retry a call to ``func`` until success.

    Args:
        func (Callable): A callable that takes no arguments and produces
            an HTTP response which will be checked as retry-able.
        retry_strategy (Optional[google.api_core.retry.Retry]): The
            strategy to use if the request fails and must be retried.
        transport (Optional[object]): Transport object making the request.
        method (Optional[str]): HTTP request method.
        url (Optional[str]): Request URL or fallback URL for route normalization.
        streaming (bool): Whether TTFB should be deferred to streamed body read.

    Returns:
        object: The return value of ``func``.
    """
    recorder = resolve_transport_recorder(transport)
    if recorder is not None:
        base_func = func

        def _timed_attempt():
            state = _MediaAttemptState(
                recorder=recorder,
                method=method,
                fallback_url=url,
                streaming=streaming,
            )
            token = _MEDIA_ATTEMPT_STATE.set(state)
            try:
                result = base_func()
            except BaseException as exc:
                duration = time.perf_counter() - state.attempt_start
                resp = state.response
                if resp is None:
                    resp = getattr(exc, "response", None)
                status_code = _extract_status_code(resp)
                if (
                    status_code is not None
                    and state.response is not None
                    and not state.ttfb_recorded
                    and isinstance(exc, InvalidResponse)
                    and state.header_duration is not None
                ):
                    state.ttfb_recorded = True
                    recorder.record_ttfb(
                        state.header_duration, network_path="cloudpath"
                    )
                recorder.record_http_attempt(
                    duration=duration,
                    http_method=state.method or "UNKNOWN",
                    url_template=_opentelemetry_metrics.normalize_url_template(
                        state.url
                    ),
                    status_code=status_code,
                    error_type=_opentelemetry_metrics.classify_error_type(
                        exc, status_code=status_code
                    ),
                    network_path="cloudpath",
                )
                raise
            finally:
                _MEDIA_ATTEMPT_STATE.reset(token)

            duration = time.perf_counter() - state.attempt_start
            resp = state.response if state.response is not None else result
            status_code = _extract_status_code(resp)
            if not state.ttfb_recorded and status_code is not None:
                ttfb_dur = (
                    state.header_duration
                    if state.header_duration is not None
                    else duration
                )
                state.ttfb_recorded = True
                recorder.record_ttfb(ttfb_dur, network_path="cloudpath")
            recorder.record_http_attempt(
                duration=duration,
                http_method=state.method or "UNKNOWN",
                url_template=_opentelemetry_metrics.normalize_url_template(state.url),
                status_code=status_code,
                error_type="OK",
                network_path="cloudpath",
            )
            return result

        func = _timed_attempt

    try:
        if retry_strategy:
            func = retry_strategy(func)
        return func()
    finally:
        if recorder is not None:
            current_op = _opentelemetry_metrics.get_current_operation()
            if current_op is not None:
                current_op.last_failure_error_type = None
