# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import logging
import time
import typing
import warnings
from typing import Any, Dict, Optional, Union

# Only import at module-level at type checking time to avoid circular
# dependencies in the pandas package, which has an optional dependency on
# pandas-gbq.
if typing.TYPE_CHECKING:  # pragma: NO COVER
    import pandas

import pandas_gbq.constants
import pandas_gbq.core.read
import pandas_gbq.environment as environment
import pandas_gbq.exceptions
import pandas_gbq.query
from pandas_gbq import dry_runs
from pandas_gbq.contexts import context
from pandas_gbq.exceptions import QueryTimeout
from pandas_gbq.features import FEATURES

tqdm: Any = None
try:
    import tqdm  # noqa
except ImportError:
    pass

logger = logging.getLogger(__name__)


class GbqConnector:
    def __init__(
        self,
        project_id,
        reauth=False,
        private_key=None,
        auth_local_webserver=True,
        dialect="standard",
        location=None,
        credentials=None,
        use_bqstorage_api=False,
        auth_redirect_uri=None,
        client_id=None,
        client_secret=None,
        user_agent=None,
        rfc9110_delimiter=False,
        bigquery_client=None,
    ):
        from pandas_gbq import auth

        self.http_error = pandas_gbq.constants.HTTP_ERRORS
        self.project_id = project_id
        self.location = location
        self.reauth = reauth
        self.private_key = private_key
        self.auth_local_webserver = auth_local_webserver
        self.dialect = dialect
        self.credentials = credentials
        self.auth_redirect_uri = auth_redirect_uri
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.rfc9110_delimiter = rfc9110_delimiter
        self.use_bqstorage_api = use_bqstorage_api

        if bigquery_client is not None:
            # If a bq client is already provided, use it to populate auth fields.
            self.project_id = bigquery_client.project
            self.credentials = bigquery_client._credentials
            self.client = bigquery_client
            return

        default_project = None

        # Service account credentials have a project associated with them.
        # Prefer that project if none was supplied.
        if self.project_id is None and hasattr(self.credentials, "project_id"):
            self.project_id = credentials.project_id

        # Load credentials from cache.
        if not self.credentials:
            self.credentials = context.credentials
            default_project = context.project

        # Credentials were explicitly asked for, so don't use the cache.
        if private_key or reauth or not self.credentials:
            self.credentials, default_project = auth.get_credentials(
                private_key=private_key,
                project_id=project_id,
                reauth=reauth,
                auth_local_webserver=auth_local_webserver,
                auth_redirect_uri=auth_redirect_uri,
                client_id=client_id,
                client_secret=client_secret,
            )

        if self.project_id is None:
            self.project_id = default_project

        if self.project_id is None:
            raise ValueError("Could not determine project ID and one was not supplied.")

        # Cache the credentials if they haven't been set yet.
        if context.credentials is None:
            context.credentials = self.credentials
        if context.project is None:
            context.project = self.project_id

        self.client = _get_client(
            self.user_agent, self.rfc9110_delimiter, self.project_id, self.credentials
        )

    def _start_timer(self):
        self.start = time.time()

    def get_elapsed_seconds(self):
        return round(time.time() - self.start, 2)

    def log_elapsed_seconds(self, prefix="Elapsed", postfix="s.", overlong=6):
        sec = self.get_elapsed_seconds()
        if sec > overlong:
            logger.info("{} {} {}".format(prefix, sec, postfix))

    def get_client(self):
        import google.api_core.client_info

        bigquery = FEATURES.bigquery_try_import()

        user_agent = create_user_agent(
            user_agent=self.user_agent, rfc9110_delimiter=self.rfc9110_delimiter
        )

        client_info = google.api_core.client_info.ClientInfo(
            user_agent=user_agent,
        )
        return bigquery.Client(
            project=self.project_id,
            credentials=self.credentials,
            client_info=client_info,
        )

    @staticmethod
    def process_http_error(ex):
        # See `BigQuery Troubleshooting Errors
        # <https://cloud.google.com/bigquery/troubleshooting-errors>`__
        raise pandas_gbq.exceptions.translate_exception(ex) from ex

    def download_table(
        self,
        table_id: str,
        max_results: Optional[int] = None,
        progress_bar_type: Optional[str] = None,
        dtypes: Optional[Dict[str, Union[str, Any]]] = None,
    ) -> Optional[pandas.DataFrame]:
        from google.cloud import bigquery

        self._start_timer()

        try:
            table_ref = bigquery.TableReference.from_string(
                table_id, default_project=self.project_id
            )
            rows_iter = self.client.list_rows(table_ref, max_results=max_results)
        except self.http_error as ex:
            self.process_http_error(ex)

        return self._download_results(
            rows_iter,
            max_results=max_results,
            progress_bar_type=progress_bar_type,
            user_dtypes=dtypes,
        )

    def run_query(
        self,
        query,
        max_results=None,
        progress_bar_type=None,
        dry_run: bool = False,
        **kwargs,
    ):
        from google.cloud import bigquery

        job_config_dict = {
            "query": {
                "useLegacySql": self.dialect
                == "legacy"
                # 'allowLargeResults', 'createDisposition',
                # 'preserveNulls', destinationTable, useQueryCache
            }
        }
        config = kwargs.get("configuration")
        if config is not None:
            job_config_dict.update(config)

        timeout_ms = job_config_dict.get("jobTimeoutMs") or job_config_dict[
            "query"
        ].get("timeoutMs")

        if timeout_ms:
            if not isinstance(timeout_ms, (str, int, float)):
                raise TypeError(f"Expected str, int or float, got {type(timeout_ms)}")
            timeout_ms = int(timeout_ms)
            # Having too small a timeout_ms results in individual
            # API calls timing out before they can finish.
            # ~300 milliseconds is rule of thumb for bare minimum
            # latency from the BigQuery API, however, 400 milliseconds
            # produced too many issues with flakybot failures.
            minimum_latency = 500
            if timeout_ms < minimum_latency:
                raise QueryTimeout(
                    f"Query timeout must be at least 500 milliseconds: timeout_ms equals {timeout_ms}."
                )
        else:
            timeout_ms = None

        self._start_timer()
        job_config = bigquery.QueryJobConfig.from_api_repr(job_config_dict)
        job_config = typing.cast(bigquery.QueryJobConfig, job_config)
        job_config.dry_run = dry_run

        if FEATURES.bigquery_has_query_and_wait:
            rows_iter = pandas_gbq.query.query_and_wait_via_client_library(
                self,
                self.client,
                query,
                location=self.location,
                project_id=self.project_id,
                job_config=job_config,
                max_results=max_results,
                timeout_ms=timeout_ms,
            )
        else:
            rows_iter = pandas_gbq.query.query_and_wait(
                self,
                self.client,
                query,
                location=self.location,
                project_id=self.project_id,
                job_config=job_config,
                max_results=max_results,
                timeout_ms=timeout_ms,
            )

        if dry_run:
            return dry_runs.get_query_stats(rows_iter.job)

        return self._download_results(
            rows_iter,
            max_results=max_results,
            progress_bar_type=progress_bar_type,
            user_dtypes=kwargs.get("dtypes"),
        )

    def _download_results(
        self,
        rows_iter,
        max_results=None,
        progress_bar_type=None,
        user_dtypes=None,
    ):
        return pandas_gbq.core.read.download_results(
            rows_iter,
            bqclient=self.get_client(),
            progress_bar_type=progress_bar_type,
            warn_on_large_results=True,
            max_results=max_results,
            user_dtypes=user_dtypes,
            use_bqstorage_api=self.use_bqstorage_api,
        )

    def load_data(
        self,
        dataframe,
        destination_table_ref,
        write_disposition,
        chunksize=None,
        schema=None,
        progress_bar=True,
        api_method: str = "load_parquet",
        billing_project: Optional[str] = None,
    ):
        from pandas_gbq import load

        total_rows = len(dataframe)

        try:
            chunks = load.load_chunks(
                self.client,
                dataframe,
                destination_table_ref,
                chunksize=chunksize,
                schema=schema,
                location=self.location,
                api_method=api_method,
                write_disposition=write_disposition,
                billing_project=billing_project,
            )
            if progress_bar and tqdm:
                chunks = tqdm.tqdm(chunks)
            for remaining_rows in chunks:
                logger.info(
                    "\r{} out of {} rows loaded.".format(
                        total_rows - remaining_rows, total_rows
                    )
                )
        except self.http_error as ex:
            self.process_http_error(ex)


def _get_client(user_agent, rfc9110_delimiter, project_id, credentials):
    import google.api_core.client_info

    bigquery = FEATURES.bigquery_try_import()

    user_agent = create_user_agent(
        user_agent=user_agent, rfc9110_delimiter=rfc9110_delimiter
    )

    client_info = google.api_core.client_info.ClientInfo(
        user_agent=user_agent,
    )
    return bigquery.Client(
        project=project_id,
        credentials=credentials,
        client_info=client_info,
    )


def create_user_agent(
    user_agent: Optional[str] = None, rfc9110_delimiter: bool = False
) -> str:
    """Creates a user agent string.

    The legacy format of our the user agent string was: `product-x.y.z` (where x,
    y, and z are the major, minor, and micro version numbers).

    Users are able to prepend this string with their own user agent identifier
    to render something similar to `<my_user_agent> pandas-x.y.z`.

    The legacy format used a hyphen to separate the product from the product
    version which differs slightly from the format recommended by RFC9110, which is:
    `product/x.y.z`. To produce a user agent more in line with the RFC, set
    rfc9110_delimiter to True. This setting does not depend on whether a
    user_agent is also supplied.

    Reference:
        https://www.rfc-editor.org/info/rfc9110

    Args:
        user_agent (Optional[str]): User agent string.

        rfc9110_delimiter (Optional[bool]): Sets delimiter to a hyphen or a slash.
        Default is False, meaning a hyphen will be used.

    Returns (str):
        Customized user agent string.

    Deprecation Warning:
        In a future major release, the default delimiter will be changed to
        a `/` in accordance with RFC9110.
    """
    import pandas as pd

    if rfc9110_delimiter:
        delimiter = "/"
    else:
        warnings.warn(
            "In a future major release, the default delimiter will be "
            "changed to a `/` in accordance with RFC9110.",
            PendingDeprecationWarning,
            stacklevel=2,
        )
        delimiter = "-"

    identities = [] if user_agent is None else [user_agent]
    identities.append(f"pandas{delimiter}{pd.__version__}")

    if environment.is_vscode():
        identities.append("vscode")
        if environment.is_vscode_google_cloud_code_extension_installed():
            identities.append(environment.GOOGLE_CLOUD_CODE_EXTENSION_NAME)
    elif environment.is_jupyter():
        identities.append("jupyter")
        if environment.is_jupyter_bigquery_plugin_installed():
            identities.append(environment.BIGQUERY_JUPYTER_PLUGIN_NAME)

    return " ".join(identities)
