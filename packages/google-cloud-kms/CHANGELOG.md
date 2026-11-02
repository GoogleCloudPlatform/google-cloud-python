# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-kms/#history

## [3.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.17.0...google-cloud-kms-v3.18.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [3.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.16.0...google-cloud-kms-v3.17.0) (2026-09-17)


### Features

* update API sources and regenerate ([#18396](https://github.com/googleapis/google-cloud-python/issues/18396)) ([e9f8e59](https://github.com/googleapis/google-cloud-python/commit/e9f8e590b7b395e660cc5437535166dfb920d246))
* update API sources and regenerate. ([e9f8e59](https://github.com/googleapis/google-cloud-python/commit/e9f8e590b7b395e660cc5437535166dfb920d246))

## [3.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.15.0...google-cloud-kms-v3.16.0) (2026-07-16)


### Features

* update googleapis and regenerate ([#17725](https://github.com/googleapis/google-cloud-python/issues/17725)) ([35e16da](https://github.com/googleapis/google-cloud-python/commit/35e16daf25480d66e9fc3443fe485ae2b0241ae3))

## [3.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.14.0...google-cloud-kms-v3.15.0) (2026-07-07)


### Features

* update googleapis and regenerate ([#17635](https://github.com/googleapis/google-cloud-python/issues/17635)) ([9638879](https://github.com/googleapis/google-cloud-python/commit/96388796440b226440f885c04ce565782b1d9190))

## [3.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.13.0...google-cloud-kms-v3.14.0) (2026-06-22)


### Features

* regenerate google-cloud-[k-n] packages ([#17074](https://github.com/googleapis/google-cloud-python/issues/17074)) ([ec54f78](https://github.com/googleapis/google-cloud-python/commit/ec54f78e37bb3b48e0794d544784b99fa13d6f85))

## [3.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.12.0...google-cloud-kms-v3.13.0) (2026-05-06)

## [3.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.11.0...google-cloud-kms-v3.12.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [3.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.10.0...google-cloud-kms-v3.11.0) (2026-02-19)


### Documentation

* Update documentation for AutokeyAdmin service and messages to support folder and project-level configurations ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))
* Clarify supported resources for the crypto_key_backend field in ImportJob ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))


### Features

* Add KeyProjectResolutionMode to AutokeyConfig to support project-level configurations ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))
* Add more post-quantum (PQ) signature algorithms to CryptoKeyVersion ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))
* Added DeleteCryptoKey and DeleteCryptoKeyVersion RPCs to permanently remove resources ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))
* Added ListRetiredResources and GetRetiredResource RPCs to manage and view these records ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))
* Introduced the RetiredResource resource to track records of deleted keys and prevent the reuse of their resource names ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))

## [3.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.9.0...google-cloud-kms-v3.10.0) (2026-01-22)


### Documentation

* A comment for field `crypto_key_backend` in message `.google.cloud.kms.v1.CryptoKey` is expanded to include SingleTenantHsmInstances ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))
* A comment for enum value `MODIFIED_GOOGLE_INITIATED_SYSTEM_OPERATION` in enum `AccessReason` is changed ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))
* A comment for enum value `MODIFIED_CUSTOMER_INITIATED_ACCESS` in enum `AccessReason` is changed ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))


### Features

* add the SingleTenantHsm functionality including the management API and resource types ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))

## [3.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.8.0...google-cloud-kms-v3.9.0) (2026-01-15)


### Documentation

* Marking MODIFIED_CUSTOMER_INITIATED_ACCESS and MODIFIED_GOOGLE_INITIATED_SYSTEM_OPERATION Key Access Justification codes as deprecated in favor of GOOGLE_RESPONSE_TO_PRODUCTION_ALERT ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))

## [3.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.7.0...google-cloud-kms-v3.8.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [3.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.6.0...google-cloud-kms-v3.7.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [3.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.5.1...google-cloud-kms-v3.6.0) (2025-09-22)


### Features

* Add PublicKeyFormat enums XWING_RAW_BYTES (used for KEM_XWING) and DER ([186cef2](https://github.com/googleapis/google-cloud-python/commit/186cef27be0e3b6669ed86d7ce064b90bfd545dc))
* Support KEY_ENCAPSULATION purpose and quantum-safe algorithms ML_KEM_768, ML_KEM_1024 and KEM_XWING ([186cef2](https://github.com/googleapis/google-cloud-python/commit/186cef27be0e3b6669ed86d7ce064b90bfd545dc))

## [3.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.5.0...google-cloud-kms-v3.5.1) (2025-05-20)


### Documentation

* [google-cloud-kms] A comment for enum value `DESTROYED` in enum `CryptoKeyVersionState` is changed ([#13913](https://github.com/googleapis/google-cloud-python/issues/13913)) ([cdca657](https://github.com/googleapis/google-cloud-python/commit/cdca65752c8ae2289c09f0320e39b66826725417))

## [3.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.4.1...google-cloud-kms-v3.5.0) (2025-05-15)


### Features

* Adding eTag field to AutokeyConfig ([5d7b972](https://github.com/googleapis/google-cloud-python/commit/5d7b9728009f7ef561d65d70a8b712400b509d34))


### Documentation

* Updating docs for total_size field in KMS List APIs ([5d7b972](https://github.com/googleapis/google-cloud-python/commit/5d7b9728009f7ef561d65d70a8b712400b509d34))

## [3.4.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.4.0...google-cloud-kms-v3.4.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [3.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.3.1...google-cloud-kms-v3.4.0) (2025-02-24)


### Features

* [google-cloud-kms] Support PQC asymmetric signing algorithms ML_DSA_65 and SLH_DSA_SHA2_128s ([#13538](https://github.com/googleapis/google-cloud-python/issues/13538)) ([891365e](https://github.com/googleapis/google-cloud-python/commit/891365e3030506c1205a56919d1b1e25e0cd926e))
* Add a PublicKeyFormat enum to allow specifying the format the ([891365e](https://github.com/googleapis/google-cloud-python/commit/891365e3030506c1205a56919d1b1e25e0cd926e))

## [3.3.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.3.0...google-cloud-kms-v3.3.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([16e14c8](https://github.com/googleapis/google-cloud-python/commit/16e14c8d547864360dcab45d90e9e55169204fc6))

## [3.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.2.2...google-cloud-kms-v3.3.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [3.2.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.2.1...google-cloud-kms-v3.2.2) (2025-01-13)


### Documentation

* [google-cloud-kms] modify enum comment ([#13410](https://github.com/googleapis/google-cloud-python/issues/13410)) ([129140e](https://github.com/googleapis/google-cloud-python/commit/129140eeb51c96459b22d9e8fedb26a432d36ff6))

## [3.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.2.0...google-cloud-kms-v3.2.1) (2024-12-18)


### Documentation

* [google-cloud-kms] code documentation improvements ([#13366](https://github.com/googleapis/google-cloud-python/issues/13366)) ([0c0f37d](https://github.com/googleapis/google-cloud-python/commit/0c0f37d415a844d29d97a5dba59258d181c8bcc3))

## [3.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.1.1...google-cloud-kms-v3.2.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))


### Documentation

* [google-cloud-kms] A comment for enum `CryptoKeyVersionAlgorithm` is changed ([#13305](https://github.com/googleapis/google-cloud-python/issues/13305)) ([028a334](https://github.com/googleapis/google-cloud-python/commit/028a334c383892e50003a8735a050dbabfabdcfc))

## [3.1.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.1.0...google-cloud-kms-v3.1.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [3.1.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v3.0.0...google-cloud-kms-v3.1.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13207](https://github.com/googleapis/google-cloud-python/issues/13207)) ([ceb9be8](https://github.com/googleapis/google-cloud-python/commit/ceb9be8f89ac7355d842bac1d77b2926eb0b649c))

## [3.0.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.24.2...google-cloud-kms-v3.0.0) (2024-09-23)


### ⚠ BREAKING CHANGES

* Pagination feature is introduced for method ListKeyHandles in service Autokey

### Features

* Adding a state field for AutokeyConfig ([b4c9770](https://github.com/googleapis/google-cloud-python/commit/b4c977059e075c73781c179b26fdf915548e65c4))


### Bug Fixes

* Pagination feature is introduced for method ListKeyHandles in service Autokey ([b4c9770](https://github.com/googleapis/google-cloud-python/commit/b4c977059e075c73781c179b26fdf915548e65c4))


### Documentation

* A comment for field destroy_scheduled_duration in message .google.cloud.kms.v1.CryptoKey is updated for the default duration ([b4c9770](https://github.com/googleapis/google-cloud-python/commit/b4c977059e075c73781c179b26fdf915548e65c4))
* Field service_resolvers in message .google.cloud.kms.v1.EkmConnection is Explicitly is marked as to have field behavior of Optional ([b4c9770](https://github.com/googleapis/google-cloud-python/commit/b4c977059e075c73781c179b26fdf915548e65c4))

## [2.24.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.24.1...google-cloud-kms-v2.24.2) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [2.24.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.24.0...google-cloud-kms-v2.24.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12867](https://github.com/googleapis/google-cloud-python/issues/12867)) ([3362176](https://github.com/googleapis/google-cloud-python/commit/33621762b989106ccf85adb538cf531c513a746c))

## [2.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.23.0...google-cloud-kms-v2.24.0) (2024-06-24)


### Features

* support Key Access Justifications policy configuration ([6945437](https://github.com/googleapis/google-cloud-python/commit/69454372b112a4fc08cd6ff1fcd0583333b22eef))

## [2.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.22.0...google-cloud-kms-v2.23.0) (2024-05-16)


### Features

* add client library for KMS Autokey service, which enables automated KMS key provision and management ([b74c6c2](https://github.com/googleapis/google-cloud-python/commit/b74c6c26225d3bb2703cf6421f047372df59eaa8))

## [2.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.21.4...google-cloud-kms-v2.22.0) (2024-05-07)


### Features

* introduce Long-Running Operations (LRO) for KMS ([18b3c0d](https://github.com/googleapis/google-cloud-python/commit/18b3c0d8ee3c27728648fbd8144134cd7dcebd4f))

## [2.21.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.21.3...google-cloud-kms-v2.21.4) (2024-04-17)


### Documentation

* [google-cloud-kms] in google.cloud.kms.v1.PublicKey, pem field is always populated ([#12584](https://github.com/googleapis/google-cloud-python/issues/12584)) ([1392da5](https://github.com/googleapis/google-cloud-python/commit/1392da5054e922446a51b7302596ba3809896bf3))

## [2.21.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.21.2...google-cloud-kms-v2.21.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12385](https://github.com/googleapis/google-cloud-python/issues/12385)) ([d50f4d0](https://github.com/googleapis/google-cloud-python/commit/d50f4d042774e2f12e9fe03459eae9ce91247df3))

## [2.21.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.21.1...google-cloud-kms-v2.21.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12307](https://github.com/googleapis/google-cloud-python/issues/12307)) ([be87bc4](https://github.com/googleapis/google-cloud-python/commit/be87bc4a33fe32a512448a42246c9873da88269f))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [2.21.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.21.0...google-cloud-kms-v2.21.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))

## [2.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.20.0...google-cloud-kms-v2.21.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12241](https://github.com/googleapis/google-cloud-python/issues/12241)) ([aae72f5](https://github.com/googleapis/google-cloud-python/commit/aae72f5e6c7d48e777fdf68d1012b2b51b912bad))


### Documentation

* [google-cloud-kms] update comments ([#12232](https://github.com/googleapis/google-cloud-python/issues/12232)) ([7caca2e](https://github.com/googleapis/google-cloud-python/commit/7caca2e52c8568d020e0bd56eefe32ff824be722))

## [2.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-kms-v2.19.2...google-cloud-kms-v2.20.0) (2023-12-07)


### Features

* Add support for python 3.12 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Introduce compatibility with native namespace packages ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Use `retry_async` instead of `retry` in async client ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))

## [2.19.2](https://github.com/googleapis/python-kms/compare/v2.19.1...v2.19.2) (2023-10-09)


### Documentation

* Minor formatting ([#416](https://github.com/googleapis/python-kms/issues/416)) ([0a09d11](https://github.com/googleapis/python-kms/commit/0a09d118e680e4d90df6df65548bc5740952df2d))

## [2.19.1](https://github.com/googleapis/python-kms/compare/v2.19.0...v2.19.1) (2023-08-02)


### Documentation

* Minor formatting ([#411](https://github.com/googleapis/python-kms/issues/411)) ([ea4717c](https://github.com/googleapis/python-kms/commit/ea4717c2a89d90c23146b5a769cb07389e7d3872))

## [2.19.0](https://github.com/googleapis/python-kms/compare/v2.18.0...v2.19.0) (2023-07-21)


### Features

* Add interoperable symmetric encryption system ([#403](https://github.com/googleapis/python-kms/issues/403)) ([39ad43d](https://github.com/googleapis/python-kms/commit/39ad43dcfbc09265087ea8b7b55117b3d2b1b99c))

## [2.18.0](https://github.com/googleapis/python-kms/compare/v2.17.0...v2.18.0) (2023-07-04)


### Features

* Add interoperable symmetric encryption system ([#396](https://github.com/googleapis/python-kms/issues/396)) ([57141c2](https://github.com/googleapis/python-kms/commit/57141c20066600e7203bb7c2035800fe3c9dc2c7))


### Bug Fixes

* Add async context manager return types ([#398](https://github.com/googleapis/python-kms/issues/398)) ([cb7c193](https://github.com/googleapis/python-kms/commit/cb7c1930c9749d967556ec79ccdef3ae6fb8296d))

## [2.17.0](https://github.com/googleapis/python-kms/compare/v2.16.1...v2.17.0) (2023-05-12)


### Features

* Added VerifyConnectivity RPC ([#388](https://github.com/googleapis/python-kms/issues/388)) ([b265bd7](https://github.com/googleapis/python-kms/commit/b265bd79502619a86ec179e19495df0b377b992b))

## [2.16.1](https://github.com/googleapis/python-kms/compare/v2.16.0...v2.16.1) (2023-03-28)


### Documentation

* Publish the API comment changes related to supporting different hash functions/values for ECDSA signing ([#386](https://github.com/googleapis/python-kms/issues/386)) ([c45e891](https://github.com/googleapis/python-kms/commit/c45e8914fe198abf5767727103fb1832cca645dc))

## [2.16.0](https://github.com/googleapis/python-kms/compare/v2.15.0...v2.16.0) (2023-03-23)


### Features

* Add support for Coordinated External Keys ([#382](https://github.com/googleapis/python-kms/issues/382)) ([3f68192](https://github.com/googleapis/python-kms/commit/3f681923dee66e30eed91bf5a19485dea19e524e))


### Documentation

* Fix formatting of request arg in docstring ([#385](https://github.com/googleapis/python-kms/issues/385)) ([94d33c2](https://github.com/googleapis/python-kms/commit/94d33c206d7a06265933359074b61aab94f6be8e))

## [2.15.0](https://github.com/googleapis/python-kms/compare/v2.14.1...v2.15.0) (2023-02-21)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#377](https://github.com/googleapis/python-kms/issues/377)) ([ae74545](https://github.com/googleapis/python-kms/commit/ae745452faea7f02ac7c4c0264b24dec2be787ee))

## [2.14.1](https://github.com/googleapis/python-kms/compare/v2.14.0...v2.14.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([8137467](https://github.com/googleapis/python-kms/commit/81374671d9cf5b88c35555b089b2abd8d2e613a0))


### Documentation

* Add documentation for enums ([8137467](https://github.com/googleapis/python-kms/commit/81374671d9cf5b88c35555b089b2abd8d2e613a0))

## [2.14.0](https://github.com/googleapis/python-kms/compare/v2.13.0...v2.14.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#368](https://github.com/googleapis/python-kms/issues/368)) ([753aff8](https://github.com/googleapis/python-kms/commit/753aff8ee7747372e2b1d4170f436ab367eefc2a))

## [2.13.0](https://github.com/googleapis/python-kms/compare/v2.12.3...v2.13.0) (2022-12-14)


### Features

* Add SHA-2 import methods ([6311278](https://github.com/googleapis/python-kms/commit/6311278a4aa3413751ba789cde6e6741a69b7791))
* Add support for `google.cloud.kms.__version__` ([6311278](https://github.com/googleapis/python-kms/commit/6311278a4aa3413751ba789cde6e6741a69b7791))
* Add support for additional HMAC algorithms ([6311278](https://github.com/googleapis/python-kms/commit/6311278a4aa3413751ba789cde6e6741a69b7791))
* Add typing to proto.Message based class attributes ([6311278](https://github.com/googleapis/python-kms/commit/6311278a4aa3413751ba789cde6e6741a69b7791))


### Bug Fixes

* Add dict typing for client_options ([6311278](https://github.com/googleapis/python-kms/commit/6311278a4aa3413751ba789cde6e6741a69b7791))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([dbe2f96](https://github.com/googleapis/python-kms/commit/dbe2f9697ec5183302c7c870d30165f0b436df20))
* Drop usage of pkg_resources ([dbe2f96](https://github.com/googleapis/python-kms/commit/dbe2f9697ec5183302c7c870d30165f0b436df20))
* Fix timeout default values ([dbe2f96](https://github.com/googleapis/python-kms/commit/dbe2f9697ec5183302c7c870d30165f0b436df20))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([6311278](https://github.com/googleapis/python-kms/commit/6311278a4aa3413751ba789cde6e6741a69b7791))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([dbe2f96](https://github.com/googleapis/python-kms/commit/dbe2f9697ec5183302c7c870d30165f0b436df20))

## [2.12.3](https://github.com/googleapis/python-kms/compare/v2.12.2...v2.12.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#350](https://github.com/googleapis/python-kms/issues/350)) ([cfdad0a](https://github.com/googleapis/python-kms/commit/cfdad0ac9cdacb174595dcce89e8ad160d42b009))

## [2.12.2](https://github.com/googleapis/python-kms/compare/v2.12.1...v2.12.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#347](https://github.com/googleapis/python-kms/issues/347)) ([9287a76](https://github.com/googleapis/python-kms/commit/9287a76ec0632caff5b2de429fffadf5ded4e348))

## [2.12.1](https://github.com/googleapis/python-kms/compare/v2.12.0...v2.12.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#322](https://github.com/googleapis/python-kms/issues/322)) ([229e0f5](https://github.com/googleapis/python-kms/commit/229e0f5825732b41d0fcbae7208065465b4ac200))
* **deps:** require proto-plus >= 1.22.0 ([229e0f5](https://github.com/googleapis/python-kms/commit/229e0f5825732b41d0fcbae7208065465b4ac200))

## [2.12.0](https://github.com/googleapis/python-kms/compare/v2.11.2...v2.12.0) (2022-07-14)


### Features

* add audience parameter ([06a4096](https://github.com/googleapis/python-kms/commit/06a4096a61c8b2ed14ccbf88f386203e2c8dc54e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#315](https://github.com/googleapis/python-kms/issues/315)) ([82ab556](https://github.com/googleapis/python-kms/commit/82ab556b8aec33d75e99c151f01b7e2c4aa6a719))
* require python 3.7+ ([#313](https://github.com/googleapis/python-kms/issues/313)) ([28d244f](https://github.com/googleapis/python-kms/commit/28d244f1347337f9294a9c3445df426c28b7d1d3))

## [2.11.2](https://github.com/googleapis/python-kms/compare/v2.11.1...v2.11.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#299](https://github.com/googleapis/python-kms/issues/299)) ([45b97e8](https://github.com/googleapis/python-kms/commit/45b97e8cd0443c090c28b348af1e3ccddf2dbf29))


### Documentation

* fix changelog header to consistent size ([#298](https://github.com/googleapis/python-kms/issues/298)) ([d3f7a5b](https://github.com/googleapis/python-kms/commit/d3f7a5b9abe6828f84d45df570845d3be16f5411))

## [2.11.1](https://github.com/googleapis/python-kms/compare/v2.11.0...v2.11.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#247](https://github.com/googleapis/python-kms/issues/247)) ([ef54503](https://github.com/googleapis/python-kms/commit/ef54503efc02d178e1294f3550693208082d256f))
* **deps:** require proto-plus>=1.15.0 ([ef54503](https://github.com/googleapis/python-kms/commit/ef54503efc02d178e1294f3550693208082d256f))


### Documentation

* add generated snippets ([#236](https://github.com/googleapis/python-kms/issues/236)) ([314485f](https://github.com/googleapis/python-kms/commit/314485f55904eb9e914380b627d3a80fc65712b3))
* **samples:** updated var name to avoid shadowing built-in ([#238](https://github.com/googleapis/python-kms/issues/238)) ([5bbf2c3](https://github.com/googleapis/python-kms/commit/5bbf2c36b99c5f547cda5806f803d06cef17c627))

## [2.11.0](https://github.com/googleapis/python-kms/compare/v2.10.1...v2.11.0) (2022-02-03)


### Features

* add a new EkmService API ([#233](https://github.com/googleapis/python-kms/issues/233)) ([eb532f5](https://github.com/googleapis/python-kms/commit/eb532f5c84907c12356e549c694c0210e5ad585b))
* add api key support ([#230](https://github.com/googleapis/python-kms/issues/230)) ([fdf62ae](https://github.com/googleapis/python-kms/commit/fdf62ae3b3209a1215e0f2f2440add1f01d40907))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([97f7ea5](https://github.com/googleapis/python-kms/commit/97f7ea50a30d1dc1133d7703e6bd90ad209f75a1))


### Documentation

* **samples:** fix typo in verify_asymmetric_ec.py ([#227](https://github.com/googleapis/python-kms/issues/227)) ([3817d73](https://github.com/googleapis/python-kms/commit/3817d7390fddebd137c99865455f0ae145dbcf63))

## [2.10.1](https://www.github.com/googleapis/python-kms/compare/v2.10.0...v2.10.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([6d7b8c1](https://www.github.com/googleapis/python-kms/commit/6d7b8c1043e59f3749c58b032f3fe800293c03f5))
* **deps:** require google-api-core >= 1.28.0 ([6d7b8c1](https://www.github.com/googleapis/python-kms/commit/6d7b8c1043e59f3749c58b032f3fe800293c03f5))


### Documentation

* list oneofs in docstring ([6d7b8c1](https://www.github.com/googleapis/python-kms/commit/6d7b8c1043e59f3749c58b032f3fe800293c03f5))

## [2.10.0](https://www.github.com/googleapis/python-kms/compare/v2.9.0...v2.10.0) (2021-10-18)


### Features

* add support for Raw PKCS[#1](https://www.github.com/googleapis/python-kms/issues/1) signing keys ([#195](https://www.github.com/googleapis/python-kms/issues/195)) ([9c4f997](https://www.github.com/googleapis/python-kms/commit/9c4f997d09e9a83141eda767cd2bb63a0bf58a37))

## [2.9.0](https://www.github.com/googleapis/python-kms/compare/v2.8.0...v2.9.0) (2021-10-08)


### Features

* add context manager support in client ([#190](https://www.github.com/googleapis/python-kms/issues/190)) ([6707e79](https://www.github.com/googleapis/python-kms/commit/6707e7950f9ebcedaa22d2e1d12aa0af6e35581d))

## [2.8.0](https://www.github.com/googleapis/python-kms/compare/v2.7.0...v2.8.0) (2021-09-30)


### Features

* add RPC retry information for MacSign, MacVerify, and GenerateRandomBytes ([#186](https://www.github.com/googleapis/python-kms/issues/186)) ([62591c8](https://www.github.com/googleapis/python-kms/commit/62591c8ead85c33fa5a5c4cc7c2a26779cbd1075))

## [2.7.0](https://www.github.com/googleapis/python-kms/compare/v2.6.1...v2.7.0) (2021-09-30)


### Features

* add OAEP+SHA1 to the list of supported algorithms ([#181](https://www.github.com/googleapis/python-kms/issues/181)) ([65b2c97](https://www.github.com/googleapis/python-kms/commit/65b2c975d2635cd562a0e4b7ff8f1989643929ee))


### Bug Fixes

* improper types in pagers generation ([8ff7501](https://www.github.com/googleapis/python-kms/commit/8ff75018aeacd87bd00abb4a12a130f3e28604f5))

## [2.6.1](https://www.github.com/googleapis/python-kms/compare/v2.6.0...v2.6.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([728e5e0](https://www.github.com/googleapis/python-kms/commit/728e5e08738e4954c3f1f9eecda5c1d1753501c3))

## [2.6.0](https://www.github.com/googleapis/python-kms/compare/v2.5.0...v2.6.0) (2021-08-30)


### Features

* add support for Key Reimport ([#167](https://www.github.com/googleapis/python-kms/issues/167)) ([1aaaea9](https://www.github.com/googleapis/python-kms/commit/1aaaea9405109a2f226f3d6a9631eb5f110349ab))


### Documentation

* **kms:** add samples for new hmac and rng apis ([#161](https://www.github.com/googleapis/python-kms/issues/161)) ([558b740](https://www.github.com/googleapis/python-kms/commit/558b740f0491311ebcaf3c62d7117ec15883150a))

## [2.5.0](https://www.github.com/googleapis/python-kms/compare/v2.4.3...v2.5.0) (2021-08-07)


### Features

* add support for HMAC, Variable Key Destruction, and GenerateRandom ([#157](https://www.github.com/googleapis/python-kms/issues/157)) ([4b7c9f9](https://www.github.com/googleapis/python-kms/commit/4b7c9f96a73fba8b825f8c7cfabc748728c0eb62))

## [2.4.3](https://www.github.com/googleapis/python-kms/compare/v2.4.2...v2.4.3) (2021-07-29)


### Documentation

* update README for attestation verification scripts ([#151](https://www.github.com/googleapis/python-kms/issues/151)) ([a1a111d](https://www.github.com/googleapis/python-kms/commit/a1a111d67017b89235c18455512658514ce65140))

## [2.4.2](https://www.github.com/googleapis/python-kms/compare/v2.4.1...v2.4.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#149](https://www.github.com/googleapis/python-kms/issues/149)) ([211fe79](https://www.github.com/googleapis/python-kms/commit/211fe797d8847675390af67691d7296bbf150a02))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#144](https://www.github.com/googleapis/python-kms/issues/144)) ([88fee3a](https://www.github.com/googleapis/python-kms/commit/88fee3ab24acca72d2bade56e471d60cc893d97f))


### Miscellaneous Chores

* release as 2.4.2 ([#150](https://www.github.com/googleapis/python-kms/issues/150)) ([6663190](https://www.github.com/googleapis/python-kms/commit/66631903dc8c32eea1af0bd0265893e6bdffd55f))

## [2.4.1](https://www.github.com/googleapis/python-kms/compare/v2.4.0...v2.4.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#143](https://www.github.com/googleapis/python-kms/issues/143)) ([c1f33e1](https://www.github.com/googleapis/python-kms/commit/c1f33e1844dfe2bca4b03d9ad29195381b5c0fd8))

## [2.4.0](https://www.github.com/googleapis/python-kms/compare/v2.3.0...v2.4.0) (2021-07-12)


### Features

* add always_use_jwt_access ([#129](https://www.github.com/googleapis/python-kms/issues/129)) ([cfa0802](https://www.github.com/googleapis/python-kms/commit/cfa08022db3e096e2414418b63482606af8d46cb))


### Bug Fixes

* disable always_use_jwt_access ([#133](https://www.github.com/googleapis/python-kms/issues/133)) ([8007b81](https://www.github.com/googleapis/python-kms/commit/8007b810f11ebf49cd24edd77867abac174841e9))


### Documentation

* Include verify_attestation_chains.py help text to attestations README ([#134](https://www.github.com/googleapis/python-kms/issues/134)) ([2f2bb49](https://www.github.com/googleapis/python-kms/commit/2f2bb49adca244031d584ffbb27e32585e64ed42))
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-kms/issues/1127)) ([#124](https://www.github.com/googleapis/python-kms/issues/124)) ([5c3e273](https://www.github.com/googleapis/python-kms/commit/5c3e27391c4771b4a03c87e21a5260ed8d61b9c4)), closes [#1126](https://www.github.com/googleapis/python-kms/issues/1126)

## [2.3.0](https://www.github.com/googleapis/python-kms/compare/v2.2.0...v2.3.0) (2021-06-14)


### Features

* add `from_service_account_info` ([6d115ce](https://www.github.com/googleapis/python-kms/commit/6d115ce1902e4306ba3e1d80de64a2424e47ef52))
* add common resource path helpers ([#74](https://www.github.com/googleapis/python-kms/issues/74)) ([6d115ce](https://www.github.com/googleapis/python-kms/commit/6d115ce1902e4306ba3e1d80de64a2424e47ef52))
* add ECDSA secp256k1 to the list of supported algorithms ([#120](https://www.github.com/googleapis/python-kms/issues/120)) ([65a453f](https://www.github.com/googleapis/python-kms/commit/65a453f3a2adb71ea82a96d769d748ad0dc721b4))
* add script to verify attestations with certificate chains ([#99](https://www.github.com/googleapis/python-kms/issues/99)) ([7b0799f](https://www.github.com/googleapis/python-kms/commit/7b0799f4e1b52b359862e97ea2b89befafe92713))
* expose client transport ([6d115ce](https://www.github.com/googleapis/python-kms/commit/6d115ce1902e4306ba3e1d80de64a2424e47ef52))


### Bug Fixes

* **deps:** add packaging requirement ([#114](https://www.github.com/googleapis/python-kms/issues/114)) ([a6a894f](https://www.github.com/googleapis/python-kms/commit/a6a894f0c49fb1774d74aa26441e7525f0c0d138))
* fix retryable errors ([6d115ce](https://www.github.com/googleapis/python-kms/commit/6d115ce1902e4306ba3e1d80de64a2424e47ef52))
* remove grpc send/recv limits ([6d115ce](https://www.github.com/googleapis/python-kms/commit/6d115ce1902e4306ba3e1d80de64a2424e47ef52))
* use correct retry deadline ([6d115ce](https://www.github.com/googleapis/python-kms/commit/6d115ce1902e4306ba3e1d80de64a2424e47ef52))

## [2.2.0](https://www.github.com/googleapis/python-kms/compare/v2.1.0...v2.2.0) (2020-09-16)


### Features

* regenerate client lib to pick up new mtls env ([#55](https://www.github.com/googleapis/python-kms/issues/55)) ([4d62c19](https://www.github.com/googleapis/python-kms/commit/4d62c19d2f0f7c597214f2b39dfecb85f9d75a58))


### Documentation

* add crypto_key_path_path method rename to UPGRADING.md ([#45](https://www.github.com/googleapis/python-kms/issues/45)) ([81db5d9](https://www.github.com/googleapis/python-kms/commit/81db5d90112092772b83aec57e2358088ed88e0d)), closes [#43](https://www.github.com/googleapis/python-kms/issues/43)

## [2.1.0](https://www.github.com/googleapis/python-kms/compare/v2.0.1...v2.1.0) (2020-08-27)


### Features

* accept custom client_info ([#41](https://www.github.com/googleapis/python-kms/issues/41)) ([6688e80](https://www.github.com/googleapis/python-kms/commit/6688e80aa4db74980d4a6194519c814a22cde177))

## [2.0.1](https://www.github.com/googleapis/python-kms/compare/v2.0.0...v2.0.1) (2020-08-24)


### Bug Fixes

* add system test back ([#39](https://www.github.com/googleapis/python-kms/issues/39)) ([fc5a720](https://www.github.com/googleapis/python-kms/commit/fc5a720d93ba41cd2616c7c9c8012d9a3e8f4a9c))


### Documentation

* Generate using new common.py_samples() synthtool functionality ([#35](https://www.github.com/googleapis/python-kms/issues/35)) ([90097bc](https://www.github.com/googleapis/python-kms/commit/90097bca7660f148f36e009f70d108404efa5308))

## [2.0.0](https://www.github.com/googleapis/python-kms/compare/v1.4.0...v2.0.0) (2020-07-30)


### ⚠ BREAKING CHANGES

* migrate to microgenerator. (#16)

### Features

* migrate to microgenerator. See [Migration Guide](https://github.com/googleapis/python-kms/blob/release-v2.0.0/UPGRADING.md). ([#16](https://www.github.com/googleapis/python-kms/issues/16)) ([605f757](https://www.github.com/googleapis/python-kms/commit/605f7577a9a9f1a2b39fa69da7e250b5f70e945e))


## [1.4.0](https://www.github.com/googleapis/python-kms/compare/v1.3.0...v1.4.0) (2020-04-14)


### Features

* add support for external key manager (via synth) ([#8](https://www.github.com/googleapis/python-kms/issues/8)) ([4077fc8](https://www.github.com/googleapis/python-kms/commit/4077fc89943cc09d489d44c05efcf9cab61cdbaf))

## [1.3.0](https://www.github.com/googleapis/python-kms/compare/v1.2.1...v1.3.0) (2020-02-12)


### Features

* **kms:** add `ProtectionLevel.External` enum; standardize use of 'optional' and 'required' in docstrings (via synth) ([#10070](https://www.github.com/googleapis/python-kms/issues/10070)) ([add232f](https://www.github.com/googleapis/python-kms/commit/add232fb657505264300ff37b07dc47fcdbbeede))
* **kms:** undeprecate resource name helper methods, add 2.7 deprecation warning (via synth) ([#10045](https://www.github.com/googleapis/python-kms/issues/10045)) ([23dca59](https://www.github.com/googleapis/python-kms/commit/23dca598dbfef86460d1a16e5a4386ab2714cfd3))


### Bug Fixes

* **kms:** deprecate resource name helper methods (via synth) ([#9836](https://www.github.com/googleapis/python-kms/issues/9836)) ([a3eca00](https://www.github.com/googleapis/python-kms/commit/a3eca000de2518080e4a960be731fb2be08c90da))

## 1.2.1

08-12-2019 13:44 PDT


### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8959](https://github.com/googleapis/google-cloud-python/pull/8959))

### Documentation
- Fix links to googleapis.dev ([#8998](https://github.com/googleapis/google-cloud-python/pull/8998))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 1.2.0

07-24-2019 16:42 PDT


### Implementation Changes
- Accomodate new location of 'IAMPolicyStub' (via synth). ([#8679](https://github.com/googleapis/google-cloud-python/pull/8679))

### New Features
- Add 'options_' argument to client's 'get_iam_policy'; pin black version (via synth). ([#8656](https://github.com/googleapis/google-cloud-python/pull/8656))
- Add 'client_options' support, update list method docstrings (via synth). ([#8514](https://github.com/googleapis/google-cloud-python/pull/8514))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

## 1.1.0

06-27-2019 12:32 PDT

### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8395](https://github.com/googleapis/google-cloud-python/pull/8395))
- Add empty lines (via synth). ([#8062](https://github.com/googleapis/google-cloud-python/pull/8062))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Add ability to create keys via import, add crypto algorithms (via synth).  ([#8356](https://github.com/googleapis/google-cloud-python/pull/8356))
- Retry idempotent codes for Encyrpt, Decrypt, Asymmetric Decrypt, Asymmetric Sign (via synth). ([#7715](https://github.com/googleapis/google-cloud-python/pull/7715))
- Add CAVIUM_V2_COMPRESSED option to KeyOperationAttestation (via synth). ([#7396](https://github.com/googleapis/google-cloud-python/pull/7396))

### Documentation
- Update docstrings. ([#7868](https://github.com/googleapis/google-cloud-python/pull/7868))
- Update information in READMEs to indicate KMS is GA. ([#7840](https://github.com/googleapis/google-cloud-python/pull/7840))

### Internal / Testing Changes
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Add disclaimer to auto-generated template files (via synth). ([#8318](https://github.com/googleapis/google-cloud-python/pull/8318))
- Suppress checking 'cov-fail-under' in nox default session (via synth).  ([#8245](https://github.com/googleapis/google-cloud-python/pull/8245))
- Fix coverage in 'types.py'; blacken 'noxfile.py' / 'setup.py' (via synth). ([#8157](https://github.com/googleapis/google-cloud-python/pull/8157))
- Add nox session `docs`, reorder methods (via synth). ([#7775](https://github.com/googleapis/google-cloud-python/pull/7775))
- Copy lintified proto files (via synth). ([#7449](https://github.com/googleapis/google-cloud-python/pull/7449))

## 1.0.0

02-13-2019 10:53 PST

### Implementation Changes
- Remove unused message exports. ([#7270](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/7270))
- Pick up stub docstring fix in GAPIC generator. ([#6974](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6974))

### Documentation
- Updated client library documentation URLs. ([#7307](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/7307))

### Internal / Testing Changes
- Add KMS system test ([#7304](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/7304))
- Add protos as an artifact to library ([#7205](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/7205))
- Update copyright headers
- Protoc-generated serialization update. ([#7086](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/7086))

## 0.2.1

12-18-2018 09:24 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up changes in GAPIC generator. ([#6499](https://github.com/googleapis/google-cloud-python/pull/6499))
- Fix `client_info` bug, update docstrings. ([#6414](https://github.com/googleapis/google-cloud-python/pull/6414))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))
- Update IAM version in dependencies ([#6362](https://github.com/googleapis/google-cloud-python/pull/6362))
- Avoid broken 'google-common-apis 1.5.4' release. ([#6355](https://github.com/googleapis/google-cloud-python/pull/6355))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))

### Internal / Testing Changes
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add synth metadata. ([#6569](https://github.com/googleapis/google-cloud-python/pull/6569))
- Add 'mock' to unit test dependencies for autogen libs. ([#6402](https://github.com/googleapis/google-cloud-python/pull/6402))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Don't update nox in 'kms/synth.py'. ([#6233](https://github.com/googleapis/google-cloud-python/pull/6233))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Don't scribble on setup.py harder. ([#6064](https://github.com/googleapis/google-cloud-python/pull/6064))
- Harmonize / DRY 'README.rst' / 'docs/index.rst'. ([#6021](https://github.com/googleapis/google-cloud-python/pull/6021))
- Exclude 'setup.py' from synth. ([#6038](https://github.com/googleapis/google-cloud-python/pull/6038))

## 0.2.0

### Documentation
- Docs: Replace links to `/stable/` with `/latest/`. ([#5901](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Re-generate library using kms/synth.py ([#5977](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5977))
- Re-generate library using kms/synth.py ([#5951](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5951))
- Remove synth fix for replacing `iam_policy_pb2_grpc` ([#5755](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5755))

## 0.1.0

### New Features
- KMS v1
