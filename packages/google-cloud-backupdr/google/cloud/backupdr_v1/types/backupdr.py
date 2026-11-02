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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.backupdr_v1.types import backupvault_cloudsql

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "NetworkConfig",
        "ManagementURI",
        "WorkforceIdentityBasedManagementURI",
        "WorkforceIdentityBasedOAuth2ClientID",
        "ManagementServer",
        "ListManagementServersRequest",
        "ListManagementServersResponse",
        "GetManagementServerRequest",
        "CreateManagementServerRequest",
        "DeleteManagementServerRequest",
        "InitializeServiceRequest",
        "InitializeServiceResponse",
        "OperationMetadata",
    },
)


class NetworkConfig(proto.Message):
    r"""Network configuration for ManagementServer instance.

    Attributes:
        network (str):
            Optional. The resource name of the Google
            Compute Engine VPC network to which the
            ManagementServer instance is connected.
        peering_mode (google.cloud.backupdr_v1.types.NetworkConfig.PeeringMode):
            Optional. The network connect mode of the ManagementServer
            instance. For this version, only PRIVATE_SERVICE_ACCESS is
            supported.
    """

    class PeeringMode(proto.Enum):
        r"""VPC peering modes supported by Cloud BackupDR.

        Values:
            PEERING_MODE_UNSPECIFIED (0):
                Peering mode not set.
            PRIVATE_SERVICE_ACCESS (1):
                Connect using Private Service Access to the
                Management Server. Private services access
                provides an IP address range for multiple Google
                Cloud services, including Cloud BackupDR.
        """

        PEERING_MODE_UNSPECIFIED = 0
        PRIVATE_SERVICE_ACCESS = 1

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peering_mode: PeeringMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=PeeringMode,
    )


class ManagementURI(proto.Message):
    r"""ManagementURI for the Management Server resource.

    Attributes:
        web_ui (str):
            Output only. The ManagementServer AGM/RD
            WebUI URL.
        api (str):
            Output only. The ManagementServer AGM/RD API
            URL.
    """

    web_ui: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkforceIdentityBasedManagementURI(proto.Message):
    r"""ManagementURI depending on the Workforce Identity i.e. either
    1p or 3p.

    Attributes:
        first_party_management_uri (str):
            Output only. First party Management URI for
            Google Identities.
        third_party_management_uri (str):
            Output only. Third party Management URI for
            External Identity Providers.
    """

    first_party_management_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    third_party_management_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkforceIdentityBasedOAuth2ClientID(proto.Message):
    r"""OAuth Client ID depending on the Workforce Identity i.e.
    either 1p or 3p,

    Attributes:
        first_party_oauth2_client_id (str):
            Output only. First party OAuth Client ID for
            Google Identities.
        third_party_oauth2_client_id (str):
            Output only. Third party OAuth Client ID for
            External Identity Providers.
    """

    first_party_oauth2_client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    third_party_oauth2_client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ManagementServer(proto.Message):
    r"""ManagementServer describes a single BackupDR ManagementServer
    instance.

    Attributes:
        name (str):
            Output only. Identifier. The resource name.
        description (str):
            Optional. The description of the
            ManagementServer instance (2048 characters or
            less).
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user provided
            metadata. Labels currently defined:

            1. migrate_from_go=<false|true> If set to true, the MS is
               created in migration ready mode.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            updated.
        type_ (google.cloud.backupdr_v1.types.ManagementServer.InstanceType):
            Optional. The type of the ManagementServer
            resource.
        management_uri (google.cloud.backupdr_v1.types.ManagementURI):
            Output only. The hostname or ip address of
            the exposed AGM endpoints, used by clients to
            connect to AGM/RD graphical user interface and
            APIs.
        workforce_identity_based_management_uri (google.cloud.backupdr_v1.types.WorkforceIdentityBasedManagementURI):
            Output only. The hostnames of the exposed AGM
            endpoints for both types of user i.e. 1p and 3p,
            used to connect AGM/RM UI.
        state (google.cloud.backupdr_v1.types.ManagementServer.InstanceState):
            Output only. The ManagementServer state.
        networks (MutableSequence[google.cloud.backupdr_v1.types.NetworkConfig]):
            Optional. VPC networks to which the
            ManagementServer instance is connected. For this
            version, only a single network is supported.
            This field is optional if MS is created without
            PSA
        etag (str):
            Optional. Server specified ETag for the
            ManagementServer resource to prevent
            simultaneous updates from overwiting each other.
        oauth2_client_id (str):
            Output only. The OAuth 2.0 client id is required to make API
            calls to the BackupDR instance API of this ManagementServer.
            This is the value that should be provided in the 'aud' field
            of the OIDC ID Token (see openid specification
            https://openid.net/specs/openid-connect-core-1_0.html#IDToken).
        workforce_identity_based_oauth2_client_id (google.cloud.backupdr_v1.types.WorkforceIdentityBasedOAuth2ClientID):
            Output only. The OAuth client IDs for both
            types of user i.e. 1p and 3p.
        ba_proxy_uri (MutableSequence[str]):
            Output only. The hostname or ip address of
            the exposed AGM endpoints, used by BAs to
            connect to BA proxy.
        satisfies_pzs (google.protobuf.wrappers_pb2.BoolValue):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
    """

    class InstanceType(proto.Enum):
        r"""Type of backup service resource.

        Values:
            INSTANCE_TYPE_UNSPECIFIED (0):
                Instance type is not mentioned.
            BACKUP_RESTORE (1):
                Instance for backup and restore management
                (i.e., AGM).
        """

        INSTANCE_TYPE_UNSPECIFIED = 0
        BACKUP_RESTORE = 1

    class InstanceState(proto.Enum):
        r"""State of Management server instance.

        Values:
            INSTANCE_STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The instance is being created.
            READY (2):
                The instance has been created and is fully
                usable.
            UPDATING (3):
                The instance configuration is being updated.
                Certain kinds of updates may cause the instance
                to become unusable while the update is in
                progress.
            DELETING (4):
                The instance is being deleted.
            REPAIRING (5):
                The instance is being repaired and may be
                unstable.
            MAINTENANCE (6):
                Maintenance is being performed on this
                instance.
            ERROR (7):
                The instance is experiencing an issue and
                might be unusable. You can get further details
                from the statusMessage field of Instance
                resource.
        """

        INSTANCE_STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        UPDATING = 3
        DELETING = 4
        REPAIRING = 5
        MAINTENANCE = 6
        ERROR = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
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
    type_: InstanceType = proto.Field(
        proto.ENUM,
        number=14,
        enum=InstanceType,
    )
    management_uri: "ManagementURI" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ManagementURI",
    )
    workforce_identity_based_management_uri: "WorkforceIdentityBasedManagementURI" = (
        proto.Field(
            proto.MESSAGE,
            number=16,
            message="WorkforceIdentityBasedManagementURI",
        )
    )
    state: InstanceState = proto.Field(
        proto.ENUM,
        number=7,
        enum=InstanceState,
    )
    networks: MutableSequence["NetworkConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="NetworkConfig",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=13,
    )
    oauth2_client_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    workforce_identity_based_oauth2_client_id: "WorkforceIdentityBasedOAuth2ClientID" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="WorkforceIdentityBasedOAuth2ClientID",
    )
    ba_proxy_uri: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=18,
    )
    satisfies_pzs: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=19,
        message=wrappers_pb2.BoolValue,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class ListManagementServersRequest(proto.Message):
    r"""Request message for listing management servers.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            management servers information, in the format
            'projects/{project_id}/locations/{location}'. In Cloud
            BackupDR, locations map to Google Cloud regions, for example
            **us-central1**. To retrieve management servers for all
            locations, use "-" for the '{location}' value.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.

            This field is a member of `oneof`_ ``_filter``.
        order_by (str):
            Optional. Hint for how to order the results.

            This field is a member of `oneof`_ ``_order_by``.
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
        optional=True,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )


class ListManagementServersResponse(proto.Message):
    r"""Response message for listing management servers.

    Attributes:
        management_servers (MutableSequence[google.cloud.backupdr_v1.types.ManagementServer]):
            The list of ManagementServer instances in the
            project for the specified location.

            If the '{location}' value in the request is "-",
            the response contains a list of instances from
            all locations. In case any location is
            unreachable, the response will only return
            management servers in reachable locations and
            the 'unreachable' field will be populated with a
            list of unreachable locations.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    management_servers: MutableSequence["ManagementServer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ManagementServer",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetManagementServerRequest(proto.Message):
    r"""Request message for getting a management server instance.

    Attributes:
        name (str):
            Required. Name of the management server resource name, in
            the format
            'projects/{project_id}/locations/{location}/managementServers/{resource_name}'
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateManagementServerRequest(proto.Message):
    r"""Request message for creating a management server instance.

    Attributes:
        parent (str):
            Required. The management server project and location in the
            format 'projects/{project_id}/locations/{location}'. In
            Cloud Backup and DR locations map to Google Cloud regions,
            for example **us-central1**.
        management_server_id (str):
            Required. The name of the management server
            to create. The name must be unique for the
            specified project and location.
        management_server (google.cloud.backupdr_v1.types.ManagementServer):
            Required. A [management server
            resource][google.cloud.backupdr.v1.ManagementServer]
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
    management_server_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    management_server: "ManagementServer" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ManagementServer",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteManagementServerRequest(proto.Message):
    r"""Request message for deleting a management server instance.

    Attributes:
        name (str):
            Required. Name of the resource
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


class InitializeServiceRequest(proto.Message):
    r"""Request message for initializing the service.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the serviceConfig used to
            initialize the service. Format:
            ``projects/{project_id}/locations/{location}/serviceConfig``.
        resource_type (str):
            Required. The resource type to which the
            default service config will be applied. Examples
            include, "compute.googleapis.com/Instance" and
            "storage.googleapis.com/Bucket".
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        cloud_sql_instance_initialization_config (google.cloud.backupdr_v1.types.CloudSqlInstanceInitializationConfig):
            Optional. The configuration for initializing
            a Cloud SQL instance.

            This field is a member of `oneof`_ ``initialization_config``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_sql_instance_initialization_config: backupvault_cloudsql.CloudSqlInstanceInitializationConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="initialization_config",
        message=backupvault_cloudsql.CloudSqlInstanceInitializationConfig,
    )


class InitializeServiceResponse(proto.Message):
    r"""Response message for initializing the service.

    Attributes:
        backup_vault_name (str):
            The resource name of the default ``BackupVault`` created.
            Format:
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}``.
        backup_plan_name (str):
            The resource name of the default ``BackupPlan`` created.
            Format:
            ``projects/{project_id}/locations/{location}/backupPlans/{backup_plan_id}``.
    """

    backup_vault_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_plan_name: str = proto.Field(
        proto.STRING,
        number=2,
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
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to 'Code.CANCELLED'.
        api_version (str):
            Output only. API version used to start the
            operation.
        additional_info (MutableMapping[str, str]):
            Output only. AdditionalInfo contains
            additional Info related to backup plan
            association resource.
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
    additional_info: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
