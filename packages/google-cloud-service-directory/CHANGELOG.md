# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-service-directory/#history

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.18.0...google-cloud-service-directory-v1.19.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.17.0...google-cloud-service-directory-v1.18.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.16.0...google-cloud-service-directory-v1.17.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.15.0...google-cloud-service-directory-v1.16.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.14.2...google-cloud-service-directory-v1.15.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.14.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.14.1...google-cloud-service-directory-v1.14.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.14.0...google-cloud-service-directory-v1.14.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([770cf0f](https://github.com/googleapis/google-cloud-python/commit/770cf0f31125586a8622e9639f6d24c1bafa9b31))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.13.0...google-cloud-service-directory-v1.14.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))
* Add support for reading selective GAPIC generation methods from service YAML ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.12.1...google-cloud-service-directory-v1.13.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.12.0...google-cloud-service-directory-v1.12.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13245](https://github.com/googleapis/google-cloud-python/issues/13245)) ([875f712](https://github.com/googleapis/google-cloud-python/commit/875f712265a36919409964f5ade218330f1d0147))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.6...google-cloud-service-directory-v1.12.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [1.11.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.5...google-cloud-service-directory-v1.11.6) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([42c4d04](https://github.com/googleapis/google-cloud-python/commit/42c4d04ee1362ba0ed0f1b6a134ac8e409875b63))

## [1.11.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.4...google-cloud-service-directory-v1.11.5) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [1.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.3...google-cloud-service-directory-v1.11.4) (2024-05-16)


### Documentation

* add maximum page_size to ListEndpoint API documentation ([f8ff81b](https://github.com/googleapis/google-cloud-python/commit/f8ff81ba1e57c7c974a40fcce2f6b61b1ca12e47))
* add maximum page_size to ListNamespace API documentation ([f8ff81b](https://github.com/googleapis/google-cloud-python/commit/f8ff81ba1e57c7c974a40fcce2f6b61b1ca12e47))
* add maximum page_size to ListService API documentation ([f8ff81b](https://github.com/googleapis/google-cloud-python/commit/f8ff81ba1e57c7c974a40fcce2f6b61b1ca12e47))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.2...google-cloud-service-directory-v1.11.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.1...google-cloud-service-directory-v1.11.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))
* fix ValueError in test__validate_universe_domain ([2451e88](https://github.com/googleapis/google-cloud-python/commit/2451e88f302bc582b3f6d01a6ec6aceba7646252))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.11.0...google-cloud-service-directory-v1.11.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.10.0...google-cloud-service-directory-v1.11.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.9.2...google-cloud-service-directory-v1.10.0) (2023-12-07)


### Features

* Add support for python 3.12 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Introduce compatibility with native namespace packages ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Use `retry_async` instead of `retry` in async client ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))

## [1.9.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.9.1...google-cloud-service-directory-v1.9.2) (2023-09-19)


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.9.0...google-cloud-service-directory-v1.9.1) (2023-08-03)


### Documentation

* Minor formatting ([#11543](https://github.com/googleapis/google-cloud-python/issues/11543)) ([8cc031e](https://github.com/googleapis/google-cloud-python/commit/8cc031e723350890b4ceb6e813f24c4bcde3d65f))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.8.2...google-cloud-service-directory-v1.9.0) (2023-07-24)


### Features

* added network and uid fields in Endpoint message ([4e7d204](https://github.com/googleapis/google-cloud-python/commit/4e7d204ac8f004749be9f61335ff7d66bcc41787))
* added uid field to Namespace message ([4e7d204](https://github.com/googleapis/google-cloud-python/commit/4e7d204ac8f004749be9f61335ff7d66bcc41787))
* added uid field to Service message ([4e7d204](https://github.com/googleapis/google-cloud-python/commit/4e7d204ac8f004749be9f61335ff7d66bcc41787))
* enable Location methods ([4e7d204](https://github.com/googleapis/google-cloud-python/commit/4e7d204ac8f004749be9f61335ff7d66bcc41787))


### Documentation

* updated docs for ListServicesRequest and ListEndpointsRequest message ([4e7d204](https://github.com/googleapis/google-cloud-python/commit/4e7d204ac8f004749be9f61335ff7d66bcc41787))
* updated docs for ResolveServiceRequest message ([4e7d204](https://github.com/googleapis/google-cloud-python/commit/4e7d204ac8f004749be9f61335ff7d66bcc41787))

## [1.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-service-directory-v1.8.1...google-cloud-service-directory-v1.8.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [1.8.1](https://github.com/googleapis/python-service-directory/compare/v1.8.0...v1.8.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#266](https://github.com/googleapis/python-service-directory/issues/266)) ([132ebdf](https://github.com/googleapis/python-service-directory/commit/132ebdfbc723cf48c3623d89ade48ce0c4f03666))

## [1.8.0](https://github.com/googleapis/python-service-directory/compare/v1.7.1...v1.8.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([d1506cb](https://github.com/googleapis/python-service-directory/commit/d1506cbd52a84ea1904320134b72b8a626d38aaa))

## [1.7.1](https://github.com/googleapis/python-service-directory/compare/v1.7.0...v1.7.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([#253](https://github.com/googleapis/python-service-directory/issues/253)) ([4e932f5](https://github.com/googleapis/python-service-directory/commit/4e932f5de09a5a73003aa3d76eae525901e573ed))

## [1.7.0](https://github.com/googleapis/python-service-directory/compare/v1.6.0...v1.7.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#251](https://github.com/googleapis/python-service-directory/issues/251)) ([1fadceb](https://github.com/googleapis/python-service-directory/commit/1fadceb23be6a328f090dc336d15b0ec7c3019c1))

## [1.6.0](https://github.com/googleapis/python-service-directory/compare/v1.5.3...v1.6.0) (2022-12-14)


### Features

* Add support for `google.cloud.servicedirectory.__version__` ([8e84d42](https://github.com/googleapis/python-service-directory/commit/8e84d42c42fb37d7b11eb17ee70619124f6cd338))
* Add typing to proto.Message based class attributes ([8e84d42](https://github.com/googleapis/python-service-directory/commit/8e84d42c42fb37d7b11eb17ee70619124f6cd338))


### Bug Fixes

* Add dict typing for client_options ([8e84d42](https://github.com/googleapis/python-service-directory/commit/8e84d42c42fb37d7b11eb17ee70619124f6cd338))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([9fae8c9](https://github.com/googleapis/python-service-directory/commit/9fae8c9648e09da82a80af7fe1a84fad6f8402ab))
* Drop usage of pkg_resources ([9fae8c9](https://github.com/googleapis/python-service-directory/commit/9fae8c9648e09da82a80af7fe1a84fad6f8402ab))
* Fix timeout default values ([9fae8c9](https://github.com/googleapis/python-service-directory/commit/9fae8c9648e09da82a80af7fe1a84fad6f8402ab))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([8e84d42](https://github.com/googleapis/python-service-directory/commit/8e84d42c42fb37d7b11eb17ee70619124f6cd338))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([9fae8c9](https://github.com/googleapis/python-service-directory/commit/9fae8c9648e09da82a80af7fe1a84fad6f8402ab))

## [1.5.3](https://github.com/googleapis/python-service-directory/compare/v1.5.2...v1.5.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#239](https://github.com/googleapis/python-service-directory/issues/239)) ([9406ff6](https://github.com/googleapis/python-service-directory/commit/9406ff66562481d656cd36d68ef5b937e742ec22))

## [1.5.2](https://github.com/googleapis/python-service-directory/compare/v1.5.1...v1.5.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#237](https://github.com/googleapis/python-service-directory/issues/237)) ([bd8c9dd](https://github.com/googleapis/python-service-directory/commit/bd8c9dd649a70c2c233c7077546f0ca5fc372b91))

## [1.5.1](https://github.com/googleapis/python-service-directory/compare/v1.5.0...v1.5.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#222](https://github.com/googleapis/python-service-directory/issues/222)) ([39e40a9](https://github.com/googleapis/python-service-directory/commit/39e40a96d6df2df7d97a63085d69cd8e827f1691))
* **deps:** require proto-plus >= 1.22.0 ([39e40a9](https://github.com/googleapis/python-service-directory/commit/39e40a96d6df2df7d97a63085d69cd8e827f1691))

## [1.5.0](https://github.com/googleapis/python-service-directory/compare/v1.4.1...v1.5.0) (2022-07-16)


### Features

* add audience parameter ([edb9d42](https://github.com/googleapis/python-service-directory/commit/edb9d424ed3054d54a1aaf72cb072a5acb0d1892))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#217](https://github.com/googleapis/python-service-directory/issues/217)) ([b8c81db](https://github.com/googleapis/python-service-directory/commit/b8c81dbe400fefc3ba64da02c170a760df2d08ab))
* require python 3.7+ ([#215](https://github.com/googleapis/python-service-directory/issues/215)) ([d7a5808](https://github.com/googleapis/python-service-directory/commit/d7a580829538f2a820d6c0069fc838975569423d))

## [1.4.1](https://github.com/googleapis/python-service-directory/compare/v1.4.0...v1.4.1) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#205](https://github.com/googleapis/python-service-directory/issues/205)) ([b693784](https://github.com/googleapis/python-service-directory/commit/b6937849043941bf5238e5101f2935a27660e872))


### Documentation

* fix changelog header to consistent size ([#206](https://github.com/googleapis/python-service-directory/issues/206)) ([73bd664](https://github.com/googleapis/python-service-directory/commit/73bd664112df42552cf125c35752001e0a395528))

## [1.4.0](https://github.com/googleapis/python-service-directory/compare/v1.3.1...v1.4.0) (2022-05-05)


### Features

* AuditConfig for IAM v1 ([ab48a2a](https://github.com/googleapis/python-service-directory/commit/ab48a2a2f2dddfaf9bc18b53f99b379ad66098d2))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([ab48a2a](https://github.com/googleapis/python-service-directory/commit/ab48a2a2f2dddfaf9bc18b53f99b379ad66098d2))


### Documentation

* fix type in docstring for map fields ([ab48a2a](https://github.com/googleapis/python-service-directory/commit/ab48a2a2f2dddfaf9bc18b53f99b379ad66098d2))

## [1.3.1](https://github.com/googleapis/python-service-directory/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#162](https://github.com/googleapis/python-service-directory/issues/162)) ([8cf5f69](https://github.com/googleapis/python-service-directory/commit/8cf5f6950ccb302aac014a539855206403a50baf))
* **deps:** require proto-plus>=1.15.0 ([8cf5f69](https://github.com/googleapis/python-service-directory/commit/8cf5f6950ccb302aac014a539855206403a50baf))

## [1.3.0](https://github.com/googleapis/python-service-directory/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#148](https://github.com/googleapis/python-service-directory/issues/148)) ([a562a5d](https://github.com/googleapis/python-service-directory/commit/a562a5d8f530b41078062612b9916bc76882f211))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([55c52b5](https://github.com/googleapis/python-service-directory/commit/55c52b5b67891ac723a34fae22040feb5b5fcf15))

## [1.2.1](https://www.github.com/googleapis/python-service-directory/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([809bcd7](https://www.github.com/googleapis/python-service-directory/commit/809bcd7ee993eba50cb3be1cf70658beb008db5b))
* **deps:** require google-api-core >= 1.28.0 ([809bcd7](https://www.github.com/googleapis/python-service-directory/commit/809bcd7ee993eba50cb3be1cf70658beb008db5b))


### Documentation

* list oneofs in docstring ([809bcd7](https://www.github.com/googleapis/python-service-directory/commit/809bcd7ee993eba50cb3be1cf70658beb008db5b))

## [1.2.0](https://www.github.com/googleapis/python-service-directory/compare/v1.1.0...v1.2.0) (2021-10-20)


### Features

* add support for python 3.10 ([#126](https://www.github.com/googleapis/python-service-directory/issues/126)) ([3d3847c](https://www.github.com/googleapis/python-service-directory/commit/3d3847cd14542934a4b992ab789bbc5f1bffe2ef))


### Documentation

* fix docstring formatting ([#130](https://www.github.com/googleapis/python-service-directory/issues/130)) ([a440a30](https://www.github.com/googleapis/python-service-directory/commit/a440a307044cb58c301111df7491ce59778abaac))

## [1.1.0](https://www.github.com/googleapis/python-service-directory/compare/v1.0.4...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#122](https://www.github.com/googleapis/python-service-directory/issues/122)) ([59229eb](https://www.github.com/googleapis/python-service-directory/commit/59229ebe9f17be35cb39119cbae2e19e7a4c8732))

## [1.0.4](https://www.github.com/googleapis/python-service-directory/compare/v1.0.3...v1.0.4) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([1b0841d](https://www.github.com/googleapis/python-service-directory/commit/1b0841dec49d193c777601ff16ee0706395349b3))

## [1.0.3](https://www.github.com/googleapis/python-service-directory/compare/v1.0.2...v1.0.3) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([b1982e1](https://www.github.com/googleapis/python-service-directory/commit/b1982e1e3d9214c93b59dbbb1f9ff00532fc6120))

## [1.0.2](https://www.github.com/googleapis/python-service-directory/compare/v1.0.1...v1.0.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#101](https://www.github.com/googleapis/python-service-directory/issues/101)) ([b81c721](https://www.github.com/googleapis/python-service-directory/commit/b81c721ccebd363b078f4c6acbe6deef6a70ff7e))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#97](https://www.github.com/googleapis/python-service-directory/issues/97)) ([195861c](https://www.github.com/googleapis/python-service-directory/commit/195861c821be6a3ba853074d07a609ef67a48bcf))


### Miscellaneous Chores

* release as 1.0.2 ([#102](https://www.github.com/googleapis/python-service-directory/issues/102)) ([47caf13](https://www.github.com/googleapis/python-service-directory/commit/47caf1346029bc6d017a1498f3a9b97e396ef667))

## [1.0.1](https://www.github.com/googleapis/python-service-directory/compare/v1.0.0...v1.0.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#96](https://www.github.com/googleapis/python-service-directory/issues/96)) ([ec30558](https://www.github.com/googleapis/python-service-directory/commit/ec30558ee8b89b951509e3f7b9cea6f548b69fe6))

## [1.0.0](https://www.github.com/googleapis/python-service-directory/compare/v0.5.0...v1.0.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#87](https://www.github.com/googleapis/python-service-directory/issues/87)) ([6104fe4](https://www.github.com/googleapis/python-service-directory/commit/6104fe4e8ee660031562291ac216d6376b33cb73))
* bump release level to production/stable ([#77](https://www.github.com/googleapis/python-service-directory/issues/77)) ([b267e2f](https://www.github.com/googleapis/python-service-directory/commit/b267e2f326b5247c84800c8f23e47b53540b663a))
* support self-signed JWT flow for service accounts ([a0387dd](https://www.github.com/googleapis/python-service-directory/commit/a0387dd9d4fd8303e96f2d028b5c450546e26ec0))
* Update Service Directory v1beta1 protos to include VPC Network field, and create/modify timestamp fields. ([#88](https://www.github.com/googleapis/python-service-directory/issues/88)) ([e7fba11](https://www.github.com/googleapis/python-service-directory/commit/e7fba11e53b85ff25620ba92e8859206fd7884d8))


### Bug Fixes

* add async client to %name_%version/init.py ([a0387dd](https://www.github.com/googleapis/python-service-directory/commit/a0387dd9d4fd8303e96f2d028b5c450546e26ec0))
* disable always_use_jwt_access ([1df4a39](https://www.github.com/googleapis/python-service-directory/commit/1df4a3918f59264f1b3b3041ae7c8a51460ed80f))
* disable always_use_jwt_access ([#91](https://www.github.com/googleapis/python-service-directory/issues/91)) ([1df4a39](https://www.github.com/googleapis/python-service-directory/commit/1df4a3918f59264f1b3b3041ae7c8a51460ed80f))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-service-directory/issues/1127)) ([#84](https://www.github.com/googleapis/python-service-directory/issues/84)) ([d9c20bb](https://www.github.com/googleapis/python-service-directory/commit/d9c20bb7dc9f393d0383e69367f5e1ec703ac416))


### Miscellaneous Chores

* release as 1.0.0 ([#82](https://www.github.com/googleapis/python-service-directory/issues/82)) ([a3eaeff](https://www.github.com/googleapis/python-service-directory/commit/a3eaeff0750200a53969c2be0b2d41129e8c194a))

## [0.5.0](https://www.github.com/googleapis/python-service-directory/compare/v0.4.1...v0.5.0) (2021-03-31)


### Features

* add `from_service_account_info` ([#45](https://www.github.com/googleapis/python-service-directory/issues/45)) ([db77e88](https://www.github.com/googleapis/python-service-directory/commit/db77e88a44ffdabd284d61775960079309071617))

## [0.4.1](https://www.github.com/googleapis/python-service-directory/compare/v0.4.0...v0.4.1) (2021-02-11)


### Bug Fixes

* remove gRPC send/recv limits ([#39](https://www.github.com/googleapis/python-service-directory/issues/39)) ([07908c0](https://www.github.com/googleapis/python-service-directory/commit/07908c009307485955886fc042c1c2b18b43adbd))

## [0.4.0](https://www.github.com/googleapis/python-service-directory/compare/v0.3.0...v0.4.0) (2020-12-03)


### Features

* add v1; add async client ([#30](https://www.github.com/googleapis/python-service-directory/issues/30)) ([7a771b1](https://www.github.com/googleapis/python-service-directory/commit/7a771b12d61e47e1cd341f3bd2d2fc8d221e07c0))

## [0.3.0](https://www.github.com/googleapis/python-service-directory/compare/v0.2.0...v0.3.0) (2020-06-11)


### Features

* add mTLS support, fix missing routing header issue  ([#15](https://www.github.com/googleapis/python-service-directory/issues/15)) ([b983735](https://www.github.com/googleapis/python-service-directory/commit/b98373544181ecc55104230fc1e53b206c2e23ac))

## [0.2.0](https://www.github.com/googleapis/python-service-directory/compare/v0.1.1...v0.2.0) (2020-05-19)


### Features

* add mTLS support (via synth) ([#4](https://www.github.com/googleapis/python-service-directory/issues/4)) ([25e0fcf](https://www.github.com/googleapis/python-service-directory/commit/25e0fcfb32d100be0cba3799d62543569dd2d2c6))


### Bug Fixes

* fix docs link ([#9](https://www.github.com/googleapis/python-service-directory/issues/9)) ([0f73da9](https://www.github.com/googleapis/python-service-directory/commit/0f73da9722e3e0c943b67063af4a7f9d0fc1f9e4))

## [0.1.1](https://www.github.com/googleapis/python-service-directory/compare/v0.1.0...v0.1.1) (2020-04-17)


### Bug Fixes

* fix link to client library documentation ([#3](https://www.github.com/googleapis/python-service-directory/issues/3)) ([8e9e602](https://www.github.com/googleapis/python-service-directory/commit/8e9e6020ffdeb2e012ef93fb466658da9fbac8df))

## 0.1.0 (2020-03-13)


### Features

* generate v1beta1 ([c2b8b99](https://www.github.com/googleapis/python-service-directory/commit/c2b8b99579a866ec7701e8ed95e6d05069593fb0))
