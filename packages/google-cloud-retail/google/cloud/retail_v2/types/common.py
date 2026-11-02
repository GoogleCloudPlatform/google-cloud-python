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

__protobuf__ = proto.module(
    package="google.cloud.retail.v2",
    manifest={
        "AttributeConfigLevel",
        "SolutionType",
        "RecommendationsFilteringOption",
        "SearchSolutionUseCase",
        "Condition",
        "Rule",
        "Audience",
        "ColorInfo",
        "CustomAttribute",
        "FulfillmentInfo",
        "Image",
        "Interval",
        "PriceInfo",
        "Rating",
        "UserInfo",
        "LocalInventory",
        "PinControlMetadata",
        "StringList",
        "DoubleList",
    },
)


class AttributeConfigLevel(proto.Enum):
    r"""At which level we offer configuration for attributes.

    Values:
        ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED (0):
            Value used when unset. In this case, server behavior
            defaults to
            [CATALOG_LEVEL_ATTRIBUTE_CONFIG][google.cloud.retail.v2.AttributeConfigLevel.CATALOG_LEVEL_ATTRIBUTE_CONFIG].
        PRODUCT_LEVEL_ATTRIBUTE_CONFIG (1):
            At this level, we honor the attribute configurations set in
            [Product.attributes][google.cloud.retail.v2.Product.attributes].
        CATALOG_LEVEL_ATTRIBUTE_CONFIG (2):
            At this level, we honor the attribute configurations set in
            ``CatalogConfig.attribute_configs``.
    """

    ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED = 0
    PRODUCT_LEVEL_ATTRIBUTE_CONFIG = 1
    CATALOG_LEVEL_ATTRIBUTE_CONFIG = 2


class SolutionType(proto.Enum):
    r"""The type of solution.

    Values:
        SOLUTION_TYPE_UNSPECIFIED (0):
            Default value.
        SOLUTION_TYPE_RECOMMENDATION (1):
            Used for Recommendations AI.
        SOLUTION_TYPE_SEARCH (2):
            Used for Retail Search.
    """

    SOLUTION_TYPE_UNSPECIFIED = 0
    SOLUTION_TYPE_RECOMMENDATION = 1
    SOLUTION_TYPE_SEARCH = 2


class RecommendationsFilteringOption(proto.Enum):
    r"""If filtering for recommendations is enabled.

    Values:
        RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED (0):
            Value used when unset. In this case, server behavior
            defaults to
            [RECOMMENDATIONS_FILTERING_DISABLED][google.cloud.retail.v2.RecommendationsFilteringOption.RECOMMENDATIONS_FILTERING_DISABLED].
        RECOMMENDATIONS_FILTERING_DISABLED (1):
            Recommendation filtering is disabled.
        RECOMMENDATIONS_FILTERING_ENABLED (3):
            Recommendation filtering is enabled.
    """

    RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED = 0
    RECOMMENDATIONS_FILTERING_DISABLED = 1
    RECOMMENDATIONS_FILTERING_ENABLED = 3


class SearchSolutionUseCase(proto.Enum):
    r"""The use case of Cloud Retail Search.

    Values:
        SEARCH_SOLUTION_USE_CASE_UNSPECIFIED (0):
            The value when it's unspecified. In this case, server
            behavior defaults to
            [SEARCH_SOLUTION_USE_CASE_SEARCH][google.cloud.retail.v2.SearchSolutionUseCase.SEARCH_SOLUTION_USE_CASE_SEARCH].
        SEARCH_SOLUTION_USE_CASE_SEARCH (1):
            Search use case. Expects the traffic has a non-empty
            [query][google.cloud.retail.v2.SearchRequest.query].
        SEARCH_SOLUTION_USE_CASE_BROWSE (2):
            Browse use case. Expects the traffic has an empty
            [query][google.cloud.retail.v2.SearchRequest.query].
    """

    SEARCH_SOLUTION_USE_CASE_UNSPECIFIED = 0
    SEARCH_SOLUTION_USE_CASE_SEARCH = 1
    SEARCH_SOLUTION_USE_CASE_BROWSE = 2


class Condition(proto.Message):
    r"""Metadata that is used to define a condition that triggers an action.
    A valid condition must specify at least one of 'query_terms' or
    'products_filter'. If multiple fields are specified, the condition
    is met if all the fields are satisfied e.g. if a set of query terms
    and product_filter are set, then only items matching the
    product_filter for requests with a query matching the query terms
    wil get boosted.

    Attributes:
        query_terms (MutableSequence[google.cloud.retail_v2.types.Condition.QueryTerm]):
            A list (up to 10 entries) of terms to match
            the query on. If not specified, match all
            queries. If many query terms are specified, the
            condition is matched if any of the terms is a
            match (i.e. using the OR operator).
        active_time_range (MutableSequence[google.cloud.retail_v2.types.Condition.TimeRange]):
            Range of time(s) specifying when Condition is
            active. Condition true if any time range
            matches.
        page_categories (MutableSequence[str]):
            Used to support browse uses cases. A list (up to 10 entries)
            of categories or departments. The format should be the same
            as
            [UserEvent.page_categories][google.cloud.retail.v2.UserEvent.page_categories];
    """

    class QueryTerm(proto.Message):
        r"""Query terms that we want to match on.

        Attributes:
            value (str):
                The value of the term to match on.
                Value cannot be empty.
                Value can have at most 3 terms if specified as a
                partial match. Each space separated string is
                considered as one term. For example, "a b c" is
                3 terms and allowed, but " a b c d" is 4 terms
                and not allowed for a partial match.
            full_match (bool):
                Whether this is supposed to be a full or
                partial match.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        full_match: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class TimeRange(proto.Message):
        r"""Used for time-dependent conditions.
        Example: Want to have rule applied for week long sale.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start of time range. Range is inclusive.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                End of time range. Range is inclusive.
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

    query_terms: MutableSequence[QueryTerm] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=QueryTerm,
    )
    active_time_range: MutableSequence[TimeRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=TimeRange,
    )
    page_categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class Rule(proto.Message):
    r"""A rule is a condition-action pair

    - A condition defines when a rule is to be triggered.
    - An action specifies what occurs on that trigger. Currently rules
      only work for [controls][google.cloud.retail.v2.Control] with
      [SOLUTION_TYPE_SEARCH][google.cloud.retail.v2.SolutionType.SOLUTION_TYPE_SEARCH].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        boost_action (google.cloud.retail_v2.types.Rule.BoostAction):
            A boost action.

            This field is a member of `oneof`_ ``action``.
        redirect_action (google.cloud.retail_v2.types.Rule.RedirectAction):
            Redirects a shopper to a specific page.

            This field is a member of `oneof`_ ``action``.
        oneway_synonyms_action (google.cloud.retail_v2.types.Rule.OnewaySynonymsAction):
            Treats specific term as a synonym with a
            group of terms. Group of terms will not be
            treated as synonyms with the specific term.

            This field is a member of `oneof`_ ``action``.
        do_not_associate_action (google.cloud.retail_v2.types.Rule.DoNotAssociateAction):
            Prevents term from being associated with
            other terms.

            This field is a member of `oneof`_ ``action``.
        replacement_action (google.cloud.retail_v2.types.Rule.ReplacementAction):
            Replaces specific terms in the query.

            This field is a member of `oneof`_ ``action``.
        ignore_action (google.cloud.retail_v2.types.Rule.IgnoreAction):
            Ignores specific terms from query during
            search.

            This field is a member of `oneof`_ ``action``.
        filter_action (google.cloud.retail_v2.types.Rule.FilterAction):
            Filters results.

            This field is a member of `oneof`_ ``action``.
        twoway_synonyms_action (google.cloud.retail_v2.types.Rule.TwowaySynonymsAction):
            Treats a set of terms as synonyms of one
            another.

            This field is a member of `oneof`_ ``action``.
        force_return_facet_action (google.cloud.retail_v2.types.Rule.ForceReturnFacetAction):
            Force returns an attribute as a facet in the
            request.

            This field is a member of `oneof`_ ``action``.
        remove_facet_action (google.cloud.retail_v2.types.Rule.RemoveFacetAction):
            Remove an attribute as a facet in the request
            (if present).

            This field is a member of `oneof`_ ``action``.
        pin_action (google.cloud.retail_v2.types.Rule.PinAction):
            Pins one or more specified products to a
            specific position in the results.

            This field is a member of `oneof`_ ``action``.
        condition (google.cloud.retail_v2.types.Condition):
            Required. The condition that triggers the
            rule. If the condition is empty, the rule will
            always apply.
    """

    class BoostAction(proto.Message):
        r"""A boost action to apply to results matching condition
        specified above.

        Attributes:
            boost (float):
                Strength of the condition boost, which must be in [-1, 1].
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
            products_filter (str):
                The filter can have a max size of 5000 characters. An
                expression which specifies which products to apply an action
                to. The syntax and supported fields are the same as a filter
                expression. See
                [SearchRequest.filter][google.cloud.retail.v2.SearchRequest.filter]
                for detail syntax and limitations.

                Examples:

                - To boost products with product ID "product_1" or
                  "product_2", and color "Red" or "Blue": *(id:
                  ANY("product_1", "product_2"))* *AND* *(colorFamilies:
                  ANY("Red", "Blue"))*
        """

        boost: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        products_filter: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class FilterAction(proto.Message):
        r"""- Rule Condition:

          - No
            [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
            provided is a global match.
          - 1 or more
            [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
            provided are combined with OR operator.

        - Action Input: The request query and filter that are applied to the
          retrieved products, in addition to any filters already provided
          with the SearchRequest. The AND operator is used to combine the
          query's existing filters with the filter rule(s). NOTE: May result
          in 0 results when filters conflict.

        - Action Result: Filters the returned objects to be ONLY those that
          passed the filter.

        Attributes:
            filter (str):
                A filter to apply on the matching condition results.
                Supported features:

                - [filter][google.cloud.retail.v2.Rule.FilterAction.filter]
                  must be set.
                - Filter syntax is identical to
                  [SearchRequest.filter][google.cloud.retail.v2.SearchRequest.filter].
                  For more information, see
                  `Filter </retail/docs/filter-and-order#filter>`__.
                - To filter products with product ID "product_1" or
                  "product_2", and color "Red" or "Blue": *(id:
                  ANY("product_1", "product_2"))* *AND* *(colorFamilies:
                  ANY("Red", "Blue"))*
        """

        filter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RedirectAction(proto.Message):
        r"""Redirects a shopper to a specific page.

        - Rule Condition: Must specify
          [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms].
        - Action Input: Request Query
        - Action Result: Redirects shopper to provided uri.

        Attributes:
            redirect_uri (str):
                URL must have length equal or less than 2000
                characters.
        """

        redirect_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class TwowaySynonymsAction(proto.Message):
        r"""Creates a set of terms that will be treated as synonyms of each
        other. Example: synonyms of "sneakers" and "shoes":

        - "sneakers" will use a synonym of "shoes".
        - "shoes" will use a synonym of "sneakers".

        Attributes:
            synonyms (MutableSequence[str]):
                Defines a set of synonyms.
                Can specify up to 100 synonyms.
                Must specify at least 2 synonyms.
        """

        synonyms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class OnewaySynonymsAction(proto.Message):
        r"""Maps a set of terms to a set of synonyms. Set of synonyms will be
        treated as synonyms of each query term only. ``query_terms`` will
        not be treated as synonyms of each other. Example: "sneakers" will
        use a synonym of "shoes". "shoes" will not use a synonym of
        "sneakers".

        Attributes:
            query_terms (MutableSequence[str]):
                Terms from the search query.
                Will treat synonyms as their synonyms.
                Not themselves synonyms of the synonyms.
                Can specify up to 100 terms.
            synonyms (MutableSequence[str]):
                Defines a set of synonyms.
                Cannot contain duplicates.
                Can specify up to 100 synonyms.
            oneway_terms (MutableSequence[str]):
                Will be [deprecated = true] post migration;
        """

        query_terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        synonyms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        oneway_terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class DoNotAssociateAction(proto.Message):
        r"""Prevents ``query_term`` from being associated with specified terms
        during search. Example: Don't associate "gShoe" and "cheap".

        Attributes:
            query_terms (MutableSequence[str]):
                Terms from the search query. Will not consider
                do_not_associate_terms for search if in search query. Can
                specify up to 100 terms.
            do_not_associate_terms (MutableSequence[str]):
                Cannot contain duplicates or the query term.
                Can specify up to 100 terms.
            terms (MutableSequence[str]):
                Will be [deprecated = true] post migration;
        """

        query_terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        do_not_associate_terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class ReplacementAction(proto.Message):
        r"""Replaces a term in the query. Multiple replacement candidates can be
        specified. All ``query_terms`` will be replaced with the replacement
        term. Example: Replace "gShoe" with "google shoe".

        Attributes:
            query_terms (MutableSequence[str]):
                Terms from the search query.
                Will be replaced by replacement term.
                Can specify up to 100 terms.
            replacement_term (str):
                Term that will be used for replacement.
            term (str):
                Will be [deprecated = true] post migration;
        """

        query_terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        replacement_term: str = proto.Field(
            proto.STRING,
            number=3,
        )
        term: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class IgnoreAction(proto.Message):
        r"""Prevents a term in the query from being used in search.
        Example: Don't search for "shoddy".

        Attributes:
            ignore_terms (MutableSequence[str]):
                Terms to ignore in the search query.
        """

        ignore_terms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class ForceReturnFacetAction(proto.Message):
        r"""Force returns an attribute/facet in the request around a certain
        position or above.

        - Rule Condition: Must specify non-empty
          [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
          (for search only) or
          [Condition.page_categories][google.cloud.retail.v2.Condition.page_categories]
          (for browse only), but can't specify both.

        - Action Inputs: attribute name, position

        - Action Result: Will force return a facet key around a certain
          position or above if the condition is satisfied.

        Example: Suppose the query is "shoes", the
        [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
        is "shoes", the
        [ForceReturnFacetAction.FacetPositionAdjustment.attribute_name][google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.attribute_name]
        is "size" and the
        [ForceReturnFacetAction.FacetPositionAdjustment.position][google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.position]
        is 8.

        Two cases: a) The facet key "size" is not already in the top 8
        slots, then the facet "size" will appear at a position close to 8.
        b) The facet key "size" in among the top 8 positions in the request,
        then it will stay at its current rank.

        Attributes:
            facet_position_adjustments (MutableSequence[google.cloud.retail_v2.types.Rule.ForceReturnFacetAction.FacetPositionAdjustment]):
                Each instance corresponds to a force return
                attribute for the given condition. There can't
                be more 15 instances here.
        """

        class FacetPositionAdjustment(proto.Message):
            r"""Each facet position adjustment consists of a single attribute
            name (i.e. facet key) along with a specified position.

            Attributes:
                attribute_name (str):
                    The attribute name to force return as a
                    facet. Each attribute name should be a valid
                    attribute name, be non-empty and contain at most
                    80 characters long.
                position (int):
                    This is the position in the request as
                    explained above. It should be strictly positive
                    be at most 100.
            """

            attribute_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            position: int = proto.Field(
                proto.INT32,
                number=2,
            )

        facet_position_adjustments: MutableSequence[
            "Rule.ForceReturnFacetAction.FacetPositionAdjustment"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Rule.ForceReturnFacetAction.FacetPositionAdjustment",
        )

    class RemoveFacetAction(proto.Message):
        r"""Removes an attribute/facet in the request if is present.

        - Rule Condition: Must specify non-empty
          [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
          (for search only) or
          [Condition.page_categories][google.cloud.retail.v2.Condition.page_categories]
          (for browse only), but can't specify both.

        - Action Input: attribute name

        - Action Result: Will remove the attribute (as a facet) from the
          request if it is present.

        Example: Suppose the query is "shoes", the
        [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
        is "shoes" and the attribute name "size", then facet key "size" will
        be removed from the request (if it is present).

        Attributes:
            attribute_names (MutableSequence[str]):
                The attribute names (i.e. facet keys) to
                remove from the dynamic facets (if present in
                the request). There can't be more 3 attribute
                names. Each attribute name should be a valid
                attribute name, be non-empty and contain at most
                80 characters.
        """

        attribute_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class PinAction(proto.Message):
        r"""Pins one or more specified products to a specific position in the
        results.

        - Rule Condition: Must specify non-empty
          [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
          (for search only) or
          [Condition.page_categories][google.cloud.retail.v2.Condition.page_categories]
          (for browse only), but can't specify both.

        - Action Input: mapping of ``[pin_position, product_id]`` pairs (pin
          position uses 1-based indexing).

        - Action Result: Will pin products with matching ids to the position
          specified in the final result order.

        Example: Suppose the query is ``shoes``, the
        [Condition.query_terms][google.cloud.retail.v2.Condition.query_terms]
        is ``shoes`` and the pin_map has ``{1, "pid1"}``, then product with
        ``pid1`` will be pinned to the top position in the final results.

        If multiple PinActions are matched to a single request the actions
        will be processed from most to least recently updated.

        Pins to positions larger than the max allowed page size of 120 are
        not allowed.

        Attributes:
            pin_map (MutableMapping[int, str]):
                Required. A map of positions to product_ids.

                Partial matches per action are allowed, if a certain
                position in the map is already filled that
                ``[position, product_id]`` pair will be ignored but the rest
                may still be applied. This case will only occur if multiple
                pin actions are matched to a single request, as the map
                guarantees that pin positions are unique within the same
                action.

                Duplicate product_ids are not permitted within a single pin
                map.

                The max size of this map is 120, equivalent to the max
                `request page
                size <https://cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs.placements/search#request-body>`__.
        """

        pin_map: MutableMapping[int, str] = proto.MapField(
            proto.INT64,
            proto.STRING,
            number=1,
        )

    boost_action: BoostAction = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message=BoostAction,
    )
    redirect_action: RedirectAction = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message=RedirectAction,
    )
    oneway_synonyms_action: OnewaySynonymsAction = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action",
        message=OnewaySynonymsAction,
    )
    do_not_associate_action: DoNotAssociateAction = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="action",
        message=DoNotAssociateAction,
    )
    replacement_action: ReplacementAction = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="action",
        message=ReplacementAction,
    )
    ignore_action: IgnoreAction = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message=IgnoreAction,
    )
    filter_action: FilterAction = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="action",
        message=FilterAction,
    )
    twoway_synonyms_action: TwowaySynonymsAction = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="action",
        message=TwowaySynonymsAction,
    )
    force_return_facet_action: ForceReturnFacetAction = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="action",
        message=ForceReturnFacetAction,
    )
    remove_facet_action: RemoveFacetAction = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="action",
        message=RemoveFacetAction,
    )
    pin_action: PinAction = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="action",
        message=PinAction,
    )
    condition: "Condition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Condition",
    )


class Audience(proto.Message):
    r"""An intended audience of the
    [Product][google.cloud.retail.v2.Product] for whom it's sold.

    Attributes:
        genders (MutableSequence[str]):
            The genders of the audience. Strongly encouraged to use the
            standard values: "male", "female", "unisex".

            At most 5 values are allowed. Each value must be a UTF-8
            encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `gender <https://support.google.com/merchants/answer/6324479>`__.
            Schema.org property
            `Product.audience.suggestedGender <https://schema.org/suggestedGender>`__.
        age_groups (MutableSequence[str]):
            The age groups of the audience. Strongly encouraged to use
            the standard values: "newborn" (up to 3 months old),
            "infant" (3–12 months old), "toddler" (1–5 years old),
            "kids" (5–13 years old), "adult" (typically teens or older).

            At most 5 values are allowed. Each value must be a UTF-8
            encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `age_group <https://support.google.com/merchants/answer/6324463>`__.
            Schema.org property
            `Product.audience.suggestedMinAge <https://schema.org/suggestedMinAge>`__
            and
            `Product.audience.suggestedMaxAge <https://schema.org/suggestedMaxAge>`__.
    """

    genders: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    age_groups: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ColorInfo(proto.Message):
    r"""The color information of a
    [Product][google.cloud.retail.v2.Product].

    Attributes:
        color_families (MutableSequence[str]):
            The standard color families. Strongly recommended to use the
            following standard color groups: "Red", "Pink", "Orange",
            "Yellow", "Purple", "Green", "Cyan", "Blue", "Brown",
            "White", "Gray", "Black" and "Mixed". Normally it is
            expected to have only 1 color family. May consider using
            single "Mixed" instead of multiple values.

            A maximum of 5 values are allowed. Each value must be a
            UTF-8 encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `color <https://support.google.com/merchants/answer/6324487>`__.
            Schema.org property
            `Product.color <https://schema.org/color>`__.

            The colorFamilies field as a system attribute is not a
            required field but strongly recommended to be specified.
            Google Search models treat this field as more important than
            a custom product attribute when specified.
        colors (MutableSequence[str]):
            The color display names, which may be different from
            standard color family names, such as the color aliases used
            in the website frontend. Normally it is expected to have
            only 1 color. May consider using single "Mixed" instead of
            multiple values.

            A maximum of 75 colors are allowed. Each value must be a
            UTF-8 encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `color <https://support.google.com/merchants/answer/6324487>`__.
            Schema.org property
            `Product.color <https://schema.org/color>`__.
    """

    color_families: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    colors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CustomAttribute(proto.Message):
    r"""A custom attribute that is not explicitly modeled in
    [Product][google.cloud.retail.v2.Product].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (MutableSequence[str]):
            The textual values of this custom attribute. For example,
            ``["yellow", "green"]`` when the key is "color".

            Empty string is not allowed. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Exactly one of
            [text][google.cloud.retail.v2.CustomAttribute.text] or
            [numbers][google.cloud.retail.v2.CustomAttribute.numbers]
            should be set. Otherwise, an INVALID_ARGUMENT error is
            returned.
        numbers (MutableSequence[float]):
            The numerical values of this custom attribute. For example,
            ``[2.3, 15.4]`` when the key is "lengths_cm".

            Exactly one of
            [text][google.cloud.retail.v2.CustomAttribute.text] or
            [numbers][google.cloud.retail.v2.CustomAttribute.numbers]
            should be set. Otherwise, an INVALID_ARGUMENT error is
            returned.
        searchable (bool):
            This field is normally ignored unless
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2.AttributesConfig.attribute_config_level]
            of the [Catalog][google.cloud.retail.v2.Catalog] is set to
            the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For
            information about product-level attribute configuration, see
            `Configuration
            modes <https://cloud.google.com/retail/docs/attribute-config#config-modes>`__.
            If true, custom attribute values are searchable by text
            queries in
            [SearchService.Search][google.cloud.retail.v2.SearchService.Search].

            This field is ignored in a
            [UserEvent][google.cloud.retail.v2.UserEvent].

            Only set if type
            [text][google.cloud.retail.v2.CustomAttribute.text] is set.
            Otherwise, a INVALID_ARGUMENT error is returned.

            This field is a member of `oneof`_ ``_searchable``.
        indexable (bool):
            This field is normally ignored unless
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2.AttributesConfig.attribute_config_level]
            of the [Catalog][google.cloud.retail.v2.Catalog] is set to
            the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For
            information about product-level attribute configuration, see
            `Configuration
            modes <https://cloud.google.com/retail/docs/attribute-config#config-modes>`__.
            If true, custom attribute values are indexed, so that they
            can be filtered, faceted or boosted in
            [SearchService.Search][google.cloud.retail.v2.SearchService.Search].

            This field is ignored in a
            [UserEvent][google.cloud.retail.v2.UserEvent].

            See
            [SearchRequest.filter][google.cloud.retail.v2.SearchRequest.filter],
            [SearchRequest.facet_specs][google.cloud.retail.v2.SearchRequest.facet_specs]
            and
            [SearchRequest.boost_spec][google.cloud.retail.v2.SearchRequest.boost_spec]
            for more details.

            This field is a member of `oneof`_ ``_indexable``.
    """

    text: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    numbers: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=2,
    )
    searchable: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    indexable: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


class FulfillmentInfo(proto.Message):
    r"""Fulfillment information, such as the store IDs for in-store
    pickup or region IDs for different shipping methods.

    Attributes:
        type_ (str):
            The fulfillment type, including commonly used types (such as
            pickup in store and same day delivery), and custom types.
            Customers have to map custom types to their display names
            before rendering UI.

            Supported values:

            - "pickup-in-store"
            - "ship-to-store"
            - "same-day-delivery"
            - "next-day-delivery"
            - "custom-type-1"
            - "custom-type-2"
            - "custom-type-3"
            - "custom-type-4"
            - "custom-type-5"

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.
        place_ids (MutableSequence[str]):
            The IDs for this
            [type][google.cloud.retail.v2.FulfillmentInfo.type], such as
            the store IDs for
            [FulfillmentInfo.type.pickup-in-store][google.cloud.retail.v2.FulfillmentInfo.type]
            or the region IDs for
            [FulfillmentInfo.type.same-day-delivery][google.cloud.retail.v2.FulfillmentInfo.type].

            A maximum of 3000 values are allowed. Each value must be a
            string with a length limit of 30 characters, matching the
            pattern ``[a-zA-Z0-9_-]+``, such as "store1" or "REGION-2".
            Otherwise, an INVALID_ARGUMENT error is returned.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    place_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Image(proto.Message):
    r"""[Product][google.cloud.retail.v2.Product] image. Recommendations AI
    and Retail Search use product images to improve prediction and
    search results. Product images can be returned in results, and are
    shown in prediction or search previews in the console. Please try to
    provide correct product images and avoid using images with size too
    small.

    Attributes:
        uri (str):
            Required. URI of the image.

            This field must be a valid UTF-8 encoded URI with a length
            limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Google Merchant Center property
            `image_link <https://support.google.com/merchants/answer/6324350>`__.
            Schema.org property
            `Product.image <https://schema.org/image>`__.
        height (int):
            Height of the image in number of pixels.

            This field must be nonnegative. Otherwise, an
            INVALID_ARGUMENT error is returned.
        width (int):
            Width of the image in number of pixels.

            This field must be nonnegative. Otherwise, an
            INVALID_ARGUMENT error is returned.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    height: int = proto.Field(
        proto.INT32,
        number=2,
    )
    width: int = proto.Field(
        proto.INT32,
        number=3,
    )


class Interval(proto.Message):
    r"""A floating point interval.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        minimum (float):
            Inclusive lower bound.

            This field is a member of `oneof`_ ``min``.
        exclusive_minimum (float):
            Exclusive lower bound.

            This field is a member of `oneof`_ ``min``.
        maximum (float):
            Inclusive upper bound.

            This field is a member of `oneof`_ ``max``.
        exclusive_maximum (float):
            Exclusive upper bound.

            This field is a member of `oneof`_ ``max``.
    """

    minimum: float = proto.Field(
        proto.DOUBLE,
        number=1,
        oneof="min",
    )
    exclusive_minimum: float = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="min",
    )
    maximum: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="max",
    )
    exclusive_maximum: float = proto.Field(
        proto.DOUBLE,
        number=4,
        oneof="max",
    )


class PriceInfo(proto.Message):
    r"""The price information of a
    [Product][google.cloud.retail.v2.Product].

    Attributes:
        currency_code (str):
            The 3-letter currency code defined in `ISO
            4217 <https://www.iso.org/iso-4217-currency-codes.html>`__.

            If this field is an unrecognizable currency code, an
            INVALID_ARGUMENT error is returned.

            The
            [Product.Type.VARIANT][google.cloud.retail.v2.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2.Product]s with the same
            [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id]
            must share the same
            [currency_code][google.cloud.retail.v2.PriceInfo.currency_code].
            Otherwise, a FAILED_PRECONDITION error is returned.
        price (float):
            Price of the product.

            Google Merchant Center property
            `price <https://support.google.com/merchants/answer/6324371>`__.
            Schema.org property
            `Offer.price <https://schema.org/price>`__.
        original_price (float):
            Price of the product without any discount. If zero, by
            default set to be the
            [price][google.cloud.retail.v2.PriceInfo.price]. If set,
            [original_price][google.cloud.retail.v2.PriceInfo.original_price]
            should be greater than or equal to
            [price][google.cloud.retail.v2.PriceInfo.price], otherwise
            an INVALID_ARGUMENT error is thrown.
        cost (float):
            The costs associated with the sale of a particular product.
            Used for gross profit reporting.

            - Profit = [price][google.cloud.retail.v2.PriceInfo.price] -
              [cost][google.cloud.retail.v2.PriceInfo.cost]

            Google Merchant Center property
            `cost_of_goods_sold <https://support.google.com/merchants/answer/9017895>`__.
        price_effective_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the
            [price][google.cloud.retail.v2.PriceInfo.price] starts to be
            effective. This can be set as a future timestamp, and the
            [price][google.cloud.retail.v2.PriceInfo.price] is only used
            for search after
            [price_effective_time][google.cloud.retail.v2.PriceInfo.price_effective_time].
            If so, the
            [original_price][google.cloud.retail.v2.PriceInfo.original_price]
            must be set and
            [original_price][google.cloud.retail.v2.PriceInfo.original_price]
            is used before
            [price_effective_time][google.cloud.retail.v2.PriceInfo.price_effective_time].

            Do not set if
            [price][google.cloud.retail.v2.PriceInfo.price] is always
            effective because it will cause additional latency during
            search.
        price_expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the
            [price][google.cloud.retail.v2.PriceInfo.price] stops to be
            effective. The
            [price][google.cloud.retail.v2.PriceInfo.price] is used for
            search before
            [price_expire_time][google.cloud.retail.v2.PriceInfo.price_expire_time].
            If this field is set, the
            [original_price][google.cloud.retail.v2.PriceInfo.original_price]
            must be set and
            [original_price][google.cloud.retail.v2.PriceInfo.original_price]
            is used after
            [price_expire_time][google.cloud.retail.v2.PriceInfo.price_expire_time].

            Do not set if
            [price][google.cloud.retail.v2.PriceInfo.price] is always
            effective because it will cause additional latency during
            search.
        price_range (google.cloud.retail_v2.types.PriceInfo.PriceRange):
            Output only. The price range of all the child
            [Product.Type.VARIANT][google.cloud.retail.v2.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2.Product]s grouped together
            on the
            [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2.Product]. Only populated
            for
            [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2.Product]s.

            Note: This field is OUTPUT_ONLY for
            [ProductService.GetProduct][google.cloud.retail.v2.ProductService.GetProduct].
            Do not set this field in API requests.
    """

    class PriceRange(proto.Message):
        r"""The price range of all
        [variant][google.cloud.retail.v2.Product.Type.VARIANT]
        [Product][google.cloud.retail.v2.Product] having the same
        [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id].

        Attributes:
            price (google.cloud.retail_v2.types.Interval):
                The inclusive
                [Product.pricing_info.price][google.cloud.retail.v2.PriceInfo.price]
                interval of all
                [variant][google.cloud.retail.v2.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2.Product] having the same
                [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id].
            original_price (google.cloud.retail_v2.types.Interval):
                The inclusive
                [Product.pricing_info.original_price][google.cloud.retail.v2.PriceInfo.original_price]
                internal of all
                [variant][google.cloud.retail.v2.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2.Product] having the same
                [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id].
        """

        price: "Interval" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Interval",
        )
        original_price: "Interval" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Interval",
        )

    currency_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    price: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    original_price: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    cost: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    price_effective_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    price_expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    price_range: PriceRange = proto.Field(
        proto.MESSAGE,
        number=7,
        message=PriceRange,
    )


class Rating(proto.Message):
    r"""The rating of a [Product][google.cloud.retail.v2.Product].

    Attributes:
        rating_count (int):
            The total number of ratings. This value is independent of
            the value of
            [rating_histogram][google.cloud.retail.v2.Rating.rating_histogram].

            This value must be nonnegative. Otherwise, an
            INVALID_ARGUMENT error is returned.
        average_rating (float):
            The average rating of the
            [Product][google.cloud.retail.v2.Product].

            The rating is scaled at 1-5. Otherwise, an INVALID_ARGUMENT
            error is returned.
        rating_histogram (MutableSequence[int]):
            List of rating counts per rating value (index = rating - 1).
            The list is empty if there is no rating. If the list is
            non-empty, its size is always 5. Otherwise, an
            INVALID_ARGUMENT error is returned.

            For example, [41, 14, 13, 47, 303]. It means that the
            [Product][google.cloud.retail.v2.Product] got 41 ratings
            with 1 star, 14 ratings with 2 star, and so on.
    """

    rating_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    average_rating: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    rating_histogram: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )


class UserInfo(proto.Message):
    r"""Information of an end user.

    Attributes:
        user_id (str):
            Highly recommended for logged-in users. Unique identifier
            for logged-in user, such as a user name. Don't set for
            anonymous users.

            Always use a hashed value for this ID.

            Don't set the field to the same fixed ID for different
            users. This mixes the event history of those users together,
            which results in degraded model quality.

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        ip_address (str):
            The end user's IP address. This field is used to extract
            location information for personalization.

            This field must be either an IPv4 address (e.g.
            "104.133.9.80") or an IPv6 address (e.g.
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334"). Otherwise, an
            INVALID_ARGUMENT error is returned.

            This should not be set when:

            - setting
              [SearchRequest.user_info][google.cloud.retail.v2.SearchRequest.user_info].
            - using the JavaScript tag in
              [UserEventService.CollectUserEvent][google.cloud.retail.v2.UserEventService.CollectUserEvent]
              or if
              [direct_user_request][google.cloud.retail.v2.UserInfo.direct_user_request]
              is set.
        user_agent (str):
            User agent as included in the HTTP header. The field must be
            a UTF-8 encoded string with a length limit of 1,000
            characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            This should not be set when using the client side event
            reporting with GTM or JavaScript tag in
            [UserEventService.CollectUserEvent][google.cloud.retail.v2.UserEventService.CollectUserEvent]
            or if
            [direct_user_request][google.cloud.retail.v2.UserInfo.direct_user_request]
            is set.
        direct_user_request (bool):
            True if the request is made directly from the end user, in
            which case the
            [ip_address][google.cloud.retail.v2.UserInfo.ip_address] and
            [user_agent][google.cloud.retail.v2.UserInfo.user_agent] can
            be populated from the HTTP request. This flag should be set
            only if the API request is made directly from the end user
            such as a mobile app (and not if a gateway or a server is
            processing and pushing the user events).

            This should not be set when using the JavaScript tag in
            [UserEventService.CollectUserEvent][google.cloud.retail.v2.UserEventService.CollectUserEvent].
    """

    user_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    direct_user_request: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class LocalInventory(proto.Message):
    r"""The inventory information at a place (e.g. a store)
    identified by a place ID.

    Attributes:
        place_id (str):
            Optional. The place ID for the current set of
            inventory information.
        price_info (google.cloud.retail_v2.types.PriceInfo):
            Optional. Product price and cost information.

            Google Merchant Center property
            `price <https://support.google.com/merchants/answer/6324371>`__.
        attributes (MutableMapping[str, google.cloud.retail_v2.types.CustomAttribute]):
            Optional. Additional local inventory attributes, for
            example, store name, promotion tags, etc.

            This field needs to pass all below criteria, otherwise an
            INVALID_ARGUMENT error is returned:

            - At most 30 attributes are allowed.
            - The key must be a UTF-8 encoded string with a length limit
              of 32 characters.
            - The key must match the pattern:
              ``[a-zA-Z0-9][a-zA-Z0-9_]*``. For example, key0LikeThis or
              KEY_1_LIKE_THIS.
            - The attribute values must be of the same type (text or
              number).
            - Only 1 value is allowed for each attribute.
            - For text values, the length limit is 256 UTF-8 characters.
            - The attribute does not support search. The ``searchable``
              field should be unset or set to false.
            - The max summed total bytes of custom attribute keys and
              values per product is 5MiB.
        fulfillment_types (MutableSequence[str]):
            Optional. Supported fulfillment types. Valid fulfillment
            type values include commonly used types (such as pickup in
            store and same day delivery), and custom types. Customers
            have to map custom types to their display names before
            rendering UI.

            Supported values:

            - "pickup-in-store"
            - "ship-to-store"
            - "same-day-delivery"
            - "next-day-delivery"
            - "custom-type-1"
            - "custom-type-2"
            - "custom-type-3"
            - "custom-type-4"
            - "custom-type-5"

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.

            All the elements must be distinct. Otherwise, an
            INVALID_ARGUMENT error is returned.
    """

    place_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    price_info: "PriceInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PriceInfo",
    )
    attributes: MutableMapping[str, "CustomAttribute"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message="CustomAttribute",
    )
    fulfillment_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class PinControlMetadata(proto.Message):
    r"""Metadata for pinning to be returned in the response.
    This is used for distinguishing between applied vs dropped pins.

    Attributes:
        all_matched_pins (MutableMapping[int, google.cloud.retail_v2.types.PinControlMetadata.ProductPins]):
            Map of all matched pins, keyed by pin
            position.
        dropped_pins (MutableMapping[int, google.cloud.retail_v2.types.PinControlMetadata.ProductPins]):
            Map of pins that were dropped due to overlap
            with other matching pins, keyed by pin position.
    """

    class ProductPins(proto.Message):
        r"""List of product ids which have associated pins.

        Attributes:
            product_id (MutableSequence[str]):
                List of product ids which have associated
                pins.
        """

        product_id: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    all_matched_pins: MutableMapping[int, ProductPins] = proto.MapField(
        proto.INT64,
        proto.MESSAGE,
        number=1,
        message=ProductPins,
    )
    dropped_pins: MutableMapping[int, ProductPins] = proto.MapField(
        proto.INT64,
        proto.MESSAGE,
        number=2,
        message=ProductPins,
    )


class StringList(proto.Message):
    r"""A list of string values.

    Attributes:
        values (MutableSequence[str]):
            String values.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DoubleList(proto.Message):
    r"""A message with a list of double values.

    Attributes:
        values (MutableSequence[float]):
            The list of double values.
    """

    values: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
