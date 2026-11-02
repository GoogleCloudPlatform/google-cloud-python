# -*- coding: utf-8 -*-
#
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

from google.cloud import bigquery_datatransfer_v1


@pytest.fixture(scope="session")
def project_id():
    return os.environ["PROJECT_ID"]


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_list_data_sources(project_id: str, transport: str):
    client = bigquery_datatransfer_v1.DataTransferServiceClient(transport=transport)

    parent = client.common_location_path(project_id, location="us-central1")
    client.list_data_sources(parent=parent)

    # The purpose of this smoke test is to test the communication with the API server,
    # rather than API-specific functionality.
    # If the smoke test fails, we won't reach this line.
    assert True
