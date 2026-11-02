# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""System tests for Jupyter/IPython connector."""

import re
from unittest import mock

import google.cloud.bigquery
import pandas
from IPython.testing import globalipapp
from IPython.utils import io


def test_bigquery_magic():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()

    ip.extension_manager.load_extension("bigquery_magics")
    sql = """
        SELECT
            CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
            view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10
    """
    with mock.patch.object(
        google.cloud.bigquery.Client,
        "close",
        autospec=True,
        side_effect=google.cloud.bigquery.Client.close,
    ) as mock_close:
        with io.capture_output() as captured:
            result = ip.run_cell_magic("bigquery", "--use_rest_api", sql)

        # Verify that client close is explicitly called to release sockets.
        mock_close.assert_called_once()

    lines = re.split("\n|\r", captured.stdout)
    # Removes blanks & terminal code (result of display clearing)
    updates = list(filter(lambda x: bool(x) and x != "\x1b[2K", lines))
    assert re.match("Executing query with job ID: .*", updates[0])
    assert (re.match("Query executing: .*s", line) for line in updates[1:-1])
    assert isinstance(result, pandas.DataFrame)
    assert len(result) == 10  # verify row count
    assert list(result) == ["url", "view_count"]  # verify column names
