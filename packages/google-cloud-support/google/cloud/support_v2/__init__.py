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

from google.cloud.support_v2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.support_v2.services.case_attachment_service",
    "google.cloud.support_v2.services.case_service",
    "google.cloud.support_v2.services.comment_service",
    "google.cloud.support_v2.services.support_event_subscription_service",
    "google.cloud.support_v2.types.actor",
    "google.cloud.support_v2.types.attachment",
    "google.cloud.support_v2.types.attachment_service",
    "google.cloud.support_v2.types.case",
    "google.cloud.support_v2.types.case_service",
    "google.cloud.support_v2.types.comment",
    "google.cloud.support_v2.types.comment_service",
    "google.cloud.support_v2.types.escalation",
    "google.cloud.support_v2.types.support_event_subscription",
    "google.cloud.support_v2.types.support_event_subscription_service",
}


from .services.case_attachment_service import (
    CaseAttachmentServiceAsyncClient,
    CaseAttachmentServiceClient,
)
from .services.case_service import CaseServiceAsyncClient, CaseServiceClient
from .services.comment_service import CommentServiceAsyncClient, CommentServiceClient
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
from .types.case import Case, CaseClassification
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
from .types.escalation import Escalation
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
    "EscalateCaseRequest",
    "Escalation",
    "ExpungeSupportEventSubscriptionRequest",
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
    "SearchCaseClassificationsRequest",
    "SearchCaseClassificationsResponse",
    "SearchCasesRequest",
    "SearchCasesResponse",
    "SupportEventSubscription",
    "SupportEventSubscriptionServiceClient",
    "UndeleteSupportEventSubscriptionRequest",
    "UpdateCaseRequest",
    "UpdateSupportEventSubscriptionRequest",
)

api_core.check_python_version("google.cloud.support_v2")
api_core.check_dependency_versions("google.cloud.support_v2")
