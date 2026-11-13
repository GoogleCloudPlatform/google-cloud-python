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

from google.shopping.merchant_accounts_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.merchant_accounts_v1.services.account_issue_service",
    "google.shopping.merchant_accounts_v1.services.account_relationships_service",
    "google.shopping.merchant_accounts_v1.services.account_services_service",
    "google.shopping.merchant_accounts_v1.services.accounts_service",
    "google.shopping.merchant_accounts_v1.services.autofeed_settings_service",
    "google.shopping.merchant_accounts_v1.services.automatic_improvements_service",
    "google.shopping.merchant_accounts_v1.services.business_identity_service",
    "google.shopping.merchant_accounts_v1.services.business_info_service",
    "google.shopping.merchant_accounts_v1.services.checkout_settings_service",
    "google.shopping.merchant_accounts_v1.services.developer_registration_service",
    "google.shopping.merchant_accounts_v1.services.email_preferences_service",
    "google.shopping.merchant_accounts_v1.services.gbp_accounts_service",
    "google.shopping.merchant_accounts_v1.services.homepage_service",
    "google.shopping.merchant_accounts_v1.services.lfp_providers_service",
    "google.shopping.merchant_accounts_v1.services.omnichannel_settings_service",
    "google.shopping.merchant_accounts_v1.services.online_return_policy_service",
    "google.shopping.merchant_accounts_v1.services.programs_service",
    "google.shopping.merchant_accounts_v1.services.regions_service",
    "google.shopping.merchant_accounts_v1.services.shipping_settings_service",
    "google.shopping.merchant_accounts_v1.services.terms_of_service_agreement_state_service",
    "google.shopping.merchant_accounts_v1.services.terms_of_service_service",
    "google.shopping.merchant_accounts_v1.services.user_service",
    "google.shopping.merchant_accounts_v1.types.accessright",
    "google.shopping.merchant_accounts_v1.types.accountissue",
    "google.shopping.merchant_accounts_v1.types.accountrelationships",
    "google.shopping.merchant_accounts_v1.types.accounts",
    "google.shopping.merchant_accounts_v1.types.accountservices",
    "google.shopping.merchant_accounts_v1.types.autofeedsettings",
    "google.shopping.merchant_accounts_v1.types.automaticimprovements",
    "google.shopping.merchant_accounts_v1.types.businessidentity",
    "google.shopping.merchant_accounts_v1.types.businessinfo",
    "google.shopping.merchant_accounts_v1.types.checkoutsettings",
    "google.shopping.merchant_accounts_v1.types.customerservice",
    "google.shopping.merchant_accounts_v1.types.developerregistration",
    "google.shopping.merchant_accounts_v1.types.emailpreferences",
    "google.shopping.merchant_accounts_v1.types.gbpaccounts",
    "google.shopping.merchant_accounts_v1.types.homepage",
    "google.shopping.merchant_accounts_v1.types.lfpproviders",
    "google.shopping.merchant_accounts_v1.types.omnichannelsettings",
    "google.shopping.merchant_accounts_v1.types.online_return_policy",
    "google.shopping.merchant_accounts_v1.types.phoneverificationstate",
    "google.shopping.merchant_accounts_v1.types.programs",
    "google.shopping.merchant_accounts_v1.types.regions",
    "google.shopping.merchant_accounts_v1.types.shippingsettings",
    "google.shopping.merchant_accounts_v1.types.termsofservice",
    "google.shopping.merchant_accounts_v1.types.termsofserviceagreementstate",
    "google.shopping.merchant_accounts_v1.types.termsofservicekind",
    "google.shopping.merchant_accounts_v1.types.user",
    "google.shopping.merchant_accounts_v1.types.verificationmailsettings",
}


from .services.account_issue_service import (
    AccountIssueServiceAsyncClient,
    AccountIssueServiceClient,
)
from .services.account_relationships_service import (
    AccountRelationshipsServiceAsyncClient,
    AccountRelationshipsServiceClient,
)
from .services.account_services_service import (
    AccountServicesServiceAsyncClient,
    AccountServicesServiceClient,
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
from .services.developer_registration_service import (
    DeveloperRegistrationServiceAsyncClient,
    DeveloperRegistrationServiceClient,
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
from .types.accountissue import (
    AccountIssue,
    ListAccountIssuesRequest,
    ListAccountIssuesResponse,
)
from .types.accountrelationships import (
    AccountRelationship,
    GetAccountRelationshipRequest,
    ListAccountRelationshipsRequest,
    ListAccountRelationshipsResponse,
    UpdateAccountRelationshipRequest,
)
from .types.accounts import (
    Account,
    CreateAndConfigureAccountRequest,
    CreateTestAccountRequest,
    DeleteAccountRequest,
    GetAccountRequest,
    ListAccountsRequest,
    ListAccountsResponse,
    ListSubAccountsRequest,
    ListSubAccountsResponse,
    UpdateAccountRequest,
)
from .types.accountservices import (
    AccountAggregation,
    AccountManagement,
    AccountService,
    ApproveAccountServiceRequest,
    CampaignsManagement,
    ComparisonShopping,
    GetAccountServiceRequest,
    Handshake,
    ListAccountServicesRequest,
    ListAccountServicesResponse,
    LocalListingManagement,
    ProductsManagement,
    ProposeAccountServiceRequest,
    RejectAccountServiceRequest,
)
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
from .types.developerregistration import (
    DeveloperRegistration,
    GetAccountForGcpRegistrationResponse,
    GetDeveloperRegistrationRequest,
    RegisterGcpRequest,
    UnregisterGcpRequest,
)
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
    BatchCreateRegionsRequest,
    BatchCreateRegionsResponse,
    BatchDeleteRegionsRequest,
    BatchUpdateRegionsRequest,
    BatchUpdateRegionsResponse,
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
from .types.termsofservice import (
    AcceptTermsOfServiceRequest,
    AcceptTermsOfServiceResponse,
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
    VerifySelfRequest,
)
from .types.verificationmailsettings import VerificationMailSettings

__all__ = (
    "AccountIssueServiceAsyncClient",
    "AccountRelationshipsServiceAsyncClient",
    "AccountServicesServiceAsyncClient",
    "AccountsServiceAsyncClient",
    "AutofeedSettingsServiceAsyncClient",
    "AutomaticImprovementsServiceAsyncClient",
    "BusinessIdentityServiceAsyncClient",
    "BusinessInfoServiceAsyncClient",
    "CheckoutSettingsServiceAsyncClient",
    "DeveloperRegistrationServiceAsyncClient",
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
    "AcceptTermsOfServiceResponse",
    "Accepted",
    "AccessRight",
    "Account",
    "AccountAggregation",
    "AccountIssue",
    "AccountIssueServiceClient",
    "AccountManagement",
    "AccountRelationship",
    "AccountRelationshipsServiceClient",
    "AccountService",
    "AccountServicesServiceClient",
    "AccountsServiceClient",
    "Address",
    "ApproveAccountServiceRequest",
    "AutofeedSettings",
    "AutofeedSettingsServiceClient",
    "AutomaticImageImprovements",
    "AutomaticImprovements",
    "AutomaticImprovementsServiceClient",
    "AutomaticItemUpdates",
    "AutomaticShippingImprovements",
    "BatchCreateRegionsRequest",
    "BatchCreateRegionsResponse",
    "BatchDeleteRegionsRequest",
    "BatchUpdateRegionsRequest",
    "BatchUpdateRegionsResponse",
    "BusinessDayConfig",
    "BusinessIdentity",
    "BusinessIdentityServiceClient",
    "BusinessInfo",
    "BusinessInfoServiceClient",
    "CampaignsManagement",
    "CarrierRate",
    "CheckoutSettings",
    "CheckoutSettingsServiceClient",
    "ClaimHomepageRequest",
    "ComparisonShopping",
    "CreateAndConfigureAccountRequest",
    "CreateCheckoutSettingsRequest",
    "CreateOmnichannelSettingRequest",
    "CreateOnlineReturnPolicyRequest",
    "CreateRegionRequest",
    "CreateTestAccountRequest",
    "CreateUserRequest",
    "CustomerService",
    "CutoffTime",
    "DeleteAccountRequest",
    "DeleteCheckoutSettingsRequest",
    "DeleteOnlineReturnPolicyRequest",
    "DeleteRegionRequest",
    "DeleteUserRequest",
    "DeliveryTime",
    "DeveloperRegistration",
    "DeveloperRegistrationServiceClient",
    "DisableProgramRequest",
    "Distance",
    "EmailPreferences",
    "EmailPreferencesServiceClient",
    "EnableProgramRequest",
    "FindLfpProvidersRequest",
    "FindLfpProvidersResponse",
    "GbpAccount",
    "GbpAccountsServiceClient",
    "GetAccountForGcpRegistrationResponse",
    "GetAccountRelationshipRequest",
    "GetAccountRequest",
    "GetAccountServiceRequest",
    "GetAutofeedSettingsRequest",
    "GetAutomaticImprovementsRequest",
    "GetBusinessIdentityRequest",
    "GetBusinessInfoRequest",
    "GetCheckoutSettingsRequest",
    "GetDeveloperRegistrationRequest",
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
    "Handshake",
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
    "ListAccountRelationshipsRequest",
    "ListAccountRelationshipsResponse",
    "ListAccountServicesRequest",
    "ListAccountServicesResponse",
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
    "LocalListingManagement",
    "LocationIdSet",
    "MinimumOrderValueTable",
    "OmnichannelSetting",
    "OmnichannelSettingsServiceClient",
    "OnDisplayToOrder",
    "OnlineReturnPolicy",
    "OnlineReturnPolicyServiceClient",
    "PhoneVerificationState",
    "Pickup",
    "ProductsManagement",
    "Program",
    "ProgramsServiceClient",
    "ProposeAccountServiceRequest",
    "RateGroup",
    "Region",
    "RegionsServiceClient",
    "RegisterGcpRequest",
    "RejectAccountServiceRequest",
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
    "TermsOfService",
    "TermsOfServiceAgreementState",
    "TermsOfServiceAgreementStateServiceClient",
    "TermsOfServiceKind",
    "TermsOfServiceServiceClient",
    "TransitTable",
    "UnclaimHomepageRequest",
    "UnregisterGcpRequest",
    "UpdateAccountRelationshipRequest",
    "UpdateAccountRequest",
    "UpdateAutofeedSettingsRequest",
    "UpdateAutomaticImprovementsRequest",
    "UpdateBusinessIdentityRequest",
    "UpdateBusinessInfoRequest",
    "UpdateCheckoutSettingsRequest",
    "UpdateEmailPreferencesRequest",
    "UpdateHomepageRequest",
    "UpdateOmnichannelSettingRequest",
    "UpdateRegionRequest",
    "UpdateUserRequest",
    "UriSettings",
    "User",
    "UserServiceClient",
    "Value",
    "VerificationMailSettings",
    "VerifySelfRequest",
    "Warehouse",
    "WarehouseBasedDeliveryTime",
    "WarehouseCutoffTime",
)

api_core.check_python_version("google.shopping.merchant_accounts_v1")
api_core.check_dependency_versions("google.shopping.merchant_accounts_v1")
