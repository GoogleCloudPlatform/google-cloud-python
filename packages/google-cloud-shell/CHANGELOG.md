# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-shell/#history

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.16.0...google-cloud-shell-v1.17.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.15.0...google-cloud-shell-v1.16.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.14.0...google-cloud-shell-v1.15.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.13.0...google-cloud-shell-v1.14.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.12.1...google-cloud-shell-v1.13.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.12.0...google-cloud-shell-v1.12.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.11.0...google-cloud-shell-v1.12.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))
* Add support for reading selective GAPIC generation methods from service YAML ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.10.1...google-cloud-shell-v1.11.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))

## [1.10.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.10.0...google-cloud-shell-v1.10.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13246](https://github.com/googleapis/google-cloud-python/issues/13246)) ([bcad563](https://github.com/googleapis/google-cloud-python/commit/bcad563acea541bb51f9fbd005f18e9f32e381f0))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.9.5...google-cloud-shell-v1.10.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [1.9.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.9.4...google-cloud-shell-v1.9.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([42c4d04](https://github.com/googleapis/google-cloud-python/commit/42c4d04ee1362ba0ed0f1b6a134ac8e409875b63))

## [1.9.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.9.3...google-cloud-shell-v1.9.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [1.9.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.9.2...google-cloud-shell-v1.9.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [1.9.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.9.1...google-cloud-shell-v1.9.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))
* fix ValueError in test__validate_universe_domain ([2451e88](https://github.com/googleapis/google-cloud-python/commit/2451e88f302bc582b3f6d01a6ec6aceba7646252))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.9.0...google-cloud-shell-v1.9.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.8.0...google-cloud-shell-v1.9.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.7.3...google-cloud-shell-v1.8.0) (2023-12-07)


### Features

* Add support for python 3.12 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Introduce compatibility with native namespace packages ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Use `retry_async` instead of `retry` in async client ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))

## [1.7.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.7.2...google-cloud-shell-v1.7.3) (2023-09-19)


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.7.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-shell-v1.7.1...google-cloud-shell-v1.7.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [1.7.1](https://github.com/googleapis/python-shell/compare/v1.7.0...v1.7.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#164](https://github.com/googleapis/python-shell/issues/164)) ([a4751ad](https://github.com/googleapis/python-shell/commit/a4751adef57a187b13bdb0605cf09394c4c1adc9))

## [1.7.0](https://github.com/googleapis/python-shell/compare/v1.6.1...v1.7.0) (2023-02-09)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#157](https://github.com/googleapis/python-shell/issues/157)) ([ab83466](https://github.com/googleapis/python-shell/commit/ab83466c220483593acaef6ef47d8813f9ebd302))

## [1.6.1](https://github.com/googleapis/python-shell/compare/v1.6.0...v1.6.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([287a2a5](https://github.com/googleapis/python-shell/commit/287a2a568fd1f1e7180afb58b393aa94ef65fe93))


### Documentation

* Add documentation for enums ([287a2a5](https://github.com/googleapis/python-shell/commit/287a2a568fd1f1e7180afb58b393aa94ef65fe93))

## [1.6.0](https://github.com/googleapis/python-shell/compare/v1.5.0...v1.6.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#149](https://github.com/googleapis/python-shell/issues/149)) ([9df9c9c](https://github.com/googleapis/python-shell/commit/9df9c9ca2b44edb4ec0acf879432be338ac8e6fe))

## [1.5.0](https://github.com/googleapis/python-shell/compare/v1.4.3...v1.5.0) (2022-12-14)


### Features

* Add CloudShellErrorCode.ENVIRONMENT_UNAVAILABLE enum value ([82fc2bc](https://github.com/googleapis/python-shell/commit/82fc2bca5b5908ded7277db4b78297294a599d3c))
* Add support for `google.cloud.shell.__version__` ([82fc2bc](https://github.com/googleapis/python-shell/commit/82fc2bca5b5908ded7277db4b78297294a599d3c))
* Add typing to proto.Message based class attributes ([82fc2bc](https://github.com/googleapis/python-shell/commit/82fc2bca5b5908ded7277db4b78297294a599d3c))


### Bug Fixes

* Add dict typing for client_options ([82fc2bc](https://github.com/googleapis/python-shell/commit/82fc2bca5b5908ded7277db4b78297294a599d3c))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([563be00](https://github.com/googleapis/python-shell/commit/563be001e063a0ef60cb15f2c59e70d4d7670a22))
* Drop usage of pkg_resources ([563be00](https://github.com/googleapis/python-shell/commit/563be001e063a0ef60cb15f2c59e70d4d7670a22))
* Fix timeout default values ([563be00](https://github.com/googleapis/python-shell/commit/563be001e063a0ef60cb15f2c59e70d4d7670a22))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([82fc2bc](https://github.com/googleapis/python-shell/commit/82fc2bca5b5908ded7277db4b78297294a599d3c))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([563be00](https://github.com/googleapis/python-shell/commit/563be001e063a0ef60cb15f2c59e70d4d7670a22))

## [1.4.3](https://github.com/googleapis/python-shell/compare/v1.4.2...v1.4.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#139](https://github.com/googleapis/python-shell/issues/139)) ([52ad573](https://github.com/googleapis/python-shell/commit/52ad5733fd97fd3a5edf93933a2b888714fdc59c))

## [1.4.2](https://github.com/googleapis/python-shell/compare/v1.4.1...v1.4.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#137](https://github.com/googleapis/python-shell/issues/137)) ([3ad02f1](https://github.com/googleapis/python-shell/commit/3ad02f134e8fae58756252f6bac7e1478f303fc2))

## [1.4.1](https://github.com/googleapis/python-shell/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#124](https://github.com/googleapis/python-shell/issues/124)) ([87ab035](https://github.com/googleapis/python-shell/commit/87ab0352e1c91e054f1929165764a97158f47e4d))
* **deps:** require proto-plus >= 1.22.0 ([87ab035](https://github.com/googleapis/python-shell/commit/87ab0352e1c91e054f1929165764a97158f47e4d))

## [1.4.0](https://github.com/googleapis/python-shell/compare/v1.3.3...v1.4.0) (2022-07-16)


### Features

* add audience parameter ([900311d](https://github.com/googleapis/python-shell/commit/900311d83e9d8c0bdd130a4b9b9e4cdfa36df28c))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#118](https://github.com/googleapis/python-shell/issues/118)) ([6fbe772](https://github.com/googleapis/python-shell/commit/6fbe772cad0080308f6e99152284e6d54a716eb5))
* require python 3.7+ ([#116](https://github.com/googleapis/python-shell/issues/116)) ([8cb5409](https://github.com/googleapis/python-shell/commit/8cb540908551132d6a689bc8019014abe174a298))

## [1.3.3](https://github.com/googleapis/python-shell/compare/v1.3.2...v1.3.3) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#106](https://github.com/googleapis/python-shell/issues/106)) ([5ac2e3b](https://github.com/googleapis/python-shell/commit/5ac2e3b0bbf79f4910a3e00f077554f78bf9accf))


### Documentation

* fix changelog header to consistent size ([#107](https://github.com/googleapis/python-shell/issues/107)) ([4d16fd5](https://github.com/googleapis/python-shell/commit/4d16fd5738b545fac4cb7b4ae47a59b618a73333))

## [1.3.2](https://github.com/googleapis/python-shell/compare/v1.3.1...v1.3.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#85](https://github.com/googleapis/python-shell/issues/85)) ([b3271c5](https://github.com/googleapis/python-shell/commit/b3271c5f07fc1326a614ab8fb365cc9b7c46c897))

## [1.3.1](https://github.com/googleapis/python-shell/compare/v1.3.0...v1.3.1) (2022-02-11)


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([b660c07](https://github.com/googleapis/python-shell/commit/b660c07d2f42673a85dd596590c82e2f972530fd))

## [1.3.0](https://github.com/googleapis/python-shell/compare/v1.2.2...v1.3.0) (2022-01-25)


### Features

* add api key support ([#70](https://github.com/googleapis/python-shell/issues/70)) ([3e91fb8](https://github.com/googleapis/python-shell/commit/3e91fb8bacf28a19e167a357829ffcbb9e0e02c9))

## [1.2.2](https://www.github.com/googleapis/python-shell/compare/v1.2.1...v1.2.2) (2022-01-07)


### Bug Fixes

* provide appropriate mock values for message body fields ([24cf144](https://www.github.com/googleapis/python-shell/commit/24cf144d17b64dc71a5182d1ccbc44444bd68450))

## [1.2.1](https://www.github.com/googleapis/python-shell/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([ff43aa0](https://www.github.com/googleapis/python-shell/commit/ff43aa0900e4fc626ab3243621f1ccc763878616))
* **deps:** require google-api-core >= 1.28.0 ([ff43aa0](https://www.github.com/googleapis/python-shell/commit/ff43aa0900e4fc626ab3243621f1ccc763878616))


### Documentation

* list oneofs in docstring ([ff43aa0](https://www.github.com/googleapis/python-shell/commit/ff43aa0900e4fc626ab3243621f1ccc763878616))

## [1.2.0](https://www.github.com/googleapis/python-shell/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add support for python 3.10 ([#45](https://www.github.com/googleapis/python-shell/issues/45)) ([c8d6c7e](https://www.github.com/googleapis/python-shell/commit/c8d6c7ecf22d929963de5433f9d7abe7c7c402fd))

## [1.1.0](https://www.github.com/googleapis/python-shell/compare/v1.0.1...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#41](https://www.github.com/googleapis/python-shell/issues/41)) ([33eb545](https://www.github.com/googleapis/python-shell/commit/33eb545715c52bb3e8e04cba07ee84466ace672e))

## [1.0.1](https://www.github.com/googleapis/python-shell/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([c07f6c9](https://www.github.com/googleapis/python-shell/commit/c07f6c900b41a7513fa73a36544f62d429d1a36d))

## [1.0.0](https://www.github.com/googleapis/python-shell/compare/v0.2.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#25](https://www.github.com/googleapis/python-shell/issues/25)) ([9a1a44e](https://www.github.com/googleapis/python-shell/commit/9a1a44e65f4c9adc16bce134046752e10d04ce4b))

## [0.2.2](https://www.github.com/googleapis/python-shell/compare/v0.2.1...v0.2.2) (2021-07-30)


### Features

* add Samples section to CONTRIBUTING.rst ([#17](https://www.github.com/googleapis/python-shell/issues/17)) ([ce23d47](https://www.github.com/googleapis/python-shell/commit/ce23d475183fa3baa561f23c30d28cac09f6794d))


### Bug Fixes

* enable self signed jwt for grpc ([#21](https://www.github.com/googleapis/python-shell/issues/21)) ([0dafd2f](https://www.github.com/googleapis/python-shell/commit/0dafd2fbb839fcca38d6dc27b9fffff182f2add0))


### Miscellaneous Chores

* release as 0.2.2 ([#22](https://www.github.com/googleapis/python-shell/issues/22)) ([d3b208a](https://www.github.com/googleapis/python-shell/commit/d3b208aa33932c1008c5627d61bcd8dcf67aa85a))

## [0.2.1](https://www.github.com/googleapis/python-shell/compare/v0.2.0...v0.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#16](https://www.github.com/googleapis/python-shell/issues/16)) ([61b6123](https://www.github.com/googleapis/python-shell/commit/61b61231accd865e69f3a3b097e1c1c1a755f3bc))

## [0.2.0](https://www.github.com/googleapis/python-shell/compare/v0.1.0...v0.2.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#9](https://www.github.com/googleapis/python-shell/issues/9)) ([13ce7ba](https://www.github.com/googleapis/python-shell/commit/13ce7bab4613f287a73743d80d1bbbee5c59969a))


### Bug Fixes

* disable always_use_jwt_access ([b447260](https://www.github.com/googleapis/python-shell/commit/b4472606f4eb050b9135d5dd948d65ae065a1e04))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-shell/issues/1127)) ([#4](https://www.github.com/googleapis/python-shell/issues/4)) ([0150a5d](https://www.github.com/googleapis/python-shell/commit/0150a5d71e22b6aeb194cd2992d58ed03683d1ca)), closes [#1126](https://www.github.com/googleapis/python-shell/issues/1126)

## 0.1.0 (2021-06-13)


### Features

* generate v1 ([311a15b](https://www.github.com/googleapis/python-shell/commit/311a15b0a8ee3a4695e3922b549e534be5d019ab))
