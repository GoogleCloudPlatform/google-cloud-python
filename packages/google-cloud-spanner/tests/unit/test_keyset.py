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


import unittest


class TestKeyRange(unittest.TestCase):
    def _get_target_class(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        return KeyRange

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor_no_start_no_end(self):
        with self.assertRaises(ValueError):
            self._make_one()

    def test_ctor_w_start_open_and_start_closed(self):
        KEY_1 = ["key_1"]
        KEY_2 = ["key_2"]
        with self.assertRaises(ValueError):
            self._make_one(start_open=KEY_1, start_closed=KEY_2)

    def test_ctor_w_end_open_and_end_closed(self):
        KEY_1 = ["key_1"]
        KEY_2 = ["key_2"]
        with self.assertRaises(ValueError):
            self._make_one(end_open=KEY_1, end_closed=KEY_2)

    def test_ctor_w_only_start_open(self):
        KEY_1 = ["key_1"]
        krange = self._make_one(start_open=KEY_1)
        self.assertEqual(krange.start_open, KEY_1)
        self.assertEqual(krange.start_closed, None)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, [])

    def test_ctor_w_only_start_closed(self):
        KEY_1 = ["key_1"]
        krange = self._make_one(start_closed=KEY_1)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, KEY_1)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, [])

    def test_ctor_w_only_end_open(self):
        KEY_1 = ["key_1"]
        krange = self._make_one(end_open=KEY_1)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, [])
        self.assertEqual(krange.end_open, KEY_1)
        self.assertEqual(krange.end_closed, None)

    def test_ctor_w_only_end_closed(self):
        KEY_1 = ["key_1"]
        krange = self._make_one(end_closed=KEY_1)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, [])
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, KEY_1)

    def test_ctor_w_start_open_and_end_closed(self):
        KEY_1 = ["key_1"]
        KEY_2 = ["key_2"]
        krange = self._make_one(start_open=KEY_1, end_closed=KEY_2)
        self.assertEqual(krange.start_open, KEY_1)
        self.assertEqual(krange.start_closed, None)
        self.assertEqual(krange.end_open, None)
        self.assertEqual(krange.end_closed, KEY_2)

    def test_ctor_w_start_closed_and_end_open(self):
        KEY_1 = ["key_1"]
        KEY_2 = ["key_2"]
        krange = self._make_one(start_closed=KEY_1, end_open=KEY_2)
        self.assertEqual(krange.start_open, None)
        self.assertEqual(krange.start_closed, KEY_1)
        self.assertEqual(krange.end_open, KEY_2)
        self.assertEqual(krange.end_closed, None)

    def test___eq___self(self):
        key_1 = ["key_1"]
        krange = self._make_one(end_open=key_1)
        self.assertEqual(krange, krange)

    def test___eq___other_type(self):
        key_1 = ["key_1"]
        krange = self._make_one(end_open=key_1)
        self.assertNotEqual(krange, object())

    def test___eq___other_hit(self):
        key_1 = ["key_1"]
        krange = self._make_one(end_open=key_1)
        other = self._make_one(end_open=key_1)
        self.assertEqual(krange, other)

    def test___eq___other(self):
        key_1 = ["key_1"]
        key_2 = ["key_2"]
        krange = self._make_one(end_open=key_1)
        other = self._make_one(start_closed=key_2, end_open=key_1)
        self.assertNotEqual(krange, other)

    def test_to_pb_w_start_closed_and_end_open(self):
        from google.cloud.spanner_v1.types.keys import KeyRange as KeyRangePB

        key1 = "key_1"
        key2 = "key_2"
        key_range = self._make_one(start_closed=[key1], end_open=[key2])
        key_range_pb = key_range._to_pb()
        expected = KeyRangePB(
            start_closed=[key1],
            end_open=[key2],
        )
        self.assertEqual(key_range_pb, expected)

    def test_to_pb_w_start_open_and_end_closed(self):
        from google.cloud.spanner_v1.types.keys import KeyRange as KeyRangePB

        key1 = "key_1"
        key2 = "key_2"
        key_range = self._make_one(start_open=[key1], end_closed=[key2])
        key_range_pb = key_range._to_pb()
        expected = KeyRangePB(start_open=[key1], end_closed=[key2])
        self.assertEqual(key_range_pb, expected)

    def test_to_pb_w_empty_list(self):
        from google.cloud.spanner_v1.types.keys import KeyRange as KeyRangePB

        key = "key"
        key_range = self._make_one(start_closed=[], end_closed=[key])
        key_range_pb = key_range._to_pb()
        expected = KeyRangePB(start_closed=[], end_closed=[key])
        self.assertEqual(key_range_pb, expected)

    def test_to_dict_w_start_closed_and_end_open(self):
        key1 = "key_1"
        key2 = "key_2"
        key_range = self._make_one(start_closed=[key1], end_open=[key2])
        expected = {"start_closed": [key1], "end_open": [key2]}
        self.assertEqual(key_range._to_dict(), expected)

    def test_to_dict_w_start_open_and_end_closed(self):
        key1 = "key_1"
        key2 = "key_2"
        key_range = self._make_one(start_open=[key1], end_closed=[key2])
        expected = {"start_open": [key1], "end_closed": [key2]}
        self.assertEqual(key_range._to_dict(), expected)

    def test_to_dict_w_end_closed(self):
        key = "key"
        key_range = self._make_one(end_closed=[key])
        expected = {"end_closed": [key]}
        self.assertEqual(key_range._to_dict(), expected)


class TestKeySet(unittest.TestCase):
    def _get_target_class(self):
        from google.cloud.spanner_v1.keyset import KeySet

        return KeySet

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor_w_all(self):
        keyset = self._make_one(all_=True)

        self.assertTrue(keyset.all_)
        self.assertEqual(keyset.keys, [])
        self.assertEqual(keyset.ranges, [])

    def test_ctor_w_keys(self):
        KEYS = [["key1"], ["key2"]]

        keyset = self._make_one(keys=KEYS)

        self.assertFalse(keyset.all_)
        self.assertEqual(keyset.keys, KEYS)
        self.assertEqual(keyset.ranges, [])

    def test_ctor_w_ranges(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        range_1 = KeyRange(start_closed=["key1"], end_open=["key3"])
        range_2 = KeyRange(start_open=["key5"], end_closed=["key6"])

        keyset = self._make_one(ranges=[range_1, range_2])

        self.assertFalse(keyset.all_)
        self.assertEqual(keyset.keys, [])
        self.assertEqual(keyset.ranges, [range_1, range_2])

    def test_ctor_w_all_and_keys(self):
        with self.assertRaises(ValueError):
            self._make_one(all_=True, keys=[["key1"], ["key2"]])

    def test_ctor_w_all_and_ranges(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        range_1 = KeyRange(start_closed=["key1"], end_open=["key3"])
        range_2 = KeyRange(start_open=["key5"], end_closed=["key6"])

        with self.assertRaises(ValueError):
            self._make_one(all_=True, ranges=[range_1, range_2])

    def test___eq___w_self(self):
        keyset = self._make_one(all_=True)
        self.assertEqual(keyset, keyset)

    def test___eq___w_other_type(self):
        keyset = self._make_one(all_=True)
        self.assertNotEqual(keyset, object())

    def test___eq___w_all_hit(self):
        keyset = self._make_one(all_=True)
        other = self._make_one(all_=True)
        self.assertEqual(keyset, other)

    def test___eq___w_all_miss(self):
        keys = [["key1"], ["key2"]]
        keyset = self._make_one(all_=True)
        other = self._make_one(keys=keys)
        self.assertNotEqual(keyset, other)

    def test___eq___w_keys_hit(self):
        keys = [["key1"], ["key2"]]

        keyset = self._make_one(keys=keys)
        other = self._make_one(keys=keys)

        self.assertEqual(keyset, other)

    def test___eq___w_keys_miss(self):
        keys = [["key1"], ["key2"]]

        keyset = self._make_one(keys=keys[:1])
        other = self._make_one(keys=keys[1:])

        self.assertNotEqual(keyset, other)

    def test___eq___w_ranges_hit(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        range_1 = KeyRange(start_closed=["key1"], end_open=["key3"])
        range_2 = KeyRange(start_open=["key5"], end_closed=["key6"])

        keyset = self._make_one(ranges=[range_1, range_2])
        other = self._make_one(ranges=[range_1, range_2])

        self.assertEqual(keyset, other)

    def test___eq___w_ranges_miss(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        range_1 = KeyRange(start_closed=["key1"], end_open=["key3"])
        range_2 = KeyRange(start_open=["key5"], end_closed=["key6"])

        keyset = self._make_one(ranges=[range_1])
        other = self._make_one(ranges=[range_2])

        self.assertNotEqual(keyset, other)

    def test_to_pb_w_all(self):
        from google.cloud.spanner_v1 import KeySetPB

        keyset = self._make_one(all_=True)

        result = keyset._to_pb()

        self.assertIsInstance(result, KeySetPB)
        self.assertTrue(result.all_)
        self.assertEqual(len(result.keys), 0)
        self.assertEqual(len(result.ranges), 0)

    def test_to_pb_w_only_keys(self):
        from google.cloud.spanner_v1 import KeySetPB

        KEYS = [["key1"], ["key2"]]
        keyset = self._make_one(keys=KEYS)

        result = keyset._to_pb()

        self.assertIsInstance(result, KeySetPB)
        self.assertFalse(result.all_)
        self.assertEqual(len(result.keys), len(KEYS))

        for found, expected in zip(result.keys, KEYS):
            self.assertEqual(len(found), len(expected))
            self.assertEqual(found[0], expected[0])

        self.assertEqual(len(result.ranges), 0)

    def test_to_pb_w_only_ranges(self):
        from google.cloud.spanner_v1 import KeyRangePB, KeySetPB
        from google.cloud.spanner_v1.keyset import KeyRange

        KEY_1 = "KEY_1"
        KEY_2 = "KEY_2"
        KEY_3 = "KEY_3"
        KEY_4 = "KEY_4"
        RANGES = [
            KeyRange(start_open=KEY_1, end_closed=KEY_2),
            KeyRange(start_closed=KEY_3, end_open=KEY_4),
        ]
        keyset = self._make_one(ranges=RANGES)

        result = keyset._to_pb()

        self.assertIsInstance(result, KeySetPB)
        self.assertFalse(result.all_)
        self.assertEqual(len(result.keys), 0)
        self.assertEqual(len(result.ranges), len(RANGES))

        expected_ranges = [
            KeyRangePB(start_open=KEY_1, end_closed=KEY_2),
            KeyRangePB(start_closed=KEY_3, end_open=KEY_4),
        ]
        for found, expected in zip(result.ranges, expected_ranges):
            self.assertEqual(found, expected)

    def test_to_dict_w_all(self):
        keyset = self._make_one(all_=True)
        expected = {"all": True}
        self.assertEqual(keyset._to_dict(), expected)

    def test_to_dict_w_only_keys(self):
        KEYS = [["key1"], ["key2"]]
        keyset = self._make_one(keys=KEYS)

        expected = {"keys": KEYS, "ranges": []}
        self.assertEqual(keyset._to_dict(), expected)

    def test_to_dict_w_only_ranges(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        key_1 = "KEY_1"
        key_2 = "KEY_2"
        key_3 = "KEY_3"
        key_4 = "KEY_4"
        ranges = [
            KeyRange(start_open=[key_1], end_closed=[key_2]),
            KeyRange(start_closed=[key_3], end_open=[key_4]),
        ]
        keyset = self._make_one(ranges=ranges)

        expected = {
            "keys": [],
            "ranges": [
                {"start_open": [key_1], "end_closed": [key_2]},
                {"start_closed": [key_3], "end_open": [key_4]},
            ],
        }
        self.assertEqual(keyset._to_dict(), expected)

    def test_from_dict_w_all(self):
        klass = self._get_target_class()
        mapping = {"all": True}

        keyset = klass._from_dict(mapping)

        self.assertTrue(keyset.all_)
        self.assertEqual(keyset.keys, [])
        self.assertEqual(keyset.ranges, [])

    def test_from_dict_w_keys(self):
        klass = self._get_target_class()
        keys = [["key1"], ["key2"]]
        mapping = {"keys": keys}

        keyset = klass._from_dict(mapping)

        self.assertFalse(keyset.all_)
        self.assertEqual(keyset.keys, keys)
        self.assertEqual(keyset.ranges, [])

    def test_from_dict_w_ranges(self):
        from google.cloud.spanner_v1.keyset import KeyRange

        klass = self._get_target_class()
        key_1 = "KEY_1"
        key_2 = "KEY_2"
        key_3 = "KEY_3"
        key_4 = "KEY_4"
        mapping = {
            "ranges": [
                {"start_open": [key_1], "end_closed": [key_2]},
                {"start_closed": [key_3], "end_open": [key_4]},
            ]
        }

        keyset = klass._from_dict(mapping)

        range_1 = KeyRange(start_open=[key_1], end_closed=[key_2])
        range_2 = KeyRange(start_closed=[key_3], end_open=[key_4])

        self.assertFalse(keyset.all_)
        self.assertEqual(keyset.keys, [])
        self.assertEqual(keyset.ranges, [range_1, range_2])
