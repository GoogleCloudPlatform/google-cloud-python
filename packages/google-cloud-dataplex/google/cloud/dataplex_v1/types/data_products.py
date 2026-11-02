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

from google.cloud.dataplex_v1.types import approval_workflow

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "DataProduct",
        "DataAsset",
        "CreateDataProductRequest",
        "DeleteDataProductRequest",
        "GetDataProductRequest",
        "ListDataProductsRequest",
        "ListDataProductsResponse",
        "UpdateDataProductRequest",
        "RequestDataProductAccessRequest",
        "RequestDataProductAccessResponse",
        "CreateDataAssetRequest",
        "UpdateDataAssetRequest",
        "DeleteDataAssetRequest",
        "GetDataAssetRequest",
        "ListDataAssetsRequest",
        "ListDataAssetsResponse",
    },
)


class DataProduct(proto.Message):
    r"""A data product is a curated collection of data assets,
    packaged to address specific use cases. It's a way to manage and
    share data in a more organized, product-like manner.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the data product. Format:
            ``projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}``.
        uid (str):
            Output only. System generated unique ID for
            the data product. This ID will be different if
            the data product is deleted and re-created with
            the same name.
        display_name (str):
            Required. User-friendly display name of the
            data product.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data
            product was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data
            product was last updated.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the data product.

            Example:

            ::

               {
                 "environment": "production",
                 "billing": "marketing-department"
               }
        description (str):
            Optional. Description of the data product.
        icon (bytes):
            Optional. Base64 encoded image representing
            the data product. Max Size: 3.0MiB Expected
            image dimensions are 512x512 pixels, however the
            API only performs validation on size of the
            encoded data. Note: For byte fields, the content
            of the fields are base64-encoded (which
            increases the size of the data by 33-36%) when
            using JSON on the wire.
        owner_emails (MutableSequence[str]):
            Required. Emails of the data product owners.
        asset_count (int):
            Output only. Number of data assets associated
            with this data product.
        access_groups (MutableMapping[str, google.cloud.dataplex_v1.types.DataProduct.AccessGroup]):
            Optional. Data product access groups by access group id as
            key. If data product is used only for packaging data assets,
            then access groups may be empty. However, if a data product
            is used for sharing data assets, then at least one access
            group must be specified.

            Example:

            ::

               {
                 "analyst": {
                   "id": "analyst",
                   "displayName": "Analyst",
                   "description": "Access group for analysts",
                   "principal": {
                     "googleGroup": "analysts@example.com"
                   }
                 }
               }
        access_approval_config (google.cloud.dataplex_v1.types.DataProduct.AccessApprovalConfig):
            Optional. Configuration for access approval
            for the data product.

            This field is a member of `oneof`_ ``_access_approval_config``.
    """

    class Principal(proto.Message):
        r"""Represents the principal entity associated with an access
        group, as per
        https://cloud.google.com/iam/docs/principals-overview.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            google_group (str):
                Optional. Email of the Google Group, as per
                https://cloud.google.com/iam/docs/principals-overview#google-group.

                This field is a member of `oneof`_ ``type``.
            service_account (str):
                Optional. Specifies the email of the producer
                service account, as per
                https://cloud.google.com/iam/docs/principals-overview#service-account.

                This field is a member of `oneof`_ ``_service_account``.
        """

        google_group: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="type",
        )
        service_account: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    class AccessGroup(proto.Message):
        r"""Custom user defined access groups at the data product level.
        These are used for granting different levels of access (IAM
        roles) on the individual data product's data assets.

        Attributes:
            id (str):
                Required. Unique identifier of the access
                group within the data product. User defined. Eg.
                "analyst", "developer", etc.
            display_name (str):
                Required. User friendly display name of the
                access group. Eg. "Analyst", "Developer", etc.
            description (str):
                Optional. Description of the access group.
            principal (google.cloud.dataplex_v1.types.DataProduct.Principal):
                Required. The principal entity associated
                with this access group.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        description: str = proto.Field(
            proto.STRING,
            number=3,
        )
        principal: "DataProduct.Principal" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="DataProduct.Principal",
        )

    class AccessApprovalConfig(proto.Message):
        r"""Configuration for access approval for the data product.

        Attributes:
            approver_emails (MutableSequence[str]):
                Optional. Specifies the email addresses of
                users who are potential approvers and are
                notified when an access request is made for the
                data product. The maximum number of emails
                allowed is 10.
        """

        approver_emails: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    icon: bytes = proto.Field(
        proto.BYTES,
        number=10,
    )
    owner_emails: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    asset_count: int = proto.Field(
        proto.INT32,
        number=13,
    )
    access_groups: MutableMapping[str, AccessGroup] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=14,
        message=AccessGroup,
    )
    access_approval_config: AccessApprovalConfig = proto.Field(
        proto.MESSAGE,
        number=15,
        optional=True,
        message=AccessApprovalConfig,
    )


class DataAsset(proto.Message):
    r"""Represents a data asset resource that can be packaged and
    shared via a data product.

    Attributes:
        name (str):
            Identifier. Resource name of the data asset. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}
        uid (str):
            Output only. System generated globally unique
            ID for the data asset. This ID will be different
            if the data asset is deleted and re-created with
            the same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data asset
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data asset
            was last updated.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the data asset.

            Example:

            ::

               {
                 "environment": "production",
                 "billing": "marketing-department"
               }
        resource (str):
            Required. Immutable. Full resource name of the cloud
            resource represented by the data asset. This must follow
            https://cloud.google.com/iam/docs/full-resource-names.
            Example:
            ``//bigquery.googleapis.com/projects/my_project_123/datasets/dataset_456/tables/table_789``
            Only BigQuery tables and datasets are currently supported.
            Data asset creator must have getIamPolicy and setIamPolicy
            permissions on the resource. Data asset creator must also
            have resource specific get permission, for instance,
            bigquery.tables.get for BigQuery tables.
        access_group_configs (MutableMapping[str, google.cloud.dataplex_v1.types.DataAsset.AccessGroupConfig]):
            Optional. Access groups configurations for this data asset.

            The key is ``DataProduct.AccessGroup.id`` and the value is
            ``AccessGroupConfig``.

            Example:

            ::

                {
                  "analyst": {
                    "iamRoles": ["roles/bigquery.dataViewer"]
                  }
                }

            Currently, at most one IAM role is allowed per access group.
            For providing multiple predefined IAM roles, wrap them in a
            custom IAM role as per
            https://cloud.google.com/iam/docs/creating-custom-roles.
    """

    class AccessGroupConfig(proto.Message):
        r"""Configuration for access group inherited from the parent data
        product.

        Attributes:
            iam_roles (MutableSequence[str]):
                Optional. IAM roles granted on the resource to this access
                group. Role name follows
                https://cloud.google.com/iam/docs/reference/rest/v1/roles.

                Example: ``[ "roles/bigquery.dataViewer" ]``
        """

        iam_roles: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=7,
    )
    access_group_configs: MutableMapping[str, AccessGroupConfig] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=9,
        message=AccessGroupConfig,
    )


class CreateDataProductRequest(proto.Message):
    r"""Request message for creating a data product.

    Attributes:
        parent (str):
            Required. The parent resource where this data product will
            be created. Format:
            projects/{project_id_or_number}/locations/{location_id}
        data_product_id (str):
            Optional. The ID of the data product to create.

            The ID must conform to RFC-1034 and contain only lower-case
            letters (a-z), numbers (0-9), or hyphens, with the first
            character a letter, the last a letter or a number, and a 63
            character maximum. Characters outside of ASCII are not
            permitted. Valid format regex:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`` If not provided, a
            system generated ID will be used.
        data_product (google.cloud.dataplex_v1.types.DataProduct):
            Required. The data product to create.
        validate_only (bool):
            Optional. Validates the request without
            actually creating the data product. Default:
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_product_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_product: "DataProduct" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataProduct",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteDataProductRequest(proto.Message):
    r"""Request message for deleting a data product.

    Attributes:
        name (str):
            Required. The name of the data product to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}
        etag (str):
            Optional. The etag of the data product.

            If an etag is provided and does not match the
            current etag of the data product, then the
            deletion will be blocked and an ABORTED error
            will be returned.
        validate_only (bool):
            Optional. Validates the request without
            actually deleting the data product. Default:
            false.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetDataProductRequest(proto.Message):
    r"""Request message for getting a data product.

    Attributes:
        name (str):
            Required. The name of the data product to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataProductsRequest(proto.Message):
    r"""Request message for listing data products.

    Attributes:
        parent (str):
            Required. The parent, which has this collection of data
            products.

            Format:
            ``projects/{project_id_or_number}/locations/{location_id}``.

            Supports listing across all locations with the wildcard
            ``-`` (hyphen) character. Example:
            ``projects/{project_id_or_number}/locations/-``
        filter (str):
            Optional. Filter expression that filters data products
            listed in the response.

            Example of using this filter is:
            ``display_name="my-data-product"``
        page_size (int):
            Optional. The maximum number of data products
            to return. The service may return fewer than
            this value. If unspecified, at most 50 data
            products will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDataProducts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDataProducts`` must match the call that provided the
            page token.
        order_by (str):
            Optional. Order by expression that orders data products
            listed in the response.

            Supported Order by fields are: ``name`` or ``create_time``.

            If not specified, the ordering is undefined.

            Ordering by ``create_time`` is not supported when listing
            resources across locations (i.e. when request contains
            ``/locations/-``).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDataProductsResponse(proto.Message):
    r"""Response message for listing data products.

    Attributes:
        data_products (MutableSequence[google.cloud.dataplex_v1.types.DataProduct]):
            The data products for the requested filter
            criteria.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is empty, then there are no
            subsequent pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that the service
            couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    data_products: MutableSequence["DataProduct"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataProduct",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateDataProductRequest(proto.Message):
    r"""Request message for updating a data product.

    Attributes:
        data_product (google.cloud.dataplex_v1.types.DataProduct):
            Required. The data product to update. The data product's
            ``name`` field is used to identify the data product to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
            If this is empty or not set, then all the fields
            will be updated.
        validate_only (bool):
            Optional. Validates the request without
            actually updating the data product. Default:
            false.
    """

    data_product: "DataProduct" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataProduct",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class RequestDataProductAccessRequest(proto.Message):
    r"""Message for requesting access to a Data Product.

    Attributes:
        parent (str):
            Required. The resource name of the data product. Format:
            projects/{project_number}/locations/{location_id}/dataProducts/{data_product_id}
        change_request (google.cloud.dataplex_v1.types.ChangeRequest):
            Required. The change request for the data
            product access request.
        validate_only (bool):
            Optional. Validates the request without
            actually creating the access change request.
            Defaults to false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    change_request: approval_workflow.ChangeRequest = proto.Field(
        proto.MESSAGE,
        number=2,
        message=approval_workflow.ChangeRequest,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class RequestDataProductAccessResponse(proto.Message):
    r"""Response message for requesting access to a Data Product.

    Attributes:
        change_request_name (str):
            The resource name of the created ChangeRequest. Format:
            projects/{project_number}/locations/{location_id}/changeRequests/{change_request_id}
    """

    change_request_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDataAssetRequest(proto.Message):
    r"""Request message for creating a data asset.

    Attributes:
        parent (str):
            Required. The parent resource where this data asset will be
            created. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}
        data_asset_id (str):
            Optional. The ID of the data asset to create.

            The ID must conform to RFC-1034 and contain only lower-case
            letters (a-z), numbers (0-9), or hyphens, with the first
            character a letter, the last a letter or a number, and a 63
            character maximum. Characters outside of ASCII are not
            permitted. Valid format regex:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`` If not provided, a
            system generated ID will be used.
        data_asset (google.cloud.dataplex_v1.types.DataAsset):
            Required. The data asset to create.
        validate_only (bool):
            Optional. Validates the request without
            actually creating the data asset. Defaults to
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_asset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_asset: "DataAsset" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataAsset",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateDataAssetRequest(proto.Message):
    r"""Request message for updating a data asset.

    Attributes:
        data_asset (google.cloud.dataplex_v1.types.DataAsset):
            Required. The data asset to update. The data asset's
            ``name`` field is used to identify the data asset to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
            If this is empty or not set, then all the fields
            will be updated.
        validate_only (bool):
            Optional. Validates the request without
            actually updating the data asset. Defaults to
            false.
    """

    data_asset: "DataAsset" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataAsset",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteDataAssetRequest(proto.Message):
    r"""Request message for deleting a data asset.

    Attributes:
        name (str):
            Required. The name of the data asset to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}
        etag (str):
            Optional. The etag of the data asset.
            If this is provided, it must match the server's
            etag. If the etag is provided and does not match
            the server-computed etag, the request must fail
            with a ABORTED error code.
        validate_only (bool):
            Optional. Validates the request without
            actually deleting the data asset. Defaults to
            false.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetDataAssetRequest(proto.Message):
    r"""Request message for getting a data asset.

    Attributes:
        name (str):
            Required. The name of the data asset to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataAssetsRequest(proto.Message):
    r"""Request message for listing data assets.

    Attributes:
        parent (str):
            Required. The parent, which has this collection of data
            assets. Format:
            projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}
        filter (str):
            Optional. Filter expression that filters data
            assets listed in the response.
        order_by (str):
            Optional. Order by expression that orders data assets listed
            in the response.

            Supported ``order_by`` fields are: ``name`` or
            ``create_time``.

            If not specified, the ordering is undefined.
        page_size (int):
            Optional. The maximum number of data assets
            to return. The service may return fewer than
            this value. If unspecified, at most 50 data
            assets will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDataAssets`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDataAssets`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDataAssetsResponse(proto.Message):
    r"""Response message for listing data assets.

    Attributes:
        data_assets (MutableSequence[google.cloud.dataplex_v1.types.DataAsset]):
            The data assets for the requested filter
            criteria.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is empty, then there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    data_assets: MutableSequence["DataAsset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataAsset",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
