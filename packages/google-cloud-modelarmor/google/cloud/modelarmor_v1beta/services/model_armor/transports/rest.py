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
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.modelarmor_v1beta._compat import transcode_request
from google.cloud.modelarmor_v1beta.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseModelArmorRestTransport

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


class ModelArmorRestInterceptor:
    """Interceptor for ModelArmor.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ModelArmorRestTransport.

    .. code-block:: python
        class MyCustomModelArmorInterceptor(ModelArmorRestInterceptor):
            def pre_create_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_floor_setting(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_floor_setting(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_sanitize_model_response(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_sanitize_model_response(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_sanitize_user_prompt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_sanitize_user_prompt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_floor_setting(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_floor_setting(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_template(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ModelArmorRestTransport(interceptor=MyCustomModelArmorInterceptor())
        client = ModelArmorClient(transport=transport)


    """

    def pre_create_template(
        self,
        request: service.CreateTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_create_template(self, response: service.Template) -> service.Template:
        """Post-rpc interceptor for create_template

        DEPRECATED. Please use the `post_create_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_create_template` interceptor runs
        before the `post_create_template_with_metadata` interceptor.
        """
        return response

    def post_create_template_with_metadata(
        self,
        response: service.Template,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Template, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_create_template_with_metadata`
        interceptor in new development instead of the `post_create_template` interceptor.
        When both interceptors are used, this `post_create_template_with_metadata` interceptor runs after the
        `post_create_template` interceptor. The (possibly modified) response returned by
        `post_create_template` will be passed to
        `post_create_template_with_metadata`.
        """
        return response, metadata

    def pre_delete_template(
        self,
        request: service.DeleteTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def pre_get_floor_setting(
        self,
        request: service.GetFloorSettingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetFloorSettingRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_floor_setting

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_get_floor_setting(
        self, response: service.FloorSetting
    ) -> service.FloorSetting:
        """Post-rpc interceptor for get_floor_setting

        DEPRECATED. Please use the `post_get_floor_setting_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_get_floor_setting` interceptor runs
        before the `post_get_floor_setting_with_metadata` interceptor.
        """
        return response

    def post_get_floor_setting_with_metadata(
        self,
        response: service.FloorSetting,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.FloorSetting, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_floor_setting

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_get_floor_setting_with_metadata`
        interceptor in new development instead of the `post_get_floor_setting` interceptor.
        When both interceptors are used, this `post_get_floor_setting_with_metadata` interceptor runs after the
        `post_get_floor_setting` interceptor. The (possibly modified) response returned by
        `post_get_floor_setting` will be passed to
        `post_get_floor_setting_with_metadata`.
        """
        return response, metadata

    def pre_get_template(
        self,
        request: service.GetTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_get_template(self, response: service.Template) -> service.Template:
        """Post-rpc interceptor for get_template

        DEPRECATED. Please use the `post_get_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_get_template` interceptor runs
        before the `post_get_template_with_metadata` interceptor.
        """
        return response

    def post_get_template_with_metadata(
        self,
        response: service.Template,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Template, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_get_template_with_metadata`
        interceptor in new development instead of the `post_get_template` interceptor.
        When both interceptors are used, this `post_get_template_with_metadata` interceptor runs after the
        `post_get_template` interceptor. The (possibly modified) response returned by
        `post_get_template` will be passed to
        `post_get_template_with_metadata`.
        """
        return response, metadata

    def pre_list_templates(
        self,
        request: service.ListTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListTemplatesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_list_templates(
        self, response: service.ListTemplatesResponse
    ) -> service.ListTemplatesResponse:
        """Post-rpc interceptor for list_templates

        DEPRECATED. Please use the `post_list_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_list_templates` interceptor runs
        before the `post_list_templates_with_metadata` interceptor.
        """
        return response

    def post_list_templates_with_metadata(
        self,
        response: service.ListTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListTemplatesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_list_templates_with_metadata`
        interceptor in new development instead of the `post_list_templates` interceptor.
        When both interceptors are used, this `post_list_templates_with_metadata` interceptor runs after the
        `post_list_templates` interceptor. The (possibly modified) response returned by
        `post_list_templates` will be passed to
        `post_list_templates_with_metadata`.
        """
        return response, metadata

    def pre_sanitize_model_response(
        self,
        request: service.SanitizeModelResponseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.SanitizeModelResponseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for sanitize_model_response

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_sanitize_model_response(
        self, response: service.SanitizeModelResponseResponse
    ) -> service.SanitizeModelResponseResponse:
        """Post-rpc interceptor for sanitize_model_response

        DEPRECATED. Please use the `post_sanitize_model_response_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_sanitize_model_response` interceptor runs
        before the `post_sanitize_model_response_with_metadata` interceptor.
        """
        return response

    def post_sanitize_model_response_with_metadata(
        self,
        response: service.SanitizeModelResponseResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.SanitizeModelResponseResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for sanitize_model_response

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_sanitize_model_response_with_metadata`
        interceptor in new development instead of the `post_sanitize_model_response` interceptor.
        When both interceptors are used, this `post_sanitize_model_response_with_metadata` interceptor runs after the
        `post_sanitize_model_response` interceptor. The (possibly modified) response returned by
        `post_sanitize_model_response` will be passed to
        `post_sanitize_model_response_with_metadata`.
        """
        return response, metadata

    def pre_sanitize_user_prompt(
        self,
        request: service.SanitizeUserPromptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.SanitizeUserPromptRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for sanitize_user_prompt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_sanitize_user_prompt(
        self, response: service.SanitizeUserPromptResponse
    ) -> service.SanitizeUserPromptResponse:
        """Post-rpc interceptor for sanitize_user_prompt

        DEPRECATED. Please use the `post_sanitize_user_prompt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_sanitize_user_prompt` interceptor runs
        before the `post_sanitize_user_prompt_with_metadata` interceptor.
        """
        return response

    def post_sanitize_user_prompt_with_metadata(
        self,
        response: service.SanitizeUserPromptResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.SanitizeUserPromptResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for sanitize_user_prompt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_sanitize_user_prompt_with_metadata`
        interceptor in new development instead of the `post_sanitize_user_prompt` interceptor.
        When both interceptors are used, this `post_sanitize_user_prompt_with_metadata` interceptor runs after the
        `post_sanitize_user_prompt` interceptor. The (possibly modified) response returned by
        `post_sanitize_user_prompt` will be passed to
        `post_sanitize_user_prompt_with_metadata`.
        """
        return response, metadata

    def pre_update_floor_setting(
        self,
        request: service.UpdateFloorSettingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateFloorSettingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_floor_setting

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_update_floor_setting(
        self, response: service.FloorSetting
    ) -> service.FloorSetting:
        """Post-rpc interceptor for update_floor_setting

        DEPRECATED. Please use the `post_update_floor_setting_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_update_floor_setting` interceptor runs
        before the `post_update_floor_setting_with_metadata` interceptor.
        """
        return response

    def post_update_floor_setting_with_metadata(
        self,
        response: service.FloorSetting,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.FloorSetting, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_floor_setting

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_update_floor_setting_with_metadata`
        interceptor in new development instead of the `post_update_floor_setting` interceptor.
        When both interceptors are used, this `post_update_floor_setting_with_metadata` interceptor runs after the
        `post_update_floor_setting` interceptor. The (possibly modified) response returned by
        `post_update_floor_setting` will be passed to
        `post_update_floor_setting_with_metadata`.
        """
        return response, metadata

    def pre_update_template(
        self,
        request: service.UpdateTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_update_template(self, response: service.Template) -> service.Template:
        """Post-rpc interceptor for update_template

        DEPRECATED. Please use the `post_update_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code. This `post_update_template` interceptor runs
        before the `post_update_template_with_metadata` interceptor.
        """
        return response

    def post_update_template_with_metadata(
        self,
        response: service.Template,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Template, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ModelArmor server but before it is returned to user code.

        We recommend only using this `post_update_template_with_metadata`
        interceptor in new development instead of the `post_update_template` interceptor.
        When both interceptors are used, this `post_update_template_with_metadata` interceptor runs after the
        `post_update_template` interceptor. The (possibly modified) response returned by
        `post_update_template` will be passed to
        `post_update_template_with_metadata`.
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
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ModelArmor server but before
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
        before they are sent to the ModelArmor server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ModelArmor server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ModelArmorRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ModelArmorRestInterceptor


class ModelArmorRestTransport(_BaseModelArmorRestTransport):
    """REST backend synchronous transport for ModelArmor.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "modelarmor.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ModelArmorRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'modelarmor.googleapis.com').
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
            interceptor (Optional[ModelArmorRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ModelArmorRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateTemplate(
        _BaseModelArmorRestTransport._BaseCreateTemplate, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.CreateTemplate")

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
            request: service.CreateTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Template:
            r"""Call the create template method over HTTP.

            Args:
                request (~.service.CreateTemplateRequest):
                    The request object. Message for creating a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Template:
                    Message describing Template resource
            """

            http_options = (
                _BaseModelArmorRestTransport._BaseCreateTemplate._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseCreateTemplate,
                    "_BaseCreateTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.CreateTemplate",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "CreateTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._CreateTemplate._get_response(
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
            resp = service.Template()
            pb_resp = service.Template.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Template.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.create_template",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "CreateTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTemplate(
        _BaseModelArmorRestTransport._BaseDeleteTemplate, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.DeleteTemplate")

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
            request: service.DeleteTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete template method over HTTP.

            Args:
                request (~.service.DeleteTemplateRequest):
                    The request object. Message for deleting a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseModelArmorRestTransport._BaseDeleteTemplate._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseDeleteTemplate,
                    "_BaseDeleteTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.DeleteTemplate",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "DeleteTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._DeleteTemplate._get_response(
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

    class _GetFloorSetting(
        _BaseModelArmorRestTransport._BaseGetFloorSetting, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.GetFloorSetting")

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
            request: service.GetFloorSettingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.FloorSetting:
            r"""Call the get floor setting method over HTTP.

            Args:
                request (~.service.GetFloorSettingRequest):
                    The request object. Message for getting a Floor Setting
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.FloorSetting:
                    Message describing FloorSetting
                resource

            """

            http_options = (
                _BaseModelArmorRestTransport._BaseGetFloorSetting._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_floor_setting(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseGetFloorSetting,
                    "_BaseGetFloorSetting__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.GetFloorSetting",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "GetFloorSetting",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._GetFloorSetting._get_response(
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
            resp = service.FloorSetting()
            pb_resp = service.FloorSetting.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_floor_setting(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_floor_setting_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.FloorSetting.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.get_floor_setting",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "GetFloorSetting",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTemplate(
        _BaseModelArmorRestTransport._BaseGetTemplate, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.GetTemplate")

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
            request: service.GetTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Template:
            r"""Call the get template method over HTTP.

            Args:
                request (~.service.GetTemplateRequest):
                    The request object. Message for getting a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Template:
                    Message describing Template resource
            """

            http_options = (
                _BaseModelArmorRestTransport._BaseGetTemplate._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseGetTemplate,
                    "_BaseGetTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.GetTemplate",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "GetTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._GetTemplate._get_response(
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
            resp = service.Template()
            pb_resp = service.Template.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Template.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.get_template",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "GetTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTemplates(
        _BaseModelArmorRestTransport._BaseListTemplates, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.ListTemplates")

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
            request: service.ListTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListTemplatesResponse:
            r"""Call the list templates method over HTTP.

            Args:
                request (~.service.ListTemplatesRequest):
                    The request object. Message for requesting list of
                Templates
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListTemplatesResponse:
                    Message for response to listing
                Templates

            """

            http_options = (
                _BaseModelArmorRestTransport._BaseListTemplates._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_templates(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseListTemplates,
                    "_BaseListTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.ListTemplates",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "ListTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._ListTemplates._get_response(
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
            resp = service.ListTemplatesResponse()
            pb_resp = service.ListTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListTemplatesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.list_templates",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "ListTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SanitizeModelResponse(
        _BaseModelArmorRestTransport._BaseSanitizeModelResponse, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.SanitizeModelResponse")

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
            request: service.SanitizeModelResponseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.SanitizeModelResponseResponse:
            r"""Call the sanitize model response method over HTTP.

            Args:
                request (~.service.SanitizeModelResponseRequest):
                    The request object. Sanitize Model Response request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.SanitizeModelResponseResponse:
                    Sanitized Model Response Response.
            """

            http_options = _BaseModelArmorRestTransport._BaseSanitizeModelResponse._get_http_options()
            request, metadata = self._interceptor.pre_sanitize_model_response(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseSanitizeModelResponse,
                    "_BaseSanitizeModelResponse__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.SanitizeModelResponse",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "SanitizeModelResponse",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._SanitizeModelResponse._get_response(
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
            resp = service.SanitizeModelResponseResponse()
            pb_resp = service.SanitizeModelResponseResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_sanitize_model_response(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_sanitize_model_response_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.SanitizeModelResponseResponse.to_json(
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
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.sanitize_model_response",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "SanitizeModelResponse",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SanitizeUserPrompt(
        _BaseModelArmorRestTransport._BaseSanitizeUserPrompt, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.SanitizeUserPrompt")

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
            request: service.SanitizeUserPromptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.SanitizeUserPromptResponse:
            r"""Call the sanitize user prompt method over HTTP.

            Args:
                request (~.service.SanitizeUserPromptRequest):
                    The request object. Sanitize User Prompt request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.SanitizeUserPromptResponse:
                    Sanitized User Prompt Response.
            """

            http_options = (
                _BaseModelArmorRestTransport._BaseSanitizeUserPrompt._get_http_options()
            )
            request, metadata = self._interceptor.pre_sanitize_user_prompt(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseSanitizeUserPrompt,
                    "_BaseSanitizeUserPrompt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.SanitizeUserPrompt",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "SanitizeUserPrompt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._SanitizeUserPrompt._get_response(
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
            resp = service.SanitizeUserPromptResponse()
            pb_resp = service.SanitizeUserPromptResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_sanitize_user_prompt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_sanitize_user_prompt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.SanitizeUserPromptResponse.to_json(
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
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.sanitize_user_prompt",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "SanitizeUserPrompt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StreamSanitizeModelResponse(
        _BaseModelArmorRestTransport._BaseStreamSanitizeModelResponse,
        ModelArmorRestStub,
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.StreamSanitizeModelResponse")

        def __call__(
            self,
            request: service.SanitizeModelResponseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method StreamSanitizeModelResponse is not available over REST transport"
            )

    class _StreamSanitizeUserPrompt(
        _BaseModelArmorRestTransport._BaseStreamSanitizeUserPrompt, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.StreamSanitizeUserPrompt")

        def __call__(
            self,
            request: service.SanitizeUserPromptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method StreamSanitizeUserPrompt is not available over REST transport"
            )

    class _UpdateFloorSetting(
        _BaseModelArmorRestTransport._BaseUpdateFloorSetting, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.UpdateFloorSetting")

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
            request: service.UpdateFloorSettingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.FloorSetting:
            r"""Call the update floor setting method over HTTP.

            Args:
                request (~.service.UpdateFloorSettingRequest):
                    The request object. Message for Updating a Floor Setting
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.FloorSetting:
                    Message describing FloorSetting
                resource

            """

            http_options = (
                _BaseModelArmorRestTransport._BaseUpdateFloorSetting._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_floor_setting(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseUpdateFloorSetting,
                    "_BaseUpdateFloorSetting__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.UpdateFloorSetting",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "UpdateFloorSetting",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._UpdateFloorSetting._get_response(
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
            resp = service.FloorSetting()
            pb_resp = service.FloorSetting.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_floor_setting(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_floor_setting_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.FloorSetting.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.update_floor_setting",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "UpdateFloorSetting",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTemplate(
        _BaseModelArmorRestTransport._BaseUpdateTemplate, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.UpdateTemplate")

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
            request: service.UpdateTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Template:
            r"""Call the update template method over HTTP.

            Args:
                request (~.service.UpdateTemplateRequest):
                    The request object. Message for updating a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Template:
                    Message describing Template resource
            """

            http_options = (
                _BaseModelArmorRestTransport._BaseUpdateTemplate._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseUpdateTemplate,
                    "_BaseUpdateTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.UpdateTemplate",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "UpdateTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._UpdateTemplate._get_response(
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
            resp = service.Template()
            pb_resp = service.Template.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Template.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorClient.update_template",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "UpdateTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_template(
        self,
    ) -> Callable[[service.CreateTemplateRequest], service.Template]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_template(
        self,
    ) -> Callable[[service.DeleteTemplateRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_floor_setting(
        self,
    ) -> Callable[[service.GetFloorSettingRequest], service.FloorSetting]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFloorSetting(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_template(self) -> Callable[[service.GetTemplateRequest], service.Template]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_templates(
        self,
    ) -> Callable[[service.ListTemplatesRequest], service.ListTemplatesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTemplates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def sanitize_model_response(
        self,
    ) -> Callable[
        [service.SanitizeModelResponseRequest], service.SanitizeModelResponseResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SanitizeModelResponse(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def sanitize_user_prompt(
        self,
    ) -> Callable[
        [service.SanitizeUserPromptRequest], service.SanitizeUserPromptResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SanitizeUserPrompt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stream_sanitize_model_response(
        self,
    ) -> Callable[
        [service.SanitizeModelResponseRequest], service.SanitizeModelResponseResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamSanitizeModelResponse(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def stream_sanitize_user_prompt(
        self,
    ) -> Callable[
        [service.SanitizeUserPromptRequest], service.SanitizeUserPromptResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamSanitizeUserPrompt(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_floor_setting(
        self,
    ) -> Callable[[service.UpdateFloorSettingRequest], service.FloorSetting]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFloorSetting(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_template(
        self,
    ) -> Callable[[service.UpdateTemplateRequest], service.Template]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseModelArmorRestTransport._BaseGetLocation, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.GetLocation")

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

            http_options = (
                _BaseModelArmorRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
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
        _BaseModelArmorRestTransport._BaseListLocations, ModelArmorRestStub
    ):
        def __hash__(self):
            return hash("ModelArmorRestTransport.ListLocations")

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

            http_options = (
                _BaseModelArmorRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseModelArmorRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.modelarmor_v1beta.ModelArmorClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ModelArmorRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.modelarmor_v1beta.ModelArmorAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.modelarmor.v1beta.ModelArmor",
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


__all__ = ("ModelArmorRestTransport",)
