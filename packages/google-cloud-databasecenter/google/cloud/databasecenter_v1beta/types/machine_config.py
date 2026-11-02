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
        "MachineConfig",
    },
)


class MachineConfig(proto.Message):
    r"""MachineConfig describes the configuration of a machine
    specific to a Database Resource.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        memory_size_bytes (int):
            Memory size in bytes.
        shard_count (int):
            Optional. The number of Shards (if
            applicable).

            This field is a member of `oneof`_ ``_shard_count``.
        vcpu_count (float):
            Optional. The number of vCPUs (if
            applicable).

            This field is a member of `oneof`_ ``_vcpu_count``.
        baseline_slot_count (int):
            Optional. Baseline slots for BigQuery
            Reservations. Baseline slots are in increments
            of 50.

            This field is a member of `oneof`_ ``_baseline_slot_count``.
        max_reservation_slot_count (int):
            Optional. Max slots for BigQuery
            Reservations. Max slots are in increments of 50.

            This field is a member of `oneof`_ ``_max_reservation_slot_count``.
    """

    memory_size_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    shard_count: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    vcpu_count: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    baseline_slot_count: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    max_reservation_slot_count: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
