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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.maintenance_api_v1beta._compat import transcode_request
from google.cloud.maintenance_api_v1beta.types import maintenance_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseMaintenanceRestTransport

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


class MaintenanceRestInterceptor:
    """Interceptor for Maintenance.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MaintenanceRestTransport.

    .. code-block:: python
        class MyCustomMaintenanceInterceptor(MaintenanceRestInterceptor):
            def pre_get_resource_maintenance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource_maintenance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resource_maintenances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resource_maintenances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_summarize_maintenances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_summarize_maintenances(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MaintenanceRestTransport(interceptor=MyCustomMaintenanceInterceptor())
        client = MaintenanceClient(transport=transport)


    """

    def pre_get_resource_maintenance(
        self,
        request: maintenance_service.GetResourceMaintenanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maintenance_service.GetResourceMaintenanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_resource_maintenance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Maintenance server.
        """
        return request, metadata

    def post_get_resource_maintenance(
        self, response: maintenance_service.ResourceMaintenance
    ) -> maintenance_service.ResourceMaintenance:
        """Post-rpc interceptor for get_resource_maintenance

        DEPRECATED. Please use the `post_get_resource_maintenance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Maintenance server but before
        it is returned to user code. This `post_get_resource_maintenance` interceptor runs
        before the `post_get_resource_maintenance_with_metadata` interceptor.
        """
        return response

    def post_get_resource_maintenance_with_metadata(
        self,
        response: maintenance_service.ResourceMaintenance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maintenance_service.ResourceMaintenance, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_resource_maintenance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Maintenance server but before it is returned to user code.

        We recommend only using this `post_get_resource_maintenance_with_metadata`
        interceptor in new development instead of the `post_get_resource_maintenance` interceptor.
        When both interceptors are used, this `post_get_resource_maintenance_with_metadata` interceptor runs after the
        `post_get_resource_maintenance` interceptor. The (possibly modified) response returned by
        `post_get_resource_maintenance` will be passed to
        `post_get_resource_maintenance_with_metadata`.
        """
        return response, metadata

    def pre_list_resource_maintenances(
        self,
        request: maintenance_service.ListResourceMaintenancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maintenance_service.ListResourceMaintenancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_resource_maintenances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Maintenance server.
        """
        return request, metadata

    def post_list_resource_maintenances(
        self, response: maintenance_service.ListResourceMaintenancesResponse
    ) -> maintenance_service.ListResourceMaintenancesResponse:
        """Post-rpc interceptor for list_resource_maintenances

        DEPRECATED. Please use the `post_list_resource_maintenances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Maintenance server but before
        it is returned to user code. This `post_list_resource_maintenances` interceptor runs
        before the `post_list_resource_maintenances_with_metadata` interceptor.
        """
        return response

    def post_list_resource_maintenances_with_metadata(
        self,
        response: maintenance_service.ListResourceMaintenancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maintenance_service.ListResourceMaintenancesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_resource_maintenances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Maintenance server but before it is returned to user code.

        We recommend only using this `post_list_resource_maintenances_with_metadata`
        interceptor in new development instead of the `post_list_resource_maintenances` interceptor.
        When both interceptors are used, this `post_list_resource_maintenances_with_metadata` interceptor runs after the
        `post_list_resource_maintenances` interceptor. The (possibly modified) response returned by
        `post_list_resource_maintenances` will be passed to
        `post_list_resource_maintenances_with_metadata`.
        """
        return response, metadata

    def pre_summarize_maintenances(
        self,
        request: maintenance_service.SummarizeMaintenancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maintenance_service.SummarizeMaintenancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for summarize_maintenances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Maintenance server.
        """
        return request, metadata

    def post_summarize_maintenances(
        self, response: maintenance_service.SummarizeMaintenancesResponse
    ) -> maintenance_service.SummarizeMaintenancesResponse:
        """Post-rpc interceptor for summarize_maintenances

        DEPRECATED. Please use the `post_summarize_maintenances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Maintenance server but before
        it is returned to user code. This `post_summarize_maintenances` interceptor runs
        before the `post_summarize_maintenances_with_metadata` interceptor.
        """
        return response

    def post_summarize_maintenances_with_metadata(
        self,
        response: maintenance_service.SummarizeMaintenancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maintenance_service.SummarizeMaintenancesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for summarize_maintenances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Maintenance server but before it is returned to user code.

        We recommend only using this `post_summarize_maintenances_with_metadata`
        interceptor in new development instead of the `post_summarize_maintenances` interceptor.
        When both interceptors are used, this `post_summarize_maintenances_with_metadata` interceptor runs after the
        `post_summarize_maintenances` interceptor. The (possibly modified) response returned by
        `post_summarize_maintenances` will be passed to
        `post_summarize_maintenances_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Maintenance server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Maintenance server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Maintenance server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Maintenance server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class MaintenanceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MaintenanceRestInterceptor


class MaintenanceRestTransport(_BaseMaintenanceRestTransport):
    """REST backend synchronous transport for Maintenance.

    Unified Maintenance service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "maintenance.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[MaintenanceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'maintenance.googleapis.com').
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
            interceptor (Optional[MaintenanceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or MaintenanceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetResourceMaintenance(
        _BaseMaintenanceRestTransport._BaseGetResourceMaintenance, MaintenanceRestStub
    ):
        def __hash__(self):
            return hash("MaintenanceRestTransport.GetResourceMaintenance")

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
            request: maintenance_service.GetResourceMaintenanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> maintenance_service.ResourceMaintenance:
            r"""Call the get resource maintenance method over HTTP.

            Args:
                request (~.maintenance_service.GetResourceMaintenanceRequest):
                    The request object. The request structure for the
                GetResourceMaintenance method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.maintenance_service.ResourceMaintenance:
                    ResourceMaintenance is a resource
                that represents a maintenance operation
                on a resource.

            """

            http_options = _BaseMaintenanceRestTransport._BaseGetResourceMaintenance._get_http_options()
            request, metadata = self._interceptor.pre_get_resource_maintenance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMaintenanceRestTransport._BaseGetResourceMaintenance,
                    "_BaseGetResourceMaintenance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.maintenance.api_v1beta.MaintenanceClient.GetResourceMaintenance",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "GetResourceMaintenance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MaintenanceRestTransport._GetResourceMaintenance._get_response(
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
            resp = maintenance_service.ResourceMaintenance()
            pb_resp = maintenance_service.ResourceMaintenance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource_maintenance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_resource_maintenance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = maintenance_service.ResourceMaintenance.to_json(
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
                    "Received response for google.cloud.maintenance.api_v1beta.MaintenanceClient.get_resource_maintenance",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "GetResourceMaintenance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResourceMaintenances(
        _BaseMaintenanceRestTransport._BaseListResourceMaintenances, MaintenanceRestStub
    ):
        def __hash__(self):
            return hash("MaintenanceRestTransport.ListResourceMaintenances")

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
            request: maintenance_service.ListResourceMaintenancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> maintenance_service.ListResourceMaintenancesResponse:
            r"""Call the list resource
            maintenances method over HTTP.

                Args:
                    request (~.maintenance_service.ListResourceMaintenancesRequest):
                        The request object. The request structure for the
                    ListResourceMaintenances method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.maintenance_service.ListResourceMaintenancesResponse:
                        The response structure for the
                    ListResourceMaintenances method.

            """

            http_options = _BaseMaintenanceRestTransport._BaseListResourceMaintenances._get_http_options()
            request, metadata = self._interceptor.pre_list_resource_maintenances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMaintenanceRestTransport._BaseListResourceMaintenances,
                    "_BaseListResourceMaintenances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.maintenance.api_v1beta.MaintenanceClient.ListResourceMaintenances",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "ListResourceMaintenances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MaintenanceRestTransport._ListResourceMaintenances._get_response(
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
            resp = maintenance_service.ListResourceMaintenancesResponse()
            pb_resp = maintenance_service.ListResourceMaintenancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resource_maintenances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_resource_maintenances_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        maintenance_service.ListResourceMaintenancesResponse.to_json(
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
                    "Received response for google.cloud.maintenance.api_v1beta.MaintenanceClient.list_resource_maintenances",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "ListResourceMaintenances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SummarizeMaintenances(
        _BaseMaintenanceRestTransport._BaseSummarizeMaintenances, MaintenanceRestStub
    ):
        def __hash__(self):
            return hash("MaintenanceRestTransport.SummarizeMaintenances")

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
            request: maintenance_service.SummarizeMaintenancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> maintenance_service.SummarizeMaintenancesResponse:
            r"""Call the summarize maintenances method over HTTP.

            Args:
                request (~.maintenance_service.SummarizeMaintenancesRequest):
                    The request object. Request message for
                SummarizeMaintenances custom method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.maintenance_service.SummarizeMaintenancesResponse:
                    Request message for
                SummarizeMaintenances custom method.

            """

            http_options = _BaseMaintenanceRestTransport._BaseSummarizeMaintenances._get_http_options()
            request, metadata = self._interceptor.pre_summarize_maintenances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMaintenanceRestTransport._BaseSummarizeMaintenances,
                    "_BaseSummarizeMaintenances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.maintenance.api_v1beta.MaintenanceClient.SummarizeMaintenances",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "SummarizeMaintenances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MaintenanceRestTransport._SummarizeMaintenances._get_response(
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
            resp = maintenance_service.SummarizeMaintenancesResponse()
            pb_resp = maintenance_service.SummarizeMaintenancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_summarize_maintenances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_summarize_maintenances_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        maintenance_service.SummarizeMaintenancesResponse.to_json(
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
                    "Received response for google.cloud.maintenance.api_v1beta.MaintenanceClient.summarize_maintenances",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "SummarizeMaintenances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_resource_maintenance(
        self,
    ) -> Callable[
        [maintenance_service.GetResourceMaintenanceRequest],
        maintenance_service.ResourceMaintenance,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResourceMaintenance(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_resource_maintenances(
        self,
    ) -> Callable[
        [maintenance_service.ListResourceMaintenancesRequest],
        maintenance_service.ListResourceMaintenancesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResourceMaintenances(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def summarize_maintenances(
        self,
    ) -> Callable[
        [maintenance_service.SummarizeMaintenancesRequest],
        maintenance_service.SummarizeMaintenancesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SummarizeMaintenances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseMaintenanceRestTransport._BaseGetLocation, MaintenanceRestStub
    ):
        def __hash__(self):
            return hash("MaintenanceRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseMaintenanceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMaintenanceRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.maintenance.api_v1beta.MaintenanceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MaintenanceRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.maintenance.api_v1beta.MaintenanceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseMaintenanceRestTransport._BaseListLocations, MaintenanceRestStub
    ):
        def __hash__(self):
            return hash("MaintenanceRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseMaintenanceRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMaintenanceRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.maintenance.api_v1beta.MaintenanceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MaintenanceRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.maintenance.api_v1beta.MaintenanceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.maintenance.api.v1beta.Maintenance",
                        "rpcName": "ListLocations",
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


__all__ = ("MaintenanceRestTransport",)
