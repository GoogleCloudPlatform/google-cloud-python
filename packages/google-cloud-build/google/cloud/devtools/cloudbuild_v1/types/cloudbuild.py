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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.cloudbuild.v1",
    manifest={
        "GetDefaultServiceAccountRequest",
        "DefaultServiceAccount",
        "RetryBuildRequest",
        "RunBuildTriggerRequest",
        "StorageSource",
        "GitSource",
        "RepoSource",
        "StorageSourceManifest",
        "ConnectedRepository",
        "Source",
        "BuiltImage",
        "UploadedPythonPackage",
        "UploadedMavenArtifact",
        "UploadedGoModule",
        "UploadedNpmPackage",
        "BuildStep",
        "Volume",
        "Results",
        "ArtifactResult",
        "Build",
        "Dependency",
        "GitConfig",
        "Artifacts",
        "TimeSpan",
        "BuildOperationMetadata",
        "SourceProvenance",
        "FileHashes",
        "Hash",
        "Secrets",
        "InlineSecret",
        "SecretManagerSecret",
        "Secret",
        "CreateBuildRequest",
        "GetBuildRequest",
        "ListBuildsRequest",
        "ListBuildsResponse",
        "CancelBuildRequest",
        "ApproveBuildRequest",
        "BuildApproval",
        "ApprovalConfig",
        "ApprovalResult",
        "GitRepoSource",
        "GitFileSource",
        "BuildTrigger",
        "RepositoryEventConfig",
        "GitHubEventsConfig",
        "PubsubConfig",
        "WebhookConfig",
        "PullRequestFilter",
        "PushFilter",
        "CreateBuildTriggerRequest",
        "GetBuildTriggerRequest",
        "ListBuildTriggersRequest",
        "ListBuildTriggersResponse",
        "DeleteBuildTriggerRequest",
        "UpdateBuildTriggerRequest",
        "BuildOptions",
        "ReceiveTriggerWebhookRequest",
        "ReceiveTriggerWebhookResponse",
        "GitHubEnterpriseConfig",
        "GitHubEnterpriseSecrets",
        "WorkerPool",
        "PrivatePoolV1Config",
        "CreateWorkerPoolRequest",
        "GetWorkerPoolRequest",
        "DeleteWorkerPoolRequest",
        "UpdateWorkerPoolRequest",
        "ListWorkerPoolsRequest",
        "ListWorkerPoolsResponse",
        "CreateWorkerPoolOperationMetadata",
        "UpdateWorkerPoolOperationMetadata",
        "DeleteWorkerPoolOperationMetadata",
    },
)


class GetDefaultServiceAccountRequest(proto.Message):
    r"""Returns the default service account that will be used for
    ``Builds``.

    Attributes:
        name (str):
            Required. The name of the ``DefaultServiceAccount`` to
            retrieve. Format:
            ``projects/{project}/locations/{location}/defaultServiceAccount``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DefaultServiceAccount(proto.Message):
    r"""The default service account used for ``Builds``.

    Attributes:
        name (str):
            Identifier. Format:
            ``projects/{project}/locations/{location}/defaultServiceAccount``
        service_account_email (str):
            Output only. The email address of the service account
            identity that will be used for a build by default.

            This is returned in the format
            ``projects/{project}/serviceAccounts/{service_account}``
            where ``{service_account}`` could be the legacy Cloud Build
            SA, in the format
            [PROJECT_NUMBER]@cloudbuild.gserviceaccount.com or the
            Compute SA, in the format
            [PROJECT_NUMBER]-compute@developer.gserviceaccount.com.

            If no service account will be used by default, this will be
            empty.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RetryBuildRequest(proto.Message):
    r"""Specifies a build to retry.

    Attributes:
        name (str):
            The name of the ``Build`` to retry. Format:
            ``projects/{project}/locations/{location}/builds/{build}``
        project_id (str):
            Required. ID of the project.
        id (str):
            Required. Build ID of the original build.
    """

    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RunBuildTriggerRequest(proto.Message):
    r"""Specifies a build trigger to run and the source to use.

    Attributes:
        name (str):
            The name of the ``Trigger`` to run. Format:
            ``projects/{project}/locations/{location}/triggers/{trigger}``
        project_id (str):
            Required. ID of the project.
        trigger_id (str):
            Required. ID of the trigger.
        source (google.cloud.devtools.cloudbuild_v1.types.RepoSource):
            Source to build against this trigger.
            Branch and tag names cannot consist of regular
            expressions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source: "RepoSource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RepoSource",
    )


class StorageSource(proto.Message):
    r"""Location of the source in an archive file in Cloud Storage.

    Attributes:
        bucket (str):
            Cloud Storage bucket containing the source (see `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
        object_ (str):
            Required. Cloud Storage object containing the source.

            This object must be a zipped (``.zip``) or gzipped archive
            file (``.tar.gz``) containing source to build.
        generation (int):
            Optional. Cloud Storage generation for the
            object. If the generation is omitted, the latest
            generation will be used.
        source_fetcher (google.cloud.devtools.cloudbuild_v1.types.StorageSource.SourceFetcher):
            Optional. Option to specify the tool to fetch
            the source file for the build.
    """

    class SourceFetcher(proto.Enum):
        r"""Specifies the tool to fetch the source file for the build.

        Values:
            SOURCE_FETCHER_UNSPECIFIED (0):
                Unspecified defaults to GSUTIL.
            GSUTIL (1):
                Use the "gsutil" tool to download the source
                file.
            GCS_FETCHER (2):
                Use the Cloud Storage Fetcher tool to
                download the source file.
        """

        SOURCE_FETCHER_UNSPECIFIED = 0
        GSUTIL = 1
        GCS_FETCHER = 2

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
    source_fetcher: SourceFetcher = proto.Field(
        proto.ENUM,
        number=5,
        enum=SourceFetcher,
    )


class GitSource(proto.Message):
    r"""Location of the source in any accessible Git repository.

    Attributes:
        url (str):
            Required. Location of the Git repo to build.

            This will be used as a ``git remote``, see
            https://git-scm.com/docs/git-remote.
        dir_ (str):
            Optional. Directory, relative to the source root, in which
            to run the build.

            This must be a relative path. If a step's ``dir`` is
            specified and is an absolute path, this value is ignored for
            that step's execution.
        revision (str):
            Optional. The revision to fetch from the Git repository such
            as a branch, a tag, a commit SHA, or any Git ref.

            Cloud Build uses ``git fetch`` to fetch the revision from
            the Git repository; therefore make sure that the string you
            provide for ``revision`` is parsable by the command. For
            information on string values accepted by ``git fetch``, see
            https://git-scm.com/docs/gitrevisions#_specifying_revisions.
            For information on ``git fetch``, see
            https://git-scm.com/docs/git-fetch.
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=5,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=6,
    )


class RepoSource(proto.Message):
    r"""Location of the source in a Google Cloud Source Repository.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project_id (str):
            Optional. ID of the project that owns the
            Cloud Source Repository. If omitted, the project
            ID requesting the build is assumed.
        repo_name (str):
            Required. Name of the Cloud Source
            Repository.
        branch_name (str):
            Regex matching branches to build.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        tag_name (str):
            Regex matching tags to build.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        commit_sha (str):
            Explicit commit SHA to build.

            This field is a member of `oneof`_ ``revision``.
        dir_ (str):
            Optional. Directory, relative to the source root, in which
            to run the build.

            This must be a relative path. If a step's ``dir`` is
            specified and is an absolute path, this value is ignored for
            that step's execution.
        invert_regex (bool):
            Optional. Only trigger a build if the
            revision regex does NOT match the revision
            regex.
        substitutions (MutableMapping[str, str]):
            Optional. Substitutions to use in a triggered
            build. Should only be used with RunBuildTrigger
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repo_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    branch_name: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="revision",
    )
    tag_name: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="revision",
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="revision",
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=7,
    )
    invert_regex: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    substitutions: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class StorageSourceManifest(proto.Message):
    r"""Location of the source manifest in Cloud Storage. This feature is in
    Preview; see description
    `here <https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gcs-fetcher>`__.

    Attributes:
        bucket (str):
            Required. Cloud Storage bucket containing the source
            manifest (see `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
        object_ (str):
            Required. Cloud Storage object containing the
            source manifest.
            This object must be a JSON file.
        generation (int):
            Cloud Storage generation for the object. If
            the generation is omitted, the latest generation
            will be used.
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


class ConnectedRepository(proto.Message):
    r"""Location of the source in a 2nd-gen Google Cloud Build
    repository resource.

    Attributes:
        repository (str):
            Required. Name of the Google Cloud Build repository,
            formatted as
            ``projects/*/locations/*/connections/*/repositories/*``.
        dir_ (str):
            Optional. Directory, relative to the source
            root, in which to run the build.
        revision (str):
            Required. The revision to fetch from the Git
            repository such as a branch, a tag, a commit
            SHA, or any Git ref.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Source(proto.Message):
    r"""Location of the source in a supported storage service.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        storage_source (google.cloud.devtools.cloudbuild_v1.types.StorageSource):
            If provided, get the source from this
            location in Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        repo_source (google.cloud.devtools.cloudbuild_v1.types.RepoSource):
            If provided, get the source from this
            location in a Cloud Source Repository.

            This field is a member of `oneof`_ ``source``.
        git_source (google.cloud.devtools.cloudbuild_v1.types.GitSource):
            If provided, get the source from this Git
            repository.

            This field is a member of `oneof`_ ``source``.
        storage_source_manifest (google.cloud.devtools.cloudbuild_v1.types.StorageSourceManifest):
            If provided, get the source from this manifest in Cloud
            Storage. This feature is in Preview; see description
            `here <https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gcs-fetcher>`__.

            This field is a member of `oneof`_ ``source``.
        connected_repository (google.cloud.devtools.cloudbuild_v1.types.ConnectedRepository):
            Optional. If provided, get the source from
            this 2nd-gen Google Cloud Build repository
            resource.

            This field is a member of `oneof`_ ``source``.
    """

    storage_source: "StorageSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="StorageSource",
    )
    repo_source: "RepoSource" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="RepoSource",
    )
    git_source: "GitSource" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source",
        message="GitSource",
    )
    storage_source_manifest: "StorageSourceManifest" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="source",
        message="StorageSourceManifest",
    )
    connected_repository: "ConnectedRepository" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="source",
        message="ConnectedRepository",
    )


class BuiltImage(proto.Message):
    r"""An image built by the pipeline.

    Attributes:
        name (str):
            Name used to push the container image to Google Container
            Registry, as presented to ``docker push``.
        digest (str):
            Docker Registry 2.0 digest.
        push_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            pushing the specified image.
        artifact_registry_package (str):
            Output only. Path to the artifact in Artifact
            Registry.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    digest: str = proto.Field(
        proto.STRING,
        number=3,
    )
    push_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TimeSpan",
    )
    artifact_registry_package: str = proto.Field(
        proto.STRING,
        number=5,
    )


class UploadedPythonPackage(proto.Message):
    r"""Artifact uploaded using the PythonPackage directive.

    Attributes:
        uri (str):
            URI of the uploaded artifact.
        file_hashes (google.cloud.devtools.cloudbuild_v1.types.FileHashes):
            Hash types and values of the Python Artifact.
        push_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            pushing the specified artifact.
        artifact_registry_package (str):
            Output only. Path to the artifact in Artifact
            Registry.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_hashes: "FileHashes" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FileHashes",
    )
    push_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TimeSpan",
    )
    artifact_registry_package: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UploadedMavenArtifact(proto.Message):
    r"""A Maven artifact uploaded using the MavenArtifact directive.

    Attributes:
        uri (str):
            URI of the uploaded artifact.
        file_hashes (google.cloud.devtools.cloudbuild_v1.types.FileHashes):
            Hash types and values of the Maven Artifact.
        push_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            pushing the specified artifact.
        artifact_registry_package (str):
            Output only. Path to the artifact in Artifact
            Registry.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_hashes: "FileHashes" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FileHashes",
    )
    push_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TimeSpan",
    )
    artifact_registry_package: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UploadedGoModule(proto.Message):
    r"""A Go module artifact uploaded to Artifact Registry using the
    GoModule directive.

    Attributes:
        uri (str):
            URI of the uploaded artifact.
        file_hashes (google.cloud.devtools.cloudbuild_v1.types.FileHashes):
            Hash types and values of the Go Module
            Artifact.
        push_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            pushing the specified artifact.
        artifact_registry_package (str):
            Output only. Path to the artifact in Artifact
            Registry.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_hashes: "FileHashes" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FileHashes",
    )
    push_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TimeSpan",
    )
    artifact_registry_package: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UploadedNpmPackage(proto.Message):
    r"""An npm package uploaded to Artifact Registry using the
    NpmPackage directive.

    Attributes:
        uri (str):
            URI of the uploaded npm package.
        file_hashes (google.cloud.devtools.cloudbuild_v1.types.FileHashes):
            Hash types and values of the npm package.
        push_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            pushing the specified artifact.
        artifact_registry_package (str):
            Output only. Path to the artifact in Artifact
            Registry.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_hashes: "FileHashes" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FileHashes",
    )
    push_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TimeSpan",
    )
    artifact_registry_package: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BuildStep(proto.Message):
    r"""A step in the build pipeline.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the container image that will run this
            particular build step.

            If the image is available in the host's Docker daemon's
            cache, it will be run directly. If not, the host will
            attempt to pull the image first, using the builder service
            account's credentials if necessary.

            The Docker daemon's cache will already have the latest
            versions of all of the officially supported build steps
            (https://github.com/GoogleCloudPlatform/cloud-builders). The
            Docker daemon will also have cached many of the layers for
            some popular images, like "ubuntu", "debian", but they will
            be refreshed at the time you attempt to use them.

            If you built an image in a previous build step, it will be
            stored in the host's Docker daemon's cache and is available
            to use as the name for a later build step.
        env (MutableSequence[str]):
            A list of environment variable definitions to
            be used when running a step.
            The elements are of the form "KEY=VALUE" for the
            environment variable "KEY" being given the value
            "VALUE".
        args (MutableSequence[str]):
            A list of arguments that will be presented to the step when
            it is started.

            If the image used to run the step's container has an
            entrypoint, the ``args`` are used as arguments to that
            entrypoint. If the image does not define an entrypoint, the
            first element in args is used as the entrypoint, and the
            remainder will be used as arguments.
        dir_ (str):
            Working directory to use when running this step's container.

            If this value is a relative path, it is relative to the
            build's working directory. If this value is absolute, it may
            be outside the build's working directory, in which case the
            contents of the path may not be persisted across build step
            executions, unless a ``volume`` for that path is specified.

            If the build specifies a ``RepoSource`` with ``dir`` and a
            step with a ``dir``, which specifies an absolute path, the
            ``RepoSource`` ``dir`` is ignored for the step's execution.
        id (str):
            Unique identifier for this build step, used in ``wait_for``
            to reference this build step as a dependency.
        wait_for (MutableSequence[str]):
            The ID(s) of the step(s) that this build step depends on.
            This build step will not start until all the build steps in
            ``wait_for`` have completed successfully. If ``wait_for`` is
            empty, this build step will start when all previous build
            steps in the ``Build.Steps`` list have completed
            successfully.
        entrypoint (str):
            Entrypoint to be used instead of the build
            step image's default entrypoint. If unset, the
            image's default entrypoint is used.
        secret_env (MutableSequence[str]):
            A list of environment variables which are encrypted using a
            Cloud Key Management Service crypto key. These values must
            be specified in the build's ``Secret``.
        volumes (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Volume]):
            List of volumes to mount into the build step.

            Each volume is created as an empty volume prior
            to execution of the build step. Upon completion
            of the build, volumes and their contents are
            discarded.

            Using a named volume in only one step is not
            valid as it is indicative of a build request
            with an incorrect configuration.
        timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            executing this build step.
        pull_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Output only. Stores timing information for
            pulling this build step's builder image only.
        timeout (google.protobuf.duration_pb2.Duration):
            Time limit for executing this build step. If
            not defined, the step has no time limit and will
            be allowed to continue to run until either it
            completes or the build itself times out.
        status (google.cloud.devtools.cloudbuild_v1.types.Build.Status):
            Output only. Status of the build step. At
            this time, build step status is only updated on
            build completion; step status is not updated in
            real-time as the build progresses.
        allow_failure (bool):
            Allow this build step to fail without failing the entire
            build.

            If false, the entire build will fail if this step fails.
            Otherwise, the build will succeed, but this step will still
            have a failure status. Error information will be reported in
            the failure_detail field.
        exit_code (int):
            Output only. Return code from running the
            step.
        allow_exit_codes (MutableSequence[int]):
            Allow this build step to fail without failing the entire
            build if and only if the exit code is one of the specified
            codes. If allow_failure is also specified, this field will
            take precedence.
        script (str):
            A shell script to be executed in the step.

            When script is provided, the user cannot specify
            the entrypoint or args.
        automap_substitutions (bool):
            Option to include built-in and custom
            substitutions as env variables for this build
            step. This option will override the global
            option in BuildOption.

            This field is a member of `oneof`_ ``_automap_substitutions``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    env: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    wait_for: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    entrypoint: str = proto.Field(
        proto.STRING,
        number=7,
    )
    secret_env: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    volumes: MutableSequence["Volume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Volume",
    )
    timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="TimeSpan",
    )
    pull_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="TimeSpan",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=11,
        message=duration_pb2.Duration,
    )
    status: "Build.Status" = proto.Field(
        proto.ENUM,
        number=12,
        enum="Build.Status",
    )
    allow_failure: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    exit_code: int = proto.Field(
        proto.INT32,
        number=16,
    )
    allow_exit_codes: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=18,
    )
    script: str = proto.Field(
        proto.STRING,
        number=19,
    )
    automap_substitutions: bool = proto.Field(
        proto.BOOL,
        number=20,
        optional=True,
    )


class Volume(proto.Message):
    r"""Volume describes a Docker container volume which is mounted
    into build steps in order to persist files across build step
    execution.

    Attributes:
        name (str):
            Name of the volume to mount.

            Volume names must be unique per build step and
            must be valid names for Docker volumes. Each
            named volume must be used by at least two build
            steps.
        path (str):
            Path at which to mount the volume.

            Paths must be absolute and cannot conflict with
            other volume paths on the same build step or
            with certain reserved volume paths.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Results(proto.Message):
    r"""Artifacts created by the build pipeline.

    Attributes:
        images (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.BuiltImage]):
            Container images that were built as a part of
            the build.
        build_step_images (MutableSequence[str]):
            List of build step digests, in the order
            corresponding to build step indices.
        artifact_manifest (str):
            Path to the artifact manifest for
            non-container artifacts uploaded to Cloud
            Storage. Only populated when artifacts are
            uploaded to Cloud Storage.
        num_artifacts (int):
            Number of non-container artifacts uploaded to
            Cloud Storage. Only populated when artifacts are
            uploaded to Cloud Storage.
        build_step_outputs (MutableSequence[bytes]):
            List of build step outputs, produced by builder images, in
            the order corresponding to build step indices.

            `Cloud
            Builders <https://cloud.google.com/cloud-build/docs/cloud-builders>`__
            can produce this output by writing to
            ``$BUILDER_OUTPUT/output``. Only the first 50KB of data is
            stored. Note that the ``$BUILDER_OUTPUT`` variable is
            read-only and can't be substituted.
        artifact_timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
            Time to push all non-container artifacts to
            Cloud Storage.
        python_packages (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.UploadedPythonPackage]):
            Python artifacts uploaded to Artifact
            Registry at the end of the build.
        maven_artifacts (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.UploadedMavenArtifact]):
            Maven artifacts uploaded to Artifact Registry
            at the end of the build.
        go_modules (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.UploadedGoModule]):
            Optional. Go module artifacts uploaded to
            Artifact Registry at the end of the build.
        npm_packages (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.UploadedNpmPackage]):
            Npm packages uploaded to Artifact Registry at
            the end of the build.
    """

    images: MutableSequence["BuiltImage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="BuiltImage",
    )
    build_step_images: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    artifact_manifest: str = proto.Field(
        proto.STRING,
        number=4,
    )
    num_artifacts: int = proto.Field(
        proto.INT64,
        number=5,
    )
    build_step_outputs: MutableSequence[bytes] = proto.RepeatedField(
        proto.BYTES,
        number=6,
    )
    artifact_timing: "TimeSpan" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="TimeSpan",
    )
    python_packages: MutableSequence["UploadedPythonPackage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="UploadedPythonPackage",
    )
    maven_artifacts: MutableSequence["UploadedMavenArtifact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="UploadedMavenArtifact",
    )
    go_modules: MutableSequence["UploadedGoModule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="UploadedGoModule",
    )
    npm_packages: MutableSequence["UploadedNpmPackage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="UploadedNpmPackage",
    )


class ArtifactResult(proto.Message):
    r"""An artifact that was uploaded during a build. This
    is a single record in the artifact manifest JSON file.

    Attributes:
        location (str):
            The path of an artifact in a Cloud Storage bucket, with the
            generation number. For example,
            ``gs://mybucket/path/to/output.jar#generation``.
        file_hash (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.FileHashes]):
            The file hash of the artifact.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_hash: MutableSequence["FileHashes"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FileHashes",
    )


class Build(proto.Message):
    r"""A build resource in the Cloud Build API.

    At a high level, a ``Build`` describes where to find source code,
    how to build it (for example, the builder image to run on the
    source), and where to store the built artifacts.

    Fields can include the following variables, which will be expanded
    when the build is created:

    - $PROJECT_ID: the project ID of the build.
    - $PROJECT_NUMBER: the project number of the build.
    - $LOCATION: the location/region of the build.
    - $BUILD_ID: the autogenerated ID of the build.
    - $REPO_NAME: the source repository name specified by RepoSource.
    - $BRANCH_NAME: the branch name specified by RepoSource.
    - $TAG_NAME: the tag name specified by RepoSource.
    - $REVISION_ID or $COMMIT_SHA: the commit SHA specified by
      RepoSource or resolved from the specified branch or tag.
    - $SHORT_SHA: first 7 characters of $REVISION_ID or $COMMIT_SHA.

    Attributes:
        name (str):
            Output only. The 'Build' name with format:
            ``projects/{project}/locations/{location}/builds/{build}``,
            where {build} is a unique identifier generated by the
            service.
        id (str):
            Output only. Unique identifier of the build.
        project_id (str):
            Output only. ID of the project.
        status (google.cloud.devtools.cloudbuild_v1.types.Build.Status):
            Output only. Status of the build.
        status_detail (str):
            Output only. Customer-readable message about
            the current status.
        source (google.cloud.devtools.cloudbuild_v1.types.Source):
            Optional. The location of the source files to
            build.
        steps (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.BuildStep]):
            Required. The operations to be performed on
            the workspace.
        results (google.cloud.devtools.cloudbuild_v1.types.Results):
            Output only. Results of the build.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the request to
            create the build was received.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which execution of the
            build was started.
        finish_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which execution of the build was
            finished.

            The difference between finish_time and start_time is the
            duration of the build's execution.
        timeout (google.protobuf.duration_pb2.Duration):
            Amount of time that this build should be allowed to run, to
            second granularity. If this amount of time elapses, work on
            the build will cease and the build status will be
            ``TIMEOUT``.

            ``timeout`` starts ticking from ``startTime``.

            Default time is 60 minutes.
        images (MutableSequence[str]):
            A list of images to be pushed upon the successful completion
            of all build steps.

            The images are pushed using the builder service account's
            credentials.

            The digests of the pushed images will be stored in the
            ``Build`` resource's results field.

            If any of the images fail to be pushed, the build status is
            marked ``FAILURE``.
        queue_ttl (google.protobuf.duration_pb2.Duration):
            TTL in queue for this build. If provided and the build is
            enqueued longer than this value, the build will expire and
            the build status will be ``EXPIRED``.

            The TTL starts ticking from create_time.
        artifacts (google.cloud.devtools.cloudbuild_v1.types.Artifacts):
            Artifacts produced by the build that should
            be uploaded upon successful completion of all
            build steps.
        logs_bucket (str):
            Cloud Storage bucket where logs should be written (see
            `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
            Logs file names will be of the format
            ``${logs_bucket}/log-${build_id}.txt``.
        source_provenance (google.cloud.devtools.cloudbuild_v1.types.SourceProvenance):
            Output only. A permanent fixed identifier for
            source.
        build_trigger_id (str):
            Output only. The ID of the ``BuildTrigger`` that triggered
            this build, if it was triggered automatically.
        options (google.cloud.devtools.cloudbuild_v1.types.BuildOptions):
            Special options for this build.
        log_url (str):
            Output only. URL to logs for this build in
            Google Cloud Console.
        substitutions (MutableMapping[str, str]):
            Substitutions data for ``Build`` resource.
        tags (MutableSequence[str]):
            Tags for annotation of a ``Build``. These are not docker
            tags.
        secrets (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Secret]):
            Secrets to decrypt using Cloud Key Management Service. Note:
            Secret Manager is the recommended technique for managing
            sensitive data with Cloud Build. Use ``available_secrets``
            to configure builds to access secrets from Secret Manager.
            For instructions, see:
            https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets
        timing (MutableMapping[str, google.cloud.devtools.cloudbuild_v1.types.TimeSpan]):
            Output only. Stores timing information for phases of the
            build. Valid keys are:

            - BUILD: time to execute all build steps.
            - PUSH: time to push all artifacts including docker images
              and non docker artifacts.
            - FETCHSOURCE: time to fetch source.
            - SETUPBUILD: time to set up build.

            If the build does not specify source or images, these keys
            will not be included.
        approval (google.cloud.devtools.cloudbuild_v1.types.BuildApproval):
            Output only. Describes this build's approval
            configuration, status, and result.
        service_account (str):
            IAM service account whose credentials will be used at build
            runtime. Must be of the format
            ``projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}``. ACCOUNT
            can be email address or uniqueId of the service account.
        available_secrets (google.cloud.devtools.cloudbuild_v1.types.Secrets):
            Secrets and secret environment variables.
        warnings (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Build.Warning]):
            Output only. Non-fatal problems encountered
            during the execution of the build.
        git_config (google.cloud.devtools.cloudbuild_v1.types.GitConfig):
            Optional. Configuration for git operations.
        failure_info (google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo):
            Output only. Contains information about the
            build when status=FAILURE.
        dependencies (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Dependency]):
            Optional. Dependencies that the Cloud Build
            worker will fetch before executing user steps.
    """

    class Status(proto.Enum):
        r"""Possible status of a build or build step.

        Values:
            STATUS_UNKNOWN (0):
                Status of the build is unknown.
            PENDING (10):
                Build has been created and is pending
                execution and queuing. It has not been queued.
            QUEUED (1):
                Build or step is queued; work has not yet
                begun.
            WORKING (2):
                Build or step is being executed.
            SUCCESS (3):
                Build or step finished successfully.
            FAILURE (4):
                Build or step failed to complete
                successfully.
            INTERNAL_ERROR (5):
                Build or step failed due to an internal
                cause.
            TIMEOUT (6):
                Build or step took longer than was allowed.
            CANCELLED (7):
                Build or step was canceled by a user.
            EXPIRED (9):
                Build was enqueued for longer than the value of
                ``queue_ttl``.
        """

        STATUS_UNKNOWN = 0
        PENDING = 10
        QUEUED = 1
        WORKING = 2
        SUCCESS = 3
        FAILURE = 4
        INTERNAL_ERROR = 5
        TIMEOUT = 6
        CANCELLED = 7
        EXPIRED = 9

    class Warning(proto.Message):
        r"""A non-fatal problem encountered during the execution of the
        build.

        Attributes:
            text (str):
                Explanation of the warning generated.
            priority (google.cloud.devtools.cloudbuild_v1.types.Build.Warning.Priority):
                The priority for this warning.
        """

        class Priority(proto.Enum):
            r"""The relative importance of this warning.

            Values:
                PRIORITY_UNSPECIFIED (0):
                    Should not be used.
                INFO (1):
                    e.g. deprecation warnings and alternative
                    feature highlights.
                WARNING (2):
                    e.g. automated detection of possible issues
                    with the build.
                ALERT (3):
                    e.g. alerts that a feature used in the build
                    is pending removal
            """

            PRIORITY_UNSPECIFIED = 0
            INFO = 1
            WARNING = 2
            ALERT = 3

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        priority: "Build.Warning.Priority" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Build.Warning.Priority",
        )

    class FailureInfo(proto.Message):
        r"""A fatal problem encountered during the execution of the
        build.

        Attributes:
            type_ (google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo.FailureType):
                The name of the failure.
            detail (str):
                Explains the failure issue in more detail
                using hard-coded text.
        """

        class FailureType(proto.Enum):
            r"""The name of a fatal problem encountered during the execution
            of the build.

            Values:
                FAILURE_TYPE_UNSPECIFIED (0):
                    Type unspecified
                PUSH_FAILED (1):
                    Unable to push the image to the repository.
                PUSH_IMAGE_NOT_FOUND (2):
                    Final image not found.
                PUSH_NOT_AUTHORIZED (3):
                    Unauthorized push of the final image.
                LOGGING_FAILURE (4):
                    Backend logging failures. Should retry.
                USER_BUILD_STEP (5):
                    A build step has failed.
                FETCH_SOURCE_FAILED (6):
                    The source fetching has failed.
            """

            FAILURE_TYPE_UNSPECIFIED = 0
            PUSH_FAILED = 1
            PUSH_IMAGE_NOT_FOUND = 2
            PUSH_NOT_AUTHORIZED = 3
            LOGGING_FAILURE = 4
            USER_BUILD_STEP = 5
            FETCH_SOURCE_FAILED = 6

        type_: "Build.FailureInfo.FailureType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Build.FailureInfo.FailureType",
        )
        detail: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=45,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=16,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=2,
        enum=Status,
    )
    status_detail: str = proto.Field(
        proto.STRING,
        number=24,
    )
    source: "Source" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Source",
    )
    steps: MutableSequence["BuildStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="BuildStep",
    )
    results: "Results" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Results",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    finish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )
    images: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    queue_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=40,
        message=duration_pb2.Duration,
    )
    artifacts: "Artifacts" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="Artifacts",
    )
    logs_bucket: str = proto.Field(
        proto.STRING,
        number=19,
    )
    source_provenance: "SourceProvenance" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="SourceProvenance",
    )
    build_trigger_id: str = proto.Field(
        proto.STRING,
        number=22,
    )
    options: "BuildOptions" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="BuildOptions",
    )
    log_url: str = proto.Field(
        proto.STRING,
        number=25,
    )
    substitutions: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=29,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=31,
    )
    secrets: MutableSequence["Secret"] = proto.RepeatedField(
        proto.MESSAGE,
        number=32,
        message="Secret",
    )
    timing: MutableMapping[str, "TimeSpan"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=33,
        message="TimeSpan",
    )
    approval: "BuildApproval" = proto.Field(
        proto.MESSAGE,
        number=44,
        message="BuildApproval",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=42,
    )
    available_secrets: "Secrets" = proto.Field(
        proto.MESSAGE,
        number=47,
        message="Secrets",
    )
    warnings: MutableSequence[Warning] = proto.RepeatedField(
        proto.MESSAGE,
        number=49,
        message=Warning,
    )
    git_config: "GitConfig" = proto.Field(
        proto.MESSAGE,
        number=48,
        message="GitConfig",
    )
    failure_info: FailureInfo = proto.Field(
        proto.MESSAGE,
        number=51,
        message=FailureInfo,
    )
    dependencies: MutableSequence["Dependency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=56,
        message="Dependency",
    )


class Dependency(proto.Message):
    r"""A dependency that the Cloud Build worker will fetch before
    executing user steps.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        empty (bool):
            If set to true disable all dependency
            fetching (ignoring the default source as well).

            This field is a member of `oneof`_ ``dep``.
        git_source (google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceDependency):
            Represents a git repository as a build
            dependency.

            This field is a member of `oneof`_ ``dep``.
    """

    class GitSourceDependency(proto.Message):
        r"""Represents a git repository as a build dependency.

        Attributes:
            repository (google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceRepository):
                Required. The kind of repo (url or dev
                connect).
            revision (str):
                Required. The revision that we will fetch the
                repo at.
            recurse_submodules (bool):
                Optional. True if submodules should be
                fetched too (default false).
            depth (int):
                Optional. How much history should be fetched
                for the build (default 1, -1 for all history).
            dest_path (str):
                Required. Where should the files be placed on
                the worker.
            fetch_tags (bool):
                Optional. True if remote tags should be
                fetched too (default false). Note: when depth is
                1 (default), git fetch only retrieves tags
                pointing to commits within the shallow boundary.
                Set depth to -1 to fetch all historical tags.
        """

        repository: "Dependency.GitSourceRepository" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Dependency.GitSourceRepository",
        )
        revision: str = proto.Field(
            proto.STRING,
            number=2,
        )
        recurse_submodules: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        depth: int = proto.Field(
            proto.INT64,
            number=4,
        )
        dest_path: str = proto.Field(
            proto.STRING,
            number=5,
        )
        fetch_tags: bool = proto.Field(
            proto.BOOL,
            number=6,
        )

    class GitSourceRepository(proto.Message):
        r"""A repository for a git source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            url (str):
                Location of the Git repository.

                This field is a member of `oneof`_ ``repotype``.
            developer_connect (str):
                The Developer Connect Git repository link formatted as
                ``projects/*/locations/*/connections/*/gitRepositoryLink/*``

                This field is a member of `oneof`_ ``repotype``.
        """

        url: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="repotype",
        )
        developer_connect: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="repotype",
        )

    empty: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="dep",
    )
    git_source: GitSourceDependency = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="dep",
        message=GitSourceDependency,
    )


class GitConfig(proto.Message):
    r"""GitConfig is a configuration for git operations.

    Attributes:
        http (google.cloud.devtools.cloudbuild_v1.types.GitConfig.HttpConfig):
            Configuration for HTTP related git
            operations.
    """

    class HttpConfig(proto.Message):
        r"""HttpConfig is a configuration for HTTP related git
        operations.

        Attributes:
            proxy_secret_version_name (str):
                SecretVersion resource of the HTTP proxy URL. The Service
                Account used in the build (either the default Service
                Account or user-specified Service Account) should have
                ``secretmanager.versions.access`` permissions on this
                secret. The proxy URL should be in format
                ``[protocol://][user[:password]@]proxyhost[:port]``.
        """

        proxy_secret_version_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    http: HttpConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=HttpConfig,
    )


class Artifacts(proto.Message):
    r"""Artifacts produced by a build that should be uploaded upon
    successful completion of all build steps.

    Attributes:
        images (MutableSequence[str]):
            A list of images to be pushed upon the
            successful completion of all build steps.

            The images will be pushed using the builder
            service account's credentials.

            The digests of the pushed images will be stored
            in the Build resource's results field.

            If any of the images fail to be pushed, the
            build is marked FAILURE.
        objects (google.cloud.devtools.cloudbuild_v1.types.Artifacts.ArtifactObjects):
            A list of objects to be uploaded to Cloud
            Storage upon successful completion of all build
            steps.

            Files in the workspace matching specified paths
            globs will be uploaded to the specified Cloud
            Storage location using the builder service
            account's credentials.

            The location and generation of the uploaded
            objects will be stored in the Build resource's
            results field.

            If any objects fail to be pushed, the build is
            marked FAILURE.
        maven_artifacts (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Artifacts.MavenArtifact]):
            A list of Maven artifacts to be uploaded to
            Artifact Registry upon successful completion of
            all build steps.

            Artifacts in the workspace matching specified
            paths globs will be uploaded to the specified
            Artifact Registry repository using the builder
            service account's credentials.

            If any artifacts fail to be pushed, the build is
            marked FAILURE.
        go_modules (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Artifacts.GoModule]):
            Optional. A list of Go modules to be uploaded
            to Artifact Registry upon successful completion
            of all build steps.

            If any objects fail to be pushed, the build is
            marked FAILURE.
        python_packages (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Artifacts.PythonPackage]):
            A list of Python packages to be uploaded to
            Artifact Registry upon successful completion of
            all build steps.

            The build service account credentials will be
            used to perform the upload.

            If any objects fail to be pushed, the build is
            marked FAILURE.
        npm_packages (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Artifacts.NpmPackage]):
            A list of npm packages to be uploaded to
            Artifact Registry upon successful completion of
            all build steps.

            Npm packages in the specified paths will be
            uploaded to the specified Artifact Registry
            repository using the builder service account's
            credentials.

            If any packages fail to be pushed, the build is
            marked FAILURE.
    """

    class ArtifactObjects(proto.Message):
        r"""Files in the workspace to upload to Cloud Storage upon
        successful completion of all build steps.

        Attributes:
            location (str):
                Cloud Storage bucket and optional object path, in the form
                "gs://bucket/path/to/somewhere/". (see `Bucket Name
                Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).

                Files in the workspace matching any path pattern will be
                uploaded to Cloud Storage with this location as a prefix.
            paths (MutableSequence[str]):
                Path globs used to match files in the build's
                workspace.
            timing (google.cloud.devtools.cloudbuild_v1.types.TimeSpan):
                Output only. Stores timing information for
                pushing all artifact objects.
        """

        location: str = proto.Field(
            proto.STRING,
            number=1,
        )
        paths: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        timing: "TimeSpan" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="TimeSpan",
        )

    class MavenArtifact(proto.Message):
        r"""A Maven artifact to upload to Artifact Registry upon
        successful completion of all build steps.

        Attributes:
            repository (str):
                Artifact Registry repository, in the form
                "https://$REGION-maven.pkg.dev/$PROJECT/$REPOSITORY"

                Artifact in the workspace specified by path will
                be uploaded to Artifact Registry with this
                location as a prefix.
            path (str):
                Optional. Path to an artifact in the build's
                workspace to be uploaded to Artifact Registry.
                This can be either an absolute path,
                e.g.
                /workspace/my-app/target/my-app-1.0.SNAPSHOT.jar
                or a relative path from /workspace,
                e.g. my-app/target/my-app-1.0.SNAPSHOT.jar.
            artifact_id (str):
                Maven ``artifactId`` value used when uploading the artifact
                to Artifact Registry.
            group_id (str):
                Maven ``groupId`` value used when uploading the artifact to
                Artifact Registry.
            version (str):
                Maven ``version`` value used when uploading the artifact to
                Artifact Registry.
        """

        repository: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        artifact_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        group_id: str = proto.Field(
            proto.STRING,
            number=4,
        )
        version: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class GoModule(proto.Message):
        r"""Go module to upload to Artifact Registry upon successful
        completion of all build steps. A module refers to all
        dependencies in a go.mod file.

        Attributes:
            repository_name (str):
                Optional. Artifact Registry repository name.

                Specified Go modules will be zipped and uploaded
                to Artifact Registry with this location as a
                prefix.
                e.g. my-go-repo
            repository_location (str):
                Optional. Location of the Artifact Registry
                repository. i.e. us-east1 Defaults to the
                build’s location.
            repository_project_id (str):
                Optional. Project ID of the Artifact Registry
                repository. Defaults to the build project.
            source_path (str):
                Optional. Source path of the go.mod file in
                the build's workspace. If not specified, this
                will default to the current directory. e.g.
                ~/code/go/mypackage
            module_path (str):
                Optional. The Go module's "module path".
                e.g. example.com/foo/v2
            module_version (str):
                Optional. The Go module's semantic version in
                the form vX.Y.Z. e.g. v0.1.1 Pre-release
                identifiers can also be added by appending a
                dash and dot separated ASCII alphanumeric
                characters and hyphens. e.g.
                v0.2.3-alpha.x.12m.5
        """

        repository_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        repository_location: str = proto.Field(
            proto.STRING,
            number=2,
        )
        repository_project_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        source_path: str = proto.Field(
            proto.STRING,
            number=4,
        )
        module_path: str = proto.Field(
            proto.STRING,
            number=5,
        )
        module_version: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class PythonPackage(proto.Message):
        r"""Python package to upload to Artifact Registry upon successful
        completion of all build steps. A package can encapsulate
        multiple objects to be uploaded to a single repository.

        Attributes:
            repository (str):
                Artifact Registry repository, in the form
                "https://$REGION-python.pkg.dev/$PROJECT/$REPOSITORY"

                Files in the workspace matching any path pattern
                will be uploaded to Artifact Registry with this
                location as a prefix.
            paths (MutableSequence[str]):
                Path globs used to match files in the build's workspace. For
                Python/ Twine, this is usually ``dist/*``, and sometimes
                additionally an ``.asc`` file.
        """

        repository: str = proto.Field(
            proto.STRING,
            number=1,
        )
        paths: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class NpmPackage(proto.Message):
        r"""Npm package to upload to Artifact Registry upon successful
        completion of all build steps.

        Attributes:
            repository (str):
                Artifact Registry repository, in the form
                "https://$REGION-npm.pkg.dev/$PROJECT/$REPOSITORY"

                Npm package in the workspace specified by path
                will be zipped and uploaded to Artifact Registry
                with this location as a prefix.
            package_path (str):
                Optional. Path to the package.json. e.g.
                workspace/path/to/package

                Only one of ``archive`` or ``package_path`` can be
                specified.
        """

        repository: str = proto.Field(
            proto.STRING,
            number=1,
        )
        package_path: str = proto.Field(
            proto.STRING,
            number=2,
        )

    images: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    objects: ArtifactObjects = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ArtifactObjects,
    )
    maven_artifacts: MutableSequence[MavenArtifact] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=MavenArtifact,
    )
    go_modules: MutableSequence[GoModule] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=GoModule,
    )
    python_packages: MutableSequence[PythonPackage] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=PythonPackage,
    )
    npm_packages: MutableSequence[NpmPackage] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=NpmPackage,
    )


class TimeSpan(proto.Message):
    r"""Start and end times for a build execution phase.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start of time span.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End of time span.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class BuildOperationMetadata(proto.Message):
    r"""Metadata for build operations.

    Attributes:
        build (google.cloud.devtools.cloudbuild_v1.types.Build):
            The build that the operation is tracking.
    """

    build: "Build" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Build",
    )


class SourceProvenance(proto.Message):
    r"""Provenance of the source. Ways to find the original source,
    or verify that some source was used for this build.

    Attributes:
        resolved_storage_source (google.cloud.devtools.cloudbuild_v1.types.StorageSource):
            A copy of the build's ``source.storage_source``, if exists,
            with any generations resolved.
        resolved_repo_source (google.cloud.devtools.cloudbuild_v1.types.RepoSource):
            A copy of the build's ``source.repo_source``, if exists,
            with any revisions resolved.
        resolved_storage_source_manifest (google.cloud.devtools.cloudbuild_v1.types.StorageSourceManifest):
            A copy of the build's ``source.storage_source_manifest``, if
            exists, with any revisions resolved. This feature is in
            Preview.
        resolved_connected_repository (google.cloud.devtools.cloudbuild_v1.types.ConnectedRepository):
            Output only. A copy of the build's
            ``source.connected_repository``, if exists, with any
            revisions resolved.
        resolved_git_source (google.cloud.devtools.cloudbuild_v1.types.GitSource):
            Output only. A copy of the build's ``source.git_source``, if
            exists, with any revisions resolved.
        file_hashes (MutableMapping[str, google.cloud.devtools.cloudbuild_v1.types.FileHashes]):
            Output only. Hash(es) of the build source, which can be used
            to verify that the original source integrity was maintained
            in the build. Note that ``FileHashes`` will only be
            populated if ``BuildOptions`` has requested a
            ``SourceProvenanceHash``.

            The keys to this map are file paths used as build source and
            the values contain the hash values for those files.

            If the build source came in a single package such as a
            gzipped tarfile (``.tar.gz``), the ``FileHash`` will be for
            the single path to that file.
    """

    resolved_storage_source: "StorageSource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="StorageSource",
    )
    resolved_repo_source: "RepoSource" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RepoSource",
    )
    resolved_storage_source_manifest: "StorageSourceManifest" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="StorageSourceManifest",
    )
    resolved_connected_repository: "ConnectedRepository" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ConnectedRepository",
    )
    resolved_git_source: "GitSource" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="GitSource",
    )
    file_hashes: MutableMapping[str, "FileHashes"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message="FileHashes",
    )


class FileHashes(proto.Message):
    r"""Container message for hashes of byte content of files, used
    in SourceProvenance messages to verify integrity of source input
    to the build.

    Attributes:
        file_hash (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Hash]):
            Collection of file hashes.
    """

    file_hash: MutableSequence["Hash"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Hash",
    )


class Hash(proto.Message):
    r"""Container message for hash values.

    Attributes:
        type_ (google.cloud.devtools.cloudbuild_v1.types.Hash.HashType):
            The type of hash that was performed.
        value (bytes):
            The hash value.
    """

    class HashType(proto.Enum):
        r"""Specifies the hash algorithm, if any.

        Values:
            NONE (0):
                No hash requested.
            SHA256 (1):
                Use a sha256 hash.
            MD5 (2):
                Use a md5 hash.
            GO_MODULE_H1 (3):
                Dirhash of a Go module's source code which is
                then hex-encoded.
            SHA512 (4):
                Use a sha512 hash.
        """

        NONE = 0
        SHA256 = 1
        MD5 = 2
        GO_MODULE_H1 = 3
        SHA512 = 4

    type_: HashType = proto.Field(
        proto.ENUM,
        number=1,
        enum=HashType,
    )
    value: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class Secrets(proto.Message):
    r"""Secrets and secret environment variables.

    Attributes:
        secret_manager (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.SecretManagerSecret]):
            Secrets in Secret Manager and associated
            secret environment variable.
        inline (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.InlineSecret]):
            Secrets encrypted with KMS key and the
            associated secret environment variable.
    """

    secret_manager: MutableSequence["SecretManagerSecret"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SecretManagerSecret",
    )
    inline: MutableSequence["InlineSecret"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="InlineSecret",
    )


class InlineSecret(proto.Message):
    r"""Pairs a set of secret environment variables mapped to
    encrypted values with the Cloud KMS key to use to decrypt the
    value.

    Attributes:
        kms_key_name (str):
            Resource name of Cloud KMS crypto key to decrypt the
            encrypted value. In format:
            projects/*/locations/*/keyRings/*/cryptoKeys/*
        env_map (MutableMapping[str, bytes]):
            Map of environment variable name to its
            encrypted value.
            Secret environment variables must be unique
            across all of a build's secrets, and must be
            used by at least one build step. Values can be
            at most 64 KB in size. There can be at most 100
            secret values across all of a build's secrets.
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    env_map: MutableMapping[str, bytes] = proto.MapField(
        proto.STRING,
        proto.BYTES,
        number=2,
    )


class SecretManagerSecret(proto.Message):
    r"""Pairs a secret environment variable with a SecretVersion in
    Secret Manager.

    Attributes:
        version_name (str):
            Resource name of the SecretVersion. In format:
            projects/*/secrets/*/versions/\*
        env (str):
            Environment variable name to associate with
            the secret. Secret environment variables must be
            unique across all of a build's secrets, and must
            be used by at least one build step.
    """

    version_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    env: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Secret(proto.Message):
    r"""Pairs a set of secret environment variables containing encrypted
    values with the Cloud KMS key to use to decrypt the value. Note: Use
    ``kmsKeyName`` with ``available_secrets`` instead of using
    ``kmsKeyName`` with ``secret``. For instructions see:
    https://cloud.google.com/cloud-build/docs/securing-builds/use-encrypted-credentials.

    Attributes:
        kms_key_name (str):
            Cloud KMS key name to use to decrypt these
            envs.
        secret_env (MutableMapping[str, bytes]):
            Map of environment variable name to its
            encrypted value.
            Secret environment variables must be unique
            across all of a build's secrets, and must be
            used by at least one build step. Values can be
            at most 64 KB in size. There can be at most 100
            secret values across all of a build's secrets.
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_env: MutableMapping[str, bytes] = proto.MapField(
        proto.STRING,
        proto.BYTES,
        number=3,
    )


class CreateBuildRequest(proto.Message):
    r"""Request to create a new build.

    Attributes:
        parent (str):
            The parent resource where this build will be created.
            Format: ``projects/{project}/locations/{location}``
        project_id (str):
            Required. ID of the project.
        build (google.cloud.devtools.cloudbuild_v1.types.Build):
            Required. Build resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    build: "Build" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Build",
    )


class GetBuildRequest(proto.Message):
    r"""Request to get a build.

    Attributes:
        name (str):
            The name of the ``Build`` to retrieve. Format:
            ``projects/{project}/locations/{location}/builds/{build}``
        project_id (str):
            Required. ID of the project.
        id (str):
            Required. ID of the build.
    """

    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListBuildsRequest(proto.Message):
    r"""Request to list builds.

    Attributes:
        parent (str):
            The parent of the collection of ``Builds``. Format:
            ``projects/{project}/locations/{location}``
        project_id (str):
            Required. ID of the project.
        page_size (int):
            Number of results to return in the list.
        page_token (str):
            The page token for the next page of Builds.

            If unspecified, the first page of results is returned.

            If the token is rejected for any reason, INVALID_ARGUMENT
            will be thrown. In this case, the token should be discarded,
            and pagination should be restarted from the first page of
            results.

            See https://google.aip.dev/158 for more.
        filter (str):
            The raw filter text to constrain the results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=9,
    )
    project_id: str = proto.Field(
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
        number=8,
    )


class ListBuildsResponse(proto.Message):
    r"""Response including listed builds.

    Attributes:
        builds (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Build]):
            Builds will be sorted by ``create_time``, descending.
        next_page_token (str):
            Token to receive the next page of results.
            This will be absent if the end of the response
            list has been reached.
    """

    @property
    def raw_page(self):
        return self

    builds: MutableSequence["Build"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Build",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CancelBuildRequest(proto.Message):
    r"""Request to cancel an ongoing build.

    Attributes:
        name (str):
            The name of the ``Build`` to cancel. Format:
            ``projects/{project}/locations/{location}/builds/{build}``
        project_id (str):
            Required. ID of the project.
        id (str):
            Required. ID of the build.
    """

    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ApproveBuildRequest(proto.Message):
    r"""Request to approve or reject a pending build.

    Attributes:
        name (str):
            Required. Name of the target build. For example:
            "projects/{$project_id}/builds/{$build_id}".
        approval_result (google.cloud.devtools.cloudbuild_v1.types.ApprovalResult):
            Approval decision and metadata.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    approval_result: "ApprovalResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ApprovalResult",
    )


class BuildApproval(proto.Message):
    r"""BuildApproval describes a build's approval configuration,
    state, and result.

    Attributes:
        state (google.cloud.devtools.cloudbuild_v1.types.BuildApproval.State):
            Output only. The state of this build's
            approval.
        config (google.cloud.devtools.cloudbuild_v1.types.ApprovalConfig):
            Output only. Configuration for manual
            approval of this build.
        result (google.cloud.devtools.cloudbuild_v1.types.ApprovalResult):
            Output only. Result of manual approval for
            this Build.
    """

    class State(proto.Enum):
        r"""Specifies the current state of a build's approval.

        Values:
            STATE_UNSPECIFIED (0):
                Default enum type. This should not be used.
            PENDING (1):
                Build approval is pending.
            APPROVED (2):
                Build approval has been approved.
            REJECTED (3):
                Build approval has been rejected.
            CANCELLED (5):
                Build was cancelled while it was still
                pending approval.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        APPROVED = 2
        REJECTED = 3
        CANCELLED = 5

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    config: "ApprovalConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ApprovalConfig",
    )
    result: "ApprovalResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ApprovalResult",
    )


class ApprovalConfig(proto.Message):
    r"""ApprovalConfig describes configuration for manual approval of
    a build.

    Attributes:
        approval_required (bool):
            Whether or not approval is needed. If this is
            set on a build, it will become pending when
            created, and will need to be explicitly approved
            to start.
    """

    approval_required: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ApprovalResult(proto.Message):
    r"""ApprovalResult describes the decision and associated metadata
    of a manual approval of a build.

    Attributes:
        approver_account (str):
            Output only. Email of the user that called
            the ApproveBuild API to approve or reject a
            build at the time that the API was called.
        approval_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the approval
            decision was made.
        decision (google.cloud.devtools.cloudbuild_v1.types.ApprovalResult.Decision):
            Required. The decision of this manual
            approval.
        comment (str):
            Optional. An optional comment for this manual
            approval result.
        url (str):
            Optional. An optional URL tied to this manual
            approval result. This field is essentially the
            same as comment, except that it will be rendered
            by the UI differently. An example use case is a
            link to an external job that approved this
            Build.
    """

    class Decision(proto.Enum):
        r"""Specifies whether or not this manual approval result is to
        approve or reject a build.

        Values:
            DECISION_UNSPECIFIED (0):
                Default enum type. This should not be used.
            APPROVED (1):
                Build is approved.
            REJECTED (2):
                Build is rejected.
        """

        DECISION_UNSPECIFIED = 0
        APPROVED = 1
        REJECTED = 2

    approver_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    approval_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    decision: Decision = proto.Field(
        proto.ENUM,
        number=4,
        enum=Decision,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=5,
    )
    url: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GitRepoSource(proto.Message):
    r"""GitRepoSource describes a repo and ref of a code repository.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            The URI of the repo (e.g. https://github.com/user/repo.git).
            Either ``uri`` or ``repository`` can be specified and is
            required.
        repository (str):
            The connected repository resource name, in the format
            ``projects/*/locations/*/connections/*/repositories/*``.
            Either ``uri`` or ``repository`` can be specified and is
            required.

            This field is a member of `oneof`_ ``source``.
        ref (str):
            The branch or tag to use. Must start with
            "refs/" (required).
        repo_type (google.cloud.devtools.cloudbuild_v1.types.GitFileSource.RepoType):
            See RepoType below.
        github_enterprise_config (str):
            The full resource name of the github enterprise config.
            Format:
            ``projects/{project}/locations/{location}/githubEnterpriseConfigs/{id}``.
            ``projects/{project}/githubEnterpriseConfigs/{id}``.

            This field is a member of `oneof`_ ``enterprise_config``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repository: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="source",
    )
    ref: str = proto.Field(
        proto.STRING,
        number=2,
    )
    repo_type: "GitFileSource.RepoType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="GitFileSource.RepoType",
    )
    github_enterprise_config: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="enterprise_config",
    )


class GitFileSource(proto.Message):
    r"""GitFileSource describes a file within a (possibly remote)
    code repository.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        path (str):
            The path of the file, with the repo root as
            the root of the path.
        uri (str):
            The URI of the repo.
            Either uri or repository can be specified.
            If unspecified, the repo from which the trigger
            invocation originated is assumed to be the repo
            from which to read the specified path.
        repository (str):
            The fully qualified resource name of the
            Repos API repository. Either URI or repository
            can be specified. If unspecified, the repo from
            which the trigger invocation originated is
            assumed to be the repo from which to read the
            specified path.

            This field is a member of `oneof`_ ``source``.
        repo_type (google.cloud.devtools.cloudbuild_v1.types.GitFileSource.RepoType):
            See RepoType above.
        revision (str):
            The branch, tag, arbitrary ref, or SHA
            version of the repo to use when resolving the
            filename (optional). This field respects the
            same syntax/resolution as described here:

            https://git-scm.com/docs/gitrevisions
            If unspecified, the revision from which the
            trigger invocation originated is assumed to be
            the revision from which to read the specified
            path.
        github_enterprise_config (str):
            The full resource name of the github enterprise config.
            Format:
            ``projects/{project}/locations/{location}/githubEnterpriseConfigs/{id}``.
            ``projects/{project}/githubEnterpriseConfigs/{id}``.

            This field is a member of `oneof`_ ``enterprise_config``.
    """

    class RepoType(proto.Enum):
        r"""The type of the repo, since it may not be explicit from the ``repo``
        field (e.g from a URL).

        Values:
            UNKNOWN (0):
                The default, unknown repo type. Don't use it,
                instead use one of the other repo types.
            CLOUD_SOURCE_REPOSITORIES (1):
                A Google Cloud Source Repositories-hosted
                repo.
            GITHUB (2):
                A GitHub-hosted repo not necessarily on
                "github.com" (i.e. GitHub Enterprise).
            BITBUCKET_SERVER (3):
                A Bitbucket Server-hosted repo.
            GITLAB (4):
                A GitLab-hosted repo.
        """

        UNKNOWN = 0
        CLOUD_SOURCE_REPOSITORIES = 1
        GITHUB = 2
        BITBUCKET_SERVER = 3
        GITLAB = 4

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    repository: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="source",
    )
    repo_type: RepoType = proto.Field(
        proto.ENUM,
        number=3,
        enum=RepoType,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=4,
    )
    github_enterprise_config: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="enterprise_config",
    )


class BuildTrigger(proto.Message):
    r"""Configuration for an automated build in response to source
    repository changes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            The ``Trigger`` name with format:
            ``projects/{project}/locations/{location}/triggers/{trigger}``,
            where {trigger} is a unique identifier generated by the
            service.
        id (str):
            Output only. Unique identifier of the
            trigger.
        description (str):
            Human-readable description of this trigger.
        name (str):
            User-assigned name of the trigger. Must be
            unique within the project. Trigger names must
            meet the following requirements:

            + They must contain only alphanumeric characters
              and dashes.
            + They can be 1-64 characters long.
            + They must begin and end with an alphanumeric
              character.
        tags (MutableSequence[str]):
            Tags for annotation of a ``BuildTrigger``
        trigger_template (google.cloud.devtools.cloudbuild_v1.types.RepoSource):
            Template describing the types of source changes to trigger a
            build.

            Branch and tag names in trigger templates are interpreted as
            regular expressions. Any branch or tag change that matches
            that regular expression will trigger a build.

            Mutually exclusive with ``github``.
        github (google.cloud.devtools.cloudbuild_v1.types.GitHubEventsConfig):
            GitHubEventsConfig describes the configuration of a trigger
            that creates a build whenever a GitHub event is received.

            Mutually exclusive with ``trigger_template``.
        pubsub_config (google.cloud.devtools.cloudbuild_v1.types.PubsubConfig):
            PubsubConfig describes the configuration of a
            trigger that creates a build whenever a Pub/Sub
            message is published.
        webhook_config (google.cloud.devtools.cloudbuild_v1.types.WebhookConfig):
            WebhookConfig describes the configuration of
            a trigger that creates a build whenever a
            webhook is sent to a trigger's webhook URL.
        autodetect (bool):
            Autodetect build configuration.  The
            following precedence is used (case insensitive):

            1. cloudbuild.yaml
            2. cloudbuild.yml
            3. cloudbuild.json
            4. Dockerfile

            Currently only available for GitHub App
            Triggers.

            This field is a member of `oneof`_ ``build_template``.
        build (google.cloud.devtools.cloudbuild_v1.types.Build):
            Contents of the build template.

            This field is a member of `oneof`_ ``build_template``.
        filename (str):
            Path, from the source root, to the build
            configuration file (i.e. cloudbuild.yaml).

            This field is a member of `oneof`_ ``build_template``.
        git_file_source (google.cloud.devtools.cloudbuild_v1.types.GitFileSource):
            The file source describing the local or
            remote Build template.

            This field is a member of `oneof`_ ``build_template``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the trigger was
            created.
        disabled (bool):
            If true, the trigger will never automatically
            execute a build.
        substitutions (MutableMapping[str, str]):
            Substitutions for Build resource. The keys must match the
            following regular expression: ``^_[A-Z0-9_]+$``.
        ignored_files (MutableSequence[str]):
            ignored_files and included_files are file glob matches using
            https://golang.org/pkg/path/filepath/#Match extended with
            support for "\*\*".

            If ignored_files and changed files are both empty, then they
            are not used to determine whether or not to trigger a build.

            If ignored_files is not empty, then we ignore any files that
            match any of the ignored_file globs. If the change has no
            files that are outside of the ignored_files globs, then we
            do not trigger a build.
        included_files (MutableSequence[str]):
            If any of the files altered in the commit pass the
            ignored_files filter and included_files is empty, then as
            far as this filter is concerned, we should trigger the
            build.

            If any of the files altered in the commit pass the
            ignored_files filter and included_files is not empty, then
            we make sure that at least one of those files matches a
            included_files glob. If not, then we do not trigger a build.
        filter (str):
            Optional. A Common Expression Language
            string.
        source_to_build (google.cloud.devtools.cloudbuild_v1.types.GitRepoSource):
            The repo and ref of the repository from which
            to build. This field is used only for those
            triggers that do not respond to SCM events.
            Triggers that respond to such events build
            source at whatever commit caused the event.
            This field is currently only used by Webhook,
            Pub/Sub, Manual, and Cron triggers.
        approval_config (google.cloud.devtools.cloudbuild_v1.types.ApprovalConfig):
            Configuration for manual approval to start a
            build invocation of this BuildTrigger.
        service_account (str):
            The service account used for all user-controlled operations
            including UpdateBuildTrigger, RunBuildTrigger, CreateBuild,
            and CancelBuild. If no service account is set and the legacy
            Cloud Build service account
            (``[PROJECT_NUM]@cloudbuild.gserviceaccount.com``) is the
            default for the project then it will be used instead.
            Format:
            ``projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}``
        repository_event_config (google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig):
            The configuration of a trigger that creates a
            build whenever an event from Repo API is
            received.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=34,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=10,
    )
    name: str = proto.Field(
        proto.STRING,
        number=21,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=19,
    )
    trigger_template: "RepoSource" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="RepoSource",
    )
    github: "GitHubEventsConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="GitHubEventsConfig",
    )
    pubsub_config: "PubsubConfig" = proto.Field(
        proto.MESSAGE,
        number=29,
        message="PubsubConfig",
    )
    webhook_config: "WebhookConfig" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="WebhookConfig",
    )
    autodetect: bool = proto.Field(
        proto.BOOL,
        number=18,
        oneof="build_template",
    )
    build: "Build" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="build_template",
        message="Build",
    )
    filename: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="build_template",
    )
    git_file_source: "GitFileSource" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="build_template",
        message="GitFileSource",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    substitutions: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    ignored_files: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    included_files: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=30,
    )
    source_to_build: "GitRepoSource" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="GitRepoSource",
    )
    approval_config: "ApprovalConfig" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="ApprovalConfig",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=33,
    )
    repository_event_config: "RepositoryEventConfig" = proto.Field(
        proto.MESSAGE,
        number=39,
        message="RepositoryEventConfig",
    )


class RepositoryEventConfig(proto.Message):
    r"""The configuration of a trigger that creates a build whenever
    an event from Repo API is received.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        repository (str):
            The resource name of the Repo API resource.
        repository_type (google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig.RepositoryType):
            Output only. The type of the SCM vendor the
            repository points to.
        pull_request (google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter):
            Filter to match changes in pull requests.

            This field is a member of `oneof`_ ``filter``.
        push (google.cloud.devtools.cloudbuild_v1.types.PushFilter):
            Filter to match changes in refs like
            branches, tags.

            This field is a member of `oneof`_ ``filter``.
    """

    class RepositoryType(proto.Enum):
        r"""All possible SCM repo types from Repo API.

        Values:
            REPOSITORY_TYPE_UNSPECIFIED (0):
                If unspecified, RepositoryType defaults to
                GITHUB.
            GITHUB (1):
                The SCM repo is GITHUB.
            GITHUB_ENTERPRISE (2):
                The SCM repo is GITHUB Enterprise.
            GITLAB_ENTERPRISE (3):
                The SCM repo is GITLAB Enterprise.
        """

        REPOSITORY_TYPE_UNSPECIFIED = 0
        GITHUB = 1
        GITHUB_ENTERPRISE = 2
        GITLAB_ENTERPRISE = 3

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repository_type: RepositoryType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RepositoryType,
    )
    pull_request: "PullRequestFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="filter",
        message="PullRequestFilter",
    )
    push: "PushFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="filter",
        message="PushFilter",
    )


class GitHubEventsConfig(proto.Message):
    r"""GitHubEventsConfig describes the configuration of a trigger
    that creates a build whenever a GitHub event is received.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        installation_id (int):
            The installationID that emits the GitHub
            event.
        owner (str):
            Owner of the repository. For example: The
            owner for
            https://github.com/googlecloudplatform/cloud-builders
            is "googlecloudplatform".
        name (str):
            Name of the repository. For example: The name
            for
            https://github.com/googlecloudplatform/cloud-builders
            is "cloud-builders".
        pull_request (google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter):
            filter to match changes in pull requests.

            This field is a member of `oneof`_ ``event``.
        push (google.cloud.devtools.cloudbuild_v1.types.PushFilter):
            filter to match changes in refs like
            branches, tags.

            This field is a member of `oneof`_ ``event``.
    """

    installation_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=6,
    )
    name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    pull_request: "PullRequestFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="event",
        message="PullRequestFilter",
    )
    push: "PushFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="event",
        message="PushFilter",
    )


class PubsubConfig(proto.Message):
    r"""PubsubConfig describes the configuration of a trigger that
    creates a build whenever a Pub/Sub message is published.

    Attributes:
        subscription (str):
            Output only. Name of the subscription. Format is
            ``projects/{project}/subscriptions/{subscription}``.
        topic (str):
            Optional. The name of the topic from which this subscription
            is receiving messages. Format is
            ``projects/{project}/topics/{topic}``.
        service_account_email (str):
            Service account that will make the push
            request.
        state (google.cloud.devtools.cloudbuild_v1.types.PubsubConfig.State):
            Potential issues with the underlying Pub/Sub
            subscription configuration. Only populated on
            get requests.
    """

    class State(proto.Enum):
        r"""Enumerates potential issues with the underlying Pub/Sub
        subscription configuration.

        Values:
            STATE_UNSPECIFIED (0):
                The subscription configuration has not been
                checked.
            OK (1):
                The Pub/Sub subscription is properly
                configured.
            SUBSCRIPTION_DELETED (2):
                The subscription has been deleted.
            TOPIC_DELETED (3):
                The topic has been deleted.
            SUBSCRIPTION_MISCONFIGURED (4):
                Some of the subscription's field are
                misconfigured.
        """

        STATE_UNSPECIFIED = 0
        OK = 1
        SUBSCRIPTION_DELETED = 2
        TOPIC_DELETED = 3
        SUBSCRIPTION_MISCONFIGURED = 4

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    topic: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class WebhookConfig(proto.Message):
    r"""WebhookConfig describes the configuration of a trigger that
    creates a build whenever a webhook is sent to a trigger's
    webhook URL.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        secret (str):
            Required. Resource name for the secret
            required as a URL parameter.

            This field is a member of `oneof`_ ``auth_method``.
        state (google.cloud.devtools.cloudbuild_v1.types.WebhookConfig.State):
            Potential issues with the underlying Pub/Sub
            subscription configuration. Only populated on
            get requests.
    """

    class State(proto.Enum):
        r"""Enumerates potential issues with the Secret Manager secret
        provided by the user.

        Values:
            STATE_UNSPECIFIED (0):
                The webhook auth configuration not been
                checked.
            OK (1):
                The auth configuration is properly setup.
            SECRET_DELETED (2):
                The secret provided in auth_method has been deleted.
        """

        STATE_UNSPECIFIED = 0
        OK = 1
        SECRET_DELETED = 2

    secret: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="auth_method",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class PullRequestFilter(proto.Message):
    r"""PullRequestFilter contains filter properties for matching
    GitHub Pull Requests.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        branch (str):
            Regex of branches to match.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``git_ref``.
        comment_control (google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter.CommentControl):
            If CommentControl is enabled, depending on the setting,
            builds may not fire until a repository writer comments
            ``/gcbrun`` on a pull request or ``/gcbrun`` is in the pull
            request description. Only PR comments that contain
            ``/gcbrun`` will trigger builds.

            If CommentControl is set to disabled, comments with
            ``/gcbrun`` from a user with repository write permission or
            above will still trigger builds to run.
        invert_regex (bool):
            If true, branches that do NOT match the git_ref will trigger
            a build.
    """

    class CommentControl(proto.Enum):
        r"""Controls whether or not a ``/gcbrun`` comment is required from a
        user with repository write permission or above in order to trigger
        Build runs for pull requests. Pull Request update events differ
        between repo types. Check repo specific guides
        (`GitHub <https://cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise#creating_a_github_enterprise_trigger>`__,
        `Bitbucket <https://cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server#creating_a_bitbucket_server_trigger>`__,
        `GitLab <https://cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab#creating_a_gitlab_trigger>`__
        for details.

        Values:
            COMMENTS_DISABLED (0):
                Do not require ``/gcbrun`` comments from a user with
                repository write permission or above on pull requests before
                builds are triggered. Comments that contain ``/gcbrun`` will
                still fire builds so this should be thought of as comments
                not required.
            COMMENTS_ENABLED (1):
                Builds will only fire in response to pull requests if:

                1. The pull request author has repository write permission
                   or above and ``/gcbrun`` is in the PR description.
                2. A user with repository writer permissions or above
                   comments ``/gcbrun`` on a pull request authored by any
                   user.
            COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY (2):
                Builds will only fire in response to pull requests if:

                1. The pull request author is a repository writer or above.
                2. If the author does not have write permissions, a user
                   with write permissions or above must comment ``/gcbrun``
                   in order to fire a build.
        """

        COMMENTS_DISABLED = 0
        COMMENTS_ENABLED = 1
        COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY = 2

    branch: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="git_ref",
    )
    comment_control: CommentControl = proto.Field(
        proto.ENUM,
        number=5,
        enum=CommentControl,
    )
    invert_regex: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class PushFilter(proto.Message):
    r"""Push contains filter properties for matching GitHub git
    pushes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        branch (str):
            Regexes matching branches to build.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``git_ref``.
        tag (str):
            Regexes matching tags to build.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``git_ref``.
        invert_regex (bool):
            When true, only trigger a build if the revision regex does
            NOT match the git_ref regex.
    """

    branch: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="git_ref",
    )
    tag: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="git_ref",
    )
    invert_regex: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class CreateBuildTriggerRequest(proto.Message):
    r"""Request to create a new ``BuildTrigger``.

    Attributes:
        parent (str):
            The parent resource where this trigger will be created.
            Format: ``projects/{project}/locations/{location}``
        project_id (str):
            Required. ID of the project for which to
            configure automatic builds.
        trigger (google.cloud.devtools.cloudbuild_v1.types.BuildTrigger):
            Required. ``BuildTrigger`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger: "BuildTrigger" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BuildTrigger",
    )


class GetBuildTriggerRequest(proto.Message):
    r"""Returns the ``BuildTrigger`` with the specified ID.

    Attributes:
        name (str):
            The name of the ``Trigger`` to retrieve. Format:
            ``projects/{project}/locations/{location}/triggers/{trigger}``
        project_id (str):
            Required. ID of the project that owns the
            trigger.
        trigger_id (str):
            Required. Identifier (``id`` or ``name``) of the
            ``BuildTrigger`` to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListBuildTriggersRequest(proto.Message):
    r"""Request to list existing ``BuildTriggers``.

    Attributes:
        parent (str):
            The parent of the collection of ``Triggers``. Format:
            ``projects/{project}/locations/{location}``
        project_id (str):
            Required. ID of the project for which to list
            BuildTriggers.
        page_size (int):
            Number of results to return in the list.
        page_token (str):
            Token to provide to skip to a particular spot
            in the list.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    project_id: str = proto.Field(
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


class ListBuildTriggersResponse(proto.Message):
    r"""Response containing existing ``BuildTriggers``.

    Attributes:
        triggers (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.BuildTrigger]):
            ``BuildTriggers`` for the project, sorted by ``create_time``
            descending.
        next_page_token (str):
            Token to receive the next page of results.
    """

    @property
    def raw_page(self):
        return self

    triggers: MutableSequence["BuildTrigger"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BuildTrigger",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteBuildTriggerRequest(proto.Message):
    r"""Request to delete a ``BuildTrigger``.

    Attributes:
        name (str):
            The name of the ``Trigger`` to delete. Format:
            ``projects/{project}/locations/{location}/triggers/{trigger}``
        project_id (str):
            Required. ID of the project that owns the
            trigger.
        trigger_id (str):
            Required. ID of the ``BuildTrigger`` to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateBuildTriggerRequest(proto.Message):
    r"""Request to update an existing ``BuildTrigger``.

    Attributes:
        project_id (str):
            Required. ID of the project that owns the
            trigger.
        trigger_id (str):
            Required. ID of the ``BuildTrigger`` to update.
        trigger (google.cloud.devtools.cloudbuild_v1.types.BuildTrigger):
            Required. ``BuildTrigger`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Update mask for the resource. If this is set,
            the server will only update the fields specified
            in the field mask. Otherwise, a full update of
            the mutable resource fields will be performed.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trigger: "BuildTrigger" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BuildTrigger",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class BuildOptions(proto.Message):
    r"""Optional arguments to enable specific features of builds.

    Attributes:
        source_provenance_hash (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Hash.HashType]):
            Requested hash for SourceProvenance.
        requested_verify_option (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.VerifyOption):
            Requested verifiability options.
        machine_type (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.MachineType):
            Compute Engine machine type on which to run
            the build.
        disk_size_gb (int):
            Requested disk size for the VM that runs the build. Note
            that this is *NOT* "disk free"; some of the space will be
            used by the operating system and build utilities. Also note
            that this is the minimum disk size that will be allocated
            for the build -- the build may run with a larger disk than
            requested. At present, the maximum disk size is 4000GB;
            builds that request more than the maximum are rejected with
            an error.
        substitution_option (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.SubstitutionOption):
            Option to specify behavior when there is an error in the
            substitution checks.

            NOTE: this is always set to ALLOW_LOOSE for triggered builds
            and cannot be overridden in the build configuration file.
        dynamic_substitutions (bool):
            Option to specify whether or not to apply
            bash style string operations to the
            substitutions.

            NOTE: this is always enabled for triggered
            builds and cannot be overridden in the build
            configuration file.
        automap_substitutions (bool):
            Option to include built-in and custom
            substitutions as env variables for all build
            steps.
        log_streaming_option (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LogStreamingOption):
            Option to define build log streaming behavior
            to Cloud Storage.
        worker_pool (str):
            This field deprecated; please use ``pool.name`` instead.
        pool (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.PoolOption):
            Optional. Specification for execution on a ``WorkerPool``.

            See `running builds in a private
            pool <https://cloud.google.com/build/docs/private-pools/run-builds-in-private-pool>`__
            for more information.
        logging (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LoggingMode):
            Option to specify the logging mode, which
            determines if and where build logs are stored.
        env (MutableSequence[str]):
            A list of global environment variable
            definitions that will exist for all build steps
            in this build. If a variable is defined in both
            globally and in a build step, the variable will
            use the build step value.

            The elements are of the form "KEY=VALUE" for the
            environment variable "KEY" being given the value
            "VALUE".
        secret_env (MutableSequence[str]):
            A list of global environment variables, which are encrypted
            using a Cloud Key Management Service crypto key. These
            values must be specified in the build's ``Secret``. These
            variables will be available to all build steps in this
            build.
        volumes (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.Volume]):
            Global list of volumes to mount for ALL build
            steps
            Each volume is created as an empty volume prior
            to starting the build process. Upon completion
            of the build, volumes and their contents are
            discarded. Global volume names and paths cannot
            conflict with the volumes defined a build step.

            Using a global volume in a build with only one
            step is not valid as it is indicative of a build
            request with an incorrect configuration.
        default_logs_bucket_behavior (google.cloud.devtools.cloudbuild_v1.types.BuildOptions.DefaultLogsBucketBehavior):
            Optional. Option to specify how default logs
            buckets are setup.
        enable_structured_logging (bool):
            Optional. Option to specify whether
            structured logging is enabled.
            If true, JSON-formatted logs are parsed as
            structured logs.
        worker_release (str):
            Optional. Option to specify which release or release channel
            (rapid|regular|stable) to use to run this build.
        resolved_worker_release (str):
            Output only. Worker release resolved from the
            release channel.
    """

    class VerifyOption(proto.Enum):
        r"""Specifies the manner in which the build should be verified, if at
        all.

        If a verified build is requested, and any part of the process to
        generate and upload provenance fails, the build will also fail.

        If the build does not request verification then that process may
        occur, but is not guaranteed to. If it does occur and fails, the
        build will not fail.

        For more information, see `Viewing Build
        Provenance <https://cloud.google.com/build/docs/securing-builds/view-build-provenance>`__.

        Values:
            NOT_VERIFIED (0):
                Not a verifiable build (the default).
            VERIFIED (1):
                Build must be verified.
        """

        NOT_VERIFIED = 0
        VERIFIED = 1

    class MachineType(proto.Enum):
        r"""Supported Compute Engine machine types. For more information, see
        `Machine
        types <https://cloud.google.com/compute/docs/machine-types>`__.

        Values:
            UNSPECIFIED (0):
                Standard machine type.
            N1_HIGHCPU_8 (1):
                Highcpu machine with 8 CPUs.
            N1_HIGHCPU_32 (2):
                Highcpu machine with 32 CPUs.
            E2_HIGHCPU_8 (5):
                Highcpu e2 machine with 8 CPUs.
            E2_HIGHCPU_32 (6):
                Highcpu e2 machine with 32 CPUs.
            E2_MEDIUM (7):
                E2 machine with 1 CPU.
            E2_STANDARD_2 (11):
                E2 machine with 2 CPUs.
        """

        UNSPECIFIED = 0
        N1_HIGHCPU_8 = 1
        N1_HIGHCPU_32 = 2
        E2_HIGHCPU_8 = 5
        E2_HIGHCPU_32 = 6
        E2_MEDIUM = 7
        E2_STANDARD_2 = 11

    class SubstitutionOption(proto.Enum):
        r"""Specifies the behavior when there is an error in the
        substitution checks.

        Values:
            MUST_MATCH (0):
                Fails the build if error in substitutions
                checks, like missing a substitution in the
                template or in the map.
            ALLOW_LOOSE (1):
                Do not fail the build if error in
                substitutions checks.
        """

        MUST_MATCH = 0
        ALLOW_LOOSE = 1

    class LogStreamingOption(proto.Enum):
        r"""Specifies the behavior when writing build logs to Cloud
        Storage.

        Values:
            STREAM_DEFAULT (0):
                Service may automatically determine build log
                streaming behavior.
            STREAM_ON (1):
                Build logs should be streamed to Cloud
                Storage.
            STREAM_OFF (2):
                Build logs should not be streamed to Cloud
                Storage; they will be written when the build is
                completed.
        """

        STREAM_DEFAULT = 0
        STREAM_ON = 1
        STREAM_OFF = 2

    class LoggingMode(proto.Enum):
        r"""Specifies the logging mode.

        Values:
            LOGGING_UNSPECIFIED (0):
                The service determines the logging mode. The default is
                ``LEGACY``. Do not rely on the default logging behavior as
                it may change in the future.
            LEGACY (1):
                Build logs are stored in Cloud Logging and
                Cloud Storage.
            GCS_ONLY (2):
                Build logs are stored in Cloud Storage.
            STACKDRIVER_ONLY (3):
                This option is the same as CLOUD_LOGGING_ONLY.
            CLOUD_LOGGING_ONLY (5):
                Build logs are stored in Cloud Logging. Selecting this
                option will not allow `logs
                streaming <https://cloud.google.com/sdk/gcloud/reference/builds/log>`__.
            NONE (4):
                Turn off all logging. No build logs will be
                captured.
        """

        LOGGING_UNSPECIFIED = 0
        LEGACY = 1
        GCS_ONLY = 2
        STACKDRIVER_ONLY = 3
        CLOUD_LOGGING_ONLY = 5
        NONE = 4

    class DefaultLogsBucketBehavior(proto.Enum):
        r"""Default Cloud Storage log bucket behavior options.

        Values:
            DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED (0):
                Unspecified.
            REGIONAL_USER_OWNED_BUCKET (1):
                Bucket is located in user-owned project in
                the same region as the build. The builder
                service account must have access to create and
                write to Cloud Storage buckets in the build
                project.
            LEGACY_BUCKET (2):
                Bucket is located in a Google-owned project
                and is not regionalized.
        """

        DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED = 0
        REGIONAL_USER_OWNED_BUCKET = 1
        LEGACY_BUCKET = 2

    class PoolOption(proto.Message):
        r"""Details about how a build should be executed on a ``WorkerPool``.

        See `running builds in a private
        pool <https://cloud.google.com/build/docs/private-pools/run-builds-in-private-pool>`__
        for more information.

        Attributes:
            name (str):
                The ``WorkerPool`` resource to execute the build on. You
                must have ``cloudbuild.workerpools.use`` on the project
                hosting the WorkerPool.

                Format
                projects/{project}/locations/{location}/workerPools/{workerPoolId}
            worker_release (str):
                Output only. OUTPUT_ONLY. The release or release channel
                used to run the Build. This is set to the same value as
                ``PrivatePoolV1Config.WorkerConfig.worker_release`` for the
                UI to easily access.
            resolved_worker_release (str):
                Output only. OUTPUT_ONLY. Worker release resolved from the
                release channel.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        worker_release: str = proto.Field(
            proto.STRING,
            number=4,
        )
        resolved_worker_release: str = proto.Field(
            proto.STRING,
            number=5,
        )

    source_provenance_hash: MutableSequence["Hash.HashType"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="Hash.HashType",
    )
    requested_verify_option: VerifyOption = proto.Field(
        proto.ENUM,
        number=2,
        enum=VerifyOption,
    )
    machine_type: MachineType = proto.Field(
        proto.ENUM,
        number=3,
        enum=MachineType,
    )
    disk_size_gb: int = proto.Field(
        proto.INT64,
        number=6,
    )
    substitution_option: SubstitutionOption = proto.Field(
        proto.ENUM,
        number=4,
        enum=SubstitutionOption,
    )
    dynamic_substitutions: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    automap_substitutions: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    log_streaming_option: LogStreamingOption = proto.Field(
        proto.ENUM,
        number=5,
        enum=LogStreamingOption,
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=7,
    )
    pool: PoolOption = proto.Field(
        proto.MESSAGE,
        number=19,
        message=PoolOption,
    )
    logging: LoggingMode = proto.Field(
        proto.ENUM,
        number=11,
        enum=LoggingMode,
    )
    env: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    secret_env: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    volumes: MutableSequence["Volume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="Volume",
    )
    default_logs_bucket_behavior: DefaultLogsBucketBehavior = proto.Field(
        proto.ENUM,
        number=21,
        enum=DefaultLogsBucketBehavior,
    )
    enable_structured_logging: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    worker_release: str = proto.Field(
        proto.STRING,
        number=25,
    )
    resolved_worker_release: str = proto.Field(
        proto.STRING,
        number=26,
    )


class ReceiveTriggerWebhookRequest(proto.Message):
    r"""ReceiveTriggerWebhookRequest [Experimental] is the request object
    accepted by the ReceiveTriggerWebhook method.

    Attributes:
        name (str):
            The name of the ``ReceiveTriggerWebhook`` to retrieve.
            Format:
            ``projects/{project}/locations/{location}/triggers/{trigger}``
        body (google.api.httpbody_pb2.HttpBody):
            HTTP request body.
        project_id (str):
            Project in which the specified trigger lives
        trigger (str):
            Name of the trigger to run the payload
            against
        secret (str):
            Secret token used for authorization if an
            OAuth token isn't provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    body: httpbody_pb2.HttpBody = proto.Field(
        proto.MESSAGE,
        number=1,
        message=httpbody_pb2.HttpBody,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trigger: str = proto.Field(
        proto.STRING,
        number=3,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ReceiveTriggerWebhookResponse(proto.Message):
    r"""ReceiveTriggerWebhookResponse [Experimental] is the response object
    for the ReceiveTriggerWebhook method.

    """


class GitHubEnterpriseConfig(proto.Message):
    r"""GitHubEnterpriseConfig represents a configuration for a
    GitHub Enterprise server.

    Attributes:
        name (str):
            The full resource name for the GitHubEnterpriseConfig For
            example:
            "projects/{$project_id}/locations/{$location_id}/githubEnterpriseConfigs/{$config_id}".
        host_url (str):
            The URL of the github enterprise host the
            configuration is for.
        app_id (int):
            Required. The GitHub app id of the Cloud
            Build app on the GitHub Enterprise server.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the installation was
            associated with the project.
        webhook_key (str):
            The key that should be attached to webhook
            calls to the ReceiveWebhook endpoint.
        peered_network (str):
            Optional. The network to be used when reaching out to the
            GitHub Enterprise server. The VPC network must be enabled
            for private service connection. This should be set if the
            GitHub Enterprise server is hosted on-premises and not
            reachable by public internet. If this field is left empty,
            no network peering will occur and calls to the GitHub
            Enterprise server will be made over the public internet.
            Must be in the format
            ``projects/{project}/global/networks/{network}``, where
            {project} is a project number or id and {network} is the
            name of a VPC network in the project.
        secrets (google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseSecrets):
            Optional. Names of secrets in Secret Manager.
        display_name (str):
            Optional. Name to display for this config.
        ssl_ca (str):
            Optional. SSL certificate to use for requests
            to GitHub Enterprise.
    """

    name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    host_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    app_id: int = proto.Field(
        proto.INT64,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    webhook_key: str = proto.Field(
        proto.STRING,
        number=8,
    )
    peered_network: str = proto.Field(
        proto.STRING,
        number=9,
    )
    secrets: "GitHubEnterpriseSecrets" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="GitHubEnterpriseSecrets",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    ssl_ca: str = proto.Field(
        proto.STRING,
        number=12,
    )


class GitHubEnterpriseSecrets(proto.Message):
    r"""GitHubEnterpriseSecrets represents the names of all necessary
    secrets in Secret Manager for a GitHub Enterprise server. Format
    is: projects/<project number>/secrets/<secret name>.

    Attributes:
        private_key_version_name (str):
            The resource name for the private key secret
            version.
        webhook_secret_version_name (str):
            The resource name for the webhook secret
            secret version in Secret Manager.
        oauth_secret_version_name (str):
            The resource name for the OAuth secret secret
            version in Secret Manager.
        oauth_client_id_version_name (str):
            The resource name for the OAuth client ID
            secret version in Secret Manager.
    """

    private_key_version_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    webhook_secret_version_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    oauth_secret_version_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    oauth_client_id_version_name: str = proto.Field(
        proto.STRING,
        number=8,
    )


class WorkerPool(proto.Message):
    r"""Configuration for a ``WorkerPool``.

    Cloud Build owns and maintains a pool of workers for general use and
    have no access to a project's private network. By default, builds
    submitted to Cloud Build will use a worker from this pool.

    If your build needs access to resources on a private network, create
    and use a ``WorkerPool`` to run your builds. Private
    ``WorkerPool``\ s give your builds access to any single VPC network
    that you administer, including any on-prem resources connected to
    that VPC network. For an overview of private pools, see `Private
    pools
    overview <https://cloud.google.com/build/docs/private-pools/private-pools-overview>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of the ``WorkerPool``, with
            format
            ``projects/{project}/locations/{location}/workerPools/{worker_pool}``.
            The value of ``{worker_pool}`` is provided by
            ``worker_pool_id`` in ``CreateWorkerPool`` request and the
            value of ``{location}`` is determined by the endpoint
            accessed.
        display_name (str):
            A user-specified, human-readable name for the
            ``WorkerPool``. If provided, this value must be 1-63
            characters.
        uid (str):
            Output only. A unique identifier for the ``WorkerPool``.
        annotations (MutableMapping[str, str]):
            User specified annotations. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the request to create the
            ``WorkerPool`` was received.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the request to update the
            ``WorkerPool`` was received.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the request to delete the
            ``WorkerPool`` was received.
        state (google.cloud.devtools.cloudbuild_v1.types.WorkerPool.State):
            Output only. ``WorkerPool`` state.
        private_pool_v1_config (google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config):
            Private Pool configuration.

            This field is a member of `oneof`_ ``config``.
        etag (str):
            Output only. Checksum computed by the server.
            May be sent on update and delete requests to
            ensure that the client has an up-to-date value
            before proceeding.
    """

    class State(proto.Enum):
        r"""State of the ``WorkerPool``.

        Values:
            STATE_UNSPECIFIED (0):
                State of the ``WorkerPool`` is unknown.
            CREATING (1):
                ``WorkerPool`` is being created.
            RUNNING (2):
                ``WorkerPool`` is running.
            DELETING (3):
                ``WorkerPool`` is being deleted: cancelling builds and
                draining workers.
            DELETED (4):
                ``WorkerPool`` is deleted.
            UPDATING (5):
                ``WorkerPool`` is being updated; new builds cannot be run.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        RUNNING = 2
        DELETING = 3
        DELETED = 4
        UPDATING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    private_pool_v1_config: "PrivatePoolV1Config" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="config",
        message="PrivatePoolV1Config",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )


class PrivatePoolV1Config(proto.Message):
    r"""Configuration for a V1 ``PrivatePool``.

    Attributes:
        worker_config (google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.WorkerConfig):
            Machine configuration for the workers in the
            pool.
        network_config (google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig):
            Network configuration for the pool.
        private_service_connect (google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.PrivateServiceConnect):
            Immutable. Private Service Connect(PSC)
            Network configuration for the pool.
    """

    class WorkerConfig(proto.Message):
        r"""Defines the configuration to be used for creating workers in
        the pool.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            machine_type (str):
                Optional. Machine type of a worker, such as ``e2-medium``.
                See `Worker pool config
                file <https://cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema>`__.
                If left blank, Cloud Build will use a sensible default.
            disk_size_gb (int):
                Size of the disk attached to the worker, in GB. See `Worker
                pool config
                file <https://cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema>`__.
                Specify a value of up to 4000. If ``0`` is specified, Cloud
                Build will use a standard disk size.
            enable_nested_virtualization (bool):
                Optional. Enable nested virtualization on the
                worker, if supported by the machine type. By
                default, nested virtualization is disabled.

                This field is a member of `oneof`_ ``_enable_nested_virtualization``.
            worker_release (str):
                Optional. Option to specify which release or release channel
                (rapid|regular|stable) to use to run this build.
        """

        machine_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        disk_size_gb: int = proto.Field(
            proto.INT64,
            number=2,
        )
        enable_nested_virtualization: bool = proto.Field(
            proto.BOOL,
            number=3,
            optional=True,
        )
        worker_release: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class NetworkConfig(proto.Message):
        r"""Defines the network configuration for the pool.

        Attributes:
            peered_network (str):
                Required. Immutable. The network definition that the workers
                are peered to. If this section is left empty, the workers
                will be peered to ``WorkerPool.project_id`` on the service
                producer network. Must be in the format
                ``projects/{project}/global/networks/{network}``, where
                ``{project}`` is a project number, such as ``12345``, and
                ``{network}`` is the name of a VPC network in the project.
                See `Understanding network configuration
                options <https://cloud.google.com/build/docs/private-pools/set-up-private-pool-environment>`__
            egress_option (google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig.EgressOption):
                Option to configure network egress for the
                workers.
            peered_network_ip_range (str):
                Immutable. Subnet IP range within the peered network. This
                is specified in CIDR notation with a slash and the subnet
                prefix size. You can optionally specify an IP address before
                the subnet prefix value. e.g. ``192.168.0.0/29`` would
                specify an IP range starting at 192.168.0.0 with a prefix
                size of 29 bits. ``/16`` would specify a prefix size of 16
                bits, with an automatically determined IP within the peered
                VPC. If unspecified, a value of ``/24`` will be used.
        """

        class EgressOption(proto.Enum):
            r"""Defines the egress option for the pool.

            Values:
                EGRESS_OPTION_UNSPECIFIED (0):
                    If set, defaults to PUBLIC_EGRESS.
                NO_PUBLIC_EGRESS (1):
                    If set, workers are created without any
                    public address, which prevents network egress to
                    public IPs unless a network proxy is configured.
                PUBLIC_EGRESS (2):
                    If set, workers are created with a public
                    address which allows for public internet egress.
            """

            EGRESS_OPTION_UNSPECIFIED = 0
            NO_PUBLIC_EGRESS = 1
            PUBLIC_EGRESS = 2

        peered_network: str = proto.Field(
            proto.STRING,
            number=1,
        )
        egress_option: "PrivatePoolV1Config.NetworkConfig.EgressOption" = proto.Field(
            proto.ENUM,
            number=2,
            enum="PrivatePoolV1Config.NetworkConfig.EgressOption",
        )
        peered_network_ip_range: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class PrivateServiceConnect(proto.Message):
        r"""Defines the Private Service Connect network configuration for
        the pool.

        Attributes:
            network_attachment (str):
                Required. Immutable. The network attachment that the worker
                network interface is peered to. Must be in the format
                ``projects/{project}/regions/{region}/networkAttachments/{networkAttachment}``.
                The region of network attachment must be the same as the
                worker pool. See `Network
                Attachments <https://cloud.google.com/vpc/docs/about-network-attachments>`__
            public_ip_address_disabled (bool):
                Required. Immutable. Disable public IP on the primary
                network interface.

                If true, workers are created without any public address,
                which prevents network egress to public IPs unless a network
                proxy is configured. If false, workers are created with a
                public address which allows for public internet egress. The
                public address only applies to traffic through the primary
                network interface. If ``route_all_traffic`` is set to true,
                all traffic will go through the non-primary network
                interface, this boolean has no effect.
            route_all_traffic (bool):
                Immutable. Route all traffic through PSC
                interface. Enable this if you want full control
                of traffic in the private pool. Configure Cloud
                NAT for the subnet of network attachment if you
                need to access public Internet.

                If false, Only route RFC 1918 (10.0.0.0/8,
                172.16.0.0/12, and 192.168.0.0/16) and RFC 6598
                (100.64.0.0/10) through PSC interface.
        """

        network_attachment: str = proto.Field(
            proto.STRING,
            number=1,
        )
        public_ip_address_disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        route_all_traffic: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    worker_config: WorkerConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=WorkerConfig,
    )
    network_config: NetworkConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=NetworkConfig,
    )
    private_service_connect: PrivateServiceConnect = proto.Field(
        proto.MESSAGE,
        number=5,
        message=PrivateServiceConnect,
    )


class CreateWorkerPoolRequest(proto.Message):
    r"""Request to create a new ``WorkerPool``.

    Attributes:
        parent (str):
            Required. The parent resource where this worker pool will be
            created. Format:
            ``projects/{project}/locations/{location}``.
        worker_pool (google.cloud.devtools.cloudbuild_v1.types.WorkerPool):
            Required. ``WorkerPool`` resource to create.
        worker_pool_id (str):
            Required. Immutable. The ID to use for the ``WorkerPool``,
            which will become the final component of the resource name.

            This value should be 1-63 characters, and valid characters
            are /[a-z][0-9]-/.
        validate_only (bool):
            If set, validate the request and preview the
            response, but do not actually post it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    worker_pool: "WorkerPool" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="WorkerPool",
    )
    worker_pool_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetWorkerPoolRequest(proto.Message):
    r"""Request to get a ``WorkerPool`` with the specified name.

    Attributes:
        name (str):
            Required. The name of the ``WorkerPool`` to retrieve.
            Format:
            ``projects/{project}/locations/{location}/workerPools/{workerPool}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteWorkerPoolRequest(proto.Message):
    r"""Request to delete a ``WorkerPool``.

    Attributes:
        name (str):
            Required. The name of the ``WorkerPool`` to delete. Format:
            ``projects/{project}/locations/{location}/workerPools/{workerPool}``.
        etag (str):
            Optional. If provided, it must match the
            server's etag on the workerpool for the request
            to be processed.
        allow_missing (bool):
            If set to true, and the ``WorkerPool`` is not found, the
            request will succeed but no action will be taken on the
            server.
        validate_only (bool):
            If set, validate the request and preview the
            response, but do not actually post it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateWorkerPoolRequest(proto.Message):
    r"""Request to update a ``WorkerPool``.

    Attributes:
        worker_pool (google.cloud.devtools.cloudbuild_v1.types.WorkerPool):
            Required. The ``WorkerPool`` to update.

            The ``name`` field is used to identify the ``WorkerPool`` to
            update. Format:
            ``projects/{project}/locations/{location}/workerPools/{workerPool}``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A mask specifying which fields in ``worker_pool``
            to update.
        validate_only (bool):
            If set, validate the request and preview the
            response, but do not actually post it.
    """

    worker_pool: "WorkerPool" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="WorkerPool",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListWorkerPoolsRequest(proto.Message):
    r"""Request to list ``WorkerPool``\ s.

    Attributes:
        parent (str):
            Required. The parent of the collection of ``WorkerPools``.
            Format: ``projects/{project}/locations/{location}``.
        page_size (int):
            The maximum number of ``WorkerPool``\ s to return. The
            service may return fewer than this value. If omitted, the
            server will use a sensible default.
        page_token (str):
            A page token, received from a previous ``ListWorkerPools``
            call. Provide this to retrieve the subsequent page.
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


class ListWorkerPoolsResponse(proto.Message):
    r"""Response containing existing ``WorkerPools``.

    Attributes:
        worker_pools (MutableSequence[google.cloud.devtools.cloudbuild_v1.types.WorkerPool]):
            ``WorkerPools`` for the specified project.
        next_page_token (str):
            Continuation token used to page through large
            result sets. Provide this value in a subsequent
            ListWorkerPoolsRequest to return the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    worker_pools: MutableSequence["WorkerPool"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="WorkerPool",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateWorkerPoolOperationMetadata(proto.Message):
    r"""Metadata for the ``CreateWorkerPool`` operation.

    Attributes:
        worker_pool (str):
            The resource name of the ``WorkerPool`` to create. Format:
            ``projects/{project}/locations/{location}/workerPools/{worker_pool}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the operation was created.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the operation was completed.
    """

    worker_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class UpdateWorkerPoolOperationMetadata(proto.Message):
    r"""Metadata for the ``UpdateWorkerPool`` operation.

    Attributes:
        worker_pool (str):
            The resource name of the ``WorkerPool`` being updated.
            Format:
            ``projects/{project}/locations/{location}/workerPools/{worker_pool}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the operation was created.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the operation was completed.
    """

    worker_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class DeleteWorkerPoolOperationMetadata(proto.Message):
    r"""Metadata for the ``DeleteWorkerPool`` operation.

    Attributes:
        worker_pool (str):
            The resource name of the ``WorkerPool`` being deleted.
            Format:
            ``projects/{project}/locations/{location}/workerPools/{worker_pool}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the operation was created.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the operation was completed.
    """

    worker_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
