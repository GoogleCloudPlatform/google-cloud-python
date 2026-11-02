# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Module for checking dependency versions and supported features."""

# https://github.com/googleapis/python-bigquery/blob/main/CHANGELOG.md
BIGQUERY_MINIMUM_VERSION = "3.4.2"
BIGQUERY_QUERY_AND_WAIT_VERSION = "3.14.0"
PANDAS_VERBOSITY_DEPRECATION_VERSION = "0.23.0"
PANDAS_BOOLEAN_DTYPE_VERSION = "1.0.0"


class Features:
    def __init__(self):
        self._bigquery_installed_version = None
        self._pandas_installed_version = None

    @property
    def bigquery_installed_version(self):
        import google.cloud.bigquery
        import packaging.version

        if self._bigquery_installed_version is not None:
            return self._bigquery_installed_version

        self._bigquery_installed_version = packaging.version.parse(
            google.cloud.bigquery.__version__
        )
        return self._bigquery_installed_version

    def bigquery_try_import(self):
        import google.cloud.bigquery
        import packaging.version

        bigquery_minimum_version = packaging.version.parse(BIGQUERY_MINIMUM_VERSION)

        if self.bigquery_installed_version < bigquery_minimum_version:
            raise ImportError(
                "pandas-gbq requires google-cloud-bigquery >= {0}, "
                "current version {1}".format(
                    bigquery_minimum_version, self._bigquery_installed_version
                )
            )

        return google.cloud.bigquery

    @property
    def bigquery_has_query_and_wait(self):
        import packaging.version

        min_version = packaging.version.parse(BIGQUERY_QUERY_AND_WAIT_VERSION)
        return self.bigquery_installed_version >= min_version

    @property
    def pandas_installed_version(self):
        import packaging.version
        import pandas

        if self._pandas_installed_version is not None:
            return self._pandas_installed_version

        self._pandas_installed_version = packaging.version.parse(pandas.__version__)
        return self._pandas_installed_version

    @property
    def pandas_has_deprecated_verbose(self):
        import packaging.version

        # Add check for Pandas version before showing deprecation warning.
        # https://github.com/pydata/pandas-gbq/issues/157
        pandas_verbosity_deprecation = packaging.version.parse(
            PANDAS_VERBOSITY_DEPRECATION_VERSION
        )
        return self.pandas_installed_version >= pandas_verbosity_deprecation

    @property
    def pandas_has_boolean_dtype(self):
        import packaging.version

        desired_version = packaging.version.parse(PANDAS_BOOLEAN_DTYPE_VERSION)
        return self.pandas_installed_version >= desired_version


FEATURES = Features()
