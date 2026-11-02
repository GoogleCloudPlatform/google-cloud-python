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
# Snippet for RemoveAclEntry
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-managedkafka


# [START managedkafka_v1_generated_ManagedKafka_RemoveAclEntry_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import managedkafka_v1


def sample_remove_acl_entry():
    # Create a client
    client = managedkafka_v1.ManagedKafkaClient()

    # Initialize request argument(s)
    acl_entry = managedkafka_v1.AclEntry()
    acl_entry.principal = "principal_value"
    acl_entry.permission_type = "permission_type_value"
    acl_entry.operation = "operation_value"
    acl_entry.host = "host_value"

    request = managedkafka_v1.RemoveAclEntryRequest(
        acl="acl_value",
        acl_entry=acl_entry,
    )

    # Make the request
    response = client.remove_acl_entry(request=request)

    # Handle the response
    print(response)


# [END managedkafka_v1_generated_ManagedKafka_RemoveAclEntry_sync]
