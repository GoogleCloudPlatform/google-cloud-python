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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.reports.v1alpha",
    manifest={
        "SearchRequest",
        "SearchResponse",
        "ReportRow",
        "ProductPerformanceView",
        "ProductView",
        "PriceCompetitivenessProductView",
        "PriceInsightsProductView",
        "BestSellersProductClusterView",
        "BestSellersBrandView",
        "NonProductPerformanceView",
        "CompetitiveVisibilityCompetitorView",
        "CompetitiveVisibilityTopMerchantView",
        "CompetitiveVisibilityBenchmarkView",
        "MarketingMethod",
        "ReportGranularity",
        "RelativeDemand",
        "RelativeDemandChangeType",
        "TrafficSource",
        "YoutubeCreatorPerformanceView",
        "YoutubeContentPerformanceView",
        "YoutubeProductPerformanceView",
    },
)


class SearchRequest(proto.Message):
    r"""Request message for the ``ReportService.Search`` method.

    Attributes:
        parent (str):
            Required. Id of the account making the call.
            Must be a standalone account or an MCA
            subaccount. Format: accounts/{account}
        query (str):
            Required. Query that defines a report to be
            retrieved.
            For details on how to construct your query, see
            the Query Language guide. For the full list of
            available tables and fields, see the Available
            fields.
        page_size (int):
            Optional. Number of ``ReportRows`` to retrieve in a single
            page. Defaults to 1000. Values above 5000 are coerced to
            5000.
        page_token (str):
            Optional. Token of the page to retrieve. If not specified,
            the first page of results is returned. In order to request
            the next page of results, the value obtained from
            ``next_page_token`` in the previous response should be used.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
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


class SearchResponse(proto.Message):
    r"""Response message for the ``ReportService.Search`` method.

    Attributes:
        results (MutableSequence[google.shopping.merchant_reports_v1alpha.types.ReportRow]):
            Rows that matched the search query.
        next_page_token (str):
            Token which can be sent as ``page_token`` to retrieve the
            next page. If omitted, there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence["ReportRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReportRow",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportRow(proto.Message):
    r"""Result row returned from the search query.

    Only the message corresponding to the queried table is populated
    in the response. Within the populated message, only the fields
    requested explicitly in the query are populated.

    Attributes:
        product_performance_view (google.shopping.merchant_reports_v1alpha.types.ProductPerformanceView):
            Fields available for query in ``product_performance_view``
            table.
        non_product_performance_view (google.shopping.merchant_reports_v1alpha.types.NonProductPerformanceView):
            Fields available for query in
            ``non_product_performance_view`` table.
        product_view (google.shopping.merchant_reports_v1alpha.types.ProductView):
            Fields available for query in ``product_view`` table.
        price_competitiveness_product_view (google.shopping.merchant_reports_v1alpha.types.PriceCompetitivenessProductView):
            Fields available for query in
            ``price_competitiveness_product_view`` table.
        price_insights_product_view (google.shopping.merchant_reports_v1alpha.types.PriceInsightsProductView):
            Fields available for query in
            ``price_insights_product_view`` table.
        best_sellers_product_cluster_view (google.shopping.merchant_reports_v1alpha.types.BestSellersProductClusterView):
            Fields available for query in
            ``best_sellers_product_cluster_view`` table.
        best_sellers_brand_view (google.shopping.merchant_reports_v1alpha.types.BestSellersBrandView):
            Fields available for query in ``best_sellers_brand_view``
            table.
        competitive_visibility_competitor_view (google.shopping.merchant_reports_v1alpha.types.CompetitiveVisibilityCompetitorView):
            Fields available for query in
            ``competitive_visibility_competitor_view`` table.
        competitive_visibility_top_merchant_view (google.shopping.merchant_reports_v1alpha.types.CompetitiveVisibilityTopMerchantView):
            Fields available for query in
            ``competitive_visibility_top_merchant_view`` table.
        competitive_visibility_benchmark_view (google.shopping.merchant_reports_v1alpha.types.CompetitiveVisibilityBenchmarkView):
            Fields available for query in
            ``competitive_visibility_benchmark_view`` table.
        youtube_creator_performance_view (google.shopping.merchant_reports_v1alpha.types.YoutubeCreatorPerformanceView):
            Fields available for query in
            ``youtube_creator_performance_view`` table.
        youtube_content_performance_view (google.shopping.merchant_reports_v1alpha.types.YoutubeContentPerformanceView):
            Fields available for query in
            ``youtube_content_performance_view`` table.
        youtube_product_performance_view (google.shopping.merchant_reports_v1alpha.types.YoutubeProductPerformanceView):
            Fields available for query in
            ``youtube_product_performance_view`` table.
    """

    product_performance_view: "ProductPerformanceView" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ProductPerformanceView",
    )
    non_product_performance_view: "NonProductPerformanceView" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="NonProductPerformanceView",
    )
    product_view: "ProductView" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProductView",
    )
    price_competitiveness_product_view: "PriceCompetitivenessProductView" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PriceCompetitivenessProductView",
    )
    price_insights_product_view: "PriceInsightsProductView" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PriceInsightsProductView",
    )
    best_sellers_product_cluster_view: "BestSellersProductClusterView" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="BestSellersProductClusterView",
    )
    best_sellers_brand_view: "BestSellersBrandView" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="BestSellersBrandView",
    )
    competitive_visibility_competitor_view: "CompetitiveVisibilityCompetitorView" = (
        proto.Field(
            proto.MESSAGE,
            number=8,
            message="CompetitiveVisibilityCompetitorView",
        )
    )
    competitive_visibility_top_merchant_view: "CompetitiveVisibilityTopMerchantView" = (
        proto.Field(
            proto.MESSAGE,
            number=9,
            message="CompetitiveVisibilityTopMerchantView",
        )
    )
    competitive_visibility_benchmark_view: "CompetitiveVisibilityBenchmarkView" = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            message="CompetitiveVisibilityBenchmarkView",
        )
    )
    youtube_creator_performance_view: "YoutubeCreatorPerformanceView" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="YoutubeCreatorPerformanceView",
    )
    youtube_content_performance_view: "YoutubeContentPerformanceView" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="YoutubeContentPerformanceView",
    )
    youtube_product_performance_view: "YoutubeProductPerformanceView" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="YoutubeProductPerformanceView",
    )


class ProductPerformanceView(proto.Message):
    r"""Fields available for query in ``product_performance_view`` table.

    Product performance data for your account, including performance
    metrics (for example, ``clicks``) and dimensions according to which
    performance metrics are segmented (for example, ``offer_id``).
    Values of product dimensions, such as ``offer_id``, reflect the
    state of a product at the time of the impression.

    Segment fields cannot be selected in queries without also selecting
    at least one metric field.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        marketing_method (google.shopping.merchant_reports_v1alpha.types.MarketingMethod.MarketingMethodEnum):
            Marketing method to which metrics apply.
            Segment.

            This field is a member of `oneof`_ ``_marketing_method``.
        date (google.type.date_pb2.Date):
            Date in the merchant timezone to which metrics apply.
            Segment.

            Condition on ``date`` is required in the ``WHERE`` clause.
        week (google.type.date_pb2.Date):
            First day of the week (Monday) of the metrics
            date in the merchant timezone. Segment.
        customer_country_code (str):
            Code of the country where the customer is
            located at the time of the event. Represented in
            the ISO 3166 format. Segment.

            If the customer country cannot be determined, a
            special 'ZZ' code is returned.

            This field is a member of `oneof`_ ``_customer_country_code``.
        offer_id (str):
            Merchant-provided id of the product. Segment.

            This field is a member of `oneof`_ ``_offer_id``.
        title (str):
            Title of the product. Segment.

            This field is a member of `oneof`_ ``_title``.
        brand (str):
            Brand of the product. Segment.

            This field is a member of `oneof`_ ``_brand``.
        category_l1 (str):
            `Product category (1st
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in Google's product taxonomy. Segment.

            This field is a member of `oneof`_ ``_category_l1``.
        category_l2 (str):
            `Product category (2nd
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in Google's product taxonomy. Segment.

            This field is a member of `oneof`_ ``_category_l2``.
        category_l3 (str):
            `Product category (3rd
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in Google's product taxonomy. Segment.

            This field is a member of `oneof`_ ``_category_l3``.
        category_l4 (str):
            `Product category (4th
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in Google's product taxonomy. Segment.

            This field is a member of `oneof`_ ``_category_l4``.
        category_l5 (str):
            `Product category (5th
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in Google's product taxonomy. Segment.

            This field is a member of `oneof`_ ``_category_l5``.
        product_type_l1 (str):
            `Product type (1st
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in merchant's own product taxonomy. Segment.

            This field is a member of `oneof`_ ``_product_type_l1``.
        product_type_l2 (str):
            `Product type (2nd
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in merchant's own product taxonomy. Segment.

            This field is a member of `oneof`_ ``_product_type_l2``.
        product_type_l3 (str):
            `Product type (3rd
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in merchant's own product taxonomy. Segment.

            This field is a member of `oneof`_ ``_product_type_l3``.
        product_type_l4 (str):
            `Product type (4th
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in merchant's own product taxonomy. Segment.

            This field is a member of `oneof`_ ``_product_type_l4``.
        product_type_l5 (str):
            `Product type (5th
            level) <https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type>`__
            in merchant's own product taxonomy. Segment.

            This field is a member of `oneof`_ ``_product_type_l5``.
        custom_label0 (str):
            Custom label 0 for custom grouping of
            products. Segment.

            This field is a member of `oneof`_ ``_custom_label0``.
        custom_label1 (str):
            Custom label 1 for custom grouping of
            products. Segment.

            This field is a member of `oneof`_ ``_custom_label1``.
        custom_label2 (str):
            Custom label 2 for custom grouping of
            products. Segment.

            This field is a member of `oneof`_ ``_custom_label2``.
        custom_label3 (str):
            Custom label 3 for custom grouping of
            products. Segment.

            This field is a member of `oneof`_ ``_custom_label3``.
        custom_label4 (str):
            Custom label 4 for custom grouping of
            products. Segment.

            This field is a member of `oneof`_ ``_custom_label4``.
        clicks (int):
            Number of clicks. Metric.

            This field is a member of `oneof`_ ``_clicks``.
        impressions (int):
            Number of times merchant's products are
            shown. Metric.

            This field is a member of `oneof`_ ``_impressions``.
        click_through_rate (float):
            Click-through rate - the number of clicks
            merchant's products receive (clicks) divided by
            the number of times the products are shown
            (impressions). Metric.

            This field is a member of `oneof`_ ``_click_through_rate``.
        conversions (float):
            Number of conversions attributed to the product, reported on
            the conversion date. Depending on the attribution model, a
            conversion might be distributed across multiple clicks,
            where each click gets its own credit assigned. This metric
            is a sum of all such credits. Metric.

            Available only for the ``FREE`` traffic source.

            This field is a member of `oneof`_ ``_conversions``.
        conversion_value (google.shopping.type.types.Price):
            Value of conversions attributed to the product, reported on
            the conversion date. Metric.

            Available only for the ``FREE`` traffic source.
        conversion_rate (float):
            Number of conversions divided by the number of clicks,
            reported on the impression date. Metric.

            Available only for the ``FREE`` traffic source.

            This field is a member of `oneof`_ ``_conversion_rate``.
    """

    marketing_method: "MarketingMethod.MarketingMethodEnum" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="MarketingMethod.MarketingMethodEnum",
    )
    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    week: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        message=date_pb2.Date,
    )
    customer_country_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    category_l1: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    category_l2: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    category_l3: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    category_l4: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    category_l5: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    product_type_l1: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    product_type_l2: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    product_type_l3: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    product_type_l4: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    product_type_l5: str = proto.Field(
        proto.STRING,
        number=17,
        optional=True,
    )
    custom_label0: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    custom_label1: str = proto.Field(
        proto.STRING,
        number=19,
        optional=True,
    )
    custom_label2: str = proto.Field(
        proto.STRING,
        number=20,
        optional=True,
    )
    custom_label3: str = proto.Field(
        proto.STRING,
        number=21,
        optional=True,
    )
    custom_label4: str = proto.Field(
        proto.STRING,
        number=22,
        optional=True,
    )
    clicks: int = proto.Field(
        proto.INT64,
        number=23,
        optional=True,
    )
    impressions: int = proto.Field(
        proto.INT64,
        number=24,
        optional=True,
    )
    click_through_rate: float = proto.Field(
        proto.DOUBLE,
        number=25,
        optional=True,
    )
    conversions: float = proto.Field(
        proto.DOUBLE,
        number=26,
        optional=True,
    )
    conversion_value: types.Price = proto.Field(
        proto.MESSAGE,
        number=27,
        message=types.Price,
    )
    conversion_rate: float = proto.Field(
        proto.DOUBLE,
        number=28,
        optional=True,
    )


class ProductView(proto.Message):
    r"""Fields available for query in ``product_view`` table.

    Products in the current inventory. Products in this table are the
    same as in Products sub-API but not all product attributes from
    Products sub-API are available for query in this table. In contrast
    to Products sub-API, this table allows to filter the returned list
    of products by product attributes. To retrieve a single product by
    ``id`` or list all products, Products sub-API should be used.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            REST ID of the product, in the form of
            ``channel~languageCode~feedLabel~offerId``. Merchant API
            methods that operate on products take this as their ``name``
            parameter.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_id``.
        channel (google.shopping.type.types.Channel.ChannelEnum):
            Channel of the product. Can be ``ONLINE`` or ``LOCAL``.

            This field is a member of `oneof`_ ``_channel``.
        language_code (str):
            Language code of the product in BCP 47
            format.

            This field is a member of `oneof`_ ``_language_code``.
        feed_label (str):
            Feed label of the product.

            This field is a member of `oneof`_ ``_feed_label``.
        offer_id (str):
            Merchant-provided id of the product.

            This field is a member of `oneof`_ ``_offer_id``.
        title (str):
            Title of the product.

            This field is a member of `oneof`_ ``_title``.
        brand (str):
            Brand of the product.

            This field is a member of `oneof`_ ``_brand``.
        category_l1 (str):
            Product category (1st level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l1``.
        category_l2 (str):
            Product category (2nd level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l2``.
        category_l3 (str):
            Product category (3rd level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l3``.
        category_l4 (str):
            Product category (4th level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l4``.
        category_l5 (str):
            Product category (5th level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l5``.
        product_type_l1 (str):
            Product type (1st level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l1``.
        product_type_l2 (str):
            Product type (2nd level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l2``.
        product_type_l3 (str):
            Product type (3rd level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l3``.
        product_type_l4 (str):
            Product type (4th level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l4``.
        product_type_l5 (str):
            Product type (5th level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l5``.
        price (google.shopping.type.types.Price):
            Product price. Absent if the information
            about the price of the product is not available.
        condition (str):
            `Condition <https://support.google.com/merchants/answer/6324469>`__
            of the product.

            This field is a member of `oneof`_ ``_condition``.
        availability (str):
            `Availability <https://support.google.com/merchants/answer/6324448>`__
            of the product.

            This field is a member of `oneof`_ ``_availability``.
        shipping_label (str):
            Normalized `shipping
            label <https://support.google.com/merchants/answer/6324504>`__
            specified in the data source.

            This field is a member of `oneof`_ ``_shipping_label``.
        gtin (MutableSequence[str]):
            List of Global Trade Item Numbers (GTINs) of
            the product.
        item_group_id (str):
            Item group id provided by the merchant for
            grouping variants together.

            This field is a member of `oneof`_ ``_item_group_id``.
        thumbnail_link (str):
            Link to the processed image of the product,
            hosted on the Google infrastructure.

            This field is a member of `oneof`_ ``_thumbnail_link``.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the merchant created the product in
            timestamp seconds.
        expiration_date (google.type.date_pb2.Date):
            Expiration date for the product, specified on
            insertion.
        aggregated_reporting_context_status (google.shopping.merchant_reports_v1alpha.types.ProductView.AggregatedReportingContextStatus):
            Aggregated status.

            This field is a member of `oneof`_ ``_aggregated_reporting_context_status``.
        item_issues (MutableSequence[google.shopping.merchant_reports_v1alpha.types.ProductView.ItemIssue]):
            List of item issues for the product.

            **This field cannot be used for sorting the results.**

            **Only selected attributes of this field (for example,
            ``item_issues.severity.aggregated_severity``) can be used
            for filtering the results.**
        click_potential (google.shopping.merchant_reports_v1alpha.types.ProductView.ClickPotential):
            Estimated performance potential compared to
            highest performing products of the merchant.
        click_potential_rank (int):
            Rank of the product based on its click potential. A product
            with ``click_potential_rank`` 1 has the highest click
            potential among the merchant's products that fulfill the
            search query conditions.

            This field is a member of `oneof`_ ``_click_potential_rank``.
    """

    class AggregatedReportingContextStatus(proto.Enum):
        r"""Status of the product aggregated for all reporting contexts.

        Here's an example of how the aggregated status is computed:

        Free listings \| Shopping ads \| Status
        --------------\|--------------\|------------------------------
        Approved \| Approved \| ELIGIBLE Approved \| Pending \| ELIGIBLE
        Approved \| Disapproved \| ELIGIBLE_LIMITED Pending \| Pending \|
        PENDING Disapproved \| Disapproved \| NOT_ELIGIBLE_OR_DISAPPROVED

        Values:
            AGGREGATED_REPORTING_CONTEXT_STATUS_UNSPECIFIED (0):
                Not specified.
            NOT_ELIGIBLE_OR_DISAPPROVED (1):
                Product is not eligible or is disapproved for
                all reporting contexts.
            PENDING (2):
                Product's status is pending in all reporting
                contexts.
            ELIGIBLE_LIMITED (3):
                Product is eligible for some (but not all)
                reporting contexts.
            ELIGIBLE (4):
                Product is eligible for all reporting
                contexts.
        """

        AGGREGATED_REPORTING_CONTEXT_STATUS_UNSPECIFIED = 0
        NOT_ELIGIBLE_OR_DISAPPROVED = 1
        PENDING = 2
        ELIGIBLE_LIMITED = 3
        ELIGIBLE = 4

    class ClickPotential(proto.Enum):
        r"""A product's `click
        potential <https://support.google.com/merchants/answer/188488>`__
        estimates its performance potential compared to highest performing
        products of the merchant. Click potential of a product helps
        merchants to prioritize which products to fix and helps them
        understand how products are performing against their potential.

        Values:
            CLICK_POTENTIAL_UNSPECIFIED (0):
                Unknown predicted clicks impact.
            LOW (1):
                Potential to receive a low number of clicks
                compared to the highest performing products of
                the merchant.
            MEDIUM (2):
                Potential to receive a moderate number of
                clicks compared to the highest performing
                products of the merchant.
            HIGH (3):
                Potential to receive a similar number of
                clicks as the highest performing products of the
                merchant.
        """

        CLICK_POTENTIAL_UNSPECIFIED = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    class ItemIssue(proto.Message):
        r"""Item issue associated with the product.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.shopping.merchant_reports_v1alpha.types.ProductView.ItemIssue.ItemIssueType):
                Item issue type.
            severity (google.shopping.merchant_reports_v1alpha.types.ProductView.ItemIssue.ItemIssueSeverity):
                Item issue severity.
            resolution (google.shopping.merchant_reports_v1alpha.types.ProductView.ItemIssue.ItemIssueResolution):
                Item issue resolution.

                This field is a member of `oneof`_ ``_resolution``.
        """

        class ItemIssueResolution(proto.Enum):
            r"""How to resolve the issue.

            Values:
                ITEM_ISSUE_RESOLUTION_UNSPECIFIED (0):
                    Not specified.
                MERCHANT_ACTION (1):
                    The merchant has to fix the issue.
                PENDING_PROCESSING (2):
                    The issue will be resolved automatically (for
                    example, image crawl) or through a Google
                    review. No merchant action is required now.
                    Resolution might lead to another issue (for
                    example, if crawl fails).
            """

            ITEM_ISSUE_RESOLUTION_UNSPECIFIED = 0
            MERCHANT_ACTION = 1
            PENDING_PROCESSING = 2

        class ItemIssueType(proto.Message):
            r"""Issue type.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                code (str):
                    Error code of the issue, equivalent to the ``code`` of
                    `Product
                    issues <https://developers.google.com/shopping-content/guides/product-issues>`__.

                    This field is a member of `oneof`_ ``_code``.
                canonical_attribute (str):
                    Canonical attribute name for
                    attribute-specific issues.

                    This field is a member of `oneof`_ ``_canonical_attribute``.
            """

            code: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            canonical_attribute: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )

        class ItemIssueSeverity(proto.Message):
            r"""How the issue affects the serving of the product.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                severity_per_reporting_context (MutableSequence[google.shopping.merchant_reports_v1alpha.types.ProductView.ItemIssue.ItemIssueSeverity.IssueSeverityPerReportingContext]):
                    Issue severity per reporting context.
                aggregated_severity (google.shopping.merchant_reports_v1alpha.types.ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity):
                    Aggregated severity of the issue for all reporting contexts
                    it affects.

                    **This field can be used for filtering the results.**

                    This field is a member of `oneof`_ ``_aggregated_severity``.
            """

            class AggregatedIssueSeverity(proto.Enum):
                r"""Issue severity aggregated for all reporting contexts.

                Values:
                    AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED (0):
                        Not specified.
                    DISAPPROVED (1):
                        Issue disapproves the product in at least one
                        reporting context.
                    DEMOTED (2):
                        Issue demotes the product in all reporting
                        contexts it affects.
                    PENDING (3):
                        Issue resolution is ``PENDING_PROCESSING``.
                """

                AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED = 0
                DISAPPROVED = 1
                DEMOTED = 2
                PENDING = 3

            class IssueSeverityPerReportingContext(proto.Message):
                r"""Issue severity per reporting context.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                        Reporting context the issue applies to.

                        This field is a member of `oneof`_ ``_reporting_context``.
                    disapproved_countries (MutableSequence[str]):
                        List of disapproved countries in the
                        reporting context, represented in ISO 3166
                        format.
                    demoted_countries (MutableSequence[str]):
                        List of demoted countries in the reporting
                        context, represented in ISO 3166 format.
                """

                reporting_context: types.ReportingContext.ReportingContextEnum = (
                    proto.Field(
                        proto.ENUM,
                        number=1,
                        optional=True,
                        enum=types.ReportingContext.ReportingContextEnum,
                    )
                )
                disapproved_countries: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=2,
                )
                demoted_countries: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=3,
                )

            severity_per_reporting_context: MutableSequence[
                "ProductView.ItemIssue.ItemIssueSeverity.IssueSeverityPerReportingContext"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ProductView.ItemIssue.ItemIssueSeverity.IssueSeverityPerReportingContext",
            )
            aggregated_severity: "ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity" = proto.Field(
                proto.ENUM,
                number=2,
                optional=True,
                enum="ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity",
            )

        type_: "ProductView.ItemIssue.ItemIssueType" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="ProductView.ItemIssue.ItemIssueType",
        )
        severity: "ProductView.ItemIssue.ItemIssueSeverity" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ProductView.ItemIssue.ItemIssueSeverity",
        )
        resolution: "ProductView.ItemIssue.ItemIssueResolution" = proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum="ProductView.ItemIssue.ItemIssueResolution",
        )

    id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    channel: types.Channel.ChannelEnum = proto.Field(
        proto.ENUM,
        number=28,
        optional=True,
        enum=types.Channel.ChannelEnum,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    category_l1: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    category_l2: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    category_l3: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    category_l4: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    category_l5: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    product_type_l1: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    product_type_l2: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    product_type_l3: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    product_type_l4: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    product_type_l5: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=17,
        message=types.Price,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    availability: str = proto.Field(
        proto.STRING,
        number=19,
        optional=True,
    )
    shipping_label: str = proto.Field(
        proto.STRING,
        number=20,
        optional=True,
    )
    gtin: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=21,
    )
    item_group_id: str = proto.Field(
        proto.STRING,
        number=22,
        optional=True,
    )
    thumbnail_link: str = proto.Field(
        proto.STRING,
        number=23,
        optional=True,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    expiration_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=25,
        message=date_pb2.Date,
    )
    aggregated_reporting_context_status: AggregatedReportingContextStatus = proto.Field(
        proto.ENUM,
        number=26,
        optional=True,
        enum=AggregatedReportingContextStatus,
    )
    item_issues: MutableSequence[ItemIssue] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message=ItemIssue,
    )
    click_potential: ClickPotential = proto.Field(
        proto.ENUM,
        number=29,
        enum=ClickPotential,
    )
    click_potential_rank: int = proto.Field(
        proto.INT64,
        number=30,
        optional=True,
    )


class PriceCompetitivenessProductView(proto.Message):
    r"""Fields available for query in ``price_competitiveness_product_view``
    table.

    `Price
    competitiveness <https://support.google.com/merchants/answer/9626903>`__
    report.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        report_country_code (str):
            Country of the price benchmark. Represented in the ISO 3166
            format.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_report_country_code``.
        id (str):
            REST ID of the product, in the form of
            ``channel~languageCode~feedLabel~offerId``. Can be used to
            join data with the ``product_view`` table.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_id``.
        offer_id (str):
            Merchant-provided id of the product.

            This field is a member of `oneof`_ ``_offer_id``.
        title (str):
            Title of the product.

            This field is a member of `oneof`_ ``_title``.
        brand (str):
            Brand of the product.

            This field is a member of `oneof`_ ``_brand``.
        category_l1 (str):
            Product category (1st level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l1``.
        category_l2 (str):
            Product category (2nd level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l2``.
        category_l3 (str):
            Product category (3rd level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l3``.
        category_l4 (str):
            Product category (4th level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l4``.
        category_l5 (str):
            Product category (5th level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l5``.
        product_type_l1 (str):
            Product type (1st level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l1``.
        product_type_l2 (str):
            Product type (2nd level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l2``.
        product_type_l3 (str):
            Product type (3rd level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l3``.
        product_type_l4 (str):
            Product type (4th level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l4``.
        product_type_l5 (str):
            Product type (5th level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l5``.
        price (google.shopping.type.types.Price):
            Current price of the product.
        benchmark_price (google.shopping.type.types.Price):
            Latest available price benchmark for the
            product's catalog in the benchmark country.
    """

    report_country_code: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    category_l1: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    category_l2: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    category_l3: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    category_l4: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    category_l5: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    product_type_l1: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    product_type_l2: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    product_type_l3: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    product_type_l4: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    product_type_l5: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=16,
        message=types.Price,
    )
    benchmark_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=17,
        message=types.Price,
    )


class PriceInsightsProductView(proto.Message):
    r"""Fields available for query in ``price_insights_product_view`` table.

    `Price
    insights <https://support.google.com/merchants/answer/11916926>`__
    report.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            REST ID of the product, in the form of
            ``channel~languageCode~feedLabel~offerId``. Can be used to
            join data with the ``product_view`` table.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_id``.
        offer_id (str):
            Merchant-provided id of the product.

            This field is a member of `oneof`_ ``_offer_id``.
        title (str):
            Title of the product.

            This field is a member of `oneof`_ ``_title``.
        brand (str):
            Brand of the product.

            This field is a member of `oneof`_ ``_brand``.
        category_l1 (str):
            Product category (1st level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l1``.
        category_l2 (str):
            Product category (2nd level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l2``.
        category_l3 (str):
            Product category (3rd level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l3``.
        category_l4 (str):
            Product category (4th level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l4``.
        category_l5 (str):
            Product category (5th level) in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l5``.
        product_type_l1 (str):
            Product type (1st level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l1``.
        product_type_l2 (str):
            Product type (2nd level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l2``.
        product_type_l3 (str):
            Product type (3rd level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l3``.
        product_type_l4 (str):
            Product type (4th level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l4``.
        product_type_l5 (str):
            Product type (5th level) in merchant's own `product
            taxonomy <https://support.google.com/merchants/answer/6324406>`__.

            This field is a member of `oneof`_ ``_product_type_l5``.
        price (google.shopping.type.types.Price):
            Current price of the product.
        suggested_price (google.shopping.type.types.Price):
            Latest suggested price for the product.
        predicted_impressions_change_fraction (float):
            Predicted change in impressions as a fraction
            after introducing the suggested price compared
            to current active price. For example, 0.05 is a
            5% predicted increase in impressions.

            This field is a member of `oneof`_ ``_predicted_impressions_change_fraction``.
        predicted_clicks_change_fraction (float):
            Predicted change in clicks as a fraction
            after introducing the suggested price compared
            to current active price. For example, 0.05 is a
            5% predicted increase in clicks.

            This field is a member of `oneof`_ ``_predicted_clicks_change_fraction``.
        predicted_conversions_change_fraction (float):
            Predicted change in conversions as a fraction
            after introducing the suggested price compared
            to current active price. For example, 0.05 is a
            5% predicted increase in conversions).

            This field is a member of `oneof`_ ``_predicted_conversions_change_fraction``.
        effectiveness (google.shopping.merchant_reports_v1alpha.types.PriceInsightsProductView.Effectiveness):
            The predicted effectiveness of applying the
            price suggestion, bucketed.
    """

    class Effectiveness(proto.Enum):
        r"""Predicted effectiveness bucket.

        Effectiveness indicates which products would benefit most from price
        changes. This rating takes into consideration the performance boost
        predicted by adjusting the sale price and the difference between
        your current price and the suggested price. Price suggestions with
        ``HIGH`` effectiveness are predicted to drive the largest increase
        in performance.

        Values:
            EFFECTIVENESS_UNSPECIFIED (0):
                Effectiveness is unknown.
            LOW (1):
                Effectiveness is low.
            MEDIUM (2):
                Effectiveness is medium.
            HIGH (3):
                Effectiveness is high.
        """

        EFFECTIVENESS_UNSPECIFIED = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    category_l1: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    category_l2: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    category_l3: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    category_l4: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    category_l5: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    product_type_l1: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    product_type_l2: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    product_type_l3: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    product_type_l4: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    product_type_l5: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=15,
        message=types.Price,
    )
    suggested_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=16,
        message=types.Price,
    )
    predicted_impressions_change_fraction: float = proto.Field(
        proto.DOUBLE,
        number=17,
        optional=True,
    )
    predicted_clicks_change_fraction: float = proto.Field(
        proto.DOUBLE,
        number=18,
        optional=True,
    )
    predicted_conversions_change_fraction: float = proto.Field(
        proto.DOUBLE,
        number=19,
        optional=True,
    )
    effectiveness: Effectiveness = proto.Field(
        proto.ENUM,
        number=22,
        enum=Effectiveness,
    )


class BestSellersProductClusterView(proto.Message):
    r"""Fields available for query in ``best_sellers_product_cluster_view``
    table.

    `Best
    sellers <https://support.google.com/merchants/answer/9488679>`__
    report with top product clusters. A product cluster is a grouping
    for different offers and variants that represent the same product,
    for example, Google Pixel 7.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        report_date (google.type.date_pb2.Date):
            Report date. The value of this field can only be one of the
            following:

            - The first day of the week (Monday) for weekly reports,
            - The first day of the month for monthly reports.

            Required in the ``SELECT`` clause. If a ``WHERE`` condition
            on ``report_date`` is not specified in the query, the latest
            available weekly or monthly report is returned.
        report_granularity (google.shopping.merchant_reports_v1alpha.types.ReportGranularity.ReportGranularityEnum):
            Granularity of the report. The ranking can be done over a
            week or a month timeframe.

            Required in the ``SELECT`` clause. Condition on
            ``report_granularity`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_granularity``.
        report_country_code (str):
            Country where the ranking is calculated. Represented in the
            ISO 3166 format.

            Required in the ``SELECT`` clause. Condition on
            ``report_country_code`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_country_code``.
        report_category_id (int):
            Google product category ID to calculate the ranking for,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            Required in the ``SELECT`` clause. If a ``WHERE`` condition
            on ``report_category_id`` is not specified in the query,
            rankings for all top-level categories are returned.

            This field is a member of `oneof`_ ``_report_category_id``.
        title (str):
            Title of the product cluster.

            This field is a member of `oneof`_ ``_title``.
        brand (str):
            Brand of the product cluster.

            This field is a member of `oneof`_ ``_brand``.
        category_l1 (str):
            Product category (1st level) of the product cluster,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l1``.
        category_l2 (str):
            Product category (2nd level) of the product cluster,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l2``.
        category_l3 (str):
            Product category (3rd level) of the product cluster,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l3``.
        category_l4 (str):
            Product category (4th level) of the product cluster,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l4``.
        category_l5 (str):
            Product category (5th level) of the product cluster,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            This field is a member of `oneof`_ ``_category_l5``.
        variant_gtins (MutableSequence[str]):
            GTINs of example variants of the product
            cluster.
        inventory_status (google.shopping.merchant_reports_v1alpha.types.BestSellersProductClusterView.InventoryStatus):
            Whether the product cluster is ``IN_STOCK`` in your product
            data source in at least one of the countries,
            ``OUT_OF_STOCK`` in your product data source in all
            countries, or ``NOT_IN_INVENTORY`` at all.

            The field doesn't take the Best sellers report country
            filter into account.

            This field is a member of `oneof`_ ``_inventory_status``.
        brand_inventory_status (google.shopping.merchant_reports_v1alpha.types.BestSellersProductClusterView.InventoryStatus):
            Whether there is at least one product of the brand currently
            ``IN_STOCK`` in your product data source in at least one of
            the countries, all products are ``OUT_OF_STOCK`` in your
            product data source in all countries, or
            ``NOT_IN_INVENTORY``.

            The field doesn't take the Best sellers report country
            filter into account.

            This field is a member of `oneof`_ ``_brand_inventory_status``.
        rank (int):
            Popularity of the product cluster on Ads and
            organic surfaces, in the selected category and
            country, based on the estimated number of units
            sold.

            This field is a member of `oneof`_ ``_rank``.
        previous_rank (int):
            Popularity rank in the previous week or
            month.

            This field is a member of `oneof`_ ``_previous_rank``.
        relative_demand (google.shopping.merchant_reports_v1alpha.types.RelativeDemand.RelativeDemandEnum):
            Estimated demand in relation to the product
            cluster with the highest popularity rank in the
            same category and country.

            This field is a member of `oneof`_ ``_relative_demand``.
        previous_relative_demand (google.shopping.merchant_reports_v1alpha.types.RelativeDemand.RelativeDemandEnum):
            Estimated demand in relation to the product
            cluster with the highest popularity rank in the
            same category and country in the previous week
            or month.

            This field is a member of `oneof`_ ``_previous_relative_demand``.
        relative_demand_change (google.shopping.merchant_reports_v1alpha.types.RelativeDemandChangeType.RelativeDemandChangeTypeEnum):
            Change in the estimated demand. Whether it
            rose, sank or remained flat.

            This field is a member of `oneof`_ ``_relative_demand_change``.
    """

    class InventoryStatus(proto.Enum):
        r"""Status of the product cluster or brand in your inventory.

        Values:
            INVENTORY_STATUS_UNSPECIFIED (0):
                Not specified.
            IN_STOCK (1):
                You have a product for this product cluster
                or brand in stock.
            OUT_OF_STOCK (2):
                You have a product for this product cluster
                or brand in inventory but it is currently out of
                stock.
            NOT_IN_INVENTORY (3):
                You do not have a product for this product
                cluster or brand in inventory.
        """

        INVENTORY_STATUS_UNSPECIFIED = 0
        IN_STOCK = 1
        OUT_OF_STOCK = 2
        NOT_IN_INVENTORY = 3

    report_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    report_granularity: "ReportGranularity.ReportGranularityEnum" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="ReportGranularity.ReportGranularityEnum",
    )
    report_country_code: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    report_category_id: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    category_l1: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    category_l2: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    category_l3: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    category_l4: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    category_l5: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    variant_gtins: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    inventory_status: InventoryStatus = proto.Field(
        proto.ENUM,
        number=14,
        optional=True,
        enum=InventoryStatus,
    )
    brand_inventory_status: InventoryStatus = proto.Field(
        proto.ENUM,
        number=15,
        optional=True,
        enum=InventoryStatus,
    )
    rank: int = proto.Field(
        proto.INT64,
        number=16,
        optional=True,
    )
    previous_rank: int = proto.Field(
        proto.INT64,
        number=17,
        optional=True,
    )
    relative_demand: "RelativeDemand.RelativeDemandEnum" = proto.Field(
        proto.ENUM,
        number=18,
        optional=True,
        enum="RelativeDemand.RelativeDemandEnum",
    )
    previous_relative_demand: "RelativeDemand.RelativeDemandEnum" = proto.Field(
        proto.ENUM,
        number=19,
        optional=True,
        enum="RelativeDemand.RelativeDemandEnum",
    )
    relative_demand_change: "RelativeDemandChangeType.RelativeDemandChangeTypeEnum" = (
        proto.Field(
            proto.ENUM,
            number=20,
            optional=True,
            enum="RelativeDemandChangeType.RelativeDemandChangeTypeEnum",
        )
    )


class BestSellersBrandView(proto.Message):
    r"""Fields available for query in ``best_sellers_brand_view`` table.

    `Best
    sellers <https://support.google.com/merchants/answer/9488679>`__
    report with top brands.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        report_date (google.type.date_pb2.Date):
            Report date. The value of this field can only be one of the
            following:

            - The first day of the week (Monday) for weekly reports,
            - The first day of the month for monthly reports.

            Required in the ``SELECT`` clause. If a ``WHERE`` condition
            on ``report_date`` is not specified in the query, the latest
            available weekly or monthly report is returned.
        report_granularity (google.shopping.merchant_reports_v1alpha.types.ReportGranularity.ReportGranularityEnum):
            Granularity of the report. The ranking can be done over a
            week or a month timeframe.

            Required in the ``SELECT`` clause. Condition on
            ``report_granularity`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_granularity``.
        report_country_code (str):
            Country where the ranking is calculated. Represented in the
            ISO 3166 format.

            Required in the ``SELECT`` clause. Condition on
            ``report_country_code`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_country_code``.
        report_category_id (int):
            Google product category ID to calculate the ranking for,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            Required in the ``SELECT`` clause. If a ``WHERE`` condition
            on ``report_category_id`` is not specified in the query,
            rankings for all top-level categories are returned.

            This field is a member of `oneof`_ ``_report_category_id``.
        brand (str):
            Name of the brand.

            This field is a member of `oneof`_ ``_brand``.
        rank (int):
            Popularity of the brand on Ads and organic
            surfaces, in the selected category and country,
            based on the estimated number of units sold.

            This field is a member of `oneof`_ ``_rank``.
        previous_rank (int):
            Popularity rank in the previous week or
            month.

            This field is a member of `oneof`_ ``_previous_rank``.
        relative_demand (google.shopping.merchant_reports_v1alpha.types.RelativeDemand.RelativeDemandEnum):
            Estimated demand in relation to the brand
            with the highest popularity rank in the same
            category and country.

            This field is a member of `oneof`_ ``_relative_demand``.
        previous_relative_demand (google.shopping.merchant_reports_v1alpha.types.RelativeDemand.RelativeDemandEnum):
            Estimated demand in relation to the brand
            with the highest popularity rank in the same
            category and country in the previous week or
            month.

            This field is a member of `oneof`_ ``_previous_relative_demand``.
        relative_demand_change (google.shopping.merchant_reports_v1alpha.types.RelativeDemandChangeType.RelativeDemandChangeTypeEnum):
            Change in the estimated demand. Whether it
            rose, sank or remained flat.

            This field is a member of `oneof`_ ``_relative_demand_change``.
    """

    report_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    report_granularity: "ReportGranularity.ReportGranularityEnum" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="ReportGranularity.ReportGranularityEnum",
    )
    report_country_code: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    report_category_id: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    rank: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    previous_rank: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    relative_demand: "RelativeDemand.RelativeDemandEnum" = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum="RelativeDemand.RelativeDemandEnum",
    )
    previous_relative_demand: "RelativeDemand.RelativeDemandEnum" = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum="RelativeDemand.RelativeDemandEnum",
    )
    relative_demand_change: "RelativeDemandChangeType.RelativeDemandChangeTypeEnum" = (
        proto.Field(
            proto.ENUM,
            number=11,
            optional=True,
            enum="RelativeDemandChangeType.RelativeDemandChangeTypeEnum",
        )
    )


class NonProductPerformanceView(proto.Message):
    r"""Fields available for query in ``non_product_performance_view``
    table.

    Performance data on images and online store links leading to your
    non-product pages. This includes performance metrics (for example,
    ``clicks``) and dimensions according to which performance metrics
    are segmented (for example, ``date``).

    Segment fields cannot be selected in queries without also selecting
    at least one metric field.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date in the merchant timezone to which metrics apply.
            Segment.

            Condition on ``date`` is required in the ``WHERE`` clause.
        week (google.type.date_pb2.Date):
            First day of the week (Monday) of the metrics
            date in the merchant timezone. Segment.
        clicks (int):
            Number of clicks on images and online store
            links leading to your non-product pages. Metric.

            This field is a member of `oneof`_ ``_clicks``.
        impressions (int):
            Number of times images and online store links
            leading to your non-product pages were shown.
            Metric.

            This field is a member of `oneof`_ ``_impressions``.
        click_through_rate (float):
            Click-through rate - the number of clicks (``clicks``)
            divided by the number of impressions (``impressions``) of
            images and online store links leading to your non-product
            pages. Metric.

            This field is a member of `oneof`_ ``_click_through_rate``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    week: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    clicks: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    impressions: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    click_through_rate: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )


class CompetitiveVisibilityCompetitorView(proto.Message):
    r"""Fields available for query in
    ``competitive_visibility_competitor_view`` table.

    `Competitive
    visibility <https://support.google.com/merchants/answer/11366442>`__
    report with businesses with similar visibility.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date of this row.

            A condition on ``date`` is required in the ``WHERE`` clause.
        domain (str):
            Domain of your competitor or your domain, if
            'is_your_domain' is true.

            Required in the ``SELECT`` clause. Cannot be filtered on in
            the 'WHERE' clause.

            This field is a member of `oneof`_ ``_domain``.
        is_your_domain (bool):
            True if this row contains data for your
            domain.
            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_is_your_domain``.
        report_country_code (str):
            Country where impressions appeared.

            Required in the ``SELECT`` clause. A condition on
            ``report_country_code`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_country_code``.
        report_category_id (int):
            Google product category ID to calculate the report for,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            Required in the ``SELECT`` clause. A condition on
            ``report_category_id`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_category_id``.
        traffic_source (google.shopping.merchant_reports_v1alpha.types.TrafficSource.TrafficSourceEnum):
            Traffic source of impressions.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_traffic_source``.
        rank (int):
            Position of the domain in the similar businesses ranking for
            the selected keys (``date``, ``report_category_id``,
            ``report_country_code``, ``traffic_source``) based on
            impressions. 1 is the highest.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_rank``.
        ads_organic_ratio (float):
            [Ads / organic ratio]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio)
            shows how often the domain receives impressions from
            Shopping ads compared to organic traffic. The number is
            rounded and bucketed.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_ads_organic_ratio``.
        page_overlap_rate (float):
            [Page overlap rate]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate)
            shows how frequently competing retailers’ offers are shown
            together with your offers on the same page.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_page_overlap_rate``.
        higher_position_rate (float):
            [Higher position rate]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate)
            shows how often a competitor’s offer got placed in a higher
            position on the page than your offer.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_higher_position_rate``.
        relative_visibility (float):
            [Relative visibility]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Crelative-visibility)
            shows how often your competitors’ offers are shown compared
            to your offers. In other words, this is the number of
            displayed impressions of a competitor retailer divided by
            the number of your displayed impressions during a selected
            time range for a selected product category and country.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_relative_visibility``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    is_your_domain: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    report_country_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    report_category_id: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    traffic_source: "TrafficSource.TrafficSourceEnum" = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum="TrafficSource.TrafficSourceEnum",
    )
    rank: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    ads_organic_ratio: float = proto.Field(
        proto.DOUBLE,
        number=8,
        optional=True,
    )
    page_overlap_rate: float = proto.Field(
        proto.DOUBLE,
        number=9,
        optional=True,
    )
    higher_position_rate: float = proto.Field(
        proto.DOUBLE,
        number=10,
        optional=True,
    )
    relative_visibility: float = proto.Field(
        proto.DOUBLE,
        number=11,
        optional=True,
    )


class CompetitiveVisibilityTopMerchantView(proto.Message):
    r"""Fields available for query in
    ``competitive_visibility_top_merchant_view`` table.

    `Competitive
    visibility <https://support.google.com/merchants/answer/11366442>`__
    report with business with highest visibility.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date of this row.

            Cannot be selected in the ``SELECT`` clause. A condition on
            ``date`` is required in the ``WHERE`` clause.
        domain (str):
            Domain of your competitor or your domain, if
            'is_your_domain' is true.

            Required in the ``SELECT`` clause. Cannot be filtered on in
            the 'WHERE' clause.

            This field is a member of `oneof`_ ``_domain``.
        is_your_domain (bool):
            True if this row contains data for your
            domain.
            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_is_your_domain``.
        report_country_code (str):
            Country where impressions appeared.

            Required in the ``SELECT`` clause. A condition on
            ``report_country_code`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_country_code``.
        report_category_id (int):
            Google product category ID to calculate the report for,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            Required in the ``SELECT`` clause. A condition on
            ``report_category_id`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_category_id``.
        traffic_source (google.shopping.merchant_reports_v1alpha.types.TrafficSource.TrafficSourceEnum):
            Traffic source of impressions.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_traffic_source``.
        rank (int):
            Position of the domain in the top merchants ranking for the
            selected keys (``date``, ``report_category_id``,
            ``report_country_code``, ``traffic_source``) based on
            impressions. 1 is the highest.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_rank``.
        ads_organic_ratio (float):
            [Ads / organic ratio]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio)
            shows how often the domain receives impressions from
            Shopping ads compared to organic traffic. The number is
            rounded and bucketed.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_ads_organic_ratio``.
        page_overlap_rate (float):
            [Page overlap rate]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate)
            shows how frequently competing retailers’ offers are shown
            together with your offers on the same page.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_page_overlap_rate``.
        higher_position_rate (float):
            [Higher position rate]
            (https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate)
            shows how often a competitor’s offer got placed in a higher
            position on the page than your offer.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_higher_position_rate``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    is_your_domain: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    report_country_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    report_category_id: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    traffic_source: "TrafficSource.TrafficSourceEnum" = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum="TrafficSource.TrafficSourceEnum",
    )
    rank: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    ads_organic_ratio: float = proto.Field(
        proto.DOUBLE,
        number=8,
        optional=True,
    )
    page_overlap_rate: float = proto.Field(
        proto.DOUBLE,
        number=9,
        optional=True,
    )
    higher_position_rate: float = proto.Field(
        proto.DOUBLE,
        number=10,
        optional=True,
    )


class CompetitiveVisibilityBenchmarkView(proto.Message):
    r"""Fields available for query in
    ``competitive_visibility_benchmark_view`` table.

    `Competitive
    visibility <https://support.google.com/merchants/answer/11366442>`__
    report with the category benchmark.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date of this row.

            Required in the ``SELECT`` clause. A condition on ``date``
            is required in the ``WHERE`` clause.
        report_country_code (str):
            Country where impressions appeared.

            Required in the ``SELECT`` clause. A condition on
            ``report_country_code`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_country_code``.
        report_category_id (int):
            Google product category ID to calculate the report for,
            represented in `Google's product
            taxonomy <https://support.google.com/merchants/answer/6324436>`__.

            Required in the ``SELECT`` clause. A condition on
            ``report_category_id`` is required in the ``WHERE`` clause.

            This field is a member of `oneof`_ ``_report_category_id``.
        traffic_source (google.shopping.merchant_reports_v1alpha.types.TrafficSource.TrafficSourceEnum):
            Traffic source of impressions.

            Required in the ``SELECT`` clause.

            This field is a member of `oneof`_ ``_traffic_source``.
        your_domain_visibility_trend (float):
            Change in visibility based on impressions for
            your domain with respect to the start of the
            selected time range (or first day with non-zero
            impressions).

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_your_domain_visibility_trend``.
        category_benchmark_visibility_trend (float):
            Change in visibility based on impressions
            with respect to the start of the selected time
            range (or first day with non-zero impressions)
            for a combined set of merchants with highest
            visibility approximating the market.

            Cannot be filtered on in the 'WHERE' clause.

            This field is a member of `oneof`_ ``_category_benchmark_visibility_trend``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    report_country_code: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    report_category_id: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    traffic_source: "TrafficSource.TrafficSourceEnum" = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum="TrafficSource.TrafficSourceEnum",
    )
    your_domain_visibility_trend: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )
    category_benchmark_visibility_trend: float = proto.Field(
        proto.DOUBLE,
        number=6,
        optional=True,
    )


class MarketingMethod(proto.Message):
    r"""Marketing method used to promote your products on Google
    (organic versus ads).

    """

    class MarketingMethodEnum(proto.Enum):
        r"""Marketing method values.

        Values:
            MARKETING_METHOD_ENUM_UNSPECIFIED (0):
                Not specified.
            ORGANIC (1):
                Organic marketing.
            ADS (2):
                Ads-based marketing.
        """

        MARKETING_METHOD_ENUM_UNSPECIFIED = 0
        ORGANIC = 1
        ADS = 2


class ReportGranularity(proto.Message):
    r"""Granularity of the Best sellers report. Best sellers reports
    are computed over a week and a month timeframe.

    """

    class ReportGranularityEnum(proto.Enum):
        r"""Report granularity values.

        Values:
            REPORT_GRANULARITY_ENUM_UNSPECIFIED (0):
                Not specified.
            WEEKLY (1):
                Report is computed over a week timeframe.
            MONTHLY (2):
                Report is computed over a month timeframe.
        """

        REPORT_GRANULARITY_ENUM_UNSPECIFIED = 0
        WEEKLY = 1
        MONTHLY = 2


class RelativeDemand(proto.Message):
    r"""Relative demand of a product cluster or brand in the Best
    sellers report.

    """

    class RelativeDemandEnum(proto.Enum):
        r"""Relative demand values.

        Values:
            RELATIVE_DEMAND_ENUM_UNSPECIFIED (0):
                Not specified.
            VERY_LOW (10):
                Demand is 0-5% of the demand of the highest
                ranked product cluster or brand.
            LOW (20):
                Demand is 6-10% of the demand of the highest
                ranked product cluster or brand.
            MEDIUM (30):
                Demand is 11-20% of the demand of the highest
                ranked product cluster or brand.
            HIGH (40):
                Demand is 21-50% of the demand of the highest
                ranked product cluster or brand.
            VERY_HIGH (50):
                Demand is 51-100% of the demand of the
                highest ranked product cluster or brand.
        """

        RELATIVE_DEMAND_ENUM_UNSPECIFIED = 0
        VERY_LOW = 10
        LOW = 20
        MEDIUM = 30
        HIGH = 40
        VERY_HIGH = 50


class RelativeDemandChangeType(proto.Message):
    r"""Relative demand of a product cluster or brand in the Best
    sellers report compared to the previous time period.

    """

    class RelativeDemandChangeTypeEnum(proto.Enum):
        r"""Relative demand change type values.

        Values:
            RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED (0):
                Not specified.
            SINKER (1):
                Relative demand is lower than the previous
                time period.
            FLAT (2):
                Relative demand is equal to the previous time
                period.
            RISER (3):
                Relative demand is higher than the previous
                time period.
        """

        RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED = 0
        SINKER = 1
        FLAT = 2
        RISER = 3


class TrafficSource(proto.Message):
    r"""Traffic source of impressions in the Competitive visibility
    report.

    """

    class TrafficSourceEnum(proto.Enum):
        r"""Traffic source values.

        Values:
            TRAFFIC_SOURCE_ENUM_UNSPECIFIED (0):
                Not specified.
            ORGANIC (1):
                Organic traffic.
            ADS (2):
                Traffic from ads.
            ALL (3):
                Organic and ads traffic.
        """

        TRAFFIC_SOURCE_ENUM_UNSPECIFIED = 0
        ORGANIC = 1
        ADS = 2
        ALL = 3


class YoutubeCreatorPerformanceView(proto.Message):
    r"""Fields available for query in ``youtube_creator_performance_view``
    table.

    `YouTube creator performance
    data <https://support.google.com/merchants/answer/14947975>`__ for
    your account. This data is only available if an account is enrolled
    in the `YouTube Shopping Affiliate
    program <https://support.google.com/merchants/answer/14815513?hl=en>`__.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date in the merchant timezone to which metrics apply.
            Segment.

            Condition on ``date`` is required in the ``WHERE`` clause.
        title (str):
            The title of the creator channel.

            This field is a member of `oneof`_ ``_title``.
        channel_id (str):
            The id for the creator channel.

            This field is a member of `oneof`_ ``_channel_id``.
        gross_sales (google.shopping.type.types.Price):
            The gross sales amount, before refunds.

            This field is a member of `oneof`_ ``_gross_sales``.
        commissions (google.shopping.type.types.Price):
            The commissions amount (pending and paid).

            This field is a member of `oneof`_ ``_commissions``.
        orders (int):
            The number of orders.

            This field is a member of `oneof`_ ``_orders``.
        views (int):
            The number of YouTube views.

            This field is a member of `oneof`_ ``_views``.
        clicks (int):
            The number of product clicks.

            This field is a member of `oneof`_ ``_clicks``.
        net_sales (google.shopping.type.types.Price):
            The net sales amount (includes both purchase
            and refunds).

            This field is a member of `oneof`_ ``_net_sales``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    channel_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    gross_sales: types.Price = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=types.Price,
    )
    commissions: types.Price = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=types.Price,
    )
    orders: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    views: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    clicks: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    net_sales: types.Price = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=types.Price,
    )


class YoutubeContentPerformanceView(proto.Message):
    r"""Fields available for query in ``youtube_content_performance_view``
    table.

    `YouTube content performance
    data <https://support.google.com/merchants/answer/14947975>`__ for
    your account. This data is only available if an account is enrolled
    in the `YouTube Shopping Affiliate
    program <https://support.google.com/merchants/answer/14815513?hl=en>`__.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date in the merchant timezone to which metrics apply.
            Segment.

            Condition on ``date`` is required in the ``WHERE`` clause.
        title (str):
            The video title.

            This field is a member of `oneof`_ ``_title``.
        video_id (str):
            The video id.

            This field is a member of `oneof`_ ``_video_id``.
        channel_title (str):
            The channel title.

            This field is a member of `oneof`_ ``_channel_title``.
        channel_id (str):
            The channel id.

            This field is a member of `oneof`_ ``_channel_id``.
        gross_sales (google.shopping.type.types.Price):
            The gross sales amount, before refunds.

            This field is a member of `oneof`_ ``_gross_sales``.
        commissions (google.shopping.type.types.Price):
            The commissions amount (pending and paid).

            This field is a member of `oneof`_ ``_commissions``.
        orders (int):
            The number of orders.

            This field is a member of `oneof`_ ``_orders``.
        views (int):
            The number of YouTube views.

            This field is a member of `oneof`_ ``_views``.
        clicks (int):
            The number of product clicks.

            This field is a member of `oneof`_ ``_clicks``.
        net_sales (google.shopping.type.types.Price):
            The net sales amount (includes both purchase
            and refunds).

            This field is a member of `oneof`_ ``_net_sales``.
        tagged_product_ids (MutableSequence[str]):
            Set of unique `product
            IDs <https://support.google.com/merchants/answer/188494#id>`__
            tagged on the YouTube video. These IDs correspond to the
            'offerId' in the Products API.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    video_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    channel_title: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    channel_id: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    gross_sales: types.Price = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=types.Price,
    )
    commissions: types.Price = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=types.Price,
    )
    orders: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    views: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    clicks: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    net_sales: types.Price = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message=types.Price,
    )
    tagged_product_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )


class YoutubeProductPerformanceView(proto.Message):
    r"""Fields available for query in ``youtube_product_performance_view``
    table.

    `YouTube product performance
    data <https://support.google.com/merchants/answer/14947975>`__ for
    your account. This data is only available if an account is enrolled
    in the `YouTube Shopping Affiliate
    program <https://support.google.com/merchants/answer/14815513?hl=en>`__.

    Values are only set for fields requested explicitly in the request's
    search query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Date in the merchant timezone to which metrics apply.
            Segment.

            Condition on ``date`` is required in the ``WHERE`` clause.
        title (str):
            The product title.

            This field is a member of `oneof`_ ``_title``.
        offer_id (str):
            The merchant-provided product id.

            This field is a member of `oneof`_ ``_offer_id``.
        distinct_video_count (int):
            The number of distinct videos the product was
            shown on.

            This field is a member of `oneof`_ ``_distinct_video_count``.
        distinct_creator_count (int):
            The number of distinct creator channels the
            product was shown on.

            This field is a member of `oneof`_ ``_distinct_creator_count``.
        gross_sales (google.shopping.type.types.Price):
            The gross sales amount, before refunds.

            This field is a member of `oneof`_ ``_gross_sales``.
        commissions (google.shopping.type.types.Price):
            The commissions amount (pending and paid).

            This field is a member of `oneof`_ ``_commissions``.
        orders (int):
            The number of orders.

            This field is a member of `oneof`_ ``_orders``.
        views (int):
            The number of YouTube views.

            This field is a member of `oneof`_ ``_views``.
        clicks (int):
            The number of product clicks.

            This field is a member of `oneof`_ ``_clicks``.
        net_sales (google.shopping.type.types.Price):
            The net sales amount (includes both purchase
            and refunds).

            This field is a member of `oneof`_ ``_net_sales``.
        tagged_creator_count (int):
            The number of distinct creators that tagged
            the product.

            This field is a member of `oneof`_ ``_tagged_creator_count``.
        tagged_video_count (int):
            The number of distinct videos that tagged the
            product.

            This field is a member of `oneof`_ ``_tagged_video_count``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    distinct_video_count: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    distinct_creator_count: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    gross_sales: types.Price = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=types.Price,
    )
    commissions: types.Price = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=types.Price,
    )
    orders: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    views: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    clicks: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    net_sales: types.Price = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message=types.Price,
    )
    tagged_creator_count: int = proto.Field(
        proto.INT64,
        number=12,
        optional=True,
    )
    tagged_video_count: int = proto.Field(
        proto.INT64,
        number=13,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
