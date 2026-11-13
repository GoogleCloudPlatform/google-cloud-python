# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-crc32c/#history

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-crc32c-v1.9.0-rc0...google-crc32c-v1.9.0) (2026-09-24)


### Features

* **crc32c:** support Python 3.15 ([1bf979a](https://github.com/googleapis/google-cloud-python/commit/1bf979a2efc0b8c6ccc738b046698beb7914d21a))

## [1.9.0-rc0](https://github.com/googleapis/google-cloud-python/compare/google-crc32c-v1.8.0...google-crc32c-v1.9.0-rc0) (2026-09-23)


### Features

* add unit and cover nox sessions and enforce 100% test coverage for ([9d2e62f](https://github.com/googleapis/google-cloud-python/commit/9d2e62faea7f812a4564c56034eb32113f41edba)), refs [#17052](https://github.com/googleapis/google-cloud-python/issues/17052)
* **crc32c:** add Python 3.15 classifier ([08291df](https://github.com/googleapis/google-cloud-python/commit/08291df4d20f8742a1f139ff3b896ff8485f567d))
* **crc32c:** add Python 3.15 wheel build support ([#18416](https://github.com/googleapis/google-cloud-python/issues/18416)) ([47b2845](https://github.com/googleapis/google-cloud-python/commit/47b2845c8b4113fd0633242c439d150b8f684888))
* **crc32c:** add unit and cover nox sessions ([#18424](https://github.com/googleapis/google-cloud-python/issues/18424)) ([9d2e62f](https://github.com/googleapis/google-cloud-python/commit/9d2e62faea7f812a4564c56034eb32113f41edba))


### Bug Fixes

* bump pip from 26.1.1 to 26.2 in /packages/google-crc32c/scripts ([#18259](https://github.com/googleapis/google-cloud-python/issues/18259)) ([ef272c7](https://github.com/googleapis/google-cloud-python/commit/ef272c7ebeef65304c441a8d5136464cc0bd202c))
* **crc32c:** escape the version dot and anchor the pyenv check regex ([#17555](https://github.com/googleapis/google-cloud-python/issues/17555)) ([b6a0275](https://github.com/googleapis/google-cloud-python/commit/b6a027513422507f99662c840068249b84522a5c))


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))


### Miscellaneous Chores

* **crc32c:** document Python 3.15 wheel support ([#18442](https://github.com/googleapis/google-cloud-python/issues/18442)) ([72c6a57](https://github.com/googleapis/google-cloud-python/commit/72c6a5716b8c4f7ecdf185b0da87960192acf578))

## [1.8.0](https://github.com/googleapis/python-crc32c/compare/v1.7.1...v1.8.0) (2025-12-15)


### Features

* Add support for Python 3.14 ([d3118d9](https://github.com/googleapis/python-crc32c/commit/d3118d938b0acabc68fbc9d009aeb1e00445bc4c))
* Support Python 3.14 ([#315](https://github.com/googleapis/python-crc32c/issues/315)) ([49d0a36](https://github.com/googleapis/python-crc32c/commit/49d0a36f3334048833d0201788fd864d3342d1b2))


### Bug Fixes

* Update toml file with setup.cfg content ([#319](https://github.com/googleapis/python-crc32c/issues/319)) ([42e5268](https://github.com/googleapis/python-crc32c/commit/42e5268c7e6077a71e54b342ada4ed2843dbc01e))

## [1.8.0](https://github.com/googleapis/python-crc32c/compare/v1.7.1...v1.8.0) (2025-12-15)


### Features

* support Python 3.14 (#315) ([49d0a36f3334048833d0201788fd864d3342d1b2](https://github.com/googleapis/python-crc32c/commit/49d0a36f3334048833d0201788fd864d3342d1b2))


### Bug Fixes

* update toml file with setup.cfg content (#319) ([42e5268c7e6077a71e54b342ada4ed2843dbc01e](https://github.com/googleapis/python-crc32c/commit/42e5268c7e6077a71e54b342ada4ed2843dbc01e))

## [1.7.1](https://github.com/googleapis/python-crc32c/compare/v1.7.0...v1.7.1) (2025-03-25)


### Bug Fixes

* Add Python 3.13 windows wheels ([fbb0e26](https://github.com/googleapis/python-crc32c/commit/fbb0e26b576fb82b8677b14505e702313cbcfe4e))

## [1.7.0](https://github.com/googleapis/python-crc32c/compare/v1.6.0...v1.7.0) (2025-03-17)


### Features

* Add Python 3.13 trove classifier ([#233](https://github.com/googleapis/python-crc32c/issues/233)) ([b125257](https://github.com/googleapis/python-crc32c/commit/b1252575f21d0dde1e131f5251a989f56fb2c0d5))
* Add support for python 3.13 ([#239](https://github.com/googleapis/python-crc32c/issues/239)) ([6b918f4](https://github.com/googleapis/python-crc32c/commit/6b918f4b081daf3cbee0cbd778b27c98670fb3a4))

## [1.6.0](https://github.com/googleapis/python-crc32c/compare/v1.5.0...v1.6.0) (2024-08-29)


### Features

* Add support for python 3.12 ([#177](https://github.com/googleapis/python-crc32c/issues/177)) ([5ff1207](https://github.com/googleapis/python-crc32c/commit/5ff1207e7b60256e7a32932324ccb9ad4ec265d2))
* Build using Visual Studio 17 2022 instead of Visual Studio 16 2019 ([c1c8c59](https://github.com/googleapis/python-crc32c/commit/c1c8c597d07e573406d76765022a837b007f9074))


### Bug Fixes

* Drop support for python 3.7 and 3.8 ([c1c8c59](https://github.com/googleapis/python-crc32c/commit/c1c8c597d07e573406d76765022a837b007f9074))
* Drop support for Windows 32bit which is not supported in Visual Studio 17 2022 ([c1c8c59](https://github.com/googleapis/python-crc32c/commit/c1c8c597d07e573406d76765022a837b007f9074))
* Remove manylinux1 which is no longer supported by PyPA ([#186](https://github.com/googleapis/python-crc32c/issues/186)) ([79edb3f](https://github.com/googleapis/python-crc32c/commit/79edb3fd3cda0e4193a6fb6a8346058398df43de))

## [1.5.0](https://github.com/googleapis/python-crc32c/compare/v1.4.0...v1.5.0) (2022-08-31)


### Features

* add support for Python 3.11 ([#144](https://github.com/googleapis/python-crc32c/issues/144)) ([63f5166](https://github.com/googleapis/python-crc32c/commit/63f5166815682d3430a771c51c7fd5a81d2fd259))


### Bug Fixes

* drop support for python 3.6 ([#145](https://github.com/googleapis/python-crc32c/issues/145)) ([f9745b8](https://github.com/googleapis/python-crc32c/commit/f9745b8089fa2645be7b8823c979f5192df3eec7))


### Documentation

* fix changelog header to consistent size ([#136](https://github.com/googleapis/python-crc32c/issues/136)) ([0fb3b88](https://github.com/googleapis/python-crc32c/commit/0fb3b88131aeee316e6d6f607fa32ec4767e4386))

## [1.4.0](https://github.com/googleapis/python-crc32c/compare/v1.3.0...v1.4.0) (2022-03-10)


### Features

* add 'py.typed' declaration ([#119](https://github.com/googleapis/python-crc32c/issues/119)) ([f1c91c2](https://github.com/googleapis/python-crc32c/commit/f1c91c277f1baac2ca8d60dd1e45361551ad3140))


### Bug Fixes

* add empty slots to CommonChecksum ([#121](https://github.com/googleapis/python-crc32c/issues/121)) ([c21cb89](https://github.com/googleapis/python-crc32c/commit/c21cb8923728801d732c11f6531a2415a1e5cd3f))

## [1.3.0](https://www.github.com/googleapis/python-crc32c/compare/v1.2.0...v1.3.0) (2021-10-05)


### Features

* add support for Python 3.10 ([#116](https://www.github.com/googleapis/python-crc32c/issues/116)) ([01ee9c0](https://www.github.com/googleapis/python-crc32c/commit/01ee9c0b4d6a992ddcf1fbbeaaea9d107c972b74))

## [1.2.0](https://www.github.com/googleapis/python-crc32c/compare/v1.1.5...v1.2.0) (2021-09-17)


### Features

* build wheels using CIBuildWheel ([#103](https://www.github.com/googleapis/python-crc32c/issues/103)) ([55eb731](https://www.github.com/googleapis/python-crc32c/commit/55eb7310b0a0f424da33f4b6d3b4b50e02c323eb))


### Documentation

* update list of supported wheel platforms / architectures ([#105](https://www.github.com/googleapis/python-crc32c/issues/105)) ([edc8d2d](https://www.github.com/googleapis/python-crc32c/commit/edc8d2dbe643f0c2bf1180f855e1585b0e81bdba))

## [1.1.5](https://www.github.com/googleapis/python-crc32c/compare/v1.1.4...v1.1.5) (2021-09-07)


### Bug Fixes

* revert to silent fallback to pure-Python build ([#93](https://www.github.com/googleapis/python-crc32c/issues/93)) ([789a420](https://www.github.com/googleapis/python-crc32c/commit/789a4203648d1b43f060332510177cf3867f82c4))
* fix segfault on MacOS 11 ("Big Sur") for Python < 3.9 ([#93](https://www.github.com/googleapis/python-crc32c/issues/93)) ([789a420](https://www.github.com/googleapis/python-crc32c/commit/789a4203648d1b43f060332510177cf3867f82c4))

## [1.1.4](https://www.github.com/googleapis/python-crc32c/compare/v1.1.4...v1.1.4) (2021-09-02)


### Bug Fixes

* advise setting 'CRC32C_PURE_PYTHON' after build failure ([#84](https://www.github.com/googleapis/python-crc32c/issues/84)) ([6aa1cd6](https://www.github.com/googleapis/python-crc32c/commit/6aa1cd69376b57fbc9bc2c470ed63a270279623d))
* restore building 'manylinux1' wheels ([#87](https://www.github.com/googleapis/python-crc32c/issues/87)) ([ebb9c68](https://www.github.com/googleapis/python-crc32c/commit/ebb9c68aca66e6b89d832e9e237679ac8b9ad344))
* use correct Python 3.10 specifier ([#88](https://www.github.com/googleapis/python-crc32c/issues/88)) ([0c1b740](https://www.github.com/googleapis/python-crc32c/commit/0c1b740c195caed8ac1e67fc38d87073223a6b3d))

## [1.1.4](https://www.github.com/googleapis/python-crc32c/compare/v1.1.3...v1.1.4) (2021-09-01)


### Bug Fixes

* advise setting 'CRC32C_PURE_PYTHON' after build failure ([#84](https://www.github.com/googleapis/python-crc32c/issues/84)) ([6aa1cd6](https://www.github.com/googleapis/python-crc32c/commit/6aa1cd69376b57fbc9bc2c470ed63a270279623d))
* restore building 'manylinux1' wheels ([#87](https://www.github.com/googleapis/python-crc32c/issues/87)) ([ebb9c68](https://www.github.com/googleapis/python-crc32c/commit/ebb9c68aca66e6b89d832e9e237679ac8b9ad344))

## [1.1.3](https://www.github.com/googleapis/python-crc32c/compare/v1.1.2...v1.1.3) (2021-08-30)


### Performance Improvements

* replace CFFI with a native C extension ([#76](https://www.github.com/googleapis/python-crc32c/issues/76)) ([b1bf461](https://www.github.com/googleapis/python-crc32c/commit/b1bf461cc0539962ac16a62860cae3cd2384cb4f))

## [1.1.2](https://www.github.com/googleapis/python-crc32c/compare/v1.1.1...v1.1.2) (2021-01-20)


### Bug Fixes

* add manylinux2014_aarch64 wheels ([#61](https://www.github.com/googleapis/python-crc32c/issues/61)) ([6387658](https://www.github.com/googleapis/python-crc32c/commit/63876582aec715100f61581657f9d994a1ace1bc))
* Add manylinux2014_x86_64 wheels ([#57](https://www.github.com/googleapis/python-crc32c/issues/57)) ([74cb457](https://www.github.com/googleapis/python-crc32c/commit/74cb457255a81d0aa5bee16425675140ed637410))


### Documentation

* add aarch64 to the readme as produced wheels ([#62](https://www.github.com/googleapis/python-crc32c/issues/62)) ([4ef317d](https://www.github.com/googleapis/python-crc32c/commit/4ef317d0efcd654842d17e03749b801303c8bc30))

## [1.1.1](https://www.github.com/googleapis/python-crc32c/compare/v1.1.0...v1.1.1) (2021-01-14)


### Bug Fixes

* Update CI to use GitHub actions and build for osx, windows, linux ([#51](https://www.github.com/googleapis/python-crc32c/issues/51)) ([66f49b8](https://www.github.com/googleapis/python-crc32c/commit/66f49b889ad66f7ecd5d6aeaf840f2c8f2ac131e))


### Documentation

* simplify main readme that is shown on pypi, add additional BUILDING.md ([#54](https://www.github.com/googleapis/python-crc32c/issues/54)) ([93e021f](https://www.github.com/googleapis/python-crc32c/commit/93e021fe8bc55fb046317b884ca21cb75e131e4f))

## [1.1.0](https://www.github.com/googleapis/python-crc32c/compare/v0.1.1...v1.1.0) (2020-12-14)


### Features

* add Python 3.9 support, drop Python 3.5 support ([#42](https://www.github.com/googleapis/python-crc32c/issues/42)) ([1d7fe63](https://www.github.com/googleapis/python-crc32c/commit/1d7fe6338fbcb0e74245f84c2034ac5371f7782a)), closes [#38](https://www.github.com/googleapis/python-crc32c/issues/38)


### Bug Fixes

* add LICENSE to package manifest ([#34](https://www.github.com/googleapis/python-crc32c/issues/34)) ([6c8883b](https://www.github.com/googleapis/python-crc32c/commit/6c8883b2c41aaa6f0dd5991896ad58e73f516182))

## [1.0.0](https://www.github.com/googleapis/python-crc32c/compare/v0.1.0...v1.0.0) (2020-08-07)

### Breaking Changes
* prefix module name with 'google_' to avoid conflict with ICRAR version ([#30](https://www.github.com/googleapis/python-crc32c/issues/30)) ([b50f43e](https://www.github.com/googleapis/python-crc32c/commit/b50f43e7bc40d91ccdade9ccc577a93c0ed05f3a)), closes [#29](https://www.github.com/googleapis/python-crc32c/issues/29)

### Documentation

* rewrap long line ([#32](https://www.github.com/googleapis/python-crc32c/issues/32)) ([30479d4](https://www.github.com/googleapis/python-crc32c/commit/30479d41997a09115aa0152b39ffef09bc97b13a))

## [0.1.0](https://www.github.com/googleapis/python-crc32c/compare/v0.0.2...v0.1.0) (2020-03-20)


### Features

* add pure python implementation ([#20](https://www.github.com/googleapis/python-crc32c/issues/20)) ([97cf381](https://www.github.com/googleapis/python-crc32c/commit/97cf3819035486628b2dcc2ad03e3b427fbf8046))


### Bug Fixes

* retrieve package version at runtime ([#24](https://www.github.com/googleapis/python-crc32c/issues/24)) ([f365e47](https://www.github.com/googleapis/python-crc32c/commit/f365e471c9ae90238ded65456635ccdb6cd33ca2))

## 0.0.2

03-09-2020 15:33 PDT


### Packaging Changes
- fix: add a manifest to specify other files ([#14](https://github.com/googleapis/python-crc32c/pull/14))

### Documentation
- docs: README.md improvements ([#15](https://github.com/googleapis/python-crc32c/pull/15))
