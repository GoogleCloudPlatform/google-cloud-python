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
# Snippet for ImportDataObjects
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vectorsearch


# [START vectorsearch_v1_generated_VectorSearchService_ImportDataObjects_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import vectorsearch_v1


def sample_import_data_objects():
    # Create a client
    client = vectorsearch_v1.VectorSearchServiceClient()

    # Initialize request argument(s)
    gcs_import = vectorsearch_v1.GcsImportConfig()
    gcs_import.contents_uri = "contents_uri_value"
    gcs_import.error_uri = "error_uri_value"

    request = vectorsearch_v1.ImportDataObjectsRequest(
        gcs_import=gcs_import,
        name="name_value",
    )

    # Make the request
    operation = client.import_data_objects(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END vectorsearch_v1_generated_VectorSearchService_ImportDataObjects_sync]
