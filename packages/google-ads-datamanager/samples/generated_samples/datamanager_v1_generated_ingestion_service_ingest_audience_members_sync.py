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
# Snippet for IngestAudienceMembers
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-ads-datamanager


# [START datamanager_v1_generated_IngestionService_IngestAudienceMembers_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.ads import datamanager_v1


def sample_ingest_audience_members():
    # Create a client
    client = datamanager_v1.IngestionServiceClient()

    # Initialize request argument(s)
    destinations = datamanager_v1.Destination()
    destinations.operating_account.account_id = "account_id_value"
    destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

    audience_members = datamanager_v1.AudienceMember()
    audience_members.user_data.user_identifiers.email_address = "email_address_value"

    request = datamanager_v1.IngestAudienceMembersRequest(
        destinations=destinations,
        audience_members=audience_members,
    )

    # Make the request
    response = client.ingest_audience_members(request=request)

    # Handle the response
    print(response)


# [END datamanager_v1_generated_IngestionService_IngestAudienceMembers_sync]
