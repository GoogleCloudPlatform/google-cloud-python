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
import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bigtable_v2.types import data, feature_flags, request_stats

__protobuf__ = proto.module(
    package="google.bigtable.v2",
    manifest={
        "SessionType",
        "LoadBalancingOptions",
        "SessionScopeDiversionConfiguration",
        "SessionDiversionConfiguration",
        "SessionClientConfiguration",
        "TelemetryConfiguration",
        "OpenSessionRequest",
        "BackendIdentifier",
        "OpenSessionResponse",
        "CloseSessionRequest",
        "OpenTableRequest",
        "OpenTableResponse",
        "OpenAuthorizedViewRequest",
        "OpenAuthorizedViewResponse",
        "OpenMaterializedViewRequest",
        "OpenMaterializedViewResponse",
        "VirtualRpcRequest",
        "ContinueVirtualRpcRequest",
        "CancelVirtualRpcRequest",
        "ClusterInformation",
        "SessionRequestStats",
        "VirtualRpcResponse",
        "ErrorResponse",
        "TableRequest",
        "TableResponse",
        "AuthorizedViewRequest",
        "AuthorizedViewResponse",
        "MaterializedViewRequest",
        "MaterializedViewResponse",
        "SessionReadRowRequest",
        "SessionReadRowResponse",
        "SessionReadRowsRequest",
        "SessionReadRowsResponse",
        "SessionMutateRowRequest",
        "SessionMutateRowResponse",
        "SessionCheckAndMutateRowRequest",
        "SessionCheckAndMutateRowResponse",
        "SessionReadModifyWriteRowRequest",
        "SessionReadModifyWriteRowResponse",
        "SessionMutateRowsRequest",
        "SessionMutateRowsResponse",
        "SessionParametersResponse",
        "HeartbeatResponse",
        "GoAwayResponse",
        "SessionRefreshConfig",
    },
)


class SessionType(proto.Enum):
    r"""Supported session types.

    Values:
        SESSION_TYPE_UNSET (0):
            No description available.
        SESSION_TYPE_TABLE (1):
            No description available.
        SESSION_TYPE_AUTHORIZED_VIEW (2):
            No description available.
        SESSION_TYPE_MATERIALIZED_VIEW (3):
            No description available.
        SESSION_TYPE_TEST (9999):
            For internal protocol testing only.
    """

    SESSION_TYPE_UNSET = 0
    SESSION_TYPE_TABLE = 1
    SESSION_TYPE_AUTHORIZED_VIEW = 2
    SESSION_TYPE_MATERIALIZED_VIEW = 3
    SESSION_TYPE_TEST = 9999


class LoadBalancingOptions(proto.Message):
    r"""Configuration for how to balance vRPCs over sessions.
    Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        least_in_flight (google.cloud.bigtable_v2.types.LoadBalancingOptions.LeastInFlight):

            This field is a member of `oneof`_ ``load_balancing_strategy``.
        peak_ewma (google.cloud.bigtable_v2.types.LoadBalancingOptions.PeakEwma):

            This field is a member of `oneof`_ ``load_balancing_strategy``.
        random (google.cloud.bigtable_v2.types.LoadBalancingOptions.Random):

            This field is a member of `oneof`_ ``load_balancing_strategy``.
    """

    class LeastInFlight(proto.Message):
        r"""Balances vRPCs over backends, preferring to send new vRPCs to
        AFEs with the least number of active vRPCs.

        Attributes:
            random_subset_size (int):
                Of all connected AFEs, the size of the random
                subset to run the algorithm on. Zero implies all
                connected AFEs.
        """

        random_subset_size: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class PeakEwma(proto.Message):
        r"""Balances vRPCs over backends, by maintaining a moving average
        of each AFE's round-trip time, weighted by the number of
        outstanding vRPCs, and distribute traffic to AFEs where that
        cost function is smallest.

        See:

        https://linkerd.io/2016/03/16/beyond-round-robin-load-balancing-for-latency

        Attributes:
            random_subset_size (int):
                Of all connected AFEs, the size of the random
                subset to compare costs over. Zero implies all
                connected AFEs.
        """

        random_subset_size: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class Random(proto.Message):
        r"""Balances vRPCs over backends, by randomly selecting a
        backend.

        """

    least_in_flight: LeastInFlight = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="load_balancing_strategy",
        message=LeastInFlight,
    )
    peak_ewma: PeakEwma = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="load_balancing_strategy",
        message=PeakEwma,
    )
    random: Random = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="load_balancing_strategy",
        message=Random,
    )


class SessionScopeDiversionConfiguration(proto.Message):
    r"""Configuration for how a given slice of traffic is diverted to
    sessions. Internal usage only.

    Attributes:
        session_load (float):
            What share of in-scope requests should operate on a session,
            [0, 1]. The remaining requests within this scope should
            operate on the classic API.
    """

    session_load: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class SessionDiversionConfiguration(proto.Message):
    r"""Configuration for how to divert load to sessions. Internal
    usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        global_diversion (google.cloud.bigtable_v2.types.SessionScopeDiversionConfiguration):
            If provided, all scopes should use this
            diversion config.

            This field is a member of `oneof`_ ``diversion_strategy``.
        per_scope_diversion (google.cloud.bigtable_v2.types.SessionDiversionConfiguration.PerScopeDiversion):
            Diversion happens per-scope.

            This field is a member of `oneof`_ ``diversion_strategy``.
    """

    class PerScopeDiversion(proto.Message):
        r"""Configuration for how to balance sessions per method.
        Internal usage only.

        Attributes:
            scope_diversions (MutableMapping[str, google.cloud.bigtable_v2.types.SessionScopeDiversionConfiguration]):
                Keys: Attributes of the request scope that
                can impact the diversion. Valid format is:

                  "method:<service>.<method>" - All requests
                with this scope will have   the specified
                diversion config applied.
        """

        scope_diversions: MutableMapping[str, "SessionScopeDiversionConfiguration"] = (
            proto.MapField(
                proto.STRING,
                proto.MESSAGE,
                number=1,
                message="SessionScopeDiversionConfiguration",
            )
        )

    global_diversion: "SessionScopeDiversionConfiguration" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="diversion_strategy",
        message="SessionScopeDiversionConfiguration",
    )
    per_scope_diversion: PerScopeDiversion = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="diversion_strategy",
        message=PerScopeDiversion,
    )


class SessionClientConfiguration(proto.Message):
    r"""Configuration for the Session API. Internal usage only.

    Attributes:
        session_load (float):
            Deprecated: Prefer session_diversion_configuration. If both
            are provided, the client should apply this session_load to
            Bigtable.ReadRow & Bigtable.MutateRow, then process the
            session_diversion_configuration, overwriting any behavior
            established by this value.

            What share of the following methods should operate on a
            session, [0, 1]:

            - Bigtable.ReadRow
            - Bigtable.MutateRow

            The rest should operate on the classic API, e.g. have
            session_load = 0.
        session_diversion_configuration (google.cloud.bigtable_v2.types.SessionDiversionConfiguration):
            How load should be divered to sessions.
        load_balancing_options (google.cloud.bigtable_v2.types.LoadBalancingOptions):

        channel_configuration (google.cloud.bigtable_v2.types.SessionClientConfiguration.ChannelPoolConfiguration):
            Configuration for the channel pool.
        session_pool_configuration (google.cloud.bigtable_v2.types.SessionClientConfiguration.SessionPoolConfiguration):
            Configuration for the session pools.
    """

    class ChannelPoolConfiguration(proto.Message):
        r"""Configuration for the channel pool.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            min_server_count (int):
                The minimum number of distcint servers to
                connect to in the channel pool. The client will
                ensure that the channel pool will have at least
                this many distinct servers, but may have
                multiple channels connected to the same server
                (e.g. the client may have M channels on N
                machines, where M > N).
            max_server_count (int):
                The maximum number of distinct servers to
                connect to in the channel pool. The client will
                ensure that the channel pool will have at most
                this many distinct servers.
            per_server_session_count (int):
                Soft maximum for how many sessions are allowed per server.
                Normally, the client will ensure that it does not host more
                than this count of sessions per server, unless there are
                other limits encountered (e.g. the connected servers is
                already at max_servers).
            direct_access_with_fallback (google.cloud.bigtable_v2.types.SessionClientConfiguration.ChannelPoolConfiguration.DirectAccessWithFallback):
                DirectAccess with a fallback to CloudPath.

                This field is a member of `oneof`_ ``mode``.
            direct_access_only (google.cloud.bigtable_v2.types.SessionClientConfiguration.ChannelPoolConfiguration.DirectAccessOnly):
                DirectAccess only.

                This field is a member of `oneof`_ ``mode``.
            cloud_path_only (google.cloud.bigtable_v2.types.SessionClientConfiguration.ChannelPoolConfiguration.CloudPathOnly):
                CloudPath only.

                This field is a member of `oneof`_ ``mode``.
        """

        class DirectAccessWithFallback(proto.Message):
            r"""A channel mode which allows DirectAccess with a fallback to
            CloudPath if DirectAccess is unavailable.

            Attributes:
                error_rate_threshold (float):
                    The threshold for errors on DirectAccess to trigger
                    CloudPath fallback. The error rate is calculated based on a
                    count of vRPCs with errors divided by a total count of
                    vRPCs, over a rolling window of the past check_interval. If
                    this ratio exceeds this threshold, the fallback to CloudPath
                    is triggered. [0, 1].
                check_interval (google.protobuf.duration_pb2.Duration):
                    The interval to check the error rate over.
            """

            error_rate_threshold: float = proto.Field(
                proto.FLOAT,
                number=1,
            )
            check_interval: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=2,
                message=duration_pb2.Duration,
            )

        class DirectAccessOnly(proto.Message):
            r"""A channel mode which only allows DirectAccess."""

        class CloudPathOnly(proto.Message):
            r"""A channel mode which only allows CloudPath."""

        min_server_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        max_server_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        per_server_session_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        direct_access_with_fallback: "SessionClientConfiguration.ChannelPoolConfiguration.DirectAccessWithFallback" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="mode",
            message="SessionClientConfiguration.ChannelPoolConfiguration.DirectAccessWithFallback",
        )
        direct_access_only: "SessionClientConfiguration.ChannelPoolConfiguration.DirectAccessOnly" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="mode",
            message="SessionClientConfiguration.ChannelPoolConfiguration.DirectAccessOnly",
        )
        cloud_path_only: "SessionClientConfiguration.ChannelPoolConfiguration.CloudPathOnly" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="mode",
            message="SessionClientConfiguration.ChannelPoolConfiguration.CloudPathOnly",
        )

    class SessionPoolConfiguration(proto.Message):
        r"""Configuration for the session pools. Session pools are tied
        to a scope like a table, an app profile, and a permission.

        Attributes:
            headroom (float):
                Fraction of idle sessions to keep in order to
                manage an increase in requests-in-flight. For
                example, a headroom of 0.5 will keep enough
                sessions to deal with a 50% increase in QPS.
            min_session_count (int):
                The minimum number of sessions for a given
                scope.
            max_session_count (int):
                The maximum number of sessions for a given
                scope.
            new_session_queue_length (int):
                Number of vRPCs that can be queued per
                starting session.
            new_session_creation_budget (int):
                How many concurrent session establishments
                are allowed. The client will hold onto a count
                against this budget whenever it is establishing
                a new session, and release that count once the
                session is successfully established or failed to
                establish.
            new_session_creation_penalty (google.protobuf.duration_pb2.Duration):
                How long to penalize the creation budget for
                a failed session creation attempt.
            soft_session_close_budget (int):
                How many concurrent session closures are
                allowed. The client will hold onto a count
                against this budget whenever it is closing a
                session, and release that count once the session
                is successfully established or failed to
                establish.
            consecutive_session_failure_threshold (int):
                A threshold for cancelling all pending vRPCs
                based on how many consecutive session
                establishment errors have been observed. The
                client will eagerly cancel queued vRPCs after
                this threshold is met to avoid them waiting
                their entire deadlines before terminating (while
                waiting for any session to establish to actually
                send the vRPC).
            load_balancing_options (google.cloud.bigtable_v2.types.LoadBalancingOptions):
                How to balance vRPC load over connections to AFEs.

                Set only if session_load or session_diversion_configuration
                indicates that there will be some session traffic.
        """

        headroom: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        min_session_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        max_session_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        new_session_queue_length: int = proto.Field(
            proto.INT32,
            number=4,
        )
        new_session_creation_budget: int = proto.Field(
            proto.INT32,
            number=5,
        )
        new_session_creation_penalty: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
        soft_session_close_budget: int = proto.Field(
            proto.INT32,
            number=7,
        )
        consecutive_session_failure_threshold: int = proto.Field(
            proto.INT32,
            number=8,
        )
        load_balancing_options: "LoadBalancingOptions" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="LoadBalancingOptions",
        )

    session_load: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    session_diversion_configuration: "SessionDiversionConfiguration" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SessionDiversionConfiguration",
    )
    load_balancing_options: "LoadBalancingOptions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LoadBalancingOptions",
    )
    channel_configuration: ChannelPoolConfiguration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ChannelPoolConfiguration,
    )
    session_pool_configuration: SessionPoolConfiguration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SessionPoolConfiguration,
    )


class TelemetryConfiguration(proto.Message):
    r"""Server provided instructions for enabling finer grained
    observability on the client to help diagnose customer issues.
    Internal usage only.

    Attributes:
        debug_tag_level (google.cloud.bigtable_v2.types.TelemetryConfiguration.Level):
            Selector for the debug counters that should
            be uploaded.
    """

    class Level(proto.Enum):
        r"""The level of detail of telemetry to be sent from the client.

        Values:
            LEVEL_UNSPECIFIED (0):
                Server did not specify a level. Should
                disable all debug tag counters.
            DEBUG (1):
                Enables all debug tag counter levels.
            INFO (2):
                Eables all debug tag counters except for
                DEBUG.
            WARN (3):
                Enables all debug tag counters except for
                DEBUG and INFO.
            ERROR (4):
                Enables only error debug tag counters.
        """

        LEVEL_UNSPECIFIED = 0
        DEBUG = 1
        INFO = 2
        WARN = 3
        ERROR = 4

    debug_tag_level: Level = proto.Field(
        proto.ENUM,
        number=1,
        enum=Level,
    )


class OpenSessionRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        protocol_version (int):
            A version indicator from the client stating
            its understanding of the protocol. This is to
            disambiguate client behavior amidst changes in
            semantic usage of the API, e.g. if the structure
            remains the same but behavior changes.
        flags (google.cloud.bigtable_v2.types.FeatureFlags):
            Client settings, including a record of
        consecutive_failed_connection_attempts (int):
            Used for serverside observability.
        routing_cookie (bytes):
            How the request should be routed (if
            presented as part of a GOAWAY from a previous
            session). Post V1.
        payload (bytes):
            Can be
            Open{Table,AuthorizedView,MaterializedView}Request,
            (or in post-V1, PrepareSqlQueryRequest)
    """

    protocol_version: int = proto.Field(
        proto.INT64,
        number=1,
    )
    flags: feature_flags.FeatureFlags = proto.Field(
        proto.MESSAGE,
        number=2,
        message=feature_flags.FeatureFlags,
    )
    consecutive_failed_connection_attempts: int = proto.Field(
        proto.INT64,
        number=3,
    )
    routing_cookie: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    payload: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class BackendIdentifier(proto.Message):
    r"""Information about the connected backends from a session
    client's perspective. This information may be used to make
    choices about session re-establishment en-masse for sessions
    with the same backend identifiers. Internal usage only.

    Attributes:
        google_frontend_id (int):
            An opaque identifier for the Google Frontend
            which serviced this request. Only set when not
            using DirectAccess.
        application_frontend_id (int):
            An opaque identifier for the application
            frontend which serviced this request.
        application_frontend_zone (str):
            The zone of the application frontend that
            served this request.
    """

    google_frontend_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    application_frontend_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    application_frontend_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OpenSessionResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        backend (google.cloud.bigtable_v2.types.BackendIdentifier):
            Information on the backend(s) that are
            hosting this session.
        payload (bytes):
            Can be
            Open{Table,AuthorizedView,MaterializedView}Response,
            (or in post-V1, PrepareSqlQueryResponse)
    """

    backend: "BackendIdentifier" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackendIdentifier",
    )
    payload: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class CloseSessionRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        reason (google.cloud.bigtable_v2.types.CloseSessionRequest.CloseSessionReason):

        description (str):

    """

    class CloseSessionReason(proto.Enum):
        r"""Client-generated reason for terminating the session,
        including a plain-text description of why.
        'reason' may be used for metrics, while both may be logged
        (server-side).

        Values:
            CLOSE_SESSION_REASON_UNSET (0):
                No description available.
            CLOSE_SESSION_REASON_GOAWAY (1):
                No description available.
            CLOSE_SESSION_REASON_ERROR (2):
                No description available.
            CLOSE_SESSION_REASON_USER (3):
                No description available.
            CLOSE_SESSION_REASON_DOWNSIZE (4):
                No description available.
            CLOSE_SESSION_REASON_MISSED_HEARTBEAT (5):
                No description available.
        """

        CLOSE_SESSION_REASON_UNSET = 0
        CLOSE_SESSION_REASON_GOAWAY = 1
        CLOSE_SESSION_REASON_ERROR = 2
        CLOSE_SESSION_REASON_USER = 3
        CLOSE_SESSION_REASON_DOWNSIZE = 4
        CLOSE_SESSION_REASON_MISSED_HEARTBEAT = 5

    reason: CloseSessionReason = proto.Field(
        proto.ENUM,
        number=1,
        enum=CloseSessionReason,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OpenTableRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        table_name (str):

        app_profile_id (str):

        permission (google.cloud.bigtable_v2.types.OpenTableRequest.Permission):

    """

    class Permission(proto.Enum):
        r"""

        Values:
            PERMISSION_UNSET (0):
                No description available.
            PERMISSION_READ (1):
                No description available.
            PERMISSION_WRITE (2):
                No description available.
            PERMISSION_READ_WRITE (3):
                No description available.
        """

        PERMISSION_UNSET = 0
        PERMISSION_READ = 1
        PERMISSION_WRITE = 2
        PERMISSION_READ_WRITE = 3

    table_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    permission: Permission = proto.Field(
        proto.ENUM,
        number=3,
        enum=Permission,
    )


class OpenTableResponse(proto.Message):
    r"""Internal usage only."""


class OpenAuthorizedViewRequest(proto.Message):
    r"""Open sessions for an AuthorizedView. Internal usage only.

    Attributes:
        authorized_view_name (str):
            The Authorized view name to read and write from. Values are
            of the form
            ``projects/<project>/instances/<instance>/tables/<table>/authorizedViews/<authorized_view>``.
        app_profile_id (str):
            The app profile id to use for the authorized
            view sessions.
        permission (google.cloud.bigtable_v2.types.OpenAuthorizedViewRequest.Permission):
            Permission for the session.
    """

    class Permission(proto.Enum):
        r"""

        Values:
            PERMISSION_UNSET (0):
                No description available.
            PERMISSION_READ (1):
                No description available.
            PERMISSION_WRITE (2):
                No description available.
            PERMISSION_READ_WRITE (3):
                No description available.
        """

        PERMISSION_UNSET = 0
        PERMISSION_READ = 1
        PERMISSION_WRITE = 2
        PERMISSION_READ_WRITE = 3

    authorized_view_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    permission: Permission = proto.Field(
        proto.ENUM,
        number=3,
        enum=Permission,
    )


class OpenAuthorizedViewResponse(proto.Message):
    r"""Internal usage only."""


class OpenMaterializedViewRequest(proto.Message):
    r"""Open sessions for a MaterializedView. Internal usage only.

    Attributes:
        materialized_view_name (str):
            The Materialized view name to read and write from. Values
            are of the form
            ``projects/<project>/instances/<instance>/materializedViews/<materialized_view>``.
        app_profile_id (str):
            The app profile id to use for the
            materialized view sessions.
        permission (google.cloud.bigtable_v2.types.OpenMaterializedViewRequest.Permission):
            Permission for the session.
    """

    class Permission(proto.Enum):
        r"""

        Values:
            PERMISSION_UNSET (0):
                No description available.
            PERMISSION_READ (1):
                No description available.
        """

        PERMISSION_UNSET = 0
        PERMISSION_READ = 1

    materialized_view_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    permission: Permission = proto.Field(
        proto.ENUM,
        number=3,
        enum=Permission,
    )


class OpenMaterializedViewResponse(proto.Message):
    r"""Internal usage only."""


class VirtualRpcRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        rpc_id (int):
            Client chosen, monotonically increasing
            identifier for the request. Must be unique
            within a session.
        deadline (google.protobuf.duration_pb2.Duration):
            Attempt deadline.

            Note, this may not be needed for V1, TBD (e.g.
            operation vs attempt deadline).
        metadata (google.cloud.bigtable_v2.types.VirtualRpcRequest.Metadata):
            vRPC metadata.
        payload (bytes):
            Could be TableRequest (or in post-V1,
            SqlRequest)
    """

    class Metadata(proto.Message):
        r"""Container for all vRPC Metadata.

        Attributes:
            attempt_number (int):
                Track retry attempts for this vRPC at the
                AFE.
            attempt_start (google.protobuf.timestamp_pb2.Timestamp):
                Track the client's known start time for the
                attempt. This is likely not easily compared with
                the server's time due to clock skew.
            traceparent (str):
                Link OpenTelemetry traces (e.g. Tapper). This
                can be used to link attempts together for the
                same logical operation (e.g. in logs / traces).

                Note, this may not be needed for V1, TBD.
            delay (google.protobuf.duration_pb2.Duration):
                How long to delay the operation for on the
                server-side, for testing.
        """

        attempt_number: int = proto.Field(
            proto.INT64,
            number=1,
        )
        attempt_start: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        traceparent: str = proto.Field(
            proto.STRING,
            number=3,
        )
        delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )

    rpc_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    deadline: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    metadata: Metadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Metadata,
    )
    payload: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )


class ContinueVirtualRpcRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        rpc_id (int):

    """

    rpc_id: int = proto.Field(
        proto.INT64,
        number=1,
    )


class CancelVirtualRpcRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        rpc_id (int):

    """

    rpc_id: int = proto.Field(
        proto.INT64,
        number=1,
    )


class ClusterInformation(proto.Message):
    r"""Information on which Cluster served a vRPC, e.g. for
    Client-Side metrics. Internal usage only.

    Attributes:
        cluster_id (str):

        zone_id (str):

    """

    cluster_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SessionRequestStats(proto.Message):
    r"""Internal usage only.

    Attributes:
        backend_latency (google.protobuf.duration_pb2.Duration):
            Backend (critical section) latency for the
            request.
    """

    backend_latency: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class VirtualRpcResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        rpc_id (int):
            Which vRPC this response is for.
        cluster_info (google.cloud.bigtable_v2.types.ClusterInformation):

        stats (google.cloud.bigtable_v2.types.SessionRequestStats):

        payload (bytes):
            Could be TableResponse (or in post-V1,
            SqlResponse)
        has_more (bool):
            If there are more responses for this rpc_id coming.
    """

    rpc_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    cluster_info: "ClusterInformation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ClusterInformation",
    )
    stats: "SessionRequestStats" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SessionRequestStats",
    )
    payload: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    has_more: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ErrorResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        rpc_id (int):
            Which vRPC this response is for.
        cluster_info (google.cloud.bigtable_v2.types.ClusterInformation):

        status (google.rpc.status_pb2.Status):
            The error from the vRPC and any retry
            information to consider.
        retry_info (google.rpc.error_details_pb2.RetryInfo):

    """

    rpc_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    cluster_info: "ClusterInformation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ClusterInformation",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    retry_info: error_details_pb2.RetryInfo = proto.Field(
        proto.MESSAGE,
        number=4,
        message=error_details_pb2.RetryInfo,
    )


class TableRequest(proto.Message):
    r"""Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_row (google.cloud.bigtable_v2.types.SessionReadRowRequest):

            This field is a member of `oneof`_ ``payload``.
        mutate_row (google.cloud.bigtable_v2.types.SessionMutateRowRequest):

            This field is a member of `oneof`_ ``payload``.
        read_rows (google.cloud.bigtable_v2.types.SessionReadRowsRequest):

            This field is a member of `oneof`_ ``payload``.
        check_and_mutate_row (google.cloud.bigtable_v2.types.SessionCheckAndMutateRowRequest):

            This field is a member of `oneof`_ ``payload``.
        read_modify_write_row (google.cloud.bigtable_v2.types.SessionReadModifyWriteRowRequest):

            This field is a member of `oneof`_ ``payload``.
        mutate_rows (google.cloud.bigtable_v2.types.SessionMutateRowsRequest):

            This field is a member of `oneof`_ ``payload``.
    """

    read_row: "SessionReadRowRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="payload",
        message="SessionReadRowRequest",
    )
    mutate_row: "SessionMutateRowRequest" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message="SessionMutateRowRequest",
    )
    read_rows: "SessionReadRowsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="payload",
        message="SessionReadRowsRequest",
    )
    check_and_mutate_row: "SessionCheckAndMutateRowRequest" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="payload",
        message="SessionCheckAndMutateRowRequest",
    )
    read_modify_write_row: "SessionReadModifyWriteRowRequest" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="payload",
        message="SessionReadModifyWriteRowRequest",
    )
    mutate_rows: "SessionMutateRowsRequest" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="payload",
        message="SessionMutateRowsRequest",
    )


class TableResponse(proto.Message):
    r"""Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_row (google.cloud.bigtable_v2.types.SessionReadRowResponse):

            This field is a member of `oneof`_ ``payload``.
        mutate_row (google.cloud.bigtable_v2.types.SessionMutateRowResponse):

            This field is a member of `oneof`_ ``payload``.
        read_rows (google.cloud.bigtable_v2.types.SessionReadRowsResponse):

            This field is a member of `oneof`_ ``payload``.
        check_and_mutate_row (google.cloud.bigtable_v2.types.SessionCheckAndMutateRowResponse):

            This field is a member of `oneof`_ ``payload``.
        read_modify_write_row (google.cloud.bigtable_v2.types.SessionReadModifyWriteRowResponse):

            This field is a member of `oneof`_ ``payload``.
        mutate_rows (google.cloud.bigtable_v2.types.SessionMutateRowsResponse):

            This field is a member of `oneof`_ ``payload``.
    """

    read_row: "SessionReadRowResponse" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="payload",
        message="SessionReadRowResponse",
    )
    mutate_row: "SessionMutateRowResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message="SessionMutateRowResponse",
    )
    read_rows: "SessionReadRowsResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="payload",
        message="SessionReadRowsResponse",
    )
    check_and_mutate_row: "SessionCheckAndMutateRowResponse" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="payload",
        message="SessionCheckAndMutateRowResponse",
    )
    read_modify_write_row: "SessionReadModifyWriteRowResponse" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="payload",
        message="SessionReadModifyWriteRowResponse",
    )
    mutate_rows: "SessionMutateRowsResponse" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="payload",
        message="SessionMutateRowsResponse",
    )


class AuthorizedViewRequest(proto.Message):
    r"""A request wrapper for operations on an authorized view.
    Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_row (google.cloud.bigtable_v2.types.SessionReadRowRequest):

            This field is a member of `oneof`_ ``payload``.
        mutate_row (google.cloud.bigtable_v2.types.SessionMutateRowRequest):

            This field is a member of `oneof`_ ``payload``.
        read_rows (google.cloud.bigtable_v2.types.SessionReadRowsRequest):

            This field is a member of `oneof`_ ``payload``.
        check_and_mutate_row (google.cloud.bigtable_v2.types.SessionCheckAndMutateRowRequest):

            This field is a member of `oneof`_ ``payload``.
        read_modify_write_row (google.cloud.bigtable_v2.types.SessionReadModifyWriteRowRequest):

            This field is a member of `oneof`_ ``payload``.
        mutate_rows (google.cloud.bigtable_v2.types.SessionMutateRowsRequest):

            This field is a member of `oneof`_ ``payload``.
    """

    read_row: "SessionReadRowRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="payload",
        message="SessionReadRowRequest",
    )
    mutate_row: "SessionMutateRowRequest" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message="SessionMutateRowRequest",
    )
    read_rows: "SessionReadRowsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="payload",
        message="SessionReadRowsRequest",
    )
    check_and_mutate_row: "SessionCheckAndMutateRowRequest" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="payload",
        message="SessionCheckAndMutateRowRequest",
    )
    read_modify_write_row: "SessionReadModifyWriteRowRequest" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="payload",
        message="SessionReadModifyWriteRowRequest",
    )
    mutate_rows: "SessionMutateRowsRequest" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="payload",
        message="SessionMutateRowsRequest",
    )


class AuthorizedViewResponse(proto.Message):
    r"""A response wrapper for operations on an authorized view.
    Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_row (google.cloud.bigtable_v2.types.SessionReadRowResponse):

            This field is a member of `oneof`_ ``payload``.
        mutate_row (google.cloud.bigtable_v2.types.SessionMutateRowResponse):

            This field is a member of `oneof`_ ``payload``.
        read_rows (google.cloud.bigtable_v2.types.SessionReadRowsResponse):

            This field is a member of `oneof`_ ``payload``.
        check_and_mutate_row (google.cloud.bigtable_v2.types.SessionCheckAndMutateRowResponse):

            This field is a member of `oneof`_ ``payload``.
        read_modify_write_row (google.cloud.bigtable_v2.types.SessionReadModifyWriteRowResponse):

            This field is a member of `oneof`_ ``payload``.
        mutate_rows (google.cloud.bigtable_v2.types.SessionMutateRowsResponse):

            This field is a member of `oneof`_ ``payload``.
    """

    read_row: "SessionReadRowResponse" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="payload",
        message="SessionReadRowResponse",
    )
    mutate_row: "SessionMutateRowResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message="SessionMutateRowResponse",
    )
    read_rows: "SessionReadRowsResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="payload",
        message="SessionReadRowsResponse",
    )
    check_and_mutate_row: "SessionCheckAndMutateRowResponse" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="payload",
        message="SessionCheckAndMutateRowResponse",
    )
    read_modify_write_row: "SessionReadModifyWriteRowResponse" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="payload",
        message="SessionReadModifyWriteRowResponse",
    )
    mutate_rows: "SessionMutateRowsResponse" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="payload",
        message="SessionMutateRowsResponse",
    )


class MaterializedViewRequest(proto.Message):
    r"""A request wrapper for operations on a materialized view.
    Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_row (google.cloud.bigtable_v2.types.SessionReadRowRequest):

            This field is a member of `oneof`_ ``payload``.
        read_rows (google.cloud.bigtable_v2.types.SessionReadRowsRequest):

            This field is a member of `oneof`_ ``payload``.
    """

    read_row: "SessionReadRowRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="payload",
        message="SessionReadRowRequest",
    )
    read_rows: "SessionReadRowsRequest" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message="SessionReadRowsRequest",
    )


class MaterializedViewResponse(proto.Message):
    r"""A response wrapper for operations on a materialized view.
    Internal usage only.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_row (google.cloud.bigtable_v2.types.SessionReadRowResponse):

            This field is a member of `oneof`_ ``payload``.
        read_rows (google.cloud.bigtable_v2.types.SessionReadRowsResponse):

            This field is a member of `oneof`_ ``payload``.
    """

    read_row: "SessionReadRowResponse" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="payload",
        message="SessionReadRowResponse",
    )
    read_rows: "SessionReadRowsResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message="SessionReadRowsResponse",
    )


class SessionReadRowRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        key (bytes):

        filter (google.cloud.bigtable_v2.types.RowFilter):

    """

    key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    filter: data.RowFilter = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data.RowFilter,
    )


class SessionReadRowResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        row (google.cloud.bigtable_v2.types.Row):

        stats (google.cloud.bigtable_v2.types.RequestStats):

    """

    row: data.Row = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.Row,
    )
    stats: request_stats.RequestStats = proto.Field(
        proto.MESSAGE,
        number=2,
        message=request_stats.RequestStats,
    )


class SessionReadRowsRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        rows (google.cloud.bigtable_v2.types.RowSet):

        filter (google.cloud.bigtable_v2.types.RowFilter):

        rows_limit (int):

        reversed (bool):

    """

    rows: data.RowSet = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.RowSet,
    )
    filter: data.RowFilter = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data.RowFilter,
    )
    rows_limit: int = proto.Field(
        proto.INT64,
        number=3,
    )
    reversed: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class SessionReadRowsResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        row (MutableSequence[google.cloud.bigtable_v2.types.Row]):

        stats (google.cloud.bigtable_v2.types.RequestStats):

    """

    row: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.Row,
    )
    stats: request_stats.RequestStats = proto.Field(
        proto.MESSAGE,
        number=2,
        message=request_stats.RequestStats,
    )


class SessionMutateRowRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        key (bytes):

        mutations (MutableSequence[google.cloud.bigtable_v2.types.Mutation]):

    """

    key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    mutations: MutableSequence[data.Mutation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.Mutation,
    )


class SessionMutateRowResponse(proto.Message):
    r"""Internal usage only."""


class SessionCheckAndMutateRowRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        key (bytes):

        predicate_filter (google.cloud.bigtable_v2.types.RowFilter):

        true_mutations (MutableSequence[google.cloud.bigtable_v2.types.Mutation]):

        false_mutations (MutableSequence[google.cloud.bigtable_v2.types.Mutation]):

    """

    key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    predicate_filter: data.RowFilter = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data.RowFilter,
    )
    true_mutations: MutableSequence[data.Mutation] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Mutation,
    )
    false_mutations: MutableSequence[data.Mutation] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.Mutation,
    )


class SessionCheckAndMutateRowResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        predicate_matched (bool):

    """

    predicate_matched: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class SessionReadModifyWriteRowRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        key (bytes):

        rules (MutableSequence[google.cloud.bigtable_v2.types.ReadModifyWriteRule]):

    """

    key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    rules: MutableSequence[data.ReadModifyWriteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.ReadModifyWriteRule,
    )


class SessionReadModifyWriteRowResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        row (google.cloud.bigtable_v2.types.Row):

    """

    row: data.Row = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.Row,
    )


class SessionMutateRowsRequest(proto.Message):
    r"""Internal usage only.

    Attributes:
        entries (MutableSequence[google.cloud.bigtable_v2.types.SessionMutateRowsRequest.Entry]):
            The row keys and corresponding mutations to
            be applied in bulk.
    """

    class Entry(proto.Message):
        r"""A mutation for a given row.

        Attributes:
            key (bytes):
                The key of the row to which the ``mutations`` should be
                applied.
            mutations (MutableSequence[google.cloud.bigtable_v2.types.Mutation]):
                Changes to be atomically applied to the
                specified row.
            idempotency (google.cloud.bigtable_v2.types.Idempotency):
                The idempotency of the mutation.
        """

        key: bytes = proto.Field(
            proto.BYTES,
            number=1,
        )
        mutations: MutableSequence[data.Mutation] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=data.Mutation,
        )
        idempotency: data.Idempotency = proto.Field(
            proto.MESSAGE,
            number=3,
            message=data.Idempotency,
        )

    entries: MutableSequence[Entry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Entry,
    )


class SessionMutateRowsResponse(proto.Message):
    r"""Internal usage only.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        entries (MutableSequence[google.cloud.bigtable_v2.types.SessionMutateRowsResponse.Entry]):
            One or more results for Entries from the
            batch request.
        rate_limit_info (google.cloud.bigtable_v2.types.SessionMutateRowsResponse.RateLimitInfo):
            Information about how the client should
            adjust its rate of requests.

            This field is a member of `oneof`_ ``_rate_limit_info``.
    """

    class Entry(proto.Message):
        r"""The result of applying a passed mutation in the original
        request.

        Attributes:
            index (int):
                The index into the original request's ``entries`` list of
                the Entry for which a result is being reported.
            status (google.rpc.status_pb2.Status):
                The result of the request Entry identified by ``index``.
        """

        index: int = proto.Field(
            proto.INT64,
            number=1,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    class RateLimitInfo(proto.Message):
        r"""Rate limiting information for batched mutations.

        Attributes:
            period (google.protobuf.duration_pb2.Duration):
                Time that must pass before the client should
                adjust its rate again.
            factor (float):
                Multiplier that the client should apply to
                its current request rate.
        """

        period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        factor: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )

    entries: MutableSequence[Entry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Entry,
    )
    rate_limit_info: RateLimitInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=RateLimitInfo,
    )


class SessionParametersResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        keep_alive (google.protobuf.duration_pb2.Duration):
            Maximum time between messages that the AFE
            will send to the client. The client may use this
            information to determine its control-flow in
            relation to pruning black-holed or otherwise
            non-responsive sessions. Must be set and
            positive.

            See also Heartbeats.
        softmax_streaming_prefetch_buffer_bytes (int):
            Client will pull this many bytes at most to
            make messages for steamed responses. If the last
            byte is mid-message, it will continue until a
            full message comes.
    """

    keep_alive: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    softmax_streaming_prefetch_buffer_bytes: int = proto.Field(
        proto.INT32,
        number=2,
    )


class HeartbeatResponse(proto.Message):
    r"""Internal usage only."""


class GoAwayResponse(proto.Message):
    r"""Internal usage only.

    Attributes:
        reason (str):
            Server-generated reason for GOAWAY, including
            a plain-text description of why. 'reason' may be
            used for CSM, while both may be logged.
        description (str):

        last_rpc_id_admitted (int):
            The last vRPC which was admitted by the AFE.
            The client may expect the result from the vRPC
            on the stream before disconnecting, and should
            retry vRPCs beyond this boundary.
    """

    reason: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    last_rpc_id_admitted: int = proto.Field(
        proto.INT64,
        number=3,
    )


class SessionRefreshConfig(proto.Message):
    r"""Internal usage only.

    Attributes:
        optimized_open_request (google.cloud.bigtable_v2.types.OpenSessionRequest):
            An optimized Open request that the session
            may use on a retry when establishing this
            session again. This can be sent from the AFE to
            avoid certain work e.g. encoding a query plan
            for BTQL.
        metadata (MutableSequence[google.cloud.bigtable_v2.types.SessionRefreshConfig.Metadata]):
            Output only. Any additional metadata to
            include when reconnecting.
    """

    class Metadata(proto.Message):
        r"""Any additional metadata to include when reconnecting. Not a
        ``map<>`` type as this can be a multimap.

        Attributes:
            key (str):
                Output only. The key for the metadata entry.
            value (bytes):
                Output only. The value for the metadata
                entry.
        """

        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: bytes = proto.Field(
            proto.BYTES,
            number=2,
        )

    optimized_open_request: "OpenSessionRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OpenSessionRequest",
    )
    metadata: MutableSequence[Metadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Metadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
