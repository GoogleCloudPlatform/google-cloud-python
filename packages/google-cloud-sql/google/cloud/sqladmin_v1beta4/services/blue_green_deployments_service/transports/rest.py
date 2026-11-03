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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.sqladmin_v1beta4._compat import transcode_request
from google.cloud.sqladmin_v1beta4.types import (
    cloud_sql_blue_green_deployments,
    cloud_sql_resources,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBlueGreenDeploymentsServiceRestTransport

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


class BlueGreenDeploymentsServiceRestInterceptor:
    """Interceptor for BlueGreenDeploymentsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BlueGreenDeploymentsServiceRestTransport.

    .. code-block:: python
        class MyCustomBlueGreenDeploymentsServiceInterceptor(BlueGreenDeploymentsServiceRestInterceptor):
            def pre_create_blue_green_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_blue_green_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_blue_green_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_blue_green_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_blue_green_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_blue_green_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_blue_green_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_blue_green_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_switchover_blue_green_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_switchover_blue_green_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BlueGreenDeploymentsServiceRestTransport(interceptor=MyCustomBlueGreenDeploymentsServiceInterceptor())
        client = BlueGreenDeploymentsServiceClient(transport=transport)


    """

    def pre_create_blue_green_deployment(
        self,
        request: cloud_sql_blue_green_deployments.CreateBlueGreenDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.CreateBlueGreenDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_blue_green_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BlueGreenDeploymentsService server.
        """
        return request, metadata

    def post_create_blue_green_deployment(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for create_blue_green_deployment

        DEPRECATED. Please use the `post_create_blue_green_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BlueGreenDeploymentsService server but before
        it is returned to user code. This `post_create_blue_green_deployment` interceptor runs
        before the `post_create_blue_green_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_blue_green_deployment_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_blue_green_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BlueGreenDeploymentsService server but before it is returned to user code.

        We recommend only using this `post_create_blue_green_deployment_with_metadata`
        interceptor in new development instead of the `post_create_blue_green_deployment` interceptor.
        When both interceptors are used, this `post_create_blue_green_deployment_with_metadata` interceptor runs after the
        `post_create_blue_green_deployment` interceptor. The (possibly modified) response returned by
        `post_create_blue_green_deployment` will be passed to
        `post_create_blue_green_deployment_with_metadata`.
        """
        return response, metadata

    def pre_delete_blue_green_deployment(
        self,
        request: cloud_sql_blue_green_deployments.DeleteBlueGreenDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.DeleteBlueGreenDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_blue_green_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BlueGreenDeploymentsService server.
        """
        return request, metadata

    def post_delete_blue_green_deployment(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for delete_blue_green_deployment

        DEPRECATED. Please use the `post_delete_blue_green_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BlueGreenDeploymentsService server but before
        it is returned to user code. This `post_delete_blue_green_deployment` interceptor runs
        before the `post_delete_blue_green_deployment_with_metadata` interceptor.
        """
        return response

    def post_delete_blue_green_deployment_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_blue_green_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BlueGreenDeploymentsService server but before it is returned to user code.

        We recommend only using this `post_delete_blue_green_deployment_with_metadata`
        interceptor in new development instead of the `post_delete_blue_green_deployment` interceptor.
        When both interceptors are used, this `post_delete_blue_green_deployment_with_metadata` interceptor runs after the
        `post_delete_blue_green_deployment` interceptor. The (possibly modified) response returned by
        `post_delete_blue_green_deployment` will be passed to
        `post_delete_blue_green_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_blue_green_deployment(
        self,
        request: cloud_sql_blue_green_deployments.GetBlueGreenDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.GetBlueGreenDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_blue_green_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BlueGreenDeploymentsService server.
        """
        return request, metadata

    def post_get_blue_green_deployment(
        self, response: cloud_sql_blue_green_deployments.BlueGreenDeployment
    ) -> cloud_sql_blue_green_deployments.BlueGreenDeployment:
        """Post-rpc interceptor for get_blue_green_deployment

        DEPRECATED. Please use the `post_get_blue_green_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BlueGreenDeploymentsService server but before
        it is returned to user code. This `post_get_blue_green_deployment` interceptor runs
        before the `post_get_blue_green_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_blue_green_deployment_with_metadata(
        self,
        response: cloud_sql_blue_green_deployments.BlueGreenDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.BlueGreenDeployment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_blue_green_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BlueGreenDeploymentsService server but before it is returned to user code.

        We recommend only using this `post_get_blue_green_deployment_with_metadata`
        interceptor in new development instead of the `post_get_blue_green_deployment` interceptor.
        When both interceptors are used, this `post_get_blue_green_deployment_with_metadata` interceptor runs after the
        `post_get_blue_green_deployment` interceptor. The (possibly modified) response returned by
        `post_get_blue_green_deployment` will be passed to
        `post_get_blue_green_deployment_with_metadata`.
        """
        return response, metadata

    def pre_list_blue_green_deployments(
        self,
        request: cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_blue_green_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BlueGreenDeploymentsService server.
        """
        return request, metadata

    def post_list_blue_green_deployments(
        self,
        response: cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse,
    ) -> cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse:
        """Post-rpc interceptor for list_blue_green_deployments

        DEPRECATED. Please use the `post_list_blue_green_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BlueGreenDeploymentsService server but before
        it is returned to user code. This `post_list_blue_green_deployments` interceptor runs
        before the `post_list_blue_green_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_blue_green_deployments_with_metadata(
        self,
        response: cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_blue_green_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BlueGreenDeploymentsService server but before it is returned to user code.

        We recommend only using this `post_list_blue_green_deployments_with_metadata`
        interceptor in new development instead of the `post_list_blue_green_deployments` interceptor.
        When both interceptors are used, this `post_list_blue_green_deployments_with_metadata` interceptor runs after the
        `post_list_blue_green_deployments` interceptor. The (possibly modified) response returned by
        `post_list_blue_green_deployments` will be passed to
        `post_list_blue_green_deployments_with_metadata`.
        """
        return response, metadata

    def pre_switchover_blue_green_deployment(
        self,
        request: cloud_sql_blue_green_deployments.SwitchoverBlueGreenDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_blue_green_deployments.SwitchoverBlueGreenDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for switchover_blue_green_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BlueGreenDeploymentsService server.
        """
        return request, metadata

    def post_switchover_blue_green_deployment(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for switchover_blue_green_deployment

        DEPRECATED. Please use the `post_switchover_blue_green_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BlueGreenDeploymentsService server but before
        it is returned to user code. This `post_switchover_blue_green_deployment` interceptor runs
        before the `post_switchover_blue_green_deployment_with_metadata` interceptor.
        """
        return response

    def post_switchover_blue_green_deployment_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for switchover_blue_green_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BlueGreenDeploymentsService server but before it is returned to user code.

        We recommend only using this `post_switchover_blue_green_deployment_with_metadata`
        interceptor in new development instead of the `post_switchover_blue_green_deployment` interceptor.
        When both interceptors are used, this `post_switchover_blue_green_deployment_with_metadata` interceptor runs after the
        `post_switchover_blue_green_deployment` interceptor. The (possibly modified) response returned by
        `post_switchover_blue_green_deployment` will be passed to
        `post_switchover_blue_green_deployment_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class BlueGreenDeploymentsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BlueGreenDeploymentsServiceRestInterceptor


class BlueGreenDeploymentsServiceRestTransport(
    _BaseBlueGreenDeploymentsServiceRestTransport
):
    """REST backend synchronous transport for BlueGreenDeploymentsService.

    Service for managing blue-green deployments.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "sqladmin.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BlueGreenDeploymentsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'sqladmin.googleapis.com').
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
            interceptor (Optional[BlueGreenDeploymentsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or BlueGreenDeploymentsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateBlueGreenDeployment(
        _BaseBlueGreenDeploymentsServiceRestTransport._BaseCreateBlueGreenDeployment,
        BlueGreenDeploymentsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "BlueGreenDeploymentsServiceRestTransport.CreateBlueGreenDeployment"
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
            request: cloud_sql_blue_green_deployments.CreateBlueGreenDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the create blue green
            deployment method over HTTP.

                Args:
                    request (~.cloud_sql_blue_green_deployments.CreateBlueGreenDeploymentRequest):
                        The request object. The request message for creating a
                    ``BlueGreenDeployment`` resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.Operation:
                        An Operation resource.&nbsp;For
                    successful operations that return an
                    Operation resource, only the fields
                    relevant to the operation are populated
                    in the resource.

            """

            http_options = _BaseBlueGreenDeploymentsServiceRestTransport._BaseCreateBlueGreenDeployment._get_http_options()
            request, metadata = self._interceptor.pre_create_blue_green_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBlueGreenDeploymentsServiceRestTransport._BaseCreateBlueGreenDeployment,
                    "_BaseCreateBlueGreenDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.CreateBlueGreenDeployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "CreateBlueGreenDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BlueGreenDeploymentsServiceRestTransport._CreateBlueGreenDeployment._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_blue_green_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_blue_green_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.create_blue_green_deployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "CreateBlueGreenDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBlueGreenDeployment(
        _BaseBlueGreenDeploymentsServiceRestTransport._BaseDeleteBlueGreenDeployment,
        BlueGreenDeploymentsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "BlueGreenDeploymentsServiceRestTransport.DeleteBlueGreenDeployment"
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
            request: cloud_sql_blue_green_deployments.DeleteBlueGreenDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the delete blue green
            deployment method over HTTP.

                Args:
                    request (~.cloud_sql_blue_green_deployments.DeleteBlueGreenDeploymentRequest):
                        The request object. Request message for deleting a ``BlueGreenDeployment``
                    resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.Operation:
                        An Operation resource.&nbsp;For
                    successful operations that return an
                    Operation resource, only the fields
                    relevant to the operation are populated
                    in the resource.

            """

            http_options = _BaseBlueGreenDeploymentsServiceRestTransport._BaseDeleteBlueGreenDeployment._get_http_options()
            request, metadata = self._interceptor.pre_delete_blue_green_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBlueGreenDeploymentsServiceRestTransport._BaseDeleteBlueGreenDeployment,
                    "_BaseDeleteBlueGreenDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.DeleteBlueGreenDeployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "DeleteBlueGreenDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BlueGreenDeploymentsServiceRestTransport._DeleteBlueGreenDeployment._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_blue_green_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_blue_green_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.delete_blue_green_deployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "DeleteBlueGreenDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBlueGreenDeployment(
        _BaseBlueGreenDeploymentsServiceRestTransport._BaseGetBlueGreenDeployment,
        BlueGreenDeploymentsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "BlueGreenDeploymentsServiceRestTransport.GetBlueGreenDeployment"
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
            request: cloud_sql_blue_green_deployments.GetBlueGreenDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_blue_green_deployments.BlueGreenDeployment:
            r"""Call the get blue green deployment method over HTTP.

            Args:
                request (~.cloud_sql_blue_green_deployments.GetBlueGreenDeploymentRequest):
                    The request object. The request message for getting a
                ``BlueGreenDeployment`` resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_blue_green_deployments.BlueGreenDeployment:
                    A ``BlueGreenDeployment`` resource represents a Cloud
                SQL blue-green deployment setup. It orchestrates the
                lifecycle of creating a synchronized "green" environment
                from a "blue" production environment, performing
                updates, and managing the switchover process to minimize
                downtime.

            """

            http_options = _BaseBlueGreenDeploymentsServiceRestTransport._BaseGetBlueGreenDeployment._get_http_options()
            request, metadata = self._interceptor.pre_get_blue_green_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBlueGreenDeploymentsServiceRestTransport._BaseGetBlueGreenDeployment,
                    "_BaseGetBlueGreenDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.GetBlueGreenDeployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "GetBlueGreenDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BlueGreenDeploymentsServiceRestTransport._GetBlueGreenDeployment._get_response(
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
            resp = cloud_sql_blue_green_deployments.BlueGreenDeployment()
            pb_resp = cloud_sql_blue_green_deployments.BlueGreenDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_blue_green_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_blue_green_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_sql_blue_green_deployments.BlueGreenDeployment.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.get_blue_green_deployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "GetBlueGreenDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBlueGreenDeployments(
        _BaseBlueGreenDeploymentsServiceRestTransport._BaseListBlueGreenDeployments,
        BlueGreenDeploymentsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "BlueGreenDeploymentsServiceRestTransport.ListBlueGreenDeployments"
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
            request: cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse:
            r"""Call the list blue green
            deployments method over HTTP.

                Args:
                    request (~.cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsRequest):
                        The request object. The request message for listing
                    blue-green deployment resources.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse:
                        The response message for listing
                    blue-green deployment resources.

            """

            http_options = _BaseBlueGreenDeploymentsServiceRestTransport._BaseListBlueGreenDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_blue_green_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBlueGreenDeploymentsServiceRestTransport._BaseListBlueGreenDeployments,
                    "_BaseListBlueGreenDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.ListBlueGreenDeployments",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "ListBlueGreenDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BlueGreenDeploymentsServiceRestTransport._ListBlueGreenDeployments._get_response(
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
            resp = cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse()
            pb_resp = (
                cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_blue_green_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_blue_green_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.list_blue_green_deployments",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "ListBlueGreenDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SwitchoverBlueGreenDeployment(
        _BaseBlueGreenDeploymentsServiceRestTransport._BaseSwitchoverBlueGreenDeployment,
        BlueGreenDeploymentsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "BlueGreenDeploymentsServiceRestTransport.SwitchoverBlueGreenDeployment"
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
            request: cloud_sql_blue_green_deployments.SwitchoverBlueGreenDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the switchover blue green
            deployment method over HTTP.

                Args:
                    request (~.cloud_sql_blue_green_deployments.SwitchoverBlueGreenDeploymentRequest):
                        The request object. Request message for switching over a
                    ``BlueGreenDeployment`` resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.Operation:
                        An Operation resource.&nbsp;For
                    successful operations that return an
                    Operation resource, only the fields
                    relevant to the operation are populated
                    in the resource.

            """

            http_options = _BaseBlueGreenDeploymentsServiceRestTransport._BaseSwitchoverBlueGreenDeployment._get_http_options()
            request, metadata = self._interceptor.pre_switchover_blue_green_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBlueGreenDeploymentsServiceRestTransport._BaseSwitchoverBlueGreenDeployment,
                    "_BaseSwitchoverBlueGreenDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.SwitchoverBlueGreenDeployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "SwitchoverBlueGreenDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BlueGreenDeploymentsServiceRestTransport._SwitchoverBlueGreenDeployment._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_switchover_blue_green_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_switchover_blue_green_deployment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.BlueGreenDeploymentsServiceClient.switchover_blue_green_deployment",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.BlueGreenDeploymentsService",
                        "rpcName": "SwitchoverBlueGreenDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_blue_green_deployment(
        self,
    ) -> Callable[
        [cloud_sql_blue_green_deployments.CreateBlueGreenDeploymentRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBlueGreenDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_blue_green_deployment(
        self,
    ) -> Callable[
        [cloud_sql_blue_green_deployments.DeleteBlueGreenDeploymentRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBlueGreenDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_blue_green_deployment(
        self,
    ) -> Callable[
        [cloud_sql_blue_green_deployments.GetBlueGreenDeploymentRequest],
        cloud_sql_blue_green_deployments.BlueGreenDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBlueGreenDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_blue_green_deployments(
        self,
    ) -> Callable[
        [cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsRequest],
        cloud_sql_blue_green_deployments.ListBlueGreenDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBlueGreenDeployments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def switchover_blue_green_deployment(
        self,
    ) -> Callable[
        [cloud_sql_blue_green_deployments.SwitchoverBlueGreenDeploymentRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SwitchoverBlueGreenDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("BlueGreenDeploymentsServiceRestTransport",)
