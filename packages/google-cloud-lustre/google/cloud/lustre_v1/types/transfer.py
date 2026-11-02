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
import google.rpc.code_pb2 as code_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.lustre.v1",
    manifest={
        "TransferType",
        "ImportDataRequest",
        "ExportDataRequest",
        "ExportDataResponse",
        "ImportDataResponse",
        "ExportDataMetadata",
        "ImportDataMetadata",
        "GcsPath",
        "LustrePath",
        "TransferCounters",
        "ErrorLogEntry",
        "ErrorSummary",
        "TransferOperationMetadata",
    },
)


class TransferType(proto.Enum):
    r"""Type of transfer that occurred.

    Values:
        TRANSFER_TYPE_UNSPECIFIED (0):
            Zero is an illegal value.
        IMPORT (1):
            Imports to Lustre.
        EXPORT (2):
            Exports from Lustre.
    """

    TRANSFER_TYPE_UNSPECIFIED = 0
    IMPORT = 1
    EXPORT = 2


class ImportDataRequest(proto.Message):
    r"""Message for importing data to Lustre.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_path (google.cloud.lustre_v1.types.GcsPath):
            The Cloud Storage source bucket and, optionally, path inside
            the bucket. If a path inside the bucket is specified, it
            must end with a forward slash (``/``).

            This field is a member of `oneof`_ ``source``.
        lustre_path (google.cloud.lustre_v1.types.LustrePath):
            Lustre path destination.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. The name of the Managed Lustre instance in the
            format
            ``projects/{project}/locations/{location}/instances/{instance}``.
        request_id (str):
            Optional. UUID to identify requests.
        service_account (str):
            Optional. User-specified service account used to perform the
            transfer. If unspecified, the default Managed Lustre service
            agent will be used.

            Use one of the following formats:

            - ``{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``
    """

    gcs_path: "GcsPath" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="GcsPath",
    )
    lustre_path: "LustrePath" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination",
        message="LustrePath",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ExportDataRequest(proto.Message):
    r"""Export data from Managed Lustre to a Cloud Storage bucket.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        lustre_path (google.cloud.lustre_v1.types.LustrePath):
            The root directory path to the Managed Lustre file system.
            Must start with ``/``. Default is ``/``.

            This field is a member of `oneof`_ ``source``.
        gcs_path (google.cloud.lustre_v1.types.GcsPath):
            The URI to a Cloud Storage bucket, or a path within a
            bucket, using the format
            ``gs://<bucket_name>/<optional_path_inside_bucket>/``. If a
            path inside the bucket is specified, it must end with a
            forward slash (``/``).

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. The name of the Managed Lustre instance in the
            format
            ``projects/{project}/locations/{location}/instances/{instance}``.
        request_id (str):
            Optional. UUID to identify requests.
        service_account (str):
            Optional. User-specified service account used to perform the
            transfer. If unspecified, the Managed Lustre service agent
            is used.

            Use one of the following formats:

            - ``{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``
    """

    lustre_path: "LustrePath" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="LustrePath",
    )
    gcs_path: "GcsPath" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination",
        message="GcsPath",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ExportDataResponse(proto.Message):
    r"""Response message for ExportData."""


class ImportDataResponse(proto.Message):
    r"""Response message for ImportData."""


class ExportDataMetadata(proto.Message):
    r"""Metadata of the export data operation.

    Attributes:
        operation_metadata (google.cloud.lustre_v1.types.TransferOperationMetadata):
            Data transfer operation metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    operation_metadata: "TransferOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TransferOperationMetadata",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=4,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=5,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ImportDataMetadata(proto.Message):
    r"""Metadata of the import data operation.

    Attributes:
        operation_metadata (google.cloud.lustre_v1.types.TransferOperationMetadata):
            Data transfer operation metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        status_message (str):
            Output only. Name of the verb executed by the
            operation.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    operation_metadata: "TransferOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TransferOperationMetadata",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GcsPath(proto.Message):
    r"""Specifies a Cloud Storage bucket and, optionally, a path
    inside the bucket.

    Attributes:
        uri (str):
            Required. The URI to a Cloud Storage bucket, or a path
            within a bucket, using the format
            ``gs://<bucket_name>/<optional_path_inside_bucket>/``. If a
            path inside the bucket is specified, it must end with a
            forward slash (``/``).
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LustrePath(proto.Message):
    r"""The root directory path to the Lustre file system.

    Attributes:
        path (str):
            Optional. The root directory path to the Managed Lustre file
            system. Must start with ``/``. Default is ``/``. If you're
            importing data into Managed Lustre, any path other than the
            default must already exist on the file system.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TransferCounters(proto.Message):
    r"""A collection of counters that report the progress of a
    transfer operation.

    Attributes:
        found_objects_count (int):
            Objects found in the data source that are
            scheduled to be transferred, excluding any that
            are filtered based on object conditions or
            skipped due to sync.
        bytes_found_count (int):
            Total number of bytes found in the data
            source that are scheduled to be transferred,
            excluding any that are filtered based on object
            conditions or skipped due to sync.
        objects_skipped_count (int):
            Objects in the data source that are not
            transferred because they already exist in the
            data destination.
        bytes_skipped_count (int):
            Bytes in the data source that are not
            transferred because they already exist in the
            data destination.
        objects_copied_count (int):
            Objects that are copied to the data
            destination.
        bytes_copied_count (int):
            Bytes that are copied to the data
            destination.
        objects_failed_count (int):
            Output only. Objects that are failed to write
            to the data destination.
        bytes_failed_count (int):
            Output only. Bytes that are failed to write
            to the data destination.
    """

    found_objects_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    bytes_found_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    objects_skipped_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    bytes_skipped_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    objects_copied_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    bytes_copied_count: int = proto.Field(
        proto.INT64,
        number=6,
    )
    objects_failed_count: int = proto.Field(
        proto.INT64,
        number=7,
    )
    bytes_failed_count: int = proto.Field(
        proto.INT64,
        number=8,
    )


class ErrorLogEntry(proto.Message):
    r"""An entry describing an error that has occurred.

    Attributes:
        uri (str):
            Required. A URL that refers to the target (a
            data source, a data sink, or an object) with
            which the error is associated.
        error_details (MutableSequence[str]):
            A list of messages that carry the error
            details.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_details: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ErrorSummary(proto.Message):
    r"""A summary of errors by error code, plus a count and sample
    error log entries.

    Attributes:
        error_code (google.rpc.code_pb2.Code):
            Required.
        error_count (int):
            Required. Count of this type of error.
        error_log_entries (MutableSequence[google.cloud.lustre_v1.types.ErrorLogEntry]):
            Error samples.

            At most 5 error log entries are recorded for a
            given error code for a single transfer
            operation.
    """

    error_code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    error_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    error_log_entries: MutableSequence["ErrorLogEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ErrorLogEntry",
    )


class TransferOperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running transfer
    operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_lustre_path (google.cloud.lustre_v1.types.LustrePath):
            Output only. Lustre source.

            This field is a member of `oneof`_ ``source``.
        source_gcs_path (google.cloud.lustre_v1.types.GcsPath):
            Output only. Cloud Storage source.

            This field is a member of `oneof`_ ``source``.
        destination_gcs_path (google.cloud.lustre_v1.types.GcsPath):
            Output only. Cloud Storage destination.

            This field is a member of `oneof`_ ``destination``.
        destination_lustre_path (google.cloud.lustre_v1.types.LustrePath):
            Output only. Lustre destination.

            This field is a member of `oneof`_ ``destination``.
        counters (google.cloud.lustre_v1.types.TransferCounters):
            Output only. The progress of the transfer
            operation.
        transfer_type (google.cloud.lustre_v1.types.TransferType):
            Output only. The type of transfer occurring.
        error_summaries (MutableSequence[google.cloud.lustre_v1.types.ErrorSummary]):
            Output only. Error summary about the transfer
            operation
    """

    source_lustre_path: "LustrePath" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="LustrePath",
    )
    source_gcs_path: "GcsPath" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message="GcsPath",
    )
    destination_gcs_path: "GcsPath" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="destination",
        message="GcsPath",
    )
    destination_lustre_path: "LustrePath" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="destination",
        message="LustrePath",
    )
    counters: "TransferCounters" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TransferCounters",
    )
    transfer_type: "TransferType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="TransferType",
    )
    error_summaries: MutableSequence["ErrorSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ErrorSummary",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
