# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-os-config/#history

## [1.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.25.0...google-cloud-os-config-v1.26.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.24.0...google-cloud-os-config-v1.25.0) (2026-06-22)


### Features

* regenerate google-cloud-[o-r] packages ([#17075](https://github.com/googleapis/google-cloud-python/issues/17075)) ([f4bd018](https://github.com/googleapis/google-cloud-python/commit/f4bd0182d808ae73c3c6981e6ce3d565f78a6051))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.23.0...google-cloud-os-config-v1.24.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.22.0...google-cloud-os-config-v1.23.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.21.0...google-cloud-os-config-v1.22.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.20.2...google-cloud-os-config-v1.21.0) (2025-08-10)


### Features

* Add highest_upgradable_cve_severity field to Vulnerability report ([e8feca7](https://github.com/googleapis/google-cloud-python/commit/e8feca76cfe1a2eaf7e96ff2341715545d15b5a8))


### Documentation

* A comment for field `filter` in message `.google.cloud.osconfig.v1.ListVulnerabilityReportsRequest` is changed ([e8feca7](https://github.com/googleapis/google-cloud-python/commit/e8feca76cfe1a2eaf7e96ff2341715545d15b5a8))
* A comment for field `update_time` in message `.google.cloud.osconfig.v1.VulnerabilityReport` is changed ([e8feca7](https://github.com/googleapis/google-cloud-python/commit/e8feca76cfe1a2eaf7e96ff2341715545d15b5a8))

## [1.20.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.20.1...google-cloud-os-config-v1.20.2) (2025-06-11)


### Documentation

* Update import statement example in README ([dfc2cd6](https://github.com/googleapis/google-cloud-python/commit/dfc2cd6be6422baa45dcebc5ff6e7fc846bf5c7d))

## [1.20.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.20.0...google-cloud-os-config-v1.20.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([7295cbb](https://github.com/googleapis/google-cloud-python/commit/7295cbb7c3122eeff1042c3c543bfc9b8b3ca913))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.19.0...google-cloud-os-config-v1.20.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([a0910dd](https://github.com/googleapis/google-cloud-python/commit/a0910dd51541d238bc5fcf10159066ddfd928579))
* Add support for reading selective GAPIC generation methods from service YAML ([a0910dd](https://github.com/googleapis/google-cloud-python/commit/a0910dd51541d238bc5fcf10159066ddfd928579))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.18.1...google-cloud-os-config-v1.19.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([8e6b0cc](https://github.com/googleapis/google-cloud-python/commit/8e6b0cca8709ae8c7f0c722c5ebf0707358d3359))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([8e6b0cc](https://github.com/googleapis/google-cloud-python/commit/8e6b0cca8709ae8c7f0c722c5ebf0707358d3359))

## [1.18.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.18.0...google-cloud-os-config-v1.18.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13244](https://github.com/googleapis/google-cloud-python/issues/13244)) ([ae1f471](https://github.com/googleapis/google-cloud-python/commit/ae1f47175bf3354f78cb558a844a9cab00317b95))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.17.5...google-cloud-os-config-v1.18.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13208](https://github.com/googleapis/google-cloud-python/issues/13208)) ([a019409](https://github.com/googleapis/google-cloud-python/commit/a019409a5b5a983402301f1ac175d8b7e45c3818))

## [1.17.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.17.4...google-cloud-os-config-v1.17.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([d95af77](https://github.com/googleapis/google-cloud-python/commit/d95af77248f0935a5fe3dba1fccc75124c8b1451))

## [1.17.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.17.3...google-cloud-os-config-v1.17.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12868](https://github.com/googleapis/google-cloud-python/issues/12868)) ([0e39c1a](https://github.com/googleapis/google-cloud-python/commit/0e39c1a0ab46757bcf80a178d9bd422f6dcb24c6))

## [1.17.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.17.2...google-cloud-os-config-v1.17.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12386](https://github.com/googleapis/google-cloud-python/issues/12386)) ([edcad16](https://github.com/googleapis/google-cloud-python/commit/edcad1661973ae1677c69b3fc1c03c3069ec0e71))

## [1.17.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.17.1...google-cloud-os-config-v1.17.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12308](https://github.com/googleapis/google-cloud-python/issues/12308)) ([74dabeb](https://github.com/googleapis/google-cloud-python/commit/74dabebab206189e649ff6e00f3c7809d96c043b))
* fix ValueError in test__validate_universe_domain ([7c2f2c2](https://github.com/googleapis/google-cloud-python/commit/7c2f2c29d74c9584efc42ddfe8bc098a594391a2))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.17.0...google-cloud-os-config-v1.17.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.16.0...google-cloud-os-config-v1.17.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([4368029](https://github.com/googleapis/google-cloud-python/commit/436802904bfdafa7e90f94b128813506525e1605))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.15.3...google-cloud-os-config-v1.16.0) (2023-12-07)


### Features

* Add support for python 3.12 ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))
* Introduce compatibility with native namespace packages ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))
* Use `retry_async` instead of `retry` in async client ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))

## [1.15.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-os-config-v1.15.2...google-cloud-os-config-v1.15.3) (2023-09-30)


### Documentation

* Minor formatting ([#295](https://github.com/googleapis/google-cloud-python/issues/295)) ([8805a43](https://github.com/googleapis/google-cloud-python/commit/8805a436e218ea0c7a7ec9de1b7a1e57635604e4))

## [1.15.2](https://github.com/googleapis/python-os-config/compare/v1.15.1...v1.15.2) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#280](https://github.com/googleapis/python-os-config/issues/280)) ([ba03471](https://github.com/googleapis/python-os-config/commit/ba0347119e6e14ea6a30793a1499ceaf60e46b56))

## [1.15.1](https://github.com/googleapis/python-os-config/compare/v1.15.0...v1.15.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#272](https://github.com/googleapis/python-os-config/issues/272)) ([4fdfa8b](https://github.com/googleapis/python-os-config/commit/4fdfa8bb23c85bfb6785aa6e9450fdb042a3fb83))

## [1.15.0](https://github.com/googleapis/python-os-config/compare/v1.14.1...v1.15.0) (2023-02-21)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#266](https://github.com/googleapis/python-os-config/issues/266)) ([679246f](https://github.com/googleapis/python-os-config/commit/679246ff80d7768e23fbdc7375515ecd6c1684b3))

## [1.14.1](https://github.com/googleapis/python-os-config/compare/v1.14.0...v1.14.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([97b46fa](https://github.com/googleapis/python-os-config/commit/97b46fa4d0bb76692202b9645d6489cc5e97b6b8))


### Documentation

* Add documentation for enums ([97b46fa](https://github.com/googleapis/python-os-config/commit/97b46fa4d0bb76692202b9645d6489cc5e97b6b8))

## [1.14.0](https://github.com/googleapis/python-os-config/compare/v1.13.0...v1.14.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#257](https://github.com/googleapis/python-os-config/issues/257)) ([fa3a63f](https://github.com/googleapis/python-os-config/commit/fa3a63f72b1c1c6603655aae1c1457638f53b489))

## [1.13.0](https://github.com/googleapis/python-os-config/compare/v1.12.4...v1.13.0) (2022-12-13)


### Features

* Add support for `google.cloud.osconfig.__version__` ([0980ecc](https://github.com/googleapis/python-os-config/commit/0980eccc0b4d528719b13849f2ff9bb2707e4a21))
* Add typing to proto.Message based class attributes ([0980ecc](https://github.com/googleapis/python-os-config/commit/0980eccc0b4d528719b13849f2ff9bb2707e4a21))


### Bug Fixes

* Add dict typing for client_options ([0980ecc](https://github.com/googleapis/python-os-config/commit/0980eccc0b4d528719b13849f2ff9bb2707e4a21))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([326bd8c](https://github.com/googleapis/python-os-config/commit/326bd8cc374f342187beb50f95308408fe839986))
* Drop usage of pkg_resources ([326bd8c](https://github.com/googleapis/python-os-config/commit/326bd8cc374f342187beb50f95308408fe839986))
* Fix timeout default values ([326bd8c](https://github.com/googleapis/python-os-config/commit/326bd8cc374f342187beb50f95308408fe839986))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([0980ecc](https://github.com/googleapis/python-os-config/commit/0980eccc0b4d528719b13849f2ff9bb2707e4a21))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([326bd8c](https://github.com/googleapis/python-os-config/commit/326bd8cc374f342187beb50f95308408fe839986))

## [1.12.4](https://github.com/googleapis/python-os-config/compare/v1.12.3...v1.12.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#245](https://github.com/googleapis/python-os-config/issues/245)) ([adeb2d1](https://github.com/googleapis/python-os-config/commit/adeb2d1bc30f88c032a1079f9469046e6ca5b5f1))

## [1.12.3](https://github.com/googleapis/python-os-config/compare/v1.12.2...v1.12.3) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#243](https://github.com/googleapis/python-os-config/issues/243)) ([73c75aa](https://github.com/googleapis/python-os-config/commit/73c75aa2a64e2accb6093dd8b5011370fb02bfe4))

## [1.12.2](https://github.com/googleapis/python-os-config/compare/v1.12.1...v1.12.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#227](https://github.com/googleapis/python-os-config/issues/227)) ([c3a2047](https://github.com/googleapis/python-os-config/commit/c3a2047ac58a718e6bc34b6f6f43f48e42b65f92))
* **deps:** require proto-plus >= 1.22.0 ([c3a2047](https://github.com/googleapis/python-os-config/commit/c3a2047ac58a718e6bc34b6f6f43f48e42b65f92))

## [1.12.1](https://github.com/googleapis/python-os-config/compare/v1.12.0...v1.12.1) (2022-07-13)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#218](https://github.com/googleapis/python-os-config/issues/218)) ([50330f2](https://github.com/googleapis/python-os-config/commit/50330f24ebe9bcc6851725ad6669331a9349020b))

## [1.12.0](https://github.com/googleapis/python-os-config/compare/v1.11.2...v1.12.0) (2022-07-07)


### Features

* add audience parameter ([d700d11](https://github.com/googleapis/python-os-config/commit/d700d1171f2ceab7aaf362eeff385c9733cf456c))


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#213](https://github.com/googleapis/python-os-config/issues/213)) ([d700d11](https://github.com/googleapis/python-os-config/commit/d700d1171f2ceab7aaf362eeff385c9733cf456c))
* require python 3.7+ ([#215](https://github.com/googleapis/python-os-config/issues/215)) ([397e04d](https://github.com/googleapis/python-os-config/commit/397e04d1b76dc8d5145109140ac41be84609adac))

## [1.11.2](https://github.com/googleapis/python-os-config/compare/v1.11.1...v1.11.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#205](https://github.com/googleapis/python-os-config/issues/205)) ([14b8400](https://github.com/googleapis/python-os-config/commit/14b8400e2f23158f402f18b4af7c5e1fac0b35c5))


### Documentation

* fix changelog header to consistent size ([#206](https://github.com/googleapis/python-os-config/issues/206)) ([17b8505](https://github.com/googleapis/python-os-config/commit/17b850599b0da9625dc1dcd26064f17f30448448))

## [1.11.1](https://github.com/googleapis/python-os-config/compare/v1.11.0...v1.11.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#174](https://github.com/googleapis/python-os-config/issues/174)) ([a47fc64](https://github.com/googleapis/python-os-config/commit/a47fc64945a6f21bbd42bcd4bf3191c245e04b61))

## [1.11.0](https://github.com/googleapis/python-os-config/compare/v1.10.0...v1.11.0) (2022-02-26)


### Features

* Add existing os_policy_assignment_reports.proto ([eb6bbb7](https://github.com/googleapis/python-os-config/commit/eb6bbb7a5e99dc22377d49a4c739c2a22f8e0558))
* Add GetOsPolicyAssignmentReport and analogous List rpc method ([eb6bbb7](https://github.com/googleapis/python-os-config/commit/eb6bbb7a5e99dc22377d49a4c739c2a22f8e0558))
* Add Inventory to InstanceFilter ([eb6bbb7](https://github.com/googleapis/python-os-config/commit/eb6bbb7a5e99dc22377d49a4c739c2a22f8e0558))
* Add item that is affected by vulnerability ([eb6bbb7](https://github.com/googleapis/python-os-config/commit/eb6bbb7a5e99dc22377d49a4c739c2a22f8e0558))


### Bug Fixes

* Mark methods as deprecated ([eb6bbb7](https://github.com/googleapis/python-os-config/commit/eb6bbb7a5e99dc22377d49a4c739c2a22f8e0558))


### Documentation

* add generated snippets ([eb6bbb7](https://github.com/googleapis/python-os-config/commit/eb6bbb7a5e99dc22377d49a4c739c2a22f8e0558))

## [1.10.0](https://github.com/googleapis/python-os-config/compare/v1.9.0...v1.10.0) (2022-02-08)


### Features

* add ability to change the state of a patch deployment ([#163](https://github.com/googleapis/python-os-config/issues/163)) ([fbf55b5](https://github.com/googleapis/python-os-config/commit/fbf55b5abbe63d946d9fea4a335a9edd5495ad86))
* add api key support ([#158](https://github.com/googleapis/python-os-config/issues/158)) ([4de2275](https://github.com/googleapis/python-os-config/commit/4de22754f2d45bfce7c20b97f0a6a6a2f30b7a97))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([e7f8549](https://github.com/googleapis/python-os-config/commit/e7f854968db11231c3f5a8d4469e66a9cfc196e3))


### Documentation

* add autogenerated code snippets ([fbf55b5](https://github.com/googleapis/python-os-config/commit/fbf55b5abbe63d946d9fea4a335a9edd5495ad86))

## [1.9.0](https://www.github.com/googleapis/python-os-config/compare/v1.8.0...v1.9.0) (2021-11-11)


### Features

* **v1:** Add OS inventory item ([#147](https://www.github.com/googleapis/python-os-config/issues/147)) ([14102d9](https://www.github.com/googleapis/python-os-config/commit/14102d97b78f5d9c10aca07452f11112d53a1788))

## [1.8.0](https://www.github.com/googleapis/python-os-config/compare/v1.7.1...v1.8.0) (2021-11-04)


### Features

* add OS policy assignment rpcs ([#142](https://www.github.com/googleapis/python-os-config/issues/142)) ([44c158d](https://www.github.com/googleapis/python-os-config/commit/44c158dd19c4329678e170733377494821ca955f))

## [1.7.1](https://www.github.com/googleapis/python-os-config/compare/v1.7.0...v1.7.1) (2021-11-02)


### Bug Fixes

* **deps:** drop packaging dependency ([df69ccc](https://www.github.com/googleapis/python-os-config/commit/df69ccc66f45ccb4e94fbe8251c3f58e744fcf6b))
* **deps:** require google-api-core >= 1.28.0 ([df69ccc](https://www.github.com/googleapis/python-os-config/commit/df69ccc66f45ccb4e94fbe8251c3f58e744fcf6b))


### Documentation

* list oneofs in docstring ([df69ccc](https://www.github.com/googleapis/python-os-config/commit/df69ccc66f45ccb4e94fbe8251c3f58e744fcf6b))

## [1.7.0](https://www.github.com/googleapis/python-os-config/compare/v1.6.0...v1.7.0) (2021-10-18)


### Features

* add support for python 3.10 ([#133](https://www.github.com/googleapis/python-os-config/issues/133)) ([44e23f4](https://www.github.com/googleapis/python-os-config/commit/44e23f4b82fad2079b79366670b8a14002a37d68))
* Update RecurringSchedule.Frequency with DAILY frequency ([#137](https://www.github.com/googleapis/python-os-config/issues/137)) ([75b232e](https://www.github.com/googleapis/python-os-config/commit/75b232e9ca86beeb6a9d2a9f45629e2ffa458c6d))

## [1.6.0](https://www.github.com/googleapis/python-os-config/compare/v1.5.2...v1.6.0) (2021-10-08)


### Features

* add context manager support in client ([#129](https://www.github.com/googleapis/python-os-config/issues/129)) ([b207115](https://www.github.com/googleapis/python-os-config/commit/b207115ed97544585c5f0dc7512d71fd94b5aae2))

## [1.5.2](https://www.github.com/googleapis/python-os-config/compare/v1.5.1...v1.5.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([e6d6242](https://www.github.com/googleapis/python-os-config/commit/e6d62422e555f33cd5107eb59073c8d88d292681))

## [1.5.1](https://www.github.com/googleapis/python-os-config/compare/v1.5.0...v1.5.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([911871e](https://www.github.com/googleapis/python-os-config/commit/911871e8154fdb16a6e182764563864cf2235153))

## [1.5.0](https://www.github.com/googleapis/python-os-config/compare/v1.4.0...v1.5.0) (2021-09-07)


### Features

* add OSConfigZonalService API ([#116](https://www.github.com/googleapis/python-os-config/issues/116)) ([72bb90f](https://www.github.com/googleapis/python-os-config/commit/72bb90f67be410d981854f9a5f34fd31b1934693))

## [1.4.0](https://www.github.com/googleapis/python-os-config/compare/v1.3.2...v1.4.0) (2021-08-30)


### Features

* Update osconfig v1 and v1alpha with WindowsApplication ([#108](https://www.github.com/googleapis/python-os-config/issues/108)) ([befbfdc](https://www.github.com/googleapis/python-os-config/commit/befbfdcd6bffdc402330bd0b715593ac788bd3b0))

## [1.3.2](https://www.github.com/googleapis/python-os-config/compare/v1.3.1...v1.3.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#101](https://www.github.com/googleapis/python-os-config/issues/101)) ([5f6c367](https://www.github.com/googleapis/python-os-config/commit/5f6c367753fb780f15ff38245b2c85387e01965e))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#97](https://www.github.com/googleapis/python-os-config/issues/97)) ([404adc3](https://www.github.com/googleapis/python-os-config/commit/404adc3419aaa40b0b66f55fc3ed92758287816b))


### Miscellaneous Chores

* release as 1.3.2 ([#102](https://www.github.com/googleapis/python-os-config/issues/102)) ([7c642b0](https://www.github.com/googleapis/python-os-config/commit/7c642b0eb32171275ee47db7ab64900176d0a4a1))

## [1.3.1](https://www.github.com/googleapis/python-os-config/compare/v1.3.0...v1.3.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#96](https://www.github.com/googleapis/python-os-config/issues/96)) ([022e149](https://www.github.com/googleapis/python-os-config/commit/022e149322e719465f1b0b66850def2b94c42eb1))

## [1.3.0](https://www.github.com/googleapis/python-os-config/compare/v1.2.0...v1.3.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#88](https://www.github.com/googleapis/python-os-config/issues/88)) ([abb4837](https://www.github.com/googleapis/python-os-config/commit/abb48378d71deab058958c3b3b1efff5c253c99e))


### Bug Fixes

* disable always_use_jwt_access ([#92](https://www.github.com/googleapis/python-os-config/issues/92)) ([5d8a4bb](https://www.github.com/googleapis/python-os-config/commit/5d8a4bb9ef477f8fd81344fbd02631ac31660169))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-os-config/issues/1127)) ([#83](https://www.github.com/googleapis/python-os-config/issues/83)) ([b9fc494](https://www.github.com/googleapis/python-os-config/commit/b9fc4948a320fcf6a7154a2c7a1476cc78736c4d))

## [1.2.0](https://www.github.com/googleapis/python-os-config/compare/v1.1.0...v1.2.0) (2021-06-09)


### Features

* release as GA ([#46](https://www.github.com/googleapis/python-os-config/issues/46)) ([d5aece9](https://www.github.com/googleapis/python-os-config/commit/d5aece996ff225dc747e7c59978576bfcb79a3d1))
* support self-signed JWT flow for service accounts ([6fbaf4b](https://www.github.com/googleapis/python-os-config/commit/6fbaf4bb16b0bb381edf13957b85297c1659a206))
* add v1alpha ([#80](https://www.github.com/googleapis/python-os-config/issues/80)) ([493ac75](https://www.github.com/googleapis/python-os-config/commit/493ac75a5fec0185fa15415fe4feffe0c36ca7e9))


### Bug Fixes

* add async client to %name_%version/init.py ([6fbaf4b](https://www.github.com/googleapis/python-os-config/commit/6fbaf4bb16b0bb381edf13957b85297c1659a206))
* **deps:** add packaging requirement ([#72](https://www.github.com/googleapis/python-os-config/issues/72)) ([44e0947](https://www.github.com/googleapis/python-os-config/commit/44e09479922f8569b8d95657009e7c806eb101f9))


### Documentation

* fix sphinx identifiers ([#52](https://www.github.com/googleapis/python-os-config/issues/52)) ([940916d](https://www.github.com/googleapis/python-os-config/commit/940916de78ac19bea3f63f75ce073648f920c70b))

## [1.1.0](https://www.github.com/googleapis/python-os-config/compare/v1.0.0...v1.1.0) (2021-02-12)


### Features

* add `from_service_account_info` ([#31](https://www.github.com/googleapis/python-os-config/issues/31)) ([d8d921f](https://www.github.com/googleapis/python-os-config/commit/d8d921fc28d294039c574e4dc327fbe1caa27337))


### Bug Fixes

* remove client side receive limits  ([#29](https://www.github.com/googleapis/python-os-config/issues/29)) ([628ada4](https://www.github.com/googleapis/python-os-config/commit/628ada4004b1add04f5c2d95b9b1cad48616cf2c))

## [1.0.0](https://www.github.com/googleapis/python-os-config/compare/v0.1.2...v1.0.0) (2020-11-18)


### ⚠ BREAKING CHANGES

* rename attributes that conflict with builtins (#24)
    * `Instance.type` ->`Instance.type_`
    * `GcsObject.object` -> `GcsObject.object_`
    * `PatchInstanceFilter.all` -> `PatchInstanceFilter.all_`

### Features

* add async client ([#8](https://www.github.com/googleapis/python-os-config/issues/8)) ([33f46ba](https://www.github.com/googleapis/python-os-config/commit/33f46ba4aa34e066a70a5ad792254574b5985f83))
* add patch rollout to patch deployments ([#24](https://www.github.com/googleapis/python-os-config/issues/24)) ([4d8605e](https://www.github.com/googleapis/python-os-config/commit/4d8605e2d92af271b2c363490926689266c1d4b6))
* add common resource path helpers ([#24](https://www.github.com/googleapis/python-os-config/issues/24)) ([4d8605e](https://www.github.com/googleapis/python-os-config/commit/4d8605e2d92af271b2c363490926689266c1d4b6))
* make client transport public ([#24](https://www.github.com/googleapis/python-os-config/issues/24)) ([4d8605e](https://www.github.com/googleapis/python-os-config/commit/4d8605e2d92af271b2c363490926689266c1d4b6))
---
## [0.1.2](https://www.github.com/googleapis/python-os-config/compare/v0.1.1...v0.1.2) (2020-06-11)


### Bug Fixes

* remove duplicate version ([#6](https://www.github.com/googleapis/python-os-config/issues/6)) ([351b553](https://www.github.com/googleapis/python-os-config/commit/351b5531244bb207fc6696625dbeaf840e7a469f))

## [0.1.1](https://www.github.com/googleapis/python-os-config/compare/v0.1.0...v0.1.1) (2020-06-11)


### Bug Fixes

* fix documentation links ([#2](https://www.github.com/googleapis/python-os-config/issues/2)) ([9d71787](https://www.github.com/googleapis/python-os-config/commit/9d717874d310d40efdb8f2a316521ea90e8c0e63))

## 0.1.0 (2020-06-10)


### Features

* generate v1 ([5d1f582](https://www.github.com/googleapis/python-os-config/commit/5d1f582b5b02d128ef44120d285941805d234ec7))
