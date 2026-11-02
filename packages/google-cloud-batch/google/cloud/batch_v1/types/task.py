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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.batch_v1.types import volume

__protobuf__ = proto.module(
    package="google.cloud.batch.v1",
    manifest={
        "ComputeResource",
        "StatusEvent",
        "TaskExecution",
        "TaskStatus",
        "Runnable",
        "TaskSpec",
        "LifecyclePolicy",
        "Task",
        "Environment",
    },
)


class ComputeResource(proto.Message):
    r"""Compute resource requirements.

    ComputeResource defines the amount of resources required for each
    task. Make sure your tasks have enough resources to successfully
    run. If you also define the types of resources for a job to use with
    the
    `InstancePolicyOrTemplate <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate>`__
    field, make sure both fields are compatible with each other.

    Attributes:
        cpu_milli (int):
            The milliCPU count.

            ``cpuMilli`` defines the amount of CPU resources per task in
            milliCPU units. For example, ``1000`` corresponds to 1 vCPU
            per task. If undefined, the default value is ``2000``.

            If you also define the VM's machine type using the
            ``machineType`` in
            `InstancePolicy <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy>`__
            field or inside the ``instanceTemplate`` in the
            `InstancePolicyOrTemplate <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate>`__
            field, make sure the CPU resources for both fields are
            compatible with each other and with how many tasks you want
            to allow to run on the same VM at the same time.

            For example, if you specify the ``n2-standard-2`` machine
            type, which has 2 vCPUs each, you are recommended to set
            ``cpuMilli`` no more than ``2000``, or you are recommended
            to run two tasks on the same VM if you set ``cpuMilli`` to
            ``1000`` or less.
        memory_mib (int):
            Memory in MiB.

            ``memoryMib`` defines the amount of memory per task in MiB
            units. If undefined, the default value is ``2000``. If you
            also define the VM's machine type using the ``machineType``
            in
            `InstancePolicy <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy>`__
            field or inside the ``instanceTemplate`` in the
            `InstancePolicyOrTemplate <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate>`__
            field, make sure the memory resources for both fields are
            compatible with each other and with how many tasks you want
            to allow to run on the same VM at the same time.

            For example, if you specify the ``n2-standard-2`` machine
            type, which has 8 GiB each, you are recommended to set
            ``memoryMib`` to no more than ``8192``, or you are
            recommended to run two tasks on the same VM if you set
            ``memoryMib`` to ``4096`` or less.
        boot_disk_mib (int):
            Extra boot disk size in MiB for each task.
    """

    cpu_milli: int = proto.Field(
        proto.INT64,
        number=1,
    )
    memory_mib: int = proto.Field(
        proto.INT64,
        number=2,
    )
    boot_disk_mib: int = proto.Field(
        proto.INT64,
        number=4,
    )


class StatusEvent(proto.Message):
    r"""Status event.

    Attributes:
        type_ (str):
            Type of the event.
        description (str):
            Description of the event.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            The time this event occurred.
        task_execution (google.cloud.batch_v1.types.TaskExecution):
            Task Execution.
            This field is only defined for task-level status
            events where the task fails.
        task_state (google.cloud.batch_v1.types.TaskStatus.State):
            Task State.
            This field is only defined for task-level status
            events.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    task_execution: "TaskExecution" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TaskExecution",
    )
    task_state: "TaskStatus.State" = proto.Field(
        proto.ENUM,
        number=5,
        enum="TaskStatus.State",
    )


class TaskExecution(proto.Message):
    r"""This Task Execution field includes detail information for
    task execution procedures, based on StatusEvent types.

    Attributes:
        exit_code (int):
            The exit code of a finished task.

            If the task succeeded, the exit code will be 0. If the task
            failed but not due to the following reasons, the exit code
            will be 50000.

            Otherwise, it can be from different sources:

            - Batch known failures:
              https://cloud.google.com/batch/docs/troubleshooting#reserved-exit-codes.
            - Batch runnable execution failures; you can rely on Batch
              logs to further diagnose:
              https://cloud.google.com/batch/docs/analyze-job-using-logs.
              If there are multiple runnables failures, Batch only
              exposes the first error.
    """

    exit_code: int = proto.Field(
        proto.INT32,
        number=1,
    )


class TaskStatus(proto.Message):
    r"""Status of a task.

    Attributes:
        state (google.cloud.batch_v1.types.TaskStatus.State):
            Task state.
        status_events (MutableSequence[google.cloud.batch_v1.types.StatusEvent]):
            Detailed info about why the state is reached.
    """

    class State(proto.Enum):
        r"""Task states.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown state.
            PENDING (1):
                The Task is created and waiting for
                resources.
            ASSIGNED (2):
                The Task is assigned to at least one VM.
            RUNNING (3):
                The Task is running.
            FAILED (4):
                The Task has failed.
            SUCCEEDED (5):
                The Task has succeeded.
            UNEXECUTED (6):
                The Task has not been executed when the Job
                finishes.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ASSIGNED = 2
        RUNNING = 3
        FAILED = 4
        SUCCEEDED = 5
        UNEXECUTED = 6

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    status_events: MutableSequence["StatusEvent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="StatusEvent",
    )


class Runnable(proto.Message):
    r"""Runnable describes instructions for executing a specific
    script or container as part of a Task.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        container (google.cloud.batch_v1.types.Runnable.Container):
            Container runnable.

            This field is a member of `oneof`_ ``executable``.
        script (google.cloud.batch_v1.types.Runnable.Script):
            Script runnable.

            This field is a member of `oneof`_ ``executable``.
        barrier (google.cloud.batch_v1.types.Runnable.Barrier):
            Barrier runnable.

            This field is a member of `oneof`_ ``executable``.
        display_name (str):
            Optional. DisplayName is an optional field
            that can be provided by the caller. If provided,
            it will be used in logs and other outputs to
            identify the script, making it easier for users
            to understand the logs. If not provided the
            index of the runnable will be used for outputs.
        ignore_exit_status (bool):
            Normally, a runnable that returns a non-zero exit status
            fails and causes the task to fail. However, you can set this
            field to ``true`` to allow the task to continue executing
            its other runnables even if this runnable fails.
        background (bool):
            Normally, a runnable that doesn't exit causes its task to
            fail. However, you can set this field to ``true`` to
            configure a background runnable. Background runnables are
            allowed continue running in the background while the task
            executes subsequent runnables. For example, background
            runnables are useful for providing services to other
            runnables or providing debugging-support tools like SSH
            servers.

            Specifically, background runnables are killed automatically
            (if they have not already exited) a short time after all
            foreground runnables have completed. Even though this is
            likely to result in a non-zero exit status for the
            background runnable, these automatic kills are not treated
            as task failures.
        always_run (bool):
            By default, after a Runnable fails, no further Runnable are
            executed. This flag indicates that this Runnable must be run
            even if the Task has already failed. This is useful for
            Runnables that copy output files off of the VM or for
            debugging.

            The always_run flag does not override the Task's overall
            max_run_duration. If the max_run_duration has expired then
            no further Runnables will execute, not even always_run
            Runnables.
        environment (google.cloud.batch_v1.types.Environment):
            Environment variables for this Runnable
            (overrides variables set for the whole Task or
            TaskGroup).
        timeout (google.protobuf.duration_pb2.Duration):
            Timeout for this Runnable.
        labels (MutableMapping[str, str]):
            Labels for this Runnable.
    """

    class Container(proto.Message):
        r"""Container runnable.

        Attributes:
            image_uri (str):
                Required. The URI to pull the container image
                from.
            commands (MutableSequence[str]):
                Required for some container images. Overrides the ``CMD``
                specified in the container. If there is an ``ENTRYPOINT``
                (either in the container image or with the ``entrypoint``
                field below) then these commands are appended as arguments
                to the ``ENTRYPOINT``.
            entrypoint (str):
                Required for some container images. Overrides the
                ``ENTRYPOINT`` specified in the container.
            volumes (MutableSequence[str]):
                Volumes to mount (bind mount) from the host machine files or
                directories into the container, formatted to match
                ``--volume`` option for the ``docker run`` command—for
                example, ``/foo:/bar`` or ``/foo:/bar:ro``.

                If the ``TaskSpec.Volumes`` field is specified but this
                field is not, Batch will mount each volume from the host
                machine to the container with the same mount path by
                default. In this case, the default mount option for
                containers will be read-only (``ro``) for existing
                persistent disks and read-write (``rw``) for other volume
                types, regardless of the original mount options specified in
                ``TaskSpec.Volumes``. If you need different mount settings,
                you can explicitly configure them in this field.
            options (str):
                Required for some container images. Arbitrary additional
                options to include in the ``docker run`` command when
                running this container—for example, ``--network host``. For
                the ``--volume`` option, use the ``volumes`` field for the
                container.
            block_external_network (bool):
                If set to true, external network access to and from
                container will be blocked, containers that are with
                block_external_network as true can still communicate with
                each other, network cannot be specified in the
                ``container.options`` field.
            username (str):
                Required if the container image is from a private Docker
                registry. The username to login to the Docker registry that
                contains the image.

                You can either specify the username directly by using plain
                text or specify an encrypted username by using a Secret
                Manager secret: ``projects/*/secrets/*/versions/*``.
                However, using a secret is recommended for enhanced
                security.

                Caution: If you specify the username using plain text, you
                risk the username being exposed to any users who can view
                the job or its logs. To avoid this risk, specify a secret
                that contains the username instead.

                Learn more about `Secret
                Manager <https://cloud.google.com/secret-manager/docs/>`__
                and `using Secret Manager with
                Batch <https://cloud.google.com/batch/docs/create-run-job-secret-manager>`__.
            password (str):
                Required if the container image is from a private Docker
                registry. The password to login to the Docker registry that
                contains the image.

                For security, it is strongly recommended to specify an
                encrypted password by using a Secret Manager secret:
                ``projects/*/secrets/*/versions/*``.

                Warning: If you specify the password using plain text, you
                risk the password being exposed to any users who can view
                the job or its logs. To avoid this risk, specify a secret
                that contains the password instead.

                Learn more about `Secret
                Manager <https://cloud.google.com/secret-manager/docs/>`__
                and `using Secret Manager with
                Batch <https://cloud.google.com/batch/docs/create-run-job-secret-manager>`__.
            enable_image_streaming (bool):
                Optional. If set to true, this container runnable uses Image
                streaming.

                Use Image streaming to allow the runnable to initialize
                without waiting for the entire container image to download,
                which can significantly reduce startup time for large
                container images.

                When ``enableImageStreaming`` is set to true, the container
                runtime is `containerd <https://containerd.io/>`__ instead
                of Docker. Additionally, this container runnable only
                supports the following ``container`` subfields:
                ``imageUri``, ``commands[]``, ``entrypoint``, and
                ``volumes[]``; any other ``container`` subfields are
                ignored.

                For more information about the requirements and limitations
                for using Image streaming with Batch, see the
                ```image-streaming`` sample on
                GitHub <https://github.com/GoogleCloudPlatform/batch-samples/tree/main/api-samples/image-streaming>`__.
        """

        image_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        commands: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        entrypoint: str = proto.Field(
            proto.STRING,
            number=3,
        )
        volumes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )
        options: str = proto.Field(
            proto.STRING,
            number=8,
        )
        block_external_network: bool = proto.Field(
            proto.BOOL,
            number=9,
        )
        username: str = proto.Field(
            proto.STRING,
            number=10,
        )
        password: str = proto.Field(
            proto.STRING,
            number=11,
        )
        enable_image_streaming: bool = proto.Field(
            proto.BOOL,
            number=12,
        )

    class Script(proto.Message):
        r"""Script runnable.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            path (str):
                The path to a script file that is accessible from the host
                VM(s).

                Unless the script file supports the default ``#!/bin/sh``
                shell interpreter, you must specify an interpreter by
                including a [shebang
                line](https://en.wikipedia.org/wiki/Shebang\_(Unix) as the
                first line of the file. For example, to execute the script
                using bash, include ``#!/bin/bash`` as the first line of the
                file. Alternatively, to execute the script using Python3,
                include ``#!/usr/bin/env python3`` as the first line of the
                file.

                This field is a member of `oneof`_ ``command``.
            text (str):
                The text for a script.

                Unless the script text supports the default ``#!/bin/sh``
                shell interpreter, you must specify an interpreter by
                including a [shebang
                line](https://en.wikipedia.org/wiki/Shebang\_(Unix) at the
                beginning of the text. For example, to execute the script
                using bash, include ``#!/bin/bash\n`` at the beginning of
                the text. Alternatively, to execute the script using
                Python3, include ``#!/usr/bin/env python3\n`` at the
                beginning of the text.

                This field is a member of `oneof`_ ``command``.
        """

        path: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="command",
        )
        text: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="command",
        )

    class Barrier(proto.Message):
        r"""A barrier runnable automatically blocks the execution of
        subsequent runnables until all the tasks in the task group reach
        the barrier.

        Attributes:
            name (str):
                Barriers are identified by their index in
                runnable list. Names are not required, but if
                present should be an identifier.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    container: Container = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="executable",
        message=Container,
    )
    script: Script = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="executable",
        message=Script,
    )
    barrier: Barrier = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="executable",
        message=Barrier,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ignore_exit_status: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    background: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    always_run: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Environment",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class TaskSpec(proto.Message):
    r"""Spec of a task

    Attributes:
        runnables (MutableSequence[google.cloud.batch_v1.types.Runnable]):
            Required. The sequence of one or more runnables (executable
            scripts, executable containers, and/or barriers) for each
            task in this task group to run. Each task runs this list of
            runnables in order. For a task to succeed, all of its script
            and container runnables each must meet at least one of the
            following conditions:

            - The runnable exited with a zero status.
            - The runnable didn't finish, but you enabled its
              ``background`` subfield.
            - The runnable exited with a non-zero status, but you
              enabled its ``ignore_exit_status`` subfield.
        compute_resource (google.cloud.batch_v1.types.ComputeResource):
            ComputeResource requirements.
        max_run_duration (google.protobuf.duration_pb2.Duration):
            Maximum duration the task should run before being
            automatically retried (if enabled) or automatically failed.
            Format the value of this field as a time limit in seconds
            followed by ``s``—for example, ``3600s`` for 1 hour. The
            field accepts any value between 0 and the maximum listed for
            the ``Duration`` field type at
            https://protobuf.dev/reference/protobuf/google.protobuf/#duration;
            however, the actual maximum run time for a job will be
            limited to the maximum run time for a job listed at
            https://cloud.google.com/batch/quotas#max-job-duration.
        max_retry_count (int):
            Maximum number of retries on failures. The default, 0, which
            means never retry. The valid value range is [0, 10].
        lifecycle_policies (MutableSequence[google.cloud.batch_v1.types.LifecyclePolicy]):
            Lifecycle management schema when any task in a task group is
            failed. Currently we only support one lifecycle policy. When
            the lifecycle policy condition is met, the action in the
            policy will execute. If task execution result does not meet
            with the defined lifecycle policy, we consider it as the
            default policy. Default policy means if the exit code is 0,
            exit task. If task ends with non-zero exit code, retry the
            task with max_retry_count.
        environments (MutableMapping[str, str]):
            Deprecated: please use
            environment(non-plural) instead.
        volumes (MutableSequence[google.cloud.batch_v1.types.Volume]):
            Volumes to mount before running Tasks using
            this TaskSpec.
        environment (google.cloud.batch_v1.types.Environment):
            Environment variables to set before running
            the Task.
    """

    runnables: MutableSequence["Runnable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="Runnable",
    )
    compute_resource: "ComputeResource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ComputeResource",
    )
    max_run_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    max_retry_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    lifecycle_policies: MutableSequence["LifecyclePolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="LifecyclePolicy",
    )
    environments: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    volumes: MutableSequence[volume.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=volume.Volume,
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Environment",
    )


class LifecyclePolicy(proto.Message):
    r"""LifecyclePolicy describes how to deal with task failures
    based on different conditions.

    Attributes:
        action (google.cloud.batch_v1.types.LifecyclePolicy.Action):
            Action to execute when ActionCondition is true. When
            RETRY_TASK is specified, we will retry failed tasks if we
            notice any exit code match and fail tasks if no match is
            found. Likewise, when FAIL_TASK is specified, we will fail
            tasks if we notice any exit code match and retry tasks if no
            match is found.
        action_condition (google.cloud.batch_v1.types.LifecyclePolicy.ActionCondition):
            Conditions that decide why a task failure is
            dealt with a specific action.
    """

    class Action(proto.Enum):
        r"""Action on task failures based on different conditions.

        Values:
            ACTION_UNSPECIFIED (0):
                Action unspecified.
            RETRY_TASK (1):
                Action that tasks in the group will be
                scheduled to re-execute.
            FAIL_TASK (2):
                Action that tasks in the group will be
                stopped immediately.
        """

        ACTION_UNSPECIFIED = 0
        RETRY_TASK = 1
        FAIL_TASK = 2

    class ActionCondition(proto.Message):
        r"""Conditions for actions to deal with task failures.

        Attributes:
            exit_codes (MutableSequence[int]):
                Exit codes of a task execution.
                If there are more than 1 exit codes,
                when task executes with any of the exit code in
                the list, the condition is met and the action
                will be executed.
        """

        exit_codes: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=1,
        )

    action: Action = proto.Field(
        proto.ENUM,
        number=1,
        enum=Action,
    )
    action_condition: ActionCondition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ActionCondition,
    )


class Task(proto.Message):
    r"""A Cloud Batch task.

    Attributes:
        name (str):
            Task name.
            The name is generated from the parent TaskGroup
            name and 'id' field. For example:

            "projects/123456/locations/us-west1/jobs/job01/taskGroups/group01/tasks/task01".
        status (google.cloud.batch_v1.types.TaskStatus):
            Task Status.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: "TaskStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TaskStatus",
    )


class Environment(proto.Message):
    r"""An Environment describes a collection of environment
    variables to set when executing Tasks.

    Attributes:
        variables (MutableMapping[str, str]):
            A map of environment variable names to
            values.
        secret_variables (MutableMapping[str, str]):
            A map of environment variable names to Secret
            Manager secret names. The VM will access the
            named secrets to set the value of each
            environment variable.
        encrypted_variables (google.cloud.batch_v1.types.Environment.KMSEnvMap):
            An encrypted JSON dictionary where the
            key/value pairs correspond to environment
            variable names and their values.
    """

    class KMSEnvMap(proto.Message):
        r"""

        Attributes:
            key_name (str):
                The name of the KMS key that will be used to
                decrypt the cipher text.
            cipher_text (str):
                The value of the cipherText response from the ``encrypt``
                method.
        """

        key_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        cipher_text: str = proto.Field(
            proto.STRING,
            number=2,
        )

    variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    secret_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    encrypted_variables: KMSEnvMap = proto.Field(
        proto.MESSAGE,
        number=3,
        message=KMSEnvMap,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
