# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-ndb/#history

## [2.7.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.7.0...google-cloud-ndb-v2.7.1) (2026-10-01)


### Bug Fixes

* repair broken and stale repository URLs in package metadata ([#18498](https://github.com/googleapis/google-cloud-python/issues/18498)) ([54dbd12](https://github.com/googleapis/google-cloud-python/commit/54dbd12056abcfc007b5b76006751c3b11bea99f)), refs [#18497](https://github.com/googleapis/google-cloud-python/issues/18497)

## [2.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.6.1...google-cloud-ndb-v2.7.0) (2026-09-29)


### Features

* declare Python3.15 support ([05b0c34](https://github.com/googleapis/google-cloud-python/commit/05b0c342683b2b0e1b8dccd201ec86ec89612edc))

## [2.6.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.6.0...google-cloud-ndb-v2.6.1) (2026-09-24)


### Bug Fixes

* **google-cloud-ndb:** allow redis 8.x ([#18438](https://github.com/googleapis/google-cloud-python/issues/18438)) ([9630fe4](https://github.com/googleapis/google-cloud-python/commit/9630fe4a3076d1c05334615314ecc2101e65ea9b))

## [2.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.5.1...google-cloud-ndb-v2.6.0) (2026-08-21)


### Features

* check python and dependency versions in bigquery and ndb ([#18075](https://github.com/googleapis/google-cloud-python/issues/18075)) ([62ff6f3](https://github.com/googleapis/google-cloud-python/commit/62ff6f37f04de1b8a88876bfc1ac379573e42b36))


### Bug Fixes

* **ndb:** avoid unbound lock in delete callback ([#17969](https://github.com/googleapis/google-cloud-python/issues/17969)) ([c513b39](https://github.com/googleapis/google-cloud-python/commit/c513b397eb3514eaec81e26e6cf044a92b57cf23))
* **ndb:** use the single-argument generator.throw() signature ([#18159](https://github.com/googleapis/google-cloud-python/issues/18159)) ([dfb0e36](https://github.com/googleapis/google-cloud-python/commit/dfb0e36f3ac9089364bf4a638694e70514b18b51))


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [2.5.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.5.0...google-cloud-ndb-v2.5.1) (2026-08-06)


### Bug Fixes

* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [2.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.4.2...google-cloud-ndb-v2.5.0) (2026-05-06)


### Features

* enable mypy session for ndb (#16691) ([192ccc52a030a59f7e2c49ed9701130156d73d6f](https://github.com/googleapis/google-cloud-python/commit/192ccc52a030a59f7e2c49ed9701130156d73d6f))


### Bug Fixes

* Drop support for Python 3.9 (#16950) ([d37a95301da1db1ee1be273d2ac9af320c91809f](https://github.com/googleapis/google-cloud-python/commit/d37a95301da1db1ee1be273d2ac9af320c91809f))

## [2.4.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.4.1...google-cloud-ndb-v2.4.2) (2026-04-02)


### Bug Fixes

* allow redis 7.x (#16533) ([4c541cf2a364ef7ba39bc48c0a6a063a9334d31a](https://github.com/googleapis/google-cloud-python/commit/4c541cf2a364ef7ba39bc48c0a6a063a9334d31a))

## [2.4.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.4.0...google-cloud-ndb-v2.4.1) (2026-03-26)


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [2.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-ndb-v2.3.4...google-cloud-ndb-v2.4.0) (2025-12-15)


### Features

* Add support for Python 3.14 (#1028) ([947ff9b73c516f18b0411b828d45eb4bd8b95d39](https://github.com/googleapis/google-cloud-python/commit/947ff9b73c516f18b0411b828d45eb4bd8b95d39))

## [2.3.4](https://github.com/googleapis/python-ndb/compare/v2.3.3...v2.3.4) (2025-06-11)


### Bug Fixes

* Allow protobuf 6.x, allow redis 6.x ([#1013](https://github.com/googleapis/python-ndb/issues/1013)) ([b3684fe](https://github.com/googleapis/python-ndb/commit/b3684fe46c13b5d39deccc456f544b0f6f473d91))

## [2.3.3](https://github.com/googleapis/python-ndb/compare/v2.3.2...v2.3.3) (2025-05-09)


### Bug Fixes

* Support sub-meanings for datastore v2.20.3 ([#1014](https://github.com/googleapis/python-ndb/issues/1014)) ([88f14fa](https://github.com/googleapis/python-ndb/commit/88f14fa462b7f7caf72688374682bb1b7a2d933c))

## [2.3.2](https://github.com/googleapis/python-ndb/compare/v2.3.1...v2.3.2) (2024-07-15)


### Bug Fixes

* Allow Protobuf 5.x ([#991](https://github.com/googleapis/python-ndb/issues/991)) ([5812a3c](https://github.com/googleapis/python-ndb/commit/5812a3c2833ef9edda1726645e32789752474bd6))

## [2.3.1](https://github.com/googleapis/python-ndb/compare/v2.3.0...v2.3.1) (2024-03-16)


### Bug Fixes

* **grpc:** Fix large payload handling when using the emulator. ([#975](https://github.com/googleapis/python-ndb/issues/975)) ([d9162ae](https://github.com/googleapis/python-ndb/commit/d9162aee709062683bf5f9f01208bd40f46d490a))
* Remove uses of six. [#913](https://github.com/googleapis/python-ndb/issues/913) ([#958](https://github.com/googleapis/python-ndb/issues/958)) ([e17129a](https://github.com/googleapis/python-ndb/commit/e17129a2114c3f5d45b99cc9a4911b586eb3fafa))
* Show a non-None error for core_exception.Unknown errors. ([#968](https://github.com/googleapis/python-ndb/issues/968)) ([66e61cc](https://github.com/googleapis/python-ndb/commit/66e61cc578335509d480650906528fa390f44c11))


### Documentation

* Document how to run system tests against the emulator. ([#963](https://github.com/googleapis/python-ndb/issues/963)) ([47db5b9](https://github.com/googleapis/python-ndb/commit/47db5b9f6ee1fc7c01ad86d476cd8e066fb5cffb))
* Note to use functools.wrap instead of utils.wrapping. ([#966](https://github.com/googleapis/python-ndb/issues/966)) ([5e9f3d6](https://github.com/googleapis/python-ndb/commit/5e9f3d6977677c20b3447f07bf8bcf4553aac076))
* Tell users of utils.wrapping to use functools.wraps ([#967](https://github.com/googleapis/python-ndb/issues/967)) ([042645b](https://github.com/googleapis/python-ndb/commit/042645b52608a1c11645dd4b014a90040468b113))

## [2.3.0](https://github.com/googleapis/python-ndb/compare/v2.2.2...v2.3.0) (2024-03-01)


### Features

* Add field information when raising validation errors. ([#956](https://github.com/googleapis/python-ndb/issues/956)) ([17caf0b](https://github.com/googleapis/python-ndb/commit/17caf0b5f7d0c4d18522f676c8af990b8ff8462d))
* Add Python 3.12 ([#949](https://github.com/googleapis/python-ndb/issues/949)) ([b5c8477](https://github.com/googleapis/python-ndb/commit/b5c847783b80071c2dd9e9a3dbf899230c99e64a))
* Add support for google.cloud.ndb.__version__ ([#929](https://github.com/googleapis/python-ndb/issues/929)) ([42b3f01](https://github.com/googleapis/python-ndb/commit/42b3f0137caed25ac3242435b571155d2d84c78e))
* Add support for server side NOT_IN filter. ([#957](https://github.com/googleapis/python-ndb/issues/957)) ([f0b0724](https://github.com/googleapis/python-ndb/commit/f0b0724d7e364cc3f3574e77076465657089b09c))
* Allow queries using server side IN. ([#954](https://github.com/googleapis/python-ndb/issues/954)) ([2646cef](https://github.com/googleapis/python-ndb/commit/2646cef3e2687461174a11c45f29de7b84d1fcdb))
* Introduce compatibility with native namespace packages ([#933](https://github.com/googleapis/python-ndb/issues/933)) ([ccae387](https://github.com/googleapis/python-ndb/commit/ccae387720a28db2686e69dfe23a2599fc4908f0))
* Use server side != for queries. ([#950](https://github.com/googleapis/python-ndb/issues/950)) ([106772f](https://github.com/googleapis/python-ndb/commit/106772f031f6c37500a0d463698e59008f9bf19a))


### Bug Fixes

* Compressed repeated to uncompressed property ([#772](https://github.com/googleapis/python-ndb/issues/772)) ([dab9edf](https://github.com/googleapis/python-ndb/commit/dab9edf0fc161051eb13c296cbe973b3a16b502d))
* Repeated structured property containing blob property with legacy_data ([#817](https://github.com/googleapis/python-ndb/issues/817)) ([#946](https://github.com/googleapis/python-ndb/issues/946)) ([455f860](https://github.com/googleapis/python-ndb/commit/455f860343ff1b71232dad98cf91415492a899ca))


### Documentation

* **__init__:** Note that Firestore in Datastore Mode is supported ([#919](https://github.com/googleapis/python-ndb/issues/919)) ([0fa75e7](https://github.com/googleapis/python-ndb/commit/0fa75e71dfc6d56d2c0eaf214a48774b99bb959f))
* Correct read_consistency docs. ([#948](https://github.com/googleapis/python-ndb/issues/948)) ([7e8481d](https://github.com/googleapis/python-ndb/commit/7e8481db84a6d0b96cf09c38e90f47d6b7847a0b))
* Fix a mistaken ID description ([#943](https://github.com/googleapis/python-ndb/issues/943)) ([5103813](https://github.com/googleapis/python-ndb/commit/51038139e45807b3a14346ded702fbe202dcfdf2))
* Show how to use named databases ([#932](https://github.com/googleapis/python-ndb/issues/932)) ([182fe4e](https://github.com/googleapis/python-ndb/commit/182fe4e2d295768aaf016f94cb43b6b1e5572ebd))

## [2.2.2](https://github.com/googleapis/python-ndb/compare/v2.2.1...v2.2.2) (2023-09-19)


### Documentation

* **query:** Document deprecation of Query.default_options ([#915](https://github.com/googleapis/python-ndb/issues/915)) ([a656719](https://github.com/googleapis/python-ndb/commit/a656719d8a4f20a8b8dc564a1e3837a2cfb037c4)), closes [#880](https://github.com/googleapis/python-ndb/issues/880)

## [2.2.1](https://github.com/googleapis/python-ndb/compare/v2.2.0...v2.2.1) (2023-09-15)


### Bug Fixes

* **deps:** Add missing six dependency ([#912](https://github.com/googleapis/python-ndb/issues/912)) ([3b1ffb7](https://github.com/googleapis/python-ndb/commit/3b1ffb7e5cabdadfe2a4be6802adef774eec5ef8))


### Documentation

* Mark database argument for get_by_id and its async counterpart as ignored ([#905](https://github.com/googleapis/python-ndb/issues/905)) ([b0f4310](https://github.com/googleapis/python-ndb/commit/b0f431048b7b2ebb20e4255340290c7687e27425))

## [2.2.0](https://github.com/googleapis/python-ndb/compare/v2.1.1...v2.2.0) (2023-07-26)


### Features

* Named db support ([#882](https://github.com/googleapis/python-ndb/issues/882)) ([f5713b0](https://github.com/googleapis/python-ndb/commit/f5713b0e36e54ef69e9fa7e99975f32870832f65))


### Documentation

* **query:** Fix Py2-style print statements ([#878](https://github.com/googleapis/python-ndb/issues/878)) ([a3a181a](https://github.com/googleapis/python-ndb/commit/a3a181a427cc292882691d963b30bc78c05c6592))

## [2.1.1](https://github.com/googleapis/python-ndb/compare/v2.1.0...v2.1.1) (2023-02-28)


### Bug Fixes

* Query options were not respecting use_cache ([#873](https://github.com/googleapis/python-ndb/issues/873)) ([802d88d](https://github.com/googleapis/python-ndb/commit/802d88d108969cba02437f55e5858556221930f3)), closes [#752](https://github.com/googleapis/python-ndb/issues/752)


### Documentation

* Note that we support Python 3.11 in CONTRIBUTING file ([#872](https://github.com/googleapis/python-ndb/issues/872)) ([982ee5f](https://github.com/googleapis/python-ndb/commit/982ee5f9e768c6f7f5ef19bf6fe9e646e4e08e1f))
* Use cached versions of Cloud objects.inv files ([#863](https://github.com/googleapis/python-ndb/issues/863)) ([4471e2f](https://github.com/googleapis/python-ndb/commit/4471e2f11757be280266779544c59c90222b8184)), closes [#862](https://github.com/googleapis/python-ndb/issues/862)

## [2.1.0](https://github.com/googleapis/python-ndb/compare/v2.0.0...v2.1.0) (2022-12-15)


### Features

* Support client_options for clients ([#815](https://github.com/googleapis/python-ndb/issues/815)) ([6f94f40](https://github.com/googleapis/python-ndb/commit/6f94f40dfcd6f10e3cec979e4eb2b83408c66a30))


### Bug Fixes

* **zlib:** Accomodate different Zlib compression levels ([#852](https://github.com/googleapis/python-ndb/issues/852)) ([c1ab83b](https://github.com/googleapis/python-ndb/commit/c1ab83b9581b3d4d10dc7d2508b1c93b14e3c31a))

## [2.0.0](https://github.com/googleapis/python-ndb/compare/v1.12.0...v2.0.0) (2022-12-06)


### ⚠ BREAKING CHANGES

* **dependencies:** Upgrade to google-cloud-datastore >= 2.7.2

### Features

* **dependencies:** Upgrade to google-cloud-datastore &gt;= 2.7.2 ([12bbcb5](https://github.com/googleapis/python-ndb/commit/12bbcb548c47803406246d6e3cf55cd947b1500a))


### Bug Fixes

* Correct access to SerializeToString, CopyFrom, and MergeFromString ([12bbcb5](https://github.com/googleapis/python-ndb/commit/12bbcb548c47803406246d6e3cf55cd947b1500a))
* Fix enum namespaces ([12bbcb5](https://github.com/googleapis/python-ndb/commit/12bbcb548c47803406246d6e3cf55cd947b1500a))
* Update API capitalization/casing ([12bbcb5](https://github.com/googleapis/python-ndb/commit/12bbcb548c47803406246d6e3cf55cd947b1500a))
* Update datastore stub creation ([12bbcb5](https://github.com/googleapis/python-ndb/commit/12bbcb548c47803406246d6e3cf55cd947b1500a))
* Update module imports ([12bbcb5](https://github.com/googleapis/python-ndb/commit/12bbcb548c47803406246d6e3cf55cd947b1500a))

## [1.12.0](https://github.com/googleapis/python-ndb/compare/v1.11.2...v1.12.0) (2022-11-29)


### Bug Fixes

* Drop Python 2 support ([90efd77](https://github.com/googleapis/python-ndb/commit/90efd77633c97f530088dc3f079547ef4eefd796))
* Drop Python 3.6 support ([#829](https://github.com/googleapis/python-ndb/issues/829)) ([b110199](https://github.com/googleapis/python-ndb/commit/b1101994a34f70804027ea0c8a1b9f276d260756))
* **model:** Ensure repeated props have same kind when converting from ds ([#824](https://github.com/googleapis/python-ndb/issues/824)) ([29f5a85](https://github.com/googleapis/python-ndb/commit/29f5a853174857545e225fe2f0c682dfa0bc3884))


### Documentation

* Add note in Django middleware documentation that it is unimplemented ([#805](https://github.com/googleapis/python-ndb/issues/805)) ([aa7621d](https://github.com/googleapis/python-ndb/commit/aa7621dba3b5c32141cdcb1d07829a217bb8b0bd))
* Add note that ProtoRPC message classes are unimplemented ([#819](https://github.com/googleapis/python-ndb/issues/819)) ([ae813e9](https://github.com/googleapis/python-ndb/commit/ae813e9995d103a45a0c7bc6b4c7bdc148c19c29))
* **context:** Note that several methods are no longer implemented. ([#821](https://github.com/googleapis/python-ndb/issues/821)) ([34c2c38](https://github.com/googleapis/python-ndb/commit/34c2c389d02f4692840631d34b6249b88867d725))
* **CONTRIBUTING:** Note the need for Redis/Memcached env vars in tests ([#838](https://github.com/googleapis/python-ndb/issues/838)) ([19f8415](https://github.com/googleapis/python-ndb/commit/19f84150ab06ae71e25ee48ba7f7285eb0402738)), closes [#836](https://github.com/googleapis/python-ndb/issues/836)
* Fix bad import path in migration guide ([#827](https://github.com/googleapis/python-ndb/issues/827)) ([7b44961](https://github.com/googleapis/python-ndb/commit/7b449615629b5a08836ee17a8ab34eb8efbaed21))
* Fix typo in begin_transaction docstring ([#822](https://github.com/googleapis/python-ndb/issues/822)) ([7fd3ed3](https://github.com/googleapis/python-ndb/commit/7fd3ed315d39a9a50746b00898b22edd3f7d1d0c))
* **README:** Syncronize supported version text with python-datastore ([#837](https://github.com/googleapis/python-ndb/issues/837)) ([316f959](https://github.com/googleapis/python-ndb/commit/316f95913f2dca12f314e429bbe8bd2582bc1c0f))
* **tasklets:** Fix Py2-style print statement ([#840](https://github.com/googleapis/python-ndb/issues/840)) ([0ebfaed](https://github.com/googleapis/python-ndb/commit/0ebfaedc48911b57d0cb23584a2a84c31a92d06a))

## [1.11.2](https://github.com/googleapis/python-ndb/compare/v1.11.1...v1.11.2) (2022-06-03)


### Documentation

* fix changelog header to consistent size ([#773](https://github.com/googleapis/python-ndb/issues/773)) ([7bb4e5a](https://github.com/googleapis/python-ndb/commit/7bb4e5a7bf11061a546f21e6f57cf2937f7a3a9d))

## [1.11.1](https://www.github.com/googleapis/python-ndb/compare/v1.11.0...v1.11.1) (2021-11-03)


### Bug Fixes

* increase cache lock expiration time ([#740](https://www.github.com/googleapis/python-ndb/issues/740)) ([2634d01](https://www.github.com/googleapis/python-ndb/commit/2634d01ac9d4a73057d5e16cf476c5ecfc8e7fcf)), closes [#728](https://www.github.com/googleapis/python-ndb/issues/728)

## [1.11.0](https://www.github.com/googleapis/python-ndb/compare/v1.10.5...v1.11.0) (2021-10-28)


### Features

* add support for python 3.10 ([#735](https://www.github.com/googleapis/python-ndb/issues/735)) ([58620c1](https://www.github.com/googleapis/python-ndb/commit/58620c1b17e3a4b3608614bea620e93f39e1bd3a))

## [1.10.5](https://www.github.com/googleapis/python-ndb/compare/v1.10.4...v1.10.5) (2021-10-08)


### Bug Fixes

* correct regression in `Model.get_or_insert` ([#731](https://www.github.com/googleapis/python-ndb/issues/731)) ([921ec69](https://www.github.com/googleapis/python-ndb/commit/921ec695e246e548f207b0c6aded7296e4b3b263)), closes [#729](https://www.github.com/googleapis/python-ndb/issues/729)

## [1.10.4](https://www.github.com/googleapis/python-ndb/compare/v1.10.3...v1.10.4) (2021-09-28)


### Bug Fixes

* pin grpcio / googleapis-common-protos under Python2 ([#725](https://www.github.com/googleapis/python-ndb/issues/725)) ([ccc82e4](https://www.github.com/googleapis/python-ndb/commit/ccc82e42fe2bbb285779a81cff03866facfad667))

## [1.10.3](https://www.github.com/googleapis/python-ndb/compare/v1.10.2...v1.10.3) (2021-09-07)


### Bug Fixes

* use thread-safe iterator to generate context ids ([#716](https://www.github.com/googleapis/python-ndb/issues/716)) ([92ec8ac](https://www.github.com/googleapis/python-ndb/commit/92ec8ac7de8cd0f50d6104b9e514b4e933cfbb13)), closes [#715](https://www.github.com/googleapis/python-ndb/issues/715)

## [1.10.2](https://www.github.com/googleapis/python-ndb/compare/v1.10.1...v1.10.2) (2021-08-31)


### Bug Fixes

* **deps:** add pytz as an explicit dependency ([#707](https://www.github.com/googleapis/python-ndb/issues/707)) ([6b48548](https://www.github.com/googleapis/python-ndb/commit/6b48548a1ea4b0c125314f907c25b47992ee6556))

## [1.10.1](https://www.github.com/googleapis/python-ndb/compare/v1.10.0...v1.10.1) (2021-08-11)


### Bug Fixes

* add rpc request object to debug logging ([#696](https://www.github.com/googleapis/python-ndb/issues/696)) ([45e590a](https://www.github.com/googleapis/python-ndb/commit/45e590a0903e6690a516a1eb35002664eebf540d)), closes [#695](https://www.github.com/googleapis/python-ndb/issues/695)
* allow for legacy repeated structured properties with empty values ([#702](https://www.github.com/googleapis/python-ndb/issues/702)) ([60c293d](https://www.github.com/googleapis/python-ndb/commit/60c293d039721f7e842ac8973a743642e182e4a5)), closes [#694](https://www.github.com/googleapis/python-ndb/issues/694)
* fix bug with concurrent writes to global cache ([#705](https://www.github.com/googleapis/python-ndb/issues/705)) ([bb7cadc](https://www.github.com/googleapis/python-ndb/commit/bb7cadc45df92757b0b2d49c8914a10869d64965)), closes [#692](https://www.github.com/googleapis/python-ndb/issues/692)

## [1.10.0](https://www.github.com/googleapis/python-ndb/compare/v1.9.0...v1.10.0) (2021-07-20)


### Features

* add 'python_requires' metadata to setup ([#681](https://www.github.com/googleapis/python-ndb/issues/681)) ([e9a09d3](https://www.github.com/googleapis/python-ndb/commit/e9a09d3f0facd29836ccce078575f12e102462c9))


### Bug Fixes

* fix bug with repeated structured properties with Expando values ([#671](https://www.github.com/googleapis/python-ndb/issues/671)) ([882dff0](https://www.github.com/googleapis/python-ndb/commit/882dff0517be9ddad5814317853ce87bf99d5db0)), closes [#669](https://www.github.com/googleapis/python-ndb/issues/669)
* properly handle legacy structured properties in Expando instances ([#676](https://www.github.com/googleapis/python-ndb/issues/676)) ([70710c8](https://www.github.com/googleapis/python-ndb/commit/70710c83c5ace83504167801da990bc81cb43c89)), closes [#673](https://www.github.com/googleapis/python-ndb/issues/673)
* refactor global cache to address concurrency and fault tolerance issues ([#667](https://www.github.com/googleapis/python-ndb/issues/667)) ([5e2c591](https://www.github.com/googleapis/python-ndb/commit/5e2c591cbd89d8783527252d7f771fba91792602))

## [1.9.0](https://www.github.com/googleapis/python-ndb/compare/v1.8.0...v1.9.0) (2021-06-07)


### Features

* don't flush entire global cache on transient errors ([#654](https://www.github.com/googleapis/python-ndb/issues/654)) ([cbf2d7d](https://www.github.com/googleapis/python-ndb/commit/cbf2d7de3d532ce08bd0d25fa18b5226afd216b9))


### Bug Fixes

* correct inconsistent behavior with regards to namespaces ([#662](https://www.github.com/googleapis/python-ndb/issues/662)) ([cf21a28](https://www.github.com/googleapis/python-ndb/commit/cf21a285e784019f9ba0f2a89a7acc4105fdcd2a)), closes [#661](https://www.github.com/googleapis/python-ndb/issues/661)
* correctly decode falsy values in legacy protocol buffers ([#628](https://www.github.com/googleapis/python-ndb/issues/628)) ([69a9f63](https://www.github.com/googleapis/python-ndb/commit/69a9f63be89ca50bbf0a42d0565a9f1fdcf6d143)), closes [#625](https://www.github.com/googleapis/python-ndb/issues/625)
* defer clearing global cache when in transaction ([#660](https://www.github.com/googleapis/python-ndb/issues/660)) ([73020ed](https://www.github.com/googleapis/python-ndb/commit/73020ed8f8eb1430f87be4b5680690d9e373c846))
* detect cache write failure for `MemcacheCache` ([#665](https://www.github.com/googleapis/python-ndb/issues/665)) ([5d7f163](https://www.github.com/googleapis/python-ndb/commit/5d7f163988c6e8c43579aae616d275db4ca4ff45)), closes [#656](https://www.github.com/googleapis/python-ndb/issues/656)
* do not set read_consistency for queries. ([#664](https://www.github.com/googleapis/python-ndb/issues/664)) ([36a5b55](https://www.github.com/googleapis/python-ndb/commit/36a5b55b1b21d7333923edd4a42d1a32fd453dfa)), closes [#666](https://www.github.com/googleapis/python-ndb/issues/666)
* limit memcache keys to 250 bytes ([#663](https://www.github.com/googleapis/python-ndb/issues/663)) ([7dc11df](https://www.github.com/googleapis/python-ndb/commit/7dc11df00fc15392fde61e828e1445eb9e66a1ac)), closes [#619](https://www.github.com/googleapis/python-ndb/issues/619)
* properly handle error when clearing cache ([#636](https://www.github.com/googleapis/python-ndb/issues/636)) ([d0ffcf3](https://www.github.com/googleapis/python-ndb/commit/d0ffcf3517fe357d6689943265b829258c397d93)), closes [#633](https://www.github.com/googleapis/python-ndb/issues/633)
* retry connection errors with memcache ([#645](https://www.github.com/googleapis/python-ndb/issues/645)) ([06b466a](https://www.github.com/googleapis/python-ndb/commit/06b466a8421ff7a5586164bf4deb43d6bcbf0ef4)), closes [#620](https://www.github.com/googleapis/python-ndb/issues/620)
* support ordering by key for multi queries ([#630](https://www.github.com/googleapis/python-ndb/issues/630)) ([508d8cb](https://www.github.com/googleapis/python-ndb/commit/508d8cb8c65afe5e885c1fdba4dce933d52cfd4b)), closes [#629](https://www.github.com/googleapis/python-ndb/issues/629)

## [1.8.0](https://www.github.com/googleapis/python-ndb/compare/v1.7.3...v1.8.0) (2021-04-06)


### Features

* retry global cache operations on transient errors ([#603](https://www.github.com/googleapis/python-ndb/issues/603)) ([5d6b650](https://www.github.com/googleapis/python-ndb/commit/5d6b6503ce40ba0d36ea79a461c2c95897235734)), closes [#601](https://www.github.com/googleapis/python-ndb/issues/601)


### Bug Fixes

* don't return `None` for entities found in queries ([#612](https://www.github.com/googleapis/python-ndb/issues/612)) ([9e5e255](https://www.github.com/googleapis/python-ndb/commit/9e5e255c14716b3046a9dc70bb8a4596beec1562)), closes [#586](https://www.github.com/googleapis/python-ndb/issues/586)
* fix bug with compressed blob property ([#615](https://www.github.com/googleapis/python-ndb/issues/615)) ([d305f9f](https://www.github.com/googleapis/python-ndb/commit/d305f9fd2b1cfe8e7d709849e392402f4ae059ac)), closes [#602](https://www.github.com/googleapis/python-ndb/issues/602)
* fix failing unit test ([#607](https://www.github.com/googleapis/python-ndb/issues/607)) ([5d3927e](https://www.github.com/googleapis/python-ndb/commit/5d3927e0b0a6d6a447585d2cc90077de26f24c5c)), closes [#606](https://www.github.com/googleapis/python-ndb/issues/606)
* handle unpickling between GAE NDB (2.7) to Cloud NDB (3) ([#596](https://www.github.com/googleapis/python-ndb/issues/596)) ([5be4225](https://www.github.com/googleapis/python-ndb/commit/5be4225f20b9216b49f953c464b8b8ef9683d8bf))
* mock call to `tasklets.sleep` in unit test ([#609](https://www.github.com/googleapis/python-ndb/issues/609)) ([00e23f3](https://www.github.com/googleapis/python-ndb/commit/00e23f3f31fb531b402f087e29b539a7af9ac79f)), closes [#608](https://www.github.com/googleapis/python-ndb/issues/608)
* prevent mismatch error when using default namespace on ancestor queries ([#614](https://www.github.com/googleapis/python-ndb/issues/614)) ([ae67f04](https://www.github.com/googleapis/python-ndb/commit/ae67f04db12c65ecca9d6145f113729072b952f3))
* reimplement `_clone_properties` ([#610](https://www.github.com/googleapis/python-ndb/issues/610)) ([e23f42b](https://www.github.com/googleapis/python-ndb/commit/e23f42b27cec6f7fcf05ae51d4e6ee2aea30f6ca)), closes [#566](https://www.github.com/googleapis/python-ndb/issues/566)
* replicate legacy behavior for using cache with queries ([#613](https://www.github.com/googleapis/python-ndb/issues/613)) ([edd1185](https://www.github.com/googleapis/python-ndb/commit/edd1185f01c6db5b4876f7b0ce81df0315c98890)), closes [#586](https://www.github.com/googleapis/python-ndb/issues/586)
* support `int` as base type for `BooleanProperty` ([#624](https://www.github.com/googleapis/python-ndb/issues/624)) ([a04bf3a](https://www.github.com/googleapis/python-ndb/commit/a04bf3acef3eb88f23c4f0832ce74af9557cb03d))

## [1.7.3](https://www.github.com/googleapis/python-ndb/compare/v1.7.2...v1.7.3) (2021-01-21)


### Bug Fixes

* handle negatives in protobuf deserialization ([#591](https://www.github.com/googleapis/python-ndb/issues/591)) ([0d3d3ca](https://www.github.com/googleapis/python-ndb/commit/0d3d3ca99df10a3d6e1c6f31ee719faa373ccacf)), closes [#590](https://www.github.com/googleapis/python-ndb/issues/590)
* make nested retry blocks work for RPC calls ([#589](https://www.github.com/googleapis/python-ndb/issues/589)) ([f125459](https://www.github.com/googleapis/python-ndb/commit/f125459d4eef05861776ccefd29d137a5f22e240))


### Documentation

* correct documentation for `GlobalCache` ([#565](https://www.github.com/googleapis/python-ndb/issues/565)) ([be5b157](https://www.github.com/googleapis/python-ndb/commit/be5b1571e8e30bd1d736ae5d77b3017473b1a373))
* fix return type in fetch docstring ([#594](https://www.github.com/googleapis/python-ndb/issues/594)) ([9eb15f4](https://www.github.com/googleapis/python-ndb/commit/9eb15f4ff75204ad25f943dbc1e85c227d88faf6)), closes [#576](https://www.github.com/googleapis/python-ndb/issues/576)
* fix typo in example code ([#588](https://www.github.com/googleapis/python-ndb/issues/588)) ([76fab49](https://www.github.com/googleapis/python-ndb/commit/76fab49f9d08a2add4135c011d08ff24f04549b2))

## [1.7.2](https://www.github.com/googleapis/python-ndb/compare/v1.7.1...v1.7.2) (2020-12-16)


### Bug Fixes

* always use brute-force counting with Datastore emulator and clean up related hacks ([#585](https://www.github.com/googleapis/python-ndb/issues/585)) ([8480a8b](https://www.github.com/googleapis/python-ndb/commit/8480a8bd0d169e2499ee62d1fb9d140aa6ce00d4))
* return a tuple when empty result returned on query ([#582](https://www.github.com/googleapis/python-ndb/issues/582)) ([7cf0e87](https://www.github.com/googleapis/python-ndb/commit/7cf0e878054dbfe7bc8b6c0c9fea96a602e8e859))
* support empty not_finished messages that cause query.count() to return early ([#580](https://www.github.com/googleapis/python-ndb/issues/580)) ([fc31553](https://www.github.com/googleapis/python-ndb/commit/fc31553c77f6e7865df0efd4c820f69366f6607c)), closes [#575](https://www.github.com/googleapis/python-ndb/issues/575)


### Documentation

* Add urlsafe() info to migration notes ([#579](https://www.github.com/googleapis/python-ndb/issues/579)) ([9df2f9f](https://www.github.com/googleapis/python-ndb/commit/9df2f9f8be40d95fbde297335eb99b19bafad583))

## [1.7.1](https://www.github.com/googleapis/python-ndb/compare/v1.7.0...v1.7.1) (2020-11-11)


### Bug Fixes

* **dependencies:** Pin to less than 2.0.0 for google-cloud-datastore ([#569](https://www.github.com/googleapis/python-ndb/issues/569)) ([c8860a6](https://www.github.com/googleapis/python-ndb/commit/c8860a6541f638fb458b74cfdffc1ddb7b035549)), closes [#568](https://www.github.com/googleapis/python-ndb/issues/568)

## [1.7.0](https://www.github.com/googleapis/python-ndb/compare/v1.6.1...v1.7.0) (2020-10-22)


### Features

* fault tolerance for global caches ([#560](https://www.github.com/googleapis/python-ndb/issues/560)) ([8ab8ee0](https://www.github.com/googleapis/python-ndb/commit/8ab8ee01f5577cfe468ed77d3cd48d6f6b816b0e)), closes [#557](https://www.github.com/googleapis/python-ndb/issues/557)
* Transaction propagation using ndb.TransactionOptions ([#537](https://www.github.com/googleapis/python-ndb/issues/537)) ([f3aa027](https://www.github.com/googleapis/python-ndb/commit/f3aa027d7d55d9aee9a72ce23cebc26a5975bb28))

## [1.6.1](https://www.github.com/googleapis/python-ndb/compare/v1.6.0...v1.6.1) (2020-10-08)


### Bug Fixes

* `[@non](https://www.github.com/non)_transactional` decorator was not working correctly with async ([#554](https://www.github.com/googleapis/python-ndb/issues/554)) ([758c8e6](https://www.github.com/googleapis/python-ndb/commit/758c8e66314da4cb1f077e9fbe8cf1ae09bccd4e)), closes [#552](https://www.github.com/googleapis/python-ndb/issues/552)
* fix a connection leak in RedisCache ([#556](https://www.github.com/googleapis/python-ndb/issues/556)) ([47ae172](https://www.github.com/googleapis/python-ndb/commit/47ae172edc435a49d25687d83747afff153b59d2))
* get_by_id and get_or_insert should use default namespace when passed in ([#542](https://www.github.com/googleapis/python-ndb/issues/542)) ([3674650](https://www.github.com/googleapis/python-ndb/commit/3674650a7ba1a1dd7a72b728f343f623f660ba6a)), closes [#535](https://www.github.com/googleapis/python-ndb/issues/535)


### Documentation

* address docs builds and memcached customization to docker file ([#548](https://www.github.com/googleapis/python-ndb/issues/548)) ([88e7e24](https://www.github.com/googleapis/python-ndb/commit/88e7e244854acb2409c324855deb9229f33a44fd))
* update docker image used for docs generation [#549](https://www.github.com/googleapis/python-ndb/issues/549) ([5e8bf57](https://www.github.com/googleapis/python-ndb/commit/5e8bf57508e3b995f51dcc3171e5ea77c4bc4484))

## [1.6.0](https://www.github.com/googleapis/python-ndb/compare/v1.5.2...v1.6.0) (2020-09-14)


### Features

* memcached integration ([#536](https://www.github.com/googleapis/python-ndb/issues/536)) ([2bd43da](https://www.github.com/googleapis/python-ndb/commit/2bd43dabbd6b6fbffbb4390520e47ae06262c858))

## [1.5.2](https://www.github.com/googleapis/python-ndb/compare/v1.5.1...v1.5.2) (2020-09-03)


### Bug Fixes

* avoid kind error when using subclasses in local structured properties ([#531](https://www.github.com/googleapis/python-ndb/issues/531)) ([49f9e48](https://www.github.com/googleapis/python-ndb/commit/49f9e48a7d8bf9c3c8cc8a30ae385bcbcb95dbaa))
* fix bug when setting naive datetime on `DateTimeProperty` with timezone ([#534](https://www.github.com/googleapis/python-ndb/issues/534)) ([ad42606](https://www.github.com/googleapis/python-ndb/commit/ad426063257f8633bb4207a77b29b35fc0173ec1)), closes [#517](https://www.github.com/googleapis/python-ndb/issues/517)
* make optimized `Query.count()` work with the datastore emulator ([#528](https://www.github.com/googleapis/python-ndb/issues/528)) ([e5df1e3](https://www.github.com/googleapis/python-ndb/commit/e5df1e37c97fc0765f8f95ada6d4dadd7b4bb445)), closes [#525](https://www.github.com/googleapis/python-ndb/issues/525)
* make sure `keys_only` ordered multiquery returns keys not entities ([#527](https://www.github.com/googleapis/python-ndb/issues/527)) ([2078dc1](https://www.github.com/googleapis/python-ndb/commit/2078dc1c2239299729d8ecade2e3592f49bc65db)), closes [#526](https://www.github.com/googleapis/python-ndb/issues/526)


### Documentation

* fix type hint for urlsafe ([#532](https://www.github.com/googleapis/python-ndb/issues/532)) ([87a3475](https://www.github.com/googleapis/python-ndb/commit/87a347536b459c461a02c401b8a8c097e276d3ea)), closes [#529](https://www.github.com/googleapis/python-ndb/issues/529)

## [1.5.1](https://www.github.com/googleapis/python-ndb/compare/v1.5.0...v1.5.1) (2020-08-28)


### Bug Fixes

* fix exception handling bug in tasklets ([#520](https://www.github.com/googleapis/python-ndb/issues/520)) ([fc0366a](https://www.github.com/googleapis/python-ndb/commit/fc0366a9db9fa5263533631cb08ccb5be07960ad)), closes [#519](https://www.github.com/googleapis/python-ndb/issues/519)
* fix format exceptions in `utils.logging_debug` ([#514](https://www.github.com/googleapis/python-ndb/issues/514)) ([d38c0a3](https://www.github.com/googleapis/python-ndb/commit/d38c0a36dac1dc183d344a08050815010b256638)), closes [#508](https://www.github.com/googleapis/python-ndb/issues/508)
* transparently add sort properties to projection for multiqueries ([#511](https://www.github.com/googleapis/python-ndb/issues/511)) ([4e46327](https://www.github.com/googleapis/python-ndb/commit/4e463273a36b5fe69f87d429260fba1a690d55b9)), closes [#509](https://www.github.com/googleapis/python-ndb/issues/509)

## [1.5.0](https://www.github.com/googleapis/python-ndb/compare/v1.4.2...v1.5.0) (2020-08-12)


### Features

* use contextvars.ConvextVar instead of threading.local in Python 3 ([4c634f3](https://www.github.com/googleapis/python-ndb/commit/4c634f348f8847fda139fe469e0e8adfabfd649a)), closes [#504](https://www.github.com/googleapis/python-ndb/issues/504)


### Bug Fixes

* fix concurrency bug in redis cache implementation ([#503](https://www.github.com/googleapis/python-ndb/issues/503)) ([6c18b95](https://www.github.com/googleapis/python-ndb/commit/6c18b9522e83e5e599a491c6ed287de2d7cdf089)), closes [#496](https://www.github.com/googleapis/python-ndb/issues/496)
* support polymodel in local structured property ([#497](https://www.github.com/googleapis/python-ndb/issues/497)) ([9ccbdd2](https://www.github.com/googleapis/python-ndb/commit/9ccbdd23448dcb401b111f03e951fa89ae65174f)), closes [#481](https://www.github.com/googleapis/python-ndb/issues/481)

## [1.4.2](https://www.github.com/googleapis/python-ndb/compare/v1.4.1...v1.4.2) (2020-07-30)


### Bug Fixes

* include ancestors in `Key.to_legacy_urlsafe` ([#494](https://www.github.com/googleapis/python-ndb/issues/494)) ([0f29190](https://www.github.com/googleapis/python-ndb/commit/0f2919070ef78a17988fb5cae573a1514ff63926)), closes [#478](https://www.github.com/googleapis/python-ndb/issues/478)
* properly handle explicitly passing default namespace ([#488](https://www.github.com/googleapis/python-ndb/issues/488)) ([3c64483](https://www.github.com/googleapis/python-ndb/commit/3c644838a499f54620c6a12773f8cdd1c245096f)), closes [#476](https://www.github.com/googleapis/python-ndb/issues/476)

## [1.4.1](https://www.github.com/googleapis/python-ndb/compare/v1.4.0...v1.4.1) (2020-07-10)


### Bug Fixes

* do not disclose cache contents in stack traces ([#485](https://www.github.com/googleapis/python-ndb/issues/485)) ([2d2c5a2](https://www.github.com/googleapis/python-ndb/commit/2d2c5a2004629b807f296f74648c789c6ce9a6ba)), closes [#482](https://www.github.com/googleapis/python-ndb/issues/482)

## [1.4.0](https://www.github.com/googleapis/python-ndb/compare/v1.3.0...v1.4.0) (2020-07-01)


### Features

* allow `Query.fetch_page` for queries with post filters ([#463](https://www.github.com/googleapis/python-ndb/issues/463)) ([632435c](https://www.github.com/googleapis/python-ndb/commit/632435c155f565f5e7b45ab08680613599994f0e)), closes [#270](https://www.github.com/googleapis/python-ndb/issues/270)
* record time spent waiting on rpc calls ([#472](https://www.github.com/googleapis/python-ndb/issues/472)) ([1629805](https://www.github.com/googleapis/python-ndb/commit/16298057c96921a3c995e9ddded36d37fc90819f))


### Bug Fixes

* ignore datastore properties that are not mapped to NDB properties ([#470](https://www.github.com/googleapis/python-ndb/issues/470)) ([ab460fa](https://www.github.com/googleapis/python-ndb/commit/ab460fad8ded5b3b550359253e90a6b189145842)), closes [#461](https://www.github.com/googleapis/python-ndb/issues/461)
* make sure `tests` package is not included in distribution ([#469](https://www.github.com/googleapis/python-ndb/issues/469)) ([5a20d0a](https://www.github.com/googleapis/python-ndb/commit/5a20d0af6c6c1c2d10e9e42a35a5b58fa952547c)), closes [#468](https://www.github.com/googleapis/python-ndb/issues/468)
* retry grpc `UNKNOWN` errors ([#458](https://www.github.com/googleapis/python-ndb/issues/458)) ([5d354e4](https://www.github.com/googleapis/python-ndb/commit/5d354e4b4247372f2ffdc9caa2df1516ce97ff8d)), closes [#310](https://www.github.com/googleapis/python-ndb/issues/310)

## [1.3.0](https://www.github.com/googleapis/python-ndb/compare/v1.2.1...v1.3.0) (2020-06-01)


### Features

* add templates for python samples projects ([#506](https://www.github.com/googleapis/python-ndb/issues/506)) ([#455](https://www.github.com/googleapis/python-ndb/issues/455)) ([e329276](https://www.github.com/googleapis/python-ndb/commit/e32927623645112513675fbbfe5884a63eac24e1))
* convert grpc errors to api core exceptions ([#457](https://www.github.com/googleapis/python-ndb/issues/457)) ([042cf6c](https://www.github.com/googleapis/python-ndb/commit/042cf6ceabe2a47b2fe77501ccd618e64877886a)), closes [#416](https://www.github.com/googleapis/python-ndb/issues/416)


### Bug Fixes

* Add support for 'name' Key instances to to_legacy_urlsafe ([#420](https://www.github.com/googleapis/python-ndb/issues/420)) ([59fc5af](https://www.github.com/googleapis/python-ndb/commit/59fc5afc36d01b72ad4b53befa593803b55df8b3))
* all query types should use cache if available ([#454](https://www.github.com/googleapis/python-ndb/issues/454)) ([69b3a0a](https://www.github.com/googleapis/python-ndb/commit/69b3a0ae49ab446a9ed903646ae6e01690411d3e)), closes [#441](https://www.github.com/googleapis/python-ndb/issues/441)
* fix `NotImplementedError` for `get_or_insert` inside a transaction ([#451](https://www.github.com/googleapis/python-ndb/issues/451)) ([99aa403](https://www.github.com/googleapis/python-ndb/commit/99aa40358b469be1c8486c84ba5873929715f25e)), closes [#433](https://www.github.com/googleapis/python-ndb/issues/433)
* make sure datastore key constructor never gets None in a pair ([#446](https://www.github.com/googleapis/python-ndb/issues/446)) ([e6173cf](https://www.github.com/googleapis/python-ndb/commit/e6173cf8feec866c365d35e7cb461f72d19544fa)), closes [#384](https://www.github.com/googleapis/python-ndb/issues/384) [#439](https://www.github.com/googleapis/python-ndb/issues/439)
* refactor transactions to use their own event loops ([#443](https://www.github.com/googleapis/python-ndb/issues/443)) ([7590be8](https://www.github.com/googleapis/python-ndb/commit/7590be8233fe58f9c45076eb38c1995363f02362)), closes [#426](https://www.github.com/googleapis/python-ndb/issues/426) [#426](https://www.github.com/googleapis/python-ndb/issues/426)
* respect `_code_name` in `StructuredProperty.__getattr__` ([#453](https://www.github.com/googleapis/python-ndb/issues/453)) ([4f54dfc](https://www.github.com/googleapis/python-ndb/commit/4f54dfcee91b15d45cc6046f6b9933d1593d0956)), closes [#449](https://www.github.com/googleapis/python-ndb/issues/449)
* strip `order_by` option from query when using `count()` ([#452](https://www.github.com/googleapis/python-ndb/issues/452)) ([9d20a2d](https://www.github.com/googleapis/python-ndb/commit/9d20a2d5d75cc0590c4326019ea94159bb4aebe2)), closes [#447](https://www.github.com/googleapis/python-ndb/issues/447)

## [1.2.1](https://www.github.com/googleapis/python-ndb/compare/v1.2.0...v1.2.1) (2020-05-15)


### Features

* Improve custom validators ([#408](https://www.github.com/googleapis/python-ndb/issues/408)) ([5b6cdd6](https://www.github.com/googleapis/python-ndb/commit/5b6cdd627dfce3e5b987c2ecd945d39b5056aa37)), closes [#252](https://www.github.com/googleapis/python-ndb/issues/252)


### Bug Fixes

* clear context cache on rollback ([#410](https://www.github.com/googleapis/python-ndb/issues/410)) ([aa17986](https://www.github.com/googleapis/python-ndb/commit/aa17986759f32ea16c340961d70fbc8fc123b244)), closes [#398](https://www.github.com/googleapis/python-ndb/issues/398)
* do not allow empty key parts for key constructor in namespaced model ([#401](https://www.github.com/googleapis/python-ndb/issues/401)) ([f3528b3](https://www.github.com/googleapis/python-ndb/commit/f3528b3e51c93c762c4e31eed76a1b2f06be84e1)), closes [#384](https://www.github.com/googleapis/python-ndb/issues/384)
* don't rely on duck typing for `_retry.is_transient_error` ([#425](https://www.github.com/googleapis/python-ndb/issues/425)) ([4524542](https://www.github.com/googleapis/python-ndb/commit/4524542e5f6da1af047d86fee3d48cf65ea75508)), closes [#415](https://www.github.com/googleapis/python-ndb/issues/415)
* handle empty batches from Firestore ([#396](https://www.github.com/googleapis/python-ndb/issues/396)) ([1a054ca](https://www.github.com/googleapis/python-ndb/commit/1a054cadff07074de9395cb99ae2c40f987aed2e)), closes [#386](https://www.github.com/googleapis/python-ndb/issues/386)
* make sure reads happen in transaction if there is a transaction ([#395](https://www.github.com/googleapis/python-ndb/issues/395)) ([f32644f](https://www.github.com/googleapis/python-ndb/commit/f32644fcf8c16dc0fd74e14108d7955effff1771)), closes [#394](https://www.github.com/googleapis/python-ndb/issues/394)
* more should be boolean in fetch_page call ([#423](https://www.github.com/googleapis/python-ndb/issues/423)) ([a69ffd2](https://www.github.com/googleapis/python-ndb/commit/a69ffd21aaaa881f5e8e54339fd62a1b02d19c4b)), closes [#422](https://www.github.com/googleapis/python-ndb/issues/422)
* support same options in model.query as query ([#407](https://www.github.com/googleapis/python-ndb/issues/407)) ([d08019f](https://www.github.com/googleapis/python-ndb/commit/d08019fbecb0f018987267b01929a21e97b418e2))
* uniform handling of `projection` argument ([#428](https://www.github.com/googleapis/python-ndb/issues/428)) ([2b65c04](https://www.github.com/googleapis/python-ndb/commit/2b65c04e72a66062e2c792b5b1fb067fb935987f)), closes [#379](https://www.github.com/googleapis/python-ndb/issues/379)
* use `skipped_results` from query results to adjust offset ([#399](https://www.github.com/googleapis/python-ndb/issues/399)) ([6d1452d](https://www.github.com/googleapis/python-ndb/commit/6d1452d977f3f030ff65d5cbb3e593c0789e6c14)), closes [#392](https://www.github.com/googleapis/python-ndb/issues/392)
* use fresh context cache for each transaction ([#409](https://www.github.com/googleapis/python-ndb/issues/409)) ([5109b91](https://www.github.com/googleapis/python-ndb/commit/5109b91425e917727973079020dc51c2b8fddf53)), closes [#394](https://www.github.com/googleapis/python-ndb/issues/394)
* use true `keys_only` query for `Query.count()` ([#405](https://www.github.com/googleapis/python-ndb/issues/405)) ([88184c3](https://www.github.com/googleapis/python-ndb/commit/88184c312dd7bdc7bd36ec58fd53e3fd5001d7ac)), closes [#400](https://www.github.com/googleapis/python-ndb/issues/400) [#404](https://www.github.com/googleapis/python-ndb/issues/404)

## [1.2.0](https://www.github.com/googleapis/python-ndb/compare/v1.1.2...v1.2.0) (2020-04-20)


### Features

* add `namespace` property to `context.Context` ([#388](https://www.github.com/googleapis/python-ndb/issues/388)) ([34bac15](https://www.github.com/googleapis/python-ndb/commit/34bac153bcc191857715a8760671acaf4fd12706)), closes [#385](https://www.github.com/googleapis/python-ndb/issues/385)
* new `join` argument for `transaction` and related functions ([#381](https://www.github.com/googleapis/python-ndb/issues/381)) ([2c91685](https://www.github.com/googleapis/python-ndb/commit/2c916851d088b650a5d643dc322a4919f456fe05)), closes [#366](https://www.github.com/googleapis/python-ndb/issues/366)


### Bug Fixes

* accept `bytes` or `str` as base value for `JsonProperty` ([#380](https://www.github.com/googleapis/python-ndb/issues/380)) ([e7a0c7c](https://www.github.com/googleapis/python-ndb/commit/e7a0c7c8fb7d80f009442f759abadbd336c0c828)), closes [#378](https://www.github.com/googleapis/python-ndb/issues/378)
* add `ABORTED` to retryable status codes ([#391](https://www.github.com/googleapis/python-ndb/issues/391)) ([183c0c3](https://www.github.com/googleapis/python-ndb/commit/183c0c33a4429ad6bdaa9f141a8ac88ad4e3544d)), closes [#383](https://www.github.com/googleapis/python-ndb/issues/383)
* add missing _get_for_dict method ([#368](https://www.github.com/googleapis/python-ndb/issues/368)) ([55b80ff](https://www.github.com/googleapis/python-ndb/commit/55b80ffa086568e8f820f9ab304952bc39383bd8)), closes [#367](https://www.github.com/googleapis/python-ndb/issues/367)
* empty Entities for optional LocalStructuredProperty fields  ([#370](https://www.github.com/googleapis/python-ndb/issues/370)) ([27a0969](https://www.github.com/googleapis/python-ndb/commit/27a0969982013b37d3f6d8785c3ad127788661f9)), closes [#369](https://www.github.com/googleapis/python-ndb/issues/369)
* return type in DateTimeProperty._to_base_type docstring ([#371](https://www.github.com/googleapis/python-ndb/issues/371)) ([0c549c8](https://www.github.com/googleapis/python-ndb/commit/0c549c89ff78554c4a4dde40973b503aa741422f))

## [1.1.2](https://www.github.com/googleapis/python-ndb/compare/v1.1.1...v1.1.2) (2020-03-16)


### Bug Fixes

* check for legacy local structured property values ([#365](https://www.github.com/googleapis/python-ndb/issues/365)) ([f81f406](https://www.github.com/googleapis/python-ndb/commit/f81f406d8e1059121341828836fce2aae5782fca)), closes [#359](https://www.github.com/googleapis/python-ndb/issues/359)
* move stub (grpc communication channel) to client ([#362](https://www.github.com/googleapis/python-ndb/issues/362)) ([90e0625](https://www.github.com/googleapis/python-ndb/commit/90e06252df25fa2ce199543e7b01b17ec284aaf1)), closes [#343](https://www.github.com/googleapis/python-ndb/issues/343)

## [1.1.1](https://www.github.com/googleapis/python-ndb/compare/v1.1.0...v1.1.1) (2020-03-05)


### Bug Fixes

* fix bug with `yield` of empty list in tasklets ([#354](https://www.github.com/googleapis/python-ndb/issues/354)) ([2d60ebf](https://www.github.com/googleapis/python-ndb/commit/2d60ebfe656abd75f6b9303550b2e03c2cbd79b7)), closes [#353](https://www.github.com/googleapis/python-ndb/issues/353)
* LocalStructuredProperty keep_keys ([#355](https://www.github.com/googleapis/python-ndb/issues/355)) ([9ff1b3d](https://www.github.com/googleapis/python-ndb/commit/9ff1b3de817da50b58a6aed574d7e2f2dcf92310))
* support nested sequences in parallel `yield` for tasklets ([#358](https://www.github.com/googleapis/python-ndb/issues/358)) ([8c91e7a](https://www.github.com/googleapis/python-ndb/commit/8c91e7ae8262f355a9eafe9051b3c1ef19d4c7cd)), closes [#349](https://www.github.com/googleapis/python-ndb/issues/349)

## [1.1.0](https://www.github.com/googleapis/python-ndb/compare/v1.0.1...v1.1.0) (2020-03-02)


### Features

* `Key.to_legacy_urlsafe()` ([#348](https://www.github.com/googleapis/python-ndb/issues/348)) ([ab10e3c](https://www.github.com/googleapis/python-ndb/commit/ab10e3c4998b8995d5a057163ce8d9dc8992111a))


### Bug Fixes

* allow legacy ndb to read LocalStructuredProperty entities. ([#344](https://www.github.com/googleapis/python-ndb/issues/344)) ([7b07692](https://www.github.com/googleapis/python-ndb/commit/7b0769236841cea1e864ae1e928a7b7021d300dc))
* fix delete in transaction ([#333](https://www.github.com/googleapis/python-ndb/issues/333)) ([5c162f4](https://www.github.com/googleapis/python-ndb/commit/5c162f4337b837f7125b1fb03f8cff5fb1b4a356)), closes [#271](https://www.github.com/googleapis/python-ndb/issues/271)
* make sure ``key.Key`` uses namespace from client when not specified ([#339](https://www.github.com/googleapis/python-ndb/issues/339)) ([44f02e4](https://www.github.com/googleapis/python-ndb/commit/44f02e46deef245f4d1ae80f9d2e4edd46ecd265)), closes [#337](https://www.github.com/googleapis/python-ndb/issues/337)
* properly exclude from indexes non-indexed subproperties of structured properties ([#346](https://www.github.com/googleapis/python-ndb/issues/346)) ([dde6b85](https://www.github.com/googleapis/python-ndb/commit/dde6b85897457cef7a1080690df5cfae9cb6c31e)), closes [#341](https://www.github.com/googleapis/python-ndb/issues/341)
* resurrect support for compressed text property ([#342](https://www.github.com/googleapis/python-ndb/issues/342)) ([5a86456](https://www.github.com/googleapis/python-ndb/commit/5a864563dc6e155b73e2ac35af6519823c356e19)), closes [#277](https://www.github.com/googleapis/python-ndb/issues/277)
* use correct name when reading legacy structured properties with names ([#347](https://www.github.com/googleapis/python-ndb/issues/347)) ([01d1256](https://www.github.com/googleapis/python-ndb/commit/01d1256e9d41c20bb5836067455c4be4abe1c516)), closes [#345](https://www.github.com/googleapis/python-ndb/issues/345)

## [1.0.1](https://www.github.com/googleapis/python-ndb/compare/v1.0.0...v1.0.1) (2020-02-11)


### Bug Fixes

* attempt to have fewer transient errors in continuous integration ([#328](https://www.github.com/googleapis/python-ndb/issues/328)) ([0484c7a](https://www.github.com/googleapis/python-ndb/commit/0484c7abf5a1529db5fecf17ebdf0252eab8449e))
* correct migration doc ([#313](https://www.github.com/googleapis/python-ndb/issues/313)) ([#317](https://www.github.com/googleapis/python-ndb/issues/317)) ([efce24f](https://www.github.com/googleapis/python-ndb/commit/efce24f16a877aecf78264946c22a2c9e3e97f53))
* disuse `__slots__` in most places ([#330](https://www.github.com/googleapis/python-ndb/issues/330)) ([a8b723b](https://www.github.com/googleapis/python-ndb/commit/a8b723b992e7a91860f6a73c0ee0fd7071e574d3)), closes [#311](https://www.github.com/googleapis/python-ndb/issues/311)
* don't set key on structured property entities ([#312](https://www.github.com/googleapis/python-ndb/issues/312)) ([63f3d94](https://www.github.com/googleapis/python-ndb/commit/63f3d943001d77c1ea0eb9b719e71ecff4eb5dd6)), closes [#281](https://www.github.com/googleapis/python-ndb/issues/281)
* fix race condition in remote calls ([#329](https://www.github.com/googleapis/python-ndb/issues/329)) ([f550510](https://www.github.com/googleapis/python-ndb/commit/f5505100f065e71a14714369d8aef1f7b06ee838)), closes [#302](https://www.github.com/googleapis/python-ndb/issues/302)
* make query options convert projection properties to strings ([#325](https://www.github.com/googleapis/python-ndb/issues/325)) ([d1a4800](https://www.github.com/googleapis/python-ndb/commit/d1a4800c5f53490e6956c11797bd3472ea404b5b))
* use multiple batches of limited size for large operations ([#321](https://www.github.com/googleapis/python-ndb/issues/321)) ([8e69453](https://www.github.com/googleapis/python-ndb/commit/8e6945377a4635632d0c35b7a41daebe501d4f0f)), closes [#318](https://www.github.com/googleapis/python-ndb/issues/318)
* use six string_types and integer_types for all isinstance() checks ([#323](https://www.github.com/googleapis/python-ndb/issues/323)) ([133acf8](https://www.github.com/googleapis/python-ndb/commit/133acf87b2a2efbfeae23ac9f629132cfb368a55))

## [1.0.0](https://www.github.com/googleapis/python-ndb/compare/v0.2.2...v1.0.0) (2020-01-30)


### Bug Fixes

* add user agent prefix google-cloud-ndb + version ([#299](https://www.github.com/googleapis/python-ndb/issues/299)) ([9fa136b](https://www.github.com/googleapis/python-ndb/commit/9fa136b9c163b24aefde6ccbc227a1035fa24bcd))
* Finish implementation of UserProperty. ([#301](https://www.github.com/googleapis/python-ndb/issues/301)) ([fd2e0ed](https://www.github.com/googleapis/python-ndb/commit/fd2e0ed9bb6cec8b5651c58eaee2b3ca8a96aebb)), closes [#280](https://www.github.com/googleapis/python-ndb/issues/280)
* Fix bug when wrapping base values. ([#303](https://www.github.com/googleapis/python-ndb/issues/303)) ([91ca8d9](https://www.github.com/googleapis/python-ndb/commit/91ca8d9044671361b731323317cef720dd19be82)), closes [#300](https://www.github.com/googleapis/python-ndb/issues/300)
* Fix bug with the _GlobalCacheGetBatch. ([#305](https://www.github.com/googleapis/python-ndb/issues/305)) ([f213165](https://www.github.com/googleapis/python-ndb/commit/f2131654c6e5f67895fb0e3c09a507e8dc25c4bb)), closes [#294](https://www.github.com/googleapis/python-ndb/issues/294)
* Preserve `QueryIterator.cursor_after`. ([#296](https://www.github.com/googleapis/python-ndb/issues/296)) ([4ffedc7](https://www.github.com/googleapis/python-ndb/commit/4ffedc7b5a2366be15dcd299052d8a46a748addd)), closes [#292](https://www.github.com/googleapis/python-ndb/issues/292)

## [0.2.2](https://www.github.com/googleapis/python-ndb/compare/v0.2.1...v0.2.2) (2020-01-15)


### Bug Fixes

* Convert NDB keys to Datastore keys for serialization. ([#287](https://www.github.com/googleapis/python-ndb/issues/287)) ([779411b](https://www.github.com/googleapis/python-ndb/commit/779411b562575bd2d6f0627ce1903c2996f3c529)), closes [#284](https://www.github.com/googleapis/python-ndb/issues/284)
* fix missing __ne__ methods ([#279](https://www.github.com/googleapis/python-ndb/issues/279)) ([03dd5e1](https://www.github.com/googleapis/python-ndb/commit/03dd5e1c78b8e8354379d743e2f810ef1bece4d2))
* Fix repr() for ComputedProperty ([#291](https://www.github.com/googleapis/python-ndb/issues/291)) ([2d8857b](https://www.github.com/googleapis/python-ndb/commit/2d8857b8e9a7119a47fd72ae76401af4e42bb5b5)), closes [#256](https://www.github.com/googleapis/python-ndb/issues/256)
* Handle `int` for DateTimeProperty ([#285](https://www.github.com/googleapis/python-ndb/issues/285)) ([2fe5be3](https://www.github.com/googleapis/python-ndb/commit/2fe5be31784a036062180f9c0f2c7b5eda978123)), closes [#261](https://www.github.com/googleapis/python-ndb/issues/261)
* More friendly error message when using `fetch_page` with post-filters. ([#269](https://www.github.com/googleapis/python-ndb/issues/269)) ([a40ae74](https://www.github.com/googleapis/python-ndb/commit/a40ae74d74fa83119349de4b3a91f90df40d7ea5)), closes [#254](https://www.github.com/googleapis/python-ndb/issues/254)

## [0.2.1](https://www.github.com/googleapis/python-ndb/compare/v0.2.0...v0.2.1) (2019-12-10)


### Bug Fixes

* Correctly handle `limit` and `offset` when batching query results. ([#237](https://www.github.com/googleapis/python-ndb/issues/237)) ([8d3ce5c](https://www.github.com/googleapis/python-ndb/commit/8d3ce5c6cce9055d21400aa9feebc99e66393667)), closes [#236](https://www.github.com/googleapis/python-ndb/issues/236)
* Improve test cleanup. ([#234](https://www.github.com/googleapis/python-ndb/issues/234)) ([21f3d8b](https://www.github.com/googleapis/python-ndb/commit/21f3d8b12a3e2fefe488a951fb5186c7620cb864))
* IntegerProperty now accepts `long` type for Python 2.7. ([#262](https://www.github.com/googleapis/python-ndb/issues/262)) ([9591e56](https://www.github.com/googleapis/python-ndb/commit/9591e569db32769c449d60dd3d9bdd6772dbc8f6)), closes [#250](https://www.github.com/googleapis/python-ndb/issues/250)
* Unstable order bug in unit test. ([#251](https://www.github.com/googleapis/python-ndb/issues/251)) ([7ff1df5](https://www.github.com/googleapis/python-ndb/commit/7ff1df51056f8498dc4320fc4b2684ead34a9116)), closes [#244](https://www.github.com/googleapis/python-ndb/issues/244)

## 0.2.0

11-06-2019 10:39 PST


### Implementation Changes
- `query.map()` and `query.map_async()` hanging with empty result set. ([#230](https://github.com/googleapis/python-ndb/pull/230))
- remove dunder version ([#202](https://github.com/googleapis/python-ndb/pull/202))
- Check context ([#211](https://github.com/googleapis/python-ndb/pull/211))
- Fix `Model._gql`. ([#223](https://github.com/googleapis/python-ndb/pull/223))
- Update intersphinx mapping ([#206](https://github.com/googleapis/python-ndb/pull/206))
- do not set meanings for compressed property when it has no value ([#200](https://github.com/googleapis/python-ndb/pull/200))

### New Features
- Python 2.7 compatibility ([#203](https://github.com/googleapis/python-ndb/pull/203))
- Add `tzinfo` to DateTimeProperty. ([#226](https://github.com/googleapis/python-ndb/pull/226))
- Implement `_prepare_for_put` for `StructuredProperty` and `LocalStructuredProperty`. ([#221](https://github.com/googleapis/python-ndb/pull/221))
- Implement ``Query.map`` and ``Query.map_async``. ([#218](https://github.com/googleapis/python-ndb/pull/218))
- Allow class member values in projection and distinct queries  ([#214](https://github.com/googleapis/python-ndb/pull/214))
- Implement ``Future.cancel()`` ([#204](https://github.com/googleapis/python-ndb/pull/204))

### Documentation
- Update README to include Python 2 support. ([#231](https://github.com/googleapis/python-ndb/pull/231))
- Fix typo in MIGRATION_NOTES.md ([#208](https://github.com/googleapis/python-ndb/pull/208))
- Spelling fixes. ([#209](https://github.com/googleapis/python-ndb/pull/209))
- Add spell checking dependencies for documentation build. ([#196](https://github.com/googleapis/python-ndb/pull/196))

### Internal / Testing Changes
- Enable release-please ([#228](https://github.com/googleapis/python-ndb/pull/228))
- Introduce local redis for tests ([#191](https://github.com/googleapis/python-ndb/pull/191))
- Use .kokoro configs from templates. ([#194](https://github.com/googleapis/python-ndb/pull/194))

## 0.1.0

09-10-2019 13:43 PDT

### Deprecations
- Deprecate `max_memcache_items`, memcache options, `force_rewrites`, `Query.map()`, `Query.map_async()`, `blobstore`. ([#168](https://github.com/googleapis/python-ndb/pull/168))

### Implementation Changes
- Fix error retrieving values for properties with different stored name ([#187](https://github.com/googleapis/python-ndb/pull/187))
- Use correct class when deserializing a PolyModel entity. ([#186](https://github.com/googleapis/python-ndb/pull/186))
- Support legacy compressed properties back and forth ([#183](https://github.com/googleapis/python-ndb/pull/183))
- Store Structured Properties in backwards compatible way ([#184](https://github.com/googleapis/python-ndb/pull/184))
- Allow put and get to work with compressed blob properties ([#175](https://github.com/googleapis/python-ndb/pull/175))
- Raise an exception when storing entity with partial key without Datastore. ([#171](https://github.com/googleapis/python-ndb/pull/171))
- Normalize to prefer ``project`` over ``app``. ([#170](https://github.com/googleapis/python-ndb/pull/170))
- Enforce naive datetimes for ``DateTimeProperty``. ([#167](https://github.com/googleapis/python-ndb/pull/167))
- Handle projections with structured properties. ([#166](https://github.com/googleapis/python-ndb/pull/166))
- Fix polymodel put and get ([#151](https://github.com/googleapis/python-ndb/pull/151))
- `_prepare_for_put` was not being called at entity level ([#138](https://github.com/googleapis/python-ndb/pull/138))
- Fix key property. ([#136](https://github.com/googleapis/python-ndb/pull/136))
- Fix thread local context. ([#131](https://github.com/googleapis/python-ndb/pull/131))
- Bugfix: Respect ``_indexed`` flag of properties. ([#127](https://github.com/googleapis/python-ndb/pull/127))
- Backwards compatibility with older style structured properties. ([#126](https://github.com/googleapis/python-ndb/pull/126))

### New Features
- Read legacy data with Repeated Structured Expando properties. ([#176](https://github.com/googleapis/python-ndb/pull/176))
- Implement ``Context.call_on_commit``. ([#159](https://github.com/googleapis/python-ndb/pull/159))
- Implement ``Context.flush`` ([#158](https://github.com/googleapis/python-ndb/pull/158))
- Implement ``use_datastore`` flag. ([#155](https://github.com/googleapis/python-ndb/pull/155))
- Implement ``tasklets.toplevel``. ([#157](https://github.com/googleapis/python-ndb/pull/157))
- Add RedisCache implementation of global cache ([#150](https://github.com/googleapis/python-ndb/pull/150))
- Implement Global Cache ([#148](https://github.com/googleapis/python-ndb/pull/148))
- ndb.Expando properties load and save ([#117](https://github.com/googleapis/python-ndb/pull/117))
- Implement cache policy. ([#116](https://github.com/googleapis/python-ndb/pull/116))

### Documentation
- Fix Kokoro publish-docs job ([#153](https://github.com/googleapis/python-ndb/pull/153))
- Update Migration Notes. ([#152](https://github.com/googleapis/python-ndb/pull/152))
- Add `project_urls` for pypi page ([#144](https://github.com/googleapis/python-ndb/pull/144))
- Fix `TRAMPOLINE_BUILD_FILE` in docs/common.cfg. ([#143](https://github.com/googleapis/python-ndb/pull/143))
- Add kokoro docs job to publish to googleapis.dev. ([#142](https://github.com/googleapis/python-ndb/pull/142))
- Initial version of migration guide ([#121](https://github.com/googleapis/python-ndb/pull/121))
- Add spellcheck sphinx extension to docs build process ([#123](https://github.com/googleapis/python-ndb/pull/123))

### Internal / Testing Changes
- Clean up usage of `object.__new__` and mocks for `Model` in unit tests ([#177](https://github.com/googleapis/python-ndb/pull/177))
- Prove tasklets can be Python 2.7 and 3.7 compatible. ([#174](https://github.com/googleapis/python-ndb/pull/174))
- Discard src directory and fix flake8 failures ([#173](https://github.com/googleapis/python-ndb/pull/173))
- Add tests for `Model.__eq__()` ([#169](https://github.com/googleapis/python-ndb/pull/169))
- Remove skip flag accidentally left over ([#154](https://github.com/googleapis/python-ndb/pull/154))
- Try to get kokoro to add indexes for system tests ([#145](https://github.com/googleapis/python-ndb/pull/145))
- Add system test for PolyModel ([#133](https://github.com/googleapis/python-ndb/pull/133))
- Fix system test under Datastore Emulator. (Fixes [#118](https://github.com/googleapis/python-ndb/pull/118)) ([#119](https://github.com/googleapis/python-ndb/pull/119))
- Add unit tests for `_entity_from_ds_entity` expando support ([#120](https://github.com/googleapis/python-ndb/pull/120))

## 0.0.1

06-11-2019 16:30 PDT

### Implementation Changes
- Query repeated structured properties. ([#103](https://github.com/googleapis/python-ndb/pull/103))
- Fix Structured Properties ([#102](https://github.com/googleapis/python-ndb/pull/102))

### New Features
- Implement expando model ([#99](https://github.com/googleapis/python-ndb/pull/99))
- Model properties ([#96](https://github.com/googleapis/python-ndb/pull/96))
- Implemented tasklets.synctasklet ([#58](https://github.com/googleapis/python-ndb/pull/58))
- Implement LocalStructuredProperty ([#93](https://github.com/googleapis/python-ndb/pull/93))
- Implement hooks. ([#95](https://github.com/googleapis/python-ndb/pull/95))
- Three easy Model methods. ([#94](https://github.com/googleapis/python-ndb/pull/94))
- Model.get or insert ([#92](https://github.com/googleapis/python-ndb/pull/92))
- Implement ``Model.get_by_id`` and ``Model.get_by_id_async``.
- Implement ``Model.allocate_ids`` and ``Model.allocate_ids_async``.
- Implement ``Query.fetch_page`` and ``Query.fetch_page_async``.
- Implement ``Query.count`` and ``Query.count_async``
- Implement ``Query.get`` and ``Query.get_async``.

### Documentation
- update sphinx version and eliminate all warnings ([#105](https://github.com/googleapis/python-ndb/pull/105))

## 0.0.1dev1

Initial development release of NDB client library.
