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
from .ad_break_messages import (
    AdBreak,
)
from .ad_break_optimization_type_enum import (
    AdBreakOptimizationTypeEnum,
)
from .ad_break_service import (
    CreateAdBreakRequest,
    DeleteAdBreakRequest,
    GetAdBreakRequest,
    ListAdBreaksRequest,
    ListAdBreaksResponse,
    UpdateAdBreakRequest,
)
from .ad_review_center_ad_enums import (
    AdReviewCenterAdStatusEnum,
    ArcCreativeFormatEnum,
    ManualAdReviewCenterAdStatusEnum,
)
from .ad_review_center_ad_messages import (
    AdReviewCenterAd,
)
from .ad_review_center_ad_service import (
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
from .ad_rule_enums import (
    AdRuleFrequencyCapBehaviorEnum,
    AdRuleStatusEnum,
)
from .ad_rule_fill_order_direction_enum import (
    AdRuleFillOrderDirectionEnum,
)
from .ad_rule_messages import (
    AdRule,
    AdRuleSlot,
)
from .ad_rule_service import (
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
from .ad_rule_slot_behavior_enum import (
    AdRuleSlotBehaviorEnum,
)
from .ad_rule_slot_bumper_enum import (
    AdRuleSlotBumperEnum,
)
from .ad_rule_slot_midroll_frequency_type_enum import (
    AdRuleSlotMidrollFrequencyTypeEnum,
)
from .ad_spot_fill_type_enum import (
    AdSpotFillTypeEnum,
)
from .ad_spot_messages import (
    AdSpot,
)
from .ad_spot_service import (
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
from .ad_spot_targeting_type_enum import (
    AdSpotTargetingTypeEnum,
)
from .ad_unit_enums import (
    AdUnitStatusEnum,
    RefreshRateTypeEnum,
    SmartSizeModeEnum,
    TargetWindowEnum,
)
from .ad_unit_messages import (
    AdUnit,
    AdUnitParent,
    AdUnitSize,
    LabelFrequencyCap,
)
from .ad_unit_service import (
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
from .admanager_error import (
    AdManagerError,
)
from .application_enums import (
    ApplicationApprovalStatusEnum,
    ApplicationPlatformEnum,
    ApplicationStoreEnum,
    WebviewClaimingStatusEnum,
)
from .application_messages import (
    Application,
)
from .application_service import (
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
from .applied_label import (
    AppliedLabel,
)
from .asset_enums import (
    AssetImageDensityEnum,
)
from .asset_messages import (
    Asset,
)
from .audience_segment_enums import (
    AudienceSegmentApprovalStatusEnum,
    AudienceSegmentLicenseTypeEnum,
    AudienceSegmentStatusEnum,
    AudienceSegmentTypeEnum,
)
from .audience_segment_messages import (
    AudienceSegment,
)
from .audience_segment_service import (
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
from .bandwidth_group_messages import (
    BandwidthGroup,
)
from .bandwidth_group_service import (
    GetBandwidthGroupRequest,
    ListBandwidthGroupsRequest,
    ListBandwidthGroupsResponse,
)
from .brand_lift_partner_enum import (
    BrandLiftPartnerEnum,
)
from .break_template_messages import (
    BreakTemplate,
    BreakTemplateMember,
)
from .break_template_service import (
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
from .browser_language_messages import (
    BrowserLanguage,
)
from .browser_language_service import (
    GetBrowserLanguageRequest,
    ListBrowserLanguagesRequest,
    ListBrowserLanguagesResponse,
)
from .browser_messages import (
    Browser,
)
from .browser_service import (
    GetBrowserRequest,
    ListBrowsersRequest,
    ListBrowsersResponse,
)
from .cdn_config_messages import (
    AdMediaDeliveryConfig,
    CdnConfig,
    CdnSecurityPolicy,
    MediaLocation,
    SourceContentConfig,
)
from .cdn_config_service import (
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
from .cdn_config_status_enum import (
    CdnConfigStatusEnum,
)
from .cdn_config_type_enum import (
    CdnConfigTypeEnum,
)
from .cdn_security_policy_enum import (
    CdnSecurityPolicyTypeEnum,
)
from .cdn_security_policy_origin_forwarding_enum import (
    CdnSecurityPolicyOriginForwardingEnum,
)
from .child_content_eligibility_enum import (
    ChildContentEligibilityEnum,
)
from .child_publisher_messages import (
    ChildPublisher,
)
from .child_publisher_service import (
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
from .cms_metadata_key_enums import (
    CmsMetadataKeyStatusEnum,
)
from .cms_metadata_key_messages import (
    CmsMetadataKey,
)
from .cms_metadata_key_service import (
    BatchActivateCmsMetadataKeysRequest,
    BatchActivateCmsMetadataKeysResponse,
    BatchDeactivateCmsMetadataKeysRequest,
    BatchDeactivateCmsMetadataKeysResponse,
    GetCmsMetadataKeyRequest,
    ListCmsMetadataKeysRequest,
    ListCmsMetadataKeysResponse,
)
from .cms_metadata_value_enums import (
    CmsMetadataValueStatusEnum,
)
from .cms_metadata_value_messages import (
    CmsMetadataValue,
)
from .cms_metadata_value_service import (
    BatchActivateCmsMetadataValuesRequest,
    BatchActivateCmsMetadataValuesResponse,
    BatchDeactivateCmsMetadataValuesRequest,
    BatchDeactivateCmsMetadataValuesResponse,
    GetCmsMetadataValueRequest,
    ListCmsMetadataValuesRequest,
    ListCmsMetadataValuesResponse,
)
from .company_enums import (
    CompanyCreditStatusEnum,
    CompanyTypeEnum,
)
from .company_messages import (
    Company,
)
from .company_service import (
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
from .contact_enums import (
    ContactStatusEnum,
)
from .contact_messages import (
    Contact,
)
from .contact_service import (
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
from .content_bundle_enums import (
    ContentBundleStatusEnum,
)
from .content_bundle_messages import (
    ContentBundle,
)
from .content_bundle_service import (
    BatchActivateContentBundlesRequest,
    BatchActivateContentBundlesResponse,
    BatchDeactivateContentBundlesRequest,
    BatchDeactivateContentBundlesResponse,
    GetContentBundleRequest,
    ListContentBundlesRequest,
    ListContentBundlesResponse,
)
from .content_enums import (
    ContentStatusEnum,
    ContentStatusSourceEnum,
    DaiIngestErrorReasonEnum,
    DaiIngestStatusEnum,
)
from .content_label_messages import (
    ContentLabel,
)
from .content_label_service import (
    GetContentLabelRequest,
    ListContentLabelsRequest,
    ListContentLabelsResponse,
)
from .content_messages import (
    CmsContent,
    Content,
    DaiIngestError,
)
from .content_service import (
    GetContentRequest,
    ListContentRequest,
    ListContentResponse,
)
from .conversion_event_enum import (
    ConversionEventEnum,
)
from .creative_asset import (
    ClickTag,
    CreativeAsset,
)
from .creative_enums import (
    CreativeDestinationUrlTypeEnum,
    CreativeLockedOrientationEnum,
    CreativeSslOverrideEnum,
    CreativeSslScanResultEnum,
    VastAdIdTypeEnum,
)
from .creative_messages import (
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
from .creative_placeholder import (
    CreativePlaceholder,
    CreativePlaceholderCompanion,
)
from .creative_service import (
    BatchActivateCreativesRequest,
    BatchActivateCreativesResponse,
    BatchDeactivateCreativesRequest,
    BatchDeactivateCreativesResponse,
    GetCreativeRequest,
    ListCreativesRequest,
    ListCreativesResponse,
)
from .creative_set_messages import (
    CreativeSet,
)
from .creative_set_service import (
    CreateCreativeSetRequest,
    GetCreativeSetRequest,
    ListCreativeSetsRequest,
    ListCreativeSetsResponse,
    UpdateCreativeSetRequest,
)
from .creative_targeting import (
    CreativeTargeting,
)
from .creative_template_enums import (
    CreativeTemplateStatusEnum,
    CreativeTemplateTypeEnum,
)
from .creative_template_messages import (
    CreativeTemplate,
    CreativeTemplateVariable,
)
from .creative_template_service import (
    GetCreativeTemplateRequest,
    ListCreativeTemplatesRequest,
    ListCreativeTemplatesResponse,
)
from .creative_template_variable_url_type_enum import (
    CreativeTemplateVariableUrlTypeEnum,
)
from .creative_third_party_data_declaration_status_enum import (
    CreativeThirdPartyDataDeclarationStatusEnum,
)
from .creative_wrapper_enums import (
    CreativeWrapperOrderingEnum,
    CreativeWrapperStatusEnum,
    CreativeWrapperTypeEnum,
)
from .creative_wrapper_messages import (
    CreativeWrapper,
)
from .creative_wrapper_service import (
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
from .custom_creative_asset import (
    CustomCreativeAsset,
)
from .custom_field_enums import (
    CustomFieldDataTypeEnum,
    CustomFieldEntityTypeEnum,
    CustomFieldStatusEnum,
    CustomFieldVisibilityEnum,
)
from .custom_field_messages import (
    CustomField,
    CustomFieldOption,
)
from .custom_field_service import (
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
from .custom_field_value import (
    CustomFieldValue,
)
from .custom_pacing_curve import (
    CustomPacingCurve,
    CustomPacingGoal,
)
from .custom_pacing_goal_unit_enum import (
    CustomPacingGoalUnitEnum,
)
from .custom_targeting_key_enums import (
    CustomTargetingKeyReportableTypeEnum,
    CustomTargetingKeyStatusEnum,
    CustomTargetingKeyTypeEnum,
)
from .custom_targeting_key_messages import (
    CustomTargetingKey,
)
from .custom_targeting_key_service import (
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
from .custom_targeting_value_enums import (
    CustomTargetingValueMatchTypeEnum,
    CustomTargetingValueStatusEnum,
)
from .custom_targeting_value_messages import (
    CustomTargetingValue,
)
from .custom_targeting_value_service import (
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
from .dai_authentication_key_enums import (
    DaiAuthenticationKeyStatusEnum,
    DaiAuthenticationKeyTypeEnum,
)
from .dai_authentication_key_messages import (
    DaiAuthenticationKey,
)
from .dai_authentication_key_service import (
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
from .dai_encoding_profile_enums import (
    ContainerTypeEnum,
    DaiEncodingProfileStatusEnum,
    DaiEncodingProfileVariantTypeEnum,
)
from .dai_encoding_profile_messages import (
    AudioSettings,
    DaiEncodingProfile,
    VideoSettings,
)
from .dai_encoding_profile_service import (
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
from .dai_session_enums import (
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
from .dai_session_messages import (
    DaiSession,
)
from .dai_session_service import (
    GetDaiSessionRequest,
)
from .date_range import (
    DateRange,
)
from .deal_buyer_permission_type_enum import (
    DealBuyerPermissionTypeEnum,
)
from .deal_priority_tier_enum import (
    DealPriorityTierEnum,
)
from .delivery_enums import (
    CompanionDeliveryOptionEnum,
    CreativeRotationTypeEnum,
    LineItemDeliveryRateTypeEnum,
    RoadblockingTypeEnum,
)
from .delivery_indicator import (
    DeliveryIndicator,
)
from .device_capability_messages import (
    DeviceCapability,
)
from .device_capability_service import (
    GetDeviceCapabilityRequest,
    ListDeviceCapabilitiesRequest,
    ListDeviceCapabilitiesResponse,
)
from .device_category_messages import (
    DeviceCategory,
)
from .device_category_service import (
    GetDeviceCategoryRequest,
    ListDeviceCategoriesRequest,
    ListDeviceCategoriesResponse,
)
from .device_manufacturer_messages import (
    DeviceManufacturer,
)
from .device_manufacturer_service import (
    GetDeviceManufacturerRequest,
    ListDeviceManufacturersRequest,
    ListDeviceManufacturersResponse,
)
from .discount_type_enum import (
    DiscountTypeEnum,
)
from .early_ad_break_notification_enums import (
    AdBreakStateEnum,
)
from .entity_signals_mapping_messages import (
    EntitySignalsMapping,
)
from .entity_signals_mapping_service import (
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
from .environment_type_enum import (
    EnvironmentTypeEnum,
)
from .exchange_syndication_product_enum import (
    ExchangeSyndicationProductEnum,
)
from .exclusion_scope_enum import (
    ExclusionScopeEnum,
)
from .forecast_messages import (
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
from .forecast_service import (
    RunAvailabilityForecastRequest,
    RunAvailabilityForecastResponse,
    RunDeliveryForecastRequest,
    RunDeliveryForecastResponse,
    RunTrafficDataRequest,
    RunTrafficDataResponse,
)
from .forecasting_enums import (
    ForecastingGrpAgeEnum,
    ForecastingGrpGenderEnum,
    ForecastingGrpUnitEnum,
    ForecastingTargetingDimensionEnum,
)
from .frequency_cap import (
    FrequencyCap,
)
from .geo_target_messages import (
    GeoTarget,
)
from .geo_target_service import (
    GetGeoTargetRequest,
    ListGeoTargetsRequest,
    ListGeoTargetsResponse,
)
from .goal import (
    Goal,
)
from .goal_enums import (
    GoalTypeEnum,
    UnitTypeEnum,
)
from .grp_provider_enum import (
    GrpProviderEnum,
)
from .grp_settings import (
    GrpSettings,
)
from .grp_target_gender_enum import (
    GrpTargetGenderEnum,
)
from .label_enums import (
    LabelTypeEnum,
)
from .label_messages import (
    Label,
)
from .label_service import (
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
from .line_item_allowed_format_enum import (
    LineItemAllowedFormatEnum,
)
from .line_item_creative_association_enums import (
    LineItemCreativeAssociationStatusEnum,
)
from .line_item_creative_association_messages import (
    LineItemCreativeAssociation,
    LineItemCreativeAssociationStats,
)
from .line_item_creative_association_service import (
    GetLineItemCreativeAssociationRequest,
    ListLineItemCreativeAssociationsRequest,
    ListLineItemCreativeAssociationsResponse,
)
from .line_item_deal_info import (
    LineItemDealInfo,
)
from .line_item_delivery_forecast_source_enum import (
    LineItemDeliveryForecastSourceEnum,
)
from .line_item_discount import (
    LineItemDiscount,
)
from .line_item_enums import (
    LineItemComputedStatusEnum,
    LineItemCostTypeEnum,
    LineItemReservationStatusEnum,
    LineItemTypeEnum,
)
from .line_item_messages import (
    LineItem,
)
from .line_item_service import (
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
from .line_item_stats import (
    LineItemStats,
)
from .line_item_template_messages import (
    LineItemTemplate,
)
from .line_item_template_service import (
    GetLineItemTemplateRequest,
    ListLineItemTemplatesRequest,
    ListLineItemTemplatesResponse,
)
from .linked_device_enums import (
    LinkedDeviceVisibilityEnum,
)
from .linked_device_messages import (
    LinkedDevice,
)
from .linked_device_service import (
    GetLinkedDeviceRequest,
    ListLinkedDevicesRequest,
    ListLinkedDevicesResponse,
)
from .live_stream_event_enums import (
    AdBreakFillTypeEnum,
    AdBreakMarkupTypeEnum,
    DynamicAdInsertionTypeEnum,
    HlsMasterPlaylistRefreshTypeEnum,
    HlsSettingsPlaylistTypeEnum,
    LiveStreamEventStatusEnum,
    LiveStreamEventStreamingFormatEnum,
    SlateStatusEnum,
)
from .live_stream_event_messages import (
    LiveStreamEvent,
)
from .live_stream_messages import (
    AuxiliaryAdSettings,
    DashBridge,
    HlsSettings,
    LiveStream,
    LiveStreamConditioning,
    MasterPlaylistSettings,
    PrefetchSettings,
    PrerollSettings,
)
from .live_stream_service import (
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
from .mcm_earnings_messages import (
    EarningsProductBreakdown,
    McmEarnings,
)
from .mcm_earnings_service import (
    FetchMcmEarningsRequest,
    FetchMcmEarningsResponse,
)
from .mcm_enums import (
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
from .mobile_carrier_messages import (
    MobileCarrier,
)
from .mobile_carrier_service import (
    GetMobileCarrierRequest,
    ListMobileCarriersRequest,
    ListMobileCarriersResponse,
)
from .mobile_device_messages import (
    MobileDevice,
)
from .mobile_device_service import (
    GetMobileDeviceRequest,
    ListMobileDevicesRequest,
    ListMobileDevicesResponse,
)
from .mobile_device_submodel_messages import (
    MobileDeviceSubmodel,
)
from .mobile_device_submodel_service import (
    GetMobileDeviceSubmodelRequest,
    ListMobileDeviceSubmodelsRequest,
    ListMobileDeviceSubmodelsResponse,
)
from .native_style_enums import (
    NativeStyleStatusEnum,
)
from .native_style_messages import (
    NativeStyle,
)
from .native_style_service import (
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
from .network_messages import (
    DefaultThirdPartyDataDeclaration,
    Network,
)
from .network_service import (
    GetDefaultThirdPartyDataDeclarationRequest,
    GetNetworkRequest,
    ListNetworksRequest,
    ListNetworksResponse,
    ProvisionTestNetworkRequest,
    UpdateNetworkRequest,
)
from .nielsen_ctv_pacing_enum import (
    NielsenCtvPacingEnum,
)
from .non_guaranteed_deal_priority import (
    NonGuaranteedDealPriority,
)
from .operating_system_messages import (
    OperatingSystem,
)
from .operating_system_service import (
    GetOperatingSystemRequest,
    ListOperatingSystemsRequest,
    ListOperatingSystemsResponse,
)
from .operating_system_version_messages import (
    OperatingSystemVersion,
)
from .operating_system_version_service import (
    GetOperatingSystemVersionRequest,
    ListOperatingSystemVersionsRequest,
    ListOperatingSystemVersionsResponse,
)
from .order_enums import (
    OrderStatusEnum,
)
from .order_messages import (
    Order,
)
from .order_service import (
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
from .pacing_device_categorization_enum import (
    PacingDeviceCategorizationEnum,
)
from .partner_messages import (
    Partner,
)
from .partner_service import (
    BatchUpdatePartnersRequest,
    BatchUpdatePartnersResponse,
    GetPartnerRequest,
    ListPartnersRequest,
    ListPartnersResponse,
    UpdatePartnerRequest,
)
from .placement_enums import (
    PlacementStatusEnum,
)
from .placement_messages import (
    Placement,
)
from .placement_service import (
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
from .private_auction_deal_messages import (
    PrivateAuctionDeal,
)
from .private_auction_deal_service import (
    CreatePrivateAuctionDealRequest,
    GetPrivateAuctionDealRequest,
    ListPrivateAuctionDealsRequest,
    ListPrivateAuctionDealsResponse,
    UpdatePrivateAuctionDealRequest,
)
from .private_auction_messages import (
    PrivateAuction,
)
from .private_auction_service import (
    CreatePrivateAuctionRequest,
    GetPrivateAuctionRequest,
    ListPrivateAuctionsRequest,
    ListPrivateAuctionsResponse,
    UpdatePrivateAuctionRequest,
)
from .private_marketplace_enums import (
    PrivateMarketplaceDealStatusEnum,
)
from .programmatic_buyer_messages import (
    ProgrammaticBuyer,
)
from .programmatic_buyer_service import (
    GetProgrammaticBuyerRequest,
    ListProgrammaticBuyersRequest,
    ListProgrammaticBuyersResponse,
)
from .reach_partner_enum import (
    ReachPartnerEnum,
)
from .report_definition import (
    ReportDefinition,
)
from .report_delivery import (
    ScheduleOptions,
)
from .report_messages import (
    Report,
    ReportDataTable,
)
from .report_service import (
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
from .report_value import (
    ReportValue,
)
from .report_visibility_enum import (
    ReportVisibilityEnum,
)
from .request_platform_enum import (
    RequestPlatformEnum,
)
from .rich_media_ads_company_enums import (
    RichMediaAdsCompanyGdprStatusEnum,
)
from .rich_media_ads_company_messages import (
    RichMediaAdsCompany,
)
from .rich_media_ads_company_service import (
    GetRichMediaAdsCompanyRequest,
    ListRichMediaAdsCompaniesRequest,
    ListRichMediaAdsCompaniesResponse,
)
from .rich_media_studio_child_asset_type_enum import (
    RichMediaStudioChildAssetTypeEnum,
)
from .rich_media_studio_creative_billing_attribute_enum import (
    RichMediaStudioCreativeBillingAttributeEnum,
)
from .rich_media_studio_creative_format_enum import (
    RichMediaStudioCreativeFormatEnum,
)
from .rich_media_studio_messages import (
    RichMediaStudioChildAssetProperty,
)
from .role_enums import (
    RoleStatusEnum,
)
from .role_messages import (
    Role,
)
from .role_service import (
    GetRoleRequest,
    ListRolesRequest,
    ListRolesResponse,
)
from .site_enums import (
    SiteApprovalStatusEnum,
    SiteDisapprovalReasonEnum,
)
from .site_messages import (
    DisapprovalReason,
    Site,
)
from .site_service import (
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
from .size import (
    Size,
)
from .size_type_enum import (
    SizeTypeEnum,
)
from .skippable_ad_type_enum import (
    SkippableAdTypeEnum,
)
from .slate_messages import (
    Slate,
)
from .slate_service import (
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
from .suggested_ad_unit_messages import (
    SuggestedAdUnit,
)
from .suggested_ad_unit_service import (
    BatchApproveSuggestedAdUnitsRequest,
    BatchApproveSuggestedAdUnitsResponse,
    GetSuggestedAdUnitRequest,
    ListSuggestedAdUnitsRequest,
    ListSuggestedAdUnitsResponse,
)
from .target_platform_enum import (
    TargetPlatformEnum,
)
from .targeted_video_bumper_type_enum import (
    TargetedVideoBumperTypeEnum,
)
from .targeting import (
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
from .targeting_preset_enums import (
    TargetingPresetStatusEnum,
)
from .targeting_preset_messages import (
    TargetingPreset,
)
from .targeting_preset_service import (
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
from .taxonomy_category_messages import (
    TaxonomyCategory,
)
from .taxonomy_category_service import (
    GetTaxonomyCategoryRequest,
    ListTaxonomyCategoriesRequest,
    ListTaxonomyCategoriesResponse,
)
from .taxonomy_type_enum import (
    TaxonomyTypeEnum,
)
from .team_enums import (
    TeamAccessTypeEnum,
    TeamStatusEnum,
)
from .team_messages import (
    Team,
)
from .team_service import (
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
from .third_party_company_enums import (
    ThirdPartyCompanyStatusEnum,
    ThirdPartyCompanyTypeEnum,
)
from .third_party_company_messages import (
    ThirdPartyCompany,
)
from .third_party_company_service import (
    GetThirdPartyCompanyRequest,
    ListThirdPartyCompaniesRequest,
    ListThirdPartyCompaniesResponse,
)
from .third_party_data_declaration import (
    ThirdPartyDataDeclaration,
)
from .third_party_data_declaration_type_enum import (
    ThirdPartyDataDeclarationTypeEnum,
)
from .third_party_measurement_settings import (
    ThirdPartyMeasurementSettings,
)
from .time_unit_enum import (
    TimeUnitEnum,
)
from .user_messages import (
    User,
)
from .user_service import (
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
from .vast_redirect_type_enum import (
    VastRedirectTypeEnum,
)
from .video_position_enum import (
    VideoPositionEnum,
)
from .video_tracking_url import (
    VideoTrackingUrl,
)
from .video_transcode_status_enum import (
    VideoTranscodeStatusEnum,
)
from .viewability_partner_enum import (
    ViewabilityPartnerEnum,
)
from .viewability_provider_messages import (
    ViewabilityProvider,
)
from .viewability_provider_service import (
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
from .web_property import (
    WebProperty,
)

__all__ = (
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
