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

from google.cloud.binaryauthorization_v1beta1._compat import transcode_request
from google.cloud.binaryauthorization_v1beta1.types import resources, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBinauthzManagementServiceV1Beta1RestTransport

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


class BinauthzManagementServiceV1Beta1RestInterceptor:
    """Interceptor for BinauthzManagementServiceV1Beta1.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BinauthzManagementServiceV1Beta1RestTransport.

    .. code-block:: python
        class MyCustomBinauthzManagementServiceV1Beta1Interceptor(BinauthzManagementServiceV1Beta1RestInterceptor):
            def pre_create_attestor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_attestor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_attestor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_attestor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_attestor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_attestors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_attestors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_attestor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_attestor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BinauthzManagementServiceV1Beta1RestTransport(interceptor=MyCustomBinauthzManagementServiceV1Beta1Interceptor())
        client = BinauthzManagementServiceV1Beta1Client(transport=transport)


    """

    def pre_create_attestor(
        self,
        request: service.CreateAttestorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateAttestorRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_attestor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_create_attestor(self, response: resources.Attestor) -> resources.Attestor:
        """Post-rpc interceptor for create_attestor

        DEPRECATED. Please use the `post_create_attestor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code. This `post_create_attestor` interceptor runs
        before the `post_create_attestor_with_metadata` interceptor.
        """
        return response

    def post_create_attestor_with_metadata(
        self,
        response: resources.Attestor,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Attestor, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_attestor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BinauthzManagementServiceV1Beta1 server but before it is returned to user code.

        We recommend only using this `post_create_attestor_with_metadata`
        interceptor in new development instead of the `post_create_attestor` interceptor.
        When both interceptors are used, this `post_create_attestor_with_metadata` interceptor runs after the
        `post_create_attestor` interceptor. The (possibly modified) response returned by
        `post_create_attestor` will be passed to
        `post_create_attestor_with_metadata`.
        """
        return response, metadata

    def pre_delete_attestor(
        self,
        request: service.DeleteAttestorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteAttestorRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_attestor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def pre_get_attestor(
        self,
        request: service.GetAttestorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetAttestorRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_attestor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_get_attestor(self, response: resources.Attestor) -> resources.Attestor:
        """Post-rpc interceptor for get_attestor

        DEPRECATED. Please use the `post_get_attestor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code. This `post_get_attestor` interceptor runs
        before the `post_get_attestor_with_metadata` interceptor.
        """
        return response

    def post_get_attestor_with_metadata(
        self,
        response: resources.Attestor,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Attestor, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_attestor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BinauthzManagementServiceV1Beta1 server but before it is returned to user code.

        We recommend only using this `post_get_attestor_with_metadata`
        interceptor in new development instead of the `post_get_attestor` interceptor.
        When both interceptors are used, this `post_get_attestor_with_metadata` interceptor runs after the
        `post_get_attestor` interceptor. The (possibly modified) response returned by
        `post_get_attestor` will be passed to
        `post_get_attestor_with_metadata`.
        """
        return response, metadata

    def pre_get_policy(
        self,
        request: service.GetPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_get_policy(self, response: resources.Policy) -> resources.Policy:
        """Post-rpc interceptor for get_policy

        DEPRECATED. Please use the `post_get_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code. This `post_get_policy` interceptor runs
        before the `post_get_policy_with_metadata` interceptor.
        """
        return response

    def post_get_policy_with_metadata(
        self,
        response: resources.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BinauthzManagementServiceV1Beta1 server but before it is returned to user code.

        We recommend only using this `post_get_policy_with_metadata`
        interceptor in new development instead of the `post_get_policy` interceptor.
        When both interceptors are used, this `post_get_policy_with_metadata` interceptor runs after the
        `post_get_policy` interceptor. The (possibly modified) response returned by
        `post_get_policy` will be passed to
        `post_get_policy_with_metadata`.
        """
        return response, metadata

    def pre_list_attestors(
        self,
        request: service.ListAttestorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListAttestorsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_attestors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_list_attestors(
        self, response: service.ListAttestorsResponse
    ) -> service.ListAttestorsResponse:
        """Post-rpc interceptor for list_attestors

        DEPRECATED. Please use the `post_list_attestors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code. This `post_list_attestors` interceptor runs
        before the `post_list_attestors_with_metadata` interceptor.
        """
        return response

    def post_list_attestors_with_metadata(
        self,
        response: service.ListAttestorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListAttestorsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_attestors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BinauthzManagementServiceV1Beta1 server but before it is returned to user code.

        We recommend only using this `post_list_attestors_with_metadata`
        interceptor in new development instead of the `post_list_attestors` interceptor.
        When both interceptors are used, this `post_list_attestors_with_metadata` interceptor runs after the
        `post_list_attestors` interceptor. The (possibly modified) response returned by
        `post_list_attestors` will be passed to
        `post_list_attestors_with_metadata`.
        """
        return response, metadata

    def pre_update_attestor(
        self,
        request: service.UpdateAttestorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateAttestorRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_attestor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_update_attestor(self, response: resources.Attestor) -> resources.Attestor:
        """Post-rpc interceptor for update_attestor

        DEPRECATED. Please use the `post_update_attestor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code. This `post_update_attestor` interceptor runs
        before the `post_update_attestor_with_metadata` interceptor.
        """
        return response

    def post_update_attestor_with_metadata(
        self,
        response: resources.Attestor,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Attestor, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_attestor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BinauthzManagementServiceV1Beta1 server but before it is returned to user code.

        We recommend only using this `post_update_attestor_with_metadata`
        interceptor in new development instead of the `post_update_attestor` interceptor.
        When both interceptors are used, this `post_update_attestor_with_metadata` interceptor runs after the
        `post_update_attestor` interceptor. The (possibly modified) response returned by
        `post_update_attestor` will be passed to
        `post_update_attestor_with_metadata`.
        """
        return response, metadata

    def pre_update_policy(
        self,
        request: service.UpdatePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdatePolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_update_policy(self, response: resources.Policy) -> resources.Policy:
        """Post-rpc interceptor for update_policy

        DEPRECATED. Please use the `post_update_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code. This `post_update_policy` interceptor runs
        before the `post_update_policy_with_metadata` interceptor.
        """
        return response

    def post_update_policy_with_metadata(
        self,
        response: resources.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BinauthzManagementServiceV1Beta1 server but before it is returned to user code.

        We recommend only using this `post_update_policy_with_metadata`
        interceptor in new development instead of the `post_update_policy` interceptor.
        When both interceptors are used, this `post_update_policy_with_metadata` interceptor runs after the
        `post_update_policy` interceptor. The (possibly modified) response returned by
        `post_update_policy` will be passed to
        `post_update_policy_with_metadata`.
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
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
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
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
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
        before they are sent to the BinauthzManagementServiceV1Beta1 server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the BinauthzManagementServiceV1Beta1 server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class BinauthzManagementServiceV1Beta1RestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BinauthzManagementServiceV1Beta1RestInterceptor


class BinauthzManagementServiceV1Beta1RestTransport(
    _BaseBinauthzManagementServiceV1Beta1RestTransport
):
    """REST backend synchronous transport for BinauthzManagementServiceV1Beta1.

    Google Cloud Management Service for Binary Authorization admission
    policies and attestation authorities.

    This API implements a REST model with the following objects:

    - [Policy][google.cloud.binaryauthorization.v1beta1.Policy]
    - [Attestor][google.cloud.binaryauthorization.v1beta1.Attestor]

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "binaryauthorization.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BinauthzManagementServiceV1Beta1RestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'binaryauthorization.googleapis.com').
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
            interceptor (Optional[BinauthzManagementServiceV1Beta1RestInterceptor]): Interceptor used
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
            interceptor or BinauthzManagementServiceV1Beta1RestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CreateAttestor(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseCreateAttestor,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.CreateAttestor")

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
            request: service.CreateAttestorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Attestor:
            r"""Call the create attestor method over HTTP.

            Args:
                request (~.service.CreateAttestorRequest):
                    The request object. Request message for
                [BinauthzManagementService.CreateAttestor][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Attestor:
                    An
                [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
                that attests to container image artifacts. An existing
                attestor cannot be modified except where indicated.

            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseCreateAttestor._get_http_options()
            request, metadata = self._interceptor.pre_create_attestor(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseCreateAttestor,
                    "_BaseCreateAttestor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.CreateAttestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "CreateAttestor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._CreateAttestor._get_response(
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
            resp = resources.Attestor()
            pb_resp = resources.Attestor.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_attestor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_attestor_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Attestor.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.create_attestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "CreateAttestor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAttestor(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseDeleteAttestor,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.DeleteAttestor")

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
            request: service.DeleteAttestorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete attestor method over HTTP.

            Args:
                request (~.service.DeleteAttestorRequest):
                    The request object. Request message for
                [BinauthzManagementService.DeleteAttestor][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseDeleteAttestor._get_http_options()
            request, metadata = self._interceptor.pre_delete_attestor(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseDeleteAttestor,
                    "_BaseDeleteAttestor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.DeleteAttestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "DeleteAttestor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._DeleteAttestor._get_response(
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

    class _GetAttestor(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetAttestor,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.GetAttestor")

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
            request: service.GetAttestorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Attestor:
            r"""Call the get attestor method over HTTP.

            Args:
                request (~.service.GetAttestorRequest):
                    The request object. Request message for
                [BinauthzManagementService.GetAttestor][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Attestor:
                    An
                [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
                that attests to container image artifacts. An existing
                attestor cannot be modified except where indicated.

            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetAttestor._get_http_options()
            request, metadata = self._interceptor.pre_get_attestor(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetAttestor,
                    "_BaseGetAttestor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.GetAttestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "GetAttestor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._GetAttestor._get_response(
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
            resp = resources.Attestor()
            pb_resp = resources.Attestor.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_attestor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_attestor_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Attestor.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.get_attestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "GetAttestor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPolicy(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetPolicy,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.GetPolicy")

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
            request: service.GetPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Policy:
            r"""Call the get policy method over HTTP.

            Args:
                request (~.service.GetPolicyRequest):
                    The request object. Request message for
                [BinauthzManagementService.GetPolicy][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Policy:
                    A
                [policy][google.cloud.binaryauthorization.v1beta1.Policy]
                for Binary Authorization.

            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetPolicy,
                    "_BaseGetPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.GetPolicy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "GetPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BinauthzManagementServiceV1Beta1RestTransport._GetPolicy._get_response(
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
            resp = resources.Policy()
            pb_resp = resources.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.get_policy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "GetPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAttestors(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseListAttestors,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.ListAttestors")

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
            request: service.ListAttestorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListAttestorsResponse:
            r"""Call the list attestors method over HTTP.

            Args:
                request (~.service.ListAttestorsRequest):
                    The request object. Request message for
                [BinauthzManagementService.ListAttestors][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListAttestorsResponse:
                    Response message for
                [BinauthzManagementService.ListAttestors][].

            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseListAttestors._get_http_options()
            request, metadata = self._interceptor.pre_list_attestors(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseListAttestors,
                    "_BaseListAttestors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.ListAttestors",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "ListAttestors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._ListAttestors._get_response(
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
            resp = service.ListAttestorsResponse()
            pb_resp = service.ListAttestorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_attestors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_attestors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListAttestorsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.list_attestors",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "ListAttestors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAttestor(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseUpdateAttestor,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.UpdateAttestor")

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
            request: service.UpdateAttestorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Attestor:
            r"""Call the update attestor method over HTTP.

            Args:
                request (~.service.UpdateAttestorRequest):
                    The request object. Request message for
                [BinauthzManagementService.UpdateAttestor][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Attestor:
                    An
                [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
                that attests to container image artifacts. An existing
                attestor cannot be modified except where indicated.

            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseUpdateAttestor._get_http_options()
            request, metadata = self._interceptor.pre_update_attestor(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseUpdateAttestor,
                    "_BaseUpdateAttestor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.UpdateAttestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "UpdateAttestor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._UpdateAttestor._get_response(
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
            resp = resources.Attestor()
            pb_resp = resources.Attestor.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_attestor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_attestor_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Attestor.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.update_attestor",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "UpdateAttestor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePolicy(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseUpdatePolicy,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.UpdatePolicy")

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
            request: service.UpdatePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Policy:
            r"""Call the update policy method over HTTP.

            Args:
                request (~.service.UpdatePolicyRequest):
                    The request object. Request message for
                [BinauthzManagementService.UpdatePolicy][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Policy:
                    A
                [policy][google.cloud.binaryauthorization.v1beta1.Policy]
                for Binary Authorization.

            """

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseUpdatePolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseUpdatePolicy,
                    "_BaseUpdatePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.UpdatePolicy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "UpdatePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._UpdatePolicy._get_response(
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
            resp = resources.Policy()
            pb_resp = resources.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.update_policy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "UpdatePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_attestor(
        self,
    ) -> Callable[[service.CreateAttestorRequest], resources.Attestor]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAttestor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_attestor(
        self,
    ) -> Callable[[service.DeleteAttestorRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAttestor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_attestor(
        self,
    ) -> Callable[[service.GetAttestorRequest], resources.Attestor]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAttestor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_policy(self) -> Callable[[service.GetPolicyRequest], resources.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_attestors(
        self,
    ) -> Callable[[service.ListAttestorsRequest], service.ListAttestorsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAttestors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_attestor(
        self,
    ) -> Callable[[service.UpdateAttestorRequest], resources.Attestor]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAttestor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_policy(
        self,
    ) -> Callable[[service.UpdatePolicyRequest], resources.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetIamPolicy,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.GetIamPolicy")

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

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1AsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
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
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseSetIamPolicy,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash("BinauthzManagementServiceV1Beta1RestTransport.SetIamPolicy")

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

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1AsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
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
        _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseTestIamPermissions,
        BinauthzManagementServiceV1Beta1RestStub,
    ):
        def __hash__(self):
            return hash(
                "BinauthzManagementServiceV1Beta1RestTransport.TestIamPermissions"
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

            http_options = _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBinauthzManagementServiceV1Beta1RestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1Client.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BinauthzManagementServiceV1Beta1RestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.binaryauthorization_v1beta1.BinauthzManagementServiceV1Beta1AsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1",
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


__all__ = ("BinauthzManagementServiceV1Beta1RestTransport",)
