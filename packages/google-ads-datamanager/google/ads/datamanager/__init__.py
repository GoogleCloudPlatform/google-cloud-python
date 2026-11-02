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
from google.ads.datamanager import gapic_version as package_version

__version__ = package_version.__version__


from google.ads.datamanager_v1.services.ingestion_service.async_client import (
    IngestionServiceAsyncClient,
)
from google.ads.datamanager_v1.services.ingestion_service.client import (
    IngestionServiceClient,
)
from google.ads.datamanager_v1.services.marketing_data_insights_service.async_client import (
    MarketingDataInsightsServiceAsyncClient,
)
from google.ads.datamanager_v1.services.marketing_data_insights_service.client import (
    MarketingDataInsightsServiceClient,
)
from google.ads.datamanager_v1.services.partner_link_service.async_client import (
    PartnerLinkServiceAsyncClient,
)
from google.ads.datamanager_v1.services.partner_link_service.client import (
    PartnerLinkServiceClient,
)
from google.ads.datamanager_v1.services.user_list_direct_license_service.async_client import (
    UserListDirectLicenseServiceAsyncClient,
)
from google.ads.datamanager_v1.services.user_list_direct_license_service.client import (
    UserListDirectLicenseServiceClient,
)
from google.ads.datamanager_v1.services.user_list_global_license_service.async_client import (
    UserListGlobalLicenseServiceAsyncClient,
)
from google.ads.datamanager_v1.services.user_list_global_license_service.client import (
    UserListGlobalLicenseServiceClient,
)
from google.ads.datamanager_v1.services.user_list_service.async_client import (
    UserListServiceAsyncClient,
)
from google.ads.datamanager_v1.services.user_list_service.client import (
    UserListServiceClient,
)
from google.ads.datamanager_v1.types.ad_event import (
    AdEvent,
    AdFormat,
    AdPlacement,
    AdType,
    AttributionHint,
    Platform,
    PlatformType,
    TargetingType,
)
from google.ads.datamanager_v1.types.age_range import AgeRange
from google.ads.datamanager_v1.types.audience import (
    AudienceMember,
    CompositeData,
    GoogleUserIdData,
    IpData,
    MobileData,
    PairData,
    PartnerProvidedIdData,
    PpidData,
    UserIdData,
)
from google.ads.datamanager_v1.types.cart_data import CartData, Item, ItemCustomVariable
from google.ads.datamanager_v1.types.consent import Consent, ConsentStatus
from google.ads.datamanager_v1.types.destination import (
    Destination,
    Product,
    ProductAccount,
)
from google.ads.datamanager_v1.types.device_info import DeviceInfo
from google.ads.datamanager_v1.types.encrypted_user_id import EncryptedUserId
from google.ads.datamanager_v1.types.encryption_info import (
    AwsWrappedKeyInfo,
    CoordinatorKeyInfo,
    EncryptionInfo,
    GcpWrappedKeyInfo,
)
from google.ads.datamanager_v1.types.error import ErrorReason
from google.ads.datamanager_v1.types.event import (
    AdIdentifiers,
    CustomVariable,
    Event,
    EventLocation,
    EventParameter,
    EventSource,
)
from google.ads.datamanager_v1.types.experimental_field import ExperimentalField
from google.ads.datamanager_v1.types.gender import Gender
from google.ads.datamanager_v1.types.ingestion_service import (
    Encoding,
    IngestAdEventsRequest,
    IngestAdEventsResponse,
    IngestAudienceMembersRequest,
    IngestAudienceMembersResponse,
    IngestEventsRequest,
    IngestEventsResponse,
    IngestUsersRequest,
    IngestUsersResponse,
    RemoveAllAudienceMembersRequest,
    RemoveAllAudienceMembersResponse,
    RemoveAudienceMembersRequest,
    RemoveAudienceMembersResponse,
    RemoveUsersRequest,
    RemoveUsersResponse,
    RetrieveRequestStatusRequest,
    RetrieveRequestStatusResponse,
)
from google.ads.datamanager_v1.types.insights_service import (
    Baseline,
    RetrieveInsightsRequest,
    RetrieveInsightsResponse,
)
from google.ads.datamanager_v1.types.item_parameter import ItemParameter
from google.ads.datamanager_v1.types.match_rate import MatchRateRange
from google.ads.datamanager_v1.types.partner_link_service import (
    CreatePartnerLinkRequest,
    DeletePartnerLinkRequest,
    FeatureSet,
    PartnerCustomerAccount,
    PartnerLink,
    PartnerLinkMetadata,
    SearchPartnerLinksRequest,
    SearchPartnerLinksResponse,
)
from google.ads.datamanager_v1.types.processing_errors import (
    ErrorCount,
    ErrorInfo,
    FieldWarning,
    ProcessingErrorReason,
    ProcessingWarningReason,
    WarningCount,
    WarningInfo,
    WarningReason,
)
from google.ads.datamanager_v1.types.request_status_per_destination import (
    RequestStatusPerDestination,
)
from google.ads.datamanager_v1.types.terms_of_service import (
    TermsOfService,
    TermsOfServiceStatus,
)
from google.ads.datamanager_v1.types.user import User
from google.ads.datamanager_v1.types.user_data import (
    AddressInfo,
    UserData,
    UserIdentifier,
)
from google.ads.datamanager_v1.types.user_list import (
    ContactIdInfo,
    DataSourceType,
    IngestedUserListInfo,
    MobileIdInfo,
    PairIdInfo,
    PartnerAudienceInfo,
    PseudonymousIdInfo,
    SizeInfo,
    TargetNetworkInfo,
    UserIdInfo,
    UserList,
)
from google.ads.datamanager_v1.types.user_list_direct_license import (
    UserListDirectLicense,
)
from google.ads.datamanager_v1.types.user_list_direct_license_service import (
    CreateUserListDirectLicenseRequest,
    GetUserListDirectLicenseRequest,
    ListUserListDirectLicensesRequest,
    ListUserListDirectLicensesResponse,
    UpdateUserListDirectLicenseRequest,
)
from google.ads.datamanager_v1.types.user_list_global_license import (
    UserListGlobalLicense,
    UserListGlobalLicenseCustomerInfo,
)
from google.ads.datamanager_v1.types.user_list_global_license_service import (
    CreateUserListGlobalLicenseRequest,
    GetUserListGlobalLicenseRequest,
    ListUserListGlobalLicenseCustomerInfosRequest,
    ListUserListGlobalLicenseCustomerInfosResponse,
    ListUserListGlobalLicensesRequest,
    ListUserListGlobalLicensesResponse,
    UpdateUserListGlobalLicenseRequest,
)
from google.ads.datamanager_v1.types.user_list_global_license_type import (
    UserListGlobalLicenseType,
)
from google.ads.datamanager_v1.types.user_list_license_client_account_type import (
    UserListLicenseClientAccountType,
)
from google.ads.datamanager_v1.types.user_list_license_metrics import (
    UserListLicenseMetrics,
)
from google.ads.datamanager_v1.types.user_list_license_pricing import (
    UserListLicensePricing,
)
from google.ads.datamanager_v1.types.user_list_license_status import (
    UserListLicenseStatus,
)
from google.ads.datamanager_v1.types.user_list_service import (
    CreateUserListRequest,
    DeleteUserListRequest,
    GetUserListRequest,
    ListUserListsRequest,
    ListUserListsResponse,
    UpdateUserListRequest,
)
from google.ads.datamanager_v1.types.user_properties import (
    CustomerType,
    CustomerValueBucket,
    UserProperties,
    UserProperty,
)
from google.ads.datamanager_v1.types.viewability_info import (
    MediaQuartile,
    ViewabilityInfo,
    ViewType,
)

__all__ = (
    "IngestionServiceClient",
    "IngestionServiceAsyncClient",
    "MarketingDataInsightsServiceClient",
    "MarketingDataInsightsServiceAsyncClient",
    "PartnerLinkServiceClient",
    "PartnerLinkServiceAsyncClient",
    "UserListDirectLicenseServiceClient",
    "UserListDirectLicenseServiceAsyncClient",
    "UserListGlobalLicenseServiceClient",
    "UserListGlobalLicenseServiceAsyncClient",
    "UserListServiceClient",
    "UserListServiceAsyncClient",
    "AdEvent",
    "AdFormat",
    "AdPlacement",
    "AdType",
    "AttributionHint",
    "Platform",
    "PlatformType",
    "TargetingType",
    "AgeRange",
    "AudienceMember",
    "CompositeData",
    "GoogleUserIdData",
    "IpData",
    "MobileData",
    "PairData",
    "PartnerProvidedIdData",
    "PpidData",
    "UserIdData",
    "CartData",
    "Item",
    "ItemCustomVariable",
    "Consent",
    "ConsentStatus",
    "Destination",
    "ProductAccount",
    "Product",
    "DeviceInfo",
    "EncryptedUserId",
    "AwsWrappedKeyInfo",
    "CoordinatorKeyInfo",
    "EncryptionInfo",
    "GcpWrappedKeyInfo",
    "ErrorReason",
    "AdIdentifiers",
    "CustomVariable",
    "Event",
    "EventLocation",
    "EventParameter",
    "EventSource",
    "ExperimentalField",
    "Gender",
    "IngestAdEventsRequest",
    "IngestAdEventsResponse",
    "IngestAudienceMembersRequest",
    "IngestAudienceMembersResponse",
    "IngestEventsRequest",
    "IngestEventsResponse",
    "IngestUsersRequest",
    "IngestUsersResponse",
    "RemoveAllAudienceMembersRequest",
    "RemoveAllAudienceMembersResponse",
    "RemoveAudienceMembersRequest",
    "RemoveAudienceMembersResponse",
    "RemoveUsersRequest",
    "RemoveUsersResponse",
    "RetrieveRequestStatusRequest",
    "RetrieveRequestStatusResponse",
    "Encoding",
    "Baseline",
    "RetrieveInsightsRequest",
    "RetrieveInsightsResponse",
    "ItemParameter",
    "MatchRateRange",
    "CreatePartnerLinkRequest",
    "DeletePartnerLinkRequest",
    "PartnerCustomerAccount",
    "PartnerLink",
    "PartnerLinkMetadata",
    "SearchPartnerLinksRequest",
    "SearchPartnerLinksResponse",
    "FeatureSet",
    "ErrorCount",
    "ErrorInfo",
    "FieldWarning",
    "WarningCount",
    "WarningInfo",
    "ProcessingErrorReason",
    "ProcessingWarningReason",
    "WarningReason",
    "RequestStatusPerDestination",
    "TermsOfService",
    "TermsOfServiceStatus",
    "User",
    "AddressInfo",
    "UserData",
    "UserIdentifier",
    "ContactIdInfo",
    "IngestedUserListInfo",
    "MobileIdInfo",
    "PairIdInfo",
    "PartnerAudienceInfo",
    "PseudonymousIdInfo",
    "SizeInfo",
    "TargetNetworkInfo",
    "UserIdInfo",
    "UserList",
    "DataSourceType",
    "UserListDirectLicense",
    "CreateUserListDirectLicenseRequest",
    "GetUserListDirectLicenseRequest",
    "ListUserListDirectLicensesRequest",
    "ListUserListDirectLicensesResponse",
    "UpdateUserListDirectLicenseRequest",
    "UserListGlobalLicense",
    "UserListGlobalLicenseCustomerInfo",
    "CreateUserListGlobalLicenseRequest",
    "GetUserListGlobalLicenseRequest",
    "ListUserListGlobalLicenseCustomerInfosRequest",
    "ListUserListGlobalLicenseCustomerInfosResponse",
    "ListUserListGlobalLicensesRequest",
    "ListUserListGlobalLicensesResponse",
    "UpdateUserListGlobalLicenseRequest",
    "UserListGlobalLicenseType",
    "UserListLicenseClientAccountType",
    "UserListLicenseMetrics",
    "UserListLicensePricing",
    "UserListLicenseStatus",
    "CreateUserListRequest",
    "DeleteUserListRequest",
    "GetUserListRequest",
    "ListUserListsRequest",
    "ListUserListsResponse",
    "UpdateUserListRequest",
    "UserProperties",
    "UserProperty",
    "CustomerType",
    "CustomerValueBucket",
    "ViewabilityInfo",
    "MediaQuartile",
    "ViewType",
)
