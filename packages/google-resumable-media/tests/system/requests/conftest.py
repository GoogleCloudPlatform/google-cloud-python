# Copyright 2019 Google Inc.
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
"""py.test fixtures to be shared across multiple system test modules."""

import google.auth  # type: ignore
import google.auth.transport.requests as tr_requests  # type: ignore
import pytest  # type: ignore

from tests.system import utils


def ensure_bucket(transport):
    get_response = transport.get(utils.BUCKET_URL)
    if get_response.status_code == 404:
        credentials = transport.credentials
        query_params = {"project": credentials.project_id}
        payload = {"name": utils.BUCKET_NAME}
        post_response = transport.post(
            utils.BUCKET_POST_URL, params=query_params, json=payload
        )

        if not post_response.ok:
            raise ValueError(
                "{}: {}".format(post_response.status_code, post_response.reason)
            )


def cleanup_bucket(transport):
    del_response = utils.retry_transient_errors(transport.delete)(utils.BUCKET_URL)

    if not del_response.ok:
        raise ValueError("{}: {}".format(del_response.status_code, del_response.reason))


@pytest.fixture(scope="session")
def authorized_transport():
    credentials, _ = google.auth.default(scopes=(utils.GCS_RW_SCOPE,))
    yield tr_requests.AuthorizedSession(credentials)


@pytest.fixture(scope="session")
def bucket(authorized_transport):
    ensure_bucket(authorized_transport)

    yield utils.BUCKET_NAME

    cleanup_bucket(authorized_transport)
