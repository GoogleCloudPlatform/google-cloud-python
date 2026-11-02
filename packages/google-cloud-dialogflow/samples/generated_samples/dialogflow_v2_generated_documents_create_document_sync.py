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
# Snippet for CreateDocument
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2_generated_Documents_CreateDocument_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import dialogflow_v2


def sample_create_document():
    # Create a client
    client = dialogflow_v2.DocumentsClient()

    # Initialize request argument(s)
    document = dialogflow_v2.Document()
    document.content_uri = "content_uri_value"
    document.display_name = "display_name_value"
    document.mime_type = "mime_type_value"
    document.knowledge_types = ["AGENT_FACING_SMART_REPLY"]

    request = dialogflow_v2.CreateDocumentRequest(
        parent="parent_value",
        document=document,
    )

    # Make the request
    operation = client.create_document(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END dialogflow_v2_generated_Documents_CreateDocument_sync]
