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
# Snippet for CreateCertificateIssuanceConfig
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-certificate-manager


# [START certificatemanager_v1_generated_CertificateManager_CreateCertificateIssuanceConfig_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import certificate_manager_v1


def sample_create_certificate_issuance_config():
    # Create a client
    client = certificate_manager_v1.CertificateManagerClient()

    # Initialize request argument(s)
    certificate_issuance_config = certificate_manager_v1.CertificateIssuanceConfig()
    certificate_issuance_config.certificate_authority_config.certificate_authority_service_config.ca_pool = "ca_pool_value"
    certificate_issuance_config.rotation_window_percentage = 2788
    certificate_issuance_config.key_algorithm = "ECDSA_P256"

    request = certificate_manager_v1.CreateCertificateIssuanceConfigRequest(
        parent="parent_value",
        certificate_issuance_config_id="certificate_issuance_config_id_value",
        certificate_issuance_config=certificate_issuance_config,
    )

    # Make the request
    operation = client.create_certificate_issuance_config(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END certificatemanager_v1_generated_CertificateManager_CreateCertificateIssuanceConfig_sync]
