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

from google.cloud.bare_metal_solution_v2.types import common, network, volume
from google.cloud.bare_metal_solution_v2.types import lun as gcb_lun

__protobuf__ = proto.module(
    package="google.cloud.baremetalsolution.v2",
    manifest={
        "Instance",
        "GetInstanceRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "UpdateInstanceRequest",
        "RenameInstanceRequest",
        "ResetInstanceRequest",
        "StartInstanceRequest",
        "StartInstanceResponse",
        "StopInstanceRequest",
        "StopInstanceResponse",
        "EnableInteractiveSerialConsoleRequest",
        "EnableInteractiveSerialConsoleResponse",
        "DisableInteractiveSerialConsoleRequest",
        "DisableInteractiveSerialConsoleResponse",
        "DetachLunRequest",
        "ServerNetworkTemplate",
    },
)


class Instance(proto.Message):
    r"""A server.

    Attributes:
        name (str):
            Immutable. The resource name of this ``Instance``. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        id (str):
            Output only. An identifier for the ``Instance``, generated
            by the backend.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create a time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update a time stamp.
        machine_type (str):
            Immutable. The server type. `Available server
            types <https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations>`__
        state (google.cloud.bare_metal_solution_v2.types.Instance.State):
            Output only. The state of the server.
        hyperthreading_enabled (bool):
            True if you enable hyperthreading for the
            server, otherwise false. The default value is
            false.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        luns (MutableSequence[google.cloud.bare_metal_solution_v2.types.Lun]):
            Immutable. List of LUNs associated with this
            server.
        volumes (MutableSequence[google.cloud.bare_metal_solution_v2.types.Volume]):
            Input only. List of Volumes to attach to this
            Instance on creation. This field won't be
            populated in Get/List responses.
        networks (MutableSequence[google.cloud.bare_metal_solution_v2.types.Network]):
            Output only. List of networks associated with
            this server.
        interactive_serial_console_enabled (bool):
            Output only. True if the interactive serial
            console feature is enabled for the instance,
            false otherwise. The default value is false.
        os_image (str):
            The OS image currently installed on the
            server.
        pod (str):
            Immutable. Pod name.
            Pod is an independent part of infrastructure.
            Instance can be connected to the assets
            (networks, volumes) allocated in the same pod
            only.
        network_template (str):
            Instance network template name. For eg, bondaa-bondaa,
            bondab-nic, etc. Generally, the template name follows the
            syntax of "bond<bond_mode>" or "nic".
        logical_interfaces (MutableSequence[google.cloud.bare_metal_solution_v2.types.LogicalInterface]):
            List of logical interfaces for the instance. The number of
            logical interfaces will be the same as number of hardware
            bond/nic on the chosen network template. For the
            non-multivlan configurations (for eg, existing servers) that
            use existing default network template (bondaa-bondaa), both
            the Instance.networks field and the
            Instance.logical_interfaces fields will be filled to ensure
            backward compatibility. For the others, only
            Instance.logical_interfaces will be filled.
        login_info (str):
            Output only. Text field about info for
            logging in.
        workload_profile (google.cloud.bare_metal_solution_v2.types.WorkloadProfile):
            The workload profile for the instance.
        firmware_version (str):
            Output only. The firmware version for the
            instance.
    """

    class State(proto.Enum):
        r"""The possible states for this server.

        Values:
            STATE_UNSPECIFIED (0):
                The server is in an unknown state.
            PROVISIONING (1):
                The server is being provisioned.
            RUNNING (2):
                The server is running.
            DELETED (3):
                The server has been deleted.
            UPDATING (4):
                The server is being updated.
            STARTING (5):
                The server is starting.
            STOPPING (6):
                The server is stopping.
            SHUTDOWN (7):
                The server is shutdown.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        DELETED = 3
        UPDATING = 4
        STARTING = 5
        STOPPING = 6
        SHUTDOWN = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=11,
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
    machine_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    hyperthreading_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    luns: MutableSequence[gcb_lun.Lun] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=gcb_lun.Lun,
    )
    volumes: MutableSequence[volume.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message=volume.Volume,
    )
    networks: MutableSequence[network.Network] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=network.Network,
    )
    interactive_serial_console_enabled: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    os_image: str = proto.Field(
        proto.STRING,
        number=12,
    )
    pod: str = proto.Field(
        proto.STRING,
        number=13,
    )
    network_template: str = proto.Field(
        proto.STRING,
        number=14,
    )
    logical_interfaces: MutableSequence[network.LogicalInterface] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=network.LogicalInterface,
    )
    login_info: str = proto.Field(
        proto.STRING,
        number=17,
    )
    workload_profile: common.WorkloadProfile = proto.Field(
        proto.ENUM,
        number=18,
        enum=common.WorkloadProfile,
    )
    firmware_version: str = proto.Field(
        proto.STRING,
        number=19,
    )


class GetInstanceRequest(proto.Message):
    r"""Message for requesting server information.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListInstancesRequest(proto.Message):
    r"""Message for requesting the list of servers.

    Attributes:
        parent (str):
            Required. Parent value for
            ListInstancesRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results from
            the server.
        filter (str):
            List filter.
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


class ListInstancesResponse(proto.Message):
    r"""Response message for the list of servers.

    Attributes:
        instances (MutableSequence[google.cloud.bare_metal_solution_v2.types.Instance]):
            The list of servers.
        next_page_token (str):
            A token identifying a page of results from
            the server.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Message requesting to updating a server.

    Attributes:
        instance (google.cloud.bare_metal_solution_v2.types.Instance):
            Required. The server to update.

            The ``name`` field is used to identify the instance to
            update. Format:
            projects/{project}/locations/{location}/instances/{instance}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. The currently supported fields
            are: ``labels`` ``hyperthreading_enabled`` ``os_image``
    """

    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class RenameInstanceRequest(proto.Message):
    r"""Message requesting rename of a server.

    Attributes:
        name (str):
            Required. The ``name`` field is used to identify the
            instance. Format:
            projects/{project}/locations/{location}/instances/{instance}
        new_instance_id (str):
            Required. The new ``id`` of the instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ResetInstanceRequest(proto.Message):
    r"""Message requesting to reset a server.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartInstanceRequest(proto.Message):
    r"""Message requesting to start a server.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartInstanceResponse(proto.Message):
    r"""Response message from starting a server."""


class StopInstanceRequest(proto.Message):
    r"""Message requesting to stop a server.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StopInstanceResponse(proto.Message):
    r"""Response message from stopping a server."""


class EnableInteractiveSerialConsoleRequest(proto.Message):
    r"""Message for enabling the interactive serial console on an
    instance.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EnableInteractiveSerialConsoleResponse(proto.Message):
    r"""Message for response of EnableInteractiveSerialConsole."""


class DisableInteractiveSerialConsoleRequest(proto.Message):
    r"""Message for disabling the interactive serial console on an
    instance.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DisableInteractiveSerialConsoleResponse(proto.Message):
    r"""Message for response of DisableInteractiveSerialConsole."""


class DetachLunRequest(proto.Message):
    r"""Message for detach specific LUN from an Instance.

    Attributes:
        instance (str):
            Required. Name of the instance.
        lun (str):
            Required. Name of the Lun to detach.
        skip_reboot (bool):
            If true, performs lun unmapping without
            instance reboot.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lun: str = proto.Field(
        proto.STRING,
        number=2,
    )
    skip_reboot: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ServerNetworkTemplate(proto.Message):
    r"""Network template.

    Attributes:
        name (str):
            Output only. Template's unique name. The full resource name
            follows the pattern:
            ``projects/{project}/locations/{location}/serverNetworkTemplate/{server_network_template}``
            Generally, the {server_network_template} follows the syntax
            of "bond<interface_type_index><bond_mode>" or
            "nic<interface_type_index>".
        applicable_instance_types (MutableSequence[str]):
            Instance types this template is applicable
            to.
        logical_interfaces (MutableSequence[google.cloud.bare_metal_solution_v2.types.ServerNetworkTemplate.LogicalInterface]):
            Logical interfaces.
    """

    class LogicalInterface(proto.Message):
        r"""Logical interface.

        Attributes:
            name (str):
                Interface name. This is not a globally unique identifier.
                Name is unique only inside the ServerNetworkTemplate. This
                is of syntax <interface_type_index><bond_mode> or
                <interface_type_index> and forms part of the network
                template name.
            type_ (google.cloud.bare_metal_solution_v2.types.ServerNetworkTemplate.LogicalInterface.InterfaceType):
                Interface type.
            required (bool):
                If true, interface must have network
                connected.
        """

        class InterfaceType(proto.Enum):
            r"""Interface type.

            Values:
                INTERFACE_TYPE_UNSPECIFIED (0):
                    Unspecified value.
                BOND (1):
                    Bond interface type.
                NIC (2):
                    NIC interface type.
            """

            INTERFACE_TYPE_UNSPECIFIED = 0
            BOND = 1
            NIC = 2

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "ServerNetworkTemplate.LogicalInterface.InterfaceType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ServerNetworkTemplate.LogicalInterface.InterfaceType",
        )
        required: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    applicable_instance_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    logical_interfaces: MutableSequence[LogicalInterface] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=LogicalInterface,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
