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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.errorreporting_v1beta1.types import common

__protobuf__ = proto.module(
    package="google.devtools.clouderrorreporting.v1beta1",
    manifest={
        "ReportErrorEventRequest",
        "ReportErrorEventResponse",
        "ReportedErrorEvent",
    },
)


class ReportErrorEventRequest(proto.Message):
    r"""A request for reporting an individual error event.

    Attributes:
        project_name (str):
            Required. The resource name of the Google Cloud Platform
            project. Written as ``projects/{projectId}``, where
            ``{projectId}`` is the `Google Cloud Platform project
            ID <https://support.google.com/cloud/answer/6158840>`__.

            Example: // ``projects/my-project-123``.
        event (google.cloud.errorreporting_v1beta1.types.ReportedErrorEvent):
            Required. The error event to be reported.
    """

    project_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event: "ReportedErrorEvent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReportedErrorEvent",
    )


class ReportErrorEventResponse(proto.Message):
    r"""Response for reporting an individual error event.
    Data may be added to this message in the future.

    """


class ReportedErrorEvent(proto.Message):
    r"""An error event which is reported to the Error Reporting
    system.

    Attributes:
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Time when the event occurred. If not provided, the
            time when the event was received by the Error Reporting
            system is used. If provided, the time must not exceed the
            `logs retention
            period <https://cloud.google.com/logging/quotas#logs_retention_periods>`__
            in the past, or be more than 24 hours in the future. If an
            invalid time is provided, then an error is returned.
        service_context (google.cloud.errorreporting_v1beta1.types.ServiceContext):
            Required. The service context in which this
            error has occurred.
        message (str):
            Required. The error message. If no
            ``context.reportLocation`` is provided, the message must
            contain a header (typically consisting of the exception type
            name and an error message) and an exception stack trace in
            one of the supported programming languages and formats.
            Supported languages are Java, Python, JavaScript, Ruby, C#,
            PHP, and Go. Supported stack trace formats are:

            - **Java**: Must be the return value of
              ```Throwable.printStackTrace()`` <https://docs.oracle.com/javase/7/docs/api/java/lang/Throwable.html#printStackTrace%28%29>`__.
            - **Python**: Must be the return value of
              ```traceback.format_exc()`` <https://docs.python.org/2/library/traceback.html#traceback.format_exc>`__.
            - **JavaScript**: Must be the value of
              ```error.stack`` <https://github.com/v8/v8/wiki/Stack-Trace-API>`__
              as returned by V8.
            - **Ruby**: Must contain frames returned by
              ```Exception.backtrace`` <https://ruby-doc.org/core-2.2.0/Exception.html#method-i-backtrace>`__.
            - **C#**: Must be the return value of
              ```Exception.ToString()`` <https://msdn.microsoft.com/en-us/library/system.exception.tostring.aspx>`__.
            - **PHP**: Must be prefixed with
              ``"PHP (Notice|Parse error|Fatal error|Warning): "`` and
              contain the result of
              ```(string)$exception`` <https://php.net/manual/en/exception.tostring.php>`__.
            - **Go**: Must be the return value of
              ```runtime.Stack()`` <https://golang.org/pkg/runtime/debug/#Stack>`__.
        context (google.cloud.errorreporting_v1beta1.types.ErrorContext):
            Optional. A description of the context in
            which the error occurred.
    """

    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    service_context: common.ServiceContext = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.ServiceContext,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    context: common.ErrorContext = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.ErrorContext,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
