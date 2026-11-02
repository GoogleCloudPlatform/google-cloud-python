# Copyright 2023 Google LLC
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

import sys
import types
from unittest import mock

import packaging.version
import pytest

try:
    import pyarrow  # type: ignore
except ImportError:
    pyarrow = None

try:
    from google.cloud import bigquery_storage  # type: ignore
except ImportError:
    bigquery_storage = None

try:
    import pandas  # type: ignore
except ImportError:
    pandas = None

from google import cloud
from google.cloud.bigquery import _versions_helpers, exceptions


@pytest.mark.skipif(pyarrow is None, reason="pyarrow is not installed")
def test_try_import_raises_no_error_w_recent_pyarrow():
    versions = _versions_helpers.PyarrowVersions()
    with mock.patch("pyarrow.__version__", new="5.0.0"):
        pyarrow = versions.try_import(raise_if_error=True)
        assert pyarrow is not None


@pytest.mark.skipif(pyarrow is None, reason="pyarrow is not installed")
def test_try_import_returns_none_w_legacy_pyarrow():
    versions = _versions_helpers.PyarrowVersions()
    with mock.patch("pyarrow.__version__", new="2.0.0"):
        pyarrow = versions.try_import()
        assert pyarrow is None


@pytest.mark.skipif(pyarrow is None, reason="pyarrow is not installed")
def test_try_import_raises_error_w_legacy_pyarrow():
    versions = _versions_helpers.PyarrowVersions()
    with mock.patch("pyarrow.__version__", new="2.0.0"):
        with pytest.raises(exceptions.LegacyPyarrowError):
            versions.try_import(raise_if_error=True)


def test_try_import_raises_error_w_no_pyarrow():
    versions = _versions_helpers.PyarrowVersions()
    with mock.patch.dict(sys.modules, {"pyarrow": None}):
        assert versions.try_import(raise_if_error=False) is None
        with pytest.raises(exceptions.LegacyPyarrowError):
            versions.try_import(raise_if_error=True)


@pytest.mark.skipif(pyarrow is None, reason="pyarrow is not installed")
def test_installed_pyarrow_version_returns_cached():
    versions = _versions_helpers.PyarrowVersions()
    versions._installed_version = object()

    assert versions.installed_version is versions._installed_version


@pytest.mark.skipif(pyarrow is None, reason="pyarrow is not installed")
def test_installed_pyarrow_version_returns_parsed_version():
    versions = _versions_helpers.PyarrowVersions()
    with mock.patch("pyarrow.__version__", new="1.2.3"):
        version = versions.installed_version

    assert version.major == 1
    assert version.minor == 2
    assert version.micro == 3


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_raises_no_error_w_recent_bqstorage():
    with mock.patch("google.cloud.bigquery_storage.__version__", new="2.0.0"):
        try:
            bqstorage_versions = _versions_helpers.BQStorageVersions()
            bqstorage_versions.try_import(raise_if_error=True)
        except exceptions.LegacyBigQueryStorageError:  # pragma: NO COVER
            raise ("Legacy error raised with a non-legacy dependency version.")


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_raises_error_w_legacy_bqstorage():
    with mock.patch("google.cloud.bigquery_storage.__version__", new="1.9.9"):
        with pytest.raises(exceptions.LegacyBigQueryStorageError):
            bqstorage_versions = _versions_helpers.BQStorageVersions()
            bqstorage_versions.try_import(raise_if_error=True)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_returns_none_with_legacy_bqstorage():
    with mock.patch("google.cloud.bigquery_storage.__version__", new="1.9.9"):
        try:
            bqstorage_versions = _versions_helpers.BQStorageVersions()
            bq_storage = bqstorage_versions.try_import()
        except exceptions.LegacyBigQueryStorageError:  # pragma: NO COVER
            raise ("Legacy error raised when raise_if_error == False.")
        assert bq_storage is None


def test_returns_none_with_bqstorage_uninstalled():
    versions = _versions_helpers.BQStorageVersions()
    with (
        mock.patch.dict(sys.modules, {"google.cloud.bigquery_storage": None}),
        mock.patch.dict(cloud.__dict__),
    ):
        cloud.__dict__.pop("bigquery_storage", None)

        assert versions.try_import() is None


def test_raises_error_with_bqstorage_uninstalled():
    versions = _versions_helpers.BQStorageVersions()
    with (
        mock.patch.dict(sys.modules, {"google.cloud.bigquery_storage": None}),
        mock.patch.dict(cloud.__dict__),
    ):
        cloud.__dict__.pop("bigquery_storage", None)

        with pytest.raises(exceptions.BigQueryStorageNotFoundError):
            versions.try_import(raise_if_error=True)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_raises_error_w_unknown_bqstorage_version():
    with mock.patch("google.cloud.bigquery_storage", autospec=True) as fake_module:
        del fake_module.__version__
        error_pattern = r"version found: 0.0.0"
        with pytest.raises(exceptions.LegacyBigQueryStorageError, match=error_pattern):
            bqstorage_versions = _versions_helpers.BQStorageVersions()
            bqstorage_versions.try_import(raise_if_error=True)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_installed_bqstorage_version_returns_cached():
    bqstorage_versions = _versions_helpers.BQStorageVersions()
    bqstorage_versions._installed_version = object()

    assert bqstorage_versions.installed_version is bqstorage_versions._installed_version


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_installed_bqstorage_version_returns_parsed_version():
    bqstorage_versions = _versions_helpers.BQStorageVersions()
    with mock.patch("google.cloud.bigquery_storage.__version__", new="1.2.3"):
        bqstorage_versions = bqstorage_versions.installed_version

    assert bqstorage_versions.major == 1
    assert bqstorage_versions.minor == 2
    assert bqstorage_versions.micro == 3


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bqstorage_is_read_session_optional_true():
    bqstorage_versions = _versions_helpers.BQStorageVersions()
    with mock.patch("google.cloud.bigquery_storage.__version__", new="2.6.0"):
        assert bqstorage_versions.is_read_session_optional


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bqstorage_is_read_session_optional_false():
    bqstorage_versions = _versions_helpers.BQStorageVersions()
    with mock.patch("google.cloud.bigquery_storage.__version__", new="2.5.0"):
        assert not bqstorage_versions.is_read_session_optional


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bqstorage_supports_arrow_serialization_options_true():
    from google.cloud.bigquery_storage_v1 import reader

    bqstorage_versions = _versions_helpers.BQStorageVersions()
    with mock.patch.object(reader.ReadRowsStream, "cancel", create=True):
        assert bqstorage_versions.supports_arrow_serialization_options


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bqstorage_supports_arrow_serialization_options_false():
    from google.cloud.bigquery_storage_v1 import reader

    class ReadRowsStream:
        """Stands in for a ReadRowsStream from before cancel() was added."""

    bqstorage_versions = _versions_helpers.BQStorageVersions()
    with mock.patch.object(reader, "ReadRowsStream", ReadRowsStream):
        assert not bqstorage_versions.supports_arrow_serialization_options


@pytest.mark.skipif(pandas is None, reason="pandas is not installed")
@pytest.mark.parametrize("version", ["1.1.5", "2.0.0", "2.1.0"])
def test_try_import_raises_no_error_w_recent_pandas(version):
    # Comparing against the minimum allowed pandas version.
    # As long as the installed version is greater than that, no
    # error is raised.
    versions = _versions_helpers.PandasVersions()
    with mock.patch("pandas.__version__", new=version):
        try:
            pandas = versions.try_import(raise_if_error=True)
            assert pandas is not None
        # this exception should not fire unless there is something broken
        # hence the pragma.
        except exceptions.LegacyPandasError:  # pragma: no cover
            raise ("Legacy error raised with a non-legacy dependency version.")


@pytest.mark.skipif(pandas is None, reason="pandas is not installed")
def test_try_import_returns_none_w_legacy_pandas():
    versions = _versions_helpers.PandasVersions()
    with mock.patch("pandas.__version__", new="1.0.0"):
        pandas = versions.try_import()
        assert pandas is None


@pytest.mark.skipif(pandas is None, reason="pandas is not installed")
def test_try_import_raises_error_w_legacy_pandas():
    versions = _versions_helpers.PandasVersions()
    with mock.patch("pandas.__version__", new="1.0.0"):
        with pytest.raises(exceptions.LegacyPandasError):
            versions.try_import(raise_if_error=True)


def test_try_import_raises_error_w_no_pandas():
    versions = _versions_helpers.PandasVersions()
    with mock.patch.dict(sys.modules, {"pandas": None}):
        assert versions.try_import(raise_if_error=False) is None
        with pytest.raises(exceptions.LegacyPandasError):
            versions.try_import(raise_if_error=True)


@pytest.mark.skipif(pandas is None, reason="pandas is not installed")
def test_installed_pandas_version_returns_cached():
    versions = _versions_helpers.PandasVersions()
    versions._installed_version = object()

    assert versions.installed_version is versions._installed_version


@pytest.mark.skipif(pandas is None, reason="pandas is not installed")
def test_installed_pandas_version_returns_parsed_version():
    versions = _versions_helpers.PandasVersions()
    with mock.patch("pandas.__version__", new="1.1.0"):
        version = versions.installed_version

    assert version.major == 1
    assert version.minor == 1
    assert version.micro == 0


def test_installed_pandas_gbq_version_returns_cached():
    versions = _versions_helpers.PandasGBQVersions()
    versions._installed_version = object()

    assert versions.installed_version is versions._installed_version


def test_installed_pandas_gbq_version_returns_parsed_version():
    mock_pandas_gbq = mock.Mock()
    mock_pandas_gbq.__version__ = "1.2.3"
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": mock_pandas_gbq}):
        version = versions.installed_version

    assert version.major == 1
    assert version.minor == 2
    assert version.micro == 3


def test_installed_pandas_gbq_version_falls_back_on_import_error():
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": None}):
        version = versions.installed_version

    assert version.major == 0
    assert version.minor == 0
    assert version.micro == 0


def test_installed_pandas_gbq_version_falls_back_on_missing_version_attribute():
    mock_pandas_gbq = types.ModuleType("pandas_gbq")
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": mock_pandas_gbq}):
        version = versions.installed_version

    assert version.major == 0
    assert version.minor == 0
    assert version.micro == 0


def test_installed_pandas_gbq_version_falls_back_on_other_error():
    class CorruptPandasGBQ:
        @property
        def __version__(self):
            raise TypeError("Corrupted package")

    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": CorruptPandasGBQ()}):
        version = versions.installed_version

    assert version.major == 0
    assert version.minor == 0
    assert version.micro == 0


def test_pandas_gbq_delegation_api_version_returns_cached():
    versions = _versions_helpers.PandasGBQVersions()
    versions._delegation_api_version = object()

    assert versions.delegation_api_version is versions._delegation_api_version


def test_pandas_gbq_delegation_api_version_returns_value():
    mock_pandas_gbq = mock.Mock()
    mock_pandas_gbq._internal_delegation_api_version = "1.2.3"
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": mock_pandas_gbq}):
        version = versions.delegation_api_version

    assert version.major == 1
    assert version.minor == 2
    assert version.micro == 3


def test_pandas_gbq_delegation_api_version_supports_integer_value():
    mock_pandas_gbq = mock.Mock()
    mock_pandas_gbq._internal_delegation_api_version = 1
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": mock_pandas_gbq}):
        version = versions.delegation_api_version

    assert version.major == 1
    assert version.minor == 0
    assert version.micro == 0


def test_pandas_gbq_delegation_api_version_falls_back_on_missing_attribute():
    mock_pandas_gbq = types.ModuleType("pandas_gbq")
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": mock_pandas_gbq}):
        version = versions.delegation_api_version

    assert version.major == 0
    assert version.minor == 0
    assert version.micro == 0


def test_pandas_gbq_delegation_api_version_falls_back_on_import_error():
    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": None}):
        version = versions.delegation_api_version

    assert version.major == 0
    assert version.minor == 0
    assert version.micro == 0


def test_pandas_gbq_delegation_api_version_falls_back_on_other_error():
    class CorruptPandasGBQ:
        @property
        def _internal_delegation_api_version(self):
            raise TypeError("Corrupted package")

    versions = _versions_helpers.PandasGBQVersions()
    with mock.patch.dict(sys.modules, {"pandas_gbq": CorruptPandasGBQ()}):
        version = versions.delegation_api_version

    assert version.major == 0
    assert version.minor == 0
    assert version.micro == 0


def test_pandas_gbq_is_delegation_supported_true():
    versions = _versions_helpers.PandasGBQVersions()
    versions._delegation_api_version = packaging.version.Version("1.0.0")

    assert versions.is_delegation_supported is True


def test_pandas_gbq_is_delegation_supported_with_sub_minor_version():
    versions = _versions_helpers.PandasGBQVersions()
    versions._delegation_api_version = packaging.version.Version("1.2.0")

    assert versions.is_delegation_supported is True


def test_pandas_gbq_is_delegation_supported_false():
    versions = _versions_helpers.PandasGBQVersions()
    versions._delegation_api_version = packaging.version.Version("0.9.9")

    assert versions.is_delegation_supported is False
