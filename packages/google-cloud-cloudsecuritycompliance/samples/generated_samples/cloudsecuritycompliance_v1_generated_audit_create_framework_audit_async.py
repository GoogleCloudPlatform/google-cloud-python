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
# Snippet for CreateFrameworkAudit
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-cloudsecuritycompliance


# [START cloudsecuritycompliance_v1_generated_Audit_CreateFrameworkAudit_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import cloudsecuritycompliance_v1


async def sample_create_framework_audit():
    # Create a client
    client = cloudsecuritycompliance_v1.AuditAsyncClient()

    # Initialize request argument(s)
    framework_audit = cloudsecuritycompliance_v1.FrameworkAudit()
    framework_audit.framework_audit_destination.bucket.bucket_uri = "bucket_uri_value"

    request = cloudsecuritycompliance_v1.CreateFrameworkAuditRequest(
        parent="parent_value",
        framework_audit=framework_audit,
    )

    # Make the request
    operation = await client.create_framework_audit(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END cloudsecuritycompliance_v1_generated_Audit_CreateFrameworkAudit_async]
