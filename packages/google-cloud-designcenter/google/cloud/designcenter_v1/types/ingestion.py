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
    package="google.cloud.designcenter.v1",
    manifest={
        "GitSource",
        "DeveloperConnectConfig",
        "DeveloperConnectSourceConfig",
        "GitReference",
        "OciRepo",
        "IaCModule",
        "IaCFile",
        "ImportIaCError",
        "CodeRange",
        "CodePosition",
    },
)


class GitSource(proto.Message):
    r"""Defines how to access a Git source.

    Attributes:
        repo (str):
            Required. Location of the git repo to build.
        dir_ (str):
            Optional. Directory, relative to the source root, in which
            to run the build. This must be a relative path. If a step's
            ``dir`` is specified and is an absolute path, this value is
            ignored for that step's execution.
        commit_sha (str):
            Output only. The commit SHA of the git repo deduced from
            given ref_tag.
        developer_connect_config (google.cloud.designcenter_v1.types.DeveloperConnectConfig):
            Optional. This config defines the location of
            a source through Developer Connect. Used to
            access private git repos.
        ref_tag (str):
            Required. The reference tag of the git repo.
    """

    repo: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=3,
    )
    developer_connect_config: "DeveloperConnectConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DeveloperConnectConfig",
    )
    ref_tag: str = proto.Field(
        proto.STRING,
        number=5,
    )


class DeveloperConnectConfig(proto.Message):
    r"""This config defines the location of a source through
    Developer Connect.

    Attributes:
        git_repository_link (str):
            Required. The Developer Connect Git repository link,
            formatted as
            ``projects/*/locations/*/connections/*/gitRepositoryLink/*``.
    """

    git_repository_link: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeveloperConnectSourceConfig(proto.Message):
    r"""This config specifies the location of a source (such as
    GitHub or Bitbucket) through Developer Connect.

    Attributes:
        developer_connect_repo_uri (str):
            Required. The Developer Connect Git repository link,
            formatted as
            ``projects/*/locations/*/connections/*/gitRepositoryLinks/*``.
        reference (google.cloud.designcenter_v1.types.GitReference):
            Required. The reference (for example, a
            branch, tag, or commit SHA) from which the
            content should be read.
        dir_ (str):
            Required. The sub-directory within the
            repository from which to read content. The path
            must be relative to the repository's root such
            as dir1/dir2. To read content from the root dir,
            provide "/" as the value of the field.
        fetched_commit_sha (str):
            Output only. The SHA of the commit deduced
            from GitReference.
    """

    developer_connect_repo_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reference: "GitReference" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="GitReference",
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=5,
    )
    fetched_commit_sha: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GitReference(proto.Message):
    r"""The Git reference. Can be a commit SHA, branch name, or tag
    name.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        branch (str):
            Optional. The name of the branch from which
            content should be read. For example: "main".

            This field is a member of `oneof`_ ``reference``.
        ref_tag (str):
            Optional. The reference tag from which
            content should be read. For example: "v1.2.3".

            This field is a member of `oneof`_ ``reference``.
        commit_sha (str):
            Optional. The full SHA hash of a specific
            commit from which content should be read.

            This field is a member of `oneof`_ ``reference``.
    """

    branch: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="reference",
    )
    ref_tag: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="reference",
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="reference",
    )


class OciRepo(proto.Message):
    r"""Open Container Initiative (OCI) repo.

    Attributes:
        uri (str):
            Required. Path to Open Container Initiative
            (OCI) repo. Example:
            oci://us-west1-docker.pkg.dev/nyap-test/helm-repo/my-chart
        version (str):
            Optional. The version of the helm chart.
        module_source_uri (str):
            Optional. Field for containing the references
            to the source from which the OCI repo was
            created.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    module_source_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class IaCModule(proto.Message):
    r"""IaCModule represents a single infrastructure as code module.

    Attributes:
        files (MutableSequence[google.cloud.designcenter_v1.types.IaCFile]):
            Optional. The files in the module.
    """

    files: MutableSequence["IaCFile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IaCFile",
    )


class IaCFile(proto.Message):
    r"""IaCFile represents a single infrastructure as code file.

    Attributes:
        name (str):
            Required. The name of the file.
        content (str):
            Optional. The content of the file. The
            content of the file can be read and passed as a
            string. For example, for a Terraform file, the
            content is the HCL content of the file.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ImportIaCError(proto.Message):
    r"""Message representing the error encountered during import. Example: A
    variable with name "name" is expected to be of type string, but is
    provided as number, inside a module named "my_module". {
    resource_address: "module.my_module.name" file:
    "gs://my_bucket/main.tf" range: { start: { line: 2 byte_offset: 1
    column: 2 } end: { line: 2 byte_offset: 10 column: 10 } }
    description: "Error parsing field: "name". Expected type "string"
    but got "number"." type: INVALID }

    Attributes:
        resource_address (str):
            Output only. The resource address of the
            error.
        file (str):
            Output only. The file where the error has
            occurred.
        range_ (google.cloud.designcenter_v1.types.CodeRange):
            Output only. The code portion where this
            error occurs.
        description (str):
            Output only. The description of the error.
        type_ (google.cloud.designcenter_v1.types.ImportIaCError.Type):
            Output only. The type of error.
        error_code (google.cloud.designcenter_v1.types.ImportIaCError.ErrorCode):
            Output only. Specific error code for the
            import error.
    """

    class Type(proto.Enum):
        r"""The type of error.

        Values:
            TYPE_UNSPECIFIED (0):
                Default.
            INVALID (1):
                The change is invalid.
                Example: a string value provided for a number
                input parameter type, which would be caught by
                Terraform validation.
            NOT_SUPPORTED (2):
                The change is not supported.
                Example: a user directly adding a Terraform
                resource in main.tf that Design Center does not
                support importing.
        """

        TYPE_UNSPECIFIED = 0
        INVALID = 1
        NOT_SUPPORTED = 2

    class ErrorCode(proto.Enum):
        r"""Specific error code for UI and programmatic handling.

        Values:
            ERROR_CODE_UNSPECIFIED (0):
                Default.
            ERROR_CODE_SYNTAX_ERROR (1):
                HCL Syntax errors (e.g. unclosed blocks, bad
                characters)
            ERROR_CODE_UNSUPPORTED_BLOCK_TYPE (2):
                Top-level block is e.g. "resource", "data",
                "locals".
            ERROR_CODE_TOP_LEVEL_ATTRIBUTE (3):
                Attributes defined outside of allowed blocks
            ERROR_CODE_UNSUPPORTED_MODULE (4):
                Module not present in catalog
            ERROR_CODE_MODULE_UNSUPPORTED_ATTRIBUTE_ADDED (5):
                Attribute defined inside module that is not
                in the shared template
            ERROR_CODE_MODULE_REQUIRED_ATTRIBUTE_REMOVED (6):
                Mandatory attribute of shared template is
                missing in module block
            ERROR_CODE_PARAMETER_VALUE_INVALID (7):
                Value fails shared template schema checks
                (regex, range, etc.)
            ERROR_CODE_UNSUPPORTED_VARIABLE_CHANGE (8):
                Variable in variables.tf is added, removed or
                schema changed
            ERROR_CODE_UNSUPPORTED_OUTPUT_CHANGE (9):
                Output in outputs.tf is added, removed or
                schema changed
            ERROR_CODE_UNSUPPORTED_PROVIDER_CHANGE (10):
                Provider in providers.tf has added blocks or
                modified attributes
            ERROR_CODE_UNSUPPORTED_TFVAR_CHANGE (11):
                Value modified for variables defined in
                terraform.tfvars
        """

        ERROR_CODE_UNSPECIFIED = 0
        ERROR_CODE_SYNTAX_ERROR = 1
        ERROR_CODE_UNSUPPORTED_BLOCK_TYPE = 2
        ERROR_CODE_TOP_LEVEL_ATTRIBUTE = 3
        ERROR_CODE_UNSUPPORTED_MODULE = 4
        ERROR_CODE_MODULE_UNSUPPORTED_ATTRIBUTE_ADDED = 5
        ERROR_CODE_MODULE_REQUIRED_ATTRIBUTE_REMOVED = 6
        ERROR_CODE_PARAMETER_VALUE_INVALID = 7
        ERROR_CODE_UNSUPPORTED_VARIABLE_CHANGE = 8
        ERROR_CODE_UNSUPPORTED_OUTPUT_CHANGE = 9
        ERROR_CODE_UNSUPPORTED_PROVIDER_CHANGE = 10
        ERROR_CODE_UNSUPPORTED_TFVAR_CHANGE = 11

    resource_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file: str = proto.Field(
        proto.STRING,
        number=2,
    )
    range_: "CodeRange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CodeRange",
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=Type,
    )
    error_code: ErrorCode = proto.Field(
        proto.ENUM,
        number=6,
        enum=ErrorCode,
    )


class CodeRange(proto.Message):
    r"""CodeRange represents a portion of code.

    Attributes:
        start (google.cloud.designcenter_v1.types.CodePosition):
            Output only. Start position.
        end (google.cloud.designcenter_v1.types.CodePosition):
            Output only. End position.
    """

    start: "CodePosition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CodePosition",
    )
    end: "CodePosition" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CodePosition",
    )


class CodePosition(proto.Message):
    r"""CodePosition represents a code location.

    Attributes:
        line (int):
            Output only. One-based line count of the
            relevant position.
        byte_offset (int):
            Output only. Byte offset in the content.
        column (int):
            Output only. One-based column count of the
            relevant position.
    """

    line: int = proto.Field(
        proto.INT32,
        number=1,
    )
    byte_offset: int = proto.Field(
        proto.INT32,
        number=2,
    )
    column: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
