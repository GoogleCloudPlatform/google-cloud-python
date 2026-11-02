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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.redis.cluster.v1beta1",
    manifest={
        "PscConnectionStatus",
        "AuthorizationMode",
        "NodeType",
        "TransitEncryptionMode",
        "ServerCaMode",
        "ConnectionType",
        "CreateClusterRequest",
        "CreateAclPolicyRequest",
        "ListClustersRequest",
        "ListClustersResponse",
        "ListAclPoliciesRequest",
        "ListAclPoliciesResponse",
        "ListAclPolicyRevisionsRequest",
        "ListAclPolicyRevisionsResponse",
        "UpdateClusterRequest",
        "UpdateAclPolicyRequest",
        "GetClusterRequest",
        "GetAclPolicyRequest",
        "GetAclPolicyRevisionRequest",
        "DeleteClusterRequest",
        "DeleteAclPolicyRequest",
        "GetClusterCertificateAuthorityRequest",
        "ListBackupCollectionsRequest",
        "ListBackupCollectionsResponse",
        "GetBackupCollectionRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "DeleteBackupRequest",
        "ExportBackupRequest",
        "BackupClusterRequest",
        "ListTokenAuthUsersRequest",
        "ListTokenAuthUsersResponse",
        "GetTokenAuthUserRequest",
        "ListAuthTokensRequest",
        "ListAuthTokensResponse",
        "GetAuthTokenRequest",
        "AddTokenAuthUserRequest",
        "DeleteTokenAuthUserRequest",
        "AddAuthTokenRequest",
        "DeleteAuthTokenRequest",
        "Cluster",
        "AclPolicyInfo",
        "AclPolicy",
        "AclPolicyRevisionStatus",
        "ClusterAclPolicyAttachment",
        "AclPolicyRevision",
        "AclRule",
        "AutomatedBackupConfig",
        "BackupCollection",
        "Backup",
        "BackupFile",
        "PscServiceAttachment",
        "CrossClusterReplicationConfig",
        "ClusterMaintenancePolicy",
        "ClusterWeeklyMaintenanceWindow",
        "ClusterMaintenanceSchedule",
        "PscConfig",
        "DiscoveryEndpoint",
        "PscConnection",
        "ClusterEndpoint",
        "ConnectionDetail",
        "PscAutoConnection",
        "SharedRegionalCertificateAuthority",
        "GetSharedRegionalCertificateAuthorityRequest",
        "OperationMetadata",
        "TokenAuthUser",
        "AuthToken",
        "CertificateAuthority",
        "ClusterPersistenceConfig",
        "ZoneDistributionConfig",
        "RescheduleClusterMaintenanceRequest",
        "EncryptionInfo",
    },
)


class PscConnectionStatus(proto.Enum):
    r"""Status of the PSC connection.

    Values:
        PSC_CONNECTION_STATUS_UNSPECIFIED (0):
            PSC connection status is not specified.
        PSC_CONNECTION_STATUS_ACTIVE (1):
            The connection is active
        PSC_CONNECTION_STATUS_NOT_FOUND (2):
            Connection not found
    """

    PSC_CONNECTION_STATUS_UNSPECIFIED = 0
    PSC_CONNECTION_STATUS_ACTIVE = 1
    PSC_CONNECTION_STATUS_NOT_FOUND = 2


class AuthorizationMode(proto.Enum):
    r"""Available authorization mode of a Redis cluster.

    Values:
        AUTH_MODE_UNSPECIFIED (0):
            Not set.
        AUTH_MODE_IAM_AUTH (1):
            IAM basic authorization mode
        AUTH_MODE_DISABLED (2):
            Authorization disabled mode
        AUTH_MODE_TOKEN_AUTH (3):
            Token based authorization mode
    """

    AUTH_MODE_UNSPECIFIED = 0
    AUTH_MODE_IAM_AUTH = 1
    AUTH_MODE_DISABLED = 2
    AUTH_MODE_TOKEN_AUTH = 3


class NodeType(proto.Enum):
    r"""NodeType of a redis cluster node,

    Values:
        NODE_TYPE_UNSPECIFIED (0):
            Node type unspecified
        REDIS_SHARED_CORE_NANO (1):
            Redis shared core nano node_type.
        REDIS_HIGHMEM_MEDIUM (2):
            Redis highmem medium node_type.
        REDIS_HIGHMEM_XLARGE (3):
            Redis highmem xlarge node_type.
        REDIS_STANDARD_SMALL (4):
            Redis standard small node_type.
        REDIS_HIGHCPU_MEDIUM (7):
            Redis highcpu medium node_type.
        REDIS_STANDARD_LARGE (8):
            Redis standard large node_type.
        REDIS_HIGHMEM_2XLARGE (9):
            Redis highmem 2xlarge node_type.
    """

    NODE_TYPE_UNSPECIFIED = 0
    REDIS_SHARED_CORE_NANO = 1
    REDIS_HIGHMEM_MEDIUM = 2
    REDIS_HIGHMEM_XLARGE = 3
    REDIS_STANDARD_SMALL = 4
    REDIS_HIGHCPU_MEDIUM = 7
    REDIS_STANDARD_LARGE = 8
    REDIS_HIGHMEM_2XLARGE = 9


class TransitEncryptionMode(proto.Enum):
    r"""Available mode of in-transit encryption.

    Values:
        TRANSIT_ENCRYPTION_MODE_UNSPECIFIED (0):
            In-transit encryption not set.
        TRANSIT_ENCRYPTION_MODE_DISABLED (1):
            In-transit encryption disabled.
        TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION (2):
            Use server managed encryption for in-transit
            encryption.
    """

    TRANSIT_ENCRYPTION_MODE_UNSPECIFIED = 0
    TRANSIT_ENCRYPTION_MODE_DISABLED = 1
    TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION = 2


class ServerCaMode(proto.Enum):
    r"""Server CA mode for the cluster.

    Values:
        SERVER_CA_MODE_UNSPECIFIED (0):
            Server CA mode not specified.
        SERVER_CA_MODE_GOOGLE_MANAGED_PER_INSTANCE_CA (1):
            Each cluster has its own Google managed CA.
        SERVER_CA_MODE_GOOGLE_MANAGED_SHARED_CA (2):
            The cluster uses Google managed shared CA in
            the region.
        SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA (3):
            The cluster uses customer managed CA from
            CAS.
    """

    SERVER_CA_MODE_UNSPECIFIED = 0
    SERVER_CA_MODE_GOOGLE_MANAGED_PER_INSTANCE_CA = 1
    SERVER_CA_MODE_GOOGLE_MANAGED_SHARED_CA = 2
    SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA = 3


class ConnectionType(proto.Enum):
    r"""Type of a PSC connection, for cluster access purpose.

    Values:
        CONNECTION_TYPE_UNSPECIFIED (0):
            Cluster endpoint Type is not set
        CONNECTION_TYPE_DISCOVERY (1):
            Cluster endpoint that will be used as for
            cluster topology discovery.
        CONNECTION_TYPE_PRIMARY (2):
            Cluster endpoint that will be used as primary
            endpoint to access primary.
        CONNECTION_TYPE_READER (3):
            Cluster endpoint that will be used as reader
            endpoint to access replicas.
    """

    CONNECTION_TYPE_UNSPECIFIED = 0
    CONNECTION_TYPE_DISCOVERY = 1
    CONNECTION_TYPE_PRIMARY = 2
    CONNECTION_TYPE_READER = 3


class CreateClusterRequest(proto.Message):
    r"""Request for [CreateCluster][CloudRedis.CreateCluster].

    Attributes:
        parent (str):
            Required. The resource name of the cluster location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a GCP region.
        cluster_id (str):
            Required. The logical name of the Redis cluster in the
            customer project with the following restrictions:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the customer project / location
        cluster (google.cloud.redis_cluster_v1beta1.types.Cluster):
            Required. The cluster that is to be created.
        request_id (str):
            Idempotent request UUID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Cluster",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateAclPolicyRequest(proto.Message):
    r"""Request for ``CreateAclPolicy``.

    Attributes:
        parent (str):
            Required. The resource name of the cluster location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a Google Cloud region.
        acl_policy_id (str):
            Required. The logical name of the ACL policy in the customer
            project with the following restrictions:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the customer project / location
        acl_policy (google.cloud.redis_cluster_v1beta1.types.AclPolicy):
            Required. The ACL policy that is to be
            created.
        request_id (str):
            Optional. Idempotent request UUID.
            .
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    acl_policy: "AclPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AclPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListClustersRequest(proto.Message):
    r"""Request for [ListClusters][CloudRedis.ListClusters].

    Attributes:
        parent (str):
            Required. The resource name of the cluster location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a GCP region.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.cluster.v1beta1.ListClustersResponse.next_page_token]
            to determine if there are more clusters left to be queried.
        page_token (str):
            The ``next_page_token`` value returned from a previous
            [ListClusters][CloudRedis.ListClusters] request, if any.
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


class ListClustersResponse(proto.Message):
    r"""Response for [ListClusters][CloudRedis.ListClusters].

    Attributes:
        clusters (MutableSequence[google.cloud.redis_cluster_v1beta1.types.Cluster]):
            A list of Redis clusters in the project in the specified
            location, or across all locations.

            If the ``location_id`` in the parent field of the request is
            "-", all regions available to the project are queried, and
            the results aggregated. If in such an aggregated query a
            location is unavailable, a placeholder Redis entry is
            included in the response with the ``name`` field set to a
            value of the form
            ``projects/{project_id}/locations/{location_id}/clusters/``-
            and the ``status`` field set to ERROR and ``status_message``
            field set to "location not available for ListClusters".
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence["Cluster"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Cluster",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListAclPoliciesRequest(proto.Message):
    r"""Request for ``ListAclPolicies``.

    Attributes:
        parent (str):
            Required. The resource name of the ACL policy location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.cluster.v1beta1.ListAclPoliciesResponse.next_page_token]
            to determine if there are more ACL policies left to be
            queried.

            The maximum value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListAclPolicies`` request, if any.
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


class ListAclPoliciesResponse(proto.Message):
    r"""Response for ``ListAclPolicies``.

    Attributes:
        acl_policies (MutableSequence[google.cloud.redis_cluster_v1beta1.types.AclPolicy]):
            A list of ACL policies in the project in the specified
            location, or across all locations.

            If the ``location_id`` in the parent field of the request is
            "-", all regions available to the project are queried, and
            the results aggregated.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    acl_policies: MutableSequence["AclPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AclPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListAclPolicyRevisionsRequest(proto.Message):
    r"""Request for ``ListAclPolicyRevisions``.

    Attributes:
        parent (str):
            Required. The name of the ACL policy to list revisions for.
            Format:
            "projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}".
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListAclPolicyRevisions`` request, if any.
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


class ListAclPolicyRevisionsResponse(proto.Message):
    r"""Response for ``ListAclPolicyRevisions``.

    Attributes:
        acl_policy_revisions (MutableSequence[google.cloud.redis_cluster_v1beta1.types.AclPolicyRevision]):
            A list of ACL policy revisions.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    acl_policy_revisions: MutableSequence["AclPolicyRevision"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AclPolicyRevision",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateClusterRequest(proto.Message):
    r"""Request for [UpdateCluster][CloudRedis.UpdateCluster].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field may only include these fields from
            [Cluster][google.cloud.redis.cluster.v1beta1.Cluster]:

            - ``size_gb``
            - ``replica_count``
        cluster (google.cloud.redis_cluster_v1beta1.types.Cluster):
            Required. Update description. Only fields specified in
            update_mask are updated.
        request_id (str):
            Idempotent request UUID.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Cluster",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateAclPolicyRequest(proto.Message):
    r"""Request for ``UpdateAclPolicy``.

    Attributes:
        acl_policy (google.cloud.redis_cluster_v1beta1.types.AclPolicy):
            Required. The ACL policy to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to be updated. At least one path
            must be supplied in this field. The elements of the repeated
            paths field may only include these fields from
            ``AclPolicy``:

            - ``rules``
        request_id (str):
            Optional. Idempotent request UUID.
    """

    acl_policy: "AclPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AclPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetClusterRequest(proto.Message):
    r"""Request for [GetCluster][CloudRedis.GetCluster].

    Attributes:
        name (str):
            Required. Redis cluster resource name using the form:
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
            where ``location_id`` refers to a GCP region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAclPolicyRequest(proto.Message):
    r"""Request for ``GetAclPolicy``.

    Attributes:
        name (str):
            Required. Redis ACL policy resource name using the form:
            ``projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}``
            where ``location_id`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAclPolicyRevisionRequest(proto.Message):
    r"""Request for ``GetAclPolicyRevision``.

    Attributes:
        name (str):
            Required. Redis ACL policy revision resource name using the
            form:
            ``projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}/revisions/{revision_id}``
            where ``location_id`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteClusterRequest(proto.Message):
    r"""Request for [DeleteCluster][CloudRedis.DeleteCluster].

    Attributes:
        name (str):
            Required. Redis cluster resource name using the form:
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
            where ``location_id`` refers to a GCP region.
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAclPolicyRequest(proto.Message):
    r"""Request for ``DeleteAclPolicy``.

    Attributes:
        name (str):
            Required. Redis ACL policy resource name using the form:
            ``projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}``
            where ``location_id`` refers to a Google Cloud region.
        request_id (str):
            Optional. Idempotent request UUID.
        etag (str):
            Optional. Etag of the ACL policy. If this is
            different from the server's etag, the request
            will fail with an ABORTED error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetClusterCertificateAuthorityRequest(proto.Message):
    r"""Request for
    [GetClusterCertificateAuthorityRequest][CloudRedis.GetClusterCertificateAuthorityRequest].

    Attributes:
        name (str):
            Required. Redis cluster certificate authority resource name
            using the form:
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}/certificateAuthority``
            where ``location_id`` refers to a GCP region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupCollectionsRequest(proto.Message):
    r"""Request for [ListBackupCollections]

    Attributes:
        parent (str):
            Required. The resource name of the backupCollection location
            using the form:
            ``projects/{project_id}/locations/{location_id}`` where
            ``location_id`` refers to a GCP region.
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.cluster.v1beta1.ListBackupCollectionsResponse.next_page_token]
            to determine if there are more clusters left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous [ListBackupCollections] request, if any.
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


class ListBackupCollectionsResponse(proto.Message):
    r"""Response for [ListBackupCollections].

    Attributes:
        backup_collections (MutableSequence[google.cloud.redis_cluster_v1beta1.types.BackupCollection]):
            A list of backupCollections in the project.

            If the ``location_id`` in the parent field of the request is
            "-", all regions available to the project are queried, and
            the results aggregated. If in such an aggregated query a
            location is unavailable, a placeholder backupCollection
            entry is included in the response with the ``name`` field
            set to a value of the form
            ``projects/{project_id}/locations/{location_id}/backupCollections/``-
            and the ``status`` field set to ERROR and ``status_message``
            field set to "location not available for
            ListBackupCollections".
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_collections: MutableSequence["BackupCollection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupCollection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupCollectionRequest(proto.Message):
    r"""Request for [GetBackupCollection].

    Attributes:
        name (str):
            Required. Redis backupCollection resource name using the
            form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}``
            where ``location_id`` refers to a GCP region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupsRequest(proto.Message):
    r"""Request for [ListBackups].

    Attributes:
        parent (str):
            Required. The resource name of the backupCollection using
            the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}``
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.cluster.v1beta1.ListBackupsResponse.next_page_token]
            to determine if there are more clusters left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous [ListBackupCollections] request, if any.
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


class ListBackupsResponse(proto.Message):
    r"""Response for [ListBackups].

    Attributes:
        backups (MutableSequence[google.cloud.redis_cluster_v1beta1.types.Backup]):
            A list of backups in the project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Backups that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence["Backup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Backup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupRequest(proto.Message):
    r"""Request for [GetBackup].

    Attributes:
        name (str):
            Required. Redis backup resource name using the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteBackupRequest(proto.Message):
    r"""Request for [DeleteBackup].

    Attributes:
        name (str):
            Required. Redis backup resource name using the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``
        request_id (str):
            Optional. Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExportBackupRequest(proto.Message):
    r"""Request for [ExportBackup].

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_bucket (str):
            Google Cloud Storage bucket, like
            "my-bucket".

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. Redis backup resource name using the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``
    """

    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="destination",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BackupClusterRequest(proto.Message):
    r"""Request for [BackupCluster].

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Redis cluster resource name using the form:
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
            where ``location_id`` refers to a GCP region.
        ttl (google.protobuf.duration_pb2.Duration):
            Optional. TTL for the backup to expire. Value
            range is 1 day to 100 years. If not specified,
            the default value is 100 years.
        backup_id (str):
            Optional. The id of the backup to be created. If not
            specified, the default value ([YYYYMMDDHHMMSS]\_[Shortened
            Cluster UID] is used.

            This field is a member of `oneof`_ ``_backup_id``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class ListTokenAuthUsersRequest(proto.Message):
    r"""Request message for [ListTokenAuthUsers][].

    Attributes:
        parent (str):
            Required. The parent resource that this token
            based auth user will be listed for. Format:

            projects/{project}/locations/{location}/clusters/{cluster}
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's The maximum value is 1000; values above 1000 will
            be coerced to 1000.
            [``next_page_token``][google.cloud.redis.cluster.v1beta1.ListTokenAuthUsersResponse.next_page_token]
            to determine if there are more clusters left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous [ListTokenAuthUsers] request, if any.
        filter (str):
            Optional. Expression for filtering results.
        order_by (str):
            Optional. Sort results by a defined order.
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


class ListTokenAuthUsersResponse(proto.Message):
    r"""Response message for [ListTokenAuthUsers][].

    Attributes:
        token_auth_users (MutableSequence[google.cloud.redis_cluster_v1beta1.types.TokenAuthUser]):
            A list of token auth users in the project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Token auth users that could
            not be reached.
    """

    @property
    def raw_page(self):
        return self

    token_auth_users: MutableSequence["TokenAuthUser"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TokenAuthUser",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTokenAuthUserRequest(proto.Message):
    r"""Request message for [GetTokenAuthUser][].

    Attributes:
        name (str):
            Required. The name of token auth user for a token based auth
            enabled cluster. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAuthTokensRequest(proto.Message):
    r"""Request message for [ListAuthTokens][].

    Attributes:
        parent (str):
            Required. The parent resource that this auth token will be
            listed for. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}
        page_size (int):
            Optional. The maximum number of items to return. The maximum
            value is 1000; values above 1000 will be coerced to 1000. If
            not specified, a default value of 1000 will be used by the
            service. Regardless of the page_size value, the response may
            include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.cluster.v1beta1.ListTokenAuthUsersResponse.next_page_token]
            to determine if there are more clusters left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous [ListTokenAuthUsers] request, if any.
        filter (str):
            Optional. Expression for filtering results.
        order_by (str):
            Optional. Sort results by a defined order.
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


class ListAuthTokensResponse(proto.Message):
    r"""Response message for [ListAuthTokens][].

    Attributes:
        auth_tokens (MutableSequence[google.cloud.redis_cluster_v1beta1.types.AuthToken]):
            A list of auth tokens in the project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Auth tokens that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    auth_tokens: MutableSequence["AuthToken"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuthToken",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAuthTokenRequest(proto.Message):
    r"""Request message for [GetAuthToken][].

    Attributes:
        name (str):
            Required. The name of auth token for a token based auth
            enabled cluster. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AddTokenAuthUserRequest(proto.Message):
    r"""Request message for [AddTokenAuthUser][].

    Attributes:
        cluster (str):
            Required. The cluster resource that this
            token auth user will be added for. Format:
            projects/{project}/locations/{location}/clusters/{cluster}
        token_auth_user (str):
            Required. The id of the token auth user to
            add.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    token_auth_user: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteTokenAuthUserRequest(proto.Message):
    r"""Request message for [DeleteTokenAuthUser][].

    Attributes:
        name (str):
            Required. The name of the token auth user to delete. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}
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
        force (bool):
            Optional. If set to true, any child auth
            tokens of this user will also be deleted.
            Otherwise, the request will only work if the
            user has no auth tokens.
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


class AddAuthTokenRequest(proto.Message):
    r"""Request message for [AddAuthToken][].

    Attributes:
        token_auth_user (str):
            Required. The name of the token auth user resource that this
            auth token will be added for. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}
        auth_token (google.cloud.redis_cluster_v1beta1.types.AuthToken):
            Required. The auth token to add.
    """

    token_auth_user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auth_token: "AuthToken" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthToken",
    )


class DeleteAuthTokenRequest(proto.Message):
    r"""Request message for [DeleteAuthToken][].

    Attributes:
        name (str):
            Required. The name of the token auth user resource that this
            auth token will be deleted from. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Cluster(proto.Message):
    r"""A cluster instance.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.redis_cluster_v1beta1.types.Cluster.GcsBackupSource):
            Optional. Backups stored in Cloud Storage
            buckets. The Cloud Storage buckets need to be
            the same region as the clusters. Read permission
            is required to import from the provided Cloud
            Storage objects.

            This field is a member of `oneof`_ ``import_sources``.
        managed_backup_source (google.cloud.redis_cluster_v1beta1.types.Cluster.ManagedBackupSource):
            Optional. Backups generated and managed by
            memorystore service.

            This field is a member of `oneof`_ ``import_sources``.
        name (str):
            Required. Identifier. Unique name of the resource in this
            scope including project and location using the form:
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp associated with
            the cluster creation request.
        state (google.cloud.redis_cluster_v1beta1.types.Cluster.State):
            Output only. The current state of this
            cluster. Can be CREATING, READY, UPDATING,
            DELETING and SUSPENDED
        uid (str):
            Output only. System assigned, unique
            identifier for the cluster.
        replica_count (int):
            Optional. The number of replica nodes per
            shard.

            This field is a member of `oneof`_ ``_replica_count``.
        authorization_mode (google.cloud.redis_cluster_v1beta1.types.AuthorizationMode):
            Optional. The authorization mode of the Redis
            cluster. If not provided, auth feature is
            disabled for the cluster.
        transit_encryption_mode (google.cloud.redis_cluster_v1beta1.types.TransitEncryptionMode):
            Optional. The in-transit encryption for the
            Redis cluster. If not provided, encryption  is
            disabled for the cluster.
        size_gb (int):
            Output only. Redis memory size in GB for the
            entire cluster rounded up to the next integer.

            This field is a member of `oneof`_ ``_size_gb``.
        shard_count (int):
            Optional. Number of shards for the Redis
            cluster.

            This field is a member of `oneof`_ ``_shard_count``.
        psc_configs (MutableSequence[google.cloud.redis_cluster_v1beta1.types.PscConfig]):
            Optional. Each PscConfig configures the
            consumer network where IPs will be designated to
            the cluster for client access through Private
            Service Connect Automation. Currently, only one
            PscConfig is supported.
        discovery_endpoints (MutableSequence[google.cloud.redis_cluster_v1beta1.types.DiscoveryEndpoint]):
            Output only. Endpoints created on each given
            network, for Redis clients to connect to the
            cluster. Currently only one discovery endpoint
            is supported.
        psc_connections (MutableSequence[google.cloud.redis_cluster_v1beta1.types.PscConnection]):
            Output only. The list of PSC connections that
            are auto-created through service connectivity
            automation.
        state_info (google.cloud.redis_cluster_v1beta1.types.Cluster.StateInfo):
            Output only. Additional information about the
            current state of the cluster.
        node_type (google.cloud.redis_cluster_v1beta1.types.NodeType):
            Optional. The type of a redis node in the
            cluster. NodeType determines the underlying
            machine-type of a redis node.
        persistence_config (google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig):
            Optional. Persistence config (RDB, AOF) for
            the cluster.
        redis_configs (MutableMapping[str, str]):
            Optional. Key/Value pairs of customer
            overrides for mutable Redis Configs
        precise_size_gb (float):
            Output only. Precise value of redis memory
            size in GB for the entire cluster.

            This field is a member of `oneof`_ ``_precise_size_gb``.
        zone_distribution_config (google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig):
            Optional. This config will be used to
            determine how the customer wants us to
            distribute cluster resources within the region.
        cross_cluster_replication_config (google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig):
            Optional. Cross cluster replication config.
        deletion_protection_enabled (bool):
            Optional. The delete operation will fail when
            the value is set to true.

            This field is a member of `oneof`_ ``_deletion_protection_enabled``.
        maintenance_policy (google.cloud.redis_cluster_v1beta1.types.ClusterMaintenancePolicy):
            Optional. ClusterMaintenancePolicy determines
            when to allow or deny updates.

            This field is a member of `oneof`_ ``_maintenance_policy``.
        maintenance_schedule (google.cloud.redis_cluster_v1beta1.types.ClusterMaintenanceSchedule):
            Output only. ClusterMaintenanceSchedule
            Output only Published maintenance schedule.

            This field is a member of `oneof`_ ``_maintenance_schedule``.
        psc_service_attachments (MutableSequence[google.cloud.redis_cluster_v1beta1.types.PscServiceAttachment]):
            Output only. Service attachment details to
            configure Psc connections
        cluster_endpoints (MutableSequence[google.cloud.redis_cluster_v1beta1.types.ClusterEndpoint]):
            Optional. A list of cluster enpoints.
        backup_collection (str):
            Optional. Output only. The backup collection
            full resource name. Example:
            projects/{project}/locations/{location}/backupCollections/{collection}

            This field is a member of `oneof`_ ``_backup_collection``.
        kms_key (str):
            Optional. The KMS key used to encrypt the
            at-rest data of the cluster.

            This field is a member of `oneof`_ ``_kms_key``.
        automated_backup_config (google.cloud.redis_cluster_v1beta1.types.AutomatedBackupConfig):
            Optional. The automated backup config for the
            cluster.
        encryption_info (google.cloud.redis_cluster_v1beta1.types.EncryptionInfo):
            Output only. Encryption information of the
            data at rest of the cluster.
        async_cluster_endpoints_deletion_enabled (bool):
            Optional. If true, cluster endpoints that are
            created and registered by customers can be
            deleted asynchronously. That is, such a cluster
            endpoint can be de-registered before the
            forwarding rules in the cluster endpoint are
            deleted.

            This field is a member of `oneof`_ ``_async_cluster_endpoints_deletion_enabled``.
        server_ca_mode (google.cloud.redis_cluster_v1beta1.types.ServerCaMode):
            Optional. Server CA mode for the cluster.

            This field is a member of `oneof`_ ``_server_ca_mode``.
        server_ca_pool (str):
            Optional. Customer-managed CA pool for the cluster. Only
            applicable for BYOCA i.e. if server_ca_mode is
            SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format:
            "projects/{project}/locations/{region}/caPools/{ca_pool}".

            This field is a member of `oneof`_ ``_server_ca_pool``.
        rotate_server_certificate (bool):
            Optional. Input only. Rotate the server
            certificates.

            This field is a member of `oneof`_ ``_rotate_server_certificate``.
        acl_policy (str):
            Optional. The ACL policy to be applied to the
            cluster.
        acl_policy_info (google.cloud.redis_cluster_v1beta1.types.AclPolicyInfo):
            Output only. Details of the applied ACL
            policy.
    """

    class State(proto.Enum):
        r"""Represents the different states of a Redis cluster.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                Redis cluster is being created.
            ACTIVE (2):
                Redis cluster has been created and is fully
                usable.
            UPDATING (3):
                Redis cluster configuration is being updated.
            DELETING (4):
                Redis cluster is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4

    class StateInfo(proto.Message):
        r"""Represents additional information about the state of the
        cluster.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            update_info (google.cloud.redis_cluster_v1beta1.types.Cluster.StateInfo.UpdateInfo):
                Describes ongoing update on the cluster when
                cluster state is UPDATING.

                This field is a member of `oneof`_ ``info``.
        """

        class UpdateInfo(proto.Message):
            r"""Represents information about an updating cluster.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                target_shard_count (int):
                    Target number of shards for redis cluster

                    This field is a member of `oneof`_ ``_target_shard_count``.
                target_replica_count (int):
                    Target number of replica nodes per shard.

                    This field is a member of `oneof`_ ``_target_replica_count``.
            """

            target_shard_count: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            target_replica_count: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )

        update_info: "Cluster.StateInfo.UpdateInfo" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="info",
            message="Cluster.StateInfo.UpdateInfo",
        )

    class GcsBackupSource(proto.Message):
        r"""Backups stored in Cloud Storage buckets.
        The Cloud Storage buckets need to be the same region as the
        clusters.

        Attributes:
            uris (MutableSequence[str]):
                Optional. URIs of the GCS objects to import.
                Example: gs://bucket1/object1,
                gs://bucket2/folder2/object2
        """

        uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class ManagedBackupSource(proto.Message):
        r"""Backups that generated and managed by memorystore.

        Attributes:
            backup (str):
                Optional. Example:
                //redis.googleapis.com/projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup}
                A shorter version (without the prefix) of the backup name is
                also supported, like
                projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup_id}
                In this case, it assumes the backup is under
                redis.googleapis.com.
        """

        backup: str = proto.Field(
            proto.STRING,
            number=1,
        )

    gcs_source: GcsBackupSource = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="import_sources",
        message=GcsBackupSource,
    )
    managed_backup_source: ManagedBackupSource = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="import_sources",
        message=ManagedBackupSource,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=5,
    )
    replica_count: int = proto.Field(
        proto.INT32,
        number=8,
        optional=True,
    )
    authorization_mode: "AuthorizationMode" = proto.Field(
        proto.ENUM,
        number=11,
        enum="AuthorizationMode",
    )
    transit_encryption_mode: "TransitEncryptionMode" = proto.Field(
        proto.ENUM,
        number=12,
        enum="TransitEncryptionMode",
    )
    size_gb: int = proto.Field(
        proto.INT32,
        number=13,
        optional=True,
    )
    shard_count: int = proto.Field(
        proto.INT32,
        number=14,
        optional=True,
    )
    psc_configs: MutableSequence["PscConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message="PscConfig",
    )
    discovery_endpoints: MutableSequence["DiscoveryEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="DiscoveryEndpoint",
    )
    psc_connections: MutableSequence["PscConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="PscConnection",
    )
    state_info: StateInfo = proto.Field(
        proto.MESSAGE,
        number=18,
        message=StateInfo,
    )
    node_type: "NodeType" = proto.Field(
        proto.ENUM,
        number=19,
        enum="NodeType",
    )
    persistence_config: "ClusterPersistenceConfig" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="ClusterPersistenceConfig",
    )
    redis_configs: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=21,
    )
    precise_size_gb: float = proto.Field(
        proto.DOUBLE,
        number=22,
        optional=True,
    )
    zone_distribution_config: "ZoneDistributionConfig" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="ZoneDistributionConfig",
    )
    cross_cluster_replication_config: "CrossClusterReplicationConfig" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="CrossClusterReplicationConfig",
    )
    deletion_protection_enabled: bool = proto.Field(
        proto.BOOL,
        number=25,
        optional=True,
    )
    maintenance_policy: "ClusterMaintenancePolicy" = proto.Field(
        proto.MESSAGE,
        number=26,
        optional=True,
        message="ClusterMaintenancePolicy",
    )
    maintenance_schedule: "ClusterMaintenanceSchedule" = proto.Field(
        proto.MESSAGE,
        number=27,
        optional=True,
        message="ClusterMaintenanceSchedule",
    )
    psc_service_attachments: MutableSequence["PscServiceAttachment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=30,
            message="PscServiceAttachment",
        )
    )
    cluster_endpoints: MutableSequence["ClusterEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=36,
        message="ClusterEndpoint",
    )
    backup_collection: str = proto.Field(
        proto.STRING,
        number=39,
        optional=True,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=40,
        optional=True,
    )
    automated_backup_config: "AutomatedBackupConfig" = proto.Field(
        proto.MESSAGE,
        number=42,
        message="AutomatedBackupConfig",
    )
    encryption_info: "EncryptionInfo" = proto.Field(
        proto.MESSAGE,
        number=43,
        message="EncryptionInfo",
    )
    async_cluster_endpoints_deletion_enabled: bool = proto.Field(
        proto.BOOL,
        number=44,
        optional=True,
    )
    server_ca_mode: "ServerCaMode" = proto.Field(
        proto.ENUM,
        number=53,
        optional=True,
        enum="ServerCaMode",
    )
    server_ca_pool: str = proto.Field(
        proto.STRING,
        number=54,
        optional=True,
    )
    rotate_server_certificate: bool = proto.Field(
        proto.BOOL,
        number=55,
        optional=True,
    )
    acl_policy: str = proto.Field(
        proto.STRING,
        number=56,
    )
    acl_policy_info: "AclPolicyInfo" = proto.Field(
        proto.MESSAGE,
        number=58,
        message="AclPolicyInfo",
    )


class AclPolicyInfo(proto.Message):
    r"""Details of the applied ACL policy.

    Attributes:
        applied_acl_policy (str):
            Output only. The resource name of the applied ACL policy.
            Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}".
        applied_acl_policy_revision (str):
            Output only. The resource name of the applied ACL policy
            revision. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".
        applied_acl_policy_revision_number (int):
            Output only. The revision number of the
            applied ACL policy revision.
        acl_policy_revision_statuses (MutableSequence[google.cloud.redis_cluster_v1beta1.types.AclPolicyRevisionStatus]):
            Output only. A list of status for various
            revisions of this ACL policy on the cluster.
    """

    applied_acl_policy: str = proto.Field(
        proto.STRING,
        number=1,
    )
    applied_acl_policy_revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    applied_acl_policy_revision_number: int = proto.Field(
        proto.INT64,
        number=3,
    )
    acl_policy_revision_statuses: MutableSequence["AclPolicyRevisionStatus"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="AclPolicyRevisionStatus",
        )
    )


class AclPolicy(proto.Message):
    r"""The ACL policy resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Full resource path of the ACL
            policy.
        rules (MutableSequence[google.cloud.redis_cluster_v1beta1.types.AclRule]):
            Required. The ACL rules within the ACL
            policy.
        state (google.cloud.redis_cluster_v1beta1.types.AclPolicy.State):
            Output only. The state of the ACL policy.
        etag (str):
            Output only. Etag for the ACL policy.

            This field is a member of `oneof`_ ``_etag``.
        cluster_acl_policy_attachments (MutableSequence[google.cloud.redis_cluster_v1beta1.types.ClusterAclPolicyAttachment]):
            Output only. The ACL policy attachment status
            for each attached cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the ACL
            policy was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the ACL
            policy was last updated.
    """

    class State(proto.Enum):
        r"""Represents the different states of an ACL policy.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                ACL policy has been created and is fully
                usable. Since ACL policy creation is synchronous
                and not an LRO, there is no CREATING state.
            UPDATING (2):
                ACL policy is being updated.
            DELETING (3):
                ACL policy is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        UPDATING = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rules: MutableSequence["AclRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AclRule",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    cluster_acl_policy_attachments: MutableSequence["ClusterAclPolicyAttachment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="ClusterAclPolicyAttachment",
        )
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class AclPolicyRevisionStatus(proto.Message):
    r"""AclPolicyRevisionStatus stores the per-revision status for an
    attached cluster.

    Attributes:
        acl_policy_revision (str):
            Output only. The resource name of the ACL policy revision
            this status refers to. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".
        acl_policy_revision_number (int):
            Output only. The revision number of the ACL
            policy revision this status refers to.
        state (google.cloud.redis_cluster_v1beta1.types.AclPolicyRevisionStatus.State):
            Output only. AclPolicyRevision state.
        error_message (str):
            Output only. Human-readable error message
            providing more details for FAILED states.
    """

    class State(proto.Enum):
        r"""Enum indicating the status of this ACL policy revision on the
        cluster.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            APPLYING (1):
                The cluster is attempting to apply this
                revision.
            APPLIED (2):
                The cluster has successfully applied this
                revision.
            FAILED (3):
                The cluster failed to apply this revision.
        """

        STATE_UNSPECIFIED = 0
        APPLYING = 1
        APPLIED = 2
        FAILED = 3

    acl_policy_revision: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_policy_revision_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ClusterAclPolicyAttachment(proto.Message):
    r"""ClusterAclPolicyAttachment stores the ACL policy status for
    an attached cluster for the revisions successfully applied,
    under application or failed.

    Attributes:
        cluster (str):
            Output only. The resource name of the
            attached Cluster. Format:

            "projects/{project}/locations/{location}/clusters/{cluster}".
        acl_policy_revision_statuses (MutableSequence[google.cloud.redis_cluster_v1beta1.types.AclPolicyRevisionStatus]):
            Output only. A list of status for various
            revisions of this ACL policy on the cluster.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_policy_revision_statuses: MutableSequence["AclPolicyRevisionStatus"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="AclPolicyRevisionStatus",
        )
    )


class AclPolicyRevision(proto.Message):
    r"""The ACL policy revision resource.

    Attributes:
        name (str):
            Identifier. The name of the ACL policy revision. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".
        revision_number (int):
            Output only. The revision number of the ACL
            policy revision.
        snapshot (google.cloud.redis_cluster_v1beta1.types.AclPolicy):
            Output only. The snapshot of the ACL policy
            at the time of revision creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        attached_clusters (MutableSequence[str]):
            Output only. A list of clusters that are
            attached to this ACL policy revision.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    snapshot: "AclPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AclPolicy",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    attached_clusters: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class AclRule(proto.Message):
    r"""A single ACL rule which defines the policy for a user.

    Attributes:
        username (str):
            Required. Specifies the IAM user or service
            account to be added to the ACL policy. This
            username will be directly set on the Redis OSS.
        rule (str):
            Required. The rule to be applied to the username. Ex: "on
            >password123 ~\* +@all" The format of the rule is defined by
            Redis OSS:
            https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AutomatedBackupConfig(proto.Message):
    r"""The automated backup config for a cluster.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        fixed_frequency_schedule (google.cloud.redis_cluster_v1beta1.types.AutomatedBackupConfig.FixedFrequencySchedule):
            Optional. Trigger automated backups at a
            fixed frequency.

            This field is a member of `oneof`_ ``schedule``.
        automated_backup_mode (google.cloud.redis_cluster_v1beta1.types.AutomatedBackupConfig.AutomatedBackupMode):
            Optional. The automated backup mode. If the
            mode is disabled, the other fields will be
            ignored.
        retention (google.protobuf.duration_pb2.Duration):
            Optional. How long to keep automated backups
            before the backups are deleted. The value should
            be between 1 day and 365 days. If not specified,
            the default value is 35 days.

            This field is a member of `oneof`_ ``_retention``.
    """

    class AutomatedBackupMode(proto.Enum):
        r"""The automated backup mode.

        Values:
            AUTOMATED_BACKUP_MODE_UNSPECIFIED (0):
                Default value. Automated backup config is not
                specified.
            DISABLED (1):
                Automated backup config disabled.
            ENABLED (2):
                Automated backup config enabled.
        """

        AUTOMATED_BACKUP_MODE_UNSPECIFIED = 0
        DISABLED = 1
        ENABLED = 2

    class FixedFrequencySchedule(proto.Message):
        r"""This schedule allows the backup to be triggered at a fixed
        frequency (currently only daily is supported).


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            start_time (google.type.timeofday_pb2.TimeOfDay):
                Required. The start time of every automated
                backup in UTC. It must be set to the start of an
                hour. This field is required.

                This field is a member of `oneof`_ ``_start_time``.
        """

        start_time: timeofday_pb2.TimeOfDay = proto.Field(
            proto.MESSAGE,
            number=2,
            optional=True,
            message=timeofday_pb2.TimeOfDay,
        )

    fixed_frequency_schedule: FixedFrequencySchedule = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="schedule",
        message=FixedFrequencySchedule,
    )
    automated_backup_mode: AutomatedBackupMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=AutomatedBackupMode,
    )
    retention: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=duration_pb2.Duration,
    )


class BackupCollection(proto.Message):
    r"""BackupCollection of a cluster.

    Attributes:
        name (str):
            Identifier. Full resource path of the backup
            collection.
        cluster_uid (str):
            Output only. The cluster uid of the backup
            collection.
        cluster (str):
            Output only. The full resource path of the
            cluster the backup collection belongs to.
            Example:

            projects/{project}/locations/{location}/clusters/{cluster}
        kms_key (str):
            Output only. The KMS key used to encrypt the
            backups under this backup collection.
        uid (str):
            Output only. System assigned unique
            identifier of the backup collection.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=4,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=5,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Backup(proto.Message):
    r"""Backup of a cluster.

    Attributes:
        name (str):
            Identifier. Full resource path of the backup. the last part
            of the name is the backup id with the following format:
            [YYYYMMDDHHMMSS]\_[Shorted Cluster UID] OR customer
            specified while backup cluster. Example: 20240515123000_1234
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup was
            created.
        cluster (str):
            Output only. Cluster resource path of this
            backup.
        cluster_uid (str):
            Output only. Cluster uid of this backup.
        total_size_bytes (int):
            Output only. Total size of the backup in
            bytes.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup will
            expire.
        engine_version (str):
            Output only. redis-7.2, valkey-7.5
        backup_files (MutableSequence[google.cloud.redis_cluster_v1beta1.types.BackupFile]):
            Output only. List of backup files of the
            backup.
        node_type (google.cloud.redis_cluster_v1beta1.types.NodeType):
            Output only. Node type of the cluster.
        replica_count (int):
            Output only. Number of replicas for the
            cluster.
        shard_count (int):
            Output only. Number of shards for the
            cluster.
        backup_type (google.cloud.redis_cluster_v1beta1.types.Backup.BackupType):
            Output only. Type of the backup.
        state (google.cloud.redis_cluster_v1beta1.types.Backup.State):
            Output only. State of the backup.
        encryption_info (google.cloud.redis_cluster_v1beta1.types.EncryptionInfo):
            Output only. Encryption information of the
            backup.
        uid (str):
            Output only. System assigned unique
            identifier of the backup.
    """

    class BackupType(proto.Enum):
        r"""Type of the backup.

        Values:
            BACKUP_TYPE_UNSPECIFIED (0):
                The default value, not set.
            ON_DEMAND (1):
                On-demand backup.
            AUTOMATED (2):
                Automated backup.
        """

        BACKUP_TYPE_UNSPECIFIED = 0
        ON_DEMAND = 1
        AUTOMATED = 2

    class State(proto.Enum):
        r"""State of the backup.

        Values:
            STATE_UNSPECIFIED (0):
                The default value, not set.
            CREATING (1):
                The backup is being created.
            ACTIVE (2):
                The backup is active to be used.
            DELETING (3):
                The backup is being deleted.
            SUSPENDED (4):
                The backup is currently suspended due to
                reasons like project deletion, billing account
                closure, etc.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        SUSPENDED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    total_size_bytes: int = proto.Field(
        proto.INT64,
        number=5,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    engine_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    backup_files: MutableSequence["BackupFile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="BackupFile",
    )
    node_type: "NodeType" = proto.Field(
        proto.ENUM,
        number=9,
        enum="NodeType",
    )
    replica_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    shard_count: int = proto.Field(
        proto.INT32,
        number=11,
    )
    backup_type: BackupType = proto.Field(
        proto.ENUM,
        number=12,
        enum=BackupType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    encryption_info: "EncryptionInfo" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="EncryptionInfo",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=15,
    )


class BackupFile(proto.Message):
    r"""Backup is consisted of multiple backup files.

    Attributes:
        file_name (str):
            Output only. e.g: <shard-id>.rdb
        size_bytes (int):
            Output only. Size of the backup file in
            bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup file
            was created.
    """

    file_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class PscServiceAttachment(proto.Message):
    r"""Configuration of a service attachment of the cluster, for
    creating PSC connections.

    Attributes:
        service_attachment (str):
            Output only. Service attachment URI which
            your self-created PscConnection should use as
            target
        connection_type (google.cloud.redis_cluster_v1beta1.types.ConnectionType):
            Output only. Type of a PSC connection
            targeting this service attachment.
    """

    service_attachment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_type: "ConnectionType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ConnectionType",
    )


class CrossClusterReplicationConfig(proto.Message):
    r"""Cross cluster replication config.

    Attributes:
        cluster_role (google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.ClusterRole):
            The role of the cluster in cross cluster
            replication.
        primary_cluster (google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.RemoteCluster):
            Details of the primary cluster that is used
            as the replication source for this secondary
            cluster.

            This field is only set for a secondary cluster.
        secondary_clusters (MutableSequence[google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.RemoteCluster]):
            List of secondary clusters that are
            replicating from this primary cluster.
            This field is only set for a primary cluster.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time cross cluster
            replication config was updated.
        membership (google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.Membership):
            Output only. An output only view of all the
            member clusters participating in the cross
            cluster replication. This view will be provided
            by every member cluster irrespective of its
            cluster role(primary or secondary).

            A primary cluster can provide information about
            all the secondary clusters replicating from it.
            However, a secondary cluster only knows about
            the primary cluster from which it is
            replicating. However, for scenarios, where the
            primary cluster is unavailable(e.g. regional
            outage), a GetCluster request can be sent to any
            other member cluster and this field will list
            all the member clusters participating in cross
            cluster replication.
    """

    class ClusterRole(proto.Enum):
        r"""The role of the cluster in cross cluster replication.

        Values:
            CLUSTER_ROLE_UNSPECIFIED (0):
                Cluster role is not set.
                The behavior is equivalent to NONE.
            NONE (1):
                This cluster does not participate in cross
                cluster replication. It is an independent
                cluster and does not replicate to or from any
                other clusters.
            PRIMARY (2):
                A cluster that allows both reads and writes.
                Any data written to this cluster is also
                replicated to the attached secondary clusters.
            SECONDARY (3):
                A cluster that allows only reads and
                replicates data from a primary cluster.
        """

        CLUSTER_ROLE_UNSPECIFIED = 0
        NONE = 1
        PRIMARY = 2
        SECONDARY = 3

    class RemoteCluster(proto.Message):
        r"""Details of the remote cluster associated with this cluster in
        a cross cluster replication setup.

        Attributes:
            cluster (str):
                The full resource path of the remote cluster
                in the format:
                projects/<project>/locations/<region>/clusters/<cluster-id>
            uid (str):
                Output only. The unique identifier of the
                remote cluster.
        """

        cluster: str = proto.Field(
            proto.STRING,
            number=1,
        )
        uid: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Membership(proto.Message):
        r"""An output only view of all the member clusters participating
        in the cross cluster replication.

        Attributes:
            primary_cluster (google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.RemoteCluster):
                Output only. The primary cluster that acts as
                the source of replication for the secondary
                clusters.
            secondary_clusters (MutableSequence[google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.RemoteCluster]):
                Output only. The list of secondary clusters
                replicating from the primary cluster.
        """

        primary_cluster: "CrossClusterReplicationConfig.RemoteCluster" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="CrossClusterReplicationConfig.RemoteCluster",
        )
        secondary_clusters: MutableSequence[
            "CrossClusterReplicationConfig.RemoteCluster"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CrossClusterReplicationConfig.RemoteCluster",
        )

    cluster_role: ClusterRole = proto.Field(
        proto.ENUM,
        number=1,
        enum=ClusterRole,
    )
    primary_cluster: RemoteCluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RemoteCluster,
    )
    secondary_clusters: MutableSequence[RemoteCluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=RemoteCluster,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    membership: Membership = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Membership,
    )


class ClusterMaintenancePolicy(proto.Message):
    r"""Maintenance policy per cluster.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the policy was
            created i.e. Maintenance Window or Deny Period
            was assigned.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the policy was
            updated i.e. Maintenance Window or Deny Period
            was updated.
        weekly_maintenance_window (MutableSequence[google.cloud.redis_cluster_v1beta1.types.ClusterWeeklyMaintenanceWindow]):
            Optional. Maintenance window that is applied to resources
            covered by this policy. Minimum 1. For the current version,
            the maximum number of weekly_maintenance_window is expected
            to be one.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    weekly_maintenance_window: MutableSequence["ClusterWeeklyMaintenanceWindow"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="ClusterWeeklyMaintenanceWindow",
        )
    )


class ClusterWeeklyMaintenanceWindow(proto.Message):
    r"""Time window specified for weekly operations.

    Attributes:
        day (google.type.dayofweek_pb2.DayOfWeek):
            Allows to define schedule that runs specified
            day of the week.
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Start time of the window in UTC.
    """

    day: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=1,
        enum=dayofweek_pb2.DayOfWeek,
    )
    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timeofday_pb2.TimeOfDay,
    )


class ClusterMaintenanceSchedule(proto.Message):
    r"""Upcoming maitenance schedule.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of any upcoming
            scheduled maintenance for this instance.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of any upcoming
            scheduled maintenance for this instance.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class PscConfig(proto.Message):
    r"""

    Attributes:
        network (str):
            Required. The network where the IP address of the discovery
            endpoint will be reserved, in the form of
            projects/{network_project}/global/networks/{network_id}.
    """

    network: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DiscoveryEndpoint(proto.Message):
    r"""Endpoints on each network, for Redis clients to connect to
    the cluster.

    Attributes:
        address (str):
            Output only. Address of the exposed Redis
            endpoint used by clients to connect to the
            service. The address could be either IP or
            hostname.
        port (int):
            Output only. The port number of the exposed
            Redis endpoint.
        psc_config (google.cloud.redis_cluster_v1beta1.types.PscConfig):
            Output only. Customer configuration for where
            the endpoint is created and accessed from.
    """

    address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    psc_config: "PscConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PscConfig",
    )


class PscConnection(proto.Message):
    r"""Details of consumer resources in a PSC connection.

    Attributes:
        psc_connection_id (str):
            Required. The PSC connection id of the
            forwarding rule connected to the service
            attachment.
        address (str):
            Required. The IP allocated on the consumer
            network for the PSC forwarding rule.
        forwarding_rule (str):
            Required. The URI of the consumer side
            forwarding rule. Example:

            projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.
        project_id (str):
            Optional. Project ID of the consumer project
            where the forwarding rule is created in.
        network (str):
            Required. The consumer network where the IP address resides,
            in the form of
            projects/{project_id}/global/networks/{network_id}.
        service_attachment (str):
            Required. The service attachment which is the
            target of the PSC connection, in the form of
            projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.
        psc_connection_status (google.cloud.redis_cluster_v1beta1.types.PscConnectionStatus):
            Output only. The status of the PSC
            connection. Please note that this value is
            updated periodically. To get the latest status
            of a PSC connection, follow
            https://cloud.google.com/vpc/docs/configure-private-service-connect-services#endpoint-details.
        connection_type (google.cloud.redis_cluster_v1beta1.types.ConnectionType):
            Output only. Type of the PSC connection.
    """

    psc_connection_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    forwarding_rule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_attachment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    psc_connection_status: "PscConnectionStatus" = proto.Field(
        proto.ENUM,
        number=8,
        enum="PscConnectionStatus",
    )
    connection_type: "ConnectionType" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ConnectionType",
    )


class ClusterEndpoint(proto.Message):
    r"""ClusterEndpoint consists of PSC connections that are created
    as a group in each VPC network for accessing the cluster. In
    each group, there shall be one connection for each service
    attachment in the cluster.

    Attributes:
        connections (MutableSequence[google.cloud.redis_cluster_v1beta1.types.ConnectionDetail]):
            A group of PSC connections. They are created
            in the same VPC network, one for each service
            attachment in the cluster.
    """

    connections: MutableSequence["ConnectionDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConnectionDetail",
    )


class ConnectionDetail(proto.Message):
    r"""Detailed information of each PSC connection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        psc_auto_connection (google.cloud.redis_cluster_v1beta1.types.PscAutoConnection):
            Detailed information of a PSC connection that
            is created through service connectivity
            automation.

            This field is a member of `oneof`_ ``connection``.
        psc_connection (google.cloud.redis_cluster_v1beta1.types.PscConnection):
            Detailed information of a PSC connection that
            is created by the customer who owns the cluster.

            This field is a member of `oneof`_ ``connection``.
    """

    psc_auto_connection: "PscAutoConnection" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="connection",
        message="PscAutoConnection",
    )
    psc_connection: "PscConnection" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="connection",
        message="PscConnection",
    )


class PscAutoConnection(proto.Message):
    r"""Details of consumer resources in a PSC connection that is
    created through Service Connectivity Automation.

    Attributes:
        psc_connection_id (str):
            Output only. The PSC connection id of the
            forwarding rule connected to the service
            attachment.
        address (str):
            Output only. The IP allocated on the consumer
            network for the PSC forwarding rule.
        forwarding_rule (str):
            Output only. The URI of the consumer side
            forwarding rule. Example:

            projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.
        project_id (str):
            Required. The consumer project_id where the forwarding rule
            is created from.
        network (str):
            Required. The consumer network where the IP address resides,
            in the form of
            projects/{project_id}/global/networks/{network_id}.
        service_attachment (str):
            Output only. The service attachment which is
            the target of the PSC connection, in the form of
            projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.
        psc_connection_status (google.cloud.redis_cluster_v1beta1.types.PscConnectionStatus):
            Output only. The status of the PSC
            connection. Please note that this value is
            updated periodically. Please use Private Service
            Connect APIs for the latest status.
        connection_type (google.cloud.redis_cluster_v1beta1.types.ConnectionType):
            Output only. Type of the PSC connection.
    """

    psc_connection_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    forwarding_rule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_attachment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    psc_connection_status: "PscConnectionStatus" = proto.Field(
        proto.ENUM,
        number=8,
        enum="PscConnectionStatus",
    )
    connection_type: "ConnectionType" = proto.Field(
        proto.ENUM,
        number=9,
        enum="ConnectionType",
    )


class SharedRegionalCertificateAuthority(proto.Message):
    r"""Shared regional certificate authority

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        managed_server_ca (google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority):
            CA certificate chains for redis managed
            server authentication.

            This field is a member of `oneof`_ ``server_ca``.
        name (str):
            Identifier. Unique name of the resource in this scope
            including project and location using the form:
            ``projects/{project}/locations/{location}/sharedRegionalCertificateAuthority``
    """

    class RegionalManagedCertificateAuthority(proto.Message):
        r"""CA certificate chains for redis managed server
        authentication.

        Attributes:
            ca_certs (MutableSequence[google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain]):
                The PEM encoded CA certificate chains for
                redis managed server authentication
        """

        class RegionalCertChain(proto.Message):
            r"""The certificates that form the CA chain, from leaf to root
            order.

            Attributes:
                certificates (MutableSequence[str]):
                    The certificates that form the CA chain, from
                    leaf to root order.
            """

            certificates: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        ca_certs: MutableSequence[
            "SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain",
        )

    managed_server_ca: RegionalManagedCertificateAuthority = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="server_ca",
        message=RegionalManagedCertificateAuthority,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSharedRegionalCertificateAuthorityRequest(proto.Message):
    r"""Request for
    [GetSharedRegionalCertificateAuthority][CloudRedis.GetSharedRegionalCertificateAuthority].

    Attributes:
        name (str):
            Required. Regional certificate authority resource name using
            the form:
            ``projects/{project_id}/locations/{location_id}/sharedRegionalCertificateAuthority``
            where ``location_id`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Pre-defined metadata fields.

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


class TokenAuthUser(proto.Message):
    r"""Represents a token based auth user for the cluster.

    Attributes:
        name (str):
            Identifier. The resource name of the token based auth user.
            Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}
        state (google.cloud.redis_cluster_v1beta1.types.TokenAuthUser.State):
            Output only. The state of the token based
            auth user.
    """

    class State(proto.Enum):
        r"""Represents the different states of a token based auth user.
        New values may be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                The auth user is active.
            CREATING (2):
                The auth user is being created.
            UPDATING (3):
                The auth user is being updated.
            DELETING (4):
                The auth user is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )


class AuthToken(proto.Message):
    r"""Auth token for the cluster.

    Attributes:
        name (str):
            Identifier. Name of the auth token. Format:
            projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}
        token (str):
            Output only. The service generated
            authentication token used to connect to the
            Redis cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the auth token.
        state (google.cloud.redis_cluster_v1beta1.types.AuthToken.State):
            Output only. State of the auth token.
    """

    class State(proto.Enum):
        r"""Represents the different states of an auth token.
        New values may be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                The auth token is active.
            CREATING (2):
                The auth token is being created.
            DELETING (3):
                The auth token is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class CertificateAuthority(proto.Message):
    r"""Redis cluster certificate authority

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        managed_server_ca (google.cloud.redis_cluster_v1beta1.types.CertificateAuthority.ManagedCertificateAuthority):

            This field is a member of `oneof`_ ``server_ca``.
        name (str):
            Identifier. Unique name of the resource in this scope
            including project, location and cluster using the form:
            ``projects/{project}/locations/{location}/clusters/{cluster}/certificateAuthority``
    """

    class ManagedCertificateAuthority(proto.Message):
        r"""

        Attributes:
            ca_certs (MutableSequence[google.cloud.redis_cluster_v1beta1.types.CertificateAuthority.ManagedCertificateAuthority.CertChain]):
                The PEM encoded CA certificate chains for
                redis managed server authentication
        """

        class CertChain(proto.Message):
            r"""

            Attributes:
                certificates (MutableSequence[str]):
                    The certificates that form the CA chain, from
                    leaf to root order.
            """

            certificates: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        ca_certs: MutableSequence[
            "CertificateAuthority.ManagedCertificateAuthority.CertChain"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CertificateAuthority.ManagedCertificateAuthority.CertChain",
        )

    managed_server_ca: ManagedCertificateAuthority = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="server_ca",
        message=ManagedCertificateAuthority,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ClusterPersistenceConfig(proto.Message):
    r"""Configuration of the persistence functionality.

    Attributes:
        mode (google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.PersistenceMode):
            Optional. The mode of persistence.
        rdb_config (google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.RDBConfig):
            Optional. RDB configuration. This field will
            be ignored if mode is not RDB.
        aof_config (google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.AOFConfig):
            Optional. AOF configuration. This field will
            be ignored if mode is not AOF.
    """

    class PersistenceMode(proto.Enum):
        r"""Available persistence modes.

        Values:
            PERSISTENCE_MODE_UNSPECIFIED (0):
                Not set.
            DISABLED (1):
                Persistence is disabled, and any snapshot
                data is deleted.
            RDB (2):
                RDB based persistence is enabled.
            AOF (3):
                AOF based persistence is enabled.
        """

        PERSISTENCE_MODE_UNSPECIFIED = 0
        DISABLED = 1
        RDB = 2
        AOF = 3

    class RDBConfig(proto.Message):
        r"""Configuration of the RDB based persistence.

        Attributes:
            rdb_snapshot_period (google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.RDBConfig.SnapshotPeriod):
                Optional. Period between RDB snapshots.
            rdb_snapshot_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The time that the first snapshot
                was/will be attempted, and to which future
                snapshots will be aligned. If not provided, the
                current time will be used.
        """

        class SnapshotPeriod(proto.Enum):
            r"""Available snapshot periods.

            Values:
                SNAPSHOT_PERIOD_UNSPECIFIED (0):
                    Not set.
                ONE_HOUR (1):
                    One hour.
                SIX_HOURS (2):
                    Six hours.
                TWELVE_HOURS (3):
                    Twelve hours.
                TWENTY_FOUR_HOURS (4):
                    Twenty four hours.
            """

            SNAPSHOT_PERIOD_UNSPECIFIED = 0
            ONE_HOUR = 1
            SIX_HOURS = 2
            TWELVE_HOURS = 3
            TWENTY_FOUR_HOURS = 4

        rdb_snapshot_period: "ClusterPersistenceConfig.RDBConfig.SnapshotPeriod" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="ClusterPersistenceConfig.RDBConfig.SnapshotPeriod",
            )
        )
        rdb_snapshot_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class AOFConfig(proto.Message):
        r"""Configuration of the AOF based persistence.

        Attributes:
            append_fsync (google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.AOFConfig.AppendFsync):
                Optional. fsync configuration.
        """

        class AppendFsync(proto.Enum):
            r"""Available fsync modes.

            Values:
                APPEND_FSYNC_UNSPECIFIED (0):
                    Not set. Default: EVERYSEC
                NO (1):
                    Never fsync. Normally Linux will flush data
                    every 30 seconds with this configuration, but
                    it's up to the kernel's exact tuning.
                EVERYSEC (2):
                    fsync every second. Fast enough, and you may
                    lose 1 second of data if there is a disaster
                ALWAYS (3):
                    fsync every time new write commands are
                    appended to the AOF. It has the best data loss
                    protection at the cost of performance
            """

            APPEND_FSYNC_UNSPECIFIED = 0
            NO = 1
            EVERYSEC = 2
            ALWAYS = 3

        append_fsync: "ClusterPersistenceConfig.AOFConfig.AppendFsync" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ClusterPersistenceConfig.AOFConfig.AppendFsync",
        )

    mode: PersistenceMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=PersistenceMode,
    )
    rdb_config: RDBConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RDBConfig,
    )
    aof_config: AOFConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=AOFConfig,
    )


class ZoneDistributionConfig(proto.Message):
    r"""Zone distribution config for allocation of cluster resources.

    Attributes:
        mode (google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig.ZoneDistributionMode):
            Optional. The mode of zone distribution. Defaults to
            MULTI_ZONE, when not specified.
        zone (str):
            Optional. When SINGLE ZONE distribution is selected, zone
            field would be used to allocate all resources in that zone.
            This is not applicable to MULTI_ZONE, and would be ignored
            for MULTI_ZONE clusters.
        zones (MutableSequence[str]):
            Optional. Specify the zones of a multi-zone
            cluster where Redis Cluster allocates resources.
            This flag isn't applicable for single-zone
            clusters.
        active_zones (MutableSequence[str]):
            Output only. The exact list of zones where
            the cluster currently has active VMs.
    """

    class ZoneDistributionMode(proto.Enum):
        r"""Defines various modes of zone distribution.

        Values:
            ZONE_DISTRIBUTION_MODE_UNSPECIFIED (0):
                Not Set. Default: MULTI_ZONE
            MULTI_ZONE (1):
                Distribute all resources across 3 zones
                picked at random, within the region.
            SINGLE_ZONE (2):
                Distribute all resources in a single zone.
                The zone field must be specified, when this mode
                is selected.
        """

        ZONE_DISTRIBUTION_MODE_UNSPECIFIED = 0
        MULTI_ZONE = 1
        SINGLE_ZONE = 2

    mode: ZoneDistributionMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=ZoneDistributionMode,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    active_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class RescheduleClusterMaintenanceRequest(proto.Message):
    r"""Request for rescheduling a cluster maintenance.

    Attributes:
        name (str):
            Required. Redis Cluster instance resource name using the
            form:
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
            where ``location_id`` refers to a GCP region.
        reschedule_type (google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest.RescheduleType):
            Required. If reschedule type is SPECIFIC_TIME, must set up
            schedule_time as well.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp when the maintenance shall be
            rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339
            format, for example ``2012-11-15T16:19:00.094Z``.
    """

    class RescheduleType(proto.Enum):
        r"""Reschedule options.

        Values:
            RESCHEDULE_TYPE_UNSPECIFIED (0):
                Not set.
            IMMEDIATE (1):
                If the user wants to schedule the maintenance
                to happen now.
            SPECIFIC_TIME (3):
                If the user wants to reschedule the
                maintenance to a specific time.
        """

        RESCHEDULE_TYPE_UNSPECIFIED = 0
        IMMEDIATE = 1
        SPECIFIC_TIME = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reschedule_type: RescheduleType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RescheduleType,
    )
    schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class EncryptionInfo(proto.Message):
    r"""EncryptionInfo describes the encryption information of a
    cluster or a backup.

    Attributes:
        encryption_type (google.cloud.redis_cluster_v1beta1.types.EncryptionInfo.Type):
            Output only. Type of encryption.
        kms_key_versions (MutableSequence[str]):
            Output only. KMS key versions that are being
            used to protect the data at-rest.
        kms_key_primary_state (google.cloud.redis_cluster_v1beta1.types.EncryptionInfo.KmsKeyState):
            Output only. The state of the primary version
            of the KMS key perceived by the system. This
            field is not populated in backups.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time when the
            encryption info was updated.
    """

    class Type(proto.Enum):
        r"""Possible encryption types.

        Values:
            TYPE_UNSPECIFIED (0):
                Encryption type not specified. Defaults to
                GOOGLE_DEFAULT_ENCRYPTION.
            GOOGLE_DEFAULT_ENCRYPTION (1):
                The data is encrypted at rest with a key that
                is fully managed by Google. No key version will
                be populated. This is the default state.
            CUSTOMER_MANAGED_ENCRYPTION (2):
                The data is encrypted at rest with a key that
                is managed by the customer. KMS key versions
                will be populated.
        """

        TYPE_UNSPECIFIED = 0
        GOOGLE_DEFAULT_ENCRYPTION = 1
        CUSTOMER_MANAGED_ENCRYPTION = 2

    class KmsKeyState(proto.Enum):
        r"""The state of the KMS key perceived by the system. Refer to
        the public documentation for the impact of each state.

        Values:
            KMS_KEY_STATE_UNSPECIFIED (0):
                The default value. This value is unused.
            ENABLED (1):
                The KMS key is enabled and correctly
                configured.
            PERMISSION_DENIED (2):
                Permission denied on the KMS key.
            DISABLED (3):
                The KMS key is disabled.
            DESTROYED (4):
                The KMS key is destroyed.
            DESTROY_SCHEDULED (5):
                The KMS key is scheduled to be destroyed.
            EKM_KEY_UNREACHABLE_DETECTED (6):
                The EKM key is unreachable.
            BILLING_DISABLED (7):
                Billing is disabled for the project.
            UNKNOWN_FAILURE (8):
                All other unknown failures.
        """

        KMS_KEY_STATE_UNSPECIFIED = 0
        ENABLED = 1
        PERMISSION_DENIED = 2
        DISABLED = 3
        DESTROYED = 4
        DESTROY_SCHEDULED = 5
        EKM_KEY_UNREACHABLE_DETECTED = 6
        BILLING_DISABLED = 7
        UNKNOWN_FAILURE = 8

    encryption_type: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    kms_key_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    kms_key_primary_state: KmsKeyState = proto.Field(
        proto.ENUM,
        number=3,
        enum=KmsKeyState,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
