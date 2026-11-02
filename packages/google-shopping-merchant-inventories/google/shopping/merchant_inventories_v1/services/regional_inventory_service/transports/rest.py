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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.shopping.merchant_inventories_v1._compat import transcode_request
from google.shopping.merchant_inventories_v1.types import regionalinventory

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseRegionalInventoryServiceRestTransport

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


class RegionalInventoryServiceRestInterceptor:
    """Interceptor for RegionalInventoryService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RegionalInventoryServiceRestTransport.

    .. code-block:: python
        class MyCustomRegionalInventoryServiceInterceptor(RegionalInventoryServiceRestInterceptor):
            def pre_delete_regional_inventory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_insert_regional_inventory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert_regional_inventory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_regional_inventories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_regional_inventories(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RegionalInventoryServiceRestTransport(interceptor=MyCustomRegionalInventoryServiceInterceptor())
        client = RegionalInventoryServiceClient(transport=transport)


    """

    def pre_delete_regional_inventory(
        self,
        request: regionalinventory.DeleteRegionalInventoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        regionalinventory.DeleteRegionalInventoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_regional_inventory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RegionalInventoryService server.
        """
        return request, metadata

    def pre_insert_regional_inventory(
        self,
        request: regionalinventory.InsertRegionalInventoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        regionalinventory.InsertRegionalInventoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for insert_regional_inventory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RegionalInventoryService server.
        """
        return request, metadata

    def post_insert_regional_inventory(
        self, response: regionalinventory.RegionalInventory
    ) -> regionalinventory.RegionalInventory:
        """Post-rpc interceptor for insert_regional_inventory

        DEPRECATED. Please use the `post_insert_regional_inventory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RegionalInventoryService server but before
        it is returned to user code. This `post_insert_regional_inventory` interceptor runs
        before the `post_insert_regional_inventory_with_metadata` interceptor.
        """
        return response

    def post_insert_regional_inventory_with_metadata(
        self,
        response: regionalinventory.RegionalInventory,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        regionalinventory.RegionalInventory, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for insert_regional_inventory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RegionalInventoryService server but before it is returned to user code.

        We recommend only using this `post_insert_regional_inventory_with_metadata`
        interceptor in new development instead of the `post_insert_regional_inventory` interceptor.
        When both interceptors are used, this `post_insert_regional_inventory_with_metadata` interceptor runs after the
        `post_insert_regional_inventory` interceptor. The (possibly modified) response returned by
        `post_insert_regional_inventory` will be passed to
        `post_insert_regional_inventory_with_metadata`.
        """
        return response, metadata

    def pre_list_regional_inventories(
        self,
        request: regionalinventory.ListRegionalInventoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        regionalinventory.ListRegionalInventoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_regional_inventories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RegionalInventoryService server.
        """
        return request, metadata

    def post_list_regional_inventories(
        self, response: regionalinventory.ListRegionalInventoriesResponse
    ) -> regionalinventory.ListRegionalInventoriesResponse:
        """Post-rpc interceptor for list_regional_inventories

        DEPRECATED. Please use the `post_list_regional_inventories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RegionalInventoryService server but before
        it is returned to user code. This `post_list_regional_inventories` interceptor runs
        before the `post_list_regional_inventories_with_metadata` interceptor.
        """
        return response

    def post_list_regional_inventories_with_metadata(
        self,
        response: regionalinventory.ListRegionalInventoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        regionalinventory.ListRegionalInventoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_regional_inventories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RegionalInventoryService server but before it is returned to user code.

        We recommend only using this `post_list_regional_inventories_with_metadata`
        interceptor in new development instead of the `post_list_regional_inventories` interceptor.
        When both interceptors are used, this `post_list_regional_inventories_with_metadata` interceptor runs after the
        `post_list_regional_inventories` interceptor. The (possibly modified) response returned by
        `post_list_regional_inventories` will be passed to
        `post_list_regional_inventories_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class RegionalInventoryServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: RegionalInventoryServiceRestInterceptor


class RegionalInventoryServiceRestTransport(_BaseRegionalInventoryServiceRestTransport):
    """REST backend synchronous transport for RegionalInventoryService.

    Service to manage regional inventory for products. There is also
    separate ``regions`` resource and API to manage regions definitions.

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
        interceptor: Optional[RegionalInventoryServiceRestInterceptor] = None,
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
            interceptor (Optional[RegionalInventoryServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or RegionalInventoryServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DeleteRegionalInventory(
        _BaseRegionalInventoryServiceRestTransport._BaseDeleteRegionalInventory,
        RegionalInventoryServiceRestStub,
    ):
        def __hash__(self):
            return hash("RegionalInventoryServiceRestTransport.DeleteRegionalInventory")

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
            request: regionalinventory.DeleteRegionalInventoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete regional inventory method over HTTP.

            Args:
                request (~.regionalinventory.DeleteRegionalInventoryRequest):
                    The request object. Request message for the ``DeleteRegionalInventory``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseRegionalInventoryServiceRestTransport._BaseDeleteRegionalInventory._get_http_options()
            request, metadata = self._interceptor.pre_delete_regional_inventory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRegionalInventoryServiceRestTransport._BaseDeleteRegionalInventory,
                    "_BaseDeleteRegionalInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.inventories_v1.RegionalInventoryServiceClient.DeleteRegionalInventory",
                    extra={
                        "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
                        "rpcName": "DeleteRegionalInventory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RegionalInventoryServiceRestTransport._DeleteRegionalInventory._get_response(
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

    class _InsertRegionalInventory(
        _BaseRegionalInventoryServiceRestTransport._BaseInsertRegionalInventory,
        RegionalInventoryServiceRestStub,
    ):
        def __hash__(self):
            return hash("RegionalInventoryServiceRestTransport.InsertRegionalInventory")

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
            request: regionalinventory.InsertRegionalInventoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> regionalinventory.RegionalInventory:
            r"""Call the insert regional inventory method over HTTP.

            Args:
                request (~.regionalinventory.InsertRegionalInventoryRequest):
                    The request object. Request message for the ``InsertRegionalInventory``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.regionalinventory.RegionalInventory:
                    Regional inventory information for the product.
                Represents specific information like price and
                availability for a given product in a specific
                [``region``][google.shopping.merchant.inventories.v1.RegionalInventory.region].
                For a list of all accepted attribute values, see the
                `regional product inventory data
                specification <https://support.google.com/merchants/answer/9698880>`__.

            """

            http_options = _BaseRegionalInventoryServiceRestTransport._BaseInsertRegionalInventory._get_http_options()
            request, metadata = self._interceptor.pre_insert_regional_inventory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRegionalInventoryServiceRestTransport._BaseInsertRegionalInventory,
                    "_BaseInsertRegionalInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.inventories_v1.RegionalInventoryServiceClient.InsertRegionalInventory",
                    extra={
                        "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
                        "rpcName": "InsertRegionalInventory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RegionalInventoryServiceRestTransport._InsertRegionalInventory._get_response(
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
            resp = regionalinventory.RegionalInventory()
            pb_resp = regionalinventory.RegionalInventory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert_regional_inventory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_regional_inventory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = regionalinventory.RegionalInventory.to_json(
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
                    "Received response for google.shopping.merchant.inventories_v1.RegionalInventoryServiceClient.insert_regional_inventory",
                    extra={
                        "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
                        "rpcName": "InsertRegionalInventory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRegionalInventories(
        _BaseRegionalInventoryServiceRestTransport._BaseListRegionalInventories,
        RegionalInventoryServiceRestStub,
    ):
        def __hash__(self):
            return hash("RegionalInventoryServiceRestTransport.ListRegionalInventories")

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
            request: regionalinventory.ListRegionalInventoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> regionalinventory.ListRegionalInventoriesResponse:
            r"""Call the list regional inventories method over HTTP.

            Args:
                request (~.regionalinventory.ListRegionalInventoriesRequest):
                    The request object. Request message for the ``ListRegionalInventories``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.regionalinventory.ListRegionalInventoriesResponse:
                    Response message for the ``ListRegionalInventories``
                method.

            """

            http_options = _BaseRegionalInventoryServiceRestTransport._BaseListRegionalInventories._get_http_options()
            request, metadata = self._interceptor.pre_list_regional_inventories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRegionalInventoryServiceRestTransport._BaseListRegionalInventories,
                    "_BaseListRegionalInventories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.inventories_v1.RegionalInventoryServiceClient.ListRegionalInventories",
                    extra={
                        "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
                        "rpcName": "ListRegionalInventories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RegionalInventoryServiceRestTransport._ListRegionalInventories._get_response(
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
            resp = regionalinventory.ListRegionalInventoriesResponse()
            pb_resp = regionalinventory.ListRegionalInventoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_regional_inventories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_regional_inventories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        regionalinventory.ListRegionalInventoriesResponse.to_json(
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
                    "Received response for google.shopping.merchant.inventories_v1.RegionalInventoryServiceClient.list_regional_inventories",
                    extra={
                        "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
                        "rpcName": "ListRegionalInventories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def delete_regional_inventory(
        self,
    ) -> Callable[[regionalinventory.DeleteRegionalInventoryRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRegionalInventory(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def insert_regional_inventory(
        self,
    ) -> Callable[
        [regionalinventory.InsertRegionalInventoryRequest],
        regionalinventory.RegionalInventory,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InsertRegionalInventory(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_regional_inventories(
        self,
    ) -> Callable[
        [regionalinventory.ListRegionalInventoriesRequest],
        regionalinventory.ListRegionalInventoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRegionalInventories(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("RegionalInventoryServiceRestTransport",)
