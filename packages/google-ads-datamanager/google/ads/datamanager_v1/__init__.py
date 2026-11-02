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

from google.ads.datamanager_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.ads.datamanager_v1.services.ingestion_service",
    "google.ads.datamanager_v1.services.marketing_data_insights_service",
    "google.ads.datamanager_v1.services.partner_link_service",
    "google.ads.datamanager_v1.services.user_list_direct_license_service",
    "google.ads.datamanager_v1.services.user_list_global_license_service",
    "google.ads.datamanager_v1.services.user_list_service",
    "google.ads.datamanager_v1.types.ad_event",
    "google.ads.datamanager_v1.types.age_range",
    "google.ads.datamanager_v1.types.audience",
    "google.ads.datamanager_v1.types.cart_data",
    "google.ads.datamanager_v1.types.consent",
    "google.ads.datamanager_v1.types.destination",
    "google.ads.datamanager_v1.types.device_info",
    "google.ads.datamanager_v1.types.encrypted_user_id",
    "google.ads.datamanager_v1.types.encryption_info",
    "google.ads.datamanager_v1.types.error",
    "google.ads.datamanager_v1.types.event",
    "google.ads.datamanager_v1.types.experimental_field",
    "google.ads.datamanager_v1.types.gender",
    "google.ads.datamanager_v1.types.ingestion_service",
    "google.ads.datamanager_v1.types.insights_service",
    "google.ads.datamanager_v1.types.item_parameter",
    "google.ads.datamanager_v1.types.match_rate",
    "google.ads.datamanager_v1.types.partner_link_service",
    "google.ads.datamanager_v1.types.processing_errors",
    "google.ads.datamanager_v1.types.request_status_per_destination",
    "google.ads.datamanager_v1.types.terms_of_service",
    "google.ads.datamanager_v1.types.user",
    "google.ads.datamanager_v1.types.user_data",
    "google.ads.datamanager_v1.types.user_list",
    "google.ads.datamanager_v1.types.user_list_direct_license",
    "google.ads.datamanager_v1.types.user_list_direct_license_service",
    "google.ads.datamanager_v1.types.user_list_global_license",
    "google.ads.datamanager_v1.types.user_list_global_license_service",
    "google.ads.datamanager_v1.types.user_list_global_license_type",
    "google.ads.datamanager_v1.types.user_list_license_client_account_type",
    "google.ads.datamanager_v1.types.user_list_license_metrics",
    "google.ads.datamanager_v1.types.user_list_license_pricing",
    "google.ads.datamanager_v1.types.user_list_license_status",
    "google.ads.datamanager_v1.types.user_list_service",
    "google.ads.datamanager_v1.types.user_properties",
    "google.ads.datamanager_v1.types.viewability_info",
}


from .services.ingestion_service import (
    IngestionServiceAsyncClient,
    IngestionServiceClient,
)
from .services.marketing_data_insights_service import (
    MarketingDataInsightsServiceAsyncClient,
    MarketingDataInsightsServiceClient,
)
from .services.partner_link_service import (
    PartnerLinkServiceAsyncClient,
    PartnerLinkServiceClient,
)
from .services.user_list_direct_license_service import (
    UserListDirectLicenseServiceAsyncClient,
    UserListDirectLicenseServiceClient,
)
from .services.user_list_global_license_service import (
    UserListGlobalLicenseServiceAsyncClient,
    UserListGlobalLicenseServiceClient,
)
from .services.user_list_service import (
    UserListServiceAsyncClient,
    UserListServiceClient,
)
from .types.ad_event import (
    AdEvent,
    AdFormat,
    AdPlacement,
    AdType,
    AttributionHint,
    Platform,
    PlatformType,
    TargetingType,
)
from .types.age_range import AgeRange
from .types.audience import (
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
from .types.cart_data import CartData, Item, ItemCustomVariable
from .types.consent import Consent, ConsentStatus
from .types.destination import Destination, Product, ProductAccount
from .types.device_info import DeviceInfo
from .types.encrypted_user_id import EncryptedUserId
from .types.encryption_info import (
    AwsWrappedKeyInfo,
    CoordinatorKeyInfo,
    EncryptionInfo,
    GcpWrappedKeyInfo,
)
from .types.error import ErrorReason
from .types.event import (
    AdIdentifiers,
    CustomVariable,
    Event,
    EventLocation,
    EventParameter,
    EventSource,
)
from .types.experimental_field import ExperimentalField
from .types.gender import Gender
from .types.ingestion_service import (
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
from .types.insights_service import (
    Baseline,
    RetrieveInsightsRequest,
    RetrieveInsightsResponse,
)
from .types.item_parameter import ItemParameter
from .types.match_rate import MatchRateRange
from .types.partner_link_service import (
    CreatePartnerLinkRequest,
    DeletePartnerLinkRequest,
    FeatureSet,
    PartnerCustomerAccount,
    PartnerLink,
    PartnerLinkMetadata,
    SearchPartnerLinksRequest,
    SearchPartnerLinksResponse,
)
from .types.processing_errors import (
    ErrorCount,
    ErrorInfo,
    FieldWarning,
    ProcessingErrorReason,
    ProcessingWarningReason,
    WarningCount,
    WarningInfo,
    WarningReason,
)
from .types.request_status_per_destination import RequestStatusPerDestination
from .types.terms_of_service import TermsOfService, TermsOfServiceStatus
from .types.user import User
from .types.user_data import AddressInfo, UserData, UserIdentifier
from .types.user_list import (
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
from .types.user_list_direct_license import UserListDirectLicense
from .types.user_list_direct_license_service import (
    CreateUserListDirectLicenseRequest,
    GetUserListDirectLicenseRequest,
    ListUserListDirectLicensesRequest,
    ListUserListDirectLicensesResponse,
    UpdateUserListDirectLicenseRequest,
)
from .types.user_list_global_license import (
    UserListGlobalLicense,
    UserListGlobalLicenseCustomerInfo,
)
from .types.user_list_global_license_service import (
    CreateUserListGlobalLicenseRequest,
    GetUserListGlobalLicenseRequest,
    ListUserListGlobalLicenseCustomerInfosRequest,
    ListUserListGlobalLicenseCustomerInfosResponse,
    ListUserListGlobalLicensesRequest,
    ListUserListGlobalLicensesResponse,
    UpdateUserListGlobalLicenseRequest,
)
from .types.user_list_global_license_type import UserListGlobalLicenseType
from .types.user_list_license_client_account_type import (
    UserListLicenseClientAccountType,
)
from .types.user_list_license_metrics import UserListLicenseMetrics
from .types.user_list_license_pricing import UserListLicensePricing
from .types.user_list_license_status import UserListLicenseStatus
from .types.user_list_service import (
    CreateUserListRequest,
    DeleteUserListRequest,
    GetUserListRequest,
    ListUserListsRequest,
    ListUserListsResponse,
    UpdateUserListRequest,
)
from .types.user_properties import (
    CustomerType,
    CustomerValueBucket,
    UserProperties,
    UserProperty,
)
from .types.viewability_info import MediaQuartile, ViewabilityInfo, ViewType

__all__ = (
    "IngestionServiceAsyncClient",
    "MarketingDataInsightsServiceAsyncClient",
    "PartnerLinkServiceAsyncClient",
    "UserListDirectLicenseServiceAsyncClient",
    "UserListGlobalLicenseServiceAsyncClient",
    "UserListServiceAsyncClient",
    "AdEvent",
    "AdFormat",
    "AdIdentifiers",
    "AdPlacement",
    "AdType",
    "AddressInfo",
    "AgeRange",
    "AttributionHint",
    "AudienceMember",
    "AwsWrappedKeyInfo",
    "Baseline",
    "CartData",
    "CompositeData",
    "Consent",
    "ConsentStatus",
    "ContactIdInfo",
    "CoordinatorKeyInfo",
    "CreatePartnerLinkRequest",
    "CreateUserListDirectLicenseRequest",
    "CreateUserListGlobalLicenseRequest",
    "CreateUserListRequest",
    "CustomVariable",
    "CustomerType",
    "CustomerValueBucket",
    "DataSourceType",
    "DeletePartnerLinkRequest",
    "DeleteUserListRequest",
    "Destination",
    "DeviceInfo",
    "Encoding",
    "EncryptedUserId",
    "EncryptionInfo",
    "ErrorCount",
    "ErrorInfo",
    "ErrorReason",
    "Event",
    "EventLocation",
    "EventParameter",
    "EventSource",
    "ExperimentalField",
    "FeatureSet",
    "FieldWarning",
    "GcpWrappedKeyInfo",
    "Gender",
    "GetUserListDirectLicenseRequest",
    "GetUserListGlobalLicenseRequest",
    "GetUserListRequest",
    "GoogleUserIdData",
    "IngestAdEventsRequest",
    "IngestAdEventsResponse",
    "IngestAudienceMembersRequest",
    "IngestAudienceMembersResponse",
    "IngestEventsRequest",
    "IngestEventsResponse",
    "IngestUsersRequest",
    "IngestUsersResponse",
    "IngestedUserListInfo",
    "IngestionServiceClient",
    "IpData",
    "Item",
    "ItemCustomVariable",
    "ItemParameter",
    "ListUserListDirectLicensesRequest",
    "ListUserListDirectLicensesResponse",
    "ListUserListGlobalLicenseCustomerInfosRequest",
    "ListUserListGlobalLicenseCustomerInfosResponse",
    "ListUserListGlobalLicensesRequest",
    "ListUserListGlobalLicensesResponse",
    "ListUserListsRequest",
    "ListUserListsResponse",
    "MarketingDataInsightsServiceClient",
    "MatchRateRange",
    "MediaQuartile",
    "MobileData",
    "MobileIdInfo",
    "PairData",
    "PairIdInfo",
    "PartnerAudienceInfo",
    "PartnerCustomerAccount",
    "PartnerLink",
    "PartnerLinkMetadata",
    "PartnerLinkServiceClient",
    "PartnerProvidedIdData",
    "Platform",
    "PlatformType",
    "PpidData",
    "ProcessingErrorReason",
    "ProcessingWarningReason",
    "Product",
    "ProductAccount",
    "PseudonymousIdInfo",
    "RemoveAllAudienceMembersRequest",
    "RemoveAllAudienceMembersResponse",
    "RemoveAudienceMembersRequest",
    "RemoveAudienceMembersResponse",
    "RemoveUsersRequest",
    "RemoveUsersResponse",
    "RequestStatusPerDestination",
    "RetrieveInsightsRequest",
    "RetrieveInsightsResponse",
    "RetrieveRequestStatusRequest",
    "RetrieveRequestStatusResponse",
    "SearchPartnerLinksRequest",
    "SearchPartnerLinksResponse",
    "SizeInfo",
    "TargetNetworkInfo",
    "TargetingType",
    "TermsOfService",
    "TermsOfServiceStatus",
    "UpdateUserListDirectLicenseRequest",
    "UpdateUserListGlobalLicenseRequest",
    "UpdateUserListRequest",
    "User",
    "UserData",
    "UserIdData",
    "UserIdInfo",
    "UserIdentifier",
    "UserList",
    "UserListDirectLicense",
    "UserListDirectLicenseServiceClient",
    "UserListGlobalLicense",
    "UserListGlobalLicenseCustomerInfo",
    "UserListGlobalLicenseServiceClient",
    "UserListGlobalLicenseType",
    "UserListLicenseClientAccountType",
    "UserListLicenseMetrics",
    "UserListLicensePricing",
    "UserListLicenseStatus",
    "UserListServiceClient",
    "UserProperties",
    "UserProperty",
    "ViewType",
    "ViewabilityInfo",
    "WarningCount",
    "WarningInfo",
    "WarningReason",
)

api_core.check_python_version("google.ads.datamanager_v1")
api_core.check_dependency_versions("google.ads.datamanager_v1")
