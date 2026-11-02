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

import random
import threading
import unittest

from google.cloud.spanner_v1._helpers import AtomicCounter


class TestAtomicCounter(unittest.TestCase):
    def test_initialization(self):
        ac_default = AtomicCounter()
        assert ac_default.value == 0

        ac_1 = AtomicCounter(1)
        assert ac_1.value == 1

        ac_negative_1 = AtomicCounter(-1)
        assert ac_negative_1.value == -1

    def test_increment(self):
        ac = AtomicCounter()
        result_default = ac.increment()
        assert result_default == 1
        assert ac.value == 1

        result_with_value = ac.increment(2)
        assert result_with_value == 3
        assert ac.value == 3
        result_plus_100 = ac.increment(100)
        assert result_plus_100 == 103

    def test_plus_call(self):
        ac = AtomicCounter()
        ac += 1
        assert ac.value == 1

        n = ac + 2
        assert n == 3
        assert ac.value == 1

        n = 200 + ac
        assert n == 201
        assert ac.value == 1

    def test_multiple_threads_incrementing(self):
        ac = AtomicCounter()
        n = 200
        m = 10

        def do_work():
            for i in range(m):
                ac.increment()

        threads = []
        for i in range(n):
            th = threading.Thread(target=do_work)
            threads.append(th)
            th.start()

        random.shuffle(threads)
        for th in threads:
            th.join()
            assert not th.is_alive()

        # Finally the result should be n*m
        assert ac.value == n * m
