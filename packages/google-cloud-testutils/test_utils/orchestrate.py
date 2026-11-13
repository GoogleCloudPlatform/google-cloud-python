# Copyright 2018 Google LLC
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
from __future__ import annotations

import itertools
import math
import queue
import sys
import threading
import tokenize


def orchestrate(*tests, **kwargs):
    """
    Orchestrate a deterministic concurrency test.

    Runs test functions in separate threads, with each thread taking turns running up
    until predefined syncpoints in a deterministic order. All possible orderings are
    tested.

    Most of the time, we try to use logic, best practices, and static analysis to insure
    correct operation of concurrent code. Sometimes our powers of reasoning fail us and,
    either through non-determistic stress testing or running code in production, a
    concurrent bug is discovered. When this occurs, we'd like to have a regression test
    to insure we've understood the problem and implemented a correct solution.
    `orchestrate` provides a means of deterministically testing concurrent code so we
    can write robust regression tests for complex concurrent scenarios.

    `orchestrate` runs each passed in test function in its own thread. Threads then
    "take turns" running. Turns are defined by setting syncpoints in the code under
    test, using comments containing "pragma: SYNCPOINT". `orchestrate` will scan the
    code under test and add syncpoints where it finds these comments.

    For example, let's say you have the following code in production::

        def hither_and_yon(destination):
            hither(destination)
            yon(destination)

    You've found there's a concurrency bug when two threads execute this code with the
    same argument, and you think that by adding a syncpoint between the calls to
    `hither` and `yon` you can reproduce the problem in a regression test. First add a
    comment with "pragma: SYNCPOINT" to the code under test::

        def hither_and_yon(destination):
            hither(destination)   # pragma: SYNCPOINT
            yon(destination)

    When testing with orchestrate, there will now be a syncpoint, or a pause, after the
    call to `hither` and before the call to `yon`. Now you can write a test to exercise
    `hither_and_yon` running in parallel::

        from unittest import mock
        from tests.unit import orchestrate

        from myorg.myproj.sales import travel

        def test_concurrent_hither_and_yon():

            def test_hither_and_yon():
                assert something
                travel.hither_and_yon("Raleigh")
                assert something_else

            counts = orchestrate.orchestrate(test_hither_and_yon, test_hither_and_yon)
            assert counts == (2, 2)

    What `orchestrate` will do now is take each of the two test functions passed in
    (actually the same function, twice, in this case), run them serially, and count the
    number of turns it takes to run each test to completion. In this example, it will
    take two turns for each test: one turn to start the thread and execute up until the
    syncpoint, and then another turn to execute from the syncpoint to the end of the
    test. The number of turns will always be one greater than the number of syncpoints
    encountered when executing the test.

    Once the counts have been taken, `orchestrate` will construct a test sequence that
    represents all of the turns taken by the passed in tests, with each value in the
    sequence representing the index of the test whose turn it is in the sequence. In
    this example, then, it would produce::

        [0, 0, 1, 1]

    This represents the first test taking both of its turns, followed by the second test
    taking both of its turns. At this point this scenario has already been tested,
    because this is what was run to produce the counts and the initial test sequence.
    Now `orchestrate` will run all of the remaining scenarios by finding all the
    permutations of the test sequence and executing those, in turn::

        [0, 1, 0, 1]
        [0, 1, 1, 0]
        [1, 0, 0, 1]
        [1, 0, 1, 0]
        [1, 1, 0, 0]

    You'll notice in our example that since both test functions are actually the same
    function, that although it tested 6 scenarios there are effectively only really 3
    unique scenarios. For the time being, though, `orchestrate` doesn't attempt to
    detect this condition or optimize for it.

    There are some performance considerations that should be taken into account when
    writing tests. The number of unique test sequences grows quite quickly with the
    number of turns taken by the functions under test. Our simple example with two
    threads each taking two turns, only yielded 6 scenarios, but two threads each taking
    6 turns, for example, yields 924 scenarios. Add another six step thread, for a total
    of three threads, and now you have over 17 thousand scenarios. In general, use the
    least number of steps/threads you can get away with and still expose the behavior
    you want to correct.

    For the same reason as above, it is recommended that if you have many concurrent
    tests, that you name your syncpoints so that you're not accidentally using
    syncpoints intended for other tests, as this will add steps to your tests. While
    it's not problematic from a testing standpoint to have extra steps in your tests, it
    can use computing resources unnecessarily. A name can be added to any syncpoint
    after the `SYNCPOINT` keyword in the pragma definition::

        def hither_and_yon(destination):
            hither(destination)   # pragma: SYNCPOINT hither and yon
            yon(destination)

    In your test, then, pass that name to `orchestrate` to cause it to use only
    syncpoints with that name::

        orchestrate.orchestrate(
            test_hither_and_yon, test_hither_and_yon, name="hither and yon"
        )

    As soon as any error or failure is detected, no more scenarios are run
    and that error is propagated to the main thread.

    One limitation of `orchestrate` is that it cannot really be used with `coverage`,
    since both tools use `sys.set_trace`. Any code that needs verifiable test coverage
    should have additional tests that do not use `orchestrate`, since code that is run
    under orchestrate will not show up in a coverage report generated by `coverage`.

    Args:
        tests (Tuple[Callable]): Test functions to be run. These functions will not be
            called with any arguments, so they must not have any required arguments.
        name (Optional[str]): Only use syncpoints with the given name. If omitted, only
            unnamed syncpoints will be used.

    Returns:
        Tuple[int]: A tuple of the count of the number turns for test passed in. Can be
            used a sanity check in tests to make sure you understand what's actually
            happening during a test.
    """
    name = kwargs.pop("name", None)
    if kwargs:
        raise TypeError(
            "Unexpected keyword arguments: {}".format(", ".join(kwargs.keys()))
        )

    # Produce an initial test sequence. The fundamental question we're always trying to
    # answer is "whose turn is it?" First we'll find out how many "turns" each test
    # needs to complete when run serially and use that to construct a sequence of
    # indexes. When a test's index appears in the sequence, it is that test's turn to
    # run. We'll start by constructing a sequence that would run each test through to
    # completion serially, one after the other.
    test_sequence = []
    counts = []
    for index, test in enumerate(tests):
        thread = _TestThread(test, name)
        for count in itertools.count(1):  # pragma: NO BRANCH
            # Pragma is required because loop never finishes naturally.
            thread.go()
            if thread.finished:
                break

        counts.append(count)
        test_sequence += [index] * count

    # Now we can take that initial sequence and generate all of its permutations,
    # running each one to try to uncover concurrency bugs
    sequences = iter(_permutations(test_sequence))

    # We already tested the first sequence getting our counts, so we can discard it
    next(sequences)

    # Test each sequence
    for test_sequence in sequences:
        threads = [_TestThread(test, name) for test in tests]
        try:
            for index in test_sequence:
                threads[index].go()

            # Its possible for number of turns to vary from one test run to the other,
            # especially if there is some undiscovered concurrency bug. Go ahead and
            # finish running each test to completion, if not already complete.
            for thread in threads:
                while not thread.finished:
                    thread.go()

        except Exception:
            # If an exception occurs, we still need to let any threads that are still
            # going finish up. Additional exceptions are silently ignored.
            for thread in threads:
                thread.finish()
            raise

    return tuple(counts)


_local = threading.local()


class _Conductor:
    """Coordinate communication between main thread and a test thread.

    Two way communicaton is maintained between the main thread and a test thread using
    two synchronized queues (`queue.Queue`) each with a size of one.
    """

    def __init__(self):
        self._notify = queue.Queue(1)
        self._go = queue.Queue(1)

    def notify(self):
        """Called from test thread to let us know it's finished or is ready for its next
        turn."""
        self._notify.put(None)

    def standby(self):
        """Called from test thread in order to block until told to go."""
        self._go.get()

    def wait(self):
        """Called from main thread to wait for test thread to either get to the
        next syncpoint or finish."""
        self._notify.get()

    def go(self):
        """Called from main thread to tell test thread to go."""
        self._go.put(None)


_SYNCPOINTS: dict[str, dict[str, set[int]]] = {}
"""Dict[str, Dict[str, Set[int]]]: Dict mapping source fileneme to a dict mapping
syncpoint name to set of line numbers where syncpoints with that name occur in the
source file.
"""


def _get_syncpoints(filename):
    """Find syncpoints in a source file.

    Does a simple tokenization of the source file, looking for comments with "pragma:
    SYNCPOINT", and populates _SYNCPOINTS using the syncpoint name and line number in
    the source file.
    """
    _SYNCPOINTS[filename] = syncpoints = {}

    # Use tokenize to find pragma comments
    with open(filename, "r") as pyfile:
        tokens = tokenize.generate_tokens(pyfile.readline)
        for type, value, start, end, line in tokens:
            if type == tokenize.COMMENT and "pragma: SYNCPOINT" in value:
                name = value.split("SYNCPOINT", 1)[1].strip()
                if not name:
                    name = None

                if name not in syncpoints:
                    syncpoints[name] = set()

                lineno, column = start
                syncpoints[name].add(lineno)


class _TestThread:
    """A thread for a test function."""

    thread = None
    finished = False
    error = None
    at_syncpoint = False

    def __init__(self, test, name):
        self.test = test
        self.name = name
        self.conductor = _Conductor()

    def _run(self):
        sys.settrace(self._trace)
        _local.conductor = self.conductor
        try:
            self.test()
        except Exception as error:
            self.error = error
        finally:
            self.finished = True
            self.conductor.notify()

    def _sync(self):
        # Tell main thread we're finished, for now
        self.conductor.notify()

        # Wait for the main thread to tell us to go again
        self.conductor.standby()

    def _trace(self, frame, event, arg):
        """Argument to `sys.settrace`.

        Handles frames during test run, syncing at syncpoints, when found.

        Returns:
            `None` if no more tracing is required for the function call, `self._trace`
            if tracing should continue.
        """
        if self.at_syncpoint:
            # We hit a syncpoint on the previous call, so now we sync.
            self._sync()
            self.at_syncpoint = False

        filename = frame.f_globals.get("__file__")
        if not filename:
            # Can't trace code without a source file
            return

        if filename.endswith(".pyc"):
            filename = filename[:-1]

        if filename not in _SYNCPOINTS:
            _get_syncpoints(filename)

        syncpoints = _SYNCPOINTS[filename].get(self.name)
        if not syncpoints:
            # This file doesn't contain syncpoints, don't continue to trace
            return

        # We've hit a syncpoint. Execute whatever line the syncpoint is on and then
        # sync next time this gets called.
        if frame.f_lineno in syncpoints:
            self.at_syncpoint = True

        return self._trace

    def go(self):
        if self.finished:
            return

        if self.thread is None:
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

        else:
            self.conductor.go()

        self.conductor.wait()

        if self.error:
            raise self.error

    def finish(self):
        while not self.finished:
            try:
                self.go()
            except Exception:
                pass


class _permutations:
    """Generates a sequence of all permutations of `sequence`.

    Permutations are returned in lexicographic order using the "Generation in
    lexicographic order" algorithm described in `the Wikipedia article on "Permutation"
    <https://en.wikipedia.org/wiki/Permutation>`_.

    This implementation differs significantly from `itertools.permutations` in that the
    value of individual elements is taken into account, thus eliminating redundant
    orderings that would be produced by `itertools.permutations`.

    Args:
        sequence (Sequence[Any]): Sequence must be finite and orderable.

    Returns:
        Sequence[Sequence[Any]]: Set of all permutations of `sequence`.
    """

    def __init__(self, sequence):
        self._start = tuple(sorted(sequence))

    def __len__(self):
        """Compute the number of permutations.

        Let the number of elements in a sequence N and the number of repetitions for
        individual members of the sequence be n1, n2, ... nx. The number of unique
        permutations is: N! / n1! / n2! / ... / nx!.

        For example, let `sequence` be [1, 2, 3, 1, 2, 3, 1, 2, 3]. The number of unique
        permutations is: 9! / 3! / 3! / 3! = 1680.

        See: "Permutations of multisets" in `the Wikipedia article on "Permutation"
        <https://en.wikipedia.org/wiki/Permutation>`_.
        """
        repeats = [len(list(group)) for value, group in itertools.groupby(self._start)]
        length = math.factorial(len(self._start))
        for repeat in repeats:
            length /= math.factorial(repeat)

        return int(length)

    def __iter__(self):
        """Iterate over permutations.

        See: "Generation in lexicographic order" algorithm described in `the Wikipedia
        article on "Permutation" <https://en.wikipedia.org/wiki/Permutation>`_.
        """
        current = list(self._start)
        size = len(current)

        while True:
            yield tuple(current)

            # 1. Find the largest index i such that a[i] < a[i + 1].
            for i in range(size - 2, -1, -1):
                if current[i] < current[i + 1]:
                    break

            else:
                # If no such index exists, the permutation is the last permutation.
                return

            # 2. Find the largest index j greater than i such that a[i] < a[j].
            for j in range(size - 1, i, -1):
                if current[i] < current[j]:
                    break

            else:  # pragma: NO COVER
                raise RuntimeError("Broken algorithm")

            # 3. Swap the value of a[i] with that of a[j].
            temp = current[i]
            current[i] = current[j]
            current[j] = temp

            # 4. Reverse the sequence from a[i + 1] up to and including the final
            # element a[n].
            current = current[: i + 1] + list(reversed(current[i + 1 :]))
