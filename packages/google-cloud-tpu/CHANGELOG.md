# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-tpu/#history

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.27.0...google-cloud-tpu-v1.28.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.26.0...google-cloud-tpu-v1.27.0) (2026-06-22)


### Features

* regenerate google-cloud-[t-w] packages ([#17076](https://github.com/googleapis/google-cloud-python/issues/17076)) ([928a03c](https://github.com/googleapis/google-cloud-python/commit/928a03ce41fbcb82398636e89f840c00c7749cf8))

## [1.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.25.0...google-cloud-tpu-v1.26.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.24.0...google-cloud-tpu-v1.25.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.23.2...google-cloud-tpu-v1.24.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.23.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.23.1...google-cloud-tpu-v1.23.2) (2025-06-11)


### Documentation

* Update import statement example in README ([0131a33](https://github.com/googleapis/google-cloud-python/commit/0131a33582f84d9be5ecb1c0ef8b56aa3d9e9cf0))

## [1.23.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.23.0...google-cloud-tpu-v1.23.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([4757dae](https://github.com/googleapis/google-cloud-python/commit/4757daede978618382ba46f4aa91bb9cfd9b937b))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.22.0...google-cloud-tpu-v1.23.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))
* Add support for reading selective GAPIC generation methods from service YAML ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.21.0...google-cloud-tpu-v1.22.0) (2025-01-16)


### Features

* **v2alpha1:** A new enum `State` is added ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** add creation timestamp to queued resources ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** add repeated networks ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** Add reservation_name field ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** Add UNKNOWN to TPU node state, This state will be used to prevent a node from being marked as READY during diagnose after it has failed repair ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** add Usage to CLH getreservations API ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** add workload_type field ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** Introduce PerformMaintenance API ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** Make V5Litepod accelerator config available ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** Make v6e available for public preview ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** Promote `spot` to v2alpha1 API ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** provide WAITING_FOR_CAPACITY state for queued resource, when the session is waiting to be provisioned ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** publish boot_disk_config to support CHD with KMS ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** v5p available for public review ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))


### Documentation

* **v2alpha1:** A comment for field `network_config` in message `.google.cloud.tpu.v2alpha1.Node` is changed ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))
* **v2alpha1:** A comment for field `state_initiator` in message `.google.cloud.tpu.v2alpha1.QueuedResourceState` is changed ([c7e1d21](https://github.com/googleapis/google-cloud-python/commit/c7e1d21b96965d8879105874f82c55f23e993adc))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.20.0...google-cloud-tpu-v1.21.0) (2025-01-13)


### Features

* [google-cloud-tpu] Add UNKNOWN to TPU node state, This state will be used to prevent a node from being marked as READY during diagnose after it has failed repair ([#13429](https://github.com/googleapis/google-cloud-python/issues/13429)) ([9adc081](https://github.com/googleapis/google-cloud-python/commit/9adc081395d805241602aaac71711576dc9340c0))
* Add UNKNOWN to TPU node state, This state will be used to prevent a node from being marked as READY during diagnose after it has failed repair ([ad5c169](https://github.com/googleapis/google-cloud-python/commit/ad5c169e9c9d7bc130ab8fc90a8fedb76eede436))
* Make V5Litepod accelerator config available for v2 ([ad5c169](https://github.com/googleapis/google-cloud-python/commit/ad5c169e9c9d7bc130ab8fc90a8fedb76eede436))
* Make v5p available for GA ([ad5c169](https://github.com/googleapis/google-cloud-python/commit/ad5c169e9c9d7bc130ab8fc90a8fedb76eede436))
* Make v6e available for GA ([ad5c169](https://github.com/googleapis/google-cloud-python/commit/ad5c169e9c9d7bc130ab8fc90a8fedb76eede436))
* Promote network_configs field to v2 API ([ad5c169](https://github.com/googleapis/google-cloud-python/commit/ad5c169e9c9d7bc130ab8fc90a8fedb76eede436))


### Documentation

* A comment for field `network_config` in message `.google.cloud.tpu.v2.Node` is changed ([ad5c169](https://github.com/googleapis/google-cloud-python/commit/ad5c169e9c9d7bc130ab8fc90a8fedb76eede436))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.19.1...google-cloud-tpu-v1.20.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))

## [1.19.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.19.0...google-cloud-tpu-v1.19.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13246](https://github.com/googleapis/google-cloud-python/issues/13246)) ([bcad563](https://github.com/googleapis/google-cloud-python/commit/bcad563acea541bb51f9fbd005f18e9f32e381f0))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.18.5...google-cloud-tpu-v1.19.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13210](https://github.com/googleapis/google-cloud-python/issues/13210)) ([0b62ac6](https://github.com/googleapis/google-cloud-python/commit/0b62ac6aa99bd3259a088097630f2bd1f06825e6))

## [1.18.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.18.4...google-cloud-tpu-v1.18.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([9cdac77](https://github.com/googleapis/google-cloud-python/commit/9cdac77b20a8c9720aa668639e3ca6d1e759a2de))

## [1.18.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.18.3...google-cloud-tpu-v1.18.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12870](https://github.com/googleapis/google-cloud-python/issues/12870)) ([4d16761](https://github.com/googleapis/google-cloud-python/commit/4d16761640dd8e35410b3219b7d675d7668d2f88))

## [1.18.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.18.2...google-cloud-tpu-v1.18.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12388](https://github.com/googleapis/google-cloud-python/issues/12388)) ([d2cd4ff](https://github.com/googleapis/google-cloud-python/commit/d2cd4ffd12467ad512cccd7a0e9bb897ff2ce2a7))

## [1.18.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.18.1...google-cloud-tpu-v1.18.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12310](https://github.com/googleapis/google-cloud-python/issues/12310)) ([41821da](https://github.com/googleapis/google-cloud-python/commit/41821da1fe08cc2aeeefc8c8f516023e4b0d0700))
* fix ValueError in test__validate_universe_domain ([2451e88](https://github.com/googleapis/google-cloud-python/commit/2451e88f302bc582b3f6d01a6ec6aceba7646252))

## [1.18.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.18.0...google-cloud-tpu-v1.18.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.17.0...google-cloud-tpu-v1.18.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.16.0...google-cloud-tpu-v1.17.0) (2023-12-07)


### Features

* Add support for python 3.12 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Introduce compatibility with native namespace packages ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Use `retry_async` instead of `retry` in async client ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.15.1...google-cloud-tpu-v1.16.0) (2023-09-20)


### Features

* **v2alpha1:** added new WAITING_FOR_RESOURCES state for QueuedResourceState ([#11673](https://github.com/googleapis/google-cloud-python/issues/11673)) ([f108e9b](https://github.com/googleapis/google-cloud-python/commit/f108e9b8235dba344f80171fd058b959c4eeed0b))

## [1.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.15.0...google-cloud-tpu-v1.15.1) (2023-09-19)


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.14.0...google-cloud-tpu-v1.15.0) (2023-08-31)


### Features

* Add MultiNodeParams in TPU ([ee2ea0d](https://github.com/googleapis/google-cloud-python/commit/ee2ea0d1ff8798d445146df8dea19eb697390b98))
* Add ResetQueueResource to the TPU service ([ee2ea0d](https://github.com/googleapis/google-cloud-python/commit/ee2ea0d1ff8798d445146df8dea19eb697390b98))
* publish boot_disk_config to support CHD with KMS ([#11622](https://github.com/googleapis/google-cloud-python/issues/11622)) ([050b5c1](https://github.com/googleapis/google-cloud-python/commit/050b5c1515a2773d5c7bc833bda97a62c2cb76b6))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.13.0...google-cloud-tpu-v1.14.0) (2023-08-10)


### Features

* **v2alpha1:** Add `state_initiator` to `QueuedResourceState` ([#11557](https://github.com/googleapis/google-cloud-python/issues/11557)) ([315e949](https://github.com/googleapis/google-cloud-python/commit/315e9495b3666f2aaeb41c6d1621ff6ff30a2142))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.12.0...google-cloud-tpu-v1.13.0) (2023-08-03)


### Features

* Add `spot` tier in v2alpha Create QueuedResource API request ([#11526](https://github.com/googleapis/google-cloud-python/issues/11526)) ([5ad269d](https://github.com/googleapis/google-cloud-python/commit/5ad269d1c897e8725acd7e002a788c12e814c27e))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.11.2...google-cloud-tpu-v1.12.0) (2023-07-25)


### Features

* add multislice_node flag ([4ccdde0](https://github.com/googleapis/google-cloud-python/commit/4ccdde051bc1741c4ac93aeb7825b58f18aa1d90))
* enable QueuedResources in us-east5 ([4ccdde0](https://github.com/googleapis/google-cloud-python/commit/4ccdde051bc1741c4ac93aeb7825b58f18aa1d90))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.11.1...google-cloud-tpu-v1.11.2) (2023-07-06)


### Documentation

* minor updates in comments ([#11465](https://github.com/googleapis/google-cloud-python/issues/11465)) ([2164070](https://github.com/googleapis/google-cloud-python/commit/2164070f7abb6d8b7d0659dc5ca774f5aa531d96))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-tpu-v1.11.0...google-cloud-tpu-v1.11.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [1.11.0](https://github.com/googleapis/python-tpu/compare/v1.10.1...v1.11.0) (2023-06-01)


### Features

* **v2alpha1:** Add MultisliceNode ([df85e2c](https://github.com/googleapis/python-tpu/commit/df85e2c95a097b2620c1f368a2dc0325c5fc9a81))
* **v2alpha1:** Enable Force on DeleteQueuedResource ([df85e2c](https://github.com/googleapis/python-tpu/commit/df85e2c95a097b2620c1f368a2dc0325c5fc9a81))

## [1.10.1](https://github.com/googleapis/python-tpu/compare/v1.10.0...v1.10.1) (2023-05-04)


### Bug Fixes

* **tpu_v2alpha1:** Restrict the visibility of API `ResetQueuedResource` ([#226](https://github.com/googleapis/python-tpu/issues/226)) ([06f1647](https://github.com/googleapis/python-tpu/commit/06f1647ff908d0d8689111cc2743b202f53f1e6d))

## [1.10.0](https://github.com/googleapis/python-tpu/compare/v1.9.0...v1.10.0) (2023-04-15)


### Features

* **v2alpha1:** Add reset_queued_resource ([45b85f2](https://github.com/googleapis/python-tpu/commit/45b85f2e7692e7df11e763bc618137f100a52298))
* **v2alpha1:** Make reservation_name parameter generally visible in QueuedResource message ([45b85f2](https://github.com/googleapis/python-tpu/commit/45b85f2e7692e7df11e763bc618137f100a52298))

## [1.9.0](https://github.com/googleapis/python-tpu/compare/v1.8.0...v1.9.0) (2023-03-24)


### Features

* Add AcceleratorConfig to ListAcceleratorTypesResponse ([#220](https://github.com/googleapis/python-tpu/issues/220)) ([495fbad](https://github.com/googleapis/python-tpu/commit/495fbad638714a9cc30d8699462630c5492c0430))


### Documentation

* Fix formatting of request arg in docstring ([#223](https://github.com/googleapis/python-tpu/issues/223)) ([58839c4](https://github.com/googleapis/python-tpu/commit/58839c441b1677a40df09fb0352e5dd28e02384d))

## [1.8.0](https://github.com/googleapis/python-tpu/compare/v1.7.2...v1.8.0) (2023-02-17)


### Features

* **v2alpha1:** Add AcceleratorConfig ([#214](https://github.com/googleapis/python-tpu/issues/214)) ([77b7f38](https://github.com/googleapis/python-tpu/commit/77b7f38d2413036442c0092224896102a1c3e54b))


### Bug Fixes

* Add service_yaml_parameters to py_gapic_library BUILD.bazel targets ([#216](https://github.com/googleapis/python-tpu/issues/216)) ([b45515e](https://github.com/googleapis/python-tpu/commit/b45515eb6f82e71c2420ddc6aadff331000bcc64))

## [1.7.2](https://github.com/googleapis/python-tpu/compare/v1.7.1...v1.7.2) (2023-01-30)


### Bug Fixes

* Proper http bindings for v2 API ([#209](https://github.com/googleapis/python-tpu/issues/209)) ([e549185](https://github.com/googleapis/python-tpu/commit/e549185be8c93233ece34290e56df72ad5f56d14))

## [1.7.1](https://github.com/googleapis/python-tpu/compare/v1.7.0...v1.7.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([3b28ff9](https://github.com/googleapis/python-tpu/commit/3b28ff913817f944e93df3b780e3ba3ba76be14f))


### Documentation

* Add documentation for enums ([3b28ff9](https://github.com/googleapis/python-tpu/commit/3b28ff913817f944e93df3b780e3ba3ba76be14f))

## [1.7.0](https://github.com/googleapis/python-tpu/compare/v1.6.0...v1.7.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#205](https://github.com/googleapis/python-tpu/issues/205)) ([9590ec0](https://github.com/googleapis/python-tpu/commit/9590ec085bbb610726e2013beaab407abab3917d))

## [1.6.0](https://github.com/googleapis/python-tpu/compare/v1.5.2...v1.6.0) (2022-12-15)


### Features

* Add support for `google.cloud.tpu.__version__` ([7bb593a](https://github.com/googleapis/python-tpu/commit/7bb593a5f9813c94210628bf447220a30fa74f8b))
* Add typing to proto.Message based class attributes ([7bb593a](https://github.com/googleapis/python-tpu/commit/7bb593a5f9813c94210628bf447220a30fa74f8b))
* Publishing TPU v2 API ([ac1bc46](https://github.com/googleapis/python-tpu/commit/ac1bc467ebffc8c8457d7dd08daf45cdc5826662))


### Bug Fixes

* Add dict typing for client_options ([7bb593a](https://github.com/googleapis/python-tpu/commit/7bb593a5f9813c94210628bf447220a30fa74f8b))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([ac1bc46](https://github.com/googleapis/python-tpu/commit/ac1bc467ebffc8c8457d7dd08daf45cdc5826662))
* Drop usage of pkg_resources ([ac1bc46](https://github.com/googleapis/python-tpu/commit/ac1bc467ebffc8c8457d7dd08daf45cdc5826662))
* Fix incorrect resource annotations for TPU v2alpha1 API ([ac1bc46](https://github.com/googleapis/python-tpu/commit/ac1bc467ebffc8c8457d7dd08daf45cdc5826662))
* Fix timeout default values ([ac1bc46](https://github.com/googleapis/python-tpu/commit/ac1bc467ebffc8c8457d7dd08daf45cdc5826662))


### Documentation

* Minor updates in comments ([#201](https://github.com/googleapis/python-tpu/issues/201)) ([0519c68](https://github.com/googleapis/python-tpu/commit/0519c684182432d210b67b885e31e7d91adfbf45))
* **samples:** Snippetgen handling of repeated enum field ([7bb593a](https://github.com/googleapis/python-tpu/commit/7bb593a5f9813c94210628bf447220a30fa74f8b))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([ac1bc46](https://github.com/googleapis/python-tpu/commit/ac1bc467ebffc8c8457d7dd08daf45cdc5826662))

## [1.5.2](https://github.com/googleapis/python-tpu/compare/v1.5.1...v1.5.2) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#194](https://github.com/googleapis/python-tpu/issues/194)) ([8f61064](https://github.com/googleapis/python-tpu/commit/8f6106452b3897c5db1eb68073082e6f5d746450))

## [1.5.1](https://github.com/googleapis/python-tpu/compare/v1.5.0...v1.5.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#192](https://github.com/googleapis/python-tpu/issues/192)) ([e65bac8](https://github.com/googleapis/python-tpu/commit/e65bac898636ab5588c581868e718231d88d11f6))

## [1.5.0](https://github.com/googleapis/python-tpu/compare/v1.4.1...v1.5.0) (2022-09-16)


### Features

* Add Secure Boot support to TPU v2alpha1 API ([#190](https://github.com/googleapis/python-tpu/issues/190)) ([955e3db](https://github.com/googleapis/python-tpu/commit/955e3dbc7bfcaa32027a4e467b05c2579f217483))

## [1.4.1](https://github.com/googleapis/python-tpu/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#175](https://github.com/googleapis/python-tpu/issues/175)) ([a7b60dc](https://github.com/googleapis/python-tpu/commit/a7b60dc3416a0f33f28e97b361df8951da706bf8))
* **deps:** require proto-plus >= 1.22.0 ([a7b60dc](https://github.com/googleapis/python-tpu/commit/a7b60dc3416a0f33f28e97b361df8951da706bf8))

## [1.4.0](https://github.com/googleapis/python-tpu/compare/v1.3.4...v1.4.0) (2022-07-16)


### Features

* add audience parameter ([3ba29bf](https://github.com/googleapis/python-tpu/commit/3ba29bfe7d9726a9ab83b70fadda23cafd2fd1b4))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#170](https://github.com/googleapis/python-tpu/issues/170)) ([8bdcce8](https://github.com/googleapis/python-tpu/commit/8bdcce87f5b9c2765619b5f724b462a59d190e8e))
* require python 3.7+ ([#168](https://github.com/googleapis/python-tpu/issues/168)) ([e08415b](https://github.com/googleapis/python-tpu/commit/e08415b197e68768b6d1b9185ad11966a3fbb04e))

## [1.3.4](https://github.com/googleapis/python-tpu/compare/v1.3.3...v1.3.4) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#158](https://github.com/googleapis/python-tpu/issues/158)) ([1d789e5](https://github.com/googleapis/python-tpu/commit/1d789e506309cd98c11b4952f5ff89f479ea3695))


### Documentation

* fix changelog header to consistent size ([#159](https://github.com/googleapis/python-tpu/issues/159)) ([1788016](https://github.com/googleapis/python-tpu/commit/1788016409819f3a3627b3c55a453e9240934fc9))

## [1.3.3](https://github.com/googleapis/python-tpu/compare/v1.3.2...v1.3.3) (2022-05-05)


### Documentation

* fix docstring for map fields ([5c230d6](https://github.com/googleapis/python-tpu/commit/5c230d6ff4533f572c6315889ca0ff7d5f6a0882))

## [1.3.2](https://github.com/googleapis/python-tpu/compare/v1.3.1...v1.3.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#89](https://github.com/googleapis/python-tpu/issues/89)) ([07b8c1a](https://github.com/googleapis/python-tpu/commit/07b8c1acd38d029fb792378f2970191f36b80445))

## [1.3.1](https://github.com/googleapis/python-tpu/compare/v1.3.0...v1.3.1) (2022-02-11)


### Documentation

* add generated snippets ([#79](https://github.com/googleapis/python-tpu/issues/79)) ([c09c807](https://github.com/googleapis/python-tpu/commit/c09c807b4f57798d4798589be0bf4c4d287e6073))

## [1.3.0](https://github.com/googleapis/python-tpu/compare/v1.2.1...v1.3.0) (2022-02-03)


### Features

* add api key support ([#74](https://github.com/googleapis/python-tpu/issues/74)) ([c6b1bfa](https://github.com/googleapis/python-tpu/commit/c6b1bfaecdf02c53d972f6d4181d3eb49d7f460a))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([776dbea](https://github.com/googleapis/python-tpu/commit/776dbea03b1bc19e930b62708ec68bce49f4d06d))

## [1.2.1](https://www.github.com/googleapis/python-tpu/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([6b3efb3](https://www.github.com/googleapis/python-tpu/commit/6b3efb38c6bdf23c8dae3fe965e01a3457f5757e))
* **deps:** require google-api-core >= 1.28.0 ([6b3efb3](https://www.github.com/googleapis/python-tpu/commit/6b3efb38c6bdf23c8dae3fe965e01a3457f5757e))


### Documentation

* list oneofs in docstring ([6b3efb3](https://www.github.com/googleapis/python-tpu/commit/6b3efb38c6bdf23c8dae3fe965e01a3457f5757e))

## [1.2.0](https://www.github.com/googleapis/python-tpu/compare/v1.1.0...v1.2.0) (2021-10-15)


### Features

* add support for python 3.10 ([#52](https://www.github.com/googleapis/python-tpu/issues/52)) ([18b9ee0](https://www.github.com/googleapis/python-tpu/commit/18b9ee0cff03b4f97071ef6c7a2bc3e613a01242))
* add TPU v2alpha1 ([#55](https://www.github.com/googleapis/python-tpu/issues/55)) ([72e3e8b](https://www.github.com/googleapis/python-tpu/commit/72e3e8b955690b5f180af89a0a15a8870fd556a8))

## [1.1.0](https://www.github.com/googleapis/python-tpu/compare/v1.0.2...v1.1.0) (2021-10-07)


### Features

* add context manager support in client ([#48](https://www.github.com/googleapis/python-tpu/issues/48)) ([f51a651](https://www.github.com/googleapis/python-tpu/commit/f51a6513f7f13c8aa0c9b06a63134a04ae6463f2))

## [1.0.2](https://www.github.com/googleapis/python-tpu/compare/v1.0.1...v1.0.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([306f0f7](https://www.github.com/googleapis/python-tpu/commit/306f0f7703ba2e1d3c1dc0201b0bd9142cd1cfde))

## [1.0.1](https://www.github.com/googleapis/python-tpu/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([2487395](https://www.github.com/googleapis/python-tpu/commit/24873956eccde0a118ea11ea19ede30758c34180))

## [1.0.0](https://www.github.com/googleapis/python-tpu/compare/v0.2.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#28](https://www.github.com/googleapis/python-tpu/issues/28)) ([64818bf](https://www.github.com/googleapis/python-tpu/commit/64818bfa56c89569bb961c3463872404cee990cf))

## [0.2.2](https://www.github.com/googleapis/python-tpu/compare/v0.2.1...v0.2.2) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#24](https://www.github.com/googleapis/python-tpu/issues/24)) ([4285625](https://www.github.com/googleapis/python-tpu/commit/4285625fc0f935820dbb428606730f10033f1974))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#20](https://www.github.com/googleapis/python-tpu/issues/20)) ([2724d46](https://www.github.com/googleapis/python-tpu/commit/2724d4653cc4c261f578a9862a4ba0adfa065236))


### Miscellaneous Chores

* release as 0.2.2 ([#25](https://www.github.com/googleapis/python-tpu/issues/25)) ([53e254f](https://www.github.com/googleapis/python-tpu/commit/53e254fbd3148eacf72236fe264049570e5f1c95))

## [0.2.1](https://www.github.com/googleapis/python-tpu/compare/v0.2.0...v0.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#19](https://www.github.com/googleapis/python-tpu/issues/19)) ([6128053](https://www.github.com/googleapis/python-tpu/commit/612805319b5aeaf6d6dce9878ea379c65258333e))

## [0.2.0](https://www.github.com/googleapis/python-tpu/compare/v0.1.0...v0.2.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#11](https://www.github.com/googleapis/python-tpu/issues/11)) ([5ed6734](https://www.github.com/googleapis/python-tpu/commit/5ed673416bc3cbaf28c7ff7537261a506d246418))


### Bug Fixes

* disable always_use_jwt_access ([b03acdf](https://www.github.com/googleapis/python-tpu/commit/b03acdf41b2deac509184f9038db70a161b4f30b))
* disable always_use_jwt_access ([#15](https://www.github.com/googleapis/python-tpu/issues/15)) ([b03acdf](https://www.github.com/googleapis/python-tpu/commit/b03acdf41b2deac509184f9038db70a161b4f30b))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-tpu/issues/1127)) ([#6](https://www.github.com/googleapis/python-tpu/issues/6)) ([e2c8018](https://www.github.com/googleapis/python-tpu/commit/e2c801881d4a6018f56b8fe81d32b0e50bd4426f)), closes [#1126](https://www.github.com/googleapis/python-tpu/issues/1126)

## 0.1.0 (2021-06-13)


### Features

* generate v1 ([7e1096c](https://www.github.com/googleapis/python-tpu/commit/7e1096c850c223445a097da61ba490499532cd34))
