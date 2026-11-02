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
from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Any

from google.protobuf.json_format import MessageToDict
from google.protobuf.wrappers_pb2 import StringValue

from google.cloud.firestore_v1.types.document import MapValue, Value
from google.cloud.firestore_v1.types.explain_stats import (
    ExplainStats as ExplainStats_pb,
)


@dataclass(frozen=True)
class ExplainOptions:
    """
    Explain options for the query.
    Set on a query object using the explain_options attribute at query
    construction time.

    :type analyze: bool
    :param analyze: Optional. Whether to execute this query. When false
    (the default), the query will be planned, returning only metrics from the
    planning stages. When true, the query will be planned and executed,
    returning the full query results along with both planning and execution
    stage metrics.
    """

    analyze: bool = False

    def _to_dict(self):
        return {"analyze": self.analyze}


@dataclass(frozen=True)
class PipelineExplainOptions:
    """
    Explain options for pipeline queries.

    Set on a pipeline.execution() or pipeline.stream() call, to provide
    explain_stats in the pipeline output

    :type mode: str
    :param mode: Optional. The mode of operation for this explain query.
        When set to 'analyze', the query will be executed and return the full
        query results along with execution statistics.

    :type output_format: str | None
    :param output_format: Optional. The format in which to return the explain
        stats.
    """

    mode: str = "analyze"

    def _to_value(self):
        out_dict = {"mode": Value(string_value=self.mode)}
        value_pb = MapValue(fields=out_dict)
        return Value(map_value=value_pb)


@dataclass(frozen=True)
class PlanSummary:
    """
    Contains planning phase information about a query.`

    :type indexes_used: list[dict[str, Any]]
    :param indexes_used: The indexes selected for this query.
    """

    indexes_used: list[dict[str, Any]]


@dataclass(frozen=True)
class ExecutionStats:
    """
    Execution phase information about a query.

    Only available when explain_options.analyze is True.

    :type results_returned: int
    :param results_returned: Total number of results returned, including
        documents, projections, aggregation results, keys.
    :type execution_duration: datetime.timedelta
    :param execution_duration: Total time to execute the query in the backend.
    :type read_operations: int
    :param read_operations: Total billable read operations.
    :type debug_stats: dict[str, Any]
    :param debug_stats: Debugging statistics from the execution of the query.
        Note that the debugging stats are subject to change as Firestore evolves
    """

    results_returned: int
    execution_duration: datetime.timedelta
    read_operations: int
    debug_stats: dict[str, Any]


@dataclass(frozen=True)
class ExplainMetrics:
    """
    ExplainMetrics contains information about the planning and execution of a query.

    When explain_options.analyze is false, only plan_summary is available.
    When explain_options.analyze is true, execution_stats is also available.

    :type plan_summary: PlanSummary
    :param plan_summary: Planning phase information about the query.
    :type execution_stats: ExecutionStats
    :param execution_stats: Execution phase information about the query.
    """

    plan_summary: PlanSummary

    @staticmethod
    def _from_pb(metrics_pb):
        dict_repr = MessageToDict(metrics_pb._pb, preserving_proto_field_name=True)
        plan_summary = PlanSummary(
            indexes_used=dict_repr.get("plan_summary", {}).get("indexes_used", [])
        )
        if "execution_stats" in dict_repr:
            stats_dict = dict_repr.get("execution_stats", {})
            execution_stats = ExecutionStats(
                results_returned=int(stats_dict.get("results_returned", 0)),
                execution_duration=metrics_pb.execution_stats.execution_duration,
                read_operations=int(stats_dict.get("read_operations", 0)),
                debug_stats=stats_dict.get("debug_stats", {}),
            )
            return _ExplainAnalyzeMetrics(
                plan_summary=plan_summary, _execution_stats=execution_stats
            )
        else:
            return ExplainMetrics(plan_summary=plan_summary)

    @property
    def execution_stats(self) -> ExecutionStats:
        raise QueryExplainError(
            "execution_stats not available when explain_options.analyze=False."
        )


@dataclass(frozen=True)
class _ExplainAnalyzeMetrics(ExplainMetrics):
    """
    Subclass of ExplainMetrics that includes execution_stats.
    Only available when explain_options.analyze is True.
    """

    plan_summary: PlanSummary
    _execution_stats: ExecutionStats

    @property
    def execution_stats(self) -> ExecutionStats:
        return self._execution_stats


class QueryExplainError(Exception):
    """
    Error returned when there is a problem accessing query profiling information.
    """

    pass


class ExplainStats:
    """
    Contains query profiling statistics for a pipeline query.

    This class is not meant to be instantiated directly by the user. Instead, an
    instance of `ExplainStats` may be returned by pipeline execution methods
    when `explain_options` are provided.

    It provides methods to access the explain statistics in different formats.
    """

    def __init__(self, stats_pb: ExplainStats_pb):
        """
        Args:
            stats_pb (ExplainStats_pb): The raw protobuf message for explain stats.
        """
        self._stats_pb = stats_pb

    def get_text(self) -> str:
        """
        Returns the explain stats as a string.

        This method is suitable for explain formats that have a text-based output,
        such as 'text' or 'json'.

        Returns:
            str: The string representation of the explain stats.

        Raises:
            QueryExplainError: If the explain stats payload from the backend is not
                a string. This can happen if a non-text output format was requested.
        """
        pb_data = self._stats_pb._pb.data
        content = StringValue()
        if pb_data.Unpack(content):
            return content.value
        raise QueryExplainError(
            "Unable to decode explain stats. Did you request an output format that returns a string value, such as 'text' or 'json'?"
        )

    def get_raw(self) -> ExplainStats_pb:
        """
        Returns the explain stats in an encoded proto format, as returned from the Firestore backend.
        The caller is responsible for unpacking this proto message.

        Returns:
            google.cloud.firestore_v1.types.explain_stats.ExplainStats: the proto from the backend
        """
        return self._stats_pb
