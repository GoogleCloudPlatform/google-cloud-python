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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.pubsub_v1._compat import transcode_request
from google.pubsub_v1.types import schema
from google.pubsub_v1.types import schema as gp_schema

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSchemaServiceRestTransport

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


class SchemaServiceRestInterceptor:
    """Interceptor for SchemaService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SchemaServiceRestTransport.

    .. code-block:: python
        class MyCustomSchemaServiceInterceptor(SchemaServiceRestInterceptor):
            def pre_commit_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_commit_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_schema_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_schema_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_schema_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_schema_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rollback_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rollback_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_message(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_message(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SchemaServiceRestTransport(interceptor=MyCustomSchemaServiceInterceptor())
        client = SchemaServiceClient(transport=transport)


    """

    def pre_commit_schema(
        self,
        request: gp_schema.CommitSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gp_schema.CommitSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for commit_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_commit_schema(self, response: gp_schema.Schema) -> gp_schema.Schema:
        """Post-rpc interceptor for commit_schema

        DEPRECATED. Please use the `post_commit_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_commit_schema` interceptor runs
        before the `post_commit_schema_with_metadata` interceptor.
        """
        return response

    def post_commit_schema_with_metadata(
        self,
        response: gp_schema.Schema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gp_schema.Schema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for commit_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_commit_schema_with_metadata`
        interceptor in new development instead of the `post_commit_schema` interceptor.
        When both interceptors are used, this `post_commit_schema_with_metadata` interceptor runs after the
        `post_commit_schema` interceptor. The (possibly modified) response returned by
        `post_commit_schema` will be passed to
        `post_commit_schema_with_metadata`.
        """
        return response, metadata

    def pre_create_schema(
        self,
        request: gp_schema.CreateSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gp_schema.CreateSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_create_schema(self, response: gp_schema.Schema) -> gp_schema.Schema:
        """Post-rpc interceptor for create_schema

        DEPRECATED. Please use the `post_create_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_create_schema` interceptor runs
        before the `post_create_schema_with_metadata` interceptor.
        """
        return response

    def post_create_schema_with_metadata(
        self,
        response: gp_schema.Schema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gp_schema.Schema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_create_schema_with_metadata`
        interceptor in new development instead of the `post_create_schema` interceptor.
        When both interceptors are used, this `post_create_schema_with_metadata` interceptor runs after the
        `post_create_schema` interceptor. The (possibly modified) response returned by
        `post_create_schema` will be passed to
        `post_create_schema_with_metadata`.
        """
        return response, metadata

    def pre_delete_schema(
        self,
        request: schema.DeleteSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.DeleteSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def pre_delete_schema_revision(
        self,
        request: schema.DeleteSchemaRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema.DeleteSchemaRevisionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_schema_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_delete_schema_revision(self, response: schema.Schema) -> schema.Schema:
        """Post-rpc interceptor for delete_schema_revision

        DEPRECATED. Please use the `post_delete_schema_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_delete_schema_revision` interceptor runs
        before the `post_delete_schema_revision_with_metadata` interceptor.
        """
        return response

    def post_delete_schema_revision_with_metadata(
        self, response: schema.Schema, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[schema.Schema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_schema_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_delete_schema_revision_with_metadata`
        interceptor in new development instead of the `post_delete_schema_revision` interceptor.
        When both interceptors are used, this `post_delete_schema_revision_with_metadata` interceptor runs after the
        `post_delete_schema_revision` interceptor. The (possibly modified) response returned by
        `post_delete_schema_revision` will be passed to
        `post_delete_schema_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_schema(
        self,
        request: schema.GetSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.GetSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_get_schema(self, response: schema.Schema) -> schema.Schema:
        """Post-rpc interceptor for get_schema

        DEPRECATED. Please use the `post_get_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_get_schema` interceptor runs
        before the `post_get_schema_with_metadata` interceptor.
        """
        return response

    def post_get_schema_with_metadata(
        self, response: schema.Schema, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[schema.Schema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_get_schema_with_metadata`
        interceptor in new development instead of the `post_get_schema` interceptor.
        When both interceptors are used, this `post_get_schema_with_metadata` interceptor runs after the
        `post_get_schema` interceptor. The (possibly modified) response returned by
        `post_get_schema` will be passed to
        `post_get_schema_with_metadata`.
        """
        return response, metadata

    def pre_list_schema_revisions(
        self,
        request: schema.ListSchemaRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema.ListSchemaRevisionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_schema_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_list_schema_revisions(
        self, response: schema.ListSchemaRevisionsResponse
    ) -> schema.ListSchemaRevisionsResponse:
        """Post-rpc interceptor for list_schema_revisions

        DEPRECATED. Please use the `post_list_schema_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_list_schema_revisions` interceptor runs
        before the `post_list_schema_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_schema_revisions_with_metadata(
        self,
        response: schema.ListSchemaRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema.ListSchemaRevisionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_schema_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_list_schema_revisions_with_metadata`
        interceptor in new development instead of the `post_list_schema_revisions` interceptor.
        When both interceptors are used, this `post_list_schema_revisions_with_metadata` interceptor runs after the
        `post_list_schema_revisions` interceptor. The (possibly modified) response returned by
        `post_list_schema_revisions` will be passed to
        `post_list_schema_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_schemas(
        self,
        request: schema.ListSchemasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.ListSchemasRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_list_schemas(
        self, response: schema.ListSchemasResponse
    ) -> schema.ListSchemasResponse:
        """Post-rpc interceptor for list_schemas

        DEPRECATED. Please use the `post_list_schemas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_list_schemas` interceptor runs
        before the `post_list_schemas_with_metadata` interceptor.
        """
        return response

    def post_list_schemas_with_metadata(
        self,
        response: schema.ListSchemasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.ListSchemasResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_schemas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_list_schemas_with_metadata`
        interceptor in new development instead of the `post_list_schemas` interceptor.
        When both interceptors are used, this `post_list_schemas_with_metadata` interceptor runs after the
        `post_list_schemas` interceptor. The (possibly modified) response returned by
        `post_list_schemas` will be passed to
        `post_list_schemas_with_metadata`.
        """
        return response, metadata

    def pre_rollback_schema(
        self,
        request: schema.RollbackSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.RollbackSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for rollback_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_rollback_schema(self, response: schema.Schema) -> schema.Schema:
        """Post-rpc interceptor for rollback_schema

        DEPRECATED. Please use the `post_rollback_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_rollback_schema` interceptor runs
        before the `post_rollback_schema_with_metadata` interceptor.
        """
        return response

    def post_rollback_schema_with_metadata(
        self, response: schema.Schema, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[schema.Schema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rollback_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_rollback_schema_with_metadata`
        interceptor in new development instead of the `post_rollback_schema` interceptor.
        When both interceptors are used, this `post_rollback_schema_with_metadata` interceptor runs after the
        `post_rollback_schema` interceptor. The (possibly modified) response returned by
        `post_rollback_schema` will be passed to
        `post_rollback_schema_with_metadata`.
        """
        return response, metadata

    def pre_validate_message(
        self,
        request: schema.ValidateMessageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.ValidateMessageRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for validate_message

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_validate_message(
        self, response: schema.ValidateMessageResponse
    ) -> schema.ValidateMessageResponse:
        """Post-rpc interceptor for validate_message

        DEPRECATED. Please use the `post_validate_message_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_validate_message` interceptor runs
        before the `post_validate_message_with_metadata` interceptor.
        """
        return response

    def post_validate_message_with_metadata(
        self,
        response: schema.ValidateMessageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[schema.ValidateMessageResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for validate_message

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_validate_message_with_metadata`
        interceptor in new development instead of the `post_validate_message` interceptor.
        When both interceptors are used, this `post_validate_message_with_metadata` interceptor runs after the
        `post_validate_message` interceptor. The (possibly modified) response returned by
        `post_validate_message` will be passed to
        `post_validate_message_with_metadata`.
        """
        return response, metadata

    def pre_validate_schema(
        self,
        request: gp_schema.ValidateSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gp_schema.ValidateSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for validate_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_validate_schema(
        self, response: gp_schema.ValidateSchemaResponse
    ) -> gp_schema.ValidateSchemaResponse:
        """Post-rpc interceptor for validate_schema

        DEPRECATED. Please use the `post_validate_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code. This `post_validate_schema` interceptor runs
        before the `post_validate_schema_with_metadata` interceptor.
        """
        return response

    def post_validate_schema_with_metadata(
        self,
        response: gp_schema.ValidateSchemaResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gp_schema.ValidateSchemaResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for validate_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SchemaService server but before it is returned to user code.

        We recommend only using this `post_validate_schema_with_metadata`
        interceptor in new development instead of the `post_validate_schema` interceptor.
        When both interceptors are used, this `post_validate_schema_with_metadata` interceptor runs after the
        `post_validate_schema` interceptor. The (possibly modified) response returned by
        `post_validate_schema` will be passed to
        `post_validate_schema_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SchemaService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the SchemaService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SchemaServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SchemaServiceRestInterceptor


class SchemaServiceRestTransport(_BaseSchemaServiceRestTransport):
    """REST backend synchronous transport for SchemaService.

    Service for doing schema-related operations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "pubsub.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SchemaServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'pubsub.googleapis.com').
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
            interceptor (Optional[SchemaServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SchemaServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CommitSchema(
        _BaseSchemaServiceRestTransport._BaseCommitSchema, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.CommitSchema")

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
            request: gp_schema.CommitSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gp_schema.Schema:
            r"""Call the commit schema method over HTTP.

            Args:
                request (~.gp_schema.CommitSchemaRequest):
                    The request object. Request for CommitSchema method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gp_schema.Schema:
                    A schema resource.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseCommitSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_commit_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseCommitSchema,
                    "_BaseCommitSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.CommitSchema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "CommitSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._CommitSchema._get_response(
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
            resp = gp_schema.Schema()
            pb_resp = gp_schema.Schema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_commit_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_commit_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gp_schema.Schema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.commit_schema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "CommitSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSchema(
        _BaseSchemaServiceRestTransport._BaseCreateSchema, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.CreateSchema")

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
            request: gp_schema.CreateSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gp_schema.Schema:
            r"""Call the create schema method over HTTP.

            Args:
                request (~.gp_schema.CreateSchemaRequest):
                    The request object. Request for the CreateSchema method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gp_schema.Schema:
                    A schema resource.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseCreateSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseCreateSchema,
                    "_BaseCreateSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.CreateSchema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "CreateSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._CreateSchema._get_response(
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
            resp = gp_schema.Schema()
            pb_resp = gp_schema.Schema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gp_schema.Schema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.create_schema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "CreateSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSchema(
        _BaseSchemaServiceRestTransport._BaseDeleteSchema, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.DeleteSchema")

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
            request: schema.DeleteSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete schema method over HTTP.

            Args:
                request (~.schema.DeleteSchemaRequest):
                    The request object. Request for the ``DeleteSchema`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseDeleteSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseDeleteSchema,
                    "_BaseDeleteSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.DeleteSchema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "DeleteSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._DeleteSchema._get_response(
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

    class _DeleteSchemaRevision(
        _BaseSchemaServiceRestTransport._BaseDeleteSchemaRevision, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.DeleteSchemaRevision")

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
            request: schema.DeleteSchemaRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema.Schema:
            r"""Call the delete schema revision method over HTTP.

            Args:
                request (~.schema.DeleteSchemaRevisionRequest):
                    The request object. Request for the ``DeleteSchemaRevision`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema.Schema:
                    A schema resource.
            """

            http_options = _BaseSchemaServiceRestTransport._BaseDeleteSchemaRevision._get_http_options()
            request, metadata = self._interceptor.pre_delete_schema_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseDeleteSchemaRevision,
                    "_BaseDeleteSchemaRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.DeleteSchemaRevision",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "DeleteSchemaRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._DeleteSchemaRevision._get_response(
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
            resp = schema.Schema()
            pb_resp = schema.Schema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_schema_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_schema_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema.Schema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.delete_schema_revision",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "DeleteSchemaRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSchema(
        _BaseSchemaServiceRestTransport._BaseGetSchema, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.GetSchema")

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
            request: schema.GetSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema.Schema:
            r"""Call the get schema method over HTTP.

            Args:
                request (~.schema.GetSchemaRequest):
                    The request object. Request for the GetSchema method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema.Schema:
                    A schema resource.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseGetSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseGetSchema,
                    "_BaseGetSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.GetSchema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "GetSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._GetSchema._get_response(
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
            resp = schema.Schema()
            pb_resp = schema.Schema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema.Schema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.get_schema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "GetSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSchemaRevisions(
        _BaseSchemaServiceRestTransport._BaseListSchemaRevisions, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.ListSchemaRevisions")

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
            request: schema.ListSchemaRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema.ListSchemaRevisionsResponse:
            r"""Call the list schema revisions method over HTTP.

            Args:
                request (~.schema.ListSchemaRevisionsRequest):
                    The request object. Request for the ``ListSchemaRevisions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema.ListSchemaRevisionsResponse:
                    Response for the ``ListSchemaRevisions`` method.
            """

            http_options = _BaseSchemaServiceRestTransport._BaseListSchemaRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_schema_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseListSchemaRevisions,
                    "_BaseListSchemaRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.ListSchemaRevisions",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ListSchemaRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._ListSchemaRevisions._get_response(
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
            resp = schema.ListSchemaRevisionsResponse()
            pb_resp = schema.ListSchemaRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_schema_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_schema_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema.ListSchemaRevisionsResponse.to_json(
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
                    "Received response for google.pubsub_v1.SchemaServiceClient.list_schema_revisions",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ListSchemaRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSchemas(
        _BaseSchemaServiceRestTransport._BaseListSchemas, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.ListSchemas")

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
            request: schema.ListSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema.ListSchemasResponse:
            r"""Call the list schemas method over HTTP.

            Args:
                request (~.schema.ListSchemasRequest):
                    The request object. Request for the ``ListSchemas`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema.ListSchemasResponse:
                    Response for the ``ListSchemas`` method.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseListSchemas._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_schemas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseListSchemas,
                    "_BaseListSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.ListSchemas",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ListSchemas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._ListSchemas._get_response(
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
            resp = schema.ListSchemasResponse()
            pb_resp = schema.ListSchemasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_schemas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_schemas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema.ListSchemasResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.list_schemas",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ListSchemas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RollbackSchema(
        _BaseSchemaServiceRestTransport._BaseRollbackSchema, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.RollbackSchema")

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
            request: schema.RollbackSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema.Schema:
            r"""Call the rollback schema method over HTTP.

            Args:
                request (~.schema.RollbackSchemaRequest):
                    The request object. Request for the ``RollbackSchema`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema.Schema:
                    A schema resource.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseRollbackSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_rollback_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseRollbackSchema,
                    "_BaseRollbackSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.RollbackSchema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "RollbackSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._RollbackSchema._get_response(
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
            resp = schema.Schema()
            pb_resp = schema.Schema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rollback_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rollback_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema.Schema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.rollback_schema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "RollbackSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateMessage(
        _BaseSchemaServiceRestTransport._BaseValidateMessage, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.ValidateMessage")

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
            request: schema.ValidateMessageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema.ValidateMessageResponse:
            r"""Call the validate message method over HTTP.

            Args:
                request (~.schema.ValidateMessageRequest):
                    The request object. Request for the ``ValidateMessage`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema.ValidateMessageResponse:
                    Response for the ``ValidateMessage`` method. Empty for
                now.

            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseValidateMessage._get_http_options()
            )
            request, metadata = self._interceptor.pre_validate_message(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseValidateMessage,
                    "_BaseValidateMessage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.ValidateMessage",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ValidateMessage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._ValidateMessage._get_response(
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
            resp = schema.ValidateMessageResponse()
            pb_resp = schema.ValidateMessageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_validate_message(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_validate_message_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema.ValidateMessageResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SchemaServiceClient.validate_message",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ValidateMessage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateSchema(
        _BaseSchemaServiceRestTransport._BaseValidateSchema, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.ValidateSchema")

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
            request: gp_schema.ValidateSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gp_schema.ValidateSchemaResponse:
            r"""Call the validate schema method over HTTP.

            Args:
                request (~.gp_schema.ValidateSchemaRequest):
                    The request object. Request for the ``ValidateSchema`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gp_schema.ValidateSchemaResponse:
                    Response for the ``ValidateSchema`` method. Empty for
                now.

            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseValidateSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_validate_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseValidateSchema,
                    "_BaseValidateSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.ValidateSchema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ValidateSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._ValidateSchema._get_response(
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
            resp = gp_schema.ValidateSchemaResponse()
            pb_resp = gp_schema.ValidateSchemaResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_validate_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_validate_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gp_schema.ValidateSchemaResponse.to_json(
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
                    "Received response for google.pubsub_v1.SchemaServiceClient.validate_schema",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "ValidateSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def commit_schema(
        self,
    ) -> Callable[[gp_schema.CommitSchemaRequest], gp_schema.Schema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CommitSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_schema(
        self,
    ) -> Callable[[gp_schema.CreateSchemaRequest], gp_schema.Schema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_schema(self) -> Callable[[schema.DeleteSchemaRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_schema_revision(
        self,
    ) -> Callable[[schema.DeleteSchemaRevisionRequest], schema.Schema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSchemaRevision(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_schema(self) -> Callable[[schema.GetSchemaRequest], schema.Schema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_schema_revisions(
        self,
    ) -> Callable[
        [schema.ListSchemaRevisionsRequest], schema.ListSchemaRevisionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSchemaRevisions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_schemas(
        self,
    ) -> Callable[[schema.ListSchemasRequest], schema.ListSchemasResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSchemas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback_schema(
        self,
    ) -> Callable[[schema.RollbackSchemaRequest], schema.Schema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RollbackSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def validate_message(
        self,
    ) -> Callable[[schema.ValidateMessageRequest], schema.ValidateMessageResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateMessage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def validate_schema(
        self,
    ) -> Callable[[gp_schema.ValidateSchemaRequest], gp_schema.ValidateSchemaResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseSchemaServiceRestTransport._BaseGetIamPolicy, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.pubsub_v1.SchemaServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseSchemaServiceRestTransport._BaseSetIamPolicy, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseSchemaServiceRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.pubsub_v1.SchemaServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseSchemaServiceRestTransport._BaseTestIamPermissions, SchemaServiceRestStub
    ):
        def __hash__(self):
            return hash("SchemaServiceRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseSchemaServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSchemaServiceRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SchemaServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SchemaServiceRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.pubsub_v1.SchemaServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.pubsub.v1.SchemaService",
                        "rpcName": "TestIamPermissions",
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


__all__ = ("SchemaServiceRestTransport",)
