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

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Transport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSPORT_UNSPECIFIED: _ClassVar[Transport]
    JSON: _ClassVar[Transport]
    GRPC: _ClassVar[Transport]

TRANSPORT_UNSPECIFIED: Transport
JSON: Transport
GRPC: Transport

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    def __init__(self, payload: _Optional[bytes] = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    def __init__(self, payload: _Optional[bytes] = ...) -> None: ...

class ObjectMeta(_message.Message):
    __slots__ = (
        "size",
        "generation",
        "metageneration",
        "content_type",
        "content_encoding",
        "crc32c",
    )
    SIZE_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    size: int
    generation: int
    metageneration: int
    content_type: str
    content_encoding: str
    crc32c: int
    def __init__(
        self,
        size: _Optional[int] = ...,
        generation: _Optional[int] = ...,
        metageneration: _Optional[int] = ...,
        content_type: _Optional[str] = ...,
        content_encoding: _Optional[str] = ...,
        crc32c: _Optional[int] = ...,
    ) -> None: ...

class ReadObjectRequest(_message.Message):
    __slots__ = (
        "bucket",
        "object",
        "offset",
        "length",
        "generation",
        "if_generation_match",
        "transport",
        "chunk_size",
    )
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    offset: int
    length: int
    generation: int
    if_generation_match: int
    transport: Transport
    chunk_size: int
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        object: _Optional[str] = ...,
        offset: _Optional[int] = ...,
        length: _Optional[int] = ...,
        generation: _Optional[int] = ...,
        if_generation_match: _Optional[int] = ...,
        transport: _Optional[_Union[Transport, str]] = ...,
        chunk_size: _Optional[int] = ...,
    ) -> None: ...

class ReadChunk(_message.Message):
    __slots__ = ("data", "meta")
    DATA_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[bytes]
    meta: ObjectMeta
    def __init__(
        self,
        data: _Optional[_Iterable[bytes]] = ...,
        meta: _Optional[_Union[ObjectMeta, _Mapping]] = ...,
    ) -> None: ...

class ReadObjectShmRequest(_message.Message):
    __slots__ = ("read", "region", "base_offset", "capacity")
    READ_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    BASE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    read: ReadObjectRequest
    region: int
    base_offset: int
    capacity: int
    def __init__(
        self,
        read: _Optional[_Union[ReadObjectRequest, _Mapping]] = ...,
        region: _Optional[int] = ...,
        base_offset: _Optional[int] = ...,
        capacity: _Optional[int] = ...,
    ) -> None: ...

class ShmChunk(_message.Message):
    __slots__ = ("offset", "len", "meta")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    offset: int
    len: int
    meta: ObjectMeta
    def __init__(
        self,
        offset: _Optional[int] = ...,
        len: _Optional[int] = ...,
        meta: _Optional[_Union[ObjectMeta, _Mapping]] = ...,
    ) -> None: ...

class OpenObjectRequest(_message.Message):
    __slots__ = ("bucket", "object", "generation")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        object: _Optional[str] = ...,
        generation: _Optional[int] = ...,
    ) -> None: ...

class OpenObjectResponse(_message.Message):
    __slots__ = ("handle", "meta")
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    handle: int
    meta: ObjectMeta
    def __init__(
        self,
        handle: _Optional[int] = ...,
        meta: _Optional[_Union[ObjectMeta, _Mapping]] = ...,
    ) -> None: ...

class ReadRangeRequest(_message.Message):
    __slots__ = ("handle", "offset", "length", "chunk_size")
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    handle: int
    offset: int
    length: int
    chunk_size: int
    def __init__(
        self,
        handle: _Optional[int] = ...,
        offset: _Optional[int] = ...,
        length: _Optional[int] = ...,
        chunk_size: _Optional[int] = ...,
    ) -> None: ...

class CloseObjectRequest(_message.Message):
    __slots__ = ("handle",)
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    handle: int
    def __init__(self, handle: _Optional[int] = ...) -> None: ...

class WriteHeader(_message.Message):
    __slots__ = (
        "bucket",
        "object",
        "content_type",
        "if_generation_match",
        "known_size",
        "chunk_size",
        "transport",
    )
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    KNOWN_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    content_type: str
    if_generation_match: int
    known_size: int
    chunk_size: int
    transport: Transport
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        object: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
        if_generation_match: _Optional[int] = ...,
        known_size: _Optional[int] = ...,
        chunk_size: _Optional[int] = ...,
        transport: _Optional[_Union[Transport, str]] = ...,
    ) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: WriteHeader
    data: bytes
    def __init__(
        self,
        header: _Optional[_Union[WriteHeader, _Mapping]] = ...,
        data: _Optional[bytes] = ...,
    ) -> None: ...

class WriteObjectResponse(_message.Message):
    __slots__ = ("size", "generation", "crc32c", "transport_used")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_USED_FIELD_NUMBER: _ClassVar[int]
    size: int
    generation: int
    crc32c: int
    transport_used: Transport
    def __init__(
        self,
        size: _Optional[int] = ...,
        generation: _Optional[int] = ...,
        crc32c: _Optional[int] = ...,
        transport_used: _Optional[_Union[Transport, str]] = ...,
    ) -> None: ...

class ListObjectsRequest(_message.Message):
    __slots__ = (
        "bucket",
        "prefix",
        "delimiter",
        "start_offset",
        "end_offset",
        "page_token",
        "page_size",
        "versions",
    )
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    prefix: str
    delimiter: str
    start_offset: str
    end_offset: str
    page_token: str
    page_size: int
    versions: bool
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        prefix: _Optional[str] = ...,
        delimiter: _Optional[str] = ...,
        start_offset: _Optional[str] = ...,
        end_offset: _Optional[str] = ...,
        page_token: _Optional[str] = ...,
        page_size: _Optional[int] = ...,
        versions: _Optional[bool] = ...,
    ) -> None: ...

class ListedObject(_message.Message):
    __slots__ = (
        "name",
        "size",
        "generation",
        "metageneration",
        "content_type",
        "storage_class",
        "updated_unix_secs",
        "crc32c",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_UNIX_SECS_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    generation: int
    metageneration: int
    content_type: str
    storage_class: str
    updated_unix_secs: int
    crc32c: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        size: _Optional[int] = ...,
        generation: _Optional[int] = ...,
        metageneration: _Optional[int] = ...,
        content_type: _Optional[str] = ...,
        storage_class: _Optional[str] = ...,
        updated_unix_secs: _Optional[int] = ...,
        crc32c: _Optional[int] = ...,
    ) -> None: ...

class ListObjectsResponse(_message.Message):
    __slots__ = ("items", "prefixes", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ListedObject]
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(
        self,
        items: _Optional[_Iterable[_Union[ListedObject, _Mapping]]] = ...,
        prefixes: _Optional[_Iterable[str]] = ...,
        next_page_token: _Optional[str] = ...,
    ) -> None: ...

class ListBucketsRequest(_message.Message):
    __slots__ = ("project", "prefix", "page_token", "page_size")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    project: str
    prefix: str
    page_token: str
    page_size: int
    def __init__(
        self,
        project: _Optional[str] = ...,
        prefix: _Optional[str] = ...,
        page_token: _Optional[str] = ...,
        page_size: _Optional[int] = ...,
    ) -> None: ...

class ListedBucket(_message.Message):
    __slots__ = (
        "name",
        "location",
        "storage_class",
        "metageneration",
        "created_unix_secs",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CREATED_UNIX_SECS_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: str
    storage_class: str
    metageneration: int
    created_unix_secs: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        location: _Optional[str] = ...,
        storage_class: _Optional[str] = ...,
        metageneration: _Optional[int] = ...,
        created_unix_secs: _Optional[int] = ...,
    ) -> None: ...

class ListBucketsResponse(_message.Message):
    __slots__ = ("items", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ListedBucket]
    next_page_token: str
    def __init__(
        self,
        items: _Optional[_Iterable[_Union[ListedBucket, _Mapping]]] = ...,
        next_page_token: _Optional[str] = ...,
    ) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = (
        "access_token",
        "expiry_unix_secs",
        "quota_project",
        "endpoint",
        "universe_domain",
        "anonymous",
    )
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_UNIX_SECS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UNIVERSE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expiry_unix_secs: int
    quota_project: str
    endpoint: str
    universe_domain: str
    anonymous: bool
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        expiry_unix_secs: _Optional[int] = ...,
        quota_project: _Optional[str] = ...,
        endpoint: _Optional[str] = ...,
        universe_domain: _Optional[str] = ...,
        anonymous: _Optional[bool] = ...,
    ) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class UpdateTokenRequest(_message.Message):
    __slots__ = ("session_id", "access_token", "expiry_unix_secs")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_UNIX_SECS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    access_token: str
    expiry_unix_secs: int
    def __init__(
        self,
        session_id: _Optional[str] = ...,
        access_token: _Optional[str] = ...,
        expiry_unix_secs: _Optional[int] = ...,
    ) -> None: ...

class SessionRef(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class StatsRequest(_message.Message):
    __slots__ = ("reset_peak_rss",)
    RESET_PEAK_RSS_FIELD_NUMBER: _ClassVar[int]
    reset_peak_rss: bool
    def __init__(self, reset_peak_rss: _Optional[bool] = ...) -> None: ...

class StatsResponse(_message.Message):
    __slots__ = (
        "pid",
        "cpu_user_secs",
        "cpu_sys_secs",
        "rss_bytes",
        "peak_rss_bytes",
        "threads",
        "uptime_ms",
        "rpcs_served",
    )
    PID_FIELD_NUMBER: _ClassVar[int]
    CPU_USER_SECS_FIELD_NUMBER: _ClassVar[int]
    CPU_SYS_SECS_FIELD_NUMBER: _ClassVar[int]
    RSS_BYTES_FIELD_NUMBER: _ClassVar[int]
    PEAK_RSS_BYTES_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    UPTIME_MS_FIELD_NUMBER: _ClassVar[int]
    RPCS_SERVED_FIELD_NUMBER: _ClassVar[int]
    pid: int
    cpu_user_secs: float
    cpu_sys_secs: float
    rss_bytes: int
    peak_rss_bytes: int
    threads: int
    uptime_ms: int
    rpcs_served: int
    def __init__(
        self,
        pid: _Optional[int] = ...,
        cpu_user_secs: _Optional[float] = ...,
        cpu_sys_secs: _Optional[float] = ...,
        rss_bytes: _Optional[int] = ...,
        peak_rss_bytes: _Optional[int] = ...,
        threads: _Optional[int] = ...,
        uptime_ms: _Optional[int] = ...,
        rpcs_served: _Optional[int] = ...,
    ) -> None: ...

class ServerInfo(_message.Message):
    __slots__ = (
        "server_version",
        "storage_crate_version",
        "features",
        "max_ranges_per_request",
        "shm_region_size",
        "shm_slot_size",
        "pid",
        "uid",
    )
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CRATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    MAX_RANGES_PER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SHM_REGION_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHM_SLOT_SIZE_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    server_version: str
    storage_crate_version: str
    features: _containers.RepeatedScalarFieldContainer[str]
    max_ranges_per_request: int
    shm_region_size: int
    shm_slot_size: int
    pid: int
    uid: int
    def __init__(
        self,
        server_version: _Optional[str] = ...,
        storage_crate_version: _Optional[str] = ...,
        features: _Optional[_Iterable[str]] = ...,
        max_ranges_per_request: _Optional[int] = ...,
        shm_region_size: _Optional[int] = ...,
        shm_slot_size: _Optional[int] = ...,
        pid: _Optional[int] = ...,
        uid: _Optional[int] = ...,
    ) -> None: ...

class ShmSlotRef(_message.Message):
    __slots__ = ("region_id", "slot", "length")
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    region_id: int
    slot: int
    length: int
    def __init__(
        self,
        region_id: _Optional[int] = ...,
        slot: _Optional[int] = ...,
        length: _Optional[int] = ...,
    ) -> None: ...

class ObjectResource(_message.Message):
    __slots__ = (
        "bucket",
        "name",
        "generation",
        "metageneration",
        "size",
        "storage_class",
        "etag",
        "content_type",
        "content_encoding",
        "finalized",
        "crc32c",
        "md5_hash",
        "metadata",
        "kms_key",
        "object_json",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    BUCKET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    MD5_HASH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_JSON_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    name: str
    generation: int
    metageneration: int
    size: int
    storage_class: str
    etag: str
    content_type: str
    content_encoding: str
    finalized: bool
    crc32c: int
    md5_hash: bytes
    metadata: _containers.ScalarMap[str, str]
    kms_key: str
    object_json: str
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        name: _Optional[str] = ...,
        generation: _Optional[int] = ...,
        metageneration: _Optional[int] = ...,
        size: _Optional[int] = ...,
        storage_class: _Optional[str] = ...,
        etag: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
        content_encoding: _Optional[str] = ...,
        finalized: _Optional[bool] = ...,
        crc32c: _Optional[int] = ...,
        md5_hash: _Optional[bytes] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
        kms_key: _Optional[str] = ...,
        object_json: _Optional[str] = ...,
    ) -> None: ...

class ObjectAttrs(_message.Message):
    __slots__ = (
        "storage_class",
        "content_type",
        "content_encoding",
        "content_language",
        "content_disposition",
        "cache_control",
        "metadata",
        "kms_key",
        "custom_time_secs",
        "contexts_json",
        "custom_time_nanos",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTS_JSON_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TIME_NANOS_FIELD_NUMBER: _ClassVar[int]
    storage_class: str
    content_type: str
    content_encoding: str
    content_language: str
    content_disposition: str
    cache_control: str
    metadata: _containers.ScalarMap[str, str]
    kms_key: str
    custom_time_secs: int
    contexts_json: bytes
    custom_time_nanos: int
    def __init__(
        self,
        storage_class: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
        content_encoding: _Optional[str] = ...,
        content_language: _Optional[str] = ...,
        content_disposition: _Optional[str] = ...,
        cache_control: _Optional[str] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
        kms_key: _Optional[str] = ...,
        custom_time_secs: _Optional[int] = ...,
        contexts_json: _Optional[bytes] = ...,
        custom_time_nanos: _Optional[int] = ...,
    ) -> None: ...

class BidiReadObjectRequest(_message.Message):
    __slots__ = ("open", "read", "release", "cancel")
    OPEN_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    open: OpenReadSpec
    read: ReadRanges
    release: ReleaseSlots
    cancel: CancelRanges
    def __init__(
        self,
        open: _Optional[_Union[OpenReadSpec, _Mapping]] = ...,
        read: _Optional[_Union[ReadRanges, _Mapping]] = ...,
        release: _Optional[_Union[ReleaseSlots, _Mapping]] = ...,
        cancel: _Optional[_Union[CancelRanges, _Mapping]] = ...,
    ) -> None: ...

class OpenReadSpec(_message.Message):
    __slots__ = (
        "bucket",
        "object",
        "generation",
        "if_generation_match",
        "if_generation_not_match",
        "if_metageneration_match",
        "if_metageneration_not_match",
        "read_region_id",
        "compute_full_crc32c",
        "read_handle",
        "quota_project",
        "user_agent",
    )
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    READ_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FULL_CRC32C_FIELD_NUMBER: _ClassVar[int]
    READ_HANDLE_FIELD_NUMBER: _ClassVar[int]
    QUOTA_PROJECT_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    read_region_id: int
    compute_full_crc32c: bool
    read_handle: bytes
    quota_project: str
    user_agent: str
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        object: _Optional[str] = ...,
        generation: _Optional[int] = ...,
        if_generation_match: _Optional[int] = ...,
        if_generation_not_match: _Optional[int] = ...,
        if_metageneration_match: _Optional[int] = ...,
        if_metageneration_not_match: _Optional[int] = ...,
        read_region_id: _Optional[int] = ...,
        compute_full_crc32c: _Optional[bool] = ...,
        read_handle: _Optional[bytes] = ...,
        quota_project: _Optional[str] = ...,
        user_agent: _Optional[str] = ...,
    ) -> None: ...

class RangeSpec(_message.Message):
    __slots__ = ("range_id", "offset", "length")
    RANGE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    range_id: int
    offset: int
    length: int
    def __init__(
        self,
        range_id: _Optional[int] = ...,
        offset: _Optional[int] = ...,
        length: _Optional[int] = ...,
    ) -> None: ...

class ReadRanges(_message.Message):
    __slots__ = ("ranges",)
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[RangeSpec]
    def __init__(
        self, ranges: _Optional[_Iterable[_Union[RangeSpec, _Mapping]]] = ...
    ) -> None: ...

class ReleaseSlots(_message.Message):
    __slots__ = ("slots",)
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, slots: _Optional[_Iterable[int]] = ...) -> None: ...

class CancelRanges(_message.Message):
    __slots__ = ("range_ids",)
    RANGE_IDS_FIELD_NUMBER: _ClassVar[int]
    range_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, range_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class BidiReadObjectResponse(_message.Message):
    __slots__ = ("opened", "data", "range_error")
    OPENED_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RANGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    opened: ReadOpened
    data: RangeData
    range_error: RangeError
    def __init__(
        self,
        opened: _Optional[_Union[ReadOpened, _Mapping]] = ...,
        data: _Optional[_Union[RangeData, _Mapping]] = ...,
        range_error: _Optional[_Union[RangeError, _Mapping]] = ...,
    ) -> None: ...

class ReadOpened(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: ObjectResource
    def __init__(
        self, object: _Optional[_Union[ObjectResource, _Mapping]] = ...
    ) -> None: ...

class RangeData(_message.Message):
    __slots__ = ("range_id", "range_offset", "slot", "inline_data", "range_end")
    RANGE_ID_FIELD_NUMBER: _ClassVar[int]
    RANGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    range_id: int
    range_offset: int
    slot: ShmSlotRef
    inline_data: bytes
    range_end: bool
    def __init__(
        self,
        range_id: _Optional[int] = ...,
        range_offset: _Optional[int] = ...,
        slot: _Optional[_Union[ShmSlotRef, _Mapping]] = ...,
        inline_data: _Optional[bytes] = ...,
        range_end: _Optional[bool] = ...,
    ) -> None: ...

class RangeError(_message.Message):
    __slots__ = ("range_id", "code", "message", "checksum_mismatch")
    RANGE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_MISMATCH_FIELD_NUMBER: _ClassVar[int]
    range_id: int
    code: int
    message: str
    checksum_mismatch: bool
    def __init__(
        self,
        range_id: _Optional[int] = ...,
        code: _Optional[int] = ...,
        message: _Optional[str] = ...,
        checksum_mismatch: _Optional[bool] = ...,
    ) -> None: ...

class BidiWriteObjectRequest(_message.Message):
    __slots__ = ("open", "append", "flush", "close", "finalize", "op_id")
    OPEN_FIELD_NUMBER: _ClassVar[int]
    APPEND_FIELD_NUMBER: _ClassVar[int]
    FLUSH_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_FIELD_NUMBER: _ClassVar[int]
    OP_ID_FIELD_NUMBER: _ClassVar[int]
    open: OpenAppendSpec
    append: Append
    flush: Flush
    close: Close
    finalize: Finalize
    op_id: int
    def __init__(
        self,
        open: _Optional[_Union[OpenAppendSpec, _Mapping]] = ...,
        append: _Optional[_Union[Append, _Mapping]] = ...,
        flush: _Optional[_Union[Flush, _Mapping]] = ...,
        close: _Optional[_Union[Close, _Mapping]] = ...,
        finalize: _Optional[_Union[Finalize, _Mapping]] = ...,
        op_id: _Optional[int] = ...,
    ) -> None: ...

class OpenAppendSpec(_message.Message):
    __slots__ = (
        "bucket",
        "object",
        "reopen_generation",
        "if_generation_match",
        "if_metageneration_match",
        "if_metageneration_not_match",
        "write_handle",
        "routing_token",
        "attrs",
        "write_region_id",
        "quota_project",
        "if_generation_not_match",
        "user_agent",
    )
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    REOPEN_GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    WRITE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    WRITE_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    QUOTA_PROJECT_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    reopen_generation: int
    if_generation_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    write_handle: bytes
    routing_token: str
    attrs: ObjectAttrs
    write_region_id: int
    quota_project: str
    if_generation_not_match: int
    user_agent: str
    def __init__(
        self,
        bucket: _Optional[str] = ...,
        object: _Optional[str] = ...,
        reopen_generation: _Optional[int] = ...,
        if_generation_match: _Optional[int] = ...,
        if_metageneration_match: _Optional[int] = ...,
        if_metageneration_not_match: _Optional[int] = ...,
        write_handle: _Optional[bytes] = ...,
        routing_token: _Optional[str] = ...,
        attrs: _Optional[_Union[ObjectAttrs, _Mapping]] = ...,
        write_region_id: _Optional[int] = ...,
        quota_project: _Optional[str] = ...,
        if_generation_not_match: _Optional[int] = ...,
        user_agent: _Optional[str] = ...,
    ) -> None: ...

class Append(_message.Message):
    __slots__ = ("slot", "inline_data")
    SLOT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    slot: ShmSlotRef
    inline_data: bytes
    def __init__(
        self,
        slot: _Optional[_Union[ShmSlotRef, _Mapping]] = ...,
        inline_data: _Optional[bytes] = ...,
    ) -> None: ...

class Flush(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Close(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Finalize(_message.Message):
    __slots__ = ("full_object_crc32c",)
    FULL_OBJECT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    full_object_crc32c: int
    def __init__(self, full_object_crc32c: _Optional[int] = ...) -> None: ...

class BidiWriteObjectResponse(_message.Message):
    __slots__ = ("opened", "released", "flushed", "closed", "finalized", "op_id")
    OPENED_FIELD_NUMBER: _ClassVar[int]
    RELEASED_FIELD_NUMBER: _ClassVar[int]
    FLUSHED_FIELD_NUMBER: _ClassVar[int]
    CLOSED_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_FIELD_NUMBER: _ClassVar[int]
    OP_ID_FIELD_NUMBER: _ClassVar[int]
    opened: WriteOpened
    released: SlotsReleased
    flushed: Flushed
    closed: Closed
    finalized: Finalized
    op_id: int
    def __init__(
        self,
        opened: _Optional[_Union[WriteOpened, _Mapping]] = ...,
        released: _Optional[_Union[SlotsReleased, _Mapping]] = ...,
        flushed: _Optional[_Union[Flushed, _Mapping]] = ...,
        closed: _Optional[_Union[Closed, _Mapping]] = ...,
        finalized: _Optional[_Union[Finalized, _Mapping]] = ...,
        op_id: _Optional[int] = ...,
    ) -> None: ...

class WriteOpened(_message.Message):
    __slots__ = ("generation", "persisted_size")
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    PERSISTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    generation: int
    persisted_size: int
    def __init__(
        self, generation: _Optional[int] = ..., persisted_size: _Optional[int] = ...
    ) -> None: ...

class SlotsReleased(_message.Message):
    __slots__ = ("slots",)
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, slots: _Optional[_Iterable[int]] = ...) -> None: ...

class Flushed(_message.Message):
    __slots__ = ("persisted_size",)
    PERSISTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    persisted_size: int
    def __init__(self, persisted_size: _Optional[int] = ...) -> None: ...

class Closed(_message.Message):
    __slots__ = ("persisted_size",)
    PERSISTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    persisted_size: int
    def __init__(self, persisted_size: _Optional[int] = ...) -> None: ...

class Finalized(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: ObjectResource
    def __init__(
        self, object: _Optional[_Union[ObjectResource, _Mapping]] = ...
    ) -> None: ...
