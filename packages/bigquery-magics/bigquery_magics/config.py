# Copyright 2018 Google LLC
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
from dataclasses import dataclass
from typing import Optional

import google.api_core.client_options as client_options
import google.cloud.bigquery as bigquery
import pydata_google_auth

_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]


def _get_default_credentials_with_project():
    return pydata_google_auth.default(scopes=_SCOPES, use_local_webserver=False)


@dataclass
class Context(object):
    """Storage for objects to be used throughout an IPython notebook session.

    A Context object is initialized when the ``bigquery_magics`` module is imported,
    and can be found at ``bigquery_magics.context``.
    """

    _connection = None

    default_query_job_config = bigquery.QueryJobConfig()
    """google.cloud.bigquery.job.QueryJobConfig: Default job
        configuration for queries.

        The context's :class:`~google.cloud.bigquery.job.QueryJobConfig` is
        used for queries. Some properties can be overridden with arguments to
        the magics.

        Example:
            Manually setting the default value for ``maximum_bytes_billed``
            to 100 MB:

            >>> from google.cloud.bigquery import magics
            >>> bigquery_magics.context.default_query_job_config.maximum_bytes_billed = 100000000
    """

    bigquery_client_options = client_options.ClientOptions()
    """google.api_core.client_options.ClientOptions: client options to be
        used through IPython magics.

        Note::
            The client options do not need to be explicitly defined if no
            special network connections are required. Normally you would be
            using the https://bigquery.googleapis.com/ end point.

        Example:
            Manually setting the endpoint:

            >>> from google.cloud.bigquery import magics
            >>> client_options = {}
            >>> client_options['api_endpoint'] = "https://some.special.url"
            >>> bigquery_magics.context.bigquery_client_options = client_options
    """

    bqstorage_client_options = client_options.ClientOptions()
    """google.api_core.client_options.ClientOptions: client options to be
        used through IPython magics for the storage client.

        Note::
            The client options do not need to be explicitly defined if no
            special network connections are required. Normally you would be
            using the https://bigquerystorage.googleapis.com/ end point.

        Example:
            Manually setting the endpoint:

            >>> from google.cloud.bigquery import magics
            >>> client_options = {}
            >>> client_options['api_endpoint'] = "https://some.special.url"
            >>> bigquery_magics.context.bqstorage_client_options = client_options
    """

    progress_bar_type = "tqdm_notebook"
    """str: Default progress bar type to use to display progress bar while
        executing queries through IPython magics.

        Note::
            Install the ``tqdm`` package to use this feature.

        Example:
            Manually setting the progress_bar_type:

            >>> from google.cloud.bigquery import magics
            >>> bigquery_magics.context.progress_bar_type = "tqdm_notebook"
    """

    _credentials = None

    @property
    def credentials(self):
        """google.auth.credentials.Credentials: Credentials to use for queries
        performed through IPython magics.

        Note:
            These credentials do not need to be explicitly defined if you are
            using Application Default Credentials. If you are not using
            Application Default Credentials, manually construct a
            :class:`google.auth.credentials.Credentials` object and set it as
            the context credentials as demonstrated in the example below. See
            `auth docs`_ for more information on obtaining credentials.

        Example:
            Manually setting the context credentials:

            >>> from google.cloud.bigquery import magics
            >>> from google.oauth2 import service_account
            >>> credentials = (service_account
            ...     .Credentials.from_service_account_file(
            ...         '/path/to/key.json'))
            >>> bigquery_magics.context.credentials = credentials


        .. _auth docs: http://google-auth.readthedocs.io
            /en/latest/user-guide.html#obtaining-credentials
        """
        if self._credentials is None:
            self._credentials, _ = _get_default_credentials_with_project()
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

    _default_variable: Optional[str] = None

    @property
    def default_variable(self) -> Optional[str]:
        """Optional[str]: If set, the variable name to use for the DataFrame
        returned from running the query.
        """
        return self._default_variable

    @default_variable.setter
    def default_variable(self, value: Optional[str]):
        self._default_variable = value

    _project = None

    @property
    def project(self):
        """str: Default project to use for queries performed through IPython
        magics.

        Note:
            The project does not need to be explicitly defined if you have an
            environment default project set. If you do not have a default
            project set in your environment, manually assign the project as
            demonstrated in the example below.

        Example:
            Manually setting the context project:

            >>> from google.cloud.bigquery import magics
            >>> bigquery_magics.context.project = 'my-project'
        """
        if self._project is None:
            _, self._project = _get_default_credentials_with_project()
        return self._project

    @project.setter
    def project(self, value):
        self._project = value

    _engine = "pandas"

    @property
    def engine(self) -> str:
        """[Deprecated] Engine to run the query. Could either be "pandas" or
        "bigframes".

        If using "pandas", the query result will be stored in a Pandas dataframe.
        If using "bigframes", the query result will be stored in a bigframes
        dataframe instead.

        Please use ``%load_ext bigframes`` and the ``%%bqsql`` magic instead.
        See: https://dataframes.bigquery.dev/notebooks/getting_started/magics.html

        Example:
            Manully setting the content engine:

            >>> from google.cloud.bigquery import magics
            >>> bigquery_magics.context.engine = 'bigframes'
        """
        return self._engine

    @engine.setter
    def engine(self, value):
        if value != "pandas" and value != "bigframes":
            raise ValueError("engine must be either 'pandas' or 'bigframes'")
        if value == "bigframes":
            warnings.warn(
                "The bigframes engine is deprecated. Please use %load_ext bigframes "
                "and the %%bqsql magic instead. "
                "See: https://dataframes.bigquery.dev/notebooks/getting_started/magics.html",
                FutureWarning,
                stacklevel=2,
            )
        self._engine = value


context = Context()
