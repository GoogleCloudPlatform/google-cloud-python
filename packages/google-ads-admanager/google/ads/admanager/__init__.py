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
from google.ads.admanager import gapic_version as package_version

__version__ = package_version.__version__


from google.ads.admanager_v1.services.ad_break_service.client import (
    AdBreakServiceClient,
)
from google.ads.admanager_v1.services.ad_review_center_ad_service.client import (
    AdReviewCenterAdServiceClient,
)
from google.ads.admanager_v1.services.ad_rule_service.client import AdRuleServiceClient
from google.ads.admanager_v1.services.ad_spot_service.client import AdSpotServiceClient
from google.ads.admanager_v1.services.ad_unit_service.client import AdUnitServiceClient
from google.ads.admanager_v1.services.application_service.client import (
    ApplicationServiceClient,
)
from google.ads.admanager_v1.services.audience_segment_service.client import (
    AudienceSegmentServiceClient,
)
from google.ads.admanager_v1.services.bandwidth_group_service.client import (
    BandwidthGroupServiceClient,
)
from google.ads.admanager_v1.services.break_template_service.client import (
    BreakTemplateServiceClient,
)
from google.ads.admanager_v1.services.browser_language_service.client import (
    BrowserLanguageServiceClient,
)
from google.ads.admanager_v1.services.browser_service.client import BrowserServiceClient
from google.ads.admanager_v1.services.cdn_config_service.client import (
    CdnConfigServiceClient,
)
from google.ads.admanager_v1.services.child_publisher_service.client import (
    ChildPublisherServiceClient,
)
from google.ads.admanager_v1.services.cms_metadata_key_service.client import (
    CmsMetadataKeyServiceClient,
)
from google.ads.admanager_v1.services.cms_metadata_value_service.client import (
    CmsMetadataValueServiceClient,
)
from google.ads.admanager_v1.services.company_service.client import CompanyServiceClient
from google.ads.admanager_v1.services.contact_service.client import ContactServiceClient
from google.ads.admanager_v1.services.content_bundle_service.client import (
    ContentBundleServiceClient,
)
from google.ads.admanager_v1.services.content_label_service.client import (
    ContentLabelServiceClient,
)
from google.ads.admanager_v1.services.content_service.client import ContentServiceClient
from google.ads.admanager_v1.services.creative_service.client import (
    CreativeServiceClient,
)
from google.ads.admanager_v1.services.creative_set_service.client import (
    CreativeSetServiceClient,
)
from google.ads.admanager_v1.services.creative_template_service.client import (
    CreativeTemplateServiceClient,
)
from google.ads.admanager_v1.services.creative_wrapper_service.client import (
    CreativeWrapperServiceClient,
)
from google.ads.admanager_v1.services.custom_field_service.client import (
    CustomFieldServiceClient,
)
from google.ads.admanager_v1.services.custom_targeting_key_service.client import (
    CustomTargetingKeyServiceClient,
)
from google.ads.admanager_v1.services.custom_targeting_value_service.client import (
    CustomTargetingValueServiceClient,
)
from google.ads.admanager_v1.services.dai_authentication_key_service.client import (
    DaiAuthenticationKeyServiceClient,
)
from google.ads.admanager_v1.services.dai_encoding_profile_service.client import (
    DaiEncodingProfileServiceClient,
)
from google.ads.admanager_v1.services.dai_session_service.client import (
    DaiSessionServiceClient,
)
from google.ads.admanager_v1.services.device_capability_service.client import (
    DeviceCapabilityServiceClient,
)
from google.ads.admanager_v1.services.device_category_service.client import (
    DeviceCategoryServiceClient,
)
from google.ads.admanager_v1.services.device_manufacturer_service.client import (
    DeviceManufacturerServiceClient,
)
from google.ads.admanager_v1.services.entity_signals_mapping_service.client import (
    EntitySignalsMappingServiceClient,
)
from google.ads.admanager_v1.services.forecast_service.client import (
    ForecastServiceClient,
)
from google.ads.admanager_v1.services.geo_target_service.client import (
    GeoTargetServiceClient,
)
from google.ads.admanager_v1.services.label_service.client import LabelServiceClient
from google.ads.admanager_v1.services.line_item_creative_association_service.client import (
    LineItemCreativeAssociationServiceClient,
)
from google.ads.admanager_v1.services.line_item_service.client import (
    LineItemServiceClient,
)
from google.ads.admanager_v1.services.line_item_template_service.client import (
    LineItemTemplateServiceClient,
)
from google.ads.admanager_v1.services.linked_device_service.client import (
    LinkedDeviceServiceClient,
)
from google.ads.admanager_v1.services.live_stream_service.client import (
    LiveStreamServiceClient,
)
from google.ads.admanager_v1.services.mcm_earnings_service.client import (
    McmEarningsServiceClient,
)
from google.ads.admanager_v1.services.mobile_carrier_service.client import (
    MobileCarrierServiceClient,
)
from google.ads.admanager_v1.services.mobile_device_service.client import (
    MobileDeviceServiceClient,
)
from google.ads.admanager_v1.services.mobile_device_submodel_service.client import (
    MobileDeviceSubmodelServiceClient,
)
from google.ads.admanager_v1.services.native_style_service.client import (
    NativeStyleServiceClient,
)
from google.ads.admanager_v1.services.network_service.client import NetworkServiceClient
from google.ads.admanager_v1.services.operating_system_service.client import (
    OperatingSystemServiceClient,
)
from google.ads.admanager_v1.services.operating_system_version_service.client import (
    OperatingSystemVersionServiceClient,
)
from google.ads.admanager_v1.services.order_service.client import OrderServiceClient
from google.ads.admanager_v1.services.partner_service.client import PartnerServiceClient
from google.ads.admanager_v1.services.placement_service.client import (
    PlacementServiceClient,
)
from google.ads.admanager_v1.services.private_auction_deal_service.client import (
    PrivateAuctionDealServiceClient,
)
from google.ads.admanager_v1.services.private_auction_service.client import (
    PrivateAuctionServiceClient,
)
from google.ads.admanager_v1.services.programmatic_buyer_service.client import (
    ProgrammaticBuyerServiceClient,
)
from google.ads.admanager_v1.services.report_service.client import ReportServiceClient
from google.ads.admanager_v1.services.rich_media_ads_company_service.client import (
    RichMediaAdsCompanyServiceClient,
)
from google.ads.admanager_v1.services.role_service.client import RoleServiceClient
from google.ads.admanager_v1.services.site_service.client import SiteServiceClient
from google.ads.admanager_v1.services.slate_service.client import SlateServiceClient
from google.ads.admanager_v1.services.suggested_ad_unit_service.client import (
    SuggestedAdUnitServiceClient,
)
from google.ads.admanager_v1.services.targeting_preset_service.client import (
    TargetingPresetServiceClient,
)
from google.ads.admanager_v1.services.taxonomy_category_service.client import (
    TaxonomyCategoryServiceClient,
)
from google.ads.admanager_v1.services.team_service.client import TeamServiceClient
from google.ads.admanager_v1.services.third_party_company_service.client import (
    ThirdPartyCompanyServiceClient,
)
from google.ads.admanager_v1.services.user_service.client import UserServiceClient
from google.ads.admanager_v1.services.viewability_provider_service.client import (
    ViewabilityProviderServiceClient,
)
from google.ads.admanager_v1.types.ad_break_messages import AdBreak
from google.ads.admanager_v1.types.ad_break_optimization_type_enum import (
    AdBreakOptimizationTypeEnum,
)
from google.ads.admanager_v1.types.ad_break_service import (
    CreateAdBreakRequest,
    DeleteAdBreakRequest,
    GetAdBreakRequest,
    ListAdBreaksRequest,
    ListAdBreaksResponse,
    UpdateAdBreakRequest,
)
from google.ads.admanager_v1.types.ad_review_center_ad_enums import (
    AdReviewCenterAdStatusEnum,
    ArcCreativeFormatEnum,
    ManualAdReviewCenterAdStatusEnum,
)
from google.ads.admanager_v1.types.ad_review_center_ad_messages import AdReviewCenterAd
from google.ads.admanager_v1.types.ad_review_center_ad_service import (
    BatchAdReviewCenterAdsOperationMetadata,
    BatchAllowAdReviewCenterAdsRequest,
    BatchAllowAdReviewCenterAdsResponse,
    BatchApplyAdReviewCenterCustomLabelsRequest,
    BatchApplyAdReviewCenterCustomLabelsResponse,
    BatchBlockAdReviewCenterAdsRequest,
    BatchBlockAdReviewCenterAdsResponse,
    FetchAdReviewCenterCustomLabelsRequest,
    FetchAdReviewCenterCustomLabelsResponse,
    SearchAdReviewCenterAdsRequest,
    SearchAdReviewCenterAdsResponse,
)
from google.ads.admanager_v1.types.ad_rule_enums import (
    AdRuleFrequencyCapBehaviorEnum,
    AdRuleStatusEnum,
)
from google.ads.admanager_v1.types.ad_rule_fill_order_direction_enum import (
    AdRuleFillOrderDirectionEnum,
)
from google.ads.admanager_v1.types.ad_rule_messages import AdRule, AdRuleSlot
from google.ads.admanager_v1.types.ad_rule_service import (
    BatchActivateAdRulesRequest,
    BatchActivateAdRulesResponse,
    BatchCreateAdRulesRequest,
    BatchCreateAdRulesResponse,
    BatchDeactivateAdRulesRequest,
    BatchDeactivateAdRulesResponse,
    BatchDeleteAdRulesRequest,
    BatchUpdateAdRulesRequest,
    BatchUpdateAdRulesResponse,
    CreateAdRuleRequest,
    GetAdRuleRequest,
    ListAdRulesRequest,
    ListAdRulesResponse,
    UpdateAdRuleRequest,
)
from google.ads.admanager_v1.types.ad_rule_slot_behavior_enum import (
    AdRuleSlotBehaviorEnum,
)
from google.ads.admanager_v1.types.ad_rule_slot_bumper_enum import AdRuleSlotBumperEnum
from google.ads.admanager_v1.types.ad_rule_slot_midroll_frequency_type_enum import (
    AdRuleSlotMidrollFrequencyTypeEnum,
)
from google.ads.admanager_v1.types.ad_spot_fill_type_enum import AdSpotFillTypeEnum
from google.ads.admanager_v1.types.ad_spot_messages import AdSpot
from google.ads.admanager_v1.types.ad_spot_service import (
    BatchCreateAdSpotsRequest,
    BatchCreateAdSpotsResponse,
    BatchUpdateAdSpotsRequest,
    BatchUpdateAdSpotsResponse,
    CreateAdSpotRequest,
    GetAdSpotRequest,
    ListAdSpotsRequest,
    ListAdSpotsResponse,
    UpdateAdSpotRequest,
)
from google.ads.admanager_v1.types.ad_spot_targeting_type_enum import (
    AdSpotTargetingTypeEnum,
)
from google.ads.admanager_v1.types.ad_unit_enums import (
    AdUnitStatusEnum,
    RefreshRateTypeEnum,
    SmartSizeModeEnum,
    TargetWindowEnum,
)
from google.ads.admanager_v1.types.ad_unit_messages import (
    AdUnit,
    AdUnitParent,
    AdUnitSize,
    LabelFrequencyCap,
)
from google.ads.admanager_v1.types.ad_unit_service import (
    BatchActivateAdUnitsRequest,
    BatchActivateAdUnitsResponse,
    BatchArchiveAdUnitsRequest,
    BatchArchiveAdUnitsResponse,
    BatchCreateAdUnitsRequest,
    BatchCreateAdUnitsResponse,
    BatchDeactivateAdUnitsRequest,
    BatchDeactivateAdUnitsResponse,
    BatchUpdateAdUnitsRequest,
    BatchUpdateAdUnitsResponse,
    CreateAdUnitRequest,
    GetAdUnitRequest,
    ListAdUnitSizesRequest,
    ListAdUnitSizesResponse,
    ListAdUnitsRequest,
    ListAdUnitsResponse,
    UpdateAdUnitRequest,
)
from google.ads.admanager_v1.types.admanager_error import AdManagerError
from google.ads.admanager_v1.types.application_enums import (
    ApplicationApprovalStatusEnum,
    ApplicationPlatformEnum,
    ApplicationStoreEnum,
    WebviewClaimingStatusEnum,
)
from google.ads.admanager_v1.types.application_messages import Application
from google.ads.admanager_v1.types.application_service import (
    BatchArchiveApplicationsRequest,
    BatchArchiveApplicationsResponse,
    BatchCreateApplicationsRequest,
    BatchCreateApplicationsResponse,
    BatchUnarchiveApplicationsRequest,
    BatchUnarchiveApplicationsResponse,
    BatchUpdateApplicationsRequest,
    BatchUpdateApplicationsResponse,
    CreateApplicationRequest,
    GetApplicationRequest,
    ListApplicationsRequest,
    ListApplicationsResponse,
    UpdateApplicationRequest,
)
from google.ads.admanager_v1.types.applied_label import AppliedLabel
from google.ads.admanager_v1.types.asset_enums import AssetImageDensityEnum
from google.ads.admanager_v1.types.asset_messages import Asset
from google.ads.admanager_v1.types.audience_segment_enums import (
    AudienceSegmentApprovalStatusEnum,
    AudienceSegmentLicenseTypeEnum,
    AudienceSegmentStatusEnum,
    AudienceSegmentTypeEnum,
)
from google.ads.admanager_v1.types.audience_segment_messages import AudienceSegment
from google.ads.admanager_v1.types.audience_segment_service import (
    BatchActivateAudienceSegmentsRequest,
    BatchActivateAudienceSegmentsResponse,
    BatchApproveAudienceSegmentsRequest,
    BatchApproveAudienceSegmentsResponse,
    BatchCreateAudienceSegmentsRequest,
    BatchCreateAudienceSegmentsResponse,
    BatchDeactivateAudienceSegmentsRequest,
    BatchDeactivateAudienceSegmentsResponse,
    BatchPopulateAudienceSegmentsRequest,
    BatchPopulateAudienceSegmentsResponse,
    BatchRejectAudienceSegmentsRequest,
    BatchRejectAudienceSegmentsResponse,
    BatchUpdateAudienceSegmentsRequest,
    BatchUpdateAudienceSegmentsResponse,
    CreateAudienceSegmentRequest,
    GetAudienceSegmentRequest,
    ListAudienceSegmentsRequest,
    ListAudienceSegmentsResponse,
    UpdateAudienceSegmentRequest,
)
from google.ads.admanager_v1.types.bandwidth_group_messages import BandwidthGroup
from google.ads.admanager_v1.types.bandwidth_group_service import (
    GetBandwidthGroupRequest,
    ListBandwidthGroupsRequest,
    ListBandwidthGroupsResponse,
)
from google.ads.admanager_v1.types.brand_lift_partner_enum import BrandLiftPartnerEnum
from google.ads.admanager_v1.types.break_template_messages import (
    BreakTemplate,
    BreakTemplateMember,
)
from google.ads.admanager_v1.types.break_template_service import (
    BatchCreateBreakTemplatesRequest,
    BatchCreateBreakTemplatesResponse,
    BatchUpdateBreakTemplatesRequest,
    BatchUpdateBreakTemplatesResponse,
    CreateBreakTemplateRequest,
    GetBreakTemplateRequest,
    ListBreakTemplatesRequest,
    ListBreakTemplatesResponse,
    UpdateBreakTemplateRequest,
)
from google.ads.admanager_v1.types.browser_language_messages import BrowserLanguage
from google.ads.admanager_v1.types.browser_language_service import (
    GetBrowserLanguageRequest,
    ListBrowserLanguagesRequest,
    ListBrowserLanguagesResponse,
)
from google.ads.admanager_v1.types.browser_messages import Browser
from google.ads.admanager_v1.types.browser_service import (
    GetBrowserRequest,
    ListBrowsersRequest,
    ListBrowsersResponse,
)
from google.ads.admanager_v1.types.cdn_config_messages import (
    AdMediaDeliveryConfig,
    CdnConfig,
    CdnSecurityPolicy,
    MediaLocation,
    SourceContentConfig,
)
from google.ads.admanager_v1.types.cdn_config_service import (
    BatchActivateCdnConfigsRequest,
    BatchActivateCdnConfigsResponse,
    BatchArchiveCdnConfigsRequest,
    BatchArchiveCdnConfigsResponse,
    BatchCreateCdnConfigsRequest,
    BatchCreateCdnConfigsResponse,
    BatchUpdateCdnConfigsRequest,
    BatchUpdateCdnConfigsResponse,
    CreateCdnConfigRequest,
    GetCdnConfigRequest,
    ListCdnConfigsRequest,
    ListCdnConfigsResponse,
    UpdateCdnConfigRequest,
)
from google.ads.admanager_v1.types.cdn_config_status_enum import CdnConfigStatusEnum
from google.ads.admanager_v1.types.cdn_config_type_enum import CdnConfigTypeEnum
from google.ads.admanager_v1.types.cdn_security_policy_enum import (
    CdnSecurityPolicyTypeEnum,
)
from google.ads.admanager_v1.types.cdn_security_policy_origin_forwarding_enum import (
    CdnSecurityPolicyOriginForwardingEnum,
)
from google.ads.admanager_v1.types.child_content_eligibility_enum import (
    ChildContentEligibilityEnum,
)
from google.ads.admanager_v1.types.child_publisher_messages import ChildPublisher
from google.ads.admanager_v1.types.child_publisher_service import (
    BatchCreateChildPublishersRequest,
    BatchCreateChildPublishersResponse,
    BatchRejectChildPublishersRequest,
    BatchRejectChildPublishersResponse,
    BatchRenegotiateChildPublisherAgreementsRequest,
    BatchRenegotiateChildPublisherAgreementsResponse,
    BatchResendChildPublisherInvitationEmailsRequest,
    BatchResendChildPublisherInvitationEmailsResponse,
    BatchUpdateChildPublishersRequest,
    BatchUpdateChildPublishersResponse,
    BatchWithdrawChildPublishersRequest,
    BatchWithdrawChildPublishersResponse,
    CreateChildPublisherRequest,
    GetChildPublisherRequest,
    ListChildPublishersRequest,
    ListChildPublishersResponse,
    RenegotiateChildPublisherAgreementRequest,
    UpdateChildPublisherRequest,
)
from google.ads.admanager_v1.types.cms_metadata_key_enums import (
    CmsMetadataKeyStatusEnum,
)
from google.ads.admanager_v1.types.cms_metadata_key_messages import CmsMetadataKey
from google.ads.admanager_v1.types.cms_metadata_key_service import (
    BatchActivateCmsMetadataKeysRequest,
    BatchActivateCmsMetadataKeysResponse,
    BatchDeactivateCmsMetadataKeysRequest,
    BatchDeactivateCmsMetadataKeysResponse,
    GetCmsMetadataKeyRequest,
    ListCmsMetadataKeysRequest,
    ListCmsMetadataKeysResponse,
)
from google.ads.admanager_v1.types.cms_metadata_value_enums import (
    CmsMetadataValueStatusEnum,
)
from google.ads.admanager_v1.types.cms_metadata_value_messages import CmsMetadataValue
from google.ads.admanager_v1.types.cms_metadata_value_service import (
    BatchActivateCmsMetadataValuesRequest,
    BatchActivateCmsMetadataValuesResponse,
    BatchDeactivateCmsMetadataValuesRequest,
    BatchDeactivateCmsMetadataValuesResponse,
    GetCmsMetadataValueRequest,
    ListCmsMetadataValuesRequest,
    ListCmsMetadataValuesResponse,
)
from google.ads.admanager_v1.types.company_enums import (
    CompanyCreditStatusEnum,
    CompanyTypeEnum,
)
from google.ads.admanager_v1.types.company_messages import Company
from google.ads.admanager_v1.types.company_service import (
    BatchCreateCompaniesRequest,
    BatchCreateCompaniesResponse,
    BatchUpdateCompaniesRequest,
    BatchUpdateCompaniesResponse,
    CreateCompanyRequest,
    GetCompanyRequest,
    ListCompaniesRequest,
    ListCompaniesResponse,
    UpdateCompanyRequest,
)
from google.ads.admanager_v1.types.contact_enums import ContactStatusEnum
from google.ads.admanager_v1.types.contact_messages import Contact
from google.ads.admanager_v1.types.contact_service import (
    BatchCreateContactsRequest,
    BatchCreateContactsResponse,
    BatchUpdateContactsRequest,
    BatchUpdateContactsResponse,
    CreateContactRequest,
    GetContactRequest,
    ListContactsRequest,
    ListContactsResponse,
    UpdateContactRequest,
)
from google.ads.admanager_v1.types.content_bundle_enums import ContentBundleStatusEnum
from google.ads.admanager_v1.types.content_bundle_messages import ContentBundle
from google.ads.admanager_v1.types.content_bundle_service import (
    BatchActivateContentBundlesRequest,
    BatchActivateContentBundlesResponse,
    BatchDeactivateContentBundlesRequest,
    BatchDeactivateContentBundlesResponse,
    GetContentBundleRequest,
    ListContentBundlesRequest,
    ListContentBundlesResponse,
)
from google.ads.admanager_v1.types.content_enums import (
    ContentStatusEnum,
    ContentStatusSourceEnum,
    DaiIngestErrorReasonEnum,
    DaiIngestStatusEnum,
)
from google.ads.admanager_v1.types.content_label_messages import ContentLabel
from google.ads.admanager_v1.types.content_label_service import (
    GetContentLabelRequest,
    ListContentLabelsRequest,
    ListContentLabelsResponse,
)
from google.ads.admanager_v1.types.content_messages import (
    CmsContent,
    Content,
    DaiIngestError,
)
from google.ads.admanager_v1.types.content_service import (
    GetContentRequest,
    ListContentRequest,
    ListContentResponse,
)
from google.ads.admanager_v1.types.conversion_event_enum import ConversionEventEnum
from google.ads.admanager_v1.types.creative_asset import ClickTag, CreativeAsset
from google.ads.admanager_v1.types.creative_enums import (
    CreativeDestinationUrlTypeEnum,
    CreativeLockedOrientationEnum,
    CreativeSslOverrideEnum,
    CreativeSslScanResultEnum,
    VastAdIdTypeEnum,
)
from google.ads.admanager_v1.types.creative_messages import (
    AdExchangeCreativeDetails,
    AdSenseCreativeDetails,
    AspectRatioImageCreativeDetails,
    AudioCreativeDetails,
    AudioRedirectCreativeDetails,
    BuyerPlacementConfig,
    ClickTrackingCreativeDetails,
    Creative,
    CustomCreativeDetails,
    Html5CreativeDetails,
    ImageCreativeDetails,
    ImageOverlayCreativeDetails,
    ImageRedirectCreativeDetails,
    ImageRedirectOverlayCreativeDetails,
    InternalRedirectCreativeDetails,
    LegacyDfpCreativeDetails,
    ProgrammaticCreativeDetails,
    RichMediaStudioCreativeDetails,
    SetTopBoxCreativeDetails,
    TemplateCreativeDetails,
    ThirdPartyCreativeDetails,
    VastInfo,
    VastRedirectCreativeDetails,
    VideoCreativeDetails,
    VideoRedirectCreativeDetails,
)
from google.ads.admanager_v1.types.creative_placeholder import (
    CreativePlaceholder,
    CreativePlaceholderCompanion,
)
from google.ads.admanager_v1.types.creative_service import (
    BatchActivateCreativesRequest,
    BatchActivateCreativesResponse,
    BatchDeactivateCreativesRequest,
    BatchDeactivateCreativesResponse,
    GetCreativeRequest,
    ListCreativesRequest,
    ListCreativesResponse,
)
from google.ads.admanager_v1.types.creative_set_messages import CreativeSet
from google.ads.admanager_v1.types.creative_set_service import (
    CreateCreativeSetRequest,
    GetCreativeSetRequest,
    ListCreativeSetsRequest,
    ListCreativeSetsResponse,
    UpdateCreativeSetRequest,
)
from google.ads.admanager_v1.types.creative_targeting import CreativeTargeting
from google.ads.admanager_v1.types.creative_template_enums import (
    CreativeTemplateStatusEnum,
    CreativeTemplateTypeEnum,
)
from google.ads.admanager_v1.types.creative_template_messages import (
    CreativeTemplate,
    CreativeTemplateVariable,
)
from google.ads.admanager_v1.types.creative_template_service import (
    GetCreativeTemplateRequest,
    ListCreativeTemplatesRequest,
    ListCreativeTemplatesResponse,
)
from google.ads.admanager_v1.types.creative_template_variable_url_type_enum import (
    CreativeTemplateVariableUrlTypeEnum,
)
from google.ads.admanager_v1.types.creative_third_party_data_declaration_status_enum import (
    CreativeThirdPartyDataDeclarationStatusEnum,
)
from google.ads.admanager_v1.types.creative_wrapper_enums import (
    CreativeWrapperOrderingEnum,
    CreativeWrapperStatusEnum,
    CreativeWrapperTypeEnum,
)
from google.ads.admanager_v1.types.creative_wrapper_messages import CreativeWrapper
from google.ads.admanager_v1.types.creative_wrapper_service import (
    BatchActivateCreativeWrappersRequest,
    BatchActivateCreativeWrappersResponse,
    BatchCreateCreativeWrappersRequest,
    BatchCreateCreativeWrappersResponse,
    BatchDeactivateCreativeWrappersRequest,
    BatchDeactivateCreativeWrappersResponse,
    BatchUpdateCreativeWrappersRequest,
    BatchUpdateCreativeWrappersResponse,
    CreateCreativeWrapperRequest,
    GetCreativeWrapperRequest,
    ListCreativeWrappersRequest,
    ListCreativeWrappersResponse,
    UpdateCreativeWrapperRequest,
)
from google.ads.admanager_v1.types.custom_creative_asset import CustomCreativeAsset
from google.ads.admanager_v1.types.custom_field_enums import (
    CustomFieldDataTypeEnum,
    CustomFieldEntityTypeEnum,
    CustomFieldStatusEnum,
    CustomFieldVisibilityEnum,
)
from google.ads.admanager_v1.types.custom_field_messages import (
    CustomField,
    CustomFieldOption,
)
from google.ads.admanager_v1.types.custom_field_service import (
    BatchActivateCustomFieldsRequest,
    BatchActivateCustomFieldsResponse,
    BatchCreateCustomFieldsRequest,
    BatchCreateCustomFieldsResponse,
    BatchDeactivateCustomFieldsRequest,
    BatchDeactivateCustomFieldsResponse,
    BatchUpdateCustomFieldsRequest,
    BatchUpdateCustomFieldsResponse,
    CreateCustomFieldRequest,
    GetCustomFieldRequest,
    ListCustomFieldsRequest,
    ListCustomFieldsResponse,
    UpdateCustomFieldRequest,
)
from google.ads.admanager_v1.types.custom_field_value import CustomFieldValue
from google.ads.admanager_v1.types.custom_pacing_curve import (
    CustomPacingCurve,
    CustomPacingGoal,
)
from google.ads.admanager_v1.types.custom_pacing_goal_unit_enum import (
    CustomPacingGoalUnitEnum,
)
from google.ads.admanager_v1.types.custom_targeting_key_enums import (
    CustomTargetingKeyReportableTypeEnum,
    CustomTargetingKeyStatusEnum,
    CustomTargetingKeyTypeEnum,
)
from google.ads.admanager_v1.types.custom_targeting_key_messages import (
    CustomTargetingKey,
)
from google.ads.admanager_v1.types.custom_targeting_key_service import (
    BatchActivateCustomTargetingKeysRequest,
    BatchActivateCustomTargetingKeysResponse,
    BatchCreateCustomTargetingKeysRequest,
    BatchCreateCustomTargetingKeysResponse,
    BatchDeactivateCustomTargetingKeysRequest,
    BatchDeactivateCustomTargetingKeysResponse,
    BatchUpdateCustomTargetingKeysRequest,
    BatchUpdateCustomTargetingKeysResponse,
    CreateCustomTargetingKeyRequest,
    GetCustomTargetingKeyRequest,
    ListCustomTargetingKeysRequest,
    ListCustomTargetingKeysResponse,
    UpdateCustomTargetingKeyRequest,
)
from google.ads.admanager_v1.types.custom_targeting_value_enums import (
    CustomTargetingValueMatchTypeEnum,
    CustomTargetingValueStatusEnum,
)
from google.ads.admanager_v1.types.custom_targeting_value_messages import (
    CustomTargetingValue,
)
from google.ads.admanager_v1.types.custom_targeting_value_service import (
    ActivateCustomTargetingValueRequest,
    BatchActivateCustomTargetingValuesRequest,
    BatchActivateCustomTargetingValuesResponse,
    BatchCreateCustomTargetingValuesRequest,
    BatchCreateCustomTargetingValuesResponse,
    BatchDeactivateCustomTargetingValuesRequest,
    BatchDeactivateCustomTargetingValuesResponse,
    BatchUpdateCustomTargetingValuesRequest,
    BatchUpdateCustomTargetingValuesResponse,
    CreateCustomTargetingValueRequest,
    DeactivateCustomTargetingValueRequest,
    GetCustomTargetingValueRequest,
    ListCustomTargetingValuesRequest,
    ListCustomTargetingValuesResponse,
    UpdateCustomTargetingValueRequest,
)
from google.ads.admanager_v1.types.dai_authentication_key_enums import (
    DaiAuthenticationKeyStatusEnum,
    DaiAuthenticationKeyTypeEnum,
)
from google.ads.admanager_v1.types.dai_authentication_key_messages import (
    DaiAuthenticationKey,
)
from google.ads.admanager_v1.types.dai_authentication_key_service import (
    BatchActivateDaiAuthenticationKeysRequest,
    BatchActivateDaiAuthenticationKeysResponse,
    BatchCreateDaiAuthenticationKeysRequest,
    BatchCreateDaiAuthenticationKeysResponse,
    BatchDeactivateDaiAuthenticationKeysRequest,
    BatchDeactivateDaiAuthenticationKeysResponse,
    BatchUpdateDaiAuthenticationKeysRequest,
    BatchUpdateDaiAuthenticationKeysResponse,
    CreateDaiAuthenticationKeyRequest,
    GetDaiAuthenticationKeyRequest,
    ListDaiAuthenticationKeysRequest,
    ListDaiAuthenticationKeysResponse,
    UpdateDaiAuthenticationKeyRequest,
)
from google.ads.admanager_v1.types.dai_encoding_profile_enums import (
    ContainerTypeEnum,
    DaiEncodingProfileStatusEnum,
    DaiEncodingProfileVariantTypeEnum,
)
from google.ads.admanager_v1.types.dai_encoding_profile_messages import (
    AudioSettings,
    DaiEncodingProfile,
    VideoSettings,
)
from google.ads.admanager_v1.types.dai_encoding_profile_service import (
    ActivateDaiEncodingProfileRequest,
    ArchiveDaiEncodingProfileRequest,
    BatchActivateDaiEncodingProfilesRequest,
    BatchActivateDaiEncodingProfilesResponse,
    BatchArchiveDaiEncodingProfilesRequest,
    BatchArchiveDaiEncodingProfilesResponse,
    BatchCreateDaiEncodingProfilesRequest,
    BatchCreateDaiEncodingProfilesResponse,
    BatchUpdateDaiEncodingProfilesRequest,
    BatchUpdateDaiEncodingProfilesResponse,
    CreateDaiEncodingProfileRequest,
    GetDaiEncodingProfileRequest,
    ListDaiEncodingProfilesRequest,
    ListDaiEncodingProfilesResponse,
    UpdateDaiEncodingProfileRequest,
)
from google.ads.admanager_v1.types.dai_session_enums import (
    AdBreakFindingTypeEnum,
    AdRequestFindingTypeEnum,
    AdResponseTypeEnum,
    BreakTypeEnum,
    CreativeFindingTypeEnum,
    CreativeIdTypeEnum,
    PodFindingTypeEnum,
    PrefetchStageTypeEnum,
    ReportingTypeEnum,
    SessionFindingSeverityEnum,
    SlateFindingTypeEnum,
    StitchingTypeEnum,
    TrackingPingFindingTypeEnum,
)
from google.ads.admanager_v1.types.dai_session_messages import DaiSession
from google.ads.admanager_v1.types.dai_session_service import GetDaiSessionRequest
from google.ads.admanager_v1.types.date_range import DateRange
from google.ads.admanager_v1.types.deal_buyer_permission_type_enum import (
    DealBuyerPermissionTypeEnum,
)
from google.ads.admanager_v1.types.deal_priority_tier_enum import DealPriorityTierEnum
from google.ads.admanager_v1.types.delivery_enums import (
    CompanionDeliveryOptionEnum,
    CreativeRotationTypeEnum,
    LineItemDeliveryRateTypeEnum,
    RoadblockingTypeEnum,
)
from google.ads.admanager_v1.types.delivery_indicator import DeliveryIndicator
from google.ads.admanager_v1.types.device_capability_messages import DeviceCapability
from google.ads.admanager_v1.types.device_capability_service import (
    GetDeviceCapabilityRequest,
    ListDeviceCapabilitiesRequest,
    ListDeviceCapabilitiesResponse,
)
from google.ads.admanager_v1.types.device_category_messages import DeviceCategory
from google.ads.admanager_v1.types.device_category_service import (
    GetDeviceCategoryRequest,
    ListDeviceCategoriesRequest,
    ListDeviceCategoriesResponse,
)
from google.ads.admanager_v1.types.device_manufacturer_messages import (
    DeviceManufacturer,
)
from google.ads.admanager_v1.types.device_manufacturer_service import (
    GetDeviceManufacturerRequest,
    ListDeviceManufacturersRequest,
    ListDeviceManufacturersResponse,
)
from google.ads.admanager_v1.types.discount_type_enum import DiscountTypeEnum
from google.ads.admanager_v1.types.early_ad_break_notification_enums import (
    AdBreakStateEnum,
)
from google.ads.admanager_v1.types.entity_signals_mapping_messages import (
    EntitySignalsMapping,
)
from google.ads.admanager_v1.types.entity_signals_mapping_service import (
    BatchCreateEntitySignalsMappingsRequest,
    BatchCreateEntitySignalsMappingsResponse,
    BatchUpdateEntitySignalsMappingsRequest,
    BatchUpdateEntitySignalsMappingsResponse,
    CreateEntitySignalsMappingRequest,
    GetEntitySignalsMappingRequest,
    ListEntitySignalsMappingsRequest,
    ListEntitySignalsMappingsResponse,
    UpdateEntitySignalsMappingRequest,
)
from google.ads.admanager_v1.types.environment_type_enum import EnvironmentTypeEnum
from google.ads.admanager_v1.types.exchange_syndication_product_enum import (
    ExchangeSyndicationProductEnum,
)
from google.ads.admanager_v1.types.exclusion_scope_enum import ExclusionScopeEnum
from google.ads.admanager_v1.types.forecast_messages import (
    AlternativeUnitTypeForecast,
    AvailabilityForecast,
    AvailabilityForecastOptions,
    ContendingLineItem,
    DeliveryForecast,
    DeliveryForecastOptions,
    DeliveryForecastResult,
    ExistingLineItemList,
    ForecastBreakdown,
    ForecastBreakdownEntry,
    ForecastBreakdownOptions,
    ForecastBreakdownTarget,
    GrpDemographicBreakdown,
    LineItemDeliveryForecast,
    TargetingCriteriaBreakdown,
    TimeSeries,
)
from google.ads.admanager_v1.types.forecast_service import (
    RunAvailabilityForecastRequest,
    RunAvailabilityForecastResponse,
    RunDeliveryForecastRequest,
    RunDeliveryForecastResponse,
    RunTrafficDataRequest,
    RunTrafficDataResponse,
)
from google.ads.admanager_v1.types.forecasting_enums import (
    ForecastingGrpAgeEnum,
    ForecastingGrpGenderEnum,
    ForecastingGrpUnitEnum,
    ForecastingTargetingDimensionEnum,
)
from google.ads.admanager_v1.types.frequency_cap import FrequencyCap
from google.ads.admanager_v1.types.geo_target_messages import GeoTarget
from google.ads.admanager_v1.types.geo_target_service import (
    GetGeoTargetRequest,
    ListGeoTargetsRequest,
    ListGeoTargetsResponse,
)
from google.ads.admanager_v1.types.goal import Goal
from google.ads.admanager_v1.types.goal_enums import GoalTypeEnum, UnitTypeEnum
from google.ads.admanager_v1.types.grp_provider_enum import GrpProviderEnum
from google.ads.admanager_v1.types.grp_settings import GrpSettings
from google.ads.admanager_v1.types.grp_target_gender_enum import GrpTargetGenderEnum
from google.ads.admanager_v1.types.label_enums import LabelTypeEnum
from google.ads.admanager_v1.types.label_messages import Label
from google.ads.admanager_v1.types.label_service import (
    BatchActivateLabelsRequest,
    BatchActivateLabelsResponse,
    BatchCreateLabelsRequest,
    BatchCreateLabelsResponse,
    BatchDeactivateLabelsRequest,
    BatchDeactivateLabelsResponse,
    BatchUpdateLabelsRequest,
    BatchUpdateLabelsResponse,
    CreateLabelRequest,
    GetLabelRequest,
    ListLabelsRequest,
    ListLabelsResponse,
    UpdateLabelRequest,
)
from google.ads.admanager_v1.types.line_item_allowed_format_enum import (
    LineItemAllowedFormatEnum,
)
from google.ads.admanager_v1.types.line_item_creative_association_enums import (
    LineItemCreativeAssociationStatusEnum,
)
from google.ads.admanager_v1.types.line_item_creative_association_messages import (
    LineItemCreativeAssociation,
    LineItemCreativeAssociationStats,
)
from google.ads.admanager_v1.types.line_item_creative_association_service import (
    GetLineItemCreativeAssociationRequest,
    ListLineItemCreativeAssociationsRequest,
    ListLineItemCreativeAssociationsResponse,
)
from google.ads.admanager_v1.types.line_item_deal_info import LineItemDealInfo
from google.ads.admanager_v1.types.line_item_delivery_forecast_source_enum import (
    LineItemDeliveryForecastSourceEnum,
)
from google.ads.admanager_v1.types.line_item_discount import LineItemDiscount
from google.ads.admanager_v1.types.line_item_enums import (
    LineItemComputedStatusEnum,
    LineItemCostTypeEnum,
    LineItemReservationStatusEnum,
    LineItemTypeEnum,
)
from google.ads.admanager_v1.types.line_item_messages import LineItem
from google.ads.admanager_v1.types.line_item_service import (
    BatchActivateLineItemsRequest,
    BatchActivateLineItemsResponse,
    BatchArchiveLineItemsRequest,
    BatchArchiveLineItemsResponse,
    BatchCreateLineItemsRequest,
    BatchCreateLineItemsResponse,
    BatchDeleteLineItemsRequest,
    BatchPauseLineItemsRequest,
    BatchPauseLineItemsResponse,
    BatchReleaseLineItemsRequest,
    BatchReleaseLineItemsResponse,
    BatchReserveAndOverbookLineItemsRequest,
    BatchReserveAndOverbookLineItemsResponse,
    BatchReserveLineItemsRequest,
    BatchReserveLineItemsResponse,
    BatchResumeAndOverbookLineItemsRequest,
    BatchResumeAndOverbookLineItemsResponse,
    BatchResumeLineItemsRequest,
    BatchResumeLineItemsResponse,
    BatchUnarchiveLineItemsRequest,
    BatchUnarchiveLineItemsResponse,
    BatchUpdateLineItemsRequest,
    BatchUpdateLineItemsResponse,
    CreateLineItemRequest,
    GetLineItemRequest,
    ListLineItemsRequest,
    ListLineItemsResponse,
    UpdateLineItemRequest,
)
from google.ads.admanager_v1.types.line_item_stats import LineItemStats
from google.ads.admanager_v1.types.line_item_template_messages import LineItemTemplate
from google.ads.admanager_v1.types.line_item_template_service import (
    GetLineItemTemplateRequest,
    ListLineItemTemplatesRequest,
    ListLineItemTemplatesResponse,
)
from google.ads.admanager_v1.types.linked_device_enums import LinkedDeviceVisibilityEnum
from google.ads.admanager_v1.types.linked_device_messages import LinkedDevice
from google.ads.admanager_v1.types.linked_device_service import (
    GetLinkedDeviceRequest,
    ListLinkedDevicesRequest,
    ListLinkedDevicesResponse,
)
from google.ads.admanager_v1.types.live_stream_event_enums import (
    AdBreakFillTypeEnum,
    AdBreakMarkupTypeEnum,
    DynamicAdInsertionTypeEnum,
    HlsMasterPlaylistRefreshTypeEnum,
    HlsSettingsPlaylistTypeEnum,
    LiveStreamEventStatusEnum,
    LiveStreamEventStreamingFormatEnum,
    SlateStatusEnum,
)
from google.ads.admanager_v1.types.live_stream_event_messages import LiveStreamEvent
from google.ads.admanager_v1.types.live_stream_messages import (
    AuxiliaryAdSettings,
    DashBridge,
    HlsSettings,
    LiveStream,
    LiveStreamConditioning,
    MasterPlaylistSettings,
    PrefetchSettings,
    PrerollSettings,
)
from google.ads.admanager_v1.types.live_stream_service import (
    BatchActivateLiveStreamsRequest,
    BatchActivateLiveStreamsResponse,
    BatchArchiveLiveStreamsRequest,
    BatchArchiveLiveStreamsResponse,
    BatchCreateLiveStreamsRequest,
    BatchCreateLiveStreamsResponse,
    BatchPauseAdsLiveStreamsRequest,
    BatchPauseAdsLiveStreamsResponse,
    BatchPauseLiveStreamsRequest,
    BatchPauseLiveStreamsResponse,
    BatchRefreshMasterPlaylistsRequest,
    BatchRefreshMasterPlaylistsResponse,
    BatchUpdateLiveStreamsRequest,
    BatchUpdateLiveStreamsResponse,
    CreateLiveStreamRequest,
    GetLiveStreamRequest,
    ListLiveStreamsRequest,
    ListLiveStreamsResponse,
    UpdateLiveStreamRequest,
)
from google.ads.admanager_v1.types.mcm_earnings_messages import (
    EarningsProductBreakdown,
    McmEarnings,
)
from google.ads.admanager_v1.types.mcm_earnings_service import (
    FetchMcmEarningsRequest,
    FetchMcmEarningsResponse,
)
from google.ads.admanager_v1.types.mcm_enums import (
    ChildPublisherAddressVerificationStatusEnum,
    ChildPublisherIdentityVerificationStatusEnum,
    ChildPublisherOnboardingTaskEnum,
    DelegationAccountStatusEnum,
    DelegationApprovalStatusEnum,
    DelegationInvitationStatusEnum,
    DelegationTypeEnum,
    McmEarningsProductTypeEnum,
    McmReadinessStatusEnum,
)
from google.ads.admanager_v1.types.mobile_carrier_messages import MobileCarrier
from google.ads.admanager_v1.types.mobile_carrier_service import (
    GetMobileCarrierRequest,
    ListMobileCarriersRequest,
    ListMobileCarriersResponse,
)
from google.ads.admanager_v1.types.mobile_device_messages import MobileDevice
from google.ads.admanager_v1.types.mobile_device_service import (
    GetMobileDeviceRequest,
    ListMobileDevicesRequest,
    ListMobileDevicesResponse,
)
from google.ads.admanager_v1.types.mobile_device_submodel_messages import (
    MobileDeviceSubmodel,
)
from google.ads.admanager_v1.types.mobile_device_submodel_service import (
    GetMobileDeviceSubmodelRequest,
    ListMobileDeviceSubmodelsRequest,
    ListMobileDeviceSubmodelsResponse,
)
from google.ads.admanager_v1.types.native_style_enums import NativeStyleStatusEnum
from google.ads.admanager_v1.types.native_style_messages import NativeStyle
from google.ads.admanager_v1.types.native_style_service import (
    BatchActivateNativeStylesRequest,
    BatchActivateNativeStylesResponse,
    BatchArchiveNativeStylesRequest,
    BatchArchiveNativeStylesResponse,
    BatchCreateNativeStylesRequest,
    BatchCreateNativeStylesResponse,
    BatchDeactivateNativeStylesRequest,
    BatchDeactivateNativeStylesResponse,
    BatchUpdateNativeStylesRequest,
    BatchUpdateNativeStylesResponse,
    CreateNativeStyleRequest,
    GetNativeStyleRequest,
    ListNativeStylesRequest,
    ListNativeStylesResponse,
    UpdateNativeStyleRequest,
)
from google.ads.admanager_v1.types.network_messages import (
    DefaultThirdPartyDataDeclaration,
    Network,
)
from google.ads.admanager_v1.types.network_service import (
    GetDefaultThirdPartyDataDeclarationRequest,
    GetNetworkRequest,
    ListNetworksRequest,
    ListNetworksResponse,
    ProvisionTestNetworkRequest,
    UpdateNetworkRequest,
)
from google.ads.admanager_v1.types.nielsen_ctv_pacing_enum import NielsenCtvPacingEnum
from google.ads.admanager_v1.types.non_guaranteed_deal_priority import (
    NonGuaranteedDealPriority,
)
from google.ads.admanager_v1.types.operating_system_messages import OperatingSystem
from google.ads.admanager_v1.types.operating_system_service import (
    GetOperatingSystemRequest,
    ListOperatingSystemsRequest,
    ListOperatingSystemsResponse,
)
from google.ads.admanager_v1.types.operating_system_version_messages import (
    OperatingSystemVersion,
)
from google.ads.admanager_v1.types.operating_system_version_service import (
    GetOperatingSystemVersionRequest,
    ListOperatingSystemVersionsRequest,
    ListOperatingSystemVersionsResponse,
)
from google.ads.admanager_v1.types.order_enums import OrderStatusEnum
from google.ads.admanager_v1.types.order_messages import Order
from google.ads.admanager_v1.types.order_service import (
    BatchApproveAndOverbookOrdersRequest,
    BatchApproveAndOverbookOrdersResponse,
    BatchApproveOrdersRequest,
    BatchApproveOrdersResponse,
    BatchApproveOrdersWithoutReservationRequest,
    BatchApproveOrdersWithoutReservationResponse,
    BatchArchiveOrdersRequest,
    BatchArchiveOrdersResponse,
    BatchCreateOrdersRequest,
    BatchCreateOrdersResponse,
    BatchDeleteOrdersRequest,
    BatchDeleteOrdersResponse,
    BatchDisapproveOrdersRequest,
    BatchDisapproveOrdersResponse,
    BatchDisapproveOrdersWithoutReservationChangesRequest,
    BatchDisapproveOrdersWithoutReservationChangesResponse,
    BatchPauseOrdersRequest,
    BatchPauseOrdersResponse,
    BatchResumeAndOverbookOrdersRequest,
    BatchResumeAndOverbookOrdersResponse,
    BatchResumeOrdersRequest,
    BatchResumeOrdersResponse,
    BatchRetractOrdersRequest,
    BatchRetractOrdersResponse,
    BatchRetractOrdersWithoutReservationChangesRequest,
    BatchRetractOrdersWithoutReservationChangesResponse,
    BatchSubmitOrdersForApprovalAndOverbookRequest,
    BatchSubmitOrdersForApprovalAndOverbookResponse,
    BatchSubmitOrdersForApprovalRequest,
    BatchSubmitOrdersForApprovalResponse,
    BatchSubmitOrdersForApprovalWithoutReservationChangesRequest,
    BatchSubmitOrdersForApprovalWithoutReservationChangesResponse,
    BatchUnarchiveOrdersRequest,
    BatchUnarchiveOrdersResponse,
    BatchUpdateOrdersRequest,
    BatchUpdateOrdersResponse,
    CreateOrderRequest,
    GetOrderRequest,
    ListOrdersRequest,
    ListOrdersResponse,
    UpdateOrderRequest,
)
from google.ads.admanager_v1.types.pacing_device_categorization_enum import (
    PacingDeviceCategorizationEnum,
)
from google.ads.admanager_v1.types.partner_messages import Partner
from google.ads.admanager_v1.types.partner_service import (
    BatchUpdatePartnersRequest,
    BatchUpdatePartnersResponse,
    GetPartnerRequest,
    ListPartnersRequest,
    ListPartnersResponse,
    UpdatePartnerRequest,
)
from google.ads.admanager_v1.types.placement_enums import PlacementStatusEnum
from google.ads.admanager_v1.types.placement_messages import Placement
from google.ads.admanager_v1.types.placement_service import (
    BatchActivatePlacementsRequest,
    BatchActivatePlacementsResponse,
    BatchArchivePlacementsRequest,
    BatchArchivePlacementsResponse,
    BatchCreatePlacementsRequest,
    BatchCreatePlacementsResponse,
    BatchDeactivatePlacementsRequest,
    BatchDeactivatePlacementsResponse,
    BatchUpdatePlacementsRequest,
    BatchUpdatePlacementsResponse,
    CreatePlacementRequest,
    GetPlacementRequest,
    ListPlacementsRequest,
    ListPlacementsResponse,
    UpdatePlacementRequest,
)
from google.ads.admanager_v1.types.private_auction_deal_messages import (
    PrivateAuctionDeal,
)
from google.ads.admanager_v1.types.private_auction_deal_service import (
    CreatePrivateAuctionDealRequest,
    GetPrivateAuctionDealRequest,
    ListPrivateAuctionDealsRequest,
    ListPrivateAuctionDealsResponse,
    UpdatePrivateAuctionDealRequest,
)
from google.ads.admanager_v1.types.private_auction_messages import PrivateAuction
from google.ads.admanager_v1.types.private_auction_service import (
    CreatePrivateAuctionRequest,
    GetPrivateAuctionRequest,
    ListPrivateAuctionsRequest,
    ListPrivateAuctionsResponse,
    UpdatePrivateAuctionRequest,
)
from google.ads.admanager_v1.types.private_marketplace_enums import (
    PrivateMarketplaceDealStatusEnum,
)
from google.ads.admanager_v1.types.programmatic_buyer_messages import ProgrammaticBuyer
from google.ads.admanager_v1.types.programmatic_buyer_service import (
    GetProgrammaticBuyerRequest,
    ListProgrammaticBuyersRequest,
    ListProgrammaticBuyersResponse,
)
from google.ads.admanager_v1.types.reach_partner_enum import ReachPartnerEnum
from google.ads.admanager_v1.types.report_definition import ReportDefinition
from google.ads.admanager_v1.types.report_delivery import ScheduleOptions
from google.ads.admanager_v1.types.report_messages import Report, ReportDataTable
from google.ads.admanager_v1.types.report_service import (
    CreateReportRequest,
    FetchReportResultRowsRequest,
    FetchReportResultRowsResponse,
    GetReportRequest,
    ListReportsRequest,
    ListReportsResponse,
    RunReportMetadata,
    RunReportRequest,
    RunReportResponse,
    UpdateReportRequest,
)
from google.ads.admanager_v1.types.report_value import ReportValue
from google.ads.admanager_v1.types.report_visibility_enum import ReportVisibilityEnum
from google.ads.admanager_v1.types.request_platform_enum import RequestPlatformEnum
from google.ads.admanager_v1.types.rich_media_ads_company_enums import (
    RichMediaAdsCompanyGdprStatusEnum,
)
from google.ads.admanager_v1.types.rich_media_ads_company_messages import (
    RichMediaAdsCompany,
)
from google.ads.admanager_v1.types.rich_media_ads_company_service import (
    GetRichMediaAdsCompanyRequest,
    ListRichMediaAdsCompaniesRequest,
    ListRichMediaAdsCompaniesResponse,
)
from google.ads.admanager_v1.types.rich_media_studio_child_asset_type_enum import (
    RichMediaStudioChildAssetTypeEnum,
)
from google.ads.admanager_v1.types.rich_media_studio_creative_billing_attribute_enum import (
    RichMediaStudioCreativeBillingAttributeEnum,
)
from google.ads.admanager_v1.types.rich_media_studio_creative_format_enum import (
    RichMediaStudioCreativeFormatEnum,
)
from google.ads.admanager_v1.types.rich_media_studio_messages import (
    RichMediaStudioChildAssetProperty,
)
from google.ads.admanager_v1.types.role_enums import RoleStatusEnum
from google.ads.admanager_v1.types.role_messages import Role
from google.ads.admanager_v1.types.role_service import (
    GetRoleRequest,
    ListRolesRequest,
    ListRolesResponse,
)
from google.ads.admanager_v1.types.site_enums import (
    SiteApprovalStatusEnum,
    SiteDisapprovalReasonEnum,
)
from google.ads.admanager_v1.types.site_messages import DisapprovalReason, Site
from google.ads.admanager_v1.types.site_service import (
    BatchCreateSitesRequest,
    BatchCreateSitesResponse,
    BatchDeactivateSitesRequest,
    BatchDeactivateSitesResponse,
    BatchSubmitSitesForApprovalRequest,
    BatchSubmitSitesForApprovalResponse,
    BatchUpdateSitesRequest,
    BatchUpdateSitesResponse,
    CreateSiteRequest,
    GetSiteRequest,
    ListSitesRequest,
    ListSitesResponse,
    UpdateSiteRequest,
)
from google.ads.admanager_v1.types.size import Size
from google.ads.admanager_v1.types.size_type_enum import SizeTypeEnum
from google.ads.admanager_v1.types.skippable_ad_type_enum import SkippableAdTypeEnum
from google.ads.admanager_v1.types.slate_messages import Slate
from google.ads.admanager_v1.types.slate_service import (
    BatchArchiveSlatesRequest,
    BatchArchiveSlatesResponse,
    BatchCreateSlatesRequest,
    BatchCreateSlatesResponse,
    BatchUnarchiveSlatesRequest,
    BatchUnarchiveSlatesResponse,
    BatchUpdateSlatesRequest,
    BatchUpdateSlatesResponse,
    CreateSlateRequest,
    GetSlateRequest,
    ListSlatesRequest,
    ListSlatesResponse,
    UpdateSlateRequest,
)
from google.ads.admanager_v1.types.suggested_ad_unit_messages import SuggestedAdUnit
from google.ads.admanager_v1.types.suggested_ad_unit_service import (
    BatchApproveSuggestedAdUnitsRequest,
    BatchApproveSuggestedAdUnitsResponse,
    GetSuggestedAdUnitRequest,
    ListSuggestedAdUnitsRequest,
    ListSuggestedAdUnitsResponse,
)
from google.ads.admanager_v1.types.target_platform_enum import TargetPlatformEnum
from google.ads.admanager_v1.types.targeted_video_bumper_type_enum import (
    TargetedVideoBumperTypeEnum,
)
from google.ads.admanager_v1.types.targeting import (
    AdUnitTargeting,
    AudienceSegmentTargeting,
    BandwidthTargeting,
    BrowserLanguageTargeting,
    BrowserTargeting,
    CmsMetadataTargeting,
    ContentTargeting,
    CustomTargeting,
    CustomTargetingClause,
    CustomTargetingLiteral,
    DataSegmentTargeting,
    DeviceCapabilityTargeting,
    DeviceCategoryTargeting,
    DeviceManufacturerTargeting,
    FirstPartyMobileApplicationTargeting,
    GeoTargeting,
    InventoryTargeting,
    MobileApplicationTargeting,
    MobileCarrierTargeting,
    OperatingSystemTargeting,
    RequestFormatTargeting,
    RequestPlatformTargeting,
    Targeting,
    TechnologyTargeting,
    UserDomainTargeting,
    VideoPosition,
    VideoPositionTargeting,
)
from google.ads.admanager_v1.types.targeting_preset_enums import (
    TargetingPresetStatusEnum,
)
from google.ads.admanager_v1.types.targeting_preset_messages import TargetingPreset
from google.ads.admanager_v1.types.targeting_preset_service import (
    BatchCreateTargetingPresetsRequest,
    BatchCreateTargetingPresetsResponse,
    BatchDeactivateTargetingPresetsRequest,
    BatchDeactivateTargetingPresetsResponse,
    BatchUpdateTargetingPresetsRequest,
    BatchUpdateTargetingPresetsResponse,
    CreateTargetingPresetRequest,
    DeactivateTargetingPresetRequest,
    GetTargetingPresetRequest,
    ListTargetingPresetsRequest,
    ListTargetingPresetsResponse,
    UpdateTargetingPresetRequest,
)
from google.ads.admanager_v1.types.taxonomy_category_messages import TaxonomyCategory
from google.ads.admanager_v1.types.taxonomy_category_service import (
    GetTaxonomyCategoryRequest,
    ListTaxonomyCategoriesRequest,
    ListTaxonomyCategoriesResponse,
)
from google.ads.admanager_v1.types.taxonomy_type_enum import TaxonomyTypeEnum
from google.ads.admanager_v1.types.team_enums import TeamAccessTypeEnum, TeamStatusEnum
from google.ads.admanager_v1.types.team_messages import Team
from google.ads.admanager_v1.types.team_service import (
    BatchActivateTeamsRequest,
    BatchActivateTeamsResponse,
    BatchCreateTeamsRequest,
    BatchCreateTeamsResponse,
    BatchDeactivateTeamsRequest,
    BatchDeactivateTeamsResponse,
    BatchUpdateTeamsRequest,
    BatchUpdateTeamsResponse,
    CreateTeamRequest,
    GetTeamRequest,
    ListTeamsRequest,
    ListTeamsResponse,
    UpdateTeamRequest,
)
from google.ads.admanager_v1.types.third_party_company_enums import (
    ThirdPartyCompanyStatusEnum,
    ThirdPartyCompanyTypeEnum,
)
from google.ads.admanager_v1.types.third_party_company_messages import ThirdPartyCompany
from google.ads.admanager_v1.types.third_party_company_service import (
    GetThirdPartyCompanyRequest,
    ListThirdPartyCompaniesRequest,
    ListThirdPartyCompaniesResponse,
)
from google.ads.admanager_v1.types.third_party_data_declaration import (
    ThirdPartyDataDeclaration,
)
from google.ads.admanager_v1.types.third_party_data_declaration_type_enum import (
    ThirdPartyDataDeclarationTypeEnum,
)
from google.ads.admanager_v1.types.third_party_measurement_settings import (
    ThirdPartyMeasurementSettings,
)
from google.ads.admanager_v1.types.time_unit_enum import TimeUnitEnum
from google.ads.admanager_v1.types.user_messages import User
from google.ads.admanager_v1.types.user_service import (
    BatchActivateUsersRequest,
    BatchActivateUsersResponse,
    BatchCreateUsersRequest,
    BatchCreateUsersResponse,
    BatchDeactivateUsersRequest,
    BatchDeactivateUsersResponse,
    BatchUpdateUsersRequest,
    BatchUpdateUsersResponse,
    CreateUserRequest,
    GetUserRequest,
    ListUsersRequest,
    ListUsersResponse,
    UpdateUserRequest,
)
from google.ads.admanager_v1.types.vast_redirect_type_enum import VastRedirectTypeEnum
from google.ads.admanager_v1.types.video_position_enum import VideoPositionEnum
from google.ads.admanager_v1.types.video_tracking_url import VideoTrackingUrl
from google.ads.admanager_v1.types.video_transcode_status_enum import (
    VideoTranscodeStatusEnum,
)
from google.ads.admanager_v1.types.viewability_partner_enum import (
    ViewabilityPartnerEnum,
)
from google.ads.admanager_v1.types.viewability_provider_messages import (
    ViewabilityProvider,
)
from google.ads.admanager_v1.types.viewability_provider_service import (
    BatchCreateViewabilityProvidersRequest,
    BatchCreateViewabilityProvidersResponse,
    BatchUpdateViewabilityProvidersRequest,
    BatchUpdateViewabilityProvidersResponse,
    CreateViewabilityProviderRequest,
    GetViewabilityProviderRequest,
    ListViewabilityProvidersRequest,
    ListViewabilityProvidersResponse,
    UpdateViewabilityProviderRequest,
)
from google.ads.admanager_v1.types.web_property import WebProperty

__all__ = (
    "AdBreakServiceClient",
    "AdReviewCenterAdServiceClient",
    "AdRuleServiceClient",
    "AdSpotServiceClient",
    "AdUnitServiceClient",
    "ApplicationServiceClient",
    "AudienceSegmentServiceClient",
    "BandwidthGroupServiceClient",
    "BreakTemplateServiceClient",
    "BrowserLanguageServiceClient",
    "BrowserServiceClient",
    "CdnConfigServiceClient",
    "ChildPublisherServiceClient",
    "CmsMetadataKeyServiceClient",
    "CmsMetadataValueServiceClient",
    "CompanyServiceClient",
    "ContactServiceClient",
    "ContentBundleServiceClient",
    "ContentLabelServiceClient",
    "ContentServiceClient",
    "CreativeServiceClient",
    "CreativeSetServiceClient",
    "CreativeTemplateServiceClient",
    "CreativeWrapperServiceClient",
    "CustomFieldServiceClient",
    "CustomTargetingKeyServiceClient",
    "CustomTargetingValueServiceClient",
    "DaiAuthenticationKeyServiceClient",
    "DaiEncodingProfileServiceClient",
    "DaiSessionServiceClient",
    "DeviceCapabilityServiceClient",
    "DeviceCategoryServiceClient",
    "DeviceManufacturerServiceClient",
    "EntitySignalsMappingServiceClient",
    "ForecastServiceClient",
    "GeoTargetServiceClient",
    "LabelServiceClient",
    "LineItemCreativeAssociationServiceClient",
    "LineItemServiceClient",
    "LineItemTemplateServiceClient",
    "LinkedDeviceServiceClient",
    "LiveStreamServiceClient",
    "McmEarningsServiceClient",
    "MobileCarrierServiceClient",
    "MobileDeviceServiceClient",
    "MobileDeviceSubmodelServiceClient",
    "NativeStyleServiceClient",
    "NetworkServiceClient",
    "OperatingSystemServiceClient",
    "OperatingSystemVersionServiceClient",
    "OrderServiceClient",
    "PartnerServiceClient",
    "PlacementServiceClient",
    "PrivateAuctionDealServiceClient",
    "PrivateAuctionServiceClient",
    "ProgrammaticBuyerServiceClient",
    "ReportServiceClient",
    "RichMediaAdsCompanyServiceClient",
    "RoleServiceClient",
    "SiteServiceClient",
    "SlateServiceClient",
    "SuggestedAdUnitServiceClient",
    "TargetingPresetServiceClient",
    "TaxonomyCategoryServiceClient",
    "TeamServiceClient",
    "ThirdPartyCompanyServiceClient",
    "UserServiceClient",
    "ViewabilityProviderServiceClient",
    "AdBreak",
    "AdBreakOptimizationTypeEnum",
    "CreateAdBreakRequest",
    "DeleteAdBreakRequest",
    "GetAdBreakRequest",
    "ListAdBreaksRequest",
    "ListAdBreaksResponse",
    "UpdateAdBreakRequest",
    "AdReviewCenterAdStatusEnum",
    "ArcCreativeFormatEnum",
    "ManualAdReviewCenterAdStatusEnum",
    "AdReviewCenterAd",
    "BatchAdReviewCenterAdsOperationMetadata",
    "BatchAllowAdReviewCenterAdsRequest",
    "BatchAllowAdReviewCenterAdsResponse",
    "BatchApplyAdReviewCenterCustomLabelsRequest",
    "BatchApplyAdReviewCenterCustomLabelsResponse",
    "BatchBlockAdReviewCenterAdsRequest",
    "BatchBlockAdReviewCenterAdsResponse",
    "FetchAdReviewCenterCustomLabelsRequest",
    "FetchAdReviewCenterCustomLabelsResponse",
    "SearchAdReviewCenterAdsRequest",
    "SearchAdReviewCenterAdsResponse",
    "AdRuleFrequencyCapBehaviorEnum",
    "AdRuleStatusEnum",
    "AdRuleFillOrderDirectionEnum",
    "AdRule",
    "AdRuleSlot",
    "BatchActivateAdRulesRequest",
    "BatchActivateAdRulesResponse",
    "BatchCreateAdRulesRequest",
    "BatchCreateAdRulesResponse",
    "BatchDeactivateAdRulesRequest",
    "BatchDeactivateAdRulesResponse",
    "BatchDeleteAdRulesRequest",
    "BatchUpdateAdRulesRequest",
    "BatchUpdateAdRulesResponse",
    "CreateAdRuleRequest",
    "GetAdRuleRequest",
    "ListAdRulesRequest",
    "ListAdRulesResponse",
    "UpdateAdRuleRequest",
    "AdRuleSlotBehaviorEnum",
    "AdRuleSlotBumperEnum",
    "AdRuleSlotMidrollFrequencyTypeEnum",
    "AdSpotFillTypeEnum",
    "AdSpot",
    "BatchCreateAdSpotsRequest",
    "BatchCreateAdSpotsResponse",
    "BatchUpdateAdSpotsRequest",
    "BatchUpdateAdSpotsResponse",
    "CreateAdSpotRequest",
    "GetAdSpotRequest",
    "ListAdSpotsRequest",
    "ListAdSpotsResponse",
    "UpdateAdSpotRequest",
    "AdSpotTargetingTypeEnum",
    "AdUnitStatusEnum",
    "RefreshRateTypeEnum",
    "SmartSizeModeEnum",
    "TargetWindowEnum",
    "AdUnit",
    "AdUnitParent",
    "AdUnitSize",
    "LabelFrequencyCap",
    "BatchActivateAdUnitsRequest",
    "BatchActivateAdUnitsResponse",
    "BatchArchiveAdUnitsRequest",
    "BatchArchiveAdUnitsResponse",
    "BatchCreateAdUnitsRequest",
    "BatchCreateAdUnitsResponse",
    "BatchDeactivateAdUnitsRequest",
    "BatchDeactivateAdUnitsResponse",
    "BatchUpdateAdUnitsRequest",
    "BatchUpdateAdUnitsResponse",
    "CreateAdUnitRequest",
    "GetAdUnitRequest",
    "ListAdUnitSizesRequest",
    "ListAdUnitSizesResponse",
    "ListAdUnitsRequest",
    "ListAdUnitsResponse",
    "UpdateAdUnitRequest",
    "AdManagerError",
    "ApplicationApprovalStatusEnum",
    "ApplicationPlatformEnum",
    "ApplicationStoreEnum",
    "WebviewClaimingStatusEnum",
    "Application",
    "BatchArchiveApplicationsRequest",
    "BatchArchiveApplicationsResponse",
    "BatchCreateApplicationsRequest",
    "BatchCreateApplicationsResponse",
    "BatchUnarchiveApplicationsRequest",
    "BatchUnarchiveApplicationsResponse",
    "BatchUpdateApplicationsRequest",
    "BatchUpdateApplicationsResponse",
    "CreateApplicationRequest",
    "GetApplicationRequest",
    "ListApplicationsRequest",
    "ListApplicationsResponse",
    "UpdateApplicationRequest",
    "AppliedLabel",
    "AssetImageDensityEnum",
    "Asset",
    "AudienceSegmentApprovalStatusEnum",
    "AudienceSegmentLicenseTypeEnum",
    "AudienceSegmentStatusEnum",
    "AudienceSegmentTypeEnum",
    "AudienceSegment",
    "BatchActivateAudienceSegmentsRequest",
    "BatchActivateAudienceSegmentsResponse",
    "BatchApproveAudienceSegmentsRequest",
    "BatchApproveAudienceSegmentsResponse",
    "BatchCreateAudienceSegmentsRequest",
    "BatchCreateAudienceSegmentsResponse",
    "BatchDeactivateAudienceSegmentsRequest",
    "BatchDeactivateAudienceSegmentsResponse",
    "BatchPopulateAudienceSegmentsRequest",
    "BatchPopulateAudienceSegmentsResponse",
    "BatchRejectAudienceSegmentsRequest",
    "BatchRejectAudienceSegmentsResponse",
    "BatchUpdateAudienceSegmentsRequest",
    "BatchUpdateAudienceSegmentsResponse",
    "CreateAudienceSegmentRequest",
    "GetAudienceSegmentRequest",
    "ListAudienceSegmentsRequest",
    "ListAudienceSegmentsResponse",
    "UpdateAudienceSegmentRequest",
    "BandwidthGroup",
    "GetBandwidthGroupRequest",
    "ListBandwidthGroupsRequest",
    "ListBandwidthGroupsResponse",
    "BrandLiftPartnerEnum",
    "BreakTemplate",
    "BreakTemplateMember",
    "BatchCreateBreakTemplatesRequest",
    "BatchCreateBreakTemplatesResponse",
    "BatchUpdateBreakTemplatesRequest",
    "BatchUpdateBreakTemplatesResponse",
    "CreateBreakTemplateRequest",
    "GetBreakTemplateRequest",
    "ListBreakTemplatesRequest",
    "ListBreakTemplatesResponse",
    "UpdateBreakTemplateRequest",
    "BrowserLanguage",
    "GetBrowserLanguageRequest",
    "ListBrowserLanguagesRequest",
    "ListBrowserLanguagesResponse",
    "Browser",
    "GetBrowserRequest",
    "ListBrowsersRequest",
    "ListBrowsersResponse",
    "AdMediaDeliveryConfig",
    "CdnConfig",
    "CdnSecurityPolicy",
    "MediaLocation",
    "SourceContentConfig",
    "BatchActivateCdnConfigsRequest",
    "BatchActivateCdnConfigsResponse",
    "BatchArchiveCdnConfigsRequest",
    "BatchArchiveCdnConfigsResponse",
    "BatchCreateCdnConfigsRequest",
    "BatchCreateCdnConfigsResponse",
    "BatchUpdateCdnConfigsRequest",
    "BatchUpdateCdnConfigsResponse",
    "CreateCdnConfigRequest",
    "GetCdnConfigRequest",
    "ListCdnConfigsRequest",
    "ListCdnConfigsResponse",
    "UpdateCdnConfigRequest",
    "CdnConfigStatusEnum",
    "CdnConfigTypeEnum",
    "CdnSecurityPolicyTypeEnum",
    "CdnSecurityPolicyOriginForwardingEnum",
    "ChildContentEligibilityEnum",
    "ChildPublisher",
    "BatchCreateChildPublishersRequest",
    "BatchCreateChildPublishersResponse",
    "BatchRejectChildPublishersRequest",
    "BatchRejectChildPublishersResponse",
    "BatchRenegotiateChildPublisherAgreementsRequest",
    "BatchRenegotiateChildPublisherAgreementsResponse",
    "BatchResendChildPublisherInvitationEmailsRequest",
    "BatchResendChildPublisherInvitationEmailsResponse",
    "BatchUpdateChildPublishersRequest",
    "BatchUpdateChildPublishersResponse",
    "BatchWithdrawChildPublishersRequest",
    "BatchWithdrawChildPublishersResponse",
    "CreateChildPublisherRequest",
    "GetChildPublisherRequest",
    "ListChildPublishersRequest",
    "ListChildPublishersResponse",
    "RenegotiateChildPublisherAgreementRequest",
    "UpdateChildPublisherRequest",
    "CmsMetadataKeyStatusEnum",
    "CmsMetadataKey",
    "BatchActivateCmsMetadataKeysRequest",
    "BatchActivateCmsMetadataKeysResponse",
    "BatchDeactivateCmsMetadataKeysRequest",
    "BatchDeactivateCmsMetadataKeysResponse",
    "GetCmsMetadataKeyRequest",
    "ListCmsMetadataKeysRequest",
    "ListCmsMetadataKeysResponse",
    "CmsMetadataValueStatusEnum",
    "CmsMetadataValue",
    "BatchActivateCmsMetadataValuesRequest",
    "BatchActivateCmsMetadataValuesResponse",
    "BatchDeactivateCmsMetadataValuesRequest",
    "BatchDeactivateCmsMetadataValuesResponse",
    "GetCmsMetadataValueRequest",
    "ListCmsMetadataValuesRequest",
    "ListCmsMetadataValuesResponse",
    "CompanyCreditStatusEnum",
    "CompanyTypeEnum",
    "Company",
    "BatchCreateCompaniesRequest",
    "BatchCreateCompaniesResponse",
    "BatchUpdateCompaniesRequest",
    "BatchUpdateCompaniesResponse",
    "CreateCompanyRequest",
    "GetCompanyRequest",
    "ListCompaniesRequest",
    "ListCompaniesResponse",
    "UpdateCompanyRequest",
    "ContactStatusEnum",
    "Contact",
    "BatchCreateContactsRequest",
    "BatchCreateContactsResponse",
    "BatchUpdateContactsRequest",
    "BatchUpdateContactsResponse",
    "CreateContactRequest",
    "GetContactRequest",
    "ListContactsRequest",
    "ListContactsResponse",
    "UpdateContactRequest",
    "ContentBundleStatusEnum",
    "ContentBundle",
    "BatchActivateContentBundlesRequest",
    "BatchActivateContentBundlesResponse",
    "BatchDeactivateContentBundlesRequest",
    "BatchDeactivateContentBundlesResponse",
    "GetContentBundleRequest",
    "ListContentBundlesRequest",
    "ListContentBundlesResponse",
    "ContentStatusEnum",
    "ContentStatusSourceEnum",
    "DaiIngestErrorReasonEnum",
    "DaiIngestStatusEnum",
    "ContentLabel",
    "GetContentLabelRequest",
    "ListContentLabelsRequest",
    "ListContentLabelsResponse",
    "CmsContent",
    "Content",
    "DaiIngestError",
    "GetContentRequest",
    "ListContentRequest",
    "ListContentResponse",
    "ConversionEventEnum",
    "ClickTag",
    "CreativeAsset",
    "CreativeDestinationUrlTypeEnum",
    "CreativeLockedOrientationEnum",
    "CreativeSslOverrideEnum",
    "CreativeSslScanResultEnum",
    "VastAdIdTypeEnum",
    "AdExchangeCreativeDetails",
    "AdSenseCreativeDetails",
    "AspectRatioImageCreativeDetails",
    "AudioCreativeDetails",
    "AudioRedirectCreativeDetails",
    "BuyerPlacementConfig",
    "ClickTrackingCreativeDetails",
    "Creative",
    "CustomCreativeDetails",
    "Html5CreativeDetails",
    "ImageCreativeDetails",
    "ImageOverlayCreativeDetails",
    "ImageRedirectCreativeDetails",
    "ImageRedirectOverlayCreativeDetails",
    "InternalRedirectCreativeDetails",
    "LegacyDfpCreativeDetails",
    "ProgrammaticCreativeDetails",
    "RichMediaStudioCreativeDetails",
    "SetTopBoxCreativeDetails",
    "TemplateCreativeDetails",
    "ThirdPartyCreativeDetails",
    "VastInfo",
    "VastRedirectCreativeDetails",
    "VideoCreativeDetails",
    "VideoRedirectCreativeDetails",
    "CreativePlaceholder",
    "CreativePlaceholderCompanion",
    "BatchActivateCreativesRequest",
    "BatchActivateCreativesResponse",
    "BatchDeactivateCreativesRequest",
    "BatchDeactivateCreativesResponse",
    "GetCreativeRequest",
    "ListCreativesRequest",
    "ListCreativesResponse",
    "CreativeSet",
    "CreateCreativeSetRequest",
    "GetCreativeSetRequest",
    "ListCreativeSetsRequest",
    "ListCreativeSetsResponse",
    "UpdateCreativeSetRequest",
    "CreativeTargeting",
    "CreativeTemplateStatusEnum",
    "CreativeTemplateTypeEnum",
    "CreativeTemplate",
    "CreativeTemplateVariable",
    "GetCreativeTemplateRequest",
    "ListCreativeTemplatesRequest",
    "ListCreativeTemplatesResponse",
    "CreativeTemplateVariableUrlTypeEnum",
    "CreativeThirdPartyDataDeclarationStatusEnum",
    "CreativeWrapperOrderingEnum",
    "CreativeWrapperStatusEnum",
    "CreativeWrapperTypeEnum",
    "CreativeWrapper",
    "BatchActivateCreativeWrappersRequest",
    "BatchActivateCreativeWrappersResponse",
    "BatchCreateCreativeWrappersRequest",
    "BatchCreateCreativeWrappersResponse",
    "BatchDeactivateCreativeWrappersRequest",
    "BatchDeactivateCreativeWrappersResponse",
    "BatchUpdateCreativeWrappersRequest",
    "BatchUpdateCreativeWrappersResponse",
    "CreateCreativeWrapperRequest",
    "GetCreativeWrapperRequest",
    "ListCreativeWrappersRequest",
    "ListCreativeWrappersResponse",
    "UpdateCreativeWrapperRequest",
    "CustomCreativeAsset",
    "CustomFieldDataTypeEnum",
    "CustomFieldEntityTypeEnum",
    "CustomFieldStatusEnum",
    "CustomFieldVisibilityEnum",
    "CustomField",
    "CustomFieldOption",
    "BatchActivateCustomFieldsRequest",
    "BatchActivateCustomFieldsResponse",
    "BatchCreateCustomFieldsRequest",
    "BatchCreateCustomFieldsResponse",
    "BatchDeactivateCustomFieldsRequest",
    "BatchDeactivateCustomFieldsResponse",
    "BatchUpdateCustomFieldsRequest",
    "BatchUpdateCustomFieldsResponse",
    "CreateCustomFieldRequest",
    "GetCustomFieldRequest",
    "ListCustomFieldsRequest",
    "ListCustomFieldsResponse",
    "UpdateCustomFieldRequest",
    "CustomFieldValue",
    "CustomPacingCurve",
    "CustomPacingGoal",
    "CustomPacingGoalUnitEnum",
    "CustomTargetingKeyReportableTypeEnum",
    "CustomTargetingKeyStatusEnum",
    "CustomTargetingKeyTypeEnum",
    "CustomTargetingKey",
    "BatchActivateCustomTargetingKeysRequest",
    "BatchActivateCustomTargetingKeysResponse",
    "BatchCreateCustomTargetingKeysRequest",
    "BatchCreateCustomTargetingKeysResponse",
    "BatchDeactivateCustomTargetingKeysRequest",
    "BatchDeactivateCustomTargetingKeysResponse",
    "BatchUpdateCustomTargetingKeysRequest",
    "BatchUpdateCustomTargetingKeysResponse",
    "CreateCustomTargetingKeyRequest",
    "GetCustomTargetingKeyRequest",
    "ListCustomTargetingKeysRequest",
    "ListCustomTargetingKeysResponse",
    "UpdateCustomTargetingKeyRequest",
    "CustomTargetingValueMatchTypeEnum",
    "CustomTargetingValueStatusEnum",
    "CustomTargetingValue",
    "ActivateCustomTargetingValueRequest",
    "BatchActivateCustomTargetingValuesRequest",
    "BatchActivateCustomTargetingValuesResponse",
    "BatchCreateCustomTargetingValuesRequest",
    "BatchCreateCustomTargetingValuesResponse",
    "BatchDeactivateCustomTargetingValuesRequest",
    "BatchDeactivateCustomTargetingValuesResponse",
    "BatchUpdateCustomTargetingValuesRequest",
    "BatchUpdateCustomTargetingValuesResponse",
    "CreateCustomTargetingValueRequest",
    "DeactivateCustomTargetingValueRequest",
    "GetCustomTargetingValueRequest",
    "ListCustomTargetingValuesRequest",
    "ListCustomTargetingValuesResponse",
    "UpdateCustomTargetingValueRequest",
    "DaiAuthenticationKeyStatusEnum",
    "DaiAuthenticationKeyTypeEnum",
    "DaiAuthenticationKey",
    "BatchActivateDaiAuthenticationKeysRequest",
    "BatchActivateDaiAuthenticationKeysResponse",
    "BatchCreateDaiAuthenticationKeysRequest",
    "BatchCreateDaiAuthenticationKeysResponse",
    "BatchDeactivateDaiAuthenticationKeysRequest",
    "BatchDeactivateDaiAuthenticationKeysResponse",
    "BatchUpdateDaiAuthenticationKeysRequest",
    "BatchUpdateDaiAuthenticationKeysResponse",
    "CreateDaiAuthenticationKeyRequest",
    "GetDaiAuthenticationKeyRequest",
    "ListDaiAuthenticationKeysRequest",
    "ListDaiAuthenticationKeysResponse",
    "UpdateDaiAuthenticationKeyRequest",
    "ContainerTypeEnum",
    "DaiEncodingProfileStatusEnum",
    "DaiEncodingProfileVariantTypeEnum",
    "AudioSettings",
    "DaiEncodingProfile",
    "VideoSettings",
    "ActivateDaiEncodingProfileRequest",
    "ArchiveDaiEncodingProfileRequest",
    "BatchActivateDaiEncodingProfilesRequest",
    "BatchActivateDaiEncodingProfilesResponse",
    "BatchArchiveDaiEncodingProfilesRequest",
    "BatchArchiveDaiEncodingProfilesResponse",
    "BatchCreateDaiEncodingProfilesRequest",
    "BatchCreateDaiEncodingProfilesResponse",
    "BatchUpdateDaiEncodingProfilesRequest",
    "BatchUpdateDaiEncodingProfilesResponse",
    "CreateDaiEncodingProfileRequest",
    "GetDaiEncodingProfileRequest",
    "ListDaiEncodingProfilesRequest",
    "ListDaiEncodingProfilesResponse",
    "UpdateDaiEncodingProfileRequest",
    "AdBreakFindingTypeEnum",
    "AdRequestFindingTypeEnum",
    "AdResponseTypeEnum",
    "BreakTypeEnum",
    "CreativeFindingTypeEnum",
    "CreativeIdTypeEnum",
    "PodFindingTypeEnum",
    "PrefetchStageTypeEnum",
    "ReportingTypeEnum",
    "SessionFindingSeverityEnum",
    "SlateFindingTypeEnum",
    "StitchingTypeEnum",
    "TrackingPingFindingTypeEnum",
    "DaiSession",
    "GetDaiSessionRequest",
    "DateRange",
    "DealBuyerPermissionTypeEnum",
    "DealPriorityTierEnum",
    "CompanionDeliveryOptionEnum",
    "CreativeRotationTypeEnum",
    "LineItemDeliveryRateTypeEnum",
    "RoadblockingTypeEnum",
    "DeliveryIndicator",
    "DeviceCapability",
    "GetDeviceCapabilityRequest",
    "ListDeviceCapabilitiesRequest",
    "ListDeviceCapabilitiesResponse",
    "DeviceCategory",
    "GetDeviceCategoryRequest",
    "ListDeviceCategoriesRequest",
    "ListDeviceCategoriesResponse",
    "DeviceManufacturer",
    "GetDeviceManufacturerRequest",
    "ListDeviceManufacturersRequest",
    "ListDeviceManufacturersResponse",
    "DiscountTypeEnum",
    "AdBreakStateEnum",
    "EntitySignalsMapping",
    "BatchCreateEntitySignalsMappingsRequest",
    "BatchCreateEntitySignalsMappingsResponse",
    "BatchUpdateEntitySignalsMappingsRequest",
    "BatchUpdateEntitySignalsMappingsResponse",
    "CreateEntitySignalsMappingRequest",
    "GetEntitySignalsMappingRequest",
    "ListEntitySignalsMappingsRequest",
    "ListEntitySignalsMappingsResponse",
    "UpdateEntitySignalsMappingRequest",
    "EnvironmentTypeEnum",
    "ExchangeSyndicationProductEnum",
    "ExclusionScopeEnum",
    "AlternativeUnitTypeForecast",
    "AvailabilityForecast",
    "AvailabilityForecastOptions",
    "ContendingLineItem",
    "DeliveryForecast",
    "DeliveryForecastOptions",
    "DeliveryForecastResult",
    "ExistingLineItemList",
    "ForecastBreakdown",
    "ForecastBreakdownEntry",
    "ForecastBreakdownOptions",
    "ForecastBreakdownTarget",
    "GrpDemographicBreakdown",
    "LineItemDeliveryForecast",
    "TargetingCriteriaBreakdown",
    "TimeSeries",
    "RunAvailabilityForecastRequest",
    "RunAvailabilityForecastResponse",
    "RunDeliveryForecastRequest",
    "RunDeliveryForecastResponse",
    "RunTrafficDataRequest",
    "RunTrafficDataResponse",
    "ForecastingGrpAgeEnum",
    "ForecastingGrpGenderEnum",
    "ForecastingGrpUnitEnum",
    "ForecastingTargetingDimensionEnum",
    "FrequencyCap",
    "GeoTarget",
    "GetGeoTargetRequest",
    "ListGeoTargetsRequest",
    "ListGeoTargetsResponse",
    "Goal",
    "GoalTypeEnum",
    "UnitTypeEnum",
    "GrpProviderEnum",
    "GrpSettings",
    "GrpTargetGenderEnum",
    "LabelTypeEnum",
    "Label",
    "BatchActivateLabelsRequest",
    "BatchActivateLabelsResponse",
    "BatchCreateLabelsRequest",
    "BatchCreateLabelsResponse",
    "BatchDeactivateLabelsRequest",
    "BatchDeactivateLabelsResponse",
    "BatchUpdateLabelsRequest",
    "BatchUpdateLabelsResponse",
    "CreateLabelRequest",
    "GetLabelRequest",
    "ListLabelsRequest",
    "ListLabelsResponse",
    "UpdateLabelRequest",
    "LineItemAllowedFormatEnum",
    "LineItemCreativeAssociationStatusEnum",
    "LineItemCreativeAssociation",
    "LineItemCreativeAssociationStats",
    "GetLineItemCreativeAssociationRequest",
    "ListLineItemCreativeAssociationsRequest",
    "ListLineItemCreativeAssociationsResponse",
    "LineItemDealInfo",
    "LineItemDeliveryForecastSourceEnum",
    "LineItemDiscount",
    "LineItemComputedStatusEnum",
    "LineItemCostTypeEnum",
    "LineItemReservationStatusEnum",
    "LineItemTypeEnum",
    "LineItem",
    "BatchActivateLineItemsRequest",
    "BatchActivateLineItemsResponse",
    "BatchArchiveLineItemsRequest",
    "BatchArchiveLineItemsResponse",
    "BatchCreateLineItemsRequest",
    "BatchCreateLineItemsResponse",
    "BatchDeleteLineItemsRequest",
    "BatchPauseLineItemsRequest",
    "BatchPauseLineItemsResponse",
    "BatchReleaseLineItemsRequest",
    "BatchReleaseLineItemsResponse",
    "BatchReserveAndOverbookLineItemsRequest",
    "BatchReserveAndOverbookLineItemsResponse",
    "BatchReserveLineItemsRequest",
    "BatchReserveLineItemsResponse",
    "BatchResumeAndOverbookLineItemsRequest",
    "BatchResumeAndOverbookLineItemsResponse",
    "BatchResumeLineItemsRequest",
    "BatchResumeLineItemsResponse",
    "BatchUnarchiveLineItemsRequest",
    "BatchUnarchiveLineItemsResponse",
    "BatchUpdateLineItemsRequest",
    "BatchUpdateLineItemsResponse",
    "CreateLineItemRequest",
    "GetLineItemRequest",
    "ListLineItemsRequest",
    "ListLineItemsResponse",
    "UpdateLineItemRequest",
    "LineItemStats",
    "LineItemTemplate",
    "GetLineItemTemplateRequest",
    "ListLineItemTemplatesRequest",
    "ListLineItemTemplatesResponse",
    "LinkedDeviceVisibilityEnum",
    "LinkedDevice",
    "GetLinkedDeviceRequest",
    "ListLinkedDevicesRequest",
    "ListLinkedDevicesResponse",
    "AdBreakFillTypeEnum",
    "AdBreakMarkupTypeEnum",
    "DynamicAdInsertionTypeEnum",
    "HlsMasterPlaylistRefreshTypeEnum",
    "HlsSettingsPlaylistTypeEnum",
    "LiveStreamEventStatusEnum",
    "LiveStreamEventStreamingFormatEnum",
    "SlateStatusEnum",
    "LiveStreamEvent",
    "AuxiliaryAdSettings",
    "DashBridge",
    "HlsSettings",
    "LiveStream",
    "LiveStreamConditioning",
    "MasterPlaylistSettings",
    "PrefetchSettings",
    "PrerollSettings",
    "BatchActivateLiveStreamsRequest",
    "BatchActivateLiveStreamsResponse",
    "BatchArchiveLiveStreamsRequest",
    "BatchArchiveLiveStreamsResponse",
    "BatchCreateLiveStreamsRequest",
    "BatchCreateLiveStreamsResponse",
    "BatchPauseAdsLiveStreamsRequest",
    "BatchPauseAdsLiveStreamsResponse",
    "BatchPauseLiveStreamsRequest",
    "BatchPauseLiveStreamsResponse",
    "BatchRefreshMasterPlaylistsRequest",
    "BatchRefreshMasterPlaylistsResponse",
    "BatchUpdateLiveStreamsRequest",
    "BatchUpdateLiveStreamsResponse",
    "CreateLiveStreamRequest",
    "GetLiveStreamRequest",
    "ListLiveStreamsRequest",
    "ListLiveStreamsResponse",
    "UpdateLiveStreamRequest",
    "EarningsProductBreakdown",
    "McmEarnings",
    "FetchMcmEarningsRequest",
    "FetchMcmEarningsResponse",
    "ChildPublisherAddressVerificationStatusEnum",
    "ChildPublisherIdentityVerificationStatusEnum",
    "ChildPublisherOnboardingTaskEnum",
    "DelegationAccountStatusEnum",
    "DelegationApprovalStatusEnum",
    "DelegationInvitationStatusEnum",
    "DelegationTypeEnum",
    "McmEarningsProductTypeEnum",
    "McmReadinessStatusEnum",
    "MobileCarrier",
    "GetMobileCarrierRequest",
    "ListMobileCarriersRequest",
    "ListMobileCarriersResponse",
    "MobileDevice",
    "GetMobileDeviceRequest",
    "ListMobileDevicesRequest",
    "ListMobileDevicesResponse",
    "MobileDeviceSubmodel",
    "GetMobileDeviceSubmodelRequest",
    "ListMobileDeviceSubmodelsRequest",
    "ListMobileDeviceSubmodelsResponse",
    "NativeStyleStatusEnum",
    "NativeStyle",
    "BatchActivateNativeStylesRequest",
    "BatchActivateNativeStylesResponse",
    "BatchArchiveNativeStylesRequest",
    "BatchArchiveNativeStylesResponse",
    "BatchCreateNativeStylesRequest",
    "BatchCreateNativeStylesResponse",
    "BatchDeactivateNativeStylesRequest",
    "BatchDeactivateNativeStylesResponse",
    "BatchUpdateNativeStylesRequest",
    "BatchUpdateNativeStylesResponse",
    "CreateNativeStyleRequest",
    "GetNativeStyleRequest",
    "ListNativeStylesRequest",
    "ListNativeStylesResponse",
    "UpdateNativeStyleRequest",
    "DefaultThirdPartyDataDeclaration",
    "Network",
    "GetDefaultThirdPartyDataDeclarationRequest",
    "GetNetworkRequest",
    "ListNetworksRequest",
    "ListNetworksResponse",
    "ProvisionTestNetworkRequest",
    "UpdateNetworkRequest",
    "NielsenCtvPacingEnum",
    "NonGuaranteedDealPriority",
    "OperatingSystem",
    "GetOperatingSystemRequest",
    "ListOperatingSystemsRequest",
    "ListOperatingSystemsResponse",
    "OperatingSystemVersion",
    "GetOperatingSystemVersionRequest",
    "ListOperatingSystemVersionsRequest",
    "ListOperatingSystemVersionsResponse",
    "OrderStatusEnum",
    "Order",
    "BatchApproveAndOverbookOrdersRequest",
    "BatchApproveAndOverbookOrdersResponse",
    "BatchApproveOrdersRequest",
    "BatchApproveOrdersResponse",
    "BatchApproveOrdersWithoutReservationRequest",
    "BatchApproveOrdersWithoutReservationResponse",
    "BatchArchiveOrdersRequest",
    "BatchArchiveOrdersResponse",
    "BatchCreateOrdersRequest",
    "BatchCreateOrdersResponse",
    "BatchDeleteOrdersRequest",
    "BatchDeleteOrdersResponse",
    "BatchDisapproveOrdersRequest",
    "BatchDisapproveOrdersResponse",
    "BatchDisapproveOrdersWithoutReservationChangesRequest",
    "BatchDisapproveOrdersWithoutReservationChangesResponse",
    "BatchPauseOrdersRequest",
    "BatchPauseOrdersResponse",
    "BatchResumeAndOverbookOrdersRequest",
    "BatchResumeAndOverbookOrdersResponse",
    "BatchResumeOrdersRequest",
    "BatchResumeOrdersResponse",
    "BatchRetractOrdersRequest",
    "BatchRetractOrdersResponse",
    "BatchRetractOrdersWithoutReservationChangesRequest",
    "BatchRetractOrdersWithoutReservationChangesResponse",
    "BatchSubmitOrdersForApprovalAndOverbookRequest",
    "BatchSubmitOrdersForApprovalAndOverbookResponse",
    "BatchSubmitOrdersForApprovalRequest",
    "BatchSubmitOrdersForApprovalResponse",
    "BatchSubmitOrdersForApprovalWithoutReservationChangesRequest",
    "BatchSubmitOrdersForApprovalWithoutReservationChangesResponse",
    "BatchUnarchiveOrdersRequest",
    "BatchUnarchiveOrdersResponse",
    "BatchUpdateOrdersRequest",
    "BatchUpdateOrdersResponse",
    "CreateOrderRequest",
    "GetOrderRequest",
    "ListOrdersRequest",
    "ListOrdersResponse",
    "UpdateOrderRequest",
    "PacingDeviceCategorizationEnum",
    "Partner",
    "BatchUpdatePartnersRequest",
    "BatchUpdatePartnersResponse",
    "GetPartnerRequest",
    "ListPartnersRequest",
    "ListPartnersResponse",
    "UpdatePartnerRequest",
    "PlacementStatusEnum",
    "Placement",
    "BatchActivatePlacementsRequest",
    "BatchActivatePlacementsResponse",
    "BatchArchivePlacementsRequest",
    "BatchArchivePlacementsResponse",
    "BatchCreatePlacementsRequest",
    "BatchCreatePlacementsResponse",
    "BatchDeactivatePlacementsRequest",
    "BatchDeactivatePlacementsResponse",
    "BatchUpdatePlacementsRequest",
    "BatchUpdatePlacementsResponse",
    "CreatePlacementRequest",
    "GetPlacementRequest",
    "ListPlacementsRequest",
    "ListPlacementsResponse",
    "UpdatePlacementRequest",
    "PrivateAuctionDeal",
    "CreatePrivateAuctionDealRequest",
    "GetPrivateAuctionDealRequest",
    "ListPrivateAuctionDealsRequest",
    "ListPrivateAuctionDealsResponse",
    "UpdatePrivateAuctionDealRequest",
    "PrivateAuction",
    "CreatePrivateAuctionRequest",
    "GetPrivateAuctionRequest",
    "ListPrivateAuctionsRequest",
    "ListPrivateAuctionsResponse",
    "UpdatePrivateAuctionRequest",
    "PrivateMarketplaceDealStatusEnum",
    "ProgrammaticBuyer",
    "GetProgrammaticBuyerRequest",
    "ListProgrammaticBuyersRequest",
    "ListProgrammaticBuyersResponse",
    "ReachPartnerEnum",
    "ReportDefinition",
    "ScheduleOptions",
    "Report",
    "ReportDataTable",
    "CreateReportRequest",
    "FetchReportResultRowsRequest",
    "FetchReportResultRowsResponse",
    "GetReportRequest",
    "ListReportsRequest",
    "ListReportsResponse",
    "RunReportMetadata",
    "RunReportRequest",
    "RunReportResponse",
    "UpdateReportRequest",
    "ReportValue",
    "ReportVisibilityEnum",
    "RequestPlatformEnum",
    "RichMediaAdsCompanyGdprStatusEnum",
    "RichMediaAdsCompany",
    "GetRichMediaAdsCompanyRequest",
    "ListRichMediaAdsCompaniesRequest",
    "ListRichMediaAdsCompaniesResponse",
    "RichMediaStudioChildAssetTypeEnum",
    "RichMediaStudioCreativeBillingAttributeEnum",
    "RichMediaStudioCreativeFormatEnum",
    "RichMediaStudioChildAssetProperty",
    "RoleStatusEnum",
    "Role",
    "GetRoleRequest",
    "ListRolesRequest",
    "ListRolesResponse",
    "SiteApprovalStatusEnum",
    "SiteDisapprovalReasonEnum",
    "DisapprovalReason",
    "Site",
    "BatchCreateSitesRequest",
    "BatchCreateSitesResponse",
    "BatchDeactivateSitesRequest",
    "BatchDeactivateSitesResponse",
    "BatchSubmitSitesForApprovalRequest",
    "BatchSubmitSitesForApprovalResponse",
    "BatchUpdateSitesRequest",
    "BatchUpdateSitesResponse",
    "CreateSiteRequest",
    "GetSiteRequest",
    "ListSitesRequest",
    "ListSitesResponse",
    "UpdateSiteRequest",
    "Size",
    "SizeTypeEnum",
    "SkippableAdTypeEnum",
    "Slate",
    "BatchArchiveSlatesRequest",
    "BatchArchiveSlatesResponse",
    "BatchCreateSlatesRequest",
    "BatchCreateSlatesResponse",
    "BatchUnarchiveSlatesRequest",
    "BatchUnarchiveSlatesResponse",
    "BatchUpdateSlatesRequest",
    "BatchUpdateSlatesResponse",
    "CreateSlateRequest",
    "GetSlateRequest",
    "ListSlatesRequest",
    "ListSlatesResponse",
    "UpdateSlateRequest",
    "SuggestedAdUnit",
    "BatchApproveSuggestedAdUnitsRequest",
    "BatchApproveSuggestedAdUnitsResponse",
    "GetSuggestedAdUnitRequest",
    "ListSuggestedAdUnitsRequest",
    "ListSuggestedAdUnitsResponse",
    "TargetPlatformEnum",
    "TargetedVideoBumperTypeEnum",
    "AdUnitTargeting",
    "AudienceSegmentTargeting",
    "BandwidthTargeting",
    "BrowserLanguageTargeting",
    "BrowserTargeting",
    "CmsMetadataTargeting",
    "ContentTargeting",
    "CustomTargeting",
    "CustomTargetingClause",
    "CustomTargetingLiteral",
    "DataSegmentTargeting",
    "DeviceCapabilityTargeting",
    "DeviceCategoryTargeting",
    "DeviceManufacturerTargeting",
    "FirstPartyMobileApplicationTargeting",
    "GeoTargeting",
    "InventoryTargeting",
    "MobileApplicationTargeting",
    "MobileCarrierTargeting",
    "OperatingSystemTargeting",
    "RequestFormatTargeting",
    "RequestPlatformTargeting",
    "Targeting",
    "TechnologyTargeting",
    "UserDomainTargeting",
    "VideoPosition",
    "VideoPositionTargeting",
    "TargetingPresetStatusEnum",
    "TargetingPreset",
    "BatchCreateTargetingPresetsRequest",
    "BatchCreateTargetingPresetsResponse",
    "BatchDeactivateTargetingPresetsRequest",
    "BatchDeactivateTargetingPresetsResponse",
    "BatchUpdateTargetingPresetsRequest",
    "BatchUpdateTargetingPresetsResponse",
    "CreateTargetingPresetRequest",
    "DeactivateTargetingPresetRequest",
    "GetTargetingPresetRequest",
    "ListTargetingPresetsRequest",
    "ListTargetingPresetsResponse",
    "UpdateTargetingPresetRequest",
    "TaxonomyCategory",
    "GetTaxonomyCategoryRequest",
    "ListTaxonomyCategoriesRequest",
    "ListTaxonomyCategoriesResponse",
    "TaxonomyTypeEnum",
    "TeamAccessTypeEnum",
    "TeamStatusEnum",
    "Team",
    "BatchActivateTeamsRequest",
    "BatchActivateTeamsResponse",
    "BatchCreateTeamsRequest",
    "BatchCreateTeamsResponse",
    "BatchDeactivateTeamsRequest",
    "BatchDeactivateTeamsResponse",
    "BatchUpdateTeamsRequest",
    "BatchUpdateTeamsResponse",
    "CreateTeamRequest",
    "GetTeamRequest",
    "ListTeamsRequest",
    "ListTeamsResponse",
    "UpdateTeamRequest",
    "ThirdPartyCompanyStatusEnum",
    "ThirdPartyCompanyTypeEnum",
    "ThirdPartyCompany",
    "GetThirdPartyCompanyRequest",
    "ListThirdPartyCompaniesRequest",
    "ListThirdPartyCompaniesResponse",
    "ThirdPartyDataDeclaration",
    "ThirdPartyDataDeclarationTypeEnum",
    "ThirdPartyMeasurementSettings",
    "TimeUnitEnum",
    "User",
    "BatchActivateUsersRequest",
    "BatchActivateUsersResponse",
    "BatchCreateUsersRequest",
    "BatchCreateUsersResponse",
    "BatchDeactivateUsersRequest",
    "BatchDeactivateUsersResponse",
    "BatchUpdateUsersRequest",
    "BatchUpdateUsersResponse",
    "CreateUserRequest",
    "GetUserRequest",
    "ListUsersRequest",
    "ListUsersResponse",
    "UpdateUserRequest",
    "VastRedirectTypeEnum",
    "VideoPositionEnum",
    "VideoTrackingUrl",
    "VideoTranscodeStatusEnum",
    "ViewabilityPartnerEnum",
    "ViewabilityProvider",
    "BatchCreateViewabilityProvidersRequest",
    "BatchCreateViewabilityProvidersResponse",
    "BatchUpdateViewabilityProvidersRequest",
    "BatchUpdateViewabilityProvidersResponse",
    "CreateViewabilityProviderRequest",
    "GetViewabilityProviderRequest",
    "ListViewabilityProvidersRequest",
    "ListViewabilityProvidersResponse",
    "UpdateViewabilityProviderRequest",
    "WebProperty",
)
