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
    package="google.devtools.artifactregistry.v1",
    manifest={
        "DockerImage",
        "ImageManifest",
        "ListDockerImagesRequest",
        "ListDockerImagesResponse",
        "GetDockerImageRequest",
        "MavenArtifact",
        "ListMavenArtifactsRequest",
        "ListMavenArtifactsResponse",
        "GetMavenArtifactRequest",
        "NpmPackage",
        "ListNpmPackagesRequest",
        "ListNpmPackagesResponse",
        "GetNpmPackageRequest",
        "PythonPackage",
        "ListPythonPackagesRequest",
        "ListPythonPackagesResponse",
        "GetPythonPackageRequest",
    },
)


class DockerImage(proto.Message):
    r"""DockerImage represents a docker artifact. The following fields are
    returned as untyped metadata in the Version resource, using
    camelcase keys (i.e. metadata.imageSizeBytes):

    - imageSizeBytes
    - mediaType
    - buildTime

    Attributes:
        name (str):
            Required. registry_location, project_id, repository_name and
            image id forms a unique image
            name:``projects/<project_id>/locations/<location>/repositories/<repository_name>/dockerImages/<docker_image>``.
            For example,
            "projects/test-project/locations/us-west4/repositories/test-repo/dockerImages/
            nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf",
            where "us-west4" is the registry_location, "test-project" is
            the project_id, "test-repo" is the repository_name and
            "nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf"
            is the image's digest.
        uri (str):
            Required. URL to access the image.
            Example:

            us-west4-docker.pkg.dev/test-project/test-repo/nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf
        tags (MutableSequence[str]):
            Tags attached to this image.
        image_size_bytes (int):
            Calculated size of the image.
            This field is returned as the
            'metadata.imageSizeBytes' field in the Version
            resource.
        upload_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the image was uploaded.
        media_type (str):
            Media type of this image, e.g.
            "application/vnd.docker.distribution.manifest.v2+json".
            This field is returned as the
            'metadata.mediaType' field in the Version
            resource.
        build_time (google.protobuf.timestamp_pb2.Timestamp):
            The time this image was built.
            This field is returned as the
            'metadata.buildTime' field in the Version
            resource.
            The build time is returned to the client as an
            RFC 3339 string, which can be easily used with
            the JavaScript Date constructor.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the docker image
            was last updated.
        artifact_type (str):
            ArtifactType of this image, e.g.
            "application/vnd.example+type". If the ``subject_digest`` is
            set and no ``artifact_type`` is given, the ``media_type``
            will be considered as the ``artifact_type``. This field is
            returned as the ``metadata.artifactType`` field in the
            Version resource.
        image_manifests (MutableSequence[google.cloud.artifactregistry_v1.types.ImageManifest]):
            Optional. For multi-arch images (manifest
            lists), this field contains the list of image
            manifests.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    image_size_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )
    upload_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    media_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    build_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    artifact_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    image_manifests: MutableSequence["ImageManifest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="ImageManifest",
    )


class ImageManifest(proto.Message):
    r"""Details of a single image manifest within a multi-arch image.

    Attributes:
        architecture (str):
            Optional. The CPU architecture of the image.
            Values are provided by the Docker client and are
            not validated by Artifact Registry. Example
            values include "amd64", "arm64", "ppc64le",
            "s390x", "riscv64", "mips64le", etc.
        os (str):
            Optional. The operating system of the image.
            Values are provided by the Docker client and are
            not validated by Artifact Registry. Example
            values include "linux", "windows", "darwin",
            "aix", etc.
        digest (str):
            Optional. The manifest digest, in the format
            "sha256:<sha256_hex_digest>".
        media_type (str):
            Optional. The media type of the manifest,
            e.g.,
            "application/vnd.docker.distribution.manifest.v2+json".
        os_version (str):
            Optional. The OS version of the image, for example on
            Windows ``10.0.14393.1066``.
        os_features (MutableSequence[str]):
            Optional. The required OS features for the image, for
            example on Windows ``win32k``.
        variant (str):
            Optional. The variant of the CPU in the image, for example
            ``v7`` to specify ARMv7 when architecture is ``arm``.
    """

    architecture: str = proto.Field(
        proto.STRING,
        number=1,
    )
    os: str = proto.Field(
        proto.STRING,
        number=2,
    )
    digest: str = proto.Field(
        proto.STRING,
        number=3,
    )
    media_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    os_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    os_features: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    variant: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListDockerImagesRequest(proto.Message):
    r"""The request to list docker images.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            whose docker images will be listed.
        page_size (int):
            The maximum number of artifacts to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
        order_by (str):
            The field to order the results by.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDockerImagesResponse(proto.Message):
    r"""The response from listing docker images.

    Attributes:
        docker_images (MutableSequence[google.cloud.artifactregistry_v1.types.DockerImage]):
            The docker images returned.
        next_page_token (str):
            The token to retrieve the next page of
            artifacts, or empty if there are no more
            artifacts to return.
    """

    @property
    def raw_page(self):
        return self

    docker_images: MutableSequence["DockerImage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DockerImage",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDockerImageRequest(proto.Message):
    r"""The request to get docker images.

    Attributes:
        name (str):
            Required. The name of the docker images.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MavenArtifact(proto.Message):
    r"""MavenArtifact represents a maven artifact.

    Attributes:
        name (str):
            Required. registry_location, project_id, repository_name and
            maven_artifact forms a unique artifact For example,
            "projects/test-project/locations/us-west4/repositories/test-repo/mavenArtifacts/
            com.google.guava:guava:31.0-jre", where "us-west4" is the
            registry_location, "test-project" is the project_id,
            "test-repo" is the repository_name and
            "com.google.guava:guava:31.0-jre" is the maven artifact.
        pom_uri (str):
            Required. URL to access the pom file of the
            artifact. Example:

            us-west4-maven.pkg.dev/test-project/test-repo/com/google/guava/guava/31.0/guava-31.0.pom
        group_id (str):
            Group ID for the artifact.
            Example:

            com.google.guava
        artifact_id (str):
            Artifact ID for the artifact.
        version (str):
            Version of this artifact.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the artifact was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the artifact was updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pom_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    artifact_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class ListMavenArtifactsRequest(proto.Message):
    r"""The request to list maven artifacts.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            whose maven artifacts will be listed.
        page_size (int):
            The maximum number of artifacts to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
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


class ListMavenArtifactsResponse(proto.Message):
    r"""The response from listing maven artifacts.

    Attributes:
        maven_artifacts (MutableSequence[google.cloud.artifactregistry_v1.types.MavenArtifact]):
            The maven artifacts returned.
        next_page_token (str):
            The token to retrieve the next page of
            artifacts, or empty if there are no more
            artifacts to return.
    """

    @property
    def raw_page(self):
        return self

    maven_artifacts: MutableSequence["MavenArtifact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MavenArtifact",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMavenArtifactRequest(proto.Message):
    r"""The request to get maven artifacts.

    Attributes:
        name (str):
            Required. The name of the maven artifact.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NpmPackage(proto.Message):
    r"""NpmPackage represents an npm artifact.

    Attributes:
        name (str):
            Required. registry_location, project_id, repository_name and
            npm_package forms a unique package For example,
            "projects/test-project/locations/us-west4/repositories/test-repo/npmPackages/
            npm_test:1.0.0", where "us-west4" is the registry_location,
            "test-project" is the project_id, "test-repo" is the
            repository_name and npm_test:1.0.0" is the npm package.
        package_name (str):
            Package for the artifact.
        version (str):
            Version of this package.
        tags (MutableSequence[str]):
            Tags attached to this package.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the package was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the package was updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    package_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class ListNpmPackagesRequest(proto.Message):
    r"""The request to list npm packages.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            whose npm packages will be listed.
        page_size (int):
            The maximum number of artifacts to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
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


class ListNpmPackagesResponse(proto.Message):
    r"""The response from listing npm packages.

    Attributes:
        npm_packages (MutableSequence[google.cloud.artifactregistry_v1.types.NpmPackage]):
            The npm packages returned.
        next_page_token (str):
            The token to retrieve the next page of
            artifacts, or empty if there are no more
            artifacts to return.
    """

    @property
    def raw_page(self):
        return self

    npm_packages: MutableSequence["NpmPackage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NpmPackage",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetNpmPackageRequest(proto.Message):
    r"""The request to get npm packages.

    Attributes:
        name (str):
            Required. The name of the npm package.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PythonPackage(proto.Message):
    r"""PythonPackage represents a python artifact.

    Attributes:
        name (str):
            Required. registry_location, project_id, repository_name and
            python_package forms a unique package
            name:``projects/<project_id>/locations/<location>/repository/<repository_name>/pythonPackages/<python_package>``.
            For example,
            "projects/test-project/locations/us-west4/repositories/test-repo/pythonPackages/
            python_package:1.0.0", where "us-west4" is the
            registry_location, "test-project" is the project_id,
            "test-repo" is the repository_name and python_package:1.0.0"
            is the python package.
        uri (str):
            Required. URL to access the package. Example:
            us-west4-python.pkg.dev/test-project/test-repo/python_package/file-name-1.0.0.tar.gz
        package_name (str):
            Package for the artifact.
        version (str):
            Version of this package.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the package was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the package was updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    package_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class ListPythonPackagesRequest(proto.Message):
    r"""The request to list python packages.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            whose python packages will be listed.
        page_size (int):
            The maximum number of artifacts to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
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


class ListPythonPackagesResponse(proto.Message):
    r"""The response from listing python packages.

    Attributes:
        python_packages (MutableSequence[google.cloud.artifactregistry_v1.types.PythonPackage]):
            The python packages returned.
        next_page_token (str):
            The token to retrieve the next page of
            artifacts, or empty if there are no more
            artifacts to return.
    """

    @property
    def raw_page(self):
        return self

    python_packages: MutableSequence["PythonPackage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PythonPackage",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPythonPackageRequest(proto.Message):
    r"""The request to get python packages.

    Attributes:
        name (str):
            Required. The name of the python package.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
