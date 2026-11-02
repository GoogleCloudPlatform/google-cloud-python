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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.datamanager_v1._compat import transcode_request
from google.ads.datamanager_v1.types import partner_link_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePartnerLinkServiceRestTransport

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


class PartnerLinkServiceRestInterceptor:
    """Interceptor for PartnerLinkService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PartnerLinkServiceRestTransport.

    .. code-block:: python
        class MyCustomPartnerLinkServiceInterceptor(PartnerLinkServiceRestInterceptor):
            def pre_create_partner_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_partner_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_partner_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_search_partner_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_partner_links(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PartnerLinkServiceRestTransport(interceptor=MyCustomPartnerLinkServiceInterceptor())
        client = PartnerLinkServiceClient(transport=transport)


    """

    def pre_create_partner_link(
        self,
        request: partner_link_service.CreatePartnerLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_link_service.CreatePartnerLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_partner_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerLinkService server.
        """
        return request, metadata

    def post_create_partner_link(
        self, response: partner_link_service.PartnerLink
    ) -> partner_link_service.PartnerLink:
        """Post-rpc interceptor for create_partner_link

        DEPRECATED. Please use the `post_create_partner_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PartnerLinkService server but before
        it is returned to user code. This `post_create_partner_link` interceptor runs
        before the `post_create_partner_link_with_metadata` interceptor.
        """
        return response

    def post_create_partner_link_with_metadata(
        self,
        response: partner_link_service.PartnerLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_link_service.PartnerLink, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_partner_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PartnerLinkService server but before it is returned to user code.

        We recommend only using this `post_create_partner_link_with_metadata`
        interceptor in new development instead of the `post_create_partner_link` interceptor.
        When both interceptors are used, this `post_create_partner_link_with_metadata` interceptor runs after the
        `post_create_partner_link` interceptor. The (possibly modified) response returned by
        `post_create_partner_link` will be passed to
        `post_create_partner_link_with_metadata`.
        """
        return response, metadata

    def pre_delete_partner_link(
        self,
        request: partner_link_service.DeletePartnerLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_link_service.DeletePartnerLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_partner_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerLinkService server.
        """
        return request, metadata

    def pre_search_partner_links(
        self,
        request: partner_link_service.SearchPartnerLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_link_service.SearchPartnerLinksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_partner_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerLinkService server.
        """
        return request, metadata

    def post_search_partner_links(
        self, response: partner_link_service.SearchPartnerLinksResponse
    ) -> partner_link_service.SearchPartnerLinksResponse:
        """Post-rpc interceptor for search_partner_links

        DEPRECATED. Please use the `post_search_partner_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PartnerLinkService server but before
        it is returned to user code. This `post_search_partner_links` interceptor runs
        before the `post_search_partner_links_with_metadata` interceptor.
        """
        return response

    def post_search_partner_links_with_metadata(
        self,
        response: partner_link_service.SearchPartnerLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_link_service.SearchPartnerLinksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_partner_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PartnerLinkService server but before it is returned to user code.

        We recommend only using this `post_search_partner_links_with_metadata`
        interceptor in new development instead of the `post_search_partner_links` interceptor.
        When both interceptors are used, this `post_search_partner_links_with_metadata` interceptor runs after the
        `post_search_partner_links` interceptor. The (possibly modified) response returned by
        `post_search_partner_links` will be passed to
        `post_search_partner_links_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class PartnerLinkServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PartnerLinkServiceRestInterceptor


class PartnerLinkServiceRestTransport(_BasePartnerLinkServiceRestTransport):
    """REST backend synchronous transport for PartnerLinkService.

    Service for managing partner links.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "datamanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[PartnerLinkServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'datamanager.googleapis.com').
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
            interceptor (Optional[PartnerLinkServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or PartnerLinkServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreatePartnerLink(
        _BasePartnerLinkServiceRestTransport._BaseCreatePartnerLink,
        PartnerLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("PartnerLinkServiceRestTransport.CreatePartnerLink")

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
            request: partner_link_service.CreatePartnerLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_link_service.PartnerLink:
            r"""Call the create partner link method over HTTP.

            Args:
                request (~.partner_link_service.CreatePartnerLinkRequest):
                    The request object. Request to create a
                [PartnerLink][google.ads.datamanager.v1.PartnerLink]
                resource. Returns a
                [PartnerLink][google.ads.datamanager.v1.PartnerLink].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_link_service.PartnerLink:
                    A partner link between an owning
                account and a partner account.

            """

            http_options = _BasePartnerLinkServiceRestTransport._BaseCreatePartnerLink._get_http_options()
            request, metadata = self._interceptor.pre_create_partner_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerLinkServiceRestTransport._BaseCreatePartnerLink,
                    "_BaseCreatePartnerLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.PartnerLinkServiceClient.CreatePartnerLink",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.PartnerLinkService",
                        "rpcName": "CreatePartnerLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerLinkServiceRestTransport._CreatePartnerLink._get_response(
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
            resp = partner_link_service.PartnerLink()
            pb_resp = partner_link_service.PartnerLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_partner_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_partner_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = partner_link_service.PartnerLink.to_json(
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
                    "Received response for google.ads.datamanager_v1.PartnerLinkServiceClient.create_partner_link",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.PartnerLinkService",
                        "rpcName": "CreatePartnerLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePartnerLink(
        _BasePartnerLinkServiceRestTransport._BaseDeletePartnerLink,
        PartnerLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("PartnerLinkServiceRestTransport.DeletePartnerLink")

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
            request: partner_link_service.DeletePartnerLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete partner link method over HTTP.

            Args:
                request (~.partner_link_service.DeletePartnerLinkRequest):
                    The request object. Request to delete a
                [PartnerLink][google.ads.datamanager.v1.PartnerLink]
                resource. Returns a
                [google.protobuf.Empty][google.protobuf.Empty].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BasePartnerLinkServiceRestTransport._BaseDeletePartnerLink._get_http_options()
            request, metadata = self._interceptor.pre_delete_partner_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerLinkServiceRestTransport._BaseDeletePartnerLink,
                    "_BaseDeletePartnerLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.PartnerLinkServiceClient.DeletePartnerLink",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.PartnerLinkService",
                        "rpcName": "DeletePartnerLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerLinkServiceRestTransport._DeletePartnerLink._get_response(
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

    class _SearchPartnerLinks(
        _BasePartnerLinkServiceRestTransport._BaseSearchPartnerLinks,
        PartnerLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("PartnerLinkServiceRestTransport.SearchPartnerLinks")

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
            request: partner_link_service.SearchPartnerLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_link_service.SearchPartnerLinksResponse:
            r"""Call the search partner links method over HTTP.

            Args:
                request (~.partner_link_service.SearchPartnerLinksRequest):
                    The request object. Request to search for
                [PartnerLink][google.ads.datamanager.v1.PartnerLink]
                resources. Returns a
                [SearchPartnerLinksResponse][google.ads.datamanager.v1.SearchPartnerLinksResponse].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_link_service.SearchPartnerLinksResponse:
                    Response from the
                [SearchPartnerLinksRequest][google.ads.datamanager.v1.SearchPartnerLinksRequest].

            """

            http_options = _BasePartnerLinkServiceRestTransport._BaseSearchPartnerLinks._get_http_options()
            request, metadata = self._interceptor.pre_search_partner_links(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerLinkServiceRestTransport._BaseSearchPartnerLinks,
                    "_BaseSearchPartnerLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.PartnerLinkServiceClient.SearchPartnerLinks",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.PartnerLinkService",
                        "rpcName": "SearchPartnerLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PartnerLinkServiceRestTransport._SearchPartnerLinks._get_response(
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
            resp = partner_link_service.SearchPartnerLinksResponse()
            pb_resp = partner_link_service.SearchPartnerLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_partner_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_partner_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        partner_link_service.SearchPartnerLinksResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.PartnerLinkServiceClient.search_partner_links",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.PartnerLinkService",
                        "rpcName": "SearchPartnerLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_partner_link(
        self,
    ) -> Callable[
        [partner_link_service.CreatePartnerLinkRequest],
        partner_link_service.PartnerLink,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePartnerLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_partner_link(
        self,
    ) -> Callable[[partner_link_service.DeletePartnerLinkRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePartnerLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_partner_links(
        self,
    ) -> Callable[
        [partner_link_service.SearchPartnerLinksRequest],
        partner_link_service.SearchPartnerLinksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchPartnerLinks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("PartnerLinkServiceRestTransport",)
