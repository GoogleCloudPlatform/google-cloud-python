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
from google.shopping.merchant_accounts_v1.types import programs

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseProgramsServiceRestTransport

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


class ProgramsServiceRestInterceptor:
    """Interceptor for ProgramsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ProgramsServiceRestTransport.

    .. code-block:: python
        class MyCustomProgramsServiceInterceptor(ProgramsServiceRestInterceptor):
            def pre_disable_program(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_program(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_program(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_program(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_program(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_program(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_programs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_programs(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ProgramsServiceRestTransport(interceptor=MyCustomProgramsServiceInterceptor())
        client = ProgramsServiceClient(transport=transport)


    """

    def pre_disable_program(
        self,
        request: programs.DisableProgramRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.DisableProgramRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for disable_program

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProgramsService server.
        """
        return request, metadata

    def post_disable_program(self, response: programs.Program) -> programs.Program:
        """Post-rpc interceptor for disable_program

        DEPRECATED. Please use the `post_disable_program_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProgramsService server but before
        it is returned to user code. This `post_disable_program` interceptor runs
        before the `post_disable_program_with_metadata` interceptor.
        """
        return response

    def post_disable_program_with_metadata(
        self,
        response: programs.Program,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.Program, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_program

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProgramsService server but before it is returned to user code.

        We recommend only using this `post_disable_program_with_metadata`
        interceptor in new development instead of the `post_disable_program` interceptor.
        When both interceptors are used, this `post_disable_program_with_metadata` interceptor runs after the
        `post_disable_program` interceptor. The (possibly modified) response returned by
        `post_disable_program` will be passed to
        `post_disable_program_with_metadata`.
        """
        return response, metadata

    def pre_enable_program(
        self,
        request: programs.EnableProgramRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.EnableProgramRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for enable_program

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProgramsService server.
        """
        return request, metadata

    def post_enable_program(self, response: programs.Program) -> programs.Program:
        """Post-rpc interceptor for enable_program

        DEPRECATED. Please use the `post_enable_program_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProgramsService server but before
        it is returned to user code. This `post_enable_program` interceptor runs
        before the `post_enable_program_with_metadata` interceptor.
        """
        return response

    def post_enable_program_with_metadata(
        self,
        response: programs.Program,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.Program, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_program

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProgramsService server but before it is returned to user code.

        We recommend only using this `post_enable_program_with_metadata`
        interceptor in new development instead of the `post_enable_program` interceptor.
        When both interceptors are used, this `post_enable_program_with_metadata` interceptor runs after the
        `post_enable_program` interceptor. The (possibly modified) response returned by
        `post_enable_program` will be passed to
        `post_enable_program_with_metadata`.
        """
        return response, metadata

    def pre_get_program(
        self,
        request: programs.GetProgramRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.GetProgramRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_program

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProgramsService server.
        """
        return request, metadata

    def post_get_program(self, response: programs.Program) -> programs.Program:
        """Post-rpc interceptor for get_program

        DEPRECATED. Please use the `post_get_program_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProgramsService server but before
        it is returned to user code. This `post_get_program` interceptor runs
        before the `post_get_program_with_metadata` interceptor.
        """
        return response

    def post_get_program_with_metadata(
        self,
        response: programs.Program,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.Program, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_program

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProgramsService server but before it is returned to user code.

        We recommend only using this `post_get_program_with_metadata`
        interceptor in new development instead of the `post_get_program` interceptor.
        When both interceptors are used, this `post_get_program_with_metadata` interceptor runs after the
        `post_get_program` interceptor. The (possibly modified) response returned by
        `post_get_program` will be passed to
        `post_get_program_with_metadata`.
        """
        return response, metadata

    def pre_list_programs(
        self,
        request: programs.ListProgramsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.ListProgramsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_programs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProgramsService server.
        """
        return request, metadata

    def post_list_programs(
        self, response: programs.ListProgramsResponse
    ) -> programs.ListProgramsResponse:
        """Post-rpc interceptor for list_programs

        DEPRECATED. Please use the `post_list_programs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProgramsService server but before
        it is returned to user code. This `post_list_programs` interceptor runs
        before the `post_list_programs_with_metadata` interceptor.
        """
        return response

    def post_list_programs_with_metadata(
        self,
        response: programs.ListProgramsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[programs.ListProgramsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_programs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProgramsService server but before it is returned to user code.

        We recommend only using this `post_list_programs_with_metadata`
        interceptor in new development instead of the `post_list_programs` interceptor.
        When both interceptors are used, this `post_list_programs_with_metadata` interceptor runs after the
        `post_list_programs` interceptor. The (possibly modified) response returned by
        `post_list_programs` will be passed to
        `post_list_programs_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ProgramsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ProgramsServiceRestInterceptor


class ProgramsServiceRestTransport(_BaseProgramsServiceRestTransport):
    """REST backend synchronous transport for ProgramsService.

    Service for program management.

    Programs provide a mechanism for adding functionality to merchant
    accounts. A typical example of this is the `Free product
    listings <https://support.google.com/merchants/answer/13889434>`__
    program, which enables products from a merchant's store to be shown
    across Google for free.

    This service exposes methods to retrieve a business's participation
    in all available programs, in addition to methods for explicitly
    enabling or disabling participation in each program.

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
        interceptor: Optional[ProgramsServiceRestInterceptor] = None,
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
            interceptor (Optional[ProgramsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ProgramsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DisableProgram(
        _BaseProgramsServiceRestTransport._BaseDisableProgram, ProgramsServiceRestStub
    ):
        def __hash__(self):
            return hash("ProgramsServiceRestTransport.DisableProgram")

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
            request: programs.DisableProgramRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> programs.Program:
            r"""Call the disable program method over HTTP.

            Args:
                request (~.programs.DisableProgramRequest):
                    The request object. Request message for the
                DisableProgram method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.programs.Program:
                    Defines participation in a given program for the
                specified account.

                Programs provide a mechanism for adding functionality to
                a Merchant Center accounts. A typical example of this is
                the `Free product
                listings <https://support.google.com/merchants/answer/13889434>`__
                program, which enables products from a business's store
                to be shown across Google for free.

                The following list is the available set of program
                resource IDs accessible through the API:

                - ``checkout``
                - ``free-listings``
                - ``product-ratings``
                - ``shopping-ads``
                - ``youtube-shopping-checkout``

            """

            http_options = _BaseProgramsServiceRestTransport._BaseDisableProgram._get_http_options()
            request, metadata = self._interceptor.pre_disable_program(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProgramsServiceRestTransport._BaseDisableProgram,
                    "_BaseDisableProgram__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.ProgramsServiceClient.DisableProgram",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "DisableProgram",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProgramsServiceRestTransport._DisableProgram._get_response(
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
            resp = programs.Program()
            pb_resp = programs.Program.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_disable_program(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_program_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = programs.Program.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.ProgramsServiceClient.disable_program",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "DisableProgram",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableProgram(
        _BaseProgramsServiceRestTransport._BaseEnableProgram, ProgramsServiceRestStub
    ):
        def __hash__(self):
            return hash("ProgramsServiceRestTransport.EnableProgram")

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
            request: programs.EnableProgramRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> programs.Program:
            r"""Call the enable program method over HTTP.

            Args:
                request (~.programs.EnableProgramRequest):
                    The request object. Request message for the EnableProgram
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.programs.Program:
                    Defines participation in a given program for the
                specified account.

                Programs provide a mechanism for adding functionality to
                a Merchant Center accounts. A typical example of this is
                the `Free product
                listings <https://support.google.com/merchants/answer/13889434>`__
                program, which enables products from a business's store
                to be shown across Google for free.

                The following list is the available set of program
                resource IDs accessible through the API:

                - ``checkout``
                - ``free-listings``
                - ``product-ratings``
                - ``shopping-ads``
                - ``youtube-shopping-checkout``

            """

            http_options = (
                _BaseProgramsServiceRestTransport._BaseEnableProgram._get_http_options()
            )
            request, metadata = self._interceptor.pre_enable_program(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProgramsServiceRestTransport._BaseEnableProgram,
                    "_BaseEnableProgram__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.ProgramsServiceClient.EnableProgram",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "EnableProgram",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProgramsServiceRestTransport._EnableProgram._get_response(
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
            resp = programs.Program()
            pb_resp = programs.Program.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_enable_program(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_program_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = programs.Program.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.ProgramsServiceClient.enable_program",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "EnableProgram",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProgram(
        _BaseProgramsServiceRestTransport._BaseGetProgram, ProgramsServiceRestStub
    ):
        def __hash__(self):
            return hash("ProgramsServiceRestTransport.GetProgram")

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
            request: programs.GetProgramRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> programs.Program:
            r"""Call the get program method over HTTP.

            Args:
                request (~.programs.GetProgramRequest):
                    The request object. Request message for the GetProgram
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.programs.Program:
                    Defines participation in a given program for the
                specified account.

                Programs provide a mechanism for adding functionality to
                a Merchant Center accounts. A typical example of this is
                the `Free product
                listings <https://support.google.com/merchants/answer/13889434>`__
                program, which enables products from a business's store
                to be shown across Google for free.

                The following list is the available set of program
                resource IDs accessible through the API:

                - ``checkout``
                - ``free-listings``
                - ``product-ratings``
                - ``shopping-ads``
                - ``youtube-shopping-checkout``

            """

            http_options = (
                _BaseProgramsServiceRestTransport._BaseGetProgram._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_program(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProgramsServiceRestTransport._BaseGetProgram,
                    "_BaseGetProgram__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.ProgramsServiceClient.GetProgram",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "GetProgram",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProgramsServiceRestTransport._GetProgram._get_response(
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
            resp = programs.Program()
            pb_resp = programs.Program.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_program(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_program_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = programs.Program.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.ProgramsServiceClient.get_program",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "GetProgram",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrograms(
        _BaseProgramsServiceRestTransport._BaseListPrograms, ProgramsServiceRestStub
    ):
        def __hash__(self):
            return hash("ProgramsServiceRestTransport.ListPrograms")

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
            request: programs.ListProgramsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> programs.ListProgramsResponse:
            r"""Call the list programs method over HTTP.

            Args:
                request (~.programs.ListProgramsRequest):
                    The request object. Request message for the ListPrograms
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.programs.ListProgramsResponse:
                    Response message for the ListPrograms
                method.

            """

            http_options = (
                _BaseProgramsServiceRestTransport._BaseListPrograms._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_programs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProgramsServiceRestTransport._BaseListPrograms,
                    "_BaseListPrograms__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.ProgramsServiceClient.ListPrograms",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "ListPrograms",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProgramsServiceRestTransport._ListPrograms._get_response(
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
            resp = programs.ListProgramsResponse()
            pb_resp = programs.ListProgramsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_programs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_programs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = programs.ListProgramsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.ProgramsServiceClient.list_programs",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.ProgramsService",
                        "rpcName": "ListPrograms",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def disable_program(
        self,
    ) -> Callable[[programs.DisableProgramRequest], programs.Program]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableProgram(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_program(
        self,
    ) -> Callable[[programs.EnableProgramRequest], programs.Program]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableProgram(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_program(self) -> Callable[[programs.GetProgramRequest], programs.Program]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProgram(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_programs(
        self,
    ) -> Callable[[programs.ListProgramsRequest], programs.ListProgramsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrograms(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ProgramsServiceRestTransport",)
