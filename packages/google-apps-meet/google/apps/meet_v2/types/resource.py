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
    package="google.apps.meet.v2",
    manifest={
        "Space",
        "ActiveConference",
        "SpaceConfig",
        "Member",
        "ConferenceRecord",
        "Participant",
        "ParticipantSession",
        "SignedinUser",
        "AnonymousUser",
        "PhoneUser",
        "Recording",
        "DriveDestination",
        "Transcript",
        "DocsDestination",
        "TranscriptEntry",
        "SmartNote",
    },
)


class Space(proto.Message):
    r"""Virtual place where conferences are held. Only one active
    conference can be held in one space at any given time.

    Attributes:
        name (str):
            Immutable. Resource name of the space.

            Format: ``spaces/{space}``.

            ``{space}`` is the resource identifier for the space. It's a
            unique, server-generated ID and is case sensitive. For
            example, ``jQCFfuBOdN5z``.

            For more information, see `How Meet identifies a meeting
            space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space>`__.
        meeting_uri (str):
            Output only. URI used to join meetings consisting of
            ``https://meet.google.com/`` followed by the
            ``meeting_code``. For example,
            ``https://meet.google.com/abc-mnop-xyz``.
        meeting_code (str):
            Output only. Type friendly unique string used to join the
            meeting.

            Format: ``[a-z]+-[a-z]+-[a-z]+``. For example,
            ``abc-mnop-xyz``.

            The maximum length is 128 characters.

            Can only be used as an alias of the space name to get the
            space.
        config (google.apps.meet_v2.types.SpaceConfig):
            Configuration pertaining to the meeting
            space.
        active_conference (google.apps.meet_v2.types.ActiveConference):
            Active conference, if it exists.
        phone_access (MutableSequence[google.apps.meet_v2.types.Space.PhoneAccess]):
            Output only. All regional phone access
            methods for this meeting space. Can be empty.
        gateway_sip_access (MutableSequence[google.apps.meet_v2.types.Space.GatewaySipAccess]):
            Output only. The SIP-based access methods
            that can be used to join the conference. Can be
            empty.
    """

    class PhoneAccess(proto.Message):
        r"""Phone access contains information required to dial into a
        conference using a regional phone number and a PIN that is
        specific to that phone number.

        Attributes:
            phone_number (str):
                The phone number to dial for this meeting
                space in E.164 format. Full phone number with a
                leading '+' character.
            pin (str):
                The PIN that users must enter after dialing
                the given number. The PIN consists of only
                decimal digits and the length may vary.
            region_code (str):
                The CLDR/ISO 3166 region code for the country
                associated with this phone access. To be parsed
                by the i18n RegionCode utility. Example: "SE"
                for Sweden.
            language_code (str):
                The BCP 47/LDML language code for the
                language associated with this phone access. To
                be parsed by the i18n LanguageCode utility.
                Examples: "es-419" for Latin American Spanish,
                "fr-CA" for Canadian French.
        """

        phone_number: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pin: str = proto.Field(
            proto.STRING,
            number=2,
        )
        region_code: str = proto.Field(
            proto.STRING,
            number=3,
        )
        language_code: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class GatewaySipAccess(proto.Message):
        r"""Details how to join the conference through a SIP gateway.

        Attributes:
            uri (str):
                The Session Initiation Protocol (SIP) URI the conference can
                be reached through.

                The string is in one of these formats:

                - "sip:USER_ID@GATEWAY_ADDRESS"
                - "sips:USER_ID@GATEWAY_ADDRESS"

                where USER_ID is the 13-digit universal pin (with the future
                option to support using a Meet meeting code as well), and
                GATEWAY_ADDRESS is a valid address to be resolved using a
                DNS SRV lookup, or a dotted quad.
            sip_access_code (str):
                The permanent numeric code for manual entry
                on specially configured devices.
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sip_access_code: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    meeting_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    meeting_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    config: "SpaceConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SpaceConfig",
    )
    active_conference: "ActiveConference" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ActiveConference",
    )
    phone_access: MutableSequence[PhoneAccess] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=PhoneAccess,
    )
    gateway_sip_access: MutableSequence[GatewaySipAccess] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=GatewaySipAccess,
    )


class ActiveConference(proto.Message):
    r"""Active conference.

    Attributes:
        conference_record (str):
            Output only. Reference to 'ConferenceRecord' resource.
            Format: ``conferenceRecords/{conference_record}`` where
            ``{conference_record}`` is a unique ID for each instance of
            a call within a space.
    """

    conference_record: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SpaceConfig(proto.Message):
    r"""The configuration pertaining to a meeting space.

    Attributes:
        access_type (google.apps.meet_v2.types.SpaceConfig.AccessType):
            Access type of the meeting space that
            determines who can join without knocking.
            Default: The user's default access settings.
            Controlled by the user's admin for enterprise
            users or RESTRICTED.
        entry_point_access (google.apps.meet_v2.types.SpaceConfig.EntryPointAccess):
            Defines the entry points that can be used to
            join meetings hosted in this meeting space.
            Default: EntryPointAccess.ALL
        moderation (google.apps.meet_v2.types.SpaceConfig.Moderation):
            The pre-configured moderation mode for the
            Meeting. Default: Controlled by the user's
            policies.
        moderation_restrictions (google.apps.meet_v2.types.SpaceConfig.ModerationRestrictions):
            When moderation.ON, these restrictions go
            into effect for the meeting. When
            moderation.OFF, will be reset to default
            ModerationRestrictions.
        attendance_report_generation_type (google.apps.meet_v2.types.SpaceConfig.AttendanceReportGenerationType):
            Whether attendance report is enabled for the
            meeting space.
        artifact_config (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig):
            Configuration pertaining to the
            auto-generated artifacts that the meeting
            supports.
    """

    class AccessType(proto.Enum):
        r"""Possible access types for a meeting space.

        Values:
            ACCESS_TYPE_UNSPECIFIED (0):
                Default value specified by the user's
                organization. Note: This is never returned, as
                the configured access type is returned instead.
            OPEN (1):
                Anyone with the join information (for
                example, the URL or phone access information)
                can join without knocking.
            TRUSTED (2):
                Members of the host's organization, invited
                external users, and dial-in users can join
                without knocking. Everyone else must knock.
            RESTRICTED (3):
                Only invitees can join without knocking.
                Everyone else must knock.
        """

        ACCESS_TYPE_UNSPECIFIED = 0
        OPEN = 1
        TRUSTED = 2
        RESTRICTED = 3

    class EntryPointAccess(proto.Enum):
        r"""Entry points that can be used to join a meeting. Example:
        ``meet.google.com``, the Meet Embed SDK Web, or a mobile
        application.

        Values:
            ENTRY_POINT_ACCESS_UNSPECIFIED (0):
                Unused.
            ALL (1):
                All entry points are allowed.
            CREATOR_APP_ONLY (2):
                Only entry points owned by the Google Cloud
                project that created the space can be used to
                join meetings in this space. Apps can use the
                Meet Embed SDK Web or mobile Meet SDKs to create
                owned entry points.
        """

        ENTRY_POINT_ACCESS_UNSPECIFIED = 0
        ALL = 1
        CREATOR_APP_ONLY = 2

    class Moderation(proto.Enum):
        r"""The moderation mode for a meeting. When the moderation mode
        is on, the meeting owner has more control over the meeting with
        features such as co-host management (see message Member) and
        feature restrictions (see message ModerationRestrictions).

        Values:
            MODERATION_UNSPECIFIED (0):
                Moderation type is not specified. This is
                used to indicate the user hasn't specified any
                value as the user does not intend to update the
                state. Users are not allowed to set the value as
                unspecified.
            OFF (1):
                Moderation is off.
            ON (2):
                Moderation is on.
        """

        MODERATION_UNSPECIFIED = 0
        OFF = 1
        ON = 2

    class AttendanceReportGenerationType(proto.Enum):
        r"""Possible states of whether attendance report is enabled for
        the meeting space.

        Values:
            ATTENDANCE_REPORT_GENERATION_TYPE_UNSPECIFIED (0):
                Default value specified by user policy.
                This should never be returned.
            GENERATE_REPORT (1):
                Attendance report will be generated and sent
                to drive/email.
            DO_NOT_GENERATE (2):
                Attendance report will not be generated.
        """

        ATTENDANCE_REPORT_GENERATION_TYPE_UNSPECIFIED = 0
        GENERATE_REPORT = 1
        DO_NOT_GENERATE = 2

    class ModerationRestrictions(proto.Message):
        r"""Defines restrictions for features when the meeting is
        moderated.

        Attributes:
            chat_restriction (google.apps.meet_v2.types.SpaceConfig.ModerationRestrictions.RestrictionType):
                Defines who has permission to send chat
                messages in the meeting space.
            reaction_restriction (google.apps.meet_v2.types.SpaceConfig.ModerationRestrictions.RestrictionType):
                Defines who has permission to send reactions
                in the meeting space.
            present_restriction (google.apps.meet_v2.types.SpaceConfig.ModerationRestrictions.RestrictionType):
                Defines who has permission to share their
                screen in the meeting space.
            default_join_as_viewer_type (google.apps.meet_v2.types.SpaceConfig.ModerationRestrictions.DefaultJoinAsViewerType):
                Defines whether to restrict the default role
                assigned to users as viewer.
        """

        class RestrictionType(proto.Enum):
            r"""Determines who has permission to use a particular feature.

            Values:
                RESTRICTION_TYPE_UNSPECIFIED (0):
                    Default value specified by user policy.
                    This should never be returned.
                HOSTS_ONLY (1):
                    Meeting owner and co-host have the
                    permission.
                NO_RESTRICTION (2):
                    All Participants have permissions.
            """

            RESTRICTION_TYPE_UNSPECIFIED = 0
            HOSTS_ONLY = 1
            NO_RESTRICTION = 2

        class DefaultJoinAsViewerType(proto.Enum):
            r"""By default users will join as contributors. Hosts can
            restrict users to join as viewers.
            Note: If an explicit role is set for a user in the Member
            resource, the user will join as that role.

            Values:
                DEFAULT_JOIN_AS_VIEWER_TYPE_UNSPECIFIED (0):
                    Default value specified by user policy.
                    This should never be returned.
                ON (1):
                    Users will by default join as viewers.
                OFF (2):
                    Users will by default join as contributors.
            """

            DEFAULT_JOIN_AS_VIEWER_TYPE_UNSPECIFIED = 0
            ON = 1
            OFF = 2

        chat_restriction: "SpaceConfig.ModerationRestrictions.RestrictionType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="SpaceConfig.ModerationRestrictions.RestrictionType",
            )
        )
        reaction_restriction: "SpaceConfig.ModerationRestrictions.RestrictionType" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="SpaceConfig.ModerationRestrictions.RestrictionType",
            )
        )
        present_restriction: "SpaceConfig.ModerationRestrictions.RestrictionType" = (
            proto.Field(
                proto.ENUM,
                number=3,
                enum="SpaceConfig.ModerationRestrictions.RestrictionType",
            )
        )
        default_join_as_viewer_type: "SpaceConfig.ModerationRestrictions.DefaultJoinAsViewerType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="SpaceConfig.ModerationRestrictions.DefaultJoinAsViewerType",
        )

    class ArtifactConfig(proto.Message):
        r"""Configuration related to meeting artifacts potentially
        generated by this meeting space.

        Attributes:
            recording_config (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig.RecordingConfig):
                Configuration for recording.
            transcription_config (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig.TranscriptionConfig):
                Configuration for auto-transcript.
            smart_notes_config (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig.SmartNotesConfig):
                Configuration for auto-smart-notes.
        """

        class AutoGenerationType(proto.Enum):
            r"""Determines whether an artifact can be automatically generated
            in the meeting space.

            Values:
                AUTO_GENERATION_TYPE_UNSPECIFIED (0):
                    Default value specified by user policy.
                    This should never be returned.
                ON (1):
                    The artifact is generated automatically.
                OFF (2):
                    The artifact is not generated automatically.
            """

            AUTO_GENERATION_TYPE_UNSPECIFIED = 0
            ON = 1
            OFF = 2

        class RecordingConfig(proto.Message):
            r"""Configuration related to recording in a meeting space.

            Attributes:
                auto_recording_generation (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig.AutoGenerationType):
                    Defines whether a meeting space is
                    automatically recorded when someone with the
                    privilege to record joins the meeting.
            """

            auto_recording_generation: "SpaceConfig.ArtifactConfig.AutoGenerationType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="SpaceConfig.ArtifactConfig.AutoGenerationType",
            )

        class TranscriptionConfig(proto.Message):
            r"""Configuration related to transcription in a meeting space.

            Attributes:
                auto_transcription_generation (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig.AutoGenerationType):
                    Defines whether the content of a meeting is
                    automatically transcribed when someone with the
                    privilege to transcribe joins the meeting.
            """

            auto_transcription_generation: "SpaceConfig.ArtifactConfig.AutoGenerationType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="SpaceConfig.ArtifactConfig.AutoGenerationType",
            )

        class SmartNotesConfig(proto.Message):
            r"""Configuration related to smart notes in a meeting space. For more
            information about smart notes, see `"Take notes for me" in Google
            Meet <https://support.google.com/meet/answer/14754931>`__.

            Attributes:
                auto_smart_notes_generation (google.apps.meet_v2.types.SpaceConfig.ArtifactConfig.AutoGenerationType):
                    Defines whether to automatically generate a
                    summary and recap of the meeting for all
                    invitees in the organization when someone with
                    the privilege to enable smart notes joins the
                    meeting.
            """

            auto_smart_notes_generation: "SpaceConfig.ArtifactConfig.AutoGenerationType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="SpaceConfig.ArtifactConfig.AutoGenerationType",
            )

        recording_config: "SpaceConfig.ArtifactConfig.RecordingConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="SpaceConfig.ArtifactConfig.RecordingConfig",
        )
        transcription_config: "SpaceConfig.ArtifactConfig.TranscriptionConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="SpaceConfig.ArtifactConfig.TranscriptionConfig",
            )
        )
        smart_notes_config: "SpaceConfig.ArtifactConfig.SmartNotesConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="SpaceConfig.ArtifactConfig.SmartNotesConfig",
        )

    access_type: AccessType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AccessType,
    )
    entry_point_access: EntryPointAccess = proto.Field(
        proto.ENUM,
        number=2,
        enum=EntryPointAccess,
    )
    moderation: Moderation = proto.Field(
        proto.ENUM,
        number=3,
        enum=Moderation,
    )
    moderation_restrictions: ModerationRestrictions = proto.Field(
        proto.MESSAGE,
        number=4,
        message=ModerationRestrictions,
    )
    attendance_report_generation_type: AttendanceReportGenerationType = proto.Field(
        proto.ENUM,
        number=6,
        enum=AttendanceReportGenerationType,
    )
    artifact_config: ArtifactConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=ArtifactConfig,
    )


class Member(proto.Message):
    r"""Users who are configured to have a role in the space. These
    users can join the space without knocking.

    Attributes:
        name (str):
            Identifier. Resource name of the member.
            Format: spaces/{space}/members/{member}
        email (str):
            Email for the member. This is required for
            creating the member.
        role (google.apps.meet_v2.types.Member.Role):
            The meeting role assigned to the member.
    """

    class Role(proto.Enum):
        r"""Role of this member in the space.

        Values:
            ROLE_UNSPECIFIED (0):
                This is used to indicate the user hasn't specified any value
                and the user’s role will be determined upon joining the
                meetings between 'contributor' and 'viewer' role depending
                on meeting configuration. For more information about the
                viewer role, see `Assign View only roles in Google
                Meet <https://support.google.com/meet/answer/13658394>`__.
            COHOST (1):
                Co-host role.
        """

        ROLE_UNSPECIFIED = 0
        COHOST = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    role: Role = proto.Field(
        proto.ENUM,
        number=3,
        enum=Role,
    )


class ConferenceRecord(proto.Message):
    r"""Single instance of a meeting held in a space.

    Attributes:
        name (str):
            Identifier. Resource name of the conference record. Format:
            ``conferenceRecords/{conference_record}`` where
            ``{conference_record}`` is a unique ID for each instance of
            a call within a space.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the conference
            started. Always set.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the conference
            ended. Set for past conferences. Unset if the
            conference is ongoing.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Server enforced expiration time
            for when this conference record resource is
            deleted. The resource is deleted 30 days after
            the conference ends.
        space (str):
            Output only. The space where the conference
            was held.
    """

    name: str = proto.Field(
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
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    space: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Participant(proto.Message):
    r"""User who attended or is attending a conference.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        signedin_user (google.apps.meet_v2.types.SignedinUser):
            Signed-in user.

            This field is a member of `oneof`_ ``user``.
        anonymous_user (google.apps.meet_v2.types.AnonymousUser):
            Anonymous user.

            This field is a member of `oneof`_ ``user``.
        phone_user (google.apps.meet_v2.types.PhoneUser):
            User calling from their phone.

            This field is a member of `oneof`_ ``user``.
        name (str):
            Output only. Resource name of the participant. Format:
            ``conferenceRecords/{conference_record}/participants/{participant}``
        earliest_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the participant first
            joined the meeting.
        latest_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the participant left
            the meeting for the last time. This can be null
            if it's an active meeting.
    """

    signedin_user: "SignedinUser" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="user",
        message="SignedinUser",
    )
    anonymous_user: "AnonymousUser" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="user",
        message="AnonymousUser",
    )
    phone_user: "PhoneUser" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="user",
        message="PhoneUser",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    earliest_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    latest_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class ParticipantSession(proto.Message):
    r"""Refers to each unique join or leave session when a user joins
    a conference from a device. Note that any time a user joins the
    conference a new unique ID is assigned. That means if a user
    joins a space multiple times from the same device, they're
    assigned different IDs, and are also be treated as different
    participant sessions.

    Attributes:
        name (str):
            Identifier. Session id.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the user session
            starts.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the user session
            ends. Unset if the user session hasn’t ended.
    """

    name: str = proto.Field(
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


class SignedinUser(proto.Message):
    r"""A signed-in user can be:

    a) An individual joining from a personal computer, mobile
    device, or through companion mode.
    b) A robot account used by conference room devices.

    Attributes:
        user (str):
            Output only. Unique ID for the user. Interoperable with
            Admin SDK API and People API. Format: ``users/{user}``
        display_name (str):
            Output only. For a personal device, it's the
            user's first name and last name. For a robot
            account, it's the administrator-specified device
            name. For example, "Altostrat Room".
    """

    user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AnonymousUser(proto.Message):
    r"""User who joins anonymously (meaning not signed into a Google
    Account).

    Attributes:
        display_name (str):
            Output only. User provided name when they
            join a conference anonymously.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PhoneUser(proto.Message):
    r"""User dialing in from a phone where the user's identity is
    unknown because they haven't signed in with a Google Account.

    Attributes:
        display_name (str):
            Output only. Partially redacted user's phone
            number when calling.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Recording(proto.Message):
    r"""Metadata about a recording created during a conference.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        drive_destination (google.apps.meet_v2.types.DriveDestination):
            Output only. Recording is saved to Google Drive as an MP4
            file. The ``drive_destination`` includes the Drive
            ``fileId`` that can be used to download the file using the
            ``files.get`` method of the Drive API.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Output only. Resource name of the recording. Format:
            ``conferenceRecords/{conference_record}/recordings/{recording}``
            where ``{recording}`` is a 1:1 mapping to each unique
            recording session during the conference.
        state (google.apps.meet_v2.types.Recording.State):
            Output only. Current state.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the recording
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the recording
            ended.
    """

    class State(proto.Enum):
        r"""Current state of the recording session.

        Values:
            STATE_UNSPECIFIED (0):
                Default, never used.
            STARTED (1):
                An active recording session has started.
            ENDED (2):
                This recording session has ended, but the
                recording file hasn't been generated yet.
            FILE_GENERATED (3):
                Recording file is generated and ready to
                download.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        ENDED = 2
        FILE_GENERATED = 3

    drive_destination: "DriveDestination" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="destination",
        message="DriveDestination",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
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


class DriveDestination(proto.Message):
    r"""Export location where a recording file is saved in Google
    Drive.

    Attributes:
        file (str):
            Output only. The ``fileId`` for the underlying MP4 file. For
            example, "1kuceFZohVoCh6FulBHxwy6I15Ogpc4hP". Use
            ``$ GET https://www.googleapis.com/drive/v3/files/{$fileId}?alt=media``
            to download the blob. For more information, see
            https://developers.google.com/drive/api/v3/reference/files/get.
        export_uri (str):
            Output only. Link used to play back the recording file in
            the browser. For example,
            ``https://drive.google.com/file/d/{$fileId}/view``.
    """

    file: str = proto.Field(
        proto.STRING,
        number=1,
    )
    export_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Transcript(proto.Message):
    r"""Metadata for a transcript generated from a conference. It
    refers to the ASR (Automatic Speech Recognition) result of
    user's speech during the conference.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        docs_destination (google.apps.meet_v2.types.DocsDestination):
            Output only. Where the Google Docs transcript
            is saved.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Output only. Resource name of the transcript. Format:
            ``conferenceRecords/{conference_record}/transcripts/{transcript}``,
            where ``{transcript}`` is a 1:1 mapping to each unique
            transcription session of the conference.
        state (google.apps.meet_v2.types.Transcript.State):
            Output only. Current state.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the transcript
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the transcript
            stopped.
    """

    class State(proto.Enum):
        r"""Current state of the transcript session.

        Values:
            STATE_UNSPECIFIED (0):
                Default, never used.
            STARTED (1):
                An active transcript session has started.
            ENDED (2):
                This transcript session has ended, but the
                transcript file hasn't been generated yet.
            FILE_GENERATED (3):
                Transcript file is generated and ready to
                download.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        ENDED = 2
        FILE_GENERATED = 3

    docs_destination: "DocsDestination" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="destination",
        message="DocsDestination",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
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


class DocsDestination(proto.Message):
    r"""Google Docs location where the transcript file is saved.

    Attributes:
        document (str):
            Output only. The document ID for the underlying Google Docs
            transcript file. For example,
            "1kuceFZohVoCh6FulBHxwy6I15Ogpc4hP". Use the
            ``documents.get`` method of the Google Docs API
            (https://developers.google.com/docs/api/reference/rest/v1/documents/get)
            to fetch the content.
        export_uri (str):
            Output only. URI for the Google Docs transcript file. Use
            ``https://docs.google.com/document/d/{$DocumentId}/view`` to
            browse the transcript in the browser.
    """

    document: str = proto.Field(
        proto.STRING,
        number=1,
    )
    export_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TranscriptEntry(proto.Message):
    r"""Single entry for one user’s speech during a transcript
    session.

    Attributes:
        name (str):
            Output only. Resource name of the entry. Format:
            "conferenceRecords/{conference_record}/transcripts/{transcript}/entries/{entry}".
        participant (str):
            Output only. Refers to the participant who
            speaks.
        text (str):
            Output only. The transcribed text of the
            participant's voice, at maximum 10K words. Note
            that the limit is subject to change.
        language_code (str):
            Output only. Language of spoken text, such as
            "en-US". IETF BCP 47 syntax
            (https://tools.ietf.org/html/bcp47)
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the transcript
            entry started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the transcript
            entry ended.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant: str = proto.Field(
        proto.STRING,
        number=2,
    )
    text: str = proto.Field(
        proto.STRING,
        number=3,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class SmartNote(proto.Message):
    r"""Metadata for a smart note generated from a conference. It
    refers to the notes generated from Take Notes with Gemini during
    the conference.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        docs_destination (google.apps.meet_v2.types.DocsDestination):
            Output only. The Google Doc destination where
            the smart notes are saved.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Output only. Identifier. Resource name of the smart notes.
            Format:
            ``conferenceRecords/{conference_record}/smartNotes/{smart_note}``,
            where ``{smart_note}`` is a 1:1 mapping to each unique smart
            notes session of the conference.
        state (google.apps.meet_v2.types.SmartNote.State):
            Output only. Current state.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the smart notes
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the smart notes
            stopped.
    """

    class State(proto.Enum):
        r"""Current state of the smart notes session.

        Values:
            STATE_UNSPECIFIED (0):
                Default, never used.
            STARTED (1):
                An active smart notes session has started.
            ENDED (2):
                This smart notes session has ended, but the
                smart notes file hasn't been generated yet.
            FILE_GENERATED (3):
                Smart notes file is generated and ready to
                download.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        ENDED = 2
        FILE_GENERATED = 3

    docs_destination: "DocsDestination" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="destination",
        message="DocsDestination",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
