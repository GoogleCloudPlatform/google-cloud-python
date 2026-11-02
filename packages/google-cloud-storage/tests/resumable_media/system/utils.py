# Copyright 2017 Google Inc.
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

import base64
import hashlib
import time

from test_utils.retry import RetryResult  # type: ignore

BUCKET_NAME = "grpm-systest-{}".format(int(1000 * time.time()))
BUCKET_POST_URL = "https://www.googleapis.com/storage/v1/b/"
BUCKET_URL = "https://www.googleapis.com/storage/v1/b/{}".format(BUCKET_NAME)

_DOWNLOAD_BASE = "https://www.googleapis.com/download/storage/v1/b/{}".format(
    BUCKET_NAME
)
DOWNLOAD_URL_TEMPLATE = _DOWNLOAD_BASE + "/o/{blob_name}?alt=media"

_UPLOAD_BASE = (
    "https://www.googleapis.com/upload/storage/v1/b/{}".format(BUCKET_NAME)
    + "/o?uploadType="
)
SIMPLE_UPLOAD_TEMPLATE = _UPLOAD_BASE + "media&name={blob_name}"
MULTIPART_UPLOAD = _UPLOAD_BASE + "multipart"
RESUMABLE_UPLOAD = _UPLOAD_BASE + "resumable"

METADATA_URL_TEMPLATE = BUCKET_URL + "/o/{blob_name}"

XML_UPLOAD_URL_TEMPLATE = "https://{bucket}.storage.googleapis.com/{blob}"


GCS_RW_SCOPE = "https://www.googleapis.com/auth/devstorage.read_write"
# Generated using random.choice() with all 256 byte choices.
ENCRYPTION_KEY = (
    b"R\xb8\x1b\x94T\xea_\xa8\x93\xae\xd1\xf6\xfca\x15\x0ekA"
    b"\x08 Y\x13\xe2\n\x02i\xadc\xe2\xd99x"
)


_RETRYABLE_CODES = [
    409,  # Conflict
    429,  # TooManyRequests
    503,  # ServiceUnavailable
]


def _not_retryable(response):
    return response.status_code not in _RETRYABLE_CODES


retry_transient_errors = RetryResult(_not_retryable)


def get_encryption_headers(key=ENCRYPTION_KEY):
    """Builds customer-supplied encryption key headers

    See `Managing Data Encryption`_ for more details.

    Args:
        key (bytes): 32 byte key to build request key and hash.

    Returns:
        Dict[str, str]: The algorithm, key and key-SHA256 headers.

    .. _Managing Data Encryption:
        https://cloud.google.com/storage/docs/encryption
    """
    key_hash = hashlib.sha256(key).digest()
    key_hash_b64 = base64.b64encode(key_hash)
    key_b64 = base64.b64encode(key)

    return {
        "x-goog-encryption-algorithm": "AES256",
        "x-goog-encryption-key": key_b64.decode("utf-8"),
        "x-goog-encryption-key-sha256": key_hash_b64.decode("utf-8"),
    }
