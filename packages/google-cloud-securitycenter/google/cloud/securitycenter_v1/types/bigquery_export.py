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
    package="google.cloud.securitycenter.v1",
    manifest={
        "BigQueryExport",
    },
)


class BigQueryExport(proto.Message):
    r"""Configures how to deliver Findings to BigQuery Instance.

    Attributes:
        name (str):
            The relative resource name of this export. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name.
            Example format:
            "organizations/{organization_id}/bigQueryExports/{export_id}"
            Example format:
            "folders/{folder_id}/bigQueryExports/{export_id}" Example
            format: "projects/{project_id}/bigQueryExports/{export_id}"
            This field is provided in responses, and is ignored when
            provided in create requests.
        description (str):
            The description of the export (max of 1024
            characters).
        filter (str):
            Expression that defines the filter to apply across
            create/update events of findings. The expression is a list
            of zero or more restrictions combined via logical operators
            ``AND`` and ``OR``. Parentheses are supported, and ``OR``
            has higher precedence than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. The fields map to those defined in the
            corresponding resource.

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.
        dataset (str):
            The dataset to write findings' updates to. Its format is
            "projects/[project_id]/datasets/[bigquery_dataset_id]".
            BigQuery Dataset unique ID must contain only letters (a-z,
            A-Z), numbers (0-9), or underscores (\_).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the BigQuery
            export was created. This field is set by the
            server and will be ignored if provided on export
            on creation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the BigQuery export was updated. This field is
            set by the server and will be ignored if
            provided on export creation or update.
        most_recent_editor (str):
            Output only. Email address of the user who
            last edited the BigQuery export. This field is
            set by the server and will be ignored if
            provided on export creation or update.
        principal (str):
            Output only. The service account that needs
            permission to create table and upload data to
            the BigQuery dataset.
        deletion_notifications_enabled (bool):
            Optional. Indicates whether the notifications
            will be sent for deleted findings. When enabled,
            the filter is still respected when sending
            deletion notifications.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    dataset: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    most_recent_editor: str = proto.Field(
        proto.STRING,
        number=7,
    )
    principal: str = proto.Field(
        proto.STRING,
        number=8,
    )
    deletion_notifications_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
