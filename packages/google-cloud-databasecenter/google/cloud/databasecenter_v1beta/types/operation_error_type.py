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

__protobuf__ = proto.module(
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "OperationErrorType",
    },
)


class OperationErrorType(proto.Enum):
    r"""OperationErrorType is used to expose specific error type
    which can happen in database resource while performing an
    operation. For example, an error can happen while database
    resource being backed up.

    Values:
        OPERATION_ERROR_TYPE_UNSPECIFIED (0):
            UNSPECIFIED means operation error type is not
            known or available.
        KMS_KEY_ERROR (1):
            Key destroyed, expired, not found,
            unreachable or permission denied.
        DATABASE_ERROR (2):
            Database is not accessible.
        STOCKOUT_ERROR (3):
            The zone or region does not have sufficient
            resources to handle the request at the moment.
        CANCELLATION_ERROR (4):
            User initiated cancellation.
        SQLSERVER_ERROR (5):
            SQL server specific error.
        INTERNAL_ERROR (6):
            Any other internal error.
    """

    OPERATION_ERROR_TYPE_UNSPECIFIED = 0
    KMS_KEY_ERROR = 1
    DATABASE_ERROR = 2
    STOCKOUT_ERROR = 3
    CANCELLATION_ERROR = 4
    SQLSERVER_ERROR = 5
    INTERNAL_ERROR = 6


__all__ = tuple(sorted(__protobuf__.manifest))
