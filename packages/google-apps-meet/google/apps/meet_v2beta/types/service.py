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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.apps.meet_v2beta.types import resource

__protobuf__ = proto.module(
    package="google.apps.meet.v2beta",
    manifest={
        "CreateSpaceRequest",
        "GetSpaceRequest",
        "UpdateSpaceRequest",
        "ConnectActiveConferenceRequest",
        "ConnectActiveConferenceResponse",
        "EndActiveConferenceRequest",
        "CreateMemberRequest",
        "GetMemberRequest",
        "ListMembersRequest",
        "ListMembersResponse",
        "DeleteMemberRequest",
        "UpdateMemberRequest",
        "BatchUpdateMembersRequest",
        "BatchUpdateMembersResponse",
        "GetConferenceRecordRequest",
        "ListConferenceRecordsRequest",
        "ListConferenceRecordsResponse",
        "GetParticipantRequest",
        "ListParticipantsRequest",
        "ListParticipantsResponse",
        "GetParticipantSessionRequest",
        "ListParticipantSessionsRequest",
        "ListParticipantSessionsResponse",
        "GetRecordingRequest",
        "ListRecordingsRequest",
        "ListRecordingsResponse",
        "GetTranscriptRequest",
        "ListTranscriptsRequest",
        "ListTranscriptsResponse",
        "GetTranscriptEntryRequest",
        "ListTranscriptEntriesRequest",
        "ListTranscriptEntriesResponse",
        "GetSmartNoteRequest",
        "ListSmartNotesRequest",
        "ListSmartNotesResponse",
    },
)


class CreateSpaceRequest(proto.Message):
    r"""Request to create a space.

    Attributes:
        space (google.apps.meet_v2beta.types.Space):
            Space to be created. As of May 2023, the
            input space can be empty. Later on the input
            space can be non-empty when space configuration
            is introduced.
    """

    space: resource.Space = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resource.Space,
    )


class GetSpaceRequest(proto.Message):
    r"""Request to get a space.

    Attributes:
        name (str):
            Required. Resource name of the space.

            Format: ``spaces/{space}`` or ``spaces/{meetingCode}``.

            ``{space}`` is the resource identifier for the space. It's a
            unique, server-generated ID and is case sensitive. For
            example, ``jQCFfuBOdN5z``.

            ``{meetingCode}`` is an alias for the space. It's a
            typeable, unique character string and is non-case sensitive.
            For example, ``abc-mnop-xyz``. The maximum length is 128
            characters.

            A ``meetingCode`` shouldn't be stored long term as it can
            become dissociated from a meeting space and can be reused
            for different meeting spaces in the future. Generally, a
            ``meetingCode`` expires 365 days after last use. For more
            information, see `Learn about meeting codes in Google
            Meet <https://support.google.com/meet/answer/10710509>`__.

            For more information, see `How Meet identifies a meeting
            space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSpaceRequest(proto.Message):
    r"""Request to update a space.

    Attributes:
        space (google.apps.meet_v2beta.types.Space):
            Required. Space to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask used to specify the fields to be
            updated in the space. If update_mask isn't provided(not set,
            set with empty paths, or only has "" as paths), it defaults
            to update all fields provided with values in the request.
            Using "\*" as update_mask will update all fields, including
            deleting fields not set in the request.
    """

    space: resource.Space = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resource.Space,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ConnectActiveConferenceRequest(proto.Message):
    r"""Request to establish a WebRTC connection to the active
    conference of a space.

    Attributes:
        name (str):
            Required. Resource name of the space.
            Format: spaces/{spaceId}
        offer (str):
            Required. WebRTC SDP (Session Description Protocol) offer
            from the client.

            The format is defined by `RFC
            8866 <https://www.rfc-editor.org/rfc/rfc8866>`__ with
            mandatory keys defined by `RFC
            8829 <https://www.rfc-editor.org/rfc/rfc8829>`__. This is
            the standard SDP format generated by a peer connection's
            createOffer() and createAnswer() methods.
        config (google.apps.meet_v2beta.types.ConnectActiveConferenceRequest.ConnectionConfig):
            Optional. Additional configuration options
            for a Media API session. If unset, default
            values will be provided for the session.
    """

    class ConnectionConfig(proto.Message):
        r"""Additional configuration options for Media API sessions.

        Attributes:
            confirmation_timeout (google.protobuf.duration_pb2.Duration):
                Optional. The amount of time to wait before a
                confirmation action is cancelled. If unset, a
                default value will be used. The duration cannot
                exceed 5 minutes. Larger timeouts and negative
                durations will result in RPC failure.
        """

        confirmation_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offer: str = proto.Field(
        proto.STRING,
        number=2,
    )
    config: ConnectionConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ConnectionConfig,
    )


class ConnectActiveConferenceResponse(proto.Message):
    r"""Response of ConnectActiveConference method.

    A success response does not indicate the meeting is fully joined;
    further communication must occur across WebRTC.

    See `Meet Media API
    overview <https://developers.google.com/workspace/meet/media-api/guides/overview>`__
    for more details about this connection.

    Attributes:
        answer (str):
            WebRTC SDP answer to the offer.
        trace_id (str):
            Trace ID for debugging purposes. Please
            include this value when filing bugs.
    """

    answer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EndActiveConferenceRequest(proto.Message):
    r"""Request to end an ongoing conference of a space.

    Attributes:
        name (str):
            Required. Resource name of the space.

            Format: ``spaces/{space}``.

            ``{space}`` is the resource identifier for the space. It's a
            unique, server-generated ID and is case sensitive. For
            example, ``jQCFfuBOdN5z``.

            For more information, see `How Meet identifies a meeting
            space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMemberRequest(proto.Message):
    r"""Request to create a member for a space.

    Attributes:
        parent (str):
            Required. Format: spaces/{space}
        member (google.apps.meet_v2beta.types.Member):
            Required. The member to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    member: resource.Member = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resource.Member,
    )


class GetMemberRequest(proto.Message):
    r"""Request to get a member from a space.

    Attributes:
        name (str):
            Required. Format:
            “spaces/{space}/members/{member}”
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMembersRequest(proto.Message):
    r"""Request to list all members of a space.

    Attributes:
        parent (str):
            Required. Format: spaces/{space}
        page_size (int):
            Optional. Maximum number of members to
            return. The service might return fewer than this
            value. If unspecified or set to 0, at most 250
            members are returned. The maximum value is 500;
            values above 500 are coerced to 500. Maximum
            might change in the future.
        page_token (str):
            Optional. Page token returned from previous
            List Call.
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


class ListMembersResponse(proto.Message):
    r"""Response of list members.

    Attributes:
        members (MutableSequence[google.apps.meet_v2beta.types.Member]):
            The list of members for the current page.
        next_page_token (str):
            Token to be circulated back for further list
            call if current list doesn't include all the
            members. Unset if all members are returned.
    """

    @property
    def raw_page(self):
        return self

    members: MutableSequence[resource.Member] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.Member,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteMemberRequest(proto.Message):
    r"""Request to delete a member from a space.

    Attributes:
        name (str):
            Required. Format:
            “spaces/{space}/members/{member}”
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateMemberRequest(proto.Message):
    r"""Request to update a member.

    Attributes:
        member (google.apps.meet_v2beta.types.Member):
            Required. The Member to update.
            Format: spaces/{space}/members/{member}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask used to specify the fields to be
            updated in the member. If update_mask isn't provided(not
            set, set with empty paths, or only has "" as paths), it
            defaults to update all fields provided with values in the
            request. Using "\*" as update_mask will update all fields,
            including deleting fields not set in the request. In case of
            BatchUpdate, it must be absent or the same as the
            update_mask in BatchUpdateMembersRequest when
            UpdateMemberRequest is built as a child request of
            BatchUpdateMembersRequest.
    """

    member: resource.Member = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resource.Member,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateMembersRequest(proto.Message):
    r"""Request to update members of one space within a batch.

    Attributes:
        parent (str):
            Required. The parent resource shared by all
            Members being updated. Format: spaces/{space}
        requests (MutableSequence[google.apps.meet_v2beta.types.UpdateMemberRequest]):
            Required. The request message specifying the
            resources to update. A maximum of 500 members
            can be modified in a batch.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Top-level field mask used to
            specify the fields to be updated in the member
            for all UpdateMemberRequests. There are 4
            possible scenarios for top-level and child field
            mask:

            1. top-level and child field mask is absent:

               All fields provided in the requests are
            updated, including deleting    fields not set in
            the requests.
            2. top-level field mask is present but child
                field mask is absent:

               The fields specified in the top-level field
            mask are updated.
            3. top-level and child field mask is present:

               The child field mask must be the same as the
            top-level field mask.
            4. top-level field mask is absent but child
                field mask is present:

               It isn't supported and will return an error.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateMemberRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateMemberRequest",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateMembersResponse(proto.Message):
    r"""Response of batch update members.

    Attributes:
        members (MutableSequence[google.apps.meet_v2beta.types.Member]):
            Members updated.
    """

    members: MutableSequence[resource.Member] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.Member,
    )


class GetConferenceRecordRequest(proto.Message):
    r"""Request to get a conference record.

    Attributes:
        name (str):
            Required. Resource name of the conference.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConferenceRecordsRequest(proto.Message):
    r"""Request to fetch list of conference records per user.

    Attributes:
        page_size (int):
            Optional. Maximum number of conference
            records to return. The service might return
            fewer than this value. If unspecified, at most
            25 conference records are returned. The maximum
            value is 100; values above 100 are coerced to
            100. Maximum might change in the future.
        page_token (str):
            Optional. Page token returned from previous
            List Call.
        filter (str):
            Optional. User specified filtering condition in `EBNF
            format <https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form>`__.
            The following are the filterable fields:

            - ``space.meeting_code``
            - ``space.name``
            - ``start_time``
            - ``end_time``

            For example, consider the following filters:

            - ``space.name = "spaces/NAME"``
            - ``space.meeting_code = "abc-mnop-xyz"``
            - ``start_time>="2024-01-01T00:00:00.000Z" AND start_time<="2024-01-02T00:00:00.000Z"``
            - ``end_time IS NULL``
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListConferenceRecordsResponse(proto.Message):
    r"""Response of ListConferenceRecords method.

    Attributes:
        conference_records (MutableSequence[google.apps.meet_v2beta.types.ConferenceRecord]):
            List of conferences in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List does NOT include all the
            Conferences. Unset if all conferences have been
            returned.
    """

    @property
    def raw_page(self):
        return self

    conference_records: MutableSequence[resource.ConferenceRecord] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resource.ConferenceRecord,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetParticipantRequest(proto.Message):
    r"""Request to get a participant.

    Attributes:
        name (str):
            Required. Resource name of the participant.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListParticipantsRequest(proto.Message):
    r"""Request to fetch list of participants per conference.

    Attributes:
        parent (str):
            Required. Format: ``conferenceRecords/{conference_record}``
        page_size (int):
            Maximum number of participants to return. The
            service might return fewer than this value.
            If unspecified, at most 100 participants are
            returned. The maximum value is 250; values above
            250 are coerced to 250. Maximum might change in
            the future.
        page_token (str):
            Page token returned from previous List Call.
        filter (str):
            Optional. User specified filtering condition in `EBNF
            format <https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form>`__.
            The following are the filterable fields:

            - ``earliest_start_time``
            - ``latest_end_time``

            For example, ``latest_end_time IS NULL`` returns active
            participants in the conference.
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


class ListParticipantsResponse(proto.Message):
    r"""Response of ListParticipants method.

    Attributes:
        participants (MutableSequence[google.apps.meet_v2beta.types.Participant]):
            List of participants in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List doesn't include all the
            participants. Unset if all participants are
            returned.
        total_size (int):
            Total, exact number of ``participants``. By default, this
            field isn't included in the response. Set the field mask in
            `SystemParameterContext <https://cloud.google.com/apis/docs/system-parameters>`__
            to receive this field in the response.
    """

    @property
    def raw_page(self):
        return self

    participants: MutableSequence[resource.Participant] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.Participant,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetParticipantSessionRequest(proto.Message):
    r"""Request to get a participant session.

    Attributes:
        name (str):
            Required. Resource name of the participant.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListParticipantSessionsRequest(proto.Message):
    r"""Request to fetch list of participant sessions per conference
    record, per participant.

    Attributes:
        parent (str):
            Required. Format:
            ``conferenceRecords/{conference_record}/participants/{participant}``
        page_size (int):
            Optional. Maximum number of participant
            sessions to return. The service might return
            fewer than this value. If unspecified, at most
            100 participants are returned. The maximum value
            is 250; values above 250 are coerced to 250.
            Maximum might change in the future.
        page_token (str):
            Optional. Page token returned from previous
            List Call.
        filter (str):
            Optional. User specified filtering condition in `EBNF
            format <https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form>`__.
            The following are the filterable fields:

            - ``start_time``
            - ``end_time``

            For example, ``end_time IS NULL`` returns active participant
            sessions in the conference record.
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


class ListParticipantSessionsResponse(proto.Message):
    r"""Response of ListParticipants method.

    Attributes:
        participant_sessions (MutableSequence[google.apps.meet_v2beta.types.ParticipantSession]):
            List of participants in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List doesn't include all the
            participants. Unset if all participants are
            returned.
    """

    @property
    def raw_page(self):
        return self

    participant_sessions: MutableSequence[resource.ParticipantSession] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resource.ParticipantSession,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRecordingRequest(proto.Message):
    r"""Request message for GetRecording method.

    Attributes:
        name (str):
            Required. Resource name of the recording.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRecordingsRequest(proto.Message):
    r"""Request for ListRecordings method.

    Attributes:
        parent (str):
            Required. Format: ``conferenceRecords/{conference_record}``
        page_size (int):
            Maximum number of recordings to return. The
            service might return fewer than this value.
            If unspecified, at most 10 recordings are
            returned. The maximum value is 100; values above
            100 are coerced to 100. Maximum might change in
            the future.
        page_token (str):
            Page token returned from previous List Call.
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


class ListRecordingsResponse(proto.Message):
    r"""Response for ListRecordings method.

    Attributes:
        recordings (MutableSequence[google.apps.meet_v2beta.types.Recording]):
            List of recordings in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List doesn't include all the
            recordings. Unset if all recordings are
            returned.
    """

    @property
    def raw_page(self):
        return self

    recordings: MutableSequence[resource.Recording] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.Recording,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTranscriptRequest(proto.Message):
    r"""Request for GetTranscript method.

    Attributes:
        name (str):
            Required. Resource name of the transcript.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTranscriptsRequest(proto.Message):
    r"""Request for ListTranscripts method.

    Attributes:
        parent (str):
            Required. Format: ``conferenceRecords/{conference_record}``
        page_size (int):
            Maximum number of transcripts to return. The
            service might return fewer than this value.
            If unspecified, at most 10 transcripts are
            returned. The maximum value is 100; values above
            100 are coerced to 100. Maximum might change in
            the future.
        page_token (str):
            Page token returned from previous List Call.
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


class ListTranscriptsResponse(proto.Message):
    r"""Response for ListTranscripts method.

    Attributes:
        transcripts (MutableSequence[google.apps.meet_v2beta.types.Transcript]):
            List of transcripts in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List doesn't include all the
            transcripts. Unset if all transcripts are
            returned.
    """

    @property
    def raw_page(self):
        return self

    transcripts: MutableSequence[resource.Transcript] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.Transcript,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTranscriptEntryRequest(proto.Message):
    r"""Request for GetTranscriptEntry method.

    Attributes:
        name (str):
            Required. Resource name of the ``TranscriptEntry``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTranscriptEntriesRequest(proto.Message):
    r"""Request for ListTranscriptEntries method.

    Attributes:
        parent (str):
            Required. Format:
            ``conferenceRecords/{conference_record}/transcripts/{transcript}``
        page_size (int):
            Maximum number of entries to return. The
            service might return fewer than this value.
            If unspecified, at most 10 entries are returned.
            The maximum value is 100; values above 100 are
            coerced to 100. Maximum might change in the
            future.
        page_token (str):
            Page token returned from previous List Call.
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


class ListTranscriptEntriesResponse(proto.Message):
    r"""Response for ListTranscriptEntries method.

    Attributes:
        transcript_entries (MutableSequence[google.apps.meet_v2beta.types.TranscriptEntry]):
            List of TranscriptEntries in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List doesn't include all the
            transcript entries. Unset if all entries are
            returned.
    """

    @property
    def raw_page(self):
        return self

    transcript_entries: MutableSequence[resource.TranscriptEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.TranscriptEntry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSmartNoteRequest(proto.Message):
    r"""Request for GetSmartNote method.

    Attributes:
        name (str):
            Required. Resource name of the smart note. Format:
            conferenceRecords/{conference_record}/smartNotes/{smart_note}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSmartNotesRequest(proto.Message):
    r"""Request for ListSmartNotes method.

    Attributes:
        parent (str):
            Required. Format: ``conferenceRecords/{conference_record}``
        page_size (int):
            Optional. Maximum number of smart notes to
            return. The service might return fewer than this
            value. If unspecified, at most 10 smart notes
            are returned. The maximum value is 100; values
            above 100 are coerced to 100. Maximum might
            change in the future.
        page_token (str):
            Optional. Page token returned from previous
            List Call.
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


class ListSmartNotesResponse(proto.Message):
    r"""Response for ListSmartNotes method.

    Attributes:
        smart_notes (MutableSequence[google.apps.meet_v2beta.types.SmartNote]):
            List of smart notes in one page.
        next_page_token (str):
            Token to be circulated back for further List
            call if current List doesn't include all the
            smart notes. Unset if all smart notes are
            returned.
    """

    @property
    def raw_page(self):
        return self

    smart_notes: MutableSequence[resource.SmartNote] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.SmartNote,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
