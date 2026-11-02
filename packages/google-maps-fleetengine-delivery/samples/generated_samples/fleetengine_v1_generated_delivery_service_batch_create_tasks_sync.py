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
# Snippet for BatchCreateTasks
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-maps-fleetengine-delivery


# [START fleetengine_v1_generated_DeliveryService_BatchCreateTasks_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.maps import fleetengine_delivery_v1


def sample_batch_create_tasks():
    # Create a client
    client = fleetengine_delivery_v1.DeliveryServiceClient()

    # Initialize request argument(s)
    requests = fleetengine_delivery_v1.CreateTaskRequest()
    requests.parent = "parent_value"
    requests.task_id = "task_id_value"
    requests.task.type_ = "UNAVAILABLE"
    requests.task.state = "CLOSED"

    request = fleetengine_delivery_v1.BatchCreateTasksRequest(
        parent="parent_value",
        requests=requests,
    )

    # Make the request
    response = client.batch_create_tasks(request=request)

    # Handle the response
    print(response)


# [END fleetengine_v1_generated_DeliveryService_BatchCreateTasks_sync]
