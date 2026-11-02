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
from google.shopping.merchant_accounts import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_accounts_v1.services.account_issue_service.async_client import (
    AccountIssueServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.account_issue_service.client import (
    AccountIssueServiceClient,
)
from google.shopping.merchant_accounts_v1.services.account_relationships_service.async_client import (
    AccountRelationshipsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.account_relationships_service.client import (
    AccountRelationshipsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.account_services_service.async_client import (
    AccountServicesServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.account_services_service.client import (
    AccountServicesServiceClient,
)
from google.shopping.merchant_accounts_v1.services.accounts_service.async_client import (
    AccountsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.accounts_service.client import (
    AccountsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.autofeed_settings_service.async_client import (
    AutofeedSettingsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.autofeed_settings_service.client import (
    AutofeedSettingsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.automatic_improvements_service.async_client import (
    AutomaticImprovementsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.automatic_improvements_service.client import (
    AutomaticImprovementsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.business_identity_service.async_client import (
    BusinessIdentityServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.business_identity_service.client import (
    BusinessIdentityServiceClient,
)
from google.shopping.merchant_accounts_v1.services.business_info_service.async_client import (
    BusinessInfoServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.business_info_service.client import (
    BusinessInfoServiceClient,
)
from google.shopping.merchant_accounts_v1.services.checkout_settings_service.async_client import (
    CheckoutSettingsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.checkout_settings_service.client import (
    CheckoutSettingsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.developer_registration_service.async_client import (
    DeveloperRegistrationServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.developer_registration_service.client import (
    DeveloperRegistrationServiceClient,
)
from google.shopping.merchant_accounts_v1.services.email_preferences_service.async_client import (
    EmailPreferencesServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.email_preferences_service.client import (
    EmailPreferencesServiceClient,
)
from google.shopping.merchant_accounts_v1.services.gbp_accounts_service.async_client import (
    GbpAccountsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.gbp_accounts_service.client import (
    GbpAccountsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.homepage_service.async_client import (
    HomepageServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.homepage_service.client import (
    HomepageServiceClient,
)
from google.shopping.merchant_accounts_v1.services.lfp_providers_service.async_client import (
    LfpProvidersServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.lfp_providers_service.client import (
    LfpProvidersServiceClient,
)
from google.shopping.merchant_accounts_v1.services.omnichannel_settings_service.async_client import (
    OmnichannelSettingsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.omnichannel_settings_service.client import (
    OmnichannelSettingsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.online_return_policy_service.async_client import (
    OnlineReturnPolicyServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.online_return_policy_service.client import (
    OnlineReturnPolicyServiceClient,
)
from google.shopping.merchant_accounts_v1.services.programs_service.async_client import (
    ProgramsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.programs_service.client import (
    ProgramsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.regions_service.async_client import (
    RegionsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.regions_service.client import (
    RegionsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.shipping_settings_service.async_client import (
    ShippingSettingsServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.shipping_settings_service.client import (
    ShippingSettingsServiceClient,
)
from google.shopping.merchant_accounts_v1.services.terms_of_service_agreement_state_service.async_client import (
    TermsOfServiceAgreementStateServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.terms_of_service_agreement_state_service.client import (
    TermsOfServiceAgreementStateServiceClient,
)
from google.shopping.merchant_accounts_v1.services.terms_of_service_service.async_client import (
    TermsOfServiceServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.terms_of_service_service.client import (
    TermsOfServiceServiceClient,
)
from google.shopping.merchant_accounts_v1.services.user_service.async_client import (
    UserServiceAsyncClient,
)
from google.shopping.merchant_accounts_v1.services.user_service.client import (
    UserServiceClient,
)
from google.shopping.merchant_accounts_v1.types.accessright import AccessRight
from google.shopping.merchant_accounts_v1.types.accountissue import (
    AccountIssue,
    ListAccountIssuesRequest,
    ListAccountIssuesResponse,
)
from google.shopping.merchant_accounts_v1.types.accountrelationships import (
    AccountRelationship,
    GetAccountRelationshipRequest,
    ListAccountRelationshipsRequest,
    ListAccountRelationshipsResponse,
    UpdateAccountRelationshipRequest,
)
from google.shopping.merchant_accounts_v1.types.accounts import (
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
from google.shopping.merchant_accounts_v1.types.accountservices import (
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
from google.shopping.merchant_accounts_v1.types.autofeedsettings import (
    AutofeedSettings,
    GetAutofeedSettingsRequest,
    UpdateAutofeedSettingsRequest,
)
from google.shopping.merchant_accounts_v1.types.automaticimprovements import (
    AutomaticImageImprovements,
    AutomaticImprovements,
    AutomaticItemUpdates,
    AutomaticShippingImprovements,
    GetAutomaticImprovementsRequest,
    UpdateAutomaticImprovementsRequest,
)
from google.shopping.merchant_accounts_v1.types.businessidentity import (
    BusinessIdentity,
    GetBusinessIdentityRequest,
    UpdateBusinessIdentityRequest,
)
from google.shopping.merchant_accounts_v1.types.businessinfo import (
    BusinessInfo,
    GetBusinessInfoRequest,
    UpdateBusinessInfoRequest,
)
from google.shopping.merchant_accounts_v1.types.checkoutsettings import (
    CheckoutSettings,
    CreateCheckoutSettingsRequest,
    DeleteCheckoutSettingsRequest,
    GetCheckoutSettingsRequest,
    UpdateCheckoutSettingsRequest,
    UriSettings,
)
from google.shopping.merchant_accounts_v1.types.customerservice import CustomerService
from google.shopping.merchant_accounts_v1.types.developerregistration import (
    DeveloperRegistration,
    GetAccountForGcpRegistrationResponse,
    GetDeveloperRegistrationRequest,
    RegisterGcpRequest,
    UnregisterGcpRequest,
)
from google.shopping.merchant_accounts_v1.types.emailpreferences import (
    EmailPreferences,
    GetEmailPreferencesRequest,
    UpdateEmailPreferencesRequest,
)
from google.shopping.merchant_accounts_v1.types.gbpaccounts import (
    GbpAccount,
    LinkGbpAccountRequest,
    LinkGbpAccountResponse,
    ListGbpAccountsRequest,
    ListGbpAccountsResponse,
)
from google.shopping.merchant_accounts_v1.types.homepage import (
    ClaimHomepageRequest,
    GetHomepageRequest,
    Homepage,
    UnclaimHomepageRequest,
    UpdateHomepageRequest,
)
from google.shopping.merchant_accounts_v1.types.lfpproviders import (
    FindLfpProvidersRequest,
    FindLfpProvidersResponse,
    LfpProvider,
    LinkLfpProviderRequest,
    LinkLfpProviderResponse,
)
from google.shopping.merchant_accounts_v1.types.omnichannelsettings import (
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
from google.shopping.merchant_accounts_v1.types.online_return_policy import (
    CreateOnlineReturnPolicyRequest,
    DeleteOnlineReturnPolicyRequest,
    GetOnlineReturnPolicyRequest,
    ListOnlineReturnPoliciesRequest,
    ListOnlineReturnPoliciesResponse,
    OnlineReturnPolicy,
)
from google.shopping.merchant_accounts_v1.types.phoneverificationstate import (
    PhoneVerificationState,
)
from google.shopping.merchant_accounts_v1.types.programs import (
    DisableProgramRequest,
    EnableProgramRequest,
    GetProgramRequest,
    ListProgramsRequest,
    ListProgramsResponse,
    Program,
)
from google.shopping.merchant_accounts_v1.types.regions import (
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
from google.shopping.merchant_accounts_v1.types.shippingsettings import (
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
from google.shopping.merchant_accounts_v1.types.termsofservice import (
    AcceptTermsOfServiceRequest,
    AcceptTermsOfServiceResponse,
    GetTermsOfServiceRequest,
    RetrieveLatestTermsOfServiceRequest,
    TermsOfService,
)
from google.shopping.merchant_accounts_v1.types.termsofserviceagreementstate import (
    Accepted,
    GetTermsOfServiceAgreementStateRequest,
    Required,
    RetrieveForApplicationTermsOfServiceAgreementStateRequest,
    TermsOfServiceAgreementState,
)
from google.shopping.merchant_accounts_v1.types.termsofservicekind import (
    TermsOfServiceKind,
)
from google.shopping.merchant_accounts_v1.types.user import (
    CreateUserRequest,
    DeleteUserRequest,
    GetUserRequest,
    ListUsersRequest,
    ListUsersResponse,
    UpdateUserRequest,
    User,
    VerifySelfRequest,
)
from google.shopping.merchant_accounts_v1.types.verificationmailsettings import (
    VerificationMailSettings,
)

__all__ = (
    "AccountIssueServiceClient",
    "AccountIssueServiceAsyncClient",
    "AccountRelationshipsServiceClient",
    "AccountRelationshipsServiceAsyncClient",
    "AccountServicesServiceClient",
    "AccountServicesServiceAsyncClient",
    "AccountsServiceClient",
    "AccountsServiceAsyncClient",
    "AutofeedSettingsServiceClient",
    "AutofeedSettingsServiceAsyncClient",
    "AutomaticImprovementsServiceClient",
    "AutomaticImprovementsServiceAsyncClient",
    "BusinessIdentityServiceClient",
    "BusinessIdentityServiceAsyncClient",
    "BusinessInfoServiceClient",
    "BusinessInfoServiceAsyncClient",
    "CheckoutSettingsServiceClient",
    "CheckoutSettingsServiceAsyncClient",
    "DeveloperRegistrationServiceClient",
    "DeveloperRegistrationServiceAsyncClient",
    "EmailPreferencesServiceClient",
    "EmailPreferencesServiceAsyncClient",
    "GbpAccountsServiceClient",
    "GbpAccountsServiceAsyncClient",
    "HomepageServiceClient",
    "HomepageServiceAsyncClient",
    "LfpProvidersServiceClient",
    "LfpProvidersServiceAsyncClient",
    "OmnichannelSettingsServiceClient",
    "OmnichannelSettingsServiceAsyncClient",
    "OnlineReturnPolicyServiceClient",
    "OnlineReturnPolicyServiceAsyncClient",
    "ProgramsServiceClient",
    "ProgramsServiceAsyncClient",
    "RegionsServiceClient",
    "RegionsServiceAsyncClient",
    "ShippingSettingsServiceClient",
    "ShippingSettingsServiceAsyncClient",
    "TermsOfServiceAgreementStateServiceClient",
    "TermsOfServiceAgreementStateServiceAsyncClient",
    "TermsOfServiceServiceClient",
    "TermsOfServiceServiceAsyncClient",
    "UserServiceClient",
    "UserServiceAsyncClient",
    "AccessRight",
    "AccountIssue",
    "ListAccountIssuesRequest",
    "ListAccountIssuesResponse",
    "AccountRelationship",
    "GetAccountRelationshipRequest",
    "ListAccountRelationshipsRequest",
    "ListAccountRelationshipsResponse",
    "UpdateAccountRelationshipRequest",
    "Account",
    "CreateAndConfigureAccountRequest",
    "CreateTestAccountRequest",
    "DeleteAccountRequest",
    "GetAccountRequest",
    "ListAccountsRequest",
    "ListAccountsResponse",
    "ListSubAccountsRequest",
    "ListSubAccountsResponse",
    "UpdateAccountRequest",
    "AccountAggregation",
    "AccountManagement",
    "AccountService",
    "ApproveAccountServiceRequest",
    "CampaignsManagement",
    "ComparisonShopping",
    "GetAccountServiceRequest",
    "Handshake",
    "ListAccountServicesRequest",
    "ListAccountServicesResponse",
    "LocalListingManagement",
    "ProductsManagement",
    "ProposeAccountServiceRequest",
    "RejectAccountServiceRequest",
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
    "DeveloperRegistration",
    "GetAccountForGcpRegistrationResponse",
    "GetDeveloperRegistrationRequest",
    "RegisterGcpRequest",
    "UnregisterGcpRequest",
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
    "PhoneVerificationState",
    "DisableProgramRequest",
    "EnableProgramRequest",
    "GetProgramRequest",
    "ListProgramsRequest",
    "ListProgramsResponse",
    "Program",
    "BatchCreateRegionsRequest",
    "BatchCreateRegionsResponse",
    "BatchDeleteRegionsRequest",
    "BatchUpdateRegionsRequest",
    "BatchUpdateRegionsResponse",
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
    "AcceptTermsOfServiceRequest",
    "AcceptTermsOfServiceResponse",
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
    "VerifySelfRequest",
    "VerificationMailSettings",
)
