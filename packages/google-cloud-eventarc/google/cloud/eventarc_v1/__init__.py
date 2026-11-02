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

from google.cloud.eventarc_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.eventarc_v1.services.eventarc",
    "google.cloud.eventarc_v1.types.channel",
    "google.cloud.eventarc_v1.types.channel_connection",
    "google.cloud.eventarc_v1.types.discovery",
    "google.cloud.eventarc_v1.types.enrollment",
    "google.cloud.eventarc_v1.types.eventarc",
    "google.cloud.eventarc_v1.types.google_api_source",
    "google.cloud.eventarc_v1.types.google_channel_config",
    "google.cloud.eventarc_v1.types.logging_config",
    "google.cloud.eventarc_v1.types.message_bus",
    "google.cloud.eventarc_v1.types.network_config",
    "google.cloud.eventarc_v1.types.pipeline",
    "google.cloud.eventarc_v1.types.trigger",
}


from .services.eventarc import EventarcAsyncClient, EventarcClient
from .types.channel import Channel
from .types.channel_connection import ChannelConnection
from .types.discovery import EventType, FilteringAttribute, Provider
from .types.enrollment import Enrollment
from .types.eventarc import (
    CreateChannelConnectionRequest,
    CreateChannelRequest,
    CreateEnrollmentRequest,
    CreateGoogleApiSourceRequest,
    CreateMessageBusRequest,
    CreatePipelineRequest,
    CreateTriggerRequest,
    DeleteChannelConnectionRequest,
    DeleteChannelRequest,
    DeleteEnrollmentRequest,
    DeleteGoogleApiSourceRequest,
    DeleteMessageBusRequest,
    DeletePipelineRequest,
    DeleteTriggerRequest,
    GetChannelConnectionRequest,
    GetChannelRequest,
    GetEnrollmentRequest,
    GetGoogleApiSourceRequest,
    GetGoogleChannelConfigRequest,
    GetMessageBusRequest,
    GetPipelineRequest,
    GetProviderRequest,
    GetTriggerRequest,
    ListChannelConnectionsRequest,
    ListChannelConnectionsResponse,
    ListChannelsRequest,
    ListChannelsResponse,
    ListEnrollmentsRequest,
    ListEnrollmentsResponse,
    ListGoogleApiSourcesRequest,
    ListGoogleApiSourcesResponse,
    ListMessageBusEnrollmentsRequest,
    ListMessageBusEnrollmentsResponse,
    ListMessageBusesRequest,
    ListMessageBusesResponse,
    ListPipelinesRequest,
    ListPipelinesResponse,
    ListProvidersRequest,
    ListProvidersResponse,
    ListTriggersRequest,
    ListTriggersResponse,
    OperationMetadata,
    UpdateChannelRequest,
    UpdateEnrollmentRequest,
    UpdateGoogleApiSourceRequest,
    UpdateGoogleChannelConfigRequest,
    UpdateMessageBusRequest,
    UpdatePipelineRequest,
    UpdateTriggerRequest,
)
from .types.google_api_source import GoogleApiSource
from .types.google_channel_config import GoogleChannelConfig
from .types.logging_config import LoggingConfig
from .types.message_bus import MessageBus
from .types.network_config import NetworkConfig
from .types.pipeline import Pipeline
from .types.trigger import (
    GKE,
    CloudRun,
    Destination,
    EventFilter,
    HttpEndpoint,
    Pubsub,
    StateCondition,
    Transport,
    Trigger,
)

__all__ = (
    "EventarcAsyncClient",
    "Channel",
    "ChannelConnection",
    "CloudRun",
    "CreateChannelConnectionRequest",
    "CreateChannelRequest",
    "CreateEnrollmentRequest",
    "CreateGoogleApiSourceRequest",
    "CreateMessageBusRequest",
    "CreatePipelineRequest",
    "CreateTriggerRequest",
    "DeleteChannelConnectionRequest",
    "DeleteChannelRequest",
    "DeleteEnrollmentRequest",
    "DeleteGoogleApiSourceRequest",
    "DeleteMessageBusRequest",
    "DeletePipelineRequest",
    "DeleteTriggerRequest",
    "Destination",
    "Enrollment",
    "EventFilter",
    "EventType",
    "EventarcClient",
    "FilteringAttribute",
    "GKE",
    "GetChannelConnectionRequest",
    "GetChannelRequest",
    "GetEnrollmentRequest",
    "GetGoogleApiSourceRequest",
    "GetGoogleChannelConfigRequest",
    "GetMessageBusRequest",
    "GetPipelineRequest",
    "GetProviderRequest",
    "GetTriggerRequest",
    "GoogleApiSource",
    "GoogleChannelConfig",
    "HttpEndpoint",
    "ListChannelConnectionsRequest",
    "ListChannelConnectionsResponse",
    "ListChannelsRequest",
    "ListChannelsResponse",
    "ListEnrollmentsRequest",
    "ListEnrollmentsResponse",
    "ListGoogleApiSourcesRequest",
    "ListGoogleApiSourcesResponse",
    "ListMessageBusEnrollmentsRequest",
    "ListMessageBusEnrollmentsResponse",
    "ListMessageBusesRequest",
    "ListMessageBusesResponse",
    "ListPipelinesRequest",
    "ListPipelinesResponse",
    "ListProvidersRequest",
    "ListProvidersResponse",
    "ListTriggersRequest",
    "ListTriggersResponse",
    "LoggingConfig",
    "MessageBus",
    "NetworkConfig",
    "OperationMetadata",
    "Pipeline",
    "Provider",
    "Pubsub",
    "StateCondition",
    "Transport",
    "Trigger",
    "UpdateChannelRequest",
    "UpdateEnrollmentRequest",
    "UpdateGoogleApiSourceRequest",
    "UpdateGoogleChannelConfigRequest",
    "UpdateMessageBusRequest",
    "UpdatePipelineRequest",
    "UpdateTriggerRequest",
)

api_core.check_python_version("google.cloud.eventarc_v1")
api_core.check_dependency_versions("google.cloud.eventarc_v1")
