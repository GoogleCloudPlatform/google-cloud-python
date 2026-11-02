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
    package="google.cloud.dataplex.v1",
    manifest={
        "DataQualityRuleTemplate",
    },
)


class DataQualityRuleTemplate(proto.Message):
    r"""DataQualityRuleTemplate represents a template which can be
    reused across multiple data quality rules.

    Attributes:
        name (str):
            Output only. The name of the rule template in the format:
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``
        dimension (str):
            Output only. The dimension a rule template
            belongs to. Rule level results are also
            aggregated at the dimension level.
        sql_collection (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRuleTemplate.Sql]):
            Output only. Collection of SQLs for data
            quality rules. Currently only one SQL is
            supported.
        input_parameters (MutableMapping[str, google.cloud.dataplex_v1.types.DataQualityRuleTemplate.ParameterDescription]):
            Output only. Description for input parameters
        capabilities (MutableSequence[str]):
            Output only. A list of features or properties
            supported by this rule template.
    """

    class Sql(proto.Message):
        r"""Templatized SQL query for data quality rules. It can have
        parameters that can be substituted with values when a rule is
        created using this template.

        Attributes:
            query (str):
                Output only. Templatized SQL query for data
                quality rules.
        """

        query: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ParameterDescription(proto.Message):
        r"""Description of the input parameter. It can include the
        type(s) supported by the parameter and intended usage. It is for
        information purposes only and does not affect the behavior of
        the rule template.

        Attributes:
            description (str):
                Output only. Description of the input
                parameter. It can include the type(s) supported
                by the parameter and intended usage. It is for
                information purposes only and does not affect
                the behavior of the rule template.
            default_value (str):
                Output only. The default value for the
                parameter if no value is provided.
        """

        description: str = proto.Field(
            proto.STRING,
            number=1,
        )
        default_value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimension: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sql_collection: MutableSequence[Sql] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Sql,
    )
    input_parameters: MutableMapping[str, ParameterDescription] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=ParameterDescription,
    )
    capabilities: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
