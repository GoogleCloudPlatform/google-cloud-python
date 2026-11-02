# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-analytics-admin/#history

## [0.30.2](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.30.1...google-analytics-admin-v0.30.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.30.1](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.30.0...google-analytics-admin-v0.30.1) (2026-06-25)


### Features

* update googleapis and regenerate ([#17554](https://github.com/googleapis/google-cloud-python/issues/17554)) ([03d0574](https://github.com/googleapis/google-cloud-python/commit/03d0574da8485e918f16e90666928f5c7b7f1c92))

## [0.30.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.29.0...google-analytics-admin-v0.30.0) (2026-06-02)


### Features

* regenerate remaining packages (#17078) ([cc4f36f65e8b29d28f636e082435801b899cbca0](https://github.com/googleapis/google-cloud-python/commit/cc4f36f65e8b29d28f636e082435801b899cbca0))

## [0.29.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.28.0...google-analytics-admin-v0.29.0) (2026-05-06)

## [0.28.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.27.0...google-analytics-admin-v0.28.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.27.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.26.0...google-analytics-admin-v0.27.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.26.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.25.0...google-analytics-admin-v0.26.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.25.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.24.1...google-analytics-admin-v0.25.0) (2025-08-29)


### ⚠ BREAKING CHANGES

* remove the `FetchAutomatedGa4ConfigurationOptOut` method
* remove the `CreateConnectedSiteTag` method
* remove the `DeleteConnectedSiteTag` method
* remove the `ListConnectedSiteTags` method
* remove the `FetchConnectedGa4Property` method
* remove the `SetAutomatedGa4ConfigurationOptOutRequest` resource
* remove the `SetAutomatedGa4ConfigurationOptOutResponse` resource
* remove the `FetchAutomatedGa4ConfigurationOptOutRequest` resource
* remove the `FetchAutomatedGa4ConfigurationOptOutResponse` resource
* remove the `CreateConnectedSiteTagRequest` resource
* remove the `CreateConnectedSiteTagResponse` resource
* remove the `DeleteConnectedSiteTagRequest` resource
* remove the `ListConnectedSiteTagsRequest` resource
* remove the `ListConnectedSiteTagsResponse` resource
* remove the `FetchConnectedGa4PropertyRequest` resource
* remove the `FetchConnectedGa4PropertyResponse` resource
* remove the `ConnectedSiteTag` resource
* remove the `SetAutomatedGa4ConfigurationOptOut` method

### Features

* add reporting_identity_settings` fields to the `ChangeHistoryResource` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* add the `GetReportingIdentitySettings` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* add the `GetReportingIdentitySettingsRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* add the `REPORTING_IDENTITY_SETTINGS` resource type to the `ChangeHistoryResourceType` enum ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* add the `ReportingIdentitySettings` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))


### Bug Fixes

* remove the `ConnectedSiteTag` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `CreateConnectedSiteTag` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `CreateConnectedSiteTagRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `CreateConnectedSiteTagResponse` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `DeleteConnectedSiteTag` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `DeleteConnectedSiteTagRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `FetchAutomatedGa4ConfigurationOptOut` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `FetchAutomatedGa4ConfigurationOptOutRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `FetchAutomatedGa4ConfigurationOptOutResponse` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `FetchConnectedGa4Property` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `FetchConnectedGa4PropertyRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `FetchConnectedGa4PropertyResponse` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `ListConnectedSiteTags` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `ListConnectedSiteTagsRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `ListConnectedSiteTagsResponse` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `SetAutomatedGa4ConfigurationOptOut` method ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `SetAutomatedGa4ConfigurationOptOutRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))
* remove the `SetAutomatedGa4ConfigurationOptOutResponse` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))


### Documentation

* provide additional guidelines for the `user_provided_data` field in the `SubmitUserDeletionRequest` resource ([594263e](https://github.com/googleapis/google-cloud-python/commit/594263e519e347dad9a9639ecfe5ec12bdd9d7a0))

## [0.24.1](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.24.0...google-analytics-admin-v0.24.1) (2025-06-19)


### Features

* add the `GetSubpropertySyncConfigRequest` method ([223c62b](https://github.com/googleapis/google-cloud-python/commit/223c62bb9548d21de59e8bf5b950d30e8264afd6))
* add the `ListSubpropertySyncConfigsRequest` method ([223c62b](https://github.com/googleapis/google-cloud-python/commit/223c62bb9548d21de59e8bf5b950d30e8264afd6))
* add the `UpdateSubpropertySyncConfigRequest` method ([223c62b](https://github.com/googleapis/google-cloud-python/commit/223c62bb9548d21de59e8bf5b950d30e8264afd6))

## [0.24.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.6...google-analytics-admin-v0.24.0) (2025-04-17)


### ⚠ BREAKING CHANGES

* change an existing value KEY_EVENT = 32 to KEY_EVENT = 30 in enum `ChangeHistoryResourceType`.
* rename an existing field `key_event` to `reporting_data_annotation` in `ChangeHistoryChange`.

### Features

* add `key_event`, `reporting_data_annotation` fields to the `ChangeHistoryResource` resource ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `CreateReportingDataAnnotation` method ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `DeleteReportingDataAnnotation` method ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `GetReportingDataAnnotation` method ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `ListReportingDataAnnotations` method ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `REPORTING_DATA_ANNOTATION` resource type to the `ChangeHistoryResourceType` enum ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `ReportingDataAnnotation` type ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `SubmitUserDeletion` method ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* add the `UpdateReportingDataAnnotation` method ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))


### Bug Fixes

* change an existing value KEY_EVENT = 32 to KEY_EVENT = 30 in enum `ChangeHistoryResourceType`. ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* rename an existing field `key_event` to `reporting_data_annotation` in `ChangeHistoryChange`. ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))


### Documentation

* announce the deprecation of the `sharing_with_google_any_sales_enabled` field of the `DataSharingSettings` type ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))
* update the documentation of `sharing_with_google_support_enabled`, `sharing_with_google_assigned_sales_enabled`, 'sharing_with_google_products_enabled', 'sharing_with_others_enabled' fields of the `DataSharingSettings` type ([c59a5c9](https://github.com/googleapis/google-cloud-python/commit/c59a5c9a88038f81f8899003988bfd3201bf40ed))

## [0.23.6](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.5...google-analytics-admin-v0.23.6) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([a1b9294](https://github.com/googleapis/google-cloud-python/commit/a1b9294d0bf6e27c2a951d6df7faf7807dc5420b))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.23.5](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.4...google-analytics-admin-v0.23.5) (2025-03-06)


### Features

* added support for KeyEvents AdminAPI ChangeHistory ([1cc1a3d](https://github.com/googleapis/google-cloud-python/commit/1cc1a3d09ee59e4be030d3019d147f33b4009a34))

## [0.23.4](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.3...google-analytics-admin-v0.23.4) (2025-02-12)


### Features

* add `user_data_retention` field to `DataRetentionSettings` and mark as `REQUIRED` ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))
* add `user_data_retention` field to `DataRetentionSettings` and mark as `REQUIRED` ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))
* Add REST Interceptors which support reading metadata ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))
* Add support for reading selective GAPIC generation methods from service YAML ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))


### Bug Fixes

* mark `event_data_retention` field in `DataRetentionSettings` as `REQUIRED` ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))
* mark `event_data_retention` field in `DataRetentionSettings` as `REQUIRED` ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))


### Documentation

* replace "GA4" with "Google Analytics" or "GA" in all comments ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))
* replace "GA4" with "Google Analytics" or "GA" in all comments ([96aefef](https://github.com/googleapis/google-cloud-python/commit/96aefef02f806d12a2f4c1847a228181ab5b4afa))

## [0.23.3](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.2...google-analytics-admin-v0.23.3) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [0.23.2](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.1...google-analytics-admin-v0.23.2) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([85c7512](https://github.com/googleapis/google-cloud-python/commit/85c7512bbdde2b9cc60b4ad42b8c36c4558a07a5))

## [0.23.1](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.23.0...google-analytics-admin-v0.23.1) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13199](https://github.com/googleapis/google-cloud-python/issues/13199)) ([2fc3726](https://github.com/googleapis/google-cloud-python/commit/2fc372685731141ca1ed2a917dd18bacd79db88e))

## [0.23.0](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.9...google-analytics-admin-v0.23.0) (2024-08-08)


### ⚠ BREAKING CHANGES

* Rename custom method `CreateSubpropertyRequest` to `ProvisionSubpropertyRequest`

### Features

* add `CreateBigQueryLink`, `UpdateBigQueryLink`, and `DeleteBigQueryLink` methods ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add `GetEventEditRule`, `CreateEventEditRule`, `ListEventEditRules`, `UpdateEventEditRule`, `DeleteEventEditRule`, and `ReorderEventEditRules` methods to the Admin API v1 alpha ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add `GetKeyEvent`, `CreateKeyEvent`, `ListKeyEvents`, `UpdateKeyEvent`, and `DeleteKeyEvent` methods ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add the `BIGQUERY_LINK` option to the `ChangeHistoryResourceType` enum ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add the `create_time` field to the `Audience` resource ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add the `dataset_location` field to the `BigQueryLink` resource ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add the `gmp_organization` field to the `Account` resource ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* add the `primary` field to the `ChannelGroup` resource ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* mark `GetConversionEvent`, `CreateConversionEvent`, `ListConversionEvents`, `UpdateConversionEvent`, and `DeleteConversionEvent` methods as deprecated ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))


### Bug Fixes

* Rename custom method `CreateSubpropertyRequest` to `ProvisionSubpropertyRequest` ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))


### Documentation

* add deprecation comment to `GetConversionEvent`, `CreateConversionEvent`, `ListConversionEvents`, `UpdateConversionEvent`, and `DeleteConversionEvent` methods ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* improve comment formatting of `account` and `property` fields in `SearchChangeHistoryEventsRequest` ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* improve comment formatting of the `name` field in `DeleteFirebaseLinkRequest`, `GetGlobalSiteTagRequest`, and `GetDataSharingSettingsRequest` ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))
* improve comment formatting of the `parent` field in `CreateFirebaseLinkRequest` and `ListFirebaseLinksRequest` ([9033800](https://github.com/googleapis/google-cloud-python/commit/9033800e464f15be0e4c418710c158591a84439d))

## [0.22.9](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.8...google-analytics-admin-v0.22.9) (2024-07-30)


### Features

* [google-analytics-admin] add GetKeyEvent, CreateKeyEvent, ListKeyEvents, UpdateKeyEvent, DeleteKeyEvent methods to the Admin API v1beta ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))
* add the `default_conversion_value` field to the `ConversionEvent` resource in the Admin API v1beta ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))
* add the `gmp_organization` field to the `Account` resource in the Admin API v1beta ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))
* add the `include_all_users` and `expand_groups` fields to the `RunAccessReportRequest` resource in the Admin API v1beta ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))
* mark `GetConversionEvent`, `CreateConversionEvent`, `ListConversionEvents`, `UpdateConversionEvent`, `DeleteConversionEvent` methods as deprecated in the Admin API v1beta ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([c6eeae0](https://github.com/googleapis/google-cloud-python/commit/c6eeae00de802d98badd3de879ce5e870ba60a3a))


### Documentation

* change comment for field `property_type` in message `Property` ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))
* change comment for methods `DeleteAccount`, `DeleteProperty`, and `RunAccessReport` in service `AnalyticsAdminService` ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))
* change comment in fields `account` and `property` in message `SearchChangeHistoryEventsRequest` ([7b156ee](https://github.com/googleapis/google-cloud-python/commit/7b156ee7b233afc0f5f2050df7c654cad82772c9))

## [0.22.8](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.7...google-analytics-admin-v0.22.8) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12863](https://github.com/googleapis/google-cloud-python/issues/12863)) ([3e6e423](https://github.com/googleapis/google-cloud-python/commit/3e6e423b86cdace8538f610941aa84c7a6217934))

## [0.22.7](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.6...google-analytics-admin-v0.22.7) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12381](https://github.com/googleapis/google-cloud-python/issues/12381)) ([48ae8ab](https://github.com/googleapis/google-cloud-python/commit/48ae8aba7ec71a382e001b3a659022f942c3b436))

## [0.22.6](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.5...google-analytics-admin-v0.22.6) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12280](https://github.com/googleapis/google-cloud-python/issues/12280)) ([2d75d0e](https://github.com/googleapis/google-cloud-python/commit/2d75d0e67ca4cccddc688bd37c14ac80564a2e65))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))

## [0.22.5](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.4...google-analytics-admin-v0.22.5) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [0.22.4](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.3...google-analytics-admin-v0.22.4) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [0.22.3](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.2...google-analytics-admin-v0.22.3) (2024-01-26)


### Features

* Add `GetCalculatedMetric`, `CreateCalculatedMetric`, `ListCalculatedMetrics`, `UpdateCalculatedMetric`, `DeleteCalculatedMetric` methods to the Admin API v1alpha ([dea3367](https://github.com/googleapis/google-cloud-python/commit/dea3367d61b292c8d0a282ca937f4fc4f87981b7))
* Add the `calculated_metric` field to the `ChangeHistoryResource.resource` oneof field ([dea3367](https://github.com/googleapis/google-cloud-python/commit/dea3367d61b292c8d0a282ca937f4fc4f87981b7))
* Add the `CALCULATED_METRIC` option to the `ChangeHistoryResourceType` enum ([dea3367](https://github.com/googleapis/google-cloud-python/commit/dea3367d61b292c8d0a282ca937f4fc4f87981b7))
* Add the `CalculatedMetric` resource ([dea3367](https://github.com/googleapis/google-cloud-python/commit/dea3367d61b292c8d0a282ca937f4fc4f87981b7))

## [0.22.2](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.1...google-analytics-admin-v0.22.2) (2024-01-04)


### Features

* **v1alpha:** Add `GetSubpropertyEventFilter`, `ListSubpropertyEventFilters` methods to the Admin API v1 alpha ([fd30dff](https://github.com/googleapis/google-cloud-python/commit/fd30dff92a6e1523699e0f7340029e3187c42944))
* **v1alpha:** Add the `default_conversion_value` field to the `ConversionEvent` type ([fd30dff](https://github.com/googleapis/google-cloud-python/commit/fd30dff92a6e1523699e0f7340029e3187c42944))


### Documentation

* **v1alpha:** Update the documentation for `grouping_rule`, `system_defined` fields of the `ChannelGroup` type ([fd30dff](https://github.com/googleapis/google-cloud-python/commit/fd30dff92a6e1523699e0f7340029e3187c42944))
* **v1alpha:** Update the documentation for the `RunAccessReport` method ([fd30dff](https://github.com/googleapis/google-cloud-python/commit/fd30dff92a6e1523699e0f7340029e3187c42944))

## [0.22.1](https://github.com/googleapis/google-cloud-python/compare/google-analytics-admin-v0.22.0...google-analytics-admin-v0.22.1) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [0.22.0](https://github.com/googleapis/python-analytics-admin/compare/v0.21.0...v0.22.0) (2023-10-19)


### Features

* Add `DataRedactionSettings`, `RollupPropertySourceLink`, `SubpropertyEventFilterCondition`, `SubpropertyEventFilterExpression`, `SubpropertyEventFilterExpressionList`, `SubpropertyEventFilterClause`, `SubpropertyEventFilter` types ([49d0449](https://github.com/googleapis/python-analytics-admin/commit/49d0449e05cceca61fc976b35f542b1c344e4c23))
* Add `include_all_users`, `expand_groups` fields to `RunAccessReportRequest` ([49d0449](https://github.com/googleapis/python-analytics-admin/commit/49d0449e05cceca61fc976b35f542b1c344e4c23))
* Add `UpdateDataRedactionSettings`, `CreateRollupProperty`, `GetRollupPropertySourceLink`, `ListRollupPropertySourceLinks`, `CreateRollupPropertySourceLink`, `DeleteRollupPropertySourceLink`, `CreateSubproperty`, `CreateSubpropertyEventFilter`, `CreateSubpropertyEventFilter`, `ListSubpropertyEventFilters`, `UpdateSubpropertyEventFilter`, `DeleteSubpropertyEventFilter` methods to the Admin API v1 alpha ([49d0449](https://github.com/googleapis/python-analytics-admin/commit/49d0449e05cceca61fc976b35f542b1c344e4c23))
* Add the `data_redaction_settings` field to the `ChangeHistoryResource.resource` oneof field ([49d0449](https://github.com/googleapis/python-analytics-admin/commit/49d0449e05cceca61fc976b35f542b1c344e4c23))
* Add the `DATA_REDACTION_SETTINGS` option to the `ChangeHistoryResourceType` enum ([49d0449](https://github.com/googleapis/python-analytics-admin/commit/49d0449e05cceca61fc976b35f542b1c344e4c23))


### Bug Fixes

* Delete BatchDeleteUserLinks, DeleteUserLink, BatchUpdateUserLinks, UpdateUserLink, BatchCreateUserLinks, CreateUserLink, AuditUserLinks, ListUserLinks, BatchGetUserLinks, GetUserLink from the Admin API v1 alpha as per the announcement in https://bit.ly/46yBIDt ([49d0449](https://github.com/googleapis/python-analytics-admin/commit/49d0449e05cceca61fc976b35f542b1c344e4c23))

## [0.21.0](https://github.com/googleapis/python-analytics-admin/compare/v0.20.0...v0.21.0) (2023-10-10)


### ⚠ BREAKING CHANGES

* rename the `enterprise_daily_export_enabled` field to `fresh_daily_export_enabled` in the `BigQueryLink` resource

### Features

* Add `CoarseValue`, `ConversionValues`, `EventMapping`, `SKAdNetworkConversionValueSchema` types ([cabcb1f](https://github.com/googleapis/python-analytics-admin/commit/cabcb1ff2eb5100885c5684c2cfb6896ccadd97b))
* Add `GetSKAdNetworkConversionValueSchema`, `CreateSKAdNetworkConversionValueSchema`, `DeleteSKAdNetworkConversionValueSchema`, `UpdateSKAdNetworkConversionValueSchema`, `ListSKAdNetworkConversionValueSchemas` methods to the Admin API v1 alpha ([cabcb1f](https://github.com/googleapis/python-analytics-admin/commit/cabcb1ff2eb5100885c5684c2cfb6896ccadd97b))
* Add `UpdateConversionEvent` method to the Admin API v1 beta ([7c8f27f](https://github.com/googleapis/python-analytics-admin/commit/7c8f27f204724ff46f8400effb97dfc786a4fcb5))
* Add the `ConversionCountingMethod` enum ([7c8f27f](https://github.com/googleapis/python-analytics-admin/commit/7c8f27f204724ff46f8400effb97dfc786a4fcb5))
* Add the `counting_method` field to the `ConversionEvent` type ([7c8f27f](https://github.com/googleapis/python-analytics-admin/commit/7c8f27f204724ff46f8400effb97dfc786a4fcb5))
* Add the `ITEM` option to the `DimensionScope` enum ([7c8f27f](https://github.com/googleapis/python-analytics-admin/commit/7c8f27f204724ff46f8400effb97dfc786a4fcb5))
* Add the `skadnetwork_conversion_value_schema` field to the `ChangeHistoryResource.resource` oneof type ([cabcb1f](https://github.com/googleapis/python-analytics-admin/commit/cabcb1ff2eb5100885c5684c2cfb6896ccadd97b))
* Add the `SKADNETWORK_CONVERSION_VALUE_SCHEMA` option to the `ChangeHistoryResourceType` enum ([cabcb1f](https://github.com/googleapis/python-analytics-admin/commit/cabcb1ff2eb5100885c5684c2cfb6896ccadd97b))
* Make the field `default_uri` of `WebStreamData` mutable ([7c8f27f](https://github.com/googleapis/python-analytics-admin/commit/7c8f27f204724ff46f8400effb97dfc786a4fcb5))


### Bug Fixes

* Add the missing `REQUIRED` annotation to the `update_mask` field of `UpdateMeasurementProtocolSecretRequest` ([7c8f27f](https://github.com/googleapis/python-analytics-admin/commit/7c8f27f204724ff46f8400effb97dfc786a4fcb5))
* Rename the `enterprise_daily_export_enabled` field to `fresh_daily_export_enabled` in the `BigQueryLink` resource ([cabcb1f](https://github.com/googleapis/python-analytics-admin/commit/cabcb1ff2eb5100885c5684c2cfb6896ccadd97b))


### Documentation

* Minor formatting ([#379](https://github.com/googleapis/python-analytics-admin/issues/379)) ([ab8a30b](https://github.com/googleapis/python-analytics-admin/commit/ab8a30b637284a9526fae5b85e05b1c54891c609))

## [0.20.0](https://github.com/googleapis/python-analytics-admin/compare/v0.19.0...v0.20.0) (2023-08-10)


### Features

* **v1alpha:** Add `UpdateConversionEvent` method to the Admin API v1 alpha ([7685881](https://github.com/googleapis/python-analytics-admin/commit/7685881c45f9a58158ccf8dbb625c9d8f91bc4b2))
* **v1alpha:** Add the `ConversionCountingMethod` enum ([7685881](https://github.com/googleapis/python-analytics-admin/commit/7685881c45f9a58158ccf8dbb625c9d8f91bc4b2))
* **v1alpha:** Add the `counting_method` field to the `ConversionEvent` type ([7685881](https://github.com/googleapis/python-analytics-admin/commit/7685881c45f9a58158ccf8dbb625c9d8f91bc4b2))


### Bug Fixes

* **v1alpha:** Rename the `intraday_export_enabled` field to `enterprise_export_enabled`  in the `BigQueryLink` resource ([7685881](https://github.com/googleapis/python-analytics-admin/commit/7685881c45f9a58158ccf8dbb625c9d8f91bc4b2))

## [0.19.0](https://github.com/googleapis/python-analytics-admin/compare/v0.18.1...v0.19.0) (2023-07-27)


### Bug Fixes

* **v1alpha:** Rename enum from `ADS_PREFERRED_LAST_CLICK` to `GOOGLE_PAID_CHANNELS_LAST_CLICK` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `ADS_PREFERRED` to `GOOGLE_PAID_CHANNELS` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL_DATA_DRIVEN` to `PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL_FIRST_CLICK` to `PAID_AND_ORGANIC_CHANNELS_FIRST_CLICK` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL_LAST_CLICK` to `PAID_AND_ORGANIC_CHANNELS_LAST_CLICK` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL_LINEAR` to `PAID_AND_ORGANIC_CHANNELS_LINEAR` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL_POSITION_BASED` to `PAID_AND_ORGANIC_CHANNELS_POSITION_BASED` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL_TIME_DECAY` to `PAID_AND_ORGANIC_CHANNELS_TIME_DECAY` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))
* **v1alpha:** Rename enum from `CROSS_CHANNEL` to `PAID_AND_ORGANIC_CHANNELS` ([9a644b5](https://github.com/googleapis/python-analytics-admin/commit/9a644b5ca12959e086301313853c7777405ab7f3))

## [0.18.1](https://github.com/googleapis/python-analytics-admin/compare/v0.18.0...v0.18.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#355](https://github.com/googleapis/python-analytics-admin/issues/355)) ([2dfee7b](https://github.com/googleapis/python-analytics-admin/commit/2dfee7b3e825133d8c406d7a15c68f3ac535198c))

## [0.18.0](https://github.com/googleapis/python-analytics-admin/compare/v0.17.0...v0.18.0) (2023-06-21)


### Features

* Add `AdsWebConversionDataExportScope` enum ([d3aeb71](https://github.com/googleapis/python-analytics-admin/commit/d3aeb7186c53a69b53f7d81dc23108cfd8c6ab78))
* Add the `ads_web_conversion_data_export_scope` field to the `ReportingAttributionModel` type ([d3aeb71](https://github.com/googleapis/python-analytics-admin/commit/d3aeb7186c53a69b53f7d81dc23108cfd8c6ab78))
* Update the `default_uri` field of the `WebStreamData` type to be mutable ([d3aeb71](https://github.com/googleapis/python-analytics-admin/commit/d3aeb7186c53a69b53f7d81dc23108cfd8c6ab78))


### Documentation

* Announce the deprecation of first-click, linear, time-decay and position-based attribution models  ([d3aeb71](https://github.com/googleapis/python-analytics-admin/commit/d3aeb7186c53a69b53f7d81dc23108cfd8c6ab78))

## [0.17.0](https://github.com/googleapis/python-analytics-admin/compare/v0.16.0...v0.17.0) (2023-05-31)


### Features

* **v1alpha:** Add `AdSenseLink` type ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `audience`, `event_create_rule` fields to the `ChangeHistoryResource.resource` oneof field ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `AUDIENCE`, `EVENT_CREATE_RULE` options to the `ChangeHistoryResourceType` enum ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `ChannelGroupFilter`, `ChannelGroupFilterExpression`, `ChannelGroupFilterExpressionList`, `GroupingRule`, `ChannelGroup` types ([2ef0b67](https://github.com/googleapis/python-analytics-admin/commit/2ef0b674161c721ff854fdcd7debbfc8552a9ef8))
* **v1alpha:** Add `CreateEventCreateRule`, `UpdateEventCreateRule`,`DeleteEventCreateRule`, `ListEventCreateRules` methods ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `EventCreateRule`, `MatchingCondition` types ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `FetchConnectedGa4Property` method ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `GetAdSenseLink`, `CreateAdSenseLink`, `DeleteAdSenseLink`, `ListAdSenseLinks` methods ([e3b5b03](https://github.com/googleapis/python-analytics-admin/commit/e3b5b03b937d3bdd827419be1ca9a10c79691823))
* **v1alpha:** Add `GetChannelGroup`, `ListChannelGroups`, `CreateChannelGroup`, `UpdateChannelGroup` methods ([2ef0b67](https://github.com/googleapis/python-analytics-admin/commit/2ef0b674161c721ff854fdcd7debbfc8552a9ef8))
* **v1alpha:** Add FetchConnectedGa4Property method ([2ef0b67](https://github.com/googleapis/python-analytics-admin/commit/2ef0b674161c721ff854fdcd7debbfc8552a9ef8))

## [0.16.0](https://github.com/googleapis/python-analytics-admin/compare/v0.15.0...v0.16.0) (2023-03-24)


### Features

* **v1alpha:** Add `enhanced_measurement_settings` option to the `ChangeHistoryResource.resource` oneof field ([49c9f02](https://github.com/googleapis/python-analytics-admin/commit/49c9f022ac5efd2df7e0e82080810d9e26d81376))
* **v1alpha:** Add `ENHANCED_MEASUREMENT_SETTINGS` option to the `ChangeHistoryResourceType` enum ([49c9f02](https://github.com/googleapis/python-analytics-admin/commit/49c9f022ac5efd2df7e0e82080810d9e26d81376))
* **v1alpha:** Add `intraday_export_enabled` field to the `BigQueryLink` resource ([49c9f02](https://github.com/googleapis/python-analytics-admin/commit/49c9f022ac5efd2df7e0e82080810d9e26d81376))
* **v1alpha:** Add account-level binding for the `RunAccessReport` method ([49c9f02](https://github.com/googleapis/python-analytics-admin/commit/49c9f022ac5efd2df7e0e82080810d9e26d81376))
* **v1beta:** Add `AccessDimension`, `AccessMetric`, `AccessDateRange`, `AccessFilterExpression`, `AccessFilterExpressionList`, `AccessFilter`, `AccessStringFilter`, `AccessInListFilter`, `AccessNumericFilter`, `AccessBetweenFilter`, `NumericValue`, `AccessOrderBy`, `AccessDimensionHeader`, `AccessMetricHeader`, `AccessRow`, `AccessDimensionValue`, `AccessMetricValue`, `AccessQuota`, `AccessQuotaStatus` types ([c397e0a](https://github.com/googleapis/python-analytics-admin/commit/c397e0a818b693e0d53b312e0e31aeb060828603))
* **v1beta:** Add RunAccessReport method (with bindings for account and property resources) ([c397e0a](https://github.com/googleapis/python-analytics-admin/commit/c397e0a818b693e0d53b312e0e31aeb060828603))


### Documentation

* Fix formatting of request arg in docstring ([#335](https://github.com/googleapis/python-analytics-admin/issues/335)) ([5c24a33](https://github.com/googleapis/python-analytics-admin/commit/5c24a33512e1ece8904a70c7dd6bd666f2e527d1))

## [0.15.0](https://github.com/googleapis/python-analytics-admin/compare/v0.14.1...v0.15.0) (2023-02-28)


### Features

* Add `BigQueryLink`, `SearchAds360Link` resource types to the Admin API v1alpha ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Add `EXPANDED_DATA_SET`, `CHANNEL_GROUP` values to `ChangeHistoryResourceType` enum ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Add `GetBigQueryLink`, `ListBigQueryLinks` methods to the Admin API v1alpha ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Add `search_ads_360_link`, `expanded_data_set`, `bigquery_link` values to ChangeHistoryResource.resource oneof field ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Add `SetAutomatedGa4ConfigurationOptOut`, `FetchAutomatedGa4ConfigurationOptOut` methods to the Admin API v1alpha ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Add `tokens_per_project_per_hour` field to `AccessQuota` type ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Add GetSearchAds360Link, ListSearchAds360Links, CreateSearchAds360Link, DeleteSearchAds360Link, UpdateSearchAds360Link methods to the Admin API v1alpha ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* **v1alpha:** Add `AccessBinding`, `ExpandedDataSet`, `ExpandedDataSetFilter`, `ExpandedDataSetFilterExpression`, `ExpandedDataSetFilterExpressionList` resource types ([1d2897e](https://github.com/googleapis/python-analytics-admin/commit/1d2897e0f29cec3101835a9955a79d773aeece52))
* **v1alpha:** Add `CreateAccessBinding`, `GetAccessBinding`, `UpdateAccessBinding`, `DeleteAccessBinding`, `ListAccessBindings`, `BatchCreateAccessBindings`, `BatchGetAccessBindings`, `BatchUpdateAccessBindings`, `BatchDeleteAccessBindings` methods ([1d2897e](https://github.com/googleapis/python-analytics-admin/commit/1d2897e0f29cec3101835a9955a79d773aeece52))
* **v1alpha:** Add `GetExpandedDataSet`, `ListExpandedDataSets`, `CreateExpandedDataSet`, `UpdateExpandedDataSet`, `DeleteExpandedDataSet` methods ([1d2897e](https://github.com/googleapis/python-analytics-admin/commit/1d2897e0f29cec3101835a9955a79d773aeece52))


### Bug Fixes

* Remove `LESS_THAN_OR_EQUAL`, `GREATER_THAN_OR_EQUAL` values from NumericFilter.Operation enum ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))
* Remove `PARTIAL_REGEXP` value from StringFilter.MatchType enum ([efd4b20](https://github.com/googleapis/python-analytics-admin/commit/efd4b20ba5f49c38668f3b8c9c4ff365b44752da))

## [0.14.1](https://github.com/googleapis/python-analytics-admin/compare/v0.14.0...v0.14.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([b43c855](https://github.com/googleapis/python-analytics-admin/commit/b43c855e3434f31612e4744559f13508d7f6f071))


### Documentation

* Add documentation for enums ([b43c855](https://github.com/googleapis/python-analytics-admin/commit/b43c855e3434f31612e4744559f13508d7f6f071))

## [0.14.0](https://github.com/googleapis/python-analytics-admin/compare/v0.13.0...v0.14.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#313](https://github.com/googleapis/python-analytics-admin/issues/313)) ([5a39a38](https://github.com/googleapis/python-analytics-admin/commit/5a39a3841f7c5f78dd1a36bfd76a86e3cb0ad2e6))

## [0.13.0](https://github.com/googleapis/python-analytics-admin/compare/v0.12.0...v0.13.0) (2022-12-14)


### Features

* Add typing to proto.Message based class  attributes ([6fb3129](https://github.com/googleapis/python-analytics-admin/commit/6fb3129a9a558cf1e08d472ae1aa516a9c9bf132))


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([28dc93b](https://github.com/googleapis/python-analytics-admin/commit/28dc93b4609d3e0934a1841e407749ab16c00d09))
* Drop usage of pkg_resources ([28dc93b](https://github.com/googleapis/python-analytics-admin/commit/28dc93b4609d3e0934a1841e407749ab16c00d09))
* Fix timeout default values ([28dc93b](https://github.com/googleapis/python-analytics-admin/commit/28dc93b4609d3e0934a1841e407749ab16c00d09))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([6fb3129](https://github.com/googleapis/python-analytics-admin/commit/6fb3129a9a558cf1e08d472ae1aa516a9c9bf132))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([28dc93b](https://github.com/googleapis/python-analytics-admin/commit/28dc93b4609d3e0934a1841e407749ab16c00d09))
* Updates the `properties_run_access_report` sample to return aggregated data instead of individual data access records ([#298](https://github.com/googleapis/python-analytics-admin/issues/298)) ([86568d1](https://github.com/googleapis/python-analytics-admin/commit/86568d1e39d19f3e51996dd6e319c40110daebaa))

## [0.12.0](https://github.com/googleapis/python-analytics-admin/compare/v0.11.2...v0.12.0) (2022-11-07)


### Features

* add support for `google.analytics.admin.__version__` ([380b426](https://github.com/googleapis/python-analytics-admin/commit/380b4264003b17b802b7099b98837694cd0b87d1))


### Bug Fixes

* Add dict typing for client_options ([380b426](https://github.com/googleapis/python-analytics-admin/commit/380b4264003b17b802b7099b98837694cd0b87d1))


### Documentation

* Add a sample for runAccessReport method ([#289](https://github.com/googleapis/python-analytics-admin/issues/289)) ([6aa8f8c](https://github.com/googleapis/python-analytics-admin/commit/6aa8f8c6fe1a2c208e601cd21521b76645430ec4))

## [0.11.2](https://github.com/googleapis/python-analytics-admin/compare/v0.11.1...v0.11.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#283](https://github.com/googleapis/python-analytics-admin/issues/283)) ([e686492](https://github.com/googleapis/python-analytics-admin/commit/e6864926c0f2691ed6233858969634fc40c93e5a))
* **deps:** require google-api-core&gt;=1.33.2 ([e686492](https://github.com/googleapis/python-analytics-admin/commit/e6864926c0f2691ed6233858969634fc40c93e5a))

## [0.11.1](https://github.com/googleapis/python-analytics-admin/compare/v0.11.0...v0.11.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#278](https://github.com/googleapis/python-analytics-admin/issues/278)) ([c464f38](https://github.com/googleapis/python-analytics-admin/commit/c464f3811f361c05e48b44c0ce60139f40d1fe44))

## [0.11.0](https://github.com/googleapis/python-analytics-admin/compare/v0.10.1...v0.11.0) (2022-09-12)


### Features

* Enable REST transport support ([#265](https://github.com/googleapis/python-analytics-admin/issues/265)) ([c220210](https://github.com/googleapis/python-analytics-admin/commit/c220210adf0093a1257d8e91209488c1dec7602b))


### Bug Fixes

* **deps:** require google-api-core>=1.33.0,>=2.8.0 ([c220210](https://github.com/googleapis/python-analytics-admin/commit/c220210adf0093a1257d8e91209488c1dec7602b))
* **deps:** require protobuf >= 3.20.1 ([c220210](https://github.com/googleapis/python-analytics-admin/commit/c220210adf0093a1257d8e91209488c1dec7602b))

## [0.10.1](https://github.com/googleapis/python-analytics-admin/compare/v0.10.0...v0.10.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#250](https://github.com/googleapis/python-analytics-admin/issues/250)) ([84a8df1](https://github.com/googleapis/python-analytics-admin/commit/84a8df140081c5095d71fa9dd99b83549d07c9c6))
* **deps:** require proto-plus >= 1.22.0 ([84a8df1](https://github.com/googleapis/python-analytics-admin/commit/84a8df140081c5095d71fa9dd99b83549d07c9c6))

## [0.10.0](https://github.com/googleapis/python-analytics-admin/compare/v0.9.0...v0.10.0) (2022-08-05)


### Features

* **v1alpha:** add `GetAttributionSettings`, `UpdateAttributionSettings` methods ([6e6b741](https://github.com/googleapis/python-analytics-admin/commit/6e6b74144706ffe6ecd898d11f9eb41e46d77c94))
* **v1alpha:** add `GetAudience`, 'ListAudience', 'CreateAudience', 'UpdateAudience', 'ArchiveAudience' methods ([6e6b741](https://github.com/googleapis/python-analytics-admin/commit/6e6b74144706ffe6ecd898d11f9eb41e46d77c94))
* **v1alpha:** add `RunAccessReport` method ([#246](https://github.com/googleapis/python-analytics-admin/issues/246)) ([6e6b741](https://github.com/googleapis/python-analytics-admin/commit/6e6b74144706ffe6ecd898d11f9eb41e46d77c94))

## [0.9.0](https://github.com/googleapis/python-analytics-admin/compare/v0.8.2...v0.9.0) (2022-07-20)


### Features

* add audience parameter ([dc6107c](https://github.com/googleapis/python-analytics-admin/commit/dc6107cbe784ac6e4dcd2b2a0fd118ed1a2b929e))
* release the Google Analytics Admin API V1 Beta ([dc6107c](https://github.com/googleapis/python-analytics-admin/commit/dc6107cbe784ac6e4dcd2b2a0fd118ed1a2b929e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#236](https://github.com/googleapis/python-analytics-admin/issues/236)) ([dc6107c](https://github.com/googleapis/python-analytics-admin/commit/dc6107cbe784ac6e4dcd2b2a0fd118ed1a2b929e))
* require python 3.7+ ([#239](https://github.com/googleapis/python-analytics-admin/issues/239)) ([ec0580e](https://github.com/googleapis/python-analytics-admin/commit/ec0580e77d8b7ec395f0a2d0979b336ba44a19fd))

## [0.8.2](https://github.com/googleapis/python-analytics-admin/compare/v0.8.1...v0.8.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#227](https://github.com/googleapis/python-analytics-admin/issues/227)) ([2dc98b3](https://github.com/googleapis/python-analytics-admin/commit/2dc98b354cefb6eeafe2a8065b3d85e60c0c7824))


### Documentation

* fix changelog header to consistent size ([#228](https://github.com/googleapis/python-analytics-admin/issues/228)) ([2385b9b](https://github.com/googleapis/python-analytics-admin/commit/2385b9b9b96abac09b9adebd6d462d8a95afe356))

## [0.8.1](https://github.com/googleapis/python-analytics-admin/compare/v0.8.0...v0.8.1) (2022-05-13)


### Bug Fixes

* CustomDimension and CustomMetric resource configuration ([#222](https://github.com/googleapis/python-analytics-admin/issues/222)) ([79470bd](https://github.com/googleapis/python-analytics-admin/commit/79470bdd437d3fe45cdcf1e89b13f6e1b289bd24))

## [0.8.0](https://github.com/googleapis/python-analytics-admin/compare/v0.7.2...v0.8.0) (2022-03-07)


### Features

* add `CreateDataStream`, `DeleteDataStream`, `UpdateDataStream`, `ListDataStreams` operations to support the new `DataStream` resource ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add `DISPLAY_VIDEO_360_ADVERTISER_LINK`,  `DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL` fields to `ChangeHistoryResourceType` enum ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add `restricted_metric_type` field to the `CustomMetric` resource ([aeb64bf](https://github.com/googleapis/python-analytics-admin/commit/aeb64bfc7653de24c84f54f9a921c4dc3f63a31b))
* add api key support ([#185](https://github.com/googleapis/python-analytics-admin/issues/185)) ([2ec0a0b](https://github.com/googleapis/python-analytics-admin/commit/2ec0a0b648edcfb3b76bf847a4463cbb551e1997))
* add the `account` field to the `Property` type ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add the AcknowledgeUserDataCollection operation ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add the new resource type `DataStream`, which is planned to eventually replace `WebDataStream`, `IosAppDataStream`, `AndroidAppDataStream` resources ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* move the `GlobalSiteTag` resource from the property level to the data stream level ([aeb64bf](https://github.com/googleapis/python-analytics-admin/commit/aeb64bfc7653de24c84f54f9a921c4dc3f63a31b))
* remove `WebDataStream`, `IosAppDataStream`, `AndroidAppDataStream` resources ([#195](https://github.com/googleapis/python-analytics-admin/issues/195)) ([aeb64bf](https://github.com/googleapis/python-analytics-admin/commit/aeb64bfc7653de24c84f54f9a921c4dc3f63a31b)), closes [#184](https://github.com/googleapis/python-analytics-admin/issues/184)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#194](https://github.com/googleapis/python-analytics-admin/issues/194)) ([f2b9bc3](https://github.com/googleapis/python-analytics-admin/commit/f2b9bc38695697dfadc451eb102cd8b4e4e90c34))
* **deps:** require proto-plus>=1.15.0 ([f2b9bc3](https://github.com/googleapis/python-analytics-admin/commit/f2b9bc38695697dfadc451eb102cd8b4e4e90c34))
* remove `GetEnhancedMeasurementSettings`, `UpdateEnhancedMeasurementSettingsRequest`, `UpdateEnhancedMeasurementSettingsRequest` operations from the API ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* resolve DuplicateCredentialArgs error when using credentials_file ([49c8857](https://github.com/googleapis/python-analytics-admin/commit/49c8857d28b7e2a9c563046d0b0cdee39e3b312e))


### Documentation

* add autogenerated code snippets ([323815a](https://github.com/googleapis/python-analytics-admin/commit/323815a140de25fe75e7e9c9f45fdaa45c71ce35))
* update the documentation with a new list of valid values for `UserLink.direct_roles` field ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))

## [0.7.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.7.1...v0.7.2) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([be96ebc](https://www.github.com/googleapis/python-analytics-admin/commit/be96ebc5d99e3d3ea1883ce22fafa95847825fb3))
* **deps:** require google-api-core >= 1.28.0 ([be96ebc](https://www.github.com/googleapis/python-analytics-admin/commit/be96ebc5d99e3d3ea1883ce22fafa95847825fb3))


### Documentation

* list oneofs in docstring ([be96ebc](https://www.github.com/googleapis/python-analytics-admin/commit/be96ebc5d99e3d3ea1883ce22fafa95847825fb3))

## [0.7.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.7.0...v0.7.1) (2021-10-19)


### Documentation

* **samples:** add samples for Measurement Protocol Secrets management methods ([#152](https://www.github.com/googleapis/python-analytics-admin/issues/152)) ([e264571](https://www.github.com/googleapis/python-analytics-admin/commit/e2645719d6fc518857f64482c48f60e1e0963fc7))
* **samples:** add samples for Conversion Event management methods ([#153](https://www.github.com/googleapis/python-analytics-admin/issues/153)) ([126f271](https://www.github.com/googleapis/python-analytics-admin/commit/126f2711c9fdedaa7cddfe8b3c7bdaff03d0297e))

## [0.7.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.6.0...v0.7.0) (2021-10-12)


### Features

* add support for python 3.10 ([#150](https://www.github.com/googleapis/python-analytics-admin/issues/150)) ([f6d2033](https://www.github.com/googleapis/python-analytics-admin/commit/f6d2033e054e0c13e1134e95ec822a93bf227798))

## [0.6.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.5.2...v0.6.0) (2021-10-08)


### Features

* add context manager support in client ([#146](https://www.github.com/googleapis/python-analytics-admin/issues/146)) ([f1559b6](https://www.github.com/googleapis/python-analytics-admin/commit/f1559b6074e75e453e0f3c6f32a21bfac487e562))

## [0.5.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.5.1...v0.5.2) (2021-10-07)


### Bug Fixes

* improper types in pagers generation ([aa076a9](https://www.github.com/googleapis/python-analytics-admin/commit/aa076a9bde90aaa2ceeaaa580c499a42e212b39f))


### Documentation

* add samples for accounts.search_change_history_events() method ([#137](https://www.github.com/googleapis/python-analytics-admin/issues/137)) ([c299b37](https://www.github.com/googleapis/python-analytics-admin/commit/c299b370c42a8684faa86f5bb5f65b3da8a2d0a8))

## [0.5.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.5.0...v0.5.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([256c880](https://www.github.com/googleapis/python-analytics-admin/commit/256c880c486761e32c00ece8ee40ee3a23d87bdb))

## [0.5.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.3...v0.5.0) (2021-08-25)


### Features

* add `CancelDisplayVideo360AdvertiserLinkProposal` method to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `CreateDisplayVideo360AdvertiserLink`, `DeleteDisplayVideo360AdvertiserLink` methods to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `custom` output only field to `ConversionEvent` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `data_retention_settings` fields to `ChangeHistoryChange.resource` oneof field. ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `DeleteDisplayVideo360AdvertiserLinkProposal` method to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `display_video_360_advertiser_link_proposal` fields to `ChangeHistoryChange.resource` oneof field. ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `display_video_360_advertiser_link` fields to `ChangeHistoryChange.resource` oneof field. ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `DisplayVideo360AdvertiserLink`, `LinkProposalState` types to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `GetDataRetentionSettings`, `UpdateDataRetentionSettings` methods to the API ([#119](https://www.github.com/googleapis/python-analytics-admin/issues/119)) ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `GetDisplayVideo360AdvertiserLink`, `ListDisplayVideo360AdvertiserLinks` methods to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `GetDisplayVideo360AdvertiserLinkProposal`, `ListDisplayVideo360AdvertiserLinkProposals` methods to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `LinkProposalInitiatingProduct`, `ServiceLevel`, `DataRetentionSettings` types to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `LinkProposalStatusDetails`, `DisplayVideo360AdvertiserLinkProposal` types to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `service_level` field to `Property` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* change `measurement_unit` field to mutable in `CustomMetric` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))


### Bug Fixes

* remove `maximum_user_access` field from `FirebaseLink` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* remove `MaximumUserAccess` enum from the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* remove `UpdateFirebaseLink` method from the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* rename `email_address` field of `GoogleAdsLink` type to `creator_email_address` ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* rename `is_deletable` field of `ConversionEvent` type to `deletable` ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))

## [0.4.3](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.2...v0.4.3) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#107](https://www.github.com/googleapis/python-analytics-admin/issues/107)) ([dd2235c](https://www.github.com/googleapis/python-analytics-admin/commit/dd2235ca02ff481253dee5e90fa15f6c7bcfc4e8))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#102](https://www.github.com/googleapis/python-analytics-admin/issues/102)) ([99d607c](https://www.github.com/googleapis/python-analytics-admin/commit/99d607c5dc6ea562c4d70cb56c65b01e6c4d9e25))


### Miscellaneous Chores

* release as 0.4.3 ([#108](https://www.github.com/googleapis/python-analytics-admin/issues/108)) ([4dd86a1](https://www.github.com/googleapis/python-analytics-admin/commit/4dd86a139ecfcdab9b1ed847fe7c76fb578ca6af))

## [0.4.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.1...v0.4.2) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#101](https://www.github.com/googleapis/python-analytics-admin/issues/101)) ([cde3379](https://www.github.com/googleapis/python-analytics-admin/commit/cde3379e9b40082f69327b46ba0acdabe520c21b))

## [0.4.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.0...v0.4.1) (2021-06-30)


### Bug Fixes

* disable always_use_jwt_access ([5e3df32](https://www.github.com/googleapis/python-analytics-admin/commit/5e3df324aa9d428d63d80816d10ad7d2d7ef41c1))
* disable always_use_jwt_access ([#95](https://www.github.com/googleapis/python-analytics-admin/issues/95)) ([5e3df32](https://www.github.com/googleapis/python-analytics-admin/commit/5e3df324aa9d428d63d80816d10ad7d2d7ef41c1))

## [0.4.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.3.2...v0.4.0) (2021-06-23)


### Features

* add always_use_jwt_access ([#89](https://www.github.com/googleapis/python-analytics-admin/issues/89)) ([268fdec](https://www.github.com/googleapis/python-analytics-admin/commit/268fdec4dd859a42d1025f94812053311df149ce))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-analytics-admin/issues/1127)) ([#84](https://www.github.com/googleapis/python-analytics-admin/issues/84)) ([6ce863e](https://www.github.com/googleapis/python-analytics-admin/commit/6ce863e147dae3c1da40c27034a0ac42180c6303)), closes [#1126](https://www.github.com/googleapis/python-analytics-admin/issues/1126)

## [0.3.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.3.1...v0.3.2) (2021-06-16)


### Bug Fixes

* **deps:** add packaging requirement ([#80](https://www.github.com/googleapis/python-analytics-admin/issues/80)) ([6d99bcc](https://www.github.com/googleapis/python-analytics-admin/commit/6d99bcc3e940e4f6bc857e7d4ede53e01537c7ec))

## [0.3.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.3.0...v0.3.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#78](https://www.github.com/googleapis/python-analytics-admin/issues/78)) ([680a695](https://www.github.com/googleapis/python-analytics-admin/commit/680a695e446c979e30542cd4dc563028b126aef5))

## [0.3.0](https://www.github.com/googleapis/python-analytics-admin/compare/v1.0.0...v0.3.0) (2021-06-09)


### Features

* add `ConversionEvent` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `ConversionEvent` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomDimension` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomDimension` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomMetric` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomMetric` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `GetGoogleSignalsSettings`, `UpdateGoogleSignalsSettings` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `GoogleSignalsSettings`  type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `GoogleSignalsState`, `GoogleSignalsConsent` types ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `MeasurementProtocolSecret` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add MeasurementProtocolSecret methods to the API ([#71](https://www.github.com/googleapis/python-analytics-admin/issues/71)) ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* extend `ChangeHistoryResourceType` enum ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))


### Bug Fixes

* label `email_address` field of `UserLink` type as immutable ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* label `name` field of `UserLink` type as output only ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))


### Documentation

* add Admin API samples for account management methods ([#58](https://www.github.com/googleapis/python-analytics-admin/issues/58)) ([2ecc350](https://www.github.com/googleapis/python-analytics-admin/commit/2ecc350759cfa50f02c0f29f75b647e260cacec0))
* add Admin API samples for account management methods ([#65](https://www.github.com/googleapis/python-analytics-admin/issues/65)) ([a3fecc4](https://www.github.com/googleapis/python-analytics-admin/commit/a3fecc47bb329aeba3706b7d6f0b26196c3a8977))
* add Admin API samples for property stream management methods ([#68](https://www.github.com/googleapis/python-analytics-admin/issues/68)) ([27da97e](https://www.github.com/googleapis/python-analytics-admin/commit/27da97e4574baec81ba3c13be8aece1efa689f75))
* add Admin API samples for property user link management methods ([#67](https://www.github.com/googleapis/python-analytics-admin/issues/67)) ([aa55627](https://www.github.com/googleapis/python-analytics-admin/commit/aa5562777009bbdd21fdc39990b50ac5fb19cc53))
* add samples for Google Analytics property management methods ([#74](https://www.github.com/googleapis/python-analytics-admin/issues/74)) ([bdb85be](https://www.github.com/googleapis/python-analytics-admin/commit/bdb85bee0125db8199d6a2a3cf18fbcbd443070b))


### Miscellaneous Chores

* release 0.3.0 ([#75](https://www.github.com/googleapis/python-analytics-admin/issues/75)) ([243b6c5](https://www.github.com/googleapis/python-analytics-admin/commit/243b6c558078bee738b01220384bc04840d59bbe))

## [0.2.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.1.0...v0.2.0) (2021-01-20)


### ⚠ BREAKING CHANGES

* `update_mask` field is required for all Update operations
* rename `country_code` field to `region_code` in `Account`
* rename `url_query_parameter` field to `uri_query_parameter` in `EnhancedMeasurementSettings`
* remove `parent` field from `GoogleAdsLink`
* remove unused fields from `EnhancedMeasurementSettings` (#29)

### Features

* add ListAccountSummaries ([#20](https://www.github.com/googleapis/python-analytics-admin/issues/20)) ([04d05d7](https://www.github.com/googleapis/python-analytics-admin/commit/04d05d7436a752dba18cb04d0e6882b1670114d7))
* add pagination support for `ListFirebaseLinks` operation ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))


### Bug Fixes

* `update_mask` field is required for all Update operations ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* remove `parent` field from `GoogleAdsLink` ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* remove unused fields from `EnhancedMeasurementSettings` ([#29](https://www.github.com/googleapis/python-analytics-admin/issues/29)) ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* rename `country_code` field to `region_code` in `Account` ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* rename `url_query_parameter` field to `uri_query_parameter` in `EnhancedMeasurementSettings` ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))


### Documentation

* added a sample ([#9](https://www.github.com/googleapis/python-analytics-admin/issues/9)) ([60918d8](https://www.github.com/googleapis/python-analytics-admin/commit/60918d8896d37f32a19c3d5724611df5cc4d4619))

## 0.1.0 (2020-07-23)


### Features

* generate v1alpha ([496c679](https://www.github.com/googleapis/python-analytics-admin/commit/496c6792dab14ac680e5b80cc7af1de445023715))
