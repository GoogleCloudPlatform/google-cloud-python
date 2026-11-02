# -*- coding: utf-8 -*-
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
#

"""Helpers for preparing and structuring API requests.

This module provides utilities to preprocess request parameters and objects
before invoking API methods, such as automatically generating request IDs
if they are not already set.
"""

import uuid
from typing import TYPE_CHECKING, Union

import google.protobuf.message

if TYPE_CHECKING:  # pragma: NO COVER
    import proto  # type: ignore[import-untyped]


def setup_request_id(
    request: Union[google.protobuf.message.Message, "proto.Message", dict, None],
    field_name: str,
    is_proto3_optional: bool,
) -> None:
    """Populate a UUID4 field in the request if it is not already set.

    This helper is used to ensure request idempotency by automatically
    generating a unique identifier (such as `request_id`) for requests
    that support it. If a request is retried, the same identifier can be
    sent on subsequent retries, allowing the server to recognize the retried
    request and prevent duplicate processing (e.g., creating duplicate
    resources).

    Args:
        request (Union[google.protobuf.message.Message, proto.Message, dict, None]): The
            request object or dictionary.
        field_name (str): The name of the field to populate (e.g., "request_id").
        is_proto3_optional (bool): Whether the field supports explicit presence
            (defined with `optional` in proto3 syntax). When True, empty strings ("")
            are preserved as explicit user input per AIP-4235, and UUID auto-population
            occurs only if the field is unset. When False, any empty or falsy value is
            populated with a UUID.
    """
    if request is None:
        return

    # Evaluate whether the field is considered "unset" and needs auto-population.
    #
    # According to AIP-4235, optional request ID fields must be populated
    # if and only if they have explicit presence (`is_proto3_optional=True`)
    # and were not set by the user (i.e. unset). Explicitly provided empty
    # strings ('') must be preserved when `is_proto3_optional=True`.
    should_populate = False
    if isinstance(request, dict):
        if is_proto3_optional:
            # Case 1a: Dictionary request with explicit presence (`is_proto3_optional=True`).
            # Per AIP-4235, auto-populate only if the key is completely missing from
            # the dictionary or its value is explicitly set to None.
            # An explicit empty string ('') must NOT be overwritten.
            should_populate = field_name not in request or request[field_name] is None
        else:
            # Case 1b: Dictionary request without explicit presence (`is_proto3_optional=False`).
            # Auto-populate if the key is missing, None, or falsy (e.g., empty string '').
            should_populate = not request.get(field_name)
    else:
        if is_proto3_optional:
            # Case 2a: Proto request with explicit presence (`is_proto3_optional=True`)
            # (proto-plus wrapper or pure protobuf message).
            # Extract the protobuf from proto-plus if wrapped.
            pure_pb: google.protobuf.message.Message = getattr(request, "_pb", request)
            try:
                should_populate = not pure_pb.HasField(field_name)
            except (AttributeError, ValueError):
                # Fall back if `HasField` fails or is unsupported.
                should_populate = getattr(pure_pb, field_name, None) is None
        else:
            # Case 2b: Proto request without explicit presence (`is_proto3_optional=False`).
            # Auto-populate if the field value is falsy (None or empty string '').
            should_populate = not bool(getattr(request, field_name, False))

    # If the field was found to be empty, set random id
    if should_populate:
        generated_id = str(uuid.uuid4())
        if isinstance(request, dict):
            request[field_name] = generated_id
        else:
            setattr(request, field_name, generated_id)
