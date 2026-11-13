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

from google.cloud.support_v2._compat import transcode_request
from google.cloud.support_v2.types import case, case_service
from google.cloud.support_v2.types import case as gcs_case

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCaseServiceRestTransport

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


class CaseServiceRestInterceptor:
    """Interceptor for CaseService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CaseServiceRestTransport.

    .. code-block:: python
        class MyCustomCaseServiceInterceptor(CaseServiceRestInterceptor):
            def pre_close_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_close_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_escalate_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_escalate_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_case(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_cases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_case_classifications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_case_classifications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_cases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_cases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_case(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_case(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CaseServiceRestTransport(interceptor=MyCustomCaseServiceInterceptor())
        client = CaseServiceClient(transport=transport)


    """

    def pre_close_case(
        self,
        request: case_service.CloseCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[case_service.CloseCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for close_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_close_case(self, response: case.Case) -> case.Case:
        """Post-rpc interceptor for close_case

        DEPRECATED. Please use the `post_close_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_close_case` interceptor runs
        before the `post_close_case_with_metadata` interceptor.
        """
        return response

    def post_close_case_with_metadata(
        self, response: case.Case, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[case.Case, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for close_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_close_case_with_metadata`
        interceptor in new development instead of the `post_close_case` interceptor.
        When both interceptors are used, this `post_close_case_with_metadata` interceptor runs after the
        `post_close_case` interceptor. The (possibly modified) response returned by
        `post_close_case` will be passed to
        `post_close_case_with_metadata`.
        """
        return response, metadata

    def pre_create_case(
        self,
        request: case_service.CreateCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[case_service.CreateCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_create_case(self, response: gcs_case.Case) -> gcs_case.Case:
        """Post-rpc interceptor for create_case

        DEPRECATED. Please use the `post_create_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_create_case` interceptor runs
        before the `post_create_case_with_metadata` interceptor.
        """
        return response

    def post_create_case_with_metadata(
        self, response: gcs_case.Case, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcs_case.Case, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_create_case_with_metadata`
        interceptor in new development instead of the `post_create_case` interceptor.
        When both interceptors are used, this `post_create_case_with_metadata` interceptor runs after the
        `post_create_case` interceptor. The (possibly modified) response returned by
        `post_create_case` will be passed to
        `post_create_case_with_metadata`.
        """
        return response, metadata

    def pre_escalate_case(
        self,
        request: case_service.EscalateCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        case_service.EscalateCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for escalate_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_escalate_case(self, response: case.Case) -> case.Case:
        """Post-rpc interceptor for escalate_case

        DEPRECATED. Please use the `post_escalate_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_escalate_case` interceptor runs
        before the `post_escalate_case_with_metadata` interceptor.
        """
        return response

    def post_escalate_case_with_metadata(
        self, response: case.Case, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[case.Case, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for escalate_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_escalate_case_with_metadata`
        interceptor in new development instead of the `post_escalate_case` interceptor.
        When both interceptors are used, this `post_escalate_case_with_metadata` interceptor runs after the
        `post_escalate_case` interceptor. The (possibly modified) response returned by
        `post_escalate_case` will be passed to
        `post_escalate_case_with_metadata`.
        """
        return response, metadata

    def pre_get_case(
        self,
        request: case_service.GetCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[case_service.GetCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_get_case(self, response: case.Case) -> case.Case:
        """Post-rpc interceptor for get_case

        DEPRECATED. Please use the `post_get_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_get_case` interceptor runs
        before the `post_get_case_with_metadata` interceptor.
        """
        return response

    def post_get_case_with_metadata(
        self, response: case.Case, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[case.Case, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_get_case_with_metadata`
        interceptor in new development instead of the `post_get_case` interceptor.
        When both interceptors are used, this `post_get_case_with_metadata` interceptor runs after the
        `post_get_case` interceptor. The (possibly modified) response returned by
        `post_get_case` will be passed to
        `post_get_case_with_metadata`.
        """
        return response, metadata

    def pre_list_cases(
        self,
        request: case_service.ListCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[case_service.ListCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_list_cases(
        self, response: case_service.ListCasesResponse
    ) -> case_service.ListCasesResponse:
        """Post-rpc interceptor for list_cases

        DEPRECATED. Please use the `post_list_cases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_list_cases` interceptor runs
        before the `post_list_cases_with_metadata` interceptor.
        """
        return response

    def post_list_cases_with_metadata(
        self,
        response: case_service.ListCasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[case_service.ListCasesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_cases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_list_cases_with_metadata`
        interceptor in new development instead of the `post_list_cases` interceptor.
        When both interceptors are used, this `post_list_cases_with_metadata` interceptor runs after the
        `post_list_cases` interceptor. The (possibly modified) response returned by
        `post_list_cases` will be passed to
        `post_list_cases_with_metadata`.
        """
        return response, metadata

    def pre_search_case_classifications(
        self,
        request: case_service.SearchCaseClassificationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        case_service.SearchCaseClassificationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_case_classifications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_search_case_classifications(
        self, response: case_service.SearchCaseClassificationsResponse
    ) -> case_service.SearchCaseClassificationsResponse:
        """Post-rpc interceptor for search_case_classifications

        DEPRECATED. Please use the `post_search_case_classifications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_search_case_classifications` interceptor runs
        before the `post_search_case_classifications_with_metadata` interceptor.
        """
        return response

    def post_search_case_classifications_with_metadata(
        self,
        response: case_service.SearchCaseClassificationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        case_service.SearchCaseClassificationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_case_classifications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_search_case_classifications_with_metadata`
        interceptor in new development instead of the `post_search_case_classifications` interceptor.
        When both interceptors are used, this `post_search_case_classifications_with_metadata` interceptor runs after the
        `post_search_case_classifications` interceptor. The (possibly modified) response returned by
        `post_search_case_classifications` will be passed to
        `post_search_case_classifications_with_metadata`.
        """
        return response, metadata

    def pre_search_cases(
        self,
        request: case_service.SearchCasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        case_service.SearchCasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_cases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_search_cases(
        self, response: case_service.SearchCasesResponse
    ) -> case_service.SearchCasesResponse:
        """Post-rpc interceptor for search_cases

        DEPRECATED. Please use the `post_search_cases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_search_cases` interceptor runs
        before the `post_search_cases_with_metadata` interceptor.
        """
        return response

    def post_search_cases_with_metadata(
        self,
        response: case_service.SearchCasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        case_service.SearchCasesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for search_cases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_search_cases_with_metadata`
        interceptor in new development instead of the `post_search_cases` interceptor.
        When both interceptors are used, this `post_search_cases_with_metadata` interceptor runs after the
        `post_search_cases` interceptor. The (possibly modified) response returned by
        `post_search_cases` will be passed to
        `post_search_cases_with_metadata`.
        """
        return response, metadata

    def pre_update_case(
        self,
        request: case_service.UpdateCaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[case_service.UpdateCaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_case

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CaseService server.
        """
        return request, metadata

    def post_update_case(self, response: gcs_case.Case) -> gcs_case.Case:
        """Post-rpc interceptor for update_case

        DEPRECATED. Please use the `post_update_case_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CaseService server but before
        it is returned to user code. This `post_update_case` interceptor runs
        before the `post_update_case_with_metadata` interceptor.
        """
        return response

    def post_update_case_with_metadata(
        self, response: gcs_case.Case, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcs_case.Case, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_case

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CaseService server but before it is returned to user code.

        We recommend only using this `post_update_case_with_metadata`
        interceptor in new development instead of the `post_update_case` interceptor.
        When both interceptors are used, this `post_update_case_with_metadata` interceptor runs after the
        `post_update_case` interceptor. The (possibly modified) response returned by
        `post_update_case` will be passed to
        `post_update_case_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class CaseServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CaseServiceRestInterceptor


class CaseServiceRestTransport(_BaseCaseServiceRestTransport):
    """REST backend synchronous transport for CaseService.

    A service to manage Google Cloud support cases.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudsupport.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CaseServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudsupport.googleapis.com').
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
            interceptor (Optional[CaseServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CaseServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CloseCase(_BaseCaseServiceRestTransport._BaseCloseCase, CaseServiceRestStub):
        def __hash__(self):
            return hash("CaseServiceRestTransport.CloseCase")

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
            request: case_service.CloseCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> case.Case:
            r"""Call the close case method over HTTP.

            Args:
                request (~.case_service.CloseCaseRequest):
                    The request object. The request message for the CloseCase
                endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.case.Case:
                    A Case is an object that contains the details of a
                support case. It contains fields for the time it was
                created, its priority, its classification, and more.
                Cases can also have comments and attachments that get
                added over time.

                A case is parented by a Google Cloud organization or
                project.

                Organizations are identified by a number, so the name of
                a case parented by an organization would look like this:

                ::

                   organizations/123/cases/456

                Projects have two unique identifiers, an ID and a
                number, and they look like this:

                ::

                   projects/abc/cases/456

                ::

                   projects/123/cases/456

                You can use either of them when calling the API. To
                learn more about project identifiers, see
                `AIP-2510 <https://google.aip.dev/cloud/2510>`__.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseCloseCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_close_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseCloseCase,
                    "_BaseCloseCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.CloseCase",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "CloseCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._CloseCase._get_response(
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
            resp = case.Case()
            pb_resp = case.Case.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_close_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_close_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = case.Case.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.close_case",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "CloseCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCase(
        _BaseCaseServiceRestTransport._BaseCreateCase, CaseServiceRestStub
    ):
        def __hash__(self):
            return hash("CaseServiceRestTransport.CreateCase")

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
            request: case_service.CreateCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_case.Case:
            r"""Call the create case method over HTTP.

            Args:
                request (~.case_service.CreateCaseRequest):
                    The request object. The request message for the
                CreateCase endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_case.Case:
                    A Case is an object that contains the details of a
                support case. It contains fields for the time it was
                created, its priority, its classification, and more.
                Cases can also have comments and attachments that get
                added over time.

                A case is parented by a Google Cloud organization or
                project.

                Organizations are identified by a number, so the name of
                a case parented by an organization would look like this:

                ::

                   organizations/123/cases/456

                Projects have two unique identifiers, an ID and a
                number, and they look like this:

                ::

                   projects/abc/cases/456

                ::

                   projects/123/cases/456

                You can use either of them when calling the API. To
                learn more about project identifiers, see
                `AIP-2510 <https://google.aip.dev/cloud/2510>`__.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseCreateCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseCreateCase,
                    "_BaseCreateCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.CreateCase",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "CreateCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._CreateCase._get_response(
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
            resp = gcs_case.Case()
            pb_resp = gcs_case.Case.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_case.Case.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.create_case",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "CreateCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EscalateCase(
        _BaseCaseServiceRestTransport._BaseEscalateCase, CaseServiceRestStub
    ):
        def __hash__(self):
            return hash("CaseServiceRestTransport.EscalateCase")

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
            request: case_service.EscalateCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> case.Case:
            r"""Call the escalate case method over HTTP.

            Args:
                request (~.case_service.EscalateCaseRequest):
                    The request object. The request message for the
                EscalateCase endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.case.Case:
                    A Case is an object that contains the details of a
                support case. It contains fields for the time it was
                created, its priority, its classification, and more.
                Cases can also have comments and attachments that get
                added over time.

                A case is parented by a Google Cloud organization or
                project.

                Organizations are identified by a number, so the name of
                a case parented by an organization would look like this:

                ::

                   organizations/123/cases/456

                Projects have two unique identifiers, an ID and a
                number, and they look like this:

                ::

                   projects/abc/cases/456

                ::

                   projects/123/cases/456

                You can use either of them when calling the API. To
                learn more about project identifiers, see
                `AIP-2510 <https://google.aip.dev/cloud/2510>`__.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseEscalateCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_escalate_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseEscalateCase,
                    "_BaseEscalateCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.EscalateCase",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "EscalateCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._EscalateCase._get_response(
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
            resp = case.Case()
            pb_resp = case.Case.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_escalate_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_escalate_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = case.Case.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.escalate_case",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "EscalateCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCase(_BaseCaseServiceRestTransport._BaseGetCase, CaseServiceRestStub):
        def __hash__(self):
            return hash("CaseServiceRestTransport.GetCase")

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
            request: case_service.GetCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> case.Case:
            r"""Call the get case method over HTTP.

            Args:
                request (~.case_service.GetCaseRequest):
                    The request object. The request message for the GetCase
                endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.case.Case:
                    A Case is an object that contains the details of a
                support case. It contains fields for the time it was
                created, its priority, its classification, and more.
                Cases can also have comments and attachments that get
                added over time.

                A case is parented by a Google Cloud organization or
                project.

                Organizations are identified by a number, so the name of
                a case parented by an organization would look like this:

                ::

                   organizations/123/cases/456

                Projects have two unique identifiers, an ID and a
                number, and they look like this:

                ::

                   projects/abc/cases/456

                ::

                   projects/123/cases/456

                You can use either of them when calling the API. To
                learn more about project identifiers, see
                `AIP-2510 <https://google.aip.dev/cloud/2510>`__.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseGetCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseGetCase,
                    "_BaseGetCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.GetCase",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "GetCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._GetCase._get_response(
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
            resp = case.Case()
            pb_resp = case.Case.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = case.Case.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.get_case",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "GetCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCases(_BaseCaseServiceRestTransport._BaseListCases, CaseServiceRestStub):
        def __hash__(self):
            return hash("CaseServiceRestTransport.ListCases")

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
            request: case_service.ListCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> case_service.ListCasesResponse:
            r"""Call the list cases method over HTTP.

            Args:
                request (~.case_service.ListCasesRequest):
                    The request object. The request message for the ListCases
                endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.case_service.ListCasesResponse:
                    The response message for the
                ListCases endpoint.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseListCases._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_cases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseListCases,
                    "_BaseListCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.ListCases",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "ListCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._ListCases._get_response(
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
            resp = case_service.ListCasesResponse()
            pb_resp = case_service.ListCasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_cases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_cases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = case_service.ListCasesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.list_cases",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "ListCases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchCaseClassifications(
        _BaseCaseServiceRestTransport._BaseSearchCaseClassifications,
        CaseServiceRestStub,
    ):
        def __hash__(self):
            return hash("CaseServiceRestTransport.SearchCaseClassifications")

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
            request: case_service.SearchCaseClassificationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> case_service.SearchCaseClassificationsResponse:
            r"""Call the search case
            classifications method over HTTP.

                Args:
                    request (~.case_service.SearchCaseClassificationsRequest):
                        The request object. The request message for the
                    SearchCaseClassifications endpoint.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.case_service.SearchCaseClassificationsResponse:
                        The response message for
                    SearchCaseClassifications endpoint.

            """

            http_options = _BaseCaseServiceRestTransport._BaseSearchCaseClassifications._get_http_options()
            request, metadata = self._interceptor.pre_search_case_classifications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseSearchCaseClassifications,
                    "_BaseSearchCaseClassifications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.SearchCaseClassifications",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "SearchCaseClassifications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CaseServiceRestTransport._SearchCaseClassifications._get_response(
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
            resp = case_service.SearchCaseClassificationsResponse()
            pb_resp = case_service.SearchCaseClassificationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_case_classifications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_case_classifications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        case_service.SearchCaseClassificationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.search_case_classifications",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "SearchCaseClassifications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchCases(
        _BaseCaseServiceRestTransport._BaseSearchCases, CaseServiceRestStub
    ):
        def __hash__(self):
            return hash("CaseServiceRestTransport.SearchCases")

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
            request: case_service.SearchCasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> case_service.SearchCasesResponse:
            r"""Call the search cases method over HTTP.

            Args:
                request (~.case_service.SearchCasesRequest):
                    The request object. The request message for the
                SearchCases endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.case_service.SearchCasesResponse:
                    The response message for the
                SearchCases endpoint.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseSearchCases._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_cases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseSearchCases,
                    "_BaseSearchCases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.SearchCases",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "SearchCases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._SearchCases._get_response(
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
            resp = case_service.SearchCasesResponse()
            pb_resp = case_service.SearchCasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_cases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_cases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = case_service.SearchCasesResponse.to_json(
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
                    "Received response for google.cloud.support_v2.CaseServiceClient.search_cases",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "SearchCases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCase(
        _BaseCaseServiceRestTransport._BaseUpdateCase, CaseServiceRestStub
    ):
        def __hash__(self):
            return hash("CaseServiceRestTransport.UpdateCase")

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
            request: case_service.UpdateCaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_case.Case:
            r"""Call the update case method over HTTP.

            Args:
                request (~.case_service.UpdateCaseRequest):
                    The request object. The request message for the
                UpdateCase endpoint
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_case.Case:
                    A Case is an object that contains the details of a
                support case. It contains fields for the time it was
                created, its priority, its classification, and more.
                Cases can also have comments and attachments that get
                added over time.

                A case is parented by a Google Cloud organization or
                project.

                Organizations are identified by a number, so the name of
                a case parented by an organization would look like this:

                ::

                   organizations/123/cases/456

                Projects have two unique identifiers, an ID and a
                number, and they look like this:

                ::

                   projects/abc/cases/456

                ::

                   projects/123/cases/456

                You can use either of them when calling the API. To
                learn more about project identifiers, see
                `AIP-2510 <https://google.aip.dev/cloud/2510>`__.

            """

            http_options = (
                _BaseCaseServiceRestTransport._BaseUpdateCase._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_case(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCaseServiceRestTransport._BaseUpdateCase,
                    "_BaseUpdateCase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.CaseServiceClient.UpdateCase",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "UpdateCase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CaseServiceRestTransport._UpdateCase._get_response(
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
            resp = gcs_case.Case()
            pb_resp = gcs_case.Case.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_case(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_case_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_case.Case.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.support_v2.CaseServiceClient.update_case",
                    extra={
                        "serviceName": "google.cloud.support.v2.CaseService",
                        "rpcName": "UpdateCase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def close_case(self) -> Callable[[case_service.CloseCaseRequest], case.Case]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CloseCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_case(self) -> Callable[[case_service.CreateCaseRequest], gcs_case.Case]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def escalate_case(self) -> Callable[[case_service.EscalateCaseRequest], case.Case]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EscalateCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_case(self) -> Callable[[case_service.GetCaseRequest], case.Case]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_cases(
        self,
    ) -> Callable[[case_service.ListCasesRequest], case_service.ListCasesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_case_classifications(
        self,
    ) -> Callable[
        [case_service.SearchCaseClassificationsRequest],
        case_service.SearchCaseClassificationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchCaseClassifications(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_cases(
        self,
    ) -> Callable[[case_service.SearchCasesRequest], case_service.SearchCasesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchCases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_case(self) -> Callable[[case_service.UpdateCaseRequest], gcs_case.Case]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("CaseServiceRestTransport",)
