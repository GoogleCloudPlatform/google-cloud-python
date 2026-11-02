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
from google.shopping.merchant_notifications import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_notifications_v1.services.notifications_api_service.async_client import (
    NotificationsApiServiceAsyncClient,
)
from google.shopping.merchant_notifications_v1.services.notifications_api_service.client import (
    NotificationsApiServiceClient,
)
from google.shopping.merchant_notifications_v1.types.notificationsapi import (
    CreateNotificationSubscriptionRequest,
    DeleteNotificationSubscriptionRequest,
    GetNotificationSubscriptionHealthMetricsRequest,
    GetNotificationSubscriptionRequest,
    ListNotificationSubscriptionsRequest,
    ListNotificationSubscriptionsResponse,
    NotificationSubscription,
    NotificationSubscriptionHealthMetrics,
    UpdateNotificationSubscriptionRequest,
)

__all__ = (
    "NotificationsApiServiceClient",
    "NotificationsApiServiceAsyncClient",
    "CreateNotificationSubscriptionRequest",
    "DeleteNotificationSubscriptionRequest",
    "GetNotificationSubscriptionHealthMetricsRequest",
    "GetNotificationSubscriptionRequest",
    "ListNotificationSubscriptionsRequest",
    "ListNotificationSubscriptionsResponse",
    "NotificationSubscription",
    "NotificationSubscriptionHealthMetrics",
    "UpdateNotificationSubscriptionRequest",
)
