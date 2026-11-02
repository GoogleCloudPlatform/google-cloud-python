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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "GoldengateConnectionAssignment",
        "GoldengateConnectionAssignmentProperties",
        "ListGoldengateConnectionAssignmentsRequest",
        "ListGoldengateConnectionAssignmentsResponse",
        "GetGoldengateConnectionAssignmentRequest",
        "CreateGoldengateConnectionAssignmentRequest",
        "TestGoldengateConnectionAssignmentRequest",
        "TestConnectionAssignmentError",
        "TestGoldengateConnectionAssignmentResponse",
        "DeleteGoldengateConnectionAssignmentRequest",
    },
)


class GoldengateConnectionAssignment(proto.Message):
    r"""Represents the metadata of a Goldengate Connection
    Assignment.

    Attributes:
        name (str):
            Identifier. The name of the GoldengateConnectionAssignment
            resource in the following format:
            projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengate_connection_assignment}
        properties (google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignmentProperties):
            Required. The properties of the
            GoldengateConnectionAssignment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the connection
            assignment was created.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the GoldengateConnectionAssignment.
        display_name (str):
            Optional. The display name for the
            GoldengateConnectionAssignment.
        entitlement_id (str):
            Output only. The OCID of the entitlement
            linked to this resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "GoldengateConnectionAssignmentProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GoldengateConnectionAssignmentProperties",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GoldengateConnectionAssignmentProperties(proto.Message):
    r"""The properties of a GoldengateConnectionAssignment.

    Attributes:
        ocid (str):
            Output only. The
            `OCID <https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm>`__
            of the connection assignment being referenced.
        goldengate_connection (str):
            Required. The GoldengateConnection resource to be assigned.
            Format:
            projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}
        goldengate_deployment (str):
            Required. The GoldenGateDeployment to assign the connection
            to. Format:
            projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}
        alias (str):
            Output only. Credential store alias.
        state (google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignmentProperties.State):
            Output only. The lifecycle state of the
            connection assignment.
    """

    class State(proto.Enum):
        r"""Possible lifecycle states for connection assignments.

        Values:
            STATE_UNSPECIFIED (0):
                Lifecycle state is unspecified.
            CREATING (1):
                Connection assignment is being created.
            ACTIVE (2):
                Connection assignment is active.
            FAILED (3):
                Connection assignment failed.
            UPDATING (4):
                Connection assignment is being updated.
            DELETING (5):
                Connection assignment is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        UPDATING = 4
        DELETING = 5

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    goldengate_connection: str = proto.Field(
        proto.STRING,
        number=2,
    )
    goldengate_deployment: str = proto.Field(
        proto.STRING,
        number=3,
    )
    alias: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )


class ListGoldengateConnectionAssignmentsRequest(proto.Message):
    r"""Request message for listing GoldengateConnectionAssignments.

    Attributes:
        parent (str):
            Required. The parent value for the
            GoldengateConnectionAssignments. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of
            GoldengateConnectionAssignments to return. The
            service may return fewer than this value. If
            unspecified, at most 50
            GoldengateConnectionAssignments will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListGoldengateConnectionAssignments`` call. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListGoldengateConnectionAssignments`` must match the call
            that provided the page token.
        filter (str):
            Optional. A filter expression that filters
            GoldengateConnectionAssignments listed in the
            response.
        order_by (str):
            Optional. A comma-separated list of fields to
            order by, sorted in ascending order. Use "DESC"
            after a field name for descending.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListGoldengateConnectionAssignmentsResponse(proto.Message):
    r"""Response message for listing GoldengateConnectionAssignments.

    Attributes:
        goldengate_connection_assignments (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignment]):
            The list of GoldengateConnectionAssignments.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    goldengate_connection_assignments: MutableSequence[
        "GoldengateConnectionAssignment"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GoldengateConnectionAssignment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetGoldengateConnectionAssignmentRequest(proto.Message):
    r"""Request message for getting a GoldengateConnectionAssignment.

    Attributes:
        name (str):
            Required. The name of the GoldengateConnectionAssignment to
            retrieve. Format:
            projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGoldengateConnectionAssignmentRequest(proto.Message):
    r"""Request message for creating a
    GoldengateConnectionAssignment.

    Attributes:
        parent (str):
            Required. The parent resource where this
            GoldengateConnectionAssignment will be created.
            Format: projects/{project}/locations/{location}
        goldengate_connection_assignment_id (str):
            Required. The ID of the
            GoldengateConnectionAssignment to create.
        goldengate_connection_assignment (google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignment):
            Required. The GoldengateConnectionAssignment
            to create.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    goldengate_connection_assignment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    goldengate_connection_assignment: "GoldengateConnectionAssignment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GoldengateConnectionAssignment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class TestGoldengateConnectionAssignmentRequest(proto.Message):
    r"""Request message for TestGoldengateConnectionAssignment.

    Attributes:
        name (str):
            Required. Name of the connection assignment for which to
            test connection.
            projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengate_connection_assignment}
        type_ (google.cloud.oracledatabase_v1.types.TestGoldengateConnectionAssignmentRequest.TestType):
            Optional. The type of the test of the
            assigned connection. The only type actually
            supported is DEFAULT.
    """

    class TestType(proto.Enum):
        r"""The type of test to perform.

        Values:
            TEST_TYPE_UNSPECIFIED (0):
                The default value. This value is unused.
            DEFAULT (1):
                The default connection test.
        """

        TEST_TYPE_UNSPECIFIED = 0
        DEFAULT = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: TestType = proto.Field(
        proto.ENUM,
        number=2,
        enum=TestType,
    )


class TestConnectionAssignmentError(proto.Message):
    r"""Error details for TestGoldengateConnectionAssignment.

    Attributes:
        code (str):
            A short error code that defines the error,
            meant for programmatic parsing.
        message (str):
            A human-readable error message.
        action (str):
            The text describing the action required to
            fix the issue.
        issue (str):
            The text describing the root cause of the
            reported issue.
    """

    code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    action: str = proto.Field(
        proto.STRING,
        number=3,
    )
    issue: str = proto.Field(
        proto.STRING,
        number=4,
    )


class TestGoldengateConnectionAssignmentResponse(proto.Message):
    r"""The result of the connectivity test performed between the
    Goldengate deployment and the associated database / service.

    Attributes:
        result_type (google.cloud.oracledatabase_v1.types.TestGoldengateConnectionAssignmentResponse.ResultType):
            Type of the result i.e. Success, Failure or
            Timeout.
        error (google.cloud.oracledatabase_v1.types.TestConnectionAssignmentError):
            Error details if test connection failed.
        errors (MutableSequence[google.cloud.oracledatabase_v1.types.TestConnectionAssignmentError]):
            List of test connection assignment error
            objects.
    """

    class ResultType(proto.Enum):
        r"""Type of the result.

        Values:
            RESULT_TYPE_UNSPECIFIED (0):
                Result type is unspecified.
            SUCCEEDED (1):
                Test connection succeeded.
            FAILED (2):
                Test connection failed.
            TIMED_OUT (3):
                Test connection timed out.
        """

        RESULT_TYPE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        TIMED_OUT = 3

    result_type: ResultType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ResultType,
    )
    error: "TestConnectionAssignmentError" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TestConnectionAssignmentError",
    )
    errors: MutableSequence["TestConnectionAssignmentError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="TestConnectionAssignmentError",
    )


class DeleteGoldengateConnectionAssignmentRequest(proto.Message):
    r"""Request message for deleting a
    GoldengateConnectionAssignment.

    Attributes:
        name (str):
            Required. The name of the GoldengateConnectionAssignment to
            delete. Format:
            projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
