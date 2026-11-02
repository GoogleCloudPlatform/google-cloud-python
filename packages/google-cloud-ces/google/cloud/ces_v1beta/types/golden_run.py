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
    package="google.cloud.ces.v1beta",
    manifest={
        "GoldenRunMethod",
    },
)


class GoldenRunMethod(proto.Enum):
    r"""The method used to run the evaluation.

    Values:
        GOLDEN_RUN_METHOD_UNSPECIFIED (0):
            Run method is not specified.
        STABLE (1):
            Run the evaluation as stable replay, where
            each turn is a unique session with the previous
            expected turns injected as context.
        NAIVE (2):
            Run the evaluation as naive replay, where the
            run is a single session with no context
            injected.
    """

    GOLDEN_RUN_METHOD_UNSPECIFIED = 0
    STABLE = 1
    NAIVE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
