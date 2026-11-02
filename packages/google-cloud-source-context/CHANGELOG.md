# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-source-context/#history

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.11.0...google-cloud-source-context-v1.12.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.10.0...google-cloud-source-context-v1.11.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.9.0...google-cloud-source-context-v1.10.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.8.0...google-cloud-source-context-v1.9.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.7.1...google-cloud-source-context-v1.8.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.7.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.7.0...google-cloud-source-context-v1.7.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.6.0...google-cloud-source-context-v1.7.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))
* Add support for reading selective GAPIC generation methods from service YAML ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))

## [1.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.5.5...google-cloud-source-context-v1.6.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [1.5.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.5.4...google-cloud-source-context-v1.5.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([42c4d04](https://github.com/googleapis/google-cloud-python/commit/42c4d04ee1362ba0ed0f1b6a134ac8e409875b63))

## [1.5.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.5.3...google-cloud-source-context-v1.5.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [1.5.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.5.2...google-cloud-source-context-v1.5.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [1.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.5.1...google-cloud-source-context-v1.5.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))

## [1.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.5.0...google-cloud-source-context-v1.5.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [1.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.4.3...google-cloud-source-context-v1.5.0) (2023-12-07)


### Features

* Add support for python 3.12 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Introduce compatibility with native namespace packages ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Use `retry_async` instead of `retry` in async client ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))

## [1.4.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.4.2...google-cloud-source-context-v1.4.3) (2023-09-19)


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.4.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-source-context-v1.4.1...google-cloud-source-context-v1.4.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [1.4.1](https://github.com/googleapis/python-source-context/compare/v1.4.0...v1.4.1) (2023-01-23)


### Documentation

* Add documentation for enums ([#131](https://github.com/googleapis/python-source-context/issues/131)) ([702003c](https://github.com/googleapis/python-source-context/commit/702003cf9c4bd58b8b88bca1d40ab81cb5f1ac12))

## [1.4.0](https://github.com/googleapis/python-source-context/compare/v1.3.0...v1.4.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#129](https://github.com/googleapis/python-source-context/issues/129)) ([fb1ef8a](https://github.com/googleapis/python-source-context/commit/fb1ef8a5fb266d0d2338ca3930dd06f673b08e8c))

## [1.3.0](https://github.com/googleapis/python-source-context/compare/v1.2.8...v1.3.0) (2022-12-15)


### Features

* Add support for `google.cloud.source_context.__version__` ([f6fd32c](https://github.com/googleapis/python-source-context/commit/f6fd32cd17bb36b3c002fbd3177ce267ddfdfc91))


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([#126](https://github.com/googleapis/python-source-context/issues/126)) ([665ad9f](https://github.com/googleapis/python-source-context/commit/665ad9f76d0e826b45ce63bd68ded249bcb08c17))

## [1.2.8](https://github.com/googleapis/python-source-context/compare/v1.2.7...v1.2.8) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#118](https://github.com/googleapis/python-source-context/issues/118)) ([45a19ad](https://github.com/googleapis/python-source-context/commit/45a19addbc6f1d24048b1566c23c761bdc30fea7))

## [1.2.7](https://github.com/googleapis/python-source-context/compare/v1.2.6...v1.2.7) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#116](https://github.com/googleapis/python-source-context/issues/116)) ([668bf44](https://github.com/googleapis/python-source-context/commit/668bf44578457929c4e127e02e04d5cee7c44230))

## [1.2.6](https://github.com/googleapis/python-source-context/compare/v1.2.5...v1.2.6) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#103](https://github.com/googleapis/python-source-context/issues/103)) ([bcc515b](https://github.com/googleapis/python-source-context/commit/bcc515bdafa3a6d0e992ba659f5e7bc89289edd5))
* **deps:** require proto-plus >= 1.22.0 ([bcc515b](https://github.com/googleapis/python-source-context/commit/bcc515bdafa3a6d0e992ba659f5e7bc89289edd5))

## [1.2.5](https://github.com/googleapis/python-source-context/compare/v1.2.4...v1.2.5) (2022-07-10)


### Bug Fixes

* require python 3.7+ ([#97](https://github.com/googleapis/python-source-context/issues/97)) ([e0b928e](https://github.com/googleapis/python-source-context/commit/e0b928e6407ca720867150b22a304dee3daea5f6))

## [1.2.4](https://github.com/googleapis/python-source-context/compare/v1.2.3...v1.2.4) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#87](https://github.com/googleapis/python-source-context/issues/87)) ([5b86140](https://github.com/googleapis/python-source-context/commit/5b86140b3a4ffa4c591722e127e4bbff64eab91e))


### Documentation

* fix changelog header to consistent size ([#88](https://github.com/googleapis/python-source-context/issues/88)) ([7b7fe62](https://github.com/googleapis/python-source-context/commit/7b7fe6278cf454196e89c18db63a20acd2c8aa23))

## [1.2.3](https://github.com/googleapis/python-source-context/compare/v1.2.2...v1.2.3) (2022-05-05)


### Documentation

* fix docstring for map fields ([614c640](https://github.com/googleapis/python-source-context/commit/614c640a224c6fcf0c1fd4656d871b3799508314))

## [1.2.2](https://github.com/googleapis/python-source-context/compare/v1.2.1...v1.2.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#66](https://github.com/googleapis/python-source-context/issues/66)) ([0b06641](https://github.com/googleapis/python-source-context/commit/0b06641e0a648bdebf1539eaf12f666845795b80))

## [1.2.1](https://www.github.com/googleapis/python-source-context/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([5234b6b](https://www.github.com/googleapis/python-source-context/commit/5234b6bd2e42a1b7cd6bcb4a0055801a81c928ca))
* **deps:** require google-api-core >= 1.28.0 ([5234b6b](https://www.github.com/googleapis/python-source-context/commit/5234b6bd2e42a1b7cd6bcb4a0055801a81c928ca))


### Documentation

* list oneofs in docstring ([5234b6b](https://www.github.com/googleapis/python-source-context/commit/5234b6bd2e42a1b7cd6bcb4a0055801a81c928ca))

## [1.2.0](https://www.github.com/googleapis/python-source-context/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add support for python 3.10 ([#39](https://www.github.com/googleapis/python-source-context/issues/39)) ([6d9675f](https://www.github.com/googleapis/python-source-context/commit/6d9675f6fa15e7f76ef47bf968ee9ff552f7a547))

## [1.1.0](https://www.github.com/googleapis/python-source-context/compare/v1.0.0...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#35](https://www.github.com/googleapis/python-source-context/issues/35)) ([e9694fd](https://www.github.com/googleapis/python-source-context/commit/e9694fd650aa24132013f7fd097b344969034b83))

## [1.0.0](https://www.github.com/googleapis/python-source-context/compare/v0.1.4...v1.0.0) (2021-10-04)


### Features

* bump release level to production/stable ([#31](https://www.github.com/googleapis/python-source-context/issues/31)) ([139188c](https://www.github.com/googleapis/python-source-context/commit/139188cb7a7850878b91756bacb0daf758cdcf2a))

## [0.1.4](https://www.github.com/googleapis/python-source-context/compare/v0.1.3...v0.1.4) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([0039f92](https://www.github.com/googleapis/python-source-context/commit/0039f92abf768992bdd79e68fb99407cd0e47629))

## [0.1.3](https://www.github.com/googleapis/python-source-context/compare/v0.1.2...v0.1.3) (2021-08-23)


### Documentation

* Migrate default branch to main ([#17](https://www.github.com/googleapis/python-source-context/issues/17)) ([6011f91](https://www.github.com/googleapis/python-source-context/commit/6011f91031abce8a71c5b6891a1ee8e241d580e0))

## [0.1.2](https://www.github.com/googleapis/python-source-context/compare/v0.1.1...v0.1.2) (2021-07-29)


### Documentation

* add Samples section to CONTRIBUTING.rst ([#6](https://www.github.com/googleapis/python-source-context/issues/6)) ([19c3b12](https://www.github.com/googleapis/python-source-context/commit/19c3b12f9b0447c975de206655784a19fd059d8e))


### Miscellaneous Chores

* release as 0.1.2 ([#11](https://www.github.com/googleapis/python-source-context/issues/11)) ([1581f56](https://www.github.com/googleapis/python-source-context/commit/1581f56aae3879407e6b2d6de2012760f976deaf))

## [0.1.1](https://www.github.com/googleapis/python-source-context/compare/v0.1.0...v0.1.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#5](https://www.github.com/googleapis/python-source-context/issues/5)) ([8aa433b](https://www.github.com/googleapis/python-source-context/commit/8aa433b5cfee23ab3d87463cef88e0b4c8ed770d))

## 0.1.0 (2021-06-23)


### Features

* generate v1 ([f5db974](https://www.github.com/googleapis/python-source/commit/f5db974cd7119d5b0e12ad8bcc86280abff29fd7))
