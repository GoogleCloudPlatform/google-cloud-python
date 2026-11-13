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

import contextlib
import datetime
import os
import uuid

import google.cloud.bigquery
from sqlalchemy.engine import make_url
from sqlalchemy.testing.provision import (
    create_db,
    drop_db,
    follower_url_from_main,
    generate_driver_url,
)

try:
    import test_utils.prefixer  # pragma: NO COVER

    prefixer = test_utils.prefixer.Prefixer(  # pragma: NO COVER
        "python-bigquery-sqlalchemy", "tests/compliance"
    )
except ImportError:
    prefixer = None


def _dataset_id_from_ident(ident: str) -> str:
    """Derive a deterministic BigQuery dataset ID for an xdist follower ident."""
    run_prefix = os.environ.get("COMPLIANCE_RUN_PREFIX")
    if not run_prefix:
        if prefixer:
            run_prefix = prefixer.create_prefix()
        else:
            now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S")
            run_prefix = f"python_bigquery_sqlalchemy_tests_compliance_{now}_{uuid.uuid4().hex[:6]}"
        os.environ["COMPLIANCE_RUN_PREFIX"] = run_prefix
    return f"{run_prefix}_{ident}"


@generate_driver_url.for_db("bigquery")
def _bigquery_generate_driver_url(url, driver, query_str):
    url = make_url(url)
    if driver and driver != "bigquery":
        new_url = url.set(drivername=f"bigquery+{driver}")
    else:
        new_url = url.set(drivername="bigquery")
    if query_str:
        new_url = new_url.update_query_string(query_str)
    return new_url


@follower_url_from_main.for_db("bigquery")
def _bigquery_follower_url_from_main(url, ident):
    url = make_url(url)
    dataset_id = _dataset_id_from_ident(ident)
    return url.set(database=dataset_id)


def ensure_dataset(dataset_id: str) -> None:
    """Ensure a BigQuery dataset exists with a 1-hour expiration safety net."""
    with contextlib.closing(google.cloud.bigquery.Client()) as client:
        dataset_ref = google.cloud.bigquery.DatasetReference(client.project, dataset_id)
        dataset = google.cloud.bigquery.Dataset(dataset_ref)
        dataset.default_table_expiration_ms = 3600 * 1000
        client.create_dataset(dataset, exists_ok=True)


def drop_dataset(dataset_id: str) -> None:
    """Drop a BigQuery dataset and its contents if it exists."""
    with contextlib.closing(google.cloud.bigquery.Client()) as client:
        client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)


@create_db.for_db("bigquery")
def _bigquery_create_db(cfg, eng, ident):
    dataset_id = _dataset_id_from_ident(ident)
    ensure_dataset(dataset_id)


@drop_db.for_db("bigquery")
def _bigquery_drop_db(cfg, eng, ident):
    dataset_id = _dataset_id_from_ident(ident)
    drop_dataset(dataset_id)
