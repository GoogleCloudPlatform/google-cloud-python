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

from google.ads.admanager_v1.types import proposal_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetProposalRequest",
        "ListProposalsRequest",
        "ListProposalsResponse",
        "CreateProposalRequest",
        "BatchCreateProposalsRequest",
        "BatchCreateProposalsResponse",
        "UpdateProposalRequest",
        "BatchUpdateProposalsRequest",
        "BatchUpdateProposalsResponse",
        "BatchArchiveProposalsRequest",
        "BatchArchiveProposalsResponse",
        "BatchUnarchiveProposalsRequest",
        "BatchUnarchiveProposalsResponse",
        "BatchPauseProposalsRequest",
        "BatchPauseProposalsResponse",
        "BatchResumeProposalsRequest",
        "BatchResumeProposalsResponse",
        "BatchRequestBuyerReviewProposalsRequest",
        "BatchRequestBuyerReviewProposalsResponse",
        "BatchRequestBuyerAcceptProposalsRequest",
        "BatchRequestBuyerAcceptProposalsResponse",
        "BatchReserveProposalsRequest",
        "BatchReserveProposalsResponse",
        "BatchRedraftProposalsRequest",
        "BatchRedraftProposalsResponse",
        "BatchDiscardDraftProposalsRequest",
        "BatchDiscardDraftProposalsResponse",
        "BatchTerminateProposalsRequest",
        "BatchTerminateProposalsResponse",
        "BatchPushToOrderProposalsRequest",
        "BatchPushToOrderProposalsResponse",
        "FetchMarketplaceCommentsRequest",
        "FetchMarketplaceCommentsResponse",
    },
)


class GetProposalRequest(proto.Message):
    r"""Request object for ``GetProposal`` method.

    Attributes:
        name (str):
            Required. The resource name of the Proposal. Format:
            ``networks/{network_code}/proposals/{proposal_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProposalsRequest(proto.Message):
    r"""Request object for ``ListProposals`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Proposals. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Proposals`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Proposals`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListProposals`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListProposals`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            Syntax summary: double-quoted ``"..."`` (never ``'...'``)
            strings and RFC 3339 timestamps, full resource names on
            reference fields (for example,
            ``order = "networks/123/orders/456"``, not ``*Id`` or bare
            IDs), prefix or suffix ``*`` wildcards with ``=``
            (``displayName = "foo*"``), ``:`` for substring or
            repeated-field matching, unquoted enums and booleans,
            uppercase ``AND``/``OR``/``NOT``, and standalone
            ``IN(field, SET(v1, v2))`` (not ``field IN (...)``).

            **Filterable fields:**

            - ``advertiser``
            - ``agencies.company``
            - ``appliedTeams``
            - ``archived``
            - ``currencyCode``
            - ``displayName``
            - ``endTime``
            - ``marketplaceInfo.negotiationStatus``
            - ``name``
            - ``order``
            - ``primarySalesperson``
            - ``salesPlannerUsers``
            - ``sellerContactUsers``
            - ``sold``
            - ``startTime``
            - ``supplyPath``
            - ``trafficker``
            - ``updateTime``
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


class ListProposalsResponse(proto.Message):
    r"""Response object for ``ListProposalsRequest`` containing matching
    ``Proposal`` objects.

    Attributes:
        proposals (MutableSequence[google.ads.admanager_v1.types.Proposal]):
            The ``Proposal`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Proposal`` objects. If a filter was
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

    proposals: MutableSequence[proposal_messages.Proposal] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=proposal_messages.Proposal,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateProposalRequest(proto.Message):
    r"""Request object for ``CreateProposal`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Proposal`` will
            be created. Format: ``networks/{network_code}``
        proposal (google.ads.admanager_v1.types.Proposal):
            Required. The ``Proposal`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    proposal: proposal_messages.Proposal = proto.Field(
        proto.MESSAGE,
        number=2,
        message=proposal_messages.Proposal,
    )


class BatchCreateProposalsRequest(proto.Message):
    r"""Request object for ``BatchCreateProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Proposals`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateProposalRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateProposalRequest]):
            Required. The ``Proposal`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateProposalRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateProposalRequest",
    )


class BatchCreateProposalsResponse(proto.Message):
    r"""Response object for ``BatchCreateProposals`` method.

    Attributes:
        proposals (MutableSequence[google.ads.admanager_v1.types.Proposal]):
            The ``Proposal`` objects created.
    """

    proposals: MutableSequence[proposal_messages.Proposal] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=proposal_messages.Proposal,
    )


class UpdateProposalRequest(proto.Message):
    r"""Request object for ``UpdateProposal`` method.

    Attributes:
        proposal (google.ads.admanager_v1.types.Proposal):
            Required. The ``Proposal`` to update.

            The ``Proposal``'s ``name`` is used to identify the
            ``Proposal`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    proposal: proposal_messages.Proposal = proto.Field(
        proto.MESSAGE,
        number=1,
        message=proposal_messages.Proposal,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateProposalsRequest(proto.Message):
    r"""Request object for ``BatchUpdateProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Proposals`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateProposalRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateProposalRequest]):
            Required. The ``Proposal`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateProposalRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateProposalRequest",
    )


class BatchUpdateProposalsResponse(proto.Message):
    r"""Response object for ``BatchUpdateProposals`` method.

    Attributes:
        proposals (MutableSequence[google.ads.admanager_v1.types.Proposal]):
            The ``Proposal`` objects updated.
    """

    proposals: MutableSequence[proposal_messages.Proposal] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=proposal_messages.Proposal,
    )


class BatchArchiveProposalsRequest(proto.Message):
    r"""Request message for ``BatchArchiveProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            archived. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to archive.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveProposalsResponse(proto.Message):
    r"""Response message for ``BatchArchiveProposals`` method."""


class BatchUnarchiveProposalsRequest(proto.Message):
    r"""Request message for ``BatchUnarchiveProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            unarchived. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to unarchive.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchUnarchiveProposalsResponse(proto.Message):
    r"""Response message for ``BatchUnarchiveProposals`` method."""


class BatchPauseProposalsRequest(proto.Message):
    r"""Request message for ``BatchPauseProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            paused. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to pause.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
        reason (str):
            Required. The reason for pausing the
            Proposals.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchPauseProposalsResponse(proto.Message):
    r"""Response message for ``BatchPauseProposals`` method."""


class BatchResumeProposalsRequest(proto.Message):
    r"""Request message for ``BatchResumeProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            resumed. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to resume.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchResumeProposalsResponse(proto.Message):
    r"""Response message for ``BatchResumeProposals`` method."""


class BatchRequestBuyerReviewProposalsRequest(proto.Message):
    r"""Request message for ``BatchRequestBuyerReviewProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            reviewed. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to request
            buyer review. Format:
            ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchRequestBuyerReviewProposalsResponse(proto.Message):
    r"""Response message for ``BatchRequestBuyerReviewProposals`` method."""


class BatchRequestBuyerAcceptProposalsRequest(proto.Message):
    r"""Request message for ``BatchRequestBuyerAcceptProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            accepted. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to request
            buyer accept. Format:
            ``networks/{network_code}/proposals/{proposal_id}``
        overbooking_allowed (bool):
            Optional. Whether to allow overbooking when
            requesting buyer acceptance.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    overbooking_allowed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchRequestBuyerAcceptProposalsResponse(proto.Message):
    r"""Response message for ``BatchRequestBuyerAcceptProposals`` method."""


class BatchReserveProposalsRequest(proto.Message):
    r"""Request message for ``BatchReserveProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            reserved. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to reserve.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
        overbooking_allowed (bool):
            Optional. Whether to allow overbooking when
            reserving inventory.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    overbooking_allowed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchReserveProposalsResponse(proto.Message):
    r"""Response message for ``BatchReserveProposals`` method."""


class BatchRedraftProposalsRequest(proto.Message):
    r"""Request message for ``BatchRedraftProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            redrafted. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to redraft.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchRedraftProposalsResponse(proto.Message):
    r"""Response message for ``BatchRedraftProposals`` method."""


class BatchDiscardDraftProposalsRequest(proto.Message):
    r"""Request message for ``BatchDiscardDraftProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            discarded. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to discard.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDiscardDraftProposalsResponse(proto.Message):
    r"""Response message for ``BatchDiscardDraftProposals`` method."""


class BatchTerminateProposalsRequest(proto.Message):
    r"""Request message for ``BatchTerminateProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be
            terminated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to terminate.
            Format: ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchTerminateProposalsResponse(proto.Message):
    r"""Response message for ``BatchTerminateProposals`` method."""


class BatchPushToOrderProposalsRequest(proto.Message):
    r"""Request message for ``BatchPushToOrderProposals`` method.

    Attributes:
        parent (str):
            Required. The parent resource where proposals will be pushed
            to order. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals to push to
            order. Format:
            ``networks/{network_code}/proposals/{proposal_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchPushToOrderProposalsResponse(proto.Message):
    r"""Response message for ``BatchPushToOrderProposals`` method."""


class FetchMarketplaceCommentsRequest(proto.Message):
    r"""Request message for ``FetchMarketplaceComments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where MarketplaceComments will
            be fetched from. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the Proposals for which to
            fetch marketplace comments. A maximum of 50 proposal names
            can be specified. Format:
            ``networks/{network_code}/proposals/{proposal_id}``
        page_size (int):
            Optional. The maximum number of ``MarketplaceComment``
            objects to return. The service may return fewer than this
            value. If unspecified, at most 50 ``MarketplaceComments``
            will be returned. The maximum value is 1000; values greater
            than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``FetchMarketplaceComments`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``FetchMarketplaceComments`` must match the call that
            provided the page token.
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    skip: int = proto.Field(
        proto.INT32,
        number=5,
    )


class FetchMarketplaceCommentsResponse(proto.Message):
    r"""Response message for ``FetchMarketplaceComments`` method.

    Attributes:
        marketplace_comments (MutableSequence[google.ads.admanager_v1.types.MarketplaceComment]):
            The ``MarketplaceComment`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    marketplace_comments: MutableSequence[proposal_messages.MarketplaceComment] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=proposal_messages.MarketplaceComment,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
