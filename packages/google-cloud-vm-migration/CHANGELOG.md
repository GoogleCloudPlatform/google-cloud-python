# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-vm-migration/#history

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.17.0...google-cloud-vm-migration-v1.18.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.16.0...google-cloud-vm-migration-v1.17.0) (2026-06-22)


### Features

* regenerate google-cloud-[t-w] packages ([#17076](https://github.com/googleapis/google-cloud-python/issues/17076)) ([928a03c](https://github.com/googleapis/google-cloud-python/commit/928a03ce41fbcb82398636e89f840c00c7749cf8))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.15.0...google-cloud-vm-migration-v1.16.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.14.0...google-cloud-vm-migration-v1.15.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.13.0...google-cloud-vm-migration-v1.14.0) (2025-12-04)


### Documentation

* A comment for message `DataDiskImageImport` is changed ([c958ebdfe9351d3d4e80d388a6e95804b515d030](https://github.com/googleapis/google-cloud-python/commit/c958ebdfe9351d3d4e80d388a6e95804b515d030))
* A comment for method `CancelImageImportJob` in service `VmMigration` is changed ([c958ebdfe9351d3d4e80d388a6e95804b515d030](https://github.com/googleapis/google-cloud-python/commit/c958ebdfe9351d3d4e80d388a6e95804b515d030))


### Features

* add adaptation modifiers and guest OS features to ImageImport target details ([c958ebdfe9351d3d4e80d388a6e95804b515d030](https://github.com/googleapis/google-cloud-python/commit/c958ebdfe9351d3d4e80d388a6e95804b515d030))
* add adaptation modifiers and storage pools to MigratingVM target defaults ([c958ebdfe9351d3d4e80d388a6e95804b515d030](https://github.com/googleapis/google-cloud-python/commit/c958ebdfe9351d3d4e80d388a6e95804b515d030))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.12.0...google-cloud-vm-migration-v1.13.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.11.3...google-cloud-vm-migration-v1.12.0) (2025-09-08)


### Features

* API for extending the time to live (TTL) of a Migrating VM ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Azure as a source ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* CMEK support ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Cutover forecast ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Image Import ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Machine Image Import ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Migration warnings in addition to errors ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Multiple additional supported target details ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* OS capabilities detection ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* VM disk migration ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))


### Bug Fixes

* Changed field behavior for an existing field `key` in message `.google.cloud.vmmigration.v1.AwsSourceDetails` to `required` to protect from incorrect input ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Changed field behavior for an existing field `project` in message `.google.cloud.vmmigration.v1.TargetProject` to `required` to protect from incorrect input ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))
* Changed field behavior for an existing field `value` in message `.google.cloud.vmmigration.v1.AwsSourceDetails` to `required` to protect from incorrect input ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))


### Documentation

* Updated comments and descriptions to improve clarity ([6b7325d](https://github.com/googleapis/google-cloud-python/commit/6b7325d5339c513f4567d0b745c2d1b9fac3fc24))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.11.2...google-cloud-vm-migration-v1.11.3) (2025-06-11)


### Documentation

* Update import statement example in README ([0131a33](https://github.com/googleapis/google-cloud-python/commit/0131a33582f84d9be5ecb1c0ef8b56aa3d9e9cf0))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.11.1...google-cloud-vm-migration-v1.11.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([4757dae](https://github.com/googleapis/google-cloud-python/commit/4757daede978618382ba46f4aa91bb9cfd9b937b))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.11.0...google-cloud-vm-migration-v1.11.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([0c5f868](https://github.com/googleapis/google-cloud-python/commit/0c5f86820c42e5cd857c1a0eef25f5e6a65b2ad8))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.10.0...google-cloud-vm-migration-v1.11.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))
* Add support for reading selective GAPIC generation methods from service YAML ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.9.1...google-cloud-vm-migration-v1.10.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.9.0...google-cloud-vm-migration-v1.9.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13246](https://github.com/googleapis/google-cloud-python/issues/13246)) ([bcad563](https://github.com/googleapis/google-cloud-python/commit/bcad563acea541bb51f9fbd005f18e9f32e381f0))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.8.5...google-cloud-vm-migration-v1.9.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13210](https://github.com/googleapis/google-cloud-python/issues/13210)) ([0b62ac6](https://github.com/googleapis/google-cloud-python/commit/0b62ac6aa99bd3259a088097630f2bd1f06825e6))

## [1.8.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.8.4...google-cloud-vm-migration-v1.8.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([9cdac77](https://github.com/googleapis/google-cloud-python/commit/9cdac77b20a8c9720aa668639e3ca6d1e759a2de))

## [1.8.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.8.3...google-cloud-vm-migration-v1.8.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12870](https://github.com/googleapis/google-cloud-python/issues/12870)) ([4d16761](https://github.com/googleapis/google-cloud-python/commit/4d16761640dd8e35410b3219b7d675d7668d2f88))

## [1.8.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.8.2...google-cloud-vm-migration-v1.8.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12388](https://github.com/googleapis/google-cloud-python/issues/12388)) ([d2cd4ff](https://github.com/googleapis/google-cloud-python/commit/d2cd4ffd12467ad512cccd7a0e9bb897ff2ce2a7))

## [1.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.8.1...google-cloud-vm-migration-v1.8.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12310](https://github.com/googleapis/google-cloud-python/issues/12310)) ([41821da](https://github.com/googleapis/google-cloud-python/commit/41821da1fe08cc2aeeefc8c8f516023e4b0d0700))
* fix ValueError in test__validate_universe_domain ([f3974d4](https://github.com/googleapis/google-cloud-python/commit/f3974d46a9ba9f549e31251ebc2daeb6b9b4745a))

## [1.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.8.0...google-cloud-vm-migration-v1.8.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.7.0...google-cloud-vm-migration-v1.8.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12244](https://github.com/googleapis/google-cloud-python/issues/12244)) ([8d6b772](https://github.com/googleapis/google-cloud-python/commit/8d6b7729d93c1347529a3d34ed6266af55225578))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.6.3...google-cloud-vm-migration-v1.7.0) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [1.6.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.6.2...google-cloud-vm-migration-v1.6.3) (2023-09-19)


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.6.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-vm-migration-v1.6.1...google-cloud-vm-migration-v1.6.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [1.6.1](https://github.com/googleapis/python-vm-migration/compare/v1.6.0...v1.6.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#119](https://github.com/googleapis/python-vm-migration/issues/119)) ([cc95fb4](https://github.com/googleapis/python-vm-migration/commit/cc95fb484f188cf7967457a342a2f11da9c4db23))

## [1.6.0](https://github.com/googleapis/python-vm-migration/compare/v1.5.1...v1.6.0) (2023-02-09)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#113](https://github.com/googleapis/python-vm-migration/issues/113)) ([f6d145d](https://github.com/googleapis/python-vm-migration/commit/f6d145d8ae1b287f55a381436273ffaa717381b7))

## [1.5.1](https://github.com/googleapis/python-vm-migration/compare/v1.5.0...v1.5.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([a25c621](https://github.com/googleapis/python-vm-migration/commit/a25c621955f2b293a7020b9413f393959d69b344))


### Documentation

* Add documentation for enums ([a25c621](https://github.com/googleapis/python-vm-migration/commit/a25c621955f2b293a7020b9413f393959d69b344))

## [1.5.0](https://github.com/googleapis/python-vm-migration/compare/v1.4.0...v1.5.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#106](https://github.com/googleapis/python-vm-migration/issues/106)) ([d0192a1](https://github.com/googleapis/python-vm-migration/commit/d0192a19b22a517c5ab49964d9b38e7eaf34f30a))
* AWS as a source  ([6430190](https://github.com/googleapis/python-vm-migration/commit/6430190d31af9f24747e9d1395c84ff32ea32898))
* Cycle\Clone\Cutover steps ([6430190](https://github.com/googleapis/python-vm-migration/commit/6430190d31af9f24747e9d1395c84ff32ea32898))
* Cycles history ([6430190](https://github.com/googleapis/python-vm-migration/commit/6430190d31af9f24747e9d1395c84ff32ea32898))

## [1.4.0](https://github.com/googleapis/python-vm-migration/compare/v1.3.3...v1.4.0) (2022-12-15)


### Features

* Add support for `google.cloud.vmmigration.__version__` ([10abf02](https://github.com/googleapis/python-vm-migration/commit/10abf02cfd5aa474d4a78de135e34836d3e4fd03))
* Add typing to proto.Message based class attributes ([10abf02](https://github.com/googleapis/python-vm-migration/commit/10abf02cfd5aa474d4a78de135e34836d3e4fd03))


### Bug Fixes

* Add dict typing for client_options ([10abf02](https://github.com/googleapis/python-vm-migration/commit/10abf02cfd5aa474d4a78de135e34836d3e4fd03))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([fbef486](https://github.com/googleapis/python-vm-migration/commit/fbef486e187c595a1eb74837166c190787837a92))
* Drop usage of pkg_resources ([fbef486](https://github.com/googleapis/python-vm-migration/commit/fbef486e187c595a1eb74837166c190787837a92))
* Fix timeout default values ([fbef486](https://github.com/googleapis/python-vm-migration/commit/fbef486e187c595a1eb74837166c190787837a92))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([10abf02](https://github.com/googleapis/python-vm-migration/commit/10abf02cfd5aa474d4a78de135e34836d3e4fd03))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([fbef486](https://github.com/googleapis/python-vm-migration/commit/fbef486e187c595a1eb74837166c190787837a92))

## [1.3.3](https://github.com/googleapis/python-vm-migration/compare/v1.3.2...v1.3.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#94](https://github.com/googleapis/python-vm-migration/issues/94)) ([f1fdfb0](https://github.com/googleapis/python-vm-migration/commit/f1fdfb079272c277ac9061c16f679f364f0ca646))

## [1.3.2](https://github.com/googleapis/python-vm-migration/compare/v1.3.1...v1.3.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#92](https://github.com/googleapis/python-vm-migration/issues/92)) ([d962e5a](https://github.com/googleapis/python-vm-migration/commit/d962e5a7f9db2397c26cac2ebea0271e10b9341b))

## [1.3.1](https://github.com/googleapis/python-vm-migration/compare/v1.3.0...v1.3.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#69](https://github.com/googleapis/python-vm-migration/issues/69)) ([d4d1ba8](https://github.com/googleapis/python-vm-migration/commit/d4d1ba873f490e30a85efb8a2df8c0ca3edf8daa))
* **deps:** require proto-plus >= 1.22.0 ([d4d1ba8](https://github.com/googleapis/python-vm-migration/commit/d4d1ba873f490e30a85efb8a2df8c0ca3edf8daa))

## [1.3.0](https://github.com/googleapis/python-vm-migration/compare/v1.2.0...v1.3.0) (2022-07-19)


### Features

* add ApplianceVersion, AvailableUpdates, MigratingVmView, UpgradeApplianceRequest, UpgradeApplianceResponse, UpgradeStatus ([#64](https://github.com/googleapis/python-vm-migration/issues/64)) ([839fac4](https://github.com/googleapis/python-vm-migration/commit/839fac47189552905a80d8443df90cd8f97829fe))

## [1.2.0](https://github.com/googleapis/python-vm-migration/compare/v1.1.2...v1.2.0) (2022-07-16)


### Features

* add audience parameter ([61827e2](https://github.com/googleapis/python-vm-migration/commit/61827e246c7aae16537d00095737a47ccf537f90))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#61](https://github.com/googleapis/python-vm-migration/issues/61)) ([2e7fb1e](https://github.com/googleapis/python-vm-migration/commit/2e7fb1ef0d7069cd22f64de464148940c8330ac2))
* require python 3.7+ ([#59](https://github.com/googleapis/python-vm-migration/issues/59)) ([af250ac](https://github.com/googleapis/python-vm-migration/commit/af250ac6e3307ce002b5c2cedd3878342e580c7e))

## [1.1.2](https://github.com/googleapis/python-vm-migration/compare/v1.1.1...v1.1.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#48](https://github.com/googleapis/python-vm-migration/issues/48)) ([c5c3155](https://github.com/googleapis/python-vm-migration/commit/c5c3155f62d5f46ac4f5071d68af0c448edcd93d))


### Documentation

* fix changelog header to consistent size ([#49](https://github.com/googleapis/python-vm-migration/issues/49)) ([1f5f92a](https://github.com/googleapis/python-vm-migration/commit/1f5f92ab6422e9b737a9f8e597501eb0cf17b798))

## [1.1.1](https://github.com/googleapis/python-vm-migration/compare/v1.1.0...v1.1.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#24](https://github.com/googleapis/python-vm-migration/issues/24)) ([0ee06fd](https://github.com/googleapis/python-vm-migration/commit/0ee06fda92a66981f21b0fe546335362f4fc8d80))

## [1.1.0](https://github.com/googleapis/python-vm-migration/compare/v1.0.0...v1.1.0) (2022-02-11)


### Features

* add api key support ([#14](https://github.com/googleapis/python-vm-migration/issues/14)) ([bf6760c](https://github.com/googleapis/python-vm-migration/commit/bf6760ce5ead26b352a5a89e079fa2ca20c0c3c6))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([c53543e](https://github.com/googleapis/python-vm-migration/commit/c53543e159c2513089223fdc956860a051244c29))

## [1.0.0](https://github.com/googleapis/python-vm-migration/compare/v0.1.0...v1.0.0) (2022-01-24)


### Features

* bump release level to production/stable ([#4](https://github.com/googleapis/python-vm-migration/issues/4)) ([23b4a5e](https://github.com/googleapis/python-vm-migration/commit/23b4a5ef93452580a4587e3d95163fcf664ed39f))

## 0.1.0 (2021-11-18)


### Features

* generate v1 ([4041de0](https://www.github.com/googleapis/python-vm-migration/commit/4041de00804957fddba57f6e972c7ed1415354f9))
