# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
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
"""System tests for reading rows from tables."""

import pytest

from google.cloud import bigquery_storage, bigquery_storage_v1beta2


@pytest.fixture(scope="session")
def client_v1(credentials):
    return bigquery_storage.BigQueryReadClient(credentials=credentials)


@pytest.fixture(scope="session")
def client_v1beta2(credentials):
    return bigquery_storage_v1beta2.BigQueryReadClient(credentials=credentials)


@pytest.fixture(scope="session", params=["v1", "v1beta2"])
def client_and_types(request, client_v1, client_v1beta2):
    if request.param == "v1":
        return client_v1, bigquery_storage.types
    return client_v1beta2, bigquery_storage_v1beta2.types
