# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-workstations/#history

## [0.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.8.1...google-cloud-workstations-v0.8.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.8.0...google-cloud-workstations-v0.8.1) (2026-06-22)


### Features

* regenerate google-cloud-[t-w] packages ([#17076](https://github.com/googleapis/google-cloud-python/issues/17076)) ([928a03c](https://github.com/googleapis/google-cloud-python/commit/928a03ce41fbcb82398636e89f840c00c7749cf8))
* update googleapis and regenerate ([33ba3af](https://github.com/googleapis/google-cloud-python/commit/33ba3afe520e2f64ac7464f1b4ee31c0624a65ac))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.7.0...google-cloud-workstations-v0.8.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.6.0...google-cloud-workstations-v0.7.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.15...google-cloud-workstations-v0.6.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.5.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.14...google-cloud-workstations-v0.5.15) (2025-06-11)


### Documentation

* Update import statement example in README ([8066d24](https://github.com/googleapis/google-cloud-python/commit/8066d24068e6d036dcf77e7abb5401a5ba3f8a63))

## [0.5.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.13...google-cloud-workstations-v0.5.14) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([25ced24](https://github.com/googleapis/google-cloud-python/commit/25ced2444528a1dc6a22daa32b82b844961f1b75))

## [0.5.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.12...google-cloud-workstations-v0.5.13) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([0c5f868](https://github.com/googleapis/google-cloud-python/commit/0c5f86820c42e5cd857c1a0eef25f5e6a65b2ad8))

## [0.5.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.11...google-cloud-workstations-v0.5.12) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))
* Add support for reading selective GAPIC generation methods from service YAML ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))

## [0.5.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.10...google-cloud-workstations-v0.5.11) (2024-12-12)


### Features

* Add support for opt-in debug logging ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))

## [0.5.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.9...google-cloud-workstations-v0.5.10) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13247](https://github.com/googleapis/google-cloud-python/issues/13247)) ([5adc8b7](https://github.com/googleapis/google-cloud-python/commit/5adc8b7d2cc8ab9707ab5a65f15270c125cee051))

## [0.5.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.8...google-cloud-workstations-v0.5.9) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13211](https://github.com/googleapis/google-cloud-python/issues/13211)) ([f712162](https://github.com/googleapis/google-cloud-python/commit/f712162c01f065da29fffbbed1e856a1f3876b1b))

## [0.5.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.7...google-cloud-workstations-v0.5.8) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([4adddf4](https://github.com/googleapis/google-cloud-python/commit/4adddf4d90634e454ee006774bfc631fc12c1700))

## [0.5.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.6...google-cloud-workstations-v0.5.7) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12871](https://github.com/googleapis/google-cloud-python/issues/12871)) ([73b35d5](https://github.com/googleapis/google-cloud-python/commit/73b35d56f8626d99ce7c3902a8c223cc09b4ca74))

## [0.5.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.5...google-cloud-workstations-v0.5.6) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12388](https://github.com/googleapis/google-cloud-python/issues/12388)) ([d2cd4ff](https://github.com/googleapis/google-cloud-python/commit/d2cd4ffd12467ad512cccd7a0e9bb897ff2ce2a7))

## [0.5.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.4...google-cloud-workstations-v0.5.5) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12311](https://github.com/googleapis/google-cloud-python/issues/12311)) ([e4c864b](https://github.com/googleapis/google-cloud-python/commit/e4c864b3e67c7f7f33dfb0d2107fa138492ad338))
* fix ValueError in test__validate_universe_domain ([f3974d4](https://github.com/googleapis/google-cloud-python/commit/f3974d46a9ba9f549e31251ebc2daeb6b9b4745a))

## [0.5.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.3...google-cloud-workstations-v0.5.4) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e16032f](https://github.com/googleapis/google-cloud-python/commit/e16032ffe9b15dfd008b51f046dbb10211356998))

## [0.5.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.2...google-cloud-workstations-v0.5.3) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12244](https://github.com/googleapis/google-cloud-python/issues/12244)) ([8d6b772](https://github.com/googleapis/google-cloud-python/commit/8d6b7729d93c1347529a3d34ed6266af55225578))

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.1...google-cloud-workstations-v0.5.2) (2023-12-07)


### Features

* Add support for python 3.12 ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))
* Introduce compatibility with native namespace packages ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))
* Use `retry_async` instead of `retry` in async client ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.5.0...google-cloud-workstations-v0.5.1) (2023-09-19)


### Documentation

* Minor formatting ([77bf61a](https://github.com/googleapis/google-cloud-python/commit/77bf61a36539bc2e6317dca1f954189d5241e4f1))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.4.1...google-cloud-workstations-v0.5.0) (2023-08-31)


### Features

* add config service_account_scopes ([03ea643](https://github.com/googleapis/google-cloud-python/commit/03ea6435209371d3ac18a1a954a5c96ece600c4c))
* add enable_nested_virtualization ([03ea643](https://github.com/googleapis/google-cloud-python/commit/03ea6435209371d3ac18a1a954a5c96ece600c4c))
* add ephemeral_directories ([03ea643](https://github.com/googleapis/google-cloud-python/commit/03ea6435209371d3ac18a1a954a5c96ece600c4c))
* add initial files for google.cloud.workstations.v1 ([#11603](https://github.com/googleapis/google-cloud-python/issues/11603)) ([d355347](https://github.com/googleapis/google-cloud-python/commit/d355347eea116cc74d194c2fc99842f9b907f4ce))
* add output field start_time ([03ea643](https://github.com/googleapis/google-cloud-python/commit/03ea6435209371d3ac18a1a954a5c96ece600c4c))
* add replica_zones ([03ea643](https://github.com/googleapis/google-cloud-python/commit/03ea6435209371d3ac18a1a954a5c96ece600c4c))


### Documentation

* adjust documentation wording & annotations ([03ea643](https://github.com/googleapis/google-cloud-python/commit/03ea6435209371d3ac18a1a954a5c96ece600c4c))

## [0.4.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.4.0...google-cloud-workstations-v0.4.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11449](https://github.com/googleapis/google-cloud-python/issues/11449)) ([3885820](https://github.com/googleapis/google-cloud-python/commit/388582082828e22a517c4f794901ee5dcbc31bd9))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.3.0...google-cloud-workstations-v0.4.0) (2023-05-17)


### Features

* **v1beta:** add auditd support ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))
* **v1beta:** add output field for the control plane IP address ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))
* **v1beta:** add output field for the number of pooled instances ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))
* **v1beta:** add support for accelerators ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))
* **v1beta:** add support for readiness checks ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))
* **v1beta:** add support for workstation-level environment variables ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))


### Documentation

* **v1beta:** adjust documentation wording ([78957ed](https://github.com/googleapis/google-cloud-python/commit/78957ed60b63eb3c5d26912934c77c99b288c3a7))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.2.1...google-cloud-workstations-v0.3.0) (2023-05-11)


### Features

* add output field for the control plane IP address ([60e16ee](https://github.com/googleapis/google-cloud-python/commit/60e16ee099ab5522563e44d307a76af4c8177288))
* add output field for the number of pooled instances ([60e16ee](https://github.com/googleapis/google-cloud-python/commit/60e16ee099ab5522563e44d307a76af4c8177288))


### Documentation

* adjust documentation wording ([60e16ee](https://github.com/googleapis/google-cloud-python/commit/60e16ee099ab5522563e44d307a76af4c8177288))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.2.0...google-cloud-workstations-v0.2.1) (2023-04-11)


### Documentation

* Adjust wording around service accounts and control planes ([#11057](https://github.com/googleapis/google-cloud-python/issues/11057)) ([9f5b7c5](https://github.com/googleapis/google-cloud-python/commit/9f5b7c5a03b34fa1219c7218fa239ea6d829a949))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.1.1...google-cloud-workstations-v0.2.0) (2023-04-06)


### Features

* add client libraries for Workstations v1 ([#11051](https://github.com/googleapis/google-cloud-python/issues/11051)) ([0113725](https://github.com/googleapis/google-cloud-python/commit/011372504f796156bc929ce414a9aa96bd73360c))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-workstations-v0.1.0...google-cloud-workstations-v0.1.1) (2023-03-25)


### Documentation

* Fix formatting of request arg in docstring ([#10867](https://github.com/googleapis/google-cloud-python/issues/10867)) ([d34a425](https://github.com/googleapis/google-cloud-python/commit/d34a425f7d0f02bebaf20d24b725b8c25c699697))

## 0.1.0 (2023-03-17)


### Features

* add initial files for google.cloud.workstations.v1beta ([#10858](https://github.com/googleapis/google-cloud-python/issues/10858)) ([c9650f7](https://github.com/googleapis/google-cloud-python/commit/c9650f74cbf6ee04d1ccbd17947b66a0fecd4237))

## Changelog
