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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2alpha.types import common
from google.cloud.retail_v2alpha.types import product as gcr_product

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "CreateProductRequest",
        "GetProductRequest",
        "UpdateProductRequest",
        "DeleteProductRequest",
        "ListProductsRequest",
        "ListProductsResponse",
        "SetInventoryRequest",
        "SetInventoryMetadata",
        "SetInventoryResponse",
        "AddFulfillmentPlacesRequest",
        "AddFulfillmentPlacesMetadata",
        "AddFulfillmentPlacesResponse",
        "AddLocalInventoriesRequest",
        "AddLocalInventoriesMetadata",
        "AddLocalInventoriesResponse",
        "RemoveLocalInventoriesRequest",
        "RemoveLocalInventoriesMetadata",
        "RemoveLocalInventoriesResponse",
        "RemoveFulfillmentPlacesRequest",
        "RemoveFulfillmentPlacesMetadata",
        "RemoveFulfillmentPlacesResponse",
    },
)


class CreateProductRequest(proto.Message):
    r"""Request message for
    [ProductService.CreateProduct][google.cloud.retail.v2alpha.ProductService.CreateProduct]
    method.

    Attributes:
        parent (str):
            Required. The parent catalog resource name, such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch``.
        product (google.cloud.retail_v2alpha.types.Product):
            Required. The [Product][google.cloud.retail.v2alpha.Product]
            to create.
        product_id (str):
            Required. The ID to use for the
            [Product][google.cloud.retail.v2alpha.Product], which will
            become the final component of the
            [Product.name][google.cloud.retail.v2alpha.Product.name].

            If the caller does not have permission to create the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.

            This field must be unique among all
            [Product][google.cloud.retail.v2alpha.Product]s with the
            same
            [parent][google.cloud.retail.v2alpha.CreateProductRequest.parent].
            Otherwise, an ALREADY_EXISTS error is returned.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product: gcr_product.Product = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcr_product.Product,
    )
    product_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetProductRequest(proto.Message):
    r"""Request message for
    [ProductService.GetProduct][google.cloud.retail.v2alpha.ProductService.GetProduct]
    method.

    Attributes:
        name (str):
            Required. Full resource name of
            [Product][google.cloud.retail.v2alpha.Product], such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

            If the caller does not have permission to access the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.

            If the requested
            [Product][google.cloud.retail.v2alpha.Product] does not
            exist, a NOT_FOUND error is returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateProductRequest(proto.Message):
    r"""Request message for
    [ProductService.UpdateProduct][google.cloud.retail.v2alpha.ProductService.UpdateProduct]
    method.

    Attributes:
        product (google.cloud.retail_v2alpha.types.Product):
            Required. The product to update/create.

            If the caller does not have permission to update the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.

            If the [Product][google.cloud.retail.v2alpha.Product] to
            update does not exist and
            [allow_missing][google.cloud.retail.v2alpha.UpdateProductRequest.allow_missing]
            is not set, a NOT_FOUND error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [Product][google.cloud.retail.v2alpha.Product] to update.
            The immutable and output only fields are NOT supported. If
            not set, all supported fields (the fields that are neither
            immutable nor output only) are updated.

            If an unsupported or unknown field is provided, an
            INVALID_ARGUMENT error is returned.

            The attribute key can be updated by setting the mask path as
            "attributes.${key_name}". If a key name is present in the
            mask but not in the patching product from the request, this
            key will be deleted after the update.
        allow_missing (bool):
            If set to true, and the
            [Product][google.cloud.retail.v2alpha.Product] is not found,
            a new [Product][google.cloud.retail.v2alpha.Product] will be
            created. In this situation, ``update_mask`` is ignored.
    """

    product: gcr_product.Product = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_product.Product,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteProductRequest(proto.Message):
    r"""Request message for
    [ProductService.DeleteProduct][google.cloud.retail.v2alpha.ProductService.DeleteProduct]
    method.

    Attributes:
        name (str):
            Required. Full resource name of
            [Product][google.cloud.retail.v2alpha.Product], such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

            If the caller does not have permission to delete the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.

            If the [Product][google.cloud.retail.v2alpha.Product] to
            delete does not exist, a NOT_FOUND error is returned.

            The [Product][google.cloud.retail.v2alpha.Product] to delete
            can neither be a
            [Product.Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION]
            [Product][google.cloud.retail.v2alpha.Product] member nor a
            [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product] with more
            than one
            [variants][google.cloud.retail.v2alpha.Product.Type.VARIANT].
            Otherwise, an INVALID_ARGUMENT error is returned.

            All inventory information for the named
            [Product][google.cloud.retail.v2alpha.Product] will be
            deleted.
        force (bool):
            This value only applies to the case when the
            target product is of type PRIMARY.
            When deleting a product of VARIANT/COLLECTION
            type, this value will be ignored.
            When set to true, the subsequent variant
            products will be deleted.
            When set to false, if the primary product has
            active variant products, an error will be
            returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListProductsRequest(proto.Message):
    r"""Request message for
    [ProductService.ListProducts][google.cloud.retail.v2alpha.ProductService.ListProducts]
    method.

    Attributes:
        parent (str):
            Required. The parent branch resource name, such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/0``.
            Use ``default_branch`` as the branch ID, to list products
            under the default branch.

            If the caller does not have permission to list
            [Product][google.cloud.retail.v2alpha.Product]s under this
            branch, regardless of whether or not this branch exists, a
            PERMISSION_DENIED error is returned.
        page_size (int):
            Maximum number of
            [Product][google.cloud.retail.v2alpha.Product]s to return.
            If unspecified, defaults to 100. The maximum allowed value
            is 1000. Values above 1000 will be coerced to 1000.

            If this field is negative, an INVALID_ARGUMENT error is
            returned.
        page_token (str):
            A page token
            [ListProductsResponse.next_page_token][google.cloud.retail.v2alpha.ListProductsResponse.next_page_token],
            received from a previous
            [ProductService.ListProducts][google.cloud.retail.v2alpha.ProductService.ListProducts]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [ProductService.ListProducts][google.cloud.retail.v2alpha.ProductService.ListProducts]
            must match the call that provided the page token. Otherwise,
            an INVALID_ARGUMENT error is returned.
        filter (str):
            A filter to apply on the list results. Supported features:

            - List all the products under the parent branch if
              [filter][google.cloud.retail.v2alpha.ListProductsRequest.filter]
              is unset.
            - List
              [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
              [Product][google.cloud.retail.v2alpha.Product]s sharing
              the same
              [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
              [Product][google.cloud.retail.v2alpha.Product]. For
              example: ``primary_product_id = "some_product_id"``
            - List [Product][google.cloud.retail.v2alpha.Product]s
              bundled in a
              [Product.Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION]
              [Product][google.cloud.retail.v2alpha.Product]. For
              example: ``collection_product_id = "some_product_id"``
            - List [Product][google.cloud.retail.v2alpha.Product]s with
              a partibular type. For example: ``type = "PRIMARY"``
              ``type = "VARIANT"`` ``type = "COLLECTION"``

            If the field is unrecognizable, an INVALID_ARGUMENT error is
            returned.

            If the specified
            [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product] or
            [Product.Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION]
            [Product][google.cloud.retail.v2alpha.Product] does not
            exist, a NOT_FOUND error is returned.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields of [Product][google.cloud.retail.v2alpha.Product]
            to return in the responses. If not set or empty, the
            following fields are returned:

            - [Product.name][google.cloud.retail.v2alpha.Product.name]
            - [Product.id][google.cloud.retail.v2alpha.Product.id]
            - [Product.title][google.cloud.retail.v2alpha.Product.title]
            - [Product.uri][google.cloud.retail.v2alpha.Product.uri]
            - [Product.images][google.cloud.retail.v2alpha.Product.images]
            - [Product.price_info][google.cloud.retail.v2alpha.Product.price_info]
            - [Product.brands][google.cloud.retail.v2alpha.Product.brands]

            If "\*" is provided, all fields are returned.
            [Product.name][google.cloud.retail.v2alpha.Product.name] is
            always returned no matter what mask is set.

            If an unsupported or unknown field is provided, an
            INVALID_ARGUMENT error is returned.
        require_total_size (bool):
            If true and
            [page_token][google.cloud.retail.v2alpha.ListProductsRequest.page_token]
            is empty,
            [ListProductsResponse.total_size][google.cloud.retail.v2alpha.ListProductsResponse.total_size]
            is set to the total count of matched items irrespective of
            pagination.

            Notice that setting this field to true affects the
            performance.
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
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )
    require_total_size: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListProductsResponse(proto.Message):
    r"""Response message for
    [ProductService.ListProducts][google.cloud.retail.v2alpha.ProductService.ListProducts]
    method.

    Attributes:
        products (MutableSequence[google.cloud.retail_v2alpha.types.Product]):
            The [Product][google.cloud.retail.v2alpha.Product]s.
        next_page_token (str):
            A token that can be sent as
            [ListProductsRequest.page_token][google.cloud.retail.v2alpha.ListProductsRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages.
        total_size (int):
            The total count of matched
            [Product][google.cloud.retail.v2alpha.Product]s irrespective
            of pagination. The total number of
            [Product][google.cloud.retail.v2alpha.Product]s returned by
            pagination may be less than the
            [total_size][google.cloud.retail.v2alpha.ListProductsResponse.total_size]
            that matches.

            This field is ignored if
            [ListProductsRequest.require_total_size][google.cloud.retail.v2alpha.ListProductsRequest.require_total_size]
            is not set or
            [ListProductsRequest.page_token][google.cloud.retail.v2alpha.ListProductsRequest.page_token]
            is not empty.
    """

    @property
    def raw_page(self):
        return self

    products: MutableSequence[gcr_product.Product] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcr_product.Product,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class SetInventoryRequest(proto.Message):
    r"""Request message for
    [ProductService.SetInventory][google.cloud.retail.v2alpha.ProductService.SetInventory]
    method.

    Attributes:
        inventory (google.cloud.retail_v2alpha.types.Product):
            Required. The inventory information to update. The allowable
            fields to update are:

            - [Product.price_info][google.cloud.retail.v2alpha.Product.price_info]
            - [Product.availability][google.cloud.retail.v2alpha.Product.availability]
            - [Product.available_quantity][google.cloud.retail.v2alpha.Product.available_quantity]
            - [Product.fulfillment_info][google.cloud.retail.v2alpha.Product.fulfillment_info]
              The updated inventory fields must be specified in
              [SetInventoryRequest.set_mask][google.cloud.retail.v2alpha.SetInventoryRequest.set_mask].

            If
            [SetInventoryRequest.inventory.name][google.cloud.retail.v2alpha.Product.name]
            is empty or invalid, an INVALID_ARGUMENT error is returned.

            If the caller does not have permission to update the
            [Product][google.cloud.retail.v2alpha.Product] named in
            [Product.name][google.cloud.retail.v2alpha.Product.name],
            regardless of whether or not it exists, a PERMISSION_DENIED
            error is returned.

            If the [Product][google.cloud.retail.v2alpha.Product] to
            update does not have existing inventory information, the
            provided inventory information will be inserted.

            If the [Product][google.cloud.retail.v2alpha.Product] to
            update has existing inventory information, the provided
            inventory information will be merged while respecting the
            last update time for each inventory field, using the
            provided or default value for
            [SetInventoryRequest.set_time][google.cloud.retail.v2alpha.SetInventoryRequest.set_time].

            The caller can replace place IDs for a subset of fulfillment
            types in the following ways:

            - Adds "fulfillment_info" in
              [SetInventoryRequest.set_mask][google.cloud.retail.v2alpha.SetInventoryRequest.set_mask]
            - Specifies only the desired fulfillment types and
              corresponding place IDs to update in
              [SetInventoryRequest.inventory.fulfillment_info][google.cloud.retail.v2alpha.Product.fulfillment_info]

            The caller can clear all place IDs from a subset of
            fulfillment types in the following ways:

            - Adds "fulfillment_info" in
              [SetInventoryRequest.set_mask][google.cloud.retail.v2alpha.SetInventoryRequest.set_mask]
            - Specifies only the desired fulfillment types to clear in
              [SetInventoryRequest.inventory.fulfillment_info][google.cloud.retail.v2alpha.Product.fulfillment_info]
            - Checks that only the desired fulfillment info types have
              empty
              [SetInventoryRequest.inventory.fulfillment_info.place_ids][google.cloud.retail.v2alpha.FulfillmentInfo.place_ids]

            The last update time is recorded for the following inventory
            fields:

            - [Product.price_info][google.cloud.retail.v2alpha.Product.price_info]
            - [Product.availability][google.cloud.retail.v2alpha.Product.availability]
            - [Product.available_quantity][google.cloud.retail.v2alpha.Product.available_quantity]
            - [Product.fulfillment_info][google.cloud.retail.v2alpha.Product.fulfillment_info]

            If a full overwrite of inventory information while ignoring
            timestamps is needed,
            [ProductService.UpdateProduct][google.cloud.retail.v2alpha.ProductService.UpdateProduct]
            should be invoked instead.
        set_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which inventory fields in the provided
            [Product][google.cloud.retail.v2alpha.Product] to update.

            At least one field must be provided.

            If an unsupported or unknown field is provided, an
            INVALID_ARGUMENT error is returned and the entire update
            will be ignored.
        set_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the request is issued, used to
            prevent out-of-order updates on inventory fields
            with the last update time recorded. If not
            provided, the internal system time will be used.
        allow_missing (bool):
            If set to true, and the
            [Product][google.cloud.retail.v2alpha.Product] with name
            [Product.name][google.cloud.retail.v2alpha.Product.name] is
            not found, the inventory update will still be processed and
            retained for at most 1 day until the
            [Product][google.cloud.retail.v2alpha.Product] is created.
            If set to false, a NOT_FOUND error is returned if the
            [Product][google.cloud.retail.v2alpha.Product] is not found.
    """

    inventory: gcr_product.Product = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_product.Product,
    )
    set_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    set_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class SetInventoryMetadata(proto.Message):
    r"""Metadata related to the progress of the SetInventory operation.
    Currently empty because there is no meaningful metadata populated
    from the
    [ProductService.SetInventory][google.cloud.retail.v2alpha.ProductService.SetInventory]
    method.

    """


class SetInventoryResponse(proto.Message):
    r"""Response of the SetInventoryRequest. Currently empty because there
    is no meaningful response populated from the
    [ProductService.SetInventory][google.cloud.retail.v2alpha.ProductService.SetInventory]
    method.

    """


class AddFulfillmentPlacesRequest(proto.Message):
    r"""Request message for
    [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces]
    method.

    Attributes:
        product (str):
            Required. Full resource name of
            [Product][google.cloud.retail.v2alpha.Product], such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

            If the caller does not have permission to access the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.
        type_ (str):
            Required. The fulfillment type, including commonly used
            types (such as pickup in store and same day delivery), and
            custom types.

            Supported values:

            - "pickup-in-store"
            - "ship-to-store"
            - "same-day-delivery"
            - "next-day-delivery"
            - "custom-type-1"
            - "custom-type-2"
            - "custom-type-3"
            - "custom-type-4"
            - "custom-type-5"

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.

            This field directly corresponds to
            [Product.fulfillment_info.type][google.cloud.retail.v2alpha.FulfillmentInfo.type].
        place_ids (MutableSequence[str]):
            Required. The IDs for this
            [type][google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type],
            such as the store IDs for "pickup-in-store" or the region
            IDs for "same-day-delivery" to be added for this
            [type][google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type].
            Duplicate IDs will be automatically ignored.

            At least 1 value is required, and a maximum of 2000 values
            are allowed. Each value must be a string with a length limit
            of 10 characters, matching the pattern ``[a-zA-Z0-9_-]+``,
            such as "store1" or "REGION-2". Otherwise, an
            INVALID_ARGUMENT error is returned.

            If the total number of place IDs exceeds 2000 for this
            [type][google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type]
            after adding, then the update will be rejected.
        add_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the fulfillment updates are
            issued, used to prevent out-of-order updates on
            fulfillment information. If not provided, the
            internal system time will be used.
        allow_missing (bool):
            If set to true, and the
            [Product][google.cloud.retail.v2alpha.Product] is not found,
            the fulfillment information will still be processed and
            retained for at most 1 day and processed once the
            [Product][google.cloud.retail.v2alpha.Product] is created.
            If set to false, a NOT_FOUND error is returned if the
            [Product][google.cloud.retail.v2alpha.Product] is not found.
    """

    product: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    place_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    add_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class AddFulfillmentPlacesMetadata(proto.Message):
    r"""Metadata related to the progress of the AddFulfillmentPlaces
    operation. Currently empty because there is no meaningful metadata
    populated from the
    [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces]
    method.

    """


class AddFulfillmentPlacesResponse(proto.Message):
    r"""Response of the AddFulfillmentPlacesRequest. Currently empty because
    there is no meaningful response populated from the
    [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces]
    method.

    """


class AddLocalInventoriesRequest(proto.Message):
    r"""Request message for
    [ProductService.AddLocalInventories][google.cloud.retail.v2alpha.ProductService.AddLocalInventories]
    method.

    Attributes:
        product (str):
            Required. Full resource name of
            [Product][google.cloud.retail.v2alpha.Product], such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

            If the caller does not have permission to access the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.
        local_inventories (MutableSequence[google.cloud.retail_v2alpha.types.LocalInventory]):
            Required. A list of inventory information at
            difference places. Each place is identified by
            its place ID. At most 3000 inventories are
            allowed per request.
        add_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which inventory fields in the provided list of
            [LocalInventory][google.cloud.retail.v2alpha.LocalInventory]
            to update. The field is updated to the provided value.

            If a field is set while the place does not have a previous
            local inventory, the local inventory at that store is
            created.

            If a field is set while the value of that field is not
            provided, the original field value, if it exists, is
            deleted.

            If the mask is not set or set with empty paths, all
            inventory fields will be updated.

            If an unsupported or unknown field is provided, an
            INVALID_ARGUMENT error is returned and the entire update
            will be ignored.
        add_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the inventory updates are
            issued. Used to prevent out-of-order updates on
            local inventory fields. If not provided, the
            internal system time will be used.
        allow_missing (bool):
            If set to true, and the
            [Product][google.cloud.retail.v2alpha.Product] is not found,
            the local inventory will still be processed and retained for
            at most 1 day and processed once the
            [Product][google.cloud.retail.v2alpha.Product] is created.
            If set to false, a NOT_FOUND error is returned if the
            [Product][google.cloud.retail.v2alpha.Product] is not found.
    """

    product: str = proto.Field(
        proto.STRING,
        number=1,
    )
    local_inventories: MutableSequence[common.LocalInventory] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=common.LocalInventory,
    )
    add_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    add_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class AddLocalInventoriesMetadata(proto.Message):
    r"""Metadata related to the progress of the AddLocalInventories
    operation. Currently empty because there is no meaningful metadata
    populated from the
    [ProductService.AddLocalInventories][google.cloud.retail.v2alpha.ProductService.AddLocalInventories]
    method.

    """


class AddLocalInventoriesResponse(proto.Message):
    r"""Response of the
    [ProductService.AddLocalInventories][google.cloud.retail.v2alpha.ProductService.AddLocalInventories]
    API. Currently empty because there is no meaningful response
    populated from the
    [ProductService.AddLocalInventories][google.cloud.retail.v2alpha.ProductService.AddLocalInventories]
    method.

    """


class RemoveLocalInventoriesRequest(proto.Message):
    r"""Request message for
    [ProductService.RemoveLocalInventories][google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories]
    method.

    Attributes:
        product (str):
            Required. Full resource name of
            [Product][google.cloud.retail.v2alpha.Product], such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

            If the caller does not have permission to access the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.
        place_ids (MutableSequence[str]):
            Required. A list of place IDs to have their
            inventory deleted. At most 3000 place IDs are
            allowed per request.
        remove_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the inventory deletions are
            issued. Used to prevent out-of-order updates and
            deletions on local inventory fields. If not
            provided, the internal system time will be used.
        allow_missing (bool):
            If set to true, and the
            [Product][google.cloud.retail.v2alpha.Product] is not found,
            the local inventory removal request will still be processed
            and retained for at most 1 day and processed once the
            [Product][google.cloud.retail.v2alpha.Product] is created.
            If set to false, a NOT_FOUND error is returned if the
            [Product][google.cloud.retail.v2alpha.Product] is not found.
    """

    product: str = proto.Field(
        proto.STRING,
        number=1,
    )
    place_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    remove_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class RemoveLocalInventoriesMetadata(proto.Message):
    r"""Metadata related to the progress of the RemoveLocalInventories
    operation. Currently empty because there is no meaningful metadata
    populated from the
    [ProductService.RemoveLocalInventories][google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories]
    method.

    """


class RemoveLocalInventoriesResponse(proto.Message):
    r"""Response of the
    [ProductService.RemoveLocalInventories][google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories]
    API. Currently empty because there is no meaningful response
    populated from the
    [ProductService.RemoveLocalInventories][google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories]
    method.

    """


class RemoveFulfillmentPlacesRequest(proto.Message):
    r"""Request message for
    [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces]
    method.

    Attributes:
        product (str):
            Required. Full resource name of
            [Product][google.cloud.retail.v2alpha.Product], such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

            If the caller does not have permission to access the
            [Product][google.cloud.retail.v2alpha.Product], regardless
            of whether or not it exists, a PERMISSION_DENIED error is
            returned.
        type_ (str):
            Required. The fulfillment type, including commonly used
            types (such as pickup in store and same day delivery), and
            custom types.

            Supported values:

            - "pickup-in-store"
            - "ship-to-store"
            - "same-day-delivery"
            - "next-day-delivery"
            - "custom-type-1"
            - "custom-type-2"
            - "custom-type-3"
            - "custom-type-4"
            - "custom-type-5"

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.

            This field directly corresponds to
            [Product.fulfillment_info.type][google.cloud.retail.v2alpha.FulfillmentInfo.type].
        place_ids (MutableSequence[str]):
            Required. The IDs for this
            [type][google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest.type],
            such as the store IDs for "pickup-in-store" or the region
            IDs for "same-day-delivery", to be removed for this
            [type][google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest.type].

            At least 1 value is required, and a maximum of 2000 values
            are allowed. Each value must be a string with a length limit
            of 10 characters, matching the pattern ``[a-zA-Z0-9_-]+``,
            such as "store1" or "REGION-2". Otherwise, an
            INVALID_ARGUMENT error is returned.
        remove_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the fulfillment updates are
            issued, used to prevent out-of-order updates on
            fulfillment information. If not provided, the
            internal system time will be used.
        allow_missing (bool):
            If set to true, and the
            [Product][google.cloud.retail.v2alpha.Product] is not found,
            the fulfillment information will still be processed and
            retained for at most 1 day and processed once the
            [Product][google.cloud.retail.v2alpha.Product] is created.
            If set to false, a NOT_FOUND error is returned if the
            [Product][google.cloud.retail.v2alpha.Product] is not found.
    """

    product: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    place_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    remove_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class RemoveFulfillmentPlacesMetadata(proto.Message):
    r"""Metadata related to the progress of the RemoveFulfillmentPlaces
    operation. Currently empty because there is no meaningful metadata
    populated from the
    [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces]
    method.

    """


class RemoveFulfillmentPlacesResponse(proto.Message):
    r"""Response of the RemoveFulfillmentPlacesRequest. Currently empty
    because there is no meaningful response populated from the
    [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces]
    method.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
