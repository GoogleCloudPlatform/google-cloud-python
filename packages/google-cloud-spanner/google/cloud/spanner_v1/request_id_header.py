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
# Python clients always report channel 1.
REQ_CHANNEL_ID = 1


def generate_rand_uint64():
    return int.from_bytes(os.urandom(8), "big")


def _get_process_id():
    """Return the process ID used in every request ID of this process.

    Users can override it with the ``SPANNER_PROCESS_ID`` or
    ``GOOGLE_CLOUD_SPANNER_PROCESS_ID`` environment variable. Otherwise it is a
    64-bit random value formatted as 16 lower-case hexadecimal characters,
    matching the Java and Go clients.
    """
    return (
        os.environ.get("SPANNER_PROCESS_ID")
        or os.environ.get("GOOGLE_CLOUD_SPANNER_PROCESS_ID")
        or f"{generate_rand_uint64():016x}"
    )


REQ_RAND_PROCESS_ID = _get_process_id()
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
    """Parse ``<version>.<process>.<client>.<channel>.<request>.<attempt>``.

    Returns a 6-tuple. The process ID is returned as its hexadecimal string;
    the other five components are returned as ints.
    """
    splits = request_id_str.split(".")
    if len(splits) != 6:
        raise ValueError(
            f"Request ID must have 6 dot-separated components, got {len(splits)}: "
            f"{request_id_str!r}"
        )
    version, rand_process_id, client_id, channel_id, nth_request, nth_attempt = splits
    return (
        int(version),
        rand_process_id,
        int(client_id),
        int(channel_id),
        int(nth_request),
        int(nth_attempt),
    )
