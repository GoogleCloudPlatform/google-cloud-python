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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.datasources.v1beta",
    manifest={
        "FileUpload",
        "GetFileUploadRequest",
    },
)


class FileUpload(proto.Message):
    r"""The file upload of a specific data source, that is, the
    result of the retrieval of the data source at a certain
    timestamp computed asynchronously when the data source
    processing is finished. Only applicable to file data sources.

    Attributes:
        name (str):
            Identifier. The name of the data source file upload. Format:
            ``{datasource.name=accounts/{account}/dataSources/{datasource}/fileUploads/{fileupload}}``
        data_source_id (int):
            Output only. The data source id.
        processing_state (google.shopping.merchant_datasources_v1beta.types.FileUpload.ProcessingState):
            Output only. The processing state of the data
            source.
        issues (MutableSequence[google.shopping.merchant_datasources_v1beta.types.FileUpload.Issue]):
            Output only. The list of issues occurring in
            the data source.
        items_total (int):
            Output only. The number of items in the data
            source that were processed.
        items_created (int):
            Output only. The number of items in the data
            source that were created.
        items_updated (int):
            Output only. The number of items in the data
            source that were updated.
        upload_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date at which the file of
            the data source was uploaded.
    """

    class ProcessingState(proto.Enum):
        r"""The processing state of the data source.

        Values:
            PROCESSING_STATE_UNSPECIFIED (0):
                Processing state unspecified.
            FAILED (1):
                The data source could not be processed or all
                the items had errors.
            IN_PROGRESS (2):
                The data source is being processed.
            SUCCEEDED (3):
                The data source was processed successfully,
                though some items might have had errors.
        """

        PROCESSING_STATE_UNSPECIFIED = 0
        FAILED = 1
        IN_PROGRESS = 2
        SUCCEEDED = 3

    class Issue(proto.Message):
        r"""An error occurring in the data source, like "invalid price".

        Attributes:
            title (str):
                Output only. The title of the issue, for
                example, "Item too big".
            description (str):
                Output only. The error description, for
                example, "Your data source contains items which
                have too many attributes, or are too big. These
                items will be dropped".
            code (str):
                Output only. The code of the error, for example,
                "validation/invalid_value". Returns "?" if the code is
                unknown.
            count (int):
                Output only. The number of occurrences of the
                error in the file upload.
            severity (google.shopping.merchant_datasources_v1beta.types.FileUpload.Issue.Severity):
                Output only. The severity of the issue.
            documentation_uri (str):
                Output only. Link to the documentation
                explaining the issue in more details, if
                available.
        """

        class Severity(proto.Enum):
            r"""The severity of the issue.

            Values:
                SEVERITY_UNSPECIFIED (0):
                    Severity unspecified.
                WARNING (1):
                    The issue is the warning.
                ERROR (2):
                    The issue is an error.
            """

            SEVERITY_UNSPECIFIED = 0
            WARNING = 1
            ERROR = 2

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        code: str = proto.Field(
            proto.STRING,
            number=3,
        )
        count: int = proto.Field(
            proto.INT64,
            number=4,
        )
        severity: "FileUpload.Issue.Severity" = proto.Field(
            proto.ENUM,
            number=5,
            enum="FileUpload.Issue.Severity",
        )
        documentation_uri: str = proto.Field(
            proto.STRING,
            number=6,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    processing_state: ProcessingState = proto.Field(
        proto.ENUM,
        number=3,
        enum=ProcessingState,
    )
    issues: MutableSequence[Issue] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Issue,
    )
    items_total: int = proto.Field(
        proto.INT64,
        number=5,
    )
    items_created: int = proto.Field(
        proto.INT64,
        number=6,
    )
    items_updated: int = proto.Field(
        proto.INT64,
        number=7,
    )
    upload_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class GetFileUploadRequest(proto.Message):
    r"""Request message for the GetFileUploadRequest method.

    Attributes:
        name (str):
            Required. The name of the data source file upload to
            retrieve. Format:
            ``accounts/{account}/dataSources/{datasource}/fileUploads/latest``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
