# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


class Context(object):
    """Storage for objects to be used throughout a session.

    A Context object is initialized when the ``pandas_gbq`` module is
    imported, and can be found at :attr:`pandas_gbq.context`.
    """

    def __init__(self):
        self._credentials = None
        self._project = None
        # dialect defaults to None so that read_gbq can stop warning if set.
        self._dialect = None

    @property
    def credentials(self):
        """
        Credentials to use for Google APIs.

        These credentials are automatically cached in memory by calls to
        :func:`pandas_gbq.read_gbq` and :func:`pandas_gbq.to_gbq`. To
        manually set the credentials, construct an
        :class:`google.auth.credentials.Credentials` object and set it as
        the context credentials as demonstrated in the example below. See
        `auth docs`_ for more information on obtaining credentials.

        .. _auth docs: http://google-auth.readthedocs.io
            /en/latest/user-guide.html#obtaining-credentials

        Returns
        -------
        google.auth.credentials.Credentials

        Examples
        --------

        Manually setting the context credentials:

        >>> import pandas_gbq
        >>> from google.oauth2 import service_account
        >>> credentials = service_account.Credentials.from_service_account_file(
        ...     '/path/to/key.json',
        ... )
        >>> pandas_gbq.context.credentials = credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

    @property
    def project(self):
        """Default project to use for calls to Google APIs.

        Returns
        -------
        str

        Examples
        --------

        Manually setting the context project:

        >>> import pandas_gbq
        >>> pandas_gbq.context.project = 'my-project'
        """
        return self._project

    @project.setter
    def project(self, value):
        self._project = value

    @property
    def dialect(self):
        """
        Default dialect to use in :func:`pandas_gbq.read_gbq`.

        Allowed values for the BigQuery SQL syntax dialect:

        ``'legacy'``
            Use BigQuery's legacy SQL dialect. For more information see
            `BigQuery Legacy SQL Reference
            <https://cloud.google.com/bigquery/docs/reference/legacy-sql>`__.
        ``'standard'``
            Use BigQuery's standard SQL, which is
            compliant with the SQL 2011 standard. For more information
            see `BigQuery Standard SQL Reference
            <https://cloud.google.com/bigquery/docs/reference/standard-sql/>`__.

        Returns
        -------
        str

        Examples
        --------

        Setting the default syntax to standard:

        >>> import pandas_gbq
        >>> pandas_gbq.context.dialect = 'standard'
        """
        return self._dialect

    @dialect.setter
    def dialect(self, value):
        self._dialect = value


# Create an empty context, used to cache credentials.
context = Context()
"""A :class:`pandas_gbq.Context` object used to cache credentials.

Credentials automatically are cached in-memory by :func:`pandas_gbq.read_gbq`
and :func:`pandas_gbq.to_gbq`.
"""
