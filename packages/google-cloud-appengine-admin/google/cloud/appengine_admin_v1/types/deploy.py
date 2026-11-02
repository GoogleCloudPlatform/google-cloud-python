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

__protobuf__ = proto.module(
    package="google.appengine.v1",
    manifest={
        "Deployment",
        "FileInfo",
        "ContainerInfo",
        "CloudBuildOptions",
        "ZipInfo",
    },
)


class Deployment(proto.Message):
    r"""Code and application artifacts used to deploy a version to
    App Engine.

    Attributes:
        files (MutableMapping[str, google.cloud.appengine_admin_v1.types.FileInfo]):
            Manifest of the files stored in Google Cloud
            Storage that are included as part of this
            version. All files must be readable using the
            credentials supplied with this call.
        container (google.cloud.appengine_admin_v1.types.ContainerInfo):
            The Docker image for the container that runs
            the version. Only applicable for instances
            running in the App Engine flexible environment.
        zip_ (google.cloud.appengine_admin_v1.types.ZipInfo):
            The zip file for this deployment, if this is
            a zip deployment.
        cloud_build_options (google.cloud.appengine_admin_v1.types.CloudBuildOptions):
            Options for any Google Cloud Build builds
            created as a part of this deployment.

            These options will only be used if a new build
            is created, such as when deploying to the App
            Engine flexible environment using files or zip.
    """

    files: MutableMapping[str, "FileInfo"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="FileInfo",
    )
    container: "ContainerInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ContainerInfo",
    )
    zip_: "ZipInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ZipInfo",
    )
    cloud_build_options: "CloudBuildOptions" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CloudBuildOptions",
    )


class FileInfo(proto.Message):
    r"""Single source file that is part of the version to be
    deployed. Each source file that is deployed must be specified
    separately.

    Attributes:
        source_url (str):
            URL source to use to fetch this file. Must be
            a URL to a resource in Google Cloud Storage in
            the form
            'http(s)://storage.googleapis.com/\<bucket\>/\<object\>'.
        sha1_sum (str):
            The SHA1 hash of the file, in hex.
        mime_type (str):
            The MIME type of the file.

            Defaults to the value from Google Cloud Storage.
    """

    source_url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sha1_sum: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ContainerInfo(proto.Message):
    r"""Docker image that is used to create a container and start a
    VM instance for the version that you deploy. Only applicable for
    instances running in the App Engine flexible environment.

    Attributes:
        image (str):
            URI to the hosted container image in Google
            Container Registry. The URI must be fully
            qualified and include a tag or digest. Examples:
            "gcr.io/my-project/image:tag" or
            "gcr.io/my-project/image@digest".
    """

    image: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudBuildOptions(proto.Message):
    r"""Options for the build operations performed as a part of the
    version deployment. Only applicable for App Engine flexible
    environment when creating a version using source code directly.

    Attributes:
        app_yaml_path (str):
            Path to the yaml file used in deployment,
            used to determine runtime configuration details.

            Required for flexible environment builds.

            See
            https://cloud.google.com/appengine/docs/standard/python/config/appref
            for more details.
        cloud_build_timeout (google.protobuf.duration_pb2.Duration):
            The Cloud Build timeout used as part of any
            dependent builds performed by version creation.
            Defaults to 10 minutes.
    """

    app_yaml_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_build_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class ZipInfo(proto.Message):
    r"""The zip file information for a zip deployment.

    Attributes:
        source_url (str):
            URL of the zip file to deploy from. Must be a
            URL to a resource in Google Cloud Storage in the
            form
            'http(s)://storage.googleapis.com/\<bucket\>/\<object\>'.
        files_count (int):
            An estimate of the number of files in a zip
            for a zip deployment. If set, must be greater
            than or equal to the actual number of files.
            Used for optimizing performance; if not
            provided, deployment may be slow.
    """

    source_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    files_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
