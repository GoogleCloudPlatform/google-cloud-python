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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.optimization_v1.types import async_model

__protobuf__ = proto.module(
    package="google.cloud.optimization.v1",
    manifest={
        "OptimizeToursRequest",
        "OptimizeToursResponse",
        "BatchOptimizeToursRequest",
        "BatchOptimizeToursResponse",
        "ShipmentModel",
        "Shipment",
        "ShipmentTypeIncompatibility",
        "ShipmentTypeRequirement",
        "RouteModifiers",
        "Vehicle",
        "TimeWindow",
        "CapacityQuantity",
        "CapacityQuantityInterval",
        "DistanceLimit",
        "TransitionAttributes",
        "Waypoint",
        "Location",
        "BreakRule",
        "ShipmentRoute",
        "SkippedShipment",
        "AggregatedMetrics",
        "InjectedSolutionConstraint",
        "OptimizeToursValidationError",
    },
)


class OptimizeToursRequest(proto.Message):
    r"""Request to be given to a tour optimization solver which
    defines the shipment model to solve as well as optimization
    parameters.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Target project and location to make a call.

            Format: ``projects/{project-id}/locations/{location-id}``.

            If no location is specified, a region will be chosen
            automatically.
        timeout (google.protobuf.duration_pb2.Duration):
            If this timeout is set, the server returns a
            response before the timeout period has elapsed
            or the server deadline for synchronous requests
            is reached, whichever is sooner.

            For asynchronous requests, the server will
            generate a solution (if possible) before the
            timeout has elapsed.
        model (google.cloud.optimization_v1.types.ShipmentModel):
            Shipment model to solve.
        solving_mode (google.cloud.optimization_v1.types.OptimizeToursRequest.SolvingMode):
            By default, the solving mode is ``DEFAULT_SOLVE`` (0).
        search_mode (google.cloud.optimization_v1.types.OptimizeToursRequest.SearchMode):
            Search mode used to solve the request.
        injected_first_solution_routes (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute]):
            Guide the optimization algorithm in finding a first solution
            that is similar to a previous solution.

            The model is constrained when the first solution is built.
            Any shipments not performed on a route are implicitly
            skipped in the first solution, but they may be performed in
            successive solutions.

            The solution must satisfy some basic validity assumptions:

            - for all routes, ``vehicle_index`` must be in range and not
              be duplicated.
            - for all visits, ``shipment_index`` and
              ``visit_request_index`` must be in range.
            - a shipment may only be referenced on one route.
            - the pickup of a pickup-delivery shipment must be performed
              before the delivery.
            - no more than one pickup alternative or delivery
              alternative of a shipment may be performed.
            - for all routes, times are increasing (i.e.,
              ``vehicle_start_time <= visits[0].start_time <= visits[1].start_time ... <= vehicle_end_time``).
            - a shipment may only be performed on a vehicle that is
              allowed. A vehicle is allowed if
              [Shipment.allowed_vehicle_indices][google.cloud.optimization.v1.Shipment.allowed_vehicle_indices]
              is empty or its ``vehicle_index`` is included in
              [Shipment.allowed_vehicle_indices][google.cloud.optimization.v1.Shipment.allowed_vehicle_indices].

            If the injected solution is not feasible, a validation error
            is not necessarily returned and an error indicating
            infeasibility may be returned instead.
        injected_solution_constraint (google.cloud.optimization_v1.types.InjectedSolutionConstraint):
            Constrain the optimization algorithm to find
            a final solution that is similar to a previous
            solution. For example, this may be used to
            freeze portions of routes which have already
            been completed or which are to be completed but
            must not be modified.

            If the injected solution is not feasible, a
            validation error is not necessarily returned and
            an error indicating infeasibility may be
            returned instead.
        refresh_details_routes (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute]):
            If non-empty, the given routes will be refreshed, without
            modifying their underlying sequence of visits or travel
            times: only other details will be updated. This does not
            solve the model.

            As of 2020/11, this only populates the polylines of
            non-empty routes and requires that ``populate_polylines`` is
            true.

            The ``route_polyline`` fields of the passed-in routes may be
            inconsistent with route ``transitions``.

            This field must not be used together with
            ``injected_first_solution_routes`` or
            ``injected_solution_constraint``.

            ``Shipment.ignore`` and ``Vehicle.ignore`` have no effect on
            the behavior. Polylines are still populated between all
            visits in all non-empty routes regardless of whether the
            related shipments or vehicles are ignored.
        interpret_injected_solutions_using_labels (bool):
            If true:

            - uses
              [ShipmentRoute.vehicle_label][google.cloud.optimization.v1.ShipmentRoute.vehicle_label]
              instead of ``vehicle_index`` to match routes in an
              injected solution with vehicles in the request; reuses the
              mapping of original
              [ShipmentRoute.vehicle_index][google.cloud.optimization.v1.ShipmentRoute.vehicle_index]
              to new
              [ShipmentRoute.vehicle_index][google.cloud.optimization.v1.ShipmentRoute.vehicle_index]
              to update
              [ConstraintRelaxation.vehicle_indices][google.cloud.optimization.v1.InjectedSolutionConstraint.ConstraintRelaxation.vehicle_indices]
              if non-empty, but the mapping must be unambiguous (i.e.,
              multiple ``ShipmentRoute``\ s must not share the same
              original ``vehicle_index``).
            - uses
              [ShipmentRoute.Visit.shipment_label][google.cloud.optimization.v1.ShipmentRoute.Visit.shipment_label]
              instead of ``shipment_index`` to match visits in an
              injected solution with shipments in the request;
            - uses
              [SkippedShipment.label][google.cloud.optimization.v1.SkippedShipment.label]
              instead of
              [SkippedShipment.index][google.cloud.optimization.v1.SkippedShipment.index]
              to match skipped shipments in the injected solution with
              request shipments.

            This interpretation applies to the
            ``injected_first_solution_routes``,
            ``injected_solution_constraint``, and
            ``refresh_details_routes`` fields. It can be used when
            shipment or vehicle indices in the request have changed
            since the solution was created, perhaps because shipments or
            vehicles have been removed from or added to the request.

            If true, labels in the following categories must appear at
            most once in their category:

            - [Vehicle.label][google.cloud.optimization.v1.Vehicle.label]
              in the request;
            - [Shipment.label][google.cloud.optimization.v1.Shipment.label]
              in the request;
            - [ShipmentRoute.vehicle_label][google.cloud.optimization.v1.ShipmentRoute.vehicle_label]
              in the injected solution;
            - [SkippedShipment.label][google.cloud.optimization.v1.SkippedShipment.label]
              and
              [ShipmentRoute.Visit.shipment_label][google.cloud.optimization.v1.ShipmentRoute.Visit.shipment_label]
              in the injected solution (except pickup/delivery visit
              pairs, whose ``shipment_label`` must appear twice).

            If a ``vehicle_label`` in the injected solution does not
            correspond to a request vehicle, the corresponding route is
            removed from the solution along with its visits. If a
            ``shipment_label`` in the injected solution does not
            correspond to a request shipment, the corresponding visit is
            removed from the solution. If a
            [SkippedShipment.label][google.cloud.optimization.v1.SkippedShipment.label]
            in the injected solution does not correspond to a request
            shipment, the ``SkippedShipment`` is removed from the
            solution.

            Removing route visits or entire routes from an injected
            solution may have an effect on the implied constraints,
            which may lead to change in solution, validation errors, or
            infeasibility.

            NOTE: The caller must ensure that each
            [Vehicle.label][google.cloud.optimization.v1.Vehicle.label]
            (resp.
            [Shipment.label][google.cloud.optimization.v1.Shipment.label])
            uniquely identifies a vehicle (resp. shipment) entity used
            across the two relevant requests: the past request that
            produced the ``OptimizeToursResponse`` used in the injected
            solution and the current request that includes the injected
            solution. The uniqueness checks described above are not
            enough to guarantee this requirement.
        consider_road_traffic (bool):
            Consider traffic estimation in calculating ``ShipmentRoute``
            fields
            [Transition.travel_duration][google.cloud.optimization.v1.ShipmentRoute.Transition.travel_duration],
            [Visit.start_time][google.cloud.optimization.v1.ShipmentRoute.Visit.start_time],
            and ``vehicle_end_time``; in setting the
            [ShipmentRoute.has_traffic_infeasibilities][google.cloud.optimization.v1.ShipmentRoute.has_traffic_infeasibilities]
            field, and in calculating the
            [OptimizeToursResponse.total_cost][google.cloud.optimization.v1.OptimizeToursResponse.total_cost]
            field.
        populate_polylines (bool):
            If true, polylines will be populated in response
            ``ShipmentRoute``\ s.
        populate_transition_polylines (bool):
            If true, polylines will be populated in response
            [ShipmentRoute.transitions][google.cloud.optimization.v1.ShipmentRoute.transitions].
            Note that in this case, the polylines will also be populated
            in the deprecated ``travel_steps``.
        allow_large_deadline_despite_interruption_risk (bool):
            If this is set, then the request can have a
            deadline (see https://grpc.io/blog/deadlines) of
            up to 60 minutes. Otherwise, the maximum
            deadline is only 30 minutes. Note that
            long-lived requests have a significantly larger
            (but still small) risk of interruption.
        use_geodesic_distances (bool):
            If true, travel distances will be computed using geodesic
            distances instead of Google Maps distances, and travel times
            will be computed using geodesic distances with a speed
            defined by ``geodesic_meters_per_second``.
        geodesic_meters_per_second (float):
            When ``use_geodesic_distances`` is true, this field must be
            set and defines the speed applied to compute travel times.
            Its value must be at least 1.0 meters/seconds.

            This field is a member of `oneof`_ ``_geodesic_meters_per_second``.
        max_validation_errors (int):
            Truncates the number of validation errors returned. These
            errors are typically attached to an INVALID_ARGUMENT error
            payload as a BadRequest error detail
            (https://cloud.google.com/apis/design/errors#error_details),
            unless solving_mode=VALIDATE_ONLY: see the
            [OptimizeToursResponse.validation_errors][google.cloud.optimization.v1.OptimizeToursResponse.validation_errors]
            field. This defaults to 100 and is capped at 10,000.

            This field is a member of `oneof`_ ``_max_validation_errors``.
        label (str):
            Label that may be used to identify this request, reported
            back in the
            [OptimizeToursResponse.request_label][google.cloud.optimization.v1.OptimizeToursResponse.request_label].
        populate_travel_step_polylines (bool):
            Deprecated: Use
            [OptimizeToursRequest.populate_transition_polylines][google.cloud.optimization.v1.OptimizeToursRequest.populate_transition_polylines]
            instead. If true, polylines will be populated in response
            [ShipmentRoute.transitions][google.cloud.optimization.v1.ShipmentRoute.transitions].
            Note that in this case, the polylines will also be populated
            in the deprecated ``travel_steps``.
    """

    class SolvingMode(proto.Enum):
        r"""Defines how the solver should handle the request. In all modes but
        ``VALIDATE_ONLY``, if the request is invalid, you will receive an
        ``INVALID_REQUEST`` error. See
        [max_validation_errors][google.cloud.optimization.v1.OptimizeToursRequest.max_validation_errors]
        to cap the number of errors returned.

        Values:
            DEFAULT_SOLVE (0):
                Solve the model.
            VALIDATE_ONLY (1):
                Only validates the model without solving it: populates as
                many
                [OptimizeToursResponse.validation_errors][google.cloud.optimization.v1.OptimizeToursResponse.validation_errors]
                as possible.
            DETECT_SOME_INFEASIBLE_SHIPMENTS (2):
                Only populates
                [OptimizeToursResponse.validation_errors][google.cloud.optimization.v1.OptimizeToursResponse.validation_errors]
                or
                [OptimizeToursResponse.skipped_shipments][google.cloud.optimization.v1.OptimizeToursResponse.skipped_shipments],
                and doesn't actually solve the rest of the request
                (``status`` and ``routes`` are unset in the response). If
                infeasibilities in ``injected_solution_constraint`` routes
                are detected they are populated in the
                [OptimizeToursResponse.validation_errors][google.cloud.optimization.v1.OptimizeToursResponse.validation_errors]
                field and
                [OptimizeToursResponse.skipped_shipments][google.cloud.optimization.v1.OptimizeToursResponse.skipped_shipments]
                is left empty.

                *IMPORTANT*: not all infeasible shipments are returned here,
                but only the ones that are detected as infeasible during
                preprocessing.
        """

        DEFAULT_SOLVE = 0
        VALIDATE_ONLY = 1
        DETECT_SOME_INFEASIBLE_SHIPMENTS = 2

    class SearchMode(proto.Enum):
        r"""Mode defining the behavior of the search, trading off latency
        versus solution quality. In all modes, the global request
        deadline is enforced.

        Values:
            SEARCH_MODE_UNSPECIFIED (0):
                Unspecified search mode, equivalent to ``RETURN_FAST``.
            RETURN_FAST (1):
                Stop the search after finding the first good
                solution.
            CONSUME_ALL_AVAILABLE_TIME (2):
                Spend all the available time to search for
                better solutions.
        """

        SEARCH_MODE_UNSPECIFIED = 0
        RETURN_FAST = 1
        CONSUME_ALL_AVAILABLE_TIME = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    model: "ShipmentModel" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ShipmentModel",
    )
    solving_mode: SolvingMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=SolvingMode,
    )
    search_mode: SearchMode = proto.Field(
        proto.ENUM,
        number=6,
        enum=SearchMode,
    )
    injected_first_solution_routes: MutableSequence["ShipmentRoute"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="ShipmentRoute",
        )
    )
    injected_solution_constraint: "InjectedSolutionConstraint" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="InjectedSolutionConstraint",
    )
    refresh_details_routes: MutableSequence["ShipmentRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="ShipmentRoute",
    )
    interpret_injected_solutions_using_labels: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    consider_road_traffic: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    populate_polylines: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    populate_transition_polylines: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    allow_large_deadline_despite_interruption_risk: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    use_geodesic_distances: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    geodesic_meters_per_second: float = proto.Field(
        proto.DOUBLE,
        number=16,
        optional=True,
    )
    max_validation_errors: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    label: str = proto.Field(
        proto.STRING,
        number=17,
    )
    populate_travel_step_polylines: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class OptimizeToursResponse(proto.Message):
    r"""Response after solving a tour optimization problem containing
    the routes followed by each vehicle, the shipments which have
    been skipped and the overall cost of the solution.

    Attributes:
        routes (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute]):
            Routes computed for each vehicle; the i-th
            route corresponds to the i-th vehicle in the
            model.
        request_label (str):
            Copy of the
            [OptimizeToursRequest.label][google.cloud.optimization.v1.OptimizeToursRequest.label],
            if a label was specified in the request.
        skipped_shipments (MutableSequence[google.cloud.optimization_v1.types.SkippedShipment]):
            The list of all shipments skipped.
        validation_errors (MutableSequence[google.cloud.optimization_v1.types.OptimizeToursValidationError]):
            List of all the validation errors that we were able to
            detect independently. See the "MULTIPLE ERRORS" explanation
            for the
            [OptimizeToursValidationError][google.cloud.optimization.v1.OptimizeToursValidationError]
            message.
        metrics (google.cloud.optimization_v1.types.OptimizeToursResponse.Metrics):
            Duration, distance and usage metrics for this
            solution.
        total_cost (float):
            Deprecated: Use
            [Metrics.total_cost][google.cloud.optimization.v1.OptimizeToursResponse.Metrics.total_cost]
            instead. Total cost of the solution. This takes into account
            all costs: costs per per hour and travel hour, fixed vehicle
            costs, unperformed shipment penalty costs, global duration
            cost, etc.
    """

    class Metrics(proto.Message):
        r"""Overall metrics, aggregated over all routes.

        Attributes:
            aggregated_route_metrics (google.cloud.optimization_v1.types.AggregatedMetrics):
                Aggregated over the routes. Each metric is the sum (or max,
                for loads) over all
                [ShipmentRoute.metrics][google.cloud.optimization.v1.ShipmentRoute.metrics]
                fields of the same name.
            skipped_mandatory_shipment_count (int):
                Number of mandatory shipments skipped.
            used_vehicle_count (int):
                Number of vehicles used. Note: if a vehicle route is empty
                and
                [Vehicle.used_if_route_is_empty][google.cloud.optimization.v1.Vehicle.used_if_route_is_empty]
                is true, the vehicle is considered used.
            earliest_vehicle_start_time (google.protobuf.timestamp_pb2.Timestamp):
                The earliest start time for a used vehicle, computed as the
                minimum over all used vehicles of
                [ShipmentRoute.vehicle_start_time][google.cloud.optimization.v1.ShipmentRoute.vehicle_start_time].
            latest_vehicle_end_time (google.protobuf.timestamp_pb2.Timestamp):
                The latest end time for a used vehicle, computed as the
                maximum over all used vehicles of
                [ShipmentRoute.vehicle_end_time][google.cloud.optimization.v1.ShipmentRoute.vehicle_end_time].
            costs (MutableMapping[str, float]):
                Cost of the solution, broken down by cost-related request
                fields. The keys are proto paths, relative to the input
                OptimizeToursRequest, e.g. "model.shipments.pickups.cost",
                and the values are the total cost generated by the
                corresponding cost field, aggregated over the whole
                solution. In other words,
                costs["model.shipments.pickups.cost"] is the sum of all
                pickup costs over the solution. All costs defined in the
                model are reported in detail here with the exception of
                costs related to TransitionAttributes that are only reported
                in an aggregated way as of 2022/01.
            total_cost (float):
                Total cost of the solution. The sum of all
                values in the costs map.
        """

        aggregated_route_metrics: "AggregatedMetrics" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="AggregatedMetrics",
        )
        skipped_mandatory_shipment_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        used_vehicle_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        earliest_vehicle_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        latest_vehicle_end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        costs: MutableMapping[str, float] = proto.MapField(
            proto.STRING,
            proto.DOUBLE,
            number=10,
        )
        total_cost: float = proto.Field(
            proto.DOUBLE,
            number=6,
        )

    routes: MutableSequence["ShipmentRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ShipmentRoute",
    )
    request_label: str = proto.Field(
        proto.STRING,
        number=3,
    )
    skipped_shipments: MutableSequence["SkippedShipment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SkippedShipment",
    )
    validation_errors: MutableSequence["OptimizeToursValidationError"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="OptimizeToursValidationError",
        )
    )
    metrics: Metrics = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Metrics,
    )
    total_cost: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class BatchOptimizeToursRequest(proto.Message):
    r"""Request to batch optimize tours as an asynchronous operation. Each
    input file should contain one ``OptimizeToursRequest``, and each
    output file will contain one ``OptimizeToursResponse``. The request
    contains information to read/write and parse the files. All the
    input and output files should be under the same project.

    Attributes:
        parent (str):
            Required. Target project and location to make a call.

            Format: ``projects/{project-id}/locations/{location-id}``.

            If no location is specified, a region will be chosen
            automatically.
        model_configs (MutableSequence[google.cloud.optimization_v1.types.BatchOptimizeToursRequest.AsyncModelConfig]):
            Required. Input/Output information each
            purchase model, such as file paths and data
            formats.
    """

    class AsyncModelConfig(proto.Message):
        r"""Information for solving one optimization model
        asynchronously.

        Attributes:
            display_name (str):
                User defined model name, can be used as alias
                by users to keep track of models.
            input_config (google.cloud.optimization_v1.types.InputConfig):
                Required. Information about the input model.
            output_config (google.cloud.optimization_v1.types.OutputConfig):
                Required. The desired output location
                information.
            enable_checkpoints (bool):
                If this is set, the model will be solved in the checkpoint
                mode. In this mode, the input model can have a deadline
                longer than 30 mins without the risk of interruption. The
                model will be solved in multiple short-running stages. Each
                stage generates an intermediate checkpoint and stores it in
                the user's Cloud Storage buckets. The checkpoint mode should
                be preferred over
                allow_large_deadline_despite_interruption_risk since it
                prevents the risk of interruption.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        input_config: async_model.InputConfig = proto.Field(
            proto.MESSAGE,
            number=2,
            message=async_model.InputConfig,
        )
        output_config: async_model.OutputConfig = proto.Field(
            proto.MESSAGE,
            number=3,
            message=async_model.OutputConfig,
        )
        enable_checkpoints: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    model_configs: MutableSequence[AsyncModelConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AsyncModelConfig,
    )


class BatchOptimizeToursResponse(proto.Message):
    r"""Response to a ``BatchOptimizeToursRequest``. This is returned in the
    LRO Operation after the operation is complete.

    """


class ShipmentModel(proto.Message):
    r"""A shipment model contains a set of shipments which must be performed
    by a set of vehicles, while minimizing the overall cost, which is
    the sum of:

    - the cost of routing the vehicles (sum of cost per total time, cost
      per travel time, and fixed cost over all vehicles).
    - the unperformed shipment penalties.
    - the cost of the global duration of the shipments


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        shipments (MutableSequence[google.cloud.optimization_v1.types.Shipment]):
            Set of shipments which must be performed in
            the model.
        vehicles (MutableSequence[google.cloud.optimization_v1.types.Vehicle]):
            Set of vehicles which can be used to perform
            visits.
        max_active_vehicles (int):
            Constrains the maximum number of active
            vehicles. A vehicle is active if its route
            performs at least one shipment. This can be used
            to limit the number of routes in the case where
            there are fewer drivers than vehicles and that
            the fleet of vehicles is heterogeneous. The
            optimization will then select the best subset of
            vehicles to use. Must be strictly positive.

            This field is a member of `oneof`_ ``_max_active_vehicles``.
        global_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Global start and end time of the model: no times outside of
            this range can be considered valid.

            The model's time span must be less than a year, i.e. the
            ``global_end_time`` and the ``global_start_time`` must be
            within 31536000 seconds of each other.

            When using ``cost_per_*hour`` fields, you might want to set
            this window to a smaller interval to increase performance
            (eg. if you model a single day, you should set the global
            time limits to that day). If unset, 00:00:00 UTC, January 1,
            1970 (i.e. seconds: 0, nanos: 0) is used as default.
        global_end_time (google.protobuf.timestamp_pb2.Timestamp):
            If unset, 00:00:00 UTC, January 1, 1971 (i.e.
            seconds: 31536000, nanos: 0) is used as default.
        global_duration_cost_per_hour (float):
            The "global duration" of the overall plan is the difference
            between the earliest effective start time and the latest
            effective end time of all vehicles. Users can assign a cost
            per hour to that quantity to try and optimize for earliest
            job completion, for example. This cost must be in the same
            unit as
            [Shipment.penalty_cost][google.cloud.optimization.v1.Shipment.penalty_cost].
        duration_distance_matrices (MutableSequence[google.cloud.optimization_v1.types.ShipmentModel.DurationDistanceMatrix]):
            Specifies duration and distance matrices used in the model.
            If this field is empty, Google Maps or geodesic distances
            will be used instead, depending on the value of the
            ``use_geodesic_distances`` field. If it is not empty,
            ``use_geodesic_distances`` cannot be true and neither
            ``duration_distance_matrix_src_tags`` nor
            ``duration_distance_matrix_dst_tags`` can be empty.

            Usage examples:

            - There are two locations: locA and locB.
            - 1 vehicle starting its route at locA and ending it at
              locA.
            - 1 pickup visit request at locB.

            ::

               model {
                 vehicles { start_tags: "locA"  end_tags: "locA" }
                 shipments { pickups { tags: "locB" } }
                 duration_distance_matrix_src_tags: "locA"
                 duration_distance_matrix_src_tags: "locB"
                 duration_distance_matrix_dst_tags: "locA"
                 duration_distance_matrix_dst_tags: "locB"
                 duration_distance_matrices {
                   rows {  # from: locA
                     durations { seconds: 0 }   meters: 0    # to: locA
                     durations { seconds: 100 } meters: 1000 # to: locB
                   }
                   rows {  # from: locB
                     durations { seconds: 102 } meters: 990 # to: locA
                     durations { seconds: 0 }   meters: 0   # to: locB
                   }
                 }
               }

            - There are three locations: locA, locB and locC.
            - 1 vehicle starting its route at locA and ending it at
              locB, using matrix "fast".
            - 1 vehicle starting its route at locB and ending it at
              locB, using matrix "slow".
            - 1 vehicle starting its route at locB and ending it at
              locB, using matrix "fast".
            - 1 pickup visit request at locC.

            ::

               model {
                 vehicles { start_tags: "locA" end_tags: "locB" start_tags: "fast" }
                 vehicles { start_tags: "locB" end_tags: "locB" start_tags: "slow" }
                 vehicles { start_tags: "locB" end_tags: "locB" start_tags: "fast" }
                 shipments { pickups { tags: "locC" } }
                 duration_distance_matrix_src_tags: "locA"
                 duration_distance_matrix_src_tags: "locB"
                 duration_distance_matrix_src_tags: "locC"
                 duration_distance_matrix_dst_tags: "locB"
                 duration_distance_matrix_dst_tags: "locC"
                 duration_distance_matrices {
                   vehicle_start_tag: "fast"
                   rows {  # from: locA
                     durations { seconds: 1000 } meters: 2000 # to: locB
                     durations { seconds: 600 }  meters: 1000 # to: locC
                   }
                   rows {  # from: locB
                     durations { seconds: 0 }   meters: 0    # to: locB
                     durations { seconds: 700 } meters: 1200 # to: locC
                   }
                   rows {  # from: locC
                     durations { seconds: 702 } meters: 1190 # to: locB
                     durations { seconds: 0 }   meters: 0    # to: locC
                   }
                 }
                 duration_distance_matrices {
                   vehicle_start_tag: "slow"
                   rows {  # from: locA
                     durations { seconds: 1800 } meters: 2001 # to: locB
                     durations { seconds: 900 }  meters: 1002 # to: locC
                   }
                   rows {  # from: locB
                     durations { seconds: 0 }    meters: 0    # to: locB
                     durations { seconds: 1000 } meters: 1202 # to: locC
                   }
                   rows {  # from: locC
                     durations { seconds: 1001 } meters: 1195 # to: locB
                     durations { seconds: 0 }    meters: 0    # to: locC
                   }
                 }
               }
        duration_distance_matrix_src_tags (MutableSequence[str]):
            Tags defining the sources of the duration and distance
            matrices; ``duration_distance_matrices(i).rows(j)`` defines
            durations and distances from visits with tag
            ``duration_distance_matrix_src_tags(j)`` to other visits in
            matrix i.

            Tags correspond to
            [VisitRequest.tags][google.cloud.optimization.v1.Shipment.VisitRequest.tags]
            or
            [Vehicle.start_tags][google.cloud.optimization.v1.Vehicle.start_tags].
            A given ``VisitRequest`` or ``Vehicle`` must match exactly
            one tag in this field. Note that a ``Vehicle``'s source,
            destination and matrix tags may be the same; similarly a
            ``VisitRequest``'s source and destination tags may be the
            same. All tags must be different and cannot be empty
            strings. If this field is not empty, then
            ``duration_distance_matrices`` must not be empty.
        duration_distance_matrix_dst_tags (MutableSequence[str]):
            Tags defining the destinations of the duration and distance
            matrices;
            ``duration_distance_matrices(i).rows(j).durations(k)``
            (resp. ``duration_distance_matrices(i).rows(j).meters(k))``
            defines the duration (resp. the distance) of the travel from
            visits with tag ``duration_distance_matrix_src_tags(j)`` to
            visits with tag ``duration_distance_matrix_dst_tags(k)`` in
            matrix i.

            Tags correspond to
            [VisitRequest.tags][google.cloud.optimization.v1.Shipment.VisitRequest.tags]
            or
            [Vehicle.start_tags][google.cloud.optimization.v1.Vehicle.start_tags].
            A given ``VisitRequest`` or ``Vehicle`` must match exactly
            one tag in this field. Note that a ``Vehicle``'s source,
            destination and matrix tags may be the same; similarly a
            ``VisitRequest``'s source and destination tags may be the
            same. All tags must be different and cannot be empty
            strings. If this field is not empty, then
            ``duration_distance_matrices`` must not be empty.
        transition_attributes (MutableSequence[google.cloud.optimization_v1.types.TransitionAttributes]):
            Transition attributes added to the model.
        shipment_type_incompatibilities (MutableSequence[google.cloud.optimization_v1.types.ShipmentTypeIncompatibility]):
            Sets of incompatible shipment_types (see
            ``ShipmentTypeIncompatibility``).
        shipment_type_requirements (MutableSequence[google.cloud.optimization_v1.types.ShipmentTypeRequirement]):
            Sets of ``shipment_type`` requirements (see
            ``ShipmentTypeRequirement``).
        precedence_rules (MutableSequence[google.cloud.optimization_v1.types.ShipmentModel.PrecedenceRule]):
            Set of precedence rules which must be
            enforced in the model.
        break_rules (MutableSequence[google.cloud.optimization_v1.types.ShipmentModel.BreakRule]):
            Deprecated: No longer used. Set of break rules used in the
            model. Each vehicle specifies the ``BreakRule`` that applies
            to it via the
            [Vehicle.break_rule_indices][google.cloud.optimization.v1.Vehicle.break_rule_indices]
            field (which must be a singleton).
    """

    class DurationDistanceMatrix(proto.Message):
        r"""Specifies a duration and distance matrix from visit and
        vehicle start locations to visit and vehicle end locations.

        Attributes:
            rows (MutableSequence[google.cloud.optimization_v1.types.ShipmentModel.DurationDistanceMatrix.Row]):
                Specifies the rows of the duration and distance matrix. It
                must have as many elements as
                [ShipmentModel.duration_distance_matrix_src_tags][google.cloud.optimization.v1.ShipmentModel.duration_distance_matrix_src_tags].
            vehicle_start_tag (str):
                Tag defining to which vehicles this duration and distance
                matrix applies. If empty, this applies to all vehicles, and
                there can only be a single matrix.

                Each vehicle start must match exactly one matrix, i.e.
                exactly one of their ``start_tags`` field must match the
                ``vehicle_start_tag`` of a matrix (and of that matrix only).

                All matrices must have a different ``vehicle_start_tag``.
        """

        class Row(proto.Message):
            r"""Specifies a row of the duration and distance matrix.

            Attributes:
                durations (MutableSequence[google.protobuf.duration_pb2.Duration]):
                    Duration values for a given row. It must have as many
                    elements as
                    [ShipmentModel.duration_distance_matrix_dst_tags][google.cloud.optimization.v1.ShipmentModel.duration_distance_matrix_dst_tags].
                meters (MutableSequence[float]):
                    Distance values for a given row. If no costs or constraints
                    refer to distances in the model, this can be left empty;
                    otherwise it must have as many elements as ``durations``.
            """

            durations: MutableSequence[duration_pb2.Duration] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message=duration_pb2.Duration,
            )
            meters: MutableSequence[float] = proto.RepeatedField(
                proto.DOUBLE,
                number=2,
            )

        rows: MutableSequence["ShipmentModel.DurationDistanceMatrix.Row"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ShipmentModel.DurationDistanceMatrix.Row",
            )
        )
        vehicle_start_tag: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class PrecedenceRule(proto.Message):
        r"""A precedence rule between two events (each event is the pickup or
        the delivery of a shipment): the "second" event has to start at
        least ``offset_duration`` after "first" has started.

        Several precedences can refer to the same (or related) events, e.g.,
        "pickup of B happens after delivery of A" and "pickup of C happens
        after pickup of B".

        Furthermore, precedences only apply when both shipments are
        performed and are otherwise ignored.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            first_index (int):
                Shipment index of the "first" event. This
                field must be specified.

                This field is a member of `oneof`_ ``_first_index``.
            first_is_delivery (bool):
                Indicates if the "first" event is a delivery.
            second_index (int):
                Shipment index of the "second" event. This
                field must be specified.

                This field is a member of `oneof`_ ``_second_index``.
            second_is_delivery (bool):
                Indicates if the "second" event is a
                delivery.
            offset_duration (google.protobuf.duration_pb2.Duration):
                The offset between the "first" and "second"
                event. It can be negative.
        """

        first_index: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        first_is_delivery: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        second_index: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )
        second_is_delivery: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        offset_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )

    class BreakRule(proto.Message):
        r"""Deprecated: Use top level
        [BreakRule][google.cloud.optimization.v1.ShipmentModel.BreakRule]
        instead. Rules to generate time breaks for a vehicle (e.g. lunch
        breaks). A break is a contiguous period of time during which the
        vehicle remains idle at its current position and cannot perform any
        visit. A break may occur:

        - during the travel between two visits (which includes the time
          right before or right after a visit, but not in the middle of a
          visit), in which case it extends the corresponding transit time
          between the visits
        - before the vehicle start (the vehicle may not start in the middle
          of a break), in which case it does not affect the vehicle start
          time.
        - after the vehicle end (ditto, with the vehicle end time).

        Attributes:
            break_requests (MutableSequence[google.cloud.optimization_v1.types.ShipmentModel.BreakRule.BreakRequest]):
                Sequence of breaks. See the ``BreakRequest`` message.
            frequency_constraints (MutableSequence[google.cloud.optimization_v1.types.ShipmentModel.BreakRule.FrequencyConstraint]):
                Several ``FrequencyConstraint`` may apply. They must all be
                satisfied by the ``BreakRequest``\ s of this ``BreakRule``.
                See ``FrequencyConstraint``.
        """

        class BreakRequest(proto.Message):
            r"""The sequence of breaks (i.e. their number and order) that apply to
            each vehicle must be known beforehand. The repeated
            ``BreakRequest``\ s define that sequence, in the order in which they
            must occur. Their time windows (``earliest_start_time`` /
            ``latest_start_time``) may overlap, but they must be compatible with
            the order (this is checked).

            Attributes:
                earliest_start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Required. Lower bound (inclusive) on the
                    start of the break.
                latest_start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Required. Upper bound (inclusive) on the
                    start of the break.
                min_duration (google.protobuf.duration_pb2.Duration):
                    Required. Minimum duration of the break. Must
                    be positive.
            """

            earliest_start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=1,
                message=timestamp_pb2.Timestamp,
            )
            latest_start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                message=timestamp_pb2.Timestamp,
            )
            min_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=3,
                message=duration_pb2.Duration,
            )

        class FrequencyConstraint(proto.Message):
            r"""One may further constrain the frequency and duration of the breaks
            specified above, by enforcing a minimum break frequency, such as
            "There must be a break of at least 1 hour every 12 hours". Assuming
            that this can be interpreted as "Within any sliding time window of
            12h, there must be at least one break of at least one hour", that
            example would translate to the following ``FrequencyConstraint``:

            ::

               {
                  min_break_duration { seconds: 3600 }         # 1 hour.
                  max_inter_break_duration { seconds: 39600 }  # 11 hours (12 - 1 = 11).
               }

            The timing and duration of the breaks in the solution will respect
            all such constraints, in addition to the time windows and minimum
            durations already specified in the ``BreakRequest``.

            A ``FrequencyConstraint`` may in practice apply to non-consecutive
            breaks. For example, the following schedule honors the "1h every
            12h" example:

            ::

                 04:00 vehicle start
                  .. performing travel and visits ..
                 09:00 1 hour break
                 10:00 end of the break
                  .. performing travel and visits ..
                 12:00 20-min lunch break
                 12:20 end of the break
                  .. performing travel and visits ..
                 21:00 1 hour break
                 22:00 end of the break
                  .. performing travel and visits ..
                 23:59 vehicle end

            Attributes:
                min_break_duration (google.protobuf.duration_pb2.Duration):
                    Required. Minimum break duration for this constraint.
                    Nonnegative. See description of ``FrequencyConstraint``.
                max_inter_break_duration (google.protobuf.duration_pb2.Duration):
                    Required. Maximum allowed span of any interval of time in
                    the route that does not include at least partially a break
                    of ``duration >= min_break_duration``. Must be positive.
            """

            min_break_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                message=duration_pb2.Duration,
            )
            max_inter_break_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=2,
                message=duration_pb2.Duration,
            )

        break_requests: MutableSequence["ShipmentModel.BreakRule.BreakRequest"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ShipmentModel.BreakRule.BreakRequest",
            )
        )
        frequency_constraints: MutableSequence[
            "ShipmentModel.BreakRule.FrequencyConstraint"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="ShipmentModel.BreakRule.FrequencyConstraint",
        )

    shipments: MutableSequence["Shipment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Shipment",
    )
    vehicles: MutableSequence["Vehicle"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Vehicle",
    )
    max_active_vehicles: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    global_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    global_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    global_duration_cost_per_hour: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    duration_distance_matrices: MutableSequence[DurationDistanceMatrix] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message=DurationDistanceMatrix,
        )
    )
    duration_distance_matrix_src_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    duration_distance_matrix_dst_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    transition_attributes: MutableSequence["TransitionAttributes"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message="TransitionAttributes",
        )
    )
    shipment_type_incompatibilities: MutableSequence["ShipmentTypeIncompatibility"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="ShipmentTypeIncompatibility",
        )
    )
    shipment_type_requirements: MutableSequence["ShipmentTypeRequirement"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message="ShipmentTypeRequirement",
        )
    )
    precedence_rules: MutableSequence[PrecedenceRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=PrecedenceRule,
    )
    break_rules: MutableSequence[BreakRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=BreakRule,
    )


class Shipment(proto.Message):
    r"""The shipment of a single item, from one of its pickups to one
    of its deliveries. For the shipment to be considered as
    performed, a unique vehicle must visit one of its pickup
    locations (and decrease its spare capacities accordingly), then
    visit one of its delivery locations later on (and therefore
    re-increase its spare capacities accordingly).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pickups (MutableSequence[google.cloud.optimization_v1.types.Shipment.VisitRequest]):
            Set of pickup alternatives associated to the
            shipment. If not specified, the vehicle only
            needs to visit a location corresponding to the
            deliveries.
        deliveries (MutableSequence[google.cloud.optimization_v1.types.Shipment.VisitRequest]):
            Set of delivery alternatives associated to
            the shipment. If not specified, the vehicle only
            needs to visit a location corresponding to the
            pickups.
        load_demands (MutableMapping[str, google.cloud.optimization_v1.types.Shipment.Load]):
            Load demands of the shipment (for example weight, volume,
            number of pallets etc). The keys in the map should be
            identifiers describing the type of the corresponding load,
            ideally also including the units. For example: "weight_kg",
            "volume_gallons", "pallet_count", etc. If a given key does
            not appear in the map, the corresponding load is considered
            as null.
        penalty_cost (float):
            If the shipment is not completed, this penalty is added to
            the overall cost of the routes. A shipment is considered
            completed if one of its pickup and delivery alternatives is
            visited. The cost may be expressed in the same unit used for
            all other cost-related fields in the model and must be
            positive.

            *IMPORTANT*: If this penalty is not specified, it is
            considered infinite, i.e. the shipment must be completed.

            This field is a member of `oneof`_ ``_penalty_cost``.
        allowed_vehicle_indices (MutableSequence[int]):
            The set of vehicles that may perform this shipment. If
            empty, all vehicles may perform it. Vehicles are given by
            their index in the ``ShipmentModel``'s ``vehicles`` list.
        costs_per_vehicle (MutableSequence[float]):
            Specifies the cost that is incurred when this shipment is
            delivered by each vehicle. If specified, it must have
            EITHER:

            - the same number of elements as
              ``costs_per_vehicle_indices``. ``costs_per_vehicle[i]``
              corresponds to vehicle ``costs_per_vehicle_indices[i]`` of
              the model.
            - the same number of elements as there are vehicles in the
              model. The i-th element corresponds to vehicle #i of the
              model.

            These costs must be in the same unit as ``penalty_cost`` and
            must not be negative. Leave this field empty, if there are
            no such costs.
        costs_per_vehicle_indices (MutableSequence[int]):
            Indices of the vehicles to which ``costs_per_vehicle``
            applies. If non-empty, it must have the same number of
            elements as ``costs_per_vehicle``. A vehicle index may not
            be specified more than once. If a vehicle is excluded from
            ``costs_per_vehicle_indices``, its cost is zero.
        pickup_to_delivery_relative_detour_limit (float):
            Specifies the maximum relative detour time compared to the
            shortest path from pickup to delivery. If specified, it must
            be nonnegative, and the shipment must contain at least a
            pickup and a delivery.

            For example, let t be the shortest time taken to go from the
            selected pickup alternative directly to the selected
            delivery alternative. Then setting
            ``pickup_to_delivery_relative_detour_limit`` enforces:

            ::

               start_time(delivery) - start_time(pickup) <=
               std::ceil(t * (1.0 + pickup_to_delivery_relative_detour_limit))

            If both relative and absolute limits are specified on the
            same shipment, the more constraining limit is used for each
            possible pickup/delivery pair. As of 2017/10, detours are
            only supported when travel durations do not depend on
            vehicles.

            This field is a member of `oneof`_ ``_pickup_to_delivery_relative_detour_limit``.
        pickup_to_delivery_absolute_detour_limit (google.protobuf.duration_pb2.Duration):
            Specifies the maximum absolute detour time compared to the
            shortest path from pickup to delivery. If specified, it must
            be nonnegative, and the shipment must contain at least a
            pickup and a delivery.

            For example, let t be the shortest time taken to go from the
            selected pickup alternative directly to the selected
            delivery alternative. Then setting
            ``pickup_to_delivery_absolute_detour_limit`` enforces:

            ::

               start_time(delivery) - start_time(pickup) <=
               t + pickup_to_delivery_absolute_detour_limit

            If both relative and absolute limits are specified on the
            same shipment, the more constraining limit is used for each
            possible pickup/delivery pair. As of 2017/10, detours are
            only supported when travel durations do not depend on
            vehicles.
        pickup_to_delivery_time_limit (google.protobuf.duration_pb2.Duration):
            Specifies the maximum duration from start of
            pickup to start of delivery of a shipment. If
            specified, it must be nonnegative, and the
            shipment must contain at least a pickup and a
            delivery. This does not depend on which
            alternatives are selected for pickup and
            delivery, nor on vehicle speed. This can be
            specified alongside maximum detour constraints:
            the solution will respect both specifications.
        shipment_type (str):
            Non-empty string specifying a "type" for this shipment. This
            feature can be used to define incompatibilities or
            requirements between ``shipment_types`` (see
            ``shipment_type_incompatibilities`` and
            ``shipment_type_requirements`` in ``ShipmentModel``).

            Differs from ``visit_types`` which is specified for a single
            visit: All pickup/deliveries belonging to the same shipment
            share the same ``shipment_type``.
        label (str):
            Specifies a label for this shipment. This label is reported
            in the response in the ``shipment_label`` of the
            corresponding
            [ShipmentRoute.Visit][google.cloud.optimization.v1.ShipmentRoute.Visit].
        ignore (bool):
            If true, skip this shipment, but don't apply a
            ``penalty_cost``.

            Ignoring a shipment results in a validation error when there
            are any ``shipment_type_requirements`` in the model.

            Ignoring a shipment that is performed in
            ``injected_first_solution_routes`` or
            ``injected_solution_constraint`` is permitted; the solver
            removes the related pickup/delivery visits from the
            performing route. ``precedence_rules`` that reference
            ignored shipments will also be ignored.
        demands (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
            Deprecated: Use
            [Shipment.load_demands][google.cloud.optimization.v1.Shipment.load_demands]
            instead.
    """

    class VisitRequest(proto.Message):
        r"""Request for a visit which can be done by a vehicle: it has a
        geo-location (or two, see below), opening and closing times
        represented by time windows, and a service duration time (time
        spent by the vehicle once it has arrived to pickup or drop off
        goods).

        Attributes:
            arrival_location (google.type.latlng_pb2.LatLng):
                The geo-location where the vehicle arrives when performing
                this ``VisitRequest``. If the shipment model has duration
                distance matrices, ``arrival_location`` must not be
                specified.
            arrival_waypoint (google.cloud.optimization_v1.types.Waypoint):
                The waypoint where the vehicle arrives when performing this
                ``VisitRequest``. If the shipment model has duration
                distance matrices, ``arrival_waypoint`` must not be
                specified.
            departure_location (google.type.latlng_pb2.LatLng):
                The geo-location where the vehicle departs after completing
                this ``VisitRequest``. Can be omitted if it is the same as
                ``arrival_location``. If the shipment model has duration
                distance matrices, ``departure_location`` must not be
                specified.
            departure_waypoint (google.cloud.optimization_v1.types.Waypoint):
                The waypoint where the vehicle departs after completing this
                ``VisitRequest``. Can be omitted if it is the same as
                ``arrival_waypoint``. If the shipment model has duration
                distance matrices, ``departure_waypoint`` must not be
                specified.
            tags (MutableSequence[str]):
                Specifies tags attached to the visit request.
                Empty or duplicate strings are not allowed.
            time_windows (MutableSequence[google.cloud.optimization_v1.types.TimeWindow]):
                Time windows which constrain the arrival time at a visit.
                Note that a vehicle may depart outside of the arrival time
                window, i.e. arrival time + duration do not need to be
                inside a time window. This can result in waiting time if the
                vehicle arrives before
                [TimeWindow.start_time][google.cloud.optimization.v1.TimeWindow.start_time].

                The absence of ``TimeWindow`` means that the vehicle can
                perform this visit at any time.

                Time windows must be disjoint, i.e. no time window must
                overlap with or be adjacent to another, and they must be in
                increasing order.

                ``cost_per_hour_after_soft_end_time`` and ``soft_end_time``
                can only be set if there is a single time window.
            duration (google.protobuf.duration_pb2.Duration):
                Duration of the visit, i.e. time spent by the vehicle
                between arrival and departure (to be added to the possible
                waiting time; see ``time_windows``).
            cost (float):
                Cost to service this visit request on a vehicle route. This
                can be used to pay different costs for each alternative
                pickup or delivery of a shipment. This cost must be in the
                same unit as ``Shipment.penalty_cost`` and must not be
                negative.
            load_demands (MutableMapping[str, google.cloud.optimization_v1.types.Shipment.Load]):
                Load demands of this visit request. This is just like
                [Shipment.load_demands][google.cloud.optimization.v1.Shipment.load_demands]
                field, except that it only applies to this
                [VisitRequest][google.cloud.optimization.v1.Shipment.VisitRequest]
                instead of the whole
                [Shipment][google.cloud.optimization.v1.Shipment]. The
                demands listed here are added to the demands listed in
                [Shipment.load_demands][google.cloud.optimization.v1.Shipment.load_demands].
            visit_types (MutableSequence[str]):
                Specifies the types of the visit. This may be used to
                allocate additional time required for a vehicle to complete
                this visit (see
                [Vehicle.extra_visit_duration_for_visit_type][google.cloud.optimization.v1.Vehicle.extra_visit_duration_for_visit_type]).

                A type can only appear once.
            label (str):
                Specifies a label for this ``VisitRequest``. This label is
                reported in the response as ``visit_label`` in the
                corresponding
                [ShipmentRoute.Visit][google.cloud.optimization.v1.ShipmentRoute.Visit].
            demands (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
                Deprecated: Use
                [VisitRequest.load_demands][google.cloud.optimization.v1.Shipment.VisitRequest.load_demands]
                instead.
        """

        arrival_location: latlng_pb2.LatLng = proto.Field(
            proto.MESSAGE,
            number=1,
            message=latlng_pb2.LatLng,
        )
        arrival_waypoint: "Waypoint" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Waypoint",
        )
        departure_location: latlng_pb2.LatLng = proto.Field(
            proto.MESSAGE,
            number=3,
            message=latlng_pb2.LatLng,
        )
        departure_waypoint: "Waypoint" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Waypoint",
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        time_windows: MutableSequence["TimeWindow"] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="TimeWindow",
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )
        cost: float = proto.Field(
            proto.DOUBLE,
            number=8,
        )
        load_demands: MutableMapping[str, "Shipment.Load"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=12,
            message="Shipment.Load",
        )
        visit_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=10,
        )
        label: str = proto.Field(
            proto.STRING,
            number=11,
        )
        demands: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="CapacityQuantity",
        )

    class Load(proto.Message):
        r"""When performing a visit, a predefined amount may be added to the
        vehicle load if it's a pickup, or subtracted if it's a delivery.
        This message defines such amount. See
        [load_demands][google.cloud.optimization.v1.Shipment.load_demands].

        Attributes:
            amount (int):
                The amount by which the load of the vehicle
                performing the corresponding visit will vary.
                Since it is an integer, users are advised to
                choose an appropriate unit to avoid loss of
                precision. Must be ≥ 0.
        """

        amount: int = proto.Field(
            proto.INT64,
            number=2,
        )

    pickups: MutableSequence[VisitRequest] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=VisitRequest,
    )
    deliveries: MutableSequence[VisitRequest] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=VisitRequest,
    )
    load_demands: MutableMapping[str, Load] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=14,
        message=Load,
    )
    penalty_cost: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    allowed_vehicle_indices: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=5,
    )
    costs_per_vehicle: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=6,
    )
    costs_per_vehicle_indices: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=7,
    )
    pickup_to_delivery_relative_detour_limit: float = proto.Field(
        proto.DOUBLE,
        number=8,
        optional=True,
    )
    pickup_to_delivery_absolute_detour_limit: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    pickup_to_delivery_time_limit: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        message=duration_pb2.Duration,
    )
    shipment_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    label: str = proto.Field(
        proto.STRING,
        number=12,
    )
    ignore: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    demands: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="CapacityQuantity",
    )


class ShipmentTypeIncompatibility(proto.Message):
    r"""Specifies incompatibilties between shipments depending on their
    shipment_type. The appearance of incompatible shipments on the same
    route is restricted based on the incompatibility mode.

    Attributes:
        types (MutableSequence[str]):
            List of incompatible types. Two shipments having different
            ``shipment_types`` among those listed are "incompatible".
        incompatibility_mode (google.cloud.optimization_v1.types.ShipmentTypeIncompatibility.IncompatibilityMode):
            Mode applied to the incompatibility.
    """

    class IncompatibilityMode(proto.Enum):
        r"""Modes defining how the appearance of incompatible shipments
        are restricted on the same route.

        Values:
            INCOMPATIBILITY_MODE_UNSPECIFIED (0):
                Unspecified incompatibility mode. This value
                should never be used.
            NOT_PERFORMED_BY_SAME_VEHICLE (1):
                In this mode, two shipments with incompatible
                types can never share the same vehicle.
            NOT_IN_SAME_VEHICLE_SIMULTANEOUSLY (2):
                For two shipments with incompatible types with the
                ``NOT_IN_SAME_VEHICLE_SIMULTANEOUSLY`` incompatibility mode:

                - If both are pickups only (no deliveries) or deliveries
                  only (no pickups), they cannot share the same vehicle at
                  all.
                - If one of the shipments has a delivery and the other a
                  pickup, the two shipments can share the same vehicle iff
                  the former shipment is delivered before the latter is
                  picked up.
        """

        INCOMPATIBILITY_MODE_UNSPECIFIED = 0
        NOT_PERFORMED_BY_SAME_VEHICLE = 1
        NOT_IN_SAME_VEHICLE_SIMULTANEOUSLY = 2

    types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    incompatibility_mode: IncompatibilityMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=IncompatibilityMode,
    )


class ShipmentTypeRequirement(proto.Message):
    r"""Specifies requirements between shipments based on their
    shipment_type. The specifics of the requirement are defined by the
    requirement mode.

    Attributes:
        required_shipment_type_alternatives (MutableSequence[str]):
            List of alternative shipment types required by the
            ``dependent_shipment_types``.
        dependent_shipment_types (MutableSequence[str]):
            All shipments with a type in the
            ``dependent_shipment_types`` field require at least one
            shipment of type ``required_shipment_type_alternatives`` to
            be visited on the same route.

            NOTE: Chains of requirements such that a ``shipment_type``
            depends on itself are not allowed.
        requirement_mode (google.cloud.optimization_v1.types.ShipmentTypeRequirement.RequirementMode):
            Mode applied to the requirement.
    """

    class RequirementMode(proto.Enum):
        r"""Modes defining the appearance of dependent shipments on a
        route.

        Values:
            REQUIREMENT_MODE_UNSPECIFIED (0):
                Unspecified requirement mode. This value
                should never be used.
            PERFORMED_BY_SAME_VEHICLE (1):
                In this mode, all "dependent" shipments must
                share the same vehicle as at least one of their
                "required" shipments.
            IN_SAME_VEHICLE_AT_PICKUP_TIME (2):
                With the ``IN_SAME_VEHICLE_AT_PICKUP_TIME`` mode, all
                "dependent" shipments need to have at least one "required"
                shipment on their vehicle at the time of their pickup.

                A "dependent" shipment pickup must therefore have either:

                - A delivery-only "required" shipment delivered on the route
                  after, or
                - A "required" shipment picked up on the route before it,
                  and if the "required" shipment has a delivery, this
                  delivery must be performed after the "dependent"
                  shipment's pickup.
            IN_SAME_VEHICLE_AT_DELIVERY_TIME (3):
                Same as before, except the "dependent" shipments need to
                have a "required" shipment on their vehicle at the time of
                their *delivery*.
        """

        REQUIREMENT_MODE_UNSPECIFIED = 0
        PERFORMED_BY_SAME_VEHICLE = 1
        IN_SAME_VEHICLE_AT_PICKUP_TIME = 2
        IN_SAME_VEHICLE_AT_DELIVERY_TIME = 3

    required_shipment_type_alternatives: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    dependent_shipment_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    requirement_mode: RequirementMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=RequirementMode,
    )


class RouteModifiers(proto.Message):
    r"""Encapsulates a set of optional conditions to satisfy when
    calculating vehicle routes. This is similar to ``RouteModifiers`` in
    the Google Maps Platform API; see:
    https://developers.google.com/maps/documentation/routes/reference/rest/v2/RouteModifiers.

    Attributes:
        avoid_tolls (bool):
            Specifies whether to avoid toll roads where
            reasonable. Preference will be given to routes
            not containing toll roads. Applies only to
            motorized travel modes.
        avoid_highways (bool):
            Specifies whether to avoid highways where
            reasonable. Preference will be given to routes
            not containing highways. Applies only to
            motorized travel modes.
        avoid_ferries (bool):
            Specifies whether to avoid ferries where
            reasonable. Preference will be given to routes
            not containing travel by ferries. Applies only
            to motorized travel modes.
        avoid_indoor (bool):
            Optional. Specifies whether to avoid navigating indoors
            where reasonable. Preference will be given to routes not
            containing indoor navigation. Applies only to the
            ``WALKING`` travel mode.
    """

    avoid_tolls: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    avoid_highways: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    avoid_ferries: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    avoid_indoor: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class Vehicle(proto.Message):
    r"""Models a vehicle in a shipment problem. Solving a shipment problem
    will build a route starting from ``start_location`` and ending at
    ``end_location`` for this vehicle. A route is a sequence of visits
    (see ``ShipmentRoute``).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        travel_mode (google.cloud.optimization_v1.types.Vehicle.TravelMode):
            The travel mode which affects the roads usable by the
            vehicle and its speed. See also
            ``travel_duration_multiple``.
        route_modifiers (google.cloud.optimization_v1.types.RouteModifiers):
            Optional. A set of conditions to satisfy that
            affect the way routes are calculated for the
            given vehicle.
        start_location (google.type.latlng_pb2.LatLng):
            Geographic location where the vehicle starts before picking
            up any shipments. If not specified, the vehicle starts at
            its first pickup. If the shipment model has duration and
            distance matrices, ``start_location`` must not be specified.
        start_waypoint (google.cloud.optimization_v1.types.Waypoint):
            Waypoint representing a geographic location where the
            vehicle starts before picking up any shipments. If neither
            ``start_waypoint`` nor ``start_location`` is specified, the
            vehicle starts at its first pickup. If the shipment model
            has duration and distance matrices, ``start_waypoint`` must
            not be specified.
        end_location (google.type.latlng_pb2.LatLng):
            Geographic location where the vehicle ends after it has
            completed its last ``VisitRequest``. If not specified the
            vehicle's ``ShipmentRoute`` ends immediately when it
            completes its last ``VisitRequest``. If the shipment model
            has duration and distance matrices, ``end_location`` must
            not be specified.
        end_waypoint (google.cloud.optimization_v1.types.Waypoint):
            Waypoint representing a geographic location where the
            vehicle ends after it has completed its last
            ``VisitRequest``. If neither ``end_waypoint`` nor
            ``end_location`` is specified, the vehicle's
            ``ShipmentRoute`` ends immediately when it completes its
            last ``VisitRequest``. If the shipment model has duration
            and distance matrices, ``end_waypoint`` must not be
            specified.
        start_tags (MutableSequence[str]):
            Specifies tags attached to the start of the
            vehicle's route.
            Empty or duplicate strings are not allowed.
        end_tags (MutableSequence[str]):
            Specifies tags attached to the end of the
            vehicle's route.
            Empty or duplicate strings are not allowed.
        start_time_windows (MutableSequence[google.cloud.optimization_v1.types.TimeWindow]):
            Time windows during which the vehicle may depart its start
            location. They must be within the global time limits (see
            [ShipmentModel.global\_\*][google.cloud.optimization.v1.ShipmentModel.global_start_time]
            fields). If unspecified, there is no limitation besides
            those global time limits.

            Time windows belonging to the same repeated field must be
            disjoint, i.e. no time window can overlap with or be
            adjacent to another, and they must be in chronological
            order.

            ``cost_per_hour_after_soft_end_time`` and ``soft_end_time``
            can only be set if there is a single time window.
        end_time_windows (MutableSequence[google.cloud.optimization_v1.types.TimeWindow]):
            Time windows during which the vehicle may arrive at its end
            location. They must be within the global time limits (see
            [ShipmentModel.global\_\*][google.cloud.optimization.v1.ShipmentModel.global_start_time]
            fields). If unspecified, there is no limitation besides
            those global time limits.

            Time windows belonging to the same repeated field must be
            disjoint, i.e. no time window can overlap with or be
            adjacent to another, and they must be in chronological
            order.

            ``cost_per_hour_after_soft_end_time`` and ``soft_end_time``
            can only be set if there is a single time window.
        travel_duration_multiple (float):
            Specifies a multiplicative factor that can be used to
            increase or decrease travel times of this vehicle. For
            example, setting this to 2.0 means that this vehicle is
            slower and has travel times that are twice what they are for
            standard vehicles. This multiple does not affect visit
            durations. It does affect cost if ``cost_per_hour`` or
            ``cost_per_traveled_hour`` are specified. This must be in
            the range [0.001, 1000.0]. If unset, the vehicle is
            standard, and this multiple is considered 1.0.

            WARNING: Travel times will be rounded to the nearest second
            after this multiple is applied but before performing any
            numerical operations, thus, a small multiple may result in a
            loss of precision.

            See also ``extra_visit_duration_for_visit_type`` below.

            This field is a member of `oneof`_ ``_travel_duration_multiple``.
        unloading_policy (google.cloud.optimization_v1.types.Vehicle.UnloadingPolicy):
            Unloading policy enforced on the vehicle.
        load_limits (MutableMapping[str, google.cloud.optimization_v1.types.Vehicle.LoadLimit]):
            Capacities of the vehicle (weight, volume, # of pallets for
            example). The keys in the map are the identifiers of the
            type of load, consistent with the keys of the
            [Shipment.load_demands][google.cloud.optimization.v1.Shipment.load_demands]
            field. If a given key is absent from this map, the
            corresponding capacity is considered to be limitless.
        cost_per_hour (float):
            Vehicle costs: all costs add up and must be in the same unit
            as
            [Shipment.penalty_cost][google.cloud.optimization.v1.Shipment.penalty_cost].

            Cost per hour of the vehicle route. This cost is applied to
            the total time taken by the route, and includes travel time,
            waiting time, and visit time. Using ``cost_per_hour``
            instead of just ``cost_per_traveled_hour`` may result in
            additional latency.
        cost_per_traveled_hour (float):
            Cost per traveled hour of the vehicle route. This cost is
            applied only to travel time taken by the route (i.e., that
            reported in
            [ShipmentRoute.transitions][google.cloud.optimization.v1.ShipmentRoute.transitions]),
            and excludes waiting time and visit time.
        cost_per_kilometer (float):
            Cost per kilometer of the vehicle route. This cost is
            applied to the distance reported in the
            [ShipmentRoute.transitions][google.cloud.optimization.v1.ShipmentRoute.transitions]
            and does not apply to any distance implicitly traveled from
            the ``arrival_location`` to the ``departure_location`` of a
            single ``VisitRequest``.
        fixed_cost (float):
            Fixed cost applied if this vehicle is used to
            handle a shipment.
        used_if_route_is_empty (bool):
            This field only applies to vehicles when their route does
            not serve any shipments. It indicates if the vehicle should
            be considered as used or not in this case.

            If true, the vehicle goes from its start to its end location
            even if it doesn't serve any shipments, and time and
            distance costs resulting from its start --> end travel are
            taken into account.

            Otherwise, it doesn't travel from its start to its end
            location, and no ``break_rule`` or delay (from
            ``TransitionAttributes``) are scheduled for this vehicle. In
            this case, the vehicle's ``ShipmentRoute`` doesn't contain
            any information except for the vehicle index and label.
        route_duration_limit (google.cloud.optimization_v1.types.Vehicle.DurationLimit):
            Limit applied to the total duration of the vehicle's route.
            In a given ``OptimizeToursResponse``, the route duration of
            a vehicle is the difference between its ``vehicle_end_time``
            and ``vehicle_start_time``.
        travel_duration_limit (google.cloud.optimization_v1.types.Vehicle.DurationLimit):
            Limit applied to the travel duration of the vehicle's route.
            In a given ``OptimizeToursResponse``, the route travel
            duration is the sum of all its
            [transitions.travel_duration][google.cloud.optimization.v1.ShipmentRoute.Transition.travel_duration].
        route_distance_limit (google.cloud.optimization_v1.types.DistanceLimit):
            Limit applied to the total distance of the vehicle's route.
            In a given ``OptimizeToursResponse``, the route distance is
            the sum of all its
            [transitions.travel_distance_meters][google.cloud.optimization.v1.ShipmentRoute.Transition.travel_distance_meters].
        extra_visit_duration_for_visit_type (MutableMapping[str, google.protobuf.duration_pb2.Duration]):
            Specifies a map from visit_types strings to durations. The
            duration is time in addition to
            [VisitRequest.duration][google.cloud.optimization.v1.Shipment.VisitRequest.duration]
            to be taken at visits with the specified ``visit_types``.
            This extra visit duration adds cost if ``cost_per_hour`` is
            specified. Keys (i.e. ``visit_types``) cannot be empty
            strings.

            If a visit request has multiple types, a duration will be
            added for each type in the map.
        break_rule (google.cloud.optimization_v1.types.BreakRule):
            Describes the break schedule to be enforced
            on this vehicle. If empty, no breaks will be
            scheduled for this vehicle.
        label (str):
            Specifies a label for this vehicle. This label is reported
            in the response as the ``vehicle_label`` of the
            corresponding
            [ShipmentRoute][google.cloud.optimization.v1.ShipmentRoute].
        ignore (bool):
            If true, ``used_if_route_is_empty`` must be false, and this
            vehicle will remain unused.

            If a shipment is performed by an ignored vehicle in
            ``injected_first_solution_routes``, it is skipped in the
            first solution but is free to be performed in the response.

            If a shipment is performed by an ignored vehicle in
            ``injected_solution_constraint`` and any related
            pickup/delivery is constrained to remain on the vehicle
            (i.e., not relaxed to level ``RELAX_ALL_AFTER_THRESHOLD``),
            it is skipped in the response. If a shipment has a non-empty
            ``allowed_vehicle_indices`` field and all of the allowed
            vehicles are ignored, it is skipped in the response.
        break_rule_indices (MutableSequence[int]):
            Deprecated: No longer used. Indices in the ``break_rule``
            field in the source
            [ShipmentModel][google.cloud.optimization.v1.ShipmentModel].
            They correspond to break rules enforced on the vehicle.

            As of 2018/03, at most one rule index per vehicle can be
            specified.
        capacities (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
            Deprecated: Use
            [Vehicle.load_limits][google.cloud.optimization.v1.Vehicle.load_limits]
            instead.
        start_load_intervals (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantityInterval]):
            Deprecated: Use
            [Vehicle.LoadLimit.start_load_interval][google.cloud.optimization.v1.Vehicle.LoadLimit.start_load_interval]
            instead.
        end_load_intervals (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantityInterval]):
            Deprecated: Use
            [Vehicle.LoadLimit.end_load_interval][google.cloud.optimization.v1.Vehicle.LoadLimit.end_load_interval]
            instead.
    """

    class TravelMode(proto.Enum):
        r"""Travel modes which can be used by vehicles.

        These should be a subset of the Google Maps Platform Routes
        Preferred API travel modes, see:
        https://developers.google.com/maps/documentation/routes_preferred/reference/rest/Shared.Types/RouteTravelMode.

        Values:
            TRAVEL_MODE_UNSPECIFIED (0):
                Unspecified travel mode, equivalent to ``DRIVING``.
            DRIVING (1):
                Travel mode corresponding to driving
                directions (car, ...).
            WALKING (2):
                Travel mode corresponding to walking
                directions.
        """

        TRAVEL_MODE_UNSPECIFIED = 0
        DRIVING = 1
        WALKING = 2

    class UnloadingPolicy(proto.Enum):
        r"""Policy on how a vehicle can be unloaded. Applies only to shipments
        having both a pickup and a delivery.

        Other shipments are free to occur anywhere on the route independent
        of ``unloading_policy``.

        Values:
            UNLOADING_POLICY_UNSPECIFIED (0):
                Unspecified unloading policy; deliveries must
                just occur after their corresponding pickups.
            LAST_IN_FIRST_OUT (1):
                Deliveries must occur in reverse order of
                pickups
            FIRST_IN_FIRST_OUT (2):
                Deliveries must occur in the same order as
                pickups
        """

        UNLOADING_POLICY_UNSPECIFIED = 0
        LAST_IN_FIRST_OUT = 1
        FIRST_IN_FIRST_OUT = 2

    class LoadLimit(proto.Message):
        r"""Defines a load limit applying to a vehicle, e.g. "this truck may
        only carry up to 3500 kg". See
        [load_limits][google.cloud.optimization.v1.Vehicle.load_limits].


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            max_load (int):
                The maximum acceptable amount of load.

                This field is a member of `oneof`_ ``_max_load``.
            soft_max_load (int):
                A soft limit of the load. See
                [cost_per_unit_above_soft_max][google.cloud.optimization.v1.Vehicle.LoadLimit.cost_per_unit_above_soft_max].
            cost_per_unit_above_soft_max (float):
                If the load ever exceeds
                [soft_max_load][google.cloud.optimization.v1.Vehicle.LoadLimit.soft_max_load]
                along this vehicle's route, the following cost penalty
                applies (only once per vehicle): (load -
                [soft_max_load][google.cloud.optimization.v1.Vehicle.LoadLimit.soft_max_load])

                - [cost_per_unit_above_soft_max][google.cloud.optimization.v1.Vehicle.LoadLimit.cost_per_unit_above_soft_max].
                  All costs add up and must be in the same unit as
                  [Shipment.penalty_cost][google.cloud.optimization.v1.Shipment.penalty_cost].
            start_load_interval (google.cloud.optimization_v1.types.Vehicle.LoadLimit.Interval):
                The acceptable load interval of the vehicle
                at the start of the route.
            end_load_interval (google.cloud.optimization_v1.types.Vehicle.LoadLimit.Interval):
                The acceptable load interval of the vehicle
                at the end of the route.
        """

        class Interval(proto.Message):
            r"""Interval of acceptable load amounts.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                min_ (int):
                    A minimum acceptable load. Must be ≥ 0. If they're both
                    specified,
                    [min][google.cloud.optimization.v1.Vehicle.LoadLimit.Interval.min]
                    must be ≤
                    [max][google.cloud.optimization.v1.Vehicle.LoadLimit.Interval.max].
                max_ (int):
                    A maximum acceptable load. Must be ≥ 0. If unspecified, the
                    maximum load is unrestricted by this message. If they're
                    both specified,
                    [min][google.cloud.optimization.v1.Vehicle.LoadLimit.Interval.min]
                    must be ≤
                    [max][google.cloud.optimization.v1.Vehicle.LoadLimit.Interval.max].

                    This field is a member of `oneof`_ ``_max``.
            """

            min_: int = proto.Field(
                proto.INT64,
                number=1,
            )
            max_: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )

        max_load: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        soft_max_load: int = proto.Field(
            proto.INT64,
            number=2,
        )
        cost_per_unit_above_soft_max: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )
        start_load_interval: "Vehicle.LoadLimit.Interval" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Vehicle.LoadLimit.Interval",
        )
        end_load_interval: "Vehicle.LoadLimit.Interval" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Vehicle.LoadLimit.Interval",
        )

    class DurationLimit(proto.Message):
        r"""A limit defining a maximum duration of the route of a
        vehicle. It can be either hard or soft.

        When a soft limit field is defined, both the soft max threshold
        and its associated cost must be defined together.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            max_duration (google.protobuf.duration_pb2.Duration):
                A hard limit constraining the duration to be at most
                max_duration.
            soft_max_duration (google.protobuf.duration_pb2.Duration):
                A soft limit not enforcing a maximum duration limit, but
                when violated makes the route incur a cost. This cost adds
                up to other costs defined in the model, with the same unit.

                If defined, ``soft_max_duration`` must be nonnegative. If
                max_duration is also defined, ``soft_max_duration`` must be
                less than max_duration.
            cost_per_hour_after_soft_max (float):
                Cost per hour incurred if the ``soft_max_duration``
                threshold is violated. The additional cost is 0 if the
                duration is under the threshold, otherwise the cost depends
                on the duration as follows:

                ::

                     cost_per_hour_after_soft_max * (duration - soft_max_duration)

                The cost must be nonnegative.

                This field is a member of `oneof`_ ``_cost_per_hour_after_soft_max``.
            quadratic_soft_max_duration (google.protobuf.duration_pb2.Duration):
                A soft limit not enforcing a maximum duration limit, but
                when violated makes the route incur a cost, quadratic in the
                duration. This cost adds up to other costs defined in the
                model, with the same unit.

                If defined, ``quadratic_soft_max_duration`` must be
                nonnegative. If ``max_duration`` is also defined,
                ``quadratic_soft_max_duration`` must be less than
                ``max_duration``, and the difference must be no larger than
                one day:

                ::

                   `max_duration - quadratic_soft_max_duration <= 86400 seconds`
            cost_per_square_hour_after_quadratic_soft_max (float):
                Cost per square hour incurred if the
                ``quadratic_soft_max_duration`` threshold is violated.

                The additional cost is 0 if the duration is under the
                threshold, otherwise the cost depends on the duration as
                follows:

                ::

                     cost_per_square_hour_after_quadratic_soft_max *
                     (duration - quadratic_soft_max_duration)^2

                The cost must be nonnegative.

                This field is a member of `oneof`_ ``_cost_per_square_hour_after_quadratic_soft_max``.
        """

        max_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        soft_max_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        cost_per_hour_after_soft_max: float = proto.Field(
            proto.DOUBLE,
            number=3,
            optional=True,
        )
        quadratic_soft_max_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        cost_per_square_hour_after_quadratic_soft_max: float = proto.Field(
            proto.DOUBLE,
            number=5,
            optional=True,
        )

    travel_mode: TravelMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=TravelMode,
    )
    route_modifiers: "RouteModifiers" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RouteModifiers",
    )
    start_location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=3,
        message=latlng_pb2.LatLng,
    )
    start_waypoint: "Waypoint" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Waypoint",
    )
    end_location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=5,
        message=latlng_pb2.LatLng,
    )
    end_waypoint: "Waypoint" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Waypoint",
    )
    start_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    end_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    start_time_windows: MutableSequence["TimeWindow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="TimeWindow",
    )
    end_time_windows: MutableSequence["TimeWindow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="TimeWindow",
    )
    travel_duration_multiple: float = proto.Field(
        proto.DOUBLE,
        number=11,
        optional=True,
    )
    unloading_policy: UnloadingPolicy = proto.Field(
        proto.ENUM,
        number=12,
        enum=UnloadingPolicy,
    )
    load_limits: MutableMapping[str, LoadLimit] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=30,
        message=LoadLimit,
    )
    cost_per_hour: float = proto.Field(
        proto.DOUBLE,
        number=16,
    )
    cost_per_traveled_hour: float = proto.Field(
        proto.DOUBLE,
        number=17,
    )
    cost_per_kilometer: float = proto.Field(
        proto.DOUBLE,
        number=18,
    )
    fixed_cost: float = proto.Field(
        proto.DOUBLE,
        number=19,
    )
    used_if_route_is_empty: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    route_duration_limit: DurationLimit = proto.Field(
        proto.MESSAGE,
        number=21,
        message=DurationLimit,
    )
    travel_duration_limit: DurationLimit = proto.Field(
        proto.MESSAGE,
        number=22,
        message=DurationLimit,
    )
    route_distance_limit: "DistanceLimit" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="DistanceLimit",
    )
    extra_visit_duration_for_visit_type: MutableMapping[str, duration_pb2.Duration] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=24,
            message=duration_pb2.Duration,
        )
    )
    break_rule: "BreakRule" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="BreakRule",
    )
    label: str = proto.Field(
        proto.STRING,
        number=27,
    )
    ignore: bool = proto.Field(
        proto.BOOL,
        number=28,
    )
    break_rule_indices: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=29,
    )
    capacities: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="CapacityQuantity",
    )
    start_load_intervals: MutableSequence["CapacityQuantityInterval"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message="CapacityQuantityInterval",
        )
    )
    end_load_intervals: MutableSequence["CapacityQuantityInterval"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=15,
            message="CapacityQuantityInterval",
        )
    )


class TimeWindow(proto.Message):
    r"""Time windows constrain the time of an event, such as the arrival
    time at a visit, or the start and end time of a vehicle.

    Hard time window bounds, ``start_time`` and ``end_time``, enforce
    the earliest and latest time of the event, such that
    ``start_time <= event_time <= end_time``. The soft time window lower
    bound, ``soft_start_time``, expresses a preference for the event to
    happen at or after ``soft_start_time`` by incurring a cost
    proportional to how long before soft_start_time the event occurs.
    The soft time window upper bound, ``soft_end_time``, expresses a
    preference for the event to happen at or before ``soft_end_time`` by
    incurring a cost proportional to how long after ``soft_end_time``
    the event occurs. ``start_time``, ``end_time``, ``soft_start_time``
    and ``soft_end_time`` should be within the global time limits (see
    [ShipmentModel.global_start_time][google.cloud.optimization.v1.ShipmentModel.global_start_time]
    and
    [ShipmentModel.global_end_time][google.cloud.optimization.v1.ShipmentModel.global_end_time])
    and should respect:

    ::

         0 <= `start_time` <= `soft_start_time` <= `end_time` and
         0 <= `start_time` <= `soft_end_time` <= `end_time`.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The hard time window start time. If unspecified it will be
            set to ``ShipmentModel.global_start_time``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The hard time window end time. If unspecified it will be set
            to ``ShipmentModel.global_end_time``.
        soft_start_time (google.protobuf.timestamp_pb2.Timestamp):
            The soft start time of the time window.
        soft_end_time (google.protobuf.timestamp_pb2.Timestamp):
            The soft end time of the time window.
        cost_per_hour_before_soft_start_time (float):
            A cost per hour added to other costs in the model if the
            event occurs before soft_start_time, computed as:

            ::

                  max(0, soft_start_time - t.seconds)
                                         * cost_per_hour_before_soft_start_time / 3600,
               t being the time of the event.

            This cost must be positive, and the field can only be set if
            soft_start_time has been set.

            This field is a member of `oneof`_ ``_cost_per_hour_before_soft_start_time``.
        cost_per_hour_after_soft_end_time (float):
            A cost per hour added to other costs in the model if the
            event occurs after ``soft_end_time``, computed as:

            ::

                  max(0, t.seconds - soft_end_time.seconds)
                                   * cost_per_hour_after_soft_end_time / 3600,
               t being the time of the event.

            This cost must be positive, and the field can only be set if
            ``soft_end_time`` has been set.

            This field is a member of `oneof`_ ``_cost_per_hour_after_soft_end_time``.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    soft_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    soft_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    cost_per_hour_before_soft_start_time: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )
    cost_per_hour_after_soft_end_time: float = proto.Field(
        proto.DOUBLE,
        number=6,
        optional=True,
    )


class CapacityQuantity(proto.Message):
    r"""Deprecated: Use
    [Vehicle.LoadLimit.Interval][google.cloud.optimization.v1.Vehicle.LoadLimit.Interval]
    instead.

    Attributes:
        type_ (str):

        value (int):

    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: int = proto.Field(
        proto.INT64,
        number=2,
    )


class CapacityQuantityInterval(proto.Message):
    r"""Deprecated: Use
    [Vehicle.LoadLimit.Interval][google.cloud.optimization.v1.Vehicle.LoadLimit.Interval]
    instead.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (str):

        min_value (int):

            This field is a member of `oneof`_ ``_min_value``.
        max_value (int):

            This field is a member of `oneof`_ ``_max_value``.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    min_value: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    max_value: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class DistanceLimit(proto.Message):
    r"""A limit defining a maximum distance which can be traveled. It can be
    either hard or soft.

    If a soft limit is defined, both ``soft_max_meters`` and
    ``cost_per_kilometer_above_soft_max`` must be defined and be
    nonnegative.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        max_meters (int):
            A hard limit constraining the distance to be at most
            max_meters. The limit must be nonnegative.

            This field is a member of `oneof`_ ``_max_meters``.
        soft_max_meters (int):
            A soft limit not enforcing a maximum distance limit, but
            when violated results in a cost which adds up to other costs
            defined in the model, with the same unit.

            If defined soft_max_meters must be less than max_meters and
            must be nonnegative.

            This field is a member of `oneof`_ ``_soft_max_meters``.
        cost_per_kilometer_below_soft_max (float):
            Cost per kilometer incurred, increasing up to
            ``soft_max_meters``, with formula:

            ::

                 min(distance_meters, soft_max_meters) / 1000.0 *
                 cost_per_kilometer_below_soft_max.

            This cost is not supported in ``route_distance_limit``.

            This field is a member of `oneof`_ ``_cost_per_kilometer_below_soft_max``.
        cost_per_kilometer_above_soft_max (float):
            Cost per kilometer incurred if distance is above
            ``soft_max_meters`` limit. The additional cost is 0 if the
            distance is under the limit, otherwise the formula used to
            compute the cost is the following:

            ::

                 (distance_meters - soft_max_meters) / 1000.0 *
                 cost_per_kilometer_above_soft_max.

            The cost must be nonnegative.

            This field is a member of `oneof`_ ``_cost_per_kilometer_above_soft_max``.
    """

    max_meters: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    soft_max_meters: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    cost_per_kilometer_below_soft_max: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    cost_per_kilometer_above_soft_max: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class TransitionAttributes(proto.Message):
    r"""Specifies attributes of transitions between two consecutive visits
    on a route. Several ``TransitionAttributes`` may apply to the same
    transition: in that case, all extra costs add up and the strictest
    constraint or limit applies (following natural "AND" semantics).

    Attributes:
        src_tag (str):
            Tags defining the set of (src->dst) transitions these
            attributes apply to.

            A source visit or vehicle start matches iff its
            [VisitRequest.tags][google.cloud.optimization.v1.Shipment.VisitRequest.tags]
            or
            [Vehicle.start_tags][google.cloud.optimization.v1.Vehicle.start_tags]
            either contains ``src_tag`` or does not contain
            ``excluded_src_tag`` (depending on which of these two fields
            is non-empty).
        excluded_src_tag (str):
            See ``src_tag``. Exactly one of ``src_tag`` and
            ``excluded_src_tag`` must be non-empty.
        dst_tag (str):
            A destination visit or vehicle end matches iff its
            [VisitRequest.tags][google.cloud.optimization.v1.Shipment.VisitRequest.tags]
            or
            [Vehicle.end_tags][google.cloud.optimization.v1.Vehicle.end_tags]
            either contains ``dst_tag`` or does not contain
            ``excluded_dst_tag`` (depending on which of these two fields
            is non-empty).
        excluded_dst_tag (str):
            See ``dst_tag``. Exactly one of ``dst_tag`` and
            ``excluded_dst_tag`` must be non-empty.
        cost (float):
            Specifies a cost for performing this
            transition. This is in the same unit as all
            other costs in the model and must not be
            negative. It is applied on top of all other
            existing costs.
        cost_per_kilometer (float):
            Specifies a cost per kilometer applied to the distance
            traveled while performing this transition. It adds up to any
            [Vehicle.cost_per_kilometer][google.cloud.optimization.v1.Vehicle.cost_per_kilometer]
            specified on vehicles.
        distance_limit (google.cloud.optimization_v1.types.DistanceLimit):
            Specifies a limit on the distance traveled
            while performing this transition.

            As of 2021/06, only soft limits are supported.
        delay (google.protobuf.duration_pb2.Duration):
            Specifies a delay incurred when performing this transition.

            This delay always occurs *after* finishing the source visit
            and *before* starting the destination visit.
    """

    src_tag: str = proto.Field(
        proto.STRING,
        number=1,
    )
    excluded_src_tag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dst_tag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    excluded_dst_tag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cost: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    cost_per_kilometer: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    distance_limit: "DistanceLimit" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DistanceLimit",
    )
    delay: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )


class Waypoint(proto.Message):
    r"""Encapsulates a waypoint. Waypoints mark arrival and departure
    locations of VisitRequests, and start and end locations of
    Vehicles.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location (google.cloud.optimization_v1.types.Location):
            A point specified using geographic
            coordinates, including an optional heading.

            This field is a member of `oneof`_ ``location_type``.
        place_id (str):
            The POI Place ID associated with the
            waypoint.

            This field is a member of `oneof`_ ``location_type``.
        side_of_road (bool):
            Indicates that the location of this waypoint is meant to
            have a preference for the vehicle to stop at a particular
            side of road. When you set this value, the route will pass
            through the location so that the vehicle can stop at the
            side of road that the location is biased towards from the
            center of the road. This option works only for the 'DRIVING'
            travel mode, and when the 'location_type' is set to
            'location'.
    """

    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="location_type",
        message="Location",
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="location_type",
    )
    side_of_road: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class Location(proto.Message):
    r"""Encapsulates a location (a geographic point, and an optional
    heading).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        lat_lng (google.type.latlng_pb2.LatLng):
            The waypoint's geographic coordinates.
        heading (int):
            The compass heading associated with the
            direction of the flow of traffic. This value is
            used to specify the side of the road to use for
            pickup and drop-off. Heading values can be from
            0 to 360, where 0 specifies a heading of due
            North, 90 specifies a heading of due East, etc.

            This field is a member of `oneof`_ ``_heading``.
    """

    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    heading: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class BreakRule(proto.Message):
    r"""Rules to generate time breaks for a vehicle (e.g. lunch breaks). A
    break is a contiguous period of time during which the vehicle
    remains idle at its current position and cannot perform any visit. A
    break may occur:

    - during the travel between two visits (which includes the time
      right before or right after a visit, but not in the middle of a
      visit), in which case it extends the corresponding transit time
      between the visits,
    - or before the vehicle start (the vehicle may not start in the
      middle of a break), in which case it does not affect the vehicle
      start time.
    - or after the vehicle end (ditto, with the vehicle end time).

    Attributes:
        break_requests (MutableSequence[google.cloud.optimization_v1.types.BreakRule.BreakRequest]):
            Sequence of breaks. See the ``BreakRequest`` message.
        frequency_constraints (MutableSequence[google.cloud.optimization_v1.types.BreakRule.FrequencyConstraint]):
            Several ``FrequencyConstraint`` may apply. They must all be
            satisfied by the ``BreakRequest``\ s of this ``BreakRule``.
            See ``FrequencyConstraint``.
    """

    class BreakRequest(proto.Message):
        r"""The sequence of breaks (i.e. their number and order) that apply to
        each vehicle must be known beforehand. The repeated
        ``BreakRequest``\ s define that sequence, in the order in which they
        must occur. Their time windows (``earliest_start_time`` /
        ``latest_start_time``) may overlap, but they must be compatible with
        the order (this is checked).

        Attributes:
            earliest_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Lower bound (inclusive) on the
                start of the break.
            latest_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Upper bound (inclusive) on the
                start of the break.
            min_duration (google.protobuf.duration_pb2.Duration):
                Required. Minimum duration of the break. Must
                be positive.
        """

        earliest_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        latest_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        min_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )

    class FrequencyConstraint(proto.Message):
        r"""One may further constrain the frequency and duration of the breaks
        specified above, by enforcing a minimum break frequency, such as
        "There must be a break of at least 1 hour every 12 hours". Assuming
        that this can be interpreted as "Within any sliding time window of
        12h, there must be at least one break of at least one hour", that
        example would translate to the following ``FrequencyConstraint``:

        ::

           {
              min_break_duration { seconds: 3600 }         # 1 hour.
              max_inter_break_duration { seconds: 39600 }  # 11 hours (12 - 1 = 11).
           }

        The timing and duration of the breaks in the solution will respect
        all such constraints, in addition to the time windows and minimum
        durations already specified in the ``BreakRequest``.

        A ``FrequencyConstraint`` may in practice apply to non-consecutive
        breaks. For example, the following schedule honors the "1h every
        12h" example:

        ::

             04:00 vehicle start
              .. performing travel and visits ..
             09:00 1 hour break
             10:00 end of the break
              .. performing travel and visits ..
             12:00 20-min lunch break
             12:20 end of the break
              .. performing travel and visits ..
             21:00 1 hour break
             22:00 end of the break
              .. performing travel and visits ..
             23:59 vehicle end

        Attributes:
            min_break_duration (google.protobuf.duration_pb2.Duration):
                Required. Minimum break duration for this constraint.
                Nonnegative. See description of ``FrequencyConstraint``.
            max_inter_break_duration (google.protobuf.duration_pb2.Duration):
                Required. Maximum allowed span of any interval of time in
                the route that does not include at least partially a break
                of ``duration >= min_break_duration``. Must be positive.
        """

        min_break_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        max_inter_break_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    break_requests: MutableSequence[BreakRequest] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=BreakRequest,
    )
    frequency_constraints: MutableSequence[FrequencyConstraint] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=FrequencyConstraint,
    )


class ShipmentRoute(proto.Message):
    r"""A vehicle's route can be decomposed, along the time axis, like this
    (we assume there are n visits):

    ::

         |            |            |          |       |  T[2], |        |      |
         | Transition |  Visit #0  |          |       |  V[2], |        |      |
         |     #0     |    aka     |   T[1]   |  V[1] |  ...   | V[n-1] | T[n] |
         |  aka T[0]  |    V[0]    |          |       | V[n-2],|        |      |
         |            |            |          |       | T[n-1] |        |      |
         ^            ^            ^          ^       ^        ^        ^      ^
       vehicle    V[0].start   V[0].end     V[1].   V[1].    V[n].    V[n]. vehicle
        start     (arrival)   (departure)   start   end      start    end     end

    Note that we make a difference between:

    - "punctual events", such as the vehicle start and end and each
      visit's start and end (aka arrival and departure). They happen at
      a given second.
    - "time intervals", such as the visits themselves, and the
      transition between visits. Though time intervals can sometimes
      have zero duration, i.e. start and end at the same second, they
      often have a positive duration.

    Invariants:

    - If there are n visits, there are n+1 transitions.
    - A visit is always surrounded by a transition before it (same
      index) and a transition after it (index + 1).
    - The vehicle start is always followed by transition #0.
    - The vehicle end is always preceded by transition #n.

    Zooming in, here is what happens during a ``Transition`` and a
    ``Visit``:

    ::

       ---+-------------------------------------+-----------------------------+-->
          |           TRANSITION[i]             |           VISIT[i]          |
          |                                     |                             |
          |  * TRAVEL: the vehicle moves from   |      PERFORM the visit:     |
          |    VISIT[i-1].departure_location to |                             |
          |    VISIT[i].arrival_location, which |  * Spend some time:         |
          |    takes a given travel duration    |    the "visit duration".    |
          |    and distance                     |                             |
          |                                     |  * Load or unload           |
          |  * BREAKS: the driver may have      |    some quantities from the |
          |    breaks (e.g. lunch break).       |    vehicle: the "demand".   |
          |                                     |                             |
          |  * WAIT: the driver/vehicle does    |                             |
          |    nothing. This can happen for     |                             |
          |    many reasons, for example when   |                             |
          |    the vehicle reaches the next     |                             |
          |    event's destination before the   |                             |
          |    start of its time window         |                             |
          |                                     |                             |
          |  * DELAY: *right before* the next   |                             |
          |    arrival. E.g. the vehicle and/or |                             |
          |    driver spends time unloading.    |                             |
          |                                     |                             |
       ---+-------------------------------------+-----------------------------+-->
          ^                                     ^                             ^
       V[i-1].end                           V[i].start                    V[i].end

    Lastly, here is how the TRAVEL, BREAKS, DELAY and WAIT can be
    arranged during a transition.

    - They don't overlap.
    - The DELAY is unique and *must* be a contiguous period of time
      right before the next visit (or vehicle end). Thus, it suffice to
      know the delay duration to know its start and end time.
    - The BREAKS are contiguous, non-overlapping periods of time. The
      response specifies the start time and duration of each break.
    - TRAVEL and WAIT are "preemptable": they can be interrupted several
      times during this transition. Clients can assume that travel
      happens "as soon as possible" and that "wait" fills the remaining
      time.

    A (complex) example:

    ::

                                      TRANSITION[i]
       --++-----+-----------------------------------------------------------++-->
         ||     |       |           |       |           |         |         ||
         ||  T  |   B   |     T     |       |     B     |         |    D    ||
         ||  r  |   r   |     r     |   W   |     r     |    W    |    e    ||
         ||  a  |   e   |     a     |   a   |     e     |    a    |    l    ||
         ||  v  |   a   |     v     |   i   |     a     |    i    |    a    ||
         ||  e  |   k   |     e     |   t   |     k     |    t    |    y    ||
         ||  l  |       |     l     |       |           |         |         ||
         ||     |       |           |       |           |         |         ||
       --++-----------------------------------------------------------------++-->

    Attributes:
        vehicle_index (int):
            Vehicle performing the route, identified by its index in the
            source ``ShipmentModel``.
        vehicle_label (str):
            Label of the vehicle performing this route, equal to
            ``ShipmentModel.vehicles(vehicle_index).label``, if
            specified.
        vehicle_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Time at which the vehicle starts its route.
        vehicle_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Time at which the vehicle finishes its route.
        visits (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute.Visit]):
            Ordered sequence of visits representing a route. visits[i]
            is the i-th visit in the route. If this field is empty, the
            vehicle is considered as unused.
        transitions (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute.Transition]):
            Ordered list of transitions for the route.
        has_traffic_infeasibilities (bool):
            When
            [OptimizeToursRequest.consider_road_traffic][google.cloud.optimization.v1.OptimizeToursRequest.consider_road_traffic],
            is set to true, this field indicates that inconsistencies in
            route timings are predicted using traffic-based travel
            duration estimates. There may be insufficient time to
            complete traffic-adjusted travel, delays, and breaks between
            visits, before the first visit, or after the last visit,
            while still satisfying the visit and vehicle time windows.
            For example,

            ::

                 start_time(previous_visit) + duration(previous_visit) +
                 travel_duration(previous_visit, next_visit) > start_time(next_visit)

            Arrival at next_visit will likely happen later than its
            current time window due the increased estimate of travel
            time ``travel_duration(previous_visit, next_visit)`` due to
            traffic. Also, a break may be forced to overlap with a visit
            due to an increase in travel time estimates and visit or
            break time window restrictions.
        route_polyline (google.cloud.optimization_v1.types.ShipmentRoute.EncodedPolyline):
            The encoded polyline representation of the route. This field
            is only populated if
            [OptimizeToursRequest.populate_polylines][google.cloud.optimization.v1.OptimizeToursRequest.populate_polylines]
            is set to true.
        breaks (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute.Break]):
            Breaks scheduled for the vehicle performing this route. The
            ``breaks`` sequence represents time intervals, each starting
            at the corresponding ``start_time`` and lasting ``duration``
            seconds.
        metrics (google.cloud.optimization_v1.types.AggregatedMetrics):
            Duration, distance and load metrics for this route. The
            fields of
            [AggregatedMetrics][google.cloud.optimization.v1.AggregatedMetrics]
            are summed over all
            [ShipmentRoute.transitions][google.cloud.optimization.v1.ShipmentRoute.transitions]
            or
            [ShipmentRoute.visits][google.cloud.optimization.v1.ShipmentRoute.visits],
            depending on the context.
        route_costs (MutableMapping[str, float]):
            Cost of the route, broken down by cost-related request
            fields. The keys are proto paths, relative to the input
            OptimizeToursRequest, e.g. "model.shipments.pickups.cost",
            and the values are the total cost generated by the
            corresponding cost field, aggregated over the whole route.
            In other words, costs["model.shipments.pickups.cost"] is the
            sum of all pickup costs over the route. All costs defined in
            the model are reported in detail here with the exception of
            costs related to TransitionAttributes that are only reported
            in an aggregated way as of 2022/01.
        route_total_cost (float):
            Total cost of the route. The sum of all costs
            in the cost map.
        end_loads (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
            Deprecated: Use
            [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads]
            instead. Vehicle loads upon arrival at its end location, for
            each type specified in
            [Vehicle.capacities][google.cloud.optimization.v1.Vehicle.capacities],
            ``start_load_intervals``, ``end_load_intervals`` or demands.
            Exception: we omit loads for quantity types unconstrained by
            intervals and that don't have any non-zero demand on the
            route.
        travel_steps (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute.TravelStep]):
            Deprecated: Use
            [ShipmentRoute.transitions][google.cloud.optimization.v1.ShipmentRoute.transitions]
            instead. Ordered list of travel steps for the route.
        vehicle_detour (google.protobuf.duration_pb2.Duration):
            Deprecated: No longer used. This field will only be
            populated at the
            [ShipmentRoute.Visit][google.cloud.optimization.v1.ShipmentRoute.Visit]
            level.

            This field is the extra detour time due to the shipments
            visited on the route.

            It is equal to ``vehicle_end_time`` - ``vehicle_start_time``
            - travel duration from the vehicle's start_location to its
            ``end_location``.
        delay_before_vehicle_end (google.cloud.optimization_v1.types.ShipmentRoute.Delay):
            Deprecated: Delay occurring before the vehicle end. See
            [TransitionAttributes.delay][google.cloud.optimization.v1.TransitionAttributes.delay].
    """

    class Delay(proto.Message):
        r"""Deprecated: Use
        [ShipmentRoute.Transition.delay_duration][google.cloud.optimization.v1.ShipmentRoute.Transition.delay_duration]
        instead. Time interval spent on the route resulting from a
        [TransitionAttributes.delay][google.cloud.optimization.v1.TransitionAttributes.delay].

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start of the delay.
            duration (google.protobuf.duration_pb2.Duration):
                Duration of the delay.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    class Visit(proto.Message):
        r"""A visit performed during a route. This visit corresponds to a pickup
        or a delivery of a ``Shipment``.

        Attributes:
            shipment_index (int):
                Index of the ``shipments`` field in the source
                [ShipmentModel][google.cloud.optimization.v1.ShipmentModel].
            is_pickup (bool):
                If true the visit corresponds to a pickup of a ``Shipment``.
                Otherwise, it corresponds to a delivery.
            visit_request_index (int):
                Index of ``VisitRequest`` in either the pickup or delivery
                field of the ``Shipment`` (see ``is_pickup``).
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Time at which the visit starts. Note that the vehicle may
                arrive earlier than this at the visit location. Times are
                consistent with the ``ShipmentModel``.
            load_demands (MutableMapping[str, google.cloud.optimization_v1.types.Shipment.Load]):
                Total visit load demand as the sum of the shipment and the
                visit request ``load_demands``. The values are negative if
                the visit is a delivery. Demands are reported for the same
                types as the
                [Transition.loads][google.cloud.optimization.v1.ShipmentRoute.Transition]
                (see this field).
            detour (google.protobuf.duration_pb2.Duration):
                Extra detour time due to the shipments visited on the route
                before the visit and to the potential waiting time induced
                by time windows. If the visit is a delivery, the detour is
                computed from the corresponding pickup visit and is equal
                to:

                ::

                   start_time(delivery) - start_time(pickup)
                   - (duration(pickup) + travel duration from the pickup location
                   to the delivery location).

                Otherwise, it is computed from the vehicle
                ``start_location`` and is equal to:

                ::

                   start_time - vehicle_start_time - travel duration from
                   the vehicle's `start_location` to the visit.
            shipment_label (str):
                Copy of the corresponding ``Shipment.label``, if specified
                in the ``Shipment``.
            visit_label (str):
                Copy of the corresponding
                [VisitRequest.label][google.cloud.optimization.v1.Shipment.VisitRequest.label],
                if specified in the ``VisitRequest``.
            arrival_loads (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
                Deprecated: Use
                [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads]
                instead. Vehicle loads upon arrival at the visit location,
                for each type specified in
                [Vehicle.capacities][google.cloud.optimization.v1.Vehicle.capacities],
                ``start_load_intervals``, ``end_load_intervals`` or
                ``demands``.

                Exception: we omit loads for quantity types unconstrained by
                intervals and that don't have any non-zero demand on the
                route.
            delay_before_start (google.cloud.optimization_v1.types.ShipmentRoute.Delay):
                Deprecated: Use
                [ShipmentRoute.Transition.delay_duration][google.cloud.optimization.v1.ShipmentRoute.Transition.delay_duration]
                instead. Delay occurring before the visit starts.
            demands (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
                Deprecated: Use
                [Visit.load_demands][google.cloud.optimization.v1.ShipmentRoute.Visit.load_demands]
                instead.
        """

        shipment_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        is_pickup: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        visit_request_index: int = proto.Field(
            proto.INT32,
            number=3,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        load_demands: MutableMapping[str, "Shipment.Load"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=11,
            message="Shipment.Load",
        )
        detour: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
        shipment_label: str = proto.Field(
            proto.STRING,
            number=7,
        )
        visit_label: str = proto.Field(
            proto.STRING,
            number=8,
        )
        arrival_loads: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="CapacityQuantity",
        )
        delay_before_start: "ShipmentRoute.Delay" = proto.Field(
            proto.MESSAGE,
            number=10,
            message="ShipmentRoute.Delay",
        )
        demands: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="CapacityQuantity",
        )

    class Transition(proto.Message):
        r"""Transition between two events on the route. See the description of
        [ShipmentRoute][google.cloud.optimization.v1.ShipmentRoute].

        If the vehicle does not have a ``start_location`` and/or
        ``end_location``, the corresponding travel metrics are 0.

        Attributes:
            travel_duration (google.protobuf.duration_pb2.Duration):
                Travel duration during this transition.
            travel_distance_meters (float):
                Distance traveled during the transition.
            traffic_info_unavailable (bool):
                When traffic is requested via
                [OptimizeToursRequest.consider_road_traffic]
                [google.cloud.optimization.v1.OptimizeToursRequest.consider_road_traffic],
                and the traffic info couldn't be retrieved for a
                ``Transition``, this boolean is set to true. This may be
                temporary (rare hiccup in the realtime traffic servers) or
                permanent (no data for this location).
            delay_duration (google.protobuf.duration_pb2.Duration):
                Sum of the delay durations applied to this transition. If
                any, the delay starts exactly ``delay_duration`` seconds
                before the next event (visit or vehicle end). See
                [TransitionAttributes.delay][google.cloud.optimization.v1.TransitionAttributes.delay].
            break_duration (google.protobuf.duration_pb2.Duration):
                Sum of the duration of the breaks occurring during this
                transition, if any. Details about each break's start time
                and duration are stored in
                [ShipmentRoute.breaks][google.cloud.optimization.v1.ShipmentRoute.breaks].
            wait_duration (google.protobuf.duration_pb2.Duration):
                Time spent waiting during this transition.
                Wait duration corresponds to idle time and does
                not include break time. Also note that this wait
                time may be split into several non-contiguous
                intervals.
            total_duration (google.protobuf.duration_pb2.Duration):
                Total duration of the transition, provided for convenience.
                It is equal to:

                - next visit ``start_time`` (or ``vehicle_end_time`` if this
                  is the last transition) - this transition's
                  ``start_time``;
                - if ``ShipmentRoute.has_traffic_infeasibilities`` is false,
                  the following additionally holds: \`total_duration =
                  travel_duration + delay_duration

                - break_duration + wait_duration\`.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start time of this transition.
            route_polyline (google.cloud.optimization_v1.types.ShipmentRoute.EncodedPolyline):
                The encoded polyline representation of the route followed
                during the transition. This field is only populated if
                [populate_transition_polylines]
                [google.cloud.optimization.v1.OptimizeToursRequest.populate_transition_polylines]
                is set to true.
            vehicle_loads (MutableMapping[str, google.cloud.optimization_v1.types.ShipmentRoute.VehicleLoad]):
                Vehicle loads during this transition, for each type that
                either appears in this vehicle's
                [Vehicle.load_limits][google.cloud.optimization.v1.Vehicle.load_limits],
                or that have non-zero
                [Shipment.load_demands][google.cloud.optimization.v1.Shipment.load_demands]
                on some shipment performed on this route.

                The loads during the first transition are the starting loads
                of the vehicle route. Then, after each visit, the visit's
                ``load_demands`` are either added or subtracted to get the
                next transition's loads, depending on whether the visit was
                a pickup or a delivery.
            loads (MutableSequence[google.cloud.optimization_v1.types.CapacityQuantity]):
                Deprecated: Use
                [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads]
                instead.
        """

        travel_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        travel_distance_meters: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        traffic_info_unavailable: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        delay_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        break_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        wait_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
        total_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=8,
            message=timestamp_pb2.Timestamp,
        )
        route_polyline: "ShipmentRoute.EncodedPolyline" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="ShipmentRoute.EncodedPolyline",
        )
        vehicle_loads: MutableMapping[str, "ShipmentRoute.VehicleLoad"] = (
            proto.MapField(
                proto.STRING,
                proto.MESSAGE,
                number=11,
                message="ShipmentRoute.VehicleLoad",
            )
        )
        loads: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="CapacityQuantity",
        )

    class VehicleLoad(proto.Message):
        r"""Reports the actual load of the vehicle at some point along the
        route, for a given type (see
        [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads]).

        Attributes:
            amount (int):
                The amount of load on the vehicle, for the given type. The
                unit of load is usually indicated by the type. See
                [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads].
        """

        amount: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class EncodedPolyline(proto.Message):
        r"""The encoded representation of a polyline. More information on
        polyline encoding can be found here:

        https://developers.google.com/maps/documentation/utilities/polylinealgorithm
        https://developers.google.com/maps/documentation/javascript/reference/geometry#encoding.

        Attributes:
            points (str):
                String representing encoded points of the
                polyline.
        """

        points: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Break(proto.Message):
        r"""Data representing the execution of a break.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start time of a break.
            duration (google.protobuf.duration_pb2.Duration):
                Duration of a break.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    class TravelStep(proto.Message):
        r"""Deprecated: Use
        [ShipmentRoute.Transition][google.cloud.optimization.v1.ShipmentRoute.Transition]
        instead. Travel between each visit along the route: from the
        vehicle's ``start_location`` to the first visit's
        ``arrival_location``, then from the first visit's
        ``departure_location`` to the second visit's ``arrival_location``,
        and so on until the vehicle's ``end_location``. This accounts only
        for the actual travel between visits, not counting the waiting time,
        the time spent performing a visit, nor the distance covered during a
        visit.

        Invariant: ``travel_steps_size() == visits_size() + 1``.

        If the vehicle does not have a start\_ and/or end_location, the
        corresponding travel metrics are 0 and/or empty.

        Attributes:
            duration (google.protobuf.duration_pb2.Duration):
                Duration of the travel step.
            distance_meters (float):
                Distance traveled during the step.
            traffic_info_unavailable (bool):
                When traffic is requested via
                [OptimizeToursRequest.consider_road_traffic][google.cloud.optimization.v1.OptimizeToursRequest.consider_road_traffic],
                and the traffic info couldn't be retrieved for a TravelStep,
                this boolean is set to true. This may be temporary (rare
                hiccup in the realtime traffic servers) or permanent (no
                data for this location).
            route_polyline (google.cloud.optimization_v1.types.ShipmentRoute.EncodedPolyline):
                The encoded polyline representation of the route followed
                during the step.

                This field is only populated if
                [OptimizeToursRequest.populate_travel_step_polylines][google.cloud.optimization.v1.OptimizeToursRequest.populate_travel_step_polylines]
                is set to true.
        """

        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        distance_meters: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        traffic_info_unavailable: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        route_polyline: "ShipmentRoute.EncodedPolyline" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="ShipmentRoute.EncodedPolyline",
        )

    vehicle_index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    vehicle_label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vehicle_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    vehicle_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    visits: MutableSequence[Visit] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=Visit,
    )
    transitions: MutableSequence[Transition] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=Transition,
    )
    has_traffic_infeasibilities: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    route_polyline: EncodedPolyline = proto.Field(
        proto.MESSAGE,
        number=10,
        message=EncodedPolyline,
    )
    breaks: MutableSequence[Break] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=Break,
    )
    metrics: "AggregatedMetrics" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AggregatedMetrics",
    )
    route_costs: MutableMapping[str, float] = proto.MapField(
        proto.STRING,
        proto.DOUBLE,
        number=17,
    )
    route_total_cost: float = proto.Field(
        proto.DOUBLE,
        number=18,
    )
    end_loads: MutableSequence["CapacityQuantity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="CapacityQuantity",
    )
    travel_steps: MutableSequence[TravelStep] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=TravelStep,
    )
    vehicle_detour: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=15,
        message=duration_pb2.Duration,
    )
    delay_before_vehicle_end: Delay = proto.Field(
        proto.MESSAGE,
        number=16,
        message=Delay,
    )


class SkippedShipment(proto.Message):
    r"""Specifies details of unperformed shipments in a solution. For
    trivial cases and/or if we are able to identify the cause for
    skipping, we report the reason here.

    Attributes:
        index (int):
            The index corresponds to the index of the shipment in the
            source ``ShipmentModel``.
        label (str):
            Copy of the corresponding
            [Shipment.label][google.cloud.optimization.v1.Shipment.label],
            if specified in the ``Shipment``.
        reasons (MutableSequence[google.cloud.optimization_v1.types.SkippedShipment.Reason]):
            A list of reasons that explain why the shipment was skipped.
            See comment above ``Reason``.
    """

    class Reason(proto.Message):
        r"""If we can explain why the shipment was skipped, reasons will be
        listed here. If the reason is not the same for all vehicles,
        ``reason`` will have more than 1 element. A skipped shipment cannot
        have duplicate reasons, i.e. where all fields are the same except
        for ``example_vehicle_index``. Example:

        ::

           reasons {
             code: DEMAND_EXCEEDS_VEHICLE_CAPACITY
             example_vehicle_index: 1
             example_exceeded_capacity_type: "Apples"
           }
           reasons {
             code: DEMAND_EXCEEDS_VEHICLE_CAPACITY
             example_vehicle_index: 3
             example_exceeded_capacity_type: "Pears"
           }
           reasons {
             code: CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DISTANCE_LIMIT
             example_vehicle_index: 1
           }

        The skipped shipment is incompatible with all vehicles. The reasons
        may be different for all vehicles but at least one vehicle's
        "Apples" capacity would be exceeded (including vehicle 1), at least
        one vehicle's "Pears" capacity would be exceeded (including vehicle
        3) and at least one vehicle's distance limit would be exceeded
        (including vehicle 1).


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            code (google.cloud.optimization_v1.types.SkippedShipment.Reason.Code):
                Refer to the comments of Code.
            example_vehicle_index (int):
                If the reason is related to a
                shipment-vehicle incompatibility, this field
                provides the index of one relevant vehicle.

                This field is a member of `oneof`_ ``_example_vehicle_index``.
            example_exceeded_capacity_type (str):
                If the reason code is ``DEMAND_EXCEEDS_VEHICLE_CAPACITY``,
                documents one capacity type that is exceeded.
        """

        class Code(proto.Enum):
            r"""Code identifying the reason type. The order here is
            meaningless. In particular, it gives no indication of whether a
            given reason will appear before another in the solution, if both
            apply.

            Values:
                CODE_UNSPECIFIED (0):
                    This should never be used. If we are unable
                    to understand why a shipment was skipped, we
                    simply return an empty set of reasons.
                NO_VEHICLE (1):
                    There is no vehicle in the model making all
                    shipments infeasible.
                DEMAND_EXCEEDS_VEHICLE_CAPACITY (2):
                    The demand of the shipment exceeds a vehicle's capacity for
                    some capacity types, one of which is
                    ``example_exceeded_capacity_type``.
                CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DISTANCE_LIMIT (3):
                    The minimum distance necessary to perform this shipment,
                    i.e. from the vehicle's ``start_location`` to the shipment's
                    pickup and/or delivery locations and to the vehicle's end
                    location exceeds the vehicle's ``route_distance_limit``.

                    Note that for this computation we use the geodesic
                    distances.
                CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DURATION_LIMIT (4):
                    The minimum time necessary to perform this shipment,
                    including travel time, wait time and service time exceeds
                    the vehicle's ``route_duration_limit``.

                    Note: travel time is computed in the best-case scenario,
                    namely as geodesic distance x 36 m/s (roughly 130 km/hour).
                CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TRAVEL_DURATION_LIMIT (5):
                    Same as above but we only compare minimum travel time and
                    the vehicle's ``travel_duration_limit``.
                CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TIME_WINDOWS (6):
                    The vehicle cannot perform this shipment in the best-case
                    scenario (see
                    ``CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DURATION_LIMIT`` for
                    time computation) if it starts at its earliest start time:
                    the total time would make the vehicle end after its latest
                    end time.
                VEHICLE_NOT_ALLOWED (7):
                    The ``allowed_vehicle_indices`` field of the shipment is not
                    empty and this vehicle does not belong to it.
            """

            CODE_UNSPECIFIED = 0
            NO_VEHICLE = 1
            DEMAND_EXCEEDS_VEHICLE_CAPACITY = 2
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DISTANCE_LIMIT = 3
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DURATION_LIMIT = 4
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TRAVEL_DURATION_LIMIT = 5
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TIME_WINDOWS = 6
            VEHICLE_NOT_ALLOWED = 7

        code: "SkippedShipment.Reason.Code" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SkippedShipment.Reason.Code",
        )
        example_vehicle_index: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )
        example_exceeded_capacity_type: str = proto.Field(
            proto.STRING,
            number=3,
        )

    index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reasons: MutableSequence[Reason] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Reason,
    )


class AggregatedMetrics(proto.Message):
    r"""Aggregated metrics for
    [ShipmentRoute][google.cloud.optimization.v1.ShipmentRoute] (resp.
    for
    [OptimizeToursResponse][google.cloud.optimization.v1.OptimizeToursResponse]
    over all
    [Transition][google.cloud.optimization.v1.ShipmentRoute.Transition]
    and/or [Visit][google.cloud.optimization.v1.ShipmentRoute.Visit]
    (resp. over all
    [ShipmentRoute][google.cloud.optimization.v1.ShipmentRoute])
    elements.

    Attributes:
        performed_shipment_count (int):
            Number of shipments performed. Note that a
            pickup and delivery pair only counts once.
        travel_duration (google.protobuf.duration_pb2.Duration):
            Total travel duration for a route or a
            solution.
        wait_duration (google.protobuf.duration_pb2.Duration):
            Total wait duration for a route or a
            solution.
        delay_duration (google.protobuf.duration_pb2.Duration):
            Total delay duration for a route or a
            solution.
        break_duration (google.protobuf.duration_pb2.Duration):
            Total break duration for a route or a
            solution.
        visit_duration (google.protobuf.duration_pb2.Duration):
            Total visit duration for a route or a
            solution.
        total_duration (google.protobuf.duration_pb2.Duration):
            The total duration should be equal to the sum of all
            durations above. For routes, it also corresponds to:
            [ShipmentRoute.vehicle_end_time][google.cloud.optimization.v1.ShipmentRoute.vehicle_end_time]
            ``-``
            [ShipmentRoute.vehicle_start_time][google.cloud.optimization.v1.ShipmentRoute.vehicle_start_time]
        travel_distance_meters (float):
            Total travel distance for a route or a
            solution.
        max_loads (MutableMapping[str, google.cloud.optimization_v1.types.ShipmentRoute.VehicleLoad]):
            Maximum load achieved over the entire route (resp.
            solution), for each of the quantities on this route (resp.
            solution), computed as the maximum over all
            [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads]
            (resp.
            [ShipmentRoute.metrics.max_loads][google.cloud.optimization.v1.AggregatedMetrics.max_loads].
        costs (MutableMapping[str, float]):
            Deprecated: Use
            [ShipmentRoute.route_costs][google.cloud.optimization.v1.ShipmentRoute.route_costs]
            and
            [OptimizeToursResponse.Metrics.costs][google.cloud.optimization.v1.OptimizeToursResponse.Metrics.costs]
            instead.
        total_cost (float):
            Deprecated: Use
            [ShipmentRoute.route_total_cost][google.cloud.optimization.v1.ShipmentRoute.route_total_cost]
            and
            [OptimizeToursResponse.Metrics.total_cost][google.cloud.optimization.v1.OptimizeToursResponse.Metrics.total_cost]
            instead.
    """

    performed_shipment_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    travel_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    wait_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    delay_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    break_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    visit_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    total_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    travel_distance_meters: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    max_loads: MutableMapping[str, "ShipmentRoute.VehicleLoad"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=9,
        message="ShipmentRoute.VehicleLoad",
    )
    costs: MutableMapping[str, float] = proto.MapField(
        proto.STRING,
        proto.DOUBLE,
        number=10,
    )
    total_cost: float = proto.Field(
        proto.DOUBLE,
        number=11,
    )


class InjectedSolutionConstraint(proto.Message):
    r"""Solution injected in the request including information about
    which visits must be constrained and how they must be
    constrained.

    Attributes:
        routes (MutableSequence[google.cloud.optimization_v1.types.ShipmentRoute]):
            Routes of the solution to inject. Some routes may be omitted
            from the original solution. The routes and skipped shipments
            must satisfy the basic validity assumptions listed for
            ``injected_first_solution_routes``.
        skipped_shipments (MutableSequence[google.cloud.optimization_v1.types.SkippedShipment]):
            Skipped shipments of the solution to inject. Some may be
            omitted from the original solution. See the ``routes``
            field.
        constraint_relaxations (MutableSequence[google.cloud.optimization_v1.types.InjectedSolutionConstraint.ConstraintRelaxation]):
            For zero or more groups of vehicles,
            specifies when and how much to relax
            constraints. If this field is empty, all
            non-empty vehicle routes are fully constrained.
    """

    class ConstraintRelaxation(proto.Message):
        r"""For a group of vehicles, specifies at what threshold(s) constraints
        on visits will be relaxed and to which level. Shipments listed in
        the ``skipped_shipment`` field are constrained to be skipped; i.e.,
        they cannot be performed.

        Attributes:
            relaxations (MutableSequence[google.cloud.optimization_v1.types.InjectedSolutionConstraint.ConstraintRelaxation.Relaxation]):
                All the visit constraint relaxations that will apply to
                visits on routes with vehicles in ``vehicle_indices``.
            vehicle_indices (MutableSequence[int]):
                Specifies the vehicle indices to which the visit constraint
                ``relaxations`` apply. If empty, this is considered the
                default and the ``relaxations`` apply to all vehicles that
                are not specified in other ``constraint_relaxations``. There
                can be at most one default, i.e., at most one constraint
                relaxation field is allowed empty ``vehicle_indices``. A
                vehicle index can only be listed once, even within several
                ``constraint_relaxations``.

                A vehicle index is mapped the same as
                [ShipmentRoute.vehicle_index][google.cloud.optimization.v1.ShipmentRoute.vehicle_index],
                if ``interpret_injected_solutions_using_labels`` is true
                (see ``fields`` comment).
        """

        class Relaxation(proto.Message):
            r"""If ``relaxations`` is empty, the start time and sequence of all
            visits on ``routes`` are fully constrained and no new visits may be
            inserted or added to those routes. Also, a vehicle's start and end
            time in ``routes`` is fully constrained, unless the vehicle is empty
            (i.e., has no visits and has ``used_if_route_is_empty`` set to false
            in the model).

            ``relaxations(i).level`` specifies the constraint relaxation level
            applied to a visit #j that satisfies:

            - ``route.visits(j).start_time >= relaxations(i).threshold_time``
              AND
            - ``j + 1 >= relaxations(i).threshold_visit_count``

            Similarly, the vehicle start is relaxed to ``relaxations(i).level``
            if it satisfies:

            - ``vehicle_start_time >= relaxations(i).threshold_time`` AND
            - ``relaxations(i).threshold_visit_count == 0`` and the vehicle end
              is relaxed to ``relaxations(i).level`` if it satisfies:
            - ``vehicle_end_time >= relaxations(i).threshold_time`` AND
            - ``route.visits_size() + 1 >= relaxations(i).threshold_visit_count``

            To apply a relaxation level if a visit meets the
            ``threshold_visit_count`` OR the ``threshold_time`` add two
            ``relaxations`` with the same ``level``: one with only
            ``threshold_visit_count`` set and the other with only
            ``threshold_time`` set. If a visit satisfies the conditions of
            multiple ``relaxations``, the most relaxed level applies. As a
            result, from the vehicle start through the route visits in order to
            the vehicle end, the relaxation level becomes more relaxed: i.e.,
            the relaxation level is non-decreasing as the route progresses.

            The timing and sequence of route visits that do not satisfy the
            threshold conditions of any ``relaxations`` are fully constrained
            and no visits may be inserted into these sequences. Also, if a
            vehicle start or end does not satisfy the conditions of any
            relaxation the time is fixed, unless the vehicle is empty.

            Attributes:
                level (google.cloud.optimization_v1.types.InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level):
                    The constraint relaxation level that applies when the
                    conditions at or after ``threshold_time`` AND at least
                    ``threshold_visit_count`` are satisfied.
                threshold_time (google.protobuf.timestamp_pb2.Timestamp):
                    The time at or after which the relaxation ``level`` may be
                    applied.
                threshold_visit_count (int):
                    The number of visits at or after which the relaxation
                    ``level`` may be applied. If ``threshold_visit_count`` is 0
                    (or unset), the ``level`` may be applied directly at the
                    vehicle start.

                    If it is ``route.visits_size() + 1``, the ``level`` may only
                    be applied to the vehicle end. If it is more than
                    ``route.visits_size() + 1``, ``level`` is not applied at all
                    for that route.
            """

            class Level(proto.Enum):
                r"""Expresses the different constraint relaxation levels, which
                are applied for a visit and those that follow when it satisfies
                the threshold conditions.

                The enumeration below is in order of increasing relaxation.

                Values:
                    LEVEL_UNSPECIFIED (0):
                        Implicit default relaxation level: no constraints are
                        relaxed, i.e., all visits are fully constrained.

                        This value must not be explicitly used in ``level``.
                    RELAX_VISIT_TIMES_AFTER_THRESHOLD (1):
                        Visit start times and vehicle start/end times
                        will be relaxed, but each visit remains bound to
                        the same vehicle and the visit sequence must be
                        observed: no visit can be inserted between them
                        or before them.
                    RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD (2):
                        Same as ``RELAX_VISIT_TIMES_AFTER_THRESHOLD``, but the visit
                        sequence is also relaxed: visits can only be performed by
                        this vehicle, but can potentially become unperformed.
                    RELAX_ALL_AFTER_THRESHOLD (3):
                        Same as ``RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD``,
                        but the vehicle is also relaxed: visits are completely free
                        at or after the threshold time and can potentially become
                        unperformed.
                """

                LEVEL_UNSPECIFIED = 0
                RELAX_VISIT_TIMES_AFTER_THRESHOLD = 1
                RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD = 2
                RELAX_ALL_AFTER_THRESHOLD = 3

            level: "InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level" = proto.Field(
                proto.ENUM,
                number=1,
                enum="InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level",
            )
            threshold_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                message=timestamp_pb2.Timestamp,
            )
            threshold_visit_count: int = proto.Field(
                proto.INT32,
                number=3,
            )

        relaxations: MutableSequence[
            "InjectedSolutionConstraint.ConstraintRelaxation.Relaxation"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="InjectedSolutionConstraint.ConstraintRelaxation.Relaxation",
        )
        vehicle_indices: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=2,
        )

    routes: MutableSequence["ShipmentRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ShipmentRoute",
    )
    skipped_shipments: MutableSequence["SkippedShipment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SkippedShipment",
    )
    constraint_relaxations: MutableSequence[ConstraintRelaxation] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ConstraintRelaxation,
    )


class OptimizeToursValidationError(proto.Message):
    r"""Describes an error encountered when validating an
    ``OptimizeToursRequest``.

    Attributes:
        code (int):
            A validation error is defined by the pair (``code``,
            ``display_name``) which are always present.

            Other fields (below) provide more context about the error.

            *MULTIPLE ERRORS*: When there are multiple errors, the
            validation process tries to output several of them. Much
            like a compiler, this is an imperfect process. Some
            validation errors will be "fatal", meaning that they stop
            the entire validation process. This is the case for
            ``display_name="UNSPECIFIED"`` errors, among others. Some
            may cause the validation process to skip other errors.

            *STABILITY*: ``code`` and ``display_name`` should be very
            stable. But new codes and display names may appear over
            time, which may cause a given (invalid) request to yield a
            different (``code``, ``display_name``) pair because the new
            error hid the old one (see "MULTIPLE ERRORS").

            *REFERENCE*: A list of all (code, name) pairs:

            - UNSPECIFIED = 0;

            - VALIDATION_TIMEOUT_ERROR = 10; Validation couldn't be
              completed within the deadline.

            - REQUEST_OPTIONS_ERROR = 12;

              - REQUEST_OPTIONS_INVALID_SOLVING_MODE = 1201;
              - REQUEST_OPTIONS_INVALID_MAX_VALIDATION_ERRORS = 1203;
              - REQUEST_OPTIONS_INVALID_GEODESIC_METERS_PER_SECOND =
                1204;
              - REQUEST_OPTIONS_GEODESIC_METERS_PER_SECOND_TOO_SMALL =
                1205;
              - REQUEST_OPTIONS_MISSING_GEODESIC_METERS_PER_SECOND =
                1206;
              - REQUEST_OPTIONS_POPULATE_PATHFINDER_TRIPS_AND_GEODESIC_DISTANCE
                = 1207;
              - REQUEST_OPTIONS_COST_MODEL_OPTIONS_AND_GEODESIC_DISTANCE
                = 1208;
              - REQUEST_OPTIONS_TRAVEL_MODE_INCOMPATIBLE_WITH_TRAFFIC =
                1211;
              - REQUEST_OPTIONS_MULTIPLE_TRAFFIC_FLAVORS = 1212;
              - REQUEST_OPTIONS_INVALID_TRAFFIC_FLAVOR = 1213;
              - REQUEST_OPTIONS_TRAFFIC_ENABLED_WITHOUT_GLOBAL_START_TIME
                = 1214;
              - REQUEST_OPTIONS_TRAFFIC_ENABLED_WITH_PRECEDENCES = 1215;
              - REQUEST_OPTIONS_TRAFFIC_PREFILL_MODE_INVALID = 1216;
              - REQUEST_OPTIONS_TRAFFIC_PREFILL_ENABLED_WITHOUT_TRAFFIC
                = 1217;

            - INJECTED_SOLUTION_ERROR = 20;

              - INJECTED_SOLUTION_MISSING_LABEL = 2000;
              - INJECTED_SOLUTION_DUPLICATE_LABEL = 2001;
              - INJECTED_SOLUTION_AMBIGUOUS_INDEX = 2002;
              - INJECTED_SOLUTION_INFEASIBLE_AFTER_GETTING_TRAVEL_TIMES
                = 2003;
              - INJECTED_SOLUTION_TRANSITION_INCONSISTENT_WITH_ACTUAL_TRAVEL
                = 2004;
              - INJECTED_SOLUTION_CONCURRENT_SOLUTION_TYPES = 2005;
              - INJECTED_SOLUTION_MORE_THAN_ONE_PER_TYPE = 2006;
              - INJECTED_SOLUTION_REFRESH_WITHOUT_POPULATE = 2008;
              - INJECTED_SOLUTION_CONSTRAINED_ROUTE_PORTION_INFEASIBLE =
                2010;

            - SHIPMENT_MODEL_ERROR = 22;

              - SHIPMENT_MODEL_TOO_LARGE = 2200;
              - SHIPMENT_MODEL_TOO_MANY_CAPACITY_TYPES = 2201;
              - SHIPMENT_MODEL_GLOBAL_START_TIME_NEGATIVE_OR_NAN = 2202;
              - SHIPMENT_MODEL_GLOBAL_END_TIME_TOO_LARGE_OR_NAN = 2203;
              - SHIPMENT_MODEL_GLOBAL_START_TIME_AFTER_GLOBAL_END_TIME =
                2204;
              - SHIPMENT_MODEL_GLOBAL_DURATION_TOO_LONG = 2205;
              - SHIPMENT_MODEL_MAX_ACTIVE_VEHICLES_NOT_POSITIVE = 2206;
              - SHIPMENT_MODEL_DURATION_MATRIX_TOO_LARGE = 2207;

            - INDEX_ERROR = 24;

            - TAG_ERROR = 26;

            - TIME_WINDOW_ERROR = 28;

              - TIME_WINDOW_INVALID_START_TIME = 2800;
              - TIME_WINDOW_INVALID_END_TIME = 2801;
              - TIME_WINDOW_INVALID_SOFT_START_TIME = 2802;
              - TIME_WINDOW_INVALID_SOFT_END_TIME = 2803;
              - TIME_WINDOW_OUTSIDE_GLOBAL_TIME_WINDOW = 2804;
              - TIME_WINDOW_START_TIME_AFTER_END_TIME = 2805;
              - TIME_WINDOW_INVALID_COST_PER_HOUR_BEFORE_SOFT_START_TIME
                = 2806;
              - TIME_WINDOW_INVALID_COST_PER_HOUR_AFTER_SOFT_END_TIME =
                2807;
              - TIME_WINDOW_COST_BEFORE_SOFT_START_TIME_WITHOUT_SOFT_START_TIME
                = 2808;
              - TIME_WINDOW_COST_AFTER_SOFT_END_TIME_WITHOUT_SOFT_END_TIME
                = 2809;
              - TIME_WINDOW_SOFT_START_TIME_WITHOUT_COST_BEFORE_SOFT_START_TIME
                = 2810;
              - TIME_WINDOW_SOFT_END_TIME_WITHOUT_COST_AFTER_SOFT_END_TIME
                = 2811;
              - TIME_WINDOW_OVERLAPPING_ADJACENT_OR_EARLIER_THAN_PREVIOUS
                = 2812;
              - TIME_WINDOW_START_TIME_AFTER_SOFT_START_TIME = 2813;
              - TIME_WINDOW_SOFT_START_TIME_AFTER_END_TIME = 2814;
              - TIME_WINDOW_START_TIME_AFTER_SOFT_END_TIME = 2815;
              - TIME_WINDOW_SOFT_END_TIME_AFTER_END_TIME = 2816;
              - TIME_WINDOW_COST_BEFORE_SOFT_START_TIME_SET_AND_MULTIPLE_WINDOWS
                = 2817;
              - TIME_WINDOW_COST_AFTER_SOFT_END_TIME_SET_AND_MULTIPLE_WINDOWS
                = 2818;
              - TRANSITION_ATTRIBUTES_ERROR = 30;
              - TRANSITION_ATTRIBUTES_INVALID_COST = 3000;
              - TRANSITION_ATTRIBUTES_INVALID_COST_PER_KILOMETER = 3001;
              - TRANSITION_ATTRIBUTES_DUPLICATE_TAG_PAIR = 3002;
              - TRANSITION_ATTRIBUTES_DISTANCE_LIMIT_MAX_METERS_UNSUPPORTED
                = 3003;
              - TRANSITION_ATTRIBUTES_UNSPECIFIED_SOURCE_TAGS = 3004;
              - TRANSITION_ATTRIBUTES_CONFLICTING_SOURCE_TAGS_FIELDS =
                3005;
              - TRANSITION_ATTRIBUTES_UNSPECIFIED_DESTINATION_TAGS =
                3006;
              - TRANSITION_ATTRIBUTES_CONFLICTING_DESTINATION_TAGS_FIELDS
                = 3007;
              - TRANSITION_ATTRIBUTES_DELAY_DURATION_NEGATIVE_OR_NAN =
                3008;
              - TRANSITION_ATTRIBUTES_DELAY_DURATION_EXCEEDS_GLOBAL_DURATION
                = 3009;

            - AMOUNT_ERROR = 31;

              - AMOUNT_NEGATIVE_VALUE = 3100;

            - LOAD_LIMIT_ERROR = 33;

              - LOAD_LIMIT_INVALID_COST_ABOVE_SOFT_MAX = 3303;
              - LOAD_LIMIT_SOFT_MAX_WITHOUT_COST_ABOVE_SOFT_MAX = 3304;
              - LOAD_LIMIT_COST_ABOVE_SOFT_MAX_WITHOUT_SOFT_MAX = 3305;
              - LOAD_LIMIT_NEGATIVE_SOFT_MAX = 3306;
              - LOAD_LIMIT_MIXED_DEMAND_TYPE = 3307;
              - LOAD_LIMIT_MAX_LOAD_NEGATIVE_VALUE = 3308;
              - LOAD_LIMIT_SOFT_MAX_ABOVE_MAX = 3309;

            - INTERVAL_ERROR = 34;

              - INTERVAL_MIN_EXCEEDS_MAX = 3401;
              - INTERVAL_NEGATIVE_MIN = 3402;
              - INTERVAL_NEGATIVE_MAX = 3403;
              - INTERVAL_MIN_EXCEEDS_CAPACITY = 3404;
              - INTERVAL_MAX_EXCEEDS_CAPACITY = 3405;

            - DISTANCE_LIMIT_ERROR = 36;

              - DISTANCE_LIMIT_INVALID_COST_AFTER_SOFT_MAX = 3601;
              - DISTANCE_LIMIT_SOFT_MAX_WITHOUT_COST_AFTER_SOFT_MAX =
                3602;
              - DISTANCE_LIMIT_COST_AFTER_SOFT_MAX_WITHOUT_SOFT_MAX =
                3603;
              - DISTANCE_LIMIT_NEGATIVE_MAX = 3604;
              - DISTANCE_LIMIT_NEGATIVE_SOFT_MAX = 3605;
              - DISTANCE_LIMIT_SOFT_MAX_LARGER_THAN_MAX = 3606;

            - DURATION_LIMIT_ERROR = 38;

              - DURATION_LIMIT_MAX_DURATION_NEGATIVE_OR_NAN = 3800;
              - DURATION_LIMIT_SOFT_MAX_DURATION_NEGATIVE_OR_NAN = 3801;
              - DURATION_LIMIT_INVALID_COST_PER_HOUR_AFTER_SOFT_MAX =
                3802;
              - DURATION_LIMIT_SOFT_MAX_WITHOUT_COST_AFTER_SOFT_MAX =
                3803;
              - DURATION_LIMIT_COST_AFTER_SOFT_MAX_WITHOUT_SOFT_MAX =
                3804;
              - DURATION_LIMIT_QUADRATIC_SOFT_MAX_DURATION_NEGATIVE_OR_NAN
                = 3805;
              - DURATION_LIMIT_INVALID_COST_AFTER_QUADRATIC_SOFT_MAX =
                3806;
              - DURATION_LIMIT_QUADRATIC_SOFT_MAX_WITHOUT_COST_PER_SQUARE_HOUR
                = 3807;
              - DURATION_LIMIT_COST_PER_SQUARE_HOUR_WITHOUT_QUADRATIC_SOFT_MAX
                = 3808;
              - DURATION_LIMIT_QUADRATIC_SOFT_MAX_WITHOUT_MAX = 3809;
              - DURATION_LIMIT_SOFT_MAX_LARGER_THAN_MAX = 3810;
              - DURATION_LIMIT_QUADRATIC_SOFT_MAX_LARGER_THAN_MAX =
                3811;
              - DURATION_LIMIT_DIFF_BETWEEN_MAX_AND_QUADRATIC_SOFT_MAX_TOO_LARGE
                = 3812;
              - DURATION_LIMIT_MAX_DURATION_EXCEEDS_GLOBAL_DURATION =
                3813;
              - DURATION_LIMIT_SOFT_MAX_DURATION_EXCEEDS_GLOBAL_DURATION
                = 3814;
              - DURATION_LIMIT_QUADRATIC_SOFT_MAX_DURATION_EXCEEDS_GLOBAL_DURATION
                = 3815;

            - SHIPMENT_ERROR = 40;

              - SHIPMENT_PD_LIMIT_WITHOUT_PICKUP_AND_DELIVERY = 4014;
              - SHIPMENT_PD_ABSOLUTE_DETOUR_LIMIT_DURATION_NEGATIVE_OR_NAN
                = 4000;
              - SHIPMENT_PD_ABSOLUTE_DETOUR_LIMIT_DURATION_EXCEEDS_GLOBAL_DURATION
                = 4001;
              - SHIPMENT_PD_RELATIVE_DETOUR_LIMIT_INVALID = 4015;
              - SHIPMENT_PD_DETOUR_LIMIT_AND_EXTRA_VISIT_DURATION =
                4016;
              - SHIPMENT_PD_TIME_LIMIT_DURATION_NEGATIVE_OR_NAN = 4002;
              - SHIPMENT_PD_TIME_LIMIT_DURATION_EXCEEDS_GLOBAL_DURATION
                = 4003;
              - SHIPMENT_EMPTY_SHIPMENT_TYPE = 4004;
              - SHIPMENT_NO_PICKUP_NO_DELIVERY = 4005;
              - SHIPMENT_INVALID_PENALTY_COST = 4006;
              - SHIPMENT_ALLOWED_VEHICLE_INDEX_OUT_OF_BOUNDS = 4007;
              - SHIPMENT_DUPLICATE_ALLOWED_VEHICLE_INDEX = 4008;
              - SHIPMENT_INCONSISTENT_COST_FOR_VEHICLE_SIZE_WITHOUT_INDEX
                = 4009;
              - SHIPMENT_INCONSISTENT_COST_FOR_VEHICLE_SIZE_WITH_INDEX =
                4010;
              - SHIPMENT_INVALID_COST_FOR_VEHICLE = 4011;
              - SHIPMENT_COST_FOR_VEHICLE_INDEX_OUT_OF_BOUNDS = 4012;
              - SHIPMENT_DUPLICATE_COST_FOR_VEHICLE_INDEX = 4013;

            - VEHICLE_ERROR = 42;

              - VEHICLE_EMPTY_REQUIRED_OPERATOR_TYPE = 4200;
              - VEHICLE_DUPLICATE_REQUIRED_OPERATOR_TYPE = 4201;
              - VEHICLE_NO_OPERATOR_WITH_REQUIRED_OPERATOR_TYPE = 4202;
              - VEHICLE_EMPTY_START_TAG = 4203;
              - VEHICLE_DUPLICATE_START_TAG = 4204;
              - VEHICLE_EMPTY_END_TAG = 4205;
              - VEHICLE_DUPLICATE_END_TAG = 4206;
              - VEHICLE_EXTRA_VISIT_DURATION_NEGATIVE_OR_NAN = 4207;
              - VEHICLE_EXTRA_VISIT_DURATION_EXCEEDS_GLOBAL_DURATION =
                4208;
              - VEHICLE_EXTRA_VISIT_DURATION_EMPTY_KEY = 4209;
              - VEHICLE_FIRST_SHIPMENT_INDEX_OUT_OF_BOUNDS = 4210;
              - VEHICLE_FIRST_SHIPMENT_IGNORED = 4211;
              - VEHICLE_FIRST_SHIPMENT_NOT_BOUND = 4212;
              - VEHICLE_LAST_SHIPMENT_INDEX_OUT_OF_BOUNDS = 4213;
              - VEHICLE_LAST_SHIPMENT_IGNORED = 4214;
              - VEHICLE_LAST_SHIPMENT_NOT_BOUND = 4215;
              - VEHICLE_IGNORED_WITH_USED_IF_ROUTE_IS_EMPTY = 4216;
              - VEHICLE_INVALID_COST_PER_KILOMETER = 4217;
              - VEHICLE_INVALID_COST_PER_HOUR = 4218;
              - VEHICLE_INVALID_COST_PER_TRAVELED_HOUR = 4219;
              - VEHICLE_INVALID_FIXED_COST = 4220;
              - VEHICLE_INVALID_TRAVEL_DURATION_MULTIPLE = 4221;
              - VEHICLE_TRAVEL_DURATION_MULTIPLE_WITH_SHIPMENT_PD_DETOUR_LIMITS
                = 4223;
              - VEHICLE_MATRIX_INDEX_WITH_SHIPMENT_PD_DETOUR_LIMITS =
                4224;
              - VEHICLE_MINIMUM_DURATION_LONGER_THAN_DURATION_LIMIT =
                4222;

            - VISIT_REQUEST_ERROR = 44;

              - VISIT_REQUEST_EMPTY_TAG = 4400;
              - VISIT_REQUEST_DUPLICATE_TAG = 4401;
              - VISIT_REQUEST_DURATION_NEGATIVE_OR_NAN = 4404;
              - VISIT_REQUEST_DURATION_EXCEEDS_GLOBAL_DURATION = 4405;

            - PRECEDENCE_ERROR = 46;

              - PRECEDENCE_RULE_MISSING_FIRST_INDEX = 4600;
              - PRECEDENCE_RULE_MISSING_SECOND_INDEX = 4601;
              - PRECEDENCE_RULE_FIRST_INDEX_OUT_OF_BOUNDS = 4602;
              - PRECEDENCE_RULE_SECOND_INDEX_OUT_OF_BOUNDS = 4603;
              - PRECEDENCE_RULE_DUPLICATE_INDEX = 4604;
              - PRECEDENCE_RULE_INEXISTENT_FIRST_VISIT_REQUEST = 4605;
              - PRECEDENCE_RULE_INEXISTENT_SECOND_VISIT_REQUEST = 4606;

            - BREAK_ERROR = 48;

              - BREAK_RULE_EMPTY = 4800;
              - BREAK_REQUEST_UNSPECIFIED_DURATION = 4801;
              - BREAK_REQUEST_UNSPECIFIED_EARLIEST_START_TIME = 4802;
              - BREAK_REQUEST_UNSPECIFIED_LATEST_START_TIME = 4803;
              - BREAK_REQUEST_DURATION_NEGATIVE_OR_NAN = 4804; = 4804;
              - BREAK_REQUEST_LATEST_START_TIME_BEFORE_EARLIEST_START_TIME
                = 4805;
              - BREAK_REQUEST_EARLIEST_START_TIME_BEFORE_GLOBAL_START_TIME
                = 4806;
              - BREAK_REQUEST_LATEST_END_TIME_AFTER_GLOBAL_END_TIME =
                4807;
              - BREAK_REQUEST_NON_SCHEDULABLE = 4808;
              - BREAK_FREQUENCY_MAX_INTER_BREAK_DURATION_NEGATIVE_OR_NAN
                = 4809;
              - BREAK_FREQUENCY_MIN_BREAK_DURATION_NEGATIVE_OR_NAN =
                4810;
              - BREAK_FREQUENCY_MIN_BREAK_DURATION_EXCEEDS_GLOBAL_DURATION
                = 4811;
              - BREAK_FREQUENCY_MAX_INTER_BREAK_DURATION_EXCEEDS_GLOBAL_DURATION
                = 4812;
              - BREAK_REQUEST_DURATION_EXCEEDS_GLOBAL_DURATION = 4813;
              - BREAK_FREQUENCY_MISSING_MAX_INTER_BREAK_DURATION = 4814;
              - BREAK_FREQUENCY_MISSING_MIN_BREAK_DURATION = 4815;

            - SHIPMENT_TYPE_INCOMPATIBILITY_ERROR = 50;

              - SHIPMENT_TYPE_INCOMPATIBILITY_EMPTY_TYPE = 5001;
              - SHIPMENT_TYPE_INCOMPATIBILITY_LESS_THAN_TWO_TYPES =
                5002;
              - SHIPMENT_TYPE_INCOMPATIBILITY_DUPLICATE_TYPE = 5003;
              - SHIPMENT_TYPE_INCOMPATIBILITY_INVALID_INCOMPATIBILITY_MODE
                = 5004;
              - SHIPMENT_TYPE_INCOMPATIBILITY_TOO_MANY_INCOMPATIBILITIES
                = 5005;

            - SHIPMENT_TYPE_REQUIREMENT_ERROR = 52;

              - SHIPMENT_TYPE_REQUIREMENT_NO_REQUIRED_TYPE = 52001;
              - SHIPMENT_TYPE_REQUIREMENT_NO_DEPENDENT_TYPE = 52002;
              - SHIPMENT_TYPE_REQUIREMENT_INVALID_REQUIREMENT_MODE =
                52003;
              - SHIPMENT_TYPE_REQUIREMENT_TOO_MANY_REQUIREMENTS = 52004;
              - SHIPMENT_TYPE_REQUIREMENT_EMPTY_REQUIRED_TYPE = 52005;
              - SHIPMENT_TYPE_REQUIREMENT_DUPLICATE_REQUIRED_TYPE =
                52006;
              - SHIPMENT_TYPE_REQUIREMENT_NO_REQUIRED_TYPE_FOUND =
                52007;
              - SHIPMENT_TYPE_REQUIREMENT_EMPTY_DEPENDENT_TYPE = 52008;
              - SHIPMENT_TYPE_REQUIREMENT_DUPLICATE_DEPENDENT_TYPE =
                52009;
              - SHIPMENT_TYPE_REQUIREMENT_SELF_DEPENDENT_TYPE = 52010;
              - SHIPMENT_TYPE_REQUIREMENT_GRAPH_HAS_CYCLES = 52011;

            - VEHICLE_OPERATOR_ERROR = 54;

              - VEHICLE_OPERATOR_EMPTY_TYPE = 5400;
              - VEHICLE_OPERATOR_MULTIPLE_START_TIME_WINDOWS = 5401;
              - VEHICLE_OPERATOR_SOFT_START_TIME_WINDOW = 5402;
              - VEHICLE_OPERATOR_MULTIPLE_END_TIME_WINDOWS = 5403;
              - VEHICLE_OPERATOR_SOFT_END_TIME_WINDOW = 5404;

            - DURATION_SECONDS_MATRIX_ERROR = 56;

              - DURATION_SECONDS_MATRIX_DURATION_NEGATIVE_OR_NAN = 5600;
              - DURATION_SECONDS_MATRIX_DURATION_EXCEEDS_GLOBAL_DURATION
                = 5601;
        display_name (str):
            The error display name.
        fields (MutableSequence[google.cloud.optimization_v1.types.OptimizeToursValidationError.FieldReference]):
            An error context may involve 0, 1 (most of the time) or more
            fields. For example, referring to vehicle #4 and shipment
            #2's first pickup can be done as follows:

            ::

               fields { name: "vehicles" index: 4}
               fields { name: "shipments" index: 2 sub_field {name: "pickups" index: 0} }

            Note, however, that the cardinality of ``fields`` should not
            change for a given error code.
        error_message (str):
            Human-readable string describing the error. There is a 1:1
            mapping between ``code`` and ``error_message`` (when code !=
            "UNSPECIFIED").

            *STABILITY*: Not stable: the error message associated to a
            given ``code`` may change (hopefully to clarify it) over
            time. Please rely on the ``display_name`` and ``code``
            instead.
        offending_values (str):
            May contain the value(s) of the field(s).
            This is not always available. You should
            absolutely not rely on it and use it only for
            manual model debugging.
    """

    class FieldReference(proto.Message):
        r"""Specifies a context for the validation error. A ``FieldReference``
        always refers to a given field in this file and follows the same
        hierarchical structure. For example, we may specify element #2 of
        ``start_time_windows`` of vehicle #5 using:

        ::

           name: "vehicles" index: 5 sub_field { name: "end_time_windows" index: 2 }

        We however omit top-level entities such as ``OptimizeToursRequest``
        or ``ShipmentModel`` to avoid crowding the message.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            name (str):
                Name of the field, e.g., "vehicles".
            index (int):
                Index of the field if repeated.

                This field is a member of `oneof`_ ``index_or_key``.
            key (str):
                Key if the field is a map.

                This field is a member of `oneof`_ ``index_or_key``.
            sub_field (google.cloud.optimization_v1.types.OptimizeToursValidationError.FieldReference):
                Recursively nested sub-field, if needed.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        index: int = proto.Field(
            proto.INT32,
            number=2,
            oneof="index_or_key",
        )
        key: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="index_or_key",
        )
        sub_field: "OptimizeToursValidationError.FieldReference" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="OptimizeToursValidationError.FieldReference",
        )

    code: int = proto.Field(
        proto.INT32,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    fields: MutableSequence[FieldReference] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=FieldReference,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    offending_values: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
