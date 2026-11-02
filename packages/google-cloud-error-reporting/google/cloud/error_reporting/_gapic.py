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

"""GAX wrapper for Error Reporting API requests."""

import json

import google.cloud.errorreporting_v1beta1


def make_report_error_api(client):
    """Create an instance of the gapic Logging API.

    :type client::class:`google.cloud.error_reporting.Client`
    :param client: Error Reporting client.

    :rtype: :class:_ErrorReportingGapicApi
    :returns: An Error Reporting API instance.
    """
    gapic_api = google.cloud.errorreporting_v1beta1.ReportErrorsServiceClient(
        credentials=client._credentials,
        client_info=client._client_info,
        client_options=client._client_options,
    )
    return _ErrorReportingGapicApi(gapic_api, client.project)


class _ErrorReportingGapicApi(object):
    """Helper mapping Error Reporting-related APIs

    :type gapic:
        :class:`google.cloud.errorreporting_v1beta1.ReportErrorsServiceClient`
    :param gapic: API object used to make RPCs.

    :type project: str
    :param project: Google Cloud Project ID
    """

    def __init__(self, gapic_api, project):
        self._gapic_api = gapic_api
        self._project = project

    def report_error_event(self, error_report):
        """Uses the gapic client to report the error.

        :type error_report: dict
        :param error_report:
            payload of the error report formatted according to
            https://cloud.google.com/error-reporting/docs/formatting-error-messages
            This object should be built using
            Use
            :meth:~`google.cloud.error_reporting.client._build_error_report`
        """
        project_name = f"projects/{self._project}"

        # Since error_report uses camel case for key names (like serviceContext),
        # but ReportedErrorEvent uses snake case for key names (like service_context),
        # we need to route throught json.
        error_report_payload = (
            google.cloud.errorreporting_v1beta1.ReportedErrorEvent.from_json(
                json.dumps(error_report)
            )
        )

        self._gapic_api.report_error_event(
            project_name=project_name, event=error_report_payload
        )
