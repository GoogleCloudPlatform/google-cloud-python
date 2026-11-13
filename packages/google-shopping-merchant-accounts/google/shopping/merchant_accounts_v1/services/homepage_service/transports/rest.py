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

from google.shopping.merchant_accounts_v1._compat import transcode_request
from google.shopping.merchant_accounts_v1.types import homepage
from google.shopping.merchant_accounts_v1.types import homepage as gsma_homepage

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseHomepageServiceRestTransport

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


class HomepageServiceRestInterceptor:
    """Interceptor for HomepageService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the HomepageServiceRestTransport.

    .. code-block:: python
        class MyCustomHomepageServiceInterceptor(HomepageServiceRestInterceptor):
            def pre_claim_homepage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_claim_homepage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_homepage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_homepage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_unclaim_homepage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_unclaim_homepage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_homepage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_homepage(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = HomepageServiceRestTransport(interceptor=MyCustomHomepageServiceInterceptor())
        client = HomepageServiceClient(transport=transport)


    """

    def pre_claim_homepage(
        self,
        request: homepage.ClaimHomepageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[homepage.ClaimHomepageRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for claim_homepage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HomepageService server.
        """
        return request, metadata

    def post_claim_homepage(self, response: homepage.Homepage) -> homepage.Homepage:
        """Post-rpc interceptor for claim_homepage

        DEPRECATED. Please use the `post_claim_homepage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HomepageService server but before
        it is returned to user code. This `post_claim_homepage` interceptor runs
        before the `post_claim_homepage_with_metadata` interceptor.
        """
        return response

    def post_claim_homepage_with_metadata(
        self,
        response: homepage.Homepage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[homepage.Homepage, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for claim_homepage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HomepageService server but before it is returned to user code.

        We recommend only using this `post_claim_homepage_with_metadata`
        interceptor in new development instead of the `post_claim_homepage` interceptor.
        When both interceptors are used, this `post_claim_homepage_with_metadata` interceptor runs after the
        `post_claim_homepage` interceptor. The (possibly modified) response returned by
        `post_claim_homepage` will be passed to
        `post_claim_homepage_with_metadata`.
        """
        return response, metadata

    def pre_get_homepage(
        self,
        request: homepage.GetHomepageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[homepage.GetHomepageRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_homepage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HomepageService server.
        """
        return request, metadata

    def post_get_homepage(self, response: homepage.Homepage) -> homepage.Homepage:
        """Post-rpc interceptor for get_homepage

        DEPRECATED. Please use the `post_get_homepage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HomepageService server but before
        it is returned to user code. This `post_get_homepage` interceptor runs
        before the `post_get_homepage_with_metadata` interceptor.
        """
        return response

    def post_get_homepage_with_metadata(
        self,
        response: homepage.Homepage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[homepage.Homepage, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_homepage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HomepageService server but before it is returned to user code.

        We recommend only using this `post_get_homepage_with_metadata`
        interceptor in new development instead of the `post_get_homepage` interceptor.
        When both interceptors are used, this `post_get_homepage_with_metadata` interceptor runs after the
        `post_get_homepage` interceptor. The (possibly modified) response returned by
        `post_get_homepage` will be passed to
        `post_get_homepage_with_metadata`.
        """
        return response, metadata

    def pre_unclaim_homepage(
        self,
        request: homepage.UnclaimHomepageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        homepage.UnclaimHomepageRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for unclaim_homepage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HomepageService server.
        """
        return request, metadata

    def post_unclaim_homepage(self, response: homepage.Homepage) -> homepage.Homepage:
        """Post-rpc interceptor for unclaim_homepage

        DEPRECATED. Please use the `post_unclaim_homepage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HomepageService server but before
        it is returned to user code. This `post_unclaim_homepage` interceptor runs
        before the `post_unclaim_homepage_with_metadata` interceptor.
        """
        return response

    def post_unclaim_homepage_with_metadata(
        self,
        response: homepage.Homepage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[homepage.Homepage, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for unclaim_homepage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HomepageService server but before it is returned to user code.

        We recommend only using this `post_unclaim_homepage_with_metadata`
        interceptor in new development instead of the `post_unclaim_homepage` interceptor.
        When both interceptors are used, this `post_unclaim_homepage_with_metadata` interceptor runs after the
        `post_unclaim_homepage` interceptor. The (possibly modified) response returned by
        `post_unclaim_homepage` will be passed to
        `post_unclaim_homepage_with_metadata`.
        """
        return response, metadata

    def pre_update_homepage(
        self,
        request: gsma_homepage.UpdateHomepageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsma_homepage.UpdateHomepageRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_homepage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HomepageService server.
        """
        return request, metadata

    def post_update_homepage(
        self, response: gsma_homepage.Homepage
    ) -> gsma_homepage.Homepage:
        """Post-rpc interceptor for update_homepage

        DEPRECATED. Please use the `post_update_homepage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HomepageService server but before
        it is returned to user code. This `post_update_homepage` interceptor runs
        before the `post_update_homepage_with_metadata` interceptor.
        """
        return response

    def post_update_homepage_with_metadata(
        self,
        response: gsma_homepage.Homepage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsma_homepage.Homepage, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_homepage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HomepageService server but before it is returned to user code.

        We recommend only using this `post_update_homepage_with_metadata`
        interceptor in new development instead of the `post_update_homepage` interceptor.
        When both interceptors are used, this `post_update_homepage_with_metadata` interceptor runs after the
        `post_update_homepage` interceptor. The (possibly modified) response returned by
        `post_update_homepage` will be passed to
        `post_update_homepage_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class HomepageServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: HomepageServiceRestInterceptor


class HomepageServiceRestTransport(_BaseHomepageServiceRestTransport):
    """REST backend synchronous transport for HomepageService.

    Service to support an API for a store's homepage.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "merchantapi.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[HomepageServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'merchantapi.googleapis.com').
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
            interceptor (Optional[HomepageServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or HomepageServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ClaimHomepage(
        _BaseHomepageServiceRestTransport._BaseClaimHomepage, HomepageServiceRestStub
    ):
        def __hash__(self):
            return hash("HomepageServiceRestTransport.ClaimHomepage")

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
            request: homepage.ClaimHomepageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> homepage.Homepage:
            r"""Call the claim homepage method over HTTP.

            Args:
                request (~.homepage.ClaimHomepageRequest):
                    The request object. Request message for the ``ClaimHomepage`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.homepage.Homepage:
                    The ``Homepage`` message represents a business's store
                homepage within the system.

                A business's homepage is the primary domain where
                customers interact with their store.

                The homepage can be claimed and verified as a proof of
                ownership and allows the business to unlock features
                that require a verified website. For more information,
                see `Understanding online store URL
                verification <//support.google.com/merchants/answer/176793>`__.

            """

            http_options = (
                _BaseHomepageServiceRestTransport._BaseClaimHomepage._get_http_options()
            )
            request, metadata = self._interceptor.pre_claim_homepage(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHomepageServiceRestTransport._BaseClaimHomepage,
                    "_BaseClaimHomepage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.HomepageServiceClient.ClaimHomepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "ClaimHomepage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HomepageServiceRestTransport._ClaimHomepage._get_response(
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
            resp = homepage.Homepage()
            pb_resp = homepage.Homepage.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_claim_homepage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_claim_homepage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = homepage.Homepage.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.HomepageServiceClient.claim_homepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "ClaimHomepage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHomepage(
        _BaseHomepageServiceRestTransport._BaseGetHomepage, HomepageServiceRestStub
    ):
        def __hash__(self):
            return hash("HomepageServiceRestTransport.GetHomepage")

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
            request: homepage.GetHomepageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> homepage.Homepage:
            r"""Call the get homepage method over HTTP.

            Args:
                request (~.homepage.GetHomepageRequest):
                    The request object. Request message for the ``GetHomepage`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.homepage.Homepage:
                    The ``Homepage`` message represents a business's store
                homepage within the system.

                A business's homepage is the primary domain where
                customers interact with their store.

                The homepage can be claimed and verified as a proof of
                ownership and allows the business to unlock features
                that require a verified website. For more information,
                see `Understanding online store URL
                verification <//support.google.com/merchants/answer/176793>`__.

            """

            http_options = (
                _BaseHomepageServiceRestTransport._BaseGetHomepage._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_homepage(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHomepageServiceRestTransport._BaseGetHomepage,
                    "_BaseGetHomepage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.HomepageServiceClient.GetHomepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "GetHomepage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HomepageServiceRestTransport._GetHomepage._get_response(
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
            resp = homepage.Homepage()
            pb_resp = homepage.Homepage.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_homepage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_homepage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = homepage.Homepage.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.HomepageServiceClient.get_homepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "GetHomepage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UnclaimHomepage(
        _BaseHomepageServiceRestTransport._BaseUnclaimHomepage, HomepageServiceRestStub
    ):
        def __hash__(self):
            return hash("HomepageServiceRestTransport.UnclaimHomepage")

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
            request: homepage.UnclaimHomepageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> homepage.Homepage:
            r"""Call the unclaim homepage method over HTTP.

            Args:
                request (~.homepage.UnclaimHomepageRequest):
                    The request object. Request message for the ``UnclaimHomepage`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.homepage.Homepage:
                    The ``Homepage`` message represents a business's store
                homepage within the system.

                A business's homepage is the primary domain where
                customers interact with their store.

                The homepage can be claimed and verified as a proof of
                ownership and allows the business to unlock features
                that require a verified website. For more information,
                see `Understanding online store URL
                verification <//support.google.com/merchants/answer/176793>`__.

            """

            http_options = _BaseHomepageServiceRestTransport._BaseUnclaimHomepage._get_http_options()
            request, metadata = self._interceptor.pre_unclaim_homepage(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHomepageServiceRestTransport._BaseUnclaimHomepage,
                    "_BaseUnclaimHomepage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.HomepageServiceClient.UnclaimHomepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "UnclaimHomepage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HomepageServiceRestTransport._UnclaimHomepage._get_response(
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
            resp = homepage.Homepage()
            pb_resp = homepage.Homepage.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_unclaim_homepage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_unclaim_homepage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = homepage.Homepage.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.HomepageServiceClient.unclaim_homepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "UnclaimHomepage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHomepage(
        _BaseHomepageServiceRestTransport._BaseUpdateHomepage, HomepageServiceRestStub
    ):
        def __hash__(self):
            return hash("HomepageServiceRestTransport.UpdateHomepage")

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
            request: gsma_homepage.UpdateHomepageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsma_homepage.Homepage:
            r"""Call the update homepage method over HTTP.

            Args:
                request (~.gsma_homepage.UpdateHomepageRequest):
                    The request object. Request message for the ``UpdateHomepage`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsma_homepage.Homepage:
                    The ``Homepage`` message represents a business's store
                homepage within the system.

                A business's homepage is the primary domain where
                customers interact with their store.

                The homepage can be claimed and verified as a proof of
                ownership and allows the business to unlock features
                that require a verified website. For more information,
                see `Understanding online store URL
                verification <//support.google.com/merchants/answer/176793>`__.

            """

            http_options = _BaseHomepageServiceRestTransport._BaseUpdateHomepage._get_http_options()
            request, metadata = self._interceptor.pre_update_homepage(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHomepageServiceRestTransport._BaseUpdateHomepage,
                    "_BaseUpdateHomepage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.HomepageServiceClient.UpdateHomepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "UpdateHomepage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HomepageServiceRestTransport._UpdateHomepage._get_response(
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
            resp = gsma_homepage.Homepage()
            pb_resp = gsma_homepage.Homepage.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_homepage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_homepage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsma_homepage.Homepage.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.HomepageServiceClient.update_homepage",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.HomepageService",
                        "rpcName": "UpdateHomepage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def claim_homepage(
        self,
    ) -> Callable[[homepage.ClaimHomepageRequest], homepage.Homepage]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ClaimHomepage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_homepage(
        self,
    ) -> Callable[[homepage.GetHomepageRequest], homepage.Homepage]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHomepage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def unclaim_homepage(
        self,
    ) -> Callable[[homepage.UnclaimHomepageRequest], homepage.Homepage]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UnclaimHomepage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_homepage(
        self,
    ) -> Callable[[gsma_homepage.UpdateHomepageRequest], gsma_homepage.Homepage]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHomepage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("HomepageServiceRestTransport",)
