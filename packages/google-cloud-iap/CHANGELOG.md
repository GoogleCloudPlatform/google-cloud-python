# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-iap/#history

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.22.0...google-cloud-iap-v1.23.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.21.0...google-cloud-iap-v1.22.0) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.20.0...google-cloud-iap-v1.21.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.19.0...google-cloud-iap-v1.20.0) (2026-03-23)


### Features

* add oauth fields for IapSettings ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.18.0...google-cloud-iap-v1.19.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.17.1...google-cloud-iap-v1.18.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.17.0...google-cloud-iap-v1.17.1) (2025-05-29)


### Documentation

* Add clarifications on IAP CorsSettings behavior ([80c61d3](https://github.com/googleapis/google-cloud-python/commit/80c61d3fb32e124be9c02d0439a00d12f67d890a))
* Minor updates on GcipSettings description ([80c61d3](https://github.com/googleapis/google-cloud-python/commit/80c61d3fb32e124be9c02d0439a00d12f67d890a))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.16.2...google-cloud-iap-v1.17.0) (2025-04-12)


### Features

* Add fields `AccessSettings.workforce_identity_settings` and `AccessSettings.identity_sources` ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Use IAP with Workforce Identity Federation ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))


### Documentation

* A comment for enum `PolicyType` is changed ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* A comment for field `cidrs` in message `.google.cloud.iap.v1.TunnelDestGroup` is changed ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* A comment for field `fqdns` in message `.google.cloud.iap.v1.TunnelDestGroup` is changed ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* A comment for field `name` in message `.google.cloud.iap.v1.TunnelDestGroup` is changed ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `access_denied_page_settings` in message `.google.cloud.iap.v1.ApplicationSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `access_settings` in message `.google.cloud.iap.v1.IapSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `allowed_domains_settings` in message `.google.cloud.iap.v1.AccessSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `application_settings` in message `.google.cloud.iap.v1.IapSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `attribute_propagation_settings` in message `.google.cloud.iap.v1.ApplicationSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `cors_settings` in message `.google.cloud.iap.v1.AccessSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `csm_settings` in message `.google.cloud.iap.v1.ApplicationSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `domains` in message `.google.cloud.iap.v1.AllowedDomainsSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `enable` in message `.google.cloud.iap.v1.AllowedDomainsSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `enable` in message `.google.cloud.iap.v1.AttributePropagationSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `expression` in message `.google.cloud.iap.v1.AttributePropagationSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `gcip_settings` in message `.google.cloud.iap.v1.AccessSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `max_age` in message `.google.cloud.iap.v1.ReauthSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `method` in message `.google.cloud.iap.v1.ReauthSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `oauth_settings` in message `.google.cloud.iap.v1.AccessSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `output_credentials` in message `.google.cloud.iap.v1.AttributePropagationSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `policy_type` in message `.google.cloud.iap.v1.ReauthSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `programmatic_clients` in message `.google.cloud.iap.v1.OAuthSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `reauth_settings` in message `.google.cloud.iap.v1.AccessSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))
* Mark `tenant_ids` in message `.google.cloud.iap.v1.GcipSettings` as optional ([9114e1d](https://github.com/googleapis/google-cloud-python/commit/9114e1da42d7994f4050c9204538e04ee4735eff))

## [1.16.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.16.1...google-cloud-iap-v1.16.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.16.0...google-cloud-iap-v1.16.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([16e14c8](https://github.com/googleapis/google-cloud-python/commit/16e14c8d547864360dcab45d90e9e55169204fc6))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.15.0...google-cloud-iap-v1.16.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.14.1...google-cloud-iap-v1.15.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))

## [1.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.14.0...google-cloud-iap-v1.14.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.13.5...google-cloud-iap-v1.14.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13207](https://github.com/googleapis/google-cloud-python/issues/13207)) ([ceb9be8](https://github.com/googleapis/google-cloud-python/commit/ceb9be8f89ac7355d842bac1d77b2926eb0b649c))

## [1.13.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.13.4...google-cloud-iap-v1.13.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [1.13.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.13.3...google-cloud-iap-v1.13.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12867](https://github.com/googleapis/google-cloud-python/issues/12867)) ([3362176](https://github.com/googleapis/google-cloud-python/commit/33621762b989106ccf85adb538cf531c513a746c))

## [1.13.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.13.2...google-cloud-iap-v1.13.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12385](https://github.com/googleapis/google-cloud-python/issues/12385)) ([d50f4d0](https://github.com/googleapis/google-cloud-python/commit/d50f4d042774e2f12e9fe03459eae9ce91247df3))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.13.1...google-cloud-iap-v1.13.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12307](https://github.com/googleapis/google-cloud-python/issues/12307)) ([be87bc4](https://github.com/googleapis/google-cloud-python/commit/be87bc4a33fe32a512448a42246c9873da88269f))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.13.0...google-cloud-iap-v1.13.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.12.0...google-cloud-iap-v1.13.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12241](https://github.com/googleapis/google-cloud-python/issues/12241)) ([aae72f5](https://github.com/googleapis/google-cloud-python/commit/aae72f5e6c7d48e777fdf68d1012b2b51b912bad))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.11.0...google-cloud-iap-v1.12.0) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.10.3...google-cloud-iap-v1.11.0) (2023-09-19)


### Features

* Adding programmatic_clients attribute to UpdateIapSettings API request ([#11649](https://github.com/googleapis/google-cloud-python/issues/11649)) ([269241b](https://github.com/googleapis/google-cloud-python/commit/269241b45b2a83618fe7eebaa72550db548aa2af))


### Documentation

* Fixing Oauth typo ([#11662](https://github.com/googleapis/google-cloud-python/issues/11662)) ([e6fcc93](https://github.com/googleapis/google-cloud-python/commit/e6fcc93562d9f9c0ef84c2aaa268178fc1789cb9))

## [1.10.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.10.2...google-cloud-iap-v1.10.3) (2023-08-03)


### Documentation

* Minor formatting ([#11543](https://github.com/googleapis/google-cloud-python/issues/11543)) ([8cc031e](https://github.com/googleapis/google-cloud-python/commit/8cc031e723350890b4ceb6e813f24c4bcde3d65f))

## [1.10.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-iap-v1.10.1...google-cloud-iap-v1.10.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [1.10.1](https://github.com/googleapis/python-iap/compare/v1.10.0...v1.10.1) (2023-04-01)


### Documentation

* Minor changes in AttributePropagationSettings ([#168](https://github.com/googleapis/python-iap/issues/168)) ([2c61c43](https://github.com/googleapis/python-iap/commit/2c61c438f6e254fea0662589f7047d2c8464d9f2))

## [1.10.0](https://github.com/googleapis/python-iap/compare/v1.9.0...v1.10.0) (2023-03-23)


### Features

* Add an enum ENROLLED_SECOND_FACTORS under IapSettings ([8890e9e](https://github.com/googleapis/python-iap/commit/8890e9eceb2cfc41c3fee269d2e084052e783c5e))


### Documentation

* Fix formatting of request arg in docstring ([#167](https://github.com/googleapis/python-iap/issues/167)) ([a95d454](https://github.com/googleapis/python-iap/commit/a95d4548860e8bf8f3a6e269c9b3882cda42d364))
* Update doc description for field_mask ([8890e9e](https://github.com/googleapis/python-iap/commit/8890e9eceb2cfc41c3fee269d2e084052e783c5e))

## [1.9.0](https://github.com/googleapis/python-iap/compare/v1.8.1...v1.9.0) (2023-02-19)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#157](https://github.com/googleapis/python-iap/issues/157)) ([15be642](https://github.com/googleapis/python-iap/commit/15be6424ef580e8f02855a7f939a331a42236cd1))

## [1.8.1](https://github.com/googleapis/python-iap/compare/v1.8.0...v1.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([6d93973](https://github.com/googleapis/python-iap/commit/6d9397372916d91bb156f8995f3741c98729aa84))


### Documentation

* Add documentation for enums ([6d93973](https://github.com/googleapis/python-iap/commit/6d9397372916d91bb156f8995f3741c98729aa84))

## [1.8.0](https://github.com/googleapis/python-iap/compare/v1.7.0...v1.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#149](https://github.com/googleapis/python-iap/issues/149)) ([e136d2f](https://github.com/googleapis/python-iap/commit/e136d2fcd7e12c811972a2ff0fe819154e9cfca2))

## [1.7.0](https://github.com/googleapis/python-iap/compare/v1.6.0...v1.7.0) (2023-01-04)


### Features

* Add AllowedDomainSettings to the UpdateIapSettingsRequest ([1be4844](https://github.com/googleapis/python-iap/commit/1be48441b21823dbc1ac53f7da7290da7bb66352))
* Add AttributePropagationSettings to the UpdateIapSettingsRequest ([1be4844](https://github.com/googleapis/python-iap/commit/1be48441b21823dbc1ac53f7da7290da7bb66352))
* Add remediation_token_generation_enabled to the CsmSettings ([1be4844](https://github.com/googleapis/python-iap/commit/1be48441b21823dbc1ac53f7da7290da7bb66352))

## [1.6.0](https://github.com/googleapis/python-iap/compare/v1.5.4...v1.6.0) (2022-12-14)


### Features

* Add support for `google.cloud.iap.__version__` ([828e0bd](https://github.com/googleapis/python-iap/commit/828e0bdc68c1f1c0f8986dec6bd0d99b0bd8f561))
* Add typing to proto.Message based class attributes ([828e0bd](https://github.com/googleapis/python-iap/commit/828e0bdc68c1f1c0f8986dec6bd0d99b0bd8f561))


### Bug Fixes

* Add dict typing for client_options ([828e0bd](https://github.com/googleapis/python-iap/commit/828e0bdc68c1f1c0f8986dec6bd0d99b0bd8f561))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([2c0f3e5](https://github.com/googleapis/python-iap/commit/2c0f3e5f044b956b02e1389741adeaa0ee2bc259))
* Drop usage of pkg_resources ([2c0f3e5](https://github.com/googleapis/python-iap/commit/2c0f3e5f044b956b02e1389741adeaa0ee2bc259))
* Fix timeout default values ([2c0f3e5](https://github.com/googleapis/python-iap/commit/2c0f3e5f044b956b02e1389741adeaa0ee2bc259))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([828e0bd](https://github.com/googleapis/python-iap/commit/828e0bdc68c1f1c0f8986dec6bd0d99b0bd8f561))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([2c0f3e5](https://github.com/googleapis/python-iap/commit/2c0f3e5f044b956b02e1389741adeaa0ee2bc259))

## [1.5.4](https://github.com/googleapis/python-iap/compare/v1.5.3...v1.5.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#137](https://github.com/googleapis/python-iap/issues/137)) ([c5fd70f](https://github.com/googleapis/python-iap/commit/c5fd70f7168a5a87a52afb25a399a6990ab2c9e0))

## [1.5.3](https://github.com/googleapis/python-iap/compare/v1.5.2...v1.5.3) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#135](https://github.com/googleapis/python-iap/issues/135)) ([8ba970c](https://github.com/googleapis/python-iap/commit/8ba970cd3e7395e3c52cdf57b0af813f5d68e162))

## [1.5.2](https://github.com/googleapis/python-iap/compare/v1.5.1...v1.5.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#120](https://github.com/googleapis/python-iap/issues/120)) ([e5e67d0](https://github.com/googleapis/python-iap/commit/e5e67d0df1f26b1a786e23b26028de1406458b3f))
* **deps:** require proto-plus >= 1.22.0 ([e5e67d0](https://github.com/googleapis/python-iap/commit/e5e67d0df1f26b1a786e23b26028de1406458b3f))

## [1.5.1](https://github.com/googleapis/python-iap/compare/v1.5.0...v1.5.1) (2022-07-13)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#114](https://github.com/googleapis/python-iap/issues/114)) ([ecf5c0e](https://github.com/googleapis/python-iap/commit/ecf5c0ef344578bc32474b1b6b13216faa2ebcbb))

## [1.5.0](https://github.com/googleapis/python-iap/compare/v1.4.1...v1.5.0) (2022-07-12)


### Features

* add audience parameter ([01dc926](https://github.com/googleapis/python-iap/commit/01dc926fe83c7e774aefa7d5b859aa0c8a606e8e))


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#110](https://github.com/googleapis/python-iap/issues/110)) ([01dc926](https://github.com/googleapis/python-iap/commit/01dc926fe83c7e774aefa7d5b859aa0c8a606e8e))
* require python 3.7+ ([#112](https://github.com/googleapis/python-iap/issues/112)) ([7230d5f](https://github.com/googleapis/python-iap/commit/7230d5f2d9b15c970d56305a823886858b3d23c9))

## [1.4.1](https://github.com/googleapis/python-iap/compare/v1.4.0...v1.4.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#103](https://github.com/googleapis/python-iap/issues/103)) ([c8b9cc5](https://github.com/googleapis/python-iap/commit/c8b9cc54d3734f62fd5bfaeb8f7f107427f3bae3))


### Documentation

* fix changelog header to consistent size ([#102](https://github.com/googleapis/python-iap/issues/102)) ([7c7a470](https://github.com/googleapis/python-iap/commit/7c7a4705af42124a616a193ebc4a665bfa9e69be))

## [1.4.0](https://github.com/googleapis/python-iap/compare/v1.3.1...v1.4.0) (2022-05-19)


### Features

* add ReauthSettings to the UpdateIapSettingsRequest ([36c1866](https://github.com/googleapis/python-iap/commit/36c1866e605e4e880e65eb44a7d4dc49389f92f3))
* add the TunnelDestGroup-related methods and types ([#93](https://github.com/googleapis/python-iap/issues/93)) ([36c1866](https://github.com/googleapis/python-iap/commit/36c1866e605e4e880e65eb44a7d4dc49389f92f3))
* AuditConfig for IAM v1 ([49dc9c7](https://github.com/googleapis/python-iap/commit/49dc9c7162e956c684892bdf866f20b47e3b27d2))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([49dc9c7](https://github.com/googleapis/python-iap/commit/49dc9c7162e956c684892bdf866f20b47e3b27d2))

## [1.3.1](https://github.com/googleapis/python-iap/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#71](https://github.com/googleapis/python-iap/issues/71)) ([0e00d6a](https://github.com/googleapis/python-iap/commit/0e00d6a489ee97707bb733387a951e48e1f415dc))

## [1.3.0](https://github.com/googleapis/python-iap/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#57](https://github.com/googleapis/python-iap/issues/57)) ([1787cb0](https://github.com/googleapis/python-iap/commit/1787cb00158f111915d0f9bb948abeceab75a6f4))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([18f725d](https://github.com/googleapis/python-iap/commit/18f725d81007e02d2054538087d7567029b2d179))


### Documentation

* add generated snippets ([#62](https://github.com/googleapis/python-iap/issues/62)) ([27c14d2](https://github.com/googleapis/python-iap/commit/27c14d24ce50d6bb80f09218bcf0ebc1db9ceabd))

## [1.2.1](https://www.github.com/googleapis/python-iap/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([30b353c](https://www.github.com/googleapis/python-iap/commit/30b353c9296d37f8792759a5ee997b3f50572f19))
* **deps:** require google-api-core >= 1.28.0 ([30b353c](https://www.github.com/googleapis/python-iap/commit/30b353c9296d37f8792759a5ee997b3f50572f19))


### Documentation

* list oneofs in docstring ([30b353c](https://www.github.com/googleapis/python-iap/commit/30b353c9296d37f8792759a5ee997b3f50572f19))

## [1.2.0](https://www.github.com/googleapis/python-iap/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add support for python 3.10 ([#37](https://www.github.com/googleapis/python-iap/issues/37)) ([7716426](https://www.github.com/googleapis/python-iap/commit/7716426b83a457a3206fae1dee66c46cf35bd7e7))

## [1.1.0](https://www.github.com/googleapis/python-iap/compare/v1.0.2...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#34](https://www.github.com/googleapis/python-iap/issues/34)) ([a985591](https://www.github.com/googleapis/python-iap/commit/a985591b016e768a5a172ab5f8de873319b1e7e0))

## [1.0.2](https://www.github.com/googleapis/python-iap/compare/v1.0.1...v1.0.2) (2021-10-05)


### Bug Fixes

* improper types in pagers generation ([242d445](https://www.github.com/googleapis/python-iap/commit/242d44516fe55141a26024653158ea94fa93e525))

## [1.0.1](https://www.github.com/googleapis/python-iap/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([a5b27d2](https://www.github.com/googleapis/python-iap/commit/a5b27d26e4bc845aeede7281959a81f693ee52c2))

## [1.0.0](https://www.github.com/googleapis/python-iap/compare/v0.1.2...v1.0.0) (2021-08-09)


### Features

* bump release level to production/stable ([#13](https://www.github.com/googleapis/python-iap/issues/13)) ([9d0a9f8](https://www.github.com/googleapis/python-iap/commit/9d0a9f84554b98fd2b1829532c9c13b16432b0af))

## [0.1.2](https://www.github.com/googleapis/python-iap/compare/v0.1.1...v0.1.2) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#9](https://www.github.com/googleapis/python-iap/issues/9)) ([51304a3](https://www.github.com/googleapis/python-iap/commit/51304a327207a233e40308a8b49c9fdeda87c28b))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#5](https://www.github.com/googleapis/python-iap/issues/5)) ([2ba31c5](https://www.github.com/googleapis/python-iap/commit/2ba31c5a2ea2e52c4a79410548a252bf8fc0522e))


### Miscellaneous Chores

* release as 0.1.2 ([#10](https://www.github.com/googleapis/python-iap/issues/10)) ([4499ba5](https://www.github.com/googleapis/python-iap/commit/4499ba5ccd90edc882fbda73e4d792074ff44e6d))

## [0.1.1](https://www.github.com/googleapis/python-iap/compare/v0.1.0...v0.1.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#4](https://www.github.com/googleapis/python-iap/issues/4)) ([21e9e57](https://www.github.com/googleapis/python-iap/commit/21e9e57451a87d9f9dd1137142d138cb73aa746c))

## 0.1.0 (2021-07-06)


### Features

* generate v1 ([6fdf055](https://www.github.com/googleapis/python-iap/commit/6fdf055c835adf6715bf43e9255d02abcd2affd4))
