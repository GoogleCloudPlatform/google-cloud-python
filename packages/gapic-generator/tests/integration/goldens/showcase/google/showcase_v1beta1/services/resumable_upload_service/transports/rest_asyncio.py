# -*- coding: utf-8 -*-
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

import google.auth
try:
    import aiohttp # type: ignore
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession # type: ignore
    from google.api_core import rest_streaming_async # type: ignore
    from google.api_core.operations_v1 import AsyncOperationsRestClient # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError("`rest_asyncio` transport requires the library to be installed with the `async_rest` extra. Install the library with the `async_rest` extra using `pip install google-showcase[async_rest]`") from e

from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.aio import credentials as ga_credentials_async  # type: ignore

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core.client_options import ClientOptions
import urllib.parse
from google.api_core import resumable_transfer
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore
from google.api_core import retry_async as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async  # type: ignore
from google.showcase_v1beta1._compat import transcode_request, trace_http_request

import google.protobuf

from google.protobuf import json_format
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore

import json  # type: ignore
import dataclasses
from typing import Any, Dict, List, Callable, Tuple, Optional, Sequence, Union


from google.showcase_v1beta1.types import resumable_upload
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseResumableUploadServiceRestTransport

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


import logging

try:
    from google.api_core import client_logging  # type: ignore
    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"google-auth@{google.auth.__version__}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AsyncResumableUploadServiceRestInterceptor:
    """Asynchronous Interceptor for ResumableUploadService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AsyncResumableUploadServiceRestTransport.

    .. code-block:: python
        class MyCustomResumableUploadServiceInterceptor(ResumableUploadServiceRestInterceptor):
            async def pre_upload_media(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

        transport = AsyncResumableUploadServiceRestTransport(interceptor=MyCustomResumableUploadServiceInterceptor())
        client = async ResumableUploadServiceClient(transport=transport)


    """
    async def pre_upload_media(self, request: resumable_upload.UploadMediaRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[resumable_upload.UploadMediaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for upload_media

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ResumableUploadService server.
        """
        return request, metadata


@dataclasses.dataclass
class AsyncResumableUploadServiceRestStub:
    _session: AsyncAuthorizedSession
    _host: str
    _interceptor: AsyncResumableUploadServiceRestInterceptor
    _client_options: Optional[ClientOptions] = None

class AsyncResumableUploadServiceRestTransport(_BaseResumableUploadServiceRestTransport):
    """Asynchronous REST backend transport for ResumableUploadService.

    A service showcasing universal resumable upload protocol
    support.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    def __init__(self,
            *,
            host: str = 'localhost:7469',
            credentials: Optional[Union[ga_credentials.Credentials, ga_credentials_async.Credentials]] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            url_scheme: str = 'https',
            interceptor: Optional[AsyncResumableUploadServiceRestInterceptor] = None,
            client_options: Optional[ClientOptions] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
            credentials (Optional[Union[google.auth.credentials.Credentials, google.auth.aio.credentials.Credentials]]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            url_scheme (str): the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[AsyncResumableUploadServiceRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            client_options (Optional[google.api_core.client_options.ClientOptions]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
        """
        # Run the base constructor
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=False,
            url_scheme=url_scheme,
            api_audience=None,
            client_options=client_options,
            **kwargs,
        )
        self._session = AsyncAuthorizedSession(self._credentials)  # type: ignore
        self._interceptor = interceptor or AsyncResumableUploadServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for async RPC dispatch.

        Overrides the base class method to use asynchronous wrappers and retries.
        """
        self._wrapped_methods = {
            self.upload_media: self._wrap_async_method(
                self.upload_media,
                default_timeout=None,
                client_info=client_info,
                method_name="google.showcase.v1beta1.ResumableUploadService/UploadMedia",
            ),
        }

    class _UploadMedia(_BaseResumableUploadServiceRestTransport._BaseUploadMedia, AsyncResumableUploadServiceRestStub):
        def __hash__(self):
            return hash("AsyncResumableUploadServiceRestTransport.UploadMedia")

        async def __call__(self,
                    request: resumable_upload.UploadMediaRequest, *,
                    config: Optional[resumable_transfer.ResumableUploadConfig]=None,
                    start_retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> resumable_transfer.AsyncResumableUploadSession:
            r"""Call the upload media method over HTTP.

            Args:
                request (~.resumable_upload.UploadMediaRequest):
                    The request object.
                config (Optional[google.api_core.resumable_transfer.ResumableUploadConfig]):
                    Optional configuration for the resumable upload session.
                start_retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried when initiating the resumable upload session.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resumable_transfer.AsyncResumableUploadSession:
                    An object representing a resumable
                upload session.

            """
            http_options = _BaseResumableUploadServiceRestTransport._BaseUploadMedia._get_http_options()
            request, metadata = await self._interceptor.pre_upload_media(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseResumableUploadServiceRestTransport._BaseUploadMedia,
                    "_BaseUploadMedia__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            uri = transcoded_request["uri"]
            params = rest_helpers.flatten_query_params(query_params, strict=True)
            query_string = f"?{urllib.parse.urlencode(params)}" if params else ""
            upload_url = f"{self._host}{uri}{query_string}"
            headers: Dict[str, Any] = {**dict(metadata), **dict((config.headers or {}) if config else {})}
            headers["Content-Type"] = "application/json"
            if config is None:
                config = resumable_transfer.ResumableUploadConfig(headers=headers)
            else:
                config = dataclasses.replace(config, headers=headers)

            session_kwargs: Dict[str, Any] = (
                {"start_timeout": timeout}
                if isinstance(timeout, (int, float))
                else {}
            )
            # ``start_retry`` is used instead of ``retry`` because ``_GapicCallable``
            # consumes the ``retry`` argument before invoking the transport callable
            # and only forwards extra keyword arguments such as ``start_retry``.
            return resumable_transfer.AsyncResumableUploadSession(
                upload_url=upload_url,
                config=config,
                transport=self._session,
                response_type=resumable_upload.UploadMediaResponse,
                start_retry=start_retry if isinstance(start_retry, retries.AsyncRetry) else None,
                request_body=body,
                **session_kwargs,
            )

    @property
    def upload_media(self) -> Callable[
            [resumable_upload.UploadMediaRequest],
            resumable_transfer.AsyncResumableUploadSession]:
        return self._UploadMedia(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()
