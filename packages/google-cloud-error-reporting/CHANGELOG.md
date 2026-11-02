# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-error-reporting/#history

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-error-reporting-v1.16.1...google-cloud-error-reporting-v1.17.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-error-reporting-v1.16.0...google-cloud-error-reporting-v1.16.1) (2026-08-21)


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-error-reporting-v1.15.0...google-cloud-error-reporting-v1.16.0) (2026-06-22)


### Features

* regenerate google-cloud-[e-i] packages ([#17079](https://github.com/googleapis/google-cloud-python/issues/17079)) ([5239b18](https://github.com/googleapis/google-cloud-python/commit/5239b1814f216676bf02dea08726313ad355439d))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-error-reporting-v1.14.0...google-cloud-error-reporting-v1.15.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:a38add811f7f139d6a385b22d283ad09ef305b8cf50382ef62f0ce690787f021 ([51f9aa03553afae0e4ae2232063eee0f8392c100](https://github.com/googleapis/google-cloud-python/commit/51f9aa03553afae0e4ae2232063eee0f8392c100))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.14.0](https://github.com/googleapis/python-error-reporting/compare/v1.13.0...v1.14.0) (2025-12-16)


### Features

* support mTLS certificates when available (#717) ([7e99258b41ddef55b63c70c7e31afced4ab30103](https://github.com/googleapis/python-error-reporting/commit/7e99258b41ddef55b63c70c7e31afced4ab30103))

## [1.13.0](https://github.com/googleapis/python-error-reporting/compare/v1.12.0...v1.13.0) (2025-11-12)


### Features

* Add support for Python 3.14 ([#712](https://github.com/googleapis/python-error-reporting/issues/712)) ([e8b4762](https://github.com/googleapis/python-error-reporting/commit/e8b4762d289755377acb7c69744a347fbe6651d6))


### Bug Fixes

* Deprecate credentials_file argument ([f86c964](https://github.com/googleapis/python-error-reporting/commit/f86c964200cc16488e46fdd95ad78e7975760b53))

## [1.12.0](https://github.com/googleapis/python-error-reporting/compare/v1.11.1...v1.12.0) (2025-05-21)


### Features

* Add REST Interceptors which support reading metadata ([1d120c7](https://github.com/googleapis/python-error-reporting/commit/1d120c77c73b566796b32cab017a0d4cdfa28713))
* Add support for opt-in debug logging ([1d120c7](https://github.com/googleapis/python-error-reporting/commit/1d120c77c73b566796b32cab017a0d4cdfa28713))


### Bug Fixes

* Allow Protobuf 6.x ([#557](https://github.com/googleapis/python-error-reporting/issues/557)) ([9f8faeb](https://github.com/googleapis/python-error-reporting/commit/9f8faeba223a0e1834c0750d21b5cafdee74d327))
* Fix typing issue with gRPC metadata when key ends in -bin ([1d120c7](https://github.com/googleapis/python-error-reporting/commit/1d120c77c73b566796b32cab017a0d4cdfa28713))
* Remove setup.cfg configuration for creating universal wheels ([#562](https://github.com/googleapis/python-error-reporting/issues/562)) ([0738c03](https://github.com/googleapis/python-error-reporting/commit/0738c03fa4321fd29c0915da2336bf77947367ae))
* Require proto-plus &gt;= 1.25.0 for Python 3.13 ([#567](https://github.com/googleapis/python-error-reporting/issues/567)) ([d5cd225](https://github.com/googleapis/python-error-reporting/commit/d5cd225fd71d8b54197c4f02c30d32eb8cd24dfa))

## [1.11.1](https://github.com/googleapis/python-error-reporting/compare/v1.11.0...v1.11.1) (2024-09-17)


### Bug Fixes

* Allow Protobuf 5.x ([#507](https://github.com/googleapis/python-error-reporting/issues/507)) ([8d33168](https://github.com/googleapis/python-error-reporting/commit/8d3316866c0825911b26f17fd4f703cabbc3c396))
* Retry and timeout values do not propagate in requests during pagination ([#518](https://github.com/googleapis/python-error-reporting/issues/518)) ([cbe41fd](https://github.com/googleapis/python-error-reporting/commit/cbe41fd1fa4edbb1c574cd2c07dc99d4415c3078))


### Documentation

* Add summary_overview template ([#496](https://github.com/googleapis/python-error-reporting/issues/496)) ([988def5](https://github.com/googleapis/python-error-reporting/commit/988def551df3f95577519450470a7cbf5f3b6b7d))
* Removes references as a "global-only" service ([1fef616](https://github.com/googleapis/python-error-reporting/commit/1fef61635e3f9d7297f9fe28d18568cf6c2a0fc1))
* Updates documentation with regional resource names for multiple requests ([1fef616](https://github.com/googleapis/python-error-reporting/commit/1fef61635e3f9d7297f9fe28d18568cf6c2a0fc1))

## [1.11.0](https://github.com/googleapis/python-error-reporting/compare/v1.10.0...v1.11.0) (2024-03-26)


### Features

* Allow users to explicitly configure universe domain ([#475](https://github.com/googleapis/python-error-reporting/issues/475)) ([e4c3454](https://github.com/googleapis/python-error-reporting/commit/e4c3454bd5ba9f452479b0bc956c6ef011766d14))

## [1.10.0](https://github.com/googleapis/python-error-reporting/compare/v1.9.2...v1.10.0) (2023-12-10)


### Features

* Add support for Python 3.12 ([#459](https://github.com/googleapis/python-error-reporting/issues/459)) ([36c1b59](https://github.com/googleapis/python-error-reporting/commit/36c1b598b35561e56815ce729884410134c3357d))
* Use native namespaces instead of pkg_resources ([#463](https://github.com/googleapis/python-error-reporting/issues/463)) ([a63e3f2](https://github.com/googleapis/python-error-reporting/commit/a63e3f25ce5ef0cd0077838cdbb6ceff0f15ce31))


### Bug Fixes

* Use `retry_async` instead of `retry` in async client ([#462](https://github.com/googleapis/python-error-reporting/issues/462)) ([44c2b14](https://github.com/googleapis/python-error-reporting/commit/44c2b146aec92e272134ebaa6945fe78f98753bd))


### Documentation

* Minor formatting ([#448](https://github.com/googleapis/python-error-reporting/issues/448)) ([48823d4](https://github.com/googleapis/python-error-reporting/commit/48823d4529fc2a2ac7b6c3f745c3ea5cb0ec9d38))

## [1.9.2](https://github.com/googleapis/python-error-reporting/compare/v1.9.1...v1.9.2) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#434](https://github.com/googleapis/python-error-reporting/issues/434)) ([319fa54](https://github.com/googleapis/python-error-reporting/commit/319fa54a19cb9aca3a079439fd7c6bd2c3163f71))

## [1.9.1](https://github.com/googleapis/python-error-reporting/compare/v1.9.0...v1.9.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#422](https://github.com/googleapis/python-error-reporting/issues/422)) ([561dc39](https://github.com/googleapis/python-error-reporting/commit/561dc395302f7989820db79f1c82aad04b7f6f7c))

## [1.9.0](https://github.com/googleapis/python-error-reporting/compare/v1.8.2...v1.9.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#418](https://github.com/googleapis/python-error-reporting/issues/418)) ([b2b9eab](https://github.com/googleapis/python-error-reporting/commit/b2b9eab649f413d7ad8a47fd660f9e2bcc32a820))

## [1.8.2](https://github.com/googleapis/python-error-reporting/compare/v1.8.1...v1.8.2) (2023-02-04)


### Documentation

* Removed link to the regionalization page ([#411](https://github.com/googleapis/python-error-reporting/issues/411)) ([3a0d82d](https://github.com/googleapis/python-error-reporting/commit/3a0d82db6a425b91430be0ee84fd9c957f39af00))

## [1.8.1](https://github.com/googleapis/python-error-reporting/compare/v1.8.0...v1.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([26a0749](https://github.com/googleapis/python-error-reporting/commit/26a074998b0c0a0697ed03086f7e1f6c4b77e35a))


### Documentation

* Add documentation for enums ([26a0749](https://github.com/googleapis/python-error-reporting/commit/26a074998b0c0a0697ed03086f7e1f6c4b77e35a))

## [1.8.0](https://github.com/googleapis/python-error-reporting/compare/v1.7.0...v1.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#405](https://github.com/googleapis/python-error-reporting/issues/405)) ([d5e0c4c](https://github.com/googleapis/python-error-reporting/commit/d5e0c4cf0cb40aab80146cad16141217b1998b30))

## [1.7.0](https://github.com/googleapis/python-error-reporting/compare/v1.6.3...v1.7.0) (2022-12-15)


### Features

* Add typing to proto.Message based class attributes ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))


### Bug Fixes

* Add dict typing for client_options ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))
* Drop usage of pkg_resources ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))
* Fix timeout default values ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([ccaa40f](https://github.com/googleapis/python-error-reporting/commit/ccaa40f1eca7d001cb58cd340189d521e93632ff))

## [1.6.3](https://github.com/googleapis/python-error-reporting/compare/v1.6.2...v1.6.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#391](https://github.com/googleapis/python-error-reporting/issues/391)) ([6a42c05](https://github.com/googleapis/python-error-reporting/commit/6a42c056a7535f4c43d7698525e19df655c91092))

## [1.6.2](https://github.com/googleapis/python-error-reporting/compare/v1.6.1...v1.6.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#388](https://github.com/googleapis/python-error-reporting/issues/388)) ([adde212](https://github.com/googleapis/python-error-reporting/commit/adde212c5c37ecbfac9a7ccda9e1fa027c670e52))

## [1.6.1](https://github.com/googleapis/python-error-reporting/compare/v1.6.0...v1.6.1) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#366](https://github.com/googleapis/python-error-reporting/issues/366)) ([9535a28](https://github.com/googleapis/python-error-reporting/commit/9535a289a458badf7406688d3e9a77f0e580d0a8))
* **deps:** require proto-plus >= 1.22.0 ([9535a28](https://github.com/googleapis/python-error-reporting/commit/9535a289a458badf7406688d3e9a77f0e580d0a8))

## [1.6.0](https://github.com/googleapis/python-error-reporting/compare/v1.5.3...v1.6.0) (2022-07-14)


### Features

* add audience parameter ([f53a2fa](https://github.com/googleapis/python-error-reporting/commit/f53a2fa49567035a1a3bb94d13444dd65bd104c6))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#354](https://github.com/googleapis/python-error-reporting/issues/354)) ([f53a2fa](https://github.com/googleapis/python-error-reporting/commit/f53a2fa49567035a1a3bb94d13444dd65bd104c6))
* require python 3.7+ ([#358](https://github.com/googleapis/python-error-reporting/issues/358)) ([ab0a9ba](https://github.com/googleapis/python-error-reporting/commit/ab0a9bacf9594ce3ff4c521413a20a2995533032))

## [1.5.3](https://github.com/googleapis/python-error-reporting/compare/v1.5.2...v1.5.3) (2022-06-07)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#347](https://github.com/googleapis/python-error-reporting/issues/347)) ([ad4c778](https://github.com/googleapis/python-error-reporting/commit/ad4c778e290eb76ea1d62252b5e115ca4c30d42c))


### Documentation

* fix changelog header to consistent size ([#346](https://github.com/googleapis/python-error-reporting/issues/346)) ([6dc90f7](https://github.com/googleapis/python-error-reporting/commit/6dc90f7e8978c06899c50f1897c160f5e253be79))

## [1.5.2](https://github.com/googleapis/python-error-reporting/compare/v1.5.1...v1.5.2) (2022-04-16)


### Bug Fixes

* Reenable staleness bot ([#264](https://github.com/googleapis/python-error-reporting/issues/264)) ([393141a](https://github.com/googleapis/python-error-reporting/commit/393141ac2c661485fdafb8f21fe13a6b2c854d07))

## [1.5.1](https://github.com/googleapis/python-error-reporting/compare/v1.5.0...v1.5.1) (2022-03-07)


### Bug Fixes

* **deps:** allow google-cloud-logging <4.0.0dev ([#244](https://github.com/googleapis/python-error-reporting/issues/244)) ([b2f83cf](https://github.com/googleapis/python-error-reporting/commit/b2f83cfb02792d4dfd1d881a07460d90e0ad4eb0))
* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#241](https://github.com/googleapis/python-error-reporting/issues/241)) ([af66168](https://github.com/googleapis/python-error-reporting/commit/af66168f3926d63161070bbd3b6c6880155cf07d))
* **deps:** require proto-plus>=1.15.0 ([af66168](https://github.com/googleapis/python-error-reporting/commit/af66168f3926d63161070bbd3b6c6880155cf07d))

## [1.5.0](https://github.com/googleapis/python-error-reporting/compare/v1.4.1...v1.5.0) (2022-02-16)


### Features

* add api key support ([#221](https://github.com/googleapis/python-error-reporting/issues/221)) ([b207f2c](https://github.com/googleapis/python-error-reporting/commit/b207f2cec4f5f3196e775ed35cd429f34f9c0bd1))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([f0afcae](https://github.com/googleapis/python-error-reporting/commit/f0afcae54c834872d1e40d1f5c948c1e0c299b85))

## [1.4.1](https://www.github.com/googleapis/python-error-reporting/compare/v1.4.0...v1.4.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([31e3d6b](https://www.github.com/googleapis/python-error-reporting/commit/31e3d6b269139831e914165a316b450c01bc6c0d))
* **deps:** require google-api-core >= 1.28.0 ([31e3d6b](https://www.github.com/googleapis/python-error-reporting/commit/31e3d6b269139831e914165a316b450c01bc6c0d))


### Documentation

* list oneofs in docstring ([31e3d6b](https://www.github.com/googleapis/python-error-reporting/commit/31e3d6b269139831e914165a316b450c01bc6c0d))

## [1.4.0](https://www.github.com/googleapis/python-error-reporting/compare/v1.3.0...v1.4.0) (2021-10-14)


### Features

* add support for python 3.10 ([#192](https://www.github.com/googleapis/python-error-reporting/issues/192)) ([76cc041](https://www.github.com/googleapis/python-error-reporting/commit/76cc041c367d05a361c2fce355340e01bae116ed))

## [1.3.0](https://www.github.com/googleapis/python-error-reporting/compare/v1.2.3...v1.3.0) (2021-10-11)


### Features

* add context manager support in client ([#187](https://www.github.com/googleapis/python-error-reporting/issues/187)) ([a4e2cd4](https://www.github.com/googleapis/python-error-reporting/commit/a4e2cd4654ae6b3f785727e279ce362798368598))


### Bug Fixes

* exception thrown when grpc is disabled ([#190](https://www.github.com/googleapis/python-error-reporting/issues/190)) ([929e293](https://www.github.com/googleapis/python-error-reporting/commit/929e293a479dea3059bfca152b93d7740348fc39))
* improper types in pagers generation ([18c93a9](https://www.github.com/googleapis/python-error-reporting/commit/18c93a99a967b6d86e7409f4e26ff56f1c9788de))

## [1.2.3](https://www.github.com/googleapis/python-error-reporting/compare/v1.2.2...v1.2.3) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([253a66f](https://www.github.com/googleapis/python-error-reporting/commit/253a66f5f606f722bf5401cdd678989b9d2baa98))

## [1.2.2](https://www.github.com/googleapis/python-error-reporting/compare/v1.2.1...v1.2.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#156](https://www.github.com/googleapis/python-error-reporting/issues/156)) ([f9656c8](https://www.github.com/googleapis/python-error-reporting/commit/f9656c81db2f29ba4ac9ba4a5304004cd725ca5c))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#151](https://www.github.com/googleapis/python-error-reporting/issues/151)) ([8f11190](https://www.github.com/googleapis/python-error-reporting/commit/8f11190661e62165bd1c4a30b40797ef31abed33))


### Miscellaneous Chores

* release as 1.2.2 ([#157](https://www.github.com/googleapis/python-error-reporting/issues/157)) ([ea26377](https://www.github.com/googleapis/python-error-reporting/commit/ea2637721efac36b122edc499da08c12ae894d28))

## [1.2.1](https://www.github.com/googleapis/python-error-reporting/compare/v1.2.0...v1.2.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#150](https://www.github.com/googleapis/python-error-reporting/issues/150)) ([1c87673](https://www.github.com/googleapis/python-error-reporting/commit/1c876738b0bdca1b2bd65d78fa541846b0474cfa))

## [1.2.0](https://www.github.com/googleapis/python-error-reporting/compare/v1.1.2...v1.2.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#140](https://www.github.com/googleapis/python-error-reporting/issues/140)) ([2f8f790](https://www.github.com/googleapis/python-error-reporting/commit/2f8f790dd70646848afd5e5209a147b01c6f388b))


### Bug Fixes

* **deps:** add packaging requirement ([#124](https://www.github.com/googleapis/python-error-reporting/issues/124)) ([ed36389](https://www.github.com/googleapis/python-error-reporting/commit/ed3638946f8829c4d2b379785e38cc2a2228c688))
* **deps:** widen version range on google-cloud-logging ([#133](https://www.github.com/googleapis/python-error-reporting/issues/133)) ([c5e87bb](https://www.github.com/googleapis/python-error-reporting/commit/c5e87bb8c177688833ca9524daa4e6229875627d))
* disable always_use_jwt_access ([8aff323](https://www.github.com/googleapis/python-error-reporting/commit/8aff32330ebf544cc043bec0003140d61df7e7a1))
* disable always_use_jwt_access ([#144](https://www.github.com/googleapis/python-error-reporting/issues/144)) ([8aff323](https://www.github.com/googleapis/python-error-reporting/commit/8aff32330ebf544cc043bec0003140d61df7e7a1))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-error-reporting/issues/1127)) ([#137](https://www.github.com/googleapis/python-error-reporting/issues/137)) ([0ca7d43](https://www.github.com/googleapis/python-error-reporting/commit/0ca7d4385de86e7ff462322807a717345774c017))

## [1.1.2](https://www.github.com/googleapis/python-error-reporting/compare/v1.1.1...v1.1.2) (2021-04-05)


### Dependencies

* upgrade sphinx ([#99](https://www.github.com/googleapis/python-error-reporting/issues/99)) ([a118123](https://www.github.com/googleapis/python-error-reporting/commit/a118123cbfe8b5dd2a7ba260631b248c351cb116))

## [1.1.1](https://www.github.com/googleapis/python-error-reporting/compare/v1.1.0...v1.1.1) (2021-02-25)


### Bug Fixes

* remove gRPC send/recv limit; add enums to `types/__init__.py` ([#57](https://www.github.com/googleapis/python-error-reporting/issues/57)) ([e23e5ba](https://www.github.com/googleapis/python-error-reporting/commit/e23e5ba7eba4482735d5f4897210a1ebb81bfb8a))

## [1.1.0](https://www.github.com/googleapis/python-error-reporting/compare/v1.0.0...v1.1.0) (2020-12-01)


### Features

* add common resource path helpers; expose client transport as property ([#37](https://www.github.com/googleapis/python-error-reporting/issues/37)) ([bc92bc2](https://www.github.com/googleapis/python-error-reporting/commit/bc92bc2cfa549200bf8fa87cf2f6d81ded77486c))


### Bug Fixes

* changed import path for logging client ([#43](https://www.github.com/googleapis/python-error-reporting/issues/43)) ([a09449d](https://www.github.com/googleapis/python-error-reporting/commit/a09449def35077beb85782c34a61c8f172c2f018))


### Documentation

* removed stackdriver branding ([#44](https://www.github.com/googleapis/python-error-reporting/issues/44)) ([5eea8c4](https://www.github.com/googleapis/python-error-reporting/commit/5eea8c4f533a32d2b81b1b69e48d3bb47f1bc5b4))

## [1.0.0](https://www.github.com/googleapis/python-error-reporting/compare/v0.34.0...v1.0.0) (2020-08-28)


### ⚠ BREAKING CHANGES

* migrate to use microgen (#23)

### Features

* migrate to use microgen ([#23](https://www.github.com/googleapis/python-error-reporting/issues/23)) ([cb41e3a](https://www.github.com/googleapis/python-error-reporting/commit/cb41e3a1003cb4ef4e32efc8b5c5b5ba7d670f7d))


### Documentation

* add multiprocessing note ([#13](https://www.github.com/googleapis/python-error-reporting/issues/13)) ([840d67c](https://www.github.com/googleapis/python-error-reporting/commit/840d67c09502ae99ce4771c66bde1cefb961a367))

## [0.34.0](https://www.github.com/googleapis/python-error-reporting/compare/v0.33.0...v0.34.0) (2020-05-03)


### Features

* set release_status to beta ([#5](https://www.github.com/googleapis/python-error-reporting/issues/5)) ([e9361c5](https://www.github.com/googleapis/python-error-reporting/commit/e9361c5e0f427a4796974fd4a3da506324220e9e))

## 0.33.0

10-22-2019 12:10 PDT

### New Features
- Add `client_options` to constructor ([#9152](https://github.com/googleapis/google-cloud-python/pull/9152))

### Dependencies
- Pin `google-cloud-logging >= 1.14.0, < 2.0.0dev`. ([#9476](https://github.com/googleapis/google-cloud-python/pull/9476))

### Documentation
- Remove references to the old authentication credentials. ([#9456](https://github.com/googleapis/google-cloud-python/pull/9456))
- Fix intersphinx reference to requests. ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Remove CI for `gh-pages`, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))

### Internal / Testing Changes
- Harden `test_report_exception` systest by increasing `max_tries`. ([#9396](https://github.com/googleapis/google-cloud-python/pull/9396))

## 0.32.1

08-23-2019 10:12 PDT

### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8954](https://github.com/googleapis/google-cloud-python/pull/8954))

### Documentation
- Fix documentation links for iam and error-reporting. ([#9073](https://github.com/googleapis/google-cloud-python/pull/9073))
- Remove compatability badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 0.32.0

07-24-2019 16:17 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8389](https://github.com/googleapis/google-cloud-python/pull/8389))
- Fix typo in non-gRPC import. ([#8028](https://github.com/googleapis/google-cloud-python/pull/8028))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8508](https://github.com/googleapis/google-cloud-python/pull/8508))

### Documentation
- Fix docs navigation issues. ([#8723](https://github.com/googleapis/google-cloud-python/pull/8723))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Fix mistake in documentation ([#8271](https://github.com/googleapis/google-cloud-python/pull/8271))

### Internal / Testing Changes
- Pin black version (via synth). ([#8582](https://github.com/googleapis/google-cloud-python/pull/8582))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8351](https://github.com/googleapis/google-cloud-python/pull/8351))
- Add disclaimer to auto-generated template files (via synth). ([#8313](https://github.com/googleapis/google-cloud-python/pull/8313))
- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8240](https://github.com/googleapis/google-cloud-python/pull/8240))
- Blacken noxfile.py, setup.py (via synth). ([#8122](https://github.com/googleapis/google-cloud-python/pull/8122))
- Add empty lines (via synth). ([#8057](https://github.com/googleapis/google-cloud-python/pull/8057))

## 0.31.0

05-17-2019 08:23 PDT

### Implementation Changes
- Add routing header to method metadata (via synth). ([#7594](https://github.com/googleapis/google-cloud-python/pull/7594))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Add `client_info` support to Client. ([#7903](https://github.com/googleapis/google-cloud-python/pull/7903))

### Dependencies
- Pin `google-cloud-logging >= 1.11.0`. ([#8015](https://github.com/googleapis/google-cloud-python/pull/8015))

### Documentation
- Update client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))

### Internal / Testing Changes
- Add nox session `docs` (via synth). ([#7770](https://github.com/googleapis/google-cloud-python/pull/7770))
- Fix docstring replace in synth ([#7458](https://github.com/googleapis/google-cloud-python/pull/7458))
- Copy lintified proto files (via synth). ([#7447](https://github.com/googleapis/google-cloud-python/pull/7447))
- Add clarifying comment to blacken nox target (via synth). ([#7391](https://github.com/googleapis/google-cloud-python/pull/7391))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers. ([#7144](https://github.com/googleapis/google-cloud-python/pull/7144))
- Protoc-generated serialization update. ([#7082](https://github.com/googleapis/google-cloud-python/pull/7082))
- Pick up stub docstring fix in GAPIC generator. ([#6970](https://github.com/googleapis/google-cloud-python/pull/6970))
- Fix formatting ([#7002](https://github.com/googleapis/google-cloud-python/pull/7002))

## 0.30.1

12-17-2018 18:17 PST


### Implementation Changes
- Pick up fixes to GAPIC generator. ([#6522](https://github.com/googleapis/google-cloud-python/pull/6522))
- Fix `client_info` bug, update docstrings via synth. ([#6442](https://github.com/googleapis/google-cloud-python/pull/6442))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Fix [#6321](https://github.com/googleapis/google-cloud-python/pull/6321) Update README service links in quickstart guides. ([#6322](https://github.com/googleapis/google-cloud-python/pull/6322))
- Prep docs for repo split. ([#6155](https://github.com/googleapis/google-cloud-python/pull/6155))
- Replace links to `/stable/` with `/latest/`. ([#5901](https://github.com/googleapis/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add synth metadata. ([#6566](https://github.com/googleapis/google-cloud-python/pull/6566))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Add 'synth.py'. ([#6082](https://github.com/googleapis/google-cloud-python/pull/6082))
- Use Nox inplace installs ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))

## 0.30.0

### Implementation Changes
- Make dependency on logging less restrictive in error_reporting (#5345)

### Internal / Testing Changes
- Modify system tests to use prerelease versions of grpcio (#5304)
- Add Test runs for Python 3.7 and remove 3.4 (#5295)
- Fix bad trove classifier

## 0.29.1

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)
- Fix missing extra in api-core dependency (#4764)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)

## 0.29.0

### Breaking changes

- The underlying autogenerated client library was re-generated to pick up new 
  features and resolve bugs, this may change the exceptions raised from various
  methods. (#4695)

## 0.28.0

### Documentation

- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)
- Upgrading to `google-cloud-logging >= 1.4.0` (#4296)

PyPI: https://pypi.org/project/google-cloud-error-reporting/0.28.0/
