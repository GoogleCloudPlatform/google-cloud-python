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

from google.cloud.iam_v3beta.types import (
    access_policy_resources,
    policy_binding_resources,
)

__protobuf__ = proto.module(
    package="google.iam.v3beta",
    manifest={
        "CreateAccessPolicyRequest",
        "GetAccessPolicyRequest",
        "UpdateAccessPolicyRequest",
        "DeleteAccessPolicyRequest",
        "ListAccessPoliciesRequest",
        "ListAccessPoliciesResponse",
        "SearchAccessPolicyBindingsRequest",
        "SearchAccessPolicyBindingsResponse",
    },
)


class CreateAccessPolicyRequest(proto.Message):
    r"""Request message for CreateAccessPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource where this access policy will
            be created.

            Format: ``projects/{project_id}/locations/{location}``
            ``projects/{project_number}/locations/{location}``
            ``folders/{folder_id}/locations/{location}``
            ``organizations/{organization_id}/locations/{location}``
        access_policy_id (str):
            Required. The ID to use for the access policy, which will
            become the final component of the access policy's resource
            name.

            This value must start with a lowercase letter followed by up
            to 62 lowercase letters, numbers, hyphens, or dots. Pattern,
            /[a-z][a-z0-9-.]{2,62}/.

            This value must be unique among all access policies with the
            same parent.
        access_policy (google.cloud.iam_v3beta.types.AccessPolicy):
            Required. The access policy to create.
        validate_only (bool):
            Optional. If set, validate the request and
            preview the creation, but do not actually post
            it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    access_policy: access_policy_resources.AccessPolicy = proto.Field(
        proto.MESSAGE,
        number=3,
        message=access_policy_resources.AccessPolicy,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetAccessPolicyRequest(proto.Message):
    r"""Request message for GetAccessPolicy method.

    Attributes:
        name (str):
            Required. The name of the access policy to retrieve.

            Format:
            ``projects/{project_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``projects/{project_number}/locations/{location}/accessPolicies/{access_policy_id}``
            ``folders/{folder_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``organizations/{organization_id}/locations/{location}/accessPolicies/{access_policy_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAccessPolicyRequest(proto.Message):
    r"""Request message for UpdateAccessPolicy method.

    Attributes:
        access_policy (google.cloud.iam_v3beta.types.AccessPolicy):
            Required. The access policy to update.

            The access policy's ``name`` field is used to identify the
            policy to update.
        validate_only (bool):
            Optional. If set, validate the request and
            preview the update, but do not actually post it.
    """

    access_policy: access_policy_resources.AccessPolicy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=access_policy_resources.AccessPolicy,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DeleteAccessPolicyRequest(proto.Message):
    r"""Request message for DeleteAccessPolicy method.

    Attributes:
        name (str):
            Required. The name of the access policy to delete.

            Format:
            ``projects/{project_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``projects/{project_number}/locations/{location}/accessPolicies/{access_policy_id}``
            ``folders/{folder_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``organizations/{organization_id}/locations/{location}/accessPolicies/{access_policy_id}``
        etag (str):
            Optional. The etag of the access policy. If
            this is provided, it must match the server's
            etag.
        validate_only (bool):
            Optional. If set, validate the request and
            preview the deletion, but do not actually post
            it.
        force (bool):
            Optional. If set to true, the request will
            force the deletion of the Policy even if the
            Policy references PolicyBindings.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListAccessPoliciesRequest(proto.Message):
    r"""Request message for ListAccessPolicies method.

    Attributes:
        parent (str):
            Required. The parent resource, which owns the collection of
            access policy resources.

            Format: ``projects/{project_id}/locations/{location}``
            ``projects/{project_number}/locations/{location}``
            ``folders/{folder_id}/locations/{location}``
            ``organizations/{organization_id}/locations/{location}``
        page_size (int):
            Optional. The maximum number of access
            policies to return. The service may return fewer
            than this value.

            If unspecified, at most 50 access policies will
            be returned. Valid value ranges from 1 to 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccessPolicies`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAccessPolicies`` must match the call that provided the
            page token.
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


class ListAccessPoliciesResponse(proto.Message):
    r"""Response message for ListAccessPolicies method.

    Attributes:
        access_policies (MutableSequence[google.cloud.iam_v3beta.types.AccessPolicy]):
            The access policies from the specified
            parent.
        next_page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    access_policies: MutableSequence[access_policy_resources.AccessPolicy] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=access_policy_resources.AccessPolicy,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchAccessPolicyBindingsRequest(proto.Message):
    r"""Request message for SearchAccessPolicyBindings rpc.

    Attributes:
        name (str):
            Required. The name of the access policy. Format:
            ``organizations/{organization_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``folders/{folder_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``projects/{project_id}/locations/{location}/accessPolicies/{access_policy_id}``
            ``projects/{project_number}/locations/{location}/accessPolicies/{access_policy_id}``
        page_size (int):
            Optional. The maximum number of policy
            bindings to return. The service may return fewer
            than this value.

            If unspecified, at most 50 policy bindings will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``SearchAccessPolicyBindingsRequest`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``SearchAccessPolicyBindingsRequest`` must match the call
            that provided the page token.
    """

    name: str = proto.Field(
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


class SearchAccessPolicyBindingsResponse(proto.Message):
    r"""Response message for SearchAccessPolicyBindings rpc.

    Attributes:
        policy_bindings (MutableSequence[google.cloud.iam_v3beta.types.PolicyBinding]):
            The policy bindings that reference the
            specified policy.
        next_page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    policy_bindings: MutableSequence[policy_binding_resources.PolicyBinding] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=policy_binding_resources.PolicyBinding,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
