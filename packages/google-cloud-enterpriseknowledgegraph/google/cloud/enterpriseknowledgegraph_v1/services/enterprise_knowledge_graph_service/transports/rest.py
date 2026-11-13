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

from google.cloud.enterpriseknowledgegraph_v1._compat import transcode_request
from google.cloud.enterpriseknowledgegraph_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseEnterpriseKnowledgeGraphServiceRestTransport

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


class EnterpriseKnowledgeGraphServiceRestInterceptor:
    """Interceptor for EnterpriseKnowledgeGraphService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EnterpriseKnowledgeGraphServiceRestTransport.

    .. code-block:: python
        class MyCustomEnterpriseKnowledgeGraphServiceInterceptor(EnterpriseKnowledgeGraphServiceRestInterceptor):
            def pre_cancel_entity_reconciliation_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_create_entity_reconciliation_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_entity_reconciliation_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_entity_reconciliation_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_entity_reconciliation_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_entity_reconciliation_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_entity_reconciliation_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_entity_reconciliation_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_public_kg(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_public_kg(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_public_kg(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_public_kg(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EnterpriseKnowledgeGraphServiceRestTransport(interceptor=MyCustomEnterpriseKnowledgeGraphServiceInterceptor())
        client = EnterpriseKnowledgeGraphServiceClient(transport=transport)


    """

    def pre_cancel_entity_reconciliation_job(
        self,
        request: service.CancelEntityReconciliationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CancelEntityReconciliationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for cancel_entity_reconciliation_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def pre_create_entity_reconciliation_job(
        self,
        request: service.CreateEntityReconciliationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateEntityReconciliationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_entity_reconciliation_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_create_entity_reconciliation_job(
        self, response: service.EntityReconciliationJob
    ) -> service.EntityReconciliationJob:
        """Post-rpc interceptor for create_entity_reconciliation_job

        DEPRECATED. Please use the `post_create_entity_reconciliation_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_create_entity_reconciliation_job` interceptor runs
        before the `post_create_entity_reconciliation_job_with_metadata` interceptor.
        """
        return response

    def post_create_entity_reconciliation_job_with_metadata(
        self,
        response: service.EntityReconciliationJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.EntityReconciliationJob, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_entity_reconciliation_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_create_entity_reconciliation_job_with_metadata`
        interceptor in new development instead of the `post_create_entity_reconciliation_job` interceptor.
        When both interceptors are used, this `post_create_entity_reconciliation_job_with_metadata` interceptor runs after the
        `post_create_entity_reconciliation_job` interceptor. The (possibly modified) response returned by
        `post_create_entity_reconciliation_job` will be passed to
        `post_create_entity_reconciliation_job_with_metadata`.
        """
        return response, metadata

    def pre_delete_entity_reconciliation_job(
        self,
        request: service.DeleteEntityReconciliationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteEntityReconciliationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_entity_reconciliation_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def pre_get_entity_reconciliation_job(
        self,
        request: service.GetEntityReconciliationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetEntityReconciliationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_entity_reconciliation_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_get_entity_reconciliation_job(
        self, response: service.EntityReconciliationJob
    ) -> service.EntityReconciliationJob:
        """Post-rpc interceptor for get_entity_reconciliation_job

        DEPRECATED. Please use the `post_get_entity_reconciliation_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_get_entity_reconciliation_job` interceptor runs
        before the `post_get_entity_reconciliation_job_with_metadata` interceptor.
        """
        return response

    def post_get_entity_reconciliation_job_with_metadata(
        self,
        response: service.EntityReconciliationJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.EntityReconciliationJob, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_entity_reconciliation_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_get_entity_reconciliation_job_with_metadata`
        interceptor in new development instead of the `post_get_entity_reconciliation_job` interceptor.
        When both interceptors are used, this `post_get_entity_reconciliation_job_with_metadata` interceptor runs after the
        `post_get_entity_reconciliation_job` interceptor. The (possibly modified) response returned by
        `post_get_entity_reconciliation_job` will be passed to
        `post_get_entity_reconciliation_job_with_metadata`.
        """
        return response, metadata

    def pre_list_entity_reconciliation_jobs(
        self,
        request: service.ListEntityReconciliationJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListEntityReconciliationJobsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_entity_reconciliation_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_list_entity_reconciliation_jobs(
        self, response: service.ListEntityReconciliationJobsResponse
    ) -> service.ListEntityReconciliationJobsResponse:
        """Post-rpc interceptor for list_entity_reconciliation_jobs

        DEPRECATED. Please use the `post_list_entity_reconciliation_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_list_entity_reconciliation_jobs` interceptor runs
        before the `post_list_entity_reconciliation_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_entity_reconciliation_jobs_with_metadata(
        self,
        response: service.ListEntityReconciliationJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListEntityReconciliationJobsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_entity_reconciliation_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_list_entity_reconciliation_jobs_with_metadata`
        interceptor in new development instead of the `post_list_entity_reconciliation_jobs` interceptor.
        When both interceptors are used, this `post_list_entity_reconciliation_jobs_with_metadata` interceptor runs after the
        `post_list_entity_reconciliation_jobs` interceptor. The (possibly modified) response returned by
        `post_list_entity_reconciliation_jobs` will be passed to
        `post_list_entity_reconciliation_jobs_with_metadata`.
        """
        return response, metadata

    def pre_lookup(
        self,
        request: service.LookupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.LookupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for lookup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_lookup(self, response: service.LookupResponse) -> service.LookupResponse:
        """Post-rpc interceptor for lookup

        DEPRECATED. Please use the `post_lookup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_lookup` interceptor runs
        before the `post_lookup_with_metadata` interceptor.
        """
        return response

    def post_lookup_with_metadata(
        self,
        response: service.LookupResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.LookupResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for lookup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_lookup_with_metadata`
        interceptor in new development instead of the `post_lookup` interceptor.
        When both interceptors are used, this `post_lookup_with_metadata` interceptor runs after the
        `post_lookup` interceptor. The (possibly modified) response returned by
        `post_lookup` will be passed to
        `post_lookup_with_metadata`.
        """
        return response, metadata

    def pre_lookup_public_kg(
        self,
        request: service.LookupPublicKgRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.LookupPublicKgRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for lookup_public_kg

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_lookup_public_kg(
        self, response: service.LookupPublicKgResponse
    ) -> service.LookupPublicKgResponse:
        """Post-rpc interceptor for lookup_public_kg

        DEPRECATED. Please use the `post_lookup_public_kg_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_lookup_public_kg` interceptor runs
        before the `post_lookup_public_kg_with_metadata` interceptor.
        """
        return response

    def post_lookup_public_kg_with_metadata(
        self,
        response: service.LookupPublicKgResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.LookupPublicKgResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for lookup_public_kg

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_lookup_public_kg_with_metadata`
        interceptor in new development instead of the `post_lookup_public_kg` interceptor.
        When both interceptors are used, this `post_lookup_public_kg_with_metadata` interceptor runs after the
        `post_lookup_public_kg` interceptor. The (possibly modified) response returned by
        `post_lookup_public_kg` will be passed to
        `post_lookup_public_kg_with_metadata`.
        """
        return response, metadata

    def pre_search(
        self,
        request: service.SearchRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.SearchRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_search(self, response: service.SearchResponse) -> service.SearchResponse:
        """Post-rpc interceptor for search

        DEPRECATED. Please use the `post_search_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_search` interceptor runs
        before the `post_search_with_metadata` interceptor.
        """
        return response

    def post_search_with_metadata(
        self,
        response: service.SearchResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.SearchResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_search_with_metadata`
        interceptor in new development instead of the `post_search` interceptor.
        When both interceptors are used, this `post_search_with_metadata` interceptor runs after the
        `post_search` interceptor. The (possibly modified) response returned by
        `post_search` will be passed to
        `post_search_with_metadata`.
        """
        return response, metadata

    def pre_search_public_kg(
        self,
        request: service.SearchPublicKgRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.SearchPublicKgRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_public_kg

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EnterpriseKnowledgeGraphService server.
        """
        return request, metadata

    def post_search_public_kg(
        self, response: service.SearchPublicKgResponse
    ) -> service.SearchPublicKgResponse:
        """Post-rpc interceptor for search_public_kg

        DEPRECATED. Please use the `post_search_public_kg_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EnterpriseKnowledgeGraphService server but before
        it is returned to user code. This `post_search_public_kg` interceptor runs
        before the `post_search_public_kg_with_metadata` interceptor.
        """
        return response

    def post_search_public_kg_with_metadata(
        self,
        response: service.SearchPublicKgResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.SearchPublicKgResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_public_kg

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EnterpriseKnowledgeGraphService server but before it is returned to user code.

        We recommend only using this `post_search_public_kg_with_metadata`
        interceptor in new development instead of the `post_search_public_kg` interceptor.
        When both interceptors are used, this `post_search_public_kg_with_metadata` interceptor runs after the
        `post_search_public_kg` interceptor. The (possibly modified) response returned by
        `post_search_public_kg` will be passed to
        `post_search_public_kg_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class EnterpriseKnowledgeGraphServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EnterpriseKnowledgeGraphServiceRestInterceptor


class EnterpriseKnowledgeGraphServiceRestTransport(
    _BaseEnterpriseKnowledgeGraphServiceRestTransport
):
    """REST backend synchronous transport for EnterpriseKnowledgeGraphService.

    APIs for enterprise knowledge graph product.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "enterpriseknowledgegraph.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[EnterpriseKnowledgeGraphServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'enterpriseknowledgegraph.googleapis.com').
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
            interceptor (Optional[EnterpriseKnowledgeGraphServiceRestInterceptor]): Interceptor used
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
        self._interceptor = (
            interceptor or EnterpriseKnowledgeGraphServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CancelEntityReconciliationJob(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseCancelEntityReconciliationJob,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EnterpriseKnowledgeGraphServiceRestTransport.CancelEntityReconciliationJob"
            )

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
            request: service.CancelEntityReconciliationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the cancel entity
            reconciliation job method over HTTP.

                Args:
                    request (~.service.CancelEntityReconciliationJobRequest):
                        The request object. Request message for
                    CancelEntityReconciliationJob.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseCancelEntityReconciliationJob._get_http_options()
            request, metadata = self._interceptor.pre_cancel_entity_reconciliation_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseCancelEntityReconciliationJob,
                    "_BaseCancelEntityReconciliationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.CancelEntityReconciliationJob",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "CancelEntityReconciliationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._CancelEntityReconciliationJob._get_response(
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

    class _CreateEntityReconciliationJob(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseCreateEntityReconciliationJob,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EnterpriseKnowledgeGraphServiceRestTransport.CreateEntityReconciliationJob"
            )

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
            request: service.CreateEntityReconciliationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.EntityReconciliationJob:
            r"""Call the create entity
            reconciliation job method over HTTP.

                Args:
                    request (~.service.CreateEntityReconciliationJobRequest):
                        The request object. Request message for
                    CreateEntityReconciliationJob.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.EntityReconciliationJob:
                        Entity reconciliation job message.
            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseCreateEntityReconciliationJob._get_http_options()
            request, metadata = self._interceptor.pre_create_entity_reconciliation_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseCreateEntityReconciliationJob,
                    "_BaseCreateEntityReconciliationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.CreateEntityReconciliationJob",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "CreateEntityReconciliationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._CreateEntityReconciliationJob._get_response(
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
            resp = service.EntityReconciliationJob()
            pb_resp = service.EntityReconciliationJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_entity_reconciliation_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_entity_reconciliation_job_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.EntityReconciliationJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.create_entity_reconciliation_job",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "CreateEntityReconciliationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEntityReconciliationJob(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseDeleteEntityReconciliationJob,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EnterpriseKnowledgeGraphServiceRestTransport.DeleteEntityReconciliationJob"
            )

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
            request: service.DeleteEntityReconciliationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete entity
            reconciliation job method over HTTP.

                Args:
                    request (~.service.DeleteEntityReconciliationJobRequest):
                        The request object. Request message for
                    DeleteEntityReconciliationJob.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseDeleteEntityReconciliationJob._get_http_options()
            request, metadata = self._interceptor.pre_delete_entity_reconciliation_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseDeleteEntityReconciliationJob,
                    "_BaseDeleteEntityReconciliationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.DeleteEntityReconciliationJob",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "DeleteEntityReconciliationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._DeleteEntityReconciliationJob._get_response(
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

    class _GetEntityReconciliationJob(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseGetEntityReconciliationJob,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EnterpriseKnowledgeGraphServiceRestTransport.GetEntityReconciliationJob"
            )

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
            request: service.GetEntityReconciliationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.EntityReconciliationJob:
            r"""Call the get entity reconciliation
            job method over HTTP.

                Args:
                    request (~.service.GetEntityReconciliationJobRequest):
                        The request object. Request message for
                    GetEntityReconciliationJob.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.EntityReconciliationJob:
                        Entity reconciliation job message.
            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseGetEntityReconciliationJob._get_http_options()
            request, metadata = self._interceptor.pre_get_entity_reconciliation_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseGetEntityReconciliationJob,
                    "_BaseGetEntityReconciliationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.GetEntityReconciliationJob",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "GetEntityReconciliationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._GetEntityReconciliationJob._get_response(
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
            resp = service.EntityReconciliationJob()
            pb_resp = service.EntityReconciliationJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_entity_reconciliation_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_entity_reconciliation_job_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.EntityReconciliationJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.get_entity_reconciliation_job",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "GetEntityReconciliationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEntityReconciliationJobs(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseListEntityReconciliationJobs,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EnterpriseKnowledgeGraphServiceRestTransport.ListEntityReconciliationJobs"
            )

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
            request: service.ListEntityReconciliationJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListEntityReconciliationJobsResponse:
            r"""Call the list entity
            reconciliation jobs method over HTTP.

                Args:
                    request (~.service.ListEntityReconciliationJobsRequest):
                        The request object. Request message for
                    [EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ListEntityReconciliationJobsResponse:
                        Response message for
                    [EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs].

            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseListEntityReconciliationJobs._get_http_options()
            request, metadata = self._interceptor.pre_list_entity_reconciliation_jobs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseListEntityReconciliationJobs,
                    "_BaseListEntityReconciliationJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.ListEntityReconciliationJobs",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "ListEntityReconciliationJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._ListEntityReconciliationJobs._get_response(
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
            resp = service.ListEntityReconciliationJobsResponse()
            pb_resp = service.ListEntityReconciliationJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_entity_reconciliation_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_entity_reconciliation_jobs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ListEntityReconciliationJobsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.list_entity_reconciliation_jobs",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "ListEntityReconciliationJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Lookup(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseLookup,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash("EnterpriseKnowledgeGraphServiceRestTransport.Lookup")

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
            request: service.LookupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.LookupResponse:
            r"""Call the lookup method over HTTP.

            Args:
                request (~.service.LookupRequest):
                    The request object. Request message for
                [EnterpriseKnowledgeGraphService.Lookup][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.LookupResponse:
                    Response message for
                [EnterpriseKnowledgeGraphService.Lookup][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup].

            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseLookup._get_http_options()
            request, metadata = self._interceptor.pre_lookup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseLookup,
                    "_BaseLookup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.Lookup",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "Lookup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnterpriseKnowledgeGraphServiceRestTransport._Lookup._get_response(
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
            resp = service.LookupResponse()
            pb_resp = service.LookupResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.LookupResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.lookup",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "Lookup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupPublicKg(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseLookupPublicKg,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash("EnterpriseKnowledgeGraphServiceRestTransport.LookupPublicKg")

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
            request: service.LookupPublicKgRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.LookupPublicKgResponse:
            r"""Call the lookup public kg method over HTTP.

            Args:
                request (~.service.LookupPublicKgRequest):
                    The request object. Request message for
                [EnterpriseKnowledgeGraphService.LookupPublicKg][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.LookupPublicKg].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.LookupPublicKgResponse:
                    Response message for
                [EnterpriseKnowledgeGraphService.LookupPublicKg][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.LookupPublicKg].

            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseLookupPublicKg._get_http_options()
            request, metadata = self._interceptor.pre_lookup_public_kg(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseLookupPublicKg,
                    "_BaseLookupPublicKg__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.LookupPublicKg",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "LookupPublicKg",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._LookupPublicKg._get_response(
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
            resp = service.LookupPublicKgResponse()
            pb_resp = service.LookupPublicKgResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_public_kg(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_public_kg_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.LookupPublicKgResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.lookup_public_kg",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "LookupPublicKg",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Search(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseSearch,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash("EnterpriseKnowledgeGraphServiceRestTransport.Search")

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
            request: service.SearchRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.SearchResponse:
            r"""Call the search method over HTTP.

            Args:
                request (~.service.SearchRequest):
                    The request object. Request message for
                [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.SearchResponse:
                    Response message for
                [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].

            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseSearch._get_http_options()
            request, metadata = self._interceptor.pre_search(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseSearch,
                    "_BaseSearch__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.Search",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "Search",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnterpriseKnowledgeGraphServiceRestTransport._Search._get_response(
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
            resp = service.SearchResponse()
            pb_resp = service.SearchResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.SearchResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.search",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "Search",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchPublicKg(
        _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseSearchPublicKg,
        EnterpriseKnowledgeGraphServiceRestStub,
    ):
        def __hash__(self):
            return hash("EnterpriseKnowledgeGraphServiceRestTransport.SearchPublicKg")

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
            request: service.SearchPublicKgRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.SearchPublicKgResponse:
            r"""Call the search public kg method over HTTP.

            Args:
                request (~.service.SearchPublicKgRequest):
                    The request object. Request message for
                [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.SearchPublicKgResponse:
                    Response message for
                [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].

            """

            http_options = _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseSearchPublicKg._get_http_options()
            request, metadata = self._interceptor.pre_search_public_kg(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnterpriseKnowledgeGraphServiceRestTransport._BaseSearchPublicKg,
                    "_BaseSearchPublicKg__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.SearchPublicKg",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "SearchPublicKg",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnterpriseKnowledgeGraphServiceRestTransport._SearchPublicKg._get_response(
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
            resp = service.SearchPublicKgResponse()
            pb_resp = service.SearchPublicKgResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_public_kg(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_public_kg_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.SearchPublicKgResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceClient.search_public_kg",
                    extra={
                        "serviceName": "google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService",
                        "rpcName": "SearchPublicKg",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def cancel_entity_reconciliation_job(
        self,
    ) -> Callable[[service.CancelEntityReconciliationJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelEntityReconciliationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_entity_reconciliation_job(
        self,
    ) -> Callable[
        [service.CreateEntityReconciliationJobRequest], service.EntityReconciliationJob
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEntityReconciliationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_entity_reconciliation_job(
        self,
    ) -> Callable[[service.DeleteEntityReconciliationJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEntityReconciliationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_entity_reconciliation_job(
        self,
    ) -> Callable[
        [service.GetEntityReconciliationJobRequest], service.EntityReconciliationJob
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEntityReconciliationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_entity_reconciliation_jobs(
        self,
    ) -> Callable[
        [service.ListEntityReconciliationJobsRequest],
        service.ListEntityReconciliationJobsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEntityReconciliationJobs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def lookup(self) -> Callable[[service.LookupRequest], service.LookupResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Lookup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup_public_kg(
        self,
    ) -> Callable[[service.LookupPublicKgRequest], service.LookupPublicKgResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupPublicKg(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search(self) -> Callable[[service.SearchRequest], service.SearchResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Search(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_public_kg(
        self,
    ) -> Callable[[service.SearchPublicKgRequest], service.SearchPublicKgResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchPublicKg(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("EnterpriseKnowledgeGraphServiceRestTransport",)
