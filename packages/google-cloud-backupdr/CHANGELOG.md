# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-backupdr/#history

## [0.10.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.10.2...google-cloud-backupdr-v0.10.3) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.10.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.10.1...google-cloud-backupdr-v0.10.2) (2026-09-17)


### Features

* **google/cloud/backupdr/v1beta:** add google-cloud-backupdr ([#18399](https://github.com/googleapis/google-cloud-python/issues/18399)) ([91b7ae7](https://github.com/googleapis/google-cloud-python/commit/91b7ae7ef0aaa626b58b0d00e1c7d4a247c7c126))

## [0.10.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.10.0...google-cloud-backupdr-v0.10.1) (2026-08-06)


### Features

* update googleapis and regenerate ([#17893](https://github.com/googleapis/google-cloud-python/issues/17893)) ([e70ab6f](https://github.com/googleapis/google-cloud-python/commit/e70ab6fd45edfec5ca0c865e01876f0ea4f09cae))

## [0.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.9.0...google-cloud-backupdr-v0.10.0) (2026-06-02)


### Features

* regenerate google-cloud-b packages (#17090) ([77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd](https://github.com/googleapis/google-cloud-python/commit/77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.8.0...google-cloud-backupdr-v0.9.0) (2026-03-26)


### Features

* Adding new workload specific fields for AlloyDB ([397ae5384b5fa2741d0f479ba7efc1612e1195da](https://github.com/googleapis/google-cloud-python/commit/397ae5384b5fa2741d0f479ba7efc1612e1195da))
* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.7.0...google-cloud-backupdr-v0.8.0) (2026-02-05)


### Documentation

* A comment for field `log_retention_days` in message `.google.cloud.backupdr.v1.BackupPlan` is changed ([fe0a0b4638a8f5301c30be43fd2f2898ddc6db37](https://github.com/googleapis/google-cloud-python/commit/fe0a0b4638a8f5301c30be43fd2f2898ddc6db37))


### Features

* Add support for AlloyDB backup and restore ([fe0a0b4638a8f5301c30be43fd2f2898ddc6db37](https://github.com/googleapis/google-cloud-python/commit/fe0a0b4638a8f5301c30be43fd2f2898ddc6db37))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.6.0...google-cloud-backupdr-v0.7.0) (2026-01-15)


### Features

* A new service `BackupDrProtectionSummary` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `BackupDrTemplateConfig` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `BackupLocation` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `PitrSettings` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `ListResourceBackupConfigsResponse` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `BackupConfigDetails` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `ResourceBackupConfig` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `BackupDrPlanConfig` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `BackupDrPlanRule` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new resource_definition `backupdr.googleapis.com/ResourceBackupConfig` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `ListResourceBackupConfigsRequest` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.5.0...google-cloud-backupdr-v0.6.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.4.0...google-cloud-backupdr-v0.5.0) (2025-12-04)


### Features

* Adding new fields for CMEK and Retention Inheritance features ([c958ebdfe9351d3d4e80d388a6e95804b515d030](https://github.com/googleapis/google-cloud-python/commit/c958ebdfe9351d3d4e80d388a6e95804b515d030))
* Adding `unreachable` field to `ListDataSourceReferences` API ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.3.0...google-cloud-backupdr-v0.4.0) (2025-11-06)


### Features

* Adding `source_resource` fields to Backup resource  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* Adding `ListDataSourceReferences` API  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* Adding new workload specific fields for Cloud SQL  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* Adding `FetchBackupsForResourceType` API  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.2.5...google-cloud-backupdr-v0.3.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.2.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.2.4...google-cloud-backupdr-v0.2.5) (2025-07-23)


### Features

* Add BackupPlanRevision resource and associated RPCs ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add DataSourceReference resource and associated RPCs ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add FetchBackupPlanAssociationsForResourceType RPC ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add new states to resources (UPDATING, UPLOADING) ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add ON_DEMAND_OPERATIONAL backup type ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add support for Cloud SQL backup and restore ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add support for GCE Disk backup and restore ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Add Update RPCs for BackupPlan and BackupPlanAssociation ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* Change BackupRule.standard_schedule to be OPTIONAL ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))


### Documentation

* A comment for field backup_retention_days in message .google.cloud.backupdr.v1.BackupRule is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field disks in message .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field hourly_frequency in message .google.cloud.backupdr.v1.StandardSchedule is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field network_interfaces in message .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field resource in message .google.cloud.backupdr.v1.BackupPlanAssociation is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field resource_policies in message .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field resource_type in message .google.cloud.backupdr.v1.BackupPlan is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))
* A comment for field resource_type in message .google.cloud.backupdr.v1.BackupPlanAssociation is changed ([0393818](https://github.com/googleapis/google-cloud-python/commit/03938180ed28d9f3f272a4fe7952ea9c0e31ec22))

## [0.2.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.2.3...google-cloud-backupdr-v0.2.4) (2025-06-11)


### Documentation

* Update import statement example in README ([eea9e6f](https://github.com/googleapis/google-cloud-python/commit/eea9e6f798406fec17a17dfd71e40fbeea42cf6a))

## [0.2.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.2.2...google-cloud-backupdr-v0.2.3) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([3a85796](https://github.com/googleapis/google-cloud-python/commit/3a85796774ebf728cbc9e82dc536316530ac78c1))

## [0.2.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.2.1...google-cloud-backupdr-v0.2.2) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([4571dff](https://github.com/googleapis/google-cloud-python/commit/4571dff9614843c6944c8568bd234c6ac5197218))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.2.0...google-cloud-backupdr-v0.2.1) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))
* Add support for reading selective GAPIC generation methods from service YAML ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.7...google-cloud-backupdr-v0.2.0) (2025-01-13)


### ⚠ BREAKING CHANGES

* Update field behavior of `resource_type` field in message `BackupPlanAssociation` to `REQUIRED`

### Features

* `ignore_backup_plan_references` added to the DeleteBackupVaultRequest ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* add enum to Backup Vault Access Restriction field ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* add InitializeServiceAPI ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* Update field behavior of `networks` field in message `ManagementServer` to `OPTIONAL` ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))


### Bug Fixes

* Update field behavior of `resource_type` field in message `BackupPlanAssociation` to `REQUIRED` ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))


### Documentation

* A comment for enum value `ACCESS_RESTRICTION_UNSPECIFIED` in enum `AccessRestriction` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `access_restriction` in message `.google.cloud.backupdr.v1.BackupVault` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `backup_retention_days` in message `.google.cloud.backupdr.v1.BackupRule` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `data_source` in message `.google.cloud.backupdr.v1.BackupPlanAssociation` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `last_backup_error` in message `.google.cloud.backupdr.v1.RuleConfigInfo` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `networks` in message `.google.cloud.backupdr.v1.ManagementServer` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `requested_cancellation` in message `.google.cloud.backupdr.v1.OperationMetadata` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `resource_type` in message `.google.cloud.backupdr.v1.BackupPlan` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `resource_type` in message `.google.cloud.backupdr.v1.BackupPlanAssociation` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `rule_id` in message `.google.cloud.backupdr.v1.RuleConfigInfo` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))
* A comment for field `uid` in message `.google.cloud.backupdr.v1.BackupVault` is changed ([b5cdea3](https://github.com/googleapis/google-cloud-python/commit/b5cdea3f1d59f67ff0bd01d1891abf948a4f5582))

## [0.1.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.6...google-cloud-backupdr-v0.1.7) (2024-12-12)


### Features

* Add support for opt-in debug logging ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))

## [0.1.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.5...google-cloud-backupdr-v0.1.6) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([4ed4108](https://github.com/googleapis/google-cloud-python/commit/4ed41088ab3cbadfe4de7fa170f172666015ed24))

## [0.1.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.4...google-cloud-backupdr-v0.1.5) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13200](https://github.com/googleapis/google-cloud-python/issues/13200)) ([19dc048](https://github.com/googleapis/google-cloud-python/commit/19dc0485852406b90743297bcf257020e6012593))

## [0.1.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.3...google-cloud-backupdr-v0.1.4) (2024-10-08)


### Features

* [google-cloud-backupdr] Client library for the backupvault api is added ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* Add backupplan proto ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* Add backupplanassociation proto ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* Add backupvault_ba proto ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* Add backupvault_gce proto ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))


### Documentation

* A comment for field `management_servers` in message `.google.cloud.backupdr.v1.ListManagementServersResponse` is changed ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* A comment for field `name` in message `.google.cloud.backupdr.v1.GetManagementServerRequest` is changed ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* A comment for field `oauth2_client_id` in message `.google.cloud.backupdr.v1.ManagementServer` is changed ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* A comment for field `parent` in message `.google.cloud.backupdr.v1.CreateManagementServerRequest` is changed ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* A comment for field `parent` in message `.google.cloud.backupdr.v1.ListManagementServersRequest` is changed ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))
* A comment for field `requested_cancellation` in message `.google.cloud.backupdr.v1.OperationMetadata` is changed ([27c262d](https://github.com/googleapis/google-cloud-python/commit/27c262d51c5d9f055152d9448f5fb6759da4bdb3))

## [0.1.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.2...google-cloud-backupdr-v0.1.3) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([6e83a37](https://github.com/googleapis/google-cloud-python/commit/6e83a37612d9eb951cb0ef1e372ef4241f8afa59))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.1...google-cloud-backupdr-v0.1.2) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12864](https://github.com/googleapis/google-cloud-python/issues/12864)) ([728b307](https://github.com/googleapis/google-cloud-python/commit/728b307ed0cc497685507a219e913f002f097132))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-backupdr-v0.1.0...google-cloud-backupdr-v0.1.1) (2024-06-24)


### Features

* A new field `satisfies_pzi` is added ([9e20534](https://github.com/googleapis/google-cloud-python/commit/9e205344d6b24d6cedced1d9c177be7652f54267))
* A new field `satisfies_pzs` is added ([9e20534](https://github.com/googleapis/google-cloud-python/commit/9e205344d6b24d6cedced1d9c177be7652f54267))
* Updated documentation URI ([9e20534](https://github.com/googleapis/google-cloud-python/commit/9e205344d6b24d6cedced1d9c177be7652f54267))

## 0.1.0 (2024-04-15)


### Features

* add initial files for google.cloud.backupdr.v1 ([#12552](https://github.com/googleapis/google-cloud-python/issues/12552)) ([d9222a9](https://github.com/googleapis/google-cloud-python/commit/d9222a97786ce1badae4561410ca5e09386a3377))

## Changelog
