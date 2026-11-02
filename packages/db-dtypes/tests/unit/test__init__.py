# Copyright 2025 Google LLC
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

from collections import namedtuple
from unittest import mock

import pytest

# Module paths used for mocking
MODULE_PATH = "db_dtypes"
MOCK_WARN = "warnings.warn"  # Target the standard warnings module

VersionInfo = namedtuple("VersionInfo", ["major", "minor", "micro"])


@pytest.mark.parametrize(
    "mock_version_tuple, version_str",
    [
        ((3, 7, 10), "3.7.10"),
        ((3, 7, 0), "3.7.0"),
        ((3, 8, 5), "3.8.5"),
        ((3, 8, 12), "3.8.12"),
        ((3, 9, 5), "3.9.5"),
    ],
)
def test_check_python_version_warns_on_unsupported(mock_version_tuple, version_str):
    """
    Test that _check_python_version issues a FutureWarning for Python 3.7/3.8/3.9.
    """

    from db_dtypes import _check_python_version

    mock_version = VersionInfo(*mock_version_tuple)

    # Mock sys.version_info and warnings.warn
    with (
        mock.patch("sys.version_info", new=mock_version),
        mock.patch(MOCK_WARN) as mock_warn_call,
    ):
        _check_python_version()  # Call the function

        # Assert that warnings.warn was called exactly once
        mock_warn_call.assert_called_once()

        # Check the arguments passed to warnings.warn
        args, kwargs = mock_warn_call.call_args
        assert len(args) >= 1  # Should have at least the message
        warning_message = args[0]
        warning_category = args[1] if len(args) > 1 else kwargs.get("category")

        # Verify message content and category
        assert "longer supports Python 3.7, 3.8, and 3.9" in warning_message
        assert warning_category == FutureWarning


@pytest.mark.parametrize(
    "mock_version_tuple",
    [
        (3, 10, 0),
        (3, 11, 2),
        (3, 12, 0),
        (3, 13, 0),
        (3, 14, 0),
    ],
)
def test_check_python_version_does_not_warn_on_supported(mock_version_tuple):
    """
    Test that _check_python_version does NOT issue a warning for other versions.
    """

    from db_dtypes import _check_python_version

    mock_version = VersionInfo(*mock_version_tuple)

    # Mock sys.version_info and warnings.warn
    with (
        mock.patch("sys.version_info", new=mock_version),
        mock.patch(MOCK_WARN) as mock_warn_call,
    ):
        _check_python_version()

        # Assert that warnings.warn was NOT called
        mock_warn_call.assert_not_called()
