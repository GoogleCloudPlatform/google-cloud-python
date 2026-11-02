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

__protobuf__ = proto.module(
    package="google.cloud.financialservices.v1",
    manifest={
        "BigQueryDestination",
    },
)


class BigQueryDestination(proto.Message):
    r"""BigQueryDestination is a wrapper for BigQuery output
    information.

    Attributes:
        table_uri (str):
            Optional. BigQuery URI to a table, must be of
            the form bq://projectId.bqDatasetId.tableId.
            Note that the BigQuery dataset must already
            exist. VPC-SC restrictions apply.
        write_disposition (google.cloud.financialservices_v1.types.BigQueryDestination.WriteDisposition):
            Required. Whether or not to overwrite the
            destination table. By default the table won't be
            overwritten and an error will be returned if the
            table exists and contains data.
    """

    class WriteDisposition(proto.Enum):
        r"""WriteDisposition controls the behavior when the destination
        table already exists.

        Values:
            WRITE_DISPOSITION_UNSPECIFIED (0):
                Default behavior is the same as WRITE_EMPTY.
            WRITE_EMPTY (1):
                If the table already exists and contains
                data, an error is returned.
            WRITE_TRUNCATE (2):
                If the table already exists, the data will be
                overwritten.
        """

        WRITE_DISPOSITION_UNSPECIFIED = 0
        WRITE_EMPTY = 1
        WRITE_TRUNCATE = 2

    table_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    write_disposition: WriteDisposition = proto.Field(
        proto.ENUM,
        number=2,
        enum=WriteDisposition,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
