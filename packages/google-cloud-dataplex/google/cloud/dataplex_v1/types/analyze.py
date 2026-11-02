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

from google.cloud.dataplex_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "Environment",
        "Content",
        "Session",
    },
)


class Environment(proto.Message):
    r"""Environment represents a user-visible compute infrastructure
    for analytics within a lake.

    Attributes:
        name (str):
            Output only. The relative resource name of the environment,
            of the form:
            projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id}
        display_name (str):
            Optional. User friendly display name.
        uid (str):
            Output only. System generated globally unique
            ID for the environment. This ID will be
            different if the environment is deleted and
            re-created with the same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Environment creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the environment
            was last updated.
        labels (MutableMapping[str, str]):
            Optional. User defined labels for the
            environment.
        description (str):
            Optional. Description of the environment.
        state (google.cloud.dataplex_v1.types.State):
            Output only. Current state of the
            environment.
        infrastructure_spec (google.cloud.dataplex_v1.types.Environment.InfrastructureSpec):
            Required. Infrastructure specification for
            the Environment.
        session_spec (google.cloud.dataplex_v1.types.Environment.SessionSpec):
            Optional. Configuration for sessions created
            for this environment.
        session_status (google.cloud.dataplex_v1.types.Environment.SessionStatus):
            Output only. Status of sessions created for
            this environment.
        endpoints (google.cloud.dataplex_v1.types.Environment.Endpoints):
            Output only. URI Endpoints to access sessions
            associated with the Environment.
    """

    class InfrastructureSpec(proto.Message):
        r"""Configuration for the underlying infrastructure used to run
        workloads.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            compute (google.cloud.dataplex_v1.types.Environment.InfrastructureSpec.ComputeResources):
                Optional. Compute resources needed for
                analyze interactive workloads.

                This field is a member of `oneof`_ ``resources``.
            os_image (google.cloud.dataplex_v1.types.Environment.InfrastructureSpec.OsImageRuntime):
                Required. Software Runtime Configuration for
                analyze interactive workloads.

                This field is a member of `oneof`_ ``runtime``.
        """

        class ComputeResources(proto.Message):
            r"""Compute resources associated with the analyze interactive
            workloads.

            Attributes:
                disk_size_gb (int):
                    Optional. Size in GB of the disk. Default is
                    100 GB.
                node_count (int):
                    Optional. Total number of nodes in the
                    sessions created for this environment.
                max_node_count (int):
                    Optional. Max configurable nodes. If max_node_count >
                    node_count, then auto-scaling is enabled.
            """

            disk_size_gb: int = proto.Field(
                proto.INT32,
                number=1,
            )
            node_count: int = proto.Field(
                proto.INT32,
                number=2,
            )
            max_node_count: int = proto.Field(
                proto.INT32,
                number=3,
            )

        class OsImageRuntime(proto.Message):
            r"""Software Runtime Configuration to run Analyze.

            Attributes:
                image_version (str):
                    Required. Dataplex Universal Catalog Image
                    version.
                java_libraries (MutableSequence[str]):
                    Optional. List of Java jars to be included in
                    the runtime environment. Valid input includes
                    Cloud Storage URIs to Jar binaries. For example,
                    gs://bucket-name/my/path/to/file.jar
                python_packages (MutableSequence[str]):
                    Optional. A list of python packages to be
                    installed. Valid formats include Cloud Storage
                    URI to a PIP installable library. For example,
                    gs://bucket-name/my/path/to/lib.tar.gz
                properties (MutableMapping[str, str]):
                    Optional. Spark properties to provide configuration for use
                    in sessions created for this environment. The properties to
                    set on daemon config files. Property keys are specified in
                    ``prefix:property`` format. The prefix must be "spark".
            """

            image_version: str = proto.Field(
                proto.STRING,
                number=1,
            )
            java_libraries: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            python_packages: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )
            properties: MutableMapping[str, str] = proto.MapField(
                proto.STRING,
                proto.STRING,
                number=4,
            )

        compute: "Environment.InfrastructureSpec.ComputeResources" = proto.Field(
            proto.MESSAGE,
            number=50,
            oneof="resources",
            message="Environment.InfrastructureSpec.ComputeResources",
        )
        os_image: "Environment.InfrastructureSpec.OsImageRuntime" = proto.Field(
            proto.MESSAGE,
            number=100,
            oneof="runtime",
            message="Environment.InfrastructureSpec.OsImageRuntime",
        )

    class SessionSpec(proto.Message):
        r"""Configuration for sessions created for this environment.

        Attributes:
            max_idle_duration (google.protobuf.duration_pb2.Duration):
                Optional. The idle time configuration of the
                session. The session will be auto-terminated at
                the end of this period.
            enable_fast_startup (bool):
                Optional. If True, this causes sessions to be
                pre-created and available for faster startup to
                enable interactive exploration use-cases. This
                defaults to False to avoid additional billed
                charges. These can only be set to True for the
                environment with name set to "default", and with
                default configuration.
        """

        max_idle_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        enable_fast_startup: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class SessionStatus(proto.Message):
        r"""Status of sessions created for this environment.

        Attributes:
            active (bool):
                Output only. Queries over sessions to mark
                whether the environment is currently active or
                not
        """

        active: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class Endpoints(proto.Message):
        r"""URI Endpoints to access sessions associated with the
        Environment.

        Attributes:
            notebooks (str):
                Output only. URI to serve notebook APIs
            sql (str):
                Output only. URI to serve SQL APIs
        """

        notebooks: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sql: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: resources.State = proto.Field(
        proto.ENUM,
        number=8,
        enum=resources.State,
    )
    infrastructure_spec: InfrastructureSpec = proto.Field(
        proto.MESSAGE,
        number=100,
        message=InfrastructureSpec,
    )
    session_spec: SessionSpec = proto.Field(
        proto.MESSAGE,
        number=101,
        message=SessionSpec,
    )
    session_status: SessionStatus = proto.Field(
        proto.MESSAGE,
        number=102,
        message=SessionStatus,
    )
    endpoints: Endpoints = proto.Field(
        proto.MESSAGE,
        number=200,
        message=Endpoints,
    )


class Content(proto.Message):
    r"""Content represents a user-visible notebook or a sql script

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The relative resource name of the content, of
            the form:
            projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id}
        uid (str):
            Output only. System generated globally unique
            ID for the content. This ID will be different if
            the content is deleted and re-created with the
            same name.
        path (str):
            Required. The path for the Content file,
            represented as directory structure. Unique
            within a lake. Limited to alphanumerics,
            hyphens, underscores, dots and slashes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Content creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the content was
            last updated.
        labels (MutableMapping[str, str]):
            Optional. User defined labels for the
            content.
        description (str):
            Optional. Description of the content.
        data_text (str):
            Required. Content data in string format.

            This field is a member of `oneof`_ ``data``.
        sql_script (google.cloud.dataplex_v1.types.Content.SqlScript):
            Sql Script related configurations.

            This field is a member of `oneof`_ ``content``.
        notebook (google.cloud.dataplex_v1.types.Content.Notebook):
            Notebook related configurations.

            This field is a member of `oneof`_ ``content``.
    """

    class SqlScript(proto.Message):
        r"""Configuration for the Sql Script content.

        Attributes:
            engine (google.cloud.dataplex_v1.types.Content.SqlScript.QueryEngine):
                Required. Query Engine to be used for the Sql
                Query.
        """

        class QueryEngine(proto.Enum):
            r"""Query Engine Type of the SQL Script.

            Values:
                QUERY_ENGINE_UNSPECIFIED (0):
                    Value was unspecified.
                SPARK (2):
                    Spark SQL Query.
            """

            QUERY_ENGINE_UNSPECIFIED = 0
            SPARK = 2

        engine: "Content.SqlScript.QueryEngine" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Content.SqlScript.QueryEngine",
        )

    class Notebook(proto.Message):
        r"""Configuration for Notebook content.

        Attributes:
            kernel_type (google.cloud.dataplex_v1.types.Content.Notebook.KernelType):
                Required. Kernel Type of the notebook.
        """

        class KernelType(proto.Enum):
            r"""Kernel Type of the Jupyter notebook.

            Values:
                KERNEL_TYPE_UNSPECIFIED (0):
                    Kernel Type unspecified.
                PYTHON3 (1):
                    Python 3 Kernel.
            """

            KERNEL_TYPE_UNSPECIFIED = 0
            PYTHON3 = 1

        kernel_type: "Content.Notebook.KernelType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Content.Notebook.KernelType",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    data_text: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="data",
    )
    sql_script: SqlScript = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="content",
        message=SqlScript,
    )
    notebook: Notebook = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="content",
        message=Notebook,
    )


class Session(proto.Message):
    r"""Represents an active analyze session running for a user.

    Attributes:
        name (str):
            Output only. The relative resource name of the content, of
            the form:
            projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id}/sessions/{session_id}
        user_id (str):
            Output only. Email of user running the
            session.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Session start time.
        state (google.cloud.dataplex_v1.types.State):
            Output only. State of Session
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: resources.State = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
