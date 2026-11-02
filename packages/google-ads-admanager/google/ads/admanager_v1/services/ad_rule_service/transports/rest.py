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

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import ad_rule_messages, ad_rule_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAdRuleServiceRestTransport

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


class AdRuleServiceRestInterceptor:
    """Interceptor for AdRuleService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AdRuleServiceRestTransport.

    .. code-block:: python
        class MyCustomAdRuleServiceInterceptor(AdRuleServiceRestInterceptor):
            def pre_batch_activate_ad_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_ad_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_ad_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_ad_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_ad_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_ad_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_delete_ad_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_batch_update_ad_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_ad_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_ad_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ad_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_ad_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ad_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ad_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ad_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_ad_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_ad_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AdRuleServiceRestTransport(interceptor=MyCustomAdRuleServiceInterceptor())
        client = AdRuleServiceClient(transport=transport)


    """

    def pre_batch_activate_ad_rules(
        self,
        request: ad_rule_service.BatchActivateAdRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchActivateAdRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_ad_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_batch_activate_ad_rules(
        self, response: ad_rule_service.BatchActivateAdRulesResponse
    ) -> ad_rule_service.BatchActivateAdRulesResponse:
        """Post-rpc interceptor for batch_activate_ad_rules

        DEPRECATED. Please use the `post_batch_activate_ad_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_batch_activate_ad_rules` interceptor runs
        before the `post_batch_activate_ad_rules_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_ad_rules_with_metadata(
        self,
        response: ad_rule_service.BatchActivateAdRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchActivateAdRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_ad_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_ad_rules_with_metadata`
        interceptor in new development instead of the `post_batch_activate_ad_rules` interceptor.
        When both interceptors are used, this `post_batch_activate_ad_rules_with_metadata` interceptor runs after the
        `post_batch_activate_ad_rules` interceptor. The (possibly modified) response returned by
        `post_batch_activate_ad_rules` will be passed to
        `post_batch_activate_ad_rules_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_ad_rules(
        self,
        request: ad_rule_service.BatchCreateAdRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchCreateAdRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_ad_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_batch_create_ad_rules(
        self, response: ad_rule_service.BatchCreateAdRulesResponse
    ) -> ad_rule_service.BatchCreateAdRulesResponse:
        """Post-rpc interceptor for batch_create_ad_rules

        DEPRECATED. Please use the `post_batch_create_ad_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_batch_create_ad_rules` interceptor runs
        before the `post_batch_create_ad_rules_with_metadata` interceptor.
        """
        return response

    def post_batch_create_ad_rules_with_metadata(
        self,
        response: ad_rule_service.BatchCreateAdRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchCreateAdRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_ad_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_batch_create_ad_rules_with_metadata`
        interceptor in new development instead of the `post_batch_create_ad_rules` interceptor.
        When both interceptors are used, this `post_batch_create_ad_rules_with_metadata` interceptor runs after the
        `post_batch_create_ad_rules` interceptor. The (possibly modified) response returned by
        `post_batch_create_ad_rules` will be passed to
        `post_batch_create_ad_rules_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_ad_rules(
        self,
        request: ad_rule_service.BatchDeactivateAdRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchDeactivateAdRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_ad_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_batch_deactivate_ad_rules(
        self, response: ad_rule_service.BatchDeactivateAdRulesResponse
    ) -> ad_rule_service.BatchDeactivateAdRulesResponse:
        """Post-rpc interceptor for batch_deactivate_ad_rules

        DEPRECATED. Please use the `post_batch_deactivate_ad_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_batch_deactivate_ad_rules` interceptor runs
        before the `post_batch_deactivate_ad_rules_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_ad_rules_with_metadata(
        self,
        response: ad_rule_service.BatchDeactivateAdRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchDeactivateAdRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_ad_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_ad_rules_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_ad_rules` interceptor.
        When both interceptors are used, this `post_batch_deactivate_ad_rules_with_metadata` interceptor runs after the
        `post_batch_deactivate_ad_rules` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_ad_rules` will be passed to
        `post_batch_deactivate_ad_rules_with_metadata`.
        """
        return response, metadata

    def pre_batch_delete_ad_rules(
        self,
        request: ad_rule_service.BatchDeleteAdRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchDeleteAdRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_delete_ad_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def pre_batch_update_ad_rules(
        self,
        request: ad_rule_service.BatchUpdateAdRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchUpdateAdRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_ad_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_batch_update_ad_rules(
        self, response: ad_rule_service.BatchUpdateAdRulesResponse
    ) -> ad_rule_service.BatchUpdateAdRulesResponse:
        """Post-rpc interceptor for batch_update_ad_rules

        DEPRECATED. Please use the `post_batch_update_ad_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_batch_update_ad_rules` interceptor runs
        before the `post_batch_update_ad_rules_with_metadata` interceptor.
        """
        return response

    def post_batch_update_ad_rules_with_metadata(
        self,
        response: ad_rule_service.BatchUpdateAdRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.BatchUpdateAdRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_ad_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_batch_update_ad_rules_with_metadata`
        interceptor in new development instead of the `post_batch_update_ad_rules` interceptor.
        When both interceptors are used, this `post_batch_update_ad_rules_with_metadata` interceptor runs after the
        `post_batch_update_ad_rules` interceptor. The (possibly modified) response returned by
        `post_batch_update_ad_rules` will be passed to
        `post_batch_update_ad_rules_with_metadata`.
        """
        return response, metadata

    def pre_create_ad_rule(
        self,
        request: ad_rule_service.CreateAdRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.CreateAdRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_ad_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_create_ad_rule(
        self, response: ad_rule_messages.AdRule
    ) -> ad_rule_messages.AdRule:
        """Post-rpc interceptor for create_ad_rule

        DEPRECATED. Please use the `post_create_ad_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_create_ad_rule` interceptor runs
        before the `post_create_ad_rule_with_metadata` interceptor.
        """
        return response

    def post_create_ad_rule_with_metadata(
        self,
        response: ad_rule_messages.AdRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_rule_messages.AdRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ad_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_create_ad_rule_with_metadata`
        interceptor in new development instead of the `post_create_ad_rule` interceptor.
        When both interceptors are used, this `post_create_ad_rule_with_metadata` interceptor runs after the
        `post_create_ad_rule` interceptor. The (possibly modified) response returned by
        `post_create_ad_rule` will be passed to
        `post_create_ad_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_ad_rule(
        self,
        request: ad_rule_service.GetAdRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.GetAdRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_ad_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_get_ad_rule(
        self, response: ad_rule_messages.AdRule
    ) -> ad_rule_messages.AdRule:
        """Post-rpc interceptor for get_ad_rule

        DEPRECATED. Please use the `post_get_ad_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_get_ad_rule` interceptor runs
        before the `post_get_ad_rule_with_metadata` interceptor.
        """
        return response

    def post_get_ad_rule_with_metadata(
        self,
        response: ad_rule_messages.AdRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_rule_messages.AdRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ad_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_get_ad_rule_with_metadata`
        interceptor in new development instead of the `post_get_ad_rule` interceptor.
        When both interceptors are used, this `post_get_ad_rule_with_metadata` interceptor runs after the
        `post_get_ad_rule` interceptor. The (possibly modified) response returned by
        `post_get_ad_rule` will be passed to
        `post_get_ad_rule_with_metadata`.
        """
        return response, metadata

    def pre_list_ad_rules(
        self,
        request: ad_rule_service.ListAdRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.ListAdRulesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_ad_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_list_ad_rules(
        self, response: ad_rule_service.ListAdRulesResponse
    ) -> ad_rule_service.ListAdRulesResponse:
        """Post-rpc interceptor for list_ad_rules

        DEPRECATED. Please use the `post_list_ad_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_list_ad_rules` interceptor runs
        before the `post_list_ad_rules_with_metadata` interceptor.
        """
        return response

    def post_list_ad_rules_with_metadata(
        self,
        response: ad_rule_service.ListAdRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.ListAdRulesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_ad_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_list_ad_rules_with_metadata`
        interceptor in new development instead of the `post_list_ad_rules` interceptor.
        When both interceptors are used, this `post_list_ad_rules_with_metadata` interceptor runs after the
        `post_list_ad_rules` interceptor. The (possibly modified) response returned by
        `post_list_ad_rules` will be passed to
        `post_list_ad_rules_with_metadata`.
        """
        return response, metadata

    def pre_update_ad_rule(
        self,
        request: ad_rule_service.UpdateAdRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_rule_service.UpdateAdRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_ad_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_update_ad_rule(
        self, response: ad_rule_messages.AdRule
    ) -> ad_rule_messages.AdRule:
        """Post-rpc interceptor for update_ad_rule

        DEPRECATED. Please use the `post_update_ad_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code. This `post_update_ad_rule` interceptor runs
        before the `post_update_ad_rule_with_metadata` interceptor.
        """
        return response

    def post_update_ad_rule_with_metadata(
        self,
        response: ad_rule_messages.AdRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_rule_messages.AdRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_ad_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdRuleService server but before it is returned to user code.

        We recommend only using this `post_update_ad_rule_with_metadata`
        interceptor in new development instead of the `post_update_ad_rule` interceptor.
        When both interceptors are used, this `post_update_ad_rule_with_metadata` interceptor runs after the
        `post_update_ad_rule` interceptor. The (possibly modified) response returned by
        `post_update_ad_rule` will be passed to
        `post_update_ad_rule_with_metadata`.
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
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdRuleService server but before
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
        before they are sent to the AdRuleService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdRuleService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AdRuleServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AdRuleServiceRestInterceptor


class AdRuleServiceRestTransport(_BaseAdRuleServiceRestTransport):
    """REST backend synchronous transport for AdRuleService.

    Provides methods for handling ``AdRule`` objects.

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
        interceptor: Optional[AdRuleServiceRestInterceptor] = None,
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
            interceptor (Optional[AdRuleServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AdRuleServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateAdRules(
        _BaseAdRuleServiceRestTransport._BaseBatchActivateAdRules, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.BatchActivateAdRules")

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
            request: ad_rule_service.BatchActivateAdRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_service.BatchActivateAdRulesResponse:
            r"""Call the batch activate ad rules method over HTTP.

            Args:
                request (~.ad_rule_service.BatchActivateAdRulesRequest):
                    The request object. Request object for ``BatchActivateAdRules`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_service.BatchActivateAdRulesResponse:
                    Response object for ``BatchActivateAdRules`` method.
            """

            http_options = _BaseAdRuleServiceRestTransport._BaseBatchActivateAdRules._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_ad_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseBatchActivateAdRules,
                    "_BaseBatchActivateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.BatchActivateAdRules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchActivateAdRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._BatchActivateAdRules._get_response(
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
            resp = ad_rule_service.BatchActivateAdRulesResponse()
            pb_resp = ad_rule_service.BatchActivateAdRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_ad_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_ad_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_rule_service.BatchActivateAdRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.batch_activate_ad_rules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchActivateAdRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateAdRules(
        _BaseAdRuleServiceRestTransport._BaseBatchCreateAdRules, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.BatchCreateAdRules")

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
            request: ad_rule_service.BatchCreateAdRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_service.BatchCreateAdRulesResponse:
            r"""Call the batch create ad rules method over HTTP.

            Args:
                request (~.ad_rule_service.BatchCreateAdRulesRequest):
                    The request object. Request object for ``BatchCreateAdRules`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_service.BatchCreateAdRulesResponse:
                    Response object for ``BatchCreateAdRules`` method.
            """

            http_options = _BaseAdRuleServiceRestTransport._BaseBatchCreateAdRules._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_ad_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseBatchCreateAdRules,
                    "_BaseBatchCreateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.BatchCreateAdRules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchCreateAdRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._BatchCreateAdRules._get_response(
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
            resp = ad_rule_service.BatchCreateAdRulesResponse()
            pb_resp = ad_rule_service.BatchCreateAdRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_ad_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_ad_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_rule_service.BatchCreateAdRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.batch_create_ad_rules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchCreateAdRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateAdRules(
        _BaseAdRuleServiceRestTransport._BaseBatchDeactivateAdRules,
        AdRuleServiceRestStub,
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.BatchDeactivateAdRules")

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
            request: ad_rule_service.BatchDeactivateAdRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_service.BatchDeactivateAdRulesResponse:
            r"""Call the batch deactivate ad rules method over HTTP.

            Args:
                request (~.ad_rule_service.BatchDeactivateAdRulesRequest):
                    The request object. Request object for ``BatchDeactivateAdRules`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_service.BatchDeactivateAdRulesResponse:
                    Response object for ``BatchDeactivateAdRules`` method.
            """

            http_options = _BaseAdRuleServiceRestTransport._BaseBatchDeactivateAdRules._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_ad_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseBatchDeactivateAdRules,
                    "_BaseBatchDeactivateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.BatchDeactivateAdRules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchDeactivateAdRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._BatchDeactivateAdRules._get_response(
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
            resp = ad_rule_service.BatchDeactivateAdRulesResponse()
            pb_resp = ad_rule_service.BatchDeactivateAdRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_ad_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_ad_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_rule_service.BatchDeactivateAdRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.batch_deactivate_ad_rules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchDeactivateAdRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeleteAdRules(
        _BaseAdRuleServiceRestTransport._BaseBatchDeleteAdRules, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.BatchDeleteAdRules")

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
            request: ad_rule_service.BatchDeleteAdRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the batch delete ad rules method over HTTP.

            Args:
                request (~.ad_rule_service.BatchDeleteAdRulesRequest):
                    The request object. Request object for ``BatchDeleteAdRules`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAdRuleServiceRestTransport._BaseBatchDeleteAdRules._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_ad_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseBatchDeleteAdRules,
                    "_BaseBatchDeleteAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.BatchDeleteAdRules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchDeleteAdRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._BatchDeleteAdRules._get_response(
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

    class _BatchUpdateAdRules(
        _BaseAdRuleServiceRestTransport._BaseBatchUpdateAdRules, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.BatchUpdateAdRules")

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
            request: ad_rule_service.BatchUpdateAdRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_service.BatchUpdateAdRulesResponse:
            r"""Call the batch update ad rules method over HTTP.

            Args:
                request (~.ad_rule_service.BatchUpdateAdRulesRequest):
                    The request object. Request object for ``BatchUpdateAdRules`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_service.BatchUpdateAdRulesResponse:
                    Response object for ``BatchUpdateAdRules`` method.
            """

            http_options = _BaseAdRuleServiceRestTransport._BaseBatchUpdateAdRules._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_ad_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseBatchUpdateAdRules,
                    "_BaseBatchUpdateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.BatchUpdateAdRules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchUpdateAdRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._BatchUpdateAdRules._get_response(
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
            resp = ad_rule_service.BatchUpdateAdRulesResponse()
            pb_resp = ad_rule_service.BatchUpdateAdRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_ad_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_ad_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_rule_service.BatchUpdateAdRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.batch_update_ad_rules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "BatchUpdateAdRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAdRule(
        _BaseAdRuleServiceRestTransport._BaseCreateAdRule, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.CreateAdRule")

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
            request: ad_rule_service.CreateAdRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_messages.AdRule:
            r"""Call the create ad rule method over HTTP.

            Args:
                request (~.ad_rule_service.CreateAdRuleRequest):
                    The request object. Request object for ``CreateAdRule`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_messages.AdRule:
                    An AdRule contains data that the ad
                server will use to generate a playlist
                of video ads.

            """

            http_options = (
                _BaseAdRuleServiceRestTransport._BaseCreateAdRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_ad_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseCreateAdRule,
                    "_BaseCreateAdRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.CreateAdRule",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "CreateAdRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._CreateAdRule._get_response(
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
            resp = ad_rule_messages.AdRule()
            pb_resp = ad_rule_messages.AdRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ad_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ad_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_rule_messages.AdRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.create_ad_rule",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "CreateAdRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAdRule(
        _BaseAdRuleServiceRestTransport._BaseGetAdRule, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.GetAdRule")

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
            request: ad_rule_service.GetAdRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_messages.AdRule:
            r"""Call the get ad rule method over HTTP.

            Args:
                request (~.ad_rule_service.GetAdRuleRequest):
                    The request object. Request object for ``GetAdRule`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_messages.AdRule:
                    An AdRule contains data that the ad
                server will use to generate a playlist
                of video ads.

            """

            http_options = (
                _BaseAdRuleServiceRestTransport._BaseGetAdRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_ad_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseGetAdRule,
                    "_BaseGetAdRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.GetAdRule",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "GetAdRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._GetAdRule._get_response(
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
            resp = ad_rule_messages.AdRule()
            pb_resp = ad_rule_messages.AdRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ad_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ad_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_rule_messages.AdRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.get_ad_rule",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "GetAdRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAdRules(
        _BaseAdRuleServiceRestTransport._BaseListAdRules, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.ListAdRules")

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
            request: ad_rule_service.ListAdRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_service.ListAdRulesResponse:
            r"""Call the list ad rules method over HTTP.

            Args:
                request (~.ad_rule_service.ListAdRulesRequest):
                    The request object. Request object for ``ListAdRules`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_service.ListAdRulesResponse:
                    Response object for ``ListAdRulesRequest`` containing
                matching ``AdRule`` objects.

            """

            http_options = (
                _BaseAdRuleServiceRestTransport._BaseListAdRules._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ad_rules(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseListAdRules,
                    "_BaseListAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.ListAdRules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "ListAdRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._ListAdRules._get_response(
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
            resp = ad_rule_service.ListAdRulesResponse()
            pb_resp = ad_rule_service.ListAdRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ad_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ad_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_rule_service.ListAdRulesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.list_ad_rules",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "ListAdRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAdRule(
        _BaseAdRuleServiceRestTransport._BaseUpdateAdRule, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.UpdateAdRule")

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
            request: ad_rule_service.UpdateAdRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_rule_messages.AdRule:
            r"""Call the update ad rule method over HTTP.

            Args:
                request (~.ad_rule_service.UpdateAdRuleRequest):
                    The request object. Request object for ``UpdateAdRule`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_rule_messages.AdRule:
                    An AdRule contains data that the ad
                server will use to generate a playlist
                of video ads.

            """

            http_options = (
                _BaseAdRuleServiceRestTransport._BaseUpdateAdRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_ad_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseUpdateAdRule,
                    "_BaseUpdateAdRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.UpdateAdRule",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "UpdateAdRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._UpdateAdRule._get_response(
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
            resp = ad_rule_messages.AdRule()
            pb_resp = ad_rule_messages.AdRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_ad_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_ad_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_rule_messages.AdRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdRuleServiceClient.update_ad_rule",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "UpdateAdRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_ad_rules(
        self,
    ) -> Callable[
        [ad_rule_service.BatchActivateAdRulesRequest],
        ad_rule_service.BatchActivateAdRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateAdRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_ad_rules(
        self,
    ) -> Callable[
        [ad_rule_service.BatchCreateAdRulesRequest],
        ad_rule_service.BatchCreateAdRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateAdRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_ad_rules(
        self,
    ) -> Callable[
        [ad_rule_service.BatchDeactivateAdRulesRequest],
        ad_rule_service.BatchDeactivateAdRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateAdRules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_delete_ad_rules(
        self,
    ) -> Callable[[ad_rule_service.BatchDeleteAdRulesRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteAdRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_ad_rules(
        self,
    ) -> Callable[
        [ad_rule_service.BatchUpdateAdRulesRequest],
        ad_rule_service.BatchUpdateAdRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateAdRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_ad_rule(
        self,
    ) -> Callable[[ad_rule_service.CreateAdRuleRequest], ad_rule_messages.AdRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAdRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ad_rule(
        self,
    ) -> Callable[[ad_rule_service.GetAdRuleRequest], ad_rule_messages.AdRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAdRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_ad_rules(
        self,
    ) -> Callable[
        [ad_rule_service.ListAdRulesRequest], ad_rule_service.ListAdRulesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAdRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_ad_rule(
        self,
    ) -> Callable[[ad_rule_service.UpdateAdRuleRequest], ad_rule_messages.AdRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAdRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAdRuleServiceRestTransport._BaseCancelOperation, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.CancelOperation")

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

            http_options = (
                _BaseAdRuleServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._CancelOperation._get_response(
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
        _BaseAdRuleServiceRestTransport._BaseGetOperation, AdRuleServiceRestStub
    ):
        def __hash__(self):
            return hash("AdRuleServiceRestTransport.GetOperation")

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
                _BaseAdRuleServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdRuleServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.AdRuleServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdRuleServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.AdRuleServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
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


__all__ = ("AdRuleServiceRestTransport",)
