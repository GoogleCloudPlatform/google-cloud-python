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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2alpha.types import common
from google.cloud.retail_v2alpha.types import product as gcr_product

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "UserEvent",
        "ProductDetail",
        "CompletionDetail",
        "PurchaseTransaction",
    },
)


class UserEvent(proto.Message):
    r"""UserEvent captures all metadata information Retail API needs
    to know about how end users interact with customers' website.

    Attributes:
        event_type (str):
            Required. User event type. Allowed values are:

            - ``add-to-cart``: Products being added to cart.
            - ``remove-from-cart``: Products being removed from cart.
            - ``category-page-view``: Special pages such as sale or
              promotion pages viewed.
            - ``detail-page-view``: Products detail page viewed.
            - ``home-page-view``: Homepage viewed.
            - ``purchase-complete``: User finishing a purchase.
            - ``search``: Product search.
            - ``shopping-cart-page-view``: User viewing a shopping cart.
        visitor_id (str):
            Required. A unique identifier for tracking visitors.

            For example, this could be implemented with an HTTP cookie,
            which should be able to uniquely identify a visitor on a
            single device. This unique identifier should not change if
            the visitor log in/out of the website.

            Don't set the field to the same fixed ID for different
            users. This mixes the event history of those users together,
            which results in degraded model quality.

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            The field should not contain PII or user-data. We recommend
            to use Google Analytics `Client
            ID <https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference#clientId>`__
            for this field.
        session_id (str):
            A unique identifier for tracking a visitor session with a
            length limit of 128 bytes. A session is an aggregation of an
            end user behavior in a time span.

            A general guideline to populate the sesion_id:

            1. If user has no activity for 30 min, a new session_id
               should be assigned.
            2. The session_id should be unique across users, suggest use
               uuid or add visitor_id as prefix.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Only required for
            [UserEventService.ImportUserEvents][google.cloud.retail.v2alpha.UserEventService.ImportUserEvents]
            method. Timestamp of when the user event happened.
        experiment_ids (MutableSequence[str]):
            A list of identifiers for the independent
            experiment groups this user event belongs to.
            This is used to distinguish between user events
            associated with different experiment setups
            (e.g. using Retail API, using different
            recommendation models).
        attribution_token (str):
            Highly recommended for user events that are the result of
            [PredictionService.Predict][google.cloud.retail.v2alpha.PredictionService.Predict].
            This field enables accurate attribution of recommendation
            model performance.

            The value must be a valid
            [PredictResponse.attribution_token][google.cloud.retail.v2alpha.PredictResponse.attribution_token]
            for user events that are the result of
            [PredictionService.Predict][google.cloud.retail.v2alpha.PredictionService.Predict].
            The value must be a valid
            [SearchResponse.attribution_token][google.cloud.retail.v2alpha.SearchResponse.attribution_token]
            for user events that are the result of
            [SearchService.Search][google.cloud.retail.v2alpha.SearchService.Search].

            This token enables us to accurately attribute page view or
            purchase back to the event and the particular predict
            response containing this clicked/purchased product. If user
            clicks on product K in the recommendation results, pass
            [PredictResponse.attribution_token][google.cloud.retail.v2alpha.PredictResponse.attribution_token]
            as a URL parameter to product K's page. When recording
            events on product K's page, log the
            [PredictResponse.attribution_token][google.cloud.retail.v2alpha.PredictResponse.attribution_token]
            to this field.
        product_details (MutableSequence[google.cloud.retail_v2alpha.types.ProductDetail]):
            The main product details related to the event.

            This field is optional except for the following event types:

            - ``add-to-cart``
            - ``detail-page-view``
            - ``purchase-complete``

            In a ``search`` event, this field represents the products
            returned to the end user on the current page (the end user
            may have not finished browsing the whole page yet). When a
            new page is returned to the end user, after
            pagination/filtering/ordering even for the same query, a new
            ``search`` event with different
            [product_details][google.cloud.retail.v2alpha.UserEvent.product_details]
            is desired. The end user may have not finished browsing the
            whole page yet.
        completion_detail (google.cloud.retail_v2alpha.types.CompletionDetail):
            The main auto-completion details related to the event.

            This field should be set for ``search`` event when
            autocomplete function is enabled and the user clicks a
            suggestion for search.
        attributes (MutableMapping[str, google.cloud.retail_v2alpha.types.CustomAttribute]):
            Extra user event features to include in the recommendation
            model.

            If you provide custom attributes for ingested user events,
            also include them in the user events that you associate with
            prediction requests. Custom attribute formatting must be
            consistent between imported events and events provided with
            prediction requests. This lets the Retail API use those
            custom attributes when training models and serving
            predictions, which helps improve recommendation quality.

            This field needs to pass all below criteria, otherwise an
            INVALID_ARGUMENT error is returned:

            - The key must be a UTF-8 encoded string with a length limit
              of 5,000 characters.
            - For text attributes, at most 400 values are allowed. Empty
              values are not allowed. Each value must be a UTF-8 encoded
              string with a length limit of 256 characters.
            - For number attributes, at most 400 values are allowed.

            For product recommendations, an example of extra user
            information is traffic_channel, which is how a user arrives
            at the site. Users can arrive at the site by coming to the
            site directly, coming through Google search, or in other
            ways.
        cart_id (str):
            The ID or name of the associated shopping cart. This ID is
            used to associate multiple items added or present in the
            cart before purchase.

            This can only be set for ``add-to-cart``,
            ``purchase-complete``, or ``shopping-cart-page-view``
            events.
        purchase_transaction (google.cloud.retail_v2alpha.types.PurchaseTransaction):
            A transaction represents the entire purchase transaction.

            Required for ``purchase-complete`` events. Other event types
            should not set this field. Otherwise, an INVALID_ARGUMENT
            error is returned.
        search_query (str):
            The user's search query.

            See
            [SearchRequest.query][google.cloud.retail.v2alpha.SearchRequest.query]
            for definition.

            The value must be a UTF-8 encoded string with a length limit
            of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            At least one of
            [search_query][google.cloud.retail.v2alpha.UserEvent.search_query]
            or
            [page_categories][google.cloud.retail.v2alpha.UserEvent.page_categories]
            is required for ``search`` events. Other event types should
            not set this field. Otherwise, an INVALID_ARGUMENT error is
            returned.
        filter (str):
            The filter syntax consists of an expression language for
            constructing a predicate from one or more fields of the
            products being filtered.

            See
            [SearchRequest.filter][google.cloud.retail.v2alpha.SearchRequest.filter]
            for definition and syntax.

            The value must be a UTF-8 encoded string with a length limit
            of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        order_by (str):
            The order in which products are returned.

            See
            [SearchRequest.order_by][google.cloud.retail.v2alpha.SearchRequest.order_by]
            for definition and syntax.

            The value must be a UTF-8 encoded string with a length limit
            of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            This can only be set for ``search`` events. Other event
            types should not set this field. Otherwise, an
            INVALID_ARGUMENT error is returned.
        offset (int):
            An integer that specifies the current offset for pagination
            (the 0-indexed starting location, amongst the products
            deemed by the API as relevant).

            See
            [SearchRequest.offset][google.cloud.retail.v2alpha.SearchRequest.offset]
            for definition.

            If this field is negative, an INVALID_ARGUMENT is returned.

            This can only be set for ``search`` events. Other event
            types should not set this field. Otherwise, an
            INVALID_ARGUMENT error is returned.
        page_categories (MutableSequence[str]):
            The categories associated with a category page.

            To represent full path of category, use '>' sign to separate
            different hierarchies. If '>' is part of the category name,
            replace it with other character(s).

            Category pages include special pages such as sales or
            promotions. For instance, a special sale page may have the
            category hierarchy: "pageCategories" : ["Sales > 2017 Black
            Friday Deals"].

            Required for ``category-page-view`` events. At least one of
            [search_query][google.cloud.retail.v2alpha.UserEvent.search_query]
            or
            [page_categories][google.cloud.retail.v2alpha.UserEvent.page_categories]
            is required for ``search`` events. Other event types should
            not set this field. Otherwise, an INVALID_ARGUMENT error is
            returned.
        user_info (google.cloud.retail_v2alpha.types.UserInfo):
            User information.
        uri (str):
            Complete URL (window.location.href) of the
            user's current page.
            When using the client side event reporting with
            JavaScript pixel and Google Tag Manager, this
            value is filled in automatically. Maximum length
            5,000 characters.
        referrer_uri (str):
            The referrer URL of the current page.

            When using the client side event reporting with
            JavaScript pixel and Google Tag Manager, this
            value is filled in automatically.
        page_view_id (str):
            A unique ID of a web page view.

            This should be kept the same for all user events triggered
            from the same pageview. For example, an item detail page
            view could trigger multiple events as the user is browsing
            the page. The ``pageViewId`` property should be kept the
            same for all these events so that they can be grouped
            together properly.

            When using the client side event reporting with JavaScript
            pixel and Google Tag Manager, this value is filled in
            automatically.
        entity (str):
            The entity for customers that may run multiple different
            entities, domains, sites or regions, for example,
            ``Google US``, ``Google Ads``, ``Waymo``, ``google.com``,
            ``youtube.com``, etc. We recommend that you set this field
            to get better per-entity search, completion, and prediction
            results.
    """

    event_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    visitor_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=21,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    experiment_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    attribution_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    product_details: MutableSequence["ProductDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ProductDetail",
    )
    completion_detail: "CompletionDetail" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="CompletionDetail",
    )
    attributes: MutableMapping[str, common.CustomAttribute] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=common.CustomAttribute,
    )
    cart_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    purchase_transaction: "PurchaseTransaction" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="PurchaseTransaction",
    )
    search_query: str = proto.Field(
        proto.STRING,
        number=10,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=16,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=17,
    )
    offset: int = proto.Field(
        proto.INT32,
        number=18,
    )
    page_categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    user_info: common.UserInfo = proto.Field(
        proto.MESSAGE,
        number=12,
        message=common.UserInfo,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=13,
    )
    referrer_uri: str = proto.Field(
        proto.STRING,
        number=14,
    )
    page_view_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    entity: str = proto.Field(
        proto.STRING,
        number=23,
    )


class ProductDetail(proto.Message):
    r"""Detailed product information associated with a user event.

    Attributes:
        product (google.cloud.retail_v2alpha.types.Product):
            Required. [Product][google.cloud.retail.v2alpha.Product]
            information.

            Required field(s):

            - [Product.id][google.cloud.retail.v2alpha.Product.id]

            Optional override field(s):

            - [Product.price_info][google.cloud.retail.v2alpha.Product.price_info]

            If any supported optional fields are provided, we will treat
            them as a full override when looking up product information
            from the catalog. Thus, it is important to ensure that the
            overriding fields are accurate and complete.

            All other product fields are ignored and instead populated
            via catalog lookup after event ingestion.
        quantity (google.protobuf.wrappers_pb2.Int32Value):
            Quantity of the product associated with the user event.

            For example, this field will be 2 if two products are added
            to the shopping cart for ``purchase-complete`` event.
            Required for ``add-to-cart`` and ``purchase-complete`` event
            types.
    """

    product: gcr_product.Product = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_product.Product,
    )
    quantity: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )


class CompletionDetail(proto.Message):
    r"""Detailed completion information including completion
    attribution token and clicked completion info.

    Attributes:
        completion_attribution_token (str):
            Completion attribution token in
            [CompleteQueryResponse.attribution_token][google.cloud.retail.v2alpha.CompleteQueryResponse.attribution_token].
        selected_suggestion (str):
            End user selected
            [CompleteQueryResponse.CompletionResult.suggestion][google.cloud.retail.v2alpha.CompleteQueryResponse.CompletionResult.suggestion].
        selected_position (int):
            End user selected
            [CompleteQueryResponse.CompletionResult.suggestion][google.cloud.retail.v2alpha.CompleteQueryResponse.CompletionResult.suggestion]
            position, starting from 0.
    """

    completion_attribution_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    selected_suggestion: str = proto.Field(
        proto.STRING,
        number=2,
    )
    selected_position: int = proto.Field(
        proto.INT32,
        number=3,
    )


class PurchaseTransaction(proto.Message):
    r"""A transaction represents the entire purchase transaction.

    Attributes:
        id (str):
            The transaction ID with a length limit of 128
            characters.
        revenue (float):
            Required. Total non-zero revenue or grand
            total associated with the transaction. This
            value include shipping, tax, or other
            adjustments to total revenue that you want to
            include as part of your revenue calculations.
        tax (float):
            All the taxes associated with the
            transaction.
        cost (float):
            All the costs associated with the products. These can be
            manufacturing costs, shipping expenses not borne by the end
            user, or any other costs, such that:

            - Profit =
              [revenue][google.cloud.retail.v2alpha.PurchaseTransaction.revenue]
              -
              [tax][google.cloud.retail.v2alpha.PurchaseTransaction.tax]
              -
              [cost][google.cloud.retail.v2alpha.PurchaseTransaction.cost]
        currency_code (str):
            Required. Currency code. Use three-character
            ISO-4217 code.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revenue: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    tax: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    cost: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
