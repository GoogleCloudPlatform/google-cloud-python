# Copyright 2026 Google LLC
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

import pytest

import bigquery_magics.config
from bigquery_magics import bigquery as magics


@pytest.fixture(autouse=True)
def mock_bq_client_and_credentials(mock_credentials):
    from unittest import mock

    with mock.patch("google.cloud.bigquery.Client", autospec=True):
        with mock.patch("bigquery_magics.core.create_bq_client", autospec=True):
            yield


def test_config_engine_setter_warning():
    context = bigquery_magics.config.Context()
    with pytest.warns(FutureWarning, match="The bigframes engine is deprecated"):
        context.engine = "bigframes"


def test_query_with_bigframes_warning(mock_ipython):
    # Mocking bigframes.pandas since it might not be installed
    from unittest import mock

    with mock.patch("bigquery_magics.bigquery.bpd") as mock_bpd:
        mock_bpd.read_gbq_query.return_value = mock.MagicMock()

        args = mock.MagicMock()
        args.engine = "bigframes"
        args.dry_run = False
        args.max_results = None
        args.destination_var = None
        args.destination_table = None

        with pytest.warns(FutureWarning, match="The bigframes engine is deprecated"):
            magics._query_with_bigframes("SELECT 1", [], args)


def test_cell_magic_engine_bigframes_warning(mock_ipython):
    from unittest import mock

    from IPython.testing.globalipapp import get_ipython, start_ipython

    start_ipython()
    ip = get_ipython()

    ip.extension_manager.load_extension("bigquery_magics")

    # Mock the actual execution to avoid needing real credentials/data
    with mock.patch("bigquery_magics.bigquery.bpd") as mock_bpd:
        mock_bpd.read_gbq_query.return_value = mock.MagicMock()
        with pytest.warns(FutureWarning, match="The bigframes engine is deprecated"):
            ip.run_cell_magic("bigquery", "--engine bigframes", "SELECT 1")


@pytest.fixture
def mock_ipython():
    from unittest import mock

    with mock.patch("bigquery_magics.bigquery.get_ipython") as mock_get_ipython:
        yield mock_get_ipython
