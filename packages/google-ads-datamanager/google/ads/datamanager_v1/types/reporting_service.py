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

from google.ads.datamanager_v1.types import partner_match_report_entry

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "RetrievePartnerMatchReportRequest",
        "RetrievePartnerMatchReportResponse",
    },
)


class RetrievePartnerMatchReportRequest(proto.Message):
    r"""Request message for DM API
    ReportingService.RetrievePartnerMatchReport

    Attributes:
        parent (str):
            Required. The parent account that owns the user list.
            Format: ``accountTypes/{account_type}/accounts/{account}``
        currency_code (str):
            Optional. The currency to return the
            costs/fees in. If unspecified, defaults to the
            Data Partner's currency
        filter (str):
            Optional. A `filter string <https://google.aip.dev/160>`__
            to apply to the list request. All fields need to be on the
            left hand side of each condition (for example:
            ``user_list_id = 123``). Fields must be specified using
            either all `camel
            case <https://en.wikipedia.org/wiki/Camel_case>`__ or all
            `snake case <https://en.wikipedia.org/wiki/Snake_case>`__.
            Don't use a combination of camel case and snake case.

            **Supported Operations:**

            - ``AND``
            - ``=``
            - ``!=``
            - ``>``
            - ``>=``
            - ``<``
            - ``<=``

            **Supported Functions:**

            - ``IN(field, value1, value2, ...)``: returns true if the
              field matches any of the values. Example:
              ``IN(user_list_id, 123, 456)``

            **Supported Fields:**

            - ``advertiser_account.account_type``
            - ``advertiser_account.account_id``
            - ``campaign.campaign_id``
            - ``ad_group.ad_group_id``
            - ``user_list.user_list_id``
        start_date (int):
            Required. The start date (inclusive) of the
            report data to retrieve.  Only data from the
            last 2 years can be retrieved.  If the start
            date is set to an older date, only data from the
            last 2 years will be returned. Should be in the
            format YYYYMMDD.
        end_date (int):
            Optional. The end date (inclusive) of the
            report data to retrieve. Defaults to the current
            date if not populated.  Should be in the format
            YYYYMMDD.
        page_size (int):
            Optional. The maximum number of partner match
            report entries to return per page. The service
            may return fewer than this value. If
            unspecified, at most 50 reports will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``RetrievePartnerMatchReport`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``RetrievePartnerMatchReport`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_date: int = proto.Field(
        proto.INT64,
        number=8,
    )
    end_date: int = proto.Field(
        proto.INT64,
        number=9,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )


class RetrievePartnerMatchReportResponse(proto.Message):
    r"""Response message for DM API
    ReportingService.RetrievePartnerMatchReport

    Attributes:
        partner_match_report_entries (MutableSequence[google.ads.datamanager_v1.types.PartnerMatchReportEntry]):
            A list of the rows/entries in the partner
            match report.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    partner_match_report_entries: MutableSequence[
        partner_match_report_entry.PartnerMatchReportEntry
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=partner_match_report_entry.PartnerMatchReportEntry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
