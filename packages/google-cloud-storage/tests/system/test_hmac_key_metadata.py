# Copyright 2021 Google LLC
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

import datetime

import pytest

from . import _helpers


def ensure_hmac_key_deleted(hmac_key):
    from google.cloud.storage.hmac_key import HMACKeyMetadata

    if hmac_key.state != HMACKeyMetadata.INACTIVE_STATE:
        hmac_key.state = HMACKeyMetadata.INACTIVE_STATE
        hmac_key.update()
    _helpers.retry_429_harder(hmac_key.delete)()


@pytest.fixture
def scrubbed_hmac_keys(storage_client):
    from google.cloud.storage._helpers import _NOW, _UTC

    before_hmac_keys = set(storage_client.list_hmac_keys())

    now = _NOW(_UTC)
    yesterday = now - datetime.timedelta(days=1)

    # Delete any HMAC keys older than a day.
    for hmac_key in list(before_hmac_keys):
        if hmac_key.time_created < yesterday:
            ensure_hmac_key_deleted(hmac_key)
            before_hmac_keys.remove(hmac_key)

    hmac_keys_to_delete = []
    yield before_hmac_keys, hmac_keys_to_delete

    # Delete any HMAC keys we created
    for hmac_key in hmac_keys_to_delete:
        ensure_hmac_key_deleted(hmac_key)


def test_hmac_key_crud(storage_client, scrubbed_hmac_keys, service_account):
    from google.cloud.storage.hmac_key import HMACKeyMetadata

    before_hmac_keys, hmac_keys_to_delete = scrubbed_hmac_keys

    email = service_account.service_account_email

    metadata, secret = storage_client.create_hmac_key(email)
    hmac_keys_to_delete.append(metadata)

    assert isinstance(secret, str)
    assert len(secret) == 40

    after_hmac_keys = set(storage_client.list_hmac_keys())
    assert metadata not in before_hmac_keys
    assert metadata in after_hmac_keys

    another = HMACKeyMetadata(storage_client)
    another._properties["accessId"] = "nonesuch"

    assert not another.exists()

    another._properties["accessId"] = metadata.access_id
    assert another.exists()

    another.reload()

    assert another._properties == metadata._properties

    metadata.state = HMACKeyMetadata.INACTIVE_STATE
    metadata.update()

    metadata.delete()
    hmac_keys_to_delete.remove(metadata)
