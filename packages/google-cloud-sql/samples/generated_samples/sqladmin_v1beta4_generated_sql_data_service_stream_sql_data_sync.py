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
# Snippet for StreamSqlData
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-sql


# [START sqladmin_v1beta4_generated_SqlDataService_StreamSqlData_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import sqladmin_v1beta4


def sample_stream_sql_data():
    # Create a client
    client = sqladmin_v1beta4.SqlDataServiceClient()

    # Initialize request argument(s)
    start_session = sqladmin_v1beta4.StartSession()
    start_session.location_id = "location_id_value"
    start_session.instance_id = "instance_id_value"

    request = sqladmin_v1beta4.StreamSqlDataRequest(
        start_session=start_session,
    )

    # This method expects an iterator which contains
    # 'sqladmin_v1beta4.StreamSqlDataRequest' objects
    # Here we create a generator that yields a single `request` for
    # demonstrative purposes.
    requests = [request]

    def request_generator():
        for request in requests:
            yield request

    # Make the request
    stream = client.stream_sql_data(requests=request_generator())

    # Handle the response
    for response in stream:
        print(response)


# [END sqladmin_v1beta4_generated_SqlDataService_StreamSqlData_sync]
