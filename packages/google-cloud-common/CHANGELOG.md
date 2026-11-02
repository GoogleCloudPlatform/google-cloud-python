# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-common/#history

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.10.0...google-cloud-common-v1.11.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.9.0...google-cloud-common-v1.10.0) (2026-06-02)


### Features

* regenerate google-cloud-c packages (#17091) ([165839343695fc74d09fc7900d4c55ddcb31a4d8](https://github.com/googleapis/google-cloud-python/commit/165839343695fc74d09fc7900d4c55ddcb31a4d8))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.8.0...google-cloud-common-v1.9.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.7.0...google-cloud-common-v1.8.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.6.0...google-cloud-common-v1.7.0) (2025-10-28)


### Bug Fixes

* upgrade gRPC service registration func An update to Go gRPC Protobuf generation will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go service files. This change should affect very few client library users. See release notes advisories in https://github.com/googleapis/google-cloud-go/pull/11025.  ([c3c2fbbacf03dcaf015bbfb949f95d46d9e669cb](https://github.com/googleapis/google-cloud-python/commit/c3c2fbbacf03dcaf015bbfb949f95d46d9e669cb))

## [1.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.5.2...google-cloud-common-v1.6.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.5.1...google-cloud-common-v1.5.2) (2025-06-11)


### Documentation

* Update import statement example in README ([8697120](https://github.com/googleapis/google-cloud-python/commit/869712032803cb31d93f3b16abc2abdb14f733a4))

## [1.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.5.0...google-cloud-common-v1.5.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([1e43e75](https://github.com/googleapis/google-cloud-python/commit/1e43e75e99445373785b11381e0e859fa14bb485))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.4.0...google-cloud-common-v1.5.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))
* Add support for reading selective GAPIC generation methods from service YAML ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))

## [1.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.3.5...google-cloud-common-v1.4.0) (2024-10-24)


### Features

* Add support for  Python 3.13 ([6252476](https://github.com/googleapis/google-cloud-python/commit/6252476e5938352fb2417d098a1edcc08558fe10))

## [1.3.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.3.4...google-cloud-common-v1.3.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([a6f7356](https://github.com/googleapis/google-cloud-python/commit/a6f7356f1549721f9fab83d4dcfa226cec1965d0))

## [1.3.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.3.3...google-cloud-common-v1.3.4) (2024-07-08)


### Bug Fixes

* Allow protobuf 5.x ([04ec204](https://github.com/googleapis/google-cloud-python/commit/04ec2046ed11c690273912e1bb6220823c7dd7c0))

## [1.3.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.3.2...google-cloud-common-v1.3.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12383](https://github.com/googleapis/google-cloud-python/issues/12383)) ([305f43f](https://github.com/googleapis/google-cloud-python/commit/305f43f7d6293e3316248f421fdc19c5d8405c21))

## [1.3.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.3.1...google-cloud-common-v1.3.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12305](https://github.com/googleapis/google-cloud-python/issues/12305)) ([2aa7f17](https://github.com/googleapis/google-cloud-python/commit/2aa7f17a5fd4f2249260225db91fb0414d06eaa7))

## [1.3.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.3.0...google-cloud-common-v1.3.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))

## [1.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-common-v1.2.0...google-cloud-common-v1.3.0) (2023-12-07)


### Features

* Add support for python 3.12 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Introduce compatibility with native namespace packages ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Use `retry_async` instead of `retry` in async client ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))

## [1.2.0](https://github.com/googleapis/python-cloud-common/compare/v1.1.0...v1.2.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#100](https://github.com/googleapis/python-cloud-common/issues/100)) ([6ddb9f8](https://github.com/googleapis/python-cloud-common/commit/6ddb9f89dbebda57e491a0dcefdff22c0497cca3))

## [1.1.0](https://github.com/googleapis/python-cloud-common/compare/v1.0.6...v1.1.0) (2022-12-15)


### Features

* Add support for `google.cloud.common.__version__` ([0d9d45f](https://github.com/googleapis/python-cloud-common/commit/0d9d45f96fa52e70d16ef9488b3548e5e7f8bb05))


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([#97](https://github.com/googleapis/python-cloud-common/issues/97)) ([6464998](https://github.com/googleapis/python-cloud-common/commit/6464998254db8e37b866211700e168b6cd382766))

## [1.0.6](https://github.com/googleapis/python-cloud-common/compare/v1.0.5...v1.0.6) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#89](https://github.com/googleapis/python-cloud-common/issues/89)) ([4bb2dfb](https://github.com/googleapis/python-cloud-common/commit/4bb2dfbc93efaf63a771b996d1fb2dd648571089))

## [1.0.5](https://github.com/googleapis/python-cloud-common/compare/v1.0.4...v1.0.5) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#87](https://github.com/googleapis/python-cloud-common/issues/87)) ([4430802](https://github.com/googleapis/python-cloud-common/commit/44308020a0db1c0cc4853c827426de7ee4c2ee4f))

## [1.0.4](https://github.com/googleapis/python-cloud-common/compare/v1.0.3...v1.0.4) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#73](https://github.com/googleapis/python-cloud-common/issues/73)) ([eb28a57](https://github.com/googleapis/python-cloud-common/commit/eb28a5768eaeae2aeeb8c295f146065981a1ebf4))
* **deps:** require proto-plus >= 1.22.0 ([eb28a57](https://github.com/googleapis/python-cloud-common/commit/eb28a5768eaeae2aeeb8c295f146065981a1ebf4))

## [1.0.3](https://github.com/googleapis/python-cloud-common/compare/v1.0.2...v1.0.3) (2022-07-16)


### Bug Fixes

* require python 3.7+ ([#67](https://github.com/googleapis/python-cloud-common/issues/67)) ([8f65b92](https://github.com/googleapis/python-cloud-common/commit/8f65b92e81f7c3e3341a6ccdadbb10cdeecdd872))

## [1.0.2](https://github.com/googleapis/python-cloud-common/compare/v1.0.1...v1.0.2) (2022-06-03)


### Bug Fixes

* **deps:** drop dependency packaging ([170234d](https://github.com/googleapis/python-cloud-common/commit/170234db68e087ecbcd5ff22176635e397c11f9a))
* **deps:** require protobuf <4.0.0dev ([#58](https://github.com/googleapis/python-cloud-common/issues/58)) ([170234d](https://github.com/googleapis/python-cloud-common/commit/170234db68e087ecbcd5ff22176635e397c11f9a))

## [1.0.1](https://github.com/googleapis/python-cloud-common/compare/v1.0.0...v1.0.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#38](https://github.com/googleapis/python-cloud-common/issues/38)) ([756847f](https://github.com/googleapis/python-cloud-common/commit/756847fc408db91a42738f2253a96f9132f886e8))

## [1.0.0](https://www.github.com/googleapis/python-cloud-common/compare/v0.2.0...v1.0.0) (2021-11-03)


### Features

* bump release level to production/stable ([#4](https://www.github.com/googleapis/python-cloud-common/issues/4)) ([a83cb9d](https://www.github.com/googleapis/python-cloud-common/commit/a83cb9df15dbe381a7180abe26eea30e8ec3a281))

## [0.2.0](https://www.github.com/googleapis/python-cloud-common/compare/v0.1.0...v0.2.0) (2021-10-08)


### Features

* add context manager support in client ([#8](https://www.github.com/googleapis/python-cloud-common/issues/8)) ([6bed942](https://www.github.com/googleapis/python-cloud-common/commit/6bed942cce256f2ae0624c09563b8833263cc46d))

## 0.1.0 (2021-10-01)


### Features

* generate google.cloud.common ([61b5082](https://www.github.com/googleapis/python-cloud-common/commit/61b5082fcb5a48cc1006e01102f35ec9730e0f14))
