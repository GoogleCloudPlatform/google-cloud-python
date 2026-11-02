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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "OutputConfig",
        "ExportErrorsConfig",
        "ExportProductsRequest",
        "ExportUserEventsRequest",
        "ExportAnalyticsMetricsRequest",
        "ExportMetadata",
        "ExportProductsResponse",
        "ExportUserEventsResponse",
        "ExportAnalyticsMetricsResponse",
        "OutputResult",
        "BigQueryOutputResult",
        "GcsOutputResult",
    },
)


class OutputConfig(proto.Message):
    r"""The output configuration setting.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.retail_v2alpha.types.OutputConfig.GcsDestination):
            The Google Cloud Storage location where the
            output is to be written to.

            This field is a member of `oneof`_ ``destination``.
        bigquery_destination (google.cloud.retail_v2alpha.types.OutputConfig.BigQueryDestination):
            The BigQuery location where the output is to
            be written to.

            This field is a member of `oneof`_ ``destination``.
    """

    class GcsDestination(proto.Message):
        r"""The Google Cloud Storage output destination configuration.

        Attributes:
            output_uri_prefix (str):
                Required. The output uri prefix for saving output data to
                json files. Some mapping examples are as follows:
                output_uri_prefix sample output(assuming the object is
                foo.json) ========================
                ============================================= gs://bucket/
                gs://bucket/foo.json gs://bucket/folder/
                gs://bucket/folder/foo.json gs://bucket/folder/item\_
                gs://bucket/folder/item_foo.json
        """

        output_uri_prefix: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class BigQueryDestination(proto.Message):
        r"""The BigQuery output destination configuration.

        Attributes:
            dataset_id (str):
                Required. The ID of a BigQuery Dataset.
            table_id_prefix (str):
                Required. The prefix of exported BigQuery
                tables.
            table_type (str):
                Required. Describes the table type. The following values are
                supported:

                - ``table``: A BigQuery native table.
                - ``view``: A virtual table defined by a SQL query.
        """

        dataset_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table_id_prefix: str = proto.Field(
            proto.STRING,
            number=2,
        )
        table_type: str = proto.Field(
            proto.STRING,
            number=3,
        )

    gcs_destination: GcsDestination = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message=GcsDestination,
    )
    bigquery_destination: BigQueryDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message=BigQueryDestination,
    )


class ExportErrorsConfig(proto.Message):
    r"""Configuration of destination for Export related errors.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_prefix (str):
            Google Cloud Storage path for import errors. This must be an
            empty, existing Cloud Storage bucket. Export errors will be
            written to a file in this bucket, one per line, as a
            JSON-encoded ``google.rpc.Status`` message.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_prefix: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="destination",
    )


class ExportProductsRequest(proto.Message):
    r"""Request message for ExportProducts method.

    Attributes:
        parent (str):
            Required. Resource name of a
            [Branch][google.cloud.retail.v2alpha.Branch], and
            ``default_branch`` for branch_id component is supported. For
            example
            ``projects/1234/locations/global/catalogs/default_catalog/branches/default_branch``
        output_config (google.cloud.retail_v2alpha.types.OutputConfig):
            Required. The output location of the data.
        filter (str):
            A filtering expression to specify restrictions on returned
            events. The expression is a sequence of terms. Each term
            applies a restriction to the returned products. Use this
            expression to restrict results to a specific time range,
            tag, or stock state or to filter products by product type.
            For example,
            ``lastModifiedTime > "2012-04-23T18:25:43.511Z" lastModifiedTime<"2012-04-23T18:25:43.511Z" productType=primary``

            We expect only four types of fields:

            ::

               * `lastModifiedTime`: This can be specified twice, once with a
                 less than operator and once with a greater than operator. The
                 `lastModifiedTime` restriction should result in one, contiguous,
                 valid, last-modified, time range.

               * `productType`: Supported values are `primary` and `variant`. The
               Boolean operators `OR` and `NOT` are supported if the expression is
               enclosed in parentheses and must be separated from the
                 `productType` values by a space.

               * `availability`: Supported values are `IN_STOCK`, `OUT_OF_STOCK`,
               `PREORDER`, and `BACKORDER`. Boolean operators `OR` and `NOT` are
               supported if the expression is enclosed in parentheses and must be
               separated from the `availability` values by a space.

               * `Tag expressions`: Restricts output to products that match all of the
                 specified tags. Boolean operators `OR` and `NOT` are supported if the
                 expression is enclosed in parentheses and the operators are separated
                 from the tag values by a space. Also supported is '`-"tagA"`', which
                 is equivalent to '`NOT "tagA"`'. Tag values must be double-quoted,
                 UTF-8 encoded strings and have a size limit of 1,000 characters.

            Some examples of valid filters expressions:

            - Example 1:
              ``lastModifiedTime > "2012-04-23T18:25:43.511Z" lastModifiedTime < "2012-04-23T18:30:43.511Z"``
            - Example 2:
              ``lastModifiedTime > "2012-04-23T18:25:43.511Z" productType = "variant"``
            - Example 3:
              ``tag=("Red" OR "Blue") tag="New-Arrival" tag=(NOT "promotional") productType = "primary" lastModifiedTime < "2018-04-23T18:30:43.511Z"``
            - Example 4:
              ``lastModifiedTime > "2012-04-23T18:25:43.511Z"``
            - Example 5: ``availability = (IN_STOCK OR BACKORDER)``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputConfig",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExportUserEventsRequest(proto.Message):
    r"""Request message for the ``ExportUserEvents`` method.

    Attributes:
        parent (str):
            Required. Resource name of a
            [Catalog][google.cloud.retail.v2alpha.Catalog]. For example
            ``projects/1234/locations/global/catalogs/default_catalog``
        output_config (google.cloud.retail_v2alpha.types.OutputConfig):
            Required. The output location of the data.
        filter (str):
            A filtering expression to specify restrictions on returned
            events. The expression is a sequence of terms. Each term
            applies a restriction to the returned user events. Use this
            expression to restrict results to a specific time range or
            to filter events by eventType. For example,
            ``eventTime > "2012-04-23T18:25:43.511Z" eventsMissingCatalogItems eventTime<"2012-04-23T18:25:43.511Z" eventType=search``

            We expect only three types of fields:

            ::

               * `eventTime`: This can be specified twice, once with a
                 less than operator and once with a greater than operator. The
                 `eventTime` restriction should result in one, contiguous, valid,
                 `eventTime` range.

               * `eventType`: Boolean operators `OR` and `NOT` are supported if the
                 expression is enclosed in parentheses and the operators are separated
                 from the tag values by a space.

               * `eventsMissingCatalogItems`: This restricts results
                 to events for which catalog items were not found in the catalog. The
                 default behavior is to return only those events for which catalog
                 items were found.

            Some examples of valid filters expressions:

            - Example 1:
              ``eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"``
            - Example 2:
              ``eventTime > "2012-04-23T18:25:43.511Z" eventType = detail-page-view``
            - Example 3:
              ``eventsMissingCatalogItems eventType = (NOT search) eventTime < "2018-04-23T18:30:43.511Z"``
            - Example 4: ``eventTime > "2012-04-23T18:25:43.511Z"``
            - Example 5: ``eventType = (detail-page-view OR search)``
            - Example 6: ``eventsMissingCatalogItems``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputConfig",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExportAnalyticsMetricsRequest(proto.Message):
    r"""Request message for the ``ExportAnalyticsMetrics`` method.

    Attributes:
        catalog (str):
            Required. Full resource name of the parent catalog. Expected
            format: ``projects/*/locations/*/catalogs/*``
        output_config (google.cloud.retail_v2alpha.types.OutputConfig):
            Required. The output location of the data.
        filter (str):
            A filtering expression to specify restrictions on returned
            metrics. The expression is a sequence of terms. Each term
            applies a restriction to the returned metrics. Use this
            expression to restrict results to a specific time range.

            Currently we expect only one types of fields:

            ::

               * `timestamp`: This can be specified twice, once with a
                 less than operator and once with a greater than operator. The
                 `timestamp` restriction should result in one, contiguous, valid,
                 `timestamp` range.

            Some examples of valid filters expressions:

            - Example 1:
              ``timestamp > "2012-04-23T18:25:43.511Z" timestamp < "2012-04-23T18:30:43.511Z"``
            - Example 2: ``timestamp > "2012-04-23T18:25:43.511Z"``
    """

    catalog: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputConfig",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExportMetadata(proto.Message):
    r"""Metadata related to the progress of the Export operation.
    This is returned by the google.longrunning.Operation.metadata
    field.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation last update time. If the operation
            is done, this is also the finish time.
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


class ExportProductsResponse(proto.Message):
    r"""Response of the ExportProductsRequest. If the long running
    operation is done, then this message is returned by the
    google.longrunning.Operations.response field if the operation
    was successful.

    Attributes:
        error_samples (MutableSequence[google.rpc.status_pb2.Status]):
            A sample of errors encountered while
            processing the request.
        errors_config (google.cloud.retail_v2alpha.types.ExportErrorsConfig):
            This field is never set.
        output_result (google.cloud.retail_v2alpha.types.OutputResult):
            Output result indicating where the data were
            exported to.
    """

    error_samples: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    errors_config: "ExportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExportErrorsConfig",
    )
    output_result: "OutputResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputResult",
    )


class ExportUserEventsResponse(proto.Message):
    r"""Response of the ExportUserEventsRequest. If the long running
    operation was successful, then this message is returned by the
    google.longrunning.Operations.response field if the operation
    was successful.

    Attributes:
        error_samples (MutableSequence[google.rpc.status_pb2.Status]):
            A sample of errors encountered while
            processing the request.
        errors_config (google.cloud.retail_v2alpha.types.ExportErrorsConfig):
            This field is never set.
        output_result (google.cloud.retail_v2alpha.types.OutputResult):
            Output result indicating where the data were
            exported to.
    """

    error_samples: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    errors_config: "ExportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExportErrorsConfig",
    )
    output_result: "OutputResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputResult",
    )


class ExportAnalyticsMetricsResponse(proto.Message):
    r"""Response of the ExportAnalyticsMetricsRequest. If the long
    running operation was successful, then this message is returned
    by the google.longrunning.Operations.response field if the
    operation was successful.

    Attributes:
        error_samples (MutableSequence[google.rpc.status_pb2.Status]):
            A sample of errors encountered while
            processing the request.
        errors_config (google.cloud.retail_v2alpha.types.ExportErrorsConfig):
            This field is never set.
        output_result (google.cloud.retail_v2alpha.types.OutputResult):
            Output result indicating where the data were
            exported to.
    """

    error_samples: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    errors_config: "ExportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExportErrorsConfig",
    )
    output_result: "OutputResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputResult",
    )


class OutputResult(proto.Message):
    r"""Output result that stores the information about where the
    exported data is stored.

    Attributes:
        bigquery_result (MutableSequence[google.cloud.retail_v2alpha.types.BigQueryOutputResult]):
            The BigQuery location where the result is
            stored.
        gcs_result (MutableSequence[google.cloud.retail_v2alpha.types.GcsOutputResult]):
            The Google Cloud Storage location where the
            result is stored.
    """

    bigquery_result: MutableSequence["BigQueryOutputResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BigQueryOutputResult",
    )
    gcs_result: MutableSequence["GcsOutputResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="GcsOutputResult",
    )


class BigQueryOutputResult(proto.Message):
    r"""A BigQuery output result.

    Attributes:
        dataset_id (str):
            The ID of a BigQuery Dataset.
        table_id (str):
            The ID of a BigQuery Table.
    """

    dataset_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GcsOutputResult(proto.Message):
    r"""A Gcs output result.

    Attributes:
        output_uri (str):
            The uri of Gcs output
    """

    output_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
