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
    package="google.cloud.networkmanagement.v1",
    manifest={
        "LoadBalancerType",
        "Trace",
        "Step",
        "InstanceInfo",
        "NetworkInfo",
        "FirewallInfo",
        "RouteInfo",
        "GoogleServiceInfo",
        "ForwardingRuleInfo",
        "LoadBalancerInfo",
        "LoadBalancerBackend",
        "HybridSubnetInfo",
        "VpnGatewayInfo",
        "VpnTunnelInfo",
        "InterconnectAttachmentInfo",
        "EndpointInfo",
        "DeliverInfo",
        "ForwardInfo",
        "AbortInfo",
        "DropInfo",
        "GKEMasterInfo",
        "GkePodInfo",
        "IpMasqueradingSkippedInfo",
        "GkeNetworkPolicyInfo",
        "GkeNetworkPolicySkippedInfo",
        "CloudSQLInstanceInfo",
        "RedisInstanceInfo",
        "RedisClusterInfo",
        "CloudFunctionInfo",
        "CloudRunRevisionInfo",
        "CloudRunJobInfo",
        "AppEngineVersionInfo",
        "VpcConnectorInfo",
        "DirectVpcEgressConnectionInfo",
        "ServerlessExternalConnectionInfo",
        "NatInfo",
        "ProxyConnectionInfo",
        "LoadBalancerBackendInfo",
        "StorageBucketInfo",
        "ServerlessNegInfo",
        "NgfwPacketInspectionInfo",
        "PrivateConnectionInfo",
    },
)


class LoadBalancerType(proto.Enum):
    r"""Type of a load balancer. For more information, see `Summary of
    Google Cloud load
    balancers <https://cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers>`__.

    Values:
        LOAD_BALANCER_TYPE_UNSPECIFIED (0):
            Forwarding rule points to a different target
            than a load balancer or a load balancer type is
            unknown.
        HTTPS_ADVANCED_LOAD_BALANCER (1):
            Global external HTTP(S) load balancer.
        HTTPS_LOAD_BALANCER (2):
            Global external HTTP(S) load balancer
            (classic)
        REGIONAL_HTTPS_LOAD_BALANCER (3):
            Regional external HTTP(S) load balancer.
        INTERNAL_HTTPS_LOAD_BALANCER (4):
            Internal HTTP(S) load balancer.
        SSL_PROXY_LOAD_BALANCER (5):
            External SSL proxy load balancer.
        TCP_PROXY_LOAD_BALANCER (6):
            External TCP proxy load balancer.
        INTERNAL_TCP_PROXY_LOAD_BALANCER (7):
            Internal regional TCP proxy load balancer.
        NETWORK_LOAD_BALANCER (8):
            External TCP/UDP Network load balancer.
        LEGACY_NETWORK_LOAD_BALANCER (9):
            Target-pool based external TCP/UDP Network
            load balancer.
        TCP_UDP_INTERNAL_LOAD_BALANCER (10):
            Internal TCP/UDP load balancer.
    """

    LOAD_BALANCER_TYPE_UNSPECIFIED = 0
    HTTPS_ADVANCED_LOAD_BALANCER = 1
    HTTPS_LOAD_BALANCER = 2
    REGIONAL_HTTPS_LOAD_BALANCER = 3
    INTERNAL_HTTPS_LOAD_BALANCER = 4
    SSL_PROXY_LOAD_BALANCER = 5
    TCP_PROXY_LOAD_BALANCER = 6
    INTERNAL_TCP_PROXY_LOAD_BALANCER = 7
    NETWORK_LOAD_BALANCER = 8
    LEGACY_NETWORK_LOAD_BALANCER = 9
    TCP_UDP_INTERNAL_LOAD_BALANCER = 10


class Trace(proto.Message):
    r"""Trace represents one simulated packet forwarding path.

    - Each trace contains multiple ordered steps.
    - Each step is in a particular state with associated configuration.
    - State is categorized as final or non-final states.
    - Each final state has a reason associated.
    - Each trace must end with a final state (the last step).

    ::

         |---------------------Trace----------------------|
         Step1(State) Step2(State) ---  StepN(State(final))

    Attributes:
        endpoint_info (google.cloud.network_management_v1.types.EndpointInfo):
            Derived from the source and destination endpoints definition
            specified by user request, and validated by the data plane
            model. If there are multiple traces starting from different
            source locations, then the endpoint_info may be different
            between traces.
        steps (MutableSequence[google.cloud.network_management_v1.types.Step]):
            A trace of a test contains multiple steps
            from the initial state to the final state
            (delivered, dropped, forwarded, or aborted).

            The steps are ordered by the processing sequence
            within the simulated network state machine. It
            is critical to preserve the order of the steps
            and avoid reordering or sorting them.
        forward_trace_id (int):
            ID of trace. For forward traces, this ID is
            unique for each trace. For return traces, it
            matches ID of associated forward trace. A single
            forward trace can be associated with none, one
            or more than one return trace.
    """

    endpoint_info: "EndpointInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EndpointInfo",
    )
    steps: MutableSequence["Step"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Step",
    )
    forward_trace_id: int = proto.Field(
        proto.INT32,
        number=4,
    )


class Step(proto.Message):
    r"""A simulated forwarding path is composed of multiple steps.
    Each step has a well-defined state and an associated
    configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            A description of the step. Usually this is a
            summary of the state.
        state (google.cloud.network_management_v1.types.Step.State):
            Each step is in one of the pre-defined
            states.
        causes_drop (bool):
            This is a step that leads to the final state
            Drop.
        project_id (str):
            Project ID that contains the configuration
            this step is validating.
        instance (google.cloud.network_management_v1.types.InstanceInfo):
            Display information of a Compute Engine
            instance.

            This field is a member of `oneof`_ ``step_info``.
        firewall (google.cloud.network_management_v1.types.FirewallInfo):
            Display information of a Compute Engine
            firewall rule.

            This field is a member of `oneof`_ ``step_info``.
        route (google.cloud.network_management_v1.types.RouteInfo):
            Display information of a Compute Engine
            route.

            This field is a member of `oneof`_ ``step_info``.
        endpoint (google.cloud.network_management_v1.types.EndpointInfo):
            Display information of the source and
            destination under analysis. The endpoint
            information in an intermediate state may differ
            with the initial input, as it might be modified
            by state like NAT, or Connection Proxy.

            This field is a member of `oneof`_ ``step_info``.
        google_service (google.cloud.network_management_v1.types.GoogleServiceInfo):
            Display information of a Google service

            This field is a member of `oneof`_ ``step_info``.
        forwarding_rule (google.cloud.network_management_v1.types.ForwardingRuleInfo):
            Display information of a Compute Engine
            forwarding rule.

            This field is a member of `oneof`_ ``step_info``.
        hybrid_subnet (google.cloud.network_management_v1.types.HybridSubnetInfo):
            Display information of a hybrid subnet.

            This field is a member of `oneof`_ ``step_info``.
        vpn_gateway (google.cloud.network_management_v1.types.VpnGatewayInfo):
            Display information of a Compute Engine VPN
            gateway.

            This field is a member of `oneof`_ ``step_info``.
        vpn_tunnel (google.cloud.network_management_v1.types.VpnTunnelInfo):
            Display information of a Compute Engine VPN
            tunnel.

            This field is a member of `oneof`_ ``step_info``.
        interconnect_attachment (google.cloud.network_management_v1.types.InterconnectAttachmentInfo):
            Display information of an interconnect
            attachment.

            This field is a member of `oneof`_ ``step_info``.
        vpc_connector (google.cloud.network_management_v1.types.VpcConnectorInfo):
            Display information of a VPC connector.

            This field is a member of `oneof`_ ``step_info``.
        direct_vpc_egress_connection (google.cloud.network_management_v1.types.DirectVpcEgressConnectionInfo):
            Display information of a serverless direct
            VPC egress connection.

            This field is a member of `oneof`_ ``step_info``.
        serverless_external_connection (google.cloud.network_management_v1.types.ServerlessExternalConnectionInfo):
            Display information of a serverless public
            (external) connection.

            This field is a member of `oneof`_ ``step_info``.
        deliver (google.cloud.network_management_v1.types.DeliverInfo):
            Display information of the final state
            "deliver" and reason.

            This field is a member of `oneof`_ ``step_info``.
        forward (google.cloud.network_management_v1.types.ForwardInfo):
            Display information of the final state
            "forward" and reason.

            This field is a member of `oneof`_ ``step_info``.
        abort (google.cloud.network_management_v1.types.AbortInfo):
            Display information of the final state
            "abort" and reason.

            This field is a member of `oneof`_ ``step_info``.
        drop (google.cloud.network_management_v1.types.DropInfo):
            Display information of the final state "drop"
            and reason.

            This field is a member of `oneof`_ ``step_info``.
        load_balancer (google.cloud.network_management_v1.types.LoadBalancerInfo):
            Display information of the load balancers. Deprecated in
            favor of the ``load_balancer_backend_info`` field, not used
            in new tests.

            This field is a member of `oneof`_ ``step_info``.
        network (google.cloud.network_management_v1.types.NetworkInfo):
            Display information of a Google Cloud
            network.

            This field is a member of `oneof`_ ``step_info``.
        gke_master (google.cloud.network_management_v1.types.GKEMasterInfo):
            Display information of a Google Kubernetes
            Engine cluster master.

            This field is a member of `oneof`_ ``step_info``.
        gke_pod (google.cloud.network_management_v1.types.GkePodInfo):
            Display information of a Google Kubernetes
            Engine Pod.

            This field is a member of `oneof`_ ``step_info``.
        ip_masquerading_skipped (google.cloud.network_management_v1.types.IpMasqueradingSkippedInfo):
            Display information of the reason why GKE Pod
            IP masquerading was skipped.

            This field is a member of `oneof`_ ``step_info``.
        gke_network_policy (google.cloud.network_management_v1.types.GkeNetworkPolicyInfo):
            Display information of a GKE Network Policy.

            This field is a member of `oneof`_ ``step_info``.
        gke_network_policy_skipped (google.cloud.network_management_v1.types.GkeNetworkPolicySkippedInfo):
            Display information of the reason why GKE
            Network Policy evaluation was skipped.

            This field is a member of `oneof`_ ``step_info``.
        cloud_sql_instance (google.cloud.network_management_v1.types.CloudSQLInstanceInfo):
            Display information of a Cloud SQL instance.

            This field is a member of `oneof`_ ``step_info``.
        redis_instance (google.cloud.network_management_v1.types.RedisInstanceInfo):
            Display information of a Redis Instance.

            This field is a member of `oneof`_ ``step_info``.
        redis_cluster (google.cloud.network_management_v1.types.RedisClusterInfo):
            Display information of a Redis Cluster.

            This field is a member of `oneof`_ ``step_info``.
        cloud_function (google.cloud.network_management_v1.types.CloudFunctionInfo):
            Display information of a Cloud Function.

            This field is a member of `oneof`_ ``step_info``.
        app_engine_version (google.cloud.network_management_v1.types.AppEngineVersionInfo):
            Display information of an App Engine service
            version.

            This field is a member of `oneof`_ ``step_info``.
        cloud_run_revision (google.cloud.network_management_v1.types.CloudRunRevisionInfo):
            Display information of a Cloud Run revision.

            This field is a member of `oneof`_ ``step_info``.
        cloud_run_job (google.cloud.network_management_v1.types.CloudRunJobInfo):
            Display information of a Cloud Run job.

            This field is a member of `oneof`_ ``step_info``.
        nat (google.cloud.network_management_v1.types.NatInfo):
            Display information of a NAT.

            This field is a member of `oneof`_ ``step_info``.
        proxy_connection (google.cloud.network_management_v1.types.ProxyConnectionInfo):
            Display information of a ProxyConnection.

            This field is a member of `oneof`_ ``step_info``.
        load_balancer_backend_info (google.cloud.network_management_v1.types.LoadBalancerBackendInfo):
            Display information of a specific load
            balancer backend.

            This field is a member of `oneof`_ ``step_info``.
        storage_bucket (google.cloud.network_management_v1.types.StorageBucketInfo):
            Display information of a Storage Bucket. Used
            only for return traces.

            This field is a member of `oneof`_ ``step_info``.
        serverless_neg (google.cloud.network_management_v1.types.ServerlessNegInfo):
            Display information of a Serverless network
            endpoint group backend. Used only for return
            traces.

            This field is a member of `oneof`_ ``step_info``.
        ngfw_packet_inspection (google.cloud.network_management_v1.types.NgfwPacketInspectionInfo):
            Display information of a layer 7 packet
            inspection by the firewall.

            This field is a member of `oneof`_ ``step_info``.
        dms_private_connection (google.cloud.network_management_v1.types.PrivateConnectionInfo):
            Display information of a DMS Private
            Connection.

            This field is a member of `oneof`_ ``step_info``.
    """

    class State(proto.Enum):
        r"""Type of states that are defined in the network state machine.
        Each step in the packet trace is in a specific state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            START_FROM_INSTANCE (1):
                Initial state: packet originating from a
                Compute Engine instance. An InstanceInfo is
                populated with starting instance information.
            START_FROM_INTERNET (2):
                Initial state: packet originating from the
                internet. The endpoint information is populated.
            START_FROM_GOOGLE_SERVICE (27):
                Initial state: packet originating from a Google service. The
                google_service information is populated.
            START_FROM_PRIVATE_NETWORK (3):
                Initial state: packet originating from a VPC
                or on-premises network with internal source IP.
                If the source is a VPC network visible to the
                user, a NetworkInfo is populated with details of
                the network.
            START_FROM_GKE_MASTER (21):
                Initial state: packet originating from a
                Google Kubernetes Engine cluster master. A
                GKEMasterInfo is populated with starting
                instance information.
            START_FROM_CLOUD_SQL_INSTANCE (22):
                Initial state: packet originating from a
                Cloud SQL instance. A CloudSQLInstanceInfo is
                populated with starting instance information.
            START_FROM_GKE_POD (39):
                Initial state: packet originating from a
                Google Kubernetes Engine Pod. A GkePodInfo is
                populated with starting Pod information.
            START_FROM_REDIS_INSTANCE (32):
                Initial state: packet originating from a
                Redis instance. A RedisInstanceInfo is populated
                with starting instance information.
            START_FROM_REDIS_CLUSTER (33):
                Initial state: packet originating from a
                Redis Cluster. A RedisClusterInfo is populated
                with starting Cluster information.
            START_FROM_CLOUD_FUNCTION (23):
                Initial state: packet originating from a
                Cloud Function. A CloudFunctionInfo is populated
                with starting function information.
            START_FROM_APP_ENGINE_VERSION (25):
                Initial state: packet originating from an App
                Engine service version. An AppEngineVersionInfo
                is populated with starting version information.
            START_FROM_CLOUD_RUN_REVISION (26):
                Initial state: packet originating from a
                Cloud Run revision. A CloudRunRevisionInfo is
                populated with starting revision information.
            START_FROM_CLOUD_RUN_JOB (50):
                Initial state: packet originating from a
                Cloud Run Job. A CloudRunJobInfo is populated
                with starting Job information.
            START_FROM_STORAGE_BUCKET (29):
                Initial state: packet originating from a Storage Bucket.
                Used only for return traces. The storage_bucket information
                is populated.
            START_FROM_PSC_PUBLISHED_SERVICE (30):
                Initial state: packet originating from a
                published service that uses Private Service
                Connect. Used only for return traces.
            START_FROM_SERVERLESS_NEG (31):
                Initial state: packet originating from a serverless network
                endpoint group backend. Used only for return traces. The
                serverless_neg information is populated.
            START_FROM_DMS_PRIVATE_CONNECTION (48):
                Initial state: packet originating from a DMS
                Private Connection.
            APPLY_INGRESS_FIREWALL_RULE (4):
                Config checking state: verify ingress
                firewall rule.
            APPLY_EGRESS_FIREWALL_RULE (5):
                Config checking state: verify egress firewall
                rule.
            APPLY_ROUTE (6):
                Config checking state: verify route.
            APPLY_FORWARDING_RULE (7):
                Config checking state: match forwarding rule.
            ANALYZE_LOAD_BALANCER_BACKEND (28):
                Config checking state: verify load balancer
                backend configuration.
            SPOOFING_APPROVED (8):
                Config checking state: packet sent or
                received under foreign IP address and allowed.
            ARRIVE_AT_INSTANCE (9):
                Forwarding state: arriving at a Compute
                Engine instance.
            ARRIVE_AT_INTERNAL_LOAD_BALANCER (10):
                Forwarding state: arriving at a Compute
                Engine internal load balancer.
            ARRIVE_AT_EXTERNAL_LOAD_BALANCER (11):
                Forwarding state: arriving at a Compute
                Engine external load balancer.
            ARRIVE_AT_HYBRID_SUBNET (38):
                Forwarding state: arriving at a hybrid
                subnet. Appropriate routing configuration will
                be determined here.
            ARRIVE_AT_VPN_GATEWAY (12):
                Forwarding state: arriving at a Cloud VPN
                gateway.
            ARRIVE_AT_VPN_TUNNEL (13):
                Forwarding state: arriving at a Cloud VPN
                tunnel.
            ARRIVE_AT_INTERCONNECT_ATTACHMENT (37):
                Forwarding state: arriving at an interconnect
                attachment.
            ARRIVE_AT_VPC_CONNECTOR (24):
                Forwarding state: arriving at a VPC
                connector.
            ARRIVE_AT_GKE_POD (44):
                Forwarding state: arriving at a GKE Pod.
            DIRECT_VPC_EGRESS_CONNECTION (35):
                Forwarding state: for packets originating
                from a serverless endpoint forwarded through
                Direct VPC egress.
            SERVERLESS_EXTERNAL_CONNECTION (36):
                Forwarding state: for packets originating
                from a serverless endpoint forwarded through
                public (external) connectivity.
            NGFW_PACKET_INSPECTION (47):
                Forwarding state: Layer 7 packet inspection
                by the firewall endpoint based on the configured
                security profile group.
            NAT (14):
                Transition state: packet header translated. The ``nat``
                field is populated with the translation information.
            SKIP_GKE_POD_IP_MASQUERADING (40):
                Transition state: GKE Pod IP masquerading is skipped. The
                ``ip_masquerading_skipped`` field is populated with the
                reason.
            SKIP_GKE_INGRESS_NETWORK_POLICY (41):
                Transition state: GKE Ingress Network Policy is skipped. The
                ``gke_network_policy_skipped`` field is populated with the
                reason.
            SKIP_GKE_EGRESS_NETWORK_POLICY (42):
                Transition state: GKE Egress Network Policy is skipped. The
                ``gke_network_policy_skipped`` field is populated with the
                reason.
            APPLY_INGRESS_GKE_NETWORK_POLICY (45):
                Config checking state: verify ingress GKE
                network policy.
            APPLY_EGRESS_GKE_NETWORK_POLICY (46):
                Config checking state: verify egress GKE
                network policy.
            PROXY_CONNECTION (15):
                Transition state: original connection is
                terminated and a new proxied connection is
                initiated.
            DELIVER (16):
                Final state: packet could be delivered.
            DROP (17):
                Final state: packet could be dropped.
            FORWARD (18):
                Final state: packet could be forwarded to a
                network with an unknown configuration.
            ABORT (19):
                Final state: analysis is aborted.
            VIEWER_PERMISSION_MISSING (20):
                Special state: viewer of the test result does
                not have permission to see the configuration in
                this step.
        """

        STATE_UNSPECIFIED = 0
        START_FROM_INSTANCE = 1
        START_FROM_INTERNET = 2
        START_FROM_GOOGLE_SERVICE = 27
        START_FROM_PRIVATE_NETWORK = 3
        START_FROM_GKE_MASTER = 21
        START_FROM_CLOUD_SQL_INSTANCE = 22
        START_FROM_GKE_POD = 39
        START_FROM_REDIS_INSTANCE = 32
        START_FROM_REDIS_CLUSTER = 33
        START_FROM_CLOUD_FUNCTION = 23
        START_FROM_APP_ENGINE_VERSION = 25
        START_FROM_CLOUD_RUN_REVISION = 26
        START_FROM_CLOUD_RUN_JOB = 50
        START_FROM_STORAGE_BUCKET = 29
        START_FROM_PSC_PUBLISHED_SERVICE = 30
        START_FROM_SERVERLESS_NEG = 31
        START_FROM_DMS_PRIVATE_CONNECTION = 48
        APPLY_INGRESS_FIREWALL_RULE = 4
        APPLY_EGRESS_FIREWALL_RULE = 5
        APPLY_ROUTE = 6
        APPLY_FORWARDING_RULE = 7
        ANALYZE_LOAD_BALANCER_BACKEND = 28
        SPOOFING_APPROVED = 8
        ARRIVE_AT_INSTANCE = 9
        ARRIVE_AT_INTERNAL_LOAD_BALANCER = 10
        ARRIVE_AT_EXTERNAL_LOAD_BALANCER = 11
        ARRIVE_AT_HYBRID_SUBNET = 38
        ARRIVE_AT_VPN_GATEWAY = 12
        ARRIVE_AT_VPN_TUNNEL = 13
        ARRIVE_AT_INTERCONNECT_ATTACHMENT = 37
        ARRIVE_AT_VPC_CONNECTOR = 24
        ARRIVE_AT_GKE_POD = 44
        DIRECT_VPC_EGRESS_CONNECTION = 35
        SERVERLESS_EXTERNAL_CONNECTION = 36
        NGFW_PACKET_INSPECTION = 47
        NAT = 14
        SKIP_GKE_POD_IP_MASQUERADING = 40
        SKIP_GKE_INGRESS_NETWORK_POLICY = 41
        SKIP_GKE_EGRESS_NETWORK_POLICY = 42
        APPLY_INGRESS_GKE_NETWORK_POLICY = 45
        APPLY_EGRESS_GKE_NETWORK_POLICY = 46
        PROXY_CONNECTION = 15
        DELIVER = 16
        DROP = 17
        FORWARD = 18
        ABORT = 19
        VIEWER_PERMISSION_MISSING = 20

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    causes_drop: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    instance: "InstanceInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="step_info",
        message="InstanceInfo",
    )
    firewall: "FirewallInfo" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="step_info",
        message="FirewallInfo",
    )
    route: "RouteInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="step_info",
        message="RouteInfo",
    )
    endpoint: "EndpointInfo" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="step_info",
        message="EndpointInfo",
    )
    google_service: "GoogleServiceInfo" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="step_info",
        message="GoogleServiceInfo",
    )
    forwarding_rule: "ForwardingRuleInfo" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="step_info",
        message="ForwardingRuleInfo",
    )
    hybrid_subnet: "HybridSubnetInfo" = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="step_info",
        message="HybridSubnetInfo",
    )
    vpn_gateway: "VpnGatewayInfo" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="step_info",
        message="VpnGatewayInfo",
    )
    vpn_tunnel: "VpnTunnelInfo" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="step_info",
        message="VpnTunnelInfo",
    )
    interconnect_attachment: "InterconnectAttachmentInfo" = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="step_info",
        message="InterconnectAttachmentInfo",
    )
    vpc_connector: "VpcConnectorInfo" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="step_info",
        message="VpcConnectorInfo",
    )
    direct_vpc_egress_connection: "DirectVpcEgressConnectionInfo" = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="step_info",
        message="DirectVpcEgressConnectionInfo",
    )
    serverless_external_connection: "ServerlessExternalConnectionInfo" = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="step_info",
        message="ServerlessExternalConnectionInfo",
    )
    deliver: "DeliverInfo" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="step_info",
        message="DeliverInfo",
    )
    forward: "ForwardInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="step_info",
        message="ForwardInfo",
    )
    abort: "AbortInfo" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="step_info",
        message="AbortInfo",
    )
    drop: "DropInfo" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="step_info",
        message="DropInfo",
    )
    load_balancer: "LoadBalancerInfo" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="step_info",
        message="LoadBalancerInfo",
    )
    network: "NetworkInfo" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="step_info",
        message="NetworkInfo",
    )
    gke_master: "GKEMasterInfo" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="step_info",
        message="GKEMasterInfo",
    )
    gke_pod: "GkePodInfo" = proto.Field(
        proto.MESSAGE,
        number=37,
        oneof="step_info",
        message="GkePodInfo",
    )
    ip_masquerading_skipped: "IpMasqueradingSkippedInfo" = proto.Field(
        proto.MESSAGE,
        number=38,
        oneof="step_info",
        message="IpMasqueradingSkippedInfo",
    )
    gke_network_policy: "GkeNetworkPolicyInfo" = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="step_info",
        message="GkeNetworkPolicyInfo",
    )
    gke_network_policy_skipped: "GkeNetworkPolicySkippedInfo" = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="step_info",
        message="GkeNetworkPolicySkippedInfo",
    )
    cloud_sql_instance: "CloudSQLInstanceInfo" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="step_info",
        message="CloudSQLInstanceInfo",
    )
    redis_instance: "RedisInstanceInfo" = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="step_info",
        message="RedisInstanceInfo",
    )
    redis_cluster: "RedisClusterInfo" = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="step_info",
        message="RedisClusterInfo",
    )
    cloud_function: "CloudFunctionInfo" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="step_info",
        message="CloudFunctionInfo",
    )
    app_engine_version: "AppEngineVersionInfo" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="step_info",
        message="AppEngineVersionInfo",
    )
    cloud_run_revision: "CloudRunRevisionInfo" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="step_info",
        message="CloudRunRevisionInfo",
    )
    cloud_run_job: "CloudRunJobInfo" = proto.Field(
        proto.MESSAGE,
        number=45,
        oneof="step_info",
        message="CloudRunJobInfo",
    )
    nat: "NatInfo" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="step_info",
        message="NatInfo",
    )
    proxy_connection: "ProxyConnectionInfo" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="step_info",
        message="ProxyConnectionInfo",
    )
    load_balancer_backend_info: "LoadBalancerBackendInfo" = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="step_info",
        message="LoadBalancerBackendInfo",
    )
    storage_bucket: "StorageBucketInfo" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="step_info",
        message="StorageBucketInfo",
    )
    serverless_neg: "ServerlessNegInfo" = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="step_info",
        message="ServerlessNegInfo",
    )
    ngfw_packet_inspection: "NgfwPacketInspectionInfo" = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="step_info",
        message="NgfwPacketInspectionInfo",
    )
    dms_private_connection: "PrivateConnectionInfo" = proto.Field(
        proto.MESSAGE,
        number=43,
        oneof="step_info",
        message="PrivateConnectionInfo",
    )


class InstanceInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    instance.

    Attributes:
        display_name (str):
            Name of a Compute Engine instance.
        uri (str):
            URI of a Compute Engine instance.
        interface (str):
            Name of the network interface of a Compute
            Engine instance.
        network_uri (str):
            URI of a Compute Engine network.
        internal_ip (str):
            Internal IP address of the network interface.
        external_ip (str):
            External IP address of the network interface.
        network_tags (MutableSequence[str]):
            Network tags configured on the instance.
        service_account (str):
            Service account authorized for the instance.
        psc_network_attachment_uri (str):
            URI of the PSC network attachment the NIC is
            attached to (if relevant).
        running (bool):
            Indicates whether the Compute Engine instance is running.
            Deprecated: use the ``status`` field instead.
        status (google.cloud.network_management_v1.types.InstanceInfo.Status):
            The status of the instance.
    """

    class Status(proto.Enum):
        r"""The status of the instance. We treat all states other than
        "RUNNING" as not running.

        Values:
            STATUS_UNSPECIFIED (0):
                Default unspecified value.
            RUNNING (1):
                The instance is running.
            NOT_RUNNING (2):
                The instance has any status other than
                "RUNNING".
        """

        STATUS_UNSPECIFIED = 0
        RUNNING = 1
        NOT_RUNNING = 2

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    interface: str = proto.Field(
        proto.STRING,
        number=3,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    internal_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    external_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=8,
    )
    psc_network_attachment_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    running: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=11,
        enum=Status,
    )


class NetworkInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    network.

    Attributes:
        display_name (str):
            Name of a Compute Engine network.
        uri (str):
            URI of a Compute Engine network.
        matched_subnet_uri (str):
            URI of the subnet matching the source IP
            address of the test.
        matched_ip_range (str):
            The IP range of the subnet matching the
            source IP address of the test.
        region (str):
            The region of the subnet matching the source
            IP address of the test.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    matched_subnet_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    matched_ip_range: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region: str = proto.Field(
        proto.STRING,
        number=6,
    )


class FirewallInfo(proto.Message):
    r"""For display only. Metadata associated with a VPC firewall
    rule, an implied VPC firewall rule, or a firewall policy rule.

    Attributes:
        display_name (str):
            The display name of the firewall rule. This
            field might be empty for firewall policy rules.
        uri (str):
            The URI of the firewall rule. This field is
            not applicable to implied VPC firewall rules.
        direction (str):
            Possible values: INGRESS, EGRESS
        action (str):
            Possible values: ALLOW, DENY, APPLY_SECURITY_PROFILE_GROUP
        priority (int):
            The priority of the firewall rule.
        network_uri (str):
            The URI of the VPC network that the firewall
            rule is associated with. This field is not
            applicable to hierarchical firewall policy
            rules.
        target_tags (MutableSequence[str]):
            The target tags defined by the VPC firewall
            rule. This field is not applicable to firewall
            policy rules.
        target_service_accounts (MutableSequence[str]):
            The target service accounts specified by the
            firewall rule.
        policy (str):
            The name of the firewall policy that this
            rule is associated with. This field is not
            applicable to VPC firewall rules and implied VPC
            firewall rules.
        policy_uri (str):
            The URI of the firewall policy that this rule
            is associated with. This field is not applicable
            to VPC firewall rules and implied VPC firewall
            rules.
        firewall_rule_type (google.cloud.network_management_v1.types.FirewallInfo.FirewallRuleType):
            The firewall rule's type.
        policy_priority (int):
            The priority of the firewall policy that this
            rule is associated with. This field is not
            applicable to VPC firewall rules and implied VPC
            firewall rules.
        target_type (google.cloud.network_management_v1.types.FirewallInfo.TargetType):
            Target type of the firewall rule.
    """

    class FirewallRuleType(proto.Enum):
        r"""The firewall rule's type.

        Values:
            FIREWALL_RULE_TYPE_UNSPECIFIED (0):
                Unspecified type.
            HIERARCHICAL_FIREWALL_POLICY_RULE (1):
                Hierarchical firewall policy rule. For details, see
                `Hierarchical firewall policies
                overview <https://cloud.google.com/vpc/docs/firewall-policies>`__.
            VPC_FIREWALL_RULE (2):
                VPC firewall rule. For details, see `VPC firewall rules
                overview <https://cloud.google.com/vpc/docs/firewalls>`__.
            IMPLIED_VPC_FIREWALL_RULE (3):
                Implied VPC firewall rule. For details, see `Implied
                rules <https://cloud.google.com/vpc/docs/firewalls#default_firewall_rules>`__.
            SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE (4):
                Implicit firewall rules that are managed by serverless VPC
                access to allow ingress access. They are not visible in the
                Google Cloud console. For details, see `VPC connector's
                implicit
                rules <https://cloud.google.com/functions/docs/networking/connecting-vpc#restrict-access>`__.
            NETWORK_FIREWALL_POLICY_RULE (5):
                User-defined global network firewall policy rule. For
                details, see `Network firewall
                policies <https://cloud.google.com/vpc/docs/network-firewall-policies>`__.
            NETWORK_REGIONAL_FIREWALL_POLICY_RULE (6):
                User-defined regional network firewall policy rule. For
                details, see `Regional network firewall
                policies <https://cloud.google.com/firewall/docs/regional-firewall-policies>`__.
            SYSTEM_NETWORK_FIREWALL_POLICY_RULE (7):
                System-defined global network firewall policy
                rule.
            SYSTEM_REGIONAL_NETWORK_FIREWALL_POLICY_RULE (8):
                System-defined regional network firewall
                policy rule.
            UNSUPPORTED_FIREWALL_POLICY_RULE (100):
                Firewall policy rule containing attributes not yet supported
                in Connectivity tests. Firewall analysis is skipped if such
                a rule can potentially be matched. Please see the `list of
                unsupported
                configurations <https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#unsupported-configs>`__.
            TRACKING_STATE (101):
                Tracking state for response traffic created when request
                traffic goes through allow firewall rule. For details, see
                `firewall rules
                specifications <https://cloud.google.com/firewall/docs/firewalls#specifications>`__
            ANALYSIS_SKIPPED (102):
                Firewall analysis was skipped due to
                executing Connectivity Test in the
                BypassFirewallChecks mode
        """

        FIREWALL_RULE_TYPE_UNSPECIFIED = 0
        HIERARCHICAL_FIREWALL_POLICY_RULE = 1
        VPC_FIREWALL_RULE = 2
        IMPLIED_VPC_FIREWALL_RULE = 3
        SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE = 4
        NETWORK_FIREWALL_POLICY_RULE = 5
        NETWORK_REGIONAL_FIREWALL_POLICY_RULE = 6
        SYSTEM_NETWORK_FIREWALL_POLICY_RULE = 7
        SYSTEM_REGIONAL_NETWORK_FIREWALL_POLICY_RULE = 8
        UNSUPPORTED_FIREWALL_POLICY_RULE = 100
        TRACKING_STATE = 101
        ANALYSIS_SKIPPED = 102

    class TargetType(proto.Enum):
        r"""Target type of the firewall rule.

        Values:
            TARGET_TYPE_UNSPECIFIED (0):
                Target type is not specified. In this case we
                treat the rule as applying to INSTANCES target
                type.
            INSTANCES (1):
                Firewall rule applies to instances.
            INTERNAL_MANAGED_LB (2):
                Firewall rule applies to internal managed
                load balancers.
        """

        TARGET_TYPE_UNSPECIFIED = 0
        INSTANCES = 1
        INTERNAL_MANAGED_LB = 2

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    direction: str = proto.Field(
        proto.STRING,
        number=3,
    )
    action: str = proto.Field(
        proto.STRING,
        number=4,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=5,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    target_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    target_service_accounts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    policy: str = proto.Field(
        proto.STRING,
        number=9,
    )
    policy_uri: str = proto.Field(
        proto.STRING,
        number=11,
    )
    firewall_rule_type: FirewallRuleType = proto.Field(
        proto.ENUM,
        number=10,
        enum=FirewallRuleType,
    )
    policy_priority: int = proto.Field(
        proto.INT32,
        number=12,
    )
    target_type: TargetType = proto.Field(
        proto.ENUM,
        number=13,
        enum=TargetType,
    )


class RouteInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    route.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        route_type (google.cloud.network_management_v1.types.RouteInfo.RouteType):
            Type of route.
        next_hop_type (google.cloud.network_management_v1.types.RouteInfo.NextHopType):
            Type of next hop.
        route_scope (google.cloud.network_management_v1.types.RouteInfo.RouteScope):
            Indicates where route is applicable. Deprecated, routes with
            NCC_HUB scope are not included in the trace in new tests.
        display_name (str):
            Name of a route.
        uri (str):
            URI of a route. SUBNET, STATIC, PEERING_SUBNET (only for
            peering network) and POLICY_BASED routes only.
        region (str):
            Region of the route. DYNAMIC, PEERING_DYNAMIC, POLICY_BASED
            and ADVERTISED routes only. If set for POLICY_BASED route,
            this is a region of VLAN attachments for Cloud Interconnect
            the route applies to. If set to "all" for POLICY_BASED
            route, the route applies to VLAN attachments of Cloud
            Interconnect in all regions.
        dest_ip_range (str):
            Destination IP range of the route.
        next_hop (str):
            String type of the next hop of the route (for example, "VPN
            tunnel"). Deprecated in favor of the next_hop_type and
            next_hop_uri fields, not used in new tests.
        network_uri (str):
            URI of a VPC network where route is located.
        priority (int):
            Priority of the route.
        instance_tags (MutableSequence[str]):
            Instance tags of the route.
        src_ip_range (str):
            Source IP address range of the route. POLICY_BASED routes
            only.
        dest_port_ranges (MutableSequence[str]):
            Destination port ranges of the route. POLICY_BASED routes
            only.
        src_port_ranges (MutableSequence[str]):
            Source port ranges of the route. POLICY_BASED routes only.
        protocols (MutableSequence[str]):
            Protocols of the route. POLICY_BASED routes only.
        ncc_hub_uri (str):
            URI of the NCC Hub the route is advertised by.
            PEERING_SUBNET and PEERING_DYNAMIC routes that are
            advertised by NCC Hub only.

            This field is a member of `oneof`_ ``_ncc_hub_uri``.
        ncc_spoke_uri (str):
            URI of the destination NCC Spoke. PEERING_SUBNET and
            PEERING_DYNAMIC routes that are advertised by NCC Hub only.

            This field is a member of `oneof`_ ``_ncc_spoke_uri``.
        advertised_route_source_router_uri (str):
            For ADVERTISED dynamic routes, the URI of the
            Cloud Router that advertised the corresponding
            IP prefix.

            This field is a member of `oneof`_ ``_advertised_route_source_router_uri``.
        advertised_route_next_hop_uri (str):
            For ADVERTISED routes, the URI of their next hop, i.e. the
            URI of the hybrid endpoint (VPN tunnel, Interconnect
            attachment, NCC router appliance) the advertised prefix is
            advertised through, or URI of the source peered network.
            Deprecated in favor of the next_hop_uri field, not used in
            new tests.

            This field is a member of `oneof`_ ``_advertised_route_next_hop_uri``.
        next_hop_uri (str):
            URI of the next hop resource.
        next_hop_network_uri (str):
            URI of a VPC network where the next hop
            resource is located.
        originating_route_uri (str):
            For PEERING_SUBNET and PEERING_STATIC routes, the URI of the
            originating SUBNET/STATIC route.
        originating_route_display_name (str):
            For PEERING_SUBNET, PEERING_STATIC and PEERING_DYNAMIC
            routes, the name of the originating SUBNET/STATIC/DYNAMIC
            route.
        ncc_hub_route_uri (str):
            For PEERING_SUBNET and PEERING_DYNAMIC routes that are
            advertised by NCC Hub, the URI of the corresponding route in
            NCC Hub's routing table.
    """

    class RouteType(proto.Enum):
        r"""Type of route:

        Values:
            ROUTE_TYPE_UNSPECIFIED (0):
                Unspecified type. Default value.
            SUBNET (1):
                Route is a subnet route automatically created
                by the system.
            STATIC (2):
                Static route created by the user, including
                the default route to the internet.
            DYNAMIC (3):
                Dynamic route exchanged between BGP peers.
            PEERING_SUBNET (4):
                A subnet route received from peering network
                or NCC Hub.
            PEERING_STATIC (5):
                A static route received from peering network.
            PEERING_DYNAMIC (6):
                A dynamic route received from peering network
                or NCC Hub.
            POLICY_BASED (7):
                Policy based route.
            ADVERTISED (101):
                Advertised route. Synthetic route which is
                used to transition from the
                StartFromPrivateNetwork state in Connectivity
                tests.
        """

        ROUTE_TYPE_UNSPECIFIED = 0
        SUBNET = 1
        STATIC = 2
        DYNAMIC = 3
        PEERING_SUBNET = 4
        PEERING_STATIC = 5
        PEERING_DYNAMIC = 6
        POLICY_BASED = 7
        ADVERTISED = 101

    class NextHopType(proto.Enum):
        r"""Type of next hop:

        Values:
            NEXT_HOP_TYPE_UNSPECIFIED (0):
                Unspecified type. Default value.
            NEXT_HOP_IP (1):
                Next hop is an IP address.
            NEXT_HOP_INSTANCE (2):
                Next hop is a Compute Engine instance.
            NEXT_HOP_NETWORK (3):
                Next hop is a VPC network gateway.
            NEXT_HOP_PEERING (4):
                Next hop is a peering VPC. This scenario only
                happens when the user doesn't have permissions
                to the project where the next hop resource is
                located.
            NEXT_HOP_INTERCONNECT (5):
                Next hop is an interconnect.
            NEXT_HOP_VPN_TUNNEL (6):
                Next hop is a VPN tunnel.
            NEXT_HOP_VPN_GATEWAY (7):
                Next hop is a VPN gateway. This scenario only
                happens when tracing connectivity from an
                on-premises network to Google Cloud through a
                VPN. The analysis simulates a packet departing
                from the on-premises network through a VPN
                tunnel and arriving at a Cloud VPN gateway.
            NEXT_HOP_INTERNET_GATEWAY (8):
                Next hop is an internet gateway.
            NEXT_HOP_BLACKHOLE (9):
                Next hop is blackhole; that is, the next hop
                either does not exist or is unusable.
            NEXT_HOP_ILB (10):
                Next hop is the forwarding rule of an
                Internal Load Balancer.
            NEXT_HOP_ROUTER_APPLIANCE (11):
                Next hop is a `router appliance
                instance <https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview>`__.
            NEXT_HOP_NCC_HUB (12):
                Next hop is an NCC hub. This scenario only
                happens when the user doesn't have permissions
                to the project where the next hop resource is
                located.
            SECURE_WEB_PROXY_GATEWAY (13):
                Next hop is Secure Web Proxy Gateway.
        """

        NEXT_HOP_TYPE_UNSPECIFIED = 0
        NEXT_HOP_IP = 1
        NEXT_HOP_INSTANCE = 2
        NEXT_HOP_NETWORK = 3
        NEXT_HOP_PEERING = 4
        NEXT_HOP_INTERCONNECT = 5
        NEXT_HOP_VPN_TUNNEL = 6
        NEXT_HOP_VPN_GATEWAY = 7
        NEXT_HOP_INTERNET_GATEWAY = 8
        NEXT_HOP_BLACKHOLE = 9
        NEXT_HOP_ILB = 10
        NEXT_HOP_ROUTER_APPLIANCE = 11
        NEXT_HOP_NCC_HUB = 12
        SECURE_WEB_PROXY_GATEWAY = 13

    class RouteScope(proto.Enum):
        r"""Indicates where routes are applicable.

        Values:
            ROUTE_SCOPE_UNSPECIFIED (0):
                Unspecified scope. Default value.
            NETWORK (1):
                Route is applicable to packets in Network.
            NCC_HUB (2):
                Route is applicable to packets using NCC
                Hub's routing table.
        """

        ROUTE_SCOPE_UNSPECIFIED = 0
        NETWORK = 1
        NCC_HUB = 2

    route_type: RouteType = proto.Field(
        proto.ENUM,
        number=8,
        enum=RouteType,
    )
    next_hop_type: NextHopType = proto.Field(
        proto.ENUM,
        number=9,
        enum=NextHopType,
    )
    route_scope: RouteScope = proto.Field(
        proto.ENUM,
        number=14,
        enum=RouteScope,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=19,
    )
    dest_ip_range: str = proto.Field(
        proto.STRING,
        number=3,
    )
    next_hop: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=6,
    )
    instance_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    src_ip_range: str = proto.Field(
        proto.STRING,
        number=10,
    )
    dest_port_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    src_port_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    protocols: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    ncc_hub_uri: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    ncc_spoke_uri: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    advertised_route_source_router_uri: str = proto.Field(
        proto.STRING,
        number=17,
        optional=True,
    )
    advertised_route_next_hop_uri: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    next_hop_uri: str = proto.Field(
        proto.STRING,
        number=20,
    )
    next_hop_network_uri: str = proto.Field(
        proto.STRING,
        number=21,
    )
    originating_route_uri: str = proto.Field(
        proto.STRING,
        number=22,
    )
    originating_route_display_name: str = proto.Field(
        proto.STRING,
        number=23,
    )
    ncc_hub_route_uri: str = proto.Field(
        proto.STRING,
        number=24,
    )


class GoogleServiceInfo(proto.Message):
    r"""For display only. Details of a Google Service sending packets to a
    VPC network. Although the source IP might be a publicly routable
    address, some Google Services use special routes within Google
    production infrastructure to reach Compute Engine Instances.
    https://cloud.google.com/vpc/docs/routes#special_return_paths

    Attributes:
        source_ip (str):
            Source IP address.
        google_service_type (google.cloud.network_management_v1.types.GoogleServiceInfo.GoogleServiceType):
            Recognized type of a Google Service.
    """

    class GoogleServiceType(proto.Enum):
        r"""Recognized type of a Google Service.

        Values:
            GOOGLE_SERVICE_TYPE_UNSPECIFIED (0):
                Unspecified Google Service.
            IAP (1):
                Identity aware proxy.
                https://cloud.google.com/iap/docs/using-tcp-forwarding
            GFE_PROXY_OR_HEALTH_CHECK_PROBER (2):
                One of two services sharing IP ranges:

                - Load Balancer proxy
                - Centralized Health Check prober
                  https://cloud.google.com/load-balancing/docs/firewall-rules
            CLOUD_DNS (3):
                Connectivity from Cloud DNS to forwarding
                targets or alternate name servers that use
                private routing.
                https://cloud.google.com/dns/docs/zones/forwarding-zones#firewall-rules
                https://cloud.google.com/dns/docs/policies#firewall-rules
            GOOGLE_API (4):
                private.googleapis.com and
                restricted.googleapis.com
            GOOGLE_API_PSC (5):
                Google API via Private Service Connect.
                https://cloud.google.com/vpc/docs/configure-private-service-connect-apis
            GOOGLE_API_VPC_SC (6):
                Google API via VPC Service Controls.
                https://cloud.google.com/vpc/docs/configure-private-service-connect-apis
            SERVERLESS_VPC_ACCESS (7):
                Google API via Serverless VPC Access.
                https://cloud.google.com/vpc/docs/serverless-vpc-access
        """

        GOOGLE_SERVICE_TYPE_UNSPECIFIED = 0
        IAP = 1
        GFE_PROXY_OR_HEALTH_CHECK_PROBER = 2
        CLOUD_DNS = 3
        GOOGLE_API = 4
        GOOGLE_API_PSC = 5
        GOOGLE_API_VPC_SC = 6
        SERVERLESS_VPC_ACCESS = 7

    source_ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    google_service_type: GoogleServiceType = proto.Field(
        proto.ENUM,
        number=2,
        enum=GoogleServiceType,
    )


class ForwardingRuleInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    forwarding rule.

    Attributes:
        display_name (str):
            Name of the forwarding rule.
        uri (str):
            URI of the forwarding rule.
        matched_protocol (str):
            Protocol defined in the forwarding rule that
            matches the packet.
        matched_port_range (str):
            Port range defined in the forwarding rule
            that matches the packet.
        vip (str):
            VIP of the forwarding rule.
        target (str):
            Target type of the forwarding rule.
        network_uri (str):
            Network URI.
        region (str):
            Region of the forwarding rule. Set only for
            regional forwarding rules.
        load_balancer_name (str):
            Name of the load balancer the forwarding rule
            belongs to. Empty for forwarding rules not
            related to load balancers (like PSC forwarding
            rules).
        psc_service_attachment_uri (str):
            URI of the PSC service attachment this
            forwarding rule targets (if applicable).
        psc_google_api_target (str):
            PSC Google API target this forwarding rule
            targets (if applicable).
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    matched_protocol: str = proto.Field(
        proto.STRING,
        number=3,
    )
    matched_port_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    vip: str = proto.Field(
        proto.STRING,
        number=4,
    )
    target: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    region: str = proto.Field(
        proto.STRING,
        number=8,
    )
    load_balancer_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    psc_service_attachment_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    psc_google_api_target: str = proto.Field(
        proto.STRING,
        number=11,
    )


class LoadBalancerInfo(proto.Message):
    r"""For display only. Metadata associated with a load balancer.

    Attributes:
        load_balancer_type (google.cloud.network_management_v1.types.LoadBalancerInfo.LoadBalancerType):
            Type of the load balancer.
        health_check_uri (str):
            URI of the health check for the load
            balancer. Deprecated and no longer populated as
            different load balancer backends might have
            different health checks.
        backends (MutableSequence[google.cloud.network_management_v1.types.LoadBalancerBackend]):
            Information for the loadbalancer backends.
        backend_type (google.cloud.network_management_v1.types.LoadBalancerInfo.BackendType):
            Type of load balancer's backend
            configuration.
        backend_uri (str):
            Backend configuration URI.
    """

    class LoadBalancerType(proto.Enum):
        r"""The type definition for a load balancer:

        Values:
            LOAD_BALANCER_TYPE_UNSPECIFIED (0):
                Type is unspecified.
            INTERNAL_TCP_UDP (1):
                Internal TCP/UDP load balancer.
            NETWORK_TCP_UDP (2):
                Network TCP/UDP load balancer.
            HTTP_PROXY (3):
                HTTP(S) proxy load balancer.
            TCP_PROXY (4):
                TCP proxy load balancer.
            SSL_PROXY (5):
                SSL proxy load balancer.
        """

        LOAD_BALANCER_TYPE_UNSPECIFIED = 0
        INTERNAL_TCP_UDP = 1
        NETWORK_TCP_UDP = 2
        HTTP_PROXY = 3
        TCP_PROXY = 4
        SSL_PROXY = 5

    class BackendType(proto.Enum):
        r"""The type definition for a load balancer backend
        configuration:

        Values:
            BACKEND_TYPE_UNSPECIFIED (0):
                Type is unspecified.
            BACKEND_SERVICE (1):
                Backend Service as the load balancer's
                backend.
            TARGET_POOL (2):
                Target Pool as the load balancer's backend.
            TARGET_INSTANCE (3):
                Target Instance as the load balancer's
                backend.
        """

        BACKEND_TYPE_UNSPECIFIED = 0
        BACKEND_SERVICE = 1
        TARGET_POOL = 2
        TARGET_INSTANCE = 3

    load_balancer_type: LoadBalancerType = proto.Field(
        proto.ENUM,
        number=1,
        enum=LoadBalancerType,
    )
    health_check_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backends: MutableSequence["LoadBalancerBackend"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="LoadBalancerBackend",
    )
    backend_type: BackendType = proto.Field(
        proto.ENUM,
        number=4,
        enum=BackendType,
    )
    backend_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


class LoadBalancerBackend(proto.Message):
    r"""For display only. Metadata associated with a specific load
    balancer backend.

    Attributes:
        display_name (str):
            Name of a Compute Engine instance or network
            endpoint.
        uri (str):
            URI of a Compute Engine instance or network
            endpoint.
        health_check_firewall_state (google.cloud.network_management_v1.types.LoadBalancerBackend.HealthCheckFirewallState):
            State of the health check firewall
            configuration.
        health_check_allowing_firewall_rules (MutableSequence[str]):
            A list of firewall rule URIs allowing probes
            from health check IP ranges.
        health_check_blocking_firewall_rules (MutableSequence[str]):
            A list of firewall rule URIs blocking probes
            from health check IP ranges.
    """

    class HealthCheckFirewallState(proto.Enum):
        r"""State of a health check firewall configuration:

        Values:
            HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED (0):
                State is unspecified. Default state if not
                populated.
            CONFIGURED (1):
                There are configured firewall rules to allow
                health check probes to the backend.
            MISCONFIGURED (2):
                There are firewall rules configured to allow
                partial health check ranges or block all health
                check ranges. If a health check probe is sent
                from denied IP ranges, the health check to the
                backend will fail. Then, the backend will be
                marked unhealthy and will not receive traffic
                sent to the load balancer.
        """

        HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED = 0
        CONFIGURED = 1
        MISCONFIGURED = 2

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    health_check_firewall_state: HealthCheckFirewallState = proto.Field(
        proto.ENUM,
        number=3,
        enum=HealthCheckFirewallState,
    )
    health_check_allowing_firewall_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    health_check_blocking_firewall_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class HybridSubnetInfo(proto.Message):
    r"""For display only. Metadata associated with a hybrid subnet.

    Attributes:
        display_name (str):
            Name of a hybrid subnet.
        uri (str):
            URI of a hybrid subnet.
        region (str):
            Name of a Google Cloud region where the
            hybrid subnet is configured.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )


class VpnGatewayInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    VPN gateway.

    Attributes:
        display_name (str):
            Name of a VPN gateway.
        uri (str):
            URI of a VPN gateway.
        network_uri (str):
            URI of a Compute Engine network where the VPN
            gateway is configured.
        ip_address (str):
            IP address of the VPN gateway.
        vpn_tunnel_uri (str):
            A VPN tunnel that is associated with this VPN
            gateway. There may be multiple VPN tunnels
            configured on a VPN gateway, and only the one
            relevant to the test is displayed.
        region (str):
            Name of a Google Cloud region where this VPN
            gateway is configured.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    vpn_tunnel_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    region: str = proto.Field(
        proto.STRING,
        number=6,
    )


class VpnTunnelInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    VPN tunnel.

    Attributes:
        display_name (str):
            Name of a VPN tunnel.
        uri (str):
            URI of a VPN tunnel.
        source_gateway (str):
            URI of the VPN gateway at local end of the
            tunnel.
        remote_gateway (str):
            URI of a VPN gateway at remote end of the
            tunnel.
        remote_gateway_ip (str):
            Remote VPN gateway's IP address.
        source_gateway_ip (str):
            Local VPN gateway's IP address.
        network_uri (str):
            URI of a Compute Engine network where the VPN
            tunnel is configured.
        region (str):
            Name of a Google Cloud region where this VPN
            tunnel is configured.
        routing_type (google.cloud.network_management_v1.types.VpnTunnelInfo.RoutingType):
            Type of the routing policy.
    """

    class RoutingType(proto.Enum):
        r"""Types of VPN routing policy. For details, refer to `Networks and
        Tunnel
        routing <https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing/>`__.

        Values:
            ROUTING_TYPE_UNSPECIFIED (0):
                Unspecified type. Default value.
            ROUTE_BASED (1):
                Route based VPN.
            POLICY_BASED (2):
                Policy based routing.
            DYNAMIC (3):
                Dynamic (BGP) routing.
        """

        ROUTING_TYPE_UNSPECIFIED = 0
        ROUTE_BASED = 1
        POLICY_BASED = 2
        DYNAMIC = 3

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_gateway: str = proto.Field(
        proto.STRING,
        number=3,
    )
    remote_gateway: str = proto.Field(
        proto.STRING,
        number=4,
    )
    remote_gateway_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    source_gateway_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    region: str = proto.Field(
        proto.STRING,
        number=8,
    )
    routing_type: RoutingType = proto.Field(
        proto.ENUM,
        number=9,
        enum=RoutingType,
    )


class InterconnectAttachmentInfo(proto.Message):
    r"""For display only. Metadata associated with an Interconnect
    attachment.

    Attributes:
        display_name (str):
            Name of an Interconnect attachment.
        uri (str):
            URI of an Interconnect attachment.
        interconnect_uri (str):
            URI of the Interconnect where the
            Interconnect attachment is configured.
        region (str):
            Name of a Google Cloud region where the
            Interconnect attachment is configured.
        cloud_router_uri (str):
            URI of the Cloud Router to be used for
            dynamic routing.
        type_ (google.cloud.network_management_v1.types.InterconnectAttachmentInfo.Type):
            The type of interconnect attachment this is.
        l2_attachment_matched_ip_address (str):
            Appliance IP address that was matched for L2_DEDICATED
            attachments.
    """

    class Type(proto.Enum):
        r"""What type of interconnect attachment this is.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            DEDICATED (1):
                Attachment to a dedicated interconnect.
            PARTNER (2):
                Attachment to a partner interconnect, created
                by the customer.
            PARTNER_PROVIDER (3):
                Attachment to a partner interconnect, created
                by the partner.
            L2_DEDICATED (4):
                Attachment to a L2 interconnect, created by
                the customer.
        """

        TYPE_UNSPECIFIED = 0
        DEDICATED = 1
        PARTNER = 2
        PARTNER_PROVIDER = 3
        L2_DEDICATED = 4

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    interconnect_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cloud_router_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    l2_attachment_matched_ip_address: str = proto.Field(
        proto.STRING,
        number=7,
    )


class EndpointInfo(proto.Message):
    r"""For display only. The specification of the endpoints for the
    test. EndpointInfo is derived from source and destination
    Endpoint and validated by the backend data plane model.

    Attributes:
        source_ip (str):
            Source IP address.
        destination_ip (str):
            Destination IP address.
        protocol (str):
            IP protocol in string format, for example:
            "TCP", "UDP", "ICMP".
        source_port (int):
            Source port. Only valid when protocol is TCP
            or UDP.
        destination_port (int):
            Destination port. Only valid when protocol is
            TCP or UDP.
        source_network_uri (str):
            URI of the network where this packet
            originates from.
        destination_network_uri (str):
            URI of the network where this packet is sent
            to.
        source_agent_uri (str):
            URI of the source telemetry agent this packet
            originates from.
    """

    source_ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    protocol: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source_port: int = proto.Field(
        proto.INT32,
        number=4,
    )
    destination_port: int = proto.Field(
        proto.INT32,
        number=5,
    )
    source_network_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    destination_network_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    source_agent_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )


class DeliverInfo(proto.Message):
    r"""Details of the final state "deliver" and associated resource.

    Attributes:
        target (google.cloud.network_management_v1.types.DeliverInfo.Target):
            Target type where the packet is delivered to.
        resource_uri (str):
            URI of the resource that the packet is
            delivered to.
        ip_address (str):
            IP address of the target (if applicable).
        storage_bucket (str):
            Name of the Cloud Storage Bucket the packet
            is delivered to (if applicable).
        psc_google_api_target (str):
            PSC Google API target the packet is delivered
            to (if applicable).
        google_service_type (google.cloud.network_management_v1.types.DeliverInfo.GoogleServiceType):
            Recognized type of a Google Service the
            packet is delivered to (if applicable).
    """

    class Target(proto.Enum):
        r"""Deliver target types:

        Values:
            TARGET_UNSPECIFIED (0):
                Target not specified.
            INSTANCE (1):
                Target is a Compute Engine instance.
            INTERNET (2):
                Target is the internet.
            GOOGLE_API (3):
                Target is a Google API.
            GKE_MASTER (4):
                Target is a Google Kubernetes Engine cluster
                master.
            CLOUD_SQL_INSTANCE (5):
                Target is a Cloud SQL instance.
            PSC_PUBLISHED_SERVICE (6):
                Target is a published service that uses `Private Service
                Connect <https://cloud.google.com/vpc/docs/configure-private-service-connect-services>`__.
            PSC_GOOGLE_API (7):
                Target is Google APIs that use `Private Service
                Connect <https://cloud.google.com/vpc/docs/configure-private-service-connect-apis>`__.
            PSC_VPC_SC (8):
                Target is a VPC-SC that uses `Private Service
                Connect <https://cloud.google.com/vpc/docs/configure-private-service-connect-apis>`__.
            SERVERLESS_NEG (9):
                Target is a serverless network endpoint
                group.
            STORAGE_BUCKET (10):
                Target is a Cloud Storage bucket.
            PRIVATE_NETWORK (11):
                Target is a private network. Used only for
                return traces.
            CLOUD_FUNCTION (12):
                Target is a Cloud Function. Used only for
                return traces.
            APP_ENGINE_VERSION (13):
                Target is a App Engine service version. Used
                only for return traces.
            CLOUD_RUN_REVISION (14):
                Target is a Cloud Run revision. Used only for
                return traces.
            GOOGLE_MANAGED_SERVICE (15):
                Target is a Google-managed service. Used only
                for return traces.
            REDIS_INSTANCE (16):
                Target is a Redis Instance.
            REDIS_CLUSTER (17):
                Target is a Redis Cluster.
            GKE_POD (19):
                Target is a GKE Pod.
            CLOUD_RUN_JOB (20):
                Target is a Cloud Run Job. Used only for
                return traces.
            DMS_PRIVATE_CONNECTION (21):
                Target is a DMS Private Connection. Used only
                for return traces.
        """

        TARGET_UNSPECIFIED = 0
        INSTANCE = 1
        INTERNET = 2
        GOOGLE_API = 3
        GKE_MASTER = 4
        CLOUD_SQL_INSTANCE = 5
        PSC_PUBLISHED_SERVICE = 6
        PSC_GOOGLE_API = 7
        PSC_VPC_SC = 8
        SERVERLESS_NEG = 9
        STORAGE_BUCKET = 10
        PRIVATE_NETWORK = 11
        CLOUD_FUNCTION = 12
        APP_ENGINE_VERSION = 13
        CLOUD_RUN_REVISION = 14
        GOOGLE_MANAGED_SERVICE = 15
        REDIS_INSTANCE = 16
        REDIS_CLUSTER = 17
        GKE_POD = 19
        CLOUD_RUN_JOB = 20
        DMS_PRIVATE_CONNECTION = 21

    class GoogleServiceType(proto.Enum):
        r"""Recognized type of a Google Service.

        Values:
            GOOGLE_SERVICE_TYPE_UNSPECIFIED (0):
                Unspecified Google Service.
            IAP (1):
                Identity aware proxy.
                https://cloud.google.com/iap/docs/using-tcp-forwarding
            GFE_PROXY_OR_HEALTH_CHECK_PROBER (2):
                One of two services sharing IP ranges:

                - Load Balancer proxy
                - Centralized Health Check prober
                  https://cloud.google.com/load-balancing/docs/firewall-rules
            CLOUD_DNS (3):
                Connectivity from Cloud DNS to forwarding
                targets or alternate name servers that use
                private routing.
                https://cloud.google.com/dns/docs/zones/forwarding-zones#firewall-rules
                https://cloud.google.com/dns/docs/policies#firewall-rules
            PRIVATE_GOOGLE_ACCESS (4):
                private.googleapis.com and
                restricted.googleapis.com
            SERVERLESS_VPC_ACCESS (5):
                Google API via Private Service Connect.
                https://cloud.google.com/vpc/docs/configure-private-service-connect-apis
                Google API via Serverless VPC Access.
                https://cloud.google.com/vpc/docs/serverless-vpc-access
        """

        GOOGLE_SERVICE_TYPE_UNSPECIFIED = 0
        IAP = 1
        GFE_PROXY_OR_HEALTH_CHECK_PROBER = 2
        CLOUD_DNS = 3
        PRIVATE_GOOGLE_ACCESS = 4
        SERVERLESS_VPC_ACCESS = 5

    target: Target = proto.Field(
        proto.ENUM,
        number=1,
        enum=Target,
    )
    resource_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
    )
    storage_bucket: str = proto.Field(
        proto.STRING,
        number=4,
    )
    psc_google_api_target: str = proto.Field(
        proto.STRING,
        number=5,
    )
    google_service_type: GoogleServiceType = proto.Field(
        proto.ENUM,
        number=6,
        enum=GoogleServiceType,
    )


class ForwardInfo(proto.Message):
    r"""Details of the final state "forward" and associated resource.

    Attributes:
        target (google.cloud.network_management_v1.types.ForwardInfo.Target):
            Target type where this packet is forwarded
            to.
        resource_uri (str):
            URI of the resource that the packet is
            forwarded to.
        ip_address (str):
            IP address of the target (if applicable).
    """

    class Target(proto.Enum):
        r"""Forward target types.

        Values:
            TARGET_UNSPECIFIED (0):
                Target not specified.
            PEERING_VPC (1):
                Forwarded to a VPC peering network.
            VPN_GATEWAY (2):
                Forwarded to a Cloud VPN gateway.
            INTERCONNECT (3):
                Forwarded to a Cloud Interconnect connection.
            GKE_MASTER (4):
                Forwarded to a Google Kubernetes Engine
                Container cluster master.
            IMPORTED_CUSTOM_ROUTE_NEXT_HOP (5):
                Forwarded to the next hop of a custom route
                imported from a peering VPC.
            CLOUD_SQL_INSTANCE (6):
                Forwarded to a Cloud SQL instance.
            ANOTHER_PROJECT (7):
                Forwarded to a VPC network in another
                project.
            NCC_HUB (8):
                Forwarded to an NCC Hub.
            ROUTER_APPLIANCE (9):
                Forwarded to a router appliance.
            SECURE_WEB_PROXY_GATEWAY (10):
                Forwarded to a Secure Web Proxy Gateway.
        """

        TARGET_UNSPECIFIED = 0
        PEERING_VPC = 1
        VPN_GATEWAY = 2
        INTERCONNECT = 3
        GKE_MASTER = 4
        IMPORTED_CUSTOM_ROUTE_NEXT_HOP = 5
        CLOUD_SQL_INSTANCE = 6
        ANOTHER_PROJECT = 7
        NCC_HUB = 8
        ROUTER_APPLIANCE = 9
        SECURE_WEB_PROXY_GATEWAY = 10

    target: Target = proto.Field(
        proto.ENUM,
        number=1,
        enum=Target,
    )
    resource_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AbortInfo(proto.Message):
    r"""Details of the final state "abort" and associated resource.

    Attributes:
        cause (google.cloud.network_management_v1.types.AbortInfo.Cause):
            Causes that the analysis is aborted.
        resource_uri (str):
            URI of the resource that caused the abort.
        ip_address (str):
            IP address that caused the abort.
        projects_missing_permission (MutableSequence[str]):
            List of project IDs the user specified in the request but
            lacks access to. In this case, analysis is aborted with the
            PERMISSION_DENIED cause.
    """

    class Cause(proto.Enum):
        r"""Abort cause types:

        Values:
            CAUSE_UNSPECIFIED (0):
                Cause is unspecified.
            UNKNOWN_NETWORK (1):
                Aborted due to unknown network. Deprecated,
                not used in the new tests.
            UNKNOWN_PROJECT (3):
                Aborted because no project information can be
                derived from the test input. Deprecated, not
                used in the new tests.
            NO_EXTERNAL_IP (7):
                Aborted because traffic is sent from a public
                IP to an instance without an external IP.
                Deprecated, not used in the new tests.
            UNINTENDED_DESTINATION (8):
                Aborted because none of the traces matches
                destination information specified in the input
                test request. Deprecated, not used in the new
                tests.
            SOURCE_ENDPOINT_NOT_FOUND (11):
                Aborted because the source endpoint could not
                be found. Deprecated, not used in the new tests.
            MISMATCHED_SOURCE_NETWORK (12):
                Aborted because the source network does not
                match the source endpoint. Deprecated, not used
                in the new tests.
            DESTINATION_ENDPOINT_NOT_FOUND (13):
                Aborted because the destination endpoint
                could not be found. Deprecated, not used in the
                new tests.
            MISMATCHED_DESTINATION_NETWORK (14):
                Aborted because the destination network does
                not match the destination endpoint. Deprecated,
                not used in the new tests.
            UNKNOWN_IP (2):
                Aborted because no endpoint with the packet's
                destination IP address is found.
            GOOGLE_MANAGED_SERVICE_UNKNOWN_IP (32):
                Aborted because no endpoint with the packet's
                destination IP is found in the Google-managed
                project.
            SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK (23):
                Aborted because the source IP address doesn't
                belong to any of the subnets of the source VPC
                network.
            PERMISSION_DENIED (4):
                Aborted because user lacks permission to
                access all or part of the network configurations
                required to run the test.
            PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS (28):
                Aborted because user lacks permission to
                access Cloud NAT configs required to run the
                test.
            PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS (29):
                Aborted because user lacks permission to
                access Network endpoint group endpoint configs
                required to run the test.
            PERMISSION_DENIED_NO_CLOUD_ROUTER_CONFIGS (36):
                Aborted because user lacks permission to
                access Cloud Router configs required to run the
                test.
            NO_SOURCE_LOCATION (5):
                Aborted because no valid source or
                destination endpoint can be derived from the
                test request.
            NO_SOURCE_GCP_NETWORK_LOCATION (42):
                Aborted because the source IP address is not
                contained within the subnet ranges of the
                provided VPC network.
            NO_SOURCE_NON_GCP_NETWORK_LOCATION (43):
                Aborted because the source IP address is not
                contained within the destination ranges of the
                routes towards non-GCP networks in the provided
                VPC network.
            NO_SOURCE_INTERNET_LOCATION (44):
                Aborted because the source IP address can't
                be resolved as an Internet IP address.
            INVALID_ARGUMENT (6):
                Aborted because the source or destination
                endpoint specified in the request is invalid.
                Some examples:

                - The request might contain malformed resource
                  URI, project ID, or IP address.
                - The request might contain inconsistent
                  information (for example, the request might
                  include both the instance and the network, but
                  the instance might not have a NIC in that
                  network).
            TRACE_TOO_LONG (9):
                Aborted because the number of steps in the
                trace exceeds a certain limit. It might be
                caused by a routing loop.
            INTERNAL_ERROR (10):
                Aborted due to internal server error.
            UNSUPPORTED (15):
                Aborted because the test scenario is not
                supported.
            MISMATCHED_IP_VERSION (16):
                Aborted because the source and destination
                resources have no common IP version.
            GKE_KONNECTIVITY_PROXY_UNSUPPORTED (17):
                Aborted because the connection between the
                control plane and the node of the source cluster
                is initiated by the node and managed by the
                Konnectivity proxy.
            RESOURCE_CONFIG_NOT_FOUND (18):
                Aborted because expected resource
                configuration was missing.
            VM_INSTANCE_CONFIG_NOT_FOUND (24):
                Aborted because expected VM instance
                configuration was missing.
            NETWORK_CONFIG_NOT_FOUND (25):
                Aborted because expected network
                configuration was missing.
            FIREWALL_CONFIG_NOT_FOUND (26):
                Aborted because expected firewall
                configuration was missing.
            ROUTE_CONFIG_NOT_FOUND (27):
                Aborted because expected route configuration
                was missing.
            GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT (19):
                Aborted because PSC endpoint selection for
                the Google-managed service is ambiguous (several
                PSC endpoints satisfy test input).
            GOOGLE_MANAGED_SERVICE_AMBIGUOUS_ENDPOINT (39):
                Aborted because endpoint selection for the
                Google-managed service is ambiguous (several
                endpoints satisfy test input).
            SOURCE_PSC_CLOUD_SQL_UNSUPPORTED (20):
                Aborted because tests with a PSC-based Cloud
                SQL instance as a source are not supported.
            SOURCE_EXTERNAL_CLOUD_SQL_UNSUPPORTED (45):
                Aborted because tests with the external
                database as a source are not supported. In such
                replication scenarios, the connection is
                initiated by the Cloud SQL replica instance.
            SOURCE_REDIS_CLUSTER_UNSUPPORTED (34):
                Aborted because tests with a Redis Cluster as
                a source are not supported.
            SOURCE_REDIS_INSTANCE_UNSUPPORTED (35):
                Aborted because tests with a Redis Instance
                as a source are not supported.
            SOURCE_FORWARDING_RULE_UNSUPPORTED (21):
                Aborted because tests with a forwarding rule
                as a source are not supported.
            NON_ROUTABLE_IP_ADDRESS (22):
                Aborted because one of the endpoints is a
                non-routable IP address (loopback, link-local,
                etc).
            UNKNOWN_ISSUE_IN_GOOGLE_MANAGED_PROJECT (30):
                Aborted due to an unknown issue in the
                Google-managed project.
            UNSUPPORTED_GOOGLE_MANAGED_PROJECT_CONFIG (31):
                Aborted due to an unsupported configuration
                of the Google-managed project.
            NO_SERVERLESS_IP_RANGES (37):
                Aborted because the source endpoint is a
                Cloud Run revision with direct VPC access
                enabled, but there are no reserved serverless IP
                ranges.
            IP_VERSION_PROTOCOL_MISMATCH (40):
                Aborted because the used protocol is not
                supported for the used IP version.
            GKE_POD_UNKNOWN_ENDPOINT_LOCATION (41):
                Aborted because selected GKE Pod endpoint
                location is unknown. This is often the case for
                "Pending" Pods, which don't have assigned IP
                addresses yet.
        """

        CAUSE_UNSPECIFIED = 0
        UNKNOWN_NETWORK = 1
        UNKNOWN_PROJECT = 3
        NO_EXTERNAL_IP = 7
        UNINTENDED_DESTINATION = 8
        SOURCE_ENDPOINT_NOT_FOUND = 11
        MISMATCHED_SOURCE_NETWORK = 12
        DESTINATION_ENDPOINT_NOT_FOUND = 13
        MISMATCHED_DESTINATION_NETWORK = 14
        UNKNOWN_IP = 2
        GOOGLE_MANAGED_SERVICE_UNKNOWN_IP = 32
        SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK = 23
        PERMISSION_DENIED = 4
        PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS = 28
        PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS = 29
        PERMISSION_DENIED_NO_CLOUD_ROUTER_CONFIGS = 36
        NO_SOURCE_LOCATION = 5
        NO_SOURCE_GCP_NETWORK_LOCATION = 42
        NO_SOURCE_NON_GCP_NETWORK_LOCATION = 43
        NO_SOURCE_INTERNET_LOCATION = 44
        INVALID_ARGUMENT = 6
        TRACE_TOO_LONG = 9
        INTERNAL_ERROR = 10
        UNSUPPORTED = 15
        MISMATCHED_IP_VERSION = 16
        GKE_KONNECTIVITY_PROXY_UNSUPPORTED = 17
        RESOURCE_CONFIG_NOT_FOUND = 18
        VM_INSTANCE_CONFIG_NOT_FOUND = 24
        NETWORK_CONFIG_NOT_FOUND = 25
        FIREWALL_CONFIG_NOT_FOUND = 26
        ROUTE_CONFIG_NOT_FOUND = 27
        GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT = 19
        GOOGLE_MANAGED_SERVICE_AMBIGUOUS_ENDPOINT = 39
        SOURCE_PSC_CLOUD_SQL_UNSUPPORTED = 20
        SOURCE_EXTERNAL_CLOUD_SQL_UNSUPPORTED = 45
        SOURCE_REDIS_CLUSTER_UNSUPPORTED = 34
        SOURCE_REDIS_INSTANCE_UNSUPPORTED = 35
        SOURCE_FORWARDING_RULE_UNSUPPORTED = 21
        NON_ROUTABLE_IP_ADDRESS = 22
        UNKNOWN_ISSUE_IN_GOOGLE_MANAGED_PROJECT = 30
        UNSUPPORTED_GOOGLE_MANAGED_PROJECT_CONFIG = 31
        NO_SERVERLESS_IP_RANGES = 37
        IP_VERSION_PROTOCOL_MISMATCH = 40
        GKE_POD_UNKNOWN_ENDPOINT_LOCATION = 41

    cause: Cause = proto.Field(
        proto.ENUM,
        number=1,
        enum=Cause,
    )
    resource_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    projects_missing_permission: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DropInfo(proto.Message):
    r"""Details of the final state "drop" and associated resource.

    Attributes:
        cause (google.cloud.network_management_v1.types.DropInfo.Cause):
            Cause that the packet is dropped.
        resource_uri (str):
            URI of the resource that caused the drop.
        source_ip (str):
            Source IP address of the dropped packet (if
            relevant).
        destination_ip (str):
            Destination IP address of the dropped packet
            (if relevant).
        region (str):
            Region of the dropped packet (if relevant).
        source_geolocation_code (str):
            Geolocation (region code) of the source IP
            address (if relevant).
        destination_geolocation_code (str):
            Geolocation (region code) of the destination
            IP address (if relevant).
    """

    class Cause(proto.Enum):
        r"""Drop cause types:

        Values:
            CAUSE_UNSPECIFIED (0):
                Cause is unspecified.
            UNKNOWN_EXTERNAL_ADDRESS (1):
                Destination external address cannot be
                resolved to a known target. If the address is
                used in a Google Cloud project, provide the
                project ID as test input.
            FOREIGN_IP_DISALLOWED (2):
                A Compute Engine instance can only send or receive a packet
                with a foreign IP address if ip_forward is enabled.
            FIREWALL_RULE (3):
                Dropped due to a firewall rule, unless
                allowed due to connection tracking.
            NO_ROUTE (4):
                Dropped due to no matching routes.
            ROUTE_BLACKHOLE (5):
                Dropped due to invalid route. Route's next
                hop is a blackhole.
            ROUTE_WRONG_NETWORK (6):
                Packet is sent to a wrong (unintended)
                network. Example: you trace a packet from
                VM1:Network1 to VM2:Network2, however, the route
                configured in Network1 sends the packet destined
                for VM2's IP address to Network3.
            ROUTE_NEXT_HOP_IP_ADDRESS_NOT_RESOLVED (42):
                Route's next hop IP address cannot be
                resolved to a GCP resource.
            ROUTE_NEXT_HOP_RESOURCE_NOT_FOUND (43):
                Route's next hop resource is not found.
            ROUTE_NEXT_HOP_INSTANCE_WRONG_NETWORK (49):
                Route's next hop instance doesn't have a NIC
                in the route's network.
            ROUTE_NEXT_HOP_INSTANCE_NON_PRIMARY_IP (50):
                Route's next hop IP address is not a primary
                IP address of the next hop instance.
            ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH (51):
                Route's next hop forwarding rule doesn't
                match next hop IP address.
            ROUTE_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED (52):
                Route's next hop VPN tunnel is down (does not
                have valid IKE SAs).
            ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID (53):
                Route's next hop forwarding rule type is
                invalid (it's not a forwarding rule of the
                internal passthrough load balancer).
            NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV6_ADDRESS (44):
                Packet is sent from the Internet to the
                private IPv6 address.
            NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV4_ADDRESS (109):
                Packet is sent from the Internet to the
                private IPv4 address.
            NO_ROUTE_FROM_EXTERNAL_IPV6_SOURCE_TO_PRIVATE_IPV6_ADDRESS (98):
                Packet is sent from the external IPv6 source
                address of an instance to the private IPv6
                address of an instance.
            VPN_TUNNEL_LOCAL_SELECTOR_MISMATCH (45):
                The packet does not match a policy-based VPN
                tunnel local selector.
            VPN_TUNNEL_REMOTE_SELECTOR_MISMATCH (46):
                The packet does not match a policy-based VPN
                tunnel remote selector.
            PRIVATE_TRAFFIC_TO_INTERNET (7):
                Packet with internal destination address sent
                to the internet gateway.
            PRIVATE_GOOGLE_ACCESS_DISALLOWED (8):
                Endpoint with only an internal IP address
                tries to access Google API and services, but
                Private Google Access is not enabled in the
                subnet or is not applicable.
            PRIVATE_GOOGLE_ACCESS_VIA_VPN_TUNNEL_UNSUPPORTED (47):
                Source endpoint tries to access Google API
                and services through the VPN tunnel to another
                network, but Private Google Access needs to be
                enabled in the source endpoint network.
            NO_EXTERNAL_ADDRESS (9):
                Endpoint with only an internal IP address
                tries to access external hosts, but there is no
                matching Cloud NAT gateway in the subnet.
            UNKNOWN_INTERNAL_ADDRESS (10):
                Destination internal address cannot be
                resolved to a known target. If this is a shared
                VPC scenario, verify if the service project ID
                is provided as test input. Otherwise, verify if
                the IP address is being used in the project.
            FORWARDING_RULE_MISMATCH (11):
                Forwarding rule's protocol and ports do not
                match the packet header.
            FORWARDING_RULE_NO_INSTANCES (12):
                Forwarding rule does not have backends
                configured.
            FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK (13):
                Firewalls block the health check probes to the backends and
                cause the backends to be unavailable for traffic from the
                load balancer. For more details, see `Health check firewall
                rules <https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules>`__.
            INGRESS_FIREWALL_TAGS_UNSUPPORTED_BY_DIRECT_VPC_EGRESS (85):
                Matching ingress firewall rules by network
                tags for packets sent via serverless VPC direct
                egress is unsupported. Behavior is undefined.
                https://cloud.google.com/run/docs/configuring/vpc-direct-vpc#limitations
            INSTANCE_NOT_RUNNING (14):
                Packet is sent from or to a Compute Engine
                instance that is not in a running state.
            GKE_CLUSTER_NOT_RUNNING (27):
                Packet sent from or to a GKE cluster that is
                not in running state.
            GKE_POD_NOT_RUNNING (103):
                Packet sent from or to a GKE Pod that is not
                in running state.
            CLOUD_SQL_INSTANCE_NOT_RUNNING (28):
                Packet sent from or to a Cloud SQL instance
                that is not in running state.
            REDIS_INSTANCE_NOT_RUNNING (68):
                Packet sent from or to a Redis Instance that
                is not in running state.
            REDIS_CLUSTER_NOT_RUNNING (69):
                Packet sent from or to a Redis Cluster that
                is not in running state.
            TRAFFIC_TYPE_BLOCKED (15):
                The type of traffic is blocked and the user cannot configure
                a firewall rule to enable it. See `Always blocked
                traffic <https://cloud.google.com/vpc/docs/firewalls#blockedtraffic>`__
                for more details.
            GKE_MASTER_UNAUTHORIZED_ACCESS (16):
                Access to Google Kubernetes Engine cluster master's endpoint
                is not authorized. See `Access to the cluster
                endpoints <https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#access_to_the_cluster_endpoints>`__
                for more details.
            CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS (17):
                Access to the Cloud SQL instance endpoint is not authorized.
                See `Authorizing with authorized
                networks <https://cloud.google.com/sql/docs/mysql/authorize-networks>`__
                for more details.
            DROPPED_INSIDE_GKE_SERVICE (18):
                Packet was dropped inside Google Kubernetes
                Engine Service.
            DROPPED_INSIDE_CLOUD_SQL_SERVICE (19):
                Packet was dropped inside Cloud SQL Service.
            DROPPED_INSIDE_DMS_PRIVATE_CONNECTION (114):
                Packet was dropped inside DMS Private
                Connection.
            GOOGLE_MANAGED_SERVICE_NO_PEERING (20):
                Packet was dropped because there is no
                peering between the originating network and the
                Google Managed Services Network.
            GOOGLE_MANAGED_SERVICE_NO_PSC_ENDPOINT (38):
                Packet was dropped because the Google-managed
                service uses Private Service Connect (PSC), but
                the PSC endpoint is not found in the project.
            GKE_PSC_ENDPOINT_MISSING (36):
                Packet was dropped because the GKE cluster
                uses Private Service Connect (PSC), but the PSC
                endpoint is not found in the project.
            CLOUD_SQL_INSTANCE_NO_IP_ADDRESS (21):
                Packet was dropped because the Cloud SQL
                instance has neither a private nor a public IP
                address.
            GKE_CONTROL_PLANE_REGION_MISMATCH (30):
                Packet was dropped because a GKE cluster
                private endpoint is unreachable from a region
                different from the cluster's region.
            PUBLIC_GKE_CONTROL_PLANE_TO_PRIVATE_DESTINATION (31):
                Packet sent from a public GKE cluster control
                plane to a private IP address.
            GKE_CONTROL_PLANE_NO_ROUTE (32):
                Packet was dropped because there is no route
                from a GKE cluster control plane to a
                destination network.
            CLOUD_SQL_INSTANCE_NOT_CONFIGURED_FOR_EXTERNAL_TRAFFIC (33):
                Packet sent from a Cloud SQL instance to an
                external IP address is not allowed. The Cloud
                SQL instance is not configured to send packets
                to external IP addresses.
            PUBLIC_CLOUD_SQL_INSTANCE_TO_PRIVATE_DESTINATION (34):
                Packet sent from a Cloud SQL instance with
                only a public IP address to a private IP
                address.
            CLOUD_SQL_INSTANCE_NO_ROUTE (35):
                Packet was dropped because there is no route
                from a Cloud SQL instance to a destination
                network.
            CLOUD_SQL_CONNECTOR_REQUIRED (63):
                Packet was dropped because the Cloud SQL
                instance requires all connections to use Cloud
                SQL connectors and to target the Cloud SQL proxy
                port (3307).
            CLOUD_FUNCTION_NOT_ACTIVE (22):
                Packet could be dropped because the Cloud
                Function is not in an active status.
            VPC_CONNECTOR_NOT_SET (23):
                Packet could be dropped because no VPC
                connector is set.
            VPC_CONNECTOR_NOT_RUNNING (24):
                Packet could be dropped because the VPC
                connector is not in a running state.
            VPC_CONNECTOR_SERVERLESS_TRAFFIC_BLOCKED (60):
                Packet could be dropped because the traffic
                from the serverless service to the VPC connector
                is not allowed.
            VPC_CONNECTOR_HEALTH_CHECK_TRAFFIC_BLOCKED (61):
                Packet could be dropped because the health
                check traffic to the VPC connector is not
                allowed.
            FORWARDING_RULE_REGION_MISMATCH (25):
                Packet could be dropped because it was sent
                from a different region to a regional forwarding
                without global access.
            PSC_CONNECTION_NOT_ACCEPTED (26):
                The Private Service Connect endpoint is in a
                project that is not approved to connect to the
                service.
            PSC_ENDPOINT_ACCESSED_FROM_PEERED_NETWORK (41):
                The packet is sent to the Private Service Connect endpoint
                over the peering, but `it's not
                supported <https://cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises>`__.
            PSC_NEG_PRODUCER_ENDPOINT_NO_GLOBAL_ACCESS (48):
                The packet is sent to the Private Service
                Connect backend (network endpoint group), but
                the producer PSC forwarding rule does not have
                global access enabled.
            PSC_NEG_PRODUCER_FORWARDING_RULE_MULTIPLE_PORTS (54):
                The packet is sent to the Private Service
                Connect backend (network endpoint group), but
                the producer PSC forwarding rule has multiple
                ports specified.
            CLOUD_SQL_PSC_NEG_UNSUPPORTED (58):
                The packet is sent to the Private Service
                Connect backend (network endpoint group)
                targeting a Cloud SQL service attachment, but
                this configuration is not supported.
            NO_NAT_SUBNETS_FOR_PSC_SERVICE_ATTACHMENT (57):
                No NAT subnets are defined for the PSC
                service attachment.
            PSC_TRANSITIVITY_NOT_PROPAGATED (64):
                PSC endpoint is accessed via NCC, but PSC
                transitivity configuration is not yet
                propagated.
            HYBRID_NEG_NON_DYNAMIC_ROUTE_MATCHED (55):
                The packet sent from the hybrid NEG proxy
                matches a non-dynamic route, but such a
                configuration is not supported.
            HYBRID_NEG_NON_LOCAL_DYNAMIC_ROUTE_MATCHED (56):
                The packet sent from the hybrid NEG proxy
                matches a dynamic route with a next hop in a
                different region, but such a configuration is
                not supported.
            CLOUD_RUN_REVISION_NOT_READY (29):
                Packet sent from a Cloud Run revision that is
                not ready.
            CLOUD_RUN_JOB_NOT_READY (113):
                Packet sent from a Cloud Run job that is not
                ready.
            DROPPED_INSIDE_PSC_SERVICE_PRODUCER (37):
                Packet was dropped inside Private Service
                Connect service producer.
            LOAD_BALANCER_HAS_NO_PROXY_SUBNET (39):
                Packet sent to a load balancer, which
                requires a proxy-only subnet and the subnet is
                not found.
            CLOUD_NAT_NO_ADDRESSES (40):
                Packet sent to Cloud Nat without active NAT
                IPs.
            ROUTING_LOOP (59):
                Packet is stuck in a routing loop.
            DROPPED_INSIDE_GOOGLE_MANAGED_SERVICE (62):
                Packet is dropped inside a Google-managed
                service due to being delivered in return trace
                to an endpoint that doesn't match the endpoint
                the packet was sent from in forward trace. Used
                only for return traces.
            LOAD_BALANCER_BACKEND_INVALID_NETWORK (65):
                Packet is dropped due to a load balancer
                backend instance not having a network interface
                in the network expected by the load balancer.
            BACKEND_SERVICE_NAMED_PORT_NOT_DEFINED (66):
                Packet is dropped due to a backend service
                named port not being defined on the instance
                group level.
            DESTINATION_IS_PRIVATE_NAT_IP_RANGE (67):
                Packet is dropped due to a destination IP
                range being part of a Private NAT IP range.
            DROPPED_INSIDE_REDIS_INSTANCE_SERVICE (70):
                Generic drop cause for a packet being dropped
                inside a Redis Instance service project.
            REDIS_INSTANCE_UNSUPPORTED_PORT (71):
                Packet is dropped due to an unsupported port
                being used to connect to a Redis Instance. Port
                6379 should be used to connect to a Redis
                Instance.
            REDIS_INSTANCE_CONNECTING_FROM_PUPI_ADDRESS (72):
                Packet is dropped due to connecting from PUPI
                address to a PSA based Redis Instance.
            REDIS_INSTANCE_NO_ROUTE_TO_DESTINATION_NETWORK (73):
                Packet is dropped due to no route to the
                destination network.
            REDIS_INSTANCE_NO_EXTERNAL_IP (74):
                Redis Instance does not have an external IP
                address.
            REDIS_INSTANCE_UNSUPPORTED_PROTOCOL (78):
                Packet is dropped due to an unsupported
                protocol being used to connect to a Redis
                Instance. Only TCP connections are accepted by a
                Redis Instance.
            DROPPED_INSIDE_REDIS_CLUSTER_SERVICE (75):
                Generic drop cause for a packet being dropped
                inside a Redis Cluster service project.
            REDIS_CLUSTER_UNSUPPORTED_PORT (76):
                Packet is dropped due to an unsupported port
                being used to connect to a Redis Cluster. Ports
                6379 and 11000 to 13047 should be used to
                connect to a Redis Cluster.
            REDIS_CLUSTER_NO_EXTERNAL_IP (77):
                Redis Cluster does not have an external IP
                address.
            REDIS_CLUSTER_UNSUPPORTED_PROTOCOL (79):
                Packet is dropped due to an unsupported
                protocol being used to connect to a Redis
                Cluster. Only TCP connections are accepted by a
                Redis Cluster.
            NO_ADVERTISED_ROUTE_TO_GCP_DESTINATION (80):
                Packet from the non-GCP (on-prem) or unknown
                GCP network is dropped due to the destination IP
                address not belonging to any IP prefix
                advertised via BGP by the Cloud Router.
            NO_TRAFFIC_SELECTOR_TO_GCP_DESTINATION (81):
                Packet from the non-GCP (on-prem) or unknown
                GCP network is dropped due to the destination IP
                address not belonging to any IP prefix included
                to the local traffic selector of the VPN tunnel.
            NO_KNOWN_ROUTE_FROM_PEERED_NETWORK_TO_DESTINATION (82):
                Packet from the unknown peered network is
                dropped due to no known route from the source
                network to the destination IP address.
            PRIVATE_NAT_TO_PSC_ENDPOINT_UNSUPPORTED (83):
                Sending packets processed by the Private NAT
                Gateways to the Private Service Connect
                endpoints is not supported.
            PSC_PORT_MAPPING_PORT_MISMATCH (86):
                Packet is sent to the PSC port mapping
                service, but its destination port does not match
                any port mapping rules.
            PSC_PORT_MAPPING_WITHOUT_PSC_CONNECTION_UNSUPPORTED (87):
                Sending packets directly to the PSC port
                mapping service without going through the PSC
                connection is not supported.
            UNSUPPORTED_ROUTE_MATCHED_FOR_NAT64_DESTINATION (88):
                Packet with destination IP address within the
                reserved NAT64 range is dropped due to matching
                a route of an unsupported type.
            TRAFFIC_FROM_HYBRID_ENDPOINT_TO_INTERNET_DISALLOWED (89):
                Packet could be dropped because hybrid
                endpoint like a VPN gateway or Interconnect is
                not allowed to send traffic to the Internet.
            NO_MATCHING_NAT64_GATEWAY (90):
                Packet with destination IP address within the
                reserved NAT64 range is dropped due to no
                matching NAT gateway in the subnet.
            NO_CONFIGURED_PRIVATE_NAT64_RULE (107):
                Packet is dropped due to matching a Private
                NAT64 gateway with no rules for source IPv6
                addresses.
            LOAD_BALANCER_BACKEND_IP_VERSION_MISMATCH (96):
                Packet is dropped due to being sent to a
                backend of a passthrough load balancer that
                doesn't use the same IP version as the frontend.
            NO_KNOWN_ROUTE_FROM_NCC_NETWORK_TO_DESTINATION (97):
                Packet from the unknown NCC network is
                dropped due to no known route from the source
                network to the destination IP address.
            CLOUD_NAT_PROTOCOL_UNSUPPORTED (99):
                Packet is dropped by Cloud NAT due to using
                an unsupported protocol.
            L2_INTERCONNECT_UNSUPPORTED_PROTOCOL (100):
                Packet is dropped due to using an unsupported
                protocol (any other than UDP) for L2
                Interconnect.
            L2_INTERCONNECT_UNSUPPORTED_PORT (101):
                Packet is dropped due to using an unsupported
                port (any other than 6081) for L2 Interconnect.
            L2_INTERCONNECT_DESTINATION_IP_MISMATCH (102):
                Packet is dropped due to destination IP not
                matching the appliance mapping IPs configured on
                the L2 Interconnect attachment.
            NCC_ROUTE_WITHIN_HYBRID_SUBNET_UNSUPPORTED (104):
                Packet could be dropped because it matches a
                route associated with an NCC spoke in the hybrid
                subnet context, but such a configuration is not
                supported.
            HYBRID_SUBNET_REGION_MISMATCH (105):
                Packet is dropped because the region of the
                hybrid subnet is different from the region of
                the next hop of the route matched within this
                hybrid subnet.
            HYBRID_SUBNET_NO_ROUTE (106):
                Packet is dropped because no matching route
                was found in the hybrid subnet.
            GKE_NETWORK_POLICY (108):
                Packet is dropped by GKE Network Policy.
            NO_VALID_ROUTE_FROM_GOOGLE_MANAGED_NETWORK_TO_DESTINATION (110):
                Packet is dropped because there is no valid
                matching route from the network of the
                Google-managed service to the destination.
            PRIVATE_CONNECTION_NO_RUNNING_INSTANCE (111):
                Packet is dropped due to no running instance
                found for private connection.
        """

        CAUSE_UNSPECIFIED = 0
        UNKNOWN_EXTERNAL_ADDRESS = 1
        FOREIGN_IP_DISALLOWED = 2
        FIREWALL_RULE = 3
        NO_ROUTE = 4
        ROUTE_BLACKHOLE = 5
        ROUTE_WRONG_NETWORK = 6
        ROUTE_NEXT_HOP_IP_ADDRESS_NOT_RESOLVED = 42
        ROUTE_NEXT_HOP_RESOURCE_NOT_FOUND = 43
        ROUTE_NEXT_HOP_INSTANCE_WRONG_NETWORK = 49
        ROUTE_NEXT_HOP_INSTANCE_NON_PRIMARY_IP = 50
        ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH = 51
        ROUTE_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED = 52
        ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID = 53
        NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV6_ADDRESS = 44
        NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV4_ADDRESS = 109
        NO_ROUTE_FROM_EXTERNAL_IPV6_SOURCE_TO_PRIVATE_IPV6_ADDRESS = 98
        VPN_TUNNEL_LOCAL_SELECTOR_MISMATCH = 45
        VPN_TUNNEL_REMOTE_SELECTOR_MISMATCH = 46
        PRIVATE_TRAFFIC_TO_INTERNET = 7
        PRIVATE_GOOGLE_ACCESS_DISALLOWED = 8
        PRIVATE_GOOGLE_ACCESS_VIA_VPN_TUNNEL_UNSUPPORTED = 47
        NO_EXTERNAL_ADDRESS = 9
        UNKNOWN_INTERNAL_ADDRESS = 10
        FORWARDING_RULE_MISMATCH = 11
        FORWARDING_RULE_NO_INSTANCES = 12
        FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK = 13
        INGRESS_FIREWALL_TAGS_UNSUPPORTED_BY_DIRECT_VPC_EGRESS = 85
        INSTANCE_NOT_RUNNING = 14
        GKE_CLUSTER_NOT_RUNNING = 27
        GKE_POD_NOT_RUNNING = 103
        CLOUD_SQL_INSTANCE_NOT_RUNNING = 28
        REDIS_INSTANCE_NOT_RUNNING = 68
        REDIS_CLUSTER_NOT_RUNNING = 69
        TRAFFIC_TYPE_BLOCKED = 15
        GKE_MASTER_UNAUTHORIZED_ACCESS = 16
        CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS = 17
        DROPPED_INSIDE_GKE_SERVICE = 18
        DROPPED_INSIDE_CLOUD_SQL_SERVICE = 19
        DROPPED_INSIDE_DMS_PRIVATE_CONNECTION = 114
        GOOGLE_MANAGED_SERVICE_NO_PEERING = 20
        GOOGLE_MANAGED_SERVICE_NO_PSC_ENDPOINT = 38
        GKE_PSC_ENDPOINT_MISSING = 36
        CLOUD_SQL_INSTANCE_NO_IP_ADDRESS = 21
        GKE_CONTROL_PLANE_REGION_MISMATCH = 30
        PUBLIC_GKE_CONTROL_PLANE_TO_PRIVATE_DESTINATION = 31
        GKE_CONTROL_PLANE_NO_ROUTE = 32
        CLOUD_SQL_INSTANCE_NOT_CONFIGURED_FOR_EXTERNAL_TRAFFIC = 33
        PUBLIC_CLOUD_SQL_INSTANCE_TO_PRIVATE_DESTINATION = 34
        CLOUD_SQL_INSTANCE_NO_ROUTE = 35
        CLOUD_SQL_CONNECTOR_REQUIRED = 63
        CLOUD_FUNCTION_NOT_ACTIVE = 22
        VPC_CONNECTOR_NOT_SET = 23
        VPC_CONNECTOR_NOT_RUNNING = 24
        VPC_CONNECTOR_SERVERLESS_TRAFFIC_BLOCKED = 60
        VPC_CONNECTOR_HEALTH_CHECK_TRAFFIC_BLOCKED = 61
        FORWARDING_RULE_REGION_MISMATCH = 25
        PSC_CONNECTION_NOT_ACCEPTED = 26
        PSC_ENDPOINT_ACCESSED_FROM_PEERED_NETWORK = 41
        PSC_NEG_PRODUCER_ENDPOINT_NO_GLOBAL_ACCESS = 48
        PSC_NEG_PRODUCER_FORWARDING_RULE_MULTIPLE_PORTS = 54
        CLOUD_SQL_PSC_NEG_UNSUPPORTED = 58
        NO_NAT_SUBNETS_FOR_PSC_SERVICE_ATTACHMENT = 57
        PSC_TRANSITIVITY_NOT_PROPAGATED = 64
        HYBRID_NEG_NON_DYNAMIC_ROUTE_MATCHED = 55
        HYBRID_NEG_NON_LOCAL_DYNAMIC_ROUTE_MATCHED = 56
        CLOUD_RUN_REVISION_NOT_READY = 29
        CLOUD_RUN_JOB_NOT_READY = 113
        DROPPED_INSIDE_PSC_SERVICE_PRODUCER = 37
        LOAD_BALANCER_HAS_NO_PROXY_SUBNET = 39
        CLOUD_NAT_NO_ADDRESSES = 40
        ROUTING_LOOP = 59
        DROPPED_INSIDE_GOOGLE_MANAGED_SERVICE = 62
        LOAD_BALANCER_BACKEND_INVALID_NETWORK = 65
        BACKEND_SERVICE_NAMED_PORT_NOT_DEFINED = 66
        DESTINATION_IS_PRIVATE_NAT_IP_RANGE = 67
        DROPPED_INSIDE_REDIS_INSTANCE_SERVICE = 70
        REDIS_INSTANCE_UNSUPPORTED_PORT = 71
        REDIS_INSTANCE_CONNECTING_FROM_PUPI_ADDRESS = 72
        REDIS_INSTANCE_NO_ROUTE_TO_DESTINATION_NETWORK = 73
        REDIS_INSTANCE_NO_EXTERNAL_IP = 74
        REDIS_INSTANCE_UNSUPPORTED_PROTOCOL = 78
        DROPPED_INSIDE_REDIS_CLUSTER_SERVICE = 75
        REDIS_CLUSTER_UNSUPPORTED_PORT = 76
        REDIS_CLUSTER_NO_EXTERNAL_IP = 77
        REDIS_CLUSTER_UNSUPPORTED_PROTOCOL = 79
        NO_ADVERTISED_ROUTE_TO_GCP_DESTINATION = 80
        NO_TRAFFIC_SELECTOR_TO_GCP_DESTINATION = 81
        NO_KNOWN_ROUTE_FROM_PEERED_NETWORK_TO_DESTINATION = 82
        PRIVATE_NAT_TO_PSC_ENDPOINT_UNSUPPORTED = 83
        PSC_PORT_MAPPING_PORT_MISMATCH = 86
        PSC_PORT_MAPPING_WITHOUT_PSC_CONNECTION_UNSUPPORTED = 87
        UNSUPPORTED_ROUTE_MATCHED_FOR_NAT64_DESTINATION = 88
        TRAFFIC_FROM_HYBRID_ENDPOINT_TO_INTERNET_DISALLOWED = 89
        NO_MATCHING_NAT64_GATEWAY = 90
        NO_CONFIGURED_PRIVATE_NAT64_RULE = 107
        LOAD_BALANCER_BACKEND_IP_VERSION_MISMATCH = 96
        NO_KNOWN_ROUTE_FROM_NCC_NETWORK_TO_DESTINATION = 97
        CLOUD_NAT_PROTOCOL_UNSUPPORTED = 99
        L2_INTERCONNECT_UNSUPPORTED_PROTOCOL = 100
        L2_INTERCONNECT_UNSUPPORTED_PORT = 101
        L2_INTERCONNECT_DESTINATION_IP_MISMATCH = 102
        NCC_ROUTE_WITHIN_HYBRID_SUBNET_UNSUPPORTED = 104
        HYBRID_SUBNET_REGION_MISMATCH = 105
        HYBRID_SUBNET_NO_ROUTE = 106
        GKE_NETWORK_POLICY = 108
        NO_VALID_ROUTE_FROM_GOOGLE_MANAGED_NETWORK_TO_DESTINATION = 110
        PRIVATE_CONNECTION_NO_RUNNING_INSTANCE = 111

    cause: Cause = proto.Field(
        proto.ENUM,
        number=1,
        enum=Cause,
    )
    resource_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_ip: str = proto.Field(
        proto.STRING,
        number=3,
    )
    destination_ip: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region: str = proto.Field(
        proto.STRING,
        number=5,
    )
    source_geolocation_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    destination_geolocation_code: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GKEMasterInfo(proto.Message):
    r"""For display only. Metadata associated with a Google
    Kubernetes Engine (GKE) cluster master.

    Attributes:
        cluster_uri (str):
            URI of a GKE cluster.
        cluster_network_uri (str):
            URI of a GKE cluster network.
        internal_ip (str):
            Internal IP address of a GKE cluster control
            plane.
        external_ip (str):
            External IP address of a GKE cluster control
            plane.
        dns_endpoint (str):
            DNS endpoint of a GKE cluster control plane.
    """

    cluster_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_network_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    internal_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    external_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    dns_endpoint: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GkePodInfo(proto.Message):
    r"""For display only. Metadata associated with a Google
    Kubernetes Engine (GKE) Pod.

    Attributes:
        pod_uri (str):
            URI of a GKE Pod. For Pods in regional Clusters, the URI
            format is:
            ``projects/{project}/locations/{location}/clusters/{cluster}/k8s/namespaces/{namespace}/pods/{pod}``
            For Pods in zonal Clusters, the URI format is:
            ``projects/{project}/zones/{zone}/clusters/{cluster}/k8s/namespaces/{namespace}/pods/{pod}``
        ip_address (str):
            IP address of a GKE Pod. If the Pod is
            dual-stack, this is the IP address relevant to
            the trace.
        network_uri (str):
            URI of the network containing the GKE Pod.
    """

    pod_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class IpMasqueradingSkippedInfo(proto.Message):
    r"""For display only. Contains information about why IP
    masquerading was skipped for the packet.

    Attributes:
        reason (google.cloud.network_management_v1.types.IpMasqueradingSkippedInfo.Reason):
            Reason why IP masquerading was not applied.
        non_masquerade_range (str):
            The matched non-masquerade IP range. Only set if reason is
            DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE or
            DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE.
    """

    class Reason(proto.Enum):
        r"""Reason why IP masquerading was skipped.

        Values:
            REASON_UNSPECIFIED (0):
                Unused default value.
            DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE (1):
                Masquerading not applied because destination
                IP is in one of configured non-masquerade
                ranges.
            DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE (2):
                Masquerading not applied because destination
                IP is in one of default non-masquerade ranges.
            DESTINATION_ON_SAME_NODE (3):
                Masquerading not applied because destination
                is on the same Node.
            DEFAULT_SNAT_DISABLED (4):
                Masquerading not applied because
                ip-masq-agent doesn't exist and default SNAT is
                disabled.
            NO_MASQUERADING_FOR_IPV6 (5):
                Masquerading not applied because the packet's
                IP version is IPv6.
            POD_USES_NODE_NETWORK_NAMESPACE (6):
                Masquerading not applied because the source
                Pod uses the host Node's network namespace,
                including the Node's IP address.
            NO_MASQUERADING_FOR_RETURN_PACKET (7):
                Masquerading not applied because the packet
                is a return packet.
        """

        REASON_UNSPECIFIED = 0
        DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE = 1
        DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE = 2
        DESTINATION_ON_SAME_NODE = 3
        DEFAULT_SNAT_DISABLED = 4
        NO_MASQUERADING_FOR_IPV6 = 5
        POD_USES_NODE_NETWORK_NAMESPACE = 6
        NO_MASQUERADING_FOR_RETURN_PACKET = 7

    reason: Reason = proto.Field(
        proto.ENUM,
        number=1,
        enum=Reason,
    )
    non_masquerade_range: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GkeNetworkPolicyInfo(proto.Message):
    r"""For display only. Metadata associated with a GKE Network
    Policy.

    Attributes:
        display_name (str):
            The name of the Network Policy.
        uri (str):
            The URI of the Network Policy. Format for a Network Policy
            in a zonal cluster:
            ``projects/<project_id>/zones/<zone>/clusters/<cluster>/k8s/namespaces/<namespace>/networking.k8s.io/networkpolicies/<networkpolicy>``
            Format for a Network Policy in a regional cluster:
            ``projects/<project_id>/locations/<location>/clusters/<cluster>/k8s/namespaces/<namespace>/networking.k8s.io/networkpolicies/<networkpolicy>``
        direction (str):
            Possible values: INGRESS, EGRESS
        action (str):
            Possible values: ALLOW, DENY
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    direction: str = proto.Field(
        proto.STRING,
        number=3,
    )
    action: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GkeNetworkPolicySkippedInfo(proto.Message):
    r"""For display only. Contains information about why GKE Network
    Policy evaluation was skipped.

    Attributes:
        reason (google.cloud.network_management_v1.types.GkeNetworkPolicySkippedInfo.Reason):
            Reason why Network Policy evaluation was
            skipped.
    """

    class Reason(proto.Enum):
        r"""

        Values:
            REASON_UNSPECIFIED (0):
                Unused default value.
            NETWORK_POLICY_DISABLED (1):
                Network Policy is disabled on the cluster.
            INGRESS_SOURCE_ON_SAME_NODE (2):
                Ingress traffic to a Pod from a source on the
                same Node is always allowed.
            EGRESS_FROM_NODE_NETWORK_NAMESPACE_POD (3):
                Egress traffic from a Pod that uses the
                Node's network namespace is not subject to
                Network Policy.
            NETWORK_POLICY_NOT_APPLIED_TO_RESPONSE_TRAFFIC (4):
                Network Policy is not applied to response
                traffic. This is because GKE Network Policy
                evaluation is stateful in both GKE Dataplane V2
                (eBPF) and legacy (iptables) implementations.
            NETWORK_POLICY_ANALYSIS_UNSUPPORTED (100):
                Network Policy evaluation is currently not
                supported for clusters with FQDN Network
                Policies enabled.
        """

        REASON_UNSPECIFIED = 0
        NETWORK_POLICY_DISABLED = 1
        INGRESS_SOURCE_ON_SAME_NODE = 2
        EGRESS_FROM_NODE_NETWORK_NAMESPACE_POD = 3
        NETWORK_POLICY_NOT_APPLIED_TO_RESPONSE_TRAFFIC = 4
        NETWORK_POLICY_ANALYSIS_UNSUPPORTED = 100

    reason: Reason = proto.Field(
        proto.ENUM,
        number=1,
        enum=Reason,
    )


class CloudSQLInstanceInfo(proto.Message):
    r"""For display only. Metadata associated with a Cloud SQL
    instance.

    Attributes:
        display_name (str):
            Name of a Cloud SQL instance.
        uri (str):
            URI of a Cloud SQL instance.
        network_uri (str):
            URI of a Cloud SQL instance network or empty
            string if the instance does not have one.
        internal_ip (str):
            Internal IP address of a Cloud SQL instance.
        external_ip (str):
            External IP address of a Cloud SQL instance.
        region (str):
            Region in which the Cloud SQL instance is
            running.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    internal_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    external_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    region: str = proto.Field(
        proto.STRING,
        number=7,
    )


class RedisInstanceInfo(proto.Message):
    r"""For display only. Metadata associated with a Cloud Redis
    Instance.

    Attributes:
        display_name (str):
            Name of a Cloud Redis Instance.
        uri (str):
            URI of a Cloud Redis Instance.
        network_uri (str):
            URI of a Cloud Redis Instance network.
        primary_endpoint_ip (str):
            Primary endpoint IP address of a Cloud Redis
            Instance.
        read_endpoint_ip (str):
            Read endpoint IP address of a Cloud Redis
            Instance (if applicable).
        region (str):
            Region in which the Cloud Redis Instance is
            defined.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    primary_endpoint_ip: str = proto.Field(
        proto.STRING,
        number=4,
    )
    read_endpoint_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    region: str = proto.Field(
        proto.STRING,
        number=6,
    )


class RedisClusterInfo(proto.Message):
    r"""For display only. Metadata associated with a Redis Cluster.

    Attributes:
        display_name (str):
            Name of a Redis Cluster.
        uri (str):
            URI of a Redis Cluster in format
            "projects/{project_id}/locations/{location}/clusters/{cluster_id}".
        network_uri (str):
            URI of the network containing the Redis Cluster endpoints in
            format "projects/{project_id}/global/networks/{network_id}".
        discovery_endpoint_ip_address (str):
            Discovery endpoint IP address of a Redis
            Cluster.
        secondary_endpoint_ip_address (str):
            Secondary endpoint IP address of a Redis
            Cluster.
        location (str):
            Name of the region in which the Redis Cluster
            is defined. For example, "us-central1".
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    discovery_endpoint_ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    secondary_endpoint_ip_address: str = proto.Field(
        proto.STRING,
        number=5,
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )


class CloudFunctionInfo(proto.Message):
    r"""For display only. Metadata associated with a Cloud Function.

    Attributes:
        display_name (str):
            Name of a Cloud Function.
        uri (str):
            URI of a Cloud Function.
        location (str):
            Location in which the Cloud Function is
            deployed.
        version_id (int):
            Latest successfully deployed version id of
            the Cloud Function.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version_id: int = proto.Field(
        proto.INT64,
        number=4,
    )


class CloudRunRevisionInfo(proto.Message):
    r"""For display only. Metadata associated with a Cloud Run
    revision.

    Attributes:
        display_name (str):
            Name of a Cloud Run revision.
        uri (str):
            URI of a Cloud Run revision.
        location (str):
            Location in which this revision is deployed.
        service_uri (str):
            URI of Cloud Run service this revision
            belongs to.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CloudRunJobInfo(proto.Message):
    r"""For display only. Metadata associated with a Cloud Run job.

    Attributes:
        display_name (str):
            Name of a Cloud Run job.
        uri (str):
            URI of a Cloud Run job.
        location (str):
            Location in which this job is deployed.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AppEngineVersionInfo(proto.Message):
    r"""For display only. Metadata associated with an App Engine
    version.

    Attributes:
        display_name (str):
            Name of an App Engine version.
        uri (str):
            URI of an App Engine version.
        runtime (str):
            Runtime of the App Engine version.
        environment (str):
            App Engine execution environment for a
            version.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    runtime: str = proto.Field(
        proto.STRING,
        number=3,
    )
    environment: str = proto.Field(
        proto.STRING,
        number=4,
    )


class VpcConnectorInfo(proto.Message):
    r"""For display only. Metadata associated with a VPC connector.

    Attributes:
        display_name (str):
            Name of a VPC connector.
        uri (str):
            URI of a VPC connector.
        location (str):
            Location in which the VPC connector is
            deployed.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DirectVpcEgressConnectionInfo(proto.Message):
    r"""For display only. Metadata associated with a serverless
    direct VPC egress connection.

    Attributes:
        network_uri (str):
            URI of direct access network.
        subnetwork_uri (str):
            URI of direct access subnetwork.
        selected_ip_range (str):
            Selected IP range.
        selected_ip_address (str):
            Selected starting IP address, from the
            selected IP range.
        region (str):
            Region in which the Direct VPC egress is
            deployed.
    """

    network_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnetwork_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    selected_ip_range: str = proto.Field(
        proto.STRING,
        number=3,
    )
    selected_ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ServerlessExternalConnectionInfo(proto.Message):
    r"""For display only. Metadata associated with a serverless
    public connection.

    Attributes:
        selected_ip_address (str):
            Selected starting IP address, from the Google
            dynamic address pool.
    """

    selected_ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NatInfo(proto.Message):
    r"""For display only. Metadata associated with NAT.

    Attributes:
        type_ (google.cloud.network_management_v1.types.NatInfo.Type):
            Type of NAT.
        protocol (str):
            IP protocol in string format, for example:
            "TCP", "UDP", "ICMP".
        network_uri (str):
            URI of the network where NAT translation
            takes place.
        old_source_ip (str):
            Source IP address before NAT translation.
        new_source_ip (str):
            Source IP address after NAT translation.
        old_destination_ip (str):
            Destination IP address before NAT
            translation.
        new_destination_ip (str):
            Destination IP address after NAT translation.
        old_source_port (int):
            Source port before NAT translation. Only
            valid when protocol is TCP or UDP.
        new_source_port (int):
            Source port after NAT translation. Only valid
            when protocol is TCP or UDP.
        old_destination_port (int):
            Destination port before NAT translation. Only
            valid when protocol is TCP or UDP.
        new_destination_port (int):
            Destination port after NAT translation. Only
            valid when protocol is TCP or UDP.
        router_uri (str):
            Uri of the Cloud Router. Only valid when type is CLOUD_NAT.
        nat_gateway_name (str):
            The name of Cloud NAT Gateway. Only valid when type is
            CLOUD_NAT.
        cloud_nat_gateway_type (google.cloud.network_management_v1.types.NatInfo.CloudNatGatewayType):
            Type of Cloud NAT gateway. Only valid when ``type`` is
            CLOUD_NAT.
    """

    class Type(proto.Enum):
        r"""Types of NAT.

        Values:
            TYPE_UNSPECIFIED (0):
                Type is unspecified.
            INTERNAL_TO_EXTERNAL (1):
                From Compute Engine instance's internal
                address to external address.
            EXTERNAL_TO_INTERNAL (2):
                From Compute Engine instance's external
                address to internal address.
            CLOUD_NAT (3):
                Cloud NAT Gateway.
            PRIVATE_SERVICE_CONNECT (4):
                Private service connect NAT.
            GKE_POD_IP_MASQUERADING (5):
                GKE Pod IP address masquerading.
        """

        TYPE_UNSPECIFIED = 0
        INTERNAL_TO_EXTERNAL = 1
        EXTERNAL_TO_INTERNAL = 2
        CLOUD_NAT = 3
        PRIVATE_SERVICE_CONNECT = 4
        GKE_POD_IP_MASQUERADING = 5

    class CloudNatGatewayType(proto.Enum):
        r"""Types of Cloud NAT gateway.

        Values:
            CLOUD_NAT_GATEWAY_TYPE_UNSPECIFIED (0):
                Type is unspecified.
            PUBLIC_NAT44 (1):
                Public NAT gateway.
            PUBLIC_NAT64 (2):
                Public NAT64 gateway.
            PRIVATE_NAT_NCC (3):
                Private NAT gateway for NCC.
            PRIVATE_NAT_HYBRID (4):
                Private NAT gateway for hybrid connectivity.
            PRIVATE_NAT64 (5):
                Private NAT64 gateway.
        """

        CLOUD_NAT_GATEWAY_TYPE_UNSPECIFIED = 0
        PUBLIC_NAT44 = 1
        PUBLIC_NAT64 = 2
        PRIVATE_NAT_NCC = 3
        PRIVATE_NAT_HYBRID = 4
        PRIVATE_NAT64 = 5

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    protocol: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    old_source_ip: str = proto.Field(
        proto.STRING,
        number=4,
    )
    new_source_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    old_destination_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    new_destination_ip: str = proto.Field(
        proto.STRING,
        number=7,
    )
    old_source_port: int = proto.Field(
        proto.INT32,
        number=8,
    )
    new_source_port: int = proto.Field(
        proto.INT32,
        number=9,
    )
    old_destination_port: int = proto.Field(
        proto.INT32,
        number=10,
    )
    new_destination_port: int = proto.Field(
        proto.INT32,
        number=11,
    )
    router_uri: str = proto.Field(
        proto.STRING,
        number=12,
    )
    nat_gateway_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    cloud_nat_gateway_type: CloudNatGatewayType = proto.Field(
        proto.ENUM,
        number=14,
        enum=CloudNatGatewayType,
    )


class ProxyConnectionInfo(proto.Message):
    r"""For display only. Metadata associated with ProxyConnection.

    Attributes:
        protocol (str):
            IP protocol in string format, for example:
            "TCP", "UDP", "ICMP".
        old_source_ip (str):
            Source IP address of an original connection.
        new_source_ip (str):
            Source IP address of a new connection.
        old_destination_ip (str):
            Destination IP address of an original
            connection
        new_destination_ip (str):
            Destination IP address of a new connection.
        old_source_port (int):
            Source port of an original connection. Only
            valid when protocol is TCP or UDP.
        new_source_port (int):
            Source port of a new connection. Only valid
            when protocol is TCP or UDP.
        old_destination_port (int):
            Destination port of an original connection.
            Only valid when protocol is TCP or UDP.
        new_destination_port (int):
            Destination port of a new connection. Only
            valid when protocol is TCP or UDP.
        subnet_uri (str):
            Uri of proxy subnet.
        network_uri (str):
            URI of the network where connection is
            proxied.
    """

    protocol: str = proto.Field(
        proto.STRING,
        number=1,
    )
    old_source_ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    new_source_ip: str = proto.Field(
        proto.STRING,
        number=3,
    )
    old_destination_ip: str = proto.Field(
        proto.STRING,
        number=4,
    )
    new_destination_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    old_source_port: int = proto.Field(
        proto.INT32,
        number=6,
    )
    new_source_port: int = proto.Field(
        proto.INT32,
        number=7,
    )
    old_destination_port: int = proto.Field(
        proto.INT32,
        number=8,
    )
    new_destination_port: int = proto.Field(
        proto.INT32,
        number=9,
    )
    subnet_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=11,
    )


class LoadBalancerBackendInfo(proto.Message):
    r"""For display only. Metadata associated with the load balancer
    backend.

    Attributes:
        name (str):
            Display name of the backend. For example, it
            might be an instance name for the instance group
            backends, or an IP address and port for zonal
            network endpoint group backends.
        instance_uri (str):
            URI of the backend instance (if applicable).
            Populated for instance group backends, and zonal
            NEG backends.
        backend_service_uri (str):
            URI of the backend service this backend
            belongs to (if applicable).
        instance_group_uri (str):
            URI of the instance group this backend
            belongs to (if applicable).
        network_endpoint_group_uri (str):
            URI of the network endpoint group this
            backend belongs to (if applicable).
        backend_bucket_uri (str):
            URI of the backend bucket this backend
            targets (if applicable).
        psc_service_attachment_uri (str):
            URI of the PSC service attachment this PSC
            NEG backend targets (if applicable).
        psc_google_api_target (str):
            PSC Google API target this PSC NEG backend
            targets (if applicable).
        health_check_uri (str):
            URI of the health check attached to this
            backend (if applicable).
        health_check_firewalls_config_state (google.cloud.network_management_v1.types.LoadBalancerBackendInfo.HealthCheckFirewallsConfigState):
            Output only. Health check firewalls
            configuration state for the backend. This is a
            result of the static firewall analysis
            (verifying that health check traffic from
            required IP ranges to the backend is allowed or
            not). The backend might still be unhealthy even
            if these firewalls are configured. Please refer
            to the documentation for more information:

            https://cloud.google.com/load-balancing/docs/firewall-rules
    """

    class HealthCheckFirewallsConfigState(proto.Enum):
        r"""Health check firewalls configuration state enum.

        Values:
            HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED (0):
                Configuration state unspecified. It usually
                means that the backend has no health check
                attached, or there was an unexpected
                configuration error preventing Connectivity
                tests from verifying health check configuration.
            FIREWALLS_CONFIGURED (1):
                Firewall rules (policies) allowing health
                check traffic from all required IP ranges to the
                backend are configured.
            FIREWALLS_PARTIALLY_CONFIGURED (2):
                Firewall rules (policies) allow health check
                traffic only from a part of required IP ranges.
            FIREWALLS_NOT_CONFIGURED (3):
                Firewall rules (policies) deny health check
                traffic from all required IP ranges to the
                backend.
            FIREWALLS_UNSUPPORTED (4):
                The network contains firewall rules of
                unsupported types, so Connectivity tests were
                not able to verify health check configuration
                status. Please refer to the documentation for
                the list of unsupported configurations:

                https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#unsupported-configs
        """

        HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED = 0
        FIREWALLS_CONFIGURED = 1
        FIREWALLS_PARTIALLY_CONFIGURED = 2
        FIREWALLS_NOT_CONFIGURED = 3
        FIREWALLS_UNSUPPORTED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backend_service_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_group_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network_endpoint_group_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    backend_bucket_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )
    psc_service_attachment_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    psc_google_api_target: str = proto.Field(
        proto.STRING,
        number=10,
    )
    health_check_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    health_check_firewalls_config_state: HealthCheckFirewallsConfigState = proto.Field(
        proto.ENUM,
        number=7,
        enum=HealthCheckFirewallsConfigState,
    )


class StorageBucketInfo(proto.Message):
    r"""For display only. Metadata associated with Storage Bucket.

    Attributes:
        bucket (str):
            Cloud Storage Bucket name.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ServerlessNegInfo(proto.Message):
    r"""For display only. Metadata associated with the serverless
    network endpoint group backend.

    Attributes:
        neg_uri (str):
            URI of the serverless network endpoint group.
    """

    neg_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NgfwPacketInspectionInfo(proto.Message):
    r"""For display only. Metadata associated with a layer 7 packet
    inspection by the firewall.

    Attributes:
        security_profile_group_uri (str):
            URI of the security profile group associated
            with this firewall packet inspection.
    """

    security_profile_group_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PrivateConnectionInfo(proto.Message):
    r"""For display only. Metadata associated with a Private
    Connection.

    Attributes:
        uri (str):
            URI of the Private Connection in format
            "projects/{project_id}/locations/{location}/privateConnections/{private_connection_id}".
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
