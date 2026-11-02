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
import google.api_core as api_core

from google.cloud.commerceproducer_v1beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.commerceproducer_v1beta.services.commerce_transaction",
    "google.cloud.commerceproducer_v1beta.types.commerce_transaction",
    "google.cloud.commerceproducer_v1beta.types.private_offer",
    "google.cloud.commerceproducer_v1beta.types.service",
    "google.cloud.commerceproducer_v1beta.types.sku",
    "google.cloud.commerceproducer_v1beta.types.sku_group",
    "google.cloud.commerceproducer_v1beta.types.standard_offer",
}


from .services.commerce_transaction import (
    CommerceTransactionAsyncClient,
    CommerceTransactionClient,
)
from .types.commerce_transaction import (
    CancelPrivateOfferRequest,
    CreatePrivateOfferDocumentRequest,
    CreatePrivateOfferRequest,
    DeletePrivateOfferDocumentRequest,
    DeletePrivateOfferRequest,
    GetPrivateOfferDocumentRequest,
    GetPrivateOfferRequest,
    GetServiceRequest,
    GetSkuGroupRequest,
    GetSkuRequest,
    GetStandardOfferRequest,
    ListPrivateOfferDocumentsRequest,
    ListPrivateOfferDocumentsResponse,
    ListPrivateOffersRequest,
    ListPrivateOffersResponse,
    ListServicesRequest,
    ListServicesResponse,
    ListSkuGroupsRequest,
    ListSkuGroupsResponse,
    ListSkusRequest,
    ListSkusResponse,
    ListStandardOffersRequest,
    ListStandardOffersResponse,
    PrivateOfferView,
    PublishPrivateOfferRequest,
    ResolveAmendmentTargetRequest,
    ResolveAmendmentTargetResponse,
    ServiceView,
    StandardOfferView,
    UpdatePrivateOfferDocumentRequest,
    UpdatePrivateOfferRequest,
)
from .types.private_offer import PrivateOffer, PrivateOfferDocument
from .types.service import Service
from .types.sku import Sku
from .types.sku_group import SkuGroup
from .types.standard_offer import StandardOffer

__all__ = (
    "CommerceTransactionAsyncClient",
    "CancelPrivateOfferRequest",
    "CommerceTransactionClient",
    "CreatePrivateOfferDocumentRequest",
    "CreatePrivateOfferRequest",
    "DeletePrivateOfferDocumentRequest",
    "DeletePrivateOfferRequest",
    "GetPrivateOfferDocumentRequest",
    "GetPrivateOfferRequest",
    "GetServiceRequest",
    "GetSkuGroupRequest",
    "GetSkuRequest",
    "GetStandardOfferRequest",
    "ListPrivateOfferDocumentsRequest",
    "ListPrivateOfferDocumentsResponse",
    "ListPrivateOffersRequest",
    "ListPrivateOffersResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "ListSkuGroupsRequest",
    "ListSkuGroupsResponse",
    "ListSkusRequest",
    "ListSkusResponse",
    "ListStandardOffersRequest",
    "ListStandardOffersResponse",
    "PrivateOffer",
    "PrivateOfferDocument",
    "PrivateOfferView",
    "PublishPrivateOfferRequest",
    "ResolveAmendmentTargetRequest",
    "ResolveAmendmentTargetResponse",
    "Service",
    "ServiceView",
    "Sku",
    "SkuGroup",
    "StandardOffer",
    "StandardOfferView",
    "UpdatePrivateOfferDocumentRequest",
    "UpdatePrivateOfferRequest",
)

api_core.check_python_version("google.cloud.commerceproducer_v1beta")
api_core.check_dependency_versions("google.cloud.commerceproducer_v1beta")
