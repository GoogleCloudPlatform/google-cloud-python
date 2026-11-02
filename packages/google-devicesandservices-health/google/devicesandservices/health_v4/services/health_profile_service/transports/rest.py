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

from google.devicesandservices.health_v4._compat import transcode_request
from google.devicesandservices.health_v4.types import health_profile

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseHealthProfileServiceRestTransport

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


class HealthProfileServiceRestInterceptor:
    """Interceptor for HealthProfileService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the HealthProfileServiceRestTransport.

    .. code-block:: python
        class MyCustomHealthProfileServiceInterceptor(HealthProfileServiceRestInterceptor):
            def pre_get_identity(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_identity(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_irn_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_irn_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_paired_device(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_paired_device(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_paired_devices(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_paired_devices(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = HealthProfileServiceRestTransport(interceptor=MyCustomHealthProfileServiceInterceptor())
        client = HealthProfileServiceClient(transport=transport)


    """

    def pre_get_identity(
        self,
        request: health_profile.GetIdentityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.GetIdentityRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_identity

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_get_identity(
        self, response: health_profile.Identity
    ) -> health_profile.Identity:
        """Post-rpc interceptor for get_identity

        DEPRECATED. Please use the `post_get_identity_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_get_identity` interceptor runs
        before the `post_get_identity_with_metadata` interceptor.
        """
        return response

    def post_get_identity_with_metadata(
        self,
        response: health_profile.Identity,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.Identity, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_identity

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_get_identity_with_metadata`
        interceptor in new development instead of the `post_get_identity` interceptor.
        When both interceptors are used, this `post_get_identity_with_metadata` interceptor runs after the
        `post_get_identity` interceptor. The (possibly modified) response returned by
        `post_get_identity` will be passed to
        `post_get_identity_with_metadata`.
        """
        return response, metadata

    def pre_get_irn_profile(
        self,
        request: health_profile.GetIrnProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.GetIrnProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_irn_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_get_irn_profile(
        self, response: health_profile.IrnProfile
    ) -> health_profile.IrnProfile:
        """Post-rpc interceptor for get_irn_profile

        DEPRECATED. Please use the `post_get_irn_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_get_irn_profile` interceptor runs
        before the `post_get_irn_profile_with_metadata` interceptor.
        """
        return response

    def post_get_irn_profile_with_metadata(
        self,
        response: health_profile.IrnProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.IrnProfile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_irn_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_get_irn_profile_with_metadata`
        interceptor in new development instead of the `post_get_irn_profile` interceptor.
        When both interceptors are used, this `post_get_irn_profile_with_metadata` interceptor runs after the
        `post_get_irn_profile` interceptor. The (possibly modified) response returned by
        `post_get_irn_profile` will be passed to
        `post_get_irn_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_paired_device(
        self,
        request: health_profile.GetPairedDeviceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.GetPairedDeviceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_paired_device

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_get_paired_device(
        self, response: health_profile.PairedDevice
    ) -> health_profile.PairedDevice:
        """Post-rpc interceptor for get_paired_device

        DEPRECATED. Please use the `post_get_paired_device_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_get_paired_device` interceptor runs
        before the `post_get_paired_device_with_metadata` interceptor.
        """
        return response

    def post_get_paired_device_with_metadata(
        self,
        response: health_profile.PairedDevice,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.PairedDevice, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_paired_device

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_get_paired_device_with_metadata`
        interceptor in new development instead of the `post_get_paired_device` interceptor.
        When both interceptors are used, this `post_get_paired_device_with_metadata` interceptor runs after the
        `post_get_paired_device` interceptor. The (possibly modified) response returned by
        `post_get_paired_device` will be passed to
        `post_get_paired_device_with_metadata`.
        """
        return response, metadata

    def pre_get_profile(
        self,
        request: health_profile.GetProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.GetProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_get_profile(
        self, response: health_profile.Profile
    ) -> health_profile.Profile:
        """Post-rpc interceptor for get_profile

        DEPRECATED. Please use the `post_get_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_get_profile` interceptor runs
        before the `post_get_profile_with_metadata` interceptor.
        """
        return response

    def post_get_profile_with_metadata(
        self,
        response: health_profile.Profile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.Profile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_get_profile_with_metadata`
        interceptor in new development instead of the `post_get_profile` interceptor.
        When both interceptors are used, this `post_get_profile_with_metadata` interceptor runs after the
        `post_get_profile` interceptor. The (possibly modified) response returned by
        `post_get_profile` will be passed to
        `post_get_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_settings(
        self,
        request: health_profile.GetSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.GetSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_get_settings(
        self, response: health_profile.Settings
    ) -> health_profile.Settings:
        """Post-rpc interceptor for get_settings

        DEPRECATED. Please use the `post_get_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_get_settings` interceptor runs
        before the `post_get_settings_with_metadata` interceptor.
        """
        return response

    def post_get_settings_with_metadata(
        self,
        response: health_profile.Settings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.Settings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_get_settings_with_metadata`
        interceptor in new development instead of the `post_get_settings` interceptor.
        When both interceptors are used, this `post_get_settings_with_metadata` interceptor runs after the
        `post_get_settings` interceptor. The (possibly modified) response returned by
        `post_get_settings` will be passed to
        `post_get_settings_with_metadata`.
        """
        return response, metadata

    def pre_list_paired_devices(
        self,
        request: health_profile.ListPairedDevicesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.ListPairedDevicesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_paired_devices

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_list_paired_devices(
        self, response: health_profile.ListPairedDevicesResponse
    ) -> health_profile.ListPairedDevicesResponse:
        """Post-rpc interceptor for list_paired_devices

        DEPRECATED. Please use the `post_list_paired_devices_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_list_paired_devices` interceptor runs
        before the `post_list_paired_devices_with_metadata` interceptor.
        """
        return response

    def post_list_paired_devices_with_metadata(
        self,
        response: health_profile.ListPairedDevicesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.ListPairedDevicesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_paired_devices

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_list_paired_devices_with_metadata`
        interceptor in new development instead of the `post_list_paired_devices` interceptor.
        When both interceptors are used, this `post_list_paired_devices_with_metadata` interceptor runs after the
        `post_list_paired_devices` interceptor. The (possibly modified) response returned by
        `post_list_paired_devices` will be passed to
        `post_list_paired_devices_with_metadata`.
        """
        return response, metadata

    def pre_update_profile(
        self,
        request: health_profile.UpdateProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.UpdateProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_update_profile(
        self, response: health_profile.Profile
    ) -> health_profile.Profile:
        """Post-rpc interceptor for update_profile

        DEPRECATED. Please use the `post_update_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_update_profile` interceptor runs
        before the `post_update_profile_with_metadata` interceptor.
        """
        return response

    def post_update_profile_with_metadata(
        self,
        response: health_profile.Profile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.Profile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_update_profile_with_metadata`
        interceptor in new development instead of the `post_update_profile` interceptor.
        When both interceptors are used, this `post_update_profile_with_metadata` interceptor runs after the
        `post_update_profile` interceptor. The (possibly modified) response returned by
        `post_update_profile` will be passed to
        `post_update_profile_with_metadata`.
        """
        return response, metadata

    def pre_update_settings(
        self,
        request: health_profile.UpdateSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        health_profile.UpdateSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HealthProfileService server.
        """
        return request, metadata

    def post_update_settings(
        self, response: health_profile.Settings
    ) -> health_profile.Settings:
        """Post-rpc interceptor for update_settings

        DEPRECATED. Please use the `post_update_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HealthProfileService server but before
        it is returned to user code. This `post_update_settings` interceptor runs
        before the `post_update_settings_with_metadata` interceptor.
        """
        return response

    def post_update_settings_with_metadata(
        self,
        response: health_profile.Settings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[health_profile.Settings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HealthProfileService server but before it is returned to user code.

        We recommend only using this `post_update_settings_with_metadata`
        interceptor in new development instead of the `post_update_settings` interceptor.
        When both interceptors are used, this `post_update_settings_with_metadata` interceptor runs after the
        `post_update_settings` interceptor. The (possibly modified) response returned by
        `post_update_settings` will be passed to
        `post_update_settings_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class HealthProfileServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: HealthProfileServiceRestInterceptor


class HealthProfileServiceRestTransport(_BaseHealthProfileServiceRestTransport):
    """REST backend synchronous transport for HealthProfileService.

    Health Profile Service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "health.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[HealthProfileServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'health.googleapis.com').
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
            interceptor (Optional[HealthProfileServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or HealthProfileServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetIdentity(
        _BaseHealthProfileServiceRestTransport._BaseGetIdentity,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.GetIdentity")

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
            request: health_profile.GetIdentityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.Identity:
            r"""Call the get identity method over HTTP.

            Args:
                request (~.health_profile.GetIdentityRequest):
                    The request object. Request message for getting Identity
                details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.Identity:
                    Represents details about the Google
                user's identity.

            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseGetIdentity._get_http_options()
            request, metadata = self._interceptor.pre_get_identity(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseGetIdentity,
                    "_BaseGetIdentity__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.GetIdentity",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetIdentity",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._GetIdentity._get_response(
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
            resp = health_profile.Identity()
            pb_resp = health_profile.Identity.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_identity(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_identity_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.Identity.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.get_identity",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetIdentity",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIrnProfile(
        _BaseHealthProfileServiceRestTransport._BaseGetIrnProfile,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.GetIrnProfile")

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
            request: health_profile.GetIrnProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.IrnProfile:
            r"""Call the get irn profile method over HTTP.

            Args:
                request (~.health_profile.GetIrnProfileRequest):
                    The request object. Request message for getting IRN
                Profile details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.IrnProfile:
                    Irregular Rhythm Notifications (IRN)
                Profile details.
                The Irregular Rhythm Notifications (IRN)
                feature checks for signs of atrial
                fibrillation (AFib). The IrnProfile
                details include information about the
                user's onboarding status, enrollment
                status, and the last update time of
                analyzable data for this feature.

            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseGetIrnProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_irn_profile(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseGetIrnProfile,
                    "_BaseGetIrnProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.GetIrnProfile",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetIrnProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._GetIrnProfile._get_response(
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
            resp = health_profile.IrnProfile()
            pb_resp = health_profile.IrnProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_irn_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_irn_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.IrnProfile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.get_irn_profile",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetIrnProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPairedDevice(
        _BaseHealthProfileServiceRestTransport._BaseGetPairedDevice,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.GetPairedDevice")

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
            request: health_profile.GetPairedDeviceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.PairedDevice:
            r"""Call the get paired device method over HTTP.

            Args:
                request (~.health_profile.GetPairedDeviceRequest):
                    The request object. Request message for getting a Device.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.PairedDevice:
                    User's Paired 1P Device

                The PairedDevice details include
                information about the device type,
                battery status, battery level, last sync
                time, device version, mac address, and
                features.

            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseGetPairedDevice._get_http_options()
            request, metadata = self._interceptor.pre_get_paired_device(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseGetPairedDevice,
                    "_BaseGetPairedDevice__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.GetPairedDevice",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetPairedDevice",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._GetPairedDevice._get_response(
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
            resp = health_profile.PairedDevice()
            pb_resp = health_profile.PairedDevice.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_paired_device(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_paired_device_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.PairedDevice.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.get_paired_device",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetPairedDevice",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProfile(
        _BaseHealthProfileServiceRestTransport._BaseGetProfile,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.GetProfile")

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
            request: health_profile.GetProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.Profile:
            r"""Call the get profile method over HTTP.

            Args:
                request (~.health_profile.GetProfileRequest):
                    The request object. Request message for getting Profile
                details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.Profile:
                    Profile details.
            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseGetProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_profile(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseGetProfile,
                    "_BaseGetProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.GetProfile",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._GetProfile._get_response(
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
            resp = health_profile.Profile()
            pb_resp = health_profile.Profile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.Profile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.get_profile",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSettings(
        _BaseHealthProfileServiceRestTransport._BaseGetSettings,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.GetSettings")

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
            request: health_profile.GetSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.Settings:
            r"""Call the get settings method over HTTP.

            Args:
                request (~.health_profile.GetSettingsRequest):
                    The request object. Request message for getting Settings
                details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.Settings:
                    Settings details.
            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseGetSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_settings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseGetSettings,
                    "_BaseGetSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.GetSettings",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._GetSettings._get_response(
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
            resp = health_profile.Settings()
            pb_resp = health_profile.Settings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.Settings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.get_settings",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "GetSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPairedDevices(
        _BaseHealthProfileServiceRestTransport._BaseListPairedDevices,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.ListPairedDevices")

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
            request: health_profile.ListPairedDevicesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.ListPairedDevicesResponse:
            r"""Call the list paired devices method over HTTP.

            Args:
                request (~.health_profile.ListPairedDevicesRequest):
                    The request object. Request message for listing Devices.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.ListPairedDevicesResponse:
                    Response message for
                ListPairedDevices.

            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseListPairedDevices._get_http_options()
            request, metadata = self._interceptor.pre_list_paired_devices(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseListPairedDevices,
                    "_BaseListPairedDevices__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.ListPairedDevices",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "ListPairedDevices",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HealthProfileServiceRestTransport._ListPairedDevices._get_response(
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
            resp = health_profile.ListPairedDevicesResponse()
            pb_resp = health_profile.ListPairedDevicesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_paired_devices(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_paired_devices_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.ListPairedDevicesResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.list_paired_devices",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "ListPairedDevices",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProfile(
        _BaseHealthProfileServiceRestTransport._BaseUpdateProfile,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.UpdateProfile")

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
            request: health_profile.UpdateProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.Profile:
            r"""Call the update profile method over HTTP.

            Args:
                request (~.health_profile.UpdateProfileRequest):
                    The request object. Request message for updating Profile
                details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.Profile:
                    Profile details.
            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseUpdateProfile._get_http_options()
            request, metadata = self._interceptor.pre_update_profile(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseUpdateProfile,
                    "_BaseUpdateProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.UpdateProfile",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "UpdateProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._UpdateProfile._get_response(
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
            resp = health_profile.Profile()
            pb_resp = health_profile.Profile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.Profile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.update_profile",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "UpdateProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSettings(
        _BaseHealthProfileServiceRestTransport._BaseUpdateSettings,
        HealthProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("HealthProfileServiceRestTransport.UpdateSettings")

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
            request: health_profile.UpdateSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> health_profile.Settings:
            r"""Call the update settings method over HTTP.

            Args:
                request (~.health_profile.UpdateSettingsRequest):
                    The request object. Request message for updating Settings
                details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.health_profile.Settings:
                    Settings details.
            """

            http_options = _BaseHealthProfileServiceRestTransport._BaseUpdateSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_settings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHealthProfileServiceRestTransport._BaseUpdateSettings,
                    "_BaseUpdateSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.HealthProfileServiceClient.UpdateSettings",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "UpdateSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HealthProfileServiceRestTransport._UpdateSettings._get_response(
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
            resp = health_profile.Settings()
            pb_resp = health_profile.Settings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = health_profile.Settings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.HealthProfileServiceClient.update_settings",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.HealthProfileService",
                        "rpcName": "UpdateSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_identity(
        self,
    ) -> Callable[[health_profile.GetIdentityRequest], health_profile.Identity]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIdentity(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_irn_profile(
        self,
    ) -> Callable[[health_profile.GetIrnProfileRequest], health_profile.IrnProfile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIrnProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_paired_device(
        self,
    ) -> Callable[[health_profile.GetPairedDeviceRequest], health_profile.PairedDevice]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPairedDevice(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_profile(
        self,
    ) -> Callable[[health_profile.GetProfileRequest], health_profile.Profile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_settings(
        self,
    ) -> Callable[[health_profile.GetSettingsRequest], health_profile.Settings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_paired_devices(
        self,
    ) -> Callable[
        [health_profile.ListPairedDevicesRequest],
        health_profile.ListPairedDevicesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPairedDevices(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_profile(
        self,
    ) -> Callable[[health_profile.UpdateProfileRequest], health_profile.Profile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_settings(
        self,
    ) -> Callable[[health_profile.UpdateSettingsRequest], health_profile.Settings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("HealthProfileServiceRestTransport",)
