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

from google.cloud.oracledatabase_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DbSystemComputePerformance",
        "ComputePerformance",
        "ListDbSystemComputePerformancesRequest",
        "ListDbSystemComputePerformancesResponse",
    },
)


class DbSystemComputePerformance(proto.Message):
    r"""Details of the DbSystem compute performance resource.

    Attributes:
        name (str):
            Identifier. The name of the DbSystemComputePerformance
            resource with the format:
            projects/{project}/locations/{location}/dbSystemComputePerformances/{db_system_compute_performance}
        shape (str):
            Output only. The shape of the DB system.
        compute_performances (MutableSequence[google.cloud.oracledatabase_v1.types.ComputePerformance]):
            Output only. List of Compute performance
            details for the specified DB system shape.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shape: str = proto.Field(
        proto.STRING,
        number=2,
    )
    compute_performances: MutableSequence["ComputePerformance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ComputePerformance",
    )


class ComputePerformance(proto.Message):
    r"""Parameters detailing the compute performance for a specified
    DB system shape.

    Attributes:
        cpu_core_count (int):
            Output only. The number of CPU cores
            available.
        compute_model (google.cloud.oracledatabase_v1.types.ComputeModel):
            Output only. The compute model for Base
            Database Service.
        compute_count (int):
            Output only. The number of compute servers
            for the DB system.
        memory_in_gbs (float):
            Output only. The amount of memory allocated
            for the VMDB System in GBs.
    """

    cpu_core_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    compute_model: common.ComputeModel = proto.Field(
        proto.ENUM,
        number=2,
        enum=common.ComputeModel,
    )
    compute_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    memory_in_gbs: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )


class ListDbSystemComputePerformancesRequest(proto.Message):
    r"""Message for listing DbSystemComputePerformances.

    Attributes:
        parent (str):
            Required. Parent value for
            ListDbSystemComputePerformancesRequest Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the ``db_system_shape`` field is supported in
            the following format:
            ``db_system_shape="{db_system_shape}"``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDbSystemComputePerformancesResponse(proto.Message):
    r"""Message for response to listing DbSystemComputePerformances

    Attributes:
        db_system_compute_performances (MutableSequence[google.cloud.oracledatabase_v1.types.DbSystemComputePerformance]):
            The list of DbSystemComputePerformance.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    db_system_compute_performances: MutableSequence["DbSystemComputePerformance"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DbSystemComputePerformance",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
