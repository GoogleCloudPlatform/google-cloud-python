# Copyright 2023 Google LLC
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
from google.cloud.bigtable.data._metrics.data_model import (
    ActiveOperationMetric,
    CompletedAttemptMetric,
    CompletedOperationMetric,
)


class MetricsHandler:
    """
    Base class for all metrics handlers. Metrics handlers will receive callbacks
    when operations and attempts are completed, and can use this information to
    update some external metrics system.
    """

    def __init__(self, **kwargs):
        pass

    def on_operation_complete(self, op: CompletedOperationMetric) -> None:
        pass

    def on_attempt_complete(
        self, attempt: CompletedAttemptMetric, op: ActiveOperationMetric
    ) -> None:
        pass

    def close(self):
        pass
