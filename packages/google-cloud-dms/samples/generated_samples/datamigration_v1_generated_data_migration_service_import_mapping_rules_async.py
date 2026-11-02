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
# Snippet for ImportMappingRules
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dms


# [START datamigration_v1_generated_DataMigrationService_ImportMappingRules_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import clouddms_v1


async def sample_import_mapping_rules():
    # Create a client
    client = clouddms_v1.DataMigrationServiceAsyncClient()

    # Initialize request argument(s)
    rules_files = clouddms_v1.RulesFile()
    rules_files.rules_source_filename = "rules_source_filename_value"
    rules_files.rules_content = "rules_content_value"

    request = clouddms_v1.ImportMappingRulesRequest(
        parent="parent_value",
        rules_format="IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE",
        rules_files=rules_files,
        auto_commit=True,
    )

    # Make the request
    operation = await client.import_mapping_rules(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END datamigration_v1_generated_DataMigrationService_ImportMappingRules_async]
