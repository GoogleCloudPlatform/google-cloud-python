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

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "Condition",
    },
)


class Condition(proto.Message):
    r"""Defines a status condition for a resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (str):
            type is used to communicate the status of the reconciliation
            process. See also:
            https://github.com/knative/serving/blob/main/docs/spec/errors.md#error-conditions-and-reporting
            Types common to all resources include:

            - "Ready": True when the Resource is ready.
        state (google.cloud.run_v2.types.Condition.State):
            State of the condition.
        message (str):
            Human readable message indicating details
            about the current status.
        last_transition_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the condition transitioned from one
            status to another.
        severity (google.cloud.run_v2.types.Condition.Severity):
            How to interpret failures of this condition,
            one of Error, Warning, Info
        reason (google.cloud.run_v2.types.Condition.CommonReason):
            Output only. A common (service-level) reason
            for this condition.

            This field is a member of `oneof`_ ``reasons``.
        revision_reason (google.cloud.run_v2.types.Condition.RevisionReason):
            Output only. A reason for the revision
            condition.

            This field is a member of `oneof`_ ``reasons``.
        execution_reason (google.cloud.run_v2.types.Condition.ExecutionReason):
            Output only. A reason for the execution
            condition.

            This field is a member of `oneof`_ ``reasons``.
    """

    class State(proto.Enum):
        r"""Represents the possible Condition states.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            CONDITION_PENDING (1):
                Transient state: Reconciliation has not
                started yet.
            CONDITION_RECONCILING (2):
                Transient state: reconciliation is still in
                progress.
            CONDITION_FAILED (3):
                Terminal state: Reconciliation did not
                succeed.
            CONDITION_SUCCEEDED (4):
                Terminal state: Reconciliation completed
                successfully.
        """

        STATE_UNSPECIFIED = 0
        CONDITION_PENDING = 1
        CONDITION_RECONCILING = 2
        CONDITION_FAILED = 3
        CONDITION_SUCCEEDED = 4

    class Severity(proto.Enum):
        r"""Represents the severity of the condition failures.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Unspecified severity
            ERROR (1):
                Error severity.
            WARNING (2):
                Warning severity.
            INFO (3):
                Info severity.
        """

        SEVERITY_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2
        INFO = 3

    class CommonReason(proto.Enum):
        r"""Reasons common to all types of conditions.

        Values:
            COMMON_REASON_UNDEFINED (0):
                Default value.
            UNKNOWN (1):
                Reason unknown. Further details will be in
                message.
            REVISION_FAILED (3):
                Revision creation process failed.
            PROGRESS_DEADLINE_EXCEEDED (4):
                Timed out waiting for completion.
            CONTAINER_MISSING (6):
                The container image path is incorrect.
            CONTAINER_PERMISSION_DENIED (7):
                Insufficient permissions on the container
                image.
            CONTAINER_IMAGE_UNAUTHORIZED (8):
                Container image is not authorized by policy.
            CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED (9):
                Container image policy authorization check
                failed.
            ENCRYPTION_KEY_PERMISSION_DENIED (10):
                Insufficient permissions on encryption key.
            ENCRYPTION_KEY_CHECK_FAILED (11):
                Permission check on encryption key failed.
            SECRETS_ACCESS_CHECK_FAILED (12):
                At least one Access check on secrets failed.
            WAITING_FOR_OPERATION (13):
                Waiting for operation to complete.
            IMMEDIATE_RETRY (14):
                System will retry immediately.
            POSTPONED_RETRY (15):
                System will retry later; current attempt
                failed.
            INTERNAL (16):
                An internal error occurred. Further
                information may be in the message.
            VPC_NETWORK_NOT_FOUND (17):
                User-provided VPC network was not found.
        """

        COMMON_REASON_UNDEFINED = 0
        UNKNOWN = 1
        REVISION_FAILED = 3
        PROGRESS_DEADLINE_EXCEEDED = 4
        CONTAINER_MISSING = 6
        CONTAINER_PERMISSION_DENIED = 7
        CONTAINER_IMAGE_UNAUTHORIZED = 8
        CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED = 9
        ENCRYPTION_KEY_PERMISSION_DENIED = 10
        ENCRYPTION_KEY_CHECK_FAILED = 11
        SECRETS_ACCESS_CHECK_FAILED = 12
        WAITING_FOR_OPERATION = 13
        IMMEDIATE_RETRY = 14
        POSTPONED_RETRY = 15
        INTERNAL = 16
        VPC_NETWORK_NOT_FOUND = 17

    class RevisionReason(proto.Enum):
        r"""Reasons specific to Revision resource.

        Values:
            REVISION_REASON_UNDEFINED (0):
                Default value.
            PENDING (1):
                Revision in Pending state.
            RESERVE (2):
                Revision is in Reserve state.
            RETIRED (3):
                Revision is Retired.
            RETIRING (4):
                Revision is being retired.
            RECREATING (5):
                Revision is being recreated.
            HEALTH_CHECK_CONTAINER_ERROR (6):
                There was a health check error.
            CUSTOMIZED_PATH_RESPONSE_PENDING (7):
                Health check failed due to user error from
                customized path of the container. System will
                retry.
            MIN_INSTANCES_NOT_PROVISIONED (8):
                A revision with min_instance_count > 0 was created and is
                reserved, but it was not configured to serve traffic, so
                it's not live. This can also happen momentarily during
                traffic migration.
            ACTIVE_REVISION_LIMIT_REACHED (9):
                The maximum allowed number of active
                revisions has been reached.
            NO_DEPLOYMENT (10):
                There was no deployment defined.
                This value is no longer used, but Services
                created in older versions of the API might
                contain this value.
            HEALTH_CHECK_SKIPPED (11):
                A revision's container has no port specified
                since the revision is of a manually scaled
                service with 0 instance count
            MIN_INSTANCES_WARMING (12):
                A revision with min_instance_count > 0 was created and is
                waiting for enough instances to begin a traffic migration.
        """

        REVISION_REASON_UNDEFINED = 0
        PENDING = 1
        RESERVE = 2
        RETIRED = 3
        RETIRING = 4
        RECREATING = 5
        HEALTH_CHECK_CONTAINER_ERROR = 6
        CUSTOMIZED_PATH_RESPONSE_PENDING = 7
        MIN_INSTANCES_NOT_PROVISIONED = 8
        ACTIVE_REVISION_LIMIT_REACHED = 9
        NO_DEPLOYMENT = 10
        HEALTH_CHECK_SKIPPED = 11
        MIN_INSTANCES_WARMING = 12

    class ExecutionReason(proto.Enum):
        r"""Reasons specific to Execution resource.

        Values:
            EXECUTION_REASON_UNDEFINED (0):
                Default value.
            JOB_STATUS_SERVICE_POLLING_ERROR (1):
                Internal system error getting execution
                status. System will retry.
            NON_ZERO_EXIT_CODE (2):
                A task reached its retry limit and the last
                attempt failed due to the user container exiting
                with a non-zero exit code.
            CANCELLED (3):
                The execution was cancelled by users.
            CANCELLING (4):
                The execution is in the process of being
                cancelled.
            DELETED (5):
                The execution was deleted.
            DELAYED_START_PENDING (6):
                A delayed execution is waiting for a start
                time.
        """

        EXECUTION_REASON_UNDEFINED = 0
        JOB_STATUS_SERVICE_POLLING_ERROR = 1
        NON_ZERO_EXIT_CODE = 2
        CANCELLED = 3
        CANCELLING = 4
        DELETED = 5
        DELAYED_START_PENDING = 6

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    last_transition_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=5,
        enum=Severity,
    )
    reason: CommonReason = proto.Field(
        proto.ENUM,
        number=6,
        oneof="reasons",
        enum=CommonReason,
    )
    revision_reason: RevisionReason = proto.Field(
        proto.ENUM,
        number=9,
        oneof="reasons",
        enum=RevisionReason,
    )
    execution_reason: ExecutionReason = proto.Field(
        proto.ENUM,
        number=11,
        oneof="reasons",
        enum=ExecutionReason,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
