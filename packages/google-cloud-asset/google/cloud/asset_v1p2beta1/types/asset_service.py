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

from google.cloud.asset_v1p2beta1.types import assets as gca_assets

__protobuf__ = proto.module(
    package="google.cloud.asset.v1p2beta1",
    manifest={
        "ContentType",
        "ExportAssetsResponse",
        "BatchGetAssetsHistoryResponse",
        "CreateFeedRequest",
        "GetFeedRequest",
        "ListFeedsRequest",
        "ListFeedsResponse",
        "UpdateFeedRequest",
        "DeleteFeedRequest",
        "OutputConfig",
        "GcsDestination",
        "PubsubDestination",
        "FeedOutputConfig",
        "Feed",
    },
)


class ContentType(proto.Enum):
    r"""Asset content type.

    Values:
        CONTENT_TYPE_UNSPECIFIED (0):
            Unspecified content type.
        RESOURCE (1):
            Resource metadata.
        IAM_POLICY (2):
            The actual IAM policy set on a resource.
    """

    CONTENT_TYPE_UNSPECIFIED = 0
    RESOURCE = 1
    IAM_POLICY = 2


class ExportAssetsResponse(proto.Message):
    r"""The export asset response. This message is returned by the
    [google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]
    method in the returned
    [google.longrunning.Operation.response][google.longrunning.Operation.response]
    field.

    Attributes:
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the snapshot was taken.
        output_config (google.cloud.asset_v1p2beta1.types.OutputConfig):
            Output configuration indicating where the
            results were output to.
    """

    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputConfig",
    )


class BatchGetAssetsHistoryResponse(proto.Message):
    r"""Batch get assets history response.

    Attributes:
        assets (MutableSequence[google.cloud.asset_v1p2beta1.types.TemporalAsset]):
            A list of assets with valid time windows.
    """

    assets: MutableSequence[gca_assets.TemporalAsset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_assets.TemporalAsset,
    )


class CreateFeedRequest(proto.Message):
    r"""Create asset feed request.

    Attributes:
        parent (str):
            Required. The name of the
            project/folder/organization where this feed
            should be created in. It can only be an
            organization number (such as
            "organizations/123"), a folder number (such as
            "folders/123"), a project ID (such as
            "projects/my-project-id"), or a project number
            (such as "projects/12345").
        feed_id (str):
            Required. This is the client-assigned asset
            feed identifier and it needs to be unique under
            a specific parent project/folder/organization.
        feed (google.cloud.asset_v1p2beta1.types.Feed):
            Required. The feed details. The field ``name`` must be empty
            and it will be generated in the format of:
            projects/project_number/feeds/feed_id
            folders/folder_number/feeds/feed_id
            organizations/organization_number/feeds/feed_id
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feed_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    feed: "Feed" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Feed",
    )


class GetFeedRequest(proto.Message):
    r"""Get asset feed request.

    Attributes:
        name (str):
            Required. The name of the Feed and it must be in the format
            of: projects/project_number/feeds/feed_id
            folders/folder_number/feeds/feed_id
            organizations/organization_number/feeds/feed_id
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFeedsRequest(proto.Message):
    r"""List asset feeds request.

    Attributes:
        parent (str):
            Required. The parent
            project/folder/organization whose feeds are to
            be listed. It can only be using
            project/folder/organization number (such as
            "folders/12345")", or a project ID (such as
            "projects/my-project-id").
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFeedsResponse(proto.Message):
    r"""

    Attributes:
        feeds (MutableSequence[google.cloud.asset_v1p2beta1.types.Feed]):
            A list of feeds.
    """

    feeds: MutableSequence["Feed"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Feed",
    )


class UpdateFeedRequest(proto.Message):
    r"""Update asset feed request.

    Attributes:
        feed (google.cloud.asset_v1p2beta1.types.Feed):
            Required. The new values of feed details. It must match an
            existing feed and the field ``name`` must be in the format
            of: projects/project_number/feeds/feed_id or
            folders/folder_number/feeds/feed_id or
            organizations/organization_number/feeds/feed_id.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Only updates the ``feed`` fields indicated by this
            mask. The field mask must not be empty, and it must not
            contain fields that are immutable or only set by the server.
    """

    feed: "Feed" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Feed",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteFeedRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the feed and it must be in the format
            of: projects/project_number/feeds/feed_id
            folders/folder_number/feeds/feed_id
            organizations/organization_number/feeds/feed_id
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OutputConfig(proto.Message):
    r"""Output configuration for export assets destination.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.asset_v1p2beta1.types.GcsDestination):
            Destination on Cloud Storage.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="GcsDestination",
    )


class GcsDestination(proto.Message):
    r"""A Cloud Storage location.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            The URI of the Cloud Storage object. It's the same URI that
            is used by gsutil. For example:
            "gs://bucket_name/object_name". See `Viewing and Editing
            Object
            Metadata <https://cloud.google.com/storage/docs/viewing-editing-metadata>`__
            for more information.

            This field is a member of `oneof`_ ``object_uri``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="object_uri",
    )


class PubsubDestination(proto.Message):
    r"""A Pub/Sub destination.

    Attributes:
        topic (str):
            The name of the Pub/Sub topic to publish to. For example:
            ``projects/PROJECT_ID/topics/TOPIC_ID``.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FeedOutputConfig(proto.Message):
    r"""Output configuration for asset feed destination.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pubsub_destination (google.cloud.asset_v1p2beta1.types.PubsubDestination):
            Destination on Pub/Sub.

            This field is a member of `oneof`_ ``destination``.
    """

    pubsub_destination: "PubsubDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="PubsubDestination",
    )


class Feed(proto.Message):
    r"""An asset feed used to export asset updates to a destinations.
    An asset feed filter controls what updates are exported. The
    asset feed must be created within a project, organization, or
    folder. Supported destinations are:

    Cloud Pub/Sub topics.

    Attributes:
        name (str):
            Required. The format will be
            projects/{project_number}/feeds/{client-assigned_feed_identifier}
            or
            folders/{folder_number}/feeds/{client-assigned_feed_identifier}
            or
            organizations/{organization_number}/feeds/{client-assigned_feed_identifier}

            The client-assigned feed identifier must be unique within
            the parent project/folder/organization.
        asset_names (MutableSequence[str]):
            A list of the full names of the assets to receive updates.
            You must specify either or both of asset_names and
            asset_types. Only asset updates matching specified
            asset_names or asset_types are exported to the feed. For
            example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more info.
        asset_types (MutableSequence[str]):
            A list of types of the assets to receive updates. You must
            specify either or both of asset_names and asset_types. Only
            asset updates matching specified asset_names or asset_types
            are exported to the feed. For example:
            "compute.googleapis.com/Disk" See `Introduction to Cloud
            Asset
            Inventory <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview>`__
            for all supported asset types.
        content_type (google.cloud.asset_v1p2beta1.types.ContentType):
            Asset content type. If not specified, no
            content but the asset name and type will be
            returned.
        feed_output_config (google.cloud.asset_v1p2beta1.types.FeedOutputConfig):
            Required. Feed output configuration defining
            where the asset updates are published to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    asset_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    content_type: "ContentType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ContentType",
    )
    feed_output_config: "FeedOutputConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FeedOutputConfig",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
