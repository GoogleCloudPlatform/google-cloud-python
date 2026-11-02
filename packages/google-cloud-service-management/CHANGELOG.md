# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-service-management/#history

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.17.0...google-cloud-service-management-v1.18.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.16.0...google-cloud-service-management-v1.17.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.15.0...google-cloud-service-management-v1.16.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.14.0...google-cloud-service-management-v1.15.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.13.2...google-cloud-service-management-v1.14.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.13.1...google-cloud-service-management-v1.13.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.13.0...google-cloud-service-management-v1.13.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([770cf0f](https://github.com/googleapis/google-cloud-python/commit/770cf0f31125586a8622e9639f6d24c1bafa9b31))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.12.0...google-cloud-service-management-v1.13.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([7a2f3e6](https://github.com/googleapis/google-cloud-python/commit/7a2f3e60244aac5e5037f442629ff84c58a3fbf0))
* add support for field generate_omitted_as_internal in selective gapic generation ([7a2f3e6](https://github.com/googleapis/google-cloud-python/commit/7a2f3e60244aac5e5037f442629ff84c58a3fbf0))
* Add support for reading selective GAPIC generation methods from service YAML ([7a2f3e6](https://github.com/googleapis/google-cloud-python/commit/7a2f3e60244aac5e5037f442629ff84c58a3fbf0))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.11.0...google-cloud-service-management-v1.12.0) (2024-12-12)


### Features

* add service renaming to GoSettings ([9dc3d4a](https://github.com/googleapis/google-cloud-python/commit/9dc3d4ac473823860bb27172c0d05a37643c794a))
* Add support for opt-in debug logging ([9dc3d4a](https://github.com/googleapis/google-cloud-python/commit/9dc3d4ac473823860bb27172c0d05a37643c794a))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([9dc3d4a](https://github.com/googleapis/google-cloud-python/commit/9dc3d4ac473823860bb27172c0d05a37643c794a))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.10.1...google-cloud-service-management-v1.11.0) (2024-11-11)


### Features

* Add field protobuf_pythonic_types_enabled to message ExperimentalFeatures ([a6897e3](https://github.com/googleapis/google-cloud-python/commit/a6897e3f763e831a22602d1860f1810e9600e014))


### Documentation

* A comment for field `unit` in message `.google.api.QuotaLimit` is changed ([a6897e3](https://github.com/googleapis/google-cloud-python/commit/a6897e3f763e831a22602d1860f1810e9600e014))

## [1.10.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.10.0...google-cloud-service-management-v1.10.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([59c4287](https://github.com/googleapis/google-cloud-python/commit/59c42878386ee08d1717b73e47d33d76cfb38ba0))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.9.0...google-cloud-service-management-v1.10.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13202](https://github.com/googleapis/google-cloud-python/issues/13202)) ([5b1f2f3](https://github.com/googleapis/google-cloud-python/commit/5b1f2f3a81ed171b643812e67a7ed179b9b703ea))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.8.5...google-cloud-service-management-v1.9.0) (2024-09-03)


### Features

* Support local binding for variables with keyword name collision ([c54700d](https://github.com/googleapis/google-cloud-python/commit/c54700d3e11e59eb5fae01fda25dbf3a9acbe382))

## [1.8.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.8.4...google-cloud-service-management-v1.8.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([42c4d04](https://github.com/googleapis/google-cloud-python/commit/42c4d04ee1362ba0ed0f1b6a134ac8e409875b63))

## [1.8.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.8.3...google-cloud-service-management-v1.8.4) (2024-07-08)


### Bug Fixes

* Allow protobuf 5.x ([04ec204](https://github.com/googleapis/google-cloud-python/commit/04ec2046ed11c690273912e1bb6220823c7dd7c0))

## [1.8.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.8.2...google-cloud-service-management-v1.8.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [1.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.8.1...google-cloud-service-management-v1.8.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12283](https://github.com/googleapis/google-cloud-python/issues/12283)) ([f20b41a](https://github.com/googleapis/google-cloud-python/commit/f20b41ac35b02a40135b83edfe819ff7a355ab21))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))

## [1.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.8.0...google-cloud-service-management-v1.8.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.7.0...google-cloud-service-management-v1.8.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-management-v1.6.1...google-cloud-service-management-v1.7.0) (2023-12-07)


### Features

* Add support for python 3.12 ([0e3a902](https://github.com/googleapis/google-cloud-python/commit/0e3a9027360f73b64c68ced4d079fcd2eaf3120d))
* Introduce compatibility with native namespace packages ([0e3a902](https://github.com/googleapis/google-cloud-python/commit/0e3a9027360f73b64c68ced4d079fcd2eaf3120d))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([0e3a902](https://github.com/googleapis/google-cloud-python/commit/0e3a9027360f73b64c68ced4d079fcd2eaf3120d))
* Use `retry_async` instead of `retry` in async client ([0e3a902](https://github.com/googleapis/google-cloud-python/commit/0e3a9027360f73b64c68ced4d079fcd2eaf3120d))

## [1.6.1](https://github.com/googleapis/python-service-management/compare/v1.6.0...v1.6.1) (2023-03-23)


### Bug Fixes

* **deps:** Require googleapis-common-protos &gt;= 1.59.0 ([#199](https://github.com/googleapis/python-service-management/issues/199)) ([e36155c](https://github.com/googleapis/python-service-management/commit/e36155c9455ae30a3ff9c8f928a16d534e36aa3d))


### Documentation

* Fix formatting of request arg in docstring ([#201](https://github.com/googleapis/python-service-management/issues/201)) ([5dfeb11](https://github.com/googleapis/python-service-management/commit/5dfeb1179bf12e785f1e8079abd6bf80ad3e2fdb))

## [1.6.0](https://github.com/googleapis/python-service-management/compare/v1.5.1...v1.6.0) (2023-02-17)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#192](https://github.com/googleapis/python-service-management/issues/192)) ([b4c2aa2](https://github.com/googleapis/python-service-management/commit/b4c2aa2b7be38bd3101a582c326b75a74468f9a6))

## [1.5.1](https://github.com/googleapis/python-service-management/compare/v1.5.0...v1.5.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([4436870](https://github.com/googleapis/python-service-management/commit/443687007443553e1aa4881d7923f68575626015))


### Documentation

* Add documentation for enums ([4436870](https://github.com/googleapis/python-service-management/commit/443687007443553e1aa4881d7923f68575626015))

## [1.5.0](https://github.com/googleapis/python-service-management/compare/v1.4.0...v1.5.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#184](https://github.com/googleapis/python-service-management/issues/184)) ([0aeacd5](https://github.com/googleapis/python-service-management/commit/0aeacd51f9388e62a1ae009aa11415d500a5021e))

## [1.4.0](https://github.com/googleapis/python-service-management/compare/v1.3.3...v1.4.0) (2022-12-14)


### Features

* Add support for `google.cloud.servicemanagement.__version__` ([9c86c72](https://github.com/googleapis/python-service-management/commit/9c86c7250b6fdea6cacdd6a031525a35966b281c))
* Add typing to proto.Message based class attributes ([9c86c72](https://github.com/googleapis/python-service-management/commit/9c86c7250b6fdea6cacdd6a031525a35966b281c))


### Bug Fixes

* Add dict typing for client_options ([9c86c72](https://github.com/googleapis/python-service-management/commit/9c86c7250b6fdea6cacdd6a031525a35966b281c))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([c5f88eb](https://github.com/googleapis/python-service-management/commit/c5f88eb83b40ca345ef36ca2c2d754036d0a5e46))
* Drop usage of pkg_resources ([c5f88eb](https://github.com/googleapis/python-service-management/commit/c5f88eb83b40ca345ef36ca2c2d754036d0a5e46))
* Fix timeout default values ([c5f88eb](https://github.com/googleapis/python-service-management/commit/c5f88eb83b40ca345ef36ca2c2d754036d0a5e46))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([9c86c72](https://github.com/googleapis/python-service-management/commit/9c86c7250b6fdea6cacdd6a031525a35966b281c))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([c5f88eb](https://github.com/googleapis/python-service-management/commit/c5f88eb83b40ca345ef36ca2c2d754036d0a5e46))

## [1.3.3](https://github.com/googleapis/python-service-management/compare/v1.3.2...v1.3.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#173](https://github.com/googleapis/python-service-management/issues/173)) ([c97c57a](https://github.com/googleapis/python-service-management/commit/c97c57a8fc207bd5920fbb02299e880aba21c378))

## [1.3.2](https://github.com/googleapis/python-service-management/compare/v1.3.1...v1.3.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#171](https://github.com/googleapis/python-service-management/issues/171)) ([8c9ecfd](https://github.com/googleapis/python-service-management/commit/8c9ecfdb8a3cb31a95baa46bd703d63bdf4f5e39))

## [1.3.1](https://github.com/googleapis/python-service-management/compare/v1.3.0...v1.3.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#158](https://github.com/googleapis/python-service-management/issues/158)) ([fbe3c6d](https://github.com/googleapis/python-service-management/commit/fbe3c6d9b1d560b4c7f20a28666dfb6ee19c7348))
* **deps:** require proto-plus >= 1.22.0 ([fbe3c6d](https://github.com/googleapis/python-service-management/commit/fbe3c6d9b1d560b4c7f20a28666dfb6ee19c7348))

## [1.3.0](https://github.com/googleapis/python-service-management/compare/v1.2.3...v1.3.0) (2022-07-16)


### Features

* add audience parameter ([7be1829](https://github.com/googleapis/python-service-management/commit/7be1829be33a4c26a6fe3f9072352129da64ca5a))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#149](https://github.com/googleapis/python-service-management/issues/149)) ([7be1829](https://github.com/googleapis/python-service-management/commit/7be1829be33a4c26a6fe3f9072352129da64ca5a))
* require python 3.7+ ([#151](https://github.com/googleapis/python-service-management/issues/151)) ([7dfff48](https://github.com/googleapis/python-service-management/commit/7dfff48e46fa806556eaf77a378e7b0f16aab7fb))

## [1.2.3](https://github.com/googleapis/python-service-management/compare/v1.2.2...v1.2.3) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#141](https://github.com/googleapis/python-service-management/issues/141)) ([4c7181c](https://github.com/googleapis/python-service-management/commit/4c7181cb92354ba4d1adcaaf67d8cd374be1943a))


### Documentation

* fix changelog header to consistent size ([#142](https://github.com/googleapis/python-service-management/issues/142)) ([61c20c7](https://github.com/googleapis/python-service-management/commit/61c20c73279399731f4c525bbf328a27e17f64dc))

## [1.2.2](https://github.com/googleapis/python-service-management/compare/v1.2.1...v1.2.2) (2022-05-05)


### Documentation

* fix broken links ([#121](https://github.com/googleapis/python-service-management/issues/121)) ([f67944e](https://github.com/googleapis/python-service-management/commit/f67944e9c1865447b452bca6d852879e90664ab2))
* fix broken links ([#126](https://github.com/googleapis/python-service-management/issues/126)) ([1988c2d](https://github.com/googleapis/python-service-management/commit/1988c2ddf9b9c9929ea263246a98cbfb8d4c7980))

## [1.2.1](https://github.com/googleapis/python-service-management/compare/v1.2.0...v1.2.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#107](https://github.com/googleapis/python-service-management/issues/107)) ([4fc6a16](https://github.com/googleapis/python-service-management/commit/4fc6a16ac804b65cf5a9443b07a3522cbfbf68af))

## [1.2.0](https://github.com/googleapis/python-service-management/compare/v1.1.1...v1.2.0) (2022-02-18)


### Features

* add api key support ([#91](https://github.com/googleapis/python-service-management/issues/91)) ([ad49299](https://github.com/googleapis/python-service-management/commit/ad49299424aefbaaef686c79af533058d5fa5b66))


### Bug Fixes

* **deps:** remove unused dependency libcst ([#97](https://github.com/googleapis/python-service-management/issues/97)) ([b2b62f1](https://github.com/googleapis/python-service-management/commit/b2b62f156e0ca50d10c0941af7e4fedcd42d8e4c))
* Remove EnableService and DisableService RPC methods and related modules ([#98](https://github.com/googleapis/python-service-management/issues/98)) ([9a2d72c](https://github.com/googleapis/python-service-management/commit/9a2d72c0eb27238925634b1950f40a90ff4d64a0))
* resolve DuplicateCredentialArgs error when using credentials_file ([21f9f5d](https://github.com/googleapis/python-service-management/commit/21f9f5deb04992ecc683afda5c4dd3cae5ffffd3))

## [1.1.1](https://www.github.com/googleapis/python-service-management/compare/v1.1.0...v1.1.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([f00ac02](https://www.github.com/googleapis/python-service-management/commit/f00ac02469bd7b8b5462ffcf2028fa25d33369cb))
* **deps:** require google-api-core >= 1.28.0 ([f00ac02](https://www.github.com/googleapis/python-service-management/commit/f00ac02469bd7b8b5462ffcf2028fa25d33369cb))


### Documentation

* list oneofs in docstring ([f00ac02](https://www.github.com/googleapis/python-service-management/commit/f00ac02469bd7b8b5462ffcf2028fa25d33369cb))

## [1.1.0](https://www.github.com/googleapis/python-service-management/compare/v1.0.4...v1.1.0) (2021-10-26)


### Features

* add context manager support in client ([#63](https://www.github.com/googleapis/python-service-management/issues/63)) ([71186c1](https://www.github.com/googleapis/python-service-management/commit/71186c1256a9bfbd65f2fcd9ed639f724400eeaf))

## [1.0.4](https://www.github.com/googleapis/python-service-management/compare/v1.0.3...v1.0.4) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([538b500](https://www.github.com/googleapis/python-service-management/commit/538b5005bac38276ffaaa3c6a2d82f9d7bff3477))

## [1.0.3](https://www.github.com/googleapis/python-service-management/compare/v1.0.2...v1.0.3) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([7547e3a](https://www.github.com/googleapis/python-service-management/commit/7547e3a53a6a437e56cbc832d62aecc627cb4cd6))

## [1.0.2](https://www.github.com/googleapis/python-service-management/compare/v1.0.1...v1.0.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#41](https://www.github.com/googleapis/python-service-management/issues/41)) ([a995bbb](https://www.github.com/googleapis/python-service-management/commit/a995bbb11f53bfd2a224155d0665c141aababc1e))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#37](https://www.github.com/googleapis/python-service-management/issues/37)) ([87472ed](https://www.github.com/googleapis/python-service-management/commit/87472ed593f442e7b73a3aa2ee45a4357094d290))


### Miscellaneous Chores

* release as 1.0.2 ([#42](https://www.github.com/googleapis/python-service-management/issues/42)) ([27b79f7](https://www.github.com/googleapis/python-service-management/commit/27b79f7d63ae01e2ba6553eaeedb20b86e878f88))

## [1.0.1](https://www.github.com/googleapis/python-service-management/compare/v1.0.0...v1.0.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#36](https://www.github.com/googleapis/python-service-management/issues/36)) ([84e2ee4](https://www.github.com/googleapis/python-service-management/commit/84e2ee48eaf4605bb445ac01479c4aada420679a))

## [1.0.0](https://www.github.com/googleapis/python-service-management/compare/v0.1.0...v1.0.0) (2021-07-10)


### Features

* add always_use_jwt_access ([#31](https://www.github.com/googleapis/python-service-management/issues/31)) ([8d76ae3](https://www.github.com/googleapis/python-service-management/commit/8d76ae37bb3186e8aa0991fa89a4852dd0798280))
* bump release level to production/stable ([#17](https://www.github.com/googleapis/python-service-management/issues/17)) ([f521883](https://www.github.com/googleapis/python-service-management/commit/f52188344dea468736855dd357570d6a428b2f62))
* support self-signed JWT flow for service accounts ([cb785b5](https://www.github.com/googleapis/python-service-management/commit/cb785b5b6885a7063f49de76ab2ff0145a83e4fe))


### Bug Fixes

* add async client ([cb785b5](https://www.github.com/googleapis/python-service-management/commit/cb785b5b6885a7063f49de76ab2ff0145a83e4fe))
* **deps:** add packaging requirement ([#18](https://www.github.com/googleapis/python-service-management/issues/18)) ([d7084d9](https://www.github.com/googleapis/python-service-management/commit/d7084d9a4d019d54d2a7e5ded04d9d3996f0cc4c))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-service-management/issues/1127)) ([#25](https://www.github.com/googleapis/python-service-management/issues/25)) ([78f33d1](https://www.github.com/googleapis/python-service-management/commit/78f33d18edec8caa2c014258307289c9aef3d609))


### Miscellaneous Chores

* release as 1.0.0 ([#22](https://www.github.com/googleapis/python-service-management/issues/22)) ([028b5a1](https://www.github.com/googleapis/python-service-management/commit/028b5a15fd80dfd62ae708a53cdef6de95ecbe92))

## 0.1.0 (2021-03-24)


### Features

* generate v1 ([1088a47](https://www.github.com/googleapis/python-service-management/commit/1088a4726aa3e5bd8b04e37db2a9e99329d1e5a5))
