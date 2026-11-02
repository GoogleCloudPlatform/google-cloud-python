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
    package="google.backstory",
    manifest={
        "DataAccessIngestionLabel",
        "DataAccessLabels",
    },
)


class DataAccessIngestionLabel(proto.Message):
    r"""Label used in data access for ingestion.

    Attributes:
        key (str):
            The key.
        value (str):
            The value.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DataAccessLabels(proto.Message):
    r"""Label used in data access.

    Attributes:
        log_types (MutableSequence[str]):
            All the LogType labels.
        ingestion_labels (MutableSequence[str]):
            All the ingestion labels.
        namespaces (MutableSequence[str]):
            All the namespaces.
        custom_labels (MutableSequence[str]):
            All the complex labels (UDM search syntax
            based).
        ingestion_kv_labels (MutableSequence[google.backstory.types.DataAccessIngestionLabel]):
            All the ingestion labels (key/value pairs).
        allow_scoped_access (bool):
            Are the labels ready for scoped access
    """

    log_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    ingestion_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    namespaces: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    custom_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    ingestion_kv_labels: MutableSequence["DataAccessIngestionLabel"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="DataAccessIngestionLabel",
        )
    )
    allow_scoped_access: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
