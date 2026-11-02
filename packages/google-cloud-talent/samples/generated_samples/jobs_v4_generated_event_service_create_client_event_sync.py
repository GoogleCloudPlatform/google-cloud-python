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
# Snippet for CreateClientEvent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-talent


# [START jobs_v4_generated_EventService_CreateClientEvent_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import talent_v4


def sample_create_client_event():
    # Create a client
    client = talent_v4.EventServiceClient()

    # Initialize request argument(s)
    client_event = talent_v4.ClientEvent()
    client_event.job_event.type_ = "INTERVIEW_GRANTED"
    client_event.job_event.jobs = ["jobs_value1", "jobs_value2"]
    client_event.event_id = "event_id_value"

    request = talent_v4.CreateClientEventRequest(
        parent="parent_value",
        client_event=client_event,
    )

    # Make the request
    response = client.create_client_event(request=request)

    # Handle the response
    print(response)


# [END jobs_v4_generated_EventService_CreateClientEvent_sync]
