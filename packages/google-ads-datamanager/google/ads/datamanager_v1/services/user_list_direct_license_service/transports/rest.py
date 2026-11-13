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

from google.ads.datamanager_v1._compat import transcode_request
from google.ads.datamanager_v1.types import (
    user_list_direct_license,
    user_list_direct_license_service,
)
from google.ads.datamanager_v1.types import (
    user_list_direct_license as gad_user_list_direct_license,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseUserListDirectLicenseServiceRestTransport

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


class UserListDirectLicenseServiceRestInterceptor:
    """Interceptor for UserListDirectLicenseService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the UserListDirectLicenseServiceRestTransport.

    .. code-block:: python
        class MyCustomUserListDirectLicenseServiceInterceptor(UserListDirectLicenseServiceRestInterceptor):
            def pre_create_user_list_direct_license(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user_list_direct_license(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_user_list_direct_license(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user_list_direct_license(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_user_list_direct_licenses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_user_list_direct_licenses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user_list_direct_license(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user_list_direct_license(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = UserListDirectLicenseServiceRestTransport(interceptor=MyCustomUserListDirectLicenseServiceInterceptor())
        client = UserListDirectLicenseServiceClient(transport=transport)


    """

    def pre_create_user_list_direct_license(
        self,
        request: user_list_direct_license_service.CreateUserListDirectLicenseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_list_direct_license_service.CreateUserListDirectLicenseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_user_list_direct_license

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserListDirectLicenseService server.
        """
        return request, metadata

    def post_create_user_list_direct_license(
        self, response: gad_user_list_direct_license.UserListDirectLicense
    ) -> gad_user_list_direct_license.UserListDirectLicense:
        """Post-rpc interceptor for create_user_list_direct_license

        DEPRECATED. Please use the `post_create_user_list_direct_license_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserListDirectLicenseService server but before
        it is returned to user code. This `post_create_user_list_direct_license` interceptor runs
        before the `post_create_user_list_direct_license_with_metadata` interceptor.
        """
        return response

    def post_create_user_list_direct_license_with_metadata(
        self,
        response: gad_user_list_direct_license.UserListDirectLicense,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gad_user_list_direct_license.UserListDirectLicense,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_user_list_direct_license

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserListDirectLicenseService server but before it is returned to user code.

        We recommend only using this `post_create_user_list_direct_license_with_metadata`
        interceptor in new development instead of the `post_create_user_list_direct_license` interceptor.
        When both interceptors are used, this `post_create_user_list_direct_license_with_metadata` interceptor runs after the
        `post_create_user_list_direct_license` interceptor. The (possibly modified) response returned by
        `post_create_user_list_direct_license` will be passed to
        `post_create_user_list_direct_license_with_metadata`.
        """
        return response, metadata

    def pre_get_user_list_direct_license(
        self,
        request: user_list_direct_license_service.GetUserListDirectLicenseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_list_direct_license_service.GetUserListDirectLicenseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_user_list_direct_license

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserListDirectLicenseService server.
        """
        return request, metadata

    def post_get_user_list_direct_license(
        self, response: user_list_direct_license.UserListDirectLicense
    ) -> user_list_direct_license.UserListDirectLicense:
        """Post-rpc interceptor for get_user_list_direct_license

        DEPRECATED. Please use the `post_get_user_list_direct_license_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserListDirectLicenseService server but before
        it is returned to user code. This `post_get_user_list_direct_license` interceptor runs
        before the `post_get_user_list_direct_license_with_metadata` interceptor.
        """
        return response

    def post_get_user_list_direct_license_with_metadata(
        self,
        response: user_list_direct_license.UserListDirectLicense,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_list_direct_license.UserListDirectLicense,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_user_list_direct_license

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserListDirectLicenseService server but before it is returned to user code.

        We recommend only using this `post_get_user_list_direct_license_with_metadata`
        interceptor in new development instead of the `post_get_user_list_direct_license` interceptor.
        When both interceptors are used, this `post_get_user_list_direct_license_with_metadata` interceptor runs after the
        `post_get_user_list_direct_license` interceptor. The (possibly modified) response returned by
        `post_get_user_list_direct_license` will be passed to
        `post_get_user_list_direct_license_with_metadata`.
        """
        return response, metadata

    def pre_list_user_list_direct_licenses(
        self,
        request: user_list_direct_license_service.ListUserListDirectLicensesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_list_direct_license_service.ListUserListDirectLicensesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_user_list_direct_licenses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserListDirectLicenseService server.
        """
        return request, metadata

    def post_list_user_list_direct_licenses(
        self,
        response: user_list_direct_license_service.ListUserListDirectLicensesResponse,
    ) -> user_list_direct_license_service.ListUserListDirectLicensesResponse:
        """Post-rpc interceptor for list_user_list_direct_licenses

        DEPRECATED. Please use the `post_list_user_list_direct_licenses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserListDirectLicenseService server but before
        it is returned to user code. This `post_list_user_list_direct_licenses` interceptor runs
        before the `post_list_user_list_direct_licenses_with_metadata` interceptor.
        """
        return response

    def post_list_user_list_direct_licenses_with_metadata(
        self,
        response: user_list_direct_license_service.ListUserListDirectLicensesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_list_direct_license_service.ListUserListDirectLicensesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_user_list_direct_licenses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserListDirectLicenseService server but before it is returned to user code.

        We recommend only using this `post_list_user_list_direct_licenses_with_metadata`
        interceptor in new development instead of the `post_list_user_list_direct_licenses` interceptor.
        When both interceptors are used, this `post_list_user_list_direct_licenses_with_metadata` interceptor runs after the
        `post_list_user_list_direct_licenses` interceptor. The (possibly modified) response returned by
        `post_list_user_list_direct_licenses` will be passed to
        `post_list_user_list_direct_licenses_with_metadata`.
        """
        return response, metadata

    def pre_update_user_list_direct_license(
        self,
        request: user_list_direct_license_service.UpdateUserListDirectLicenseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_list_direct_license_service.UpdateUserListDirectLicenseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_user_list_direct_license

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserListDirectLicenseService server.
        """
        return request, metadata

    def post_update_user_list_direct_license(
        self, response: gad_user_list_direct_license.UserListDirectLicense
    ) -> gad_user_list_direct_license.UserListDirectLicense:
        """Post-rpc interceptor for update_user_list_direct_license

        DEPRECATED. Please use the `post_update_user_list_direct_license_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserListDirectLicenseService server but before
        it is returned to user code. This `post_update_user_list_direct_license` interceptor runs
        before the `post_update_user_list_direct_license_with_metadata` interceptor.
        """
        return response

    def post_update_user_list_direct_license_with_metadata(
        self,
        response: gad_user_list_direct_license.UserListDirectLicense,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gad_user_list_direct_license.UserListDirectLicense,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_user_list_direct_license

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserListDirectLicenseService server but before it is returned to user code.

        We recommend only using this `post_update_user_list_direct_license_with_metadata`
        interceptor in new development instead of the `post_update_user_list_direct_license` interceptor.
        When both interceptors are used, this `post_update_user_list_direct_license_with_metadata` interceptor runs after the
        `post_update_user_list_direct_license` interceptor. The (possibly modified) response returned by
        `post_update_user_list_direct_license` will be passed to
        `post_update_user_list_direct_license_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class UserListDirectLicenseServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: UserListDirectLicenseServiceRestInterceptor


class UserListDirectLicenseServiceRestTransport(
    _BaseUserListDirectLicenseServiceRestTransport
):
    """REST backend synchronous transport for UserListDirectLicenseService.

    Service for managing user list direct licenses. Delete is not
    a supported operation for UserListDirectLicenses.  Callers
    should update the license status to DISABLED to instead to
    deactivate a license.

    This feature is only available to data partners.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "datamanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[UserListDirectLicenseServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'datamanager.googleapis.com').
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
            interceptor (Optional[UserListDirectLicenseServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or UserListDirectLicenseServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateUserListDirectLicense(
        _BaseUserListDirectLicenseServiceRestTransport._BaseCreateUserListDirectLicense,
        UserListDirectLicenseServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "UserListDirectLicenseServiceRestTransport.CreateUserListDirectLicense"
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
            request: user_list_direct_license_service.CreateUserListDirectLicenseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gad_user_list_direct_license.UserListDirectLicense:
            r"""Call the create user list direct
            license method over HTTP.

                Args:
                    request (~.user_list_direct_license_service.CreateUserListDirectLicenseRequest):
                        The request object. Request to create a
                    [UserListDirectLicense][google.ads.datamanager.v1.UserListDirectLicense]
                    resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gad_user_list_direct_license.UserListDirectLicense:
                        A user list direct license.

                    This feature is only available to data
                    partners.

            """

            http_options = _BaseUserListDirectLicenseServiceRestTransport._BaseCreateUserListDirectLicense._get_http_options()
            request, metadata = self._interceptor.pre_create_user_list_direct_license(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserListDirectLicenseServiceRestTransport._BaseCreateUserListDirectLicense,
                    "_BaseCreateUserListDirectLicense__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.CreateUserListDirectLicense",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "CreateUserListDirectLicense",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserListDirectLicenseServiceRestTransport._CreateUserListDirectLicense._get_response(
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
            resp = gad_user_list_direct_license.UserListDirectLicense()
            pb_resp = gad_user_list_direct_license.UserListDirectLicense.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user_list_direct_license(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_user_list_direct_license_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gad_user_list_direct_license.UserListDirectLicense.to_json(
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
                    "Received response for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.create_user_list_direct_license",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "CreateUserListDirectLicense",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUserListDirectLicense(
        _BaseUserListDirectLicenseServiceRestTransport._BaseGetUserListDirectLicense,
        UserListDirectLicenseServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "UserListDirectLicenseServiceRestTransport.GetUserListDirectLicense"
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
            request: user_list_direct_license_service.GetUserListDirectLicenseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_list_direct_license.UserListDirectLicense:
            r"""Call the get user list direct
            license method over HTTP.

                Args:
                    request (~.user_list_direct_license_service.GetUserListDirectLicenseRequest):
                        The request object. Request to get a
                    [UserListDirectLicense][google.ads.datamanager.v1.UserListDirectLicense]
                    resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.user_list_direct_license.UserListDirectLicense:
                        A user list direct license.

                    This feature is only available to data
                    partners.

            """

            http_options = _BaseUserListDirectLicenseServiceRestTransport._BaseGetUserListDirectLicense._get_http_options()
            request, metadata = self._interceptor.pre_get_user_list_direct_license(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserListDirectLicenseServiceRestTransport._BaseGetUserListDirectLicense,
                    "_BaseGetUserListDirectLicense__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.GetUserListDirectLicense",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "GetUserListDirectLicense",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserListDirectLicenseServiceRestTransport._GetUserListDirectLicense._get_response(
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
            resp = user_list_direct_license.UserListDirectLicense()
            pb_resp = user_list_direct_license.UserListDirectLicense.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user_list_direct_license(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_user_list_direct_license_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        user_list_direct_license.UserListDirectLicense.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.get_user_list_direct_license",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "GetUserListDirectLicense",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUserListDirectLicenses(
        _BaseUserListDirectLicenseServiceRestTransport._BaseListUserListDirectLicenses,
        UserListDirectLicenseServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "UserListDirectLicenseServiceRestTransport.ListUserListDirectLicenses"
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
            request: user_list_direct_license_service.ListUserListDirectLicensesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_list_direct_license_service.ListUserListDirectLicensesResponse:
            r"""Call the list user list direct
            licenses method over HTTP.

                Args:
                    request (~.user_list_direct_license_service.ListUserListDirectLicensesRequest):
                        The request object. Request to list all
                    [UserListDirectLicense][google.ads.datamanager.v1.UserListDirectLicense]
                    resources for a given account.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.user_list_direct_license_service.ListUserListDirectLicensesResponse:
                        Response from the
                    [ListUserListDirectLicensesRequest][google.ads.datamanager.v1.ListUserListDirectLicensesRequest].

            """

            http_options = _BaseUserListDirectLicenseServiceRestTransport._BaseListUserListDirectLicenses._get_http_options()
            request, metadata = self._interceptor.pre_list_user_list_direct_licenses(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserListDirectLicenseServiceRestTransport._BaseListUserListDirectLicenses,
                    "_BaseListUserListDirectLicenses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.ListUserListDirectLicenses",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "ListUserListDirectLicenses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserListDirectLicenseServiceRestTransport._ListUserListDirectLicenses._get_response(
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
            resp = user_list_direct_license_service.ListUserListDirectLicensesResponse()
            pb_resp = (
                user_list_direct_license_service.ListUserListDirectLicensesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_user_list_direct_licenses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_user_list_direct_licenses_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = user_list_direct_license_service.ListUserListDirectLicensesResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.list_user_list_direct_licenses",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "ListUserListDirectLicenses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUserListDirectLicense(
        _BaseUserListDirectLicenseServiceRestTransport._BaseUpdateUserListDirectLicense,
        UserListDirectLicenseServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "UserListDirectLicenseServiceRestTransport.UpdateUserListDirectLicense"
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
            request: user_list_direct_license_service.UpdateUserListDirectLicenseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gad_user_list_direct_license.UserListDirectLicense:
            r"""Call the update user list direct
            license method over HTTP.

                Args:
                    request (~.user_list_direct_license_service.UpdateUserListDirectLicenseRequest):
                        The request object. Request to update a
                    [UserListDirectLicense][google.ads.datamanager.v1.UserListDirectLicense]
                    resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gad_user_list_direct_license.UserListDirectLicense:
                        A user list direct license.

                    This feature is only available to data
                    partners.

            """

            http_options = _BaseUserListDirectLicenseServiceRestTransport._BaseUpdateUserListDirectLicense._get_http_options()
            request, metadata = self._interceptor.pre_update_user_list_direct_license(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserListDirectLicenseServiceRestTransport._BaseUpdateUserListDirectLicense,
                    "_BaseUpdateUserListDirectLicense__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.UpdateUserListDirectLicense",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "UpdateUserListDirectLicense",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserListDirectLicenseServiceRestTransport._UpdateUserListDirectLicense._get_response(
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
            resp = gad_user_list_direct_license.UserListDirectLicense()
            pb_resp = gad_user_list_direct_license.UserListDirectLicense.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user_list_direct_license(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_user_list_direct_license_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gad_user_list_direct_license.UserListDirectLicense.to_json(
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
                    "Received response for google.ads.datamanager_v1.UserListDirectLicenseServiceClient.update_user_list_direct_license",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.UserListDirectLicenseService",
                        "rpcName": "UpdateUserListDirectLicense",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_user_list_direct_license(
        self,
    ) -> Callable[
        [user_list_direct_license_service.CreateUserListDirectLicenseRequest],
        gad_user_list_direct_license.UserListDirectLicense,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUserListDirectLicense(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_user_list_direct_license(
        self,
    ) -> Callable[
        [user_list_direct_license_service.GetUserListDirectLicenseRequest],
        user_list_direct_license.UserListDirectLicense,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUserListDirectLicense(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_user_list_direct_licenses(
        self,
    ) -> Callable[
        [user_list_direct_license_service.ListUserListDirectLicensesRequest],
        user_list_direct_license_service.ListUserListDirectLicensesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUserListDirectLicenses(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_user_list_direct_license(
        self,
    ) -> Callable[
        [user_list_direct_license_service.UpdateUserListDirectLicenseRequest],
        gad_user_list_direct_license.UserListDirectLicense,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUserListDirectLicense(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("UserListDirectLicenseServiceRestTransport",)
