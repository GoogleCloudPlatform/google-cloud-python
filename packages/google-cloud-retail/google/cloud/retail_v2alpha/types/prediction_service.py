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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2alpha.types import user_event as gcr_user_event

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "PredictRequest",
        "PredictResponse",
    },
)


class PredictRequest(proto.Message):
    r"""Request message for Predict method.

    Attributes:
        placement (str):
            Required. Full resource name of the format:
            ``{placement=projects/*/locations/global/catalogs/default_catalog/servingConfigs/*}``
            or
            ``{placement=projects/*/locations/global/catalogs/default_catalog/placements/*}``.
            We recommend using the ``servingConfigs`` resource.
            ``placements`` is a legacy resource. The ID of the
            Recommendations AI serving config or placement. Before you
            can request predictions from your model, you must create at
            least one serving config or placement for it. For more
            information, see [Manage serving configs]
            (https://cloud.google.com/retail/docs/manage-configs).

            The full list of available serving configs can be seen at
            https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs
        user_event (google.cloud.retail_v2alpha.types.UserEvent):
            Required. Context about the user, what they are looking at
            and what action they took to trigger the predict request.
            Note that this user event detail won't be ingested to
            userEvent logs. Thus, a separate userEvent write request is
            required for event logging.

            Don't set
            [UserEvent.visitor_id][google.cloud.retail.v2alpha.UserEvent.visitor_id]
            or
            [UserInfo.user_id][google.cloud.retail.v2alpha.UserInfo.user_id]
            to the same fixed ID for different users. If you are trying
            to receive non-personalized recommendations (not
            recommended; this can negatively impact model performance),
            instead set
            [UserEvent.visitor_id][google.cloud.retail.v2alpha.UserEvent.visitor_id]
            to a random unique ID and leave
            [UserInfo.user_id][google.cloud.retail.v2alpha.UserInfo.user_id]
            unset.
        page_size (int):
            Maximum number of results to return. Set this
            property to the number of prediction results
            needed. If zero, the service will choose a
            reasonable default. The maximum allowed value is
            100. Values above 100 will be coerced to 100.
        page_token (str):
            This field is not used; leave it unset.
        filter (str):
            Filter for restricting prediction results with a length
            limit of 5,000 characters. Accepts values for tags and the
            ``filterOutOfStockItems`` flag.

            - Tag expressions. Restricts predictions to products that
              match all of the specified tags. Boolean operators ``OR``
              and ``NOT`` are supported if the expression is enclosed in
              parentheses, and must be separated from the tag values by
              a space. ``-"tagA"`` is also supported and is equivalent
              to ``NOT "tagA"``. Tag values must be double quoted UTF-8
              encoded strings with a size limit of 1,000 characters.

              Note: "Recently viewed" models don't support tag filtering
              at the moment.

            - filterOutOfStockItems. Restricts predictions to products
              that do not have a stockState value of OUT_OF_STOCK.

            Examples:

            - tag=("Red" OR "Blue") tag="New-Arrival" tag=(NOT
              "promotional")
            - filterOutOfStockItems tag=(-"promotional")
            - filterOutOfStockItems

            If your filter blocks all prediction results, the API will
            return *no* results. If instead you want empty result sets
            to return generic (unfiltered) popular products, set
            ``strictFiltering`` to False in ``PredictRequest.params``.
            Note that the API will never return items with storageStatus
            of "EXPIRED" or "DELETED" regardless of filter choices.

            If ``filterSyntaxV2`` is set to true under the ``params``
            field, then attribute-based expressions are expected instead
            of the above described tag-based syntax. Examples:

            - (colors: ANY("Red", "Blue")) AND NOT (categories:
              ANY("Phones"))
            - (availability: ANY("IN_STOCK")) AND (colors: ANY("Red") OR
              categories: ANY("Phones"))

            For more information, see `Filter
            recommendations <https://cloud.google.com/retail/docs/filter-recs>`__.
        validate_only (bool):
            Use validate only mode for this prediction
            query. If set to true, a dummy model will be
            used that returns arbitrary products. Note that
            the validate only mode should only be used for
            testing the API, or if the model is not ready.
        params (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Additional domain specific parameters for the predictions.

            Allowed values:

            - ``returnProduct``: Boolean. If set to true, the associated
              product object will be returned in the
              ``results.metadata`` field in the prediction response.
            - ``returnScore``: Boolean. If set to true, the prediction
              'score' corresponding to each returned product will be set
              in the ``results.metadata`` field in the prediction
              response. The given 'score' indicates the probability of a
              product being clicked/purchased given the user's context
              and history.
            - ``strictFiltering``: Boolean. True by default. If set to
              false, the service will return generic (unfiltered)
              popular products instead of empty if your filter blocks
              all prediction results.
            - ``priceRerankLevel``: String. Default empty. If set to be
              non-empty, then it needs to be one of
              {'no-price-reranking', 'low-price-reranking',
              'medium-price-reranking', 'high-price-reranking'}. This
              gives request-level control and adjusts prediction results
              based on product price.
            - ``diversityLevel``: String. Default empty. If set to be
              non-empty, then it needs to be one of {'no-diversity',
              'low-diversity', 'medium-diversity', 'high-diversity',
              'auto-diversity'}. This gives request-level control and
              adjusts prediction results based on product category.
            - ``filterSyntaxV2``: Boolean. False by default. If set to
              true, the ``filter`` field is interpreteted according to
              the new, attribute-based syntax.
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

            See `Google Cloud
            Document <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`__
            for more details.
    """

    placement: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_event: gcr_user_event.UserEvent = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcr_user_event.UserEvent,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    params: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Value,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


class PredictResponse(proto.Message):
    r"""Response message for predict method.

    Attributes:
        results (MutableSequence[google.cloud.retail_v2alpha.types.PredictResponse.PredictionResult]):
            A list of recommended products. The order
            represents the ranking (from the most relevant
            product to the least).
        attribution_token (str):
            A unique attribution token. This should be included in the
            [UserEvent][google.cloud.retail.v2alpha.UserEvent] logs
            resulting from this recommendation, which enables accurate
            attribution of recommendation model performance.
        missing_ids (MutableSequence[str]):
            IDs of products in the request that were
            missing from the inventory.
        validate_only (bool):
            True if the validateOnly property was set in
            the request.
    """

    class PredictionResult(proto.Message):
        r"""PredictionResult represents the recommendation prediction
        results.

        Attributes:
            id (str):
                ID of the recommended product
            metadata (MutableMapping[str, google.protobuf.struct_pb2.Value]):
                Additional product metadata / annotations.

                Possible values:

                - ``product``: JSON representation of the product. Is set if
                  ``returnProduct`` is set to true in
                  ``PredictRequest.params``.
                - ``score``: Prediction score in double value. Is set if
                  ``returnScore`` is set to true in
                  ``PredictRequest.params``.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        metadata: MutableMapping[str, struct_pb2.Value] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Value,
        )

    results: MutableSequence[PredictionResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=PredictionResult,
    )
    attribution_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    missing_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
