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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.month_pb2 as month_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.oracledatabase_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "CloudExadataInfrastructure",
        "CloudExadataInfrastructureProperties",
        "ExascaleConfig",
        "MaintenanceWindow",
        "ConfigureExascaleCloudExadataInfrastructureRequest",
    },
)


class CloudExadataInfrastructure(proto.Message):
    r"""Represents CloudExadataInfrastructure resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudExadataInfrastructure/

    Attributes:
        name (str):
            Identifier. The name of the Exadata Infrastructure resource
            with the format:
            projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}
        display_name (str):
            Optional. User friendly name for this
            resource.
        gcp_oracle_zone (str):
            Optional. The GCP Oracle zone where Oracle
            Exadata Infrastructure is hosted. Example:
            us-east4-b-r2. If not specified, the system will
            pick a zone based on availability.
        entitlement_id (str):
            Output only. Entitlement ID of the private
            offer against which this infrastructure resource
            is provisioned.
        properties (google.cloud.oracledatabase_v1.types.CloudExadataInfrastructureProperties):
            Optional. Various properties of the infra.
        labels (MutableMapping[str, str]):
            Optional. Labels or tags associated with the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            Exadata Infrastructure was created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=8,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    properties: "CloudExadataInfrastructureProperties" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CloudExadataInfrastructureProperties",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class CloudExadataInfrastructureProperties(proto.Message):
    r"""Various properties of Exadata Infrastructure.

    Attributes:
        ocid (str):
            Output only. OCID of created infra.
            https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle
        compute_count (int):
            Optional. The number of compute servers for
            the Exadata Infrastructure.
        storage_count (int):
            Optional. The number of Cloud Exadata storage
            servers for the Exadata Infrastructure.
        total_storage_size_gb (int):
            Optional. The total storage allocated to the
            Exadata Infrastructure resource, in gigabytes
            (GB).
        available_storage_size_gb (int):
            Output only. The available storage can be
            allocated to the Exadata Infrastructure
            resource, in gigabytes (GB).
        maintenance_window (google.cloud.oracledatabase_v1.types.MaintenanceWindow):
            Optional. Maintenance window for repair.
        state (google.cloud.oracledatabase_v1.types.CloudExadataInfrastructureProperties.State):
            Output only. The current lifecycle state of
            the Exadata Infrastructure.
        shape (str):
            Required. The shape of the Exadata
            Infrastructure. The shape determines the amount
            of CPU, storage, and memory resources allocated
            to the instance.
        oci_url (str):
            Output only. Deep link to the OCI console to
            view this resource.
        cpu_count (int):
            Output only. The number of enabled CPU cores.
        max_cpu_count (int):
            Output only. The total number of CPU cores
            available.
        memory_size_gb (int):
            Output only. The memory allocated in GBs.
        max_memory_gb (int):
            Output only. The total memory available in
            GBs.
        db_node_storage_size_gb (int):
            Output only. The local node storage allocated
            in GBs.
        max_db_node_storage_size_gb (int):
            Output only. The total local node storage
            available in GBs.
        data_storage_size_tb (float):
            Output only. Size, in terabytes, of the DATA
            disk group.
        max_data_storage_tb (float):
            Output only. The total available DATA disk
            group size.
        activated_storage_count (int):
            Output only. The requested number of
            additional storage servers activated for the
            Exadata Infrastructure.
        additional_storage_count (int):
            Output only. The requested number of
            additional storage servers for the Exadata
            Infrastructure.
        db_server_version (str):
            Output only. The software version of the
            database servers (dom0) in the Exadata
            Infrastructure.
        storage_server_version (str):
            Output only. The software version of the
            storage servers (cells) in the Exadata
            Infrastructure.
        next_maintenance_run_id (str):
            Output only. The OCID of the next maintenance
            run.
        next_maintenance_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the next
            maintenance run will occur.
        next_security_maintenance_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the next security
            maintenance run will occur.
        customer_contacts (MutableSequence[google.cloud.oracledatabase_v1.types.CustomerContact]):
            Optional. The list of customer contacts.
        monthly_storage_server_version (str):
            Output only. The monthly software version of
            the storage servers (cells) in the Exadata
            Infrastructure. Example: 20.1.15
        monthly_db_server_version (str):
            Output only. The monthly software version of
            the database servers (dom0) in the Exadata
            Infrastructure. Example: 20.1.15
        compute_model (google.cloud.oracledatabase_v1.types.ComputeModel):
            Output only. The compute model of the Exadata
            Infrastructure.
        database_server_type (str):
            Optional. The database server type of the
            Exadata Infrastructure.
        storage_server_type (str):
            Optional. The storage server type of the
            Exadata Infrastructure.
        exascale_config (google.cloud.oracledatabase_v1.types.ExascaleConfig):
            Output only. The Exascale configuration for
            the Exadata Infrastructure.
    """

    class State(proto.Enum):
        r"""The various lifecycle states of the Exadata Infrastructure.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            PROVISIONING (1):
                The Exadata Infrastructure is being
                provisioned.
            AVAILABLE (2):
                The Exadata Infrastructure is available for
                use.
            UPDATING (3):
                The Exadata Infrastructure is being updated.
            TERMINATING (4):
                The Exadata Infrastructure is being
                terminated.
            TERMINATED (5):
                The Exadata Infrastructure is terminated.
            FAILED (6):
                The Exadata Infrastructure is in failed
                state.
            MAINTENANCE_IN_PROGRESS (7):
                The Exadata Infrastructure is in maintenance.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        TERMINATING = 4
        TERMINATED = 5
        FAILED = 6
        MAINTENANCE_IN_PROGRESS = 7

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compute_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    storage_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    total_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=4,
    )
    available_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    maintenance_window: "MaintenanceWindow" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="MaintenanceWindow",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    shape: str = proto.Field(
        proto.STRING,
        number=8,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=9,
    )
    cpu_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    max_cpu_count: int = proto.Field(
        proto.INT32,
        number=11,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=12,
    )
    max_memory_gb: int = proto.Field(
        proto.INT32,
        number=13,
    )
    db_node_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=14,
    )
    max_db_node_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=15,
    )
    data_storage_size_tb: float = proto.Field(
        proto.DOUBLE,
        number=16,
    )
    max_data_storage_tb: float = proto.Field(
        proto.DOUBLE,
        number=17,
    )
    activated_storage_count: int = proto.Field(
        proto.INT32,
        number=18,
    )
    additional_storage_count: int = proto.Field(
        proto.INT32,
        number=19,
    )
    db_server_version: str = proto.Field(
        proto.STRING,
        number=20,
    )
    storage_server_version: str = proto.Field(
        proto.STRING,
        number=21,
    )
    next_maintenance_run_id: str = proto.Field(
        proto.STRING,
        number=22,
    )
    next_maintenance_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    next_security_maintenance_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    customer_contacts: MutableSequence[common.CustomerContact] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message=common.CustomerContact,
    )
    monthly_storage_server_version: str = proto.Field(
        proto.STRING,
        number=26,
    )
    monthly_db_server_version: str = proto.Field(
        proto.STRING,
        number=27,
    )
    compute_model: common.ComputeModel = proto.Field(
        proto.ENUM,
        number=31,
        enum=common.ComputeModel,
    )
    database_server_type: str = proto.Field(
        proto.STRING,
        number=29,
    )
    storage_server_type: str = proto.Field(
        proto.STRING,
        number=30,
    )
    exascale_config: "ExascaleConfig" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="ExascaleConfig",
    )


class ExascaleConfig(proto.Message):
    r"""Details of the Exascale configuration for the Exadata
    Infrastructure.

    Attributes:
        total_storage_size_gb (int):
            Output only. Total storage size needed for
            Exascale in GBs.
        available_storage_size_gb (int):
            Output only. Available storage size for
            Exascale in GBs.
        total_vm_storage_size_gb (int):
            Output only. Storage size needed for VM
            storage on Exascale in GBs.
        available_vm_storage_size_gb (int):
            Output only. Available storage size for VM
            storage on Exascale in GBs.
    """

    total_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=1,
    )
    available_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=2,
    )
    total_vm_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=3,
    )
    available_vm_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=4,
    )


class MaintenanceWindow(proto.Message):
    r"""Maintenance window as defined by Oracle.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/MaintenanceWindow

    Attributes:
        preference (google.cloud.oracledatabase_v1.types.MaintenanceWindow.MaintenanceWindowPreference):
            Optional. The maintenance window scheduling
            preference.
        months (MutableSequence[google.type.month_pb2.Month]):
            Optional. Months during the year when
            maintenance should be performed.
        weeks_of_month (MutableSequence[int]):
            Optional. Weeks during the month when
            maintenance should be performed. Weeks start on
            the 1st, 8th, 15th, and 22nd days of the month,
            and have a duration of 7 days. Weeks start and
            end based on calendar dates, not days of the
            week.
        days_of_week (MutableSequence[google.type.dayofweek_pb2.DayOfWeek]):
            Optional. Days during the week when
            maintenance should be performed.
        hours_of_day (MutableSequence[int]):
            Optional. The window of hours during the day
            when maintenance should be performed. The window
            is a 4 hour slot. Valid values are:

              0 - represents time slot 0:00 - 3:59 UTC
              4 - represents time slot 4:00 - 7:59 UTC
              8 - represents time slot 8:00 - 11:59 UTC
              12 - represents time slot 12:00 - 15:59 UTC
            16 - represents time slot 16:00 - 19:59 UTC   20
            - represents time slot 20:00 - 23:59 UTC
        lead_time_week (int):
            Optional. Lead time window allows user to set
            a lead time to prepare for a down time. The lead
            time is in weeks and valid value is between 1 to
            4.
        patching_mode (google.cloud.oracledatabase_v1.types.MaintenanceWindow.PatchingMode):
            Optional. Cloud CloudExadataInfrastructure
            node patching method, either "ROLLING" or
            "NONROLLING". Default value is ROLLING.
        custom_action_timeout_mins (int):
            Optional. Determines the amount of time the
            system will wait before the start of each
            database server patching operation. Custom
            action timeout is in minutes and valid value is
            between 15 to 120 (inclusive).
        is_custom_action_timeout_enabled (bool):
            Optional. If true, enables the configuration
            of a custom action timeout (waiting period)
            between database server patching operations.
    """

    class MaintenanceWindowPreference(proto.Enum):
        r"""Maintenance window preference.

        Values:
            MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED (0):
                Default unspecified value.
            CUSTOM_PREFERENCE (1):
                Custom preference.
            NO_PREFERENCE (2):
                No preference.
        """

        MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED = 0
        CUSTOM_PREFERENCE = 1
        NO_PREFERENCE = 2

    class PatchingMode(proto.Enum):
        r"""Patching mode.

        Values:
            PATCHING_MODE_UNSPECIFIED (0):
                Default unspecified value.
            ROLLING (1):
                Updates the Cloud Exadata database server
                hosts in a rolling fashion.
            NON_ROLLING (2):
                The non-rolling maintenance method first
                updates your storage servers at the same time,
                then your database servers at the same time.
        """

        PATCHING_MODE_UNSPECIFIED = 0
        ROLLING = 1
        NON_ROLLING = 2

    preference: MaintenanceWindowPreference = proto.Field(
        proto.ENUM,
        number=1,
        enum=MaintenanceWindowPreference,
    )
    months: MutableSequence[month_pb2.Month] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=month_pb2.Month,
    )
    weeks_of_month: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )
    days_of_week: MutableSequence[dayofweek_pb2.DayOfWeek] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=dayofweek_pb2.DayOfWeek,
    )
    hours_of_day: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=5,
    )
    lead_time_week: int = proto.Field(
        proto.INT32,
        number=6,
    )
    patching_mode: PatchingMode = proto.Field(
        proto.ENUM,
        number=7,
        enum=PatchingMode,
    )
    custom_action_timeout_mins: int = proto.Field(
        proto.INT32,
        number=8,
    )
    is_custom_action_timeout_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class ConfigureExascaleCloudExadataInfrastructureRequest(proto.Message):
    r"""The request for ``CloudExadataInfrastructure.ConfigureExascale``.

    Attributes:
        name (str):
            Required. The name of the Cloud Exadata Infrastructure in
            the following format:
            projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.
        total_storage_size_gb (int):
            Required. The total storage to be allocated
            to Exascale in GBs.
        total_vm_storage_size_gb (int):
            Optional. Storage size needed for VM storage
            on Exascale in GBs.
        request_id (str):
            Optional. An optional ID to identify the
            request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    total_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=2,
    )
    total_vm_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=4,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
