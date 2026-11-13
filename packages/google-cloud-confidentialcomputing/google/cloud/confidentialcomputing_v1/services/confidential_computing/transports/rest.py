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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.confidentialcomputing_v1._compat import transcode_request
from google.cloud.confidentialcomputing_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseConfidentialComputingRestTransport

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


class ConfidentialComputingRestInterceptor:
    """Interceptor for ConfidentialComputing.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ConfidentialComputingRestTransport.

    .. code-block:: python
        class MyCustomConfidentialComputingInterceptor(ConfidentialComputingRestInterceptor):
            def pre_create_challenge(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_challenge(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_attestation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_attestation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_confidential_gke(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_confidential_gke(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_confidential_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_confidential_space(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ConfidentialComputingRestTransport(interceptor=MyCustomConfidentialComputingInterceptor())
        client = ConfidentialComputingClient(transport=transport)


    """

    def pre_create_challenge(
        self,
        request: service.CreateChallengeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateChallengeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_challenge

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfidentialComputing server.
        """
        return request, metadata

    def post_create_challenge(self, response: service.Challenge) -> service.Challenge:
        """Post-rpc interceptor for create_challenge

        DEPRECATED. Please use the `post_create_challenge_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfidentialComputing server but before
        it is returned to user code. This `post_create_challenge` interceptor runs
        before the `post_create_challenge_with_metadata` interceptor.
        """
        return response

    def post_create_challenge_with_metadata(
        self,
        response: service.Challenge,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Challenge, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_challenge

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfidentialComputing server but before it is returned to user code.

        We recommend only using this `post_create_challenge_with_metadata`
        interceptor in new development instead of the `post_create_challenge` interceptor.
        When both interceptors are used, this `post_create_challenge_with_metadata` interceptor runs after the
        `post_create_challenge` interceptor. The (possibly modified) response returned by
        `post_create_challenge` will be passed to
        `post_create_challenge_with_metadata`.
        """
        return response, metadata

    def pre_verify_attestation(
        self,
        request: service.VerifyAttestationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.VerifyAttestationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for verify_attestation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfidentialComputing server.
        """
        return request, metadata

    def post_verify_attestation(
        self, response: service.VerifyAttestationResponse
    ) -> service.VerifyAttestationResponse:
        """Post-rpc interceptor for verify_attestation

        DEPRECATED. Please use the `post_verify_attestation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfidentialComputing server but before
        it is returned to user code. This `post_verify_attestation` interceptor runs
        before the `post_verify_attestation_with_metadata` interceptor.
        """
        return response

    def post_verify_attestation_with_metadata(
        self,
        response: service.VerifyAttestationResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.VerifyAttestationResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for verify_attestation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfidentialComputing server but before it is returned to user code.

        We recommend only using this `post_verify_attestation_with_metadata`
        interceptor in new development instead of the `post_verify_attestation` interceptor.
        When both interceptors are used, this `post_verify_attestation_with_metadata` interceptor runs after the
        `post_verify_attestation` interceptor. The (possibly modified) response returned by
        `post_verify_attestation` will be passed to
        `post_verify_attestation_with_metadata`.
        """
        return response, metadata

    def pre_verify_confidential_gke(
        self,
        request: service.VerifyConfidentialGkeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.VerifyConfidentialGkeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for verify_confidential_gke

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfidentialComputing server.
        """
        return request, metadata

    def post_verify_confidential_gke(
        self, response: service.VerifyConfidentialGkeResponse
    ) -> service.VerifyConfidentialGkeResponse:
        """Post-rpc interceptor for verify_confidential_gke

        DEPRECATED. Please use the `post_verify_confidential_gke_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfidentialComputing server but before
        it is returned to user code. This `post_verify_confidential_gke` interceptor runs
        before the `post_verify_confidential_gke_with_metadata` interceptor.
        """
        return response

    def post_verify_confidential_gke_with_metadata(
        self,
        response: service.VerifyConfidentialGkeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.VerifyConfidentialGkeResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for verify_confidential_gke

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfidentialComputing server but before it is returned to user code.

        We recommend only using this `post_verify_confidential_gke_with_metadata`
        interceptor in new development instead of the `post_verify_confidential_gke` interceptor.
        When both interceptors are used, this `post_verify_confidential_gke_with_metadata` interceptor runs after the
        `post_verify_confidential_gke` interceptor. The (possibly modified) response returned by
        `post_verify_confidential_gke` will be passed to
        `post_verify_confidential_gke_with_metadata`.
        """
        return response, metadata

    def pre_verify_confidential_space(
        self,
        request: service.VerifyConfidentialSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.VerifyConfidentialSpaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for verify_confidential_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfidentialComputing server.
        """
        return request, metadata

    def post_verify_confidential_space(
        self, response: service.VerifyConfidentialSpaceResponse
    ) -> service.VerifyConfidentialSpaceResponse:
        """Post-rpc interceptor for verify_confidential_space

        DEPRECATED. Please use the `post_verify_confidential_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfidentialComputing server but before
        it is returned to user code. This `post_verify_confidential_space` interceptor runs
        before the `post_verify_confidential_space_with_metadata` interceptor.
        """
        return response

    def post_verify_confidential_space_with_metadata(
        self,
        response: service.VerifyConfidentialSpaceResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.VerifyConfidentialSpaceResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for verify_confidential_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfidentialComputing server but before it is returned to user code.

        We recommend only using this `post_verify_confidential_space_with_metadata`
        interceptor in new development instead of the `post_verify_confidential_space` interceptor.
        When both interceptors are used, this `post_verify_confidential_space_with_metadata` interceptor runs after the
        `post_verify_confidential_space` interceptor. The (possibly modified) response returned by
        `post_verify_confidential_space` will be passed to
        `post_verify_confidential_space_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfidentialComputing server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ConfidentialComputing server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfidentialComputing server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ConfidentialComputing server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ConfidentialComputingRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ConfidentialComputingRestInterceptor


class ConfidentialComputingRestTransport(_BaseConfidentialComputingRestTransport):
    """REST backend synchronous transport for ConfidentialComputing.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "confidentialcomputing.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ConfidentialComputingRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'confidentialcomputing.googleapis.com').
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
            interceptor (Optional[ConfidentialComputingRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ConfidentialComputingRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateChallenge(
        _BaseConfidentialComputingRestTransport._BaseCreateChallenge,
        ConfidentialComputingRestStub,
    ):
        def __hash__(self):
            return hash("ConfidentialComputingRestTransport.CreateChallenge")

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
            request: service.CreateChallengeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Challenge:
            r"""Call the create challenge method over HTTP.

            Args:
                request (~.service.CreateChallengeRequest):
                    The request object. Message for creating a Challenge
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Challenge:
                    A Challenge from the server used to
                guarantee freshness of attestations

            """

            http_options = _BaseConfidentialComputingRestTransport._BaseCreateChallenge._get_http_options()
            request, metadata = self._interceptor.pre_create_challenge(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfidentialComputingRestTransport._BaseCreateChallenge,
                    "_BaseCreateChallenge__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.CreateChallenge",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "CreateChallenge",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConfidentialComputingRestTransport._CreateChallenge._get_response(
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
            resp = service.Challenge()
            pb_resp = service.Challenge.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_challenge(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_challenge_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Challenge.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.create_challenge",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "CreateChallenge",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyAttestation(
        _BaseConfidentialComputingRestTransport._BaseVerifyAttestation,
        ConfidentialComputingRestStub,
    ):
        def __hash__(self):
            return hash("ConfidentialComputingRestTransport.VerifyAttestation")

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
            request: service.VerifyAttestationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.VerifyAttestationResponse:
            r"""Call the verify attestation method over HTTP.

            Args:
                request (~.service.VerifyAttestationRequest):
                    The request object. A request for an attestation token,
                providing all the necessary information
                needed for this service to verify the
                platform state of the requestor.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.VerifyAttestationResponse:
                    A response once an attestation has
                been successfully verified, containing a
                signed attestation token.

            """

            http_options = _BaseConfidentialComputingRestTransport._BaseVerifyAttestation._get_http_options()
            request, metadata = self._interceptor.pre_verify_attestation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfidentialComputingRestTransport._BaseVerifyAttestation,
                    "_BaseVerifyAttestation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.VerifyAttestation",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "VerifyAttestation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConfidentialComputingRestTransport._VerifyAttestation._get_response(
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
            resp = service.VerifyAttestationResponse()
            pb_resp = service.VerifyAttestationResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_attestation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_verify_attestation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.VerifyAttestationResponse.to_json(
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
                    "Received response for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.verify_attestation",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "VerifyAttestation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyConfidentialGke(
        _BaseConfidentialComputingRestTransport._BaseVerifyConfidentialGke,
        ConfidentialComputingRestStub,
    ):
        def __hash__(self):
            return hash("ConfidentialComputingRestTransport.VerifyConfidentialGke")

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
            request: service.VerifyConfidentialGkeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.VerifyConfidentialGkeResponse:
            r"""Call the verify confidential gke method over HTTP.

            Args:
                request (~.service.VerifyConfidentialGkeRequest):
                    The request object. A request for an attestation token,
                providing all the necessary information
                needed for this service to verify
                Confidential GKE platform state of the
                requestor.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.VerifyConfidentialGkeResponse:
                    VerifyConfidentialGkeResponse
                response is returened once a
                Confidential GKE attestation has been
                successfully verified, containing a
                signed OIDC token.

            """

            http_options = _BaseConfidentialComputingRestTransport._BaseVerifyConfidentialGke._get_http_options()
            request, metadata = self._interceptor.pre_verify_confidential_gke(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfidentialComputingRestTransport._BaseVerifyConfidentialGke,
                    "_BaseVerifyConfidentialGke__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.VerifyConfidentialGke",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "VerifyConfidentialGke",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConfidentialComputingRestTransport._VerifyConfidentialGke._get_response(
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
            resp = service.VerifyConfidentialGkeResponse()
            pb_resp = service.VerifyConfidentialGkeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_confidential_gke(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_verify_confidential_gke_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.VerifyConfidentialGkeResponse.to_json(
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
                    "Received response for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.verify_confidential_gke",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "VerifyConfidentialGke",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyConfidentialSpace(
        _BaseConfidentialComputingRestTransport._BaseVerifyConfidentialSpace,
        ConfidentialComputingRestStub,
    ):
        def __hash__(self):
            return hash("ConfidentialComputingRestTransport.VerifyConfidentialSpace")

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
            request: service.VerifyConfidentialSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.VerifyConfidentialSpaceResponse:
            r"""Call the verify confidential space method over HTTP.

            Args:
                request (~.service.VerifyConfidentialSpaceRequest):
                    The request object. A request for an attestation token,
                providing all the necessary information
                needed for this service to verify the
                platform state of the requestor.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.VerifyConfidentialSpaceResponse:
                    VerifyConfidentialSpaceResponse is
                returned once a Confidential Space
                attestation has been successfully
                verified, containing a signed token.

            """

            http_options = _BaseConfidentialComputingRestTransport._BaseVerifyConfidentialSpace._get_http_options()
            request, metadata = self._interceptor.pre_verify_confidential_space(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfidentialComputingRestTransport._BaseVerifyConfidentialSpace,
                    "_BaseVerifyConfidentialSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.VerifyConfidentialSpace",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "VerifyConfidentialSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfidentialComputingRestTransport._VerifyConfidentialSpace._get_response(
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
            resp = service.VerifyConfidentialSpaceResponse()
            pb_resp = service.VerifyConfidentialSpaceResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_confidential_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_verify_confidential_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.VerifyConfidentialSpaceResponse.to_json(
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
                    "Received response for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.verify_confidential_space",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "VerifyConfidentialSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_challenge(
        self,
    ) -> Callable[[service.CreateChallengeRequest], service.Challenge]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateChallenge(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def verify_attestation(
        self,
    ) -> Callable[
        [service.VerifyAttestationRequest], service.VerifyAttestationResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyAttestation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def verify_confidential_gke(
        self,
    ) -> Callable[
        [service.VerifyConfidentialGkeRequest], service.VerifyConfidentialGkeResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyConfidentialGke(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def verify_confidential_space(
        self,
    ) -> Callable[
        [service.VerifyConfidentialSpaceRequest],
        service.VerifyConfidentialSpaceResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyConfidentialSpace(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseConfidentialComputingRestTransport._BaseGetLocation,
        ConfidentialComputingRestStub,
    ):
        def __hash__(self):
            return hash("ConfidentialComputingRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseConfidentialComputingRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfidentialComputingRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfidentialComputingRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.confidentialcomputing_v1.ConfidentialComputingAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseConfidentialComputingRestTransport._BaseListLocations,
        ConfidentialComputingRestStub,
    ):
        def __hash__(self):
            return hash("ConfidentialComputingRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseConfidentialComputingRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfidentialComputingRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.confidentialcomputing_v1.ConfidentialComputingClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfidentialComputingRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.confidentialcomputing_v1.ConfidentialComputingAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.confidentialcomputing.v1.ConfidentialComputing",
                        "rpcName": "ListLocations",
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


__all__ = ("ConfidentialComputingRestTransport",)
