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

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "CreateCurationRequest",
        "GetCurationRequest",
        "UpdateCurationRequest",
        "DeleteCurationRequest",
        "ListCurationsRequest",
        "ListCurationsResponse",
        "Curation",
        "Endpoint",
        "ApplicationIntegrationEndpointDetails",
    },
)


class CreateCurationRequest(proto.Message):
    r"""The [CreateCuration][ApiHub.CreateCuration] method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the curation resource.
            Format: ``projects/{project}/locations/{location}``
        curation_id (str):
            Optional. The ID to use for the curation resource, which
            will become the final component of the curations's resource
            name. This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified ID is already used by another
              curation resource in the API hub.
            - If not provided, a system generated ID will be used.

            This value should be 4-500 characters, and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        curation (google.cloud.apihub_v1.types.Curation):
            Required. The curation resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    curation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    curation: "Curation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Curation",
    )


class GetCurationRequest(proto.Message):
    r"""The [GetCuration][ApiHub.GetCuration] method's request.

    Attributes:
        name (str):
            Required. The name of the curation resource to retrieve.
            Format:
            ``projects/{project}/locations/{location}/curations/{curation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCurationRequest(proto.Message):
    r"""The [UpdateCuration][ApiHub.UpdateCuration] method's request.

    Attributes:
        curation (google.cloud.apihub_v1.types.Curation):
            Required. The curation resource to update.

            The curation resource's ``name`` field is used to identify
            the curation resource to update. Format:
            ``projects/{project}/locations/{location}/curations/{curation}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    curation: "Curation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Curation",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCurationRequest(proto.Message):
    r"""The [DeleteCuration][ApiHub.DeleteCuration] method's request.

    Attributes:
        name (str):
            Required. The name of the curation resource to delete.
            Format:
            ``projects/{project}/locations/{location}/curations/{curation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCurationsRequest(proto.Message):
    r"""The [ListCurations][ApiHub.ListCurations] method's request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of curation
            resources. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            Optional. An expression that filters the list of curation
            resources.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. The comparison operator must be one of: ``<``,
            ``>``, ``:`` or ``=``. Filters are case insensitive.

            The following fields in the ``curation resource`` are
            eligible for filtering:

            - ``create_time`` - The time at which the curation was
              created. The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.
            - ``display_name`` - The display name of the curation.
              Allowed comparison operators: ``=``.
            - ``state`` - The state of the curation. Allowed comparison
              operators: ``=``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"``
              - The curation resource was created before *2021-08-15
              14:50:00 UTC* and after *2021-08-10 12:00:00 UTC*.
        page_size (int):
            Optional. The maximum number of curation
            resources to return. The service may return
            fewer than this value. If unspecified, at most
            50 curations will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCurations`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListCurations`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListCurationsResponse(proto.Message):
    r"""The [ListCurations][ApiHub.ListCurations] method's response.

    Attributes:
        curations (MutableSequence[google.cloud.apihub_v1.types.Curation]):
            The curation resources present in the API
            hub.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    curations: MutableSequence["Curation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Curation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Curation(proto.Message):
    r"""A curation resource in the API Hub.

    Attributes:
        name (str):
            Identifier. The name of the curation.

            Format:
            ``projects/{project}/locations/{location}/curations/{curation}``
        display_name (str):
            Required. The display name of the curation.
        description (str):
            Optional. The description of the curation.
        endpoint (google.cloud.apihub_v1.types.Endpoint):
            Required. The endpoint to be triggered for
            curation.
        plugin_instance_actions (MutableSequence[google.cloud.apihub_v1.types.Curation.PluginInstanceActionID]):
            Output only. The plugin instances and
            associated actions that are using the curation.
            Note: A particular curation could be used by
            multiple plugin instances or multiple actions in
            a plugin instance.
        last_execution_state (google.cloud.apihub_v1.types.Curation.LastExecutionState):
            Output only. The last execution state of the
            curation.
        last_execution_error_code (google.cloud.apihub_v1.types.Curation.ErrorCode):
            Output only. The error code of the last
            execution of the curation. The error code is
            populated only when the last execution state is
            failed.
        last_execution_error_message (str):
            Output only. Error message describing the
            failure, if any, during the last execution of
            the curation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the curation
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the curation
            was last updated.
    """

    class LastExecutionState(proto.Enum):
        r"""The state of the last execution of the curation.

        Values:
            LAST_EXECUTION_STATE_UNSPECIFIED (0):
                Default unspecified state.
            SUCCEEDED (1):
                The last curation execution was successful.
            FAILED (2):
                The last curation execution failed.
        """

        LAST_EXECUTION_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    class ErrorCode(proto.Enum):
        r"""The error codes for failed executions.

        Values:
            ERROR_CODE_UNSPECIFIED (0):
                Default unspecified error code.
            INTERNAL_ERROR (1):
                The execution failed due to an internal
                error.
            UNAUTHORIZED (2):
                The curation is not authorized to trigger the
                endpoint uri.
        """

        ERROR_CODE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        UNAUTHORIZED = 2

    class PluginInstanceActionID(proto.Message):
        r"""The plugin instance and associated action that is using the
        curation.

        Attributes:
            plugin_instance (str):
                Output only. Plugin instance that is using the curation.
                Format is
                ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``
            action_id (str):
                Output only. The action ID that is using the
                curation. This should map to one of the action
                IDs specified in action configs in the plugin.
        """

        plugin_instance: str = proto.Field(
            proto.STRING,
            number=1,
        )
        action_id: str = proto.Field(
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
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    endpoint: "Endpoint" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Endpoint",
    )
    plugin_instance_actions: MutableSequence[PluginInstanceActionID] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=PluginInstanceActionID,
        )
    )
    last_execution_state: LastExecutionState = proto.Field(
        proto.ENUM,
        number=6,
        enum=LastExecutionState,
    )
    last_execution_error_code: ErrorCode = proto.Field(
        proto.ENUM,
        number=7,
        enum=ErrorCode,
    )
    last_execution_error_message: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class Endpoint(proto.Message):
    r"""The endpoint to be triggered for curation. The endpoint will be
    invoked with a request payload containing
    [ApiMetadata][google.cloud.apihub.v1.ApiHub.ApiMetadata]. Response
    should contain curated data in the form of
    [ApiMetadata][google.cloud.apihub.v1.ApiHub.ApiMetadata].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        application_integration_endpoint_details (google.cloud.apihub_v1.types.ApplicationIntegrationEndpointDetails):
            Required. The details of the Application
            Integration endpoint to be triggered for
            curation.

            This field is a member of `oneof`_ ``endpoint_details``.
    """

    application_integration_endpoint_details: "ApplicationIntegrationEndpointDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="endpoint_details",
        message="ApplicationIntegrationEndpointDetails",
    )


class ApplicationIntegrationEndpointDetails(proto.Message):
    r"""The details of the Application Integration endpoint to be
    triggered for curation.

    Attributes:
        uri (str):
            Required. The endpoint URI should be a valid REST URI for
            triggering an Application Integration. Format:
            ``https://integrations.googleapis.com/v1/{name=projects/*/locations/*/integrations/*}:execute``
            or
            ``https://{location}-integrations.googleapis.com/v1/{name=projects/*/locations/*/integrations/*}:execute``
        trigger_id (str):
            Required. The API trigger ID of the
            Application Integration workflow.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
