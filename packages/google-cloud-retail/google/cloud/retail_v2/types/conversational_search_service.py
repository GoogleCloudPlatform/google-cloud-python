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

import proto  # type: ignore

from google.cloud.retail_v2.types import common, safety, search_service

__protobuf__ = proto.module(
    package="google.cloud.retail.v2",
    manifest={
        "ConversationalSearchRequest",
        "ConversationalSearchResponse",
    },
)


class ConversationalSearchRequest(proto.Message):
    r"""Request message for
    [ConversationalSearchService.ConversationalSearch][google.cloud.retail.v2.ConversationalSearchService.ConversationalSearch]
    method.

    Attributes:
        placement (str):
            Required. The resource name of the search engine placement,
            such as
            ``projects/*/locations/global/catalogs/default_catalog/placements/default_search``
            or
            ``projects/*/locations/global/catalogs/default_catalog/servingConfigs/default_serving_config``
            This field is used to identify the serving config name and
            the set of models that will be used to make the search.
        branch (str):
            Required. The branch resource name, such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/0``.

            Use "default_branch" as the branch ID or leave this field
            empty, to search products under the default branch.
        query (str):
            Optional. Raw search query to be searched
            for.
            If this field is empty, the request is
            considered a category browsing request.
        page_categories (MutableSequence[str]):
            Optional. The categories associated with a category page.
            Must be set for category navigation queries to achieve good
            search quality. The format should be the same as
            [UserEvent.page_categories][google.cloud.retail.v2.UserEvent.page_categories];

            To represent full path of category, use '>' sign to separate
            different hierarchies. If '>' is part of the category name,
            replace it with other character(s).

            Category pages include special pages such as sales or
            promotions. For instance, a special sale page may have the
            category hierarchy: "pageCategories" : ["Sales > 2017 Black
            Friday Deals"].
        conversation_id (str):
            Optional. This field specifies the conversation id, which
            maintains the state of the conversation between client side
            and server side. Use the value from the previous
            [ConversationalSearchResponse.conversation_id][google.cloud.retail.v2.ConversationalSearchResponse.conversation_id].
            For the initial request, this should be empty.
        search_params (google.cloud.retail_v2.types.ConversationalSearchRequest.SearchParams):
            Optional. Search parameters.
        visitor_id (str):
            Required. A unique identifier for tracking visitors. For
            example, this could be implemented with an HTTP cookie,
            which should be able to uniquely identify a visitor on a
            single device. This unique identifier should not change if
            the visitor logs in or out of the website.

            This should be the same identifier as
            [UserEvent.visitor_id][google.cloud.retail.v2.UserEvent.visitor_id].

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        user_info (google.cloud.retail_v2.types.UserInfo):
            Optional. User information.
        conversational_filtering_spec (google.cloud.retail_v2.types.ConversationalSearchRequest.ConversationalFilteringSpec):
            Optional. This field specifies all
            conversational filtering related parameters.
        user_labels (MutableMapping[str, str]):
            Optional. The user labels applied to a resource must meet
            the following requirements:

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

            See `Google Cloud
            Document <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`__
            for more details.
        safety_settings (MutableSequence[google.cloud.retail_v2.types.SafetySetting]):
            Optional. The safety settings to be applied
            to the generated content.
    """

    class SearchParams(proto.Message):
        r"""Search parameters.

        Attributes:
            filter (str):
                Optional. The filter string to restrict search results.

                The syntax of the filter string is the same as
                [SearchRequest.filter][google.cloud.retail.v2.SearchRequest.filter].
            canonical_filter (str):
                Optional. The canonical filter string to restrict search
                results.

                The syntax of the canonical filter string is the same as
                [SearchRequest.canonical_filter][google.cloud.retail.v2.SearchRequest.canonical_filter].
            sort_by (str):
                Optional. The sort string to specify the sorting of search
                results.

                The syntax of the sort string is the same as
                [SearchRequest.sort][].
            boost_spec (google.cloud.retail_v2.types.SearchRequest.BoostSpec):
                Optional. The boost spec to specify the boosting of search
                results.

                The syntax of the boost spec is the same as
                [SearchRequest.boost_spec][google.cloud.retail.v2.SearchRequest.boost_spec].
        """

        filter: str = proto.Field(
            proto.STRING,
            number=1,
        )
        canonical_filter: str = proto.Field(
            proto.STRING,
            number=2,
        )
        sort_by: str = proto.Field(
            proto.STRING,
            number=3,
        )
        boost_spec: search_service.SearchRequest.BoostSpec = proto.Field(
            proto.MESSAGE,
            number=4,
            message=search_service.SearchRequest.BoostSpec,
        )

    class UserAnswer(proto.Message):
        r"""This field specifies the current user answer during the
        conversational filtering search. This can be either user
        selected from suggested answers or user input plain text.

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
            selected_answer (google.cloud.retail_v2.types.ConversationalSearchRequest.UserAnswer.SelectedAnswer):
                Optional. This field specifies the selected answer during
                the conversational search. This should be a subset of
                [ConversationalSearchResponse.followup_question.suggested_answers][].

                This field is a member of `oneof`_ ``type``.
        """

        class SelectedAnswer(proto.Message):
            r"""This field specifies the selected answers during the
            conversational search.

            Attributes:
                product_attribute_value (google.cloud.retail_v2.types.ProductAttributeValue):
                    Optional. This field specifies the selected
                    answer which is a attribute key-value.
            """

            product_attribute_value: search_service.ProductAttributeValue = proto.Field(
                proto.MESSAGE,
                number=1,
                message=search_service.ProductAttributeValue,
            )

        text_answer: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="type",
        )
        selected_answer: "ConversationalSearchRequest.UserAnswer.SelectedAnswer" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="type",
                message="ConversationalSearchRequest.UserAnswer.SelectedAnswer",
            )
        )

    class ConversationalFilteringSpec(proto.Message):
        r"""This field specifies all conversational filtering related
        parameters addition to conversational retail search.

        Attributes:
            enable_conversational_filtering (bool):
                Optional. This field is deprecated. Please use
                [ConversationalFilteringSpec.conversational_filtering_mode][google.cloud.retail.v2.ConversationalSearchRequest.ConversationalFilteringSpec.conversational_filtering_mode]
                instead.
            user_answer (google.cloud.retail_v2.types.ConversationalSearchRequest.UserAnswer):
                Optional. This field specifies the current
                user answer during the conversational filtering
                search. It can be either user selected from
                suggested answers or user input plain text.
            conversational_filtering_mode (google.cloud.retail_v2.types.ConversationalSearchRequest.ConversationalFilteringSpec.Mode):
                Optional. Mode to control Conversational Filtering. Defaults
                to
                [Mode.DISABLED][google.cloud.retail.v2.ConversationalSearchRequest.ConversationalFilteringSpec.Mode.DISABLED]
                if it's unset.
        """

        class Mode(proto.Enum):
            r"""Enum to control Conversational Filtering mode.
            A single conversation session including multiple turns supports
            modes for Conversational Search OR Conversational Filtering
            without Conversational Search, but not both.

            Values:
                MODE_UNSPECIFIED (0):
                    Default value.
                DISABLED (1):
                    Disables Conversational Filtering when using
                    Conversational Search.
                ENABLED (2):
                    Enables Conversational Filtering when using
                    Conversational Search.
                CONVERSATIONAL_FILTER_ONLY (3):
                    Enables Conversational Filtering without
                    Conversational Search.
            """

            MODE_UNSPECIFIED = 0
            DISABLED = 1
            ENABLED = 2
            CONVERSATIONAL_FILTER_ONLY = 3

        enable_conversational_filtering: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        user_answer: "ConversationalSearchRequest.UserAnswer" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ConversationalSearchRequest.UserAnswer",
        )
        conversational_filtering_mode: "ConversationalSearchRequest.ConversationalFilteringSpec.Mode" = proto.Field(
            proto.ENUM,
            number=4,
            enum="ConversationalSearchRequest.ConversationalFilteringSpec.Mode",
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
    page_categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    conversation_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    search_params: SearchParams = proto.Field(
        proto.MESSAGE,
        number=6,
        message=SearchParams,
    )
    visitor_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    user_info: common.UserInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        message=common.UserInfo,
    )
    conversational_filtering_spec: ConversationalFilteringSpec = proto.Field(
        proto.MESSAGE,
        number=8,
        message=ConversationalFilteringSpec,
    )
    user_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    safety_settings: MutableSequence[safety.SafetySetting] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=safety.SafetySetting,
    )


class ConversationalSearchResponse(proto.Message):
    r"""Response message for
    [ConversationalSearchService.ConversationalSearch][google.cloud.retail.v2.ConversationalSearchService.ConversationalSearch]
    method.

    Attributes:
        user_query_types (MutableSequence[str]):
            The types Retail classifies the search query as.

            Supported values are:

            - "ORDER_SUPPORT"
            - "SIMPLE_PRODUCT_SEARCH"
            - "INTENT_REFINEMENT"
            - "PRODUCT_DETAILS"
            - "PRODUCT_COMPARISON"
            - "DEALS_AND_COUPONS"
            - "STORE_RELEVANT"
            - "BLOCKLISTED"
            - "BEST_PRODUCT"
            - "RETAIL_SUPPORT"
            - "DISABLED".
        conversational_text_response (str):
            The conversational answer-based text response
            generated by the Server.
        followup_question (google.cloud.retail_v2.types.ConversationalSearchResponse.FollowupQuestion):
            The conversational followup question
            generated for Intent refinement.
        conversation_id (str):
            Conversation UUID. This field will be stored in client side
            storage to maintain the conversation session with server and
            will be used for next search request's
            [ConversationalSearchRequest.conversation_id][google.cloud.retail.v2.ConversationalSearchRequest.conversation_id]
            to restore conversation state in server.
        refined_search (MutableSequence[google.cloud.retail_v2.types.ConversationalSearchResponse.RefinedSearch]):
            The proposed refined search queries. They can be used to
            fetch the relevant search results. When using
            CONVERSATIONAL_FILTER_ONLY mode, the refined_query from
            search response will be populated here.
        conversational_filtering_result (google.cloud.retail_v2.types.ConversationalSearchResponse.ConversationalFilteringResult):
            This field specifies all related information
            that is needed on client side for UI rendering
            of conversational filtering search.
        state (google.cloud.retail_v2.types.ConversationalSearchResponse.State):
            Output only. The state of the response
            generation.
    """

    class State(proto.Enum):
        r"""The state of the response generation.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown.
            STREAMING (1):
                Response generation is being streamed.
            SUCCEEDED (2):
                Response generation has succeeded.
        """

        STATE_UNSPECIFIED = 0
        STREAMING = 1
        SUCCEEDED = 2

    class FollowupQuestion(proto.Message):
        r"""The conversational followup question generated for Intent
        refinement.

        Attributes:
            followup_question (str):
                The conversational followup question
                generated for Intent refinement.
            suggested_answers (MutableSequence[google.cloud.retail_v2.types.ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer]):
                The answer options provided to client for the
                follow-up question.
        """

        class SuggestedAnswer(proto.Message):
            r"""Suggested answers to the follow-up question.
            If it's numerical attribute, only ProductAttributeInterval will
            be set. If it's textual attribute, only productAttributeValue
            will be set.

            Attributes:
                product_attribute_value (google.cloud.retail_v2.types.ProductAttributeValue):
                    Product attribute value, including an
                    attribute key and an attribute value. Other
                    types can be added here in the future.
            """

            product_attribute_value: search_service.ProductAttributeValue = proto.Field(
                proto.MESSAGE,
                number=1,
                message=search_service.ProductAttributeValue,
            )

        followup_question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        suggested_answers: MutableSequence[
            "ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer",
        )

    class RefinedSearch(proto.Message):
        r"""The proposed refined search for intent-refinement/bundled shopping
        conversation. When using CONVERSATIONAL_FILTER_ONLY mode, the
        refined_query from search response will be populated here.

        Attributes:
            query (str):
                The query to be used for search.
        """

        query: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ConversationalFilteringResult(proto.Message):
        r"""This field specifies all related information that is needed
        on client side for UI rendering of conversational filtering
        search.

        Attributes:
            followup_question (google.cloud.retail_v2.types.ConversationalSearchResponse.FollowupQuestion):
                The conversational filtering question.
            additional_filter (google.cloud.retail_v2.types.ConversationalSearchResponse.ConversationalFilteringResult.AdditionalFilter):
                This is the incremental additional filters implied from the
                current user answer. User should add the suggested addition
                filters to the previous
                [ConversationalSearchRequest.search_params.filter][] and
                [SearchRequest.filter][google.cloud.retail.v2.SearchRequest.filter],
                and use the merged filter in the follow up requests.
        """

        class AdditionalFilter(proto.Message):
            r"""Additional filter that client side need to apply.

            Attributes:
                product_attribute_value (google.cloud.retail_v2.types.ProductAttributeValue):
                    Product attribute value, including an
                    attribute key and an attribute value. Other
                    types can be added here in the future.
            """

            product_attribute_value: search_service.ProductAttributeValue = proto.Field(
                proto.MESSAGE,
                number=1,
                message=search_service.ProductAttributeValue,
            )

        followup_question: "ConversationalSearchResponse.FollowupQuestion" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                message="ConversationalSearchResponse.FollowupQuestion",
            )
        )
        additional_filter: "ConversationalSearchResponse.ConversationalFilteringResult.AdditionalFilter" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ConversationalSearchResponse.ConversationalFilteringResult.AdditionalFilter",
        )

    user_query_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    conversational_text_response: str = proto.Field(
        proto.STRING,
        number=2,
    )
    followup_question: FollowupQuestion = proto.Field(
        proto.MESSAGE,
        number=3,
        message=FollowupQuestion,
    )
    conversation_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    refined_search: MutableSequence[RefinedSearch] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=RefinedSearch,
    )
    conversational_filtering_result: ConversationalFilteringResult = proto.Field(
        proto.MESSAGE,
        number=7,
        message=ConversationalFilteringResult,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
