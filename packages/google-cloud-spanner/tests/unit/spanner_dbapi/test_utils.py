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

import unittest


class TestUtils(unittest.TestCase):
    def test_PeekIterator(self):
        from google.cloud.spanner_dbapi.utils import PeekIterator

        cases = [
            ("list", [1, 2, 3, 4, 6, 7], [1, 2, 3, 4, 6, 7]),
            ("iter_from_list", iter([1, 2, 3, 4, 6, 7]), [1, 2, 3, 4, 6, 7]),
            ("tuple", ("a", 12, 0xFF), ["a", 12, 0xFF]),
            ("iter_from_tuple", iter(("a", 12, 0xFF)), ["a", 12, 0xFF]),
            ("no_args", (), []),
        ]

        for name, data_in, expected in cases:
            with self.subTest(name=name):
                pitr = PeekIterator(data_in)
                actual = list(pitr)
                self.assertEqual(actual, expected)

    def test_peekIterator_list_rows_converted_to_tuples(self):
        from google.cloud.spanner_dbapi.utils import PeekIterator

        # Cloud Spanner returns results in lists e.g. [result].
        # PeekIterator is used by BaseCursor in its fetch* methods.
        # This test ensures that anything passed into PeekIterator
        # will be returned as a tuple.
        pit = PeekIterator([["a"], ["b"], ["c"], ["d"], ["e"]])
        got = list(pit)
        want = [("a",), ("b",), ("c",), ("d",), ("e",)]
        self.assertEqual(got, want, "Rows of type list must be returned as tuples")

        seventeen = PeekIterator([[17]])
        self.assertEqual(list(seventeen), [(17,)])

        pit = PeekIterator([["%", "%d"]])
        self.assertEqual(next(pit), ("%", "%d"))

        pit = PeekIterator([("Clark", "Kent")])
        self.assertEqual(next(pit), ("Clark", "Kent"))

    def test_peekIterator_nonlist_rows_unconverted(self):
        from google.cloud.spanner_dbapi.utils import PeekIterator

        pi = PeekIterator(["a", "b", "c", "d", "e"])
        got = list(pi)
        want = ["a", "b", "c", "d", "e"]
        self.assertEqual(got, want, "Values should be returned unchanged")

    def test_backtick_unicode(self):
        from google.cloud.spanner_dbapi.utils import backtick_unicode

        cases = [
            ("SELECT (1) as foo WHERE 1=1", "SELECT (1) as foo WHERE 1=1"),
            ("SELECT (1) as föö", "SELECT (1) as `föö`"),
            ("SELECT (1) as `föö`", "SELECT (1) as `föö`"),
            ("SELECT (1) as `föö` `umläut", "SELECT (1) as `föö` `umläut"),
            ("SELECT (1) as `föö", "SELECT (1) as `föö"),
        ]
        for sql, want in cases:
            with self.subTest(sql=sql):
                got = backtick_unicode(sql)
                self.assertEqual(got, want)

    def test_StreamedManyResultSets(self):
        from google.cloud.spanner_dbapi.utils import StreamedManyResultSets

        cases = [
            ("iter_from_list", iter([1, 2, 3, 4, 6, 7]), [1, 2, 3, 4, 6, 7]),
            ("iter_from_tuple", iter(("a", 12, 0xFF)), ["a", 12, 0xFF]),
        ]

        for name, data_in, expected in cases:
            with self.subTest(name=name):
                stream_result = StreamedManyResultSets()
                stream_result._iterators.append(data_in)
                actual = list(stream_result)
                self.assertEqual(actual, expected)

    def test_BufferedIterator(self):
        from google.cloud.spanner_dbapi.utils import BufferedIterator

        cases = [
            ("list_of_lists", [["a", 1], ["b", 2]], [("a", 1), ("b", 2)]),
            ("iter_of_lists", iter([["a", 1], ["b", 2]]), [("a", 1), ("b", 2)]),
            ("list_of_tuples", [("a", 1), ("b", 2)], [("a", 1), ("b", 2)]),
            ("iter_of_tuples", iter([("a", 1), ("b", 2)]), [("a", 1), ("b", 2)]),
            ("empty_list", [], []),
            ("empty_tuple", (), []),
            ("none_source", None, []),
        ]

        for name, data_in, expected in cases:
            with self.subTest(name=name):
                bitr = BufferedIterator(data_in)
                self.assertEqual(len(bitr), len(expected))
                actual = list(bitr)
                self.assertEqual(actual, expected)
                with self.assertRaises(StopIteration):
                    next(bitr)

    def test_BufferedIterator_eagerly_drains_stream(self):
        from google.cloud.spanner_dbapi.utils import BufferedIterator

        drained = False

        def generator():
            nonlocal drained
            yield ["first", 1]
            yield ["second", 2]
            drained = True

        bitr = BufferedIterator(generator())
        # The generator must be completely drained during __init__
        self.assertTrue(drained)
        self.assertEqual(len(bitr), 2)
        self.assertEqual(next(bitr), ("first", 1))
        self.assertEqual(next(bitr), ("second", 2))
        with self.assertRaises(StopIteration):
            next(bitr)
