# Copyright 2026 Google LLC All rights reserved.
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

import base64
import datetime
import gzip
import json
import unittest

from google.cloud.spanner_dbapi import partition_helper
from google.cloud.spanner_v1 import BatchTransactionId
from google.cloud.spanner_v1.types import ExecuteSqlRequest


class TestPartitionHelper(unittest.TestCase):
    def test_encode_and_decode_success_query(self):
        btid = BatchTransactionId(
            transaction_id=b"test-txn-123",
            session_id="session-xyz",
            read_timestamp=datetime.datetime(
                2024, 5, 10, 12, 34, 56, tzinfo=datetime.timezone.utc
            ),
        )

        query_options = ExecuteSqlRequest.QueryOptions(
            optimizer_version="2",
            optimizer_statistics_package="package-abc",
        )

        partition_result = {
            "partition": b"partition-token-456",
            "query": {
                "sql": "SELECT * FROM users WHERE age > %s",
                "params": {"age": 21},
                "query_options": query_options,
            },
        }

        encoded = partition_helper.encode_to_string(btid, partition_result)
        self.assertIsInstance(encoded, str)

        decoded = partition_helper.decode_from_string(encoded)
        self.assertIsInstance(decoded, partition_helper.PartitionId)

        # Verify BatchTransactionId
        self.assertEqual(
            decoded.batch_transaction_id.transaction_id, btid.transaction_id
        )
        self.assertEqual(decoded.batch_transaction_id.session_id, btid.session_id)
        self.assertEqual(
            decoded.batch_transaction_id.read_timestamp, btid.read_timestamp
        )

        # Verify partition result
        self.assertEqual(decoded.partition_result["partition"], b"partition-token-456")
        self.assertEqual(
            decoded.partition_result["query"]["sql"],
            "SELECT * FROM users WHERE age > %s",
        )
        self.assertEqual(decoded.partition_result["query"]["params"], {"age": "21"})

        # Verify query options (restored to object)
        opts_obj = decoded.partition_result["query"]["query_options"]
        self.assertEqual(opts_obj.optimizer_version, "2")
        self.assertEqual(opts_obj.optimizer_statistics_package, "package-abc")

    def test_encode_and_decode_success_read(self):
        btid = BatchTransactionId(
            transaction_id=b"test-txn-456",
            session_id="session-abc",
            read_timestamp=None,
        )

        partition_result = {
            "partition": b"partition-token-789",
            "read": {
                "table": "users",
                "columns": ["name", "age"],
                "keyset": {"keys": [[1], [2]]},
            },
        }

        encoded = partition_helper.encode_to_string(btid, partition_result)
        decoded = partition_helper.decode_from_string(encoded)

        self.assertEqual(
            decoded.batch_transaction_id.transaction_id, btid.transaction_id
        )
        self.assertEqual(decoded.batch_transaction_id.session_id, btid.session_id)
        self.assertIsNone(decoded.batch_transaction_id.read_timestamp)

        self.assertEqual(decoded.partition_result["partition"], b"partition-token-789")
        self.assertEqual(decoded.partition_result["read"]["table"], "users")
        self.assertEqual(decoded.partition_result["read"]["columns"], ["name", "age"])
        self.assertEqual(
            decoded.partition_result["read"]["keyset"], {"keys": [[1], [2]]}
        )

    def test_insecure_deserialization_failure(self):
        # Malicious payload that attempts to execute pickle.loads under old code
        # (Here, we'll just pass invalid JSON wrapped in gzip + base64, or a pickle payload,
        # and make sure it does NOT get deserialized or execute anything, but raises an error gracefully)

        # A valid pickle payload for some simple object, base64 encoded and compressed
        import pickle

        pickle_bytes = pickle.dumps({"test": "payload"})
        gzip_bytes = gzip.compress(pickle_bytes)
        encoded_pickle = base64.b64encode(gzip_bytes).decode("utf-8")

        # Since we now use json.loads, a pickle payload will fail to decode as UTF-8 / JSON
        with self.assertRaises((json.JSONDecodeError, UnicodeDecodeError)):
            partition_helper.decode_from_string(encoded_pickle)

    def test_protobuf_round_trip_reversibility(self):
        # Any Protobuf message returned by Spanner options must be fully and reversibly
        # round-trip deserializable to its original class, not falling back to a dict.
        for cls_name, cls in partition_helper._PROTO_CLASS_MAP.items():
            instance = cls()
            serialized = partition_helper._serialize_value(instance)
            deserialized = partition_helper._deserialize_value(serialized)
            self.assertIsInstance(deserialized, cls)
            self.assertEqual(deserialized.__class__.__name__, cls_name)

    def test_dynamic_partition_options_registered(self):
        # Dynamically verify that any Protobuf message class generated inside query_info or read_info
        # during partitioning is registered in _PROTO_CLASS_MAP.
        from unittest.mock import MagicMock

        from google.protobuf.message import Message

        from google.cloud.spanner_v1.database import BatchSnapshot
        from google.cloud.spanner_v1.types import DirectedReadOptions, ExecuteSqlRequest

        db = MagicMock()
        db.observability_options = {}
        db._instance._client._query_options = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1"
        )

        snapshot = BatchSnapshot(db)
        snapshot._snapshot = MagicMock()
        snapshot._snapshot.partition_query.return_value = [b"token-123"]
        snapshot._snapshot.partition_read.return_value = [b"token-456"]

        query_options = ExecuteSqlRequest.QueryOptions(optimizer_version="2")
        directed_read_options = DirectedReadOptions()

        query_batches = list(
            snapshot.generate_query_batches(
                sql="SELECT 1",
                query_options=query_options,
                directed_read_options=directed_read_options,
            )
        )

        from google.cloud.spanner_v1.keyset import KeySet

        read_batches = list(
            snapshot.generate_read_batches(
                table="users",
                columns=["name"],
                keyset=KeySet(all_=True),
                directed_read_options=directed_read_options,
            )
        )

        discovered_protobuf_classes = set()

        def collect_protobufs(val):
            if isinstance(val, dict):
                for v in val.values():
                    collect_protobufs(v)
            elif isinstance(val, list):
                for v in val:
                    collect_protobufs(v)
            elif hasattr(val, "_pb") or isinstance(val, Message):
                discovered_protobuf_classes.add(val.__class__)

        for batch in query_batches + read_batches:
            collect_protobufs(batch)

        registered_classes = set(partition_helper._PROTO_CLASS_MAP.values())
        for cls in discovered_protobuf_classes:
            with self.subTest(cls_name=cls.__name__):
                self.assertIn(
                    cls,
                    registered_classes,
                    f"Protobuf class '{cls.__name__}' is generated in partition batch details "
                    f"but is not registered in partition_helper._PROTO_CLASS_MAP! "
                    f"Please add it to _PROTO_CLASS_MAP to prevent silent deserialization failures.",
                )

    def test_all_spanner_param_types_round_trip(self):
        import datetime
        import decimal
        import uuid

        from google.api_core.datetime_helpers import DatetimeWithNanoseconds

        from google.cloud.spanner_v1.data_types import Interval, JsonObject

        complex_params = {
            "uuid_val": uuid.UUID("12345678-1234-5678-1234-567812345678"),
            "date_val": datetime.date(2026, 5, 12),
            "decimal_val": decimal.Decimal("99999.99"),
            "interval_val": Interval(months=35, days=12, nanos=54321000),
            "json_val": JsonObject({"name": "Alice", "active": True}),
            "timestamp_val": datetime.datetime(
                2026, 5, 12, 12, 34, 56, tzinfo=datetime.timezone.utc
            ),
            "timestamp_nanos_val": DatetimeWithNanoseconds(
                2026, 5, 12, 12, 34, 56, 123456, tzinfo=datetime.timezone.utc
            ),
            "bytes_val": b"binary-data",
            "bool_val": True,
            "int_val": 100,
            "float_val": 123.45,
            "str_val": "hello-world",
            "none_val": None,
        }

        # DYNAMIC AST VERIFICATION OF CORE SDK SUPPORTED TYPES
        # Dynamically discover all classes checked by `isinstance` inside Spanner's `_make_value_pb`.
        import ast
        import inspect

        from google.cloud.spanner_v1._helpers import _make_value_pb

        source = inspect.getsource(_make_value_pb)
        tree = ast.parse(source)

        discovered_types = set()
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "isinstance"
            ):
                if (
                    len(node.args) >= 2
                    and isinstance(node.args[0], ast.Name)
                    and node.args[0].id == "value"
                ):
                    type_arg = node.args[1]
                    if isinstance(type_arg, ast.Tuple):
                        for elt in type_arg.elts:
                            if isinstance(elt, ast.Name):
                                discovered_types.add(elt.id)
                    elif isinstance(type_arg, ast.Name):
                        discovered_types.add(type_arg.id)
                    elif isinstance(type_arg, ast.Attribute):
                        discovered_types.add(type_arg.attr)

        # Map our test's `complex_params` actual class/instance types to the class name strings
        test_param_class_names = set()
        for val in complex_params.values():
            if val is not None:
                test_param_class_names.add(val.__class__.__name__)
                # Also map base classes (e.g., DatetimeWithNanoseconds inherits from datetime)
                for base in val.__class__.__mro__:
                    test_param_class_names.add(base.__name__)

        # Special mappings for primitive built-ins checked in standard library or tuple serialization
        test_param_class_names.update({"list", "tuple", "Message", "ListValue"})

        # Assert that every type validated in Spanner SDK's _make_value_pb
        # has a corresponding test parameter type implemented in our round-trip check
        for sdk_type in discovered_types:
            with self.subTest(sdk_type=sdk_type):
                self.assertIn(
                    sdk_type,
                    test_param_class_names,
                    f"Spanner SDK parameter helper (_make_value_pb) supports type '{sdk_type}', "
                    f"but this type has not been implemented/mapped in the DB-API partition "
                    f"helper tests! Please add a verification case for it.",
                )

        # For each parameter type, try round-trip serialization through partition encode/decode
        btid = BatchTransactionId(
            transaction_id=b"test-txn",
            session_id="session-123",
            read_timestamp=None,
        )
        partition_result = {
            "partition": b"token-123",
            "query": {
                "sql": "SELECT 1",
                "params": complex_params,
            },
        }

        encoded = partition_helper.encode_to_string(btid, partition_result)
        decoded = partition_helper.decode_from_string(encoded)
        deserialized_params = decoded.partition_result["query"]["params"]

        # Verify the deserialized parameters are standard Spanner primitive representations:
        self.assertEqual(deserialized_params["int_val"], "100")
        self.assertEqual(
            deserialized_params["uuid_val"], str(complex_params["uuid_val"])
        )
        self.assertEqual(
            deserialized_params["date_val"], complex_params["date_val"].isoformat()
        )
        self.assertEqual(
            deserialized_params["decimal_val"], str(complex_params["decimal_val"])
        )
        self.assertEqual(
            deserialized_params["interval_val"], str(complex_params["interval_val"])
        )
        self.assertEqual(
            deserialized_params["json_val"], complex_params["json_val"].serialize()
        )
        self.assertEqual(
            deserialized_params["timestamp_val"], "2026-05-12T12:34:56.000000Z"
        )
        self.assertEqual(
            deserialized_params["timestamp_nanos_val"], "2026-05-12T12:34:56.123456Z"
        )

        self.assertEqual(
            deserialized_params["bytes_val"], b"binary-data".decode("utf-8")
        )
        self.assertEqual(deserialized_params["bool_val"], True)
        self.assertEqual(deserialized_params["float_val"], 123.45)
        self.assertEqual(deserialized_params["str_val"], "hello-world")
        self.assertIsNone(deserialized_params["none_val"])
