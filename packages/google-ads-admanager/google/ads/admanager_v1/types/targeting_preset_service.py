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

from google.ads.admanager_v1.types import targeting_preset_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetTargetingPresetRequest",
        "ListTargetingPresetsRequest",
        "ListTargetingPresetsResponse",
        "CreateTargetingPresetRequest",
        "BatchCreateTargetingPresetsRequest",
        "BatchCreateTargetingPresetsResponse",
        "UpdateTargetingPresetRequest",
        "BatchUpdateTargetingPresetsRequest",
        "BatchUpdateTargetingPresetsResponse",
        "DeactivateTargetingPresetRequest",
        "BatchDeactivateTargetingPresetsRequest",
        "BatchDeactivateTargetingPresetsResponse",
    },
)


class GetTargetingPresetRequest(proto.Message):
    r"""Request object for ``GetTargetingPreset`` method.

    Attributes:
        name (str):
            Required. The resource name of the TargetingPreset. Format:
            ``networks/{network_code}/targetingPresets/{targeting_preset_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTargetingPresetsRequest(proto.Message):
    r"""Request object for ``ListTargetingPresets`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            TargetingPresets. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``TargetingPresets`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``TargetingPresets`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTargetingPresets`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListTargetingPresets`` must match the call that provided
            the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``displayName``
            - ``name``
            - ``status``
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


class ListTargetingPresetsResponse(proto.Message):
    r"""Response object for ``ListTargetingPresetsRequest`` containing
    matching ``TargetingPreset`` objects.

    Attributes:
        targeting_presets (MutableSequence[google.ads.admanager_v1.types.TargetingPreset]):
            The ``TargetingPreset`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``TargetingPreset`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    targeting_presets: MutableSequence[targeting_preset_messages.TargetingPreset] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=targeting_preset_messages.TargetingPreset,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateTargetingPresetRequest(proto.Message):
    r"""Request object for ``CreateTargetingPreset`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``TargetingPreset``
            will be created. Format: ``networks/{network_code}``
        targeting_preset (google.ads.admanager_v1.types.TargetingPreset):
            Required. The ``TargetingPreset`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    targeting_preset: targeting_preset_messages.TargetingPreset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=targeting_preset_messages.TargetingPreset,
    )


class BatchCreateTargetingPresetsRequest(proto.Message):
    r"""Request object for ``BatchCreateTargetingPresets`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``TargetingPresets``
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreateTargetingPresetRequest must match
            this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateTargetingPresetRequest]):
            Required. The ``TargetingPreset`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateTargetingPresetRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateTargetingPresetRequest",
    )


class BatchCreateTargetingPresetsResponse(proto.Message):
    r"""Response object for ``BatchCreateTargetingPresets`` method.

    Attributes:
        targeting_presets (MutableSequence[google.ads.admanager_v1.types.TargetingPreset]):
            The ``TargetingPreset`` objects created.
    """

    targeting_presets: MutableSequence[targeting_preset_messages.TargetingPreset] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=targeting_preset_messages.TargetingPreset,
        )
    )


class UpdateTargetingPresetRequest(proto.Message):
    r"""Request object for ``UpdateTargetingPreset`` method.

    Attributes:
        targeting_preset (google.ads.admanager_v1.types.TargetingPreset):
            Required. The ``TargetingPreset`` to update.

            The ``TargetingPreset``'s ``name`` is used to identify the
            ``TargetingPreset`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    targeting_preset: targeting_preset_messages.TargetingPreset = proto.Field(
        proto.MESSAGE,
        number=1,
        message=targeting_preset_messages.TargetingPreset,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateTargetingPresetsRequest(proto.Message):
    r"""Request object for ``BatchUpdateTargetingPresets`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``TargetingPresets``
            will be updated. Format: ``networks/{network_code}`` The
            parent field in the UpdateTargetingPresetRequest must match
            this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateTargetingPresetRequest]):
            Required. The ``TargetingPreset`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateTargetingPresetRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateTargetingPresetRequest",
    )


class BatchUpdateTargetingPresetsResponse(proto.Message):
    r"""Response object for ``BatchUpdateTargetingPresets`` method.

    Attributes:
        targeting_presets (MutableSequence[google.ads.admanager_v1.types.TargetingPreset]):
            The ``TargetingPreset`` objects updated.
    """

    targeting_presets: MutableSequence[targeting_preset_messages.TargetingPreset] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=targeting_preset_messages.TargetingPreset,
        )
    )


class DeactivateTargetingPresetRequest(proto.Message):
    r"""Request object for ``DeactivateTargetingPreset`` method.

    Attributes:
        name (str):
            Required. Resource name for the TargetingPreset. Format:
            ``networks/{network_code}/targetingPreset/{targeting_preset_id}``
        targeting_preset_id (int):
            Required. TargetingPreset ID to deactivate.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    targeting_preset_id: int = proto.Field(
        proto.INT64,
        number=2,
    )


class BatchDeactivateTargetingPresetsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateTargetingPresets`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        requests (MutableSequence[google.ads.admanager_v1.types.DeactivateTargetingPresetRequest]):
            Required. The ``TargetingPreset`` objects to deactivate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["DeactivateTargetingPresetRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="DeactivateTargetingPresetRequest",
    )


class BatchDeactivateTargetingPresetsResponse(proto.Message):
    r"""Response message for ``DeactivateTargetingPresets`` method.

    Attributes:
        change_count (int):
            The number of objects that were deactivated
            as a result of performing the action.
    """

    change_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
