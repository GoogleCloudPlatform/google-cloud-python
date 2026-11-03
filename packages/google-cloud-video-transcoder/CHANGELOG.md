# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-video-transcoder/#history

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.22.0...google-cloud-video-transcoder-v1.23.0) (2026-10-29)


### Features

* update API sources and regenerate ([#18889](https://github.com/googleapis/google-cloud-python/issues/18889)) ([8705243](https://github.com/googleapis/google-cloud-python/commit/870524380c52ea234235e0c449f5c9aee2945283))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.21.0...google-cloud-video-transcoder-v1.22.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.20.0...google-cloud-video-transcoder-v1.21.0) (2026-06-22)


### Features

* regenerate google-cloud-[t-w] packages ([#17076](https://github.com/googleapis/google-cloud-python/issues/17076)) ([928a03c](https://github.com/googleapis/google-cloud-python/commit/928a03ce41fbcb82398636e89f840c00c7749cf8))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.19.0...google-cloud-video-transcoder-v1.20.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.18.0...google-cloud-video-transcoder-v1.19.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.17.0...google-cloud-video-transcoder-v1.18.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.16.0...google-cloud-video-transcoder-v1.17.0) (2025-08-29)


### Features

* [google-cloud-video-transcoder] add support for automatically generating subtitle for input videos ([#14286](https://github.com/googleapis/google-cloud-python/issues/14286)) ([35069f7](https://github.com/googleapis/google-cloud-python/commit/35069f768bb9755099eec5591f81e2fe53a49384))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.15.2...google-cloud-video-transcoder-v1.16.0) (2025-07-23)


### Features

* added support for converting the input video to a supported high dynamic range (HDR) formats ([dad1378](https://github.com/googleapis/google-cloud-python/commit/dad137832990f592fc9b90bbe387cee1a8973128))
* added support for DROP_DUPLICATE frame rate conversion strategy to achieve the exact frame rate on the output video ([dad1378](https://github.com/googleapis/google-cloud-python/commit/dad137832990f592fc9b90bbe387cee1a8973128))
* added support for fill_content_gaps field to allow processing inputs with significant number of missing frames ([dad1378](https://github.com/googleapis/google-cloud-python/commit/dad137832990f592fc9b90bbe387cee1a8973128))
* added support for specifying HEVC codec tag ([dad1378](https://github.com/googleapis/google-cloud-python/commit/dad137832990f592fc9b90bbe387cee1a8973128))


### Documentation

* improve comment formatting, add links, add references ([dad1378](https://github.com/googleapis/google-cloud-python/commit/dad137832990f592fc9b90bbe387cee1a8973128))

## [1.15.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.15.1...google-cloud-video-transcoder-v1.15.2) (2025-06-11)


### Documentation

* Update import statement example in README ([0131a33](https://github.com/googleapis/google-cloud-python/commit/0131a33582f84d9be5ecb1c0ef8b56aa3d9e9cf0))

## [1.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.15.0...google-cloud-video-transcoder-v1.15.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([4757dae](https://github.com/googleapis/google-cloud-python/commit/4757daede978618382ba46f4aa91bb9cfd9b937b))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.14.0...google-cloud-video-transcoder-v1.15.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))
* Add support for reading selective GAPIC generation methods from service YAML ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.13.1...google-cloud-video-transcoder-v1.14.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.13.0...google-cloud-video-transcoder-v1.13.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13246](https://github.com/googleapis/google-cloud-python/issues/13246)) ([bcad563](https://github.com/googleapis/google-cloud-python/commit/bcad563acea541bb51f9fbd005f18e9f32e381f0))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.12.5...google-cloud-video-transcoder-v1.13.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13210](https://github.com/googleapis/google-cloud-python/issues/13210)) ([0b62ac6](https://github.com/googleapis/google-cloud-python/commit/0b62ac6aa99bd3259a088097630f2bd1f06825e6))

## [1.12.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.12.4...google-cloud-video-transcoder-v1.12.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([9cdac77](https://github.com/googleapis/google-cloud-python/commit/9cdac77b20a8c9720aa668639e3ca6d1e759a2de))

## [1.12.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.12.3...google-cloud-video-transcoder-v1.12.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12870](https://github.com/googleapis/google-cloud-python/issues/12870)) ([4d16761](https://github.com/googleapis/google-cloud-python/commit/4d16761640dd8e35410b3219b7d675d7668d2f88))

## [1.12.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.12.2...google-cloud-video-transcoder-v1.12.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12388](https://github.com/googleapis/google-cloud-python/issues/12388)) ([d2cd4ff](https://github.com/googleapis/google-cloud-python/commit/d2cd4ffd12467ad512cccd7a0e9bb897ff2ce2a7))

## [1.12.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.12.1...google-cloud-video-transcoder-v1.12.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12310](https://github.com/googleapis/google-cloud-python/issues/12310)) ([41821da](https://github.com/googleapis/google-cloud-python/commit/41821da1fe08cc2aeeefc8c8f516023e4b0d0700))
* fix ValueError in test__validate_universe_domain ([2451e88](https://github.com/googleapis/google-cloud-python/commit/2451e88f302bc582b3f6d01a6ec6aceba7646252))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.12.0...google-cloud-video-transcoder-v1.12.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.11.0...google-cloud-video-transcoder-v1.12.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12244](https://github.com/googleapis/google-cloud-python/issues/12244)) ([8d6b772](https://github.com/googleapis/google-cloud-python/commit/8d6b7729d93c1347529a3d34ed6266af55225578))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-transcoder-v1.10.1...google-cloud-video-transcoder-v1.11.0) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [1.10.1](https://github.com/googleapis/python-video-transcoder/compare/v1.10.0...v1.10.1) (2023-09-18)


### Documentation

* Minor formatting ([180aca1](https://github.com/googleapis/python-video-transcoder/commit/180aca14aca091cb5705451e164f2b9466481ea2))
* Remove migrated samples ([#333](https://github.com/googleapis/python-video-transcoder/issues/333)) ([27b99fb](https://github.com/googleapis/python-video-transcoder/commit/27b99fb757e206f13062ca69c3b752d256351397))

## [1.10.0](https://github.com/googleapis/python-video-transcoder/compare/v1.9.1...v1.10.0) (2023-07-11)


### Features

* Added support for batch mode priority ([1c4f0fe](https://github.com/googleapis/python-video-transcoder/commit/1c4f0fe0ffa08b404ca0cd8f5fda0920cacbd483))
* Added support for content encryption (DRM) ([1c4f0fe](https://github.com/googleapis/python-video-transcoder/commit/1c4f0fe0ffa08b404ca0cd8f5fda0920cacbd483))
* Added support for disabling job processing optimizations ([1c4f0fe](https://github.com/googleapis/python-video-transcoder/commit/1c4f0fe0ffa08b404ca0cd8f5fda0920cacbd483))
* Added support for segment template manifest generation with DASH ([1c4f0fe](https://github.com/googleapis/python-video-transcoder/commit/1c4f0fe0ffa08b404ca0cd8f5fda0920cacbd483))

## [1.9.1](https://github.com/googleapis/python-video-transcoder/compare/v1.9.0...v1.9.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#314](https://github.com/googleapis/python-video-transcoder/issues/314)) ([a56cebc](https://github.com/googleapis/python-video-transcoder/commit/a56cebc53896633e47bf14f5cfd2a0c0cd882c4b))

## [1.9.0](https://github.com/googleapis/python-video-transcoder/compare/v1.8.2...v1.9.0) (2023-04-13)


### Features

* Add support for batch processing mode ([#300](https://github.com/googleapis/python-video-transcoder/issues/300)) ([b1bbc0d](https://github.com/googleapis/python-video-transcoder/commit/b1bbc0dbd10ae60da462b0e50207da7e440cb86a))

## [1.8.2](https://github.com/googleapis/python-video-transcoder/compare/v1.8.1...v1.8.2) (2023-04-12)


### Documentation

* **samples:** Remove restriction of JPEGs only for overlay images ([#299](https://github.com/googleapis/python-video-transcoder/issues/299)) ([a73bdbb](https://github.com/googleapis/python-video-transcoder/commit/a73bdbb1048d2cfacc80cef3db8fd135da2fcc35))
* **samples:** Update captions code samples for display name and language ([10adada](https://github.com/googleapis/python-video-transcoder/commit/10adada9a3b4e0bbe37e2a1ba630f819916a78e0))

## [1.8.1](https://github.com/googleapis/python-video-transcoder/compare/v1.8.0...v1.8.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#296](https://github.com/googleapis/python-video-transcoder/issues/296)) ([ced945e](https://github.com/googleapis/python-video-transcoder/commit/ced945edd9994b8bd45d3c350735b394b3c1c48e))

## [1.8.0](https://github.com/googleapis/python-video-transcoder/compare/v1.7.0...v1.8.0) (2023-03-01)


### Features

* Specifying language code and display name for text and audio streams is now supported ([#288](https://github.com/googleapis/python-video-transcoder/issues/288)) ([9a47aa7](https://github.com/googleapis/python-video-transcoder/commit/9a47aa7d8549d0317af910d0d18bef897fcb7708))

## [1.7.0](https://github.com/googleapis/python-video-transcoder/compare/v1.6.1...v1.7.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#283](https://github.com/googleapis/python-video-transcoder/issues/283)) ([3c36813](https://github.com/googleapis/python-video-transcoder/commit/3c368135a0874f76909e0f9b92f12fea32617acd))

## [1.6.1](https://github.com/googleapis/python-video-transcoder/compare/v1.6.0...v1.6.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([37abda1](https://github.com/googleapis/python-video-transcoder/commit/37abda184aea0d52b710469af59f77405bd7904a))


### Documentation

* Add documentation for enums ([37abda1](https://github.com/googleapis/python-video-transcoder/commit/37abda184aea0d52b710469af59f77405bd7904a))

## [1.6.0](https://github.com/googleapis/python-video-transcoder/compare/v1.5.0...v1.6.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#265](https://github.com/googleapis/python-video-transcoder/issues/265)) ([a1f708a](https://github.com/googleapis/python-video-transcoder/commit/a1f708a1398a633e086793e3d6bf0354f837e138))

## [1.5.0](https://github.com/googleapis/python-video-transcoder/compare/v1.4.3...v1.5.0) (2022-12-15)


### Features

* Add PreprocessingConfig.deinterlace ([227a759](https://github.com/googleapis/python-video-transcoder/commit/227a759d2edf9ad1e6c3110b6004e530a35dd13b))
* Add support for `google.cloud.video.transcoder.__version__` ([227a759](https://github.com/googleapis/python-video-transcoder/commit/227a759d2edf9ad1e6c3110b6004e530a35dd13b))
* Add typing to proto.Message based class attributes ([227a759](https://github.com/googleapis/python-video-transcoder/commit/227a759d2edf9ad1e6c3110b6004e530a35dd13b))


### Bug Fixes

* Add dict typing for client_options ([227a759](https://github.com/googleapis/python-video-transcoder/commit/227a759d2edf9ad1e6c3110b6004e530a35dd13b))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([0d53a7b](https://github.com/googleapis/python-video-transcoder/commit/0d53a7baba85c976a4315edf54d34e8bf7225029))
* Drop usage of pkg_resources ([0d53a7b](https://github.com/googleapis/python-video-transcoder/commit/0d53a7baba85c976a4315edf54d34e8bf7225029))
* Fix timeout default values ([0d53a7b](https://github.com/googleapis/python-video-transcoder/commit/0d53a7baba85c976a4315edf54d34e8bf7225029))


### Documentation

* Minor documentation changes ([227a759](https://github.com/googleapis/python-video-transcoder/commit/227a759d2edf9ad1e6c3110b6004e530a35dd13b))
* **samples:** Snippetgen handling of repeated enum field ([227a759](https://github.com/googleapis/python-video-transcoder/commit/227a759d2edf9ad1e6c3110b6004e530a35dd13b))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([0d53a7b](https://github.com/googleapis/python-video-transcoder/commit/0d53a7baba85c976a4315edf54d34e8bf7225029))

## [1.4.3](https://github.com/googleapis/python-video-transcoder/compare/v1.4.2...v1.4.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#246](https://github.com/googleapis/python-video-transcoder/issues/246)) ([34fdac8](https://github.com/googleapis/python-video-transcoder/commit/34fdac8f493cf4a14319c4b7d29f09bd0f771167))

## [1.4.2](https://github.com/googleapis/python-video-transcoder/compare/v1.4.1...v1.4.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#241](https://github.com/googleapis/python-video-transcoder/issues/241)) ([e7dafea](https://github.com/googleapis/python-video-transcoder/commit/e7dafea508fb1c0d016cac8eb134978a75d05b10))

## [1.4.1](https://github.com/googleapis/python-video-transcoder/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#217](https://github.com/googleapis/python-video-transcoder/issues/217)) ([150b732](https://github.com/googleapis/python-video-transcoder/commit/150b732719344061a49fb2e1438fbee63a8a0af8))
* **deps:** require proto-plus >= 1.22.0 ([150b732](https://github.com/googleapis/python-video-transcoder/commit/150b732719344061a49fb2e1438fbee63a8a0af8))

## [1.4.0](https://github.com/googleapis/python-video-transcoder/compare/v1.3.2...v1.4.0) (2022-07-16)


### Features

* add audience parameter ([63e75a3](https://github.com/googleapis/python-video-transcoder/commit/63e75a37e22c8eeaa98a7d97601a5bc49e4e2dc2))
* add support for user labels for job and job template ([#203](https://github.com/googleapis/python-video-transcoder/issues/203)) ([a0d7927](https://github.com/googleapis/python-video-transcoder/commit/a0d7927a08855596410c351f1c8fabf348a560a8))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#205](https://github.com/googleapis/python-video-transcoder/issues/205)) ([63e75a3](https://github.com/googleapis/python-video-transcoder/commit/63e75a37e22c8eeaa98a7d97601a5bc49e4e2dc2))
* require python 3.7+ ([#208](https://github.com/googleapis/python-video-transcoder/issues/208)) ([8b4aa48](https://github.com/googleapis/python-video-transcoder/commit/8b4aa4888247767ce7da821b91bd878bdb4c1085))

## [1.3.2](https://github.com/googleapis/python-video-transcoder/compare/v1.3.1...v1.3.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#195](https://github.com/googleapis/python-video-transcoder/issues/195)) ([8d9c679](https://github.com/googleapis/python-video-transcoder/commit/8d9c679a2f0b460c1f34456ab2e46437c4cbdc16))


### Documentation

* fix changelog header to consistent size ([#196](https://github.com/googleapis/python-video-transcoder/issues/196)) ([04ee631](https://github.com/googleapis/python-video-transcoder/commit/04ee631bb65cd5bb0121f7dcfce9b78e67d19198))

## [1.3.1](https://github.com/googleapis/python-video-transcoder/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#153](https://github.com/googleapis/python-video-transcoder/issues/153)) ([03ba693](https://github.com/googleapis/python-video-transcoder/commit/03ba693031d605a3e61b3fd1e7e0c5529bc3c399))

## [1.3.0](https://github.com/googleapis/python-video-transcoder/compare/v1.2.1...v1.3.0) (2022-02-24)


### Features

* add api key support ([#127](https://github.com/googleapis/python-video-transcoder/issues/127)) ([ac6a403](https://github.com/googleapis/python-video-transcoder/commit/ac6a4031ac66a721d776c41885830023023f14f2)), closes [#140](https://github.com/googleapis/python-video-transcoder/issues/140)


### Bug Fixes

* **deps:** require proto-plus >= 1.20.3 ([ac6a403](https://github.com/googleapis/python-video-transcoder/commit/ac6a4031ac66a721d776c41885830023023f14f2))
* Remove deprecated v1beta1 API that is no longer available ([#138](https://github.com/googleapis/python-video-transcoder/issues/138)) ([e8a85da](https://github.com/googleapis/python-video-transcoder/commit/e8a85da130a0b688167a1474c339c66af1c6760c))
* rename mapping attribute of AudioStream to mapping_ ([c14695b](https://github.com/googleapis/python-video-transcoder/commit/c14695bc9070ec64a890c8f81af382165f5d04ea))
* resolve DuplicateCredentialArgs error when using credentials_file ([6774bd3](https://github.com/googleapis/python-video-transcoder/commit/6774bd328f235894caf7343088c25cc2809d8932))
* resolve issue where mapping attribute of AudioStream could not be set ([c14695b](https://github.com/googleapis/python-video-transcoder/commit/c14695bc9070ec64a890c8f81af382165f5d04ea))


### Documentation

* add generated snippets ([e8a85da](https://github.com/googleapis/python-video-transcoder/commit/e8a85da130a0b688167a1474c339c66af1c6760c))
* **samples:** update samples to use mapping_ attribute of AudioStream ([#142](https://github.com/googleapis/python-video-transcoder/issues/142)) ([7fbc619](https://github.com/googleapis/python-video-transcoder/commit/7fbc61917562c269439828df82b474700c95ea23))
* **samples:** add samples and tests for adding captions to a job ([#131](https://github.com/googleapis/python-video-transcoder/issues/131)) ([e30431f](https://github.com/googleapis/python-video-transcoder/commit/e30431fec7c15666afbb5bc975f7077389aac06d))

## [1.2.1](https://www.github.com/googleapis/python-video-transcoder/compare/v1.2.0...v1.2.1) (2021-11-04)


### Bug Fixes

* **deps:** drop packaging dependency ([9850614](https://www.github.com/googleapis/python-video-transcoder/commit/985061433802e6a49a23e53b77aecbaafe7bf12a))
* **deps:** require google-api-core >= 1.28.0 ([9850614](https://www.github.com/googleapis/python-video-transcoder/commit/985061433802e6a49a23e53b77aecbaafe7bf12a))


### Documentation

* list oneofs in docstring ([9850614](https://www.github.com/googleapis/python-video-transcoder/commit/985061433802e6a49a23e53b77aecbaafe7bf12a))

## [1.2.0](https://www.github.com/googleapis/python-video-transcoder/compare/v1.1.0...v1.2.0) (2021-10-14)


### Features

* add support for python 3.10 ([#108](https://www.github.com/googleapis/python-video-transcoder/issues/108)) ([e9c1c22](https://www.github.com/googleapis/python-video-transcoder/commit/e9c1c229fe88d200d0f60314814078e79e3f1524))

## [1.1.0](https://www.github.com/googleapis/python-video-transcoder/compare/v1.0.1...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#104](https://www.github.com/googleapis/python-video-transcoder/issues/104)) ([2c5f07d](https://www.github.com/googleapis/python-video-transcoder/commit/2c5f07d5d12d05c65854409f45374b846363328c))


### Bug Fixes

* remove Encryption settings that were published erroneously ([#102](https://www.github.com/googleapis/python-video-transcoder/issues/102)) ([824009a](https://www.github.com/googleapis/python-video-transcoder/commit/824009ac01700341071b50af2741ef6493dcbcf5))

## [1.0.1](https://www.github.com/googleapis/python-video-transcoder/compare/v1.0.0...v1.0.1) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([34391dc](https://www.github.com/googleapis/python-video-transcoder/commit/34391dc7fbf433278e34843d4994364f44e62b4e))

## [1.0.0](https://www.github.com/googleapis/python-video-transcoder/compare/v0.5.1...v1.0.0) (2021-09-29)


### Features

* bump release level to production/stable ([#79](https://www.github.com/googleapis/python-video-transcoder/issues/79)) ([45ba870](https://www.github.com/googleapis/python-video-transcoder/commit/45ba87048ef73c666c00248c6da3637fd418d70a))

## [0.5.1](https://www.github.com/googleapis/python-video-transcoder/compare/v0.5.0...v0.5.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([81b1273](https://www.github.com/googleapis/python-video-transcoder/commit/81b127355c37c59a36a5da45a71f8c02d64ae592))

## [0.5.0](https://www.github.com/googleapis/python-video-transcoder/compare/v0.4.1...v0.5.0) (2021-08-07)


### Features

* Add ttl_after_completion_days field to Job ([d862900](https://www.github.com/googleapis/python-video-transcoder/commit/d86290047e9464e4026c264a6dfea51936b21c2c))
* Add video cropping feature ([#81](https://www.github.com/googleapis/python-video-transcoder/issues/81)) ([d862900](https://www.github.com/googleapis/python-video-transcoder/commit/d86290047e9464e4026c264a6dfea51936b21c2c))
* Add video padding feature ([d862900](https://www.github.com/googleapis/python-video-transcoder/commit/d86290047e9464e4026c264a6dfea51936b21c2c))


### Documentation

* Indicate v1beta1 deprecation ([d862900](https://www.github.com/googleapis/python-video-transcoder/commit/d86290047e9464e4026c264a6dfea51936b21c2c))
* Update proto documentation ([d862900](https://www.github.com/googleapis/python-video-transcoder/commit/d86290047e9464e4026c264a6dfea51936b21c2c))

## [0.4.1](https://www.github.com/googleapis/python-video-transcoder/compare/v0.4.0...v0.4.1) (2021-07-27)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#70](https://www.github.com/googleapis/python-video-transcoder/issues/70)) ([37d076a](https://www.github.com/googleapis/python-video-transcoder/commit/37d076a9fba1fc995ee955528007d10c75765975))
* enable self signed jwt for grpc ([#75](https://www.github.com/googleapis/python-video-transcoder/issues/75)) ([af5ecd9](https://www.github.com/googleapis/python-video-transcoder/commit/af5ecd9295f46bc9a82bc62cd53b815ef5db10df))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#71](https://www.github.com/googleapis/python-video-transcoder/issues/71)) ([0b67055](https://www.github.com/googleapis/python-video-transcoder/commit/0b670557d0000fc891ebae7ea8f4f54959c89b79))


### Miscellaneous Chores

* release as 0.4.1 ([#76](https://www.github.com/googleapis/python-video-transcoder/issues/76)) ([4173cf3](https://www.github.com/googleapis/python-video-transcoder/commit/4173cf356a1ce84cde8ef28e0098cb8ad06f57e4))

## [0.4.0](https://www.github.com/googleapis/python-video-transcoder/compare/v0.3.1...v0.4.0) (2021-07-09)


### Features

* add always_use_jwt_access ([#62](https://www.github.com/googleapis/python-video-transcoder/issues/62)) ([d43c40e](https://www.github.com/googleapis/python-video-transcoder/commit/d43c40e9ab80c42afd25efa1c2980d23dbc50ce2))
* Add Transcoder V1 ([#67](https://www.github.com/googleapis/python-video-transcoder/issues/67)) ([721d28e](https://www.github.com/googleapis/python-video-transcoder/commit/721d28ec565bfdb41a195167a989baf042ede228))


### Bug Fixes

* disable always_use_jwt_access ([#66](https://www.github.com/googleapis/python-video-transcoder/issues/66)) ([98d8b86](https://www.github.com/googleapis/python-video-transcoder/commit/98d8b860227a9b9a8b4cecc851ec547d7789ac66))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-video-transcoder/issues/1127)) ([#58](https://www.github.com/googleapis/python-video-transcoder/issues/58)) ([1659ce8](https://www.github.com/googleapis/python-video-transcoder/commit/1659ce88ef94139a271be9719a4adaf4e3a600c0)), closes [#1126](https://www.github.com/googleapis/python-video-transcoder/issues/1126)

## [0.3.1](https://www.github.com/googleapis/python-video-transcoder/compare/v0.3.0...v0.3.1) (2021-05-28)


### Bug Fixes

* **deps:** add packaging requirement ([#52](https://www.github.com/googleapis/python-video-transcoder/issues/52)) ([7ffa13c](https://www.github.com/googleapis/python-video-transcoder/commit/7ffa13c999260f47fbeb9dcce04110a7db9fd172))

## [0.3.0](https://www.github.com/googleapis/python-video-transcoder/compare/v0.2.1...v0.3.0) (2021-03-31)


### Features

* add `from_service_account_info` ([#32](https://www.github.com/googleapis/python-video-transcoder/issues/32)) ([4076914](https://www.github.com/googleapis/python-video-transcoder/commit/4076914adfde514417b5a39a0e5fcd905e5f6e8f))

## [0.2.1](https://www.github.com/googleapis/python-video-transcoder/compare/v0.2.0...v0.2.1) (2021-02-12)


### Bug Fixes

* remove gRPC send/recv limits ([#18](https://www.github.com/googleapis/python-video-transcoder/issues/18)) ([03332a4](https://www.github.com/googleapis/python-video-transcoder/commit/03332a4287ad31d2fd41f4de27c3fea5f20e1d53))

## [0.2.0](https://www.github.com/googleapis/python-video-transcoder/compare/v0.1.0...v0.2.0) (2020-11-14)


### Features

* add create_time, start_time, and end_time to jobs ([#10](https://www.github.com/googleapis/python-video-transcoder/issues/10)) ([a5a210e](https://www.github.com/googleapis/python-video-transcoder/commit/a5a210e16420e3450200a346aaa2cd18a7270cf3))

## 0.1.0 (2020-08-24)


### Features

* generate v1beta1 ([06cfb30](https://www.github.com/googleapis/python-video-transcoder/commit/06cfb307250f3e0ef4a6ce3e54e55c3b89c73095))
