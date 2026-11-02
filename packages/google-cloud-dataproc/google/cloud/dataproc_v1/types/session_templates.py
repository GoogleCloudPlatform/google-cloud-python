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

from google.cloud.dataproc_v1.types import sessions, shared

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "CreateSessionTemplateRequest",
        "UpdateSessionTemplateRequest",
        "GetSessionTemplateRequest",
        "ListSessionTemplatesRequest",
        "ListSessionTemplatesResponse",
        "DeleteSessionTemplateRequest",
        "SessionTemplate",
    },
)


class CreateSessionTemplateRequest(proto.Message):
    r"""A request to create a session template.

    Attributes:
        parent (str):
            Required. The parent resource where this
            session template will be created.
        session_template (google.cloud.dataproc_v1.types.SessionTemplate):
            Required. The session template to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    session_template: "SessionTemplate" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SessionTemplate",
    )


class UpdateSessionTemplateRequest(proto.Message):
    r"""A request to update a session template.

    Attributes:
        session_template (google.cloud.dataproc_v1.types.SessionTemplate):
            Required. The updated session template.
    """

    session_template: "SessionTemplate" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SessionTemplate",
    )


class GetSessionTemplateRequest(proto.Message):
    r"""A request to get the resource representation for a session
    template.

    Attributes:
        name (str):
            Required. The name of the session template to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSessionTemplatesRequest(proto.Message):
    r"""A request to list session templates in a project.

    Attributes:
        parent (str):
            Required. The parent that owns this
            collection of session templates.
        page_size (int):
            Optional. The maximum number of sessions to
            return in each response. The service may return
            fewer than this value.
        page_token (str):
            Optional. A page token received from a previous
            ``ListSessions`` call. Provide this token to retrieve the
            subsequent page.
        filter (str):
            Optional. A filter for the session templates to return in
            the response. Filters are case sensitive and have the
            following syntax:

            [field = value] AND [field [= value]] ...
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


class ListSessionTemplatesResponse(proto.Message):
    r"""A list of session templates.

    Attributes:
        session_templates (MutableSequence[google.cloud.dataproc_v1.types.SessionTemplate]):
            Output only. Session template list
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    session_templates: MutableSequence["SessionTemplate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SessionTemplate",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteSessionTemplateRequest(proto.Message):
    r"""A request to delete a session template.

    Attributes:
        name (str):
            Required. The name of the session template
            resource to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SessionTemplate(proto.Message):
    r"""A representation of a session template.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Identifier. The resource name of
            the session template.
        description (str):
            Optional. Brief description of the template.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the template was
            created.
        jupyter_session (google.cloud.dataproc_v1.types.JupyterConfig):
            Optional. Jupyter session config.

            This field is a member of `oneof`_ ``session_config``.
        spark_connect_session (google.cloud.dataproc_v1.types.SparkConnectConfig):
            Optional. Spark connect session config.

            This field is a member of `oneof`_ ``session_config``.
        creator (str):
            Output only. The email address of the user
            who created the template.
        labels (MutableMapping[str, str]):
            Optional. Labels to associate with sessions created using
            this template. Label **keys** must contain 1 to 63
            characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. Label
            **values** can be empty, but, if present, must contain 1 to
            63 characters and conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a session.
        runtime_config (google.cloud.dataproc_v1.types.RuntimeConfig):
            Optional. Runtime configuration for session
            execution.
        environment_config (google.cloud.dataproc_v1.types.EnvironmentConfig):
            Optional. Environment configuration for
            session execution.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the template was last
            updated.
        uuid (str):
            Output only. A session template UUID (Unique
            Universal Identifier). The service generates
            this value when it creates the session template.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    jupyter_session: sessions.JupyterConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="session_config",
        message=sessions.JupyterConfig,
    )
    spark_connect_session: sessions.SparkConnectConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="session_config",
        message=sessions.SparkConnectConfig,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    runtime_config: shared.RuntimeConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=shared.RuntimeConfig,
    )
    environment_config: shared.EnvironmentConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=shared.EnvironmentConfig,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
