# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-resumable-media/#history

## [2.11.0](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.10.2...google-resumable-media-v2.11.0) (2026-09-29)


### Features

* declare Python3.15 support ([05b0c34](https://github.com/googleapis/google-cloud-python/commit/05b0c342683b2b0e1b8dccd201ec86ec89612edc))

## [2.10.2](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.10.1...google-resumable-media-v2.10.2) (2026-08-21)


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [2.10.1](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.10.0...google-resumable-media-v2.10.1) (2026-08-06)


### Bug Fixes

* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [2.10.0](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.9.0...google-resumable-media-v2.10.0) (2026-06-02)


### Bug Fixes

* update incorrect urls in setup.py to point at monorepo vs splitrepo (#17237) ([eaed04baf3cd356c3811c66e64c277c8841c7563](https://github.com/googleapis/google-cloud-python/commit/eaed04baf3cd356c3811c66e64c277c8841c7563))

## [2.9.0](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.8.2...google-resumable-media-v2.9.0) (2026-05-06)


### Bug Fixes

* Drop support for Python 3.9 (#16938) ([33b55050e75d956efb4c3c4438f339e46e8e9782](https://github.com/googleapis/google-cloud-python/commit/33b55050e75d956efb4c3c4438f339e46e8e9782))

## [2.8.2](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.8.1...google-resumable-media-v2.8.2) (2026-03-26)


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [2.8.1](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.8.0...google-resumable-media-v2.8.1) (2026-03-12)


### Bug Fixes

* add max_length support to Gzip/Brotli decoders for urllib3 2.6+ (#495) ([cb9006056d402e01b918a7375662c8c33bfe5566](https://github.com/googleapis/google-cloud-python/commit/cb9006056d402e01b918a7375662c8c33bfe5566))

## [2.8.0](https://github.com/googleapis/google-cloud-python/compare/google-resumable-media-v2.7.2...google-resumable-media-v2.8.0) (2025-11-11)


### Features

* Add support for Python 3.13 and 3.14 (#485) ([9937233ded26924179d717b69df7c76c93f8c133](https://github.com/googleapis/google-cloud-python/commit/9937233ded26924179d717b69df7c76c93f8c133))


### Bug Fixes

* remove setup.cfg configuration for creating universal wheels (#484) ([75dbecf8d140483da27dffc970e2e87338e71432](https://github.com/googleapis/google-cloud-python/commit/75dbecf8d140483da27dffc970e2e87338e71432))
* resolve issue where pre-release versions of dependencies are installed (#481) ([23dafcf3f216a090a0d0c6941048c7da13cbe496](https://github.com/googleapis/google-cloud-python/commit/23dafcf3f216a090a0d0c6941048c7da13cbe496))

## [2.7.2](https://github.com/googleapis/google-resumable-media-python/compare/v2.7.1...v2.7.2) (2024-08-07)


### Bug Fixes

* Correctly calculate starting offset for retries of ranged reads ([#450](https://github.com/googleapis/google-resumable-media-python/issues/450)) ([34302b4](https://github.com/googleapis/google-resumable-media-python/commit/34302b4eb984330cc057ddebe3e9ff55a2745b01))

## [2.7.1](https://github.com/googleapis/google-resumable-media-python/compare/v2.7.0...v2.7.1) (2024-05-31)


### Bug Fixes

* Add a check for partial response data ([#435](https://github.com/googleapis/google-resumable-media-python/issues/435)) ([aaea392](https://github.com/googleapis/google-resumable-media-python/commit/aaea3921cb4caacf3cb142639bad41dfaf7ebb28))

## [2.7.0](https://github.com/googleapis/google-resumable-media-python/compare/v2.6.0...v2.7.0) (2023-12-10)


### Features

* Add support for Python 3.12 ([#407](https://github.com/googleapis/google-resumable-media-python/issues/407)) ([4f90013](https://github.com/googleapis/google-resumable-media-python/commit/4f900139dd9f5d158342e24f9d8657ab0134a4d8))
* Support brotli encoding ([#403](https://github.com/googleapis/google-resumable-media-python/issues/403)) ([295e40a](https://github.com/googleapis/google-resumable-media-python/commit/295e40ae414b1a6372796f3831e192fe174e45ee))

## [2.6.0](https://github.com/googleapis/google-resumable-media-python/compare/v2.5.0...v2.6.0) (2023-09-06)


### Features

* Add support for concurrent XML MPU uploads ([#395](https://github.com/googleapis/google-resumable-media-python/issues/395)) ([a8d56bc](https://github.com/googleapis/google-resumable-media-python/commit/a8d56bc7f51b9b75f5735b241b4bcdb5b2c62fd6))
* Introduce compatibility with native namespace packages ([#385](https://github.com/googleapis/google-resumable-media-python/issues/385)) ([cdd7a5e](https://github.com/googleapis/google-resumable-media-python/commit/cdd7a5ec140d9e4f77fa7201d9d6dd289f82dabf))


### Bug Fixes

* Add google-auth to aiohttp extra ([#386](https://github.com/googleapis/google-resumable-media-python/issues/386)) ([30c2ebd](https://github.com/googleapis/google-resumable-media-python/commit/30c2ebdb18be28cae522df9fd2af45f1cb2b406d))

## [2.5.0](https://github.com/googleapis/google-resumable-media-python/compare/v2.4.1...v2.5.0) (2023-04-21)


### Features

* Add support to retry known connection errors ([#375](https://github.com/googleapis/google-resumable-media-python/issues/375)) ([147e845](https://github.com/googleapis/google-resumable-media-python/commit/147e8458578cc500dfe98d9ac7a447332fb9c52b))

## [2.4.1](https://github.com/googleapis/google-resumable-media-python/compare/v2.4.0...v2.4.1) (2023-01-06)


### Bug Fixes

* Avoid validating checksums for partial responses ([#361](https://github.com/googleapis/google-resumable-media-python/issues/361)) ([354287f](https://github.com/googleapis/google-resumable-media-python/commit/354287f023c34e269ca5ef0b24b28b9c37ae9dd7))

## [2.4.0](https://github.com/googleapis/google-resumable-media-python/compare/v2.3.3...v2.4.0) (2022-09-29)


### Features

* Handle interrupted downloads with decompressive transcoding ([#346](https://github.com/googleapis/google-resumable-media-python/issues/346)) ([f4d26b7](https://github.com/googleapis/google-resumable-media-python/commit/f4d26b7317bf452c8bc4e7f140f9d10e088b8644))


### Bug Fixes

* Allow recover to check the status of upload regardless of state ([#343](https://github.com/googleapis/google-resumable-media-python/issues/343)) ([3599267](https://github.com/googleapis/google-resumable-media-python/commit/3599267df25e54be8d1aa07a673f74d7230aa0b7))
* Require python 3.7+ ([#337](https://github.com/googleapis/google-resumable-media-python/issues/337)) ([942665f](https://github.com/googleapis/google-resumable-media-python/commit/942665f1bb01d2efb604e0be52736690160973b9))
* Use unittest.mock ([#329](https://github.com/googleapis/google-resumable-media-python/issues/329)) ([82f9769](https://github.com/googleapis/google-resumable-media-python/commit/82f9769f3368404d1854dd22eeed34eeb25ea835))


### Documentation

* Fix changelog header to consistent size ([#331](https://github.com/googleapis/google-resumable-media-python/issues/331)) ([7b1dc9c](https://github.com/googleapis/google-resumable-media-python/commit/7b1dc9cc547d6cff7d1340d5b688d1cb0c492e2a))

## [2.3.3](https://github.com/googleapis/google-resumable-media-python/compare/v2.3.2...v2.3.3) (2022-05-05)


### Bug Fixes

* retry client side requests timeout ([#319](https://github.com/googleapis/google-resumable-media-python/issues/319)) ([d0649c7](https://github.com/googleapis/google-resumable-media-python/commit/d0649c7509f4a45623d8676cbc37690864e1ca2f))

## [2.3.2](https://github.com/googleapis/google-resumable-media-python/compare/v2.3.1...v2.3.2) (2022-03-08)


### Bug Fixes

* append existing headers in prepare_initiate_request ([#314](https://github.com/googleapis/google-resumable-media-python/issues/314)) ([dfaa317](https://github.com/googleapis/google-resumable-media-python/commit/dfaa31703b1bdce80012622687f8cb02db7f4570))

## [2.3.1](https://github.com/googleapis/google-resumable-media-python/compare/v2.3.0...v2.3.1) (2022-03-03)


### Bug Fixes

* include existing headers in prepare request ([#309](https://github.com/googleapis/google-resumable-media-python/issues/309)) ([010680b](https://github.com/googleapis/google-resumable-media-python/commit/010680b942365bb8bcfd326015a3d99a9f0ec825))

## [2.3.0](https://github.com/googleapis/google-resumable-media-python/compare/v2.2.1...v2.3.0) (2022-02-11)


### Features

* safely resume interrupted downloads ([#294](https://github.com/googleapis/google-resumable-media-python/issues/294)) ([b363329](https://github.com/googleapis/google-resumable-media-python/commit/b36332915a783ef748bc6f8126bc6b41ee9a044d))

## [2.2.1](https://github.com/googleapis/google-resumable-media-python/compare/v2.2.0...v2.2.1) (2022-02-09)


### Bug Fixes

* don't overwrite user-agent on requests ([42b380e](https://github.com/googleapis/google-resumable-media-python/commit/42b380e9ec7aba59aa205f8f354764c9b7e35f19))

## [2.2.0](https://github.com/googleapis/google-resumable-media-python/compare/v2.1.0...v2.2.0) (2022-01-28)


### Features

* add 'py.typed' declaration file ([#287](https://github.com/googleapis/google-resumable-media-python/issues/287)) ([cee4164](https://github.com/googleapis/google-resumable-media-python/commit/cee416449701b72e7fd532585a1f739b02b6ab32))
* add support for signed resumable upload URLs ([#290](https://github.com/googleapis/google-resumable-media-python/issues/290)) ([e1290f5](https://github.com/googleapis/google-resumable-media-python/commit/e1290f523808c7ef5be7dd335a5c94cd1739e6e3))


### Bug Fixes

* add user-agent on requests ([#295](https://github.com/googleapis/google-resumable-media-python/issues/295)) ([e107a0c](https://github.com/googleapis/google-resumable-media-python/commit/e107a0cac7ca367015a025a6872a8ad28c7ff15c))

## [2.1.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v2.0.3...v2.1.0) (2021-10-20)


### Features

* add support for Python 3.10 ([#279](https://www.github.com/googleapis/google-resumable-media-python/issues/279)) ([4dbd14a](https://www.github.com/googleapis/google-resumable-media-python/commit/4dbd14aed14b87d4d288584a59e8ea11beccaf97))


### Bug Fixes

* Include ConnectionError and urllib3 exception as retriable ([#282](https://www.github.com/googleapis/google-resumable-media-python/issues/282)) ([d33465f](https://www.github.com/googleapis/google-resumable-media-python/commit/d33465fc047f4188dd967871ea93255aefd4ac2e))

## [2.0.3](https://www.github.com/googleapis/google-resumable-media-python/compare/v2.0.2...v2.0.3) (2021-09-20)


### Bug Fixes

* add REQUEST_TIMEOUT 408 as retryable code ([#270](https://www.github.com/googleapis/google-resumable-media-python/issues/270)) ([d0ad0aa](https://www.github.com/googleapis/google-resumable-media-python/commit/d0ad0aade5f4e7c8efed4f4339fc31fb3304fd3c))
* un-pin google-crc32c ([#267](https://www.github.com/googleapis/google-resumable-media-python/issues/267)) ([6b03a13](https://www.github.com/googleapis/google-resumable-media-python/commit/6b03a13717e1d4d18186bdf2146d5b452d9e3237))

## [2.0.2](https://www.github.com/googleapis/google-resumable-media-python/compare/v2.0.1...v2.0.2) (2021-09-02)


### Bug Fixes

* temporarily pin google-crc32c to 1.1.2 to mitigate upstream issue affecting OS X Big Sur ([#264](https://www.github.com/googleapis/google-resumable-media-python/issues/264)) ([9fa344f](https://www.github.com/googleapis/google-resumable-media-python/commit/9fa344f42a99db1af27b8ca126a2ea6b3c01d837))

## [2.0.1](https://www.github.com/googleapis/google-resumable-media-python/compare/v2.0.0...v2.0.1) (2021-08-30)


### Bug Fixes

* check if retry is allowed after retry wait calculation ([#258](https://www.github.com/googleapis/google-resumable-media-python/issues/258)) ([00ccf71](https://www.github.com/googleapis/google-resumable-media-python/commit/00ccf7120251d3899c8d0c2eccdf3b177b5b3742))
* do not mark upload download instances invalid with retriable error codes ([#261](https://www.github.com/googleapis/google-resumable-media-python/issues/261)) ([a1c5f7d](https://www.github.com/googleapis/google-resumable-media-python/commit/a1c5f7d0e3ce48d8d6eb8aced31707a881f7ee96))

## [2.0.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v2.0.0-b1...v2.0.0) (2021-08-19)


### ⚠ BREAKING CHANGES

* drop Python 2.7 support ([#229](https://www.github.com/googleapis/google-resumable-media-python/issues/229)) ([af10d4b](https://www.github.com/googleapis/google-resumable-media-python/commit/af10d4b9a5a3f97f08cf1c634f13b0fb24fc83b3))

### Bug Fixes

* retry ConnectionError and similar errors that occur mid-download ([#251](https://www.github.com/googleapis/google-resumable-media-python/issues/251)) ([bb3ec13](https://www.github.com/googleapis/google-resumable-media-python/commit/bb3ec13f5dbc0e26795cebce957247ecbb525f7b))

## [2.0.0b1](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.3.3...v2.0.0b1) (2021-08-02)


### ⚠ BREAKING CHANGES

* drop Python 2.7 support ([#229](https://www.github.com/googleapis/google-resumable-media-python/issues/229)) ([af10d4b](https://www.github.com/googleapis/google-resumable-media-python/commit/af10d4b9a5a3f97f08cf1c634f13b0fb24fc83b3))

## [1.3.3](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.3.2...v1.3.3) (2021-07-30)


### Reverts

* revert "fix: add retry coverage to the streaming portion of a download" ([#245](https://www.github.com/googleapis/google-resumable-media-python/issues/245)) ([98673d0](https://www.github.com/googleapis/google-resumable-media-python/commit/98673d01e90de8ea8fb101348dd9d15ae4e0531d))

## [1.3.2](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.3.1...v1.3.2) (2021-07-27)


### Bug Fixes

* add retry coverage to the streaming portion of a download ([#241](https://www.github.com/googleapis/google-resumable-media-python/issues/241)) ([cc1f07c](https://www.github.com/googleapis/google-resumable-media-python/commit/cc1f07c241876dba62927f841b1a61aa2554996a))

## [1.3.1](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.3.0...v1.3.1) (2021-06-18)


### Bug Fixes

* **deps:** require six>=1.4.0 ([#194](https://www.github.com/googleapis/google-resumable-media-python/issues/194)) ([a840691](https://www.github.com/googleapis/google-resumable-media-python/commit/a84069127cd48f68e3a56b3df16c63ff494637f3))

## [1.3.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.2.0...v1.3.0) (2021-05-18)


### Features

* allow RetryStrategy to be configured with a custom initial wait and multiplier ([#216](https://www.github.com/googleapis/google-resumable-media-python/issues/216)) ([579a54b](https://www.github.com/googleapis/google-resumable-media-python/commit/579a54b56dd7045da7af0dcacacfa5833c1cfa87))


### Documentation

* address terminology ([#201](https://www.github.com/googleapis/google-resumable-media-python/issues/201)) ([a88cfb9](https://www.github.com/googleapis/google-resumable-media-python/commit/a88cfb9637015839307ea4e967eef6f232c007a5))

## [1.2.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.1.0...v1.2.0) (2020-12-14)


### Features

* add support for Python 3.9, drop support for Python 3.5 ([#191](https://www.github.com/googleapis/google-resumable-media-python/issues/191)) ([76839fb](https://www.github.com/googleapis/google-resumable-media-python/commit/76839fb9bf6fd57ec6bea7b82aeaa1b3fe6f4464)), closes [#189](https://www.github.com/googleapis/google-resumable-media-python/issues/189)
* add retries for 'requests.ConnectionError' ([#186](https://www.github.com/googleapis/google-resumable-media-python/issues/186)) ([0d76eac](https://www.github.com/googleapis/google-resumable-media-python/commit/0d76eac29758d119e292fb27ab8000432944a938))

## [1.1.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v1.0.0...v1.1.0) (2020-10-05)


### Features

* add _async_resumable_media experimental support ([#179](https://www.github.com/googleapis/google-resumable-media-python/issues/179)) ([03c11ba](https://www.github.com/googleapis/google-resumable-media-python/commit/03c11bae0c43830d539f1e0adcc837a6c88f4e2e)), closes [#160](https://www.github.com/googleapis/google-resumable-media-python/issues/160) [#153](https://www.github.com/googleapis/google-resumable-media-python/issues/153) [#176](https://www.github.com/googleapis/google-resumable-media-python/issues/176) [#178](https://www.github.com/googleapis/google-resumable-media-python/issues/178)


### Bug Fixes

* allow space in checksum header ([#170](https://www.github.com/googleapis/google-resumable-media-python/issues/170)) ([224fc98](https://www.github.com/googleapis/google-resumable-media-python/commit/224fc9858b903396e0f94801757814e47cff45e7)), closes [#169](https://www.github.com/googleapis/google-resumable-media-python/issues/169)
* **lint:** blacken 5 files ([#171](https://www.github.com/googleapis/google-resumable-media-python/issues/171)) ([cdea3ee](https://www.github.com/googleapis/google-resumable-media-python/commit/cdea3eec76c7586a66b1641bca906f630d915c0e))

## [1.0.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v0.7.1...v1.0.0) (2020-08-24)


### Features

* bump 'google-crc32c >= 1.0' ([#162](https://www.github.com/googleapis/google-resumable-media-python/issues/162)) ([eaf9faa](https://www.github.com/googleapis/google-resumable-media-python/commit/eaf9faa80dc51bd719161557584e151b30c7e082))

## [0.7.1](https://www.github.com/googleapis/google-resumable-media-python/compare/v0.7.0...v0.7.1) (2020-08-06)


### Dependencies
* pin 'google-crc32c < 0.2dev' ([#160](https://www.github.com/googleapis/google-resumable-media-python/issues/160)) ([52a322d](https://www.github.com/googleapis/google-resumable-media-python/commit/52a322d478e074a646e20d92ca9b2457c6e03941))

### Documentation

* update docs build (via synth) ([#155](https://www.github.com/googleapis/google-resumable-media-python/issues/155)) ([1c33de4](https://www.github.com/googleapis/google-resumable-media-python/commit/1c33de475585e27bba2bcb7ea5dbead9e0214660))
* use googleapis.dev docs link ([#149](https://www.github.com/googleapis/google-resumable-media-python/issues/149)) ([90bd0c1](https://www.github.com/googleapis/google-resumable-media-python/commit/90bd0c1a6a88b53c2049cd75cf73129fcecde5de))

## [0.7.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v0.6.0...v0.7.0) (2020-07-23)


### Features

* add configurable checksum support for uploads ([#139](https://www.github.com/googleapis/google-resumable-media-python/issues/139)) ([68264f8](https://www.github.com/googleapis/google-resumable-media-python/commit/68264f811473a5aa06102912ea8d454b6bb59307))


### Bug Fixes

* accept `201 Created` as valid upload response ([#141](https://www.github.com/googleapis/google-resumable-media-python/issues/141)) ([00d280e](https://www.github.com/googleapis/google-resumable-media-python/commit/00d280e116d69f7f8d8a4b970bb1176e338f9ce0)), closes [#125](https://www.github.com/googleapis/google-resumable-media-python/issues/125) [#124](https://www.github.com/googleapis/google-resumable-media-python/issues/124)

## [0.6.0](https://www.github.com/googleapis/google-resumable-media-python/compare/v0.5.1...v0.6.0) (2020-07-07)


### Features

* add customizable timeouts to upload/download methods ([#116](https://www.github.com/googleapis/google-resumable-media-python/issues/116)) ([5310921](https://www.github.com/googleapis/google-resumable-media-python/commit/5310921dacf5232ad58a5d6e324f3df6b320eca7))
* add configurable crc32c checksumming for downloads ([#135](https://www.github.com/googleapis/google-resumable-media-python/issues/135)) ([db31bf5](https://www.github.com/googleapis/google-resumable-media-python/commit/db31bf56560109f19b49cf38c494ecacfa74b0b2))
* add templates for python samples projects ([#506](https://www.github.com/googleapis/google-resumable-media-python/issues/506)) ([#132](https://www.github.com/googleapis/google-resumable-media-python/issues/132)) ([8e60cc4](https://www.github.com/googleapis/google-resumable-media-python/commit/8e60cc45d4fefe63d7353e978d15d6e238b7a1a1))


### Documentation

* update client_documentation link ([#136](https://www.github.com/googleapis/google-resumable-media-python/issues/136)) ([063b4f9](https://www.github.com/googleapis/google-resumable-media-python/commit/063b4f9f3ea3dff850d9ae46b2abf25d08312320))

## [0.5.1](https://www.github.com/googleapis/google-resumable-media-python/compare/v0.5.0...v0.5.1) (2020-05-26)


### Bug Fixes

* fix failing unit tests by dropping Python 3.4, add Python 3.8 ([#118](https://www.github.com/googleapis/google-resumable-media-python/issues/118)) ([1edb974](https://www.github.com/googleapis/google-resumable-media-python/commit/1edb974175d16c9f542fe84dd6bbfa2d70115d48))
* fix upload_from_file size greater than multipart ([#129](https://www.github.com/googleapis/google-resumable-media-python/issues/129)) ([07dd9c2](https://www.github.com/googleapis/google-resumable-media-python/commit/07dd9c26a7eff9b2b43d32636faf9a5aa151fed5))
* Generated file update for docs and testing templates. ([#127](https://www.github.com/googleapis/google-resumable-media-python/issues/127)) ([bc7a5a9](https://www.github.com/googleapis/google-resumable-media-python/commit/bc7a5a9b66e16d08778ace96845bb429b94ddbce))

## 0.5.0

10-28-2019 09:16 PDT


### New Features
- Add raw download classes. ([#109](https://github.com/googleapis/google-resumable-media-python/pull/109))

### Documentation
- Update Sphinx inventory URL for requests library. ([#108](https://github.com/googleapis/google-resumable-media-python/pull/108))

### Internal / Testing Changes
- Initial synth. ([#105](https://github.com/googleapis/google-resumable-media-python/pull/105))
- Remove CircleCI. ([#102](https://github.com/googleapis/google-resumable-media-python/pull/102))

## 0.4.1

09-16-2019 17:59 PDT


### Implementation Changes
- Revert "Always use raw response data. ([#87](https://github.com/googleapis/google-resumable-media-python/pull/87))" ([#103](https://github.com/googleapis/google-resumable-media-python/pull/103))

### Internal / Testing Changes
- Add black. ([#94](https://github.com/googleapis/google-resumable-media-python/pull/94))

## 0.4.0

09-05-2019 11:59 PDT

### Backward-Compatibility Note

The change to use raw response data (PR
[#87](https://github.com/googleapis/google-resumable-media-python/pull/87))
might break the hypothetical usecase of downloading a blob marked with
`Content-Encoding: gzip` and expecting to get the expanded data.

### Implementation Changes
- Require 200 response for initial resumable upload request. ([#95](https://github.com/googleapis/google-resumable-media-python/pull/95))
- Use `response` as variable for object returned from `http_request`. ([#98](https://github.com/googleapis/google-resumable-media-python/pull/98))
- Further DRY request dependency pins. ([#96](https://github.com/googleapis/google-resumable-media-python/pull/96))
- Finish download on seeing 416 response with zero byte range. ([#86](https://github.com/googleapis/google-resumable-media-python/pull/86))
- Always use raw response data. ([#87](https://github.com/googleapis/google-resumable-media-python/pull/87))

### Dependencies
- Drop runtime dependency check on `requests`. ([#97](https://github.com/googleapis/google-resumable-media-python/pull/97))

### Documentation
- Update docs after release ([#93](https://github.com/googleapis/google-resumable-media-python/pull/93))

## 0.3.3

08-23-2019 14:15 PDT

### Implementation Changes
- Add a default timeout for the http_request method ([#88](https://github.com/googleapis/google-resumable-media-python/pull/88))
- DRY 'requests' pin; don't shadow exception. ([#83](https://github.com/googleapis/google-resumable-media-python/pull/83))
- Drop a hardcoded value in an error message. ([#48](https://github.com/googleapis/google-resumable-media-python/pull/48))

### Documentation
- Reconstruct 'CHANGELOG.md' from pre-releasetool era releases. ([#66](https://github.com/googleapis/google-resumable-media-python/pull/66))

### Internal / Testing Changes
- Use Kokoro for CI ([#90](https://github.com/googleapis/google-resumable-media-python/pull/90))
- Renovate: preserve semver ranges. ([#82](https://github.com/googleapis/google-resumable-media-python/pull/82))
- Add renovate.json ([#79](https://github.com/googleapis/google-resumable-media-python/pull/79))
- Fix systest bitrot. ([#77](https://github.com/googleapis/google-resumable-media-python/pull/77))
- Fix docs build redux. ([#75](https://github.com/googleapis/google-resumable-media-python/pull/75))
- Update to new nox ([#57](https://github.com/googleapis/google-resumable-media-python/pull/57))

## 0.3.2

2018-12-17 17:31 PST

### Implementation Changes
- Using `str` instead of `repr` for multipart boundary.

### Dependencies
- Making `requests` a strict dependency for the `requests` subpackage.

### Documentation
- Announce deprecation of Python 2.7 ([#51](https://github.com/googleapis/google-resumable-media-python/pull/51))
- Fix broken redirect after repository move
- Updating generated static content in docs.

### Internal / Testing Changes
- Modify file not found test to look for the correct error message
- Harden tests so they can run with debug logging statements
- Add Appveyor support. ([#40](https://github.com/googleapis/google-resumable-media-python/pull/40))
- Mark the version in `main` as `.dev1`.


## 0.3.1

2017-10-20

### Implementation Changes

- Add requests/urllib3 work-around for intercepting gzipped bytes. ([#36](https://github.com/googleapis/google-resumable-media-python/pull/36))

### Internal / Testing Changes
- Re-factor `system/requests/test_download.py`. ([#35](https://github.com/googleapis/google-resumable-media-python/pull/35))


## 0.3.0

2017-10-13

### Implementation Changes

- Add checksum validation for non-chunked non-composite downloads. ([#32](https://github.com/googleapis/google-resumable-media-python/pull/32))

### Dependencies

- Add `requests` extra to `setup.py`. ([#30](https://github.com/googleapis/google-resumable-media-python/pull/30))

### Documentation

- Update generated docs, due to updated `objects.inf` from reequests.


## 0.2.3

2017-08-07

### Implementation Changes

- Allow empty files to be uploaded. ([#25](https://github.com/googleapis/google-resumable-media-python/pull/25))


## 0.2.2

2017-08-01

### Implementation Changes

- Swap the order of `_write_to_stream()` / `_process_response()` in `requests` download. ([#24](https://github.com/googleapis/google-resumable-media-python/pull/24))
- Use requests `iter_content()` to avoid storing response body in RAM. ([#21](https://github.com/googleapis/google-resumable-media-python/pull/21))
- Add optional stream argument to DownloadBase. ([#20](https://github.com/googleapis/google-resumable-media-python/pull/20))


## 0.2.1

2017-07-21

### Implementation Changes

- Drop usage of `size` to measure (resumable) bytes uploaded. ([#18](https://github.com/googleapis/google-resumable-media-python/pull/18))
- Use explicit u prefix on unicode strings. ([#16](https://github.com/googleapis/google-resumable-media-python/pull/16))

### Internal / Testing Changes

- Update `author_email1` to official mailing list.

## 0.2.0

2017-07-18

### Implementation Changes

- Ensure passing  unicode to `json.loads()` rather than `bytes`. ([#13](https://github.com/googleapis/google-resumable-media-python/pull/13))
- Add `MANIFEST.in` to repository. ([#9](https://github.com/googleapis/google-resumable-media-python/pull/9))
- Move contents of exceptions module into common.

### Documentation

- Update docs after latest version of Sphinx. ([#11](https://github.com/googleapis/google-resumable-media-python/pull/11))
- Update `custom_html_writer` after Sphinx update removed a class. ([#10](https://github.com/googleapis/google-resumable-media-python/pull/10))

### Internal / Testing Changes

- Use nox `session.skip` (instead of ValueError) for system tests. ([#14](https://github.com/googleapis/google-resumable-media-python/pull/14))


## 0.1.1

2017-05-05


### Implementation Changes

- Add `common.RetryStrategy` class; us it in `wait_and_retry`.
- Rename `constants` module -> `common`.


## 0.1.0

2017-05-03

### Implementation Changes

- Pass `total_bytes` in `requests.ResumableUpload.initiate`.


## 0.0.5

2017-05-02

### New Features

- Add support for resumable uploads of unknown size. ([#6](https://github.com/googleapis/google-resumable-media-python/pull/6))


## 0.0.4

2017-04-28

### Implementation Changes

- Refactor upload / download support into public, transport-agnostic classes and private, `requests`-specific implementations.


## 0.0.3

2017-04-24

### New Features

- Add automatic retries for 429, 500, 502, 503 and 504 error responses. ([#4](https://github.com/googleapis/google-resumable-media-python/pull/4))


## 0.0.2

2017-04-24

### New Features

- Add optional `headers` to upload / download classes.

### Documentation

- Automate documentation builds via CircleCI.


## 0.0.1

2017-04-21

- Initial public release.
