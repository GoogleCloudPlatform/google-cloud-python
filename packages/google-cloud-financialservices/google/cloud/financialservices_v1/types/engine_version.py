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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.financialservices_v1.types import (
    line_of_business as gcf_line_of_business,
)

__protobuf__ = proto.module(
    package="google.cloud.financialservices.v1",
    manifest={
        "EngineVersion",
        "ListEngineVersionsRequest",
        "ListEngineVersionsResponse",
        "GetEngineVersionRequest",
    },
)


class EngineVersion(proto.Message):
    r"""EngineVersion controls which version of the engine is used to
    tune, train, and run the model.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            EngineVersion format:
            ``/projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}``
        state (google.cloud.financialservices_v1.types.EngineVersion.State):
            Output only. The state of the version.
        expected_limitation_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Planned time to stop allowing
            training/tuning using this version. Existing
            trained models can still be used for
            prediction/backtest.
        expected_decommission_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Planned time to stop supporting
            the version, in addition to no training or
            tuning, models trained on this version can no
            longer be used for prediction/backtest.
        line_of_business (google.cloud.financialservices_v1.types.LineOfBusiness):
            Output only. The line of business
            (Retail/Commercial) this engine version is used
            for.
    """

    class State(proto.Enum):
        r"""State determines the lifecycle of a version and the
        models/engine configs trained with it.

        Values:
            STATE_UNSPECIFIED (0):
                Default state, should never be used.
            ACTIVE (1):
                Version is available for training and
                inference.
            LIMITED (2):
                Models using this version can still be run,
                but new ones cannot be trained.
            DECOMMISSIONED (3):
                Version is deprecated, listed for
                informational purposes only.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        LIMITED = 2
        DECOMMISSIONED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    expected_limitation_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    expected_decommission_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    line_of_business: gcf_line_of_business.LineOfBusiness = proto.Field(
        proto.ENUM,
        number=5,
        enum=gcf_line_of_business.LineOfBusiness,
    )


class ListEngineVersionsRequest(proto.Message):
    r"""Request for retrieving a paginated list of EngineVersion
    resources that meet the specified criteria.

    Attributes:
        parent (str):
            Required. The parent of the EngineVersion is
            the Instance.
        page_size (int):
            Optional. The number of resources to be included in the
            response. The response contains a next_page_token, which can
            be used to retrieve the next page of resources.
        page_token (str):
            Optional. In case of paginated results, this is the token
            that was returned in the previous
            ListEngineVersionsResponse. It should be copied here to
            retrieve the next page of resources. Empty will give the
            first page of ListEngineVersionsRequest, and the last page
            will return an empty page_token.
        filter (str):
            Optional. Specify a filter to narrow search results. If
            empty or unset will default to "state!=DEPRECATED", to view
            deprecated versions use "state:\*" or any other filter.
        order_by (str):
            Optional. Specify a field to use for
            ordering.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListEngineVersionsResponse(proto.Message):
    r"""The response to a list call containing the list of engine
    versions.

    Attributes:
        engine_versions (MutableSequence[google.cloud.financialservices_v1.types.EngineVersion]):
            List of EngineVersion resources
        next_page_token (str):
            This token should be passed to the next
            EngineVersionsRequest to retrieve the next page
            of EngineVersions (empty indicates we are done).
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    engine_versions: MutableSequence["EngineVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EngineVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEngineVersionRequest(proto.Message):
    r"""Request for retrieving a specific EngineVersion resource.

    Attributes:
        name (str):
            Required. The resource name of the
            EngineVersion
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
