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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.commerceproducer_v1beta._compat import transcode_request
from google.cloud.commerceproducer_v1beta.types import (
    commerce_transaction,
    private_offer,
    service,
    sku,
    sku_group,
    standard_offer,
)
from google.cloud.commerceproducer_v1beta.types import (
    private_offer as gcc_private_offer,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCommerceTransactionRestTransport

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


class CommerceTransactionRestInterceptor:
    """Interceptor for CommerceTransaction.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CommerceTransactionRestTransport.

    .. code-block:: python
        class MyCustomCommerceTransactionInterceptor(CommerceTransactionRestInterceptor):
            def pre_cancel_private_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_private_offer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_private_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_private_offer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_private_offer_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_private_offer_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_private_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_private_offer_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_private_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_private_offer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_private_offer_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_private_offer_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_sku(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_sku(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_sku_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_sku_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_standard_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_standard_offer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_offer_documents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_offer_documents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_offers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_offers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_services(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_services(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_sku_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_sku_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_skus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_skus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_standard_offers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_standard_offers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_publish_private_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_publish_private_offer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resolve_amendment_target(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resolve_amendment_target(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_private_offer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_private_offer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_private_offer_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_private_offer_document(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CommerceTransactionRestTransport(interceptor=MyCustomCommerceTransactionInterceptor())
        client = CommerceTransactionClient(transport=transport)


    """

    def pre_cancel_private_offer(
        self,
        request: commerce_transaction.CancelPrivateOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.CancelPrivateOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for cancel_private_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_cancel_private_offer(
        self, response: private_offer.PrivateOffer
    ) -> private_offer.PrivateOffer:
        """Post-rpc interceptor for cancel_private_offer

        DEPRECATED. Please use the `post_cancel_private_offer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_cancel_private_offer` interceptor runs
        before the `post_cancel_private_offer_with_metadata` interceptor.
        """
        return response

    def post_cancel_private_offer_with_metadata(
        self,
        response: private_offer.PrivateOffer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[private_offer.PrivateOffer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_private_offer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_cancel_private_offer_with_metadata`
        interceptor in new development instead of the `post_cancel_private_offer` interceptor.
        When both interceptors are used, this `post_cancel_private_offer_with_metadata` interceptor runs after the
        `post_cancel_private_offer` interceptor. The (possibly modified) response returned by
        `post_cancel_private_offer` will be passed to
        `post_cancel_private_offer_with_metadata`.
        """
        return response, metadata

    def pre_create_private_offer(
        self,
        request: commerce_transaction.CreatePrivateOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.CreatePrivateOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_private_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_create_private_offer(
        self, response: private_offer.PrivateOffer
    ) -> private_offer.PrivateOffer:
        """Post-rpc interceptor for create_private_offer

        DEPRECATED. Please use the `post_create_private_offer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_create_private_offer` interceptor runs
        before the `post_create_private_offer_with_metadata` interceptor.
        """
        return response

    def post_create_private_offer_with_metadata(
        self,
        response: private_offer.PrivateOffer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[private_offer.PrivateOffer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_private_offer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_create_private_offer_with_metadata`
        interceptor in new development instead of the `post_create_private_offer` interceptor.
        When both interceptors are used, this `post_create_private_offer_with_metadata` interceptor runs after the
        `post_create_private_offer` interceptor. The (possibly modified) response returned by
        `post_create_private_offer` will be passed to
        `post_create_private_offer_with_metadata`.
        """
        return response, metadata

    def pre_create_private_offer_document(
        self,
        request: commerce_transaction.CreatePrivateOfferDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.CreatePrivateOfferDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_private_offer_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_create_private_offer_document(
        self, response: private_offer.PrivateOfferDocument
    ) -> private_offer.PrivateOfferDocument:
        """Post-rpc interceptor for create_private_offer_document

        DEPRECATED. Please use the `post_create_private_offer_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_create_private_offer_document` interceptor runs
        before the `post_create_private_offer_document_with_metadata` interceptor.
        """
        return response

    def post_create_private_offer_document_with_metadata(
        self,
        response: private_offer.PrivateOfferDocument,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        private_offer.PrivateOfferDocument, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_private_offer_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_create_private_offer_document_with_metadata`
        interceptor in new development instead of the `post_create_private_offer_document` interceptor.
        When both interceptors are used, this `post_create_private_offer_document_with_metadata` interceptor runs after the
        `post_create_private_offer_document` interceptor. The (possibly modified) response returned by
        `post_create_private_offer_document` will be passed to
        `post_create_private_offer_document_with_metadata`.
        """
        return response, metadata

    def pre_delete_private_offer(
        self,
        request: commerce_transaction.DeletePrivateOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.DeletePrivateOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_private_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def pre_delete_private_offer_document(
        self,
        request: commerce_transaction.DeletePrivateOfferDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.DeletePrivateOfferDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_private_offer_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def pre_get_private_offer(
        self,
        request: commerce_transaction.GetPrivateOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.GetPrivateOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_private_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_private_offer(
        self, response: private_offer.PrivateOffer
    ) -> private_offer.PrivateOffer:
        """Post-rpc interceptor for get_private_offer

        DEPRECATED. Please use the `post_get_private_offer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_get_private_offer` interceptor runs
        before the `post_get_private_offer_with_metadata` interceptor.
        """
        return response

    def post_get_private_offer_with_metadata(
        self,
        response: private_offer.PrivateOffer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[private_offer.PrivateOffer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_private_offer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_get_private_offer_with_metadata`
        interceptor in new development instead of the `post_get_private_offer` interceptor.
        When both interceptors are used, this `post_get_private_offer_with_metadata` interceptor runs after the
        `post_get_private_offer` interceptor. The (possibly modified) response returned by
        `post_get_private_offer` will be passed to
        `post_get_private_offer_with_metadata`.
        """
        return response, metadata

    def pre_get_private_offer_document(
        self,
        request: commerce_transaction.GetPrivateOfferDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.GetPrivateOfferDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_private_offer_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_private_offer_document(
        self, response: private_offer.PrivateOfferDocument
    ) -> private_offer.PrivateOfferDocument:
        """Post-rpc interceptor for get_private_offer_document

        DEPRECATED. Please use the `post_get_private_offer_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_get_private_offer_document` interceptor runs
        before the `post_get_private_offer_document_with_metadata` interceptor.
        """
        return response

    def post_get_private_offer_document_with_metadata(
        self,
        response: private_offer.PrivateOfferDocument,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        private_offer.PrivateOfferDocument, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_private_offer_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_get_private_offer_document_with_metadata`
        interceptor in new development instead of the `post_get_private_offer_document` interceptor.
        When both interceptors are used, this `post_get_private_offer_document_with_metadata` interceptor runs after the
        `post_get_private_offer_document` interceptor. The (possibly modified) response returned by
        `post_get_private_offer_document` will be passed to
        `post_get_private_offer_document_with_metadata`.
        """
        return response, metadata

    def pre_get_service(
        self,
        request: commerce_transaction.GetServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.GetServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_service(self, response: service.Service) -> service.Service:
        """Post-rpc interceptor for get_service

        DEPRECATED. Please use the `post_get_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_get_service` interceptor runs
        before the `post_get_service_with_metadata` interceptor.
        """
        return response

    def post_get_service_with_metadata(
        self,
        response: service.Service,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Service, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_get_service_with_metadata`
        interceptor in new development instead of the `post_get_service` interceptor.
        When both interceptors are used, this `post_get_service_with_metadata` interceptor runs after the
        `post_get_service` interceptor. The (possibly modified) response returned by
        `post_get_service` will be passed to
        `post_get_service_with_metadata`.
        """
        return response, metadata

    def pre_get_sku(
        self,
        request: commerce_transaction.GetSkuRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.GetSkuRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_sku

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_sku(self, response: sku.Sku) -> sku.Sku:
        """Post-rpc interceptor for get_sku

        DEPRECATED. Please use the `post_get_sku_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_get_sku` interceptor runs
        before the `post_get_sku_with_metadata` interceptor.
        """
        return response

    def post_get_sku_with_metadata(
        self, response: sku.Sku, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[sku.Sku, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_sku

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_get_sku_with_metadata`
        interceptor in new development instead of the `post_get_sku` interceptor.
        When both interceptors are used, this `post_get_sku_with_metadata` interceptor runs after the
        `post_get_sku` interceptor. The (possibly modified) response returned by
        `post_get_sku` will be passed to
        `post_get_sku_with_metadata`.
        """
        return response, metadata

    def pre_get_sku_group(
        self,
        request: commerce_transaction.GetSkuGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.GetSkuGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_sku_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_sku_group(self, response: sku_group.SkuGroup) -> sku_group.SkuGroup:
        """Post-rpc interceptor for get_sku_group

        DEPRECATED. Please use the `post_get_sku_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_get_sku_group` interceptor runs
        before the `post_get_sku_group_with_metadata` interceptor.
        """
        return response

    def post_get_sku_group_with_metadata(
        self,
        response: sku_group.SkuGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sku_group.SkuGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_sku_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_get_sku_group_with_metadata`
        interceptor in new development instead of the `post_get_sku_group` interceptor.
        When both interceptors are used, this `post_get_sku_group_with_metadata` interceptor runs after the
        `post_get_sku_group` interceptor. The (possibly modified) response returned by
        `post_get_sku_group` will be passed to
        `post_get_sku_group_with_metadata`.
        """
        return response, metadata

    def pre_get_standard_offer(
        self,
        request: commerce_transaction.GetStandardOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.GetStandardOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_standard_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_standard_offer(
        self, response: standard_offer.StandardOffer
    ) -> standard_offer.StandardOffer:
        """Post-rpc interceptor for get_standard_offer

        DEPRECATED. Please use the `post_get_standard_offer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_get_standard_offer` interceptor runs
        before the `post_get_standard_offer_with_metadata` interceptor.
        """
        return response

    def post_get_standard_offer_with_metadata(
        self,
        response: standard_offer.StandardOffer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[standard_offer.StandardOffer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_standard_offer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_get_standard_offer_with_metadata`
        interceptor in new development instead of the `post_get_standard_offer` interceptor.
        When both interceptors are used, this `post_get_standard_offer_with_metadata` interceptor runs after the
        `post_get_standard_offer` interceptor. The (possibly modified) response returned by
        `post_get_standard_offer` will be passed to
        `post_get_standard_offer_with_metadata`.
        """
        return response, metadata

    def pre_list_private_offer_documents(
        self,
        request: commerce_transaction.ListPrivateOfferDocumentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListPrivateOfferDocumentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_private_offer_documents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_private_offer_documents(
        self, response: commerce_transaction.ListPrivateOfferDocumentsResponse
    ) -> commerce_transaction.ListPrivateOfferDocumentsResponse:
        """Post-rpc interceptor for list_private_offer_documents

        DEPRECATED. Please use the `post_list_private_offer_documents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_list_private_offer_documents` interceptor runs
        before the `post_list_private_offer_documents_with_metadata` interceptor.
        """
        return response

    def post_list_private_offer_documents_with_metadata(
        self,
        response: commerce_transaction.ListPrivateOfferDocumentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListPrivateOfferDocumentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_private_offer_documents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_list_private_offer_documents_with_metadata`
        interceptor in new development instead of the `post_list_private_offer_documents` interceptor.
        When both interceptors are used, this `post_list_private_offer_documents_with_metadata` interceptor runs after the
        `post_list_private_offer_documents` interceptor. The (possibly modified) response returned by
        `post_list_private_offer_documents` will be passed to
        `post_list_private_offer_documents_with_metadata`.
        """
        return response, metadata

    def pre_list_private_offers(
        self,
        request: commerce_transaction.ListPrivateOffersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListPrivateOffersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_private_offers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_private_offers(
        self, response: commerce_transaction.ListPrivateOffersResponse
    ) -> commerce_transaction.ListPrivateOffersResponse:
        """Post-rpc interceptor for list_private_offers

        DEPRECATED. Please use the `post_list_private_offers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_list_private_offers` interceptor runs
        before the `post_list_private_offers_with_metadata` interceptor.
        """
        return response

    def post_list_private_offers_with_metadata(
        self,
        response: commerce_transaction.ListPrivateOffersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListPrivateOffersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_private_offers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_list_private_offers_with_metadata`
        interceptor in new development instead of the `post_list_private_offers` interceptor.
        When both interceptors are used, this `post_list_private_offers_with_metadata` interceptor runs after the
        `post_list_private_offers` interceptor. The (possibly modified) response returned by
        `post_list_private_offers` will be passed to
        `post_list_private_offers_with_metadata`.
        """
        return response, metadata

    def pre_list_services(
        self,
        request: commerce_transaction.ListServicesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListServicesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_services

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_services(
        self, response: commerce_transaction.ListServicesResponse
    ) -> commerce_transaction.ListServicesResponse:
        """Post-rpc interceptor for list_services

        DEPRECATED. Please use the `post_list_services_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_list_services` interceptor runs
        before the `post_list_services_with_metadata` interceptor.
        """
        return response

    def post_list_services_with_metadata(
        self,
        response: commerce_transaction.ListServicesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListServicesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_services

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_list_services_with_metadata`
        interceptor in new development instead of the `post_list_services` interceptor.
        When both interceptors are used, this `post_list_services_with_metadata` interceptor runs after the
        `post_list_services` interceptor. The (possibly modified) response returned by
        `post_list_services` will be passed to
        `post_list_services_with_metadata`.
        """
        return response, metadata

    def pre_list_sku_groups(
        self,
        request: commerce_transaction.ListSkuGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListSkuGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_sku_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_sku_groups(
        self, response: commerce_transaction.ListSkuGroupsResponse
    ) -> commerce_transaction.ListSkuGroupsResponse:
        """Post-rpc interceptor for list_sku_groups

        DEPRECATED. Please use the `post_list_sku_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_list_sku_groups` interceptor runs
        before the `post_list_sku_groups_with_metadata` interceptor.
        """
        return response

    def post_list_sku_groups_with_metadata(
        self,
        response: commerce_transaction.ListSkuGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListSkuGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_sku_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_list_sku_groups_with_metadata`
        interceptor in new development instead of the `post_list_sku_groups` interceptor.
        When both interceptors are used, this `post_list_sku_groups_with_metadata` interceptor runs after the
        `post_list_sku_groups` interceptor. The (possibly modified) response returned by
        `post_list_sku_groups` will be passed to
        `post_list_sku_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_skus(
        self,
        request: commerce_transaction.ListSkusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListSkusRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_skus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_skus(
        self, response: commerce_transaction.ListSkusResponse
    ) -> commerce_transaction.ListSkusResponse:
        """Post-rpc interceptor for list_skus

        DEPRECATED. Please use the `post_list_skus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_list_skus` interceptor runs
        before the `post_list_skus_with_metadata` interceptor.
        """
        return response

    def post_list_skus_with_metadata(
        self,
        response: commerce_transaction.ListSkusResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListSkusResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_skus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_list_skus_with_metadata`
        interceptor in new development instead of the `post_list_skus` interceptor.
        When both interceptors are used, this `post_list_skus_with_metadata` interceptor runs after the
        `post_list_skus` interceptor. The (possibly modified) response returned by
        `post_list_skus` will be passed to
        `post_list_skus_with_metadata`.
        """
        return response, metadata

    def pre_list_standard_offers(
        self,
        request: commerce_transaction.ListStandardOffersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListStandardOffersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_standard_offers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_standard_offers(
        self, response: commerce_transaction.ListStandardOffersResponse
    ) -> commerce_transaction.ListStandardOffersResponse:
        """Post-rpc interceptor for list_standard_offers

        DEPRECATED. Please use the `post_list_standard_offers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_list_standard_offers` interceptor runs
        before the `post_list_standard_offers_with_metadata` interceptor.
        """
        return response

    def post_list_standard_offers_with_metadata(
        self,
        response: commerce_transaction.ListStandardOffersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ListStandardOffersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_standard_offers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_list_standard_offers_with_metadata`
        interceptor in new development instead of the `post_list_standard_offers` interceptor.
        When both interceptors are used, this `post_list_standard_offers_with_metadata` interceptor runs after the
        `post_list_standard_offers` interceptor. The (possibly modified) response returned by
        `post_list_standard_offers` will be passed to
        `post_list_standard_offers_with_metadata`.
        """
        return response, metadata

    def pre_publish_private_offer(
        self,
        request: commerce_transaction.PublishPrivateOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.PublishPrivateOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for publish_private_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_publish_private_offer(
        self, response: private_offer.PrivateOffer
    ) -> private_offer.PrivateOffer:
        """Post-rpc interceptor for publish_private_offer

        DEPRECATED. Please use the `post_publish_private_offer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_publish_private_offer` interceptor runs
        before the `post_publish_private_offer_with_metadata` interceptor.
        """
        return response

    def post_publish_private_offer_with_metadata(
        self,
        response: private_offer.PrivateOffer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[private_offer.PrivateOffer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for publish_private_offer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_publish_private_offer_with_metadata`
        interceptor in new development instead of the `post_publish_private_offer` interceptor.
        When both interceptors are used, this `post_publish_private_offer_with_metadata` interceptor runs after the
        `post_publish_private_offer` interceptor. The (possibly modified) response returned by
        `post_publish_private_offer` will be passed to
        `post_publish_private_offer_with_metadata`.
        """
        return response, metadata

    def pre_resolve_amendment_target(
        self,
        request: commerce_transaction.ResolveAmendmentTargetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ResolveAmendmentTargetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for resolve_amendment_target

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_resolve_amendment_target(
        self, response: commerce_transaction.ResolveAmendmentTargetResponse
    ) -> commerce_transaction.ResolveAmendmentTargetResponse:
        """Post-rpc interceptor for resolve_amendment_target

        DEPRECATED. Please use the `post_resolve_amendment_target_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_resolve_amendment_target` interceptor runs
        before the `post_resolve_amendment_target_with_metadata` interceptor.
        """
        return response

    def post_resolve_amendment_target_with_metadata(
        self,
        response: commerce_transaction.ResolveAmendmentTargetResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.ResolveAmendmentTargetResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for resolve_amendment_target

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_resolve_amendment_target_with_metadata`
        interceptor in new development instead of the `post_resolve_amendment_target` interceptor.
        When both interceptors are used, this `post_resolve_amendment_target_with_metadata` interceptor runs after the
        `post_resolve_amendment_target` interceptor. The (possibly modified) response returned by
        `post_resolve_amendment_target` will be passed to
        `post_resolve_amendment_target_with_metadata`.
        """
        return response, metadata

    def pre_update_private_offer(
        self,
        request: commerce_transaction.UpdatePrivateOfferRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.UpdatePrivateOfferRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_private_offer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_update_private_offer(
        self, response: gcc_private_offer.PrivateOffer
    ) -> gcc_private_offer.PrivateOffer:
        """Post-rpc interceptor for update_private_offer

        DEPRECATED. Please use the `post_update_private_offer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_update_private_offer` interceptor runs
        before the `post_update_private_offer_with_metadata` interceptor.
        """
        return response

    def post_update_private_offer_with_metadata(
        self,
        response: gcc_private_offer.PrivateOffer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_private_offer.PrivateOffer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_private_offer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_update_private_offer_with_metadata`
        interceptor in new development instead of the `post_update_private_offer` interceptor.
        When both interceptors are used, this `post_update_private_offer_with_metadata` interceptor runs after the
        `post_update_private_offer` interceptor. The (possibly modified) response returned by
        `post_update_private_offer` will be passed to
        `post_update_private_offer_with_metadata`.
        """
        return response, metadata

    def pre_update_private_offer_document(
        self,
        request: commerce_transaction.UpdatePrivateOfferDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        commerce_transaction.UpdatePrivateOfferDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_private_offer_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_update_private_offer_document(
        self, response: private_offer.PrivateOfferDocument
    ) -> private_offer.PrivateOfferDocument:
        """Post-rpc interceptor for update_private_offer_document

        DEPRECATED. Please use the `post_update_private_offer_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code. This `post_update_private_offer_document` interceptor runs
        before the `post_update_private_offer_document_with_metadata` interceptor.
        """
        return response

    def post_update_private_offer_document_with_metadata(
        self,
        response: private_offer.PrivateOfferDocument,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        private_offer.PrivateOfferDocument, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_private_offer_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CommerceTransaction server but before it is returned to user code.

        We recommend only using this `post_update_private_offer_document_with_metadata`
        interceptor in new development instead of the `post_update_private_offer_document` interceptor.
        When both interceptors are used, this `post_update_private_offer_document_with_metadata` interceptor runs after the
        `post_update_private_offer_document` interceptor. The (possibly modified) response returned by
        `post_update_private_offer_document` will be passed to
        `post_update_private_offer_document_with_metadata`.
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
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the CommerceTransaction server but before
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
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CommerceTransaction server but before
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
        before they are sent to the CommerceTransaction server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CommerceTransaction server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CommerceTransactionRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CommerceTransactionRestInterceptor


class CommerceTransactionRestTransport(_BaseCommerceTransactionRestTransport):
    """REST backend synchronous transport for CommerceTransaction.

    APIs related to managing resources that model commercial
    transactions.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "commerceproducer.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CommerceTransactionRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'commerceproducer.googleapis.com').
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
            interceptor (Optional[CommerceTransactionRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CommerceTransactionRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CancelPrivateOffer(
        _BaseCommerceTransactionRestTransport._BaseCancelPrivateOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.CancelPrivateOffer")

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
            request: commerce_transaction.CancelPrivateOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOffer:
            r"""Call the cancel private offer method over HTTP.

            Args:
                request (~.commerce_transaction.CancelPrivateOfferRequest):
                    The request object. Message for cancelling a PrivateOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.private_offer.PrivateOffer:
                    Message describing PrivateOffer
                resource.
                Note on OPTIONAL fields: To facilitate
                saving incomplete draft offers, most
                fields are categorized as OPTIONAL
                irrespective of whether they are
                necessary for a private offer to be
                valid. Many fields labeled OPTIONAL must
                be set to publish the offer.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseCancelPrivateOffer._get_http_options()
            request, metadata = self._interceptor.pre_cancel_private_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseCancelPrivateOffer,
                    "_BaseCancelPrivateOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.CancelPrivateOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CancelPrivateOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._CancelPrivateOffer._get_response(
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
            resp = private_offer.PrivateOffer()
            pb_resp = private_offer.PrivateOffer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_cancel_private_offer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_private_offer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOffer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.cancel_private_offer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CancelPrivateOffer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePrivateOffer(
        _BaseCommerceTransactionRestTransport._BaseCreatePrivateOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.CreatePrivateOffer")

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
            request: commerce_transaction.CreatePrivateOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOffer:
            r"""Call the create private offer method over HTTP.

            Args:
                request (~.commerce_transaction.CreatePrivateOfferRequest):
                    The request object. Message for creating a PrivateOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.private_offer.PrivateOffer:
                    Message describing PrivateOffer
                resource.
                Note on OPTIONAL fields: To facilitate
                saving incomplete draft offers, most
                fields are categorized as OPTIONAL
                irrespective of whether they are
                necessary for a private offer to be
                valid. Many fields labeled OPTIONAL must
                be set to publish the offer.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseCreatePrivateOffer._get_http_options()
            request, metadata = self._interceptor.pre_create_private_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseCreatePrivateOffer,
                    "_BaseCreatePrivateOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.CreatePrivateOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CreatePrivateOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._CreatePrivateOffer._get_response(
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
            resp = private_offer.PrivateOffer()
            pb_resp = private_offer.PrivateOffer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_private_offer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_private_offer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOffer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.create_private_offer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CreatePrivateOffer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePrivateOfferDocument(
        _BaseCommerceTransactionRestTransport._BaseCreatePrivateOfferDocument,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.CreatePrivateOfferDocument")

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
            request: commerce_transaction.CreatePrivateOfferDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOfferDocument:
            r"""Call the create private offer
            document method over HTTP.

                Args:
                    request (~.commerce_transaction.CreatePrivateOfferDocumentRequest):
                        The request object. Message for creating a
                    PrivateOfferDocument.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.private_offer.PrivateOfferDocument:
                        Message describing the PrivateOfferDocument resource.
                    Used to attach documents to a private offer in state
                    DRAFT. Once a private offer is no longer in state DRAFT,
                    the set of child documents is immutable. Existing
                    documents cannot be updated or deleted, and new
                    documents cannot be added.

                    A private offer may have at most one document of each
                    type, and may not have both a standard EULA and a custom
                    EULA.

                    Which document types are required, optional, or not
                    permitted depends on the service the offer is for, and
                    is returned in ``Service.document_requirement``.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseCreatePrivateOfferDocument._get_http_options()
            request, metadata = self._interceptor.pre_create_private_offer_document(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseCreatePrivateOfferDocument,
                    "_BaseCreatePrivateOfferDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.CreatePrivateOfferDocument",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CreatePrivateOfferDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._CreatePrivateOfferDocument._get_response(
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
            resp = private_offer.PrivateOfferDocument()
            pb_resp = private_offer.PrivateOfferDocument.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_private_offer_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_private_offer_document_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOfferDocument.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.create_private_offer_document",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CreatePrivateOfferDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePrivateOffer(
        _BaseCommerceTransactionRestTransport._BaseDeletePrivateOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.DeletePrivateOffer")

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
            request: commerce_transaction.DeletePrivateOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete private offer method over HTTP.

            Args:
                request (~.commerce_transaction.DeletePrivateOfferRequest):
                    The request object. Message for deleting a PrivateOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCommerceTransactionRestTransport._BaseDeletePrivateOffer._get_http_options()
            request, metadata = self._interceptor.pre_delete_private_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseDeletePrivateOffer,
                    "_BaseDeletePrivateOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.DeletePrivateOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "DeletePrivateOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._DeletePrivateOffer._get_response(
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

    class _DeletePrivateOfferDocument(
        _BaseCommerceTransactionRestTransport._BaseDeletePrivateOfferDocument,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.DeletePrivateOfferDocument")

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
            request: commerce_transaction.DeletePrivateOfferDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete private offer
            document method over HTTP.

                Args:
                    request (~.commerce_transaction.DeletePrivateOfferDocumentRequest):
                        The request object. Message for deleting a
                    PrivateOfferDocument
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseCommerceTransactionRestTransport._BaseDeletePrivateOfferDocument._get_http_options()
            request, metadata = self._interceptor.pre_delete_private_offer_document(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseDeletePrivateOfferDocument,
                    "_BaseDeletePrivateOfferDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.DeletePrivateOfferDocument",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "DeletePrivateOfferDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._DeletePrivateOfferDocument._get_response(
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

    class _GetPrivateOffer(
        _BaseCommerceTransactionRestTransport._BaseGetPrivateOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetPrivateOffer")

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
            request: commerce_transaction.GetPrivateOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOffer:
            r"""Call the get private offer method over HTTP.

            Args:
                request (~.commerce_transaction.GetPrivateOfferRequest):
                    The request object. Message for getting a PrivateOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.private_offer.PrivateOffer:
                    Message describing PrivateOffer
                resource.
                Note on OPTIONAL fields: To facilitate
                saving incomplete draft offers, most
                fields are categorized as OPTIONAL
                irrespective of whether they are
                necessary for a private offer to be
                valid. Many fields labeled OPTIONAL must
                be set to publish the offer.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseGetPrivateOffer._get_http_options()
            request, metadata = self._interceptor.pre_get_private_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetPrivateOffer,
                    "_BaseGetPrivateOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetPrivateOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetPrivateOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetPrivateOffer._get_response(
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
            resp = private_offer.PrivateOffer()
            pb_resp = private_offer.PrivateOffer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_private_offer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_private_offer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOffer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.get_private_offer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetPrivateOffer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPrivateOfferDocument(
        _BaseCommerceTransactionRestTransport._BaseGetPrivateOfferDocument,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetPrivateOfferDocument")

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
            request: commerce_transaction.GetPrivateOfferDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOfferDocument:
            r"""Call the get private offer
            document method over HTTP.

                Args:
                    request (~.commerce_transaction.GetPrivateOfferDocumentRequest):
                        The request object. Message for getting a
                    PrivateOfferDocument
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.private_offer.PrivateOfferDocument:
                        Message describing the PrivateOfferDocument resource.
                    Used to attach documents to a private offer in state
                    DRAFT. Once a private offer is no longer in state DRAFT,
                    the set of child documents is immutable. Existing
                    documents cannot be updated or deleted, and new
                    documents cannot be added.

                    A private offer may have at most one document of each
                    type, and may not have both a standard EULA and a custom
                    EULA.

                    Which document types are required, optional, or not
                    permitted depends on the service the offer is for, and
                    is returned in ``Service.document_requirement``.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseGetPrivateOfferDocument._get_http_options()
            request, metadata = self._interceptor.pre_get_private_offer_document(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetPrivateOfferDocument,
                    "_BaseGetPrivateOfferDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetPrivateOfferDocument",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetPrivateOfferDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._GetPrivateOfferDocument._get_response(
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
            resp = private_offer.PrivateOfferDocument()
            pb_resp = private_offer.PrivateOfferDocument.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_private_offer_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_private_offer_document_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOfferDocument.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.get_private_offer_document",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetPrivateOfferDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetService(
        _BaseCommerceTransactionRestTransport._BaseGetService,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetService")

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
            request: commerce_transaction.GetServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Service:
            r"""Call the get service method over HTTP.

            Args:
                request (~.commerce_transaction.GetServiceRequest):
                    The request object. Message for getting a Service
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Service:
                    Message describing Service resource.
            """

            http_options = _BaseCommerceTransactionRestTransport._BaseGetService._get_http_options()
            request, metadata = self._interceptor.pre_get_service(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetService,
                    "_BaseGetService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetService",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetService._get_response(
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
            resp = service.Service()
            pb_resp = service.Service.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Service.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.get_service",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSku(
        _BaseCommerceTransactionRestTransport._BaseGetSku, CommerceTransactionRestStub
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetSku")

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
            request: commerce_transaction.GetSkuRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sku.Sku:
            r"""Call the get sku method over HTTP.

            Args:
                request (~.commerce_transaction.GetSkuRequest):
                    The request object. Message for getting a Sku
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sku.Sku:
                    Message describing the Sku resource.

                Encapsulates and represents a stock keeping unit (SKU),
                the atomic unit of pricing and billing in Google Cloud.
                Each customer charge is associated with and originates
                from exactly one SKU. While the Cloud Marketplace Sku
                resource shares a close relationship with the public
                `Sku resource in the Cloud Billing
                API <https://cloud.google.com/billing/docs/how-to/get-pricing-information-api>`__,
                Cloud Marketplace SKUs are represented here with
                additional information in an alternative format tailored
                for use by Cloud Marketplace partners, and are not
                necessarily public and by extension are not generally
                visible in the Cloud Billing API or the `Google Cloud
                Public SKUs <https://cloud.google.com/skus>`__.

                Note on terminology: While the name of the resource
                derives from the acronym 'SKU' it is named 'Sku' for
                consistency with other resource type names, and may be
                rendered variously as 'Sku', 'sku', or 'SKU' across this
                and other documentation.

            """

            http_options = (
                _BaseCommerceTransactionRestTransport._BaseGetSku._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_sku(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetSku,
                    "_BaseGetSku__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetSku",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetSku",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetSku._get_response(
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
            resp = sku.Sku()
            pb_resp = sku.Sku.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_sku(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_sku_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sku.Sku.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.get_sku",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetSku",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSkuGroup(
        _BaseCommerceTransactionRestTransport._BaseGetSkuGroup,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetSkuGroup")

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
            request: commerce_transaction.GetSkuGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sku_group.SkuGroup:
            r"""Call the get sku group method over HTTP.

            Args:
                request (~.commerce_transaction.GetSkuGroupRequest):
                    The request object. Message for getting a SkuGroup
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sku_group.SkuGroup:
                    Message describing SkuGroup resource
            """

            http_options = _BaseCommerceTransactionRestTransport._BaseGetSkuGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_sku_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetSkuGroup,
                    "_BaseGetSkuGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetSkuGroup",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetSkuGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetSkuGroup._get_response(
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
            resp = sku_group.SkuGroup()
            pb_resp = sku_group.SkuGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_sku_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_sku_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sku_group.SkuGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.get_sku_group",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetSkuGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetStandardOffer(
        _BaseCommerceTransactionRestTransport._BaseGetStandardOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetStandardOffer")

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
            request: commerce_transaction.GetStandardOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> standard_offer.StandardOffer:
            r"""Call the get standard offer method over HTTP.

            Args:
                request (~.commerce_transaction.GetStandardOfferRequest):
                    The request object. Message for getting a StandardOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.standard_offer.StandardOffer:
                    Message describing the StandardOffer
                resource.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseGetStandardOffer._get_http_options()
            request, metadata = self._interceptor.pre_get_standard_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetStandardOffer,
                    "_BaseGetStandardOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetStandardOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetStandardOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetStandardOffer._get_response(
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
            resp = standard_offer.StandardOffer()
            pb_resp = standard_offer.StandardOffer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_standard_offer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_standard_offer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = standard_offer.StandardOffer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.get_standard_offer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetStandardOffer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrivateOfferDocuments(
        _BaseCommerceTransactionRestTransport._BaseListPrivateOfferDocuments,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListPrivateOfferDocuments")

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
            request: commerce_transaction.ListPrivateOfferDocumentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ListPrivateOfferDocumentsResponse:
            r"""Call the list private offer
            documents method over HTTP.

                Args:
                    request (~.commerce_transaction.ListPrivateOfferDocumentsRequest):
                        The request object. Message for requesting list of
                    PrivateOfferDocuments
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.commerce_transaction.ListPrivateOfferDocumentsResponse:
                        Message for response to listing
                    PrivateOfferDocuments

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseListPrivateOfferDocuments._get_http_options()
            request, metadata = self._interceptor.pre_list_private_offer_documents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListPrivateOfferDocuments,
                    "_BaseListPrivateOfferDocuments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListPrivateOfferDocuments",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListPrivateOfferDocuments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._ListPrivateOfferDocuments._get_response(
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
            resp = commerce_transaction.ListPrivateOfferDocumentsResponse()
            pb_resp = commerce_transaction.ListPrivateOfferDocumentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_private_offer_documents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_private_offer_documents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        commerce_transaction.ListPrivateOfferDocumentsResponse.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.list_private_offer_documents",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListPrivateOfferDocuments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrivateOffers(
        _BaseCommerceTransactionRestTransport._BaseListPrivateOffers,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListPrivateOffers")

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
            request: commerce_transaction.ListPrivateOffersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ListPrivateOffersResponse:
            r"""Call the list private offers method over HTTP.

            Args:
                request (~.commerce_transaction.ListPrivateOffersRequest):
                    The request object. Message for requesting list of
                PrivateOffers
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.commerce_transaction.ListPrivateOffersResponse:
                    Message for response to listing
                PrivateOffers

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseListPrivateOffers._get_http_options()
            request, metadata = self._interceptor.pre_list_private_offers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListPrivateOffers,
                    "_BaseListPrivateOffers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListPrivateOffers",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListPrivateOffers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._ListPrivateOffers._get_response(
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
            resp = commerce_transaction.ListPrivateOffersResponse()
            pb_resp = commerce_transaction.ListPrivateOffersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_private_offers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_private_offers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        commerce_transaction.ListPrivateOffersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.list_private_offers",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListPrivateOffers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServices(
        _BaseCommerceTransactionRestTransport._BaseListServices,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListServices")

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
            request: commerce_transaction.ListServicesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ListServicesResponse:
            r"""Call the list services method over HTTP.

            Args:
                request (~.commerce_transaction.ListServicesRequest):
                    The request object. Message for requesting list of
                Services
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.commerce_transaction.ListServicesResponse:
                    Message for response to listing
                Services

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseListServices._get_http_options()
            request, metadata = self._interceptor.pre_list_services(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListServices,
                    "_BaseListServices__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListServices",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListServices",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._ListServices._get_response(
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
            resp = commerce_transaction.ListServicesResponse()
            pb_resp = commerce_transaction.ListServicesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_services(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_services_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        commerce_transaction.ListServicesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.list_services",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListServices",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSkuGroups(
        _BaseCommerceTransactionRestTransport._BaseListSkuGroups,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListSkuGroups")

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
            request: commerce_transaction.ListSkuGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ListSkuGroupsResponse:
            r"""Call the list sku groups method over HTTP.

            Args:
                request (~.commerce_transaction.ListSkuGroupsRequest):
                    The request object. Message for requesting list of
                SkuGroups
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.commerce_transaction.ListSkuGroupsResponse:
                    Message for response to listing
                SkuGroups

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseListSkuGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_sku_groups(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListSkuGroups,
                    "_BaseListSkuGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListSkuGroups",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListSkuGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._ListSkuGroups._get_response(
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
            resp = commerce_transaction.ListSkuGroupsResponse()
            pb_resp = commerce_transaction.ListSkuGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_sku_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_sku_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        commerce_transaction.ListSkuGroupsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.list_sku_groups",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListSkuGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSkus(
        _BaseCommerceTransactionRestTransport._BaseListSkus, CommerceTransactionRestStub
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListSkus")

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
            request: commerce_transaction.ListSkusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ListSkusResponse:
            r"""Call the list skus method over HTTP.

            Args:
                request (~.commerce_transaction.ListSkusRequest):
                    The request object. Message for requesting list of Skus
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.commerce_transaction.ListSkusResponse:
                    Message for response to listing Skus
            """

            http_options = (
                _BaseCommerceTransactionRestTransport._BaseListSkus._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_skus(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListSkus,
                    "_BaseListSkus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListSkus",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListSkus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._ListSkus._get_response(
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
            resp = commerce_transaction.ListSkusResponse()
            pb_resp = commerce_transaction.ListSkusResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_skus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_skus_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = commerce_transaction.ListSkusResponse.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.list_skus",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListSkus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListStandardOffers(
        _BaseCommerceTransactionRestTransport._BaseListStandardOffers,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListStandardOffers")

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
            request: commerce_transaction.ListStandardOffersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ListStandardOffersResponse:
            r"""Call the list standard offers method over HTTP.

            Args:
                request (~.commerce_transaction.ListStandardOffersRequest):
                    The request object. Message for requesting list of
                StandardOffers
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.commerce_transaction.ListStandardOffersResponse:
                    Message for response to listing
                StandardOffers

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseListStandardOffers._get_http_options()
            request, metadata = self._interceptor.pre_list_standard_offers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListStandardOffers,
                    "_BaseListStandardOffers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListStandardOffers",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListStandardOffers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._ListStandardOffers._get_response(
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
            resp = commerce_transaction.ListStandardOffersResponse()
            pb_resp = commerce_transaction.ListStandardOffersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_standard_offers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_standard_offers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        commerce_transaction.ListStandardOffersResponse.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.list_standard_offers",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListStandardOffers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PublishPrivateOffer(
        _BaseCommerceTransactionRestTransport._BasePublishPrivateOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.PublishPrivateOffer")

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
            request: commerce_transaction.PublishPrivateOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOffer:
            r"""Call the publish private offer method over HTTP.

            Args:
                request (~.commerce_transaction.PublishPrivateOfferRequest):
                    The request object. Message for publishing a PrivateOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.private_offer.PrivateOffer:
                    Message describing PrivateOffer
                resource.
                Note on OPTIONAL fields: To facilitate
                saving incomplete draft offers, most
                fields are categorized as OPTIONAL
                irrespective of whether they are
                necessary for a private offer to be
                valid. Many fields labeled OPTIONAL must
                be set to publish the offer.

            """

            http_options = _BaseCommerceTransactionRestTransport._BasePublishPrivateOffer._get_http_options()
            request, metadata = self._interceptor.pre_publish_private_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BasePublishPrivateOffer,
                    "_BasePublishPrivateOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.PublishPrivateOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "PublishPrivateOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._PublishPrivateOffer._get_response(
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
            resp = private_offer.PrivateOffer()
            pb_resp = private_offer.PrivateOffer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_publish_private_offer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_publish_private_offer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOffer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.publish_private_offer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "PublishPrivateOffer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResolveAmendmentTarget(
        _BaseCommerceTransactionRestTransport._BaseResolveAmendmentTarget,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ResolveAmendmentTarget")

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
            request: commerce_transaction.ResolveAmendmentTargetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> commerce_transaction.ResolveAmendmentTargetResponse:
            r"""Call the resolve amendment target method over HTTP.

            Args:
                request (~.commerce_transaction.ResolveAmendmentTargetRequest):
                    The request object. Message for resolving an amended
                offer.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.commerce_transaction.ResolveAmendmentTargetResponse:
                    Message in response to
                ResolveAmendmentTarget.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseResolveAmendmentTarget._get_http_options()
            request, metadata = self._interceptor.pre_resolve_amendment_target(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseResolveAmendmentTarget,
                    "_BaseResolveAmendmentTarget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ResolveAmendmentTarget",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ResolveAmendmentTarget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._ResolveAmendmentTarget._get_response(
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
            resp = commerce_transaction.ResolveAmendmentTargetResponse()
            pb_resp = commerce_transaction.ResolveAmendmentTargetResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_resolve_amendment_target(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resolve_amendment_target_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        commerce_transaction.ResolveAmendmentTargetResponse.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.resolve_amendment_target",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ResolveAmendmentTarget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePrivateOffer(
        _BaseCommerceTransactionRestTransport._BaseUpdatePrivateOffer,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.UpdatePrivateOffer")

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
            request: commerce_transaction.UpdatePrivateOfferRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_private_offer.PrivateOffer:
            r"""Call the update private offer method over HTTP.

            Args:
                request (~.commerce_transaction.UpdatePrivateOfferRequest):
                    The request object. Message for updating a PrivateOffer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_private_offer.PrivateOffer:
                    Message describing PrivateOffer
                resource.
                Note on OPTIONAL fields: To facilitate
                saving incomplete draft offers, most
                fields are categorized as OPTIONAL
                irrespective of whether they are
                necessary for a private offer to be
                valid. Many fields labeled OPTIONAL must
                be set to publish the offer.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseUpdatePrivateOffer._get_http_options()
            request, metadata = self._interceptor.pre_update_private_offer(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseUpdatePrivateOffer,
                    "_BaseUpdatePrivateOffer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.UpdatePrivateOffer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "UpdatePrivateOffer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CommerceTransactionRestTransport._UpdatePrivateOffer._get_response(
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
            resp = gcc_private_offer.PrivateOffer()
            pb_resp = gcc_private_offer.PrivateOffer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_private_offer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_private_offer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_private_offer.PrivateOffer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.update_private_offer",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "UpdatePrivateOffer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePrivateOfferDocument(
        _BaseCommerceTransactionRestTransport._BaseUpdatePrivateOfferDocument,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.UpdatePrivateOfferDocument")

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
            request: commerce_transaction.UpdatePrivateOfferDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> private_offer.PrivateOfferDocument:
            r"""Call the update private offer
            document method over HTTP.

                Args:
                    request (~.commerce_transaction.UpdatePrivateOfferDocumentRequest):
                        The request object. Message for updating a
                    PrivateOfferDocument
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.private_offer.PrivateOfferDocument:
                        Message describing the PrivateOfferDocument resource.
                    Used to attach documents to a private offer in state
                    DRAFT. Once a private offer is no longer in state DRAFT,
                    the set of child documents is immutable. Existing
                    documents cannot be updated or deleted, and new
                    documents cannot be added.

                    A private offer may have at most one document of each
                    type, and may not have both a standard EULA and a custom
                    EULA.

                    Which document types are required, optional, or not
                    permitted depends on the service the offer is for, and
                    is returned in ``Service.document_requirement``.

            """

            http_options = _BaseCommerceTransactionRestTransport._BaseUpdatePrivateOfferDocument._get_http_options()
            request, metadata = self._interceptor.pre_update_private_offer_document(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseUpdatePrivateOfferDocument,
                    "_BaseUpdatePrivateOfferDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.UpdatePrivateOfferDocument",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "UpdatePrivateOfferDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._UpdatePrivateOfferDocument._get_response(
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
            resp = private_offer.PrivateOfferDocument()
            pb_resp = private_offer.PrivateOfferDocument.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_private_offer_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_private_offer_document_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = private_offer.PrivateOfferDocument.to_json(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.update_private_offer_document",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "UpdatePrivateOfferDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def cancel_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.CancelPrivateOfferRequest], private_offer.PrivateOffer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelPrivateOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.CreatePrivateOfferRequest], private_offer.PrivateOffer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePrivateOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.CreatePrivateOfferDocumentRequest],
        private_offer.PrivateOfferDocument,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePrivateOfferDocument(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_private_offer(
        self,
    ) -> Callable[[commerce_transaction.DeletePrivateOfferRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePrivateOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.DeletePrivateOfferDocumentRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePrivateOfferDocument(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.GetPrivateOfferRequest], private_offer.PrivateOffer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPrivateOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.GetPrivateOfferDocumentRequest],
        private_offer.PrivateOfferDocument,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPrivateOfferDocument(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_service(
        self,
    ) -> Callable[[commerce_transaction.GetServiceRequest], service.Service]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_sku(self) -> Callable[[commerce_transaction.GetSkuRequest], sku.Sku]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSku(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_sku_group(
        self,
    ) -> Callable[[commerce_transaction.GetSkuGroupRequest], sku_group.SkuGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSkuGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_standard_offer(
        self,
    ) -> Callable[
        [commerce_transaction.GetStandardOfferRequest], standard_offer.StandardOffer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStandardOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_private_offer_documents(
        self,
    ) -> Callable[
        [commerce_transaction.ListPrivateOfferDocumentsRequest],
        commerce_transaction.ListPrivateOfferDocumentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateOfferDocuments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_private_offers(
        self,
    ) -> Callable[
        [commerce_transaction.ListPrivateOffersRequest],
        commerce_transaction.ListPrivateOffersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateOffers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_services(
        self,
    ) -> Callable[
        [commerce_transaction.ListServicesRequest],
        commerce_transaction.ListServicesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServices(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_sku_groups(
        self,
    ) -> Callable[
        [commerce_transaction.ListSkuGroupsRequest],
        commerce_transaction.ListSkuGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSkuGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_skus(
        self,
    ) -> Callable[
        [commerce_transaction.ListSkusRequest], commerce_transaction.ListSkusResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSkus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_standard_offers(
        self,
    ) -> Callable[
        [commerce_transaction.ListStandardOffersRequest],
        commerce_transaction.ListStandardOffersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStandardOffers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def publish_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.PublishPrivateOfferRequest], private_offer.PrivateOffer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PublishPrivateOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resolve_amendment_target(
        self,
    ) -> Callable[
        [commerce_transaction.ResolveAmendmentTargetRequest],
        commerce_transaction.ResolveAmendmentTargetResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResolveAmendmentTarget(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.UpdatePrivateOfferRequest], gcc_private_offer.PrivateOffer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePrivateOffer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.UpdatePrivateOfferDocumentRequest],
        private_offer.PrivateOfferDocument,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePrivateOfferDocument(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseCommerceTransactionRestTransport._BaseGetLocation,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetLocation")

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

            http_options = _BaseCommerceTransactionRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
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
        _BaseCommerceTransactionRestTransport._BaseListLocations,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListLocations")

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

            http_options = _BaseCommerceTransactionRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCommerceTransactionRestTransport._BaseCancelOperation,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.CancelOperation")

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
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCommerceTransactionRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseCommerceTransactionRestTransport._BaseDeleteOperation,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCommerceTransactionRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCommerceTransactionRestTransport._BaseGetOperation,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.GetOperation")

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

            http_options = _BaseCommerceTransactionRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
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
        _BaseCommerceTransactionRestTransport._BaseListOperations,
        CommerceTransactionRestStub,
    ):
        def __hash__(self):
            return hash("CommerceTransactionRestTransport.ListOperations")

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

            http_options = _BaseCommerceTransactionRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCommerceTransactionRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.commerceproducer_v1beta.CommerceTransactionClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CommerceTransactionRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.commerceproducer_v1beta.CommerceTransactionAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
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


__all__ = ("CommerceTransactionRestTransport",)
