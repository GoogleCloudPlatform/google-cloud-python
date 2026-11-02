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

import proto  # type: ignore

from google.cloud.websecurityscanner_v1.types import (
    scan_config_error as gcw_scan_config_error,
)

__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1",
    manifest={
        "ScanRunErrorTrace",
    },
)


class ScanRunErrorTrace(proto.Message):
    r"""Output only.
    Defines an error trace message for a ScanRun.

    Attributes:
        code (google.cloud.websecurityscanner_v1.types.ScanRunErrorTrace.Code):
            Output only. Indicates the error reason code.
        scan_config_error (google.cloud.websecurityscanner_v1.types.ScanConfigError):
            Output only. If the scan encounters SCAN_CONFIG_ISSUE error,
            this field has the error message encountered during scan
            configuration validation that is performed before each scan
            run.
        most_common_http_error_code (int):
            Output only. If the scan encounters TOO_MANY_HTTP_ERRORS,
            this field indicates the most common HTTP error code, if
            such is available. For example, if this code is 404, the
            scan has encountered too many NOT_FOUND responses.
    """

    class Code(proto.Enum):
        r"""Output only.
        Defines an error reason code.
        Next id: 8

        Values:
            CODE_UNSPECIFIED (0):
                Default value is never used.
            INTERNAL_ERROR (1):
                Indicates that the scan run failed due to an
                internal server error.
            SCAN_CONFIG_ISSUE (2):
                Indicates a scan configuration error, usually due to
                outdated ScanConfig settings, such as starting_urls or the
                DNS configuration.
            AUTHENTICATION_CONFIG_ISSUE (3):
                Indicates an authentication error, usually
                due to outdated ScanConfig authentication
                settings.
            TIMED_OUT_WHILE_SCANNING (4):
                Indicates a scan operation timeout, usually
                caused by a very large site.
            TOO_MANY_REDIRECTS (5):
                Indicates that a scan encountered excessive
                redirects, either to authentication or some
                other page outside of the scan scope.
            TOO_MANY_HTTP_ERRORS (6):
                Indicates that a scan encountered numerous errors from the
                web site pages. When available, most_common_http_error_code
                field indicates the most common HTTP error code encountered
                during the scan.
        """

        CODE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        SCAN_CONFIG_ISSUE = 2
        AUTHENTICATION_CONFIG_ISSUE = 3
        TIMED_OUT_WHILE_SCANNING = 4
        TOO_MANY_REDIRECTS = 5
        TOO_MANY_HTTP_ERRORS = 6

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )
    scan_config_error: gcw_scan_config_error.ScanConfigError = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcw_scan_config_error.ScanConfigError,
    )
    most_common_http_error_code: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
