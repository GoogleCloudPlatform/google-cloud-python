# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/bigquery-magics/#history

## [0.15.2](https://github.com/googleapis/google-cloud-python/compare/bigquery-magics-v0.15.1...bigquery-magics-v0.15.2) (2026-10-23)


### Features

* support Python 3.15 ([8fceef4](https://github.com/googleapis/google-cloud-python/commit/8fceef49c523bcc8989abf3b6b82bcf143332d50))


### Bug Fixes

* **bigquery-magics:** wait for graph server startup before returning from init ([#18763](https://github.com/googleapis/google-cloud-python/issues/18763)) ([77e4d66](https://github.com/googleapis/google-cloud-python/commit/77e4d661b6d060a55f1b0eb6af58f848cc5e714d))
* validate Host header in graph_server request handlers ([#17932](https://github.com/googleapis/google-cloud-python/issues/17932)) ([ea7299f](https://github.com/googleapis/google-cloud-python/commit/ea7299fe071149fe42b2ebd63f58fc97e43ad5ec))

## [0.15.1](https://github.com/googleapis/google-cloud-python/compare/bigquery-magics-v0.15.0...bigquery-magics-v0.15.1) (2026-08-06)


### Bug Fixes

* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [0.15.0](https://github.com/googleapis/google-cloud-python/compare/bigquery-magics-v0.14.0...bigquery-magics-v0.15.0) (2026-05-06)


### Bug Fixes

* Drop support for Python 3.9 (#16949) ([fab4e7123cd7f7b5d5fef3e8eb923a37d8999388](https://github.com/googleapis/google-cloud-python/commit/fab4e7123cd7f7b5d5fef3e8eb923a37d8999388))

## [0.13.0](https://github.com/googleapis/google-cloud-python/compare/bigquery-magics-v0.12.2...bigquery-magics-v0.13.0) (2026-04-09)


### Features

* drop support for Python 3.9 (#16587) ([961eacd039a2583bc019e0502bc4c1c1d88ab410](https://github.com/googleapis/google-cloud-python/commit/961eacd039a2583bc019e0502bc4c1c1d88ab410))
* deprecate `--engine=bigframes`, run `%load_ext bigframes` and use `%%bqsql` magics instead (#16573) ([dbaf8f54db13d66bc0a2311bff6085615ee38958](https://github.com/googleapis/google-cloud-python/commit/dbaf8f54db13d66bc0a2311bff6085615ee38958))

## [0.12.2](https://github.com/googleapis/google-cloud-python/compare/bigquery-magics-v0.12.1...bigquery-magics-v0.12.2) (2026-03-26)


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [0.12.1](https://github.com/googleapis/python-bigquery-magics/compare/v0.12.0...v0.12.1) (2026-02-25)


### Bug Fixes

* usability improvement to the graph visualizer (#215) ([7655ada777d16f6514040747855fd1f0e9d77b1b](https://github.com/googleapis/python-bigquery-magics/commit/7655ada777d16f6514040747855fd1f0e9d77b1b))

## [0.12.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.11.0...v0.12.0) (2026-02-10)


### Features

* support schema view (#211) ([8e1883ee553a5ca4a31c0ad3affbbfd96433a6d2](https://github.com/googleapis/python-bigquery-magics/commit/8e1883ee553a5ca4a31c0ad3affbbfd96433a6d2))
* remove bqsql magic to make that name available for bigframes (#210) ([c46c94af3a7e8d9632e2abed0198bc070a1fa2cf](https://github.com/googleapis/python-bigquery-magics/commit/c46c94af3a7e8d9632e2abed0198bc070a1fa2cf))


### Bug Fixes

* reduce conflicts between Spanner and BigQuery graph visualization on Colab (#209) ([7dca7b13164953bd07929c5313648184d44a422f](https://github.com/googleapis/python-bigquery-magics/commit/7dca7b13164953bd07929c5313648184d44a422f))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/bigquery-magics-v0.10.3...bigquery-magics-v0.11.0) (2025-12-16)


### Features

* support python 3.14 (#165) ([8ee73ecf20636eed124b80f76a364ca990acd5fe](https://github.com/googleapis/google-cloud-python/commit/8ee73ecf20636eed124b80f76a364ca990acd5fe))

## [0.10.3](https://github.com/googleapis/python-bigquery-magics/compare/v0.10.2...v0.10.3) (2025-08-21)


### Bug Fixes

* Convert property fields in graph visualization to strings before sending them to JavaScript ([#133](https://github.com/googleapis/python-bigquery-magics/issues/133)) ([f869a61](https://github.com/googleapis/python-bigquery-magics/commit/f869a61369801f1e6fee56d6dcb51b647d16df95))

## [0.10.2](https://github.com/googleapis/python-bigquery-magics/compare/v0.10.1...v0.10.2) (2025-08-04)


### Dependencies

* Drop support for Python 3.7 and 3.8 ([#127](https://github.com/googleapis/python-bigquery-magics/issues/127)) ([2a8e9de](https://github.com/googleapis/python-bigquery-magics/commit/2a8e9debe32f4f406e41072ee56bb954656af3de))
* Make graph features compatible with `spanner-graph-notebook >= 1.1.7` ([#131](https://github.com/googleapis/python-bigquery-magics/issues/131)) ([f6f6d70](https://github.com/googleapis/python-bigquery-magics/commit/f6f6d70f575113e192107dce13a0f93b853b0ad3))

## [0.10.1](https://github.com/googleapis/python-bigquery-magics/compare/v0.10.0...v0.10.1) (2025-07-07)


### Dependencies

* Move spanner-graph-notebook back to version 1.1.6 ([#126](https://github.com/googleapis/python-bigquery-magics/issues/126)) ([17ee695](https://github.com/googleapis/python-bigquery-magics/commit/17ee6956c8fec740440836609a9106e900b63074))

## [0.10.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.9.0...v0.10.0) (2025-05-16)


### Features

* Instrument vscode, jupyter and 3p plugin usage ([#115](https://github.com/googleapis/python-bigquery-magics/issues/115)) ([0dd163f](https://github.com/googleapis/python-bigquery-magics/commit/0dd163f3e5a2627e21b7d2d91ad1eefcd662b7a0))

## [0.9.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.8.1...v0.9.0) (2025-03-26)


### Features

* Add --pyformat option to use Python string formatting ([#111](https://github.com/googleapis/python-bigquery-magics/issues/111)) ([bd15a5b](https://github.com/googleapis/python-bigquery-magics/commit/bd15a5b941d14212c6bfaad84b0bc4cfd3220a0f))

## [0.8.1](https://github.com/googleapis/python-bigquery-magics/compare/v0.8.0...v0.8.1) (2025-03-21)


### Bug Fixes

* Remove setup.cfg configuration for creating universal wheels ([#106](https://github.com/googleapis/python-bigquery-magics/issues/106)) ([fe3ec29](https://github.com/googleapis/python-bigquery-magics/commit/fe3ec29fefb7ca9195484d13f2bf15c65cf20614))


### Dependencies

* Bump minimum required version of spanner-graph-notebook to 1.1.5 ([#110](https://github.com/googleapis/python-bigquery-magics/issues/110)) ([756ac0d](https://github.com/googleapis/python-bigquery-magics/commit/756ac0d0910a0622aee88ed558886456311976e9))

## [0.8.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.7.0...v0.8.0) (2025-03-13)


### Features

* Fix graph visualization to work with latest spanner-graph-notebook code; also, allow visualization when only some columns are json. ([#102](https://github.com/googleapis/python-bigquery-magics/issues/102)) ([c33297c](https://github.com/googleapis/python-bigquery-magics/commit/c33297cf2a1db9a0bd2e8c078be1e06239122459))
* Support multiple columns in graph visualization ([#100](https://github.com/googleapis/python-bigquery-magics/issues/100)) ([dbb6442](https://github.com/googleapis/python-bigquery-magics/commit/dbb64426dd617697785bccf15d98c32f8217c33e))

## [0.7.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.6.0...v0.7.0) (2025-03-11)


### Features

* Support visualization of graph queries by adding the --graph argument. ([#94](https://github.com/googleapis/python-bigquery-magics/issues/94)) ([3c054f5](https://github.com/googleapis/python-bigquery-magics/commit/3c054f5e27b5097c18899ff732fccebdf36b47e6))


### Bug Fixes

* Resolve issue where pre-release versions of dependencies are installed ([#97](https://github.com/googleapis/python-bigquery-magics/issues/97)) ([79c59e7](https://github.com/googleapis/python-bigquery-magics/commit/79c59e7b8ceba6f2be1fbe16d12b69b5a0b4d774))

## [0.6.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.5.0...v0.6.0) (2025-02-12)


### Features

* Add '--use-geodataframe' argument to return a GeoDataFrame ([#91](https://github.com/googleapis/python-bigquery-magics/issues/91)) ([fc04f34](https://github.com/googleapis/python-bigquery-magics/commit/fc04f343d0e9c5c6b11e784d698c28865c2909cd))
* Add an is_registered global value to indicate whether the extension has been loaded ([#83](https://github.com/googleapis/python-bigquery-magics/issues/83)) ([0bc4473](https://github.com/googleapis/python-bigquery-magics/commit/0bc4473d550c612241ea1428f7538938257b2656))

## [0.5.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.4.0...v0.5.0) (2024-12-17)


### Features

* Add `%%bqsql` as an alias to the `%%bigquery` magic ([#72](https://github.com/googleapis/python-bigquery-magics/issues/72)) ([03fe1d5](https://github.com/googleapis/python-bigquery-magics/commit/03fe1d544ef22865c07c680873f980c64bbc7abc))
* Add `bigquery_magics.context.default_variable` option ([#70](https://github.com/googleapis/python-bigquery-magics/issues/70)) ([72ed882](https://github.com/googleapis/python-bigquery-magics/commit/72ed882c9359718a702bab2bca76933548650064))

## [0.4.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.3.0...v0.4.0) (2024-09-24)


### Features

* Add support for overriding `context.engine` by magic argument ([#60](https://github.com/googleapis/python-bigquery-magics/issues/60)) ([ff57f14](https://github.com/googleapis/python-bigquery-magics/commit/ff57f14aa43c60ffc02b8966da2405c31ea42c64))

## [0.3.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.2.0...v0.3.0) (2024-09-20)


### Features

* Add support for BigQuery DataFrames. Set `context.engine` to 'bigframes' to support query results larger than 10 GB ([#58](https://github.com/googleapis/python-bigquery-magics/issues/58)) ([90ba05f](https://github.com/googleapis/python-bigquery-magics/commit/90ba05f3d918979788e01b0cd3201ac8f01741a9))

## [0.2.0](https://github.com/googleapis/python-bigquery-magics/compare/v0.1.1...v0.2.0) (2024-08-27)


### Features

* Depend on pydata-google-auth to fetch credentials ([#49](https://github.com/googleapis/python-bigquery-magics/issues/49)) ([8db23fc](https://github.com/googleapis/python-bigquery-magics/commit/8db23fc60624baae9c0dffd500d8856cb6e92f42))

## [0.1.1](https://github.com/googleapis/python-bigquery-magics/compare/v0.1.0...v0.1.1) (2024-08-22)


### Dependencies

* Depend on ipykernel 5.5.6+ instead of 6.0+ ([83d8fac](https://github.com/googleapis/python-bigquery-magics/commit/83d8facf6d04752c1f8c5e25575a3975c9b30e1c))


### Documentation

* Correct links to project pages in README ([#33](https://github.com/googleapis/python-bigquery-magics/issues/33)) ([ace5020](https://github.com/googleapis/python-bigquery-magics/commit/ace5020ff8ae374145579e75cb996150680f2bde))
* Update the IPython Magics docs ([#27](https://github.com/googleapis/python-bigquery-magics/issues/27)) ([62e88b3](https://github.com/googleapis/python-bigquery-magics/commit/62e88b3f4a595ecdc4a00d661b956c5d50fd6c35))

## 0.1.0 (2024-04-25)


### Features

* Initial copy from google-cloud-bigquery ([4a69d26](https://github.com/googleapis/python-bigquery-magics/commit/4a69d26ae3e5e7c659c7b79ac935393abb4146e3))


### Documentation

* Clean up docs and let the nox pass ([#24](https://github.com/googleapis/python-bigquery-magics/issues/24)) ([275712f](https://github.com/googleapis/python-bigquery-magics/commit/275712f4e4b647cda2d253e1f6b7a2fa093ee7c1))
* Reset the changelog for the new package ([#22](https://github.com/googleapis/python-bigquery-magics/issues/22)) ([f7d9c14](https://github.com/googleapis/python-bigquery-magics/commit/f7d9c1445feac32e468a3e06ca55c9474a1ae548))
