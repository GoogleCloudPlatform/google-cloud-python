# Copyright 2015 Google LLC
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

from .helpers import _Base
import datetime


class TestBiEngineStats:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job.query import BiEngineStats

        return BiEngineStats

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        bi_engine_stats = self._make_one()
        assert bi_engine_stats.mode == "ACCELERATION_MODE_UNSPECIFIED"
        assert bi_engine_stats.reasons == []

    def test_from_api_repr_unspecified(self):
        klass = self._get_target_class()
        result = klass.from_api_repr({"biEngineMode": "ACCELERATION_MODE_UNSPECIFIED"})

        assert isinstance(result, klass)
        assert result.mode == "ACCELERATION_MODE_UNSPECIFIED"
        assert result.reasons == []

    def test_from_api_repr_full(self):
        klass = self._get_target_class()
        result = klass.from_api_repr({"biEngineMode": "FULL"})

        assert isinstance(result, klass)
        assert result.mode == "FULL"
        assert result.reasons == []

    def test_from_api_repr_disabled(self):
        klass = self._get_target_class()
        result = klass.from_api_repr(
            {
                "biEngineMode": "DISABLED",
                "biEngineReasons": [
                    {
                        "code": "OTHER_REASON",
                        "message": "Unable to support input table xyz due to an internal error.",
                    }
                ],
            }
        )

        assert isinstance(result, klass)
        assert result.mode == "DISABLED"

        reason = result.reasons[0]
        assert reason.code == "OTHER_REASON"
        assert (
            reason.reason
            == "Unable to support input table xyz due to an internal error."
        )


class TestDmlStats:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import DmlStats

        return DmlStats

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        dml_stats = self._make_one()
        assert dml_stats.inserted_row_count == 0
        assert dml_stats.deleted_row_count == 0
        assert dml_stats.updated_row_count == 0

    def test_from_api_repr_partial_stats(self):
        klass = self._get_target_class()
        result = klass.from_api_repr({"deletedRowCount": "12"})

        assert isinstance(result, klass)
        assert result.inserted_row_count == 0
        assert result.deleted_row_count == 12
        assert result.updated_row_count == 0

    def test_from_api_repr_full_stats(self):
        klass = self._get_target_class()
        result = klass.from_api_repr(
            {"updatedRowCount": "4", "insertedRowCount": "7", "deletedRowCount": "25"}
        )

        assert isinstance(result, klass)
        assert result.inserted_row_count == 7
        assert result.deleted_row_count == 25
        assert result.updated_row_count == 4


class TestSearchStatistics:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job.query import SearchStats

        return SearchStats

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor_defaults(self):
        search_stats = self._make_one()
        assert search_stats.mode is None
        assert search_stats.reason == []

    def test_from_api_repr_unspecified(self):
        klass = self._get_target_class()
        result = klass.from_api_repr(
            {"indexUsageMode": "INDEX_USAGE_MODE_UNSPECIFIED", "indexUnusedReasons": []}
        )

        assert isinstance(result, klass)
        assert result.mode == "INDEX_USAGE_MODE_UNSPECIFIED"
        assert result.reason == []


class TestIndexUnusedReason:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job.query import IndexUnusedReason

        return IndexUnusedReason

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor_defaults(self):
        search_reason = self._make_one()
        assert search_reason.code is None
        assert search_reason.message is None
        assert search_reason.baseTable is None
        assert search_reason.indexName is None

    def test_from_api_repr_unspecified(self):
        klass = self._get_target_class()
        result = klass.from_api_repr(
            {
                "code": "INDEX_CONFIG_NOT_AVAILABLE",
                "message": "There is no search index...",
                "baseTable": {
                    "projectId": "bigquery-public-data",
                    "datasetId": "usa_names",
                    "tableId": "usa_1910_current",
                },
                "indexName": None,
            }
        )

        assert isinstance(result, klass)
        assert result.code == "INDEX_CONFIG_NOT_AVAILABLE"
        assert result.message == "There is no search index..."
        assert result.baseTable == {
            "projectId": "bigquery-public-data",
            "datasetId": "usa_names",
            "tableId": "usa_1910_current",
        }
        assert result.indexName is None


class TestQueryPlanEntryStep(_Base):
    KIND = "KIND"
    SUBSTEPS = ("SUB1", "SUB2")

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import QueryPlanEntryStep

        return QueryPlanEntryStep

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        step = self._make_one(self.KIND, self.SUBSTEPS)
        self.assertEqual(step.kind, self.KIND)
        self.assertEqual(step.substeps, list(self.SUBSTEPS))

    def test_from_api_repr_empty(self):
        klass = self._get_target_class()
        step = klass.from_api_repr({})
        self.assertIsNone(step.kind)
        self.assertEqual(step.substeps, [])

    def test_from_api_repr_normal(self):
        resource = {"kind": self.KIND, "substeps": self.SUBSTEPS}
        klass = self._get_target_class()
        step = klass.from_api_repr(resource)
        self.assertEqual(step.kind, self.KIND)
        self.assertEqual(step.substeps, list(self.SUBSTEPS))

    def test___eq___mismatched_type(self):
        step = self._make_one(self.KIND, self.SUBSTEPS)
        self.assertNotEqual(step, object())

    def test___eq___mismatch_kind(self):
        step = self._make_one(self.KIND, self.SUBSTEPS)
        other = self._make_one("OTHER", self.SUBSTEPS)
        self.assertNotEqual(step, other)

    def test___eq___mismatch_substeps(self):
        step = self._make_one(self.KIND, self.SUBSTEPS)
        other = self._make_one(self.KIND, ())
        self.assertNotEqual(step, other)

    def test___eq___hit(self):
        step = self._make_one(self.KIND, self.SUBSTEPS)
        other = self._make_one(self.KIND, self.SUBSTEPS)
        self.assertEqual(step, other)

    def test___eq___wrong_type(self):
        step = self._make_one(self.KIND, self.SUBSTEPS)
        self.assertFalse(step == "hello")


class TestQueryPlanEntry(_Base):
    NAME = "NAME"
    ENTRY_ID = 1234
    START_MS = 1522540800000
    END_MS = 1522540804000
    INPUT_STAGES = (88, 101)
    PARALLEL_INPUTS = 1000
    COMPLETED_PARALLEL_INPUTS = 5
    WAIT_MS_AVG = 33
    WAIT_MS_MAX = 400
    WAIT_RATIO_AVG = 2.71828
    WAIT_RATIO_MAX = 3.14159
    READ_MS_AVG = 45
    READ_MS_MAX = 90
    READ_RATIO_AVG = 1.41421
    READ_RATIO_MAX = 1.73205
    COMPUTE_MS_AVG = 55
    COMPUTE_MS_MAX = 99
    COMPUTE_RATIO_AVG = 0.69315
    COMPUTE_RATIO_MAX = 1.09861
    WRITE_MS_AVG = 203
    WRITE_MS_MAX = 340
    WRITE_RATIO_AVG = 3.32193
    WRITE_RATIO_MAX = 2.30258
    RECORDS_READ = 100
    RECORDS_WRITTEN = 1
    STATUS = "STATUS"
    SHUFFLE_OUTPUT_BYTES = 1024
    SHUFFLE_OUTPUT_BYTES_SPILLED = 1
    SLOT_MS = 25

    START_RFC3339_MICROS = "2018-04-01T00:00:00.000000Z"
    END_RFC3339_MICROS = "2018-04-01T00:00:04.000000Z"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import QueryPlanEntry

        return QueryPlanEntry

    def test_from_api_repr_empty(self):
        klass = self._get_target_class()

        entry = klass.from_api_repr({})

        self.assertIsNone(entry.name)
        self.assertIsNone(entry.entry_id)
        self.assertEqual(entry.input_stages, [])
        self.assertIsNone(entry.start)
        self.assertIsNone(entry.end)
        self.assertIsNone(entry.parallel_inputs)
        self.assertIsNone(entry.completed_parallel_inputs)
        self.assertIsNone(entry.wait_ms_avg)
        self.assertIsNone(entry.wait_ms_max)
        self.assertIsNone(entry.wait_ratio_avg)
        self.assertIsNone(entry.wait_ratio_max)
        self.assertIsNone(entry.read_ms_avg)
        self.assertIsNone(entry.read_ms_max)
        self.assertIsNone(entry.read_ratio_avg)
        self.assertIsNone(entry.read_ratio_max)
        self.assertIsNone(entry.compute_ms_avg)
        self.assertIsNone(entry.compute_ms_max)
        self.assertIsNone(entry.compute_ratio_avg)
        self.assertIsNone(entry.compute_ratio_max)
        self.assertIsNone(entry.write_ms_avg)
        self.assertIsNone(entry.write_ms_max)
        self.assertIsNone(entry.write_ratio_avg)
        self.assertIsNone(entry.write_ratio_max)
        self.assertIsNone(entry.records_read)
        self.assertIsNone(entry.records_written)
        self.assertIsNone(entry.status)
        self.assertIsNone(entry.shuffle_output_bytes)
        self.assertIsNone(entry.shuffle_output_bytes_spilled)
        self.assertEqual(entry.steps, [])
        self.assertIsNone(entry.slot_ms)

    def test_from_api_repr_normal(self):
        from google.cloud.bigquery.job import QueryPlanEntryStep

        steps = [
            QueryPlanEntryStep(
                kind=TestQueryPlanEntryStep.KIND,
                substeps=TestQueryPlanEntryStep.SUBSTEPS,
            )
        ]
        resource = {
            "name": self.NAME,
            "id": self.ENTRY_ID,
            "inputStages": self.INPUT_STAGES,
            "startMs": self.START_MS,
            "endMs": self.END_MS,
            "waitMsAvg": self.WAIT_MS_AVG,
            "waitMsMax": self.WAIT_MS_MAX,
            "waitRatioAvg": self.WAIT_RATIO_AVG,
            "waitRatioMax": self.WAIT_RATIO_MAX,
            "readMsAvg": self.READ_MS_AVG,
            "readMsMax": self.READ_MS_MAX,
            "readRatioAvg": self.READ_RATIO_AVG,
            "readRatioMax": self.READ_RATIO_MAX,
            "computeMsAvg": self.COMPUTE_MS_AVG,
            "computeMsMax": self.COMPUTE_MS_MAX,
            "computeRatioAvg": self.COMPUTE_RATIO_AVG,
            "computeRatioMax": self.COMPUTE_RATIO_MAX,
            "writeMsAvg": self.WRITE_MS_AVG,
            "writeMsMax": self.WRITE_MS_MAX,
            "writeRatioAvg": self.WRITE_RATIO_AVG,
            "writeRatioMax": self.WRITE_RATIO_MAX,
            "recordsRead": self.RECORDS_READ,
            "recordsWritten": self.RECORDS_WRITTEN,
            "status": self.STATUS,
            "shuffleOutputBytes": self.SHUFFLE_OUTPUT_BYTES,
            "shuffleOutputBytesSpilled": self.SHUFFLE_OUTPUT_BYTES_SPILLED,
            "steps": [
                {
                    "kind": TestQueryPlanEntryStep.KIND,
                    "substeps": TestQueryPlanEntryStep.SUBSTEPS,
                }
            ],
            "slotMs": self.SLOT_MS,
        }
        klass = self._get_target_class()

        entry = klass.from_api_repr(resource)
        self.assertEqual(entry.name, self.NAME)
        self.assertEqual(entry.entry_id, self.ENTRY_ID)
        self.assertEqual(entry.wait_ratio_avg, self.WAIT_RATIO_AVG)
        self.assertEqual(entry.wait_ratio_max, self.WAIT_RATIO_MAX)
        self.assertEqual(entry.read_ratio_avg, self.READ_RATIO_AVG)
        self.assertEqual(entry.read_ratio_max, self.READ_RATIO_MAX)
        self.assertEqual(entry.compute_ratio_avg, self.COMPUTE_RATIO_AVG)
        self.assertEqual(entry.compute_ratio_max, self.COMPUTE_RATIO_MAX)
        self.assertEqual(entry.write_ratio_avg, self.WRITE_RATIO_AVG)
        self.assertEqual(entry.write_ratio_max, self.WRITE_RATIO_MAX)
        self.assertEqual(entry.records_read, self.RECORDS_READ)
        self.assertEqual(entry.records_written, self.RECORDS_WRITTEN)
        self.assertEqual(entry.status, self.STATUS)
        self.assertEqual(entry.steps, steps)
        self.assertEqual(entry.slot_ms, self.SLOT_MS)

    def test_start(self):
        from google.cloud._helpers import _RFC3339_MICROS

        klass = self._get_target_class()

        entry = klass.from_api_repr({})
        self.assertEqual(entry.start, None)

        entry._properties["startMs"] = self.START_MS
        self.assertEqual(
            entry.start.strftime(_RFC3339_MICROS), self.START_RFC3339_MICROS
        )

    def test_end(self):
        from google.cloud._helpers import _RFC3339_MICROS

        klass = self._get_target_class()

        entry = klass.from_api_repr({})
        self.assertEqual(entry.end, None)

        entry._properties["endMs"] = self.END_MS
        self.assertEqual(entry.end.strftime(_RFC3339_MICROS), self.END_RFC3339_MICROS)


class TestScriptStackFrame(_Base):
    def _make_one(self, resource):
        from google.cloud.bigquery.job import ScriptStackFrame

        return ScriptStackFrame(resource)

    def test_procedure_id(self):
        frame = self._make_one({"procedureId": "some-procedure"})
        self.assertEqual(frame.procedure_id, "some-procedure")
        del frame._properties["procedureId"]
        self.assertIsNone(frame.procedure_id)

    def test_start_line(self):
        frame = self._make_one({"startLine": 5})
        self.assertEqual(frame.start_line, 5)
        frame._properties["startLine"] = "5"
        self.assertEqual(frame.start_line, 5)

    def test_start_column(self):
        frame = self._make_one({"startColumn": 29})
        self.assertEqual(frame.start_column, 29)
        frame._properties["startColumn"] = "29"
        self.assertEqual(frame.start_column, 29)

    def test_end_line(self):
        frame = self._make_one({"endLine": 9})
        self.assertEqual(frame.end_line, 9)
        frame._properties["endLine"] = "9"
        self.assertEqual(frame.end_line, 9)

    def test_end_column(self):
        frame = self._make_one({"endColumn": 14})
        self.assertEqual(frame.end_column, 14)
        frame._properties["endColumn"] = "14"
        self.assertEqual(frame.end_column, 14)

    def test_text(self):
        frame = self._make_one({"text": "QUERY TEXT"})
        self.assertEqual(frame.text, "QUERY TEXT")


class TestScriptStatistics(_Base):
    def _make_one(self, resource):
        from google.cloud.bigquery.job import ScriptStatistics

        return ScriptStatistics(resource)

    def test_evalutation_kind(self):
        stats = self._make_one({"evaluationKind": "EXPRESSION"})
        self.assertEqual(stats.evaluation_kind, "EXPRESSION")
        self.assertEqual(stats.stack_frames, [])

    def test_stack_frames(self):
        stats = self._make_one(
            {
                "stackFrames": [
                    {
                        "procedureId": "some-procedure",
                        "startLine": 5,
                        "startColumn": 29,
                        "endLine": 9,
                        "endColumn": 14,
                        "text": "QUERY TEXT",
                    },
                    {},
                ]
            }
        )
        stack_frames = stats.stack_frames
        self.assertEqual(len(stack_frames), 2)
        stack_frame = stack_frames[0]
        self.assertEqual(stack_frame.procedure_id, "some-procedure")
        self.assertEqual(stack_frame.start_line, 5)
        self.assertEqual(stack_frame.start_column, 29)
        self.assertEqual(stack_frame.end_line, 9)
        self.assertEqual(stack_frame.end_column, 14)
        self.assertEqual(stack_frame.text, "QUERY TEXT")
        stack_frame = stack_frames[1]
        self.assertIsNone(stack_frame.procedure_id)
        self.assertIsNone(stack_frame.start_line)
        self.assertIsNone(stack_frame.start_column)
        self.assertIsNone(stack_frame.end_line)
        self.assertIsNone(stack_frame.end_column)
        self.assertIsNone(stack_frame.text)


class TestTimelineEntry(_Base):
    ELAPSED_MS = 101
    ACTIVE_UNITS = 50
    PENDING_UNITS = 98
    COMPLETED_UNITS = 520
    SLOT_MILLIS = 12029

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import TimelineEntry

        return TimelineEntry

    def test_from_api_repr_empty(self):
        klass = self._get_target_class()
        entry = klass.from_api_repr({})
        self.assertIsNone(entry.elapsed_ms)
        self.assertIsNone(entry.active_units)
        self.assertIsNone(entry.pending_units)
        self.assertIsNone(entry.completed_units)
        self.assertIsNone(entry.slot_millis)

    def test_from_api_repr_normal(self):
        resource = {
            "elapsedMs": self.ELAPSED_MS,
            "activeUnits": self.ACTIVE_UNITS,
            "pendingUnits": self.PENDING_UNITS,
            "completedUnits": self.COMPLETED_UNITS,
            "totalSlotMs": self.SLOT_MILLIS,
        }
        klass = self._get_target_class()

        entry = klass.from_api_repr(resource)
        self.assertEqual(entry.elapsed_ms, self.ELAPSED_MS)
        self.assertEqual(entry.active_units, self.ACTIVE_UNITS)
        self.assertEqual(entry.pending_units, self.PENDING_UNITS)
        self.assertEqual(entry.completed_units, self.COMPLETED_UNITS)
        self.assertEqual(entry.slot_millis, self.SLOT_MILLIS)


class TestIncrementalResultStats:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import IncrementalResultStats

        return IncrementalResultStats

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        stats = self._make_one()
        assert stats.disabled_reason is None
        assert stats.result_set_last_replace_time is None
        assert stats.result_set_last_modify_time is None

    def test_from_api_repr_partial_stats(self):
        klass = self._get_target_class()
        stats = klass.from_api_repr({"disabledReason": "FOO"})

        assert isinstance(stats, klass)
        assert stats.disabled_reason == "FOO"
        assert stats.result_set_last_replace_time is None
        assert stats.result_set_last_modify_time is None

    def test_from_api_repr_full_stats(self):
        klass = self._get_target_class()
        stats = klass.from_api_repr(
            {
                "disabledReason": "BAR",
                "resultSetLastReplaceTime": "2025-01-02T03:04:05.06Z",
                "resultSetLastModifyTime": "2025-02-02T02:02:02.02Z",
            }
        )

        assert isinstance(stats, klass)
        assert stats.disabled_reason == "BAR"
        assert stats.result_set_last_replace_time == datetime.datetime(
            2025, 1, 2, 3, 4, 5, 60000, tzinfo=datetime.timezone.utc
        )
        assert stats.result_set_last_modify_time == datetime.datetime(
            2025, 2, 2, 2, 2, 2, 20000, tzinfo=datetime.timezone.utc
        )

    def test_from_api_repr_invalid_stats(self):
        klass = self._get_target_class()
        stats = klass.from_api_repr(
            {
                "disabledReason": "BAR",
                "resultSetLastReplaceTime": "xxx",
                "resultSetLastModifyTime": "yyy",
            }
        )

        assert isinstance(stats, klass)
        assert stats.disabled_reason == "BAR"
        assert stats.result_set_last_replace_time is None
        assert stats.result_set_last_modify_time is None
