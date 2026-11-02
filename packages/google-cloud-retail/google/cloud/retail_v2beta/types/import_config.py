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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2beta.types import product, user_event

__protobuf__ = proto.module(
    package="google.cloud.retail.v2beta",
    manifest={
        "GcsSource",
        "BigQuerySource",
        "ProductInlineSource",
        "UserEventInlineSource",
        "ImportErrorsConfig",
        "ImportProductsRequest",
        "ImportUserEventsRequest",
        "ImportCompletionDataRequest",
        "ProductInputConfig",
        "UserEventInputConfig",
        "CompletionDataInputConfig",
        "ImportMetadata",
        "ImportProductsResponse",
        "ImportUserEventsResponse",
        "UserEventImportSummary",
        "ImportCompletionDataResponse",
    },
)


class GcsSource(proto.Message):
    r"""Google Cloud Storage location for input content.

    Attributes:
        input_uris (MutableSequence[str]):
            Required. Google Cloud Storage URIs to input files. URI can
            be up to 2000 characters long. URIs can match the full
            object path (for example,
            ``gs://bucket/directory/object.json``) or a pattern matching
            one or more files, such as ``gs://bucket/directory/*.json``.
            A request can contain at most 100 files, and each file can
            be up to 2 GB. See `Importing product
            information <https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog>`__
            for the expected file format and setup instructions.
        data_schema (str):
            The schema to use when parsing the data from the source.

            Supported values for product imports:

            - ``product`` (default): One JSON
              [Product][google.cloud.retail.v2beta.Product] per line.
              Each product must have a valid
              [Product.id][google.cloud.retail.v2beta.Product.id].
            - ``product_merchant_center``: See `Importing catalog data
              from Merchant
              Center <https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog#mc>`__.

            Supported values for user events imports:

            - ``user_event`` (default): One JSON
              [UserEvent][google.cloud.retail.v2beta.UserEvent] per
              line.
            - ``user_event_ga360``: Using
              https://support.google.com/analytics/answer/3437719.

            Supported values for control imports:

            - ``control`` (default): One JSON
              [Control][google.cloud.retail.v2beta.Control] per line.

            Supported values for catalog attribute imports:

            - ``catalog_attribute`` (default): One CSV
              [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
              per line.
    """

    input_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    data_schema: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BigQuerySource(proto.Message):
    r"""BigQuery source import data from.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        partition_date (google.type.date_pb2.Date):
            BigQuery time partitioned table's \_PARTITIONDATE in
            YYYY-MM-DD format.

            This field is a member of `oneof`_ ``partition``.
        project_id (str):
            The project ID (can be project # or ID) that
            the BigQuery source is in with a length limit of
            128 characters. If not specified, inherits the
            project ID from the parent request.
        dataset_id (str):
            Required. The BigQuery data set to copy the
            data from with a length limit of 1,024
            characters.
        table_id (str):
            Required. The BigQuery table to copy the data
            from with a length limit of 1,024 characters.
        gcs_staging_dir (str):
            Intermediate Cloud Storage directory used for
            the import with a length limit of 2,000
            characters. Can be specified if one wants to
            have the BigQuery export to a specific Cloud
            Storage directory.
        data_schema (str):
            The schema to use when parsing the data from the source.

            Supported values for product imports:

            - ``product`` (default): One JSON
              [Product][google.cloud.retail.v2beta.Product] per line.
              Each product must have a valid
              [Product.id][google.cloud.retail.v2beta.Product.id].
            - ``product_merchant_center``: See `Importing catalog data
              from Merchant
              Center <https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog#mc>`__.

            Supported values for user events imports:

            - ``user_event`` (default): One JSON
              [UserEvent][google.cloud.retail.v2beta.UserEvent] per
              line.
            - ``user_event_ga360``: The schema is available here:
              https://support.google.com/analytics/answer/3437719.
            - ``user_event_ga4``: The schema is available here:
              https://support.google.com/analytics/answer/7029846.

            Supported values for autocomplete imports:

            - ``suggestions`` (default): One JSON completion suggestion
              per line.
            - ``denylist``: One JSON deny suggestion per line.
            - ``allowlist``: One JSON allow suggestion per line.
    """

    partition_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="partition",
        message=date_pb2.Date,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gcs_staging_dir: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_schema: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ProductInlineSource(proto.Message):
    r"""The inline source for the input config for ImportProducts
    method.

    Attributes:
        products (MutableSequence[google.cloud.retail_v2beta.types.Product]):
            Required. A list of products to update/create. Each product
            must have a valid
            [Product.id][google.cloud.retail.v2beta.Product.id].
            Recommended max of 100 items.
    """

    products: MutableSequence[product.Product] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=product.Product,
    )


class UserEventInlineSource(proto.Message):
    r"""The inline source for the input config for ImportUserEvents
    method.

    Attributes:
        user_events (MutableSequence[google.cloud.retail_v2beta.types.UserEvent]):
            Required. A list of user events to import.
            Recommended max of 10k items.
    """

    user_events: MutableSequence[user_event.UserEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=user_event.UserEvent,
    )


class ImportErrorsConfig(proto.Message):
    r"""Configuration of destination for Import related errors.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_prefix (str):
            Google Cloud Storage prefix for import errors. This must be
            an empty, existing Cloud Storage directory. Import errors
            are written to sharded files in this directory, one per
            line, as a JSON-encoded ``google.rpc.Status`` message.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_prefix: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="destination",
    )


class ImportProductsRequest(proto.Message):
    r"""Request message for Import methods.

    Attributes:
        parent (str):
            Required.
            ``projects/1234/locations/global/catalogs/default_catalog/branches/default_branch``

            If no updateMask is specified, requires products.create
            permission. If updateMask is specified, requires
            products.update permission.
        request_id (str):
            Deprecated. This field has no effect.
        input_config (google.cloud.retail_v2beta.types.ProductInputConfig):
            Required. The desired input location of the
            data.
        errors_config (google.cloud.retail_v2beta.types.ImportErrorsConfig):
            The desired location of errors incurred
            during the Import.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided imported ``products``
            to update. If not set, all fields are updated. If provided,
            only the existing product fields are updated. Missing
            products will not be created.
        reconciliation_mode (google.cloud.retail_v2beta.types.ImportProductsRequest.ReconciliationMode):
            The mode of reconciliation between existing products and the
            products to be imported. Defaults to
            [ReconciliationMode.INCREMENTAL][google.cloud.retail.v2beta.ImportProductsRequest.ReconciliationMode.INCREMENTAL].
        notification_pubsub_topic (str):
            Full Pub/Sub topic name for receiving notification. If this
            field is set, when the import is finished, a notification is
            sent to specified Pub/Sub topic. The message data is JSON
            string of a [Operation][google.longrunning.Operation].

            Format of the Pub/Sub topic is
            ``projects/{project}/topics/{topic}``. It has to be within
            the same project as
            [ImportProductsRequest.parent][google.cloud.retail.v2beta.ImportProductsRequest.parent].
            Make sure that both
            ``cloud-retail-customer-data-access@system.gserviceaccount.com``
            and
            ``service-<project number>@gcp-sa-retail.iam.gserviceaccount.com``
            have the ``pubsub.topics.publish`` IAM permission on the
            topic.

            Only supported when
            [ImportProductsRequest.reconciliation_mode][google.cloud.retail.v2beta.ImportProductsRequest.reconciliation_mode]
            is set to ``FULL``.
    """

    class ReconciliationMode(proto.Enum):
        r"""Indicates how imported products are reconciled with the
        existing products created or imported before.

        Values:
            RECONCILIATION_MODE_UNSPECIFIED (0):
                Defaults to INCREMENTAL.
            INCREMENTAL (1):
                Inserts new products or updates existing
                products.
            FULL (2):
                Calculates diff and replaces the entire
                product dataset. Existing products may be
                deleted if they are not present in the source
                location.
        """

        RECONCILIATION_MODE_UNSPECIFIED = 0
        INCREMENTAL = 1
        FULL = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    input_config: "ProductInputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProductInputConfig",
    )
    errors_config: "ImportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImportErrorsConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    reconciliation_mode: ReconciliationMode = proto.Field(
        proto.ENUM,
        number=5,
        enum=ReconciliationMode,
    )
    notification_pubsub_topic: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ImportUserEventsRequest(proto.Message):
    r"""Request message for the ImportUserEvents request.

    Attributes:
        parent (str):
            Required.
            ``projects/1234/locations/global/catalogs/default_catalog``
        input_config (google.cloud.retail_v2beta.types.UserEventInputConfig):
            Required. The desired input location of the
            data.
        errors_config (google.cloud.retail_v2beta.types.ImportErrorsConfig):
            The desired location of errors incurred
            during the Import. Cannot be set for inline user
            event imports.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config: "UserEventInputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserEventInputConfig",
    )
    errors_config: "ImportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImportErrorsConfig",
    )


class ImportCompletionDataRequest(proto.Message):
    r"""Request message for ImportCompletionData methods.

    Attributes:
        parent (str):
            Required. The catalog which the suggestions dataset belongs
            to.

            Format:
            ``projects/1234/locations/global/catalogs/default_catalog``.
        input_config (google.cloud.retail_v2beta.types.CompletionDataInputConfig):
            Required. The desired input location of the
            data.
        notification_pubsub_topic (str):
            Pub/Sub topic for receiving notification. If this field is
            set, when the import is finished, a notification is sent to
            specified Pub/Sub topic. The message data is JSON string of
            a [Operation][google.longrunning.Operation]. Format of the
            Pub/Sub topic is ``projects/{project}/topics/{topic}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config: "CompletionDataInputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CompletionDataInputConfig",
    )
    notification_pubsub_topic: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ProductInputConfig(proto.Message):
    r"""The input config source for products.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        product_inline_source (google.cloud.retail_v2beta.types.ProductInlineSource):
            The Inline source for the input content for
            products.

            This field is a member of `oneof`_ ``source``.
        gcs_source (google.cloud.retail_v2beta.types.GcsSource):
            Google Cloud Storage location for the input
            content.

            This field is a member of `oneof`_ ``source``.
        big_query_source (google.cloud.retail_v2beta.types.BigQuerySource):
            BigQuery input source.

            This field is a member of `oneof`_ ``source``.
    """

    product_inline_source: "ProductInlineSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="ProductInlineSource",
    )
    gcs_source: "GcsSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="GcsSource",
    )
    big_query_source: "BigQuerySource" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="BigQuerySource",
    )


class UserEventInputConfig(proto.Message):
    r"""The input config source for user events.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_event_inline_source (google.cloud.retail_v2beta.types.UserEventInlineSource):
            Required. The Inline source for the input
            content for UserEvents.

            This field is a member of `oneof`_ ``source``.
        gcs_source (google.cloud.retail_v2beta.types.GcsSource):
            Required. Google Cloud Storage location for
            the input content.

            This field is a member of `oneof`_ ``source``.
        big_query_source (google.cloud.retail_v2beta.types.BigQuerySource):
            Required. BigQuery input source.

            This field is a member of `oneof`_ ``source``.
    """

    user_event_inline_source: "UserEventInlineSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="UserEventInlineSource",
    )
    gcs_source: "GcsSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="GcsSource",
    )
    big_query_source: "BigQuerySource" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="BigQuerySource",
    )


class CompletionDataInputConfig(proto.Message):
    r"""The input config source for completion data.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        big_query_source (google.cloud.retail_v2beta.types.BigQuerySource):
            Required. BigQuery input source.

            Add the IAM permission "BigQuery Data Viewer"
            for
            cloud-retail-customer-data-access@system.gserviceaccount.com
            before using this feature otherwise an error is
            thrown.

            This field is a member of `oneof`_ ``source``.
    """

    big_query_source: "BigQuerySource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="BigQuerySource",
    )


class ImportMetadata(proto.Message):
    r"""Metadata related to the progress of the Import operation.
    This is returned by the google.longrunning.Operation.metadata
    field.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation last update time. If the operation
            is done, this is also the finish time.
        success_count (int):
            Count of entries that were processed
            successfully.
        failure_count (int):
            Count of entries that encountered errors
            while processing.
        request_id (str):
            Deprecated. This field is never set.
        notification_pubsub_topic (str):
            Pub/Sub topic for receiving notification. If this field is
            set, when the import is finished, a notification is sent to
            specified Pub/Sub topic. The message data is JSON string of
            a [Operation][google.longrunning.Operation]. Format of the
            Pub/Sub topic is ``projects/{project}/topics/{topic}``.
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
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    notification_pubsub_topic: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ImportProductsResponse(proto.Message):
    r"""Response of the
    [ImportProductsRequest][google.cloud.retail.v2beta.ImportProductsRequest].
    If the long running operation is done, then this message is returned
    by the google.longrunning.Operations.response field if the operation
    was successful.

    Attributes:
        error_samples (MutableSequence[google.rpc.status_pb2.Status]):
            A sample of errors encountered while
            processing the request.
        errors_config (google.cloud.retail_v2beta.types.ImportErrorsConfig):
            Echoes the destination for the complete
            errors in the request if set.
    """

    error_samples: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    errors_config: "ImportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ImportErrorsConfig",
    )


class ImportUserEventsResponse(proto.Message):
    r"""Response of the ImportUserEventsRequest. If the long running
    operation was successful, then this message is returned by the
    google.longrunning.Operations.response field if the operation
    was successful.

    Attributes:
        error_samples (MutableSequence[google.rpc.status_pb2.Status]):
            A sample of errors encountered while
            processing the request.
        errors_config (google.cloud.retail_v2beta.types.ImportErrorsConfig):
            Echoes the destination for the complete
            errors if this field was set in the request.
        import_summary (google.cloud.retail_v2beta.types.UserEventImportSummary):
            Aggregated statistics of user event import
            status.
    """

    error_samples: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    errors_config: "ImportErrorsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ImportErrorsConfig",
    )
    import_summary: "UserEventImportSummary" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UserEventImportSummary",
    )


class UserEventImportSummary(proto.Message):
    r"""A summary of import result. The UserEventImportSummary
    summarizes the import status for user events.

    Attributes:
        joined_events_count (int):
            Count of user events imported with complete
            existing catalog information.
        unjoined_events_count (int):
            Count of user events imported, but with
            catalog information not found in the imported
            catalog.
    """

    joined_events_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    unjoined_events_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ImportCompletionDataResponse(proto.Message):
    r"""Response of the
    [ImportCompletionDataRequest][google.cloud.retail.v2beta.ImportCompletionDataRequest].
    If the long running operation is done, this message is returned by
    the google.longrunning.Operations.response field if the operation is
    successful.

    Attributes:
        error_samples (MutableSequence[google.rpc.status_pb2.Status]):
            A sample of errors encountered while
            processing the request.
    """

    error_samples: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
