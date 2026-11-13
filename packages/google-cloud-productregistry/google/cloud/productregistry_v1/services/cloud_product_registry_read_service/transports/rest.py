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

from google.cloud.productregistry_v1._compat import transcode_request
from google.cloud.productregistry_v1.types import (
    cloud_product_registry_read_service,
    logical_product,
    logical_product_variant,
    product_suite,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCloudProductRegistryReadServiceRestTransport

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


class CloudProductRegistryReadServiceRestInterceptor:
    """Interceptor for CloudProductRegistryReadService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CloudProductRegistryReadServiceRestTransport.

    .. code-block:: python
        class MyCustomCloudProductRegistryReadServiceInterceptor(CloudProductRegistryReadServiceRestInterceptor):
            def pre_get_logical_product(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_logical_product(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_logical_product_variant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_logical_product_variant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_product_suite(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_product_suite(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_logical_products(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_logical_products(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_logical_product_variants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_logical_product_variants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_product_suites(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_product_suites(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_entity(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_entity(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CloudProductRegistryReadServiceRestTransport(interceptor=MyCustomCloudProductRegistryReadServiceInterceptor())
        client = CloudProductRegistryReadServiceClient(transport=transport)


    """

    def pre_get_logical_product(
        self,
        request: cloud_product_registry_read_service.GetLogicalProductRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.GetLogicalProductRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_logical_product

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_get_logical_product(
        self, response: logical_product.LogicalProduct
    ) -> logical_product.LogicalProduct:
        """Post-rpc interceptor for get_logical_product

        DEPRECATED. Please use the `post_get_logical_product_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_get_logical_product` interceptor runs
        before the `post_get_logical_product_with_metadata` interceptor.
        """
        return response

    def post_get_logical_product_with_metadata(
        self,
        response: logical_product.LogicalProduct,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[logical_product.LogicalProduct, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_logical_product

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_get_logical_product_with_metadata`
        interceptor in new development instead of the `post_get_logical_product` interceptor.
        When both interceptors are used, this `post_get_logical_product_with_metadata` interceptor runs after the
        `post_get_logical_product` interceptor. The (possibly modified) response returned by
        `post_get_logical_product` will be passed to
        `post_get_logical_product_with_metadata`.
        """
        return response, metadata

    def pre_get_logical_product_variant(
        self,
        request: cloud_product_registry_read_service.GetLogicalProductVariantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.GetLogicalProductVariantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_logical_product_variant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_get_logical_product_variant(
        self, response: logical_product_variant.LogicalProductVariant
    ) -> logical_product_variant.LogicalProductVariant:
        """Post-rpc interceptor for get_logical_product_variant

        DEPRECATED. Please use the `post_get_logical_product_variant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_get_logical_product_variant` interceptor runs
        before the `post_get_logical_product_variant_with_metadata` interceptor.
        """
        return response

    def post_get_logical_product_variant_with_metadata(
        self,
        response: logical_product_variant.LogicalProductVariant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        logical_product_variant.LogicalProductVariant,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_logical_product_variant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_get_logical_product_variant_with_metadata`
        interceptor in new development instead of the `post_get_logical_product_variant` interceptor.
        When both interceptors are used, this `post_get_logical_product_variant_with_metadata` interceptor runs after the
        `post_get_logical_product_variant` interceptor. The (possibly modified) response returned by
        `post_get_logical_product_variant` will be passed to
        `post_get_logical_product_variant_with_metadata`.
        """
        return response, metadata

    def pre_get_product_suite(
        self,
        request: cloud_product_registry_read_service.GetProductSuiteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.GetProductSuiteRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_product_suite

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_get_product_suite(
        self, response: product_suite.ProductSuite
    ) -> product_suite.ProductSuite:
        """Post-rpc interceptor for get_product_suite

        DEPRECATED. Please use the `post_get_product_suite_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_get_product_suite` interceptor runs
        before the `post_get_product_suite_with_metadata` interceptor.
        """
        return response

    def post_get_product_suite_with_metadata(
        self,
        response: product_suite.ProductSuite,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[product_suite.ProductSuite, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_product_suite

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_get_product_suite_with_metadata`
        interceptor in new development instead of the `post_get_product_suite` interceptor.
        When both interceptors are used, this `post_get_product_suite_with_metadata` interceptor runs after the
        `post_get_product_suite` interceptor. The (possibly modified) response returned by
        `post_get_product_suite` will be passed to
        `post_get_product_suite_with_metadata`.
        """
        return response, metadata

    def pre_list_logical_products(
        self,
        request: cloud_product_registry_read_service.ListLogicalProductsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.ListLogicalProductsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_logical_products

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_list_logical_products(
        self, response: cloud_product_registry_read_service.ListLogicalProductsResponse
    ) -> cloud_product_registry_read_service.ListLogicalProductsResponse:
        """Post-rpc interceptor for list_logical_products

        DEPRECATED. Please use the `post_list_logical_products_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_list_logical_products` interceptor runs
        before the `post_list_logical_products_with_metadata` interceptor.
        """
        return response

    def post_list_logical_products_with_metadata(
        self,
        response: cloud_product_registry_read_service.ListLogicalProductsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.ListLogicalProductsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_logical_products

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_list_logical_products_with_metadata`
        interceptor in new development instead of the `post_list_logical_products` interceptor.
        When both interceptors are used, this `post_list_logical_products_with_metadata` interceptor runs after the
        `post_list_logical_products` interceptor. The (possibly modified) response returned by
        `post_list_logical_products` will be passed to
        `post_list_logical_products_with_metadata`.
        """
        return response, metadata

    def pre_list_logical_product_variants(
        self,
        request: cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_logical_product_variants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_list_logical_product_variants(
        self,
        response: cloud_product_registry_read_service.ListLogicalProductVariantsResponse,
    ) -> cloud_product_registry_read_service.ListLogicalProductVariantsResponse:
        """Post-rpc interceptor for list_logical_product_variants

        DEPRECATED. Please use the `post_list_logical_product_variants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_list_logical_product_variants` interceptor runs
        before the `post_list_logical_product_variants_with_metadata` interceptor.
        """
        return response

    def post_list_logical_product_variants_with_metadata(
        self,
        response: cloud_product_registry_read_service.ListLogicalProductVariantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.ListLogicalProductVariantsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_logical_product_variants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_list_logical_product_variants_with_metadata`
        interceptor in new development instead of the `post_list_logical_product_variants` interceptor.
        When both interceptors are used, this `post_list_logical_product_variants_with_metadata` interceptor runs after the
        `post_list_logical_product_variants` interceptor. The (possibly modified) response returned by
        `post_list_logical_product_variants` will be passed to
        `post_list_logical_product_variants_with_metadata`.
        """
        return response, metadata

    def pre_list_product_suites(
        self,
        request: cloud_product_registry_read_service.ListProductSuitesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.ListProductSuitesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_product_suites

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_list_product_suites(
        self, response: cloud_product_registry_read_service.ListProductSuitesResponse
    ) -> cloud_product_registry_read_service.ListProductSuitesResponse:
        """Post-rpc interceptor for list_product_suites

        DEPRECATED. Please use the `post_list_product_suites_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_list_product_suites` interceptor runs
        before the `post_list_product_suites_with_metadata` interceptor.
        """
        return response

    def post_list_product_suites_with_metadata(
        self,
        response: cloud_product_registry_read_service.ListProductSuitesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.ListProductSuitesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_product_suites

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_list_product_suites_with_metadata`
        interceptor in new development instead of the `post_list_product_suites` interceptor.
        When both interceptors are used, this `post_list_product_suites_with_metadata` interceptor runs after the
        `post_list_product_suites` interceptor. The (possibly modified) response returned by
        `post_list_product_suites` will be passed to
        `post_list_product_suites_with_metadata`.
        """
        return response, metadata

    def pre_lookup_entity(
        self,
        request: cloud_product_registry_read_service.LookupEntityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.LookupEntityRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for lookup_entity

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudProductRegistryReadService server.
        """
        return request, metadata

    def post_lookup_entity(
        self, response: cloud_product_registry_read_service.LookupEntityResponse
    ) -> cloud_product_registry_read_service.LookupEntityResponse:
        """Post-rpc interceptor for lookup_entity

        DEPRECATED. Please use the `post_lookup_entity_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudProductRegistryReadService server but before
        it is returned to user code. This `post_lookup_entity` interceptor runs
        before the `post_lookup_entity_with_metadata` interceptor.
        """
        return response

    def post_lookup_entity_with_metadata(
        self,
        response: cloud_product_registry_read_service.LookupEntityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_product_registry_read_service.LookupEntityResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for lookup_entity

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudProductRegistryReadService server but before it is returned to user code.

        We recommend only using this `post_lookup_entity_with_metadata`
        interceptor in new development instead of the `post_lookup_entity` interceptor.
        When both interceptors are used, this `post_lookup_entity_with_metadata` interceptor runs after the
        `post_lookup_entity` interceptor. The (possibly modified) response returned by
        `post_lookup_entity` will be passed to
        `post_lookup_entity_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class CloudProductRegistryReadServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CloudProductRegistryReadServiceRestInterceptor


class CloudProductRegistryReadServiceRestTransport(
    _BaseCloudProductRegistryReadServiceRestTransport
):
    """REST backend synchronous transport for CloudProductRegistryReadService.

    Cloud Product Registry Read Service provides capabilities to
    access all first and third party Google Cloud products.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudproductregistry.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CloudProductRegistryReadServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudproductregistry.googleapis.com').
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
            interceptor (Optional[CloudProductRegistryReadServiceRestInterceptor]): Interceptor used
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
            interceptor or CloudProductRegistryReadServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _GetLogicalProduct(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseGetLogicalProduct,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CloudProductRegistryReadServiceRestTransport.GetLogicalProduct"
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
            request: cloud_product_registry_read_service.GetLogicalProductRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> logical_product.LogicalProduct:
            r"""Call the get logical product method over HTTP.

            Args:
                request (~.cloud_product_registry_read_service.GetLogicalProductRequest):
                    The request object. Request message for
                GetLogicalProduct.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.logical_product.LogicalProduct:
                    Represents an independent service
                offering that can be provisioned by a
                customer.

            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseGetLogicalProduct._get_http_options()
            request, metadata = self._interceptor.pre_get_logical_product(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseGetLogicalProduct,
                    "_BaseGetLogicalProduct__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.GetLogicalProduct",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "GetLogicalProduct",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._GetLogicalProduct._get_response(
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
            resp = logical_product.LogicalProduct()
            pb_resp = logical_product.LogicalProduct.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_logical_product(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_logical_product_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = logical_product.LogicalProduct.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.get_logical_product",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "GetLogicalProduct",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLogicalProductVariant(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseGetLogicalProductVariant,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CloudProductRegistryReadServiceRestTransport.GetLogicalProductVariant"
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
            request: cloud_product_registry_read_service.GetLogicalProductVariantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> logical_product_variant.LogicalProductVariant:
            r"""Call the get logical product
            variant method over HTTP.

                Args:
                    request (~.cloud_product_registry_read_service.GetLogicalProductVariantRequest):
                        The request object. Request message for
                    GetLogicalProductVariant.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.logical_product_variant.LogicalProductVariant:
                        Represents a distinct offering
                    derived from a primary product that
                    retains core functionalities but offers
                    specialized features for a specific
                    market segment.

            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseGetLogicalProductVariant._get_http_options()
            request, metadata = self._interceptor.pre_get_logical_product_variant(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseGetLogicalProductVariant,
                    "_BaseGetLogicalProductVariant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.GetLogicalProductVariant",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "GetLogicalProductVariant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._GetLogicalProductVariant._get_response(
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
            resp = logical_product_variant.LogicalProductVariant()
            pb_resp = logical_product_variant.LogicalProductVariant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_logical_product_variant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_logical_product_variant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        logical_product_variant.LogicalProductVariant.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.get_logical_product_variant",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "GetLogicalProductVariant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProductSuite(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseGetProductSuite,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash("CloudProductRegistryReadServiceRestTransport.GetProductSuite")

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
            request: cloud_product_registry_read_service.GetProductSuiteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> product_suite.ProductSuite:
            r"""Call the get product suite method over HTTP.

            Args:
                request (~.cloud_product_registry_read_service.GetProductSuiteRequest):
                    The request object. Request message for GetProductSuite.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.product_suite.ProductSuite:
                    Represents a unified grouping of
                products sharing a common brand and
                market positioning.

            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseGetProductSuite._get_http_options()
            request, metadata = self._interceptor.pre_get_product_suite(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseGetProductSuite,
                    "_BaseGetProductSuite__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.GetProductSuite",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "GetProductSuite",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._GetProductSuite._get_response(
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
            resp = product_suite.ProductSuite()
            pb_resp = product_suite.ProductSuite.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_product_suite(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_product_suite_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = product_suite.ProductSuite.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.get_product_suite",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "GetProductSuite",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLogicalProducts(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseListLogicalProducts,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CloudProductRegistryReadServiceRestTransport.ListLogicalProducts"
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
            request: cloud_product_registry_read_service.ListLogicalProductsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_product_registry_read_service.ListLogicalProductsResponse:
            r"""Call the list logical products method over HTTP.

            Args:
                request (~.cloud_product_registry_read_service.ListLogicalProductsRequest):
                    The request object. Request message for
                ListLogicalProducts.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_product_registry_read_service.ListLogicalProductsResponse:
                    Response message for
                ListLogicalProducts.

            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseListLogicalProducts._get_http_options()
            request, metadata = self._interceptor.pre_list_logical_products(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseListLogicalProducts,
                    "_BaseListLogicalProducts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.ListLogicalProducts",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "ListLogicalProducts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._ListLogicalProducts._get_response(
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
            resp = cloud_product_registry_read_service.ListLogicalProductsResponse()
            pb_resp = (
                cloud_product_registry_read_service.ListLogicalProductsResponse.pb(resp)
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_logical_products(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_logical_products_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_product_registry_read_service.ListLogicalProductsResponse.to_json(
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
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.list_logical_products",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "ListLogicalProducts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLogicalProductVariants(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseListLogicalProductVariants,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CloudProductRegistryReadServiceRestTransport.ListLogicalProductVariants"
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
            request: cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_product_registry_read_service.ListLogicalProductVariantsResponse:
            r"""Call the list logical product
            variants method over HTTP.

                Args:
                    request (~.cloud_product_registry_read_service.ListLogicalProductVariantsRequest):
                        The request object. Request message for
                    ListLogicalProductVariants.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_product_registry_read_service.ListLogicalProductVariantsResponse:
                        Response message for
                    ListLogicalProductVariants.

            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseListLogicalProductVariants._get_http_options()
            request, metadata = self._interceptor.pre_list_logical_product_variants(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseListLogicalProductVariants,
                    "_BaseListLogicalProductVariants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.ListLogicalProductVariants",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "ListLogicalProductVariants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._ListLogicalProductVariants._get_response(
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
            resp = (
                cloud_product_registry_read_service.ListLogicalProductVariantsResponse()
            )
            pb_resp = cloud_product_registry_read_service.ListLogicalProductVariantsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_logical_product_variants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_logical_product_variants_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_product_registry_read_service.ListLogicalProductVariantsResponse.to_json(
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
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.list_logical_product_variants",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "ListLogicalProductVariants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProductSuites(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseListProductSuites,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CloudProductRegistryReadServiceRestTransport.ListProductSuites"
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
            request: cloud_product_registry_read_service.ListProductSuitesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_product_registry_read_service.ListProductSuitesResponse:
            r"""Call the list product suites method over HTTP.

            Args:
                request (~.cloud_product_registry_read_service.ListProductSuitesRequest):
                    The request object. Request message for
                ListProductSuites.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_product_registry_read_service.ListProductSuitesResponse:
                    Response message for
                ListProductSuites.

            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseListProductSuites._get_http_options()
            request, metadata = self._interceptor.pre_list_product_suites(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseListProductSuites,
                    "_BaseListProductSuites__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.ListProductSuites",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "ListProductSuites",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._ListProductSuites._get_response(
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
            resp = cloud_product_registry_read_service.ListProductSuitesResponse()
            pb_resp = cloud_product_registry_read_service.ListProductSuitesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_product_suites(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_product_suites_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_product_registry_read_service.ListProductSuitesResponse.to_json(
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
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.list_product_suites",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "ListProductSuites",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupEntity(
        _BaseCloudProductRegistryReadServiceRestTransport._BaseLookupEntity,
        CloudProductRegistryReadServiceRestStub,
    ):
        def __hash__(self):
            return hash("CloudProductRegistryReadServiceRestTransport.LookupEntity")

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
            request: cloud_product_registry_read_service.LookupEntityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_product_registry_read_service.LookupEntityResponse:
            r"""Call the lookup entity method over HTTP.

            Args:
                request (~.cloud_product_registry_read_service.LookupEntityRequest):
                    The request object. Request message for LookupEntity.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_product_registry_read_service.LookupEntityResponse:
                    Response message for LookupEntity.
            """

            http_options = _BaseCloudProductRegistryReadServiceRestTransport._BaseLookupEntity._get_http_options()
            request, metadata = self._interceptor.pre_lookup_entity(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudProductRegistryReadServiceRestTransport._BaseLookupEntity,
                    "_BaseLookupEntity__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.LookupEntity",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "LookupEntity",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudProductRegistryReadServiceRestTransport._LookupEntity._get_response(
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
            resp = cloud_product_registry_read_service.LookupEntityResponse()
            pb_resp = cloud_product_registry_read_service.LookupEntityResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_entity(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_entity_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_product_registry_read_service.LookupEntityResponse.to_json(
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
                    "Received response for google.cloud.productregistry_v1.CloudProductRegistryReadServiceClient.lookup_entity",
                    extra={
                        "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                        "rpcName": "LookupEntity",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_logical_product(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.GetLogicalProductRequest],
        logical_product.LogicalProduct,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLogicalProduct(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_logical_product_variant(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.GetLogicalProductVariantRequest],
        logical_product_variant.LogicalProductVariant,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLogicalProductVariant(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_product_suite(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.GetProductSuiteRequest],
        product_suite.ProductSuite,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProductSuite(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_logical_products(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.ListLogicalProductsRequest],
        cloud_product_registry_read_service.ListLogicalProductsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLogicalProducts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_logical_product_variants(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.ListLogicalProductVariantsRequest],
        cloud_product_registry_read_service.ListLogicalProductVariantsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLogicalProductVariants(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_product_suites(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.ListProductSuitesRequest],
        cloud_product_registry_read_service.ListProductSuitesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProductSuites(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup_entity(
        self,
    ) -> Callable[
        [cloud_product_registry_read_service.LookupEntityRequest],
        cloud_product_registry_read_service.LookupEntityResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupEntity(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("CloudProductRegistryReadServiceRestTransport",)
