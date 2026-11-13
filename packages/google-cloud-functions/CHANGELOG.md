# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-functions/#history

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.24.0...google-cloud-functions-v1.25.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.23.0...google-cloud-functions-v1.24.0) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.22.0...google-cloud-functions-v1.23.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.21.0...google-cloud-functions-v1.22.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.20.4...google-cloud-functions-v1.21.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.20.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.20.3...google-cloud-functions-v1.20.4) (2025-06-11)


### Documentation

* Update import statement example in README ([821bdb1](https://github.com/googleapis/google-cloud-python/commit/821bdb1d108c8e77a7a576557aa95d4b9c943e12))

## [1.20.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.20.2...google-cloud-functions-v1.20.3) (2025-04-12)


### Documentation

* small fixes ([bc9fdfe](https://github.com/googleapis/google-cloud-python/commit/bc9fdfe26b08ac1573abbcb112fe511f70956826))
* updated `docker_registry` proto to reflect its deprecated status ([bc9fdfe](https://github.com/googleapis/google-cloud-python/commit/bc9fdfe26b08ac1573abbcb112fe511f70956826))
* updated docker_registry proto to reflect its deprecated status [#13736](https://github.com/googleapis/google-cloud-python/issues/13736) ([bc9fdfe](https://github.com/googleapis/google-cloud-python/commit/bc9fdfe26b08ac1573abbcb112fe511f70956826))

## [1.20.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.20.1...google-cloud-functions-v1.20.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.20.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.20.0...google-cloud-functions-v1.20.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([16e14c8](https://github.com/googleapis/google-cloud-python/commit/16e14c8d547864360dcab45d90e9e55169204fc6))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.19.0...google-cloud-functions-v1.20.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.18.1...google-cloud-functions-v1.19.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [1.18.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.18.0...google-cloud-functions-v1.18.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.17.0...google-cloud-functions-v1.18.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.16.5...google-cloud-functions-v1.17.0) (2024-08-08)


### Features

* Added `build_service_account` field to CloudFunction ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* additional field on the output that specified whether the deployment supports Physical Zone Separation. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* Generate upload URL now supports for specifying the GCF generation that the generated upload url will be used for. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* ListRuntimes response now includes deprecation and decommissioning dates. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* optional field for binary authorization policy. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* optional field for deploying a source from a GitHub repository. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* optional field for specifying a revision on GetFunction. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* optional field for specifying a service account to use for the build. This helps navigate the change of historical default on new projects. For more details, see https://cloud.google.com/build/docs/cloud-build-service-account-updates ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* optional fields for setting up automatic base image updates. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))


### Documentation

* A comment for field `automatic_update_policy` in message `.google.cloud.functions.v1.CloudFunction` is changed ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* A comment for field `docker_repository` in message `.google.cloud.functions.v1.CloudFunction` is changed ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* A comment for field `on_deploy_update_policy` in message `.google.cloud.functions.v1.CloudFunction` is changed ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* A comment for field `runtime_version` in message `.google.cloud.functions.v1.CloudFunction` is changed ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* A comment for field `url` in message `.google.cloud.functions.v1.HttpsTrigger` is changed ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* A comment for field `url` in message `.google.cloud.functions.v1.SourceRepository` is changed ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))
* Refined description in several fields. ([68e105d](https://github.com/googleapis/google-cloud-python/commit/68e105d404f53e8e08bf75704b6a031f178cf96b))

## [1.16.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.16.4...google-cloud-functions-v1.16.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [1.16.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.16.3...google-cloud-functions-v1.16.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## [1.16.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.16.2...google-cloud-functions-v1.16.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12384](https://github.com/googleapis/google-cloud-python/issues/12384)) ([c69966f](https://github.com/googleapis/google-cloud-python/commit/c69966fa7aac2cba4e22513e4a053b3754f8ea5e))

## [1.16.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.16.1...google-cloud-functions-v1.16.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12283](https://github.com/googleapis/google-cloud-python/issues/12283)) ([f20b41a](https://github.com/googleapis/google-cloud-python/commit/f20b41ac35b02a40135b83edfe819ff7a355ab21))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))

## [1.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.16.0...google-cloud-functions-v1.16.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.15.0...google-cloud-functions-v1.16.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.14.0...google-cloud-functions-v1.15.0) (2024-01-24)


### Features

* Add fields for automatic runtime updates ([82e676d](https://github.com/googleapis/google-cloud-python/commit/82e676dd9a49d54a88fe37c264b8b0145d2ca147))
* Add optional parameter `version_id` to `GetFunctionRequest` ([82e676d](https://github.com/googleapis/google-cloud-python/commit/82e676dd9a49d54a88fe37c264b8b0145d2ca147))


### Documentation

* Deprecate `network` field of `CloudFunction` ([82e676d](https://github.com/googleapis/google-cloud-python/commit/82e676dd9a49d54a88fe37c264b8b0145d2ca147))
* Minor updates in comments throughout ([82e676d](https://github.com/googleapis/google-cloud-python/commit/82e676dd9a49d54a88fe37c264b8b0145d2ca147))
* Update description for docker_registry to reflect transition to Artifact Registry ([82e676d](https://github.com/googleapis/google-cloud-python/commit/82e676dd9a49d54a88fe37c264b8b0145d2ca147))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.13.3...google-cloud-functions-v1.14.0) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [1.13.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.13.2...google-cloud-functions-v1.13.3) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.13.1...google-cloud-functions-v1.13.2) (2023-08-03)


### Documentation

* Minor formatting ([#11543](https://github.com/googleapis/google-cloud-python/issues/11543)) ([8cc031e](https://github.com/googleapis/google-cloud-python/commit/8cc031e723350890b4ceb6e813f24c4bcde3d65f))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-functions-v1.13.0...google-cloud-functions-v1.13.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [1.13.0](https://github.com/googleapis/python-functions/compare/v1.12.0...v1.13.0) (2023-05-25)


### Features

* Added helper methods for long running operations, IAM, and locations ([17b7a5b](https://github.com/googleapis/python-functions/commit/17b7a5ba23bb561ea06c58df0436d5fed79d0413))
* ListFunctions now include metadata which indicates whether a function is a `GEN_1` or `GEN_2` function ([#263](https://github.com/googleapis/python-functions/issues/263)) ([ea38aad](https://github.com/googleapis/python-functions/commit/ea38aadbd148e7984a6cfd4a68acaa8b697affc1))


### Documentation

* Applied general style guide updates to descriptions ([17b7a5b](https://github.com/googleapis/python-functions/commit/17b7a5ba23bb561ea06c58df0436d5fed79d0413))
* Clarified that vpcConnector shortname is only returned if the connector is in the same project as the function ([17b7a5b](https://github.com/googleapis/python-functions/commit/17b7a5ba23bb561ea06c58df0436d5fed79d0413))

## [1.12.0](https://github.com/googleapis/python-functions/compare/v1.11.0...v1.12.0) (2023-03-23)


### Features

* Add `available_cpu` field ([af189a0](https://github.com/googleapis/python-functions/commit/af189a0b5f2ef5c29f017cb4265f0011074ce366))
* Add `kms_key_name` field to ServiceConfig (the CMEK use case) ([af189a0](https://github.com/googleapis/python-functions/commit/af189a0b5f2ef5c29f017cb4265f0011074ce366))
* Add `max_instance_request_concurrency` field ([af189a0](https://github.com/googleapis/python-functions/commit/af189a0b5f2ef5c29f017cb4265f0011074ce366))
* Add `security_level` field ([af189a0](https://github.com/googleapis/python-functions/commit/af189a0b5f2ef5c29f017cb4265f0011074ce366))


### Documentation

* Fix formatting of request arg in docstring ([#259](https://github.com/googleapis/python-functions/issues/259)) ([8befe21](https://github.com/googleapis/python-functions/commit/8befe21b1d7bc16112f17fe32c1280ae7fa52ce2))

## [1.11.0](https://github.com/googleapis/python-functions/compare/v1.10.1...v1.11.0) (2023-02-16)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#248](https://github.com/googleapis/python-functions/issues/248)) ([be19686](https://github.com/googleapis/python-functions/commit/be1968686b0e566d1c661369fad84664b65336d2))

## [1.10.1](https://github.com/googleapis/python-functions/compare/v1.10.0...v1.10.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([e50be06](https://github.com/googleapis/python-functions/commit/e50be06af842c476c53d7965a909b28875b23fe4))


### Documentation

* Add documentation for enums ([e50be06](https://github.com/googleapis/python-functions/commit/e50be06af842c476c53d7965a909b28875b23fe4))

## [1.10.0](https://github.com/googleapis/python-functions/compare/v1.9.0...v1.10.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#237](https://github.com/googleapis/python-functions/issues/237)) ([827f45e](https://github.com/googleapis/python-functions/commit/827f45e9aad7857ee36c09ef65a89a9c6d93dfc6))

## [1.9.0](https://github.com/googleapis/python-functions/compare/v1.8.3...v1.9.0) (2022-12-14)


### Features

* Add support for `google.cloud.functions.__version__` ([8fa10be](https://github.com/googleapis/python-functions/commit/8fa10be9991622bfba4a5f974917281ff79bd04e))
* Add typing to proto.Message based class attributes ([8fa10be](https://github.com/googleapis/python-functions/commit/8fa10be9991622bfba4a5f974917281ff79bd04e))


### Bug Fixes

* Add dict typing for client_options ([8fa10be](https://github.com/googleapis/python-functions/commit/8fa10be9991622bfba4a5f974917281ff79bd04e))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([716d441](https://github.com/googleapis/python-functions/commit/716d4413770dc29bd8c3cd21ac5d4abce8053521))
* Drop usage of pkg_resources ([716d441](https://github.com/googleapis/python-functions/commit/716d4413770dc29bd8c3cd21ac5d4abce8053521))
* Fix timeout default values ([716d441](https://github.com/googleapis/python-functions/commit/716d4413770dc29bd8c3cd21ac5d4abce8053521))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([8fa10be](https://github.com/googleapis/python-functions/commit/8fa10be9991622bfba4a5f974917281ff79bd04e))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([716d441](https://github.com/googleapis/python-functions/commit/716d4413770dc29bd8c3cd21ac5d4abce8053521))

## [1.8.3](https://github.com/googleapis/python-functions/compare/v1.8.2...v1.8.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#227](https://github.com/googleapis/python-functions/issues/227)) ([496d3e4](https://github.com/googleapis/python-functions/commit/496d3e40962afe45825b5ea923fdae78957bd5e6))

## [1.8.2](https://github.com/googleapis/python-functions/compare/v1.8.1...v1.8.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#224](https://github.com/googleapis/python-functions/issues/224)) ([63e1cd1](https://github.com/googleapis/python-functions/commit/63e1cd10e16d42e54ba8b25822a13d77a76fe0cb))

## [1.8.1](https://github.com/googleapis/python-functions/compare/v1.8.0...v1.8.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#207](https://github.com/googleapis/python-functions/issues/207)) ([bdc415b](https://github.com/googleapis/python-functions/commit/bdc415b435de8de9072e136cee7d27e9cd802d2c))
* **deps:** require proto-plus >= 1.22.0 ([bdc415b](https://github.com/googleapis/python-functions/commit/bdc415b435de8de9072e136cee7d27e9cd802d2c))

## [1.8.0](https://github.com/googleapis/python-functions/compare/v1.7.0...v1.8.0) (2022-07-14)


### Features

* add audience parameter ([10a61fa](https://github.com/googleapis/python-functions/commit/10a61fa9fd9b0f343a2acfab83dea95011984e34))
* generate v2 ([#195](https://github.com/googleapis/python-functions/issues/195)) ([10a61fa](https://github.com/googleapis/python-functions/commit/10a61fa9fd9b0f343a2acfab83dea95011984e34))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([10a61fa](https://github.com/googleapis/python-functions/commit/10a61fa9fd9b0f343a2acfab83dea95011984e34))
* require python 3.7+ ([#197](https://github.com/googleapis/python-functions/issues/197)) ([6ed2206](https://github.com/googleapis/python-functions/commit/6ed2206eabbdad9a297d19a8b6893cc00b839dcc))

## [1.7.0](https://github.com/googleapis/python-functions/compare/v1.6.0...v1.7.0) (2022-06-06)


### Features

* added support for CMEK ([#188](https://github.com/googleapis/python-functions/issues/188)) ([fa7d695](https://github.com/googleapis/python-functions/commit/fa7d695822e8dc6bb26a2d17800a312c3220fc4c))


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#184](https://github.com/googleapis/python-functions/issues/184)) ([d1e8907](https://github.com/googleapis/python-functions/commit/d1e8907c5862549a412424009a7621b1f321548a))


### Documentation

* fix changelog header to consistent size ([#183](https://github.com/googleapis/python-functions/issues/183)) ([b28c780](https://github.com/googleapis/python-functions/commit/b28c780a405faaf4b068a8e2860932bab4f2ebd9))

## [1.6.0](https://github.com/googleapis/python-functions/compare/v1.5.2...v1.6.0) (2022-04-14)


### Features

* AuditConfig for IAM v1 ([784539c](https://github.com/googleapis/python-functions/commit/784539cbe13583722195f21780781c682ba8c7ac))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([784539c](https://github.com/googleapis/python-functions/commit/784539cbe13583722195f21780781c682ba8c7ac))

## [1.5.2](https://github.com/googleapis/python-functions/compare/v1.5.1...v1.5.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#157](https://github.com/googleapis/python-functions/issues/157)) ([68d56b4](https://github.com/googleapis/python-functions/commit/68d56b41fe472e30101030b8604d7c064acc33d6))
* **deps:** require proto-plus>=1.15.0 ([68d56b4](https://github.com/googleapis/python-functions/commit/68d56b41fe472e30101030b8604d7c064acc33d6))

## [1.5.1](https://github.com/googleapis/python-functions/compare/v1.5.0...v1.5.1) (2022-02-26)


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([80fe038](https://github.com/googleapis/python-functions/commit/80fe038f05f695177cb2366bb92063b485c2bc38))

## [1.5.0](https://github.com/googleapis/python-functions/compare/v1.4.0...v1.5.0) (2022-01-25)


### Features

* add api key support ([#146](https://github.com/googleapis/python-functions/issues/146)) ([258eb69](https://github.com/googleapis/python-functions/commit/258eb698ed1c1adb92b039661ba78b17dc2f5851))

## [1.4.0](https://www.github.com/googleapis/python-functions/compare/v1.3.1...v1.4.0) (2021-11-05)


### Features

* CMEK integration fields 'kms_key_name' and 'docker_repository' added ([47c99d0](https://www.github.com/googleapis/python-functions/commit/47c99d0ea2e5e7d74d10976ea1ec7d8d399e06a4))
* Secret Manager integration fields 'secret_environment_variables' and 'secret_volumes' added ([#130](https://www.github.com/googleapis/python-functions/issues/130)) ([47c99d0](https://www.github.com/googleapis/python-functions/commit/47c99d0ea2e5e7d74d10976ea1ec7d8d399e06a4))

## [1.3.1](https://www.github.com/googleapis/python-functions/compare/v1.3.0...v1.3.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([7076c62](https://www.github.com/googleapis/python-functions/commit/7076c62bf0d9ba93c1ad2726978224f1f7402ab9))
* **deps:** require google-api-core >= 1.28.0 ([7076c62](https://www.github.com/googleapis/python-functions/commit/7076c62bf0d9ba93c1ad2726978224f1f7402ab9))


### Documentation

* list oneofs in docstring ([7076c62](https://www.github.com/googleapis/python-functions/commit/7076c62bf0d9ba93c1ad2726978224f1f7402ab9))

## [1.3.0](https://www.github.com/googleapis/python-functions/compare/v1.2.0...v1.3.0) (2021-10-21)


### Features

* add support for python 3.10 ([#122](https://www.github.com/googleapis/python-functions/issues/122)) ([f7ceeeb](https://www.github.com/googleapis/python-functions/commit/f7ceeebc09d826394f9bb225a823ec504161ac1f))

## [1.2.0](https://www.github.com/googleapis/python-functions/compare/v1.1.1...v1.2.0) (2021-10-08)


### Features

* add context manager support in client ([#119](https://www.github.com/googleapis/python-functions/issues/119)) ([66772fa](https://www.github.com/googleapis/python-functions/commit/66772faffc88aeb6e84984f402902d51c2d786b2))

## [1.1.1](https://www.github.com/googleapis/python-functions/compare/v1.1.0...v1.1.1) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([ef050bd](https://www.github.com/googleapis/python-functions/commit/ef050bd15318cd9ca4481502411e16bf5c7f2c2e))

## [1.1.0](https://www.github.com/googleapis/python-functions/compare/v1.0.4...v1.1.0) (2021-09-16)


### Features

* add SecurityLevel option on HttpsTrigger ([#109](https://www.github.com/googleapis/python-functions/issues/109)) ([91aa229](https://www.github.com/googleapis/python-functions/commit/91aa229a10b7a6fcdfeb03b2566f4f5a2702636e))

## [1.0.4](https://www.github.com/googleapis/python-functions/compare/v1.0.3...v1.0.4) (2021-08-30)


### Documentation

* minor formatting fixes to Cloud Functions reference docs ([#98](https://www.github.com/googleapis/python-functions/issues/98)) ([05f10cf](https://www.github.com/googleapis/python-functions/commit/05f10cfc3d735d04806a25630875c5ecb3bad65d))

## [1.0.3](https://www.github.com/googleapis/python-functions/compare/v1.0.2...v1.0.3) (2021-08-07)


### Bug Fixes

* Updating behavior of source_upload_url during Get/List function calls ([#93](https://www.github.com/googleapis/python-functions/issues/93)) ([264984c](https://www.github.com/googleapis/python-functions/commit/264984cda2a6a1b75a4e5d78268b35d247ebdd99))

## [1.0.2](https://www.github.com/googleapis/python-functions/compare/v1.0.1...v1.0.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#90](https://www.github.com/googleapis/python-functions/issues/90)) ([03bd652](https://www.github.com/googleapis/python-functions/commit/03bd652e1016ab88dbb458311ad82828219637c9))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#86](https://www.github.com/googleapis/python-functions/issues/86)) ([a20de35](https://www.github.com/googleapis/python-functions/commit/a20de355fc32f6849c7ad5a9c5e16f436483fec5))


### Miscellaneous Chores

* release as 1.0.2 ([#91](https://www.github.com/googleapis/python-functions/issues/91)) ([a0f104c](https://www.github.com/googleapis/python-functions/commit/a0f104c51302a8065e35b3eff25b5031f5110162))

## [1.0.1](https://www.github.com/googleapis/python-functions/compare/v1.0.0...v1.0.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#85](https://www.github.com/googleapis/python-functions/issues/85)) ([5ad78fb](https://www.github.com/googleapis/python-functions/commit/5ad78fb363b8aa4057f8dc76ebac35dbdf5c39f7))

## [1.0.0](https://www.github.com/googleapis/python-functions/compare/v0.7.0...v1.0.0) (2021-06-30)


### Features

* bump release level to production/stable ([#65](https://www.github.com/googleapis/python-functions/issues/65)) ([b0f9d70](https://www.github.com/googleapis/python-functions/commit/b0f9d70287cf4c330523d052371793ad7faf33ae))

## [0.7.0](https://www.github.com/googleapis/python-functions/compare/v0.6.1...v0.7.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#77](https://www.github.com/googleapis/python-functions/issues/77)) ([d2005b7](https://www.github.com/googleapis/python-functions/commit/d2005b7770232d855f47b5037a176a7679b6366a))


### Bug Fixes

* disable always_use_jwt_access ([#81](https://www.github.com/googleapis/python-functions/issues/81)) ([81072d3](https://www.github.com/googleapis/python-functions/commit/81072d3225c9f7b17becd981b8bc0f53cdf8f613))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-functions/issues/1127)) ([#72](https://www.github.com/googleapis/python-functions/issues/72)) ([ec7129a](https://www.github.com/googleapis/python-functions/commit/ec7129a4ce543a08db862f30bc67d394d5a7ef9c)), closes [#1126](https://www.github.com/googleapis/python-functions/issues/1126)

## [0.6.1](https://www.github.com/googleapis/python-functions/compare/v0.6.0...v0.6.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#69](https://www.github.com/googleapis/python-functions/issues/69)) ([c75b52b](https://www.github.com/googleapis/python-functions/commit/c75b52bcc46d13f8f5ad61b91d5b7ced9c1b1e15))

## [0.6.0](https://www.github.com/googleapis/python-functions/compare/v0.5.1...v0.6.0) (2021-05-28)


### Features

* support self-signed JWT flow for service accounts ([167f431](https://www.github.com/googleapis/python-functions/commit/167f43144f4f9c5ef88a68bd880ec47a3062a3b6))


### Bug Fixes

* add async client to %name_%version/init.py ([167f431](https://www.github.com/googleapis/python-functions/commit/167f43144f4f9c5ef88a68bd880ec47a3062a3b6))
* **deps:** add packaging requirement ([#62](https://www.github.com/googleapis/python-functions/issues/62)) ([1384f55](https://www.github.com/googleapis/python-functions/commit/1384f55b4e35f6263d42639667c4a38ab1689b16))
* use correct default retry and timeout ([#42](https://www.github.com/googleapis/python-functions/issues/42)) ([8c7db91](https://www.github.com/googleapis/python-functions/commit/8c7db919535193151ed52465a3038d3ac72d701e))

## [0.5.1](https://www.github.com/googleapis/python-functions/compare/v0.5.0...v0.5.1) (2021-02-08)


### Bug Fixes

* remove client recv msg limit and add enums to `types/__init__.py` ([#26](https://www.github.com/googleapis/python-functions/issues/26)) ([207db35](https://www.github.com/googleapis/python-functions/commit/207db35e31d203120f66d384932e54fafec44a08))

## [0.5.0](https://www.github.com/googleapis/python-functions/compare/v0.4.0...v0.5.0) (2020-12-07)


### Features

* add common resource helper paths, expose client transport ([#17](https://www.github.com/googleapis/python-functions/issues/17)) ([e2660f2](https://www.github.com/googleapis/python-functions/commit/e2660f2c53055560c2e7848fa3969d1440aebb62))


### Documentation

* fix link to documentation ([#24](https://www.github.com/googleapis/python-functions/issues/24)) ([8f3ef44](https://www.github.com/googleapis/python-functions/commit/8f3ef446c1ffc5a3395773a70450624c0de99526)), closes [#22](https://www.github.com/googleapis/python-functions/issues/22)

## [0.4.0](https://www.github.com/googleapis/python-functions/compare/v0.1.0...v0.4.0) (2020-10-02)


### Features

* release 0.4.0 ([#7](https://www.github.com/googleapis/python-functions/issues/7)) ([e4e3997](https://www.github.com/googleapis/python-functions/commit/e4e3997cca3d8bdafe04e4931e73da5e934cb769))

## 0.1.0 (2020-07-20)


### Features

* generate v1 ([9a67e29](https://www.github.com/googleapis/python-functions/commit/9a67e29b73b6e653e1d9c5f7c83e44c7f312ab12))
