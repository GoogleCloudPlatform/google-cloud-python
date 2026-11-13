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
from google.cloud.devicestreaming import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.devicestreaming_v1.services.direct_access_service.async_client import (
    DirectAccessServiceAsyncClient,
)
from google.cloud.devicestreaming_v1.services.direct_access_service.client import (
    DirectAccessServiceClient,
)
from google.cloud.devicestreaming_v1.types.adb_service import (
    AdbMessage,
    Close,
    DeviceMessage,
    Fail,
    Okay,
    Open,
    StatusUpdate,
    StreamData,
    StreamStatus,
)
from google.cloud.devicestreaming_v1.types.service import (
    AndroidDevice,
    CancelDeviceSessionRequest,
    ClientInfo,
    CreateDeviceSessionRequest,
    DeviceSession,
    GetDeviceSessionRequest,
    ListDeviceSessionsRequest,
    ListDeviceSessionsResponse,
    UpdateDeviceSessionRequest,
)

__all__ = (
    "DirectAccessServiceClient",
    "DirectAccessServiceAsyncClient",
    "AdbMessage",
    "Close",
    "DeviceMessage",
    "Fail",
    "Okay",
    "Open",
    "StatusUpdate",
    "StreamData",
    "StreamStatus",
    "AndroidDevice",
    "CancelDeviceSessionRequest",
    "ClientInfo",
    "CreateDeviceSessionRequest",
    "DeviceSession",
    "GetDeviceSessionRequest",
    "ListDeviceSessionsRequest",
    "ListDeviceSessionsResponse",
    "UpdateDeviceSessionRequest",
)
