# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Private module for fetching Google BigQuery credentials."""

import logging

logger = logging.getLogger(__name__)


CREDENTIALS_CACHE_DIRNAME = "pandas_gbq"
CREDENTIALS_CACHE_FILENAME = "bigquery_credentials.dat"
SCOPES = ["https://www.googleapis.com/auth/bigquery"]


def get_credentials(
    private_key=None,
    project_id=None,
    reauth=False,
    auth_local_webserver=True,
    auth_redirect_uri=None,
    client_id=None,
    client_secret=None,
):
    # pydata-google-auth does not have type hints nor stubs that mypy uses for type checking.
    # Remove this comment and the ignore pragma upon completing:
    # https://github.com/googleapis/google-cloud-python/issues/17045
    import pydata_google_auth  # type: ignore[import-untyped]

    if private_key:
        raise NotImplementedError(
            """The private_key argument is deprecated. Construct a credentials
object, instead, by using the
google.oauth2.service_account.Credentials.from_service_account_file or
google.oauth2.service_account.Credentials.from_service_account_info class
method from the google-auth package."""
        )

    credentials, default_project_id = pydata_google_auth.default(
        SCOPES,
        client_id=client_id,
        client_secret=client_secret,
        credentials_cache=get_credentials_cache(reauth),
        auth_local_webserver=auth_local_webserver,
        redirect_uri=auth_redirect_uri,
    )

    project_id = project_id or default_project_id
    return credentials, project_id


def get_credentials_cache(reauth):
    # pydata-google-auth does not have type hints nor stubs that mypy uses for type checking.
    # Remove this comment and the ignore pragma upon completing:
    # https://github.com/googleapis/google-cloud-python/issues/17045
    import pydata_google_auth.cache  # type: ignore[import-untyped]

    if reauth:
        return pydata_google_auth.cache.WriteOnlyCredentialsCache(
            dirname=CREDENTIALS_CACHE_DIRNAME,
            filename=CREDENTIALS_CACHE_FILENAME,
        )
    return pydata_google_auth.cache.ReadWriteCredentialsCache(
        dirname=CREDENTIALS_CACHE_DIRNAME, filename=CREDENTIALS_CACHE_FILENAME
    )
