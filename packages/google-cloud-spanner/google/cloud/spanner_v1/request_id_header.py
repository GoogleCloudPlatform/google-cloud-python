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

import os

REQ_ID_VERSION = 1  # The version of the x-goog-spanner-request-id spec.
REQ_ID_HEADER_KEY = "x-goog-spanner-request-id"


def generate_rand_uint64():
    return int.from_bytes(os.urandom(8), "big")


REQ_RAND_PROCESS_ID = generate_rand_uint64()
_REQ_ID_PROCESS_PREFIX = f"{REQ_ID_VERSION}.{REQ_RAND_PROCESS_ID}."
X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR = "x_goog_spanner_request_id"


class _CachedPrefixDescriptor:
    """Non-data descriptor that computes and caches _req_id_prefix in instance __dict__."""

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        prefix = (
            f"{_REQ_ID_PROCESS_PREFIX}{instance._nth_client_id}.{instance._channel_id}."
        )
        instance.__dict__["_req_id_prefix"] = prefix
        return prefix


def with_request_id(
    client_id, channel_id, nth_request, attempt, other_metadata=None, span=None
):
    req_id = f"{_REQ_ID_PROCESS_PREFIX}{client_id}.{channel_id}.{nth_request}.{attempt}"
    all_metadata = (
        [*other_metadata, (REQ_ID_HEADER_KEY, req_id)]
        if other_metadata
        else [(REQ_ID_HEADER_KEY, req_id)]
    )

    if span is not None and span.is_recording():
        span.set_attribute(X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR, req_id)

    return all_metadata, req_id


def with_request_id_metadata_only(
    client_id, channel_id, nth_request, attempt, other_metadata=None, span=None
):
    """Return metadata with request ID header, discarding the request ID value."""
    req_id = f"{_REQ_ID_PROCESS_PREFIX}{client_id}.{channel_id}.{nth_request}.{attempt}"
    all_metadata = (
        [*other_metadata, (REQ_ID_HEADER_KEY, req_id)]
        if other_metadata
        else [(REQ_ID_HEADER_KEY, req_id)]
    )

    if span is not None and span.is_recording():
        span.set_attribute(X_GOOG_SPANNER_REQUEST_ID_SPAN_ATTR, req_id)

    return all_metadata


def build_request_id(client_id, channel_id, nth_request, attempt):
    return f"{_REQ_ID_PROCESS_PREFIX}{client_id}.{channel_id}.{nth_request}.{attempt}"


def parse_request_id(request_id_str):
    version, rand_process_id, client_id, channel_id, nth_request, nth_attempt = map(
        int, request_id_str.split(".")
    )
    return (
        version,
        rand_process_id,
        client_id,
        channel_id,
        nth_request,
        nth_attempt,
    )
