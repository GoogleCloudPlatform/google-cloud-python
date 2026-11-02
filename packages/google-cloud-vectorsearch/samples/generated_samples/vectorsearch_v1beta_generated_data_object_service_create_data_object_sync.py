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
# Snippet for CreateDataObject
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vectorsearch


# [START vectorsearch_v1beta_generated_DataObjectService_CreateDataObject_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import vectorsearch_v1beta


def sample_create_data_object():
    # Create a client
    client = vectorsearch_v1beta.DataObjectServiceClient()

    # Initialize request argument(s)
    request = vectorsearch_v1beta.CreateDataObjectRequest(
        parent="parent_value",
        data_object_id="data_object_id_value",
    )

    # Make the request
    response = client.create_data_object(request=request)

    # Handle the response
    print(response)


# [END vectorsearch_v1beta_generated_DataObjectService_CreateDataObject_sync]
