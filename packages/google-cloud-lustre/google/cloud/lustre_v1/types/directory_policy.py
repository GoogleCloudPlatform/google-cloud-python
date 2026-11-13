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
    package="google.cloud.lustre.v1",
    manifest={
        "DirectoryPolicy",
        "CreateDirectoryPolicyRequest",
        "DeleteDirectoryPolicyRequest",
        "GetDirectoryPolicyRequest",
        "ListDirectoryPoliciesRequest",
        "ListDirectoryPoliciesResponse",
    },
)


class DirectoryPolicy(proto.Message):
    r"""A directory policy for a Managed Lustre instance.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of the directory
            policy. DirectoryPolicy names have the form
            ``projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}``.
            {id} is user provided.
        directory_path (str):
            Required. Immutable. The lustre instance
            filesystem full path of the directory. It must
            start with a slash. e.g. /lustre/testFolder
        lustre_project_id (int):
            Output only. The lustre project ID assigned for the
            directory by the service. This read-only ID can be used to
            manage quotas. See more details in
            https://docs.cloud.google.com/managed-lustre/docs/file-system-quotas#set_quotas
        uid (str):
            Output only. Unique ID of the resource.
        state (google.cloud.lustre_v1.types.DirectoryPolicy.State):
            Output only. The current state of the
            directory policy.
    """

    class State(proto.Enum):
        r"""State of the directory policy.

        Values:
            STATE_UNSPECIFIED (0):
                State is unspecified.
            CREATING (1):
                Directory policy is being created.
            ACTIVE (2):
                Directory policy is active and ready to be
                used.
            DELETING (3):
                Directory policy is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    directory_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lustre_project_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )


class CreateDirectoryPolicyRequest(proto.Message):
    r"""Request message for CreateDirectoryPolicy.

    Attributes:
        parent (str):
            Required. The parent instance. It must be in the format of
            ``projects/{project}/locations/{location}/instances/{instance}``.
        directory_policy_id (str):
            Required. The ID for the DirectoryPolicy to
            create.
        directory_policy (google.cloud.lustre_v1.types.DirectoryPolicy):
            Required. The directory policy to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    directory_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    directory_policy: "DirectoryPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DirectoryPolicy",
    )


class DeleteDirectoryPolicyRequest(proto.Message):
    r"""Request message for DeleteDirectoryPolicy.

    Attributes:
        name (str):
            Required. The resource name of the directory policy.
            DirectoryPolicy names have the form
            ``projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetDirectoryPolicyRequest(proto.Message):
    r"""Request message for GetDirectoryPolicy.

    Attributes:
        name (str):
            Required. The resource name of the directory policy.
            DirectoryPolicy names have the form
            ``projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDirectoryPoliciesRequest(proto.Message):
    r"""Request message for ListDirectoryPolicies.

    Attributes:
        parent (str):
            Required. The parent instance. It must be in the format of
            ``projects/{project}/locations/{location}/instances/{instance}``.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer items than requested. If
            unspecified, the server will pick an appropriate
            default. The maximum value is 1000; values above
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDirectoryPolicies`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListDirectoryPolicies`` must match the call
            that provided the page token.
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


class ListDirectoryPoliciesResponse(proto.Message):
    r"""Response message for ListDirectoryPolicies.

    Attributes:
        directory_policies (MutableSequence[google.cloud.lustre_v1.types.DirectoryPolicy]):
            The list of DirectoryPolicies.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    directory_policies: MutableSequence["DirectoryPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DirectoryPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
