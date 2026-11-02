# Copyright 2026 Google LLC All rights reserved.
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

"""Cloud Spanner exception utilities with request ID support."""

from google.api_core.exceptions import GoogleAPICallError


def wrap_with_request_id(error, request_id=None):
    """Add request ID information to a GoogleAPICallError.

    This function adds request_id as an attribute to the exception,
    preserving the original exception type for exception handling compatibility.
    The request_id is also appended to the error message so it appears in logs.

    Args:
        error: The error to augment. If not a GoogleAPICallError, returns as-is
        request_id (str): The request ID to include

    Returns:
        The original error with request_id attribute added and message updated
        (if GoogleAPICallError and request_id is provided), otherwise returns
        the original error unchanged.
    """
    if isinstance(error, GoogleAPICallError) and request_id:
        old_req_id = getattr(error, "request_id", None)
        if old_req_id == request_id:
            return error
        # Add request_id as an attribute for programmatic access
        error.request_id = request_id
        # Modify the message to include request_id so it appears in logs
        message = getattr(error, "message", None)
        if isinstance(message, str) and message:
            if old_req_id and f", request_id = {old_req_id}" in message:
                error.message = message.replace(
                    f", request_id = {old_req_id}", f", request_id = {request_id}"
                )
            else:
                error.message = f"{message}, request_id = {request_id}"
    return error
