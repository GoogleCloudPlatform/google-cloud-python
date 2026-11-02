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

from google.cloud.retail_v2beta._compat import transcode_request
from google.cloud.retail_v2beta.types import (
    generative_question,
    generative_question_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseGenerativeQuestionServiceRestTransport

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


class GenerativeQuestionServiceRestInterceptor:
    """Interceptor for GenerativeQuestionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GenerativeQuestionServiceRestTransport.

    .. code-block:: python
        class MyCustomGenerativeQuestionServiceInterceptor(GenerativeQuestionServiceRestInterceptor):
            def pre_batch_update_generative_question_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_generative_question_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_generative_questions_feature_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_generative_questions_feature_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_generative_question_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_generative_question_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_generative_question_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_generative_question_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_generative_questions_feature_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_generative_questions_feature_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = GenerativeQuestionServiceRestTransport(interceptor=MyCustomGenerativeQuestionServiceInterceptor())
        client = GenerativeQuestionServiceClient(transport=transport)


    """

    def pre_batch_update_generative_question_configs(
        self,
        request: generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_generative_question_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_batch_update_generative_question_configs(
        self,
        response: generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse,
    ) -> generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse:
        """Post-rpc interceptor for batch_update_generative_question_configs

        DEPRECATED. Please use the `post_batch_update_generative_question_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code. This `post_batch_update_generative_question_configs` interceptor runs
        before the `post_batch_update_generative_question_configs_with_metadata` interceptor.
        """
        return response

    def post_batch_update_generative_question_configs_with_metadata(
        self,
        response: generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_generative_question_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GenerativeQuestionService server but before it is returned to user code.

        We recommend only using this `post_batch_update_generative_question_configs_with_metadata`
        interceptor in new development instead of the `post_batch_update_generative_question_configs` interceptor.
        When both interceptors are used, this `post_batch_update_generative_question_configs_with_metadata` interceptor runs after the
        `post_batch_update_generative_question_configs` interceptor. The (possibly modified) response returned by
        `post_batch_update_generative_question_configs` will be passed to
        `post_batch_update_generative_question_configs_with_metadata`.
        """
        return response, metadata

    def pre_get_generative_questions_feature_config(
        self,
        request: generative_question_service.GetGenerativeQuestionsFeatureConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.GetGenerativeQuestionsFeatureConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_generative_questions_feature_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_get_generative_questions_feature_config(
        self, response: generative_question.GenerativeQuestionsFeatureConfig
    ) -> generative_question.GenerativeQuestionsFeatureConfig:
        """Post-rpc interceptor for get_generative_questions_feature_config

        DEPRECATED. Please use the `post_get_generative_questions_feature_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code. This `post_get_generative_questions_feature_config` interceptor runs
        before the `post_get_generative_questions_feature_config_with_metadata` interceptor.
        """
        return response

    def post_get_generative_questions_feature_config_with_metadata(
        self,
        response: generative_question.GenerativeQuestionsFeatureConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question.GenerativeQuestionsFeatureConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_generative_questions_feature_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GenerativeQuestionService server but before it is returned to user code.

        We recommend only using this `post_get_generative_questions_feature_config_with_metadata`
        interceptor in new development instead of the `post_get_generative_questions_feature_config` interceptor.
        When both interceptors are used, this `post_get_generative_questions_feature_config_with_metadata` interceptor runs after the
        `post_get_generative_questions_feature_config` interceptor. The (possibly modified) response returned by
        `post_get_generative_questions_feature_config` will be passed to
        `post_get_generative_questions_feature_config_with_metadata`.
        """
        return response, metadata

    def pre_list_generative_question_configs(
        self,
        request: generative_question_service.ListGenerativeQuestionConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.ListGenerativeQuestionConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_generative_question_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_list_generative_question_configs(
        self,
        response: generative_question_service.ListGenerativeQuestionConfigsResponse,
    ) -> generative_question_service.ListGenerativeQuestionConfigsResponse:
        """Post-rpc interceptor for list_generative_question_configs

        DEPRECATED. Please use the `post_list_generative_question_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code. This `post_list_generative_question_configs` interceptor runs
        before the `post_list_generative_question_configs_with_metadata` interceptor.
        """
        return response

    def post_list_generative_question_configs_with_metadata(
        self,
        response: generative_question_service.ListGenerativeQuestionConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.ListGenerativeQuestionConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_generative_question_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GenerativeQuestionService server but before it is returned to user code.

        We recommend only using this `post_list_generative_question_configs_with_metadata`
        interceptor in new development instead of the `post_list_generative_question_configs` interceptor.
        When both interceptors are used, this `post_list_generative_question_configs_with_metadata` interceptor runs after the
        `post_list_generative_question_configs` interceptor. The (possibly modified) response returned by
        `post_list_generative_question_configs` will be passed to
        `post_list_generative_question_configs_with_metadata`.
        """
        return response, metadata

    def pre_update_generative_question_config(
        self,
        request: generative_question_service.UpdateGenerativeQuestionConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.UpdateGenerativeQuestionConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_generative_question_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_update_generative_question_config(
        self, response: generative_question.GenerativeQuestionConfig
    ) -> generative_question.GenerativeQuestionConfig:
        """Post-rpc interceptor for update_generative_question_config

        DEPRECATED. Please use the `post_update_generative_question_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code. This `post_update_generative_question_config` interceptor runs
        before the `post_update_generative_question_config_with_metadata` interceptor.
        """
        return response

    def post_update_generative_question_config_with_metadata(
        self,
        response: generative_question.GenerativeQuestionConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question.GenerativeQuestionConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_generative_question_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GenerativeQuestionService server but before it is returned to user code.

        We recommend only using this `post_update_generative_question_config_with_metadata`
        interceptor in new development instead of the `post_update_generative_question_config` interceptor.
        When both interceptors are used, this `post_update_generative_question_config_with_metadata` interceptor runs after the
        `post_update_generative_question_config` interceptor. The (possibly modified) response returned by
        `post_update_generative_question_config` will be passed to
        `post_update_generative_question_config_with_metadata`.
        """
        return response, metadata

    def pre_update_generative_questions_feature_config(
        self,
        request: generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_generative_questions_feature_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_update_generative_questions_feature_config(
        self, response: generative_question.GenerativeQuestionsFeatureConfig
    ) -> generative_question.GenerativeQuestionsFeatureConfig:
        """Post-rpc interceptor for update_generative_questions_feature_config

        DEPRECATED. Please use the `post_update_generative_questions_feature_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code. This `post_update_generative_questions_feature_config` interceptor runs
        before the `post_update_generative_questions_feature_config_with_metadata` interceptor.
        """
        return response

    def post_update_generative_questions_feature_config_with_metadata(
        self,
        response: generative_question.GenerativeQuestionsFeatureConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_question.GenerativeQuestionsFeatureConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_generative_questions_feature_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GenerativeQuestionService server but before it is returned to user code.

        We recommend only using this `post_update_generative_questions_feature_config_with_metadata`
        interceptor in new development instead of the `post_update_generative_questions_feature_config` interceptor.
        When both interceptors are used, this `post_update_generative_questions_feature_config_with_metadata` interceptor runs after the
        `post_update_generative_questions_feature_config` interceptor. The (possibly modified) response returned by
        `post_update_generative_questions_feature_config` will be passed to
        `post_update_generative_questions_feature_config_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeQuestionService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeQuestionService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class GenerativeQuestionServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: GenerativeQuestionServiceRestInterceptor


class GenerativeQuestionServiceRestTransport(
    _BaseGenerativeQuestionServiceRestTransport
):
    """REST backend synchronous transport for GenerativeQuestionService.

    Service for managing LLM generated questions in search
    serving.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[GenerativeQuestionServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'retail.googleapis.com').
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
            interceptor (Optional[GenerativeQuestionServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or GenerativeQuestionServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchUpdateGenerativeQuestionConfigs(
        _BaseGenerativeQuestionServiceRestTransport._BaseBatchUpdateGenerativeQuestionConfigs,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "GenerativeQuestionServiceRestTransport.BatchUpdateGenerativeQuestionConfigs"
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
            request: generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse:
            r"""Call the batch update generative
            question configs method over HTTP.

                Args:
                    request (~.generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest):
                        The request object. Request for
                    BatchUpdateGenerativeQuestionConfig
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse:
                        Aggregated response for
                    UpdateGenerativeQuestionConfig method.

            """

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseBatchUpdateGenerativeQuestionConfigs._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_generative_question_configs(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseBatchUpdateGenerativeQuestionConfigs,
                    "_BaseBatchUpdateGenerativeQuestionConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.BatchUpdateGenerativeQuestionConfigs",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "BatchUpdateGenerativeQuestionConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GenerativeQuestionServiceRestTransport._BatchUpdateGenerativeQuestionConfigs._get_response(
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
            resp = generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse()
            pb_resp = generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_generative_question_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_generative_question_configs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse.to_json(
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
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.batch_update_generative_question_configs",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "BatchUpdateGenerativeQuestionConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGenerativeQuestionsFeatureConfig(
        _BaseGenerativeQuestionServiceRestTransport._BaseGetGenerativeQuestionsFeatureConfig,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "GenerativeQuestionServiceRestTransport.GetGenerativeQuestionsFeatureConfig"
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
            request: generative_question_service.GetGenerativeQuestionsFeatureConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> generative_question.GenerativeQuestionsFeatureConfig:
            r"""Call the get generative questions
            feature config method over HTTP.

                Args:
                    request (~.generative_question_service.GetGenerativeQuestionsFeatureConfigRequest):
                        The request object. Request for
                    GetGenerativeQuestionsFeatureConfig
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.generative_question.GenerativeQuestionsFeatureConfig:
                        Configuration for overall generative
                    question feature state.

            """

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseGetGenerativeQuestionsFeatureConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_generative_questions_feature_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseGetGenerativeQuestionsFeatureConfig,
                    "_BaseGetGenerativeQuestionsFeatureConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.GetGenerativeQuestionsFeatureConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "GetGenerativeQuestionsFeatureConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GenerativeQuestionServiceRestTransport._GetGenerativeQuestionsFeatureConfig._get_response(
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
            resp = generative_question.GenerativeQuestionsFeatureConfig()
            pb_resp = generative_question.GenerativeQuestionsFeatureConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_generative_questions_feature_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_generative_questions_feature_config_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        generative_question.GenerativeQuestionsFeatureConfig.to_json(
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
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.get_generative_questions_feature_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "GetGenerativeQuestionsFeatureConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGenerativeQuestionConfigs(
        _BaseGenerativeQuestionServiceRestTransport._BaseListGenerativeQuestionConfigs,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "GenerativeQuestionServiceRestTransport.ListGenerativeQuestionConfigs"
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
            request: generative_question_service.ListGenerativeQuestionConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> generative_question_service.ListGenerativeQuestionConfigsResponse:
            r"""Call the list generative question
            configs method over HTTP.

                Args:
                    request (~.generative_question_service.ListGenerativeQuestionConfigsRequest):
                        The request object. Request for ListQuestions method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.generative_question_service.ListGenerativeQuestionConfigsResponse:
                        Response for ListQuestions method.
            """

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseListGenerativeQuestionConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_generative_question_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseListGenerativeQuestionConfigs,
                    "_BaseListGenerativeQuestionConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.ListGenerativeQuestionConfigs",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "ListGenerativeQuestionConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GenerativeQuestionServiceRestTransport._ListGenerativeQuestionConfigs._get_response(
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
            resp = generative_question_service.ListGenerativeQuestionConfigsResponse()
            pb_resp = (
                generative_question_service.ListGenerativeQuestionConfigsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_generative_question_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_generative_question_configs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = generative_question_service.ListGenerativeQuestionConfigsResponse.to_json(
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
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.list_generative_question_configs",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "ListGenerativeQuestionConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGenerativeQuestionConfig(
        _BaseGenerativeQuestionServiceRestTransport._BaseUpdateGenerativeQuestionConfig,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "GenerativeQuestionServiceRestTransport.UpdateGenerativeQuestionConfig"
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
            request: generative_question_service.UpdateGenerativeQuestionConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> generative_question.GenerativeQuestionConfig:
            r"""Call the update generative
            question config method over HTTP.

                Args:
                    request (~.generative_question_service.UpdateGenerativeQuestionConfigRequest):
                        The request object. Request for
                    UpdateGenerativeQuestionConfig method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.generative_question.GenerativeQuestionConfig:
                        Configuration for a single generated
                    question.

            """

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseUpdateGenerativeQuestionConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_generative_question_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseUpdateGenerativeQuestionConfig,
                    "_BaseUpdateGenerativeQuestionConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.UpdateGenerativeQuestionConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "UpdateGenerativeQuestionConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GenerativeQuestionServiceRestTransport._UpdateGenerativeQuestionConfig._get_response(
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
            resp = generative_question.GenerativeQuestionConfig()
            pb_resp = generative_question.GenerativeQuestionConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_generative_question_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_generative_question_config_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        generative_question.GenerativeQuestionConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.update_generative_question_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "UpdateGenerativeQuestionConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGenerativeQuestionsFeatureConfig(
        _BaseGenerativeQuestionServiceRestTransport._BaseUpdateGenerativeQuestionsFeatureConfig,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "GenerativeQuestionServiceRestTransport.UpdateGenerativeQuestionsFeatureConfig"
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
            request: generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> generative_question.GenerativeQuestionsFeatureConfig:
            r"""Call the update generative
            questions feature config method over HTTP.

                Args:
                    request (~.generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest):
                        The request object. Request for
                    UpdateGenerativeQuestionsFeatureConfig
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.generative_question.GenerativeQuestionsFeatureConfig:
                        Configuration for overall generative
                    question feature state.

            """

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseUpdateGenerativeQuestionsFeatureConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_generative_questions_feature_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseUpdateGenerativeQuestionsFeatureConfig,
                    "_BaseUpdateGenerativeQuestionsFeatureConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.UpdateGenerativeQuestionsFeatureConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "UpdateGenerativeQuestionsFeatureConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GenerativeQuestionServiceRestTransport._UpdateGenerativeQuestionsFeatureConfig._get_response(
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
            resp = generative_question.GenerativeQuestionsFeatureConfig()
            pb_resp = generative_question.GenerativeQuestionsFeatureConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_generative_questions_feature_config(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_generative_questions_feature_config_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        generative_question.GenerativeQuestionsFeatureConfig.to_json(
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
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.update_generative_questions_feature_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "UpdateGenerativeQuestionsFeatureConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_update_generative_question_configs(
        self,
    ) -> Callable[
        [generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest],
        generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateGenerativeQuestionConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_generative_questions_feature_config(
        self,
    ) -> Callable[
        [generative_question_service.GetGenerativeQuestionsFeatureConfigRequest],
        generative_question.GenerativeQuestionsFeatureConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGenerativeQuestionsFeatureConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_generative_question_configs(
        self,
    ) -> Callable[
        [generative_question_service.ListGenerativeQuestionConfigsRequest],
        generative_question_service.ListGenerativeQuestionConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGenerativeQuestionConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_generative_question_config(
        self,
    ) -> Callable[
        [generative_question_service.UpdateGenerativeQuestionConfigRequest],
        generative_question.GenerativeQuestionConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGenerativeQuestionConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_generative_questions_feature_config(
        self,
    ) -> Callable[
        [generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest],
        generative_question.GenerativeQuestionsFeatureConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGenerativeQuestionsFeatureConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseGenerativeQuestionServiceRestTransport._BaseGetOperation,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash("GenerativeQuestionServiceRestTransport.GetOperation")

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

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GenerativeQuestionServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseGenerativeQuestionServiceRestTransport._BaseListOperations,
        GenerativeQuestionServiceRestStub,
    ):
        def __hash__(self):
            return hash("GenerativeQuestionServiceRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseGenerativeQuestionServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGenerativeQuestionServiceRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2beta.GenerativeQuestionServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GenerativeQuestionServiceRestTransport._ListOperations._get_response(
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

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
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
                    "Received response for google.cloud.retail_v2beta.GenerativeQuestionServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2beta.GenerativeQuestionService",
                        "rpcName": "ListOperations",
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


__all__ = ("GenerativeQuestionServiceRestTransport",)
