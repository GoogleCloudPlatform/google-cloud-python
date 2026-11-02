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

from google.ads.admanager_v1.types import audience_segment_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetAudienceSegmentRequest",
        "ListAudienceSegmentsRequest",
        "ListAudienceSegmentsResponse",
        "CreateAudienceSegmentRequest",
        "BatchCreateAudienceSegmentsRequest",
        "BatchCreateAudienceSegmentsResponse",
        "UpdateAudienceSegmentRequest",
        "BatchUpdateAudienceSegmentsRequest",
        "BatchUpdateAudienceSegmentsResponse",
        "BatchActivateAudienceSegmentsRequest",
        "BatchActivateAudienceSegmentsResponse",
        "BatchDeactivateAudienceSegmentsRequest",
        "BatchDeactivateAudienceSegmentsResponse",
        "BatchApproveAudienceSegmentsRequest",
        "BatchApproveAudienceSegmentsResponse",
        "BatchRejectAudienceSegmentsRequest",
        "BatchRejectAudienceSegmentsResponse",
        "BatchPopulateAudienceSegmentsRequest",
        "BatchPopulateAudienceSegmentsResponse",
    },
)


class GetAudienceSegmentRequest(proto.Message):
    r"""Request object for ``GetAudienceSegment`` method.

    Attributes:
        name (str):
            Required. The resource name of the AudienceSegment. Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAudienceSegmentsRequest(proto.Message):
    r"""Request object for ``ListAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. The parent publisher network associated with these
            audience segments. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``AudienceSegments`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``AudienceSegments`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAudienceSegments`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAudienceSegments`` must match the call that provided
            the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``adIdSize``
            - ``categoryIds``
            - ``dataProviderDisplayName``
            - ``displayName``
            - ``idfaSize``
            - ``mobileWebSize``
            - ``ppidSize``
            - ``segmentType``
            - ``sharedId``
            - ``size``
            - ``status``
            - ``thirdPartyAudienceSegment.approvalStatus``
            - ``thirdPartyAudienceSegment.cost``
            - ``thirdPartyAudienceSegment.endTime``
            - ``thirdPartyAudienceSegment.startTime``
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


class ListAudienceSegmentsResponse(proto.Message):
    r"""Response object for ``ListAudienceSegmentsRequest`` containing
    matching ``AudienceSegment`` objects.

    Attributes:
        audience_segments (MutableSequence[google.ads.admanager_v1.types.AudienceSegment]):
            The ``AudienceSegment`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``AudienceSegment`` objects. If a filter was
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

    audience_segments: MutableSequence[audience_segment_messages.AudienceSegment] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=audience_segment_messages.AudienceSegment,
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


class CreateAudienceSegmentRequest(proto.Message):
    r"""Request object for ``CreateAudienceSegment`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``AudienceSegment``
            will be created. Format: ``networks/{network_code}``
        audience_segment (google.ads.admanager_v1.types.AudienceSegment):
            Required. The ``AudienceSegment`` to create. Only
            first-party segments can be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audience_segment: audience_segment_messages.AudienceSegment = proto.Field(
        proto.MESSAGE,
        number=2,
        message=audience_segment_messages.AudienceSegment,
    )


class BatchCreateAudienceSegmentsRequest(proto.Message):
    r"""Request object for ``BatchCreateAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``AudienceSegments``
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreateAudienceSegmentRequest must match
            this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateAudienceSegmentRequest]):
            Required. The ``AudienceSegment`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateAudienceSegmentRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateAudienceSegmentRequest",
    )


class BatchCreateAudienceSegmentsResponse(proto.Message):
    r"""Response object for ``BatchCreateAudienceSegments`` method.

    Attributes:
        audience_segments (MutableSequence[google.ads.admanager_v1.types.AudienceSegment]):
            The ``AudienceSegment`` objects created.
    """

    audience_segments: MutableSequence[audience_segment_messages.AudienceSegment] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=audience_segment_messages.AudienceSegment,
        )
    )


class UpdateAudienceSegmentRequest(proto.Message):
    r"""Request object for ``UpdateAudienceSegment`` method.

    Attributes:
        audience_segment (google.ads.admanager_v1.types.AudienceSegment):
            Required. The ``AudienceSegment`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    audience_segment: audience_segment_messages.AudienceSegment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=audience_segment_messages.AudienceSegment,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateAudienceSegmentsRequest(proto.Message):
    r"""Request object for ``BatchUpdateAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``AudienceSegments``
            will be updated. Format: ``networks/{network_code}`` The
            parent field in the
            UpdateAudienceSegmentRequest.audienceSegment must match this
            field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateAudienceSegmentRequest]):
            Required. The ``AudienceSegment`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateAudienceSegmentRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateAudienceSegmentRequest",
    )


class BatchUpdateAudienceSegmentsResponse(proto.Message):
    r"""Response object for ``BatchUpdateAudienceSegments`` method.

    Attributes:
        audience_segments (MutableSequence[google.ads.admanager_v1.types.AudienceSegment]):
            The ``AudienceSegment`` objects updated.
    """

    audience_segments: MutableSequence[audience_segment_messages.AudienceSegment] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=audience_segment_messages.AudienceSegment,
        )
    )


class BatchActivateAudienceSegmentsRequest(proto.Message):
    r"""Request message for ``BatchActivateAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AudienceSegments. Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateAudienceSegmentsResponse(proto.Message):
    r"""Response message for ``BatchActivateAudienceSegments`` method.

    Attributes:
        change_count (int):
            Number of audience segments activated.
    """

    change_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class BatchDeactivateAudienceSegmentsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AudienceSegments. Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateAudienceSegmentsResponse(proto.Message):
    r"""Response message for ``BatchDeactivateAudienceSegments`` method.

    Attributes:
        change_count (int):
            Number of audience segments deactivated.
    """

    change_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class BatchApproveAudienceSegmentsRequest(proto.Message):
    r"""Request message for ``BatchApproveAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AudienceSegments. Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchApproveAudienceSegmentsResponse(proto.Message):
    r"""Response message for ``BatchApproveAudienceSegments`` method.

    Attributes:
        change_count (int):
            Number of audience segments approved.
    """

    change_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class BatchRejectAudienceSegmentsRequest(proto.Message):
    r"""Request message for ``BatchRejectAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AudienceSegments. Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchRejectAudienceSegmentsResponse(proto.Message):
    r"""Response message for ``BatchRejectAudienceSegments`` method.

    Attributes:
        change_count (int):
            Number of audience segments rejected.
    """

    change_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class BatchPopulateAudienceSegmentsRequest(proto.Message):
    r"""Request message for ``BatchPopulateAudienceSegments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AudienceSegments. Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchPopulateAudienceSegmentsResponse(proto.Message):
    r"""Response message for ``BatchPopulateAudienceSegments`` method.

    Attributes:
        change_count (int):
            Number of audience segments populated.
    """

    change_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
