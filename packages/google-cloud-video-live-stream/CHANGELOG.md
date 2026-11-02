# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-video-live-stream/#history

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.17.0...google-cloud-video-live-stream-v1.18.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.16.0...google-cloud-video-live-stream-v1.17.0) (2026-06-22)


### Features

* regenerate google-cloud-[t-w] packages ([#17076](https://github.com/googleapis/google-cloud-python/issues/17076)) ([928a03c](https://github.com/googleapis/google-cloud-python/commit/928a03ce41fbcb82398636e89f840c00c7749cf8))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.15.0...google-cloud-video-live-stream-v1.16.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.14.0...google-cloud-video-live-stream-v1.15.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.13.0...google-cloud-video-live-stream-v1.14.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.12.0...google-cloud-video-live-stream-v1.13.0) (2025-09-24)


### Documentation

* [google-cloud-video-live-stream] Update requirements of resource ID fields to be more clear ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))


### Features

* [google-cloud-video-live-stream] Added H.265 (HEVC) codec support  ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))
* [google-cloud-video-live-stream] Added UHD (4k) resolution support  ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))
* [google-cloud-video-live-stream] Added Auto Transcription support  ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))
* [google-cloud-video-live-stream] Added StartDistribution/StopDistribution methods and
Distribution/DistributionStream messages used for distributing live
streams to external RTMP/SRT endpoints ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))
* [google-cloud-video-live-stream] Added PreviewInput method used for the low latency input monitoring ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))
* [google-cloud-video-live-stream] Added UpdateEncryptions event to perform key rotation without restarting a channel ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.11.1...google-cloud-video-live-stream-v1.12.0) (2025-05-15)


### Features

* added DVRSession methods to support DVR feature ([f20efc4](https://github.com/googleapis/google-cloud-python/commit/f20efc44ed858b34b96a70dfcd8938e6be86cbb2))
* added OutputType field to the Clip resource to support MP4 clipping ([f20efc4](https://github.com/googleapis/google-cloud-python/commit/f20efc44ed858b34b96a70dfcd8938e6be86cbb2))


### Documentation

* A comment for field `requested_cancellation` in message `.google.cloud.video.livestream.v1.OperationMetadata` is changed to clarify error type ([f20efc4](https://github.com/googleapis/google-cloud-python/commit/f20efc44ed858b34b96a70dfcd8938e6be86cbb2))
* Clarified GCS in the comment for method `DeleteClip` in service `LivestreamService` ([f20efc4](https://github.com/googleapis/google-cloud-python/commit/f20efc44ed858b34b96a70dfcd8938e6be86cbb2))
* Updated comment for field `update_mask` in message `.google.cloud.video.livestream.v1.UpdateInputRequest` to indicate updates in `tier` field are allowed ([f20efc4](https://github.com/googleapis/google-cloud-python/commit/f20efc44ed858b34b96a70dfcd8938e6be86cbb2))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.11.0...google-cloud-video-live-stream-v1.11.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([4757dae](https://github.com/googleapis/google-cloud-python/commit/4757daede978618382ba46f4aa91bb9cfd9b937b))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.10.0...google-cloud-video-live-stream-v1.11.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))
* Add support for reading selective GAPIC generation methods from service YAML ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.9.1...google-cloud-video-live-stream-v1.10.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.9.0...google-cloud-video-live-stream-v1.9.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13246](https://github.com/googleapis/google-cloud-python/issues/13246)) ([bcad563](https://github.com/googleapis/google-cloud-python/commit/bcad563acea541bb51f9fbd005f18e9f32e381f0))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.8.1...google-cloud-video-live-stream-v1.9.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13210](https://github.com/googleapis/google-cloud-python/issues/13210)) ([0b62ac6](https://github.com/googleapis/google-cloud-python/commit/0b62ac6aa99bd3259a088097630f2bd1f06825e6))

## [1.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.8.0...google-cloud-video-live-stream-v1.8.1) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([9cdac77](https://github.com/googleapis/google-cloud-python/commit/9cdac77b20a8c9720aa668639e3ca6d1e759a2de))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.7.4...google-cloud-video-live-stream-v1.8.0) (2024-07-11)


### Features

* added Clip resource for performing clip cutting jobs ([3ca8bfb](https://github.com/googleapis/google-cloud-python/commit/3ca8bfb426b345aec23bceabcd366f4a0e368da6))
* added RetentionConfig for enabling retention of output media segments ([3ca8bfb](https://github.com/googleapis/google-cloud-python/commit/3ca8bfb426b345aec23bceabcd366f4a0e368da6))
* added StaticOverlay for embedding images the whole duration of the live stream ([3ca8bfb](https://github.com/googleapis/google-cloud-python/commit/3ca8bfb426b345aec23bceabcd366f4a0e368da6))


### Documentation

* clarify the format of key/id fields ([3ca8bfb](https://github.com/googleapis/google-cloud-python/commit/3ca8bfb426b345aec23bceabcd366f4a0e368da6))

## [1.7.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.7.3...google-cloud-video-live-stream-v1.7.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12870](https://github.com/googleapis/google-cloud-python/issues/12870)) ([4d16761](https://github.com/googleapis/google-cloud-python/commit/4d16761640dd8e35410b3219b7d675d7668d2f88))

## [1.7.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.7.2...google-cloud-video-live-stream-v1.7.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12388](https://github.com/googleapis/google-cloud-python/issues/12388)) ([d2cd4ff](https://github.com/googleapis/google-cloud-python/commit/d2cd4ffd12467ad512cccd7a0e9bb897ff2ce2a7))

## [1.7.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.7.1...google-cloud-video-live-stream-v1.7.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12310](https://github.com/googleapis/google-cloud-python/issues/12310)) ([41821da](https://github.com/googleapis/google-cloud-python/commit/41821da1fe08cc2aeeefc8c8f516023e4b0d0700))
* fix ValueError in test__validate_universe_domain ([2451e88](https://github.com/googleapis/google-cloud-python/commit/2451e88f302bc582b3f6d01a6ec6aceba7646252))

## [1.7.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.7.0...google-cloud-video-live-stream-v1.7.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.6.0...google-cloud-video-live-stream-v1.7.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12244](https://github.com/googleapis/google-cloud-python/issues/12244)) ([8d6b772](https://github.com/googleapis/google-cloud-python/commit/8d6b7729d93c1347529a3d34ed6266af55225578))

## [1.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-live-stream-v1.5.2...google-cloud-video-live-stream-v1.6.0) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [1.5.2](https://github.com/googleapis/python-video-live-stream/compare/v1.5.1...v1.5.2) (2023-09-19)


### Documentation

* Minor formatting ([39eb5b3](https://github.com/googleapis/python-video-live-stream/commit/39eb5b313967dfeb47cbaeb99e5b64030c53afae))
* Remove migrated samples ([#187](https://github.com/googleapis/python-video-live-stream/issues/187)) ([0988a81](https://github.com/googleapis/python-video-live-stream/commit/0988a81ddc2f7bab18186604d28c030be646bf09))

## [1.5.1](https://github.com/googleapis/python-video-live-stream/compare/v1.5.0...v1.5.1) (2023-08-11)


### Documentation

* **samples:** Add samples and tests for pools and assets ([#180](https://github.com/googleapis/python-video-live-stream/issues/180)) ([95977cc](https://github.com/googleapis/python-video-live-stream/commit/95977cc61c207db463675aae969e8b28e0173c7d))

## [1.5.0](https://github.com/googleapis/python-video-live-stream/compare/v1.4.1...v1.5.0) (2023-08-09)


### Features

* Added a new asset resource which can be used as the content of slate events ([825eedf](https://github.com/googleapis/python-video-live-stream/commit/825eedff15c4bb036cbcd2fe52bf7ae0fa4c9c46))
* Added a new pool resource for protecting input endpoints within a VPC Service Controls perimeter ([825eedf](https://github.com/googleapis/python-video-live-stream/commit/825eedff15c4bb036cbcd2fe52bf7ae0fa4c9c46))
* Added support for slate events which allow users to create and insert a slate into a live stream to replace the main live stream content ([825eedf](https://github.com/googleapis/python-video-live-stream/commit/825eedff15c4bb036cbcd2fe52bf7ae0fa4c9c46))

## [1.4.1](https://github.com/googleapis/python-video-live-stream/compare/v1.4.0...v1.4.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#167](https://github.com/googleapis/python-video-live-stream/issues/167)) ([f010478](https://github.com/googleapis/python-video-live-stream/commit/f0104783006f7816b5f79816ee9c3019e1c9a29c))

## [1.4.0](https://github.com/googleapis/python-video-live-stream/compare/v1.3.0...v1.4.0) (2023-03-23)


### Features

* Added Encryption for enabling output encryption with DRM systems ([638bd0a](https://github.com/googleapis/python-video-live-stream/commit/638bd0ac4008b5b2004067dbcd7307899e700f27))
* Added InputConfig to allow enabling/disabling automatic failover ([638bd0a](https://github.com/googleapis/python-video-live-stream/commit/638bd0ac4008b5b2004067dbcd7307899e700f27))
* Added new tasks to Event: inputSwitch, returnToProgram, mute, unmute ([638bd0a](https://github.com/googleapis/python-video-live-stream/commit/638bd0ac4008b5b2004067dbcd7307899e700f27))
* Added support for audio normalization and audio gain ([638bd0a](https://github.com/googleapis/python-video-live-stream/commit/638bd0ac4008b5b2004067dbcd7307899e700f27))
* Added TimecodeConfig for specifying the source of timecode used in media workflow synchronization ([638bd0a](https://github.com/googleapis/python-video-live-stream/commit/638bd0ac4008b5b2004067dbcd7307899e700f27))


### Documentation

* Clarify behavior when update_mask is omitted in PATCH requests ([638bd0a](https://github.com/googleapis/python-video-live-stream/commit/638bd0ac4008b5b2004067dbcd7307899e700f27))
* Fix formatting of request arg in docstring ([#154](https://github.com/googleapis/python-video-live-stream/issues/154)) ([c41b461](https://github.com/googleapis/python-video-live-stream/commit/c41b4613db09b35c92b3f18d09591755ea7039be))

## [1.3.0](https://github.com/googleapis/python-video-live-stream/compare/v1.2.1...v1.3.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#145](https://github.com/googleapis/python-video-live-stream/issues/145)) ([f0cb14c](https://github.com/googleapis/python-video-live-stream/commit/f0cb14c02276e10720da178ff05d63287f39b90e))

## [1.2.1](https://github.com/googleapis/python-video-live-stream/compare/v1.2.0...v1.2.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([379c135](https://github.com/googleapis/python-video-live-stream/commit/379c1353e33a2625912f7f4e489f17faf8dd1bb8))


### Documentation

* Add documentation for enums ([379c135](https://github.com/googleapis/python-video-live-stream/commit/379c1353e33a2625912f7f4e489f17faf8dd1bb8))

## [1.2.0](https://github.com/googleapis/python-video-live-stream/compare/v1.1.0...v1.2.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#133](https://github.com/googleapis/python-video-live-stream/issues/133)) ([e6ca5aa](https://github.com/googleapis/python-video-live-stream/commit/e6ca5aabc80f70430dc36a35181d8a50d976af78))

## [1.1.0](https://github.com/googleapis/python-video-live-stream/compare/v1.0.4...v1.1.0) (2022-12-15)


### Features

* Add support for `google.cloud.video.live_stream.__version__` ([714cbd4](https://github.com/googleapis/python-video-live-stream/commit/714cbd4098cca36a7768f5c8d99b426e58ebc0a7))
* Add typing to proto.Message based class attributes ([714cbd4](https://github.com/googleapis/python-video-live-stream/commit/714cbd4098cca36a7768f5c8d99b426e58ebc0a7))


### Bug Fixes

* Add dict typing for client_options ([714cbd4](https://github.com/googleapis/python-video-live-stream/commit/714cbd4098cca36a7768f5c8d99b426e58ebc0a7))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([b836b51](https://github.com/googleapis/python-video-live-stream/commit/b836b51773c80bc25599d53d56bed3a88e68ad25))
* Drop usage of pkg_resources ([b836b51](https://github.com/googleapis/python-video-live-stream/commit/b836b51773c80bc25599d53d56bed3a88e68ad25))
* Fix timeout default values ([b836b51](https://github.com/googleapis/python-video-live-stream/commit/b836b51773c80bc25599d53d56bed3a88e68ad25))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([714cbd4](https://github.com/googleapis/python-video-live-stream/commit/714cbd4098cca36a7768f5c8d99b426e58ebc0a7))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([b836b51](https://github.com/googleapis/python-video-live-stream/commit/b836b51773c80bc25599d53d56bed3a88e68ad25))

## [1.0.4](https://github.com/googleapis/python-video-live-stream/compare/v1.0.3...v1.0.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#116](https://github.com/googleapis/python-video-live-stream/issues/116)) ([db8e690](https://github.com/googleapis/python-video-live-stream/commit/db8e690192ef15766f1bab49d68d25a518c875f5))

## [1.0.3](https://github.com/googleapis/python-video-live-stream/compare/v1.0.2...v1.0.3) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#113](https://github.com/googleapis/python-video-live-stream/issues/113)) ([1c7d6ff](https://github.com/googleapis/python-video-live-stream/commit/1c7d6ff672487d4e5c79034a41cc053390ca2ac7))

## [1.0.2](https://github.com/googleapis/python-video-live-stream/compare/v1.0.1...v1.0.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#91](https://github.com/googleapis/python-video-live-stream/issues/91)) ([7493188](https://github.com/googleapis/python-video-live-stream/commit/749318882fade03988ef26f7dde297e9301fb6fd))
* **deps:** require proto-plus >= 1.22.0 ([7493188](https://github.com/googleapis/python-video-live-stream/commit/749318882fade03988ef26f7dde297e9301fb6fd))

## [1.0.1](https://github.com/googleapis/python-video-live-stream/compare/v1.0.0...v1.0.1) (2022-08-02)


### Documentation

* **samples:** fix timeout for create input and start channel LROs; first call can take up to 15 minutes ([#86](https://github.com/googleapis/python-video-live-stream/issues/86)) ([6062208](https://github.com/googleapis/python-video-live-stream/commit/60622087d88be430cce2ef9c77ffe58b15af24e7))

## [1.0.0](https://github.com/googleapis/python-video-live-stream/compare/v0.2.0...v1.0.0) (2022-07-18)


### Features

* bump release level to production/stable ([#31](https://github.com/googleapis/python-video-live-stream/issues/31)) ([b52dbc7](https://github.com/googleapis/python-video-live-stream/commit/b52dbc7c518dd338bdc221558fc433e5f5057535))

## [0.2.0](https://github.com/googleapis/python-video-live-stream/compare/v0.1.5...v0.2.0) (2022-07-16)


### Features

* add audience parameter ([f8824ce](https://github.com/googleapis/python-video-live-stream/commit/f8824ce3ca3055939a6d2ce407c414e21e140e4b))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#78](https://github.com/googleapis/python-video-live-stream/issues/78)) ([e2f1b17](https://github.com/googleapis/python-video-live-stream/commit/e2f1b17565d44f34b33d8881243fb683fba3f37f))
* require python 3.7+ ([#77](https://github.com/googleapis/python-video-live-stream/issues/77)) ([a4e7d42](https://github.com/googleapis/python-video-live-stream/commit/a4e7d427c504ac1f39e64f7417731832926a2500))


### Documentation

* align channel config with best practices ([#71](https://github.com/googleapis/python-video-live-stream/issues/71)) ([2a1a5b2](https://github.com/googleapis/python-video-live-stream/commit/2a1a5b20f6ecb9530fa48ba22f384d266301a825))

## [0.1.5](https://github.com/googleapis/python-video-live-stream/compare/v0.1.4...v0.1.5) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#65](https://github.com/googleapis/python-video-live-stream/issues/65)) ([a072bbf](https://github.com/googleapis/python-video-live-stream/commit/a072bbf7d411b4595e5f915866a839eb52e3d208))


### Documentation

* fix changelog header to consistent size ([#66](https://github.com/googleapis/python-video-live-stream/issues/66)) ([fbc3528](https://github.com/googleapis/python-video-live-stream/commit/fbc3528b4d2f22751c0f5a99bae513668fcb3db5))

## [0.1.4](https://github.com/googleapis/python-video-live-stream/compare/v0.1.3...v0.1.4) (2022-05-22)


### Documentation

* updated comments to match API behaviors ([#45](https://github.com/googleapis/python-video-live-stream/issues/45)) ([bdc9463](https://github.com/googleapis/python-video-live-stream/commit/bdc9463156a63439ef41621405394042d01f3cb9))

## [0.1.3](https://github.com/googleapis/python-video-live-stream/compare/v0.1.2...v0.1.3) (2022-05-03)


### Documentation

* **samples:** add sample for creating a channel with a failover backup input ([#37](https://github.com/googleapis/python-video-live-stream/issues/37)) ([9587382](https://github.com/googleapis/python-video-live-stream/commit/958738237c7c055a3a656ce2c3a7964e49d6b6b1))

## [0.1.2](https://github.com/googleapis/python-video-live-stream/compare/v0.1.1...v0.1.2) (2022-04-28)


### Documentation

* **samples:** add code samples ([#21](https://github.com/googleapis/python-video-live-stream/issues/21)) ([484271d](https://github.com/googleapis/python-video-live-stream/commit/484271de8790e2d9d0d4ea02feb344398317ffe5))

## [0.1.1](https://github.com/googleapis/python-video-live-stream/compare/v0.1.0...v0.1.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#13](https://github.com/googleapis/python-video-live-stream/issues/13)) ([471eb70](https://github.com/googleapis/python-video-live-stream/commit/471eb700a7c6d928f4d03e9c438be6fa81d85a52))

## 0.1.0 (2022-02-15)


### Features

* generate v1 ([9ea3475](https://github.com/googleapis/python-video-live-stream/commit/9ea347500bc80bb43d8f30d559cfa6b9838ffc46))
