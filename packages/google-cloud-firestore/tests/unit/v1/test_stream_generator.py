# Copyright 2024 Google LLC All rights reserved.
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

import pytest
from google.protobuf import struct_pb2


def _make_stream_generator(iterable, explain_options=None, explain_metrics=None):
    from google.cloud.firestore_v1.stream_generator import StreamGenerator

    def _inner_generator():
        for i in iterable:
            X = yield i
            if X:
                yield X
        return explain_metrics

    return StreamGenerator(_inner_generator(), explain_options)


def test_stream_generator_constructor():
    from google.cloud.firestore_v1.query_profile import ExplainOptions
    from google.cloud.firestore_v1.stream_generator import StreamGenerator

    explain_options = ExplainOptions(analyze=True)
    inner_generator = object()
    inst = StreamGenerator(inner_generator, explain_options)

    assert inst._generator == inner_generator
    assert inst._explain_options == explain_options
    assert inst._explain_metrics is None


def test_stream_generator_iter():
    expected_results = [0, 1, 2]
    inst = _make_stream_generator(expected_results)
    actual_results = []
    for result in inst:
        actual_results.append(result)

    assert expected_results == actual_results


def test_stream_generator_next():
    expected_results = [0, 1]
    inst = _make_stream_generator(expected_results)

    actual_results = []
    actual_results.append(next(inst))
    actual_results.append(next(inst))

    with pytest.raises(StopIteration):
        next(inst)

    assert expected_results == actual_results


def test_stream_generator_send():
    expected_results = [0, 1]
    inst = _make_stream_generator(expected_results)

    actual_results = []
    actual_results.append(next(inst))
    assert inst.send(2) == 2
    actual_results.append(next(inst))

    with pytest.raises(StopIteration):
        next(inst)

    assert expected_results == actual_results


def test_stream_generator_throw():
    inst = _make_stream_generator([])
    with pytest.raises(ValueError):
        inst.throw(ValueError)


def test_stream_generator_close():
    expected_results = [0, 1]
    inst = _make_stream_generator(expected_results)

    inst.close()

    # Verifies that generator is closed.
    with pytest.raises(StopIteration):
        next(inst)


def test_stream_generator_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    inst = _make_stream_generator([], explain_options)
    assert inst.explain_options == explain_options


def test_stream_generator_explain_metrics_explain_options_analyze_true():
    from google.protobuf import duration_pb2, struct_pb2

    import google.cloud.firestore_v1.query_profile as query_profile
    import google.cloud.firestore_v1.types.query_profile as query_profile_pb2

    iterator = [1, 2]

    indexes_used_dict = {
        "indexes_used": struct_pb2.Value(
            struct_value=struct_pb2.Struct(
                fields={
                    "query_scope": struct_pb2.Value(string_value="Collection"),
                    "properties": struct_pb2.Value(
                        string_value="(foo ASC, **name** ASC)"
                    ),
                }
            )
        )
    }
    plan_summary = query_profile_pb2.PlanSummary()
    plan_summary.indexes_used.append(indexes_used_dict)
    execution_stats = query_profile_pb2.ExecutionStats(
        {
            "results_returned": 1,
            "execution_duration": duration_pb2.Duration(seconds=2),
            "read_operations": 3,
            "debug_stats": struct_pb2.Struct(
                fields={
                    "billing_details": struct_pb2.Value(
                        string_value="billing_details_results"
                    ),
                    "documents_scanned": struct_pb2.Value(
                        string_value="documents_scanned_results"
                    ),
                    "index_entries_scanned": struct_pb2.Value(
                        string_value="index_entries_scanned"
                    ),
                }
            ),
        }
    )

    explain_options = query_profile.ExplainOptions(analyze=True)
    expected_explain_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=plan_summary,
        execution_stats=execution_stats,
    )

    inst = _make_stream_generator(iterator, explain_options, expected_explain_metrics)

    # Raise an exception if query isn't complete when explain_metrics is called.
    with pytest.raises(
        query_profile.QueryExplainError,
        match="explain_metrics not available until query is complete.",
    ):
        inst.get_explain_metrics()

    list(inst)

    actual_explain_metrics = inst.get_explain_metrics()
    assert isinstance(actual_explain_metrics, query_profile._ExplainAnalyzeMetrics)
    assert actual_explain_metrics == query_profile.ExplainMetrics._from_pb(
        expected_explain_metrics
    )
    assert actual_explain_metrics.plan_summary.indexes_used == [
        {
            "indexes_used": {
                "query_scope": "Collection",
                "properties": "(foo ASC, **name** ASC)",
            }
        }
    ]
    assert actual_explain_metrics.execution_stats.results_returned == 1
    duration = actual_explain_metrics.execution_stats.execution_duration.total_seconds()
    assert duration == 2
    assert actual_explain_metrics.execution_stats.read_operations == 3

    expected_debug_stats = {
        "billing_details": "billing_details_results",
        "documents_scanned": "documents_scanned_results",
        "index_entries_scanned": "index_entries_scanned",
    }
    assert actual_explain_metrics.execution_stats.debug_stats == expected_debug_stats


def test_stream_generator_explain_metrics_explain_options_analyze_false():
    import google.cloud.firestore_v1.query_profile as query_profile
    import google.cloud.firestore_v1.types.query_profile as query_profile_pb2

    iterator = []

    explain_options = query_profile.ExplainOptions(analyze=False)
    indexes_used_dict = {
        "indexes_used": struct_pb2.Value(
            struct_value=struct_pb2.Struct(
                fields={
                    "query_scope": struct_pb2.Value(string_value="Collection"),
                    "properties": struct_pb2.Value(
                        string_value="(foo ASC, **name** ASC)"
                    ),
                }
            )
        )
    }
    plan_summary = query_profile_pb2.PlanSummary()
    plan_summary.indexes_used.append(indexes_used_dict)
    expected_explain_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=plan_summary
    )

    inst = _make_stream_generator(iterator, explain_options, expected_explain_metrics)
    actual_explain_metrics = inst.get_explain_metrics()
    assert isinstance(actual_explain_metrics, query_profile.ExplainMetrics)
    assert actual_explain_metrics.plan_summary.indexes_used == [
        {
            "indexes_used": {
                "query_scope": "Collection",
                "properties": "(foo ASC, **name** ASC)",
            }
        }
    ]


def test_stream_generator_explain_metrics_missing_explain_options_analyze_false():
    import google.cloud.firestore_v1.query_profile as query_profile

    explain_options = query_profile.ExplainOptions(analyze=False)
    inst = _make_stream_generator([("1", None)], explain_options)
    with pytest.raises(
        query_profile.QueryExplainError, match="Did not receive explain_metrics"
    ):
        inst.get_explain_metrics()


def test_stream_generator_explain_metrics_no_explain_options():
    from google.cloud.firestore_v1.query_profile import QueryExplainError

    inst = _make_stream_generator([])

    with pytest.raises(
        QueryExplainError,
        match="explain_options not set on query.",
    ):
        inst.get_explain_metrics()
