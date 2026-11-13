# Copyright (c) 2021 The sqlalchemy-bigquery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import contextlib
import os
import re
import traceback

import google.cloud.bigquery.dbapi.connection
import test_utils.prefixer
from sqlalchemy.testing import config
from sqlalchemy.testing.plugin import pytestplugin

# flake8: F401, F403 are ignored because SQLAlchemy requires importing its testing
# plugin fixtures and hooks directly into the pytest conftest namespace.
from sqlalchemy.testing.plugin.pytestplugin import *  # noqa: F401, F403

import sqlalchemy_bigquery.base
import sqlalchemy_bigquery.provision

sqlalchemy_bigquery.BigQueryDialect.preexecute_autoincrement_sequences = True


prefixer = test_utils.prefixer.Prefixer(
    "python-bigquery-sqlalchemy", "tests/compliance"
)

google.cloud.bigquery.dbapi.connection.Connection.rollback = lambda self: None

_where = re.compile(r"\s+WHERE\s+", re.IGNORECASE).search

# BigQuery requires delete statements to have where clauses. Other
# databases don't and sqlalchemy doesn't include where clauses when
# cleaning up test data.  So we add one when we see a delete without a
# where clause when tearing down tests.  We only do this during tear
# down, by inspecting the stack, because we don't want to hide bugs
# outside of test house-keeping.


def visit_delete(self, delete_stmt, *args, **kw):
    """Compile DELETE statements, appending WHERE true during test teardown."""
    text = super(sqlalchemy_bigquery.base.BigQueryCompiler, self).visit_delete(
        delete_stmt, *args, **kw
    )

    if not _where(text) and any(
        "teardown" in f.name.lower() for f in traceback.extract_stack()
    ):
        text += " WHERE true"

    return text


sqlalchemy_bigquery.base.BigQueryCompiler.visit_delete = visit_delete


def _resolve_dataset_id(cfg) -> str:
    """Resolve the dataset ID for the current runner process (worker or master)."""
    run_prefix = os.environ["COMPLIANCE_RUN_PREFIX"]
    if hasattr(cfg, "workerinput"):
        ident = cfg.workerinput.get("follower_ident")
        if ident:
            return sqlalchemy_bigquery.provision._dataset_id_from_ident(ident)
        return f"{run_prefix}_worker"
    return f"{run_prefix}_master"


def pytest_configure(config):
    """Configure pytest session, establishing compliance run prefix and target dburi."""
    if hasattr(config, "workerinput"):
        prefix = config.workerinput.get("compliance_run_prefix")
        if prefix:
            os.environ["COMPLIANCE_RUN_PREFIX"] = prefix
    else:
        if "COMPLIANCE_RUN_PREFIX" not in os.environ:
            os.environ["COMPLIANCE_RUN_PREFIX"] = prefixer.create_prefix()

    dataset_id = _resolve_dataset_id(config)
    config.option.dburi = [f"bigquery:///{dataset_id}"]
    pytestplugin.pytest_configure(config)


def pytest_configure_node(node):
    """Propagate the compliance run prefix from the controller to worker nodes."""
    node.workerinput["compliance_run_prefix"] = os.environ.get("COMPLIANCE_RUN_PREFIX")


def pytest_sessionstart(session):
    """Ensure the target dataset exists before running compliance tests in the session."""
    dataset_id = _resolve_dataset_id(session.config)
    session.config.option.dburi = [f"bigquery:///{dataset_id}"]
    sqlalchemy_bigquery.provision.ensure_dataset(dataset_id)
    pytestplugin.pytest_sessionstart(session)


def pytest_sessionfinish(session):
    """Tear down datasets and clean up leaked test datasets after session completion."""
    if hasattr(session.config, "workerinput"):
        # Worker dataset teardown is handled by provision.drop_follower_db
        # on the controller node.
        pytestplugin.pytest_sessionfinish(session)
        return

    pytestplugin.pytest_sessionfinish(session)
    run_prefix = os.environ.get("COMPLIANCE_RUN_PREFIX")
    db = getattr(session.config, "db", None) or getattr(config, "db", None)
    if db is not None and hasattr(db.dialect, "dataset_id"):
        sqlalchemy_bigquery.provision.drop_dataset(db.dialect.dataset_id)
    elif run_prefix:
        sqlalchemy_bigquery.provision.drop_dataset(f"{run_prefix}_master")

    with contextlib.closing(google.cloud.bigquery.Client()) as client:
        for dataset in client.list_datasets():
            if prefixer.should_cleanup(dataset.dataset_id):
                client.delete_dataset(dataset, delete_contents=True, not_found_ok=True)
