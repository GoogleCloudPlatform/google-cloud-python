# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Private module for fetching Google BigQuery credentials."""

import logging

logger = logging.getLogger(__name__)


CREDENTIALS_CACHE_DIRNAME = "pandas_gbq"
CREDENTIALS_CACHE_FILENAME = "bigquery_credentials.dat"
SCOPES = ["https://www.googleapis.com/auth/bigquery"]

# The following constants are used for end-user authentication.
# It identifies (via credentials from the pandas-gbq-auth GCP project) the
# application that is requesting permission to access the BigQuery API on
# behalf of a G Suite or Gmail user.
#
# In a web application, the client secret would be kept secret, but this is not
# possible for applications that are installed locally on an end-user's
# machine.
#
# See: https://cloud.google.com/docs/authentication/end-user for details.
CLIENT_ID = "725825577420-unm2gnkiprugilg743tkbig250f4sfsj.apps.googleusercontent.com"
CLIENT_SECRET = "4hqze9yI8fxShls8eJWkeMdJ"


def get_credentials(
    private_key=None,
    project_id=None,
    reauth=False,
    auth_local_webserver=True,
    auth_redirect_uri=None,
    client_id=None,
    client_secret=None,
):
    import pydata_google_auth

    if private_key:
        raise NotImplementedError(
            """The private_key argument is deprecated. Construct a credentials
object, instead, by using the
google.oauth2.service_account.Credentials.from_service_account_file or
google.oauth2.service_account.Credentials.from_service_account_info class
method from the google-auth package."""
        )

    if client_id is None:
        client_id = CLIENT_ID

    if client_secret is None:
        client_secret = CLIENT_SECRET

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
    import pydata_google_auth.cache

    if reauth:
        return pydata_google_auth.cache.WriteOnlyCredentialsCache(
            dirname=CREDENTIALS_CACHE_DIRNAME,
            filename=CREDENTIALS_CACHE_FILENAME,
        )
    return pydata_google_auth.cache.ReadWriteCredentialsCache(
        dirname=CREDENTIALS_CACHE_DIRNAME, filename=CREDENTIALS_CACHE_FILENAME
    )
