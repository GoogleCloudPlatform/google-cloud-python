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

from google.cloud.designcenter_v1.types import enums

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "ArtifactLocation",
        "DeveloperConnectExportConfig",
        "ExportIaCConfig",
        "TerraformConfig",
        "TerraformModuleConfig",
    },
)


class ArtifactLocation(proto.Message):
    r"""Defines the location for storing an artifact, such as
    generated IaC.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        developer_connect_export_config (google.cloud.designcenter_v1.types.DeveloperConnectExportConfig):
            Optional. Source Code Management(SCM) config
            for storing the content, such as generated IaC.
            Supports sources integrated with Developer
            Connect like GitHub, GitHub Enterprise, GitLab,
            and Bitbucket.

            This field is a member of `oneof`_ ``location``.
        gcs_uri (str):
            Optional. The Cloud Storage URI for storing
            the generated IaC.

            This field is a member of `oneof`_ ``location``.
    """

    developer_connect_export_config: "DeveloperConnectExportConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="location",
        message="DeveloperConnectExportConfig",
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="location",
    )


class DeveloperConnectExportConfig(proto.Message):
    r"""Through Developer Connect, defines a location where content
    such as Infrastructure as Code (IaC) is stored.

    Attributes:
        developer_connect_repo_uri (str):
            Required. The Developer Connect Git repository link,
            formatted as
            ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``.
        branch (str):
            Optional. The branch in repo to which the
            content such as Infrastructure as Code (IaC)
            should be written to. If empty, Application
            Design Center will create a branch and push the
            changes.
        dir_ (str):
            Required. Directory, relative to the source
            repo, where content such as Infrastructure as
            Code (IaC) will be stored. This must be a
            relative path.To specify the root directory, use
            '/'. If the path or any subdirectories do not
            exist, they will be created.
        commit_sha (str):
            Output only. The SHA of the Git commit that
            contains the exported content such as
            Infrastructure as Code (IaC).
    """

    developer_connect_repo_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    branch: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ExportIaCConfig(proto.Message):
    r"""Configuration for exporting a resource as IAC.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tf_config (google.cloud.designcenter_v1.types.TerraformConfig):
            Optional. Configuration on how to handle
            terraform IaC export.

            This field is a member of `oneof`_ ``config_payload``.
        iac_format (google.cloud.designcenter_v1.types.IACFormat):
            Optional. IaC format of the export. Default is
            [IACFormat.TERRAFORM].
    """

    tf_config: "TerraformConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="config_payload",
        message="TerraformConfig",
    )
    iac_format: enums.IACFormat = proto.Field(
        proto.ENUM,
        number=1,
        enum=enums.IACFormat,
    )


class TerraformConfig(proto.Message):
    r"""Configuration for exporting a resource as Terraform IAC.

    Attributes:
        tf_module_config (google.cloud.designcenter_v1.types.TerraformModuleConfig):
            Optional. Configuration on how terraform
            module should be handled during export.
    """

    tf_module_config: "TerraformModuleConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TerraformModuleConfig",
    )


class TerraformModuleConfig(proto.Message):
    r"""Configuration on how terraform module should be handled
    during export.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        git_proxy_enabled (bool):
            Optional. This is typically only valid for 3P
            components if ingested via devconnect URI.
            Typically, for 1P components, since they are
            sourced from public git repos, this field is not
            applicable.

            This field is a member of `oneof`_ ``source_override``.
        local_references_enabled (bool):
            Optional. If set, all the dependent modules
            will be downloaded from the target repository
            and referenced locally.

            This field is a member of `oneof`_ ``source_override``.
    """

    git_proxy_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="source_override",
    )
    local_references_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="source_override",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
