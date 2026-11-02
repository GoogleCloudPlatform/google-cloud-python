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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.datatransfer.v1",
    manifest={
        "TransferType",
        "TransferState",
        "EmailPreferences",
        "ScheduleOptions",
        "ScheduleOptionsV2",
        "TimeBasedSchedule",
        "ManualSchedule",
        "EventDrivenSchedule",
        "UserInfo",
        "TransferConfig",
        "EncryptionConfiguration",
        "TransferRun",
        "TransferMessage",
    },
)


class TransferType(proto.Enum):
    r"""DEPRECATED. Represents data transfer type.

    Values:
        TRANSFER_TYPE_UNSPECIFIED (0):
            Invalid or Unknown transfer type placeholder.
        BATCH (1):
            Batch data transfer.
        STREAMING (2):
            Streaming data transfer. Streaming data
            source currently doesn't support multiple
            transfer configs per project.
    """

    _pb_options = {"deprecated": True}
    TRANSFER_TYPE_UNSPECIFIED = 0
    BATCH = 1
    STREAMING = 2


class TransferState(proto.Enum):
    r"""Represents data transfer run state.

    Values:
        TRANSFER_STATE_UNSPECIFIED (0):
            State placeholder (0).
        PENDING (2):
            Data transfer is scheduled and is waiting to
            be picked up by data transfer backend (2).
        RUNNING (3):
            Data transfer is in progress (3).
        SUCCEEDED (4):
            Data transfer completed successfully (4).
        FAILED (5):
            Data transfer failed (5).
        CANCELLED (6):
            Data transfer is cancelled (6).
    """

    TRANSFER_STATE_UNSPECIFIED = 0
    PENDING = 2
    RUNNING = 3
    SUCCEEDED = 4
    FAILED = 5
    CANCELLED = 6


class EmailPreferences(proto.Message):
    r"""Represents preferences for sending email notifications for
    transfer run events.

    Attributes:
        enable_failure_email (bool):
            If true, email notifications will be sent on
            transfer run failures.
    """

    enable_failure_email: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ScheduleOptions(proto.Message):
    r"""Options customizing the data transfer schedule.

    Attributes:
        disable_auto_scheduling (bool):
            If true, automatic scheduling of data
            transfer runs for this configuration will be
            disabled. The runs can be started on ad-hoc
            basis using StartManualTransferRuns API. When
            automatic scheduling is disabled, the
            TransferConfig.schedule field will be ignored.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Specifies time to start scheduling transfer
            runs. The first run will be scheduled at or
            after the start time according to a recurrence
            pattern defined in the schedule string. The
            start time can be changed at any moment. The
            time when a data transfer can be triggered
            manually is not limited by this option.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Defines time to stop scheduling transfer
            runs. A transfer run cannot be scheduled at or
            after the end time. The end time can be changed
            at any moment. The time when a data transfer can
            be triggered manually is not limited by this
            option.
    """

    disable_auto_scheduling: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ScheduleOptionsV2(proto.Message):
    r"""V2 options customizing different types of data transfer
    schedule. This field supports existing time-based and manual
    transfer schedule. Also supports Event-Driven transfer schedule.
    ScheduleOptionsV2 cannot be used together with
    ScheduleOptions/Schedule.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        time_based_schedule (google.cloud.bigquery_datatransfer_v1.types.TimeBasedSchedule):
            Time based transfer schedule options. This is
            the default schedule option.

            This field is a member of `oneof`_ ``schedule``.
        manual_schedule (google.cloud.bigquery_datatransfer_v1.types.ManualSchedule):
            Manual transfer schedule. If set, the transfer run will not
            be auto-scheduled by the system, unless the client invokes
            StartManualTransferRuns. This is equivalent to
            disable_auto_scheduling = true.

            This field is a member of `oneof`_ ``schedule``.
        event_driven_schedule (google.cloud.bigquery_datatransfer_v1.types.EventDrivenSchedule):
            Event driven transfer schedule options. If
            set, the transfer will be scheduled upon events
            arrial.

            This field is a member of `oneof`_ ``schedule``.
    """

    time_based_schedule: "TimeBasedSchedule" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="schedule",
        message="TimeBasedSchedule",
    )
    manual_schedule: "ManualSchedule" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="schedule",
        message="ManualSchedule",
    )
    event_driven_schedule: "EventDrivenSchedule" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="schedule",
        message="EventDrivenSchedule",
    )


class TimeBasedSchedule(proto.Message):
    r"""Options customizing the time based transfer schedule.
    Options are migrated from the original ScheduleOptions message.

    Attributes:
        schedule (str):
            Data transfer schedule. If the data source does not support
            a custom schedule, this should be empty. If it is empty, the
            default value for the data source will be used. The
            specified times are in UTC. Examples of valid format:
            ``1st,3rd monday of month 15:30``,
            ``every wed,fri of jan,jun 13:15``, and
            ``first sunday of quarter 00:00``. See more explanation
            about the format here:
            https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format

            NOTE: The minimum interval time between recurring transfers
            depends on the data source; refer to the documentation for
            your data source.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Specifies time to start scheduling transfer
            runs. The first run will be scheduled at or
            after the start time according to a recurrence
            pattern defined in the schedule string. The
            start time can be changed at any moment.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Defines time to stop scheduling transfer
            runs. A transfer run cannot be scheduled at or
            after the end time. The end time can be changed
            at any moment.
    """

    schedule: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class ManualSchedule(proto.Message):
    r"""Options customizing manual transfers schedule."""


class EventDrivenSchedule(proto.Message):
    r"""Options customizing EventDriven transfers schedule.

    Attributes:
        pubsub_subscription (str):
            Pub/Sub subscription name used to receive
            events. Only Google Cloud Storage data source
            support this option. Format:
            projects/{project}/subscriptions/{subscription}
    """

    pubsub_subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UserInfo(proto.Message):
    r"""Information about a user.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        email (str):
            E-mail address of the user.

            This field is a member of `oneof`_ ``_email``.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class TransferConfig(proto.Message):
    r"""Represents a data transfer configuration. A transfer configuration
    contains all metadata needed to perform a data transfer. For
    example, ``destination_dataset_id`` specifies where data should be
    stored. When a new transfer configuration is created, the specified
    ``destination_dataset_id`` is created when needed and shared with
    the appropriate data source service account.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the transfer config.
            Transfer config names have the form either
            ``projects/{project_id}/locations/{region}/transferConfigs/{config_id}``
            or ``projects/{project_id}/transferConfigs/{config_id}``,
            where ``config_id`` is usually a UUID, even though it is not
            guaranteed or required. The name is ignored when creating a
            transfer config.
        destination_dataset_id (str):
            The BigQuery target dataset id.

            This field is a member of `oneof`_ ``destination``.
        display_name (str):
            User specified display name for the data
            transfer.
        data_source_id (str):
            Data source ID. This cannot be changed once
            data transfer is created. The full list of
            available data source IDs can be returned
            through an API call:

            https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/projects.locations.dataSources/list
        params (google.protobuf.struct_pb2.Struct):
            Parameters specific to each data source. For
            more information see the bq tab in the 'Setting
            up a data transfer' section for each data
            source. For example the parameters for Cloud
            Storage transfers are listed here:

            https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
        schedule (str):
            Data transfer schedule. If the data source does not support
            a custom schedule, this should be empty. If it is empty, the
            default value for the data source will be used. The
            specified times are in UTC. Examples of valid format:
            ``1st,3rd monday of month 15:30``,
            ``every wed,fri of jan,jun 13:15``, and
            ``first sunday of quarter 00:00``. See more explanation
            about the format here:
            https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format

            NOTE: The minimum interval time between recurring transfers
            depends on the data source; refer to the documentation for
            your data source.
        schedule_options (google.cloud.bigquery_datatransfer_v1.types.ScheduleOptions):
            Options customizing the data transfer
            schedule.
        schedule_options_v2 (google.cloud.bigquery_datatransfer_v1.types.ScheduleOptionsV2):
            Options customizing different types of data transfer
            schedule. This field replaces "schedule" and
            "schedule_options" fields. ScheduleOptionsV2 cannot be used
            together with ScheduleOptions/Schedule.
        data_refresh_window_days (int):
            The number of days to look back to automatically refresh the
            data. For example, if ``data_refresh_window_days = 10``,
            then every day BigQuery reingests data for [today-10,
            today-1], rather than ingesting data for just [today-1].
            Only valid if the data source supports the feature. Set the
            value to 0 to use the default value.
        disabled (bool):
            Is this config disabled. When set to true, no
            runs will be scheduled for this transfer config.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Data transfer modification time.
            Ignored by server on input.
        next_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Next time when data transfer
            will run.
        state (google.cloud.bigquery_datatransfer_v1.types.TransferState):
            Output only. State of the most recently
            updated transfer run.
        user_id (int):
            Deprecated. Unique ID of the user on whose
            behalf transfer is done.
        dataset_region (str):
            Output only. Region in which BigQuery dataset
            is located.
        notification_pubsub_topic (str):
            Pub/Sub topic where notifications will be sent after
            transfer runs associated with this transfer config finish.

            The format for specifying a pubsub topic is:
            ``projects/{project_id}/topics/{topic_id}``
        email_preferences (google.cloud.bigquery_datatransfer_v1.types.EmailPreferences):
            Email notifications will be sent according to
            these preferences to the email address of the
            user who owns this transfer config.
        owner_info (google.cloud.bigquery_datatransfer_v1.types.UserInfo):
            Output only. Information about the user whose credentials
            are used to transfer data. Populated only for
            ``transferConfigs.get`` requests. In case the user
            information is not available, this field will not be
            populated.

            This field is a member of `oneof`_ ``_owner_info``.
        encryption_configuration (google.cloud.bigquery_datatransfer_v1.types.EncryptionConfiguration):
            The encryption configuration part. Currently,
            it is only used for the optional KMS key name.
            The BigQuery service account of your project
            must be granted permissions to use the key. Read
            methods will return the key name applied in
            effect. Write methods will apply the key if it
            is present, or otherwise try to apply project
            default keys if it is absent.
        error (google.rpc.status_pb2.Status):
            Output only. Error code with detailed
            information about reason of the latest config
            failure.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="destination",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_source_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    params: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=7,
    )
    schedule_options: "ScheduleOptions" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="ScheduleOptions",
    )
    schedule_options_v2: "ScheduleOptionsV2" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="ScheduleOptionsV2",
    )
    data_refresh_window_days: int = proto.Field(
        proto.INT32,
        number=12,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    next_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    state: "TransferState" = proto.Field(
        proto.ENUM,
        number=10,
        enum="TransferState",
    )
    user_id: int = proto.Field(
        proto.INT64,
        number=11,
    )
    dataset_region: str = proto.Field(
        proto.STRING,
        number=14,
    )
    notification_pubsub_topic: str = proto.Field(
        proto.STRING,
        number=15,
    )
    email_preferences: "EmailPreferences" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="EmailPreferences",
    )
    owner_info: "UserInfo" = proto.Field(
        proto.MESSAGE,
        number=27,
        optional=True,
        message="UserInfo",
    )
    encryption_configuration: "EncryptionConfiguration" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="EncryptionConfiguration",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=32,
        message=status_pb2.Status,
    )


class EncryptionConfiguration(proto.Message):
    r"""Represents the encryption configuration for a transfer.

    Attributes:
        kms_key_name (google.protobuf.wrappers_pb2.StringValue):
            The name of the KMS key used for encrypting
            BigQuery data.
    """

    kms_key_name: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.StringValue,
    )


class TransferRun(proto.Message):
    r"""Represents a data transfer run.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the transfer run. Transfer
            run names have the form
            ``projects/{project_id}/locations/{location}/transferConfigs/{config_id}/runs/{run_id}``.
            The name is ignored when creating a transfer run.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Minimum time after which a transfer run can
            be started.
        run_time (google.protobuf.timestamp_pb2.Timestamp):
            For batch transfer runs, specifies the date
            and time of the data should be ingested.
        error_status (google.rpc.status_pb2.Status):
            Status of the transfer run.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when transfer run was
            started. Parameter ignored by server for input
            requests.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when transfer run ended.
            Parameter ignored by server for input requests.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the data transfer run
            state was updated.
        params (google.protobuf.struct_pb2.Struct):
            Output only. Parameters specific to each data
            source. For more information see the bq tab in
            the 'Setting up a data transfer' section for
            each data source. For example the parameters for
            Cloud Storage transfers are listed here:

            https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
        destination_dataset_id (str):
            Output only. The BigQuery target dataset id.

            This field is a member of `oneof`_ ``destination``.
        data_source_id (str):
            Output only. Data source id.
        state (google.cloud.bigquery_datatransfer_v1.types.TransferState):
            Data transfer run state. Ignored for input
            requests.
        user_id (int):
            Deprecated. Unique ID of the user on whose
            behalf transfer is done.
        schedule (str):
            Output only. Describes the schedule of this transfer run if
            it was created as part of a regular schedule. For batch
            transfer runs that are scheduled manually, this is empty.
            NOTE: the system might choose to delay the schedule
            depending on the current load, so ``schedule_time`` doesn't
            always match this.
        notification_pubsub_topic (str):
            Output only. Pub/Sub topic where a notification will be sent
            after this transfer run finishes.

            The format for specifying a pubsub topic is:
            ``projects/{project_id}/topics/{topic_id}``
        email_preferences (google.cloud.bigquery_datatransfer_v1.types.EmailPreferences):
            Output only. Email notifications will be sent
            according to these preferences to the email
            address of the user who owns the transfer config
            this run was derived from.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    error_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=21,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    params: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    destination_dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="destination",
    )
    data_source_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: "TransferState" = proto.Field(
        proto.ENUM,
        number=8,
        enum="TransferState",
    )
    user_id: int = proto.Field(
        proto.INT64,
        number=11,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=12,
    )
    notification_pubsub_topic: str = proto.Field(
        proto.STRING,
        number=23,
    )
    email_preferences: "EmailPreferences" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="EmailPreferences",
    )


class TransferMessage(proto.Message):
    r"""Represents a user facing message for a particular data
    transfer run.

    Attributes:
        message_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when message was logged.
        severity (google.cloud.bigquery_datatransfer_v1.types.TransferMessage.MessageSeverity):
            Message severity.
        message_text (str):
            Message text.
    """

    class MessageSeverity(proto.Enum):
        r"""Represents data transfer user facing message severity.

        Values:
            MESSAGE_SEVERITY_UNSPECIFIED (0):
                No severity specified.
            INFO (1):
                Informational message.
            WARNING (2):
                Warning message.
            ERROR (3):
                Error message.
        """

        MESSAGE_SEVERITY_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3

    message_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    severity: MessageSeverity = proto.Field(
        proto.ENUM,
        number=2,
        enum=MessageSeverity,
    )
    message_text: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
