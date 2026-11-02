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
from .async_model import (
    AsyncModelMetadata,
    DataFormat,
    GcsDestination,
    GcsSource,
    InputConfig,
    OutputConfig,
)
from .fleet_routing import (
    AggregatedMetrics,
    BatchOptimizeToursRequest,
    BatchOptimizeToursResponse,
    BreakRule,
    CapacityQuantity,
    CapacityQuantityInterval,
    DistanceLimit,
    InjectedSolutionConstraint,
    Location,
    OptimizeToursRequest,
    OptimizeToursResponse,
    OptimizeToursValidationError,
    RouteModifiers,
    Shipment,
    ShipmentModel,
    ShipmentRoute,
    ShipmentTypeIncompatibility,
    ShipmentTypeRequirement,
    SkippedShipment,
    TimeWindow,
    TransitionAttributes,
    Vehicle,
    Waypoint,
)

__all__ = (
    "AsyncModelMetadata",
    "GcsDestination",
    "GcsSource",
    "InputConfig",
    "OutputConfig",
    "DataFormat",
    "AggregatedMetrics",
    "BatchOptimizeToursRequest",
    "BatchOptimizeToursResponse",
    "BreakRule",
    "CapacityQuantity",
    "CapacityQuantityInterval",
    "DistanceLimit",
    "InjectedSolutionConstraint",
    "Location",
    "OptimizeToursRequest",
    "OptimizeToursResponse",
    "OptimizeToursValidationError",
    "RouteModifiers",
    "Shipment",
    "ShipmentModel",
    "ShipmentRoute",
    "ShipmentTypeIncompatibility",
    "ShipmentTypeRequirement",
    "SkippedShipment",
    "TimeWindow",
    "TransitionAttributes",
    "Vehicle",
    "Waypoint",
)
