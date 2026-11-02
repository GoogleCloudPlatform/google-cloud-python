# Copyright 2024, Google LLC All rights reserved.
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

from typing import List, Optional

from opentelemetry.propagators.textmap import Getter, Setter

from google.pubsub_v1 import PubsubMessage


class OpenTelemetryContextSetter(Setter):
    """
    Used by Open Telemetry for context propagation.
    """

    def set(self, carrier: PubsubMessage, key: str, value: str) -> None:
        """
        Injects trace context into Pub/Sub message attributes with
        "googclient_" prefix.

        Args:
            carrier(PubsubMessage): The Pub/Sub message which is the carrier of Open Telemetry
            data.
            key(str): The key for which the Open Telemetry context data needs to be set.
            value(str): The Open Telemetry context value to be set.

        Returns:
            None
        """
        carrier.attributes["googclient_" + key] = value


class OpenTelemetryContextGetter(Getter):
    """
    Used by Open Telemetry for context propagation.
    """

    def get(self, carrier: PubsubMessage, key: str) -> Optional[List[str]]:
        if ("googclient_" + key) not in carrier.attributes:
            return None
        return [carrier.attributes["googclient_" + key]]

    def keys(self, carrier: PubsubMessage) -> List[str]:
        return list(map(str, carrier.attributes.keys()))
