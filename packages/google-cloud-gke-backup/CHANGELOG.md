# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-gke-backup/#history

## [0.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.8.1...google-cloud-gke-backup-v0.8.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.8.0...google-cloud-gke-backup-v0.8.1) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.7.0...google-cloud-gke-backup-v0.8.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.6.0...google-cloud-gke-backup-v0.7.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.19...google-cloud-gke-backup-v0.6.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.5.19](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.18...google-cloud-gke-backup-v0.5.19) (2025-05-15)


### Features

* Add BackupChannel field in BackupPlan ([091f988](https://github.com/googleapis/google-cloud-python/commit/091f988fe45f5859c7540dabc809cc20aa9c5bfc))
* Add BackupConfig of Backups in BackupPlanBinding ([091f988](https://github.com/googleapis/google-cloud-python/commit/091f988fe45f5859c7540dabc809cc20aa9c5bfc))
* Add RestoreChannel field in RestorePlan ([091f988](https://github.com/googleapis/google-cloud-python/commit/091f988fe45f5859c7540dabc809cc20aa9c5bfc))
* Add support for Project ID in BackupChannel and RestoreChannel ([091f988](https://github.com/googleapis/google-cloud-python/commit/091f988fe45f5859c7540dabc809cc20aa9c5bfc))


### Documentation

* minor documentation fixes ([091f988](https://github.com/googleapis/google-cloud-python/commit/091f988fe45f5859c7540dabc809cc20aa9c5bfc))

## [0.5.18](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.17...google-cloud-gke-backup-v0.5.18) (2025-04-23)


### Features

* Adding `CLEANED_UP` enum in state field of volume.proto ([5900059](https://github.com/googleapis/google-cloud-python/commit/5900059276c15615ff178952384d0d4ee28e03c8))
* Adding `last_successful_backup_time` field in BackupPlan ([5900059](https://github.com/googleapis/google-cloud-python/commit/5900059276c15615ff178952384d0d4ee28e03c8))
* Adding `VALIDATING` enum in state field of restore.proto ([5900059](https://github.com/googleapis/google-cloud-python/commit/5900059276c15615ff178952384d0d4ee28e03c8))
* Adding new BackupChannel, RestoreChannel, BackupPlanBinding and RestorePlanBinding ([5900059](https://github.com/googleapis/google-cloud-python/commit/5900059276c15615ff178952384d0d4ee28e03c8))


### Documentation

* minor documentation fixes ([5900059](https://github.com/googleapis/google-cloud-python/commit/5900059276c15615ff178952384d0d4ee28e03c8))

## [0.5.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.16...google-cloud-gke-backup-v0.5.17) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.5.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.15...google-cloud-gke-backup-v0.5.16) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([16e14c8](https://github.com/googleapis/google-cloud-python/commit/16e14c8d547864360dcab45d90e9e55169204fc6))

## [0.5.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.14...google-cloud-gke-backup-v0.5.15) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [0.5.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.13...google-cloud-gke-backup-v0.5.14) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [0.5.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.12...google-cloud-gke-backup-v0.5.13) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [0.5.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.11...google-cloud-gke-backup-v0.5.12) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [0.5.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.10...google-cloud-gke-backup-v0.5.11) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [0.5.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.9...google-cloud-gke-backup-v0.5.10) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12867](https://github.com/googleapis/google-cloud-python/issues/12867)) ([3362176](https://github.com/googleapis/google-cloud-python/commit/33621762b989106ccf85adb538cf531c513a746c))

## [0.5.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.8...google-cloud-gke-backup-v0.5.9) (2024-05-27)


### Features

* add fine-grained restore ([9268d28](https://github.com/googleapis/google-cloud-python/commit/9268d284f74af2398f50c3faf7af3278337d3f75))
* add gitops ([9268d28](https://github.com/googleapis/google-cloud-python/commit/9268d284f74af2398f50c3faf7af3278337d3f75))
* add restore order ([9268d28](https://github.com/googleapis/google-cloud-python/commit/9268d284f74af2398f50c3faf7af3278337d3f75))
* add strict-permissive mode ([9268d28](https://github.com/googleapis/google-cloud-python/commit/9268d284f74af2398f50c3faf7af3278337d3f75))
* add volume restore flexibility ([9268d28](https://github.com/googleapis/google-cloud-python/commit/9268d284f74af2398f50c3faf7af3278337d3f75))


### Documentation

* update duration comment to include new validation from smart scheduling ([9268d28](https://github.com/googleapis/google-cloud-python/commit/9268d284f74af2398f50c3faf7af3278337d3f75))

## [0.5.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.7...google-cloud-gke-backup-v0.5.8) (2024-03-26)


### Features

* add backup indexing ([cbe3118](https://github.com/googleapis/google-cloud-python/commit/cbe311847fdb38dc012ca868ccba8521cfedb916))
* add smart scheduling ([cbe3118](https://github.com/googleapis/google-cloud-python/commit/cbe311847fdb38dc012ca868ccba8521cfedb916))


### Documentation

* add output only and optional api field behavior label ([cbe3118](https://github.com/googleapis/google-cloud-python/commit/cbe311847fdb38dc012ca868ccba8521cfedb916))
* remove the next id annotation ([cbe3118](https://github.com/googleapis/google-cloud-python/commit/cbe311847fdb38dc012ca868ccba8521cfedb916))
* update retention policy and cron schedule comment to include new constraints from smart scheduling ([cbe3118](https://github.com/googleapis/google-cloud-python/commit/cbe311847fdb38dc012ca868ccba8521cfedb916))

## [0.5.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.6...google-cloud-gke-backup-v0.5.7) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12384](https://github.com/googleapis/google-cloud-python/issues/12384)) ([c69966f](https://github.com/googleapis/google-cloud-python/commit/c69966fa7aac2cba4e22513e4a053b3754f8ea5e))

## [0.5.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.5...google-cloud-gke-backup-v0.5.6) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [0.5.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.4...google-cloud-gke-backup-v0.5.5) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))

## [0.5.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.3...google-cloud-gke-backup-v0.5.4) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [0.5.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-backup-v0.5.2...google-cloud-gke-backup-v0.5.3) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [0.5.2](https://github.com/googleapis/python-gke-backup/compare/v0.5.1...v0.5.2) (2023-09-13)


### Documentation

* Minor formatting ([#87](https://github.com/googleapis/python-gke-backup/issues/87)) ([137dbdf](https://github.com/googleapis/python-gke-backup/commit/137dbdf3667ff6be8601e664335cd985c4c99f9c))

## [0.5.1](https://github.com/googleapis/python-gke-backup/compare/v0.5.0...v0.5.1) (2023-08-03)


### Documentation

* Minor formatting ([#74](https://github.com/googleapis/python-gke-backup/issues/74)) ([2071a3c](https://github.com/googleapis/python-gke-backup/commit/2071a3cf1e72edd143ebc462c3124b4e3478ae49))

## [0.5.0](https://github.com/googleapis/python-gke-backup/compare/v0.4.4...v0.5.0) (2023-07-04)


### Features

* Added BackupPlan and RestorePlan state information ([8ddab08](https://github.com/googleapis/python-gke-backup/commit/8ddab0894c63bc7c6ffaad027bbc53a38688cbcf))
* Added new restore scope options ([8ddab08](https://github.com/googleapis/python-gke-backup/commit/8ddab0894c63bc7c6ffaad027bbc53a38688cbcf))
* Added transformation rules for restore ([8ddab08](https://github.com/googleapis/python-gke-backup/commit/8ddab0894c63bc7c6ffaad027bbc53a38688cbcf))


### Bug Fixes

* Add async context manager return types ([#72](https://github.com/googleapis/python-gke-backup/issues/72)) ([301ec6d](https://github.com/googleapis/python-gke-backup/commit/301ec6de120e70f94c8938ad8073b4a8ed2dc63d))

## [0.4.4](https://github.com/googleapis/python-gke-backup/compare/v0.4.3...v0.4.4) (2023-06-12)


### Documentation

* Minor documentation fixes ([#66](https://github.com/googleapis/python-gke-backup/issues/66)) ([4ff9cb7](https://github.com/googleapis/python-gke-backup/commit/4ff9cb7c2fdfdf53e9a9b61f615b27b6517fec2c))

## [0.4.3](https://github.com/googleapis/python-gke-backup/compare/v0.4.2...v0.4.3) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#60](https://github.com/googleapis/python-gke-backup/issues/60)) ([911b0ed](https://github.com/googleapis/python-gke-backup/commit/911b0edd7976b83f256a3daaceaa043b2af10fd4))

## [0.4.2](https://github.com/googleapis/python-gke-backup/compare/v0.4.1...v0.4.2) (2023-02-17)


### Bug Fixes

* Add service_yaml_parameters to py_gapic_library BUILD.bazel targets ([#54](https://github.com/googleapis/python-gke-backup/issues/54)) ([d5f4bbd](https://github.com/googleapis/python-gke-backup/commit/d5f4bbd6a6ab6d8d7db65dbbf52ffab59b5645da))

## [0.4.1](https://github.com/googleapis/python-gke-backup/compare/v0.4.0...v0.4.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([5ef7c49](https://github.com/googleapis/python-gke-backup/commit/5ef7c4953fdfe4381aed572c7ed4d9cac8d83553))


### Documentation

* Add documentation for enums ([5ef7c49](https://github.com/googleapis/python-gke-backup/commit/5ef7c4953fdfe4381aed572c7ed4d9cac8d83553))

## [0.4.0](https://github.com/googleapis/python-gke-backup/compare/v0.3.0...v0.4.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#45](https://github.com/googleapis/python-gke-backup/issues/45)) ([ebe4ae2](https://github.com/googleapis/python-gke-backup/commit/ebe4ae22f4570ba84695ad84833dd65c38ed7f29))

## [0.3.0](https://github.com/googleapis/python-gke-backup/compare/v0.2.2...v0.3.0) (2022-12-15)


### Features

* Add support for `google.cloud.gke_backup.__version__` ([f754a3a](https://github.com/googleapis/python-gke-backup/commit/f754a3aee9de6da2419d3b792e900bc0c0bfd732))
* Add typing to proto.Message based class attributes ([f754a3a](https://github.com/googleapis/python-gke-backup/commit/f754a3aee9de6da2419d3b792e900bc0c0bfd732))


### Bug Fixes

* Add dict typing for client_options ([f754a3a](https://github.com/googleapis/python-gke-backup/commit/f754a3aee9de6da2419d3b792e900bc0c0bfd732))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([58b2855](https://github.com/googleapis/python-gke-backup/commit/58b2855280fce1cd11a4300cb10742d153480439))
* Drop usage of pkg_resources ([58b2855](https://github.com/googleapis/python-gke-backup/commit/58b2855280fce1cd11a4300cb10742d153480439))
* Fix timeout default values ([58b2855](https://github.com/googleapis/python-gke-backup/commit/58b2855280fce1cd11a4300cb10742d153480439))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([f754a3a](https://github.com/googleapis/python-gke-backup/commit/f754a3aee9de6da2419d3b792e900bc0c0bfd732))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([58b2855](https://github.com/googleapis/python-gke-backup/commit/58b2855280fce1cd11a4300cb10742d153480439))

## [0.2.2](https://github.com/googleapis/python-gke-backup/compare/v0.2.1...v0.2.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#32](https://github.com/googleapis/python-gke-backup/issues/32)) ([273e5e3](https://github.com/googleapis/python-gke-backup/commit/273e5e37839caf413d854313955f6031098b0b86))
* **deps:** require google-api-core&gt;=1.33.2 ([273e5e3](https://github.com/googleapis/python-gke-backup/commit/273e5e37839caf413d854313955f6031098b0b86))

## [0.2.1](https://github.com/googleapis/python-gke-backup/compare/v0.2.0...v0.2.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#29](https://github.com/googleapis/python-gke-backup/issues/29)) ([4081d9f](https://github.com/googleapis/python-gke-backup/commit/4081d9f0e62358222a7bec96cca05703adfa3cd2))

## [0.2.0](https://github.com/googleapis/python-gke-backup/compare/v0.1.1...v0.2.0) (2022-09-16)


### Features

* Add support for REST transport ([#24](https://github.com/googleapis/python-gke-backup/issues/24)) ([fbaff82](https://github.com/googleapis/python-gke-backup/commit/fbaff8285a3e6efa78c74bec26f681906af60754))


### Bug Fixes

* **deps:** require google-api-core>=1.33.1,>=2.8.0 ([fbaff82](https://github.com/googleapis/python-gke-backup/commit/fbaff8285a3e6efa78c74bec26f681906af60754))
* **deps:** require protobuf >= 3.20.1 ([fbaff82](https://github.com/googleapis/python-gke-backup/commit/fbaff8285a3e6efa78c74bec26f681906af60754))

## [0.1.1](https://github.com/googleapis/python-gke-backup/compare/v0.1.0...v0.1.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#11](https://github.com/googleapis/python-gke-backup/issues/11)) ([ab147e1](https://github.com/googleapis/python-gke-backup/commit/ab147e13c065681719efdeb2ef5cba3ffdee4ca2))
* **deps:** require proto-plus >= 1.22.0 ([ab147e1](https://github.com/googleapis/python-gke-backup/commit/ab147e13c065681719efdeb2ef5cba3ffdee4ca2))

## 0.1.0 (2022-07-08)


### Features

* generate v1 ([2978d06](https://github.com/googleapis/python-gke-backup/commit/2978d068619e9f5fe7599c32464ab9cc7be728f1))
