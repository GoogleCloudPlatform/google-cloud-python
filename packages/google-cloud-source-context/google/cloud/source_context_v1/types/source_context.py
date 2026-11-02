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

__protobuf__ = proto.module(
    package="google.devtools.source.v1",
    manifest={
        "SourceContext",
        "ExtendedSourceContext",
        "AliasContext",
        "CloudRepoSourceContext",
        "CloudWorkspaceSourceContext",
        "GerritSourceContext",
        "GitSourceContext",
        "RepoId",
        "ProjectRepoId",
        "CloudWorkspaceId",
    },
)


class SourceContext(proto.Message):
    r"""A SourceContext is a reference to a tree of files. A
    SourceContext together with a path point to a unique revision of
    a single file or directory.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_repo (google.cloud.source_context_v1.types.CloudRepoSourceContext):
            A SourceContext referring to a revision in a
            cloud repo.

            This field is a member of `oneof`_ ``context``.
        cloud_workspace (google.cloud.source_context_v1.types.CloudWorkspaceSourceContext):
            A SourceContext referring to a snapshot in a
            cloud workspace.

            This field is a member of `oneof`_ ``context``.
        gerrit (google.cloud.source_context_v1.types.GerritSourceContext):
            A SourceContext referring to a Gerrit
            project.

            This field is a member of `oneof`_ ``context``.
        git (google.cloud.source_context_v1.types.GitSourceContext):
            A SourceContext referring to any third party
            Git repo (e.g. GitHub).

            This field is a member of `oneof`_ ``context``.
    """

    cloud_repo: "CloudRepoSourceContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="context",
        message="CloudRepoSourceContext",
    )
    cloud_workspace: "CloudWorkspaceSourceContext" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="context",
        message="CloudWorkspaceSourceContext",
    )
    gerrit: "GerritSourceContext" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="context",
        message="GerritSourceContext",
    )
    git: "GitSourceContext" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="context",
        message="GitSourceContext",
    )


class ExtendedSourceContext(proto.Message):
    r"""An ExtendedSourceContext is a SourceContext combined with
    additional details describing the context.

    Attributes:
        context (google.cloud.source_context_v1.types.SourceContext):
            Any source context.
        labels (MutableMapping[str, str]):
            Labels with user defined metadata.
    """

    context: "SourceContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SourceContext",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class AliasContext(proto.Message):
    r"""An alias to a repo revision.

    Attributes:
        kind (google.cloud.source_context_v1.types.AliasContext.Kind):
            The alias kind.
        name (str):
            The alias name.
    """

    class Kind(proto.Enum):
        r"""The type of an Alias.

        Values:
            ANY (0):
                Do not use.
            FIXED (1):
                Git tag
            MOVABLE (2):
                Git branch
            OTHER (4):
                OTHER is used to specify non-standard
                aliases, those not of the kinds above. For
                example, if a Git repo has a ref named
                "refs/foo/bar", it is considered to be of kind
                OTHER.
        """

        ANY = 0
        FIXED = 1
        MOVABLE = 2
        OTHER = 4

    kind: Kind = proto.Field(
        proto.ENUM,
        number=1,
        enum=Kind,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloudRepoSourceContext(proto.Message):
    r"""A CloudRepoSourceContext denotes a particular revision in a
    cloud repo (a repo hosted by the Google Cloud Platform).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        repo_id (google.cloud.source_context_v1.types.RepoId):
            The ID of the repo.
        revision_id (str):
            A revision ID.

            This field is a member of `oneof`_ ``revision``.
        alias_name (str):
            The name of an alias (branch, tag, etc.).

            This field is a member of `oneof`_ ``revision``.
        alias_context (google.cloud.source_context_v1.types.AliasContext):
            An alias, which may be a branch or tag.

            This field is a member of `oneof`_ ``revision``.
    """

    repo_id: "RepoId" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RepoId",
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="revision",
    )
    alias_name: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="revision",
    )
    alias_context: "AliasContext" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="revision",
        message="AliasContext",
    )


class CloudWorkspaceSourceContext(proto.Message):
    r"""A CloudWorkspaceSourceContext denotes a workspace at a
    particular snapshot.

    Attributes:
        workspace_id (google.cloud.source_context_v1.types.CloudWorkspaceId):
            The ID of the workspace.
        snapshot_id (str):
            The ID of the snapshot. An empty snapshot_id refers to the
            most recent snapshot.
    """

    workspace_id: "CloudWorkspaceId" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudWorkspaceId",
    )
    snapshot_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GerritSourceContext(proto.Message):
    r"""A SourceContext referring to a Gerrit project.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        host_uri (str):
            The URI of a running Gerrit instance.
        gerrit_project (str):
            The full project name within the host.
            Projects may be nested, so "project/subproject"
            is a valid project name. The "repo name" is
            hostURI/project.
        revision_id (str):
            A revision (commit) ID.

            This field is a member of `oneof`_ ``revision``.
        alias_name (str):
            The name of an alias (branch, tag, etc.).

            This field is a member of `oneof`_ ``revision``.
        alias_context (google.cloud.source_context_v1.types.AliasContext):
            An alias, which may be a branch or tag.

            This field is a member of `oneof`_ ``revision``.
    """

    host_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gerrit_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="revision",
    )
    alias_name: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="revision",
    )
    alias_context: "AliasContext" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="revision",
        message="AliasContext",
    )


class GitSourceContext(proto.Message):
    r"""A GitSourceContext denotes a particular revision in a third
    party Git repository (e.g. GitHub).

    Attributes:
        url (str):
            Git repository URL.
        revision_id (str):
            Git commit hash.
            required.
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RepoId(proto.Message):
    r"""A unique identifier for a cloud repo.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project_repo_id (google.cloud.source_context_v1.types.ProjectRepoId):
            A combination of a project ID and a repo
            name.

            This field is a member of `oneof`_ ``id``.
        uid (str):
            A server-assigned, globally unique
            identifier.

            This field is a member of `oneof`_ ``id``.
    """

    project_repo_id: "ProjectRepoId" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="id",
        message="ProjectRepoId",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="id",
    )


class ProjectRepoId(proto.Message):
    r"""Selects a repo using a Google Cloud Platform project ID
    (e.g. winged-cargo-31) and a repo name within that project.

    Attributes:
        project_id (str):
            The ID of the project.
        repo_name (str):
            The name of the repo. Leave empty for the
            default repo.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repo_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloudWorkspaceId(proto.Message):
    r"""A CloudWorkspaceId is a unique identifier for a cloud
    workspace. A cloud workspace is a place associated with a repo
    where modified files can be stored before they are committed.

    Attributes:
        repo_id (google.cloud.source_context_v1.types.RepoId):
            The ID of the repo containing the workspace.
        name (str):
            The unique name of the workspace within the
            repo.  This is the name chosen by the client in
            the Source API's CreateWorkspace method.
    """

    repo_id: "RepoId" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RepoId",
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
