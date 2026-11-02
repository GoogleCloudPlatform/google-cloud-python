# Copyright 2025 Google LLC
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

import datetime
from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = (
        "version",
        "constraint",
        "etag",
        "update_time",
        "list_policy",
        "boolean_policy",
        "restore_default",
    )
    class ListPolicy(_message.Message):
        __slots__ = (
            "allowed_values",
            "denied_values",
            "all_values",
            "suggested_value",
            "inherit_from_parent",
        )
        class AllValues(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ALL_VALUES_UNSPECIFIED: _ClassVar[Policy.ListPolicy.AllValues]
            ALLOW: _ClassVar[Policy.ListPolicy.AllValues]
            DENY: _ClassVar[Policy.ListPolicy.AllValues]

        ALL_VALUES_UNSPECIFIED: Policy.ListPolicy.AllValues
        ALLOW: Policy.ListPolicy.AllValues
        DENY: Policy.ListPolicy.AllValues
        ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
        DENIED_VALUES_FIELD_NUMBER: _ClassVar[int]
        ALL_VALUES_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_VALUE_FIELD_NUMBER: _ClassVar[int]
        INHERIT_FROM_PARENT_FIELD_NUMBER: _ClassVar[int]
        allowed_values: _containers.RepeatedScalarFieldContainer[str]
        denied_values: _containers.RepeatedScalarFieldContainer[str]
        all_values: Policy.ListPolicy.AllValues
        suggested_value: str
        inherit_from_parent: bool
        def __init__(
            self,
            allowed_values: _Optional[_Iterable[str]] = ...,
            denied_values: _Optional[_Iterable[str]] = ...,
            all_values: _Optional[_Union[Policy.ListPolicy.AllValues, str]] = ...,
            suggested_value: _Optional[str] = ...,
            inherit_from_parent: _Optional[bool] = ...,
        ) -> None: ...

    class BooleanPolicy(_message.Message):
        __slots__ = ("enforced",)
        ENFORCED_FIELD_NUMBER: _ClassVar[int]
        enforced: bool
        def __init__(self, enforced: _Optional[bool] = ...) -> None: ...

    class RestoreDefault(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LIST_POLICY_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_POLICY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    version: int
    constraint: str
    etag: bytes
    update_time: _timestamp_pb2.Timestamp
    list_policy: Policy.ListPolicy
    boolean_policy: Policy.BooleanPolicy
    restore_default: Policy.RestoreDefault
    def __init__(
        self,
        version: _Optional[int] = ...,
        constraint: _Optional[str] = ...,
        etag: _Optional[bytes] = ...,
        update_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        list_policy: _Optional[_Union[Policy.ListPolicy, _Mapping]] = ...,
        boolean_policy: _Optional[_Union[Policy.BooleanPolicy, _Mapping]] = ...,
        restore_default: _Optional[_Union[Policy.RestoreDefault, _Mapping]] = ...,
    ) -> None: ...
