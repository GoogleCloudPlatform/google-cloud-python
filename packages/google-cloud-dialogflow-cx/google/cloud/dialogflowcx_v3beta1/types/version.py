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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflowcx_v3beta1.types import flow

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "CreateVersionOperationMetadata",
        "Version",
        "ListVersionsRequest",
        "ListVersionsResponse",
        "GetVersionRequest",
        "CreateVersionRequest",
        "UpdateVersionRequest",
        "DeleteVersionRequest",
        "LoadVersionRequest",
        "CompareVersionsRequest",
        "CompareVersionsResponse",
    },
)


class CreateVersionOperationMetadata(proto.Message):
    r"""Metadata associated with the long running operation for
    [Versions.CreateVersion][google.cloud.dialogflow.cx.v3beta1.Versions.CreateVersion].

    Attributes:
        version (str):
            Name of the created version. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Version(proto.Message):
    r"""Represents a version of a flow.

    Attributes:
        name (str):
            Format:

            projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>.
            Version ID is a self-increasing number generated
            by Dialogflow upon version creation.
        display_name (str):
            Required. The human-readable name of the
            version. Limit of 64 characters.
        description (str):
            The description of the version. The maximum
            length is 500 characters. If exceeded, the
            request is rejected.
        nlu_settings (google.cloud.dialogflowcx_v3beta1.types.NluSettings):
            Output only. The NLU settings of the flow at
            version creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the version.
        state (google.cloud.dialogflowcx_v3beta1.types.Version.State):
            Output only. The state of this version. This
            field is read-only and cannot be set by create
            and update methods.
    """

    class State(proto.Enum):
        r"""The state of the version.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified. This value is not used.
            RUNNING (1):
                Version is not ready to serve (e.g. training
                is running).
            SUCCEEDED (2):
                Training has succeeded and this version is
                ready to serve.
            FAILED (3):
                Version training failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        FAILED = 3

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
    nlu_settings: flow.NluSettings = proto.Field(
        proto.MESSAGE,
        number=4,
        message=flow.NluSettings,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )


class ListVersionsRequest(proto.Message):
    r"""The request message for
    [Versions.ListVersions][google.cloud.dialogflow.cx.v3beta1.Versions.ListVersions].

    Attributes:
        parent (str):
            Required. The
            [Flow][google.cloud.dialogflow.cx.v3beta1.Flow] to list all
            versions for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 20 and at most 100.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
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


class ListVersionsResponse(proto.Message):
    r"""The response message for
    [Versions.ListVersions][google.cloud.dialogflow.cx.v3beta1.Versions.ListVersions].

    Attributes:
        versions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Version]):
            A list of versions. There will be a maximum number of items
            returned based on the page_size field in the request. The
            list may in some cases be empty or contain fewer entries
            than page_size even if this isn't the last page.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    versions: MutableSequence["Version"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Version",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVersionRequest(proto.Message):
    r"""The request message for
    [Versions.GetVersion][google.cloud.dialogflow.cx.v3beta1.Versions.GetVersion].

    Attributes:
        name (str):
            Required. The name of the
            [Version][google.cloud.dialogflow.cx.v3beta1.Version].
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVersionRequest(proto.Message):
    r"""The request message for
    [Versions.CreateVersion][google.cloud.dialogflow.cx.v3beta1.Versions.CreateVersion].

    Attributes:
        parent (str):
            Required. The
            [Flow][google.cloud.dialogflow.cx.v3beta1.Flow] to create an
            [Version][google.cloud.dialogflow.cx.v3beta1.Version] for.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        version (google.cloud.dialogflowcx_v3beta1.types.Version):
            Required. The version to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: "Version" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Version",
    )


class UpdateVersionRequest(proto.Message):
    r"""The request message for
    [Versions.UpdateVersion][google.cloud.dialogflow.cx.v3beta1.Versions.UpdateVersion].

    Attributes:
        version (google.cloud.dialogflowcx_v3beta1.types.Version):
            Required. The version to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields get updated.
            Currently only ``description`` and ``display_name`` can be
            updated.
    """

    version: "Version" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Version",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteVersionRequest(proto.Message):
    r"""The request message for
    [Versions.DeleteVersion][google.cloud.dialogflow.cx.v3beta1.Versions.DeleteVersion].

    Attributes:
        name (str):
            Required. The name of the
            [Version][google.cloud.dialogflow.cx.v3beta1.Version] to
            delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LoadVersionRequest(proto.Message):
    r"""The request message for
    [Versions.LoadVersion][google.cloud.dialogflow.cx.v3beta1.Versions.LoadVersion].

    Attributes:
        name (str):
            Required. The
            [Version][google.cloud.dialogflow.cx.v3beta1.Version] to be
            loaded to draft flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
        allow_override_agent_resources (bool):
            This field is used to prevent accidental overwrite of other
            agent resources, which can potentially impact other flow's
            behavior. If ``allow_override_agent_resources`` is false,
            conflicted agent-level resources will not be overridden
            (i.e. intents, entities, webhooks).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_override_agent_resources: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CompareVersionsRequest(proto.Message):
    r"""The request message for
    [Versions.CompareVersions][google.cloud.dialogflow.cx.v3beta1.Versions.CompareVersions].

    Attributes:
        base_version (str):
            Required. Name of the base flow version to compare with the
            target version. Use version ID ``0`` to indicate the draft
            version of the specified flow.

            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
        target_version (str):
            Required. Name of the target flow version to compare with
            the base version. Use version ID ``0`` to indicate the draft
            version of the specified flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
        language_code (str):
            The language to compare the flow versions for.

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    base_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CompareVersionsResponse(proto.Message):
    r"""The response message for
    [Versions.CompareVersions][google.cloud.dialogflow.cx.v3beta1.Versions.CompareVersions].

    Attributes:
        base_version_content_json (str):
            JSON representation of the base version
            content.
        target_version_content_json (str):
            JSON representation of the target version
            content.
        compare_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the two version compares.
    """

    base_version_content_json: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_version_content_json: str = proto.Field(
        proto.STRING,
        number=2,
    )
    compare_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
