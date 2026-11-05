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

__protobuf__ = proto.module(
    package="google.cloud.observability.v1",
    manifest={
        "CmekSettings",
        "Settings",
        "Bucket",
        "CreateBucketRequest",
        "UpdateBucketRequest",
        "GetBucketRequest",
        "ListBucketsRequest",
        "ListBucketsResponse",
        "Dataset",
        "GetDatasetRequest",
        "ListDatasetsRequest",
        "ListDatasetsResponse",
        "View",
        "GetViewRequest",
        "ListViewsRequest",
        "ListViewsResponse",
        "Link",
        "CreateLinkRequest",
        "UpdateLinkRequest",
        "GetLinkRequest",
        "ListLinksRequest",
        "ListLinksResponse",
        "DeleteLinkRequest",
        "Scope",
        "GetScopeRequest",
        "UpdateScopeRequest",
        "OperationMetadata",
        "TraceScope",
        "CreateTraceScopeRequest",
        "GetTraceScopeRequest",
        "ListTraceScopesRequest",
        "ListTraceScopesResponse",
        "UpdateTraceScopeRequest",
        "DeleteTraceScopeRequest",
        "GetSettingsRequest",
        "UpdateSettingsRequest",
    },
)


class CmekSettings(proto.Message):
    r"""Settings for configuring CMEK for a bucket.

    Attributes:
        kms_key (str):
            Optional. The resource name for the configured Cloud KMS
            key. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]

            For example:

            ::

                projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key
        kms_key_version (str):
            Output only. The CryptoKeyVersion resource name for the
            configured Cloud KMS key. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]/cryptoKeyVersions/[VERSION]

            For example:

            ::

                projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key/cryptoKeyVersions/1

            This read-only field is used to convey the specific
            configured CryptoKeyVersion of the ``kms_key`` that has been
            configured. It is populated when the CMEK settings are bound
            to a single key version.
        service_account_id (str):
            Output only. The service account used to
            access the key.
    """

    kms_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Settings(proto.Message):
    r"""Describes the settings associated with a project,
    organization, or folder.

    Attributes:
        name (str):
            Identifier. The resource name of the
            settings.
        default_storage_location (str):
            Optional. The location which should be used
            when any regional resources are provisioned by
            Google Cloud.
        service_account_id (str):
            Output only. The service account for the
            given resource container, such as project or
            folder. This will be used by Cloud Observability
            to perform actions in the container's project
            like access KMS keys or create Links. Always the
            same service account per resource container
            regardless of region.
        kms_key_name (str):
            Optional. The resource name for the configured Cloud KMS
            key.

            KMS key name format:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]"

            For example:

            ``"projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key"``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_storage_location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Bucket(proto.Message):
    r"""Bucket configuration for storing observability data.

    Attributes:
        name (str):
            Identifier. Name of the bucket. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]
        display_name (str):
            Optional. User friendly display name.
        description (str):
            Optional. Description of the bucket.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Delete timestamp.
        purge_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the bucket in
            soft-deleted state is purged.
        cmek_settings (google.cloud.observability_v1.types.CmekSettings):
            Optional. Settings for configuring CMEK on a
            bucket.
    """

    name: str = proto.Field(
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
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    purge_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    cmek_settings: "CmekSettings" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="CmekSettings",
    )


class CreateBucketRequest(proto.Message):
    r"""Request for creating a bucket.

    Attributes:
        parent (str):
            Required. Name of the project and location for the bucket.
            The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]
        bucket_id (str):
            Required. Id of the bucket to create.
        bucket (google.cloud.observability_v1.types.Bucket):
            Required. Bucket to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    bucket: "Bucket" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Bucket",
    )


class UpdateBucketRequest(proto.Message):
    r"""Request for updating a bucket.

    Attributes:
        bucket (google.cloud.observability_v1.types.Bucket):
            Required. The  bucket to update.

            The name field of bucket identifies the resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    bucket: "Bucket" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Bucket",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetBucketRequest(proto.Message):
    r"""Request for getting a bucket.

    Attributes:
        name (str):
            Required. Name of the bucket to retrieve. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBucketsRequest(proto.Message):
    r"""Request for listing buckets.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of buckets.
            The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]
        page_size (int):
            Optional. The maximum number of buckets to
            return. If unspecified, then at most 100 buckets
            are returned. The maximum value is 1000; values
            above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListBuckets`` call. Provide this to retrieve the
            subsequent page.
        show_deleted (bool):
            Optional. If true, then the response will
            include deleted buckets.
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
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListBucketsResponse(proto.Message):
    r"""Response for listing buckets.

    Attributes:
        buckets (MutableSequence[google.cloud.observability_v1.types.Bucket]):
            Optional. The list of buckets.
        next_page_token (str):
            Optional. A token that can be sent as ``page_token`` to
            retrieve the next page. When this field is omitted, there
            are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    buckets: MutableSequence["Bucket"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Bucket",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Dataset(proto.Message):
    r"""A dataset is a collection of data that has a specific
    configuration. A dataset can be backed by multiple tables. One
    bucket can have multiple datasets.

    Attributes:
        name (str):
            Identifier. Name of the dataset. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]
        display_name (str):
            Optional. User friendly display name.
        description (str):
            Optional. Description of the dataset.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Delete timestamp.
        purge_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the dataset in
            soft-deleted state is purged.
    """

    name: str = proto.Field(
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
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    purge_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class GetDatasetRequest(proto.Message):
    r"""Request for getting a dataset.

    Attributes:
        name (str):
            Required. Name of the dataset to retrieve. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDatasetsRequest(proto.Message):
    r"""Request for listing datasets.

    Attributes:
        parent (str):
            Required. The parent bucket that owns this collection of
            datasets. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]
        page_size (int):
            Optional. The maximum number of datasets to
            return. If unspecified, then at most 100
            datasets are returned. The maximum value is
            1000; values above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDatasets`` call. Provide this to retrieve the
            subsequent page.
        show_deleted (bool):
            Optional. If true, then the response will
            include deleted datasets.
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
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListDatasetsResponse(proto.Message):
    r"""Response for listing datasets.

    Attributes:
        datasets (MutableSequence[google.cloud.observability_v1.types.Dataset]):
            The list of datasets.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. When this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    datasets: MutableSequence["Dataset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Dataset",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class View(proto.Message):
    r"""A view corresponds to a read-only representation of a subset
    of the data in a dataset.

    Attributes:
        name (str):
            Identifier. Name of the view. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]/views/[VIEW_ID]
        display_name (str):
            Optional. User friendly display name.
        description (str):
            Optional. Description of the view.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
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


class GetViewRequest(proto.Message):
    r"""Request for getting a view.

    Attributes:
        name (str):
            Required. Name of the view to retrieve. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]/views/[VIEW_ID]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListViewsRequest(proto.Message):
    r"""Request for listing views.

    Attributes:
        parent (str):
            Required. Dataset whose views are to be listed. The format
            is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]
        page_size (int):
            Optional. The maximum number of views to
            return. If unspecified, then at most 100 views
            are returned. The maximum value is 1000; values
            above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListViews`` call. Provide this to retrieve the subsequent
            page.
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


class ListViewsResponse(proto.Message):
    r"""Response for listing views.

    Attributes:
        views (MutableSequence[google.cloud.observability_v1.types.View]):
            The list of views.
        next_page_token (str):
            Optional. A token that can be sent as ``page_token`` to
            retrieve the next page. When this field is omitted, there
            are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    views: MutableSequence["View"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="View",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Link(proto.Message):
    r"""A link lets a dataset be accessible to BigQuery via usage of
    linked datasets.

    Attributes:
        name (str):
            Identifier. Name of the link. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]/links/[LINK_ID]
        display_name (str):
            Optional. A user friendly display name.
        description (str):
            Optional. Description of the link.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
    """

    name: str = proto.Field(
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
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class CreateLinkRequest(proto.Message):
    r"""Request for creating a link.

    Attributes:
        parent (str):
            Required. Name of the containing dataset for this link. The
            format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]
        link_id (str):
            Required. Id of the link to create.
        link (google.cloud.observability_v1.types.Link):
            Required. Link to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    link_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    link: "Link" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Link",
    )


class UpdateLinkRequest(proto.Message):
    r"""Request for updating a link.

    Attributes:
        link (google.cloud.observability_v1.types.Link):
            Required. Link to update.

            The name field of link identifies the resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    link: "Link" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Link",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetLinkRequest(proto.Message):
    r"""Request for getting a link.

    Attributes:
        name (str):
            Required. Name of the link to retrieve. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]/links/[LINK_ID]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLinksRequest(proto.Message):
    r"""Request for listing links.

    Attributes:
        parent (str):
            Required. The parent dataset that owns this collection of
            links. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]
        page_size (int):
            Optional. The maximum number of links to
            return. If unspecified, then at most 100 links
            are returned. The maximum value is 1000; values
            above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLinks`` call. Provide this to retrieve the subsequent
            page.
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


class ListLinksResponse(proto.Message):
    r"""Response for listing links.

    Attributes:
        links (MutableSequence[google.cloud.observability_v1.types.Link]):
            The list of links.
        next_page_token (str):
            Optional. A token that can be sent as ``page_token`` to
            retrieve the next page. When this field is omitted, there
            are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    links: MutableSequence["Link"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Link",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteLinkRequest(proto.Message):
    r"""Request for deleting a link.

    Attributes:
        name (str):
            Required. Name of the link to delete. The format is:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_ID]/datasets/[DATASET_ID]/links/[LINK_ID]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Scope(proto.Message):
    r"""Message describing Scope object

    Attributes:
        name (str):
            Identifier. Name of the resource. The format is:

            ::

                projects/{project}/locations/{location}/scopes/{scope}

            The ``{location}`` field must be set to ``global``. The
            ``{scope}`` field must be set to ``_Default``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
            Note: The Update timestamp for the default scope
            is initially unset.
        log_scope (str):
            Required. The full resource name of the
            ``logging.googleapis.com/LogScope``. For example:

            ::

                //logging.googleapis.com/projects/myproject/locations/global/logScopes/my-log-scope
        trace_scope (str):
            Required. The unqualified resource name of the
            ``cloudtrace.googleapis.com/TraceScope``. For example:

            ::

                projects/myproject/locations/global/traceScopes/my-trace-scope
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    log_scope: str = proto.Field(
        proto.STRING,
        number=5,
    )
    trace_scope: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GetScopeRequest(proto.Message):
    r"""Message for getting a Scope.

    Attributes:
        name (str):
            Required. Name of the resource. The format is:

            ::

                projects/{project}/locations/{location}/scopes/{scope}

            The ``{location}`` field must be set to ``global``. The
            ``{scope}`` field must be set to ``_Default``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateScopeRequest(proto.Message):
    r"""Message for updating a Scope.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Scope resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field is overwritten when it is in
            the mask. If the user does not provide a mask, then all
            fields present in the request are overwritten.
        scope (google.cloud.observability_v1.types.Scope):
            Required. The resource being updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    scope: "Scope" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Scope",
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class TraceScope(proto.Message):
    r"""A trace scope is a collection of resources whose traces are
    queried together.

    Attributes:
        name (str):
            Identifier. The resource name of the trace
            scope.
            For example:

            projects/my-project/locations/global/traceScopes/my-trace-scope
        resource_names (MutableSequence[str]):
            Required. Names of the projects that are included in this
            trace scope.

            - ``projects/[PROJECT_ID]``

            A trace scope can include a maximum of 20 projects.
        description (str):
            Optional. Describes this trace scope.

            The maximum length of the description is 8000
            characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            trace scope.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            trace scope.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
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


class CreateTraceScopeRequest(proto.Message):
    r"""Request for creating a TraceScope.

    Attributes:
        parent (str):
            Required. The full resource name of the location where the
            trace scope should be created

            ::

                projects/[PROJECT_ID]/locations/[LOCATION_ID]

            For example:

            ::

                projects/my-project/locations/global
        trace_scope_id (str):
            Required. A client-assigned identifier for
            the trace scope.
        trace_scope (google.cloud.observability_v1.types.TraceScope):
            Required. The new trace scope.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trace_scope_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trace_scope: "TraceScope" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TraceScope",
    )


class GetTraceScopeRequest(proto.Message):
    r"""Request for getting a TraceScope.

    Attributes:
        name (str):
            Required. The resource name of the trace scope:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION_ID]/traceScopes/[TRACE_SCOPE_ID]

            For example:

            ::

                projects/my-project/locations/global/traceScopes/my-trace-scope
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTraceScopesRequest(proto.Message):
    r"""Request for listing TraceScopes.

    Attributes:
        parent (str):
            Required. The full resource name of the location to look for
            trace scopes:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION_ID]

            For example:

            ::

                projects/my-project/locations/global
        page_size (int):
            Optional. The maximum number of results to return from this
            request.

            Non-positive values are ignored. The presence of
            ``next_page_token`` in the response indicates that more
            results might be available.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``page_token`` must be the value of ``next_page_token`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
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


class ListTraceScopesResponse(proto.Message):
    r"""Response for listing TraceScopes.

    Attributes:
        trace_scopes (MutableSequence[google.cloud.observability_v1.types.TraceScope]):
            Optional. A list of trace scopes.
        next_page_token (str):
            Optional. If there might be more results than appear in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call the same method again using the
            value of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    trace_scopes: MutableSequence["TraceScope"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TraceScope",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateTraceScopeRequest(proto.Message):
    r"""Request for updating a TraceScope.

    Attributes:
        trace_scope (google.cloud.observability_v1.types.TraceScope):
            Required. The updated trace scope.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    trace_scope: "TraceScope" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TraceScope",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTraceScopeRequest(proto.Message):
    r"""Request for deleting a TraceScope.

    Attributes:
        name (str):
            Required. The full resource name of the trace scope to
            delete:

            ::

                projects/[PROJECT_ID]/locations/[LOCATION_ID]/traceScopes/[TRACE_SCOPE_ID]

            For example:

            ::

                projects/my-project/locations/global/traceScopes/my-trace-scope
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSettingsRequest(proto.Message):
    r"""Request for getting Settings.

    Attributes:
        name (str):
            Required. Name of the settings to retrieve.

            Name format:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION]/settings"
                "folders/[FOLDER_ID]/locations/[LOCATION]/settings"
                "organizations/[ORGANIZATION_ID]/locations/[LOCATION]/settings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSettingsRequest(proto.Message):
    r"""Request for updating Settings.

    Attributes:
        settings (google.cloud.observability_v1.types.Settings):
            Required. The settings to update.

            The name field of settings is used to identify
            the resource to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The field mask specifying which
            fields of the settings are to be updated.
    """

    settings: "Settings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Settings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
