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
# Snippet for UpdateCustomerManagedCertificate
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-sql


# [START sqladmin_v1beta4_generated_SqlSslCertsService_UpdateCustomerManagedCertificate_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import sqladmin_v1beta4


async def sample_update_customer_managed_certificate():
    # Create a client
    client = sqladmin_v1beta4.SqlSslCertsServiceAsyncClient()

    # Initialize request argument(s)
    customer_managed_certificate_config = (
        sqladmin_v1beta4.CustomerManagedCertificateConfig()
    )
    customer_managed_certificate_config.intent = "NATIVE_REPLICATION"
    customer_managed_certificate_config.customer_managed_certificates.certificate_type = "CERTIFICATE_TYPE_PEER_CLIENT_CERTIFICATE"
    customer_managed_certificate_config.customer_managed_certificates.content = (
        b"content_blob"
    )

    request = sqladmin_v1beta4.UpdateCustomerManagedCertificateRequest(
        instance="instance_value",
        project="project_value",
        customer_managed_certificate_config=customer_managed_certificate_config,
        certificate_bundle="certificate_bundle_value",
    )

    # Make the request
    response = await client.update_customer_managed_certificate(request=request)

    # Handle the response
    print(response)


# [END sqladmin_v1beta4_generated_SqlSslCertsService_UpdateCustomerManagedCertificate_async]
