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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import (
    cms_metadata_value_messages,
    cms_metadata_value_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCmsMetadataValueServiceRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class CmsMetadataValueServiceRestInterceptor:
    """Interceptor for CmsMetadataValueService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CmsMetadataValueServiceRestTransport.

    .. code-block:: python
        class MyCustomCmsMetadataValueServiceInterceptor(CmsMetadataValueServiceRestInterceptor):
            def pre_batch_activate_cms_metadata_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_cms_metadata_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_cms_metadata_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_cms_metadata_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cms_metadata_value(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cms_metadata_value(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_cms_metadata_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_cms_metadata_values(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CmsMetadataValueServiceRestTransport(interceptor=MyCustomCmsMetadataValueServiceInterceptor())
        client = CmsMetadataValueServiceClient(transport=transport)


    """

    def pre_batch_activate_cms_metadata_values(
        self,
        request: cms_metadata_value_service.BatchActivateCmsMetadataValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.BatchActivateCmsMetadataValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_cms_metadata_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CmsMetadataValueService server.
        """
        return request, metadata

    def post_batch_activate_cms_metadata_values(
        self,
        response: cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse,
    ) -> cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse:
        """Post-rpc interceptor for batch_activate_cms_metadata_values

        DEPRECATED. Please use the `post_batch_activate_cms_metadata_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CmsMetadataValueService server but before
        it is returned to user code. This `post_batch_activate_cms_metadata_values` interceptor runs
        before the `post_batch_activate_cms_metadata_values_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_cms_metadata_values_with_metadata(
        self,
        response: cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_cms_metadata_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CmsMetadataValueService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_cms_metadata_values_with_metadata`
        interceptor in new development instead of the `post_batch_activate_cms_metadata_values` interceptor.
        When both interceptors are used, this `post_batch_activate_cms_metadata_values_with_metadata` interceptor runs after the
        `post_batch_activate_cms_metadata_values` interceptor. The (possibly modified) response returned by
        `post_batch_activate_cms_metadata_values` will be passed to
        `post_batch_activate_cms_metadata_values_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_cms_metadata_values(
        self,
        request: cms_metadata_value_service.BatchDeactivateCmsMetadataValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.BatchDeactivateCmsMetadataValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_cms_metadata_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CmsMetadataValueService server.
        """
        return request, metadata

    def post_batch_deactivate_cms_metadata_values(
        self,
        response: cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse,
    ) -> cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse:
        """Post-rpc interceptor for batch_deactivate_cms_metadata_values

        DEPRECATED. Please use the `post_batch_deactivate_cms_metadata_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CmsMetadataValueService server but before
        it is returned to user code. This `post_batch_deactivate_cms_metadata_values` interceptor runs
        before the `post_batch_deactivate_cms_metadata_values_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_cms_metadata_values_with_metadata(
        self,
        response: cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_cms_metadata_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CmsMetadataValueService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_cms_metadata_values_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_cms_metadata_values` interceptor.
        When both interceptors are used, this `post_batch_deactivate_cms_metadata_values_with_metadata` interceptor runs after the
        `post_batch_deactivate_cms_metadata_values` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_cms_metadata_values` will be passed to
        `post_batch_deactivate_cms_metadata_values_with_metadata`.
        """
        return response, metadata

    def pre_get_cms_metadata_value(
        self,
        request: cms_metadata_value_service.GetCmsMetadataValueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.GetCmsMetadataValueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_cms_metadata_value

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CmsMetadataValueService server.
        """
        return request, metadata

    def post_get_cms_metadata_value(
        self, response: cms_metadata_value_messages.CmsMetadataValue
    ) -> cms_metadata_value_messages.CmsMetadataValue:
        """Post-rpc interceptor for get_cms_metadata_value

        DEPRECATED. Please use the `post_get_cms_metadata_value_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CmsMetadataValueService server but before
        it is returned to user code. This `post_get_cms_metadata_value` interceptor runs
        before the `post_get_cms_metadata_value_with_metadata` interceptor.
        """
        return response

    def post_get_cms_metadata_value_with_metadata(
        self,
        response: cms_metadata_value_messages.CmsMetadataValue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_messages.CmsMetadataValue,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_cms_metadata_value

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CmsMetadataValueService server but before it is returned to user code.

        We recommend only using this `post_get_cms_metadata_value_with_metadata`
        interceptor in new development instead of the `post_get_cms_metadata_value` interceptor.
        When both interceptors are used, this `post_get_cms_metadata_value_with_metadata` interceptor runs after the
        `post_get_cms_metadata_value` interceptor. The (possibly modified) response returned by
        `post_get_cms_metadata_value` will be passed to
        `post_get_cms_metadata_value_with_metadata`.
        """
        return response, metadata

    def pre_list_cms_metadata_values(
        self,
        request: cms_metadata_value_service.ListCmsMetadataValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.ListCmsMetadataValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_cms_metadata_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CmsMetadataValueService server.
        """
        return request, metadata

    def post_list_cms_metadata_values(
        self, response: cms_metadata_value_service.ListCmsMetadataValuesResponse
    ) -> cms_metadata_value_service.ListCmsMetadataValuesResponse:
        """Post-rpc interceptor for list_cms_metadata_values

        DEPRECATED. Please use the `post_list_cms_metadata_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CmsMetadataValueService server but before
        it is returned to user code. This `post_list_cms_metadata_values` interceptor runs
        before the `post_list_cms_metadata_values_with_metadata` interceptor.
        """
        return response

    def post_list_cms_metadata_values_with_metadata(
        self,
        response: cms_metadata_value_service.ListCmsMetadataValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cms_metadata_value_service.ListCmsMetadataValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_cms_metadata_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CmsMetadataValueService server but before it is returned to user code.

        We recommend only using this `post_list_cms_metadata_values_with_metadata`
        interceptor in new development instead of the `post_list_cms_metadata_values` interceptor.
        When both interceptors are used, this `post_list_cms_metadata_values_with_metadata` interceptor runs after the
        `post_list_cms_metadata_values` interceptor. The (possibly modified) response returned by
        `post_list_cms_metadata_values` will be passed to
        `post_list_cms_metadata_values_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CmsMetadataValueService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CmsMetadataValueService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CmsMetadataValueService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CmsMetadataValueService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CmsMetadataValueServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CmsMetadataValueServiceRestInterceptor


class CmsMetadataValueServiceRestTransport(_BaseCmsMetadataValueServiceRestTransport):
    """REST backend synchronous transport for CmsMetadataValueService.

    Provides methods for handling ``CmsMetadataValue`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CmsMetadataValueServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'admanager.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[CmsMetadataValueServiceRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or CmsMetadataValueServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCmsMetadataValues(
        _BaseCmsMetadataValueServiceRestTransport._BaseBatchActivateCmsMetadataValues,
        CmsMetadataValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CmsMetadataValueServiceRestTransport.BatchActivateCmsMetadataValues"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: cms_metadata_value_service.BatchActivateCmsMetadataValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse:
            r"""Call the batch activate cms
            metadata values method over HTTP.

                Args:
                    request (~.cms_metadata_value_service.BatchActivateCmsMetadataValuesRequest):
                        The request object. Request object for ``BatchActivateCmsMetadataValues``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse:
                        Response object for ``BatchActivateCmsMetadataValues``
                    method.

            """

            http_options = _BaseCmsMetadataValueServiceRestTransport._BaseBatchActivateCmsMetadataValues._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_activate_cms_metadata_values(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCmsMetadataValueServiceRestTransport._BaseBatchActivateCmsMetadataValues,
                    "_BaseBatchActivateCmsMetadataValues__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.CmsMetadataValueServiceClient.BatchActivateCmsMetadataValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "BatchActivateCmsMetadataValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CmsMetadataValueServiceRestTransport._BatchActivateCmsMetadataValues._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse()
            pb_resp = (
                cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_cms_metadata_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_cms_metadata_values_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CmsMetadataValueServiceClient.batch_activate_cms_metadata_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "BatchActivateCmsMetadataValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateCmsMetadataValues(
        _BaseCmsMetadataValueServiceRestTransport._BaseBatchDeactivateCmsMetadataValues,
        CmsMetadataValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CmsMetadataValueServiceRestTransport.BatchDeactivateCmsMetadataValues"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: cms_metadata_value_service.BatchDeactivateCmsMetadataValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse:
            r"""Call the batch deactivate cms
            metadata values method over HTTP.

                Args:
                    request (~.cms_metadata_value_service.BatchDeactivateCmsMetadataValuesRequest):
                        The request object. Request object for ``BatchDeactivateCmsMetadataValues``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse:
                        Response object for ``BatchDeactivateCmsMetadataValues``
                    method.

            """

            http_options = _BaseCmsMetadataValueServiceRestTransport._BaseBatchDeactivateCmsMetadataValues._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_cms_metadata_values(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCmsMetadataValueServiceRestTransport._BaseBatchDeactivateCmsMetadataValues,
                    "_BaseBatchDeactivateCmsMetadataValues__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.CmsMetadataValueServiceClient.BatchDeactivateCmsMetadataValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "BatchDeactivateCmsMetadataValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CmsMetadataValueServiceRestTransport._BatchDeactivateCmsMetadataValues._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse()
            pb_resp = (
                cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_cms_metadata_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_cms_metadata_values_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CmsMetadataValueServiceClient.batch_deactivate_cms_metadata_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "BatchDeactivateCmsMetadataValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCmsMetadataValue(
        _BaseCmsMetadataValueServiceRestTransport._BaseGetCmsMetadataValue,
        CmsMetadataValueServiceRestStub,
    ):
        def __hash__(self):
            return hash("CmsMetadataValueServiceRestTransport.GetCmsMetadataValue")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: cms_metadata_value_service.GetCmsMetadataValueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cms_metadata_value_messages.CmsMetadataValue:
            r"""Call the get cms metadata value method over HTTP.

            Args:
                request (~.cms_metadata_value_service.GetCmsMetadataValueRequest):
                    The request object. Request object for ``GetCmsMetadataValue`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cms_metadata_value_messages.CmsMetadataValue:
                    Key value pair associated with a
                piece of content from a publisher's CMS.

            """

            http_options = _BaseCmsMetadataValueServiceRestTransport._BaseGetCmsMetadataValue._get_http_options()
            request, metadata = self._interceptor.pre_get_cms_metadata_value(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCmsMetadataValueServiceRestTransport._BaseGetCmsMetadataValue,
                    "_BaseGetCmsMetadataValue__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.CmsMetadataValueServiceClient.GetCmsMetadataValue",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "GetCmsMetadataValue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CmsMetadataValueServiceRestTransport._GetCmsMetadataValue._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = cms_metadata_value_messages.CmsMetadataValue()
            pb_resp = cms_metadata_value_messages.CmsMetadataValue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_cms_metadata_value(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_cms_metadata_value_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cms_metadata_value_messages.CmsMetadataValue.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CmsMetadataValueServiceClient.get_cms_metadata_value",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "GetCmsMetadataValue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCmsMetadataValues(
        _BaseCmsMetadataValueServiceRestTransport._BaseListCmsMetadataValues,
        CmsMetadataValueServiceRestStub,
    ):
        def __hash__(self):
            return hash("CmsMetadataValueServiceRestTransport.ListCmsMetadataValues")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: cms_metadata_value_service.ListCmsMetadataValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cms_metadata_value_service.ListCmsMetadataValuesResponse:
            r"""Call the list cms metadata values method over HTTP.

            Args:
                request (~.cms_metadata_value_service.ListCmsMetadataValuesRequest):
                    The request object. Request object for ``ListCmsMetadataValues`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cms_metadata_value_service.ListCmsMetadataValuesResponse:
                    Response object for ``ListCmsMetadataValuesRequest``
                containing matching ``CmsMetadataValue`` objects.

            """

            http_options = _BaseCmsMetadataValueServiceRestTransport._BaseListCmsMetadataValues._get_http_options()
            request, metadata = self._interceptor.pre_list_cms_metadata_values(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCmsMetadataValueServiceRestTransport._BaseListCmsMetadataValues,
                    "_BaseListCmsMetadataValues__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.CmsMetadataValueServiceClient.ListCmsMetadataValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "ListCmsMetadataValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CmsMetadataValueServiceRestTransport._ListCmsMetadataValues._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = cms_metadata_value_service.ListCmsMetadataValuesResponse()
            pb_resp = cms_metadata_value_service.ListCmsMetadataValuesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_cms_metadata_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_cms_metadata_values_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cms_metadata_value_service.ListCmsMetadataValuesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CmsMetadataValueServiceClient.list_cms_metadata_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "ListCmsMetadataValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_cms_metadata_values(
        self,
    ) -> Callable[
        [cms_metadata_value_service.BatchActivateCmsMetadataValuesRequest],
        cms_metadata_value_service.BatchActivateCmsMetadataValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCmsMetadataValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_cms_metadata_values(
        self,
    ) -> Callable[
        [cms_metadata_value_service.BatchDeactivateCmsMetadataValuesRequest],
        cms_metadata_value_service.BatchDeactivateCmsMetadataValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateCmsMetadataValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_cms_metadata_value(
        self,
    ) -> Callable[
        [cms_metadata_value_service.GetCmsMetadataValueRequest],
        cms_metadata_value_messages.CmsMetadataValue,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCmsMetadataValue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_cms_metadata_values(
        self,
    ) -> Callable[
        [cms_metadata_value_service.ListCmsMetadataValuesRequest],
        cms_metadata_value_service.ListCmsMetadataValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCmsMetadataValues(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCmsMetadataValueServiceRestTransport._BaseCancelOperation,
        CmsMetadataValueServiceRestStub,
    ):
        def __hash__(self):
            return hash("CmsMetadataValueServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCmsMetadataValueServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCmsMetadataValueServiceRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.CmsMetadataValueServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CmsMetadataValueServiceRestTransport._CancelOperation._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCmsMetadataValueServiceRestTransport._BaseGetOperation,
        CmsMetadataValueServiceRestStub,
    ):
        def __hash__(self):
            return hash("CmsMetadataValueServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseCmsMetadataValueServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCmsMetadataValueServiceRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.CmsMetadataValueServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CmsMetadataValueServiceRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CmsMetadataValueServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CmsMetadataValueService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("CmsMetadataValueServiceRestTransport",)
