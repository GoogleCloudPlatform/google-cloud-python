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
import google.rpc.code_pb2 as code_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.parallelstore.v1",
    manifest={
        "TransferType",
        "FileStripeLevel",
        "DirectoryStripeLevel",
        "DeploymentType",
        "Instance",
        "TransferMetadataOptions",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "OperationMetadata",
        "SourceGcsBucket",
        "DestinationGcsBucket",
        "SourceParallelstore",
        "DestinationParallelstore",
        "ImportDataRequest",
        "ExportDataRequest",
        "ImportDataResponse",
        "TransferErrorLogEntry",
        "TransferErrorSummary",
        "ImportDataMetadata",
        "ExportDataResponse",
        "ExportDataMetadata",
        "TransferOperationMetadata",
        "TransferCounters",
    },
)


class TransferType(proto.Enum):
    r"""Type of transfer that occurred.

    Values:
        TRANSFER_TYPE_UNSPECIFIED (0):
            Zero is an illegal value.
        IMPORT (1):
            Imports to Parallelstore.
        EXPORT (2):
            Exports from Parallelstore.
    """

    TRANSFER_TYPE_UNSPECIFIED = 0
    IMPORT = 1
    EXPORT = 2


class FileStripeLevel(proto.Enum):
    r"""Represents the striping options for files.

    Values:
        FILE_STRIPE_LEVEL_UNSPECIFIED (0):
            If not set, FileStripeLevel will default to
            FILE_STRIPE_LEVEL_BALANCED
        FILE_STRIPE_LEVEL_MIN (1):
            Minimum file striping
        FILE_STRIPE_LEVEL_BALANCED (2):
            Medium file striping
        FILE_STRIPE_LEVEL_MAX (3):
            Maximum file striping
    """

    FILE_STRIPE_LEVEL_UNSPECIFIED = 0
    FILE_STRIPE_LEVEL_MIN = 1
    FILE_STRIPE_LEVEL_BALANCED = 2
    FILE_STRIPE_LEVEL_MAX = 3


class DirectoryStripeLevel(proto.Enum):
    r"""Represents the striping options for directories.

    Values:
        DIRECTORY_STRIPE_LEVEL_UNSPECIFIED (0):
            If not set, DirectoryStripeLevel will default to
            DIRECTORY_STRIPE_LEVEL_MAX
        DIRECTORY_STRIPE_LEVEL_MIN (1):
            Minimum directory striping
        DIRECTORY_STRIPE_LEVEL_BALANCED (2):
            Medium directory striping
        DIRECTORY_STRIPE_LEVEL_MAX (3):
            Maximum directory striping
    """

    DIRECTORY_STRIPE_LEVEL_UNSPECIFIED = 0
    DIRECTORY_STRIPE_LEVEL_MIN = 1
    DIRECTORY_STRIPE_LEVEL_BALANCED = 2
    DIRECTORY_STRIPE_LEVEL_MAX = 3


class DeploymentType(proto.Enum):
    r"""Represents the deployment type for the instance.

    Values:
        DEPLOYMENT_TYPE_UNSPECIFIED (0):
            Default Deployment Type
            It is equivalent to SCRATCH
        SCRATCH (1):
            Scratch
        PERSISTENT (2):
            Persistent
    """

    DEPLOYMENT_TYPE_UNSPECIFIED = 0
    SCRATCH = 1
    PERSISTENT = 2


class Instance(proto.Message):
    r"""A Parallelstore instance.

    Attributes:
        name (str):
            Identifier. The resource name of the instance, in the format
            ``projects/{project}/locations/{location}/instances/{instance_id}``.
        description (str):
            Optional. The description of the instance.
            2048 characters or less.
        state (google.cloud.parallelstore_v1.types.Instance.State):
            Output only. The instance state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            updated.
        labels (MutableMapping[str, str]):
            Optional. Cloud Labels are a flexible and
            lightweight mechanism for organizing cloud
            resources into groups that reflect a customer's
            organizational needs and deployment strategies.
            See
            https://cloud.google.com/resource-manager/docs/labels-overview
            for details.
        capacity_gib (int):
            Required. Immutable. The instance's storage
            capacity in Gibibytes (GiB). Allowed values are
            between 12000 and 100000, in multiples of 4000;
            e.g., 12000, 16000, 20000, ...
        daos_version (str):
            Output only. Deprecated: The version of DAOS
            software running in the instance.
        access_points (MutableSequence[str]):
            Output only. A list of IPv4 addresses used
            for client side configuration.
        network (str):
            Optional. Immutable. The name of the Compute Engine `VPC
            network <https://cloud.google.com/vpc/docs/vpc>`__ to which
            the instance is connected.
        reserved_ip_range (str):
            Optional. Immutable. The ID of the IP address range being
            used by the instance's VPC network. See `Configure a VPC
            network <https://cloud.google.com/parallelstore/docs/vpc#create_and_configure_the_vpc>`__.
            If no ID is provided, all ranges are considered.
        effective_reserved_ip_range (str):
            Output only. Immutable. The ID of the IP
            address range being used by the instance's VPC
            network. This field is populated by the service
            and contains the value currently used by the
            service.
        file_stripe_level (google.cloud.parallelstore_v1.types.FileStripeLevel):
            Optional. Immutable. Stripe level for files. Allowed values
            are:

            - ``FILE_STRIPE_LEVEL_MIN``: offers the best performance for
              small size files.
            - ``FILE_STRIPE_LEVEL_BALANCED``: balances performance for
              workloads involving a mix of small and large files.
            - ``FILE_STRIPE_LEVEL_MAX``: higher throughput performance
              for larger files.
        directory_stripe_level (google.cloud.parallelstore_v1.types.DirectoryStripeLevel):
            Optional. Immutable. Stripe level for directories. Allowed
            values are:

            - ``DIRECTORY_STRIPE_LEVEL_MIN``: recommended when
              directories contain a small number of files.
            - ``DIRECTORY_STRIPE_LEVEL_BALANCED``: balances performance
              for workloads involving a mix of small and large
              directories.
            - ``DIRECTORY_STRIPE_LEVEL_MAX``: recommended for
              directories with a large number of files.
        deployment_type (google.cloud.parallelstore_v1.types.DeploymentType):
            Optional. Immutable. The deployment type of the instance.
            Allowed values are:

            - ``SCRATCH``: the instance is a scratch instance.
            - ``PERSISTENT``: the instance is a persistent instance.
    """

    class State(proto.Enum):
        r"""The possible states of a Parallelstore instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                The instance is being created.
            ACTIVE (2):
                The instance is available for use.
            DELETING (3):
                The instance is being deleted.
            FAILED (4):
                The instance is not usable.
            UPGRADING (5):
                The instance is being upgraded.
            REPAIRING (6):
                The instance is being repaired. This should only be used by
                instances using the ``PERSISTENT`` deployment type.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        FAILED = 4
        UPGRADING = 5
        REPAIRING = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    capacity_gib: int = proto.Field(
        proto.INT64,
        number=8,
    )
    daos_version: str = proto.Field(
        proto.STRING,
        number=9,
    )
    access_points: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    network: str = proto.Field(
        proto.STRING,
        number=11,
    )
    reserved_ip_range: str = proto.Field(
        proto.STRING,
        number=12,
    )
    effective_reserved_ip_range: str = proto.Field(
        proto.STRING,
        number=14,
    )
    file_stripe_level: "FileStripeLevel" = proto.Field(
        proto.ENUM,
        number=15,
        enum="FileStripeLevel",
    )
    directory_stripe_level: "DirectoryStripeLevel" = proto.Field(
        proto.ENUM,
        number=16,
        enum="DirectoryStripeLevel",
    )
    deployment_type: "DeploymentType" = proto.Field(
        proto.ENUM,
        number=17,
        enum="DeploymentType",
    )


class TransferMetadataOptions(proto.Message):
    r"""Transfer metadata options for the instance.

    Attributes:
        uid (google.cloud.parallelstore_v1.types.TransferMetadataOptions.Uid):
            Optional. The UID preservation behavior.
        gid (google.cloud.parallelstore_v1.types.TransferMetadataOptions.Gid):
            Optional. The GID preservation behavior.
        mode (google.cloud.parallelstore_v1.types.TransferMetadataOptions.Mode):
            Optional. The mode preservation behavior.
    """

    class Uid(proto.Enum):
        r"""The UID preservation behavior.

        Values:
            UID_UNSPECIFIED (0):
                default is UID_NUMBER_PRESERVE.
            UID_SKIP (1):
                Do not preserve UID during a transfer job.
            UID_NUMBER_PRESERVE (2):
                Preserve UID that is in number format during
                a transfer job.
        """

        UID_UNSPECIFIED = 0
        UID_SKIP = 1
        UID_NUMBER_PRESERVE = 2

    class Gid(proto.Enum):
        r"""The GID preservation behavior.

        Values:
            GID_UNSPECIFIED (0):
                default is GID_NUMBER_PRESERVE.
            GID_SKIP (1):
                Do not preserve GID during a transfer job.
            GID_NUMBER_PRESERVE (2):
                Preserve GID that is in number format during
                a transfer job.
        """

        GID_UNSPECIFIED = 0
        GID_SKIP = 1
        GID_NUMBER_PRESERVE = 2

    class Mode(proto.Enum):
        r"""The mode preservation behavior.

        Values:
            MODE_UNSPECIFIED (0):
                default is MODE_PRESERVE.
            MODE_SKIP (1):
                Do not preserve mode during a transfer job.
            MODE_PRESERVE (2):
                Preserve mode during a transfer job.
        """

        MODE_UNSPECIFIED = 0
        MODE_SKIP = 1
        MODE_PRESERVE = 2

    uid: Uid = proto.Field(
        proto.ENUM,
        number=1,
        enum=Uid,
    )
    gid: Gid = proto.Field(
        proto.ENUM,
        number=2,
        enum=Gid,
    )
    mode: Mode = proto.Field(
        proto.ENUM,
        number=3,
        enum=Mode,
    )


class ListInstancesRequest(proto.Message):
    r"""List instances request.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            instance information, in the format
            ``projects/{project_id}/locations/{location}``.

            To retrieve instance information for all locations, use "-"
            as the value of ``{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, the server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInstancesResponse(proto.Message):
    r"""Response from
    [ListInstances][google.cloud.parallelstore.v1.Parallelstore.ListInstances].

    Attributes:
        instances (MutableSequence[google.cloud.parallelstore_v1.types.Instance]):
            The list of Parallelstore instances.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Get an instance's details.

    Attributes:
        name (str):
            Required. The instance resource name, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Create a new Parallelstore instance.

    Attributes:
        parent (str):
            Required. The instance's project and location, in the format
            ``projects/{project}/locations/{location}``. Locations map
            to Google Cloud zones; for example, ``us-west1-b``.
        instance_id (str):
            Required. The name of the Parallelstore instance.

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the customer project / location
        instance (google.cloud.parallelstore_v1.types.Instance):
            Required. The instance to create.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Update an instance.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. Field mask is used to
            specify the fields to be overwritten in the Instance
            resource by the update. At least one path must be supplied
            in this field. The fields specified in the update_mask are
            relative to the resource, not the full request.
        instance (google.cloud.parallelstore_v1.types.Instance):
            Required. The instance to update.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Delete an instance.

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
    r"""Long-running operation metadata.

    Attributes:
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
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [Operation.error][google.longrunning.Operation.error] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class SourceGcsBucket(proto.Message):
    r"""Cloud Storage as the source of a data transfer.

    Attributes:
        uri (str):
            Required. URI to a Cloud Storage bucket in the format:
            ``gs://<bucket_name>/<path_inside_bucket>``. The path inside
            the bucket is optional.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DestinationGcsBucket(proto.Message):
    r"""Cloud Storage as the destination of a data transfer.

    Attributes:
        uri (str):
            Required. URI to a Cloud Storage bucket in the format:
            ``gs://<bucket_name>/<path_inside_bucket>``. The path inside
            the bucket is optional.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SourceParallelstore(proto.Message):
    r"""Parallelstore as the source of a data transfer.

    Attributes:
        path (str):
            Optional. Root directory path to the Paralellstore
            filesystem, starting with ``/``. Defaults to ``/`` if unset.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DestinationParallelstore(proto.Message):
    r"""Parallelstore as the destination of a data transfer.

    Attributes:
        path (str):
            Optional. Root directory path to the Paralellstore
            filesystem, starting with ``/``. Defaults to ``/`` if unset.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportDataRequest(proto.Message):
    r"""Import data from Cloud Storage into a Parallelstore instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_gcs_bucket (google.cloud.parallelstore_v1.types.SourceGcsBucket):
            The Cloud Storage source bucket and,
            optionally, path inside the bucket.

            This field is a member of `oneof`_ ``source``.
        destination_parallelstore (google.cloud.parallelstore_v1.types.DestinationParallelstore):
            Parallelstore destination.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        service_account (str):
            Optional. User-specified service account credentials to be
            used when performing the transfer.

            Use one of the following formats:

            - ``{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/{PROJECT_ID_OR_NUMBER}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``

            If unspecified, the Parallelstore service agent is used:
            ``service-<PROJECT_NUMBER>@gcp-sa-parallelstore.iam.gserviceaccount.com``
        metadata_options (google.cloud.parallelstore_v1.types.TransferMetadataOptions):
            Optional. The transfer metadata options for
            the import data.
    """

    source_gcs_bucket: "SourceGcsBucket" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="SourceGcsBucket",
    )
    destination_parallelstore: "DestinationParallelstore" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination",
        message="DestinationParallelstore",
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
    metadata_options: "TransferMetadataOptions" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="TransferMetadataOptions",
    )


class ExportDataRequest(proto.Message):
    r"""Export data from Parallelstore to Cloud Storage.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_parallelstore (google.cloud.parallelstore_v1.types.SourceParallelstore):
            Parallelstore source.

            This field is a member of `oneof`_ ``source``.
        destination_gcs_bucket (google.cloud.parallelstore_v1.types.DestinationGcsBucket):
            Cloud Storage destination.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        service_account (str):
            Optional. User-specified Service Account (SA) credentials to
            be used when performing the transfer. Use one of the
            following formats:

            - ``{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/{PROJECT_ID_OR_NUMBER}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``
            - ``projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}``

            If unspecified, the Parallelstore service agent is used:
            ``service-<PROJECT_NUMBER>@gcp-sa-parallelstore.iam.gserviceaccount.com``
        metadata_options (google.cloud.parallelstore_v1.types.TransferMetadataOptions):
            Optional. The metadata options for the export
            data.
    """

    source_parallelstore: "SourceParallelstore" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="SourceParallelstore",
    )
    destination_gcs_bucket: "DestinationGcsBucket" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination",
        message="DestinationGcsBucket",
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
    metadata_options: "TransferMetadataOptions" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="TransferMetadataOptions",
    )


class ImportDataResponse(proto.Message):
    r"""The response to a request to import data to Parallelstore."""


class TransferErrorLogEntry(proto.Message):
    r"""An entry describing an error that has occurred.

    Attributes:
        uri (str):
            A URL that refers to the target (a data
            source, a data sink, or an object) with which
            the error is associated.
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


class TransferErrorSummary(proto.Message):
    r"""A summary of errors by error code, plus a count and sample
    error log entries.

    Attributes:
        error_code (google.rpc.code_pb2.Code):
            One of the error codes that caused the
            transfer failure.
        error_count (int):
            Count of this type of error.
        error_log_entries (MutableSequence[google.cloud.parallelstore_v1.types.TransferErrorLogEntry]):
            A list of messages that carry the error
            details.
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
    error_log_entries: MutableSequence["TransferErrorLogEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="TransferErrorLogEntry",
    )


class ImportDataMetadata(proto.Message):
    r"""Metadata related to the data import operation.

    Attributes:
        operation_metadata (google.cloud.parallelstore_v1.types.TransferOperationMetadata):
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
            [Operation.error][google.longrunning.Operation.error] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
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


class ExportDataResponse(proto.Message):
    r"""The response to a request to export data from Parallelstore."""


class ExportDataMetadata(proto.Message):
    r"""Metadata related to the data export operation.

    Attributes:
        operation_metadata (google.cloud.parallelstore_v1.types.TransferOperationMetadata):
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
            [Operation.error][google.longrunning.Operation.error] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
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


class TransferOperationMetadata(proto.Message):
    r"""Long-running operation metadata related to a data transfer.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_parallelstore (google.cloud.parallelstore_v1.types.SourceParallelstore):
            Output only. Parallelstore source.

            This field is a member of `oneof`_ ``source``.
        source_gcs_bucket (google.cloud.parallelstore_v1.types.SourceGcsBucket):
            Output only. Cloud Storage source.

            This field is a member of `oneof`_ ``source``.
        destination_gcs_bucket (google.cloud.parallelstore_v1.types.DestinationGcsBucket):
            Output only. Cloud Storage destination.

            This field is a member of `oneof`_ ``destination``.
        destination_parallelstore (google.cloud.parallelstore_v1.types.DestinationParallelstore):
            Output only. Parallelstore destination.

            This field is a member of `oneof`_ ``destination``.
        counters (google.cloud.parallelstore_v1.types.TransferCounters):
            Output only. The progress of the transfer
            operation.
        transfer_type (google.cloud.parallelstore_v1.types.TransferType):
            Output only. The type of transfer occurring.
        error_summary (MutableSequence[google.cloud.parallelstore_v1.types.TransferErrorSummary]):
            Output only. List of files that failed to be
            transferred. This list will have a maximum size
            of 5 elements.
    """

    source_parallelstore: "SourceParallelstore" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="source",
        message="SourceParallelstore",
    )
    source_gcs_bucket: "SourceGcsBucket" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="source",
        message="SourceGcsBucket",
    )
    destination_gcs_bucket: "DestinationGcsBucket" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="destination",
        message="DestinationGcsBucket",
    )
    destination_parallelstore: "DestinationParallelstore" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="destination",
        message="DestinationParallelstore",
    )
    counters: "TransferCounters" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TransferCounters",
    )
    transfer_type: "TransferType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="TransferType",
    )
    error_summary: MutableSequence["TransferErrorSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="TransferErrorSummary",
    )


class TransferCounters(proto.Message):
    r"""A collection of counters that report the progress of a
    transfer operation.

    Attributes:
        objects_found (int):
            Objects found in the data source that are
            scheduled to be transferred, excluding any that
            are filtered based on object conditions or
            skipped due to sync.
        bytes_found (int):
            Bytes found in the data source that are
            scheduled to be transferred, excluding any that
            are filtered based on object conditions or
            skipped due to sync.
        objects_skipped (int):
            Objects in the data source that are not
            transferred because they already exist in the
            data destination.
        bytes_skipped (int):
            Bytes in the data source that are not
            transferred because they already exist in the
            data destination.
        objects_copied (int):
            Objects that are copied to the data
            destination.
        bytes_copied (int):
            Bytes that are copied to the data
            destination.
        objects_failed (int):
            Objects that failed to be written to the data
            destination.
        bytes_failed (int):
            Bytes that failed to be written to the data
            destination.
    """

    objects_found: int = proto.Field(
        proto.INT64,
        number=1,
    )
    bytes_found: int = proto.Field(
        proto.INT64,
        number=2,
    )
    objects_skipped: int = proto.Field(
        proto.INT64,
        number=3,
    )
    bytes_skipped: int = proto.Field(
        proto.INT64,
        number=4,
    )
    objects_copied: int = proto.Field(
        proto.INT64,
        number=5,
    )
    bytes_copied: int = proto.Field(
        proto.INT64,
        number=6,
    )
    objects_failed: int = proto.Field(
        proto.INT64,
        number=7,
    )
    bytes_failed: int = proto.Field(
        proto.INT64,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
