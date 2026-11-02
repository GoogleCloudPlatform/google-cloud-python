# Copyright 2017 Google LLC
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

try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER  # noqa: F401
except ImportError:  # pragma: NO COVER
    import mock  # type: ignore
import pytest  # noqa: I202

from ..helpers import warn_deprecated_credentials_file

try:
    import grpc
    from grpc import aio
except ImportError:  # pragma: NO COVER
    grpc = aio = None


if grpc is None:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)


import google.auth.credentials

from google.api_core import exceptions, grpc_helpers_async


class RpcErrorImpl(grpc.RpcError, grpc.Call):
    def __init__(self, code):
        super(RpcErrorImpl, self).__init__()
        self._code = code

    def code(self):
        return self._code

    def details(self):
        return None

    def trailing_metadata(self):
        return None


@pytest.mark.asyncio
async def test_wrap_unary_errors():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)
    callable_ = mock.AsyncMock(spec=["__call__"], side_effect=grpc_error)

    wrapped_callable = grpc_helpers_async._wrap_unary_errors(callable_)

    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        await wrapped_callable(1, 2, three="four")

    callable_.assert_called_once_with(1, 2, three="four")
    assert exc_info.value.response == grpc_error


@pytest.mark.asyncio
async def test_common_methods_in_wrapped_call():
    mock_call = mock.Mock(aio.UnaryUnaryCall, autospec=True)
    wrapped_call = grpc_helpers_async._WrappedUnaryUnaryCall().with_call(mock_call)

    await wrapped_call.initial_metadata()
    assert mock_call.initial_metadata.call_count == 1

    await wrapped_call.trailing_metadata()
    assert mock_call.trailing_metadata.call_count == 1

    await wrapped_call.code()
    assert mock_call.code.call_count == 1

    await wrapped_call.details()
    assert mock_call.details.call_count == 1

    wrapped_call.cancelled()
    assert mock_call.cancelled.call_count == 1

    wrapped_call.done()
    assert mock_call.done.call_count == 1

    wrapped_call.time_remaining()
    assert mock_call.time_remaining.call_count == 1

    wrapped_call.cancel()
    assert mock_call.cancel.call_count == 1

    callback = mock.sentinel.callback
    wrapped_call.add_done_callback(callback)
    mock_call.add_done_callback.assert_called_once_with(callback)

    await wrapped_call.wait_for_connection()
    assert mock_call.wait_for_connection.call_count == 1


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "callable_type,expected_wrapper_type",
    [
        (grpc.aio.UnaryStreamMultiCallable, grpc_helpers_async._WrappedUnaryStreamCall),
        (grpc.aio.StreamUnaryMultiCallable, grpc_helpers_async._WrappedStreamUnaryCall),
        (
            grpc.aio.StreamStreamMultiCallable,
            grpc_helpers_async._WrappedStreamStreamCall,
        ),
    ],
)
async def test_wrap_errors_w_stream_type(callable_type, expected_wrapper_type):
    class ConcreteMulticallable(callable_type):
        def __call__(self, *args, **kwargs):
            raise NotImplementedError("Should not be called")

    with mock.patch.object(
        grpc_helpers_async, "_wrap_stream_errors"
    ) as wrap_stream_errors:
        callable_ = ConcreteMulticallable()
        grpc_helpers_async.wrap_errors(callable_)
        assert wrap_stream_errors.call_count == 1
        wrap_stream_errors.assert_called_once_with(callable_, expected_wrapper_type)


@pytest.mark.asyncio
async def test_wrap_stream_errors_unary_stream():
    mock_call = mock.Mock(aio.UnaryStreamCall, autospec=True)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedUnaryStreamCall
    )

    await wrapped_callable(1, 2, three="four")
    multicallable.assert_called_once_with(1, 2, three="four")
    assert mock_call.wait_for_connection.call_count == 1


@pytest.mark.asyncio
async def test_wrap_stream_errors_stream_unary():
    mock_call = mock.Mock(aio.StreamUnaryCall, autospec=True)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamUnaryCall
    )

    await wrapped_callable(1, 2, three="four")
    multicallable.assert_called_once_with(1, 2, three="four")
    assert mock_call.wait_for_connection.call_count == 1


@pytest.mark.asyncio
async def test_wrap_stream_errors_stream_stream():
    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )

    await wrapped_callable(1, 2, three="four")
    multicallable.assert_called_once_with(1, 2, three="four")
    assert mock_call.wait_for_connection.call_count == 1


@pytest.mark.asyncio
async def test_wrap_stream_errors_raised():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)
    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    mock_call.wait_for_connection = mock.AsyncMock(side_effect=[grpc_error])
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )

    with pytest.raises(exceptions.InvalidArgument):
        await wrapped_callable()
    assert mock_call.wait_for_connection.call_count == 1


@pytest.mark.asyncio
async def test_wrap_stream_errors_read():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)

    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    mock_call.read = mock.AsyncMock(side_effect=grpc_error)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )

    wrapped_call = await wrapped_callable(1, 2, three="four")
    multicallable.assert_called_once_with(1, 2, three="four")
    assert mock_call.wait_for_connection.call_count == 1

    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        await wrapped_call.read()
    assert exc_info.value.response == grpc_error


@pytest.mark.asyncio
async def test_wrap_stream_errors_aiter():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)

    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    mocked_aiter = mock.Mock(spec=["__anext__"])
    mocked_aiter.__anext__ = mock.AsyncMock(
        side_effect=[mock.sentinel.response, grpc_error]
    )
    mock_call.__aiter__ = mock.Mock(return_value=mocked_aiter)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )
    wrapped_call = await wrapped_callable()

    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        async for response in wrapped_call:
            assert response == mock.sentinel.response
    assert exc_info.value.response == grpc_error


@pytest.mark.asyncio
async def test_wrap_stream_errors_aiter_non_rpc_error():
    non_grpc_error = TypeError("Not a gRPC error")

    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    mocked_aiter = mock.Mock(spec=["__anext__"])
    mocked_aiter.__anext__ = mock.AsyncMock(
        side_effect=[mock.sentinel.response, non_grpc_error]
    )
    mock_call.__aiter__ = mock.Mock(return_value=mocked_aiter)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )
    wrapped_call = await wrapped_callable()

    with pytest.raises(TypeError) as exc_info:
        async for response in wrapped_call:
            assert response == mock.sentinel.response
    assert exc_info.value == non_grpc_error


@pytest.mark.asyncio
async def test_wrap_stream_errors_aiter_called_multiple_times():
    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )
    wrapped_call = await wrapped_callable()

    assert wrapped_call.__aiter__() == wrapped_call.__aiter__()


@pytest.mark.asyncio
async def test_wrap_stream_errors_write():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)

    mock_call = mock.Mock(aio.StreamStreamCall, autospec=True)
    mock_call.write = mock.AsyncMock(side_effect=[None, grpc_error])
    mock_call.done_writing = mock.AsyncMock(side_effect=[None, grpc_error])
    multicallable = mock.Mock(return_value=mock_call)

    wrapped_callable = grpc_helpers_async._wrap_stream_errors(
        multicallable, grpc_helpers_async._WrappedStreamStreamCall
    )

    wrapped_call = await wrapped_callable()

    await wrapped_call.write(mock.sentinel.request)
    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        await wrapped_call.write(mock.sentinel.request)
    assert mock_call.write.call_count == 2
    assert exc_info.value.response == grpc_error

    await wrapped_call.done_writing()
    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        await wrapped_call.done_writing()
    assert mock_call.done_writing.call_count == 2
    assert exc_info.value.response == grpc_error


@mock.patch("google.api_core.grpc_helpers_async._wrap_unary_errors")
def test_wrap_errors_non_streaming(wrap_unary_errors):
    callable_ = mock.create_autospec(aio.UnaryUnaryMultiCallable)

    result = grpc_helpers_async.wrap_errors(callable_)

    assert result == wrap_unary_errors.return_value
    wrap_unary_errors.assert_called_once_with(callable_)


def test_grpc_async_stream():
    """
    GrpcAsyncStream type should be both an AsyncIterator and a grpc.aio.Call.
    """
    instance = grpc_helpers_async.GrpcAsyncStream[int]()
    assert isinstance(instance, grpc.aio.Call)
    # should implement __aiter__ and __anext__
    assert hasattr(instance, "__aiter__")
    it = instance.__aiter__()
    assert hasattr(it, "__anext__")


def test_awaitable_grpc_call():
    """
    AwaitableGrpcCall type should be an Awaitable and a grpc.aio.Call.
    """
    instance = grpc_helpers_async.AwaitableGrpcCall()
    assert isinstance(instance, grpc.aio.Call)
    # should implement __await__
    assert hasattr(instance, "__await__")


@mock.patch("google.api_core.grpc_helpers_async._wrap_stream_errors")
def test_wrap_errors_streaming(wrap_stream_errors):
    callable_ = mock.create_autospec(aio.UnaryStreamMultiCallable)

    result = grpc_helpers_async.wrap_errors(callable_)

    assert result == wrap_stream_errors.return_value
    wrap_stream_errors.assert_called_once_with(
        callable_, grpc_helpers_async._WrappedUnaryStreamCall
    )


@pytest.mark.parametrize(
    "attempt_direct_path,target,expected_target",
    [
        (None, "example.com:443", "example.com:443"),
        (False, "example.com:443", "example.com:443"),
        (True, "example.com:443", "google-c2p:///example.com"),
        (True, "dns:///example.com", "google-c2p:///example.com"),
        (True, "another-c2p:///example.com", "another-c2p:///example.com"),
    ],
)
@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_implicit(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
    attempt_direct_path,
    target,
    expected_target,
):
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        target, attempt_direct_path=attempt_direct_path
    )

    assert channel is grpc_secure_channel.return_value

    google_auth_default.assert_called_once_with(scopes=None, default_scopes=None)
    grpc_secure_channel.assert_called_once_with(
        expected_target, composite_creds, compression=None
    )


@pytest.mark.parametrize(
    "attempt_direct_path,target, expected_target",
    [
        (None, "example.com:443", "example.com:443"),
        (False, "example.com:443", "example.com:443"),
        (True, "example.com:443", "google-c2p:///example.com"),
        (True, "dns:///example.com", "google-c2p:///example.com"),
        (True, "another-c2p:///example.com", "another-c2p:///example.com"),
    ],
)
@mock.patch("google.auth.transport.grpc.AuthMetadataPlugin", autospec=True)
@mock.patch(
    "google.auth.transport.requests.Request",
    autospec=True,
    return_value=mock.sentinel.Request,
)
@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_implicit_with_default_host(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
    request,
    auth_metadata_plugin,
    attempt_direct_path,
    target,
    expected_target,
):
    default_host = "example.com"
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        target, default_host=default_host, attempt_direct_path=attempt_direct_path
    )

    assert channel is grpc_secure_channel.return_value

    google_auth_default.assert_called_once_with(scopes=None, default_scopes=None)
    assert auth_metadata_plugin.call_count == 1
    assert auth_metadata_plugin.call_args.args == (
        mock.sentinel.credentials,
        mock.sentinel.Request,
    )
    assert auth_metadata_plugin.call_args.kwargs["default_host"] == default_host
    # google-auth >= 2.56.3 supports suppress_metrics_header; older versions omit it during fallback
    if "suppress_metrics_header" in auth_metadata_plugin.call_args.kwargs:
        assert auth_metadata_plugin.call_args.kwargs["suppress_metrics_header"] is True
    grpc_secure_channel.assert_called_once_with(
        expected_target, composite_creds, compression=None
    )


@pytest.mark.parametrize(
    "attempt_direct_path",
    [
        None,
        False,
    ],
)
@mock.patch("grpc.composite_channel_credentials")
@mock.patch(
    "google.auth.default",
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_implicit_with_ssl_creds(
    grpc_secure_channel, default, composite_creds_call, attempt_direct_path
):
    target = "example.com:443"

    ssl_creds = grpc.ssl_channel_credentials()

    grpc_helpers_async.create_channel(
        target, ssl_credentials=ssl_creds, attempt_direct_path=attempt_direct_path
    )

    default.assert_called_once_with(scopes=None, default_scopes=None)
    composite_creds_call.assert_called_once_with(ssl_creds, mock.ANY)
    composite_creds = composite_creds_call.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=None
    )


def test_create_channel_implicit_with_ssl_creds_attempt_direct_path_true():
    target = "example.com:443"
    ssl_creds = grpc.ssl_channel_credentials()
    with pytest.raises(
        ValueError, match="Using ssl_credentials with Direct Path is not supported"
    ):
        grpc_helpers_async.create_channel(
            target, ssl_credentials=ssl_creds, attempt_direct_path=True
        )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_implicit_with_scopes(
    grpc_secure_channel, default, composite_creds_call
):
    target = "example.com:443"
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(target, scopes=["one", "two"])

    assert channel is grpc_secure_channel.return_value

    default.assert_called_once_with(scopes=["one", "two"], default_scopes=None)
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=None
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_implicit_with_default_scopes(
    grpc_secure_channel, default, composite_creds_call
):
    target = "example.com:443"
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        target, default_scopes=["three", "four"], compression=grpc.Compression.Gzip
    )

    assert channel is grpc_secure_channel.return_value

    default.assert_called_once_with(scopes=None, default_scopes=["three", "four"])
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=grpc.Compression.Gzip
    )


def test_create_channel_explicit_with_duplicate_credentials():
    target = "example:443"

    with pytest.raises(exceptions.DuplicateCredentialArgs) as excinfo:
        with warn_deprecated_credentials_file():
            grpc_helpers_async.create_channel(
                target,
                credentials_file="credentials.json",
                credentials=mock.sentinel.credentials,
            )

    assert "mutually exclusive" in str(excinfo.value)


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("google.auth.credentials.with_scopes_if_required", autospec=True)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_explicit(grpc_secure_channel, auth_creds, composite_creds_call):
    target = "example.com:443"
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        target, credentials=mock.sentinel.credentials, compression=grpc.Compression.Gzip
    )

    auth_creds.assert_called_once_with(
        mock.sentinel.credentials, scopes=None, default_scopes=None
    )
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=grpc.Compression.Gzip
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_explicit_scoped(grpc_secure_channel, composite_creds_call):
    target = "example.com:443"
    scopes = ["1", "2"]
    composite_creds = composite_creds_call.return_value

    credentials = mock.create_autospec(google.auth.credentials.Scoped, instance=True)
    credentials.requires_scopes = True

    channel = grpc_helpers_async.create_channel(
        target,
        credentials=credentials,
        scopes=scopes,
        compression=grpc.Compression.Gzip,
    )

    credentials.with_scopes.assert_called_once_with(scopes, default_scopes=None)
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=grpc.Compression.Gzip
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_explicit_default_scopes(
    grpc_secure_channel, composite_creds_call
):
    target = "example.com:443"
    default_scopes = ["3", "4"]
    composite_creds = composite_creds_call.return_value

    credentials = mock.create_autospec(google.auth.credentials.Scoped, instance=True)
    credentials.requires_scopes = True

    channel = grpc_helpers_async.create_channel(
        target,
        credentials=credentials,
        default_scopes=default_scopes,
        compression=grpc.Compression.Gzip,
    )

    credentials.with_scopes.assert_called_once_with(
        scopes=None, default_scopes=default_scopes
    )
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=grpc.Compression.Gzip
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_explicit_with_quota_project(
    grpc_secure_channel, composite_creds_call
):
    target = "example.com:443"
    composite_creds = composite_creds_call.return_value

    credentials = mock.create_autospec(
        google.auth.credentials.CredentialsWithQuotaProject, instance=True
    )

    channel = grpc_helpers_async.create_channel(
        target, credentials=credentials, quota_project_id="project-foo"
    )

    credentials.with_quota_project.assert_called_once_with("project-foo")
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=None
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("grpc.aio.secure_channel")
@mock.patch(
    "google.auth.load_credentials_from_file",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
def test_create_channel_with_credentials_file(
    load_credentials_from_file, grpc_secure_channel, composite_creds_call
):
    target = "example.com:443"

    credentials_file = "/path/to/credentials/file.json"
    composite_creds = composite_creds_call.return_value

    with warn_deprecated_credentials_file():
        channel = grpc_helpers_async.create_channel(
            target, credentials_file=credentials_file
        )

    google.auth.load_credentials_from_file.assert_called_once_with(
        credentials_file, scopes=None, default_scopes=None
    )
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=None
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("grpc.aio.secure_channel")
@mock.patch(
    "google.auth.load_credentials_from_file",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
def test_create_channel_with_credentials_file_and_scopes(
    load_credentials_from_file, grpc_secure_channel, composite_creds_call
):
    target = "example.com:443"
    scopes = ["1", "2"]

    credentials_file = "/path/to/credentials/file.json"
    composite_creds = composite_creds_call.return_value

    with warn_deprecated_credentials_file():
        channel = grpc_helpers_async.create_channel(
            target, credentials_file=credentials_file, scopes=scopes
        )

    google.auth.load_credentials_from_file.assert_called_once_with(
        credentials_file, scopes=scopes, default_scopes=None
    )
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=None
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch("grpc.aio.secure_channel")
@mock.patch(
    "google.auth.load_credentials_from_file",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
def test_create_channel_with_credentials_file_and_default_scopes(
    load_credentials_from_file, grpc_secure_channel, composite_creds_call
):
    target = "example.com:443"
    default_scopes = ["3", "4"]

    credentials_file = "/path/to/credentials/file.json"
    composite_creds = composite_creds_call.return_value

    with warn_deprecated_credentials_file():
        channel = grpc_helpers_async.create_channel(
            target, credentials_file=credentials_file, default_scopes=default_scopes
        )

    google.auth.load_credentials_from_file.assert_called_once_with(
        credentials_file, scopes=None, default_scopes=default_scopes
    )
    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        target, composite_creds, compression=None
    )


@mock.patch("grpc.aio.secure_channel")
def test_create_channel(grpc_secure_channel):
    target = "example.com:443"
    scopes = ["test_scope"]

    credentials = mock.create_autospec(google.auth.credentials.Scoped, instance=True)
    credentials.requires_scopes = True

    grpc_helpers_async.create_channel(target, credentials=credentials, scopes=scopes)
    grpc_secure_channel.assert_called()
    credentials.with_scopes.assert_called_once_with(scopes, default_scopes=None)


@mock.patch("grpc.ssl_channel_credentials")
@mock.patch("grpc.composite_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_attempt_direct_path_xds_over_interconnect_default_ssl(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
    ssl_creds_call,
):
    composite_creds = composite_creds_call.return_value
    default_ssl_creds = ssl_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=True,
    )

    assert channel is grpc_secure_channel.return_value
    ssl_creds_call.assert_called_once_with()
    assert composite_creds_call.call_args.args[0] is default_ssl_creds
    grpc_secure_channel.assert_called_once_with(
        "google-c2p:///storage-direct.googleapis.com?force-xds",
        composite_creds,
        compression=None,
        options=(("grpc.default_authority", "storage.googleapis.com"),),
    )


@mock.patch("grpc.composite_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_attempt_direct_path_xds_over_interconnect_custom_ssl(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
):
    composite_creds = composite_creds_call.return_value
    custom_ssl_creds = mock.sentinel.custom_ssl_creds

    channel = grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        ssl_credentials=custom_ssl_creds,
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=True,
    )

    assert channel is grpc_secure_channel.return_value
    assert composite_creds_call.call_args.args[0] is custom_ssl_creds
    grpc_secure_channel.assert_called_once_with(
        "google-c2p:///storage-direct.googleapis.com?force-xds",
        composite_creds,
        compression=None,
        options=(("grpc.default_authority", "storage.googleapis.com"),),
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_interconnect_fallback(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
):
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path=False,
        attempt_direct_path_xds_over_interconnect=False,
    )

    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        "storage.googleapis.com:443",
        composite_creds,
        compression=None,
    )


@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_interconnect_fallback_preserves_non_google_direct_host(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
):
    composite_creds = composite_creds_call.return_value

    channel = grpc_helpers_async.create_channel(
        "my-direct.example.com:443",
        attempt_direct_path=False,
        attempt_direct_path_xds_over_interconnect=False,
    )

    assert channel is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_once_with(
        "my-direct.example.com:443",
        composite_creds,
        compression=None,
    )

    channel2 = grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com.example.com:443",
        attempt_direct_path=False,
        attempt_direct_path_xds_over_interconnect=False,
    )
    assert channel2 is grpc_secure_channel.return_value
    grpc_secure_channel.assert_called_with(
        "storage-direct.googleapis.com.example.com:443",
        composite_creds,
        compression=None,
    )


def test_create_channel_async_invalid_env_var_raises(monkeypatch):
    monkeypatch.setenv(
        "GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT", "invalid"
    )
    with pytest.raises(
        ValueError,
        match="Invalid value for GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT",
    ):
        grpc_helpers_async.create_channel(
            "storage-direct.googleapis.com:443",
            attempt_direct_path=True,
        )


@mock.patch("grpc.ssl_channel_credentials")
@mock.patch("grpc.composite_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_async_interconnect_authority_branches(
    grpc_secure_channel,
    google_auth_default,
    composite_creds_call,
    ssl_creds_call,
):
    composite_creds = composite_creds_call.return_value

    # Authority is None (target does not contain -direct.googleapis.com)
    grpc_helpers_async.create_channel(
        "storage.googleapis.com:443",
        attempt_direct_path_xds_over_interconnect=True,
    )
    grpc_secure_channel.assert_called_with(
        "google-c2p:///storage.googleapis.com?force-xds",
        composite_creds,
        compression=None,
    )

    # Authority exists, but grpc.default_authority is already provided
    custom_options_default = (("grpc.default_authority", "custom.googleapis.com"),)
    grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path_xds_over_interconnect=True,
        options=custom_options_default,
    )
    grpc_secure_channel.assert_called_with(
        "google-c2p:///storage-direct.googleapis.com?force-xds",
        composite_creds,
        compression=None,
        options=custom_options_default,
    )

    # Authority exists, but grpc.ssl_target_name_override is already provided
    custom_options_ssl = (("grpc.ssl_target_name_override", "custom.googleapis.com"),)
    grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path_xds_over_interconnect=True,
        options=custom_options_ssl,
    )
    grpc_secure_channel.assert_called_with(
        "google-c2p:///storage-direct.googleapis.com?force-xds",
        composite_creds,
        compression=None,
        options=custom_options_ssl,
    )


@mock.patch("grpc.ssl_channel_credentials")
@mock.patch("grpc.composite_channel_credentials")
@mock.patch("grpc.compute_engine_channel_credentials")
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
@mock.patch("grpc.aio.secure_channel")
def test_create_channel_async_interconnect_gated_by_attempt_direct_path(
    grpc_secure_channel,
    google_auth_default,
    compute_engine_creds_call,
    composite_creds_call,
    ssl_creds_call,
    monkeypatch,
):
    monkeypatch.setenv("GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT", "true")
    composite_creds = composite_creds_call.return_value
    compute_creds = compute_engine_creds_call.return_value

    # When attempt_direct_path is False (default), env var override is ignored
    grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path=False,
    )
    grpc_secure_channel.assert_called_with(
        "storage.googleapis.com:443",
        compute_creds,
        compression=None,
    )

    # When attempt_direct_path is True, env var override activates DirectPath Interconnect
    grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path=True,
    )
    grpc_secure_channel.assert_called_with(
        "google-c2p:///storage-direct.googleapis.com?force-xds",
        composite_creds,
        compression=None,
        options=(("grpc.default_authority", "storage.googleapis.com"),),
    )

    # When attempt_direct_path_xds_over_interconnect is True explicitly, Interconnect activates
    grpc_helpers_async.create_channel(
        "storage-direct.googleapis.com:443",
        attempt_direct_path=False,
        attempt_direct_path_xds_over_interconnect=True,
    )
    grpc_secure_channel.assert_called_with(
        "google-c2p:///storage-direct.googleapis.com?force-xds",
        composite_creds,
        compression=None,
        options=(("grpc.default_authority", "storage.googleapis.com"),),
    )

    # When target already starts with google-c2p:/// and attempt_direct_path=False, preserve target
    grpc_helpers_async.create_channel(
        "google-c2p:///storage-direct.googleapis.com",
        attempt_direct_path=False,
    )
    grpc_secure_channel.assert_called_with(
        "google-c2p:///storage-direct.googleapis.com",
        compute_creds,
        compression=None,
    )


@pytest.mark.asyncio
async def test_fake_stream_unary_call():
    fake_call = grpc_helpers_async.FakeStreamUnaryCall()
    await fake_call.wait_for_connection()
    response = await fake_call
    assert fake_call.response == response


def test_apply_channel_interceptors_none_or_empty():
    channel = mock.Mock()
    assert grpc_helpers_async.apply_channel_interceptors(channel, None) is channel
    assert grpc_helpers_async.apply_channel_interceptors(channel, []) is channel


def test_apply_channel_interceptors_channel_without_attr():
    channel = object()
    interceptor = mock.Mock()
    assert (
        grpc_helpers_async.apply_channel_interceptors(channel, [interceptor]) is channel
    )


def test_apply_channel_interceptors_list():
    interceptor1 = mock.Mock()
    interceptor2 = mock.Mock()
    channel = mock.Mock()
    channel._unary_unary_interceptors = [interceptor1]

    result = grpc_helpers_async.apply_channel_interceptors(
        channel, [interceptor1, interceptor2]
    )
    assert result is channel
    assert channel._unary_unary_interceptors == [interceptor1, interceptor2]


def test_apply_channel_interceptors_mock():
    interceptor1 = mock.Mock()
    interceptor2 = mock.Mock()
    channel = mock.Mock()
    channel._unary_unary_interceptors = mock.Mock(spec=["append"])

    result = grpc_helpers_async.apply_channel_interceptors(
        channel, [interceptor1, interceptor2]
    )
    assert result is channel
    channel._unary_unary_interceptors.append.assert_any_call(interceptor1)
    channel._unary_unary_interceptors.append.assert_any_call(interceptor2)


def test_apply_channel_interceptors_inner_target_not_appendable():
    channel = mock.Mock(spec=["_unary_unary_interceptors"])
    channel._unary_unary_interceptors = 123
    interceptor = mock.Mock(spec=["intercept_unary_unary"])
    assert (
        grpc_helpers_async.apply_channel_interceptors(channel, [interceptor]) is channel
    )


def test_apply_channel_interceptors_fallback_not_appendable():
    channel = mock.Mock(spec=["_unary_unary_interceptors"])
    channel._unary_unary_interceptors = 123
    interceptor = mock.Mock(spec=[])
    assert (
        grpc_helpers_async.apply_channel_interceptors(channel, [interceptor]) is channel
    )


def test_apply_channel_interceptors_fallback_unary_unary_list():
    class CustomInterceptor:
        pass

    interceptor1 = CustomInterceptor()
    interceptor2 = CustomInterceptor()
    channel = mock.Mock(spec=["_unary_unary_interceptors"])
    channel._unary_unary_interceptors = [interceptor1]

    result = grpc_helpers_async.apply_channel_interceptors(
        channel, [interceptor1, interceptor2]
    )
    assert result is channel
    assert channel._unary_unary_interceptors == [interceptor1, interceptor2]


def test_apply_channel_interceptors_fallback_unary_unary_appendable():
    class CustomInterceptor:
        pass

    interceptor = CustomInterceptor()
    channel = mock.Mock(spec=["_unary_unary_interceptors"])
    mock_append = mock.Mock(spec=["append"])
    channel._unary_unary_interceptors = mock_append

    result = grpc_helpers_async.apply_channel_interceptors(channel, [interceptor])
    assert result is channel
    mock_append.append.assert_called_once_with(interceptor)
