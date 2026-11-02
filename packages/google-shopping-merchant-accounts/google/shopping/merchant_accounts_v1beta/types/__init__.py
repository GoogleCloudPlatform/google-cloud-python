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
from .accessright import (
    AccessRight,
)
from .account_tax import (
    AccountTax,
    GetAccountTaxRequest,
    ListAccountTaxRequest,
    ListAccountTaxResponse,
    UpdateAccountTaxRequest,
)
from .accountissue import (
    AccountIssue,
    ListAccountIssuesRequest,
    ListAccountIssuesResponse,
)
from .accounts import (
    Account,
    CreateAndConfigureAccountRequest,
    DeleteAccountRequest,
    GetAccountRequest,
    ListAccountsRequest,
    ListAccountsResponse,
    ListSubAccountsRequest,
    ListSubAccountsResponse,
    UpdateAccountRequest,
)
from .accountservices import (
    AccountAggregation,
)
from .autofeedsettings import (
    AutofeedSettings,
    GetAutofeedSettingsRequest,
    UpdateAutofeedSettingsRequest,
)
from .automaticimprovements import (
    AutomaticImageImprovements,
    AutomaticImprovements,
    AutomaticItemUpdates,
    AutomaticShippingImprovements,
    GetAutomaticImprovementsRequest,
    UpdateAutomaticImprovementsRequest,
)
from .businessidentity import (
    BusinessIdentity,
    GetBusinessIdentityRequest,
    UpdateBusinessIdentityRequest,
)
from .businessinfo import (
    BusinessInfo,
    GetBusinessInfoRequest,
    UpdateBusinessInfoRequest,
)
from .checkoutsettings import (
    CheckoutSettings,
    CreateCheckoutSettingsRequest,
    DeleteCheckoutSettingsRequest,
    GetCheckoutSettingsRequest,
    UpdateCheckoutSettingsRequest,
    UriSettings,
)
from .customerservice import (
    CustomerService,
)
from .emailpreferences import (
    EmailPreferences,
    GetEmailPreferencesRequest,
    UpdateEmailPreferencesRequest,
)
from .gbpaccounts import (
    GbpAccount,
    LinkGbpAccountRequest,
    LinkGbpAccountResponse,
    ListGbpAccountsRequest,
    ListGbpAccountsResponse,
)
from .homepage import (
    ClaimHomepageRequest,
    GetHomepageRequest,
    Homepage,
    UnclaimHomepageRequest,
    UpdateHomepageRequest,
)
from .lfpproviders import (
    FindLfpProvidersRequest,
    FindLfpProvidersResponse,
    LfpProvider,
    LinkLfpProviderRequest,
    LinkLfpProviderResponse,
)
from .omnichannelsettings import (
    About,
    CreateOmnichannelSettingRequest,
    GetOmnichannelSettingRequest,
    InStock,
    InventoryVerification,
    LfpLink,
    ListOmnichannelSettingsRequest,
    ListOmnichannelSettingsResponse,
    OmnichannelSetting,
    OnDisplayToOrder,
    Pickup,
    RequestInventoryVerificationRequest,
    RequestInventoryVerificationResponse,
    ReviewState,
    UpdateOmnichannelSettingRequest,
)
from .online_return_policy import (
    CreateOnlineReturnPolicyRequest,
    DeleteOnlineReturnPolicyRequest,
    GetOnlineReturnPolicyRequest,
    ListOnlineReturnPoliciesRequest,
    ListOnlineReturnPoliciesResponse,
    OnlineReturnPolicy,
    UpdateOnlineReturnPolicyRequest,
)
from .phoneverificationstate import (
    PhoneVerificationState,
)
from .programs import (
    DisableProgramRequest,
    EnableProgramRequest,
    GetProgramRequest,
    ListProgramsRequest,
    ListProgramsResponse,
    Program,
)
from .regions import (
    CreateRegionRequest,
    DeleteRegionRequest,
    GetRegionRequest,
    ListRegionsRequest,
    ListRegionsResponse,
    Region,
    UpdateRegionRequest,
)
from .shippingsettings import (
    Address,
    BusinessDayConfig,
    CarrierRate,
    CutoffTime,
    DeliveryTime,
    Distance,
    GetShippingSettingsRequest,
    Headers,
    InsertShippingSettingsRequest,
    LocationIdSet,
    MinimumOrderValueTable,
    RateGroup,
    Row,
    Service,
    ShippingSettings,
    Table,
    TransitTable,
    Value,
    Warehouse,
    WarehouseBasedDeliveryTime,
    WarehouseCutoffTime,
)
from .tax_rule import (
    TaxRule,
)
from .termsofservice import (
    AcceptTermsOfServiceRequest,
    GetTermsOfServiceRequest,
    RetrieveLatestTermsOfServiceRequest,
    TermsOfService,
)
from .termsofserviceagreementstate import (
    Accepted,
    GetTermsOfServiceAgreementStateRequest,
    Required,
    RetrieveForApplicationTermsOfServiceAgreementStateRequest,
    TermsOfServiceAgreementState,
)
from .termsofservicekind import (
    TermsOfServiceKind,
)
from .user import (
    CreateUserRequest,
    DeleteUserRequest,
    GetUserRequest,
    ListUsersRequest,
    ListUsersResponse,
    UpdateUserRequest,
    User,
)
from .verificationmailsettings import (
    VerificationMailSettings,
)

__all__ = (
    "AccessRight",
    "AccountTax",
    "GetAccountTaxRequest",
    "ListAccountTaxRequest",
    "ListAccountTaxResponse",
    "UpdateAccountTaxRequest",
    "AccountIssue",
    "ListAccountIssuesRequest",
    "ListAccountIssuesResponse",
    "Account",
    "CreateAndConfigureAccountRequest",
    "DeleteAccountRequest",
    "GetAccountRequest",
    "ListAccountsRequest",
    "ListAccountsResponse",
    "ListSubAccountsRequest",
    "ListSubAccountsResponse",
    "UpdateAccountRequest",
    "AccountAggregation",
    "AutofeedSettings",
    "GetAutofeedSettingsRequest",
    "UpdateAutofeedSettingsRequest",
    "AutomaticImageImprovements",
    "AutomaticImprovements",
    "AutomaticItemUpdates",
    "AutomaticShippingImprovements",
    "GetAutomaticImprovementsRequest",
    "UpdateAutomaticImprovementsRequest",
    "BusinessIdentity",
    "GetBusinessIdentityRequest",
    "UpdateBusinessIdentityRequest",
    "BusinessInfo",
    "GetBusinessInfoRequest",
    "UpdateBusinessInfoRequest",
    "CheckoutSettings",
    "CreateCheckoutSettingsRequest",
    "DeleteCheckoutSettingsRequest",
    "GetCheckoutSettingsRequest",
    "UpdateCheckoutSettingsRequest",
    "UriSettings",
    "CustomerService",
    "EmailPreferences",
    "GetEmailPreferencesRequest",
    "UpdateEmailPreferencesRequest",
    "GbpAccount",
    "LinkGbpAccountRequest",
    "LinkGbpAccountResponse",
    "ListGbpAccountsRequest",
    "ListGbpAccountsResponse",
    "ClaimHomepageRequest",
    "GetHomepageRequest",
    "Homepage",
    "UnclaimHomepageRequest",
    "UpdateHomepageRequest",
    "FindLfpProvidersRequest",
    "FindLfpProvidersResponse",
    "LfpProvider",
    "LinkLfpProviderRequest",
    "LinkLfpProviderResponse",
    "About",
    "CreateOmnichannelSettingRequest",
    "GetOmnichannelSettingRequest",
    "InStock",
    "InventoryVerification",
    "LfpLink",
    "ListOmnichannelSettingsRequest",
    "ListOmnichannelSettingsResponse",
    "OmnichannelSetting",
    "OnDisplayToOrder",
    "Pickup",
    "RequestInventoryVerificationRequest",
    "RequestInventoryVerificationResponse",
    "ReviewState",
    "UpdateOmnichannelSettingRequest",
    "CreateOnlineReturnPolicyRequest",
    "DeleteOnlineReturnPolicyRequest",
    "GetOnlineReturnPolicyRequest",
    "ListOnlineReturnPoliciesRequest",
    "ListOnlineReturnPoliciesResponse",
    "OnlineReturnPolicy",
    "UpdateOnlineReturnPolicyRequest",
    "PhoneVerificationState",
    "DisableProgramRequest",
    "EnableProgramRequest",
    "GetProgramRequest",
    "ListProgramsRequest",
    "ListProgramsResponse",
    "Program",
    "CreateRegionRequest",
    "DeleteRegionRequest",
    "GetRegionRequest",
    "ListRegionsRequest",
    "ListRegionsResponse",
    "Region",
    "UpdateRegionRequest",
    "Address",
    "BusinessDayConfig",
    "CarrierRate",
    "CutoffTime",
    "DeliveryTime",
    "Distance",
    "GetShippingSettingsRequest",
    "Headers",
    "InsertShippingSettingsRequest",
    "LocationIdSet",
    "MinimumOrderValueTable",
    "RateGroup",
    "Row",
    "Service",
    "ShippingSettings",
    "Table",
    "TransitTable",
    "Value",
    "Warehouse",
    "WarehouseBasedDeliveryTime",
    "WarehouseCutoffTime",
    "TaxRule",
    "AcceptTermsOfServiceRequest",
    "GetTermsOfServiceRequest",
    "RetrieveLatestTermsOfServiceRequest",
    "TermsOfService",
    "Accepted",
    "GetTermsOfServiceAgreementStateRequest",
    "Required",
    "RetrieveForApplicationTermsOfServiceAgreementStateRequest",
    "TermsOfServiceAgreementState",
    "TermsOfServiceKind",
    "CreateUserRequest",
    "DeleteUserRequest",
    "GetUserRequest",
    "ListUsersRequest",
    "ListUsersResponse",
    "UpdateUserRequest",
    "User",
    "VerificationMailSettings",
)
