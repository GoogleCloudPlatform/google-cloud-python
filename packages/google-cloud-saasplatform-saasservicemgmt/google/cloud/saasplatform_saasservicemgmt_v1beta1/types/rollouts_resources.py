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

from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import common

__protobuf__ = proto.module(
    package="google.cloud.saasplatform.saasservicemgmt.v1beta1",
    manifest={
        "RolloutAction",
        "Rollout",
        "RolloutKind",
        "ErrorBudget",
        "RolloutStats",
        "RolloutControl",
    },
)


class RolloutAction(proto.Enum):
    r"""RolloutAction indicates the action to be performed on the
    Rollout.

    Values:
        ROLLOUT_ACTION_UNSPECIFIED (0):
            Unspecified action, will be treated as RUN by
            default.
        ROLLOUT_ACTION_RUN (1):
            Run the Rollout until it naturally reaches a
            terminal state. A rollout requested to run will
            progress through all natural Rollout States
            (such as RUNNING -> SUCCEEDED or RUNNING ->
            FAILED). If retriable errors are encountered
            during the rollout, the rollout will paused by
            default and can be resumed by re-requesting this
            RUN action.
        ROLLOUT_ACTION_PAUSE (2):
            Pause the Rollout until it is resumed (i.e.
            RUN is requested).
        ROLLOUT_ACTION_CANCEL (3):
            Cancel the Rollout permanently.
    """

    ROLLOUT_ACTION_UNSPECIFIED = 0
    ROLLOUT_ACTION_RUN = 1
    ROLLOUT_ACTION_PAUSE = 2
    ROLLOUT_ACTION_CANCEL = 3


class Rollout(proto.Message):
    r"""Represents a single rollout execution and its results

    Attributes:
        name (str):
            Identifier. The resource name (full URI of the resource)
            following the standard naming scheme:

            "projects/{project}/locations/{location}/rollout/{rollout_id}".
        release (str):
            Optional. Immutable. Name of the Release that
            gets rolled out to target Units. Required if no
            other type of release is specified.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Output only. The time when the
            rollout started executing. Will be empty if the
            rollout hasn't started yet.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Output only. The time when the
            rollout finished execution (regardless of
            success, failure, or cancellation). Will be
            empty if the rollout hasn't finished yet. Once
            set, the rollout is in terminal state and all
            the results are final.
        state (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout.RolloutState):
            Output only. Current state of the rollout.
        state_message (str):
            Output only. Human readable message
            indicating details about the last state
            transition.
        state_transition_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Output only. The time when the
            rollout transitioned into its current state.
        root_rollout (str):
            Optional. Output only. The root rollout that this rollout is
            stemming from. The resource name (full URI of the resource)
            following the standard naming scheme:

            "projects/{project}/locations/{location}/rollouts/{rollout_id}".
        parent_rollout (str):
            Optional. Output only. The direct parent rollout that this
            rollout is stemming from. The resource name (full URI of the
            resource) following the standard naming scheme:

            "projects/{project}/locations/{location}/rollouts/{rollout_id}".
        rollout_orchestration_strategy (str):
            Optional. The strategy used for executing
            this Rollout. This strategy will override
            whatever strategy is specified in the
            RolloutKind. If not specified on creation, the
            strategy from RolloutKind will be used.

            There are two supported values strategies which
            are used to control
            - "Google.Cloud.Simple.AllAtOnce"
            - "Google.Cloud.Simple.OneLocationAtATime"

            A rollout with one of these simple strategies
            will rollout across all locations defined in the
            targeted UnitKind's Saas Locations.
        unit_filter (str):
            Optional. CEL(https://github.com/google/cel-spec) formatted
            filter string against Unit. The filter will be applied to
            determine the eligible unit population. This filter can only
            reduce, but not expand the scope of the rollout. If not
            provided, the unit_filter from the RolloutKind will be used.
        rollout_kind (str):
            Required. Immutable. Name of the RolloutKind
            this rollout is stemming from and adhering to.
        stats (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutStats):
            Optional. Output only. Details about the
            progress of the rollout.
        control (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutControl):
            Optional. Requested change to the execution of this rollout.
            Default RolloutControl.action is ROLLOUT_ACTION_RUN meaning
            the rollout will be executed to completion while progressing
            through all natural Rollout States (such as RUNNING ->
            SUCCEEDED or RUNNING -> FAILED). Requests can only be made
            when the Rollout is in a non-terminal state.
        effective_unit_filter (str):
            Optional. Output only. Output only snapshot of the effective
            unit filter at Rollout start time. Contains a
            CEL(https://github.com/google/cel-spec) expression
            consisting of a conjunction of Rollout.unit_filter and
            RolloutKind.unit_filter. This field captures the filter
            applied by the Rollout to determine the Unit population. If
            the associated RolloutKind's unit_filter is modified after
            the rollout is started, it will not be updated here.
        labels (MutableMapping[str, str]):
            Optional. The labels on the resource, which
            can be used for categorization. similar to
            Kubernetes resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Annotations is an unstructured
            key-value map stored with a resource that may be
            set by external tools to store and retrieve
            arbitrary metadata. They are not queryable and
            should be preserved when modifying objects.

            More info:
            https://kubernetes.io/docs/user-guide/annotations
        uid (str):
            Output only. The unique identifier of the
            resource. UID is unique in the time and space
            for this resource within the scope of the
            service. It is typically generated by the server
            on successful creation of a resource and must
            not be changed. UID is used to uniquely identify
            resources with resource name reuses. This should
            be a UUID4.
        etag (str):
            Output only. An opaque value that uniquely
            identifies a version or generation of a
            resource. It can be used to confirm that the
            client and server agree on the ordering of a
            resource being written.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was last updated. Any change to the resource
            made by users must refresh this value. Changes
            to a resource made by the service should refresh
            this value.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was marked for deletion (deletion is an
            asynchronous operation).
    """

    class RolloutState(proto.Enum):
        r"""The current state of the rollout.

        Values:
            ROLLOUT_STATE_UNSPECIFIED (0):
                Unspecified state.
            ROLLOUT_STATE_RUNNING (1):
                Rollout is in progress.
            ROLLOUT_STATE_PAUSED (2):
                Rollout has been paused.
            ROLLOUT_STATE_SUCCEEDED (3):
                Rollout completed successfully.
            ROLLOUT_STATE_FAILED (4):
                Rollout has failed.
            ROLLOUT_STATE_CANCELLED (5):
                Rollout has been canceled.
            ROLLOUT_STATE_WAITING (6):
                Rollout is waiting for some condition to be
                met before starting.
            ROLLOUT_STATE_CANCELLING (7):
                Rollout is being canceled.
            ROLLOUT_STATE_RESUMING (8):
                Rollout is being resumed.
            ROLLOUT_STATE_PAUSING (9):
                Rollout is being paused.
        """

        ROLLOUT_STATE_UNSPECIFIED = 0
        ROLLOUT_STATE_RUNNING = 1
        ROLLOUT_STATE_PAUSED = 2
        ROLLOUT_STATE_SUCCEEDED = 3
        ROLLOUT_STATE_FAILED = 4
        ROLLOUT_STATE_CANCELLED = 5
        ROLLOUT_STATE_WAITING = 6
        ROLLOUT_STATE_CANCELLING = 7
        ROLLOUT_STATE_RESUMING = 8
        ROLLOUT_STATE_PAUSING = 9

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    state: RolloutState = proto.Field(
        proto.ENUM,
        number=10,
        enum=RolloutState,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=11,
    )
    state_transition_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    root_rollout: str = proto.Field(
        proto.STRING,
        number=16,
    )
    parent_rollout: str = proto.Field(
        proto.STRING,
        number=17,
    )
    rollout_orchestration_strategy: str = proto.Field(
        proto.STRING,
        number=19,
    )
    unit_filter: str = proto.Field(
        proto.STRING,
        number=21,
    )
    rollout_kind: str = proto.Field(
        proto.STRING,
        number=22,
    )
    stats: "RolloutStats" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="RolloutStats",
    )
    control: "RolloutControl" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="RolloutControl",
    )
    effective_unit_filter: str = proto.Field(
        proto.STRING,
        number=26,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10401,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10402,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10201,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10303,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10304,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10305,
        message=timestamp_pb2.Timestamp,
    )


class RolloutKind(proto.Message):
    r"""An object that describes various settings of Rollout
    execution. Includes built-in policies across GCP and GDC, and
    customizable policies.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name (full URI of the resource)
            following the standard naming scheme:

            "projects/{project}/locations/{location}/rolloutKinds/{rollout_kind_id}".
        unit_kind (str):
            Required. Immutable. UnitKind that this
            rollout kind corresponds to. Rollouts stemming
            from this rollout kind will target the units of
            this unit kind. In other words, this defines the
            population of target units to be upgraded by
            rollouts.
        rollout_orchestration_strategy (str):
            Optional. The strategy used for executing a
            Rollout. This is a required field.

            There are two supported values strategies which
            are used to control
            - "Google.Cloud.Simple.AllAtOnce"
            - "Google.Cloud.Simple.OneLocationAtATime"

            A rollout with one of these simple strategies
            will rollout across all locations defined in the
            associated UnitKind's Saas Locations.
        unit_filter (str):
            Optional.
            CEL(https://github.com/google/cel-spec)
            formatted filter string against Unit. The filter
            will be applied to determine the eligible unit
            population. This filter can only reduce, but not
            expand the scope of the rollout.
        update_unit_kind_strategy (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind.UpdateUnitKindStrategy):
            Optional. The config for updating the unit
            kind. By default, the unit kind will be updated
            on the rollout start.
        error_budget (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ErrorBudget):
            Optional. The configuration for error budget. If the number
            of failed units exceeds max(allowed_count, allowed_ratio \*
            total_units), the rollout will be paused. If not set, all
            units will be attempted to be updated regardless of the
            number of failures encountered.

            This field is a member of `oneof`_ ``_error_budget``.
        labels (MutableMapping[str, str]):
            Optional. The labels on the resource, which
            can be used for categorization. similar to
            Kubernetes resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Annotations is an unstructured
            key-value map stored with a resource that may be
            set by external tools to store and retrieve
            arbitrary metadata. They are not queryable and
            should be preserved when modifying objects.

            More info:
            https://kubernetes.io/docs/user-guide/annotations
        uid (str):
            Output only. The unique identifier of the
            resource. UID is unique in the time and space
            for this resource within the scope of the
            service. It is typically generated by the server
            on successful creation of a resource and must
            not be changed. UID is used to uniquely identify
            resources with resource name reuses. This should
            be a UUID4.
        etag (str):
            Output only. An opaque value that uniquely
            identifies a version or generation of a
            resource. It can be used to confirm that the
            client and server agree on the ordering of a
            resource being written.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was last updated. Any change to the resource
            made by users must refresh this value. Changes
            to a resource made by the service should refresh
            this value.
    """

    class UpdateUnitKindStrategy(proto.Enum):
        r"""

        Values:
            UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED (0):
                Strategy unspecified.
            UPDATE_UNIT_KIND_STRATEGY_ON_START (1):
                Update the unit kind strategy on the rollout
                start.
            UPDATE_UNIT_KIND_STRATEGY_NEVER (2):
                Never update the unit kind.
        """

        UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED = 0
        UPDATE_UNIT_KIND_STRATEGY_ON_START = 1
        UPDATE_UNIT_KIND_STRATEGY_NEVER = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    unit_kind: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rollout_orchestration_strategy: str = proto.Field(
        proto.STRING,
        number=3,
    )
    unit_filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    update_unit_kind_strategy: UpdateUnitKindStrategy = proto.Field(
        proto.ENUM,
        number=6,
        enum=UpdateUnitKindStrategy,
    )
    error_budget: "ErrorBudget" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="ErrorBudget",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10401,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10402,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10201,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10303,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10304,
        message=timestamp_pb2.Timestamp,
    )


class ErrorBudget(proto.Message):
    r"""The configuration for error budget. If the number of failed units
    exceeds max(allowed_count, allowed_ratio \* total_units), the
    rollout will be paused.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        allowed_count (int):
            Optional. The maximum number of failed units
            allowed in a location without pausing the
            rollout.

            This field is a member of `oneof`_ ``_allowed_count``.
        allowed_percentage (int):
            Optional. The maximum percentage of units allowed to fail
            (0, 100] within a location without pausing the rollout.

            This field is a member of `oneof`_ ``_allowed_percentage``.
    """

    allowed_count: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    allowed_percentage: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class RolloutStats(proto.Message):
    r"""RolloutStats contains information about the progress of a
    rollout.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        operations_by_state (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Aggregate]):
            Optional. Output only. Unordered list. A
            breakdown of the progress of operations
            triggered by the rollout. Provides a count of
            Operations by their state. This can be used to
            determine the number of units which have been
            updated, or are scheduled to be updated.

            There will be at most one entry per group.
            Possible values for operation groups are:

            - "SCHEDULED"
            - "PENDING"
            - "RUNNING"
            - "SUCCEEDED"
            - "FAILED"
            - "CANCELLED".
        estimated_total_unit_count (int):
            Optional. Output only. Estimated number of
            units based. The estimation is computed upon
            creation of the rollout.

            This field is a member of `oneof`_ ``_estimated_total_unit_count``.
    """

    operations_by_state: MutableSequence[common.Aggregate] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=common.Aggregate,
    )
    estimated_total_unit_count: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class RolloutControl(proto.Message):
    r"""RolloutControl provides a way to request a change to the
    execution of a Rollout by pausing or canceling it.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        run_params (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutControl.RunRolloutActionParams):
            Optional. Parameters for the RUN action. It
            is an error to specify this if the RolloutAction
            is not set to RUN. By default, the rollout will
            retry failed operations when resumed.

            This field is a member of `oneof`_ ``action_params``.
        action (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutAction):
            Required. Action to be performed on the
            Rollout. The default behavior is to run the
            rollout until it naturally reaches a terminal
            state.
    """

    class RunRolloutActionParams(proto.Message):
        r"""Parameters for the RUN action controlling the behavior of the
        rollout when it is resumed from a PAUSED state.

        Attributes:
            retry_failed_operations (bool):
                Required. If true, the rollout will retry
                failed operations when resumed. This is
                applicable only the current state of the Rollout
                is PAUSED and the requested action is RUN.
        """

        retry_failed_operations: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    run_params: RunRolloutActionParams = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action_params",
        message=RunRolloutActionParams,
    )
    action: "RolloutAction" = proto.Field(
        proto.ENUM,
        number=1,
        enum="RolloutAction",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
