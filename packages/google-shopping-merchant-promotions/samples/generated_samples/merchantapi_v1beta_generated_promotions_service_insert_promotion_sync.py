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
# Generated code. DO NOT EDIT!
#
# Snippet for InsertPromotion
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-shopping-merchant-promotions


# [START merchantapi_v1beta_generated_PromotionsService_InsertPromotion_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.shopping import merchant_promotions_v1beta


def sample_insert_promotion():
    # Create a client
    client = merchant_promotions_v1beta.PromotionsServiceClient()

    # Initialize request argument(s)
    promotion = merchant_promotions_v1beta.Promotion()
    promotion.promotion_id = "promotion_id_value"
    promotion.content_language = "content_language_value"
    promotion.target_country = "target_country_value"
    promotion.redemption_channel = ["ONLINE"]

    request = merchant_promotions_v1beta.InsertPromotionRequest(
        parent="parent_value",
        promotion=promotion,
        data_source="data_source_value",
    )

    # Make the request
    response = client.insert_promotion(request=request)

    # Handle the response
    print(response)


# [END merchantapi_v1beta_generated_PromotionsService_InsertPromotion_sync]
