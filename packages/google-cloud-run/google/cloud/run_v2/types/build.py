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

import google.api.launch_stage_pb2 as launch_stage_pb2  # type: ignore
import google.longrunning.operations_pb2 as operations_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "SubmitBuildRequest",
        "SubmitBuildResponse",
        "StorageSource",
    },
)


class SubmitBuildRequest(proto.Message):
    r"""Request message for submitting a Build.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The project and location to build in. Location
            must be a region, e.g., 'us-central1' or 'global' if the
            global builder is to be used. Format:
            ``projects/{project}/locations/{location}``
        storage_source (google.cloud.run_v2.types.StorageSource):
            Required. Source for the build.

            This field is a member of `oneof`_ ``source``.
        image_uri (str):
            Required. Artifact Registry URI to store the
            built image.
        buildpack_build (google.cloud.run_v2.types.SubmitBuildRequest.BuildpacksBuild):
            Build the source using Buildpacks.

            This field is a member of `oneof`_ ``build_type``.
        docker_build (google.cloud.run_v2.types.SubmitBuildRequest.DockerBuild):
            Build the source using Docker. This means the
            source has a Dockerfile.

            This field is a member of `oneof`_ ``build_type``.
        service_account (str):
            Optional. The service account to use for the
            build. If not set, the default Cloud Build
            service account for the project will be used.
        worker_pool (str):
            Optional. Name of the Cloud Build Custom Worker Pool that
            should be used to build the function. The format of this
            field is
            ``projects/{project}/locations/{region}/workerPools/{workerPool}``
            where ``{project}`` and ``{region}`` are the project id and
            region respectively where the worker pool is defined and
            ``{workerPool}`` is the short name of the worker pool.
        tags (MutableSequence[str]):
            Optional. Additional tags to annotate the
            build.
        machine_type (str):
            Optional. The machine type from default pool to use for the
            build. If left blank, cloudbuild will use a sensible
            default. Currently only E2_HIGHCPU_8 is supported. If
            worker_pool is set, this field will be ignored.
        release_track (google.api.launch_stage_pb2.LaunchStage):
            Optional. The release track of the client
            that initiated the build request.
        client (str):
            Optional. The client that initiated the build
            request.
    """

    class DockerBuild(proto.Message):
        r"""Build the source using Docker. This means the source has a
        Dockerfile.

        """

    class BuildpacksBuild(proto.Message):
        r"""Build the source using Buildpacks.

        Attributes:
            runtime (str):
                The runtime name, e.g. 'go113'. Leave blank
                for generic builds.
            function_target (str):
                Optional. Name of the function target if the
                source is a function source. Required for
                function builds.
            cache_image_uri (str):
                Optional. cache_image_uri is the GCR/AR URL where the cache
                image will be stored. cache_image_uri is optional and
                omitting it will disable caching. This URL must be stable
                across builds. It is used to derive a build-specific
                temporary URL by substituting the tag with the build ID. The
                build will clean up the temporary image on a best-effort
                basis.
            base_image (str):
                Optional. The base image to use for the
                build.
            environment_variables (MutableMapping[str, str]):
                Optional. User-provided build-time
                environment variables.
            enable_automatic_updates (bool):
                Optional. Whether or not the application
                container will be enrolled in automatic base
                image updates. When true, the application will
                be built on a scratch base image, so the base
                layers can be appended at run time.
            project_descriptor (str):
                Optional. project_descriptor stores the path to the project
                descriptor file. When empty, it means that there is no
                project descriptor file in the source.
        """

        runtime: str = proto.Field(
            proto.STRING,
            number=1,
        )
        function_target: str = proto.Field(
            proto.STRING,
            number=2,
        )
        cache_image_uri: str = proto.Field(
            proto.STRING,
            number=3,
        )
        base_image: str = proto.Field(
            proto.STRING,
            number=4,
        )
        environment_variables: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=5,
        )
        enable_automatic_updates: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        project_descriptor: str = proto.Field(
            proto.STRING,
            number=7,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    storage_source: "StorageSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="StorageSource",
    )
    image_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    buildpack_build: BuildpacksBuild = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="build_type",
        message=BuildpacksBuild,
    )
    docker_build: DockerBuild = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="build_type",
        message=DockerBuild,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=7,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    release_track: launch_stage_pb2.LaunchStage = proto.Field(
        proto.ENUM,
        number=10,
        enum=launch_stage_pb2.LaunchStage,
    )
    client: str = proto.Field(
        proto.STRING,
        number=11,
    )


class SubmitBuildResponse(proto.Message):
    r"""Response message for submitting a Build.

    Attributes:
        build_operation (google.longrunning.operations_pb2.Operation):
            Cloud Build operation to be polled via
            CloudBuild API.
        base_image_uri (str):
            URI of the base builder image in Artifact
            Registry being used in the build. Used to opt
            into automatic base image updates.
        base_image_warning (str):
            Warning message for the base image.
    """

    build_operation: operations_pb2.Operation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operations_pb2.Operation,
    )
    base_image_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    base_image_warning: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StorageSource(proto.Message):
    r"""Location of the source in an archive file in Google Cloud
    Storage.

    Attributes:
        bucket (str):
            Required. Google Cloud Storage bucket containing the source
            (see `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
        object_ (str):
            Required. Google Cloud Storage object containing the source.

            This object must be a gzipped archive file (``.tar.gz``)
            containing source to build.
        generation (int):
            Optional. Google Cloud Storage generation for
            the object. If the generation is omitted, the
            latest generation will be used.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    object_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
