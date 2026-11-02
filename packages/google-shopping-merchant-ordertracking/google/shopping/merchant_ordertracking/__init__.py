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
from google.shopping.merchant_ordertracking import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_ordertracking_v1.services.order_tracking_signals_service.async_client import (
    OrderTrackingSignalsServiceAsyncClient,
)
from google.shopping.merchant_ordertracking_v1.services.order_tracking_signals_service.client import (
    OrderTrackingSignalsServiceClient,
)
from google.shopping.merchant_ordertracking_v1.types.order_tracking_signals import (
    CreateOrderTrackingSignalRequest,
    OrderTrackingSignal,
)

__all__ = (
    "OrderTrackingSignalsServiceClient",
    "OrderTrackingSignalsServiceAsyncClient",
    "CreateOrderTrackingSignalRequest",
    "OrderTrackingSignal",
)
