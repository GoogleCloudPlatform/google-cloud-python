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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "AutoscalingPolicy",
        "BasicAutoscalingAlgorithm",
        "BasicYarnAutoscalingConfig",
        "InstanceGroupAutoscalingPolicyConfig",
        "CreateAutoscalingPolicyRequest",
        "GetAutoscalingPolicyRequest",
        "UpdateAutoscalingPolicyRequest",
        "DeleteAutoscalingPolicyRequest",
        "ListAutoscalingPoliciesRequest",
        "ListAutoscalingPoliciesResponse",
    },
)


class AutoscalingPolicy(proto.Message):
    r"""Describes an autoscaling policy for Dataproc cluster
    autoscaler.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Required. The policy id.

            The id must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). Cannot begin or end with
            underscore or hyphen. Must consist of between 3 and 50
            characters.
        name (str):
            Output only. The "resource name" of the autoscaling policy,
            as described in
            https://cloud.google.com/apis/design/resource_names.

            - For ``projects.regions.autoscalingPolicies``, the resource
              name of the policy has the following format:
              ``projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}``

            - For ``projects.locations.autoscalingPolicies``, the
              resource name of the policy has the following format:
              ``projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}``
        basic_algorithm (google.cloud.dataproc_v1.types.BasicAutoscalingAlgorithm):

            This field is a member of `oneof`_ ``algorithm``.
        worker_config (google.cloud.dataproc_v1.types.InstanceGroupAutoscalingPolicyConfig):
            Required. Describes how the autoscaler will
            operate for primary workers.
        secondary_worker_config (google.cloud.dataproc_v1.types.InstanceGroupAutoscalingPolicyConfig):
            Optional. Describes how the autoscaler will
            operate for secondary workers.
        labels (MutableMapping[str, str]):
            Optional. The labels to associate with this autoscaling
            policy. Label **keys** must contain 1 to 63 characters, and
            must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. Label
            **values** may be empty, but, if present, must contain 1 to
            63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with an autoscaling policy.
        cluster_type (google.cloud.dataproc_v1.types.AutoscalingPolicy.ClusterType):
            Optional. The type of the clusters for which
            this autoscaling policy is to be configured.
    """

    class ClusterType(proto.Enum):
        r"""The type of the clusters for which this autoscaling policy is
        to be configured.

        Values:
            CLUSTER_TYPE_UNSPECIFIED (0):
                Not set.
            STANDARD (1):
                Standard dataproc cluster with a minimum of
                two primary workers.
            ZERO_SCALE (2):
                Clusters that can use only secondary workers
                and be scaled down to zero secondary worker
                nodes.
        """

        CLUSTER_TYPE_UNSPECIFIED = 0
        STANDARD = 1
        ZERO_SCALE = 2

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    basic_algorithm: "BasicAutoscalingAlgorithm" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="algorithm",
        message="BasicAutoscalingAlgorithm",
    )
    worker_config: "InstanceGroupAutoscalingPolicyConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="InstanceGroupAutoscalingPolicyConfig",
    )
    secondary_worker_config: "InstanceGroupAutoscalingPolicyConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="InstanceGroupAutoscalingPolicyConfig",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    cluster_type: ClusterType = proto.Field(
        proto.ENUM,
        number=7,
        enum=ClusterType,
    )


class BasicAutoscalingAlgorithm(proto.Message):
    r"""Basic algorithm for autoscaling.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        yarn_config (google.cloud.dataproc_v1.types.BasicYarnAutoscalingConfig):
            Required. YARN autoscaling configuration.

            This field is a member of `oneof`_ ``config``.
        cooldown_period (google.protobuf.duration_pb2.Duration):
            Optional. Duration between scaling events. A scaling period
            starts after the update operation from the previous event
            has completed.

            Bounds: [2m, 1d]. Default: 2m.
    """

    yarn_config: "BasicYarnAutoscalingConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="config",
        message="BasicYarnAutoscalingConfig",
    )
    cooldown_period: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class BasicYarnAutoscalingConfig(proto.Message):
    r"""Basic autoscaling configurations for YARN.

    Attributes:
        graceful_decommission_timeout (google.protobuf.duration_pb2.Duration):
            Required. Timeout for YARN graceful decommissioning of Node
            Managers. Specifies the duration to wait for jobs to
            complete before forcefully removing workers (and potentially
            interrupting jobs). Only applicable to downscaling
            operations.

            Bounds: [0s, 1d].
        scale_up_factor (float):
            Required. Fraction of average YARN pending memory in the
            last cooldown period for which to add workers. A scale-up
            factor of 1.0 will result in scaling up so that there is no
            pending memory remaining after the update (more aggressive
            scaling). A scale-up factor closer to 0 will result in a
            smaller magnitude of scaling up (less aggressive scaling).
            See `How autoscaling
            works <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works>`__
            for more information.

            Bounds: [0.0, 1.0].
        scale_down_factor (float):
            Required. Fraction of average YARN pending memory in the
            last cooldown period for which to remove workers. A
            scale-down factor of 1 will result in scaling down so that
            there is no available memory remaining after the update
            (more aggressive scaling). A scale-down factor of 0 disables
            removing workers, which can be beneficial for autoscaling a
            single job. See `How autoscaling
            works <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works>`__
            for more information.

            Bounds: [0.0, 1.0].
        scale_up_min_worker_fraction (float):
            Optional. Minimum scale-up threshold as a fraction of total
            cluster size before scaling occurs. For example, in a
            20-worker cluster, a threshold of 0.1 means the autoscaler
            must recommend at least a 2-worker scale-up for the cluster
            to scale. A threshold of 0 means the autoscaler will scale
            up on any recommended change.

            Bounds: [0.0, 1.0]. Default: 0.0.
        scale_down_min_worker_fraction (float):
            Optional. Minimum scale-down threshold as a fraction of
            total cluster size before scaling occurs. For example, in a
            20-worker cluster, a threshold of 0.1 means the autoscaler
            must recommend at least a 2 worker scale-down for the
            cluster to scale. A threshold of 0 means the autoscaler will
            scale down on any recommended change.

            Bounds: [0.0, 1.0]. Default: 0.0.
    """

    graceful_decommission_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    scale_up_factor: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    scale_down_factor: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    scale_up_min_worker_fraction: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    scale_down_min_worker_fraction: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )


class InstanceGroupAutoscalingPolicyConfig(proto.Message):
    r"""Configuration for the size bounds of an instance group,
    including its proportional size to other groups.

    Attributes:
        min_instances (int):
            Optional. Minimum number of instances for this group.

            Primary workers - Bounds: [2, max_instances]. Default: 2.
            Secondary workers - Bounds: [0, max_instances]. Default: 0.
        max_instances (int):
            Required. Maximum number of instances for this group.
            Required for primary workers. Note that by default, clusters
            will not use secondary workers. Required for secondary
            workers if the minimum secondary instances is set.

            Primary workers - Bounds: [min_instances, ). Secondary
            workers - Bounds: [min_instances, ). Default: 0.
        weight (int):
            Optional. Weight for the instance group, which is used to
            determine the fraction of total workers in the cluster from
            this instance group. For example, if primary workers have
            weight 2, and secondary workers have weight 1, the cluster
            will have approximately 2 primary workers for each secondary
            worker.

            The cluster may not reach the specified balance if
            constrained by min/max bounds or other autoscaling settings.
            For example, if ``max_instances`` for secondary workers is
            0, then only primary workers will be added. The cluster can
            also be out of balance when created.

            If weight is not set on any instance group, the cluster will
            default to equal weight for all groups: the cluster will
            attempt to maintain an equal number of workers in each group
            within the configured size bounds for each group. If weight
            is set for one group only, the cluster will default to zero
            weight on the unset group. For example if weight is set only
            on primary workers, the cluster will use primary workers
            only and no secondary workers.
    """

    min_instances: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_instances: int = proto.Field(
        proto.INT32,
        number=2,
    )
    weight: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateAutoscalingPolicyRequest(proto.Message):
    r"""A request to create an autoscaling policy.

    Attributes:
        parent (str):
            Required. The "resource name" of the region or location, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            - For ``projects.regions.autoscalingPolicies.create``, the
              resource name of the region has the following format:
              ``projects/{project_id}/regions/{region}``

            - For ``projects.locations.autoscalingPolicies.create``, the
              resource name of the location has the following format:
              ``projects/{project_id}/locations/{location}``
        policy (google.cloud.dataproc_v1.types.AutoscalingPolicy):
            Required. The autoscaling policy to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy: "AutoscalingPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AutoscalingPolicy",
    )


class GetAutoscalingPolicyRequest(proto.Message):
    r"""A request to fetch an autoscaling policy.

    Attributes:
        name (str):
            Required. The "resource name" of the autoscaling policy, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            - For ``projects.regions.autoscalingPolicies.get``, the
              resource name of the policy has the following format:
              ``projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}``

            - For ``projects.locations.autoscalingPolicies.get``, the
              resource name of the policy has the following format:
              ``projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAutoscalingPolicyRequest(proto.Message):
    r"""A request to update an autoscaling policy.

    Attributes:
        policy (google.cloud.dataproc_v1.types.AutoscalingPolicy):
            Required. The updated autoscaling policy.
    """

    policy: "AutoscalingPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AutoscalingPolicy",
    )


class DeleteAutoscalingPolicyRequest(proto.Message):
    r"""A request to delete an autoscaling policy.

    Autoscaling policies in use by one or more clusters will not be
    deleted.

    Attributes:
        name (str):
            Required. The "resource name" of the autoscaling policy, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            - For ``projects.regions.autoscalingPolicies.delete``, the
              resource name of the policy has the following format:
              ``projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}``

            - For ``projects.locations.autoscalingPolicies.delete``, the
              resource name of the policy has the following format:
              ``projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAutoscalingPoliciesRequest(proto.Message):
    r"""A request to list autoscaling policies in a project.

    Attributes:
        parent (str):
            Required. The "resource name" of the region or location, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            - For ``projects.regions.autoscalingPolicies.list``, the
              resource name of the region has the following format:
              ``projects/{project_id}/regions/{region}``

            - For ``projects.locations.autoscalingPolicies.list``, the
              resource name of the location has the following format:
              ``projects/{project_id}/locations/{location}``
        page_size (int):
            Optional. The maximum number of results to
            return in each response. Must be less than or
            equal to 1000. Defaults to 100.
        page_token (str):
            Optional. The page token, returned by a
            previous call, to request the next page of
            results.
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


class ListAutoscalingPoliciesResponse(proto.Message):
    r"""A response to a request to list autoscaling policies in a
    project.

    Attributes:
        policies (MutableSequence[google.cloud.dataproc_v1.types.AutoscalingPolicy]):
            Output only. Autoscaling policies list.
        next_page_token (str):
            Output only. This token is included in the
            response if there are more results to fetch.
    """

    @property
    def raw_page(self):
        return self

    policies: MutableSequence["AutoscalingPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AutoscalingPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
