# Copyright 2024 Google LLC All rights reserved.
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
from os import listdir
from os.path import isfile, join

import nox


@nox.session()
def hello_world(session):
    _sample(session)


@nox.session()
def auto_generated_primary_key(session):
    _sample(session)


@nox.session()
def bit_reversed_sequence(session):
    _sample(session)


@nox.session()
def date_and_timestamp(session):
    _sample(session)


@nox.session()
def default_column_value(session):
    _sample(session)


@nox.session()
def generated_column(session):
    _sample(session)


@nox.session()
def insert_data(session):
    _sample(session)


@nox.session()
def interleaved_table(session):
    _sample(session)


@nox.session()
def transaction(session):
    _sample(session)


@nox.session()
def tags(session):
    _sample(session)


@nox.session()
def isolation_level(session):
    _sample(session)


@nox.session()
def stale_read(session):
    _sample(session)


@nox.session()
def read_only_transaction(session):
    _sample(session)


@nox.session()
def database_role(session):
    _sample(session)


@nox.session()
def informational_fk(session):
    _sample(session)


@nox.session()
def insertmany(session):
    _sample(session)


@nox.session()
def parse_json(session):
    _sample(session)


@nox.session()
def _all_samples(session):
    _sample(session)


def _sample(session):
    session.install("testcontainers")
    session.install("sqlalchemy")
    session.install("setuptools")
    session.install(
        "git+https://github.com/googleapis/python-spanner.git#egg=google-cloud-spanner"
    )
    session.install("../.")
    if session.name == "_all_samples":
        files = [
            f for f in listdir(".") if isfile(join(".", f)) and f.endswith("_sample.py")
        ]
        for file in files:
            session.run("python", file)
    else:
        session.run("python", session.name + "_sample.py")
