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

import warnings
from unittest.mock import patch

import pytest

from google.api_core._python_package_support import (
    PQC_GRPC_WARNING_TEMPLATE,
    DependencyConstraint,
    DependencyVersion,
    check_dependency_versions,
    get_dependency_version,
    parse_version_to_tuple,
    warn_deprecation_for_versions_less_than,
)


@pytest.mark.parametrize("version_string_to_test", ["1.2.3", "1.2.3b1"])
def test_get_dependency_version(mocker, version_string_to_test):
    """Test get_dependency_version."""
    mock_importlib = mocker.patch(
        "importlib.metadata.version", return_value=version_string_to_test
    )
    expected = DependencyVersion(
        parse_version_to_tuple(version_string_to_test), version_string_to_test
    )
    assert get_dependency_version("some-package") == expected
    mock_importlib.assert_called_once_with("some-package")

    # Test package not found
    mock_importlib.side_effect = ImportError
    assert get_dependency_version("not-a-package") == DependencyVersion(None, "--")


@patch("google.api_core._python_package_support._get_distribution_and_import_packages")
@patch("google.api_core._python_package_support.get_dependency_version")
def test_warn_deprecation_for_versions_less_than(mock_get_version, mock_get_packages):
    """Test the deprecation warning logic."""
    # Mock the helper function to return predictable package strings
    mock_get_packages.side_effect = [
        ("dep-package (dep.package)", "dep-package"),
        ("my-package (my.package)", "my-package"),
    ]

    mock_get_version.return_value = DependencyVersion(
        parse_version_to_tuple("1.0.0"), "1.0.0"
    )
    with pytest.warns(FutureWarning) as record:
        warn_deprecation_for_versions_less_than("my.package", "dep.package", "2.0.0")
    assert len(record) == 1
    assert (
        "DEPRECATION: Package my-package (my.package) depends on dep-package (dep.package)"
        in str(record[0].message)
    )

    # Cases where no warning should be issued
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")  # Capture all warnings

        # Case 2: Installed version is equal to required, should not warn.
        mock_get_packages.reset_mock()
        mock_get_version.return_value = DependencyVersion(
            parse_version_to_tuple("2.0.0"), "2.0.0"
        )
        warn_deprecation_for_versions_less_than("my.package", "dep.package", "2.0.0")

        # Case 3: Installed version is greater than required, should not warn.
        mock_get_packages.reset_mock()
        mock_get_version.return_value = DependencyVersion(
            parse_version_to_tuple("3.0.0"), "3.0.0"
        )
        warn_deprecation_for_versions_less_than("my.package", "dep.package", "2.0.0")

        # Case 4: Dependency not found, should not warn.
        mock_get_packages.reset_mock()
        mock_get_version.return_value = DependencyVersion(None, "--")
        warn_deprecation_for_versions_less_than("my.package", "dep.package", "2.0.0")

        # Assert that no warnings were recorded
        assert len(w) == 0

    # Case 5: Custom message template.
    mock_get_packages.reset_mock()
    mock_get_packages.side_effect = [
        ("dep-package (dep.package)", "dep-package"),
        ("my-package (my.package)", "my-package"),
    ]
    mock_get_version.return_value = DependencyVersion(
        parse_version_to_tuple("1.0.0"), "1.0.0"
    )
    template = "Custom warning for {dependency_package} used by {consumer_package}."
    with pytest.warns(FutureWarning) as record:
        warn_deprecation_for_versions_less_than(
            "my.package", "dep.package", "2.0.0", message_template=template
        )
    assert len(record) == 1
    assert (
        "Custom warning for dep-package (dep.package) used by my-package (my.package)."
        in str(record[0].message)
    )

    # Case 6: Recommended version is properly formatted.
    mock_get_packages.reset_mock()
    mock_get_packages.side_effect = [
        ("dep-package (dep.package)", "dep-package"),
        ("my-package (my.package)", "my-package"),
    ]
    mock_get_version.return_value = DependencyVersion(
        parse_version_to_tuple("1.0.0"), "1.0.0"
    )
    with pytest.warns(FutureWarning) as record:
        warn_deprecation_for_versions_less_than(
            "my.package", "dep.package", "2.0.0", recommended_version="3.0.0"
        )
    assert len(record) == 1
    assert "version 2.0.0 or higher (we recommend 3.0.0)." in str(record[0].message)


@patch(
    "google.api_core._python_package_support.warn_deprecation_for_versions_less_than"
)
def test_check_dependency_versions_with_custom_warnings(mock_warn):
    """Test check_dependency_versions with custom warning parameters."""
    custom_warning1 = DependencyConstraint("pkg1", "1.0.0", "2.0.0")
    custom_warning2 = DependencyConstraint("pkg2", "2.0.0", "3.0.0")

    check_dependency_versions("my-consumer", custom_warning1, custom_warning2)

    assert mock_warn.call_count == 2
    mock_warn.assert_any_call(
        "my-consumer",
        "pkg1",
        "1.0.0",
        recommended_version="2.0.0",
        message_template=None,
    )
    mock_warn.assert_any_call(
        "my-consumer",
        "pkg2",
        "2.0.0",
        recommended_version="3.0.0",
        message_template=None,
    )


@patch(
    "google.api_core._python_package_support.warn_deprecation_for_versions_less_than"
)
def test_check_dependency_versions_default(mock_warn):
    """Test check_dependency_versions with default package dependency warnings."""
    check_dependency_versions("my-consumer")

    assert mock_warn.call_count == 2
    mock_warn.assert_any_call(
        "my-consumer",
        "google.protobuf",
        "6.33.5",
        recommended_version="6.x",
        message_template=None,
    )
    mock_warn.assert_any_call(
        "my-consumer",
        "grpcio",
        "1.83.0",
        recommended_version="1.83.x",
        message_template=PQC_GRPC_WARNING_TEMPLATE,
    )
