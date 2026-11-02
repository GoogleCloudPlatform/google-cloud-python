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
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "AccountIssue",
        "ListAccountIssuesRequest",
        "ListAccountIssuesResponse",
    },
)


class AccountIssue(proto.Message):
    r"""An
    ```AccountIssue`` <https://support.google.com/merchants/answer/12153802?sjid=17798438912526418908-EU#account>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the account issue. Format:
            ``accounts/{account}/issues/{id}``
        title (str):
            The localized title of the issue.
        severity (google.shopping.merchant_accounts_v1beta.types.AccountIssue.Severity):
            The overall severity of the issue.
        impacted_destinations (MutableSequence[google.shopping.merchant_accounts_v1beta.types.AccountIssue.ImpactedDestination]):
            The impact this issue has on various
            destinations.
        detail (str):
            Further localized details about the issue.
        documentation_uri (str):
            Link to Merchant Center Help Center providing
            further information about the issue and how to
            fix it.
    """

    class Severity(proto.Enum):
        r"""All possible issue severities.

        Values:
            SEVERITY_UNSPECIFIED (0):
                The severity is unknown.
            CRITICAL (1):
                The issue causes offers to not serve.
            ERROR (2):
                The issue might affect offers (in the future)
                or might be an indicator of issues with offers.
            SUGGESTION (3):
                The issue is a suggestion for improvement.
        """

        SEVERITY_UNSPECIFIED = 0
        CRITICAL = 1
        ERROR = 2
        SUGGESTION = 3

    class ImpactedDestination(proto.Message):
        r"""The impact of the issue on a destination.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                The impacted reporting context.

                This field is a member of `oneof`_ ``_reporting_context``.
            impacts (MutableSequence[google.shopping.merchant_accounts_v1beta.types.AccountIssue.ImpactedDestination.Impact]):
                The (negative) impact for various regions on
                the given destination.
        """

        class Impact(proto.Message):
            r"""The impact of the issue on a region.

            Attributes:
                region_code (str):
                    The `CLDR region code <https://cldr.unicode.org/>`__ where
                    this issue applies.
                severity (google.shopping.merchant_accounts_v1beta.types.AccountIssue.Severity):
                    The severity of the issue on the destination
                    and region.
            """

            region_code: str = proto.Field(
                proto.STRING,
                number=1,
            )
            severity: "AccountIssue.Severity" = proto.Field(
                proto.ENUM,
                number=2,
                enum="AccountIssue.Severity",
            )

        reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=types.ReportingContext.ReportingContextEnum,
        )
        impacts: MutableSequence["AccountIssue.ImpactedDestination.Impact"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="AccountIssue.ImpactedDestination.Impact",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=3,
        enum=Severity,
    )
    impacted_destinations: MutableSequence[ImpactedDestination] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ImpactedDestination,
    )
    detail: str = proto.Field(
        proto.STRING,
        number=5,
    )
    documentation_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListAccountIssuesRequest(proto.Message):
    r"""Request message for the ``ListAccountIssues`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of issues.
            Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of issues to
            return. The service may return fewer than this
            value. If unspecified, at most 50 users will be
            returned. The maximum value is 100; values above
            100 will be coerced to 100
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccountIssues`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAccountIssues`` must match the call that provided the
            page token.
        language_code (str):
            Optional. The issues in the response will have
            human-readable fields in the given language. The format is
            `BCP-47 <https://tools.ietf.org/html/bcp47>`__, such as
            ``en-US`` or ``sr-Latn``. If not value is provided,
            ``en-US`` will be used.
        time_zone (str):
            Optional. The `IANA <https://www.iana.org/time-zones>`__
            timezone used to localize times in human-readable fields.
            For example 'America/Los_Angeles'. If not set,
            'America/Los_Angeles' will be used.
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
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListAccountIssuesResponse(proto.Message):
    r"""Response message for the ``ListAccountIssues`` method.

    Attributes:
        account_issues (MutableSequence[google.shopping.merchant_accounts_v1beta.types.AccountIssue]):
            The issues from the specified account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    account_issues: MutableSequence["AccountIssue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountIssue",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
