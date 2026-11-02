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
        "EngineConfig",
        "ListEngineConfigsRequest",
        "ListEngineConfigsResponse",
        "GetEngineConfigRequest",
        "CreateEngineConfigRequest",
        "UpdateEngineConfigRequest",
        "DeleteEngineConfigRequest",
        "ExportEngineConfigMetadataRequest",
        "ExportEngineConfigMetadataResponse",
    },
)


class EngineConfig(proto.Message):
    r"""The EngineConfig resource creates the configuration for
    training a model.

    Attributes:
        name (str):
            Output only. The resource name of the EngineConfig. format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engine_config}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of creation of
            this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the most recent
            update of this resource.
        labels (MutableMapping[str, str]):
            Labels
        state (google.cloud.financialservices_v1.types.EngineConfig.State):
            Output only. State of the EngineConfig
            (creating, active, deleting, etc.)
        engine_version (str):
            Required. The resource name of the EngineVersion used in
            this model tuning. format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}``
        tuning (google.cloud.financialservices_v1.types.EngineConfig.Tuning):
            Optional. Configuration for tuning in creation of the
            EngineConfig. This field is required if
            ``hyperparameter_source.type`` is not ``INHERITED``, and
            output-only otherwise.
        performance_target (google.cloud.financialservices_v1.types.EngineConfig.PerformanceTarget):
            Optional. PerformanceTarget gives information on how the
            tuning and training will be evaluated. This field is
            required if ``hyperparameter_source.type`` is not
            ``INHERITED``, and output-only otherwise.
        line_of_business (google.cloud.financialservices_v1.types.LineOfBusiness):
            Output only. The line of business
            (Retail/Commercial) this engine config is used
            for. Determined by EngineVersion, cannot be set
            by user.
        hyperparameter_source_type (google.cloud.financialservices_v1.types.EngineConfig.HyperparameterSourceType):
            Optional. The origin of hyperparameters for the created
            EngineConfig. The default is ``TUNING``. In this case, the
            hyperparameters are selected as a result of a tuning run.
        hyperparameter_source (google.cloud.financialservices_v1.types.EngineConfig.HyperparameterSource):
            Optional. Configuration of hyperparameters
            source EngineConfig.
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

    class HyperparameterSourceType(proto.Enum):
        r"""The type of the hyperparameter source.

        Values:
            HYPERPARAMETER_SOURCE_TYPE_UNSPECIFIED (0):
                Hyperparameter source type is unspecified,
                defaults to TUNING.
            TUNING (1):
                The EngineConfig creation starts a tuning job
                which selects the best hyperparameters.
            INHERITED (2):
                The hyperparameters are inherited from
                another EngineConfig.
        """

        HYPERPARAMETER_SOURCE_TYPE_UNSPECIFIED = 0
        TUNING = 1
        INHERITED = 2

    class Tuning(proto.Message):
        r"""The parameters needed for the tuning operation, these are
        used only in tuning and not passed on to training.

        Attributes:
            primary_dataset (str):
                Required. The resource name of the Primary Dataset used in
                this model tuning. For information about how primary and
                auxiliary datasets are used, refer to the engine version's
                documentation. Format:
                ``/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}``
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. End_time specifies the latest time from which
                labels are used and from which data is used to generate
                features for tuning. End_time should be no later than the
                end of the date_range of the dataset.
        """

        primary_dataset: str = proto.Field(
            proto.STRING,
            number=1,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=10,
            message=timestamp_pb2.Timestamp,
        )

    class PerformanceTarget(proto.Message):
        r"""PerformanceTarget gives hints on how to evaluate the
        performance of a model.

        Attributes:
            party_investigations_per_period_hint (int):
                Required. A number that gives the tuner a
                hint on the number of parties from this data
                that will be investigated per period (monthly).
                This is used to control how the model is
                evaluated. For example, when trying AML AI for
                the first time, we recommend setting this to the
                number of parties investigated in an average
                month, based on alerts from your existing
                automated alerting system.
        """

        party_investigations_per_period_hint: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class HyperparameterSource(proto.Message):
        r"""Parameters for bootstrapping an Engine Config with the
        results of another one.

        Attributes:
            source_engine_config (str):
                Required. The resource name of the source EngineConfig whose
                outputs are used. Format:
                ``/projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engine_config}``
            source_engine_version (str):
                Output only. The resource name of the EngineVersion that was
                used in the tuning run. Format:
                ``/projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}``
        """

        source_engine_config: str = proto.Field(
            proto.STRING,
            number=1,
        )
        source_engine_version: str = proto.Field(
            proto.STRING,
            number=2,
        )

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
    tuning: Tuning = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Tuning,
    )
    performance_target: PerformanceTarget = proto.Field(
        proto.MESSAGE,
        number=11,
        message=PerformanceTarget,
    )
    line_of_business: gcf_line_of_business.LineOfBusiness = proto.Field(
        proto.ENUM,
        number=12,
        enum=gcf_line_of_business.LineOfBusiness,
    )
    hyperparameter_source_type: HyperparameterSourceType = proto.Field(
        proto.ENUM,
        number=15,
        enum=HyperparameterSourceType,
    )
    hyperparameter_source: HyperparameterSource = proto.Field(
        proto.MESSAGE,
        number=16,
        message=HyperparameterSource,
    )


class ListEngineConfigsRequest(proto.Message):
    r"""Request for retrieving a paginated list of EngineConfig
    resources that meet the specified criteria.

    Attributes:
        parent (str):
            Required. The parent of the EngineConfig is
            the Instance.
        page_size (int):
            The number of resources to be included in the response. The
            response contains a next_page_token, which can be used to
            retrieve the next page of resources.
        page_token (str):
            In case of paginated results, this is the token that was
            returned in the previous ListEngineConfigsResponse. It
            should be copied here to retrieve the next page of
            resources. Empty will give the first page of
            ListEngineConfigsRequest, and the last page will return an
            empty page_token.
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


class ListEngineConfigsResponse(proto.Message):
    r"""Response for retrieving a list of EngineConfigs

    Attributes:
        engine_configs (MutableSequence[google.cloud.financialservices_v1.types.EngineConfig]):
            List of EngineConfig resources
        next_page_token (str):
            This token should be passed to the next
            ListEngineConfigsRequest to retrieve the next
            page of EngineConfigs (empty indicates we are
            done).
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    engine_configs: MutableSequence["EngineConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EngineConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEngineConfigRequest(proto.Message):
    r"""Request for retrieving a specific EngineConfig resource.

    Attributes:
        name (str):
            Required. The resource name of the
            EngineConfig
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEngineConfigRequest(proto.Message):
    r"""Request for creating an EngineConfig resource.

    Attributes:
        parent (str):
            Required. The parent of the EngineConfig is
            the Instance.
        engine_config_id (str):
            Required. The resource id of the EngineConfig
        engine_config (google.cloud.financialservices_v1.types.EngineConfig):
            Required. The EngineConfig that will be
            created.
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
    engine_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    engine_config: "EngineConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EngineConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateEngineConfigRequest(proto.Message):
    r"""Request for updating an EngineConfig

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the EngineConfig resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        engine_config (google.cloud.financialservices_v1.types.EngineConfig):
            Required. The new value of the EngineConfig fields that will
            be updated according to the update_mask.
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
    engine_config: "EngineConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EngineConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteEngineConfigRequest(proto.Message):
    r"""Request for deleting an EngineConfig.

    Attributes:
        name (str):
            Required. The resource name of the
            EngineConfig.
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


class ExportEngineConfigMetadataRequest(proto.Message):
    r"""Request for exporting EngineConfig metadata.

    Attributes:
        engine_config (str):
            Required. The resource name of the
            EngineConfig.
        structured_metadata_destination (google.cloud.financialservices_v1.types.BigQueryDestination):
            Required. BigQuery output where the metadata
            will be written.
    """

    engine_config: str = proto.Field(
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


class ExportEngineConfigMetadataResponse(proto.Message):
    r"""Response for exporting EngineConfig metadata."""


__all__ = tuple(sorted(__protobuf__.manifest))
