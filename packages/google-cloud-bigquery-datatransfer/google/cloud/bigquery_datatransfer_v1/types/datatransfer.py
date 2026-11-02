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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bigquery_datatransfer_v1.types import transfer

__protobuf__ = proto.module(
    package="google.cloud.bigquery.datatransfer.v1",
    manifest={
        "DataSourceParameter",
        "DataSource",
        "GetDataSourceRequest",
        "ListDataSourcesRequest",
        "ListDataSourcesResponse",
        "CreateTransferConfigRequest",
        "UpdateTransferConfigRequest",
        "GetTransferConfigRequest",
        "DeleteTransferConfigRequest",
        "GetTransferRunRequest",
        "DeleteTransferRunRequest",
        "ListTransferConfigsRequest",
        "ListTransferConfigsResponse",
        "ListTransferRunsRequest",
        "ListTransferRunsResponse",
        "ListTransferLogsRequest",
        "ListTransferLogsResponse",
        "CheckValidCredsRequest",
        "CheckValidCredsResponse",
        "ScheduleTransferRunsRequest",
        "ScheduleTransferRunsResponse",
        "StartManualTransferRunsRequest",
        "StartManualTransferRunsResponse",
        "EnrollDataSourcesRequest",
        "UnenrollDataSourcesRequest",
    },
)


class DataSourceParameter(proto.Message):
    r"""A parameter used to define custom fields in a data source
    definition.

    Attributes:
        param_id (str):
            Parameter identifier.
        display_name (str):
            Parameter display name in the user interface.
        description (str):
            Parameter description.
        type_ (google.cloud.bigquery_datatransfer_v1.types.DataSourceParameter.Type):
            Parameter type.
        required (bool):
            Is parameter required.
        repeated (bool):
            Deprecated. This field has no effect.
        validation_regex (str):
            Regular expression which can be used for
            parameter validation.
        allowed_values (MutableSequence[str]):
            All possible values for the parameter.
        min_value (google.protobuf.wrappers_pb2.DoubleValue):
            For integer and double values specifies
            minimum allowed value.
        max_value (google.protobuf.wrappers_pb2.DoubleValue):
            For integer and double values specifies
            maximum allowed value.
        fields (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.DataSourceParameter]):
            Deprecated. This field has no effect.
        validation_description (str):
            Description of the requirements for this
            field, in case the user input does not fulfill
            the regex pattern or min/max values.
        validation_help_url (str):
            URL to a help document to further explain the
            naming requirements.
        immutable (bool):
            Cannot be changed after initial creation.
        recurse (bool):
            Deprecated. This field has no effect.
        deprecated (bool):
            If true, it should not be used in new
            transfers, and it should not be visible to
            users.
    """

    class Type(proto.Enum):
        r"""Parameter type.

        Values:
            TYPE_UNSPECIFIED (0):
                Type unspecified.
            STRING (1):
                String parameter.
            INTEGER (2):
                Integer parameter (64-bits).
                Will be serialized to json as string.
            DOUBLE (3):
                Double precision floating point parameter.
            BOOLEAN (4):
                Boolean parameter.
            RECORD (5):
                Deprecated. This field has no effect.
            PLUS_PAGE (6):
                Page ID for a Google+ Page.
            LIST (7):
                List of strings parameter.
        """

        TYPE_UNSPECIFIED = 0
        STRING = 1
        INTEGER = 2
        DOUBLE = 3
        BOOLEAN = 4
        RECORD = 5
        PLUS_PAGE = 6
        LIST = 7

    param_id: str = proto.Field(
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
    type_: Type = proto.Field(
        proto.ENUM,
        number=4,
        enum=Type,
    )
    required: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    repeated: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    validation_regex: str = proto.Field(
        proto.STRING,
        number=7,
    )
    allowed_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    min_value: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.DoubleValue,
    )
    max_value: wrappers_pb2.DoubleValue = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.DoubleValue,
    )
    fields: MutableSequence["DataSourceParameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="DataSourceParameter",
    )
    validation_description: str = proto.Field(
        proto.STRING,
        number=12,
    )
    validation_help_url: str = proto.Field(
        proto.STRING,
        number=13,
    )
    immutable: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    recurse: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    deprecated: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class DataSource(proto.Message):
    r"""Defines the properties and custom parameters for a data
    source.

    Attributes:
        name (str):
            Output only. Data source resource name.
        data_source_id (str):
            Data source id.
        display_name (str):
            User friendly data source name.
        description (str):
            User friendly data source description string.
        client_id (str):
            Data source client id which should be used to
            receive refresh token.
        scopes (MutableSequence[str]):
            Api auth scopes for which refresh token needs
            to be obtained. These are scopes needed by a
            data source to prepare data and ingest them into
            BigQuery, e.g.,
            https://www.googleapis.com/auth/bigquery
        transfer_type (google.cloud.bigquery_datatransfer_v1.types.TransferType):
            Deprecated. This field has no effect.
        supports_multiple_transfers (bool):
            Deprecated. This field has no effect.
        update_deadline_seconds (int):
            The number of seconds to wait for an update
            from the data source before the Data Transfer
            Service marks the transfer as FAILED.
        default_schedule (str):
            Default data transfer schedule. Examples of valid schedules
            include: ``1st,3rd monday of month 15:30``,
            ``every wed,fri of jan,jun 13:15``, and
            ``first sunday of quarter 00:00``.
        supports_custom_schedule (bool):
            Specifies whether the data source supports a user defined
            schedule, or operates on the default schedule. When set to
            ``true``, user can override default schedule.
        parameters (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.DataSourceParameter]):
            Data source parameters.
        help_url (str):
            Url for the help document for this data
            source.
        authorization_type (google.cloud.bigquery_datatransfer_v1.types.DataSource.AuthorizationType):
            Indicates the type of authorization.
        data_refresh_type (google.cloud.bigquery_datatransfer_v1.types.DataSource.DataRefreshType):
            Specifies whether the data source supports
            automatic data refresh for the past few days,
            and how it's supported. For some data sources,
            data might not be complete until a few days
            later, so it's useful to refresh data
            automatically.
        default_data_refresh_window_days (int):
            Default data refresh window on days. Only meaningful when
            ``data_refresh_type`` = ``SLIDING_WINDOW``.
        manual_runs_disabled (bool):
            Disables backfilling and manual run
            scheduling for the data source.
        minimum_schedule_interval (google.protobuf.duration_pb2.Duration):
            The minimum interval for scheduler to
            schedule runs.
    """

    class AuthorizationType(proto.Enum):
        r"""The type of authorization needed for this data source.

        Values:
            AUTHORIZATION_TYPE_UNSPECIFIED (0):
                Type unspecified.
            AUTHORIZATION_CODE (1):
                Use OAuth 2 authorization codes that can be
                exchanged for a refresh token on the backend.
            GOOGLE_PLUS_AUTHORIZATION_CODE (2):
                Return an authorization code for a given
                Google+ page that can then be exchanged for a
                refresh token on the backend.
            FIRST_PARTY_OAUTH (3):
                Use First Party OAuth.
        """

        AUTHORIZATION_TYPE_UNSPECIFIED = 0
        AUTHORIZATION_CODE = 1
        GOOGLE_PLUS_AUTHORIZATION_CODE = 2
        FIRST_PARTY_OAUTH = 3

    class DataRefreshType(proto.Enum):
        r"""Represents how the data source supports data auto refresh.

        Values:
            DATA_REFRESH_TYPE_UNSPECIFIED (0):
                The data source won't support data auto
                refresh, which is default value.
            SLIDING_WINDOW (1):
                The data source supports data auto refresh,
                and runs will be scheduled for the past few
                days. Does not allow custom values to be set for
                each transfer config.
            CUSTOM_SLIDING_WINDOW (2):
                The data source supports data auto refresh,
                and runs will be scheduled for the past few
                days. Allows custom values to be set for each
                transfer config.
        """

        DATA_REFRESH_TYPE_UNSPECIFIED = 0
        SLIDING_WINDOW = 1
        CUSTOM_SLIDING_WINDOW = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    transfer_type: transfer.TransferType = proto.Field(
        proto.ENUM,
        number=7,
        enum=transfer.TransferType,
    )
    supports_multiple_transfers: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    update_deadline_seconds: int = proto.Field(
        proto.INT32,
        number=9,
    )
    default_schedule: str = proto.Field(
        proto.STRING,
        number=10,
    )
    supports_custom_schedule: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    parameters: MutableSequence["DataSourceParameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="DataSourceParameter",
    )
    help_url: str = proto.Field(
        proto.STRING,
        number=13,
    )
    authorization_type: AuthorizationType = proto.Field(
        proto.ENUM,
        number=14,
        enum=AuthorizationType,
    )
    data_refresh_type: DataRefreshType = proto.Field(
        proto.ENUM,
        number=15,
        enum=DataRefreshType,
    )
    default_data_refresh_window_days: int = proto.Field(
        proto.INT32,
        number=16,
    )
    manual_runs_disabled: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    minimum_schedule_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=18,
        message=duration_pb2.Duration,
    )


class GetDataSourceRequest(proto.Message):
    r"""A request to get data source info.

    Attributes:
        name (str):
            Required. The field will contain name of the resource
            requested, for example:
            ``projects/{project_id}/dataSources/{data_source_id}`` or
            ``projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataSourcesRequest(proto.Message):
    r"""Request to list supported data sources and their data
    transfer settings.

    Attributes:
        parent (str):
            Required. The BigQuery project id for which data sources
            should be returned. Must be in the form:
            ``projects/{project_id}`` or
            ``projects/{project_id}/locations/{location_id}``
        page_token (str):
            Pagination token, which can be used to request a specific
            page of ``ListDataSourcesRequest`` list results. For
            multiple-page results, ``ListDataSourcesResponse`` outputs a
            ``next_page`` token, which can be used as the ``page_token``
            value to request the next page of list results.
        page_size (int):
            Page size. The default page size is the
            maximum value of 1000 results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListDataSourcesResponse(proto.Message):
    r"""Returns list of supported data sources and their metadata.

    Attributes:
        data_sources (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.DataSource]):
            List of supported data sources and their
            transfer settings.
        next_page_token (str):
            Output only. The next-pagination token. For multiple-page
            list results, this token can be used as the
            ``ListDataSourcesRequest.page_token`` to request the next
            page of list results.
    """

    @property
    def raw_page(self):
        return self

    data_sources: MutableSequence["DataSource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataSource",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateTransferConfigRequest(proto.Message):
    r"""A request to create a data transfer configuration. If new
    credentials are needed for this transfer configuration,
    authorization info must be provided. If authorization info is
    provided, the transfer configuration will be associated with the
    user id corresponding to the authorization info. Otherwise, the
    transfer configuration will be associated with the calling user.

    When using a cross project service account for creating a transfer
    config, you must enable cross project service account usage. For
    more information, see `Disable attachment of service accounts to
    resources in other
    projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.

    Attributes:
        parent (str):
            Required. The BigQuery project id where the transfer
            configuration should be created. Must be in the format
            projects/{project_id}/locations/{location_id} or
            projects/{project_id}. If specified location and location of
            the destination bigquery dataset do not match - the request
            will fail.
        transfer_config (google.cloud.bigquery_datatransfer_v1.types.TransferConfig):
            Required. Data transfer configuration to
            create.
        authorization_code (str):
            Deprecated: Authorization code was required when
            ``transferConfig.dataSourceId`` is 'youtube_channel' but it
            is no longer used in any data sources. Use ``version_info``
            instead.

            Optional OAuth2 authorization code to use with this transfer
            configuration. This is required only if
            ``transferConfig.dataSourceId`` is 'youtube_channel' and new
            credentials are needed, as indicated by ``CheckValidCreds``.
            In order to obtain authorization_code, make a request to the
            following URL:

            .. raw:: html

                <pre class="prettyprint" suppresswarning="true">
                https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=<var>client_id</var>&scope=<var>data_source_scopes</var>
                </pre>

            - The client_id is the OAuth client_id of the data source as
              returned by ListDataSources method.
            - data_source_scopes are the scopes returned by
              ListDataSources method.

            Note that this should not be set when
            ``service_account_name`` is used to create the transfer
            config.
        version_info (str):
            Optional version info. This parameter replaces
            ``authorization_code`` which is no longer used in any data
            sources. This is required only if
            ``transferConfig.dataSourceId`` is 'youtube_channel' *or*
            new credentials are needed, as indicated by
            ``CheckValidCreds``. In order to obtain version info, make a
            request to the following URL:

            .. raw:: html

                <pre class="prettyprint" suppresswarning="true">
                https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=version_info&client_id=<var>client_id</var>&scope=<var>data_source_scopes</var>
                </pre>

            - The client_id is the OAuth client_id of the data source as
              returned by ListDataSources method.
            - data_source_scopes are the scopes returned by
              ListDataSources method.

            Note that this should not be set when
            ``service_account_name`` is used to create the transfer
            config.
        service_account_name (str):
            Optional service account email. If this field is set, the
            transfer config will be created with this service account's
            credentials. It requires that the requesting user calling
            this API has permissions to act as this service account.

            Note that not all data sources support service account
            credentials when creating a transfer config. For the latest
            list of data sources, read about `using service
            accounts <https://cloud.google.com/bigquery-transfer/docs/use-service-accounts>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    transfer_config: transfer.TransferConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=transfer.TransferConfig,
    )
    authorization_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version_info: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_account_name: str = proto.Field(
        proto.STRING,
        number=6,
    )


class UpdateTransferConfigRequest(proto.Message):
    r"""A request to update a transfer configuration. To update the user id
    of the transfer configuration, authorization info needs to be
    provided.

    When using a cross project service account for updating a transfer
    config, you must enable cross project service account usage. For
    more information, see `Disable attachment of service accounts to
    resources in other
    projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.

    Attributes:
        transfer_config (google.cloud.bigquery_datatransfer_v1.types.TransferConfig):
            Required. Data transfer configuration to
            create.
        authorization_code (str):
            Deprecated: Authorization code was required when
            ``transferConfig.dataSourceId`` is 'youtube_channel' but it
            is no longer used in any data sources. Use ``version_info``
            instead.

            Optional OAuth2 authorization code to use with this transfer
            configuration. This is required only if
            ``transferConfig.dataSourceId`` is 'youtube_channel' and new
            credentials are needed, as indicated by ``CheckValidCreds``.
            In order to obtain authorization_code, make a request to the
            following URL:

            .. raw:: html

                <pre class="prettyprint" suppresswarning="true">
                https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=<var>client_id</var>&scope=<var>data_source_scopes</var>
                </pre>

            - The client_id is the OAuth client_id of the data source as
              returned by ListDataSources method.
            - data_source_scopes are the scopes returned by
              ListDataSources method.

            Note that this should not be set when
            ``service_account_name`` is used to update the transfer
            config.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Required list of fields to be
            updated in this request.
        version_info (str):
            Optional version info. This parameter replaces
            ``authorization_code`` which is no longer used in any data
            sources. This is required only if
            ``transferConfig.dataSourceId`` is 'youtube_channel' *or*
            new credentials are needed, as indicated by
            ``CheckValidCreds``. In order to obtain version info, make a
            request to the following URL:

            .. raw:: html

                <pre class="prettyprint" suppresswarning="true">
                https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=version_info&client_id=<var>client_id</var>&scope=<var>data_source_scopes</var>
                </pre>

            - The client_id is the OAuth client_id of the data source as
              returned by ListDataSources method.
            - data_source_scopes are the scopes returned by
              ListDataSources method.

            Note that this should not be set when
            ``service_account_name`` is used to update the transfer
            config.
        service_account_name (str):
            Optional service account email. If this field is set, the
            transfer config will be created with this service account's
            credentials. It requires that the requesting user calling
            this API has permissions to act as this service account.

            Note that not all data sources support service account
            credentials when creating a transfer config. For the latest
            list of data sources, read about `using service
            accounts <https://cloud.google.com/bigquery-transfer/docs/use-service-accounts>`__.
    """

    transfer_config: transfer.TransferConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferConfig,
    )
    authorization_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    version_info: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_account_name: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GetTransferConfigRequest(proto.Message):
    r"""A request to get data transfer information.

    Attributes:
        name (str):
            Required. The field will contain name of the resource
            requested, for example:
            ``projects/{project_id}/transferConfigs/{config_id}`` or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteTransferConfigRequest(proto.Message):
    r"""A request to delete data transfer information. All associated
    transfer runs and log messages will be deleted as well.

    Attributes:
        name (str):
            Required. The field will contain name of the resource
            requested, for example:
            ``projects/{project_id}/transferConfigs/{config_id}`` or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetTransferRunRequest(proto.Message):
    r"""A request to get data transfer run information.

    Attributes:
        name (str):
            Required. The field will contain name of the resource
            requested, for example:
            ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
            or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteTransferRunRequest(proto.Message):
    r"""A request to delete data transfer run information.

    Attributes:
        name (str):
            Required. The field will contain name of the resource
            requested, for example:
            ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
            or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTransferConfigsRequest(proto.Message):
    r"""A request to list data transfers configured for a BigQuery
    project.

    Attributes:
        parent (str):
            Required. The BigQuery project id for which transfer configs
            should be returned: ``projects/{project_id}`` or
            ``projects/{project_id}/locations/{location_id}``
        data_source_ids (MutableSequence[str]):
            When specified, only configurations of
            requested data sources are returned.
        page_token (str):
            Pagination token, which can be used to request a specific
            page of ``ListTransfersRequest`` list results. For
            multiple-page results, ``ListTransfersResponse`` outputs a
            ``next_page`` token, which can be used as the ``page_token``
            value to request the next page of list results.
        page_size (int):
            Page size. The default page size is the
            maximum value of 1000 results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListTransferConfigsResponse(proto.Message):
    r"""The returned list of pipelines in the project.

    Attributes:
        transfer_configs (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferConfig]):
            Output only. The stored pipeline transfer
            configurations.
        next_page_token (str):
            Output only. The next-pagination token. For multiple-page
            list results, this token can be used as the
            ``ListTransferConfigsRequest.page_token`` to request the
            next page of list results.
    """

    @property
    def raw_page(self):
        return self

    transfer_configs: MutableSequence[transfer.TransferConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTransferRunsRequest(proto.Message):
    r"""A request to list data transfer runs.

    Attributes:
        parent (str):
            Required. Name of transfer configuration for which transfer
            runs should be retrieved. Format of transfer configuration
            resource name is:
            ``projects/{project_id}/transferConfigs/{config_id}`` or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.
        states (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferState]):
            When specified, only transfer runs with
            requested states are returned.
        page_token (str):
            Pagination token, which can be used to request a specific
            page of ``ListTransferRunsRequest`` list results. For
            multiple-page results, ``ListTransferRunsResponse`` outputs
            a ``next_page`` token, which can be used as the
            ``page_token`` value to request the next page of list
            results.
        page_size (int):
            Page size. The default page size is the
            maximum value of 1000 results.
        run_attempt (google.cloud.bigquery_datatransfer_v1.types.ListTransferRunsRequest.RunAttempt):
            Indicates how run attempts are to be pulled.
    """

    class RunAttempt(proto.Enum):
        r"""Represents which runs should be pulled.

        Values:
            RUN_ATTEMPT_UNSPECIFIED (0):
                All runs should be returned.
            LATEST (1):
                Only latest run per day should be returned.
        """

        RUN_ATTEMPT_UNSPECIFIED = 0
        LATEST = 1

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    states: MutableSequence[transfer.TransferState] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=transfer.TransferState,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    run_attempt: RunAttempt = proto.Field(
        proto.ENUM,
        number=5,
        enum=RunAttempt,
    )


class ListTransferRunsResponse(proto.Message):
    r"""The returned list of pipelines in the project.

    Attributes:
        transfer_runs (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferRun]):
            Output only. The stored pipeline transfer
            runs.
        next_page_token (str):
            Output only. The next-pagination token. For multiple-page
            list results, this token can be used as the
            ``ListTransferRunsRequest.page_token`` to request the next
            page of list results.
    """

    @property
    def raw_page(self):
        return self

    transfer_runs: MutableSequence[transfer.TransferRun] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferRun,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTransferLogsRequest(proto.Message):
    r"""A request to get user facing log messages associated with
    data transfer run.

    Attributes:
        parent (str):
            Required. Transfer run name in the form:
            ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
            or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``
        page_token (str):
            Pagination token, which can be used to request a specific
            page of ``ListTransferLogsRequest`` list results. For
            multiple-page results, ``ListTransferLogsResponse`` outputs
            a ``next_page`` token, which can be used as the
            ``page_token`` value to request the next page of list
            results.
        page_size (int):
            Page size. The default page size is the
            maximum value of 1000 results.
        message_types (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferMessage.MessageSeverity]):
            Message types to return. If not populated -
            INFO, WARNING and ERROR messages are returned.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    message_types: MutableSequence[transfer.TransferMessage.MessageSeverity] = (
        proto.RepeatedField(
            proto.ENUM,
            number=6,
            enum=transfer.TransferMessage.MessageSeverity,
        )
    )


class ListTransferLogsResponse(proto.Message):
    r"""The returned list transfer run messages.

    Attributes:
        transfer_messages (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferMessage]):
            Output only. The stored pipeline transfer
            messages.
        next_page_token (str):
            Output only. The next-pagination token. For multiple-page
            list results, this token can be used as the
            ``GetTransferRunLogRequest.page_token`` to request the next
            page of list results.
    """

    @property
    def raw_page(self):
        return self

    transfer_messages: MutableSequence[transfer.TransferMessage] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferMessage,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CheckValidCredsRequest(proto.Message):
    r"""A request to determine whether the user has valid
    credentials. This method is used to limit the number of OAuth
    popups in the user interface. The user id is inferred from the
    API call context.
    If the data source has the Google+ authorization type, this
    method returns false, as it cannot be determined whether the
    credentials are already valid merely based on the user id.

    Attributes:
        name (str):
            Required. The data source in the form:
            ``projects/{project_id}/dataSources/{data_source_id}`` or
            ``projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CheckValidCredsResponse(proto.Message):
    r"""A response indicating whether the credentials exist and are
    valid.

    Attributes:
        has_valid_creds (bool):
            If set to ``true``, the credentials exist and are valid.
    """

    has_valid_creds: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ScheduleTransferRunsRequest(proto.Message):
    r"""A request to schedule transfer runs for a time range.

    Attributes:
        parent (str):
            Required. Transfer configuration name in the form:
            ``projects/{project_id}/transferConfigs/{config_id}`` or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Start time of the range of transfer runs. For
            example, ``"2017-05-25T00:00:00+00:00"``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. End time of the range of transfer runs. For
            example, ``"2017-05-30T00:00:00+00:00"``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class ScheduleTransferRunsResponse(proto.Message):
    r"""A response to schedule transfer runs for a time range.

    Attributes:
        runs (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferRun]):
            The transfer runs that were scheduled.
    """

    runs: MutableSequence[transfer.TransferRun] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferRun,
    )


class StartManualTransferRunsRequest(proto.Message):
    r"""A request to start manual transfer runs.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Transfer configuration name in the form:
            ``projects/{project_id}/transferConfigs/{config_id}`` or
            ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.
        requested_time_range (google.cloud.bigquery_datatransfer_v1.types.StartManualTransferRunsRequest.TimeRange):
            A time_range start and end timestamp for historical data
            files or reports that are scheduled to be transferred by the
            scheduled transfer run. requested_time_range must be a past
            time and cannot include future time values.

            This field is a member of `oneof`_ ``time``.
        requested_run_time (google.protobuf.timestamp_pb2.Timestamp):
            A run_time timestamp for historical data files or reports
            that are scheduled to be transferred by the scheduled
            transfer run. requested_run_time must be a past time and
            cannot include future time values.

            This field is a member of `oneof`_ ``time``.
    """

    class TimeRange(proto.Message):
        r"""A specification for a time range, this will request transfer runs
        with run_time between start_time (inclusive) and end_time
        (exclusive).

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start time of the range of transfer runs. For example,
                ``"2017-05-25T00:00:00+00:00"``. The start_time must be
                strictly less than the end_time. Creates transfer runs where
                run_time is in the range between start_time (inclusive) and
                end_time (exclusive).
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                End time of the range of transfer runs. For example,
                ``"2017-05-30T00:00:00+00:00"``. The end_time must not be in
                the future. Creates transfer runs where run_time is in the
                range between start_time (inclusive) and end_time
                (exclusive).
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requested_time_range: TimeRange = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="time",
        message=TimeRange,
    )
    requested_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="time",
        message=timestamp_pb2.Timestamp,
    )


class StartManualTransferRunsResponse(proto.Message):
    r"""A response to start manual transfer runs.

    Attributes:
        runs (MutableSequence[google.cloud.bigquery_datatransfer_v1.types.TransferRun]):
            The transfer runs that were created.
    """

    runs: MutableSequence[transfer.TransferRun] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferRun,
    )


class EnrollDataSourcesRequest(proto.Message):
    r"""A request to enroll a set of data sources so they are visible in the
    BigQuery UI's ``Transfer`` tab.

    Attributes:
        name (str):
            Required. The name of the project resource in the form:
            ``projects/{project_id}``
        data_source_ids (MutableSequence[str]):
            Data sources that are enrolled. It is
            required to provide at least one data source id.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class UnenrollDataSourcesRequest(proto.Message):
    r"""A request to unenroll a set of data sources so they are no longer
    visible in the BigQuery UI's ``Transfer`` tab.

    Attributes:
        name (str):
            Required. The name of the project resource in the form:
            ``projects/{project_id}``
        data_source_ids (MutableSequence[str]):
            Data sources that are unenrolled. It is
            required to provide at least one data source id.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
