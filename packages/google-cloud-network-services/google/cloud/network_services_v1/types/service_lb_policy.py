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
    package="google.cloud.networkservices.v1",
    manifest={
        "ServiceLbPolicy",
        "ListServiceLbPoliciesRequest",
        "ListServiceLbPoliciesResponse",
        "GetServiceLbPolicyRequest",
        "CreateServiceLbPolicyRequest",
        "UpdateServiceLbPolicyRequest",
        "DeleteServiceLbPolicyRequest",
    },
)


class ServiceLbPolicy(proto.Message):
    r"""ServiceLbPolicy holds global load balancing and traffic
    distribution configuration that can be applied to a
    BackendService.

    Attributes:
        name (str):
            Identifier. Name of the ServiceLbPolicy resource. It matches
            pattern
            ``projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this resource
            was last updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the ServiceLbPolicy resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        load_balancing_algorithm (google.cloud.network_services_v1.types.ServiceLbPolicy.LoadBalancingAlgorithm):
            Optional. The type of load balancing algorithm to be used.
            The default behavior is WATERFALL_BY_REGION.
        auto_capacity_drain (google.cloud.network_services_v1.types.ServiceLbPolicy.AutoCapacityDrain):
            Optional. Configuration to automatically move
            traffic away for unhealthy IG/NEG for the
            associated Backend Service.
        failover_config (google.cloud.network_services_v1.types.ServiceLbPolicy.FailoverConfig):
            Optional. Configuration related to health
            based failover.
        isolation_config (google.cloud.network_services_v1.types.ServiceLbPolicy.IsolationConfig):
            Optional. Configuration to provide isolation
            support for the associated Backend Service.
    """

    class LoadBalancingAlgorithm(proto.Enum):
        r"""The global load balancing algorithm to be used.

        Values:
            LOAD_BALANCING_ALGORITHM_UNSPECIFIED (0):
                The type of the loadbalancing algorithm is
                unspecified.
            SPRAY_TO_WORLD (3):
                Balance traffic across all backends across
                the world proportionally based on capacity.
            SPRAY_TO_REGION (4):
                Direct traffic to the nearest region with
                endpoints and capacity before spilling over to
                other regions and spread the traffic from each
                client to all the MIGs/NEGs in a region.
            WATERFALL_BY_REGION (5):
                Direct traffic to the nearest region with
                endpoints and capacity before spilling over to
                other regions. All MIGs/NEGs within a region are
                evenly loaded but each client might not spread
                the traffic to all the MIGs/NEGs in the region.
            WATERFALL_BY_ZONE (6):
                Attempt to keep traffic in a single zone
                closest to the client, before spilling over to
                other zones.
        """

        LOAD_BALANCING_ALGORITHM_UNSPECIFIED = 0
        SPRAY_TO_WORLD = 3
        SPRAY_TO_REGION = 4
        WATERFALL_BY_REGION = 5
        WATERFALL_BY_ZONE = 6

    class IsolationGranularity(proto.Enum):
        r"""The granularity of this isolation restriction.

        Values:
            ISOLATION_GRANULARITY_UNSPECIFIED (0):
                No isolation is configured for the backend
                service. Traffic can overflow based on the load
                balancing algorithm.
            REGION (1):
                Traffic for this service will be isolated at
                the cloud region level.
        """

        ISOLATION_GRANULARITY_UNSPECIFIED = 0
        REGION = 1

    class IsolationMode(proto.Enum):
        r"""The mode of this isolation restriction, defining whether
        clients in a given region are allowed to reach out to another
        region.

        Values:
            ISOLATION_MODE_UNSPECIFIED (0):
                No isolation mode is configured for the
                backend service.
            NEAREST (1):
                Traffic will be sent to the nearest region.
            STRICT (2):
                Traffic will fail if no serving backends are
                available in the same region as the load
                balancer.
        """

        ISOLATION_MODE_UNSPECIFIED = 0
        NEAREST = 1
        STRICT = 2

    class AutoCapacityDrain(proto.Message):
        r"""Option to specify if an unhealthy IG/NEG should be considered
        for global load balancing and traffic routing.

        Attributes:
            enable (bool):
                Optional. If set to 'True', an unhealthy
                IG/NEG will be set as drained.
                - An IG/NEG is considered unhealthy if less than
                  25% of the instances/endpoints in the IG/NEG
                  are healthy.
                - This option will never result in draining more
                  than 50% of the configured IGs/NEGs for the
                  Backend Service.
        """

        enable: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class FailoverConfig(proto.Message):
        r"""Option to specify health based failover behavior.
        This is not related to Network load balancer FailoverPolicy.

        Attributes:
            failover_health_threshold (int):
                Optional. The percentage threshold that a
                load balancer will begin to send traffic to
                failover backends. If the percentage of
                endpoints in a MIG/NEG is smaller than this
                value, traffic would be sent to failover
                backends if possible. This field should be set
                to a value between 1 and 99. The default value
                is 50 for Global external HTTP(S) load balancer
                (classic) and Proxyless service mesh, and 70 for
                others.
        """

        failover_health_threshold: int = proto.Field(
            proto.INT32,
            number=1,
        )

    class IsolationConfig(proto.Message):
        r"""Configuration to provide isolation support for the associated
        Backend Service.

        Attributes:
            isolation_granularity (google.cloud.network_services_v1.types.ServiceLbPolicy.IsolationGranularity):
                Optional. The isolation granularity of the
                load balancer.
            isolation_mode (google.cloud.network_services_v1.types.ServiceLbPolicy.IsolationMode):
                Optional. The isolation mode of the load
                balancer.
        """

        isolation_granularity: "ServiceLbPolicy.IsolationGranularity" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ServiceLbPolicy.IsolationGranularity",
        )
        isolation_mode: "ServiceLbPolicy.IsolationMode" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ServiceLbPolicy.IsolationMode",
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    load_balancing_algorithm: LoadBalancingAlgorithm = proto.Field(
        proto.ENUM,
        number=6,
        enum=LoadBalancingAlgorithm,
    )
    auto_capacity_drain: AutoCapacityDrain = proto.Field(
        proto.MESSAGE,
        number=8,
        message=AutoCapacityDrain,
    )
    failover_config: FailoverConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=FailoverConfig,
    )
    isolation_config: IsolationConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=IsolationConfig,
    )


class ListServiceLbPoliciesRequest(proto.Message):
    r"""Request used with the ListServiceLbPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ServiceLbPolicies should be listed, specified in the format
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Maximum number of ServiceLbPolicies to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListServiceLbPoliciesResponse`` Indicates that this is a
            continuation of a prior ``ListRouters`` call, and that the
            system should return the next page of data.
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


class ListServiceLbPoliciesResponse(proto.Message):
    r"""Response returned by the ListServiceLbPolicies method.

    Attributes:
        service_lb_policies (MutableSequence[google.cloud.network_services_v1.types.ServiceLbPolicy]):
            List of ServiceLbPolicy resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the
            request attempts to list all resources across
            all supported locations, while some locations
            are temporarily unavailable.
    """

    @property
    def raw_page(self):
        return self

    service_lb_policies: MutableSequence["ServiceLbPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ServiceLbPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServiceLbPolicyRequest(proto.Message):
    r"""Request used by the GetServiceLbPolicy method.

    Attributes:
        name (str):
            Required. A name of the ServiceLbPolicy to get. Must be in
            the format
            ``projects/{project}/locations/{location}/serviceLbPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceLbPolicyRequest(proto.Message):
    r"""Request used by the ServiceLbPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the ServiceLbPolicy. Must
            be in the format
            ``projects/{project}/locations/{location}``.
        service_lb_policy_id (str):
            Required. Short name of the ServiceLbPolicy resource to be
            created. E.g. for resource name
            ``projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}``.
            the id is value of {service_lb_policy_name}
        service_lb_policy (google.cloud.network_services_v1.types.ServiceLbPolicy):
            Required. ServiceLbPolicy resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_lb_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_lb_policy: "ServiceLbPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServiceLbPolicy",
    )


class UpdateServiceLbPolicyRequest(proto.Message):
    r"""Request used by the UpdateServiceLbPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ServiceLbPolicy resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        service_lb_policy (google.cloud.network_services_v1.types.ServiceLbPolicy):
            Required. Updated ServiceLbPolicy resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    service_lb_policy: "ServiceLbPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServiceLbPolicy",
    )


class DeleteServiceLbPolicyRequest(proto.Message):
    r"""Request used by the DeleteServiceLbPolicy method.

    Attributes:
        name (str):
            Required. A name of the ServiceLbPolicy to delete. Must be
            in the format
            ``projects/{project}/locations/{location}/serviceLbPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
