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
# Snippet for CreateOrderTrackingSignal
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-shopping-merchant-ordertracking


# [START merchantapi_v1beta_generated_OrderTrackingSignalsService_CreateOrderTrackingSignal_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.shopping import merchant_ordertracking_v1beta


def sample_create_order_tracking_signal():
    # Create a client
    client = merchant_ordertracking_v1beta.OrderTrackingSignalsServiceClient()

    # Initialize request argument(s)
    order_tracking_signal = merchant_ordertracking_v1beta.OrderTrackingSignal()
    order_tracking_signal.order_id = "order_id_value"
    order_tracking_signal.shipping_info.shipment_id = "shipment_id_value"
    order_tracking_signal.shipping_info.shipping_status = "DELIVERED"
    order_tracking_signal.shipping_info.origin_postal_code = "origin_postal_code_value"
    order_tracking_signal.shipping_info.origin_region_code = "origin_region_code_value"
    order_tracking_signal.line_items.line_item_id = "line_item_id_value"
    order_tracking_signal.line_items.product_id = "product_id_value"
    order_tracking_signal.line_items.quantity = 895

    request = merchant_ordertracking_v1beta.CreateOrderTrackingSignalRequest(
        parent="parent_value",
        order_tracking_signal=order_tracking_signal,
    )

    # Make the request
    response = client.create_order_tracking_signal(request=request)

    # Handle the response
    print(response)


# [END merchantapi_v1beta_generated_OrderTrackingSignalsService_CreateOrderTrackingSignal_sync]
