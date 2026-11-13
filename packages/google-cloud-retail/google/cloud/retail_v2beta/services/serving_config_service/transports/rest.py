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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.retail_v2beta._compat import transcode_request
from google.cloud.retail_v2beta.types import serving_config, serving_config_service
from google.cloud.retail_v2beta.types import serving_config as gcr_serving_config

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseServingConfigServiceRestTransport

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


class ServingConfigServiceRestInterceptor:
    """Interceptor for ServingConfigService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ServingConfigServiceRestTransport.

    .. code-block:: python
        class MyCustomServingConfigServiceInterceptor(ServingConfigServiceRestInterceptor):
            def pre_add_control(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_control(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_serving_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_serving_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_serving_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_serving_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_serving_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_serving_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_serving_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_control(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_control(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_serving_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_serving_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ServingConfigServiceRestTransport(interceptor=MyCustomServingConfigServiceInterceptor())
        client = ServingConfigServiceClient(transport=transport)


    """

    def pre_add_control(
        self,
        request: serving_config_service.AddControlRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.AddControlRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_control

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_add_control(
        self, response: gcr_serving_config.ServingConfig
    ) -> gcr_serving_config.ServingConfig:
        """Post-rpc interceptor for add_control

        DEPRECATED. Please use the `post_add_control_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code. This `post_add_control` interceptor runs
        before the `post_add_control_with_metadata` interceptor.
        """
        return response

    def post_add_control_with_metadata(
        self,
        response: gcr_serving_config.ServingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcr_serving_config.ServingConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for add_control

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServingConfigService server but before it is returned to user code.

        We recommend only using this `post_add_control_with_metadata`
        interceptor in new development instead of the `post_add_control` interceptor.
        When both interceptors are used, this `post_add_control_with_metadata` interceptor runs after the
        `post_add_control` interceptor. The (possibly modified) response returned by
        `post_add_control` will be passed to
        `post_add_control_with_metadata`.
        """
        return response, metadata

    def pre_create_serving_config(
        self,
        request: serving_config_service.CreateServingConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.CreateServingConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_serving_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_create_serving_config(
        self, response: gcr_serving_config.ServingConfig
    ) -> gcr_serving_config.ServingConfig:
        """Post-rpc interceptor for create_serving_config

        DEPRECATED. Please use the `post_create_serving_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code. This `post_create_serving_config` interceptor runs
        before the `post_create_serving_config_with_metadata` interceptor.
        """
        return response

    def post_create_serving_config_with_metadata(
        self,
        response: gcr_serving_config.ServingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcr_serving_config.ServingConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_serving_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServingConfigService server but before it is returned to user code.

        We recommend only using this `post_create_serving_config_with_metadata`
        interceptor in new development instead of the `post_create_serving_config` interceptor.
        When both interceptors are used, this `post_create_serving_config_with_metadata` interceptor runs after the
        `post_create_serving_config` interceptor. The (possibly modified) response returned by
        `post_create_serving_config` will be passed to
        `post_create_serving_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_serving_config(
        self,
        request: serving_config_service.DeleteServingConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.DeleteServingConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_serving_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def pre_get_serving_config(
        self,
        request: serving_config_service.GetServingConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.GetServingConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_serving_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_get_serving_config(
        self, response: serving_config.ServingConfig
    ) -> serving_config.ServingConfig:
        """Post-rpc interceptor for get_serving_config

        DEPRECATED. Please use the `post_get_serving_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code. This `post_get_serving_config` interceptor runs
        before the `post_get_serving_config_with_metadata` interceptor.
        """
        return response

    def post_get_serving_config_with_metadata(
        self,
        response: serving_config.ServingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[serving_config.ServingConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_serving_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServingConfigService server but before it is returned to user code.

        We recommend only using this `post_get_serving_config_with_metadata`
        interceptor in new development instead of the `post_get_serving_config` interceptor.
        When both interceptors are used, this `post_get_serving_config_with_metadata` interceptor runs after the
        `post_get_serving_config` interceptor. The (possibly modified) response returned by
        `post_get_serving_config` will be passed to
        `post_get_serving_config_with_metadata`.
        """
        return response, metadata

    def pre_list_serving_configs(
        self,
        request: serving_config_service.ListServingConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.ListServingConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_serving_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_list_serving_configs(
        self, response: serving_config_service.ListServingConfigsResponse
    ) -> serving_config_service.ListServingConfigsResponse:
        """Post-rpc interceptor for list_serving_configs

        DEPRECATED. Please use the `post_list_serving_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code. This `post_list_serving_configs` interceptor runs
        before the `post_list_serving_configs_with_metadata` interceptor.
        """
        return response

    def post_list_serving_configs_with_metadata(
        self,
        response: serving_config_service.ListServingConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.ListServingConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_serving_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServingConfigService server but before it is returned to user code.

        We recommend only using this `post_list_serving_configs_with_metadata`
        interceptor in new development instead of the `post_list_serving_configs` interceptor.
        When both interceptors are used, this `post_list_serving_configs_with_metadata` interceptor runs after the
        `post_list_serving_configs` interceptor. The (possibly modified) response returned by
        `post_list_serving_configs` will be passed to
        `post_list_serving_configs_with_metadata`.
        """
        return response, metadata

    def pre_remove_control(
        self,
        request: serving_config_service.RemoveControlRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.RemoveControlRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_control

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_remove_control(
        self, response: gcr_serving_config.ServingConfig
    ) -> gcr_serving_config.ServingConfig:
        """Post-rpc interceptor for remove_control

        DEPRECATED. Please use the `post_remove_control_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code. This `post_remove_control` interceptor runs
        before the `post_remove_control_with_metadata` interceptor.
        """
        return response

    def post_remove_control_with_metadata(
        self,
        response: gcr_serving_config.ServingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcr_serving_config.ServingConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for remove_control

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServingConfigService server but before it is returned to user code.

        We recommend only using this `post_remove_control_with_metadata`
        interceptor in new development instead of the `post_remove_control` interceptor.
        When both interceptors are used, this `post_remove_control_with_metadata` interceptor runs after the
        `post_remove_control` interceptor. The (possibly modified) response returned by
        `post_remove_control` will be passed to
        `post_remove_control_with_metadata`.
        """
        return response, metadata

    def pre_update_serving_config(
        self,
        request: serving_config_service.UpdateServingConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        serving_config_service.UpdateServingConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_serving_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_update_serving_config(
        self, response: gcr_serving_config.ServingConfig
    ) -> gcr_serving_config.ServingConfig:
        """Post-rpc interceptor for update_serving_config

        DEPRECATED. Please use the `post_update_serving_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code. This `post_update_serving_config` interceptor runs
        before the `post_update_serving_config_with_metadata` interceptor.
        """
        return response

    def post_update_serving_config_with_metadata(
        self,
        response: gcr_serving_config.ServingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcr_serving_config.ServingConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_serving_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServingConfigService server but before it is returned to user code.

        We recommend only using this `post_update_serving_config_with_metadata`
        interceptor in new development instead of the `post_update_serving_config` interceptor.
        When both interceptors are used, this `post_update_serving_config_with_metadata` interceptor runs after the
        `post_update_serving_config` interceptor. The (possibly modified) response returned by
        `post_update_serving_config` will be passed to
        `post_update_serving_config_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServingConfigService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ServingConfigService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ServingConfigServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ServingConfigServiceRestInterceptor


class ServingConfigServiceRestTransport(_BaseServingConfigServiceRestTransport):
    """REST backend synchronous transport for ServingConfigService.

    Service for modifying ServingConfig.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ServingConfigServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'retail.googleapis.com').
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
            interceptor (Optional[ServingConfigServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ServingConfigServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AddControl(
        _BaseServingConfigServiceRestTransport._BaseAddControl,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.AddControl")

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
            request: serving_config_service.AddControlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_serving_config.ServingConfig:
            r"""Call the add control method over HTTP.

            Args:
                request (~.serving_config_service.AddControlRequest):
                    The request object. Request for AddControl method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_serving_config.ServingConfig:
                    Configures metadata that is used to
                generate serving time results (e.g.
                search results or recommendation
                predictions).

            """

            http_options = _BaseServingConfigServiceRestTransport._BaseAddControl._get_http_options()
            request, metadata = self._interceptor.pre_add_control(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseAddControl,
                    "_BaseAddControl__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.AddControl",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "AddControl",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServingConfigServiceRestTransport._AddControl._get_response(
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
            resp = gcr_serving_config.ServingConfig()
            pb_resp = gcr_serving_config.ServingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_control(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_control_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_serving_config.ServingConfig.to_json(
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
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceClient.add_control",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "AddControl",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateServingConfig(
        _BaseServingConfigServiceRestTransport._BaseCreateServingConfig,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.CreateServingConfig")

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
            request: serving_config_service.CreateServingConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_serving_config.ServingConfig:
            r"""Call the create serving config method over HTTP.

            Args:
                request (~.serving_config_service.CreateServingConfigRequest):
                    The request object. Request for CreateServingConfig
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_serving_config.ServingConfig:
                    Configures metadata that is used to
                generate serving time results (e.g.
                search results or recommendation
                predictions).

            """

            http_options = _BaseServingConfigServiceRestTransport._BaseCreateServingConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_serving_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseCreateServingConfig,
                    "_BaseCreateServingConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.CreateServingConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "CreateServingConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ServingConfigServiceRestTransport._CreateServingConfig._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gcr_serving_config.ServingConfig()
            pb_resp = gcr_serving_config.ServingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_serving_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_serving_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_serving_config.ServingConfig.to_json(
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
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceClient.create_serving_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "CreateServingConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteServingConfig(
        _BaseServingConfigServiceRestTransport._BaseDeleteServingConfig,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.DeleteServingConfig")

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
            request: serving_config_service.DeleteServingConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete serving config method over HTTP.

            Args:
                request (~.serving_config_service.DeleteServingConfigRequest):
                    The request object. Request for DeleteServingConfig
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseServingConfigServiceRestTransport._BaseDeleteServingConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_serving_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseDeleteServingConfig,
                    "_BaseDeleteServingConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.DeleteServingConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "DeleteServingConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ServingConfigServiceRestTransport._DeleteServingConfig._get_response(
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

    class _GetServingConfig(
        _BaseServingConfigServiceRestTransport._BaseGetServingConfig,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.GetServingConfig")

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
            request: serving_config_service.GetServingConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> serving_config.ServingConfig:
            r"""Call the get serving config method over HTTP.

            Args:
                request (~.serving_config_service.GetServingConfigRequest):
                    The request object. Request for GetServingConfig method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.serving_config.ServingConfig:
                    Configures metadata that is used to
                generate serving time results (e.g.
                search results or recommendation
                predictions).

            """

            http_options = _BaseServingConfigServiceRestTransport._BaseGetServingConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_serving_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseGetServingConfig,
                    "_BaseGetServingConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.GetServingConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "GetServingConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ServingConfigServiceRestTransport._GetServingConfig._get_response(
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
            resp = serving_config.ServingConfig()
            pb_resp = serving_config.ServingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_serving_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_serving_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = serving_config.ServingConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceClient.get_serving_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "GetServingConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServingConfigs(
        _BaseServingConfigServiceRestTransport._BaseListServingConfigs,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.ListServingConfigs")

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
            request: serving_config_service.ListServingConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> serving_config_service.ListServingConfigsResponse:
            r"""Call the list serving configs method over HTTP.

            Args:
                request (~.serving_config_service.ListServingConfigsRequest):
                    The request object. Request for ListServingConfigs
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.serving_config_service.ListServingConfigsResponse:
                    Response for ListServingConfigs
                method.

            """

            http_options = _BaseServingConfigServiceRestTransport._BaseListServingConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_serving_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseListServingConfigs,
                    "_BaseListServingConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.ListServingConfigs",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "ListServingConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ServingConfigServiceRestTransport._ListServingConfigs._get_response(
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
            resp = serving_config_service.ListServingConfigsResponse()
            pb_resp = serving_config_service.ListServingConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_serving_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_serving_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        serving_config_service.ListServingConfigsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceClient.list_serving_configs",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "ListServingConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveControl(
        _BaseServingConfigServiceRestTransport._BaseRemoveControl,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.RemoveControl")

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
            request: serving_config_service.RemoveControlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_serving_config.ServingConfig:
            r"""Call the remove control method over HTTP.

            Args:
                request (~.serving_config_service.RemoveControlRequest):
                    The request object. Request for RemoveControl method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_serving_config.ServingConfig:
                    Configures metadata that is used to
                generate serving time results (e.g.
                search results or recommendation
                predictions).

            """

            http_options = _BaseServingConfigServiceRestTransport._BaseRemoveControl._get_http_options()
            request, metadata = self._interceptor.pre_remove_control(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseRemoveControl,
                    "_BaseRemoveControl__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.RemoveControl",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "RemoveControl",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServingConfigServiceRestTransport._RemoveControl._get_response(
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
            resp = gcr_serving_config.ServingConfig()
            pb_resp = gcr_serving_config.ServingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_control(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_control_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_serving_config.ServingConfig.to_json(
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
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceClient.remove_control",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "RemoveControl",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateServingConfig(
        _BaseServingConfigServiceRestTransport._BaseUpdateServingConfig,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.UpdateServingConfig")

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
            request: serving_config_service.UpdateServingConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_serving_config.ServingConfig:
            r"""Call the update serving config method over HTTP.

            Args:
                request (~.serving_config_service.UpdateServingConfigRequest):
                    The request object. Request for UpdateServingConfig
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_serving_config.ServingConfig:
                    Configures metadata that is used to
                generate serving time results (e.g.
                search results or recommendation
                predictions).

            """

            http_options = _BaseServingConfigServiceRestTransport._BaseUpdateServingConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_serving_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseUpdateServingConfig,
                    "_BaseUpdateServingConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.UpdateServingConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "UpdateServingConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ServingConfigServiceRestTransport._UpdateServingConfig._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gcr_serving_config.ServingConfig()
            pb_resp = gcr_serving_config.ServingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_serving_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_serving_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_serving_config.ServingConfig.to_json(
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
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceClient.update_serving_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "UpdateServingConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_control(
        self,
    ) -> Callable[
        [serving_config_service.AddControlRequest], gcr_serving_config.ServingConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddControl(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.CreateServingConfigRequest],
        gcr_serving_config.ServingConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateServingConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_serving_config(
        self,
    ) -> Callable[[serving_config_service.DeleteServingConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteServingConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.GetServingConfigRequest], serving_config.ServingConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetServingConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_serving_configs(
        self,
    ) -> Callable[
        [serving_config_service.ListServingConfigsRequest],
        serving_config_service.ListServingConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServingConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_control(
        self,
    ) -> Callable[
        [serving_config_service.RemoveControlRequest], gcr_serving_config.ServingConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveControl(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.UpdateServingConfigRequest],
        gcr_serving_config.ServingConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateServingConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseServingConfigServiceRestTransport._BaseGetOperation,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.GetOperation")

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

            http_options = _BaseServingConfigServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServingConfigServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseServingConfigServiceRestTransport._BaseListOperations,
        ServingConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("ServingConfigServiceRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseServingConfigServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServingConfigServiceRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.ServingConfigServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServingConfigServiceRestTransport._ListOperations._get_response(
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
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
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
                    "Received response for google.cloud.retail_v2beta.ServingConfigServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.ServingConfigService",
                        "rpcName": "ListOperations",
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


__all__ = ("ServingConfigServiceRestTransport",)
