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
    package="google.cloud.run.v2",
    manifest={
        "IngressTraffic",
        "ExecutionEnvironment",
        "EncryptionKeyRevocationAction",
        "VpcAccess",
        "BinaryAuthorization",
        "RevisionScaling",
        "ServiceMesh",
        "ServiceScaling",
        "WorkerPoolScaling",
        "NodeSelector",
        "BuildConfig",
    },
)


class IngressTraffic(proto.Enum):
    r"""Allowed ingress traffic for the Container.

    Values:
        INGRESS_TRAFFIC_UNSPECIFIED (0):
            Unspecified
        INGRESS_TRAFFIC_ALL (1):
            All inbound traffic is allowed.
        INGRESS_TRAFFIC_INTERNAL_ONLY (2):
            Only internal traffic is allowed.
        INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER (3):
            Both internal and Google Cloud Load Balancer
            traffic is allowed.
        INGRESS_TRAFFIC_NONE (4):
            No ingress traffic is allowed.
    """

    INGRESS_TRAFFIC_UNSPECIFIED = 0
    INGRESS_TRAFFIC_ALL = 1
    INGRESS_TRAFFIC_INTERNAL_ONLY = 2
    INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER = 3
    INGRESS_TRAFFIC_NONE = 4


class ExecutionEnvironment(proto.Enum):
    r"""Alternatives for execution environments.

    Values:
        EXECUTION_ENVIRONMENT_UNSPECIFIED (0):
            Unspecified
        EXECUTION_ENVIRONMENT_GEN1 (1):
            Uses the First Generation environment.
        EXECUTION_ENVIRONMENT_GEN2 (2):
            Uses Second Generation environment.
    """

    EXECUTION_ENVIRONMENT_UNSPECIFIED = 0
    EXECUTION_ENVIRONMENT_GEN1 = 1
    EXECUTION_ENVIRONMENT_GEN2 = 2


class EncryptionKeyRevocationAction(proto.Enum):
    r"""Specifies behavior if an encryption key used by a resource is
    revoked.

    Values:
        ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED (0):
            Unspecified
        PREVENT_NEW (1):
            Prevents the creation of new instances.
        SHUTDOWN (2):
            Shuts down existing instances, and prevents
            creation of new ones.
    """

    ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED = 0
    PREVENT_NEW = 1
    SHUTDOWN = 2


class VpcAccess(proto.Message):
    r"""VPC Access settings. For more information on sending traffic
    to a VPC network, visit
    https://cloud.google.com/run/docs/configuring/connecting-vpc.

    Attributes:
        connector (str):
            VPC Access connector name. Format:
            ``projects/{project}/locations/{location}/connectors/{connector}``,
            where ``{project}`` can be project id or number. For more
            information on sending traffic to a VPC network via a
            connector, visit
            https://cloud.google.com/run/docs/configuring/vpc-connectors.
        egress (google.cloud.run_v2.types.VpcAccess.VpcEgress):
            Optional. Traffic VPC egress settings. If not provided, it
            defaults to PRIVATE_RANGES_ONLY.
        network_interfaces (MutableSequence[google.cloud.run_v2.types.VpcAccess.NetworkInterface]):
            Optional. Direct VPC egress settings.
            Currently only single network interface is
            supported.
    """

    class VpcEgress(proto.Enum):
        r"""Egress options for VPC access.

        Values:
            VPC_EGRESS_UNSPECIFIED (0):
                Unspecified
            ALL_TRAFFIC (1):
                All outbound traffic is routed through the
                VPC connector.
            PRIVATE_RANGES_ONLY (2):
                Only private IP ranges are routed through the
                VPC connector.
        """

        VPC_EGRESS_UNSPECIFIED = 0
        ALL_TRAFFIC = 1
        PRIVATE_RANGES_ONLY = 2

    class NetworkInterface(proto.Message):
        r"""Direct VPC egress settings.

        Attributes:
            network (str):
                Optional. The VPC network that the Cloud Run
                resource will be able to send traffic to. At
                least one of network or subnetwork must be
                specified. If both network and subnetwork are
                specified, the given VPC subnetwork must belong
                to the given VPC network. If network is not
                specified, it will be looked up from the
                subnetwork.
            subnetwork (str):
                Optional. The VPC subnetwork that the Cloud
                Run resource will get IPs from. At least one of
                network or subnetwork must be specified. If both
                network and subnetwork are specified, the given
                VPC subnetwork must belong to the given VPC
                network. If subnetwork is not specified, the
                subnetwork with the same name with the network
                will be used.
            tags (MutableSequence[str]):
                Optional. Network tags applied to this Cloud
                Run resource.
        """

        network: str = proto.Field(
            proto.STRING,
            number=1,
        )
        subnetwork: str = proto.Field(
            proto.STRING,
            number=2,
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    connector: str = proto.Field(
        proto.STRING,
        number=1,
    )
    egress: VpcEgress = proto.Field(
        proto.ENUM,
        number=2,
        enum=VpcEgress,
    )
    network_interfaces: MutableSequence[NetworkInterface] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=NetworkInterface,
    )


class BinaryAuthorization(proto.Message):
    r"""Settings for Binary Authorization feature.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        use_default (bool):
            Optional. If True, indicates to use the
            default project's binary authorization policy.
            If False, binary authorization will be disabled.

            This field is a member of `oneof`_ ``binauthz_method``.
        policy (str):
            Optional. The path to a binary authorization policy. Format:
            ``projects/{project}/platforms/cloudRun/{policy-name}``

            This field is a member of `oneof`_ ``binauthz_method``.
        breakglass_justification (str):
            Optional. If present, indicates to use Breakglass using this
            justification. If use_default is False, then it must be
            empty. For more information on breakglass, see
            https://cloud.google.com/binary-authorization/docs/using-breakglass
    """

    use_default: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="binauthz_method",
    )
    policy: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="binauthz_method",
    )
    breakglass_justification: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RevisionScaling(proto.Message):
    r"""Settings for revision-level scaling settings.

    Attributes:
        min_instance_count (int):
            Optional. Minimum number of serving instances
            that this resource should have.
        max_instance_count (int):
            Optional. Maximum number of serving instances
            that this resource should have. When
            unspecified, the field is set to the server
            default value of
            100. For more information see
            https://cloud.google.com/run/docs/configuring/max-instances
    """

    min_instance_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_instance_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ServiceMesh(proto.Message):
    r"""Settings for Cloud Service Mesh. For more information see
    https://cloud.google.com/service-mesh/docs/overview.

    Attributes:
        mesh (str):
            The Mesh resource name. Format:
            ``projects/{project}/locations/global/meshes/{mesh}``, where
            ``{project}`` can be project id or number.
    """

    mesh: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ServiceScaling(proto.Message):
    r"""Scaling settings applied at the service level rather than
    at the revision level.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        min_instance_count (int):
            Optional. total min instances for the
            service. This number of instances is divided
            among all revisions with specified traffic based
            on the percent of traffic they are receiving.
        scaling_mode (google.cloud.run_v2.types.ServiceScaling.ScalingMode):
            Optional. The scaling mode for the service.
        max_instance_count (int):
            Optional. total max instances for the
            service. This number of instances is divided
            among all revisions with specified traffic based
            on the percent of traffic they are receiving.
        manual_instance_count (int):
            Optional. total instance count for the
            service in manual scaling mode. This number of
            instances is divided among all revisions with
            specified traffic based on the percent of
            traffic they are receiving.

            This field is a member of `oneof`_ ``_manual_instance_count``.
    """

    class ScalingMode(proto.Enum):
        r"""The scaling mode for the service. If not provided, it
        defaults to AUTOMATIC.

        Values:
            SCALING_MODE_UNSPECIFIED (0):
                Unspecified.
            AUTOMATIC (1):
                Scale based on traffic between min and max
                instances.
            MANUAL (2):
                Scale to exactly min instances and ignore max
                instances.
        """

        SCALING_MODE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    min_instance_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    scaling_mode: ScalingMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=ScalingMode,
    )
    max_instance_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    manual_instance_count: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )


class WorkerPoolScaling(proto.Message):
    r"""Worker pool scaling settings.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        manual_instance_count (int):
            Optional. The total number of instances in
            manual scaling mode.

            This field is a member of `oneof`_ ``_manual_instance_count``.
    """

    manual_instance_count: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )


class NodeSelector(proto.Message):
    r"""Hardware constraints configuration.

    Attributes:
        accelerator (str):
            Required. GPU accelerator type to attach to
            an instance.
    """

    accelerator: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BuildConfig(proto.Message):
    r"""Describes the Build step of the function that builds a
    container from the given source.

    Attributes:
        name (str):
            Output only. The Cloud Build name of the
            latest successful deployment of the function.
        source_location (str):
            The Cloud Storage bucket URI where the
            function source code is located.
        function_target (str):
            Optional. The name of the function (as
            defined in source code) that will be executed.
            Defaults to the resource name suffix, if not
            specified. For backward compatibility, if
            function with given name is not found, then the
            system will try to use function named
            "function".
        image_uri (str):
            Optional. Artifact Registry URI to store the
            built image.
        base_image (str):
            Optional. The base image used to build the
            function.
        enable_automatic_updates (bool):
            Optional. Sets whether the function will
            receive automatic base image updates.
        worker_pool (str):
            Optional. Name of the Cloud Build Custom Worker Pool that
            should be used to build the Cloud Run function. The format
            of this field is
            ``projects/{project}/locations/{region}/workerPools/{workerPool}``
            where ``{project}`` and ``{region}`` are the project id and
            region respectively where the worker pool is defined and
            ``{workerPool}`` is the short name of the worker pool.
        environment_variables (MutableMapping[str, str]):
            Optional. User-provided build-time
            environment variables for the function
        service_account (str):
            Optional. Service account to be used for building the
            container. The format of this field is
            ``projects/{projectId}/serviceAccounts/{serviceAccountEmail}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    function_target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    image_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    base_image: str = proto.Field(
        proto.STRING,
        number=5,
    )
    enable_automatic_updates: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=7,
    )
    environment_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
