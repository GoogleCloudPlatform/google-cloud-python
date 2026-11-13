# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-appengine-admin/#history

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.18.0...google-cloud-appengine-admin-v1.19.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.17.0...google-cloud-appengine-admin-v1.18.0) (2026-06-02)


### Features

* regenerate google-cloud-a packages (#17089) ([39c988267529419b03f808d7662ec521258571b4](https://github.com/googleapis/google-cloud-python/commit/39c988267529419b03f808d7662ec521258571b4))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.16.0...google-cloud-appengine-admin-v1.17.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.15.0...google-cloud-appengine-admin-v1.16.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.14.2...google-cloud-appengine-admin-v1.15.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.14.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.14.1...google-cloud-appengine-admin-v1.14.2) (2025-06-11)


### Documentation

* Update import statement example in README ([eea9e6f](https://github.com/googleapis/google-cloud-python/commit/eea9e6f798406fec17a17dfd71e40fbeea42cf6a))

## [1.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.14.0...google-cloud-appengine-admin-v1.14.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([3a85796](https://github.com/googleapis/google-cloud-python/commit/3a85796774ebf728cbc9e82dc536316530ac78c1))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.13.0...google-cloud-appengine-admin-v1.14.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))
* Add support for reading selective GAPIC generation methods from service YAML ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.12.1...google-cloud-appengine-admin-v1.13.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.12.0...google-cloud-appengine-admin-v1.12.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([85c7512](https://github.com/googleapis/google-cloud-python/commit/85c7512bbdde2b9cc60b4ad42b8c36c4558a07a5))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.11.5...google-cloud-appengine-admin-v1.12.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13199](https://github.com/googleapis/google-cloud-python/issues/13199)) ([2fc3726](https://github.com/googleapis/google-cloud-python/commit/2fc372685731141ca1ed2a917dd18bacd79db88e))

## [1.11.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.11.4...google-cloud-appengine-admin-v1.11.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([c6eeae0](https://github.com/googleapis/google-cloud-python/commit/c6eeae00de802d98badd3de879ce5e870ba60a3a))

## [1.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.11.3...google-cloud-appengine-admin-v1.11.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12863](https://github.com/googleapis/google-cloud-python/issues/12863)) ([3e6e423](https://github.com/googleapis/google-cloud-python/commit/3e6e423b86cdace8538f610941aa84c7a6217934))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.11.2...google-cloud-appengine-admin-v1.11.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12381](https://github.com/googleapis/google-cloud-python/issues/12381)) ([48ae8ab](https://github.com/googleapis/google-cloud-python/commit/48ae8aba7ec71a382e001b3a659022f942c3b436))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.11.1...google-cloud-appengine-admin-v1.11.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12280](https://github.com/googleapis/google-cloud-python/issues/12280)) ([2d75d0e](https://github.com/googleapis/google-cloud-python/commit/2d75d0e67ca4cccddc688bd37c14ac80564a2e65))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.11.0...google-cloud-appengine-admin-v1.11.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.10.0...google-cloud-appengine-admin-v1.11.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-appengine-admin-v1.9.4...google-cloud-appengine-admin-v1.10.0) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [1.9.4](https://github.com/googleapis/python-appengine-admin/compare/v1.9.3...v1.9.4) (2023-10-09)


### Documentation

* Minor formatting ([#249](https://github.com/googleapis/python-appengine-admin/issues/249)) ([7de9b52](https://github.com/googleapis/python-appengine-admin/commit/7de9b52ce89849f49ca067690a8725d3d9239f09))

## [1.9.3](https://github.com/googleapis/python-appengine-admin/compare/v1.9.2...v1.9.3) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#238](https://github.com/googleapis/python-appengine-admin/issues/238)) ([72764d1](https://github.com/googleapis/python-appengine-admin/commit/72764d13c06bdd3d6055efcb753819f67823a971))

## [1.9.2](https://github.com/googleapis/python-appengine-admin/compare/v1.9.1...v1.9.2) (2023-04-01)


### Documentation

* Point to Search Console for domain ownership verification ([#232](https://github.com/googleapis/python-appengine-admin/issues/232)) ([a45eff9](https://github.com/googleapis/python-appengine-admin/commit/a45eff96750e74230f60e312b2ab0ad9b9933ec5))

## [1.9.1](https://github.com/googleapis/python-appengine-admin/compare/v1.9.0...v1.9.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#230](https://github.com/googleapis/python-appengine-admin/issues/230)) ([7738bed](https://github.com/googleapis/python-appengine-admin/commit/7738bed39a867311611a57f7da9e2cd48d58f7c3))

## [1.9.0](https://github.com/googleapis/python-appengine-admin/compare/v1.8.1...v1.9.0) (2023-02-27)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#224](https://github.com/googleapis/python-appengine-admin/issues/224)) ([819631a](https://github.com/googleapis/python-appengine-admin/commit/819631abc6b95d3d40d1772f74dac62300f4616f))

## [1.8.1](https://github.com/googleapis/python-appengine-admin/compare/v1.8.0...v1.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([846b2e1](https://github.com/googleapis/python-appengine-admin/commit/846b2e19462cbe1a0b2e201b95eee65deb3dbd5b))


### Documentation

* Add documentation for enums ([846b2e1](https://github.com/googleapis/python-appengine-admin/commit/846b2e19462cbe1a0b2e201b95eee65deb3dbd5b))

## [1.8.0](https://github.com/googleapis/python-appengine-admin/compare/v1.7.1...v1.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#216](https://github.com/googleapis/python-appengine-admin/issues/216)) ([ed1c020](https://github.com/googleapis/python-appengine-admin/commit/ed1c020e28cc152dc273c409abfdc36c6c376b20))

## [1.7.1](https://github.com/googleapis/python-appengine-admin/compare/v1.7.0...v1.7.1) (2022-12-08)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([a086ce0](https://github.com/googleapis/python-appengine-admin/commit/a086ce0d68a2790bb46390fe5d2c7d9b2db235c0))
* Drop usage of pkg_resources ([a086ce0](https://github.com/googleapis/python-appengine-admin/commit/a086ce0d68a2790bb46390fe5d2c7d9b2db235c0))
* Fix timeout default values ([a086ce0](https://github.com/googleapis/python-appengine-admin/commit/a086ce0d68a2790bb46390fe5d2c7d9b2db235c0))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([a086ce0](https://github.com/googleapis/python-appengine-admin/commit/a086ce0d68a2790bb46390fe5d2c7d9b2db235c0))

## [1.7.0](https://github.com/googleapis/python-appengine-admin/compare/v1.6.0...v1.7.0) (2022-11-16)


### Features

* Add typing to proto.Message based class attributes ([80bd28c](https://github.com/googleapis/python-appengine-admin/commit/80bd28cf8f56ea3691aa08005445b81d8372e033))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([80bd28c](https://github.com/googleapis/python-appengine-admin/commit/80bd28cf8f56ea3691aa08005445b81d8372e033))

## [1.6.0](https://github.com/googleapis/python-appengine-admin/compare/v1.5.3...v1.6.0) (2022-11-08)


### Features

* add support for `google.cloud.appengine_admin.__version__` ([2126361](https://github.com/googleapis/python-appengine-admin/commit/2126361cafcaed79633e7f403591a53a507972ba))


### Bug Fixes

* Add dict typing for client_options ([2126361](https://github.com/googleapis/python-appengine-admin/commit/2126361cafcaed79633e7f403591a53a507972ba))
* **deps:** require google-api-core &gt;=1.33.2 ([2126361](https://github.com/googleapis/python-appengine-admin/commit/2126361cafcaed79633e7f403591a53a507972ba))

## [1.5.3](https://github.com/googleapis/python-appengine-admin/compare/v1.5.2...v1.5.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#201](https://github.com/googleapis/python-appengine-admin/issues/201)) ([be08794](https://github.com/googleapis/python-appengine-admin/commit/be0879490e5bc6a61756e17d71d7c51f4742a19f))

## [1.5.2](https://github.com/googleapis/python-appengine-admin/compare/v1.5.1...v1.5.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#199](https://github.com/googleapis/python-appengine-admin/issues/199)) ([dcadfa9](https://github.com/googleapis/python-appengine-admin/commit/dcadfa97388ec350a026436e644bf7d4024549a3))

## [1.5.1](https://github.com/googleapis/python-appengine-admin/compare/v1.5.0...v1.5.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#184](https://github.com/googleapis/python-appengine-admin/issues/184)) ([ee28547](https://github.com/googleapis/python-appengine-admin/commit/ee28547fb402ae8917a70ad776fa99e927599852))
* **deps:** require proto-plus >= 1.22.0 ([ee28547](https://github.com/googleapis/python-appengine-admin/commit/ee28547fb402ae8917a70ad776fa99e927599852))

## [1.5.0](https://github.com/googleapis/python-appengine-admin/compare/v1.4.1...v1.5.0) (2022-07-18)


### Features

* add audience parameter ([307bdf5](https://github.com/googleapis/python-appengine-admin/commit/307bdf56fccbb04229dd4fae1ae6d425e2c51bcc))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#175](https://github.com/googleapis/python-appengine-admin/issues/175)) ([307bdf5](https://github.com/googleapis/python-appengine-admin/commit/307bdf56fccbb04229dd4fae1ae6d425e2c51bcc))
* require python 3.7+ ([#177](https://github.com/googleapis/python-appengine-admin/issues/177)) ([a3d18cc](https://github.com/googleapis/python-appengine-admin/commit/a3d18cca4a42a6290d582c2ea2b7bb50189a65ac))

## [1.4.1](https://github.com/googleapis/python-appengine-admin/compare/v1.4.0...v1.4.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#167](https://github.com/googleapis/python-appengine-admin/issues/167)) ([d18523f](https://github.com/googleapis/python-appengine-admin/commit/d18523f1e900cd3d59ab5919629680f1023cb5da))


### Documentation

* fix changelog header to consistent size ([#168](https://github.com/googleapis/python-appengine-admin/issues/168)) ([32eb983](https://github.com/googleapis/python-appengine-admin/commit/32eb9839a119be5c9189140e02dd8e2c2798cbf3))

## [1.4.0](https://github.com/googleapis/python-appengine-admin/compare/v1.3.3...v1.4.0) (2022-05-05)


### Features

* add Application.service_account ([#134](https://github.com/googleapis/python-appengine-admin/issues/134)) ([595a87c](https://github.com/googleapis/python-appengine-admin/commit/595a87cd561cf26da72599adc6750fdf20a2f1b5))
* add client library method signature to retrieve Application by name ([595a87c](https://github.com/googleapis/python-appengine-admin/commit/595a87cd561cf26da72599adc6750fdf20a2f1b5))
* add Service.labels ([595a87c](https://github.com/googleapis/python-appengine-admin/commit/595a87cd561cf26da72599adc6750fdf20a2f1b5))
* add Version.app_engine_apis ([595a87c](https://github.com/googleapis/python-appengine-admin/commit/595a87cd561cf26da72599adc6750fdf20a2f1b5))
* add VpcAccessConnector.egress_setting ([595a87c](https://github.com/googleapis/python-appengine-admin/commit/595a87cd561cf26da72599adc6750fdf20a2f1b5))

## [1.3.3](https://github.com/googleapis/python-appengine-admin/compare/v1.3.2...v1.3.3) (2022-04-14)


### Documentation

* fix type in docstring for map fields ([b0ce988](https://github.com/googleapis/python-appengine-admin/commit/b0ce988cf7ec3620d6d586abab8b13de50e8b586))

## [1.3.2](https://github.com/googleapis/python-appengine-admin/compare/v1.3.1...v1.3.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#115](https://github.com/googleapis/python-appengine-admin/issues/115)) ([a4b3624](https://github.com/googleapis/python-appengine-admin/commit/a4b36244e2e566770f3cca84aac9bb003ca47f56))

## [1.3.1](https://github.com/googleapis/python-appengine-admin/compare/v1.3.0...v1.3.1) (2022-02-11)


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([a6ec7ac](https://github.com/googleapis/python-appengine-admin/commit/a6ec7acb2f7b0a8acb68bd7de770c299eb9ee8d2))


### Documentation

* add autogenerated code snippets ([5f989b9](https://github.com/googleapis/python-appengine-admin/commit/5f989b948c03c409466b76f8c5853819261b9737))

## [1.3.0](https://github.com/googleapis/python-appengine-admin/compare/v1.2.1...v1.3.0) (2022-01-25)


### Features

* add api key support ([#100](https://github.com/googleapis/python-appengine-admin/issues/100)) ([67f3bb4](https://github.com/googleapis/python-appengine-admin/commit/67f3bb4c0fa31f795c6aef4bd19b9a5fe9da0360))

## [1.2.1](https://www.github.com/googleapis/python-appengine-admin/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([fd7fdd7](https://www.github.com/googleapis/python-appengine-admin/commit/fd7fdd7f7ef666f1c9ff64ac27f98b4573a5d1f3))
* **deps:** require google-api-core >= 1.28.0 ([fd7fdd7](https://www.github.com/googleapis/python-appengine-admin/commit/fd7fdd7f7ef666f1c9ff64ac27f98b4573a5d1f3))


### Documentation

* list oneofs in docstring ([fd7fdd7](https://www.github.com/googleapis/python-appengine-admin/commit/fd7fdd7f7ef666f1c9ff64ac27f98b4573a5d1f3))

## [1.2.0](https://www.github.com/googleapis/python-appengine-admin/compare/v1.1.5...v1.2.0) (2021-10-11)


### Features

* add context manager support in client ([#75](https://www.github.com/googleapis/python-appengine-admin/issues/75)) ([e5d86ee](https://www.github.com/googleapis/python-appengine-admin/commit/e5d86eef07ee05454135b5b392a6841f7932a303))
* add trove classifier for python 3.10 ([#78](https://www.github.com/googleapis/python-appengine-admin/issues/78)) ([e915580](https://www.github.com/googleapis/python-appengine-admin/commit/e915580dd5e66a4d44cede94acfde0e181e9fe3a))

## [1.1.5](https://www.github.com/googleapis/python-appengine-admin/compare/v1.1.4...v1.1.5) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([a29e420](https://www.github.com/googleapis/python-appengine-admin/commit/a29e4200c6fdb7cad045bfd29e74a35c9a6e6fd6))

## [1.1.4](https://www.github.com/googleapis/python-appengine-admin/compare/v1.1.3...v1.1.4) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([89b4378](https://www.github.com/googleapis/python-appengine-admin/commit/89b4378632af08a11c3bd45d88eb0f0ac152238f))

## [1.1.3](https://www.github.com/googleapis/python-appengine-admin/compare/v1.1.2...v1.1.3) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#53](https://www.github.com/googleapis/python-appengine-admin/issues/53)) ([8b6c798](https://www.github.com/googleapis/python-appengine-admin/commit/8b6c79806ea6c052d27434da1d6b997d27a83156))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#49](https://www.github.com/googleapis/python-appengine-admin/issues/49)) ([6b59802](https://www.github.com/googleapis/python-appengine-admin/commit/6b59802d54d044575520711416baa85b0a636bea))


### Miscellaneous Chores

* release as 1.1.3 ([#54](https://www.github.com/googleapis/python-appengine-admin/issues/54)) ([aeeefd1](https://www.github.com/googleapis/python-appengine-admin/commit/aeeefd10f953ec09ddc8e3bde38f0d90bdab47f8))

## [1.1.2](https://www.github.com/googleapis/python-appengine-admin/compare/v1.1.1...v1.1.2) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#48](https://www.github.com/googleapis/python-appengine-admin/issues/48)) ([c9fac07](https://www.github.com/googleapis/python-appengine-admin/commit/c9fac071151957e69fd83cb9aefb027c6551a55c))

## [1.1.1](https://www.github.com/googleapis/python-appengine-admin/compare/v1.1.0...v1.1.1) (2021-06-30)


### Bug Fixes

* disable always_use_jwt_access ([d8d2f5f](https://www.github.com/googleapis/python-appengine-admin/commit/d8d2f5f9e6c986387fd0d811e4be06a68a83aa8e))
* disable always_use_jwt_access ([#44](https://www.github.com/googleapis/python-appengine-admin/issues/44)) ([d8d2f5f](https://www.github.com/googleapis/python-appengine-admin/commit/d8d2f5f9e6c986387fd0d811e4be06a68a83aa8e))

## [1.1.0](https://www.github.com/googleapis/python-appengine-admin/compare/v1.0.2...v1.1.0) (2021-06-23)


### Features

* add always_use_jwt_access ([#40](https://www.github.com/googleapis/python-appengine-admin/issues/40)) ([f260f90](https://www.github.com/googleapis/python-appengine-admin/commit/f260f90985b5f05f11258b86af1b1ead652a882d))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-appengine-admin/issues/1127)) ([#35](https://www.github.com/googleapis/python-appengine-admin/issues/35)) ([34b578c](https://www.github.com/googleapis/python-appengine-admin/commit/34b578c920e8fba4cca1eb0532d357552056d12f)), closes [#1126](https://www.github.com/googleapis/python-appengine-admin/issues/1126)

## [1.0.2](https://www.github.com/googleapis/python-appengine-admin/compare/v1.0.1...v1.0.2) (2021-06-16)


### Bug Fixes

* fix typo in setup.py ([#32](https://www.github.com/googleapis/python-appengine-admin/issues/32)) ([1a749ef](https://www.github.com/googleapis/python-appengine-admin/commit/1a749effe4873c759a1630c0d836bafa193856c6))

## [1.0.1](https://www.github.com/googleapis/python-appengine-admin/compare/v1.0.0...v1.0.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#30](https://www.github.com/googleapis/python-appengine-admin/issues/30)) ([16ad4ac](https://www.github.com/googleapis/python-appengine-admin/commit/16ad4acea57a44126d0d954962a15a455dfbdbf0))

## [1.0.0](https://www.github.com/googleapis/python-appengine-admin/compare/v0.2.0...v1.0.0) (2021-06-02)


### Features

* bump release level to production/stable ([#23](https://www.github.com/googleapis/python-appengine-admin/issues/23)) ([4cb1678](https://www.github.com/googleapis/python-appengine-admin/commit/4cb167891b8d926389dd9561de8ea7b5314906c4))


### Miscellaneous Chores

* release as 1.0.0 ([#28](https://www.github.com/googleapis/python-appengine-admin/issues/28)) ([de071b0](https://www.github.com/googleapis/python-appengine-admin/commit/de071b09a7ec19637452856e1bbdb522e5f1d050))

## [0.2.0](https://www.github.com/googleapis/python-appengine-admin/compare/v0.1.0...v0.2.0) (2021-05-28)


### Features

* support self-signed JWT flow for service accounts ([c798db2](https://www.github.com/googleapis/python-appengine-admin/commit/c798db287a2e85551e512e66d4bc1da344a806d2))


### Bug Fixes

* add async client to %name_%version/init.py ([c798db2](https://www.github.com/googleapis/python-appengine-admin/commit/c798db287a2e85551e512e66d4bc1da344a806d2))
* **deps:** add packaging requirement ([#20](https://www.github.com/googleapis/python-appengine-admin/issues/20)) ([f352b81](https://www.github.com/googleapis/python-appengine-admin/commit/f352b811c13dd4b5b9fecf719dad05ce292e61fa))

## 0.1.0 (2021-04-05)


### Features

* generate v1 ([1a14a9c](https://www.github.com/googleapis/python-appengine-admin/commit/1a14a9c4dba69fae84586b59da27762b5f39e58b))
