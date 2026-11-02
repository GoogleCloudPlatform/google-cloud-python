# Copyright 2021 Google LLC
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
import re

import pytest  # type: ignore

import test_utils.prefixer


class FakeDateTime(object):
    """Fake datetime class since pytest can't monkeypatch attributes of
    built-in/extension type.
    """

    def __init__(self, fake_now):
        self._fake_now = fake_now

    def now(self, timezone):
        return self._fake_now

    strptime = datetime.datetime.strptime


@pytest.mark.parametrize(
    ("repo", "relative_dir", "separator", "expected"),
    [
        (
            "python-bigquery",
            "samples/snippets",
            "_",
            "python_bigquery_samples_snippets",
        ),
        ("python-storage", "samples\\snippets", "-", "python-storage-samples-snippets"),
    ],
)
def test_common_prefix(repo, relative_dir, separator, expected):
    got = test_utils.prefixer._common_prefix(repo, relative_dir, separator=separator)
    assert got == expected


def test_create_prefix(monkeypatch):
    fake_datetime = FakeDateTime(datetime.datetime(2021, 6, 21, 3, 32, 0))
    monkeypatch.setattr(datetime, "datetime", fake_datetime)

    prefixer = test_utils.prefixer.Prefixer(
        "python-test-utils", "tests/unit", separator="?"
    )
    got = prefixer.create_prefix()
    parts = got.split("?")
    assert len(parts) == 7
    assert "?".join(parts[:5]) == "python?test?utils?tests?unit"
    datetime_part = parts[5]
    assert datetime_part == "20210621033200"
    random_hex_part = parts[6]
    assert re.fullmatch("[0-9a-f]+", random_hex_part)


@pytest.mark.parametrize(
    ("resource_name", "separator", "expected"),
    [
        ("test_utils_created_elsewhere", "_", False),
        ("test_utils_20210620120000", "_", False),
        ("test_utils_20210620120000_abcdef_my_name", "_", False),
        ("test_utils_20210619120000", "_", True),
        ("test_utils_20210619120000_abcdef_my_name", "_", True),
        ("test?utils?created?elsewhere", "_", False),
        ("test?utils?20210620120000", "?", False),
        ("test?utils?20210619120000", "?", True),
    ],
)
def test_should_cleanup(resource_name, separator, expected, monkeypatch):
    fake_datetime = FakeDateTime(datetime.datetime(2021, 6, 21, 3, 32, 0))
    monkeypatch.setattr(datetime, "datetime", fake_datetime)

    prefixer = test_utils.prefixer.Prefixer("test", "utils", separator=separator)
    assert prefixer.should_cleanup(resource_name) == expected
