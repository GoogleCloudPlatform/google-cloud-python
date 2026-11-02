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


import json
import unittest

from google.cloud.spanner_v1.data_types import JsonObject


class Test_JsonObject(unittest.TestCase):
    def _make_one(self, *args, **kwargs):
        return JsonObject(*args, **kwargs)

    def test_serialize_dict(self):
        data = {"id": "m1", "content": "hello"}
        obj = self._make_one(data)
        expected = json.dumps(data, sort_keys=True, separators=(",", ":"))
        self.assertEqual(obj.serialize(), expected)

    def test_serialize_array(self):
        data = [{"id": "m1", "content": "hello"}]
        obj = self._make_one(data)
        expected = json.dumps(data, sort_keys=True, separators=(",", ":"))
        self.assertEqual(obj.serialize(), expected)

    def test_serialize_scalar(self):
        obj = self._make_one("hello")
        self.assertEqual(obj.serialize(), '"hello"')

    def test_serialize_null(self):
        obj = self._make_one(None)
        self.assertIsNone(obj.serialize())

    def test_serialize_nested_array_jsonobject(self):
        obj = self._make_one([JsonObject([1, 2]), JsonObject(42)])
        self.assertEqual(obj.serialize(), "[[1,2],42]")

    def test_from_str(self):
        obj = JsonObject.from_str('{"id": "m1"}')
        self.assertEqual(obj.serialize(), '{"id":"m1"}')

    def test_from_str_array(self):
        obj = JsonObject.from_str('[{"id": "m1"}]')
        self.assertEqual(obj.serialize(), '[{"id":"m1"}]')

    def test_from_str_null(self):
        obj = JsonObject.from_str("null")
        self.assertIsNone(obj.serialize())


class Test_JsonObject_dict_protocol(unittest.TestCase):
    """Verify that JsonObject behaves correctly with standard Python
    operations (len, bool, iteration, indexing) for all JSON variants."""

    def test_asymmetric_equality(self):
        a = JsonObject()
        b = JsonObject(None)
        self.assertEqual(a == b, b == a, "Equality symmetry is broken!")
        self.assertEqual(a, b)

    def test_tuple_vs_list_equality(self):
        tup = JsonObject((1, 2))
        lst = JsonObject([1, 2])
        self.assertEqual(tup, lst)
        self.assertEqual(tup, [1, 2])

    def test_get_method(self):
        arr = JsonObject([10, 20])
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)
        self.assertIsNone(arr.get(2))
        obj = JsonObject({"a": 1})
        self.assertEqual(obj.get("a"), 1)
        self.assertIsNone(obj.get("b"))
        scalar = JsonObject(42)
        self.assertIsNone(scalar.get("a"))

    def test_copy_method(self):
        arr = JsonObject([10, 20])
        cp_arr = arr.copy()
        self.assertEqual(cp_arr, arr)
        self.assertEqual(cp_arr.get(0), 10)

        obj = JsonObject({"a": 1})
        cp_obj = obj.copy()
        self.assertEqual(cp_obj, obj)

        scalar = JsonObject(42)
        cp_scalar = scalar.copy()
        self.assertEqual(cp_scalar, scalar)

    def test_keys_values_items_pop(self):
        arr = JsonObject([10, 20])
        self.assertEqual(list(arr.keys()), [0, 1])
        self.assertEqual(list(arr.values()), [10, 20])
        self.assertEqual(list(arr.items()), [(0, 10), (1, 20)])
        val = arr.pop(0)
        self.assertEqual(val, 10)
        self.assertEqual(len(arr), 1)

        obj = JsonObject({"a": 1})
        self.assertEqual(list(obj.keys()), ["a"])
        self.assertEqual(list(obj.values()), [1])
        self.assertEqual(list(obj.items()), [("a", 1)])

    def test_null_sentinel_hiding(self):
        null_obj = JsonObject()
        self.assertEqual(list(null_obj), [])
        self.assertNotIn("__json_null__", null_obj)
        null_obj_none = JsonObject(None)
        self.assertEqual(list(null_obj_none), [])
        self.assertNotIn("__json_null__", null_obj_none)

    def test_isinstance_dict(self):
        obj = JsonObject({"a": 1})
        self.assertTrue(isinstance(obj, dict))
        obj_arr = JsonObject([1, 2])
        self.assertTrue(isinstance(obj_arr, dict))

    def test_array_len(self):
        obj = JsonObject([{"id": 1}, {"id": 2}])
        self.assertEqual(len(obj), 2)

    def test_array_bool_truthy(self):
        obj = JsonObject([{"id": 1}])
        self.assertTrue(obj)

    def test_array_bool_empty(self):
        obj = JsonObject([])
        self.assertFalse(obj)

    def test_array_iter(self):
        data = [{"a": 1}, {"b": 2}]
        obj = JsonObject(data)
        self.assertEqual(list(obj), data)

    def test_array_getitem(self):
        data = [{"a": 1}, {"b": 2}]
        obj = JsonObject(data)
        self.assertEqual(obj[0], {"a": 1})
        self.assertEqual(obj[1], {"b": 2})

    def test_array_contains(self):
        data = [1, 2, 3]
        obj = JsonObject(data)
        self.assertIn(2, obj)
        self.assertNotIn(4, obj)

    def test_array_eq(self):
        data = [{"id": 1}]
        obj = JsonObject(data)
        self.assertEqual(obj, data)

    def test_dict_len(self):
        obj = JsonObject({"a": 1, "b": 2})
        self.assertEqual(len(obj), 2)

    def test_dict_bool(self):
        obj = JsonObject({"a": 1})
        self.assertTrue(obj)

    def test_dict_iter(self):
        obj = JsonObject({"a": 1, "b": 2})
        self.assertEqual(sorted(obj), ["a", "b"])

    def test_dict_getitem(self):
        obj = JsonObject({"key": "value"})
        self.assertEqual(obj["key"], "value")

    def test_null_len(self):
        obj = JsonObject(None)
        self.assertEqual(len(obj), 0)

    def test_null_bool(self):
        obj = JsonObject(None)
        self.assertFalse(obj)

    def test_scalar_len(self):
        obj = JsonObject(42)
        self.assertEqual(len(obj), 1)

    def test_scalar_bool(self):
        self.assertTrue(JsonObject(42))
        self.assertFalse(JsonObject(False))
        self.assertFalse(JsonObject(0))
        self.assertFalse(JsonObject(0.0))
        self.assertFalse(JsonObject(""))

    def test_null_eq(self):
        null_obj = JsonObject(None)
        self.assertEqual(null_obj, JsonObject(None))
        self.assertEqual(null_obj, None)
        self.assertNotEqual(null_obj, {})
        self.assertNotEqual(null_obj, JsonObject({}))

    def test_scalar_not_iterable(self):
        obj = JsonObject(42)
        with self.assertRaises(TypeError):
            iter(obj)

    def test_scalar_not_subscriptable(self):
        obj = JsonObject(42)
        with self.assertRaises(TypeError):
            _ = obj[0]


class Test_JsonObject_complex_nested(unittest.TestCase):
    """Complex integration unit tests for deeply nested JsonObject compositions,
    multi-level arrays/dicts, cross-type equality, and edge cases."""

    def test_deeply_nested_serialization(self):
        complex_obj = JsonObject(
            {
                "config": JsonObject({"enabled": True, "timeout": 30}),
                "data": JsonObject(
                    [
                        JsonObject([1, 2]),
                        JsonObject({"score": 42.5}),
                        JsonObject(None),
                    ]
                ),
                "meta": JsonObject("v1.0"),
            }
        )
        expected = (
            '{"config":{"enabled":true,"timeout":30},'
            '"data":[[1,2],{"score":42.5},null],'
            '"meta":"v1.0"}'
        )
        self.assertEqual(complex_obj.serialize(), expected)

    def test_deeply_nested_equality(self):
        obj1 = JsonObject(
            {
                "users": JsonObject(
                    [
                        JsonObject({"id": 1, "roles": JsonObject(["admin"])}),
                        JsonObject({"id": 2, "roles": JsonObject(["user"])}),
                    ]
                )
            }
        )
        obj2 = JsonObject(
            {
                "users": [
                    {"id": 1, "roles": ["admin"]},
                    {"id": 2, "roles": ["user"]},
                ]
            }
        )
        raw_native = {
            "users": [
                {"id": 1, "roles": ["admin"]},
                {"id": 2, "roles": ["user"]},
            ]
        }
        self.assertEqual(obj1, obj2)
        self.assertEqual(obj1, raw_native)

    def test_multi_level_indexing_and_iteration(self):
        data = JsonObject(
            [
                JsonObject([10, 20, 30]),
                JsonObject({"key": "val"}),
            ]
        )
        self.assertEqual(data[0][1], 20)
        self.assertEqual(data[1]["key"], "val")
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 3)
        self.assertIn({"key": "val"}, data)

    def test_triple_rewrapping(self):
        obj = JsonObject(JsonObject(JsonObject([1, 2, 3])))
        self.assertTrue(obj._is_array)
        self.assertEqual(len(obj), 3)
        self.assertEqual(obj[0], 1)
        self.assertEqual(obj.serialize(), "[1,2,3]")


class Test_JsonObject_edge_cases_and_invariants(unittest.TestCase):
    """Edge cases for JsonObject rewrapping and dict invariants."""

    def test_rewrapping_null_object_preserves_null_state(self):
        """Verify that wrapping a null JsonObject preserves _is_null and serialize()."""
        # Test default JsonObject() null
        null_obj = JsonObject()
        rewrapped = JsonObject(null_obj)
        self.assertTrue(
            rewrapped._is_null, "Rewrapped JsonObject lost _is_null=True flag"
        )
        self.assertIsNone(
            rewrapped.serialize(),
            "Rewrapped JsonObject() should serialize to None",
        )
        self.assertFalse(bool(rewrapped), "Rewrapped JsonObject() should be falsy")
        self.assertEqual(len(rewrapped), 0, "Rewrapped JsonObject() length should be 0")

        # Test JsonObject(None) null
        null_none_obj = JsonObject(None)
        rewrapped_none = JsonObject(null_none_obj)
        self.assertTrue(
            rewrapped_none._is_null,
            "Rewrapped JsonObject(None) lost _is_null=True flag",
        )
        self.assertIsNone(
            rewrapped_none.serialize(),
            "Rewrapped JsonObject(None) should serialize to None",
        )

    def test_keys_values_items_dict_invariant_for_arrays(self):
        """Verify keys(), values(), and items() consistency for array JsonObjects."""
        arr = JsonObject([10, 20])
        keys = list(arr.keys())
        values = list(arr.values())
        items = list(arr.items())

        # Standard Python dict invariant: list(keys) MUST match [k for k, v in items]
        self.assertEqual(
            keys,
            [0, 1],
            "keys() should return integer indices matching items() keys",
        )
        self.assertEqual(values, [10, 20], "values() should return array elements")
        self.assertEqual(items, [(0, 10), (1, 20)])
        self.assertEqual(
            keys,
            [k for k, v in items],
            "d.keys() must match [k for k, v in d.items()]",
        )

        # Verify zip(keys, values) reconstructs items
        self.assertEqual(dict(zip(arr.keys(), arr.values())), {0: 10, 1: 20})

    def test_nested_rewrapped_null_serialization(self):
        """Verify nested rewrapped null JsonObjects serialize correctly."""
        from google.cloud.spanner_v1.data_types import _unwrap_for_json

        nested = JsonObject({"a": JsonObject(JsonObject(None))})
        self.assertEqual(nested.serialize(), '{"a":null}')

        raw_unwrapped = _unwrap_for_json({"a": JsonObject(JsonObject(None))})
        self.assertEqual(raw_unwrapped, {"a": None})


class Test_JsonObject_coverage_boost(unittest.TestCase):
    """Targeted unit tests covering all remaining branches in JsonObject."""

    def test_pop_default_and_key_errors(self):
        arr = JsonObject([10])
        self.assertEqual(arr.pop(5, "default"), "default")
        with self.assertRaises(KeyError):
            arr.pop(5)

        scalar = JsonObject(42)
        self.assertEqual(scalar.pop("missing", "default"), "default")
        with self.assertRaises(KeyError):
            scalar.pop("missing")

        null_obj = JsonObject()
        self.assertEqual(null_obj.pop("missing", "default"), "default")
        with self.assertRaises(KeyError):
            null_obj.pop("missing")

    def test_scalar_contains_typeerror(self):
        scalar = JsonObject(42)
        with self.assertRaises(TypeError):
            _ = "item" in scalar

    def test_repr_formatting(self):
        self.assertEqual(repr(JsonObject([1, 2])), "[1, 2]")
        self.assertEqual(repr(JsonObject(42)), "42")
        self.assertEqual(repr(JsonObject({"a": 1})), "{'a': 1}")

    def test_ne_operator(self):
        self.assertTrue(JsonObject(1) != JsonObject(2))
        self.assertFalse(JsonObject(1) != JsonObject(1))

    def test_from_str_scalar(self):
        obj = JsonObject.from_str("42")
        self.assertEqual(obj, 42)
        self.assertTrue(obj._is_scalar_value)

    def test_unwrap_for_json_tuple_and_nested_types(self):
        from google.cloud.spanner_v1.data_types import _unwrap_for_json

        tup_unwrapped = _unwrap_for_json((JsonObject(1), JsonObject(2)))
        self.assertEqual(tup_unwrapped, [1, 2])

    def test_rewrapping_scalar_and_dict_jsonobject(self):
        scalar_rewrapped = JsonObject(JsonObject(42))
        self.assertTrue(scalar_rewrapped._is_scalar_value)
        self.assertEqual(scalar_rewrapped._simple_value, 42)

        dict_rewrapped = JsonObject(JsonObject({"a": 1}))
        self.assertEqual(dict_rewrapped.get("a"), 1)

    def test_values_and_items_for_scalar_null_dict(self):
        self.assertEqual(list(JsonObject(42).values()), [42])
        self.assertEqual(list(JsonObject().values()), [])
        self.assertEqual(list(JsonObject(42).items()), [(0, 42)])
        self.assertEqual(list(JsonObject().items()), [])
        self.assertEqual(list(JsonObject().keys()), [])
        self.assertTrue(JsonObject().copy()._is_null)

    def test_dict_pop_and_contains(self):
        d = JsonObject({"a": 1})
        self.assertEqual(d.pop("missing", "default"), "default")
        self.assertIn("a", d)
        self.assertNotIn("b", d)

    def test_from_str_null(self):
        null_obj = JsonObject.from_str("null")
        self.assertTrue(null_obj._is_null)
        self.assertIsNone(null_obj.serialize())

    def test_unwrap_for_json_scalar(self):
        from google.cloud.spanner_v1.data_types import _unwrap_for_json

        self.assertEqual(_unwrap_for_json(JsonObject(42)), 42)
