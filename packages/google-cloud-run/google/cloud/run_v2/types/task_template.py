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

from google.cloud.run_v2.types import k8s_min, vendor_settings

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "TaskTemplate",
    },
)


class TaskTemplate(proto.Message):
    r"""TaskTemplate describes the data a task should have when
    created from a template.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        containers (MutableSequence[google.cloud.run_v2.types.Container]):
            Holds the single container that defines the
            unit of execution for this task.
        volumes (MutableSequence[google.cloud.run_v2.types.Volume]):
            Optional. A list of Volumes to make available
            to containers.
        max_retries (int):
            Number of retries allowed per Task, before
            marking this Task failed. Defaults to 3.

            This field is a member of `oneof`_ ``retries``.
        timeout (google.protobuf.duration_pb2.Duration):
            Optional. Max allowed time duration the Task
            may be active before the system will actively
            try to mark it failed and kill associated
            containers. This applies per attempt of a task,
            meaning each retry can run for the full timeout.
            Defaults to 600 seconds.
        service_account (str):
            Optional. Email address of the IAM service
            account associated with the Task of a Job. The
            service account represents the identity of the
            running task, and determines what permissions
            the task has. If not provided, the task will use
            the project's default service account.
        execution_environment (google.cloud.run_v2.types.ExecutionEnvironment):
            Optional. The execution environment being
            used to host this Task.
        encryption_key (str):
            A reference to a customer managed encryption
            key (CMEK) to use to encrypt this container
            image. For more information, go to
            https://cloud.google.com/run/docs/securing/using-cmek
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            Optional. VPC Access configuration to use for
            this Task. For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
        node_selector (google.cloud.run_v2.types.NodeSelector):
            Optional. The node selector for the task
            template.
        gpu_zonal_redundancy_disabled (bool):
            Optional. True if GPU zonal redundancy is
            disabled on this task template.

            This field is a member of `oneof`_ ``_gpu_zonal_redundancy_disabled``.
    """

    containers: MutableSequence[k8s_min.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=k8s_min.Container,
    )
    volumes: MutableSequence[k8s_min.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=k8s_min.Volume,
    )
    max_retries: int = proto.Field(
        proto.INT32,
        number=3,
        oneof="retries",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    execution_environment: vendor_settings.ExecutionEnvironment = proto.Field(
        proto.ENUM,
        number=6,
        enum=vendor_settings.ExecutionEnvironment,
    )
    encryption_key: str = proto.Field(
        proto.STRING,
        number=7,
    )
    vpc_access: vendor_settings.VpcAccess = proto.Field(
        proto.MESSAGE,
        number=8,
        message=vendor_settings.VpcAccess,
    )
    node_selector: vendor_settings.NodeSelector = proto.Field(
        proto.MESSAGE,
        number=11,
        message=vendor_settings.NodeSelector,
    )
    gpu_zonal_redundancy_disabled: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
