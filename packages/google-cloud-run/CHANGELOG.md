# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-run/#history

## [0.16.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.16.1...google-cloud-run-v0.16.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.16.0...google-cloud-run-v0.16.1) (2026-06-22)


### Features

* regenerate google-cloud-[o-r] packages ([#17075](https://github.com/googleapis/google-cloud-python/issues/17075)) ([f4bd018](https://github.com/googleapis/google-cloud-python/commit/f4bd0182d808ae73c3c6981e6ce3d565f78a6051))

## [0.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.15.0...google-cloud-run-v0.16.0) (2026-03-26)


### Documentation

* An existing repeated string field custom_audiences is marked deprecated for WorkerPools API ([397ae5384b5fa2741d0f479ba7efc1612e1195da](https://github.com/googleapis/google-cloud-python/commit/397ae5384b5fa2741d0f479ba7efc1612e1195da))


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.14.0...google-cloud-run-v0.15.0) (2026-01-22)


### Documentation

* add instances description ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))


### Features

* add instances client library ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))

## [0.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.13.0...google-cloud-run-v0.14.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.12.0...google-cloud-run-v0.13.0) (2025-12-11)


### Documentation

* A comment for field `custom_audiences` in message `.google.cloud.run.v2.WorkerPool` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `limits` in message `.google.cloud.run.v2.ResourceRequirements` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `etag` in message `.google.cloud.run.v2.Service` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `etag` in message `.google.cloud.run.v2.Job` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `items` in message `.google.cloud.run.v2.SecretVolumeSource` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `invoker_iam_disabled` in message `.google.cloud.run.v2.Service` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `etag` in message `.google.cloud.run.v2.WorkerPool` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `observed_generation` in message `.google.cloud.run.v2.WorkerPool` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `name` in message `.google.cloud.run.v2.Service` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `latest_ready_revision` in message `.google.cloud.run.v2.WorkerPool` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))
* A comment for field `reconciling` in message `.google.cloud.run.v2.WorkerPool` is changed ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))


### Features

* add SourceCode proto to Run container config ([4927067384eb6ed2018bb886f90265b7bcfc800e](https://github.com/googleapis/google-cloud-python/commit/4927067384eb6ed2018bb886f90265b7bcfc800e))

## [0.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.11.0...google-cloud-run-v0.12.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.19...google-cloud-run-v0.11.0) (2025-08-29)


### ⚠ BREAKING CHANGES

* A type of an existing resource_reference option of the field `worker_pool` in message `.google.cloud.run.v2.SubmitBuildRequest` is changed from `cloudbuild.googleapis.com/WorkerPool` to `cloudbuild.googleapis.com/BuildWorkerPool`
* A type of an existing resource_reference option of the field `worker_pool` in message `.google.cloud.run.v2.BuildConfig` is changed from `cloudbuild.googleapis.com/WorkerPool` to `cloudbuild.googleapis.com/BuildWorkerPool`
* [google-cloud-run] An existing resource_definition `cloudbuild.googleapis.com/WorkerPool` is removed

### Features

* Adding new resource tpye run.googleapis.com/WorkerPool. ([077a8ff](https://github.com/googleapis/google-cloud-python/commit/077a8ffd3e2890dc1277bf516f4126bfdf666a96))


### Bug Fixes

* [google-cloud-run] An existing resource_definition `cloudbuild.googleapis.com/WorkerPool` is removed ([077a8ff](https://github.com/googleapis/google-cloud-python/commit/077a8ffd3e2890dc1277bf516f4126bfdf666a96))
* A type of an existing resource_reference option of the field `worker_pool` in message `.google.cloud.run.v2.BuildConfig` is changed from `cloudbuild.googleapis.com/WorkerPool` to `cloudbuild.googleapis.com/BuildWorkerPool` ([077a8ff](https://github.com/googleapis/google-cloud-python/commit/077a8ffd3e2890dc1277bf516f4126bfdf666a96))
* A type of an existing resource_reference option of the field `worker_pool` in message `.google.cloud.run.v2.SubmitBuildRequest` is changed from `cloudbuild.googleapis.com/WorkerPool` to `cloudbuild.googleapis.com/BuildWorkerPool` ([077a8ff](https://github.com/googleapis/google-cloud-python/commit/077a8ffd3e2890dc1277bf516f4126bfdf666a96))

## [0.10.19](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.18...google-cloud-run-v0.10.19) (2025-07-16)


### Features

* add new field `term_signal` to `.google.cloud.run.v2.TaskAttemptResult` ([078e0e2](https://github.com/googleapis/google-cloud-python/commit/078e0e2ccb5f59a9c78c89d63b7e57c9d7dca9c2))
* support GPU zonal redundancy setting for Cloud Run jobs ([078e0e2](https://github.com/googleapis/google-cloud-python/commit/078e0e2ccb5f59a9c78c89d63b7e57c9d7dca9c2))

## [0.10.18](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.17...google-cloud-run-v0.10.18) (2025-05-15)


### Features

* support GPU zonal redundancy setting in Cloud Run services ([2f33995](https://github.com/googleapis/google-cloud-python/commit/2f33995c8f454fe9a6798aa2477bd1b0a817d1da))
* support node selector in Cloud Run jobs for GPU setting ([2f33995](https://github.com/googleapis/google-cloud-python/commit/2f33995c8f454fe9a6798aa2477bd1b0a817d1da))

## [0.10.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.16...google-cloud-run-v0.10.17) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.10.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.15...google-cloud-run-v0.10.16) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([770cf0f](https://github.com/googleapis/google-cloud-python/commit/770cf0f31125586a8622e9639f6d24c1bafa9b31))

## [0.10.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.14...google-cloud-run-v0.10.15) (2025-02-12)


### Features

* add Base Image URI to Container ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))
* add BuildConfig to Services for configuring Run functions ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))
* add BuildInfo to Revision for displaying BuildConfig used for a specific revision deployment ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))
* add creator field to Execution ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))
* add project_descriptor to BuildspackBuild ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))
* Add REST Interceptors which support reading metadata ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))
* Add support for reading selective GAPIC generation methods from service YAML ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))


### Documentation

* some typos were fixed and formatting changed ([8a3376a](https://github.com/googleapis/google-cloud-python/commit/8a3376a779ec82b552c30d76e6ba65f9ba15d6ca))

## [0.10.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.13...google-cloud-run-v0.10.14) (2024-12-12)


### Features

* Add support for opt-in debug logging ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))

## [0.10.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.12...google-cloud-run-v0.10.13) (2024-11-21)


### Features

* support manual instance count in Cloud Run for manual scaling feature ([16b5ba7](https://github.com/googleapis/google-cloud-python/commit/16b5ba78a7316bd792be6f4a1608e7280b2ea0ce))

## [0.10.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.11...google-cloud-run-v0.10.12) (2024-11-14)


### Features

* add EncryptionKeyRevocationAction and shutdown duration configuration to Services ([579e338](https://github.com/googleapis/google-cloud-python/commit/579e3383972c29e991b319a674822e676376691f))


### Documentation

* fixed formatting of some documentation ([579e338](https://github.com/googleapis/google-cloud-python/commit/579e3383972c29e991b319a674822e676376691f))

## [0.10.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.10...google-cloud-run-v0.10.11) (2024-11-11)


### Features

* support advanced configurations options for cloud storage volumes by setting mount_options in the GCSVolumeSource configuration ([97b9b6b](https://github.com/googleapis/google-cloud-python/commit/97b9b6b9f1092fc46545aa8f46d2cd3f6af46012))


### Bug Fixes

* disable universe-domain validation  ([#13245](https://github.com/googleapis/google-cloud-python/issues/13245)) ([875f712](https://github.com/googleapis/google-cloud-python/commit/875f712265a36919409964f5ade218330f1d0147))


### Documentation

* A comment for field `max_instance_request_concurrency` in message `.google.cloud.run.v2.RevisionTemplate` is changed ([97b9b6b](https://github.com/googleapis/google-cloud-python/commit/97b9b6b9f1092fc46545aa8f46d2cd3f6af46012))
* For field `invoker_iam_disabled` in message `.google.cloud.run.v2.Service`, clarify that feature is available by invitation only ([97b9b6b](https://github.com/googleapis/google-cloud-python/commit/97b9b6b9f1092fc46545aa8f46d2cd3f6af46012))
* Update docs for field `value` in message `.google.cloud.run.v2.EnvVar` to reflect Cloud Run product capabilities ([97b9b6b](https://github.com/googleapis/google-cloud-python/commit/97b9b6b9f1092fc46545aa8f46d2cd3f6af46012))

## [0.10.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.9...google-cloud-run-v0.10.10) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [0.10.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.8...google-cloud-run-v0.10.9) (2024-10-08)


### Features

* add Builds API ([6dde382](https://github.com/googleapis/google-cloud-python/commit/6dde3826c7c13ff1fcc840495811f58648e0678e))
* add GPU configuration to Services ([6dde382](https://github.com/googleapis/google-cloud-python/commit/6dde3826c7c13ff1fcc840495811f58648e0678e))
* add INGRESS_TRAFFIC_NONE to Services ([6dde382](https://github.com/googleapis/google-cloud-python/commit/6dde3826c7c13ff1fcc840495811f58648e0678e))
* add Service Mesh configuration to Services ([6dde382](https://github.com/googleapis/google-cloud-python/commit/6dde3826c7c13ff1fcc840495811f58648e0678e))
* add ServiceScaling to Services ([6dde382](https://github.com/googleapis/google-cloud-python/commit/6dde3826c7c13ff1fcc840495811f58648e0678e))


### Documentation

* fixed formatting of some documentation ([6dde382](https://github.com/googleapis/google-cloud-python/commit/6dde3826c7c13ff1fcc840495811f58648e0678e))

## [0.10.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.7...google-cloud-run-v0.10.8) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([52db52e](https://github.com/googleapis/google-cloud-python/commit/52db52ea05c6883b07956d323fdd1d3029806374))

## [0.10.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.6...google-cloud-run-v0.10.7) (2024-07-10)


### Features

* add Job ExecutionReference.completion_status to show status of the most recent execution ([0829cc1](https://github.com/googleapis/google-cloud-python/commit/0829cc12b7521b9ecb4ef302d86e0863f9159d7e))
* add Job start_execution_token and run_execution_token to execute jobs immediately on creation ([0829cc1](https://github.com/googleapis/google-cloud-python/commit/0829cc12b7521b9ecb4ef302d86e0863f9159d7e))
* support update_mask in Cloud Run UpdateService  ([0829cc1](https://github.com/googleapis/google-cloud-python/commit/0829cc12b7521b9ecb4ef302d86e0863f9159d7e))


### Documentation

* clarify optional fields in Cloud Run requests ([0829cc1](https://github.com/googleapis/google-cloud-python/commit/0829cc12b7521b9ecb4ef302d86e0863f9159d7e))

## [0.10.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.5...google-cloud-run-v0.10.6) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [0.10.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.4...google-cloud-run-v0.10.5) (2024-03-05)


### Features

* Allow disabling the default URL (run.app) for Cloud Run Services ([5535d1e](https://github.com/googleapis/google-cloud-python/commit/5535d1e6288f790899f7f6b5091ad113621da176))
* Support disabling waiting for health checks during Service deployment. ([5535d1e](https://github.com/googleapis/google-cloud-python/commit/5535d1e6288f790899f7f6b5091ad113621da176))
* Support mounting NFS and GCS volumes in Cloud Run Jobs and Services ([5535d1e](https://github.com/googleapis/google-cloud-python/commit/5535d1e6288f790899f7f6b5091ad113621da176))
* Support specifying a per-Service min-instance-count ([5535d1e](https://github.com/googleapis/google-cloud-python/commit/5535d1e6288f790899f7f6b5091ad113621da176))


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))


### Documentation

* Clarify some defaults and required or optional values ([5535d1e](https://github.com/googleapis/google-cloud-python/commit/5535d1e6288f790899f7f6b5091ad113621da176))

## [0.10.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.3...google-cloud-run-v0.10.4) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))
* fix ValueError in test__validate_universe_domain ([89c1b05](https://github.com/googleapis/google-cloud-python/commit/89c1b054f321b90ab4eed0139a3a2a79c369730d))

## [0.10.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.2...google-cloud-run-v0.10.3) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [0.10.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.1...google-cloud-run-v0.10.2) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([4368029](https://github.com/googleapis/google-cloud-python/commit/436802904bfdafa7e90f94b128813506525e1605))

## [0.10.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-run-v0.10.0...google-cloud-run-v0.10.1) (2023-12-07)


### Features

* Add support for python 3.12 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Introduce compatibility with native namespace packages ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Use `retry_async` instead of `retry` in async client ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))

## [0.10.0](https://github.com/googleapis/python-run/compare/v0.9.1...v0.10.0) (2023-10-09)


### Features

* Adds support for cancel Execution ([f2c76e1](https://github.com/googleapis/python-run/commit/f2c76e16a6abf333e36cba50b3270211eb762fcf))
* Adds support for Direct VPC egress setting ([f2c76e1](https://github.com/googleapis/python-run/commit/f2c76e16a6abf333e36cba50b3270211eb762fcf))
* Adds support for Execution overrides ([f2c76e1](https://github.com/googleapis/python-run/commit/f2c76e16a6abf333e36cba50b3270211eb762fcf))
* New field for Task's scheduled timestamp ([f2c76e1](https://github.com/googleapis/python-run/commit/f2c76e16a6abf333e36cba50b3270211eb762fcf))
* New fields for multi-container ([f2c76e1](https://github.com/googleapis/python-run/commit/f2c76e16a6abf333e36cba50b3270211eb762fcf))


### Documentation

* General documentation fixes. ([f2c76e1](https://github.com/googleapis/python-run/commit/f2c76e16a6abf333e36cba50b3270211eb762fcf))
* Minor formatting ([0b5dc70](https://github.com/googleapis/python-run/commit/0b5dc70d2f8f730e2405f2891c8007bdbbc344ad))

## [0.9.1](https://github.com/googleapis/python-run/compare/v0.9.0...v0.9.1) (2023-08-02)


### Documentation

* Minor formatting ([#120](https://github.com/googleapis/python-run/issues/120)) ([4c14a21](https://github.com/googleapis/python-run/commit/4c14a219395f7195749e142713ca62f81b7a1642))

## [0.9.0](https://github.com/googleapis/python-run/compare/v0.8.1...v0.9.0) (2023-07-06)


### Features

* Adds support for custom audiences ([#107](https://github.com/googleapis/python-run/issues/107)) ([bfd0829](https://github.com/googleapis/python-run/commit/bfd08297d6301c57e242819dba35006218d217e5))

## [0.8.1](https://github.com/googleapis/python-run/compare/v0.8.0...v0.8.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#105](https://github.com/googleapis/python-run/issues/105)) ([592b761](https://github.com/googleapis/python-run/commit/592b761bd1f04c7a6d0fb7d8e3b70ba54db01779))

## [0.8.0](https://github.com/googleapis/python-run/compare/v0.7.1...v0.8.0) (2023-05-25)


### Features

* Adds support for Session affinity in Service (GA) ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))
* Adds support for Startup CPU Boost (GA) ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))
* New 'port' field for HttpGetAction probe type ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))
* New fields/enum values ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))


### Documentation

* General documentation fixes. ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))

## [0.7.1](https://github.com/googleapis/python-run/compare/v0.7.0...v0.7.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#93](https://github.com/googleapis/python-run/issues/93)) ([4db3679](https://github.com/googleapis/python-run/commit/4db3679a05db11882644fb1b6d5f8a0461758351))

## [0.7.0](https://github.com/googleapis/python-run/compare/v0.6.0...v0.7.0) (2023-01-20)


### Features

* Adding support for encryption_key_revocation_action and encryption_key_shutdown_duration for RevisionTemplate and ExecutionTemplate  ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))


### Bug Fixes

* Add context manager return types ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))


### Documentation

* Add documentation for enums ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))
* Documentation improvements, including clarification that v1 labels/annotations are rejected in v2 API ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))

## [0.6.0](https://github.com/googleapis/python-run/compare/v0.5.0...v0.6.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#78](https://github.com/googleapis/python-run/issues/78)) ([951b679](https://github.com/googleapis/python-run/commit/951b6794b0357b788097b53fdb2e2e2264536cff))

## [0.5.0](https://github.com/googleapis/python-run/compare/v0.4.2...v0.5.0) (2022-12-14)


### Features

* Add support for `google.cloud.run.__version__` ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* Add typing to proto.Message based class attributes ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* Adds Cloud Run Jobs v2 API client libraries ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* Adds Startup and Liveness probes to Cloud Run v2 API client libraries ([#60](https://github.com/googleapis/python-run/issues/60)) ([d4d22ec](https://github.com/googleapis/python-run/commit/d4d22ecf187d7b370f10d627ece28255cbe9c804))


### Bug Fixes

* Add dict typing for client_options ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))
* Drop usage of pkg_resources ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))
* Fix timeout default values ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))

## [0.4.2](https://github.com/googleapis/python-run/compare/v0.4.1...v0.4.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#58](https://github.com/googleapis/python-run/issues/58)) ([87dcb78](https://github.com/googleapis/python-run/commit/87dcb781affd73e25e3850e01a240e0e985f0570))
* **deps:** require google-api-core&gt;=1.33.2 ([87dcb78](https://github.com/googleapis/python-run/commit/87dcb781affd73e25e3850e01a240e0e985f0570))

## [0.4.1](https://github.com/googleapis/python-run/compare/v0.4.0...v0.4.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#55](https://github.com/googleapis/python-run/issues/55)) ([7a85bac](https://github.com/googleapis/python-run/commit/7a85bac07e66efd965453fd0ecb093976edca2f2))

## [0.4.0](https://github.com/googleapis/python-run/compare/v0.3.0...v0.4.0) (2022-09-13)


### Features

* Enable REST transport support ([#45](https://github.com/googleapis/python-run/issues/45)) ([0ccecb0](https://github.com/googleapis/python-run/commit/0ccecb079d3702026d14ef577fda27030f19f3aa))

## [0.3.0](https://github.com/googleapis/python-run/compare/v0.2.1...v0.3.0) (2022-08-15)


### Features

* add audience parameter ([0d02163](https://github.com/googleapis/python-run/commit/0d02163a93eade5b9218d5330ece1723e375a3ff))


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#33](https://github.com/googleapis/python-run/issues/33)) ([55bf980](https://github.com/googleapis/python-run/commit/55bf98023e2a6855a394e487db11b6aa7dc57c17))
* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([0d02163](https://github.com/googleapis/python-run/commit/0d02163a93eade5b9218d5330ece1723e375a3ff))
* **deps:** require proto-plus >= 1.22.0 ([55bf980](https://github.com/googleapis/python-run/commit/55bf98023e2a6855a394e487db11b6aa7dc57c17))
* Updates pre-release Cloud Run v2 Preview client libraries to work with the latest API revision ([0d02163](https://github.com/googleapis/python-run/commit/0d02163a93eade5b9218d5330ece1723e375a3ff))

## [0.2.1](https://github.com/googleapis/python-run/compare/v0.2.0...v0.2.1) (2022-07-26)


### Bug Fixes

* require python 3.7+ ([#26](https://github.com/googleapis/python-run/issues/26)) ([854f73d](https://github.com/googleapis/python-run/commit/854f73db0893e080dc6098d134809692e8685f39))

## [0.2.0](https://github.com/googleapis/python-run/compare/v0.1.0...v0.2.0) (2022-04-14)


### Features

* AuditConfig for IAM v1 ([43244bc](https://github.com/googleapis/python-run/commit/43244bc4aba7e70e21348dc3c3b78c430b2bedb9))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([43244bc](https://github.com/googleapis/python-run/commit/43244bc4aba7e70e21348dc3c3b78c430b2bedb9))


### Documentation

* fix type in docstring for map fields ([43244bc](https://github.com/googleapis/python-run/commit/43244bc4aba7e70e21348dc3c3b78c430b2bedb9))

## 0.1.0 (2022-04-03)


### Features

* generate v2 ([6fd2a11](https://github.com/googleapis/python-run/commit/6fd2a11558d444d454184ab5fe594618b441c2db))
