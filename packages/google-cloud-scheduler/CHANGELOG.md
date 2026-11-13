# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-scheduler/#history

## [2.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.20.0...google-cloud-scheduler-v2.21.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [2.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.19.0...google-cloud-scheduler-v2.20.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [2.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.18.0...google-cloud-scheduler-v2.19.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [2.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.17.0...google-cloud-scheduler-v2.18.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [2.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.16.1...google-cloud-scheduler-v2.17.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [2.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.16.0...google-cloud-scheduler-v2.16.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [2.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.15.1...google-cloud-scheduler-v2.16.0) (2025-02-18)


### Features

* Add REST Interceptors which support reading metadata ([c8e0760](https://github.com/googleapis/google-cloud-python/commit/c8e0760e8088950c62279335216ad1d17716ce59))
* Add support for reading selective GAPIC generation methods from service YAML ([c8e0760](https://github.com/googleapis/google-cloud-python/commit/c8e0760e8088950c62279335216ad1d17716ce59))

## [2.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.15.0...google-cloud-scheduler-v2.15.1) (2025-01-27)


### Documentation

* annotate output-only fields as such ([6707477](https://github.com/googleapis/google-cloud-python/commit/6707477f8b97de7163303f6bdd56e191b0037a38))
* update comments ([6707477](https://github.com/googleapis/google-cloud-python/commit/6707477f8b97de7163303f6bdd56e191b0037a38))

## [2.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.14.1...google-cloud-scheduler-v2.15.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))

## [2.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.14.0...google-cloud-scheduler-v2.14.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13245](https://github.com/googleapis/google-cloud-python/issues/13245)) ([875f712](https://github.com/googleapis/google-cloud-python/commit/875f712265a36919409964f5ade218330f1d0147))

## [2.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.13.5...google-cloud-scheduler-v2.14.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [2.13.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.13.4...google-cloud-scheduler-v2.13.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([52db52e](https://github.com/googleapis/google-cloud-python/commit/52db52ea05c6883b07956d323fdd1d3029806374))

## [2.13.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.13.3...google-cloud-scheduler-v2.13.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [2.13.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.13.2...google-cloud-scheduler-v2.13.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [2.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.13.1...google-cloud-scheduler-v2.13.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))
* fix ValueError in test__validate_universe_domain ([89c1b05](https://github.com/googleapis/google-cloud-python/commit/89c1b054f321b90ab4eed0139a3a2a79c369730d))

## [2.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.13.0...google-cloud-scheduler-v2.13.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [2.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.12.0...google-cloud-scheduler-v2.13.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [2.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.11.3...google-cloud-scheduler-v2.12.0) (2023-12-07)


### Features

* Add support for python 3.12 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Introduce compatibility with native namespace packages ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Use `retry_async` instead of `retry` in async client ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))

## [2.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.11.2...google-cloud-scheduler-v2.11.3) (2023-11-13)


### Documentation

* [google-cloud-scheduler] correct timezone/offset information for Cloud Scheduler headers ([#12007](https://github.com/googleapis/google-cloud-python/issues/12007)) ([dd04e8f](https://github.com/googleapis/google-cloud-python/commit/dd04e8f16d965e7f9278e9ef24cd7dbdcc1363ec))

## [2.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-scheduler-v2.11.1...google-cloud-scheduler-v2.11.2) (2023-09-30)


### Documentation

* Minor formatting ([#353](https://github.com/googleapis/google-cloud-python/issues/353)) ([951433b](https://github.com/googleapis/google-cloud-python/commit/951433b152f9d6e3f87e0b9ccffc4170125283a8))

## [2.11.1](https://github.com/googleapis/python-scheduler/compare/v2.11.0...v2.11.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#340](https://github.com/googleapis/python-scheduler/issues/340)) ([7e65978](https://github.com/googleapis/python-scheduler/commit/7e65978db72b38d1fed273562df86dd058cfd271))

## [2.11.0](https://github.com/googleapis/python-scheduler/compare/v2.10.0...v2.11.0) (2023-03-23)


### Features

* Location API methods ([#324](https://github.com/googleapis/python-scheduler/issues/324)) ([662e648](https://github.com/googleapis/python-scheduler/commit/662e6489710ea62b86b43d04f9bc69f9bc96e8b8))


### Documentation

* Fix formatting of request arg in docstring ([#328](https://github.com/googleapis/python-scheduler/issues/328)) ([94e406e](https://github.com/googleapis/python-scheduler/commit/94e406eb242b027824536e597ced29b6f82cba97))

## [2.10.0](https://github.com/googleapis/python-scheduler/compare/v2.9.1...v2.10.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([3de2adb](https://github.com/googleapis/python-scheduler/commit/3de2adbc753902bdfa72085567da4e45a520416e))

## [2.9.1](https://github.com/googleapis/python-scheduler/compare/v2.9.0...v2.9.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([1ebe016](https://github.com/googleapis/python-scheduler/commit/1ebe016e8c755cd94465090079a98d304ca0e730))


### Documentation

* Add documentation for enums ([1ebe016](https://github.com/googleapis/python-scheduler/commit/1ebe016e8c755cd94465090079a98d304ca0e730))

## [2.9.0](https://github.com/googleapis/python-scheduler/compare/v2.8.0...v2.9.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#307](https://github.com/googleapis/python-scheduler/issues/307)) ([455fa74](https://github.com/googleapis/python-scheduler/commit/455fa74db83f7ca93f822acec4002358cfd27f3e))

## [2.8.0](https://github.com/googleapis/python-scheduler/compare/v2.7.3...v2.8.0) (2022-12-14)


### Features

* Add support for `google.cloud.scheduler.__version__` ([ab1a908](https://github.com/googleapis/python-scheduler/commit/ab1a9089bbb8f9dd0b4ea26afffa8ae7e7ad069a))
* Add typing to proto.Message based class attributes ([ab1a908](https://github.com/googleapis/python-scheduler/commit/ab1a9089bbb8f9dd0b4ea26afffa8ae7e7ad069a))
* Updated Client Libraries for Cloud Scheduler ([#304](https://github.com/googleapis/python-scheduler/issues/304)) ([a6cad2f](https://github.com/googleapis/python-scheduler/commit/a6cad2f03d2846f672f8403d38d2fcb9da69912b))


### Bug Fixes

* Add dict typing for client_options ([ab1a908](https://github.com/googleapis/python-scheduler/commit/ab1a9089bbb8f9dd0b4ea26afffa8ae7e7ad069a))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([75a677a](https://github.com/googleapis/python-scheduler/commit/75a677a30af56568ae365715056360d23f4b7f7c))
* Drop usage of pkg_resources ([75a677a](https://github.com/googleapis/python-scheduler/commit/75a677a30af56568ae365715056360d23f4b7f7c))
* Fix timeout default values ([75a677a](https://github.com/googleapis/python-scheduler/commit/75a677a30af56568ae365715056360d23f4b7f7c))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([ab1a908](https://github.com/googleapis/python-scheduler/commit/ab1a9089bbb8f9dd0b4ea26afffa8ae7e7ad069a))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([75a677a](https://github.com/googleapis/python-scheduler/commit/75a677a30af56568ae365715056360d23f4b7f7c))

## [2.7.3](https://github.com/googleapis/python-scheduler/compare/v2.7.2...v2.7.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#291](https://github.com/googleapis/python-scheduler/issues/291)) ([f0195d0](https://github.com/googleapis/python-scheduler/commit/f0195d0f5ef9e8b6342da965832a2a93fe795df2))

## [2.7.2](https://github.com/googleapis/python-scheduler/compare/v2.7.1...v2.7.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#288](https://github.com/googleapis/python-scheduler/issues/288)) ([c8357fe](https://github.com/googleapis/python-scheduler/commit/c8357fe07bd79d52b72f2733b7a7cf9557386b57))

## [2.7.1](https://github.com/googleapis/python-scheduler/compare/v2.7.0...v2.7.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#268](https://github.com/googleapis/python-scheduler/issues/268)) ([7081d77](https://github.com/googleapis/python-scheduler/commit/7081d777761e201a29b3d6d0542e30a1761350e0))
* **deps:** require proto-plus >= 1.22.0 ([7081d77](https://github.com/googleapis/python-scheduler/commit/7081d777761e201a29b3d6d0542e30a1761350e0))

## [2.7.0](https://github.com/googleapis/python-scheduler/compare/v2.6.4...v2.7.0) (2022-07-16)


### Features

* add audience parameter ([c8adf9c](https://github.com/googleapis/python-scheduler/commit/c8adf9c9877d4bbea2f5b282f95cb9f56011a94f))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#258](https://github.com/googleapis/python-scheduler/issues/258)) ([a57f965](https://github.com/googleapis/python-scheduler/commit/a57f96505640623170ae6b86c604127d14481561))
* require python 3.7+ ([#256](https://github.com/googleapis/python-scheduler/issues/256)) ([6b0faa0](https://github.com/googleapis/python-scheduler/commit/6b0faa00c155798fac1218a1f05cda54b3651f65))

## [2.6.4](https://github.com/googleapis/python-scheduler/compare/v2.6.3...v2.6.4) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#243](https://github.com/googleapis/python-scheduler/issues/243)) ([72b64ad](https://github.com/googleapis/python-scheduler/commit/72b64ad3ff1dbf92273c73e07c798f974f6afd5e))


### Documentation

* fix changelog header to consistent size ([#244](https://github.com/googleapis/python-scheduler/issues/244)) ([b6b6fd1](https://github.com/googleapis/python-scheduler/commit/b6b6fd1f607f7b67867e8dc31472c69c9ef20958))

## [2.6.3](https://github.com/googleapis/python-scheduler/compare/v2.6.2...v2.6.3) (2022-04-14)


### Bug Fixes

* fix type in docstring for map fields ([#223](https://github.com/googleapis/python-scheduler/issues/223)) ([34d7478](https://github.com/googleapis/python-scheduler/commit/34d7478c4ac14489b36980099446b9520ff3eb4a))

## [2.6.2](https://github.com/googleapis/python-scheduler/compare/v2.6.1...v2.6.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#203](https://github.com/googleapis/python-scheduler/issues/203)) ([3e68808](https://github.com/googleapis/python-scheduler/commit/3e688088d09b0ff5af55571b4e47109638a47825))
* **deps:** require proto-plus>=1.15.0 ([3e68808](https://github.com/googleapis/python-scheduler/commit/3e688088d09b0ff5af55571b4e47109638a47825))

## [2.6.1](https://github.com/googleapis/python-scheduler/compare/v2.6.0...v2.6.1) (2022-02-26)


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([993ac1a](https://github.com/googleapis/python-scheduler/commit/993ac1a793fef60730546f1faae269624efb98f7))


### Documentation

* add generated snippets ([#189](https://github.com/googleapis/python-scheduler/issues/189)) ([eccf8c6](https://github.com/googleapis/python-scheduler/commit/eccf8c635d1c2a93d933ed1381da42a18d128fec))

## [2.6.0](https://github.com/googleapis/python-scheduler/compare/v2.5.1...v2.6.0) (2022-01-25)


### Features

* add api key support ([#180](https://github.com/googleapis/python-scheduler/issues/180)) ([74eaf8b](https://github.com/googleapis/python-scheduler/commit/74eaf8b00c684c476d7a9f271880e83fc67dedac))

## [2.5.1](https://www.github.com/googleapis/python-scheduler/compare/v2.5.0...v2.5.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([240c125](https://www.github.com/googleapis/python-scheduler/commit/240c12575f8ac31c5262ad111a99a01b4dd4711a))
* **deps:** require google-api-core >= 1.28.0 ([240c125](https://www.github.com/googleapis/python-scheduler/commit/240c12575f8ac31c5262ad111a99a01b4dd4711a))


### Documentation

* list oneofs in docstring ([240c125](https://www.github.com/googleapis/python-scheduler/commit/240c12575f8ac31c5262ad111a99a01b4dd4711a))

## [2.5.0](https://www.github.com/googleapis/python-scheduler/compare/v2.4.0...v2.5.0) (2021-10-25)


### Features

* add support for python 3.10 ([#149](https://www.github.com/googleapis/python-scheduler/issues/149)) ([8c671d9](https://www.github.com/googleapis/python-scheduler/commit/8c671d928f9a39dc7c15cd1e700363e028eb61e7))

## [2.4.0](https://www.github.com/googleapis/python-scheduler/compare/v2.3.4...v2.4.0) (2021-10-08)


### Features

* add context manager support in client ([#144](https://www.github.com/googleapis/python-scheduler/issues/144)) ([4bb0fb6](https://www.github.com/googleapis/python-scheduler/commit/4bb0fb62f173edc09b640b0024d2be3bbd97b3b9))

## [2.3.4](https://www.github.com/googleapis/python-scheduler/compare/v2.3.3...v2.3.4) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([a24ad41](https://www.github.com/googleapis/python-scheduler/commit/a24ad41ae62407bc542eb5362f2fd84a1370d3c2))

## [2.3.3](https://www.github.com/googleapis/python-scheduler/compare/v2.3.2...v2.3.3) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([b8b77d1](https://www.github.com/googleapis/python-scheduler/commit/b8b77d11a46136baf2739cfdf48060bd4bfc10fa))

## [2.3.2](https://www.github.com/googleapis/python-scheduler/compare/v2.3.1...v2.3.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#116](https://www.github.com/googleapis/python-scheduler/issues/116)) ([a18fe2a](https://www.github.com/googleapis/python-scheduler/commit/a18fe2a4fe3dff4550687c0853aee351b54596de))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#111](https://www.github.com/googleapis/python-scheduler/issues/111)) ([ed91668](https://www.github.com/googleapis/python-scheduler/commit/ed9166882974b4eadb63df4e5278e88aeb0f8d89))


### Miscellaneous Chores

* release as 2.3.2 ([#117](https://www.github.com/googleapis/python-scheduler/issues/117)) ([f06e90b](https://www.github.com/googleapis/python-scheduler/commit/f06e90b68a9021108a732ca9733a80f447489be8))

## [2.3.1](https://www.github.com/googleapis/python-scheduler/compare/v2.3.0...v2.3.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#110](https://www.github.com/googleapis/python-scheduler/issues/110)) ([2b68578](https://www.github.com/googleapis/python-scheduler/commit/2b6857876f22441960badebbcdfac19130b1af9a))

## [2.3.0](https://www.github.com/googleapis/python-scheduler/compare/v2.2.0...v2.3.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#102](https://www.github.com/googleapis/python-scheduler/issues/102)) ([bd5550b](https://www.github.com/googleapis/python-scheduler/commit/bd5550b4c7732ad20c5a16fa0ac2c9f86704b8fc))


### Bug Fixes

* **deps:** add packaging requirement ([#89](https://www.github.com/googleapis/python-scheduler/issues/89)) ([8966559](https://www.github.com/googleapis/python-scheduler/commit/8966559b7bf2e4409906ca4a5eb831a011ba3484))
* disable always_use_jwt_access ([#106](https://www.github.com/googleapis/python-scheduler/issues/106)) ([c8dd497](https://www.github.com/googleapis/python-scheduler/commit/c8dd497c56f475c63c05c2ba5708067cc03c4173))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-scheduler/issues/1127)) ([#99](https://www.github.com/googleapis/python-scheduler/issues/99)) ([2dcbcdf](https://www.github.com/googleapis/python-scheduler/commit/2dcbcdf36c7678ee62d2b76ea31bee69f597d3b2)), closes [#1126](https://www.github.com/googleapis/python-scheduler/issues/1126)

## [2.2.0](https://www.github.com/googleapis/python-scheduler/compare/v2.1.1...v2.2.0) (2021-03-31)


### Features

* add `from_service_account_info` ([#67](https://www.github.com/googleapis/python-scheduler/issues/67)) ([bd21900](https://www.github.com/googleapis/python-scheduler/commit/bd2190046269eea1e08111b97f01e845f748b8e5))

## [2.1.1](https://www.github.com/googleapis/python-scheduler/compare/v2.1.0...v2.1.1) (2021-02-08)


### Bug Fixes

* remove client recv msg limit and add enums to `types/__init__.py` ([#46](https://www.github.com/googleapis/python-scheduler/issues/46)) ([b6a9feb](https://www.github.com/googleapis/python-scheduler/commit/b6a9feb31aec9ee1aa4eb46ccd44dcc8e6cc27a7))

## [2.1.0](https://www.github.com/googleapis/python-scheduler/compare/v2.0.0...v2.1.0) (2020-12-08)


### Features

* add common resource helpers; expose client transport ([#41](https://www.github.com/googleapis/python-scheduler/issues/41)) ([f9fc0f9](https://www.github.com/googleapis/python-scheduler/commit/f9fc0f9613302de642680c87286de0a02f09d086))

## [2.0.0](https://www.github.com/googleapis/python-scheduler/compare/v1.3.0...v2.0.0) (2020-08-27)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#29)

### Features

* migrate to microgenerator ([#29](https://www.github.com/googleapis/python-scheduler/issues/29)) ([82f66ed](https://www.github.com/googleapis/python-scheduler/commit/82f66ed9c163b2f6597bf5661469ca9ca1bef741))


### Bug Fixes

* update retry configs ([#20](https://www.github.com/googleapis/python-scheduler/issues/20)) ([7f82c9f](https://www.github.com/googleapis/python-scheduler/commit/7f82c9ffc292d72907de66bf6d5fa39e38d26085))

## [1.3.0](https://www.github.com/googleapis/python-scheduler/compare/v1.2.1...v1.3.0) (2020-04-21)


### ⚠ BREAKING CHANGES

* **scheduler:** remove `project_path` method, update docstrings (via synth) (#9522)

### Bug Fixes

* **scheduler:** remove `project_path` method, update docstrings (via synth) ([#9522](https://www.github.com/googleapis/python-scheduler/issues/9522)) ([36c611b](https://www.github.com/googleapis/python-scheduler/commit/36c611bdd1504918ecec39f7846c533b1e7b181c))
* add python 2.7 deprecation warning (via synth) ([#9](https://www.github.com/googleapis/python-scheduler/issues/9)) ([d17f5ff](https://www.github.com/googleapis/python-scheduler/commit/d17f5ffd8d6030190e3529d6eed5c9899145dd96))

## 1.2.1

08-12-2019 13:53 PDT

### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8966](https://github.com/googleapis/google-cloud-python/pull/8966))

### Documentation
- Fix links to googleapis.dev ([#8998](https://github.com/googleapis/google-cloud-python/pull/8998))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 1.2.0

07-24-2019 17:27 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth).  ([#8401](https://github.com/googleapis/google-cloud-python/pull/8401))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8520](https://github.com/googleapis/google-cloud-python/pull/8520))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Pin black version (via synth). ([#8593](https://github.com/googleapis/google-cloud-python/pull/8593))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

### Internal / Testing Changes
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8361](https://github.com/googleapis/google-cloud-python/pull/8361))
- Add disclaimer to auto-generated template (via synth). ([#8325](https://github.com/googleapis/google-cloud-python/pull/8325))
- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8250](https://github.com/googleapis/google-cloud-python/pull/8250))
- Fix coverage in 'types.py' (via synth). ([#8162](https://github.com/googleapis/google-cloud-python/pull/8162))
- Blacken noxfile.py, setup.py (via synth). ([#8130](https://github.com/googleapis/google-cloud-python/pull/8130))
- Add empty lines (via synth). ([#8069](https://github.com/googleapis/google-cloud-python/pull/8069))

## 1.1.0

05-13-2019 13:15 PDT

### New Features
- Add authorization headers and deadline for job attempts (via synth). ([#7938](https://github.com/googleapis/google-cloud-python/pull/7938))

### Internal / Testing Changes
- Add nox session `docs`, reorder methods (via synth). ([#7779](https://github.com/googleapis/google-cloud-python/pull/7779))

## 1.0.0

05-03-2019 10:04 PDT

### Internal / Testing Changes
- Add smoke test for scheduler. ([#7854](https://github.com/googleapis/google-cloud-python/pull/7854))

## 0.3.0

04-15-2019 10:32 PDT


### New Features
- add auth and configurable timeouts to v1beta1 (via synth). ([#7665](https://github.com/googleapis/google-cloud-python/pull/7665))

## 0.2.0

04-01-2019 15:39 PDT


### Implementation Changes
- Add routing header to method metadata (via synth). ([#7599](https://github.com/googleapis/google-cloud-python/pull/7599))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Remove unused message exports. ([#7273](https://github.com/googleapis/google-cloud-python/pull/7273))
- Protoc-generated serialization update. ([#7093](https://github.com/googleapis/google-cloud-python/pull/7093))
- Protoc-generated serialization update. ([#7055](https://github.com/googleapis/google-cloud-python/pull/7055))
- Use moved iam.policy now at google.api_core.iam.policy. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))

### New Features
- Add v1. ([#7608](https://github.com/googleapis/google-cloud-python/pull/7608))
- Pick up fixes to GAPIC generator. ([#6505](https://github.com/googleapis/google-cloud-python/pull/6505))

### Documentation
- googlecloudplatform --> googleapis in READMEs. ([#7411](https://github.com/googleapis/google-cloud-python/pull/7411))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Update copyright year. ([#7155](https://github.com/googleapis/google-cloud-python/pull/7155))
- Correct a link in a documentation string. ([#7119](https://github.com/googleapis/google-cloud-python/pull/7119))
- Pick up stub docstring fix in GAPIC generator. ([#6980](https://github.com/googleapis/google-cloud-python/pull/6980))
- Document Python 2 deprecation. ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Update link for Scheduler Docs. ([#6925](https://github.com/googleapis/google-cloud-python/pull/6925))

### Internal / Testing Changes
- Copy lintified proto files (via synth). ([#7469](https://github.com/googleapis/google-cloud-python/pull/7469))
- Add clarifying comment to blacken nox target. ([#7401](https://github.com/googleapis/google-cloud-python/pull/7401))
- Add protos as an artifact to library. ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Add baseline for synth.metadata. ([#6792](https://github.com/googleapis/google-cloud-python/pull/6865))
- Update noxfile. ([#6814](https://github.com/googleapis/google-cloud-python/pull/6814))
- Blacken all gen'd libs. ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps. ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py. ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries. ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))

## 0.1.0

11-13-2018 11:03 PST


### New Features
- Initial release of Cloud Scheduler library. ([#6482](https://github.com/googleapis/google-cloud-python/pull/6482))
