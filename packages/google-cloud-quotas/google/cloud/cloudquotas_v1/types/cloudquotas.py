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

from google.cloud.cloudquotas_v1.types import resources

__protobuf__ = proto.module(
    package="google.api.cloudquotas.v1",
    manifest={
        "ListQuotaInfosRequest",
        "ListQuotaInfosResponse",
        "GetQuotaInfoRequest",
        "ListQuotaPreferencesRequest",
        "ListQuotaPreferencesResponse",
        "GetQuotaPreferenceRequest",
        "CreateQuotaPreferenceRequest",
        "UpdateQuotaPreferenceRequest",
    },
)


class ListQuotaInfosRequest(proto.Message):
    r"""Message for requesting list of QuotaInfos

    Attributes:
        parent (str):
            Required. Identifier. Parent value of QuotaInfo resources.
            Listing across different resource containers (such as
            'projects/-') is not allowed.

            Example names:
            ``projects/123/locations/global/services/compute.googleapis.com``
            ``folders/234/locations/global/services/compute.googleapis.com``
            ``organizations/345/locations/global/services/compute.googleapis.com``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListQuotaInfosResponse(proto.Message):
    r"""Message for response to listing QuotaInfos

    Attributes:
        quota_infos (MutableSequence[google.cloud.cloudquotas_v1.types.QuotaInfo]):
            The list of QuotaInfo
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    quota_infos: MutableSequence[resources.QuotaInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.QuotaInfo,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetQuotaInfoRequest(proto.Message):
    r"""Message for getting a QuotaInfo

    Attributes:
        name (str):
            Required. Identifier. The resource name of the quota info.

            An example name:
            ``projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListQuotaPreferencesRequest(proto.Message):
    r"""Message for requesting list of QuotaPreferences

    Attributes:
        parent (str):
            Required. Identifier. Parent value of QuotaPreference
            resources. Listing across different resource containers
            (such as 'projects/-') is not allowed.

            When the value starts with 'folders' or 'organizations', it
            lists the QuotaPreferences for org quotas in the container.
            It does not list the QuotaPreferences in the descendant
            projects of the container.

            Example parents: ``projects/123/locations/global``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filter result QuotaPreferences by their state,
            type, create/update time range.

            Example filters:
            ``reconciling=true AND request_type=CLOUD_CONSOLE``,
            ``reconciling=true OR creation_time>2022-12-03T10:30:00``
        order_by (str):
            Optional. How to order of the results. By default, the
            results are ordered by create time.

            Example orders: ``quota_id``, ``service, create_time``
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListQuotaPreferencesResponse(proto.Message):
    r"""Message for response to listing QuotaPreferences

    Attributes:
        quota_preferences (MutableSequence[google.cloud.cloudquotas_v1.types.QuotaPreference]):
            The list of QuotaPreference
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    quota_preferences: MutableSequence[resources.QuotaPreference] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.QuotaPreference,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetQuotaPreferenceRequest(proto.Message):
    r"""Message for getting a QuotaPreference

    Attributes:
        name (str):
            Required. Identifier. Name of the resource

            Example name:
            ``projects/123/locations/global/quota_preferences/my-config-for-us-east1``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateQuotaPreferenceRequest(proto.Message):
    r"""Message for creating a QuotaPreference

    Attributes:
        parent (str):
            Required. Identifier. Value for parent.

            Example: ``projects/123/locations/global``
        quota_preference_id (str):
            Optional. Id of the requesting object, must
            be unique under its parent. If client does not
            set this field, the service will generate one.
        quota_preference (google.cloud.cloudquotas_v1.types.QuotaPreference):
            Required. The resource being created
        ignore_safety_checks (MutableSequence[google.cloud.cloudquotas_v1.types.QuotaSafetyCheck]):
            The list of quota safety checks to be
            ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    quota_preference_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    quota_preference: resources.QuotaPreference = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.QuotaPreference,
    )
    ignore_safety_checks: MutableSequence[resources.QuotaSafetyCheck] = (
        proto.RepeatedField(
            proto.ENUM,
            number=4,
            enum=resources.QuotaSafetyCheck,
        )
    )


class UpdateQuotaPreferenceRequest(proto.Message):
    r"""Message for updating a QuotaPreference

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the QuotaPreference resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        quota_preference (google.cloud.cloudquotas_v1.types.QuotaPreference):
            Required. The resource being updated
        allow_missing (bool):
            Optional. If set to true, and the quota preference is not
            found, a new one will be created. In this situation,
            ``update_mask`` is ignored.
        validate_only (bool):
            Optional. If set to true, validate the
            request, but do not actually update. Note that a
            request being valid does not mean that the
            request is guaranteed to be fulfilled.
        ignore_safety_checks (MutableSequence[google.cloud.cloudquotas_v1.types.QuotaSafetyCheck]):
            The list of quota safety checks to be
            ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    quota_preference: resources.QuotaPreference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.QuotaPreference,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    ignore_safety_checks: MutableSequence[resources.QuotaSafetyCheck] = (
        proto.RepeatedField(
            proto.ENUM,
            number=5,
            enum=resources.QuotaSafetyCheck,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
