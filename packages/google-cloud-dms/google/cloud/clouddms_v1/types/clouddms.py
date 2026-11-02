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

from google.cloud.clouddms_v1.types import (
    clouddms_resources,
    conversionworkspace_resources,
)

__protobuf__ = proto.module(
    package="google.cloud.clouddms.v1",
    manifest={
        "DatabaseEntityView",
        "ListMigrationJobsRequest",
        "ListMigrationJobsResponse",
        "GetMigrationJobRequest",
        "CreateMigrationJobRequest",
        "UpdateMigrationJobRequest",
        "DeleteMigrationJobRequest",
        "StartMigrationJobRequest",
        "StopMigrationJobRequest",
        "ResumeMigrationJobRequest",
        "PromoteMigrationJobRequest",
        "VerifyMigrationJobRequest",
        "RestartMigrationJobRequest",
        "GenerateSshScriptRequest",
        "VmCreationConfig",
        "VmSelectionConfig",
        "SshScript",
        "GenerateTcpProxyScriptRequest",
        "TcpProxyScript",
        "ListConnectionProfilesRequest",
        "ListConnectionProfilesResponse",
        "GetConnectionProfileRequest",
        "CreateConnectionProfileRequest",
        "UpdateConnectionProfileRequest",
        "DeleteConnectionProfileRequest",
        "CreatePrivateConnectionRequest",
        "ListPrivateConnectionsRequest",
        "ListPrivateConnectionsResponse",
        "DeletePrivateConnectionRequest",
        "GetPrivateConnectionRequest",
        "OperationMetadata",
        "ListConversionWorkspacesRequest",
        "ListConversionWorkspacesResponse",
        "GetConversionWorkspaceRequest",
        "CreateConversionWorkspaceRequest",
        "UpdateConversionWorkspaceRequest",
        "DeleteConversionWorkspaceRequest",
        "CommitConversionWorkspaceRequest",
        "RollbackConversionWorkspaceRequest",
        "ApplyConversionWorkspaceRequest",
        "ListMappingRulesRequest",
        "ListMappingRulesResponse",
        "GetMappingRuleRequest",
        "SeedConversionWorkspaceRequest",
        "ConvertConversionWorkspaceRequest",
        "ImportMappingRulesRequest",
        "DescribeDatabaseEntitiesRequest",
        "DescribeDatabaseEntitiesResponse",
        "SearchBackgroundJobsRequest",
        "SearchBackgroundJobsResponse",
        "DescribeConversionWorkspaceRevisionsRequest",
        "DescribeConversionWorkspaceRevisionsResponse",
        "CreateMappingRuleRequest",
        "DeleteMappingRuleRequest",
        "FetchStaticIpsRequest",
        "FetchStaticIpsResponse",
    },
)


class DatabaseEntityView(proto.Enum):
    r"""AIP-157 Partial Response view for Database Entity.

    Values:
        DATABASE_ENTITY_VIEW_UNSPECIFIED (0):
            Unspecified view. Defaults to basic view.
        DATABASE_ENTITY_VIEW_BASIC (1):
            Default view. Does not return DDLs or Issues.
        DATABASE_ENTITY_VIEW_FULL (2):
            Return full entity details including
            mappings, ddl and issues.
        DATABASE_ENTITY_VIEW_ROOT_SUMMARY (3):
            Top-most (Database, Schema) nodes which are returned
            contains summary details for their decendents such as the
            number of entities per type and issues rollups. When this
            view is used, only a single page of result is returned and
            the page_size property of the request is ignored. The
            returned page will only include the top-most node types.
    """

    DATABASE_ENTITY_VIEW_UNSPECIFIED = 0
    DATABASE_ENTITY_VIEW_BASIC = 1
    DATABASE_ENTITY_VIEW_FULL = 2
    DATABASE_ENTITY_VIEW_ROOT_SUMMARY = 3


class ListMigrationJobsRequest(proto.Message):
    r"""Retrieves a list of all migration jobs in a given project and
    location.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of migrationJobs.
        page_size (int):
            The maximum number of migration jobs to
            return. The service may return fewer than this
            value. If unspecified, at most 50 migration jobs
            will be returned. The maximum value is 1000;
            values above 1000 are coerced to 1000.
        page_token (str):
            The nextPageToken value received in the
            previous call to migrationJobs.list, used in the
            subsequent request to retrieve the next page of
            results. On first call this should be left
            blank. When paginating, all other parameters
            provided to migrationJobs.list must match the
            call that provided the page token.
        filter (str):
            A filter expression that filters migration jobs listed in
            the response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be either =, !=, >, or
            <. For example, list migration jobs created this year by
            specifying **createTime %gt;
            2020-01-01T00:00:00.000000000Z.** You can also filter nested
            fields. For example, you could specify
            **reverseSshConnectivity.vmIp = "1.2.3.4"** to select all
            migration jobs connecting through the specific SSH tunnel
            bastion.
        order_by (str):
            Sort the results based on the migration job
            name. Valid values are: "name", "name asc", and
            "name desc".
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


class ListMigrationJobsResponse(proto.Message):
    r"""Response message for 'ListMigrationJobs' request.

    Attributes:
        migration_jobs (MutableSequence[google.cloud.clouddms_v1.types.MigrationJob]):
            The list of migration jobs objects.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    migration_jobs: MutableSequence[clouddms_resources.MigrationJob] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=clouddms_resources.MigrationJob,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMigrationJobRequest(proto.Message):
    r"""Request message for 'GetMigrationJob' request.

    Attributes:
        name (str):
            Required. Name of the migration job resource
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMigrationJobRequest(proto.Message):
    r"""Request message to create a new Database Migration Service
    migration job in the specified project and region.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of migration jobs.
        migration_job_id (str):
            Required. The ID of the instance to create.
        migration_job (google.cloud.clouddms_v1.types.MigrationJob):
            Required. Represents a `migration
            job <https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs>`__
            object.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two requests with the same ID, then the
            second request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    migration_job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    migration_job: clouddms_resources.MigrationJob = proto.Field(
        proto.MESSAGE,
        number=3,
        message=clouddms_resources.MigrationJob,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMigrationJobRequest(proto.Message):
    r"""Request message for 'UpdateMigrationJob' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the
            fields to be overwritten by the update in the
            conversion workspace resource.
        migration_job (google.cloud.clouddms_v1.types.MigrationJob):
            Required. The migration job parameters to
            update.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    migration_job: clouddms_resources.MigrationJob = proto.Field(
        proto.MESSAGE,
        number=2,
        message=clouddms_resources.MigrationJob,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMigrationJobRequest(proto.Message):
    r"""Request message for 'DeleteMigrationJob' request.

    Attributes:
        name (str):
            Required. Name of the migration job resource
            to delete.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        force (bool):
            The destination CloudSQL connection profile
            is always deleted with the migration job. In
            case of force delete, the destination CloudSQL
            replica database is also deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class StartMigrationJobRequest(proto.Message):
    r"""Request message for 'StartMigrationJob' request.

    Attributes:
        name (str):
            Name of the migration job resource to start.
        skip_validation (bool):
            Optional. Start the migration job without running prior
            configuration verification. Defaults to ``false``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skip_validation: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class StopMigrationJobRequest(proto.Message):
    r"""Request message for 'StopMigrationJob' request.

    Attributes:
        name (str):
            Name of the migration job resource to stop.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeMigrationJobRequest(proto.Message):
    r"""Request message for 'ResumeMigrationJob' request.

    Attributes:
        name (str):
            Name of the migration job resource to resume.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PromoteMigrationJobRequest(proto.Message):
    r"""Request message for 'PromoteMigrationJob' request.

    Attributes:
        name (str):
            Name of the migration job resource to
            promote.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VerifyMigrationJobRequest(proto.Message):
    r"""Request message for 'VerifyMigrationJob' request.

    Attributes:
        name (str):
            Name of the migration job resource to verify.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the
            changed fields to be verified. It will not
            update the migration job.
        migration_job (google.cloud.clouddms_v1.types.MigrationJob):
            Optional. The changed migration job
            parameters to verify. It will not update the
            migration job.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    migration_job: clouddms_resources.MigrationJob = proto.Field(
        proto.MESSAGE,
        number=3,
        message=clouddms_resources.MigrationJob,
    )


class RestartMigrationJobRequest(proto.Message):
    r"""Request message for 'RestartMigrationJob' request.

    Attributes:
        name (str):
            Name of the migration job resource to
            restart.
        skip_validation (bool):
            Optional. Restart the migration job without running prior
            configuration verification. Defaults to ``false``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skip_validation: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class GenerateSshScriptRequest(proto.Message):
    r"""Request message for 'GenerateSshScript' request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        migration_job (str):
            Name of the migration job resource to
            generate the SSH script.
        vm (str):
            Required. Bastion VM Instance name to use or
            to create.
        vm_creation_config (google.cloud.clouddms_v1.types.VmCreationConfig):
            The VM creation configuration

            This field is a member of `oneof`_ ``vm_config``.
        vm_selection_config (google.cloud.clouddms_v1.types.VmSelectionConfig):
            The VM selection configuration

            This field is a member of `oneof`_ ``vm_config``.
        vm_port (int):
            The port that will be open on the bastion
            host.
    """

    migration_job: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vm_creation_config: "VmCreationConfig" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="vm_config",
        message="VmCreationConfig",
    )
    vm_selection_config: "VmSelectionConfig" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="vm_config",
        message="VmSelectionConfig",
    )
    vm_port: int = proto.Field(
        proto.INT32,
        number=3,
    )


class VmCreationConfig(proto.Message):
    r"""VM creation configuration message

    Attributes:
        vm_machine_type (str):
            Required. VM instance machine type to create.
        vm_zone (str):
            The Google Cloud Platform zone to create the
            VM in.
        subnet (str):
            The subnet name the vm needs to be created
            in.
    """

    vm_machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=3,
    )


class VmSelectionConfig(proto.Message):
    r"""VM selection configuration message

    Attributes:
        vm_zone (str):
            Required. The Google Cloud Platform zone the
            VM is located.
    """

    vm_zone: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SshScript(proto.Message):
    r"""Response message for 'GenerateSshScript' request.

    Attributes:
        script (str):
            The ssh configuration script.
    """

    script: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateTcpProxyScriptRequest(proto.Message):
    r"""Request message for 'GenerateTcpProxyScript' request.

    Attributes:
        migration_job (str):
            Name of the migration job resource to
            generate the TCP Proxy script.
        vm_name (str):
            Required. The name of the Compute instance
            that will host the proxy.
        vm_machine_type (str):
            Required. The type of the Compute instance
            that will host the proxy.
        vm_zone (str):
            Optional. The Google Cloud Platform zone to
            create the VM in. The fully qualified name of
            the zone must be specified, including the region
            name, for example "us-central1-b". If not
            specified, uses the "-b" zone of the destination
            Connection Profile's region.
        vm_subnet (str):
            Required. The name of the subnet the Compute
            instance will use for private connectivity. Must
            be supplied in the form of
            projects/{project}/regions/{region}/subnetworks/{subnetwork}.
            Note: the region for the subnet must match the
            Compute instance region.
    """

    migration_job: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vm_machine_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vm_zone: str = proto.Field(
        proto.STRING,
        number=4,
    )
    vm_subnet: str = proto.Field(
        proto.STRING,
        number=5,
    )


class TcpProxyScript(proto.Message):
    r"""Response message for 'GenerateTcpProxyScript' request.

    Attributes:
        script (str):
            The TCP Proxy configuration script.
    """

    script: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectionProfilesRequest(proto.Message):
    r"""Request message for 'ListConnectionProfiles' request.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of connection profiles.
        page_size (int):
            The maximum number of connection profiles to
            return. The service may return fewer than this
            value. If unspecified, at most 50 connection
            profiles will be returned. The maximum value is
            1000; values above 1000 are coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListConnectionProfiles`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListConnectionProfiles`` must match the call that provided
            the page token.
        filter (str):
            A filter expression that filters connection profiles listed
            in the response. The expression must specify the field name,
            a comparison operator, and the value that you want to use
            for filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be either =, !=, >, or
            <. For example, list connection profiles created this year
            by specifying **createTime %gt;
            2020-01-01T00:00:00.000000000Z**. You can also filter nested
            fields. For example, you could specify **mySql.username =
            %lt;my_username%gt;** to list all connection profiles
            configured to connect with a specific username.
        order_by (str):
            A comma-separated list of fields to order
            results according to.
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


class ListConnectionProfilesResponse(proto.Message):
    r"""Response message for 'ListConnectionProfiles' request.

    Attributes:
        connection_profiles (MutableSequence[google.cloud.clouddms_v1.types.ConnectionProfile]):
            The response list of connection profiles.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    connection_profiles: MutableSequence[clouddms_resources.ConnectionProfile] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=clouddms_resources.ConnectionProfile,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetConnectionProfileRequest(proto.Message):
    r"""Request message for 'GetConnectionProfile' request.

    Attributes:
        name (str):
            Required. Name of the connection profile
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConnectionProfileRequest(proto.Message):
    r"""Request message for 'CreateConnectionProfile' request.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of connection profiles.
        connection_profile_id (str):
            Required. The connection profile identifier.
        connection_profile (google.cloud.clouddms_v1.types.ConnectionProfile):
            Required. The create request body including
            the connection profile data
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two requests with the same ID, then the
            second request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        validate_only (bool):
            Optional. Only validate the connection
            profile, but don't create any resources. The
            default is false. Only supported for Oracle
            connection profiles.
        skip_validation (bool):
            Optional. Create the connection profile
            without validating it. The default is false.
            Only supported for Oracle connection profiles.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connection_profile: clouddms_resources.ConnectionProfile = proto.Field(
        proto.MESSAGE,
        number=3,
        message=clouddms_resources.ConnectionProfile,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    skip_validation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class UpdateConnectionProfileRequest(proto.Message):
    r"""Request message for 'UpdateConnectionProfile' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the
            fields to be overwritten by the update in the
            conversion workspace resource.
        connection_profile (google.cloud.clouddms_v1.types.ConnectionProfile):
            Required. The connection profile parameters
            to update.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two requests with the same ID, then the
            second request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        validate_only (bool):
            Optional. Only validate the connection
            profile, but don't update any resources. The
            default is false. Only supported for Oracle
            connection profiles.
        skip_validation (bool):
            Optional. Update the connection profile
            without validating it. The default is false.
            Only supported for Oracle connection profiles.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    connection_profile: clouddms_resources.ConnectionProfile = proto.Field(
        proto.MESSAGE,
        number=2,
        message=clouddms_resources.ConnectionProfile,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    skip_validation: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteConnectionProfileRequest(proto.Message):
    r"""Request message for 'DeleteConnectionProfile' request.

    Attributes:
        name (str):
            Required. Name of the connection profile
            resource to delete.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        force (bool):
            In case of force delete, the CloudSQL replica
            database is also deleted (only for CloudSQL
            connection profile).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CreatePrivateConnectionRequest(proto.Message):
    r"""Request message to create a new private connection in the
    specified project and region.

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of PrivateConnections.
        private_connection_id (str):
            Required. The private connection identifier.
        private_connection (google.cloud.clouddms_v1.types.PrivateConnection):
            Required. The private connection resource to
            create.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two requests with the same ID, then the
            second request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        skip_validation (bool):
            Optional. If set to true, will skip
            validations.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    private_connection: clouddms_resources.PrivateConnection = proto.Field(
        proto.MESSAGE,
        number=3,
        message=clouddms_resources.PrivateConnection,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    skip_validation: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListPrivateConnectionsRequest(proto.Message):
    r"""Request message to retrieve a list of private connections in
    a given project and location.

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of private connections.
        page_size (int):
            Maximum number of private connections to
            return. If unspecified, at most 50 private
            connections that are returned. The maximum value
            is 1000; values above 1000 are coerced to 1000.
        page_token (str):
            Page token received from a previous
            ``ListPrivateConnections`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListPrivateConnections`` must match the call that provided
            the page token.
        filter (str):
            A filter expression that filters private connections listed
            in the response. The expression must specify the field name,
            a comparison operator, and the value that you want to use
            for filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be either =, !=, >, or
            <. For example, list private connections created this year
            by specifying **createTime %gt;
            2021-01-01T00:00:00.000000000Z**.
        order_by (str):
            Order by fields for the result.
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


class ListPrivateConnectionsResponse(proto.Message):
    r"""Response message for 'ListPrivateConnections' request.

    Attributes:
        private_connections (MutableSequence[google.cloud.clouddms_v1.types.PrivateConnection]):
            List of private connections.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    private_connections: MutableSequence[clouddms_resources.PrivateConnection] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=clouddms_resources.PrivateConnection,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeletePrivateConnectionRequest(proto.Message):
    r"""Request message to delete a private connection.

    Attributes:
        name (str):
            Required. The name of the private connection
            to delete.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two requests with the same ID, then the
            second request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPrivateConnectionRequest(proto.Message):
    r"""Request message to get a private connection resource.

    Attributes:
        name (str):
            Required. The name of the private connection
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
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


class ListConversionWorkspacesRequest(proto.Message):
    r"""Retrieve a list of all conversion workspaces in a given
    project and location.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of conversion workspaces.
        page_size (int):
            The maximum number of conversion workspaces
            to return. The service may return fewer than
            this value. If unspecified, at most 50 sets are
            returned.
        page_token (str):
            The nextPageToken value received in the
            previous call to conversionWorkspaces.list, used
            in the subsequent request to retrieve the next
            page of results. On first call this should be
            left blank. When paginating, all other
            parameters provided to conversionWorkspaces.list
            must match the call that provided the page
            token.
        filter (str):
            A filter expression that filters conversion workspaces
            listed in the response. The expression must specify the
            field name, a comparison operator, and the value that you
            want to use for filtering. The value must be a string, a
            number, or a boolean. The comparison operator must be either
            =, !=, >, or <. For example, list conversion workspaces
            created this year by specifying **createTime %gt;
            2020-01-01T00:00:00.000000000Z.** You can also filter nested
            fields. For example, you could specify **source.version =
            "12.c.1"** to select all conversion workspaces with source
            database version equal to 12.c.1.
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


class ListConversionWorkspacesResponse(proto.Message):
    r"""Response message for 'ListConversionWorkspaces' request.

    Attributes:
        conversion_workspaces (MutableSequence[google.cloud.clouddms_v1.types.ConversionWorkspace]):
            The list of conversion workspace objects.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    conversion_workspaces: MutableSequence[
        conversionworkspace_resources.ConversionWorkspace
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=conversionworkspace_resources.ConversionWorkspace,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'GetConversionWorkspace' request.

    Attributes:
        name (str):
            Required. Name of the conversion workspace
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConversionWorkspaceRequest(proto.Message):
    r"""Request message to create a new Conversion Workspace
    in the specified project and region.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of conversion workspaces.
        conversion_workspace_id (str):
            Required. The ID of the conversion workspace
            to create.
        conversion_workspace (google.cloud.clouddms_v1.types.ConversionWorkspace):
            Required. Represents a conversion workspace
            object.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversion_workspace_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    conversion_workspace: conversionworkspace_resources.ConversionWorkspace = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=conversionworkspace_resources.ConversionWorkspace,
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'UpdateConversionWorkspace' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the
            fields to be overwritten by the update in the
            conversion workspace resource.
        conversion_workspace (google.cloud.clouddms_v1.types.ConversionWorkspace):
            Required. The conversion workspace parameters
            to update.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    conversion_workspace: conversionworkspace_resources.ConversionWorkspace = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=conversionworkspace_resources.ConversionWorkspace,
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'DeleteConversionWorkspace' request.

    Attributes:
        name (str):
            Required. Name of the conversion workspace
            resource to delete.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        force (bool):
            Force delete the conversion workspace, even
            if there's a running migration that is using the
            workspace.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CommitConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'CommitConversionWorkspace' request.

    Attributes:
        name (str):
            Required. Name of the conversion workspace
            resource to commit.
        commit_name (str):
            Optional. Optional name of the commit.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commit_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RollbackConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'RollbackConversionWorkspace' request.

    Attributes:
        name (str):
            Required. Name of the conversion workspace
            resource to roll back to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApplyConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'ApplyConversionWorkspace' request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the conversion workspace resource for
            which to apply the draft tree. Must be in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        filter (str):
            Filter which entities to apply. Leaving this
            field empty will apply all of the entities.
            Supports Google AIP 160 based filtering.
        dry_run (bool):
            Optional. Only validates the apply process,
            but doesn't change the destination database.
            Only works for PostgreSQL destination connection
            profile.
        auto_commit (bool):
            Optional. Specifies whether the conversion
            workspace is to be committed automatically after
            the apply.
        connection_profile (str):
            Optional. Fully qualified (Uri) name of the
            destination connection profile.

            This field is a member of `oneof`_ ``destination``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    auto_commit: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    connection_profile: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="destination",
    )


class ListMappingRulesRequest(proto.Message):
    r"""Retrieve a list of all mapping rules in a given conversion
    workspace.

    Attributes:
        parent (str):
            Required. Name of the conversion workspace resource whose
            mapping rules are listed in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        page_size (int):
            The maximum number of rules to return. The
            service may return fewer than this value.
        page_token (str):
            The nextPageToken value received in the
            previous call to mappingRules.list, used in the
            subsequent request to retrieve the next page of
            results. On first call this should be left
            blank. When paginating, all other parameters
            provided to mappingRules.list must match the
            call that provided the page token.
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


class ListMappingRulesResponse(proto.Message):
    r"""Response message for 'ListMappingRulesRequest' request.

    Attributes:
        mapping_rules (MutableSequence[google.cloud.clouddms_v1.types.MappingRule]):
            The list of conversion workspace mapping
            rules.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    mapping_rules: MutableSequence[conversionworkspace_resources.MappingRule] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=conversionworkspace_resources.MappingRule,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMappingRuleRequest(proto.Message):
    r"""Request message for 'GetMappingRule' request.

    Attributes:
        name (str):
            Required. Name of the mapping rule resource
            to get. Example:
            conversionWorkspaces/123/mappingRules/rule123

            In order to retrieve a previous revision of the
            mapping rule, also provide the revision ID.
            Example:

            conversionWorkspace/123/mappingRules/rule123@c7cfa2a8c7cfa2a8c7cfa2a8c7cfa2a8
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SeedConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'SeedConversionWorkspace' request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Name of the conversion workspace resource to seed with new
            database structure, in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        auto_commit (bool):
            Should the conversion workspace be committed
            automatically after the seed operation.
        source_connection_profile (str):
            Optional. Fully qualified (Uri) name of the
            source connection profile.

            This field is a member of `oneof`_ ``seed_from``.
        destination_connection_profile (str):
            Optional. Fully qualified (Uri) name of the
            destination connection profile.

            This field is a member of `oneof`_ ``seed_from``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auto_commit: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    source_connection_profile: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="seed_from",
    )
    destination_connection_profile: str = proto.Field(
        proto.STRING,
        number=101,
        oneof="seed_from",
    )


class ConvertConversionWorkspaceRequest(proto.Message):
    r"""Request message for 'ConvertConversionWorkspace' request.

    Attributes:
        name (str):
            Name of the conversion workspace resource to convert in the
            form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        auto_commit (bool):
            Optional. Specifies whether the conversion
            workspace is to be committed automatically after
            the conversion.
        filter (str):
            Optional. Filter the entities to convert.
            Leaving this field empty will convert all of the
            entities. Supports Google AIP-160 style
            filtering.
        convert_full_path (bool):
            Optional. Automatically convert the full
            entity path for each entity specified by the
            filter. For example, if the filter specifies a
            table, that table schema (and database if there
            is one) will also be converted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auto_commit: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    convert_full_path: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ImportMappingRulesRequest(proto.Message):
    r"""Request message for 'ImportMappingRules' request.

    Attributes:
        parent (str):
            Required. Name of the conversion workspace resource to
            import the rules to in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        rules_format (google.cloud.clouddms_v1.types.ImportRulesFileFormat):
            Required. The format of the rules content
            file.
        rules_files (MutableSequence[google.cloud.clouddms_v1.types.ImportMappingRulesRequest.RulesFile]):
            Required. One or more rules files.
        auto_commit (bool):
            Required. Should the conversion workspace be
            committed automatically after the import
            operation.
    """

    class RulesFile(proto.Message):
        r"""Details of a single rules file.

        Attributes:
            rules_source_filename (str):
                Required. The filename of the rules that
                needs to be converted. The filename is used
                mainly so that future logs of the import rules
                job contain it, and can therefore be searched by
                it.
            rules_content (str):
                Required. The text content of the rules that
                needs to be converted.
        """

        rules_source_filename: str = proto.Field(
            proto.STRING,
            number=1,
        )
        rules_content: str = proto.Field(
            proto.STRING,
            number=2,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rules_format: conversionworkspace_resources.ImportRulesFileFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=conversionworkspace_resources.ImportRulesFileFormat,
    )
    rules_files: MutableSequence[RulesFile] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=RulesFile,
    )
    auto_commit: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class DescribeDatabaseEntitiesRequest(proto.Message):
    r"""Request message for 'DescribeDatabaseEntities' request.

    Attributes:
        conversion_workspace (str):
            Required. Name of the conversion workspace resource whose
            database entities are described. Must be in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        page_size (int):
            Optional. The maximum number of entities to
            return. The service may return fewer entities
            than the value specifies.
        page_token (str):
            Optional. The nextPageToken value received in
            the previous call to
            conversionWorkspace.describeDatabaseEntities,
            used in the subsequent request to retrieve the
            next page of results. On first call this should
            be left blank. When paginating, all other
            parameters provided to
            conversionWorkspace.describeDatabaseEntities
            must match the call that provided the page
            token.
        tree (google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesRequest.DBTreeType):
            Required. The tree to fetch.
        uncommitted (bool):
            Optional. Whether to retrieve the latest committed version
            of the entities or the latest version. This field is ignored
            if a specific commit_id is specified.
        commit_id (str):
            Optional. Request a specific commit ID. If
            not specified, the entities from the latest
            commit are returned.
        filter (str):
            Optional. Filter the returned entities based
            on AIP-160 standard.
        view (google.cloud.clouddms_v1.types.DatabaseEntityView):
            Optional. Results view based on AIP-157
    """

    class DBTreeType(proto.Enum):
        r"""The type of a tree to return

        Values:
            DB_TREE_TYPE_UNSPECIFIED (0):
                Unspecified tree type.
            SOURCE_TREE (1):
                The source database tree.
            DRAFT_TREE (2):
                The draft database tree.
            DESTINATION_TREE (3):
                The destination database tree.
        """

        DB_TREE_TYPE_UNSPECIFIED = 0
        SOURCE_TREE = 1
        DRAFT_TREE = 2
        DESTINATION_TREE = 3

    conversion_workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    tree: DBTreeType = proto.Field(
        proto.ENUM,
        number=6,
        enum=DBTreeType,
    )
    uncommitted: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    commit_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=13,
    )
    view: "DatabaseEntityView" = proto.Field(
        proto.ENUM,
        number=14,
        enum="DatabaseEntityView",
    )


class DescribeDatabaseEntitiesResponse(proto.Message):
    r"""Response message for 'DescribeDatabaseEntities' request.

    Attributes:
        database_entities (MutableSequence[google.cloud.clouddms_v1.types.DatabaseEntity]):
            The list of database entities for the
            conversion workspace.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    database_entities: MutableSequence[conversionworkspace_resources.DatabaseEntity] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=conversionworkspace_resources.DatabaseEntity,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchBackgroundJobsRequest(proto.Message):
    r"""Request message for 'SearchBackgroundJobs' request.

    Attributes:
        conversion_workspace (str):
            Required. Name of the conversion workspace resource whose
            jobs are listed, in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        return_most_recent_per_job_type (bool):
            Optional. Whether or not to return just the
            most recent job per job type,
        max_size (int):
            Optional. The maximum number of jobs to
            return. The service may return fewer than this
            value. If unspecified, at most 100 jobs are
            returned. The maximum value is 100; values above
            100 are coerced to 100.
        completed_until_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. If provided, only returns jobs that
            completed until (not including) the given
            timestamp.
    """

    conversion_workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    return_most_recent_per_job_type: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    max_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    completed_until_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class SearchBackgroundJobsResponse(proto.Message):
    r"""Response message for 'SearchBackgroundJobs' request.

    Attributes:
        jobs (MutableSequence[google.cloud.clouddms_v1.types.BackgroundJobLogEntry]):
            The list of conversion workspace mapping
            rules.
    """

    jobs: MutableSequence[conversionworkspace_resources.BackgroundJobLogEntry] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=conversionworkspace_resources.BackgroundJobLogEntry,
        )
    )


class DescribeConversionWorkspaceRevisionsRequest(proto.Message):
    r"""Request message for 'DescribeConversionWorkspaceRevisions'
    request.

    Attributes:
        conversion_workspace (str):
            Required. Name of the conversion workspace resource whose
            revisions are listed. Must be in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        commit_id (str):
            Optional. Optional filter to request a
            specific commit ID.
    """

    conversion_workspace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    commit_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DescribeConversionWorkspaceRevisionsResponse(proto.Message):
    r"""Response message for 'DescribeConversionWorkspaceRevisions'
    request.

    Attributes:
        revisions (MutableSequence[google.cloud.clouddms_v1.types.ConversionWorkspace]):
            The list of conversion workspace revisions.
    """

    revisions: MutableSequence[conversionworkspace_resources.ConversionWorkspace] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=conversionworkspace_resources.ConversionWorkspace,
        )
    )


class CreateMappingRuleRequest(proto.Message):
    r"""Request message for 'CreateMappingRule' command.

    Attributes:
        parent (str):
            Required. The parent which owns this
            collection of mapping rules.
        mapping_rule_id (str):
            Required. The ID of the rule to create.
        mapping_rule (google.cloud.clouddms_v1.types.MappingRule):
            Required. Represents a [mapping rule]
            (https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules)
            object.
        request_id (str):
            A unique ID used to identify the request. If the server
            receives two requests with the same ID, then the second
            request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mapping_rule_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mapping_rule: conversionworkspace_resources.MappingRule = proto.Field(
        proto.MESSAGE,
        number=3,
        message=conversionworkspace_resources.MappingRule,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteMappingRuleRequest(proto.Message):
    r"""Request message for 'DeleteMappingRule' request.

    Attributes:
        name (str):
            Required. Name of the mapping rule resource
            to delete.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two requests with the same ID, then the
            second request is ignored.

            It is recommended to always set this value to a UUID.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchStaticIpsRequest(proto.Message):
    r"""Request message for 'FetchStaticIps' request.

    Attributes:
        name (str):
            Required. The resource name for the location for which
            static IPs should be returned. Must be in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of IPs to return.
        page_token (str):
            A page token, received from a previous ``FetchStaticIps``
            call.
    """

    name: str = proto.Field(
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


class FetchStaticIpsResponse(proto.Message):
    r"""Response message for a 'FetchStaticIps' request.

    Attributes:
        static_ips (MutableSequence[str]):
            List of static IPs.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    static_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
