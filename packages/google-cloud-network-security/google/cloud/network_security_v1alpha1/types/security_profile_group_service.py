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

from google.cloud.network_security_v1alpha1.types import (
    security_profile_group as gcn_security_profile_group,
)

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "ListSecurityProfileGroupsRequest",
        "ListSecurityProfileGroupsResponse",
        "GetSecurityProfileGroupRequest",
        "CreateSecurityProfileGroupRequest",
        "UpdateSecurityProfileGroupRequest",
        "DeleteSecurityProfileGroupRequest",
        "ListSecurityProfilesRequest",
        "ListSecurityProfilesResponse",
        "GetSecurityProfileRequest",
        "CreateSecurityProfileRequest",
        "UpdateSecurityProfileRequest",
        "DeleteSecurityProfileRequest",
    },
)


class ListSecurityProfileGroupsRequest(proto.Message):
    r"""Request used with the ListSecurityProfileGroups method.

    Attributes:
        parent (str):
            Required. The project or organization and location from
            which the SecurityProfileGroups should be listed, specified
            in the format
            ``projects|organizations/*/locations/{location}``.
        page_size (int):
            Maximum number of SecurityProfileGroups to
            return per call.
        page_token (str):
            The value returned by the last
            ``ListSecurityProfileGroupsResponse`` Indicates that this is
            a continuation of a prior ``ListSecurityProfileGroups``
            call, and that the system should return the next page of
            data.
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


class ListSecurityProfileGroupsResponse(proto.Message):
    r"""Response returned by the ListSecurityProfileGroups method.

    Attributes:
        security_profile_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.SecurityProfileGroup]):
            List of SecurityProfileGroups resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    security_profile_groups: MutableSequence[
        gcn_security_profile_group.SecurityProfileGroup
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_security_profile_group.SecurityProfileGroup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSecurityProfileGroupRequest(proto.Message):
    r"""Request used by the GetSecurityProfileGroup method.

    Attributes:
        name (str):
            Required. A name of the SecurityProfileGroup to get. Must be
            in the format
            ``projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSecurityProfileGroupRequest(proto.Message):
    r"""Request used by the CreateSecurityProfileGroup method.

    Attributes:
        parent (str):
            Required. The parent resource of the SecurityProfileGroup.
            Must be in the format
            ``projects|organizations/*/locations/{location}``.
        security_profile_group_id (str):
            Required. Short name of the SecurityProfileGroup resource to
            be created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g.
            "security_profile_group1".
        security_profile_group (google.cloud.network_security_v1alpha1.types.SecurityProfileGroup):
            Required. SecurityProfileGroup resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    security_profile_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    security_profile_group: gcn_security_profile_group.SecurityProfileGroup = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcn_security_profile_group.SecurityProfileGroup,
        )
    )


class UpdateSecurityProfileGroupRequest(proto.Message):
    r"""Request used by the UpdateSecurityProfileGroup method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the SecurityProfileGroup resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask.
        security_profile_group (google.cloud.network_security_v1alpha1.types.SecurityProfileGroup):
            Required. Updated SecurityProfileGroup
            resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    security_profile_group: gcn_security_profile_group.SecurityProfileGroup = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=gcn_security_profile_group.SecurityProfileGroup,
        )
    )


class DeleteSecurityProfileGroupRequest(proto.Message):
    r"""Request used by the DeleteSecurityProfileGroup method.

    Attributes:
        name (str):
            Required. A name of the SecurityProfileGroup to delete. Must
            be in the format
            ``projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}``.
        etag (str):
            Optional. If client provided etag is out of date, delete
            will return FAILED_PRECONDITION error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSecurityProfilesRequest(proto.Message):
    r"""Request used with the ListSecurityProfiles method.

    Attributes:
        parent (str):
            Required. The project or organization and location from
            which the SecurityProfiles should be listed, specified in
            the format
            ``projects|organizations/*/locations/{location}``.
        page_size (int):
            Maximum number of SecurityProfiles to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListSecurityProfilesResponse`` Indicates that this is a
            continuation of a prior ``ListSecurityProfiles`` call, and
            that the system should return the next page of data.
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


class ListSecurityProfilesResponse(proto.Message):
    r"""Response returned by the ListSecurityProfiles method.

    Attributes:
        security_profiles (MutableSequence[google.cloud.network_security_v1alpha1.types.SecurityProfile]):
            List of SecurityProfile resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    security_profiles: MutableSequence[gcn_security_profile_group.SecurityProfile] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcn_security_profile_group.SecurityProfile,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSecurityProfileRequest(proto.Message):
    r"""Request used by the GetSecurityProfile method.

    Attributes:
        name (str):
            Required. A name of the SecurityProfile to get. Must be in
            the format
            ``projects|organizations/*/locations/{location}/securityProfiles/{security_profile_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSecurityProfileRequest(proto.Message):
    r"""Request used by the CreateSecurityProfile method.

    Attributes:
        parent (str):
            Required. The parent resource of the SecurityProfile. Must
            be in the format
            ``projects|organizations/*/locations/{location}``.
        security_profile_id (str):
            Required. Short name of the SecurityProfile resource to be
            created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g.
            "security_profile1".
        security_profile (google.cloud.network_security_v1alpha1.types.SecurityProfile):
            Required. SecurityProfile resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    security_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    security_profile: gcn_security_profile_group.SecurityProfile = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_security_profile_group.SecurityProfile,
    )


class UpdateSecurityProfileRequest(proto.Message):
    r"""Request used by the UpdateSecurityProfile method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the SecurityProfile resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.
        security_profile (google.cloud.network_security_v1alpha1.types.SecurityProfile):
            Required. Updated SecurityProfile resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    security_profile: gcn_security_profile_group.SecurityProfile = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcn_security_profile_group.SecurityProfile,
    )


class DeleteSecurityProfileRequest(proto.Message):
    r"""Request used by the DeleteSecurityProfile method.

    Attributes:
        name (str):
            Required. A name of the SecurityProfile to delete. Must be
            in the format
            ``projects|organizations/*/locations/{location}/securityProfiles/{security_profile_id}``.
        etag (str):
            Optional. If client provided etag is out of date, delete
            will return FAILED_PRECONDITION error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
