# Copyright 2024 Google LLC
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


def test_explain_metrics__from_pb():
    """
    Test creating an instance of ExplainMetrics from a protobuf.
    """
    from google.protobuf import duration_pb2, struct_pb2

    from google.cloud.datastore.query_profile import (
        ExplainMetrics,
        PlanSummary,
        QueryExplainError,
        _ExplainAnalyzeMetrics,
    )
    from google.cloud.datastore_v1.types import query_profile as query_profile_pb2

    # test without execution_stats field
    expected_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=query_profile_pb2.PlanSummary(
            indexes_used=struct_pb2.ListValue(values=[])
        )
    )
    metrics = ExplainMetrics._from_pb(expected_metrics)
    assert isinstance(metrics, ExplainMetrics)
    assert isinstance(metrics.plan_summary, PlanSummary)
    assert metrics.plan_summary.indexes_used == []
    with pytest.raises(QueryExplainError) as exc:
        metrics.execution_stats
    assert "execution_stats not available when explain_options.analyze=False" in str(
        exc.value
    )
    # test with execution_stats field
    expected_metrics.execution_stats = query_profile_pb2.ExecutionStats(
        results_returned=1,
        execution_duration=duration_pb2.Duration(seconds=2),
        read_operations=3,
        debug_stats=struct_pb2.Struct(
            fields={"foo": struct_pb2.Value(string_value="bar")}
        ),
    )
    metrics = ExplainMetrics._from_pb(expected_metrics)
    assert isinstance(metrics, ExplainMetrics)
    assert isinstance(metrics, _ExplainAnalyzeMetrics)
    assert metrics.execution_stats.results_returned == 1
    assert metrics.execution_stats.execution_duration.total_seconds() == 2
    assert metrics.execution_stats.read_operations == 3
    assert metrics.execution_stats.debug_stats == {"foo": "bar"}


def test_explain_metrics__from_pb_empty():
    """
    Test with empty ExplainMetrics protobuf.
    """
    from google.protobuf import struct_pb2

    from google.cloud.datastore.query_profile import (
        ExecutionStats,
        ExplainMetrics,
        PlanSummary,
        _ExplainAnalyzeMetrics,
    )
    from google.cloud.datastore_v1.types import query_profile as query_profile_pb2

    expected_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=query_profile_pb2.PlanSummary(
            indexes_used=struct_pb2.ListValue(values=[])
        ),
        execution_stats=query_profile_pb2.ExecutionStats(),
    )
    metrics = ExplainMetrics._from_pb(expected_metrics)
    assert isinstance(metrics, ExplainMetrics)
    assert isinstance(metrics, _ExplainAnalyzeMetrics)
    assert isinstance(metrics.plan_summary, PlanSummary)
    assert isinstance(metrics.execution_stats, ExecutionStats)
    assert metrics.plan_summary.indexes_used == []
    assert metrics.execution_stats.results_returned == 0
    assert metrics.execution_stats.execution_duration.total_seconds() == 0
    assert metrics.execution_stats.read_operations == 0
    assert metrics.execution_stats.debug_stats == {}


def test_explain_metrics_execution_stats():
    """
    Standard ExplainMetrics class should raise exception when execution_stats is accessed.
    _ExplainAnalyzeMetrics should include the field
    """
    from google.cloud.datastore.query_profile import (
        ExplainMetrics,
        QueryExplainError,
        _ExplainAnalyzeMetrics,
    )

    metrics = ExplainMetrics(plan_summary=object())
    with pytest.raises(QueryExplainError) as exc:
        metrics.execution_stats
    assert "execution_stats not available when explain_options.analyze=False" in str(
        exc.value
    )
    expected_stats = object()
    metrics = _ExplainAnalyzeMetrics(
        plan_summary=object(), _execution_stats=expected_stats
    )
    assert metrics.execution_stats is expected_stats


def test_explain_options__to_dict():
    """
    Should be able to create a dict representation of ExplainOptions
    """
    from google.cloud.datastore.query_profile import ExplainOptions

    assert ExplainOptions(analyze=True)._to_dict() == {"analyze": True}
    assert ExplainOptions(analyze=False)._to_dict() == {"analyze": False}
