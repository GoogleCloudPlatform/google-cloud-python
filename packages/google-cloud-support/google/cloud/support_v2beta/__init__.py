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

from google.cloud.support_v2beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.support_v2beta.services.case_attachment_service",
    "google.cloud.support_v2beta.services.case_service",
    "google.cloud.support_v2beta.services.comment_service",
    "google.cloud.support_v2beta.services.feed_service",
    "google.cloud.support_v2beta.services.support_event_subscription_service",
    "google.cloud.support_v2beta.types.actor",
    "google.cloud.support_v2beta.types.attachment",
    "google.cloud.support_v2beta.types.attachment_service",
    "google.cloud.support_v2beta.types.case",
    "google.cloud.support_v2beta.types.case_service",
    "google.cloud.support_v2beta.types.comment",
    "google.cloud.support_v2beta.types.comment_service",
    "google.cloud.support_v2beta.types.content",
    "google.cloud.support_v2beta.types.email_message",
    "google.cloud.support_v2beta.types.escalation",
    "google.cloud.support_v2beta.types.feed_item",
    "google.cloud.support_v2beta.types.feed_service",
    "google.cloud.support_v2beta.types.support_event_subscription",
    "google.cloud.support_v2beta.types.support_event_subscription_service",
}


from .services.case_attachment_service import (
    CaseAttachmentServiceAsyncClient,
    CaseAttachmentServiceClient,
)
from .services.case_service import CaseServiceAsyncClient, CaseServiceClient
from .services.comment_service import CommentServiceAsyncClient, CommentServiceClient
from .services.feed_service import FeedServiceAsyncClient, FeedServiceClient
from .services.support_event_subscription_service import (
    SupportEventSubscriptionServiceAsyncClient,
    SupportEventSubscriptionServiceClient,
)
from .types.actor import Actor
from .types.attachment import Attachment
from .types.attachment_service import (
    GetAttachmentRequest,
    ListAttachmentsRequest,
    ListAttachmentsResponse,
)
from .types.case import Case, CaseClassification, Product, ProductLine
from .types.case_service import (
    CloseCaseRequest,
    CreateCaseRequest,
    EscalateCaseRequest,
    GetCaseRequest,
    ListCasesRequest,
    ListCasesResponse,
    SearchCaseClassificationsRequest,
    SearchCaseClassificationsResponse,
    SearchCasesRequest,
    SearchCasesResponse,
    UpdateCaseRequest,
)
from .types.comment import Comment
from .types.comment_service import (
    CreateCommentRequest,
    GetCommentRequest,
    ListCommentsRequest,
    ListCommentsResponse,
)
from .types.content import TextContent
from .types.email_message import EmailMessage
from .types.escalation import Escalation
from .types.feed_item import FeedItem
from .types.feed_service import ShowFeedRequest, ShowFeedResponse
from .types.support_event_subscription import SupportEventSubscription
from .types.support_event_subscription_service import (
    CreateSupportEventSubscriptionRequest,
    DeleteSupportEventSubscriptionRequest,
    ExpungeSupportEventSubscriptionRequest,
    GetSupportEventSubscriptionRequest,
    ListSupportEventSubscriptionsRequest,
    ListSupportEventSubscriptionsResponse,
    UndeleteSupportEventSubscriptionRequest,
    UpdateSupportEventSubscriptionRequest,
)

__all__ = (
    "CaseAttachmentServiceAsyncClient",
    "CaseServiceAsyncClient",
    "CommentServiceAsyncClient",
    "FeedServiceAsyncClient",
    "SupportEventSubscriptionServiceAsyncClient",
    "Actor",
    "Attachment",
    "Case",
    "CaseAttachmentServiceClient",
    "CaseClassification",
    "CaseServiceClient",
    "CloseCaseRequest",
    "Comment",
    "CommentServiceClient",
    "CreateCaseRequest",
    "CreateCommentRequest",
    "CreateSupportEventSubscriptionRequest",
    "DeleteSupportEventSubscriptionRequest",
    "EmailMessage",
    "EscalateCaseRequest",
    "Escalation",
    "ExpungeSupportEventSubscriptionRequest",
    "FeedItem",
    "FeedServiceClient",
    "GetAttachmentRequest",
    "GetCaseRequest",
    "GetCommentRequest",
    "GetSupportEventSubscriptionRequest",
    "ListAttachmentsRequest",
    "ListAttachmentsResponse",
    "ListCasesRequest",
    "ListCasesResponse",
    "ListCommentsRequest",
    "ListCommentsResponse",
    "ListSupportEventSubscriptionsRequest",
    "ListSupportEventSubscriptionsResponse",
    "Product",
    "ProductLine",
    "SearchCaseClassificationsRequest",
    "SearchCaseClassificationsResponse",
    "SearchCasesRequest",
    "SearchCasesResponse",
    "ShowFeedRequest",
    "ShowFeedResponse",
    "SupportEventSubscription",
    "SupportEventSubscriptionServiceClient",
    "TextContent",
    "UndeleteSupportEventSubscriptionRequest",
    "UpdateCaseRequest",
    "UpdateSupportEventSubscriptionRequest",
)

api_core.check_python_version("google.cloud.support_v2beta")
api_core.check_dependency_versions("google.cloud.support_v2beta")
