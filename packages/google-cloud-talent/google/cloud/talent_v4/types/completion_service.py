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

from google.cloud.talent_v4.types import common

__protobuf__ = proto.module(
    package="google.cloud.talent.v4",
    manifest={
        "CompleteQueryRequest",
        "CompleteQueryResponse",
    },
)


class CompleteQueryRequest(proto.Message):
    r"""Auto-complete parameters.

    Attributes:
        tenant (str):
            Required. Resource name of tenant the completion is
            performed within.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenants/bar".
        query (str):
            Required. The query used to generate
            suggestions.
            The maximum number of allowed characters is 255.
        language_codes (MutableSequence[str]):
            The list of languages of the query. This is the BCP-47
            language code, such as "en-US" or "sr-Latn". For more
            information, see `Tags for Identifying
            Languages <https://tools.ietf.org/html/bcp47>`__.

            The maximum number of allowed characters is 255.
        page_size (int):
            Required. Completion result count.

            The maximum allowed page size is 10.
        company (str):
            If provided, restricts completion to specified company.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}",
            for example, "projects/foo/tenants/bar/companies/baz".
        scope (google.cloud.talent_v4.types.CompleteQueryRequest.CompletionScope):
            The scope of the completion. The defaults is
            [CompletionScope.PUBLIC][google.cloud.talent.v4.CompleteQueryRequest.CompletionScope.PUBLIC].
        type_ (google.cloud.talent_v4.types.CompleteQueryRequest.CompletionType):
            The completion topic. The default is
            [CompletionType.COMBINED][google.cloud.talent.v4.CompleteQueryRequest.CompletionType.COMBINED].
    """

    class CompletionScope(proto.Enum):
        r"""Enum to specify the scope of completion.

        Values:
            COMPLETION_SCOPE_UNSPECIFIED (0):
                Default value.
            TENANT (1):
                Suggestions are based only on the data
                provided by the client.
            PUBLIC (2):
                Suggestions are based on all jobs data in the
                system that's visible to the client
        """

        COMPLETION_SCOPE_UNSPECIFIED = 0
        TENANT = 1
        PUBLIC = 2

    class CompletionType(proto.Enum):
        r"""Enum to specify auto-completion topics.

        Values:
            COMPLETION_TYPE_UNSPECIFIED (0):
                Default value.
            JOB_TITLE (1):
                Suggest job titles for jobs autocomplete.

                For
                [CompletionType.JOB_TITLE][google.cloud.talent.v4.CompleteQueryRequest.CompletionType.JOB_TITLE]
                type, only open jobs with the same
                [language_codes][google.cloud.talent.v4.CompleteQueryRequest.language_codes]
                are returned.
            COMPANY_NAME (2):
                Suggest company names for jobs autocomplete.

                For
                [CompletionType.COMPANY_NAME][google.cloud.talent.v4.CompleteQueryRequest.CompletionType.COMPANY_NAME]
                type, only companies having open jobs with the same
                [language_codes][google.cloud.talent.v4.CompleteQueryRequest.language_codes]
                are returned.
            COMBINED (3):
                Suggest both job titles and company names for jobs
                autocomplete.

                For
                [CompletionType.COMBINED][google.cloud.talent.v4.CompleteQueryRequest.CompletionType.COMBINED]
                type, only open jobs with the same
                [language_codes][google.cloud.talent.v4.CompleteQueryRequest.language_codes]
                or companies having open jobs with the same
                [language_codes][google.cloud.talent.v4.CompleteQueryRequest.language_codes]
                are returned.
        """

        COMPLETION_TYPE_UNSPECIFIED = 0
        JOB_TITLE = 1
        COMPANY_NAME = 2
        COMBINED = 3

    tenant: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    company: str = proto.Field(
        proto.STRING,
        number=5,
    )
    scope: CompletionScope = proto.Field(
        proto.ENUM,
        number=6,
        enum=CompletionScope,
    )
    type_: CompletionType = proto.Field(
        proto.ENUM,
        number=7,
        enum=CompletionType,
    )


class CompleteQueryResponse(proto.Message):
    r"""Response of auto-complete query.

    Attributes:
        completion_results (MutableSequence[google.cloud.talent_v4.types.CompleteQueryResponse.CompletionResult]):
            Results of the matching job/company
            candidates.
        metadata (google.cloud.talent_v4.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    class CompletionResult(proto.Message):
        r"""Resource that represents completion results.

        Attributes:
            suggestion (str):
                The suggestion for the query.
            type_ (google.cloud.talent_v4.types.CompleteQueryRequest.CompletionType):
                The completion topic.
            image_uri (str):
                The URI of the company image for
                [COMPANY_NAME][google.cloud.talent.v4.CompleteQueryRequest.CompletionType.COMPANY_NAME].
        """

        suggestion: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "CompleteQueryRequest.CompletionType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="CompleteQueryRequest.CompletionType",
        )
        image_uri: str = proto.Field(
            proto.STRING,
            number=3,
        )

    completion_results: MutableSequence[CompletionResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CompletionResult,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.ResponseMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
