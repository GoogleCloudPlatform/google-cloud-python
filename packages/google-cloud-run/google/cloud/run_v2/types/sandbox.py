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

from google.cloud.run_v2.types import k8s_min

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "SandboxConfiguration",
        "SandboxTemplate",
    },
)


class SandboxConfiguration(proto.Message):
    r"""Configuration for sandboxes.

    Attributes:
        templates (MutableSequence[google.cloud.run_v2.types.SandboxTemplate]):
            Required. Sandbox templates that can be launched through the
            ``sandbox`` CLI.
    """

    templates: MutableSequence["SandboxTemplate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SandboxTemplate",
    )


class SandboxTemplate(proto.Message):
    r"""Template for a single sandbox.

    Attributes:
        name (str):
            Required. Name of the sandbox specified as a DNS_LABEL (RFC
            1123).
        image (str):
            Required. Name of the container image in
            Dockerhub or Artifact Registry. If the host is
            not provided, Dockerhub is assumed.
        command (MutableSequence[str]):
            Optional. Entrypoint array. Not executed
            within a shell. The docker image's ENTRYPOINT is
            used if this is not provided.
        args (MutableSequence[str]):
            Optional. Arguments to the entrypoint.
            The docker image's CMD is used if this is not
            provided.
        env (MutableSequence[google.cloud.run_v2.types.EnvVar]):
            Optional. List of environment variables to
            set in the sandbox.
        volume_mounts (MutableSequence[google.cloud.run_v2.types.VolumeMount]):
            Optional. Volume to mount into the
            container's filesystem.
        working_dir (str):
            Optional. Container's working directory.
            If not specified, the container runtime's
            default will be used, which might be configured
            in the container image.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image: str = proto.Field(
        proto.STRING,
        number=2,
    )
    command: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    env: MutableSequence[k8s_min.EnvVar] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=k8s_min.EnvVar,
    )
    volume_mounts: MutableSequence[k8s_min.VolumeMount] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=k8s_min.VolumeMount,
    )
    working_dir: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
