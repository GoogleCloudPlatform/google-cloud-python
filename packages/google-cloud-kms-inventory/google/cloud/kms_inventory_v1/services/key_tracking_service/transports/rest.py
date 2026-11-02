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

from google.cloud.kms_inventory_v1._compat import transcode_request
from google.cloud.kms_inventory_v1.types import key_tracking_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseKeyTrackingServiceRestTransport

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


class KeyTrackingServiceRestInterceptor:
    """Interceptor for KeyTrackingService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the KeyTrackingServiceRestTransport.

    .. code-block:: python
        class MyCustomKeyTrackingServiceInterceptor(KeyTrackingServiceRestInterceptor):
            def pre_get_protected_resources_summary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_protected_resources_summary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_protected_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_protected_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = KeyTrackingServiceRestTransport(interceptor=MyCustomKeyTrackingServiceInterceptor())
        client = KeyTrackingServiceClient(transport=transport)


    """

    def pre_get_protected_resources_summary(
        self,
        request: key_tracking_service.GetProtectedResourcesSummaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        key_tracking_service.GetProtectedResourcesSummaryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_protected_resources_summary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyTrackingService server.
        """
        return request, metadata

    def post_get_protected_resources_summary(
        self, response: key_tracking_service.ProtectedResourcesSummary
    ) -> key_tracking_service.ProtectedResourcesSummary:
        """Post-rpc interceptor for get_protected_resources_summary

        DEPRECATED. Please use the `post_get_protected_resources_summary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyTrackingService server but before
        it is returned to user code. This `post_get_protected_resources_summary` interceptor runs
        before the `post_get_protected_resources_summary_with_metadata` interceptor.
        """
        return response

    def post_get_protected_resources_summary_with_metadata(
        self,
        response: key_tracking_service.ProtectedResourcesSummary,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        key_tracking_service.ProtectedResourcesSummary,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_protected_resources_summary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyTrackingService server but before it is returned to user code.

        We recommend only using this `post_get_protected_resources_summary_with_metadata`
        interceptor in new development instead of the `post_get_protected_resources_summary` interceptor.
        When both interceptors are used, this `post_get_protected_resources_summary_with_metadata` interceptor runs after the
        `post_get_protected_resources_summary` interceptor. The (possibly modified) response returned by
        `post_get_protected_resources_summary` will be passed to
        `post_get_protected_resources_summary_with_metadata`.
        """
        return response, metadata

    def pre_search_protected_resources(
        self,
        request: key_tracking_service.SearchProtectedResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        key_tracking_service.SearchProtectedResourcesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_protected_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyTrackingService server.
        """
        return request, metadata

    def post_search_protected_resources(
        self, response: key_tracking_service.SearchProtectedResourcesResponse
    ) -> key_tracking_service.SearchProtectedResourcesResponse:
        """Post-rpc interceptor for search_protected_resources

        DEPRECATED. Please use the `post_search_protected_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyTrackingService server but before
        it is returned to user code. This `post_search_protected_resources` interceptor runs
        before the `post_search_protected_resources_with_metadata` interceptor.
        """
        return response

    def post_search_protected_resources_with_metadata(
        self,
        response: key_tracking_service.SearchProtectedResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        key_tracking_service.SearchProtectedResourcesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_protected_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyTrackingService server but before it is returned to user code.

        We recommend only using this `post_search_protected_resources_with_metadata`
        interceptor in new development instead of the `post_search_protected_resources` interceptor.
        When both interceptors are used, this `post_search_protected_resources_with_metadata` interceptor runs after the
        `post_search_protected_resources` interceptor. The (possibly modified) response returned by
        `post_search_protected_resources` will be passed to
        `post_search_protected_resources_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class KeyTrackingServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: KeyTrackingServiceRestInterceptor


class KeyTrackingServiceRestTransport(_BaseKeyTrackingServiceRestTransport):
    """REST backend synchronous transport for KeyTrackingService.

    Returns information about the resources in an org that are
    protected by a given Cloud KMS key via CMEK.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "kmsinventory.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[KeyTrackingServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'kmsinventory.googleapis.com').
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
            interceptor (Optional[KeyTrackingServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or KeyTrackingServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetProtectedResourcesSummary(
        _BaseKeyTrackingServiceRestTransport._BaseGetProtectedResourcesSummary,
        KeyTrackingServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyTrackingServiceRestTransport.GetProtectedResourcesSummary")

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
            request: key_tracking_service.GetProtectedResourcesSummaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> key_tracking_service.ProtectedResourcesSummary:
            r"""Call the get protected resources
            summary method over HTTP.

                Args:
                    request (~.key_tracking_service.GetProtectedResourcesSummaryRequest):
                        The request object. Request message for
                    [KeyTrackingService.GetProtectedResourcesSummary][google.cloud.kms.inventory.v1.KeyTrackingService.GetProtectedResourcesSummary].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.key_tracking_service.ProtectedResourcesSummary:
                        Aggregate information about the
                    resources protected by a Cloud KMS key
                    in the same Cloud organization/project
                    as the key.

            """

            http_options = _BaseKeyTrackingServiceRestTransport._BaseGetProtectedResourcesSummary._get_http_options()
            request, metadata = self._interceptor.pre_get_protected_resources_summary(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyTrackingServiceRestTransport._BaseGetProtectedResourcesSummary,
                    "_BaseGetProtectedResourcesSummary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms.inventory_v1.KeyTrackingServiceClient.GetProtectedResourcesSummary",
                    extra={
                        "serviceName": "google.cloud.kms.inventory.v1.KeyTrackingService",
                        "rpcName": "GetProtectedResourcesSummary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyTrackingServiceRestTransport._GetProtectedResourcesSummary._get_response(
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
            resp = key_tracking_service.ProtectedResourcesSummary()
            pb_resp = key_tracking_service.ProtectedResourcesSummary.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_protected_resources_summary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_protected_resources_summary_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        key_tracking_service.ProtectedResourcesSummary.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms.inventory_v1.KeyTrackingServiceClient.get_protected_resources_summary",
                    extra={
                        "serviceName": "google.cloud.kms.inventory.v1.KeyTrackingService",
                        "rpcName": "GetProtectedResourcesSummary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchProtectedResources(
        _BaseKeyTrackingServiceRestTransport._BaseSearchProtectedResources,
        KeyTrackingServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyTrackingServiceRestTransport.SearchProtectedResources")

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
            request: key_tracking_service.SearchProtectedResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> key_tracking_service.SearchProtectedResourcesResponse:
            r"""Call the search protected
            resources method over HTTP.

                Args:
                    request (~.key_tracking_service.SearchProtectedResourcesRequest):
                        The request object. Request message for
                    [KeyTrackingService.SearchProtectedResources][google.cloud.kms.inventory.v1.KeyTrackingService.SearchProtectedResources].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.key_tracking_service.SearchProtectedResourcesResponse:
                        Response message for
                    [KeyTrackingService.SearchProtectedResources][google.cloud.kms.inventory.v1.KeyTrackingService.SearchProtectedResources].

            """

            http_options = _BaseKeyTrackingServiceRestTransport._BaseSearchProtectedResources._get_http_options()
            request, metadata = self._interceptor.pre_search_protected_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyTrackingServiceRestTransport._BaseSearchProtectedResources,
                    "_BaseSearchProtectedResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms.inventory_v1.KeyTrackingServiceClient.SearchProtectedResources",
                    extra={
                        "serviceName": "google.cloud.kms.inventory.v1.KeyTrackingService",
                        "rpcName": "SearchProtectedResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyTrackingServiceRestTransport._SearchProtectedResources._get_response(
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
            resp = key_tracking_service.SearchProtectedResourcesResponse()
            pb_resp = key_tracking_service.SearchProtectedResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_protected_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_protected_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        key_tracking_service.SearchProtectedResourcesResponse.to_json(
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
                    "Received response for google.cloud.kms.inventory_v1.KeyTrackingServiceClient.search_protected_resources",
                    extra={
                        "serviceName": "google.cloud.kms.inventory.v1.KeyTrackingService",
                        "rpcName": "SearchProtectedResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_protected_resources_summary(
        self,
    ) -> Callable[
        [key_tracking_service.GetProtectedResourcesSummaryRequest],
        key_tracking_service.ProtectedResourcesSummary,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProtectedResourcesSummary(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_protected_resources(
        self,
    ) -> Callable[
        [key_tracking_service.SearchProtectedResourcesRequest],
        key_tracking_service.SearchProtectedResourcesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchProtectedResources(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("KeyTrackingServiceRestTransport",)
