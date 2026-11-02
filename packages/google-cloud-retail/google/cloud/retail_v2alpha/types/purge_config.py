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
    package="google.cloud.retail.v2alpha",
    manifest={
        "PurgeMetadata",
        "PurgeProductsMetadata",
        "PurgeProductsRequest",
        "PurgeProductsResponse",
        "PurgeUserEventsRequest",
        "PurgeUserEventsResponse",
    },
)


class PurgeMetadata(proto.Message):
    r"""Metadata related to the progress of the Purge operation.
    This will be returned by the
    google.longrunning.Operation.metadata field.

    """


class PurgeProductsMetadata(proto.Message):
    r"""Metadata related to the progress of the PurgeProducts
    operation. This will be returned by the
    google.longrunning.Operation.metadata field.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation last update time. If the operation
            is done, this is also the finish time.
        success_count (int):
            Count of entries that were deleted
            successfully.
        failure_count (int):
            Count of entries that encountered errors
            while processing.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    success_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    failure_count: int = proto.Field(
        proto.INT64,
        number=4,
    )


class PurgeProductsRequest(proto.Message):
    r"""Request message for PurgeProducts method.

    Attributes:
        parent (str):
            Required. The resource name of the branch under which the
            products are created. The format is
            ``projects/${projectId}/locations/global/catalogs/${catalogId}/branches/${branchId}``
        filter (str):
            Required. The filter string to specify the products to be
            deleted with a length limit of 5,000 characters.

            Empty string filter is not allowed. "\*" implies delete all
            items in a branch.

            The eligible fields for filtering are:

            - ``availability``: Double quoted
              [Product.availability][google.cloud.retail.v2alpha.Product.availability]
              string.
            - ``create_time`` : in ISO 8601 "zulu" format.

            Supported syntax:

            - Comparators (">", "<", ">=", "<=", "="). Examples:

              - create_time <= "2015-02-13T17:05:46Z"
              - availability = "IN_STOCK"

            - Conjunctions ("AND") Examples:

              - create_time <= "2015-02-13T17:05:46Z" AND availability =
                "PREORDER"

            - Disjunctions ("OR") Examples:

              - create_time <= "2015-02-13T17:05:46Z" OR availability =
                "IN_STOCK"

            - Can support nested queries. Examples:

              - (create_time <= "2015-02-13T17:05:46Z" AND availability
                = "PREORDER") OR (create_time >= "2015-02-14T13:03:32Z"
                AND availability = "IN_STOCK")

            - Filter Limits:

              - Filter should not contain more than 6 conditions.
              - Max nesting depth should not exceed 2 levels.

            Examples queries:

            - Delete back order products created before a timestamp.
              create_time <= "2015-02-13T17:05:46Z" OR availability =
              "BACKORDER".
        force (bool):
            Actually perform the purge. If ``force`` is set to false,
            the method will return the expected purge count without
            deleting any products.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class PurgeProductsResponse(proto.Message):
    r"""Response of the PurgeProductsRequest. If the long running
    operation is successfully done, then this message is returned by
    the google.longrunning.Operations.response field.

    Attributes:
        purge_count (int):
            The total count of products purged as a
            result of the operation.
        purge_sample (MutableSequence[str]):
            A sample of the product names that will be deleted. Only
            populated if ``force`` is set to false. A max of 100 names
            will be returned and the names are chosen at random.
    """

    purge_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    purge_sample: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class PurgeUserEventsRequest(proto.Message):
    r"""Request message for PurgeUserEvents method.

    Attributes:
        parent (str):
            Required. The resource name of the catalog under which the
            events are created. The format is
            ``projects/${projectId}/locations/global/catalogs/${catalogId}``
        filter (str):
            Required. The filter string to specify the events to be
            deleted with a length limit of 5,000 characters. Empty
            string filter is not allowed. The eligible fields for
            filtering are:

            - ``eventType``: Double quoted
              [UserEvent.event_type][google.cloud.retail.v2alpha.UserEvent.event_type]
              string.
            - ``eventTime``: in ISO 8601 "zulu" format.
            - ``visitorId``: Double quoted string. Specifying this will
              delete all events associated with a visitor.
            - ``userId``: Double quoted string. Specifying this will
              delete all events associated with a user.

            Examples:

            - Deleting all events in a time range:
              ``eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"``
            - Deleting specific eventType in time range:
              ``eventTime > "2012-04-23T18:25:43.511Z" eventType = "detail-page-view"``
            - Deleting all events for a specific visitor:
              ``visitorId = "visitor1024"``

            The filtering fields are assumed to have an implicit AND.
        force (bool):
            Actually perform the purge. If ``force`` is set to false,
            the method will return the expected purge count without
            deleting any user events.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class PurgeUserEventsResponse(proto.Message):
    r"""Response of the PurgeUserEventsRequest. If the long running
    operation is successfully done, then this message is returned by
    the google.longrunning.Operations.response field.

    Attributes:
        purged_events_count (int):
            The total count of events purged as a result
            of the operation.
    """

    purged_events_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
