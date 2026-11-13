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
# Generated code. DO NOT EDIT!
#
# Snippet for IngestAdEvents
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-ads-datamanager


# [START datamanager_v1_generated_IngestionService_IngestAdEvents_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.ads import datamanager_v1


def sample_ingest_ad_events():
    # Create a client
    client = datamanager_v1.IngestionServiceClient()

    # Initialize request argument(s)
    ad_events = datamanager_v1.AdEvent()
    ad_events.event_subtype = "EVENT_SUBTYPE_OUTBOUND_CLICK"
    ad_events.ad_type = "AD_TYPE_VIDEO"
    ad_events.ad_format = "AD_FORMAT_VIDEO"
    ad_events.ad_placement = "AD_PLACEMENT_STORY"
    ad_events.targeting_type = "TARGETING_TYPE_REMARKETING"
    ad_events.platform_type = "PLATFORM_TYPE_TABLET"
    ad_events.platform = "PLATFORM_WEB"
    ad_events.advertiser_id = "advertiser_id_value"
    ad_events.event_type = "EVENT_TYPE_CLICK"
    ad_events.campaign_id = "campaign_id_value"
    ad_events.campaign_name = "campaign_name_value"
    ad_events.source = "source_value"
    ad_events.medium = "medium_value"
    ad_events.viewability_info.view_type = "VIEW_TYPE_MRC_RENDERED"

    request = datamanager_v1.IngestAdEventsRequest(
        ad_events=ad_events,
    )

    # Make the request
    response = client.ingest_ad_events(request=request)

    # Handle the response
    print(response)


# [END datamanager_v1_generated_IngestionService_IngestAdEvents_sync]
