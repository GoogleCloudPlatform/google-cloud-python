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
# Snippet for CreateScheduledEvaluationRun
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-ces


# [START ces_v1beta_generated_EvaluationService_CreateScheduledEvaluationRun_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import ces_v1beta


def sample_create_scheduled_evaluation_run():
    # Create a client
    client = ces_v1beta.EvaluationServiceClient()

    # Initialize request argument(s)
    scheduled_evaluation_run = ces_v1beta.ScheduledEvaluationRun()
    scheduled_evaluation_run.display_name = "display_name_value"
    scheduled_evaluation_run.request.app = "app_value"
    scheduled_evaluation_run.scheduling_config.frequency = "BIWEEKLY"

    request = ces_v1beta.CreateScheduledEvaluationRunRequest(
        parent="parent_value",
        scheduled_evaluation_run=scheduled_evaluation_run,
    )

    # Make the request
    response = client.create_scheduled_evaluation_run(request=request)

    # Handle the response
    print(response)


# [END ces_v1beta_generated_EvaluationService_CreateScheduledEvaluationRun_sync]
