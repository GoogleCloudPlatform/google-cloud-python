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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.automl_v1beta1.types import column_spec, data_stats, ranges

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "TablesDatasetMetadata",
        "TablesModelMetadata",
        "TablesAnnotation",
        "TablesModelColumnInfo",
    },
)


class TablesDatasetMetadata(proto.Message):
    r"""Metadata for a dataset used for AutoML Tables.

    Attributes:
        primary_table_spec_id (str):
            Output only. The table_spec_id of the primary table of this
            dataset.
        target_column_spec_id (str):
            column_spec_id of the primary table's column that should be
            used as the training & prediction target. This column must
            be non-nullable and have one of following data types
            (otherwise model creation will error):

            - CATEGORY

            - FLOAT64

            If the type is CATEGORY , only up to 100 unique values may
            exist in that column across all rows.

            NOTE: Updates of this field will instantly affect any other
            users concurrently working with the dataset.
        weight_column_spec_id (str):
            column_spec_id of the primary table's column that should be
            used as the weight column, i.e. the higher the value the
            more important the row will be during model training.
            Required type: FLOAT64. Allowed values: 0 to 10000,
            inclusive on both ends; 0 means the row is ignored for
            training. If not set all rows are assumed to have equal
            weight of 1. NOTE: Updates of this field will instantly
            affect any other users concurrently working with the
            dataset.
        ml_use_column_spec_id (str):
            column_spec_id of the primary table column which specifies a
            possible ML use of the row, i.e. the column will be used to
            split the rows into TRAIN, VALIDATE and TEST sets. Required
            type: STRING. This column, if set, must either have all of
            ``TRAIN``, ``VALIDATE``, ``TEST`` among its values, or only
            have ``TEST``, ``UNASSIGNED`` values. In the latter case the
            rows with ``UNASSIGNED`` value will be assigned by AutoML.
            Note that if a given ml use distribution makes it impossible
            to create a "good" model, that call will error describing
            the issue. If both this column_spec_id and primary table's
            time_column_spec_id are not set, then all rows are treated
            as ``UNASSIGNED``. NOTE: Updates of this field will
            instantly affect any other users concurrently working with
            the dataset.
        target_column_correlations (MutableMapping[str, google.cloud.automl_v1beta1.types.CorrelationStats]):
            Output only. Correlations between

            [TablesDatasetMetadata.target_column_spec_id][google.cloud.automl.v1beta1.TablesDatasetMetadata.target_column_spec_id],
            and other columns of the

            [TablesDatasetMetadataprimary_table][google.cloud.automl.v1beta1.TablesDatasetMetadata.primary_table_spec_id].
            Only set if the target column is set. Mapping from other
            column spec id to its CorrelationStats with the target
            column. This field may be stale, see the stats_update_time
            field for for the timestamp at which these stats were last
            updated.
        stats_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent timestamp when
            target_column_correlations field and all descendant
            ColumnSpec.data_stats and ColumnSpec.top_correlated_columns
            fields were last (re-)generated. Any changes that happened
            to the dataset afterwards are not reflected in these fields
            values. The regeneration happens in the background on a best
            effort basis.
    """

    primary_table_spec_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_column_spec_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    weight_column_spec_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ml_use_column_spec_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    target_column_correlations: MutableMapping[str, data_stats.CorrelationStats] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=6,
            message=data_stats.CorrelationStats,
        )
    )
    stats_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class TablesModelMetadata(proto.Message):
    r"""Model metadata specific to AutoML Tables.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        optimization_objective_recall_value (float):
            Required when optimization_objective is
            "MAXIMIZE_PRECISION_AT_RECALL". Must be between 0 and 1,
            inclusive.

            This field is a member of `oneof`_ ``additional_optimization_objective_config``.
        optimization_objective_precision_value (float):
            Required when optimization_objective is
            "MAXIMIZE_RECALL_AT_PRECISION". Must be between 0 and 1,
            inclusive.

            This field is a member of `oneof`_ ``additional_optimization_objective_config``.
        target_column_spec (google.cloud.automl_v1beta1.types.ColumnSpec):
            Column spec of the dataset's primary table's column the
            model is predicting. Snapshotted when model creation
            started. Only 3 fields are used: name - May be set on
            CreateModel, if it's not then the ColumnSpec corresponding
            to the current target_column_spec_id of the dataset the
            model is trained from is used. If neither is set,
            CreateModel will error. display_name - Output only.
            data_type - Output only.
        input_feature_column_specs (MutableSequence[google.cloud.automl_v1beta1.types.ColumnSpec]):
            Column specs of the dataset's primary table's columns, on
            which the model is trained and which are used as the input
            for predictions. The

            [target_column][google.cloud.automl.v1beta1.TablesModelMetadata.target_column_spec]
            as well as, according to dataset's state upon model
            creation,

            [weight_column][google.cloud.automl.v1beta1.TablesDatasetMetadata.weight_column_spec_id],
            and

            [ml_use_column][google.cloud.automl.v1beta1.TablesDatasetMetadata.ml_use_column_spec_id]
            must never be included here.

            Only 3 fields are used:

            - name - May be set on CreateModel, if set only the columns
              specified are used, otherwise all primary table's columns
              (except the ones listed above) are used for the training
              and prediction input.

            - display_name - Output only.

            - data_type - Output only.
        optimization_objective (str):
            Objective function the model is optimizing towards. The
            training process creates a model that maximizes/minimizes
            the value of the objective function over the validation set.

            The supported optimization objectives depend on the
            prediction type. If the field is not set, a default
            objective function is used.

            CLASSIFICATION_BINARY: "MAXIMIZE_AU_ROC" (default) -
            Maximize the area under the receiver operating
            characteristic (ROC) curve. "MINIMIZE_LOG_LOSS" - Minimize
            log loss. "MAXIMIZE_AU_PRC" - Maximize the area under the
            precision-recall curve. "MAXIMIZE_PRECISION_AT_RECALL" -
            Maximize precision for a specified recall value.
            "MAXIMIZE_RECALL_AT_PRECISION" - Maximize recall for a
            specified precision value.

            CLASSIFICATION_MULTI_CLASS : "MINIMIZE_LOG_LOSS" (default) -
            Minimize log loss.

            REGRESSION: "MINIMIZE_RMSE" (default) - Minimize
            root-mean-squared error (RMSE). "MINIMIZE_MAE" - Minimize
            mean-absolute error (MAE). "MINIMIZE_RMSLE" - Minimize
            root-mean-squared log error (RMSLE).
        tables_model_column_info (MutableSequence[google.cloud.automl_v1beta1.types.TablesModelColumnInfo]):
            Output only. Auxiliary information for each of the
            input_feature_column_specs with respect to this particular
            model.
        train_budget_milli_node_hours (int):
            Required. The train budget of creating this
            model, expressed in milli node hours i.e. 1,000
            value in this field means 1 node hour.

            The training cost of the model will not exceed
            this budget. The final cost will be attempted to
            be close to the budget, though may end up being
            (even) noticeably smaller - at the backend's
            discretion. This especially may happen when
            further model training ceases to provide any
            improvements.

            If the budget is set to a value known to be
            insufficient to train a model for the given
            dataset, the training won't be attempted and
            will error.

            The train budget must be between 1,000 and
            72,000 milli node hours, inclusive.
        train_cost_milli_node_hours (int):
            Output only. The actual training cost of the
            model, expressed in milli node hours, i.e. 1,000
            value in this field means 1 node hour.
            Guaranteed to not exceed the train budget.
        disable_early_stopping (bool):
            Use the entire training budget. This disables
            the early stopping feature. By default, the
            early stopping feature is enabled, which means
            that AutoML Tables might stop training before
            the entire training budget has been used.
    """

    optimization_objective_recall_value: float = proto.Field(
        proto.FLOAT,
        number=17,
        oneof="additional_optimization_objective_config",
    )
    optimization_objective_precision_value: float = proto.Field(
        proto.FLOAT,
        number=18,
        oneof="additional_optimization_objective_config",
    )
    target_column_spec: column_spec.ColumnSpec = proto.Field(
        proto.MESSAGE,
        number=2,
        message=column_spec.ColumnSpec,
    )
    input_feature_column_specs: MutableSequence[column_spec.ColumnSpec] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=column_spec.ColumnSpec,
        )
    )
    optimization_objective: str = proto.Field(
        proto.STRING,
        number=4,
    )
    tables_model_column_info: MutableSequence["TablesModelColumnInfo"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="TablesModelColumnInfo",
        )
    )
    train_budget_milli_node_hours: int = proto.Field(
        proto.INT64,
        number=6,
    )
    train_cost_milli_node_hours: int = proto.Field(
        proto.INT64,
        number=7,
    )
    disable_early_stopping: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


class TablesAnnotation(proto.Message):
    r"""Contains annotation details specific to Tables.

    Attributes:
        score (float):
            Output only. A confidence estimate between 0.0 and 1.0,
            inclusive. A higher value means greater confidence in the
            returned value. For

            [target_column_spec][google.cloud.automl.v1beta1.TablesModelMetadata.target_column_spec]
            of FLOAT64 data type the score is not populated.
        prediction_interval (google.cloud.automl_v1beta1.types.DoubleRange):
            Output only. Only populated when

            [target_column_spec][google.cloud.automl.v1beta1.TablesModelMetadata.target_column_spec]
            has FLOAT64 data type. An interval in which the exactly
            correct target value has 95% chance to be in.
        value (google.protobuf.struct_pb2.Value):
            The predicted value of the row's

            [target_column][google.cloud.automl.v1beta1.TablesModelMetadata.target_column_spec].
            The value depends on the column's DataType:

            - CATEGORY - the predicted (with the above confidence
              ``score``) CATEGORY value.

            - FLOAT64 - the predicted (with above
              ``prediction_interval``) FLOAT64 value.
        tables_model_column_info (MutableSequence[google.cloud.automl_v1beta1.types.TablesModelColumnInfo]):
            Output only. Auxiliary information for each of the model's

            [input_feature_column_specs][google.cloud.automl.v1beta1.TablesModelMetadata.input_feature_column_specs]
            with respect to this particular prediction. If no other
            fields than

            [column_spec_name][google.cloud.automl.v1beta1.TablesModelColumnInfo.column_spec_name]
            and

            [column_display_name][google.cloud.automl.v1beta1.TablesModelColumnInfo.column_display_name]
            would be populated, then this whole field is not.
        baseline_score (float):
            Output only. Stores the prediction score for
            the baseline example, which is defined as the
            example with all values set to their baseline
            values. This is used as part of the Sampled
            Shapley explanation of the model's prediction.
            This field is populated only when feature
            importance is requested. For regression models,
            this holds the baseline prediction for the
            baseline example. For classification models,
            this holds the baseline prediction for the
            baseline example for the argmax class.
    """

    score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    prediction_interval: ranges.DoubleRange = proto.Field(
        proto.MESSAGE,
        number=4,
        message=ranges.DoubleRange,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )
    tables_model_column_info: MutableSequence["TablesModelColumnInfo"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="TablesModelColumnInfo",
        )
    )
    baseline_score: float = proto.Field(
        proto.FLOAT,
        number=5,
    )


class TablesModelColumnInfo(proto.Message):
    r"""An information specific to given column and Tables Model, in
    context of the Model and the predictions created by it.

    Attributes:
        column_spec_name (str):
            Output only. The name of the ColumnSpec
            describing the column. Not populated when this
            proto is outputted to BigQuery.
        column_display_name (str):
            Output only. The display name of the column (same as the
            display_name of its ColumnSpec).
        feature_importance (float):
            Output only. When given as part of a Model (always
            populated): Measurement of how much model predictions
            correctness on the TEST data depend on values in this
            column. A value between 0 and 1, higher means higher
            influence. These values are normalized - for all input
            feature columns of a given model they add to 1.

            When given back by Predict (populated iff
            [feature_importance
            param][google.cloud.automl.v1beta1.PredictRequest.params] is
            set) or Batch Predict (populated iff
            [feature_importance][google.cloud.automl.v1beta1.PredictRequest.params]
            param is set): Measurement of how impactful for the
            prediction returned for the given row the value in this
            column was. Specifically, the feature importance specifies
            the marginal contribution that the feature made to the
            prediction score compared to the baseline score. These
            values are computed using the Sampled Shapley method.
    """

    column_spec_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    column_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    feature_importance: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
