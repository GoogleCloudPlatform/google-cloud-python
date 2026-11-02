# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-gsuiteaddons/#history

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.5.1...google-cloud-gsuiteaddons-v0.5.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.5.0...google-cloud-gsuiteaddons-v0.5.1) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.4.0...google-cloud-gsuiteaddons-v0.5.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.18...google-cloud-gsuiteaddons-v0.4.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.3.18](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.17...google-cloud-gsuiteaddons-v0.3.18) (2025-10-14)


### Features

* Add support for Python 3.14 ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))


### Bug Fixes

* Deprecate credentials_file argument ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))

## [0.3.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.16...google-cloud-gsuiteaddons-v0.3.17) (2025-06-11)


### Documentation

* Update import statement example in README ([821bdb1](https://github.com/googleapis/google-cloud-python/commit/821bdb1d108c8e77a7a576557aa95d4b9c943e12))

## [0.3.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.15...google-cloud-gsuiteaddons-v0.3.16) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.3.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.14...google-cloud-gsuiteaddons-v0.3.15) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [0.3.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.13...google-cloud-gsuiteaddons-v0.3.14) (2025-01-27)


### Documentation

* [google-cloud-gsuiteaddons] Minor documentation edits ([#13463](https://github.com/googleapis/google-cloud-python/issues/13463)) ([a2b6d21](https://github.com/googleapis/google-cloud-python/commit/a2b6d219070f85878ad0eac626cca565789d0764))

## [0.3.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.12...google-cloud-gsuiteaddons-v0.3.13) (2024-12-12)


### Features

* Add support for opt-in debug logging ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))

## [0.3.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.11...google-cloud-gsuiteaddons-v0.3.12) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [0.3.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.10...google-cloud-gsuiteaddons-v0.3.11) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13207](https://github.com/googleapis/google-cloud-python/issues/13207)) ([ceb9be8](https://github.com/googleapis/google-cloud-python/commit/ceb9be8f89ac7355d842bac1d77b2926eb0b649c))

## [0.3.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.9...google-cloud-gsuiteaddons-v0.3.10) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [0.3.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.8...google-cloud-gsuiteaddons-v0.3.9) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12867](https://github.com/googleapis/google-cloud-python/issues/12867)) ([3362176](https://github.com/googleapis/google-cloud-python/commit/33621762b989106ccf85adb538cf531c513a746c))

## [0.3.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.7...google-cloud-gsuiteaddons-v0.3.8) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12385](https://github.com/googleapis/google-cloud-python/issues/12385)) ([d50f4d0](https://github.com/googleapis/google-cloud-python/commit/d50f4d042774e2f12e9fe03459eae9ce91247df3))

## [0.3.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.6...google-cloud-gsuiteaddons-v0.3.7) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12307](https://github.com/googleapis/google-cloud-python/issues/12307)) ([be87bc4](https://github.com/googleapis/google-cloud-python/commit/be87bc4a33fe32a512448a42246c9873da88269f))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [0.3.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.5...google-cloud-gsuiteaddons-v0.3.6) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))

## [0.3.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.4...google-cloud-gsuiteaddons-v0.3.5) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [0.3.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gsuiteaddons-v0.3.3...google-cloud-gsuiteaddons-v0.3.4) (2023-12-07)


### Features

* Add support for python 3.12 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Introduce compatibility with native namespace packages ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Use `retry_async` instead of `retry` in async client ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))

## [0.3.3](https://github.com/googleapis/python-gsuiteaddons/compare/v0.3.2...v0.3.3) (2023-09-21)


### Documentation

* Minor formatting ([975e10e](https://github.com/googleapis/python-gsuiteaddons/commit/975e10ec8e76826ba6ce4ace7aa5c4cd59affc71))

## [0.3.2](https://github.com/googleapis/python-gsuiteaddons/compare/v0.3.1...v0.3.2) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#36](https://github.com/googleapis/python-gsuiteaddons/issues/36)) ([2c2bcde](https://github.com/googleapis/python-gsuiteaddons/commit/2c2bcde646d3b0e1550ea46e1008e7b7964f5f91))

## [0.3.1](https://github.com/googleapis/python-gsuiteaddons/compare/v0.3.0...v0.3.1) (2023-03-24)


### Documentation

* Fix formatting of request arg in docstring ([#28](https://github.com/googleapis/python-gsuiteaddons/issues/28)) ([825245f](https://github.com/googleapis/python-gsuiteaddons/commit/825245f81594feea5ee41ab64f4177e02d8f903d))

## [0.3.0](https://github.com/googleapis/python-gsuiteaddons/compare/v0.2.1...v0.3.0) (2023-02-19)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#22](https://github.com/googleapis/python-gsuiteaddons/issues/22)) ([3e96be1](https://github.com/googleapis/python-gsuiteaddons/commit/3e96be1efbd9b39f40db4ceb46bf7c228ab2de73))

## [0.2.1](https://github.com/googleapis/python-gsuiteaddons/compare/v0.2.0...v0.2.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([1fc871a](https://github.com/googleapis/python-gsuiteaddons/commit/1fc871ae26d3d1988e0d12063300f1b95c87c1f3))


### Documentation

* Add documentation for enums ([1fc871a](https://github.com/googleapis/python-gsuiteaddons/commit/1fc871ae26d3d1988e0d12063300f1b95c87c1f3))

## [0.2.0](https://github.com/googleapis/python-gsuiteaddons/compare/v0.1.1...v0.2.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#13](https://github.com/googleapis/python-gsuiteaddons/issues/13)) ([d30436f](https://github.com/googleapis/python-gsuiteaddons/commit/d30436fa933cbb007e86b9b0514bdb73d97bc7a4))

## [0.1.1](https://github.com/googleapis/python-gsuiteaddons/compare/v0.1.0...v0.1.1) (2022-12-08)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([e07fce5](https://github.com/googleapis/python-gsuiteaddons/commit/e07fce502d57a37fd901a97cce753ecbcf773143))
* Drop usage of pkg_resources ([e07fce5](https://github.com/googleapis/python-gsuiteaddons/commit/e07fce502d57a37fd901a97cce753ecbcf773143))
* Fix timeout default values ([e07fce5](https://github.com/googleapis/python-gsuiteaddons/commit/e07fce502d57a37fd901a97cce753ecbcf773143))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([e07fce5](https://github.com/googleapis/python-gsuiteaddons/commit/e07fce502d57a37fd901a97cce753ecbcf773143))

## 0.1.0 (2022-11-14)


### Features

* Generate v1 ([57d14c1](https://github.com/googleapis/python-gsuiteaddons/commit/57d14c10830674d1bcd314ee39d5eedfcc60159c))

## Changelog
