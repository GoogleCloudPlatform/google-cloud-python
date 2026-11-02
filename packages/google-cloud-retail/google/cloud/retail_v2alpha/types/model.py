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

from google.cloud.retail_v2alpha.types import common

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "Model",
    },
)


class Model(proto.Message):
    r"""Metadata that describes the training and serving parameters of a
    [Model][google.cloud.retail.v2alpha.Model]. A
    [Model][google.cloud.retail.v2alpha.Model] can be associated with a
    [ServingConfig][google.cloud.retail.v2alpha.ServingConfig] and then
    queried through the Predict API.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        page_optimization_config (google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig):
            Optional. The page optimization config.

            This field is a member of `oneof`_ ``training_config``.
        name (str):
            Required. The fully qualified resource name of the model.

            Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
            catalog_id has char limit of 50. recommendation_model_id has
            char limit of 40.
        display_name (str):
            Required. The display name of the model.

            Should be human readable, used to display
            Recommendation Models in the Retail Cloud
            Console Dashboard. UTF-8 encoded string with
            limit of 1024 characters.
        training_state (google.cloud.retail_v2alpha.types.Model.TrainingState):
            Optional. The training state that the model is in (e.g.
            ``TRAINING`` or ``PAUSED``).

            Since part of the cost of running the service is frequency
            of training - this can be used to determine when to train
            model in order to control cost. If not specified: the
            default value for ``CreateModel`` method is ``TRAINING``.
            The default value for ``UpdateModel`` method is to keep the
            state the same as before.
        serving_state (google.cloud.retail_v2alpha.types.Model.ServingState):
            Output only. The serving state of the model: ``ACTIVE``,
            ``NOT_ACTIVE``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the Recommendation
            Model was created at.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the Recommendation
            Model was last updated. E.g. if a Recommendation
            Model was paused - this would be the time the
            pause was initiated.
        type_ (str):
            Required. The type of model e.g. ``home-page``.

            Currently supported values: ``recommended-for-you``,
            ``others-you-may-like``, ``frequently-bought-together``,
            ``page-optimization``, ``similar-items``, ``buy-it-again``,
            ``on-sale-items``, and ``recently-viewed``\ (readonly
            value).

            This field together with
            [optimization_objective][google.cloud.retail.v2alpha.Model.optimization_objective]
            describe model metadata to use to control model training and
            serving. See https://cloud.google.com/retail/docs/models for
            more details on what the model metadata control and which
            combination of parameters are valid. For invalid
            combinations of parameters (e.g. type =
            ``frequently-bought-together`` and optimization_objective =
            ``ctr``), you receive an error 400 if you try to
            create/update a recommendation with this set of knobs.
        optimization_objective (str):
            Optional. The optimization objective e.g. ``cvr``.

            Currently supported values: ``ctr``, ``cvr``,
            ``revenue-per-order``.

            If not specified, we choose default based on model type.
            Default depends on type of recommendation:

            ``recommended-for-you`` => ``ctr``

            ``others-you-may-like`` => ``ctr``

            ``frequently-bought-together`` => ``revenue_per_order``

            This field together with
            [optimization_objective][google.cloud.retail.v2alpha.Model.type]
            describe model metadata to use to control model training and
            serving. See https://cloud.google.com/retail/docs/models for
            more details on what the model metadata control and which
            combination of parameters are valid. For invalid
            combinations of parameters (e.g. type =
            ``frequently-bought-together`` and optimization_objective =
            ``ctr``), you receive an error 400 if you try to
            create/update a recommendation with this set of knobs.
        periodic_tuning_state (google.cloud.retail_v2alpha.types.Model.PeriodicTuningState):
            Optional. The state of periodic tuning.

            The period we use is 3 months - to do a one-off tune earlier
            use the ``TuneModel`` method. Default value is
            ``PERIODIC_TUNING_ENABLED``.
        last_tune_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the latest
            successful tune finished.
        tuning_operation (str):
            Output only. The tune operation associated
            with the model.
            Can be used to determine if there is an ongoing
            tune for this recommendation. Empty field
            implies no tune is goig on.
        data_state (google.cloud.retail_v2alpha.types.Model.DataState):
            Output only. The state of data requirements for this model:
            ``DATA_OK`` and ``DATA_ERROR``.

            Recommendation model cannot be trained if the data is in
            ``DATA_ERROR`` state. Recommendation model can have
            ``DATA_ERROR`` state even if serving state is ``ACTIVE``:
            models were trained successfully before, but cannot be
            refreshed because model no longer has sufficient data for
            training.
        filtering_option (google.cloud.retail_v2alpha.types.RecommendationsFilteringOption):
            Optional. If ``RECOMMENDATIONS_FILTERING_ENABLED``,
            recommendation filtering by attributes is enabled for the
            model.
        serving_config_lists (MutableSequence[google.cloud.retail_v2alpha.types.Model.ServingConfigList]):
            Output only. The list of valid serving
            configs associated with the
            PageOptimizationConfig.
        model_features_config (google.cloud.retail_v2alpha.types.Model.ModelFeaturesConfig):
            Optional. Additional model features config.
    """

    class ServingState(proto.Enum):
        r"""The serving state of the model.

        Values:
            SERVING_STATE_UNSPECIFIED (0):
                Unspecified serving state.
            INACTIVE (1):
                The model is not serving.
            ACTIVE (2):
                The model is serving and can be queried.
            TUNED (3):
                The model is trained on tuned hyperparameters
                and can be queried.
        """

        SERVING_STATE_UNSPECIFIED = 0
        INACTIVE = 1
        ACTIVE = 2
        TUNED = 3

    class TrainingState(proto.Enum):
        r"""The training state of the model.

        Values:
            TRAINING_STATE_UNSPECIFIED (0):
                Unspecified training state.
            PAUSED (1):
                The model training is paused.
            TRAINING (2):
                The model is training.
        """

        TRAINING_STATE_UNSPECIFIED = 0
        PAUSED = 1
        TRAINING = 2

    class PeriodicTuningState(proto.Enum):
        r"""Describes whether periodic tuning is enabled for this model or not.
        Periodic tuning is scheduled at most every three months. You can
        start a tuning process manually by using the ``TuneModel`` method,
        which starts a tuning process immediately and resets the quarterly
        schedule. Enabling or disabling periodic tuning does not affect any
        current tuning processes.

        Values:
            PERIODIC_TUNING_STATE_UNSPECIFIED (0):
                Unspecified default value, should never be
                explicitly set.
            PERIODIC_TUNING_DISABLED (1):
                The model has periodic tuning disabled. Tuning can be
                reenabled by calling the ``EnableModelPeriodicTuning``
                method or by calling the ``TuneModel`` method.
            ALL_TUNING_DISABLED (3):
                The model cannot be tuned with periodic tuning OR the
                ``TuneModel`` method. Hide the options in customer UI and
                reject any requests through the backend self serve API.
            PERIODIC_TUNING_ENABLED (2):
                The model has periodic tuning enabled. Tuning can be
                disabled by calling the ``DisableModelPeriodicTuning``
                method.
        """

        PERIODIC_TUNING_STATE_UNSPECIFIED = 0
        PERIODIC_TUNING_DISABLED = 1
        ALL_TUNING_DISABLED = 3
        PERIODIC_TUNING_ENABLED = 2

    class DataState(proto.Enum):
        r"""Describes whether this model have sufficient training data
        to be continuously trained.

        Values:
            DATA_STATE_UNSPECIFIED (0):
                Unspecified default value, should never be
                explicitly set.
            DATA_OK (1):
                The model has sufficient training data.
            DATA_ERROR (2):
                The model does not have sufficient training
                data. Error messages can be queried via
                Stackdriver.
        """

        DATA_STATE_UNSPECIFIED = 0
        DATA_OK = 1
        DATA_ERROR = 2

    class ContextProductsType(proto.Enum):
        r"""Use single or multiple context products for recommendations.

        Values:
            CONTEXT_PRODUCTS_TYPE_UNSPECIFIED (0):
                Unspecified default value, should never be explicitly set.
                Defaults to
                [MULTIPLE_CONTEXT_PRODUCTS][google.cloud.retail.v2alpha.Model.ContextProductsType.MULTIPLE_CONTEXT_PRODUCTS].
            SINGLE_CONTEXT_PRODUCT (1):
                Use only a single product as context for the
                recommendation. Typically used on pages like
                add-to-cart or product details.
            MULTIPLE_CONTEXT_PRODUCTS (2):
                Use one or multiple products as context for
                the recommendation. Typically used on shopping
                cart pages.
        """

        CONTEXT_PRODUCTS_TYPE_UNSPECIFIED = 0
        SINGLE_CONTEXT_PRODUCT = 1
        MULTIPLE_CONTEXT_PRODUCTS = 2

    class PageOptimizationConfig(proto.Message):
        r"""The PageOptimizationConfig for model training.

        This determines how many panels to optimize for, and which serving
        configs to consider for each panel. The purpose of this model is to
        optimize which
        [ServingConfig][google.cloud.retail.v2alpha.ServingConfig] to show
        on which panels in way that optimizes the visitors shopping journey.

        Attributes:
            page_optimization_event_type (str):
                Required. The type of
                [UserEvent][google.cloud.retail.v2alpha.UserEvent] this page
                optimization is shown for.

                Each page has an associated event type - this will be the
                corresponding event type for the page that the page
                optimization model is used on.

                Supported types:

                - ``add-to-cart``: Products being added to cart.
                - ``detail-page-view``: Products detail page viewed.
                - ``home-page-view``: Homepage viewed
                - ``category-page-view``: Homepage viewed
                - ``shopping-cart-page-view``: User viewing a shopping cart.

                ``home-page-view`` only allows models with type
                ``recommended-for-you``. All other
                page_optimization_event_type allow all
                [Model.types][google.cloud.retail.v2alpha.Model.type].
            panels (MutableSequence[google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Panel]):
                Required. A list of panel configurations.

                Limit = 5.
            restriction (google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Restriction):
                Optional. How to restrict results across panels e.g. can the
                same
                [ServingConfig][google.cloud.retail.v2alpha.ServingConfig]
                be shown on multiple panels at once.

                If unspecified, default to ``UNIQUE_MODEL_RESTRICTION``.
        """

        class Restriction(proto.Enum):
            r"""Restrictions of expected returned results.

            Values:
                RESTRICTION_UNSPECIFIED (0):
                    Unspecified value for restriction.
                NO_RESTRICTION (1):
                    Allow any
                    [ServingConfig][google.cloud.retail.v2alpha.ServingConfig]
                    to be show on any number of panels.

                    Example:

                    ``Panel1 candidates``: pdp_ctr, pdp_cvr,
                    home_page_ctr_no_diversity

                    ``Panel2 candidates``: home_page_ctr_no_diversity,
                    home_page_ctr_diversity, pdp_cvr_no_diversity

                    ``Restriction`` = NO_RESTRICTION

                    ``Valid combinations``:

                    -  (pdp_ctr, home_page_ctr_no_diversity)
                    - (pdp_ctr, home_page_ctr_diversity)
                    - (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_cvr, home_page_ctr_no_diversity)
                    - (pdp_cvr, home_page_ctr_diversity)
                    - (pdp_cvr, pdp_cvr_no_diversity)
                    - (home_page_ctr_no_diversity, home_page_ctr_no_diversity)
                    - (home_page_ctr_no_diversity, home_page_ctr_diversity)
                    - (home_page_ctr_no_diversity, pdp_cvr_no_diversity)

                    ``Invalid combinations``: []
                UNIQUE_SERVING_CONFIG_RESTRICTION (2):
                    Do not allow the same
                    [ServingConfig.name][google.cloud.retail.v2alpha.ServingConfig.name]
                    to be shown on multiple panels.

                    Example:

                    ``Panel1 candidates``: pdp_ctr, pdp_cvr,
                    home_page_ctr_no_diversity

                    ``Panel2 candidates``: home_page_ctr_no_diversity,
                    home_page_ctr_diversity_low, pdp_cvr_no_diversity

                    ``Restriction`` = ``UNIQUE_SERVING_CONFIG_RESTRICTION``

                    ``Valid combinations``:

                    -  (pdp_ctr, home_page_ctr_no_diversity)
                    - (pdp_ctr, home_page_ctr_diversity_low)
                    - (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_cvr, home_page_ctr_no_diversity)
                    - (pdp_cvr, home_page_ctr_diversity_low)
                    - (pdp_cvr, pdp_cvr_no_diversity)
                    - (home_page_ctr_no_diversity, home_page_ctr_diversity_low)
                    - (home_page_ctr_no_diversity, pdp_cvr_no_diversity)

                    ``Invalid combinations``:

                    -  (home_page_ctr_no_diversity, home_page_ctr_no_diversity)
                UNIQUE_MODEL_RESTRICTION (3):
                    Do not allow multiple
                    [ServingConfigs][google.cloud.retail.v2alpha.ServingConfig]
                    with same
                    [Model.name][google.cloud.retail.v2alpha.Model.name] to be
                    show on on different panels.

                    Example:

                    ``Panel1 candidates``: pdp_ctr, pdp_cvr,
                    home_page_ctr_no_diversity

                    ``Panel2 candidates``: home_page_ctr_no_diversity,
                    home_page_ctr_diversity_low, pdp_cvr_no_diversity

                    ``Restriction`` = ``UNIQUE_MODEL_RESTRICTION``

                    ``Valid combinations``:

                    -  (pdp_ctr, home_page_ctr_no_diversity)
                    - (pdp_ctr, home_page_ctr_diversity)
                    - (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_cvr, home_page_ctr_no_diversity)
                    - (pdp_cvr, home_page_ctr_diversity_low)
                    - (home_page_ctr_no_diversity, pdp_cvr_no_diversity)

                    ``Invalid combinations``:

                    -  (home_page_ctr_no_diversity, home_page_ctr_no_diversity)
                    - (pdp_cvr, pdp_cvr_no_diversity)
                UNIQUE_MODEL_TYPE_RESTRICTION (4):
                    Do not allow multiple
                    [ServingConfigs][google.cloud.retail.v2alpha.ServingConfig]
                    with same
                    [Model.type][google.cloud.retail.v2alpha.Model.type] to be
                    shown on different panels.

                    Example:

                    ``Panel1 candidates``: pdp_ctr, pdp_cvr,
                    home_page_ctr_no_diversity

                    ``Panel2 candidates``: home_page_ctr_no_diversity,
                    home_page_ctr_diversity_low, pdp_cvr_no_diversity

                    ``Restriction`` = ``UNIQUE_MODEL_RESTRICTION``

                    ``Valid combinations``:

                    -  (pdp_ctr, home_page_ctr_no_diversity)
                    - (pdp_ctr, home_page_ctr_diversity)
                    - (pdp_cvr, home_page_ctr_no_diversity)
                    - (pdp_cvr, home_page_ctr_diversity_low)
                    - (home_page_ctr_no_diversity, pdp_cvr_no_diversity)

                    ``Invalid combinations``:

                    -  (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_ctr, pdp_cvr_no_diversity)
                    - (pdp_cvr, pdp_cvr_no_diversity)
                    - (home_page_ctr_no_diversity, home_page_ctr_no_diversity)
                    - (home_page_ctr_no_diversity, home_page_ctr_diversity)
            """

            RESTRICTION_UNSPECIFIED = 0
            NO_RESTRICTION = 1
            UNIQUE_SERVING_CONFIG_RESTRICTION = 2
            UNIQUE_MODEL_RESTRICTION = 3
            UNIQUE_MODEL_TYPE_RESTRICTION = 4

        class Candidate(proto.Message):
            r"""A candidate to consider for a given panel. Currently only
            [ServingConfig][google.cloud.retail.v2alpha.ServingConfig] are valid
            candidates.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                serving_config_id (str):
                    This has to be a valid
                    [ServingConfig][google.cloud.retail.v2alpha.ServingConfig]
                    identifier. For example, for a ServingConfig with full name:
                    ``projects/*/locations/global/catalogs/default_catalog/servingConfigs/my_candidate_config``,
                    this would be ``my_candidate_config``.

                    This field is a member of `oneof`_ ``candidate``.
            """

            serving_config_id: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="candidate",
            )

        class Panel(proto.Message):
            r"""An individual panel with a list of
            [ServingConfigs][google.cloud.retail.v2alpha.ServingConfig] to
            consider for it.

            Attributes:
                display_name (str):
                    Optional. The name to display for the panel.
                candidates (MutableSequence[google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Candidate]):
                    Required. The candidates to consider on the
                    panel.
                default_candidate (google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Candidate):
                    Required. The default candidate. If the model
                    fails at serving time, we fall back to the
                    default.
            """

            display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            candidates: MutableSequence["Model.PageOptimizationConfig.Candidate"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="Model.PageOptimizationConfig.Candidate",
                )
            )
            default_candidate: "Model.PageOptimizationConfig.Candidate" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Model.PageOptimizationConfig.Candidate",
            )

        page_optimization_event_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        panels: MutableSequence["Model.PageOptimizationConfig.Panel"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Model.PageOptimizationConfig.Panel",
            )
        )
        restriction: "Model.PageOptimizationConfig.Restriction" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Model.PageOptimizationConfig.Restriction",
        )

    class ServingConfigList(proto.Message):
        r"""Represents an ordered combination of valid serving configs, which
        can be used for ``PAGE_OPTIMIZATION`` recommendations.

        Attributes:
            serving_config_ids (MutableSequence[str]):
                Optional. A set of valid serving configs that may be used
                for ``PAGE_OPTIMIZATION``.
        """

        serving_config_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class FrequentlyBoughtTogetherFeaturesConfig(proto.Message):
        r"""Additional configs for the frequently-bought-together model
        type.

        Attributes:
            context_products_type (google.cloud.retail_v2alpha.types.Model.ContextProductsType):
                Optional. Specifies the context of the model when it is used
                in predict requests. Can only be set for the
                ``frequently-bought-together`` type. If it isn't specified,
                it defaults to
                [MULTIPLE_CONTEXT_PRODUCTS][google.cloud.retail.v2alpha.Model.ContextProductsType.MULTIPLE_CONTEXT_PRODUCTS].
        """

        context_products_type: "Model.ContextProductsType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Model.ContextProductsType",
        )

    class ModelFeaturesConfig(proto.Message):
        r"""Additional model features config.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            frequently_bought_together_config (google.cloud.retail_v2alpha.types.Model.FrequentlyBoughtTogetherFeaturesConfig):
                Additional configs for
                frequently-bought-together models.

                This field is a member of `oneof`_ ``type_dedicated_config``.
        """

        frequently_bought_together_config: "Model.FrequentlyBoughtTogetherFeaturesConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type_dedicated_config",
            message="Model.FrequentlyBoughtTogetherFeaturesConfig",
        )

    page_optimization_config: PageOptimizationConfig = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="training_config",
        message=PageOptimizationConfig,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    training_state: TrainingState = proto.Field(
        proto.ENUM,
        number=3,
        enum=TrainingState,
    )
    serving_state: ServingState = proto.Field(
        proto.ENUM,
        number=4,
        enum=ServingState,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=7,
    )
    optimization_objective: str = proto.Field(
        proto.STRING,
        number=8,
    )
    periodic_tuning_state: PeriodicTuningState = proto.Field(
        proto.ENUM,
        number=11,
        enum=PeriodicTuningState,
    )
    last_tune_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    tuning_operation: str = proto.Field(
        proto.STRING,
        number=15,
    )
    data_state: DataState = proto.Field(
        proto.ENUM,
        number=16,
        enum=DataState,
    )
    filtering_option: common.RecommendationsFilteringOption = proto.Field(
        proto.ENUM,
        number=18,
        enum=common.RecommendationsFilteringOption,
    )
    serving_config_lists: MutableSequence[ServingConfigList] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=ServingConfigList,
    )
    model_features_config: ModelFeaturesConfig = proto.Field(
        proto.MESSAGE,
        number=22,
        message=ModelFeaturesConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
