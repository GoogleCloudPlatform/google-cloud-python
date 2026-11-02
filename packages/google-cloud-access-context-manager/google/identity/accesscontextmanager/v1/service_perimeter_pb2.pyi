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

DESCRIPTOR: _descriptor.FileDescriptor

class ServicePerimeter(_message.Message):
    __slots__ = (
        "name",
        "title",
        "description",
        "create_time",
        "update_time",
        "perimeter_type",
        "status",
        "spec",
        "use_explicit_dry_run_spec",
    )
    class PerimeterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERIMETER_TYPE_REGULAR: _ClassVar[ServicePerimeter.PerimeterType]
        PERIMETER_TYPE_BRIDGE: _ClassVar[ServicePerimeter.PerimeterType]

    PERIMETER_TYPE_REGULAR: ServicePerimeter.PerimeterType
    PERIMETER_TYPE_BRIDGE: ServicePerimeter.PerimeterType
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    USE_EXPLICIT_DRY_RUN_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    perimeter_type: ServicePerimeter.PerimeterType
    status: ServicePerimeterConfig
    spec: ServicePerimeterConfig
    use_explicit_dry_run_spec: bool
    def __init__(
        self,
        name: _Optional[str] = ...,
        title: _Optional[str] = ...,
        description: _Optional[str] = ...,
        create_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        update_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        perimeter_type: _Optional[_Union[ServicePerimeter.PerimeterType, str]] = ...,
        status: _Optional[_Union[ServicePerimeterConfig, _Mapping]] = ...,
        spec: _Optional[_Union[ServicePerimeterConfig, _Mapping]] = ...,
        use_explicit_dry_run_spec: _Optional[bool] = ...,
    ) -> None: ...

class ServicePerimeterConfig(_message.Message):
    __slots__ = (
        "resources",
        "access_levels",
        "restricted_services",
        "vpc_accessible_services",
        "ingress_policies",
        "egress_policies",
    )
    class IdentityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDENTITY_TYPE_UNSPECIFIED: _ClassVar[ServicePerimeterConfig.IdentityType]
        ANY_IDENTITY: _ClassVar[ServicePerimeterConfig.IdentityType]
        ANY_USER_ACCOUNT: _ClassVar[ServicePerimeterConfig.IdentityType]
        ANY_SERVICE_ACCOUNT: _ClassVar[ServicePerimeterConfig.IdentityType]

    IDENTITY_TYPE_UNSPECIFIED: ServicePerimeterConfig.IdentityType
    ANY_IDENTITY: ServicePerimeterConfig.IdentityType
    ANY_USER_ACCOUNT: ServicePerimeterConfig.IdentityType
    ANY_SERVICE_ACCOUNT: ServicePerimeterConfig.IdentityType
    class VpcAccessibleServices(_message.Message):
        __slots__ = ("enable_restriction", "allowed_services")
        ENABLE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_SERVICES_FIELD_NUMBER: _ClassVar[int]
        enable_restriction: bool
        allowed_services: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            enable_restriction: _Optional[bool] = ...,
            allowed_services: _Optional[_Iterable[str]] = ...,
        ) -> None: ...

    class MethodSelector(_message.Message):
        __slots__ = ("method", "permission")
        METHOD_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        method: str
        permission: str
        def __init__(
            self, method: _Optional[str] = ..., permission: _Optional[str] = ...
        ) -> None: ...

    class ApiOperation(_message.Message):
        __slots__ = ("service_name", "method_selectors")
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        METHOD_SELECTORS_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        method_selectors: _containers.RepeatedCompositeFieldContainer[
            ServicePerimeterConfig.MethodSelector
        ]
        def __init__(
            self,
            service_name: _Optional[str] = ...,
            method_selectors: _Optional[
                _Iterable[_Union[ServicePerimeterConfig.MethodSelector, _Mapping]]
            ] = ...,
        ) -> None: ...

    class IngressSource(_message.Message):
        __slots__ = ("access_level", "resource")
        ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        access_level: str
        resource: str
        def __init__(
            self, access_level: _Optional[str] = ..., resource: _Optional[str] = ...
        ) -> None: ...

    class IngressFrom(_message.Message):
        __slots__ = ("sources", "identities", "identity_type")
        SOURCES_FIELD_NUMBER: _ClassVar[int]
        IDENTITIES_FIELD_NUMBER: _ClassVar[int]
        IDENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        sources: _containers.RepeatedCompositeFieldContainer[
            ServicePerimeterConfig.IngressSource
        ]
        identities: _containers.RepeatedScalarFieldContainer[str]
        identity_type: ServicePerimeterConfig.IdentityType
        def __init__(
            self,
            sources: _Optional[
                _Iterable[_Union[ServicePerimeterConfig.IngressSource, _Mapping]]
            ] = ...,
            identities: _Optional[_Iterable[str]] = ...,
            identity_type: _Optional[
                _Union[ServicePerimeterConfig.IdentityType, str]
            ] = ...,
        ) -> None: ...

    class IngressTo(_message.Message):
        __slots__ = ("operations", "resources")
        OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        operations: _containers.RepeatedCompositeFieldContainer[
            ServicePerimeterConfig.ApiOperation
        ]
        resources: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            operations: _Optional[
                _Iterable[_Union[ServicePerimeterConfig.ApiOperation, _Mapping]]
            ] = ...,
            resources: _Optional[_Iterable[str]] = ...,
        ) -> None: ...

    class IngressPolicy(_message.Message):
        __slots__ = ("ingress_from", "ingress_to")
        INGRESS_FROM_FIELD_NUMBER: _ClassVar[int]
        INGRESS_TO_FIELD_NUMBER: _ClassVar[int]
        ingress_from: ServicePerimeterConfig.IngressFrom
        ingress_to: ServicePerimeterConfig.IngressTo
        def __init__(
            self,
            ingress_from: _Optional[
                _Union[ServicePerimeterConfig.IngressFrom, _Mapping]
            ] = ...,
            ingress_to: _Optional[
                _Union[ServicePerimeterConfig.IngressTo, _Mapping]
            ] = ...,
        ) -> None: ...

    class EgressFrom(_message.Message):
        __slots__ = ("identities", "identity_type")
        IDENTITIES_FIELD_NUMBER: _ClassVar[int]
        IDENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        identities: _containers.RepeatedScalarFieldContainer[str]
        identity_type: ServicePerimeterConfig.IdentityType
        def __init__(
            self,
            identities: _Optional[_Iterable[str]] = ...,
            identity_type: _Optional[
                _Union[ServicePerimeterConfig.IdentityType, str]
            ] = ...,
        ) -> None: ...

    class EgressTo(_message.Message):
        __slots__ = ("resources", "operations", "external_resources")
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        resources: _containers.RepeatedScalarFieldContainer[str]
        operations: _containers.RepeatedCompositeFieldContainer[
            ServicePerimeterConfig.ApiOperation
        ]
        external_resources: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            resources: _Optional[_Iterable[str]] = ...,
            operations: _Optional[
                _Iterable[_Union[ServicePerimeterConfig.ApiOperation, _Mapping]]
            ] = ...,
            external_resources: _Optional[_Iterable[str]] = ...,
        ) -> None: ...

    class EgressPolicy(_message.Message):
        __slots__ = ("egress_from", "egress_to")
        EGRESS_FROM_FIELD_NUMBER: _ClassVar[int]
        EGRESS_TO_FIELD_NUMBER: _ClassVar[int]
        egress_from: ServicePerimeterConfig.EgressFrom
        egress_to: ServicePerimeterConfig.EgressTo
        def __init__(
            self,
            egress_from: _Optional[
                _Union[ServicePerimeterConfig.EgressFrom, _Mapping]
            ] = ...,
            egress_to: _Optional[
                _Union[ServicePerimeterConfig.EgressTo, _Mapping]
            ] = ...,
        ) -> None: ...

    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVELS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    VPC_ACCESSIBLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
    INGRESS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    EGRESS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedScalarFieldContainer[str]
    access_levels: _containers.RepeatedScalarFieldContainer[str]
    restricted_services: _containers.RepeatedScalarFieldContainer[str]
    vpc_accessible_services: ServicePerimeterConfig.VpcAccessibleServices
    ingress_policies: _containers.RepeatedCompositeFieldContainer[
        ServicePerimeterConfig.IngressPolicy
    ]
    egress_policies: _containers.RepeatedCompositeFieldContainer[
        ServicePerimeterConfig.EgressPolicy
    ]
    def __init__(
        self,
        resources: _Optional[_Iterable[str]] = ...,
        access_levels: _Optional[_Iterable[str]] = ...,
        restricted_services: _Optional[_Iterable[str]] = ...,
        vpc_accessible_services: _Optional[
            _Union[ServicePerimeterConfig.VpcAccessibleServices, _Mapping]
        ] = ...,
        ingress_policies: _Optional[
            _Iterable[_Union[ServicePerimeterConfig.IngressPolicy, _Mapping]]
        ] = ...,
        egress_policies: _Optional[
            _Iterable[_Union[ServicePerimeterConfig.EgressPolicy, _Mapping]]
        ] = ...,
    ) -> None: ...
