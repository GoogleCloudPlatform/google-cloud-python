# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import pytest

from pandas_gbq.features import FEATURES


@pytest.fixture(autouse=True)
def fresh_bigquery_version(monkeypatch):
    monkeypatch.setattr(FEATURES, "_bigquery_installed_version", None)
    monkeypatch.setattr(FEATURES, "_pandas_installed_version", None)


@pytest.mark.parametrize(
    ["bigquery_version", "expected"],
    [
        ("1.99.100", False),
        ("2.99.999", False),
        ("3.13.11", False),
        ("3.14.0", True),
        ("4.999.999", True),
    ],
)
def test_bigquery_has_query_and_wait(monkeypatch, bigquery_version, expected):
    import google.cloud.bigquery

    monkeypatch.setattr(google.cloud.bigquery, "__version__", bigquery_version)
    assert FEATURES.bigquery_has_query_and_wait == expected


@pytest.mark.parametrize(
    ["pandas_version", "expected"],
    [
        ("0.14.7", False),
        ("0.22.1", False),
        ("0.23.0", True),
        ("0.23.1", True),
        ("1.0.0", True),
        ("2.1.3", True),
    ],
)
def test_pandas_has_deprecated_verbose(monkeypatch, pandas_version, expected):
    import pandas

    monkeypatch.setattr(pandas, "__version__", pandas_version)
    assert FEATURES.pandas_has_deprecated_verbose == expected
