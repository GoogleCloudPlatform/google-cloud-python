# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-service-usage/#history

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.17.0...google-cloud-service-usage-v1.18.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.16.0...google-cloud-service-usage-v1.17.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.15.0...google-cloud-service-usage-v1.16.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.14.0...google-cloud-service-usage-v1.15.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.13.1...google-cloud-service-usage-v1.14.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.13.0...google-cloud-service-usage-v1.13.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.12.0...google-cloud-service-usage-v1.13.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))
* Add support for reading selective GAPIC generation methods from service YAML ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.11.1...google-cloud-service-usage-v1.12.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.11.0...google-cloud-service-usage-v1.11.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([59c4287](https://github.com/googleapis/google-cloud-python/commit/59c42878386ee08d1717b73e47d33d76cfb38ba0))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.10.5...google-cloud-service-usage-v1.11.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13202](https://github.com/googleapis/google-cloud-python/issues/13202)) ([5b1f2f3](https://github.com/googleapis/google-cloud-python/commit/5b1f2f3a81ed171b643812e67a7ed179b9b703ea))

## [1.10.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.10.4...google-cloud-service-usage-v1.10.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([42c4d04](https://github.com/googleapis/google-cloud-python/commit/42c4d04ee1362ba0ed0f1b6a134ac8e409875b63))

## [1.10.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.10.3...google-cloud-service-usage-v1.10.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [1.10.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.10.2...google-cloud-service-usage-v1.10.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [1.10.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.10.1...google-cloud-service-usage-v1.10.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12283](https://github.com/googleapis/google-cloud-python/issues/12283)) ([f20b41a](https://github.com/googleapis/google-cloud-python/commit/f20b41ac35b02a40135b83edfe819ff7a355ab21))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))

## [1.10.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.10.0...google-cloud-service-usage-v1.10.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.9.0...google-cloud-service-usage-v1.10.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.8.0...google-cloud-service-usage-v1.9.0) (2023-12-07)


### Features

* Add support for python 3.12 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Introduce compatibility with native namespace packages ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Use `retry_async` instead of `retry` in async client ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.7.2...google-cloud-service-usage-v1.8.0) (2023-09-19)


### Features

* added ConsumerQuotaLimit.supported_locations ([be7f5e4](https://github.com/googleapis/google-cloud-python/commit/be7f5e4d31c7dd3b3d32bce66310400d729f58ae))
* added ProducerQuotaPolicy message and QuotaBucket.producer_quota_policy field ([be7f5e4](https://github.com/googleapis/google-cloud-python/commit/be7f5e4d31c7dd3b3d32bce66310400d729f58ae))
* introduce resource class serviceusage.googleapis.com/Service ([be7f5e4](https://github.com/googleapis/google-cloud-python/commit/be7f5e4d31c7dd3b3d32bce66310400d729f58ae))


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.7.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-usage-v1.7.1...google-cloud-service-usage-v1.7.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [1.7.1](https://github.com/googleapis/python-service-usage/compare/v1.7.0...v1.7.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#170](https://github.com/googleapis/python-service-usage/issues/170)) ([f730be6](https://github.com/googleapis/python-service-usage/commit/f730be62e82de2374216e72d8a54fc8110e0a868))

## [1.7.0](https://github.com/googleapis/python-service-usage/compare/v1.6.1...v1.7.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#166](https://github.com/googleapis/python-service-usage/issues/166)) ([3dcb482](https://github.com/googleapis/python-service-usage/commit/3dcb482eef0796cfb3ab874e6c7637fa631da01a))

## [1.6.1](https://github.com/googleapis/python-service-usage/compare/v1.6.0...v1.6.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([d7c14ed](https://github.com/googleapis/python-service-usage/commit/d7c14ed360824d12122c00f527453ae564e047de))


### Documentation

* Add documentation for enums ([d7c14ed](https://github.com/googleapis/python-service-usage/commit/d7c14ed360824d12122c00f527453ae564e047de))

## [1.6.0](https://github.com/googleapis/python-service-usage/compare/v1.5.0...v1.6.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#158](https://github.com/googleapis/python-service-usage/issues/158)) ([c61468e](https://github.com/googleapis/python-service-usage/commit/c61468e5b873682af7be4bf5fd91c59da01ea74b))

## [1.5.0](https://github.com/googleapis/python-service-usage/compare/v1.4.3...v1.5.0) (2022-12-14)


### Features

* Add support for `google.cloud.service_usage.__version__` ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))
* Add typing to proto.Message based class attributes ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))


### Bug Fixes

* Add dict typing for client_options ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))
* Drop usage of pkg_resources ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))
* Fix timeout default values ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))

## [1.4.3](https://github.com/googleapis/python-service-usage/compare/v1.4.2...v1.4.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#148](https://github.com/googleapis/python-service-usage/issues/148)) ([b8cc381](https://github.com/googleapis/python-service-usage/commit/b8cc38152251900cb6c75b91585a465eb1b0de66))

## [1.4.2](https://github.com/googleapis/python-service-usage/compare/v1.4.1...v1.4.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#146](https://github.com/googleapis/python-service-usage/issues/146)) ([99d8d9e](https://github.com/googleapis/python-service-usage/commit/99d8d9e4282f5ab5c930055a0ac7ddfa6d399f44))

## [1.4.1](https://github.com/googleapis/python-service-usage/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#133](https://github.com/googleapis/python-service-usage/issues/133)) ([586a7f9](https://github.com/googleapis/python-service-usage/commit/586a7f92c6658c907cd990461a9a9beb45f7514a))
* **deps:** require proto-plus >= 1.22.0 ([586a7f9](https://github.com/googleapis/python-service-usage/commit/586a7f92c6658c907cd990461a9a9beb45f7514a))

## [1.4.0](https://github.com/googleapis/python-service-usage/compare/v1.3.2...v1.4.0) (2022-07-16)


### Features

* add audience parameter ([c0745b9](https://github.com/googleapis/python-service-usage/commit/c0745b92bae9a8f5dd8e2c2bf992984de422eb46))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#127](https://github.com/googleapis/python-service-usage/issues/127)) ([90975b7](https://github.com/googleapis/python-service-usage/commit/90975b7f86a1dcbbd7029e7860aee750a2cc243c))
* require python 3.7+ ([#125](https://github.com/googleapis/python-service-usage/issues/125)) ([c9de01e](https://github.com/googleapis/python-service-usage/commit/c9de01e72298c164fefb9243ab96bb3020484ab3))

## [1.3.2](https://github.com/googleapis/python-service-usage/compare/v1.3.1...v1.3.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#115](https://github.com/googleapis/python-service-usage/issues/115)) ([fc546f2](https://github.com/googleapis/python-service-usage/commit/fc546f2dc727e8b358d62f4f9958006c04b35c4c))


### Documentation

* fix changelog header to consistent size ([#116](https://github.com/googleapis/python-service-usage/issues/116)) ([1c9df92](https://github.com/googleapis/python-service-usage/commit/1c9df92b379f9735477bd7c7d590a9280e944fbd))

## [1.3.1](https://github.com/googleapis/python-service-usage/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#88](https://github.com/googleapis/python-service-usage/issues/88)) ([bee9ae0](https://github.com/googleapis/python-service-usage/commit/bee9ae00c8dd77fcc423ceb4b0023b0041d6c395))

## [1.3.0](https://github.com/googleapis/python-service-usage/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#74](https://github.com/googleapis/python-service-usage/issues/74)) ([c9cf774](https://github.com/googleapis/python-service-usage/commit/c9cf774ba8082ce7026acd582817e84b63d39fbe))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([27fb0c2](https://github.com/googleapis/python-service-usage/commit/27fb0c270dc776862f282159c9a637aa5900ced7))


### Documentation

* add generated snippets ([#79](https://github.com/googleapis/python-service-usage/issues/79)) ([dee08f1](https://github.com/googleapis/python-service-usage/commit/dee08f1d654cb5e04955ca51c824f77b13c000b9))

## [1.2.1](https://www.github.com/googleapis/python-service-usage/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([57a982c](https://www.github.com/googleapis/python-service-usage/commit/57a982c7cafb2f91a9c2d2f0f8b85be1502f14be))
* **deps:** require google-api-core >= 1.28.0 ([57a982c](https://www.github.com/googleapis/python-service-usage/commit/57a982c7cafb2f91a9c2d2f0f8b85be1502f14be))


### Documentation

* list oneofs in docstring ([57a982c](https://www.github.com/googleapis/python-service-usage/commit/57a982c7cafb2f91a9c2d2f0f8b85be1502f14be))

## [1.2.0](https://www.github.com/googleapis/python-service-usage/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add support for python 3.10 ([#53](https://www.github.com/googleapis/python-service-usage/issues/53)) ([9f235a8](https://www.github.com/googleapis/python-service-usage/commit/9f235a84d01b84a598f5af4bdd6203f4d752f31a))

## [1.1.0](https://www.github.com/googleapis/python-service-usage/compare/v1.0.1...v1.1.0) (2021-10-07)


### Features

* add context manager support in client ([#49](https://www.github.com/googleapis/python-service-usage/issues/49)) ([b50e7cb](https://www.github.com/googleapis/python-service-usage/commit/b50e7cbbf53e0efb6809bce5c25cdc7369e65f5d))


### Bug Fixes

* improper types in pagers generation ([b230f5f](https://www.github.com/googleapis/python-service-usage/commit/b230f5fd83f21b7ac86bb01dac85ce403d694228))

## [1.0.1](https://www.github.com/googleapis/python-service-usage/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([172ba0d](https://www.github.com/googleapis/python-service-usage/commit/172ba0dd5ca2d1d6ffee0cccce45ee28c822704b))

## [1.0.0](https://www.github.com/googleapis/python-service-usage/compare/v0.2.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#28](https://www.github.com/googleapis/python-service-usage/issues/28)) ([6627d2d](https://www.github.com/googleapis/python-service-usage/commit/6627d2dddf686a6ecc355891989928ca33003f00))

## [0.2.2](https://www.github.com/googleapis/python-service-usage/compare/v0.2.1...v0.2.2) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#24](https://www.github.com/googleapis/python-service-usage/issues/24)) ([cb9bed0](https://www.github.com/googleapis/python-service-usage/commit/cb9bed079e5ab4316ae79d44c8cf4bee1b4c3ae7))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#20](https://www.github.com/googleapis/python-service-usage/issues/20)) ([394ed1a](https://www.github.com/googleapis/python-service-usage/commit/394ed1a75dcfa2c70f8bbac6aaea1150a6d90052))


### Miscellaneous Chores

* release as 0.2.2 ([#25](https://www.github.com/googleapis/python-service-usage/issues/25)) ([4f1ab38](https://www.github.com/googleapis/python-service-usage/commit/4f1ab3848cf43ae7385ebf5c4dcb5f1b9057f14d))

## [0.2.1](https://www.github.com/googleapis/python-service-usage/compare/v0.2.0...v0.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#19](https://www.github.com/googleapis/python-service-usage/issues/19)) ([599eee0](https://www.github.com/googleapis/python-service-usage/commit/599eee0fe0f92efa4a19835691a9216c8804349f))

## [0.2.0](https://www.github.com/googleapis/python-service-usage/compare/v0.1.0...v0.2.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#10](https://www.github.com/googleapis/python-service-usage/issues/10)) ([87d2c40](https://www.github.com/googleapis/python-service-usage/commit/87d2c40eb4989b94229984f22e461fdc56a4f122))


### Bug Fixes

* disable always_use_jwt_access ([#14](https://www.github.com/googleapis/python-service-usage/issues/14)) ([2f90720](https://www.github.com/googleapis/python-service-usage/commit/2f907209d1199c5a9cec210495845775ae630ccf))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-service-usage/issues/1127)) ([#5](https://www.github.com/googleapis/python-service-usage/issues/5)) ([c8bbbcb](https://www.github.com/googleapis/python-service-usage/commit/c8bbbcbd939b421fa0b243f6003de54afc2107e1))

## 0.1.0 (2021-06-14)


### Features

* generate v1 ([b468d1b](https://www.github.com/googleapis/python-service-usage/commit/b468d1b447c30994d9266b5e0ff4c34ec0d19d80))
