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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.code_pb2 as code_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.storagebatchoperations.v1',
    manifest={
        'Job',
        'BucketOperation',
        'BucketList',
        'Manifest',
        'PrefixList',
        'PutObjectHold',
        'DeleteObject',
        'RewriteObject',
        'ObjectRetention',
        'PutMetadata',
        'ObjectCustomContextPayload',
        'CustomContextUpdates',
        'UpdateObjectCustomContext',
        'ErrorSummary',
        'ErrorLogEntry',
        'Counters',
        'LoggingConfig',
    },
)


class Job(proto.Message):
    r"""The Storage Batch Operations Job description.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the Job. job_id is unique
            within the project, that is either set by the customer or
            defined by the service. Format:
            projects/{project}/locations/global/jobs/{job_id} . For
            example: "projects/123456/locations/global/jobs/job01".
        description (str):
            Optional. A description provided by the user
            for the job. Its max length is 1024 bytes when
            Unicode-encoded.
        bucket_list (google.cloud.storagebatchoperations_v1.types.BucketList):
            Specifies a list of buckets and their objects
            to be transformed.

            This field is a member of `oneof`_ ``source``.
        put_object_hold (google.cloud.storagebatchoperations_v1.types.PutObjectHold):
            Changes object hold status.

            This field is a member of `oneof`_ ``transformation``.
        delete_object (google.cloud.storagebatchoperations_v1.types.DeleteObject):
            Delete objects.

            This field is a member of `oneof`_ ``transformation``.
        put_metadata (google.cloud.storagebatchoperations_v1.types.PutMetadata):
            Updates object metadata. Allows updating
            fixed-key and custom metadata and fixed-key
            metadata i.e. Cache-Control,
            Content-Disposition, Content-Encoding,
            Content-Language, Content-Type, Custom-Time.

            This field is a member of `oneof`_ ``transformation``.
        rewrite_object (google.cloud.storagebatchoperations_v1.types.RewriteObject):
            Rewrite the object and updates metadata like
            KMS key.

            This field is a member of `oneof`_ ``transformation``.
        update_object_custom_context (google.cloud.storagebatchoperations_v1.types.UpdateObjectCustomContext):
            Update object custom context.

            This field is a member of `oneof`_ ``transformation``.
        logging_config (google.cloud.storagebatchoperations_v1.types.LoggingConfig):
            Optional. Logging configuration.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the job was
            created.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the job was
            scheduled.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the job was
            completed.
        counters (google.cloud.storagebatchoperations_v1.types.Counters):
            Output only. Information about the progress
            of the job.
        error_summaries (MutableSequence[google.cloud.storagebatchoperations_v1.types.ErrorSummary]):
            Output only. Summarizes errors encountered
            with sample error log entries.
        state (google.cloud.storagebatchoperations_v1.types.Job.State):
            Output only. State of the job.
        dry_run (bool):
            Optional. If true, the job will run in dry
            run mode, returning the total object count and,
            if the object configuration is a prefix list,
            the bytes found from source. No transformations
            will be performed.
        is_multi_bucket_job (bool):
            Output only. If true, this Job operates on
            multiple buckets. Multibucket jobs are subject
            to different quota limits than single-bucket
            jobs.
    """
    class State(proto.Enum):
        r"""Describes state of a job.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            RUNNING (1):
                In progress.
            SUCCEEDED (2):
                Completed successfully.
            CANCELED (3):
                Cancelled by the user.
            FAILED (4):
                Terminated due to an unrecoverable failure.
            QUEUED (5):
                Queued but not yet started.
        """
        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        CANCELED = 3
        FAILED = 4
        QUEUED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    bucket_list: 'BucketList' = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof='source',
        message='BucketList',
    )
    put_object_hold: 'PutObjectHold' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='transformation',
        message='PutObjectHold',
    )
    delete_object: 'DeleteObject' = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='transformation',
        message='DeleteObject',
    )
    put_metadata: 'PutMetadata' = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof='transformation',
        message='PutMetadata',
    )
    rewrite_object: 'RewriteObject' = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof='transformation',
        message='RewriteObject',
    )
    update_object_custom_context: 'UpdateObjectCustomContext' = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof='transformation',
        message='UpdateObjectCustomContext',
    )
    logging_config: 'LoggingConfig' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='LoggingConfig',
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    counters: 'Counters' = proto.Field(
        proto.MESSAGE,
        number=13,
        message='Counters',
    )
    error_summaries: MutableSequence['ErrorSummary'] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message='ErrorSummary',
    )
    state: State = proto.Field(
        proto.ENUM,
        number=15,
        enum=State,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    is_multi_bucket_job: bool = proto.Field(
        proto.BOOL,
        number=24,
    )


class BucketOperation(proto.Message):
    r"""BucketOperation represents a bucket-level breakdown of a Job.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the BucketOperation. This
            is defined by the service. Format:
            projects/{project}/locations/global/jobs/{job_id}/bucketOperations/{bucket_operation}.
        bucket_name (str):
            The bucket name of the objects to be
            transformed in the BucketOperation.
        prefix_list (google.cloud.storagebatchoperations_v1.types.PrefixList):
            Specifies objects matching a prefix set.

            This field is a member of `oneof`_ ``object_configuration``.
        manifest (google.cloud.storagebatchoperations_v1.types.Manifest):
            Specifies objects in a manifest file.

            This field is a member of `oneof`_ ``object_configuration``.
        put_object_hold (google.cloud.storagebatchoperations_v1.types.PutObjectHold):
            Changes object hold status.

            This field is a member of `oneof`_ ``transformation``.
        delete_object (google.cloud.storagebatchoperations_v1.types.DeleteObject):
            Delete objects.

            This field is a member of `oneof`_ ``transformation``.
        put_metadata (google.cloud.storagebatchoperations_v1.types.PutMetadata):
            Updates object metadata. Allows updating
            fixed-key and custom metadata and fixed-key
            metadata i.e. Cache-Control,
            Content-Disposition, Content-Encoding,
            Content-Language, Content-Type, Custom-Time.

            This field is a member of `oneof`_ ``transformation``.
        rewrite_object (google.cloud.storagebatchoperations_v1.types.RewriteObject):
            Rewrite the object and updates metadata like
            KMS key.

            This field is a member of `oneof`_ ``transformation``.
        update_object_custom_context (google.cloud.storagebatchoperations_v1.types.UpdateObjectCustomContext):
            Update object custom context.

            This field is a member of `oneof`_ ``transformation``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the
            BucketOperation was created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the
            BucketOperation was started.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the
            BucketOperation was completed.
        counters (google.cloud.storagebatchoperations_v1.types.Counters):
            Output only. Information about the progress
            of the bucket operation.
        error_summaries (MutableSequence[google.cloud.storagebatchoperations_v1.types.ErrorSummary]):
            Output only. Summarizes errors encountered
            with sample error log entries.
        state (google.cloud.storagebatchoperations_v1.types.BucketOperation.State):
            Output only. State of the BucketOperation.
    """
    class State(proto.Enum):
        r"""Describes state of the BucketOperation.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            QUEUED (1):
                Created but not yet started.
            RUNNING (2):
                In progress.
            SUCCEEDED (3):
                Completed successfully.
            CANCELED (4):
                Cancelled by the user.
            FAILED (5):
                Terminated due to an unrecoverable failure.
        """
        STATE_UNSPECIFIED = 0
        QUEUED = 1
        RUNNING = 2
        SUCCEEDED = 3
        CANCELED = 4
        FAILED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    prefix_list: 'PrefixList' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='object_configuration',
        message='PrefixList',
    )
    manifest: 'Manifest' = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='object_configuration',
        message='Manifest',
    )
    put_object_hold: 'PutObjectHold' = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof='transformation',
        message='PutObjectHold',
    )
    delete_object: 'DeleteObject' = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof='transformation',
        message='DeleteObject',
    )
    put_metadata: 'PutMetadata' = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof='transformation',
        message='PutMetadata',
    )
    rewrite_object: 'RewriteObject' = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof='transformation',
        message='RewriteObject',
    )
    update_object_custom_context: 'UpdateObjectCustomContext' = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof='transformation',
        message='UpdateObjectCustomContext',
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    counters: 'Counters' = proto.Field(
        proto.MESSAGE,
        number=8,
        message='Counters',
    )
    error_summaries: MutableSequence['ErrorSummary'] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message='ErrorSummary',
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )


class BucketList(proto.Message):
    r"""Describes list of buckets and their objects to be
    transformed.

    Attributes:
        buckets (MutableSequence[google.cloud.storagebatchoperations_v1.types.BucketList.Bucket]):
            Required. List of buckets and their objects
            to be transformed. Currently, only one bucket
            configuration is supported. If multiple buckets
            are specified, an error will be returned.
    """

    class Bucket(proto.Message):
        r"""Describes configuration of a single bucket and its objects to
        be transformed.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            bucket (str):
                Required. Bucket name for the objects to be
                transformed.
            prefix_list (google.cloud.storagebatchoperations_v1.types.PrefixList):
                Specifies objects matching a prefix set.

                This field is a member of `oneof`_ ``object_configuration``.
            manifest (google.cloud.storagebatchoperations_v1.types.Manifest):
                Specifies objects in a manifest file.

                This field is a member of `oneof`_ ``object_configuration``.
        """

        bucket: str = proto.Field(
            proto.STRING,
            number=1,
        )
        prefix_list: 'PrefixList' = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof='object_configuration',
            message='PrefixList',
        )
        manifest: 'Manifest' = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof='object_configuration',
            message='Manifest',
        )

    buckets: MutableSequence[Bucket] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Bucket,
    )


class Manifest(proto.Message):
    r"""Describes list of objects to be transformed.

    Attributes:
        manifest_location (str):
            Required. ``manifest_location`` must contain the manifest
            source file that is a CSV file in a Google Cloud Storage
            bucket. Each row in the file must include the object details
            i.e. BucketId and Name. Generation may optionally be
            specified. When it is not specified the live object is acted
            upon. ``manifest_location`` should either be 1) An absolute
            path to the object in the format of
            ``gs://bucket_name/path/file_name.csv``. 2) An absolute path
            with a single wildcard character in the file name, for
            example ``gs://bucket_name/path/file_name*.csv``. If
            manifest location is specified with a wildcard, objects in
            all manifest files matching the pattern will be acted upon.
    """

    manifest_location: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PrefixList(proto.Message):
    r"""Describes prefixes of objects to be transformed.

    Attributes:
        included_object_prefixes (MutableSequence[str]):
            Optional. Include prefixes of the objects to be transformed.

            - Supports full object name
            - Supports prefix of the object name
            - Wildcards are not supported
            - Supports empty string for all objects in a bucket.
    """

    included_object_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class PutObjectHold(proto.Message):
    r"""Describes options to update object hold.

    Attributes:
        temporary_hold (google.cloud.storagebatchoperations_v1.types.PutObjectHold.HoldStatus):
            Required. Updates object temporary holds
            state. When object temporary hold is set, object
            cannot be deleted or replaced.
        event_based_hold (google.cloud.storagebatchoperations_v1.types.PutObjectHold.HoldStatus):
            Required. Updates object event based holds
            state. When object event based hold is set,
            object cannot be deleted or replaced. Resets
            object's time in the bucket for the purposes of
            the retention period.
    """
    class HoldStatus(proto.Enum):
        r"""Describes the status of the hold.

        Values:
            HOLD_STATUS_UNSPECIFIED (0):
                Default value, Object hold status will not be
                changed.
            SET (1):
                Places the hold.
            UNSET (2):
                Releases the hold.
        """
        HOLD_STATUS_UNSPECIFIED = 0
        SET = 1
        UNSET = 2

    temporary_hold: HoldStatus = proto.Field(
        proto.ENUM,
        number=1,
        enum=HoldStatus,
    )
    event_based_hold: HoldStatus = proto.Field(
        proto.ENUM,
        number=2,
        enum=HoldStatus,
    )


class DeleteObject(proto.Message):
    r"""Describes options to delete an object.

    Attributes:
        permanent_object_deletion_enabled (bool):
            Required. Controls deletion behavior when
            versioning is enabled for the object's bucket.
            If true both live and noncurrent objects will be
            permanently deleted. Otherwise live objects in
            versioned buckets will become noncurrent and
            objects that were already noncurrent will be
            skipped. This setting doesn't have any impact on
            the Soft Delete feature. All objects deleted by
            this service can be be restored for the duration
            of the Soft Delete retention duration if
            enabled. If enabled and the manifest doesn't
            specify an object's generation, a
            GetObjectMetadata call (a Class B operation)
            will be made to determine the live object
            generation.
    """

    permanent_object_deletion_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class RewriteObject(proto.Message):
    r"""Describes options for object rewrite.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kms_key (str):
            Required. Resource name of the Cloud KMS key
            that will be used to encrypt the object. The
            Cloud KMS key must be located in same location
            as the object. Refer to
            https://cloud.google.com/storage/docs/encryption/using-customer-managed-keys#add-object-key
            for additional documentation. Format:

            projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}
            For example:

            "projects/123456/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key".
            The object will be rewritten and set with the
            specified KMS key.

            This field is a member of `oneof`_ ``_kms_key``.
    """

    kms_key: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class ObjectRetention(proto.Message):
    r"""Describes options for object retention update.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        retain_until_time (str):
            Required. The time when the object will be
            retained until. UNSET will clear the retention.
            Must be specified in RFC 3339 format e.g.
            YYYY-MM-DD'T'HH:MM:SS.SS'Z' or
            YYYY-MM-DD'T'HH:MM:SS'Z'.

            This field is a member of `oneof`_ ``_retain_until_time``.
        retention_mode (google.cloud.storagebatchoperations_v1.types.ObjectRetention.RetentionMode):
            Required. The retention mode of the object.

            This field is a member of `oneof`_ ``_retention_mode``.
    """
    class RetentionMode(proto.Enum):
        r"""Describes the retention mode.

        Values:
            RETENTION_MODE_UNSPECIFIED (0):
                If set and retain_until_time is empty, clears the retention.
            LOCKED (1):
                Sets the retention mode to locked.
            UNLOCKED (2):
                Sets the retention mode to unlocked.
        """
        RETENTION_MODE_UNSPECIFIED = 0
        LOCKED = 1
        UNLOCKED = 2

    retain_until_time: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    retention_mode: RetentionMode = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=RetentionMode,
    )


class PutMetadata(proto.Message):
    r"""Describes options for object metadata update.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        content_disposition (str):
            Optional. Updates objects Content-Disposition
            fixed metadata. Unset values will be ignored.
            Set empty values to clear the metadata. Refer
            https://cloud.google.com/storage/docs/metadata#content-disposition
            for additional documentation.

            This field is a member of `oneof`_ ``_content_disposition``.
        content_encoding (str):
            Optional. Updates objects Content-Encoding
            fixed metadata. Unset values will be ignored.
            Set empty values to clear the metadata. Refer to
            documentation in
            https://cloud.google.com/storage/docs/metadata#content-encoding.

            This field is a member of `oneof`_ ``_content_encoding``.
        content_language (str):
            Optional. Updates objects Content-Language
            fixed metadata. Refer to ISO 639-1 language
            codes for typical values of this metadata. Max
            length 100 characters. Unset values will be
            ignored. Set empty values to clear the metadata.
            Refer to documentation in
            https://cloud.google.com/storage/docs/metadata#content-language.

            This field is a member of `oneof`_ ``_content_language``.
        content_type (str):
            Optional. Updates objects Content-Type fixed
            metadata. Unset values will be ignored. Set
            empty values to clear the metadata. Refer to
            documentation in
            https://cloud.google.com/storage/docs/metadata#content-type

            This field is a member of `oneof`_ ``_content_type``.
        cache_control (str):
            Optional. Updates objects Cache-Control fixed metadata.
            Unset values will be ignored. Set empty values to clear the
            metadata. Additionally, the value for Custom-Time cannot
            decrease. Refer to documentation in
            https://cloud.google.com/storage/docs/metadata#caching_data.

            This field is a member of `oneof`_ ``_cache_control``.
        custom_time (str):
            Optional. Updates objects Custom-Time fixed
            metadata. Unset values will be ignored. Set
            empty values to clear the metadata. Refer to
            documentation in
            https://cloud.google.com/storage/docs/metadata#custom-time.

            This field is a member of `oneof`_ ``_custom_time``.
        custom_metadata (MutableMapping[str, str]):
            Optional. Updates objects custom metadata.
            Adds or sets individual custom metadata key
            value pairs on objects. Keys that are set with
            empty custom metadata values will have its value
            cleared. Existing custom metadata not specified
            with this flag is not changed. Refer to
            documentation in
            https://cloud.google.com/storage/docs/metadata#custom-metadata
        object_retention (google.cloud.storagebatchoperations_v1.types.ObjectRetention):
            Optional. Updates objects retention lock configuration.
            Unset values will be ignored. Set empty values to clear the
            retention for the object with existing ``Unlocked``
            retention mode. Object with existing ``Locked`` retention
            mode cannot be cleared or reduce retain_until_time. Refer to
            documentation in
            https://cloud.google.com/storage/docs/object-lock

            This field is a member of `oneof`_ ``_object_retention``.
    """

    content_disposition: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    content_encoding: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    content_language: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    content_type: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    cache_control: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    custom_time: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    custom_metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    object_retention: 'ObjectRetention' = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message='ObjectRetention',
    )


class ObjectCustomContextPayload(proto.Message):
    r"""Describes the payload of a user defined object custom
    context.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            The value of the object custom context. If set, ``value``
            must NOT be an empty string since it is a required field in
            custom context. If unset, ``value`` will be ignored and no
            changes will be made to the ``value`` field of the custom
            context payload.

            This field is a member of `oneof`_ ``_value``.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class CustomContextUpdates(proto.Message):
    r"""Describes a collection of updates to apply to custom contexts
    identified by key.

    Attributes:
        updates (MutableMapping[str, google.cloud.storagebatchoperations_v1.types.ObjectCustomContextPayload]):
            Optional. Insert or update the existing
            custom contexts.
        keys_to_clear (MutableSequence[str]):
            Optional. Custom contexts to clear by key. A key cannot be
            present in both ``updates`` and ``keys_to_clear``.
    """

    updates: MutableMapping[str, 'ObjectCustomContextPayload'] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message='ObjectCustomContextPayload',
    )
    keys_to_clear: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class UpdateObjectCustomContext(proto.Message):
    r"""Describes options to update object custom contexts.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        custom_context_updates (google.cloud.storagebatchoperations_v1.types.CustomContextUpdates):
            A collection of updates to apply to specific
            custom contexts. Use this to add, update or
            delete individual contexts by key.

            This field is a member of `oneof`_ ``action``.
        clear_all (bool):
            If set, must be set to true and all existing
            object custom contexts will be deleted.

            This field is a member of `oneof`_ ``action``.
    """

    custom_context_updates: 'CustomContextUpdates' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='action',
        message='CustomContextUpdates',
    )
    clear_all: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof='action',
    )


class ErrorSummary(proto.Message):
    r"""A summary of errors by error code, plus a count and sample
    error log entries.

    Attributes:
        error_code (google.rpc.code_pb2.Code):
            Required. The canonical error code.
        error_count (int):
            Required. Number of errors encountered per ``error_code``.
        error_log_entries (MutableSequence[google.cloud.storagebatchoperations_v1.types.ErrorLogEntry]):
            Required. Sample error logs.
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
    error_log_entries: MutableSequence['ErrorLogEntry'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='ErrorLogEntry',
    )


class ErrorLogEntry(proto.Message):
    r"""An entry describing an error that has occurred.

    Attributes:
        object_uri (str):
            Required. Output only. Object URL. e.g.
            gs://my_bucket/object.txt
        error_details (MutableSequence[str]):
            Optional. Output only. At most 5 error log
            entries are recorded for a given error code for
            a job.
    """

    object_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_details: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class Counters(proto.Message):
    r"""Describes details about the progress of the job.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        total_object_count (int):
            Output only. Number of objects listed.
        succeeded_object_count (int):
            Output only. Number of objects completed.
        failed_object_count (int):
            Output only. The number of objects that
            failed due to user errors or service errors.
        total_bytes_found (int):
            Output only. Number of bytes found from
            source. This field is only populated for jobs
            with a prefix list object configuration.

            This field is a member of `oneof`_ ``_total_bytes_found``.
        object_custom_contexts_created (int):
            Output only. Number of object custom contexts
            created. This field is only populated for jobs
            with the UpdateObjectCustomContext
            transformation.

            This field is a member of `oneof`_ ``_object_custom_contexts_created``.
        object_custom_contexts_deleted (int):
            Output only. Number of object custom contexts
            deleted. This field is only populated for jobs
            with the UpdateObjectCustomContext
            transformation.

            This field is a member of `oneof`_ ``_object_custom_contexts_deleted``.
        object_custom_contexts_updated (int):
            Output only. Number of object custom contexts
            updated. This counter tracks custom contexts
            where the key already existed, but the payload
            was modified. This field is only populated for
            jobs with the UpdateObjectCustomContext
            transformation.

            This field is a member of `oneof`_ ``_object_custom_contexts_updated``.
    """

    total_object_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    succeeded_object_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    failed_object_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    total_bytes_found: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    object_custom_contexts_created: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    object_custom_contexts_deleted: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    object_custom_contexts_updated: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )


class LoggingConfig(proto.Message):
    r"""Specifies the Cloud Logging behavior.

    Attributes:
        log_actions (MutableSequence[google.cloud.storagebatchoperations_v1.types.LoggingConfig.LoggableAction]):
            Required. Specifies the actions to be logged.
        log_action_states (MutableSequence[google.cloud.storagebatchoperations_v1.types.LoggingConfig.LoggableActionState]):
            Required. States in which Action are
            logged.If empty, no logs are generated.
    """
    class LoggableAction(proto.Enum):
        r"""Loggable actions types.

        Values:
            LOGGABLE_ACTION_UNSPECIFIED (0):
                Illegal value, to avoid allowing a default.
            TRANSFORM (6):
                The corresponding transform action in this
                job.
        """
        LOGGABLE_ACTION_UNSPECIFIED = 0
        TRANSFORM = 6

    class LoggableActionState(proto.Enum):
        r"""Loggable action states filter.

        Values:
            LOGGABLE_ACTION_STATE_UNSPECIFIED (0):
                Illegal value, to avoid allowing a default.
            SUCCEEDED (1):
                ``LoggableAction`` completed successfully. ``SUCCEEDED``
                actions are logged as
                [INFO][google.logging.type.LogSeverity.INFO].
            FAILED (2):
                ``LoggableAction`` terminated in an error state. ``FAILED``
                actions are logged as
                [ERROR][google.logging.type.LogSeverity.ERROR].
        """
        LOGGABLE_ACTION_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    log_actions: MutableSequence[LoggableAction] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=LoggableAction,
    )
    log_action_states: MutableSequence[LoggableActionState] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=LoggableActionState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
