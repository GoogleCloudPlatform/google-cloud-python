# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-eventarc/#history

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.21.0...google-cloud-eventarc-v1.22.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.20.0...google-cloud-eventarc-v1.21.0) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.19.0...google-cloud-eventarc-v1.20.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.18.0...google-cloud-eventarc-v1.19.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.17.0...google-cloud-eventarc-v1.18.0) (2025-12-04)


### Features

* add wide-scope Eventarc GoogleApiSource flags ([d4e6a4ab7b428e821a59b053c689343b5f5511f9](https://github.com/googleapis/google-cloud-python/commit/d4e6a4ab7b428e821a59b053c689343b5f5511f9))
* add Eventarc Trigger RetryPolicy ([d4e6a4ab7b428e821a59b053c689343b5f5511f9](https://github.com/googleapis/google-cloud-python/commit/d4e6a4ab7b428e821a59b053c689343b5f5511f9))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.16.0...google-cloud-eventarc-v1.17.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.15.3...google-cloud-eventarc-v1.16.0) (2025-09-24)


### Documentation

* [google-cloud-eventarc] correct some comments  ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))


### Features

* [google-cloud-eventarc] add new fields to Eventarc resources  ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))


### Bug Fixes

* [google-cloud-eventarc] upgrade gRPC service registration func An update to Go gRPC Protobuf generation will change service
registration function signatures to use an interface instead of a
concrete type in generated .pb.go service files. This change should
affect very few client library users. See release notes advisories in
https://github.com/googleapis/google-cloud-go/pull/11025. ([26730096e491346f02af2a82138224a110485e74](https://github.com/googleapis/google-cloud-python/commit/26730096e491346f02af2a82138224a110485e74))

## [1.15.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.15.2...google-cloud-eventarc-v1.15.3) (2025-06-11)


### Documentation

* Update import statement example in README ([821bdb1](https://github.com/googleapis/google-cloud-python/commit/821bdb1d108c8e77a7a576557aa95d4b9c943e12))

## [1.15.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.15.1...google-cloud-eventarc-v1.15.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.15.0...google-cloud-eventarc-v1.15.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([16e14c8](https://github.com/googleapis/google-cloud-python/commit/16e14c8d547864360dcab45d90e9e55169204fc6))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.14.0...google-cloud-eventarc-v1.15.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.13.2...google-cloud-eventarc-v1.14.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.13.1...google-cloud-eventarc-v1.13.2) (2024-11-14)


### Documentation

* Fixed typo in comments in Eventarc protos ([#13271](https://github.com/googleapis/google-cloud-python/issues/13271)) ([0dc1fc9](https://github.com/googleapis/google-cloud-python/commit/0dc1fc9a71a7f7ba3fe62abc7a13386e6b6c3be2))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.13.0...google-cloud-eventarc-v1.13.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.12.0...google-cloud-eventarc-v1.13.0) (2024-10-31)


### Features

* Publish Eventarc Advanced protos ([e90120b](https://github.com/googleapis/google-cloud-python/commit/e90120b0661c17acfdeec5f3edb37c4155c19aa6))


### Documentation

* Clarified multiple comments in Eventarc Standard protos ([e90120b](https://github.com/googleapis/google-cloud-python/commit/e90120b0661c17acfdeec5f3edb37c4155c19aa6))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.11.5...google-cloud-eventarc-v1.12.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [1.11.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.11.4...google-cloud-eventarc-v1.11.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [1.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.11.3...google-cloud-eventarc-v1.11.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.11.2...google-cloud-eventarc-v1.11.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12384](https://github.com/googleapis/google-cloud-python/issues/12384)) ([c69966f](https://github.com/googleapis/google-cloud-python/commit/c69966fa7aac2cba4e22513e4a053b3754f8ea5e))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.11.1...google-cloud-eventarc-v1.11.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12283](https://github.com/googleapis/google-cloud-python/issues/12283)) ([f20b41a](https://github.com/googleapis/google-cloud-python/commit/f20b41ac35b02a40135b83edfe819ff7a355ab21))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.11.0...google-cloud-eventarc-v1.11.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.10.0...google-cloud-eventarc-v1.11.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.9.3...google-cloud-eventarc-v1.10.0) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [1.9.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.9.2...google-cloud-eventarc-v1.9.3) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [1.9.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-eventarc-v1.9.1...google-cloud-eventarc-v1.9.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [1.9.1](https://github.com/googleapis/python-eventarc/compare/v1.9.0...v1.9.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#200](https://github.com/googleapis/python-eventarc/issues/200)) ([b0be428](https://github.com/googleapis/python-eventarc/commit/b0be428683dc09184246313ed0e34ad097e7cc4b))

## [1.9.0](https://github.com/googleapis/python-eventarc/compare/v1.8.1...v1.9.0) (2023-02-09)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#194](https://github.com/googleapis/python-eventarc/issues/194)) ([1b7840c](https://github.com/googleapis/python-eventarc/commit/1b7840c6bfa128b5b43a4554c8b6d20bf20b0dca))

## [1.8.1](https://github.com/googleapis/python-eventarc/compare/v1.8.0...v1.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([2c7b15b](https://github.com/googleapis/python-eventarc/commit/2c7b15b9368dab65cd33fd20011d63df5cf0b032))


### Documentation

* Add documentation for enums ([2c7b15b](https://github.com/googleapis/python-eventarc/commit/2c7b15b9368dab65cd33fd20011d63df5cf0b032))

## [1.8.0](https://github.com/googleapis/python-eventarc/compare/v1.7.0...v1.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#186](https://github.com/googleapis/python-eventarc/issues/186)) ([2e3ef53](https://github.com/googleapis/python-eventarc/commit/2e3ef531c0a0dd9c83dafbe8c6b12f5ee1e15387))

## [1.7.0](https://github.com/googleapis/python-eventarc/compare/v1.6.3...v1.7.0) (2022-12-15)


### Features

* Add CMEK support to Eventarc client library ([6ba2726](https://github.com/googleapis/python-eventarc/commit/6ba27265ef643fc0d6e85994d15b1dab5ce496e8))
* Add support for `google.cloud.eventarc.__version__` ([6ba2726](https://github.com/googleapis/python-eventarc/commit/6ba27265ef643fc0d6e85994d15b1dab5ce496e8))
* Add typing to proto.Message based class attributes ([6ba2726](https://github.com/googleapis/python-eventarc/commit/6ba27265ef643fc0d6e85994d15b1dab5ce496e8))
* Update Eventarc Channel to support custom events ([6ba2726](https://github.com/googleapis/python-eventarc/commit/6ba27265ef643fc0d6e85994d15b1dab5ce496e8))


### Bug Fixes

* Add dict typing for client_options ([6ba2726](https://github.com/googleapis/python-eventarc/commit/6ba27265ef643fc0d6e85994d15b1dab5ce496e8))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([cc353d1](https://github.com/googleapis/python-eventarc/commit/cc353d199aa23ccdd5b6aecbf98ce077538e6c3c))
* Drop usage of pkg_resources ([cc353d1](https://github.com/googleapis/python-eventarc/commit/cc353d199aa23ccdd5b6aecbf98ce077538e6c3c))
* Fix timeout default values ([cc353d1](https://github.com/googleapis/python-eventarc/commit/cc353d199aa23ccdd5b6aecbf98ce077538e6c3c))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([6ba2726](https://github.com/googleapis/python-eventarc/commit/6ba27265ef643fc0d6e85994d15b1dab5ce496e8))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([cc353d1](https://github.com/googleapis/python-eventarc/commit/cc353d199aa23ccdd5b6aecbf98ce077538e6c3c))

## [1.6.3](https://github.com/googleapis/python-eventarc/compare/v1.6.2...v1.6.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#176](https://github.com/googleapis/python-eventarc/issues/176)) ([1a1a64d](https://github.com/googleapis/python-eventarc/commit/1a1a64d5450652c451ff59eb5041e9f81aefc056))

## [1.6.2](https://github.com/googleapis/python-eventarc/compare/v1.6.1...v1.6.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#174](https://github.com/googleapis/python-eventarc/issues/174)) ([0dcf87b](https://github.com/googleapis/python-eventarc/commit/0dcf87b9f81283e2bb45ef0a7f7ab71b91d70382))

## [1.6.1](https://github.com/googleapis/python-eventarc/compare/v1.6.0...v1.6.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#159](https://github.com/googleapis/python-eventarc/issues/159)) ([44962a0](https://github.com/googleapis/python-eventarc/commit/44962a03eba21e3445af42700f37e2063d9d9b95))
* **deps:** require proto-plus >= 1.22.0 ([44962a0](https://github.com/googleapis/python-eventarc/commit/44962a03eba21e3445af42700f37e2063d9d9b95))

## [1.6.0](https://github.com/googleapis/python-eventarc/compare/v1.5.1...v1.6.0) (2022-07-14)


### Features

* add audience parameter ([535338c](https://github.com/googleapis/python-eventarc/commit/535338c0130d289b390ef0dd17bf8e2bbbc15f3c))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#150](https://github.com/googleapis/python-eventarc/issues/150)) ([535338c](https://github.com/googleapis/python-eventarc/commit/535338c0130d289b390ef0dd17bf8e2bbbc15f3c))
* require python 3.7+ ([#152](https://github.com/googleapis/python-eventarc/issues/152)) ([0db4414](https://github.com/googleapis/python-eventarc/commit/0db4414f426b81be060e4fc49d829d4304c76530))

## [1.5.1](https://github.com/googleapis/python-eventarc/compare/v1.5.0...v1.5.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#142](https://github.com/googleapis/python-eventarc/issues/142)) ([75a17a9](https://github.com/googleapis/python-eventarc/commit/75a17a963552411e00380c44e46753517af6b83f))


### Documentation

* fix changelog header to consistent size ([#141](https://github.com/googleapis/python-eventarc/issues/141)) ([8a7b8b1](https://github.com/googleapis/python-eventarc/commit/8a7b8b1cb8d3cd52b39d3c621f1899a042cdd690))

## [1.5.0](https://github.com/googleapis/python-eventarc/compare/v1.4.2...v1.5.0) (2022-05-19)


### Features

* Add Provider resources ([#109](https://github.com/googleapis/python-eventarc/issues/109)) ([11be2a5](https://github.com/googleapis/python-eventarc/commit/11be2a5ee982a01ee974cb19f8efc9aa8e90be93))

## [1.4.2](https://github.com/googleapis/python-eventarc/compare/v1.4.1...v1.4.2) (2022-04-14)


### Bug Fixes

* fix type in docstring for map fields ([#97](https://github.com/googleapis/python-eventarc/issues/97)) ([2865664](https://github.com/googleapis/python-eventarc/commit/2865664e1cd4c75ee7ec9f3dbee78a7c1eb83d91))

## [1.4.1](https://github.com/googleapis/python-eventarc/compare/v1.4.0...v1.4.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#84](https://github.com/googleapis/python-eventarc/issues/84)) ([988eff8](https://github.com/googleapis/python-eventarc/commit/988eff8b621c91bb0e6b3844e36d5b918b9056b6))

## [1.4.0](https://github.com/googleapis/python-eventarc/compare/v1.3.0...v1.4.0) (2022-02-04)


### Features

* Add Channel and ChannelConnection resources ([#72](https://github.com/googleapis/python-eventarc/issues/72)) ([4d89018](https://github.com/googleapis/python-eventarc/commit/4d8901835ea498cf9ba3fd289f5c078f1eafe7a7))

## [1.3.0](https://github.com/googleapis/python-eventarc/compare/v1.2.1...v1.3.0) (2022-02-03)


### Features

* add api key support ([#68](https://github.com/googleapis/python-eventarc/issues/68)) ([96e07bb](https://github.com/googleapis/python-eventarc/commit/96e07bbbfbb75aa16d33ee9e0984144949e5adc3))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([6bffd75](https://github.com/googleapis/python-eventarc/commit/6bffd757478617fe6ffff905f42fc702a0cb1262))

## [1.2.1](https://www.github.com/googleapis/python-eventarc/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([f509558](https://www.github.com/googleapis/python-eventarc/commit/f509558fe1967d7b0fc65c27a1a0f498bddaa915))
* **deps:** require google-api-core >= 1.28.0 ([f509558](https://www.github.com/googleapis/python-eventarc/commit/f509558fe1967d7b0fc65c27a1a0f498bddaa915))


### Documentation

* list oneofs in docstring ([f509558](https://www.github.com/googleapis/python-eventarc/commit/f509558fe1967d7b0fc65c27a1a0f498bddaa915))

## [1.2.0](https://www.github.com/googleapis/python-eventarc/compare/v1.1.0...v1.2.0) (2021-10-14)


### Features

* add support for python 3.10 ([#47](https://www.github.com/googleapis/python-eventarc/issues/47)) ([987360c](https://www.github.com/googleapis/python-eventarc/commit/987360ceded2027693e3ba148453f0ccfd50d2ce))

## [1.1.0](https://www.github.com/googleapis/python-eventarc/compare/v1.0.2...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#44](https://www.github.com/googleapis/python-eventarc/issues/44)) ([d732a44](https://www.github.com/googleapis/python-eventarc/commit/d732a44510336c7725809b797d082e4fc58c444c))

## [1.0.2](https://www.github.com/googleapis/python-eventarc/compare/v1.0.1...v1.0.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([406ac83](https://www.github.com/googleapis/python-eventarc/commit/406ac83dc4f568500c87ce8ff7b6aa61000252b3))

## [1.0.1](https://www.github.com/googleapis/python-eventarc/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([d940eea](https://www.github.com/googleapis/python-eventarc/commit/d940eeadf232c1c4e74e4f86a65367a2bf37f428))

## [1.0.0](https://www.github.com/googleapis/python-eventarc/compare/v0.2.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#25](https://www.github.com/googleapis/python-eventarc/issues/25)) ([bf70c36](https://www.github.com/googleapis/python-eventarc/commit/bf70c364be632440d3af774e7ddbdf83661a9432))

## [0.2.2](https://www.github.com/googleapis/python-eventarc/compare/v0.2.1...v0.2.2) (2021-07-30)


### Features

* add Samples section to CONTRIBUTING.rst ([#17](https://www.github.com/googleapis/python-eventarc/issues/17)) ([7e2cd4a](https://www.github.com/googleapis/python-eventarc/commit/7e2cd4a1fb857e9992425726bbc93ff2827fea49))


### Bug Fixes

* enable self signed jwt for grpc ([#21](https://www.github.com/googleapis/python-eventarc/issues/21)) ([c9af910](https://www.github.com/googleapis/python-eventarc/commit/c9af9101a3d16395b6ccdecdfd6676394741f686))


### Miscellaneous Chores

* release as 0.2.2 ([#22](https://www.github.com/googleapis/python-eventarc/issues/22)) ([0b26e99](https://www.github.com/googleapis/python-eventarc/commit/0b26e9953c2690f2c71d87681523afd6299af638))

## [0.2.1](https://www.github.com/googleapis/python-eventarc/compare/v0.2.0...v0.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#16](https://www.github.com/googleapis/python-eventarc/issues/16)) ([74277de](https://www.github.com/googleapis/python-eventarc/commit/74277dee9067a109e0a76c5fd9fbfd7cac696c80))

## [0.2.0](https://www.github.com/googleapis/python-eventarc/compare/v0.1.0...v0.2.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#9](https://www.github.com/googleapis/python-eventarc/issues/9)) ([2ce20e8](https://www.github.com/googleapis/python-eventarc/commit/2ce20e89a2d15b43e6f72bdcec1741013d1442f2))


### Bug Fixes

* disable always_use_jwt_access ([#13](https://www.github.com/googleapis/python-eventarc/issues/13)) ([d4db355](https://www.github.com/googleapis/python-eventarc/commit/d4db35506e0e0ef4feec76260b3eda4e6ebb8b38))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-eventarc/issues/1127)) ([#4](https://www.github.com/googleapis/python-eventarc/issues/4)) ([18a491d](https://www.github.com/googleapis/python-eventarc/commit/18a491de894bede3d1d675c0bbc884def6eaaf6d))

## 0.1.0 (2021-06-15)


### Features

* generate v1 ([bb2fbd0](https://www.github.com/googleapis/python-eventarc/commit/bb2fbd08b73879699d2c2df13693e15bafde7f65))
