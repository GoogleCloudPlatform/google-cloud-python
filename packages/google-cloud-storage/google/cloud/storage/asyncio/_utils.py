# Copyright 2025 Google LLC
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

import google_crc32c
from google.api_core import exceptions

from google.cloud.storage import _opentelemetry_tracing


def raise_if_no_fast_crc32c():
    """Check if the C-accelerated version of google-crc32c is available.

    If not, raise an error to prevent silent performance degradation.

    raises google.api_core.exceptions.FailedPrecondition: If the C extension is not available.
    returns: True if the C extension is available.
    rtype: bool

    """
    if google_crc32c.implementation != "c":
        raise exceptions.FailedPrecondition(
            "The google-crc32c package is not installed with C support. "
            "C extension is required for faster data integrity checks."
            "For more information, see https://github.com/googleapis/python-crc32c."
        )


def update_write_handle_if_exists(obj, response):
    """Update the write_handle attribute of an object if it exists in the response."""
    if hasattr(response, "write_handle") and response.write_handle is not None:
        obj.write_handle = response.write_handle


def inject_traceparent_to_metadata(metadata=None):
    """Inject W3C traceparent (and tracestate) into gRPC metadata tuple or list."""
    meta_list = list(metadata) if metadata else []
    if not _opentelemetry_tracing._is_otel_traces_enabled():
        return (
            tuple(meta_list)
            if isinstance(metadata, tuple) or metadata is None
            else meta_list
        )

    try:
        from opentelemetry.trace.propagation.tracecontext import (
            TraceContextTextMapPropagator,
        )

        carrier = {}
        TraceContextTextMapPropagator().inject(carrier)
        existing_keys = {k.lower() for k, _ in meta_list}
        for key, val in carrier.items():
            if key.lower() not in existing_keys:
                meta_list.append((key, val))
    except Exception:
        pass

    return (
        tuple(meta_list)
        if isinstance(metadata, tuple) or metadata is None
        else meta_list
    )
