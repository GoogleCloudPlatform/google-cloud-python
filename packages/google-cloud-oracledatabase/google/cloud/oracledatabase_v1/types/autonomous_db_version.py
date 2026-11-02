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

from google.cloud.oracledatabase_v1.types import autonomous_database

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "AutonomousDbVersion",
    },
)


class AutonomousDbVersion(proto.Message):
    r"""Details of the Autonomous Database version.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDbVersionSummary/

    Attributes:
        name (str):
            Identifier. The name of the Autonomous Database Version
            resource with the format:
            projects/{project}/locations/{region}/autonomousDbVersions/{autonomous_db_version}
        version (str):
            Output only. An Oracle Database version for
            Autonomous Database.
        db_workload (google.cloud.oracledatabase_v1.types.DBWorkload):
            Output only. The Autonomous Database workload
            type.
        workload_uri (str):
            Output only. A URL that points to a detailed
            description of the Autonomous Database version.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    db_workload: autonomous_database.DBWorkload = proto.Field(
        proto.ENUM,
        number=4,
        enum=autonomous_database.DBWorkload,
    )
    workload_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
