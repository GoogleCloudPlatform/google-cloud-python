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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.discoveryengine_v1beta._compat import transcode_request
from google.cloud.discoveryengine_v1beta.types import (
    license_config,
    license_config_service,
)
from google.cloud.discoveryengine_v1beta.types import (
    license_config as gcd_license_config,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLicenseConfigServiceRestTransport

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


class LicenseConfigServiceRestInterceptor:
    """Interceptor for LicenseConfigService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LicenseConfigServiceRestTransport.

    .. code-block:: python
        class MyCustomLicenseConfigServiceInterceptor(LicenseConfigServiceRestInterceptor):
            def pre_create_license_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_license_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_distribute_license_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_distribute_license_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_license_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_license_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_license_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_license_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retract_license_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retract_license_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_license_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_license_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LicenseConfigServiceRestTransport(interceptor=MyCustomLicenseConfigServiceInterceptor())
        client = LicenseConfigServiceClient(transport=transport)


    """

    def pre_create_license_config(
        self,
        request: license_config_service.CreateLicenseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.CreateLicenseConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_license_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_create_license_config(
        self, response: gcd_license_config.LicenseConfig
    ) -> gcd_license_config.LicenseConfig:
        """Post-rpc interceptor for create_license_config

        DEPRECATED. Please use the `post_create_license_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code. This `post_create_license_config` interceptor runs
        before the `post_create_license_config_with_metadata` interceptor.
        """
        return response

    def post_create_license_config_with_metadata(
        self,
        response: gcd_license_config.LicenseConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_license_config.LicenseConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_license_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseConfigService server but before it is returned to user code.

        We recommend only using this `post_create_license_config_with_metadata`
        interceptor in new development instead of the `post_create_license_config` interceptor.
        When both interceptors are used, this `post_create_license_config_with_metadata` interceptor runs after the
        `post_create_license_config` interceptor. The (possibly modified) response returned by
        `post_create_license_config` will be passed to
        `post_create_license_config_with_metadata`.
        """
        return response, metadata

    def pre_distribute_license_config(
        self,
        request: license_config_service.DistributeLicenseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.DistributeLicenseConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for distribute_license_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_distribute_license_config(
        self, response: license_config_service.DistributeLicenseConfigResponse
    ) -> license_config_service.DistributeLicenseConfigResponse:
        """Post-rpc interceptor for distribute_license_config

        DEPRECATED. Please use the `post_distribute_license_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code. This `post_distribute_license_config` interceptor runs
        before the `post_distribute_license_config_with_metadata` interceptor.
        """
        return response

    def post_distribute_license_config_with_metadata(
        self,
        response: license_config_service.DistributeLicenseConfigResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.DistributeLicenseConfigResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for distribute_license_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseConfigService server but before it is returned to user code.

        We recommend only using this `post_distribute_license_config_with_metadata`
        interceptor in new development instead of the `post_distribute_license_config` interceptor.
        When both interceptors are used, this `post_distribute_license_config_with_metadata` interceptor runs after the
        `post_distribute_license_config` interceptor. The (possibly modified) response returned by
        `post_distribute_license_config` will be passed to
        `post_distribute_license_config_with_metadata`.
        """
        return response, metadata

    def pre_get_license_config(
        self,
        request: license_config_service.GetLicenseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.GetLicenseConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_license_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_get_license_config(
        self, response: license_config.LicenseConfig
    ) -> license_config.LicenseConfig:
        """Post-rpc interceptor for get_license_config

        DEPRECATED. Please use the `post_get_license_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code. This `post_get_license_config` interceptor runs
        before the `post_get_license_config_with_metadata` interceptor.
        """
        return response

    def post_get_license_config_with_metadata(
        self,
        response: license_config.LicenseConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[license_config.LicenseConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_license_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseConfigService server but before it is returned to user code.

        We recommend only using this `post_get_license_config_with_metadata`
        interceptor in new development instead of the `post_get_license_config` interceptor.
        When both interceptors are used, this `post_get_license_config_with_metadata` interceptor runs after the
        `post_get_license_config` interceptor. The (possibly modified) response returned by
        `post_get_license_config` will be passed to
        `post_get_license_config_with_metadata`.
        """
        return response, metadata

    def pre_list_license_configs(
        self,
        request: license_config_service.ListLicenseConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.ListLicenseConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_license_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_list_license_configs(
        self, response: license_config_service.ListLicenseConfigsResponse
    ) -> license_config_service.ListLicenseConfigsResponse:
        """Post-rpc interceptor for list_license_configs

        DEPRECATED. Please use the `post_list_license_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code. This `post_list_license_configs` interceptor runs
        before the `post_list_license_configs_with_metadata` interceptor.
        """
        return response

    def post_list_license_configs_with_metadata(
        self,
        response: license_config_service.ListLicenseConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.ListLicenseConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_license_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseConfigService server but before it is returned to user code.

        We recommend only using this `post_list_license_configs_with_metadata`
        interceptor in new development instead of the `post_list_license_configs` interceptor.
        When both interceptors are used, this `post_list_license_configs_with_metadata` interceptor runs after the
        `post_list_license_configs` interceptor. The (possibly modified) response returned by
        `post_list_license_configs` will be passed to
        `post_list_license_configs_with_metadata`.
        """
        return response, metadata

    def pre_retract_license_config(
        self,
        request: license_config_service.RetractLicenseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.RetractLicenseConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for retract_license_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_retract_license_config(
        self, response: license_config_service.RetractLicenseConfigResponse
    ) -> license_config_service.RetractLicenseConfigResponse:
        """Post-rpc interceptor for retract_license_config

        DEPRECATED. Please use the `post_retract_license_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code. This `post_retract_license_config` interceptor runs
        before the `post_retract_license_config_with_metadata` interceptor.
        """
        return response

    def post_retract_license_config_with_metadata(
        self,
        response: license_config_service.RetractLicenseConfigResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.RetractLicenseConfigResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for retract_license_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseConfigService server but before it is returned to user code.

        We recommend only using this `post_retract_license_config_with_metadata`
        interceptor in new development instead of the `post_retract_license_config` interceptor.
        When both interceptors are used, this `post_retract_license_config_with_metadata` interceptor runs after the
        `post_retract_license_config` interceptor. The (possibly modified) response returned by
        `post_retract_license_config` will be passed to
        `post_retract_license_config_with_metadata`.
        """
        return response, metadata

    def pre_update_license_config(
        self,
        request: license_config_service.UpdateLicenseConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        license_config_service.UpdateLicenseConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_license_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_update_license_config(
        self, response: gcd_license_config.LicenseConfig
    ) -> gcd_license_config.LicenseConfig:
        """Post-rpc interceptor for update_license_config

        DEPRECATED. Please use the `post_update_license_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code. This `post_update_license_config` interceptor runs
        before the `post_update_license_config_with_metadata` interceptor.
        """
        return response

    def post_update_license_config_with_metadata(
        self,
        response: gcd_license_config.LicenseConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_license_config.LicenseConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_license_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseConfigService server but before it is returned to user code.

        We recommend only using this `post_update_license_config_with_metadata`
        interceptor in new development instead of the `post_update_license_config` interceptor.
        When both interceptors are used, this `post_update_license_config_with_metadata` interceptor runs after the
        `post_update_license_config` interceptor. The (possibly modified) response returned by
        `post_update_license_config` will be passed to
        `post_update_license_config_with_metadata`.
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
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LicenseConfigService server but before
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
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LicenseConfigService server but before
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
        before they are sent to the LicenseConfigService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the LicenseConfigService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LicenseConfigServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LicenseConfigServiceRestInterceptor


class LicenseConfigServiceRestTransport(_BaseLicenseConfigServiceRestTransport):
    """REST backend synchronous transport for LicenseConfigService.

    Service for managing license config related resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "discoveryengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[LicenseConfigServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'discoveryengine.googleapis.com').
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
            interceptor (Optional[LicenseConfigServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LicenseConfigServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateLicenseConfig(
        _BaseLicenseConfigServiceRestTransport._BaseCreateLicenseConfig,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.CreateLicenseConfig")

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
            request: license_config_service.CreateLicenseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_license_config.LicenseConfig:
            r"""Call the create license config method over HTTP.

            Args:
                request (~.license_config_service.CreateLicenseConfigRequest):
                    The request object. Request message for
                [LicenseConfigService.CreateLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_license_config.LicenseConfig:
                    Information about users' licenses.
            """

            http_options = _BaseLicenseConfigServiceRestTransport._BaseCreateLicenseConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_license_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseCreateLicenseConfig,
                    "_BaseCreateLicenseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.CreateLicenseConfig",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "CreateLicenseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseConfigServiceRestTransport._CreateLicenseConfig._get_response(
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
            resp = gcd_license_config.LicenseConfig()
            pb_resp = gcd_license_config.LicenseConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_license_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_license_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_license_config.LicenseConfig.to_json(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.create_license_config",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "CreateLicenseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DistributeLicenseConfig(
        _BaseLicenseConfigServiceRestTransport._BaseDistributeLicenseConfig,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.DistributeLicenseConfig")

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
            request: license_config_service.DistributeLicenseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> license_config_service.DistributeLicenseConfigResponse:
            r"""Call the distribute license config method over HTTP.

            Args:
                request (~.license_config_service.DistributeLicenseConfigRequest):
                    The request object. Request message for
                [LicenseConfigService.DistributeLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.license_config_service.DistributeLicenseConfigResponse:
                    Response message for
                [LicenseConfigService.DistributeLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig]
                method.

            """

            http_options = _BaseLicenseConfigServiceRestTransport._BaseDistributeLicenseConfig._get_http_options()
            request, metadata = self._interceptor.pre_distribute_license_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseDistributeLicenseConfig,
                    "_BaseDistributeLicenseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.DistributeLicenseConfig",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "DistributeLicenseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseConfigServiceRestTransport._DistributeLicenseConfig._get_response(
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
            resp = license_config_service.DistributeLicenseConfigResponse()
            pb_resp = license_config_service.DistributeLicenseConfigResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_distribute_license_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_distribute_license_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        license_config_service.DistributeLicenseConfigResponse.to_json(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.distribute_license_config",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "DistributeLicenseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLicenseConfig(
        _BaseLicenseConfigServiceRestTransport._BaseGetLicenseConfig,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.GetLicenseConfig")

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
            request: license_config_service.GetLicenseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> license_config.LicenseConfig:
            r"""Call the get license config method over HTTP.

            Args:
                request (~.license_config_service.GetLicenseConfigRequest):
                    The request object. Request message for
                [LicenseConfigService.GetLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.license_config.LicenseConfig:
                    Information about users' licenses.
            """

            http_options = _BaseLicenseConfigServiceRestTransport._BaseGetLicenseConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_license_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseGetLicenseConfig,
                    "_BaseGetLicenseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.GetLicenseConfig",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "GetLicenseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseConfigServiceRestTransport._GetLicenseConfig._get_response(
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
            resp = license_config.LicenseConfig()
            pb_resp = license_config.LicenseConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_license_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_license_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = license_config.LicenseConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.get_license_config",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "GetLicenseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLicenseConfigs(
        _BaseLicenseConfigServiceRestTransport._BaseListLicenseConfigs,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.ListLicenseConfigs")

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
            request: license_config_service.ListLicenseConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> license_config_service.ListLicenseConfigsResponse:
            r"""Call the list license configs method over HTTP.

            Args:
                request (~.license_config_service.ListLicenseConfigsRequest):
                    The request object. Request message for
                [LicenseConfigService.ListLicenseConfigs][google.cloud.discoveryengine.v1beta.LicenseConfigService.ListLicenseConfigs]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.license_config_service.ListLicenseConfigsResponse:
                    Response message for
                [LicenseConfigService.ListLicenseConfigs][google.cloud.discoveryengine.v1beta.LicenseConfigService.ListLicenseConfigs]
                method.

            """

            http_options = _BaseLicenseConfigServiceRestTransport._BaseListLicenseConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_license_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseListLicenseConfigs,
                    "_BaseListLicenseConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.ListLicenseConfigs",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "ListLicenseConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseConfigServiceRestTransport._ListLicenseConfigs._get_response(
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
            resp = license_config_service.ListLicenseConfigsResponse()
            pb_resp = license_config_service.ListLicenseConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_license_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_license_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        license_config_service.ListLicenseConfigsResponse.to_json(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.list_license_configs",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "ListLicenseConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetractLicenseConfig(
        _BaseLicenseConfigServiceRestTransport._BaseRetractLicenseConfig,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.RetractLicenseConfig")

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
            request: license_config_service.RetractLicenseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> license_config_service.RetractLicenseConfigResponse:
            r"""Call the retract license config method over HTTP.

            Args:
                request (~.license_config_service.RetractLicenseConfigRequest):
                    The request object. Request message for
                [LicenseConfigService.RetractLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.license_config_service.RetractLicenseConfigResponse:
                    Response message for
                [LicenseConfigService.RetractLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig]
                method.

            """

            http_options = _BaseLicenseConfigServiceRestTransport._BaseRetractLicenseConfig._get_http_options()
            request, metadata = self._interceptor.pre_retract_license_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseRetractLicenseConfig,
                    "_BaseRetractLicenseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.RetractLicenseConfig",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "RetractLicenseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseConfigServiceRestTransport._RetractLicenseConfig._get_response(
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
            resp = license_config_service.RetractLicenseConfigResponse()
            pb_resp = license_config_service.RetractLicenseConfigResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retract_license_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retract_license_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        license_config_service.RetractLicenseConfigResponse.to_json(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.retract_license_config",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "RetractLicenseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLicenseConfig(
        _BaseLicenseConfigServiceRestTransport._BaseUpdateLicenseConfig,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.UpdateLicenseConfig")

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
            request: license_config_service.UpdateLicenseConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_license_config.LicenseConfig:
            r"""Call the update license config method over HTTP.

            Args:
                request (~.license_config_service.UpdateLicenseConfigRequest):
                    The request object. Request message for
                [LicenseConfigService.UpdateLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_license_config.LicenseConfig:
                    Information about users' licenses.
            """

            http_options = _BaseLicenseConfigServiceRestTransport._BaseUpdateLicenseConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_license_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseUpdateLicenseConfig,
                    "_BaseUpdateLicenseConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.UpdateLicenseConfig",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "UpdateLicenseConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseConfigServiceRestTransport._UpdateLicenseConfig._get_response(
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
            resp = gcd_license_config.LicenseConfig()
            pb_resp = gcd_license_config.LicenseConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_license_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_license_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_license_config.LicenseConfig.to_json(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.update_license_config",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "UpdateLicenseConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_license_config(
        self,
    ) -> Callable[
        [license_config_service.CreateLicenseConfigRequest],
        gcd_license_config.LicenseConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLicenseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def distribute_license_config(
        self,
    ) -> Callable[
        [license_config_service.DistributeLicenseConfigRequest],
        license_config_service.DistributeLicenseConfigResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DistributeLicenseConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_license_config(
        self,
    ) -> Callable[
        [license_config_service.GetLicenseConfigRequest], license_config.LicenseConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLicenseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_license_configs(
        self,
    ) -> Callable[
        [license_config_service.ListLicenseConfigsRequest],
        license_config_service.ListLicenseConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLicenseConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def retract_license_config(
        self,
    ) -> Callable[
        [license_config_service.RetractLicenseConfigRequest],
        license_config_service.RetractLicenseConfigResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetractLicenseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_license_config(
        self,
    ) -> Callable[
        [license_config_service.UpdateLicenseConfigRequest],
        gcd_license_config.LicenseConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLicenseConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseLicenseConfigServiceRestTransport._BaseCancelOperation,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.CancelOperation")

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

            http_options = _BaseLicenseConfigServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseConfigServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseLicenseConfigServiceRestTransport._BaseGetOperation,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.GetOperation")

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

            http_options = _BaseLicenseConfigServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseConfigServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
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
        _BaseLicenseConfigServiceRestTransport._BaseListOperations,
        LicenseConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("LicenseConfigServiceRestTransport.ListOperations")

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

            http_options = _BaseLicenseConfigServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseConfigServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.LicenseConfigServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseConfigServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.discoveryengine_v1beta.LicenseConfigServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
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


__all__ = ("LicenseConfigServiceRestTransport",)
