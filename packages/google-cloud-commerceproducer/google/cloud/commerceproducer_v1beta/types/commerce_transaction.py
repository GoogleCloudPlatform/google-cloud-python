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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.commerceproducer_v1beta.types import (
    private_offer as gcc_private_offer,
)
from google.cloud.commerceproducer_v1beta.types import (
    service,
    sku,
    sku_group,
    standard_offer,
)

__protobuf__ = proto.module(
    package="google.cloud.commerceproducer.v1beta",
    manifest={
        "PrivateOfferView",
        "StandardOfferView",
        "ServiceView",
        "ListPrivateOffersRequest",
        "ListPrivateOffersResponse",
        "GetPrivateOfferRequest",
        "ResolveAmendmentTargetRequest",
        "ResolveAmendmentTargetResponse",
        "CreatePrivateOfferRequest",
        "UpdatePrivateOfferRequest",
        "PublishPrivateOfferRequest",
        "CancelPrivateOfferRequest",
        "DeletePrivateOfferRequest",
        "ListPrivateOfferDocumentsRequest",
        "ListPrivateOfferDocumentsResponse",
        "GetPrivateOfferDocumentRequest",
        "CreatePrivateOfferDocumentRequest",
        "UpdatePrivateOfferDocumentRequest",
        "DeletePrivateOfferDocumentRequest",
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "ListStandardOffersRequest",
        "ListStandardOffersResponse",
        "GetStandardOfferRequest",
        "ListSkusRequest",
        "ListSkusResponse",
        "GetSkuRequest",
        "GetSkuGroupRequest",
        "ListSkuGroupsRequest",
        "ListSkuGroupsResponse",
    },
)


class PrivateOfferView(proto.Enum):
    r"""Controls which fields are returned in a PrivateOffer returned
    by the API. https://google.aip.dev/157

    Values:
        PRIVATE_OFFER_VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the BASIC view.
        PRIVATE_OFFER_VIEW_BASIC (1):
            Include basic metadata about the
            PrivateOffer, but not the full contents. This is
            the default value (for both List and Get
            requests).
        PRIVATE_OFFER_VIEW_FULL (2):
            Include everything.
    """

    PRIVATE_OFFER_VIEW_UNSPECIFIED = 0
    PRIVATE_OFFER_VIEW_BASIC = 1
    PRIVATE_OFFER_VIEW_FULL = 2


class StandardOfferView(proto.Enum):
    r"""Controls which fields are returned in a StandardOffer
    returned by the API. https://google.aip.dev/157

    Values:
        STANDARD_OFFER_VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the BASIC view.
        STANDARD_OFFER_VIEW_BASIC (1):
            Include basic metadata about the
            StandardOffer, but not the full contents. This
            is the default value (for both List and Get
            requests).
        STANDARD_OFFER_VIEW_FULL (2):
            Include everything.
    """

    STANDARD_OFFER_VIEW_UNSPECIFIED = 0
    STANDARD_OFFER_VIEW_BASIC = 1
    STANDARD_OFFER_VIEW_FULL = 2


class ServiceView(proto.Enum):
    r"""Controls which fields are returned in a Service returned by
    the API. https://google.aip.dev/157

    Values:
        SERVICE_VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the BASIC view.
        SERVICE_VIEW_BASIC (1):
            Include basic metadata about the Service, but
            not the full contents. This is the default value
            (for both List and Get requests).
        SERVICE_VIEW_FULL (2):
            Include everything.
    """

    SERVICE_VIEW_UNSPECIFIED = 0
    SERVICE_VIEW_BASIC = 1
    SERVICE_VIEW_FULL = 2


class ListPrivateOffersRequest(proto.Message):
    r"""Message for requesting list of PrivateOffers

    Attributes:
        parent (str):
            Required. Parent value for
            ListPrivateOffersRequest
        page_size (int):
            Optional. Maximum results to return. The
            service may return fewer than this value. The
            maximum value is 500; values above 500 will be
            coerced to 500. If unspecified, the server will
            default to the maximum.
        page_token (str):
            Optional. A page token, received from a
            previous list response message. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters of the
            list request must match the request that
            returned the page token.
        filter (str):
            Optional. Filter expression that matches a subset of
            resources to show. See https://google.aip.dev/160 for more
            details. Only supports filtering by:

            - ``update_time``. Example:
              ``update_time > "2012-04-21T11:30:00-04:00"``.
        order_by (str):
            Optional. Ordering expression for sorting the results. See
            https://google.aip.dev/132#ordering for more details. If no
            value is present the default ordering is unspecified. Only
            supports ordering by:

            - ``update_time``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListPrivateOffersResponse(proto.Message):
    r"""Message for response to listing PrivateOffers

    Attributes:
        private_offers (MutableSequence[google.cloud.commerceproducer_v1beta.types.PrivateOffer]):
            The list of PrivateOffer
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    private_offers: MutableSequence[gcc_private_offer.PrivateOffer] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcc_private_offer.PrivateOffer,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPrivateOfferRequest(proto.Message):
    r"""Message for getting a PrivateOffer

    Attributes:
        name (str):
            Required. Name of the resource
        view (google.cloud.commerceproducer_v1beta.types.PrivateOfferView):
            Optional. The view of the PrivateOffer to
            return. If unspecified, the default view is
            BASIC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "PrivateOfferView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PrivateOfferView",
    )


class ResolveAmendmentTargetRequest(proto.Message):
    r"""Message for resolving an amended offer.

    Attributes:
        parent (str):
            Required. Parent value for
            ResolveAmendmentTargetRequest
        target_billing_account (str):
            Required. The customer's billing account targeted by the
            offer. This is the billing account for which the new private
            offer will be created on. Format:
            billingAccounts/{billing_account}.
        base_standard_offer (str):
            Required. The base standard offer that the private offer
            will be based on. Format:
            projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_billing_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    base_standard_offer: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ResolveAmendmentTargetResponse(proto.Message):
    r"""Message in response to ResolveAmendmentTarget.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        required_private_offer (str):
            The resource name of an existing private offer that MUST be
            amended.

            If this is set, the new private offer the client creates
            must populate the
            ``single_product_offer.amended_private_offer`` field with
            this value.

            This field is a member of `oneof`_ ``amendment_requirement``.
        required_standard_offer (str):
            The resource name of an existing standard offer that MUST be
            amended.

            If this is set, the new private offer the client creates
            must populate the
            ``single_product_offer.amended_standard_offer`` field with
            this value.

            This field is a member of `oneof`_ ``amendment_requirement``.
        optional_offers (google.cloud.commerceproducer_v1beta.types.ResolveAmendmentTargetResponse.OptionalOffers):
            A list of existing offers that may optionally
            be amended.

            This field is a member of `oneof`_ ``amendment_requirement``.
    """

    class OptionalOffers(proto.Message):
        r"""A wrapper message containing offers that can optionally be
        amended.

        Attributes:
            private_offers (MutableSequence[str]):
                A list of existing private offers that are eligible to be
                amended.

                When creating a new private offer, the client may choose to
                populate the ``single_product_offer.amended_private_offer``
                field with one of these resource names. Alternatively, the
                client may leave the field unset to create a brand new
                offer.
        """

        private_offers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    required_private_offer: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="amendment_requirement",
    )
    required_standard_offer: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="amendment_requirement",
    )
    optional_offers: OptionalOffers = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="amendment_requirement",
        message=OptionalOffers,
    )


class CreatePrivateOfferRequest(proto.Message):
    r"""Message for creating a PrivateOffer

    Attributes:
        parent (str):
            Required. Value for parent.
        private_offer (google.cloud.commerceproducer_v1beta.types.PrivateOffer):
            Required. The resource being created
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_offer: gcc_private_offer.PrivateOffer = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_private_offer.PrivateOffer,
    )


class UpdatePrivateOfferRequest(proto.Message):
    r"""Message for updating a PrivateOffer

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. The special value "\*" means full replacement. If
            unspecified, all fields present in the request will be
            overwritten.
        private_offer (google.cloud.commerceproducer_v1beta.types.PrivateOffer):
            Required. The resource being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    private_offer: gcc_private_offer.PrivateOffer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_private_offer.PrivateOffer,
    )


class PublishPrivateOfferRequest(proto.Message):
    r"""Message for publishing a PrivateOffer

    Attributes:
        name (str):
            Required. Name of the resource
        validate_only (bool):
            Optional. If set to ``true``, validates the request but does
            not execute it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CancelPrivateOfferRequest(proto.Message):
    r"""Message for cancelling a PrivateOffer

    Attributes:
        name (str):
            Required. Name of the resource
        cancellation_note (str):
            Optional. Internal note relating to the
            cancellation. Stored on the cancelled offer. Not
            visible to customers.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cancellation_note: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeletePrivateOfferRequest(proto.Message):
    r"""Message for deleting a PrivateOffer

    Attributes:
        name (str):
            Required. Name of the resource
        force (bool):
            Optional. Indicates whether to cascade the
            delete to child resources. If false, the request
            fails if child resources exist.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListPrivateOfferDocumentsRequest(proto.Message):
    r"""Message for requesting list of PrivateOfferDocuments

    Attributes:
        parent (str):
            Required. Parent value for
            ListPrivateOfferDocumentsRequest.
        page_size (int):
            Optional. Maximum results to return. The
            service may return fewer than this value. The
            maximum value is 500; values above 500 will be
            coerced to 500. If unspecified, the server will
            default to the maximum.
        page_token (str):
            Optional. A page token, received from a
            previous list response message. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters of the
            list request must match the request that
            returned the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListPrivateOfferDocumentsResponse(proto.Message):
    r"""Message for response to listing PrivateOfferDocuments

    Attributes:
        private_offer_documents (MutableSequence[google.cloud.commerceproducer_v1beta.types.PrivateOfferDocument]):
            The list of PrivateOfferDocuments.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    private_offer_documents: MutableSequence[gcc_private_offer.PrivateOfferDocument] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcc_private_offer.PrivateOfferDocument,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPrivateOfferDocumentRequest(proto.Message):
    r"""Message for getting a PrivateOfferDocument

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePrivateOfferDocumentRequest(proto.Message):
    r"""Message for creating a PrivateOfferDocument.

    Attributes:
        parent (str):
            Required. Value for parent.
        private_offer_document (google.cloud.commerceproducer_v1beta.types.PrivateOfferDocument):
            Required. The resource being created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_offer_document: gcc_private_offer.PrivateOfferDocument = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_private_offer.PrivateOfferDocument,
    )


class UpdatePrivateOfferDocumentRequest(proto.Message):
    r"""Message for updating a PrivateOfferDocument

    Attributes:
        private_offer_document (google.cloud.commerceproducer_v1beta.types.PrivateOfferDocument):
            Required. The resource being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. The special value "\*" means full replacement. If
            unspecified, all fields present in the request will be
            overwritten.
    """

    private_offer_document: gcc_private_offer.PrivateOfferDocument = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_private_offer.PrivateOfferDocument,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeletePrivateOfferDocumentRequest(proto.Message):
    r"""Message for deleting a PrivateOfferDocument

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListServicesRequest(proto.Message):
    r"""Message for requesting list of Services

    Attributes:
        parent (str):
            Required. Parent value for
            ListServicesRequest
        page_size (int):
            Optional. Maximum results to return. The
            service may return fewer than this value. The
            maximum value is 500; values above 500 will be
            coerced to 500. If unspecified, the server will
            default to the maximum.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListServicesResponse(proto.Message):
    r"""Message for response to listing Services

    Attributes:
        services (MutableSequence[google.cloud.commerceproducer_v1beta.types.Service]):
            The list of Service
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[service.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=service.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServiceRequest(proto.Message):
    r"""Message for getting a Service

    Attributes:
        name (str):
            Required. Name of the resource
        view (google.cloud.commerceproducer_v1beta.types.ServiceView):
            Optional. The view of the Service to return.
            If unspecified, the default view is BASIC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ServiceView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ServiceView",
    )


class ListStandardOffersRequest(proto.Message):
    r"""Message for requesting list of StandardOffers

    Attributes:
        parent (str):
            Required. Parent value for
            ListStandardOffersRequest
        page_size (int):
            Optional. Maximum results to return. The
            service may return fewer than this value. The
            maximum value is 500; values above 500 will be
            coerced to 500. If unspecified, the server will
            default to the maximum.
        page_token (str):
            Optional. A page token, received from a
            previous list response message. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters of the
            list request must match the request that
            returned the page token.
        filter (str):
            Optional. Filter expression that matches a subset of
            resources to show. See https://google.aip.dev/160 for more
            details. Supports filtering by:

            - ``effective_time``. Example:
              ``effective_time > "2012-04-21T11:30:00-04:00"``.
            - ``expire_time``. Example:
              ``expire_time < "2026-05-06T00:00:00Z"``.
        order_by (str):
            Optional. Ordering expression for sorting the results. See
            https://google.aip.dev/132#ordering for more details. If no
            value is present the default ordering is unspecified.
            Supports ordering by:

            - ``effective_time``
            - ``expire_time``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListStandardOffersResponse(proto.Message):
    r"""Message for response to listing StandardOffers

    Attributes:
        standard_offers (MutableSequence[google.cloud.commerceproducer_v1beta.types.StandardOffer]):
            The list of StandardOffer
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    standard_offers: MutableSequence[standard_offer.StandardOffer] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=standard_offer.StandardOffer,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetStandardOfferRequest(proto.Message):
    r"""Message for getting a StandardOffer

    Attributes:
        name (str):
            Required. Name of the resource
        view (google.cloud.commerceproducer_v1beta.types.StandardOfferView):
            Optional. The view of the StandardOffer to
            return. If unspecified, the default view is
            BASIC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "StandardOfferView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="StandardOfferView",
    )


class ListSkusRequest(proto.Message):
    r"""Message for requesting list of Skus

    Attributes:
        parent (str):
            Required. Parent value for ListSkusRequest
        page_size (int):
            Optional. Maximum results to return. The
            service may return fewer than this value. The
            maximum value is 500; values above 500 will be
            coerced to 500. If unspecified, the server will
            default to the maximum.
        page_token (str):
            Optional. A page token, received from a
            previous list response message. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters of the
            list request must match the request that
            returned the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSkusResponse(proto.Message):
    r"""Message for response to listing Skus

    Attributes:
        skus (MutableSequence[google.cloud.commerceproducer_v1beta.types.Sku]):
            The list of Sku
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    skus: MutableSequence[sku.Sku] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=sku.Sku,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSkuRequest(proto.Message):
    r"""Message for getting a Sku

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSkuGroupRequest(proto.Message):
    r"""Message for getting a SkuGroup

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSkuGroupsRequest(proto.Message):
    r"""Message for requesting list of SkuGroups

    Attributes:
        parent (str):
            Required. Parent value for
            ListSkuGroupsRequest
        page_size (int):
            Optional. Maximum results to return. The
            service may return fewer than this value. The
            maximum value is 500; values above 500 will be
            coerced to 500. If unspecified, the server will
            default to the maximum.
        page_token (str):
            Optional. A page token, received from a
            previous list response message. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters of the
            list request must match the request that
            returned the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSkuGroupsResponse(proto.Message):
    r"""Message for response to listing SkuGroups

    Attributes:
        sku_groups (MutableSequence[google.cloud.commerceproducer_v1beta.types.SkuGroup]):
            The list of SkuGroup
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    sku_groups: MutableSequence[sku_group.SkuGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=sku_group.SkuGroup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
