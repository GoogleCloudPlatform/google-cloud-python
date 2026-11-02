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

from google.analytics.admin_v1beta.types import access_report, resources

__protobuf__ = proto.module(
    package="google.analytics.admin.v1beta",
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
        "GetDataRetentionSettingsRequest",
        "UpdateDataRetentionSettingsRequest",
        "CreateDataStreamRequest",
        "DeleteDataStreamRequest",
        "UpdateDataStreamRequest",
        "ListDataStreamsRequest",
        "ListDataStreamsResponse",
        "GetDataStreamRequest",
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
        dimensions (MutableSequence[google.analytics.admin_v1beta.types.AccessDimension]):
            The dimensions requested and displayed in the
            response. Requests are allowed up to 9
            dimensions.
        metrics (MutableSequence[google.analytics.admin_v1beta.types.AccessMetric]):
            The metrics requested and displayed in the
            response. Requests are allowed up to 10 metrics.
        date_ranges (MutableSequence[google.analytics.admin_v1beta.types.AccessDateRange]):
            Date ranges of access records to read. If
            multiple date ranges are requested, each
            response row will contain a zero based date
            range index. If two date ranges overlap, the
            access records for the overlapping days is
            included in the response rows for both date
            ranges. Requests are allowed up to 2 date
            ranges.
        dimension_filter (google.analytics.admin_v1beta.types.AccessFilterExpression):
            Dimension filters let you restrict report response to
            specific dimension values which match the filter. For
            example, filtering on access records of a single user. To
            learn more, see `Fundamentals of Dimension
            Filters <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters>`__
            for examples. Metrics cannot be used in this filter.
        metric_filter (google.analytics.admin_v1beta.types.AccessFilterExpression):
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
        order_bys (MutableSequence[google.analytics.admin_v1beta.types.AccessOrderBy]):
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
        dimension_headers (MutableSequence[google.analytics.admin_v1beta.types.AccessDimensionHeader]):
            The header for a column in the report that
            corresponds to a specific dimension. The number
            of DimensionHeaders and ordering of
            DimensionHeaders matches the dimensions present
            in rows.
        metric_headers (MutableSequence[google.analytics.admin_v1beta.types.AccessMetricHeader]):
            The header for a column in the report that
            corresponds to a specific metric. The number of
            MetricHeaders and ordering of MetricHeaders
            matches the metrics present in rows.
        rows (MutableSequence[google.analytics.admin_v1beta.types.AccessRow]):
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
        quota (google.analytics.admin_v1beta.types.AccessQuota):
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
        accounts (MutableSequence[google.analytics.admin_v1beta.types.Account]):
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
        account (google.analytics.admin_v1beta.types.Account):
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
        account (google.analytics.admin_v1beta.types.Account):
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
        properties (MutableSequence[google.analytics.admin_v1beta.types.Property]):
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
        property (google.analytics.admin_v1beta.types.Property):
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
        property (google.analytics.admin_v1beta.types.Property):
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
        firebase_link (google.analytics.admin_v1beta.types.FirebaseLink):
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
        firebase_links (MutableSequence[google.analytics.admin_v1beta.types.FirebaseLink]):
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


class CreateGoogleAdsLinkRequest(proto.Message):
    r"""Request message for CreateGoogleAdsLink RPC

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        google_ads_link (google.analytics.admin_v1beta.types.GoogleAdsLink):
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
        google_ads_link (google.analytics.admin_v1beta.types.GoogleAdsLink):
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
        google_ads_links (MutableSequence[google.analytics.admin_v1beta.types.GoogleAdsLink]):
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
        account_summaries (MutableSequence[google.analytics.admin_v1beta.types.AccountSummary]):
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
        resource_type (MutableSequence[google.analytics.admin_v1beta.types.ChangeHistoryResourceType]):
            Optional. If set, only return changes if they
            are for a resource that matches at least one of
            these types.
        action (MutableSequence[google.analytics.admin_v1beta.types.ActionType]):
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
        change_history_events (MutableSequence[google.analytics.admin_v1beta.types.ChangeHistoryEvent]):
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
        measurement_protocol_secret (google.analytics.admin_v1beta.types.MeasurementProtocolSecret):
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
        measurement_protocol_secret (google.analytics.admin_v1beta.types.MeasurementProtocolSecret):
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
        measurement_protocol_secrets (MutableSequence[google.analytics.admin_v1beta.types.MeasurementProtocolSecret]):
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


class CreateConversionEventRequest(proto.Message):
    r"""Request message for CreateConversionEvent RPC

    Attributes:
        conversion_event (google.analytics.admin_v1beta.types.ConversionEvent):
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
        conversion_event (google.analytics.admin_v1beta.types.ConversionEvent):
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
        conversion_events (MutableSequence[google.analytics.admin_v1beta.types.ConversionEvent]):
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
        key_event (google.analytics.admin_v1beta.types.KeyEvent):
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
        key_event (google.analytics.admin_v1beta.types.KeyEvent):
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
        key_events (MutableSequence[google.analytics.admin_v1beta.types.KeyEvent]):
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


class CreateCustomDimensionRequest(proto.Message):
    r"""Request message for CreateCustomDimension RPC.

    Attributes:
        parent (str):
            Required. Example format: properties/1234
        custom_dimension (google.analytics.admin_v1beta.types.CustomDimension):
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
        custom_dimension (google.analytics.admin_v1beta.types.CustomDimension):
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
        custom_dimensions (MutableSequence[google.analytics.admin_v1beta.types.CustomDimension]):
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
        custom_metric (google.analytics.admin_v1beta.types.CustomMetric):
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
        custom_metric (google.analytics.admin_v1beta.types.CustomMetric):
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
        custom_metrics (MutableSequence[google.analytics.admin_v1beta.types.CustomMetric]):
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
        data_retention_settings (google.analytics.admin_v1beta.types.DataRetentionSettings):
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
        data_stream (google.analytics.admin_v1beta.types.DataStream):
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
        data_stream (google.analytics.admin_v1beta.types.DataStream):
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
        data_streams (MutableSequence[google.analytics.admin_v1beta.types.DataStream]):
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


__all__ = tuple(sorted(__protobuf__.manifest))
