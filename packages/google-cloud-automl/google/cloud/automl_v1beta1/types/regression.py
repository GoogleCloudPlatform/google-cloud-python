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
    package="google.cloud.automl.v1beta1",
    manifest={
        "RegressionEvaluationMetrics",
    },
)


class RegressionEvaluationMetrics(proto.Message):
    r"""Metrics for regression problems.

    Attributes:
        root_mean_squared_error (float):
            Output only. Root Mean Squared Error (RMSE).
        mean_absolute_error (float):
            Output only. Mean Absolute Error (MAE).
        mean_absolute_percentage_error (float):
            Output only. Mean absolute percentage error.
            Only set if all ground truth values are are
            positive.
        r_squared (float):
            Output only. R squared.
        root_mean_squared_log_error (float):
            Output only. Root mean squared log error.
    """

    root_mean_squared_error: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    mean_absolute_error: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    mean_absolute_percentage_error: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    r_squared: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    root_mean_squared_log_error: float = proto.Field(
        proto.FLOAT,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
