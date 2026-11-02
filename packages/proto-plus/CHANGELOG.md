# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/proto-plus/#history

## [1.29.0](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.28.4...proto-plus-v1.29.0) (2026-09-29)


### Features

* declare Python3.15 support ([05b0c34](https://github.com/googleapis/google-cloud-python/commit/05b0c342683b2b0e1b8dccd201ec86ec89612edc))

## [1.28.4](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.28.3...proto-plus-v1.28.4) (2026-08-21)


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [1.28.3](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.28.2...proto-plus-v1.28.3) (2026-08-06)


### Bug Fixes

* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* **proto-plus:** add context to TypeErrors during message manipulation ([#17682](https://github.com/googleapis/google-cloud-python/issues/17682)) ([08f21a6](https://github.com/googleapis/google-cloud-python/commit/08f21a6bfc357d249a6c85cd9d4282154fa9aba2))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [1.28.2](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.28.1...proto-plus-v1.28.2) (2026-07-22)


### Bug Fixes

* **proto-plus:** make Marshal thread-safe and handle race conditions ([#17774](https://github.com/googleapis/google-cloud-python/issues/17774)) ([0719f1e](https://github.com/googleapis/google-cloud-python/commit/0719f1ec1d4146dbfc96d24c95b7ccafd31ab447)), closes [#15100](https://github.com/googleapis/google-cloud-python/issues/15100)

## [1.28.1](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.28.0...proto-plus-v1.28.1) (2026-07-07)


### Bug Fixes

* **tests:** add --cov-append to gapic-generator and proto-plus to preserve monorepo coverage ([#17603](https://github.com/googleapis/google-cloud-python/issues/17603)) ([2ddcf4d](https://github.com/googleapis/google-cloud-python/commit/2ddcf4dfc711771b284797569f7f8a2de902ade8))

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.27.2...proto-plus-v1.28.0) (2026-05-06)

## [1.27.2](https://github.com/googleapis/google-cloud-python/compare/proto-plus-v1.27.1...proto-plus-v1.27.2) (2026-03-26)


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [1.27.1](https://github.com/googleapis/proto-plus-python/compare/v1.27.0...v1.27.1) (2026-01-30)


### Bug Fixes

* remove float_precision for protobuf 7 (#559) ([390b9d571bb5e58879137d5ac7c4cea1978e0024](https://github.com/googleapis/proto-plus-python/commit/390b9d571bb5e58879137d5ac7c4cea1978e0024))

## [1.27.0](https://github.com/googleapis/proto-plus-python/compare/v1.26.1...v1.27.0) (2025-12-12)


### Features

* Add classifier for Python 3.14 (#544) ([d9f41512648c4551fc3e926649864c5dfe3964b2](https://github.com/googleapis/proto-plus-python/commit/d9f41512648c4551fc3e926649864c5dfe3964b2))

## [1.26.1](https://github.com/googleapis/proto-plus-python/compare/v1.26.0...v1.26.1) (2025-03-05)


### Bug Fixes

* **deps:** Allow protobuf 6.x ([#536](https://github.com/googleapis/proto-plus-python/issues/536)) ([51ba025](https://github.com/googleapis/proto-plus-python/commit/51ba02513c4fa12fe94db74c4a23fed7af972ea9))

## [1.26.0](https://github.com/googleapis/proto-plus-python/compare/v1.25.0...v1.26.0) (2025-01-22)


### Features

* Migrate to pyproject.toml ([#496](https://github.com/googleapis/proto-plus-python/issues/496)) ([82ed3b9](https://github.com/googleapis/proto-plus-python/commit/82ed3b91ae0cebd6f89ce6661590a1bc6b7fce31))


### Bug Fixes

* Construct messages with nested duration in protobuf 5.28+ ([#519](https://github.com/googleapis/proto-plus-python/issues/519)) ([197ddf8](https://github.com/googleapis/proto-plus-python/commit/197ddf8a3ae9ab21b0136f27692d0f1ecd727d5b))
* Fix enums initialization in PyPy ([#507](https://github.com/googleapis/proto-plus-python/issues/507)) ([b8b68f2](https://github.com/googleapis/proto-plus-python/commit/b8b68f207a00129e91551ef6725f5021f821e0a9))
* Incorrect return type annotation for Message.to_dict ([#516](https://github.com/googleapis/proto-plus-python/issues/516)) ([72990f3](https://github.com/googleapis/proto-plus-python/commit/72990f3859d77732d40db5b82c310da265e72cac))
* Use include rather than exclude to find_namespace_packages in setup.py ([#502](https://github.com/googleapis/proto-plus-python/issues/502)) ([77e252e](https://github.com/googleapis/proto-plus-python/commit/77e252e614f6434c2c47ab6168d08f87e004be43))


### Documentation

* Update docs link in README ([#524](https://github.com/googleapis/proto-plus-python/issues/524)) ([a85be75](https://github.com/googleapis/proto-plus-python/commit/a85be75f8fb811f5345cea2786b9b7a688085a7e))

## [1.25.0](https://github.com/googleapis/proto-plus-python/compare/v1.24.0...v1.25.0) (2024-10-15)


### Features

* Add support for Python 3.13 ([#493](https://github.com/googleapis/proto-plus-python/issues/493)) ([e9643a1](https://github.com/googleapis/proto-plus-python/commit/e9643a1f6135267d4389c77722120e6c98342a74))


### Bug Fixes

* Construct messages with nested struct ([#479](https://github.com/googleapis/proto-plus-python/issues/479)) ([aa4aa61](https://github.com/googleapis/proto-plus-python/commit/aa4aa61b8c7ac0cc34d2d5797999bb434de88737))
* Fix 'Couldn't build proto file' when using Python 3.13 ([#492](https://github.com/googleapis/proto-plus-python/issues/492)) ([a48c39f](https://github.com/googleapis/proto-plus-python/commit/a48c39ff2212261bc932d10132086a6c55be22e9))
* Fix conda compatibility issue ([#475](https://github.com/googleapis/proto-plus-python/issues/475)) ([e2f9c9d](https://github.com/googleapis/proto-plus-python/commit/e2f9c9d1c87230d0e8d9ccacdfd0872792d54f1b))
* Fix issue with equality comparison of repeated field with None ([#477](https://github.com/googleapis/proto-plus-python/issues/477)) ([3476348](https://github.com/googleapis/proto-plus-python/commit/3476348c995af2ce5dfcbcc688e9ddf98fa36360))
* Remove check for Protobuf version ([#474](https://github.com/googleapis/proto-plus-python/issues/474)) ([a1748a3](https://github.com/googleapis/proto-plus-python/commit/a1748a315b6b50128b0d9927b2fee353ec55975f))


### Documentation

* Fix typos in proto/message.py ([#463](https://github.com/googleapis/proto-plus-python/issues/463)) ([4d8ee65](https://github.com/googleapis/proto-plus-python/commit/4d8ee656e008ec2b22f347e5da539b6285ec4b1b))
* Update message.py spelling error `paylod` → `payload` ([e59fc9a](https://github.com/googleapis/proto-plus-python/commit/e59fc9a4f8dd9fcb0804b77347662ae29d1a31a1))

## [1.24.0](https://github.com/googleapis/proto-plus-python/compare/v1.23.0...v1.24.0) (2024-06-11)


### Features

* Add `always_print_fields_with_no_presence` fields to `to_json` and `to_dict` ([0f89372](https://github.com/googleapis/proto-plus-python/commit/0f893724cabe513a5a9f9c8428dbd31f1b4f1d52))


### Bug Fixes

* Add compatibility with protobuf==5.x ([0f89372](https://github.com/googleapis/proto-plus-python/commit/0f893724cabe513a5a9f9c8428dbd31f1b4f1d52))
* AttributeError module 'google._upb._message' has no attribute 'MessageMapContainer' ([0f89372](https://github.com/googleapis/proto-plus-python/commit/0f893724cabe513a5a9f9c8428dbd31f1b4f1d52))
* **deps:** Allow protobuf 5.x ([#457](https://github.com/googleapis/proto-plus-python/issues/457)) ([62d74e3](https://github.com/googleapis/proto-plus-python/commit/62d74e3275476b82fed48f2119fc761fe2371292))
* Drop python 3.6 ([#456](https://github.com/googleapis/proto-plus-python/issues/456)) ([5a7666c](https://github.com/googleapis/proto-plus-python/commit/5a7666c15002aee0fab44a9aa6d3279aab3f1f69))


### Documentation

* Deprecate field `including_default_value_fields` in `to_json` and `to_dict` ([0f89372](https://github.com/googleapis/proto-plus-python/commit/0f893724cabe513a5a9f9c8428dbd31f1b4f1d52))

## [1.23.0](https://github.com/googleapis/proto-plus-python/compare/v1.22.3...v1.23.0) (2023-12-01)


### Features

* Add additional parameters to `to_json()` and `to_dict()` methods ([#384](https://github.com/googleapis/proto-plus-python/issues/384)) ([8f13a46](https://github.com/googleapis/proto-plus-python/commit/8f13a46514e1d7653426c0db3c1021f9c794451a))
* Add support for proto.__version__ ([#393](https://github.com/googleapis/proto-plus-python/issues/393)) ([48cd63f](https://github.com/googleapis/proto-plus-python/commit/48cd63f2d0a7c62c40d2724f46ac564c9884675b))
* Add support for python 3.12 ([#400](https://github.com/googleapis/proto-plus-python/issues/400)) ([1b3a96f](https://github.com/googleapis/proto-plus-python/commit/1b3a96fae7a21bf0120a79ba6bf57aacfd2a0db4))


### Bug Fixes

* Use setuptools.find_namespace_packages ([#412](https://github.com/googleapis/proto-plus-python/issues/412)) ([30a6864](https://github.com/googleapis/proto-plus-python/commit/30a6864739eb8fb116caa5873044d3999f37f578))


### Documentation

* Add documentation on how to query the current oneof in a given message ([#408](https://github.com/googleapis/proto-plus-python/issues/408)) ([d89d811](https://github.com/googleapis/proto-plus-python/commit/d89d81112885f3b3ca4e1342fd2034ee6797fcf6))
* Add example for __protobuf__ module level attribute ([#409](https://github.com/googleapis/proto-plus-python/issues/409)) ([6755884](https://github.com/googleapis/proto-plus-python/commit/675588450acc4636b2d82b2bc0860a314064c4a4))

## [1.22.3](https://github.com/googleapis/proto-plus-python/compare/v1.22.2...v1.22.3) (2023-06-22)


### Bug Fixes

* Resolve issue where marshal fails with cross api dependency ([#348](https://github.com/googleapis/proto-plus-python/issues/348)) ([0dcea18](https://github.com/googleapis/proto-plus-python/commit/0dcea18898cdc2170a945f3d96216bae6a37e60f))

## [1.22.2](https://github.com/googleapis/proto-plus-python/compare/v1.22.1...v1.22.2) (2023-01-05)


### Bug Fixes

* Add support for Python 3.11 ([#329](https://github.com/googleapis/proto-plus-python/issues/329)) ([5cff3a0](https://github.com/googleapis/proto-plus-python/commit/5cff3a0d703fc90f757f1d150adc0dfd62aa3d2e))


### Documentation

* Fix typo in index.rst ([#342](https://github.com/googleapis/proto-plus-python/issues/342)) ([a66a378](https://github.com/googleapis/proto-plus-python/commit/a66a3782802a1088c775a6b29adb15fa0235e1f1))

## [1.22.1](https://github.com/googleapis/proto-plus-python/compare/v1.22.0...v1.22.1) (2022-08-29)


### Bug Fixes

* Add no-pretty print option ([#336](https://github.com/googleapis/proto-plus-python/issues/336)) ([1bb228a](https://github.com/googleapis/proto-plus-python/commit/1bb228ac93543d28871645a22e5ac7fb20a0a55c))

## [1.22.0](https://github.com/googleapis/proto-plus-python/compare/v1.21.0...v1.22.0) (2022-08-10)

### Features

* Add support for protobuf v4 ([#327](https://github.com/googleapis/proto-plus-python/issues/327)) ([ed353aa](https://github.com/googleapis/proto-plus-python/commit/ed353aaf8bd5a659535eb493221320e449f3f637))

### Bug Fixes

* Fix Timestamp, Duration and FieldMask marshaling in REST transport ([a2e7300](https://github.com/googleapis/proto-plus-python/commit/a2e7300368625ceec39dd2c2dfb96291ad8cf1f1))
* fixes bug in the test. ([#332](https://github.com/googleapis/proto-plus-python/issues/332)) ([f85f470](https://github.com/googleapis/proto-plus-python/commit/f85f470c880a7bff7f3c813d33d15e657e7b5123))

## [1.20.6](https://github.com/googleapis/proto-plus-python/compare/v1.20.5...v1.20.6) (2022-06-13)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#324](https://github.com/googleapis/proto-plus-python/issues/324)) ([af4f56e](https://github.com/googleapis/proto-plus-python/commit/af4f56edb0bfbfa808f7def37e19b24bd27d4b40))


### Documentation

* fix changelog header to consistent size ([#319](https://github.com/googleapis/proto-plus-python/issues/319)) ([27d2003](https://github.com/googleapis/proto-plus-python/commit/27d2003571342e24aa74d29a45fa49d2328ff76d))

## [1.20.5](https://github.com/googleapis/proto-plus-python/compare/v1.20.4...v1.20.5) (2022-05-26)


### Bug Fixes

* **deps:** require google-api-core[grpc] >= 1.31.5 ([1d13c41](https://github.com/googleapis/proto-plus-python/commit/1d13c415df457a87153a6fca202003fa83e56093))
* **deps:** require protobuf>= 3.15.0, <4.0.0dev ([#315](https://github.com/googleapis/proto-plus-python/issues/315)) ([1d13c41](https://github.com/googleapis/proto-plus-python/commit/1d13c415df457a87153a6fca202003fa83e56093))

## [1.20.4](https://github.com/googleapis/proto-plus-python/compare/v1.20.3...v1.20.4) (2022-05-02)


### Bug Fixes

* default proto package name is the module name, not "" ([#309](https://github.com/googleapis/proto-plus-python/issues/309)) ([3148a1c](https://github.com/googleapis/proto-plus-python/commit/3148a1c287eb69b397c940119cd44e5067357e17))
* lookup attribute instead of performing a deepcopy ([#226](https://github.com/googleapis/proto-plus-python/issues/226)) ([e469059](https://github.com/googleapis/proto-plus-python/commit/e469059d70bab4c2b0a38dd52c4451b3c61bf470))

## [1.20.3](https://github.com/googleapis/proto-plus-python/compare/v1.20.2...v1.20.3) (2022-02-18)


### Bug Fixes

* additional logic to mitigate collisions with reserved terms ([#301](https://github.com/googleapis/proto-plus-python/issues/301)) ([c9a77df](https://github.com/googleapis/proto-plus-python/commit/c9a77df58e93a87952470d809538a08103644364))

## [1.20.2](https://github.com/googleapis/proto-plus-python/compare/v1.20.1...v1.20.2) (2022-02-17)


### Bug Fixes

* dir(proto.Message) does not raise ([#302](https://github.com/googleapis/proto-plus-python/issues/302)) ([80dcce9](https://github.com/googleapis/proto-plus-python/commit/80dcce9099e630a6217792b6b3a14213add690e6))

## [1.20.1](https://github.com/googleapis/proto-plus-python/compare/v1.20.0...v1.20.1) (2022-02-14)


### Bug Fixes

* mitigate collisions in field names ([#295](https://github.com/googleapis/proto-plus-python/issues/295)) ([158ae99](https://github.com/googleapis/proto-plus-python/commit/158ae995aa4fdf6239c864a41f5df5575a3c30b3))

## [1.20.0](https://github.com/googleapis/proto-plus-python/compare/v1.19.9...v1.20.0) (2022-02-07)


### Features

* add custom __dir__ for messages and message classes ([#289](https://github.com/googleapis/proto-plus-python/issues/289)) ([35e019e](https://github.com/googleapis/proto-plus-python/commit/35e019eb8155c1e4067b326804e3e7e86f85b6a8))


### Bug Fixes

* workaround for buggy pytest ([#291](https://github.com/googleapis/proto-plus-python/issues/291)) ([28aa3b2](https://github.com/googleapis/proto-plus-python/commit/28aa3b2b325d2ba262f35cfc8d20e1f5fbdcf883))

## [1.19.9](https://github.com/googleapis/proto-plus-python/compare/v1.19.8...v1.19.9) (2022-01-25)


### Bug Fixes

* add pickling support to proto messages ([#280](https://github.com/googleapis/proto-plus-python/issues/280)) ([2b7be35](https://github.com/googleapis/proto-plus-python/commit/2b7be3563f9fc2a4649a5e14d7653b85020c566f))

## [1.19.8](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.7...v1.19.8) (2021-11-09)


### Documentation

* fix typos ([#277](https://www.github.com/googleapis/proto-plus-python/issues/277)) ([e3b71e8](https://www.github.com/googleapis/proto-plus-python/commit/e3b71e8b2a81a5abb5af666c9625facb1814a609))

## [1.19.7](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.6...v1.19.7) (2021-10-27)


### Bug Fixes

* restore allowing None as value for stringy ints ([#272](https://www.github.com/googleapis/proto-plus-python/issues/272)) ([a8991d7](https://www.github.com/googleapis/proto-plus-python/commit/a8991d71ff455093fbfef142f9140d3f2928195f))

## [1.19.6](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.5...v1.19.6) (2021-10-25)


### Bug Fixes

* setting 64bit fields from strings supported ([#267](https://www.github.com/googleapis/proto-plus-python/issues/267)) ([ea7b911](https://www.github.com/googleapis/proto-plus-python/commit/ea7b91100114f5c3d40d41320b045568ac9a68f9))

## [1.19.5](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.4...v1.19.5) (2021-10-11)


### Documentation

* Clarify semantics of multiple oneof variants passed to msg ctor ([#263](https://www.github.com/googleapis/proto-plus-python/issues/263)) ([6f8a5b2](https://www.github.com/googleapis/proto-plus-python/commit/6f8a5b2098e4f6748945c53bda3d5821e62e5a0a))

## [1.19.4](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.3...v1.19.4) (2021-10-08)


### Documentation

* clarify that proto plus messages are not pickleable ([#260](https://www.github.com/googleapis/proto-plus-python/issues/260)) ([6e691dc](https://www.github.com/googleapis/proto-plus-python/commit/6e691dc27b1e540ef0661597fd89ece8f0155c97))

## [1.19.3](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.2...v1.19.3) (2021-10-07)


### Bug Fixes

* setting bytes field from python string base64 decodes before assignment ([#255](https://www.github.com/googleapis/proto-plus-python/issues/255)) ([b6f3eb6](https://www.github.com/googleapis/proto-plus-python/commit/b6f3eb6575484748126170997b8c98512763ea66))

## [1.19.2](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.1...v1.19.2) (2021-09-29)


### Bug Fixes

* ensure enums are hashable ([#252](https://www.github.com/googleapis/proto-plus-python/issues/252)) ([232341b](https://www.github.com/googleapis/proto-plus-python/commit/232341b4f4902fba1b3597bb1e1618b8f320374b))

## [1.19.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.19.0...v1.19.1) (2021-09-29)


### Bug Fixes

* ensure enums are incomparable w other enum types ([#248](https://www.github.com/googleapis/proto-plus-python/issues/248)) ([5927c14](https://www.github.com/googleapis/proto-plus-python/commit/5927c1400f400b3213c9b92e7a37c3c3a1abd681))

## [1.19.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.18.1...v1.19.0) (2021-06-29)


### Features

* pass 'including_default_value_fields' through to 'Message.to_dict' method ([#232](https://www.github.com/googleapis/proto-plus-python/issues/232)) ([15c2f47](https://www.github.com/googleapis/proto-plus-python/commit/15c2f479f81f0f80d451ca9b043e42cecfe7184e))

## [1.18.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.18.0...v1.18.1) (2021-03-19)


### Bug Fixes

* Add arm64 support for PY3.6 ([#219](https://www.github.com/googleapis/proto-plus-python/issues/219)) ([c9667c2](https://www.github.com/googleapis/proto-plus-python/commit/c9667c22d0b8f6026dbf69d502eb8eb972279891))

## [1.18.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.17.0...v1.18.0) (2021-03-16)


### Features

* add copy_from method for field assignment ([#215](https://www.github.com/googleapis/proto-plus-python/issues/215)) ([11c3e58](https://www.github.com/googleapis/proto-plus-python/commit/11c3e58a9ba59f0d7d808a26597dab735ca982ba))

## [1.17.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.16.0...v1.17.0) (2021-03-12)


### Features

* add preserving_proto_field_name to to_json ([#213](https://www.github.com/googleapis/proto-plus-python/issues/213)) ([b2c245b](https://www.github.com/googleapis/proto-plus-python/commit/b2c245bf044b964897f4e7423ff4944ae915e469))

## [1.16.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.15.0...v1.16.0) (2021-03-12)


### Features

* add preserving_proto_field_name passthrough in MessageMeta.to_dict ([#211](https://www.github.com/googleapis/proto-plus-python/issues/211)) ([7675a0c](https://www.github.com/googleapis/proto-plus-python/commit/7675a0c8d1004f2727d64100527f2b208d305017))

## [1.15.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.14.3...v1.15.0) (2021-03-10)


### Features

* allow_alias for enums ([#207](https://www.github.com/googleapis/proto-plus-python/issues/207)) ([6d4d713](https://www.github.com/googleapis/proto-plus-python/commit/6d4d71399f494b9f3bd47b6f3ef0b6d3c0c547b5))

## [1.14.3](https://www.github.com/googleapis/proto-plus-python/compare/v1.14.2...v1.14.3) (2021-03-04)


### Bug Fixes

* adding enums to a repeated field does not raise a TypeError ([#202](https://www.github.com/googleapis/proto-plus-python/issues/202)) ([2a10bbe](https://www.github.com/googleapis/proto-plus-python/commit/2a10bbecaf8955c7bf1956086aef42630112788b))

## [1.14.2](https://www.github.com/googleapis/proto-plus-python/compare/v1.14.1...v1.14.2) (2021-02-26)


### Bug Fixes

* use the correct environment for uploading to pypi ([#199](https://www.github.com/googleapis/proto-plus-python/issues/199)) ([babdc5c](https://www.github.com/googleapis/proto-plus-python/commit/babdc5cddf08235cac3cda66200babab44204688))

## [1.14.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.14.0...v1.14.1) (2021-02-26)


### Bug Fixes

* install the wheel dependency ([#197](https://www.github.com/googleapis/proto-plus-python/issues/197)) ([923ab31](https://www.github.com/googleapis/proto-plus-python/commit/923ab31e4685b47acae793198be55335e5eeae38))

## [1.14.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.13.1...v1.14.0) (2021-02-24)


### Features

* Pypi publish ghub actions ([#189](https://www.github.com/googleapis/proto-plus-python/issues/189)) ([4c967b0](https://www.github.com/googleapis/proto-plus-python/commit/4c967b0bb2ead29156bcc53c1f3b227b3afb2e8b))


### Bug Fixes

* proper __setitem__ and insert for RepeatedComposite ([#178](https://www.github.com/googleapis/proto-plus-python/issues/178)) ([1157a76](https://www.github.com/googleapis/proto-plus-python/commit/1157a76bb608d72389f46dc4d8e9aa00cc14ccc6))
* proper native marshal for repeated enumeration fields ([#180](https://www.github.com/googleapis/proto-plus-python/issues/180)) ([30265d6](https://www.github.com/googleapis/proto-plus-python/commit/30265d654d7f3589cbd0994d2ac564db1fd44265))

## [1.13.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.13.0...v1.13.1) (2021-02-09)


### Bug Fixes

* update docstring to match type hint ([#172](https://www.github.com/googleapis/proto-plus-python/issues/172)) ([14dad5b](https://www.github.com/googleapis/proto-plus-python/commit/14dad5bf6c5967a720e9d3095d621dbfe208b614))

## [1.13.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.12.0...v1.13.0) (2020-12-04)


### Features

* add 3.9 support and drop 3.5 ([#167](https://www.github.com/googleapis/proto-plus-python/issues/167)) ([6d17195](https://www.github.com/googleapis/proto-plus-python/commit/6d171956e14b398aece931b9dde1013be9644b74))

## [1.12.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.11.0...v1.12.0) (2020-11-20)


### Features

* add default values parameter to to_json ([#164](https://www.github.com/googleapis/proto-plus-python/issues/164)) ([691f1b2](https://www.github.com/googleapis/proto-plus-python/commit/691f1b24454502c4ac49a88a09d1c9fbc287b2bd))

## [1.11.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.10.2...v1.11.0) (2020-10-19)


### Features

* provide a to_dict method ([#154](https://www.github.com/googleapis/proto-plus-python/issues/154)) ([ccf903e](https://www.github.com/googleapis/proto-plus-python/commit/ccf903e3cddfcb1ff539e853594b4342914b7d61)), closes [#153](https://www.github.com/googleapis/proto-plus-python/issues/153) [#151](https://www.github.com/googleapis/proto-plus-python/issues/151)

## [1.10.2](https://www.github.com/googleapis/proto-plus-python/compare/v1.10.1...v1.10.2) (2020-10-14)


### Documentation

* explain how to use repeated struct.Value ([#148](https://www.github.com/googleapis/proto-plus-python/issues/148)) ([9634ea8](https://www.github.com/googleapis/proto-plus-python/commit/9634ea8fa464c0d34f13469016f23cc2e986d973)), closes [#104](https://www.github.com/googleapis/proto-plus-python/issues/104)

## [1.10.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.10.0...v1.10.1) (2020-10-08)


### Bug Fixes

* accessing an unset struct_pb2.Value field does not raise ([#140](https://www.github.com/googleapis/proto-plus-python/issues/140)) ([d045cbf](https://www.github.com/googleapis/proto-plus-python/commit/d045cbf058cbb8f4ca98dd06741270fcaee865be))
* add LICENSE and tests to package ([#146](https://www.github.com/googleapis/proto-plus-python/issues/146)) ([815c943](https://www.github.com/googleapis/proto-plus-python/commit/815c9439a1dadb2d4111784eb18ba673ce6e6cc2))

## [1.10.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.9.1...v1.10.0) (2020-09-24)


### Bug Fixes

* loosen tag match for publish_package ([#123](https://www.github.com/googleapis/proto-plus-python/issues/123)) ([67441c9](https://www.github.com/googleapis/proto-plus-python/commit/67441c931b5f00b2e1084ce2539784ae9d9c31e6))
* third party enums don't break first class enums ([#118](https://www.github.com/googleapis/proto-plus-python/issues/118)) ([50b87af](https://www.github.com/googleapis/proto-plus-python/commit/50b87af481bb1f19d10d64e88dc9ee39c2d5b6f8)), closes [#103](https://www.github.com/googleapis/proto-plus-python/issues/103)


## [1.10.0-dev2](https://www.github.com/googleapis/proto-plus-python/compare/v1.9.1...v1.10.0-dev2) (2020-09-21)


### Bug Fixes

* loosen tag match for publish_package ([#123](https://www.github.com/googleapis/proto-plus-python/issues/123)) ([67441c9](https://www.github.com/googleapis/proto-plus-python/commit/67441c931b5f00b2e1084ce2539784ae9d9c31e6))
* third party enums don't break first class enums ([#118](https://www.github.com/googleapis/proto-plus-python/issues/118)) ([50b87af](https://www.github.com/googleapis/proto-plus-python/commit/50b87af481bb1f19d10d64e88dc9ee39c2d5b6f8)), closes [#103](https://www.github.com/googleapis/proto-plus-python/issues/103)


## [1.9.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.9.0...v1.9.1) (2020-09-08)


### Reverts

* Revert "feat: json serialization and deserialization support stringy enums (#112)" (#116) ([91c6d7b](https://www.github.com/googleapis/proto-plus-python/commit/91c6d7bb27d198439bb323d2454fb94e197bf3dd)), closes [#112](https://www.github.com/googleapis/proto-plus-python/issues/112) [#116](https://www.github.com/googleapis/proto-plus-python/issues/116)


### Documentation

* update README ([#120](https://www.github.com/googleapis/proto-plus-python/issues/120)) ([2077390](https://www.github.com/googleapis/proto-plus-python/commit/2077390d614acb278ab94077f131a895d7184881))

## [1.9.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.8.1...v1.9.0) (2020-09-02)


### Features

* json serialization and deserialization support stringy enums ([#112](https://www.github.com/googleapis/proto-plus-python/issues/112)) ([8d2e3a3](https://www.github.com/googleapis/proto-plus-python/commit/8d2e3a3439650dab9ca7c6ff49ed067838a02a45)), closes [#107](https://www.github.com/googleapis/proto-plus-python/issues/107)

## [1.8.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.8.0...v1.8.1) (2020-08-28)


### Bug Fixes

* revert "feat: allow enum strings in json serialization and deserialization" ([#110](https://www.github.com/googleapis/proto-plus-python/issues/110)) ([bd3d50e](https://www.github.com/googleapis/proto-plus-python/commit/bd3d50e6b4d4574a21592f51adf7b248ededd545)), closes [#107](https://www.github.com/googleapis/proto-plus-python/issues/107)

## [1.8.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.7.1...v1.8.0) (2020-08-28)


### Features

* allow enum strings in json serialization and deserialization ([#107](https://www.github.com/googleapis/proto-plus-python/issues/107)) ([a082f85](https://www.github.com/googleapis/proto-plus-python/commit/a082f85ffcb72e2c53c0e33e40e6df2927a41259))

## [1.7.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.7.0...v1.7.1) (2020-08-17)


### Bug Fixes

* revert algorithm for RepeatedComposite insertion. ([#101](https://www.github.com/googleapis/proto-plus-python/issues/101)) ([ae946aa](https://www.github.com/googleapis/proto-plus-python/commit/ae946aa2a3b394fa31590224fcf50593bde0ccaa))

## [1.7.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.6.0...v1.7.0) (2020-08-07)


### Features

* optimize insert for class RepeatedComposite. ([#95](https://www.github.com/googleapis/proto-plus-python/issues/95)) ([86790e3](https://www.github.com/googleapis/proto-plus-python/commit/86790e3f7d891e13835699a4e1f50aec6140fa6e))

## [1.6.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.5.3...v1.6.0) (2020-08-05)


### Features

* more performance optimizations ([#92](https://www.github.com/googleapis/proto-plus-python/issues/92)) ([19b1519](https://www.github.com/googleapis/proto-plus-python/commit/19b151960de7c83ac82e670b06cb47d6e885f627))

## [1.5.3](https://www.github.com/googleapis/proto-plus-python/compare/v1.5.2...v1.5.3) (2020-08-04)


### Bug Fixes

* yet more perf tweaks ([#90](https://www.github.com/googleapis/proto-plus-python/issues/90)) ([eb7891c](https://www.github.com/googleapis/proto-plus-python/commit/eb7891cf05124803352b2f4fd719937356bf9167))

## [1.5.2](https://www.github.com/googleapis/proto-plus-python/compare/v1.5.1...v1.5.2) (2020-08-03)


### Bug Fixes

* tweak to_python ([#88](https://www.github.com/googleapis/proto-plus-python/issues/88)) ([5459ede](https://www.github.com/googleapis/proto-plus-python/commit/5459ede75597b06df5a211b0e317fb2c1f4b034e))

## [1.5.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.5.0...v1.5.1) (2020-07-30)


### Bug Fixes

* numerous small performance tweaks ([#85](https://www.github.com/googleapis/proto-plus-python/issues/85)) ([7b5faf2](https://www.github.com/googleapis/proto-plus-python/commit/7b5faf2e2c20c8022c83d6a99656505aa669200b))

## [1.5.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.4.2...v1.5.0) (2020-07-29)


### Features

* support fixed filename salt to allow proto-plus use with schema registry tools ([#61](https://www.github.com/googleapis/proto-plus-python/issues/61)) ([ea86eb9](https://www.github.com/googleapis/proto-plus-python/commit/ea86eb9ac694ed1f0e711698429449f41ecfedfc))

## [1.4.2](https://www.github.com/googleapis/proto-plus-python/compare/v1.4.1...v1.4.2) (2020-07-23)


### Bug Fixes

* getattr on an invalid field raises AttributeError ([#73](https://www.github.com/googleapis/proto-plus-python/issues/73)) ([74ea8f0](https://www.github.com/googleapis/proto-plus-python/commit/74ea8f0cd9083939e53d1de2450b649500281b9a)), closes [#31](https://www.github.com/googleapis/proto-plus-python/issues/31)

## [1.4.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.4.0...v1.4.1) (2020-07-23)


### Bug Fixes

* tweak publish ci task ([#65](https://www.github.com/googleapis/proto-plus-python/issues/65)) ([983189c](https://www.github.com/googleapis/proto-plus-python/commit/983189c5effa25fb9365eb63caddb425d3cfb2b5))

## [1.4.0](https://www.github.com/googleapis/proto-plus-python/compare/v1.3.2...v1.4.0) (2020-07-23)


### Features

* prevent unnecessary copies when deserializing proto ([#63](https://www.github.com/googleapis/proto-plus-python/issues/63)) ([5e1c061](https://www.github.com/googleapis/proto-plus-python/commit/5e1c0619b5f4c5d2a6a75ae6d45a53fef2e58823))

## [1.3.2](https://www.github.com/googleapis/proto-plus-python/compare/v1.3.1...v1.3.2) (2020-07-22)


### Bug Fixes

* correctly handle passed in vanilla datetime.datetime ([#57](https://www.github.com/googleapis/proto-plus-python/issues/57)) ([a770816](https://www.github.com/googleapis/proto-plus-python/commit/a770816197cbce60ee023bd5b6ee6bd2d970ded8)), closes [googleapis/gapic-generator-python#544](https://www.github.com/googleapis/gapic-generator-python/issues/544)
* update encrypted pypi passwd ([#58](https://www.github.com/googleapis/proto-plus-python/issues/58)) ([d985233](https://www.github.com/googleapis/proto-plus-python/commit/d9852336d83717cb9ff24b6bec3ef1463239fea1))

## [1.3.1](https://www.github.com/googleapis/proto-plus-python/compare/v1.3.0...v1.3.1) (2020-07-21)


### Bug Fixes

* tweak pypi circleci task ([#54](https://www.github.com/googleapis/proto-plus-python/issues/54)) ([89c49d7](https://www.github.com/googleapis/proto-plus-python/commit/89c49d700d4b6e9a434fbfced8ca39d430dd22f9))


### Documentation

* linkify pypi badge ([#50](https://www.github.com/googleapis/proto-plus-python/issues/50)) ([8ff08e2](https://www.github.com/googleapis/proto-plus-python/commit/8ff08e21e75570aad71c5e62f4c78b43139b5df2))

## [1.3.0](https://www.github.com/googleapis/proto-plus-python/compare/1.2.0...v1.3.0) (2020-07-16)


### Features

* add convenience methods to convert to/from json ([#39](https://www.github.com/googleapis/proto-plus-python/issues/39)) ([2868946](https://www.github.com/googleapis/proto-plus-python/commit/286894609843f568c9ff367ab79542783642b801))
* add DatetimeWithNanoseconds class to maintain Timestamp pb precision. ([#40](https://www.github.com/googleapis/proto-plus-python/issues/40)) ([a17ccd5](https://www.github.com/googleapis/proto-plus-python/commit/a17ccd52c7fa3609ce79fde84b931c0693f53171)), closes [#38](https://www.github.com/googleapis/proto-plus-python/issues/38)
* add support for proto3 optional fields ([#35](https://www.github.com/googleapis/proto-plus-python/issues/35)) ([0eb5762](https://www.github.com/googleapis/proto-plus-python/commit/0eb5762681e315635db1dffd583d91a4f32cba43))


### Bug Fixes

* Modify setup.py to indicate this is google maintained ([#45](https://www.github.com/googleapis/proto-plus-python/issues/45)) ([96b3b00](https://www.github.com/googleapis/proto-plus-python/commit/96b3b00dd6712fe44e71dedf8080b20544e95416))
