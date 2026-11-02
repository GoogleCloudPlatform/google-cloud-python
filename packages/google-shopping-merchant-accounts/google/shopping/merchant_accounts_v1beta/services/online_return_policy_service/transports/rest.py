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

from google.shopping.merchant_accounts_v1beta._compat import transcode_request
from google.shopping.merchant_accounts_v1beta.types import online_return_policy
from google.shopping.merchant_accounts_v1beta.types import (
    online_return_policy as gsma_online_return_policy,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOnlineReturnPolicyServiceRestTransport

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


class OnlineReturnPolicyServiceRestInterceptor:
    """Interceptor for OnlineReturnPolicyService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OnlineReturnPolicyServiceRestTransport.

    .. code-block:: python
        class MyCustomOnlineReturnPolicyServiceInterceptor(OnlineReturnPolicyServiceRestInterceptor):
            def pre_create_online_return_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_online_return_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_online_return_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_online_return_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_online_return_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_online_return_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_online_return_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_online_return_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_online_return_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OnlineReturnPolicyServiceRestTransport(interceptor=MyCustomOnlineReturnPolicyServiceInterceptor())
        client = OnlineReturnPolicyServiceClient(transport=transport)


    """

    def pre_create_online_return_policy(
        self,
        request: gsma_online_return_policy.CreateOnlineReturnPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsma_online_return_policy.CreateOnlineReturnPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_online_return_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OnlineReturnPolicyService server.
        """
        return request, metadata

    def post_create_online_return_policy(
        self, response: gsma_online_return_policy.OnlineReturnPolicy
    ) -> gsma_online_return_policy.OnlineReturnPolicy:
        """Post-rpc interceptor for create_online_return_policy

        DEPRECATED. Please use the `post_create_online_return_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OnlineReturnPolicyService server but before
        it is returned to user code. This `post_create_online_return_policy` interceptor runs
        before the `post_create_online_return_policy_with_metadata` interceptor.
        """
        return response

    def post_create_online_return_policy_with_metadata(
        self,
        response: gsma_online_return_policy.OnlineReturnPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsma_online_return_policy.OnlineReturnPolicy,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_online_return_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OnlineReturnPolicyService server but before it is returned to user code.

        We recommend only using this `post_create_online_return_policy_with_metadata`
        interceptor in new development instead of the `post_create_online_return_policy` interceptor.
        When both interceptors are used, this `post_create_online_return_policy_with_metadata` interceptor runs after the
        `post_create_online_return_policy` interceptor. The (possibly modified) response returned by
        `post_create_online_return_policy` will be passed to
        `post_create_online_return_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_online_return_policy(
        self,
        request: online_return_policy.DeleteOnlineReturnPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        online_return_policy.DeleteOnlineReturnPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_online_return_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OnlineReturnPolicyService server.
        """
        return request, metadata

    def pre_get_online_return_policy(
        self,
        request: online_return_policy.GetOnlineReturnPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        online_return_policy.GetOnlineReturnPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_online_return_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OnlineReturnPolicyService server.
        """
        return request, metadata

    def post_get_online_return_policy(
        self, response: online_return_policy.OnlineReturnPolicy
    ) -> online_return_policy.OnlineReturnPolicy:
        """Post-rpc interceptor for get_online_return_policy

        DEPRECATED. Please use the `post_get_online_return_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OnlineReturnPolicyService server but before
        it is returned to user code. This `post_get_online_return_policy` interceptor runs
        before the `post_get_online_return_policy_with_metadata` interceptor.
        """
        return response

    def post_get_online_return_policy_with_metadata(
        self,
        response: online_return_policy.OnlineReturnPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        online_return_policy.OnlineReturnPolicy, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_online_return_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OnlineReturnPolicyService server but before it is returned to user code.

        We recommend only using this `post_get_online_return_policy_with_metadata`
        interceptor in new development instead of the `post_get_online_return_policy` interceptor.
        When both interceptors are used, this `post_get_online_return_policy_with_metadata` interceptor runs after the
        `post_get_online_return_policy` interceptor. The (possibly modified) response returned by
        `post_get_online_return_policy` will be passed to
        `post_get_online_return_policy_with_metadata`.
        """
        return response, metadata

    def pre_list_online_return_policies(
        self,
        request: online_return_policy.ListOnlineReturnPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        online_return_policy.ListOnlineReturnPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_online_return_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OnlineReturnPolicyService server.
        """
        return request, metadata

    def post_list_online_return_policies(
        self, response: online_return_policy.ListOnlineReturnPoliciesResponse
    ) -> online_return_policy.ListOnlineReturnPoliciesResponse:
        """Post-rpc interceptor for list_online_return_policies

        DEPRECATED. Please use the `post_list_online_return_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OnlineReturnPolicyService server but before
        it is returned to user code. This `post_list_online_return_policies` interceptor runs
        before the `post_list_online_return_policies_with_metadata` interceptor.
        """
        return response

    def post_list_online_return_policies_with_metadata(
        self,
        response: online_return_policy.ListOnlineReturnPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        online_return_policy.ListOnlineReturnPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_online_return_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OnlineReturnPolicyService server but before it is returned to user code.

        We recommend only using this `post_list_online_return_policies_with_metadata`
        interceptor in new development instead of the `post_list_online_return_policies` interceptor.
        When both interceptors are used, this `post_list_online_return_policies_with_metadata` interceptor runs after the
        `post_list_online_return_policies` interceptor. The (possibly modified) response returned by
        `post_list_online_return_policies` will be passed to
        `post_list_online_return_policies_with_metadata`.
        """
        return response, metadata

    def pre_update_online_return_policy(
        self,
        request: gsma_online_return_policy.UpdateOnlineReturnPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsma_online_return_policy.UpdateOnlineReturnPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_online_return_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OnlineReturnPolicyService server.
        """
        return request, metadata

    def post_update_online_return_policy(
        self, response: gsma_online_return_policy.OnlineReturnPolicy
    ) -> gsma_online_return_policy.OnlineReturnPolicy:
        """Post-rpc interceptor for update_online_return_policy

        DEPRECATED. Please use the `post_update_online_return_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OnlineReturnPolicyService server but before
        it is returned to user code. This `post_update_online_return_policy` interceptor runs
        before the `post_update_online_return_policy_with_metadata` interceptor.
        """
        return response

    def post_update_online_return_policy_with_metadata(
        self,
        response: gsma_online_return_policy.OnlineReturnPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsma_online_return_policy.OnlineReturnPolicy,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_online_return_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OnlineReturnPolicyService server but before it is returned to user code.

        We recommend only using this `post_update_online_return_policy_with_metadata`
        interceptor in new development instead of the `post_update_online_return_policy` interceptor.
        When both interceptors are used, this `post_update_online_return_policy_with_metadata` interceptor runs after the
        `post_update_online_return_policy` interceptor. The (possibly modified) response returned by
        `post_update_online_return_policy` will be passed to
        `post_update_online_return_policy_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class OnlineReturnPolicyServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OnlineReturnPolicyServiceRestInterceptor


class OnlineReturnPolicyServiceRestTransport(
    _BaseOnlineReturnPolicyServiceRestTransport
):
    """REST backend synchronous transport for OnlineReturnPolicyService.

    The service facilitates the management of a merchant's remorse
    return policy configuration, encompassing return policies for both
    ads and free listings

    programs. This API defines the following resource model:
    --------------------------------------------------------

    `OnlineReturnPolicy </merchant/api/reference/rpc/google.shopping.merchant.accounts.v1beta#google.shopping.merchant.accounts.v1beta.OnlineReturnPolicy>`__

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
        interceptor: Optional[OnlineReturnPolicyServiceRestInterceptor] = None,
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
            interceptor (Optional[OnlineReturnPolicyServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or OnlineReturnPolicyServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateOnlineReturnPolicy(
        _BaseOnlineReturnPolicyServiceRestTransport._BaseCreateOnlineReturnPolicy,
        OnlineReturnPolicyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OnlineReturnPolicyServiceRestTransport.CreateOnlineReturnPolicy"
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
            request: gsma_online_return_policy.CreateOnlineReturnPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsma_online_return_policy.OnlineReturnPolicy:
            r"""Call the create online return
            policy method over HTTP.

                Args:
                    request (~.gsma_online_return_policy.CreateOnlineReturnPolicyRequest):
                        The request object. Request message for the ``CreateOnlineReturnPolicy``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gsma_online_return_policy.OnlineReturnPolicy:
                        `Online return
                    policy <https://support.google.com/merchants/answer/10220642>`__
                    object. This is currently used to represent return
                    policies for ads and free listings programs.

            """

            http_options = _BaseOnlineReturnPolicyServiceRestTransport._BaseCreateOnlineReturnPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_online_return_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOnlineReturnPolicyServiceRestTransport._BaseCreateOnlineReturnPolicy,
                    "_BaseCreateOnlineReturnPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.CreateOnlineReturnPolicy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "CreateOnlineReturnPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OnlineReturnPolicyServiceRestTransport._CreateOnlineReturnPolicy._get_response(
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
            resp = gsma_online_return_policy.OnlineReturnPolicy()
            pb_resp = gsma_online_return_policy.OnlineReturnPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_online_return_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_online_return_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gsma_online_return_policy.OnlineReturnPolicy.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.create_online_return_policy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "CreateOnlineReturnPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteOnlineReturnPolicy(
        _BaseOnlineReturnPolicyServiceRestTransport._BaseDeleteOnlineReturnPolicy,
        OnlineReturnPolicyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OnlineReturnPolicyServiceRestTransport.DeleteOnlineReturnPolicy"
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
            request: online_return_policy.DeleteOnlineReturnPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete online return
            policy method over HTTP.

                Args:
                    request (~.online_return_policy.DeleteOnlineReturnPolicyRequest):
                        The request object. Request message for the ``DeleteOnlineReturnPolicy``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseOnlineReturnPolicyServiceRestTransport._BaseDeleteOnlineReturnPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_online_return_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOnlineReturnPolicyServiceRestTransport._BaseDeleteOnlineReturnPolicy,
                    "_BaseDeleteOnlineReturnPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.DeleteOnlineReturnPolicy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "DeleteOnlineReturnPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OnlineReturnPolicyServiceRestTransport._DeleteOnlineReturnPolicy._get_response(
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

    class _GetOnlineReturnPolicy(
        _BaseOnlineReturnPolicyServiceRestTransport._BaseGetOnlineReturnPolicy,
        OnlineReturnPolicyServiceRestStub,
    ):
        def __hash__(self):
            return hash("OnlineReturnPolicyServiceRestTransport.GetOnlineReturnPolicy")

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
            request: online_return_policy.GetOnlineReturnPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> online_return_policy.OnlineReturnPolicy:
            r"""Call the get online return policy method over HTTP.

            Args:
                request (~.online_return_policy.GetOnlineReturnPolicyRequest):
                    The request object. Request message for the ``GetOnlineReturnPolicy``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.online_return_policy.OnlineReturnPolicy:
                    `Online return
                policy <https://support.google.com/merchants/answer/10220642>`__
                object. This is currently used to represent return
                policies for ads and free listings programs.

            """

            http_options = _BaseOnlineReturnPolicyServiceRestTransport._BaseGetOnlineReturnPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_online_return_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOnlineReturnPolicyServiceRestTransport._BaseGetOnlineReturnPolicy,
                    "_BaseGetOnlineReturnPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.GetOnlineReturnPolicy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "GetOnlineReturnPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OnlineReturnPolicyServiceRestTransport._GetOnlineReturnPolicy._get_response(
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
            resp = online_return_policy.OnlineReturnPolicy()
            pb_resp = online_return_policy.OnlineReturnPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_online_return_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_online_return_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = online_return_policy.OnlineReturnPolicy.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.get_online_return_policy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "GetOnlineReturnPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOnlineReturnPolicies(
        _BaseOnlineReturnPolicyServiceRestTransport._BaseListOnlineReturnPolicies,
        OnlineReturnPolicyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OnlineReturnPolicyServiceRestTransport.ListOnlineReturnPolicies"
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
            request: online_return_policy.ListOnlineReturnPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> online_return_policy.ListOnlineReturnPoliciesResponse:
            r"""Call the list online return
            policies method over HTTP.

                Args:
                    request (~.online_return_policy.ListOnlineReturnPoliciesRequest):
                        The request object. Request message for the ``ListOnlineReturnPolicies``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.online_return_policy.ListOnlineReturnPoliciesResponse:
                        Response message for the ``ListOnlineReturnPolicies``
                    method.

            """

            http_options = _BaseOnlineReturnPolicyServiceRestTransport._BaseListOnlineReturnPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_online_return_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOnlineReturnPolicyServiceRestTransport._BaseListOnlineReturnPolicies,
                    "_BaseListOnlineReturnPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.ListOnlineReturnPolicies",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "ListOnlineReturnPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OnlineReturnPolicyServiceRestTransport._ListOnlineReturnPolicies._get_response(
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
            resp = online_return_policy.ListOnlineReturnPoliciesResponse()
            pb_resp = online_return_policy.ListOnlineReturnPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_online_return_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_online_return_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        online_return_policy.ListOnlineReturnPoliciesResponse.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.list_online_return_policies",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "ListOnlineReturnPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateOnlineReturnPolicy(
        _BaseOnlineReturnPolicyServiceRestTransport._BaseUpdateOnlineReturnPolicy,
        OnlineReturnPolicyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OnlineReturnPolicyServiceRestTransport.UpdateOnlineReturnPolicy"
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
            request: gsma_online_return_policy.UpdateOnlineReturnPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsma_online_return_policy.OnlineReturnPolicy:
            r"""Call the update online return
            policy method over HTTP.

                Args:
                    request (~.gsma_online_return_policy.UpdateOnlineReturnPolicyRequest):
                        The request object. Request message for the ``UpdateOnlineReturnPolicy``
                    method. The method supports field masks and when the
                    mask is provided, only the fields specified in the mask
                    are updated.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gsma_online_return_policy.OnlineReturnPolicy:
                        `Online return
                    policy <https://support.google.com/merchants/answer/10220642>`__
                    object. This is currently used to represent return
                    policies for ads and free listings programs.

            """

            http_options = _BaseOnlineReturnPolicyServiceRestTransport._BaseUpdateOnlineReturnPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_online_return_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOnlineReturnPolicyServiceRestTransport._BaseUpdateOnlineReturnPolicy,
                    "_BaseUpdateOnlineReturnPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.UpdateOnlineReturnPolicy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "UpdateOnlineReturnPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OnlineReturnPolicyServiceRestTransport._UpdateOnlineReturnPolicy._get_response(
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
            resp = gsma_online_return_policy.OnlineReturnPolicy()
            pb_resp = gsma_online_return_policy.OnlineReturnPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_online_return_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_online_return_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gsma_online_return_policy.OnlineReturnPolicy.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.OnlineReturnPolicyServiceClient.update_online_return_policy",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.OnlineReturnPolicyService",
                        "rpcName": "UpdateOnlineReturnPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_online_return_policy(
        self,
    ) -> Callable[
        [gsma_online_return_policy.CreateOnlineReturnPolicyRequest],
        gsma_online_return_policy.OnlineReturnPolicy,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOnlineReturnPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_online_return_policy(
        self,
    ) -> Callable[
        [online_return_policy.DeleteOnlineReturnPolicyRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteOnlineReturnPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_online_return_policy(
        self,
    ) -> Callable[
        [online_return_policy.GetOnlineReturnPolicyRequest],
        online_return_policy.OnlineReturnPolicy,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOnlineReturnPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_online_return_policies(
        self,
    ) -> Callable[
        [online_return_policy.ListOnlineReturnPoliciesRequest],
        online_return_policy.ListOnlineReturnPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOnlineReturnPolicies(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_online_return_policy(
        self,
    ) -> Callable[
        [gsma_online_return_policy.UpdateOnlineReturnPolicyRequest],
        gsma_online_return_policy.OnlineReturnPolicy,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateOnlineReturnPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("OnlineReturnPolicyServiceRestTransport",)
