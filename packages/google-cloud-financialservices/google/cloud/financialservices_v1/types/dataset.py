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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.financialservices.v1",
    manifest={
        "Dataset",
        "ListDatasetsRequest",
        "ListDatasetsResponse",
        "GetDatasetRequest",
        "CreateDatasetRequest",
        "UpdateDatasetRequest",
        "DeleteDatasetRequest",
    },
)


class Dataset(proto.Message):
    r"""The Dataset resource contains summary information about a
    dataset.

    Attributes:
        name (str):
            Output only. The resource name of the Dataset. format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of creation of
            this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the most recent
            update of this resource.
        labels (MutableMapping[str, str]):
            Labels
        table_specs (MutableMapping[str, str]):
            Required. The set of BigQuery tables in the dataset. The key
            should be the table type and the value should be the
            BigQuery tables in the format
            ``bq://{project}.{dataset}.{table}``. Current table types
            are:

            - ``party``
            - ``account_party_link``
            - ``transaction``
            - ``risk_case_event``
            - ``party_supplementary_data``
        state (google.cloud.financialservices_v1.types.Dataset.State):
            Output only. State of the dataset (creating,
            active, deleting, etc.)
        date_range (google.type.interval_pb2.Interval):
            Required. Core time window of the dataset.
            All tables should have complete data covering
            this period.
        time_zone (google.type.datetime_pb2.TimeZone):
            The timezone of the data, default will act as
            UTC.
    """

    class State(proto.Enum):
        r"""The possible states of a resource.

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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    table_specs: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    date_range: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=8,
        message=interval_pb2.Interval,
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=9,
        message=datetime_pb2.TimeZone,
    )


class ListDatasetsRequest(proto.Message):
    r"""Request for retrieving a paginated list of Dataset resources
    that meet the specified criteria.

    Attributes:
        parent (str):
            Required. The parent of the Dataset is the
            Instance.
        page_size (int):
            The number of resources to be included in the response. The
            response contains a next_page_token, which can be used to
            retrieve the next page of resources.
        page_token (str):
            In case of paginated results, this is the token that was
            returned in the previous ListDatasetResponse. It should be
            copied here to retrieve the next page of resources. Empty
            will give the first page of ListDatasetRequest, and the last
            page will return an empty page_token.
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


class ListDatasetsResponse(proto.Message):
    r"""Response for retrieving a list of Datasets

    Attributes:
        datasets (MutableSequence[google.cloud.financialservices_v1.types.Dataset]):
            List of Dataset resources
        next_page_token (str):
            This token should be passed to the next
            ListDatasetsRequest to retrieve the next page of
            Datasets (empty indicates we are done).
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
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
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDatasetRequest(proto.Message):
    r"""Request for retrieving a specific Dataset resource.

    Attributes:
        name (str):
            Required. The resource name of the Dataset
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDatasetRequest(proto.Message):
    r"""Request for creating a Dataset resource.

    Attributes:
        parent (str):
            Required. The parent of the Dataset is the
            Instance.
        dataset_id (str):
            Required. The resource id of the dataset
        dataset (google.cloud.financialservices_v1.types.Dataset):
            Required. The dataset that will be created.
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
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dataset: "Dataset" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Dataset",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateDatasetRequest(proto.Message):
    r"""Request for updating a Dataset

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Dataset resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        dataset (google.cloud.financialservices_v1.types.Dataset):
            Required. The new value of the dataset fields that will be
            updated according to the update_mask.
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
    dataset: "Dataset" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Dataset",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteDatasetRequest(proto.Message):
    r"""Request for deleting a Dataset.

    Attributes:
        name (str):
            Required. The resource name of the Dataset.
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


__all__ = tuple(sorted(__protobuf__.manifest))
