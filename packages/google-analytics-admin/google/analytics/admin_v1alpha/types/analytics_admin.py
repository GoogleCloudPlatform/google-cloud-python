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

from google.analytics.admin_v1alpha.types import (
    access_report,
    event_create_and_edit,
    resources,
)
from google.analytics.admin_v1alpha.types import audience as gaa_audience
from google.analytics.admin_v1alpha.types import channel_group as gaa_channel_group
from google.analytics.admin_v1alpha.types import (
    expanded_data_set as gaa_expanded_data_set,
)
from google.analytics.admin_v1alpha.types import (
    subproperty_event_filter as gaa_subproperty_event_filter,
)

__protobuf__ = proto.module(
    package="google.analytics.admin.v1alpha",
    manifest={
        "RunAccessReportRequest",
        "RunAccessReportResponse",
        "GetAccountRequest",
        "ListAccountsRequest",
        "ListAccountsResponse",
        "DeleteAccountRequest",
        "UpdateAccountRequest",
        "ProvisionAccountTicketRequest",
        "ProvisionAccountTicketResponse",
        "GetPropertyRequest",
        "ListPropertiesRequest",
        "ListPropertiesResponse",
        "UpdatePropertyRequest",
        "CreatePropertyRequest",
        "DeletePropertyRequest",
        "CreateFirebaseLinkRequest",
        "DeleteFirebaseLinkRequest",
        "ListFirebaseLinksRequest",
        "ListFirebaseLinksResponse",
        "GetGlobalSiteTagRequest",
        "CreateGoogleAdsLinkRequest",
        "UpdateGoogleAdsLinkRequest",
        "DeleteGoogleAdsLinkRequest",
        "ListGoogleAdsLinksRequest",
        "ListGoogleAdsLinksResponse",
        "GetDataSharingSettingsRequest",
        "ListAccountSummariesRequest",
        "ListAccountSummariesResponse",
        "AcknowledgeUserDataCollectionRequest",
        "AcknowledgeUserDataCollectionResponse",
        "SearchChangeHistoryEventsRequest",
        "SearchChangeHistoryEventsResponse",
        "GetMeasurementProtocolSecretRequest",
        "CreateMeasurementProtocolSecretRequest",
        "DeleteMeasurementProtocolSecretRequest",
        "UpdateMeasurementProtocolSecretRequest",
        "ListMeasurementProtocolSecretsRequest",
        "ListMeasurementProtocolSecretsResponse",
        "GetSKAdNetworkConversionValueSchemaRequest",
        "CreateSKAdNetworkConversionValueSchemaRequest",
        "DeleteSKAdNetworkConversionValueSchemaRequest",
        "UpdateSKAdNetworkConversionValueSchemaRequest",
        "ListSKAdNetworkConversionValueSchemasRequest",
        "ListSKAdNetworkConversionValueSchemasResponse",
        "GetGoogleSignalsSettingsRequest",
        "UpdateGoogleSignalsSettingsRequest",
        "CreateConversionEventRequest",
        "UpdateConversionEventRequest",
        "GetConversionEventRequest",
        "DeleteConversionEventRequest",
        "ListConversionEventsRequest",
        "ListConversionEventsResponse",
        "CreateKeyEventRequest",
        "UpdateKeyEventRequest",
        "GetKeyEventRequest",
        "DeleteKeyEventRequest",
        "ListKeyEventsRequest",
        "ListKeyEventsResponse",
        "GetDisplayVideo360AdvertiserLinkRequest",
        "ListDisplayVideo360AdvertiserLinksRequest",
        "ListDisplayVideo360AdvertiserLinksResponse",
        "CreateDisplayVideo360AdvertiserLinkRequest",
        "DeleteDisplayVideo360AdvertiserLinkRequest",
        "UpdateDisplayVideo360AdvertiserLinkRequest",
        "GetDisplayVideo360AdvertiserLinkProposalRequest",
        "ListDisplayVideo360AdvertiserLinkProposalsRequest",
        "ListDisplayVideo360AdvertiserLinkProposalsResponse",
        "CreateDisplayVideo360AdvertiserLinkProposalRequest",
        "DeleteDisplayVideo360AdvertiserLinkProposalRequest",
        "ApproveDisplayVideo360AdvertiserLinkProposalRequest",
        "ApproveDisplayVideo360AdvertiserLinkProposalResponse",
        "CancelDisplayVideo360AdvertiserLinkProposalRequest",
        "GetSearchAds360LinkRequest",
        "ListSearchAds360LinksRequest",
        "ListSearchAds360LinksResponse",
        "CreateSearchAds360LinkRequest",
        "DeleteSearchAds360LinkRequest",
        "UpdateSearchAds360LinkRequest",
        "CreateCustomDimensionRequest",
        "UpdateCustomDimensionRequest",
        "ListCustomDimensionsRequest",
        "ListCustomDimensionsResponse",
        "ArchiveCustomDimensionRequest",
        "GetCustomDimensionRequest",
        "CreateCustomMetricRequest",
        "UpdateCustomMetricRequest",
        "ListCustomMetricsRequest",
        "ListCustomMetricsResponse",
        "ArchiveCustomMetricRequest",
        "GetCustomMetricRequest",
        "CreateCalculatedMetricRequest",
        "UpdateCalculatedMetricRequest",
        "DeleteCalculatedMetricRequest",
        "ListCalculatedMetricsRequest",
        "ListCalculatedMetricsResponse",
        "GetCalculatedMetricRequest",
        "GetDataRetentionSettingsRequest",
        "UpdateDataRetentionSettingsRequest",
        "CreateDataStreamRequest",
        "DeleteDataStreamRequest",
        "UpdateDataStreamRequest",
        "ListDataStreamsRequest",
        "ListDataStreamsResponse",
        "GetDataStreamRequest",
        "GetAudienceRequest",
        "ListAudiencesRequest",
        "ListAudiencesResponse",
        "CreateAudienceRequest",
        "UpdateAudienceRequest",
        "ArchiveAudienceRequest",
        "GetAttributionSettingsRequest",
        "UpdateAttributionSettingsRequest",
        "GetAccessBindingRequest",
        "BatchGetAccessBindingsRequest",
        "BatchGetAccessBindingsResponse",
        "ListAccessBindingsRequest",
        "ListAccessBindingsResponse",
        "CreateAccessBindingRequest",
        "BatchCreateAccessBindingsRequest",
        "BatchCreateAccessBindingsResponse",
        "UpdateAccessBindingRequest",
        "BatchUpdateAccessBindingsRequest",
        "BatchUpdateAccessBindingsResponse",
        "DeleteAccessBindingRequest",
        "BatchDeleteAccessBindingsRequest",
        "CreateExpandedDataSetRequest",
        "UpdateExpandedDataSetRequest",
        "DeleteExpandedDataSetRequest",
        "GetExpandedDataSetRequest",
        "ListExpandedDataSetsRequest",
        "ListExpandedDataSetsResponse",
        "CreateChannelGroupRequest",
        "UpdateChannelGroupRequest",
        "DeleteChannelGroupRequest",
        "GetChannelGroupRequest",
        "ListChannelGroupsRequest",
        "ListChannelGroupsResponse",
        "CreateBigQueryLinkRequest",
        "GetBigQueryLinkRequest",
        "ListBigQueryLinksRequest",
        "ListBigQueryLinksResponse",
        "UpdateBigQueryLinkRequest",
        "DeleteBigQueryLinkRequest",
        "GetEnhancedMeasurementSettingsRequest",
        "UpdateEnhancedMeasurementSettingsRequest",
        "GetDataRedactionSettingsRequest",
        "UpdateDataRedactionSettingsRequest",
        "CreateAdSenseLinkRequest",
        "GetAdSenseLinkRequest",
        "DeleteAdSenseLinkRequest",
        "ListAdSenseLinksRequest",
        "ListAdSenseLinksResponse",
        "CreateEventCreateRuleRequest",
        "UpdateEventCreateRuleRequest",
        "DeleteEventCreateRuleRequest",
        "GetEventCreateRuleRequest",
        "ListEventCreateRulesRequest",
        "ListEventCreateRulesResponse",
        "CreateEventEditRuleRequest",
        "UpdateEventEditRuleRequest",
        "DeleteEventEditRuleRequest",
        "GetEventEditRuleRequest",
        "ListEventEditRulesRequest",
        "ListEventEditRulesResponse",
        "ReorderEventEditRulesRequest",
        "CreateRollupPropertyRequest",
        "CreateRollupPropertyResponse",
        "GetRollupPropertySourceLinkRequest",
        "ListRollupPropertySourceLinksRequest",
        "ListRollupPropertySourceLinksResponse",
        "CreateRollupPropertySourceLinkRequest",
        "DeleteRollupPropertySourceLinkRequest",
        "ProvisionSubpropertyRequest",
        "ProvisionSubpropertyResponse",
        "CreateSubpropertyEventFilterRequest",
        "GetSubpropertyEventFilterRequest",
        "ListSubpropertyEventFiltersRequest",
        "ListSubpropertyEventFiltersResponse",
        "UpdateSubpropertyEventFilterRequest",
        "DeleteSubpropertyEventFilterRequest",
        "CreateReportingDataAnnotationRequest",
        "GetReportingDataAnnotationRequest",
        "ListReportingDataAnnotationsRequest",
        "ListReportingDataAnnotationsResponse",
        "UpdateReportingDataAnnotationRequest",
        "DeleteReportingDataAnnotationRequest",
        "SubmitUserDeletionRequest",
        "SubmitUserDeletionResponse",
        "GetSubpropertySyncConfigRequest",
        "ListSubpropertySyncConfigsRequest",
        "ListSubpropertySyncConfigsResponse",
        "UpdateSubpropertySyncConfigRequest",
        "GetReportingIdentitySettingsRequest",
        "UpdateReportingIdentitySettingsRequest",
        "GetUserProvidedDataSettingsRequest",
    },
)


class RunAccessReportRequest(proto.Message):
    r"""The request for a Data Access Record Report.

    Attributes:
        entity (str):
            The Data Access Report supports requesting at
            the property level or account level. If
            requested at the account level, Data Access
            Reports include all access for all properties
            under that account.

            To request at the property level, entity should
            be for example 'properties/123' if "123" is your
            Google Analytics property ID. To request at the
            account level, entity should be for example
            'accounts/1234' if "1234" is your Google
            Analytics Account ID.
        dimensions (MutableSequence[google.analytics.admin_v1alpha.types.AccessDimension]):
            The dimensions requested and displayed in the
            response. Requests are allowed up to 9
            dimensions.
        metrics (MutableSequence[google.analytics.admin_v1alpha.types.AccessMetric]):
            The metrics requested and displayed in the
            response. Requests are allowed up to 10 metrics.
        date_ranges (MutableSequence[google.analytics.admin_v1alpha.types.AccessDateRange]):
            Date ranges of access records to read. If
            multiple date ranges are requested, each
            response row will contain a zero based date
            range index. If two date ranges overlap, the
            access records for the overlapping days is
            included in the response rows for both date
            ranges. Requests are allowed up to 2 date
            ranges.
        dimension_filter (google.analytics.admin_v1alpha.types.AccessFilterExpression):
            Dimension filters let you restrict report response to
            specific dimension values which match the filter. For
            example, filtering on access records of a single user. To
            learn more, see `Fundamentals of Dimension
            Filters <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters>`__
            for examples. Metrics cannot be used in this filter.
        metric_filter (google.analytics.admin_v1alpha.types.AccessFilterExpression):
            Metric filters allow you to restrict report
            response to specific metric values which match
            the filter. Metric filters are applied after
            aggregating the report's rows, similar to SQL
            having-clause. Dimensions cannot be used in this
            filter.
        offset (int):
            The row count of the start row. The first row is counted as
            row 0. If offset is unspecified, it is treated as 0. If
            offset is zero, then this method will return the first page
            of results with ``limit`` entries.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        limit (int):
            The number of rows to return. If unspecified, 10,000 rows
            are returned. The API returns a maximum of 100,000 rows per
            request, no matter how many you ask for. ``limit`` must be
            positive.

            The API may return fewer rows than the requested ``limit``,
            if there aren't as many remaining rows as the ``limit``. For
            instance, there are fewer than 300 possible values for the
            dimension ``country``, so when reporting on only
            ``country``, you can't get more than 300 rows, even if you
            set ``limit`` to a higher value.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        time_zone (str):
            This request's time zone if specified. If unspecified, the
            property's time zone is used. The request's time zone is
            used to interpret the start & end dates of the report.

            Formatted as strings from the IANA Time Zone database
            (https://www.iana.org/time-zones); for example
            "America/New_York" or "Asia/Tokyo".
        order_bys (MutableSequence[google.analytics.admin_v1alpha.types.AccessOrderBy]):
            Specifies how rows are ordered in the
            response.
        return_entity_quota (bool):
            Toggles whether to return the current state of this
            Analytics Property's quota. Quota is returned in
            `AccessQuota <#AccessQuota>`__. For account-level requests,
            this field must be false.
        include_all_users (bool):
            Optional. Determines whether to include users
            who have never made an API call in the response.
            If true, all users with access to the specified
            property or account are included in the
            response, regardless of whether they have made
            an API call or not. If false, only the users who
            have made an API call will be included.
        expand_groups (bool):
            Optional. Decides whether to return the users within user
            groups. This field works only when include_all_users is set
            to true. If true, it will return all users with access to
            the specified property or account. If false, only the users
            with direct access will be returned.
    """

    entity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableSequence[access_report.AccessDimension] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=access_report.AccessDimension,
    )
    metrics: MutableSequence[access_report.AccessMetric] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=access_report.AccessMetric,
    )
    date_ranges: MutableSequence[access_report.AccessDateRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=access_report.AccessDateRange,
    )
    dimension_filter: access_report.AccessFilterExpression = proto.Field(
        proto.MESSAGE,
        number=5,
        message=access_report.AccessFilterExpression,
    )
    metric_filter: access_report.AccessFilterExpression = proto.Field(
        proto.MESSAGE,
        number=6,
        message=access_report.AccessFilterExpression,
    )
    offset: int = proto.Field(
        proto.INT64,
        number=7,
    )
    limit: int = proto.Field(
        proto.INT64,
        number=8,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=9,
    )
    order_bys: MutableSequence[access_report.AccessOrderBy] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=access_report.AccessOrderBy,
    )
    return_entity_quota: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    include_all_users: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    expand_groups: bool = proto.Field(
        proto.BOOL,
        number=13,
    )


class RunAccessReportResponse(proto.Message):
    r"""The customized Data Access Record Report response.

    Attributes:
        dimension_headers (MutableSequence[google.analytics.admin_v1alpha.types.AccessDimensionHeader]):
            The header for a column in the report that
            corresponds to a specific dimension. The number
            of DimensionHeaders and ordering of
            DimensionHeaders matches the dimensions present
            in rows.
        metric_headers (MutableSequence[google.analytics.admin_v1alpha.types.AccessMetricHeader]):
            The header for a column in the report that
            corresponds to a specific metric. The number of
            MetricHeaders and ordering of MetricHeaders
            matches the metrics present in rows.
        rows (MutableSequence[google.analytics.admin_v1alpha.types.AccessRow]):
            Rows of dimension value combinations and
            metric values in the report.
        row_count (int):
            The total number of rows in the query result. ``rowCount``
            is independent of the number of rows returned in the
            response, the ``limit`` request parameter, and the
            ``offset`` request parameter. For example if a query returns
            175 rows and includes ``limit`` of 50 in the API request,
            the response will contain ``rowCount`` of 175 but only 50
            rows.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        quota (google.analytics.admin_v1alpha.types.AccessQuota):
            The quota state for this Analytics property
            including this request. This field doesn't work
            with account-level requests.
    """

    dimension_headers: MutableSequence[access_report.AccessDimensionHeader] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=access_report.AccessDimensionHeader,
        )
    )
    metric_headers: MutableSequence[access_report.AccessMetricHeader] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=access_report.AccessMetricHeader,
        )
    )
    rows: MutableSequence[access_report.AccessRow] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=access_report.AccessRow,
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    quota: access_report.AccessQuota = proto.Field(
        proto.MESSAGE,
        number=5,
        message=access_report.AccessQuota,
    )


class GetAccountRequest(proto.Message):
    r"""Request message for GetAccount RPC.

    Attributes:
        name (str):
            Required. The name of the account to lookup.
            Format: accounts/{account}
            Example: "accounts/100".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAccountsRequest(proto.Message):
    r"""Request message for ListAccounts RPC.

    Attributes:
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccounts`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListAccounts`` must match the call that
            provided the page token.
        show_deleted (bool):
            Whether to include soft-deleted (ie:
            "trashed") Accounts in the results. Accounts can
            be inspected to determine whether they are
            deleted or not.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListAccountsResponse(proto.Message):
    r"""Request message for ListAccounts RPC.

    Attributes:
        accounts (MutableSequence[google.analytics.admin_v1alpha.types.Account]):
            Results that were accessible to the caller.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    accounts: MutableSequence[resources.Account] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Account,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAccountRequest(proto.Message):
    r"""Request message for DeleteAccount RPC.

    Attributes:
        name (str):
            Required. The name of the Account to
            soft-delete. Format: accounts/{account}
            Example: "accounts/100".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAccountRequest(proto.Message):
    r"""Request message for UpdateAccount RPC.

    Attributes:
        account (google.analytics.admin_v1alpha.types.Account):
            Required. The account to update. The account's ``name``
            field is used to identify the account.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    account: resources.Account = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Account,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ProvisionAccountTicketRequest(proto.Message):
    r"""Request message for ProvisionAccountTicket RPC.

    Attributes:
        account (google.analytics.admin_v1alpha.types.Account):
            The account to create.
        redirect_uri (str):
            Redirect URI where the user will be sent
            after accepting Terms of Service. Must be
            configured in Cloud Console as a Redirect URI.
    """

    account: resources.Account = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Account,
    )
    redirect_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProvisionAccountTicketResponse(proto.Message):
    r"""Response message for ProvisionAccountTicket RPC.

    Attributes:
        account_ticket_id (str):
            The param to be passed in the ToS link.
    """

    account_ticket_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetPropertyRequest(proto.Message):
    r"""Request message for GetProperty RPC.

    Attributes:
        name (str):
            Required. The name of the property to lookup. Format:
            properties/{property_id} Example: "properties/1000".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPropertiesRequest(proto.Message):
    r"""Request message for ListProperties RPC.

    Attributes:
        filter (str):
            Required. An expression for filtering the results of the
            request. Fields eligible for filtering are:
            ``parent:``\ (The resource name of the parent
            account/property) or ``ancestor:``\ (The resource name of
            the parent account) or ``firebase_project:``\ (The id or
            number of the linked firebase project). Some examples of
            filters:

            ::

               | Filter                      | Description                               |
               |-----------------------------|-------------------------------------------|
               | parent:accounts/123         | The account with account id: 123.       |
               | parent:properties/123       | The property with property id: 123.       |
               | ancestor:accounts/123       | The account with account id: 123.         |
               | firebase_project:project-id | The firebase project with id: project-id. |
               | firebase_project:123        | The firebase project with number: 123.    |
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListProperties`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListProperties`` must match the call that
            provided the page token.
        show_deleted (bool):
            Whether to include soft-deleted (ie:
            "trashed") Properties in the results. Properties
            can be inspected to determine whether they are
            deleted or not.
    """

    filter: str = proto.Field(
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
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListPropertiesResponse(proto.Message):
    r"""Response message for ListProperties RPC.

    Attributes:
        properties (MutableSequence[google.analytics.admin_v1alpha.types.Property]):
            Results that matched the filter criteria and
            were accessible to the caller.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    properties: MutableSequence[resources.Property] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Property,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdatePropertyRequest(proto.Message):
    r"""Request message for UpdateProperty RPC.

    Attributes:
        property (google.analytics.admin_v1alpha.types.Property):
            Required. The property to update. The property's ``name``
            field is used to identify the property to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    property: resources.Property = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Property,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreatePropertyRequest(proto.Message):
    r"""Request message for CreateProperty RPC.

    Attributes:
        property (google.analytics.admin_v1alpha.types.Property):
            Required. The property to create.
            Note: the supplied property must specify its
            parent.
    """

    property: resources.Property = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Property,
    )


class DeletePropertyRequest(proto.Message):
    r"""Request message for DeleteProperty RPC.

    Attributes:
        name (str):
            Required. The name of the Property to soft-delete. Format:
            properties/{property_id} Example: "properties/1000".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFirebaseLinkRequest(proto.Message):
    r"""Request message for CreateFirebaseLink RPC

    Attributes:
        parent (str):
            Required. Format: properties/{property_id}

            Example: ``properties/1234``
        firebase_link (google.analytics.admin_v1alpha.types.FirebaseLink):
            Required. The Firebase link to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    firebase_link: resources.FirebaseLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.FirebaseLink,
    )


class DeleteFirebaseLinkRequest(proto.Message):
    r"""Request message for DeleteFirebaseLink RPC

    Attributes:
        name (str):
            Required. Format:
            properties/{property_id}/firebaseLinks/{firebase_link_id}

            Example: ``properties/1234/firebaseLinks/5678``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFirebaseLinksRequest(proto.Message):
    r"""Request message for ListFirebaseLinks RPC

    Attributes:
        parent (str):
            Required. Format: properties/{property_id}

            Example: ``properties/1234``
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListFirebaseLinks`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListFirebaseLinks`` must match the call that
            provided the page token.
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


class ListFirebaseLinksResponse(proto.Message):
    r"""Response message for ListFirebaseLinks RPC

    Attributes:
        firebase_links (MutableSequence[google.analytics.admin_v1alpha.types.FirebaseLink]):
            List of FirebaseLinks. This will have at most
            one value.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. Currently, Google Analytics supports only one
            FirebaseLink per property, so this will never be populated.
    """

    @property
    def raw_page(self):
        return self

    firebase_links: MutableSequence[resources.FirebaseLink] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.FirebaseLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetGlobalSiteTagRequest(proto.Message):
    r"""Request message for GetGlobalSiteTag RPC.

    Attributes:
        name (str):
            Required. The name of the site tag to lookup. Note that site
            tags are singletons and do not have unique IDs. Format:
            properties/{property_id}/dataStreams/{stream_id}/globalSiteTag

            Example: ``properties/123/dataStreams/456/globalSiteTag``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGoogleAdsLinkRequest(proto.Message):
    r"""Request message for CreateGoogleAdsLink RPC

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        google_ads_link (google.analytics.admin_v1alpha.types.GoogleAdsLink):
            Required. The GoogleAdsLink to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    google_ads_link: resources.GoogleAdsLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.GoogleAdsLink,
    )


class UpdateGoogleAdsLinkRequest(proto.Message):
    r"""Request message for UpdateGoogleAdsLink RPC

    Attributes:
        google_ads_link (google.analytics.admin_v1alpha.types.GoogleAdsLink):
            The GoogleAdsLink to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    google_ads_link: resources.GoogleAdsLink = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.GoogleAdsLink,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteGoogleAdsLinkRequest(proto.Message):
    r"""Request message for DeleteGoogleAdsLink RPC.

    Attributes:
        name (str):
            Required. Example format:
            properties/1234/googleAdsLinks/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGoogleAdsLinksRequest(proto.Message):
    r"""Request message for ListGoogleAdsLinks RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 50 resources
            will be returned. The maximum value is 200
            (higher values will be coerced to the maximum).
        page_token (str):
            Optional. A page token, received from a previous
            ``ListGoogleAdsLinks`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListGoogleAdsLinks`` must match the call that provided the
            page token.
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


class ListGoogleAdsLinksResponse(proto.Message):
    r"""Response message for ListGoogleAdsLinks RPC.

    Attributes:
        google_ads_links (MutableSequence[google.analytics.admin_v1alpha.types.GoogleAdsLink]):
            List of GoogleAdsLinks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    google_ads_links: MutableSequence[resources.GoogleAdsLink] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.GoogleAdsLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDataSharingSettingsRequest(proto.Message):
    r"""Request message for GetDataSharingSettings RPC.

    Attributes:
        name (str):
            Required. The name of the settings to lookup. Format:
            accounts/{account}/dataSharingSettings

            Example: ``accounts/1000/dataSharingSettings``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAccountSummariesRequest(proto.Message):
    r"""Request message for ListAccountSummaries RPC.

    Attributes:
        page_size (int):
            Optional. The maximum number of
            AccountSummary resources to return. The service
            may return fewer than this value, even if there
            are additional pages. If unspecified, at most 50
            resources will be returned. The maximum value is
            200; (higher values will be coerced to the
            maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccountSummaries`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListAccountSummaries`` must match the call
            that provided the page token.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAccountSummariesResponse(proto.Message):
    r"""Response message for ListAccountSummaries RPC.

    Attributes:
        account_summaries (MutableSequence[google.analytics.admin_v1alpha.types.AccountSummary]):
            Account summaries of all accounts the caller
            has access to.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    account_summaries: MutableSequence[resources.AccountSummary] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AccountSummary,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AcknowledgeUserDataCollectionRequest(proto.Message):
    r"""Request message for AcknowledgeUserDataCollection RPC.

    Attributes:
        property (str):
            Required. The property for which to
            acknowledge user data collection.
        acknowledgement (str):
            Required. An acknowledgement that the caller
            of this method understands the terms of user
            data collection.

            This field must contain the exact value:

            "I acknowledge that I have the necessary privacy
            disclosures and rights from my end users for the
            collection and processing of their data,
            including the association of such data with the
            visitation information Google Analytics collects
            from my site and/or app property.".
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acknowledgement: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AcknowledgeUserDataCollectionResponse(proto.Message):
    r"""Response message for AcknowledgeUserDataCollection RPC."""


class SearchChangeHistoryEventsRequest(proto.Message):
    r"""Request message for SearchChangeHistoryEvents RPC.

    Attributes:
        account (str):
            Required. The account resource for which to return change
            history resources. Format: accounts/{account}

            Example: ``accounts/100``
        property (str):
            Optional. Resource name for a child property. If set, only
            return changes made to this property or its child resources.
            Format: properties/{propertyId}

            Example: ``properties/100``
        resource_type (MutableSequence[google.analytics.admin_v1alpha.types.ChangeHistoryResourceType]):
            Optional. If set, only return changes if they
            are for a resource that matches at least one of
            these types.
        action (MutableSequence[google.analytics.admin_v1alpha.types.ActionType]):
            Optional. If set, only return changes that
            match one or more of these types of actions.
        actor_email (MutableSequence[str]):
            Optional. If set, only return changes if they
            are made by a user in this list.
        earliest_change_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. If set, only return changes made
            after this time (inclusive).
        latest_change_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. If set, only return changes made
            before this time (inclusive).
        page_size (int):
            Optional. The maximum number of ChangeHistoryEvent items to
            return. If unspecified, at most 50 items will be returned.
            The maximum value is 200 (higher values will be coerced to
            the maximum).

            Note that the service may return a page with fewer items
            than this value specifies (potentially even zero), and that
            there still may be additional pages. If you want a
            particular number of items, you'll need to continue
            requesting additional pages using ``page_token`` until you
            get the needed number.
        page_token (str):
            Optional. A page token, received from a previous
            ``SearchChangeHistoryEvents`` call. Provide this to retrieve
            the subsequent page. When paginating, all other parameters
            provided to ``SearchChangeHistoryEvents`` must match the
            call that provided the page token.
    """

    account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    property: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_type: MutableSequence[resources.ChangeHistoryResourceType] = (
        proto.RepeatedField(
            proto.ENUM,
            number=3,
            enum=resources.ChangeHistoryResourceType,
        )
    )
    action: MutableSequence[resources.ActionType] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=resources.ActionType,
    )
    actor_email: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    earliest_change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    latest_change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=8,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=9,
    )


class SearchChangeHistoryEventsResponse(proto.Message):
    r"""Response message for SearchAccounts RPC.

    Attributes:
        change_history_events (MutableSequence[google.analytics.admin_v1alpha.types.ChangeHistoryEvent]):
            Results that were accessible to the caller.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    change_history_events: MutableSequence[resources.ChangeHistoryEvent] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.ChangeHistoryEvent,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMeasurementProtocolSecretRequest(proto.Message):
    r"""Request message for GetMeasurementProtocolSecret RPC.

    Attributes:
        name (str):
            Required. The name of the measurement
            protocol secret to lookup. Format:

            properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMeasurementProtocolSecretRequest(proto.Message):
    r"""Request message for CreateMeasurementProtocolSecret RPC

    Attributes:
        parent (str):
            Required. The parent resource where this
            secret will be created. Format:
            properties/{property}/dataStreams/{dataStream}
        measurement_protocol_secret (google.analytics.admin_v1alpha.types.MeasurementProtocolSecret):
            Required. The measurement protocol secret to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    measurement_protocol_secret: resources.MeasurementProtocolSecret = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.MeasurementProtocolSecret,
    )


class DeleteMeasurementProtocolSecretRequest(proto.Message):
    r"""Request message for DeleteMeasurementProtocolSecret RPC

    Attributes:
        name (str):
            Required. The name of the
            MeasurementProtocolSecret to delete. Format:

            properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateMeasurementProtocolSecretRequest(proto.Message):
    r"""Request message for UpdateMeasurementProtocolSecret RPC

    Attributes:
        measurement_protocol_secret (google.analytics.admin_v1alpha.types.MeasurementProtocolSecret):
            Required. The measurement protocol secret to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated.
            Omitted fields will not be updated.
    """

    measurement_protocol_secret: resources.MeasurementProtocolSecret = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.MeasurementProtocolSecret,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListMeasurementProtocolSecretsRequest(proto.Message):
    r"""Request message for ListMeasurementProtocolSecret RPC

    Attributes:
        parent (str):
            Required. The resource name of the parent
            stream. Format:

            properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 10 resources
            will be returned. The maximum value is 10.
            Higher values will be coerced to the maximum.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMeasurementProtocolSecrets`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListMeasurementProtocolSecrets``
            must match the call that provided the page token.
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


class ListMeasurementProtocolSecretsResponse(proto.Message):
    r"""Response message for ListMeasurementProtocolSecret RPC

    Attributes:
        measurement_protocol_secrets (MutableSequence[google.analytics.admin_v1alpha.types.MeasurementProtocolSecret]):
            A list of secrets for the parent stream
            specified in the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    measurement_protocol_secrets: MutableSequence[
        resources.MeasurementProtocolSecret
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.MeasurementProtocolSecret,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSKAdNetworkConversionValueSchemaRequest(proto.Message):
    r"""Request message for GetSKAdNetworkConversionValueSchema RPC.

    Attributes:
        name (str):
            Required. The resource name of SKAdNetwork conversion value
            schema to look up. Format:
            properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSchema/{skadnetwork_conversion_value_schema}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSKAdNetworkConversionValueSchemaRequest(proto.Message):
    r"""Request message for CreateSKAdNetworkConversionValueSchema
    RPC.

    Attributes:
        parent (str):
            Required. The parent resource where this
            schema will be created. Format:
            properties/{property}/dataStreams/{dataStream}
        skadnetwork_conversion_value_schema (google.analytics.admin_v1alpha.types.SKAdNetworkConversionValueSchema):
            Required. SKAdNetwork conversion value schema
            to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skadnetwork_conversion_value_schema: resources.SKAdNetworkConversionValueSchema = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=resources.SKAdNetworkConversionValueSchema,
        )
    )


class DeleteSKAdNetworkConversionValueSchemaRequest(proto.Message):
    r"""Request message for DeleteSKAdNetworkConversionValueSchema
    RPC.

    Attributes:
        name (str):
            Required. The name of the SKAdNetworkConversionValueSchema
            to delete. Format:
            properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSchema/{skadnetwork_conversion_value_schema}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSKAdNetworkConversionValueSchemaRequest(proto.Message):
    r"""Request message for UpdateSKAdNetworkConversionValueSchema
    RPC.

    Attributes:
        skadnetwork_conversion_value_schema (google.analytics.admin_v1alpha.types.SKAdNetworkConversionValueSchema):
            Required. SKAdNetwork conversion value schema
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated.
            Omitted fields will not be updated.
    """

    skadnetwork_conversion_value_schema: resources.SKAdNetworkConversionValueSchema = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=resources.SKAdNetworkConversionValueSchema,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListSKAdNetworkConversionValueSchemasRequest(proto.Message):
    r"""Request message for ListSKAdNetworkConversionValueSchemas RPC

    Attributes:
        parent (str):
            Required. The DataStream resource to list schemas for.
            Format: properties/{property_id}/dataStreams/{dataStream}
            Example: properties/1234/dataStreams/5678
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSKAdNetworkConversionValueSchemas`` call. Provide this
            to retrieve the subsequent page. When paginating, all other
            parameters provided to
            ``ListSKAdNetworkConversionValueSchema`` must match the call
            that provided the page token.
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


class ListSKAdNetworkConversionValueSchemasResponse(proto.Message):
    r"""Response message for ListSKAdNetworkConversionValueSchemas
    RPC

    Attributes:
        skadnetwork_conversion_value_schemas (MutableSequence[google.analytics.admin_v1alpha.types.SKAdNetworkConversionValueSchema]):
            List of SKAdNetworkConversionValueSchemas.
            This will have at most one value.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. Currently, Google Analytics supports only one
            SKAdNetworkConversionValueSchema per dataStream, so this
            will never be populated.
    """

    @property
    def raw_page(self):
        return self

    skadnetwork_conversion_value_schemas: MutableSequence[
        resources.SKAdNetworkConversionValueSchema
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.SKAdNetworkConversionValueSchema,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetGoogleSignalsSettingsRequest(proto.Message):
    r"""Request message for GetGoogleSignalsSettings RPC

    Attributes:
        name (str):
            Required. The name of the google signals
            settings to retrieve. Format:
            properties/{property}/googleSignalsSettings
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateGoogleSignalsSettingsRequest(proto.Message):
    r"""Request message for UpdateGoogleSignalsSettings RPC

    Attributes:
        google_signals_settings (google.analytics.admin_v1alpha.types.GoogleSignalsSettings):
            Required. The settings to update. The ``name`` field is used
            to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    google_signals_settings: resources.GoogleSignalsSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.GoogleSignalsSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateConversionEventRequest(proto.Message):
    r"""Request message for CreateConversionEvent RPC

    Attributes:
        conversion_event (google.analytics.admin_v1alpha.types.ConversionEvent):
            Required. The conversion event to create.
        parent (str):
            Required. The resource name of the parent
            property where this conversion event will be
            created. Format: properties/123
    """

    conversion_event: resources.ConversionEvent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.ConversionEvent,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateConversionEventRequest(proto.Message):
    r"""Request message for UpdateConversionEvent RPC

    Attributes:
        conversion_event (google.analytics.admin_v1alpha.types.ConversionEvent):
            Required. The conversion event to update. The ``name`` field
            is used to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    conversion_event: resources.ConversionEvent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.ConversionEvent,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetConversionEventRequest(proto.Message):
    r"""Request message for GetConversionEvent RPC

    Attributes:
        name (str):
            Required. The resource name of the conversion event to
            retrieve. Format:
            properties/{property}/conversionEvents/{conversion_event}
            Example: "properties/123/conversionEvents/456".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteConversionEventRequest(proto.Message):
    r"""Request message for DeleteConversionEvent RPC

    Attributes:
        name (str):
            Required. The resource name of the conversion event to
            delete. Format:
            properties/{property}/conversionEvents/{conversion_event}
            Example: "properties/123/conversionEvents/456".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConversionEventsRequest(proto.Message):
    r"""Request message for ListConversionEvents RPC

    Attributes:
        parent (str):
            Required. The resource name of the parent
            property. Example: 'properties/123'
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 50 resources
            will be returned. The maximum value is 200;
            (higher values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListConversionEvents`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListConversionEvents`` must match the call
            that provided the page token.
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


class ListConversionEventsResponse(proto.Message):
    r"""Response message for ListConversionEvents RPC.

    Attributes:
        conversion_events (MutableSequence[google.analytics.admin_v1alpha.types.ConversionEvent]):
            The requested conversion events
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    conversion_events: MutableSequence[resources.ConversionEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.ConversionEvent,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateKeyEventRequest(proto.Message):
    r"""Request message for CreateKeyEvent RPC

    Attributes:
        key_event (google.analytics.admin_v1alpha.types.KeyEvent):
            Required. The Key Event to create.
        parent (str):
            Required. The resource name of the parent
            property where this Key Event will be created.
            Format: properties/123
    """

    key_event: resources.KeyEvent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.KeyEvent,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateKeyEventRequest(proto.Message):
    r"""Request message for UpdateKeyEvent RPC

    Attributes:
        key_event (google.analytics.admin_v1alpha.types.KeyEvent):
            Required. The Key Event to update. The ``name`` field is
            used to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    key_event: resources.KeyEvent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.KeyEvent,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetKeyEventRequest(proto.Message):
    r"""Request message for GetKeyEvent RPC

    Attributes:
        name (str):
            Required. The resource name of the Key Event to retrieve.
            Format: properties/{property}/keyEvents/{key_event} Example:
            "properties/123/keyEvents/456".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteKeyEventRequest(proto.Message):
    r"""Request message for DeleteKeyEvent RPC

    Attributes:
        name (str):
            Required. The resource name of the Key Event to delete.
            Format: properties/{property}/keyEvents/{key_event} Example:
            "properties/123/keyEvents/456".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListKeyEventsRequest(proto.Message):
    r"""Request message for ListKeyEvents RPC

    Attributes:
        parent (str):
            Required. The resource name of the parent
            property. Example: 'properties/123'
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 50 resources
            will be returned. The maximum value is 200;
            (higher values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListKeyEvents`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListKeyEvents`` must match the call that
            provided the page token.
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


class ListKeyEventsResponse(proto.Message):
    r"""Response message for ListKeyEvents RPC.

    Attributes:
        key_events (MutableSequence[google.analytics.admin_v1alpha.types.KeyEvent]):
            The requested Key Events
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    key_events: MutableSequence[resources.KeyEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.KeyEvent,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDisplayVideo360AdvertiserLinkRequest(proto.Message):
    r"""Request message for GetDisplayVideo360AdvertiserLink RPC.

    Attributes:
        name (str):
            Required. The name of the
            DisplayVideo360AdvertiserLink to get. Example
            format:
            properties/1234/displayVideo360AdvertiserLink/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDisplayVideo360AdvertiserLinksRequest(proto.Message):
    r"""Request message for ListDisplayVideo360AdvertiserLinks RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous
            ``ListDisplayVideo360AdvertiserLinks`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDisplayVideo360AdvertiserLinks`` must match the call
            that provided the page token.
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


class ListDisplayVideo360AdvertiserLinksResponse(proto.Message):
    r"""Response message for ListDisplayVideo360AdvertiserLinks RPC.

    Attributes:
        display_video_360_advertiser_links (MutableSequence[google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLink]):
            List of DisplayVideo360AdvertiserLinks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    display_video_360_advertiser_links: MutableSequence[
        resources.DisplayVideo360AdvertiserLink
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.DisplayVideo360AdvertiserLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDisplayVideo360AdvertiserLinkRequest(proto.Message):
    r"""Request message for CreateDisplayVideo360AdvertiserLink RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        display_video_360_advertiser_link (google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLink):
            Required. The DisplayVideo360AdvertiserLink
            to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_video_360_advertiser_link: resources.DisplayVideo360AdvertiserLink = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=resources.DisplayVideo360AdvertiserLink,
        )
    )


class DeleteDisplayVideo360AdvertiserLinkRequest(proto.Message):
    r"""Request message for DeleteDisplayVideo360AdvertiserLink RPC.

    Attributes:
        name (str):
            Required. The name of the
            DisplayVideo360AdvertiserLink to delete. Example
            format:
            properties/1234/displayVideo360AdvertiserLinks/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDisplayVideo360AdvertiserLinkRequest(proto.Message):
    r"""Request message for UpdateDisplayVideo360AdvertiserLink RPC.

    Attributes:
        display_video_360_advertiser_link (google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLink):
            The DisplayVideo360AdvertiserLink to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    display_video_360_advertiser_link: resources.DisplayVideo360AdvertiserLink = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=resources.DisplayVideo360AdvertiserLink,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetDisplayVideo360AdvertiserLinkProposalRequest(proto.Message):
    r"""Request message for GetDisplayVideo360AdvertiserLinkProposal
    RPC.

    Attributes:
        name (str):
            Required. The name of the
            DisplayVideo360AdvertiserLinkProposal to get.
            Example format:
            properties/1234/displayVideo360AdvertiserLinkProposals/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDisplayVideo360AdvertiserLinkProposalsRequest(proto.Message):
    r"""Request message for
    ListDisplayVideo360AdvertiserLinkProposals RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous
            ``ListDisplayVideo360AdvertiserLinkProposals`` call. Provide
            this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDisplayVideo360AdvertiserLinkProposals`` must match
            the call that provided the page token.
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


class ListDisplayVideo360AdvertiserLinkProposalsResponse(proto.Message):
    r"""Response message for
    ListDisplayVideo360AdvertiserLinkProposals RPC.

    Attributes:
        display_video_360_advertiser_link_proposals (MutableSequence[google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLinkProposal]):
            List of
            DisplayVideo360AdvertiserLinkProposals.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    display_video_360_advertiser_link_proposals: MutableSequence[
        resources.DisplayVideo360AdvertiserLinkProposal
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.DisplayVideo360AdvertiserLinkProposal,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDisplayVideo360AdvertiserLinkProposalRequest(proto.Message):
    r"""Request message for
    CreateDisplayVideo360AdvertiserLinkProposal RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        display_video_360_advertiser_link_proposal (google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLinkProposal):
            Required. The
            DisplayVideo360AdvertiserLinkProposal to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_video_360_advertiser_link_proposal: resources.DisplayVideo360AdvertiserLinkProposal = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.DisplayVideo360AdvertiserLinkProposal,
    )


class DeleteDisplayVideo360AdvertiserLinkProposalRequest(proto.Message):
    r"""Request message for
    DeleteDisplayVideo360AdvertiserLinkProposal RPC.

    Attributes:
        name (str):
            Required. The name of the
            DisplayVideo360AdvertiserLinkProposal to delete.
            Example format:
            properties/1234/displayVideo360AdvertiserLinkProposals/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApproveDisplayVideo360AdvertiserLinkProposalRequest(proto.Message):
    r"""Request message for
    ApproveDisplayVideo360AdvertiserLinkProposal RPC.

    Attributes:
        name (str):
            Required. The name of the
            DisplayVideo360AdvertiserLinkProposal to
            approve. Example format:
            properties/1234/displayVideo360AdvertiserLinkProposals/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApproveDisplayVideo360AdvertiserLinkProposalResponse(proto.Message):
    r"""Response message for
    ApproveDisplayVideo360AdvertiserLinkProposal RPC.

    Attributes:
        display_video_360_advertiser_link (google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLink):
            The DisplayVideo360AdvertiserLink created as
            a result of approving the proposal.
    """

    display_video_360_advertiser_link: resources.DisplayVideo360AdvertiserLink = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=resources.DisplayVideo360AdvertiserLink,
        )
    )


class CancelDisplayVideo360AdvertiserLinkProposalRequest(proto.Message):
    r"""Request message for
    CancelDisplayVideo360AdvertiserLinkProposal RPC.

    Attributes:
        name (str):
            Required. The name of the
            DisplayVideo360AdvertiserLinkProposal to cancel.
            Example format:
            properties/1234/displayVideo360AdvertiserLinkProposals/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSearchAds360LinkRequest(proto.Message):
    r"""Request message for GetSearchAds360Link RPC.

    Attributes:
        name (str):
            Required. The name of the SearchAds360Link to
            get. Example format:
            properties/1234/SearchAds360Link/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSearchAds360LinksRequest(proto.Message):
    r"""Request message for ListSearchAds360Links RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous
            ``ListSearchAds360Links`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListSearchAds360Links`` must match the call that provided
            the page token.
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


class ListSearchAds360LinksResponse(proto.Message):
    r"""Response message for ListSearchAds360Links RPC.

    Attributes:
        search_ads_360_links (MutableSequence[google.analytics.admin_v1alpha.types.SearchAds360Link]):
            List of SearchAds360Links.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    search_ads_360_links: MutableSequence[resources.SearchAds360Link] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.SearchAds360Link,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateSearchAds360LinkRequest(proto.Message):
    r"""Request message for CreateSearchAds360Link RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        search_ads_360_link (google.analytics.admin_v1alpha.types.SearchAds360Link):
            Required. The SearchAds360Link to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_ads_360_link: resources.SearchAds360Link = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.SearchAds360Link,
    )


class DeleteSearchAds360LinkRequest(proto.Message):
    r"""Request message for DeleteSearchAds360Link RPC.

    Attributes:
        name (str):
            Required. The name of the SearchAds360Link to
            delete. Example format:
            properties/1234/SearchAds360Links/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSearchAds360LinkRequest(proto.Message):
    r"""Request message for UpdateSearchAds360Link RPC.

    Attributes:
        search_ads_360_link (google.analytics.admin_v1alpha.types.SearchAds360Link):
            The SearchAds360Link to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    search_ads_360_link: resources.SearchAds360Link = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.SearchAds360Link,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateCustomDimensionRequest(proto.Message):
    r"""Request message for CreateCustomDimension RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        custom_dimension (google.analytics.admin_v1alpha.types.CustomDimension):
            Required. The CustomDimension to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_dimension: resources.CustomDimension = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.CustomDimension,
    )


class UpdateCustomDimensionRequest(proto.Message):
    r"""Request message for UpdateCustomDimension RPC.

    Attributes:
        custom_dimension (google.analytics.admin_v1alpha.types.CustomDimension):
            The CustomDimension to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    custom_dimension: resources.CustomDimension = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CustomDimension,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListCustomDimensionsRequest(proto.Message):
    r"""Request message for ListCustomDimensions RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 50 resources
            will be returned. The maximum value is 200
            (higher values will be coerced to the maximum).
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCustomDimensions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCustomDimensions`` must match the call that provided
            the page token.
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


class ListCustomDimensionsResponse(proto.Message):
    r"""Response message for ListCustomDimensions RPC.

    Attributes:
        custom_dimensions (MutableSequence[google.analytics.admin_v1alpha.types.CustomDimension]):
            List of CustomDimensions.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    custom_dimensions: MutableSequence[resources.CustomDimension] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.CustomDimension,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ArchiveCustomDimensionRequest(proto.Message):
    r"""Request message for ArchiveCustomDimension RPC.

    Attributes:
        name (str):
            Required. The name of the CustomDimension to
            archive. Example format:
            properties/1234/customDimensions/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCustomDimensionRequest(proto.Message):
    r"""Request message for GetCustomDimension RPC.

    Attributes:
        name (str):
            Required. The name of the CustomDimension to
            get. Example format:
            properties/1234/customDimensions/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCustomMetricRequest(proto.Message):
    r"""Request message for CreateCustomMetric RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        custom_metric (google.analytics.admin_v1alpha.types.CustomMetric):
            Required. The CustomMetric to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_metric: resources.CustomMetric = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.CustomMetric,
    )


class UpdateCustomMetricRequest(proto.Message):
    r"""Request message for UpdateCustomMetric RPC.

    Attributes:
        custom_metric (google.analytics.admin_v1alpha.types.CustomMetric):
            The CustomMetric to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    custom_metric: resources.CustomMetric = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CustomMetric,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListCustomMetricsRequest(proto.Message):
    r"""Request message for ListCustomMetrics RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous ``ListCustomMetrics``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListCustomMetrics`` must match the call that provided the
            page token.
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


class ListCustomMetricsResponse(proto.Message):
    r"""Response message for ListCustomMetrics RPC.

    Attributes:
        custom_metrics (MutableSequence[google.analytics.admin_v1alpha.types.CustomMetric]):
            List of CustomMetrics.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    custom_metrics: MutableSequence[resources.CustomMetric] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.CustomMetric,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ArchiveCustomMetricRequest(proto.Message):
    r"""Request message for ArchiveCustomMetric RPC.

    Attributes:
        name (str):
            Required. The name of the CustomMetric to
            archive. Example format:
            properties/1234/customMetrics/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCustomMetricRequest(proto.Message):
    r"""Request message for GetCustomMetric RPC.

    Attributes:
        name (str):
            Required. The name of the CustomMetric to
            get. Example format:
            properties/1234/customMetrics/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCalculatedMetricRequest(proto.Message):
    r"""Request message for CreateCalculatedMetric RPC.

    Attributes:
        parent (str):
            Required. Format: properties/{property_id} Example:
            properties/1234
        calculated_metric_id (str):
            Required. The ID to use for the calculated metric which will
            become the final component of the calculated metric's
            resource name.

            This value should be 1-80 characters and valid characters
            are /[a-zA-Z0-9\_]/, no spaces allowed. calculated_metric_id
            must be unique between all calculated metrics under a
            property. The calculated_metric_id is used when referencing
            this calculated metric from external APIs, for example,
            "calcMetric:{calculated_metric_id}".
        calculated_metric (google.analytics.admin_v1alpha.types.CalculatedMetric):
            Required. The CalculatedMetric to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    calculated_metric_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    calculated_metric: resources.CalculatedMetric = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.CalculatedMetric,
    )


class UpdateCalculatedMetricRequest(proto.Message):
    r"""Request message for UpdateCalculatedMetric RPC.

    Attributes:
        calculated_metric (google.analytics.admin_v1alpha.types.CalculatedMetric):
            Required. The CalculatedMetric to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    calculated_metric: resources.CalculatedMetric = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CalculatedMetric,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCalculatedMetricRequest(proto.Message):
    r"""Request message for DeleteCalculatedMetric RPC.

    Attributes:
        name (str):
            Required. The name of the CalculatedMetric to delete.
            Format:
            properties/{property_id}/calculatedMetrics/{calculated_metric_id}
            Example: properties/1234/calculatedMetrics/Metric01
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCalculatedMetricsRequest(proto.Message):
    r"""Request message for ListCalculatedMetrics RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 50 resources
            will be returned. The maximum value is 200
            (higher values will be coerced to the maximum).
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCalculatedMetrics`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCalculatedMetrics`` must match the call that provided
            the page token.
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


class ListCalculatedMetricsResponse(proto.Message):
    r"""Response message for ListCalculatedMetrics RPC.

    Attributes:
        calculated_metrics (MutableSequence[google.analytics.admin_v1alpha.types.CalculatedMetric]):
            List of CalculatedMetrics.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    calculated_metrics: MutableSequence[resources.CalculatedMetric] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.CalculatedMetric,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCalculatedMetricRequest(proto.Message):
    r"""Request message for GetCalculatedMetric RPC.

    Attributes:
        name (str):
            Required. The name of the CalculatedMetric to get. Format:
            properties/{property_id}/calculatedMetrics/{calculated_metric_id}
            Example: properties/1234/calculatedMetrics/Metric01
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetDataRetentionSettingsRequest(proto.Message):
    r"""Request message for GetDataRetentionSettings RPC.

    Attributes:
        name (str):
            Required. The name of the settings to lookup.
            Format:

            properties/{property}/dataRetentionSettings
            Example: "properties/1000/dataRetentionSettings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataRetentionSettingsRequest(proto.Message):
    r"""Request message for UpdateDataRetentionSettings RPC.

    Attributes:
        data_retention_settings (google.analytics.admin_v1alpha.types.DataRetentionSettings):
            Required. The settings to update. The ``name`` field is used
            to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    data_retention_settings: resources.DataRetentionSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.DataRetentionSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateDataStreamRequest(proto.Message):
    r"""Request message for CreateDataStream RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        data_stream (google.analytics.admin_v1alpha.types.DataStream):
            Required. The DataStream to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_stream: resources.DataStream = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.DataStream,
    )


class DeleteDataStreamRequest(proto.Message):
    r"""Request message for DeleteDataStream RPC.

    Attributes:
        name (str):
            Required. The name of the DataStream to
            delete. Example format:
            properties/1234/dataStreams/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataStreamRequest(proto.Message):
    r"""Request message for UpdateDataStream RPC.

    Attributes:
        data_stream (google.analytics.admin_v1alpha.types.DataStream):
            The DataStream to update
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    data_stream: resources.DataStream = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.DataStream,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListDataStreamsRequest(proto.Message):
    r"""Request message for ListDataStreams RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous ``ListDataStreams``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDataStreams`` must match the call that provided the
            page token.
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


class ListDataStreamsResponse(proto.Message):
    r"""Response message for ListDataStreams RPC.

    Attributes:
        data_streams (MutableSequence[google.analytics.admin_v1alpha.types.DataStream]):
            List of DataStreams.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_streams: MutableSequence[resources.DataStream] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.DataStream,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDataStreamRequest(proto.Message):
    r"""Request message for GetDataStream RPC.

    Attributes:
        name (str):
            Required. The name of the DataStream to get.
            Example format: properties/1234/dataStreams/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAudienceRequest(proto.Message):
    r"""Request message for GetAudience RPC.

    Attributes:
        name (str):
            Required. The name of the Audience to get.
            Example format: properties/1234/audiences/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAudiencesRequest(proto.Message):
    r"""Request message for ListAudiences RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous ``ListAudiences``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAudiences`` must match the call that provided the page
            token.
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


class ListAudiencesResponse(proto.Message):
    r"""Response message for ListAudiences RPC.

    Attributes:
        audiences (MutableSequence[google.analytics.admin_v1alpha.types.Audience]):
            List of Audiences.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    audiences: MutableSequence[gaa_audience.Audience] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gaa_audience.Audience,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAudienceRequest(proto.Message):
    r"""Request message for CreateAudience RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        audience (google.analytics.admin_v1alpha.types.Audience):
            Required. The audience to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audience: gaa_audience.Audience = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gaa_audience.Audience,
    )


class UpdateAudienceRequest(proto.Message):
    r"""Request message for UpdateAudience RPC.

    Attributes:
        audience (google.analytics.admin_v1alpha.types.Audience):
            Required. The audience to update. The audience's ``name``
            field is used to identify the audience to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    audience: gaa_audience.Audience = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gaa_audience.Audience,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ArchiveAudienceRequest(proto.Message):
    r"""Request message for ArchiveAudience RPC.

    Attributes:
        name (str):
            Required. Example format:
            properties/1234/audiences/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAttributionSettingsRequest(proto.Message):
    r"""Request message for GetAttributionSettings RPC.

    Attributes:
        name (str):
            Required. The name of the attribution
            settings to retrieve. Format:
            properties/{property}/attributionSettings
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAttributionSettingsRequest(proto.Message):
    r"""Request message for UpdateAttributionSettings RPC

    Attributes:
        attribution_settings (google.analytics.admin_v1alpha.types.AttributionSettings):
            Required. The attribution settings to update. The ``name``
            field is used to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    attribution_settings: resources.AttributionSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.AttributionSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetAccessBindingRequest(proto.Message):
    r"""Request message for GetAccessBinding RPC.

    Attributes:
        name (str):
            Required. The name of the access binding to
            retrieve. Formats:

            -
              accounts/{account}/accessBindings/{accessBinding}
            -
              properties/{property}/accessBindings/{accessBinding}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchGetAccessBindingsRequest(proto.Message):
    r"""Request message for BatchGetAccessBindings RPC.

    Attributes:
        parent (str):
            Required. The account or property that owns
            the access bindings. The parent of all provided
            values for the 'names' field must match this
            field. Formats:

            - accounts/{account}
            - properties/{property}
        names (MutableSequence[str]):
            Required. The names of the access bindings to
            retrieve. A maximum of 1000 access bindings can
            be retrieved in a batch. Formats:

            -
              accounts/{account}/accessBindings/{accessBinding}
            -
              properties/{property}/accessBindings/{accessBinding}
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchGetAccessBindingsResponse(proto.Message):
    r"""Response message for BatchGetAccessBindings RPC.

    Attributes:
        access_bindings (MutableSequence[google.analytics.admin_v1alpha.types.AccessBinding]):
            The requested access bindings.
    """

    access_bindings: MutableSequence[resources.AccessBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AccessBinding,
    )


class ListAccessBindingsRequest(proto.Message):
    r"""Request message for ListAccessBindings RPC.

    Attributes:
        parent (str):
            Required. Formats:

            - accounts/{account}
            - properties/{property}
        page_size (int):
            The maximum number of access bindings to
            return. The service may return fewer than this
            value. If unspecified, at most 200 access
            bindings will be returned. The maximum value is
            500; values above 500 will be coerced to 500.
        page_token (str):
            A page token, received from a previous
            ``ListAccessBindings`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListAccessBindings`` must match the call that
            provided the page token.
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


class ListAccessBindingsResponse(proto.Message):
    r"""Response message for ListAccessBindings RPC.

    Attributes:
        access_bindings (MutableSequence[google.analytics.admin_v1alpha.types.AccessBinding]):
            List of AccessBindings. These will be ordered
            stably, but in an arbitrary order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    access_bindings: MutableSequence[resources.AccessBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AccessBinding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAccessBindingRequest(proto.Message):
    r"""Request message for CreateAccessBinding RPC.

    Attributes:
        parent (str):
            Required. Formats:

            - accounts/{account}
            - properties/{property}
        access_binding (google.analytics.admin_v1alpha.types.AccessBinding):
            Required. The access binding to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_binding: resources.AccessBinding = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AccessBinding,
    )


class BatchCreateAccessBindingsRequest(proto.Message):
    r"""Request message for BatchCreateAccessBindings RPC.

    Attributes:
        parent (str):
            Required. The account or property that owns
            the access bindings. The parent field in the
            CreateAccessBindingRequest messages must either
            be empty or match this field. Formats:

            - accounts/{account}
            - properties/{property}
        requests (MutableSequence[google.analytics.admin_v1alpha.types.CreateAccessBindingRequest]):
            Required. The requests specifying the access
            bindings to create. A maximum of 1000 access
            bindings can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateAccessBindingRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="CreateAccessBindingRequest",
    )


class BatchCreateAccessBindingsResponse(proto.Message):
    r"""Response message for BatchCreateAccessBindings RPC.

    Attributes:
        access_bindings (MutableSequence[google.analytics.admin_v1alpha.types.AccessBinding]):
            The access bindings created.
    """

    access_bindings: MutableSequence[resources.AccessBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AccessBinding,
    )


class UpdateAccessBindingRequest(proto.Message):
    r"""Request message for UpdateAccessBinding RPC.

    Attributes:
        access_binding (google.analytics.admin_v1alpha.types.AccessBinding):
            Required. The access binding to update.
    """

    access_binding: resources.AccessBinding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.AccessBinding,
    )


class BatchUpdateAccessBindingsRequest(proto.Message):
    r"""Request message for BatchUpdateAccessBindings RPC.

    Attributes:
        parent (str):
            Required. The account or property that owns
            the access bindings. The parent of all provided
            AccessBinding in UpdateAccessBindingRequest
            messages must match this field.
            Formats:

            - accounts/{account}
            - properties/{property}
        requests (MutableSequence[google.analytics.admin_v1alpha.types.UpdateAccessBindingRequest]):
            Required. The requests specifying the access
            bindings to update. A maximum of 1000 access
            bindings can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateAccessBindingRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateAccessBindingRequest",
    )


class BatchUpdateAccessBindingsResponse(proto.Message):
    r"""Response message for BatchUpdateAccessBindings RPC.

    Attributes:
        access_bindings (MutableSequence[google.analytics.admin_v1alpha.types.AccessBinding]):
            The access bindings updated.
    """

    access_bindings: MutableSequence[resources.AccessBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AccessBinding,
    )


class DeleteAccessBindingRequest(proto.Message):
    r"""Request message for DeleteAccessBinding RPC.

    Attributes:
        name (str):
            Required. Formats:

            -
              accounts/{account}/accessBindings/{accessBinding}
            -
              properties/{property}/accessBindings/{accessBinding}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchDeleteAccessBindingsRequest(proto.Message):
    r"""Request message for BatchDeleteAccessBindings RPC.

    Attributes:
        parent (str):
            Required. The account or property that owns
            the access bindings. The parent of all provided
            values for the 'names' field in
            DeleteAccessBindingRequest messages must match
            this field. Formats:

            - accounts/{account}
            - properties/{property}
        requests (MutableSequence[google.analytics.admin_v1alpha.types.DeleteAccessBindingRequest]):
            Required. The requests specifying the access
            bindings to delete. A maximum of 1000 access
            bindings can be deleted in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["DeleteAccessBindingRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="DeleteAccessBindingRequest",
    )


class CreateExpandedDataSetRequest(proto.Message):
    r"""Request message for CreateExpandedDataSet RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        expanded_data_set (google.analytics.admin_v1alpha.types.ExpandedDataSet):
            Required. The ExpandedDataSet to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expanded_data_set: gaa_expanded_data_set.ExpandedDataSet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gaa_expanded_data_set.ExpandedDataSet,
    )


class UpdateExpandedDataSetRequest(proto.Message):
    r"""Request message for UpdateExpandedDataSet RPC.

    Attributes:
        expanded_data_set (google.analytics.admin_v1alpha.types.ExpandedDataSet):
            Required. The ExpandedDataSet to update. The resource's
            ``name`` field is used to identify the ExpandedDataSet to be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    expanded_data_set: gaa_expanded_data_set.ExpandedDataSet = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gaa_expanded_data_set.ExpandedDataSet,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteExpandedDataSetRequest(proto.Message):
    r"""Request message for DeleteExpandedDataSet RPC.

    Attributes:
        name (str):
            Required. Example format:
            properties/1234/expandedDataSets/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetExpandedDataSetRequest(proto.Message):
    r"""Request message for GetExpandedDataSet RPC.

    Attributes:
        name (str):
            Required. The name of the ExpandedDataSet to
            get. Example format:
            properties/1234/expandedDataSets/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExpandedDataSetsRequest(proto.Message):
    r"""Request message for ListExpandedDataSets RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous
            ``ListExpandedDataSets`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListExpandedDataSet`` must match the call that provided
            the page token.
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


class ListExpandedDataSetsResponse(proto.Message):
    r"""Response message for ListExpandedDataSets RPC.

    Attributes:
        expanded_data_sets (MutableSequence[google.analytics.admin_v1alpha.types.ExpandedDataSet]):
            List of ExpandedDataSet. These will be
            ordered stably, but in an arbitrary order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    expanded_data_sets: MutableSequence[gaa_expanded_data_set.ExpandedDataSet] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gaa_expanded_data_set.ExpandedDataSet,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateChannelGroupRequest(proto.Message):
    r"""Request message for CreateChannelGroup RPC.

    Attributes:
        parent (str):
            Required. The property for which to create a
            ChannelGroup. Example format: properties/1234
        channel_group (google.analytics.admin_v1alpha.types.ChannelGroup):
            Required. The ChannelGroup to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    channel_group: gaa_channel_group.ChannelGroup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gaa_channel_group.ChannelGroup,
    )


class UpdateChannelGroupRequest(proto.Message):
    r"""Request message for UpdateChannelGroup RPC.

    Attributes:
        channel_group (google.analytics.admin_v1alpha.types.ChannelGroup):
            Required. The ChannelGroup to update. The resource's
            ``name`` field is used to identify the ChannelGroup to be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    channel_group: gaa_channel_group.ChannelGroup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gaa_channel_group.ChannelGroup,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteChannelGroupRequest(proto.Message):
    r"""Request message for DeleteChannelGroup RPC.

    Attributes:
        name (str):
            Required. The ChannelGroup to delete.
            Example format:
            properties/1234/channelGroups/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetChannelGroupRequest(proto.Message):
    r"""Request message for GetChannelGroup RPC.

    Attributes:
        name (str):
            Required. The ChannelGroup to get.
            Example format:
            properties/1234/channelGroups/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListChannelGroupsRequest(proto.Message):
    r"""Request message for ListChannelGroups RPC.

    Attributes:
        parent (str):
            Required. The property for which to list
            ChannelGroups. Example format: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous ``ListChannelGroups``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListChannelGroups`` must match the call that provided the
            page token.
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


class ListChannelGroupsResponse(proto.Message):
    r"""Response message for ListChannelGroups RPC.

    Attributes:
        channel_groups (MutableSequence[google.analytics.admin_v1alpha.types.ChannelGroup]):
            List of ChannelGroup. These will be ordered
            stably, but in an arbitrary order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    channel_groups: MutableSequence[gaa_channel_group.ChannelGroup] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gaa_channel_group.ChannelGroup,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateBigQueryLinkRequest(proto.Message):
    r"""Request message for CreateBigQueryLink RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        bigquery_link (google.analytics.admin_v1alpha.types.BigQueryLink):
            Required. The BigQueryLink to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bigquery_link: resources.BigQueryLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.BigQueryLink,
    )


class GetBigQueryLinkRequest(proto.Message):
    r"""Request message for GetBigQueryLink RPC.

    Attributes:
        name (str):
            Required. The name of the BigQuery link to lookup. Format:
            properties/{property_id}/bigQueryLinks/{bigquery_link_id}
            Example: properties/123/bigQueryLinks/456
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBigQueryLinksRequest(proto.Message):
    r"""Request message for ListBigQueryLinks RPC.

    Attributes:
        parent (str):
            Required. The name of the property to list BigQuery links
            under. Format: properties/{property_id} Example:
            properties/1234
        page_size (int):
            The maximum number of resources to return.
            The service may return fewer than this value,
            even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            A page token, received from a previous ``ListBigQueryLinks``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to
            ``ListBigQueryLinks`` must match the call that provided the
            page token.
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


class ListBigQueryLinksResponse(proto.Message):
    r"""Response message for ListBigQueryLinks RPC

    Attributes:
        bigquery_links (MutableSequence[google.analytics.admin_v1alpha.types.BigQueryLink]):
            List of BigQueryLinks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    bigquery_links: MutableSequence[resources.BigQueryLink] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.BigQueryLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateBigQueryLinkRequest(proto.Message):
    r"""Request message for UpdateBigQueryLink RPC.

    Attributes:
        bigquery_link (google.analytics.admin_v1alpha.types.BigQueryLink):
            Required. The settings to update. The ``name`` field is used
            to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    bigquery_link: resources.BigQueryLink = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.BigQueryLink,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteBigQueryLinkRequest(proto.Message):
    r"""Request message for DeleteBigQueryLink RPC.

    Attributes:
        name (str):
            Required. The BigQueryLink to delete.
            Example format:
            properties/1234/bigQueryLinks/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEnhancedMeasurementSettingsRequest(proto.Message):
    r"""Request message for GetEnhancedMeasurementSettings RPC.

    Attributes:
        name (str):
            Required. The name of the settings to lookup. Format:
            properties/{property}/dataStreams/{data_stream}/enhancedMeasurementSettings
            Example:
            "properties/1000/dataStreams/2000/enhancedMeasurementSettings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateEnhancedMeasurementSettingsRequest(proto.Message):
    r"""Request message for UpdateEnhancedMeasurementSettings RPC.

    Attributes:
        enhanced_measurement_settings (google.analytics.admin_v1alpha.types.EnhancedMeasurementSettings):
            Required. The settings to update. The ``name`` field is used
            to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    enhanced_measurement_settings: resources.EnhancedMeasurementSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.EnhancedMeasurementSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetDataRedactionSettingsRequest(proto.Message):
    r"""Request message for GetDataRedactionSettings RPC.

    Attributes:
        name (str):
            Required. The name of the settings to lookup. Format:
            properties/{property}/dataStreams/{data_stream}/dataRedactionSettings
            Example:
            "properties/1000/dataStreams/2000/dataRedactionSettings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataRedactionSettingsRequest(proto.Message):
    r"""Request message for UpdateDataRedactionSettings RPC.

    Attributes:
        data_redaction_settings (google.analytics.admin_v1alpha.types.DataRedactionSettings):
            Required. The settings to update. The ``name`` field is used
            to identify the settings to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    data_redaction_settings: resources.DataRedactionSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.DataRedactionSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateAdSenseLinkRequest(proto.Message):
    r"""Request message to be passed to CreateAdSenseLink method.

    Attributes:
        parent (str):
            Required. The property for which to create an
            AdSense Link. Format: properties/{propertyId}
            Example: properties/1234
        adsense_link (google.analytics.admin_v1alpha.types.AdSenseLink):
            Required. The AdSense Link to create
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    adsense_link: resources.AdSenseLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AdSenseLink,
    )


class GetAdSenseLinkRequest(proto.Message):
    r"""Request message to be passed to GetAdSenseLink method.

    Attributes:
        name (str):
            Required. Unique identifier for the AdSense
            Link requested. Format:
            properties/{propertyId}/adSenseLinks/{linkId}
            Example: properties/1234/adSenseLinks/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteAdSenseLinkRequest(proto.Message):
    r"""Request message to be passed to DeleteAdSenseLink method.

    Attributes:
        name (str):
            Required. Unique identifier for the AdSense
            Link to be deleted. Format:
            properties/{propertyId}/adSenseLinks/{linkId}
            Example: properties/1234/adSenseLinks/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAdSenseLinksRequest(proto.Message):
    r"""Request message to be passed to ListAdSenseLinks method.

    Attributes:
        parent (str):
            Required. Resource name of the parent
            property. Format: properties/{propertyId}
            Example: properties/1234
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token received from a previous ``ListAdSenseLinks``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAdSenseLinks`` must match the call that provided the
            page token.
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


class ListAdSenseLinksResponse(proto.Message):
    r"""Response message for ListAdSenseLinks method.

    Attributes:
        adsense_links (MutableSequence[google.analytics.admin_v1alpha.types.AdSenseLink]):
            List of AdSenseLinks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    adsense_links: MutableSequence[resources.AdSenseLink] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AdSenseLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateEventCreateRuleRequest(proto.Message):
    r"""Request message for CreateEventCreateRule RPC.

    Attributes:
        parent (str):
            Required. Example format:
            properties/123/dataStreams/456
        event_create_rule (google.analytics.admin_v1alpha.types.EventCreateRule):
            Required. The EventCreateRule to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_create_rule: event_create_and_edit.EventCreateRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=event_create_and_edit.EventCreateRule,
    )


class UpdateEventCreateRuleRequest(proto.Message):
    r"""Request message for UpdateEventCreateRule RPC.

    Attributes:
        event_create_rule (google.analytics.admin_v1alpha.types.EventCreateRule):
            Required. The EventCreateRule to update. The resource's
            ``name`` field is used to identify the EventCreateRule to be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    event_create_rule: event_create_and_edit.EventCreateRule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=event_create_and_edit.EventCreateRule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEventCreateRuleRequest(proto.Message):
    r"""Request message for DeleteEventCreateRule RPC.

    Attributes:
        name (str):
            Required. Example format:

            properties/123/dataStreams/456/eventCreateRules/789
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEventCreateRuleRequest(proto.Message):
    r"""Request message for GetEventCreateRule RPC.

    Attributes:
        name (str):
            Required. The name of the EventCreateRule to
            get. Example format:
            properties/123/dataStreams/456/eventCreateRules/789
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEventCreateRulesRequest(proto.Message):
    r"""Request message for ListEventCreateRules RPC.

    Attributes:
        parent (str):
            Required. Example format:
            properties/123/dataStreams/456
        page_size (int):
            The maximum number of resources to return.
            If unspecified, at most 50 resources will be
            returned. The maximum value is 200 (higher
            values will be coerced to the maximum).
        page_token (str):
            A page token, received from a previous
            ``ListEventCreateRules`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListEventCreateRules`` must match the call that provided
            the page token.
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


class ListEventCreateRulesResponse(proto.Message):
    r"""Response message for ListEventCreateRules RPC.

    Attributes:
        event_create_rules (MutableSequence[google.analytics.admin_v1alpha.types.EventCreateRule]):
            List of EventCreateRules. These will be
            ordered stably, but in an arbitrary order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    event_create_rules: MutableSequence[event_create_and_edit.EventCreateRule] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=event_create_and_edit.EventCreateRule,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateEventEditRuleRequest(proto.Message):
    r"""Request message for CreateEventEditRule RPC.

    Attributes:
        parent (str):
            Required. Example format:
            properties/123/dataStreams/456
        event_edit_rule (google.analytics.admin_v1alpha.types.EventEditRule):
            Required. The EventEditRule to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_edit_rule: event_create_and_edit.EventEditRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=event_create_and_edit.EventEditRule,
    )


class UpdateEventEditRuleRequest(proto.Message):
    r"""Request message for UpdateEventEditRule RPC.

    Attributes:
        event_edit_rule (google.analytics.admin_v1alpha.types.EventEditRule):
            Required. The EventEditRule to update. The resource's
            ``name`` field is used to identify the EventEditRule to be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. Field names must
            be in snake case (e.g., "field_to_update"). Omitted fields
            will not be updated. To replace the entire entity, use one
            path with the string "\*" to match all fields.
    """

    event_edit_rule: event_create_and_edit.EventEditRule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=event_create_and_edit.EventEditRule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEventEditRuleRequest(proto.Message):
    r"""Request message for DeleteEventEditRule RPC.

    Attributes:
        name (str):
            Required. Example format:
            properties/123/dataStreams/456/eventEditRules/789
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEventEditRuleRequest(proto.Message):
    r"""Request message for GetEventEditRule RPC.

    Attributes:
        name (str):
            Required. The name of the EventEditRule to
            get. Example format:
            properties/123/dataStreams/456/eventEditRules/789
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEventEditRulesRequest(proto.Message):
    r"""Request message for ListEventEditRules RPC.

    Attributes:
        parent (str):
            Required. Example format:
            properties/123/dataStreams/456
        page_size (int):
            Optional. The maximum number of resources to
            return. If unspecified, at most 50 resources
            will be returned. The maximum value is 200
            (higher values will be coerced to the maximum).
        page_token (str):
            Optional. A page token, received from a previous
            ``ListEventEditRules`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListEventEditRules`` must match the call that provided the
            page token.
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


class ListEventEditRulesResponse(proto.Message):
    r"""Response message for ListEventEditRules RPC.

    Attributes:
        event_edit_rules (MutableSequence[google.analytics.admin_v1alpha.types.EventEditRule]):
            List of EventEditRules. These will be ordered
            stably, but in an arbitrary order.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    event_edit_rules: MutableSequence[event_create_and_edit.EventEditRule] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=event_create_and_edit.EventEditRule,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReorderEventEditRulesRequest(proto.Message):
    r"""Request message for ReorderEventEditRules RPC.

    Attributes:
        parent (str):
            Required. Example format:
            properties/123/dataStreams/456
        event_edit_rules (MutableSequence[str]):
            Required. EventEditRule resource names for
            the specified data stream, in the needed
            processing order. All EventEditRules for the
            stream must be present in the list.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_edit_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CreateRollupPropertyRequest(proto.Message):
    r"""Request message for CreateRollupProperty RPC.

    Attributes:
        rollup_property (google.analytics.admin_v1alpha.types.Property):
            Required. The roll-up property to create.
        source_properties (MutableSequence[str]):
            Optional. The resource names of properties
            that will be sources to the created roll-up
            property.
    """

    rollup_property: resources.Property = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Property,
    )
    source_properties: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CreateRollupPropertyResponse(proto.Message):
    r"""Response message for CreateRollupProperty RPC.

    Attributes:
        rollup_property (google.analytics.admin_v1alpha.types.Property):
            The created roll-up property.
        rollup_property_source_links (MutableSequence[google.analytics.admin_v1alpha.types.RollupPropertySourceLink]):
            The created roll-up property source links.
    """

    rollup_property: resources.Property = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Property,
    )
    rollup_property_source_links: MutableSequence[
        resources.RollupPropertySourceLink
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=resources.RollupPropertySourceLink,
    )


class GetRollupPropertySourceLinkRequest(proto.Message):
    r"""Request message for GetRollupPropertySourceLink RPC.

    Attributes:
        name (str):
            Required. The name of the roll-up property source link to
            lookup. Format:
            properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_link_id}
            Example: properties/123/rollupPropertySourceLinks/456
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRollupPropertySourceLinksRequest(proto.Message):
    r"""Request message for ListRollupPropertySourceLinks RPC.

    Attributes:
        parent (str):
            Required. The name of the roll-up property to list roll-up
            property source links under. Format:
            properties/{property_id} Example: properties/1234
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRollupPropertySourceLinks`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListRollupPropertySourceLinks``
            must match the call that provided the page token.
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


class ListRollupPropertySourceLinksResponse(proto.Message):
    r"""Response message for ListRollupPropertySourceLinks RPC.

    Attributes:
        rollup_property_source_links (MutableSequence[google.analytics.admin_v1alpha.types.RollupPropertySourceLink]):
            List of RollupPropertySourceLinks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rollup_property_source_links: MutableSequence[
        resources.RollupPropertySourceLink
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.RollupPropertySourceLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateRollupPropertySourceLinkRequest(proto.Message):
    r"""Request message for CreateRollupPropertySourceLink RPC.

    Attributes:
        parent (str):
            Required. Format: properties/{property_id} Example:
            properties/1234
        rollup_property_source_link (google.analytics.admin_v1alpha.types.RollupPropertySourceLink):
            Required. The roll-up property source link to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollup_property_source_link: resources.RollupPropertySourceLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.RollupPropertySourceLink,
    )


class DeleteRollupPropertySourceLinkRequest(proto.Message):
    r"""Request message for DeleteRollupPropertySourceLink RPC.

    Attributes:
        name (str):
            Required. Format:
            properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_link_id}
            Example: properties/1234/rollupPropertySourceLinks/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ProvisionSubpropertyRequest(proto.Message):
    r"""Request message for CreateSubproperty RPC.

    Attributes:
        subproperty (google.analytics.admin_v1alpha.types.Property):
            Required. The subproperty to create.
        subproperty_event_filter (google.analytics.admin_v1alpha.types.SubpropertyEventFilter):
            Optional. The subproperty event filter to
            create on an ordinary property.
        custom_dimension_and_metric_synchronization_mode (google.analytics.admin_v1alpha.types.SubpropertySyncConfig.SynchronizationMode):
            Optional. The subproperty feature
            synchronization mode for Custom Dimensions and
            Metrics
    """

    subproperty: resources.Property = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Property,
    )
    subproperty_event_filter: gaa_subproperty_event_filter.SubpropertyEventFilter = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=gaa_subproperty_event_filter.SubpropertyEventFilter,
        )
    )
    custom_dimension_and_metric_synchronization_mode: resources.SubpropertySyncConfig.SynchronizationMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.SubpropertySyncConfig.SynchronizationMode,
    )


class ProvisionSubpropertyResponse(proto.Message):
    r"""Response message for ProvisionSubproperty RPC.

    Attributes:
        subproperty (google.analytics.admin_v1alpha.types.Property):
            The created subproperty.
        subproperty_event_filter (google.analytics.admin_v1alpha.types.SubpropertyEventFilter):
            The created subproperty event filter.
    """

    subproperty: resources.Property = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Property,
    )
    subproperty_event_filter: gaa_subproperty_event_filter.SubpropertyEventFilter = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=gaa_subproperty_event_filter.SubpropertyEventFilter,
        )
    )


class CreateSubpropertyEventFilterRequest(proto.Message):
    r"""Request message for CreateSubpropertyEventFilter RPC.

    Attributes:
        parent (str):
            Required. The ordinary property for which to create a
            subproperty event filter. Format: properties/property_id
            Example: properties/123
        subproperty_event_filter (google.analytics.admin_v1alpha.types.SubpropertyEventFilter):
            Required. The subproperty event filter to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subproperty_event_filter: gaa_subproperty_event_filter.SubpropertyEventFilter = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=gaa_subproperty_event_filter.SubpropertyEventFilter,
        )
    )


class GetSubpropertyEventFilterRequest(proto.Message):
    r"""Request message for GetSubpropertyEventFilter RPC.

    Attributes:
        name (str):
            Required. Resource name of the subproperty event filter to
            lookup. Format:
            properties/property_id/subpropertyEventFilters/subproperty_event_filter
            Example: properties/123/subpropertyEventFilters/456
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSubpropertyEventFiltersRequest(proto.Message):
    r"""Request message for ListSubpropertyEventFilters RPC.

    Attributes:
        parent (str):
            Required. Resource name of the ordinary property. Format:
            properties/property_id Example: properties/123
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSubpropertyEventFilters`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListSubpropertyEventFilters`` must
            match the call that provided the page token.
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


class ListSubpropertyEventFiltersResponse(proto.Message):
    r"""Response message for ListSubpropertyEventFilter RPC.

    Attributes:
        subproperty_event_filters (MutableSequence[google.analytics.admin_v1alpha.types.SubpropertyEventFilter]):
            List of subproperty event filters.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    subproperty_event_filters: MutableSequence[
        gaa_subproperty_event_filter.SubpropertyEventFilter
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gaa_subproperty_event_filter.SubpropertyEventFilter,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSubpropertyEventFilterRequest(proto.Message):
    r"""Request message for UpdateSubpropertyEventFilter RPC.

    Attributes:
        subproperty_event_filter (google.analytics.admin_v1alpha.types.SubpropertyEventFilter):
            Required. The subproperty event filter to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Field names must be
            in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    subproperty_event_filter: gaa_subproperty_event_filter.SubpropertyEventFilter = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=gaa_subproperty_event_filter.SubpropertyEventFilter,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSubpropertyEventFilterRequest(proto.Message):
    r"""Request message for DeleteSubpropertyEventFilter RPC.

    Attributes:
        name (str):
            Required. Resource name of the subproperty event filter to
            delete. Format:
            properties/property_id/subpropertyEventFilters/subproperty_event_filter
            Example: properties/123/subpropertyEventFilters/456
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateReportingDataAnnotationRequest(proto.Message):
    r"""Request message for CreateReportingDataAnnotation RPC.

    Attributes:
        parent (str):
            Required. The property for which to create a Reporting Data
            Annotation. Format: properties/property_id Example:
            properties/123
        reporting_data_annotation (google.analytics.admin_v1alpha.types.ReportingDataAnnotation):
            Required. The Reporting Data Annotation to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reporting_data_annotation: resources.ReportingDataAnnotation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.ReportingDataAnnotation,
    )


class GetReportingDataAnnotationRequest(proto.Message):
    r"""Request message for GetReportingDataAnnotation RPC.

    Attributes:
        name (str):
            Required. Resource name of the Reporting Data Annotation to
            lookup. Format:
            properties/property_id/reportingDataAnnotations/reportingDataAnnotation
            Example: properties/123/reportingDataAnnotations/456
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListReportingDataAnnotationsRequest(proto.Message):
    r"""Request message for ListReportingDataAnnotation RPC.

    Attributes:
        parent (str):
            Required. Resource name of the property. Format:
            properties/property_id Example: properties/123
        filter (str):
            Optional. Filter that restricts which reporting data
            annotations under the parent property are listed.

            Supported fields are:

            - 'name'
            - ``title``
            - ``description``
            - ``annotation_date``
            - ``annotation_date_range``
            - ``color``

            Additionally, this API provides the following helper
            functions:

            - annotation_duration() : the duration that this annotation
              marks,
              `durations <https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto>`__.
              expect a numeric representation of seconds followed by an
              ``s`` suffix.
            - is_annotation_in_range(start_date, end_date) : if the
              annotation is in the range specified by the ``start_date``
              and ``end_date``. The dates are in ISO-8601 format, for
              example ``2031-06-28``.

            Supported operations:

            - ``=`` : equals
            - ``!=`` : not equals
            - ``<`` : less than
            - ``>`` : greater than
            - ``<=`` : less than or equals
            - ``>=`` : greater than or equals
            - ``:`` : has operator
            - ``=~`` : `regular
              expression <https://github.com/google/re2/wiki/Syntax>`__
              match
            - ``!~`` : `regular
              expression <https://github.com/google/re2/wiki/Syntax>`__
              does not match
            - ``NOT`` : Logical not
            - ``AND`` : Logical and
            - ``OR`` : Logical or

            Examples:

            1. ``title="Holiday Sale"``
            2. ``description=~"[Bb]ig [Gg]ame.*[Ss]ale"``
            3. ``is_annotation_in_range("2025-12-25", "2026-01-16") = true``
            4. ``annotation_duration() >= 172800s AND title:BOGO``
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListReportingDataAnnotations`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListReportingDataAnnotations`` must
            match the call that provided the page token.
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


class ListReportingDataAnnotationsResponse(proto.Message):
    r"""Response message for ListReportingDataAnnotation RPC.

    Attributes:
        reporting_data_annotations (MutableSequence[google.analytics.admin_v1alpha.types.ReportingDataAnnotation]):
            List of Reporting Data Annotations.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    reporting_data_annotations: MutableSequence[resources.ReportingDataAnnotation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.ReportingDataAnnotation,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateReportingDataAnnotationRequest(proto.Message):
    r"""Request message for UpdateReportingDataAnnotation RPC.

    Attributes:
        reporting_data_annotation (google.analytics.admin_v1alpha.types.ReportingDataAnnotation):
            Required. The Reporting Data Annotation to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Field names must be
            in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    reporting_data_annotation: resources.ReportingDataAnnotation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.ReportingDataAnnotation,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteReportingDataAnnotationRequest(proto.Message):
    r"""Request message for DeleteReportingDataAnnotation RPC.

    Attributes:
        name (str):
            Required. Resource name of the Reporting Data Annotation to
            delete. Format:
            properties/property_id/reportingDataAnnotations/reporting_data_annotation
            Example: properties/123/reportingDataAnnotations/456
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SubmitUserDeletionRequest(proto.Message):
    r"""Request message for SubmitUserDeletion RPC.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_id (str):
            Google Analytics `user
            ID <https://firebase.google.com/docs/analytics/userid>`__.

            This field is a member of `oneof`_ ``user``.
        client_id (str):
            Google Analytics `client
            ID <https://support.google.com/analytics/answer/11593727>`__.

            This field is a member of `oneof`_ ``user``.
        app_instance_id (str):
            Firebase `application instance
            ID <https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.html#getAppInstanceId>`__.

            This field is a member of `oneof`_ ``user``.
        user_provided_data (str):
            `User-provided
            data <https://support.google.com/analytics/answer/14077171>`__.
            May contain either one email address or one phone number.

            Email addresses should be normalized as such:

            - lowercase
            - remove periods before @ for gmail.com/googlemail.com
              addresses
            - remove all spaces

            Phone numbers should be normalized as such:

            - remove all non digit characters
            - add + prefix

            This field is a member of `oneof`_ ``user``.
        name (str):
            Required. The name of the property to submit
            user deletion for.
    """

    user_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="user",
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="user",
    )
    app_instance_id: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="user",
    )
    user_provided_data: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="user",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SubmitUserDeletionResponse(proto.Message):
    r"""Response message for SubmitUserDeletion RPC.

    Attributes:
        deletion_request_time (google.protobuf.timestamp_pb2.Timestamp):
            Marks the moment for which all visitor data
            before this point should be deleted. This is set
            to the time at which the deletion request was
            received.
    """

    deletion_request_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class GetSubpropertySyncConfigRequest(proto.Message):
    r"""Request message for GetSubpropertySyncConfig RPC.

    Attributes:
        name (str):
            Required. Resource name of the SubpropertySyncConfig to
            lookup. Format:
            properties/{ordinary_property_id}/subpropertySyncConfigs/{subproperty_id}
            Example: properties/1234/subpropertySyncConfigs/5678
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSubpropertySyncConfigsRequest(proto.Message):
    r"""Request message for ListSubpropertySyncConfigs RPC.

    Attributes:
        parent (str):
            Required. Resource name of the property. Format:
            properties/property_id Example: properties/123
        page_size (int):
            Optional. The maximum number of resources to
            return. The service may return fewer than this
            value, even if there are additional pages. If
            unspecified, at most 50 resources will be
            returned. The maximum value is 200; (higher
            values will be coerced to the maximum)
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSubpropertySyncConfig`` call. Provide this to retrieve
            the subsequent page. When paginating, all other parameters
            provided to ``ListSubpropertySyncConfig`` must match the
            call that provided the page token.
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


class ListSubpropertySyncConfigsResponse(proto.Message):
    r"""Response message for ListSubpropertySyncConfigs RPC.

    Attributes:
        subproperty_sync_configs (MutableSequence[google.analytics.admin_v1alpha.types.SubpropertySyncConfig]):
            List of ``SubpropertySyncConfig`` resources.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    subproperty_sync_configs: MutableSequence[resources.SubpropertySyncConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.SubpropertySyncConfig,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSubpropertySyncConfigRequest(proto.Message):
    r"""Request message for UpdateSubpropertySyncConfig RPC.

    Attributes:
        subproperty_sync_config (google.analytics.admin_v1alpha.types.SubpropertySyncConfig):
            Required. The ``SubpropertySyncConfig`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Field names must be
            in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    subproperty_sync_config: resources.SubpropertySyncConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.SubpropertySyncConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetReportingIdentitySettingsRequest(proto.Message):
    r"""Request message for GetReportingIdentitySettings RPC.

    Attributes:
        name (str):
            Required. The name of the settings to lookup.
            Format:

            properties/{property}/reportingIdentitySettings
            Example:
            "properties/1000/reportingIdentitySettings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateReportingIdentitySettingsRequest(proto.Message):
    r"""Request message for UpdateReportingIdentitySettings RPC.

    Attributes:
        reporting_identity_settings (google.analytics.admin_v1alpha.types.ReportingIdentitySettings):
            Required. The reporting identity settings to update. The
            settings' ``name`` field is used to identify the settings.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated. Field names must
            be in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields. If
            omitted, the service will treat it as an implied field mask
            equivalent to all fields that are populated.
    """

    reporting_identity_settings: resources.ReportingIdentitySettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.ReportingIdentitySettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetUserProvidedDataSettingsRequest(proto.Message):
    r"""Request message for GetUserProvidedDataSettings RPC

    Attributes:
        name (str):
            Required. The name of the user provided data
            settings to retrieve. Format:
            properties/{property}/userProvidedDataSettings
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
