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
# Snippet for Publish
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-eventarc-publishing


# [START eventarcpublishing_v1_generated_Publisher_Publish_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import eventarc_publishing_v1


def sample_publish():
    # Create a client
    client = eventarc_publishing_v1.PublisherClient()

    # Initialize request argument(s)
    proto_message = eventarc_publishing_v1.CloudEvent()
    proto_message.binary_data = b"binary_data_blob"
    proto_message.id = "id_value"
    proto_message.source = "source_value"
    proto_message.spec_version = "spec_version_value"
    proto_message.type_ = "type__value"

    request = eventarc_publishing_v1.PublishRequest(
        proto_message=proto_message,
        message_bus="message_bus_value",
    )

    # Make the request
    response = client.publish(request=request)

    # Handle the response
    print(response)


# [END eventarcpublishing_v1_generated_Publisher_Publish_sync]
