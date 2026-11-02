# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-asset/#history

## [4.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v4.4.0...google-cloud-asset-v4.5.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [4.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v4.3.0...google-cloud-asset-v4.4.0) (2026-06-02)


### Features

* regenerate asset w/ dependencies using generator v1.32.0 (#17153) ([ac594a0d31bcdef08c341a57badce462efcd7684](https://github.com/googleapis/google-cloud-python/commit/ac594a0d31bcdef08c341a57badce462efcd7684))

## [4.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v4.2.0...google-cloud-asset-v4.3.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [4.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v4.1.0...google-cloud-asset-v4.2.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [4.1.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v4.0.0...google-cloud-asset-v4.1.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [4.0.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.30.1...google-cloud-asset-v4.0.0) (2025-10-07)


### Bug Fixes

* remove google.cloud.asset_v1p4beta1 (#14571) Remove `google.cloud.asset_v1p4beta1` which doesn't exist in
https://github.com/googleapis/googleapis/tree/master/google/cloud/asset ([521e7d7dd1d9978f0db19f0125a05e50050d077b](https://github.com/googleapis/google-cloud-python/commit/521e7d7dd1d9978f0db19f0125a05e50050d077b))

## [3.30.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.30.0...google-cloud-asset-v3.30.1) (2025-05-08)


### Documentation

* fix typos in documentation ([deb14f3](https://github.com/googleapis/google-cloud-python/commit/deb14f34f821ab238692e0597fd0f7b79833fc26))

## [3.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.29.2...google-cloud-asset-v3.30.0) (2025-04-24)


### Features

* A new field `enrichments` is added to message `.google.cloud.asset.v1.ResourceSearchResult` ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A new message `AssetEnrichment` is added ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A new message `ResourceOwners` is added ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A new value `GOVERN_TAGS` is added to enum `MethodType` ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A new value `REMOVE_GRANT` is added to enum `MethodType` ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))


### Documentation

* A comment for field `attached_resource` in message `.google.cloud.asset.v1.EffectiveTagDetails` is changed ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A comment for field `consolidated_policy` in message `.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse` is changed ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A comment for field `policy_bundle` in message `.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse` is changed ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A comment for field `policy_bundle` in message `.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse` is changed ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A comment for field `policy_bundle` in message `.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse` is changed ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))
* A comment for field `service_account_impersonation_analysis` in message `.google.cloud.asset.v1.AnalyzeIamPolicyResponse` is changed ([b464b68](https://github.com/googleapis/google-cloud-python/commit/b464b68f31f1c54ec98881262a903de85f21cb8c))

## [3.29.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.29.1...google-cloud-asset-v3.29.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([3a85796](https://github.com/googleapis/google-cloud-python/commit/3a85796774ebf728cbc9e82dc536316530ac78c1))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [3.29.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.29.0...google-cloud-asset-v3.29.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([4571dff](https://github.com/googleapis/google-cloud-python/commit/4571dff9614843c6944c8568bd234c6ac5197218))

## [3.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.28.0...google-cloud-asset-v3.29.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))
* Add support for reading selective GAPIC generation methods from service YAML ([b1c3ce8](https://github.com/googleapis/google-cloud-python/commit/b1c3ce8b271e9d22afabcde054e81dcedae6b0ef))

## [3.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.27.1...google-cloud-asset-v3.28.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [3.27.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.27.0...google-cloud-asset-v3.27.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([85c7512](https://github.com/googleapis/google-cloud-python/commit/85c7512bbdde2b9cc60b4ad42b8c36c4558a07a5))

## [3.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.26.4...google-cloud-asset-v3.27.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13200](https://github.com/googleapis/google-cloud-python/issues/13200)) ([19dc048](https://github.com/googleapis/google-cloud-python/commit/19dc0485852406b90743297bcf257020e6012593))

## [3.26.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.26.3...google-cloud-asset-v3.26.4) (2024-09-16)


### Documentation

* [google-cloud-asset] Comments are clarified for certain fields in messages `QueryAssetsResponse` and `ResourceSearchResult` ([#13076](https://github.com/googleapis/google-cloud-python/issues/13076)) ([35b2c45](https://github.com/googleapis/google-cloud-python/commit/35b2c456c6791bc47ffe894f3ef966558cb6c98e))

## [3.26.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.26.2...google-cloud-asset-v3.26.3) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([6e83a37](https://github.com/googleapis/google-cloud-python/commit/6e83a37612d9eb951cb0ef1e372ef4241f8afa59))

## [3.26.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.26.1...google-cloud-asset-v3.26.2) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12863](https://github.com/googleapis/google-cloud-python/issues/12863)) ([3e6e423](https://github.com/googleapis/google-cloud-python/commit/3e6e423b86cdace8538f610941aa84c7a6217934))

## [3.26.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.26.0...google-cloud-asset-v3.26.1) (2024-04-24)


### Documentation

* fix required permissions for resources.searchAll and iamPolicies.searchAll ([bbc49a5](https://github.com/googleapis/google-cloud-python/commit/bbc49a5476ab8a3fc3dafd4186e2b39319d9e6bf))

## [3.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.25.1...google-cloud-asset-v3.26.0) (2024-03-28)


### Features

* add tag key id support ([2c17f60](https://github.com/googleapis/google-cloud-python/commit/2c17f60ab9dca74be1e99a1e056f7661b9a2b8c1))


### Documentation

* add tagKeyIds example for ResourceSearchResult.tags ([2c17f60](https://github.com/googleapis/google-cloud-python/commit/2c17f60ab9dca74be1e99a1e056f7661b9a2b8c1))

## [3.25.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.25.0...google-cloud-asset-v3.25.1) (2024-03-22)


### Documentation

* [google-cloud-asset] Minor comment updates ([#12477](https://github.com/googleapis/google-cloud-python/issues/12477)) ([e6374ef](https://github.com/googleapis/google-cloud-python/commit/e6374efd784192c64f76b29268105442c9637d4f))

## [3.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.24.3...google-cloud-asset-v3.25.0) (2024-03-07)


### Features

* Add `asset_type` field to `GovernedIamPolicy` and `GovernedResource` ([ff71d1a](https://github.com/googleapis/google-cloud-python/commit/ff71d1a34668a0684b0ec55cf068774faf3c127f))
* Add `effective_tags` field to `GovernedResource` ([ff71d1a](https://github.com/googleapis/google-cloud-python/commit/ff71d1a34668a0684b0ec55cf068774faf3c127f))
* Add field `condition_evaluation` to `AnalyzerOrgPolicy.Rule` ([ff71d1a](https://github.com/googleapis/google-cloud-python/commit/ff71d1a34668a0684b0ec55cf068774faf3c127f))
* Add fields `project`, `folders` and `organization` to `OrgPolicyResult` ([ff71d1a](https://github.com/googleapis/google-cloud-python/commit/ff71d1a34668a0684b0ec55cf068774faf3c127f))
* Add fields `project`, `folders`, `organization` and `effective_tags` to `GovernedContainer` ([ff71d1a](https://github.com/googleapis/google-cloud-python/commit/ff71d1a34668a0684b0ec55cf068774faf3c127f))


### Documentation

* Update comment for rpc `AnalyzeOrgPolicyGovernedAssets` to include additional canned constraints ([ff71d1a](https://github.com/googleapis/google-cloud-python/commit/ff71d1a34668a0684b0ec55cf068774faf3c127f))

## [3.24.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.24.2...google-cloud-asset-v3.24.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12381](https://github.com/googleapis/google-cloud-python/issues/12381)) ([48ae8ab](https://github.com/googleapis/google-cloud-python/commit/48ae8aba7ec71a382e001b3a659022f942c3b436))

## [3.24.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.24.1...google-cloud-asset-v3.24.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))
* fix ValueError in test__validate_universe_domain ([e6cd222](https://github.com/googleapis/google-cloud-python/commit/e6cd22212a6f62907c855cf889ee6055c1969eb0))


### Documentation

* [google-cloud-asset] updated comments ([e6cd222](https://github.com/googleapis/google-cloud-python/commit/e6cd22212a6f62907c855cf889ee6055c1969eb0))

## [3.24.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.24.0...google-cloud-asset-v3.24.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [3.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.23.0...google-cloud-asset-v3.24.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [3.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.22.0...google-cloud-asset-v3.23.0) (2024-01-04)


### Features

* Added new resource references to fields in AnalyzeMoveRequest  ([599e175](https://github.com/googleapis/google-cloud-python/commit/599e1754f44f934060c935f0af4d88412edda582))


### Documentation

* Updated comments ([599e175](https://github.com/googleapis/google-cloud-python/commit/599e1754f44f934060c935f0af4d88412edda582))

## [3.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.21.0...google-cloud-asset-v3.22.0) (2023-12-12)


### Features

* added Asset.access_policy, access_level, service_perimeter, org_policy ([0fc00b8](https://github.com/googleapis/google-cloud-python/commit/0fc00b8514fa29dd183381e5dac8f712a37c2f34))
* added messages ExportAssetsResponse, BatchGetAssetsHistoryResponse ([0fc00b8](https://github.com/googleapis/google-cloud-python/commit/0fc00b8514fa29dd183381e5dac8f712a37c2f34))
* added resource definitions to some messages ([0fc00b8](https://github.com/googleapis/google-cloud-python/commit/0fc00b8514fa29dd183381e5dac8f712a37c2f34))


### Documentation

* updated comments ([0fc00b8](https://github.com/googleapis/google-cloud-python/commit/0fc00b8514fa29dd183381e5dac8f712a37c2f34))

## [3.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.20.1...google-cloud-asset-v3.21.0) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [3.20.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-asset-v3.20.0...google-cloud-asset-v3.20.1) (2023-11-15)


### Bug Fixes

* drop pkg_resources ([#12015](https://github.com/googleapis/google-cloud-python/issues/12015)) ([7e9cd0c](https://github.com/googleapis/google-cloud-python/commit/7e9cd0c8edb175b98176e3a2951fcd0b681fd3a6))

## [3.20.0](https://github.com/googleapis/python-asset/compare/v3.19.1...v3.20.0) (2023-10-16)


### Features

* Add support for directly attached and effective tags ([7e2b606](https://github.com/googleapis/python-asset/commit/7e2b606ad80569b58bfb5218eac98dba151c7ad0))


### Documentation

* Clarify comments for tags and effective tags ([7e2b606](https://github.com/googleapis/python-asset/commit/7e2b606ad80569b58bfb5218eac98dba151c7ad0))
* Minor formatting ([#586](https://github.com/googleapis/python-asset/issues/586)) ([6374962](https://github.com/googleapis/python-asset/commit/63749629f90d6c433e18526c028fc5d8a907a050))

## [3.19.1](https://github.com/googleapis/python-asset/compare/v3.19.0...v3.19.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#571](https://github.com/googleapis/python-asset/issues/571)) ([4bdad82](https://github.com/googleapis/python-asset/commit/4bdad82a3e49dd4a6e61f6fab40a8b7a54e8c771))

## [3.19.0](https://github.com/googleapis/python-asset/compare/v3.18.1...v3.19.0) (2023-04-01)


### Features

* Add support for AnalyzeOrgPolicies API ([00dcd06](https://github.com/googleapis/python-asset/commit/00dcd068b0a08425f981c8b6b7a7f8d79f931504))
* Add support for AnalyzeOrgPolicyGovernedAssets API ([00dcd06](https://github.com/googleapis/python-asset/commit/00dcd068b0a08425f981c8b6b7a7f8d79f931504))
* Add support for AnalyzeOrgPolicyGovernedContainers API ([00dcd06](https://github.com/googleapis/python-asset/commit/00dcd068b0a08425f981c8b6b7a7f8d79f931504))

## [3.18.1](https://github.com/googleapis/python-asset/compare/v3.18.0...v3.18.1) (2023-03-24)


### Documentation

* Fix formatting of request arg in docstring ([#558](https://github.com/googleapis/python-asset/issues/558)) ([21e3a6d](https://github.com/googleapis/python-asset/commit/21e3a6d50cf4152cd0f9a9767f30a09fc589941a))

## [3.18.0](https://github.com/googleapis/python-asset/compare/v3.17.1...v3.18.0) (2023-02-19)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#549](https://github.com/googleapis/python-asset/issues/549)) ([e6bd01b](https://github.com/googleapis/python-asset/commit/e6bd01b917e1a42157e8a0d8ea05de79462b02c7))

## [3.17.1](https://github.com/googleapis/python-asset/compare/v3.17.0...v3.17.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([e5e63a9](https://github.com/googleapis/python-asset/commit/e5e63a9a9894b5c5594d25b57c05e06f41c5d49d))


### Documentation

* Add documentation for enums ([e5e63a9](https://github.com/googleapis/python-asset/commit/e5e63a9a9894b5c5594d25b57c05e06f41c5d49d))

## [3.17.0](https://github.com/googleapis/python-asset/compare/v3.16.0...v3.17.0) (2023-01-14)


### Features

* Policy Analyzer for Organization Policy is publicly available ([ff8f92a](https://github.com/googleapis/python-asset/commit/ff8f92a3a8dd2c103545d44ca8305eaea68ddbc3))


### Documentation

* Brand and typo fixes ([ff8f92a](https://github.com/googleapis/python-asset/commit/ff8f92a3a8dd2c103545d44ca8305eaea68ddbc3))

## [3.16.0](https://github.com/googleapis/python-asset/compare/v3.15.0...v3.16.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#528](https://github.com/googleapis/python-asset/issues/528)) ([8d59164](https://github.com/googleapis/python-asset/commit/8d591642fdda7af069326de10e91c11829907872))

## [3.15.0](https://github.com/googleapis/python-asset/compare/v3.14.1...v3.15.0) (2023-01-07)


### Features

* Add a new searchable field kmsKeys ([#506](https://github.com/googleapis/python-asset/issues/506)) ([07dd6cc](https://github.com/googleapis/python-asset/commit/07dd6ccc25d032b3fad6a0a262067b7a4fdd5f65))
* Add support for `google.cloud.asset.__version__` ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))
* Add typing to proto.Message based class attributes ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))


### Bug Fixes

* Add dict typing for client_options ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))
* Deprecate searchable field kmsKey ([07dd6cc](https://github.com/googleapis/python-asset/commit/07dd6ccc25d032b3fad6a0a262067b7a4fdd5f65))
* **deps:** Allow protobuf 3.19.5 ([#508](https://github.com/googleapis/python-asset/issues/508)) ([818abbb](https://github.com/googleapis/python-asset/commit/818abbbcbb829a726d18ba1e7e7e03f997d4256a))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))
* Drop usage of pkg_resources ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))
* Fix timeout default values ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))
* Small change for documentation ([6bad165](https://github.com/googleapis/python-asset/commit/6bad165c91a86f7d685801c99cbdf79b3b31dbaf))

## [3.14.1](https://github.com/googleapis/python-asset/compare/v3.14.0...v3.14.1) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#502](https://github.com/googleapis/python-asset/issues/502)) ([4509ad5](https://github.com/googleapis/python-asset/commit/4509ad5a9e84c28082a97e96eeb08cab3c85d157))

## [3.14.0](https://github.com/googleapis/python-asset/compare/v3.13.1...v3.14.0) (2022-09-20)


### Features

* Add client library support for AssetService v1 SavedQuery APIs ([#496](https://github.com/googleapis/python-asset/issues/496)) ([1d1103e](https://github.com/googleapis/python-asset/commit/1d1103e86d9dac7e55d2bd2ba7cebf37c4b8d597))

## [3.13.1](https://github.com/googleapis/python-asset/compare/v3.13.0...v3.13.1) (2022-08-29)


### Documentation

* **samples:** add batch_get_effective_iam_policies sample code ([#480](https://github.com/googleapis/python-asset/issues/480)) ([b171684](https://github.com/googleapis/python-asset/commit/b171684a1edce93d358b308ff818627281f0809f))

## [3.13.0](https://github.com/googleapis/python-asset/compare/v3.12.0...v3.13.0) (2022-08-17)


### Features

* Add client library support for AssetService v1 BatchGetEffectiveIamPolicies API ([#474](https://github.com/googleapis/python-asset/issues/474)) ([28fdf20](https://github.com/googleapis/python-asset/commit/28fdf206a594b03cd15b985fa1e7de1fd8998df6))

## [3.12.0](https://github.com/googleapis/python-asset/compare/v3.11.0...v3.12.0) (2022-08-12)


### Features

* Release of query system ([#467](https://github.com/googleapis/python-asset/issues/467)) ([5517102](https://github.com/googleapis/python-asset/commit/551710241f08019005583100cc73c2b46ee9c9af))


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#469](https://github.com/googleapis/python-asset/issues/469)) ([7d4a11f](https://github.com/googleapis/python-asset/commit/7d4a11fcdc868b1f135b251ebf877cb57b78391d))
* **deps:** require proto-plus >= 1.22.0 ([7d4a11f](https://github.com/googleapis/python-asset/commit/7d4a11fcdc868b1f135b251ebf877cb57b78391d))

## [3.11.0](https://github.com/googleapis/python-asset/compare/v3.10.0...v3.11.0) (2022-08-09)


### Features

* Add client library support for AssetService v1 BatchGetEffectiveIamPolicies API ([#462](https://github.com/googleapis/python-asset/issues/462)) ([30a184b](https://github.com/googleapis/python-asset/commit/30a184b697fa7d9ece8d490fa5ec95251d644162))

## [3.10.0](https://github.com/googleapis/python-asset/compare/v3.9.1...v3.10.0) (2022-07-18)


### Features

* add audience parameter ([996c4e8](https://github.com/googleapis/python-asset/commit/996c4e877d59bdadb6b604a7fbd92b6fac5a597c))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#447](https://github.com/googleapis/python-asset/issues/447)) ([996c4e8](https://github.com/googleapis/python-asset/commit/996c4e877d59bdadb6b604a7fbd92b6fac5a597c))
* require python 3.7+ ([#450](https://github.com/googleapis/python-asset/issues/450)) ([2086ef9](https://github.com/googleapis/python-asset/commit/2086ef91a8c5573b7d67ec938bc18050cd5ba637))

## [3.9.1](https://github.com/googleapis/python-asset/compare/v3.9.0...v3.9.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#432](https://github.com/googleapis/python-asset/issues/432)) ([8c28318](https://github.com/googleapis/python-asset/commit/8c2831839fcf4457b5bff244d63ced7bea715807))


### Documentation

* fix changelog header to consistent size ([#434](https://github.com/googleapis/python-asset/issues/434)) ([68d237e](https://github.com/googleapis/python-asset/commit/68d237e999f94af889c6559229d1d6c439bfe29a))

## [3.9.0](https://github.com/googleapis/python-asset/compare/v3.8.1...v3.9.0) (2022-05-19)


### Features

* Add SavedQuery CURD support ([#425](https://github.com/googleapis/python-asset/issues/425)) ([b3e5650](https://github.com/googleapis/python-asset/commit/b3e5650732e46c4c6ee7835cdfa38c1232efb3b9))

## [3.8.1](https://github.com/googleapis/python-asset/compare/v3.8.0...v3.8.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#379](https://github.com/googleapis/python-asset/issues/379)) ([6ed1b9d](https://github.com/googleapis/python-asset/commit/6ed1b9db2edcf75daad250835118dd88f3017118))
* **deps:** require proto-plus>=1.15.0 ([6ed1b9d](https://github.com/googleapis/python-asset/commit/6ed1b9db2edcf75daad250835118dd88f3017118))

## [3.8.0](https://github.com/googleapis/python-asset/compare/v3.7.1...v3.8.0) (2022-02-26)


### Features

* add api key support ([#361](https://github.com/googleapis/python-asset/issues/361)) ([6d03a57](https://github.com/googleapis/python-asset/commit/6d03a57e37387342c047ca76f9e6c15941390ad6))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([e5a9160](https://github.com/googleapis/python-asset/commit/e5a91606d50937583718d97e1e3027498c86ace1))


### Documentation

* add autogenerated code snippets ([8e6877d](https://github.com/googleapis/python-asset/commit/8e6877de9c5969d493e67f545b93d0059c8ca182))

## [3.7.1](https://www.github.com/googleapis/python-asset/compare/v3.7.0...v3.7.1) (2021-11-02)


### Bug Fixes

* **deps:** drop packaging dependency ([3f3e552](https://www.github.com/googleapis/python-asset/commit/3f3e5522e5e550e2f401238e8b7f3cfc31cd17e9))
* **deps:** require google-api-core >= 1.28.0 ([3f3e552](https://www.github.com/googleapis/python-asset/commit/3f3e5522e5e550e2f401238e8b7f3cfc31cd17e9))
* fix extras_require typo in setup.py ([3f3e552](https://www.github.com/googleapis/python-asset/commit/3f3e5522e5e550e2f401238e8b7f3cfc31cd17e9))


### Documentation

* list oneofs in docstring ([3f3e552](https://www.github.com/googleapis/python-asset/commit/3f3e5522e5e550e2f401238e8b7f3cfc31cd17e9))

## [3.7.0](https://www.github.com/googleapis/python-asset/compare/v3.6.1...v3.7.0) (2021-10-12)


### Features

* add context manager support in client ([#314](https://www.github.com/googleapis/python-asset/issues/314)) ([659db45](https://www.github.com/googleapis/python-asset/commit/659db456ff6cc7a09fffd83479b2b43d5905239f))

## [3.6.1](https://www.github.com/googleapis/python-asset/compare/v3.6.0...v3.6.1) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([fa08cbf](https://www.github.com/googleapis/python-asset/commit/fa08cbfbac5c8ce566883ad2c2e79ca5b4f32027))

## [3.6.0](https://www.github.com/googleapis/python-asset/compare/v3.5.0...v3.6.0) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([79a5a8a](https://www.github.com/googleapis/python-asset/commit/79a5a8a11d49c52162b9467e291df38f70634858))


### Documentation

* add relationship samples ([#293](https://www.github.com/googleapis/python-asset/issues/293)) ([473e133](https://www.github.com/googleapis/python-asset/commit/473e133e2674bf6a5ae655fe67be7d79fed2d8e9))

## [3.5.0](https://www.github.com/googleapis/python-asset/compare/v3.4.0...v3.5.0) (2021-09-03)


### Features

* add inventory_path ([#283](https://www.github.com/googleapis/python-asset/issues/283)) ([fbb47e6](https://www.github.com/googleapis/python-asset/commit/fbb47e6487fe454ca84d2415cf756a87bf66739f))
* **v1:** Add content type Relationship to support relationship search ([038febe](https://www.github.com/googleapis/python-asset/commit/038febe4c21d6ece23872e01cffc1110c59d6699))
* **v1:** add relationships ([#281](https://www.github.com/googleapis/python-asset/issues/281)) ([038febe](https://www.github.com/googleapis/python-asset/commit/038febe4c21d6ece23872e01cffc1110c59d6699))

## [3.4.0](https://www.github.com/googleapis/python-asset/compare/v3.3.0...v3.4.0) (2021-08-17)


### Features

* Release of relationships in v1, Add content type Relationship to support relationship export  ([#262](https://www.github.com/googleapis/python-asset/issues/262)) ([93c92c1](https://www.github.com/googleapis/python-asset/commit/93c92c150581d22ff2f7b63d7591b3a97191ff20))

## [3.3.0](https://www.github.com/googleapis/python-asset/compare/v3.2.1...v3.3.0) (2021-07-28)


### Features

* Add AnalyzeMove API ([a242adc](https://www.github.com/googleapis/python-asset/commit/a242adc8864724acb2d12136bb09d68cb7fc729c))
* Add AttachedResource field for ResourceSearchResult ([a242adc](https://www.github.com/googleapis/python-asset/commit/a242adc8864724acb2d12136bb09d68cb7fc729c))
* Add read_mask field for SearchAllResourcesRequest ([a242adc](https://www.github.com/googleapis/python-asset/commit/a242adc8864724acb2d12136bb09d68cb7fc729c))
* Add VersionedResource field for ResourceSearchResult ([a242adc](https://www.github.com/googleapis/python-asset/commit/a242adc8864724acb2d12136bb09d68cb7fc729c))
* Change metadata field for the AnalyzeIamPolicyLongrunning ([#245](https://www.github.com/googleapis/python-asset/issues/245)) ([a242adc](https://www.github.com/googleapis/python-asset/commit/a242adc8864724acb2d12136bb09d68cb7fc729c))


### Bug Fixes

* enable self signed jwt for grpc ([#244](https://www.github.com/googleapis/python-asset/issues/244)) ([a15e185](https://www.github.com/googleapis/python-asset/commit/a15e18574ce4d58a22955284ebfe444c152b30c7))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#235](https://www.github.com/googleapis/python-asset/issues/235)) ([0d00e75](https://www.github.com/googleapis/python-asset/commit/0d00e75bf46d52beea0829b83a2df580a37491ca))


## [3.2.1](https://www.github.com/googleapis/python-asset/compare/v3.2.0...v3.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#234](https://www.github.com/googleapis/python-asset/issues/234)) ([0687c84](https://www.github.com/googleapis/python-asset/commit/0687c843a2bca03ddd4671dfe2b40863dbba3fee))

## [3.2.0](https://www.github.com/googleapis/python-asset/compare/v3.1.0...v3.2.0) (2021-07-12)


### Features

* add always_use_jwt_access ([0a14f25](https://www.github.com/googleapis/python-asset/commit/0a14f25784a5d39b666709c2dc6521f014eea781))
* add new searchable fields (memberTypes, roles, project, folders and organization) in SearchAllIamPolicies ([0a14f25](https://www.github.com/googleapis/python-asset/commit/0a14f25784a5d39b666709c2dc6521f014eea781))
* new request fields (assetTypes and orderBy) in SearchAllIamPolicies ([0a14f25](https://www.github.com/googleapis/python-asset/commit/0a14f25784a5d39b666709c2dc6521f014eea781))
* new response fields (assetType, folders and organization) in SearchAllIamPolicies ([0a14f25](https://www.github.com/googleapis/python-asset/commit/0a14f25784a5d39b666709c2dc6521f014eea781))


### Bug Fixes

* disable always_use_jwt_access ([0a14f25](https://www.github.com/googleapis/python-asset/commit/0a14f25784a5d39b666709c2dc6521f014eea781))
* disable always_use_jwt_access ([#217](https://www.github.com/googleapis/python-asset/issues/217)) ([0a14f25](https://www.github.com/googleapis/python-asset/commit/0a14f25784a5d39b666709c2dc6521f014eea781))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-asset/issues/1127)) ([#205](https://www.github.com/googleapis/python-asset/issues/205)) ([b9db51a](https://www.github.com/googleapis/python-asset/commit/b9db51a1e88615ab2da22da188d59987fcfca5d4)), closes [#1126](https://www.github.com/googleapis/python-asset/issues/1126)

## [3.1.0](https://www.github.com/googleapis/python-asset/compare/v3.0.0...v3.1.0) (2021-06-07)


### Features

* add `from_service_account_info` ([34278bf](https://www.github.com/googleapis/python-asset/commit/34278bf526384296e95196f755ab983c4efeca62))
* add Cloud Asset List API, add access time as condition context in request and evaluation value in response for Cloud Asset AnalyzeIamPolicy API, add more info (folders, organizations, kms_key, create_time, update_time, state, parent_full_resource_name, parent_asset_type) in response for Cloud Asset SearchAllResources API ([#196](https://www.github.com/googleapis/python-asset/issues/196)) ([69ecd23](https://www.github.com/googleapis/python-asset/commit/69ecd237ade97257c92ba8bbe6dd7a5eca83288f))
* support self-signed JWT flow for service accounts ([d0b9b21](https://www.github.com/googleapis/python-asset/commit/d0b9b21300eb9ad233cd8f7e0c73941bebc5fe46))


### Bug Fixes

* add async client to %name_%version/init.py ([d0b9b21](https://www.github.com/googleapis/python-asset/commit/d0b9b21300eb9ad233cd8f7e0c73941bebc5fe46))
* remove v1beta1 ([#127](https://www.github.com/googleapis/python-asset/issues/127)) ([dab2d53](https://www.github.com/googleapis/python-asset/commit/dab2d539a1c89c0a5f09df4c4cab4d86f1a4ab08))
* use correct retry deadlines ([#164](https://www.github.com/googleapis/python-asset/issues/164)) ([34278bf](https://www.github.com/googleapis/python-asset/commit/34278bf526384296e95196f755ab983c4efeca62))


### Documentation

* **python:** fix intersphinx link for google-auth ([#119](https://www.github.com/googleapis/python-asset/issues/119)) ([e455c9e](https://www.github.com/googleapis/python-asset/commit/e455c9e52641cd9f13440d342c9eeb931135889c))

## [2.2.0](https://www.github.com/googleapis/python-asset/compare/v2.1.0...v2.2.0) (2020-11-19)


### Features

* add AnalyzeIamPolicy and ExportIamPolicyAnalysis; support OSInventory; add common resource helper methods; expose client transport ([#113](https://www.github.com/googleapis/python-asset/issues/113)) ([3bf4c0a](https://www.github.com/googleapis/python-asset/commit/3bf4c0ab20346e3a12af168e20139f2cc067540a))


### Documentation

* remove note on editable installs ([#99](https://www.github.com/googleapis/python-asset/issues/99)) ([cf6072a](https://www.github.com/googleapis/python-asset/commit/cf6072a09b76dce78bd4c0c471c8c2d81186e0c6))

## [2.1.0](https://www.github.com/googleapis/python-asset/compare/v2.0.0...v2.1.0) (2020-09-25)


### Features

* add support for per type and partition export ([#86](https://www.github.com/googleapis/python-asset/issues/86)) ([cd26192](https://www.github.com/googleapis/python-asset/commit/cd2619262bbea00c01d054b783b218009171284e))


### Bug Fixes

* **sample:** mark a test with flaky ([#81](https://www.github.com/googleapis/python-asset/issues/81)) ([aa153dc](https://www.github.com/googleapis/python-asset/commit/aa153dce2f62c18101472c40964cc3cee9188d78)), closes [#75](https://www.github.com/googleapis/python-asset/issues/75)

## [2.0.0](https://www.github.com/googleapis/python-asset/compare/v1.3.0...v2.0.0) (2020-08-05)


### ⚠ BREAKING CHANGES

* move to microgenerator (#58)

### Features

* **asset:** Add sample code for two new RPCs. [([#4080](https://www.github.com/googleapis/python-asset/issues/4080))](https://github.com/GoogleCloudPlatform/python-docs-samples/issues/4080) ([3e935de](https://www.github.com/googleapis/python-asset/commit/3e935dea2db2f8528b5e5ba3f899bd9601037276))
* add sample code for ListAssets v1p5beta1 [([#4251](https://www.github.com/googleapis/python-asset/issues/4251))](https://github.com/GoogleCloudPlatform/python-docs-samples/issues/4251) ([187807f](https://www.github.com/googleapis/python-asset/commit/187807f07577f36daa88d5a2605c9eb1bf2918b7)), closes [#4250](https://www.github.com/googleapis/python-asset/issues/4250)
* move to microgenerator ([#58](https://www.github.com/googleapis/python-asset/issues/58)) ([3219b64](https://www.github.com/googleapis/python-asset/commit/3219b64c091d60ea62d669ee904517f73b07c0af))


### Bug Fixes

* limit asset types to avoid exceeding quota ([00b43e8](https://www.github.com/googleapis/python-asset/commit/00b43e8af859b85be16a0e59be32ac4844df77c4))

## [1.3.0](https://www.github.com/googleapis/python-asset/compare/v1.2.0...v1.3.0) (2020-06-25)


### Features

* generate v1p5beta1 ([#47](https://www.github.com/googleapis/python-asset/issues/47)) ([207eff4](https://www.github.com/googleapis/python-asset/commit/207eff44c20122c326bc939551f0177574d706dc))


### Bug Fixes

* update default retry configs ([#51](https://www.github.com/googleapis/python-asset/issues/51)) ([58f5d58](https://www.github.com/googleapis/python-asset/commit/58f5d58eba2f37af2a0161793fd61019a236cad3))

## [1.2.0](https://www.github.com/googleapis/python-asset/compare/v1.1.0...v1.2.0) (2020-06-23)


### Features

* **v1:** add support for condition in Feed ([#44](https://www.github.com/googleapis/python-asset/issues/44)) ([467ab58](https://www.github.com/googleapis/python-asset/commit/467ab58b43aa11d8d6f8087800e5d8b451984edc))

## [1.1.0](https://www.github.com/googleapis/python-asset/compare/v1.0.0...v1.1.0) (2020-06-10)

### Features

* add `search_all_resources` and `search_all_iam_policies` (via synth) ([#32](https://www.github.com/googleapis/python-asset/issues/32)) ([24a0827](https://www.github.com/googleapis/python-asset/commit/24a0827913dfa7563ea08cdf2e329626eadca4a3)), closes [#541](https://www.github.com/googleapis/python-asset/issues/541)

## [1.0.0](https://www.github.com/googleapis/python-asset/compare/v0.10.0...v1.0.0) (2020-06-10)


### Features

* release to GA ([#17](https://www.github.com/googleapis/python-asset/issues/17)) ([731e350](https://www.github.com/googleapis/python-asset/commit/731e350f6321a1b29b482ad360172754a2a255c6))

## [0.10.0](https://www.github.com/googleapis/python-asset/compare/v0.9.0...v0.10.0) (2020-05-08)


### Features

* add orgpolicy and accesscontextmanager (via synth) ([#26](https://www.github.com/googleapis/python-asset/issues/26)) ([c9d818e](https://www.github.com/googleapis/python-asset/commit/c9d818e4c53707d51395a33e6fc1b202126d6a29))

## [0.9.0](https://www.github.com/googleapis/python-asset/compare/v0.8.0...v0.9.0) (2020-03-17)


### Features

* add v1p4beta1 ([#16](https://www.github.com/googleapis/python-asset/issues/16)) ([b5771c3](https://www.github.com/googleapis/python-asset/commit/b5771c3bf6c580e414a998b63cef5400f2b3c50d))

## [0.8.0](https://www.github.com/googleapis/python-asset/compare/v0.7.0...v0.8.0) (2020-03-07)


### Features

* remove search resources and search iam policies support in v1p1beta1; remove export assets and batch get assets history from v1p2beta1 (via synth) ([#12](https://www.github.com/googleapis/python-asset/issues/12)) ([15b60a3](https://www.github.com/googleapis/python-asset/commit/15b60a349c93c928fe121dc47d44d812a0c14439))


### Bug Fixes

* **asset:** correct asset synthfile ([#10355](https://www.github.com/googleapis/python-asset/issues/10355)) ([32d9374](https://www.github.com/googleapis/python-asset/commit/32d937433109b55c8f6632d402859a38520ee153))

## 0.7.0

01-29-2020 10:53 PST

### New Features
- Add v1p1beta1, promote library to  beta. ([#10202](https://github.com/googleapis/google-cloud-python/pull/10202))
- Undeprecate resource name helper methods, add 2.7 deprecation warning (via synth).  ([#10036](https://github.com/googleapis/google-cloud-python/pull/10036))

## 0.6.0

12-12-2019 10:46 PST

### New Features
- Add real time feed support to v1 (via synth). ([#9930](https://github.com/googleapis/google-cloud-python/pull/9930))
- Deprecate resource name helper methods (via synth). ([#9827](https://github.com/googleapis/google-cloud-python/pull/9827))

### Documentation
- Change spacing in docs templates (via synth). ([#9736](https://github.com/googleapis/google-cloud-python/pull/9736))
- Add Python 2 sunset banner to documentation. ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))

### Internal / Testing Changes
- Normalize VPCSC configuration in systests. ([#9614](https://github.com/googleapis/google-cloud-python/pull/9614))

## 0.5.0

10-29-2019 14:26 PDT

### New Features
- Add `bigquery_destination` to `OutputConfig`; make `content_type` optional argument to `BatchGetAssetsHistoryRequest`; add `uri_prefix` to `GcsDestination`; add `ORG_POLICY` and `ACCESS_POLICY` content type enums ([#9555](https://github.com/googleapis/google-cloud-python/pull/9555))

### Documentation
- Remove compatability badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))

### Internal / Testing Changes
- Fix intersphinx reference to requests ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Remove CI for gh-pages; use googleapis.dev for api_core refs ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))

## 0.4.1

08-12-2019 13:44 PDT

### Documentation
- Fix links to googleapis.dev ([#8998](https://github.com/googleapis/google-cloud-python/pull/8998))

## 0.4.0

08-01-2019 14:24 PDT

### New Features
- Generate asset v1p2beta1. ([#8888](https://github.com/googleapis/google-cloud-python/pull/8888))

### Internal / Testing Changes
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 0.3.0

07-22-2019 17:42 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8382](https://github.com/googleapis/google-cloud-python/pull/8382))
- Add nox session docs, add routing header to method metadata (via synth). ([#7919](https://github.com/googleapis/google-cloud-python/pull/7919))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Add 'client_options' support (via synth). ([#8498](https://github.com/googleapis/google-cloud-python/pull/8498))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

### Internal / Testing Changes
- Update vpcsc test settings. ([#8627](https://github.com/googleapis/google-cloud-python/pull/8627))
- Pin black version (via synth) ([#8572](https://github.com/googleapis/google-cloud-python/pull/8572))
- Add VPCSC tests. ([#8613](https://github.com/googleapis/google-cloud-python/pull/8613))
- All: Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Add disclaimer to auto-generated template files (via synth). ([#8306](https://github.com/googleapis/google-cloud-python/pull/8306))
- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8232](https://github.com/googleapis/google-cloud-python/pull/8232))
- Fix coverage in 'types.py'. ([#8144](https://github.com/googleapis/google-cloud-python/pull/8144))
- Blacken noxfile.py, setup.py (via synth). ([#8114](https://github.com/googleapis/google-cloud-python/pull/8114))
-  Declare encoding as utf-8 in pb2 files (via synth). ([#8343](https://github.com/googleapis/google-cloud-python/pull/8343))
- Add empty lines (via synth). ([#8047](https://github.com/googleapis/google-cloud-python/pull/8047))

## 0.2.0

03-19-2019 12:17 PDT


### Implementation Changes
- Rename 'GcsDestination.uri' -> 'object_uri', docstring changes . ([#7202](https://github.com/googleapis/google-cloud-python/pull/7202))
- Protoc-generated serialization update.. ([#7073](https://github.com/googleapis/google-cloud-python/pull/7073))

### New Features
- Generate v1. ([#7513](https://github.com/googleapis/google-cloud-python/pull/7513))

### Documentation
- Fix broken links to Cloud Asset API ([#7524](https://github.com/googleapis/google-cloud-python/pull/7524))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Update copyright headers
- Pick up stub docstring fix in GAPIC generator.[#6963](https://github.com/googleapis/google-cloud-python/pull/6963))

### Internal / Testing Changes
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Add support for including protos in synth ([#7114](https://github.com/googleapis/google-cloud-python/pull/7114))

## 0.1.2

12-17-2018 16:15 PST


### Implementation Changes
- Use moved iam.policy now at google.api_core.iam.policy ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up enum fixes in the GAPIC generator. ([#6607](https://github.com/googleapis/google-cloud-python/pull/6607))
- Pick up fixes in GAPIC generator. ([#6489](https://github.com/googleapis/google-cloud-python/pull/6489))
- Fix client_info bug, update docstrings. ([#6403](https://github.com/googleapis/google-cloud-python/pull/6403))
- Synth docstring changes generated from updated protos ([#6349](https://github.com/googleapis/google-cloud-python/pull/6349))
- Generated cloud asset client files are under asset-[version] ([#6341](https://github.com/googleapis/google-cloud-python/pull/6341))

### New Features

### Dependencies
- Add 'mock' to unit test dependencies for autogen libs. ([#6402](https://github.com/googleapis/google-cloud-python/pull/6402))
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))
- Avoid broken 'google-common-apis 1.5.4' release. ([#6355](https://github.com/googleapis/google-cloud-python/pull/6355))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Fix docs build. ([#6351](https://github.com/googleapis/google-cloud-python/pull/6351))
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))

### Internal / Testing Changes
- Add templating to asset synth.py ([#6606](https://github.com/googleapis/google-cloud-python/pull/6606))
- Add synth metadata. ([#6560](https://github.com/googleapis/google-cloud-python/pull/6560))
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Unblack gapic and protos.
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))

## 0.1.1

### Packaging
- Release as `google-cloud-asset`, rather than `google-cloud-cloudasset` ([#5998](https://github.com/googleapis/google-cloud-python/pull/5998))

## 0.1.0

Initial release.
