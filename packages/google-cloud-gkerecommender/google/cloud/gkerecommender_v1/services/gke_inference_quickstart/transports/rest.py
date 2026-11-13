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

from google.cloud.gkerecommender_v1._compat import transcode_request
from google.cloud.gkerecommender_v1.types import gkerecommender

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseGkeInferenceQuickstartRestTransport

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


class GkeInferenceQuickstartRestInterceptor:
    """Interceptor for GkeInferenceQuickstart.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GkeInferenceQuickstartRestTransport.

    .. code-block:: python
        class MyCustomGkeInferenceQuickstartInterceptor(GkeInferenceQuickstartRestInterceptor):
            def pre_fetch_benchmarking_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_benchmarking_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_model_servers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_model_servers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_model_server_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_model_server_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_optimized_manifest(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_optimized_manifest(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = GkeInferenceQuickstartRestTransport(interceptor=MyCustomGkeInferenceQuickstartInterceptor())
        client = GkeInferenceQuickstartClient(transport=transport)


    """

    def pre_fetch_benchmarking_data(
        self,
        request: gkerecommender.FetchBenchmarkingDataRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchBenchmarkingDataRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_benchmarking_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeInferenceQuickstart server.
        """
        return request, metadata

    def post_fetch_benchmarking_data(
        self, response: gkerecommender.FetchBenchmarkingDataResponse
    ) -> gkerecommender.FetchBenchmarkingDataResponse:
        """Post-rpc interceptor for fetch_benchmarking_data

        DEPRECATED. Please use the `post_fetch_benchmarking_data_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeInferenceQuickstart server but before
        it is returned to user code. This `post_fetch_benchmarking_data` interceptor runs
        before the `post_fetch_benchmarking_data_with_metadata` interceptor.
        """
        return response

    def post_fetch_benchmarking_data_with_metadata(
        self,
        response: gkerecommender.FetchBenchmarkingDataResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchBenchmarkingDataResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_benchmarking_data

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeInferenceQuickstart server but before it is returned to user code.

        We recommend only using this `post_fetch_benchmarking_data_with_metadata`
        interceptor in new development instead of the `post_fetch_benchmarking_data` interceptor.
        When both interceptors are used, this `post_fetch_benchmarking_data_with_metadata` interceptor runs after the
        `post_fetch_benchmarking_data` interceptor. The (possibly modified) response returned by
        `post_fetch_benchmarking_data` will be passed to
        `post_fetch_benchmarking_data_with_metadata`.
        """
        return response, metadata

    def pre_fetch_models(
        self,
        request: gkerecommender.FetchModelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchModelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeInferenceQuickstart server.
        """
        return request, metadata

    def post_fetch_models(
        self, response: gkerecommender.FetchModelsResponse
    ) -> gkerecommender.FetchModelsResponse:
        """Post-rpc interceptor for fetch_models

        DEPRECATED. Please use the `post_fetch_models_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeInferenceQuickstart server but before
        it is returned to user code. This `post_fetch_models` interceptor runs
        before the `post_fetch_models_with_metadata` interceptor.
        """
        return response

    def post_fetch_models_with_metadata(
        self,
        response: gkerecommender.FetchModelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchModelsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_models

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeInferenceQuickstart server but before it is returned to user code.

        We recommend only using this `post_fetch_models_with_metadata`
        interceptor in new development instead of the `post_fetch_models` interceptor.
        When both interceptors are used, this `post_fetch_models_with_metadata` interceptor runs after the
        `post_fetch_models` interceptor. The (possibly modified) response returned by
        `post_fetch_models` will be passed to
        `post_fetch_models_with_metadata`.
        """
        return response, metadata

    def pre_fetch_model_servers(
        self,
        request: gkerecommender.FetchModelServersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchModelServersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_model_servers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeInferenceQuickstart server.
        """
        return request, metadata

    def post_fetch_model_servers(
        self, response: gkerecommender.FetchModelServersResponse
    ) -> gkerecommender.FetchModelServersResponse:
        """Post-rpc interceptor for fetch_model_servers

        DEPRECATED. Please use the `post_fetch_model_servers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeInferenceQuickstart server but before
        it is returned to user code. This `post_fetch_model_servers` interceptor runs
        before the `post_fetch_model_servers_with_metadata` interceptor.
        """
        return response

    def post_fetch_model_servers_with_metadata(
        self,
        response: gkerecommender.FetchModelServersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchModelServersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_model_servers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeInferenceQuickstart server but before it is returned to user code.

        We recommend only using this `post_fetch_model_servers_with_metadata`
        interceptor in new development instead of the `post_fetch_model_servers` interceptor.
        When both interceptors are used, this `post_fetch_model_servers_with_metadata` interceptor runs after the
        `post_fetch_model_servers` interceptor. The (possibly modified) response returned by
        `post_fetch_model_servers` will be passed to
        `post_fetch_model_servers_with_metadata`.
        """
        return response, metadata

    def pre_fetch_model_server_versions(
        self,
        request: gkerecommender.FetchModelServerVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchModelServerVersionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_model_server_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeInferenceQuickstart server.
        """
        return request, metadata

    def post_fetch_model_server_versions(
        self, response: gkerecommender.FetchModelServerVersionsResponse
    ) -> gkerecommender.FetchModelServerVersionsResponse:
        """Post-rpc interceptor for fetch_model_server_versions

        DEPRECATED. Please use the `post_fetch_model_server_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeInferenceQuickstart server but before
        it is returned to user code. This `post_fetch_model_server_versions` interceptor runs
        before the `post_fetch_model_server_versions_with_metadata` interceptor.
        """
        return response

    def post_fetch_model_server_versions_with_metadata(
        self,
        response: gkerecommender.FetchModelServerVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchModelServerVersionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_model_server_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeInferenceQuickstart server but before it is returned to user code.

        We recommend only using this `post_fetch_model_server_versions_with_metadata`
        interceptor in new development instead of the `post_fetch_model_server_versions` interceptor.
        When both interceptors are used, this `post_fetch_model_server_versions_with_metadata` interceptor runs after the
        `post_fetch_model_server_versions` interceptor. The (possibly modified) response returned by
        `post_fetch_model_server_versions` will be passed to
        `post_fetch_model_server_versions_with_metadata`.
        """
        return response, metadata

    def pre_fetch_profiles(
        self,
        request: gkerecommender.FetchProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchProfilesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeInferenceQuickstart server.
        """
        return request, metadata

    def post_fetch_profiles(
        self, response: gkerecommender.FetchProfilesResponse
    ) -> gkerecommender.FetchProfilesResponse:
        """Post-rpc interceptor for fetch_profiles

        DEPRECATED. Please use the `post_fetch_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeInferenceQuickstart server but before
        it is returned to user code. This `post_fetch_profiles` interceptor runs
        before the `post_fetch_profiles_with_metadata` interceptor.
        """
        return response

    def post_fetch_profiles_with_metadata(
        self,
        response: gkerecommender.FetchProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.FetchProfilesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeInferenceQuickstart server but before it is returned to user code.

        We recommend only using this `post_fetch_profiles_with_metadata`
        interceptor in new development instead of the `post_fetch_profiles` interceptor.
        When both interceptors are used, this `post_fetch_profiles_with_metadata` interceptor runs after the
        `post_fetch_profiles` interceptor. The (possibly modified) response returned by
        `post_fetch_profiles` will be passed to
        `post_fetch_profiles_with_metadata`.
        """
        return response, metadata

    def pre_generate_optimized_manifest(
        self,
        request: gkerecommender.GenerateOptimizedManifestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.GenerateOptimizedManifestRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_optimized_manifest

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeInferenceQuickstart server.
        """
        return request, metadata

    def post_generate_optimized_manifest(
        self, response: gkerecommender.GenerateOptimizedManifestResponse
    ) -> gkerecommender.GenerateOptimizedManifestResponse:
        """Post-rpc interceptor for generate_optimized_manifest

        DEPRECATED. Please use the `post_generate_optimized_manifest_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeInferenceQuickstart server but before
        it is returned to user code. This `post_generate_optimized_manifest` interceptor runs
        before the `post_generate_optimized_manifest_with_metadata` interceptor.
        """
        return response

    def post_generate_optimized_manifest_with_metadata(
        self,
        response: gkerecommender.GenerateOptimizedManifestResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkerecommender.GenerateOptimizedManifestResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_optimized_manifest

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeInferenceQuickstart server but before it is returned to user code.

        We recommend only using this `post_generate_optimized_manifest_with_metadata`
        interceptor in new development instead of the `post_generate_optimized_manifest` interceptor.
        When both interceptors are used, this `post_generate_optimized_manifest_with_metadata` interceptor runs after the
        `post_generate_optimized_manifest` interceptor. The (possibly modified) response returned by
        `post_generate_optimized_manifest` will be passed to
        `post_generate_optimized_manifest_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class GkeInferenceQuickstartRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: GkeInferenceQuickstartRestInterceptor


class GkeInferenceQuickstartRestTransport(_BaseGkeInferenceQuickstartRestTransport):
    """REST backend synchronous transport for GkeInferenceQuickstart.

    GKE Inference Quickstart (GIQ) service provides profiles with
    performance metrics for popular models and model servers across
    multiple accelerators. These profiles help generate optimized
    best practices for running inference on GKE.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "gkerecommender.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[GkeInferenceQuickstartRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'gkerecommender.googleapis.com').
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
            interceptor (Optional[GkeInferenceQuickstartRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or GkeInferenceQuickstartRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _FetchBenchmarkingData(
        _BaseGkeInferenceQuickstartRestTransport._BaseFetchBenchmarkingData,
        GkeInferenceQuickstartRestStub,
    ):
        def __hash__(self):
            return hash("GkeInferenceQuickstartRestTransport.FetchBenchmarkingData")

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
            request: gkerecommender.FetchBenchmarkingDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkerecommender.FetchBenchmarkingDataResponse:
            r"""Call the fetch benchmarking data method over HTTP.

            Args:
                request (~.gkerecommender.FetchBenchmarkingDataRequest):
                    The request object. Request message for
                [GkeInferenceQuickstart.FetchBenchmarkingData][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingData].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkerecommender.FetchBenchmarkingDataResponse:
                    Response message for
                [GkeInferenceQuickstart.FetchBenchmarkingData][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingData].

            """

            http_options = _BaseGkeInferenceQuickstartRestTransport._BaseFetchBenchmarkingData._get_http_options()
            request, metadata = self._interceptor.pre_fetch_benchmarking_data(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeInferenceQuickstartRestTransport._BaseFetchBenchmarkingData,
                    "_BaseFetchBenchmarkingData__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.FetchBenchmarkingData",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchBenchmarkingData",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeInferenceQuickstartRestTransport._FetchBenchmarkingData._get_response(
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
            resp = gkerecommender.FetchBenchmarkingDataResponse()
            pb_resp = gkerecommender.FetchBenchmarkingDataResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_benchmarking_data(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_benchmarking_data_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gkerecommender.FetchBenchmarkingDataResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.fetch_benchmarking_data",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchBenchmarkingData",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchModels(
        _BaseGkeInferenceQuickstartRestTransport._BaseFetchModels,
        GkeInferenceQuickstartRestStub,
    ):
        def __hash__(self):
            return hash("GkeInferenceQuickstartRestTransport.FetchModels")

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
            request: gkerecommender.FetchModelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkerecommender.FetchModelsResponse:
            r"""Call the fetch models method over HTTP.

            Args:
                request (~.gkerecommender.FetchModelsRequest):
                    The request object. Request message for
                [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkerecommender.FetchModelsResponse:
                    Response message for
                [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels].

            """

            http_options = _BaseGkeInferenceQuickstartRestTransport._BaseFetchModels._get_http_options()
            request, metadata = self._interceptor.pre_fetch_models(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeInferenceQuickstartRestTransport._BaseFetchModels,
                    "_BaseFetchModels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.FetchModels",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchModels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeInferenceQuickstartRestTransport._FetchModels._get_response(
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
            resp = gkerecommender.FetchModelsResponse()
            pb_resp = gkerecommender.FetchModelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_models(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_models_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkerecommender.FetchModelsResponse.to_json(
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
                    "Received response for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.fetch_models",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchModels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchModelServers(
        _BaseGkeInferenceQuickstartRestTransport._BaseFetchModelServers,
        GkeInferenceQuickstartRestStub,
    ):
        def __hash__(self):
            return hash("GkeInferenceQuickstartRestTransport.FetchModelServers")

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
            request: gkerecommender.FetchModelServersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkerecommender.FetchModelServersResponse:
            r"""Call the fetch model servers method over HTTP.

            Args:
                request (~.gkerecommender.FetchModelServersRequest):
                    The request object. Request message for
                [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkerecommender.FetchModelServersResponse:
                    Response message for
                [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers].

            """

            http_options = _BaseGkeInferenceQuickstartRestTransport._BaseFetchModelServers._get_http_options()
            request, metadata = self._interceptor.pre_fetch_model_servers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeInferenceQuickstartRestTransport._BaseFetchModelServers,
                    "_BaseFetchModelServers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.FetchModelServers",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchModelServers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GkeInferenceQuickstartRestTransport._FetchModelServers._get_response(
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
            resp = gkerecommender.FetchModelServersResponse()
            pb_resp = gkerecommender.FetchModelServersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_model_servers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_model_servers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkerecommender.FetchModelServersResponse.to_json(
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
                    "Received response for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.fetch_model_servers",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchModelServers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchModelServerVersions(
        _BaseGkeInferenceQuickstartRestTransport._BaseFetchModelServerVersions,
        GkeInferenceQuickstartRestStub,
    ):
        def __hash__(self):
            return hash("GkeInferenceQuickstartRestTransport.FetchModelServerVersions")

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
            request: gkerecommender.FetchModelServerVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkerecommender.FetchModelServerVersionsResponse:
            r"""Call the fetch model server
            versions method over HTTP.

                Args:
                    request (~.gkerecommender.FetchModelServerVersionsRequest):
                        The request object. Request message for
                    [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gkerecommender.FetchModelServerVersionsResponse:
                        Response message for
                    [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions].

            """

            http_options = _BaseGkeInferenceQuickstartRestTransport._BaseFetchModelServerVersions._get_http_options()
            request, metadata = self._interceptor.pre_fetch_model_server_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeInferenceQuickstartRestTransport._BaseFetchModelServerVersions,
                    "_BaseFetchModelServerVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.FetchModelServerVersions",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchModelServerVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeInferenceQuickstartRestTransport._FetchModelServerVersions._get_response(
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
            resp = gkerecommender.FetchModelServerVersionsResponse()
            pb_resp = gkerecommender.FetchModelServerVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_model_server_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_model_server_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gkerecommender.FetchModelServerVersionsResponse.to_json(
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
                    "Received response for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.fetch_model_server_versions",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchModelServerVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchProfiles(
        _BaseGkeInferenceQuickstartRestTransport._BaseFetchProfiles,
        GkeInferenceQuickstartRestStub,
    ):
        def __hash__(self):
            return hash("GkeInferenceQuickstartRestTransport.FetchProfiles")

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
            request: gkerecommender.FetchProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkerecommender.FetchProfilesResponse:
            r"""Call the fetch profiles method over HTTP.

            Args:
                request (~.gkerecommender.FetchProfilesRequest):
                    The request object. Request message for
                [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkerecommender.FetchProfilesResponse:
                    Response message for
                [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].

            """

            http_options = _BaseGkeInferenceQuickstartRestTransport._BaseFetchProfiles._get_http_options()
            request, metadata = self._interceptor.pre_fetch_profiles(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeInferenceQuickstartRestTransport._BaseFetchProfiles,
                    "_BaseFetchProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.FetchProfiles",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeInferenceQuickstartRestTransport._FetchProfiles._get_response(
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
            resp = gkerecommender.FetchProfilesResponse()
            pb_resp = gkerecommender.FetchProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkerecommender.FetchProfilesResponse.to_json(
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
                    "Received response for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.fetch_profiles",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "FetchProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateOptimizedManifest(
        _BaseGkeInferenceQuickstartRestTransport._BaseGenerateOptimizedManifest,
        GkeInferenceQuickstartRestStub,
    ):
        def __hash__(self):
            return hash("GkeInferenceQuickstartRestTransport.GenerateOptimizedManifest")

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
            request: gkerecommender.GenerateOptimizedManifestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkerecommender.GenerateOptimizedManifestResponse:
            r"""Call the generate optimized
            manifest method over HTTP.

                Args:
                    request (~.gkerecommender.GenerateOptimizedManifestRequest):
                        The request object. Request message for
                    [GkeInferenceQuickstart.GenerateOptimizedManifest][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifest].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gkerecommender.GenerateOptimizedManifestResponse:
                        Response message for
                    [GkeInferenceQuickstart.GenerateOptimizedManifest][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifest].

            """

            http_options = _BaseGkeInferenceQuickstartRestTransport._BaseGenerateOptimizedManifest._get_http_options()
            request, metadata = self._interceptor.pre_generate_optimized_manifest(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeInferenceQuickstartRestTransport._BaseGenerateOptimizedManifest,
                    "_BaseGenerateOptimizedManifest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.GenerateOptimizedManifest",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "GenerateOptimizedManifest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeInferenceQuickstartRestTransport._GenerateOptimizedManifest._get_response(
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
            resp = gkerecommender.GenerateOptimizedManifestResponse()
            pb_resp = gkerecommender.GenerateOptimizedManifestResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_optimized_manifest(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_optimized_manifest_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gkerecommender.GenerateOptimizedManifestResponse.to_json(
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
                    "Received response for google.cloud.gkerecommender_v1.GkeInferenceQuickstartClient.generate_optimized_manifest",
                    extra={
                        "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                        "rpcName": "GenerateOptimizedManifest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def fetch_benchmarking_data(
        self,
    ) -> Callable[
        [gkerecommender.FetchBenchmarkingDataRequest],
        gkerecommender.FetchBenchmarkingDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchBenchmarkingData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_models(
        self,
    ) -> Callable[
        [gkerecommender.FetchModelsRequest], gkerecommender.FetchModelsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchModels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_model_servers(
        self,
    ) -> Callable[
        [gkerecommender.FetchModelServersRequest],
        gkerecommender.FetchModelServersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchModelServers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_model_server_versions(
        self,
    ) -> Callable[
        [gkerecommender.FetchModelServerVersionsRequest],
        gkerecommender.FetchModelServerVersionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchModelServerVersions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_profiles(
        self,
    ) -> Callable[
        [gkerecommender.FetchProfilesRequest], gkerecommender.FetchProfilesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchProfiles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_optimized_manifest(
        self,
    ) -> Callable[
        [gkerecommender.GenerateOptimizedManifestRequest],
        gkerecommender.GenerateOptimizedManifestResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateOptimizedManifest(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("GkeInferenceQuickstartRestTransport",)
