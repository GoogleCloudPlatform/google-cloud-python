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
# Snippet for ReportErrorEvent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-error-reporting


# [START clouderrorreporting_v1beta1_generated_ReportErrorsService_ReportErrorEvent_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import errorreporting_v1beta1


def sample_report_error_event():
    # Create a client
    client = errorreporting_v1beta1.ReportErrorsServiceClient()

    # Initialize request argument(s)
    event = errorreporting_v1beta1.ReportedErrorEvent()
    event.message = "message_value"

    request = errorreporting_v1beta1.ReportErrorEventRequest(
        project_name="project_name_value",
        event=event,
    )

    # Make the request
    response = client.report_error_event(request=request)

    # Handle the response
    print(response)


# [END clouderrorreporting_v1beta1_generated_ReportErrorsService_ReportErrorEvent_sync]
