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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.gke_multicloud_v1.types import common_resources

__protobuf__ = proto.module(
    package="google.cloud.gkemulticloud.v1",
    manifest={
        "AzureCluster",
        "AzureClusterNetworking",
        "AzureControlPlane",
        "ReplicaPlacement",
        "AzureProxyConfig",
        "AzureDatabaseEncryption",
        "AzureConfigEncryption",
        "AzureDiskTemplate",
        "AzureClient",
        "AzureAuthorization",
        "AzureServicesAuthentication",
        "AzureClusterUser",
        "AzureClusterGroup",
        "AzureNodePool",
        "AzureNodeManagement",
        "AzureNodeConfig",
        "AzureNodePoolAutoscaling",
        "AzureOpenIdConfig",
        "AzureJsonWebKeys",
        "AzureServerConfig",
        "AzureK8sVersionInfo",
        "AzureSshConfig",
        "AzureClusterResources",
        "AzureClusterError",
        "AzureNodePoolError",
    },
)


class AzureCluster(proto.Message):
    r"""An Anthos cluster running on Azure.

    Attributes:
        name (str):
            The name of this resource.

            Cluster names are formatted as
            ``projects/<project-number>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
        description (str):
            Optional. A human readable description of
            this cluster. Cannot be longer than 255 UTF-8
            encoded bytes.
        azure_region (str):
            Required. The Azure region where the cluster runs.

            Each Google Cloud region supports a subset of nearby Azure
            regions. You can call
            [GetAzureServerConfig][google.cloud.gkemulticloud.v1.AzureClusters.GetAzureServerConfig]
            to list all supported Azure regions within a given Google
            Cloud region.
        resource_group_id (str):
            Required. The ARM ID of the resource group where the cluster
            resources are deployed. For example:
            ``/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>``
        azure_client (str):
            Optional. Name of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            that contains authentication configuration for how the
            Anthos Multi-Cloud API connects to Azure APIs.

            Either azure_client or azure_services_authentication should
            be provided.

            The ``AzureClient`` resource must reside on the same Google
            Cloud Platform project and region as the ``AzureCluster``.

            ``AzureClient`` names are formatted as
            ``projects/<project-number>/locations/<region>/azureClients/<client-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        networking (google.cloud.gke_multicloud_v1.types.AzureClusterNetworking):
            Required. Cluster-wide networking
            configuration.
        control_plane (google.cloud.gke_multicloud_v1.types.AzureControlPlane):
            Required. Configuration related to the
            cluster control plane.
        authorization (google.cloud.gke_multicloud_v1.types.AzureAuthorization):
            Required. Configuration related to the
            cluster RBAC settings.
        azure_services_authentication (google.cloud.gke_multicloud_v1.types.AzureServicesAuthentication):
            Optional. Authentication configuration for management of
            Azure resources.

            Either azure_client or azure_services_authentication should
            be provided.
        state (google.cloud.gke_multicloud_v1.types.AzureCluster.State):
            Output only. The current state of the
            cluster.
        endpoint (str):
            Output only. The endpoint of the cluster's
            API server.
        uid (str):
            Output only. A globally unique identifier for
            the cluster.
        reconciling (bool):
            Output only. If set, there are currently
            changes in flight to the cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this cluster
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this cluster
            was last updated.
        etag (str):
            Allows clients to perform consistent
            read-modify-writes through optimistic
            concurrency control.

            Can be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        annotations (MutableMapping[str, str]):
            Optional. Annotations on the cluster.

            This field has the same restrictions as Kubernetes
            annotations. The total size of all keys and values combined
            is limited to 256k. Keys can have 2 segments: prefix
            (optional) and name (required), separated by a slash (/).
            Prefix must be a DNS subdomain. Name must be 63 characters
            or less, begin and end with alphanumerics, with dashes (-),
            underscores (\_), dots (.), and alphanumerics between.
        workload_identity_config (google.cloud.gke_multicloud_v1.types.WorkloadIdentityConfig):
            Output only. Workload Identity settings.
        cluster_ca_certificate (str):
            Output only. PEM encoded x509 certificate of
            the cluster root of trust.
        fleet (google.cloud.gke_multicloud_v1.types.Fleet):
            Required. Fleet configuration.
        managed_resources (google.cloud.gke_multicloud_v1.types.AzureClusterResources):
            Output only. Managed Azure resources for this
            cluster.
        logging_config (google.cloud.gke_multicloud_v1.types.LoggingConfig):
            Optional. Logging configuration for this
            cluster.
        errors (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureClusterError]):
            Output only. A set of errors found in the
            cluster.
        monitoring_config (google.cloud.gke_multicloud_v1.types.MonitoringConfig):
            Optional. Monitoring configuration for this
            cluster.
    """

    class State(proto.Enum):
        r"""The lifecycle state of the cluster.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            PROVISIONING (1):
                The PROVISIONING state indicates the cluster
                is being created.
            RUNNING (2):
                The RUNNING state indicates the cluster has
                been created and is fully usable.
            RECONCILING (3):
                The RECONCILING state indicates that some
                work is actively being done on the cluster, such
                as upgrading the control plane replicas.
            STOPPING (4):
                The STOPPING state indicates the cluster is
                being deleted.
            ERROR (5):
                The ERROR state indicates the cluster is in a
                broken unrecoverable state.
            DEGRADED (6):
                The DEGRADED state indicates the cluster
                requires user action to restore full
                functionality.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        RECONCILING = 3
        STOPPING = 4
        ERROR = 5
        DEGRADED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    azure_region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_group_id: str = proto.Field(
        proto.STRING,
        number=17,
    )
    azure_client: str = proto.Field(
        proto.STRING,
        number=16,
    )
    networking: "AzureClusterNetworking" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AzureClusterNetworking",
    )
    control_plane: "AzureControlPlane" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AzureControlPlane",
    )
    authorization: "AzureAuthorization" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AzureAuthorization",
    )
    azure_services_authentication: "AzureServicesAuthentication" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="AzureServicesAuthentication",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=8,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=9,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=13,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )
    workload_identity_config: common_resources.WorkloadIdentityConfig = proto.Field(
        proto.MESSAGE,
        number=18,
        message=common_resources.WorkloadIdentityConfig,
    )
    cluster_ca_certificate: str = proto.Field(
        proto.STRING,
        number=19,
    )
    fleet: common_resources.Fleet = proto.Field(
        proto.MESSAGE,
        number=20,
        message=common_resources.Fleet,
    )
    managed_resources: "AzureClusterResources" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="AzureClusterResources",
    )
    logging_config: common_resources.LoggingConfig = proto.Field(
        proto.MESSAGE,
        number=23,
        message=common_resources.LoggingConfig,
    )
    errors: MutableSequence["AzureClusterError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=24,
        message="AzureClusterError",
    )
    monitoring_config: common_resources.MonitoringConfig = proto.Field(
        proto.MESSAGE,
        number=25,
        message=common_resources.MonitoringConfig,
    )


class AzureClusterNetworking(proto.Message):
    r"""ClusterNetworking contains cluster-wide networking
    configuration.

    Attributes:
        virtual_network_id (str):
            Required. The Azure Resource Manager (ARM) ID of the VNet
            associated with your cluster.

            All components in the cluster (i.e. control plane and node
            pools) run on a single VNet.

            Example:
            ``/subscriptions/<subscription-id>/resourceGroups/<resource-group-id>/providers/Microsoft.Network/virtualNetworks/<vnet-id>``

            This field cannot be changed after creation.
        pod_address_cidr_blocks (MutableSequence[str]):
            Required. The IP address range of the pods in this cluster,
            in CIDR notation (e.g. ``10.96.0.0/14``).

            All pods in the cluster get assigned a unique IPv4 address
            from these ranges. Only a single range is supported.

            This field cannot be changed after creation.
        service_address_cidr_blocks (MutableSequence[str]):
            Required. The IP address range for services in this cluster,
            in CIDR notation (e.g. ``10.96.0.0/14``).

            All services in the cluster get assigned a unique IPv4
            address from these ranges. Only a single range is supported.

            This field cannot be changed after creating a cluster.
        service_load_balancer_subnet_id (str):
            Optional. The ARM ID of the subnet where Kubernetes private
            service type load balancers are deployed. When unspecified,
            it defaults to AzureControlPlane.subnet_id.

            Example:
            "/subscriptions/d00494d6-6f3c-4280-bbb2-899e163d1d30/resourceGroups/anthos_cluster_gkeust4/providers/Microsoft.Network/virtualNetworks/gke-vnet-gkeust4/subnets/subnetid456".
    """

    virtual_network_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pod_address_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    service_address_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    service_load_balancer_subnet_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AzureControlPlane(proto.Message):
    r"""AzureControlPlane represents the control plane
    configurations.

    Attributes:
        version (str):
            Required. The Kubernetes version to run on control plane
            replicas (e.g. ``1.19.10-gke.1000``).

            You can list all supported versions on a given Google Cloud
            region by calling
            [GetAzureServerConfig][google.cloud.gkemulticloud.v1.AzureClusters.GetAzureServerConfig].
        subnet_id (str):
            Optional. The ARM ID of the default subnet for the control
            plane. The control plane VMs are deployed in this subnet,
            unless ``AzureControlPlane.replica_placements`` is
            specified. This subnet will also be used as default for
            ``AzureControlPlane.endpoint_subnet_id`` if
            ``AzureControlPlane.endpoint_subnet_id`` is not specified.
            Similarly it will be used as default for
            ``AzureClusterNetworking.service_load_balancer_subnet_id``.

            Example:
            ``/subscriptions/<subscription-id>/resourceGroups/<resource-group-id>/providers/Microsoft.Network/virtualNetworks/<vnet-id>/subnets/default``.
        vm_size (str):
            Optional. The Azure VM size name. Example:
            ``Standard_DS2_v2``.

            For available VM sizes, see
            https://docs.microsoft.com/en-us/azure/virtual-machines/vm-naming-conventions.

            When unspecified, it defaults to ``Standard_DS2_v2``.
        ssh_config (google.cloud.gke_multicloud_v1.types.AzureSshConfig):
            Required. SSH configuration for how to access
            the underlying control plane machines.
        root_volume (google.cloud.gke_multicloud_v1.types.AzureDiskTemplate):
            Optional. Configuration related to the root
            volume provisioned for each control plane
            replica.

            When unspecified, it defaults to 32-GiB Azure
            Disk.
        main_volume (google.cloud.gke_multicloud_v1.types.AzureDiskTemplate):
            Optional. Configuration related to the main
            volume provisioned for each control plane
            replica. The main volume is in charge of storing
            all of the cluster's etcd state.

            When unspecified, it defaults to a 8-GiB Azure
            Disk.
        database_encryption (google.cloud.gke_multicloud_v1.types.AzureDatabaseEncryption):
            Optional. Configuration related to
            application-layer secrets encryption.
        proxy_config (google.cloud.gke_multicloud_v1.types.AzureProxyConfig):
            Optional. Proxy configuration for outbound
            HTTP(S) traffic.
        config_encryption (google.cloud.gke_multicloud_v1.types.AzureConfigEncryption):
            Optional. Configuration related to vm config
            encryption.
        tags (MutableMapping[str, str]):
            Optional. A set of tags to apply to all
            underlying control plane Azure resources.
        replica_placements (MutableSequence[google.cloud.gke_multicloud_v1.types.ReplicaPlacement]):
            Optional. Configuration for where to place the control plane
            replicas.

            Up to three replica placement instances can be specified. If
            replica_placements is set, the replica placement instances
            will be applied to the three control plane replicas as
            evenly as possible.
        endpoint_subnet_id (str):
            Optional. The ARM ID of the subnet where the control plane
            load balancer is deployed. When unspecified, it defaults to
            AzureControlPlane.subnet_id.

            Example:
            "/subscriptions/d00494d6-6f3c-4280-bbb2-899e163d1d30/resourceGroups/anthos_cluster_gkeust4/providers/Microsoft.Network/virtualNetworks/gke-vnet-gkeust4/subnets/subnetid123".
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vm_size: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ssh_config: "AzureSshConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="AzureSshConfig",
    )
    root_volume: "AzureDiskTemplate" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AzureDiskTemplate",
    )
    main_volume: "AzureDiskTemplate" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AzureDiskTemplate",
    )
    database_encryption: "AzureDatabaseEncryption" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="AzureDatabaseEncryption",
    )
    proxy_config: "AzureProxyConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AzureProxyConfig",
    )
    config_encryption: "AzureConfigEncryption" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="AzureConfigEncryption",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    replica_placements: MutableSequence["ReplicaPlacement"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="ReplicaPlacement",
    )
    endpoint_subnet_id: str = proto.Field(
        proto.STRING,
        number=15,
    )


class ReplicaPlacement(proto.Message):
    r"""Configuration for the placement of a control plane replica.

    Attributes:
        subnet_id (str):
            Required. For a given replica, the ARM ID of
            the subnet where the control plane VM is
            deployed. Make sure it's a subnet under the
            virtual network in the cluster configuration.
        azure_availability_zone (str):
            Required. For a given replica, the Azure
            availability zone where to provision the control
            plane VM and the ETCD disk.
    """

    subnet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_availability_zone: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureProxyConfig(proto.Message):
    r"""Details of a proxy config stored in Azure Key Vault.

    Attributes:
        resource_group_id (str):
            The ARM ID the of the resource group containing proxy
            keyvault.

            Resource group ids are formatted as
            ``/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>``.
        secret_id (str):
            The URL the of the proxy setting secret with its version.

            The secret must be a JSON encoded proxy configuration as
            described in
            https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-a-proxy#create_a_proxy_configuration_file

            Secret ids are formatted as
            ``https://<key-vault-name>.vault.azure.net/secrets/<secret-name>/<secret-version>``.
    """

    resource_group_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureDatabaseEncryption(proto.Message):
    r"""Configuration related to application-layer secrets
    encryption.
    Anthos clusters on Azure encrypts your Kubernetes data at rest
    in etcd using Azure Key Vault.

    Attributes:
        key_id (str):
            Required. The ARM ID of the Azure Key Vault key to encrypt /
            decrypt data.

            For example:
            ``/subscriptions/<subscription-id>/resourceGroups/<resource-group-id>/providers/Microsoft.KeyVault/vaults/<key-vault-id>/keys/<key-name>``
            Encryption will always take the latest version of the key
            and hence specific version is not supported.
    """

    key_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AzureConfigEncryption(proto.Message):
    r"""Configuration related to config data encryption.

    Azure VM bootstrap secret is envelope encrypted with the
    provided key vault key.

    Attributes:
        key_id (str):
            Required. The ARM ID of the Azure Key Vault key to encrypt /
            decrypt config data.

            For example:
            ``/subscriptions/<subscription-id>/resourceGroups/<resource-group-id>/providers/Microsoft.KeyVault/vaults/<key-vault-id>/keys/<key-name>``
        public_key (str):
            Optional. RSA key of the Azure Key Vault
            public key to use for encrypting the data.

            This key must be formatted as a PEM-encoded
            SubjectPublicKeyInfo (RFC 5280) in ASN.1 DER
            form. The string must be comprised of a single
            PEM block of type "PUBLIC KEY".
    """

    key_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    public_key: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AzureDiskTemplate(proto.Message):
    r"""Configuration for Azure Disks.

    Attributes:
        size_gib (int):
            Optional. The size of the disk, in GiBs.

            When unspecified, a default value is provided.
            See the specific reference in the parent
            resource.
    """

    size_gib: int = proto.Field(
        proto.INT32,
        number=1,
    )


class AzureClient(proto.Message):
    r"""``AzureClient`` resources hold client authentication information
    needed by the Anthos Multi-Cloud API to manage Azure resources on
    your Azure subscription.

    When an [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
    is created, an ``AzureClient`` resource needs to be provided and all
    operations on Azure resources associated to that cluster will
    authenticate to Azure services using the given client.

    ``AzureClient`` resources are immutable and cannot be modified upon
    creation.

    Each ``AzureClient`` resource is bound to a single Azure Active
    Directory Application and tenant.

    Attributes:
        name (str):
            The name of this resource.

            ``AzureClient`` resource names are formatted as
            ``projects/<project-number>/locations/<region>/azureClients/<client-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        tenant_id (str):
            Required. The Azure Active Directory Tenant
            ID.
        application_id (str):
            Required. The Azure Active Directory
            Application ID.
        reconciling (bool):
            Output only. If set, there are currently
            pending changes to the client.
        annotations (MutableMapping[str, str]):
            Optional. Annotations on the resource.

            This field has the same restrictions as Kubernetes
            annotations. The total size of all keys and values combined
            is limited to 256k. Keys can have 2 segments: prefix
            (optional) and name (required), separated by a slash (/).
            Prefix must be a DNS subdomain. Name must be 63 characters
            or less, begin and end with alphanumerics, with dashes (-),
            underscores (\_), dots (.), and alphanumerics between.
        pem_certificate (str):
            Output only. The PEM encoded x509
            certificate.
        uid (str):
            Output only. A globally unique identifier for
            the client.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this client
            was last updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    application_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    pem_certificate: str = proto.Field(
        proto.STRING,
        number=7,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class AzureAuthorization(proto.Message):
    r"""Configuration related to the cluster RBAC settings.

    Attributes:
        admin_users (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureClusterUser]):
            Optional. Users that can perform operations as a cluster
            admin. A managed ClusterRoleBinding will be created to grant
            the ``cluster-admin`` ClusterRole to the users. Up to ten
            admin users can be provided.

            For more info on RBAC, see
            https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles
        admin_groups (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureClusterGroup]):
            Optional. Groups of users that can perform operations as a
            cluster admin. A managed ClusterRoleBinding will be created
            to grant the ``cluster-admin`` ClusterRole to the groups. Up
            to ten admin groups can be provided.

            For more info on RBAC, see
            https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles
    """

    admin_users: MutableSequence["AzureClusterUser"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AzureClusterUser",
    )
    admin_groups: MutableSequence["AzureClusterGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AzureClusterGroup",
    )


class AzureServicesAuthentication(proto.Message):
    r"""Authentication configuration for the management of Azure
    resources.

    Attributes:
        tenant_id (str):
            Required. The Azure Active Directory Tenant
            ID.
        application_id (str):
            Required. The Azure Active Directory
            Application ID.
    """

    tenant_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    application_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureClusterUser(proto.Message):
    r"""Identities of a user-type subject for Azure clusters.

    Attributes:
        username (str):
            Required. The name of the user, e.g.
            ``my-gcp-id@gmail.com``.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AzureClusterGroup(proto.Message):
    r"""Identities of a group-type subject for Azure clusters.

    Attributes:
        group (str):
            Required. The name of the group, e.g.
            ``my-group@domain.com``.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AzureNodePool(proto.Message):
    r"""An Anthos node pool running on Azure.

    Attributes:
        name (str):
            The name of this resource.

            Node pool names are formatted as
            ``projects/<project-number>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            For more details on Google Cloud resource names, see
            `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
        version (str):
            Required. The Kubernetes version (e.g. ``1.19.10-gke.1000``)
            running on this node pool.
        config (google.cloud.gke_multicloud_v1.types.AzureNodeConfig):
            Required. The node configuration of the node
            pool.
        subnet_id (str):
            Required. The ARM ID of the subnet where the
            node pool VMs run. Make sure it's a subnet under
            the virtual network in the cluster
            configuration.
        autoscaling (google.cloud.gke_multicloud_v1.types.AzureNodePoolAutoscaling):
            Required. Autoscaler configuration for this
            node pool.
        state (google.cloud.gke_multicloud_v1.types.AzureNodePool.State):
            Output only. The current state of the node
            pool.
        uid (str):
            Output only. A globally unique identifier for
            the node pool.
        reconciling (bool):
            Output only. If set, there are currently
            pending changes to the node pool.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this node pool
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this node pool
            was last updated.
        etag (str):
            Allows clients to perform consistent
            read-modify-writes through optimistic
            concurrency control.

            Can be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        annotations (MutableMapping[str, str]):
            Optional. Annotations on the node pool.

            This field has the same restrictions as Kubernetes
            annotations. The total size of all keys and values combined
            is limited to 256k. Keys can have 2 segments: prefix
            (optional) and name (required), separated by a slash (/).
            Prefix must be a DNS subdomain. Name must be 63 characters
            or less, begin and end with alphanumerics, with dashes (-),
            underscores (\_), dots (.), and alphanumerics between.
        max_pods_constraint (google.cloud.gke_multicloud_v1.types.MaxPodsConstraint):
            Required. The constraint on the maximum
            number of pods that can be run simultaneously on
            a node in the node pool.
        azure_availability_zone (str):
            Optional. The Azure availability zone of the nodes in this
            nodepool.

            When unspecified, it defaults to ``1``.
        errors (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureNodePoolError]):
            Output only. A set of errors found in the
            node pool.
        management (google.cloud.gke_multicloud_v1.types.AzureNodeManagement):
            Optional. The Management configuration for
            this node pool.
    """

    class State(proto.Enum):
        r"""The lifecycle state of the node pool.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            PROVISIONING (1):
                The PROVISIONING state indicates the node
                pool is being created.
            RUNNING (2):
                The RUNNING state indicates the node pool has
                been created and is fully usable.
            RECONCILING (3):
                The RECONCILING state indicates that the node
                pool is being reconciled.
            STOPPING (4):
                The STOPPING state indicates the node pool is
                being deleted.
            ERROR (5):
                The ERROR state indicates the node pool is in
                a broken unrecoverable state.
            DEGRADED (6):
                The DEGRADED state indicates the node pool
                requires user action to restore full
                functionality.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        RECONCILING = 3
        STOPPING = 4
        ERROR = 5
        DEGRADED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    config: "AzureNodeConfig" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="AzureNodeConfig",
    )
    subnet_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    autoscaling: "AzureNodePoolAutoscaling" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AzureNodePoolAutoscaling",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=8,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
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
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    max_pods_constraint: common_resources.MaxPodsConstraint = proto.Field(
        proto.MESSAGE,
        number=21,
        message=common_resources.MaxPodsConstraint,
    )
    azure_availability_zone: str = proto.Field(
        proto.STRING,
        number=23,
    )
    errors: MutableSequence["AzureNodePoolError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message="AzureNodePoolError",
    )
    management: "AzureNodeManagement" = proto.Field(
        proto.MESSAGE,
        number=30,
        message="AzureNodeManagement",
    )


class AzureNodeManagement(proto.Message):
    r"""AzureNodeManagement defines the set of node management
    features turned on for an Azure node pool.

    Attributes:
        auto_repair (bool):
            Optional. Whether or not the nodes will be
            automatically repaired. When set to true, the
            nodes in this node pool will be monitored and if
            they fail health checks consistently over a
            period of time, an automatic repair action will
            be triggered to replace them with new nodes.
    """

    auto_repair: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AzureNodeConfig(proto.Message):
    r"""Parameters that describe the configuration of all node
    machines on a given node pool.

    Attributes:
        vm_size (str):
            Optional. The Azure VM size name. Example:
            ``Standard_DS2_v2``.

            See `Supported VM
            sizes </anthos/clusters/docs/azure/reference/supported-vms>`__
            for options.

            When unspecified, it defaults to ``Standard_DS2_v2``.
        root_volume (google.cloud.gke_multicloud_v1.types.AzureDiskTemplate):
            Optional. Configuration related to the root
            volume provisioned for each node pool machine.

            When unspecified, it defaults to a 32-GiB Azure
            Disk.
        tags (MutableMapping[str, str]):
            Optional. A set of tags to apply to all underlying Azure
            resources for this node pool. This currently only includes
            Virtual Machine Scale Sets.

            Specify at most 50 pairs containing alphanumerics, spaces,
            and symbols (.+-=\_:@/). Keys can be up to 127 Unicode
            characters. Values can be up to 255 Unicode characters.
        image_type (str):
            Optional. The OS image type to use on node pool instances.
            Can be unspecified, or have a value of ``ubuntu``.

            When unspecified, it defaults to ``ubuntu``.
        ssh_config (google.cloud.gke_multicloud_v1.types.AzureSshConfig):
            Required. SSH configuration for how to access
            the node pool machines.
        proxy_config (google.cloud.gke_multicloud_v1.types.AzureProxyConfig):
            Optional. Proxy configuration for outbound
            HTTP(S) traffic.
        config_encryption (google.cloud.gke_multicloud_v1.types.AzureConfigEncryption):
            Optional. Configuration related to vm config
            encryption.
        taints (MutableSequence[google.cloud.gke_multicloud_v1.types.NodeTaint]):
            Optional. The initial taints assigned to
            nodes of this node pool.
        labels (MutableMapping[str, str]):
            Optional. The initial labels assigned to
            nodes of this node pool. An object containing a
            list of "key": value pairs. Example: { "name":
            "wrench", "mass": "1.3kg", "count": "3" }.
    """

    vm_size: str = proto.Field(
        proto.STRING,
        number=1,
    )
    root_volume: "AzureDiskTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AzureDiskTemplate",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    image_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    ssh_config: "AzureSshConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AzureSshConfig",
    )
    proxy_config: "AzureProxyConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="AzureProxyConfig",
    )
    config_encryption: "AzureConfigEncryption" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AzureConfigEncryption",
    )
    taints: MutableSequence[common_resources.NodeTaint] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=common_resources.NodeTaint,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )


class AzureNodePoolAutoscaling(proto.Message):
    r"""Configuration related to Kubernetes cluster autoscaler.

    The Kubernetes cluster autoscaler will automatically adjust the
    size of the node pool based on the cluster load.

    Attributes:
        min_node_count (int):
            Required. Minimum number of nodes in the node pool. Must be
            greater than or equal to 1 and less than or equal to
            max_node_count.
        max_node_count (int):
            Required. Maximum number of nodes in the node pool. Must be
            greater than or equal to min_node_count and less than or
            equal to 50.
    """

    min_node_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_node_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class AzureOpenIdConfig(proto.Message):
    r"""AzureOpenIdConfig is an OIDC discovery document for the
    cluster. See the OpenID Connect Discovery 1.0 specification for
    details.

    Attributes:
        issuer (str):
            OIDC Issuer.
        jwks_uri (str):
            JSON Web Key uri.
        response_types_supported (MutableSequence[str]):
            Supported response types.
        subject_types_supported (MutableSequence[str]):
            Supported subject types.
        id_token_signing_alg_values_supported (MutableSequence[str]):
            supported ID Token signing Algorithms.
        claims_supported (MutableSequence[str]):
            Supported claims.
        grant_types (MutableSequence[str]):
            Supported grant types.
    """

    issuer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    jwks_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    response_types_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    subject_types_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    id_token_signing_alg_values_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    claims_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    grant_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class AzureJsonWebKeys(proto.Message):
    r"""AzureJsonWebKeys is a valid JSON Web Key Set as specififed in
    RFC 7517.

    Attributes:
        keys (MutableSequence[google.cloud.gke_multicloud_v1.types.Jwk]):
            The public component of the keys used by the
            cluster to sign token requests.
    """

    keys: MutableSequence[common_resources.Jwk] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_resources.Jwk,
    )


class AzureServerConfig(proto.Message):
    r"""AzureServerConfig contains information about a Google Cloud
    location, such as supported Azure regions and Kubernetes
    versions.

    Attributes:
        name (str):
            The ``AzureServerConfig`` resource name.

            ``AzureServerConfig`` names are formatted as
            ``projects/<project-number>/locations/<region>/azureServerConfig``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
        valid_versions (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureK8sVersionInfo]):
            List of all released Kubernetes versions, including ones
            which are end of life and can no longer be used. Filter by
            the ``enabled`` property to limit to currently available
            versions. Valid versions supported for both create and
            update operations
        supported_azure_regions (MutableSequence[str]):
            The list of supported Azure regions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    valid_versions: MutableSequence["AzureK8sVersionInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AzureK8sVersionInfo",
    )
    supported_azure_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AzureK8sVersionInfo(proto.Message):
    r"""Kubernetes version information of GKE cluster on Azure.

    Attributes:
        version (str):
            Kubernetes version name (for example, ``1.19.10-gke.1000``)
        enabled (bool):
            Optional. True if the version is available
            for cluster creation. If a version is enabled
            for creation, it can be used to create new
            clusters. Otherwise, cluster creation will fail.
            However, cluster upgrade operations may succeed,
            even if the version is not enabled.
        end_of_life (bool):
            Optional. True if this cluster version
            belongs to a minor version that has reached its
            end of life and is no longer in scope to receive
            security and bug fixes.
        end_of_life_date (google.type.date_pb2.Date):
            Optional. The estimated date (in Pacific Time) when this
            cluster version will reach its end of life. Or if this
            version is no longer supported (the ``end_of_life`` field is
            true), this is the actual date (in Pacific time) when the
            version reached its end of life.
        release_date (google.type.date_pb2.Date):
            Optional. The date (in Pacific Time) when the
            cluster version was released.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    end_of_life: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    end_of_life_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=5,
        message=date_pb2.Date,
    )
    release_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=6,
        message=date_pb2.Date,
    )


class AzureSshConfig(proto.Message):
    r"""SSH configuration for Azure resources.

    Attributes:
        authorized_key (str):
            Required. The SSH public key data for VMs managed by Anthos.
            This accepts the authorized_keys file format used in OpenSSH
            according to the sshd(8) manual page.
    """

    authorized_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AzureClusterResources(proto.Message):
    r"""Managed Azure resources for the cluster.

    The values could change and be empty, depending on the state of
    the cluster.

    Attributes:
        network_security_group_id (str):
            Output only. The ARM ID of the cluster
            network security group.
        control_plane_application_security_group_id (str):
            Output only. The ARM ID of the control plane
            application security group.
    """

    network_security_group_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    control_plane_application_security_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureClusterError(proto.Message):
    r"""AzureClusterError describes errors found on Azure clusters.

    Attributes:
        message (str):
            Human-friendly description of the error.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AzureNodePoolError(proto.Message):
    r"""AzureNodePoolError describes errors found on Azure node
    pools.

    Attributes:
        message (str):
            Human-friendly description of the error.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
