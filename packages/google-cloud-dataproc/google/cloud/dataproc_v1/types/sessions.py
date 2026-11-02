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

from google.cloud.dataproc_v1.types import shared

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "CreateSessionRequest",
        "GetSessionRequest",
        "ListSessionsRequest",
        "ListSessionsResponse",
        "TerminateSessionRequest",
        "DeleteSessionRequest",
        "Session",
        "JupyterConfig",
        "SparkConnectConfig",
    },
)


class CreateSessionRequest(proto.Message):
    r"""A request to create a session.

    Attributes:
        parent (str):
            Required. The parent resource where this
            session will be created.
        session (google.cloud.dataproc_v1.types.Session):
            Required. The interactive session to create.
        session_id (str):
            Required. The ID to use for the session, which becomes the
            final component of the session's resource name.

            This value must be 4-63 characters. Valid characters are
            /[a-z][0-9]-/.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            service receives two
            `CreateSessionRequests <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.CreateSessionRequest>`__\ s
            with the same ID, the second request is ignored, and the
            first [Session][google.cloud.dataproc.v1.Session] is created
            and stored in the backend.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The value must contain only letters (a-z, A-Z), numbers
            (0-9), underscores (\_), and hyphens (-). The maximum length
            is 40 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    session: "Session" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Session",
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetSessionRequest(proto.Message):
    r"""A request to get the resource representation for a session.

    Attributes:
        name (str):
            Required. The name of the session to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSessionsRequest(proto.Message):
    r"""A request to list sessions in a project.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of sessions.
        page_size (int):
            Optional. The maximum number of sessions to
            return in each response. The service may return
            fewer than this value.
        page_token (str):
            Optional. A page token received from a previous
            ``ListSessions`` call. Provide this token to retrieve the
            subsequent page.
        filter (str):
            Optional. A filter for the sessions to return in the
            response.

            A filter is a logical expression constraining the values of
            various fields in each session resource. Filters are case
            sensitive, and may contain multiple clauses combined with
            logical operators (AND, OR). Supported fields are
            ``session_id``, ``session_uuid``, ``state``,
            ``create_time``, and ``labels``.

            Example:
            ``state = ACTIVE and create_time < "2023-01-01T00:00:00Z"``
            is a filter for sessions in an ACTIVE state that were
            created before 2023-01-01.
            ``state = ACTIVE and labels.environment=production`` is a
            filter for sessions in an ACTIVE state that have a
            production environment label.

            See https://google.aip.dev/assets/misc/ebnf-filtering.txt
            for a detailed description of the filter syntax and a list
            of supported comparators.
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


class ListSessionsResponse(proto.Message):
    r"""A list of interactive sessions.

    Attributes:
        sessions (MutableSequence[google.cloud.dataproc_v1.types.Session]):
            Output only. The sessions from the specified
            collection.
        next_page_token (str):
            A token, which can be sent as ``page_token``, to retrieve
            the next page. If this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    sessions: MutableSequence["Session"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Session",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TerminateSessionRequest(proto.Message):
    r"""A request to terminate an interactive session.

    Attributes:
        name (str):
            Required. The name of the session resource to
            terminate.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            service receives two
            `TerminateSessionRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.TerminateSessionRequest>`__\ s
            with the same ID, the second request is ignored.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The value must contain only letters (a-z, A-Z), numbers
            (0-9), underscores (\_), and hyphens (-). The maximum length
            is 40 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteSessionRequest(proto.Message):
    r"""A request to delete a session.

    Attributes:
        name (str):
            Required. The name of the session resource to
            delete.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            service receives two
            `DeleteSessionRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.DeleteSessionRequest>`__\ s
            with the same ID, the second request is ignored.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The value must contain only letters (a-z, A-Z), numbers
            (0-9), underscores (\_), and hyphens (-). The maximum length
            is 40 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Session(proto.Message):
    r"""A representation of a session.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the session.
        uuid (str):
            Output only. A session UUID (Unique Universal
            Identifier). The service generates this value
            when it creates the session.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the session was
            created.
        jupyter_session (google.cloud.dataproc_v1.types.JupyterConfig):
            Optional. Jupyter session config.

            This field is a member of `oneof`_ ``session_config``.
        spark_connect_session (google.cloud.dataproc_v1.types.SparkConnectConfig):
            Optional. Spark connect session config.

            This field is a member of `oneof`_ ``session_config``.
        runtime_info (google.cloud.dataproc_v1.types.RuntimeInfo):
            Output only. Runtime information about
            session execution.
        state (google.cloud.dataproc_v1.types.Session.State):
            Output only. A state of the session.
        state_message (str):
            Output only. Session state details, such as the failure
            description if the state is ``FAILED``.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the session
            entered the current state.
        creator (str):
            Output only. The email address of the user
            who created the session.
        labels (MutableMapping[str, str]):
            Optional. The labels to associate with the session. Label
            **keys** must contain 1 to 63 characters, and must conform
            to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Label **values** may be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a session.
        runtime_config (google.cloud.dataproc_v1.types.RuntimeConfig):
            Optional. Runtime configuration for the
            session execution.
        environment_config (google.cloud.dataproc_v1.types.EnvironmentConfig):
            Optional. Environment configuration for the
            session execution.
        user (str):
            Optional. The email address of the user who
            owns the session.
        state_history (MutableSequence[google.cloud.dataproc_v1.types.Session.SessionStateHistory]):
            Output only. Historical state information for
            the session.
        session_template (str):
            Optional. The session template used by the session.

            Only resource names, including project ID and location, are
            valid.

            Example:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]``
            - ``projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]``

            The template must be in the same project and Dataproc region
            as the session.
    """

    class State(proto.Enum):
        r"""The session state.

        Values:
            STATE_UNSPECIFIED (0):
                The session state is unknown.
            CREATING (1):
                The session is created prior to running.
            ACTIVE (2):
                The session is running.
            TERMINATING (3):
                The session is terminating.
            TERMINATED (4):
                The session is terminated successfully.
            FAILED (5):
                The session is no longer running due to an
                error.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        TERMINATING = 3
        TERMINATED = 4
        FAILED = 5

    class SessionStateHistory(proto.Message):
        r"""Historical state information.

        Attributes:
            state (google.cloud.dataproc_v1.types.Session.State):
                Output only. The state of the session at this
                point in the session history.
            state_message (str):
                Output only. Details about the state at this
                point in the session history.
            state_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the session
                entered the historical state.
        """

        state: "Session.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Session.State",
        )
        state_message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        state_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    jupyter_session: "JupyterConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="session_config",
        message="JupyterConfig",
    )
    spark_connect_session: "SparkConnectConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="session_config",
        message="SparkConnectConfig",
    )
    runtime_info: shared.RuntimeInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=shared.RuntimeInfo,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=8,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=10,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    runtime_config: shared.RuntimeConfig = proto.Field(
        proto.MESSAGE,
        number=12,
        message=shared.RuntimeConfig,
    )
    environment_config: shared.EnvironmentConfig = proto.Field(
        proto.MESSAGE,
        number=13,
        message=shared.EnvironmentConfig,
    )
    user: str = proto.Field(
        proto.STRING,
        number=14,
    )
    state_history: MutableSequence[SessionStateHistory] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=SessionStateHistory,
    )
    session_template: str = proto.Field(
        proto.STRING,
        number=16,
    )


class JupyterConfig(proto.Message):
    r"""Jupyter configuration for an interactive session.

    Attributes:
        kernel (google.cloud.dataproc_v1.types.JupyterConfig.Kernel):
            Optional. Kernel
        display_name (str):
            Optional. Display name, shown in the Jupyter
            kernelspec card.
    """

    class Kernel(proto.Enum):
        r"""Jupyter kernel types.

        Values:
            KERNEL_UNSPECIFIED (0):
                The kernel is unknown.
            PYTHON (1):
                Python kernel.
            SCALA (2):
                Scala kernel.
        """

        KERNEL_UNSPECIFIED = 0
        PYTHON = 1
        SCALA = 2

    kernel: Kernel = proto.Field(
        proto.ENUM,
        number=1,
        enum=Kernel,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SparkConnectConfig(proto.Message):
    r"""Spark connect configuration for an interactive session."""


__all__ = tuple(sorted(__protobuf__.manifest))
