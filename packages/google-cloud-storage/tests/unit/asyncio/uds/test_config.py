# Copyright 2026 Google LLC
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
"""Unit tests for ``google.cloud.storage.asyncio._uds._config``."""

import sys
import types

import pytest

from google.cloud.storage.asyncio._uds import _config


@pytest.fixture
def uds_off(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog"])
    monkeypatch.setattr(sys, "_xoptions", {})
    monkeypatch.delenv(_config.ENV_FORCE, raising=False)
    monkeypatch.delenv(_config.ENV_MODE, raising=False)
    monkeypatch.setenv(_config.ENV_DIRECT_PATH_XDS, "true")
    assert _config.uds_mode() == "off"


def test_check_direct_path_not_enforced_is_noop_when_uds_disabled(uds_off):
    # DirectPath is enforced in every way, but the UDS backend is off.
    assert (
        _config.check_direct_path_not_enforced(
            True, {"api_endpoint": "google-c2p:///storage.googleapis.com"}
        )
        is None
    )


class _Acl(list):
    loaded = True


def _blob(acl=None, retention=None, temporary_hold=None, event_based_hold=None):
    return types.SimpleNamespace(
        acl=acl,
        retention=retention,
        temporary_hold=temporary_hold,
        event_based_hold=event_based_hold,
    )


@pytest.mark.parametrize(
    "blob, expected",
    [
        (None, []),
        (_blob(), []),
        (_blob(acl=_Acl()), []),  # loaded but empty
        (_blob(acl=_Acl([{"entity": "allUsers", "role": "READER"}])), ["acl"]),
        (_blob(retention={"mode": None, "retainUntilTime": None}), []),
        (_blob(retention={"mode": "Unlocked", "retainUntilTime": None}), ["retention"]),
        (
            _blob(temporary_hold=False, event_based_hold=True),
            ["temporary_hold", "event_based_hold"],
        ),
        (
            _blob(
                acl=_Acl([{"entity": "allUsers", "role": "READER"}]),
                retention={"mode": "Locked"},
                temporary_hold=True,
                event_based_hold=False,
            ),
            ["acl", "retention", "temporary_hold", "event_based_hold"],
        ),
    ],
)
def test_unsupported_blob_attrs(blob, expected):
    assert _config.unsupported_blob_attrs(blob) == expected
