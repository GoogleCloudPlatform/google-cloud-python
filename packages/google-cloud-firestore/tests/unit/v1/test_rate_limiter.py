# Copyright 2021 Google LLC All rights reserved.
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

import freezegun
import pytest

from google.cloud.firestore_v1 import rate_limiter

# Pick a point in time as the center of our universe for this test run.
# It is okay for this to update every time the tests are run.
fake_now = datetime.datetime.now(tz=datetime.timezone.utc)


def test_rate_limiter_basic():
    """Verifies that if the clock does not advance, the RateLimiter allows 500
    writes before crashing out.
    """
    with freezegun.freeze_time(fake_now):
        # This RateLimiter will never advance.
        ramp = rate_limiter.RateLimiter()
        for _ in range(rate_limiter.default_initial_tokens):
            assert ramp.take_tokens() == 1
        assert ramp.take_tokens() == 0


def test_rate_limiter_with_refill():
    """Verifies that if the clock advances, the RateLimiter allows appropriate
    additional writes.
    """
    with freezegun.freeze_time(fake_now) as frozen_datetime:
        ramp = rate_limiter.RateLimiter()
        ramp._available_tokens = 0
        assert ramp.take_tokens() == 0
        # Advance the clock 0.1 seconds
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                microseconds=100000,
            )
        )
        for _ in range(round(rate_limiter.default_initial_tokens / 10)):
            assert ramp.take_tokens() == 1
        assert ramp.take_tokens() == 0


def test_rate_limiter_phase_length():
    """Verifies that if the clock advances, the RateLimiter allows appropriate
    additional writes.
    """
    with freezegun.freeze_time(fake_now) as frozen_datetime:
        ramp = rate_limiter.RateLimiter()
        assert ramp.take_tokens() == 1
        ramp._available_tokens = 0
        assert ramp.take_tokens() == 0

        # Advance the clock 1 phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length,
                microseconds=1,
            )
        )
        for _ in range(round(rate_limiter.default_initial_tokens * 3 / 2)):
            assert ramp.take_tokens()

        assert ramp.take_tokens() == 0


def test_rate_limiter_idle_phase_length():
    """Verifies that if the clock advances but nothing happens, the RateLimiter
    doesn't ramp up.
    """
    with freezegun.freeze_time(fake_now) as frozen_datetime:
        ramp = rate_limiter.RateLimiter()
        ramp._available_tokens = 0
        assert ramp.take_tokens() == 0

        # Advance the clock 1 phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length,
                microseconds=1,
            )
        )

        for _ in range(round(rate_limiter.default_initial_tokens)):
            assert ramp.take_tokens() == 1
            assert ramp._maximum_tokens == 500
        assert ramp.take_tokens() == 0


def test_take_batch_size():
    """Verifies that if the clock advances but nothing happens, the RateLimiter
    doesn't ramp up.
    """
    with freezegun.freeze_time(fake_now) as frozen_datetime:
        page_size: int = 20

        ramp = rate_limiter.RateLimiter()
        ramp._available_tokens = 15
        assert ramp.take_tokens(page_size, allow_less=True) == 15

        # Advance the clock 1 phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length,
                microseconds=1,
            )
        )
        ramp._check_phase()
        assert ramp._maximum_tokens == 750

        for _ in range(740 // page_size):
            assert ramp.take_tokens(page_size) == page_size
        assert ramp.take_tokens(page_size, allow_less=True) == 10
        assert ramp.take_tokens(page_size, allow_less=True) == 0


def test_phase_progress():
    with freezegun.freeze_time(fake_now) as frozen_datetime:
        ramp = rate_limiter.RateLimiter()
        assert ramp._phase == 0
        assert ramp._maximum_tokens == 500
        ramp.take_tokens()

        # Advance the clock 1 phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length,
                microseconds=1,
            )
        )
        ramp.take_tokens()
        assert ramp._phase == 1
        assert ramp._maximum_tokens == 750

        # Advance the clock another phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length * 2,
                microseconds=1,
            )
        )

        ramp.take_tokens()
        assert ramp._phase == 2
        assert ramp._maximum_tokens == 1125

        # Advance the clock another ms and the phase should not advance
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length * 2,
                microseconds=2,
            )
        )

        ramp.take_tokens()
        assert ramp._phase == 2
        assert ramp._maximum_tokens == 1125


def test_global_max_tokens():
    with freezegun.freeze_time(fake_now) as frozen_datetime:
        ramp = rate_limiter.RateLimiter(
            global_max_tokens=499,
        )
        assert ramp._phase == 0
        assert ramp._maximum_tokens == 499
        ramp.take_tokens()

        # Advance the clock 1 phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length,
                microseconds=1,
            )
        )
        ramp.take_tokens()
        assert ramp._phase == 1
        assert ramp._maximum_tokens == 499

        # Advance the clock another phase
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length * 2,
                microseconds=1,
            )
        )

        ramp.take_tokens()
        assert ramp._phase == 2
        assert ramp._maximum_tokens == 499

        # Advance the clock another ms and the phase should not advance
        frozen_datetime.move_to(
            fake_now
            + datetime.timedelta(
                seconds=rate_limiter.default_phase_length * 2,
                microseconds=2,
            )
        )

        ramp.take_tokens()
        assert ramp._phase == 2
        assert ramp._maximum_tokens == 499


def test_utcnow():
    with pytest.warns(
        DeprecationWarning,
        match="google.cloud.firestore_v1.rate_limiter.utcnow",
    ):
        now = rate_limiter.utcnow()
    assert isinstance(now, datetime.datetime)


def test_rate_limiter_check_phase_error():
    """
    calling _check_phase with no _start time raises TypeError
    """
    ramp = rate_limiter.RateLimiter(
        global_max_tokens=499,
    )
    with pytest.raises(TypeError):
        ramp._check_phase()


def test_rate_limiter_refill_error():
    """
    calling _refill with no _last_refill raises TypeError
    """
    ramp = rate_limiter.RateLimiter(
        global_max_tokens=499,
    )
    with pytest.raises(TypeError):
        ramp._refill()
