# Copyright 2016 Google LLC All Rights Reserved.
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

"""Utility functions for Error Reporting."""

from google.cloud.error_reporting.client import HTTPContext


def build_flask_context(request):
    """Builds an HTTP context object from a Flask (Werkzeug) request object.

     This helper method extracts the relevant HTTP context from a Flask request
     object into an object ready to be sent to Error Reporting.

    .. code-block:: python

        >>> @app.errorhandler(HTTPException)
        ... def handle_error(exc):
        ...     client.report_exception(
        ...         http_context=build_flask_context(request))
        ...     # rest of error response code here

    :type request: :class:`werkzeug.wrappers.request`
    :param request: The Flask request object to convert.

    :rtype: :class:`~google.cloud.error_reporting.client.HTTPContext`
    :returns: An HTTPContext object ready to be sent to the Error Reporting
              API.
    """
    return HTTPContext(
        url=request.url,
        method=request.method,
        user_agent=request.user_agent.string,
        referrer=request.referrer,
        remote_ip=request.remote_addr,
    )
