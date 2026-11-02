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
import proto  # type: ignore

from google.cloud.notebooks_v2.types import gce_setup as gcn_gce_setup

__protobuf__ = proto.module(
    package="google.cloud.notebooks.v2",
    manifest={
        "State",
        "HealthState",
        "UpgradeHistoryEntry",
        "Instance",
    },
)


class State(proto.Enum):
    r"""The definition of the states of this instance.

    Values:
        STATE_UNSPECIFIED (0):
            State is not specified.
        STARTING (1):
            The control logic is starting the instance.
        PROVISIONING (2):
            The control logic is installing required
            frameworks and registering the instance with
            notebook proxy
        ACTIVE (3):
            The instance is running.
        STOPPING (4):
            The control logic is stopping the instance.
        STOPPED (5):
            The instance is stopped.
        DELETED (6):
            The instance is deleted.
        UPGRADING (7):
            The instance is upgrading.
        INITIALIZING (8):
            The instance is being created.
        SUSPENDING (9):
            The instance is suspending.
        SUSPENDED (10):
            The instance is suspended.
    """

    STATE_UNSPECIFIED = 0
    STARTING = 1
    PROVISIONING = 2
    ACTIVE = 3
    STOPPING = 4
    STOPPED = 5
    DELETED = 6
    UPGRADING = 7
    INITIALIZING = 8
    SUSPENDING = 9
    SUSPENDED = 10


class HealthState(proto.Enum):
    r"""The instance health state.

    Values:
        HEALTH_STATE_UNSPECIFIED (0):
            The instance substate is unknown.
        HEALTHY (1):
            The instance is known to be in an healthy
            state (for example, critical daemons are
            running) Applies to ACTIVE state.
        UNHEALTHY (2):
            The instance is known to be in an unhealthy
            state (for example, critical daemons are not
            running) Applies to ACTIVE state.
        AGENT_NOT_INSTALLED (3):
            The instance has not installed health
            monitoring agent. Applies to ACTIVE state.
        AGENT_NOT_RUNNING (4):
            The instance health monitoring agent is not
            running. Applies to ACTIVE state.
    """

    HEALTH_STATE_UNSPECIFIED = 0
    HEALTHY = 1
    UNHEALTHY = 2
    AGENT_NOT_INSTALLED = 3
    AGENT_NOT_RUNNING = 4


class UpgradeHistoryEntry(proto.Message):
    r"""The entry of VM image upgrade history.

    Attributes:
        snapshot (str):
            Optional. The snapshot of the boot disk of
            this notebook instance before upgrade.
        vm_image (str):
            Optional. The VM image before this instance
            upgrade.
        container_image (str):
            Optional. The container image before this
            instance upgrade.
        framework (str):
            Optional. The framework of this notebook
            instance.
        version (str):
            Optional. The version of the notebook
            instance before this upgrade.
        state (google.cloud.notebooks_v2.types.UpgradeHistoryEntry.State):
            Output only. The state of this instance
            upgrade history entry.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Immutable. The time that this instance
            upgrade history entry is created.
        action (google.cloud.notebooks_v2.types.UpgradeHistoryEntry.Action):
            Optional. Action. Rolloback or Upgrade.
        target_version (str):
            Optional. Target VM Version, like m63.
    """

    class State(proto.Enum):
        r"""The definition of the states of this upgrade history entry.

        Values:
            STATE_UNSPECIFIED (0):
                State is not specified.
            STARTED (1):
                The instance upgrade is started.
            SUCCEEDED (2):
                The instance upgrade is succeeded.
            FAILED (3):
                The instance upgrade is failed.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        SUCCEEDED = 2
        FAILED = 3

    class Action(proto.Enum):
        r"""The definition of operations of this upgrade history entry.

        Values:
            ACTION_UNSPECIFIED (0):
                Operation is not specified.
            UPGRADE (1):
                Upgrade.
            ROLLBACK (2):
                Rollback.
        """

        ACTION_UNSPECIFIED = 0
        UPGRADE = 1
        ROLLBACK = 2

    snapshot: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_image: str = proto.Field(
        proto.STRING,
        number=2,
    )
    container_image: str = proto.Field(
        proto.STRING,
        number=3,
    )
    framework: str = proto.Field(
        proto.STRING,
        number=4,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=8,
        enum=Action,
    )
    target_version: str = proto.Field(
        proto.STRING,
        number=9,
    )


class Instance(proto.Message):
    r"""The definition of a notebook instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of this notebook instance. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        gce_setup (google.cloud.notebooks_v2.types.GceSetup):
            Optional. Compute Engine setup for the
            notebook. Uses notebook-defined fields.

            This field is a member of `oneof`_ ``infrastructure``.
        proxy_uri (str):
            Output only. The proxy endpoint that is used
            to access the Jupyter notebook.
        instance_owners (MutableSequence[str]):
            Optional. Input only. The owner of this instance after
            creation. Format: ``alias@example.com``

            Currently supports one owner only. If not specified, all of
            the service account users of your VM instance's service
            account can use the instance.
        creator (str):
            Output only. Email address of entity that
            sent original CreateInstance request.
        state (google.cloud.notebooks_v2.types.State):
            Output only. The state of this instance.
        upgrade_history (MutableSequence[google.cloud.notebooks_v2.types.UpgradeHistoryEntry]):
            Output only. The upgrade history of this
            instance.
        id (str):
            Output only. Unique ID of the resource.
        health_state (google.cloud.notebooks_v2.types.HealthState):
            Output only. Instance health_state.
        health_info (MutableMapping[str, str]):
            Output only. Additional information about instance health.
            Example:

            ::

                healthInfo": {
                  "docker_proxy_agent_status": "1",
                  "docker_status": "1",
                  "jupyterlab_api_status": "-1",
                  "jupyterlab_status": "-1",
                  "updated": "2020-10-18 09:40:03.573409"
                }
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Instance creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Instance update time.
        disable_proxy_access (bool):
            Optional. If true, the notebook instance will
            not register with the proxy.
        labels (MutableMapping[str, str]):
            Optional. Labels to apply to this instance.
            These can be later modified by the
            UpdateInstance method.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gce_setup: gcn_gce_setup.GceSetup = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="infrastructure",
        message=gcn_gce_setup.GceSetup,
    )
    proxy_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_owners: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=6,
        enum="State",
    )
    upgrade_history: MutableSequence["UpgradeHistoryEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="UpgradeHistoryEntry",
    )
    id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    health_state: "HealthState" = proto.Field(
        proto.ENUM,
        number=9,
        enum="HealthState",
    )
    health_info: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
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
    disable_proxy_access: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
