# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-ads-datamanager/#history

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.8.0...google-ads-datamanager-v0.9.0) (2026-06-02)


### Features

* regenerate remaining packages (#17078) ([cc4f36f65e8b29d28f636e082435801b899cbca0](https://github.com/googleapis/google-cloud-python/commit/cc4f36f65e8b29d28f636e082435801b899cbca0))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.7.0...google-ads-datamanager-v0.8.0) (2026-04-02)


### Features

* add INVALID_MERCHANT_ID to the ErrorReason enum for when the merchant_id field is not valid ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* add EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED to the ErrorReason enum for campaigns missing the EU political advertising declaration ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.6.0...google-ads-datamanager-v0.7.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.5.0...google-ads-datamanager-v0.6.0) (2026-03-12)


### Documentation

* update filter field documentation to clarify case requirements and improve examples ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))


### Features

* deprecate INVALID_COUNTRY_CODE and add MEMBERSHIP_DURATION_TOO_LONG to the ErrorReason enum ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))


### Bug Fixes

* feat: update advertiser_identifier_count in PairIdInfo to be optional ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))
* update publisher_name in PairIdInfo to be required ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))
* update match_rate_percentage in PairIdInfo to be required ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.4.0...google-ads-datamanager-v0.5.0) (2026-02-26)


### Documentation

* add comments to resources and methods to clarify which are available only to data partners ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* a comment for message `PairData` is changed to clarify it is only available to data partners ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* a comment for enum `ErrorReason` is changed to clarify that it is subject to future additions ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* a comment for field `pair_data` in message `AudienceMember` is changed to clarify it is only available to data partners ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))


### Features

* add `RemoveUserIdDataStatus` to `RemoveAudienceMembersStatus` to report the status of user ID data removal ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `PartnerLinkService` for creating and managing links between advertiser and data partner accounts ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserListDirectLicense` resource ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `IngestPpidDataStatus` to `IngestAudienceMembersStatus` to report the status of PPID data ingestion ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `GOOGLE_AD_MANAGER_AUDIENCE_LINK` to the `AccountType` enum ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserListGlobalLicenseCustomerInfo` resource ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `RemovePpidDataStatus` to `RemoveAudienceMembersStatus` to report the status of PPID data removal ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `PpidData` to `AudienceMember` to support Publisher Provided ID (PPID) in audience member ingestion ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserListGlobalLicenseService` for creating and managing global user list licenses ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `MarketingDataInsightsService` for retrieving marketing data insights for a given user list ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `IngestUserIdDataStatus` to `IngestAudienceMembersStatus` to report the status of user ID data ingestion ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserIdData` to `AudienceMember` to support User ID in audience member ingestion ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add new `ErrorReason` values for licensing, user list operations, and permission checks ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `AgeRange` and `Gender` enums to support demographic breakdown in marketing insights ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserListGlobalLicense` resource ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserList` resource ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserListDirectLicenseService` for creating and managing direct user list licenses ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `PartnerLink` resource ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* add `UserListService` for creating and managing user lists ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))


### Bug Fixes

* changed `conversion_value` field to be optional in message `Event` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.3.0...google-ads-datamanager-v0.4.0) (2026-02-05)


### Documentation

* describe additional URI format for kek_uri in GcpEncryptionInfo and AwsKmsEncryptionInfo ([fe0a0b4638a8f5301c30be43fd2f2898ddc6db37](https://github.com/googleapis/google-cloud-python/commit/fe0a0b4638a8f5301c30be43fd2f2898ddc6db37))


### Bug Fixes

* update `go_package` packaging option from `google.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager` to `cloud.google.com/go/datamanager/apiv1/datamanagerpb;datamanagerpb` ([fe0a0b4638a8f5301c30be43fd2f2898ddc6db37](https://github.com/googleapis/google-cloud-python/commit/fe0a0b4638a8f5301c30be43fd2f2898ddc6db37))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.2.0...google-ads-datamanager-v0.3.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.1.0...google-ads-datamanager-v0.2.0) (2025-12-04)


### Features

* add `event_name` to `Event` for specifying the name of the Google Analytics event ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add new error codes `UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER`, `UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER`, `INVALID_PROPERTY_TYPE`, `INVALID_STREAM_TYPE`, `LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT`, `OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH`, `EVENT_TIME_INVALID`, `RESERVED_NAME_USED`, `INVALID_EVENT_NAME`, `NOT_ALLOWLISTED`, `MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT`, `FIELD_VALUE_TOO_LONG`, `TOO_MANY_ELEMENTS` to `ErrorReason` enum ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `PROCESSING_ERROR_REASON_AWS_AUTH_FAILED` to `ProcessingErrorReason` enum ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `additional_user_properties` to `UserProperties` for sending additional key-value pairs of user properties ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `AwsWrappedKeyInfo` to `EncryptionInfo` for supporting data encryption using AWS KMS keys ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `user_id` to `Event` for uniquely identifying a user as defined by the advertiser for Google Analytics events ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `client_id` to `Event` for uniquely identifying a user instance of a web client for a Google Analytics web stream ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `additional_event_parameters` to `Event` for sending additional key-value pairs of event parameters for Google Analytics events ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `GOOGLE_ANALYTICS_PROPERTY` to `AccountType` enum for supporting Google Analytics as a destination ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `additional_item_parameters` to `Item` for sending additional key-value pairs of item parameters ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `item_id` to `Item` for uniquely identifying an item ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add `PROCESSING_WARNING_REASON_AWS_AUTH_FAILED` to `ProcessingWarningReason` enum ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))

## [0.1.0](https://github.com/googleapis/google-cloud-python/compare/google-ads-datamanager-v0.0.0...google-ads-datamanager-v0.1.0) (2025-11-06)


### Features

* onboard a new library  ([8197d16dc5300cd153425dfb29e4dc510a2e7d05](https://github.com/googleapis/google-cloud-python/commit/8197d16dc5300cd153425dfb29e4dc510a2e7d05))
