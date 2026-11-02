# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-billing/#history

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.20.0...google-cloud-billing-v1.21.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.19.0...google-cloud-billing-v1.20.0) (2026-06-02)


### Features

* regenerate google-cloud-b packages (#17090) ([77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd](https://github.com/googleapis/google-cloud-python/commit/77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.18.0...google-cloud-billing-v1.19.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.17.0...google-cloud-billing-v1.18.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.16.3...google-cloud-billing-v1.17.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.16.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.16.2...google-cloud-billing-v1.16.3) (2025-06-11)


### Documentation

* Update import statement example in README ([8697120](https://github.com/googleapis/google-cloud-python/commit/869712032803cb31d93f3b16abc2abdb14f733a4))

## [1.16.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.16.1...google-cloud-billing-v1.16.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([1e43e75](https://github.com/googleapis/google-cloud-python/commit/1e43e75e99445373785b11381e0e859fa14bb485))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.16.0...google-cloud-billing-v1.16.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([4571dff](https://github.com/googleapis/google-cloud-python/commit/4571dff9614843c6944c8568bd234c6ac5197218))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.15.0...google-cloud-billing-v1.16.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))
* Add support for reading selective GAPIC generation methods from service YAML ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.14.1...google-cloud-billing-v1.15.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))
* added currency field to billing account message ([89157d6](https://github.com/googleapis/google-cloud-python/commit/89157d677acd4672d65c57ad5ac8f61ae90eaf18))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))

## [1.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.14.0...google-cloud-billing-v1.14.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([4ed4108](https://github.com/googleapis/google-cloud-python/commit/4ed41088ab3cbadfe4de7fa170f172666015ed24))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.6...google-cloud-billing-v1.14.0) (2024-10-24)


### Features

* Add support for  Python 3.13 ([6252476](https://github.com/googleapis/google-cloud-python/commit/6252476e5938352fb2417d098a1edcc08558fe10))

## [1.13.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.5...google-cloud-billing-v1.13.6) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([a6f7356](https://github.com/googleapis/google-cloud-python/commit/a6f7356f1549721f9fab83d4dcfa226cec1965d0))

## [1.13.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.4...google-cloud-billing-v1.13.5) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12864](https://github.com/googleapis/google-cloud-python/issues/12864)) ([728b307](https://github.com/googleapis/google-cloud-python/commit/728b307ed0cc497685507a219e913f002f097132))

## [1.13.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.3...google-cloud-billing-v1.13.4) (2024-06-24)


### Documentation

* Genereal documentation improvements ([73dd30d](https://github.com/googleapis/google-cloud-python/commit/73dd30dd4eac8721b5db7e664df1c885f5b3d65c))

## [1.13.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.2...google-cloud-billing-v1.13.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12382](https://github.com/googleapis/google-cloud-python/issues/12382)) ([d5db265](https://github.com/googleapis/google-cloud-python/commit/d5db2656c011be2264bd778244caf8e23d288c75))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.1...google-cloud-billing-v1.13.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12281](https://github.com/googleapis/google-cloud-python/issues/12281)) ([62cf934](https://github.com/googleapis/google-cloud-python/commit/62cf934b140173d7b39e6c9ffa66e218b98260d4))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12304](https://github.com/googleapis/google-cloud-python/issues/12304)) ([c52e0cd](https://github.com/googleapis/google-cloud-python/commit/c52e0cdbddf44c96f642d8d596c5413c4006ba82))


### Documentation

* [google-cloud-billing] Clarify that the parent field in the CreateBillingAccountRequest must be a billing account ([#12299](https://github.com/googleapis/google-cloud-python/issues/12299)) ([1ff477c](https://github.com/googleapis/google-cloud-python/commit/1ff477c9b959f1fc4b3b0e46721141702a47aff2))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.13.0...google-cloud-billing-v1.13.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.12.1...google-cloud-billing-v1.13.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12238](https://github.com/googleapis/google-cloud-python/issues/12238)) ([8701267](https://github.com/googleapis/google-cloud-python/commit/8701267fc9694844b9365024cd59354785247aa0))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.12.0...google-cloud-billing-v1.12.1) (2024-01-19)


### Documentation

* [google-cloud-billing] update comments ([#12202](https://github.com/googleapis/google-cloud-python/issues/12202)) ([9acf675](https://github.com/googleapis/google-cloud-python/commit/9acf675503176395452d5d5bd464fb20757f2ab8))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.11.5...google-cloud-billing-v1.12.0) (2023-12-07)


### Features

* Add support for python 3.12 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* added field BillingAccount.parent ([facc8ef](https://github.com/googleapis/google-cloud-python/commit/facc8ef7db22ce90a2459832bce8d3b9d034c5dc))
* added the MoveBillingAccount method, which allows changing which organization a billing account belongs to ([facc8ef](https://github.com/googleapis/google-cloud-python/commit/facc8ef7db22ce90a2459832bce8d3b9d034c5dc))
* Introduce compatibility with native namespace packages ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Use `retry_async` instead of `retry` in async client ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))

## [1.11.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.11.4...google-cloud-billing-v1.11.5) (2023-09-21)


### Documentation

* update service documentation ([#11686](https://github.com/googleapis/google-cloud-python/issues/11686)) ([3c1d20c](https://github.com/googleapis/google-cloud-python/commit/3c1d20cffeaa64ffa4d38bf766ba804d7c6bfdc8))

## [1.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.11.3...google-cloud-billing-v1.11.4) (2023-09-19)


### Documentation

* Minor formatting ([9487380](https://github.com/googleapis/google-cloud-python/commit/94873808ece8059b07644a0a49dedf8e2906900a))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.11.2...google-cloud-billing-v1.11.3) (2023-08-31)


### Documentation

* update comments ([#11598](https://github.com/googleapis/google-cloud-python/issues/11598)) ([aaa652e](https://github.com/googleapis/google-cloud-python/commit/aaa652ec54314e59c4343abef76a956b68fe8069))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.11.1...google-cloud-billing-v1.11.2) (2023-08-03)


### Documentation

* Minor formatting ([#11543](https://github.com/googleapis/google-cloud-python/issues/11543)) ([8cc031e](https://github.com/googleapis/google-cloud-python/commit/8cc031e723350890b4ceb6e813f24c4bcde3d65f))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.11.0...google-cloud-billing-v1.11.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11445](https://github.com/googleapis/google-cloud-python/issues/11445)) ([98bddda](https://github.com/googleapis/google-cloud-python/commit/98bdddafc821e2fc6e86a31965da0c46899aa229))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-billing-v1.10.1...google-cloud-billing-v1.11.0) (2023-06-19)


### Features

* added resource_reference for name in GetProjectBillingInfoRequest message ([#11409](https://github.com/googleapis/google-cloud-python/issues/11409)) ([1ec86ce](https://github.com/googleapis/google-cloud-python/commit/1ec86ce40ad760d2229acfefc85b2c8a0c1ddd05))

## [1.10.1](https://github.com/googleapis/python-billing/compare/v1.10.0...v1.10.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#244](https://github.com/googleapis/python-billing/issues/244)) ([4f0ec70](https://github.com/googleapis/python-billing/commit/4f0ec703cd725a5000529cfdcca06e94be39d53d))

## [1.10.0](https://github.com/googleapis/python-billing/compare/v1.9.1...v1.10.0) (2023-02-27)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#237](https://github.com/googleapis/python-billing/issues/237)) ([872e1dd](https://github.com/googleapis/python-billing/commit/872e1dd4a72e9a7c479e9da33324bb15c5cb9f70))

## [1.9.1](https://github.com/googleapis/python-billing/compare/v1.9.0...v1.9.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([7923a86](https://github.com/googleapis/python-billing/commit/7923a861af0a0e671701f3a2d99224e7de7a92a7))


### Documentation

* Add documentation for enums ([7923a86](https://github.com/googleapis/python-billing/commit/7923a861af0a0e671701f3a2d99224e7de7a92a7))

## [1.9.0](https://github.com/googleapis/python-billing/compare/v1.8.0...v1.9.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#228](https://github.com/googleapis/python-billing/issues/228)) ([5e14095](https://github.com/googleapis/python-billing/commit/5e140954e89a9d12655f107eb17d80274e7f00cc))

## [1.8.0](https://github.com/googleapis/python-billing/compare/v1.7.3...v1.8.0) (2022-12-15)


### Features

* Add support for `google.cloud.billing.__version__` ([76f87d4](https://github.com/googleapis/python-billing/commit/76f87d4c170d2305883a8744e1d9a4e5c952955f))
* Add typing to proto.Message based class attributes ([76f87d4](https://github.com/googleapis/python-billing/commit/76f87d4c170d2305883a8744e1d9a4e5c952955f))
* Added Sku.geo_taxonomy ([76f87d4](https://github.com/googleapis/python-billing/commit/76f87d4c170d2305883a8744e1d9a4e5c952955f))


### Bug Fixes

* Add dict typing for client_options ([76f87d4](https://github.com/googleapis/python-billing/commit/76f87d4c170d2305883a8744e1d9a4e5c952955f))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([4119740](https://github.com/googleapis/python-billing/commit/41197401fc024763cb96cc2090f2f22dbb58677c))
* Drop usage of pkg_resources ([4119740](https://github.com/googleapis/python-billing/commit/41197401fc024763cb96cc2090f2f22dbb58677c))
* Fix timeout default values ([4119740](https://github.com/googleapis/python-billing/commit/41197401fc024763cb96cc2090f2f22dbb58677c))
* More oauth scopes ([76f87d4](https://github.com/googleapis/python-billing/commit/76f87d4c170d2305883a8744e1d9a4e5c952955f))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([76f87d4](https://github.com/googleapis/python-billing/commit/76f87d4c170d2305883a8744e1d9a4e5c952955f))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([4119740](https://github.com/googleapis/python-billing/commit/41197401fc024763cb96cc2090f2f22dbb58677c))

## [1.7.3](https://github.com/googleapis/python-billing/compare/v1.7.2...v1.7.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#217](https://github.com/googleapis/python-billing/issues/217)) ([d974efc](https://github.com/googleapis/python-billing/commit/d974efc71c363f39f3f850d1960b8ae41ab9b478))

## [1.7.2](https://github.com/googleapis/python-billing/compare/v1.7.1...v1.7.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#215](https://github.com/googleapis/python-billing/issues/215)) ([153eeb3](https://github.com/googleapis/python-billing/commit/153eeb331703975d4037ff655592469ecfcf29f9))

## [1.7.1](https://github.com/googleapis/python-billing/compare/v1.7.0...v1.7.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#201](https://github.com/googleapis/python-billing/issues/201)) ([2b31ba8](https://github.com/googleapis/python-billing/commit/2b31ba8fa9558f7439b1aa6c53908e247a7f22eb))
* **deps:** require proto-plus >= 1.22.0 ([2b31ba8](https://github.com/googleapis/python-billing/commit/2b31ba8fa9558f7439b1aa6c53908e247a7f22eb))

## [1.7.0](https://github.com/googleapis/python-billing/compare/v1.6.1...v1.7.0) (2022-07-16)


### Features

* add audience parameter ([d159208](https://github.com/googleapis/python-billing/commit/d159208b453fe5748f28ab383d78c310cd69cfed))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#193](https://github.com/googleapis/python-billing/issues/193)) ([d159208](https://github.com/googleapis/python-billing/commit/d159208b453fe5748f28ab383d78c310cd69cfed))
* require python 3.7+ ([#195](https://github.com/googleapis/python-billing/issues/195)) ([025f324](https://github.com/googleapis/python-billing/commit/025f3245ac308953710a31e02b21b3faa0340eaf))

## [1.6.1](https://github.com/googleapis/python-billing/compare/v1.6.0...v1.6.1) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#185](https://github.com/googleapis/python-billing/issues/185)) ([2542e90](https://github.com/googleapis/python-billing/commit/2542e902b8c23cbb9b84d2e6e266689e80102884))


### Documentation

* fix changelog header to consistent size ([#186](https://github.com/googleapis/python-billing/issues/186)) ([0b7c05e](https://github.com/googleapis/python-billing/commit/0b7c05ea4038a68b8648e0594f5cd0c05255f381))

## [1.6.0](https://github.com/googleapis/python-billing/compare/v1.5.1...v1.6.0) (2022-05-05)


### Features

* AuditConfig for IAM v1 ([6ce587c](https://github.com/googleapis/python-billing/commit/6ce587c58fb76d0f2f2ff5c9bcfc25a8f307071d))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([6ce587c](https://github.com/googleapis/python-billing/commit/6ce587c58fb76d0f2f2ff5c9bcfc25a8f307071d))


### Documentation

* fix type in docstring for map fields ([6ce587c](https://github.com/googleapis/python-billing/commit/6ce587c58fb76d0f2f2ff5c9bcfc25a8f307071d))

## [1.5.1](https://github.com/googleapis/python-billing/compare/v1.5.0...v1.5.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#159](https://github.com/googleapis/python-billing/issues/159)) ([d5511db](https://github.com/googleapis/python-billing/commit/d5511dbae66858b39f95ab989a1049d84ea57e49))
* **deps:** require proto-plus>=1.15.0 ([d5511db](https://github.com/googleapis/python-billing/commit/d5511dbae66858b39f95ab989a1049d84ea57e49))

## [1.5.0](https://github.com/googleapis/python-billing/compare/v1.4.1...v1.5.0) (2022-02-26)


### Features

* add api key support ([#145](https://github.com/googleapis/python-billing/issues/145)) ([a434c2e](https://github.com/googleapis/python-billing/commit/a434c2eb1ec6a79c36409c6039f05501c9cfc113))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([7b94621](https://github.com/googleapis/python-billing/commit/7b94621dafbcda8a549dd849337ba51fa5305f56))

## [1.4.1](https://www.github.com/googleapis/python-billing/compare/v1.4.0...v1.4.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([11ee1bf](https://www.github.com/googleapis/python-billing/commit/11ee1bfd84cfddcdc60ee2500273f5016919eba1))
* **deps:** require google-api-core >= 1.28.0 ([11ee1bf](https://www.github.com/googleapis/python-billing/commit/11ee1bfd84cfddcdc60ee2500273f5016919eba1))


### Documentation

* list oneofs in docstring ([11ee1bf](https://www.github.com/googleapis/python-billing/commit/11ee1bfd84cfddcdc60ee2500273f5016919eba1))

## [1.4.0](https://www.github.com/googleapis/python-billing/compare/v1.3.4...v1.4.0) (2021-10-11)


### Features

* add context manager support in client ([#122](https://www.github.com/googleapis/python-billing/issues/122)) ([9ec2297](https://www.github.com/googleapis/python-billing/commit/9ec229702b9a116e2572dd10c3e40887dfd70f93))
* add trove classifier for python 3.10 ([#125](https://www.github.com/googleapis/python-billing/issues/125)) ([6b93726](https://www.github.com/googleapis/python-billing/commit/6b93726fba956a41edf7d71f4950c649bc87f96f))

## [1.3.4](https://www.github.com/googleapis/python-billing/compare/v1.3.3...v1.3.4) (2021-10-04)


### Bug Fixes

* improper types in pagers generation ([578aeef](https://www.github.com/googleapis/python-billing/commit/578aeefcde72f12063e54e86208e3c6c4b135885))

## [1.3.3](https://www.github.com/googleapis/python-billing/compare/v1.3.2...v1.3.3) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([51f7055](https://www.github.com/googleapis/python-billing/commit/51f7055f3a992902f60342de389ec261147e98af))

## [1.3.2](https://www.github.com/googleapis/python-billing/compare/v1.3.1...v1.3.2) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#101](https://www.github.com/googleapis/python-billing/issues/101)) ([261507e](https://www.github.com/googleapis/python-billing/commit/261507e86d5e14a435fa74dea96feff187cd4f87))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#97](https://www.github.com/googleapis/python-billing/issues/97)) ([05b63b3](https://www.github.com/googleapis/python-billing/commit/05b63b3f88cb7cbc77db9daedf34db5617f93ca8))


### Miscellaneous Chores

* release as 1.3.2 ([#102](https://www.github.com/googleapis/python-billing/issues/102)) ([da74027](https://www.github.com/googleapis/python-billing/commit/da74027594f06705a9f6c2fe33241514e71379b4))

## [1.3.1](https://www.github.com/googleapis/python-billing/compare/v1.3.0...v1.3.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#96](https://www.github.com/googleapis/python-billing/issues/96)) ([a9e5368](https://www.github.com/googleapis/python-billing/commit/a9e536849aea8fe4ba513cd5503c275c4a7db880))

## [1.3.0](https://www.github.com/googleapis/python-billing/compare/v1.2.1...v1.3.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#86](https://www.github.com/googleapis/python-billing/issues/86)) ([7ff02d6](https://www.github.com/googleapis/python-billing/commit/7ff02d68336e9a5d51dba0e03e6e9332d6080cf9))


### Bug Fixes

* disable always_use_jwt_access ([cff1d3e](https://www.github.com/googleapis/python-billing/commit/cff1d3e7d191321914003bc1d677954bfea49304))
* disable always_use_jwt_access ([#93](https://www.github.com/googleapis/python-billing/issues/93)) ([cff1d3e](https://www.github.com/googleapis/python-billing/commit/cff1d3e7d191321914003bc1d677954bfea49304))


### Documentation

* include client library documentation in README.rst ([#91](https://www.github.com/googleapis/python-billing/issues/91)) ([3a6999d](https://www.github.com/googleapis/python-billing/commit/3a6999d6196f8d5ea1a92f4304c60fd3c2cc549c))
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-billing/issues/1127)) ([#82](https://www.github.com/googleapis/python-billing/issues/82)) ([634d7b0](https://www.github.com/googleapis/python-billing/commit/634d7b01fba7d834b0acfd3a2ee1357260f0b695))

## [1.2.1](https://www.github.com/googleapis/python-billing/compare/v1.2.0...v1.2.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#79](https://www.github.com/googleapis/python-billing/issues/79)) ([f2fc441](https://www.github.com/googleapis/python-billing/commit/f2fc4412c677c5648cbe12a86f01699118279a56))

## [1.2.0](https://www.github.com/googleapis/python-billing/compare/v1.1.1...v1.2.0) (2021-05-28)


### Features

* add from_service_account_info factory and fix sphinx identifiers ([#42](https://www.github.com/googleapis/python-billing/issues/42)) ([95ba269](https://www.github.com/googleapis/python-billing/commit/95ba26961090dc76e75064cba10c21ca4897675e))
* support self-signed JWT flow for service accounts ([a2a6aaf](https://www.github.com/googleapis/python-billing/commit/a2a6aaf71864cd1a9e093fd77f6426e2a39ebe25))


### Bug Fixes

* add async client to %name_%version/init.py ([a2a6aaf](https://www.github.com/googleapis/python-billing/commit/a2a6aaf71864cd1a9e093fd77f6426e2a39ebe25))
* **deps:** add packaging requirement ([#75](https://www.github.com/googleapis/python-billing/issues/75)) ([73d8957](https://www.github.com/googleapis/python-billing/commit/73d895725d396d7f930c8259dfbec269897a5b62))

## [1.1.1](https://www.github.com/googleapis/python-billing/compare/v1.1.0...v1.1.1) (2021-02-11)


### Bug Fixes

* update retry and timeout settings ([#38](https://www.github.com/googleapis/python-billing/issues/38)) ([8dbad86](https://www.github.com/googleapis/python-billing/commit/8dbad869521924fc3f7d7dc2d4f5d7e9100874b3))

## [1.1.0](https://www.github.com/googleapis/python-billing/compare/v1.0.0...v1.1.0) (2020-11-17)


### Features

* add async client, support credentials_file and scopes client options ([#29](https://www.github.com/googleapis/python-billing/issues/29)) ([4177eb5](https://www.github.com/googleapis/python-billing/commit/4177eb53544392931a17a6fc8e51b24c69698969))
* add mtls support ([#19](https://www.github.com/googleapis/python-billing/issues/19)) ([fef622a](https://www.github.com/googleapis/python-billing/commit/fef622a0dddf005d8af329ee001ec41f03850427))

## [1.0.0](https://www.github.com/googleapis/python-billing/compare/v0.1.0...v1.0.0) (2020-05-18)


### Features

* release as production/stable ([#15](https://www.github.com/googleapis/python-billing/issues/15)) ([80a4fed](https://www.github.com/googleapis/python-billing/commit/80a4fed5aea4349b4f6d4e2b4a387c6cb8136295))


### Bug Fixes

* correct link to docs ([#5](https://www.github.com/googleapis/python-billing/issues/5)) ([3d87965](https://www.github.com/googleapis/python-billing/commit/3d879653ad5e1b45aadb856796c6db68145c51f4))

## 0.1.0 (2020-02-28)


### Features

* generate v1 ([61db762](https://www.github.com/googleapis/python-billing/commit/61db76297352fc61f65130dfbf50e3dfa7620fd8))
