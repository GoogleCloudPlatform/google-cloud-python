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
import google.api_core as api_core

from google.apps.meet_v2beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.apps.meet_v2beta.services.conference_records_service",
    "google.apps.meet_v2beta.services.spaces_service",
    "google.apps.meet_v2beta.types.resource",
    "google.apps.meet_v2beta.types.service",
}


from .services.conference_records_service import (
    ConferenceRecordsServiceAsyncClient,
    ConferenceRecordsServiceClient,
)
from .services.spaces_service import SpacesServiceAsyncClient, SpacesServiceClient
from .types.resource import (
    ActiveConference,
    AnonymousUser,
    ConferenceRecord,
    DocsDestination,
    DriveDestination,
    Member,
    Participant,
    ParticipantSession,
    PhoneUser,
    Recording,
    SignedinUser,
    SmartNote,
    Space,
    SpaceConfig,
    Transcript,
    TranscriptEntry,
)
from .types.service import (
    BatchUpdateMembersRequest,
    BatchUpdateMembersResponse,
    ConnectActiveConferenceRequest,
    ConnectActiveConferenceResponse,
    CreateMemberRequest,
    CreateSpaceRequest,
    DeleteMemberRequest,
    EndActiveConferenceRequest,
    GetConferenceRecordRequest,
    GetMemberRequest,
    GetParticipantRequest,
    GetParticipantSessionRequest,
    GetRecordingRequest,
    GetSmartNoteRequest,
    GetSpaceRequest,
    GetTranscriptEntryRequest,
    GetTranscriptRequest,
    ListConferenceRecordsRequest,
    ListConferenceRecordsResponse,
    ListMembersRequest,
    ListMembersResponse,
    ListParticipantSessionsRequest,
    ListParticipantSessionsResponse,
    ListParticipantsRequest,
    ListParticipantsResponse,
    ListRecordingsRequest,
    ListRecordingsResponse,
    ListSmartNotesRequest,
    ListSmartNotesResponse,
    ListTranscriptEntriesRequest,
    ListTranscriptEntriesResponse,
    ListTranscriptsRequest,
    ListTranscriptsResponse,
    UpdateMemberRequest,
    UpdateSpaceRequest,
)

__all__ = (
    "ConferenceRecordsServiceAsyncClient",
    "SpacesServiceAsyncClient",
    "ActiveConference",
    "AnonymousUser",
    "BatchUpdateMembersRequest",
    "BatchUpdateMembersResponse",
    "ConferenceRecord",
    "ConferenceRecordsServiceClient",
    "ConnectActiveConferenceRequest",
    "ConnectActiveConferenceResponse",
    "CreateMemberRequest",
    "CreateSpaceRequest",
    "DeleteMemberRequest",
    "DocsDestination",
    "DriveDestination",
    "EndActiveConferenceRequest",
    "GetConferenceRecordRequest",
    "GetMemberRequest",
    "GetParticipantRequest",
    "GetParticipantSessionRequest",
    "GetRecordingRequest",
    "GetSmartNoteRequest",
    "GetSpaceRequest",
    "GetTranscriptEntryRequest",
    "GetTranscriptRequest",
    "ListConferenceRecordsRequest",
    "ListConferenceRecordsResponse",
    "ListMembersRequest",
    "ListMembersResponse",
    "ListParticipantSessionsRequest",
    "ListParticipantSessionsResponse",
    "ListParticipantsRequest",
    "ListParticipantsResponse",
    "ListRecordingsRequest",
    "ListRecordingsResponse",
    "ListSmartNotesRequest",
    "ListSmartNotesResponse",
    "ListTranscriptEntriesRequest",
    "ListTranscriptEntriesResponse",
    "ListTranscriptsRequest",
    "ListTranscriptsResponse",
    "Member",
    "Participant",
    "ParticipantSession",
    "PhoneUser",
    "Recording",
    "SignedinUser",
    "SmartNote",
    "Space",
    "SpaceConfig",
    "SpacesServiceClient",
    "Transcript",
    "TranscriptEntry",
    "UpdateMemberRequest",
    "UpdateSpaceRequest",
)

api_core.check_python_version("google.apps.meet_v2beta")
api_core.check_dependency_versions("google.apps.meet_v2beta")
