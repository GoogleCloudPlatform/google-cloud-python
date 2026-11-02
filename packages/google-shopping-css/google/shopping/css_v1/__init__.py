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

from google.shopping.css_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.css_v1.services.account_labels_service",
    "google.shopping.css_v1.services.accounts_service",
    "google.shopping.css_v1.services.css_product_inputs_service",
    "google.shopping.css_v1.services.css_products_service",
    "google.shopping.css_v1.services.quota_service",
    "google.shopping.css_v1.types.accounts",
    "google.shopping.css_v1.types.accounts_labels",
    "google.shopping.css_v1.types.css_product_common",
    "google.shopping.css_v1.types.css_product_inputs",
    "google.shopping.css_v1.types.css_products",
    "google.shopping.css_v1.types.quota",
}


from .services.account_labels_service import (
    AccountLabelsServiceAsyncClient,
    AccountLabelsServiceClient,
)
from .services.accounts_service import AccountsServiceAsyncClient, AccountsServiceClient
from .services.css_product_inputs_service import (
    CssProductInputsServiceAsyncClient,
    CssProductInputsServiceClient,
)
from .services.css_products_service import (
    CssProductsServiceAsyncClient,
    CssProductsServiceClient,
)
from .services.quota_service import QuotaServiceAsyncClient, QuotaServiceClient
from .types.accounts import (
    Account,
    GetAccountRequest,
    ListChildAccountsRequest,
    ListChildAccountsResponse,
    UpdateAccountLabelsRequest,
)
from .types.accounts_labels import (
    AccountLabel,
    CreateAccountLabelRequest,
    DeleteAccountLabelRequest,
    ListAccountLabelsRequest,
    ListAccountLabelsResponse,
    UpdateAccountLabelRequest,
)
from .types.css_product_common import (
    Attributes,
    Certification,
    CssProductStatus,
    HeadlineOfferInstallment,
    HeadlineOfferSubscriptionCost,
    ProductDetail,
    ProductDimension,
    ProductWeight,
    SubscriptionPeriod,
)
from .types.css_product_inputs import (
    CssProductInput,
    DeleteCssProductInputRequest,
    InsertCssProductInputRequest,
    UpdateCssProductInputRequest,
)
from .types.css_products import (
    CssProduct,
    GetCssProductRequest,
    ListCssProductsRequest,
    ListCssProductsResponse,
)
from .types.quota import (
    ListQuotaGroupsRequest,
    ListQuotaGroupsResponse,
    MethodDetails,
    QuotaGroup,
)

__all__ = (
    "AccountLabelsServiceAsyncClient",
    "AccountsServiceAsyncClient",
    "CssProductInputsServiceAsyncClient",
    "CssProductsServiceAsyncClient",
    "QuotaServiceAsyncClient",
    "Account",
    "AccountLabel",
    "AccountLabelsServiceClient",
    "AccountsServiceClient",
    "Attributes",
    "Certification",
    "CreateAccountLabelRequest",
    "CssProduct",
    "CssProductInput",
    "CssProductInputsServiceClient",
    "CssProductStatus",
    "CssProductsServiceClient",
    "DeleteAccountLabelRequest",
    "DeleteCssProductInputRequest",
    "GetAccountRequest",
    "GetCssProductRequest",
    "HeadlineOfferInstallment",
    "HeadlineOfferSubscriptionCost",
    "InsertCssProductInputRequest",
    "ListAccountLabelsRequest",
    "ListAccountLabelsResponse",
    "ListChildAccountsRequest",
    "ListChildAccountsResponse",
    "ListCssProductsRequest",
    "ListCssProductsResponse",
    "ListQuotaGroupsRequest",
    "ListQuotaGroupsResponse",
    "MethodDetails",
    "ProductDetail",
    "ProductDimension",
    "ProductWeight",
    "QuotaGroup",
    "QuotaServiceClient",
    "SubscriptionPeriod",
    "UpdateAccountLabelRequest",
    "UpdateAccountLabelsRequest",
    "UpdateCssProductInputRequest",
)

api_core.check_python_version("google.shopping.css_v1")
api_core.check_dependency_versions("google.shopping.css_v1")
