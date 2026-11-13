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

from google.shopping.merchant_accounts_v1._compat import transcode_request
from google.shopping.merchant_accounts_v1.types import omnichannelsettings

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOmnichannelSettingsServiceRestTransport

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


class OmnichannelSettingsServiceRestInterceptor:
    """Interceptor for OmnichannelSettingsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OmnichannelSettingsServiceRestTransport.

    .. code-block:: python
        class MyCustomOmnichannelSettingsServiceInterceptor(OmnichannelSettingsServiceRestInterceptor):
            def pre_create_omnichannel_setting(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_omnichannel_setting(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_omnichannel_setting(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_omnichannel_setting(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_omnichannel_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_omnichannel_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_request_inventory_verification(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_request_inventory_verification(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_omnichannel_setting(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_omnichannel_setting(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OmnichannelSettingsServiceRestTransport(interceptor=MyCustomOmnichannelSettingsServiceInterceptor())
        client = OmnichannelSettingsServiceClient(transport=transport)


    """

    def pre_create_omnichannel_setting(
        self,
        request: omnichannelsettings.CreateOmnichannelSettingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.CreateOmnichannelSettingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_omnichannel_setting

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OmnichannelSettingsService server.
        """
        return request, metadata

    def post_create_omnichannel_setting(
        self, response: omnichannelsettings.OmnichannelSetting
    ) -> omnichannelsettings.OmnichannelSetting:
        """Post-rpc interceptor for create_omnichannel_setting

        DEPRECATED. Please use the `post_create_omnichannel_setting_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OmnichannelSettingsService server but before
        it is returned to user code. This `post_create_omnichannel_setting` interceptor runs
        before the `post_create_omnichannel_setting_with_metadata` interceptor.
        """
        return response

    def post_create_omnichannel_setting_with_metadata(
        self,
        response: omnichannelsettings.OmnichannelSetting,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.OmnichannelSetting, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_omnichannel_setting

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OmnichannelSettingsService server but before it is returned to user code.

        We recommend only using this `post_create_omnichannel_setting_with_metadata`
        interceptor in new development instead of the `post_create_omnichannel_setting` interceptor.
        When both interceptors are used, this `post_create_omnichannel_setting_with_metadata` interceptor runs after the
        `post_create_omnichannel_setting` interceptor. The (possibly modified) response returned by
        `post_create_omnichannel_setting` will be passed to
        `post_create_omnichannel_setting_with_metadata`.
        """
        return response, metadata

    def pre_get_omnichannel_setting(
        self,
        request: omnichannelsettings.GetOmnichannelSettingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.GetOmnichannelSettingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_omnichannel_setting

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OmnichannelSettingsService server.
        """
        return request, metadata

    def post_get_omnichannel_setting(
        self, response: omnichannelsettings.OmnichannelSetting
    ) -> omnichannelsettings.OmnichannelSetting:
        """Post-rpc interceptor for get_omnichannel_setting

        DEPRECATED. Please use the `post_get_omnichannel_setting_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OmnichannelSettingsService server but before
        it is returned to user code. This `post_get_omnichannel_setting` interceptor runs
        before the `post_get_omnichannel_setting_with_metadata` interceptor.
        """
        return response

    def post_get_omnichannel_setting_with_metadata(
        self,
        response: omnichannelsettings.OmnichannelSetting,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.OmnichannelSetting, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_omnichannel_setting

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OmnichannelSettingsService server but before it is returned to user code.

        We recommend only using this `post_get_omnichannel_setting_with_metadata`
        interceptor in new development instead of the `post_get_omnichannel_setting` interceptor.
        When both interceptors are used, this `post_get_omnichannel_setting_with_metadata` interceptor runs after the
        `post_get_omnichannel_setting` interceptor. The (possibly modified) response returned by
        `post_get_omnichannel_setting` will be passed to
        `post_get_omnichannel_setting_with_metadata`.
        """
        return response, metadata

    def pre_list_omnichannel_settings(
        self,
        request: omnichannelsettings.ListOmnichannelSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.ListOmnichannelSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_omnichannel_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OmnichannelSettingsService server.
        """
        return request, metadata

    def post_list_omnichannel_settings(
        self, response: omnichannelsettings.ListOmnichannelSettingsResponse
    ) -> omnichannelsettings.ListOmnichannelSettingsResponse:
        """Post-rpc interceptor for list_omnichannel_settings

        DEPRECATED. Please use the `post_list_omnichannel_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OmnichannelSettingsService server but before
        it is returned to user code. This `post_list_omnichannel_settings` interceptor runs
        before the `post_list_omnichannel_settings_with_metadata` interceptor.
        """
        return response

    def post_list_omnichannel_settings_with_metadata(
        self,
        response: omnichannelsettings.ListOmnichannelSettingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.ListOmnichannelSettingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_omnichannel_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OmnichannelSettingsService server but before it is returned to user code.

        We recommend only using this `post_list_omnichannel_settings_with_metadata`
        interceptor in new development instead of the `post_list_omnichannel_settings` interceptor.
        When both interceptors are used, this `post_list_omnichannel_settings_with_metadata` interceptor runs after the
        `post_list_omnichannel_settings` interceptor. The (possibly modified) response returned by
        `post_list_omnichannel_settings` will be passed to
        `post_list_omnichannel_settings_with_metadata`.
        """
        return response, metadata

    def pre_request_inventory_verification(
        self,
        request: omnichannelsettings.RequestInventoryVerificationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.RequestInventoryVerificationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for request_inventory_verification

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OmnichannelSettingsService server.
        """
        return request, metadata

    def post_request_inventory_verification(
        self, response: omnichannelsettings.RequestInventoryVerificationResponse
    ) -> omnichannelsettings.RequestInventoryVerificationResponse:
        """Post-rpc interceptor for request_inventory_verification

        DEPRECATED. Please use the `post_request_inventory_verification_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OmnichannelSettingsService server but before
        it is returned to user code. This `post_request_inventory_verification` interceptor runs
        before the `post_request_inventory_verification_with_metadata` interceptor.
        """
        return response

    def post_request_inventory_verification_with_metadata(
        self,
        response: omnichannelsettings.RequestInventoryVerificationResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.RequestInventoryVerificationResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for request_inventory_verification

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OmnichannelSettingsService server but before it is returned to user code.

        We recommend only using this `post_request_inventory_verification_with_metadata`
        interceptor in new development instead of the `post_request_inventory_verification` interceptor.
        When both interceptors are used, this `post_request_inventory_verification_with_metadata` interceptor runs after the
        `post_request_inventory_verification` interceptor. The (possibly modified) response returned by
        `post_request_inventory_verification` will be passed to
        `post_request_inventory_verification_with_metadata`.
        """
        return response, metadata

    def pre_update_omnichannel_setting(
        self,
        request: omnichannelsettings.UpdateOmnichannelSettingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.UpdateOmnichannelSettingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_omnichannel_setting

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OmnichannelSettingsService server.
        """
        return request, metadata

    def post_update_omnichannel_setting(
        self, response: omnichannelsettings.OmnichannelSetting
    ) -> omnichannelsettings.OmnichannelSetting:
        """Post-rpc interceptor for update_omnichannel_setting

        DEPRECATED. Please use the `post_update_omnichannel_setting_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OmnichannelSettingsService server but before
        it is returned to user code. This `post_update_omnichannel_setting` interceptor runs
        before the `post_update_omnichannel_setting_with_metadata` interceptor.
        """
        return response

    def post_update_omnichannel_setting_with_metadata(
        self,
        response: omnichannelsettings.OmnichannelSetting,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        omnichannelsettings.OmnichannelSetting, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_omnichannel_setting

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OmnichannelSettingsService server but before it is returned to user code.

        We recommend only using this `post_update_omnichannel_setting_with_metadata`
        interceptor in new development instead of the `post_update_omnichannel_setting` interceptor.
        When both interceptors are used, this `post_update_omnichannel_setting_with_metadata` interceptor runs after the
        `post_update_omnichannel_setting` interceptor. The (possibly modified) response returned by
        `post_update_omnichannel_setting` will be passed to
        `post_update_omnichannel_setting_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class OmnichannelSettingsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OmnichannelSettingsServiceRestInterceptor


class OmnichannelSettingsServiceRestTransport(
    _BaseOmnichannelSettingsServiceRestTransport
):
    """REST backend synchronous transport for OmnichannelSettingsService.

    The service facilitates the management of a merchant's omnichannel
    settings.

    This API defines the following resource model:
    ----------------------------------------------

    [OmnichannelSetting][google.shopping.merchant.accounts.v1.OmnichannelSetting]

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
        interceptor: Optional[OmnichannelSettingsServiceRestInterceptor] = None,
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
            interceptor (Optional[OmnichannelSettingsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or OmnichannelSettingsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateOmnichannelSetting(
        _BaseOmnichannelSettingsServiceRestTransport._BaseCreateOmnichannelSetting,
        OmnichannelSettingsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OmnichannelSettingsServiceRestTransport.CreateOmnichannelSetting"
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
            request: omnichannelsettings.CreateOmnichannelSettingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> omnichannelsettings.OmnichannelSetting:
            r"""Call the create omnichannel
            setting method over HTTP.

                Args:
                    request (~.omnichannelsettings.CreateOmnichannelSettingRequest):
                        The request object. Request message for the
                    CreateOmnichannelSetting method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.omnichannelsettings.OmnichannelSetting:
                        Collection of information related to
                    the omnichannel settings of a merchant.

            """

            http_options = _BaseOmnichannelSettingsServiceRestTransport._BaseCreateOmnichannelSetting._get_http_options()
            request, metadata = self._interceptor.pre_create_omnichannel_setting(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOmnichannelSettingsServiceRestTransport._BaseCreateOmnichannelSetting,
                    "_BaseCreateOmnichannelSetting__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.CreateOmnichannelSetting",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "CreateOmnichannelSetting",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OmnichannelSettingsServiceRestTransport._CreateOmnichannelSetting._get_response(
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
            resp = omnichannelsettings.OmnichannelSetting()
            pb_resp = omnichannelsettings.OmnichannelSetting.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_omnichannel_setting(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_omnichannel_setting_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = omnichannelsettings.OmnichannelSetting.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.create_omnichannel_setting",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "CreateOmnichannelSetting",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOmnichannelSetting(
        _BaseOmnichannelSettingsServiceRestTransport._BaseGetOmnichannelSetting,
        OmnichannelSettingsServiceRestStub,
    ):
        def __hash__(self):
            return hash("OmnichannelSettingsServiceRestTransport.GetOmnichannelSetting")

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
            request: omnichannelsettings.GetOmnichannelSettingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> omnichannelsettings.OmnichannelSetting:
            r"""Call the get omnichannel setting method over HTTP.

            Args:
                request (~.omnichannelsettings.GetOmnichannelSettingRequest):
                    The request object. Request message for the
                GetOmnichannelSettings method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.omnichannelsettings.OmnichannelSetting:
                    Collection of information related to
                the omnichannel settings of a merchant.

            """

            http_options = _BaseOmnichannelSettingsServiceRestTransport._BaseGetOmnichannelSetting._get_http_options()
            request, metadata = self._interceptor.pre_get_omnichannel_setting(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOmnichannelSettingsServiceRestTransport._BaseGetOmnichannelSetting,
                    "_BaseGetOmnichannelSetting__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.GetOmnichannelSetting",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "GetOmnichannelSetting",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OmnichannelSettingsServiceRestTransport._GetOmnichannelSetting._get_response(
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
            resp = omnichannelsettings.OmnichannelSetting()
            pb_resp = omnichannelsettings.OmnichannelSetting.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_omnichannel_setting(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_omnichannel_setting_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = omnichannelsettings.OmnichannelSetting.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.get_omnichannel_setting",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "GetOmnichannelSetting",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOmnichannelSettings(
        _BaseOmnichannelSettingsServiceRestTransport._BaseListOmnichannelSettings,
        OmnichannelSettingsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OmnichannelSettingsServiceRestTransport.ListOmnichannelSettings"
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
            request: omnichannelsettings.ListOmnichannelSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> omnichannelsettings.ListOmnichannelSettingsResponse:
            r"""Call the list omnichannel settings method over HTTP.

            Args:
                request (~.omnichannelsettings.ListOmnichannelSettingsRequest):
                    The request object. Request message for the
                ListOmnichannelSettings method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.omnichannelsettings.ListOmnichannelSettingsResponse:
                    Response message for the
                ListOmnichannelSettings method.

            """

            http_options = _BaseOmnichannelSettingsServiceRestTransport._BaseListOmnichannelSettings._get_http_options()
            request, metadata = self._interceptor.pre_list_omnichannel_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOmnichannelSettingsServiceRestTransport._BaseListOmnichannelSettings,
                    "_BaseListOmnichannelSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.ListOmnichannelSettings",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "ListOmnichannelSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OmnichannelSettingsServiceRestTransport._ListOmnichannelSettings._get_response(
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
            resp = omnichannelsettings.ListOmnichannelSettingsResponse()
            pb_resp = omnichannelsettings.ListOmnichannelSettingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_omnichannel_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_omnichannel_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        omnichannelsettings.ListOmnichannelSettingsResponse.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.list_omnichannel_settings",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "ListOmnichannelSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RequestInventoryVerification(
        _BaseOmnichannelSettingsServiceRestTransport._BaseRequestInventoryVerification,
        OmnichannelSettingsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OmnichannelSettingsServiceRestTransport.RequestInventoryVerification"
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
            request: omnichannelsettings.RequestInventoryVerificationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> omnichannelsettings.RequestInventoryVerificationResponse:
            r"""Call the request inventory
            verification method over HTTP.

                Args:
                    request (~.omnichannelsettings.RequestInventoryVerificationRequest):
                        The request object. Request message for the
                    RequestInventoryVerification method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.omnichannelsettings.RequestInventoryVerificationResponse:
                        Response message for the
                    RequestInventoryVerification method.

            """

            http_options = _BaseOmnichannelSettingsServiceRestTransport._BaseRequestInventoryVerification._get_http_options()
            request, metadata = self._interceptor.pre_request_inventory_verification(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOmnichannelSettingsServiceRestTransport._BaseRequestInventoryVerification,
                    "_BaseRequestInventoryVerification__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.RequestInventoryVerification",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "RequestInventoryVerification",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OmnichannelSettingsServiceRestTransport._RequestInventoryVerification._get_response(
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
            resp = omnichannelsettings.RequestInventoryVerificationResponse()
            pb_resp = omnichannelsettings.RequestInventoryVerificationResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_request_inventory_verification(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_request_inventory_verification_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = omnichannelsettings.RequestInventoryVerificationResponse.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.request_inventory_verification",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "RequestInventoryVerification",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateOmnichannelSetting(
        _BaseOmnichannelSettingsServiceRestTransport._BaseUpdateOmnichannelSetting,
        OmnichannelSettingsServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OmnichannelSettingsServiceRestTransport.UpdateOmnichannelSetting"
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
            request: omnichannelsettings.UpdateOmnichannelSettingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> omnichannelsettings.OmnichannelSetting:
            r"""Call the update omnichannel
            setting method over HTTP.

                Args:
                    request (~.omnichannelsettings.UpdateOmnichannelSettingRequest):
                        The request object. Request message for the
                    UpdateOmnichannelSetting method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.omnichannelsettings.OmnichannelSetting:
                        Collection of information related to
                    the omnichannel settings of a merchant.

            """

            http_options = _BaseOmnichannelSettingsServiceRestTransport._BaseUpdateOmnichannelSetting._get_http_options()
            request, metadata = self._interceptor.pre_update_omnichannel_setting(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOmnichannelSettingsServiceRestTransport._BaseUpdateOmnichannelSetting,
                    "_BaseUpdateOmnichannelSetting__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.UpdateOmnichannelSetting",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "UpdateOmnichannelSetting",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OmnichannelSettingsServiceRestTransport._UpdateOmnichannelSetting._get_response(
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
            resp = omnichannelsettings.OmnichannelSetting()
            pb_resp = omnichannelsettings.OmnichannelSetting.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_omnichannel_setting(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_omnichannel_setting_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = omnichannelsettings.OmnichannelSetting.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceClient.update_omnichannel_setting",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                        "rpcName": "UpdateOmnichannelSetting",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_omnichannel_setting(
        self,
    ) -> Callable[
        [omnichannelsettings.CreateOmnichannelSettingRequest],
        omnichannelsettings.OmnichannelSetting,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOmnichannelSetting(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_omnichannel_setting(
        self,
    ) -> Callable[
        [omnichannelsettings.GetOmnichannelSettingRequest],
        omnichannelsettings.OmnichannelSetting,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOmnichannelSetting(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_omnichannel_settings(
        self,
    ) -> Callable[
        [omnichannelsettings.ListOmnichannelSettingsRequest],
        omnichannelsettings.ListOmnichannelSettingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOmnichannelSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def request_inventory_verification(
        self,
    ) -> Callable[
        [omnichannelsettings.RequestInventoryVerificationRequest],
        omnichannelsettings.RequestInventoryVerificationResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RequestInventoryVerification(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_omnichannel_setting(
        self,
    ) -> Callable[
        [omnichannelsettings.UpdateOmnichannelSettingRequest],
        omnichannelsettings.OmnichannelSetting,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateOmnichannelSetting(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("OmnichannelSettingsServiceRestTransport",)
