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
    package="google.cloud.advisorynotifications.v1",
    manifest={
        "NotificationView",
        "LocalizationState",
        "NotificationType",
        "Notification",
        "Text",
        "Subject",
        "Message",
        "Attachment",
        "Csv",
        "ListNotificationsRequest",
        "ListNotificationsResponse",
        "GetNotificationRequest",
        "Settings",
        "NotificationSettings",
        "GetSettingsRequest",
        "UpdateSettingsRequest",
    },
)


class NotificationView(proto.Enum):
    r"""Notification view.

    Values:
        NOTIFICATION_VIEW_UNSPECIFIED (0):
            Not specified, equivalent to BASIC.
        BASIC (1):
            Server responses only include title, creation
            time and Notification ID. Note: for internal use
            responses also include the last update time, the
            latest message text and whether notification has
            attachments.
        FULL (2):
            Include everything.
    """

    NOTIFICATION_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class LocalizationState(proto.Enum):
    r"""Status of localized text.

    Values:
        LOCALIZATION_STATE_UNSPECIFIED (0):
            Not used.
        LOCALIZATION_STATE_NOT_APPLICABLE (1):
            Localization is not applicable for requested
            language. This can happen when:

            - The requested language was not supported by
              Advisory Notifications at the time of
              localization (including notifications created
              before the localization feature was launched).
            - The requested language is English, so only the
              English text is returned.
        LOCALIZATION_STATE_PENDING (2):
            Localization for requested language is in
            progress, and not ready yet.
        LOCALIZATION_STATE_COMPLETED (3):
            Localization for requested language is
            completed.
    """

    LOCALIZATION_STATE_UNSPECIFIED = 0
    LOCALIZATION_STATE_NOT_APPLICABLE = 1
    LOCALIZATION_STATE_PENDING = 2
    LOCALIZATION_STATE_COMPLETED = 3


class NotificationType(proto.Enum):
    r"""Type of notification

    Values:
        NOTIFICATION_TYPE_UNSPECIFIED (0):
            Default type
        NOTIFICATION_TYPE_SECURITY_PRIVACY_ADVISORY (1):
            Security and privacy advisory notifications
        NOTIFICATION_TYPE_SENSITIVE_ACTIONS (2):
            Sensitive action notifications
        NOTIFICATION_TYPE_SECURITY_MSA (3):
            General security MSA
        NOTIFICATION_TYPE_THREAT_HORIZONS (4):
            Threat horizons MSA
    """

    NOTIFICATION_TYPE_UNSPECIFIED = 0
    NOTIFICATION_TYPE_SECURITY_PRIVACY_ADVISORY = 1
    NOTIFICATION_TYPE_SENSITIVE_ACTIONS = 2
    NOTIFICATION_TYPE_SECURITY_MSA = 3
    NOTIFICATION_TYPE_THREAT_HORIZONS = 4


class Notification(proto.Message):
    r"""A notification object for notifying customers about security
    and privacy issues.

    Attributes:
        name (str):
            The resource name of the notification.
            Format:

            organizations/{organization}/locations/{location}/notifications/{notification}
            or
            projects/{project}/locations/{location}/notifications/{notification}.
        subject (google.cloud.advisorynotifications_v1.types.Subject):
            The subject line of the notification.
        messages (MutableSequence[google.cloud.advisorynotifications_v1.types.Message]):
            A list of messages in the notification.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the notification was
            created.
        notification_type (google.cloud.advisorynotifications_v1.types.NotificationType):
            Type of notification
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: "Subject" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Subject",
    )
    messages: MutableSequence["Message"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Message",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    notification_type: "NotificationType" = proto.Field(
        proto.ENUM,
        number=12,
        enum="NotificationType",
    )


class Text(proto.Message):
    r"""A text object containing the English text and its localized
    copies.

    Attributes:
        en_text (str):
            The English copy.
        localized_text (str):
            The requested localized copy (if applicable).
        localization_state (google.cloud.advisorynotifications_v1.types.LocalizationState):
            Status of the localization.
    """

    en_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    localized_text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    localization_state: "LocalizationState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="LocalizationState",
    )


class Subject(proto.Message):
    r"""A subject line of a notification.

    Attributes:
        text (google.cloud.advisorynotifications_v1.types.Text):
            The text content.
    """

    text: "Text" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Text",
    )


class Message(proto.Message):
    r"""A message which contains notification details.

    Attributes:
        body (google.cloud.advisorynotifications_v1.types.Message.Body):
            The message content.
        attachments (MutableSequence[google.cloud.advisorynotifications_v1.types.Attachment]):
            The attachments to download.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The Message creation timestamp.
        localization_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when Message was localized
    """

    class Body(proto.Message):
        r"""A message body containing text.

        Attributes:
            text (google.cloud.advisorynotifications_v1.types.Text):
                The text content of the message body.
        """

        text: "Text" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Text",
        )

    body: Body = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Body,
    )
    attachments: MutableSequence["Attachment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Attachment",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    localization_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class Attachment(proto.Message):
    r"""Attachment with specific information about the issue.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        csv (google.cloud.advisorynotifications_v1.types.Csv):
            A CSV file attachment. Max size is 10 MB.

            This field is a member of `oneof`_ ``data``.
        display_name (str):
            The title of the attachment.
    """

    csv: "Csv" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message="Csv",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Csv(proto.Message):
    r"""A representation of a CSV file attachment, as a list of
    column headers and a list of data rows.

    Attributes:
        headers (MutableSequence[str]):
            The list of headers for data columns in a CSV
            file.
        data_rows (MutableSequence[google.cloud.advisorynotifications_v1.types.Csv.CsvRow]):
            The list of data rows in a CSV file, as
            string arrays rather than as a single
            comma-separated string.
    """

    class CsvRow(proto.Message):
        r"""A representation of a single data row in a CSV file.

        Attributes:
            entries (MutableSequence[str]):
                The data entries in a CSV file row, as a
                string array rather than a single
                comma-separated string.
        """

        entries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    headers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    data_rows: MutableSequence[CsvRow] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=CsvRow,
    )


class ListNotificationsRequest(proto.Message):
    r"""Request for fetching all notifications for a given parent.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of notifications. Must be of the form
            "organizations/{organization}/locations/{location}"
            or "projects/{project}/locations/{location}".
        page_size (int):
            The maximum number of notifications to
            return. The service may return fewer than this
            value. If unspecified or equal to 0, at most 50
            notifications will be returned. The maximum
            value is 50; values above 50 will be coerced to
            50.
        page_token (str):
            A page token returned from a previous
            request. When paginating, all other parameters
            provided in the request must match the call that
            returned the page token.
        view (google.cloud.advisorynotifications_v1.types.NotificationView):
            Specifies which parts of the notification
            resource should be returned in the response.
        language_code (str):
            ISO code for requested localization language.
            If unset, will be interpereted as "en". If the
            requested language is valid, but not supported
            for this notification, English will be returned
            with an "Not applicable" LocalizationState. If
            the ISO code is invalid (i.e. not a real
            language), this RPC will throw an error.
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
    view: "NotificationView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="NotificationView",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListNotificationsResponse(proto.Message):
    r"""Response of ListNotifications endpoint.

    Attributes:
        notifications (MutableSequence[google.cloud.advisorynotifications_v1.types.Notification]):
            List of notifications under a given parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Estimation of a total number of
            notifications.
    """

    @property
    def raw_page(self):
        return self

    notifications: MutableSequence["Notification"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Notification",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetNotificationRequest(proto.Message):
    r"""Request for fetching a notification.

    Attributes:
        name (str):
            Required. A name of the notification to
            retrieve. Format:

            organizations/{organization}/locations/{location}/notifications/{notification}
            or
            projects/{projects}/locations/{location}/notifications/{notification}.
        language_code (str):
            ISO code for requested localization language.
            If unset, will be interpereted as "en". If the
            requested language is valid, but not supported
            for this notification, English will be returned
            with an "Not applicable" LocalizationState. If
            the ISO code is invalid (i.e. not a real
            language), this RPC will throw an error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Settings(proto.Message):
    r"""Settings for Advisory Notifications.

    Attributes:
        name (str):
            Identifier. The resource name of the settings
            to retrieve. Format:

            organizations/{organization}/locations/{location}/settings
            or
            projects/{projects}/locations/{location}/settings.
        notification_settings (MutableMapping[str, google.cloud.advisorynotifications_v1.types.NotificationSettings]):
            Required. Map of each notification type and
            its settings to get/set all settings at once.
            The server will validate the value for each
            notification type.
        etag (str):
            Required. Fingerprint for optimistic
            concurrency returned in Get requests. Must be
            provided for Update requests. If the value
            provided does not match the value known to the
            server, ABORTED will be thrown, and the client
            should retry the read-modify-write cycle.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    notification_settings: MutableMapping[str, "NotificationSettings"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="NotificationSettings",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class NotificationSettings(proto.Message):
    r"""Settings for each NotificationType.

    Attributes:
        enabled (bool):
            Whether the associated NotificationType is
            enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class GetSettingsRequest(proto.Message):
    r"""Request of GetSettings endpoint.

    Attributes:
        name (str):
            Required. The resource name of the settings
            to retrieve. Format:

            organizations/{organization}/locations/{location}/settings
            or
            projects/{projects}/locations/{location}/settings.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSettingsRequest(proto.Message):
    r"""Request of UpdateSettings endpoint.

    Attributes:
        settings (google.cloud.advisorynotifications_v1.types.Settings):
            Required. New settings.
    """

    settings: "Settings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Settings",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
