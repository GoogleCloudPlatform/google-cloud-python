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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.talent_v4._compat import transcode_request
from google.cloud.talent_v4.types import tenant, tenant_service
from google.cloud.talent_v4.types import tenant as gct_tenant

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTenantServiceRestTransport

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


class TenantServiceRestInterceptor:
    """Interceptor for TenantService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TenantServiceRestTransport.

    .. code-block:: python
        class MyCustomTenantServiceInterceptor(TenantServiceRestInterceptor):
            def pre_create_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tenant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tenant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tenants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tenants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tenant(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TenantServiceRestTransport(interceptor=MyCustomTenantServiceInterceptor())
        client = TenantServiceClient(transport=transport)


    """

    def pre_create_tenant(
        self,
        request: tenant_service.CreateTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tenant_service.CreateTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TenantService server.
        """
        return request, metadata

    def post_create_tenant(self, response: gct_tenant.Tenant) -> gct_tenant.Tenant:
        """Post-rpc interceptor for create_tenant

        DEPRECATED. Please use the `post_create_tenant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TenantService server but before
        it is returned to user code. This `post_create_tenant` interceptor runs
        before the `post_create_tenant_with_metadata` interceptor.
        """
        return response

    def post_create_tenant_with_metadata(
        self,
        response: gct_tenant.Tenant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gct_tenant.Tenant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tenant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TenantService server but before it is returned to user code.

        We recommend only using this `post_create_tenant_with_metadata`
        interceptor in new development instead of the `post_create_tenant` interceptor.
        When both interceptors are used, this `post_create_tenant_with_metadata` interceptor runs after the
        `post_create_tenant` interceptor. The (possibly modified) response returned by
        `post_create_tenant` will be passed to
        `post_create_tenant_with_metadata`.
        """
        return response, metadata

    def pre_delete_tenant(
        self,
        request: tenant_service.DeleteTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tenant_service.DeleteTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TenantService server.
        """
        return request, metadata

    def pre_get_tenant(
        self,
        request: tenant_service.GetTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tenant_service.GetTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TenantService server.
        """
        return request, metadata

    def post_get_tenant(self, response: tenant.Tenant) -> tenant.Tenant:
        """Post-rpc interceptor for get_tenant

        DEPRECATED. Please use the `post_get_tenant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TenantService server but before
        it is returned to user code. This `post_get_tenant` interceptor runs
        before the `post_get_tenant_with_metadata` interceptor.
        """
        return response

    def post_get_tenant_with_metadata(
        self, response: tenant.Tenant, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[tenant.Tenant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tenant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TenantService server but before it is returned to user code.

        We recommend only using this `post_get_tenant_with_metadata`
        interceptor in new development instead of the `post_get_tenant` interceptor.
        When both interceptors are used, this `post_get_tenant_with_metadata` interceptor runs after the
        `post_get_tenant` interceptor. The (possibly modified) response returned by
        `post_get_tenant` will be passed to
        `post_get_tenant_with_metadata`.
        """
        return response, metadata

    def pre_list_tenants(
        self,
        request: tenant_service.ListTenantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tenant_service.ListTenantsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_tenants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TenantService server.
        """
        return request, metadata

    def post_list_tenants(
        self, response: tenant_service.ListTenantsResponse
    ) -> tenant_service.ListTenantsResponse:
        """Post-rpc interceptor for list_tenants

        DEPRECATED. Please use the `post_list_tenants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TenantService server but before
        it is returned to user code. This `post_list_tenants` interceptor runs
        before the `post_list_tenants_with_metadata` interceptor.
        """
        return response

    def post_list_tenants_with_metadata(
        self,
        response: tenant_service.ListTenantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tenant_service.ListTenantsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_tenants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TenantService server but before it is returned to user code.

        We recommend only using this `post_list_tenants_with_metadata`
        interceptor in new development instead of the `post_list_tenants` interceptor.
        When both interceptors are used, this `post_list_tenants_with_metadata` interceptor runs after the
        `post_list_tenants` interceptor. The (possibly modified) response returned by
        `post_list_tenants` will be passed to
        `post_list_tenants_with_metadata`.
        """
        return response, metadata

    def pre_update_tenant(
        self,
        request: tenant_service.UpdateTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tenant_service.UpdateTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TenantService server.
        """
        return request, metadata

    def post_update_tenant(self, response: gct_tenant.Tenant) -> gct_tenant.Tenant:
        """Post-rpc interceptor for update_tenant

        DEPRECATED. Please use the `post_update_tenant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TenantService server but before
        it is returned to user code. This `post_update_tenant` interceptor runs
        before the `post_update_tenant_with_metadata` interceptor.
        """
        return response

    def post_update_tenant_with_metadata(
        self,
        response: gct_tenant.Tenant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gct_tenant.Tenant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tenant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TenantService server but before it is returned to user code.

        We recommend only using this `post_update_tenant_with_metadata`
        interceptor in new development instead of the `post_update_tenant` interceptor.
        When both interceptors are used, this `post_update_tenant_with_metadata` interceptor runs after the
        `post_update_tenant` interceptor. The (possibly modified) response returned by
        `post_update_tenant` will be passed to
        `post_update_tenant_with_metadata`.
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
        before they are sent to the TenantService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TenantService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TenantServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TenantServiceRestInterceptor


class TenantServiceRestTransport(_BaseTenantServiceRestTransport):
    """REST backend synchronous transport for TenantService.

    A service that handles tenant management, including CRUD and
    enumeration.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "jobs.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TenantServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'jobs.googleapis.com').
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
            interceptor (Optional[TenantServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TenantServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateTenant(
        _BaseTenantServiceRestTransport._BaseCreateTenant, TenantServiceRestStub
    ):
        def __hash__(self):
            return hash("TenantServiceRestTransport.CreateTenant")

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
            request: tenant_service.CreateTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gct_tenant.Tenant:
            r"""Call the create tenant method over HTTP.

            Args:
                request (~.tenant_service.CreateTenantRequest):
                    The request object. The Request of the CreateTenant
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gct_tenant.Tenant:
                    A Tenant resource represents a tenant
                in the service. A tenant is a group or
                entity that shares common access with
                specific privileges for resources like
                jobs. Customer may create multiple
                tenants to provide data isolation for
                different groups.

            """

            http_options = (
                _BaseTenantServiceRestTransport._BaseCreateTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTenantServiceRestTransport._BaseCreateTenant,
                    "_BaseCreateTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.talent_v4.TenantServiceClient.CreateTenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "CreateTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TenantServiceRestTransport._CreateTenant._get_response(
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
            resp = gct_tenant.Tenant()
            pb_resp = gct_tenant.Tenant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_tenant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tenant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gct_tenant.Tenant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.talent_v4.TenantServiceClient.create_tenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "CreateTenant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTenant(
        _BaseTenantServiceRestTransport._BaseDeleteTenant, TenantServiceRestStub
    ):
        def __hash__(self):
            return hash("TenantServiceRestTransport.DeleteTenant")

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
            request: tenant_service.DeleteTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete tenant method over HTTP.

            Args:
                request (~.tenant_service.DeleteTenantRequest):
                    The request object. Request to delete a tenant.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseTenantServiceRestTransport._BaseDeleteTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTenantServiceRestTransport._BaseDeleteTenant,
                    "_BaseDeleteTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.talent_v4.TenantServiceClient.DeleteTenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "DeleteTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TenantServiceRestTransport._DeleteTenant._get_response(
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

    class _GetTenant(
        _BaseTenantServiceRestTransport._BaseGetTenant, TenantServiceRestStub
    ):
        def __hash__(self):
            return hash("TenantServiceRestTransport.GetTenant")

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
            request: tenant_service.GetTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tenant.Tenant:
            r"""Call the get tenant method over HTTP.

            Args:
                request (~.tenant_service.GetTenantRequest):
                    The request object. Request for getting a tenant by name.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tenant.Tenant:
                    A Tenant resource represents a tenant
                in the service. A tenant is a group or
                entity that shares common access with
                specific privileges for resources like
                jobs. Customer may create multiple
                tenants to provide data isolation for
                different groups.

            """

            http_options = (
                _BaseTenantServiceRestTransport._BaseGetTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTenantServiceRestTransport._BaseGetTenant,
                    "_BaseGetTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.talent_v4.TenantServiceClient.GetTenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "GetTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TenantServiceRestTransport._GetTenant._get_response(
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
            resp = tenant.Tenant()
            pb_resp = tenant.Tenant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tenant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tenant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tenant.Tenant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.talent_v4.TenantServiceClient.get_tenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "GetTenant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTenants(
        _BaseTenantServiceRestTransport._BaseListTenants, TenantServiceRestStub
    ):
        def __hash__(self):
            return hash("TenantServiceRestTransport.ListTenants")

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
            request: tenant_service.ListTenantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tenant_service.ListTenantsResponse:
            r"""Call the list tenants method over HTTP.

            Args:
                request (~.tenant_service.ListTenantsRequest):
                    The request object. List tenants for which the client has
                ACL visibility.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tenant_service.ListTenantsResponse:
                    The List tenants response object.
            """

            http_options = (
                _BaseTenantServiceRestTransport._BaseListTenants._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tenants(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTenantServiceRestTransport._BaseListTenants,
                    "_BaseListTenants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.talent_v4.TenantServiceClient.ListTenants",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "ListTenants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TenantServiceRestTransport._ListTenants._get_response(
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
            resp = tenant_service.ListTenantsResponse()
            pb_resp = tenant_service.ListTenantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tenants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tenants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tenant_service.ListTenantsResponse.to_json(
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
                    "Received response for google.cloud.talent_v4.TenantServiceClient.list_tenants",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "ListTenants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTenant(
        _BaseTenantServiceRestTransport._BaseUpdateTenant, TenantServiceRestStub
    ):
        def __hash__(self):
            return hash("TenantServiceRestTransport.UpdateTenant")

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
            request: tenant_service.UpdateTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gct_tenant.Tenant:
            r"""Call the update tenant method over HTTP.

            Args:
                request (~.tenant_service.UpdateTenantRequest):
                    The request object. Request for updating a specified
                tenant.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gct_tenant.Tenant:
                    A Tenant resource represents a tenant
                in the service. A tenant is a group or
                entity that shares common access with
                specific privileges for resources like
                jobs. Customer may create multiple
                tenants to provide data isolation for
                different groups.

            """

            http_options = (
                _BaseTenantServiceRestTransport._BaseUpdateTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTenantServiceRestTransport._BaseUpdateTenant,
                    "_BaseUpdateTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.talent_v4.TenantServiceClient.UpdateTenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "UpdateTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TenantServiceRestTransport._UpdateTenant._get_response(
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
            resp = gct_tenant.Tenant()
            pb_resp = gct_tenant.Tenant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_tenant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tenant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gct_tenant.Tenant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.talent_v4.TenantServiceClient.update_tenant",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "UpdateTenant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_tenant(
        self,
    ) -> Callable[[tenant_service.CreateTenantRequest], gct_tenant.Tenant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tenant(
        self,
    ) -> Callable[[tenant_service.DeleteTenantRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tenant(self) -> Callable[[tenant_service.GetTenantRequest], tenant.Tenant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tenants(
        self,
    ) -> Callable[
        [tenant_service.ListTenantsRequest], tenant_service.ListTenantsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTenants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tenant(
        self,
    ) -> Callable[[tenant_service.UpdateTenantRequest], gct_tenant.Tenant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseTenantServiceRestTransport._BaseGetOperation, TenantServiceRestStub
    ):
        def __hash__(self):
            return hash("TenantServiceRestTransport.GetOperation")

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

            http_options = (
                _BaseTenantServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTenantServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.talent_v4.TenantServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TenantServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.talent_v4.TenantServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.talent.v4.TenantService",
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


__all__ = ("TenantServiceRestTransport",)
