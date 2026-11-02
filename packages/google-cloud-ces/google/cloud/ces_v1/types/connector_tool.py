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

import proto  # type: ignore

from google.cloud.ces_v1.types import auth

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "Action",
        "ConnectorTool",
    },
)


class Action(proto.Message):
    r"""Configuration of an Action for the tool to use.
    Note: This can be either an Action or an Operation. See
    https://cloud.google.com/integration-connectors/docs/entities-operation-action
    for details.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        connection_action_id (str):
            ID of a Connection action for the tool to
            use.

            This field is a member of `oneof`_ ``action_spec``.
        entity_operation (google.cloud.ces_v1.types.Action.EntityOperation):
            Entity operation configuration for the tool
            to use.

            This field is a member of `oneof`_ ``action_spec``.
        input_fields (MutableSequence[str]):
            Optional. Entity fields to use as inputs for
            the operation. If no fields are specified, all
            fields of the Entity will be used.
        output_fields (MutableSequence[str]):
            Optional. Entity fields to return from the
            operation. If no fields are specified, all
            fields of the Entity will be returned.
    """

    class EntityOperation(proto.Message):
        r"""Entity CRUD operation specification.

        Attributes:
            entity_id (str):
                Required. ID of the entity.
            operation (google.cloud.ces_v1.types.Action.EntityOperation.OperationType):
                Required. Operation to perform on the entity.
        """

        class OperationType(proto.Enum):
            r"""The operation to perform on the entity.

            Values:
                OPERATION_TYPE_UNSPECIFIED (0):
                    Operation type unspecified. Invalid,
                    ConnectorTool create/update will fail.
                LIST (1):
                    List operation.
                GET (2):
                    Get operation.
                CREATE (3):
                    Create operation.
                UPDATE (4):
                    Update operation.
                DELETE (5):
                    Delete operation.
            """

            OPERATION_TYPE_UNSPECIFIED = 0
            LIST = 1
            GET = 2
            CREATE = 3
            UPDATE = 4
            DELETE = 5

        entity_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        operation: "Action.EntityOperation.OperationType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Action.EntityOperation.OperationType",
        )

    connection_action_id: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="action_spec",
    )
    entity_operation: EntityOperation = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="action_spec",
        message=EntityOperation,
    )
    input_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    output_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ConnectorTool(proto.Message):
    r"""A ConnectorTool allows connections to different integrations.
    See:
    https://cloud.google.com/integration-connectors/docs/overview.

    Attributes:
        connection (str):
            Required. The full resource name of the referenced
            Integration Connectors Connection. Format:
            ``projects/{project}/locations/{location}/connections/{connection}``
        action (google.cloud.ces_v1.types.Action):
            Required. Action for the tool to use.
        auth_config (google.cloud.ces_v1.types.EndUserAuthConfig):
            Optional. Configures how authentication is handled in
            Integration Connectors. By default, an admin authentication
            is passed in the Integration Connectors API requests. You
            can override it with a different end-user authentication
            config. **Note**: The Connection must have authentication
            override enabled in order to specify an EUC configuration
            here - otherwise, the ConnectorTool creation will fail. See
            https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override
            for details.
        name (str):
            Optional. The name of the tool that can be
            used by the Agent to decide whether to call this
            ConnectorTool.
        description (str):
            Optional. The description of the tool that
            can be used by the Agent to decide whether to
            call this ConnectorTool.
    """

    connection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: "Action" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Action",
    )
    auth_config: auth.EndUserAuthConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=auth.EndUserAuthConfig,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
