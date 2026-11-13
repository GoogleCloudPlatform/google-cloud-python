# Copyright 2021 The sqlalchemy-bigquery Authors
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import base64
import functools
import json
import re
from typing import Optional

import google.auth
import sqlalchemy
from google.api_core import client_info
from google.cloud import bigquery
from google.oauth2 import service_account

USER_AGENT_TEMPLATE = "sqlalchemy/{}"
SCOPES = (
    "https://www.googleapis.com/auth/bigquery",
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
)


def google_client_info(
    user_agent: Optional[str] = None,
) -> google.api_core.client_info.ClientInfo:
    """
    Return a client_info object, with an optional user agent
    string.  If user_agent is None, use a default value.
    """

    if user_agent is None:
        user_agent = USER_AGENT_TEMPLATE.format(sqlalchemy.__version__)
    return client_info.ClientInfo(user_agent=user_agent)


def create_bigquery_client(
    credentials_info: Optional[dict] = None,
    credentials_path: Optional[str] = None,
    credentials_base64: Optional[str] = None,
    default_query_job_config: Optional[google.cloud.bigquery.job.QueryJobConfig] = None,
    location: Optional[str] = None,
    project_id: Optional[str] = None,
    user_agent: Optional[google.api_core.client_info.ClientInfo] = None,
) -> google.cloud.bigquery.Client:
    """Construct a BigQuery client object.

    Args:
        credentials_info Optional[dict]:
        credentials_path Optional[str]:
        credentials_base64 Optional[str]:
        default_query_job_config (Optional[google.cloud.bigquery.job.QueryJobConfig]):
            Default ``QueryJobConfig``.
            Will be merged into job configs passed into the ``query`` method.
        location (Optional[str]):
            Default location for jobs / datasets / tables.
        project_id (Optional[str]):
            Project ID for the project which the client acts on behalf of.
        user_agent (Optional[google.api_core.client_info.ClientInfo]):
            The client info used to send a user-agent string along with API
            requests. If ``None``, then default info will be used. Generally,
            you only need to set this if you're developing your own library
            or partner tool.
    """

    default_project = None

    if credentials_base64:
        credentials_info = json.loads(base64.b64decode(credentials_base64))

    if credentials_path:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path
        )
        credentials = credentials.with_scopes(SCOPES)
        default_project = credentials.project_id
    elif credentials_info:
        credentials = service_account.Credentials.from_service_account_info(
            credentials_info
        )
        credentials = credentials.with_scopes(SCOPES)
        default_project = credentials.project_id
    else:
        credentials, default_project = google.auth.default(scopes=SCOPES)

    if project_id is None:
        project_id = default_project

    client_info = google_client_info(user_agent=user_agent)

    return bigquery.Client(
        client_info=client_info,
        project=project_id,
        credentials=credentials,
        location=location,
        default_query_job_config=default_query_job_config,
    )


def substitute_re_method(r, flags=0, repl=None):
    if repl is None:
        return lambda f: substitute_re_method(r, flags, f)

    r = re.compile(r, flags)

    @functools.wraps(repl)
    def sub(self, s, *args, **kw):
        def repl_(m):
            return repl(self, m, *args, **kw)

        return r.sub(repl_, s)

    return sub


def substitute_string_re_method(r, *, repl, flags=0):
    r = re.compile(r, flags)
    return lambda self, s: r.sub(repl, s)
