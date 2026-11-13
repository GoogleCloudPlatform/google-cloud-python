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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.policysimulator_v1._compat import transcode_request
from google.cloud.policysimulator_v1.types import orgpolicy as gcp_orgpolicy

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOrgPolicyViolationsPreviewServiceRestTransport

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


class OrgPolicyViolationsPreviewServiceRestInterceptor:
    """Interceptor for OrgPolicyViolationsPreviewService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OrgPolicyViolationsPreviewServiceRestTransport.

    .. code-block:: python
        class MyCustomOrgPolicyViolationsPreviewServiceInterceptor(OrgPolicyViolationsPreviewServiceRestInterceptor):
            def pre_create_org_policy_violations_preview(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_org_policy_violations_preview(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_org_policy_violations_preview(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_org_policy_violations_preview(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_org_policy_violations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_org_policy_violations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_org_policy_violations_previews(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_org_policy_violations_previews(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OrgPolicyViolationsPreviewServiceRestTransport(interceptor=MyCustomOrgPolicyViolationsPreviewServiceInterceptor())
        client = OrgPolicyViolationsPreviewServiceClient(transport=transport)


    """

    def pre_create_org_policy_violations_preview(
        self,
        request: gcp_orgpolicy.CreateOrgPolicyViolationsPreviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.CreateOrgPolicyViolationsPreviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_org_policy_violations_preview

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicyViolationsPreviewService server.
        """
        return request, metadata

    def post_create_org_policy_violations_preview(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_org_policy_violations_preview

        DEPRECATED. Please use the `post_create_org_policy_violations_preview_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicyViolationsPreviewService server but before
        it is returned to user code. This `post_create_org_policy_violations_preview` interceptor runs
        before the `post_create_org_policy_violations_preview_with_metadata` interceptor.
        """
        return response

    def post_create_org_policy_violations_preview_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_org_policy_violations_preview

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicyViolationsPreviewService server but before it is returned to user code.

        We recommend only using this `post_create_org_policy_violations_preview_with_metadata`
        interceptor in new development instead of the `post_create_org_policy_violations_preview` interceptor.
        When both interceptors are used, this `post_create_org_policy_violations_preview_with_metadata` interceptor runs after the
        `post_create_org_policy_violations_preview` interceptor. The (possibly modified) response returned by
        `post_create_org_policy_violations_preview` will be passed to
        `post_create_org_policy_violations_preview_with_metadata`.
        """
        return response, metadata

    def pre_get_org_policy_violations_preview(
        self,
        request: gcp_orgpolicy.GetOrgPolicyViolationsPreviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.GetOrgPolicyViolationsPreviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_org_policy_violations_preview

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicyViolationsPreviewService server.
        """
        return request, metadata

    def post_get_org_policy_violations_preview(
        self, response: gcp_orgpolicy.OrgPolicyViolationsPreview
    ) -> gcp_orgpolicy.OrgPolicyViolationsPreview:
        """Post-rpc interceptor for get_org_policy_violations_preview

        DEPRECATED. Please use the `post_get_org_policy_violations_preview_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicyViolationsPreviewService server but before
        it is returned to user code. This `post_get_org_policy_violations_preview` interceptor runs
        before the `post_get_org_policy_violations_preview_with_metadata` interceptor.
        """
        return response

    def post_get_org_policy_violations_preview_with_metadata(
        self,
        response: gcp_orgpolicy.OrgPolicyViolationsPreview,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.OrgPolicyViolationsPreview,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_org_policy_violations_preview

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicyViolationsPreviewService server but before it is returned to user code.

        We recommend only using this `post_get_org_policy_violations_preview_with_metadata`
        interceptor in new development instead of the `post_get_org_policy_violations_preview` interceptor.
        When both interceptors are used, this `post_get_org_policy_violations_preview_with_metadata` interceptor runs after the
        `post_get_org_policy_violations_preview` interceptor. The (possibly modified) response returned by
        `post_get_org_policy_violations_preview` will be passed to
        `post_get_org_policy_violations_preview_with_metadata`.
        """
        return response, metadata

    def pre_list_org_policy_violations(
        self,
        request: gcp_orgpolicy.ListOrgPolicyViolationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.ListOrgPolicyViolationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_org_policy_violations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicyViolationsPreviewService server.
        """
        return request, metadata

    def post_list_org_policy_violations(
        self, response: gcp_orgpolicy.ListOrgPolicyViolationsResponse
    ) -> gcp_orgpolicy.ListOrgPolicyViolationsResponse:
        """Post-rpc interceptor for list_org_policy_violations

        DEPRECATED. Please use the `post_list_org_policy_violations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicyViolationsPreviewService server but before
        it is returned to user code. This `post_list_org_policy_violations` interceptor runs
        before the `post_list_org_policy_violations_with_metadata` interceptor.
        """
        return response

    def post_list_org_policy_violations_with_metadata(
        self,
        response: gcp_orgpolicy.ListOrgPolicyViolationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.ListOrgPolicyViolationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_org_policy_violations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicyViolationsPreviewService server but before it is returned to user code.

        We recommend only using this `post_list_org_policy_violations_with_metadata`
        interceptor in new development instead of the `post_list_org_policy_violations` interceptor.
        When both interceptors are used, this `post_list_org_policy_violations_with_metadata` interceptor runs after the
        `post_list_org_policy_violations` interceptor. The (possibly modified) response returned by
        `post_list_org_policy_violations` will be passed to
        `post_list_org_policy_violations_with_metadata`.
        """
        return response, metadata

    def pre_list_org_policy_violations_previews(
        self,
        request: gcp_orgpolicy.ListOrgPolicyViolationsPreviewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.ListOrgPolicyViolationsPreviewsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_org_policy_violations_previews

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicyViolationsPreviewService server.
        """
        return request, metadata

    def post_list_org_policy_violations_previews(
        self, response: gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse
    ) -> gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse:
        """Post-rpc interceptor for list_org_policy_violations_previews

        DEPRECATED. Please use the `post_list_org_policy_violations_previews_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicyViolationsPreviewService server but before
        it is returned to user code. This `post_list_org_policy_violations_previews` interceptor runs
        before the `post_list_org_policy_violations_previews_with_metadata` interceptor.
        """
        return response

    def post_list_org_policy_violations_previews_with_metadata(
        self,
        response: gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_org_policy_violations_previews

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicyViolationsPreviewService server but before it is returned to user code.

        We recommend only using this `post_list_org_policy_violations_previews_with_metadata`
        interceptor in new development instead of the `post_list_org_policy_violations_previews` interceptor.
        When both interceptors are used, this `post_list_org_policy_violations_previews_with_metadata` interceptor runs after the
        `post_list_org_policy_violations_previews` interceptor. The (possibly modified) response returned by
        `post_list_org_policy_violations_previews` will be passed to
        `post_list_org_policy_violations_previews_with_metadata`.
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
        before they are sent to the OrgPolicyViolationsPreviewService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the OrgPolicyViolationsPreviewService server but before
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
        before they are sent to the OrgPolicyViolationsPreviewService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the OrgPolicyViolationsPreviewService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class OrgPolicyViolationsPreviewServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OrgPolicyViolationsPreviewServiceRestInterceptor


class OrgPolicyViolationsPreviewServiceRestTransport(
    _BaseOrgPolicyViolationsPreviewServiceRestTransport
):
    """REST backend synchronous transport for OrgPolicyViolationsPreviewService.

    Violations Preview API service for OrgPolicy.

    An
    [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
    is a preview of the violations that will exist as soon as a proposed
    OrgPolicy change is submitted. To create an
    [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview],
    the API user specifies the changes they wish to make and requests
    the generation of a preview via [GenerateViolationsPreview][]. the
    OrgPolicy Simulator service then scans the API user's currently
    existing resources to determine these resources violate the newly
    set OrgPolicy.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "policysimulator.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[OrgPolicyViolationsPreviewServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'policysimulator.googleapis.com').
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
            interceptor (Optional[OrgPolicyViolationsPreviewServiceRestInterceptor]): Interceptor used
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = (
            interceptor or OrgPolicyViolationsPreviewServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/replays/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*/replays/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/replays/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/orgPolicyViolationsPreviews/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*/orgPolicyViolationsPreviews/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/orgPolicyViolationsPreviews/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/accessPolicySimulations/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*/accessPolicySimulations/*/operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/accessPolicySimulations/*/operations/**}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=operations}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/replays/*/operations}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*/replays/*/operations}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/replays/*/operations}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateOrgPolicyViolationsPreview(
        _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseCreateOrgPolicyViolationsPreview,
        OrgPolicyViolationsPreviewServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrgPolicyViolationsPreviewServiceRestTransport.CreateOrgPolicyViolationsPreview"
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
            request: gcp_orgpolicy.CreateOrgPolicyViolationsPreviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create org policy
            violations preview method over HTTP.

                Args:
                    request (~.gcp_orgpolicy.CreateOrgPolicyViolationsPreviewRequest):
                        The request object. CreateOrgPolicyViolationsPreviewRequest is the request
                    message for
                    [OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseCreateOrgPolicyViolationsPreview._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_org_policy_violations_preview(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseCreateOrgPolicyViolationsPreview,
                    "_BaseCreateOrgPolicyViolationsPreview__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.CreateOrgPolicyViolationsPreview",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "CreateOrgPolicyViolationsPreview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyViolationsPreviewServiceRestTransport._CreateOrgPolicyViolationsPreview._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_org_policy_violations_preview(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_org_policy_violations_preview_with_metadata(
                    resp, response_metadata
                )
            )
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
                    "Received response for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.create_org_policy_violations_preview",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "CreateOrgPolicyViolationsPreview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrgPolicyViolationsPreview(
        _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseGetOrgPolicyViolationsPreview,
        OrgPolicyViolationsPreviewServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrgPolicyViolationsPreviewServiceRestTransport.GetOrgPolicyViolationsPreview"
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
            request: gcp_orgpolicy.GetOrgPolicyViolationsPreviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcp_orgpolicy.OrgPolicyViolationsPreview:
            r"""Call the get org policy violations
            preview method over HTTP.

                Args:
                    request (~.gcp_orgpolicy.GetOrgPolicyViolationsPreviewRequest):
                        The request object. GetOrgPolicyViolationsPreviewRequest is the request
                    message for
                    [OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcp_orgpolicy.OrgPolicyViolationsPreview:
                        OrgPolicyViolationsPreview is a resource providing a
                    preview of the violations that will exist if an
                    OrgPolicy change is made.

                    The list of violations are modeled as child resources
                    and retrieved via a [ListOrgPolicyViolations][] API
                    call. There are potentially more [OrgPolicyViolations][]
                    than could fit in an embedded field. Thus, the use of a
                    child resource instead of a field.

            """

            http_options = _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseGetOrgPolicyViolationsPreview._get_http_options()
            request, metadata = self._interceptor.pre_get_org_policy_violations_preview(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseGetOrgPolicyViolationsPreview,
                    "_BaseGetOrgPolicyViolationsPreview__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.GetOrgPolicyViolationsPreview",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "GetOrgPolicyViolationsPreview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyViolationsPreviewServiceRestTransport._GetOrgPolicyViolationsPreview._get_response(
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
            resp = gcp_orgpolicy.OrgPolicyViolationsPreview()
            pb_resp = gcp_orgpolicy.OrgPolicyViolationsPreview.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_org_policy_violations_preview(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_org_policy_violations_preview_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcp_orgpolicy.OrgPolicyViolationsPreview.to_json(
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
                    "Received response for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.get_org_policy_violations_preview",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "GetOrgPolicyViolationsPreview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrgPolicyViolations(
        _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOrgPolicyViolations,
        OrgPolicyViolationsPreviewServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrgPolicyViolationsPreviewServiceRestTransport.ListOrgPolicyViolations"
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
            request: gcp_orgpolicy.ListOrgPolicyViolationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcp_orgpolicy.ListOrgPolicyViolationsResponse:
            r"""Call the list org policy
            violations method over HTTP.

                Args:
                    request (~.gcp_orgpolicy.ListOrgPolicyViolationsRequest):
                        The request object. ListOrgPolicyViolationsRequest is the request message
                    for
                    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolations][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcp_orgpolicy.ListOrgPolicyViolationsResponse:
                        ListOrgPolicyViolationsResponse is the response message
                    for
                    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolations][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations]

            """

            http_options = _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOrgPolicyViolations._get_http_options()
            request, metadata = self._interceptor.pre_list_org_policy_violations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOrgPolicyViolations,
                    "_BaseListOrgPolicyViolations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.ListOrgPolicyViolations",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "ListOrgPolicyViolations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyViolationsPreviewServiceRestTransport._ListOrgPolicyViolations._get_response(
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
            resp = gcp_orgpolicy.ListOrgPolicyViolationsResponse()
            pb_resp = gcp_orgpolicy.ListOrgPolicyViolationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_org_policy_violations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_org_policy_violations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcp_orgpolicy.ListOrgPolicyViolationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.list_org_policy_violations",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "ListOrgPolicyViolations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrgPolicyViolationsPreviews(
        _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOrgPolicyViolationsPreviews,
        OrgPolicyViolationsPreviewServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrgPolicyViolationsPreviewServiceRestTransport.ListOrgPolicyViolationsPreviews"
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
            request: gcp_orgpolicy.ListOrgPolicyViolationsPreviewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse:
            r"""Call the list org policy
            violations previews method over HTTP.

                Args:
                    request (~.gcp_orgpolicy.ListOrgPolicyViolationsPreviewsRequest):
                        The request object. ListOrgPolicyViolationsPreviewsRequest is the request
                    message for
                    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse:
                        ListOrgPolicyViolationsPreviewsResponse is the response
                    message for
                    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews].

            """

            http_options = _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOrgPolicyViolationsPreviews._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_org_policy_violations_previews(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOrgPolicyViolationsPreviews,
                    "_BaseListOrgPolicyViolationsPreviews__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.ListOrgPolicyViolationsPreviews",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "ListOrgPolicyViolationsPreviews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyViolationsPreviewServiceRestTransport._ListOrgPolicyViolationsPreviews._get_response(
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
            resp = gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse()
            pb_resp = gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_org_policy_violations_previews(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_org_policy_violations_previews_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse.to_json(
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
                    "Received response for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.list_org_policy_violations_previews",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "ListOrgPolicyViolationsPreviews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_org_policy_violations_preview(
        self,
    ) -> Callable[
        [gcp_orgpolicy.CreateOrgPolicyViolationsPreviewRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOrgPolicyViolationsPreview(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_org_policy_violations_preview(
        self,
    ) -> Callable[
        [gcp_orgpolicy.GetOrgPolicyViolationsPreviewRequest],
        gcp_orgpolicy.OrgPolicyViolationsPreview,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrgPolicyViolationsPreview(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_org_policy_violations(
        self,
    ) -> Callable[
        [gcp_orgpolicy.ListOrgPolicyViolationsRequest],
        gcp_orgpolicy.ListOrgPolicyViolationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrgPolicyViolations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_org_policy_violations_previews(
        self,
    ) -> Callable[
        [gcp_orgpolicy.ListOrgPolicyViolationsPreviewsRequest],
        gcp_orgpolicy.ListOrgPolicyViolationsPreviewsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrgPolicyViolationsPreviews(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseGetOperation,
        OrgPolicyViolationsPreviewServiceRestStub,
    ):
        def __hash__(self):
            return hash("OrgPolicyViolationsPreviewServiceRestTransport.GetOperation")

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

            http_options = _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyViolationsPreviewServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
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
        _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOperations,
        OrgPolicyViolationsPreviewServiceRestStub,
    ):
        def __hash__(self):
            return hash("OrgPolicyViolationsPreviewServiceRestTransport.ListOperations")

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

            http_options = _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyViolationsPreviewServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyViolationsPreviewServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.policysimulator_v1.OrgPolicyViolationsPreviewServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService",
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


__all__ = ("OrgPolicyViolationsPreviewServiceRestTransport",)
