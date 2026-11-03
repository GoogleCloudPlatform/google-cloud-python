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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.beyondcorp_appconnectors_v1.types import app_connector_instance_config
from google.cloud.beyondcorp_appconnectors_v1.types import (
    resource_info as gcba_resource_info,
)

__protobuf__ = proto.module(
    package="google.cloud.beyondcorp.appconnectors.v1",
    manifest={
        "ListAppConnectorsRequest",
        "ListAppConnectorsResponse",
        "GetAppConnectorRequest",
        "CreateAppConnectorRequest",
        "UpdateAppConnectorRequest",
        "DeleteAppConnectorRequest",
        "ResolveInstanceConfigRequest",
        "ResolveInstanceConfigResponse",
        "ReportStatusRequest",
        "AppConnector",
        "AppConnectorOperationMetadata",
    },
)


class ListAppConnectorsRequest(proto.Message):
    r"""Request message for BeyondCorp.ListAppConnectors.

    Attributes:
        parent (str):
            Required. The resource name of the AppConnector location
            using the form:
            ``projects/{project_id}/locations/{location_id}``
        page_size (int):
            Optional. The maximum number of items to return. If not
            specified, a default value of 50 will be used by the
            service. Regardless of the page_size value, the response may
            include a partial list and a caller should only rely on
            response's
            [next_page_token][google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            ListAppConnectorsRequest, if any.
        filter (str):
            Optional. A filter specifying constraints of
            a list operation.
        order_by (str):
            Optional. Specifies the ordering of results. See `Sorting
            order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__
            for more information.
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


class ListAppConnectorsResponse(proto.Message):
    r"""Response message for BeyondCorp.ListAppConnectors.

    Attributes:
        app_connectors (MutableSequence[google.cloud.beyondcorp_appconnectors_v1.types.AppConnector]):
            A list of BeyondCorp AppConnectors in the
            project.
        next_page_token (str):
            A token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            A list of locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    app_connectors: MutableSequence["AppConnector"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AppConnector",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAppConnectorRequest(proto.Message):
    r"""Request message for BeyondCorp.GetAppConnector.

    Attributes:
        name (str):
            Required. BeyondCorp AppConnector name using the form:
            ``projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAppConnectorRequest(proto.Message):
    r"""Request message for BeyondCorp.CreateAppConnector.

    Attributes:
        parent (str):
            Required. The resource project name of the AppConnector
            location using the form:
            ``projects/{project_id}/locations/{location_id}``
        app_connector_id (str):
            Optional. User-settable AppConnector resource ID.

            - Must start with a letter.
            - Must contain between 4-63 characters from
              ``/[a-z][0-9]-/``.
            - Must end with a number or a letter.
        app_connector (google.cloud.beyondcorp_appconnectors_v1.types.AppConnector):
            Required. A BeyondCorp AppConnector resource.
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
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_connector_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    app_connector: "AppConnector" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AppConnector",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateAppConnectorRequest(proto.Message):
    r"""Request message for BeyondCorp.UpdateAppConnector.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field may only include these fields from
            [BeyondCorp.AppConnector]:

            - ``labels``
            - ``display_name``
        app_connector (google.cloud.beyondcorp_appconnectors_v1.types.AppConnector):
            Required. AppConnector message with updated fields. Only
            supported fields specified in update_mask are updated.
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
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    app_connector: "AppConnector" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AppConnector",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteAppConnectorRequest(proto.Message):
    r"""Request message for BeyondCorp.DeleteAppConnector.

    Attributes:
        name (str):
            Required. BeyondCorp AppConnector name using the form:
            ``projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}``
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
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ResolveInstanceConfigRequest(proto.Message):
    r"""Request message for BeyondCorp.ResolveInstanceConfig.

    Attributes:
        app_connector (str):
            Required. BeyondCorp AppConnector name using the form:
            ``projects/{project_id}/locations/{location_id}/appConnectors/{app_connector}``
    """

    app_connector: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResolveInstanceConfigResponse(proto.Message):
    r"""Response message for BeyondCorp.ResolveInstanceConfig.

    Attributes:
        instance_config (google.cloud.beyondcorp_appconnectors_v1.types.AppConnectorInstanceConfig):
            AppConnectorInstanceConfig.
    """

    instance_config: app_connector_instance_config.AppConnectorInstanceConfig = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=app_connector_instance_config.AppConnectorInstanceConfig,
        )
    )


class ReportStatusRequest(proto.Message):
    r"""Request report the connector status.

    Attributes:
        app_connector (str):
            Required. BeyondCorp Connector name using the form:
            ``projects/{project_id}/locations/{location_id}/connectors/{connector}``
        resource_info (google.cloud.beyondcorp_appconnectors_v1.types.ResourceInfo):
            Required. Resource info of the connector.
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
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    app_connector: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_info: gcba_resource_info.ResourceInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcba_resource_info.ResourceInfo,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class AppConnector(proto.Message):
    r"""A BeyondCorp connector resource that represents an
    application facing component deployed proximal to and with
    direct access to the application instances. It is used to
    establish connectivity between the remote enterprise environment
    and GCP. It initiates connections to the applications and can
    proxy the data from users over the connection.

    Attributes:
        name (str):
            Required. Unique resource name of the
            AppConnector. The name is ignored when creating
            a AppConnector.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            last modified.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata.
        display_name (str):
            Optional. An arbitrary user-provided name for
            the AppConnector. Cannot exceed 64 characters.
        uid (str):
            Output only. A unique identifier for the
            instance generated by the system.
        state (google.cloud.beyondcorp_appconnectors_v1.types.AppConnector.State):
            Output only. The current state of the
            AppConnector.
        principal_info (google.cloud.beyondcorp_appconnectors_v1.types.AppConnector.PrincipalInfo):
            Required. Principal information about the
            Identity of the AppConnector.
        resource_info (google.cloud.beyondcorp_appconnectors_v1.types.ResourceInfo):
            Optional. Resource info of the connector.
    """

    class State(proto.Enum):
        r"""Represents the different states of a AppConnector.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                AppConnector is being created.
            CREATED (2):
                AppConnector has been created.
            UPDATING (3):
                AppConnector's configuration is being
                updated.
            DELETING (4):
                AppConnector is being deleted.
            DOWN (5):
                AppConnector is down and may be restored in
                the future. This happens when CCFE sends
                ProjectState = OFF.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        UPDATING = 3
        DELETING = 4
        DOWN = 5

    class PrincipalInfo(proto.Message):
        r"""PrincipalInfo represents an Identity oneof.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            service_account (google.cloud.beyondcorp_appconnectors_v1.types.AppConnector.PrincipalInfo.ServiceAccount):
                A GCP service account.

                This field is a member of `oneof`_ ``type``.
        """

        class ServiceAccount(proto.Message):
            r"""ServiceAccount represents a GCP service account.

            Attributes:
                email (str):
                    Email address of the service account.
            """

            email: str = proto.Field(
                proto.STRING,
                number=1,
            )

        service_account: "AppConnector.PrincipalInfo.ServiceAccount" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message="AppConnector.PrincipalInfo.ServiceAccount",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
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
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    principal_info: PrincipalInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=PrincipalInfo,
    )
    resource_info: gcba_resource_info.ResourceInfo = proto.Field(
        proto.MESSAGE,
        number=11,
        message=gcba_resource_info.ResourceInfo,
    )


class AppConnectorOperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
