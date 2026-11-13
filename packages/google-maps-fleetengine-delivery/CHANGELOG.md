# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-maps-fleetengine-delivery/#history

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.6.0...google-maps-fleetengine-delivery-v0.6.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.5.0...google-maps-fleetengine-delivery-v0.6.0) (2026-06-02)


### Features

* regenerate google-maps packages (#17073) ([bd31a8c7fd338723ac201ad1b5d0f2a1861f8925](https://github.com/googleapis/google-cloud-python/commit/bd31a8c7fd338723ac201ad1b5d0f2a1861f8925))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.4.0...google-maps-fleetengine-delivery-v0.5.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.3.0...google-maps-fleetengine-delivery-v0.4.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.13...google-maps-fleetengine-delivery-v0.3.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.2.13](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.12...google-maps-fleetengine-delivery-v0.2.13) (2025-07-10)


### Features

* [google-maps-fleetengine-delivery] add ability to specify trip attributes to Trip and deprecate Trip.remaining_waypoints_version ([#14071](https://github.com/googleapis/google-cloud-python/issues/14071)) ([5430901](https://github.com/googleapis/google-cloud-python/commit/54309016fb30031824033754687a515891c71697))

## [0.2.12](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.11...google-maps-fleetengine-delivery-v0.2.12) (2025-06-11)


### Documentation

* Update import statement example in README ([8066d24](https://github.com/googleapis/google-cloud-python/commit/8066d24068e6d036dcf77e7abb5401a5ba3f8a63))

## [0.2.11](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.10...google-maps-fleetengine-delivery-v0.2.11) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([25ced24](https://github.com/googleapis/google-cloud-python/commit/25ced2444528a1dc6a22daa32b82b844961f1b75))

## [0.2.10](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.9...google-maps-fleetengine-delivery-v0.2.10) (2025-03-03)


### Features

* [google-maps-fleetengine-delivery] Added Fleet Engine Delete APIs ([a2c1c9a](https://github.com/googleapis/google-cloud-python/commit/a2c1c9aedc2e363df88f7b8b6e8e7a2ea6856365))
* [google-maps-fleetengine-delivery] Added Fleet Engine Delete APIs ([#13568](https://github.com/googleapis/google-cloud-python/issues/13568)) ([a2c1c9a](https://github.com/googleapis/google-cloud-python/commit/a2c1c9aedc2e363df88f7b8b6e8e7a2ea6856365))

## [0.2.9](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.8...google-maps-fleetengine-delivery-v0.2.9) (2025-02-27)


### Features

* A new field `past_locations` is added to message `.maps.fleetengine.delivery.v1.DeliveryVehicle` ([bc69299](https://github.com/googleapis/google-cloud-python/commit/bc69299c381dbae1f24315af8b46f70ddc6b9269))


### Documentation

* Updated documentation for field `task` in message `.maps.fleetengine.delivery.v1.CreateTaskRequest` to clarify certain fields can be optionally set. ([bc69299](https://github.com/googleapis/google-cloud-python/commit/bc69299c381dbae1f24315af8b46f70ddc6b9269))

## [0.2.8](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.7...google-maps-fleetengine-delivery-v0.2.8) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))
* Add support for reading selective GAPIC generation methods from service YAML ([5cdcc9d](https://github.com/googleapis/google-cloud-python/commit/5cdcc9d9d3e259c9a743895940552eb75b4554d3))

## [0.2.7](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.6...google-maps-fleetengine-delivery-v0.2.7) (2024-12-12)


### Features

* Add support for opt-in debug logging ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([cf4d0e0](https://github.com/googleapis/google-cloud-python/commit/cf4d0e0ddd6d9d8808bde59d8b62acb4ff7f1750))

## [0.2.6](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.5...google-maps-fleetengine-delivery-v0.2.6) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13247](https://github.com/googleapis/google-cloud-python/issues/13247)) ([5adc8b7](https://github.com/googleapis/google-cloud-python/commit/5adc8b7d2cc8ab9707ab5a65f15270c125cee051))

## [0.2.5](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.4...google-maps-fleetengine-delivery-v0.2.5) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13211](https://github.com/googleapis/google-cloud-python/issues/13211)) ([f712162](https://github.com/googleapis/google-cloud-python/commit/f712162c01f065da29fffbbed1e856a1f3876b1b))

## [0.2.4](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.3...google-maps-fleetengine-delivery-v0.2.4) (2024-09-06)


### Documentation

* [google-maps-fleetengine-delivery] update comment link for ListTasks filter ([#13066](https://github.com/googleapis/google-cloud-python/issues/13066)) ([a7f0dbf](https://github.com/googleapis/google-cloud-python/commit/a7f0dbfb8a5f3518cf1acec86b7bc3a6151a811b))

## [0.2.3](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.2...google-maps-fleetengine-delivery-v0.2.3) (2024-07-30)


### Documentation

* [google-maps-fleetengine-delivery] document that delivery_vehicle.type can be set on CreateDeliveryVehicle ([#12959](https://github.com/googleapis/google-cloud-python/issues/12959)) ([895cbec](https://github.com/googleapis/google-cloud-python/commit/895cbec764f18fd5b775e0544d1eb0ac9506acab))

## [0.2.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.1...google-maps-fleetengine-delivery-v0.2.2) (2024-07-11)


### Documentation

* [google-maps-fleetengine-delivery] clarify behavior of UpdateDeliveryVehicle ([#12896](https://github.com/googleapis/google-cloud-python/issues/12896)) ([a19cfa8](https://github.com/googleapis/google-cloud-python/commit/a19cfa832866bdec91a195da49ede602db071239))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.2.0...google-maps-fleetengine-delivery-v0.2.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12871](https://github.com/googleapis/google-cloud-python/issues/12871)) ([73b35d5](https://github.com/googleapis/google-cloud-python/commit/73b35d56f8626d99ce7c3902a8c223cc09b4ca74))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.8...google-maps-fleetengine-delivery-v0.2.0) (2024-05-16)


### ⚠ BREAKING CHANGES

* An existing method `SearchFuzzedVehicles` is removed from service `VehicleService`
* An existing message `UpdateVehicleLocationRequest` is removed
* An existing method `UpdateVehicleLocation` is removed from service `VehicleService`

### Bug Fixes

* An existing message `UpdateVehicleLocationRequest` is removed ([6c696a2](https://github.com/googleapis/google-cloud-python/commit/6c696a2f789777ed7ecdd0cf0af5dc2a6fc97d73))
* An existing method `SearchFuzzedVehicles` is removed from service `VehicleService` ([6c696a2](https://github.com/googleapis/google-cloud-python/commit/6c696a2f789777ed7ecdd0cf0af5dc2a6fc97d73))
* An existing method `UpdateVehicleLocation` is removed from service `VehicleService` ([6c696a2](https://github.com/googleapis/google-cloud-python/commit/6c696a2f789777ed7ecdd0cf0af5dc2a6fc97d73))


### Documentation

* remove comment about deleted SearchTasks method ([11fb7ce](https://github.com/googleapis/google-cloud-python/commit/11fb7cee853fde7e87a1856325f9b756e5106b33))

## [0.1.8](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.7...google-maps-fleetengine-delivery-v0.1.8) (2024-05-07)


### Documentation

* correct link in ListTasks documentation ([0f94060](https://github.com/googleapis/google-cloud-python/commit/0f94060679ef8aba9b696077dbc453de8c1646bd))

## [0.1.7](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.6...google-maps-fleetengine-delivery-v0.1.7) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12389](https://github.com/googleapis/google-cloud-python/issues/12389)) ([5db9352](https://github.com/googleapis/google-cloud-python/commit/5db93528a1ad20825d4d12dcf5fdf9624879f2ce))

## [0.1.6](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.5...google-maps-fleetengine-delivery-v0.1.6) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12311](https://github.com/googleapis/google-cloud-python/issues/12311)) ([e4c864b](https://github.com/googleapis/google-cloud-python/commit/e4c864b3e67c7f7f33dfb0d2107fa138492ad338))
* fix ValueError in test__validate_universe_domain ([f3974d4](https://github.com/googleapis/google-cloud-python/commit/f3974d46a9ba9f549e31251ebc2daeb6b9b4745a))


### Documentation

* [google-maps-fleetengine-delivery] updated incorrect reference to `Task.journeySharingInfo` ([#12322](https://github.com/googleapis/google-cloud-python/issues/12322)) ([ef9152e](https://github.com/googleapis/google-cloud-python/commit/ef9152e4bb385976d8af743566ea02ed224901d0))

## [0.1.5](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.4...google-maps-fleetengine-delivery-v0.1.5) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))

## [0.1.4](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.3...google-maps-fleetengine-delivery-v0.1.4) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12244](https://github.com/googleapis/google-cloud-python/issues/12244)) ([8d6b772](https://github.com/googleapis/google-cloud-python/commit/8d6b7729d93c1347529a3d34ed6266af55225578))

## [0.1.3](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.2...google-maps-fleetengine-delivery-v0.1.3) (2023-12-13)


### Features

* [google-maps-fleetengine-delivery] add trace_id to Fleet Engine headers ([#12120](https://github.com/googleapis/google-cloud-python/issues/12120)) ([94238c8](https://github.com/googleapis/google-cloud-python/commit/94238c863b1806cc50d65431c425ef90dbd6ced7))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.1...google-maps-fleetengine-delivery-v0.1.2) (2023-12-07)


### Features

* Add support for python 3.12 ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))
* Introduce compatibility with native namespace packages ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))
* Use `retry_async` instead of `retry` in async client ([f920d22](https://github.com/googleapis/google-cloud-python/commit/f920d22f59fbd31822252b9677416a6cd436eba2))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-fleetengine-delivery-v0.1.0...google-maps-fleetengine-delivery-v0.1.1) (2023-11-02)


### Features

* add default sensors for RawLocation & SupplementalLocation ([#11934](https://github.com/googleapis/google-cloud-python/issues/11934)) ([c503005](https://github.com/googleapis/google-cloud-python/commit/c503005e2cfe25cc96625506991d60ade327e213))

## 0.1.0 (2023-10-19)


### Features

* add initial files for google.maps.fleetengine.delivery.v1 ([#11814](https://github.com/googleapis/google-cloud-python/issues/11814)) ([9b403f4](https://github.com/googleapis/google-cloud-python/commit/9b403f450daebc7ab92770446769e4fc547152ba))

## Changelog
