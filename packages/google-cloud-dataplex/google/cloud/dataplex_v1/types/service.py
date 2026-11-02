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

from google.cloud.dataplex_v1.types import resources
from google.cloud.dataplex_v1.types import tasks as gcd_tasks

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "CreateLakeRequest",
        "UpdateLakeRequest",
        "DeleteLakeRequest",
        "ListLakesRequest",
        "ListLakesResponse",
        "ListLakeActionsRequest",
        "ListActionsResponse",
        "GetLakeRequest",
        "CreateZoneRequest",
        "UpdateZoneRequest",
        "DeleteZoneRequest",
        "ListZonesRequest",
        "ListZonesResponse",
        "ListZoneActionsRequest",
        "GetZoneRequest",
        "CreateAssetRequest",
        "UpdateAssetRequest",
        "DeleteAssetRequest",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "ListAssetActionsRequest",
        "GetAssetRequest",
        "OperationMetadata",
        "CreateTaskRequest",
        "UpdateTaskRequest",
        "DeleteTaskRequest",
        "ListTasksRequest",
        "ListTasksResponse",
        "GetTaskRequest",
        "GetJobRequest",
        "RunTaskRequest",
        "RunTaskResponse",
        "ListJobsRequest",
        "ListJobsResponse",
        "CancelJobRequest",
    },
)


class CreateLakeRequest(proto.Message):
    r"""Create lake request.

    Attributes:
        parent (str):
            Required. The resource name of the lake location, of the
            form: projects/{project_number}/locations/{location_id}
            where ``location_id`` refers to a Google Cloud region.
        lake_id (str):
            Required. Lake identifier. This ID will be used to generate
            names such as database and dataset names when publishing
            metadata to Hive Metastore and BigQuery.

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must end with a number or a letter.
            - Must be between 1-63 characters.
            - Must be unique within the customer project / location.
        lake (google.cloud.dataplex_v1.types.Lake):
            Required. Lake resource
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lake_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lake: resources.Lake = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Lake,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateLakeRequest(proto.Message):
    r"""Update lake request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        lake (google.cloud.dataplex_v1.types.Lake):
            Required. Update description. Only fields specified in
            ``update_mask`` are updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    lake: resources.Lake = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Lake,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteLakeRequest(proto.Message):
    r"""Delete lake request.

    Attributes:
        name (str):
            Required. The resource name of the lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLakesRequest(proto.Message):
    r"""List lakes request.

    Attributes:
        parent (str):
            Required. The resource name of the lake location, of the
            form: ``projects/{project_number}/locations/{location_id}``
            where ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. Maximum number of Lakes to return.
            The service may return fewer than this value. If
            unspecified, at most 10 lakes will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous ``ListLakes``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to ``ListLakes``
            must match the call that provided the page token.
        filter (str):
            Optional. Filter request.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListLakesResponse(proto.Message):
    r"""List lakes response.

    Attributes:
        lakes (MutableSequence[google.cloud.dataplex_v1.types.Lake]):
            Lakes under the given parent location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    lakes: MutableSequence[resources.Lake] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Lake,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListLakeActionsRequest(proto.Message):
    r"""List lake actions request.

    Attributes:
        parent (str):
            Required. The resource name of the parent lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        page_size (int):
            Optional. Maximum number of actions to
            return. The service may return fewer than this
            value. If unspecified, at most 10 actions will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListLakeActions`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListLakeActions`` must match the call that
            provided the page token.
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


class ListActionsResponse(proto.Message):
    r"""List actions response.

    Attributes:
        actions (MutableSequence[google.cloud.dataplex_v1.types.Action]):
            Actions under the given parent
            lake/zone/asset.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    actions: MutableSequence[resources.Action] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Action,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetLakeRequest(proto.Message):
    r"""Get lake request.

    Attributes:
        name (str):
            Required. The resource name of the lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateZoneRequest(proto.Message):
    r"""Create zone request.

    Attributes:
        parent (str):
            Required. The resource name of the parent lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        zone_id (str):
            Required. Zone identifier. This ID will be used to generate
            names such as database and dataset names when publishing
            metadata to Hive Metastore and BigQuery.

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must end with a number or a letter.
            - Must be between 1-63 characters.
            - Must be unique across all lakes from all locations in a
              project.
            - Must not be one of the reserved IDs (i.e. "default",
              "global-temp")
        zone (google.cloud.dataplex_v1.types.Zone):
            Required. Zone resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone: resources.Zone = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Zone,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateZoneRequest(proto.Message):
    r"""Update zone request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        zone (google.cloud.dataplex_v1.types.Zone):
            Required. Update description. Only fields specified in
            ``update_mask`` are updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    zone: resources.Zone = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Zone,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteZoneRequest(proto.Message):
    r"""Delete zone request.

    Attributes:
        name (str):
            Required. The resource name of the zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListZonesRequest(proto.Message):
    r"""List zones request.

    Attributes:
        parent (str):
            Required. The resource name of the parent lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        page_size (int):
            Optional. Maximum number of zones to return.
            The service may return fewer than this value. If
            unspecified, at most 10 zones will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous ``ListZones``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to ``ListZones``
            must match the call that provided the page token.
        filter (str):
            Optional. Filter request.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListZonesResponse(proto.Message):
    r"""List zones response.

    Attributes:
        zones (MutableSequence[google.cloud.dataplex_v1.types.Zone]):
            Zones under the given parent lake.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    zones: MutableSequence[resources.Zone] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Zone,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListZoneActionsRequest(proto.Message):
    r"""List zone actions request.

    Attributes:
        parent (str):
            Required. The resource name of the parent zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        page_size (int):
            Optional. Maximum number of actions to
            return. The service may return fewer than this
            value. If unspecified, at most 10 actions will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListZoneActions`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListZoneActions`` must match the call that
            provided the page token.
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


class GetZoneRequest(proto.Message):
    r"""Get zone request.

    Attributes:
        name (str):
            Required. The resource name of the zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAssetRequest(proto.Message):
    r"""Create asset request.

    Attributes:
        parent (str):
            Required. The resource name of the parent zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        asset_id (str):
            Required. Asset identifier. This ID will be used to generate
            names such as table names when publishing metadata to Hive
            Metastore and BigQuery.

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must end with a number or a letter.
            - Must be between 1-63 characters.
            - Must be unique within the zone.
        asset (google.cloud.dataplex_v1.types.Asset):
            Required. Asset resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    asset: resources.Asset = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Asset,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAssetRequest(proto.Message):
    r"""Update asset request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        asset (google.cloud.dataplex_v1.types.Asset):
            Required. Update description. Only fields specified in
            ``update_mask`` are updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    asset: resources.Asset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Asset,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteAssetRequest(proto.Message):
    r"""Delete asset request.

    Attributes:
        name (str):
            Required. The resource name of the asset:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAssetsRequest(proto.Message):
    r"""List assets request.

    Attributes:
        parent (str):
            Required. The resource name of the parent zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        page_size (int):
            Optional. Maximum number of asset to return.
            The service may return fewer than this value. If
            unspecified, at most 10 assets will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous ``ListAssets``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to ``ListAssets``
            must match the call that provided the page token.
        filter (str):
            Optional. Filter request.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListAssetsResponse(proto.Message):
    r"""List assets response.

    Attributes:
        assets (MutableSequence[google.cloud.dataplex_v1.types.Asset]):
            Asset under the given parent zone.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assets: MutableSequence[resources.Asset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Asset,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAssetActionsRequest(proto.Message):
    r"""List asset actions request.

    Attributes:
        parent (str):
            Required. The resource name of the parent asset:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}``.
        page_size (int):
            Optional. Maximum number of actions to
            return. The service may return fewer than this
            value. If unspecified, at most 10 actions will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListAssetActions`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListAssetActions`` must match the call that
            provided the page token.
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


class GetAssetRequest(proto.Message):
    r"""Get asset request.

    Attributes:
        name (str):
            Required. The resource name of the asset:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of a long-running operation.

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
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
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


class CreateTaskRequest(proto.Message):
    r"""Create task request.

    Attributes:
        parent (str):
            Required. The resource name of the parent lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        task_id (str):
            Required. Task identifier.
        task (google.cloud.dataplex_v1.types.Task):
            Required. Task resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    task_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    task: gcd_tasks.Task = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_tasks.Task,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateTaskRequest(proto.Message):
    r"""Update task request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        task (google.cloud.dataplex_v1.types.Task):
            Required. Update description. Only fields specified in
            ``update_mask`` are updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    task: gcd_tasks.Task = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_tasks.Task,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteTaskRequest(proto.Message):
    r"""Delete task request.

    Attributes:
        name (str):
            Required. The resource name of the task:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/task/{task_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTasksRequest(proto.Message):
    r"""List tasks request.

    Attributes:
        parent (str):
            Required. The resource name of the parent lake:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        page_size (int):
            Optional. Maximum number of tasks to return.
            The service may return fewer than this value. If
            unspecified, at most 10 tasks will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous ``ListZones``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to ``ListZones``
            must match the call that provided the page token.
        filter (str):
            Optional. Filter request.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListTasksResponse(proto.Message):
    r"""List tasks response.

    Attributes:
        tasks (MutableSequence[google.cloud.dataplex_v1.types.Task]):
            Tasks under the given parent lake.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    tasks: MutableSequence[gcd_tasks.Task] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_tasks.Task,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTaskRequest(proto.Message):
    r"""Get task request.

    Attributes:
        name (str):
            Required. The resource name of the task:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{tasks_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetJobRequest(proto.Message):
    r"""Get job request.

    Attributes:
        name (str):
            Required. The resource name of the job:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunTaskRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The resource name of the task:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}``.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the task.
            If the map is left empty, the task will run with
            existing labels from task definition. If the map
            contains an entry with a new key, the same will
            be added to existing set of labels. If the map
            contains an entry with an existing label key in
            task definition, the task will run with new
            label value for that entry. Clearing an existing
            label will require label value to be explicitly
            set to a hyphen "-". The label value cannot be
            empty.
        args (MutableMapping[str, str]):
            Optional. Execution spec arguments. If the
            map is left empty, the task will run with
            existing execution spec args from task
            definition. If the map contains an entry with a
            new key, the same will be added to existing set
            of args. If the map contains an entry with an
            existing arg key in task definition, the task
            will run with new arg value for that entry.
            Clearing an existing arg will require arg value
            to be explicitly set to a hyphen "-". The arg
            value cannot be empty.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    args: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class RunTaskResponse(proto.Message):
    r"""

    Attributes:
        job (google.cloud.dataplex_v1.types.Job):
            Jobs created by RunTask API.
    """

    job: gcd_tasks.Job = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_tasks.Job,
    )


class ListJobsRequest(proto.Message):
    r"""List jobs request.

    Attributes:
        parent (str):
            Required. The resource name of the parent environment:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}``.
        page_size (int):
            Optional. Maximum number of jobs to return.
            The service may return fewer than this value. If
            unspecified, at most 10 jobs will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous ``ListJobs``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to ``ListJobs``
            must match the call that provided the page token.
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


class ListJobsResponse(proto.Message):
    r"""List jobs response.

    Attributes:
        jobs (MutableSequence[google.cloud.dataplex_v1.types.Job]):
            Jobs under a given task.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence[gcd_tasks.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_tasks.Job,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CancelJobRequest(proto.Message):
    r"""Cancel task jobs.

    Attributes:
        name (str):
            Required. The resource name of the job:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/task/{task_id}/job/{job_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
