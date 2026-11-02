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

from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from google.identity.accesscontextmanager.v1 import (
    access_level_pb2 as _access_level_pb2,
)
from google.identity.accesscontextmanager.v1 import (
    access_policy_pb2 as _access_policy_pb2,
)
from google.identity.accesscontextmanager.v1 import (
    gcp_user_access_binding_pb2 as _gcp_user_access_binding_pb2,
)
from google.identity.accesscontextmanager.v1 import (
    service_perimeter_pb2 as _service_perimeter_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LevelFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEVEL_FORMAT_UNSPECIFIED: _ClassVar[LevelFormat]
    AS_DEFINED: _ClassVar[LevelFormat]
    CEL: _ClassVar[LevelFormat]

LEVEL_FORMAT_UNSPECIFIED: LevelFormat
AS_DEFINED: LevelFormat
CEL: LevelFormat

class ListAccessPoliciesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(
        self,
        parent: _Optional[str] = ...,
        page_size: _Optional[int] = ...,
        page_token: _Optional[str] = ...,
    ) -> None: ...

class ListAccessPoliciesResponse(_message.Message):
    __slots__ = ("access_policies", "next_page_token")
    ACCESS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_policies: _containers.RepeatedCompositeFieldContainer[
        _access_policy_pb2.AccessPolicy
    ]
    next_page_token: str
    def __init__(
        self,
        access_policies: _Optional[
            _Iterable[_Union[_access_policy_pb2.AccessPolicy, _Mapping]]
        ] = ...,
        next_page_token: _Optional[str] = ...,
    ) -> None: ...

class GetAccessPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAccessPolicyRequest(_message.Message):
    __slots__ = ("policy", "update_mask")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    policy: _access_policy_pb2.AccessPolicy
    update_mask: _field_mask_pb2.FieldMask
    def __init__(
        self,
        policy: _Optional[_Union[_access_policy_pb2.AccessPolicy, _Mapping]] = ...,
        update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...,
    ) -> None: ...

class DeleteAccessPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccessLevelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "access_level_format")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    access_level_format: LevelFormat
    def __init__(
        self,
        parent: _Optional[str] = ...,
        page_size: _Optional[int] = ...,
        page_token: _Optional[str] = ...,
        access_level_format: _Optional[_Union[LevelFormat, str]] = ...,
    ) -> None: ...

class ListAccessLevelsResponse(_message.Message):
    __slots__ = ("access_levels", "next_page_token")
    ACCESS_LEVELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_levels: _containers.RepeatedCompositeFieldContainer[
        _access_level_pb2.AccessLevel
    ]
    next_page_token: str
    def __init__(
        self,
        access_levels: _Optional[
            _Iterable[_Union[_access_level_pb2.AccessLevel, _Mapping]]
        ] = ...,
        next_page_token: _Optional[str] = ...,
    ) -> None: ...

class GetAccessLevelRequest(_message.Message):
    __slots__ = ("name", "access_level_format")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_level_format: LevelFormat
    def __init__(
        self,
        name: _Optional[str] = ...,
        access_level_format: _Optional[_Union[LevelFormat, str]] = ...,
    ) -> None: ...

class CreateAccessLevelRequest(_message.Message):
    __slots__ = ("parent", "access_level")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_level: _access_level_pb2.AccessLevel
    def __init__(
        self,
        parent: _Optional[str] = ...,
        access_level: _Optional[_Union[_access_level_pb2.AccessLevel, _Mapping]] = ...,
    ) -> None: ...

class UpdateAccessLevelRequest(_message.Message):
    __slots__ = ("access_level", "update_mask")
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    access_level: _access_level_pb2.AccessLevel
    update_mask: _field_mask_pb2.FieldMask
    def __init__(
        self,
        access_level: _Optional[_Union[_access_level_pb2.AccessLevel, _Mapping]] = ...,
        update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...,
    ) -> None: ...

class DeleteAccessLevelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReplaceAccessLevelsRequest(_message.Message):
    __slots__ = ("parent", "access_levels", "etag")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_levels: _containers.RepeatedCompositeFieldContainer[
        _access_level_pb2.AccessLevel
    ]
    etag: str
    def __init__(
        self,
        parent: _Optional[str] = ...,
        access_levels: _Optional[
            _Iterable[_Union[_access_level_pb2.AccessLevel, _Mapping]]
        ] = ...,
        etag: _Optional[str] = ...,
    ) -> None: ...

class ReplaceAccessLevelsResponse(_message.Message):
    __slots__ = ("access_levels",)
    ACCESS_LEVELS_FIELD_NUMBER: _ClassVar[int]
    access_levels: _containers.RepeatedCompositeFieldContainer[
        _access_level_pb2.AccessLevel
    ]
    def __init__(
        self,
        access_levels: _Optional[
            _Iterable[_Union[_access_level_pb2.AccessLevel, _Mapping]]
        ] = ...,
    ) -> None: ...

class ListServicePerimetersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(
        self,
        parent: _Optional[str] = ...,
        page_size: _Optional[int] = ...,
        page_token: _Optional[str] = ...,
    ) -> None: ...

class ListServicePerimetersResponse(_message.Message):
    __slots__ = ("service_perimeters", "next_page_token")
    SERVICE_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_perimeters: _containers.RepeatedCompositeFieldContainer[
        _service_perimeter_pb2.ServicePerimeter
    ]
    next_page_token: str
    def __init__(
        self,
        service_perimeters: _Optional[
            _Iterable[_Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]]
        ] = ...,
        next_page_token: _Optional[str] = ...,
    ) -> None: ...

class GetServicePerimeterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateServicePerimeterRequest(_message.Message):
    __slots__ = ("parent", "service_perimeter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_perimeter: _service_perimeter_pb2.ServicePerimeter
    def __init__(
        self,
        parent: _Optional[str] = ...,
        service_perimeter: _Optional[
            _Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateServicePerimeterRequest(_message.Message):
    __slots__ = ("service_perimeter", "update_mask")
    SERVICE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    service_perimeter: _service_perimeter_pb2.ServicePerimeter
    update_mask: _field_mask_pb2.FieldMask
    def __init__(
        self,
        service_perimeter: _Optional[
            _Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]
        ] = ...,
        update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...,
    ) -> None: ...

class DeleteServicePerimeterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReplaceServicePerimetersRequest(_message.Message):
    __slots__ = ("parent", "service_perimeters", "etag")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_perimeters: _containers.RepeatedCompositeFieldContainer[
        _service_perimeter_pb2.ServicePerimeter
    ]
    etag: str
    def __init__(
        self,
        parent: _Optional[str] = ...,
        service_perimeters: _Optional[
            _Iterable[_Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]]
        ] = ...,
        etag: _Optional[str] = ...,
    ) -> None: ...

class ReplaceServicePerimetersResponse(_message.Message):
    __slots__ = ("service_perimeters",)
    SERVICE_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    service_perimeters: _containers.RepeatedCompositeFieldContainer[
        _service_perimeter_pb2.ServicePerimeter
    ]
    def __init__(
        self,
        service_perimeters: _Optional[
            _Iterable[_Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]]
        ] = ...,
    ) -> None: ...

class CommitServicePerimetersRequest(_message.Message):
    __slots__ = ("parent", "etag")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    etag: str
    def __init__(
        self, parent: _Optional[str] = ..., etag: _Optional[str] = ...
    ) -> None: ...

class CommitServicePerimetersResponse(_message.Message):
    __slots__ = ("service_perimeters",)
    SERVICE_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    service_perimeters: _containers.RepeatedCompositeFieldContainer[
        _service_perimeter_pb2.ServicePerimeter
    ]
    def __init__(
        self,
        service_perimeters: _Optional[
            _Iterable[_Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]]
        ] = ...,
    ) -> None: ...

class ListGcpUserAccessBindingsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(
        self,
        parent: _Optional[str] = ...,
        page_size: _Optional[int] = ...,
        page_token: _Optional[str] = ...,
    ) -> None: ...

class ListGcpUserAccessBindingsResponse(_message.Message):
    __slots__ = ("gcp_user_access_bindings", "next_page_token")
    GCP_USER_ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gcp_user_access_bindings: _containers.RepeatedCompositeFieldContainer[
        _gcp_user_access_binding_pb2.GcpUserAccessBinding
    ]
    next_page_token: str
    def __init__(
        self,
        gcp_user_access_bindings: _Optional[
            _Iterable[
                _Union[_gcp_user_access_binding_pb2.GcpUserAccessBinding, _Mapping]
            ]
        ] = ...,
        next_page_token: _Optional[str] = ...,
    ) -> None: ...

class GetGcpUserAccessBindingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateGcpUserAccessBindingRequest(_message.Message):
    __slots__ = ("parent", "gcp_user_access_binding")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GCP_USER_ACCESS_BINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gcp_user_access_binding: _gcp_user_access_binding_pb2.GcpUserAccessBinding
    def __init__(
        self,
        parent: _Optional[str] = ...,
        gcp_user_access_binding: _Optional[
            _Union[_gcp_user_access_binding_pb2.GcpUserAccessBinding, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateGcpUserAccessBindingRequest(_message.Message):
    __slots__ = ("gcp_user_access_binding", "update_mask")
    GCP_USER_ACCESS_BINDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    gcp_user_access_binding: _gcp_user_access_binding_pb2.GcpUserAccessBinding
    update_mask: _field_mask_pb2.FieldMask
    def __init__(
        self,
        gcp_user_access_binding: _Optional[
            _Union[_gcp_user_access_binding_pb2.GcpUserAccessBinding, _Mapping]
        ] = ...,
        update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...,
    ) -> None: ...

class DeleteGcpUserAccessBindingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GcpUserAccessBindingOperationMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessContextManagerOperationMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
