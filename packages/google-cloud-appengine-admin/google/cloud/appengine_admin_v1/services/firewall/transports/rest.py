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

from google.cloud.appengine_admin_v1._compat import transcode_request
from google.cloud.appengine_admin_v1.types import appengine, firewall

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseFirewallRestTransport

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


class FirewallRestInterceptor:
    """Interceptor for Firewall.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the FirewallRestTransport.

    .. code-block:: python
        class MyCustomFirewallInterceptor(FirewallRestInterceptor):
            def pre_batch_update_ingress_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_ingress_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_ingress_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ingress_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_ingress_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_ingress_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ingress_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ingress_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ingress_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_ingress_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_ingress_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = FirewallRestTransport(interceptor=MyCustomFirewallInterceptor())
        client = FirewallClient(transport=transport)


    """

    def pre_batch_update_ingress_rules(
        self,
        request: appengine.BatchUpdateIngressRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.BatchUpdateIngressRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_ingress_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Firewall server.
        """
        return request, metadata

    def post_batch_update_ingress_rules(
        self, response: appengine.BatchUpdateIngressRulesResponse
    ) -> appengine.BatchUpdateIngressRulesResponse:
        """Post-rpc interceptor for batch_update_ingress_rules

        DEPRECATED. Please use the `post_batch_update_ingress_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Firewall server but before
        it is returned to user code. This `post_batch_update_ingress_rules` interceptor runs
        before the `post_batch_update_ingress_rules_with_metadata` interceptor.
        """
        return response

    def post_batch_update_ingress_rules_with_metadata(
        self,
        response: appengine.BatchUpdateIngressRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.BatchUpdateIngressRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_ingress_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Firewall server but before it is returned to user code.

        We recommend only using this `post_batch_update_ingress_rules_with_metadata`
        interceptor in new development instead of the `post_batch_update_ingress_rules` interceptor.
        When both interceptors are used, this `post_batch_update_ingress_rules_with_metadata` interceptor runs after the
        `post_batch_update_ingress_rules` interceptor. The (possibly modified) response returned by
        `post_batch_update_ingress_rules` will be passed to
        `post_batch_update_ingress_rules_with_metadata`.
        """
        return response, metadata

    def pre_create_ingress_rule(
        self,
        request: appengine.CreateIngressRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.CreateIngressRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_ingress_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Firewall server.
        """
        return request, metadata

    def post_create_ingress_rule(
        self, response: firewall.FirewallRule
    ) -> firewall.FirewallRule:
        """Post-rpc interceptor for create_ingress_rule

        DEPRECATED. Please use the `post_create_ingress_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Firewall server but before
        it is returned to user code. This `post_create_ingress_rule` interceptor runs
        before the `post_create_ingress_rule_with_metadata` interceptor.
        """
        return response

    def post_create_ingress_rule_with_metadata(
        self,
        response: firewall.FirewallRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[firewall.FirewallRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ingress_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Firewall server but before it is returned to user code.

        We recommend only using this `post_create_ingress_rule_with_metadata`
        interceptor in new development instead of the `post_create_ingress_rule` interceptor.
        When both interceptors are used, this `post_create_ingress_rule_with_metadata` interceptor runs after the
        `post_create_ingress_rule` interceptor. The (possibly modified) response returned by
        `post_create_ingress_rule` will be passed to
        `post_create_ingress_rule_with_metadata`.
        """
        return response, metadata

    def pre_delete_ingress_rule(
        self,
        request: appengine.DeleteIngressRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.DeleteIngressRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_ingress_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Firewall server.
        """
        return request, metadata

    def pre_get_ingress_rule(
        self,
        request: appengine.GetIngressRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.GetIngressRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_ingress_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Firewall server.
        """
        return request, metadata

    def post_get_ingress_rule(
        self, response: firewall.FirewallRule
    ) -> firewall.FirewallRule:
        """Post-rpc interceptor for get_ingress_rule

        DEPRECATED. Please use the `post_get_ingress_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Firewall server but before
        it is returned to user code. This `post_get_ingress_rule` interceptor runs
        before the `post_get_ingress_rule_with_metadata` interceptor.
        """
        return response

    def post_get_ingress_rule_with_metadata(
        self,
        response: firewall.FirewallRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[firewall.FirewallRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ingress_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Firewall server but before it is returned to user code.

        We recommend only using this `post_get_ingress_rule_with_metadata`
        interceptor in new development instead of the `post_get_ingress_rule` interceptor.
        When both interceptors are used, this `post_get_ingress_rule_with_metadata` interceptor runs after the
        `post_get_ingress_rule` interceptor. The (possibly modified) response returned by
        `post_get_ingress_rule` will be passed to
        `post_get_ingress_rule_with_metadata`.
        """
        return response, metadata

    def pre_list_ingress_rules(
        self,
        request: appengine.ListIngressRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.ListIngressRulesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_ingress_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Firewall server.
        """
        return request, metadata

    def post_list_ingress_rules(
        self, response: appengine.ListIngressRulesResponse
    ) -> appengine.ListIngressRulesResponse:
        """Post-rpc interceptor for list_ingress_rules

        DEPRECATED. Please use the `post_list_ingress_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Firewall server but before
        it is returned to user code. This `post_list_ingress_rules` interceptor runs
        before the `post_list_ingress_rules_with_metadata` interceptor.
        """
        return response

    def post_list_ingress_rules_with_metadata(
        self,
        response: appengine.ListIngressRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.ListIngressRulesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_ingress_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Firewall server but before it is returned to user code.

        We recommend only using this `post_list_ingress_rules_with_metadata`
        interceptor in new development instead of the `post_list_ingress_rules` interceptor.
        When both interceptors are used, this `post_list_ingress_rules_with_metadata` interceptor runs after the
        `post_list_ingress_rules` interceptor. The (possibly modified) response returned by
        `post_list_ingress_rules` will be passed to
        `post_list_ingress_rules_with_metadata`.
        """
        return response, metadata

    def pre_update_ingress_rule(
        self,
        request: appengine.UpdateIngressRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        appengine.UpdateIngressRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_ingress_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Firewall server.
        """
        return request, metadata

    def post_update_ingress_rule(
        self, response: firewall.FirewallRule
    ) -> firewall.FirewallRule:
        """Post-rpc interceptor for update_ingress_rule

        DEPRECATED. Please use the `post_update_ingress_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Firewall server but before
        it is returned to user code. This `post_update_ingress_rule` interceptor runs
        before the `post_update_ingress_rule_with_metadata` interceptor.
        """
        return response

    def post_update_ingress_rule_with_metadata(
        self,
        response: firewall.FirewallRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[firewall.FirewallRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_ingress_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Firewall server but before it is returned to user code.

        We recommend only using this `post_update_ingress_rule_with_metadata`
        interceptor in new development instead of the `post_update_ingress_rule` interceptor.
        When both interceptors are used, this `post_update_ingress_rule_with_metadata` interceptor runs after the
        `post_update_ingress_rule` interceptor. The (possibly modified) response returned by
        `post_update_ingress_rule` will be passed to
        `post_update_ingress_rule_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class FirewallRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: FirewallRestInterceptor


class FirewallRestTransport(_BaseFirewallRestTransport):
    """REST backend synchronous transport for Firewall.

    Firewall resources are used to define a collection of access
    control rules for an Application. Each rule is defined with a
    position which specifies the rule's order in the sequence of
    rules, an IP range to be matched against requests, and an action
    to take upon matching requests.

    Every request is evaluated against the Firewall rules in
    priority order. Processesing stops at the first rule which
    matches the request's IP address. A final rule always specifies
    an action that applies to all remaining IP addresses. The
    default final rule for a newly-created application will be set
    to "allow" if not otherwise specified by the user.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "appengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[FirewallRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'appengine.googleapis.com').
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
            interceptor (Optional[FirewallRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or FirewallRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchUpdateIngressRules(
        _BaseFirewallRestTransport._BaseBatchUpdateIngressRules, FirewallRestStub
    ):
        def __hash__(self):
            return hash("FirewallRestTransport.BatchUpdateIngressRules")

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
            request: appengine.BatchUpdateIngressRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> appengine.BatchUpdateIngressRulesResponse:
            r"""Call the batch update ingress
            rules method over HTTP.

                Args:
                    request (~.appengine.BatchUpdateIngressRulesRequest):
                        The request object. Request message for
                    ``Firewall.BatchUpdateIngressRules``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.appengine.BatchUpdateIngressRulesResponse:
                        Response message for ``Firewall.UpdateAllIngressRules``.
            """

            http_options = _BaseFirewallRestTransport._BaseBatchUpdateIngressRules._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_ingress_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallRestTransport._BaseBatchUpdateIngressRules,
                    "_BaseBatchUpdateIngressRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.appengine_v1.FirewallClient.BatchUpdateIngressRules",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "BatchUpdateIngressRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallRestTransport._BatchUpdateIngressRules._get_response(
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
            resp = appengine.BatchUpdateIngressRulesResponse()
            pb_resp = appengine.BatchUpdateIngressRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_ingress_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_ingress_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        appengine.BatchUpdateIngressRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.appengine_v1.FirewallClient.batch_update_ingress_rules",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "BatchUpdateIngressRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateIngressRule(
        _BaseFirewallRestTransport._BaseCreateIngressRule, FirewallRestStub
    ):
        def __hash__(self):
            return hash("FirewallRestTransport.CreateIngressRule")

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
            request: appengine.CreateIngressRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall.FirewallRule:
            r"""Call the create ingress rule method over HTTP.

            Args:
                request (~.appengine.CreateIngressRuleRequest):
                    The request object. Request message for ``Firewall.CreateIngressRule``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.firewall.FirewallRule:
                    A single firewall rule that is
                evaluated against incoming traffic and
                provides an action to take on matched
                requests.

            """

            http_options = (
                _BaseFirewallRestTransport._BaseCreateIngressRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_ingress_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallRestTransport._BaseCreateIngressRule,
                    "_BaseCreateIngressRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.appengine_v1.FirewallClient.CreateIngressRule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "CreateIngressRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallRestTransport._CreateIngressRule._get_response(
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
            resp = firewall.FirewallRule()
            pb_resp = firewall.FirewallRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ingress_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ingress_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = firewall.FirewallRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.appengine_v1.FirewallClient.create_ingress_rule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "CreateIngressRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteIngressRule(
        _BaseFirewallRestTransport._BaseDeleteIngressRule, FirewallRestStub
    ):
        def __hash__(self):
            return hash("FirewallRestTransport.DeleteIngressRule")

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
            request: appengine.DeleteIngressRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete ingress rule method over HTTP.

            Args:
                request (~.appengine.DeleteIngressRuleRequest):
                    The request object. Request message for ``Firewall.DeleteIngressRule``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseFirewallRestTransport._BaseDeleteIngressRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_ingress_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallRestTransport._BaseDeleteIngressRule,
                    "_BaseDeleteIngressRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.appengine_v1.FirewallClient.DeleteIngressRule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "DeleteIngressRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallRestTransport._DeleteIngressRule._get_response(
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

    class _GetIngressRule(
        _BaseFirewallRestTransport._BaseGetIngressRule, FirewallRestStub
    ):
        def __hash__(self):
            return hash("FirewallRestTransport.GetIngressRule")

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
            request: appengine.GetIngressRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall.FirewallRule:
            r"""Call the get ingress rule method over HTTP.

            Args:
                request (~.appengine.GetIngressRuleRequest):
                    The request object. Request message for ``Firewall.GetIngressRule``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.firewall.FirewallRule:
                    A single firewall rule that is
                evaluated against incoming traffic and
                provides an action to take on matched
                requests.

            """

            http_options = (
                _BaseFirewallRestTransport._BaseGetIngressRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_ingress_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallRestTransport._BaseGetIngressRule,
                    "_BaseGetIngressRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.appengine_v1.FirewallClient.GetIngressRule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "GetIngressRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallRestTransport._GetIngressRule._get_response(
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
            resp = firewall.FirewallRule()
            pb_resp = firewall.FirewallRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ingress_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ingress_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = firewall.FirewallRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.appengine_v1.FirewallClient.get_ingress_rule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "GetIngressRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIngressRules(
        _BaseFirewallRestTransport._BaseListIngressRules, FirewallRestStub
    ):
        def __hash__(self):
            return hash("FirewallRestTransport.ListIngressRules")

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
            request: appengine.ListIngressRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> appengine.ListIngressRulesResponse:
            r"""Call the list ingress rules method over HTTP.

            Args:
                request (~.appengine.ListIngressRulesRequest):
                    The request object. Request message for ``Firewall.ListIngressRules``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.appengine.ListIngressRulesResponse:
                    Response message for ``Firewall.ListIngressRules``.
            """

            http_options = (
                _BaseFirewallRestTransport._BaseListIngressRules._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ingress_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallRestTransport._BaseListIngressRules,
                    "_BaseListIngressRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.appengine_v1.FirewallClient.ListIngressRules",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "ListIngressRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallRestTransport._ListIngressRules._get_response(
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
            resp = appengine.ListIngressRulesResponse()
            pb_resp = appengine.ListIngressRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ingress_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ingress_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = appengine.ListIngressRulesResponse.to_json(
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
                    "Received response for google.appengine_v1.FirewallClient.list_ingress_rules",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "ListIngressRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIngressRule(
        _BaseFirewallRestTransport._BaseUpdateIngressRule, FirewallRestStub
    ):
        def __hash__(self):
            return hash("FirewallRestTransport.UpdateIngressRule")

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
            request: appengine.UpdateIngressRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall.FirewallRule:
            r"""Call the update ingress rule method over HTTP.

            Args:
                request (~.appengine.UpdateIngressRuleRequest):
                    The request object. Request message for ``Firewall.UpdateIngressRule``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.firewall.FirewallRule:
                    A single firewall rule that is
                evaluated against incoming traffic and
                provides an action to take on matched
                requests.

            """

            http_options = (
                _BaseFirewallRestTransport._BaseUpdateIngressRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_ingress_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallRestTransport._BaseUpdateIngressRule,
                    "_BaseUpdateIngressRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.appengine_v1.FirewallClient.UpdateIngressRule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "UpdateIngressRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallRestTransport._UpdateIngressRule._get_response(
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
            resp = firewall.FirewallRule()
            pb_resp = firewall.FirewallRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_ingress_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_ingress_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = firewall.FirewallRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.appengine_v1.FirewallClient.update_ingress_rule",
                    extra={
                        "serviceName": "google.appengine.v1.Firewall",
                        "rpcName": "UpdateIngressRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_update_ingress_rules(
        self,
    ) -> Callable[
        [appengine.BatchUpdateIngressRulesRequest],
        appengine.BatchUpdateIngressRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateIngressRules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_ingress_rule(
        self,
    ) -> Callable[[appengine.CreateIngressRuleRequest], firewall.FirewallRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIngressRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_ingress_rule(
        self,
    ) -> Callable[[appengine.DeleteIngressRuleRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIngressRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ingress_rule(
        self,
    ) -> Callable[[appengine.GetIngressRuleRequest], firewall.FirewallRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIngressRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_ingress_rules(
        self,
    ) -> Callable[
        [appengine.ListIngressRulesRequest], appengine.ListIngressRulesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIngressRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_ingress_rule(
        self,
    ) -> Callable[[appengine.UpdateIngressRuleRequest], firewall.FirewallRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIngressRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("FirewallRestTransport",)
