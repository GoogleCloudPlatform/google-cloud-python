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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2beta.types import common
from google.cloud.retail_v2beta.types import product as gcr_product

__protobuf__ = proto.module(
    package="google.cloud.retail.v2beta",
    manifest={
        "ProductAttributeValue",
        "ProductAttributeInterval",
        "Tile",
        "SearchRequest",
        "SearchResponse",
        "ExperimentInfo",
    },
)


class ProductAttributeValue(proto.Message):
    r"""Product attribute which structured by an attribute name and value.
    This structure is used in conversational search filters and answers.
    For example, if we have ``name=color`` and ``value=red``, this means
    that the color is ``red``.

    Attributes:
        name (str):
            The attribute name.
        value (str):
            The attribute value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProductAttributeInterval(proto.Message):
    r"""Product attribute name and numeric interval.

    Attributes:
        name (str):
            The attribute name (e.g. "length")
        interval (google.cloud.retail_v2beta.types.Interval):
            The numeric interval (e.g. [10, 20))
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    interval: common.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Interval,
    )


class Tile(proto.Message):
    r"""This field specifies the tile information including an
    attribute key, attribute value. More fields will be added in the
    future, eg: product id or product counts, etc.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        product_attribute_value (google.cloud.retail_v2beta.types.ProductAttributeValue):
            The product attribute key-value.

            This field is a member of `oneof`_ ``product_attribute``.
        product_attribute_interval (google.cloud.retail_v2beta.types.ProductAttributeInterval):
            The product attribute key-numeric interval.

            This field is a member of `oneof`_ ``product_attribute``.
        representative_product_id (str):
            The representative product id for this tile.
    """

    product_attribute_value: "ProductAttributeValue" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="product_attribute",
        message="ProductAttributeValue",
    )
    product_attribute_interval: "ProductAttributeInterval" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="product_attribute",
        message="ProductAttributeInterval",
    )
    representative_product_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SearchRequest(proto.Message):
    r"""Request message for
    [SearchService.Search][google.cloud.retail.v2beta.SearchService.Search]
    method.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        placement (str):
            Required. The resource name of the Retail Search serving
            config, such as
            ``projects/*/locations/global/catalogs/default_catalog/servingConfigs/default_serving_config``
            or the name of the legacy placement resource, such as
            ``projects/*/locations/global/catalogs/default_catalog/placements/default_search``.
            This field is used to identify the serving config name and
            the set of models that are used to make the search.
        branch (str):
            The branch resource name, such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/0``.

            Use "default_branch" as the branch ID or leave this field
            empty, to search products under the default branch.
        query (str):
            Raw search query.

            If this field is empty, the request is considered a category
            browsing request and returned results are based on
            [filter][google.cloud.retail.v2beta.SearchRequest.filter]
            and
            [page_categories][google.cloud.retail.v2beta.SearchRequest.page_categories].
        visitor_id (str):
            Required. A unique identifier for tracking visitors. For
            example, this could be implemented with an HTTP cookie,
            which should be able to uniquely identify a visitor on a
            single device. This unique identifier should not change if
            the visitor logs in or out of the website.

            This should be the same identifier as
            [UserEvent.visitor_id][google.cloud.retail.v2beta.UserEvent.visitor_id].

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        user_info (google.cloud.retail_v2beta.types.UserInfo):
            User information.
        page_size (int):
            Maximum number of
            [Product][google.cloud.retail.v2beta.Product]s to return. If
            unspecified, defaults to a reasonable value. The maximum
            allowed value is 120. Values above 120 will be coerced to
            120.

            If this field is negative, an INVALID_ARGUMENT is returned.
        page_token (str):
            A page token
            [SearchResponse.next_page_token][google.cloud.retail.v2beta.SearchResponse.next_page_token],
            received from a previous
            [SearchService.Search][google.cloud.retail.v2beta.SearchService.Search]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [SearchService.Search][google.cloud.retail.v2beta.SearchService.Search]
            must match the call that provided the page token. Otherwise,
            an INVALID_ARGUMENT error is returned.
        offset (int):
            A 0-indexed integer that specifies the current offset (that
            is, starting result location, amongst the
            [Product][google.cloud.retail.v2beta.Product]s deemed by the
            API as relevant) in search results. This field is only
            considered if
            [page_token][google.cloud.retail.v2beta.SearchRequest.page_token]
            is unset.

            If this field is negative, an INVALID_ARGUMENT is returned.
        filter (str):
            The filter syntax consists of an expression language for
            constructing a predicate from one or more fields of the
            products being filtered. Filter expression is
            case-sensitive. For more information, see
            `Filter <https://cloud.google.com/retail/docs/filter-and-order#filter>`__.

            If this field is unrecognizable, an INVALID_ARGUMENT is
            returned.
        canonical_filter (str):
            The default filter that is applied when a user performs a
            search without checking any filters on the search page.

            The filter applied to every search request when quality
            improvement such as query expansion is needed. In the case a
            query does not have a sufficient amount of results this
            filter will be used to determine whether or not to enable
            the query expansion flow. The original filter will still be
            used for the query expanded search. This field is strongly
            recommended to achieve high search quality.

            For more information about filter syntax, see
            [SearchRequest.filter][google.cloud.retail.v2beta.SearchRequest.filter].
        order_by (str):
            The order in which products are returned. Products can be
            ordered by a field in an
            [Product][google.cloud.retail.v2beta.Product] object. Leave
            it unset if ordered by relevance. OrderBy expression is
            case-sensitive. For more information, see
            `Order <https://cloud.google.com/retail/docs/filter-and-order#order>`__.

            If this field is unrecognizable, an INVALID_ARGUMENT is
            returned.
        facet_specs (MutableSequence[google.cloud.retail_v2beta.types.SearchRequest.FacetSpec]):
            Facet specifications for faceted search. If empty, no facets
            are returned.

            A maximum of 200 values are allowed. Otherwise, an
            INVALID_ARGUMENT error is returned.
        dynamic_facet_spec (google.cloud.retail_v2beta.types.SearchRequest.DynamicFacetSpec):
            Deprecated. Refer to
            https://cloud.google.com/retail/docs/configs#dynamic
            to enable dynamic facets. Do not set this field.

            The specification for dynamically generated
            facets. Notice that only textual facets can be
            dynamically generated.
        boost_spec (google.cloud.retail_v2beta.types.SearchRequest.BoostSpec):
            Boost specification to boost certain products. For more
            information, see `Boost
            results <https://cloud.google.com/retail/docs/boosting>`__.

            Notice that if both
            [ServingConfig.boost_control_ids][google.cloud.retail.v2beta.ServingConfig.boost_control_ids]
            and
            [SearchRequest.boost_spec][google.cloud.retail.v2beta.SearchRequest.boost_spec]
            are set, the boost conditions from both places are
            evaluated. If a search request matches multiple boost
            conditions, the final boost score is equal to the sum of the
            boost scores from all matched boost conditions.
        query_expansion_spec (google.cloud.retail_v2beta.types.SearchRequest.QueryExpansionSpec):
            The query expansion specification that specifies the
            conditions under which query expansion occurs. For more
            information, see `Query
            expansion <https://cloud.google.com/retail/docs/result-size#query_expansion>`__.
        variant_rollup_keys (MutableSequence[str]):
            The keys to fetch and rollup the matching
            [variant][google.cloud.retail.v2beta.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2beta.Product]s attributes,
            [FulfillmentInfo][google.cloud.retail.v2beta.FulfillmentInfo]
            or
            [LocalInventory][google.cloud.retail.v2beta.LocalInventory]s
            attributes. The attributes from all the matching
            [variant][google.cloud.retail.v2beta.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2beta.Product]s or
            [LocalInventory][google.cloud.retail.v2beta.LocalInventory]s
            are merged and de-duplicated. Notice that rollup attributes
            will lead to extra query latency. Maximum number of keys is
            30.

            For
            [FulfillmentInfo][google.cloud.retail.v2beta.FulfillmentInfo],
            a fulfillment type and a fulfillment ID must be provided in
            the format of "fulfillmentType.fulfillmentId". E.g., in
            "pickupInStore.store123", "pickupInStore" is fulfillment
            type and "store123" is the store ID.

            Supported keys are:

            - colorFamilies
            - price
            - originalPrice
            - discount
            - variantId
            - inventory(place_id,price)
            - inventory(place_id,original_price)
            - inventory(place_id,attributes.key), where key is any key
              in the
              [Product.local_inventories.attributes][google.cloud.retail.v2beta.LocalInventory.attributes]
              map.
            - attributes.key, where key is any key in the
              [Product.attributes][google.cloud.retail.v2beta.Product.attributes]
              map.
            - pickupInStore.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "pickup-in-store".
            - shipToStore.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "ship-to-store".
            - sameDayDelivery.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "same-day-delivery".
            - nextDayDelivery.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "next-day-delivery".
            - customFulfillment1.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "custom-type-1".
            - customFulfillment2.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "custom-type-2".
            - customFulfillment3.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "custom-type-3".
            - customFulfillment4.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "custom-type-4".
            - customFulfillment5.id, where id is any
              [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
              for
              [FulfillmentInfo.type][google.cloud.retail.v2beta.FulfillmentInfo.type]
              "custom-type-5".

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.
        page_categories (MutableSequence[str]):
            The categories associated with a category page. Must be set
            for category navigation queries to achieve good search
            quality. The format should be the same as
            [UserEvent.page_categories][google.cloud.retail.v2beta.UserEvent.page_categories];

            To represent full path of category, use '>' sign to separate
            different hierarchies. If '>' is part of the category name,
            replace it with other character(s).

            Category pages include special pages such as sales or
            promotions. For instance, a special sale page may have the
            category hierarchy: "pageCategories" : ["Sales > 2017 Black
            Friday Deals"].
        search_mode (google.cloud.retail_v2beta.types.SearchRequest.SearchMode):
            The search mode of the search request. If not
            specified, a single search request triggers both
            product search and faceted search.
        personalization_spec (google.cloud.retail_v2beta.types.SearchRequest.PersonalizationSpec):
            The specification for personalization.

            Notice that if both
            [ServingConfig.personalization_spec][google.cloud.retail.v2beta.ServingConfig.personalization_spec]
            and
            [SearchRequest.personalization_spec][google.cloud.retail.v2beta.SearchRequest.personalization_spec]
            are set.
            [SearchRequest.personalization_spec][google.cloud.retail.v2beta.SearchRequest.personalization_spec]
            will override
            [ServingConfig.personalization_spec][google.cloud.retail.v2beta.ServingConfig.personalization_spec].
        labels (MutableMapping[str, str]):
            The labels applied to a resource must meet the following
            requirements:

            - Each resource can have multiple labels, up to a maximum of
              64.
            - Each label must be a key-value pair.
            - Keys have a minimum length of 1 character and a maximum
              length of 63 characters and cannot be empty. Values can be
              empty and have a maximum length of 63 characters.
            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes. All
              characters must use UTF-8 encoding, and international
              characters are allowed.
            - The key portion of a label must be unique. However, you
              can use the same key with multiple resources.
            - Keys must start with a lowercase letter or international
              character.

            For more information, see `Requirements for
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`__
            in the Resource Manager documentation.
        spell_correction_spec (google.cloud.retail_v2beta.types.SearchRequest.SpellCorrectionSpec):
            The spell correction specification that
            specifies the mode under which spell correction
            will take effect.

            This field is a member of `oneof`_ ``_spell_correction_spec``.
        entity (str):
            The entity for customers that may run multiple different
            entities, domains, sites or regions, for example,
            ``Google US``, ``Google Ads``, ``Waymo``, ``google.com``,
            ``youtube.com``, etc. If this is set, it should be exactly
            matched with
            [UserEvent.entity][google.cloud.retail.v2beta.UserEvent.entity]
            to get search results boosted by entity.
        conversational_search_spec (google.cloud.retail_v2beta.types.SearchRequest.ConversationalSearchSpec):
            Optional. This field specifies all
            conversational related parameters addition to
            traditional retail search.
        tile_navigation_spec (google.cloud.retail_v2beta.types.SearchRequest.TileNavigationSpec):
            Optional. This field specifies tile
            navigation related parameters.
        language_code (str):
            Optional. The BCP-47 language code, such as "en-US" or
            "sr-Latn"
            `list <https://www.unicode.org/cldr/charts/46/summary/root.html>`__.
            For more information, see `Standardized
            codes <https://google.aip.dev/143>`__. This field helps to
            better interpret the query. If a value isn't specified, the
            query language code is automatically detected, which may not
            be accurate.
        region_code (str):
            Optional. The Unicode country/region code (CLDR) of a
            location, such as "US" and "419"
            `list <https://www.unicode.org/cldr/charts/46/supplemental/territory_information.html>`__.
            For more information, see `Standardized
            codes <https://google.aip.dev/143>`__. If set, then results
            will be boosted based on the region_code provided.
        place_id (str):
            Optional. An id corresponding to a place, such as a store id
            or region id. When specified, we use the price from the
            local inventory with the matching product's
            [LocalInventory.place_id][google.cloud.retail.v2beta.LocalInventory.place_id]
            for revenue optimization.
        user_attributes (MutableMapping[str, google.cloud.retail_v2beta.types.StringList]):
            Optional. The user attributes that could be used for
            personalization of search results.

            - Populate at most 100 key-value pairs per query.
            - Only supports string keys and repeated string values.
            - Duplicate keys are not allowed within a single query.

            Example: user_attributes: [ { key: "pets" value { values:
            "dog" values: "cat" } }, { key: "state" value { values: "CA"
            } } ]
    """

    class SearchMode(proto.Enum):
        r"""The search mode of each search request.

        Values:
            SEARCH_MODE_UNSPECIFIED (0):
                Default value. In this case both product search and faceted
                search will be performed. Both
                [SearchResponse.SearchResult][google.cloud.retail.v2beta.SearchResponse.SearchResult]
                and
                [SearchResponse.Facet][google.cloud.retail.v2beta.SearchResponse.Facet]
                will be returned.
            PRODUCT_SEARCH_ONLY (1):
                Only product search will be performed. The faceted search
                will be disabled.

                Only
                [SearchResponse.SearchResult][google.cloud.retail.v2beta.SearchResponse.SearchResult]
                will be returned.
                [SearchResponse.Facet][google.cloud.retail.v2beta.SearchResponse.Facet]
                will not be returned, even if
                [SearchRequest.facet_specs][google.cloud.retail.v2beta.SearchRequest.facet_specs]
                or
                [SearchRequest.dynamic_facet_spec][google.cloud.retail.v2beta.SearchRequest.dynamic_facet_spec]
                is set.
            FACETED_SEARCH_ONLY (2):
                Only faceted search will be performed. The product search
                will be disabled.

                When in this mode, one or both of
                [SearchRequest.facet_specs][google.cloud.retail.v2beta.SearchRequest.facet_specs]
                and
                [SearchRequest.dynamic_facet_spec][google.cloud.retail.v2beta.SearchRequest.dynamic_facet_spec]
                should be set. Otherwise, an INVALID_ARGUMENT error is
                returned. Only
                [SearchResponse.Facet][google.cloud.retail.v2beta.SearchResponse.Facet]
                will be returned.
                [SearchResponse.SearchResult][google.cloud.retail.v2beta.SearchResponse.SearchResult]
                will not be returned.
        """

        SEARCH_MODE_UNSPECIFIED = 0
        PRODUCT_SEARCH_ONLY = 1
        FACETED_SEARCH_ONLY = 2

    class FacetSpec(proto.Message):
        r"""A facet specification to perform faceted search.

        Attributes:
            facet_key (google.cloud.retail_v2beta.types.SearchRequest.FacetSpec.FacetKey):
                Required. The facet key specification.
            limit (int):
                Maximum of facet values that should be returned for this
                facet. If unspecified, defaults to 50. The maximum allowed
                value is 300. Values above 300 will be coerced to 300.

                If this field is negative, an INVALID_ARGUMENT is returned.
            excluded_filter_keys (MutableSequence[str]):
                List of keys to exclude when faceting.

                By default,
                [FacetKey.key][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.key]
                is not excluded from the filter unless it is listed in this
                field.

                Listing a facet key in this field allows its values to
                appear as facet results, even when they are filtered out of
                search results. Using this field does not affect what search
                results are returned.

                For example, suppose there are 100 products with the color
                facet "Red" and 200 products with the color facet "Blue". A
                query containing the filter "colorFamilies:ANY("Red")" and
                having "colorFamilies" as
                [FacetKey.key][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.key]
                would by default return only "Red" products in the search
                results, and also return "Red" with count 100 as the only
                color facet. Although there are also blue products
                available, "Blue" would not be shown as an available facet
                value.

                If "colorFamilies" is listed in "excludedFilterKeys", then
                the query returns the facet values "Red" with count 100 and
                "Blue" with count 200, because the "colorFamilies" key is
                now excluded from the filter. Because this field doesn't
                affect search results, the search results are still
                correctly filtered to return only "Red" products.

                A maximum of 100 values are allowed. Otherwise, an
                INVALID_ARGUMENT error is returned.
            enable_dynamic_position (bool):
                Enables dynamic position for this facet. If set to true, the
                position of this facet among all facets in the response is
                determined by Google Retail Search. It is ordered together
                with dynamic facets if dynamic facets is enabled. If set to
                false, the position of this facet in the response is the
                same as in the request, and it is ranked before the facets
                with dynamic position enable and all dynamic facets.

                For example, you may always want to have rating facet
                returned in the response, but it's not necessarily to always
                display the rating facet at the top. In that case, you can
                set enable_dynamic_position to true so that the position of
                rating facet in response is determined by Google Retail
                Search.

                Another example, assuming you have the following facets in
                the request:

                - "rating", enable_dynamic_position = true

                - "price", enable_dynamic_position = false

                - "brands", enable_dynamic_position = false

                And also you have a dynamic facets enable, which generates a
                facet "gender". Then, the final order of the facets in the
                response can be ("price", "brands", "rating", "gender") or
                ("price", "brands", "gender", "rating") depends on how
                Google Retail Search orders "gender" and "rating" facets.
                However, notice that "price" and "brands" are always ranked
                at first and second position because their
                enable_dynamic_position values are false.
        """

        class FacetKey(proto.Message):
            r"""Specifies how a facet is computed.

            Attributes:
                key (str):
                    Required. Supported textual and numerical facet keys in
                    [Product][google.cloud.retail.v2beta.Product] object, over
                    which the facet values are computed. Facet key is
                    case-sensitive.

                    Allowed facet keys when
                    [FacetKey.query][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.query]
                    is not specified:

                    - textual_field =

                      - "brands"
                      - "categories"
                      - "genders"
                      - "ageGroups"
                      - "availability"
                      - "colorFamilies"
                      - "colors"
                      - "sizes"
                      - "materials"
                      - "patterns"
                      - "conditions"
                      - "attributes.key"
                      - "pickupInStore"
                      - "shipToStore"
                      - "sameDayDelivery"
                      - "nextDayDelivery"
                      - "customFulfillment1"
                      - "customFulfillment2"
                      - "customFulfillment3"
                      - "customFulfillment4"
                      - "customFulfillment5"
                      - "inventory(place_id,attributes.key)"

                    - numerical_field =

                      - "price"
                      - "discount"
                      - "rating"
                      - "ratingCount"
                      - "attributes.key"
                      - "inventory(place_id,price)"
                      - "inventory(place_id,original_price)"
                      - "inventory(place_id,attributes.key)".
                intervals (MutableSequence[google.cloud.retail_v2beta.types.Interval]):
                    Set only if values should be bucketized into
                    intervals. Must be set for facets with numerical
                    values. Must not be set for facet with text
                    values. Maximum number of intervals is 40.

                    For all numerical facet keys that appear in the
                    list of products from the catalog, the
                    percentiles 0, 10, 30, 50, 70, 90, and 100 are
                    computed from their distribution weekly. If the
                    model assigns a high score to a numerical facet
                    key and its intervals are not specified in the
                    search request, these percentiles become the
                    bounds for its intervals and are returned in the
                    response. If the facet key intervals are
                    specified in the request, then the specified
                    intervals are returned instead.
                restricted_values (MutableSequence[str]):
                    Only get facet for the given restricted values. For example,
                    when using "pickupInStore" as key and set restricted values
                    to ["store123", "store456"], only facets for "store123" and
                    "store456" are returned. Only supported on predefined
                    textual fields, custom textual attributes and fulfillments.
                    Maximum is 20.

                    Must be set for the fulfillment facet keys:

                    - pickupInStore

                    - shipToStore

                    - sameDayDelivery

                    - nextDayDelivery

                    - customFulfillment1

                    - customFulfillment2

                    - customFulfillment3

                    - customFulfillment4

                    - customFulfillment5
                prefixes (MutableSequence[str]):
                    Only get facet values that start with the
                    given string prefix. For example, suppose
                    "categories" has three values "Women > Shoe",
                    "Women > Dress" and "Men > Shoe". If set
                    "prefixes" to "Women", the "categories" facet
                    gives only "Women > Shoe" and "Women > Dress".
                    Only supported on textual fields. Maximum is 10.
                contains (MutableSequence[str]):
                    Only get facet values that contains the given
                    strings. For example, suppose "categories" has
                    three values "Women > Shoe", "Women > Dress" and
                    "Men > Shoe". If set "contains" to "Shoe", the
                    "categories" facet gives only "Women > Shoe" and
                    "Men > Shoe". Only supported on textual fields.
                    Maximum is 10.
                case_insensitive (bool):
                    True to make facet keys case insensitive when
                    getting faceting values with prefixes or
                    contains; false otherwise.
                order_by (str):
                    The order in which
                    [SearchResponse.Facet.values][google.cloud.retail.v2beta.SearchResponse.Facet.values]
                    are returned.

                    Allowed values are:

                    - "count desc", which means order by
                      [SearchResponse.Facet.values.count][google.cloud.retail.v2beta.SearchResponse.Facet.FacetValue.count]
                      descending.

                    - "value desc", which means order by
                      [SearchResponse.Facet.values.value][google.cloud.retail.v2beta.SearchResponse.Facet.FacetValue.value]
                      descending. Only applies to textual facets.

                    If not set, textual values are sorted in `natural
                    order <https://en.wikipedia.org/wiki/Natural_sort_order>`__;
                    numerical intervals are sorted in the order given by
                    [FacetSpec.FacetKey.intervals][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.intervals];
                    [FulfillmentInfo.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]
                    are sorted in the order given by
                    [FacetSpec.FacetKey.restricted_values][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.restricted_values].
                query (str):
                    The query that is used to compute facet for the given facet
                    key. When provided, it overrides the default behavior of
                    facet computation. The query syntax is the same as a filter
                    expression. See
                    [SearchRequest.filter][google.cloud.retail.v2beta.SearchRequest.filter]
                    for detail syntax and limitations. Notice that there is no
                    limitation on
                    [FacetKey.key][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.key]
                    when query is specified.

                    In the response,
                    [SearchResponse.Facet.values.value][google.cloud.retail.v2beta.SearchResponse.Facet.FacetValue.value]
                    is always "1" and
                    [SearchResponse.Facet.values.count][google.cloud.retail.v2beta.SearchResponse.Facet.FacetValue.count]
                    is the number of results that match the query.

                    For example, you can set a customized facet for
                    "shipToStore", where
                    [FacetKey.key][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.key]
                    is "customizedShipToStore", and
                    [FacetKey.query][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.query]
                    is "availability: ANY("IN_STOCK") AND shipToStore:
                    ANY("123")". Then the facet counts the products that are
                    both in stock and ship to store "123".
                return_min_max (bool):
                    Returns the min and max value for each
                    numerical facet intervals. Ignored for textual
                    facets.
            """

            key: str = proto.Field(
                proto.STRING,
                number=1,
            )
            intervals: MutableSequence[common.Interval] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message=common.Interval,
            )
            restricted_values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )
            prefixes: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=8,
            )
            contains: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=9,
            )
            case_insensitive: bool = proto.Field(
                proto.BOOL,
                number=10,
            )
            order_by: str = proto.Field(
                proto.STRING,
                number=4,
            )
            query: str = proto.Field(
                proto.STRING,
                number=5,
            )
            return_min_max: bool = proto.Field(
                proto.BOOL,
                number=11,
            )

        facet_key: "SearchRequest.FacetSpec.FacetKey" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="SearchRequest.FacetSpec.FacetKey",
        )
        limit: int = proto.Field(
            proto.INT32,
            number=2,
        )
        excluded_filter_keys: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        enable_dynamic_position: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    class DynamicFacetSpec(proto.Message):
        r"""The specifications of dynamically generated facets.

        Attributes:
            mode (google.cloud.retail_v2beta.types.SearchRequest.DynamicFacetSpec.Mode):
                Mode of the DynamicFacet feature. Defaults to
                [Mode.DISABLED][google.cloud.retail.v2beta.SearchRequest.DynamicFacetSpec.Mode.DISABLED]
                if it's unset.
        """

        class Mode(proto.Enum):
            r"""Enum to control DynamicFacet mode

            Values:
                MODE_UNSPECIFIED (0):
                    Default value.
                DISABLED (1):
                    Disable Dynamic Facet.
                ENABLED (2):
                    Automatic mode built by Google Retail Search.
            """

            MODE_UNSPECIFIED = 0
            DISABLED = 1
            ENABLED = 2

        mode: "SearchRequest.DynamicFacetSpec.Mode" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SearchRequest.DynamicFacetSpec.Mode",
        )

    class BoostSpec(proto.Message):
        r"""Boost specification to boost certain items.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            condition_boost_specs (MutableSequence[google.cloud.retail_v2beta.types.SearchRequest.BoostSpec.ConditionBoostSpec]):
                Condition boost specifications. If a product
                matches multiple conditions in the
                specifications, boost scores from these
                specifications are all applied and combined in a
                non-linear way. Maximum number of specifications
                is 20.
            skip_boost_spec_validation (bool):
                Whether to skip boostspec validation. If this field is set
                to true, invalid
                [BoostSpec.condition_boost_specs][google.cloud.retail.v2beta.SearchRequest.BoostSpec.condition_boost_specs]
                will be ignored and valid
                [BoostSpec.condition_boost_specs][google.cloud.retail.v2beta.SearchRequest.BoostSpec.condition_boost_specs]
                will still be applied.

                This field is a member of `oneof`_ ``_skip_boost_spec_validation``.
        """

        class ConditionBoostSpec(proto.Message):
            r"""Boost applies to products which match a condition.

            Attributes:
                condition (str):
                    An expression which specifies a boost condition. The syntax
                    and supported fields are the same as a filter expression.
                    See
                    [SearchRequest.filter][google.cloud.retail.v2beta.SearchRequest.filter]
                    for detail syntax and limitations.

                    Examples:

                    - To boost products with product ID "product_1" or
                      "product_2", and color "Red" or "Blue":

                      - (id: ANY("product_1", "product_2")) AND (colorFamilies:
                        ANY("Red","Blue"))
                boost (float):
                    Strength of the condition boost, which should be in [-1, 1].
                    Negative boost means demotion. Default is 0.0.

                    Setting to 1.0 gives the item a big promotion. However, it
                    does not necessarily mean that the boosted item will be the
                    top result at all times, nor that other items will be
                    excluded. Results could still be shown even when none of
                    them matches the condition. And results that are
                    significantly more relevant to the search query can still
                    trump your heavily favored but irrelevant items.

                    Setting to -1.0 gives the item a big demotion. However,
                    results that are deeply relevant might still be shown. The
                    item will have an upstream battle to get a fairly high
                    ranking, but it is not blocked out completely.

                    Setting to 0.0 means no boost applied. The boosting
                    condition is ignored.
            """

            condition: str = proto.Field(
                proto.STRING,
                number=1,
            )
            boost: float = proto.Field(
                proto.FLOAT,
                number=2,
            )

        condition_boost_specs: MutableSequence[
            "SearchRequest.BoostSpec.ConditionBoostSpec"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SearchRequest.BoostSpec.ConditionBoostSpec",
        )
        skip_boost_spec_validation: bool = proto.Field(
            proto.BOOL,
            number=2,
            optional=True,
        )

    class QueryExpansionSpec(proto.Message):
        r"""Specification to determine under which conditions query
        expansion should occur.

        Attributes:
            condition (google.cloud.retail_v2beta.types.SearchRequest.QueryExpansionSpec.Condition):
                The condition under which query expansion should occur.
                Default to
                [Condition.DISABLED][google.cloud.retail.v2beta.SearchRequest.QueryExpansionSpec.Condition.DISABLED].
            pin_unexpanded_results (bool):
                Whether to pin unexpanded results. The
                default value is false. If this field is set to
                true, unexpanded products are always at the top
                of the search results, followed by the expanded
                results.
        """

        class Condition(proto.Enum):
            r"""Enum describing under which condition query expansion should
            occur.

            Values:
                CONDITION_UNSPECIFIED (0):
                    Unspecified query expansion condition. In this case, server
                    behavior defaults to
                    [Condition.DISABLED][google.cloud.retail.v2beta.SearchRequest.QueryExpansionSpec.Condition.DISABLED].
                DISABLED (1):
                    Disabled query expansion. Only the exact search query is
                    used, even if
                    [SearchResponse.total_size][google.cloud.retail.v2beta.SearchResponse.total_size]
                    is zero.
                AUTO (3):
                    Automatic query expansion built by Google
                    Retail Search.
            """

            CONDITION_UNSPECIFIED = 0
            DISABLED = 1
            AUTO = 3

        condition: "SearchRequest.QueryExpansionSpec.Condition" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SearchRequest.QueryExpansionSpec.Condition",
        )
        pin_unexpanded_results: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class PersonalizationSpec(proto.Message):
        r"""The specification for personalization.

        Attributes:
            mode (google.cloud.retail_v2beta.types.SearchRequest.PersonalizationSpec.Mode):
                Defaults to
                [Mode.AUTO][google.cloud.retail.v2beta.SearchRequest.PersonalizationSpec.Mode.AUTO].
        """

        class Mode(proto.Enum):
            r"""The personalization mode of each search request.

            Values:
                MODE_UNSPECIFIED (0):
                    Default value. In this case, server behavior defaults to
                    [Mode.AUTO][google.cloud.retail.v2beta.SearchRequest.PersonalizationSpec.Mode.AUTO].
                AUTO (1):
                    Let CRS decide whether to use personalization
                    based on quality of user event data.
                DISABLED (2):
                    Disable personalization.
            """

            MODE_UNSPECIFIED = 0
            AUTO = 1
            DISABLED = 2

        mode: "SearchRequest.PersonalizationSpec.Mode" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SearchRequest.PersonalizationSpec.Mode",
        )

    class SpellCorrectionSpec(proto.Message):
        r"""The specification for query spell correction.

        Attributes:
            mode (google.cloud.retail_v2beta.types.SearchRequest.SpellCorrectionSpec.Mode):
                The mode under which spell correction should take effect to
                replace the original search query. Default to
                [Mode.AUTO][google.cloud.retail.v2beta.SearchRequest.SpellCorrectionSpec.Mode.AUTO].
        """

        class Mode(proto.Enum):
            r"""Enum describing under which mode spell correction should
            occur.

            Values:
                MODE_UNSPECIFIED (0):
                    Unspecified spell correction mode. In this case, server
                    behavior defaults to
                    [Mode.AUTO][google.cloud.retail.v2beta.SearchRequest.SpellCorrectionSpec.Mode.AUTO].
                SUGGESTION_ONLY (1):
                    Google Retail Search will try to find a spell suggestion if
                    there is any and put in the
                    [SearchResponse.corrected_query][google.cloud.retail.v2beta.SearchResponse.corrected_query].
                    The spell suggestion will not be used as the search query.
                AUTO (2):
                    Automatic spell correction built by Google
                    Retail Search. Search will be based on the
                    corrected query if found.
            """

            MODE_UNSPECIFIED = 0
            SUGGESTION_ONLY = 1
            AUTO = 2

        mode: "SearchRequest.SpellCorrectionSpec.Mode" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SearchRequest.SpellCorrectionSpec.Mode",
        )

    class ConversationalSearchSpec(proto.Message):
        r"""This field specifies all conversational related parameters
        addition to traditional retail search.

        Attributes:
            followup_conversation_requested (bool):
                This field specifies whether the customer
                would like to do conversational search. If this
                field is set to true, conversational related
                extra information will be returned from server
                side, including follow-up question, answer
                options, etc.
            conversation_id (str):
                This field specifies the conversation id, which maintains
                the state of the conversation between client side and server
                side. Use the value from the previous
                [ConversationalSearchResult.conversation_id][]. For the
                initial request, this should be empty.
            user_answer (google.cloud.retail_v2beta.types.SearchRequest.ConversationalSearchSpec.UserAnswer):
                This field specifies the current user answer
                during the conversational search. This can be
                either user selected from suggested answers or
                user input plain text.
        """

        class UserAnswer(proto.Message):
            r"""This field specifies the current user answer during the
            conversational search. This can be either user selected from
            suggested answers or user input plain text.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                text_answer (str):
                    This field specifies the incremental input
                    text from the user during the conversational
                    search.

                    This field is a member of `oneof`_ ``type``.
                selected_answer (google.cloud.retail_v2beta.types.SearchRequest.ConversationalSearchSpec.UserAnswer.SelectedAnswer):
                    This field specifies the selected attributes during the
                    conversational search. This should be a subset of
                    [ConversationalSearchResult.suggested_answers][].

                    This field is a member of `oneof`_ ``type``.
            """

            class SelectedAnswer(proto.Message):
                r"""This field specifies the selected answers during the
                conversational search.

                Attributes:
                    product_attribute_values (MutableSequence[google.cloud.retail_v2beta.types.ProductAttributeValue]):
                        This field is deprecated and should not be
                        set.
                    product_attribute_value (google.cloud.retail_v2beta.types.ProductAttributeValue):
                        This field specifies the selected answer
                        which is a attribute key-value.
                """

                product_attribute_values: MutableSequence["ProductAttributeValue"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=1,
                        message="ProductAttributeValue",
                    )
                )
                product_attribute_value: "ProductAttributeValue" = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="ProductAttributeValue",
                )

            text_answer: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="type",
            )
            selected_answer: "SearchRequest.ConversationalSearchSpec.UserAnswer.SelectedAnswer" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="type",
                message="SearchRequest.ConversationalSearchSpec.UserAnswer.SelectedAnswer",
            )

        followup_conversation_requested: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        conversation_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        user_answer: "SearchRequest.ConversationalSearchSpec.UserAnswer" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="SearchRequest.ConversationalSearchSpec.UserAnswer",
        )

    class TileNavigationSpec(proto.Message):
        r"""This field specifies tile navigation related parameters.

        Attributes:
            tile_navigation_requested (bool):
                This field specifies whether the customer
                would like to request tile navigation.
            applied_tiles (MutableSequence[google.cloud.retail_v2beta.types.Tile]):
                This optional field specifies the tiles which are already
                clicked in client side. While the feature works without this
                field set, particularly for an initial query, it is highly
                recommended to set this field because it can improve the
                quality of the search response and removes possible
                duplicate tiles.

                NOTE: This field is not being used for filtering search
                products. Client side should also put all the applied tiles
                in
                [SearchRequest.filter][google.cloud.retail.v2beta.SearchRequest.filter].
        """

        tile_navigation_requested: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        applied_tiles: MutableSequence["Tile"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Tile",
        )

    placement: str = proto.Field(
        proto.STRING,
        number=1,
    )
    branch: str = proto.Field(
        proto.STRING,
        number=2,
    )
    query: str = proto.Field(
        proto.STRING,
        number=3,
    )
    visitor_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    user_info: common.UserInfo = proto.Field(
        proto.MESSAGE,
        number=5,
        message=common.UserInfo,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=7,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=8,
    )
    offset: int = proto.Field(
        proto.INT32,
        number=9,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10,
    )
    canonical_filter: str = proto.Field(
        proto.STRING,
        number=28,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=11,
    )
    facet_specs: MutableSequence[FacetSpec] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=FacetSpec,
    )
    dynamic_facet_spec: DynamicFacetSpec = proto.Field(
        proto.MESSAGE,
        number=21,
        message=DynamicFacetSpec,
    )
    boost_spec: BoostSpec = proto.Field(
        proto.MESSAGE,
        number=13,
        message=BoostSpec,
    )
    query_expansion_spec: QueryExpansionSpec = proto.Field(
        proto.MESSAGE,
        number=14,
        message=QueryExpansionSpec,
    )
    variant_rollup_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    page_categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=23,
    )
    search_mode: SearchMode = proto.Field(
        proto.ENUM,
        number=31,
        enum=SearchMode,
    )
    personalization_spec: PersonalizationSpec = proto.Field(
        proto.MESSAGE,
        number=32,
        message=PersonalizationSpec,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=34,
    )
    spell_correction_spec: SpellCorrectionSpec = proto.Field(
        proto.MESSAGE,
        number=35,
        optional=True,
        message=SpellCorrectionSpec,
    )
    entity: str = proto.Field(
        proto.STRING,
        number=38,
    )
    conversational_search_spec: ConversationalSearchSpec = proto.Field(
        proto.MESSAGE,
        number=40,
        message=ConversationalSearchSpec,
    )
    tile_navigation_spec: TileNavigationSpec = proto.Field(
        proto.MESSAGE,
        number=41,
        message=TileNavigationSpec,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=43,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=44,
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=46,
    )
    user_attributes: MutableMapping[str, common.StringList] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=47,
        message=common.StringList,
    )


class SearchResponse(proto.Message):
    r"""Response message for
    [SearchService.Search][google.cloud.retail.v2beta.SearchService.Search]
    method.

    Attributes:
        results (MutableSequence[google.cloud.retail_v2beta.types.SearchResponse.SearchResult]):
            A list of matched items. The order represents
            the ranking.
        facets (MutableSequence[google.cloud.retail_v2beta.types.SearchResponse.Facet]):
            Results of facets requested by user.
        total_size (int):
            The estimated total count of matched items irrespective of
            pagination. The count of
            [results][google.cloud.retail.v2beta.SearchResponse.results]
            returned by pagination may be less than the
            [total_size][google.cloud.retail.v2beta.SearchResponse.total_size]
            that matches.
        corrected_query (str):
            Contains the spell corrected query, if found. If the spell
            correction type is AUTOMATIC, then the search results are
            based on corrected_query. Otherwise the original query is
            used for search.
        attribution_token (str):
            A unique search token. This should be included in the
            [UserEvent][google.cloud.retail.v2beta.UserEvent] logs
            resulting from this search, which enables accurate
            attribution of search model performance.
        next_page_token (str):
            A token that can be sent as
            [SearchRequest.page_token][google.cloud.retail.v2beta.SearchRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages.
        query_expansion_info (google.cloud.retail_v2beta.types.SearchResponse.QueryExpansionInfo):
            Query expansion information for the returned
            results.
        redirect_uri (str):
            The URI of a customer-defined redirect page. If redirect
            action is triggered, no search is performed, and only
            [redirect_uri][google.cloud.retail.v2beta.SearchResponse.redirect_uri]
            and
            [attribution_token][google.cloud.retail.v2beta.SearchResponse.attribution_token]
            are set in the response.
        applied_controls (MutableSequence[str]):
            The fully qualified resource name of applied
            `controls <https://cloud.google.com/retail/docs/serving-control-rules>`__.
        pin_control_metadata (google.cloud.retail_v2beta.types.PinControlMetadata):
            Metadata for pin controls which were
            applicable to the request. This contains two map
            fields, one for all matched pins and one for
            pins which were matched but not applied.

            The two maps are keyed by pin position, and the
            values are the product ids which were matched to
            that pin.
        invalid_condition_boost_specs (MutableSequence[google.cloud.retail_v2beta.types.SearchRequest.BoostSpec.ConditionBoostSpec]):
            The invalid
            [SearchRequest.BoostSpec.condition_boost_specs][google.cloud.retail.v2beta.SearchRequest.BoostSpec.condition_boost_specs]
            that are not applied during serving.
        experiment_info (MutableSequence[google.cloud.retail_v2beta.types.ExperimentInfo]):
            Metadata related to A/B testing experiment
            associated with this response. Only exists when
            an experiment is triggered.
        conversational_search_result (google.cloud.retail_v2beta.types.SearchResponse.ConversationalSearchResult):
            This field specifies all related information
            that is needed on client side for UI rendering
            of conversational retail search.
        tile_navigation_result (google.cloud.retail_v2beta.types.SearchResponse.TileNavigationResult):
            This field specifies all related information
            for tile navigation that will be used in client
            side.
    """

    class SearchResult(proto.Message):
        r"""Represents the search results.

        Attributes:
            id (str):
                [Product.id][google.cloud.retail.v2beta.Product.id] of the
                searched [Product][google.cloud.retail.v2beta.Product].
            product (google.cloud.retail_v2beta.types.Product):
                The product data snippet in the search response. Only
                [Product.name][google.cloud.retail.v2beta.Product.name] is
                guaranteed to be populated.

                [Product.variants][google.cloud.retail.v2beta.Product.variants]
                contains the product variants that match the search query.
                If there are multiple product variants matching the query,
                top 5 most relevant product variants are returned and
                ordered by relevancy.

                If relevancy can be deternmined, use
                [matching_variant_fields][google.cloud.retail.v2beta.SearchResponse.SearchResult.matching_variant_fields]
                to look up matched product variants fields. If relevancy
                cannot be determined, e.g. when searching "shoe" all
                products in a shoe product can be a match, 5 product
                variants are returned but order is meaningless.
            matching_variant_count (int):
                The count of matched
                [variant][google.cloud.retail.v2beta.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2beta.Product]s.
            matching_variant_fields (MutableMapping[str, google.protobuf.field_mask_pb2.FieldMask]):
                If a
                [variant][google.cloud.retail.v2beta.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2beta.Product] matches the
                search query, this map indicates which
                [Product][google.cloud.retail.v2beta.Product] fields are
                matched. The key is the
                [Product.name][google.cloud.retail.v2beta.Product.name], the
                value is a field mask of the matched
                [Product][google.cloud.retail.v2beta.Product] fields. If
                matched attributes cannot be determined, this map will be
                empty.

                For example, a key "sku1" with field mask
                "products.color_info" indicates there is a match between
                "sku1" [ColorInfo][google.cloud.retail.v2beta.ColorInfo] and
                the query.
            variant_rollup_values (MutableMapping[str, google.protobuf.struct_pb2.Value]):
                The rollup matching
                [variant][google.cloud.retail.v2beta.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2beta.Product] attributes.
                The key is one of the
                [SearchRequest.variant_rollup_keys][google.cloud.retail.v2beta.SearchRequest.variant_rollup_keys].
                The values are the merged and de-duplicated
                [Product][google.cloud.retail.v2beta.Product] attributes.
                Notice that the rollup values are respect filter. For
                example, when filtering by "colorFamilies:ANY("red")" and
                rollup "colorFamilies", only "red" is returned.

                For textual and numerical attributes, the rollup values is a
                list of string or double values with type
                [google.protobuf.ListValue][google.protobuf.ListValue]. For
                example, if there are two variants with colors "red" and
                "blue", the rollup values are

                ::

                    { key: "colorFamilies"
                      value {
                        list_value {
                          values { string_value: "red" }
                          values { string_value: "blue" }
                         }
                      }
                    }

                For
                [FulfillmentInfo][google.cloud.retail.v2beta.FulfillmentInfo],
                the rollup values is a double value with type
                [google.protobuf.Value][google.protobuf.Value]. For example,
                ``{key: "pickupInStore.store1" value { number_value: 10 }}``
                means a there are 10 variants in this product are available
                in the store "store1".
            personal_labels (MutableSequence[str]):
                Specifies previous events related to this product for this
                user based on
                [UserEvent][google.cloud.retail.v2beta.UserEvent] with same
                [SearchRequest.visitor_id][google.cloud.retail.v2beta.SearchRequest.visitor_id]
                or
                [UserInfo.user_id][google.cloud.retail.v2beta.UserInfo.user_id].

                This is set only when
                [SearchRequest.PersonalizationSpec.mode][google.cloud.retail.v2beta.SearchRequest.PersonalizationSpec.mode]
                is
                [SearchRequest.PersonalizationSpec.Mode.AUTO][google.cloud.retail.v2beta.SearchRequest.PersonalizationSpec.Mode.AUTO].

                Possible values:

                - ``purchased``: Indicates that this product has been
                  purchased before.
            model_scores (MutableMapping[str, google.cloud.retail_v2beta.types.DoubleList]):
                Google provided available scores.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        product: gcr_product.Product = proto.Field(
            proto.MESSAGE,
            number=2,
            message=gcr_product.Product,
        )
        matching_variant_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        matching_variant_fields: MutableMapping[str, field_mask_pb2.FieldMask] = (
            proto.MapField(
                proto.STRING,
                proto.MESSAGE,
                number=4,
                message=field_mask_pb2.FieldMask,
            )
        )
        variant_rollup_values: MutableMapping[str, struct_pb2.Value] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=5,
            message=struct_pb2.Value,
        )
        personal_labels: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )
        model_scores: MutableMapping[str, common.DoubleList] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=8,
            message=common.DoubleList,
        )

    class Facet(proto.Message):
        r"""A facet result.

        Attributes:
            key (str):
                The key for this facet. E.g., "colorFamilies"
                or "price" or "attributes.attr1".
            values (MutableSequence[google.cloud.retail_v2beta.types.SearchResponse.Facet.FacetValue]):
                The facet values for this field.
            dynamic_facet (bool):
                Whether the facet is dynamically generated.
        """

        class FacetValue(proto.Message):
            r"""A facet value which contains value names and their count.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                value (str):
                    Text value of a facet, such as "Black" for
                    facet "colorFamilies".

                    This field is a member of `oneof`_ ``facet_value``.
                interval (google.cloud.retail_v2beta.types.Interval):
                    Interval value for a facet, such as [10, 20) for facet
                    "price".

                    This field is a member of `oneof`_ ``facet_value``.
                count (int):
                    Number of items that have this facet value.
                min_value (float):
                    The minimum value in the
                    [FacetValue.interval][google.cloud.retail.v2beta.SearchResponse.Facet.FacetValue.interval].
                    Only supported on numerical facets and returned if
                    [SearchRequest.FacetSpec.FacetKey.return_min_max][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.return_min_max]
                    is true.
                max_value (float):
                    The maximum value in the
                    [FacetValue.interval][google.cloud.retail.v2beta.SearchResponse.Facet.FacetValue.interval].
                    Only supported on numerical facets and returned if
                    [SearchRequest.FacetSpec.FacetKey.return_min_max][google.cloud.retail.v2beta.SearchRequest.FacetSpec.FacetKey.return_min_max]
                    is true.
            """

            value: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="facet_value",
            )
            interval: common.Interval = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="facet_value",
                message=common.Interval,
            )
            count: int = proto.Field(
                proto.INT64,
                number=3,
            )
            min_value: float = proto.Field(
                proto.DOUBLE,
                number=5,
            )
            max_value: float = proto.Field(
                proto.DOUBLE,
                number=6,
            )

        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        values: MutableSequence["SearchResponse.Facet.FacetValue"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="SearchResponse.Facet.FacetValue",
            )
        )
        dynamic_facet: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class QueryExpansionInfo(proto.Message):
        r"""Information describing query expansion including whether
        expansion has occurred.

        Attributes:
            expanded_query (bool):
                Bool describing whether query expansion has
                occurred.
            pinned_result_count (int):
                Number of pinned results. This field will only be set when
                expansion happens and
                [SearchRequest.QueryExpansionSpec.pin_unexpanded_results][google.cloud.retail.v2beta.SearchRequest.QueryExpansionSpec.pin_unexpanded_results]
                is set to true.
        """

        expanded_query: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        pinned_result_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class ConversationalSearchResult(proto.Message):
        r"""This field specifies all related information that is needed
        on client side for UI rendering of conversational retail search.

        Attributes:
            conversation_id (str):
                Conversation UUID. This field will be stored in client side
                storage to maintain the conversation session with server and
                will be used for next search request's
                [SearchRequest.ConversationalSearchSpec.conversation_id][google.cloud.retail.v2beta.SearchRequest.ConversationalSearchSpec.conversation_id]
                to restore conversation state in server.
            refined_query (str):
                The current refined query for the conversational search.
                This field will be used in customer UI that the query in the
                search bar should be replaced with the refined query. For
                example, if
                [SearchRequest.query][google.cloud.retail.v2beta.SearchRequest.query]
                is ``dress`` and next
                [SearchRequest.ConversationalSearchSpec.UserAnswer.text_answer][google.cloud.retail.v2beta.SearchRequest.ConversationalSearchSpec.UserAnswer.text_answer]
                is ``red color``, which does not match any product attribute
                value filters, the refined query will be
                ``dress, red color``.
            additional_filters (MutableSequence[google.cloud.retail_v2beta.types.SearchResponse.ConversationalSearchResult.AdditionalFilter]):
                This field is deprecated but will be kept for backward
                compatibility. There is expected to have only one additional
                filter and the value will be the same to the same as field
                ``additional_filter``.
            followup_question (str):
                The follow-up question. e.g., ``What is the color?``
            suggested_answers (MutableSequence[google.cloud.retail_v2beta.types.SearchResponse.ConversationalSearchResult.SuggestedAnswer]):
                The answer options provided to client for the
                follow-up question.
            additional_filter (google.cloud.retail_v2beta.types.SearchResponse.ConversationalSearchResult.AdditionalFilter):
                This is the incremental additional filters implied from the
                current user answer. User should add the suggested addition
                filters to the previous
                [SearchRequest.filter][google.cloud.retail.v2beta.SearchRequest.filter],
                and use the merged filter in the follow up search request.
        """

        class SuggestedAnswer(proto.Message):
            r"""Suggested answers to the follow-up question.

            Attributes:
                product_attribute_value (google.cloud.retail_v2beta.types.ProductAttributeValue):
                    Product attribute value, including an
                    attribute key and an attribute value. Other
                    types can be added here in the future.
            """

            product_attribute_value: "ProductAttributeValue" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="ProductAttributeValue",
            )

        class AdditionalFilter(proto.Message):
            r"""Additional filter that client side need to apply.

            Attributes:
                product_attribute_value (google.cloud.retail_v2beta.types.ProductAttributeValue):
                    Product attribute value, including an
                    attribute key and an attribute value. Other
                    types can be added here in the future.
            """

            product_attribute_value: "ProductAttributeValue" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="ProductAttributeValue",
            )

        conversation_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        refined_query: str = proto.Field(
            proto.STRING,
            number=2,
        )
        additional_filters: MutableSequence[
            "SearchResponse.ConversationalSearchResult.AdditionalFilter"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="SearchResponse.ConversationalSearchResult.AdditionalFilter",
        )
        followup_question: str = proto.Field(
            proto.STRING,
            number=4,
        )
        suggested_answers: MutableSequence[
            "SearchResponse.ConversationalSearchResult.SuggestedAnswer"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="SearchResponse.ConversationalSearchResult.SuggestedAnswer",
        )
        additional_filter: "SearchResponse.ConversationalSearchResult.AdditionalFilter" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="SearchResponse.ConversationalSearchResult.AdditionalFilter",
        )

    class TileNavigationResult(proto.Message):
        r"""This field specifies all related information for tile
        navigation that will be used in client side.

        Attributes:
            tiles (MutableSequence[google.cloud.retail_v2beta.types.Tile]):
                The current tiles that are used for tile
                navigation, sorted by engagement.
        """

        tiles: MutableSequence["Tile"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Tile",
        )

    @property
    def raw_page(self):
        return self

    results: MutableSequence[SearchResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=SearchResult,
    )
    facets: MutableSequence[Facet] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Facet,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    corrected_query: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attribution_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )
    query_expansion_info: QueryExpansionInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        message=QueryExpansionInfo,
    )
    redirect_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    applied_controls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    pin_control_metadata: common.PinControlMetadata = proto.Field(
        proto.MESSAGE,
        number=22,
        message=common.PinControlMetadata,
    )
    invalid_condition_boost_specs: MutableSequence[
        "SearchRequest.BoostSpec.ConditionBoostSpec"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="SearchRequest.BoostSpec.ConditionBoostSpec",
    )
    experiment_info: MutableSequence["ExperimentInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="ExperimentInfo",
    )
    conversational_search_result: ConversationalSearchResult = proto.Field(
        proto.MESSAGE,
        number=18,
        message=ConversationalSearchResult,
    )
    tile_navigation_result: TileNavigationResult = proto.Field(
        proto.MESSAGE,
        number=19,
        message=TileNavigationResult,
    )


class ExperimentInfo(proto.Message):
    r"""Metadata for active A/B testing experiment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        serving_config_experiment (google.cloud.retail_v2beta.types.ExperimentInfo.ServingConfigExperiment):
            A/B test between existing Cloud Retail Search
            [ServingConfig][google.cloud.retail.v2beta.ServingConfig]s.

            This field is a member of `oneof`_ ``experiment_metadata``.
        experiment (str):
            The fully qualified resource name of the experiment that
            provides the serving config under test, should an active
            experiment exist. For example:
            ``projects/*/locations/global/catalogs/default_catalog/experiments/experiment_id``
    """

    class ServingConfigExperiment(proto.Message):
        r"""Metadata for active serving config A/B tests.

        Attributes:
            original_serving_config (str):
                The fully qualified resource name of the original
                [SearchRequest.placement][google.cloud.retail.v2beta.SearchRequest.placement]
                in the search request prior to reassignment by experiment
                API. For example:
                ``projects/*/locations/*/catalogs/*/servingConfigs/*``.
            experiment_serving_config (str):
                The fully qualified resource name of the serving config
                ``Experiment.VariantArm.serving_config_id`` responsible for
                generating the search response. For example:
                ``projects/*/locations/*/catalogs/*/servingConfigs/*``.
        """

        original_serving_config: str = proto.Field(
            proto.STRING,
            number=1,
        )
        experiment_serving_config: str = proto.Field(
            proto.STRING,
            number=2,
        )

    serving_config_experiment: ServingConfigExperiment = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="experiment_metadata",
        message=ServingConfigExperiment,
    )
    experiment: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
