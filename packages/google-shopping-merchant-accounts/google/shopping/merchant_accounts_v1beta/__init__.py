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

from google.shopping.merchant_accounts_v1beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.merchant_accounts_v1beta.services.account_issue_service",
    "google.shopping.merchant_accounts_v1beta.services.account_tax_service",
    "google.shopping.merchant_accounts_v1beta.services.accounts_service",
    "google.shopping.merchant_accounts_v1beta.services.autofeed_settings_service",
    "google.shopping.merchant_accounts_v1beta.services.automatic_improvements_service",
    "google.shopping.merchant_accounts_v1beta.services.business_identity_service",
    "google.shopping.merchant_accounts_v1beta.services.business_info_service",
    "google.shopping.merchant_accounts_v1beta.services.checkout_settings_service",
    "google.shopping.merchant_accounts_v1beta.services.email_preferences_service",
    "google.shopping.merchant_accounts_v1beta.services.gbp_accounts_service",
    "google.shopping.merchant_accounts_v1beta.services.homepage_service",
    "google.shopping.merchant_accounts_v1beta.services.lfp_providers_service",
    "google.shopping.merchant_accounts_v1beta.services.omnichannel_settings_service",
    "google.shopping.merchant_accounts_v1beta.services.online_return_policy_service",
    "google.shopping.merchant_accounts_v1beta.services.programs_service",
    "google.shopping.merchant_accounts_v1beta.services.regions_service",
    "google.shopping.merchant_accounts_v1beta.services.shipping_settings_service",
    "google.shopping.merchant_accounts_v1beta.services.terms_of_service_agreement_state_service",
    "google.shopping.merchant_accounts_v1beta.services.terms_of_service_service",
    "google.shopping.merchant_accounts_v1beta.services.user_service",
    "google.shopping.merchant_accounts_v1beta.types.accessright",
    "google.shopping.merchant_accounts_v1beta.types.account_tax",
    "google.shopping.merchant_accounts_v1beta.types.accountissue",
    "google.shopping.merchant_accounts_v1beta.types.accounts",
    "google.shopping.merchant_accounts_v1beta.types.accountservices",
    "google.shopping.merchant_accounts_v1beta.types.autofeedsettings",
    "google.shopping.merchant_accounts_v1beta.types.automaticimprovements",
    "google.shopping.merchant_accounts_v1beta.types.businessidentity",
    "google.shopping.merchant_accounts_v1beta.types.businessinfo",
    "google.shopping.merchant_accounts_v1beta.types.checkoutsettings",
    "google.shopping.merchant_accounts_v1beta.types.customerservice",
    "google.shopping.merchant_accounts_v1beta.types.emailpreferences",
    "google.shopping.merchant_accounts_v1beta.types.gbpaccounts",
    "google.shopping.merchant_accounts_v1beta.types.homepage",
    "google.shopping.merchant_accounts_v1beta.types.lfpproviders",
    "google.shopping.merchant_accounts_v1beta.types.omnichannelsettings",
    "google.shopping.merchant_accounts_v1beta.types.online_return_policy",
    "google.shopping.merchant_accounts_v1beta.types.phoneverificationstate",
    "google.shopping.merchant_accounts_v1beta.types.programs",
    "google.shopping.merchant_accounts_v1beta.types.regions",
    "google.shopping.merchant_accounts_v1beta.types.shippingsettings",
    "google.shopping.merchant_accounts_v1beta.types.tax_rule",
    "google.shopping.merchant_accounts_v1beta.types.termsofservice",
    "google.shopping.merchant_accounts_v1beta.types.termsofserviceagreementstate",
    "google.shopping.merchant_accounts_v1beta.types.termsofservicekind",
    "google.shopping.merchant_accounts_v1beta.types.user",
    "google.shopping.merchant_accounts_v1beta.types.verificationmailsettings",
}


from .services.account_issue_service import (
    AccountIssueServiceAsyncClient,
    AccountIssueServiceClient,
)
from .services.account_tax_service import (
    AccountTaxServiceAsyncClient,
    AccountTaxServiceClient,
)
from .services.accounts_service import AccountsServiceAsyncClient, AccountsServiceClient
from .services.autofeed_settings_service import (
    AutofeedSettingsServiceAsyncClient,
    AutofeedSettingsServiceClient,
)
from .services.automatic_improvements_service import (
    AutomaticImprovementsServiceAsyncClient,
    AutomaticImprovementsServiceClient,
)
from .services.business_identity_service import (
    BusinessIdentityServiceAsyncClient,
    BusinessIdentityServiceClient,
)
from .services.business_info_service import (
    BusinessInfoServiceAsyncClient,
    BusinessInfoServiceClient,
)
from .services.checkout_settings_service import (
    CheckoutSettingsServiceAsyncClient,
    CheckoutSettingsServiceClient,
)
from .services.email_preferences_service import (
    EmailPreferencesServiceAsyncClient,
    EmailPreferencesServiceClient,
)
from .services.gbp_accounts_service import (
    GbpAccountsServiceAsyncClient,
    GbpAccountsServiceClient,
)
from .services.homepage_service import HomepageServiceAsyncClient, HomepageServiceClient
from .services.lfp_providers_service import (
    LfpProvidersServiceAsyncClient,
    LfpProvidersServiceClient,
)
from .services.omnichannel_settings_service import (
    OmnichannelSettingsServiceAsyncClient,
    OmnichannelSettingsServiceClient,
)
from .services.online_return_policy_service import (
    OnlineReturnPolicyServiceAsyncClient,
    OnlineReturnPolicyServiceClient,
)
from .services.programs_service import ProgramsServiceAsyncClient, ProgramsServiceClient
from .services.regions_service import RegionsServiceAsyncClient, RegionsServiceClient
from .services.shipping_settings_service import (
    ShippingSettingsServiceAsyncClient,
    ShippingSettingsServiceClient,
)
from .services.terms_of_service_agreement_state_service import (
    TermsOfServiceAgreementStateServiceAsyncClient,
    TermsOfServiceAgreementStateServiceClient,
)
from .services.terms_of_service_service import (
    TermsOfServiceServiceAsyncClient,
    TermsOfServiceServiceClient,
)
from .services.user_service import UserServiceAsyncClient, UserServiceClient
from .types.accessright import AccessRight
from .types.account_tax import (
    AccountTax,
    GetAccountTaxRequest,
    ListAccountTaxRequest,
    ListAccountTaxResponse,
    UpdateAccountTaxRequest,
)
from .types.accountissue import (
    AccountIssue,
    ListAccountIssuesRequest,
    ListAccountIssuesResponse,
)
from .types.accounts import (
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
from .types.accountservices import AccountAggregation
from .types.autofeedsettings import (
    AutofeedSettings,
    GetAutofeedSettingsRequest,
    UpdateAutofeedSettingsRequest,
)
from .types.automaticimprovements import (
    AutomaticImageImprovements,
    AutomaticImprovements,
    AutomaticItemUpdates,
    AutomaticShippingImprovements,
    GetAutomaticImprovementsRequest,
    UpdateAutomaticImprovementsRequest,
)
from .types.businessidentity import (
    BusinessIdentity,
    GetBusinessIdentityRequest,
    UpdateBusinessIdentityRequest,
)
from .types.businessinfo import (
    BusinessInfo,
    GetBusinessInfoRequest,
    UpdateBusinessInfoRequest,
)
from .types.checkoutsettings import (
    CheckoutSettings,
    CreateCheckoutSettingsRequest,
    DeleteCheckoutSettingsRequest,
    GetCheckoutSettingsRequest,
    UpdateCheckoutSettingsRequest,
    UriSettings,
)
from .types.customerservice import CustomerService
from .types.emailpreferences import (
    EmailPreferences,
    GetEmailPreferencesRequest,
    UpdateEmailPreferencesRequest,
)
from .types.gbpaccounts import (
    GbpAccount,
    LinkGbpAccountRequest,
    LinkGbpAccountResponse,
    ListGbpAccountsRequest,
    ListGbpAccountsResponse,
)
from .types.homepage import (
    ClaimHomepageRequest,
    GetHomepageRequest,
    Homepage,
    UnclaimHomepageRequest,
    UpdateHomepageRequest,
)
from .types.lfpproviders import (
    FindLfpProvidersRequest,
    FindLfpProvidersResponse,
    LfpProvider,
    LinkLfpProviderRequest,
    LinkLfpProviderResponse,
)
from .types.omnichannelsettings import (
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
from .types.online_return_policy import (
    CreateOnlineReturnPolicyRequest,
    DeleteOnlineReturnPolicyRequest,
    GetOnlineReturnPolicyRequest,
    ListOnlineReturnPoliciesRequest,
    ListOnlineReturnPoliciesResponse,
    OnlineReturnPolicy,
    UpdateOnlineReturnPolicyRequest,
)
from .types.phoneverificationstate import PhoneVerificationState
from .types.programs import (
    DisableProgramRequest,
    EnableProgramRequest,
    GetProgramRequest,
    ListProgramsRequest,
    ListProgramsResponse,
    Program,
)
from .types.regions import (
    CreateRegionRequest,
    DeleteRegionRequest,
    GetRegionRequest,
    ListRegionsRequest,
    ListRegionsResponse,
    Region,
    UpdateRegionRequest,
)
from .types.shippingsettings import (
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
from .types.tax_rule import TaxRule
from .types.termsofservice import (
    AcceptTermsOfServiceRequest,
    GetTermsOfServiceRequest,
    RetrieveLatestTermsOfServiceRequest,
    TermsOfService,
)
from .types.termsofserviceagreementstate import (
    Accepted,
    GetTermsOfServiceAgreementStateRequest,
    Required,
    RetrieveForApplicationTermsOfServiceAgreementStateRequest,
    TermsOfServiceAgreementState,
)
from .types.termsofservicekind import TermsOfServiceKind
from .types.user import (
    CreateUserRequest,
    DeleteUserRequest,
    GetUserRequest,
    ListUsersRequest,
    ListUsersResponse,
    UpdateUserRequest,
    User,
)
from .types.verificationmailsettings import VerificationMailSettings

__all__ = (
    "AccountIssueServiceAsyncClient",
    "AccountTaxServiceAsyncClient",
    "AccountsServiceAsyncClient",
    "AutofeedSettingsServiceAsyncClient",
    "AutomaticImprovementsServiceAsyncClient",
    "BusinessIdentityServiceAsyncClient",
    "BusinessInfoServiceAsyncClient",
    "CheckoutSettingsServiceAsyncClient",
    "EmailPreferencesServiceAsyncClient",
    "GbpAccountsServiceAsyncClient",
    "HomepageServiceAsyncClient",
    "LfpProvidersServiceAsyncClient",
    "OmnichannelSettingsServiceAsyncClient",
    "OnlineReturnPolicyServiceAsyncClient",
    "ProgramsServiceAsyncClient",
    "RegionsServiceAsyncClient",
    "ShippingSettingsServiceAsyncClient",
    "TermsOfServiceAgreementStateServiceAsyncClient",
    "TermsOfServiceServiceAsyncClient",
    "UserServiceAsyncClient",
    "About",
    "AcceptTermsOfServiceRequest",
    "Accepted",
    "AccessRight",
    "Account",
    "AccountAggregation",
    "AccountIssue",
    "AccountIssueServiceClient",
    "AccountTax",
    "AccountTaxServiceClient",
    "AccountsServiceClient",
    "Address",
    "AutofeedSettings",
    "AutofeedSettingsServiceClient",
    "AutomaticImageImprovements",
    "AutomaticImprovements",
    "AutomaticImprovementsServiceClient",
    "AutomaticItemUpdates",
    "AutomaticShippingImprovements",
    "BusinessDayConfig",
    "BusinessIdentity",
    "BusinessIdentityServiceClient",
    "BusinessInfo",
    "BusinessInfoServiceClient",
    "CarrierRate",
    "CheckoutSettings",
    "CheckoutSettingsServiceClient",
    "ClaimHomepageRequest",
    "CreateAndConfigureAccountRequest",
    "CreateCheckoutSettingsRequest",
    "CreateOmnichannelSettingRequest",
    "CreateOnlineReturnPolicyRequest",
    "CreateRegionRequest",
    "CreateUserRequest",
    "CustomerService",
    "CutoffTime",
    "DeleteAccountRequest",
    "DeleteCheckoutSettingsRequest",
    "DeleteOnlineReturnPolicyRequest",
    "DeleteRegionRequest",
    "DeleteUserRequest",
    "DeliveryTime",
    "DisableProgramRequest",
    "Distance",
    "EmailPreferences",
    "EmailPreferencesServiceClient",
    "EnableProgramRequest",
    "FindLfpProvidersRequest",
    "FindLfpProvidersResponse",
    "GbpAccount",
    "GbpAccountsServiceClient",
    "GetAccountRequest",
    "GetAccountTaxRequest",
    "GetAutofeedSettingsRequest",
    "GetAutomaticImprovementsRequest",
    "GetBusinessIdentityRequest",
    "GetBusinessInfoRequest",
    "GetCheckoutSettingsRequest",
    "GetEmailPreferencesRequest",
    "GetHomepageRequest",
    "GetOmnichannelSettingRequest",
    "GetOnlineReturnPolicyRequest",
    "GetProgramRequest",
    "GetRegionRequest",
    "GetShippingSettingsRequest",
    "GetTermsOfServiceAgreementStateRequest",
    "GetTermsOfServiceRequest",
    "GetUserRequest",
    "Headers",
    "Homepage",
    "HomepageServiceClient",
    "InStock",
    "InsertShippingSettingsRequest",
    "InventoryVerification",
    "LfpLink",
    "LfpProvider",
    "LfpProvidersServiceClient",
    "LinkGbpAccountRequest",
    "LinkGbpAccountResponse",
    "LinkLfpProviderRequest",
    "LinkLfpProviderResponse",
    "ListAccountIssuesRequest",
    "ListAccountIssuesResponse",
    "ListAccountTaxRequest",
    "ListAccountTaxResponse",
    "ListAccountsRequest",
    "ListAccountsResponse",
    "ListGbpAccountsRequest",
    "ListGbpAccountsResponse",
    "ListOmnichannelSettingsRequest",
    "ListOmnichannelSettingsResponse",
    "ListOnlineReturnPoliciesRequest",
    "ListOnlineReturnPoliciesResponse",
    "ListProgramsRequest",
    "ListProgramsResponse",
    "ListRegionsRequest",
    "ListRegionsResponse",
    "ListSubAccountsRequest",
    "ListSubAccountsResponse",
    "ListUsersRequest",
    "ListUsersResponse",
    "LocationIdSet",
    "MinimumOrderValueTable",
    "OmnichannelSetting",
    "OmnichannelSettingsServiceClient",
    "OnDisplayToOrder",
    "OnlineReturnPolicy",
    "OnlineReturnPolicyServiceClient",
    "PhoneVerificationState",
    "Pickup",
    "Program",
    "ProgramsServiceClient",
    "RateGroup",
    "Region",
    "RegionsServiceClient",
    "RequestInventoryVerificationRequest",
    "RequestInventoryVerificationResponse",
    "Required",
    "RetrieveForApplicationTermsOfServiceAgreementStateRequest",
    "RetrieveLatestTermsOfServiceRequest",
    "ReviewState",
    "Row",
    "Service",
    "ShippingSettings",
    "ShippingSettingsServiceClient",
    "Table",
    "TaxRule",
    "TermsOfService",
    "TermsOfServiceAgreementState",
    "TermsOfServiceAgreementStateServiceClient",
    "TermsOfServiceKind",
    "TermsOfServiceServiceClient",
    "TransitTable",
    "UnclaimHomepageRequest",
    "UpdateAccountRequest",
    "UpdateAccountTaxRequest",
    "UpdateAutofeedSettingsRequest",
    "UpdateAutomaticImprovementsRequest",
    "UpdateBusinessIdentityRequest",
    "UpdateBusinessInfoRequest",
    "UpdateCheckoutSettingsRequest",
    "UpdateEmailPreferencesRequest",
    "UpdateHomepageRequest",
    "UpdateOmnichannelSettingRequest",
    "UpdateOnlineReturnPolicyRequest",
    "UpdateRegionRequest",
    "UpdateUserRequest",
    "UriSettings",
    "User",
    "UserServiceClient",
    "Value",
    "VerificationMailSettings",
    "Warehouse",
    "WarehouseBasedDeliveryTime",
    "WarehouseCutoffTime",
)

api_core.check_python_version("google.shopping.merchant_accounts_v1beta")
api_core.check_dependency_versions("google.shopping.merchant_accounts_v1beta")
