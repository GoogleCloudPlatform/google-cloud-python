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

from google.cloud.support_v2.types import case as gcs_case
from google.cloud.support_v2.types import escalation as gcs_escalation

__protobuf__ = proto.module(
    package="google.cloud.support.v2",
    manifest={
        "GetCaseRequest",
        "CreateCaseRequest",
        "ListCasesRequest",
        "ListCasesResponse",
        "SearchCasesRequest",
        "SearchCasesResponse",
        "EscalateCaseRequest",
        "UpdateCaseRequest",
        "CloseCaseRequest",
        "SearchCaseClassificationsRequest",
        "SearchCaseClassificationsResponse",
    },
)


class GetCaseRequest(proto.Message):
    r"""The request message for the GetCase endpoint.

    Attributes:
        name (str):
            Required. The full name of a case to be
            retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCaseRequest(proto.Message):
    r"""The request message for the CreateCase endpoint.

    Attributes:
        parent (str):
            Required. The name of the parent under which
            the case should be created.
        case (google.cloud.support_v2.types.Case):
            Required. The case to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    case: gcs_case.Case = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_case.Case,
    )


class ListCasesRequest(proto.Message):
    r"""The request message for the ListCases endpoint.

    Attributes:
        parent (str):
            Required. The name of a parent to list cases
            under.
        filter (str):
            An expression used to filter cases.

            If it's an empty string, then no filtering happens.
            Otherwise, the endpoint returns the cases that match the
            filter.

            Expressions use the following fields separated by ``AND``
            and specified with ``=``:

            - ``state``: Can be ``OPEN`` or ``CLOSED``.
            - ``priority``: Can be ``P0``, ``P1``, ``P2``, ``P3``, or
              ``P4``. You can specify multiple values for priority using
              the ``OR`` operator. For example,
              ``priority=P1 OR priority=P2``.
            - ``creator.email``: The email address of the case creator.

            EXAMPLES:

            - ``state=CLOSED``
            - ``state=OPEN AND creator.email="tester@example.com"``
            - ``state=OPEN AND (priority=P0 OR priority=P1)``
        page_size (int):
            The maximum number of cases fetched with each
            request. Defaults to 10.
        page_token (str):
            A token identifying the page of results to
            return. If unspecified, the first page is
            retrieved.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCasesResponse(proto.Message):
    r"""The response message for the ListCases endpoint.

    Attributes:
        cases (MutableSequence[google.cloud.support_v2.types.Case]):
            The list of cases associated with the parent
            after any filters have been applied.
        next_page_token (str):
            A token to retrieve the next page of results. Set this in
            the ``page_token`` field of subsequent ``cases.list``
            requests. If unspecified, there are no more results to
            retrieve.
    """

    @property
    def raw_page(self):
        return self

    cases: MutableSequence[gcs_case.Case] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_case.Case,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchCasesRequest(proto.Message):
    r"""The request message for the SearchCases endpoint.

    Attributes:
        parent (str):
            The name of the parent resource to search for
            cases under.
        query (str):
            An expression used to filter cases.

            Expressions use the following fields separated by ``AND``
            and specified with ``=``:

            - ``state``: Can be ``OPEN`` or ``CLOSED``.
            - ``priority``: Can be ``P0``, ``P1``, ``P2``, ``P3``, or
              ``P4``. You can specify multiple values for priority using
              the ``OR`` operator. For example,
              ``priority=P1 OR priority=P2``.
            - ``creator.email``: The email address of the case creator.

            To search across ``displayName``, ``description``, and
            comments, use a global restriction with no keyword or
            operator. For example, ``"my search"``.

            To search only cases updated after a certain date, use
            ``update_time`` restricted with that particular date, time,
            and timezone in ISO datetime format. For example,
            ``update_time>"2020-01-01T00:00:00-05:00"``. ``update_time``
            only supports the greater than operator (``>``).

            If you are using the ``v2`` version of the API, you must
            specify the case parent in the ``parent`` field. If you
            provide an empty ``query``, all cases under the parent
            resource will be returned.

            If you are using the ``v2beta`` version of the API, you must
            specify the case parent in the ``query`` field using one of
            the two fields below, which are only available for
            ``v2beta``. The ``parent`` field will be ignored.

            - ``organization``: An organization name in the form
              ``organizations/<organization_id>``.
            - ``project``: A project name in the form
              ``projects/<project_id>``.

            Examples:

            For ``v2``:

            - ``state=CLOSED``
            - ``state=OPEN AND creator.email="tester@example.com"``
            - ``state=OPEN AND (priority=P0 OR priority=P1)``
            - ``update_time>"2020-01-01T00:00:00-05:00"``

            For ``v2beta``:

            - ``organization="organizations/123456789"``
            - ``project="projects/my-project-id"``
            - ``project="projects/123456789"``
            - ``organization="organizations/123456789" AND state=CLOSED``
            - ``project="projects/my-project-id" AND creator.email="tester@example.com"``
            - ``project="projects/my-project-id" AND (priority=P0 OR priority=P1)``
        page_size (int):
            The maximum number of cases fetched with each
            request. The default page size is 10.
        page_token (str):
            A token identifying the page of results to
            return. If unspecified, the first page is
            retrieved.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    query: str = proto.Field(
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


class SearchCasesResponse(proto.Message):
    r"""The response message for the SearchCases endpoint.

    Attributes:
        cases (MutableSequence[google.cloud.support_v2.types.Case]):
            The list of cases associated with the parent
            after any filters have been applied.
        next_page_token (str):
            A token to retrieve the next page of results. Set this in
            the ``page_token`` field of subsequent ``cases.search``
            requests. If unspecified, there are no more results to
            retrieve.
    """

    @property
    def raw_page(self):
        return self

    cases: MutableSequence[gcs_case.Case] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_case.Case,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EscalateCaseRequest(proto.Message):
    r"""The request message for the EscalateCase endpoint.

    Attributes:
        name (str):
            Required. The name of the case to be
            escalated.
        escalation (google.cloud.support_v2.types.Escalation):
            The escalation information to be sent with
            the escalation request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    escalation: gcs_escalation.Escalation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_escalation.Escalation,
    )


class UpdateCaseRequest(proto.Message):
    r"""The request message for the UpdateCase endpoint

    Attributes:
        case (google.cloud.support_v2.types.Case):
            Required. The case to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            A list of attributes of the case that should be updated.
            Supported values are ``priority``, ``display_name``, and
            ``subscriber_email_addresses``. If no fields are specified,
            all supported fields are updated.

            Be careful - if you do not provide a field mask, then you
            might accidentally clear some fields. For example, if you
            leave the field mask empty and do not provide a value for
            ``subscriber_email_addresses``, then
            ``subscriber_email_addresses`` is updated to empty.
    """

    case: gcs_case.Case = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_case.Case,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CloseCaseRequest(proto.Message):
    r"""The request message for the CloseCase endpoint.

    Attributes:
        name (str):
            Required. The name of the case to close.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchCaseClassificationsRequest(proto.Message):
    r"""The request message for the SearchCaseClassifications
    endpoint.

    Attributes:
        query (str):
            An expression used to filter case
            classifications.
            If it's an empty string, then no filtering
            happens. Otherwise, case classifications will be
            returned that match the filter.
        page_size (int):
            The maximum number of classifications fetched
            with each request.
        page_token (str):
            A token identifying the page of results to
            return. If unspecified, the first page is
            retrieved.
    """

    query: str = proto.Field(
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


class SearchCaseClassificationsResponse(proto.Message):
    r"""The response message for SearchCaseClassifications endpoint.

    Attributes:
        case_classifications (MutableSequence[google.cloud.support_v2.types.CaseClassification]):
            The classifications retrieved.
        next_page_token (str):
            A token to retrieve the next page of results. Set this in
            the ``page_token`` field of subsequent
            ``caseClassifications.list`` requests. If unspecified, there
            are no more results to retrieve.
    """

    @property
    def raw_page(self):
        return self

    case_classifications: MutableSequence[gcs_case.CaseClassification] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcs_case.CaseClassification,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
