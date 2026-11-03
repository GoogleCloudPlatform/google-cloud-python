# Copyright 2025 Google LLC
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

from datetime import datetime

import mock
import pytest
from opentelemetry.metrics import Counter, Histogram

from google.cloud.spanner_v1.metrics.metrics_tracer import MetricOpTracer, MetricsTracer

pytest.importorskip("opentelemetry")


@pytest.fixture
def metrics_tracer():
    mock_attempt_counter = mock.create_autospec(Counter, instance=True)
    mock_attempt_latency = mock.create_autospec(Histogram, instance=True)
    mock_operation_counter = mock.create_autospec(Counter, instance=True)
    mock_operation_latency = mock.create_autospec(Histogram, instance=True)
    mock_gfe_latency = mock.create_autospec(Histogram, instance=True)
    mock_gfe_missing = mock.create_autospec(Counter, instance=True)
    mock_afe_latency = mock.create_autospec(Histogram, instance=True)
    mock_afe_missing = mock.create_autospec(Counter, instance=True)
    tracer = MetricsTracer(
        enabled=True,
        instrument_attempt_latency=mock_attempt_latency,
        instrument_attempt_counter=mock_attempt_counter,
        instrument_operation_latency=mock_operation_latency,
        instrument_operation_counter=mock_operation_counter,
        client_attributes={"project_id": "test_project"},
        instrument_gfe_latency=mock_gfe_latency,
        instrument_gfe_connectivity_error_count=mock_gfe_missing,
        instrument_afe_latency=mock_afe_latency,
        instrument_afe_connectivity_error_count=mock_afe_missing,
    )
    tracer.afe_server_timing_enabled = True
    return tracer


def test_record_attempt_start(metrics_tracer):
    metrics_tracer.record_attempt_start()
    assert metrics_tracer.current_op.current_attempt is not None
    assert metrics_tracer.current_op.current_attempt.start_time is not None
    assert metrics_tracer.current_op.attempt_count == 1


def test_record_operation_start(metrics_tracer):
    metrics_tracer.record_operation_start()
    assert metrics_tracer.current_op.start_time is not None


def test_record_attempt_completion(metrics_tracer):
    metrics_tracer.record_attempt_start()
    metrics_tracer.record_attempt_completion()
    assert metrics_tracer.current_op.current_attempt.status == "OK"


def test_record_operation_completion(metrics_tracer):
    metrics_tracer.record_operation_start()
    metrics_tracer.record_attempt_start()
    metrics_tracer.record_attempt_completion()
    metrics_tracer.record_operation_completion()
    assert metrics_tracer.instrument_attempt_counter.add.call_count == 1
    assert metrics_tracer.instrument_attempt_latency.record.call_count == 1
    assert metrics_tracer.instrument_operation_latency.record.call_count == 1
    assert metrics_tracer.instrument_operation_counter.add.call_count == 1


def test_atempt_otel_attributes(metrics_tracer):
    from google.cloud.spanner_v1.metrics.constants import (
        METRIC_LABEL_KEY_DIRECT_PATH_USED,
    )

    metrics_tracer.current_op._current_attempt = None
    attributes = metrics_tracer._create_attempt_otel_attributes()
    assert METRIC_LABEL_KEY_DIRECT_PATH_USED not in attributes


def test_disabled(metrics_tracer):
    mock_operation = mock.create_autospec(MetricOpTracer, instance=True)
    metrics_tracer.enabled = False
    metrics_tracer._current_op = mock_operation

    # Attempt start should be skipped
    metrics_tracer.record_attempt_start()
    assert mock_operation.new_attempt.call_count == 0

    # Attempt completion should also be skipped
    metrics_tracer.record_attempt_completion()
    assert metrics_tracer.instrument_attempt_latency.record.call_count == 0

    # Operation start should be skipped
    metrics_tracer.record_operation_start()
    assert mock_operation.start.call_count == 0

    # Operation completion should also skip all metric logic
    metrics_tracer.record_operation_completion()
    assert metrics_tracer.instrument_attempt_counter.add.call_count == 0
    assert metrics_tracer.instrument_operation_latency.record.call_count == 0
    assert metrics_tracer.instrument_operation_counter.add.call_count == 0
    assert not metrics_tracer._create_operation_otel_attributes()
    assert not metrics_tracer._create_attempt_otel_attributes()


def test_get_ms_time_diff():
    # Create two datetime objects
    start_time = datetime(2025, 1, 1, 12, 0, 0)
    end_time = datetime(2025, 1, 1, 12, 0, 1)  # 1 second later

    # Calculate expected milliseconds difference
    expected_diff = 1000.0  # 1 second in milliseconds

    # Call the static method
    actual_diff = MetricsTracer._get_ms_time_diff(start_time, end_time)

    # Assert the expected and actual values are equal
    assert actual_diff == expected_diff


def test_get_ms_time_diff_negative():
    # Create two datetime objects where end is before start
    start_time = datetime(2025, 1, 1, 12, 0, 1)
    end_time = datetime(2025, 1, 1, 12, 0, 0)  # 1 second earlier

    # Calculate expected milliseconds difference
    expected_diff = -1000.0  # -1 second in milliseconds

    # Call the static method
    actual_diff = MetricsTracer._get_ms_time_diff(start_time, end_time)

    # Assert the expected and actual values are equal
    assert actual_diff == expected_diff


def test_set_project(metrics_tracer):
    metrics_tracer.set_project("test_project")
    assert metrics_tracer.client_attributes["project_id"] == "test_project"

    # Ensure it does not overwrite
    metrics_tracer.set_project("new_project")
    assert metrics_tracer.client_attributes["project_id"] == "test_project"


def test_set_instance(metrics_tracer):
    metrics_tracer.set_instance("test_instance")
    assert metrics_tracer.client_attributes["instance_id"] == "test_instance"

    # Ensure it does not overwrite
    metrics_tracer.set_instance("new_instance")
    assert metrics_tracer.client_attributes["instance_id"] == "test_instance"


def test_set_instance_config(metrics_tracer):
    metrics_tracer.set_instance_config("test_config")
    assert metrics_tracer.client_attributes["instance_config"] == "test_config"

    # Ensure it does not overwrite
    metrics_tracer.set_instance_config("new_config")
    assert metrics_tracer.client_attributes["instance_config"] == "test_config"


def test_set_location(metrics_tracer):
    metrics_tracer.set_location("test_location")
    assert metrics_tracer.client_attributes["location"] == "test_location"

    metrics_tracer.set_location("new_location")
    assert metrics_tracer.client_attributes["location"] == "test_location"


def test_set_resource_info(metrics_tracer):
    resource_info = {
        "project": "test_project",
        "instance": "test_instance",
        "database": "test_database",
    }
    metrics_tracer.set_resource_info(resource_info)
    assert metrics_tracer.client_attributes["project_id"] == "test_project"
    assert metrics_tracer.client_attributes["instance_id"] == "test_instance"
    assert metrics_tracer.client_attributes["database"] == "test_database"

    # None and empty resource_info are safe no-ops
    metrics_tracer.set_resource_info(None)
    metrics_tracer.set_resource_info({})
    assert metrics_tracer.client_attributes["project_id"] == "test_project"


def test_set_client_hash(metrics_tracer):
    metrics_tracer.set_client_hash("test_hash")
    assert metrics_tracer.client_attributes["client_hash"] == "test_hash"

    # Ensure it does not overwrite
    metrics_tracer.set_client_hash("new_hash")
    assert metrics_tracer.client_attributes["client_hash"] == "test_hash"


def test_set_client_uid(metrics_tracer):
    metrics_tracer.set_client_uid("test_uid")
    assert metrics_tracer.client_attributes["client_uid"] == "test_uid"

    # Ensure it does not overwrite
    metrics_tracer.set_client_uid("new_uid")
    assert metrics_tracer.client_attributes["client_uid"] == "test_uid"


def test_set_client_name(metrics_tracer):
    metrics_tracer.set_client_name("test_name")
    assert metrics_tracer.client_attributes["client_name"] == "test_name"

    # Ensure it does not overwrite
    metrics_tracer.set_client_name("new_name")
    assert metrics_tracer.client_attributes["client_name"] == "test_name"


def test_set_database(metrics_tracer):
    metrics_tracer.set_database("test_db")
    assert metrics_tracer.client_attributes["database"] == "test_db"

    # Ensure it does not overwrite
    metrics_tracer.set_database("new_db")
    assert metrics_tracer.client_attributes["database"] == "test_db"


def test_enable_direct_path(metrics_tracer):
    metrics_tracer.enable_direct_path(True)
    assert metrics_tracer.client_attributes["directpath_enabled"] == "True"

    # Ensure it does not overwrite
    metrics_tracer.enable_direct_path(False)
    assert metrics_tracer.client_attributes["directpath_enabled"] == "True"


def test_set_method(metrics_tracer):
    metrics_tracer.set_method("test_method")
    assert metrics_tracer.client_attributes["method"] == "test_method"

    # Ensure it does not overwrite
    metrics_tracer.set_method("new_method")
    assert metrics_tracer.client_attributes["method"] == "test_method"


def test_record_gfe_latency(metrics_tracer):
    mock_gfe_latency = mock.create_autospec(Histogram, instance=True)
    metrics_tracer._instrument_gfe_latency = mock_gfe_latency

    # Test when tracing is enabled
    metrics_tracer.record_gfe_latency(100)
    assert mock_gfe_latency.record.call_count == 1
    assert mock_gfe_latency.record.call_args[1]["amount"] == 100
    assert (
        mock_gfe_latency.record.call_args[1]["attributes"]
        == metrics_tracer._create_attempt_otel_attributes()
    )

    # Test when tracing is disabled
    metrics_tracer.enabled = False
    metrics_tracer.record_gfe_latency(200)
    assert mock_gfe_latency.record.call_count == 1  # Should not increment
    metrics_tracer.enabled = True  # Reset for next test


def test_record_gfe_connectivity_error_count(metrics_tracer):
    mock_gfe_connectivity_error_count = mock.create_autospec(Counter, instance=True)
    metrics_tracer._instrument_gfe_connectivity_error_count = (
        mock_gfe_connectivity_error_count
    )

    # Test when tracing is enabled
    metrics_tracer.record_gfe_connectivity_error_count()
    assert mock_gfe_connectivity_error_count.add.call_count == 1
    assert mock_gfe_connectivity_error_count.add.call_args[1]["amount"] == 1
    assert (
        mock_gfe_connectivity_error_count.add.call_args[1]["attributes"]
        == metrics_tracer._create_attempt_otel_attributes()
    )

    # Test when tracing is disabled
    metrics_tracer.enabled = False
    metrics_tracer.record_gfe_connectivity_error_count()
    assert mock_gfe_connectivity_error_count.add.call_count == 1  # Should not increment
    metrics_tracer.enabled = True  # Reset for next test


def test_extract_front_end_latencies():
    # Valid trailing metadata list of tuples
    metadata_list = [
        ("server-timing", "gfet4t7; dur=123"),
        ("server-timing", "afe; dur=100"),
    ]
    assert MetricsTracer.extract_front_end_latencies(metadata_list) == (123, 100)

    # Combined header in single value (standard Spanner wire response)
    combined = [("server-timing", "gfet4t7; dur=55, afe; dur=23")]
    assert MetricsTracer.extract_front_end_latencies(combined) == (55, 23)

    # Bytes header key in list of tuples
    bytes_list = [(b"server-timing", "gfet4t7; dur=55, afe; dur=23")]
    assert MetricsTracer.extract_front_end_latencies(bytes_list) == (55, 23)

    # Valid metadata dict
    metadata_dict = {"server-timing": "gfet4t7; dur=456"}
    assert MetricsTracer.extract_front_end_latencies(metadata_dict) == (456, None)

    # Metadata dict with bytes key and combined value
    metadata_dict_bytes = {b"server-timing": "gfet4t7; dur=55, afe; dur=23"}
    assert MetricsTracer.extract_front_end_latencies(metadata_dict_bytes) == (55, 23)

    # Metadata dict with mixed case key
    metadata_dict_case = {"Server-Timing": "gfet4t7; dur=55, afe; dur=23"}
    assert MetricsTracer.extract_front_end_latencies(metadata_dict_case) == (55, 23)

    # Metadata dict with list of values
    metadata_dict_list = {"server-timing": ["gfet4t7; dur=12", "afe; dur=34"]}
    assert MetricsTracer.extract_front_end_latencies(metadata_dict_list) == (12, 34)

    # Floating point latencies truncated to int
    float_headers = [("server-timing", "gfet4t7; dur=55.8, afe; dur=23.2")]
    assert MetricsTracer.extract_front_end_latencies(float_headers) == (55, 23)

    # Bytes header value
    bytes_val = [("server-timing", b"gfet4t7; dur=55, afe; dur=23")]
    assert MetricsTracer.extract_front_end_latencies(bytes_val) == (55, 23)

    # Generator / custom iterable (simulating grpc.aio.Metadata)
    def timing_generator():
        yield ("unrelated", "1")
        yield ("server-timing", "gfet4t7; dur=77, afe; dur=88")

    assert MetricsTracer.extract_front_end_latencies(timing_generator()) == (77, 88)

    # Dict with multiple case variants (ensuring no premature loop termination)
    metadata_dict_multiple_cases = {
        "Server-Timing": "gfet4t7; dur=55",
        "server-timing": "afe; dur=23",
    }
    assert MetricsTracer.extract_front_end_latencies(metadata_dict_multiple_cases) == (
        55,
        23,
    )

    # Sequence with list-of-values
    metadata_seq_list = [("server-timing", ["gfet4t7; dur=12", "afe; dur=34"])]
    assert MetricsTracer.extract_front_end_latencies(metadata_seq_list) == (12, 34)

    # Missing header
    assert MetricsTracer.extract_front_end_latencies([("other-header", "val")]) == (
        None,
        None,
    )
    assert MetricsTracer.extract_front_end_latencies(None) == (None, None)

    # Non-iterable or malformed metadata
    assert MetricsTracer.extract_front_end_latencies(12345) == (None, None)
    assert MetricsTracer.extract_front_end_latencies([("single_item",)]) == (None, None)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "gfet4t7; dur=invalid")]
    ) == (None, None)
    # Trigger ValueError in float conversion (dur=.)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "gfet4t7; dur=.")]
    ) == (None, None)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "afe; dur=.")]
    ) == (None, None)
    # Non-string, non-bytes header value
    assert MetricsTracer.extract_front_end_latencies([("server-timing", 12345)]) == (
        None,
        None,
    )
    # Non-decodable bytes fallback
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", b"\xff\xfe\xfd")]
    ) == (None, None)

    # Non-matching bytes key and non-str non-bytes key
    assert MetricsTracer.extract_front_end_latencies(
        [(b"unrelated", "val"), (12345, "val")]
    ) == (None, None)

    # Empty header value
    assert MetricsTracer.extract_front_end_latencies([("server-timing", "")]) == (
        None,
        None,
    )

    # Separate headers where first sets AFE, second sets GFE
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "afe; dur=20"), ("server-timing", "gfet4t7; dur=30")]
    ) == (30, 20)

    # Extremely large latency value (>308 digits) handled safely without raising OverflowError
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "gfet4t7; dur=" + ("9" * 400))]
    ) == (None, None)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "afe; dur=" + ("9" * 400))]
    ) == (None, None)


def test_record_front_end_metrics(metrics_tracer):
    mock_gfe_latency = mock.create_autospec(Histogram, instance=True)
    mock_gfe_missing = mock.create_autospec(Counter, instance=True)
    mock_afe_latency = mock.create_autospec(Histogram, instance=True)
    mock_afe_missing = mock.create_autospec(Counter, instance=True)
    metrics_tracer._instrument_gfe_latency = mock_gfe_latency
    metrics_tracer._instrument_gfe_connectivity_error_count = mock_gfe_missing
    metrics_tracer._instrument_afe_latency = mock_afe_latency
    metrics_tracer._instrument_afe_connectivity_error_count = mock_afe_missing

    # With header
    metrics_tracer.record_front_end_metrics(
        [("server-timing", "gfet4t7; dur=88"), ("server-timing", "afe; dur=90")]
    )
    assert mock_gfe_latency.record.call_count == 1
    assert mock_gfe_latency.record.call_args[1]["amount"] == 88
    assert mock_gfe_missing.add.call_count == 0
    assert mock_afe_latency.record.call_count == 1
    assert mock_afe_latency.record.call_args[1]["amount"] == 90
    assert mock_afe_missing.add.call_count == 0

    # Without header
    metrics_tracer.record_front_end_metrics([("other", "1")])
    assert mock_gfe_latency.record.call_count == 1
    assert mock_gfe_missing.add.call_count == 1
    assert mock_afe_latency.record.call_count == 1
    assert mock_afe_missing.add.call_count == 1

    # When disabled, record_front_end_metrics does nothing
    metrics_tracer.enabled = False
    metrics_tracer.record_front_end_metrics(
        [("server-timing", "gfet4t7; dur=88"), ("server-timing", "afe; dur=90")]
    )
    assert mock_gfe_latency.record.call_count == 1
    assert mock_afe_latency.record.call_count == 1
    metrics_tracer.enabled = True


def test_record_afe_latency(metrics_tracer):
    mock_afe_latency = mock.create_autospec(Histogram, instance=True)
    metrics_tracer._instrument_afe_latency = mock_afe_latency

    metrics_tracer.record_afe_latency(100)
    assert mock_afe_latency.record.call_count == 1
    assert mock_afe_latency.record.call_args[1]["amount"] == 100
    assert (
        mock_afe_latency.record.call_args[1]["attributes"]
        == metrics_tracer._create_attempt_otel_attributes()
    )

    metrics_tracer.afe_server_timing_enabled = False
    metrics_tracer.record_afe_latency(300)
    assert mock_afe_latency.record.call_count == 1

    metrics_tracer.enabled = False
    metrics_tracer.record_afe_latency(200)
    assert mock_afe_latency.record.call_count == 1
    metrics_tracer.enabled = True


def test_record_afe_connectivity_error_count(metrics_tracer):
    mock_afe_missing = mock.create_autospec(Counter, instance=True)
    metrics_tracer._instrument_afe_connectivity_error_count = mock_afe_missing

    metrics_tracer.record_afe_connectivity_error_count()
    assert mock_afe_missing.add.call_count == 1
    assert mock_afe_missing.add.call_args[1]["amount"] == 1
    assert (
        mock_afe_missing.add.call_args[1]["attributes"]
        == metrics_tracer._create_attempt_otel_attributes()
    )

    metrics_tracer.afe_server_timing_enabled = False
    metrics_tracer.record_afe_connectivity_error_count()
    assert mock_afe_missing.add.call_count == 1

    metrics_tracer.enabled = False
    metrics_tracer.record_afe_connectivity_error_count()
    assert mock_afe_missing.add.call_count == 1
    metrics_tracer.enabled = True


def test_attribute_caching_and_invalidation(metrics_tracer):
    # Test attempt attribute caching
    metrics_tracer.current_op.new_attempt()
    metrics_tracer.current_op.current_attempt.status = "OK"

    first_attempt_attrs = metrics_tracer._create_attempt_otel_attributes()
    second_attempt_attrs = metrics_tracer._create_attempt_otel_attributes()
    assert first_attempt_attrs == second_attempt_attrs
    # Same cached object returned
    assert first_attempt_attrs is second_attempt_attrs

    # Changing attempt status returns new object
    metrics_tracer.current_op.current_attempt.status = "UNAVAILABLE"
    third_attempt_attrs = metrics_tracer._create_attempt_otel_attributes()
    assert third_attempt_attrs["status"] == "UNAVAILABLE"
    assert third_attempt_attrs is not first_attempt_attrs

    # Test operation attribute caching
    first_op_attrs = metrics_tracer._create_operation_otel_attributes()
    second_op_attrs = metrics_tracer._create_operation_otel_attributes()
    assert first_op_attrs is second_op_attrs

    # Non-matching AFE and GFE patterns when substring is present (lookbehind boundary check)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "safe; dur=55")]
    ) == (None, None)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "custom-afe; dur=20")]
    ) == (None, None)
    assert MetricsTracer.extract_front_end_latencies(
        [("server-timing", "x-gfet4t7; dur=15")]
    ) == (None, None)
    assert MetricsTracer.extract_front_end_latencies(
        [
            (
                "server-timing",
                "safe; dur=55, afe; dur=25, x-gfet4t7; dur=10, gfet4t7; dur=35",
            )
        ]
    ) == (35, 25)

    # Setter method invalidates cache
    empty_tracer = MetricsTracer(
        enabled=True,
        instrument_attempt_latency=mock.MagicMock(),
        instrument_attempt_counter=mock.MagicMock(),
        instrument_operation_latency=mock.MagicMock(),
        instrument_operation_counter=mock.MagicMock(),
        client_attributes={},
        instrument_gfe_latency=mock.MagicMock(),
        instrument_gfe_connectivity_error_count=mock.MagicMock(),
        instrument_afe_latency=mock.MagicMock(),
        instrument_afe_connectivity_error_count=mock.MagicMock(),
    )
    empty_tracer.set_project("new-project")
    assert empty_tracer.client_attributes["project_id"] == "new-project"

    metrics_tracer.set_instance("updated-instance")
    invalidated_attrs = metrics_tracer._create_attempt_otel_attributes()
    assert invalidated_attrs["instance_id"] == "updated-instance"
    assert invalidated_attrs is not third_attempt_attrs

    # Direct mutation of client_attributes invalidates cache via _ObservableDict
    before_direct = metrics_tracer._create_attempt_otel_attributes()
    metrics_tracer.client_attributes["database"] = "mutated_db"
    after_direct = metrics_tracer._create_attempt_otel_attributes()
    assert after_direct["database"] == "mutated_db"
    assert after_direct is not before_direct

    # _ObservableDict copy returns standard dict
    attrs_copy = metrics_tracer.client_attributes.copy()
    assert type(attrs_copy) is dict
    assert attrs_copy["database"] == "mutated_db"

    # Other observable dict operations trigger invalidation
    metrics_tracer.client_attributes.update({"instance_id": "updated_via_update"})
    assert (
        metrics_tracer._create_attempt_otel_attributes()["instance_id"]
        == "updated_via_update"
    )
    # setdefault when key is new
    metrics_tracer.client_attributes.setdefault("new_key", "default_val")
    assert metrics_tracer._create_attempt_otel_attributes()["new_key"] == "default_val"
    # setdefault when key already exists
    assert (
        metrics_tracer.client_attributes.setdefault("new_key", "other_val")
        == "default_val"
    )
    # pop
    metrics_tracer.client_attributes.pop("new_key")
    assert "new_key" not in metrics_tracer._create_attempt_otel_attributes()

    # delitem
    metrics_tracer.client_attributes["to_delete"] = "val"
    del metrics_tracer.client_attributes["to_delete"]
    assert "to_delete" not in metrics_tracer._create_attempt_otel_attributes()

    # popitem
    metrics_tracer.client_attributes["to_pop"] = "val"
    metrics_tracer.client_attributes.popitem()

    # In-place union (|=) triggers invalidation
    attrs = metrics_tracer.client_attributes
    attrs |= {"instance_id": "updated_via_ior"}
    assert (
        metrics_tracer._create_attempt_otel_attributes()["instance_id"]
        == "updated_via_ior"
    )

    # ObservableDict with no on_change callback
    from google.cloud.spanner_v1.metrics.metrics_tracer import _ObservableDict

    no_callback_dict = _ObservableDict({"a": 1})
    no_callback_dict["b"] = 2
    del no_callback_dict["a"]
    no_callback_dict.update({"c": 3})
    no_callback_dict |= {"e": 5}
    no_callback_dict.setdefault("d", 4)
    no_callback_dict.pop("c")
    no_callback_dict.popitem()
    no_callback_dict.clear()

    # clear on client_attributes
    metrics_tracer.client_attributes.clear()
    assert metrics_tracer._create_attempt_otel_attributes() == {"status": "UNAVAILABLE"}

    # Ensure client_attributes and cached attributes are dict instances for backward compatibility
    assert isinstance(metrics_tracer.client_attributes, dict)
    assert isinstance(first_attempt_attrs, dict)
    assert isinstance(first_op_attrs, dict)
