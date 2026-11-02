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
    package="google.cloud.securitycenter.v1",
    manifest={
        "CustomModuleValidationErrors",
        "CustomModuleValidationError",
        "Position",
    },
)


class CustomModuleValidationErrors(proto.Message):
    r"""A list of zero or more errors encountered while validating
    the uploaded configuration of an Event Threat Detection Custom
    Module.

    Attributes:
        errors (MutableSequence[google.cloud.securitycenter_v1.types.CustomModuleValidationError]):

    """

    errors: MutableSequence["CustomModuleValidationError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomModuleValidationError",
    )


class CustomModuleValidationError(proto.Message):
    r"""An error encountered while validating the uploaded
    configuration of an Event Threat Detection Custom Module.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            A description of the error, suitable for
            human consumption. Required.
        field_path (str):
            The path, in RFC 8901 JSON Pointer format, to
            the field that failed validation. This may be
            left empty if no specific field is affected.
        start (google.cloud.securitycenter_v1.types.Position):
            The initial position of the error in the
            uploaded text version of the module. This field
            may be omitted if no specific position applies,
            or if one could not be computed.

            This field is a member of `oneof`_ ``_start``.
        end (google.cloud.securitycenter_v1.types.Position):
            The end position of the error in the uploaded
            text version of the module. This field may be
            omitted if no specific position applies, or if
            one could not be computed..

            This field is a member of `oneof`_ ``_end``.
    """

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    field_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    start: "Position" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="Position",
    )
    end: "Position" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="Position",
    )


class Position(proto.Message):
    r"""A position in the uploaded text version of a module.

    Attributes:
        line_number (int):

        column_number (int):

    """

    line_number: int = proto.Field(
        proto.INT32,
        number=1,
    )
    column_number: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
