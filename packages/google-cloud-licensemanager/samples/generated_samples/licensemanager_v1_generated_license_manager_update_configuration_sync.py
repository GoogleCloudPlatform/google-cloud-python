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
# Snippet for UpdateConfiguration
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-licensemanager


# [START licensemanager_v1_generated_LicenseManager_UpdateConfiguration_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import licensemanager_v1


def sample_update_configuration():
    # Create a client
    client = licensemanager_v1.LicenseManagerClient()

    # Initialize request argument(s)
    configuration = licensemanager_v1.Configuration()
    configuration.display_name = "display_name_value"
    configuration.product = "product_value"
    configuration.license_type = "LICENSE_TYPE_BRING_YOUR_OWN_LICENSE"
    configuration.current_billing_info.user_count_billing.user_count = 1095
    configuration.next_billing_info.user_count_billing.user_count = 1095

    request = licensemanager_v1.UpdateConfigurationRequest(
        configuration=configuration,
    )

    # Make the request
    operation = client.update_configuration(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END licensemanager_v1_generated_LicenseManager_UpdateConfiguration_sync]
