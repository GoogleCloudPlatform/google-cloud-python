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
# Snippet for CreateMappingRule
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dms


# [START datamigration_v1_generated_DataMigrationService_CreateMappingRule_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import clouddms_v1


async def sample_create_mapping_rule():
    # Create a client
    client = clouddms_v1.DataMigrationServiceAsyncClient()

    # Initialize request argument(s)
    mapping_rule = clouddms_v1.MappingRule()
    mapping_rule.single_entity_rename.new_name = "new_name_value"
    mapping_rule.rule_scope = "DATABASE_ENTITY_TYPE_DATABASE"
    mapping_rule.rule_order = 1075

    request = clouddms_v1.CreateMappingRuleRequest(
        parent="parent_value",
        mapping_rule_id="mapping_rule_id_value",
        mapping_rule=mapping_rule,
    )

    # Make the request
    response = await client.create_mapping_rule(request=request)

    # Handle the response
    print(response)


# [END datamigration_v1_generated_DataMigrationService_CreateMappingRule_async]
