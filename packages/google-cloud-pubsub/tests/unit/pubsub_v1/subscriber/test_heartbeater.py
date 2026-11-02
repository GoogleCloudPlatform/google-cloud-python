# Copyright 2018, Google LLC
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

import logging
import threading
from unittest import mock

import pytest

from google.cloud.pubsub_v1.subscriber._protocol import (
    heartbeater,
    streaming_pull_manager,
)


def test_heartbeat_inactive_manager_active_rpc(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    manager.is_active = False
    manager.heartbeat.return_value = True  # because of active rpc

    heartbeater_ = heartbeater.Heartbeater(manager)
    make_sleep_mark_event_as_done(heartbeater_)

    heartbeater_.heartbeat()

    assert "Sent heartbeat" in caplog.text
    assert "exiting" in caplog.text


def test_heartbeat_inactive_manager_inactive_rpc(
    caplog,
    modify_google_logger_propagation,
):
    caplog.set_level(logging.DEBUG)

    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    manager.is_active = False
    manager.heartbeat.return_value = False  # because of inactive rpc

    heartbeater_ = heartbeater.Heartbeater(manager)
    make_sleep_mark_event_as_done(heartbeater_)

    heartbeater_.heartbeat()

    assert "Sent heartbeat" not in caplog.text
    assert "exiting" in caplog.text


def test_heartbeat_stopped(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )

    heartbeater_ = heartbeater.Heartbeater(manager)
    heartbeater_.stop()

    heartbeater_.heartbeat()

    assert "Sent heartbeat" not in caplog.text
    assert "exiting" in caplog.text


def make_sleep_mark_event_as_done(heartbeater):
    # Make sleep actually trigger the done event so that heartbeat()
    # exits at the end of the first run.
    def trigger_done(timeout):
        assert timeout
        heartbeater._stop_event.set()

    heartbeater._stop_event.wait = trigger_done


def test_heartbeat_once():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    heartbeater_ = heartbeater.Heartbeater(manager)
    make_sleep_mark_event_as_done(heartbeater_)

    heartbeater_.heartbeat()

    manager.heartbeat.assert_called_once()


@mock.patch("threading.Thread", autospec=True)
def test_start(thread):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    heartbeater_ = heartbeater.Heartbeater(manager)

    heartbeater_.start()

    thread.assert_called_once_with(
        name=heartbeater._HEARTBEAT_WORKER_NAME, target=heartbeater_.heartbeat
    )

    thread.return_value.start.assert_called_once()

    assert heartbeater_._thread is not None


@mock.patch("threading.Thread", autospec=True)
def test_start_already_started(thread):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    heartbeater_ = heartbeater.Heartbeater(manager)
    heartbeater_._thread = mock.sentinel.thread

    with pytest.raises(ValueError):
        heartbeater_.start()

    thread.assert_not_called()


def test_stop():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    heartbeater_ = heartbeater.Heartbeater(manager)
    thread = mock.create_autospec(threading.Thread, instance=True)
    heartbeater_._thread = thread

    heartbeater_.stop()

    assert heartbeater_._stop_event.is_set()
    thread.join.assert_called_once()
    assert heartbeater_._thread is None


def test_stop_no_join():
    heartbeater_ = heartbeater.Heartbeater(mock.sentinel.manager)

    heartbeater_.stop()
