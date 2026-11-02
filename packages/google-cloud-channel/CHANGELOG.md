# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-channel/#history

## [1.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.28.0...google-cloud-channel-v1.29.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.27.0...google-cloud-channel-v1.28.0) (2026-06-02)


### Features

* regenerate google-cloud-c packages (#17091) ([165839343695fc74d09fc7900d4c55ddcb31a4d8](https://github.com/googleapis/google-cloud-python/commit/165839343695fc74d09fc7900d4c55ddcb31a4d8))

## [1.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.26.0...google-cloud-channel-v1.27.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.25.0...google-cloud-channel-v1.26.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.24.0...google-cloud-channel-v1.25.0) (2025-12-04)


### Documentation

* A comment for field `owned` in message `.google.cloud.channel.v1.CloudIdentityCustomerAccount` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `customer_attestation_state` in message `.google.cloud.channel.v1.Customer` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `event_type` in message `.google.cloud.channel.v1.CustomerEvent` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for method `RegisterSubscriber` in service `CloudChannelService` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `account` in message `.google.cloud.channel.v1.RegisterSubscriberRequest` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for message `ChangeParametersRequest` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `account` in message `.google.cloud.channel.v1.ListSubscribersRequest` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `offers` in message `.google.cloud.channel.v1.ListOffersResponse` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `page_token` in message `.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for method `UnregisterSubscriber` in service `CloudChannelService` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `entitlement_granularity` in message `.google.cloud.channel.v1.RepricingConfig` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `account` in message `.google.cloud.channel.v1.UnregisterSubscriberRequest` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `event_type` in message `.google.cloud.channel.v1.EntitlementEvent` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `page_token` in message `.google.cloud.channel.v1.ListSkuGroupsRequest` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `next_page_token` in message `.google.cloud.channel.v1.ListSkuGroupsResponse` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for field `next_page_token` in message `.google.cloud.channel.v1.ListSkuGroupBillableSkusResponse` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for enum `CustomerAttestationState` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))
* A comment for method `ListSubscribers` in service `CloudChannelService` is changed ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))


### Bug Fixes

* Changed field behavior for an existing field `entitlement_granularity` in message `.google.cloud.channel.v1.RepricingConfig` ([2da5c2afe0241e6dcb33aa9a0e5032012bf63df4](https://github.com/googleapis/google-cloud-python/commit/2da5c2afe0241e6dcb33aa9a0e5032012bf63df4))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.23.0...google-cloud-channel-v1.24.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.22.2...google-cloud-channel-v1.23.0) (2025-06-19)


### Features

* A new enum `CustomerAttestationState` is added ([92713ab](https://github.com/googleapis/google-cloud-python/commit/92713ab86a4dbbd7112176f7985b5fd3e82d1ca9))
* A new field `customer_attestation_state` is added to message `.google.cloud.channel.v1.Customer` ([92713ab](https://github.com/googleapis/google-cloud-python/commit/92713ab86a4dbbd7112176f7985b5fd3e82d1ca9))

## [1.22.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.22.1...google-cloud-channel-v1.22.2) (2025-06-11)


### Documentation

* Update import statement example in README ([8697120](https://github.com/googleapis/google-cloud-python/commit/869712032803cb31d93f3b16abc2abdb14f733a4))

## [1.22.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.22.0...google-cloud-channel-v1.22.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([1e43e75](https://github.com/googleapis/google-cloud-python/commit/1e43e75e99445373785b11381e0e859fa14bb485))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.21.0...google-cloud-channel-v1.22.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))
* Add support for reading selective GAPIC generation methods from service YAML ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.20.1...google-cloud-channel-v1.21.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))

## [1.20.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.20.0...google-cloud-channel-v1.20.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([53c951e](https://github.com/googleapis/google-cloud-python/commit/53c951e90ad1d702fa507495532086d5d2f6b3c0))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.19.0...google-cloud-channel-v1.20.0) (2024-10-24)


### Features

* Add support for  Python 3.13 ([6252476](https://github.com/googleapis/google-cloud-python/commit/6252476e5938352fb2417d098a1edcc08558fe10))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.18.5...google-cloud-channel-v1.19.0) (2024-10-08)


### Features

* Add support for importing team customer from a different reseller ([c38431b](https://github.com/googleapis/google-cloud-python/commit/c38431b363fd4f18bb692593f401e3ac3759637c))
* Add support for primary_admin_email as customer_identity for ImportCustomer ([c38431b](https://github.com/googleapis/google-cloud-python/commit/c38431b363fd4f18bb692593f401e3ac3759637c))
* Add support to look up team customer Cloud Identity information ([c38431b](https://github.com/googleapis/google-cloud-python/commit/c38431b363fd4f18bb692593f401e3ac3759637c))


### Documentation

* Clarify the expected value of the domain field for team type customers ([c38431b](https://github.com/googleapis/google-cloud-python/commit/c38431b363fd4f18bb692593f401e3ac3759637c))

## [1.18.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.18.4...google-cloud-channel-v1.18.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([a6f7356](https://github.com/googleapis/google-cloud-python/commit/a6f7356f1549721f9fab83d4dcfa226cec1965d0))

## [1.18.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.18.3...google-cloud-channel-v1.18.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12865](https://github.com/googleapis/google-cloud-python/issues/12865)) ([7f9dedb](https://github.com/googleapis/google-cloud-python/commit/7f9dedb3abc7636cbcd97e21ac857844b885b599))

## [1.18.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.18.2...google-cloud-channel-v1.18.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12383](https://github.com/googleapis/google-cloud-python/issues/12383)) ([305f43f](https://github.com/googleapis/google-cloud-python/commit/305f43f7d6293e3316248f421fdc19c5d8405c21))

## [1.18.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.18.1...google-cloud-channel-v1.18.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12281](https://github.com/googleapis/google-cloud-python/issues/12281)) ([62cf934](https://github.com/googleapis/google-cloud-python/commit/62cf934b140173d7b39e6c9ffa66e218b98260d4))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12305](https://github.com/googleapis/google-cloud-python/issues/12305)) ([2aa7f17](https://github.com/googleapis/google-cloud-python/commit/2aa7f17a5fd4f2249260225db91fb0414d06eaa7))

## [1.18.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.18.0...google-cloud-channel-v1.18.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.17.1...google-cloud-channel-v1.18.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12238](https://github.com/googleapis/google-cloud-python/issues/12238)) ([8701267](https://github.com/googleapis/google-cloud-python/commit/8701267fc9694844b9365024cd59354785247aa0))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.17.0...google-cloud-channel-v1.17.1) (2024-01-04)


### Documentation

* Add deprecation comment for method `FetchReportResults` in service `CloudChannelReportsService` ([1e6bf49](https://github.com/googleapis/google-cloud-python/commit/1e6bf49abdd6cc27af391acab15b4ca089111849))
* Add deprecation comment for method `ListReports` in service `CloudChannelReportsService` ([1e6bf49](https://github.com/googleapis/google-cloud-python/commit/1e6bf49abdd6cc27af391acab15b4ca089111849))
* Add deprecation comment for method `RunReportJob` in service `CloudChannelReportsService` ([1e6bf49](https://github.com/googleapis/google-cloud-python/commit/1e6bf49abdd6cc27af391acab15b4ca089111849))
* Add deprecation comment for service `CloudChannelReportsService` ([1e6bf49](https://github.com/googleapis/google-cloud-python/commit/1e6bf49abdd6cc27af391acab15b4ca089111849))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.16.0...google-cloud-channel-v1.17.0) (2023-12-07)


### Features

* Add support for python 3.12 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Introduce compatibility with native namespace packages ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Use `retry_async` instead of `retry` in async client ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.15.1...google-cloud-channel-v1.16.0) (2023-09-19)


### Features

* Launch QueryEligibleBillingAccounts API ([8de7cc7](https://github.com/googleapis/google-cloud-python/commit/8de7cc7a4ad8f2968cf432b978f5f5234f427937))
* mark ChannelPartnerGranularity as deprecated and offer alternatives ([8de7cc7](https://github.com/googleapis/google-cloud-python/commit/8de7cc7a4ad8f2968cf432b978f5f5234f427937))


### Documentation

* Add clarification for the additional_apks field of TestSetup ([8de7cc7](https://github.com/googleapis/google-cloud-python/commit/8de7cc7a4ad8f2968cf432b978f5f5234f427937))

## [1.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.15.0...google-cloud-channel-v1.15.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11445](https://github.com/googleapis/google-cloud-python/issues/11445)) ([98bddda](https://github.com/googleapis/google-cloud-python/commit/98bdddafc821e2fc6e86a31965da0c46899aa229))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-channel-v1.14.0...google-cloud-channel-v1.15.0) (2023-06-19)


### Features

* Add support for ListSkuGroups and ListSkuGroupBillableSkus APIs in Cloud Channel APIs ([#11406](https://github.com/googleapis/google-cloud-python/issues/11406)) ([7f6b607](https://github.com/googleapis/google-cloud-python/commit/7f6b60708e9c7c8ac4df9ab6d7ce292cde01ad9b))

## [1.14.0](https://github.com/googleapis/python-channel/compare/v1.13.0...v1.14.0) (2023-05-25)


### Features

* Add billing account to entitlement definitions [Cloud Channel API] ([f3a411b](https://github.com/googleapis/python-channel/commit/f3a411b74007f0abf2761f36f5626e3a54d25cc9))
* Added partition_keys field to filter results from FetchReportResults ([#235](https://github.com/googleapis/python-channel/issues/235)) ([3e304f1](https://github.com/googleapis/python-channel/commit/3e304f1e26f3be410acd08f49ae20ffe116ee761))

## [1.13.0](https://github.com/googleapis/python-channel/compare/v1.12.1...v1.13.0) (2023-03-16)


### Features

* Add ListEntitlementChanges ([da4f098](https://github.com/googleapis/python-channel/commit/da4f0983e2aed026f66190c55f52d4545eda0769))
* Add show_future_offers to ListOffers ([da4f098](https://github.com/googleapis/python-channel/commit/da4f0983e2aed026f66190c55f52d4545eda0769))

## [1.12.1](https://github.com/googleapis/python-channel/compare/v1.12.0...v1.12.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([47afb33](https://github.com/googleapis/python-channel/commit/47afb33c11627e7f051e672600e336cd844e3425))


### Documentation

* Add documentation for enums ([47afb33](https://github.com/googleapis/python-channel/commit/47afb33c11627e7f051e672600e336cd844e3425))

## [1.12.0](https://github.com/googleapis/python-channel/compare/v1.11.0...v1.12.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#220](https://github.com/googleapis/python-channel/issues/220)) ([4dc0684](https://github.com/googleapis/python-channel/commit/4dc068412363999de98c07976de2fee02c422043))

## [1.11.0](https://github.com/googleapis/python-channel/compare/v1.10.0...v1.11.0) (2022-12-15)


### Features

* Add support for `google.cloud.channel.__version__` ([0eb8ef8](https://github.com/googleapis/python-channel/commit/0eb8ef824ba7aa0d5184796272b4a0c801834293))
* Add support for granular repricing configurations via SkuGroups in Cloud Channel Repricing APIs ([#218](https://github.com/googleapis/python-channel/issues/218)) ([5dae98c](https://github.com/googleapis/python-channel/commit/5dae98ccadb18635d7fdb1a2074b0f24409ab4f4))
* Add typing to proto.Message based class attributes ([0eb8ef8](https://github.com/googleapis/python-channel/commit/0eb8ef824ba7aa0d5184796272b4a0c801834293))


### Bug Fixes

* Add dict typing for client_options ([0eb8ef8](https://github.com/googleapis/python-channel/commit/0eb8ef824ba7aa0d5184796272b4a0c801834293))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([7fb1fd0](https://github.com/googleapis/python-channel/commit/7fb1fd089fd12b9e72f4e0249b7e9cea2f41b76b))
* Drop usage of pkg_resources ([7fb1fd0](https://github.com/googleapis/python-channel/commit/7fb1fd089fd12b9e72f4e0249b7e9cea2f41b76b))
* Fix timeout default values ([7fb1fd0](https://github.com/googleapis/python-channel/commit/7fb1fd089fd12b9e72f4e0249b7e9cea2f41b76b))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([0eb8ef8](https://github.com/googleapis/python-channel/commit/0eb8ef824ba7aa0d5184796272b4a0c801834293))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([7fb1fd0](https://github.com/googleapis/python-channel/commit/7fb1fd089fd12b9e72f4e0249b7e9cea2f41b76b))

## [1.10.0](https://github.com/googleapis/python-channel/compare/v1.9.3...v1.10.0) (2022-10-18)


### Features

* Add CloudChannelReportsService to CloudChannel API ([#209](https://github.com/googleapis/python-channel/issues/209)) ([347ed65](https://github.com/googleapis/python-channel/commit/347ed657f5f83bc9b83fa14a0bc8a3fabfcd22b3))

## [1.9.3](https://github.com/googleapis/python-channel/compare/v1.9.2...v1.9.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#207](https://github.com/googleapis/python-channel/issues/207)) ([320de8f](https://github.com/googleapis/python-channel/commit/320de8fb8bd85c154b1b0aa61c49b2c651ecfecd))

## [1.9.2](https://github.com/googleapis/python-channel/compare/v1.9.1...v1.9.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#205](https://github.com/googleapis/python-channel/issues/205)) ([83cecce](https://github.com/googleapis/python-channel/commit/83ceccec1c2d54e4acab0f84ef5e0f18d0504d69))

## [1.9.1](https://github.com/googleapis/python-channel/compare/v1.9.0...v1.9.1) (2022-08-15)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#192](https://github.com/googleapis/python-channel/issues/192)) ([ec0eacd](https://github.com/googleapis/python-channel/commit/ec0eacda9545c6904a5f9e48c414619cd71a9b34))
* **deps:** require proto-plus >= 1.22.0 ([ec0eacd](https://github.com/googleapis/python-channel/commit/ec0eacda9545c6904a5f9e48c414619cd71a9b34))

## [1.9.0](https://github.com/googleapis/python-channel/compare/v1.8.1...v1.9.0) (2022-07-16)


### Features

* add audience parameter ([a0e908f](https://github.com/googleapis/python-channel/commit/a0e908fe57b97ca4123ba6dfc134f39dd2dd7b42))
* google.longrunning.Operations for Cloud Channel apis ([a0e908f](https://github.com/googleapis/python-channel/commit/a0e908fe57b97ca4123ba6dfc134f39dd2dd7b42))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#183](https://github.com/googleapis/python-channel/issues/183)) ([a0e908f](https://github.com/googleapis/python-channel/commit/a0e908fe57b97ca4123ba6dfc134f39dd2dd7b42))
* require python 3.7+ ([#185](https://github.com/googleapis/python-channel/issues/185)) ([2b2459a](https://github.com/googleapis/python-channel/commit/2b2459a739a6dcf44c87ee4428f138d7f3d01474))

## [1.8.1](https://github.com/googleapis/python-channel/compare/v1.8.0...v1.8.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#175](https://github.com/googleapis/python-channel/issues/175)) ([893ca41](https://github.com/googleapis/python-channel/commit/893ca41c4dfdf94244ffb625071574d6d5c2c198))


### Documentation

* fix changelog header to consistent size ([#176](https://github.com/googleapis/python-channel/issues/176)) ([607f171](https://github.com/googleapis/python-channel/commit/607f171fac16d7b8a374db6c66cb81cd06ef50fd))

## [1.8.0](https://github.com/googleapis/python-channel/compare/v1.7.1...v1.8.0) (2022-04-27)


### Features

* Add API definitions for Cloud Channel Repricing APIs ([#169](https://github.com/googleapis/python-channel/issues/169)) ([18db43c](https://github.com/googleapis/python-channel/commit/18db43c21a935ab9bc52539edf8f97556aa05819))
* Add filter in ListCustomersRequest ([#167](https://github.com/googleapis/python-channel/issues/167)) ([2a88151](https://github.com/googleapis/python-channel/commit/2a881514bb8ecfbcbdec9dac15663f4caa00bd00))

## [1.7.1](https://github.com/googleapis/python-channel/compare/v1.7.0...v1.7.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#149](https://github.com/googleapis/python-channel/issues/149)) ([5c2908e](https://github.com/googleapis/python-channel/commit/5c2908e5f02336d3457d9625b54c73d02745e47d))
* **deps:** require proto-plus>=1.15.0 ([5c2908e](https://github.com/googleapis/python-channel/commit/5c2908e5f02336d3457d9625b54c73d02745e47d))

## [1.7.0](https://github.com/googleapis/python-channel/compare/v1.6.3...v1.7.0) (2022-02-26)


### Features

* add api key support ([#133](https://github.com/googleapis/python-channel/issues/133)) ([df6f6d7](https://github.com/googleapis/python-channel/commit/df6f6d723d507cb332b70c343c92468b90298327))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([f57605e](https://github.com/googleapis/python-channel/commit/f57605ec93277a32f88d33967b704c45e3fc060a))


### Documentation

* clarify language for provisioning_id ([#140](https://github.com/googleapis/python-channel/issues/140)) ([a925354](https://github.com/googleapis/python-channel/commit/a925354a36a6587219a6525da100afbd36f48a68))
* Update description for ProvisionedService.provisioning_id ([#137](https://github.com/googleapis/python-channel/issues/137)) ([9b24071](https://github.com/googleapis/python-channel/commit/9b24071c8701355bf29916c0a35cc1d8f067d12e))

## [1.6.3](https://www.github.com/googleapis/python-channel/compare/v1.6.2...v1.6.3) (2021-11-13)


### Documentation

* clarify entitlement parameter `assigned_units` ([#122](https://www.github.com/googleapis/python-channel/issues/122)) ([7bb783e](https://www.github.com/googleapis/python-channel/commit/7bb783ef1ba20506f35fed649a079a7b153eddb4))

## [1.6.2](https://www.github.com/googleapis/python-channel/compare/v1.6.1...v1.6.2) (2021-11-04)


### Documentation

* clarified usage of entitlement parameters ([#116](https://www.github.com/googleapis/python-channel/issues/116)) ([20fb1ff](https://www.github.com/googleapis/python-channel/commit/20fb1ffdf922875d420266c9a761c184fe19d671))

## [1.6.1](https://www.github.com/googleapis/python-channel/compare/v1.6.0...v1.6.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([339c62c](https://www.github.com/googleapis/python-channel/commit/339c62c4a1b491bd86bb70530376b65183a2b7d4))
* **deps:** require google-api-core >= 1.28.0 ([339c62c](https://www.github.com/googleapis/python-channel/commit/339c62c4a1b491bd86bb70530376b65183a2b7d4))


### Documentation

* list oneofs in docstring ([339c62c](https://www.github.com/googleapis/python-channel/commit/339c62c4a1b491bd86bb70530376b65183a2b7d4))

## [1.6.0](https://www.github.com/googleapis/python-channel/compare/v1.5.0...v1.6.0) (2021-10-27)


### Features

* add resource type to ChannelPartnerLink ([#112](https://www.github.com/googleapis/python-channel/issues/112)) ([76433c4](https://www.github.com/googleapis/python-channel/commit/76433c4869cdbaec4c43f2a85632a9e2a272f207))

## [1.5.0](https://www.github.com/googleapis/python-channel/compare/v1.4.0...v1.5.0) (2021-10-18)


### Features

* add trove classifier for python 3.9 and python 3.10 ([#105](https://www.github.com/googleapis/python-channel/issues/105)) ([8c4eb48](https://www.github.com/googleapis/python-channel/commit/8c4eb48881d99dbc6a642a7cb771c69b2c6e6242))

## [1.4.0](https://www.github.com/googleapis/python-channel/compare/v1.3.2...v1.4.0) (2021-10-08)


### Features

* add context manager support in client ([#102](https://www.github.com/googleapis/python-channel/issues/102)) ([acf8bb2](https://www.github.com/googleapis/python-channel/commit/acf8bb2ce65cf64a9bee20362b49c207f17ffe91))

## [1.3.2](https://www.github.com/googleapis/python-channel/compare/v1.3.1...v1.3.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([dae83af](https://www.github.com/googleapis/python-channel/commit/dae83af170d1d5734ba3b1b72ffc9710adfd2a67))

## [1.3.1](https://www.github.com/googleapis/python-channel/compare/v1.3.0...v1.3.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([2e959cc](https://www.github.com/googleapis/python-channel/commit/2e959cc025ddb9677796bc87707f82132333f59d))

## [1.3.0](https://www.github.com/googleapis/python-channel/compare/v1.2.3...v1.3.0) (2021-09-23)


### Features

* add ImportCustomer ([#90](https://www.github.com/googleapis/python-channel/issues/90)) ([2bb2d89](https://www.github.com/googleapis/python-channel/commit/2bb2d8987da8a6138bef45c5fd278cb25235cfa7))

## [1.2.3](https://www.github.com/googleapis/python-channel/compare/v1.2.2...v1.2.3) (2021-08-31)


### Bug Fixes

* disable self signed jwt if users provide their own credential ([#86](https://www.github.com/googleapis/python-channel/issues/86)) ([d7c07f8](https://www.github.com/googleapis/python-channel/commit/d7c07f8d579ce55ea86520e6a7b7a268befae92d))

## [1.2.2](https://www.github.com/googleapis/python-channel/compare/v1.2.1...v1.2.2) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#76](https://www.github.com/googleapis/python-channel/issues/76)) ([016111e](https://www.github.com/googleapis/python-channel/commit/016111ee4750d047c44324bf3dca752560840376))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#72](https://www.github.com/googleapis/python-channel/issues/72)) ([b70a090](https://www.github.com/googleapis/python-channel/commit/b70a0900ab7b820e623a286cbd6f0e5c29ad9256))


### Miscellaneous Chores

* release as 1.2.2 ([#77](https://www.github.com/googleapis/python-channel/issues/77)) ([2e950a4](https://www.github.com/googleapis/python-channel/commit/2e950a41e5099facad90b884fe24f43e00b59255))

## [1.2.1](https://www.github.com/googleapis/python-channel/compare/v1.2.0...v1.2.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#71](https://www.github.com/googleapis/python-channel/issues/71)) ([36ba3c3](https://www.github.com/googleapis/python-channel/commit/36ba3c36d9ffb37c1f156fd69f7216c331f55f87))

## [1.2.0](https://www.github.com/googleapis/python-channel/compare/v1.1.1...v1.2.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#64](https://www.github.com/googleapis/python-channel/issues/64)) ([45621e5](https://www.github.com/googleapis/python-channel/commit/45621e5eabad6ff6979b89d619dcbf979ed78d63))


### Bug Fixes

* disable always_use_jwt_access ([2f8fa52](https://www.github.com/googleapis/python-channel/commit/2f8fa52e232e5468e6797d2b14166c7f319a0ca1))
* disable always_use_jwt_access ([#68](https://www.github.com/googleapis/python-channel/issues/68)) ([2f8fa52](https://www.github.com/googleapis/python-channel/commit/2f8fa52e232e5468e6797d2b14166c7f319a0ca1))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-channel/issues/1127)) ([#59](https://www.github.com/googleapis/python-channel/issues/59)) ([f358de3](https://www.github.com/googleapis/python-channel/commit/f358de3eb94fc9c870a899e3d94d93c5f14b5b0d)), closes [#1126](https://www.github.com/googleapis/python-channel/issues/1126)

## [1.1.1](https://www.github.com/googleapis/python-channel/compare/v1.1.0...v1.1.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#55](https://www.github.com/googleapis/python-channel/issues/55)) ([7747953](https://www.github.com/googleapis/python-channel/commit/7747953eb02ae952108cc9d2dcd66f939e60e115))

## [1.1.0](https://www.github.com/googleapis/python-channel/compare/v1.0.0...v1.1.0) (2021-06-10)


### Features

* Add a new enum value LICENSE_CAP_CHANGED to enum EntitlementEvent.Type. ([164539d](https://www.github.com/googleapis/python-channel/commit/164539dc0892481a739bfe4372c35be8d74480d9))
* Add a new LookupOffer RPC and LookupOfferRequest proto. ([164539d](https://www.github.com/googleapis/python-channel/commit/164539dc0892481a739bfe4372c35be8d74480d9))
* Add additional_bindings to HTTP annotations of Customer related APIs (list/create/get/update/delete). ([164539d](https://www.github.com/googleapis/python-channel/commit/164539dc0892481a739bfe4372c35be8d74480d9))
* Add/Update API definitions for Cloud Channel API ([#53](https://www.github.com/googleapis/python-channel/issues/53)) ([164539d](https://www.github.com/googleapis/python-channel/commit/164539dc0892481a739bfe4372c35be8d74480d9))
* Update descriptions of APIs. ([164539d](https://www.github.com/googleapis/python-channel/commit/164539dc0892481a739bfe4372c35be8d74480d9))

## [1.0.0](https://www.github.com/googleapis/python-channel/compare/v0.3.0...v1.0.0) (2021-06-02)


### Features

* bump release level to production/stable ([#46](https://www.github.com/googleapis/python-channel/issues/46)) ([3460f68](https://www.github.com/googleapis/python-channel/commit/3460f683a4e8f1a2f94a1eeb92af7eae1dcdb02b))


### Miscellaneous Chores

* release as 1.0.0 ([#51](https://www.github.com/googleapis/python-channel/issues/51)) ([00710b6](https://www.github.com/googleapis/python-channel/commit/00710b6566540ba111c5bb3705f892e8f743b1c2))

## [0.3.0](https://www.github.com/googleapis/python-channel/compare/v0.2.1...v0.3.0) (2021-05-28)


### Features

* support self-signed JWT flow for service accounts ([c218e2e](https://www.github.com/googleapis/python-channel/commit/c218e2efeef2f2e4cf1646644a8d4c38be021bdf))


### Bug Fixes

* add async client to %name_%version/init.py ([c218e2e](https://www.github.com/googleapis/python-channel/commit/c218e2efeef2f2e4cf1646644a8d4c38be021bdf))
* **deps:** add packaging requirement ([#43](https://www.github.com/googleapis/python-channel/issues/43)) ([e368062](https://www.github.com/googleapis/python-channel/commit/e36806211b8b3392811eb5ee1047517f840265c7))

## [0.2.1](https://www.github.com/googleapis/python-channel/compare/v0.2.0...v0.2.1) (2021-04-07)


### Bug Fixes

* BREAKING deprecate TransferableSkus fields ([#14](https://www.github.com/googleapis/python-channel/issues/14)) ([0d3b493](https://www.github.com/googleapis/python-channel/commit/0d3b4939cdae196ea9b0edc00e13f61d7d71777d))

## [0.2.0](https://www.github.com/googleapis/python-channel/compare/v0.1.0...v0.2.0) (2021-02-11)


### Features

* add Pub/Sub endpoints for Cloud Channnel API ([#9](https://www.github.com/googleapis/python-channel/issues/9)) ([2c483c8](https://www.github.com/googleapis/python-channel/commit/2c483c8ec24bba25fdea7a1f46d3d5396fe2076a))

## 0.1.0 (2021-01-14)


### Features

* generate v1 ([a95c9cf](https://www.github.com/googleapis/python-channel/commit/a95c9cf86cc9188c1e3eb8535c62367d141658cc))
