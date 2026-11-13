# Copyright 2016 Google LLC All rights reserved.
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


import datetime
import unittest
import uuid
from datetime import timezone

import mock
from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes

from google.cloud.spanner_v1 import ExecuteSqlRequest, TransactionOptions, _helpers


class Test_to_query_options(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _to_query_options

        return _to_query_options(*args, **kw)

    def test_none(self):
        self.assertIsNone(self._callFUT(None))

    def test_empty_dict(self):
        self.assertIsNone(self._callFUT({}))

    def test_dict_with_empty_values(self):
        self.assertIsNone(self._callFUT({"optimizer_version": ""}))

    def test_valid_dict(self):
        expected = ExecuteSqlRequest.QueryOptions(optimizer_version="1")
        result = self._callFUT({"optimizer_version": "1"})
        self.assertEqual(result, expected)

    def test_empty_proto_object(self):
        self.assertIsNone(self._callFUT(ExecuteSqlRequest.QueryOptions()))

    def test_populated_proto_object(self):
        options = ExecuteSqlRequest.QueryOptions(optimizer_version="1")
        result = self._callFUT(options)
        self.assertEqual(result, options)

    def test_invalid_type(self):
        for invalid_value in ("invalid", 123, "", [], False):
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaises(TypeError):
                    self._callFUT(invalid_value)

    def test_unknown_key_with_empty_value_raises_error(self):
        with self.assertRaises(ValueError):
            self._callFUT({"optmizer_version": ""})

    def test_unknown_key_with_non_empty_value_raises_error(self):
        with self.assertRaises(ValueError):
            self._callFUT({"optmizer_version": "1"})


class Test_merge_query_options(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _merge_query_options

        return _merge_query_options(*args, **kw)

    def test_base_none_and_merge_none(self):
        base = merge = None
        result = self._callFUT(base, merge)
        self.assertIsNone(result)

    def test_base_dict_and_merge_none(self):
        base = {
            "optimizer_version": "2",
            "optimizer_statistics_package": "auto_20191128_14_47_22UTC",
        }
        merge = None
        expected = ExecuteSqlRequest.QueryOptions(
            optimizer_version="2",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        result = self._callFUT(base, merge)
        self.assertEqual(result, expected)

    def test_base_empty_and_merge_empty(self):
        base = ExecuteSqlRequest.QueryOptions()
        merge = ExecuteSqlRequest.QueryOptions()
        result = self._callFUT(base, merge)
        self.assertIsNone(result)

    def test_base_none_merge_object(self):
        base = None
        merge = ExecuteSqlRequest.QueryOptions(
            optimizer_version="3",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        result = self._callFUT(base, merge)
        self.assertEqual(result, merge)

    def test_base_none_merge_dict(self):
        base = None
        merge = {"optimizer_version": "3"}
        expected = ExecuteSqlRequest.QueryOptions(optimizer_version="3")
        result = self._callFUT(base, merge)
        self.assertEqual(result, expected)

    def test_base_object_merge_dict(self):
        base = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        merge = {"optimizer_version": "3"}
        expected = ExecuteSqlRequest.QueryOptions(
            optimizer_version="3",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        result = self._callFUT(base, merge)
        self.assertEqual(result, expected)

    def test_base_object_and_merge_none(self):
        base = ExecuteSqlRequest.QueryOptions(
            optimizer_version="2",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        result = self._callFUT(base, None)
        self.assertEqual(result, base)

    def test_base_empty_object_and_merge_none(self):
        base = ExecuteSqlRequest.QueryOptions()
        result = self._callFUT(base, None)
        self.assertIsNone(result)

    def test_base_none_merge_empty_object(self):
        merge = ExecuteSqlRequest.QueryOptions()
        result = self._callFUT(None, merge)
        self.assertIsNone(result)

    def test_base_object_not_mutated_on_merge(self):
        base = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        merge = {"optimizer_version": "3"}
        result = self._callFUT(base, merge)
        expected = ExecuteSqlRequest.QueryOptions(
            optimizer_version="3",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        self.assertEqual(result, expected)
        self.assertEqual(base.optimizer_version, "1")

    def test_base_dict_merge_dict(self):
        base = {"optimizer_version": "1"}
        merge = {"optimizer_statistics_package": "auto_20191128_14_47_22UTC"}
        expected = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        result = self._callFUT(base, merge)
        self.assertEqual(result, expected)

    def test_base_dict_override_dict(self):
        base = {
            "optimizer_version": "1",
            "optimizer_statistics_package": "pkg1",
        }
        merge = {"optimizer_version": "2"}
        expected = ExecuteSqlRequest.QueryOptions(
            optimizer_version="2",
            optimizer_statistics_package="pkg1",
        )
        result = self._callFUT(base, merge)
        self.assertEqual(result, expected)

    def test_base_dict_empty_merge_none(self):
        result = self._callFUT({}, None)
        self.assertIsNone(result)

    def test_base_none_merge_dict_empty(self):
        result = self._callFUT(None, {})
        self.assertIsNone(result)

    def test_base_empty_dict_merge_empty_dict(self):
        result = self._callFUT({}, {})
        self.assertIsNone(result)

    def test_base_empty_dict_merge_object(self):
        merge = ExecuteSqlRequest.QueryOptions(optimizer_version="1")
        result = self._callFUT({}, merge)
        self.assertEqual(result, merge)

    def test_base_object_merge_empty_dict(self):
        base = ExecuteSqlRequest.QueryOptions(optimizer_version="1")
        result = self._callFUT(base, {})
        self.assertEqual(result, base)

    def test_base_object_merge_object(self):
        base = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1",
            optimizer_statistics_package="pkg1",
        )
        merge = ExecuteSqlRequest.QueryOptions(optimizer_version="2")
        result = self._callFUT(base, merge)
        expected = ExecuteSqlRequest.QueryOptions(
            optimizer_version="2",
            optimizer_statistics_package="pkg1",
        )
        self.assertEqual(result, expected)
        self.assertEqual(base.optimizer_version, "1")
        self.assertEqual(base.optimizer_statistics_package, "pkg1")
        self.assertEqual(merge.optimizer_version, "2")
        self.assertEqual(merge.optimizer_statistics_package, "")

    def test_invalid_type_raises_error(self):
        for invalid_value in ("invalid", 123, "", [], False):
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaises(TypeError):
                    self._callFUT(invalid_value, None)
                with self.assertRaises(TypeError):
                    self._callFUT(None, invalid_value)

    def test_unknown_key_in_base_raises_error(self):
        with self.assertRaises(ValueError):
            self._callFUT({"optmizer_version": ""}, None)
        with self.assertRaises(ValueError):
            self._callFUT({"optmizer_version": "1"}, None)

    def test_unknown_key_in_merge_raises_error(self):
        with self.assertRaises(ValueError):
            self._callFUT(None, {"optmizer_version": ""})
        with self.assertRaises(ValueError):
            self._callFUT(None, {"optmizer_version": "1"})


class Test_as_raw_pb(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _as_raw_pb

        return _as_raw_pb(*args, **kw)

    def test_proto_plus_message_is_unwrapped(self):
        from google.cloud.spanner_v1 import RequestOptions

        request_options = RequestOptions(request_tag="tag-1")
        result = self._callFUT(request_options, RequestOptions)
        self.assertIs(type(result), RequestOptions.pb())
        self.assertEqual(result, RequestOptions.pb(request_options))

    def test_raw_protobuf_message_is_returned_unchanged(self):
        from google.cloud.spanner_v1 import RequestOptions

        request_options_pb = RequestOptions.pb(RequestOptions(request_tag="tag-1"))
        self.assertIs(
            self._callFUT(request_options_pb, RequestOptions), request_options_pb
        )

    def test_dict_is_converted(self):
        from google.cloud.spanner_v1 import RequestOptions

        result = self._callFUT({"request_tag": "tag-1"}, RequestOptions)
        self.assertIs(type(result), RequestOptions.pb())
        self.assertEqual(result.request_tag, "tag-1")

    def test_dict_containing_a_proto_plus_message_is_converted(self):
        from google.cloud.spanner_v1 import DirectedReadOptions

        # The raw protobuf constructor rejects a proto-plus message used as a
        # dict value, so dicts must be routed through proto-plus instead.
        include_replicas = DirectedReadOptions.IncludeReplicas(
            auto_failover_disabled=True
        )
        result = self._callFUT(
            {"include_replicas": include_replicas}, DirectedReadOptions
        )
        self.assertIs(type(result), DirectedReadOptions.pb())
        self.assertTrue(result.include_replicas.auto_failover_disabled)

    def test_none_is_returned_unchanged(self):
        from google.cloud.spanner_v1 import RequestOptions

        self.assertIsNone(self._callFUT(None, RequestOptions))


class Test_make_execute_sql_request(unittest.TestCase):
    SESSION_NAME = "projects/p/instances/i/databases/d/sessions/s"
    SQL = "SELECT * FROM Singers WHERE SingerId = @singer_id"

    def _callFUT(self, **kw):
        from google.cloud.spanner_v1._helpers import _make_execute_sql_request

        return _make_execute_sql_request(
            session_name=self.SESSION_NAME, sql=self.SQL, seqno=1, **kw
        )

    def _assert_matches_proto_plus(self, **kw):
        """Assert the fast builder matches the proto-plus constructor exactly.

        Comparing serialized bytes as well as message equality is what pins
        field presence: an explicitly set but empty sub-message is a different
        request on the wire than an absent one.
        """
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        # The builder names this argument `partition`, matching `execute_sql`,
        # while the proto field is `partition_token`.
        partition = kw.pop("partition", None)

        expected = ExecuteSqlRequest(
            session=self.SESSION_NAME,
            sql=self.SQL,
            seqno=1,
            partition_token=partition,
            **kw,
        )
        result = self._callFUT(partition=partition, **kw)

        self.assertIsInstance(result, ExecuteSqlRequest)
        self.assertEqual(result, expected)
        self.assertEqual(
            ExecuteSqlRequest.serialize(result),
            ExecuteSqlRequest.serialize(expected),
        )
        return result

    def test_minimal(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        result = self._assert_matches_proto_plus()
        self.assertEqual(result.session, self.SESSION_NAME)
        self.assertEqual(result.sql, self.SQL)
        self.assertEqual(result.seqno, 1)
        self.assertFalse(ExecuteSqlRequest.pb(result).HasField("params"))

    def test_all_fields_proto_plus(self):
        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1 import DirectedReadOptions, ExecuteSqlRequest
        from google.cloud.spanner_v1._helpers import _make_value_pb
        from google.cloud.spanner_v1.types import RequestOptions, Type, TypeCode

        self._assert_matches_proto_plus(
            params=Struct(fields={"singer_id": _make_value_pb(42)}),
            param_types={"singer_id": Type(code=TypeCode.INT64)},
            query_mode=ExecuteSqlRequest.QueryMode.PROFILE,
            partition=b"partition-token",
            query_options=ExecuteSqlRequest.QueryOptions(optimizer_version="1"),
            request_options=RequestOptions(
                priority=RequestOptions.Priority.PRIORITY_HIGH,
                request_tag="tag-1",
                transaction_tag="transaction-tag-1",
            ),
            last_statement=True,
            data_boost_enabled=True,
            directed_read_options=DirectedReadOptions(
                include_replicas=DirectedReadOptions.IncludeReplicas(
                    replica_selections=[
                        DirectedReadOptions.ReplicaSelection(
                            location="us-central1",
                            type_=DirectedReadOptions.ReplicaSelection.Type.READ_ONLY,
                        )
                    ],
                    auto_failover_disabled=True,
                )
            ),
        )

    def test_all_fields_as_dicts(self):
        from google.cloud.spanner_v1.types import TypeCode

        self._assert_matches_proto_plus(
            params={"singer_id": 42},
            param_types={"singer_id": {"code": TypeCode.INT64}},
            query_mode="PROFILE",
            partition=b"partition-token",
            query_options={"optimizer_version": "1"},
            request_options={"request_tag": "tag-1"},
            last_statement=True,
            data_boost_enabled=True,
            directed_read_options={
                "include_replicas": {"auto_failover_disabled": True}
            },
        )

    def test_all_fields_as_raw_protobuf(self):
        from google.cloud.spanner_v1 import DirectedReadOptions, ExecuteSqlRequest
        from google.cloud.spanner_v1.types import RequestOptions, Type, TypeCode

        self._assert_matches_proto_plus(
            param_types={"singer_id": Type.pb(Type(code=TypeCode.INT64))},
            query_options=ExecuteSqlRequest.QueryOptions.pb(
                ExecuteSqlRequest.QueryOptions(optimizer_version="1")
            ),
            request_options=RequestOptions.pb(RequestOptions(request_tag="tag-1")),
            directed_read_options=DirectedReadOptions.pb(
                DirectedReadOptions(
                    include_replicas=DirectedReadOptions.IncludeReplicas(
                        auto_failover_disabled=True
                    )
                )
            ),
        )

    def test_query_mode_accepts_name_and_value(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        profile = ExecuteSqlRequest.QueryMode.PROFILE
        for query_mode in ("PROFILE", profile, profile.value):
            with self.subTest(query_mode=query_mode):
                result = self._assert_matches_proto_plus(query_mode=query_mode)
                self.assertEqual(result.query_mode, profile)

    def test_invalid_query_mode_name_raises_key_error(self):
        # Matches what the proto-plus constructor raises today.
        with self.assertRaises(KeyError):
            self._callFUT(query_mode="NOT_A_QUERY_MODE")

    def test_empty_params_preserves_field_presence(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        # `execute_sql` passes `{}` rather than `None` when a query has no
        # parameters, which sets the `params` field to an explicit empty Struct.
        result = self._assert_matches_proto_plus(params={})
        self.assertTrue(ExecuteSqlRequest.pb(result).HasField("params"))

    def test_empty_struct_params_preserves_field_presence(self):
        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1 import ExecuteSqlRequest

        result = self._assert_matches_proto_plus(params=Struct())
        self.assertTrue(ExecuteSqlRequest.pb(result).HasField("params"))

    def test_params_none_leaves_field_unset(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        # The proto-plus constructor rejects `params=None`, so this case has no
        # counterpart to compare against.
        result = self._callFUT(params=None)
        self.assertFalse(ExecuteSqlRequest.pb(result).HasField("params"))

    def test_empty_param_types_leaves_map_empty(self):
        for param_types in (None, {}):
            with self.subTest(param_types=param_types):
                result = self._assert_matches_proto_plus(param_types=param_types)
                self.assertEqual(len(result.param_types), 0)

    def test_dicts_containing_proto_plus_messages(self):
        from google.cloud.spanner_v1 import DirectedReadOptions
        from google.cloud.spanner_v1.types import Type, TypeCode

        # `directed_read_options` and `param_types` are passed straight from
        # user input, so a dict holding a proto-plus message is reachable from
        # the public API and must behave exactly like the proto-plus
        # constructor.
        self._assert_matches_proto_plus(
            param_types={
                "ids": {
                    "code": TypeCode.ARRAY,
                    "array_element_type": Type(code=TypeCode.INT64),
                }
            },
            directed_read_options={
                "include_replicas": DirectedReadOptions.IncludeReplicas(
                    auto_failover_disabled=True
                )
            },
        )

    def test_params_dict_of_value_messages_is_not_supported(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import ExecuteSqlRequest

        # This is the one documented difference from the proto-plus
        # constructor. It is unreachable from `execute_sql`, which always
        # builds an already-encoded `Struct`, and it cannot be supported
        # without re-encoding the parameter values by hand -- which would risk
        # encoding them differently than `Struct` does.
        params = {"singer_id": Value(string_value="42")}

        ExecuteSqlRequest(
            session=self.SESSION_NAME, sql=self.SQL, seqno=1, params=params
        )
        with self.assertRaises(ValueError):
            self._callFUT(params=params)

    def test_inputs_are_copied_not_aliased(self):
        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1._helpers import _make_value_pb
        from google.cloud.spanner_v1.types import RequestOptions

        request_options = RequestOptions(request_tag="tag-1")
        params = Struct(fields={"singer_id": _make_value_pb(42)})

        expected_request_options = RequestOptions(request_tag="tag-1")
        expected_params = Struct()
        expected_params.CopyFrom(params)

        result = self._callFUT(request_options=request_options, params=params)
        result.request_options.request_tag = "mutated"
        result.params["singer_id"] = "mutated"

        # The mutations must land on the result...
        self.assertEqual(result.request_options.request_tag, "mutated")
        self.assertEqual(result.params["singer_id"], "mutated")
        # ...and must not be visible through the caller's objects.
        self.assertEqual(request_options, expected_request_options)
        self.assertEqual(params, expected_params)

    def test_builder_covers_every_request_field(self):
        import inspect

        from google.cloud.spanner_v1 import ExecuteSqlRequest
        from google.cloud.spanner_v1._helpers import _make_execute_sql_request

        fields = {field.name for field in ExecuteSqlRequest.pb().DESCRIPTOR.fields}
        parameters = set(inspect.signature(_make_execute_sql_request).parameters)
        self.assertEqual(
            fields - parameters,
            {
                # Renamed to match `execute_sql`'s public keyword arguments.
                "session",
                "partition_token",
                # Set by the retry layer in `_restart_on_unavailable`.
                "transaction",
                "resume_token",
                # Not surfaced by the handwritten layer.
                "routing_hint",
            },
            "ExecuteSqlRequest gained or lost a field; thread it through "
            "_make_execute_sql_request (or add it to this exclusion list).",
        )


class Test_get_cloud_region(unittest.TestCase):
    def setUp(self):
        _helpers._cloud_region = None

    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _get_cloud_region

        return _get_cloud_region(*args, **kw)

    @unittest.skipUnless(
        hasattr(_helpers, "GoogleCloudResourceDetector")
        and _helpers.GoogleCloudResourceDetector is not None,
        "opentelemetry-resourcedetector-gcp not installed",
    )
    @mock.patch("google.cloud.spanner_v1._helpers.GoogleCloudResourceDetector.detect")
    def test_get_location_with_region(self, mock_detect):
        """Test that _get_cloud_region returns the region when detected."""
        mock_resource = Resource.create(
            {ResourceAttributes.CLOUD_REGION: "us-central1"}
        )
        mock_detect.return_value = mock_resource

        location = self._callFUT()
        self.assertEqual(location, "us-central1")

    @unittest.skipUnless(
        hasattr(_helpers, "GoogleCloudResourceDetector")
        and _helpers.GoogleCloudResourceDetector is not None,
        "opentelemetry-resourcedetector-gcp not installed",
    )
    @mock.patch("google.cloud.spanner_v1._helpers.GoogleCloudResourceDetector.detect")
    def test_get_location_without_region(self, mock_detect):
        """Test that _get_cloud_region returns 'global' when no region is detected."""
        mock_resource = Resource.create({})  # No region attribute
        mock_detect.return_value = mock_resource

        location = self._callFUT()
        self.assertEqual(location, "global")

    @unittest.skipUnless(
        hasattr(_helpers, "GoogleCloudResourceDetector")
        and _helpers.GoogleCloudResourceDetector is not None,
        "opentelemetry-resourcedetector-gcp not installed",
    )
    @mock.patch("google.cloud.spanner_v1._helpers.GoogleCloudResourceDetector.detect")
    def test_get_location_with_exception(self, mock_detect):
        """Test that _get_cloud_region returns 'global' and logs a warning on exception."""
        mock_detect.side_effect = Exception("detector failed")

        with self.assertLogs(
            "google.cloud.spanner_v1._helpers", level="WARNING"
        ) as log:
            location = self._callFUT()
            self.assertEqual(location, "global")
            self.assertIn("Failed to detect GCP resource location", log.output[0])


class Test_try_to_coerce_bytes(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _try_to_coerce_bytes

        return _try_to_coerce_bytes(*args, **kw)

    def test_w_valid_bytes(self):
        valid_bytes = b"sample_bytes"
        result = self._callFUT(valid_bytes)
        self.assertEqual(result, valid_bytes)

    def test_w_invalid_bytes(self):
        invalid_bytes = b"\xff\xfe"
        with self.assertRaises(ValueError):
            self._callFUT(invalid_bytes)


class Test_validate_and_decode_bytes(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _validate_and_decode_bytes

        return _validate_and_decode_bytes(*args, **kw)

    def test_w_valid_bytes(self):
        valid_bytes = b"sample_bytes"
        result = self._callFUT(valid_bytes)
        self.assertEqual(result, "sample_bytes")
        self.assertIsInstance(result, str)

    def test_w_invalid_bytes(self):
        invalid_bytes = b"\xff\xfe"
        with self.assertRaises(ValueError) as context:
            self._callFUT(invalid_bytes)
        self.assertIn(
            "Received a bytes that is not base64 encoded", str(context.exception)
        )


class Test_make_value_pb(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _make_value_pb

        return _make_value_pb(*args, **kw)

    def test_w_None(self):
        value_pb = self._callFUT(None)
        self.assertTrue(value_pb.HasField("null_value"))

    def test_w_bytes(self):
        from google.protobuf.struct_pb2 import Value

        BYTES = b"BYTES"
        expected = Value(string_value="BYTES")
        value_pb = self._callFUT(BYTES)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb, expected)
        self.assertIsInstance(value_pb.string_value, str)
        self.assertEqual(value_pb.string_value, "BYTES")

    def test_w_invalid_bytes(self):
        BYTES = b"\xff\xfe\x03&"
        with self.assertRaises(ValueError):
            self._callFUT(BYTES)

    def test_w_explicit_unicode(self):
        from google.protobuf.struct_pb2 import Value

        TEXT = "TEXT"
        value_pb = self._callFUT(TEXT)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, TEXT)

    def test_w_list(self):
        from google.protobuf.struct_pb2 import ListValue, Value

        value_pb = self._callFUT(["a", "b", "c"])
        self.assertIsInstance(value_pb, Value)
        self.assertIsInstance(value_pb.list_value, ListValue)
        values = value_pb.list_value.values
        self.assertEqual([value.string_value for value in values], ["a", "b", "c"])

    def test_w_tuple(self):
        from google.protobuf.struct_pb2 import ListValue, Value

        value_pb = self._callFUT(("a", "b", "c"))
        self.assertIsInstance(value_pb, Value)
        self.assertIsInstance(value_pb.list_value, ListValue)
        values = value_pb.list_value.values
        self.assertEqual([value.string_value for value in values], ["a", "b", "c"])

    def test_w_bool(self):
        from google.protobuf.struct_pb2 import Value

        value_pb = self._callFUT(True)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.bool_value, True)

    def test_w_int(self):
        from google.protobuf.struct_pb2 import Value

        value_pb = self._callFUT(42)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "42")

    def test_w_float(self):
        from google.protobuf.struct_pb2 import Value

        value_pb = self._callFUT(3.14159)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.number_value, 3.14159)

    def test_w_float_nan(self):
        from google.protobuf.struct_pb2 import Value

        value_pb = self._callFUT(float("nan"))
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "NaN")

    def test_w_float_neg_inf(self):
        from google.protobuf.struct_pb2 import Value

        value_pb = self._callFUT(float("-inf"))
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "-Infinity")

    def test_w_float_pos_inf(self):
        from google.protobuf.struct_pb2 import Value

        value_pb = self._callFUT(float("inf"))
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "Infinity")

    def test_w_date(self):
        from google.protobuf.struct_pb2 import Value

        today = datetime.date.today()
        value_pb = self._callFUT(today)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, today.isoformat())

    def test_w_date_pre1000ad(self):
        from google.protobuf.struct_pb2 import Value

        when = datetime.date(800, 2, 25)
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "0800-02-25")

    def test_w_timestamp_w_nanos(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        when = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=123456789, tzinfo=timezone.utc
        )
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "2016-12-20T21:13:47.123456789Z")

    def test_w_timestamp_w_nanos_pre1000ad(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        when = datetime_helpers.DatetimeWithNanoseconds(
            850, 12, 20, 21, 13, 47, nanosecond=123456789, tzinfo=timezone.utc
        )
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "0850-12-20T21:13:47.123456789Z")

    def test_w_listvalue(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1._helpers import _make_list_value_pb

        list_value = _make_list_value_pb([1, 2, 3])
        value_pb = self._callFUT(list_value)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.list_value, list_value)

    def test_w_datetime(self):
        from google.protobuf.struct_pb2 import Value

        when = datetime.datetime(2021, 2, 8, 0, 0, 0, tzinfo=timezone.utc)
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "2021-02-08T00:00:00.000000Z")

    def test_w_datetime_pre1000ad(self):
        from google.protobuf.struct_pb2 import Value

        when = datetime.datetime(916, 2, 8, 0, 0, 0, tzinfo=timezone.utc)
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "0916-02-08T00:00:00.000000Z")

    def test_w_timestamp_w_tz(self):
        from google.protobuf.struct_pb2 import Value

        zone = datetime.timezone(datetime.timedelta(hours=+1), name="CET")
        when = datetime.datetime(2021, 2, 8, 0, 0, 0, tzinfo=zone)
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "2021-02-07T23:00:00.000000Z")

    def test_w_timestamp_w_tz_pre1000ad(self):
        from google.protobuf.struct_pb2 import Value

        zone = datetime.timezone(datetime.timedelta(hours=+1), name="CET")
        when = datetime.datetime(721, 2, 8, 0, 0, 0, tzinfo=zone)
        value_pb = self._callFUT(when)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "0721-02-07T23:00:00.000000Z")

    def test_w_unknown_type(self):
        with self.assertRaises(ValueError):
            self._callFUT(object())

    def test_w_numeric_precision_and_scale_valid(self):
        import decimal

        from google.protobuf.struct_pb2 import Value

        cases = [
            decimal.Decimal("42"),
            decimal.Decimal("9.9999999999999999999999999999999999999E+28"),
            decimal.Decimal("-9.9999999999999999999999999999999999999E+28"),
            decimal.Decimal("99999999999999999999999999999.999999999"),
            decimal.Decimal("1E+28"),
            decimal.Decimal("1E-9"),
        ]
        for value in cases:
            with self.subTest(value=str(value)):
                value_pb = self._callFUT(value)
                self.assertIsInstance(value_pb, Value)
                self.assertEqual(value_pb.string_value, str(value))

    def test_w_numeric_precision_and_scale_invalid(self):
        import decimal

        from google.cloud.spanner_v1._helpers import (
            NUMERIC_MAX_PRECISION_ERR_MSG,
            NUMERIC_MAX_SCALE_ERR_MSG,
        )

        max_precision_error_msg = NUMERIC_MAX_PRECISION_ERR_MSG.format("30")
        max_scale_error_msg = NUMERIC_MAX_SCALE_ERR_MSG.format("10")

        cases = [
            (
                decimal.Decimal("9.9999999999999999999999999999999999999E+29"),
                max_precision_error_msg,
            ),
            (
                decimal.Decimal("-9.9999999999999999999999999999999999999E+29"),
                max_precision_error_msg,
            ),
            (
                decimal.Decimal("999999999999999999999999999999.99999999"),
                max_precision_error_msg,
            ),
            (
                decimal.Decimal("-999999999999999999999999999999.99999999"),
                max_precision_error_msg,
            ),
            (
                decimal.Decimal("999999999999999999999999999999"),
                max_precision_error_msg,
            ),
            (decimal.Decimal("1E+29"), max_precision_error_msg),
            (decimal.Decimal("1E-10"), max_scale_error_msg),
        ]

        for value, err_msg in cases:
            with self.subTest(value=str(value), err_msg=err_msg):
                self.assertRaisesRegex(
                    ValueError,
                    err_msg,
                    lambda: self._callFUT(value),
                )

    def test_w_json(self):
        import json

        from google.protobuf.struct_pb2 import Value

        value = json.dumps(
            {"id": 27863, "Name": "Anamika"}, sort_keys=True, separators=(",", ":")
        )
        value_pb = self._callFUT(value)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, value)

    def test_w_json_None(self):
        from google.cloud.spanner_v1 import JsonObject

        value = JsonObject(None)
        value_pb = self._callFUT(value)
        self.assertTrue(value_pb.HasField("null_value"))

    def test_w_proto_message(self):
        import base64

        from google.protobuf.struct_pb2 import Value

        from .testdata import singer_pb2

        singer_info = singer_pb2.SingerInfo()
        expected = Value(
            string_value=base64.b64encode(singer_info.SerializeToString()).decode(
                "utf-8"
            )
        )
        value_pb = self._callFUT(singer_info)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb, expected)
        self.assertIsInstance(value_pb.string_value, str)

    def test_w_proto_enum(self):
        from google.protobuf.struct_pb2 import Value

        from .testdata import singer_pb2

        value_pb = self._callFUT(singer_pb2.Genre.ROCK)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, "3")

    def test_w_json_object(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import JsonObject

        value = JsonObject({"key": "value"})
        value_pb = self._callFUT(value)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, '{"key":"value"}')

    def test_w_uuid(self):
        import uuid

        from google.protobuf.struct_pb2 import Value

        unique_id = uuid.uuid4()
        value_pb = self._callFUT(unique_id)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, str(unique_id))

    def test_w_interval(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1.data_types import Interval

        interval = Interval(months=1, days=2, nanos=3000)
        value_pb = self._callFUT(interval)
        self.assertIsInstance(value_pb, Value)
        self.assertEqual(value_pb.string_value, str(interval))

    def test_w_proto_message_none(self):
        from unittest.mock import MagicMock

        from google.protobuf.message import Message

        mock_message = MagicMock(spec=Message)
        mock_message.SerializeToString.return_value = None
        value_pb = self._callFUT(mock_message)
        self.assertTrue(value_pb.HasField("null_value"))

    def test_w_subclass_fallback(self):
        import decimal
        import uuid
        from unittest.mock import MagicMock

        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import ListValue

        from google.cloud.spanner_v1 import JsonObject
        from google.cloud.spanner_v1.data_types import Interval

        class CustomList(list):
            pass

        class CustomTuple(tuple):
            pass

        class CustomInt(int):
            pass

        class CustomFloat(float):
            pass

        class CustomDate(datetime.date):
            pass

        class CustomDatetime(datetime.datetime):
            pass

        class CustomDatetimeNanos(datetime_helpers.DatetimeWithNanoseconds):
            pass

        class CustomBytes(bytes):
            pass

        class CustomStr(str):
            pass

        class CustomDecimal(decimal.Decimal):
            pass

        class CustomJsonObject(JsonObject):
            pass

        class CustomInterval(Interval):
            pass

        class CustomUUID(uuid.UUID):
            pass

        mock_bool = MagicMock(spec=bool)
        mock_list_value = MagicMock(spec=ListValue)
        mock_list_value.__getitem__.side_effect = IndexError

        fallback_cases = [
            (CustomList([1]), "list_value"),
            (CustomTuple((1,)), "list_value"),
            (CustomInt(42), "string_value"),
            (CustomFloat(3.14), "number_value"),
            (CustomFloat(float("nan")), "string_value"),
            (CustomFloat(float("inf")), "string_value"),
            (CustomDate(2023, 5, 10), "string_value"),
            (
                CustomDatetime(2023, 5, 10, 12, 0, tzinfo=datetime.timezone.utc),
                "string_value",
            ),
            (
                CustomDatetimeNanos(
                    2023, 5, 10, 12, 0, nanosecond=500, tzinfo=datetime.timezone.utc
                ),
                "string_value",
            ),
            (CustomBytes(b"custom_bytes"), "string_value"),
            (CustomStr("custom_str"), "string_value"),
            (CustomDecimal("99.95"), "string_value"),
            (CustomJsonObject({"a": 1}), "string_value"),
            (CustomJsonObject(None), "null_value"),
            (CustomInterval(months=2), "string_value"),
            (
                CustomUUID("12345678-1234-5678-1234-567812345678"),
                "string_value",
            ),
            (mock_bool, "bool_value"),
            (mock_list_value, "list_value"),
        ]

        for value, field in fallback_cases:
            with self.subTest(val_type=type(value).__name__):
                result = self._callFUT(value)
                self.assertTrue(
                    result.HasField(field),
                    f"Expected field {field} for {type(value)}, got {result}",
                )


class Test_make_list_value_pb(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _make_list_value_pb

        return _make_list_value_pb(*args, **kw)

    def test_empty(self):
        from google.protobuf.struct_pb2 import ListValue

        result = self._callFUT(values=[])
        self.assertIsInstance(result, ListValue)
        self.assertEqual(len(result.values), 0)

    def test_w_single_value(self):
        from google.protobuf.struct_pb2 import ListValue

        VALUE = "value"
        result = self._callFUT(values=[VALUE])
        self.assertIsInstance(result, ListValue)
        self.assertEqual(len(result.values), 1)
        self.assertEqual(result.values[0].string_value, VALUE)

    def test_w_multiple_values(self):
        from google.protobuf.struct_pb2 import ListValue

        VALUE_1 = "value"
        VALUE_2 = 42
        result = self._callFUT(values=[VALUE_1, VALUE_2])
        self.assertIsInstance(result, ListValue)
        self.assertEqual(len(result.values), 2)
        self.assertEqual(result.values[0].string_value, VALUE_1)
        self.assertEqual(result.values[1].string_value, str(VALUE_2))


class Test_make_list_value_pbs(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _make_list_value_pbs

        return _make_list_value_pbs(*args, **kw)

    def test_empty(self):
        result = self._callFUT(values=[])
        self.assertEqual(result, [])

    def test_w_single_values(self):
        from google.protobuf.struct_pb2 import ListValue

        values = [[0], [1]]
        result = self._callFUT(values=values)
        self.assertEqual(len(result), len(values))
        for found, expected in zip(result, values):
            self.assertIsInstance(found, ListValue)
            self.assertEqual(len(found.values), 1)
            self.assertEqual(found.values[0].string_value, str(expected[0]))

    def test_w_multiple_values(self):
        from google.protobuf.struct_pb2 import ListValue

        values = [[0, "A"], [1, "B"]]
        result = self._callFUT(values=values)
        self.assertEqual(len(result), len(values))
        for found, expected in zip(result, values):
            self.assertIsInstance(found, ListValue)
            self.assertEqual(len(found.values), 2)
            self.assertEqual(found.values[0].string_value, str(expected[0]))
            self.assertEqual(found.values[1].string_value, expected[1])


class Test_parse_value_pb(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _parse_value_pb

        return _parse_value_pb(*args, **kw)

    def test_w_null(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(code=TypeCode.STRING)
        field_name = "null_column"
        value_pb = Value(null_value=NULL_VALUE)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), None)

    def test_w_string(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = "Value"
        field_type = Type(code=TypeCode.STRING)
        field_name = "string_column"
        value_pb = Value(string_value=VALUE)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_bytes(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = b"Value"
        field_type = Type(code=TypeCode.BYTES)
        field_name = "bytes_column"
        value_pb = Value(string_value=VALUE)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_bool(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = True
        field_type = Type(code=TypeCode.BOOL)
        field_name = "bool_column"
        value_pb = Value(bool_value=VALUE)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_int(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = 12345
        field_type = Type(code=TypeCode.INT64)
        field_name = "int_column"
        value_pb = Value(string_value=str(VALUE))

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_float(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = 3.14159
        field_type = Type(code=TypeCode.FLOAT64)
        field_name = "float_column"
        value_pb = Value(number_value=VALUE)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_float_str(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = "3.14159"
        field_type = Type(code=TypeCode.FLOAT64)
        field_name = "float_str_column"
        value_pb = Value(string_value=VALUE)
        expected_value = 3.14159

        self.assertEqual(
            self._callFUT(value_pb, field_type, field_name), expected_value
        )

    def test_w_float32(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = 3.14159
        field_type = Type(code=TypeCode.FLOAT32)
        field_name = "float32_column"
        value_pb = Value(number_value=VALUE)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_float32_str(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = "3.14159"
        field_type = Type(code=TypeCode.FLOAT32)
        field_name = "float32_str_column"
        value_pb = Value(string_value=VALUE)
        expected_value = 3.14159

        self.assertEqual(
            self._callFUT(value_pb, field_type, field_name), expected_value
        )

    def test_w_date(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = datetime.date.today()
        field_type = Type(code=TypeCode.DATE)
        field_name = "date_column"
        value_pb = Value(string_value=VALUE.isoformat())

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_timestamp_wo_nanos(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        value = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=123456000, tzinfo=timezone.utc
        )
        field_type = Type(code=TypeCode.TIMESTAMP)
        field_name = "nanos_column"
        value_pb = Value(string_value="2016-12-20T21:13:47.123456Z")

        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertIsInstance(parsed, datetime_helpers.DatetimeWithNanoseconds)
        self.assertEqual(parsed, value)
        self.assertEqual(parsed.nanosecond, value.nanosecond)

    def test_w_timestamp_w_nanos(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        value = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=123456789, tzinfo=timezone.utc
        )
        field_type = Type(code=TypeCode.TIMESTAMP)
        field_name = "timestamp_column"
        value_pb = Value(string_value="2016-12-20T21:13:47.123456789Z")

        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertIsInstance(parsed, datetime_helpers.DatetimeWithNanoseconds)
        self.assertEqual(parsed, value)
        self.assertEqual(parsed.nanosecond, value.nanosecond)

    def test_w_timestamp_w_offset(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        value_pb = Value(string_value="2016-12-20T12:13:47.123456789+01:00")
        field_type = Type(code=TypeCode.TIMESTAMP)
        field_name = "timestamp_column"

        expected = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 11, 13, 47, nanosecond=123456789, tzinfo=timezone.utc
        )

        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertIsInstance(parsed, datetime_helpers.DatetimeWithNanoseconds)
        self.assertEqual(parsed, expected)
        self.assertEqual(parsed.nanosecond, expected.nanosecond)

        value_pb_neg = Value(string_value="2016-12-20T12:13:47.123456789-05:00")
        expected_neg = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 17, 13, 47, nanosecond=123456789, tzinfo=timezone.utc
        )
        parsed_neg = self._callFUT(value_pb_neg, field_type, field_name)
        self.assertEqual(parsed_neg, expected_neg)
        self.assertEqual(parsed_neg.nanosecond, expected_neg.nanosecond)

    def test_w_timestamp_various_formats(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(code=TypeCode.TIMESTAMP)
        field_name = "timestamp_column"

        # 1. No seconds fraction, UTC (Z)
        value_pb = Value(string_value="2016-12-20T21:13:47Z")
        expected = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=0, tzinfo=timezone.utc
        )
        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertEqual(parsed, expected)
        self.assertEqual(parsed.nanosecond, expected.nanosecond)

        # 2. Single digit fraction (nanoseconds), UTC (Z)
        value_pb = Value(string_value="2016-12-20T21:13:47.1Z")
        expected = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=100000000, tzinfo=timezone.utc
        )
        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertEqual(parsed, expected)
        self.assertEqual(parsed.nanosecond, expected.nanosecond)

        # 3. Milliseconds (3 digits fraction), UTC (Z)
        value_pb = Value(string_value="2016-12-20T21:13:47.123Z")
        expected = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=123000000, tzinfo=timezone.utc
        )
        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertEqual(parsed, expected)
        self.assertEqual(parsed.nanosecond, expected.nanosecond)

        # 4. Microseconds (6 digits fraction), UTC (Z)
        value_pb = Value(string_value="2016-12-20T21:13:47.123456Z")
        expected = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=123456000, tzinfo=timezone.utc
        )
        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertEqual(parsed, expected)
        self.assertEqual(parsed.nanosecond, expected.nanosecond)

        # 5. Offset without seconds fraction
        value_pb = Value(string_value="2016-12-20T21:13:47+02:00")
        expected = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 19, 13, 47, nanosecond=0, tzinfo=timezone.utc
        )
        parsed = self._callFUT(value_pb, field_type, field_name)
        self.assertEqual(parsed, expected)
        self.assertEqual(parsed.nanosecond, expected.nanosecond)

    def test_datetime_with_nanoseconds_equality_ignores_nanoseconds(self):
        from google.api_core import datetime_helpers
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(code=TypeCode.TIMESTAMP)
        field_name = "timestamp_column"

        # Actual parsed timestamp has nanoseconds = 123456789
        value_pb = Value(string_value="2016-12-20T21:13:47.123456789Z")
        parsed = self._callFUT(value_pb, field_type, field_name)

        # Expected object with DIFFERENT nanoseconds but SAME microseconds (123456)
        expected_different_nanos = datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, nanosecond=123456000, tzinfo=timezone.utc
        )

        # Assert that standard assertEqual would FALSE POSITIVE (return True / pass)
        self.assertEqual(parsed, expected_different_nanos)

        # Assert that their actual nanosecond property values are DIFFERENT
        self.assertNotEqual(parsed.nanosecond, expected_different_nanos.nanosecond)

    def test_w_timestamp_invalid_formats(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(code=TypeCode.TIMESTAMP)
        field_name = "timestamp_column"

        invalid_strings = [
            "2016-12-20T21:13:47",  # Missing timezone offset
            "2016-12-20 21:13:47Z",  # Space instead of 'T' separator
            "2016-12-20T21:13:47+0100",  # Missing colon in offset
            "2016-12-20T21:13:47.1234567890Z",  # Too many sub-seconds digits (10 digits)
            "2016-12-20T21:13:4Z",  # Single digit second
            "2016-12-20T21:1:47Z",  # Single digit minute
            "2016-12-20T2:13:47Z",  # Single digit hour
            "2016-12-20T21:13:47+1:00",  # Single digit hour in offset
        ]

        for invalid_string in invalid_strings:
            value_pb = Value(string_value=invalid_string)
            with self.assertRaises((ValueError, IndexError)):
                self._callFUT(value_pb, field_type, field_name)

    def test_w_array_empty(self):
        from google.protobuf.struct_pb2 import ListValue, Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(
            code=TypeCode.ARRAY, array_element_type=Type(code=TypeCode.INT64)
        )
        field_name = "array_empty_column"
        value_pb = Value(list_value=ListValue(values=[]))

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), [])

    def test_w_array_non_empty(self):
        from google.protobuf.struct_pb2 import ListValue, Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(
            code=TypeCode.ARRAY, array_element_type=Type(code=TypeCode.INT64)
        )
        field_name = "array_non_empty_column"
        VALUES = [32, 19, 5]
        values_pb = ListValue(
            values=[Value(string_value=str(value)) for value in VALUES]
        )
        value_pb = Value(list_value=values_pb)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUES)

    def test_w_struct(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import StructType, Type, TypeCode
        from google.cloud.spanner_v1._helpers import _make_list_value_pb

        VALUES = ["phred", 32]
        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )
        field_type = Type(code=TypeCode.STRUCT, struct_type=struct_type_pb)
        field_name = "struct_column"
        value_pb = Value(list_value=_make_list_value_pb(VALUES))

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUES)

    def test_w_numeric(self):
        import decimal

        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = decimal.Decimal("99999999999999999999999999999.999999999")
        field_type = Type(code=TypeCode.NUMERIC)
        field_name = "numeric_column"
        value_pb = Value(string_value=str(VALUE))

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

    def test_w_json(self):
        import json

        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode
        from google.cloud.spanner_v1.data_types import JsonObject

        VALUE = {"id": 27863, "Name": "Anamika"}
        str_repr = json.dumps(VALUE, sort_keys=True, separators=(",", ":"))

        field_type = Type(code=TypeCode.JSON)
        field_name = "json_column"
        value_pb = Value(string_value=str_repr)

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)

        VALUE = None
        str_repr = json.dumps(VALUE, sort_keys=True, separators=(",", ":"))

        field_type = Type(code=TypeCode.JSON)
        value_pb = Value(string_value=str_repr)

        self.assertEqual(
            self._callFUT(value_pb, field_type, field_name), JsonObject(None)
        )

    def test_w_unknown_type(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        field_type = Type(code=TypeCode.TYPE_CODE_UNSPECIFIED)
        field_name = "unknown_column"
        value_pb = Value(string_value="Borked")

        with self.assertRaises(ValueError):
            self._callFUT(value_pb, field_type, field_name)

    def test_w_proto_message(self):
        import base64

        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        from .testdata import singer_pb2

        VALUE = singer_pb2.SingerInfo()
        field_type = Type(code=TypeCode.PROTO)
        field_name = "proto_message_column"
        value_pb = Value(
            string_value=base64.b64encode(VALUE.SerializeToString()).decode("utf-8")
        )
        column_info = {"proto_message_column": singer_pb2.SingerInfo()}

        self.assertEqual(
            self._callFUT(value_pb, field_type, field_name, column_info), VALUE
        )

    def test_w_proto_message_decode_error(self):
        import base64
        from unittest import mock

        from google.protobuf.message import DecodeError
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        from .testdata import singer_pb2

        VALUE = singer_pb2.SingerInfo(singer_id=1, nationality="Canadian")
        field_type = Type(code=TypeCode.PROTO)
        field_name = "proto_message_column"
        raw_bytes = VALUE.SerializeToString()
        value_pb = Value(string_value=base64.b64encode(raw_bytes).decode("utf-8"))
        column_info = {"proto_message_column": singer_pb2.SingerInfo()}

        # Mock ParseFromString to raise DecodeError
        with mock.patch.object(
            singer_pb2.SingerInfo,
            "ParseFromString",
            side_effect=DecodeError("Mock Decode Error"),
        ):
            result = self._callFUT(value_pb, field_type, field_name, column_info)
            # Should return raw bytes
            self.assertEqual(result, raw_bytes)

    def test_w_proto_message_recursion_error(self):
        import base64
        from unittest import mock

        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        from .testdata import singer_pb2

        VALUE = singer_pb2.SingerInfo(singer_id=1, nationality="Canadian")
        field_type = Type(code=TypeCode.PROTO)
        field_name = "proto_message_column"
        raw_bytes = VALUE.SerializeToString()
        value_pb = Value(string_value=base64.b64encode(raw_bytes).decode("utf-8"))
        column_info = {"proto_message_column": singer_pb2.SingerInfo()}

        with mock.patch.object(
            singer_pb2.SingerInfo,
            "ParseFromString",
            side_effect=RecursionError("Mock Recursion Error"),
        ):
            result = self._callFUT(value_pb, field_type, field_name, column_info)
            self.assertEqual(result, raw_bytes)

    def test_w_proto_enum(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        from .testdata import singer_pb2

        VALUE = "ROCK"
        field_type = Type(code=TypeCode.ENUM)
        field_name = "proto_enum_column"
        value_pb = Value(string_value=str(singer_pb2.Genre.ROCK))
        column_info = {"proto_enum_column": singer_pb2.Genre}

        self.assertEqual(
            self._callFUT(value_pb, field_type, field_name, column_info), VALUE
        )

    def test_w_uuid(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        VALUE = uuid.uuid4()
        field_type = Type(code=TypeCode.UUID)
        field_name = "uuid_column"
        value_pb = Value(string_value=str(VALUE))

        self.assertEqual(self._callFUT(value_pb, field_type, field_name), VALUE)


class Test_parse_list_value_pbs(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _parse_list_value_pbs

        return _parse_list_value_pbs(*args, **kw)

    def test_empty(self):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode

        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )

        self.assertEqual(self._callFUT(rows=[], row_type=struct_type_pb), [])

    def test_non_empty(self):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode
        from google.cloud.spanner_v1._helpers import _make_list_value_pbs

        VALUES = [["phred", 32], ["bharney", 31]]
        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )
        values_pbs = _make_list_value_pbs(VALUES)

        self.assertEqual(
            self._callFUT(rows=values_pbs, row_type=struct_type_pb), VALUES
        )


class Test_SessionWrapper(unittest.TestCase):
    def _getTargetClass(self):
        from google.cloud.spanner_v1._helpers import _SessionWrapper

        return _SessionWrapper

    def _make_one(self, session):
        return self._getTargetClass()(session)

    def test_ctor(self):
        session = object()
        base = self._make_one(session)
        self.assertIs(base._session, session)


class Test_metadata_with_prefix(unittest.TestCase):
    def _call_fut(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _metadata_with_prefix

        return _metadata_with_prefix(*args, **kw)

    def test(self):
        prefix = "prefix"
        metadata = self._call_fut(prefix)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", prefix)])


class Test_retry(unittest.TestCase):
    class test_class:
        def test_fxn(self):
            return True

    def test_retry_on_error(self):
        import functools

        from google.api_core.exceptions import InternalServerError, NotFound

        from google.cloud.spanner_v1._helpers import _retry

        test_api = mock.create_autospec(self.test_class)
        test_api.test_fxn.side_effect = [
            InternalServerError("testing"),
            NotFound("testing"),
            True,
        ]

        _retry(functools.partial(test_api.test_fxn), delay=0)

        self.assertEqual(test_api.test_fxn.call_count, 3)

    def test_retry_allowed_exceptions(self):
        import functools

        from google.api_core.exceptions import InternalServerError, NotFound

        from google.cloud.spanner_v1._helpers import _retry

        test_api = mock.create_autospec(self.test_class)
        test_api.test_fxn.side_effect = [
            NotFound("testing"),
            InternalServerError("testing"),
            True,
        ]

        with self.assertRaises(InternalServerError):
            _retry(
                functools.partial(test_api.test_fxn),
                allowed_exceptions={NotFound: None},
                delay=0,
            )

        self.assertEqual(test_api.test_fxn.call_count, 2)

    def test_retry_count(self):
        import functools

        from google.api_core.exceptions import InternalServerError

        from google.cloud.spanner_v1._helpers import _retry

        test_api = mock.create_autospec(self.test_class)
        test_api.test_fxn.side_effect = [
            InternalServerError("testing"),
            InternalServerError("testing"),
        ]

        with self.assertRaises(InternalServerError):
            _retry(functools.partial(test_api.test_fxn), retry_count=1, delay=0)

        self.assertEqual(test_api.test_fxn.call_count, 2)

    def test_check_rst_stream_error(self):
        import functools

        from google.api_core.exceptions import InternalServerError

        from google.cloud.spanner_v1._helpers import _check_rst_stream_error, _retry

        test_api = mock.create_autospec(self.test_class)
        test_api.test_fxn.side_effect = [
            InternalServerError("Received unexpected EOS on DATA frame from server"),
            InternalServerError("RST_STREAM"),
            True,
        ]

        _retry(
            functools.partial(test_api.test_fxn),
            allowed_exceptions={InternalServerError: _check_rst_stream_error},
            delay=0,
        )

        self.assertEqual(test_api.test_fxn.call_count, 3)

    def test_retry_on_aborted_exception_with_success_after_first_aborted_retry(self):
        import functools
        import time

        from google.api_core.exceptions import Aborted

        from google.cloud.spanner_v1._helpers import _retry_on_aborted_exception

        test_api = mock.create_autospec(self.test_class)
        test_api.test_fxn.side_effect = [
            Aborted("aborted exception", errors=("Aborted error")),
            "true",
        ]
        deadline = time.time() + 30
        result_after_retry = _retry_on_aborted_exception(
            functools.partial(test_api.test_fxn), deadline, default_retry_delay=0
        )

        self.assertEqual(test_api.test_fxn.call_count, 2)
        self.assertTrue(result_after_retry)

    def test_retry_on_aborted_exception_with_success_after_three_retries(self):
        import functools
        import time

        from google.api_core.exceptions import Aborted

        from google.cloud.spanner_v1._helpers import _retry_on_aborted_exception

        test_api = mock.create_autospec(self.test_class)
        # Case where aborted exception is thrown after other generic exceptions
        aborted = Aborted("aborted exception", errors=["Aborted error"])
        test_api.test_fxn.side_effect = [
            aborted,
            aborted,
            aborted,
            "true",
        ]
        deadline = time.time() + 30
        _retry_on_aborted_exception(
            functools.partial(test_api.test_fxn),
            deadline=deadline,
            default_retry_delay=0,
        )

        self.assertEqual(test_api.test_fxn.call_count, 4)

    def test_retry_on_aborted_exception_raises_aborted_if_deadline_expires(self):
        import functools
        import time

        from google.api_core.exceptions import Aborted

        from google.cloud.spanner_v1._helpers import _retry_on_aborted_exception

        test_api = mock.create_autospec(self.test_class)
        test_api.test_fxn.side_effect = [
            Aborted("aborted exception", errors=("Aborted error")),
            "true",
        ]
        deadline = time.time() + 0.001
        with self.assertRaises(Aborted):
            _retry_on_aborted_exception(
                functools.partial(test_api.test_fxn),
                deadline=deadline,
                default_retry_delay=0.01,
            )

        self.assertEqual(test_api.test_fxn.call_count, 1)


class Test_metadata_with_leader_aware_routing(unittest.TestCase):
    def _call_fut(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _metadata_with_leader_aware_routing

        return _metadata_with_leader_aware_routing(*args, **kw)

    def test(self):
        value = True
        metadata = self._call_fut(True)
        self.assertEqual(
            metadata, ("x-goog-spanner-route-to-leader", str(value).lower())
        )


class Test_merge_transaction_options(unittest.TestCase):
    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _merge_Transaction_Options

        return _merge_Transaction_Options(*args, **kw)

    def test_default_none_and_merge_none(self):
        default = merge = None
        result = self._callFUT(default, merge)
        self.assertIsNone(result)

    def test_default_options_and_merge_none(self):
        default = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC,
            ),
        )
        merge = None
        result = self._callFUT(default, merge)
        expected = default
        self.assertEqual(result, expected)

    def test_default_none_and_merge_options(self):
        default = None
        merge = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
        )
        expected = merge
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)

    def test_default_and_merge_isolation_options(self):
        default = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
            read_write=TransactionOptions.ReadWrite(),
        )
        merge = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
            exclude_txn_from_change_streams=True,
        )
        expected = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
        )
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)

    def test_default_isolation_and_merge_options(self):
        default = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE
        )
        merge = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
        )
        expected = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
        )
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)

    def test_default_isolation_and_merge_options_isolation_unspecified(self):
        default = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE
        )
        merge = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
            isolation_level=TransactionOptions.IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED,
        )
        expected = TransactionOptions(
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
        )
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)

    def test_default_and_merge_read_lock_mode_options(self):
        default = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC,
            ),
        )
        merge = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
            exclude_txn_from_change_streams=True,
        )
        expected = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
            exclude_txn_from_change_streams=True,
        )
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)

    def test_default_read_lock_mode_and_merge_options(self):
        default = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
        )
        merge = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
        )
        expected = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
            exclude_txn_from_change_streams=True,
        )
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)

    def test_default_read_lock_mode_and_merge_options_isolation_unspecified(self):
        default = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
        )
        merge = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.READ_LOCK_MODE_UNSPECIFIED,
            ),
            exclude_txn_from_change_streams=True,
        )
        expected = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
            exclude_txn_from_change_streams=True,
        )
        result = self._callFUT(default, merge)
        self.assertEqual(result, expected)


class Test_interval(unittest.TestCase):
    from google.protobuf.struct_pb2 import Value

    from google.cloud.spanner_v1 import Interval, Type, TypeCode

    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _make_value_pb

        return _make_value_pb(*args, **kw)

    def test_interval_cases(self):
        test_cases = [
            {
                "name": "Basic interval",
                "interval": self.Interval(months=14, days=3, nanos=43926789000123),
                "expected": "P1Y2M3DT12H12M6.789000123S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Months only",
                "interval": self.Interval(months=10, days=0, nanos=0),
                "expected": "P10M",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Days only",
                "interval": self.Interval(months=0, days=10, nanos=0),
                "expected": "P10D",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Seconds only",
                "interval": self.Interval(months=0, days=0, nanos=10000000000),
                "expected": "PT10S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Milliseconds only",
                "interval": self.Interval(months=0, days=0, nanos=10000000),
                "expected": "PT0.010S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Microseconds only",
                "interval": self.Interval(months=0, days=0, nanos=10000),
                "expected": "PT0.000010S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Nanoseconds only",
                "interval": self.Interval(months=0, days=0, nanos=10),
                "expected": "PT0.000000010S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Mixed components",
                "interval": self.Interval(months=10, days=20, nanos=1030),
                "expected": "P10M20DT0.000001030S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Mixed components with negative nanos",
                "interval": self.Interval(months=10, days=20, nanos=-1030),
                "expected": "P10M20DT-0.000001030S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Negative interval",
                "interval": self.Interval(months=-14, days=-3, nanos=-43926789000123),
                "expected": "P-1Y-2M-3DT-12H-12M-6.789000123S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Mixed signs",
                "interval": self.Interval(months=10, days=3, nanos=-41401234000000),
                "expected": "P10M3DT-11H-30M-1.234S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Large values",
                "interval": self.Interval(
                    months=25, days=15, nanos=316223999999999999999
                ),
                "expected": "P2Y1M15DT87839999H59M59.999999999S",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
            {
                "name": "Zero interval",
                "interval": self.Interval(months=0, days=0, nanos=0),
                "expected": "P0Y",
                "expected_type": self.Type(code=self.TypeCode.INTERVAL),
            },
        ]

        for case in test_cases:
            with self.subTest(name=case["name"]):
                value_pb = self._callFUT(case["interval"])
                self.assertIsInstance(value_pb, self.Value)
                self.assertEqual(value_pb.string_value, case["expected"])
                # TODO: Add type checking once we have access to the type information


class Test_parse_interval(unittest.TestCase):
    from google.protobuf.struct_pb2 import Value

    def _callFUT(self, *args, **kw):
        from google.cloud.spanner_v1._helpers import _parse_interval

        return _parse_interval(*args, **kw)

    def test_parse_interval_cases(self):
        test_cases = [
            {
                "name": "full interval with all components",
                "input": "P1Y2M3DT12H12M6.789000123S",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": 43926789000123,
                "want_err": False,
            },
            {
                "name": "interval with negative minutes",
                "input": "P1Y2M3DT13H-48M6S",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": 43926000000000,
                "want_err": False,
            },
            {
                "name": "date only interval",
                "input": "P1Y2M3D",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": 0,
                "want_err": False,
            },
            {
                "name": "years and months only",
                "input": "P1Y2M",
                "expected_months": 14,
                "expected_days": 0,
                "expected_nanos": 0,
                "want_err": False,
            },
            {
                "name": "years only",
                "input": "P1Y",
                "expected_months": 12,
                "expected_days": 0,
                "expected_nanos": 0,
                "want_err": False,
            },
            {
                "name": "months only",
                "input": "P2M",
                "expected_months": 2,
                "expected_days": 0,
                "expected_nanos": 0,
                "want_err": False,
            },
            {
                "name": "days only",
                "input": "P3D",
                "expected_months": 0,
                "expected_days": 3,
                "expected_nanos": 0,
                "want_err": False,
            },
            {
                "name": "time components with fractional seconds",
                "input": "PT4H25M6.7890001S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 15906789000100,
                "want_err": False,
            },
            {
                "name": "time components without fractional seconds",
                "input": "PT4H25M6S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 15906000000000,
                "want_err": False,
            },
            {
                "name": "hours and seconds only",
                "input": "PT4H30S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 14430000000000,
                "want_err": False,
            },
            {
                "name": "hours and minutes only",
                "input": "PT4H1M",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 14460000000000,
                "want_err": False,
            },
            {
                "name": "minutes only",
                "input": "PT5M",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 300000000000,
                "want_err": False,
            },
            {
                "name": "fractional seconds only",
                "input": "PT6.789S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 6789000000,
                "want_err": False,
            },
            {
                "name": "small fractional seconds",
                "input": "PT0.123S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 123000000,
                "want_err": False,
            },
            {
                "name": "very small fractional seconds",
                "input": "PT.000000123S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 123,
                "want_err": False,
            },
            {
                "name": "zero years",
                "input": "P0Y",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 0,
                "want_err": False,
            },
            {
                "name": "all negative components",
                "input": "P-1Y-2M-3DT-12H-12M-6.789000123S",
                "expected_months": -14,
                "expected_days": -3,
                "expected_nanos": -43926789000123,
                "want_err": False,
            },
            {
                "name": "mixed signs in components",
                "input": "P1Y-2M3DT13H-51M6.789S",
                "expected_months": 10,
                "expected_days": 3,
                "expected_nanos": 43746789000000,
                "want_err": False,
            },
            {
                "name": "negative years with mixed signs",
                "input": "P-1Y2M-3DT-13H49M-6.789S",
                "expected_months": -10,
                "expected_days": -3,
                "expected_nanos": -43866789000000,
                "want_err": False,
            },
            {
                "name": "negative time components",
                "input": "P1Y2M3DT-4H25M-6.7890001S",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": -12906789000100,
                "want_err": False,
            },
            {
                "name": "large time values",
                "input": "PT100H100M100.5S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 366100500000000,
                "want_err": False,
            },
            {
                "name": "only time components with seconds",
                "input": "PT12H30M1S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 45001000000000,
                "want_err": False,
            },
            {
                "name": "date and time no seconds",
                "input": "P1Y2M3DT12H30M",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": 45000000000000,
                "want_err": False,
            },
            {
                "name": "fractional seconds with max digits",
                "input": "PT0.123456789S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 123456789,
                "want_err": False,
            },
            {
                "name": "hours and fractional seconds",
                "input": "PT1H0.5S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 3600500000000,
                "want_err": False,
            },
            {
                "name": "years and months to months with fractional seconds",
                "input": "P1Y2M3DT12H30M1.23456789S",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": 45001234567890,
                "want_err": False,
            },
            {
                "name": "comma as decimal point",
                "input": "P1Y2M3DT12H30M1,23456789S",
                "expected_months": 14,
                "expected_days": 3,
                "expected_nanos": 45001234567890,
                "want_err": False,
            },
            {
                "name": "fractional seconds without 0 before decimal",
                "input": "PT.5S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 500000000,
                "want_err": False,
            },
            {
                "name": "mixed signs",
                "input": "P-1Y2M3DT12H-30M1.234S",
                "expected_months": -10,
                "expected_days": 3,
                "expected_nanos": 41401234000000,
                "want_err": False,
            },
            {
                "name": "more mixed signs",
                "input": "P1Y-2M3DT-12H30M-1.234S",
                "expected_months": 10,
                "expected_days": 3,
                "expected_nanos": -41401234000000,
                "want_err": False,
            },
            {
                "name": "trailing zeros after decimal",
                "input": "PT1.234000S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 1234000000,
                "want_err": False,
            },
            {
                "name": "all zeros after decimal",
                "input": "PT1.000S",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 1000000000,
                "want_err": False,
            },
            # Invalid cases
            {"name": "invalid format", "input": "invalid", "want_err": True},
            {"name": "missing duration specifier", "input": "P", "want_err": True},
            {"name": "missing time components", "input": "PT", "want_err": True},
            {"name": "missing unit specifier", "input": "P1YM", "want_err": True},
            {"name": "missing T separator", "input": "P1Y2M3D4H5M6S", "want_err": True},
            {
                "name": "missing decimal value",
                "input": "P1Y2M3DT4H5M6.S",
                "want_err": True,
            },
            {
                "name": "extra unit specifier",
                "input": "P1Y2M3DT4H5M6.789SS",
                "want_err": True,
            },
            {
                "name": "missing value after decimal",
                "input": "P1Y2M3DT4H5M6.",
                "want_err": True,
            },
            {
                "name": "non-digit after decimal",
                "input": "P1Y2M3DT4H5M6.ABC",
                "want_err": True,
            },
            {"name": "missing unit", "input": "P1Y2M3", "want_err": True},
            {"name": "missing time value", "input": "P1Y2M3DT", "want_err": True},
            {
                "name": "invalid negative sign position",
                "input": "P-T1H",
                "want_err": True,
            },
            {"name": "trailing negative sign", "input": "PT1H-", "want_err": True},
            {
                "name": "too many decimal places",
                "input": "P1Y2M3DT4H5M6.789123456789S",
                "want_err": True,
            },
            {
                "name": "multiple decimal points",
                "input": "P1Y2M3DT4H5M6.123.456S",
                "want_err": True,
            },
            {
                "name": "both dot and comma decimals",
                "input": "P1Y2M3DT4H5M6.,789S",
                "want_err": True,
            },
        ]

        for case in test_cases:
            with self.subTest(name=case["name"]):
                value_pb = self.Value(string_value=case["input"])
                if case.get("want_err", False):
                    with self.assertRaises(ValueError):
                        self._callFUT(value_pb)
                else:
                    result = self._callFUT(value_pb)
                    self.assertEqual(result.months, case["expected_months"])
                    self.assertEqual(result.days, case["expected_days"])
                    self.assertEqual(result.nanos, case["expected_nanos"])

    def test_large_values(self):
        large_test_cases = [
            {
                "name": "large positive hours",
                "input": "PT87840000H",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": 316224000000000000000,
                "want_err": False,
            },
            {
                "name": "large negative hours",
                "input": "PT-87840000H",
                "expected_months": 0,
                "expected_days": 0,
                "expected_nanos": -316224000000000000000,
                "want_err": False,
            },
            {
                "name": "large mixed values with max precision",
                "input": "P2Y1M15DT87839999H59M59.999999999S",
                "expected_months": 25,
                "expected_days": 15,
                "expected_nanos": 316223999999999999999,
                "want_err": False,
            },
            {
                "name": "large mixed negative values with max precision",
                "input": "P2Y1M15DT-87839999H-59M-59.999999999S",
                "expected_months": 25,
                "expected_days": 15,
                "expected_nanos": -316223999999999999999,
                "want_err": False,
            },
        ]

        for case in large_test_cases:
            with self.subTest(name=case["name"]):
                value_pb = self.Value(string_value=case["input"])
                if case.get("want_err", False):
                    with self.assertRaises(ValueError):
                        self._callFUT(value_pb)
                else:
                    result = self._callFUT(value_pb)
                    self.assertEqual(result.months, case["expected_months"])
                    self.assertEqual(result.days, case["expected_days"])
                    self.assertEqual(result.nanos, case["expected_nanos"])


class TestBoundedStreamDrainer(unittest.TestCase):
    def test_drain_stream_consumes_iterator(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        items = [1, 2, 3]
        consumed = []

        class MockIterator:
            def __iter__(self):
                return self

            def __next__(self):
                if items:
                    item = items.pop(0)
                    consumed.append(item)
                    return item
                raise StopIteration

        iterator = MockIterator()
        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=1)
        drainer.drain(iterator)
        drainer._queue.join()

        self.assertEqual(consumed, [1, 2, 3])

    def test_drain_stream_inline_fallback_on_full_queue(self):
        from unittest import mock

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=1, worker_count=0)
        drainer._queue.put_nowait(mock.Mock())

        items = [1, 2]
        consumed = []

        class MockIterator:
            def __iter__(self):
                return self

            def __next__(self):
                if items:
                    item = items.pop(0)
                    consumed.append(item)
                    return item
                raise StopIteration

        iterator = MockIterator()
        drainer.drain(iterator)

        self.assertEqual(consumed, [1, 2])

    def test_drain_stream_handles_none(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=1)
        drainer.drain(None)
        self.assertEqual(drainer._queue.qsize(), 0)

    def test_drain_stream_handles_iterator_exception(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        class FailingIterator:
            def __iter__(self):
                return self

            def __next__(self):
                raise RuntimeError("Stream broken")

        iterator = FailingIterator()
        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=1)
        drainer.drain(iterator)
        drainer._queue.join()

    def test_drain_stream_after_shutdown_drains_inline(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=1)
        drainer.shutdown()
        self.assertTrue(drainer._stopped)

        items = [1, 2, 3]
        consumed = []

        class MockIterator:
            def __iter__(self):
                return self

            def __next__(self):
                if items:
                    item = items.pop(0)
                    consumed.append(item)
                    return item
                raise StopIteration

        iterator = MockIterator()
        drainer.drain(iterator)
        self.assertEqual(consumed, [1, 2, 3])
        self.assertEqual(drainer._queue.qsize(), 0)

    def test_drain_stream_inline_fallback_iterator_exception(self):
        from unittest import mock

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=1, worker_count=0)
        drainer._queue.put_nowait(mock.Mock())

        class FailingIterator:
            def __iter__(self):
                return self

            def __next__(self):
                raise RuntimeError("Failed inline")

        iterator = FailingIterator()
        # Should catch and ignore the exception without raising
        drainer.drain(iterator)

    def test_drainer_fallback_on_ensure_started_error(self):
        from unittest import mock

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=2, worker_count=1)
        items = [1, 2, 3]
        consumed = []

        class MockIterator:
            def __iter__(self):
                return self

            def __next__(self):
                if items:
                    val = items.pop(0)
                    consumed.append(val)
                    return val
                raise StopIteration

        with mock.patch.object(
            drainer, "_ensure_started", side_effect=RuntimeError("thread limit reached")
        ):
            drainer.drain(MockIterator())

        self.assertEqual(consumed, [1, 2, 3])

    def test_drainer_ensure_started_partial_failure_retains_started(self):
        from unittest import mock

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=2, worker_count=3)
        start_count = 0

        def _mock_thread_start(thread_self):
            nonlocal start_count
            start_count += 1
            if start_count > 1:
                raise RuntimeError("thread limit reached")

        with mock.patch(
            "google.cloud.spanner_v1._helpers.threading.Thread.start",
            _mock_thread_start,
        ):
            with self.assertRaises(RuntimeError):
                drainer._ensure_started()

        # Started should remain True because 1 worker was successfully created
        self.assertTrue(drainer._started)
        self.assertEqual(len(drainer._workers), 1)

        # Subsequent call must not attempt to spawn additional threads
        drainer._ensure_started()
        self.assertEqual(len(drainer._workers), 1)

    def test_drainer_ensure_started_total_failure_resets_started(self):
        from unittest import mock

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=2, worker_count=2)

        with mock.patch(
            "google.cloud.spanner_v1._helpers.threading.Thread.start",
            side_effect=RuntimeError("no threads"),
        ):
            with self.assertRaises(RuntimeError):
                drainer._ensure_started()

        # Started should be reset to False because 0 workers were created
        self.assertFalse(drainer._started)
        self.assertEqual(len(drainer._workers), 0)

    def test_drainer_shutdown_with_full_queue(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        items_first = [1, 2]
        items_second = [3, 4]
        consumed = []

        class MockIterator:
            def __init__(self, items):
                self._items = list(items)

            def __iter__(self):
                return self

            def __next__(self):
                if self._items:
                    val = self._items.pop(0)
                    consumed.append(val)
                    return val
                raise StopIteration

        drainer = _BoundedStreamDrainer(queue_size=2, worker_count=2)
        drainer._ensure_started()
        drainer._queue.put_nowait(MockIterator(items_first))
        drainer._queue.put_nowait(MockIterator(items_second))
        self.assertTrue(drainer._queue.full())

        # Calling shutdown when queue is already full must not raise queue.Full
        drainer.shutdown()
        self.assertTrue(drainer._stopped)

        # All workers must cleanly terminate despite the queue having been full
        for worker in drainer._workers:
            self.assertFalse(worker.is_alive())

        self.assertEqual(sorted(consumed), [1, 2, 3, 4])

    def test_drainer_shutdown_terminates_idle_workers(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=2)
        drainer._ensure_started()
        self.assertEqual(drainer._queue.qsize(), 0)

        drainer.shutdown()
        self.assertTrue(drainer._stopped)

        for worker in drainer._workers:
            self.assertFalse(worker.is_alive())

    def test_drainer_drain_during_shutdown_does_not_strand_iterator(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=2)
        drainer._ensure_started()

        items = [1, 2, 3]
        consumed = []

        class MockIterator:
            def __iter__(self):
                return self

            def __next__(self):
                if items:
                    item = items.pop(0)
                    consumed.append(item)
                    return item
                raise StopIteration

        # Shutdown the drainer, which terminates workers
        drainer.shutdown()
        self.assertTrue(drainer._stopped)

        for worker in drainer._workers:
            self.assertFalse(worker.is_alive())

        # Calling drain() on a stopped drainer must drain inline and never strand tasks in the queue
        drainer.drain(MockIterator())
        self.assertEqual(consumed, [1, 2, 3])
        self.assertEqual(drainer._queue.qsize(), 0)

    def test_drainer_shutdown_respects_timeout_when_queue_unresponsive(self):
        from unittest import mock

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=2, worker_count=0)
        drainer._started = True
        drainer._workers = [mock.Mock(), mock.Mock()]
        drainer._queue.put_nowait(mock.Mock())
        drainer._queue.put_nowait(mock.Mock())
        self.assertTrue(drainer._queue.full())

        # When the queue is full and workers cannot consume, shutdown must exit
        # cleanly within the specified timeout without raising queue.Full
        drainer.shutdown(timeout=0.05)
        self.assertTrue(drainer._stopped)

    def test_drainer_shutdown_respects_timeout_when_worker_is_busy(self):
        import threading
        import time

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=2, worker_count=1)
        drainer._ensure_started()

        unblock_event = threading.Event()

        class BlockingIterator:
            def __iter__(self):
                return self

            def __next__(self):
                unblock_event.wait(timeout=1.0)
                raise StopIteration

        drainer._queue.put_nowait(BlockingIterator())

        try:
            # shutdown with a tiny timeout of 0.05s must return within ~0.05s
            # rather than waiting indefinitely for the worker to finish
            start_time = time.monotonic()
            drainer.shutdown(timeout=0.05)
            elapsed_time = time.monotonic() - start_time
            self.assertTrue(drainer._stopped)
            self.assertLess(elapsed_time, 0.5)
        finally:
            unblock_event.set()
            for worker in drainer._workers:
                worker.join(timeout=1.0)

    def test_drainer_reset_after_fork(self):
        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=2)
        drainer._ensure_started()
        self.assertTrue(drainer._started)
        self.assertEqual(len(drainer._workers), 2)

        drainer._reset_after_fork()
        self.assertFalse(drainer._started)
        self.assertFalse(drainer._stopped)
        self.assertEqual(len(drainer._workers), 0)
        self.assertEqual(drainer._queue.qsize(), 0)

    def test_drainer_garbage_collection(self):
        import gc
        import weakref

        from google.cloud.spanner_v1._helpers import _BoundedStreamDrainer

        drainer = _BoundedStreamDrainer(queue_size=4, worker_count=1)
        ref = weakref.ref(drainer)
        del drainer
        gc.collect()

        self.assertIsNone(ref())

    def test_global_stream_drainer_reset_after_fork(self):
        from google.cloud.spanner_v1 import _helpers

        _helpers._GLOBAL_STREAM_DRAINER._ensure_started()
        self.assertTrue(_helpers._GLOBAL_STREAM_DRAINER._started)

        _helpers._GLOBAL_STREAM_DRAINER._reset_after_fork()
        self.assertFalse(_helpers._GLOBAL_STREAM_DRAINER._started)
        self.assertEqual(len(_helpers._GLOBAL_STREAM_DRAINER._workers), 0)
        self.assertEqual(_helpers._GLOBAL_STREAM_DRAINER._queue.qsize(), 0)

    def test_module_drain_stream(self):
        from unittest import mock

        from google.cloud.spanner_v1 import _helpers

        with mock.patch.object(_helpers._GLOBAL_STREAM_DRAINER, "drain") as mock_drain:
            iterator = mock.Mock()
            _helpers._drain_stream(iterator)
            mock_drain.assert_called_once_with(iterator)


class Test_get_type_decoder(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from google.cloud.spanner_v1._helpers import _get_type_decoder

        return _get_type_decoder(*args, **kwargs)

    def test_scalar_decoders(self):
        import datetime
        import decimal
        import uuid

        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode
        from google.cloud.spanner_v1._helpers import _SCALAR_DECODERS
        from google.cloud.spanner_v1.data_types import Interval, JsonObject

        test_cases = [
            (TypeCode.STRING, Value(string_value="hello"), "hello"),
            (TypeCode.BYTES, Value(string_value="bytes"), b"bytes"),
            (TypeCode.BOOL, Value(bool_value=True), True),
            (TypeCode.INT64, Value(string_value="42"), 42),
            (TypeCode.FLOAT64, Value(string_value="3.14"), 3.14),
            (TypeCode.FLOAT32, Value(string_value="2.5"), 2.5),
            (
                TypeCode.DATE,
                Value(string_value="2026-03-15"),
                datetime.date(2026, 3, 15),
            ),
            (
                TypeCode.TIMESTAMP,
                Value(string_value="2026-03-15T12:00:00Z"),
                datetime.datetime(2026, 3, 15, 12, 0, tzinfo=datetime.timezone.utc),
            ),
            (TypeCode.NUMERIC, Value(string_value="99.99"), decimal.Decimal("99.99")),
            (TypeCode.JSON, Value(string_value='{"a": 1}'), JsonObject({"a": 1})),
            (
                TypeCode.UUID,
                Value(string_value="12345678-1234-5678-1234-567812345678"),
                uuid.UUID("12345678-1234-5678-1234-567812345678"),
            ),
            (TypeCode.INTERVAL, Value(string_value="P1Y"), Interval.from_str("P1Y")),
        ]
        for type_code, sample_value_pb, expected_result in test_cases:
            field_type = Type(code=type_code)
            decoder = self._callFUT(field_type, "column_name")
            self.assertIs(decoder, _SCALAR_DECODERS[int(type_code)])
            self.assertEqual(decoder(sample_value_pb), expected_result)

    def test_proto_and_enum(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import Type, TypeCode

        proto_type = Type(code=TypeCode.PROTO)
        proto_decoder = self._callFUT(proto_type, "proto_column")
        self.assertTrue(callable(proto_decoder))

        enum_type = Type(code=TypeCode.ENUM)
        enum_decoder = self._callFUT(enum_type, "enum_column")
        self.assertTrue(callable(enum_decoder))
        self.assertEqual(enum_decoder(Value(string_value="1")), 1)

    def test_array_and_struct(self):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode

        array_type = Type(
            code=TypeCode.ARRAY,
            array_element_type=Type(code=TypeCode.STRING),
        )
        array_decoder = self._callFUT(array_type, "array_column")
        self.assertTrue(callable(array_decoder))

        struct_field = StructType.Field(
            name="subfield", type_=Type(code=TypeCode.STRING)
        )
        struct_type = Type(
            code=TypeCode.STRUCT,
            struct_type=StructType(fields=[struct_field]),
        )
        struct_decoder = self._callFUT(struct_type, "struct_column")
        self.assertTrue(callable(struct_decoder))

    def test_unknown_and_unspecified_types(self):
        from unittest import mock

        from google.cloud.spanner_v1 import Type, TypeCode

        unspecified_type = Type(code=TypeCode.TYPE_CODE_UNSPECIFIED)
        with self.assertRaises(ValueError):
            self._callFUT(unspecified_type, "unspecified")

        unknown_type = mock.Mock(code=999)
        with self.assertRaises(ValueError):
            self._callFUT(unknown_type, "unknown")

        invalid_code_type = mock.Mock(code="invalid")
        with self.assertRaises(ValueError):
            self._callFUT(invalid_code_type, "invalid")


class TestCreateSpannerOmniTransport(unittest.TestCase):
    def test_create_spanner_omni_transport_plaintext_with_auth_interceptor(self):
        import grpc

        from google.cloud.spanner_v1 import _helpers

        mock_factory = mock.MagicMock()
        mock_creds = mock.MagicMock()
        mock_interceptor = mock.MagicMock(spec=grpc.UnaryUnaryClientInterceptor)
        mock_creds.create_auth_interceptor.return_value = mock_interceptor

        with mock.patch("grpc.insecure_channel") as mock_insecure:
            with mock.patch("grpc.intercept_channel") as mock_intercept:
                _helpers._create_spanner_omni_transport(
                    mock_factory,
                    "localhost:9010",
                    use_plain_text=True,
                    ca_certificate=None,
                    client_certificate=None,
                    client_key=None,
                    credentials=mock_creds,
                )
                mock_insecure.assert_called_once_with(target="localhost:9010")
                mock_intercept.assert_called_once_with(
                    mock_insecure.return_value, mock_interceptor
                )
                mock_factory.assert_called_once_with(
                    channel=mock_intercept.return_value, credentials=mock_creds
                )

    def test_create_spanner_omni_transport_tls_and_mtls(self):
        from google.cloud.spanner_v1 import _helpers

        mock_factory = mock.MagicMock()
        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_creds:
                with mock.patch("grpc.secure_channel") as mock_secure:
                    # TLS only
                    _helpers._create_spanner_omni_transport(
                        mock_factory,
                        "omni-host:15000",
                        use_plain_text=False,
                        ca_certificate="ca.pem",
                        client_certificate=None,
                        client_key=None,
                    )
                    mock_ssl_creds.assert_called_with(root_certificates=b"cert_data")
                    mock_secure.assert_called_with(
                        "omni-host:15000", mock_ssl_creds.return_value
                    )

                    # mTLS
                    _helpers._create_spanner_omni_transport(
                        mock_factory,
                        "omni-host:15000",
                        use_plain_text=False,
                        ca_certificate="ca.pem",
                        client_certificate="client.pem",
                        client_key="key.pem",
                    )
                    mock_ssl_creds.assert_called_with(
                        root_certificates=b"cert_data",
                        private_key=b"cert_data",
                        certificate_chain=b"cert_data",
                    )

    def test_create_spanner_omni_transport_validation_errors(self):
        from google.cloud.spanner_v1 import _helpers

        mock_factory = mock.MagicMock()
        # Missing ca_certificate
        with self.assertRaises(ValueError) as cm:
            _helpers._create_spanner_omni_transport(
                mock_factory,
                "omni-host:15000",
                use_plain_text=False,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
            )
        self.assertIn("TLS/mTLS connection requires ca_certificate", str(cm.exception))

        # Missing client_key when client_certificate provided
        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            with self.assertRaises(ValueError) as cm:
                _helpers._create_spanner_omni_transport(
                    mock_factory,
                    "omni-host:15000",
                    use_plain_text=False,
                    ca_certificate="ca.pem",
                    client_certificate="client.pem",
                    client_key=None,
                )
            self.assertIn(
                "Both client_certificate and client_key must be provided for mTLS connection",
                str(cm.exception),
            )

        # Missing client_certificate when client_key provided
        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            with self.assertRaises(ValueError) as cm:
                _helpers._create_spanner_omni_transport(
                    mock_factory,
                    "omni-host:15000",
                    use_plain_text=False,
                    ca_certificate="ca.pem",
                    client_certificate=None,
                    client_key="key.pem",
                )
            self.assertIn(
                "Both client_certificate and client_key must be provided for mTLS connection",
                str(cm.exception),
            )

    def test_create_spanner_omni_transport_interceptors_and_credentials_fallback(self):
        import grpc
        from google.auth.credentials import AnonymousCredentials

        from google.cloud.spanner_v1 import _helpers

        mock_factory = mock.MagicMock()
        existing_interceptor = mock.MagicMock(spec=grpc.UnaryUnaryClientInterceptor)
        mock_creds = mock.MagicMock(spec=["create_auth_interceptor"])
        auth_interceptor = mock.MagicMock(spec=grpc.UnaryUnaryClientInterceptor)
        mock_creds.create_auth_interceptor.return_value = auth_interceptor

        # Case 1: credentials with interceptor and existing interceptors
        with mock.patch("grpc.insecure_channel") as mock_insecure:
            with mock.patch("grpc.intercept_channel") as mock_intercept:
                _helpers._create_spanner_omni_transport(
                    mock_factory,
                    "localhost:9010",
                    use_plain_text=True,
                    ca_certificate=None,
                    client_certificate=None,
                    client_key=None,
                    interceptors=[existing_interceptor],
                    credentials=mock_creds,
                )
                mock_intercept.assert_called_once_with(
                    mock_insecure.return_value, existing_interceptor, auth_interceptor
                )
                mock_factory.assert_called_once_with(
                    channel=mock_intercept.return_value, credentials=mock_creds
                )

        # Case 2: credentials without create_auth_interceptor, no interceptors
        mock_plain_creds = mock.MagicMock(spec=[])
        mock_factory.reset_mock()
        with mock.patch("grpc.insecure_channel") as mock_insecure:
            with mock.patch("grpc.intercept_channel") as mock_intercept:
                _helpers._create_spanner_omni_transport(
                    mock_factory,
                    "localhost:9010",
                    use_plain_text=True,
                    ca_certificate=None,
                    client_certificate=None,
                    client_key=None,
                    interceptors=None,
                    credentials=mock_plain_creds,
                )
                mock_intercept.assert_not_called()
                mock_factory.assert_called_once_with(
                    channel=mock_insecure.return_value, credentials=mock_plain_creds
                )

        # Case 3: credentials is None -> uses AnonymousCredentials
        mock_factory.reset_mock()
        with mock.patch("grpc.insecure_channel") as mock_insecure:
            with mock.patch("grpc.intercept_channel") as mock_intercept:
                _helpers._create_spanner_omni_transport(
                    mock_factory,
                    "localhost:9010",
                    use_plain_text=True,
                    ca_certificate=None,
                    client_certificate=None,
                    client_key=None,
                    interceptors=None,
                    credentials=None,
                )
                mock_intercept.assert_not_called()
                self.assertEqual(mock_factory.call_count, 1)
                self.assertIsInstance(
                    mock_factory.call_args[1]["credentials"], AnonymousCredentials
                )


class TestRequestIdHelpers(unittest.TestCase):
    def test_build_request_id(self):
        from google.cloud.spanner_v1.request_id_header import (
            REQ_ID_VERSION,
            REQ_RAND_PROCESS_ID,
            build_request_id,
        )

        req_id = build_request_id(1, 2, 3, 4)
        expected = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}.1.2.3.4"
        self.assertEqual(req_id, expected)

    def test_with_request_id(self):
        from google.cloud.spanner_v1.request_id_header import (
            REQ_ID_HEADER_KEY,
            REQ_ID_VERSION,
            REQ_RAND_PROCESS_ID,
            with_request_id,
        )

        expected_id = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}.10.20.30.1"
        metadata, req_id = with_request_id(10, 20, 30, 1, [("prior", "val")])
        self.assertEqual(req_id, expected_id)
        self.assertEqual(metadata, [("prior", "val"), (REQ_ID_HEADER_KEY, expected_id)])

    def test_with_request_id_metadata_only(self):
        from google.cloud.spanner_v1.request_id_header import (
            REQ_ID_HEADER_KEY,
            REQ_ID_VERSION,
            REQ_RAND_PROCESS_ID,
            with_request_id_metadata_only,
        )

        expected_id = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}.10.20.30.1"
        metadata = with_request_id_metadata_only(10, 20, 30, 1)
        self.assertEqual(metadata, [(REQ_ID_HEADER_KEY, expected_id)])

    def test_with_request_id_span_recording(self):
        from unittest import mock

        from google.cloud.spanner_v1.request_id_header import (
            X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR,
            with_request_id,
        )

        mock_span = mock.Mock()
        mock_span.is_recording.return_value = True

        _, req_id = with_request_id(1, 1, 1, 1, span=mock_span)
        mock_span.set_attribute.assert_called_once_with(
            X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR, req_id
        )

    def test_with_request_id_span_non_recording(self):
        from unittest import mock

        from google.cloud.spanner_v1.request_id_header import with_request_id

        mock_span = mock.Mock()
        mock_span.is_recording.return_value = False

        with_request_id(1, 1, 1, 1, span=mock_span)
        mock_span.set_attribute.assert_not_called()

    def test_augment_errors_with_request_id_success(self):
        from google.cloud.spanner_v1._helpers import _augment_errors_with_request_id

        with _augment_errors_with_request_id("test-req-id"):
            val = 42
        self.assertEqual(val, 42)

    def test_augment_errors_with_request_id_google_api_call_error(self):
        from google.api_core.exceptions import GoogleAPICallError

        from google.cloud.spanner_v1._helpers import _augment_errors_with_request_id

        err = GoogleAPICallError("something went wrong")
        with self.assertRaises(GoogleAPICallError) as ctx:
            with _augment_errors_with_request_id("test-req-id"):
                raise err

        raised = ctx.exception
        self.assertIs(raised, err)
        self.assertEqual(getattr(raised, "request_id", None), "test-req-id")
        self.assertIn("request_id = test-req-id", raised.message)

    def test_augment_errors_with_request_id_non_api_error(self):
        from google.cloud.spanner_v1._helpers import _augment_errors_with_request_id

        err = ValueError("regular error")
        with self.assertRaises(ValueError) as ctx:
            with _augment_errors_with_request_id("test-req-id"):
                raise err

        raised = ctx.exception
        self.assertIs(raised, err)
        self.assertFalse(hasattr(raised, "request_id"))

    def test_atomic_counter_slots(self):
        from google.cloud.spanner_v1._helpers import AtomicCounter

        counter = AtomicCounter()
        self.assertFalse(hasattr(counter, "__dict__"))
        self.assertEqual(counter.value, 0)
        self.assertEqual(counter.increment(), 1)
        self.assertEqual(counter.value, 1)
        counter += 2
        self.assertEqual(counter.value, 3)
        counter.reset()
        self.assertEqual(counter.value, 0)

    def test_helpers_metadata_with_request_id_wrappers(self):
        from google.cloud.spanner_v1._helpers import (
            _metadata_with_request_id,
            _metadata_with_request_id_and_req_id,
        )
        from google.cloud.spanner_v1.request_id_header import (
            REQ_ID_HEADER_KEY,
            REQ_ID_VERSION,
            REQ_RAND_PROCESS_ID,
        )

        expected_id = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}.1.2.3.4"
        meta = _metadata_with_request_id(1, 2, 3, 4, [("key", "val")])
        self.assertEqual(meta, [("key", "val"), (REQ_ID_HEADER_KEY, expected_id)])

        meta_tuple, req_id = _metadata_with_request_id_and_req_id(1, 2, 3, 4)
        self.assertEqual(req_id, expected_id)
        self.assertEqual(meta_tuple, [(REQ_ID_HEADER_KEY, expected_id)])

    def test_parse_request_id(self):
        from google.cloud.spanner_v1.request_id_header import parse_request_id

        parsed = parse_request_id("1.12345.2.3.4.5")
        self.assertEqual(parsed, (1, 12345, 2, 3, 4, 5))

    def test_with_request_id_metadata_only_span_recording(self):
        from unittest import mock

        from google.cloud.spanner_v1.request_id_header import (
            REQ_ID_HEADER_KEY,
            REQ_ID_VERSION,
            REQ_RAND_PROCESS_ID,
            X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR,
            with_request_id_metadata_only,
        )

        mock_span = mock.Mock()
        mock_span.is_recording.return_value = True

        expected_id = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}.1.2.3.4"
        meta = with_request_id_metadata_only(
            1, 2, 3, 4, other_metadata=[("k", "v")], span=mock_span
        )
        self.assertEqual(meta, [("k", "v"), (REQ_ID_HEADER_KEY, expected_id)])
        mock_span.set_attribute.assert_called_once_with(
            X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR, expected_id
        )

    def test_with_request_id_metadata_only_span_non_recording(self):
        from unittest import mock

        from google.cloud.spanner_v1.request_id_header import (
            with_request_id_metadata_only,
        )

        mock_span = mock.Mock()
        mock_span.is_recording.return_value = False

        with_request_id_metadata_only(1, 2, 3, 4, span=mock_span)
        mock_span.set_attribute.assert_not_called()

    def test_cached_prefix_descriptor(self):
        from google.cloud.spanner_v1.request_id_header import (
            REQ_ID_VERSION,
            REQ_RAND_PROCESS_ID,
            _CachedPrefixDescriptor,
        )

        class DummyDB:
            _nth_client_id = 5
            _channel_id = 10
            _req_id_prefix = _CachedPrefixDescriptor()

        # Class access returns descriptor instance
        self.assertIsInstance(DummyDB._req_id_prefix, _CachedPrefixDescriptor)

        # Instance access computes and caches in __dict__
        db = DummyDB()
        expected = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}.5.10."
        self.assertEqual(db._req_id_prefix, expected)
        self.assertEqual(db.__dict__["_req_id_prefix"], expected)
