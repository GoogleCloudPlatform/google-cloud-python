# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-maps-routing/#history

## [0.11.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.11.1...google-maps-routing-v0.11.2) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.11.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.11.0...google-maps-routing-v0.11.1) (2026-09-03)


### Features

* update googleapis and regenerate ([#18229](https://github.com/googleapis/google-cloud-python/issues/18229)) ([d4f8a57](https://github.com/googleapis/google-cloud-python/commit/d4f8a57abadd282ad95472e77daa59d8fb98cbcf))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.10.0...google-maps-routing-v0.11.0) (2026-06-02)


### Features

* regenerate google-maps packages (#17073) ([bd31a8c7fd338723ac201ad1b5d0f2a1861f8925](https://github.com/googleapis/google-cloud-python/commit/bd31a8c7fd338723ac201ad1b5d0f2a1861f8925))

## [0.10.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.9.0...google-maps-routing-v0.10.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.8.0...google-maps-routing-v0.9.0) (2026-03-12)


### Documentation

* regenerated documentation for fields ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))


### Features

* add a new Waypoint source to accept a token that identifies a Navigation Point obtained from the `SearchDestinations` method of the Geocoding API ([505bc9725fec0b2238a1fc102967f68027f9afdf](https://github.com/googleapis/google-cloud-python/commit/505bc9725fec0b2238a1fc102967f68027f9afdf))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.7.0...google-maps-routing-v0.8.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.16...google-maps-routing-v0.7.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.6.16](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.15...google-maps-routing-v0.6.16) (2025-06-11)


### Documentation

* Update import statement example in README ([8066d24](https://github.com/googleapis/google-cloud-python/commit/8066d24068e6d036dcf77e7abb5401a5ba3f8a63))

## [0.6.15](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.14...google-maps-routing-v0.6.15) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([25ced24](https://github.com/googleapis/google-cloud-python/commit/25ced2444528a1dc6a22daa32b82b844961f1b75))

## [0.6.14](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.13...google-maps-routing-v0.6.14) (2025-02-18)


### Features

* Add REST Interceptors which support reading metadata ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))
* Add support for reading selective GAPIC generation methods from service YAML ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))

## [0.6.13](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.12...google-maps-routing-v0.6.13) (2024-12-12)


### Features

* [google-maps-routing] add API for shorter distance reference routes ([#13306](https://github.com/googleapis/google-cloud-python/issues/13306)) ([104d44d](https://github.com/googleapis/google-cloud-python/commit/104d44d5886a32bc61483d8d25d2557aee1dd5a6))
* [Many APIs] Add support for opt-in debug logging ([#13349](https://github.com/googleapis/google-cloud-python/issues/13349)) ([8b9c7bf](https://github.com/googleapis/google-cloud-python/commit/8b9c7bf3bb1c4f0beabd71a45c469fcedb19a2c8))
* add API for experimental flyover and narrow road polyline details ([eb4c7f9](https://github.com/googleapis/google-cloud-python/commit/eb4c7f9f785f5433191efac7e21a7d2ccc2d28bc))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([8b9c7bf](https://github.com/googleapis/google-cloud-python/commit/8b9c7bf3bb1c4f0beabd71a45c469fcedb19a2c8))

## [0.6.12](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.11...google-maps-routing-v0.6.12) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13247](https://github.com/googleapis/google-cloud-python/issues/13247)) ([5adc8b7](https://github.com/googleapis/google-cloud-python/commit/5adc8b7d2cc8ab9707ab5a65f15270c125cee051))

## [0.6.11](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.10...google-maps-routing-v0.6.11) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13211](https://github.com/googleapis/google-cloud-python/issues/13211)) ([f712162](https://github.com/googleapis/google-cloud-python/commit/f712162c01f065da29fffbbed1e856a1f3876b1b))

## [0.6.10](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.9...google-maps-routing-v0.6.10) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([4adddf4](https://github.com/googleapis/google-cloud-python/commit/4adddf4d90634e454ee006774bfc631fc12c1700))

## [0.6.9](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.8...google-maps-routing-v0.6.9) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12871](https://github.com/googleapis/google-cloud-python/issues/12871)) ([73b35d5](https://github.com/googleapis/google-cloud-python/commit/73b35d56f8626d99ce7c3902a8c223cc09b4ca74))

## [0.6.8](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.7...google-maps-routing-v0.6.8) (2024-04-15)


### Features

* adds support for new toll passes ([30cf437](https://github.com/googleapis/google-cloud-python/commit/30cf4373474e0f753aaecf419110b7f67a3cb386))
* adds support for specifying units in the ComputeRouteMatrix request ([30cf437](https://github.com/googleapis/google-cloud-python/commit/30cf4373474e0f753aaecf419110b7f67a3cb386))


### Documentation

* various formatting and grammar fixes for proto documentation ([30cf437](https://github.com/googleapis/google-cloud-python/commit/30cf4373474e0f753aaecf419110b7f67a3cb386))

## [0.6.7](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.6...google-maps-routing-v0.6.7) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12389](https://github.com/googleapis/google-cloud-python/issues/12389)) ([5db9352](https://github.com/googleapis/google-cloud-python/commit/5db93528a1ad20825d4d12dcf5fdf9624879f2ce))

## [0.6.6](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.5...google-maps-routing-v0.6.6) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12311](https://github.com/googleapis/google-cloud-python/issues/12311)) ([e4c864b](https://github.com/googleapis/google-cloud-python/commit/e4c864b3e67c7f7f33dfb0d2107fa138492ad338))
* fix ValueError in test__validate_universe_domain ([f3974d4](https://github.com/googleapis/google-cloud-python/commit/f3974d46a9ba9f549e31251ebc2daeb6b9b4745a))

## [0.6.5](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.4...google-maps-routing-v0.6.5) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))

## [0.6.4](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.3...google-maps-routing-v0.6.4) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12244](https://github.com/googleapis/google-cloud-python/issues/12244)) ([8d6b772](https://github.com/googleapis/google-cloud-python/commit/8d6b7729d93c1347529a3d34ed6266af55225578))

## [0.6.3](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.2...google-maps-routing-v0.6.3) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.1...google-maps-routing-v0.6.2) (2023-09-19)


### Documentation

* Minor formatting ([77bf61a](https://github.com/googleapis/google-cloud-python/commit/77bf61a36539bc2e6317dca1f954189d5241e4f1))

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.0...google-maps-routing-v0.6.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11450](https://github.com/googleapis/google-cloud-python/issues/11450)) ([bf58f57](https://github.com/googleapis/google-cloud-python/commit/bf58f5787dbc694e5bbe8fb48a1ede9e0089d26a))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.5.1...google-maps-routing-v0.6.0) (2023-06-29)


### Features

* Add HTML Navigation Instructions feature to ComputeRoutes ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add more navigation instruction maneuvers ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add more toll pass values ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add TrafficModel feature in ComputeRoutes and ComputeRouteMatrix ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add Waypoint Optimization feature to ComputeRoutes ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Support returning localized values in ComputeRoutes and ComputeRouteMatrix ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Support Transit routes in ComputeRoutes and ComputeRouteMatrix ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.5.0...google-maps-routing-v0.5.1) (2023-06-03)


### Documentation

* fix broken client library documentation links ([#11192](https://github.com/googleapis/google-cloud-python/issues/11192)) ([5e17f7a](https://github.com/googleapis/google-cloud-python/commit/5e17f7a901bbbae8ff9a44ed62f1abd2386da2c8))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.4.0...google-maps-routing-v0.5.0) (2023-03-25)


### Features

* Add support for specifying region_code and language_code in the ComputeRouteMatrixRequest ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Add support for specifying region_code in the ComputeRoutesRequest ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Add support for specifying waypoints as addresses ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))


### Documentation

* Clarify usage of compute_alternative_routes in proto comment ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Clarify usage of RouteLegStepTravelAdvisory in comment ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Update proto comments to contain concrete references to other proto messages ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.3.1...google-maps-routing-v0.4.0) (2023-02-09)


### Features

* enable "rest" transport in Python for services supporting numeric enums ([#10839](https://github.com/googleapis/google-cloud-python/issues/10839)) ([ad59d56](https://github.com/googleapis/google-cloud-python/commit/ad59d569bda339ed31500602e2db369afdbfcf0b))

## [0.3.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.3.0...google-maps-routing-v0.3.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))


### Documentation

* Add documentation for enums ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.2.0...google-maps-routing-v0.3.0) (2023-01-19)


### Features

* Add ExtraComputations feature to ComputeRoutes and ComputeRouteMatrix ([#10820](https://github.com/googleapis/google-cloud-python/issues/10820)) ([1812a88](https://github.com/googleapis/google-cloud-python/commit/1812a8860f4aa21fc1afaf8d37c8486010fa3984))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.1.2...google-maps-routing-v0.2.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#10812](https://github.com/googleapis/google-cloud-python/issues/10812)) ([e5f88ee](https://github.com/googleapis/google-cloud-python/commit/e5f88eebd47c677850d61ddc3774532723f5505e))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.1.1...google-maps-routing-v0.1.2) (2022-12-14)


### Documentation

* updated comment for ComputeRoutesRequest and ComputeRouteMatrixRequest ([2d9d62b](https://github.com/googleapis/google-cloud-python/commit/2d9d62b948c985cd0afac7bea0447f57e4b6ab69))
* updated comment for Route.route_token ([2d9d62b](https://github.com/googleapis/google-cloud-python/commit/2d9d62b948c985cd0afac7bea0447f57e4b6ab69))
* updated comment for RouteTravelMode ([2d9d62b](https://github.com/googleapis/google-cloud-python/commit/2d9d62b948c985cd0afac7bea0447f57e4b6ab69))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.1.0...google-maps-routing-v0.1.1) (2022-12-06)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))
* Drop usage of pkg_resources ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))
* Fix timeout default values ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))

## 0.1.0 (2022-11-10)


### Features

* add initial files for google.maps.routing.v2 ([#10770](https://github.com/googleapis/google-cloud-python/issues/10770)) ([42e0e59](https://github.com/googleapis/google-cloud-python/commit/42e0e594a8dd2ff06abc92111b537ee9271046e5))
* Add typing to proto.Message based class attributes ([a6cbc16](https://github.com/googleapis/google-cloud-python/commit/a6cbc167835880f9fe31b4030ec5fba69e35b383))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([a6cbc16](https://github.com/googleapis/google-cloud-python/commit/a6cbc167835880f9fe31b4030ec5fba69e35b383))

## Changelog
