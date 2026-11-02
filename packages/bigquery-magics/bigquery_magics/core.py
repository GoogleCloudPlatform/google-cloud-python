# Copyright 2026 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy

import IPython  # type: ignore
from google.api_core import client_info
from google.cloud import bigquery

import bigquery_magics.config
import bigquery_magics.version
from bigquery_magics import environment

context = bigquery_magics.config.context


def _get_user_agent():
    identities = [
        f"ipython-{IPython.__version__}",
        f"bigquery-magics/{bigquery_magics.version.__version__}",
    ]

    if environment.is_vscode():
        identities.append("vscode")
        if environment.is_vscode_google_cloud_code_extension_installed():
            identities.append(environment.GOOGLE_CLOUD_CODE_EXTENSION_NAME)
    elif environment.is_jupyter():
        identities.append("jupyter")
        if environment.is_jupyter_bigquery_plugin_installed():
            identities.append(environment.BIGQUERY_JUPYTER_PLUGIN_NAME)

    return " ".join(identities)


def create_bq_client(*, project: str, bigquery_api_endpoint: str, location: str):
    """Creates a BigQuery client.

    Args:
        project: Project to use for api calls, None to obtain the project from the context.
        bigquery_api_endpoint: Bigquery client endpoint.
        location: Cloud region to use for api calls.

    Returns:
        google.cloud.bigquery.client.Client: The BigQuery client.
    """
    bigquery_client_options = copy.deepcopy(context.bigquery_client_options)
    if bigquery_api_endpoint:
        if isinstance(bigquery_client_options, dict):
            bigquery_client_options["api_endpoint"] = bigquery_api_endpoint
        else:
            bigquery_client_options.api_endpoint = bigquery_api_endpoint

    bq_client = bigquery.Client(
        project=project or context.project,
        credentials=context.credentials,
        default_query_job_config=context.default_query_job_config,
        client_info=client_info.ClientInfo(user_agent=_get_user_agent()),
        client_options=bigquery_client_options,
        location=location,
    )
    if context._connection:
        bq_client._connection = context._connection

    return bq_client
