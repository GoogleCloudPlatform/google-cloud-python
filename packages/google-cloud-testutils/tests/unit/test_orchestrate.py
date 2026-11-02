# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools
import threading

try:
    from unittest import mock
except ImportError:  # pragma: NO PY3 COVER
    import mock  # type: ignore

import pytest  # type: ignore

from test_utils import orchestrate


def test__permutations():
    sequence = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    permutations = orchestrate._permutations(sequence)
    assert len(permutations) == 1680

    result = list(permutations)
    assert len(permutations) == len(result)  # computed length matches reality
    assert len(result) == len(set(result))  # no duplicates
    assert result[0] == (1, 1, 1, 2, 2, 2, 3, 3, 3)
    assert result[-1] == (3, 3, 3, 2, 2, 2, 1, 1, 1)

    assert list(orchestrate._permutations([1, 2, 3])) == [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    ]


class Test_orchestrate:
    @staticmethod
    def test_bad_keyword_argument():
        with pytest.raises(TypeError):
            orchestrate.orchestrate(None, None, what="for?")

    @staticmethod
    def test_no_failures():
        test_calls = []

        def make_test(name):
            def test():  # pragma: NO COVER
                test_calls.append(name)  # pragma: SYNCPOINT
                test_calls.append(name)  # pragma: SYNCPOINT
                test_calls.append(name)

            return test

        test1 = make_test("A")
        test2 = make_test("B")

        permutations = orchestrate._permutations(["A", "B", "A", "B", "A", "B"])
        expected = list(itertools.chain(*permutations))

        counts = orchestrate.orchestrate(test1, test2)
        assert counts == (3, 3)
        assert test_calls == expected

    @staticmethod
    def test_named_syncpoints():
        test_calls = []

        def make_test(name):
            def test():  # pragma: NO COVER
                test_calls.append(name)  # pragma: SYNCPOINT test_named_syncpoints
                test_calls.append(name)  # pragma: SYNCPOINT test_named_syncpoints
                test_calls.append(name)  # pragma: SYNCPOINT

            return test

        test1 = make_test("A")
        test2 = make_test("B")

        permutations = orchestrate._permutations(["A", "B", "A", "B", "A", "B"])
        expected = list(itertools.chain(*permutations))

        counts = orchestrate.orchestrate(test1, test2, name="test_named_syncpoints")
        assert counts == (3, 3)
        assert test_calls == expected

    @staticmethod
    def test_syncpoints_decrease_after_initial_run():
        test_calls = []

        def make_test(name):
            syncpoints = [name] * 4

            def test():  # pragma: NO COVER
                test_calls.append(name)
                if syncpoints:
                    syncpoints.pop()  # pragma: SYNCPOINT
                    test_calls.append(name)

            return test

        test1 = make_test("A")
        test2 = make_test("B")

        expected = [
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "B",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
        ]

        counts = orchestrate.orchestrate(test1, test2)
        assert counts == (2, 2)
        assert test_calls == expected

    @staticmethod
    def test_syncpoints_increase_after_initial_run():
        test_calls = []

        def do_nothing():  # pragma: NO COVER
            pass

        def make_test(name):
            syncpoints = [None] * 4

            def test():  # pragma: NO COVER
                test_calls.append(name)  # pragma: SYNCPOINT
                test_calls.append(name)

                if syncpoints:
                    syncpoints.pop()
                else:
                    do_nothing()  # pragma: SYNCPOINT
                    test_calls.append(name)

            return test

        test1 = make_test("A")
        test2 = make_test("B")

        expected = [
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "B",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "B",
            "A",
            "A",
            "A",
            "B",
        ]

        counts = orchestrate.orchestrate(test1, test2)
        assert counts == (2, 2)
        assert test_calls == expected

    @staticmethod
    def test_failure():
        test_calls = []

        def make_test(name):
            syncpoints = [None] * 4

            def test():  # pragma: NO COVER
                test_calls.append(name)  # pragma: SYNCPOINT
                test_calls.append(name)

                if syncpoints:
                    syncpoints.pop()
                else:
                    assert True is False

            return test

        test1 = make_test("A")
        test2 = make_test("B")

        expected = [
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "B",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
        ]

        with pytest.raises(AssertionError):
            orchestrate.orchestrate(test1, test2)

        assert test_calls == expected


def test__conductor():
    conductor = orchestrate._Conductor()
    items = []

    def run_in_test_thread():
        conductor.notify()
        items.append("test1")
        conductor.standby()
        items.append("test2")
        conductor.notify()
        conductor.standby()
        items.append("test3")
        conductor.notify()

    assert not items
    test_thread = threading.Thread(target=run_in_test_thread)

    test_thread.start()
    conductor.wait()
    assert items == ["test1"]

    conductor.go()
    conductor.wait()
    assert items == ["test1", "test2"]

    conductor.go()
    conductor.wait()
    assert items == ["test1", "test2", "test3"]


def test__get_syncpoints():  # pragma: SYNCPOINT test_get_syncpoints
    with open(__file__, "r") as file:
        lines = enumerate(file, start=1)
        for expected_lineno, line in lines:  # pragma: NO BRANCH COVER
            if "# pragma: SYNCPOINT test_get_syncpoints" in line:
                break

    orchestrate._get_syncpoints(__file__)
    syncpoints = orchestrate._SYNCPOINTS[__file__]["test_get_syncpoints"]
    assert syncpoints == {expected_lineno}


class Test_TestThread:
    @staticmethod
    def test__sync():
        test_thread = orchestrate._TestThread(None, None)
        test_thread.conductor = mock.Mock()
        test_thread._sync()

        test_thread.conductor.notify.assert_called_once_with()
        test_thread.conductor.standby.assert_called_once_with()

    @staticmethod
    def test__trace_no_source_file():
        orchestrate._SYNCPOINTS.clear()
        frame = mock.Mock(f_globals={}, spec=("f_globals",))
        test_thread = orchestrate._TestThread(None, None)
        assert test_thread._trace(frame, None, None) is None
        assert not orchestrate._SYNCPOINTS

    @staticmethod
    def test__trace_this_source_file():
        orchestrate._SYNCPOINTS.clear()
        frame = mock.Mock(
            f_globals={"__file__": __file__},
            f_lineno=1,
            spec=(
                "f_globals",
                "f_lineno",
            ),
        )
        test_thread = orchestrate._TestThread(None, None)
        assert test_thread._trace(frame, None, None) == test_thread._trace
        assert __file__ in orchestrate._SYNCPOINTS

    @staticmethod
    def test__trace_reach_syncpoint():
        with open(__file__, "r") as file:
            lines = enumerate(file, start=1)
            for syncpoint_lineno, line in lines:  # pragma: NO BRANCH COVER
                if "# pragma: SYNCPOINT test_get_syncpoints" in line:
                    break

        orchestrate._SYNCPOINTS.clear()
        frame = mock.Mock(
            f_globals={"__file__": __file__},
            f_lineno=syncpoint_lineno,
            spec=(
                "f_globals",
                "f_lineno",
            ),
        )
        test_thread = orchestrate._TestThread(None, "test_get_syncpoints")
        test_thread._sync = mock.Mock()
        assert test_thread._trace(frame, None, None) == test_thread._trace
        test_thread._sync.assert_not_called()

        frame = mock.Mock(
            f_globals={"__file__": __file__},
            f_lineno=syncpoint_lineno + 1,
            spec=(
                "f_globals",
                "f_lineno",
            ),
        )
        assert test_thread._trace(frame, None, None) == test_thread._trace
        test_thread._sync.assert_called_once_with()

    @staticmethod
    def test__trace_other_source_file_with_no_syncpoints():
        filename = orchestrate.__file__
        if filename.endswith(".pyc"):  # pragma: NO COVER
            filename = filename[:-1]

        orchestrate._SYNCPOINTS.clear()
        frame = mock.Mock(
            f_globals={"__file__": filename + "c"},
            f_lineno=1,
            spec=(
                "f_globals",
                "f_lineno",
            ),
        )
        test_thread = orchestrate._TestThread(None, None)
        assert test_thread._trace(frame, None, None) is None
        syncpoints = orchestrate._SYNCPOINTS[filename]
        assert not syncpoints
