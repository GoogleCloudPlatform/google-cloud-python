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
import google.api_core as api_core

from google.cloud.hypercomputecluster_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.hypercomputecluster_v1.services.hypercompute_cluster",
    "google.cloud.hypercomputecluster_v1.types.hypercompute_cluster",
    "google.cloud.hypercomputecluster_v1.types.operation_metadata",
}


from .services.hypercompute_cluster import (
    HypercomputeClusterAsyncClient,
    HypercomputeClusterClient,
)
from .types.hypercompute_cluster import (
    BootDisk,
    BucketReference,
    Cluster,
    ComputeInstance,
    ComputeInstanceSlurmNodeSet,
    ComputeResource,
    ComputeResourceConfig,
    CreateClusterRequest,
    DeleteClusterRequest,
    ExistingBucketConfig,
    ExistingFilestoreConfig,
    ExistingLustreConfig,
    ExistingNetworkConfig,
    FileShareConfig,
    FilestoreReference,
    GcsAutoclassConfig,
    GcsHierarchicalNamespaceConfig,
    GetClusterRequest,
    ListClustersRequest,
    ListClustersResponse,
    LustreReference,
    NetworkReference,
    NetworkResource,
    NetworkResourceConfig,
    NewBucketConfig,
    NewFilestoreConfig,
    NewFlexStartInstancesConfig,
    NewLustreConfig,
    NewNetworkConfig,
    NewOnDemandInstancesConfig,
    NewReservedInstancesConfig,
    NewSpotInstancesConfig,
    Orchestrator,
    SlurmLoginNodes,
    SlurmNodeSet,
    SlurmOrchestrator,
    SlurmPartition,
    StorageConfig,
    StorageResource,
    StorageResourceConfig,
    UpdateClusterRequest,
)
from .types.operation_metadata import (
    CheckClusterHealth,
    CreateFilestoreInstance,
    CreateLoginNode,
    CreateLustreInstance,
    CreateNetwork,
    CreateNodeset,
    CreateOrchestrator,
    CreatePartition,
    CreatePrivateServiceAccess,
    CreateStorageBucket,
    DeleteFilestoreInstance,
    DeleteLoginNode,
    DeleteLustreInstance,
    DeleteNetwork,
    DeleteNodeset,
    DeleteOrchestrator,
    DeletePartition,
    DeletePrivateServiceAccess,
    DeleteStorageBucket,
    OperationMetadata,
    OperationProgress,
    OperationStep,
    UpdateLoginNode,
    UpdateNodeset,
    UpdateOrchestrator,
    UpdatePartition,
)

__all__ = (
    "HypercomputeClusterAsyncClient",
    "BootDisk",
    "BucketReference",
    "CheckClusterHealth",
    "Cluster",
    "ComputeInstance",
    "ComputeInstanceSlurmNodeSet",
    "ComputeResource",
    "ComputeResourceConfig",
    "CreateClusterRequest",
    "CreateFilestoreInstance",
    "CreateLoginNode",
    "CreateLustreInstance",
    "CreateNetwork",
    "CreateNodeset",
    "CreateOrchestrator",
    "CreatePartition",
    "CreatePrivateServiceAccess",
    "CreateStorageBucket",
    "DeleteClusterRequest",
    "DeleteFilestoreInstance",
    "DeleteLoginNode",
    "DeleteLustreInstance",
    "DeleteNetwork",
    "DeleteNodeset",
    "DeleteOrchestrator",
    "DeletePartition",
    "DeletePrivateServiceAccess",
    "DeleteStorageBucket",
    "ExistingBucketConfig",
    "ExistingFilestoreConfig",
    "ExistingLustreConfig",
    "ExistingNetworkConfig",
    "FileShareConfig",
    "FilestoreReference",
    "GcsAutoclassConfig",
    "GcsHierarchicalNamespaceConfig",
    "GetClusterRequest",
    "HypercomputeClusterClient",
    "ListClustersRequest",
    "ListClustersResponse",
    "LustreReference",
    "NetworkReference",
    "NetworkResource",
    "NetworkResourceConfig",
    "NewBucketConfig",
    "NewFilestoreConfig",
    "NewFlexStartInstancesConfig",
    "NewLustreConfig",
    "NewNetworkConfig",
    "NewOnDemandInstancesConfig",
    "NewReservedInstancesConfig",
    "NewSpotInstancesConfig",
    "OperationMetadata",
    "OperationProgress",
    "OperationStep",
    "Orchestrator",
    "SlurmLoginNodes",
    "SlurmNodeSet",
    "SlurmOrchestrator",
    "SlurmPartition",
    "StorageConfig",
    "StorageResource",
    "StorageResourceConfig",
    "UpdateClusterRequest",
    "UpdateLoginNode",
    "UpdateNodeset",
    "UpdateOrchestrator",
    "UpdatePartition",
)

api_core.check_python_version("google.cloud.hypercomputecluster_v1")
api_core.check_dependency_versions("google.cloud.hypercomputecluster_v1")
