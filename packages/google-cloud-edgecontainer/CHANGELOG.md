# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-edgecontainer/#history

## [0.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.8.1...google-cloud-edgecontainer-v0.8.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.8.0...google-cloud-edgecontainer-v0.8.1) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.7.0...google-cloud-edgecontainer-v0.8.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.6.0...google-cloud-edgecontainer-v0.7.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.18...google-cloud-edgecontainer-v0.6.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.5.18](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.17...google-cloud-edgecontainer-v0.5.18) (2025-06-11)


### Documentation

* Update import statement example in README ([821bdb1](https://github.com/googleapis/google-cloud-python/commit/821bdb1d108c8e77a7a576557aa95d4b9c943e12))

## [0.5.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.16...google-cloud-edgecontainer-v0.5.17) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([feb5353](https://github.com/googleapis/google-cloud-python/commit/feb53532240bb70a94b359b519f0f41f95875a33))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.5.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.15...google-cloud-edgecontainer-v0.5.16) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))
* Add support for reading selective GAPIC generation methods from service YAML ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))

## [0.5.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.14...google-cloud-edgecontainer-v0.5.15) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [0.5.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.13...google-cloud-edgecontainer-v0.5.14) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))

## [0.5.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.12...google-cloud-edgecontainer-v0.5.13) (2024-10-31)


### Features

* add config data to zone metadata ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add connection state to cluster ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add maintenance exclusion window to maintenance policy ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add resource state to control plane encryption ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add resource state to local disk encryption ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add status reason to operation metadata ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add storage schema to local control plane config ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add storage schema to node config ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))
* add VM service config to system addons config ([a0f0c7e](https://github.com/googleapis/google-cloud-python/commit/a0f0c7ee4045081927f9c3241cfff8e0c916798f))

## [0.5.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.11...google-cloud-edgecontainer-v0.5.12) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13203](https://github.com/googleapis/google-cloud-python/issues/13203)) ([d9fcbb9](https://github.com/googleapis/google-cloud-python/commit/d9fcbb9fce625bb772ae4b3cb8c4a4ab2eaaa836))

## [0.5.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.10...google-cloud-edgecontainer-v0.5.11) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([ba1064f](https://github.com/googleapis/google-cloud-python/commit/ba1064fd6a63ccbe8a390c0026f32c5772c728a5))

## [0.5.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.9...google-cloud-edgecontainer-v0.5.10) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## [0.5.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.8...google-cloud-edgecontainer-v0.5.9) (2024-03-22)


### Features

* add GetServerConfig rpc and message ([d7cc4ae](https://github.com/googleapis/google-cloud-python/commit/d7cc4ae8fed8aaa29f85ba57dbc22f72463d290a))
* add UpgradeCluster ([d7cc4ae](https://github.com/googleapis/google-cloud-python/commit/d7cc4ae8fed8aaa29f85ba57dbc22f72463d290a))

## [0.5.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.7...google-cloud-edgecontainer-v0.5.8) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12384](https://github.com/googleapis/google-cloud-python/issues/12384)) ([c69966f](https://github.com/googleapis/google-cloud-python/commit/c69966fa7aac2cba4e22513e4a053b3754f8ea5e))

## [0.5.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.6...google-cloud-edgecontainer-v0.5.7) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12283](https://github.com/googleapis/google-cloud-python/issues/12283)) ([f20b41a](https://github.com/googleapis/google-cloud-python/commit/f20b41ac35b02a40135b83edfe819ff7a355ab21))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))

## [0.5.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.5...google-cloud-edgecontainer-v0.5.6) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))

## [0.5.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.4...google-cloud-edgecontainer-v0.5.5) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [0.5.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.3...google-cloud-edgecontainer-v0.5.4) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [0.5.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.2...google-cloud-edgecontainer-v0.5.3) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-edgecontainer-v0.5.1...google-cloud-edgecontainer-v0.5.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [0.5.1](https://github.com/googleapis/python-edgecontainer/compare/v0.5.0...v0.5.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#30](https://github.com/googleapis/python-edgecontainer/issues/30)) ([010c651](https://github.com/googleapis/python-edgecontainer/commit/010c651ccb9c5f56a7cbf1e822def196fb8d706d))

## [0.5.0](https://github.com/googleapis/python-edgecontainer/compare/v0.4.1...v0.5.0) (2023-03-03)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#24](https://github.com/googleapis/python-edgecontainer/issues/24)) ([945e4fa](https://github.com/googleapis/python-edgecontainer/commit/945e4faabc1267ede01875e60488d409b73ff638))


### Bug Fixes

* Add service_yaml parameters to edgecontainer GAPIC targets ([#28](https://github.com/googleapis/python-edgecontainer/issues/28)) ([5fd68bf](https://github.com/googleapis/python-edgecontainer/commit/5fd68bf24b50ff3c01bc0438c4d2c7592c5ba060))

## [0.4.1](https://github.com/googleapis/python-edgecontainer/compare/v0.4.0...v0.4.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([21e3444](https://github.com/googleapis/python-edgecontainer/commit/21e3444558864335d28a4bb502e7b5a72d0464fa))


### Documentation

* Add documentation for enums ([21e3444](https://github.com/googleapis/python-edgecontainer/commit/21e3444558864335d28a4bb502e7b5a72d0464fa))

## [0.4.0](https://github.com/googleapis/python-edgecontainer/compare/v0.3.0...v0.4.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#15](https://github.com/googleapis/python-edgecontainer/issues/15)) ([c43bbc1](https://github.com/googleapis/python-edgecontainer/commit/c43bbc12171fbf39d1ee760ea61be145e727e807))

## [0.3.0](https://github.com/googleapis/python-edgecontainer/compare/v0.2.1...v0.3.0) (2022-12-15)


### Features

* Add support for `google.cloud.edgecontainer.__version__` ([f389e2d](https://github.com/googleapis/python-edgecontainer/commit/f389e2d224b6eeee2cb5337f2f6312d39140d897))
* Add typing to proto.Message based class attributes ([f389e2d](https://github.com/googleapis/python-edgecontainer/commit/f389e2d224b6eeee2cb5337f2f6312d39140d897))


### Bug Fixes

* Add dict typing for client_options ([f389e2d](https://github.com/googleapis/python-edgecontainer/commit/f389e2d224b6eeee2cb5337f2f6312d39140d897))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([f72016a](https://github.com/googleapis/python-edgecontainer/commit/f72016a4f5970a401853c054be3b9b07bd1c5ac2))
* Drop usage of pkg_resources ([f72016a](https://github.com/googleapis/python-edgecontainer/commit/f72016a4f5970a401853c054be3b9b07bd1c5ac2))
* Fix timeout default values ([f72016a](https://github.com/googleapis/python-edgecontainer/commit/f72016a4f5970a401853c054be3b9b07bd1c5ac2))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([f389e2d](https://github.com/googleapis/python-edgecontainer/commit/f389e2d224b6eeee2cb5337f2f6312d39140d897))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([f72016a](https://github.com/googleapis/python-edgecontainer/commit/f72016a4f5970a401853c054be3b9b07bd1c5ac2))

## [0.2.1](https://github.com/googleapis/python-edgecontainer/compare/v0.2.0...v0.2.1) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#5](https://github.com/googleapis/python-edgecontainer/issues/5)) ([3b695ec](https://github.com/googleapis/python-edgecontainer/commit/3b695ec9b0cef5aa191bf3fbae95902936c32a84))
* **deps:** require google-api-core&gt;=1.33.2 ([3b695ec](https://github.com/googleapis/python-edgecontainer/commit/3b695ec9b0cef5aa191bf3fbae95902936c32a84))

## [0.2.0](https://github.com/googleapis/python-edgecontainer/compare/v0.1.0...v0.2.0) (2022-10-03)


### Features

* add a field in cluster to describe whether the machine is disabled. ([6c98a68](https://github.com/googleapis/python-edgecontainer/commit/6c98a6803375915a20c460ff66d95a2c4a08e271))
* Temporally remove the version fields ([#3](https://github.com/googleapis/python-edgecontainer/issues/3)) ([6c98a68](https://github.com/googleapis/python-edgecontainer/commit/6c98a6803375915a20c460ff66d95a2c4a08e271))


### Bug Fixes

* mark VPC project and service account as optional fields and add details for service account format ([6c98a68](https://github.com/googleapis/python-edgecontainer/commit/6c98a6803375915a20c460ff66d95a2c4a08e271))

## 0.1.0 (2022-10-03)


### Features

* Generate v1 ([1c04325](https://github.com/googleapis/python-edgecontainer/commit/1c043255c62504d405e4647e908ecaab6d3e6b14))

## Changelog
