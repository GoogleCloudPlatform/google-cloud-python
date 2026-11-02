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

from google.cloud.discoveryengine_v1beta.types import (
    cmek_config_service,
    common,
    schema,
)
from google.cloud.discoveryengine_v1beta.types import (
    document_processing_config as gcd_document_processing_config,
)

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "DataStore",
        "AdvancedSiteSearchConfig",
        "LanguageInfo",
        "NaturalLanguageQueryUnderstandingConfig",
        "WorkspaceConfig",
    },
)


class DataStore(proto.Message):
    r"""DataStore captures global settings and configs at the
    DataStore level.

    Attributes:
        name (str):
            Immutable. Identifier. The full resource name of the data
            store. Format:
            ``projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}``.

            This field must be a UTF-8 encoded string with a length
            limit of 1024 characters.
        display_name (str):
            Required. The data store display name.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.
        industry_vertical (google.cloud.discoveryengine_v1beta.types.IndustryVertical):
            Immutable. The industry vertical that the
            data store registers.
        solution_types (MutableSequence[google.cloud.discoveryengine_v1beta.types.SolutionType]):
            The solutions that the data store enrolls. Available
            solutions for each
            [industry_vertical][google.cloud.discoveryengine.v1beta.DataStore.industry_vertical]:

            - ``MEDIA``: ``SOLUTION_TYPE_RECOMMENDATION`` and
              ``SOLUTION_TYPE_SEARCH``.
            - ``SITE_SEARCH``: ``SOLUTION_TYPE_SEARCH`` is automatically
              enrolled. Other solutions cannot be enrolled.
        default_schema_id (str):
            Output only. The id of the default
            [Schema][google.cloud.discoveryengine.v1beta.Schema]
            associated to this data store.
        content_config (google.cloud.discoveryengine_v1beta.types.DataStore.ContentConfig):
            Immutable. The content config of the data store. If this
            field is unset, the server behavior defaults to
            [ContentConfig.NO_CONTENT][google.cloud.discoveryengine.v1beta.DataStore.ContentConfig.NO_CONTENT].
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the
            [DataStore][google.cloud.discoveryengine.v1beta.DataStore]
            was created at.
        advanced_site_search_config (google.cloud.discoveryengine_v1beta.types.AdvancedSiteSearchConfig):
            Optional. Configuration for advanced site
            search.
        language_info (google.cloud.discoveryengine_v1beta.types.LanguageInfo):
            Language info for DataStore.
        natural_language_query_understanding_config (google.cloud.discoveryengine_v1beta.types.NaturalLanguageQueryUnderstandingConfig):
            Optional. Configuration for Natural Language
            Query Understanding.
        kms_key_name (str):
            Input only. The KMS key to be used to protect this DataStore
            at creation time.

            Must be set for requests that need to comply with CMEK Org
            Policy protections.

            If this field is set and processed successfully, the
            DataStore will be protected by the KMS key, as indicated in
            the cmek_config field.
        cmek_config (google.cloud.discoveryengine_v1beta.types.CmekConfig):
            Output only. CMEK-related information for the
            DataStore.
        billing_estimation (google.cloud.discoveryengine_v1beta.types.DataStore.BillingEstimation):
            Output only. Data size estimation for
            billing.
        acl_enabled (bool):
            Immutable. Whether data in the
            [DataStore][google.cloud.discoveryengine.v1beta.DataStore]
            has ACL information. If set to ``true``, the source data
            must have ACL. ACL will be ingested when data is ingested by
            [DocumentService.ImportDocuments][google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments]
            methods.

            When ACL is enabled for the
            [DataStore][google.cloud.discoveryengine.v1beta.DataStore],
            [Document][google.cloud.discoveryengine.v1beta.Document]
            can't be accessed by calling
            [DocumentService.GetDocument][google.cloud.discoveryengine.v1beta.DocumentService.GetDocument]
            or
            [DocumentService.ListDocuments][google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments].

            Currently ACL is only supported in ``GENERIC`` industry
            vertical with non-``PUBLIC_WEBSITE`` content config.
        workspace_config (google.cloud.discoveryengine_v1beta.types.WorkspaceConfig):
            Config to store data store type configuration for workspace
            data. This must be set when
            [DataStore.content_config][google.cloud.discoveryengine.v1beta.DataStore.content_config]
            is set as
            [DataStore.ContentConfig.GOOGLE_WORKSPACE][google.cloud.discoveryengine.v1beta.DataStore.ContentConfig.GOOGLE_WORKSPACE].
        document_processing_config (google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig):
            Configuration for Document understanding and
            enrichment.
        starting_schema (google.cloud.discoveryengine_v1beta.types.Schema):
            The start schema to use for this
            [DataStore][google.cloud.discoveryengine.v1beta.DataStore]
            when provisioning it. If unset, a default vertical
            specialized schema will be used.

            This field is only used by
            [CreateDataStore][google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore]
            API, and will be ignored if used in other APIs. This field
            will be omitted from all API responses including
            [CreateDataStore][google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore]
            API. To retrieve a schema of a
            [DataStore][google.cloud.discoveryengine.v1beta.DataStore],
            use
            [SchemaService.GetSchema][google.cloud.discoveryengine.v1beta.SchemaService.GetSchema]
            API instead.

            The provided schema will be validated against certain rules
            on schema. Learn more from `this
            doc <https://cloud.google.com/generative-ai-app-builder/docs/provide-schema>`__.
        healthcare_fhir_config (google.cloud.discoveryengine_v1beta.types.HealthcareFhirConfig):
            Optional. Configuration for ``HEALTHCARE_FHIR`` vertical.
        serving_config_data_store (google.cloud.discoveryengine_v1beta.types.DataStore.ServingConfigDataStore):
            Optional. Stores serving config at DataStore
            level.
        identity_mapping_store (str):
            Immutable. The fully qualified resource name of the
            associated
            [IdentityMappingStore][google.cloud.discoveryengine.v1beta.IdentityMappingStore].
            This field can only be set for acl_enabled DataStores with
            ``THIRD_PARTY`` or ``GSUITE`` IdP. Format:
            ``projects/{project}/locations/{location}/identityMappingStores/{identity_mapping_store}``.
        is_infobot_faq_data_store (bool):
            Optional. If set, this DataStore is an
            Infobot FAQ DataStore.
        federated_search_config (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig):
            Optional. If set, this DataStore is a
            federated search DataStore.
        configurable_billing_approach (google.cloud.discoveryengine_v1beta.types.DataStore.ConfigurableBillingApproach):
            Optional. Configuration for configurable
            billing approach. See
        configurable_billing_approach_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when
            configurable_billing_approach was last updated.
    """

    class ContentConfig(proto.Enum):
        r"""Content config of the data store.

        Values:
            CONTENT_CONFIG_UNSPECIFIED (0):
                Default value.
            NO_CONTENT (1):
                Only contains documents without any
                [Document.content][google.cloud.discoveryengine.v1beta.Document.content].
            CONTENT_REQUIRED (2):
                Only contains documents with
                [Document.content][google.cloud.discoveryengine.v1beta.Document.content].
            PUBLIC_WEBSITE (3):
                The data store is used for public website
                search.
            GOOGLE_WORKSPACE (4):
                The data store is used for workspace search. Details of
                workspace data store are specified in the
                [WorkspaceConfig][google.cloud.discoveryengine.v1beta.WorkspaceConfig].
        """

        CONTENT_CONFIG_UNSPECIFIED = 0
        NO_CONTENT = 1
        CONTENT_REQUIRED = 2
        PUBLIC_WEBSITE = 3
        GOOGLE_WORKSPACE = 4

    class ConfigurableBillingApproach(proto.Enum):
        r"""Configuration for configurable billing approach.

        Values:
            CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED (0):
                Default value. For Spark and non-Spark
                non-configurable billing approach.
            CONFIGURABLE_SUBSCRIPTION_INDEXING_CORE (1):
                Use the subscription base + overage billing
                for indexing core for non embedding storage.
            CONFIGURABLE_CONSUMPTION_EMBEDDING (2):
                Use the consumption pay-as-you-go billing for
                embedding storage add-on.
        """

        CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED = 0
        CONFIGURABLE_SUBSCRIPTION_INDEXING_CORE = 1
        CONFIGURABLE_CONSUMPTION_EMBEDDING = 2

    class BillingEstimation(proto.Message):
        r"""Estimation of data size per data store.

        Attributes:
            structured_data_size (int):
                Data size for structured data in terms of
                bytes.
            unstructured_data_size (int):
                Data size for unstructured data in terms of
                bytes.
            website_data_size (int):
                Data size for websites in terms of bytes.
            structured_data_update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last updated timestamp for structured data.
            unstructured_data_update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last updated timestamp for unstructured data.
            website_data_update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last updated timestamp for websites.
        """

        structured_data_size: int = proto.Field(
            proto.INT64,
            number=1,
        )
        unstructured_data_size: int = proto.Field(
            proto.INT64,
            number=2,
        )
        website_data_size: int = proto.Field(
            proto.INT64,
            number=3,
        )
        structured_data_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        unstructured_data_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        website_data_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )

    class ServingConfigDataStore(proto.Message):
        r"""Stores information regarding the serving configurations at
        DataStore level.

        Attributes:
            disabled_for_serving (bool):
                Optional. If set true, the DataStore will not
                be available for serving search requests.
        """

        disabled_for_serving: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class FederatedSearchConfig(proto.Message):
        r"""Stores information for federated search.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            alloy_db_config (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig):
                AlloyDB config. If set, this DataStore is
                connected to AlloyDB.

                This field is a member of `oneof`_ ``data_source_config``.
            third_party_oauth_config (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.ThirdPartyOauthConfig):
                Third Party OAuth config. If set, this
                DataStore is connected to a third party
                application.

                This field is a member of `oneof`_ ``data_source_config``.
            notebooklm_config (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.NotebooklmConfig):
                NotebookLM config. If set, this DataStore is
                connected to NotebookLM Enterprise.

                This field is a member of `oneof`_ ``data_source_config``.
        """

        class AlloyDbConfig(proto.Message):
            r"""Stores information for connecting to AlloyDB.

            Attributes:
                alloydb_connection_config (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig):
                    Required. Configuration for connecting to
                    AlloyDB.
                alloydb_ai_nl_config (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbAiNaturalLanguageConfig):
                    Optional. Configuration for Magic.
                returned_fields (MutableSequence[str]):
                    Optional. Fields to be returned in the search
                    results. If empty, all fields will be returned.
            """

            class AlloyDbConnectionConfig(proto.Message):
                r"""Configuration for connecting to AlloyDB.

                Attributes:
                    instance (str):
                        Required. The AlloyDB instance to connect to.
                    database (str):
                        Required. The AlloyDB database to connect to.
                    user (str):
                        Required. Database user.

                        If auth_mode = END_USER_ACCOUNT, it can be unset. In that
                        case, the user will be inferred on the AlloyDB side, based
                        on the authenticated user.
                    password (str):
                        Required. Database password.

                        If auth_mode = END_USER_ACCOUNT, it can be unset. In that
                        case, the password will be inferred on the AlloyDB side,
                        based on the authenticated user.
                    auth_mode (google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig.AuthMode):
                        Optional. Auth mode.
                    enable_psvs (bool):
                        Optional. If true, enable PSVS for AlloyDB.
                """

                class AuthMode(proto.Enum):
                    r"""Auth mode.

                    Values:
                        AUTH_MODE_UNSPECIFIED (0):
                            No description available.
                        AUTH_MODE_SERVICE_ACCOUNT (1):
                            Uses P4SA when VAIS talks to AlloyDB.
                        AUTH_MODE_END_USER_ACCOUNT (2):
                            Uses EUC when VAIS talks to AlloyDB.
                    """

                    AUTH_MODE_UNSPECIFIED = 0
                    AUTH_MODE_SERVICE_ACCOUNT = 1
                    AUTH_MODE_END_USER_ACCOUNT = 2

                instance: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                database: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                user: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                password: str = proto.Field(
                    proto.STRING,
                    number=4,
                )
                auth_mode: "DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig.AuthMode" = proto.Field(
                    proto.ENUM,
                    number=5,
                    enum="DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig.AuthMode",
                )
                enable_psvs: bool = proto.Field(
                    proto.BOOL,
                    number=6,
                )

            class AlloyDbAiNaturalLanguageConfig(proto.Message):
                r"""Configuration for AlloyDB AI Natural Language.

                Attributes:
                    nl_config_id (str):
                        Optional. AlloyDb AI NL config id, i.e. the value that was
                        used for calling
                        ``SELECT alloydb_ai_nl.g_create_configuration(...)``. Can be
                        empty.
                """

                nl_config_id: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            alloydb_connection_config: "DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig",
            )
            alloydb_ai_nl_config: "DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbAiNaturalLanguageConfig" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbAiNaturalLanguageConfig",
            )
            returned_fields: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )

        class ThirdPartyOauthConfig(proto.Message):
            r"""Stores information for third party applicationOAuth.

            Attributes:
                app_name (str):
                    Optional. The type of the application. E.g.,
                    "jira", "box", etc.
                instance_name (str):
                    Optional. The instance name identifying the 3P app, e.g.,
                    "vaissptbots-my". This is different from the instance_uri
                    which is the full URL of the 3P app e.g.,
                    "https://vaissptbots-my.sharepoint.com".
            """

            app_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            instance_name: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class NotebooklmConfig(proto.Message):
            r"""Config for connecting to NotebookLM Enterprise.

            Attributes:
                search_config (str):
                    Required. Search config name.

                    Format:
                    projects/*/locations/global/notebookLmSearchConfigs/*
            """

            search_config: str = proto.Field(
                proto.STRING,
                number=1,
            )

        alloy_db_config: "DataStore.FederatedSearchConfig.AlloyDbConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="data_source_config",
            message="DataStore.FederatedSearchConfig.AlloyDbConfig",
        )
        third_party_oauth_config: "DataStore.FederatedSearchConfig.ThirdPartyOauthConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="data_source_config",
            message="DataStore.FederatedSearchConfig.ThirdPartyOauthConfig",
        )
        notebooklm_config: "DataStore.FederatedSearchConfig.NotebooklmConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="data_source_config",
                message="DataStore.FederatedSearchConfig.NotebooklmConfig",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    industry_vertical: common.IndustryVertical = proto.Field(
        proto.ENUM,
        number=3,
        enum=common.IndustryVertical,
    )
    solution_types: MutableSequence[common.SolutionType] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum=common.SolutionType,
    )
    default_schema_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    content_config: ContentConfig = proto.Field(
        proto.ENUM,
        number=6,
        enum=ContentConfig,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    advanced_site_search_config: "AdvancedSiteSearchConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AdvancedSiteSearchConfig",
    )
    language_info: "LanguageInfo" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="LanguageInfo",
    )
    natural_language_query_understanding_config: "NaturalLanguageQueryUnderstandingConfig" = proto.Field(
        proto.MESSAGE,
        number=34,
        message="NaturalLanguageQueryUnderstandingConfig",
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=32,
    )
    cmek_config: cmek_config_service.CmekConfig = proto.Field(
        proto.MESSAGE,
        number=18,
        message=cmek_config_service.CmekConfig,
    )
    billing_estimation: BillingEstimation = proto.Field(
        proto.MESSAGE,
        number=23,
        message=BillingEstimation,
    )
    acl_enabled: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    workspace_config: "WorkspaceConfig" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="WorkspaceConfig",
    )
    document_processing_config: gcd_document_processing_config.DocumentProcessingConfig = proto.Field(
        proto.MESSAGE,
        number=27,
        message=gcd_document_processing_config.DocumentProcessingConfig,
    )
    starting_schema: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=28,
        message=schema.Schema,
    )
    healthcare_fhir_config: common.HealthcareFhirConfig = proto.Field(
        proto.MESSAGE,
        number=29,
        message=common.HealthcareFhirConfig,
    )
    serving_config_data_store: ServingConfigDataStore = proto.Field(
        proto.MESSAGE,
        number=30,
        message=ServingConfigDataStore,
    )
    identity_mapping_store: str = proto.Field(
        proto.STRING,
        number=31,
    )
    is_infobot_faq_data_store: bool = proto.Field(
        proto.BOOL,
        number=37,
    )
    federated_search_config: FederatedSearchConfig = proto.Field(
        proto.MESSAGE,
        number=38,
        message=FederatedSearchConfig,
    )
    configurable_billing_approach: ConfigurableBillingApproach = proto.Field(
        proto.ENUM,
        number=45,
        enum=ConfigurableBillingApproach,
    )
    configurable_billing_approach_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=46,
        message=timestamp_pb2.Timestamp,
    )


class AdvancedSiteSearchConfig(proto.Message):
    r"""Configuration data for advance site search.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        disable_initial_index (bool):
            If set true, initial indexing is disabled for
            the DataStore.

            This field is a member of `oneof`_ ``_disable_initial_index``.
        disable_automatic_refresh (bool):
            If set true, automatic refresh is disabled
            for the DataStore.

            This field is a member of `oneof`_ ``_disable_automatic_refresh``.
    """

    disable_initial_index: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    disable_automatic_refresh: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


class LanguageInfo(proto.Message):
    r"""Language info for DataStore.

    Attributes:
        language_code (str):
            The language code for the DataStore.
        normalized_language_code (str):
            Output only. This is the normalized form of language_code.
            E.g.: language_code of ``en-GB``, ``en_GB``, ``en-UK`` or
            ``en-gb`` will have normalized_language_code of ``en-GB``.
        language (str):
            Output only. Language part of normalized_language_code.
            E.g.: ``en-US`` -> ``en``, ``zh-Hans-HK`` -> ``zh``, ``en``
            -> ``en``.
        region (str):
            Output only. Region part of normalized_language_code, if
            present. E.g.: ``en-US`` -> ``US``, ``zh-Hans-HK`` ->
            ``HK``, ``en`` -> \`\`.
    """

    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    normalized_language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region: str = proto.Field(
        proto.STRING,
        number=4,
    )


class NaturalLanguageQueryUnderstandingConfig(proto.Message):
    r"""Configuration for Natural Language Query Understanding.

    Attributes:
        mode (google.cloud.discoveryengine_v1beta.types.NaturalLanguageQueryUnderstandingConfig.Mode):
            Mode of Natural Language Query Understanding. If this field
            is unset, the behavior defaults to
            [NaturalLanguageQueryUnderstandingConfig.Mode.DISABLED][google.cloud.discoveryengine.v1beta.NaturalLanguageQueryUnderstandingConfig.Mode.DISABLED].
    """

    class Mode(proto.Enum):
        r"""Mode of Natural Language Query Understanding. When the
        NaturalLanguageQueryUnderstandingConfig.Mode is ENABLED, the
        natural language understanding capabilities will be enabled for
        a search request if the
        NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition
        in the SearchRequest is ENABLED.

        Values:
            MODE_UNSPECIFIED (0):
                Default value.
            DISABLED (1):
                Natural Language Query Understanding is
                disabled.
            ENABLED (2):
                Natural Language Query Understanding is
                enabled.
        """

        MODE_UNSPECIFIED = 0
        DISABLED = 1
        ENABLED = 2

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )


class WorkspaceConfig(proto.Message):
    r"""Config to store data store type configuration for workspace
    data

    Attributes:
        type_ (google.cloud.discoveryengine_v1beta.types.WorkspaceConfig.Type):
            The Google Workspace data source.
        dasher_customer_id (str):
            Output only. Obfuscated Dasher customer ID.
            Derived by the server from the project's GCP
            organization at data store creation time; any
            value supplied in the request payload is
            ignored.
        super_admin_service_account (str):
            Optional. The super admin service account for
            the workspace that will be used for access token
            generation. For now we only use it for Native
            Google Drive connector data ingestion.
        super_admin_email_address (str):
            Optional. The super admin email address for
            the workspace that will be used for access token
            generation. For now we only use it for Native
            Google Drive connector data ingestion.
    """

    class Type(proto.Enum):
        r"""Specifies the type of Workspace App supported by this
        DataStore

        Values:
            TYPE_UNSPECIFIED (0):
                Defaults to an unspecified Workspace type.
            GOOGLE_DRIVE (1):
                Workspace Data Store contains Drive data
            GOOGLE_MAIL (2):
                Workspace Data Store contains Mail data
            GOOGLE_SITES (3):
                Workspace Data Store contains Sites data
            GOOGLE_CALENDAR (4):
                Workspace Data Store contains Calendar data
            GOOGLE_CHAT (5):
                Workspace Data Store contains Chat data
            GOOGLE_GROUPS (6):
                Workspace Data Store contains Groups data
            GOOGLE_KEEP (7):
                Workspace Data Store contains Keep data
            GOOGLE_PEOPLE (8):
                Workspace Data Store contains People data
        """

        TYPE_UNSPECIFIED = 0
        GOOGLE_DRIVE = 1
        GOOGLE_MAIL = 2
        GOOGLE_SITES = 3
        GOOGLE_CALENDAR = 4
        GOOGLE_CHAT = 5
        GOOGLE_GROUPS = 6
        GOOGLE_KEEP = 7
        GOOGLE_PEOPLE = 8

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    dasher_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    super_admin_service_account: str = proto.Field(
        proto.STRING,
        number=4,
    )
    super_admin_email_address: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
