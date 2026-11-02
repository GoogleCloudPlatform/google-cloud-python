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

"""Interact with Error Reporting via Logging API.

It's possible to report Error Reporting errors by formatting
structured log messages in Cloud Logging in a given format. This
client provides a mechanism to report errors using that technique.
"""

import google.cloud.logging


class _ErrorReportingLoggingAPI(object):
    """Report to Error Reporting via Logging API

    :type project: str
    :param project: the project which the client acts on behalf of. If not
                    passed falls back to the default inferred from the
                    environment.

    :type credentials: :class:`google.auth.credentials.Credentials` or
                       :class:`NoneType`
    :param credentials: The authorization credentials to attach to requests.
                        These credentials identify this application to the service.
                        If none are specified, the client will attempt to ascertain
                        the credentials from the environment.

    :type _http: :class:`~requests.Session`
    :param _http: (Optional) HTTP object to make requests. Can be any object
                  that defines ``request()`` with the same interface as
                  :meth:`requests.Session.request`. If not passed, an
                  ``_http`` object is created that is bound to the
                  ``credentials`` for the current object.
                  This parameter should be considered private, and could
                  change in the future.

    :type client_info:
        :class:`google.api_core.client_info.ClientInfo` or
        :class:`google.api_core.gapic_v1.client_info.ClientInfo`
    :param client_info:
        The client info used to send a user-agent string along with API
        requests. If ``None``, then default info will be used. Generally,
        you only need to set this if you're developing your own library
        or partner tool.

    :type client_options: :class:`~google.api_core.client_options.ClientOptions`
        or :class:`dict`
    :param client_options: (Optional) Client options used to set user options
        on the client. API Endpoint should be set through client_options.
    """

    def __init__(
        self,
        project,
        credentials=None,
        _http=None,
        client_info=None,
        client_options=None,
    ):
        self.logging_client = google.cloud.logging.Client(
            project=project,
            credentials=credentials,
            _http=_http,
            client_info=client_info,
            client_options=client_options,
        )

    def report_error_event(self, error_report):
        """Report error payload.

        :type error_report: dict
        :param: error_report:
            dict payload of the error report formatted according to
            https://cloud.google.com/error-reporting/docs/formatting-error-messages
            This object should be built using
            :meth:~`google.cloud.error_reporting.client._build_error_report`
        """
        logger = self.logging_client.logger("errors")
        logger.log_struct(error_report)
