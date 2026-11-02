# Copyright 2019 Google LLC
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

from collections import OrderedDict
import inspect

import pytest


@pytest.fixture
def query_job_class():
    from google.cloud.bigquery.job import QueryJob

    return QueryJob


@pytest.fixture
def row_iterator_class():
    from google.cloud.bigquery.table import RowIterator

    return RowIterator


def test_to_arrow_method_signatures_match(query_job_class, row_iterator_class):
    query_job_sig = inspect.signature(query_job_class.to_arrow)
    iterator_sig = inspect.signature(row_iterator_class.to_arrow)

    assert "max_results" in query_job_sig.parameters

    # Compare the signatures while ignoring the max_results parameter, which is
    # specific to the method on QueryJob.
    params = OrderedDict(query_job_sig.parameters)
    del params["max_results"]
    query_job_sig = query_job_sig.replace(parameters=params.values())

    assert query_job_sig == iterator_sig


def test_to_dataframe_method_signatures_match(query_job_class, row_iterator_class):
    query_job_sig = inspect.signature(query_job_class.to_dataframe)
    iterator_sig = inspect.signature(row_iterator_class.to_dataframe)

    assert "max_results" in query_job_sig.parameters

    # Compare the signatures while ignoring the max_results parameter, which is
    # specific to the method on QueryJob.
    params = OrderedDict(query_job_sig.parameters)
    del params["max_results"]
    query_job_sig = query_job_sig.replace(parameters=params.values())

    assert query_job_sig == iterator_sig
