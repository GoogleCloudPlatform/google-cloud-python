# Copyright 2018 Google LLC
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


import contextlib
import os
from pathlib import Path
from typing import Sequence, Tuple
from unittest import mock

import google.api_core
import grpc
import pytest
import pytest_asyncio
from google.api_core.client_options import ClientOptions  # type: ignore
from google.showcase_v1beta1.services.echo.transports import EchoRestInterceptor
from requests.adapters import HTTPAdapter

try:
    from google.api_core import _observability
except ImportError:
    _observability = None


def _installed_core_matches_monorepo() -> bool:
    """Returns True if the installed google.api_core matches the monorepo source.

    When running Showcase tests against PyPI dependencies (e.g. non-canary CI jobs),
    the installed `google-api-core` release may lag behind unreleased changes in
    `packages/google-api-core`. Comparing the installed package files against the
    monorepo source allows system tests to still execute end-to-end RPCs against
    PyPI `google-api-core` while deferring strict monorepo-specific assertions to
    `showcase-canary` (`INSTALL_LOCAL_CORE=true`).
    """
    repo_root = Path(__file__).resolve().parents[4]
    monorepo_core_dir = (
        repo_root / "packages" / "google-api-core" / "google" / "api_core"
    )
    installed_core_init = getattr(google.api_core, "__file__", None)

    # Are we running outside the monorepo (e.g. in a standalone export)
    # where the sibling `packages/google-api-core` directory does not exist?
    # If so, there is no local monorepo source to compare against, so do not skip tests.
    has_monorepo_source = monorepo_core_dir.is_dir() and installed_core_init is not None
    if not has_monorepo_source:
        return True

    # Was `google-api-core` installed in editable mode (`pip install -e`)
    # or via PYTHONPATH directly from the monorepo (`showcase-canary`)?
    # If both paths resolve to the same directory, the code is guaranteed to match.
    installed_core_dir = Path(installed_core_init).resolve().parent
    is_editable_monorepo_install = installed_core_dir == monorepo_core_dir
    if is_editable_monorepo_install:
        return True

    # Is `google-api-core` installed from PyPI into `site-packages`.
    # Because `version.py` on `main` is not bumped until release time, we cannot
    # rely on `__version__` to detect unreleased commits. Instead, verify that every
    # Python file in the monorepo exists in the installed package with identical text.
    for monorepo_file in monorepo_core_dir.rglob("*.py"):
        relative_path = monorepo_file.relative_to(monorepo_core_dir)
        installed_file = installed_core_dir / relative_path
        if not installed_file.is_file():
            return False

        monorepo_code = monorepo_file.read_text(encoding="utf-8")
        installed_code = installed_file.read_text(encoding="utf-8")
        if monorepo_code != installed_code:
            return False

    return True


INSTALLED_CORE_MATCHES_MONOREPO = _installed_core_matches_monorepo()


@contextlib.contextmanager
def skip_on_core_mismatch():
    """Runs assertions and skips only if they fail while PyPI google-api-core lags monorepo."""
    try:
        yield
    except AssertionError:
        if not INSTALLED_CORE_MATCHES_MONOREPO:
            pytest.skip(
                "Installed PyPI google-api-core differs from monorepo source; "
                "validated by showcase-canary (INSTALL_LOCAL_CORE=true)."
            )
        raise


try:
    from google.auth.aio import credentials as ga_credentials_async

    HAS_GOOGLE_AUTH_AIO = True
# NOTE: `pragma: NO COVER` is needed since the coverage for presubmits isn't combined.
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False
import google.auth
from google.auth import credentials as ga_credentials
from google.showcase import EchoClient, IdentityClient, MessagingClient

try:
    from google.showcase import ResumableUploadServiceClient

    HAS_RESUMABLE_UPLOAD_CLIENT = True
except ImportError:
    HAS_RESUMABLE_UPLOAD_CLIENT = False

HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT = False
if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    import asyncio

    from google.showcase import EchoAsyncClient, IdentityAsyncClient
    from grpc.experimental import aio

    try:
        from google.showcase_v1beta1.services.echo.transports import (
            AsyncEchoRestInterceptor,
            AsyncEchoRestTransport,
        )

        HAS_ASYNC_REST_ECHO_TRANSPORT = True
    except:
        HAS_ASYNC_REST_ECHO_TRANSPORT = False
    try:
        from google.showcase_v1beta1.services.identity.transports import (
            AsyncIdentityRestTransport,
        )

        HAS_ASYNC_REST_IDENTITY_TRANSPORT = True
    except:
        HAS_ASYNC_REST_IDENTITY_TRANSPORT = False
    try:
        from google.showcase import ResumableUploadServiceAsyncClient
        from google.showcase_v1beta1.services.resumable_upload_service.transports.rest_asyncio import (
            AsyncResumableUploadServiceRestInterceptor,
            AsyncResumableUploadServiceRestTransport,
        )

        HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT = True
    except:
        HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT = False

    _GRPC_VERSION = grpc.__version__

    # TODO: use async auth anon credentials by default once the minimum version of google-auth is upgraded.
    # See related issue: https://github.com/googleapis/gapic-generator-python/issues/2107.
    def async_anonymous_credentials():
        if HAS_GOOGLE_AUTH_AIO:
            return ga_credentials_async.AnonymousCredentials()
        return ga_credentials.AnonymousCredentials()

    _test_event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(_test_event_loop)

    # NOTE(lidiz) We must override the default event_loop fixture from
    # pytest-asyncio. pytest fixture frees resources once there isn't any reference
    # to it. So, the event loop might close before tests finishes. In the
    # customized version, we don't close the event loop.

    @pytest.fixture
    def event_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop

    @pytest_asyncio.fixture(params=["grpc_asyncio", "rest_asyncio"])
    def async_echo(use_mtls, request, event_loop):
        transport = request.param
        if transport == "rest_asyncio" and not HAS_ASYNC_REST_ECHO_TRANSPORT:
            pytest.skip("Skipping test with async rest.")
        return construct_client(
            EchoAsyncClient,
            use_mtls,
            transport_name=transport,
            channel_creator=(
                aio.insecure_channel if request.param == "grpc_asyncio" else None
            ),
            credentials=async_anonymous_credentials(),
        )

    @pytest_asyncio.fixture(params=["grpc_asyncio", "rest_asyncio"])
    def async_identity(use_mtls, request, event_loop):
        transport = request.param
        if transport == "rest_asyncio" and not HAS_ASYNC_REST_IDENTITY_TRANSPORT:
            pytest.skip("Skipping test with async rest.")
        return construct_client(
            IdentityAsyncClient,
            use_mtls,
            transport_name=transport,
            channel_creator=(
                aio.insecure_channel if request.param == "grpc_asyncio" else None
            ),
            credentials=async_anonymous_credentials(),
        )


base_dir = os.path.dirname(__file__)
CERT_PATH = os.path.join(base_dir, "../cert/mtls.crt")
KEY_PATH = os.path.join(base_dir, "../cert/mtls.key")
with open(CERT_PATH, "rb") as fh:
    cert = fh.read()
with open(KEY_PATH, "rb") as fh:
    key = fh.read()

ssl_credentials = grpc.ssl_channel_credentials(
    root_certificates=cert, certificate_chain=cert, private_key=key
)
tls_credentials = grpc.ssl_channel_credentials(root_certificates=cert)


def callback():
    return cert, key


default_mtls_client_options = ClientOptions()
default_mtls_client_options.client_cert_source = callback


def pytest_addoption(parser):
    parser.addoption(
        "--mtls", action="store_true", help="Run system test with mutual TLS channel"
    )
    parser.addoption(
        "--tls",
        action="store_true",
        help="Run system test with standard one-way TLS channel",
    )


# TODO: Need to test  without passing in a transport class
def construct_client(
    client_class,
    use_mtls,
    transport_name="grpc",
    channel_creator=grpc.insecure_channel,  # for grpc,grpc_asyncio only
    credentials=ga_credentials.AnonymousCredentials(),
    transport_endpoint="localhost:7469",
    client_options=None,
):
    if use_mtls:
        with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
            with mock.patch(
                "grpc.ssl_channel_credentials", autospec=True
            ) as mock_ssl_cred:
                mock_ssl_cred.return_value = ssl_credentials
                client = client_class(
                    credentials=credentials,
                    client_options=client_options or default_mtls_client_options,
                )
                mock_ssl_cred.assert_called_once_with(
                    certificate_chain=cert, private_key=key
                )
                return client
    else:
        transport_cls = client_class.get_transport_class(transport_name)
        if transport_name in ["grpc", "grpc_asyncio"]:
            # TODO(gapic-generator-python/issues/1914): Need to test grpc transports without a channel_creator
            assert channel_creator
            transport_kwargs = {
                "credentials": credentials,
                "channel": channel_creator(transport_endpoint),
                "client_options": client_options,
            }
            transport = transport_cls(**transport_kwargs)
        elif transport_name in ["rest", "rest_asyncio"]:
            # The custom host explicitly bypasses https.
            transport = transport_cls(
                credentials=credentials,
                host=transport_endpoint,
                url_scheme="http",
                client_options=client_options,
            )
        else:
            raise RuntimeError(f"Unexpected transport type: {transport_name}")

        client = client_class(transport=transport, client_options=client_options)
        return client


@pytest.fixture
def use_mtls(request):
    return request.config.getoption("--mtls")


@pytest.fixture
def use_tls(request):
    return request.config.getoption("--tls") or request.config.getoption("--mtls")


@pytest.fixture
def parametrized_echo(
    use_mtls,
    channel_creator,
    transport_name,
    transport_endpoint,
    credential_universe,
    client_universe,
):
    print(
        f"test_params: {channel_creator, transport_name, transport_endpoint, credential_universe, client_universe}"
    )
    credentials = ga_credentials.AnonymousCredentials()
    # TODO: This is needed to cater for older versions of google-auth
    # Make this test unconditional once the minimum supported version of
    # google-auth becomes 2.23.0 or higher.
    google_auth_major, google_auth_minor = [
        int(part) for part in google.auth.__version__.split(".")[0:2]
    ]
    if google_auth_major > 2 or (google_auth_major == 2 and google_auth_minor >= 23):
        credentials._universe_domain = credential_universe
    client = construct_client(
        EchoClient,
        use_mtls,
        transport_endpoint=transport_endpoint,
        transport_name=transport_name,
        channel_creator=channel_creator,
        credentials=credentials,
    )
    # Since `channel_creator` does not take credentials, we set them
    # explicitly in the client for test purposes.
    #
    # TODO: verify that the transport gets the correct credentials
    # from the client.
    if credential_universe:
        client.transport._credentials = credentials
    return client


@pytest.fixture(params=["grpc", "rest"])
def echo(use_mtls, request):
    return construct_client(EchoClient, use_mtls, transport_name=request.param)


@pytest.fixture(params=["grpc", "rest"])
def echo_with_universe_credentials_localhost(use_mtls, request):
    return construct_client(
        EchoClient,
        use_mtls,
        transport_name=request.param,
        credentials=ga_credentials.AnonymousCredentials(
            universe_domain="localhost:7469"
        ),
    )


@pytest.fixture(params=["grpc", "rest"])
def identity(use_mtls, request):
    return construct_client(IdentityClient, use_mtls, transport_name=request.param)


@pytest.fixture(params=["grpc", "rest"])
def messaging(use_mtls, request):
    return construct_client(MessagingClient, use_mtls, transport_name=request.param)


class EchoMetadataClientRestInterceptor(EchoRestInterceptor):
    request_metadata: Sequence[Tuple[str, str]] = []
    response_metadata: Sequence[Tuple[str, str]] = []

    def pre_echo(self, request, metadata):
        self.request_metadata = metadata
        return request, metadata

    def post_echo_with_metadata(self, request, metadata):
        self.response_metadata = metadata
        return request, metadata

    def pre_expand(self, request, metadata):
        self.request_metadata = metadata
        return request, metadata

    def post_expand_with_metadata(self, request, metadata):
        self.response_metadata = metadata
        return request, metadata


if HAS_RESUMABLE_UPLOAD_CLIENT:
    try:
        from google.showcase_v1beta1.services.resumable_upload_service.transports import (
            ResumableUploadServiceRestInterceptor,
        )

        class ResumableUploadMetadataClientRestInterceptor(
            ResumableUploadServiceRestInterceptor
        ):
            request_metadata: Sequence[Tuple[str, str]] = []
            response_metadata: Sequence[Tuple[str, str]] = []

            def pre_upload_media(self, request, metadata):
                self.request_metadata = metadata
                return request, metadata

            def post_upload_media_with_metadata(self, request, metadata):
                self.response_metadata = metadata
                return request, metadata

        HAS_RESUMABLE_UPLOAD_INTERCEPTOR = True
    except ImportError:
        HAS_RESUMABLE_UPLOAD_INTERCEPTOR = False
else:
    HAS_RESUMABLE_UPLOAD_INTERCEPTOR = False


if HAS_ASYNC_REST_ECHO_TRANSPORT:

    class EchoMetadataClientRestAsyncInterceptor(AsyncEchoRestInterceptor):
        request_metadata: Sequence[Tuple[str, str]] = []
        response_metadata: Sequence[Tuple[str, str]] = []

        async def pre_echo(self, request, metadata):
            self.request_metadata = metadata
            return request, metadata

        async def post_echo_with_metadata(self, request, metadata):
            self.response_metadata = metadata
            return request, metadata

        async def pre_expand(self, request, metadata):
            self.request_metadata = metadata
            return request, metadata

        async def post_expand_with_metadata(self, request, metadata):
            self.response_metadata = metadata
            return request, metadata


if HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT:

    class ResumableUploadMetadataClientRestAsyncInterceptor(
        AsyncResumableUploadServiceRestInterceptor
    ):
        request_metadata: Sequence[Tuple[str, str]] = []
        response_metadata: Sequence[Tuple[str, str]] = []

        async def pre_upload_media(self, request, metadata):
            self.request_metadata = metadata
            return request, metadata


class EchoMetadataClientGrpcInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self.request_metadata = []
        self.response_metadata = []

    def _add_request_metadata(self, client_call_details):
        if client_call_details.metadata is not None:
            # https://grpc.github.io/grpc/python/glossary.html#term-metadata.
            # For sync, `ClientCallDetails.metadata` is a list.
            # Whereas for async, `ClientCallDetails.metadata` is a mapping.
            # https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Metadata
            client_call_details.metadata.append((self._key, self._value))
            self.request_metadata = client_call_details.metadata

    def _read_response_metadata_stream(self):
        # Access the metadata via the original stream object
        if hasattr(self, "_original_stream"):
            self.response_metadata = self._original_stream.trailing_metadata()

    def intercept_unary_unary(self, continuation, client_call_details, request):
        self._add_request_metadata(client_call_details)
        response = continuation(client_call_details, request)
        metadata = [(k, str(v)) for k, v in response.initial_metadata()] + [
            (k, str(v)) for k, v in response.trailing_metadata()
        ]
        self.response_metadata = metadata
        return response

    def intercept_unary_stream(self, continuation, client_call_details, request):
        self._add_request_metadata(client_call_details)
        response_it = continuation(client_call_details, request)
        self._original_stream = response_it
        return response_it

    def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        self._add_request_metadata(client_call_details)
        response = continuation(client_call_details, request_iterator)
        return response

    def intercept_stream_stream(
        self, continuation, client_call_details, request_iterator
    ):
        self._add_request_metadata(client_call_details)
        response_it = continuation(client_call_details, request_iterator)
        self._original_stream = response_it
        return response_it


class EchoMetadataClientGrpcAsyncInterceptor(
    grpc.aio.UnaryUnaryClientInterceptor,
    grpc.aio.UnaryStreamClientInterceptor,
    grpc.aio.StreamUnaryClientInterceptor,
    grpc.aio.StreamStreamClientInterceptor,
):
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self.request_metadata = []
        self.response_metadata = []

    async def _add_request_metadata(self, client_call_details):
        if client_call_details.metadata is not None:
            # As of gRPC 1.75.0 and newer,
            # https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Metadata
            # Note that for async, `ClientCallDetails.metadata` is a mapping.
            # Whereas for sync, `ClientCallDetails.metadata` is a list.
            # https://grpc.github.io/grpc/python/glossary.html#term-metadata.
            # Prior to gRPC 1.75.0, `ClientCallDetails.metadata` is a list
            # for both sync and async.
            grpc_major, grpc_minor = [
                int(part) for part in _GRPC_VERSION.split(".")[0:2]
            ]
            if grpc_major == 1 and grpc_minor < 75:
                client_call_details.metadata.append((self._key, self._value))
            else:
                client_call_details.metadata[self._key] = self._value
            self.request_metadata = list(client_call_details.metadata)

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        await self._add_request_metadata(client_call_details)
        response = await continuation(client_call_details, request)
        metadata = [(k, str(v)) for k, v in await response.initial_metadata()] + [
            (k, str(v)) for k, v in await response.trailing_metadata()
        ]
        self.response_metadata = metadata
        return response

    async def intercept_unary_stream(self, continuation, client_call_details, request):
        self._add_request_metadata(client_call_details)
        response_it = continuation(client_call_details, request)
        return response_it

    async def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        self._add_request_metadata(client_call_details)
        response = continuation(client_call_details, request_iterator)
        return response

    async def intercept_stream_stream(
        self, continuation, client_call_details, request_iterator
    ):
        self._add_request_metadata(client_call_details)
        response_it = continuation(client_call_details, request_iterator)
        return response_it


@pytest.fixture
def intercepted_echo_grpc(use_mtls, use_tls):
    # The interceptor adds 'showcase-trailer' client metadata. Showcase server
    # echoes any metadata with key 'showcase-trailer', so the same metadata
    # should appear as trailing metadata in the response.
    interceptor = EchoMetadataClientGrpcInterceptor(
        "showcase-trailer",
        "intercepted",
    )
    host = "localhost:7469"
    if use_mtls:
        channel = grpc.secure_channel(host, ssl_credentials)
    elif use_tls:
        channel = grpc.secure_channel(host, tls_credentials)
    else:
        channel = grpc.insecure_channel(host)
    intercept_channel = grpc.intercept_channel(channel, interceptor)
    transport = EchoClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials(),
        channel=intercept_channel,
    )
    return EchoClient(transport=transport), interceptor


@pytest_asyncio.fixture
async def intercepted_echo_grpc_async(use_mtls, use_tls):
    # The interceptor adds 'showcase-trailer' client metadata. Showcase server
    # echoes any metadata with key 'showcase-trailer', so the same metadata
    # should appear as trailing metadata in the response.
    interceptor = EchoMetadataClientGrpcAsyncInterceptor(
        "showcase-trailer",
        "intercepted",
    )
    host = "localhost:7469"
    if use_mtls:
        channel = grpc.aio.secure_channel(
            host, ssl_credentials, interceptors=[interceptor]
        )
    elif use_tls:
        channel = grpc.aio.secure_channel(
            host, tls_credentials, interceptors=[interceptor]
        )
    else:
        channel = grpc.aio.insecure_channel(host, interceptors=[interceptor])
    transport = EchoAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=ga_credentials.AnonymousCredentials(),
        channel=channel,
    )
    return EchoAsyncClient(transport=transport), interceptor


class HostNameIgnoringAdapter(HTTPAdapter):
    """Custom HTTPAdapter that disables hostname verification for local self-signed certs."""

    def cert_verify(self, conn, url, verify, cert):
        super().cert_verify(conn, url, verify, cert)
        conn.assert_hostname = False


@pytest.fixture
def intercepted_echo_rest(use_mtls, use_tls):
    transport_name = "rest"
    transport_cls = EchoClient.get_transport_class(transport_name)
    interceptor = EchoMetadataClientRestInterceptor()

    url_scheme = "https" if (use_mtls or use_tls) else "http"
    transport = transport_cls(
        credentials=ga_credentials.AnonymousCredentials(),
        host="localhost:7469",
        url_scheme=url_scheme,
        interceptor=interceptor,
    )
    if use_mtls or use_tls:
        transport._session.verify = CERT_PATH
        transport._session.mount("https://", HostNameIgnoringAdapter())
    if use_mtls:
        transport._session.cert = (CERT_PATH, KEY_PATH)

    return EchoClient(transport=transport), interceptor


@pytest.fixture
def intercepted_echo_rest_async():
    if not HAS_ASYNC_REST_ECHO_TRANSPORT:
        pytest.skip("Skipping test with async rest.")

    transport_name = "rest_asyncio"
    transport_cls = EchoAsyncClient.get_transport_class(transport_name)
    interceptor = EchoMetadataClientRestAsyncInterceptor()

    transport = transport_cls(
        credentials=async_anonymous_credentials(),
        host="localhost:7469",
        url_scheme="http",
        interceptor=interceptor,
    )

    return EchoAsyncClient(transport=transport), interceptor


@pytest.fixture
def intercepted_resumable_upload_rest(use_mtls, use_tls):
    if not HAS_RESUMABLE_UPLOAD_CLIENT or not HAS_RESUMABLE_UPLOAD_INTERCEPTOR:
        pytest.skip("ResumableUploadServiceClient not available.")

    transport_name = "rest"
    transport_cls = ResumableUploadServiceClient.get_transport_class(transport_name)
    interceptor = ResumableUploadMetadataClientRestInterceptor()

    url_scheme = "https" if (use_mtls or use_tls) else "http"
    transport = transport_cls(
        credentials=ga_credentials.AnonymousCredentials(),
        host="localhost:7469",
        url_scheme=url_scheme,
        interceptor=interceptor,
    )
    if use_mtls or use_tls:
        transport._session.verify = CERT_PATH
        transport._session.mount("https://", HostNameIgnoringAdapter())
    if use_mtls:
        transport._session.cert = (CERT_PATH, KEY_PATH)

    return ResumableUploadServiceClient(transport=transport), interceptor


@pytest.fixture
def intercepted_resumable_upload_rest_async():
    if not HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT:
        pytest.skip("Skipping test with async rest.")

    interceptor = ResumableUploadMetadataClientRestAsyncInterceptor()

    transport = AsyncResumableUploadServiceRestTransport(
        credentials=async_anonymous_credentials(),
        host="localhost:7469",
        url_scheme="http",
        interceptor=interceptor,
    )

    return ResumableUploadServiceAsyncClient(transport=transport), interceptor


try:
    from google.api_core.resumable_transfer import (
        ResumableUploadConfig,
        ResumableUploadSession,
    )
except ImportError:
    ResumableUploadConfig = None
    ResumableUploadSession = None


def make_resumable_upload(
    transport,
    request_body,
    stream,
    upload_url,
    size=None,
    config=None,
    **kwargs,
):
    content_type = kwargs.pop("content_type", "application/octet-stream")
    response_type = kwargs.pop("response_type", None)
    retry = kwargs.pop("retry", None)
    timeout = kwargs.pop("timeout", None)

    if config is None:
        config = ResumableUploadConfig(**kwargs)
    elif kwargs:
        for k, v in kwargs.items():
            if hasattr(config, k):
                setattr(config, k, v)

    # ``make_resumable_upload`` instantiates ``ResumableUploadSession`` directly
    # rather than calling the generated GAPIC client method (``client.upload_media``).
    # Unlike the generated GAPIC REST transport, ``ResumableUploadSession`` in
    # ``google-api-core`` is payload-format agnostic and does not set
    # ``Content-Type: application/json`` on the start request automatically.
    headers = dict(config.start_headers or [])
    if request_body and "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"
        config.headers = headers

    session = ResumableUploadSession(
        upload_url=upload_url,
        config=config,
        content_type=content_type,
        response_type=response_type,
        transport=transport,
    )
    return session.upload(
        stream=stream,
        request_body=request_body,
        content_type=content_type,
        size=size,
        transport=transport,
        retry=retry,
        timeout=timeout,
    )


def resume_resumable_upload(
    transport,
    upload_url,
    stream,
    size=None,
    config=None,
    **kwargs,
):
    content_type = kwargs.pop("content_type", None)
    response_type = kwargs.pop("response_type", None)
    retry = kwargs.pop("retry", None)
    timeout = kwargs.pop("timeout", None)

    if config is None:
        config = ResumableUploadConfig(**kwargs)
    elif kwargs:
        for k, v in kwargs.items():
            if hasattr(config, k):
                setattr(config, k, v)

    session = ResumableUploadSession(
        upload_url=upload_url,
        config=config,
        transport=transport,
        content_type=content_type,
        response_type=response_type,
    )
    return session.resume(
        upload_url=upload_url,
        stream=stream,
        size=size,
        transport=transport,
        retry=retry,
        timeout=timeout,
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Prints a Telemetry Span Compliance summary to the console.

    Enables developers to view and copy all compliance test names and
    pass/fail/error states directly from CI/console output without enabling
    verbose output for unrelated tests.
    """
    reports = (
        terminalreporter.getreports("passed")
        + terminalreporter.getreports("failed")
        + terminalreporter.getreports("skipped")
        + terminalreporter.getreports("error")
    )
    compliance_reports = [
        r
        for r in reports
        if "test_span_compliance.py" in r.nodeid
        and (r.when == "call" or r.failed or r.skipped)
    ]
    if not compliance_reports:
        return

    # Aggregate status per test nodeid so setup/call/teardown don't
    # produce duplicate lines. Priority: ERROR > FAILED > SKIPPED > PASSED
    status_by_test = {}
    for rep in compliance_reports:
        test_name = rep.nodeid.split("::")[-1]
        if rep.when != "call" and rep.failed:
            rep_status = "ERROR"
        else:
            rep_status = rep.outcome.upper()

        current = status_by_test.get(test_name)
        if current is None or rep_status in ("ERROR", "FAILED"):
            status_by_test[test_name] = rep_status

    terminalreporter.section(
        "Telemetry Span Compliance Verification", sep="=", green=True
    )
    for test_name, status in status_by_test.items():
        terminalreporter.write_line(f"[{status:6}] {test_name}")
