# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
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

import os
import time

from google.cloud import errorreporting_v1beta1


class TestSystemReportErrorsService(object):
    def test_report_error_event(self):
        project_id = os.environ["PROJECT_ID"]

        client = errorreporting_v1beta1.ReportErrorsServiceClient()
        project_name = f"projects/{project_id}"
        message = "[MESSAGE]"
        service = "[SERVICE]"
        service_context = {"service": service}
        file_path = "path/to/file.lang"
        line_number = 42
        function_name = "meaningOfLife"
        report_location = {
            "file_path": file_path,
            "line_number": line_number,
            "function_name": function_name,
        }
        context = {"report_location": report_location}
        event = {
            "message": message,
            "service_context": service_context,
            "context": context,
        }
        response = client.report_error_event(
            request={"project_name": project_name, "event": event}
        )
