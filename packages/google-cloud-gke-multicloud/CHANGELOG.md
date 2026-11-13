# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-gke-multicloud/#history

## [0.9.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.9.1...google-cloud-gke-multicloud-v0.9.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.9.0...google-cloud-gke-multicloud-v0.9.1) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.8.0...google-cloud-gke-multicloud-v0.9.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.7.0...google-cloud-gke-multicloud-v0.8.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.22...google-cloud-gke-multicloud-v0.7.0) (2025-12-04)


### Documentation

* A comment for field `tags` in message `.google.cloud.gkemulticloud.v1.AttachedCluster` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `throughput` in message `.google.cloud.gkemulticloud.v1.AwsVolumeTemplate` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `requested_cancellation` in message `.google.cloud.gkemulticloud.v1.OperationMetadata` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))


### Features

* added custom tolerations and labels support for Attached Clusters ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* mark GKE-on-AWS and GKE-on-Azure protos as being deprecated to discourage any new usage as these services turn down ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))

## [0.6.22](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.21...google-cloud-gke-multicloud-v0.6.22) (2025-10-14)


### Features

* Add support for Python 3.14 ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))


### Bug Fixes

* Deprecate credentials_file argument ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))

## [0.6.21](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.20...google-cloud-gke-multicloud-v0.6.21) (2025-06-11)


### Documentation

* Update import statement example in README ([821bdb1](https://github.com/googleapis/google-cloud-python/commit/821bdb1d108c8e77a7a576557aa95d4b9c943e12))

## [0.6.20](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.19...google-cloud-gke-multicloud-v0.6.20) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.6.19](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.18...google-cloud-gke-multicloud-v0.6.19) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [0.6.18](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.17...google-cloud-gke-multicloud-v0.6.18) (2025-01-13)


### Documentation

* [google-cloud-gke-multicloud] fix comments of existing field ([#13417](https://github.com/googleapis/google-cloud-python/issues/13417)) ([3a9a8fb](https://github.com/googleapis/google-cloud-python/commit/3a9a8fb2be1304ff8d4593320236e1ea008ee696))

## [0.6.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.16...google-cloud-gke-multicloud-v0.6.17) (2025-01-02)


### Features

* added support for optionally disabling built-in GKE metrics ([57232b6](https://github.com/googleapis/google-cloud-python/commit/57232b6b38c004c5136a8ad8051fa1f667d2353d))
* added tag bindings support for Attached Clusters ([57232b6](https://github.com/googleapis/google-cloud-python/commit/57232b6b38c004c5136a8ad8051fa1f667d2353d))


### Documentation

* updated comments of existing fields ([57232b6](https://github.com/googleapis/google-cloud-python/commit/57232b6b38c004c5136a8ad8051fa1f667d2353d))

## [0.6.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.15...google-cloud-gke-multicloud-v0.6.16) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [0.6.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.14...google-cloud-gke-multicloud-v0.6.15) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [0.6.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.13...google-cloud-gke-multicloud-v0.6.14) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13207](https://github.com/googleapis/google-cloud-python/issues/13207)) ([ceb9be8](https://github.com/googleapis/google-cloud-python/commit/ceb9be8f89ac7355d842bac1d77b2926eb0b649c))

## [0.6.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.12...google-cloud-gke-multicloud-v0.6.13) (2024-09-16)


### Features

* An optional field `kubelet_config` in message `.google.cloud.gkemulticloud.v1.AwsNodePool` is added ([33834de](https://github.com/googleapis/google-cloud-python/commit/33834de6d9eeced6da30f3fcbeb4e1029e07cf18))
* An optional field `security_posture_config` in message `.google.cloud.gkemulticloud.v1.AttachedCluster` is added ([33834de](https://github.com/googleapis/google-cloud-python/commit/33834de6d9eeced6da30f3fcbeb4e1029e07cf18))

## [0.6.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.11...google-cloud-gke-multicloud-v0.6.12) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [0.6.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.10...google-cloud-gke-multicloud-v0.6.11) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12867](https://github.com/googleapis/google-cloud-python/issues/12867)) ([3362176](https://github.com/googleapis/google-cloud-python/commit/33621762b989106ccf85adb538cf531c513a746c))

## [0.6.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.9...google-cloud-gke-multicloud-v0.6.10) (2024-05-16)


### Features

* [google-cloud-gke-multicloud] option to ignore_errors while deleting Azure clusters / nodepools ([#12686](https://github.com/googleapis/google-cloud-python/issues/12686)) ([3d1901e](https://github.com/googleapis/google-cloud-python/commit/3d1901ee7d9412db4ca9ee7d10dc05a07976d387))

## [0.6.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.8...google-cloud-gke-multicloud-v0.6.9) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12385](https://github.com/googleapis/google-cloud-python/issues/12385)) ([d50f4d0](https://github.com/googleapis/google-cloud-python/commit/d50f4d042774e2f12e9fe03459eae9ce91247df3))

## [0.6.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.7...google-cloud-gke-multicloud-v0.6.8) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12307](https://github.com/googleapis/google-cloud-python/issues/12307)) ([be87bc4](https://github.com/googleapis/google-cloud-python/commit/be87bc4a33fe32a512448a42246c9873da88269f))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [0.6.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.6...google-cloud-gke-multicloud-v0.6.7) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))

## [0.6.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.5...google-cloud-gke-multicloud-v0.6.6) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [0.6.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.4...google-cloud-gke-multicloud-v0.6.5) (2024-01-04)


### Features

* added Binary Authorization support which is a deploy-time security control that ensures only trusted container images are deployed ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added force-deletion support for AWS Clusters & Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added proxy support for Attached Clusters ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added support for a new admin-groups flag in the create and update APIs ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added support for EC2 Spot instance types for AWS Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added support for per-node-pool subnet security group rules for AWS Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added Surge Update and Rollback support for AWS Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* expanded Kubernetes version info ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))


### Documentation

* updated comments of existing fields ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))

## [0.6.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.3...google-cloud-gke-multicloud-v0.6.4) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [0.6.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.2...google-cloud-gke-multicloud-v0.6.3) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.1...google-cloud-gke-multicloud-v0.6.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [0.6.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.6.0...v0.6.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#66](https://github.com/googleapis/python-gke-multicloud/issues/66)) ([cabb6f7](https://github.com/googleapis/python-gke-multicloud/commit/cabb6f70c159dd06f34b03bff36f005d0cc08d35))

## [0.6.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.5.1...v0.6.0) (2023-02-02)


### Features

* Added `reconciling` and `update_time` output fields to Azure Client resource. ([76ed673](https://github.com/googleapis/python-gke-multicloud/commit/76ed673d5438471fa90cf2a1cd3f721b1efdada1))
* Added support for Azure workload identity federation ([76ed673](https://github.com/googleapis/python-gke-multicloud/commit/76ed673d5438471fa90cf2a1cd3f721b1efdada1))

## [0.5.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.5.0...v0.5.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([970b8d3](https://github.com/googleapis/python-gke-multicloud/commit/970b8d3a969d936e617d911de276816ec90a278a))


### Documentation

* Add documentation for enums ([970b8d3](https://github.com/googleapis/python-gke-multicloud/commit/970b8d3a969d936e617d911de276816ec90a278a))

## [0.5.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.4.0...v0.5.0) (2023-01-12)


### Features

* Add support for python 3.11 ([#48](https://github.com/googleapis/python-gke-multicloud/issues/48)) ([e9ac58a](https://github.com/googleapis/python-gke-multicloud/commit/e9ac58ad64daa6ffdd0b346cbdff8a72a775908e))

## [0.4.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.3.0...v0.4.0) (2023-01-04)


### Features

* Add AWS Autoscaling Group metrics collection for AWS nodepools ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))
* Add errors output fields for cluster and nodepool resources ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))
* Add monitoring config ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))
* Support AttachedClusters ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))

## [0.3.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.2.2...v0.3.0) (2022-12-15)


### Features

* Add support for `google.cloud.gke_multicloud.__version__` ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))
* Add typing to proto.Message based class attributes ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))


### Bug Fixes

* Add dict typing for client_options ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))
* Drop usage of pkg_resources ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))
* Fix timeout default values ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))

## [0.2.2](https://github.com/googleapis/python-gke-multicloud/compare/v0.2.1...v0.2.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#34](https://github.com/googleapis/python-gke-multicloud/issues/34)) ([36ffc90](https://github.com/googleapis/python-gke-multicloud/commit/36ffc90db52dfd0a90d26fd4c8c7bbac74269058))
* **deps:** require google-api-core&gt;=1.33.2 ([36ffc90](https://github.com/googleapis/python-gke-multicloud/commit/36ffc90db52dfd0a90d26fd4c8c7bbac74269058))

## [0.2.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.2.0...v0.2.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#31](https://github.com/googleapis/python-gke-multicloud/issues/31)) ([8c73990](https://github.com/googleapis/python-gke-multicloud/commit/8c739901554b87048125d308ded429de4006b025))

## [0.2.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.1.1...v0.2.0) (2022-09-16)


### Features

* Add support for REST transport ([#23](https://github.com/googleapis/python-gke-multicloud/issues/23)) ([763dbc4](https://github.com/googleapis/python-gke-multicloud/commit/763dbc4c4defe4888c815e7c8f6b42a6b8f63468))


### Bug Fixes

* **deps:** require google-api-core>=1.33.1,>=2.8.0 ([763dbc4](https://github.com/googleapis/python-gke-multicloud/commit/763dbc4c4defe4888c815e7c8f6b42a6b8f63468))
* **deps:** require protobuf >= 3.20.1 ([763dbc4](https://github.com/googleapis/python-gke-multicloud/commit/763dbc4c4defe4888c815e7c8f6b42a6b8f63468))

## [0.1.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.1.0...v0.1.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#10](https://github.com/googleapis/python-gke-multicloud/issues/10)) ([d5f33a6](https://github.com/googleapis/python-gke-multicloud/commit/d5f33a6c9a3ecfe6c8eb1feacefe367bf8b92afb))
* **deps:** require proto-plus >= 1.22.0 ([d5f33a6](https://github.com/googleapis/python-gke-multicloud/commit/d5f33a6c9a3ecfe6c8eb1feacefe367bf8b92afb))

## 0.1.0 (2022-07-08)


### Features

* generate v1 ([eb3bd85](https://github.com/googleapis/python-gke-multicloud/commit/eb3bd8516f44889a652422961d38aa5cf4352074))
