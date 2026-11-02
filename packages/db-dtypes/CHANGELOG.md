# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/db-dtypes/#history

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.8.0...db-dtypes-v1.9.0) (2026-10-22)


### Features

* support Python 3.15 ([8fceef4](https://github.com/googleapis/google-cloud-python/commit/8fceef49c523bcc8989abf3b6b82bcf143332d50))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.7.2...db-dtypes-v1.8.0) (2026-10-15)


### Features

* **db-dtypes:** support pandas 3.1 ([#18590](https://github.com/googleapis/google-cloud-python/issues/18590)) ([f18a11e](https://github.com/googleapis/google-cloud-python/commit/f18a11eb4308b9a8889166ea3c1246fb8306a906))

## [1.7.2](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.7.1...db-dtypes-v1.7.2) (2026-10-01)


### Bug Fixes

* **ci:** fix docfx and db-dtypes pandas compat ([#18512](https://github.com/googleapis/google-cloud-python/issues/18512)) ([5d57b25](https://github.com/googleapis/google-cloud-python/commit/5d57b255271ed43274286cb65a9f6e52ee56875a))
* **db-dtypes:** support updated pandas datetime reduction error message ([#18526](https://github.com/googleapis/google-cloud-python/issues/18526)) ([04ef51e](https://github.com/googleapis/google-cloud-python/commit/04ef51e31698462229c1269ad01d7ae06d9a7bb7))

## [1.7.1](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.7.0...db-dtypes-v1.7.1) (2026-07-07)


### Bug Fixes

* avoid deprecated unitless operations for NumPy 2.5 compatibility ([#17589](https://github.com/googleapis/google-cloud-python/issues/17589)) ([d0b2abc](https://github.com/googleapis/google-cloud-python/commit/d0b2abc2aef8d95402c026cccbc866d812b819b8))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.6.0...db-dtypes-v1.7.0) (2026-06-02)


### Features

* support pandas 3.0 (#17177) ([2086b34d8b3418462c9bc89b96eac779a25a3afd](https://github.com/googleapis/google-cloud-python/commit/2086b34d8b3418462c9bc89b96eac779a25a3afd))


### Bug Fixes

* bump pyarrow from 13.0.0 to 14.0.1 in /packages/db-dtypes (#17182) ([49252da0f81c63ff7bc384dc3ddd92608e15f459](https://github.com/googleapis/google-cloud-python/commit/49252da0f81c63ff7bc384dc3ddd92608e15f459))
* Drop support for Python <= 3.9 (#16966) ([66988617e67e9c923d8bcbd4034505ec9a20968f](https://github.com/googleapis/google-cloud-python/commit/66988617e67e9c923d8bcbd4034505ec9a20968f))

## [1.6.0](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.5.1...db-dtypes-v1.6.0) (2026-05-06)


### Features

* enable mypy session for db-dtypes (#16689) ([856731e10a7e8b7531a08f8f799d0321e2fc167d](https://github.com/googleapis/google-cloud-python/commit/856731e10a7e8b7531a08f8f799d0321e2fc167d))

## [1.5.1](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.5.0...db-dtypes-v1.5.1) (2026-03-26)


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [1.5.0](https://github.com/googleapis/google-cloud-python/compare/db-dtypes-v1.4.3...db-dtypes-v1.5.0) (2025-12-15)


### Features

* Add support for Python 3.14 (#380) ([c164a47be909203606cf982d6f0becc6c8efdb09](https://github.com/googleapis/google-cloud-python/commit/c164a47be909203606cf982d6f0becc6c8efdb09))

## [1.4.4](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.4.3...v1.4.4) (2025-09-08)


### Dependencies

* Adds limits to numpy installs under 3.10 for dataproc ([#370](https://github.com/googleapis/python-db-dtypes-pandas/issues/370)) ([6d79280](https://github.com/googleapis/python-db-dtypes-pandas/commit/6d79280f54b662accd80a571412ac0fcae206abb))

## [1.4.3](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.4.2...v1.4.3) (2025-05-12)


### Bug Fixes

* Remove setup.cfg configuration for creating universal wheels ([#333](https://github.com/googleapis/python-db-dtypes-pandas/issues/333)) ([44a5aa2](https://github.com/googleapis/python-db-dtypes-pandas/commit/44a5aa24ef3219849e9e0bedeeaebc4b9ee53d9e))
* Updates noxfile with pip freeze and pandas 1.2 ([#331](https://github.com/googleapis/python-db-dtypes-pandas/issues/331)) ([5eb2a85](https://github.com/googleapis/python-db-dtypes-pandas/commit/5eb2a85acc8292e00eea994e5e5ab54d7d037fda))


### Dependencies

* Drop support for Python 3.7 and 3.8 ([66f3f0b](https://github.com/googleapis/python-db-dtypes-pandas/commit/66f3f0bed9ed0aa317519f039e8623b0715af38e))
* Updates deprecation warning to FutureWarning re: 3.7 and 3.8 ([#338](https://github.com/googleapis/python-db-dtypes-pandas/issues/338)) ([158243b](https://github.com/googleapis/python-db-dtypes-pandas/commit/158243b2e039db108cec3fa395d3391161042c4e))

## [1.4.2](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.4.1...v1.4.2) (2025-03-04)


### Bug Fixes

* Remove unbox json functionality from JSONArrowType ([#325](https://github.com/googleapis/python-db-dtypes-pandas/issues/325)) ([60deef1](https://github.com/googleapis/python-db-dtypes-pandas/commit/60deef1636ba3e4f88725db8b9ce23b634168ac2))

## [1.4.1](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.4.0...v1.4.1) (2025-01-30)


### Bug Fixes

* Re-add ModuleNotFoundError handler for pandas_backports ([#319](https://github.com/googleapis/python-db-dtypes-pandas/issues/319)) ([931ff8a](https://github.com/googleapis/python-db-dtypes-pandas/commit/931ff8a0f15fb376f77954affb48d1c953094dee))

## [1.4.0](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.3.1...v1.4.0) (2025-01-21)


### Features

* Add __hash__ property for JSONArrowType ([#316](https://github.com/googleapis/python-db-dtypes-pandas/issues/316)) ([7073e37](https://github.com/googleapis/python-db-dtypes-pandas/commit/7073e37d1fe76c2078550a8c7f0e45e3fad26809))
* Add Arrow types for efficient JSON data representation in pyarrow ([#312](https://github.com/googleapis/python-db-dtypes-pandas/issues/312)) ([d9992fc](https://github.com/googleapis/python-db-dtypes-pandas/commit/d9992fc6120351cb8ccb2dd86bd57e8097004285))

## [1.3.1](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.3.0...v1.3.1) (2024-11-12)


### Bug Fixes

* Dbjson serialization with most compact JSON representation ([#299](https://github.com/googleapis/python-db-dtypes-pandas/issues/299)) ([c5e9a10](https://github.com/googleapis/python-db-dtypes-pandas/commit/c5e9a101022844e735099d5f2c645ce0cc46f7f8))
* Support correct numpy construction for dbjson dtype in pandas 1.5 ([#297](https://github.com/googleapis/python-db-dtypes-pandas/issues/297)) ([f413f35](https://github.com/googleapis/python-db-dtypes-pandas/commit/f413f3527941fe52af7e19e2954a936bb3de8394))
* Support dbjson type on pandas version 1.5 ([#295](https://github.com/googleapis/python-db-dtypes-pandas/issues/295)) ([4b84e4a](https://github.com/googleapis/python-db-dtypes-pandas/commit/4b84e4a6fada5ecfa7f910dca61e6de714abdb9d))

## [1.3.0](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.2.0...v1.3.0) (2024-08-08)


### Features

* Create db_dtypes JSONDtype and JSONArray ([#284](https://github.com/googleapis/python-db-dtypes-pandas/issues/284)) ([76790a8](https://github.com/googleapis/python-db-dtypes-pandas/commit/76790a8c67ae8fa9687a4e6a6f950b15e6f34c6f))


### Documentation

* Add summary_overview template ([#264](https://github.com/googleapis/python-db-dtypes-pandas/issues/264)) ([a97c341](https://github.com/googleapis/python-db-dtypes-pandas/commit/a97c34198cbed37c8ff8ea683d485ebe36b804d7))

## [1.2.0](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.1.1...v1.2.0) (2023-12-10)


### Features

* Add support for Python 3.12 ([#223](https://github.com/googleapis/python-db-dtypes-pandas/issues/223)) ([1338425](https://github.com/googleapis/python-db-dtypes-pandas/commit/1338425ad765be4613bcf3fcfa7f6ce964de04a3))


### Bug Fixes

* Adds xfail marks to tests that are known to fail ([#189](https://github.com/googleapis/python-db-dtypes-pandas/issues/189)) ([4a56b76](https://github.com/googleapis/python-db-dtypes-pandas/commit/4a56b766b0ccba900a555167863f1081a76c4c0d))


### Documentation

* Update pandas extension link ([#210](https://github.com/googleapis/python-db-dtypes-pandas/issues/210)) ([668988f](https://github.com/googleapis/python-db-dtypes-pandas/commit/668988f0f1c25a9d50a7ad5523933e42553b5210))

## [1.1.1](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.1.0...v1.1.1) (2023-03-30)


### Bug Fixes

* Out-of-bounds datetime.date raises OutOfBoundsDatetime ([#180](https://github.com/googleapis/python-db-dtypes-pandas/issues/180)) ([4f3399e](https://github.com/googleapis/python-db-dtypes-pandas/commit/4f3399e3103c8ad8063b047c7718bcb5621038ca))

## [1.1.0](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.0.5...v1.1.0) (2023-03-29)


### Features

* Support pandas 2.0 release candidate ([#179](https://github.com/googleapis/python-db-dtypes-pandas/issues/179)) ([daa6852](https://github.com/googleapis/python-db-dtypes-pandas/commit/daa685234d283bc2f3c87a6127fd734d8a037ad6))


### Bug Fixes

* Adds bounds checking because pandas now handles microsecond reso… ([#166](https://github.com/googleapis/python-db-dtypes-pandas/issues/166)) ([357a315](https://github.com/googleapis/python-db-dtypes-pandas/commit/357a3156a3eb37eede2edb7fc84e93fe32967f11))

## [1.0.5](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.0.4...v1.0.5) (2022-12-05)


### Dependencies

* remove upper bound on pyarrow version ([388e082](https://github.com/googleapis/python-db-dtypes-pandas/commit/388e082a47d9515a14e20ffd87705c71712087ab))

## [1.0.4](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.0.3...v1.0.4) (2022-09-19)


### Bug Fixes

* Avoid out-of-range nanoseconds field in pandas 1.5.x ([#148](https://github.com/googleapis/python-db-dtypes-pandas/issues/148)) ([2a477ca](https://github.com/googleapis/python-db-dtypes-pandas/commit/2a477ca42033867fbf76f0a818677b04d4d66f8f))
* **deps:** Remove python version upper bound ([#145](https://github.com/googleapis/python-db-dtypes-pandas/issues/145)) ([a361806](https://github.com/googleapis/python-db-dtypes-pandas/commit/a361806026b0358270d101e9eff362d08a971076))

## [1.0.3](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.0.2...v1.0.3) (2022-08-05)


### Bug Fixes

* **deps:** allow pyarrow < 10 ([#130](https://github.com/googleapis/python-db-dtypes-pandas/issues/130)) ([508564f](https://github.com/googleapis/python-db-dtypes-pandas/commit/508564f1b898ec1ad7cae4c826ab3ad4b9a5349e))
* require python 3.7+ ([#125](https://github.com/googleapis/python-db-dtypes-pandas/issues/125)) ([bce01df](https://github.com/googleapis/python-db-dtypes-pandas/commit/bce01dfe92815ea478e1db4166e629062ec5ff97))

## [1.0.2](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.0.1...v1.0.2) (2022-06-03)


### Documentation

* fix changelog header to consistent size ([#111](https://github.com/googleapis/python-db-dtypes-pandas/issues/111)) ([145f875](https://github.com/googleapis/python-db-dtypes-pandas/commit/145f8750682fb007343a57c7c94bc5e7fa5b63ab))

## [1.0.1](https://github.com/googleapis/python-db-dtypes-pandas/compare/v1.0.0...v1.0.1) (2022-05-07)


### Bug Fixes

* **deps:** allow pyarrow v8 ([#109](https://github.com/googleapis/python-db-dtypes-pandas/issues/109)) ([fb30adf](https://github.com/googleapis/python-db-dtypes-pandas/commit/fb30adfd427d3df9919df00b096210ba1eb1b91d))

## [1.0.0](https://github.com/googleapis/python-db-dtypes-pandas/compare/v0.4.0...v1.0.0) (2022-03-25)


### Features

* label package as generally available ([#92](https://github.com/googleapis/python-db-dtypes-pandas/issues/92)) ([0363e87](https://github.com/googleapis/python-db-dtypes-pandas/commit/0363e8725b322881c1fe1e89bdeadd0f67317d22))

## [0.4.0](https://github.com/googleapis/python-db-dtypes-pandas/compare/v0.3.1...v0.4.0) (2022-03-24)


### ⚠ BREAKING CHANGES

* dbdate and dbtime dtypes return NaT instead of None for missing values

### Features

* dbdate and dbtime support numpy.datetime64 values in array constructor ([1db1357](https://github.com/googleapis/python-db-dtypes-pandas/commit/1db1357186b234a28b2ced10174bbd06e2f0ab73))


### Bug Fixes

* address failing 2D array compliance tests  in DateArray ([#64](https://github.com/googleapis/python-db-dtypes-pandas/issues/64)) ([b771e05](https://github.com/googleapis/python-db-dtypes-pandas/commit/b771e050acd2bdbf469a97f7477036c159b500f8))
* address failing tests with pandas 1.5.0 ([#82](https://github.com/googleapis/python-db-dtypes-pandas/issues/82)) ([38ac28d](https://github.com/googleapis/python-db-dtypes-pandas/commit/38ac28d8b16f9b86b5029c85e45e9f2e034159b7))
* allow comparison with scalar values ([#88](https://github.com/googleapis/python-db-dtypes-pandas/issues/88)) ([7495698](https://github.com/googleapis/python-db-dtypes-pandas/commit/7495698b3be3b7e8055ae450e24cd0e366b1b72a))
* avoid TypeError when using sorted search ([#84](https://github.com/googleapis/python-db-dtypes-pandas/issues/84)) ([42bc2d9](https://github.com/googleapis/python-db-dtypes-pandas/commit/42bc2d90174d152dfed782acf77016da55dbdaca))
* correct TypeError and comparison issues discovered in DateArray compliance tests ([#79](https://github.com/googleapis/python-db-dtypes-pandas/issues/79)) ([1e979cf](https://github.com/googleapis/python-db-dtypes-pandas/commit/1e979cf360eb586e77b415f7b710a8a41c22e981))
* dbdate and dbtime support set item with null values ([#85](https://github.com/googleapis/python-db-dtypes-pandas/issues/85)) ([1db1357](https://github.com/googleapis/python-db-dtypes-pandas/commit/1db1357186b234a28b2ced10174bbd06e2f0ab73))
* use `pandas.NaT` for missing values in dbdate and dbtime dtypes ([#67](https://github.com/googleapis/python-db-dtypes-pandas/issues/67)) ([f903c2c](https://github.com/googleapis/python-db-dtypes-pandas/commit/f903c2c68da1629241cf3bf37e1226babae669f4))
* use public pandas APIs where possible ([#60](https://github.com/googleapis/python-db-dtypes-pandas/issues/60)) ([e9d41d1](https://github.com/googleapis/python-db-dtypes-pandas/commit/e9d41d17b5d6a7d83c46e2497feb8e314545adcb))


### Tests

* add dbtime compliance tests ([#90](https://github.com/googleapis/python-db-dtypes-pandas/issues/90)) ([f14fb2b](https://github.com/googleapis/python-db-dtypes-pandas/commit/f14fb2bf78d8427b9546db4cdad1d893c1b1e5e1))
* add final dbdate compliance tests and sort ([#89](https://github.com/googleapis/python-db-dtypes-pandas/issues/89)) ([efe7e6d](https://github.com/googleapis/python-db-dtypes-pandas/commit/efe7e6d8953ebf8d2b4d9468c7c92638ea2ec9f9))

## [0.3.1](https://www.github.com/googleapis/python-db-dtypes-pandas/compare/v0.3.0...v0.3.1) (2021-12-04)


### Bug Fixes

* raise ValueError if date is out-of-bounds ([#46](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/46)) ([4253358](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/4253358b673965f7d2823b750f56553f6627e130))

## [0.3.0](https://www.github.com/googleapis/python-db-dtypes-pandas/compare/v0.2.0...v0.3.0) (2021-11-08)


### Features

* support conversion from pyarrow RecordBatch to pandas DataFrame ([#39](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/39)) ([facc7b0](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/facc7b0897e27c5ba99399b7d453818c5b4aeca7))
* support Python 3.10 ([#40](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/40)) ([a31d55d](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/a31d55db57b2f5655b1fee4230a930d5bee4b1c9))

## [0.2.0](https://www.github.com/googleapis/python-db-dtypes-pandas/compare/v0.1.1...v0.2.0) (2021-10-14)


### Features

* rename dbtime and dbdate dtypes to avoid future conflicts with pandas ([#32](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/32)) ([50ea0f7](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/50ea0f798548aa2f0516f6afc93ba6e80cc0e6d9))


### Documentation

* add how-to guide and include API reference ([#33](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/33)) ([878dce4](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/878dce48bd6714706a2a829775ce00e61724fc7a))

## [0.1.1](https://www.github.com/googleapis/python-db-dtypes-pandas/compare/v0.1.0...v0.1.1) (2021-10-04)


### Bug Fixes

* avoid rounding problems with microseconds ([#20](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/20)) ([0ff7371](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/0ff737120344602f49889596b1efa69a6a18a057))

## 0.1.0 (2021-09-29)


### Features

* add `time` and `date` dtypes ([f104171](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/f10417111642e8f5f4b9af790367af930d15a056))


### Bug Fixes

* support converting empty `time` Series to pyarrow Array ([#11](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/11)) ([7675b15](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/7675b157feb842628fa731cc6a472aa9e6b92903))
* support Pandas 0.24 ([#8](https://www.github.com/googleapis/python-db-dtypes-pandas/issues/8)) ([e996883](https://www.github.com/googleapis/python-db-dtypes-pandas/commit/e996883bc9c76fe5f593e9c19a9d2a1c13501f5e))
