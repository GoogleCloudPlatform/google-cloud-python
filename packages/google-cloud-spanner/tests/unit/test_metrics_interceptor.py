# Copyright 2025 Google LLC
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

from unittest.mock import MagicMock, Mock

import pytest

from google.cloud.spanner_v1.metrics.constants import _safe_decode_utf8
from google.cloud.spanner_v1.metrics.metrics_interceptor import (
    AsyncMetricsInterceptor,
    MetricsInterceptor,
    _AsyncStreamingResponseWrapper,
    _AsyncUnaryResponseWrapper,
    _StreamingResponseWrapper,
)
from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
    SpannerMetricsTracerFactory,
)


@pytest.fixture
def interceptor():
    SpannerMetricsTracerFactory(enabled=True)
    return MetricsInterceptor()


@pytest.fixture
def mock_tracer_ctx():
    tracer = MockMetricTracer()
    token = SpannerMetricsTracerFactory._current_metrics_tracer_ctx.set(tracer)
    yield tracer
    SpannerMetricsTracerFactory._current_metrics_tracer_ctx.reset(token)


class MockMetricTracer:
    def __init__(self):
        self.project = None
        self.instance = None
        self.database = None
        self.record_attempt_start = MagicMock()
        self.record_attempt_completion = MagicMock()
        self.set_method = MagicMock()
        self.record_front_end_metrics = MagicMock()
        self.set_project = MagicMock()
        self.set_instance = MagicMock()
        self.set_database = MagicMock()
        self.client_attributes = {}


def test_parse_resource_path_valid(interceptor):
    path = "projects/my_project/instances/my_instance/databases/my_database"
    expected = {
        "project": "my_project",
        "instance": "my_instance",
        "database": "my_database",
    }
    assert interceptor._parse_resource_path(path) == expected


def test_parse_resource_path_invalid(interceptor):
    path = "invalid/path"
    expected = {}
    assert interceptor._parse_resource_path(path) == expected


def test_extract_resource_from_path(interceptor):
    metadata = [
        (
            "google-cloud-resource-prefix",
            "projects/my_project/instances/my_instance/databases/my_database",
        )
    ]
    expected = {
        "project": "my_project",
        "instance": "my_instance",
        "database": "my_database",
    }
    assert interceptor._extract_resource_from_path(metadata) == expected


def test_set_metrics_tracer_attributes(interceptor, mock_tracer_ctx):
    # mock_tracer_ctx fixture sets the ContextVar
    resources = {
        "project": "my_project",
        "instance": "my_instance",
        "database": "my_database",
    }

    interceptor._set_metrics_tracer_attributes(resources)
    mock_tracer_ctx.set_project.assert_called_with("my_project")
    mock_tracer_ctx.set_instance.assert_called_with("my_instance")
    mock_tracer_ctx.set_database.assert_called_with("my_database")


def test_intercept_with_tracer(interceptor, mock_tracer_ctx):
    # mock_tracer_ctx fixture sets the ContextVar
    invoked_response = Mock()
    invoked_response.initial_metadata.return_value = []

    mock_invoked_method = MagicMock(return_value=invoked_response)
    call_details = MagicMock(
        method="spanner.someMethod",
        metadata=[
            (
                "google-cloud-resource-prefix",
                "projects/my_project/instances/my_instance/databases/my_database",
            )
        ],
    )

    response = interceptor.intercept(mock_invoked_method, "request", call_details)
    assert response == invoked_response
    mock_tracer_ctx.record_attempt_start.assert_called()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()
    mock_tracer_ctx.record_front_end_metrics.assert_called_once()
    mock_invoked_method.assert_called_once_with("request", call_details)


def test_format_method_name():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import _format_method_name

    method_str = "/google.spanner.v1.Spanner/ExecuteStreamingSql"
    expected = "Spanner.ExecuteStreamingSql"
    assert _format_method_name(method_str) == expected

    # Test bytes input
    method_bytes = b"/google.spanner.v1.Spanner/ExecuteStreamingSql"
    assert _format_method_name(method_bytes) == expected

    # Verify cached result
    assert _format_method_name(method_bytes) == expected

    # Unhashable type input
    assert (
        _format_method_name(["/google.spanner.v1.Spanner/ExecuteSql"])
        == "['.google.spanner.v1.Spanner.ExecuteSql']"
    )
    # Non-decodable bytes
    assert "Spanner" in _format_method_name(b"/google.spanner.v1.Spanner/\xff\xfe")


def test_extract_resource_from_path_bytes_and_dict(interceptor):
    path = "projects/p/instances/i/databases/d"
    expected = {"project": "p", "instance": "i", "database": "d"}

    # Bytes key in list of tuples
    metadata_bytes = [(b"google-cloud-resource-prefix", path.encode("utf-8"))]
    assert interceptor._extract_resource_from_path(metadata_bytes) == expected

    # Dict metadata
    metadata_dict = {"google-cloud-resource-prefix": path}
    assert interceptor._extract_resource_from_path(metadata_dict) == expected

    # Dict with bytes key and value
    metadata_dict_bytes = {b"google-cloud-resource-prefix": path.encode("utf-8")}
    assert interceptor._extract_resource_from_path(metadata_dict_bytes) == expected

    # Empty metadata
    assert interceptor._extract_resource_from_path([]) == {}
    assert interceptor._extract_resource_from_path({}) == {}


def test_parse_resource_path_edge_cases(interceptor):
    path = "projects/p1/instances/i1/databases/d1"
    first = interceptor._parse_resource_path(path)
    second = interceptor._parse_resource_path(path)
    assert first == {"project": "p1", "instance": "i1", "database": "d1"}
    assert first == second

    # Mutating returned dict should not corrupt future calls
    first["mutated"] = True
    third = interceptor._parse_resource_path(path)
    assert "mutated" not in third

    assert interceptor._parse_resource_path("") == {}
    assert interceptor._parse_resource_path(None) == {}
    assert interceptor._parse_resource_path(12345) == {}

    # Database named "sessions"
    db_named_sessions = "projects/p1/instances/i1/databases/sessions/sessions/s123"
    assert interceptor._parse_resource_path(db_named_sessions) == {
        "project": "p1",
        "instance": "i1",
        "database": "sessions",
        "session": "s123",
    }

    # Instance named "sessions"
    instance_named_sessions = (
        "projects/p1/instances/sessions/databases/d1/sessions/s123"
    )
    assert interceptor._parse_resource_path(instance_named_sessions) == {
        "project": "p1",
        "instance": "sessions",
        "database": "d1",
        "session": "s123",
    }

    # Session paths
    session_path = "projects/p1/instances/i1/databases/d1/sessions/s1"
    session_result = interceptor._parse_resource_path(session_path)
    assert session_result == {
        "project": "p1",
        "instance": "i1",
        "database": "d1",
        "session": "s1",
    }
    session_path_empty = "projects/p1/instances/i1/databases/d1/sessions/"
    session_empty_result = interceptor._parse_resource_path(session_path_empty)
    assert session_empty_result == {
        "project": "p1",
        "instance": "i1",
        "database": "d1",
    }
    # Session part starting with slash
    session_slash = "projects/p1/instances/i1/databases/d1/sessions//extra"
    assert interceptor._parse_resource_path(session_slash) == {
        "project": "p1",
        "instance": "i1",
        "database": "d1",
    }
    # Invalid paths with sessions must not return session
    assert interceptor._parse_resource_path("invalid/sessions/s123") == {}
    assert interceptor._parse_resource_path("/sessions/s123") == {}


def test_async_streaming_response_wrapper_not_awaitable():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        _AsyncStreamingResponseWrapper,
    )

    mock_stream = MagicMock()
    mock_tracer = MagicMock()
    wrapper = _AsyncStreamingResponseWrapper(mock_stream, mock_tracer)
    assert not hasattr(wrapper, "__await__")


@pytest.mark.asyncio
async def test_async_unary_response_wrapper_stream_unary():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        _AsyncUnaryResponseWrapper,
    )

    class StreamUnaryMock:
        def __init__(self):
            self.written = []
            self.done_writing_called = False

        def write(self, data):
            self.written.append(data)

        def done_writing(self):
            self.done_writing_called = True

        def initial_metadata(self):
            return []

        def __await__(self):
            async def _coro():
                return "done"

            return _coro().__await__()

    mock_stream_unary = StreamUnaryMock()
    mock_tracer = MagicMock()
    wrapper = _AsyncUnaryResponseWrapper(mock_stream_unary, mock_tracer)
    wrapper.write("item1")
    wrapper.done_writing()
    assert mock_stream_unary.written == ["item1"]
    assert mock_stream_unary.done_writing_called is True
    result = await wrapper
    assert result == "done"
    mock_tracer.record_attempt_completion.assert_called_once()


def test_extract_resource_from_path_edge_cases(interceptor):
    # Non-iterable metadata
    assert interceptor._extract_resource_from_path(12345) == {}
    assert interceptor._extract_resource_from_path(None) == {}

    # Dict without resource prefix
    assert interceptor._extract_resource_from_path({"unrelated": "header"}) == {}

    # Non-decodable bytes in dict and list metadata
    assert (
        interceptor._extract_resource_from_path(
            {"google-cloud-resource-prefix": b"\xff\xfe\xfd"}
        )
        == {}
    )
    assert (
        interceptor._extract_resource_from_path(
            [("google-cloud-resource-prefix", b"\xff\xfe\xfd")]
        )
        == {}
    )

    # Malformed tuple entries (not length 2)
    malformed = [("single_element",), ("a", "b", "c")]
    assert interceptor._extract_resource_from_path(malformed) == {}

    # Generator metadata
    path = "projects/p/instances/i/databases/d"

    def metadata_generator():
        yield ("unrelated", "value")
        yield ("google-cloud-resource-prefix", path)

    assert interceptor._extract_resource_from_path(metadata_generator()) == {
        "project": "p",
        "instance": "i",
        "database": "d",
    }


@pytest.fixture
def async_interceptor():
    SpannerMetricsTracerFactory(enabled=True)
    return AsyncMetricsInterceptor()


@pytest.mark.asyncio
async def test_async_intercept_unary_unary(async_interceptor, mock_tracer_ctx):
    class MockUnaryCall:
        def initial_metadata(self):
            return [("server-timing", "gfet4t7; dur=55")]

        def __await__(self):
            async def _coroutine():
                return "unary_result"

            return _coroutine().__await__()

    async def mock_continuation(call_details, request):
        return MockUnaryCall()

    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/ExecuteSql",
        metadata=[
            (
                "google-cloud-resource-prefix",
                "projects/my_project/instances/my_instance/databases/my_database",
            )
        ],
    )

    wrapped_call = await async_interceptor.intercept_unary_unary(
        mock_continuation, call_details, "request_payload"
    )
    assert isinstance(wrapped_call, _AsyncUnaryResponseWrapper)
    result = await wrapped_call
    assert result == "unary_result"
    mock_tracer_ctx.record_attempt_start.assert_called_once()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()
    mock_tracer_ctx.record_front_end_metrics.assert_called_once()
    mock_tracer_ctx.set_method.assert_called_with("Spanner.ExecuteSql")
    mock_tracer_ctx.set_project.assert_called_with("my_project")
    mock_tracer_ctx.set_instance.assert_called_with("my_instance")
    mock_tracer_ctx.set_database.assert_called_with("my_database")


@pytest.mark.asyncio
async def test_async_intercept_stream_unary(async_interceptor, mock_tracer_ctx):
    class MockStreamUnaryCall:
        def initial_metadata(self):
            return []

        def __await__(self):
            async def _coroutine():
                return "stream_unary_result"

            return _coroutine().__await__()

    async def mock_continuation(call_details, request_iterator):
        return MockStreamUnaryCall()

    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/Commit",
        metadata=[],
    )

    wrapped_call = await async_interceptor.intercept_stream_unary(
        mock_continuation, call_details, ["req1"]
    )
    assert isinstance(wrapped_call, _AsyncUnaryResponseWrapper)
    result = await wrapped_call
    assert result == "stream_unary_result"
    mock_tracer_ctx.record_attempt_start.assert_called_once()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


def test_streaming_response_wrapper_lifecycle():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        _StreamingResponseWrapper,
    )

    # 1. Normal iteration
    mock_response = MagicMock()
    mock_response.__iter__.return_value = iter(["chunk1", "chunk2"])
    mock_response.initial_metadata.return_value = [("server-timing", "gfet4t7; dur=10")]
    mock_tracer = MagicMock()

    wrapper = _StreamingResponseWrapper(mock_response, mock_tracer)
    items = list(wrapper)
    assert items == ["chunk1", "chunk2"]
    mock_tracer.record_attempt_completion.assert_called_once()
    mock_tracer.record_front_end_metrics.assert_called_once_with(
        [("server-timing", "gfet4t7; dur=10")]
    )

    # 2. Exception during iteration
    mock_response_err = MagicMock()
    mock_response_err.__iter__.return_value = iter(["ok"])

    class FaultyIterator:
        def __iter__(self):
            return self

        def __next__(self):
            raise RuntimeError("Stream broken")

    mock_tracer_err = MagicMock()
    wrapper_err = _StreamingResponseWrapper(FaultyIterator(), mock_tracer_err)
    with pytest.raises(RuntimeError, match="Stream broken"):
        next(wrapper_err)
    mock_tracer_err.record_attempt_completion.assert_called_once()

    # 3. Explicit cancellation
    mock_response_cancel = MagicMock()
    mock_tracer_cancel = MagicMock()
    wrapper_cancel = _StreamingResponseWrapper(mock_response_cancel, mock_tracer_cancel)
    wrapper_cancel.cancel()
    mock_tracer_cancel.record_attempt_completion.assert_called_once_with(
        status="CANCELLED"
    )
    mock_response_cancel.cancel.assert_called_once()

    # 4. Finalizer (__del__) when not completed
    mock_response_del = MagicMock()
    mock_tracer_del = MagicMock()
    wrapper_del = _StreamingResponseWrapper(mock_response_del, mock_tracer_del)
    wrapper_del.__del__()
    mock_tracer_del.record_attempt_completion.assert_called_once_with(
        status="CANCELLED"
    )

    # 5. __getattr__ delegation and error handling
    mock_response_attr = MagicMock()
    mock_response_attr.custom_field = "custom_value"
    mock_response_attr.initial_metadata.side_effect = RuntimeError("Metadata failed")
    mock_tracer_attr = MagicMock()
    mock_tracer_attr.record_attempt_completion.side_effect = RuntimeError(
        "Tracer failed"
    )
    wrapper_attr = _StreamingResponseWrapper(mock_response_attr, mock_tracer_attr)
    assert wrapper_attr.custom_field == "custom_value"
    # _record_metrics should swallow exceptions gracefully
    wrapper_attr._record_metrics()
    # Calling it a second time hits early return
    wrapper_attr._record_metrics()

    # Cancel and del error handling
    mock_tracer_cancel_err = MagicMock()
    mock_tracer_cancel_err.record_attempt_completion.side_effect = RuntimeError(
        "Cancel error"
    )
    wrapper_cancel_err = _StreamingResponseWrapper(MagicMock(), mock_tracer_cancel_err)
    wrapper_cancel_err.cancel()

    mock_tracer_del_err = MagicMock()
    mock_tracer_del_err.record_attempt_completion.side_effect = RuntimeError(
        "Del error"
    )
    wrapper_del_err = _StreamingResponseWrapper(MagicMock(), mock_tracer_del_err)
    wrapper_del_err.__del__()


@pytest.mark.asyncio
async def test_async_unary_response_wrapper_lifecycle():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        _AsyncUnaryResponseWrapper,
    )

    # 1. Exception during await
    class FaultyAwaitable:
        def __await__(self):
            async def _coro():
                raise ValueError("RPC failed")

            return _coro().__await__()

    mock_tracer_err = MagicMock()
    wrapper_err = _AsyncUnaryResponseWrapper(FaultyAwaitable(), mock_tracer_err)
    with pytest.raises(ValueError, match="RPC failed"):
        await wrapper_err
    mock_tracer_err.record_attempt_completion.assert_called_once()

    # 2. Explicit cancellation
    mock_response_cancel = MagicMock()
    mock_tracer_cancel = MagicMock()
    wrapper_cancel = _AsyncUnaryResponseWrapper(
        mock_response_cancel, mock_tracer_cancel
    )
    wrapper_cancel.cancel()
    mock_tracer_cancel.record_attempt_completion.assert_called_once_with(
        status="CANCELLED"
    )
    mock_response_cancel.cancel.assert_called_once()

    # 3. Finalizer (__del__) when unawaited
    mock_response_del = MagicMock()
    mock_tracer_del = MagicMock()
    wrapper_del = _AsyncUnaryResponseWrapper(mock_response_del, mock_tracer_del)
    wrapper_del.__del__()
    mock_tracer_del.record_attempt_completion.assert_called_once_with(
        status="CANCELLED"
    )

    # 4. Proxy methods
    mock_delegate = MagicMock()
    mock_tracer = MagicMock()
    wrapper = _AsyncUnaryResponseWrapper(mock_delegate, mock_tracer)

    wrapper.add_done_callback(MagicMock())
    mock_delegate.add_done_callback.assert_called_once()
    wrapper.cancelled()
    mock_delegate.cancelled.assert_called_once()
    wrapper.code()
    mock_delegate.code.assert_called_once()
    wrapper.details()
    mock_delegate.details.assert_called_once()
    wrapper.done()
    mock_delegate.done.assert_called_once()
    wrapper.initial_metadata()
    mock_delegate.initial_metadata.assert_called_once()
    wrapper.time_remaining()
    mock_delegate.time_remaining.assert_called_once()
    wrapper.trailing_metadata()
    mock_delegate.trailing_metadata.assert_called_once()
    wrapper.wait_for_connection()
    mock_delegate.wait_for_connection.assert_called_once()
    assert wrapper.some_custom_attr == mock_delegate.some_custom_attr

    # 5. Async initial metadata and error handling
    class AsyncMetadataCall:
        async def initial_metadata(self):
            return [("server-timing", "gfet4t7; dur=40")]

        def __await__(self):
            async def _coro():
                return "ok"

            return _coro().__await__()

    mock_tracer_meta = MagicMock()
    wrapper_meta = _AsyncUnaryResponseWrapper(AsyncMetadataCall(), mock_tracer_meta)
    result = await wrapper_meta
    assert result == "ok"
    mock_tracer_meta.record_front_end_metrics.assert_called_once_with(
        [("server-timing", "gfet4t7; dur=40")]
    )
    # Calling it a second time hits early return
    await wrapper_meta._record_metrics()

    # Cancel and del error handling
    mock_tracer_cancel_err = MagicMock()
    mock_tracer_cancel_err.record_attempt_completion.side_effect = RuntimeError(
        "Cancel error"
    )
    wrapper_cancel_err = _AsyncUnaryResponseWrapper(MagicMock(), mock_tracer_cancel_err)
    wrapper_cancel_err.cancel()

    mock_tracer_del_err = MagicMock()
    mock_tracer_del_err.record_attempt_completion.side_effect = RuntimeError(
        "Del error"
    )
    wrapper_del_err = _AsyncUnaryResponseWrapper(MagicMock(), mock_tracer_del_err)
    wrapper_del_err.__del__()

    # Metadata error in _record_metrics
    class UnaryMetadataErrorCall:
        def initial_metadata(self):
            raise RuntimeError("Metadata failed")

        def __await__(self):
            async def _coro():
                return "ok"

            return _coro().__await__()

    mock_tracer_err2 = MagicMock()
    mock_tracer_err2.record_attempt_completion.side_effect = RuntimeError(
        "Tracer failed"
    )
    wrapper_meta_err = _AsyncUnaryResponseWrapper(
        UnaryMetadataErrorCall(), mock_tracer_err2
    )
    await wrapper_meta_err


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_lifecycle():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        _AsyncStreamingResponseWrapper,
    )

    # 1. Exception during async iteration
    class FaultyAsyncIterator:
        def __aiter__(self):
            return self

        async def __anext__(self):
            raise RuntimeError("Stream error")

    mock_tracer_err = MagicMock()
    wrapper_err = _AsyncStreamingResponseWrapper(FaultyAsyncIterator(), mock_tracer_err)
    with pytest.raises(RuntimeError, match="Stream error"):
        async for _ in wrapper_err:
            pass
    mock_tracer_err.record_attempt_completion.assert_called_once()

    # 2. Cancellation
    mock_response_cancel = MagicMock()
    mock_tracer_cancel = MagicMock()
    wrapper_cancel = _AsyncStreamingResponseWrapper(
        mock_response_cancel, mock_tracer_cancel
    )
    wrapper_cancel.cancel()
    mock_tracer_cancel.record_attempt_completion.assert_called_once_with(
        status="CANCELLED"
    )
    mock_response_cancel.cancel.assert_called_once()

    # 3. Finalizer (__del__) when not completed
    mock_response_del = MagicMock()
    mock_tracer_del = MagicMock()
    wrapper_del = _AsyncStreamingResponseWrapper(mock_response_del, mock_tracer_del)
    wrapper_del.__del__()
    mock_tracer_del.record_attempt_completion.assert_called_once_with(
        status="CANCELLED"
    )

    # 4. Proxy methods
    mock_delegate = MagicMock()
    mock_tracer = MagicMock()
    wrapper = _AsyncStreamingResponseWrapper(mock_delegate, mock_tracer)

    wrapper.add_done_callback(MagicMock())
    mock_delegate.add_done_callback.assert_called_once()
    wrapper.cancelled()
    mock_delegate.cancelled.assert_called_once()
    wrapper.code()
    mock_delegate.code.assert_called_once()
    wrapper.details()
    mock_delegate.details.assert_called_once()
    wrapper.done()
    mock_delegate.done.assert_called_once()
    wrapper.initial_metadata()
    mock_delegate.initial_metadata.assert_called_once()
    wrapper.time_remaining()
    mock_delegate.time_remaining.assert_called_once()
    wrapper.trailing_metadata()
    mock_delegate.trailing_metadata.assert_called_once()
    wrapper.wait_for_connection()
    mock_delegate.wait_for_connection.assert_called_once()
    wrapper.read()
    mock_delegate.read.assert_called_once()
    wrapper.write("data")
    mock_delegate.write.assert_called_once_with("data")
    wrapper.done_writing()
    mock_delegate.done_writing.assert_called_once()
    assert wrapper.custom_attr == mock_delegate.custom_attr

    # 5. Async initial metadata in stream
    class StreamAsyncMetadata:
        def __init__(self):
            self.yielded = False

        def __aiter__(self):
            return self

        async def __anext__(self):
            if not self.yielded:
                self.yielded = True
                return "item"
            raise StopAsyncIteration

        async def initial_metadata(self):
            return [("server-timing", "afe; dur=15")]

    mock_tracer_stream_meta = MagicMock()
    wrapper_stream_meta = _AsyncStreamingResponseWrapper(
        StreamAsyncMetadata(), mock_tracer_stream_meta
    )
    items = []
    async for item in wrapper_stream_meta:
        items.append(item)
    assert items == ["item"]
    mock_tracer_stream_meta.record_front_end_metrics.assert_called_once_with(
        [("server-timing", "afe; dur=15")]
    )
    # Calling it a second time hits early return
    await wrapper_stream_meta._record_metrics()

    # Cancel and del error handling
    mock_tracer_cancel_err = MagicMock()
    mock_tracer_cancel_err.record_attempt_completion.side_effect = RuntimeError(
        "Cancel error"
    )
    wrapper_cancel_err = _AsyncStreamingResponseWrapper(
        MagicMock(), mock_tracer_cancel_err
    )
    wrapper_cancel_err.cancel()

    mock_tracer_del_err = MagicMock()
    mock_tracer_del_err.record_attempt_completion.side_effect = RuntimeError(
        "Del error"
    )
    wrapper_del_err = _AsyncStreamingResponseWrapper(MagicMock(), mock_tracer_del_err)
    wrapper_del_err.__del__()

    # Metadata error in stream
    class StreamMetadataError:
        def __init__(self):
            self.yielded = False

        def __aiter__(self):
            return self

        async def __anext__(self):
            if not self.yielded:
                self.yielded = True
                return "chunk"
            raise StopAsyncIteration

        def initial_metadata(self):
            raise RuntimeError("Stream metadata failed")

    mock_tracer_stream_err = MagicMock()
    mock_tracer_stream_err.record_attempt_completion.side_effect = RuntimeError(
        "Tracer stream error"
    )
    wrapper_stream_err = _AsyncStreamingResponseWrapper(
        StreamMetadataError(), mock_tracer_stream_err
    )
    async for _ in wrapper_stream_err:
        pass


def test_metrics_interceptor_sync_methods_and_disabled(mock_tracer_ctx):
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        MetricsInterceptor,
        _StreamingResponseWrapper,
        _wrap_response,
    )

    interceptor = MetricsInterceptor()

    # 0. _set_metrics_tracer_attributes when tracer is None
    token = SpannerMetricsTracerFactory._current_metrics_tracer_ctx.set(None)
    try:
        interceptor._set_metrics_tracer_attributes({"project": "p"})
    finally:
        SpannerMetricsTracerFactory._current_metrics_tracer_ctx.reset(token)

    # 1. Intercept when disabled
    SpannerMetricsTracerFactory(enabled=False)
    mock_continuation = MagicMock(return_value="raw_response")
    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/ExecuteSql", metadata=[]
    )
    result = interceptor.intercept(mock_continuation, "request", call_details)
    assert result == "raw_response"
    mock_continuation.assert_called_once_with("request", call_details)
    SpannerMetricsTracerFactory(enabled=True)

    # 2. _wrap_response with streaming response
    class StreamingCallMock:
        def __next__(self):
            raise StopIteration

    mock_stream_call = StreamingCallMock()
    wrapped_stream = _wrap_response(mock_stream_call, mock_tracer_ctx)
    assert isinstance(wrapped_stream, _StreamingResponseWrapper)

    # 3. _wrap_response with unary response handling errors gracefully
    class SimpleUnaryResponse:
        def initial_metadata(self):
            raise RuntimeError("Metadata error")

    unary_response = SimpleUnaryResponse()
    mock_faulty_tracer = MagicMock()
    mock_faulty_tracer.record_attempt_completion.side_effect = RuntimeError(
        "Tracer error"
    )
    result_unary = _wrap_response(unary_response, mock_faulty_tracer)
    assert result_unary is unary_response

    # 4. _StreamingResponseWrapper with initial_metadata error
    mock_resp_meta_err = MagicMock()
    mock_resp_meta_err.__iter__.return_value = iter(["chunk"])
    mock_resp_meta_err.initial_metadata.side_effect = RuntimeError("Metadata failed")
    wrapper_stream_meta_err = _StreamingResponseWrapper(mock_resp_meta_err, MagicMock())
    assert list(wrapper_stream_meta_err) == ["chunk"]


@pytest.mark.asyncio
async def test_async_wrapper_additional_error_branches():
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        _AsyncStreamingResponseWrapper,
        _AsyncUnaryResponseWrapper,
    )

    # Unary wrapper with initial_metadata error
    class UnaryInitialMetaErr:
        def initial_metadata(self):
            raise RuntimeError("Initial meta err")

        def __await__(self):
            async def _coro():
                return "ok"

            return _coro().__await__()

    wrapper_unary_meta_err = _AsyncUnaryResponseWrapper(
        UnaryInitialMetaErr(), MagicMock()
    )
    assert await wrapper_unary_meta_err == "ok"

    # Streaming wrapper without __aiter__ on response directly calling __anext__
    class DirectAsyncIterator:
        def __init__(self):
            self.done = False

        async def __anext__(self):
            if not self.done:
                self.done = True
                return "first"
            raise StopAsyncIteration

        def initial_metadata(self):
            raise RuntimeError("Stream meta err")

    wrapper_direct = _AsyncStreamingResponseWrapper(DirectAsyncIterator(), MagicMock())
    item = await wrapper_direct.__anext__()
    assert item == "first"
    with pytest.raises(StopAsyncIteration):
        await wrapper_direct.__anext__()


@pytest.mark.asyncio
async def test_async_metrics_interceptor_all_methods_and_disabled(mock_tracer_ctx):
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        AsyncMetricsInterceptor,
    )

    interceptor = AsyncMetricsInterceptor()

    # 1. Intercept when disabled
    SpannerMetricsTracerFactory(enabled=False)

    async def mock_continuation(details, request):
        return "async_raw"

    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/ExecuteSql", metadata=[]
    )
    result = await interceptor.intercept_unary_unary(
        mock_continuation, call_details, "req"
    )
    assert result == "async_raw"
    SpannerMetricsTracerFactory(enabled=True)

    # 2. intercept_stream_unary
    async def mock_stream_unary_continuation(details, request_iterator):
        class AwaitableResult:
            def __await__(self):
                async def _coro():
                    return "stream_unary_done"

                return _coro().__await__()

        return AwaitableResult()

    wrapped_stream_unary = await interceptor.intercept_stream_unary(
        mock_stream_unary_continuation, call_details, ["req1"]
    )
    assert await wrapped_stream_unary == "stream_unary_done"

    # 3. intercept_stream_stream
    async def mock_stream_stream_continuation(details, request_iterator):
        class AsyncStreamResult:
            def __aiter__(self):
                return self

            async def __anext__(self):
                raise StopAsyncIteration

        return AsyncStreamResult()

    wrapped_stream_stream = await interceptor.intercept_stream_stream(
        mock_stream_stream_continuation, call_details, ["req1"]
    )
    items = []
    async for item in wrapped_stream_stream:
        items.append(item)
    assert items == []


@pytest.mark.asyncio
async def test_interceptor_wrapper_and_branch_edge_cases(mock_tracer_ctx):
    from google.cloud.spanner_v1.metrics.metrics_interceptor import (
        AsyncMetricsInterceptor,
        MetricsInterceptor,
        _AsyncStreamingResponseWrapper,
        _AsyncUnaryResponseWrapper,
        _StreamingResponseWrapper,
        _wrap_response,
    )

    interceptor = MetricsInterceptor()
    async_interceptor = AsyncMetricsInterceptor()

    # 1. _set_metrics_tracer_attributes with partial and empty dicts
    interceptor._set_metrics_tracer_attributes({"project": "p"})
    interceptor._set_metrics_tracer_attributes({"instance": "i"})
    interceptor._set_metrics_tracer_attributes({})

    # 2. Interceptor call when tracer already has all resource attributes set
    mock_tracer_ctx.client_attributes["project_id"] = "proj"
    mock_tracer_ctx.client_attributes["instance_id"] = "inst"
    mock_tracer_ctx.client_attributes["database"] = "db"

    mock_continuation = MagicMock(return_value="response")
    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/ExecuteSql", metadata=[]
    )
    result = interceptor.intercept(mock_continuation, "req", call_details)
    assert result == "response"

    async def mock_async_continuation(details, request):
        class AsyncCall:
            def __await__(self):
                async def _coro():
                    return "async_response"

                return _coro().__await__()

        return AsyncCall()

    async_wrapped = await async_interceptor.intercept_unary_unary(
        mock_async_continuation, call_details, "req"
    )
    assert await async_wrapped == "async_response"

    # 3. _wrap_response unary branch when initial_metadata raises or is missing
    class UnaryWithFailingMetadata:
        def initial_metadata(self):
            raise RuntimeError("Metadata failed")

    mock_tracer = MagicMock()
    _wrap_response(UnaryWithFailingMetadata(), mock_tracer)
    mock_tracer.record_attempt_completion.assert_called_once()
    mock_tracer.record_front_end_metrics.assert_called_once_with([])

    _wrap_response("no_initial_metadata", mock_tracer)

    # 4. _StreamingResponseWrapper: double cancel, missing cancel, del after recorded
    # 4. _StreamingResponseWrapper:
    # 4a. cancel returns False
    stream_delegate_refused = MagicMock()
    stream_delegate_refused.cancel.return_value = False
    mock_tracer_unrecorded = MagicMock()
    stream_wrapper_refused = _StreamingResponseWrapper(
        stream_delegate_refused, mock_tracer_unrecorded
    )
    assert stream_wrapper_refused.cancel() is False
    assert stream_wrapper_refused._metrics_recorded is False
    mock_tracer_unrecorded.record_attempt_completion.assert_not_called()

    # 4b. cancel with metadata error and successful metadata
    stream_delegate_meta_err = MagicMock()
    stream_delegate_meta_err.initial_metadata.side_effect = RuntimeError("meta failed")
    stream_wrapper_meta_err = _StreamingResponseWrapper(
        stream_delegate_meta_err, mock_tracer
    )
    stream_wrapper_meta_err.cancel()

    stream_delegate_with_meta = MagicMock()
    stream_delegate_with_meta.initial_metadata.return_value = [
        ("server-timing", "gfet4t7; dur=50")
    ]
    stream_wrapper_with_meta = _StreamingResponseWrapper(
        stream_delegate_with_meta, mock_tracer
    )
    stream_wrapper_with_meta.cancel()
    mock_tracer.record_front_end_metrics.assert_called_with(
        [("server-timing", "gfet4t7; dur=50")]
    )

    stream_delegate = MagicMock(spec=["__next__"])
    stream_wrapper = _StreamingResponseWrapper(stream_delegate, mock_tracer)
    stream_wrapper.cancel()
    stream_wrapper.cancel()
    stream_wrapper.__del__()

    # 5. _AsyncUnaryResponseWrapper:
    # 5a. cancel returns False
    async_unary_refused = MagicMock()
    async_unary_refused.cancel.return_value = False
    async_unary_wrapper_refused = _AsyncUnaryResponseWrapper(
        async_unary_refused, mock_tracer_unrecorded
    )
    assert async_unary_wrapper_refused.cancel() is False
    assert async_unary_wrapper_refused._metrics_recorded is False

    # 5b. cancel with awaitable metadata, failing metadata, and normal metadata
    async_unary_async_meta = MagicMock()

    async def async_meta():
        return [("server-timing", "afe; dur=25")]

    async_unary_async_meta.initial_metadata.return_value = async_meta()
    async_unary_wrapper_meta = _AsyncUnaryResponseWrapper(
        async_unary_async_meta, mock_tracer
    )
    async_unary_wrapper_meta.cancel()

    async_unary_err_meta = MagicMock()
    async_unary_err_meta.initial_metadata.side_effect = RuntimeError("async meta error")
    async_unary_wrapper_err = _AsyncUnaryResponseWrapper(
        async_unary_err_meta, mock_tracer
    )
    async_unary_wrapper_err.cancel()

    async_unary_normal_meta = MagicMock()
    async_unary_normal_meta.initial_metadata.return_value = [
        ("server-timing", "afe; dur=25")
    ]
    async_unary_wrapper_normal = _AsyncUnaryResponseWrapper(
        async_unary_normal_meta, mock_tracer
    )
    async_unary_wrapper_normal.cancel()
    mock_tracer.record_front_end_metrics.assert_called_with(
        [("server-timing", "afe; dur=25")]
    )

    async_unary_delegate = MagicMock(spec=["cancel"])
    async_unary_wrapper = _AsyncUnaryResponseWrapper(async_unary_delegate, mock_tracer)
    async_unary_wrapper.cancel()
    async_unary_wrapper.cancel()

    # 6. _AsyncStreamingResponseWrapper:
    # 6a. cancel returns False
    async_stream_refused = MagicMock()
    async_stream_refused.cancel.return_value = False
    async_stream_wrapper_refused = _AsyncStreamingResponseWrapper(
        async_stream_refused, mock_tracer_unrecorded
    )
    assert async_stream_wrapper_refused.cancel() is False
    assert async_stream_wrapper_refused._metrics_recorded is False

    # 6b. cancel with awaitable metadata, failing metadata, and normal metadata
    async_stream_async_meta = MagicMock()
    async_stream_async_meta.initial_metadata.return_value = async_meta()
    async_stream_wrapper_meta = _AsyncStreamingResponseWrapper(
        async_stream_async_meta, mock_tracer
    )
    async_stream_wrapper_meta.cancel()

    async_stream_err_meta = MagicMock()
    async_stream_err_meta.initial_metadata.side_effect = RuntimeError(
        "async meta error"
    )
    async_stream_wrapper_err = _AsyncStreamingResponseWrapper(
        async_stream_err_meta, mock_tracer
    )
    async_stream_wrapper_err.cancel()

    async_stream_normal_meta = MagicMock()
    async_stream_normal_meta.initial_metadata.return_value = [
        ("server-timing", "gfet4t7; dur=30")
    ]
    async_stream_wrapper_normal = _AsyncStreamingResponseWrapper(
        async_stream_normal_meta, mock_tracer
    )
    async_stream_wrapper_normal.cancel()
    mock_tracer.record_front_end_metrics.assert_called_with(
        [("server-timing", "gfet4t7; dur=30")]
    )

    async_stream_delegate = MagicMock(spec=["cancel"])
    async_stream_wrapper = _AsyncStreamingResponseWrapper(
        async_stream_delegate, mock_tracer
    )
    async_stream_wrapper.cancel()
    async_stream_wrapper.cancel()

    # Async response without __aiter__ (custom async iterator)
    class CustomAsyncIterator:
        async def __anext__(self):
            raise StopAsyncIteration

    custom_async_wrapper = _AsyncStreamingResponseWrapper(
        CustomAsyncIterator(), mock_tracer
    )
    assert custom_async_wrapper.__aiter__() is custom_async_wrapper
    async for _ in custom_async_wrapper:
        pass

    # Async response where __anext__ is called before __aiter__
    class AsyncStreamWithAiter:
        def __aiter__(self):
            async def _gen():
                if False:
                    yield 1

            return _gen()

    anext_first_wrapper = _AsyncStreamingResponseWrapper(
        AsyncStreamWithAiter(), mock_tracer
    )
    with pytest.raises(StopAsyncIteration):
        await anext_first_wrapper.__anext__()


def test_safe_decode_utf8():
    assert _safe_decode_utf8(None) == ""
    assert _safe_decode_utf8("hello") == "hello"
    assert _safe_decode_utf8(b"world") == "world"
    assert _safe_decode_utf8(123) == "123"


def test_prepare_attempt():
    mock_tracer = MagicMock()
    mock_tracer.client_attributes = {}
    call_details = MagicMock()
    call_details.metadata = [
        ("google-cloud-resource-prefix", "projects/p/instances/i/databases/d")
    ]
    call_details.method = "/google.spanner.v1.Spanner/ExecuteSql"

    MetricsInterceptor._prepare_attempt(mock_tracer, call_details)

    mock_tracer.set_project.assert_called_with("p")
    mock_tracer.set_instance.assert_called_with("i")
    mock_tracer.set_database.assert_called_with("d")
    mock_tracer.set_method.assert_called_with("Spanner.ExecuteSql")
    mock_tracer.record_attempt_start.assert_called_once()


@pytest.mark.asyncio
async def test_async_intercept_unary_stream(async_interceptor, mock_tracer_ctx):
    # Simulates grpc.aio.UnaryStreamCall: defines __aiter__ returning an async generator,
    # but does NOT define __anext__ on the call object itself.
    class MockUnaryStreamCall:
        def initial_metadata(self):
            return [("server-timing", "afe; dur=25")]

        def __aiter__(self):
            async def _generator():
                yield "chunk_1"
                yield "chunk_2"

            return _generator()

    call = MockUnaryStreamCall()
    assert hasattr(call, "__aiter__")
    assert not hasattr(call, "__anext__")

    async def mock_continuation(call_details, request):
        return call

    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/ExecuteStreamingSql",
        metadata=[],
    )

    wrapped_stream = await async_interceptor.intercept_unary_stream(
        mock_continuation, call_details, "request_payload"
    )
    assert isinstance(wrapped_stream, _AsyncStreamingResponseWrapper)

    # Before iteration finishes, attempt completion is not yet recorded
    mock_tracer_ctx.record_attempt_start.assert_called_once()
    mock_tracer_ctx.record_attempt_completion.assert_not_called()

    items = []
    async for item in wrapped_stream:
        items.append(item)

    assert items == ["chunk_1", "chunk_2"]
    mock_tracer_ctx.record_attempt_completion.assert_called_once()
    mock_tracer_ctx.record_front_end_metrics.assert_called_once()


@pytest.mark.asyncio
async def test_async_intercept_stream_stream(async_interceptor, mock_tracer_ctx):
    class MockStreamStreamCall:
        def initial_metadata(self):
            return []

        def __aiter__(self):
            async def _generator():
                yield "stream_stream_chunk"

            return _generator()

    async def mock_continuation(call_details, request_iterator):
        return MockStreamStreamCall()

    call_details = MagicMock(
        method="/google.spanner.v1.Spanner/StreamingRead",
        metadata=[],
    )

    wrapped_stream = await async_interceptor.intercept_stream_stream(
        mock_continuation, call_details, ["req1"]
    )
    assert isinstance(wrapped_stream, _AsyncStreamingResponseWrapper)

    items = []
    async for item in wrapped_stream:
        items.append(item)

    assert items == ["stream_stream_chunk"]
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_intercept_disabled(mock_tracer_ctx):
    SpannerMetricsTracerFactory._metrics_tracer_factory = None
    SpannerMetricsTracerFactory(enabled=False)
    try:
        interceptor = AsyncMetricsInterceptor()

        async def mock_continuation(call_details, request):
            return "raw_unwrapped_response"

        call_details = MagicMock(
            method="/google.spanner.v1.Spanner/ExecuteSql",
            metadata=[],
        )

        result = await interceptor.intercept_unary_unary(
            mock_continuation, call_details, "request_payload"
        )
        assert result == "raw_unwrapped_response"
        mock_tracer_ctx.record_attempt_start.assert_not_called()
    finally:
        SpannerMetricsTracerFactory._metrics_tracer_factory = None


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_exception(mock_tracer_ctx):
    class FaultyStreamCall:
        def initial_metadata(self):
            return []

        def __aiter__(self):
            async def _generator():
                yield "first_chunk"
                raise RuntimeError("stream_failed")

            return _generator()

    wrapper = _AsyncStreamingResponseWrapper(FaultyStreamCall(), mock_tracer_ctx)

    with pytest.raises(RuntimeError, match="stream_failed"):
        async for _ in wrapper:
            pass

    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_delegation(mock_tracer_ctx):
    mock_response = MagicMock()
    mock_response.cancel.return_value = True
    mock_response.cancelled.return_value = False
    mock_response.code.return_value = 0
    mock_response.details.return_value = "details"
    mock_response.done.return_value = True
    mock_response.initial_metadata.return_value = []
    mock_response.time_remaining.return_value = 10.0
    mock_response.trailing_metadata.return_value = []
    mock_response.wait_for_connection.return_value = None
    mock_response.read.return_value = "chunk"
    mock_response.write.return_value = None
    mock_response.done_writing.return_value = None

    wrapper = _AsyncStreamingResponseWrapper(mock_response, mock_tracer_ctx)

    assert wrapper.cancel() is True
    mock_response.cancel.assert_called_once()
    assert wrapper.cancelled() is False
    assert wrapper.code() == 0
    assert wrapper.details() == "details"
    assert wrapper.done() is True
    assert wrapper.initial_metadata() == []
    assert wrapper.time_remaining() == 10.0
    assert wrapper.trailing_metadata() == []
    assert wrapper.wait_for_connection() is None
    assert wrapper.read() == "chunk"
    assert wrapper.write("msg") is None
    mock_response.write.assert_called_once_with("msg")
    assert wrapper.done_writing() is None
    mock_response.done_writing.assert_called_once()
    mock_response.custom_attribute = "custom"
    assert wrapper.custom_attribute == "custom"

    callback = MagicMock()
    wrapper.add_done_callback(callback)
    mock_response.add_done_callback.assert_called_once_with(callback)


@pytest.mark.asyncio
async def test_async_unary_response_wrapper_exception(mock_tracer_ctx):
    class FaultyUnaryCall:
        def initial_metadata(self):
            return []

        def __await__(self):
            async def _coroutine():
                raise RuntimeError("unary_failed")

            return _coroutine().__await__()

    wrapper = _AsyncUnaryResponseWrapper(FaultyUnaryCall(), mock_tracer_ctx)

    with pytest.raises(RuntimeError, match="unary_failed"):
        await wrapper

    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_unary_response_wrapper_delegation(mock_tracer_ctx):
    mock_response = MagicMock()
    mock_response.cancel.return_value = True
    mock_response.cancelled.return_value = False
    mock_response.code.return_value = 0
    mock_response.details.return_value = "details"
    mock_response.done.return_value = True
    mock_response.initial_metadata.return_value = []
    mock_response.time_remaining.return_value = 10.0
    mock_response.trailing_metadata.return_value = []
    mock_response.wait_for_connection.return_value = None
    mock_response.write.return_value = None
    mock_response.done_writing.return_value = None
    mock_response.custom_attribute = "custom"

    wrapper = _AsyncUnaryResponseWrapper(mock_response, mock_tracer_ctx)

    assert wrapper.cancel() is True
    mock_response.cancel.assert_called_once()
    assert wrapper.cancelled() is False
    assert wrapper.code() == 0
    assert wrapper.details() == "details"
    assert wrapper.done() is True
    assert wrapper.initial_metadata() == []
    assert wrapper.time_remaining() == 10.0
    assert wrapper.trailing_metadata() == []
    assert wrapper.wait_for_connection() is None
    assert wrapper.write("msg") is None
    mock_response.write.assert_called_once_with("msg")
    assert wrapper.done_writing() is None
    mock_response.done_writing.assert_called_once()
    assert wrapper.custom_attribute == "custom"

    callback = MagicMock()
    wrapper.add_done_callback(callback)
    mock_response.add_done_callback.assert_called_once_with(callback)


def test_async_unary_response_wrapper_del_unrecorded(mock_tracer_ctx):
    mock_response = MagicMock()
    wrapper = _AsyncUnaryResponseWrapper(mock_response, mock_tracer_ctx)
    wrapper.__del__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()

    # Second call should not record again
    wrapper.__del__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_anext_direct(mock_tracer_ctx):
    class MockCall:
        def initial_metadata(self):
            return []

        def __aiter__(self):
            async def _generator():
                yield "val1"
                yield "val2"

            return _generator()

    wrapper = _AsyncStreamingResponseWrapper(MockCall(), mock_tracer_ctx)
    # Direct __anext__ without calling __aiter__ first (matching StreamedResultSet._consume_next)
    assert await wrapper.__anext__() == "val1"
    assert await wrapper.__anext__() == "val2"
    with pytest.raises(StopAsyncIteration):
        await wrapper.__anext__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_anext_without_aiter(mock_tracer_ctx):
    class MockCallWithoutAiter:
        def initial_metadata(self):
            return []

        async def __anext__(self):
            raise StopAsyncIteration

    wrapper = _AsyncStreamingResponseWrapper(MockCallWithoutAiter(), mock_tracer_ctx)
    with pytest.raises(StopAsyncIteration):
        await wrapper.__anext__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_awaitable_metadata(mock_tracer_ctx):
    class MockCallAwaitableMetadata:
        async def initial_metadata(self):
            return [("server-timing", "gfet4t7; dur=42")]

        def __aiter__(self):
            async def _generator():
                yield "item"

            return _generator()

    wrapper = _AsyncStreamingResponseWrapper(
        MockCallAwaitableMetadata(), mock_tracer_ctx
    )
    async for _ in wrapper:
        pass
    mock_tracer_ctx.record_front_end_metrics.assert_called_once_with(
        [("server-timing", "gfet4t7; dur=42")]
    )


def test_async_streaming_response_wrapper_del_unrecorded(mock_tracer_ctx):
    mock_response = MagicMock()
    wrapper = _AsyncStreamingResponseWrapper(mock_response, mock_tracer_ctx)
    wrapper.__del__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()

    # Second call should not record again
    wrapper.__del__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


@pytest.mark.asyncio
async def test_async_streaming_response_wrapper_with_streamed_result_set(
    mock_tracer_ctx,
):
    from google.cloud.spanner_v1._async.streamed import StreamedResultSet
    from google.cloud.spanner_v1._helpers import _make_value_pb
    from google.cloud.spanner_v1.types import (
        PartialResultSet,
        ResultSetMetadata,
        StructType,
        Type,
        TypeCode,
    )

    metadata = ResultSetMetadata(
        row_type=StructType(
            fields=[StructType.Field(name="col", type_=Type(code=TypeCode.STRING))]
        )
    )
    partial_1 = PartialResultSet(metadata=metadata)
    partial_1.values.append(_make_value_pb("val1"))
    partial_2 = PartialResultSet()
    partial_2.values.append(_make_value_pb("val2"))

    class MockAsyncStreamCall:
        def initial_metadata(self):
            return [("server-timing", "gfet4t7; dur=50")]

        def __aiter__(self):
            async def _gen():
                yield partial_1
                yield partial_2

            return _gen()

    call = MockAsyncStreamCall()
    wrapper = _AsyncStreamingResponseWrapper(call, mock_tracer_ctx)

    streamed = StreamedResultSet(wrapper)
    rows = []
    async for row in streamed:
        rows.append(row)

    assert rows == [["val1"], ["val2"]]
    mock_tracer_ctx.record_attempt_completion.assert_called_once()
    mock_tracer_ctx.record_front_end_metrics.assert_called_once()


def test_sync_streaming_response_wrapper(mock_tracer_ctx):
    mock_response = iter(["item1", "item2"])
    wrapper = _StreamingResponseWrapper(mock_response, mock_tracer_ctx)

    items = list(wrapper)
    assert items == ["item1", "item2"]
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


def test_sync_streaming_response_wrapper_direct_next(mock_tracer_ctx):
    mock_response = ["item1"]
    wrapper = _StreamingResponseWrapper(mock_response, mock_tracer_ctx)

    assert next(wrapper) == "item1"
    with pytest.raises(StopIteration):
        next(wrapper)
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


def test_sync_streaming_response_wrapper_exception(mock_tracer_ctx):
    def faulty_generator():
        yield "item1"
        raise RuntimeError("stream_failed")

    wrapper = _StreamingResponseWrapper(faulty_generator(), mock_tracer_ctx)
    with pytest.raises(RuntimeError, match="stream_failed"):
        list(wrapper)
    mock_tracer_ctx.record_attempt_completion.assert_called_once()


def test_sync_streaming_response_wrapper_del_unrecorded(mock_tracer_ctx):
    mock_response = MagicMock()
    wrapper = _StreamingResponseWrapper(mock_response, mock_tracer_ctx)
    wrapper.__del__()
    mock_tracer_ctx.record_attempt_completion.assert_called_once()
