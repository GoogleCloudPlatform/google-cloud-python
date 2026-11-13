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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1beta",
    manifest={
        "RestoreVerificationPlan",
        "RestoreVerificationCleanupRule",
        "CreateRestoreVerificationPlanRequest",
        "GetRestoreVerificationPlanRequest",
        "ListRestoreVerificationPlansRequest",
        "ListRestoreVerificationPlansResponse",
        "DeleteRestoreVerificationPlanRequest",
    },
)


class RestoreVerificationPlan(proto.Message):
    r"""A ``RestoreVerificationPlan`` specifies the scheduling and clean-up
    template for automated restore verification. It contains a
    ``schedule`` to dictate when the verifications should run, and a
    ``RestoreVerificationCleanupRule`` for post-verification resource
    deletion.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            ``RestoreVerificationPlan``.

            Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restoreVerificationPlan}``
        description (str):
            Optional. The description of the ``RestoreVerificationPlan``
            resource.

            The description allows for additional details about
            ``RestoreVerificationPlan`` and its use cases to be
            provided. An example description is the following: "This is
            a restore verification plan that performs a daily
            verification and cleans up the resources immediately after."
            The description must be at most 2048 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the ``RestoreVerificationPlan`` was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the ``RestoreVerificationPlan`` was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
        state (google.cloud.backupdr_v1beta.types.RestoreVerificationPlan.State):
            Output only. The ``State`` for the
            ``RestoreVerificationPlan``.
        schedule (str):
            Required. Describes the schedule on which the restore
            verification will be executed.

            The schedule is specified as a
            `Crontab <https://en.wikipedia.org/wiki/Cron#Overview>`__
            string.
        time_zone (str):
            Optional. Specifies the time zone to be used in interpreting
            [schedule][google.cloud.backupdr.v1beta.RestoreVerificationPlan.schedule].
            The value of this field must be a time zone name from the
            `tz database <https://en.wikipedia.org/wiki/Tz_database>`__,
            like "America/New_York" or "UTC". Defaults to ``UTC`` if not
            specified.
        success_cleanup_rule (google.cloud.backupdr_v1beta.types.RestoreVerificationCleanupRule):
            Optional. The cleanup rule to apply if the
            restore verification succeeds.
        failure_cleanup_rule (google.cloud.backupdr_v1beta.types.RestoreVerificationCleanupRule):
            Optional. The cleanup rule to apply if the
            restore verification fails.
    """

    class State(proto.Enum):
        r"""``State`` enumerates the possible states for a
        ``RestoreVerificationPlan``.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The resource is being created.
            ACTIVE (2):
                The resource has been created and is fully
                usable.
            DELETING (3):
                The resource is being deleted.
            INACTIVE (4):
                The resource has been created but is not
                usable.
            UPDATING (5):
                The resource is being updated.
            ERROR (6):
                The resource is in an error state due to a
                configuration issue.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        INACTIVE = 4
        UPDATING = 5
        ERROR = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=7,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=8,
    )
    success_cleanup_rule: "RestoreVerificationCleanupRule" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="RestoreVerificationCleanupRule",
    )
    failure_cleanup_rule: "RestoreVerificationCleanupRule" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RestoreVerificationCleanupRule",
    )


class RestoreVerificationCleanupRule(proto.Message):
    r"""Defines the specific cleanup action.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cleanup_delay (google.protobuf.duration_pb2.Duration):
            Optional. Duration after restore finishes
            when cleanup triggers. Delay must be
            non-negative and at most 30 days (2592000
            seconds).
        skip_cleanup (bool):
            Optional. If set to true, the restored
            resource will not be cleaned up.

            This field is a member of `oneof`_ ``_skip_cleanup``.
    """

    cleanup_delay: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    skip_cleanup: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class CreateRestoreVerificationPlanRequest(proto.Message):
    r"""The request message for creating a ``RestoreVerificationPlan``.

    Attributes:
        parent (str):
            Required. The ``RestoreVerificationPlan`` project and
            location in the format
            ``projects/{project}/locations/{location}``. In Google Cloud
            Backup and DR locations map to Google Cloud regions, for
            example **us-central1**.
        restore_verification_plan_id (str):
            Required. The name of the ``RestoreVerificationPlan`` to
            create. The name must be unique for the specified project
            and location. The name must start with a lowercase letter
            followed by up to 62 lowercase letters, numbers, or hyphens.
            Pattern, ``^[a-z]([-a-z0-9]*[a-z0-9])?$``.
        restore_verification_plan (google.cloud.backupdr_v1beta.types.RestoreVerificationPlan):
            Required. The ``RestoreVerificationPlan`` resource object to
            create.
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
    restore_verification_plan_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    restore_verification_plan: "RestoreVerificationPlan" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RestoreVerificationPlan",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetRestoreVerificationPlanRequest(proto.Message):
    r"""The request message for getting a ``RestoreVerificationPlan``.

    Attributes:
        name (str):
            Required. The resource name of the
            ``RestoreVerificationPlan`` to retrieve.

            Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restoreVerificationPlan}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRestoreVerificationPlansRequest(proto.Message):
    r"""The request message for getting a list of
    ``RestoreVerificationPlans``.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            ``RestoreVerificationPlans`` information. Format:
            ``projects/{project}/locations/{location}``. In Google Cloud
            Backup and DR, locations map to Google Cloud regions, for
            example **us-central1**. To retrieve restore verification
            plans for all locations, use "-" for the ``{location}``
            value.
        page_size (int):
            Optional. The maximum number of ``RestoreVerificationPlans``
            to return in a single response. If not specified, a default
            value will be chosen by the service. Note that the response
            may include a partial list and a caller should only rely on
            the response's
            [next_page_token][google.cloud.backupdr.v1beta.ListRestoreVerificationPlansResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.backupdr.v1beta.ListRestoreVerificationPlansResponse.next_page_token]
            received from a previous ``ListRestoreVerificationPlans``
            call. Provide this to retrieve the subsequent page in a
            multi-page list of results. When paginating, all other
            parameters provided to ``ListRestoreVerificationPlans`` must
            match the call that provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListRestoreVerificationPlansResponse(proto.Message):
    r"""The response message for getting a list of
    ``RestoreVerificationPlans``.

    Attributes:
        restore_verification_plans (MutableSequence[google.cloud.backupdr_v1beta.types.RestoreVerificationPlan]):
            The list of ``RestoreVerificationPlans`` in the project for
            the specified location.

            If the ``{location}`` value in the request is "-", the
            response contains a list of resources from all locations. In
            case any location is unreachable, the response will only
            return restore verification plans in reachable locations and
            the 'unreachable' field will be populated with a list of
            unreachable locations.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.backupdr.v1beta.ListRestoreVerificationPlansRequest.page_token]
            in a subsequent ``ListRestoreVerificationPlans`` call to
            retrieve the next page of results. If this field is omitted
            or empty, then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    restore_verification_plans: MutableSequence["RestoreVerificationPlan"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RestoreVerificationPlan",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteRestoreVerificationPlanRequest(proto.Message):
    r"""The request message for deleting a ``RestoreVerificationPlan``.

    Attributes:
        name (str):
            Required. The resource name of the
            ``RestoreVerificationPlan`` to delete.

            Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restoreVerificationPlan}``
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
        force (bool):
            Optional. If set to true, any
            RestoreVerificationPlanAssociations linked to
            this RestoreVerificationPlan will also be
            deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
