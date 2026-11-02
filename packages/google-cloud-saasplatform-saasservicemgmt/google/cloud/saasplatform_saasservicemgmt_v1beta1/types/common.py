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
    package="google.cloud.saasplatform.saasservicemgmt.v1beta1",
    manifest={
        "UnitOperationErrorCategory",
        "Blueprint",
        "UnitVariable",
        "UnitCondition",
        "UnitOperationCondition",
        "SaasCondition",
        "Aggregate",
    },
)


class UnitOperationErrorCategory(proto.Enum):
    r"""UnitOperationErrorCategory describes the error category of
    the unit operation.

    Values:
        UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED (0):
            Unit operation error category is unspecified
        NOT_APPLICABLE (1):
            Unit operation error category is not
            applicable, or it is not an error
        FATAL (2):
            Unit operation error category is fatal
        RETRIABLE (3):
            Unit operation error category is retriable
        IGNORABLE (4):
            Unit operation error category is ignorable
        STANDARD (5):
            Unit operation error category is standard,
            counts towards Rollout error budget
    """

    UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED = 0
    NOT_APPLICABLE = 1
    FATAL = 2
    RETRIABLE = 3
    IGNORABLE = 4
    STANDARD = 5


class Blueprint(proto.Message):
    r"""Blueprints are OCI Images that contain all of the artifacts
    needed to provision a unit. Metadata such as, type of the engine
    used to actuate the blueprint (e.g. terraform, helm etc) and
    version will come from the image manifest. If the hostname is
    omitted, it will be assumed to be the regional path to Artifact
    Registry (eg. us-east1-docker.pkg.dev).

    Attributes:
        package (str):
            Optional. Immutable. URI to a blueprint used
            by the Unit (required unless unitKind or release
            is set).
        engine (str):
            Output only. Type of the engine used to
            actuate the blueprint. e.g. terraform, helm etc.
        version (str):
            Output only. Version metadata if present on
            the blueprint.
    """

    package: str = proto.Field(
        proto.STRING,
        number=1,
    )
    engine: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UnitVariable(proto.Message):
    r"""UnitVariable describes a parameter for a Unit.

    Attributes:
        variable (str):
            Required. Immutable. Name of the variable
            from actuation configs.
        type_ (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitVariable.Type):
            Optional. Immutable. Name of a supported
            variable type. Supported types are string, int,
            bool.
        value (str):
            Optional. String encoded value for the
            variable.
    """

    class Type(proto.Enum):
        r"""Enumeration of variable types. ``STRUCT`` and ``LIST`` values should
        be JSON-encoded strings.

        Values:
            TYPE_UNSPECIFIED (0):
                Variable type is unspecified.
            STRING (1):
                Variable type is string.
            INT (2):
                Variable type is int.
            BOOL (3):
                Variable type is bool.
            STRUCT (4):
                Variable type is struct.
            LIST (5):
                Variable type is list.
        """

        TYPE_UNSPECIFIED = 0
        STRING = 1
        INT = 2
        BOOL = 3
        STRUCT = 4
        LIST = 5

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    value: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UnitCondition(proto.Message):
    r"""UnitCondition describes the status of an Unit. UnitCondition
    is individual components that contribute to an overall state.

    Attributes:
        status (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitCondition.Status):
            Required. Status of the condition.
        type_ (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitCondition.Type):
            Required. Type of the condition.
        last_transition_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Last time the condition transited
            from one status to another.
        message (str):
            Required. Human readable message indicating
            details about the last transition.
        reason (str):
            Required. Brief reason for the condition's
            last transition.
    """

    class Status(proto.Enum):
        r"""Enumeration of condition statuses.

        Values:
            STATUS_UNSPECIFIED (0):
                Condition status is unspecified.
            STATUS_UNKNOWN (1):
                Condition is unknown.
            STATUS_TRUE (2):
                Condition is true.
            STATUS_FALSE (3):
                Condition is false.
        """

        STATUS_UNSPECIFIED = 0
        STATUS_UNKNOWN = 1
        STATUS_TRUE = 2
        STATUS_FALSE = 3

    class Type(proto.Enum):
        r"""Enumeration of condition types.

        Values:
            TYPE_UNSPECIFIED (0):
                Condition type is unspecified.
            TYPE_READY (1):
                Condition type is ready.
            TYPE_UPDATING (2):
                Condition type is updating.
            TYPE_PROVISIONED (3):
                Condition type is provisioned.
            TYPE_OPERATION_ERROR (4):
                Condition type is operationError.
                True when the last unit operation fails with a
                non-ignorable error.
            TYPE_APP_CREATED_OR_ALREADY_EXISTS (6):
                Indicates if AppHub app has been created or
                if Apphub app has already existed.
            TYPE_APP_COMPONENTS_REGISTERED (7):
                Indicates if services and workloads have been
                registered with AppHub.
        """

        TYPE_UNSPECIFIED = 0
        TYPE_READY = 1
        TYPE_UPDATING = 2
        TYPE_PROVISIONED = 3
        TYPE_OPERATION_ERROR = 4
        TYPE_APP_CREATED_OR_ALREADY_EXISTS = 6
        TYPE_APP_COMPONENTS_REGISTERED = 7

    status: Status = proto.Field(
        proto.ENUM,
        number=1,
        enum=Status,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    last_transition_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=5,
    )


class UnitOperationCondition(proto.Message):
    r"""UnitOperationCondition describes the status of an Unit
    Operation. UnitOperationCondition is individual components that
    contribute to an overall state.

    Attributes:
        status (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperationCondition.Status):
            Required. Status of the condition.
        type_ (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperationCondition.Type):
            Required. Type of the condition.
        last_transition_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Last time the condition transited
            from one status to another.
        message (str):
            Required. Human readable message indicating
            details about the last transition.
        reason (str):
            Required. Brief reason for the condition's
            last transition.
    """

    class Status(proto.Enum):
        r"""Enumeration of condition statuses.

        Values:
            STATUS_UNSPECIFIED (0):
                Condition status is unspecified.
            STATUS_UNKNOWN (1):
                Condition is unknown.
            STATUS_TRUE (2):
                Condition is true.
            STATUS_FALSE (3):
                Condition is false.
        """

        STATUS_UNSPECIFIED = 0
        STATUS_UNKNOWN = 1
        STATUS_TRUE = 2
        STATUS_FALSE = 3

    class Type(proto.Enum):
        r"""Enumeration of condition types.

        Values:
            TYPE_UNSPECIFIED (0):
                Condition type is unspecified.
            TYPE_SCHEDULED (2):
                Condition type is scheduled.
            TYPE_RUNNING (3):
                Condition type is running.
            TYPE_SUCCEEDED (4):
                Condition type is succeeded.
            TYPE_CANCELLED (5):
                Condition type is cancelled.
            TYPE_APP_CREATED (6):
                Indicates if AppHub app has been created.
            TYPE_APP_COMPONENTS_REGISTERED (7):
                Indicates if services and workloads have been
                registered with AppHub.
            TYPE_WORKLOAD_SUCCEEDED (8):
                Indicates if the UnitOperation's core
                workload execution completed successfully.
                The workload is the core execution operation
                performed for a UnitOperation (e.g.,
                provisioning, updating, or deprovisioning
                resources) excluding post-operation checks.
        """

        TYPE_UNSPECIFIED = 0
        TYPE_SCHEDULED = 2
        TYPE_RUNNING = 3
        TYPE_SUCCEEDED = 4
        TYPE_CANCELLED = 5
        TYPE_APP_CREATED = 6
        TYPE_APP_COMPONENTS_REGISTERED = 7
        TYPE_WORKLOAD_SUCCEEDED = 8

    status: Status = proto.Field(
        proto.ENUM,
        number=1,
        enum=Status,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    last_transition_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SaasCondition(proto.Message):
    r"""SaasCondition describes the status of a Saas.

    Attributes:
        status (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.SaasCondition.Status):
            Required. Status of the condition.
        type_ (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.SaasCondition.Type):
            Required. Type of the condition.
        last_transition_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Last time the condition transited
            from one status to another.
        message (str):
            Required. Human readable message indicating
            details about the last transition.
        reason (str):
            Required. Brief reason for the condition's
            last transition.
    """

    class Status(proto.Enum):
        r"""Enumeration of condition statuses.

        Values:
            STATUS_UNSPECIFIED (0):
                Condition status is unspecified.
            STATUS_UNKNOWN (1):
                Condition is unknown.
            STATUS_TRUE (2):
                Condition is true.
            STATUS_FALSE (3):
                Condition is false.
        """

        STATUS_UNSPECIFIED = 0
        STATUS_UNKNOWN = 1
        STATUS_TRUE = 2
        STATUS_FALSE = 3

    class Type(proto.Enum):
        r"""Enumeration of condition types.

        Values:
            TYPE_UNSPECIFIED (0):
                Condition type is unspecified.
            TYPE_READY (1):
                Condition type is ready.
            TYPE_SYNCHRONIZED (2):
                Condition type is synchronized.
        """

        TYPE_UNSPECIFIED = 0
        TYPE_READY = 1
        TYPE_SYNCHRONIZED = 2

    status: Status = proto.Field(
        proto.ENUM,
        number=1,
        enum=Status,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    last_transition_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Aggregate(proto.Message):
    r"""Represents the aggregation of a set of population of like
    records by a certain group. For example, a collection of unit
    counts can be aggregated and grouped by their state.

    Attributes:
        group (str):
            Required. Group by which to aggregate.
        count (int):
            Required. Number of records in the group.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    count: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
