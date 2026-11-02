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
        "Model",
        "ListModelsRequest",
        "ListModelsResponse",
        "GetModelRequest",
        "CreateModelRequest",
        "UpdateModelRequest",
        "DeleteModelRequest",
        "ExportModelMetadataRequest",
        "ExportModelMetadataResponse",
    },
)


class Model(proto.Message):
    r"""Model represents a trained model.

    Attributes:
        name (str):
            Output only. The resource name of the Model. format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/models/{model}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of creation of
            this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the most recent
            update of this resource.
        labels (MutableMapping[str, str]):
            Labels
        state (google.cloud.financialservices_v1.types.Model.State):
            Output only. State of the model (creating,
            active, deleting, etc.)
        engine_version (str):
            Output only. The EngineVersion used in
            training this model.  This is output only, and
            is determined from the EngineConfig used.
        engine_config (str):
            Required. The resource name of the EngineConfig the model
            training will be based on. Format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engineConfig}``
        primary_dataset (str):
            Required. The resource name of the Primary Dataset used in
            this model training. For information about how primary and
            auxiliary datasets are used, refer to the engine version's
            documentation. Format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}``
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. End_time specifies the latest time from which
            labels are used and from which data is used to generate
            features for training. End_time should be no later than the
            end of the date_range of the dataset.
        line_of_business (google.cloud.financialservices_v1.types.LineOfBusiness):
            Output only. The line of business
            (Retail/Commercial) this model is used for.
            Determined by EngineConfig, cannot be set by
            user.
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
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    engine_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    engine_config: str = proto.Field(
        proto.STRING,
        number=7,
    )
    primary_dataset: str = proto.Field(
        proto.STRING,
        number=8,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    line_of_business: gcf_line_of_business.LineOfBusiness = proto.Field(
        proto.ENUM,
        number=12,
        enum=gcf_line_of_business.LineOfBusiness,
    )


class ListModelsRequest(proto.Message):
    r"""Request for retrieving a paginated list of Model resources
    that meet the specified criteria.

    Attributes:
        parent (str):
            Required. The parent of the Model is the
            Instance.
        page_size (int):
            The number of resources to be included in the response. The
            response contains a next_page_token, which can be used to
            retrieve the next page of resources.
        page_token (str):
            In case of paginated results, this is the token that was
            returned in the previous ListModelsResponse. It should be
            copied here to retrieve the next page of resources. Empty
            will give the first page of ListModelsRequest, and the last
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


class ListModelsResponse(proto.Message):
    r"""Response for retrieving a list of Models

    Attributes:
        models (MutableSequence[google.cloud.financialservices_v1.types.Model]):
            List of Model resources
        next_page_token (str):
            This token should be passed to the next
            ListModelsRequest to retrieve the next page of
            Models (empty indicicates we are done).
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    models: MutableSequence["Model"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Model",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetModelRequest(proto.Message):
    r"""Request for retrieving a specific Model resource.

    Attributes:
        name (str):
            Required. The resource name of the Model
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateModelRequest(proto.Message):
    r"""Request for creating a Model resource.

    Attributes:
        parent (str):
            Required. The parent of the Model is the
            Instance.
        model_id (str):
            Required. The resource id of the Model
        model (google.cloud.financialservices_v1.types.Model):
            Required. The Model that will be created.
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
    model_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    model: "Model" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Model",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateModelRequest(proto.Message):
    r"""Request for updating a Model

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Model resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        model (google.cloud.financialservices_v1.types.Model):
            Required. The new value of the Model fields that will be
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
    model: "Model" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Model",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteModelRequest(proto.Message):
    r"""Request for deleting a Model.

    Attributes:
        name (str):
            Required. The resource name of the Model.
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


class ExportModelMetadataRequest(proto.Message):
    r"""Request for exporting Model metadata.

    Attributes:
        model (str):
            Required. The resource name of the Model.
        structured_metadata_destination (google.cloud.financialservices_v1.types.BigQueryDestination):
            Required. BigQuery output where the metadata
            will be written.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    structured_metadata_destination: bigquery_destination.BigQueryDestination = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=bigquery_destination.BigQueryDestination,
        )
    )


class ExportModelMetadataResponse(proto.Message):
    r"""Response for exporting Model metadata."""


__all__ = tuple(sorted(__protobuf__.manifest))
