# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-artifact-registry/#history

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.22.0...google-cloud-artifact-registry-v1.23.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.21.0...google-cloud-artifact-registry-v1.22.0) (2026-06-02)


### Features

* regenerate google-cloud-a packages (#17089) ([39c988267529419b03f808d7662ec521258571b4](https://github.com/googleapis/google-cloud-python/commit/39c988267529419b03f808d7662ec521258571b4))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.20.0...google-cloud-artifact-registry-v1.21.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.19.0...google-cloud-artifact-registry-v1.20.0) (2026-02-12)


### Features

* add DIRSUM_SHA256 hash type ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.18.0...google-cloud-artifact-registry-v1.19.0) (2026-01-08)


### Documentation

* update the description of ExportArtifact ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))


### Features

* add Fingerprint to Artifact Registry Version resource ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.17.0...google-cloud-artifact-registry-v1.18.0) (2025-12-04)


### Documentation

* A comment for enum value `ENABLEMENT_CONFIG_UNSPECIFIED` in enum `EnablementConfig` is changed ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* A comment for field `name` in message `.google.devtools.artifactregistry.v1.DockerImage` is changed ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* A comment for field `satisfies_pzs` in message `.google.devtools.artifactregistry.v1.Repository` is changed ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* A comment for field `satisfies_pzi` in message `.google.devtools.artifactregistry.v1.Repository` is changed ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))


### Features

* add ExportArtifact API ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* add artifact_type field in DockerImage ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add image_manifest field in DockerImage ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add Ruby format in VulnerabilityScanningConfig ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.16.1...google-cloud-artifact-registry-v1.17.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.16.0...google-cloud-artifact-registry-v1.16.1) (2025-06-11)


### Documentation

* Update import statement example in README ([eea9e6f](https://github.com/googleapis/google-cloud-python/commit/eea9e6f798406fec17a17dfd71e40fbeea42cf6a))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.15.2...google-cloud-artifact-registry-v1.16.0) (2025-04-12)


### Features

* add the GoModule and KfpArtifact resources ([33b1d93](https://github.com/googleapis/google-cloud-python/commit/33b1d93d262266a274cf0ad3b822fd61d260406d))


### Documentation

* remove the restriction of the maximum numbers of versions that can be deleted in one BatchDeleteVersions call ([33b1d93](https://github.com/googleapis/google-cloud-python/commit/33b1d93d262266a274cf0ad3b822fd61d260406d))

## [1.15.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.15.1...google-cloud-artifact-registry-v1.15.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([3a85796](https://github.com/googleapis/google-cloud-python/commit/3a85796774ebf728cbc9e82dc536316530ac78c1))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.15.0...google-cloud-artifact-registry-v1.15.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([4571dff](https://github.com/googleapis/google-cloud-python/commit/4571dff9614843c6944c8568bd234c6ac5197218))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.14.0...google-cloud-artifact-registry-v1.15.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))
* Add support for reading selective GAPIC generation methods from service YAML ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.13.1...google-cloud-artifact-registry-v1.14.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.13.0...google-cloud-artifact-registry-v1.13.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.12.0...google-cloud-artifact-registry-v1.13.0) (2024-10-28)


### Features

* Add Artifact Registry attachment API ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))
* Add Artifact Registry custom remote support ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))
* Add Artifact Registry generic repository support ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))
* Add Artifact Registry rule APIs ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))
* Add Artifact Registry server side resource filtering and sorting ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))
* Add Artifact Registry UpdateFile and DeleteFile APIs ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))


### Documentation

* Include max page size for all Artifact Registry APIs ([c2d1df7](https://github.com/googleapis/google-cloud-python/commit/c2d1df74b7284f96ab60be091ae8d8139dd777c6))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.11.5...google-cloud-artifact-registry-v1.12.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [1.11.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.11.4...google-cloud-artifact-registry-v1.11.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([6e83a37](https://github.com/googleapis/google-cloud-python/commit/6e83a37612d9eb951cb0ef1e372ef4241f8afa59))

## [1.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.11.3...google-cloud-artifact-registry-v1.11.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12863](https://github.com/googleapis/google-cloud-python/issues/12863)) ([3e6e423](https://github.com/googleapis/google-cloud-python/commit/3e6e423b86cdace8538f610941aa84c7a6217934))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.11.2...google-cloud-artifact-registry-v1.11.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12381](https://github.com/googleapis/google-cloud-python/issues/12381)) ([48ae8ab](https://github.com/googleapis/google-cloud-python/commit/48ae8aba7ec71a382e001b3a659022f942c3b436))

## [1.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.11.1...google-cloud-artifact-registry-v1.11.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.11.0...google-cloud-artifact-registry-v1.11.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.10.0...google-cloud-artifact-registry-v1.11.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.9.0...google-cloud-artifact-registry-v1.10.0) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.8.4...google-cloud-artifact-registry-v1.9.0) (2023-11-02)


### Features

* add support for cleanup policies ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* add support for Docker immutable tags ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* add support for Go and KFP repositories ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* add support for Physical Zone Separation ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* add support for virtual and remote repositories ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* expose the size of the Repository resource ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))


### Documentation

* mark the create_time and update_time in the Repository resource as output only fields ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* mark the repository_id and repository fields in the CreateRepository request as required fields ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))
* use code font for resource name references ([b9fa436](https://github.com/googleapis/google-cloud-python/commit/b9fa436ee5250bad0d0f1aafd2941e7b576fae14))

## [1.8.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.8.3...google-cloud-artifact-registry-v1.8.4) (2023-09-30)


### Bug Fixes

* make repository and repository_id in CreateRepository required ([3b8ea3e](https://github.com/googleapis/google-cloud-python/commit/3b8ea3e4d8f58af3cf83aeb76561857289462086))

## [1.8.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.8.2...google-cloud-artifact-registry-v1.8.3) (2023-08-03)


### Documentation

* Minor formatting ([#11543](https://github.com/googleapis/google-cloud-python/issues/11543)) ([8cc031e](https://github.com/googleapis/google-cloud-python/commit/8cc031e723350890b4ceb6e813f24c4bcde3d65f))

## [1.8.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-artifact-registry-v1.8.1...google-cloud-artifact-registry-v1.8.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11444](https://github.com/googleapis/google-cloud-python/issues/11444)) ([9aa301a](https://github.com/googleapis/google-cloud-python/commit/9aa301ae6ca3080cae286a19de9cdc1b796ab37d))

## [1.8.1](https://github.com/googleapis/python-artifact-registry/compare/v1.8.0...v1.8.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#231](https://github.com/googleapis/python-artifact-registry/issues/231)) ([5433de8](https://github.com/googleapis/python-artifact-registry/commit/5433de8e9b3109dfa162d2ef1a454ab2061c35e6))

## [1.8.0](https://github.com/googleapis/python-artifact-registry/compare/v1.7.0...v1.8.0) (2023-02-27)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#224](https://github.com/googleapis/python-artifact-registry/issues/224)) ([c06b139](https://github.com/googleapis/python-artifact-registry/commit/c06b13969006b365fe7e4450ca86146ee79701c0))

## [1.7.0](https://github.com/googleapis/python-artifact-registry/compare/v1.6.1...v1.7.0) (2023-02-04)


### Features

* Add `BatchDeleteVersionMetadata` to return version that failed to delete ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))
* Add `order_by` to `ListDockerImages` ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))
* Add an API to get and update VPCSC config ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))
* Add format-specific resources `MavenArtifact`, `NpmPackage`, `KfpArtifact` and `PythonPackage` ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))


### Bug Fixes

* Deprecate `REDIRECTION_FROM_GCR_IO_FINALIZED` ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))
* Make `GetFileRequest.name` and `ListFilesRequest.parent` required ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))
* Make `Package` a resource ([bed057d](https://github.com/googleapis/python-artifact-registry/commit/bed057d56e91a912dacdc0d1428e801c91fff307))

## [1.6.1](https://github.com/googleapis/python-artifact-registry/compare/v1.6.0...v1.6.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([62d61be](https://github.com/googleapis/python-artifact-registry/commit/62d61be47caa52f7d96ccc054010aef6ff43d5bc))


### Documentation

* Add documentation for enums ([62d61be](https://github.com/googleapis/python-artifact-registry/commit/62d61be47caa52f7d96ccc054010aef6ff43d5bc))

## [1.6.0](https://github.com/googleapis/python-artifact-registry/compare/v1.5.0...v1.6.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#214](https://github.com/googleapis/python-artifact-registry/issues/214)) ([1b68d31](https://github.com/googleapis/python-artifact-registry/commit/1b68d3161973acef42fb458efa52d6cb81597ae1))

## [1.5.0](https://github.com/googleapis/python-artifact-registry/compare/v1.4.1...v1.5.0) (2023-01-03)


### Features

* Add location methods ([#211](https://github.com/googleapis/python-artifact-registry/issues/211)) ([2458b5e](https://github.com/googleapis/python-artifact-registry/commit/2458b5e00b1cb7a91254228a37e349816f13f96c))

## [1.4.1](https://github.com/googleapis/python-artifact-registry/compare/v1.4.0...v1.4.1) (2022-12-08)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([c6e2c56](https://github.com/googleapis/python-artifact-registry/commit/c6e2c5683d135ce34b3aa86ff0262967d4a8000a))
* Drop usage of pkg_resources ([c6e2c56](https://github.com/googleapis/python-artifact-registry/commit/c6e2c5683d135ce34b3aa86ff0262967d4a8000a))
* Fix timeout default values ([c6e2c56](https://github.com/googleapis/python-artifact-registry/commit/c6e2c5683d135ce34b3aa86ff0262967d4a8000a))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([c6e2c56](https://github.com/googleapis/python-artifact-registry/commit/c6e2c5683d135ce34b3aa86ff0262967d4a8000a))

## [1.4.0](https://github.com/googleapis/python-artifact-registry/compare/v1.3.3...v1.4.0) (2022-11-16)


### Features

* add support for `google.cloud.artifactregistry.__version__` ([93a383f](https://github.com/googleapis/python-artifact-registry/commit/93a383ff7c66ed9f6f2a65e698cb5e22126c6cf2))
* Add typing to proto.Message based class attributes ([9d151b1](https://github.com/googleapis/python-artifact-registry/commit/9d151b12c06d25beb5078ee293b79369eff46ca4))


### Bug Fixes

* Add dict typing for client_options ([93a383f](https://github.com/googleapis/python-artifact-registry/commit/93a383ff7c66ed9f6f2a65e698cb5e22126c6cf2))
* **deps:** require google-api-core &gt;=1.33.2 ([93a383f](https://github.com/googleapis/python-artifact-registry/commit/93a383ff7c66ed9f6f2a65e698cb5e22126c6cf2))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([9d151b1](https://github.com/googleapis/python-artifact-registry/commit/9d151b12c06d25beb5078ee293b79369eff46ca4))

## [1.3.3](https://github.com/googleapis/python-artifact-registry/compare/v1.3.2...v1.3.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#196](https://github.com/googleapis/python-artifact-registry/issues/196)) ([ebb9234](https://github.com/googleapis/python-artifact-registry/commit/ebb92349e127ffa672ce3a35bc63104e81881f48))

## [1.3.2](https://github.com/googleapis/python-artifact-registry/compare/v1.3.1...v1.3.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#194](https://github.com/googleapis/python-artifact-registry/issues/194)) ([903c755](https://github.com/googleapis/python-artifact-registry/commit/903c755294263b900f720d6249eb129d086cdbd5))

## [1.3.1](https://github.com/googleapis/python-artifact-registry/compare/v1.3.0...v1.3.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#181](https://github.com/googleapis/python-artifact-registry/issues/181)) ([3a857d7](https://github.com/googleapis/python-artifact-registry/commit/3a857d7de80bcad309aff1ea62d687535b744a1c))
* **deps:** require proto-plus >= 1.22.0 ([3a857d7](https://github.com/googleapis/python-artifact-registry/commit/3a857d7de80bcad309aff1ea62d687535b744a1c))

## [1.3.0](https://github.com/googleapis/python-artifact-registry/compare/v1.2.1...v1.3.0) (2022-07-16)


### Features

* add audience parameter ([340303e](https://github.com/googleapis/python-artifact-registry/commit/340303e72af3bca4f2ab75e280f614ff3992b65e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#172](https://github.com/googleapis/python-artifact-registry/issues/172)) ([340303e](https://github.com/googleapis/python-artifact-registry/commit/340303e72af3bca4f2ab75e280f614ff3992b65e))
* require python 3.7+ ([#174](https://github.com/googleapis/python-artifact-registry/issues/174)) ([0c8a55c](https://github.com/googleapis/python-artifact-registry/commit/0c8a55c1b7097553bb3f8476e1a22cdbb81bf83f))

## [1.2.1](https://github.com/googleapis/python-artifact-registry/compare/v1.2.0...v1.2.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#164](https://github.com/googleapis/python-artifact-registry/issues/164)) ([3f57f9a](https://github.com/googleapis/python-artifact-registry/commit/3f57f9a14b3e8a93abefe5f57a8e5066ff7a3b6f))


### Documentation

* fix changelog header to consistent size ([#165](https://github.com/googleapis/python-artifact-registry/issues/165)) ([57f37c9](https://github.com/googleapis/python-artifact-registry/commit/57f37c956ef4adf6800ba45f20266693e9f11b57))

## [1.2.0](https://github.com/googleapis/python-artifact-registry/compare/v1.1.2...v1.2.0) (2022-04-21)


### Features

* AuditConfig for IAM v1 ([c22893b](https://github.com/googleapis/python-artifact-registry/commit/c22893b8e671fea8416ff1e6a4f23aa03e201e74))
* promote v1beta2 features to v1 ([#138](https://github.com/googleapis/python-artifact-registry/issues/138)) ([842c107](https://github.com/googleapis/python-artifact-registry/commit/842c107cb6f6705c3228495ce43653414801af9f))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([c22893b](https://github.com/googleapis/python-artifact-registry/commit/c22893b8e671fea8416ff1e6a4f23aa03e201e74))

## [1.1.2](https://github.com/googleapis/python-artifact-registry/compare/v1.1.1...v1.1.2) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#136](https://github.com/googleapis/python-artifact-registry/issues/136)) ([9bc4ec5](https://github.com/googleapis/python-artifact-registry/commit/9bc4ec5ec05e8efaf9b45725782c9ca29d1c5076))
* **deps:** require proto-plus>=1.15.0 ([9bc4ec5](https://github.com/googleapis/python-artifact-registry/commit/9bc4ec5ec05e8efaf9b45725782c9ca29d1c5076))


### Documentation

* more details for ListFilesRequest parent field ([#133](https://github.com/googleapis/python-artifact-registry/issues/133)) ([f4ef78b](https://github.com/googleapis/python-artifact-registry/commit/f4ef78b6b108543bf07d8c564f4316a8314e8d54))

## [1.1.1](https://github.com/googleapis/python-artifact-registry/compare/v1.1.0...v1.1.1) (2022-02-15)


### Bug Fixes

* **deps:** remove unused dependency libcst ([#125](https://github.com/googleapis/python-artifact-registry/issues/125)) ([9980b1e](https://github.com/googleapis/python-artifact-registry/commit/9980b1ee169d0dab3306a785872a66d96b242eb5))
* resolve DuplicateCredentialArgs error when using credentials_file ([d4329aa](https://github.com/googleapis/python-artifact-registry/commit/d4329aaffe59859df2c2f1ff10894eaa547ce7df))


### Documentation

* add autogenerated code snippets ([ef8af7a](https://github.com/googleapis/python-artifact-registry/commit/ef8af7ac0cbcca7acdbf6066c1823c468e2da71d))
* add autogenerated code snippets ([#123](https://github.com/googleapis/python-artifact-registry/issues/123)) ([ef8af7a](https://github.com/googleapis/python-artifact-registry/commit/ef8af7ac0cbcca7acdbf6066c1823c468e2da71d)), closes [#65](https://github.com/googleapis/python-artifact-registry/issues/65)

## [1.1.0](https://github.com/googleapis/python-artifact-registry/compare/v1.0.2...v1.1.0) (2022-01-25)


### Features

* add api key support ([#119](https://github.com/googleapis/python-artifact-registry/issues/119)) ([d22f2d9](https://github.com/googleapis/python-artifact-registry/commit/d22f2d93ffcc169540991d224a54c81eb7ca09a4))
* add APIs for importing and uploading Apt and Yum artifacts ([#116](https://github.com/googleapis/python-artifact-registry/issues/116)) ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))
* add order_by support for listing versions ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))
* add version policy support for Maven repositories ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))


### Bug Fixes

* mark a few resource name fields as required ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))

## [1.0.2](https://www.github.com/googleapis/python-artifact-registry/compare/v1.0.1...v1.0.2) (2022-01-07)


### Bug Fixes

* fix resource pattern ID segment name ([#107](https://www.github.com/googleapis/python-artifact-registry/issues/107)) ([254dc73](https://www.github.com/googleapis/python-artifact-registry/commit/254dc73dbbc52d41014e0d2db81f3cc6cd864058))

## [1.0.1](https://www.github.com/googleapis/python-artifact-registry/compare/v1.0.0...v1.0.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([90e3313](https://www.github.com/googleapis/python-artifact-registry/commit/90e3313b50b127d6fc562e7138b12743412fa064))
* **deps:** require google-api-core >= 1.28.0 ([90e3313](https://www.github.com/googleapis/python-artifact-registry/commit/90e3313b50b127d6fc562e7138b12743412fa064))


### Documentation

* list oneofs in docstring ([90e3313](https://www.github.com/googleapis/python-artifact-registry/commit/90e3313b50b127d6fc562e7138b12743412fa064))

## [1.0.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.5.0...v1.0.0) (2021-10-22)


### Features

* bump release level to production/stable ([#82](https://www.github.com/googleapis/python-artifact-registry/issues/82)) ([d3705c1](https://www.github.com/googleapis/python-artifact-registry/commit/d3705c13605af3e4167c2e86eeb55683a271a3d4))


### Documentation

* fix docstring formatting ([#93](https://www.github.com/googleapis/python-artifact-registry/issues/93)) ([e6c2084](https://www.github.com/googleapis/python-artifact-registry/commit/e6c208427336e8c9d5a5d607c02406c856af6a94))

## [0.5.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.4.1...v0.5.0) (2021-10-11)


### Features

* add context manager support in client ([#88](https://www.github.com/googleapis/python-artifact-registry/issues/88)) ([0f631cc](https://www.github.com/googleapis/python-artifact-registry/commit/0f631cc8bd8ff0928d5403e756d2206f1842c35c))
* add trove classifier for python 3.10 ([#91](https://www.github.com/googleapis/python-artifact-registry/issues/91)) ([e392f56](https://www.github.com/googleapis/python-artifact-registry/commit/e392f565e5e9252bff8a5f6ede67c11b25438cdd))

## [0.4.1](https://www.github.com/googleapis/python-artifact-registry/compare/v0.4.0...v0.4.1) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([8a6b687](https://www.github.com/googleapis/python-artifact-registry/commit/8a6b6870f39c34bd1cf2dafd591c58ebd2c48d77))

## [0.4.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.3...v0.4.0) (2021-09-24)


### Features

* add Artifact Registry v1  ([#80](https://www.github.com/googleapis/python-artifact-registry/issues/80)) ([43413eb](https://www.github.com/googleapis/python-artifact-registry/commit/43413ebd0d6823233573ab88c0340e4165ee4487))
* set artifactregistry_v1 as the default import ([43413eb](https://www.github.com/googleapis/python-artifact-registry/commit/43413ebd0d6823233573ab88c0340e4165ee4487))


### Bug Fixes

* add 'dict' annotation type to 'request' ([43413eb](https://www.github.com/googleapis/python-artifact-registry/commit/43413ebd0d6823233573ab88c0340e4165ee4487))

## [0.3.3](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.2...v0.3.3) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#59](https://www.github.com/googleapis/python-artifact-registry/issues/59)) ([bb98a8c](https://www.github.com/googleapis/python-artifact-registry/commit/bb98a8cfcbfadf95ef72499d8bf1fb4ae2e1b599))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#55](https://www.github.com/googleapis/python-artifact-registry/issues/55)) ([55773fe](https://www.github.com/googleapis/python-artifact-registry/commit/55773fe0ab33a8aa5c8b6669eb75e9615f226db0))


### Miscellaneous Chores

* release as 0.3.3 ([#60](https://www.github.com/googleapis/python-artifact-registry/issues/60)) ([b8d7865](https://www.github.com/googleapis/python-artifact-registry/commit/b8d78650cceae268f6616c4eefef3200c7477cc1))

## [0.3.2](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.1...v0.3.2) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#54](https://www.github.com/googleapis/python-artifact-registry/issues/54)) ([b171295](https://www.github.com/googleapis/python-artifact-registry/commit/b171295c19c0e29025aad08975ceb9a8c9aac66c))

## [0.3.1](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.0...v0.3.1) (2021-06-30)


### Bug Fixes

* disable always_use_jwt_access ([ce910f4](https://www.github.com/googleapis/python-artifact-registry/commit/ce910f40a365c56a07372664adffe98a628fabe9))
* disable always_use_jwt_access ([#50](https://www.github.com/googleapis/python-artifact-registry/issues/50)) ([ce910f4](https://www.github.com/googleapis/python-artifact-registry/commit/ce910f40a365c56a07372664adffe98a628fabe9))

## [0.3.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.2.2...v0.3.0) (2021-06-23)


### Features

* add always_use_jwt_access ([#46](https://www.github.com/googleapis/python-artifact-registry/issues/46)) ([247d779](https://www.github.com/googleapis/python-artifact-registry/commit/247d779c881e7fdfc7696adcb3256ca06b3980c3))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-artifact-registry/issues/1127)) ([#41](https://www.github.com/googleapis/python-artifact-registry/issues/41)) ([7ae05ed](https://www.github.com/googleapis/python-artifact-registry/commit/7ae05eddef4fce0f3f09774e835381f901a6a031)), closes [#1126](https://www.github.com/googleapis/python-artifact-registry/issues/1126)

## [0.2.2](https://www.github.com/googleapis/python-artifact-registry/compare/v0.2.1...v0.2.2) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#38](https://www.github.com/googleapis/python-artifact-registry/issues/38)) ([345496f](https://www.github.com/googleapis/python-artifact-registry/commit/345496fbd96d4c780acdb2ee940e530e7d48ab6c))

## [0.2.1](https://www.github.com/googleapis/python-artifact-registry/compare/v0.2.0...v0.2.1) (2021-06-01)


### Bug Fixes

* **deps:** add packaging requirement ([#33](https://www.github.com/googleapis/python-artifact-registry/issues/33)) ([ca2907e](https://www.github.com/googleapis/python-artifact-registry/commit/ca2907efdcd05a88a63c798a367baa71f2fb78b4))

## [0.2.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.1.0...v0.2.0) (2021-05-25)


### Features

* support self-signed JWT flow for service accounts ([#25](https://www.github.com/googleapis/python-artifact-registry/issues/25)) ([fade594](https://www.github.com/googleapis/python-artifact-registry/commit/fade594980fa8f389abc0e3f84e34cb1bcda1f1e))

## 0.1.0 (2021-03-15)


### Features

* generate v1beta2 ([87afc6d](https://www.github.com/googleapis/python-artifact-registry/commit/87afc6ddd4966e4c9acb0a88c556cbcd2fb6b566))
