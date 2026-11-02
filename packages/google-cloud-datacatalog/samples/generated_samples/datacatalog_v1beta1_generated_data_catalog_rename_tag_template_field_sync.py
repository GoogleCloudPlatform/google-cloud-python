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
# Snippet for RenameTagTemplateField
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datacatalog


# [START datacatalog_v1beta1_generated_DataCatalog_RenameTagTemplateField_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import datacatalog_v1beta1


def sample_rename_tag_template_field():
    # Create a client
    client = datacatalog_v1beta1.DataCatalogClient()

    # Initialize request argument(s)
    request = datacatalog_v1beta1.RenameTagTemplateFieldRequest(
        name="name_value",
        new_tag_template_field_id="new_tag_template_field_id_value",
    )

    # Make the request
    response = client.rename_tag_template_field(request=request)

    # Handle the response
    print(response)


# [END datacatalog_v1beta1_generated_DataCatalog_RenameTagTemplateField_sync]
