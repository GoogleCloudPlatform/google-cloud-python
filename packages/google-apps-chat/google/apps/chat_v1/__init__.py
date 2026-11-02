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

from google.apps.chat_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.apps.chat_v1.services.chat_service",
    "google.apps.chat_v1.types.action_status",
    "google.apps.chat_v1.types.annotation",
    "google.apps.chat_v1.types.app_command_metadata",
    "google.apps.chat_v1.types.attachment",
    "google.apps.chat_v1.types.audience",
    "google.apps.chat_v1.types.availability",
    "google.apps.chat_v1.types.chat_service",
    "google.apps.chat_v1.types.contextual_addon",
    "google.apps.chat_v1.types.deletion_metadata",
    "google.apps.chat_v1.types.event_payload",
    "google.apps.chat_v1.types.group",
    "google.apps.chat_v1.types.history_state",
    "google.apps.chat_v1.types.markup_syntax",
    "google.apps.chat_v1.types.matched_url",
    "google.apps.chat_v1.types.membership",
    "google.apps.chat_v1.types.message",
    "google.apps.chat_v1.types.message_pin",
    "google.apps.chat_v1.types.reaction",
    "google.apps.chat_v1.types.section",
    "google.apps.chat_v1.types.slash_command",
    "google.apps.chat_v1.types.space",
    "google.apps.chat_v1.types.space_event",
    "google.apps.chat_v1.types.space_notification_setting",
    "google.apps.chat_v1.types.space_read_state",
    "google.apps.chat_v1.types.space_setup",
    "google.apps.chat_v1.types.thread_read_state",
    "google.apps.chat_v1.types.user",
    "google.apps.chat_v1.types.widgets",
}


from .services.chat_service import ChatServiceAsyncClient, ChatServiceClient
from .types.action_status import ActionStatus
from .types.annotation import (
    Annotation,
    AnnotationType,
    CalendarEventLinkData,
    ChatSpaceLinkData,
    CustomEmojiMetadata,
    DriveLinkData,
    MeetSpaceLinkData,
    RichLinkMetadata,
    SlashCommandMetadata,
    UserMentionMetadata,
)
from .types.app_command_metadata import AppCommandMetadata
from .types.attachment import (
    Attachment,
    AttachmentDataRef,
    DriveDataRef,
    GetAttachmentRequest,
    UploadAttachmentRequest,
    UploadAttachmentResponse,
)
from .types.audience import Audience
from .types.availability import (
    Availability,
    CustomStatus,
    DoNotDisturbMetadata,
    GetAvailabilityRequest,
    MarkAsActiveRequest,
    MarkAsAwayRequest,
    MarkAsDoNotDisturbRequest,
    UpdateAvailabilityRequest,
)
from .types.contextual_addon import ContextualAddOnMarkup
from .types.deletion_metadata import DeletionMetadata
from .types.event_payload import (
    MembershipBatchCreatedEventData,
    MembershipBatchDeletedEventData,
    MembershipBatchUpdatedEventData,
    MembershipCreatedEventData,
    MembershipDeletedEventData,
    MembershipUpdatedEventData,
    MessageBatchCreatedEventData,
    MessageBatchDeletedEventData,
    MessageBatchUpdatedEventData,
    MessageCreatedEventData,
    MessageDeletedEventData,
    MessageUpdatedEventData,
    ReactionBatchCreatedEventData,
    ReactionBatchDeletedEventData,
    ReactionCreatedEventData,
    ReactionDeletedEventData,
    SpaceBatchUpdatedEventData,
    SpaceUpdatedEventData,
)
from .types.group import Group
from .types.history_state import HistoryState
from .types.markup_syntax import MarkupSyntax
from .types.matched_url import MatchedUrl
from .types.membership import (
    CreateMembershipRequest,
    DeleteMembershipRequest,
    GetMembershipRequest,
    ListMembershipsRequest,
    ListMembershipsResponse,
    Membership,
    UpdateMembershipRequest,
)
from .types.message import (
    AccessoryWidget,
    ActionResponse,
    AttachedGif,
    CardWithId,
    CreateMessageNotificationOptions,
    CreateMessageRequest,
    DeleteMessageRequest,
    Dialog,
    DialogAction,
    ForwardedMetadata,
    GetMessageRequest,
    ListMessagesRequest,
    ListMessagesResponse,
    Message,
    QuotedMessageMetadata,
    QuotedMessageSnapshot,
    ReplaceMessageCardsRequest,
    ReplaceMessageCardsResponse,
    SearchMessageResult,
    SearchMessagesRequest,
    SearchMessagesResponse,
    Thread,
    UpdateMessageRequest,
)
from .types.message_pin import (
    CreateMessagePinRequest,
    DeleteMessagePinRequest,
    ListMessagePinsRequest,
    ListMessagePinsResponse,
    MessagePin,
)
from .types.reaction import (
    CreateCustomEmojiRequest,
    CreateReactionRequest,
    CustomEmoji,
    DeleteCustomEmojiRequest,
    DeleteReactionRequest,
    Emoji,
    EmojiReactionSummary,
    GetCustomEmojiRequest,
    ListCustomEmojisRequest,
    ListCustomEmojisResponse,
    ListReactionsRequest,
    ListReactionsResponse,
    Reaction,
)
from .types.section import (
    CreateSectionRequest,
    DeleteSectionRequest,
    ListSectionItemsRequest,
    ListSectionItemsResponse,
    ListSectionsRequest,
    ListSectionsResponse,
    MoveSectionItemRequest,
    MoveSectionItemResponse,
    PositionSectionRequest,
    PositionSectionResponse,
    Section,
    SectionItem,
    UpdateSectionRequest,
)
from .types.slash_command import SlashCommand
from .types.space import (
    CompleteImportSpaceRequest,
    CompleteImportSpaceResponse,
    CreateSpaceRequest,
    DeleteSpaceRequest,
    FindDirectMessageRequest,
    FindGroupChatsRequest,
    FindGroupChatsResponse,
    GetSpaceRequest,
    ListSpacesRequest,
    ListSpacesResponse,
    SearchSpacesRequest,
    SearchSpacesResponse,
    Space,
    SpaceView,
    UpdateSpaceRequest,
)
from .types.space_event import (
    GetSpaceEventRequest,
    ListSpaceEventsRequest,
    ListSpaceEventsResponse,
    SpaceEvent,
)
from .types.space_notification_setting import (
    GetSpaceNotificationSettingRequest,
    SpaceNotificationSetting,
    UpdateSpaceNotificationSettingRequest,
)
from .types.space_read_state import (
    GetSpaceReadStateRequest,
    SpaceReadState,
    UpdateSpaceReadStateRequest,
)
from .types.space_setup import SetUpSpaceRequest
from .types.thread_read_state import GetThreadReadStateRequest, ThreadReadState
from .types.user import User
from .types.widgets import WidgetMarkup

__all__ = (
    "ChatServiceAsyncClient",
    "AccessoryWidget",
    "ActionResponse",
    "ActionStatus",
    "Annotation",
    "AnnotationType",
    "AppCommandMetadata",
    "AttachedGif",
    "Attachment",
    "AttachmentDataRef",
    "Audience",
    "Availability",
    "CalendarEventLinkData",
    "CardWithId",
    "ChatServiceClient",
    "ChatSpaceLinkData",
    "CompleteImportSpaceRequest",
    "CompleteImportSpaceResponse",
    "ContextualAddOnMarkup",
    "CreateCustomEmojiRequest",
    "CreateMembershipRequest",
    "CreateMessageNotificationOptions",
    "CreateMessagePinRequest",
    "CreateMessageRequest",
    "CreateReactionRequest",
    "CreateSectionRequest",
    "CreateSpaceRequest",
    "CustomEmoji",
    "CustomEmojiMetadata",
    "CustomStatus",
    "DeleteCustomEmojiRequest",
    "DeleteMembershipRequest",
    "DeleteMessagePinRequest",
    "DeleteMessageRequest",
    "DeleteReactionRequest",
    "DeleteSectionRequest",
    "DeleteSpaceRequest",
    "DeletionMetadata",
    "Dialog",
    "DialogAction",
    "DoNotDisturbMetadata",
    "DriveDataRef",
    "DriveLinkData",
    "Emoji",
    "EmojiReactionSummary",
    "FindDirectMessageRequest",
    "FindGroupChatsRequest",
    "FindGroupChatsResponse",
    "ForwardedMetadata",
    "GetAttachmentRequest",
    "GetAvailabilityRequest",
    "GetCustomEmojiRequest",
    "GetMembershipRequest",
    "GetMessageRequest",
    "GetSpaceEventRequest",
    "GetSpaceNotificationSettingRequest",
    "GetSpaceReadStateRequest",
    "GetSpaceRequest",
    "GetThreadReadStateRequest",
    "Group",
    "HistoryState",
    "ListCustomEmojisRequest",
    "ListCustomEmojisResponse",
    "ListMembershipsRequest",
    "ListMembershipsResponse",
    "ListMessagePinsRequest",
    "ListMessagePinsResponse",
    "ListMessagesRequest",
    "ListMessagesResponse",
    "ListReactionsRequest",
    "ListReactionsResponse",
    "ListSectionItemsRequest",
    "ListSectionItemsResponse",
    "ListSectionsRequest",
    "ListSectionsResponse",
    "ListSpaceEventsRequest",
    "ListSpaceEventsResponse",
    "ListSpacesRequest",
    "ListSpacesResponse",
    "MarkAsActiveRequest",
    "MarkAsAwayRequest",
    "MarkAsDoNotDisturbRequest",
    "MarkupSyntax",
    "MatchedUrl",
    "MeetSpaceLinkData",
    "Membership",
    "MembershipBatchCreatedEventData",
    "MembershipBatchDeletedEventData",
    "MembershipBatchUpdatedEventData",
    "MembershipCreatedEventData",
    "MembershipDeletedEventData",
    "MembershipUpdatedEventData",
    "Message",
    "MessageBatchCreatedEventData",
    "MessageBatchDeletedEventData",
    "MessageBatchUpdatedEventData",
    "MessageCreatedEventData",
    "MessageDeletedEventData",
    "MessagePin",
    "MessageUpdatedEventData",
    "MoveSectionItemRequest",
    "MoveSectionItemResponse",
    "PositionSectionRequest",
    "PositionSectionResponse",
    "QuotedMessageMetadata",
    "QuotedMessageSnapshot",
    "Reaction",
    "ReactionBatchCreatedEventData",
    "ReactionBatchDeletedEventData",
    "ReactionCreatedEventData",
    "ReactionDeletedEventData",
    "ReplaceMessageCardsRequest",
    "ReplaceMessageCardsResponse",
    "RichLinkMetadata",
    "SearchMessageResult",
    "SearchMessagesRequest",
    "SearchMessagesResponse",
    "SearchSpacesRequest",
    "SearchSpacesResponse",
    "Section",
    "SectionItem",
    "SetUpSpaceRequest",
    "SlashCommand",
    "SlashCommandMetadata",
    "Space",
    "SpaceBatchUpdatedEventData",
    "SpaceEvent",
    "SpaceNotificationSetting",
    "SpaceReadState",
    "SpaceUpdatedEventData",
    "SpaceView",
    "Thread",
    "ThreadReadState",
    "UpdateAvailabilityRequest",
    "UpdateMembershipRequest",
    "UpdateMessageRequest",
    "UpdateSectionRequest",
    "UpdateSpaceNotificationSettingRequest",
    "UpdateSpaceReadStateRequest",
    "UpdateSpaceRequest",
    "UploadAttachmentRequest",
    "UploadAttachmentResponse",
    "User",
    "UserMentionMetadata",
    "WidgetMarkup",
)

api_core.check_python_version("google.apps.chat_v1")
api_core.check_dependency_versions("google.apps.chat_v1")
