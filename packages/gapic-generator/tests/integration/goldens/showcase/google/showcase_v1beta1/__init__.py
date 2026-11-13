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
from google.showcase_v1beta1 import gapic_version as package_version

import google.api_core as api_core

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
"google.showcase_v1beta1.services.echo",
"google.showcase_v1beta1.services.identity",
"google.showcase_v1beta1.services.messaging",
"google.showcase_v1beta1.services.resumable_upload_service",
"google.showcase_v1beta1.services.sequence_service",
"google.showcase_v1beta1.services.testing",
"google.showcase_v1beta1.types.echo",
"google.showcase_v1beta1.types.identity",
"google.showcase_v1beta1.types.messaging",
"google.showcase_v1beta1.types.rest_error",
"google.showcase_v1beta1.types.resumable_upload",
"google.showcase_v1beta1.types.sequence",
"google.showcase_v1beta1.types.testing",
}


from .services.echo import EchoClient
from .services.echo import EchoAsyncClient
from .services.identity import IdentityClient
from .services.identity import IdentityAsyncClient
from .services.messaging import MessagingClient
from .services.messaging import MessagingAsyncClient
from .services.resumable_upload_service import ResumableUploadServiceClient
from .services.resumable_upload_service import ResumableUploadServiceAsyncClient
from .services.sequence_service import SequenceServiceClient
from .services.sequence_service import SequenceServiceAsyncClient
from .services.testing import TestingClient
from .services.testing import TestingAsyncClient

from .types.echo import BlockRequest
from .types.echo import BlockResponse
from .types.echo import EchoErrorDetailsRequest
from .types.echo import EchoErrorDetailsResponse
from .types.echo import EchoRequest
from .types.echo import EchoResponse
from .types.echo import ErrorWithMultipleDetails
from .types.echo import ErrorWithSingleDetail
from .types.echo import ExpandRequest
from .types.echo import FailEchoWithDetailsRequest
from .types.echo import FailEchoWithDetailsResponse
from .types.echo import PagedExpandLegacyMappedResponse
from .types.echo import PagedExpandLegacyRequest
from .types.echo import PagedExpandRequest
from .types.echo import PagedExpandResponse
from .types.echo import PagedExpandResponseList
from .types.echo import PoetryError
from .types.echo import WaitMetadata
from .types.echo import WaitRequest
from .types.echo import WaitResponse
from .types.echo import Severity
from .types.identity import CreateUserRequest
from .types.identity import DeleteUserRequest
from .types.identity import GetUserRequest
from .types.identity import ListUsersRequest
from .types.identity import ListUsersResponse
from .types.identity import UpdateUserRequest
from .types.identity import User
from .types.messaging import Blurb
from .types.messaging import ConnectRequest
from .types.messaging import CreateBlurbRequest
from .types.messaging import CreateRoomRequest
from .types.messaging import DeleteBlurbRequest
from .types.messaging import DeleteRoomRequest
from .types.messaging import GetBlurbRequest
from .types.messaging import GetRoomRequest
from .types.messaging import ListBlurbsRequest
from .types.messaging import ListBlurbsResponse
from .types.messaging import ListRoomsRequest
from .types.messaging import ListRoomsResponse
from .types.messaging import Room
from .types.messaging import SearchBlurbsMetadata
from .types.messaging import SearchBlurbsRequest
from .types.messaging import SearchBlurbsResponse
from .types.messaging import SendBlurbsResponse
from .types.messaging import StreamBlurbsRequest
from .types.messaging import StreamBlurbsResponse
from .types.messaging import UpdateBlurbRequest
from .types.messaging import UpdateRoomRequest
from .types.rest_error import RestError
from .types.resumable_upload import UploadMediaRequest
from .types.resumable_upload import UploadMediaResponse
from .types.sequence import AttemptSequenceRequest
from .types.sequence import AttemptStreamingSequenceRequest
from .types.sequence import AttemptStreamingSequenceResponse
from .types.sequence import CreateSequenceRequest
from .types.sequence import CreateStreamingSequenceRequest
from .types.sequence import GetSequenceReportRequest
from .types.sequence import GetStreamingSequenceReportRequest
from .types.sequence import Sequence
from .types.sequence import SequenceReport
from .types.sequence import StreamingSequence
from .types.sequence import StreamingSequenceReport
from .types.testing import CreateSessionRequest
from .types.testing import DeleteSessionRequest
from .types.testing import DeleteTestRequest
from .types.testing import GetSessionRequest
from .types.testing import Issue
from .types.testing import ListSessionsRequest
from .types.testing import ListSessionsResponse
from .types.testing import ListTestsRequest
from .types.testing import ListTestsResponse
from .types.testing import ReportSessionRequest
from .types.testing import ReportSessionResponse
from .types.testing import Session
from .types.testing import Test
from .types.testing import TestRun
from .types.testing import VerifyTestRequest
from .types.testing import VerifyTestResponse

__all__ = (
    'EchoAsyncClient',
    'IdentityAsyncClient',
    'MessagingAsyncClient',
    'ResumableUploadServiceAsyncClient',
    'SequenceServiceAsyncClient',
    'TestingAsyncClient',
'AttemptSequenceRequest',
'AttemptStreamingSequenceRequest',
'AttemptStreamingSequenceResponse',
'BlockRequest',
'BlockResponse',
'Blurb',
'ConnectRequest',
'CreateBlurbRequest',
'CreateRoomRequest',
'CreateSequenceRequest',
'CreateSessionRequest',
'CreateStreamingSequenceRequest',
'CreateUserRequest',
'DeleteBlurbRequest',
'DeleteRoomRequest',
'DeleteSessionRequest',
'DeleteTestRequest',
'DeleteUserRequest',
'EchoClient',
'EchoErrorDetailsRequest',
'EchoErrorDetailsResponse',
'EchoRequest',
'EchoResponse',
'ErrorWithMultipleDetails',
'ErrorWithSingleDetail',
'ExpandRequest',
'FailEchoWithDetailsRequest',
'FailEchoWithDetailsResponse',
'GetBlurbRequest',
'GetRoomRequest',
'GetSequenceReportRequest',
'GetSessionRequest',
'GetStreamingSequenceReportRequest',
'GetUserRequest',
'IdentityClient',
'Issue',
'ListBlurbsRequest',
'ListBlurbsResponse',
'ListRoomsRequest',
'ListRoomsResponse',
'ListSessionsRequest',
'ListSessionsResponse',
'ListTestsRequest',
'ListTestsResponse',
'ListUsersRequest',
'ListUsersResponse',
'MessagingClient',
'PagedExpandLegacyMappedResponse',
'PagedExpandLegacyRequest',
'PagedExpandRequest',
'PagedExpandResponse',
'PagedExpandResponseList',
'PoetryError',
'ReportSessionRequest',
'ReportSessionResponse',
'RestError',
'ResumableUploadServiceClient',
'Room',
'SearchBlurbsMetadata',
'SearchBlurbsRequest',
'SearchBlurbsResponse',
'SendBlurbsResponse',
'Sequence',
'SequenceReport',
'SequenceServiceClient',
'Session',
'Severity',
'StreamBlurbsRequest',
'StreamBlurbsResponse',
'StreamingSequence',
'StreamingSequenceReport',
'Test',
'TestRun',
'TestingClient',
'UpdateBlurbRequest',
'UpdateRoomRequest',
'UpdateUserRequest',
'UploadMediaRequest',
'UploadMediaResponse',
'User',
'VerifyTestRequest',
'VerifyTestResponse',
'WaitMetadata',
'WaitRequest',
'WaitResponse',
)

api_core.check_python_version("google.showcase_v1beta1")
api_core.check_dependency_versions("google.showcase_v1beta1")
