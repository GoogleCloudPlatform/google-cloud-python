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

from google.ads.admanager_v1.types import dai_encoding_profile_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetDaiEncodingProfileRequest",
        "ListDaiEncodingProfilesRequest",
        "ListDaiEncodingProfilesResponse",
        "CreateDaiEncodingProfileRequest",
        "BatchCreateDaiEncodingProfilesRequest",
        "BatchCreateDaiEncodingProfilesResponse",
        "UpdateDaiEncodingProfileRequest",
        "BatchUpdateDaiEncodingProfilesRequest",
        "BatchUpdateDaiEncodingProfilesResponse",
        "BatchActivateDaiEncodingProfilesRequest",
        "BatchActivateDaiEncodingProfilesResponse",
        "ActivateDaiEncodingProfileRequest",
        "BatchArchiveDaiEncodingProfilesRequest",
        "BatchArchiveDaiEncodingProfilesResponse",
        "ArchiveDaiEncodingProfileRequest",
    },
)


class GetDaiEncodingProfileRequest(proto.Message):
    r"""Request object for ``GetDaiEncodingProfile`` method.

    Attributes:
        name (str):
            Required. The resource name of the DaiEncodingProfile.
            Format:
            ``networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDaiEncodingProfilesRequest(proto.Message):
    r"""Request object for ``ListDaiEncodingProfiles`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            DaiEncodingProfiles. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``DaiEncodingProfiles`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``DaiEncodingProfiles`` will be
            returned. The maximum value is 1000; values above 1000 will
            be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDaiEncodingProfiles`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListDaiEncodingProfiles`` must match the call that
            provided the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``containerType``
            - ``displayName``
            - ``name``
            - ``status``
            - ``variantType``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListDaiEncodingProfilesResponse(proto.Message):
    r"""Response object for ``ListDaiEncodingProfilesRequest`` containing
    matching ``DaiEncodingProfile`` objects.

    Attributes:
        dai_encoding_profiles (MutableSequence[google.ads.admanager_v1.types.DaiEncodingProfile]):
            The ``DaiEncodingProfile`` objects from the specified
            network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``DaiEncodingProfile`` objects. If a filter
            was included in the request, this reflects the total number
            after the filtering is applied.

            ``total_size`` will not be calculated in the response unless
            it has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    dai_encoding_profiles: MutableSequence[
        dai_encoding_profile_messages.DaiEncodingProfile
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=dai_encoding_profile_messages.DaiEncodingProfile,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateDaiEncodingProfileRequest(proto.Message):
    r"""Request object for ``CreateDaiEncodingProfile`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``DaiEncodingProfile`` will be created. Format:
            ``networks/{network_code}``
        dai_encoding_profile (google.ads.admanager_v1.types.DaiEncodingProfile):
            Required. The ``DaiEncodingProfile`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dai_encoding_profile: dai_encoding_profile_messages.DaiEncodingProfile = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=dai_encoding_profile_messages.DaiEncodingProfile,
        )
    )


class BatchCreateDaiEncodingProfilesRequest(proto.Message):
    r"""Request object for ``BatchCreateDaiEncodingProfiles`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``DaiEncodingProfiles``
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreateDaiEncodingProfileRequest must
            match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateDaiEncodingProfileRequest]):
            Required. The ``DaiEncodingProfile`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateDaiEncodingProfileRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateDaiEncodingProfileRequest",
    )


class BatchCreateDaiEncodingProfilesResponse(proto.Message):
    r"""Response object for ``BatchCreateDaiEncodingProfiles`` method.

    Attributes:
        dai_encoding_profiles (MutableSequence[google.ads.admanager_v1.types.DaiEncodingProfile]):
            The ``DaiEncodingProfile`` objects created.
    """

    dai_encoding_profiles: MutableSequence[
        dai_encoding_profile_messages.DaiEncodingProfile
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=dai_encoding_profile_messages.DaiEncodingProfile,
    )


class UpdateDaiEncodingProfileRequest(proto.Message):
    r"""Request object for ``UpdateDaiEncodingProfile`` method.

    Attributes:
        dai_encoding_profile (google.ads.admanager_v1.types.DaiEncodingProfile):
            Required. The ``DaiEncodingProfile`` to update.

            The ``DaiEncodingProfile``'s ``name`` is used to identify
            the ``DaiEncodingProfile`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    dai_encoding_profile: dai_encoding_profile_messages.DaiEncodingProfile = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=dai_encoding_profile_messages.DaiEncodingProfile,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateDaiEncodingProfilesRequest(proto.Message):
    r"""Request object for ``BatchUpdateDaiEncodingProfiles`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``DaiEncodingProfiles``
            will be updated. Format: ``networks/{network_code}`` The
            parent field in the UpdateDaiEncodingProfileRequest must
            match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateDaiEncodingProfileRequest]):
            Required. The ``DaiEncodingProfile`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateDaiEncodingProfileRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateDaiEncodingProfileRequest",
    )


class BatchUpdateDaiEncodingProfilesResponse(proto.Message):
    r"""Response object for ``BatchUpdateDaiEncodingProfiles`` method.

    Attributes:
        dai_encoding_profiles (MutableSequence[google.ads.admanager_v1.types.DaiEncodingProfile]):
            The ``DaiEncodingProfile`` objects updated.
    """

    dai_encoding_profiles: MutableSequence[
        dai_encoding_profile_messages.DaiEncodingProfile
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=dai_encoding_profile_messages.DaiEncodingProfile,
    )


class BatchActivateDaiEncodingProfilesRequest(proto.Message):
    r"""Request object for ``BatchActivateDaiEncodingProfiles`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        requests (MutableSequence[google.ads.admanager_v1.types.ActivateDaiEncodingProfileRequest]):
            Required. The ``DaiEncodingProfile`` objects to activate. A
            maximum of 100 objects can be activated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["ActivateDaiEncodingProfileRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="ActivateDaiEncodingProfileRequest",
        )
    )


class BatchActivateDaiEncodingProfilesResponse(proto.Message):
    r"""Response object for ``BatchActivateDaiEncodingProfiles`` method."""


class ActivateDaiEncodingProfileRequest(proto.Message):
    r"""Request object for ``ActivateDaiEncodingProfile`` method.

    Attributes:
        name (str):
            Required. The resource name of the DaiEncodingProfile to
            activate. Format:
            ``networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchArchiveDaiEncodingProfilesRequest(proto.Message):
    r"""Request object for ``BatchArchiveDaiEncodingProfiles`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        requests (MutableSequence[google.ads.admanager_v1.types.ArchiveDaiEncodingProfileRequest]):
            Required. The ``DaiEncodingProfile`` objects to archive. A
            maximum of 100 objects can be archived in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["ArchiveDaiEncodingProfileRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ArchiveDaiEncodingProfileRequest",
    )


class BatchArchiveDaiEncodingProfilesResponse(proto.Message):
    r"""Response object for ``BatchArchiveDaiEncodingProfiles`` method."""


class ArchiveDaiEncodingProfileRequest(proto.Message):
    r"""Request object for ``ArchiveDaiEncodingProfile`` method.

    Attributes:
        name (str):
            Required. The resource name of the DaiEncodingProfile to
            archive. Format:
            ``networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
