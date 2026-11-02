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
        "Affiliation",
    },
)


class Affiliation(proto.Message):
    r"""Affiliation information of a resource

    Attributes:
        resource_id (str):
            Optional. resource id of affiliated resource
        full_resource_name (str):
            Optional. Full resource name
        lineages (MutableSequence[google.cloud.databasecenter_v1beta.types.Affiliation.Lineage]):
            Optional. Multiple lineages can be created
            from a resource. For example, a resource can be
            replicated to multiple target resources. In this
            case, there will be multiple lineages for the
            resource, one for each target resource.
    """

    class ProcessType(proto.Enum):
        r"""Type of process which created the lineage.

        Values:
            PROCESS_TYPE_UNSPECIFIED (0):
                Unspecified process type.
            COMPOSER (1):
                Composer process type.
            DATASTREAM (2):
                Datastream process type.
            DATAFLOW (3):
                Dataflow process type.
            BIGQUERY (4):
                Bigquery process type.
            DATA_FUSION (5):
                Data fusion process type.
            DATAPROC (6):
                Dataproc process type.
        """

        PROCESS_TYPE_UNSPECIFIED = 0
        COMPOSER = 1
        DATASTREAM = 2
        DATAFLOW = 3
        BIGQUERY = 4
        DATA_FUSION = 5
        DATAPROC = 6

    class Lineage(proto.Message):
        r"""lineage information of the affiliated resources
        This captures source, target and process which created the
        lineage.

        Attributes:
            source_fqn (str):
                Optional. FQN of source table / column
            target_fqn (str):
                Optional. FQN of target table / column
            process_fqn (str):
                Optional. FQN of process which created the
                lineage i.e. dataplex, datastream etc.
            process_type (google.cloud.databasecenter_v1beta.types.Affiliation.ProcessType):
                Optional. Type of process which created the
                lineage.
        """

        source_fqn: str = proto.Field(
            proto.STRING,
            number=1,
        )
        target_fqn: str = proto.Field(
            proto.STRING,
            number=2,
        )
        process_fqn: str = proto.Field(
            proto.STRING,
            number=3,
        )
        process_type: "Affiliation.ProcessType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Affiliation.ProcessType",
        )

    resource_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lineages: MutableSequence[Lineage] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Lineage,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
