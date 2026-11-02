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

import google.auth.transport._aiohttp_requests as tr_requests  # type: ignore
import pytest  # type: ignore
from google.auth._default_async import default_async  # type: ignore

from tests.system import utils


async def ensure_bucket(transport):
    get_response = await transport.request("GET", utils.BUCKET_URL)
    if get_response.status == 404:
        credentials = transport.credentials
        query_params = {"project": credentials.project_id}
        payload = {"name": utils.BUCKET_NAME}
        post_response = await transport.request(
            "POST", utils.BUCKET_POST_URL, params=query_params, json=payload
        )
        if not (post_response.status == 200):
            raise ValueError(
                "{}: {}".format(post_response.status, post_response.reason)
            )


async def cleanup_bucket(transport):
    del_response = await transport.request("DELETE", utils.BUCKET_URL)

    if not (del_response.status == 204):
        raise ValueError("{}: {}".format(del_response.status, del_response.reason))


def _get_authorized_transport():
    credentials, project_id = default_async(scopes=(utils.GCS_RW_SCOPE,))
    return tr_requests.AuthorizedSession(credentials)


@pytest.fixture(scope="module")
async def authorized_transport():
    credentials, project_id = default_async(scopes=(utils.GCS_RW_SCOPE,))
    yield _get_authorized_transport()


@pytest.fixture(scope="session")
async def bucket():
    authorized_transport = _get_authorized_transport()
    await ensure_bucket(authorized_transport)
    yield utils.BUCKET_URL
    await cleanup_bucket(authorized_transport)
