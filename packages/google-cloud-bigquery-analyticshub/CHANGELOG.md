# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-bigquery-analyticshub/#history

## [0.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.9.0...google-cloud-bigquery-analyticshub-v0.9.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.8.0...google-cloud-bigquery-analyticshub-v0.9.0) (2026-06-02)


### Features

* regenerate google-cloud-b packages (#17090) ([77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd](https://github.com/googleapis/google-cloud-python/commit/77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.7.0...google-cloud-bigquery-analyticshub-v0.8.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.6.0...google-cloud-bigquery-analyticshub-v0.7.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.5.0...google-cloud-bigquery-analyticshub-v0.6.0) (2025-11-06)


### Features

* add Stored Procedure Sharing support for analyticshub listings  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add tags support for Pub/Sub subscriptions  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.20...google-cloud-bigquery-analyticshub-v0.5.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.4.20](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.19...google-cloud-bigquery-analyticshub-v0.4.20) (2025-09-04)


### Features

* You can now configure listings for multiple regions for shared datasets and linked dataset replicas in BigQuery sharing ([92212a5](https://github.com/googleapis/google-cloud-python/commit/92212a516fe22966878a87b92e0180756506a4a3))

## [0.4.19](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.18...google-cloud-bigquery-analyticshub-v0.4.19) (2025-05-15)


### Features

* Add support for Analytics Hub & Marketplace Integration ([d875d05](https://github.com/googleapis/google-cloud-python/commit/d875d053acb170e1491dd774c93506b339524d45))
* Adding allow_only_metadata_sharing to Listing resource ([d875d05](https://github.com/googleapis/google-cloud-python/commit/d875d053acb170e1491dd774c93506b339524d45))
* Adding CommercialInfo message to the Listing and Subscription resources ([d875d05](https://github.com/googleapis/google-cloud-python/commit/d875d053acb170e1491dd774c93506b339524d45))
* Adding delete_commercial and revoke_commercial to DeleteListingRequest and RevokeSubscriptionRequest ([d875d05](https://github.com/googleapis/google-cloud-python/commit/d875d053acb170e1491dd774c93506b339524d45))
* Adding DestinationDataset to the Subscription resource ([d875d05](https://github.com/googleapis/google-cloud-python/commit/d875d053acb170e1491dd774c93506b339524d45))
* Adding routine field to the SharedResource message ([d875d05](https://github.com/googleapis/google-cloud-python/commit/d875d053acb170e1491dd774c93506b339524d45))

## [0.4.18](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.17...google-cloud-bigquery-analyticshub-v0.4.18) (2025-03-27)


### Features

* [google-cloud-bigquery-analyticshub] Support new feature Sharing Cloud Pubsub Streams via AH (GA) and Subscriber Email logging feature ([#13713](https://github.com/googleapis/google-cloud-python/issues/13713)) ([f6a55e3](https://github.com/googleapis/google-cloud-python/commit/f6a55e35fcfd5f58d3268fb3f7a46ffd761c7db3))

## [0.4.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.16...google-cloud-bigquery-analyticshub-v0.4.17) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([3a85796](https://github.com/googleapis/google-cloud-python/commit/3a85796774ebf728cbc9e82dc536316530ac78c1))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.4.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.15...google-cloud-bigquery-analyticshub-v0.4.16) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([4571dff](https://github.com/googleapis/google-cloud-python/commit/4571dff9614843c6944c8568bd234c6ac5197218))

## [0.4.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.14...google-cloud-bigquery-analyticshub-v0.4.15) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))
* Add support for reading selective GAPIC generation methods from service YAML ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))

## [0.4.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.13...google-cloud-bigquery-analyticshub-v0.4.14) (2024-12-12)


### Features

* Add support for opt-in debug logging ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))

## [0.4.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.12...google-cloud-bigquery-analyticshub-v0.4.13) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([4ed4108](https://github.com/googleapis/google-cloud-python/commit/4ed41088ab3cbadfe4de7fa170f172666015ed24))

## [0.4.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.11...google-cloud-bigquery-analyticshub-v0.4.12) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13200](https://github.com/googleapis/google-cloud-python/issues/13200)) ([19dc048](https://github.com/googleapis/google-cloud-python/commit/19dc0485852406b90743297bcf257020e6012593))

## [0.4.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.10...google-cloud-bigquery-analyticshub-v0.4.11) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([6e83a37](https://github.com/googleapis/google-cloud-python/commit/6e83a37612d9eb951cb0ef1e372ef4241f8afa59))

## [0.4.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.9...google-cloud-bigquery-analyticshub-v0.4.10) (2024-07-08)


### Features

* support Direct Table Access Toggle (Egress GA) ([94554f5](https://github.com/googleapis/google-cloud-python/commit/94554f56587f0f389f9253aceb32163de26e6488))
* support public directory self service for Listings/Exchanges ([94554f5](https://github.com/googleapis/google-cloud-python/commit/94554f56587f0f389f9253aceb32163de26e6488))


### Bug Fixes

* Allow Protobuf 5.x ([#12864](https://github.com/googleapis/google-cloud-python/issues/12864)) ([728b307](https://github.com/googleapis/google-cloud-python/commit/728b307ed0cc497685507a219e913f002f097132))


### Documentation

* A comment for message `DataExchange` is changed ([94554f5](https://github.com/googleapis/google-cloud-python/commit/94554f56587f0f389f9253aceb32163de26e6488))
* A comment for message `Listing` is changed ([94554f5](https://github.com/googleapis/google-cloud-python/commit/94554f56587f0f389f9253aceb32163de26e6488))

## [0.4.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.8...google-cloud-bigquery-analyticshub-v0.4.9) (2024-03-22)


### Features

* support output fields on DcrExchangeConfig specifying selective sharing behavior on a data clean room ([334d0b3](https://github.com/googleapis/google-cloud-python/commit/334d0b37db691d925a157eef82930d6d43faa5d6))
* support selective sharing on data clean room Listings ([334d0b3](https://github.com/googleapis/google-cloud-python/commit/334d0b37db691d925a157eef82930d6d43faa5d6))

## [0.4.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.7...google-cloud-bigquery-analyticshub-v0.4.8) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12382](https://github.com/googleapis/google-cloud-python/issues/12382)) ([d5db265](https://github.com/googleapis/google-cloud-python/commit/d5db2656c011be2264bd778244caf8e23d288c75))

## [0.4.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.6...google-cloud-bigquery-analyticshub-v0.4.7) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12281](https://github.com/googleapis/google-cloud-python/issues/12281)) ([62cf934](https://github.com/googleapis/google-cloud-python/commit/62cf934b140173d7b39e6c9ffa66e218b98260d4))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12304](https://github.com/googleapis/google-cloud-python/issues/12304)) ([c52e0cd](https://github.com/googleapis/google-cloud-python/commit/c52e0cdbddf44c96f642d8d596c5413c4006ba82))

## [0.4.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.5...google-cloud-bigquery-analyticshub-v0.4.6) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))

## [0.4.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.4...google-cloud-bigquery-analyticshub-v0.4.5) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12238](https://github.com/googleapis/google-cloud-python/issues/12238)) ([8701267](https://github.com/googleapis/google-cloud-python/commit/8701267fc9694844b9365024cd59354785247aa0))

## [0.4.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.3...google-cloud-bigquery-analyticshub-v0.4.4) (2023-12-07)


### Features

* Add support for python 3.12 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Introduce compatibility with native namespace packages ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Use `retry_async` instead of `retry` in async client ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))

## [0.4.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.2...google-cloud-bigquery-analyticshub-v0.4.3) (2023-09-30)


### Features

* add Subscription resource and RPCs ([a18915b](https://github.com/googleapis/google-cloud-python/commit/a18915b21668dd9869a2d94c92866613ac041db0))

## [0.4.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.1...google-cloud-bigquery-analyticshub-v0.4.2) (2023-08-03)


### Documentation

* Minor formatting ([#11543](https://github.com/googleapis/google-cloud-python/issues/11543)) ([8cc031e](https://github.com/googleapis/google-cloud-python/commit/8cc031e723350890b4ceb6e813f24c4bcde3d65f))

## [0.4.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.4.0...google-cloud-bigquery-analyticshub-v0.4.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11444](https://github.com/googleapis/google-cloud-python/issues/11444)) ([9aa301a](https://github.com/googleapis/google-cloud-python/commit/9aa301ae6ca3080cae286a19de9cdc1b796ab37d))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-analyticshub-v0.3.2...google-cloud-bigquery-analyticshub-v0.4.0) (2023-06-19)


### Bug Fixes

* Use `google.cloud.bigquery_analyticshub` to avoid conflict with `google.cloud.bigquery` ([fe65e8b](https://github.com/googleapis/google-cloud-python/commit/fe65e8b71b187b0825afcd6a7697280302b7d2fe))

## [0.3.2](https://github.com/googleapis/python-bigquery-analyticshub/compare/v0.3.1...v0.3.2) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#26](https://github.com/googleapis/python-bigquery-analyticshub/issues/26)) ([f306471](https://github.com/googleapis/python-bigquery-analyticshub/commit/f306471d6e75de32a430ec8e4fb24ee32a7faba0))

## [0.3.1](https://github.com/googleapis/python-bigquery-analyticshub/compare/v0.3.0...v0.3.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([14fee28](https://github.com/googleapis/python-bigquery-analyticshub/commit/14fee28c1c34bb90b4877ef1249f41602dd68c85))


### Documentation

* Add documentation for enums ([14fee28](https://github.com/googleapis/python-bigquery-analyticshub/commit/14fee28c1c34bb90b4877ef1249f41602dd68c85))

## [0.3.0](https://github.com/googleapis/python-bigquery-analyticshub/compare/v0.2.0...v0.3.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#13](https://github.com/googleapis/python-bigquery-analyticshub/issues/13)) ([794a4b0](https://github.com/googleapis/python-bigquery-analyticshub/commit/794a4b0567287ff3472e0ea5a84d6e16a998d63e))

## [0.2.0](https://github.com/googleapis/python-bigquery-analyticshub/compare/v0.1.1...v0.2.0) (2022-12-15)


### Features

* Add support for `google.cloud.bigquery.analyticshub.__version__` ([94635d0](https://github.com/googleapis/python-bigquery-analyticshub/commit/94635d09004db127100aa73656436be8cb11b400))
* Add typing to proto.Message based class attributes ([94635d0](https://github.com/googleapis/python-bigquery-analyticshub/commit/94635d09004db127100aa73656436be8cb11b400))


### Bug Fixes

* Add dict typing for client_options ([94635d0](https://github.com/googleapis/python-bigquery-analyticshub/commit/94635d09004db127100aa73656436be8cb11b400))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([919901e](https://github.com/googleapis/python-bigquery-analyticshub/commit/919901e4a15887b5f9a0bcf8326509d4962f9aab))
* Drop usage of pkg_resources ([919901e](https://github.com/googleapis/python-bigquery-analyticshub/commit/919901e4a15887b5f9a0bcf8326509d4962f9aab))
* Fix timeout default values ([919901e](https://github.com/googleapis/python-bigquery-analyticshub/commit/919901e4a15887b5f9a0bcf8326509d4962f9aab))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([94635d0](https://github.com/googleapis/python-bigquery-analyticshub/commit/94635d09004db127100aa73656436be8cb11b400))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([919901e](https://github.com/googleapis/python-bigquery-analyticshub/commit/919901e4a15887b5f9a0bcf8326509d4962f9aab))

## [0.1.1](https://github.com/googleapis/python-bigquery-analyticshub/compare/v0.1.0...v0.1.1) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#3](https://github.com/googleapis/python-bigquery-analyticshub/issues/3)) ([43e944c](https://github.com/googleapis/python-bigquery-analyticshub/commit/43e944c6e9ed24e8ae6b57535de18774e67f9b63))
* **deps:** require google-api-core&gt;=1.33.2 ([43e944c](https://github.com/googleapis/python-bigquery-analyticshub/commit/43e944c6e9ed24e8ae6b57535de18774e67f9b63))

## 0.1.0 (2022-10-03)


### Features

* Generate v1 ([4d355d7](https://github.com/googleapis/python-bigquery-analyticshub/commit/4d355d7157925af7c50f806202d09801a4881a72))

## Changelog
