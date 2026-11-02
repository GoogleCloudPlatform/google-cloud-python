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

from google.cloud.gsuiteaddons_v1._compat import transcode_request
from google.cloud.gsuiteaddons_v1.types import gsuiteaddons

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseGSuiteAddOnsRestTransport

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


class GSuiteAddOnsRestInterceptor:
    """Interceptor for GSuiteAddOns.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GSuiteAddOnsRestTransport.

    .. code-block:: python
        class MyCustomGSuiteAddOnsInterceptor(GSuiteAddOnsRestInterceptor):
            def pre_create_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_install_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_install_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_install_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_list_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_replace_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_replace_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_uninstall_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

        transport = GSuiteAddOnsRestTransport(interceptor=MyCustomGSuiteAddOnsInterceptor())
        client = GSuiteAddOnsClient(transport=transport)


    """

    def pre_create_deployment(
        self,
        request: gsuiteaddons.CreateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.CreateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def post_create_deployment(
        self, response: gsuiteaddons.Deployment
    ) -> gsuiteaddons.Deployment:
        """Post-rpc interceptor for create_deployment

        DEPRECATED. Please use the `post_create_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GSuiteAddOns server but before
        it is returned to user code. This `post_create_deployment` interceptor runs
        before the `post_create_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_deployment_with_metadata(
        self,
        response: gsuiteaddons.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsuiteaddons.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GSuiteAddOns server but before it is returned to user code.

        We recommend only using this `post_create_deployment_with_metadata`
        interceptor in new development instead of the `post_create_deployment` interceptor.
        When both interceptors are used, this `post_create_deployment_with_metadata` interceptor runs after the
        `post_create_deployment` interceptor. The (possibly modified) response returned by
        `post_create_deployment` will be passed to
        `post_create_deployment_with_metadata`.
        """
        return response, metadata

    def pre_delete_deployment(
        self,
        request: gsuiteaddons.DeleteDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.DeleteDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def pre_get_authorization(
        self,
        request: gsuiteaddons.GetAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.GetAuthorizationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def post_get_authorization(
        self, response: gsuiteaddons.Authorization
    ) -> gsuiteaddons.Authorization:
        """Post-rpc interceptor for get_authorization

        DEPRECATED. Please use the `post_get_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GSuiteAddOns server but before
        it is returned to user code. This `post_get_authorization` interceptor runs
        before the `post_get_authorization_with_metadata` interceptor.
        """
        return response

    def post_get_authorization_with_metadata(
        self,
        response: gsuiteaddons.Authorization,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsuiteaddons.Authorization, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GSuiteAddOns server but before it is returned to user code.

        We recommend only using this `post_get_authorization_with_metadata`
        interceptor in new development instead of the `post_get_authorization` interceptor.
        When both interceptors are used, this `post_get_authorization_with_metadata` interceptor runs after the
        `post_get_authorization` interceptor. The (possibly modified) response returned by
        `post_get_authorization` will be passed to
        `post_get_authorization_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment(
        self,
        request: gsuiteaddons.GetDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.GetDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def post_get_deployment(
        self, response: gsuiteaddons.Deployment
    ) -> gsuiteaddons.Deployment:
        """Post-rpc interceptor for get_deployment

        DEPRECATED. Please use the `post_get_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GSuiteAddOns server but before
        it is returned to user code. This `post_get_deployment` interceptor runs
        before the `post_get_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_with_metadata(
        self,
        response: gsuiteaddons.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsuiteaddons.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GSuiteAddOns server but before it is returned to user code.

        We recommend only using this `post_get_deployment_with_metadata`
        interceptor in new development instead of the `post_get_deployment` interceptor.
        When both interceptors are used, this `post_get_deployment_with_metadata` interceptor runs after the
        `post_get_deployment` interceptor. The (possibly modified) response returned by
        `post_get_deployment` will be passed to
        `post_get_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_install_status(
        self,
        request: gsuiteaddons.GetInstallStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.GetInstallStatusRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_install_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def post_get_install_status(
        self, response: gsuiteaddons.InstallStatus
    ) -> gsuiteaddons.InstallStatus:
        """Post-rpc interceptor for get_install_status

        DEPRECATED. Please use the `post_get_install_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GSuiteAddOns server but before
        it is returned to user code. This `post_get_install_status` interceptor runs
        before the `post_get_install_status_with_metadata` interceptor.
        """
        return response

    def post_get_install_status_with_metadata(
        self,
        response: gsuiteaddons.InstallStatus,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsuiteaddons.InstallStatus, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_install_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GSuiteAddOns server but before it is returned to user code.

        We recommend only using this `post_get_install_status_with_metadata`
        interceptor in new development instead of the `post_get_install_status` interceptor.
        When both interceptors are used, this `post_get_install_status_with_metadata` interceptor runs after the
        `post_get_install_status` interceptor. The (possibly modified) response returned by
        `post_get_install_status` will be passed to
        `post_get_install_status_with_metadata`.
        """
        return response, metadata

    def pre_install_deployment(
        self,
        request: gsuiteaddons.InstallDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.InstallDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for install_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def pre_list_deployments(
        self,
        request: gsuiteaddons.ListDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.ListDeploymentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def post_list_deployments(
        self, response: gsuiteaddons.ListDeploymentsResponse
    ) -> gsuiteaddons.ListDeploymentsResponse:
        """Post-rpc interceptor for list_deployments

        DEPRECATED. Please use the `post_list_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GSuiteAddOns server but before
        it is returned to user code. This `post_list_deployments` interceptor runs
        before the `post_list_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_deployments_with_metadata(
        self,
        response: gsuiteaddons.ListDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.ListDeploymentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GSuiteAddOns server but before it is returned to user code.

        We recommend only using this `post_list_deployments_with_metadata`
        interceptor in new development instead of the `post_list_deployments` interceptor.
        When both interceptors are used, this `post_list_deployments_with_metadata` interceptor runs after the
        `post_list_deployments` interceptor. The (possibly modified) response returned by
        `post_list_deployments` will be passed to
        `post_list_deployments_with_metadata`.
        """
        return response, metadata

    def pre_replace_deployment(
        self,
        request: gsuiteaddons.ReplaceDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.ReplaceDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for replace_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata

    def post_replace_deployment(
        self, response: gsuiteaddons.Deployment
    ) -> gsuiteaddons.Deployment:
        """Post-rpc interceptor for replace_deployment

        DEPRECATED. Please use the `post_replace_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GSuiteAddOns server but before
        it is returned to user code. This `post_replace_deployment` interceptor runs
        before the `post_replace_deployment_with_metadata` interceptor.
        """
        return response

    def post_replace_deployment_with_metadata(
        self,
        response: gsuiteaddons.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsuiteaddons.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for replace_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GSuiteAddOns server but before it is returned to user code.

        We recommend only using this `post_replace_deployment_with_metadata`
        interceptor in new development instead of the `post_replace_deployment` interceptor.
        When both interceptors are used, this `post_replace_deployment_with_metadata` interceptor runs after the
        `post_replace_deployment` interceptor. The (possibly modified) response returned by
        `post_replace_deployment` will be passed to
        `post_replace_deployment_with_metadata`.
        """
        return response, metadata

    def pre_uninstall_deployment(
        self,
        request: gsuiteaddons.UninstallDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gsuiteaddons.UninstallDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for uninstall_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GSuiteAddOns server.
        """
        return request, metadata


@dataclasses.dataclass
class GSuiteAddOnsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: GSuiteAddOnsRestInterceptor


class GSuiteAddOnsRestTransport(_BaseGSuiteAddOnsRestTransport):
    """REST backend synchronous transport for GSuiteAddOns.

    A service for managing Google Workspace add-ons deployments.

    A Google Workspace add-on is a third-party embedded component
    that can be installed in Google Workspace Applications like
    Gmail, Calendar, Drive, and the Google Docs, Sheets, and Slides
    editors. Google Workspace add-ons can display UI cards, receive
    contextual information from the host application, and perform
    actions in the host application (See:

    https://developers.google.com/gsuite/add-ons/overview for more
    information).

    A Google Workspace add-on deployment resource specifies metadata
    about the add-on, including a specification of the entry points
    in the host application that trigger add-on executions (see:

    https://developers.google.com/gsuite/add-ons/concepts/gsuite-manifests).
    Add-on deployments defined via the Google Workspace add-ons API
    define their entrypoints using HTTPS URLs (See:

    https://developers.google.com/gsuite/add-ons/guides/alternate-runtimes),

    A Google Workspace add-on deployment can be installed in
    developer mode, which allows an add-on developer to test the
    experience an end-user would see when installing and running the
    add-on in their G Suite applications.  When running in developer
    mode, more detailed error messages are exposed in the add-on UI
    to aid in debugging.

    A Google Workspace add-on deployment can be published to Google
    Workspace Marketplace, which allows other Google Workspace users
    to discover and install the add-on.  See:

    https://developers.google.com/gsuite/add-ons/how-tos/publish-add-on-overview
    for details.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "gsuiteaddons.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[GSuiteAddOnsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'gsuiteaddons.googleapis.com').
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
            interceptor (Optional[GSuiteAddOnsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or GSuiteAddOnsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateDeployment(
        _BaseGSuiteAddOnsRestTransport._BaseCreateDeployment, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.CreateDeployment")

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
            request: gsuiteaddons.CreateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsuiteaddons.Deployment:
            r"""Call the create deployment method over HTTP.

            Args:
                request (~.gsuiteaddons.CreateDeploymentRequest):
                    The request object. Request message to create a
                deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsuiteaddons.Deployment:
                    A Google Workspace add-on deployment
            """

            http_options = (
                _BaseGSuiteAddOnsRestTransport._BaseCreateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseCreateDeployment,
                    "_BaseCreateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.CreateDeployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "CreateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._CreateDeployment._get_response(
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
            resp = gsuiteaddons.Deployment()
            pb_resp = gsuiteaddons.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsuiteaddons.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.create_deployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "CreateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDeployment(
        _BaseGSuiteAddOnsRestTransport._BaseDeleteDeployment, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.DeleteDeployment")

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
            request: gsuiteaddons.DeleteDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete deployment method over HTTP.

            Args:
                request (~.gsuiteaddons.DeleteDeploymentRequest):
                    The request object. Request message to delete a
                deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseGSuiteAddOnsRestTransport._BaseDeleteDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseDeleteDeployment,
                    "_BaseDeleteDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.DeleteDeployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "DeleteDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._DeleteDeployment._get_response(
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

    class _GetAuthorization(
        _BaseGSuiteAddOnsRestTransport._BaseGetAuthorization, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.GetAuthorization")

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
            request: gsuiteaddons.GetAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsuiteaddons.Authorization:
            r"""Call the get authorization method over HTTP.

            Args:
                request (~.gsuiteaddons.GetAuthorizationRequest):
                    The request object. Request message to get Google
                Workspace add-ons authorization
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsuiteaddons.Authorization:
                    The authorization information used
                when invoking deployment endpoints.

            """

            http_options = (
                _BaseGSuiteAddOnsRestTransport._BaseGetAuthorization._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseGetAuthorization,
                    "_BaseGetAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.GetAuthorization",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "GetAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._GetAuthorization._get_response(
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
            resp = gsuiteaddons.Authorization()
            pb_resp = gsuiteaddons.Authorization.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_authorization_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsuiteaddons.Authorization.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.get_authorization",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "GetAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeployment(
        _BaseGSuiteAddOnsRestTransport._BaseGetDeployment, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.GetDeployment")

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
            request: gsuiteaddons.GetDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsuiteaddons.Deployment:
            r"""Call the get deployment method over HTTP.

            Args:
                request (~.gsuiteaddons.GetDeploymentRequest):
                    The request object. Request message to get a deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsuiteaddons.Deployment:
                    A Google Workspace add-on deployment
            """

            http_options = (
                _BaseGSuiteAddOnsRestTransport._BaseGetDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deployment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseGetDeployment,
                    "_BaseGetDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.GetDeployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "GetDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._GetDeployment._get_response(
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
            resp = gsuiteaddons.Deployment()
            pb_resp = gsuiteaddons.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsuiteaddons.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.get_deployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "GetDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstallStatus(
        _BaseGSuiteAddOnsRestTransport._BaseGetInstallStatus, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.GetInstallStatus")

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
            request: gsuiteaddons.GetInstallStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsuiteaddons.InstallStatus:
            r"""Call the get install status method over HTTP.

            Args:
                request (~.gsuiteaddons.GetInstallStatusRequest):
                    The request object. Request message to get the install
                status of a developer mode deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsuiteaddons.InstallStatus:
                    Developer mode install status of a
                deployment

            """

            http_options = (
                _BaseGSuiteAddOnsRestTransport._BaseGetInstallStatus._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_install_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseGetInstallStatus,
                    "_BaseGetInstallStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.GetInstallStatus",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "GetInstallStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._GetInstallStatus._get_response(
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
            resp = gsuiteaddons.InstallStatus()
            pb_resp = gsuiteaddons.InstallStatus.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_install_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_install_status_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsuiteaddons.InstallStatus.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.get_install_status",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "GetInstallStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InstallDeployment(
        _BaseGSuiteAddOnsRestTransport._BaseInstallDeployment, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.InstallDeployment")

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
            request: gsuiteaddons.InstallDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the install deployment method over HTTP.

            Args:
                request (~.gsuiteaddons.InstallDeploymentRequest):
                    The request object. Request message to install a
                developer mode deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseGSuiteAddOnsRestTransport._BaseInstallDeployment._get_http_options()
            request, metadata = self._interceptor.pre_install_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseInstallDeployment,
                    "_BaseInstallDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.InstallDeployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "InstallDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._InstallDeployment._get_response(
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

    class _ListDeployments(
        _BaseGSuiteAddOnsRestTransport._BaseListDeployments, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.ListDeployments")

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
            request: gsuiteaddons.ListDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsuiteaddons.ListDeploymentsResponse:
            r"""Call the list deployments method over HTTP.

            Args:
                request (~.gsuiteaddons.ListDeploymentsRequest):
                    The request object. Request message to list deployments
                for a project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsuiteaddons.ListDeploymentsResponse:
                    Response message to list deployments.
            """

            http_options = (
                _BaseGSuiteAddOnsRestTransport._BaseListDeployments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseListDeployments,
                    "_BaseListDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.ListDeployments",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "ListDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._ListDeployments._get_response(
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
            resp = gsuiteaddons.ListDeploymentsResponse()
            pb_resp = gsuiteaddons.ListDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsuiteaddons.ListDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.list_deployments",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "ListDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReplaceDeployment(
        _BaseGSuiteAddOnsRestTransport._BaseReplaceDeployment, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.ReplaceDeployment")

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
            request: gsuiteaddons.ReplaceDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsuiteaddons.Deployment:
            r"""Call the replace deployment method over HTTP.

            Args:
                request (~.gsuiteaddons.ReplaceDeploymentRequest):
                    The request object. Request message to create or replace
                a deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsuiteaddons.Deployment:
                    A Google Workspace add-on deployment
            """

            http_options = _BaseGSuiteAddOnsRestTransport._BaseReplaceDeployment._get_http_options()
            request, metadata = self._interceptor.pre_replace_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseReplaceDeployment,
                    "_BaseReplaceDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.ReplaceDeployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "ReplaceDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._ReplaceDeployment._get_response(
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
            resp = gsuiteaddons.Deployment()
            pb_resp = gsuiteaddons.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_replace_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_replace_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsuiteaddons.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.replace_deployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "ReplaceDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UninstallDeployment(
        _BaseGSuiteAddOnsRestTransport._BaseUninstallDeployment, GSuiteAddOnsRestStub
    ):
        def __hash__(self):
            return hash("GSuiteAddOnsRestTransport.UninstallDeployment")

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
            request: gsuiteaddons.UninstallDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the uninstall deployment method over HTTP.

            Args:
                request (~.gsuiteaddons.UninstallDeploymentRequest):
                    The request object. Request message to uninstall a
                developer mode deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseGSuiteAddOnsRestTransport._BaseUninstallDeployment._get_http_options()
            request, metadata = self._interceptor.pre_uninstall_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGSuiteAddOnsRestTransport._BaseUninstallDeployment,
                    "_BaseUninstallDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gsuiteaddons_v1.GSuiteAddOnsClient.UninstallDeployment",
                    extra={
                        "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                        "rpcName": "UninstallDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GSuiteAddOnsRestTransport._UninstallDeployment._get_response(
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

    @property
    def create_deployment(
        self,
    ) -> Callable[[gsuiteaddons.CreateDeploymentRequest], gsuiteaddons.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_deployment(
        self,
    ) -> Callable[[gsuiteaddons.DeleteDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_authorization(
        self,
    ) -> Callable[[gsuiteaddons.GetAuthorizationRequest], gsuiteaddons.Authorization]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuthorization(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deployment(
        self,
    ) -> Callable[[gsuiteaddons.GetDeploymentRequest], gsuiteaddons.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_install_status(
        self,
    ) -> Callable[[gsuiteaddons.GetInstallStatusRequest], gsuiteaddons.InstallStatus]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstallStatus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def install_deployment(
        self,
    ) -> Callable[[gsuiteaddons.InstallDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InstallDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [gsuiteaddons.ListDeploymentsRequest], gsuiteaddons.ListDeploymentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def replace_deployment(
        self,
    ) -> Callable[[gsuiteaddons.ReplaceDeploymentRequest], gsuiteaddons.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReplaceDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def uninstall_deployment(
        self,
    ) -> Callable[[gsuiteaddons.UninstallDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UninstallDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("GSuiteAddOnsRestTransport",)
