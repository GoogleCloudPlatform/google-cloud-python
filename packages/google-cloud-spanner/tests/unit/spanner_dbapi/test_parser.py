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

import sys
import unittest


class TestParser(unittest.TestCase):
    skip_condition = sys.version_info[0] < 3
    skip_message = "Subtests are not supported in Python 2"

    @unittest.skipIf(skip_condition, skip_message)
    def test_func(self):
        from google.cloud.spanner_dbapi.parser import (
            FUNC,
            a_args,
            expect,
            func,
            pyfmt_str,
        )

        cases = [
            ("_91())", ")", func("_91", a_args([]))),
            ("_a()", "", func("_a", a_args([]))),
            ("___()", "", func("___", a_args([]))),
            ("abc()", "", func("abc", a_args([]))),
            (
                "AF112(%s, LOWER(%s, %s), rand(%s, %s, TAN(%s, %s)))",
                "",
                func(
                    "AF112",
                    a_args(
                        [
                            pyfmt_str,
                            func("LOWER", a_args([pyfmt_str, pyfmt_str])),
                            func(
                                "rand",
                                a_args(
                                    [
                                        pyfmt_str,
                                        pyfmt_str,
                                        func("TAN", a_args([pyfmt_str, pyfmt_str])),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
            ),
        ]

        for text, want_unconsumed, want_parsed in cases:
            with self.subTest(text=text):
                got_unconsumed, got_parsed = expect(text, FUNC)
                self.assertEqual(got_parsed, want_parsed)
                self.assertEqual(got_unconsumed, want_unconsumed)

    @unittest.skipIf(skip_condition, skip_message)
    def test_func_fail(self):
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError
        from google.cloud.spanner_dbapi.parser import FUNC, expect

        cases = [
            ("", "FUNC: `` does not begin with `a-zA-z` nor a `_`"),
            ("91", "FUNC: `91` does not begin with `a-zA-z` nor a `_`"),
            ("_91", "supposed to begin with `\\(`"),
            ("_91(", "supposed to end with `\\)`"),
            ("_.()", "supposed to begin with `\\(`"),
            ("_a.b()", "supposed to begin with `\\(`"),
        ]

        for text, wantException in cases:
            with self.subTest(text=text):
                self.assertRaisesRegex(
                    ProgrammingError, wantException, lambda: expect(text, FUNC)
                )

    def test_func_eq(self):
        from google.cloud.spanner_dbapi.parser import func

        func1 = func("func1", None)
        func2 = func("func2", None)
        self.assertFalse(func1 == object)
        self.assertFalse(func1 == func2)
        func2.name = func1.name
        func1.args = 0
        func2.args = "0"
        self.assertFalse(func1 == func2)
        func1.args = [0]
        func2.args = [0, 0]
        self.assertFalse(func1 == func2)
        func2.args = func1.args
        self.assertTrue(func1 == func2)

    @unittest.skipIf(skip_condition, skip_message)
    def test_a_args(self):
        from google.cloud.spanner_dbapi.parser import (
            ARGS,
            a_args,
            expect,
            func,
            pyfmt_str,
        )

        cases = [
            ("()", "", a_args([])),
            ("(%s)", "", a_args([pyfmt_str])),
            ("(%s,)", "", a_args([pyfmt_str])),
            ("(%s),", ",", a_args([pyfmt_str])),
            (
                "(%s,%s, f1(%s, %s))",
                "",
                a_args(
                    [pyfmt_str, pyfmt_str, func("f1", a_args([pyfmt_str, pyfmt_str]))]
                ),
            ),
        ]

        for text, want_unconsumed, want_parsed in cases:
            with self.subTest(text=text):
                got_unconsumed, got_parsed = expect(text, ARGS)
                self.assertEqual(got_parsed, want_parsed)
                self.assertEqual(got_unconsumed, want_unconsumed)

    @unittest.skipIf(skip_condition, skip_message)
    def test_a_args_fail(self):
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError
        from google.cloud.spanner_dbapi.parser import ARGS, expect

        cases = [
            ("", "ARGS: supposed to begin with `\\(`"),
            ("(", "ARGS: supposed to end with `\\)`"),
            (")", "ARGS: supposed to begin with `\\(`"),
            ("(%s,%s, f1(%s, %s), %s", "ARGS: supposed to end with `\\)`"),
        ]

        for text, wantException in cases:
            with self.subTest(text=text):
                self.assertRaisesRegex(
                    ProgrammingError, wantException, lambda: expect(text, ARGS)
                )

    def test_a_args_has_expr(self):
        from google.cloud.spanner_dbapi.parser import a_args

        self.assertFalse(a_args([]).has_expr())
        self.assertTrue(a_args([[0]]).has_expr())

    def test_a_args_eq(self):
        from google.cloud.spanner_dbapi.parser import a_args

        a1 = a_args([0])
        self.assertFalse(a1 == object())
        a2 = a_args([0, 0])
        self.assertFalse(a1 == a2)
        a1.argv = [0, 1]
        self.assertFalse(a1 == a2)
        a2.argv = [0, 1]
        self.assertTrue(a1 == a2)

    def test_a_args_homogeneous(self):
        from google.cloud.spanner_dbapi.parser import a_args, terminal

        a_obj = a_args([a_args([terminal(10**i)]) for i in range(10)])
        self.assertTrue(a_obj.homogenous())

        a_obj = a_args([a_args([[object()]]) for _ in range(10)])
        self.assertFalse(a_obj.homogenous())

    def test_a_args__is_equal_length(self):
        from google.cloud.spanner_dbapi.parser import a_args

        a_obj = a_args([])
        self.assertTrue(a_obj._is_equal_length())

    @unittest.skipIf(skip_condition, "Python 2 has an outdated iterator definition")
    @unittest.skipIf(
        skip_condition, "Python 2 does not support 0-argument super() calls"
    )
    def test_values(self):
        from google.cloud.spanner_dbapi.parser import a_args, terminal, values

        a_obj = a_args([a_args([terminal(10**i)]) for i in range(10)])
        self.assertEqual(str(values(a_obj)), "VALUES%s" % str(a_obj))

    def test_expect(self):
        from google.cloud.spanner_dbapi import exceptions
        from google.cloud.spanner_dbapi.parser import ARGS, expect

        with self.assertRaises(exceptions.ProgrammingError):
            expect(word="", token=ARGS)
        with self.assertRaises(exceptions.ProgrammingError):
            expect(word="ABC", token=ARGS)
        with self.assertRaises(exceptions.ProgrammingError):
            expect(word="(", token=ARGS)

        with self.assertRaises(exceptions.ProgrammingError):
            expect(word="", token="ABC")

    @unittest.skipIf(skip_condition, skip_message)
    def test_expect_values(self):
        from google.cloud.spanner_dbapi.parser import (
            VALUES,
            a_args,
            expect,
            func,
            pyfmt_str,
            values,
        )

        cases = [
            ("VALUES ()", "", values([a_args([])])),
            ("VALUES", "", values([])),
            ("VALUES(%s)", "", values([a_args([pyfmt_str])])),
            ("    VALUES    (%s)    ", "", values([a_args([pyfmt_str])])),
            ("VALUES(%s, %s)", "", values([a_args([pyfmt_str, pyfmt_str])])),
            (
                "VALUES(%s, %s, LOWER(%s, %s))",
                "",
                values(
                    [
                        a_args(
                            [
                                pyfmt_str,
                                pyfmt_str,
                                func("LOWER", a_args([pyfmt_str, pyfmt_str])),
                            ]
                        )
                    ]
                ),
            ),
            (
                "VALUES (UPPER(%s)), (%s)",
                "",
                values(
                    [a_args([func("UPPER", a_args([pyfmt_str]))]), a_args([pyfmt_str])]
                ),
            ),
        ]

        for text, want_unconsumed, want_parsed in cases:
            with self.subTest(text=text):
                got_unconsumed, got_parsed = expect(text, VALUES)
                self.assertEqual(got_parsed, want_parsed)
                self.assertEqual(got_unconsumed, want_unconsumed)

    @unittest.skipIf(skip_condition, skip_message)
    def test_expect_values_fail(self):
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError
        from google.cloud.spanner_dbapi.parser import VALUES, expect

        cases = [
            ("", "VALUES: `` does not start with VALUES"),
            (
                "VALUES(%s, %s, (%s, %s))",
                "FUNC: `\\(%s, %s\\)\\)` does not begin with `a-zA-z` nor a `_`",
            ),
            ("VALUES(%s),,", "ARGS: supposed to begin with `\\(` in `,`"),
        ]

        for text, wantException in cases:
            with self.subTest(text=text):
                self.assertRaisesRegex(
                    ProgrammingError, wantException, lambda: expect(text, VALUES)
                )
