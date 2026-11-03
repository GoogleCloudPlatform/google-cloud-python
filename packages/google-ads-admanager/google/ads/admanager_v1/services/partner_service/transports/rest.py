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
from google.ads.admanager_v1.types import partner_messages, partner_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePartnerServiceRestTransport

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


class PartnerServiceRestInterceptor:
    """Interceptor for PartnerService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PartnerServiceRestTransport.

    .. code-block:: python
        class MyCustomPartnerServiceInterceptor(PartnerServiceRestInterceptor):
            def pre_batch_update_partners(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_partners(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_partner(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_partner(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_partners(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_partners(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_partner(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_partner(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PartnerServiceRestTransport(interceptor=MyCustomPartnerServiceInterceptor())
        client = PartnerServiceClient(transport=transport)


    """

    def pre_batch_update_partners(
        self,
        request: partner_service.BatchUpdatePartnersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_service.BatchUpdatePartnersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_partners

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerService server.
        """
        return request, metadata

    def post_batch_update_partners(
        self, response: partner_service.BatchUpdatePartnersResponse
    ) -> partner_service.BatchUpdatePartnersResponse:
        """Post-rpc interceptor for batch_update_partners

        DEPRECATED. Please use the `post_batch_update_partners_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PartnerService server but before
        it is returned to user code. This `post_batch_update_partners` interceptor runs
        before the `post_batch_update_partners_with_metadata` interceptor.
        """
        return response

    def post_batch_update_partners_with_metadata(
        self,
        response: partner_service.BatchUpdatePartnersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_service.BatchUpdatePartnersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_partners

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PartnerService server but before it is returned to user code.

        We recommend only using this `post_batch_update_partners_with_metadata`
        interceptor in new development instead of the `post_batch_update_partners` interceptor.
        When both interceptors are used, this `post_batch_update_partners_with_metadata` interceptor runs after the
        `post_batch_update_partners` interceptor. The (possibly modified) response returned by
        `post_batch_update_partners` will be passed to
        `post_batch_update_partners_with_metadata`.
        """
        return response, metadata

    def pre_get_partner(
        self,
        request: partner_service.GetPartnerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_service.GetPartnerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_partner

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerService server.
        """
        return request, metadata

    def post_get_partner(
        self, response: partner_messages.Partner
    ) -> partner_messages.Partner:
        """Post-rpc interceptor for get_partner

        DEPRECATED. Please use the `post_get_partner_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PartnerService server but before
        it is returned to user code. This `post_get_partner` interceptor runs
        before the `post_get_partner_with_metadata` interceptor.
        """
        return response

    def post_get_partner_with_metadata(
        self,
        response: partner_messages.Partner,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[partner_messages.Partner, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_partner

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PartnerService server but before it is returned to user code.

        We recommend only using this `post_get_partner_with_metadata`
        interceptor in new development instead of the `post_get_partner` interceptor.
        When both interceptors are used, this `post_get_partner_with_metadata` interceptor runs after the
        `post_get_partner` interceptor. The (possibly modified) response returned by
        `post_get_partner` will be passed to
        `post_get_partner_with_metadata`.
        """
        return response, metadata

    def pre_list_partners(
        self,
        request: partner_service.ListPartnersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_service.ListPartnersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_partners

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerService server.
        """
        return request, metadata

    def post_list_partners(
        self, response: partner_service.ListPartnersResponse
    ) -> partner_service.ListPartnersResponse:
        """Post-rpc interceptor for list_partners

        DEPRECATED. Please use the `post_list_partners_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PartnerService server but before
        it is returned to user code. This `post_list_partners` interceptor runs
        before the `post_list_partners_with_metadata` interceptor.
        """
        return response

    def post_list_partners_with_metadata(
        self,
        response: partner_service.ListPartnersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_service.ListPartnersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_partners

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PartnerService server but before it is returned to user code.

        We recommend only using this `post_list_partners_with_metadata`
        interceptor in new development instead of the `post_list_partners` interceptor.
        When both interceptors are used, this `post_list_partners_with_metadata` interceptor runs after the
        `post_list_partners` interceptor. The (possibly modified) response returned by
        `post_list_partners` will be passed to
        `post_list_partners_with_metadata`.
        """
        return response, metadata

    def pre_update_partner(
        self,
        request: partner_service.UpdatePartnerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_service.UpdatePartnerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_partner

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PartnerService server.
        """
        return request, metadata

    def post_update_partner(
        self, response: partner_messages.Partner
    ) -> partner_messages.Partner:
        """Post-rpc interceptor for update_partner

        DEPRECATED. Please use the `post_update_partner_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PartnerService server but before
        it is returned to user code. This `post_update_partner` interceptor runs
        before the `post_update_partner_with_metadata` interceptor.
        """
        return response

    def post_update_partner_with_metadata(
        self,
        response: partner_messages.Partner,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[partner_messages.Partner, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_partner

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PartnerService server but before it is returned to user code.

        We recommend only using this `post_update_partner_with_metadata`
        interceptor in new development instead of the `post_update_partner` interceptor.
        When both interceptors are used, this `post_update_partner_with_metadata` interceptor runs after the
        `post_update_partner` interceptor. The (possibly modified) response returned by
        `post_update_partner` will be passed to
        `post_update_partner_with_metadata`.
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
        before they are sent to the PartnerService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the PartnerService server but before
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
        before they are sent to the PartnerService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the PartnerService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class PartnerServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PartnerServiceRestInterceptor


class PartnerServiceRestTransport(_BasePartnerServiceRestTransport):
    """REST backend synchronous transport for PartnerService.

    Provides methods for handling
    [Partner][google.ads.admanager.v1.Partner] objects.

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
        interceptor: Optional[PartnerServiceRestInterceptor] = None,
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
            interceptor (Optional[PartnerServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or PartnerServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchUpdatePartners(
        _BasePartnerServiceRestTransport._BaseBatchUpdatePartners,
        PartnerServiceRestStub,
    ):
        def __hash__(self):
            return hash("PartnerServiceRestTransport.BatchUpdatePartners")

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
            request: partner_service.BatchUpdatePartnersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_service.BatchUpdatePartnersResponse:
            r"""Call the batch update partners method over HTTP.

            Args:
                request (~.partner_service.BatchUpdatePartnersRequest):
                    The request object. Request object for ``BatchUpdatePartners`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_service.BatchUpdatePartnersResponse:
                    Response object for ``BatchUpdatePartners`` method.
            """

            http_options = _BasePartnerServiceRestTransport._BaseBatchUpdatePartners._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_partners(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerServiceRestTransport._BaseBatchUpdatePartners,
                    "_BaseBatchUpdatePartners__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PartnerServiceClient.BatchUpdatePartners",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "BatchUpdatePartners",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerServiceRestTransport._BatchUpdatePartners._get_response(
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
            resp = partner_service.BatchUpdatePartnersResponse()
            pb_resp = partner_service.BatchUpdatePartnersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_partners(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_partners_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        partner_service.BatchUpdatePartnersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.PartnerServiceClient.batch_update_partners",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "BatchUpdatePartners",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPartner(
        _BasePartnerServiceRestTransport._BaseGetPartner, PartnerServiceRestStub
    ):
        def __hash__(self):
            return hash("PartnerServiceRestTransport.GetPartner")

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
            request: partner_service.GetPartnerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_messages.Partner:
            r"""Call the get partner method over HTTP.

            Args:
                request (~.partner_service.GetPartnerRequest):
                    The request object. Request object for ``GetPartner`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_messages.Partner:
                    The [Partner][google.ads.admanager.v1.Partner] resource.

                Represents a publishing partner with established
                agreements to share inventory and revenue based on
                assignments.

                For more information, see [Add publishing partner
                assignments]
                (https://support.google.com/admanager/answer/7032752).

            """

            http_options = (
                _BasePartnerServiceRestTransport._BaseGetPartner._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_partner(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerServiceRestTransport._BaseGetPartner,
                    "_BaseGetPartner__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PartnerServiceClient.GetPartner",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "GetPartner",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerServiceRestTransport._GetPartner._get_response(
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
            resp = partner_messages.Partner()
            pb_resp = partner_messages.Partner.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_partner(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_partner_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = partner_messages.Partner.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.PartnerServiceClient.get_partner",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "GetPartner",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPartners(
        _BasePartnerServiceRestTransport._BaseListPartners, PartnerServiceRestStub
    ):
        def __hash__(self):
            return hash("PartnerServiceRestTransport.ListPartners")

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
            request: partner_service.ListPartnersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_service.ListPartnersResponse:
            r"""Call the list partners method over HTTP.

            Args:
                request (~.partner_service.ListPartnersRequest):
                    The request object. Request object for ``ListPartners`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_service.ListPartnersResponse:
                    Response object for ``ListPartnersRequest`` containing
                matching [Partner][google.ads.admanager.v1.Partner]
                objects.

            """

            http_options = (
                _BasePartnerServiceRestTransport._BaseListPartners._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_partners(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerServiceRestTransport._BaseListPartners,
                    "_BaseListPartners__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PartnerServiceClient.ListPartners",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "ListPartners",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerServiceRestTransport._ListPartners._get_response(
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
            resp = partner_service.ListPartnersResponse()
            pb_resp = partner_service.ListPartnersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_partners(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_partners_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = partner_service.ListPartnersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PartnerServiceClient.list_partners",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "ListPartners",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePartner(
        _BasePartnerServiceRestTransport._BaseUpdatePartner, PartnerServiceRestStub
    ):
        def __hash__(self):
            return hash("PartnerServiceRestTransport.UpdatePartner")

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
            request: partner_service.UpdatePartnerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_messages.Partner:
            r"""Call the update partner method over HTTP.

            Args:
                request (~.partner_service.UpdatePartnerRequest):
                    The request object. Request object for ``UpdatePartner`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_messages.Partner:
                    The [Partner][google.ads.admanager.v1.Partner] resource.

                Represents a publishing partner with established
                agreements to share inventory and revenue based on
                assignments.

                For more information, see [Add publishing partner
                assignments]
                (https://support.google.com/admanager/answer/7032752).

            """

            http_options = (
                _BasePartnerServiceRestTransport._BaseUpdatePartner._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_partner(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerServiceRestTransport._BaseUpdatePartner,
                    "_BaseUpdatePartner__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PartnerServiceClient.UpdatePartner",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "UpdatePartner",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerServiceRestTransport._UpdatePartner._get_response(
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
            resp = partner_messages.Partner()
            pb_resp = partner_messages.Partner.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_partner(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_partner_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = partner_messages.Partner.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.PartnerServiceClient.update_partner",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "UpdatePartner",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_update_partners(
        self,
    ) -> Callable[
        [partner_service.BatchUpdatePartnersRequest],
        partner_service.BatchUpdatePartnersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdatePartners(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_partner(
        self,
    ) -> Callable[[partner_service.GetPartnerRequest], partner_messages.Partner]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPartner(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_partners(
        self,
    ) -> Callable[
        [partner_service.ListPartnersRequest], partner_service.ListPartnersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPartners(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_partner(
        self,
    ) -> Callable[[partner_service.UpdatePartnerRequest], partner_messages.Partner]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePartner(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BasePartnerServiceRestTransport._BaseCancelOperation, PartnerServiceRestStub
    ):
        def __hash__(self):
            return hash("PartnerServiceRestTransport.CancelOperation")

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

            http_options = _BasePartnerServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.PartnerServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BasePartnerServiceRestTransport._BaseGetOperation, PartnerServiceRestStub
    ):
        def __hash__(self):
            return hash("PartnerServiceRestTransport.GetOperation")

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
                _BasePartnerServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePartnerServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.PartnerServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PartnerServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.PartnerServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PartnerService",
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


__all__ = ("PartnerServiceRestTransport",)
