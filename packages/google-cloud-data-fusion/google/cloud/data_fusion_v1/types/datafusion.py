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
    package="google.cloud.datafusion.v1",
    manifest={
        "NetworkConfig",
        "Version",
        "Accelerator",
        "CryptoKeyConfig",
        "Instance",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "ListAvailableVersionsRequest",
        "ListAvailableVersionsResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "DeleteInstanceRequest",
        "UpdateInstanceRequest",
        "RestartInstanceRequest",
        "OperationMetadata",
    },
)


class NetworkConfig(proto.Message):
    r"""Network configuration for a Data Fusion instance. These
    configurations are used for peering with the customer network.
    Configurations are optional when a public Data Fusion instance
    is to be created. However, providing these configurations allows
    several benefits, such as reduced network latency while
    accessing the customer resources from managed Data Fusion
    instance nodes, as well as access to the customer on-prem
    resources.

    Attributes:
        network (str):
            Name of the network in the customer project
            with which the Tenant Project will be peered for
            executing pipelines. In case of shared VPC where
            the network resides in another host project the
            network should specified in the form of
            projects/{host-project-id}/global/networks/{network}
        ip_allocation (str):
            The IP range in CIDR notation to use for the
            managed Data Fusion instance nodes. This range
            must not overlap with any other ranges used in
            the customer network.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_allocation: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Version(proto.Message):
    r"""The Data Fusion version. This proto message stores
    information about certain Data Fusion version, which is used for
    Data Fusion version upgrade.

    Attributes:
        version_number (str):
            The version number of the Data Fusion
            instance, such as '6.0.1.0'.
        default_version (bool):
            Whether this is currently the default version
            for Cloud Data Fusion
        available_features (MutableSequence[str]):
            Represents a list of available feature names
            for a given version.
        type_ (google.cloud.data_fusion_v1.types.Version.Type):
            Type represents the release availability of
            the version
    """

    class Type(proto.Enum):
        r"""Each type represents the release availability of a CDF
        version

        Values:
            TYPE_UNSPECIFIED (0):
                Version does not have availability yet
            TYPE_PREVIEW (1):
                Version is under development and not
                considered stable
            TYPE_GENERAL_AVAILABILITY (2):
                Version is available for public use
        """

        TYPE_UNSPECIFIED = 0
        TYPE_PREVIEW = 1
        TYPE_GENERAL_AVAILABILITY = 2

    version_number: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_version: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    available_features: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=4,
        enum=Type,
    )


class Accelerator(proto.Message):
    r"""Identifies Data Fusion accelerators for an instance.

    Attributes:
        accelerator_type (google.cloud.data_fusion_v1.types.Accelerator.AcceleratorType):
            The type of an accelator for a CDF instance.
        state (google.cloud.data_fusion_v1.types.Accelerator.State):
            The state of the accelerator
    """

    class AcceleratorType(proto.Enum):
        r"""Each type represents an Accelerator (Add-On) supported by
        Cloud Data Fusion service.

        Values:
            ACCELERATOR_TYPE_UNSPECIFIED (0):
                Default value, if unspecified.
            CDC (1):
                Change Data Capture accelerator for CDF.
            HEALTHCARE (2):
                Cloud Healthcare accelerator for CDF. This
                accelerator is to enable Cloud Healthcare
                specific CDF plugins developed by Healthcare
                team.
            CCAI_INSIGHTS (3):
                Contact Center AI Insights
                This accelerator is used to enable import and
                export pipelines custom built to streamline CCAI
                Insights processing.
        """

        ACCELERATOR_TYPE_UNSPECIFIED = 0
        CDC = 1
        HEALTHCARE = 2
        CCAI_INSIGHTS = 3

    class State(proto.Enum):
        r"""Different values possible for the state of an accelerator

        Values:
            STATE_UNSPECIFIED (0):
                Default value, do not use
            ENABLED (1):
                Indicates that the accelerator is enabled and
                available to use
            DISABLED (2):
                Indicates that the accelerator is disabled
                and not available to use
            UNKNOWN (3):
                Indicates that accelerator state is currently
                unknown. Requests for enable, disable could be
                retried while in this state
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        UNKNOWN = 3

    accelerator_type: AcceleratorType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AcceleratorType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )


class CryptoKeyConfig(proto.Message):
    r"""The crypto key configuration. This field is used by the
    Customer-managed encryption keys (CMEK) feature.

    Attributes:
        key_reference (str):
            The name of the key which is used to encrypt/decrypt
            customer data. For key in Cloud KMS, the key should be in
            the format of
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
    """

    key_reference: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Instance(proto.Message):
    r"""Represents a Data Fusion instance.

    Attributes:
        name (str):
            Output only. The name of this instance is in
            the form of
            projects/{project}/locations/{location}/instances/{instance}.
        description (str):
            A description of this instance.
        type_ (google.cloud.data_fusion_v1.types.Instance.Type):
            Required. Instance type.
        enable_stackdriver_logging (bool):
            Option to enable Stackdriver Logging.
        enable_stackdriver_monitoring (bool):
            Option to enable Stackdriver Monitoring.
        private_instance (bool):
            Specifies whether the Data Fusion instance
            should be private. If set to true, all Data
            Fusion nodes will have private IP addresses and
            will not be able to access the public internet.
        network_config (google.cloud.data_fusion_v1.types.NetworkConfig):
            Network configuration options. These are
            required when a private Data Fusion instance is
            to be created.
        labels (MutableMapping[str, str]):
            The resource labels for instance to use to
            annotate any related underlying resources such
            as Compute Engine VMs. The character '=' is not
            allowed to be used within the labels.
        options (MutableMapping[str, str]):
            Map of additional options used to configure
            the behavior of Data Fusion instance.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the instance was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the instance was last
            updated.
        state (google.cloud.data_fusion_v1.types.Instance.State):
            Output only. The current state of this Data
            Fusion instance.
        state_message (str):
            Output only. Additional information about the
            current state of this Data Fusion instance if
            available.
        service_endpoint (str):
            Output only. Endpoint on which the Data
            Fusion UI is accessible.
        zone (str):
            Name of the zone in which the Data Fusion
            instance will be created. Only DEVELOPER
            instances use this field.
        version (str):
            Current version of the Data Fusion. Only
            specifiable in Update.
        service_account (str):
            Output only. Deprecated. Use tenant_project_id instead to
            extract the tenant project ID.
        display_name (str):
            Display name for an instance.
        available_version (MutableSequence[google.cloud.data_fusion_v1.types.Version]):
            Available versions that the instance can be
            upgraded to using UpdateInstanceRequest.
        api_endpoint (str):
            Output only. Endpoint on which the REST APIs
            is accessible.
        gcs_bucket (str):
            Output only. Cloud Storage bucket generated
            by Data Fusion in the customer project.
        accelerators (MutableSequence[google.cloud.data_fusion_v1.types.Accelerator]):
            List of accelerators enabled for this CDF
            instance.
        p4_service_account (str):
            Output only. P4 service account for the
            customer project.
        tenant_project_id (str):
            Output only. The name of the tenant project.
        dataproc_service_account (str):
            User-managed service account to set on
            Dataproc when Cloud Data Fusion creates Dataproc
            to run data processing pipelines.

            This allows users to have fine-grained access
            control on Dataproc's accesses to cloud
            resources.
        enable_rbac (bool):
            Option to enable granular role-based access
            control.
        crypto_key_config (google.cloud.data_fusion_v1.types.CryptoKeyConfig):
            The crypto key configuration. This field is
            used by the Customer-Managed Encryption Keys
            (CMEK) feature.
        disabled_reason (MutableSequence[google.cloud.data_fusion_v1.types.Instance.DisabledReason]):
            Output only. If the instance state is
            DISABLED, the reason for disabling the instance.
    """

    class Type(proto.Enum):
        r"""Represents the type of Data Fusion instance. Each type is
        configured with the default settings for processing and memory.

        Values:
            TYPE_UNSPECIFIED (0):
                No type specified. The instance creation will
                fail.
            BASIC (1):
                Basic Data Fusion instance. In Basic type,
                the user will be able to create data pipelines
                using point and click UI. However, there are
                certain limitations, such as fewer number of
                concurrent pipelines, no support for streaming
                pipelines, etc.
            ENTERPRISE (2):
                Enterprise Data Fusion instance. In
                Enterprise type, the user will have all features
                available, such as support for streaming
                pipelines, higher number of concurrent
                pipelines, etc.
            DEVELOPER (3):
                Developer Data Fusion instance. In Developer
                type, the user will have all features available
                but with restrictive capabilities. This is to
                help enterprises design and develop their data
                ingestion and integration pipelines at low cost.
        """

        TYPE_UNSPECIFIED = 0
        BASIC = 1
        ENTERPRISE = 2
        DEVELOPER = 3

    class State(proto.Enum):
        r"""Represents the state of a Data Fusion instance

        Values:
            STATE_UNSPECIFIED (0):
                Instance does not have a state yet
            CREATING (1):
                Instance is being created
            ACTIVE (2):
                Instance is active and ready for requests.
                This corresponds to 'RUNNING' in
                datafusion.v1beta1.
            FAILED (3):
                Instance creation failed
            DELETING (4):
                Instance is being deleted
            UPGRADING (5):
                Instance is being upgraded
            RESTARTING (6):
                Instance is being restarted
            UPDATING (7):
                Instance is being updated on customer request
            AUTO_UPDATING (8):
                Instance is being auto-updated
            AUTO_UPGRADING (9):
                Instance is being auto-upgraded
            DISABLED (10):
                Instance is disabled
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        DELETING = 4
        UPGRADING = 5
        RESTARTING = 6
        UPDATING = 7
        AUTO_UPDATING = 8
        AUTO_UPGRADING = 9
        DISABLED = 10

    class DisabledReason(proto.Enum):
        r"""The reason for disabling the instance if the state is
        DISABLED.

        Values:
            DISABLED_REASON_UNSPECIFIED (0):
                This is an unknown reason for disabling.
            KMS_KEY_ISSUE (1):
                The KMS key used by the instance is either
                revoked or denied access to
        """

        DISABLED_REASON_UNSPECIFIED = 0
        KMS_KEY_ISSUE = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    enable_stackdriver_logging: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    enable_stackdriver_monitoring: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    private_instance: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    network_config: "NetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="NetworkConfig",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    options: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=13,
    )
    service_endpoint: str = proto.Field(
        proto.STRING,
        number=14,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=15,
    )
    version: str = proto.Field(
        proto.STRING,
        number=16,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=17,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=18,
    )
    available_version: MutableSequence["Version"] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message="Version",
    )
    api_endpoint: str = proto.Field(
        proto.STRING,
        number=20,
    )
    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=21,
    )
    accelerators: MutableSequence["Accelerator"] = proto.RepeatedField(
        proto.MESSAGE,
        number=22,
        message="Accelerator",
    )
    p4_service_account: str = proto.Field(
        proto.STRING,
        number=23,
    )
    tenant_project_id: str = proto.Field(
        proto.STRING,
        number=24,
    )
    dataproc_service_account: str = proto.Field(
        proto.STRING,
        number=25,
    )
    enable_rbac: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    crypto_key_config: "CryptoKeyConfig" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="CryptoKeyConfig",
    )
    disabled_reason: MutableSequence[DisabledReason] = proto.RepeatedField(
        proto.ENUM,
        number=29,
        enum=DisabledReason,
    )


class ListInstancesRequest(proto.Message):
    r"""Request message for listing Data Fusion instances.

    Attributes:
        parent (str):
            Required. The project and location for which
            to retrieve instance information in the format
            projects/{project}/locations/{location}. If the
            location is specified as '-' (wildcard), then
            all regions available to the project are
            queried, and the results are aggregated.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        filter (str):
            List filter.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc",  or "" (unsorted).
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
    r"""Response message for the list instance request.

    Attributes:
        instances (MutableSequence[google.cloud.data_fusion_v1.types.Instance]):
            Represents a list of Data Fusion instances.
        next_page_token (str):
            Token to retrieve the next page of results or
            empty if there are no more results in the list.
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


class ListAvailableVersionsRequest(proto.Message):
    r"""Request message for the list available versions request.

    Attributes:
        parent (str):
            Required. The project and location for which
            to retrieve instance information in the format
            projects/{project}/locations/{location}.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        latest_patch_only (bool):
            Whether or not to return the latest patch of every available
            minor version. If true, only the latest patch will be
            returned. Ex. if allowed versions is [6.1.1, 6.1.2, 6.2.0]
            then response will be [6.1.2, 6.2.0]
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
    latest_patch_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListAvailableVersionsResponse(proto.Message):
    r"""Response message for the list available versions request.

    Attributes:
        available_versions (MutableSequence[google.cloud.data_fusion_v1.types.Version]):
            Represents a list of versions that are
            supported.
        next_page_token (str):
            Token to retrieve the next page of results or
            empty if there are no more results in the list.
    """

    @property
    def raw_page(self):
        return self

    available_versions: MutableSequence["Version"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Version",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInstanceRequest(proto.Message):
    r"""Request message for getting details about a Data Fusion
    instance.

    Attributes:
        name (str):
            Required. The instance resource name in the
            format
            projects/{project}/locations/{location}/instances/{instance}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request message for creating a Data Fusion instance.

    Attributes:
        parent (str):
            Required. The instance's project and location
            in the format
            projects/{project}/locations/{location}.
        instance_id (str):
            Required. The name of the instance to create.
        instance (google.cloud.data_fusion_v1.types.Instance):
            An instance resource.
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


class DeleteInstanceRequest(proto.Message):
    r"""Request message for deleting a Data Fusion instance.

    Attributes:
        name (str):
            Required. The instance resource name in the
            format
            projects/{project}/locations/{location}/instances/{instance}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Request message for updating a Data Fusion instance.
    Data Fusion allows updating the labels, options, and stack
    driver settings. This is also used for CDF version upgrade.

    Attributes:
        instance (google.cloud.data_fusion_v1.types.Instance):
            Required. The instance resource that replaces
            the resource on the server. Currently, Data
            Fusion only allows replacing labels, options,
            and stack driver settings. All other fields will
            be ignored.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields that the update
            will overwrite in an instance resource. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. If the user does not provide a mask, all the supported
            fields (labels, options, and version currently) will be
            overwritten.
    """

    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class RestartInstanceRequest(proto.Message):
    r"""Request message for restarting a Data Fusion instance.

    Attributes:
        name (str):
            Required. Name of the Data Fusion instance
            which need to be restarted in the form of
            projects/{project}/locations/{location}/instances/{instance}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of a long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_detail (str):
            Human-readable status of the operation if
            any.
        requested_cancellation (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
        additional_status (MutableMapping[str, str]):
            Map to hold any additional status info for
            the operation If there is an accelerator being
            enabled/disabled/deleted, this will be populated
            with accelerator name as key and status as
            ENABLING, DISABLING or DELETING
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
    status_detail: str = proto.Field(
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
    additional_status: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
