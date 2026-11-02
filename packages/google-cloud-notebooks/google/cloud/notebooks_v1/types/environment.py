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
    package="google.cloud.notebooks.v1",
    manifest={
        "Environment",
        "VmImage",
        "ContainerImage",
    },
)


class Environment(proto.Message):
    r"""Definition of a software environment that is used to start a
    notebook instance.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Name of this environment. Format:
            ``projects/{project_id}/locations/{location}/environments/{environment_id}``
        display_name (str):
            Display name of this environment for the UI.
        description (str):
            A brief description of this environment.
        vm_image (google.cloud.notebooks_v1.types.VmImage):
            Use a Compute Engine VM image to start the
            notebook instance.

            This field is a member of `oneof`_ ``image_type``.
        container_image (google.cloud.notebooks_v1.types.ContainerImage):
            Use a container image to start the notebook
            instance.

            This field is a member of `oneof`_ ``image_type``.
        post_startup_script (str):
            Path to a Bash script that automatically runs after a
            notebook instance fully boots up. The path must be a URL or
            Cloud Storage path. Example:
            ``"gs://path-to-file/file-name"``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            environment was created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vm_image: "VmImage" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="image_type",
        message="VmImage",
    )
    container_image: "ContainerImage" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="image_type",
        message="ContainerImage",
    )
    post_startup_script: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


class VmImage(proto.Message):
    r"""Definition of a custom Compute Engine virtual machine image
    for starting a notebook instance with the environment installed
    directly on the VM.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project (str):
            Required. The name of the Google Cloud project that this VM
            image belongs to. Format: ``{project_id}``
        image_name (str):
            Use VM image name to find the image.

            This field is a member of `oneof`_ ``image``.
        image_family (str):
            Use this VM image family to find the image;
            the newest image in this family will be used.

            This field is a member of `oneof`_ ``image``.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image_name: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="image",
    )
    image_family: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="image",
    )


class ContainerImage(proto.Message):
    r"""Definition of a container image for starting a notebook
    instance with the environment installed in a container.

    Attributes:
        repository (str):
            Required. The path to the container image repository. For
            example: ``gcr.io/{project_id}/{image_name}``
        tag (str):
            The tag of the container image. If not
            specified, this defaults to the latest tag.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
