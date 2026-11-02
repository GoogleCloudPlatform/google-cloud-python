# Copyright 2020 Google LLC All rights reserved.
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


import mock
import pytest

from google.cloud.firestore_v1.query_profile import QueryExplainError


def _make_base_document_reference(*args, **kwargs):
    from google.cloud.firestore_v1.base_document import BaseDocumentReference

    return BaseDocumentReference(*args, **kwargs)


def _make_document_snapshot(*args, **kwargs):
    from google.cloud.firestore_v1.document import DocumentSnapshot

    return DocumentSnapshot(*args, **kwargs)


def _make_query_results_list(*args, **kwargs):
    from google.cloud.firestore_v1.query_results import QueryResultsList

    return QueryResultsList(*args, **kwargs)


def _make_explain_metrics():
    from google.cloud.firestore_v1.query_profile import ExplainMetrics, PlanSummary

    plan_summary = PlanSummary(
        indexes_used=[{"properties": "(__name__ ASC)", "query_scope": "Collection"}],
    )
    return ExplainMetrics(plan_summary=plan_summary)


def test_query_results_list_constructor():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    client = mock.sentinel.client
    reference = _make_base_document_reference("hi", "bye", client=client)
    data_1 = {"zoop": 83}
    data_2 = {"zoop": 30}
    snapshot_1 = _make_document_snapshot(
        reference,
        data_1,
        True,
        mock.sentinel.read_time,
        mock.sentinel.create_time,
        mock.sentinel.update_time,
    )
    snapshot_2 = _make_document_snapshot(
        reference,
        data_2,
        True,
        mock.sentinel.read_time,
        mock.sentinel.create_time,
        mock.sentinel.update_time,
    )
    explain_metrics = _make_explain_metrics()
    explain_options = ExplainOptions(analyze=True)
    snapshot_list = _make_query_results_list(
        [snapshot_1, snapshot_2],
        explain_options=explain_options,
        explain_metrics=explain_metrics,
    )
    assert len(snapshot_list) == 2
    assert snapshot_list[0] == snapshot_1
    assert snapshot_list[1] == snapshot_2
    assert snapshot_list._explain_options == explain_options
    assert snapshot_list._explain_metrics == explain_metrics


def test_query_results_list_constructor_w_explain_options_and_wo_explain_metrics():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    with pytest.raises(
        ValueError,
        match="If explain_options is set, explain_metrics must be non-empty.",
    ):
        _make_query_results_list(
            [],
            explain_options=ExplainOptions(analyze=True),
            explain_metrics=None,
        )


def test_query_results_list_constructor_wo_explain_options_and_w_explain_metrics():
    with pytest.raises(
        ValueError, match="If explain_options is empty, explain_metrics must be empty."
    ):
        _make_query_results_list(
            [],
            explain_options=None,
            explain_metrics=_make_explain_metrics(),
        )


def test_query_results_list_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    explain_metrics = _make_explain_metrics()
    snapshot_list = _make_query_results_list(
        [], explain_options=explain_options, explain_metrics=explain_metrics
    )

    assert snapshot_list.explain_options == explain_options


def test_query_results_list_explain_metrics_w_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_metrics = _make_explain_metrics()
    snapshot_list = _make_query_results_list(
        [],
        explain_options=ExplainOptions(analyze=True),
        explain_metrics=explain_metrics,
    )

    assert snapshot_list.get_explain_metrics() == explain_metrics


def test_query_results_list_explain_metrics_wo_explain_options():
    snapshot_list = _make_query_results_list([])

    with pytest.raises(QueryExplainError, match="explain_options not set on query."):
        snapshot_list.get_explain_metrics()


def test_query_results_list_explain_metrics_empty():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_metrics = _make_explain_metrics()
    snapshot_list = _make_query_results_list(
        [],
        explain_options=ExplainOptions(analyze=True),
        explain_metrics=explain_metrics,
    )
    snapshot_list._explain_metrics = None

    with pytest.raises(
        QueryExplainError,
        match="explain_metrics is empty despite explain_options is set.",
    ):
        snapshot_list.get_explain_metrics()
