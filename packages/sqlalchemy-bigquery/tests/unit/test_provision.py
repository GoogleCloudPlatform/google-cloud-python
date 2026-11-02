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

import os
from unittest import mock

import pytest
from sqlalchemy.engine import make_url

from sqlalchemy_bigquery import provision


def test_dataset_id_from_ident_with_existing_env(monkeypatch):
    monkeypatch.setenv("COMPLIANCE_RUN_PREFIX", "custom_prefix")
    dataset_id = provision._dataset_id_from_ident("gw0")
    assert dataset_id == "custom_prefix_gw0"


def test_dataset_id_from_ident_without_env(monkeypatch):
    monkeypatch.delenv("COMPLIANCE_RUN_PREFIX", raising=False)
    monkeypatch.setattr(provision, "prefixer", None)
    dataset_id = provision._dataset_id_from_ident("gw1")
    cached_prefix = os.environ.get("COMPLIANCE_RUN_PREFIX")
    assert cached_prefix is not None
    assert dataset_id == f"{cached_prefix}_gw1"


def test_dataset_id_from_ident_with_prefixer(monkeypatch):
    monkeypatch.delenv("COMPLIANCE_RUN_PREFIX", raising=False)
    mock_prefixer = mock.Mock()
    mock_prefixer.create_prefix.return_value = "mock_pfx"
    monkeypatch.setattr(provision, "prefixer", mock_prefixer)
    dataset_id = provision._dataset_id_from_ident("gw5")
    assert dataset_id == "mock_pfx_gw5"
    assert os.environ.get("COMPLIANCE_RUN_PREFIX") == "mock_pfx"


@pytest.mark.parametrize(
    "driver, query_str, expected_drivername, expected_query",
    [
        (None, None, "bigquery", {}),
        ("bigquery", None, "bigquery", {}),
        ("bigquery", "param=1", "bigquery", {"param": "1"}),
        ("custom", None, "bigquery+custom", {}),
        ("custom", "param=2", "bigquery+custom", {"param": "2"}),
    ],
)
def test_generate_driver_url(driver, query_str, expected_drivername, expected_query):
    base_url = "bigquery:///test_master"
    result = provision._bigquery_generate_driver_url(base_url, driver, query_str)
    assert result.drivername == expected_drivername
    if expected_query:
        for k, v in expected_query.items():
            assert result.query.get(k) == v


def test_follower_url_from_main(monkeypatch):
    monkeypatch.setenv("COMPLIANCE_RUN_PREFIX", "run_123")
    base_url = make_url("bigquery:///master_dataset")
    follower_url = provision._bigquery_follower_url_from_main(base_url, "gw2")
    assert follower_url.database == "run_123_gw2"


def test_create_db(monkeypatch):
    monkeypatch.setenv("COMPLIANCE_RUN_PREFIX", "run_456")
    mock_client = mock.MagicMock()
    mock_client.project = "test-project"
    mock_cfg = mock.Mock()
    mock_cfg.db.url = make_url("bigquery:///test_dataset")

    with mock.patch("google.cloud.bigquery.Client", return_value=mock_client):
        provision._bigquery_create_db(mock_cfg, mock.Mock(), "gw3")

    mock_client.create_dataset.assert_called_once()
    created_dataset = mock_client.create_dataset.call_args[0][0]
    assert created_dataset.dataset_id == "run_456_gw3"
    assert created_dataset.default_table_expiration_ms == 3600 * 1000
    assert mock_client.create_dataset.call_args[1].get("exists_ok") is True


def test_drop_db(monkeypatch):
    monkeypatch.setenv("COMPLIANCE_RUN_PREFIX", "run_789")
    mock_client = mock.MagicMock()
    mock_cfg = mock.Mock()
    mock_cfg.db.url = make_url("bigquery:///test_dataset")

    with mock.patch("google.cloud.bigquery.Client", return_value=mock_client):
        provision._bigquery_drop_db(mock_cfg, mock.Mock(), "gw4")

    mock_client.delete_dataset.assert_called_once_with(
        "run_789_gw4", delete_contents=True, not_found_ok=True
    )


def test_ensure_dataset():
    mock_client = mock.MagicMock()
    mock_client.project = "test-project"

    with mock.patch("google.cloud.bigquery.Client", return_value=mock_client):
        provision.ensure_dataset("custom_dataset_123")

    mock_client.create_dataset.assert_called_once()
    created = mock_client.create_dataset.call_args[0][0]
    assert created.dataset_id == "custom_dataset_123"
    assert created.default_table_expiration_ms == 3600 * 1000
    assert mock_client.create_dataset.call_args[1].get("exists_ok") is True


def test_drop_dataset():
    mock_client = mock.MagicMock()

    with mock.patch("google.cloud.bigquery.Client", return_value=mock_client):
        provision.drop_dataset("custom_dataset_456")

    mock_client.delete_dataset.assert_called_once_with(
        "custom_dataset_456", delete_contents=True, not_found_ok=True
    )
