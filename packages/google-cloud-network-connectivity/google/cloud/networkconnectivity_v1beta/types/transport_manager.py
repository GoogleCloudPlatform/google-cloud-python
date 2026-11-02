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
    package="google.cloud.networkconnectivity.v1beta",
    manifest={
        "RemoteTransportProfile",
        "ListRemoteTransportProfilesRequest",
        "ListRemoteTransportProfilesResponse",
        "GetRemoteTransportProfileRequest",
        "ParseFromActivationKeyRequest",
        "ParseFromActivationKeyResponse",
        "Transport",
        "ListTransportsRequest",
        "ListTransportsResponse",
        "GetTransportRequest",
        "GetStatusRequest",
        "GetStatusResponse",
        "CreateTransportRequest",
        "UpdateTransportRequest",
        "DeleteTransportRequest",
    },
)


class RemoteTransportProfile(proto.Message):
    r"""Message describing RemoteTransportProfile object.

    Attributes:
        name (str):
            Identifier. Name of the resource in the
            format of $provider-$site.
        labels (MutableMapping[str, str]):
            Output only. Labels as key value pairs.
        description (str):
            Output only. Description of the profile.
        provider (str):
            Output only. Name of the provider on the
            other end of this profile. E.g. “Amazon Web
            Services” or “Microsoft Azure”.
        provider_site (str):
            Output only. If the profile is a Cloud
            Service Provider with compute resources, this is
            populated with the region where connectivity is
            being established. If the profile provides
            facility-level selection, this is an identity of
            the facility any connections on this profile are
            going through.
        supported_bandwidths (MutableSequence[google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile.Bandwidth]):
            Output only. List of bandwidth enum values
            that are supported by this profile.
        sla (google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile.ServiceLevelAvailability):
            Output only. Availability class that will be
            configured for this particular
            RemoteTransportProfile.
        flow (google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile.KeyProvisioningFlow):
            Output only. Type of provisioning flows
            supported by this profile.
        order_state (google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile.State):
            Output only. Order state for this profile.
        display_name (str):
            Output only. Human readable name of this
            profile, used to identify this profile in the
            UI.
        provider_type (google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile.ProviderType):
            Output only. Provider type for this profile.
    """

    class Bandwidth(proto.Enum):
        r"""Bandwidth values that may be supported for a specific
        profile.

        Values:
            BANDWIDTH_UNSPECIFIED (0):
                Unspecified bandwidth.
            BPS_50M (1):
                50 Megabits per second.
            BPS_100M (2):
                100 Megabits per second.
            BPS_200M (3):
                200 Megabits per second.
            BPS_300M (4):
                300 Megabits per second.
            BPS_400M (5):
                400 Megabits per second.
            BPS_500M (6):
                500 Megabits per second.
            BPS_1G (7):
                1 Gigabit per second.
            BPS_2G (8):
                2 Gigabits per second.
            BPS_5G (9):
                5 Gigabits per second.
            BPS_10G (10):
                10 Gigabits per second.
            BPS_20G (11):
                20 Gigabits per second.
            BPS_50G (12):
                50 Gigabits per second.
            BPS_100G (13):
                100 Gigabits per second.
        """

        BANDWIDTH_UNSPECIFIED = 0
        BPS_50M = 1
        BPS_100M = 2
        BPS_200M = 3
        BPS_300M = 4
        BPS_400M = 5
        BPS_500M = 6
        BPS_1G = 7
        BPS_2G = 8
        BPS_5G = 9
        BPS_10G = 10
        BPS_20G = 11
        BPS_50G = 12
        BPS_100G = 13

    class ServiceLevelAvailability(proto.Enum):
        r"""Availability class options.

        Values:
            SERVICE_LEVEL_AVAILABILITY_UNSPECIFIED (0):
                Unspecified service level availability.
            HIGH (1):
                This represents a 99.9% service level on the
                availability of the configured connectivity.
            MAXIMUM (2):
                This represents a 99.99% service level on the
                availability of the configured connectivity.
        """

        SERVICE_LEVEL_AVAILABILITY_UNSPECIFIED = 0
        HIGH = 1
        MAXIMUM = 2

    class KeyProvisioningFlow(proto.Enum):
        r"""Type of provisioning flows supported.

        Values:
            KEY_PROVISIONING_FLOW_UNSPECIFIED (0):
                Unspecified key provisioning flow.
            INPUT_ONLY (1):
                The activationKey field on the Transport must
                be included in a create or patch request to
                establish connectivity.
            OUTPUT_ONLY (2):
                The generatedActivationKey field is populated
                and must be read from the resource and passed
                into the other provider.
            INPUT_OR_OUTPUT (3):
                Both activation key fields are allowed for
                establishing connectivity. If a key is input,
                the generated key is still present after
                provisioning is finished.
        """

        KEY_PROVISIONING_FLOW_UNSPECIFIED = 0
        INPUT_ONLY = 1
        OUTPUT_ONLY = 2
        INPUT_OR_OUTPUT = 3

    class State(proto.Enum):
        r"""State of the RemoteTransportProfile.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CLOSED (1):
                Not enough capacity for customers to order.
            OPEN (2):
                Enough capacity to fulfill an order.
        """

        STATE_UNSPECIFIED = 0
        CLOSED = 1
        OPEN = 2

    class ProviderType(proto.Enum):
        r"""Provider type for this profile.

        Values:
            PROVIDER_TYPE_UNSPECIFIED (0):
                Unspecified provider type.
            CLOUD (1):
                Represents a Cloud service provider.
            NETWORK (2):
                Represents a Network service provider.
        """

        PROVIDER_TYPE_UNSPECIFIED = 0
        CLOUD = 1
        NETWORK = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=7,
    )
    provider_site: str = proto.Field(
        proto.STRING,
        number=8,
    )
    supported_bandwidths: MutableSequence[Bandwidth] = proto.RepeatedField(
        proto.ENUM,
        number=9,
        enum=Bandwidth,
    )
    sla: ServiceLevelAvailability = proto.Field(
        proto.ENUM,
        number=10,
        enum=ServiceLevelAvailability,
    )
    flow: KeyProvisioningFlow = proto.Field(
        proto.ENUM,
        number=11,
        enum=KeyProvisioningFlow,
    )
    order_state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    provider_type: ProviderType = proto.Field(
        proto.ENUM,
        number=14,
        enum=ProviderType,
    )


class ListRemoteTransportProfilesRequest(proto.Message):
    r"""Message for requesting list of RemoteTransportProfiles.

    Attributes:
        parent (str):
            Required. Parent value for
            ListRemoteTransportProfilesRequest.
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
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListRemoteTransportProfilesResponse(proto.Message):
    r"""Message for response to listing RemoteTransportProfiles

    Attributes:
        remote_transport_profiles (MutableSequence[google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile]):
            The list of RemoteTransportProfiles.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    remote_transport_profiles: MutableSequence["RemoteTransportProfile"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RemoteTransportProfile",
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


class GetRemoteTransportProfileRequest(proto.Message):
    r"""Message for getting a RemoteTransportProfile.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ParseFromActivationKeyRequest(proto.Message):
    r"""Message for getting a RemoteTransportProfile from an
    activation key.

    Attributes:
        parent (str):
            Required. Parent value for
            ParseFromActivationKeyRequest.
        activation_key (str):
            Required. The activation key to get the
            RemoteTransportProfile for.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    activation_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ParseFromActivationKeyResponse(proto.Message):
    r"""Message for response to getting a RemoteTransportProfile from
    an activation key.

    Attributes:
        remote_transport_profile (google.cloud.networkconnectivity_v1beta.types.RemoteTransportProfile):
            The RemoteTransportProfile that was parsed
            from the activation key.
    """

    remote_transport_profile: "RemoteTransportProfile" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RemoteTransportProfile",
    )


class Transport(proto.Message):
    r"""Message describing Transport object.

    Attributes:
        name (str):
            Identifier. Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        description (str):
            Optional. Description of the Transport.
        remote_profile (str):
            Optional. Immutable. Name of the
            remoteTransportProfile that this Transport is
            connecting to.
        provided_activation_key (str):
            Optional. Immutable. Key used for establishing a connection
            with the remote transport. This key can only be provided if
            the profile supports an INPUT key flow and the resource is
            in the PENDING_KEY state.
        generated_activation_key (str):
            Output only. Google-generated activation key. This is only
            output if the selected profile supports an OUTPUT key flow.
            Inputting this to the provider is only valid while the
            resource is in a PENDING_KEY state. Once the provider has
            accepted the key, the resource will move to the CONFIGURING
            state.
        bandwidth (google.cloud.networkconnectivity_v1beta.types.Transport.Bandwidth):
            Optional. Bandwidth of the Transport. This
            must be one of the supported bandwidths for the
            remote profile, and must be set when no
            activation key is being provided.
        stack_type (google.cloud.networkconnectivity_v1beta.types.Transport.StackType):
            Optional. IP version stack for the
            established connectivity.
        state (google.cloud.networkconnectivity_v1beta.types.Transport.State):
            Output only. State of the underlying
            connectivity.
        mtu_limit (int):
            Output only. The maximum transmission unit
            (MTU) of a packet that can be sent over this
            transport.
        admin_enabled (bool):
            Optional. Administrative state of the
            underlying connectivity. If set to true
            (default), connectivity should be available
            between your environments. If set to false, the
            connectivity over these links is disabled.
            Disabling your Transport does not affect
            billing, and retains the underlying network
            bandwidth associated with the connectivity.
        network (str):
            Optional. Immutable. Resource URI of the
            Network that will be peered with this Transport.
            This field must be provided during resource
            creation and cannot be changed.
        advertised_routes (MutableSequence[str]):
            Optional. List of IP Prefixes that will be
            advertised to the remote provider. Both IPv4 and
            IPv6 addresses are supported.
        remote_account_id (str):
            Optional. Immutable. The user supplied
            account id for the CSP associated with the
            remote profile.
        peering_network (str):
            Output only. VPC Network URI that was created for the VPC
            Peering connection to the provided ``network``. If VPC
            Peering is disconnected, this can be used to re-establish.
        hub (str):
            Optional. Immutable. The NCC Hub that the Transport should
            attach to. The hub must be in the same project as the
            Transport. Format: ``{hub}`` or
            ``projects/{project}/locations/global/hubs/{hub}``
        psc_routing_enabled (bool):
            Optional. Immutable. Controls whether a
            Routing VPC Spoke should be created and attached
            to the NCC Hub. This will provide Private
            Service Connect (PSC) connectivity through NCC.
            This can only be set when the Transport is first
            created.
        auto_accept (bool):
            Optional. Immutable. Controls whether
            resources proposed by the Transport are
            automatically accepted on behalf of the user.
            List of actions that can be automatically
            accepted are:

            1. VPC Peering creation
            2. Routing VPC Spoke creation
            3. Hybrid Spoke creation
    """

    class Bandwidth(proto.Enum):
        r"""Supported bandwidth options.

        Values:
            BANDWIDTH_UNSPECIFIED (0):
                Unspecified bandwidth.
            BPS_50M (1):
                50 Megabits per second.
            BPS_100M (2):
                100 Megabits per second.
            BPS_200M (3):
                200 Megabits per second.
            BPS_300M (4):
                300 Megabits per second.
            BPS_400M (5):
                400 Megabits per second.
            BPS_500M (6):
                500 Megabits per second.
            BPS_1G (7):
                1 Gigabit per second.
            BPS_2G (8):
                2 Gigabits per second.
            BPS_5G (9):
                5 Gigabits per second.
            BPS_10G (10):
                10 Gigabits per second.
            BPS_20G (11):
                20 Gigabits per second.
            BPS_50G (12):
                50 Gigabits per second.
            BPS_100G (13):
                100 Gigabits per second.
        """

        BANDWIDTH_UNSPECIFIED = 0
        BPS_50M = 1
        BPS_100M = 2
        BPS_200M = 3
        BPS_300M = 4
        BPS_400M = 5
        BPS_500M = 6
        BPS_1G = 7
        BPS_2G = 8
        BPS_5G = 9
        BPS_10G = 10
        BPS_20G = 11
        BPS_50G = 12
        BPS_100G = 13

    class StackType(proto.Enum):
        r"""IP version stack for the established connectivity.

        Values:
            STACK_TYPE_UNSPECIFIED (0):
                Unspecified stack type.
            IPV4_ONLY (1):
                Only IPv4 is supported. (default)
            IPV4_IPV6 (2):
                Both IPv4 and IPv6 are supported.
        """

        STACK_TYPE_UNSPECIFIED = 0
        IPV4_ONLY = 1
        IPV4_IPV6 = 2

    class State(proto.Enum):
        r"""Represents the status of the underlying connectivity. One of
        the following states, depending on who has initiated the
        Transport request.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                The resource exists locally and is being
                created / associated with the resource on the
                remote provider’s end of the underlying
                connectivity.
            PENDING_CONFIG (2):
                The Transport exists on both sides of the
                connection, and is waiting for configuration to
                finalize and be verified as operational.
            PENDING_KEY (3):
                The Transport was created in GCP. Depending
                on the profile’s key provisioning flow, this is
                either waiting for an activation key to be input
                (the key will be validated that it uses remote
                resources that match the Transport), or for the
                generated key to be input to the provider for
                finalizing. The configured bandwidth is not yet
                guaranteed.
            ACTIVE (4):
                The Transport is configured and the
                underlying connectivity is considered
                operational.
            DELETING (5):
                The Transport is being deleted from GCP. The
                underlying connectivity is no longer
                operational.
            DEPROVISIONED (6):
                The Transport was deleted on the remote provider's end and
                is no longer operational. GCP has insufficient information
                to move the resource back to PENDING_KEY state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        PENDING_CONFIG = 2
        PENDING_KEY = 3
        ACTIVE = 4
        DELETING = 5
        DEPROVISIONED = 6

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
        number=6,
    )
    remote_profile: str = proto.Field(
        proto.STRING,
        number=7,
    )
    provided_activation_key: str = proto.Field(
        proto.STRING,
        number=8,
    )
    generated_activation_key: str = proto.Field(
        proto.STRING,
        number=9,
    )
    bandwidth: Bandwidth = proto.Field(
        proto.ENUM,
        number=10,
        enum=Bandwidth,
    )
    stack_type: StackType = proto.Field(
        proto.ENUM,
        number=11,
        enum=StackType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )
    mtu_limit: int = proto.Field(
        proto.INT32,
        number=13,
    )
    admin_enabled: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    network: str = proto.Field(
        proto.STRING,
        number=15,
    )
    advertised_routes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    remote_account_id: str = proto.Field(
        proto.STRING,
        number=17,
    )
    peering_network: str = proto.Field(
        proto.STRING,
        number=18,
    )
    hub: str = proto.Field(
        proto.STRING,
        number=19,
    )
    psc_routing_enabled: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    auto_accept: bool = proto.Field(
        proto.BOOL,
        number=21,
    )


class ListTransportsRequest(proto.Message):
    r"""Message for requesting list of Transports.

    Attributes:
        parent (str):
            Required. Parent value for
            ListTransportsRequest.
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
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListTransportsResponse(proto.Message):
    r"""Message for response to listing Transports.

    Attributes:
        transports (MutableSequence[google.cloud.networkconnectivity_v1beta.types.Transport]):
            The list of Transport.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    transports: MutableSequence["Transport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Transport",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTransportRequest(proto.Message):
    r"""Message for getting a Transport.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetStatusRequest(proto.Message):
    r"""Message for getting a Transport's operational status.

    Attributes:
        name (str):
            Required. Name of the resource.
        skip_cache (bool):
            Optional. If set to true, the response will
            bypass any caches and return the freshest
            possible data.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skip_cache: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class GetStatusResponse(proto.Message):
    r"""Message for the response to getting a Transport's operational
    status.

    Attributes:
        overall_status (google.cloud.networkconnectivity_v1beta.types.GetStatusResponse.OverallStatus):
            The overall status of the Transport. This
            field will always output the most critical
            status of the Transport. For example, if the
            connectivity is DISCONNECTED, and the underlying
            networking components are DOWN, then the overall
            status will be DOWN.
        operational_status (google.cloud.networkconnectivity_v1beta.types.GetStatusResponse.OperationalStatus):
            The operational status of the underlying
            networking components.
        connectivity_status (google.cloud.networkconnectivity_v1beta.types.GetStatusResponse.ConnectivityStatus):
            Current status of connectivity to the local
            GCP resource. This reflects whether the VPC
            Peering or NCC Hub appears correctly configured.
        mac_sec_status (google.cloud.networkconnectivity_v1beta.types.GetStatusResponse.MacSecStatus):
            Current status of MACSec on the underlying
            network connectivity between GC and the partner.
    """

    class OverallStatus(proto.Enum):
        r"""The overall status of the Transport.

        Values:
            OVERALL_STATUS_UNSPECIFIED (0):
                Unspecified status.
            ACTIVE (1):
                Resource is active and operational.
            PENDING_KEY (2):
                Resource is waiting for an activation key to
                be exchanged.
            CONFIGURING (3):
                Activation keys have been exchanged and
                connectivity is being established.
            DISCONNECTED (4):
                VPC Peering has been taken down, or the NCC
                Spoke has been rejected.
            DOWN (5):
                User configuration is correct, but the
                configured capacity is operationally down.
        """

        OVERALL_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        PENDING_KEY = 2
        CONFIGURING = 3
        DISCONNECTED = 4
        DOWN = 5

    class OperationalStatus(proto.Enum):
        r"""The operational status of the underlying networking
        components.

        Values:
            OPERATIONAL_STATUS_UNSPECIFIED (0):
                Unspecified status.
            OPERATIONAL_STATUS_ACTIVE (1):
                Protected capacity is available and
                networking components show as up.
            OPERATIONAL_STATUS_DOWN (2):
                Protected capacity is showing as
                operationally down.
        """

        OPERATIONAL_STATUS_UNSPECIFIED = 0
        OPERATIONAL_STATUS_ACTIVE = 1
        OPERATIONAL_STATUS_DOWN = 2

    class ConnectivityStatus(proto.Enum):
        r"""Current status of connectivity to the local GCP resource.
        This reflects whether the VPC Peering or NCC Hub appears
        correctly configured.

        Values:
            CONNECTIVITY_STATUS_UNSPECIFIED (0):
                Unspecified status.
            CONNECTIVITY_STATUS_CONNECTED (1):
                VPC Peering or the NCC Hub appear to be
                correctly established.
            CONNECTIVITY_STATUS_DISCONNECTED (2):
                VPC Peering has been taken down, or the NCC
                Spoke has been rejected.
        """

        CONNECTIVITY_STATUS_UNSPECIFIED = 0
        CONNECTIVITY_STATUS_CONNECTED = 1
        CONNECTIVITY_STATUS_DISCONNECTED = 2

    class MacSecStatus(proto.Enum):
        r"""Current status of MACSec on the underlying network
        connectivity between GC and the partner.

        Values:
            MAC_SEC_STATUS_UNSPECIFIED (0):
                Unspecified status.
            MAC_SEC_STATUS_ACTIVE_FAIL_CLOSED (1):
                MACSec is protecting the links and configured
                in fail closed.
            MAC_SEC_STATUS_ACTIVE_FAIL_OPEN (2):
                MACSec is protecting the links and configured
                to fail open on at least one of the redundant
                links.
            MAC_SEC_STATUS_NOT_CONFIGURED (3):
                MACSec is not configured on at least one of
                the underlying links.
        """

        MAC_SEC_STATUS_UNSPECIFIED = 0
        MAC_SEC_STATUS_ACTIVE_FAIL_CLOSED = 1
        MAC_SEC_STATUS_ACTIVE_FAIL_OPEN = 2
        MAC_SEC_STATUS_NOT_CONFIGURED = 3

    overall_status: OverallStatus = proto.Field(
        proto.ENUM,
        number=1,
        enum=OverallStatus,
    )
    operational_status: OperationalStatus = proto.Field(
        proto.ENUM,
        number=2,
        enum=OperationalStatus,
    )
    connectivity_status: ConnectivityStatus = proto.Field(
        proto.ENUM,
        number=3,
        enum=ConnectivityStatus,
    )
    mac_sec_status: MacSecStatus = proto.Field(
        proto.ENUM,
        number=4,
        enum=MacSecStatus,
    )


class CreateTransportRequest(proto.Message):
    r"""Message for creating a Transport

    Attributes:
        parent (str):
            Required. Value for parent.
        transport_id (str):
            Required. Id of the requesting object
        transport (google.cloud.networkconnectivity_v1beta.types.Transport):
            Required. The resource being created
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
    transport_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    transport: "Transport" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Transport",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateTransportRequest(proto.Message):
    r"""Message for updating a Transport.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Transport resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields present in the request will be overwritten.
        transport (google.cloud.networkconnectivity_v1beta.types.Transport):
            Required. The resource being updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    transport: "Transport" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Transport",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTransportRequest(proto.Message):
    r"""Message for deleting a Transport.

    Attributes:
        name (str):
            Required. Name of the resource.
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


__all__ = tuple(sorted(__protobuf__.manifest))
