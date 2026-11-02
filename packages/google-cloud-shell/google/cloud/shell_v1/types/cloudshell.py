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

__protobuf__ = proto.module(
    package="google.cloud.shell.v1",
    manifest={
        "Environment",
        "GetEnvironmentRequest",
        "CreateEnvironmentMetadata",
        "DeleteEnvironmentMetadata",
        "StartEnvironmentRequest",
        "AuthorizeEnvironmentRequest",
        "AuthorizeEnvironmentResponse",
        "AuthorizeEnvironmentMetadata",
        "StartEnvironmentMetadata",
        "StartEnvironmentResponse",
        "AddPublicKeyRequest",
        "AddPublicKeyResponse",
        "AddPublicKeyMetadata",
        "RemovePublicKeyRequest",
        "RemovePublicKeyResponse",
        "RemovePublicKeyMetadata",
        "CloudShellErrorDetails",
    },
)


class Environment(proto.Message):
    r"""A Cloud Shell environment, which is defined as the
    combination of a Docker image specifying what is installed on
    the environment and a home directory containing the user's data
    that will remain across sessions. Each user has at least an
    environment with the ID "default".

    Attributes:
        name (str):
            Immutable. Full name of this resource, in the format
            ``users/{owner_email}/environments/{environment_id}``.
            ``{owner_email}`` is the email address of the user to whom
            this environment belongs, and ``{environment_id}`` is the
            identifier of this environment. For example,
            ``users/someone@example.com/environments/default``.
        id (str):
            Output only. The environment's identifier,
            unique among the user's environments.
        docker_image (str):
            Required. Immutable. Full path to the Docker
            image used to run this environment, e.g.
            "gcr.io/dev-con/cloud-devshell:latest".
        state (google.cloud.shell_v1.types.Environment.State):
            Output only. Current execution state of this
            environment.
        web_host (str):
            Output only. Host to which clients can
            connect to initiate HTTPS or WSS connections
            with the environment.
        ssh_username (str):
            Output only. Username that clients should use
            when initiating SSH sessions with the
            environment.
        ssh_host (str):
            Output only. Host to which clients can
            connect to initiate SSH sessions with the
            environment.
        ssh_port (int):
            Output only. Port to which clients can
            connect to initiate SSH sessions with the
            environment.
        public_keys (MutableSequence[str]):
            Output only. Public keys associated with the
            environment. Clients can connect to this
            environment via SSH only if they possess a
            private key corresponding to at least one of
            these public keys. Keys can be added to or
            removed from the environment using the
            AddPublicKey and RemovePublicKey methods.
    """

    class State(proto.Enum):
        r"""Possible execution states for an environment.

        Values:
            STATE_UNSPECIFIED (0):
                The environment's states is unknown.
            SUSPENDED (1):
                The environment is not running and can't be
                connected to. Starting the environment will
                transition it to the PENDING state.
            PENDING (2):
                The environment is being started but is not
                yet ready to accept connections.
            RUNNING (3):
                The environment is running and ready to
                accept connections. It will automatically
                transition back to DISABLED after a period of
                inactivity or if another environment is started.
            DELETING (4):
                The environment is being deleted and can't be
                connected to.
        """

        STATE_UNSPECIFIED = 0
        SUSPENDED = 1
        PENDING = 2
        RUNNING = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    docker_image: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    web_host: str = proto.Field(
        proto.STRING,
        number=12,
    )
    ssh_username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ssh_host: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ssh_port: int = proto.Field(
        proto.INT32,
        number=7,
    )
    public_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )


class GetEnvironmentRequest(proto.Message):
    r"""Request message for
    [GetEnvironment][google.cloud.shell.v1.CloudShellService.GetEnvironment].

    Attributes:
        name (str):
            Required. Name of the requested resource, for example
            ``users/me/environments/default`` or
            ``users/someone@example.com/environments/default``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEnvironmentMetadata(proto.Message):
    r"""Message included in the metadata field of operations returned from
    [CreateEnvironment][google.cloud.shell.v1.CloudShellService.CreateEnvironment].

    """


class DeleteEnvironmentMetadata(proto.Message):
    r"""Message included in the metadata field of operations returned from
    [DeleteEnvironment][google.cloud.shell.v1.CloudShellService.DeleteEnvironment].

    """


class StartEnvironmentRequest(proto.Message):
    r"""Request message for
    [StartEnvironment][google.cloud.shell.v1.CloudShellService.StartEnvironment].

    Attributes:
        name (str):
            Name of the resource that should be started, for example
            ``users/me/environments/default`` or
            ``users/someone@example.com/environments/default``.
        access_token (str):
            The initial access token passed to the
            environment. If this is present and valid, the
            environment will be pre-authenticated with
            gcloud so that the user can run gcloud commands
            in Cloud Shell without having to log in. This
            code can be updated later by calling
            AuthorizeEnvironment.
        public_keys (MutableSequence[str]):
            Public keys that should be added to the
            environment before it is started.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    public_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AuthorizeEnvironmentRequest(proto.Message):
    r"""Request message for
    [AuthorizeEnvironment][google.cloud.shell.v1.CloudShellService.AuthorizeEnvironment].

    Attributes:
        name (str):
            Name of the resource that should receive the credentials,
            for example ``users/me/environments/default`` or
            ``users/someone@example.com/environments/default``.
        access_token (str):
            The OAuth access token that should be sent to
            the environment.
        id_token (str):
            The OAuth ID token that should be sent to the
            environment.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the credentials expire. If not
            set, defaults to one hour from when the server
            received the request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    id_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class AuthorizeEnvironmentResponse(proto.Message):
    r"""Response message for
    [AuthorizeEnvironment][google.cloud.shell.v1.CloudShellService.AuthorizeEnvironment].

    """


class AuthorizeEnvironmentMetadata(proto.Message):
    r"""Message included in the metadata field of operations returned from
    [AuthorizeEnvironment][google.cloud.shell.v1.CloudShellService.AuthorizeEnvironment].

    """


class StartEnvironmentMetadata(proto.Message):
    r"""Message included in the metadata field of operations returned from
    [StartEnvironment][google.cloud.shell.v1.CloudShellService.StartEnvironment].

    Attributes:
        state (google.cloud.shell_v1.types.StartEnvironmentMetadata.State):
            Current state of the environment being
            started.
    """

    class State(proto.Enum):
        r"""Possible states an environment might transition between
        during startup. These states are not normally actionable by
        clients, but may be used to show a progress message to the user.
        An environment won't necessarily go through all of these states
        when starting. More states are likely to be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                The environment's start state is unknown.
            STARTING (1):
                The environment is in the process of being
                started, but no additional details are
                available.
            UNARCHIVING_DISK (2):
                Startup is waiting for the user's disk to be
                unarchived. This can happen when the user
                returns to Cloud Shell after not having used it
                for a while, and suggests that startup will take
                longer than normal.
            AWAITING_COMPUTE_RESOURCES (4):
                Startup is waiting for compute resources to
                be assigned to the environment. This should
                normally happen very quickly, but an environment
                might stay in this state for an extended period
                of time if the system is experiencing heavy
                load.
            FINISHED (3):
                Startup has completed. If the start operation
                was successful, the user should be able to
                establish an SSH connection to their
                environment. Otherwise, the operation will
                contain details of the failure.
        """

        STATE_UNSPECIFIED = 0
        STARTING = 1
        UNARCHIVING_DISK = 2
        AWAITING_COMPUTE_RESOURCES = 4
        FINISHED = 3

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )


class StartEnvironmentResponse(proto.Message):
    r"""Message included in the response field of operations returned from
    [StartEnvironment][google.cloud.shell.v1.CloudShellService.StartEnvironment]
    once the operation is complete.

    Attributes:
        environment (google.cloud.shell_v1.types.Environment):
            Environment that was started.
    """

    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )


class AddPublicKeyRequest(proto.Message):
    r"""Request message for
    [AddPublicKey][google.cloud.shell.v1.CloudShellService.AddPublicKey].

    Attributes:
        environment (str):
            Environment this key should be added to, e.g.
            ``users/me/environments/default``.
        key (str):
            Key that should be added to the environment. Supported
            formats are ``ssh-dss`` (see RFC4253), ``ssh-rsa`` (see
            RFC4253), ``ecdsa-sha2-nistp256`` (see RFC5656),
            ``ecdsa-sha2-nistp384`` (see RFC5656) and
            ``ecdsa-sha2-nistp521`` (see RFC5656). It should be
            structured as <format> <content>, where <content> part is
            encoded with Base64.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AddPublicKeyResponse(proto.Message):
    r"""Response message for
    [AddPublicKey][google.cloud.shell.v1.CloudShellService.AddPublicKey].

    Attributes:
        key (str):
            Key that was added to the environment.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AddPublicKeyMetadata(proto.Message):
    r"""Message included in the metadata field of operations returned from
    [AddPublicKey][google.cloud.shell.v1.CloudShellService.AddPublicKey].

    """


class RemovePublicKeyRequest(proto.Message):
    r"""Request message for
    [RemovePublicKey][google.cloud.shell.v1.CloudShellService.RemovePublicKey].

    Attributes:
        environment (str):
            Environment this key should be removed from, e.g.
            ``users/me/environments/default``.
        key (str):
            Key that should be removed from the
            environment.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemovePublicKeyResponse(proto.Message):
    r"""Response message for
    [RemovePublicKey][google.cloud.shell.v1.CloudShellService.RemovePublicKey].

    """


class RemovePublicKeyMetadata(proto.Message):
    r"""Message included in the metadata field of operations returned from
    [RemovePublicKey][google.cloud.shell.v1.CloudShellService.RemovePublicKey].

    """


class CloudShellErrorDetails(proto.Message):
    r"""Cloud-shell specific information that will be included as
    details in failure responses.

    Attributes:
        code (google.cloud.shell_v1.types.CloudShellErrorDetails.CloudShellErrorCode):
            Code indicating the specific error the
            occurred.
    """

    class CloudShellErrorCode(proto.Enum):
        r"""Set of possible errors returned from API calls.

        Values:
            CLOUD_SHELL_ERROR_CODE_UNSPECIFIED (0):
                An unknown error occurred.
            IMAGE_UNAVAILABLE (1):
                The image used by the Cloud Shell environment
                either does not exist or the user does not have
                access to it.
            CLOUD_SHELL_DISABLED (2):
                Cloud Shell has been disabled by an
                administrator for the user making the request.
            TOS_VIOLATION (4):
                Cloud Shell has been permanently disabled due
                to a Terms of Service violation by the user.
            QUOTA_EXCEEDED (5):
                The user has exhausted their weekly Cloud
                Shell quota, and Cloud Shell will be disabled
                until the quota resets.
            ENVIRONMENT_UNAVAILABLE (6):
                The Cloud Shell environment is unavailable
                and cannot be connected to at the moment.
        """

        CLOUD_SHELL_ERROR_CODE_UNSPECIFIED = 0
        IMAGE_UNAVAILABLE = 1
        CLOUD_SHELL_DISABLED = 2
        TOS_VIOLATION = 4
        QUOTA_EXCEEDED = 5
        ENVIRONMENT_UNAVAILABLE = 6

    code: CloudShellErrorCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=CloudShellErrorCode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
