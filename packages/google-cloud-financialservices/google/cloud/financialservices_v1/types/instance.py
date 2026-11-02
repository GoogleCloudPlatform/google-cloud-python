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

from google.cloud.financialservices_v1.types import bigquery_destination
from google.cloud.financialservices_v1.types import (
    line_of_business as gcf_line_of_business,
)

__protobuf__ = proto.module(
    package="google.cloud.financialservices.v1",
    manifest={
        "Instance",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "ImportRegisteredPartiesRequest",
        "ImportRegisteredPartiesResponse",
        "ExportRegisteredPartiesRequest",
        "ExportRegisteredPartiesResponse",
    },
)


class Instance(proto.Message):
    r"""Instance is a container for the rest of API resources.
    Only resources in the same instance can interact with each
    other. Child resources inherit the location (data residency) and
    encryption (CMEK). The location of the provided input and output
    in requests must match the location of the instance.

    Attributes:
        name (str):
            Output only. The full path to the Instance resource in this
            API. format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the Instance was
            created. Assigned by the server.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the Instance was
            last updated. Assigned by the server.
        state (google.cloud.financialservices_v1.types.Instance.State):
            Output only. State of the instance.
            Assigned by the server.
        labels (MutableMapping[str, str]):
            Labels
        kms_key (str):
            Required. The KMS key name used for CMEK
            (encryption-at-rest). format:
            ``projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}``
            VPC-SC restrictions apply.
    """

    class State(proto.Enum):
        r"""The Resource State

        Values:
            STATE_UNSPECIFIED (0):
                State is unspecified, should not occur.
            CREATING (1):
                The resource has not finished being created.
            ACTIVE (2):
                The resource is active/ready to be used.
            UPDATING (3):
                The resource is in the process of being
                updated.
            DELETING (4):
                The resource is in the process of being
                deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListInstancesRequest(proto.Message):
    r"""Request for retrieving a paginated list of Instance resources
    that meet the specified criteria.

    Attributes:
        parent (str):
            Required. The parent of the Instance is the
            location for that Instance. Every location has
            exactly one instance.
        page_size (int):
            The number of resources to be included in the response. The
            response contains a next_page_token, which can be used to
            retrieve the next page of resources.
        page_token (str):
            In case of paginated results, this is the
            token that was returned in the previous
            ListInstancesResponse. It should be copied here
            to retrieve the next page of resources. This
            will be empty for the first instance of
            ListInstancesRequest.
        filter (str):
            Specify a filter to narrow search results.
        order_by (str):
            Specify a field to use for ordering.
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


class ListInstancesResponse(proto.Message):
    r"""Response for retrieving a list of Instances

    Attributes:
        instances (MutableSequence[google.cloud.financialservices_v1.types.Instance]):
            List of Instance resources
        next_page_token (str):
            This token should be passed to the next
            ListInstancesRequest to retrieve the next page
            of Instances.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Request for retrieving a specific Instance resource.

    Attributes:
        name (str):
            Required. The resource name of the Instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request for creating a Instance resource.

    Attributes:
        parent (str):
            Required. The parent of the Instance is the
            location for that Instance. Every location has
            exactly one instance.
        instance_id (str):
            Required. The resource id of the instance.
        instance (google.cloud.financialservices_v1.types.Instance):
            Required. The instance that will be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Request for updating a Instance

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Instance resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        instance (google.cloud.financialservices_v1.types.Instance):
            Required. The new value of the instance fields that will be
            updated according to the update_mask
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Request for deleting a Instance.

    Attributes:
        name (str):
            Required. The resource name of the Instance.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ImportRegisteredPartiesRequest(proto.Message):
    r"""Request for adding/removing registered parties from BigQuery
    tables specified by the customer.

    Attributes:
        name (str):
            Required. The full path to the Instance resource in this
            API. format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        party_tables (MutableSequence[str]):
            Optional. List of BigQuery tables. Union of tables will be
            taken if there is more than one table. VPC-SC restrictions
            apply. format: ``bq://{project}.{bqDatasetID}.{bqTableID}``
            Use of ``datasets`` is preferred over the latter due to its
            simplicity and the reduced risk of errors ``party_tables``
            and ``datasets`` must not be provided at the same time
        mode (google.cloud.financialservices_v1.types.ImportRegisteredPartiesRequest.UpdateMode):
            Required. Mode of the request.
        validate_only (bool):
            Optional. If the request will not register
            the parties, just determine what would happen.
        line_of_business (google.cloud.financialservices_v1.types.LineOfBusiness):
            Required. LineOfBusiness for the specified
            registered parties.
    """

    class UpdateMode(proto.Enum):
        r"""UpdateMode controls the behavior for ImportRegisteredParties.

        Values:
            UPDATE_MODE_UNSPECIFIED (0):
                Default mode.
            REPLACE (1):
                Replace parties that are removable in Parties
                Table with new parties.
            APPEND (2):
                Add new parties to Parties Table.
        """

        UPDATE_MODE_UNSPECIFIED = 0
        REPLACE = 1
        APPEND = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    party_tables: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    mode: UpdateMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=UpdateMode,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    line_of_business: gcf_line_of_business.LineOfBusiness = proto.Field(
        proto.ENUM,
        number=5,
        enum=gcf_line_of_business.LineOfBusiness,
    )


class ImportRegisteredPartiesResponse(proto.Message):
    r"""Response for adding/removing registered parties from BigQuery
    tables.

    Attributes:
        parties_added (int):
            Number of parties added by this operation.
        parties_removed (int):
            Number of parties removed by this operation.
        parties_total (int):
            Total number of parties that are registered
            in this instance, after the update operation was
            completed.
        parties_failed_to_remove (int):
            Number of parties that failed to be removed
            by this operation.
        parties_uptiered (int):

        parties_downtiered (int):
            Total number of parties that are downtiered
            in this instance
        parties_failed_to_downtier (int):
            Number of parties that failed to be
            downtiered
    """

    parties_added: int = proto.Field(
        proto.INT64,
        number=1,
    )
    parties_removed: int = proto.Field(
        proto.INT64,
        number=2,
    )
    parties_total: int = proto.Field(
        proto.INT64,
        number=3,
    )
    parties_failed_to_remove: int = proto.Field(
        proto.INT64,
        number=4,
    )
    parties_uptiered: int = proto.Field(
        proto.INT64,
        number=5,
    )
    parties_downtiered: int = proto.Field(
        proto.INT64,
        number=6,
    )
    parties_failed_to_downtier: int = proto.Field(
        proto.INT64,
        number=7,
    )


class ExportRegisteredPartiesRequest(proto.Message):
    r"""Request to export a list of currently registered parties.

    Attributes:
        name (str):
            Required. The full path to the Instance resource in this
            API. format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        dataset (google.cloud.financialservices_v1.types.BigQueryDestination):
            Required. The location to output the
            RegisteredParties.
        line_of_business (google.cloud.financialservices_v1.types.LineOfBusiness):
            Required. LineOfBusiness to get
            RegisteredParties from.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset: bigquery_destination.BigQueryDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        message=bigquery_destination.BigQueryDestination,
    )
    line_of_business: gcf_line_of_business.LineOfBusiness = proto.Field(
        proto.ENUM,
        number=3,
        enum=gcf_line_of_business.LineOfBusiness,
    )


class ExportRegisteredPartiesResponse(proto.Message):
    r"""Response to export registered parties request."""


__all__ = tuple(sorted(__protobuf__.manifest))
