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
from google.cloud.support import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.support_v2.services.case_attachment_service.async_client import (
    CaseAttachmentServiceAsyncClient,
)
from google.cloud.support_v2.services.case_attachment_service.client import (
    CaseAttachmentServiceClient,
)
from google.cloud.support_v2.services.case_service.async_client import (
    CaseServiceAsyncClient,
)
from google.cloud.support_v2.services.case_service.client import CaseServiceClient
from google.cloud.support_v2.services.comment_service.async_client import (
    CommentServiceAsyncClient,
)
from google.cloud.support_v2.services.comment_service.client import CommentServiceClient
from google.cloud.support_v2.services.support_event_subscription_service.async_client import (
    SupportEventSubscriptionServiceAsyncClient,
)
from google.cloud.support_v2.services.support_event_subscription_service.client import (
    SupportEventSubscriptionServiceClient,
)
from google.cloud.support_v2.types.actor import Actor
from google.cloud.support_v2.types.attachment import Attachment
from google.cloud.support_v2.types.attachment_service import (
    GetAttachmentRequest,
    ListAttachmentsRequest,
    ListAttachmentsResponse,
)
from google.cloud.support_v2.types.case import Case, CaseClassification
from google.cloud.support_v2.types.case_service import (
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
from google.cloud.support_v2.types.comment import Comment
from google.cloud.support_v2.types.comment_service import (
    CreateCommentRequest,
    GetCommentRequest,
    ListCommentsRequest,
    ListCommentsResponse,
)
from google.cloud.support_v2.types.escalation import Escalation
from google.cloud.support_v2.types.support_event_subscription import (
    SupportEventSubscription,
)
from google.cloud.support_v2.types.support_event_subscription_service import (
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
    "CaseAttachmentServiceClient",
    "CaseAttachmentServiceAsyncClient",
    "CaseServiceClient",
    "CaseServiceAsyncClient",
    "CommentServiceClient",
    "CommentServiceAsyncClient",
    "SupportEventSubscriptionServiceClient",
    "SupportEventSubscriptionServiceAsyncClient",
    "Actor",
    "Attachment",
    "GetAttachmentRequest",
    "ListAttachmentsRequest",
    "ListAttachmentsResponse",
    "Case",
    "CaseClassification",
    "CloseCaseRequest",
    "CreateCaseRequest",
    "EscalateCaseRequest",
    "GetCaseRequest",
    "ListCasesRequest",
    "ListCasesResponse",
    "SearchCaseClassificationsRequest",
    "SearchCaseClassificationsResponse",
    "SearchCasesRequest",
    "SearchCasesResponse",
    "UpdateCaseRequest",
    "Comment",
    "CreateCommentRequest",
    "GetCommentRequest",
    "ListCommentsRequest",
    "ListCommentsResponse",
    "Escalation",
    "SupportEventSubscription",
    "CreateSupportEventSubscriptionRequest",
    "DeleteSupportEventSubscriptionRequest",
    "ExpungeSupportEventSubscriptionRequest",
    "GetSupportEventSubscriptionRequest",
    "ListSupportEventSubscriptionsRequest",
    "ListSupportEventSubscriptionsResponse",
    "UndeleteSupportEventSubscriptionRequest",
    "UpdateSupportEventSubscriptionRequest",
)
