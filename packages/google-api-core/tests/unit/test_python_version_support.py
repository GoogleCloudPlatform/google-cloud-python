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

import datetime
import textwrap
import warnings
from collections import namedtuple
from unittest.mock import patch

import pytest

# Code to be tested
from google.api_core._python_version_support import (
    DEPRECATION_WARNING_PERIOD,
    PYTHON_VERSION_INFO,
    PythonVersionStatus,
    _flatten_message,
    _get_distribution_and_import_packages,
    _get_pypi_package_name,
    check_python_version,
)

# Helper object for mocking sys.version_info
VersionInfoMock = namedtuple("VersionInfoMock", ["major", "minor"])


def test_flatten_message():
    """Test that _flatten_message correctly dedents and flattens a string."""
    input_text = """
        This is a multi-line
        string with some
            indentation.
    """
    expected_output = "This is a multi-line string with some indentation."
    assert _flatten_message(input_text) == expected_output


def _create_failure_message(
    expected, result, py_version, date, gapic_dep, py_eol, eol_warn, gapic_end
):
    """Create a detailed failure message for a test."""
    return textwrap.dedent(  # pragma: NO COVER
        f"""
        --- Test Failed ---
        Expected status: {expected.name}
        Received status: {result.name}
        ---------------------
        Context:
          - Mocked Python Version: {py_version}
          - Mocked Today's Date:   {date}
        Calculated Dates:
          - gapic_deprecation:     {gapic_dep}
          - python_eol:            {py_eol}
          - eol_warning_starts:    {eol_warn}
          - gapic_end:             {gapic_end}
        """
    )


def get_tracked_version_test_cases():
    """
    Returns a list of test parameters for all tracked versions and boundary conditions.
    """
    results = []

    for version_tuple, version_info in PYTHON_VERSION_INFO.items():
        py_version_str = f"{version_tuple[0]}.{version_tuple[1]}"
        gapic_dep = version_info.gapic_deprecation or (
            version_info.python_eol - DEPRECATION_WARNING_PERIOD
        )
        gapic_end = version_info.gapic_end or (
            version_info.python_eol + datetime.timedelta(weeks=1)
        )
        eol_warning_starts = version_info.python_eol + datetime.timedelta(weeks=1)

        test_cases = {
            "supported_before_deprecation_date": {
                "date": gapic_dep - datetime.timedelta(days=1),
                "expected": PythonVersionStatus.PYTHON_VERSION_SUPPORTED,
            },
            "deprecated_on_deprecation_date": {
                "date": gapic_dep,
                "expected": PythonVersionStatus.PYTHON_VERSION_DEPRECATED,
            },
            "deprecated_on_eol_date": {
                "date": version_info.python_eol,
                "expected": PythonVersionStatus.PYTHON_VERSION_DEPRECATED,
            },
            "deprecated_before_eol_warning_starts": {
                "date": eol_warning_starts - datetime.timedelta(days=1),
                "expected": PythonVersionStatus.PYTHON_VERSION_DEPRECATED,
            },
            "eol_on_eol_warning_date": {
                "date": eol_warning_starts,
                "expected": PythonVersionStatus.PYTHON_VERSION_EOL,
            },
            "eol_on_gapic_end_date": {
                "date": gapic_end,
                "expected": PythonVersionStatus.PYTHON_VERSION_EOL,
            },
            "unsupported_after_gapic_end_date": {
                "date": gapic_end + datetime.timedelta(days=1),
                "expected": PythonVersionStatus.PYTHON_VERSION_UNSUPPORTED,
            },
        }

        for name, params in test_cases.items():
            results.append(
                pytest.param(
                    version_tuple,
                    params["date"],
                    params["expected"],
                    gapic_dep,
                    gapic_end,
                    eol_warning_starts,
                    id=f"{py_version_str}-{name}",
                )
            )
    return results


@pytest.mark.parametrize(
    "version_tuple, mock_date, expected_status, gapic_dep, gapic_end, eol_warning_starts",
    get_tracked_version_test_cases(),
)
def test_all_tracked_versions_and_date_scenarios(
    version_tuple, mock_date, expected_status, gapic_dep, gapic_end, eol_warning_starts
):
    """Test all outcomes for each tracked version using parametrization."""
    mock_py_v = VersionInfoMock(major=version_tuple[0], minor=version_tuple[1])

    with patch("google.api_core._python_version_support.sys.version_info", mock_py_v):
        # Supported versions should not issue warnings
        if expected_status == PythonVersionStatus.PYTHON_VERSION_SUPPORTED:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                result = check_python_version(today=mock_date)
                assert len(w) == 0
        # All other statuses should issue a warning
        else:
            with pytest.warns(FutureWarning) as record:
                result = check_python_version(today=mock_date)
            assert len(record) == 1

        if result != expected_status:  # pragma: NO COVER
            py_version_str = f"{version_tuple[0]}.{version_tuple[1]}"
            version_info = PYTHON_VERSION_INFO[version_tuple]

            fail_msg = _create_failure_message(
                expected_status,
                result,
                py_version_str,
                mock_date,
                gapic_dep,
                version_info.python_eol,
                eol_warning_starts,
                gapic_end,
            )
            pytest.fail(fail_msg, pytrace=False)


def test_override_gapic_end_only():
    """Test behavior when only gapic_end is manually overridden."""
    version_tuple = (3, 10)
    original_info = PYTHON_VERSION_INFO[version_tuple]
    mock_py_version = VersionInfoMock(major=version_tuple[0], minor=version_tuple[1])

    custom_gapic_end = original_info.python_eol + datetime.timedelta(days=212)
    overridden_info = original_info._replace(gapic_end=custom_gapic_end)

    with patch(
        "google.api_core._python_version_support.sys.version_info", mock_py_version
    ):
        with patch.dict(
            "google.api_core._python_version_support.PYTHON_VERSION_INFO",
            {version_tuple: overridden_info},
        ):
            with pytest.warns(FutureWarning, match="past its end of life"):
                result_before_boundary = check_python_version(
                    today=custom_gapic_end + datetime.timedelta(days=-1)
                )
            assert result_before_boundary == PythonVersionStatus.PYTHON_VERSION_EOL

            with pytest.warns(FutureWarning, match="past its end of life"):
                result_at_boundary = check_python_version(today=custom_gapic_end)
            assert result_at_boundary == PythonVersionStatus.PYTHON_VERSION_EOL

            with pytest.warns(FutureWarning, match="non-supported Python version"):
                result_after_boundary = check_python_version(
                    today=custom_gapic_end + datetime.timedelta(days=1)
                )
            assert (
                result_after_boundary == PythonVersionStatus.PYTHON_VERSION_UNSUPPORTED
            )


def test_override_gapic_deprecation_only():
    """Test behavior when only gapic_deprecation is manually overridden."""
    version_tuple = (3, 10)
    original_info = PYTHON_VERSION_INFO[version_tuple]
    mock_py_version = VersionInfoMock(major=version_tuple[0], minor=version_tuple[1])

    custom_gapic_dep = original_info.python_eol - datetime.timedelta(days=120)
    overridden_info = original_info._replace(gapic_deprecation=custom_gapic_dep)

    with patch(
        "google.api_core._python_version_support.sys.version_info", mock_py_version
    ):
        with patch.dict(
            "google.api_core._python_version_support.PYTHON_VERSION_INFO",
            {version_tuple: overridden_info},
        ):
            result_before_boundary = check_python_version(
                today=custom_gapic_dep - datetime.timedelta(days=1)
            )
            assert (
                result_before_boundary == PythonVersionStatus.PYTHON_VERSION_SUPPORTED
            )

            with pytest.warns(FutureWarning, match="Google will stop supporting"):
                result_at_boundary = check_python_version(today=custom_gapic_dep)
            assert result_at_boundary == PythonVersionStatus.PYTHON_VERSION_DEPRECATED


def test_untracked_older_version_is_unsupported():
    """Test that an old, untracked version is unsupported and logs."""
    mock_py_version = VersionInfoMock(major=3, minor=6)

    with patch(
        "google.api_core._python_version_support.sys.version_info", mock_py_version
    ):
        with pytest.warns(FutureWarning) as record:
            mock_date = datetime.date(2025, 1, 15)
            result = check_python_version(today=mock_date)

            assert result == PythonVersionStatus.PYTHON_VERSION_UNSUPPORTED
            assert len(record) == 1
            assert "non-supported" in str(record[0].message)


def test_untracked_newer_version_is_supported():
    """Test that a new, untracked version is supported and does not log."""
    mock_py_version = VersionInfoMock(major=40, minor=0)

    with patch(
        "google.api_core._python_version_support.sys.version_info", mock_py_version
    ):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            mock_date = datetime.date(2025, 1, 15)
            result = check_python_version(today=mock_date)

            assert result == PythonVersionStatus.PYTHON_VERSION_SUPPORTED
            assert len(w) == 0


def test_get_pypi_package_name_is_noop():
    """Test that _get_pypi_package_name returns None without scanning distributions."""
    with patch("importlib.metadata.packages_distributions") as mock_pkg_dists:
        assert _get_pypi_package_name("google.api_core") is None
        assert _get_distribution_and_import_packages("google.api_core") == (
            "google.api_core",
            None,
        )
        # Verify check_python_version never calls packages_distributions() even when warning
        mock_py_v = VersionInfoMock(major=3, minor=11)
        with patch(
            "google.api_core._python_version_support.sys.version_info", mock_py_v
        ):
            # Oct 26, 2026 (incident date): now SUPPORTED with 0 warnings (outside 90-day window)
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                status = check_python_version(
                    "google.cloud.datacatalog_lineage_v1",
                    today=datetime.date(2026, 10, 26),
                )
                assert status == PythonVersionStatus.PYTHON_VERSION_SUPPORTED
                assert len(w) == 0

            # Inside 90-day window: warns, but still never calls packages_distributions()
            with pytest.warns(FutureWarning):
                status = check_python_version(
                    "google.cloud.datacatalog_lineage_v1",
                    today=datetime.date(2027, 8, 1),
                )
                assert status == PythonVersionStatus.PYTHON_VERSION_DEPRECATED

        mock_pkg_dists.assert_not_called()
    assert DEPRECATION_WARNING_PERIOD == datetime.timedelta(days=90)
