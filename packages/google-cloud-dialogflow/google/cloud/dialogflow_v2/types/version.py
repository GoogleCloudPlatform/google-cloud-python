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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "Version",
        "ListVersionsRequest",
        "ListVersionsResponse",
        "GetVersionRequest",
        "CreateVersionRequest",
        "UpdateVersionRequest",
        "DeleteVersionRequest",
    },
)


class Version(proto.Message):
    r"""You can create multiple versions of your agent and publish them to
    separate environments.

    When you edit an agent, you are editing the draft agent. At any
    point, you can save the draft agent as an agent version, which is an
    immutable snapshot of your agent.

    When you save the draft agent, it is published to the default
    environment. When you create agent versions, you can publish them to
    custom environments. You can create a variety of custom environments
    for:

    - testing
    - development
    - production
    - etc.

    For more information, see the `versions and environments
    guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

    Attributes:
        name (str):
            Output only. The unique identifier of this agent version.
            Supported formats:

            - ``projects/<Project ID>/agent/versions/<Version ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>``
        description (str):
            Optional. The developer-provided description
            of this version.
        version_number (int):
            Output only. The sequential number of this
            version. This field is read-only which means it
            cannot be set by create and update methods.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of this
            version. This field is read-only, i.e., it
            cannot be set by create and update methods.
        status (google.cloud.dialogflow_v2.types.Version.VersionStatus):
            Output only. The status of this version. This
            field is read-only and cannot be set by create
            and update methods.
    """

    class VersionStatus(proto.Enum):
        r"""The status of a version.

        Values:
            VERSION_STATUS_UNSPECIFIED (0):
                Not specified. This value is not used.
            IN_PROGRESS (1):
                Version is not ready to serve (e.g. training
                is in progress).
            READY (2):
                Version is ready to serve.
            FAILED (3):
                Version training failed.
        """

        VERSION_STATUS_UNSPECIFIED = 0
        IN_PROGRESS = 1
        READY = 2
        FAILED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version_number: int = proto.Field(
        proto.INT32,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    status: VersionStatus = proto.Field(
        proto.ENUM,
        number=6,
        enum=VersionStatus,
    )


class ListVersionsRequest(proto.Message):
    r"""The request message for
    [Versions.ListVersions][google.cloud.dialogflow.v2.Versions.ListVersions].

    Attributes:
        parent (str):
            Required. The agent to list all versions from. Supported
            formats:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
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
    [Versions.ListVersions][google.cloud.dialogflow.v2.Versions.ListVersions].

    Attributes:
        versions (MutableSequence[google.cloud.dialogflow_v2.types.Version]):
            The list of agent versions. There will be a maximum number
            of items returned based on the page_size field in the
            request.
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
    [Versions.GetVersion][google.cloud.dialogflow.v2.Versions.GetVersion].

    Attributes:
        name (str):
            Required. The name of the version. Supported formats:

            - ``projects/<Project ID>/agent/versions/<Version ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVersionRequest(proto.Message):
    r"""The request message for
    [Versions.CreateVersion][google.cloud.dialogflow.v2.Versions.CreateVersion].

    Attributes:
        parent (str):
            Required. The agent to create a version for. Supported
            formats:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
        version (google.cloud.dialogflow_v2.types.Version):
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
    [Versions.UpdateVersion][google.cloud.dialogflow.v2.Versions.UpdateVersion].

    Attributes:
        version (google.cloud.dialogflow_v2.types.Version):
            Required. The version to update. Supported formats:

            - ``projects/<Project ID>/agent/versions/<Version ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated.
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
    [Versions.DeleteVersion][google.cloud.dialogflow.v2.Versions.DeleteVersion].

    Attributes:
        name (str):
            Required. The name of the version to delete. Supported
            formats:

            - ``projects/<Project ID>/agent/versions/<Version ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
