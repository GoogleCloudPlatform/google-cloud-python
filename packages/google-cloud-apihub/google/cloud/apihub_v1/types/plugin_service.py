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

from google.cloud.apihub_v1.types import common_fields

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "ActionType",
        "GatewayType",
        "CurationType",
        "Plugin",
        "PluginActionConfig",
        "GetPluginRequest",
        "EnablePluginRequest",
        "DisablePluginRequest",
        "PluginInstanceAction",
        "PluginInstance",
        "CurationConfig",
        "ExecutionStatus",
        "CreatePluginRequest",
        "DeletePluginRequest",
        "ListPluginsRequest",
        "ListPluginsResponse",
        "CreatePluginInstanceRequest",
        "ExecutePluginInstanceActionRequest",
        "ActionExecutionDetail",
        "ExecutePluginInstanceActionResponse",
        "GetPluginInstanceRequest",
        "ListPluginInstancesRequest",
        "ListPluginInstancesResponse",
        "EnablePluginInstanceActionRequest",
        "EnablePluginInstanceActionResponse",
        "DisablePluginInstanceActionRequest",
        "DisablePluginInstanceActionResponse",
        "UpdatePluginInstanceRequest",
        "DeletePluginInstanceRequest",
    },
)


class ActionType(proto.Enum):
    r"""Enum for the action type.

    Values:
        ACTION_TYPE_UNSPECIFIED (0):
            Default unspecified action type.
        SYNC_METADATA (1):
            Action type for sync metadata.
        SYNC_RUNTIME_DATA (2):
            Action type for sync runtime data.
    """

    ACTION_TYPE_UNSPECIFIED = 0
    SYNC_METADATA = 1
    SYNC_RUNTIME_DATA = 2


class GatewayType(proto.Enum):
    r"""Enum for the gateway type.

    Values:
        GATEWAY_TYPE_UNSPECIFIED (0):
            The gateway type is not specified.
        APIGEE_X_AND_HYBRID (1):
            The gateway type is Apigee X and Hybrid.
        APIGEE_EDGE_PUBLIC_CLOUD (2):
            The gateway type is Apigee Edge Public Cloud.
        APIGEE_EDGE_PRIVATE_CLOUD (3):
            The gateway type is Apigee Edge Private
            Cloud.
        CLOUD_API_GATEWAY (4):
            The gateway type is Cloud API Gateway.
        CLOUD_ENDPOINTS (5):
            The gateway type is Cloud Endpoints.
        API_DISCOVERY (6):
            The gateway type is API Discovery.
        OTHERS (7):
            The gateway type for any other types of
            gateways.
    """

    GATEWAY_TYPE_UNSPECIFIED = 0
    APIGEE_X_AND_HYBRID = 1
    APIGEE_EDGE_PUBLIC_CLOUD = 2
    APIGEE_EDGE_PRIVATE_CLOUD = 3
    CLOUD_API_GATEWAY = 4
    CLOUD_ENDPOINTS = 5
    API_DISCOVERY = 6
    OTHERS = 7


class CurationType(proto.Enum):
    r"""Enum for the curation type.

    Values:
        CURATION_TYPE_UNSPECIFIED (0):
            Default unspecified curation type.
        DEFAULT_CURATION_FOR_API_METADATA (1):
            Default curation for API metadata will be
            used.
        CUSTOM_CURATION_FOR_API_METADATA (2):
            Custom curation for API metadata will be
            used.
    """

    CURATION_TYPE_UNSPECIFIED = 0
    DEFAULT_CURATION_FOR_API_METADATA = 1
    CUSTOM_CURATION_FOR_API_METADATA = 2


class Plugin(proto.Message):
    r"""A plugin resource in the API Hub.

    Attributes:
        name (str):
            Identifier. The name of the plugin. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``
        display_name (str):
            Required. The display name of the plugin. Max
            length is 50 characters (Unicode code points).
        type_ (google.cloud.apihub_v1.types.AttributeValues):
            Optional. The type of the API. This maps to the following
            system defined attribute:
            ``projects/{project}/locations/{location}/attributes/system-plugin-type``
            attribute. The number of allowed values for this attribute
            will be based on the cardinality of the attribute. The same
            can be retrieved via GetAttribute API. All values should be
            from the list of allowed values defined for the attribute.
            Note this field is not required for plugins developed via
            plugin framework.
        description (str):
            Optional. The plugin description. Max length
            is 2000 characters (Unicode code points).
        state (google.cloud.apihub_v1.types.Plugin.State):
            Output only. Represents the state of the
            plugin. Note this field will not be set for
            plugins developed via plugin framework as the
            state will be managed at plugin instance level.
        ownership_type (google.cloud.apihub_v1.types.Plugin.OwnershipType):
            Output only. The type of the plugin, indicating whether it
            is 'SYSTEM_OWNED' or 'USER_OWNED'.
        hosting_service (google.cloud.apihub_v1.types.Plugin.HostingService):
            Optional. This field is optional. It is used
            to notify the plugin hosting service for any
            lifecycle changes of the plugin instance and
            trigger execution of plugin instance actions in
            case of API hub managed actions.

            This field should be provided if the plugin
            instance lifecycle of the developed plugin needs
            to be managed from API hub. Also, in this case
            the plugin hosting service interface needs to be
            implemented.

            This field should not be provided if the plugin
            wants to manage plugin instance lifecycle events
            outside of hub interface and use plugin
            framework for only registering of plugin and
            plugin instances to capture the source of data
            into hub. Note, in this case the plugin hosting
            service interface is not required to be
            implemented. Also, the plugin instance lifecycle
            actions will be disabled from API hub's UI.
        actions_config (MutableSequence[google.cloud.apihub_v1.types.PluginActionConfig]):
            Optional. The configuration of actions supported by the
            plugin. **REQUIRED**: This field must be provided when
            creating or updating a Plugin. The server will reject
            requests if this field is missing.
        documentation (google.cloud.apihub_v1.types.Documentation):
            Optional. The documentation of the plugin,
            that explains how to set up and use the plugin.
        plugin_category (google.cloud.apihub_v1.types.PluginCategory):
            Optional. The category of the plugin,
            identifying its primary category or purpose.
            This field is required for all plugins.
        config_template (google.cloud.apihub_v1.types.Plugin.ConfigTemplate):
            Optional. The configuration template for the
            plugin.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            plugin was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            plugin was last updated.
        gateway_type (google.cloud.apihub_v1.types.GatewayType):
            Optional. The type of the gateway.
    """

    class State(proto.Enum):
        r"""Possible states a plugin can have. Note that this enum may
        receive new values in the future. Consumers are advised to
        always code against the enum values expecting new states can be
        added later on.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            ENABLED (1):
                The plugin is enabled.
            DISABLED (2):
                The plugin is disabled.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    class OwnershipType(proto.Enum):
        r"""Ownership type of the plugin.

        Values:
            OWNERSHIP_TYPE_UNSPECIFIED (0):
                Default unspecified type.
            SYSTEM_OWNED (1):
                System owned plugins are defined by API hub
                and are available out of the box in API hub.
            USER_OWNED (2):
                User owned plugins are defined by the user and need to be
                explicitly added to API hub via
                [CreatePlugin][google.cloud.apihub.v1.ApiHubPlugin.CreatePlugin]
                method.
        """

        OWNERSHIP_TYPE_UNSPECIFIED = 0
        SYSTEM_OWNED = 1
        USER_OWNED = 2

    class HostingService(proto.Message):
        r"""The information related to the service implemented by the
        plugin developer, used to invoke the plugin's functionality.

        Attributes:
            service_uri (str):
                Optional. The URI of the service implemented
                by the plugin developer, used to invoke the
                plugin's functionality. This information is only
                required for user defined plugins.
        """

        service_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ConfigTemplate(proto.Message):
        r"""ConfigTemplate represents the configuration template for a
        plugin.

        Attributes:
            auth_config_template (google.cloud.apihub_v1.types.Plugin.ConfigTemplate.AuthConfigTemplate):
                Optional. The authentication template for the
                plugin.
            additional_config_template (MutableSequence[google.cloud.apihub_v1.types.ConfigVariableTemplate]):
                Optional. The list of additional
                configuration variables for the plugin's
                configuration.
        """

        class AuthConfigTemplate(proto.Message):
            r"""AuthConfigTemplate represents the authentication template for
            a plugin.

            Attributes:
                supported_auth_types (MutableSequence[google.cloud.apihub_v1.types.AuthType]):
                    Required. The list of authentication types
                    supported by the plugin.
                service_account (google.cloud.apihub_v1.types.GoogleServiceAccountConfig):
                    Optional. The service account of the plugin
                    hosting service. This service account should be
                    granted the required permissions on the Auth
                    Config parameters provided while creating the
                    plugin instances corresponding to this plugin.

                    For example, if the plugin instance auth config
                    requires a secret manager secret, the service
                    account should be granted the
                    secretmanager.versions.access permission on the
                    corresponding secret, if the plugin instance
                    auth config contains a service account, the
                    service account should be granted the
                    iam.serviceAccounts.getAccessToken permission on
                    the corresponding service account.
            """

            supported_auth_types: MutableSequence[common_fields.AuthType] = (
                proto.RepeatedField(
                    proto.ENUM,
                    number=1,
                    enum=common_fields.AuthType,
                )
            )
            service_account: common_fields.GoogleServiceAccountConfig = proto.Field(
                proto.MESSAGE,
                number=2,
                message=common_fields.GoogleServiceAccountConfig,
            )

        auth_config_template: "Plugin.ConfigTemplate.AuthConfigTemplate" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Plugin.ConfigTemplate.AuthConfigTemplate",
        )
        additional_config_template: MutableSequence[
            common_fields.ConfigVariableTemplate
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=common_fields.ConfigVariableTemplate,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: common_fields.AttributeValues = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.AttributeValues,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    ownership_type: OwnershipType = proto.Field(
        proto.ENUM,
        number=6,
        enum=OwnershipType,
    )
    hosting_service: HostingService = proto.Field(
        proto.MESSAGE,
        number=7,
        message=HostingService,
    )
    actions_config: MutableSequence["PluginActionConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="PluginActionConfig",
    )
    documentation: common_fields.Documentation = proto.Field(
        proto.MESSAGE,
        number=9,
        message=common_fields.Documentation,
    )
    plugin_category: common_fields.PluginCategory = proto.Field(
        proto.ENUM,
        number=11,
        enum=common_fields.PluginCategory,
    )
    config_template: ConfigTemplate = proto.Field(
        proto.MESSAGE,
        number=12,
        message=ConfigTemplate,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    gateway_type: "GatewayType" = proto.Field(
        proto.ENUM,
        number=15,
        enum="GatewayType",
    )


class PluginActionConfig(proto.Message):
    r"""PluginActionConfig represents the configuration of an action
    supported by a plugin.

    Attributes:
        id (str):
            Required. The id of the action.
        display_name (str):
            Required. The display name of the action.
        description (str):
            Required. The description of the operation
            performed by the action.
        trigger_mode (google.cloud.apihub_v1.types.PluginActionConfig.TriggerMode):
            Required. The trigger mode supported by the
            action.
    """

    class TriggerMode(proto.Enum):
        r"""Execution mode of the action.

        Values:
            TRIGGER_MODE_UNSPECIFIED (0):
                Default unspecified mode.
            API_HUB_ON_DEMAND_TRIGGER (1):
                This action can be executed by invoking
                [ExecutePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.ExecutePluginInstanceAction]
                API with the given action id. To support this, the plugin
                hosting service should handle this action id as part of
                execute call.
            API_HUB_SCHEDULE_TRIGGER (2):
                This action will be executed on schedule by invoking
                [ExecutePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.ExecutePluginInstanceAction]
                API with the given action id. To set the schedule, the user
                can provide the cron expression in the
                [PluginAction][PluginAction.schedule_cron_expression] field
                for a given plugin instance. To support this, the plugin
                hosting service should handle this action id as part of
                execute call. Note, on demand execution will be supported by
                default in this trigger mode.
            NON_API_HUB_MANAGED (3):
                The execution of this plugin is not handled
                by API hub. In this case, the plugin hosting
                service need not handle this action id as part
                of the execute call.
        """

        TRIGGER_MODE_UNSPECIFIED = 0
        API_HUB_ON_DEMAND_TRIGGER = 1
        API_HUB_SCHEDULE_TRIGGER = 2
        NON_API_HUB_MANAGED = 3

    id: str = proto.Field(
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
    trigger_mode: TriggerMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=TriggerMode,
    )


class GetPluginRequest(proto.Message):
    r"""The [GetPlugin][google.cloud.apihub.v1.ApiHubPlugin.GetPlugin]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin to retrieve. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EnablePluginRequest(proto.Message):
    r"""The [EnablePlugin][google.cloud.apihub.v1.ApiHubPlugin.EnablePlugin]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin to enable. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DisablePluginRequest(proto.Message):
    r"""The
    [DisablePlugin][google.cloud.apihub.v1.ApiHubPlugin.DisablePlugin]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin to disable. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PluginInstanceAction(proto.Message):
    r"""PluginInstanceAction represents an action which can be
    executed in the plugin instance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hub_instance_action (google.cloud.apihub_v1.types.ExecutionStatus):
            Optional. The execution information for the
            plugin instance action done corresponding to an
            API hub instance.

            This field is a member of `oneof`_ ``action_status``.
        action_id (str):
            Required. This should map to one of the [action
            id][google.cloud.apihub.v1.PluginActionConfig.id] specified
            in
            [actions_config][google.cloud.apihub.v1.Plugin.actions_config]
            in the plugin.
        state (google.cloud.apihub_v1.types.PluginInstanceAction.State):
            Output only. The current state of the plugin
            action in the plugin instance.
        schedule_cron_expression (str):
            Optional. The schedule for this plugin instance action. This
            can only be set if the plugin supports
            API_HUB_SCHEDULE_TRIGGER mode for this action.
        curation_config (google.cloud.apihub_v1.types.CurationConfig):
            Optional. This configuration should be
            provided if the plugin action is publishing data
            to API hub curate layer.
        schedule_time_zone (str):
            Optional. The time zone for the schedule cron
            expression. If not provided, UTC will be used.
        service_account (str):
            Optional. The service account used to publish
            data. Note, the service account will only be
            accepted for non GCP plugins like OPDK.
        resource_config (google.cloud.apihub_v1.types.PluginInstanceAction.ResourceConfig):
            Output only. The configuration of resources
            created for a given plugin instance action. Note
            these will be returned only in case of Non-GCP
            plugins like OPDK.
    """

    class State(proto.Enum):
        r"""State represents the state of the plugin instance action.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified state.
            ENABLED (1):
                The action is enabled in the plugin instance
                i.e., executions can be triggered for this
                action.
            DISABLED (2):
                The action is disabled in the plugin instance
                i.e., no executions can be triggered for this
                action. This state indicates that the user
                explicitly disabled the instance, and no further
                action is needed unless the user wants to
                re-enable it.
            ENABLING (3):
                The action in the plugin instance is being
                enabled.
            DISABLING (4):
                The action in the plugin instance is being
                disabled.
            ERROR (5):
                The ERROR state can come while enabling/disabling plugin
                instance action. Users can retrigger enable, disable via
                [EnablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.EnablePluginInstanceAction]
                and
                [DisablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.DisablePluginInstanceAction]
                to restore the action back to enabled/disabled state. Note
                enable/disable on actions can only be triggered if plugin
                instance is in Active state.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        ENABLING = 3
        DISABLING = 4
        ERROR = 5

    class ResourceConfig(proto.Message):
        r"""The configuration of resources created for a given plugin
        instance action.

        Attributes:
            action_type (google.cloud.apihub_v1.types.ActionType):
                Output only. The type of the action.
            pubsub_topic (str):
                Output only. The pubsub topic to publish the
                data to. Format is
                projects/{project}/topics/{topic}
        """

        action_type: "ActionType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ActionType",
        )
        pubsub_topic: str = proto.Field(
            proto.STRING,
            number=2,
        )

    hub_instance_action: "ExecutionStatus" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action_status",
        message="ExecutionStatus",
    )
    action_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    schedule_cron_expression: str = proto.Field(
        proto.STRING,
        number=4,
    )
    curation_config: "CurationConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CurationConfig",
    )
    schedule_time_zone: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=8,
    )
    resource_config: ResourceConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=ResourceConfig,
    )


class PluginInstance(proto.Message):
    r"""Represents a plugin instance resource in the API Hub.
    A PluginInstance is a specific instance of a hub plugin with its
    own configuration, state, and execution details.

    Attributes:
        name (str):
            Identifier. The unique name of the plugin instance resource.
            Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``
        display_name (str):
            Required. The display name for this plugin
            instance. Max length is 255 characters.
        auth_config (google.cloud.apihub_v1.types.AuthConfig):
            Optional. The authentication information for
            this plugin instance.
        additional_config (MutableMapping[str, google.cloud.apihub_v1.types.ConfigVariable]):
            Optional. The additional information for this plugin
            instance corresponding to the additional config template of
            the plugin. This information will be sent to plugin hosting
            service on each call to plugin hosted service. The key will
            be the config_variable_template.display_name to uniquely
            identify the config variable.
        state (google.cloud.apihub_v1.types.PluginInstance.State):
            Output only. The current state of the plugin
            instance (e.g., enabled, disabled,
            provisioning).
        error_message (str):
            Output only. Error message describing the
            failure, if any, during Create, Delete or
            ApplyConfig operation corresponding to the
            plugin instance.This field will only be
            populated if the plugin instance is in the ERROR
            or FAILED state.
        actions (MutableSequence[google.cloud.apihub_v1.types.PluginInstanceAction]):
            Required. The action status for the plugin
            instance.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            plugin instance was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            plugin instance was last updated.
        source_project_id (str):
            Optional. The source project id of the plugin
            instance. This will be the id of runtime project
            in case of gcp based plugins and org id in case
            of non gcp based plugins. This field will be a
            required field for Google provided on-ramp
            plugins.
    """

    class State(proto.Enum):
        r"""State represents the state of the plugin instance.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified state.
            CREATING (1):
                The plugin instance is being created.
            ACTIVE (2):
                The plugin instance is active and ready for
                executions. This is the only state where
                executions can run on the plugin instance.
            APPLYING_CONFIG (3):
                The updated config that contains
                [additional_config][google.cloud.apihub.v1.PluginInstance.additional_config]
                and
                [auth_config][google.cloud.apihub.v1.PluginInstance.auth_config]
                is being applied.
            ERROR (4):
                The ERROR state can come while applying config. Users can
                retrigger
                [ApplyPluginInstanceConfig][google.cloud.apihub.v1.ApiHubPlugin.ApplyPluginInstanceConfig]
                to restore the plugin instance back to active state. Note,
                In case the ERROR state happens while applying config
                (auth_config, additional_config), the plugin instance will
                reflect the config which was trying to be applied while
                error happened. In order to overwrite, trigger ApplyConfig
                with a new config.
            FAILED (5):
                The plugin instance is in a failed state.
                This indicates that an unrecoverable error
                occurred during a previous operation (Create,
                Delete).
            DELETING (6):
                The plugin instance is being deleted. Delete
                is only possible if there is no other operation
                running on the plugin instance and plugin
                instance action.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        APPLYING_CONFIG = 3
        ERROR = 4
        FAILED = 5
        DELETING = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    auth_config: common_fields.AuthConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.AuthConfig,
    )
    additional_config: MutableMapping[str, common_fields.ConfigVariable] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=4,
            message=common_fields.ConfigVariable,
        )
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    actions: MutableSequence["PluginInstanceAction"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="PluginInstanceAction",
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
    source_project_id: str = proto.Field(
        proto.STRING,
        number=11,
    )


class CurationConfig(proto.Message):
    r"""The curation information for this plugin instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        custom_curation (google.cloud.apihub_v1.types.CurationConfig.CustomCuration):
            Optional. Custom curation information for
            this plugin instance.

            This field is a member of `oneof`_ ``curation_config``.
        curation_type (google.cloud.apihub_v1.types.CurationType):
            Required. The curation type for this plugin
            instance.
    """

    class CustomCuration(proto.Message):
        r"""Custom curation information for this plugin instance.

        Attributes:
            curation (str):
                Required. The unique name of the curation resource. This
                will be the name of the curation resource in the format:
                ``projects/{project}/locations/{location}/curations/{curation}``
        """

        curation: str = proto.Field(
            proto.STRING,
            number=1,
        )

    custom_curation: CustomCuration = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="curation_config",
        message=CustomCuration,
    )
    curation_type: "CurationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="CurationType",
    )


class ExecutionStatus(proto.Message):
    r"""The execution status for the plugin instance.

    Attributes:
        current_execution_state (google.cloud.apihub_v1.types.ExecutionStatus.CurrentExecutionState):
            Output only. The current state of the
            execution.
        last_execution (google.cloud.apihub_v1.types.ExecutionStatus.LastExecution):
            Output only. The last execution of the plugin
            instance.
    """

    class CurrentExecutionState(proto.Enum):
        r"""Enum for the current state of the execution.

        Values:
            CURRENT_EXECUTION_STATE_UNSPECIFIED (0):
                Default unspecified execution state.
            RUNNING (1):
                The plugin instance is executing.
            NOT_RUNNING (2):
                The plugin instance is not running an
                execution.
        """

        CURRENT_EXECUTION_STATE_UNSPECIFIED = 0
        RUNNING = 1
        NOT_RUNNING = 2

    class LastExecution(proto.Message):
        r"""The result of the last execution of the plugin instance.

        Attributes:
            result (google.cloud.apihub_v1.types.ExecutionStatus.LastExecution.Result):
                Output only. The result of the last execution
                of the plugin instance.
            error_message (str):
                Output only. Error message describing the
                failure, if any, during the last execution.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The last execution start time of
                the plugin instance.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The last execution end time of
                the plugin instance.
        """

        class Result(proto.Enum):
            r"""Enum for the result of the last execution of the plugin
            instance.

            Values:
                RESULT_UNSPECIFIED (0):
                    Default unspecified execution result.
                SUCCEEDED (1):
                    The plugin instance executed successfully.
                FAILED (2):
                    The plugin instance execution failed.
            """

            RESULT_UNSPECIFIED = 0
            SUCCEEDED = 1
            FAILED = 2

        result: "ExecutionStatus.LastExecution.Result" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ExecutionStatus.LastExecution.Result",
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    current_execution_state: CurrentExecutionState = proto.Field(
        proto.ENUM,
        number=1,
        enum=CurrentExecutionState,
    )
    last_execution: LastExecution = proto.Field(
        proto.MESSAGE,
        number=2,
        message=LastExecution,
    )


class CreatePluginRequest(proto.Message):
    r"""The [CreatePlugin][google.cloud.apihub.v1.ApiHubPlugin.CreatePlugin]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource where this plugin will be
            created. Format:
            ``projects/{project}/locations/{location}``.
        plugin_id (str):
            Optional. The ID to use for the Plugin resource, which will
            become the final component of the Plugin's resource name.
            This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              Plugin resource in the API hub instance.
            - If not provided, a system generated id will be used.

            This value should be 4-63 characters, overall resource name
            which will be of format
            ``projects/{project}/locations/{location}/plugins/{plugin}``,
            its length is limited to 1000 characters and valid
            characters are /[a-z][A-Z][0-9]-\_/.
        plugin (google.cloud.apihub_v1.types.Plugin):
            Required. The plugin to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    plugin_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    plugin: "Plugin" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Plugin",
    )


class DeletePluginRequest(proto.Message):
    r"""The [DeletePlugin][ApiHub.DeletePlugin] method's request.

    Attributes:
        name (str):
            Required. The name of the Plugin resource to delete. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPluginsRequest(proto.Message):
    r"""The [ListPlugins][google.cloud.apihub.v1.ApiHubPlugin.ListPlugins]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource where this plugin will be
            created. Format:
            ``projects/{project}/locations/{location}``.
        filter (str):
            Optional. An expression that filters the list of plugins.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. The comparison operator must be one of: ``<``, ``>``
            or ``=``. Filters are not case sensitive.

            The following fields in the ``Plugins`` are eligible for
            filtering:

            - ``plugin_category`` - The category of the Plugin. Allowed
              comparison operators: ``=``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API. Here are a few examples:

            - ``plugin_category = ON_RAMP`` - The plugin is of category
              on ramp.
        page_size (int):
            Optional. The maximum number of hub plugins
            to return. The service may return fewer than
            this value. If unspecified, at most 50 hub
            plugins will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPlugins`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListPlugins`` must match the call that
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


class ListPluginsResponse(proto.Message):
    r"""The [ListPlugins][google.cloud.apihub.v1.ApiHubPlugin.ListPlugins]
    method's response.

    Attributes:
        plugins (MutableSequence[google.cloud.apihub_v1.types.Plugin]):
            The plugins from the specified parent
            resource.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    plugins: MutableSequence["Plugin"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Plugin",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreatePluginInstanceRequest(proto.Message):
    r"""The
    [CreatePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.CreatePluginInstance]
    method's request.

    Attributes:
        parent (str):
            Required. The parent of the plugin instance resource.
            Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``
        plugin_instance_id (str):
            Optional. The ID to use for the plugin instance, which will
            become the final component of the plugin instance's resource
            name. This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              plugin instance in the plugin resource.
            - If not provided, a system generated id will be used.

            This value should be 4-63 characters, and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        plugin_instance (google.cloud.apihub_v1.types.PluginInstance):
            Required. The plugin instance to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    plugin_instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    plugin_instance: "PluginInstance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PluginInstance",
    )


class ExecutePluginInstanceActionRequest(proto.Message):
    r"""The
    [ExecutePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.ExecutePluginInstanceAction]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin instance to execute.
            Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``
        action_execution_detail (google.cloud.apihub_v1.types.ActionExecutionDetail):
            Required. The execution details for the
            action to execute.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_execution_detail: "ActionExecutionDetail" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ActionExecutionDetail",
    )


class ActionExecutionDetail(proto.Message):
    r"""The details for the action to execute.

    Attributes:
        action_id (str):
            Required. The action id of the plugin to
            execute.
    """

    action_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExecutePluginInstanceActionResponse(proto.Message):
    r"""The
    [ExecutePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.ExecutePluginInstanceAction]
    method's response.

    """


class GetPluginInstanceRequest(proto.Message):
    r"""The
    [GetPluginInstance][google.cloud.apihub.v1.ApiHubPlugin.GetPluginInstance]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin instance to retrieve.
            Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPluginInstancesRequest(proto.Message):
    r"""The
    [ListPluginInstances][google.cloud.apihub.v1.ApiHubPlugin.ListPluginInstances]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource where this plugin will be
            created. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}``.
            To list plugin instances for multiple plugins, use the -
            character instead of the plugin ID.
        filter (str):
            Optional. An expression that filters the list of plugin
            instances.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. The comparison operator must be one of: ``<``, ``>``
            or ``=``. Filters are not case sensitive.

            The following fields in the ``PluginInstances`` are eligible
            for filtering:

            - ``state`` - The state of the Plugin Instance. Allowed
              comparison operators: ``=``.

            A filter function is also supported in the filter string.
            The filter function is ``id(name)``. The ``id(name)``
            function returns the id of the resource name. For example,
            ``id(name) = \"plugin-instance-1\"`` is equivalent to
            ``name = \"projects/test-project-id/locations/test-location-id/plugins/plugin-1/instances/plugin-instance-1\"``
            provided the parent is
            ``projects/test-project-id/locations/test-location-id/plugins/plugin-1``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API. Here are a few examples:

            - ``state = ENABLED`` - The plugin instance is in enabled
              state.
        page_size (int):
            Optional. The maximum number of hub plugins
            to return. The service may return fewer than
            this value. If unspecified, at most 50 hub
            plugins will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPluginInstances`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListPluginInstances`` must match the call that provided
            the page token.
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


class ListPluginInstancesResponse(proto.Message):
    r"""The
    [ListPluginInstances][google.cloud.apihub.v1.ApiHubPlugin.ListPluginInstances]
    method's response.

    Attributes:
        plugin_instances (MutableSequence[google.cloud.apihub_v1.types.PluginInstance]):
            The plugin instances from the specified
            parent resource.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    plugin_instances: MutableSequence["PluginInstance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PluginInstance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EnablePluginInstanceActionRequest(proto.Message):
    r"""The
    [EnablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.EnablePluginInstanceAction]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin instance to enable. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``
        action_id (str):
            Required. The action id to enable.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EnablePluginInstanceActionResponse(proto.Message):
    r"""The
    [EnablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.EnablePluginInstanceAction]
    method's response.

    """


class DisablePluginInstanceActionRequest(proto.Message):
    r"""The
    [DisablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.DisablePluginInstanceAction]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin instance to disable.
            Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``
        action_id (str):
            Required. The action id to disable.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DisablePluginInstanceActionResponse(proto.Message):
    r"""The
    [DisablePluginInstanceAction][google.cloud.apihub.v1.ApiHubPlugin.DisablePluginInstanceAction]
    method's response.

    """


class UpdatePluginInstanceRequest(proto.Message):
    r"""The
    [UpdatePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.UpdatePluginInstance]
    method's request.

    Attributes:
        plugin_instance (google.cloud.apihub_v1.types.PluginInstance):
            Required. The plugin instance to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    plugin_instance: "PluginInstance" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PluginInstance",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeletePluginInstanceRequest(proto.Message):
    r"""The
    [DeletePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.DeletePluginInstance]
    method's request.

    Attributes:
        name (str):
            Required. The name of the plugin instance to delete. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
