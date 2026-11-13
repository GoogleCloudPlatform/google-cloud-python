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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.discoveryengine_v1.types import common, data_connector

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1",
    manifest={
        "ModelInfoView",
        "WidgetConfig",
    },
)


class ModelInfoView(proto.Enum):
    r"""Selects which "view" of the model selector configuration the backend
    computes for ``WidgetConfig.UiSettings.ModelConfigInfo``.

    The end-user views (``END_USER_WEB``, ``END_USER_MOBILE``) return
    the user-facing model selector for their respective surface; the
    ``ADMIN`` view returns the set surfaced on the Cloud Console admin
    "Feature Control" page, with
    ``ModelConfigInfo.ResolvedModel.admin_view`` populated on each
    entry.

    Values:
        MODEL_INFO_VIEW_UNSPECIFIED (0):
            Not specified.
        END_USER_WEB (1):
            The end-user web model selector view.
        ADMIN (2):
            The Cloud Console admin "Feature Control" view that displays
            model toggles. Returns admin-surfaced models with
            ``ResolvedModel.admin_view`` populated.
        END_USER_MOBILE (3):
            The end-user model selector view for the
            Gemini Enterprise mobile app. Returns only
            mobile-surfaced models, with the mobile default
            selected. Set explicitly by the mobile client.
    """

    MODEL_INFO_VIEW_UNSPECIFIED = 0
    END_USER_WEB = 1
    ADMIN = 2
    END_USER_MOBILE = 3


class WidgetConfig(proto.Message):
    r"""WidgetConfig captures configs at the Widget level.

    Attributes:
        name (str):
            Immutable. The full resource name of the widget config.
            Format:
            ``projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/widgetConfigs/{widget_config_id}``.

            This field must be a UTF-8 encoded string with a length
            limit of 1024 characters.
        display_name (str):
            Required. The human readable widget config display name.
            Used in Discovery UI.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig]
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig]
            was updated.
        data_store_type (google.cloud.discoveryengine_v1.types.WidgetConfig.DataStoreType):
            Output only. The type of the parent data
            store.
        config_id (str):
            Output only. Unique obfuscated identifier of a
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig].
        solution_type (google.cloud.discoveryengine_v1.types.SolutionType):
            Required. Immutable. Specifies the solution
            type that this WidgetConfig can be used for.
        industry_vertical (google.cloud.discoveryengine_v1.types.IndustryVertical):
            Output only. The industry vertical that the WidgetConfig
            registers. The WidgetConfig industry vertical is based on
            the associated
            [Engine][google.cloud.discoveryengine.v1.Engine].
        llm_enabled (bool):
            Output only. Whether LLM is enabled in the
            corresponding data store.
        enable_result_score (bool):
            Whether to show the result score.
        minimum_data_term_accepted (bool):
            Output only. Whether the customer accepted
            data use terms.
        collection_components (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.CollectionComponent]):
            Output only. Collection components that lists all
            collections and child data stores associated with the widget
            config, those data sources can be used for filtering in
            widget service APIs, users can return results that from
            selected data sources.

            For SaaS / Business engines, when ``LookupWidgetConfig`` is
            called with ``view = WITH_AVAILABLE_CONNECTORS``, this list
            is additionally augmented with synthetic placeholder entries
            for connectors the caller may attach but has not yet
            attached (see ``CollectionComponent`` for the placeholder
            contract). The frontend can therefore render a unified list
            of already-attached and available-to-attach sources by
            iterating this single field. For Enterprise engines and for
            the default ``view``, only already-attached connectors are
            returned (today's behavior).
        ui_settings (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings):
            Describes general widget search settings as
            seen in cloud console widget configuration page.
            Replaces top deprecated top level properties.
        access_settings (google.cloud.discoveryengine_v1.types.WidgetConfig.AccessSettings):
            Will be used for all widget access settings
            seen in cloud console integration page. Replaces
            top deprecated top level properties.
        ui_branding (google.cloud.discoveryengine_v1.types.WidgetConfig.UiBrandingSettings):
            Describes search widget UI branding settings,
            such as the widget title, logo, favicons, and
            colors.
        homepage_setting (google.cloud.discoveryengine_v1.types.WidgetConfig.HomepageSetting):
            Optional. Describes the homepage settings of
            the widget.
        assistant_settings (google.cloud.discoveryengine_v1.types.WidgetConfig.AssistantSettings):
            Optional. Output only. Describes the
            assistant settings of the widget.
        customer_provided_config (google.cloud.discoveryengine_v1.types.WidgetConfig.CustomerProvidedConfig):
            Optional. Output only. Describes the customer
            related configurations, currently only used for
            government customers. This field cannot be
            modified after project onboarding.
        enable_private_knowledge_graph (bool):
            Optional. Output only. Whether to enable
            private knowledge graph.
        gemini_bundle (bool):
            Output only. Whether the subscription is
            gemini bundle or not.
        batch_auth_statuses (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.BatchAuthStatus]):
            Output only. The batch authorization statuses
            for the widget's connectors.
        nodes (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.Node]):
            Output only. The nodes associated with the
            Widget Config.
    """

    class DataStoreType(proto.Enum):
        r"""The type of the widget's parent data store.

        Values:
            DATA_STORE_TYPE_UNSPECIFIED (0):
                Unspecified data store type.
            SITE_SEARCH (1):
                The parent data store contains a site search
                engine.
            STRUCTURED (2):
                The parent data store contains a search
                engine for structured data.
            UNSTRUCTURED (3):
                The parent data store contains a search
                engine for unstructured data.
            BLENDED (4):
                The parent data store is served for blended
                search with multiple data stores.
        """

        DATA_STORE_TYPE_UNSPECIFIED = 0
        SITE_SEARCH = 1
        STRUCTURED = 2
        UNSTRUCTURED = 3
        BLENDED = 4

    class ResultDisplayType(proto.Enum):
        r"""The type of result to display in the ucs widget.

        Values:
            RESULT_DISPLAY_TYPE_UNSPECIFIED (0):
                Unspecified display type (default to showing
                snippet).
            SNIPPET (1):
                Display results from the snippet field.
            EXTRACTIVE_ANSWER (2):
                Display results from extractive answers
                field.
        """

        RESULT_DISPLAY_TYPE_UNSPECIFIED = 0
        SNIPPET = 1
        EXTRACTIVE_ANSWER = 2

    class UIComponentField(proto.Message):
        r"""Facet field that maps to a UI Component.

        Attributes:
            field (str):
                Required. Registered field name. The format is
                ``field.abc``.
            device_visibility (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.UIComponentField.DeviceVisibility]):
                The field visibility on different types of
                devices.
            display_template (str):
                The template to customize how the field is
                displayed. An example value would be a string
                that looks like: "Price: {value}".
        """

        class DeviceVisibility(proto.Enum):
            r"""The visibility of the field on different type of devices.

            Values:
                DEVICE_VISIBILITY_UNSPECIFIED (0):
                    Default value when not specified. Server returns
                    INVALID_ARGUMENT if used in requests.
                MOBILE (1):
                    The UI component is visible on Mobile
                    devices.
                DESKTOP (2):
                    The UI component is visible on Browser-based
                    client.
            """

            DEVICE_VISIBILITY_UNSPECIFIED = 0
            MOBILE = 1
            DESKTOP = 2

        field: str = proto.Field(
            proto.STRING,
            number=1,
        )
        device_visibility: MutableSequence[
            "WidgetConfig.UIComponentField.DeviceVisibility"
        ] = proto.RepeatedField(
            proto.ENUM,
            number=2,
            enum="WidgetConfig.UIComponentField.DeviceVisibility",
        )
        display_template: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class FacetField(proto.Message):
        r"""Facet fields that store the mapping of fields to end user
        widget appearance.

        Attributes:
            field (str):
                Required. Registered field name. The format is
                ``field.abc``.
            display_name (str):
                Optional. The field name that end users will
                see.
        """

        field: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class DataStoreUiConfig(proto.Message):
        r"""UI component configuration for data store.

        Attributes:
            name (str):
                The name of the data store. It should be data store resource
                name Format:
                ``projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}``.
                For APIs under
                [WidgetService][google.cloud.discoveryengine.v1.WidgetService],
                such as
                [WidgetService.LookupWidgetConfig][google.cloud.discoveryengine.v1.WidgetService.LookupWidgetConfig],
                the project number and location part is erased in this
                field.
            id (str):
                Output only. the identifier of the data store, used for
                widget service. For now it refers to data_store_id, in the
                future we will migrate the field to encrypted data store
                name UUID.
            facet_field (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.FacetField]):
                Facet fields that store the mapping of fields
                to end user widget appearance.
            fields_ui_components_map (MutableMapping[str, google.cloud.discoveryengine_v1.types.WidgetConfig.UIComponentField]):
                The key is the UI component. Mock. Currently supported
                ``title``, ``thumbnail``, ``url``, ``custom1``, ``custom2``,
                ``custom3``.

                The value is the name of the field along with its device
                visibility.

                The 3 custom fields are optional and can be added or
                removed. ``title``, ``thumbnail``, ``url`` are required UI
                components that cannot be removed.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        facet_field: MutableSequence["WidgetConfig.FacetField"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="WidgetConfig.FacetField",
        )
        fields_ui_components_map: MutableMapping[
            str, "WidgetConfig.UIComponentField"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=4,
            message="WidgetConfig.UIComponentField",
        )

    class DataStoreComponent(proto.Message):
        r"""Read-only data store component that contains data stores fields that
        may be used for filtering, it's the child of
        ``CollectionComponent``.

        Attributes:
            name (str):
                The name of the data store. It should be data store resource
                name Format:
                ``projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}``.
                For APIs under
                [WidgetService][google.cloud.discoveryengine.v1.WidgetService],
                such as
                [WidgetService.LookupWidgetConfig][google.cloud.discoveryengine.v1.WidgetService.LookupWidgetConfig],
                the project number and location part is erased in this
                field.
            id (str):
                Output only. the identifier of the data store, used for
                widget service. For now it refers to data_store_id, in the
                future we will migrate the field to encrypted data store
                name UUID.
            display_name (str):
                The display name of the data store.
            entity_name (str):
                The name of the entity, retrieved from
                ``Collection.data_connector.entities.entityName``.
            data_store_config_type (google.cloud.discoveryengine_v1.types.WidgetConfig.DataStoreComponent.DataStoreConfigType):
                Output only. The type of the data store
                config.
        """

        class DataStoreConfigType(proto.Enum):
            r"""The type of the data store config.

            Values:
                DATA_STORE_CONFIG_TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ALLOW_DB_CONFIG (1):
                    The data store is connected to AlloyDB
                THIRD_PARTY_OAUTH_CONFIG (2):
                    The data store is a connected to a third
                    party data source.
                NOTEBOOKLM_CONFIG (3):
                    The data store is a connected to NotebookLM
                    Enterprise.
            """

            DATA_STORE_CONFIG_TYPE_UNSPECIFIED = 0
            ALLOW_DB_CONFIG = 1
            THIRD_PARTY_OAUTH_CONFIG = 2
            NOTEBOOKLM_CONFIG = 3

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        entity_name: str = proto.Field(
            proto.STRING,
            number=4,
        )
        data_store_config_type: "WidgetConfig.DataStoreComponent.DataStoreConfigType" = proto.Field(
            proto.ENUM,
            number=8,
            enum="WidgetConfig.DataStoreComponent.DataStoreConfigType",
        )

    class ConnectorAuthState(proto.Message):
        r"""Read-only connector in CollectionComponent auth state.

        Attributes:
            auth_state (google.cloud.discoveryengine_v1.types.WidgetConfig.ConnectorAuthState.AuthState):
                Output only. The authorization state of the
                data connector.
            authorization_uri (str):
                Output only. The authorization uri for the data connector.

                For synthetic placeholder ``CollectionComponent`` entries
                (returned by ``LookupWidgetConfig`` with
                ``view = WITH_AVAILABLE_CONNECTORS`` on SaaS / Business
                engines), this field is left empty. The widget should call
                ``WidgetService.WidgetBuildAuthorizationUrl`` on the user's
                "Connect" click to obtain a freshly-built authorization URL.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The authorization state update
                timestamp.
        """

        class AuthState(proto.Enum):
            r"""The authorization state of the data connector.

            Values:
                AUTH_STATE_UNSPECIFIED (0):
                    Default value. Also returned for synthetic placeholder
                    ``CollectionComponent`` entries surfaced by
                    ``LookupWidgetConfig`` with
                    ``view = WITH_AVAILABLE_CONNECTORS`` (SaaS / Business only)
                    — those entries represent connectors the caller may attach
                    but has not yet attached.
                AUTHORIZED (1):
                    The user has authorized the data connector.
                EXPIRED (2):
                    The user authorization for the data connector
                    has expired.
                ACTIONS_DISABLED (3):
                    The user can still make search requests but
                    actions need to be enabled.
                NO_AUTH (4):
                    The data connector does not require any
                    authorization. Also used for placeholder entries
                    whose underlying connector does not require user
                    OAuth.
            """

            AUTH_STATE_UNSPECIFIED = 0
            AUTHORIZED = 1
            EXPIRED = 2
            ACTIONS_DISABLED = 3
            NO_AUTH = 4

        auth_state: "WidgetConfig.ConnectorAuthState.AuthState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="WidgetConfig.ConnectorAuthState.AuthState",
        )
        authorization_uri: str = proto.Field(
            proto.STRING,
            number=3,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    class BatchAuthStatus(proto.Message):
        r"""Describes the batch authorization status for a
        batch_authorization_group.

        Attributes:
            placeholder (str):
                Output only. It is the batch authorization group placeholder
                full resource name. This is not a real data connector
                resource. E.g.
                projects/{project}/locations/{location}/collections/oauth_placeholder_google_workspace/dataStores/dataConnector.
            batch_authorization_group (str):
                Output only. The batch authorization group
                the placeholder belongs to.
            connector_auth_state (google.cloud.discoveryengine_v1.types.WidgetConfig.ConnectorAuthState):
                Output only. The current authorization state
                for this connector.
        """

        placeholder: str = proto.Field(
            proto.STRING,
            number=1,
        )
        batch_authorization_group: str = proto.Field(
            proto.STRING,
            number=2,
        )
        connector_auth_state: "WidgetConfig.ConnectorAuthState" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="WidgetConfig.ConnectorAuthState",
        )

    class CollectionComponent(proto.Message):
        r"""Read-only collection component that contains data store collections
        fields that may be used for filtering.

        For SaaS / Business engines, when ``LookupWidgetConfig`` is called
        with ``view = WITH_AVAILABLE_CONNECTORS``, instances of this message
        are also used to represent synthetic placeholder entries for
        connectors the caller may attach but has not yet attached.
        Placeholder entries have
        ``connector_auth_state.auth_state == AUTH_STATE_UNSPECIFIED`` (or
        ``NO_AUTH``), an empty ``connector_auth_state.authorization_uri``
        (the widget calls ``WidgetBuildAuthorizationUrl`` on the user's
        "Connect" click), and synthetic placeholder values in ``name`` /
        ``id`` (see field comments). Fields that only make sense for
        materialized connectors (``data_store_components``, ``tenant``,
        ``action_connector``) are left unset for placeholder entries.

        Attributes:
            name (str):
                The name of the collection. It should be collection resource
                name. Format:
                ``projects/{project}/locations/{location}/collections/{collection_id}``.
                For APIs under
                [WidgetService][google.cloud.discoveryengine.v1.WidgetService],
                such as
                [WidgetService.LookupWidgetConfig][google.cloud.discoveryengine.v1.WidgetService.LookupWidgetConfig],
                the project number and location part is erased in this
                field.

                For synthetic placeholder entries (see message-level
                comment) this carries a synthetic placeholder collection id
                that does not correspond to a real collection. Callers must
                not attempt to resolve / GET this resource until the user
                authorizes the connector.
            id (str):
                Output only. the identifier of the collection, used for
                widget service. For now it refers to collection_id, in the
                future we will migrate the field to encrypted collection
                name UUID.

                For synthetic placeholder entries (see message-level
                comment) this is a synthetic placeholder id, not a real
                collection_id.
            display_name (str):
                The display name of the collection.
            data_store_components (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.DataStoreComponent]):
                For the data store collection, list of the
                children data stores.
            data_source (str):
                The name of the data source, retrieved from
                ``Collection.data_connector.data_source``.
            data_source_version (float):
                Output only. The version of the connector definition backing
                this collection, mirroring
                ``DataConnector.data_source_version``.
            data_source_display_name (str):
                Output only. The display name of the data
                source.
            data_source_end_user_display_name (str):
                Output only. The end-user-facing display name of the data
                source, sourced from
                ``ConnectorSource.end_user_display_name``. When unset,
                clients fall back to ``data_source_display_name``.
            connector_icon_link (str):
                Output only. The icon link of the connector
                source.
            connector_auth_state (google.cloud.discoveryengine_v1.types.WidgetConfig.ConnectorAuthState):
                Output only. The auth uri of the connector
                source.
            metadata (google.cloud.discoveryengine_v1.types.DataConnector.ConnectorMetadata):
                Output only. User-facing connector metadata (``title``,
                ``description``, ``short_description``, ``author``,
                ``note``), retrieved from the registry
                ``ConnectorSource.metadata`` (joined by data source). Shown
                on the connector detail page.
            is_first_party (bool):
                Output only. Whether this is a first-party
                (Google-owned) connector, as opposed to a
                third-party connector.
            tag (str):
                Output only. The version-independent label of the connector
                backing this collection, mirroring ``DataConnector.tag``.
                Unlike the version-pinned data store id it survives a
                connector version upgrade, so an upgraded connector keeps
                the same tag.

                Not a unique key. As ``DataConnector.tag`` documents,
                several connectors may share a tag under the same (project,
                location, collection, data_source), and tag-based lookup
                resolves to the one with the greatest create_time. Clients
                must not treat this as a connector identifier.

                Empty when the connector was created before the tag-write
                launch, and for synthetic placeholder entries, which have no
                underlying ``DataConnector``. Populated only when
                ``ConnectorsFeature.enable_connector_tag`` is on.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        data_store_components: MutableSequence["WidgetConfig.DataStoreComponent"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="WidgetConfig.DataStoreComponent",
            )
        )
        data_source: str = proto.Field(
            proto.STRING,
            number=5,
        )
        data_source_version: float = proto.Field(
            proto.DOUBLE,
            number=16,
        )
        data_source_display_name: str = proto.Field(
            proto.STRING,
            number=9,
        )
        data_source_end_user_display_name: str = proto.Field(
            proto.STRING,
            number=15,
        )
        connector_icon_link: str = proto.Field(
            proto.STRING,
            number=6,
        )
        connector_auth_state: "WidgetConfig.ConnectorAuthState" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="WidgetConfig.ConnectorAuthState",
        )
        metadata: data_connector.DataConnector.ConnectorMetadata = proto.Field(
            proto.MESSAGE,
            number=13,
            message=data_connector.DataConnector.ConnectorMetadata,
        )
        is_first_party: bool = proto.Field(
            proto.BOOL,
            number=14,
        )
        tag: str = proto.Field(
            proto.STRING,
            number=19,
        )

    class UiSettings(proto.Message):
        r"""Describes general widget (or web app) UI settings as seen
        in the cloud console UI configuration page.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            interaction_type (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.InteractionType):
                Describes widget (or web app) interaction
                type
            generative_answer_config (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.GenerativeAnswerConfig):
                Describes generative answer configuration.
            result_description_type (google.cloud.discoveryengine_v1.types.WidgetConfig.ResultDisplayType):
                Controls whether result extract is display
                and how (snippet or extractive answer). Default
                to no result if unspecified.
            enable_autocomplete (bool):
                Whether or not to enable autocomplete.
            enable_safe_search (bool):
                Whether to enable safe search.
            enable_quality_feedback (bool):
                Turn on or off collecting the search result
                quality feedback from end users.
            enable_search_as_you_type (bool):
                Whether to enable search-as-you-type behavior
                for the search widget.
            default_search_request_order_by (str):
                The default ordering for search results if specified.

                Used to set SearchRequest#order_by on applicable requests.
                https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#request-body
            data_store_ui_configs (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.DataStoreUiConfig]):
                Per data store configuration.
            disable_user_events_collection (bool):
                If set to true, the widget will not collect
                user events.
            enable_visual_content_summary (bool):
                If set to true, the widget will enable visual
                content summary on applicable search requests.
                Only used by healthcare search.
            enable_people_search (bool):
                Optional. If set to true, the widget will
                enable people search.
            enable_create_agent_button (bool):
                Optional. If set to true, the widget will
                enable the create agent button.
            features (MutableMapping[str, google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.FeatureState]):
                Output only. Feature config for the engine to opt in or opt
                out of features. Supported keys:

                - ``agent-gallery``
                - ``no-code-agent-builder``
                - ``prompt-gallery``
                - ``model-selector``
                - ``notebook-lm``
                - ``people-search``
                - ``people-search-org-chart``
                - ``bi-directional-audio``
                - ``speech-to-text``
                - ``feedback``
                - ``session-sharing``
                - ``personalization-memory``
                - ``personalization-suggested-highlights``
                - ``mobile-app-access``
                - ``disable-agent-sharing``
                - ``disable-image-generation``
                - ``disable-video-generation``
                - ``disable-onedrive-upload``
                - ``disable-talk-to-content``
                - ``disable-google-drive-upload``
                - ``disable-welcome-emails``
                - ``disable-canvas``
                - ``canvas-workspace``
                - ``canvas-app-builder``
                - ``skills``
                - ``skill-sharing``
                - ``skill-sharing-without-admin-approval``
                - ``disable-projects``
                - ``sobi``
                - ``enable-end-user-sharing-with-groups``
                - ``single-agent-orchestration``
                - ``multi-agent-orchestration``
                - ``cross-product-intelligence``
                - ``workflow-agents``
                - ``in-app-notifications``
                - ``code-extraction``
                - ``remote-vm``
                - ``license-tier-badge``
            model_configs (MutableMapping[str, google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.ModelState]):
                Output only. Maps a model name to its specific configuration
                for this engine. This allows admin users to turn on/off
                individual models. This only stores models whose states are
                overridden by the admin.

                When the state is unspecified, or model_configs is empty for
                this model, the system will decide if this model should be
                available or not based on the default configuration. For
                example, a preview model should be disabled by default if
                the admin has not chosen to enable it.
            search_addon_spec (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.SearchAddonSpec):
                Optional. SearchAddonSpec is used to disable
                add-ons for search. This field is only supported
                for search requests.
            onedrive_picker_enabled (bool):
                Output only. Whether the OneDrive file picker is available
                to end-users. Computed by the backend from admin connector
                enablement (Business edition) or attached OneDrive
                connectors (Enterprise edition), combined with the existing
                ``disable-onedrive-upload`` admin feature.

                Declared ``optional`` so an explicitly-computed ``false`` is
                serialized with field presence. A plain proto3 ``bool``
                drops a default ``false`` on the wire, which prevented
                clients from distinguishing "picker disabled" (``false``)
                from "field not populated" (unset).

                This field is a member of `oneof`_ ``_onedrive_picker_enabled``.
            google_drive_picker_enabled (bool):
                Output only. Whether the Google Drive file picker is
                available to end-users. Declared ``optional`` for the same
                field-presence reason as ``onedrive_picker_enabled`` above.

                This field is a member of `oneof`_ ``_google_drive_picker_enabled``.
            model_config_info (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.ModelConfigInfo):
                Output only. The resolved, server-side view of model
                selector configuration. Holds both the ordered list of
                models that should appear in the model selector dropdown and
                the model that should be selected by default.

                Clients should render this directly without applying their
                own filtering, ordering, or localization. The legacy
                ``model_configs`` map above is retained for backward
                compatibility with clients that have not yet migrated to
                consuming this field.
            source_admin_display_name_enabled (bool):
                Optional. Whether to show the
                admin-configured display name for data
                connectors in the widget sources UI (instead of
                the connector kind). Opt-in; defaults to false.
        """

        class InteractionType(proto.Enum):
            r"""Describes interaction type.

            Values:
                INTERACTION_TYPE_UNSPECIFIED (0):
                    Not specified. Defaults to SEARCH_ONLY.
                SEARCH_ONLY (1):
                    Search without a generative answer.
                SEARCH_WITH_ANSWER (2):
                    Search with the generative answer.
                SEARCH_WITH_FOLLOW_UPS (3):
                    Search with the generative answer that
                    supports follow up questions. Also known as
                    multi-turn search.
            """

            INTERACTION_TYPE_UNSPECIFIED = 0
            SEARCH_ONLY = 1
            SEARCH_WITH_ANSWER = 2
            SEARCH_WITH_FOLLOW_UPS = 3

        class FeatureState(proto.Enum):
            r"""The state of the feature for the engine.

            Values:
                FEATURE_STATE_UNSPECIFIED (0):
                    The feature state is unspecified.
                FEATURE_STATE_ON (1):
                    The feature is turned on to be accessible.
                FEATURE_STATE_OFF (2):
                    The feature is turned off to be inaccessible.
            """

            FEATURE_STATE_UNSPECIFIED = 0
            FEATURE_STATE_ON = 1
            FEATURE_STATE_OFF = 2

        class ModelState(proto.Enum):
            r"""The state of the model for the engine.

            Values:
                MODEL_STATE_UNSPECIFIED (0):
                    The model state is unspecified.
                MODEL_ENABLED (1):
                    The model is enabled by admin.
                MODEL_DISABLED (2):
                    The model is disabled by admin.
            """

            MODEL_STATE_UNSPECIFIED = 0
            MODEL_ENABLED = 1
            MODEL_DISABLED = 2

        class GenerativeAnswerConfig(proto.Message):
            r"""Describes configuration for generative answer.

            Attributes:
                result_count (int):
                    The number of top results to generate the
                    answer from. Up to 10.
                model_version (str):
                    The model version used to generate the
                    answer.
                model_prompt_preamble (str):
                    Text at the beginning of the prompt that
                    instructs the model that generates the answer.
                max_rephrase_steps (int):
                    Max rephrase steps.
                    The max number is 5 steps.
                    If not set or set to < 1, it will be set to 1 by
                    default.
                language_code (str):
                    Language code for Summary. Use language tags defined by
                    `BCP47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__.
                    Note: This is an experimental feature.
                disable_related_questions (bool):
                    Whether generated answer contains suggested
                    related questions.
                ignore_non_answer_seeking_query (bool):
                    Optional. Specifies whether to filter out queries that are
                    not answer-seeking. The default value is ``false``.

                    No answer is returned if the search query is classified as a
                    non-answer seeking query. If this field is set to ``true``,
                    we skip generating answers for non-answer seeking queries
                    and return fallback messages instead.
                ignore_adversarial_query (bool):
                    Optional. Specifies whether to filter out
                    queries that are adversarial.
                ignore_low_relevant_content (bool):
                    Optional. Specifies whether to filter out
                    queries that are not relevant to the content.
                image_source (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.GenerativeAnswerConfig.ImageSource):
                    Optional. Source of image returned in the
                    answer.
            """

            class ImageSource(proto.Enum):
                r"""Source of image returned in the answer.

                Values:
                    IMAGE_SOURCE_UNSPECIFIED (0):
                        Unspecified image source (multimodal feature
                        is disabled by default)
                    ALL_AVAILABLE_SOURCES (1):
                        Behavior when service determines the pick
                        from all available sources.
                    CORPUS_IMAGE_ONLY (2):
                        Include image from corpus in the answer.
                    FIGURE_GENERATION_ONLY (3):
                        Triggers figure generation in the answer.
                """

                IMAGE_SOURCE_UNSPECIFIED = 0
                ALL_AVAILABLE_SOURCES = 1
                CORPUS_IMAGE_ONLY = 2
                FIGURE_GENERATION_ONLY = 3

            result_count: int = proto.Field(
                proto.INT32,
                number=3,
            )
            model_version: str = proto.Field(
                proto.STRING,
                number=4,
            )
            model_prompt_preamble: str = proto.Field(
                proto.STRING,
                number=5,
            )
            max_rephrase_steps: int = proto.Field(
                proto.INT32,
                number=6,
            )
            language_code: str = proto.Field(
                proto.STRING,
                number=7,
            )
            disable_related_questions: bool = proto.Field(
                proto.BOOL,
                number=8,
            )
            ignore_non_answer_seeking_query: bool = proto.Field(
                proto.BOOL,
                number=9,
            )
            ignore_adversarial_query: bool = proto.Field(
                proto.BOOL,
                number=10,
            )
            ignore_low_relevant_content: bool = proto.Field(
                proto.BOOL,
                number=11,
            )
            image_source: "WidgetConfig.UiSettings.GenerativeAnswerConfig.ImageSource" = proto.Field(
                proto.ENUM,
                number=12,
                enum="WidgetConfig.UiSettings.GenerativeAnswerConfig.ImageSource",
            )

        class ModelConfigInfo(proto.Message):
            r"""The resolved, server-side view of model selector configuration for
            the end-user. The backend computes this per-request by applying, in
            order: Mendel flag evaluation, regional availability rules based on
            the engine's location, and admin-panel overrides from
            ``model_configs``.

            The backend is the single source of truth for this configuration;
            clients should render ``resolved_models`` directly in the model
            selector dropdown, in the order provided, without applying their own
            filtering, ordering, or localization.

            Attributes:
                resolved_models (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.ModelConfigInfo.ResolvedModel]):
                    Output only. The list of models that are
                    available to the end-user in the model selector,
                    in the order in which they should be displayed.
                default_model_id (str):
                    Output only. The ``model_id`` of the model that should be
                    selected by default in the model selector when the end-user
                    has not made an explicit choice. The value is always one of
                    the ``model_id``\ s present in ``resolved_models``.
                auto_model_id (str):
                    Output only. The ``model_id`` a client must send when the
                    end-user picks the "Auto" entry (the empty ``model_id``).

                    Populated only for surfaces known to have no true "Auto"
                    mode, where leaving the model unset would fall back to a
                    platform default rather than a backend-chosen model. Empty
                    on every other surface, where "Auto" is resolved
                    server-side, and when none of the surface's ranked models is
                    available. When set, it is always one of the non-empty
                    ``model_id``\ s present in ``resolved_models``.
            """

            class ResolvedModel(proto.Message):
                r"""A single model that is resolved to be available to the
                end-user in the model selector, with all of its localized
                display metadata.

                Attributes:
                    model_id (str):
                        Output only. Unique identifier of the model (e.g.
                        ``gemini-2.5-flash``, ``gemini-3.1-pro-preview``).

                        This is the same identifier that clients pass back to the
                        assistant service to select this model. Virtual / "pseudo"
                        models (e.g. ``gemini-fast``) are also valid values here;
                        they are resolved to the underlying concrete model on the
                        backend.
                    display_name (str):
                        Output only. Localized display name of the model (e.g.
                        ``Gemini 3.1 Pro``). Localized server-side based on the
                        [LookupWidgetConfigRequest.language_code][google.cloud.discoveryengine.v1.LookupWidgetConfigRequest.language_code]
                        and
                        [LookupWidgetConfigRequest.region_code][google.cloud.discoveryengine.v1.LookupWidgetConfigRequest.region_code]
                        of the request.
                    icon (str):
                        Output only. GM3-compatible icon token associated with the
                        model (e.g. ``rocket_launch``, ``bolt``, ``graph_5``).
                    description (str):
                        Output only. Localized description text (e.g.
                        ``State-of-the-art reasoning``). Localized using the same
                        locale as ``display_name``.
                    is_preview (bool):
                        Output only. Whether the model is currently
                        in preview. Clients should surface this via a
                        "Preview" badge in the selector UI.
                    label (str):
                        Output only. Short label shown in the compact selector bar
                        chip (e.g. ``3.x Flash``) as opposed to the full
                        ``display_name`` (``Gemini 3.x Flash``). Falls back to
                        ``display_name`` when the backend registry does not specify
                        a distinct short label.
                    admin_view (google.cloud.discoveryengine_v1.types.WidgetConfig.UiSettings.ModelConfigInfo.ResolvedModel.AdminView):
                        Output only. Admin-surface metadata; populated only for the
                        Console admin Feature Control page (see ``AdminView``).
                        Unset for end-user surfaces.
                    promoted (bool):
                        Output only. Whether this model should be
                        promoted in the GE chat homepage banner.
                    icon_url (str):
                        Output only. Absolute URL of a brand mark to render instead
                        of ``icon``, for models whose vendor logo is not a GM3
                        glyph.

                        ``icon`` stays populated as the fallback, so a client that
                        does not render images, or that fails to fetch this one,
                        shows the glyph instead of nothing.
                    family (str):
                        Output only. Groups models that render
                        together in the selector. Models sharing a value
                        form one group; empty means the model belongs to
                        no group.

                        Compared for equality only -- never parsed, and
                        never shown to a user, so it is not localized.
                """

                class AdminView(proto.Message):
                    r"""Admin-surface metadata. Populated only when the request
                    originates from the Cloud Console admin "Feature Control" page;
                    left unset for end-user surfaces (Web, Mobile). Lets the admin
                    page render its toggle table directly from the backend instead
                    of a hardcoded client-side registry.

                    Attributes:
                        admin_overridable (bool):
                            Output only. Whether the admin can toggle this model's
                            enabled/disabled state via ``UiSettings.model_configs``.
                            Derived from ``MODEL_TAG_ADMIN_OVERRIDABLE``. When false,
                            the model is "forced" and its state is governed by
                            ``enabled_by_default``.
                        enabled_by_default (bool):
                            Output only. Whether the model is enabled when the admin has
                            set no explicit override in ``UiSettings.model_configs``.
                            Derived from ``MODEL_TAG_ENABLED_BY_DEFAULT``.
                        regions (MutableSequence[str]):
                            Output only. Regions where this model is
                            launched.
                    """

                    admin_overridable: bool = proto.Field(
                        proto.BOOL,
                        number=1,
                    )
                    enabled_by_default: bool = proto.Field(
                        proto.BOOL,
                        number=2,
                    )
                    regions: MutableSequence[str] = proto.RepeatedField(
                        proto.STRING,
                        number=3,
                    )

                model_id: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                display_name: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                icon: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                description: str = proto.Field(
                    proto.STRING,
                    number=4,
                )
                is_preview: bool = proto.Field(
                    proto.BOOL,
                    number=5,
                )
                label: str = proto.Field(
                    proto.STRING,
                    number=7,
                )
                admin_view: "WidgetConfig.UiSettings.ModelConfigInfo.ResolvedModel.AdminView" = proto.Field(
                    proto.MESSAGE,
                    number=6,
                    message="WidgetConfig.UiSettings.ModelConfigInfo.ResolvedModel.AdminView",
                )
                promoted: bool = proto.Field(
                    proto.BOOL,
                    number=8,
                )
                icon_url: str = proto.Field(
                    proto.STRING,
                    number=9,
                )
                family: str = proto.Field(
                    proto.STRING,
                    number=10,
                )

            resolved_models: MutableSequence[
                "WidgetConfig.UiSettings.ModelConfigInfo.ResolvedModel"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="WidgetConfig.UiSettings.ModelConfigInfo.ResolvedModel",
            )
            default_model_id: str = proto.Field(
                proto.STRING,
                number=2,
            )
            auto_model_id: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class SearchAddonSpec(proto.Message):
            r"""SearchAddonSpec is used to disable add-ons for search. By
            default, if this field is not specified, add-ons are enabled
            wherever applicable.

            Attributes:
                semantic_add_on_disabled (bool):
                    Optional. If true, semantic add-on is
                    disabled. Semantic add-on includes embeddings
                    and jetstream.
                kpi_personalization_add_on_disabled (bool):
                    Optional. If true, disables event re-ranking
                    and personalization to optimize KPIs &
                    personalize results.
                generative_answer_add_on_disabled (bool):
                    Optional. If true, generative answer add-on
                    is disabled. Generative answer add-on includes
                    natural language to filters and simple answers.
            """

            semantic_add_on_disabled: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            kpi_personalization_add_on_disabled: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            generative_answer_add_on_disabled: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        interaction_type: "WidgetConfig.UiSettings.InteractionType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="WidgetConfig.UiSettings.InteractionType",
        )
        generative_answer_config: "WidgetConfig.UiSettings.GenerativeAnswerConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="WidgetConfig.UiSettings.GenerativeAnswerConfig",
            )
        )
        result_description_type: "WidgetConfig.ResultDisplayType" = proto.Field(
            proto.ENUM,
            number=3,
            enum="WidgetConfig.ResultDisplayType",
        )
        enable_autocomplete: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        enable_safe_search: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        enable_quality_feedback: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        enable_search_as_you_type: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        default_search_request_order_by: str = proto.Field(
            proto.STRING,
            number=8,
        )
        data_store_ui_configs: MutableSequence["WidgetConfig.DataStoreUiConfig"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=9,
                message="WidgetConfig.DataStoreUiConfig",
            )
        )
        disable_user_events_collection: bool = proto.Field(
            proto.BOOL,
            number=10,
        )
        enable_visual_content_summary: bool = proto.Field(
            proto.BOOL,
            number=11,
        )
        enable_people_search: bool = proto.Field(
            proto.BOOL,
            number=12,
        )
        enable_create_agent_button: bool = proto.Field(
            proto.BOOL,
            number=13,
        )
        features: MutableMapping[str, "WidgetConfig.UiSettings.FeatureState"] = (
            proto.MapField(
                proto.STRING,
                proto.ENUM,
                number=30,
                enum="WidgetConfig.UiSettings.FeatureState",
            )
        )
        model_configs: MutableMapping[str, "WidgetConfig.UiSettings.ModelState"] = (
            proto.MapField(
                proto.STRING,
                proto.ENUM,
                number=45,
                enum="WidgetConfig.UiSettings.ModelState",
            )
        )
        search_addon_spec: "WidgetConfig.UiSettings.SearchAddonSpec" = proto.Field(
            proto.MESSAGE,
            number=31,
            message="WidgetConfig.UiSettings.SearchAddonSpec",
        )
        onedrive_picker_enabled: bool = proto.Field(
            proto.BOOL,
            number=48,
            optional=True,
        )
        google_drive_picker_enabled: bool = proto.Field(
            proto.BOOL,
            number=49,
            optional=True,
        )
        model_config_info: "WidgetConfig.UiSettings.ModelConfigInfo" = proto.Field(
            proto.MESSAGE,
            number=50,
            message="WidgetConfig.UiSettings.ModelConfigInfo",
        )
        source_admin_display_name_enabled: bool = proto.Field(
            proto.BOOL,
            number=51,
        )

    class AccessSettings(proto.Message):
        r"""Describes widget access settings.

        Attributes:
            allow_public_access (bool):
                Whether public unauthenticated access is
                allowed.
            allowlisted_domains (MutableSequence[str]):
                List of domains that are allowed to integrate
                the search widget.
            enable_web_app (bool):
                Whether web app access is enabled.
            workforce_identity_pool_provider (str):
                Optional. The workforce identity pool
                provider used to access the widget.
            language_code (str):
                Optional. Language code for user interface. Use language
                tags defined by
                `BCP47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__. If
                unset, the default language code is "en-US".
        """

        allow_public_access: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        allowlisted_domains: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        enable_web_app: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        workforce_identity_pool_provider: str = proto.Field(
            proto.STRING,
            number=4,
        )
        language_code: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class Image(proto.Message):
        r"""Options to store an image.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            url (str):
                Image URL.

                This field is a member of `oneof`_ ``storage_method``.
        """

        url: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="storage_method",
        )

    class UiBrandingSettings(proto.Message):
        r"""Describes widget UI branding settings.

        Attributes:
            logo (google.cloud.discoveryengine_v1.types.WidgetConfig.Image):
                Logo image.
        """

        logo: "WidgetConfig.Image" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="WidgetConfig.Image",
        )

    class HomepageSetting(proto.Message):
        r"""Describes the homepage setting of the widget. It includes all
        homepage related settings and configurations, such as shortcuts.

        Attributes:
            shortcuts (MutableSequence[google.cloud.discoveryengine_v1.types.WidgetConfig.HomepageSetting.Shortcut]):
                Optional. The shortcuts to display on the
                homepage.
        """

        class Shortcut(proto.Message):
            r"""Describes an entity of shortcut (aka pinned content) on the
            homepage. The home page will render these shortcuts in the same
            order as what the API returns. If a customer wants to reorder or
            remove a shortcut, the UI should always provide the new full
            list of shortcuts.

            Attributes:
                title (str):
                    Optional. Title of the shortcut.
                icon (google.cloud.discoveryengine_v1.types.WidgetConfig.Image):
                    Optional. Icon URL of shortcut.
                destination_uri (str):
                    Optional. Destination URL of shortcut.
            """

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            icon: "WidgetConfig.Image" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="WidgetConfig.Image",
            )
            destination_uri: str = proto.Field(
                proto.STRING,
                number=3,
            )

        shortcuts: MutableSequence["WidgetConfig.HomepageSetting.Shortcut"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="WidgetConfig.HomepageSetting.Shortcut",
            )
        )

    class AssistantSettings(proto.Message):
        r"""Describes the assistant settings of the widget.

        Attributes:
            web_grounding_type (google.cloud.discoveryengine_v1.types.WidgetConfig.AssistantSettings.WebGroundingType):
                Optional. The type of web grounding to use.
            default_web_grounding_toggle_off (bool):
                Output only. This field controls the default web grounding
                toggle for end users if ``web_grounding_type`` is set to
                ``WEB_GROUNDING_TYPE_GOOGLE_SEARCH`` or
                ``WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH``. By default,
                this field is set to false. If ``web_grounding_type`` is
                ``WEB_GROUNDING_TYPE_GOOGLE_SEARCH`` or
                ``WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH``, end users will
                have web grounding enabled by default on UI. If true,
                grounding toggle will be disabled by default on UI. End
                users can still enable web grounding in the UI if web
                grounding is enabled.
            disable_location_context (bool):
                Optional. Output only. Whether to disable
                user location context.
        """

        class WebGroundingType(proto.Enum):
            r"""The type of web grounding to use.

            Values:
                WEB_GROUNDING_TYPE_UNSPECIFIED (0):
                    Default, unspecified setting. This is the
                    same as disabled.
                WEB_GROUNDING_TYPE_DISABLED (1):
                    Web grounding is disabled.
                WEB_GROUNDING_TYPE_GOOGLE_SEARCH (2):
                    Grounding with Google Search is enabled.
                WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH (3):
                    Grounding with Enterprise Web Search is
                    enabled.
            """

            WEB_GROUNDING_TYPE_UNSPECIFIED = 0
            WEB_GROUNDING_TYPE_DISABLED = 1
            WEB_GROUNDING_TYPE_GOOGLE_SEARCH = 2
            WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH = 3

        web_grounding_type: "WidgetConfig.AssistantSettings.WebGroundingType" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="WidgetConfig.AssistantSettings.WebGroundingType",
            )
        )
        default_web_grounding_toggle_off: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        disable_location_context: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class CustomerProvidedConfig(proto.Message):
        r"""Customer provided configurations.

        Attributes:
            customer_type (google.cloud.discoveryengine_v1.types.WidgetConfig.CustomerProvidedConfig.CustomerType):
                Customer type.
            compliance_level (google.cloud.discoveryengine_v1.types.WidgetConfig.CustomerProvidedConfig.ComplianceLevel):
                Output only. The customer's Assured Workloads compliance
                level.

                ``customer_type`` collapses every compliance level into a
                single ``GOVERNMENT_CUSTOMER`` value, so a client that gates
                a feature on one specific level rather than on government
                status as a whole must read this field instead.
        """

        class CustomerType(proto.Enum):
            r"""Customer type.

            Values:
                DEFAULT_CUSTOMER (0):
                    Default customer type.
                GOVERNMENT_CUSTOMER (1):
                    Government customer type. Some features are
                    disabled for government customers due to legal
                    requirements.
            """

            DEFAULT_CUSTOMER = 0
            GOVERNMENT_CUSTOMER = 1

        class ComplianceLevel(proto.Enum):
            r"""Assured Workloads compliance level of the customer's project.

            Not frozen: further levels may be added as more compliance
            regimes are supported, so a client must treat an unrecognized
            value as government-restricted rather than as unrestricted.

            Values:
                COMPLIANCE_LEVEL_UNSPECIFIED (0):
                    The project has no Assured Workloads
                    compliance level, or reports one that this API
                    version does not model.
                COMPLIANCE_LEVEL_FEDRAMP_HIGH (1):
                    FedRAMP High compliance level.
                COMPLIANCE_LEVEL_IL4 (2):
                    Impact Level 4 (IL4) compliance level.
                COMPLIANCE_LEVEL_IL5 (3):
                    Impact Level 5 (IL5) compliance level.
            """

            COMPLIANCE_LEVEL_UNSPECIFIED = 0
            COMPLIANCE_LEVEL_FEDRAMP_HIGH = 1
            COMPLIANCE_LEVEL_IL4 = 2
            COMPLIANCE_LEVEL_IL5 = 3

        customer_type: "WidgetConfig.CustomerProvidedConfig.CustomerType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="WidgetConfig.CustomerProvidedConfig.CustomerType",
        )
        compliance_level: "WidgetConfig.CustomerProvidedConfig.ComplianceLevel" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="WidgetConfig.CustomerProvidedConfig.ComplianceLevel",
            )
        )

    class Node(proto.Message):
        r"""Represents a single reusable computational or logical unit.

        Attributes:
            display_name (str):
                Output only. A human readable name for the
                node.
            icon_url (str):
                Output only. An identifier or URL pointing to
                an icon representing this node type.
            description (str):
                Output only. A detailed description of what
                the node does.
            parameter_schema (google.protobuf.struct_pb2.Struct):
                Output only. The parameter schema of the
                tool.
                This schema is expected to conform to the
                OpenAPI Schema standard (see
                https://spec.openapis.org/oas/v3.0.3.html and
                AIP-146). It describes the expected structure of
                the parameters that this node accepts.
            output_schema (google.protobuf.struct_pb2.Struct):
                Output only. The output schema of the tool.

                This schema is expected to conform to the
                OpenAPI Schema standard (see
                https://spec.openapis.org/oas/v3.0.3.html/ and
                AIP-146). It describes the structure of the
                output produced by this node.
            type_ (google.cloud.discoveryengine_v1.types.WidgetConfig.Node.Type):
                Output only. The type of the node.
        """

        class Type(proto.Enum):
            r"""Identifies the type of the node in the agent flow.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                TRIGGER (1):
                    Trigger type.
                FLOW (2):
                    Flow type.
                CONNECTOR (3):
                    Connector type.
            """

            TYPE_UNSPECIFIED = 0
            TRIGGER = 1
            FLOW = 2
            CONNECTOR = 3

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        icon_url: str = proto.Field(
            proto.STRING,
            number=2,
        )
        description: str = proto.Field(
            proto.STRING,
            number=3,
        )
        parameter_schema: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=4,
            message=struct_pb2.Struct,
        )
        output_schema: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=5,
            message=struct_pb2.Struct,
        )
        type_: "WidgetConfig.Node.Type" = proto.Field(
            proto.ENUM,
            number=6,
            enum="WidgetConfig.Node.Type",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
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
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    data_store_type: DataStoreType = proto.Field(
        proto.ENUM,
        number=8,
        enum=DataStoreType,
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    solution_type: common.SolutionType = proto.Field(
        proto.ENUM,
        number=14,
        enum=common.SolutionType,
    )
    industry_vertical: common.IndustryVertical = proto.Field(
        proto.ENUM,
        number=26,
        enum=common.IndustryVertical,
    )
    llm_enabled: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    enable_result_score: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    minimum_data_term_accepted: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    collection_components: MutableSequence[CollectionComponent] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message=CollectionComponent,
    )
    ui_settings: UiSettings = proto.Field(
        proto.MESSAGE,
        number=33,
        message=UiSettings,
    )
    access_settings: AccessSettings = proto.Field(
        proto.MESSAGE,
        number=34,
        message=AccessSettings,
    )
    ui_branding: UiBrandingSettings = proto.Field(
        proto.MESSAGE,
        number=35,
        message=UiBrandingSettings,
    )
    homepage_setting: HomepageSetting = proto.Field(
        proto.MESSAGE,
        number=38,
        message=HomepageSetting,
    )
    assistant_settings: AssistantSettings = proto.Field(
        proto.MESSAGE,
        number=39,
        message=AssistantSettings,
    )
    customer_provided_config: CustomerProvidedConfig = proto.Field(
        proto.MESSAGE,
        number=40,
        message=CustomerProvidedConfig,
    )
    enable_private_knowledge_graph: bool = proto.Field(
        proto.BOOL,
        number=42,
    )
    gemini_bundle: bool = proto.Field(
        proto.BOOL,
        number=44,
    )
    batch_auth_statuses: MutableSequence[BatchAuthStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=48,
        message=BatchAuthStatus,
    )
    nodes: MutableSequence[Node] = proto.RepeatedField(
        proto.MESSAGE,
        number=46,
        message=Node,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
