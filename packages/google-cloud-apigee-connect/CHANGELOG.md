# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-apigee-connect/#history

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.16.0...google-cloud-apigee-connect-v1.17.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.15.0...google-cloud-apigee-connect-v1.16.0) (2026-06-02)


### Features

* regenerate google-cloud-a packages (#17089) ([39c988267529419b03f808d7662ec521258571b4](https://github.com/googleapis/google-cloud-python/commit/39c988267529419b03f808d7662ec521258571b4))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.14.0...google-cloud-apigee-connect-v1.15.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.13.0...google-cloud-apigee-connect-v1.14.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.12.2...google-cloud-apigee-connect-v1.13.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.12.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.12.1...google-cloud-apigee-connect-v1.12.2) (2025-06-11)


### Documentation

* Update import statement example in README ([1562bb7](https://github.com/googleapis/google-cloud-python/commit/1562bb740c7cd56179e52185dde3c32af861de5e))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.12.0...google-cloud-apigee-connect-v1.12.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([a1b9294](https://github.com/googleapis/google-cloud-python/commit/a1b9294d0bf6e27c2a951d6df7faf7807dc5420b))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.11.0...google-cloud-apigee-connect-v1.12.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))
* Add support for reading selective GAPIC generation methods from service YAML ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.10.1...google-cloud-apigee-connect-v1.11.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [1.10.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.10.0...google-cloud-apigee-connect-v1.10.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([85c7512](https://github.com/googleapis/google-cloud-python/commit/85c7512bbdde2b9cc60b4ad42b8c36c4558a07a5))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.9.5...google-cloud-apigee-connect-v1.10.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13199](https://github.com/googleapis/google-cloud-python/issues/13199)) ([2fc3726](https://github.com/googleapis/google-cloud-python/commit/2fc372685731141ca1ed2a917dd18bacd79db88e))

## [1.9.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.9.4...google-cloud-apigee-connect-v1.9.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([c6eeae0](https://github.com/googleapis/google-cloud-python/commit/c6eeae00de802d98badd3de879ce5e870ba60a3a))

## [1.9.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.9.3...google-cloud-apigee-connect-v1.9.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12863](https://github.com/googleapis/google-cloud-python/issues/12863)) ([3e6e423](https://github.com/googleapis/google-cloud-python/commit/3e6e423b86cdace8538f610941aa84c7a6217934))

## [1.9.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.9.2...google-cloud-apigee-connect-v1.9.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12381](https://github.com/googleapis/google-cloud-python/issues/12381)) ([48ae8ab](https://github.com/googleapis/google-cloud-python/commit/48ae8aba7ec71a382e001b3a659022f942c3b436))

## [1.9.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.9.1...google-cloud-apigee-connect-v1.9.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12280](https://github.com/googleapis/google-cloud-python/issues/12280)) ([2d75d0e](https://github.com/googleapis/google-cloud-python/commit/2d75d0e67ca4cccddc688bd37c14ac80564a2e65))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.9.0...google-cloud-apigee-connect-v1.9.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.8.0...google-cloud-apigee-connect-v1.9.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.7.3...google-cloud-apigee-connect-v1.8.0) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [1.7.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.7.2...google-cloud-apigee-connect-v1.7.3) (2023-09-30)


### Documentation

* Minor formatting ([#11630](https://github.com/googleapis/google-cloud-python/issues/11630)) ([b176996](https://github.com/googleapis/google-cloud-python/commit/b176996309cb5b3e9c257caaebde8884bd556824))

## [1.7.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apigee-connect-v1.7.1...google-cloud-apigee-connect-v1.7.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11444](https://github.com/googleapis/google-cloud-python/issues/11444)) ([9aa301a](https://github.com/googleapis/google-cloud-python/commit/9aa301ae6ca3080cae286a19de9cdc1b796ab37d))

## [1.7.1](https://github.com/googleapis/python-apigee-connect/compare/v1.7.0...v1.7.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([514bdf3](https://github.com/googleapis/python-apigee-connect/commit/514bdf3795b7bba012236d357155b5d798f60df0))


### Documentation

* Add documentation for enums ([514bdf3](https://github.com/googleapis/python-apigee-connect/commit/514bdf3795b7bba012236d357155b5d798f60df0))

## [1.7.0](https://github.com/googleapis/python-apigee-connect/compare/v1.6.1...v1.7.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#168](https://github.com/googleapis/python-apigee-connect/issues/168)) ([a340710](https://github.com/googleapis/python-apigee-connect/commit/a34071088707b876d42bf687fb12b133724c0cc6))

## [1.6.1](https://github.com/googleapis/python-apigee-connect/compare/v1.6.0...v1.6.1) (2022-12-08)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([15ed1e8](https://github.com/googleapis/python-apigee-connect/commit/15ed1e868a37c5818e137a0f95e8a48bed6d4cd9))
* Drop usage of pkg_resources ([15ed1e8](https://github.com/googleapis/python-apigee-connect/commit/15ed1e868a37c5818e137a0f95e8a48bed6d4cd9))
* Fix timeout default values ([15ed1e8](https://github.com/googleapis/python-apigee-connect/commit/15ed1e868a37c5818e137a0f95e8a48bed6d4cd9))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([15ed1e8](https://github.com/googleapis/python-apigee-connect/commit/15ed1e868a37c5818e137a0f95e8a48bed6d4cd9))

## [1.6.0](https://github.com/googleapis/python-apigee-connect/compare/v1.5.0...v1.6.0) (2022-11-16)


### Features

* Add typing to proto.Message based class attributes ([6ca9292](https://github.com/googleapis/python-apigee-connect/commit/6ca929223b74d3e2f26d6b34b3c937db8250a4e3))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([6ca9292](https://github.com/googleapis/python-apigee-connect/commit/6ca929223b74d3e2f26d6b34b3c937db8250a4e3))

## [1.5.0](https://github.com/googleapis/python-apigee-connect/compare/v1.4.3...v1.5.0) (2022-11-08)


### Features

* add support for `google.cloud.apigeeconnect.__version__` ([ec1f84c](https://github.com/googleapis/python-apigee-connect/commit/ec1f84c1685df65a1805051bc5092f04f4cec87d))


### Bug Fixes

* Add dict typing for client_options ([ec1f84c](https://github.com/googleapis/python-apigee-connect/commit/ec1f84c1685df65a1805051bc5092f04f4cec87d))
* **deps:** require google-api-core &gt;=1.33.2 ([ec1f84c](https://github.com/googleapis/python-apigee-connect/commit/ec1f84c1685df65a1805051bc5092f04f4cec87d))

## [1.4.3](https://github.com/googleapis/python-apigee-connect/compare/v1.4.2...v1.4.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#151](https://github.com/googleapis/python-apigee-connect/issues/151)) ([baca117](https://github.com/googleapis/python-apigee-connect/commit/baca117237ee80e889366fa54ff1bd0fb54e2661))

## [1.4.2](https://github.com/googleapis/python-apigee-connect/compare/v1.4.1...v1.4.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#148](https://github.com/googleapis/python-apigee-connect/issues/148)) ([43ff689](https://github.com/googleapis/python-apigee-connect/commit/43ff68925dbd3a8db86f1e2a035ee91f45948ae1))

## [1.4.1](https://github.com/googleapis/python-apigee-connect/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#133](https://github.com/googleapis/python-apigee-connect/issues/133)) ([25c184a](https://github.com/googleapis/python-apigee-connect/commit/25c184aa094ac77ee92bf87d6c4160d2fd20b4a8))
* **deps:** require proto-plus >= 1.22.0 ([25c184a](https://github.com/googleapis/python-apigee-connect/commit/25c184aa094ac77ee92bf87d6c4160d2fd20b4a8))

## [1.4.0](https://github.com/googleapis/python-apigee-connect/compare/v1.3.2...v1.4.0) (2022-07-17)


### Features

* add audience parameter ([59bcc9c](https://github.com/googleapis/python-apigee-connect/commit/59bcc9ca7ceb1aeffb74c5989e2e47ad73a4b434))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#124](https://github.com/googleapis/python-apigee-connect/issues/124)) ([59bcc9c](https://github.com/googleapis/python-apigee-connect/commit/59bcc9ca7ceb1aeffb74c5989e2e47ad73a4b434))
* require python 3.7+ ([#126](https://github.com/googleapis/python-apigee-connect/issues/126)) ([2df9df8](https://github.com/googleapis/python-apigee-connect/commit/2df9df8eef41cd34e3634e93b1f9aabc28b9973b))

## [1.3.2](https://github.com/googleapis/python-apigee-connect/compare/v1.3.1...v1.3.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#115](https://github.com/googleapis/python-apigee-connect/issues/115)) ([4abbe8b](https://github.com/googleapis/python-apigee-connect/commit/4abbe8b68e1a8bb9f32b6f37f8f9462da0179b56))


### Documentation

* fix changelog header to consistent size ([#116](https://github.com/googleapis/python-apigee-connect/issues/116)) ([de3022c](https://github.com/googleapis/python-apigee-connect/commit/de3022cfe32ff6cc796bd24fb1a6f9935599ad96))

## [1.3.1](https://github.com/googleapis/python-apigee-connect/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#92](https://github.com/googleapis/python-apigee-connect/issues/92)) ([2cee45c](https://github.com/googleapis/python-apigee-connect/commit/2cee45c4aa1873e30a461586432f94ba1f5e04fe))

## [1.3.0](https://github.com/googleapis/python-apigee-connect/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#79](https://github.com/googleapis/python-apigee-connect/issues/79)) ([ae944c1](https://github.com/googleapis/python-apigee-connect/commit/ae944c10b2f63a682cf2f196d2122ccbed2dac48))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([2ff0df1](https://github.com/googleapis/python-apigee-connect/commit/2ff0df184986fcaee52af77bfe7c26348394e0fd))


### Documentation

* add autogenerated code snippets ([86b45c2](https://github.com/googleapis/python-apigee-connect/commit/86b45c2379df54b274d192e5a46e6348e4f86005))

## [1.2.1](https://www.github.com/googleapis/python-apigee-connect/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([4cd9ea7](https://www.github.com/googleapis/python-apigee-connect/commit/4cd9ea7bd45e5a3410e6b1bde0a0ab629f75530d))
* **deps:** require google-api-core >= 1.28.0 ([4cd9ea7](https://www.github.com/googleapis/python-apigee-connect/commit/4cd9ea7bd45e5a3410e6b1bde0a0ab629f75530d))


### Documentation

* list oneofs in docstring ([4cd9ea7](https://www.github.com/googleapis/python-apigee-connect/commit/4cd9ea7bd45e5a3410e6b1bde0a0ab629f75530d))

## [1.2.0](https://www.github.com/googleapis/python-apigee-connect/compare/v1.1.0...v1.2.0) (2021-10-15)


### Features

* add support for python 3.10 ([#56](https://www.github.com/googleapis/python-apigee-connect/issues/56)) ([f119149](https://www.github.com/googleapis/python-apigee-connect/commit/f119149b8343b0a8ae84dbe3d228f6b422d13b20))

## [1.1.0](https://www.github.com/googleapis/python-apigee-connect/compare/v1.0.2...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#54](https://www.github.com/googleapis/python-apigee-connect/issues/54)) ([0dc1edd](https://www.github.com/googleapis/python-apigee-connect/commit/0dc1eddc5fae79b2516789587eb097190c8f1420))

## [1.0.2](https://www.github.com/googleapis/python-apigee-connect/compare/v1.0.1...v1.0.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([fb8b837](https://www.github.com/googleapis/python-apigee-connect/commit/fb8b837d64c9771d7af9d36688e00243794ea731))

## [1.0.1](https://www.github.com/googleapis/python-apigee-connect/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([50db178](https://www.github.com/googleapis/python-apigee-connect/commit/50db178c9dec3b1214d537da0a9bd9088d9ebf43))


## [1.0.0](https://www.github.com/googleapis/python-apigee-connect/compare/v0.2.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#28](https://www.github.com/googleapis/python-apigee-connect/issues/28)) ([65803db](https://www.github.com/googleapis/python-apigee-connect/commit/65803db4821b594124bfb88012ba4f954568a895))

## [0.2.2](https://www.github.com/googleapis/python-apigee-connect/compare/v0.2.1...v0.2.2) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#24](https://www.github.com/googleapis/python-apigee-connect/issues/24)) ([d02ffa1](https://www.github.com/googleapis/python-apigee-connect/commit/d02ffa1f4906da6ba8d479b18947e6d28ccb1987))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#20](https://www.github.com/googleapis/python-apigee-connect/issues/20)) ([6f37510](https://www.github.com/googleapis/python-apigee-connect/commit/6f37510de8b5bd00720335f1343354ee2c932d9e))


### Miscellaneous Chores

* release as 0.2.2 ([#25](https://www.github.com/googleapis/python-apigee-connect/issues/25)) ([f6660d3](https://www.github.com/googleapis/python-apigee-connect/commit/f6660d3d604c61b748abe59a51923b74b687d761))

## [0.2.1](https://www.github.com/googleapis/python-apigee-connect/compare/v0.2.0...v0.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#19](https://www.github.com/googleapis/python-apigee-connect/issues/19)) ([cfa46e7](https://www.github.com/googleapis/python-apigee-connect/commit/cfa46e7528595d57f396839ef167cb8ede29981b))

## [0.2.0](https://www.github.com/googleapis/python-apigee-connect/compare/v0.1.0...v0.2.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#11](https://www.github.com/googleapis/python-apigee-connect/issues/11)) ([bdd0f21](https://www.github.com/googleapis/python-apigee-connect/commit/bdd0f2109e34d100c285ab355f302326816f24c8))


### Bug Fixes

* disable always_use_jwt_access ([f4cff83](https://www.github.com/googleapis/python-apigee-connect/commit/f4cff83baf1865477139bd14b02a12e47505150d))
* disable always_use_jwt_access ([#15](https://www.github.com/googleapis/python-apigee-connect/issues/15)) ([f4cff83](https://www.github.com/googleapis/python-apigee-connect/commit/f4cff83baf1865477139bd14b02a12e47505150d))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-apigee-connect/issues/1127)) ([#6](https://www.github.com/googleapis/python-apigee-connect/issues/6)) ([a465d9a](https://www.github.com/googleapis/python-apigee-connect/commit/a465d9a37f4738f0f16e89b4c26a74366c0834fb)), closes [#1126](https://www.github.com/googleapis/python-apigee-connect/issues/1126)

## 0.1.0 (2021-06-13)


### Features

* generate v1 ([b52b2bf](https://www.github.com/googleapis/python-apigee-connect/commit/b52b2bf1f8456eb7fc815857d90384d2f596d23a))
