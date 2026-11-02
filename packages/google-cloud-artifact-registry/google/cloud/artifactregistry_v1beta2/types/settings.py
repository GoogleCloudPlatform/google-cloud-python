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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1beta2",
    manifest={
        "ProjectSettings",
        "GetProjectSettingsRequest",
        "UpdateProjectSettingsRequest",
    },
)


class ProjectSettings(proto.Message):
    r"""The Artifact Registry settings that apply to a Project.

    Attributes:
        name (str):
            The name of the project's settings.

            Always of the form:

            projects/{project-id}/projectSettings

            In update request: never set
            In response: always set
        legacy_redirection_state (google.cloud.artifactregistry_v1beta2.types.ProjectSettings.RedirectionState):
            The redirection state of the legacy
            repositories in this project.
    """

    class RedirectionState(proto.Enum):
        r"""The possible redirection states for legacy repositories.

        Values:
            REDIRECTION_STATE_UNSPECIFIED (0):
                No redirection status has been set.
            REDIRECTION_FROM_GCR_IO_DISABLED (1):
                Redirection is disabled.
            REDIRECTION_FROM_GCR_IO_ENABLED (2):
                Redirection is enabled.
            REDIRECTION_FROM_GCR_IO_FINALIZED (3):
                Redirection is enabled, and has been
                finalized so cannot be reverted.
        """

        REDIRECTION_STATE_UNSPECIFIED = 0
        REDIRECTION_FROM_GCR_IO_DISABLED = 1
        REDIRECTION_FROM_GCR_IO_ENABLED = 2
        REDIRECTION_FROM_GCR_IO_FINALIZED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    legacy_redirection_state: RedirectionState = proto.Field(
        proto.ENUM,
        number=2,
        enum=RedirectionState,
    )


class GetProjectSettingsRequest(proto.Message):
    r"""Gets the redirection status for a project.

    Attributes:
        name (str):
            Required. The name of the projectSettings
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateProjectSettingsRequest(proto.Message):
    r"""Sets the settings of the project.

    Attributes:
        project_settings (google.cloud.artifactregistry_v1beta2.types.ProjectSettings):
            The project settings.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask to support partial updates.
    """

    project_settings: "ProjectSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProjectSettings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
