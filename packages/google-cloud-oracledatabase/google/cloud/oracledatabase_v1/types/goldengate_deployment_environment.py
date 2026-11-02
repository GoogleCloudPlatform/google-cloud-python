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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "GoldengateDeploymentEnvironment",
        "ListGoldengateDeploymentEnvironmentsRequest",
        "ListGoldengateDeploymentEnvironmentsResponse",
    },
)


class GoldengateDeploymentEnvironment(proto.Message):
    r"""Details of the Goldengate Deployment Environment resource.

    Attributes:
        name (str):
            Identifier. The name of the Goldengate Deployment
            Environment resource with the format:
            projects/{project}/locations/{location}/goldengateDeploymentEnvironments/{goldengate_deployment_environment}
        category (google.cloud.oracledatabase_v1.types.GoldengateDeploymentEnvironment.DeploymentCategory):
            Output only. The category of the Goldengate
            Deployment Environment resource.
        display_name (str):
            The display name of the Goldengate Deployment
            Environment resource.
        default_cpu_core_count (int):
            Output only. The default CPU core count of
            the Goldengate Deployment Environment resource.
        environment_type (google.cloud.oracledatabase_v1.types.GoldengateDeploymentEnvironment.DeploymentEnvironmentType):
            Output only. The environment type of the
            Goldengate Deployment Environment resource.
        auto_scaling_enabled (bool):
            Output only. Whether auto scaling is enabled
            by default for the Goldengate Deployment
            Environment resource.
        max_cpu_core_count (int):
            Output only. The max CPU core count of the
            Goldengate Deployment Environment resource.
        memory_gb_per_cpu_core (int):
            Output only. The memory per CPU core in GBs
            of the Goldengate Deployment Environment
            resource.
        min_cpu_core_count (int):
            Output only. The min CPU core count of the
            Goldengate Deployment Environment resource.
        network_bandwidth_gbps_per_cpu_core (int):
            Output only. The network bandwidth per CPU
            core in Gbps of the Goldengate Deployment
            Environment resource.
        storage_usage_limit_gb_per_cpu_core (int):
            Output only. The storage usage limit per CPU
            core in GBs of the Goldengate Deployment
            Environment resource.
    """

    class DeploymentCategory(proto.Enum):
        r"""Deployment category of the Goldengate Deployment resource.

        Values:
            DEPLOYMENT_CATEGORY_UNSPECIFIED (0):
                Default unspecified value.
            DATA_REPLICATION_CATEGORY (1):
                Goldengate Deployment Environment category is
                DATA_REPLICATION_CATEGORY.
            DATA_TRANSFORMS_CATEGORY (2):
                Goldengate Deployment Environment category is
                DATA_TRANSFORMS_CATEGORY.
        """

        DEPLOYMENT_CATEGORY_UNSPECIFIED = 0
        DATA_REPLICATION_CATEGORY = 1
        DATA_TRANSFORMS_CATEGORY = 2

    class DeploymentEnvironmentType(proto.Enum):
        r"""The environment type of the Goldengate Deployment Environment
        resource.

        Values:
            DEPLOYMENT_ENVIRONMENT_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            PRODUCTION (1):
                Goldengate Deployment Environment type is
                PRODUCTION.
            DEVELOPMENT_OR_TESTING (2):
                Goldengate Deployment Environment type is
                DEVELOPMENT_OR_TESTING.
        """

        DEPLOYMENT_ENVIRONMENT_TYPE_UNSPECIFIED = 0
        PRODUCTION = 1
        DEVELOPMENT_OR_TESTING = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    category: DeploymentCategory = proto.Field(
        proto.ENUM,
        number=2,
        enum=DeploymentCategory,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    default_cpu_core_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    environment_type: DeploymentEnvironmentType = proto.Field(
        proto.ENUM,
        number=5,
        enum=DeploymentEnvironmentType,
    )
    auto_scaling_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    max_cpu_core_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    memory_gb_per_cpu_core: int = proto.Field(
        proto.INT32,
        number=8,
    )
    min_cpu_core_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    network_bandwidth_gbps_per_cpu_core: int = proto.Field(
        proto.INT32,
        number=10,
    )
    storage_usage_limit_gb_per_cpu_core: int = proto.Field(
        proto.INT32,
        number=11,
    )


class ListGoldengateDeploymentEnvironmentsRequest(proto.Message):
    r"""Message for listing GoldengateDeploymentEnvironments.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of GoldengateDeploymentEnvironments.
            Format:

            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 deployment
            environments will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListGoldengateDeploymentEnvironmentsResponse(proto.Message):
    r"""Message for response to listing
    GoldengateDeploymentEnvironments

    Attributes:
        goldengate_deployment_environments (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateDeploymentEnvironment]):
            The list of GoldengateDeploymentEnvironment
        next_page_token (str):
            A token identifying a page of results the
            server should return. If this field is empty,
            there are no subsequent pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    goldengate_deployment_environments: MutableSequence[
        "GoldengateDeploymentEnvironment"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GoldengateDeploymentEnvironment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
