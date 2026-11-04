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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.discoveryengine_v1.types import common, schema

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1",
    manifest={
        "ConnectorType",
        "DataConnector",
        "DestinationConfig",
        "ActionConfig",
        "IdentityScheduleConfig",
        "BAPConfig",
        "CliConfig",
        "AlertPolicyConfig",
        "Tenant",
        "DynamicTool",
    },
)


class ConnectorType(proto.Enum):
    r"""The type of connector.
    New values may be added to this enum in the future.

    Values:
        CONNECTOR_TYPE_UNSPECIFIED (0):
            Default value.
        THIRD_PARTY (1):
            Third party connector to connector to third
            party application.
        GCP_FHIR (2):
            Data connector connects between FHIR store
            and VAIS datastore.
        BIG_QUERY (3):
            Big query connector.
        GCS (4):
            Google Cloud Storage connector.
        GOOGLE_MAIL (5):
            Gmail connector.
        GOOGLE_CALENDAR (6):
            Google Calendar connector.
        GOOGLE_DRIVE (7):
            Google Drive connector.
        NATIVE_CLOUD_IDENTITY (8):
            Native Cloud Identity connector for people
            search powered by People API.
        THIRD_PARTY_FEDERATED (9):
            Federated connector, it is a third party
            connector that doesn't ingestion data, and
            search is powered by third party application's
            API.
        THIRD_PARTY_EUA (10):
            Connector utilized for End User
            Authentication features.
        GCNV (11):
            Google Cloud NetApp Volumes connector.
        GOOGLE_CHAT (12):
            Google Chat connector.
        GOOGLE_SITES (13):
            Google Sites connector.
        REMOTE_MCP (14):
            Remote MCP based connector.
        GOOGLE_WORKSPACE (15):
            Google Workspace connector.
    """

    CONNECTOR_TYPE_UNSPECIFIED = 0
    THIRD_PARTY = 1
    GCP_FHIR = 2
    BIG_QUERY = 3
    GCS = 4
    GOOGLE_MAIL = 5
    GOOGLE_CALENDAR = 6
    GOOGLE_DRIVE = 7
    NATIVE_CLOUD_IDENTITY = 8
    THIRD_PARTY_FEDERATED = 9
    THIRD_PARTY_EUA = 10
    GCNV = 11
    GOOGLE_CHAT = 12
    GOOGLE_SITES = 13
    REMOTE_MCP = 14
    GOOGLE_WORKSPACE = 15


class DataConnector(proto.Message):
    r"""Manages the connection to external data sources for all data stores
    grouped under a
    [Collection][google.cloud.discoveryengine.v1.Collection]. It's a
    singleton resource of
    [Collection][google.cloud.discoveryengine.v1.Collection]. The
    initialization is only supported through
    [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
    method, which will create a new
    [Collection][google.cloud.discoveryengine.v1.Collection] and
    initialize its
    [DataConnector][google.cloud.discoveryengine.v1.DataConnector].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        params (google.protobuf.struct_pb2.Struct):
            Required data connector parameters in
            structured json format.

            This field is a member of `oneof`_ ``data_connector_params``.
        json_params (str):
            Required data connector parameters in json
            string format.

            This field is a member of `oneof`_ ``data_connector_params``.
        name (str):
            Identifier. The full resource name of the Data Connector.
            Format:
            ``projects/*/locations/*/collections/*/dataConnector``.
        state (google.cloud.discoveryengine_v1.types.DataConnector.State):
            Output only. State of the connector.
        data_source (str):
            Required. The identifier for the data source. For the full,
            up-to-date list of supported connectors and their values,
            see `Connect a third-party data
            source <https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source#sources-by-launch-stage>`__.
        remove_param_keys (MutableSequence[str]):
            Optional. Specifies keys to be removed from the 'params'
            field. This is only active when 'params' is included in the
            'update_mask' in an UpdateDataConnectorRequest. Deletion
            takes precedence if a key is both in 'remove_param_keys' and
            present in the 'params' field of the request.
        refresh_interval (google.protobuf.duration_pb2.Duration):
            Required. The refresh interval for data sync.
            If duration is set to 0, the data will be synced
            in real time. The streaming feature is not
            supported yet. The minimum is 30 minutes and
            maximum is 7 days. When the refresh interval is
            set to the same value as the incremental refresh
            interval, incremental sync will be disabled.
        next_sync_time (google.type.datetime_pb2.DateTime):
            Defines the scheduled time for the next data
            synchronization. This field requires hour , minute, and
            time_zone from the `IANA Time Zone
            Database <https://www.iana.org/time-zones>`__. This is
            utilized when the data connector has a refresh interval
            greater than 1 day. When the hours or minutes are not
            specified, we will assume a sync time of 0:00. The user must
            provide a time zone to avoid ambiguity.
        entities (MutableSequence[google.cloud.discoveryengine_v1.types.DataConnector.SourceEntity]):
            List of entities from the connected data
            source to ingest.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            was created at.
        latest_pause_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent timestamp when this
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            was paused, affecting all functionalities such as data
            synchronization. Pausing a connector has the following
            effects:

            - All functionalities, including data synchronization, are
              halted.
            - Any ongoing data synchronization job will be canceled.
            - No future data synchronization runs will be scheduled nor
              can be triggered.
        last_sync_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For periodic connectors only,
            the last time a data sync was completed.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            was last updated.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            Output only. The errors from initialization
            or from the latest connector run.
        sync_mode (google.cloud.discoveryengine_v1.types.DataConnector.SyncMode):
            The data synchronization mode supported by
            the data connector.
        kms_key_name (str):
            Input only. The KMS key to be used to protect
            the DataStores managed by this connector.

            Must be set for requests that need to comply
            with CMEK Org Policy protections.

            If this field is set and processed successfully,
            the DataStores created by this connector will be
            protected by the KMS key.
        destination_configs (MutableSequence[google.cloud.discoveryengine_v1.types.DestinationConfig]):
            Optional. Any target destinations used to
            connect to third-party services.
        action_state (google.cloud.discoveryengine_v1.types.DataConnector.State):
            Output only. State of the action connector.
            This reflects whether the action connector is
            initializing, active or has encountered errors.
        action_config (google.cloud.discoveryengine_v1.types.ActionConfig):
            Optional. Action configurations to make the
            connector support actions.
        end_user_config (google.cloud.discoveryengine_v1.types.DataConnector.EndUserConfig):
            Optional. Any params and credentials used
            specifically for EUA connectors.
        federated_config (google.cloud.discoveryengine_v1.types.DataConnector.FederatedConfig):
            Optional. Any params and credentials used
            specifically for hybrid connectors supporting
            FEDERATED mode. This field should only be set if
            the connector is a hybrid connector and we want
            to enable FEDERATED mode.
        connector_modes (MutableSequence[google.cloud.discoveryengine_v1.types.DataConnector.ConnectorMode]):
            Optional. The modes enabled for this connector. Default
            state is CONNECTOR_MODE_UNSPECIFIED.
        static_ip_enabled (bool):
            Optional. Whether customer has enabled static
            IP addresses for this connector.
        static_ip_addresses (MutableSequence[str]):
            Output only. The static IP addresses used by
            this connector.
        oauth_static_ip_addresses (MutableSequence[str]):
            Output only. The static IP addresses used by this connector
            for OAuth APIs (e.g. end user authentication). These are
            surfaced separately from ``static_ip_addresses`` so that
            customers can apply granular firewall settings for OAuth
            endpoints. Only populated for connectors that have static IP
            enabled and are used for actions and/or federated search.
        blocking_reasons (MutableSequence[google.cloud.discoveryengine_v1.types.DataConnector.BlockingReason]):
            Output only. User actions that must be
            completed before the connector can start syncing
            data.
        identity_schedule_config (google.cloud.discoveryengine_v1.types.IdentityScheduleConfig):
            The configuration for the identity data
            synchronization runs. This contains the refresh
            interval to sync the Access Control List
            information for the documents ingested by this
            connector.
        private_connectivity_project_id (str):
            Output only. The tenant project ID associated
            with private connectivity connectors. This
            project must be allowlisted by in order for the
            connector to function.
        bap_config (google.cloud.discoveryengine_v1.types.BAPConfig):
            Optional. The configuration for establishing
            a BAP connection.
        connector_type (google.cloud.discoveryengine_v1.types.ConnectorType):
            Output only. The type of connector. Each source can only map
            to one type. For example, salesforce, confluence and jira
            have THIRD_PARTY connector type. It is not mutable once set
            by system.
        realtime_state (google.cloud.discoveryengine_v1.types.DataConnector.State):
            Output only. real-time sync state
        alert_policy_configs (MutableSequence[google.cloud.discoveryengine_v1.types.AlertPolicyConfig]):
            Optional. The connector level alert config.
        realtime_sync_config (google.cloud.discoveryengine_v1.types.DataConnector.RealtimeSyncConfig):
            Optional. The configuration for realtime
            sync.
        acl_enabled (bool):
            Optional. Whether the connector will be
            created with an ACL config. Currently this field
            only affects Cloud Storage and BigQuery
            connectors.
        create_eua_saas (bool):
            Optional. Whether the END USER AUTHENTICATION
            connector is created in SaaS.
        auto_run_disabled (bool):
            Optional. Indicates whether the connector is disabled for
            auto run. It can be used to pause periodical and real time
            sync. Update: with the introduction of
            incremental_sync_disabled, auto_run_disabled is used to
            pause/disable only full syncs
        incremental_sync_disabled (bool):
            Optional. Indicates whether incremental syncs are paused for
            this connector. This is independent of auto_run_disabled.
            Applicable to only 3P connectors. When the refresh interval
            is set to the same value as the incremental refresh
            interval, incremental sync will be disabled, i.e. set to
            true.
        incremental_refresh_interval (google.protobuf.duration_pb2.Duration):
            Optional. The refresh interval specifically
            for incremental data syncs. If unset,
            incremental syncs will use the default from env,
            set to 3hrs. The minimum is 30 minutes and
            maximum is 7 days. Applicable to only 3P
            connectors. When the refresh interval is
            set to the same value as the incremental refresh
            interval, incremental sync will be disabled.
        hybrid_ingestion_disabled (bool):
            Optional. If the connector is a hybrid
            connector, determines whether ingestion is
            enabled and appropriate resources are
            provisioned during connector creation. If the
            connector is not a hybrid connector, this field
            is ignored.
        data_protection_policy (google.cloud.discoveryengine_v1.types.DataProtectionPolicy):
            Optional. Specifies the data protection
            policy for the connector.
        egress_fqdns (MutableSequence[str]):
            Output only. The list of FQDNs of the data
            connector can egress to. This includes both FQDN
            derived from the customer provided instance URL
            and default per connector type FQDNs.
        vpcsc_enabled (bool):
            Output only. Whether the connector is created
            with VPC-SC enabled.
        dynamic_tools (MutableSequence[google.cloud.discoveryengine_v1.types.DynamicTool]):
            Output only. The dynamic tools fetched for
            this connector.
        cli_config (google.cloud.discoveryengine_v1.types.CliConfig):
            Optional. The configuration for establishing
            a CLI connection.
        connector_source_id (str):
            Optional. If set, this value instead of ``data_source`` is
            used to fetch the corresponding connector source.
        tag (str):
            Optional. Immutable. User-facing, version-independent label
            for this connector. May be shared by multiple connectors
            under the same (project, location, collection, data_source);
            tag-based lookup returns the one with the greatest
            create_time.

            Optional at Create time. If the caller omits ``tag``, the
            server auto-derives one from the collection_id (falling back
            to data_source, else a time-based ``t-<micros>`` sentinel).
            The auto-derived tag is subject to the same immutability
            guarantee as a caller-supplied one, so callers who care
            about the exact tag value should provide it explicitly
            rather than relying on the server default.

            Agent Designer resolves connectors via (data_source, tag)
            when set, falling back to the legacy resource-name lookup
            when unset, so connectors created before the tag-write
            launch continue to work without a backfill.
        metadata (google.cloud.discoveryengine_v1.types.DataConnector.ConnectorMetadata):
            Optional. User-facing metadata for the connector. Populated
            from the connector's generated metadata / registry
            ``ConnectorSource``.
    """

    class State(proto.Enum):
        r"""The state of connector.

        Values:
            STATE_UNSPECIFIED (0):
                Default value.
            CREATING (1):
                The connector is being set up.
            ACTIVE (2):
                The connector is successfully set up and
                awaiting next sync run.
            FAILED (3):
                The connector is in error. The error details can be found in
                [DataConnector.errors][google.cloud.discoveryengine.v1.DataConnector.errors].
                If the error is unfixable, the
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                can be deleted by
                [CollectionService.DeleteCollection][google.cloud.discoveryengine.v1.CollectionService.DeleteCollection]
                API.
            RUNNING (4):
                The connector is actively syncing records
                from the data source.
            WARNING (5):
                The connector has completed a sync run, but
                encountered non-fatal errors.
            INITIALIZATION_FAILED (6):
                Connector initialization failed. Potential
                causes include runtime errors or issues in the
                asynchronous pipeline, preventing the request
                from reaching downstream services (except for
                some connector types).
            UPDATING (7):
                Connector is in the process of an update.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        RUNNING = 4
        WARNING = 5
        INITIALIZATION_FAILED = 6
        UPDATING = 7

    class SyncMode(proto.Enum):
        r"""Defines the data synchronization mode supported by the data
        connector.

        Values:
            PERIODIC (0):
                The connector will sync data periodically based on the
                refresh_interval. Use it with auto_run_disabled to pause the
                periodic sync, or indicate a one-time sync.
            STREAMING (1):
                The data will be synced in real time.
            UNSPECIFIED (2):
                Connector that doesn't ingest data will have
                this value
        """

        PERIODIC = 0
        STREAMING = 1
        UNSPECIFIED = 2

    class ConnectorMode(proto.Enum):
        r"""The modes enabled for this connector. INGESTION, ACTIONS,
        FEDERATED, OR EUA

        Values:
            CONNECTOR_MODE_UNSPECIFIED (0):
                Connector mode unspecified.
            DATA_INGESTION (1):
                Connector utilized for data ingestion.
            ACTIONS (2):
                Connector utilized for actions.
            FEDERATED (3):
                Connector utilized for federated search.
            EUA (4):
                Connector utilized for End User
                Authentication.
            FEDERATED_AND_EUA (5):
                Hybrid connector utilized for federated
                search and End User Authentication.
        """

        CONNECTOR_MODE_UNSPECIFIED = 0
        DATA_INGESTION = 1
        ACTIONS = 2
        FEDERATED = 3
        EUA = 4
        FEDERATED_AND_EUA = 5

    class BlockingReason(proto.Enum):
        r"""User actions that must be completed before the connector can
        start syncing data.

        Values:
            BLOCKING_REASON_UNSPECIFIED (0):
                Default value.
            ALLOWLIST_STATIC_IP (1):
                Connector requires customer to allowlist
                static IPs.
            ALLOWLIST_IN_SERVICE_ATTACHMENT (2):
                Connector requires customer to allowlist our
                project in their service attachment.
            ALLOWLIST_SERVICE_ACCOUNT (3):
                Connector requires customer to allowlist
                service account in their project.
        """

        BLOCKING_REASON_UNSPECIFIED = 0
        ALLOWLIST_STATIC_IP = 1
        ALLOWLIST_IN_SERVICE_ATTACHMENT = 2
        ALLOWLIST_SERVICE_ACCOUNT = 3

    class SourceEntity(proto.Message):
        r"""Represents an entity in the data source. For example, the
        ``Account`` object in Salesforce.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            params (google.protobuf.struct_pb2.Struct):
                The parameters for the entity to facilitate
                data ingestion in structured json format.

                This field is a member of `oneof`_ ``entity_params``.
            json_params (str):
                The parameters for the entity to facilitate
                data ingestion in json string format.

                This field is a member of `oneof`_ ``entity_params``.
            entity_name (str):
                The name of the entity. Supported values by data source:

                - Salesforce: ``Lead``, ``Opportunity``, ``Contact``,
                  ``Account``, ``Case``, ``Contract``, ``Campaign``
                - Jira: ``Issue``
                - Confluence: ``Content``, ``Space``
            key_property_mappings (MutableMapping[str, str]):
                Attributes for indexing. Key: Field name. Value: The key
                property to map a field to, such as ``title``, and
                ``description``. Supported key properties:

                - ``title``: The title for data record. This would be
                  displayed on search results.
                - ``description``: The description for data record. This
                  would be displayed on search results.
            data_store (str):
                Output only. The full resource name of the associated data
                store for the source entity. Format:
                ``projects/*/locations/*/collections/*/dataStores/*``. When
                the connector is initialized by the
                [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
                method, a
                [DataStore][google.cloud.discoveryengine.v1.DataStore] is
                automatically created for each source entity.
            starting_schema (google.cloud.discoveryengine_v1.types.Schema):
                Optional. The start schema to use for the
                [DataStore][google.cloud.discoveryengine.v1.DataStore]
                created from this SourceEntity. If unset, a default vertical
                specialized schema will be used.

                This field is only used by
                [SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
                API, and will be ignored if used in other APIs. This field
                will be omitted from all API responses including
                [GetDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector]
                API. To retrieve a schema of a
                [DataStore][google.cloud.discoveryengine.v1.DataStore], use
                [SchemaService.GetSchema][google.cloud.discoveryengine.v1.SchemaService.GetSchema]
                API instead.

                The provided schema will be validated against certain rules
                on schema. Learn more from `this
                doc <https://cloud.google.com/generative-ai-app-builder/docs/provide-schema>`__.
            healthcare_fhir_config (google.cloud.discoveryengine_v1.types.HealthcareFhirConfig):
                Optional. Configuration for ``HEALTHCARE_FHIR`` vertical.
        """

        params: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="entity_params",
            message=struct_pb2.Struct,
        )
        json_params: str = proto.Field(
            proto.STRING,
            number=10,
            oneof="entity_params",
        )
        entity_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        key_property_mappings: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        data_store: str = proto.Field(
            proto.STRING,
            number=3,
        )
        starting_schema: schema.Schema = proto.Field(
            proto.MESSAGE,
            number=6,
            message=schema.Schema,
        )
        healthcare_fhir_config: common.HealthcareFhirConfig = proto.Field(
            proto.MESSAGE,
            number=7,
            message=common.HealthcareFhirConfig,
        )

    class EndUserConfig(proto.Message):
        r"""Any params and credentials used specifically for EUA
        connectors.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            auth_params (google.protobuf.struct_pb2.Struct):
                Optional. Any authentication parameters
                specific to EUA connectors.

                This field is a member of `oneof`_ ``auth_config``.
            json_auth_params (str):
                Optional. Any authentication parameters
                specific to EUA connectors in json string
                format.

                This field is a member of `oneof`_ ``auth_config``.
            additional_params (google.protobuf.struct_pb2.Struct):
                Optional. Any additional parameters needed
                for EUA.
            tenant (google.cloud.discoveryengine_v1.types.Tenant):
                Optional. The tenant project the connector is
                connected to.
        """

        auth_params: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="auth_config",
            message=struct_pb2.Struct,
        )
        json_auth_params: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="auth_config",
        )
        additional_params: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )
        tenant: "Tenant" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Tenant",
        )

    class FederatedConfig(proto.Message):
        r"""Any params and credentials used specifically for hybrid
        connectors supporting FEDERATED mode.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            auth_params (google.protobuf.struct_pb2.Struct):
                Optional. Any authentication parameters
                specific to FEDERATED connectors.

                This field is a member of `oneof`_ ``auth_config``.
            json_auth_params (str):
                Optional. Any authentication parameters
                specific to FEDERATED connectors in json string
                format.

                This field is a member of `oneof`_ ``auth_config``.
            additional_params (google.protobuf.struct_pb2.Struct):
                Optional. Any additional parameters needed
                for FEDERATED.
        """

        auth_params: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="auth_config",
            message=struct_pb2.Struct,
        )
        json_auth_params: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="auth_config",
        )
        additional_params: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    class RealtimeSyncConfig(proto.Message):
        r"""The configuration for realtime sync to store additional
        params for realtime sync.

        Attributes:
            webhook_uri (str):
                Optional. Webhook url for the connector to
                specify additional params for realtime sync.
            realtime_sync_secret (str):
                Optional. The ID of the Secret Manager secret
                used for webhook secret.
            streaming_error (google.cloud.discoveryengine_v1.types.DataConnector.RealtimeSyncConfig.StreamingError):
                Optional. Streaming error details.
        """

        class StreamingError(proto.Message):
            r"""Streaming error details.

            Attributes:
                streaming_error_reason (google.cloud.discoveryengine_v1.types.DataConnector.RealtimeSyncConfig.StreamingError.StreamingErrorReason):
                    Optional. Streaming error.
                error (google.rpc.status_pb2.Status):
                    Optional. Error details.
            """

            class StreamingErrorReason(proto.Enum):
                r"""Broad types of streaming errors.

                Values:
                    STREAMING_ERROR_REASON_UNSPECIFIED (0):
                        Streaming error reason unspecified.
                    STREAMING_SETUP_ERROR (1):
                        Some error occurred while setting up
                        resources for realtime sync.
                    STREAMING_SYNC_ERROR (2):
                        Some error was encountered while running
                        realtime sync for the connector.
                    INGRESS_ENDPOINT_REQUIRED (3):
                        Ingress endpoint is required when setting up
                        realtime sync in private connectivity.
                """

                STREAMING_ERROR_REASON_UNSPECIFIED = 0
                STREAMING_SETUP_ERROR = 1
                STREAMING_SYNC_ERROR = 2
                INGRESS_ENDPOINT_REQUIRED = 3

            streaming_error_reason: "DataConnector.RealtimeSyncConfig.StreamingError.StreamingErrorReason" = proto.Field(
                proto.ENUM,
                number=1,
                enum="DataConnector.RealtimeSyncConfig.StreamingError.StreamingErrorReason",
            )
            error: status_pb2.Status = proto.Field(
                proto.MESSAGE,
                number=2,
                message=status_pb2.Status,
            )

        webhook_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        realtime_sync_secret: str = proto.Field(
            proto.STRING,
            number=2,
        )
        streaming_error: "DataConnector.RealtimeSyncConfig.StreamingError" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="DataConnector.RealtimeSyncConfig.StreamingError",
            )
        )

    class ConnectorMetadata(proto.Message):
        r"""User-facing metadata for the connector, shown on the connector
        detail page (title, description, short_description, author, note).

        Attributes:
            title (str):
                Optional. Display title of the connector.
            description (str):
                Optional. Human-readable description of the
                connector, shown on the connector detail page.
                One connector has a single description.
            short_description (str):
                Optional. Short, subtitle-length description
                of the connector (e.g. shown beneath the
                connector name in list and detail views).
            author (str):
                Optional. The party that authored the
                connector, e.g. "Google" or a third-party
                provider name. Lets end users see who authored a
                connector.
            note (str):
                Optional. Free-form, multi-line note about
                the connector's capabilities or a custom note
                that can be set for the connector.
        """

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        short_description: str = proto.Field(
            proto.STRING,
            number=3,
        )
        author: str = proto.Field(
            proto.STRING,
            number=4,
        )
        note: str = proto.Field(
            proto.STRING,
            number=6,
        )

    params: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data_connector_params",
        message=struct_pb2.Struct,
    )
    json_params: str = proto.Field(
        proto.STRING,
        number=43,
        oneof="data_connector_params",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )
    remove_param_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=38,
    )
    refresh_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    next_sync_time: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=22,
        message=datetime_pb2.DateTime,
    )
    entities: MutableSequence[SourceEntity] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=SourceEntity,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    latest_pause_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )
    last_sync_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=19,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=20,
        message=timestamp_pb2.Timestamp,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=status_pb2.Status,
    )
    sync_mode: SyncMode = proto.Field(
        proto.ENUM,
        number=9,
        enum=SyncMode,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=32,
    )
    destination_configs: MutableSequence["DestinationConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="DestinationConfig",
    )
    action_state: State = proto.Field(
        proto.ENUM,
        number=37,
        enum=State,
    )
    action_config: "ActionConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ActionConfig",
    )
    end_user_config: EndUserConfig = proto.Field(
        proto.MESSAGE,
        number=30,
        message=EndUserConfig,
    )
    federated_config: FederatedConfig = proto.Field(
        proto.MESSAGE,
        number=41,
        message=FederatedConfig,
    )
    connector_modes: MutableSequence[ConnectorMode] = proto.RepeatedField(
        proto.ENUM,
        number=31,
        enum=ConnectorMode,
    )
    static_ip_enabled: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    static_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    oauth_static_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=50,
    )
    blocking_reasons: MutableSequence[BlockingReason] = proto.RepeatedField(
        proto.ENUM,
        number=16,
        enum=BlockingReason,
    )
    identity_schedule_config: "IdentityScheduleConfig" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="IdentityScheduleConfig",
    )
    private_connectivity_project_id: str = proto.Field(
        proto.STRING,
        number=17,
    )
    bap_config: "BAPConfig" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="BAPConfig",
    )
    connector_type: "ConnectorType" = proto.Field(
        proto.ENUM,
        number=25,
        enum="ConnectorType",
    )
    realtime_state: State = proto.Field(
        proto.ENUM,
        number=26,
        enum=State,
    )
    alert_policy_configs: MutableSequence["AlertPolicyConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message="AlertPolicyConfig",
    )
    realtime_sync_config: RealtimeSyncConfig = proto.Field(
        proto.MESSAGE,
        number=29,
        message=RealtimeSyncConfig,
    )
    acl_enabled: bool = proto.Field(
        proto.BOOL,
        number=33,
    )
    create_eua_saas: bool = proto.Field(
        proto.BOOL,
        number=34,
    )
    auto_run_disabled: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    incremental_sync_disabled: bool = proto.Field(
        proto.BOOL,
        number=35,
    )
    incremental_refresh_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=36,
        message=duration_pb2.Duration,
    )
    hybrid_ingestion_disabled: bool = proto.Field(
        proto.BOOL,
        number=40,
    )
    data_protection_policy: common.DataProtectionPolicy = proto.Field(
        proto.MESSAGE,
        number=44,
        message=common.DataProtectionPolicy,
    )
    egress_fqdns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=45,
    )
    vpcsc_enabled: bool = proto.Field(
        proto.BOOL,
        number=46,
    )
    dynamic_tools: MutableSequence["DynamicTool"] = proto.RepeatedField(
        proto.MESSAGE,
        number=47,
        message="DynamicTool",
    )
    cli_config: "CliConfig" = proto.Field(
        proto.MESSAGE,
        number=48,
        message="CliConfig",
    )
    connector_source_id: str = proto.Field(
        proto.STRING,
        number=49,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=51,
    )
    metadata: ConnectorMetadata = proto.Field(
        proto.MESSAGE,
        number=52,
        message=ConnectorMetadata,
    )


class DestinationConfig(proto.Message):
    r"""Defines target endpoints used to connect to third-party
    sources.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        params (google.protobuf.struct_pb2.Struct):
            Optional. Additional parameters for this
            destination config in structured json format.

            This field is a member of `oneof`_ ``destination_config_params``.
        json_params (str):
            Additional parameters for this destination
            config in json string format.

            This field is a member of `oneof`_ ``destination_config_params``.
        key (str):
            Optional. Unique destination identifier that
            is supported by the connector.
        destinations (MutableSequence[google.cloud.discoveryengine_v1.types.DestinationConfig.Destination]):
            Optional. The destinations for the
            corresponding key.
    """

    class Destination(proto.Message):
        r"""Defines a target endpoint

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            host (str):
                Publicly routable host.

                This field is a member of `oneof`_ ``destination``.
            port (int):
                Optional. Target port number accepted by the
                destination.
        """

        host: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="destination",
        )
        port: int = proto.Field(
            proto.INT32,
            number=2,
        )

    params: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination_config_params",
        message=struct_pb2.Struct,
    )
    json_params: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="destination_config_params",
    )
    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destinations: MutableSequence[Destination] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Destination,
    )


class ActionConfig(proto.Message):
    r"""Informations to support actions on the connector.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        action_params (google.protobuf.struct_pb2.Struct):
            Optional. Action parameters in structured
            json format.

            This field is a member of `oneof`_ ``action_config_params``.
        json_action_params (str):
            Optional. Action parameters in json string
            format.

            This field is a member of `oneof`_ ``action_config_params``.
        is_action_configured (bool):
            Output only. The connector contains the
            necessary parameters and is configured to
            support actions.
        service_name (str):
            Optional. The Service Directory resource name
            (projects/*/locations/*/namespaces/*/services/*)
            representing a VPC network endpoint used to connect to the
            data source's ``instance_uri``, defined in
            [DataConnector.params][google.cloud.discoveryengine.v1.DataConnector.params].

            Required when VPC Service Controls are enabled.
        use_static_secrets (bool):
            Optional. Whether to use static secrets for the connector.
            If true, the secrets provided in the action_params will be
            ignored.
        create_bap_connection (bool):
            Optional. Whether to create a BAP connection
            for the connector.
        user_defined_scopes_mapping (MutableMapping[str, google.cloud.discoveryengine_v1.types.ActionConfig.ScopeList]):
            Optional. Mapping from operation name to the
            list of scopes. Only be populated if there are
            user specified scopes.
    """

    class ScopeList(proto.Message):
        r"""Stores a list of scopes.

        Attributes:
            scopes (MutableSequence[str]):
                Optional. The list of scopes.
        """

        scopes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    action_params: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action_config_params",
        message=struct_pb2.Struct,
    )
    json_action_params: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="action_config_params",
    )
    is_action_configured: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    service_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    use_static_secrets: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    create_bap_connection: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    user_defined_scopes_mapping: MutableMapping[str, ScopeList] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=10,
        message=ScopeList,
    )


class IdentityScheduleConfig(proto.Message):
    r"""The configuration for the identity data synchronization runs.

    Attributes:
        refresh_interval (google.protobuf.duration_pb2.Duration):
            Optional. The refresh interval to sync the
            Access Control List information for the
            documents ingested by this connector. If not
            set, the access control list will be refreshed
            at the default interval of 30 minutes. The
            identity refresh interval can be at least 30
            minutes and at most 7 days.
        next_sync_time (google.type.datetime_pb2.DateTime):
            Optional. The UTC time when the next data
            sync is expected to start for the Data
            Connector. Customers are only able to specify
            the hour and minute to schedule the data sync.
            This is utilized when the data connector has a
            refresh interval greater than 1 day.
    """

    refresh_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    next_sync_time: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=datetime_pb2.DateTime,
    )


class BAPConfig(proto.Message):
    r"""The configuration for the BAP connector.

    Attributes:
        supported_connector_modes (MutableSequence[google.cloud.discoveryengine_v1.types.BAPConfig.ConnectorMode]):
            Required. The supported connector modes for
            the associated BAP connection.
        enabled_actions (MutableSequence[str]):
            Optional. The actions enabled on the
            associated BAP connection.
        toolspec_override (google.cloud.discoveryengine_v1.types.BAPConfig.ToolspecOverride):
            Optional. Custom toolspec overrides for this connection. For
            Enterprise BAP connectors that support admin-curated tool
            definitions, this holds the (simplified) per-tool overrides.
            On Get, populated by the server by merging persisted
            overrides with live runtime tool definitions and trimming
            the result for UI consumption. On Update, the supplied value
            replaces the persisted overrides after server-side
            validation and merging: the ``base_version`` field MUST
            match the server's current base toolspec version (otherwise
            the request is rejected with a user-facing error directing
            the admin to re-download the latest tools first).
    """

    class ConnectorMode(proto.Enum):
        r"""Use cases supported by this BAP connector.

        Values:
            CONNECTOR_MODE_UNSPECIFIED (0):
                Connector mode unspecified.
            DATA_INGESTION (1):
                Connector utilized for data ingestion.
            ACTIONS (2):
                Connector utilized for Actions
            END_USER_AUTHENTICATION (3):
                Connector utilized for End User
                Authentication.
        """

        CONNECTOR_MODE_UNSPECIFIED = 0
        DATA_INGESTION = 1
        ACTIONS = 2
        END_USER_AUTHENTICATION = 3

    class ToolspecOverride(proto.Message):
        r"""Customer-facing view of the admin-curated toolspec for a BAP
        connection. Holds the (simplified) per-tool definitions surfaced to
        and editable by the admin in the Discovery Engine UI.

        Mirrors the shape of the backend
        ``google.cloud.connectorexecution.v1.ToolspecOverride`` message, but
        is intentionally kept as a separate public type so the Discovery
        Engine API surface can evolve independently of the fed-API surface
        (AIP-215). Handlers convert between the two via helpers in
        //cloud/ml/discoveryengine/external_service/v1main/data_connector_service/lib:bap_custom_tool_util.

        Attributes:
            tools (MutableSequence[google.protobuf.struct_pb2.Struct]):
                Required. Tool definitions (one Struct per
                tool) that the admin has customised on top of
                the base toolspec returned by the fed API.
                REQUIRED because it is the only user-editable
                field in the modify API; the request must carry
                at least one tool.
            base_version (str):
                Required. Base toolspec version against which ``tools`` were
                authored. On Update, MUST match the server's current stable
                toolspec version for the connection; mismatch is rejected
                with a user-facing error directing the admin to re-download
                the latest tools first.
        """

        tools: MutableSequence[struct_pb2.Struct] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=struct_pb2.Struct,
        )
        base_version: str = proto.Field(
            proto.STRING,
            number=2,
        )

    supported_connector_modes: MutableSequence[ConnectorMode] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=ConnectorMode,
    )
    enabled_actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    toolspec_override: ToolspecOverride = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ToolspecOverride,
    )


class CliConfig(proto.Message):
    r"""The configuration for the CLI execution based connectors.

    Attributes:
        enabled_actions (MutableSequence[str]):
            Optional. The actions enabled on the
            associated CLI connection.
    """

    enabled_actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class AlertPolicyConfig(proto.Message):
    r"""The connector level alert config.

    Attributes:
        alert_policy_name (str):
            Immutable. The fully qualified resource name
            of the AlertPolicy.
        alert_enrollments (MutableSequence[google.cloud.discoveryengine_v1.types.AlertPolicyConfig.AlertEnrollment]):
            Optional. The enrollment states of each
            alert.
    """

    class AlertEnrollment(proto.Message):
        r"""The alert enrollment status.

        Attributes:
            alert_id (str):
                Immutable. The id of an alert.
            enroll_state (google.cloud.discoveryengine_v1.types.AlertPolicyConfig.AlertEnrollment.EnrollStates):
                Required. The enrollment status of a
                customer.
        """

        class EnrollStates(proto.Enum):
            r"""The enrollment status enum for the alert.

            Values:
                ENROLL_STATES_UNSPECIFIED (0):
                    Default value. Used for customers who have
                    not responded to the alert policy.
                ENROLLED (1):
                    Customer is enrolled in this policy.
                DECLINED (2):
                    Customer declined this policy.
            """

            ENROLL_STATES_UNSPECIFIED = 0
            ENROLLED = 1
            DECLINED = 2

        alert_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        enroll_state: "AlertPolicyConfig.AlertEnrollment.EnrollStates" = proto.Field(
            proto.ENUM,
            number=5,
            enum="AlertPolicyConfig.AlertEnrollment.EnrollStates",
        )

    alert_policy_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    alert_enrollments: MutableSequence[AlertEnrollment] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AlertEnrollment,
    )


class Tenant(proto.Message):
    r"""Tenant information for a connector source. This includes some
    of the same information stored in the Credential message, but is
    limited to only what is needed to provide a list of accessible
    tenants to the user.

    Attributes:
        id (str):
            The tenant's instance ID. Examples: Jira
            ("8594f221-9797-5f78-1fa4-485e198d7cd0"), Slack
            ("T123456").
        uri (str):
            The URI of the tenant, if applicable. For
            example, the URI of a Jira instance is
            https://my-jira-instance.atlassian.net, and a
            Slack tenant does not have a URI.
        display_name (str):
            Optional display name for the tenant, e.g.
            "My Slack Team".
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DynamicTool(proto.Message):
    r"""Configuration for dynamic tools.

    Attributes:
        name (str):
            Required. The name of the tool.
        description (str):
            Optional. The description of the tool.
        enabled (bool):
            Optional. Whether the tool is enabled.
        display_name (str):
            Optional. The display name of the tool.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
