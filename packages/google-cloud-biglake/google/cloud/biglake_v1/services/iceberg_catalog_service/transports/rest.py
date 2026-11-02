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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.biglake_v1._compat import transcode_request
from google.cloud.biglake_v1.types import iceberg_rest_catalog

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseIcebergCatalogServiceRestTransport

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


class IcebergCatalogServiceRestInterceptor:
    """Interceptor for IcebergCatalogService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IcebergCatalogServiceRestTransport.

    .. code-block:: python
        class MyCustomIcebergCatalogServiceInterceptor(IcebergCatalogServiceRestInterceptor):
            def pre_create_iceberg_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_iceberg_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_failover_iceberg_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_failover_iceberg_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iceberg_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iceberg_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_iceberg_catalogs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_iceberg_catalogs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_iceberg_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_iceberg_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = IcebergCatalogServiceRestTransport(interceptor=MyCustomIcebergCatalogServiceInterceptor())
        client = IcebergCatalogServiceClient(transport=transport)


    """

    def pre_create_iceberg_catalog(
        self,
        request: iceberg_rest_catalog.CreateIcebergCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.CreateIcebergCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_iceberg_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IcebergCatalogService server.
        """
        return request, metadata

    def post_create_iceberg_catalog(
        self, response: iceberg_rest_catalog.IcebergCatalog
    ) -> iceberg_rest_catalog.IcebergCatalog:
        """Post-rpc interceptor for create_iceberg_catalog

        DEPRECATED. Please use the `post_create_iceberg_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IcebergCatalogService server but before
        it is returned to user code. This `post_create_iceberg_catalog` interceptor runs
        before the `post_create_iceberg_catalog_with_metadata` interceptor.
        """
        return response

    def post_create_iceberg_catalog_with_metadata(
        self,
        response: iceberg_rest_catalog.IcebergCatalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.IcebergCatalog, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_iceberg_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IcebergCatalogService server but before it is returned to user code.

        We recommend only using this `post_create_iceberg_catalog_with_metadata`
        interceptor in new development instead of the `post_create_iceberg_catalog` interceptor.
        When both interceptors are used, this `post_create_iceberg_catalog_with_metadata` interceptor runs after the
        `post_create_iceberg_catalog` interceptor. The (possibly modified) response returned by
        `post_create_iceberg_catalog` will be passed to
        `post_create_iceberg_catalog_with_metadata`.
        """
        return response, metadata

    def pre_failover_iceberg_catalog(
        self,
        request: iceberg_rest_catalog.FailoverIcebergCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.FailoverIcebergCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for failover_iceberg_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IcebergCatalogService server.
        """
        return request, metadata

    def post_failover_iceberg_catalog(
        self, response: iceberg_rest_catalog.FailoverIcebergCatalogResponse
    ) -> iceberg_rest_catalog.FailoverIcebergCatalogResponse:
        """Post-rpc interceptor for failover_iceberg_catalog

        DEPRECATED. Please use the `post_failover_iceberg_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IcebergCatalogService server but before
        it is returned to user code. This `post_failover_iceberg_catalog` interceptor runs
        before the `post_failover_iceberg_catalog_with_metadata` interceptor.
        """
        return response

    def post_failover_iceberg_catalog_with_metadata(
        self,
        response: iceberg_rest_catalog.FailoverIcebergCatalogResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.FailoverIcebergCatalogResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for failover_iceberg_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IcebergCatalogService server but before it is returned to user code.

        We recommend only using this `post_failover_iceberg_catalog_with_metadata`
        interceptor in new development instead of the `post_failover_iceberg_catalog` interceptor.
        When both interceptors are used, this `post_failover_iceberg_catalog_with_metadata` interceptor runs after the
        `post_failover_iceberg_catalog` interceptor. The (possibly modified) response returned by
        `post_failover_iceberg_catalog` will be passed to
        `post_failover_iceberg_catalog_with_metadata`.
        """
        return response, metadata

    def pre_get_iceberg_catalog(
        self,
        request: iceberg_rest_catalog.GetIcebergCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.GetIcebergCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_iceberg_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IcebergCatalogService server.
        """
        return request, metadata

    def post_get_iceberg_catalog(
        self, response: iceberg_rest_catalog.IcebergCatalog
    ) -> iceberg_rest_catalog.IcebergCatalog:
        """Post-rpc interceptor for get_iceberg_catalog

        DEPRECATED. Please use the `post_get_iceberg_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IcebergCatalogService server but before
        it is returned to user code. This `post_get_iceberg_catalog` interceptor runs
        before the `post_get_iceberg_catalog_with_metadata` interceptor.
        """
        return response

    def post_get_iceberg_catalog_with_metadata(
        self,
        response: iceberg_rest_catalog.IcebergCatalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.IcebergCatalog, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_iceberg_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IcebergCatalogService server but before it is returned to user code.

        We recommend only using this `post_get_iceberg_catalog_with_metadata`
        interceptor in new development instead of the `post_get_iceberg_catalog` interceptor.
        When both interceptors are used, this `post_get_iceberg_catalog_with_metadata` interceptor runs after the
        `post_get_iceberg_catalog` interceptor. The (possibly modified) response returned by
        `post_get_iceberg_catalog` will be passed to
        `post_get_iceberg_catalog_with_metadata`.
        """
        return response, metadata

    def pre_list_iceberg_catalogs(
        self,
        request: iceberg_rest_catalog.ListIcebergCatalogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.ListIcebergCatalogsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_iceberg_catalogs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IcebergCatalogService server.
        """
        return request, metadata

    def post_list_iceberg_catalogs(
        self, response: iceberg_rest_catalog.ListIcebergCatalogsResponse
    ) -> iceberg_rest_catalog.ListIcebergCatalogsResponse:
        """Post-rpc interceptor for list_iceberg_catalogs

        DEPRECATED. Please use the `post_list_iceberg_catalogs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IcebergCatalogService server but before
        it is returned to user code. This `post_list_iceberg_catalogs` interceptor runs
        before the `post_list_iceberg_catalogs_with_metadata` interceptor.
        """
        return response

    def post_list_iceberg_catalogs_with_metadata(
        self,
        response: iceberg_rest_catalog.ListIcebergCatalogsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.ListIcebergCatalogsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_iceberg_catalogs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IcebergCatalogService server but before it is returned to user code.

        We recommend only using this `post_list_iceberg_catalogs_with_metadata`
        interceptor in new development instead of the `post_list_iceberg_catalogs` interceptor.
        When both interceptors are used, this `post_list_iceberg_catalogs_with_metadata` interceptor runs after the
        `post_list_iceberg_catalogs` interceptor. The (possibly modified) response returned by
        `post_list_iceberg_catalogs` will be passed to
        `post_list_iceberg_catalogs_with_metadata`.
        """
        return response, metadata

    def pre_update_iceberg_catalog(
        self,
        request: iceberg_rest_catalog.UpdateIcebergCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.UpdateIcebergCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_iceberg_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IcebergCatalogService server.
        """
        return request, metadata

    def post_update_iceberg_catalog(
        self, response: iceberg_rest_catalog.IcebergCatalog
    ) -> iceberg_rest_catalog.IcebergCatalog:
        """Post-rpc interceptor for update_iceberg_catalog

        DEPRECATED. Please use the `post_update_iceberg_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IcebergCatalogService server but before
        it is returned to user code. This `post_update_iceberg_catalog` interceptor runs
        before the `post_update_iceberg_catalog_with_metadata` interceptor.
        """
        return response

    def post_update_iceberg_catalog_with_metadata(
        self,
        response: iceberg_rest_catalog.IcebergCatalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iceberg_rest_catalog.IcebergCatalog, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_iceberg_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IcebergCatalogService server but before it is returned to user code.

        We recommend only using this `post_update_iceberg_catalog_with_metadata`
        interceptor in new development instead of the `post_update_iceberg_catalog` interceptor.
        When both interceptors are used, this `post_update_iceberg_catalog_with_metadata` interceptor runs after the
        `post_update_iceberg_catalog` interceptor. The (possibly modified) response returned by
        `post_update_iceberg_catalog` will be passed to
        `post_update_iceberg_catalog_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class IcebergCatalogServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IcebergCatalogServiceRestInterceptor


class IcebergCatalogServiceRestTransport(_BaseIcebergCatalogServiceRestTransport):
    """REST backend synchronous transport for IcebergCatalogService.

    Lakehouse runtime catalog supports the following catalog
    management methods:

    - GetIcebergCatalog
    - ListIcebergCatalogs
    - DeleteIcebergCatalog
    - UpdateIcebergCatalog
    - CreateIcebergCatalog
    - FailoverIcebergCatalog

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "biglake.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[IcebergCatalogServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'biglake.googleapis.com').
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
            interceptor (Optional[IcebergCatalogServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or IcebergCatalogServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateIcebergCatalog(
        _BaseIcebergCatalogServiceRestTransport._BaseCreateIcebergCatalog,
        IcebergCatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("IcebergCatalogServiceRestTransport.CreateIcebergCatalog")

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
            request: iceberg_rest_catalog.CreateIcebergCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iceberg_rest_catalog.IcebergCatalog:
            r"""Call the create iceberg catalog method over HTTP.

            Args:
                request (~.iceberg_rest_catalog.CreateIcebergCatalogRequest):
                    The request object. The request message for the ``CreateIcebergCatalog``
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iceberg_rest_catalog.IcebergCatalog:
                    The Iceberg REST Catalog information.
            """

            http_options = _BaseIcebergCatalogServiceRestTransport._BaseCreateIcebergCatalog._get_http_options()
            request, metadata = self._interceptor.pre_create_iceberg_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIcebergCatalogServiceRestTransport._BaseCreateIcebergCatalog,
                    "_BaseCreateIcebergCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake_v1.IcebergCatalogServiceClient.CreateIcebergCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "CreateIcebergCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IcebergCatalogServiceRestTransport._CreateIcebergCatalog._get_response(
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
            resp = iceberg_rest_catalog.IcebergCatalog()
            pb_resp = iceberg_rest_catalog.IcebergCatalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_iceberg_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_iceberg_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = iceberg_rest_catalog.IcebergCatalog.to_json(
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
                    "Received response for google.cloud.biglake_v1.IcebergCatalogServiceClient.create_iceberg_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "CreateIcebergCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FailoverIcebergCatalog(
        _BaseIcebergCatalogServiceRestTransport._BaseFailoverIcebergCatalog,
        IcebergCatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("IcebergCatalogServiceRestTransport.FailoverIcebergCatalog")

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
            request: iceberg_rest_catalog.FailoverIcebergCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iceberg_rest_catalog.FailoverIcebergCatalogResponse:
            r"""Call the failover iceberg catalog method over HTTP.

            Args:
                request (~.iceberg_rest_catalog.FailoverIcebergCatalogRequest):
                    The request object. Request message for
                FailoverIcebergCatalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iceberg_rest_catalog.FailoverIcebergCatalogResponse:
                    Response message for
                FailoverIcebergCatalog.

            """

            http_options = _BaseIcebergCatalogServiceRestTransport._BaseFailoverIcebergCatalog._get_http_options()
            request, metadata = self._interceptor.pre_failover_iceberg_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIcebergCatalogServiceRestTransport._BaseFailoverIcebergCatalog,
                    "_BaseFailoverIcebergCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake_v1.IcebergCatalogServiceClient.FailoverIcebergCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "FailoverIcebergCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IcebergCatalogServiceRestTransport._FailoverIcebergCatalog._get_response(
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
            resp = iceberg_rest_catalog.FailoverIcebergCatalogResponse()
            pb_resp = iceberg_rest_catalog.FailoverIcebergCatalogResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_failover_iceberg_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_failover_iceberg_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        iceberg_rest_catalog.FailoverIcebergCatalogResponse.to_json(
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
                    "Received response for google.cloud.biglake_v1.IcebergCatalogServiceClient.failover_iceberg_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "FailoverIcebergCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIcebergCatalog(
        _BaseIcebergCatalogServiceRestTransport._BaseGetIcebergCatalog,
        IcebergCatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("IcebergCatalogServiceRestTransport.GetIcebergCatalog")

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
            request: iceberg_rest_catalog.GetIcebergCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iceberg_rest_catalog.IcebergCatalog:
            r"""Call the get iceberg catalog method over HTTP.

            Args:
                request (~.iceberg_rest_catalog.GetIcebergCatalogRequest):
                    The request object. The request message for the ``GetIcebergCatalog`` API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iceberg_rest_catalog.IcebergCatalog:
                    The Iceberg REST Catalog information.
            """

            http_options = _BaseIcebergCatalogServiceRestTransport._BaseGetIcebergCatalog._get_http_options()
            request, metadata = self._interceptor.pre_get_iceberg_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIcebergCatalogServiceRestTransport._BaseGetIcebergCatalog,
                    "_BaseGetIcebergCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake_v1.IcebergCatalogServiceClient.GetIcebergCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "GetIcebergCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IcebergCatalogServiceRestTransport._GetIcebergCatalog._get_response(
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
            resp = iceberg_rest_catalog.IcebergCatalog()
            pb_resp = iceberg_rest_catalog.IcebergCatalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_iceberg_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iceberg_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = iceberg_rest_catalog.IcebergCatalog.to_json(
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
                    "Received response for google.cloud.biglake_v1.IcebergCatalogServiceClient.get_iceberg_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "GetIcebergCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIcebergCatalogs(
        _BaseIcebergCatalogServiceRestTransport._BaseListIcebergCatalogs,
        IcebergCatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("IcebergCatalogServiceRestTransport.ListIcebergCatalogs")

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
            request: iceberg_rest_catalog.ListIcebergCatalogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iceberg_rest_catalog.ListIcebergCatalogsResponse:
            r"""Call the list iceberg catalogs method over HTTP.

            Args:
                request (~.iceberg_rest_catalog.ListIcebergCatalogsRequest):
                    The request object. The request message for the ``ListIcebergCatalogs`` API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iceberg_rest_catalog.ListIcebergCatalogsResponse:
                    The response message for the ``ListIcebergCatalogs``
                API.

            """

            http_options = _BaseIcebergCatalogServiceRestTransport._BaseListIcebergCatalogs._get_http_options()
            request, metadata = self._interceptor.pre_list_iceberg_catalogs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIcebergCatalogServiceRestTransport._BaseListIcebergCatalogs,
                    "_BaseListIcebergCatalogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake_v1.IcebergCatalogServiceClient.ListIcebergCatalogs",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "ListIcebergCatalogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IcebergCatalogServiceRestTransport._ListIcebergCatalogs._get_response(
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
            resp = iceberg_rest_catalog.ListIcebergCatalogsResponse()
            pb_resp = iceberg_rest_catalog.ListIcebergCatalogsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_iceberg_catalogs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_iceberg_catalogs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        iceberg_rest_catalog.ListIcebergCatalogsResponse.to_json(
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
                    "Received response for google.cloud.biglake_v1.IcebergCatalogServiceClient.list_iceberg_catalogs",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "ListIcebergCatalogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIcebergCatalog(
        _BaseIcebergCatalogServiceRestTransport._BaseUpdateIcebergCatalog,
        IcebergCatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("IcebergCatalogServiceRestTransport.UpdateIcebergCatalog")

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
            request: iceberg_rest_catalog.UpdateIcebergCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iceberg_rest_catalog.IcebergCatalog:
            r"""Call the update iceberg catalog method over HTTP.

            Args:
                request (~.iceberg_rest_catalog.UpdateIcebergCatalogRequest):
                    The request object. The request message for the ``UpdateIcebergCatalog``
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iceberg_rest_catalog.IcebergCatalog:
                    The Iceberg REST Catalog information.
            """

            http_options = _BaseIcebergCatalogServiceRestTransport._BaseUpdateIcebergCatalog._get_http_options()
            request, metadata = self._interceptor.pre_update_iceberg_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIcebergCatalogServiceRestTransport._BaseUpdateIcebergCatalog,
                    "_BaseUpdateIcebergCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake_v1.IcebergCatalogServiceClient.UpdateIcebergCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "UpdateIcebergCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IcebergCatalogServiceRestTransport._UpdateIcebergCatalog._get_response(
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
            resp = iceberg_rest_catalog.IcebergCatalog()
            pb_resp = iceberg_rest_catalog.IcebergCatalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_iceberg_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_iceberg_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = iceberg_rest_catalog.IcebergCatalog.to_json(
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
                    "Received response for google.cloud.biglake_v1.IcebergCatalogServiceClient.update_iceberg_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                        "rpcName": "UpdateIcebergCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_iceberg_catalog(
        self,
    ) -> Callable[
        [iceberg_rest_catalog.CreateIcebergCatalogRequest],
        iceberg_rest_catalog.IcebergCatalog,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIcebergCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def failover_iceberg_catalog(
        self,
    ) -> Callable[
        [iceberg_rest_catalog.FailoverIcebergCatalogRequest],
        iceberg_rest_catalog.FailoverIcebergCatalogResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FailoverIcebergCatalog(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_iceberg_catalog(
        self,
    ) -> Callable[
        [iceberg_rest_catalog.GetIcebergCatalogRequest],
        iceberg_rest_catalog.IcebergCatalog,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIcebergCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_iceberg_catalogs(
        self,
    ) -> Callable[
        [iceberg_rest_catalog.ListIcebergCatalogsRequest],
        iceberg_rest_catalog.ListIcebergCatalogsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIcebergCatalogs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_iceberg_catalog(
        self,
    ) -> Callable[
        [iceberg_rest_catalog.UpdateIcebergCatalogRequest],
        iceberg_rest_catalog.IcebergCatalog,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIcebergCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("IcebergCatalogServiceRestTransport",)
