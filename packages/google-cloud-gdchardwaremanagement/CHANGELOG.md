# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-gdchardwaremanagement/#history

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.5.1...google-cloud-gdchardwaremanagement-v0.5.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.5.0...google-cloud-gdchardwaremanagement-v0.5.1) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.4.0...google-cloud-gdchardwaremanagement-v0.5.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.3.0...google-cloud-gdchardwaremanagement-v0.4.0) (2026-03-12)


### Features

* Add `OFFLINE` state to Zone resources A new `OFFLINE` state has been added to the `Zone.State` enum. This state indicates that the zone is temporarily not operational, for example, while undergoing maintenance or repair ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.2.0...google-cloud-gdchardwaremanagement-v0.3.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.13...google-cloud-gdchardwaremanagement-v0.2.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.1.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.12...google-cloud-gdchardwaremanagement-v0.1.13) (2025-08-29)


### Features

* Added CancelOrder RPC - allows Customers to request cancellation ([0db1073](https://github.com/googleapis/google-cloud-python/commit/0db1073d0c466ef00dc0bf11b196315349116584))
* Added RequestOrderDateChange RPC - allows Customers to request date changes ([0db1073](https://github.com/googleapis/google-cloud-python/commit/0db1073d0c466ef00dc0bf11b196315349116584))
* Exposed Order-level output-only fields for transparency ([0db1073](https://github.com/googleapis/google-cloud-python/commit/0db1073d0c466ef00dc0bf11b196315349116584))


### Documentation

* Mark `fulfillment_time` as deprecated ([0db1073](https://github.com/googleapis/google-cloud-python/commit/0db1073d0c466ef00dc0bf11b196315349116584))

## [0.1.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.11...google-cloud-gdchardwaremanagement-v0.1.12) (2025-04-23)


### Features

* accept status updates in the SignalZoneState method ([a66badc](https://github.com/googleapis/google-cloud-python/commit/a66badc3fd01734c6e2c4192b92cc4a0b998e8f8))
* add deployment type and installation dates to orders ([a66badc](https://github.com/googleapis/google-cloud-python/commit/a66badc3fd01734c6e2c4192b92cc4a0b998e8f8))
* expose the allowed hardware count for each SKU ([a66badc](https://github.com/googleapis/google-cloud-python/commit/a66badc3fd01734c6e2c4192b92cc4a0b998e8f8))


### Documentation

* make billing_id an output-only field ([a66badc](https://github.com/googleapis/google-cloud-python/commit/a66badc3fd01734c6e2c4192b92cc4a0b998e8f8))

## [0.1.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.10...google-cloud-gdchardwaremanagement-v0.1.11) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([e06ee32](https://github.com/googleapis/google-cloud-python/commit/e06ee325de4125cdfcaf040a77dc9ccc82843260))

## [0.1.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.9...google-cloud-gdchardwaremanagement-v0.1.10) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))
* Add support for reading selective GAPIC generation methods from service YAML ([908d742](https://github.com/googleapis/google-cloud-python/commit/908d7421a4adadd7407df7ec2a25e25688ff180f))

## [0.1.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.8...google-cloud-gdchardwaremanagement-v0.1.9) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [0.1.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.7...google-cloud-gdchardwaremanagement-v0.1.8) (2024-11-14)


### Features

* add DNS address, Kubernetes primary VLAN ID, and provisioning state to the Zone resource ([3c1e8b8](https://github.com/googleapis/google-cloud-python/commit/3c1e8b8173df97e15f247a9fbc892e29643bcb7e))
* add MAC address-associated IP address to the Hardware resource ([3c1e8b8](https://github.com/googleapis/google-cloud-python/commit/3c1e8b8173df97e15f247a9fbc892e29643bcb7e))
* add provisioning_state_signal field in SignalZoneState method request ([3c1e8b8](https://github.com/googleapis/google-cloud-python/commit/3c1e8b8173df97e15f247a9fbc892e29643bcb7e))


### Documentation

* change state_signal field in SignalZoneState method request as optional ([3c1e8b8](https://github.com/googleapis/google-cloud-python/commit/3c1e8b8173df97e15f247a9fbc892e29643bcb7e))

## [0.1.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.6...google-cloud-gdchardwaremanagement-v0.1.7) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13243](https://github.com/googleapis/google-cloud-python/issues/13243)) ([d794dec](https://github.com/googleapis/google-cloud-python/commit/d794dec5eff5f23a1ff926012bf9e6cad719e020))

## [0.1.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.5...google-cloud-gdchardwaremanagement-v0.1.6) (2024-10-28)


### Features

* add a DeleteSite method ([0846c97](https://github.com/googleapis/google-cloud-python/commit/0846c97aff11d282ea754f87d2f01870247b3ae3))
* add MAC address and disk info to the Hardware resource ([0846c97](https://github.com/googleapis/google-cloud-python/commit/0846c97aff11d282ea754f87d2f01870247b3ae3))


### Documentation

* annotate rack_location field as required; this was always enforced ([0846c97](https://github.com/googleapis/google-cloud-python/commit/0846c97aff11d282ea754f87d2f01870247b3ae3))

## [0.1.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.4...google-cloud-gdchardwaremanagement-v0.1.5) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [0.1.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.3...google-cloud-gdchardwaremanagement-v0.1.4) (2024-09-23)


### Features

* add an order type field to distinguish a fulfillment request from a sales inquiry ([e727cc0](https://github.com/googleapis/google-cloud-python/commit/e727cc0e98e37d55882215182f86c2a7d23154ef))
* add support to mark comments as read or unread ([e727cc0](https://github.com/googleapis/google-cloud-python/commit/e727cc0e98e37d55882215182f86c2a7d23154ef))
* rename zone state signal READY_FOR_SITE_TURNUP to FACTORY_TURNUP_CHECKS_PASSED ([e727cc0](https://github.com/googleapis/google-cloud-python/commit/e727cc0e98e37d55882215182f86c2a7d23154ef))


### Documentation

* clarify how access_times are used ([e727cc0](https://github.com/googleapis/google-cloud-python/commit/e727cc0e98e37d55882215182f86c2a7d23154ef))

## [0.1.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.2...google-cloud-gdchardwaremanagement-v0.1.3) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([189922a](https://github.com/googleapis/google-cloud-python/commit/189922a0fbe969dedc7b0f78a62ccb2e5d3f29a9))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.1...google-cloud-gdchardwaremanagement-v0.1.2) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gdchardwaremanagement-v0.1.0...google-cloud-gdchardwaremanagement-v0.1.1) (2024-06-27)


### Features

* add additional zone states ([a4bfef9](https://github.com/googleapis/google-cloud-python/commit/a4bfef92d5b6f30e40ef257b33748ce4b708e2ff))

## 0.1.0 (2024-06-26)


### Features

* add initial files for google.cloud.gdchardwaremanagement.v1alpha ([#12824](https://github.com/googleapis/google-cloud-python/issues/12824)) ([6c02375](https://github.com/googleapis/google-cloud-python/commit/6c02375e05dba7005ec9137ed7c5959127a9be46))

## Changelog
