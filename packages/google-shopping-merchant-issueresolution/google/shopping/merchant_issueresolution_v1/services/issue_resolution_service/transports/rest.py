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

from google.shopping.merchant_issueresolution_v1._compat import transcode_request
from google.shopping.merchant_issueresolution_v1.types import issueresolution

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseIssueResolutionServiceRestTransport

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


class IssueResolutionServiceRestInterceptor:
    """Interceptor for IssueResolutionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IssueResolutionServiceRestTransport.

    .. code-block:: python
        class MyCustomIssueResolutionServiceInterceptor(IssueResolutionServiceRestInterceptor):
            def pre_render_account_issues(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_render_account_issues(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_render_product_issues(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_render_product_issues(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_trigger_action(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_trigger_action(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = IssueResolutionServiceRestTransport(interceptor=MyCustomIssueResolutionServiceInterceptor())
        client = IssueResolutionServiceClient(transport=transport)


    """

    def pre_render_account_issues(
        self,
        request: issueresolution.RenderAccountIssuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        issueresolution.RenderAccountIssuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for render_account_issues

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IssueResolutionService server.
        """
        return request, metadata

    def post_render_account_issues(
        self, response: issueresolution.RenderAccountIssuesResponse
    ) -> issueresolution.RenderAccountIssuesResponse:
        """Post-rpc interceptor for render_account_issues

        DEPRECATED. Please use the `post_render_account_issues_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IssueResolutionService server but before
        it is returned to user code. This `post_render_account_issues` interceptor runs
        before the `post_render_account_issues_with_metadata` interceptor.
        """
        return response

    def post_render_account_issues_with_metadata(
        self,
        response: issueresolution.RenderAccountIssuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        issueresolution.RenderAccountIssuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for render_account_issues

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IssueResolutionService server but before it is returned to user code.

        We recommend only using this `post_render_account_issues_with_metadata`
        interceptor in new development instead of the `post_render_account_issues` interceptor.
        When both interceptors are used, this `post_render_account_issues_with_metadata` interceptor runs after the
        `post_render_account_issues` interceptor. The (possibly modified) response returned by
        `post_render_account_issues` will be passed to
        `post_render_account_issues_with_metadata`.
        """
        return response, metadata

    def pre_render_product_issues(
        self,
        request: issueresolution.RenderProductIssuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        issueresolution.RenderProductIssuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for render_product_issues

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IssueResolutionService server.
        """
        return request, metadata

    def post_render_product_issues(
        self, response: issueresolution.RenderProductIssuesResponse
    ) -> issueresolution.RenderProductIssuesResponse:
        """Post-rpc interceptor for render_product_issues

        DEPRECATED. Please use the `post_render_product_issues_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IssueResolutionService server but before
        it is returned to user code. This `post_render_product_issues` interceptor runs
        before the `post_render_product_issues_with_metadata` interceptor.
        """
        return response

    def post_render_product_issues_with_metadata(
        self,
        response: issueresolution.RenderProductIssuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        issueresolution.RenderProductIssuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for render_product_issues

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IssueResolutionService server but before it is returned to user code.

        We recommend only using this `post_render_product_issues_with_metadata`
        interceptor in new development instead of the `post_render_product_issues` interceptor.
        When both interceptors are used, this `post_render_product_issues_with_metadata` interceptor runs after the
        `post_render_product_issues` interceptor. The (possibly modified) response returned by
        `post_render_product_issues` will be passed to
        `post_render_product_issues_with_metadata`.
        """
        return response, metadata

    def pre_trigger_action(
        self,
        request: issueresolution.TriggerActionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        issueresolution.TriggerActionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for trigger_action

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IssueResolutionService server.
        """
        return request, metadata

    def post_trigger_action(
        self, response: issueresolution.TriggerActionResponse
    ) -> issueresolution.TriggerActionResponse:
        """Post-rpc interceptor for trigger_action

        DEPRECATED. Please use the `post_trigger_action_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IssueResolutionService server but before
        it is returned to user code. This `post_trigger_action` interceptor runs
        before the `post_trigger_action_with_metadata` interceptor.
        """
        return response

    def post_trigger_action_with_metadata(
        self,
        response: issueresolution.TriggerActionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        issueresolution.TriggerActionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for trigger_action

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IssueResolutionService server but before it is returned to user code.

        We recommend only using this `post_trigger_action_with_metadata`
        interceptor in new development instead of the `post_trigger_action` interceptor.
        When both interceptors are used, this `post_trigger_action_with_metadata` interceptor runs after the
        `post_trigger_action` interceptor. The (possibly modified) response returned by
        `post_trigger_action` will be passed to
        `post_trigger_action_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class IssueResolutionServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IssueResolutionServiceRestInterceptor


class IssueResolutionServiceRestTransport(_BaseIssueResolutionServiceRestTransport):
    """REST backend synchronous transport for IssueResolutionService.

    Service to provide an issue resolution content for account
    issues and product issues.

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
        interceptor: Optional[IssueResolutionServiceRestInterceptor] = None,
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
            interceptor (Optional[IssueResolutionServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or IssueResolutionServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _RenderAccountIssues(
        _BaseIssueResolutionServiceRestTransport._BaseRenderAccountIssues,
        IssueResolutionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IssueResolutionServiceRestTransport.RenderAccountIssues")

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
            request: issueresolution.RenderAccountIssuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> issueresolution.RenderAccountIssuesResponse:
            r"""Call the render account issues method over HTTP.

            Args:
                request (~.issueresolution.RenderAccountIssuesRequest):
                    The request object. Request to provide issue resolution
                content and actions for business's
                account issues.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.issueresolution.RenderAccountIssuesResponse:
                    Response containing an issue
                resolution content and actions for
                listed account issues.

            """

            http_options = _BaseIssueResolutionServiceRestTransport._BaseRenderAccountIssues._get_http_options()
            request, metadata = self._interceptor.pre_render_account_issues(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIssueResolutionServiceRestTransport._BaseRenderAccountIssues,
                    "_BaseRenderAccountIssues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.issueresolution_v1.IssueResolutionServiceClient.RenderAccountIssues",
                    extra={
                        "serviceName": "google.shopping.merchant.issueresolution.v1.IssueResolutionService",
                        "rpcName": "RenderAccountIssues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IssueResolutionServiceRestTransport._RenderAccountIssues._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = issueresolution.RenderAccountIssuesResponse()
            pb_resp = issueresolution.RenderAccountIssuesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_render_account_issues(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_render_account_issues_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        issueresolution.RenderAccountIssuesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.issueresolution_v1.IssueResolutionServiceClient.render_account_issues",
                    extra={
                        "serviceName": "google.shopping.merchant.issueresolution.v1.IssueResolutionService",
                        "rpcName": "RenderAccountIssues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenderProductIssues(
        _BaseIssueResolutionServiceRestTransport._BaseRenderProductIssues,
        IssueResolutionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IssueResolutionServiceRestTransport.RenderProductIssues")

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
            request: issueresolution.RenderProductIssuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> issueresolution.RenderProductIssuesResponse:
            r"""Call the render product issues method over HTTP.

            Args:
                request (~.issueresolution.RenderProductIssuesRequest):
                    The request object. Request to provide an issue
                resolution content and actions for
                product issues of business's product.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.issueresolution.RenderProductIssuesResponse:
                    Response containing an issue
                resolution content and actions for
                listed product issues.

            """

            http_options = _BaseIssueResolutionServiceRestTransport._BaseRenderProductIssues._get_http_options()
            request, metadata = self._interceptor.pre_render_product_issues(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIssueResolutionServiceRestTransport._BaseRenderProductIssues,
                    "_BaseRenderProductIssues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.issueresolution_v1.IssueResolutionServiceClient.RenderProductIssues",
                    extra={
                        "serviceName": "google.shopping.merchant.issueresolution.v1.IssueResolutionService",
                        "rpcName": "RenderProductIssues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IssueResolutionServiceRestTransport._RenderProductIssues._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = issueresolution.RenderProductIssuesResponse()
            pb_resp = issueresolution.RenderProductIssuesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_render_product_issues(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_render_product_issues_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        issueresolution.RenderProductIssuesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.issueresolution_v1.IssueResolutionServiceClient.render_product_issues",
                    extra={
                        "serviceName": "google.shopping.merchant.issueresolution.v1.IssueResolutionService",
                        "rpcName": "RenderProductIssues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TriggerAction(
        _BaseIssueResolutionServiceRestTransport._BaseTriggerAction,
        IssueResolutionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IssueResolutionServiceRestTransport.TriggerAction")

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
            request: issueresolution.TriggerActionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> issueresolution.TriggerActionResponse:
            r"""Call the trigger action method over HTTP.

            Args:
                request (~.issueresolution.TriggerActionRequest):
                    The request object. Request to start the selected action
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.issueresolution.TriggerActionResponse:
                    Response informing about the started
                action.

            """

            http_options = _BaseIssueResolutionServiceRestTransport._BaseTriggerAction._get_http_options()
            request, metadata = self._interceptor.pre_trigger_action(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIssueResolutionServiceRestTransport._BaseTriggerAction,
                    "_BaseTriggerAction__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.issueresolution_v1.IssueResolutionServiceClient.TriggerAction",
                    extra={
                        "serviceName": "google.shopping.merchant.issueresolution.v1.IssueResolutionService",
                        "rpcName": "TriggerAction",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IssueResolutionServiceRestTransport._TriggerAction._get_response(
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
            resp = issueresolution.TriggerActionResponse()
            pb_resp = issueresolution.TriggerActionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_trigger_action(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_trigger_action_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = issueresolution.TriggerActionResponse.to_json(
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
                    "Received response for google.shopping.merchant.issueresolution_v1.IssueResolutionServiceClient.trigger_action",
                    extra={
                        "serviceName": "google.shopping.merchant.issueresolution.v1.IssueResolutionService",
                        "rpcName": "TriggerAction",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def render_account_issues(
        self,
    ) -> Callable[
        [issueresolution.RenderAccountIssuesRequest],
        issueresolution.RenderAccountIssuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenderAccountIssues(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def render_product_issues(
        self,
    ) -> Callable[
        [issueresolution.RenderProductIssuesRequest],
        issueresolution.RenderProductIssuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenderProductIssues(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def trigger_action(
        self,
    ) -> Callable[
        [issueresolution.TriggerActionRequest], issueresolution.TriggerActionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TriggerAction(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("IssueResolutionServiceRestTransport",)
