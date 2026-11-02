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
from .ad_event import (
    AdEvent,
    AdFormat,
    AdPlacement,
    AdType,
    AttributionHint,
    Platform,
    PlatformType,
    TargetingType,
)
from .age_range import (
    AgeRange,
)
from .audience import (
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
from .cart_data import (
    CartData,
    Item,
    ItemCustomVariable,
)
from .consent import (
    Consent,
    ConsentStatus,
)
from .destination import (
    Destination,
    Product,
    ProductAccount,
)
from .device_info import (
    DeviceInfo,
)
from .encrypted_user_id import (
    EncryptedUserId,
)
from .encryption_info import (
    AwsWrappedKeyInfo,
    CoordinatorKeyInfo,
    EncryptionInfo,
    GcpWrappedKeyInfo,
)
from .error import (
    ErrorReason,
)
from .event import (
    AdIdentifiers,
    CustomVariable,
    Event,
    EventLocation,
    EventParameter,
    EventSource,
)
from .experimental_field import (
    ExperimentalField,
)
from .gender import (
    Gender,
)
from .ingestion_service import (
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
from .insights_service import (
    Baseline,
    RetrieveInsightsRequest,
    RetrieveInsightsResponse,
)
from .item_parameter import (
    ItemParameter,
)
from .match_rate import (
    MatchRateRange,
)
from .partner_link_service import (
    CreatePartnerLinkRequest,
    DeletePartnerLinkRequest,
    FeatureSet,
    PartnerCustomerAccount,
    PartnerLink,
    PartnerLinkMetadata,
    SearchPartnerLinksRequest,
    SearchPartnerLinksResponse,
)
from .processing_errors import (
    ErrorCount,
    ErrorInfo,
    FieldWarning,
    ProcessingErrorReason,
    ProcessingWarningReason,
    WarningCount,
    WarningInfo,
    WarningReason,
)
from .request_status_per_destination import (
    RequestStatusPerDestination,
)
from .terms_of_service import (
    TermsOfService,
    TermsOfServiceStatus,
)
from .user import (
    User,
)
from .user_data import (
    AddressInfo,
    UserData,
    UserIdentifier,
)
from .user_list import (
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
from .user_list_direct_license import (
    UserListDirectLicense,
)
from .user_list_direct_license_service import (
    CreateUserListDirectLicenseRequest,
    GetUserListDirectLicenseRequest,
    ListUserListDirectLicensesRequest,
    ListUserListDirectLicensesResponse,
    UpdateUserListDirectLicenseRequest,
)
from .user_list_global_license import (
    UserListGlobalLicense,
    UserListGlobalLicenseCustomerInfo,
)
from .user_list_global_license_service import (
    CreateUserListGlobalLicenseRequest,
    GetUserListGlobalLicenseRequest,
    ListUserListGlobalLicenseCustomerInfosRequest,
    ListUserListGlobalLicenseCustomerInfosResponse,
    ListUserListGlobalLicensesRequest,
    ListUserListGlobalLicensesResponse,
    UpdateUserListGlobalLicenseRequest,
)
from .user_list_global_license_type import (
    UserListGlobalLicenseType,
)
from .user_list_license_client_account_type import (
    UserListLicenseClientAccountType,
)
from .user_list_license_metrics import (
    UserListLicenseMetrics,
)
from .user_list_license_pricing import (
    UserListLicensePricing,
)
from .user_list_license_status import (
    UserListLicenseStatus,
)
from .user_list_service import (
    CreateUserListRequest,
    DeleteUserListRequest,
    GetUserListRequest,
    ListUserListsRequest,
    ListUserListsResponse,
    UpdateUserListRequest,
)
from .user_properties import (
    CustomerType,
    CustomerValueBucket,
    UserProperties,
    UserProperty,
)
from .viewability_info import (
    MediaQuartile,
    ViewabilityInfo,
    ViewType,
)

__all__ = (
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
