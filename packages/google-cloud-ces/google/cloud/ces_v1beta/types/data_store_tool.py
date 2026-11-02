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

from google.cloud.ces_v1beta.types import common
from google.cloud.ces_v1beta.types import data_store as gcc_data_store

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "DataStoreTool",
    },
)


class DataStoreTool(proto.Message):
    r"""Tool to retrieve from Vertex AI Search datastore or engine
    for grounding. Accepts either a datastore or an engine, but not
    both. See Vertex AI Search:

    https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_store_source (google.cloud.ces_v1beta.types.DataStoreTool.DataStoreSource):
            Optional. Search within a single specific
            DataStore.

            This field is a member of `oneof`_ ``search_source``.
        engine_source (google.cloud.ces_v1beta.types.DataStoreTool.EngineSource):
            Optional. Search within an Engine
            (potentially across multiple DataStores).

            This field is a member of `oneof`_ ``search_source``.
        name (str):
            Required. The data store tool name.
        description (str):
            Optional. The tool description.
        boost_specs (MutableSequence[google.cloud.ces_v1beta.types.DataStoreTool.BoostSpecs]):
            Optional. Boost specification to boost
            certain documents.
        modality_configs (MutableSequence[google.cloud.ces_v1beta.types.DataStoreTool.ModalityConfig]):
            Optional. The modality configs for the data
            store.
        filter_parameter_behavior (google.cloud.ces_v1beta.types.DataStoreTool.FilterParameterBehavior):
            Optional. The filter parameter behavior.
    """

    class FilterParameterBehavior(proto.Enum):
        r"""Filter parameter behavior.

        Values:
            FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED (0):
                Default filter behavior.
                Include filter parameter for connector
                datastores. For the rest of the datastore types,
                the filter input parameter is omitted.
            ALWAYS_INCLUDE (2):
                Always include filter parameter for all
                datastore types.
            NEVER_INCLUDE (3):
                The filter parameter is never included in the
                list of tool parameters, regardless of the
                datastore type.
        """

        FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED = 0
        ALWAYS_INCLUDE = 2
        NEVER_INCLUDE = 3

    class RewriterConfig(proto.Message):
        r"""Rewriter configuration.

        Attributes:
            model_settings (google.cloud.ces_v1beta.types.ModelSettings):
                Required. Configurations for the LLM model.
            prompt (str):
                Optional. The prompt definition. If not set,
                default prompt will be used.
            disabled (bool):
                Optional. Whether the rewriter is disabled.
        """

        model_settings: common.ModelSettings = proto.Field(
            proto.MESSAGE,
            number=1,
            message=common.ModelSettings,
        )
        prompt: str = proto.Field(
            proto.STRING,
            number=2,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class SummarizationConfig(proto.Message):
        r"""Summarization configuration.

        Attributes:
            model_settings (google.cloud.ces_v1beta.types.ModelSettings):
                Optional. Configurations for the LLM model.
            prompt (str):
                Optional. The prompt definition. If not set,
                default prompt will be used.
            disabled (bool):
                Optional. Whether summarization is disabled.
        """

        model_settings: common.ModelSettings = proto.Field(
            proto.MESSAGE,
            number=1,
            message=common.ModelSettings,
        )
        prompt: str = proto.Field(
            proto.STRING,
            number=2,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class GroundingConfig(proto.Message):
        r"""Grounding configuration.

        Attributes:
            grounding_level (float):
                Optional. The groundedness threshold of the answer based on
                the retrieved sources. The value has a configurable range of
                [1, 5]. The level is used to threshold the groundedness of
                the answer, meaning that all responses with a groundedness
                score below the threshold will fall back to returning
                relevant snippets only.

                For example, a level of 3 means that the groundedness score
                must be 3 or higher for the response to be returned.
            disabled (bool):
                Optional. Whether grounding is disabled.
        """

        grounding_level: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class DataStoreSource(proto.Message):
        r"""Configuration for searching within a specific DataStore.

        Attributes:
            filter (str):
                Optional. Filter specification for the
                DataStore. See:

                https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata
            data_store (google.cloud.ces_v1beta.types.DataStore):
                Optional. The data store.
        """

        filter: str = proto.Field(
            proto.STRING,
            number=2,
        )
        data_store: gcc_data_store.DataStore = proto.Field(
            proto.MESSAGE,
            number=4,
            message=gcc_data_store.DataStore,
        )

    class EngineSource(proto.Message):
        r"""Configuration for searching within an Engine, potentially
        targeting specific DataStores.

        Attributes:
            engine (str):
                Required. Full resource name of the Engine. Format:
                ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}``
            data_store_sources (MutableSequence[google.cloud.ces_v1beta.types.DataStoreTool.DataStoreSource]):
                Optional. Use to target specific DataStores
                within the Engine. If empty, the search applies
                to all DataStores associated with the Engine.
            filter (str):
                Optional. A filter applied to the search across the Engine.
                Not relevant and not used if 'data_store_sources' is
                provided. See:
                https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata
        """

        engine: str = proto.Field(
            proto.STRING,
            number=1,
        )
        data_store_sources: MutableSequence["DataStoreTool.DataStoreSource"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="DataStoreTool.DataStoreSource",
            )
        )
        filter: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class BoostSpecs(proto.Message):
        r"""Boost specifications to boost certain documents.
        For more information, please refer to
        https://cloud.google.com/generative-ai-app-builder/docs/boosting.

        Attributes:
            data_stores (MutableSequence[str]):
                Required. The Data Store where the boosting
                configuration is applied. Full resource name of
                DataStore, such as
                projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.
            spec (MutableSequence[google.cloud.ces_v1beta.types.DataStoreTool.BoostSpec]):
                Required. A list of boosting specifications.
        """

        data_stores: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        spec: MutableSequence["DataStoreTool.BoostSpec"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="DataStoreTool.BoostSpec",
        )

    class BoostSpec(proto.Message):
        r"""Boost specification to boost certain documents.

        Attributes:
            condition_boost_specs (MutableSequence[google.cloud.ces_v1beta.types.DataStoreTool.BoostSpec.ConditionBoostSpec]):
                Required. A list of boosting specifications.
        """

        class ConditionBoostSpec(proto.Message):
            r"""Boost specification for a condition.

            Attributes:
                condition (str):
                    Required. An expression which specifies a boost condition.
                    The syntax is the same as filter expression syntax.
                    Currently, the only supported condition is a list of BCP-47
                    lang codes. Example: To boost suggestions in languages en or
                    fr: (lang_code: ANY("en", "fr"))
                boost (float):
                    Optional. Strength of the boost, which should be in [-1, 1].
                    Negative boost means demotion. Default is 0.0.

                    Setting to 1.0 gives the suggestions a big promotion.
                    However, it does not necessarily mean that the top result
                    will be a boosted suggestion.

                    Setting to -1.0 gives the suggestions a big demotion.
                    However, other suggestions that are relevant might still be
                    shown.

                    Setting to 0.0 means no boost applied. The boosting
                    condition is ignored.
                boost_control_spec (google.cloud.ces_v1beta.types.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec):
                    Optional. Complex specification for custom
                    ranking based on customer defined attribute
                    value.
            """

            class BoostControlSpec(proto.Message):
                r"""Specification for custom ranking based on customer specified
                attribute value. It provides more controls for customized
                ranking than the simple (condition, boost) combination above.

                Attributes:
                    field_name (str):
                        Optional. The name of the field whose value
                        will be used to determine the boost amount.
                    attribute_type (google.cloud.ces_v1beta.types.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType):
                        Optional. The attribute type to be used to determine the
                        boost amount. The attribute value can be derived from the
                        field value of the specified field_name. In the case of
                        numerical it is straightforward i.e. attribute_value =
                        numerical_field_value. In the case of freshness however,
                        attribute_value = (time.now() - datetime_field_value).
                    interpolation_type (google.cloud.ces_v1beta.types.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType):
                        Optional. The interpolation type to be
                        applied to connect the control points listed
                        below.
                    control_points (MutableSequence[google.cloud.ces_v1beta.types.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint]):
                        Optional. The control points used to define the curve. The
                        monotonic function (defined through the interpolation_type
                        above) passes through the control points listed here.
                """

                class AttributeType(proto.Enum):
                    r"""The attribute(or function) for which the custom ranking is to
                    be applied.

                    Values:
                        ATTRIBUTE_TYPE_UNSPECIFIED (0):
                            Unspecified AttributeType.
                        NUMERICAL (1):
                            The value of the numerical field will be used to dynamically
                            update the boost amount. In this case, the attribute_value
                            (the x value) of the control point will be the actual value
                            of the numerical field for which the boost_amount is
                            specified.
                        FRESHNESS (2):
                            For the freshness use case the attribute value will be the
                            duration between the current time and the date in the
                            datetime field specified. The value must be formatted as an
                            XSD ``dayTimeDuration`` value (a restricted subset of an ISO
                            8601 duration value). The pattern for this is:
                            ``[nD][T[nH][nM][nS]]``. E.g. ``5D``, ``3DT12H30M``,
                            ``T24H``.
                    """

                    ATTRIBUTE_TYPE_UNSPECIFIED = 0
                    NUMERICAL = 1
                    FRESHNESS = 2

                class InterpolationType(proto.Enum):
                    r"""The interpolation type to be applied. Default will be linear
                    (Piecewise Linear).

                    Values:
                        INTERPOLATION_TYPE_UNSPECIFIED (0):
                            Interpolation type is unspecified. In this
                            case, it defaults to Linear.
                        LINEAR (1):
                            Piecewise linear interpolation will be
                            applied.
                    """

                    INTERPOLATION_TYPE_UNSPECIFIED = 0
                    LINEAR = 1

                class ControlPoint(proto.Message):
                    r"""The control points used to define the curve. The curve
                    defined through these control points can only be monotonically
                    increasing or decreasing(constant values are acceptable).

                    Attributes:
                        attribute_value (str):
                            Optional. Can be one of:

                            1. The numerical field value.
                            2. The duration spec for freshness: The value must be
                               formatted as an XSD ``dayTimeDuration`` value (a
                               restricted subset of an ISO 8601 duration value). The
                               pattern for this is: ``[nD][T[nH][nM][nS]]``.
                        boost_amount (float):
                            Optional. The value between -1 to 1 by which to boost the
                            score if the attribute_value evaluates to the value
                            specified above.
                    """

                    attribute_value: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    boost_amount: float = proto.Field(
                        proto.FLOAT,
                        number=2,
                    )

                field_name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                attribute_type: "DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType" = proto.Field(
                    proto.ENUM,
                    number=2,
                    enum="DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType",
                )
                interpolation_type: "DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType" = proto.Field(
                    proto.ENUM,
                    number=3,
                    enum="DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType",
                )
                control_points: MutableSequence[
                    "DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint",
                )

            condition: str = proto.Field(
                proto.STRING,
                number=1,
            )
            boost: float = proto.Field(
                proto.FLOAT,
                number=2,
            )
            boost_control_spec: "DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec" = proto.Field(
                proto.MESSAGE,
                number=4,
                message="DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec",
            )

        condition_boost_specs: MutableSequence[
            "DataStoreTool.BoostSpec.ConditionBoostSpec"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataStoreTool.BoostSpec.ConditionBoostSpec",
        )

    class ModalityConfig(proto.Message):
        r"""If specified, will apply the given configuration for the
        specified modality.

        Attributes:
            modality_type (google.cloud.ces_v1beta.types.DataStoreTool.ModalityConfig.ModalityType):
                Required. The modality type.
            rewriter_config (google.cloud.ces_v1beta.types.DataStoreTool.RewriterConfig):
                Optional. The rewriter config.
            summarization_config (google.cloud.ces_v1beta.types.DataStoreTool.SummarizationConfig):
                Optional. The summarization config.
            grounding_config (google.cloud.ces_v1beta.types.DataStoreTool.GroundingConfig):
                Optional. The grounding configuration.
        """

        class ModalityType(proto.Enum):
            r"""The modality type.

            Values:
                MODALITY_TYPE_UNSPECIFIED (0):
                    Unspecified modality type.
                TEXT (1):
                    Text modality.
                AUDIO (2):
                    Audio modality.
            """

            MODALITY_TYPE_UNSPECIFIED = 0
            TEXT = 1
            AUDIO = 2

        modality_type: "DataStoreTool.ModalityConfig.ModalityType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DataStoreTool.ModalityConfig.ModalityType",
        )
        rewriter_config: "DataStoreTool.RewriterConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DataStoreTool.RewriterConfig",
        )
        summarization_config: "DataStoreTool.SummarizationConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="DataStoreTool.SummarizationConfig",
        )
        grounding_config: "DataStoreTool.GroundingConfig" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="DataStoreTool.GroundingConfig",
        )

    data_store_source: DataStoreSource = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="search_source",
        message=DataStoreSource,
    )
    engine_source: EngineSource = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="search_source",
        message=EngineSource,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    boost_specs: MutableSequence[BoostSpecs] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=BoostSpecs,
    )
    modality_configs: MutableSequence[ModalityConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=ModalityConfig,
    )
    filter_parameter_behavior: FilterParameterBehavior = proto.Field(
        proto.ENUM,
        number=10,
        enum=FilterParameterBehavior,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
