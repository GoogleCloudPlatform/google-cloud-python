# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-access-context-manager/#history

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.6.1...google-cloud-access-context-manager-v0.6.2) (2026-10-22)


### Features

* declare support for Python 3.15 ([#18737](https://github.com/googleapis/google-cloud-python/issues/18737)) ([65c8767](https://github.com/googleapis/google-cloud-python/commit/65c87678e7a63aa4c8115c9273581aa5db82fbe9))
* update API sources and regenerate ([#18797](https://github.com/googleapis/google-cloud-python/issues/18797)) ([be4d954](https://github.com/googleapis/google-cloud-python/commit/be4d954baf9a27cad04637183047b156afa4784a))

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.6.0...google-cloud-access-context-manager-v0.6.1) (2026-08-06)


### Bug Fixes

* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.5.0...google-cloud-access-context-manager-v0.6.0) (2026-06-02)


### Bug Fixes

* update incorrect urls in setup.py to point at monorepo vs splitrepo (#17237) ([eaed04baf3cd356c3811c66e64c277c8841c7563](https://github.com/googleapis/google-cloud-python/commit/eaed04baf3cd356c3811c66e64c277c8841c7563))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.4.0...google-cloud-access-context-manager-v0.5.0) (2026-05-06)

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.3.0...google-cloud-access-context-manager-v0.4.0) (2026-03-26)


### Features

* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:c8612d3fffb3f6a32353b2d1abd16b61e87811866f7ec9d65b59b02eb452a620 ([d3579bf00f0cd37df54f7287518a9e2330bdcc83](https://github.com/googleapis/google-cloud-python/commit/d3579bf00f0cd37df54f7287518a9e2330bdcc83))


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.2.3...google-cloud-access-context-manager-v0.3.0) (2025-10-16)


### Features

* add support for Python 3.14 (#14699) Towards b/375664027 ([8b69540bf6fd862bc1aebb3baf423c419b1556d4](https://github.com/googleapis/google-cloud-python/commit/8b69540bf6fd862bc1aebb3baf423c419b1556d4))

## [0.2.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.2.2...google-cloud-access-context-manager-v0.2.3) (2025-10-07)


### Bug Fixes

* regenerate pb2 files with protoc v25.3 (#14569) This PR
- adds *.proto files to `packages/google-cloud-access-context-manager`
for consistency with what we have in `googleapis-common-protos`:
https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos/google/api
- uses `protoc v25.3` for consistency with what we have in
`googleapis-common-protos`:
https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos/google/api
- Adds `*.pyi` files for consistency with what we have in
`googleapis-common-protos`:
https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos/google/api
Towards https://github.com/googleapis/librarian/issues/1061 ([001097bc95a964d063eca7605a0c3acdd2f59727](https://github.com/googleapis/google-cloud-python/commit/001097bc95a964d063eca7605a0c3acdd2f59727))

## [0.2.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-access-context-manager-v0.2.1...google-cloud-access-context-manager-v0.2.2) (2025-03-15)


### Bug Fixes

* Allow protobuf 6.x ([b4d4551](https://github.com/googleapis/google-cloud-python/commit/b4d45514e4ab630334a54eb4201576062ecc1958))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))
* resolve issue where pre-release versions of dependencies are installed ([b4d4551](https://github.com/googleapis/google-cloud-python/commit/b4d45514e4ab630334a54eb4201576062ecc1958))

## [0.2.1](https://github.com/googleapis/python-access-context-manager/compare/v0.2.0...v0.2.1) (2024-08-14)


### Bug Fixes

* **deps:** Require protobuf&gt;=3.20.2, protobuf&lt;6 ([ef6827b](https://github.com/googleapis/python-access-context-manager/commit/ef6827b2aa9519abf760ddd20cd9ea0f228c4272))
* Regenerate pb2 files for compatibility with protobuf 5.x ([ef6827b](https://github.com/googleapis/python-access-context-manager/commit/ef6827b2aa9519abf760ddd20cd9ea0f228c4272))

## [0.2.0](https://github.com/googleapis/python-access-context-manager/compare/v0.1.16...v0.2.0) (2024-02-15)


### Features

* Add `egress_policies` and `ingress_policies` fields to `ServicePerimeter` [f31ec7d](https://github.com/googleapis/googleapis/commit/f31ec7d4d1f27fd76594165ae41a344465e9f228) ([eabf473](https://github.com/googleapis/python-access-context-manager/commit/eabf4737124074f8107a0dac716cb68134edf721))
* Add `google/identity/accesscontextmanager/v1/access_context_manager_pb2.py` [0b261de](https://github.com/googleapis/googleapis/commit/0b261def1cb4c61a9ddbb8bf14b103ce6add1bce) ([eabf473](https://github.com/googleapis/python-access-context-manager/commit/eabf4737124074f8107a0dac716cb68134edf721))
* Add support for Python 3.12 ([#188](https://github.com/googleapis/python-access-context-manager/issues/188)) ([c379c57](https://github.com/googleapis/python-access-context-manager/commit/c379c573573207ef6e6f355aa569e19149ef2824))
* Introduce compatibility with native namespace packages ([#187](https://github.com/googleapis/python-access-context-manager/issues/187)) ([8ffdcd3](https://github.com/googleapis/python-access-context-manager/commit/8ffdcd31ecc4a4b8e18b8534257ff02c391339f7))


### Bug Fixes

* **deps:** Require google-api-core &gt;= 1.34.1 ([eabf473](https://github.com/googleapis/python-access-context-manager/commit/eabf4737124074f8107a0dac716cb68134edf721))
* Migrate to native namespace packages ([#193](https://github.com/googleapis/python-access-context-manager/issues/193)) ([5840132](https://github.com/googleapis/python-access-context-manager/commit/58401328a92f418cb43492459971a7f2b7d712f2))

## [0.1.16](https://github.com/googleapis/python-access-context-manager/compare/v0.1.15...v0.1.16) (2023-02-27)


### Bug Fixes

* **deps:** Require google-api-core&gt;=1.34.0,>=2.11.0 ([a835c8e](https://github.com/googleapis/python-access-context-manager/commit/a835c8ef404c56b06fd446ee177bcb59daf0353a))

## [0.1.15](https://github.com/googleapis/python-access-context-manager/compare/v0.1.14...v0.1.15) (2022-12-15)


### Bug Fixes

* **deps:** Require protobuf &gt;=3.19.5 ([09d0f03](https://github.com/googleapis/python-access-context-manager/commit/09d0f0342ef60981a57458228435626d69129f70))

## [0.1.14](https://github.com/googleapis/python-access-context-manager/compare/v0.1.13...v0.1.14) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#138](https://github.com/googleapis/python-access-context-manager/issues/138)) ([3aec32e](https://github.com/googleapis/python-access-context-manager/commit/3aec32e555659b0581afdc2c2d2ed67c7de26c0d))

## [0.1.13](https://github.com/googleapis/python-access-context-manager/compare/v0.1.12...v0.1.13) (2022-07-18)


### Bug Fixes

* require python 3.7+ ([#134](https://github.com/googleapis/python-access-context-manager/issues/134)) ([27a1467](https://github.com/googleapis/python-access-context-manager/commit/27a1467e68d440b7c2a73a6b5dbcfe6bd199dd05))
* require google-api-core >=1.32.0, >=2.8.0


## [0.1.12](https://github.com/googleapis/python-access-context-manager/compare/v0.1.11...v0.1.12) (2022-06-06)


### Documentation

* fix changelog header to consistent size ([#128](https://github.com/googleapis/python-access-context-manager/issues/128)) ([e295ae6](https://github.com/googleapis/python-access-context-manager/commit/e295ae6b031d86543c54562f1011560272753898))

## [0.1.11](https://github.com/googleapis/python-access-context-manager/compare/v0.1.10...v0.1.11) (2022-05-26)


### Bug Fixes

* **deps:** require protobuf>= 3.12.0, <4.0.0dev ([#124](https://github.com/googleapis/python-access-context-manager/issues/124)) ([5c7837e](https://github.com/googleapis/python-access-context-manager/commit/5c7837eca6e49f465df306275f96ebece076364b))

## [0.1.10](https://github.com/googleapis/python-access-context-manager/compare/v0.1.9...v0.1.10) (2022-03-04)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#110](https://github.com/googleapis/python-access-context-manager/issues/110)) ([386dc8d](https://github.com/googleapis/python-access-context-manager/commit/386dc8dccbfa4ffee275ae92543b83e9dfc6f05e))
* regenerate pb2 files ([#108](https://github.com/googleapis/python-access-context-manager/issues/108)) ([f3ae216](https://github.com/googleapis/python-access-context-manager/commit/f3ae216524db604166447ccec2d646fb038ce3bb))

## [0.1.9](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.8...v0.1.9) (2021-11-12)


### Bug Fixes

* **deps:** require google-api-core >= 1.28.0 ([8845855](https://www.github.com/googleapis/python-access-context-manager/commit/8845855497454dbf62edd65dee958057a959db41))

## [0.1.8](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.7...v0.1.8) (2021-10-04)


### Bug Fixes

* update pin on 'google-api-core' to allow current versions ([#89](https://www.github.com/googleapis/python-access-context-manager/issues/89)) ([1f7b73b](https://www.github.com/googleapis/python-access-context-manager/commit/1f7b73b947011999b82976027ade8218d58ac788))

## [0.1.7](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.6...v0.1.7) (2021-08-23)


### Documentation

* migrate to main branch ([#76](https://www.github.com/googleapis/python-access-context-manager/issues/76)) ([4f36a1d](https://www.github.com/googleapis/python-access-context-manager/commit/4f36a1dad07554ef676c7b01a9f1bd0e132bdb01))

## [0.1.6](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.5...v0.1.6) (2021-07-27)


### Documentation

* add Samples section to CONTRIBUTING.rst ([#65](https://www.github.com/googleapis/python-access-context-manager/issues/65)) ([6091f99](https://www.github.com/googleapis/python-access-context-manager/commit/6091f999347e91f24842030bf1fb2e528cd4a6b5))


### Miscellaneous Chores

* release as 0.1.6 ([#68](https://www.github.com/googleapis/python-access-context-manager/issues/68)) ([647e651](https://www.github.com/googleapis/python-access-context-manager/commit/647e6513cef26eabb593c6f3e7a41780bc20648c))

## [0.1.5](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.4...v0.1.5) (2021-07-07)


### Bug Fixes

* require google-api-core >= 1.26.0 ([#57](https://www.github.com/googleapis/python-access-context-manager/issues/57)) ([12ddfa5](https://www.github.com/googleapis/python-access-context-manager/commit/12ddfa58a5c4951da5753858701a83b297d38be2))

## [0.1.4](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.3...v0.1.4) (2021-06-22)


### Bug Fixes

* **deps:** require python 3.6 ([#46](https://www.github.com/googleapis/python-access-context-manager/issues/46)) ([3a4c5de](https://www.github.com/googleapis/python-access-context-manager/commit/3a4c5def322acc5bd16bdbeafef6d3235b5eadab))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-access-context-manager/issues/1127)) ([#44](https://www.github.com/googleapis/python-access-context-manager/issues/44)) ([5bd362e](https://www.github.com/googleapis/python-access-context-manager/commit/5bd362e10d1fd84f31bca28345560dbb9f71437f))

## [0.1.3](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.2...v0.1.3) (2021-04-14)


### Bug Fixes

* add create_key to protos ([#25](https://www.github.com/googleapis/python-access-context-manager/issues/25)) ([166c54c](https://www.github.com/googleapis/python-access-context-manager/commit/166c54cd73d2cfac6d45df2a676389f252fd73e3))

## [0.1.2](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.1...v0.1.2) (2020-05-08)


### Bug Fixes

* add missing __init__.py ([5b0036f](https://www.github.com/googleapis/python-access-context-manager/commit/5b0036f6155ea90a7501076487cb048ce1640e0e))

## [0.1.1](https://www.github.com/googleapis/python-access-context-manager/compare/v0.1.0...v0.1.1) (2020-05-08)


### Bug Fixes

* fix setup.py ([b2facea](https://www.github.com/googleapis/python-access-context-manager/commit/b2faceabc0aab7a3e1a590d71fef3ede1113a08b))

## 0.1.0 (2020-05-07)


### Features

* generate v1 ([a13e3de](https://www.github.com/googleapis/python-access-context-manager/commit/a13e3de91ee249d6d0640977315881f3bef0c844))
