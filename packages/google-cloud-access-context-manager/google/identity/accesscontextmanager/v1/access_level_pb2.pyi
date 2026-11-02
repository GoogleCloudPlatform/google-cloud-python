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

from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.type import expr_pb2 as _expr_pb2

from google.identity.accesscontextmanager.type import (
    device_resources_pb2 as _device_resources_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AccessLevel(_message.Message):
    __slots__ = (
        "name",
        "title",
        "description",
        "basic",
        "custom",
        "create_time",
        "update_time",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    basic: BasicLevel
    custom: CustomLevel
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        name: _Optional[str] = ...,
        title: _Optional[str] = ...,
        description: _Optional[str] = ...,
        basic: _Optional[_Union[BasicLevel, _Mapping]] = ...,
        custom: _Optional[_Union[CustomLevel, _Mapping]] = ...,
        create_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        update_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class BasicLevel(_message.Message):
    __slots__ = ("conditions", "combining_function")
    class ConditionCombiningFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AND: _ClassVar[BasicLevel.ConditionCombiningFunction]
        OR: _ClassVar[BasicLevel.ConditionCombiningFunction]

    AND: BasicLevel.ConditionCombiningFunction
    OR: BasicLevel.ConditionCombiningFunction
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    COMBINING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    combining_function: BasicLevel.ConditionCombiningFunction
    def __init__(
        self,
        conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...,
        combining_function: _Optional[
            _Union[BasicLevel.ConditionCombiningFunction, str]
        ] = ...,
    ) -> None: ...

class Condition(_message.Message):
    __slots__ = (
        "ip_subnetworks",
        "device_policy",
        "required_access_levels",
        "negate",
        "members",
        "regions",
    )
    IP_SUBNETWORKS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ACCESS_LEVELS_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    ip_subnetworks: _containers.RepeatedScalarFieldContainer[str]
    device_policy: DevicePolicy
    required_access_levels: _containers.RepeatedScalarFieldContainer[str]
    negate: bool
    members: _containers.RepeatedScalarFieldContainer[str]
    regions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        ip_subnetworks: _Optional[_Iterable[str]] = ...,
        device_policy: _Optional[_Union[DevicePolicy, _Mapping]] = ...,
        required_access_levels: _Optional[_Iterable[str]] = ...,
        negate: _Optional[bool] = ...,
        members: _Optional[_Iterable[str]] = ...,
        regions: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class CustomLevel(_message.Message):
    __slots__ = ("expr",)
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: _expr_pb2.Expr
    def __init__(
        self, expr: _Optional[_Union[_expr_pb2.Expr, _Mapping]] = ...
    ) -> None: ...

class DevicePolicy(_message.Message):
    __slots__ = (
        "require_screenlock",
        "allowed_encryption_statuses",
        "os_constraints",
        "allowed_device_management_levels",
        "require_admin_approval",
        "require_corp_owned",
    )
    REQUIRE_SCREENLOCK_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ENCRYPTION_STATUSES_FIELD_NUMBER: _ClassVar[int]
    OS_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DEVICE_MANAGEMENT_LEVELS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ADMIN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_CORP_OWNED_FIELD_NUMBER: _ClassVar[int]
    require_screenlock: bool
    allowed_encryption_statuses: _containers.RepeatedScalarFieldContainer[
        _device_resources_pb2.DeviceEncryptionStatus
    ]
    os_constraints: _containers.RepeatedCompositeFieldContainer[OsConstraint]
    allowed_device_management_levels: _containers.RepeatedScalarFieldContainer[
        _device_resources_pb2.DeviceManagementLevel
    ]
    require_admin_approval: bool
    require_corp_owned: bool
    def __init__(
        self,
        require_screenlock: _Optional[bool] = ...,
        allowed_encryption_statuses: _Optional[
            _Iterable[_Union[_device_resources_pb2.DeviceEncryptionStatus, str]]
        ] = ...,
        os_constraints: _Optional[_Iterable[_Union[OsConstraint, _Mapping]]] = ...,
        allowed_device_management_levels: _Optional[
            _Iterable[_Union[_device_resources_pb2.DeviceManagementLevel, str]]
        ] = ...,
        require_admin_approval: _Optional[bool] = ...,
        require_corp_owned: _Optional[bool] = ...,
    ) -> None: ...

class OsConstraint(_message.Message):
    __slots__ = ("os_type", "minimum_version", "require_verified_chrome_os")
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_VERIFIED_CHROME_OS_FIELD_NUMBER: _ClassVar[int]
    os_type: _device_resources_pb2.OsType
    minimum_version: str
    require_verified_chrome_os: bool
    def __init__(
        self,
        os_type: _Optional[_Union[_device_resources_pb2.OsType, str]] = ...,
        minimum_version: _Optional[str] = ...,
        require_verified_chrome_os: _Optional[bool] = ...,
    ) -> None: ...
