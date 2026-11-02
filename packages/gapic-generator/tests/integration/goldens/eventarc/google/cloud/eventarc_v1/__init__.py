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
from google.cloud.eventarc_v1 import gapic_version as package_version

import google.api_core as api_core

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


from .services.eventarc import EventarcClient
from .services.eventarc import EventarcAsyncClient

from .types.channel import Channel
from .types.channel_connection import ChannelConnection
from .types.discovery import EventType
from .types.discovery import FilteringAttribute
from .types.discovery import Provider
from .types.enrollment import Enrollment
from .types.eventarc import CreateChannelConnectionRequest
from .types.eventarc import CreateChannelRequest
from .types.eventarc import CreateEnrollmentRequest
from .types.eventarc import CreateGoogleApiSourceRequest
from .types.eventarc import CreateMessageBusRequest
from .types.eventarc import CreatePipelineRequest
from .types.eventarc import CreateTriggerRequest
from .types.eventarc import DeleteChannelConnectionRequest
from .types.eventarc import DeleteChannelRequest
from .types.eventarc import DeleteEnrollmentRequest
from .types.eventarc import DeleteGoogleApiSourceRequest
from .types.eventarc import DeleteMessageBusRequest
from .types.eventarc import DeletePipelineRequest
from .types.eventarc import DeleteTriggerRequest
from .types.eventarc import GetChannelConnectionRequest
from .types.eventarc import GetChannelRequest
from .types.eventarc import GetEnrollmentRequest
from .types.eventarc import GetGoogleApiSourceRequest
from .types.eventarc import GetGoogleChannelConfigRequest
from .types.eventarc import GetMessageBusRequest
from .types.eventarc import GetPipelineRequest
from .types.eventarc import GetProviderRequest
from .types.eventarc import GetTriggerRequest
from .types.eventarc import ListChannelConnectionsRequest
from .types.eventarc import ListChannelConnectionsResponse
from .types.eventarc import ListChannelsRequest
from .types.eventarc import ListChannelsResponse
from .types.eventarc import ListEnrollmentsRequest
from .types.eventarc import ListEnrollmentsResponse
from .types.eventarc import ListGoogleApiSourcesRequest
from .types.eventarc import ListGoogleApiSourcesResponse
from .types.eventarc import ListMessageBusEnrollmentsRequest
from .types.eventarc import ListMessageBusEnrollmentsResponse
from .types.eventarc import ListMessageBusesRequest
from .types.eventarc import ListMessageBusesResponse
from .types.eventarc import ListPipelinesRequest
from .types.eventarc import ListPipelinesResponse
from .types.eventarc import ListProvidersRequest
from .types.eventarc import ListProvidersResponse
from .types.eventarc import ListTriggersRequest
from .types.eventarc import ListTriggersResponse
from .types.eventarc import OperationMetadata
from .types.eventarc import UpdateChannelRequest
from .types.eventarc import UpdateEnrollmentRequest
from .types.eventarc import UpdateGoogleApiSourceRequest
from .types.eventarc import UpdateGoogleChannelConfigRequest
from .types.eventarc import UpdateMessageBusRequest
from .types.eventarc import UpdatePipelineRequest
from .types.eventarc import UpdateTriggerRequest
from .types.google_api_source import GoogleApiSource
from .types.google_channel_config import GoogleChannelConfig
from .types.logging_config import LoggingConfig
from .types.message_bus import MessageBus
from .types.network_config import NetworkConfig
from .types.pipeline import Pipeline
from .types.trigger import CloudRun
from .types.trigger import Destination
from .types.trigger import EventFilter
from .types.trigger import GKE
from .types.trigger import HttpEndpoint
from .types.trigger import Pubsub
from .types.trigger import StateCondition
from .types.trigger import Transport
from .types.trigger import Trigger

__all__ = (
    'EventarcAsyncClient',
'Channel',
'ChannelConnection',
'CloudRun',
'CreateChannelConnectionRequest',
'CreateChannelRequest',
'CreateEnrollmentRequest',
'CreateGoogleApiSourceRequest',
'CreateMessageBusRequest',
'CreatePipelineRequest',
'CreateTriggerRequest',
'DeleteChannelConnectionRequest',
'DeleteChannelRequest',
'DeleteEnrollmentRequest',
'DeleteGoogleApiSourceRequest',
'DeleteMessageBusRequest',
'DeletePipelineRequest',
'DeleteTriggerRequest',
'Destination',
'Enrollment',
'EventFilter',
'EventType',
'EventarcClient',
'FilteringAttribute',
'GKE',
'GetChannelConnectionRequest',
'GetChannelRequest',
'GetEnrollmentRequest',
'GetGoogleApiSourceRequest',
'GetGoogleChannelConfigRequest',
'GetMessageBusRequest',
'GetPipelineRequest',
'GetProviderRequest',
'GetTriggerRequest',
'GoogleApiSource',
'GoogleChannelConfig',
'HttpEndpoint',
'ListChannelConnectionsRequest',
'ListChannelConnectionsResponse',
'ListChannelsRequest',
'ListChannelsResponse',
'ListEnrollmentsRequest',
'ListEnrollmentsResponse',
'ListGoogleApiSourcesRequest',
'ListGoogleApiSourcesResponse',
'ListMessageBusEnrollmentsRequest',
'ListMessageBusEnrollmentsResponse',
'ListMessageBusesRequest',
'ListMessageBusesResponse',
'ListPipelinesRequest',
'ListPipelinesResponse',
'ListProvidersRequest',
'ListProvidersResponse',
'ListTriggersRequest',
'ListTriggersResponse',
'LoggingConfig',
'MessageBus',
'NetworkConfig',
'OperationMetadata',
'Pipeline',
'Provider',
'Pubsub',
'StateCondition',
'Transport',
'Trigger',
'UpdateChannelRequest',
'UpdateEnrollmentRequest',
'UpdateGoogleApiSourceRequest',
'UpdateGoogleChannelConfigRequest',
'UpdateMessageBusRequest',
'UpdatePipelineRequest',
'UpdateTriggerRequest',
)

api_core.check_python_version("google.cloud.eventarc_v1")
api_core.check_dependency_versions("google.cloud.eventarc_v1")
