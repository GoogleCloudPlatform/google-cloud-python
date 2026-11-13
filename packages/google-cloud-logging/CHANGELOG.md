# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-logging/#history

## [3.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.16.3...google-cloud-logging-v3.17.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [3.16.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.16.2...google-cloud-logging-v3.16.3) (2026-08-21)


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [3.16.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.16.1...google-cloud-logging-v3.16.2) (2026-08-06)


### Bug Fixes

* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [3.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.16.0...google-cloud-logging-v3.16.1) (2026-07-07)


### Documentation

* **logging:** fix StructuredLogHandler docstring parameter name ([#17625](https://github.com/googleapis/google-cloud-python/issues/17625)) ([32862f0](https://github.com/googleapis/google-cloud-python/commit/32862f0a2c1c9570cc8e96f371c3188800c7d307)), closes [#17604](https://github.com/googleapis/google-cloud-python/issues/17604)

## [3.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.15.0...google-cloud-logging-v3.16.0) (2026-06-02)


### Features

* drop support for Python 3.7, 3.8, and 3.9 runtimes (#17276) ([014e951b6a1a07cb25baf4286e433a0c28783314](https://github.com/googleapis/google-cloud-python/commit/014e951b6a1a07cb25baf4286e433a0c28783314))

## [3.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.14.0...google-cloud-logging-v3.15.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [3.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-logging-v3.13.0...google-cloud-logging-v3.14.0) (2026-03-05)


### Features

* support mTLS certificates when available (#1071) ([c73e43906298e99405830d69a8383f71b85bd75b](https://github.com/googleapis/google-cloud-python/commit/c73e43906298e99405830d69a8383f71b85bd75b))

## [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)


### Features

* Add support for python 3.14 (#1065) ([6be3df6aa94539cd2ab22a4fac55b343862228b2](https://github.com/googleapis/python-logging/commit/6be3df6aa94539cd2ab22a4fac55b343862228b2))


### Bug Fixes

* remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3281f1df13f3aba6b19bc4e9397297f3d](https://github.com/googleapis/python-logging/commit/70f612c3281f1df13f3aba6b19bc4e9397297f3d))

## [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)


### Bug Fixes

* Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))

## [3.12.0](https://github.com/googleapis/python-logging/compare/v3.11.4...v3.12.0) (2025-04-10)


### Features

* Add REST Interceptors which support reading metadata ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
* Add support for opt-in debug logging ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
* Added flushes/close functionality to logging handlers ([#917](https://github.com/googleapis/python-logging/issues/917)) ([d179304](https://github.com/googleapis/python-logging/commit/d179304b344277e349456f72cd90c56f28011286))


### Bug Fixes

* Allow protobuf 6.x ([#977](https://github.com/googleapis/python-logging/issues/977)) ([6757890](https://github.com/googleapis/python-logging/commit/675789001344fdae68ee20ec14e14c11c83a0433))
* **deps:** Require google-cloud-audit-log &gt;= 0.3.1 ([#979](https://github.com/googleapis/python-logging/issues/979)) ([1cc00ec](https://github.com/googleapis/python-logging/commit/1cc00ecf646a7a36eb32afd2e5df3d9aa7f564b1))
* Fix typing issue with gRPC metadata when key ends in -bin ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))


### Documentation

* Added documentation on log_level and excluded_loggers params in setup_logging ([#971](https://github.com/googleapis/python-logging/issues/971)) ([70d9d25](https://github.com/googleapis/python-logging/commit/70d9d25bf8c3c85a3c5523ecc7fbdbf72f08c583))
* Update README to break infinite redirect loop ([#972](https://github.com/googleapis/python-logging/issues/972)) ([52cd907](https://github.com/googleapis/python-logging/commit/52cd907bb313df2766ec11e3d24c7e10cda31ca7))

## [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)


### Bug Fixes

* Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
* Require proto-plus &gt;= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
* Require proto-plus &gt;= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))

## [3.11.3](https://github.com/googleapis/python-logging/compare/v3.11.2...v3.11.3) (2024-10-15)


### Bug Fixes

* 16-bit hexadecimal formatting for XCTC span IDs ([#946](https://github.com/googleapis/python-logging/issues/946)) ([1f2b190](https://github.com/googleapis/python-logging/commit/1f2b190c0d1a7125d9412c157915d0011cdd4c47))

## [3.11.2](https://github.com/googleapis/python-logging/compare/v3.11.1...v3.11.2) (2024-08-15)


### Bug Fixes

* **deps:** Require google-cloud-appengine-logging&gt;=0.1.3 ([550abca](https://github.com/googleapis/python-logging/commit/550abca2846218d114a6b4b42cb165489e630374))
* **deps:** Require google-cloud-audit-log &gt;= 0.2.4 ([550abca](https://github.com/googleapis/python-logging/commit/550abca2846218d114a6b4b42cb165489e630374))
* **deps:** Require opentelemetry-api&gt;=1.9.0 ([550abca](https://github.com/googleapis/python-logging/commit/550abca2846218d114a6b4b42cb165489e630374))
* Fixed type hinting issue with specifying Transport class ([#930](https://github.com/googleapis/python-logging/issues/930)) ([e2875d6](https://github.com/googleapis/python-logging/commit/e2875d664c153a4328bd42790dfb7b4ac36a9048))

## [3.11.1](https://github.com/googleapis/python-logging/compare/v3.11.0...v3.11.1) (2024-08-06)


### Bug Fixes

* Allow protobuf 5.x ([#888](https://github.com/googleapis/python-logging/issues/888)) ([7746e64](https://github.com/googleapis/python-logging/commit/7746e643af29b1008d6e6d6a9958c8337c958dd4))

## [3.11.0](https://github.com/googleapis/python-logging/compare/v3.10.0...v3.11.0) (2024-07-15)


### Features

* OpenTelemetry trace/spanID integration for Python handlers ([#889](https://github.com/googleapis/python-logging/issues/889)) ([78168a3](https://github.com/googleapis/python-logging/commit/78168a38577b698130a861af4e4d229f42660330))


### Bug Fixes

* Added environment specific labels to client library when running in Cloud Run Jobs ([#877](https://github.com/googleapis/python-logging/issues/877)) ([9c5e8f0](https://github.com/googleapis/python-logging/commit/9c5e8f0548f88235fe6474469bc37685e2498dd1))
* Added missing import into logger.py ([#896](https://github.com/googleapis/python-logging/issues/896)) ([9ca242d](https://github.com/googleapis/python-logging/commit/9ca242d10f9f3bca120b292f478d62f5fa1d3c06))
* Added type hints to CloudLoggingHandler constructor ([#903](https://github.com/googleapis/python-logging/issues/903)) ([6959345](https://github.com/googleapis/python-logging/commit/69593459614be968f7a0136aa76701c4fc408834))


### Documentation

* Add summary_overview template ([#878](https://github.com/googleapis/python-logging/issues/878)) ([b60714c](https://github.com/googleapis/python-logging/commit/b60714cb1cc3aac79c86225f8f9cbd24d8ab170f))
* Changed table in web-framework-integration to bulleted list ([#875](https://github.com/googleapis/python-logging/issues/875)) ([a4aa3a7](https://github.com/googleapis/python-logging/commit/a4aa3a7cf1e3bb32ec2772084a7dc6c16e1454ff))
* Documentation update for OpenTelemetry ([#915](https://github.com/googleapis/python-logging/issues/915)) ([2a0539a](https://github.com/googleapis/python-logging/commit/2a0539a30e6dcf45c0970e3aacfd4a2772877526))
* Update `dictConfig` snippet ([#885](https://github.com/googleapis/python-logging/issues/885)) ([6264107](https://github.com/googleapis/python-logging/commit/62641075042a3da9bb9c059d963bad14a1586b1c))

## [3.10.0](https://github.com/googleapis/python-logging/compare/v3.9.0...v3.10.0) (2024-03-13)


### Features

* Allow users to explicitly configure universe domain ([#846](https://github.com/googleapis/python-logging/issues/846)) ([e998a21](https://github.com/googleapis/python-logging/commit/e998a219740cf8b2373e462867244a6860b0c88c))


### Bug Fixes

* Added placeholder kwargs to StructuredLogHandler ([#845](https://github.com/googleapis/python-logging/issues/845)) ([9bc0a37](https://github.com/googleapis/python-logging/commit/9bc0a37d910340d828db8bab33d67785f184f00c))
* Allowed for a partial override of loggers that get excluded from setup_client ([#831](https://github.com/googleapis/python-logging/issues/831)) ([870c940](https://github.com/googleapis/python-logging/commit/870c9403e03d31a0f22dddc257cd5fb2b4fc5ee3))
* Remove usage in including_default_value_fields to prepare for protobuf 5.x ([#866](https://github.com/googleapis/python-logging/issues/866)) ([66a534d](https://github.com/googleapis/python-logging/commit/66a534d1b83d7c63f5c7b013bf27ed54dd2786c3))
* Use value of cluster-location in GKE for tagging location ([#830](https://github.com/googleapis/python-logging/issues/830)) ([c15847c](https://github.com/googleapis/python-logging/commit/c15847c215c18ad3970efba12f5d337e6d499883))


### Documentation

* Added documentation for Django/Flask integrations and dictConfig ([#848](https://github.com/googleapis/python-logging/issues/848)) ([c65ec92](https://github.com/googleapis/python-logging/commit/c65ec92bf348e2bcdd8f4c5bacc152cfb4737eb1))

## [3.9.0](https://github.com/googleapis/python-logging/compare/v3.8.0...v3.9.0) (2023-12-08)


### Features

* Add support for Python 3.12 ([#813](https://github.com/googleapis/python-logging/issues/813)) ([6591b53](https://github.com/googleapis/python-logging/commit/6591b53e3fcd67e156765f329700443647b70349))
* Use native namespaces instead of pkg_resources ([#812](https://github.com/googleapis/python-logging/issues/812)) ([10ad75d](https://github.com/googleapis/python-logging/commit/10ad75d2b9276df389f5069f9f143f8f4621d04d))


### Bug Fixes

* Fixed DeprecationWarning for datetime objects for Python 3.12 ([#824](https://github.com/googleapis/python-logging/issues/824)) ([2384981](https://github.com/googleapis/python-logging/commit/2384981c9137a57a647a69a32b67dcacd619ea0a))
* Fixed object paths in autogenerated code in owlbot.py ([#804](https://github.com/googleapis/python-logging/issues/804)) ([b14bb14](https://github.com/googleapis/python-logging/commit/b14bb144fad2dcf067b7e62e402b708f45ebadbe))
* Updated protobuf JSON formatting to support nested protobufs ([#797](https://github.com/googleapis/python-logging/issues/797)) ([a00c261](https://github.com/googleapis/python-logging/commit/a00c261ee07a5dcaac9f5b966b4bb6729a2bbe65))
* Use `retry_async` instead of `retry` in async client ([#816](https://github.com/googleapis/python-logging/issues/816)) ([c79f7f5](https://github.com/googleapis/python-logging/commit/c79f7f55dddb170eac29f24b23bfe1dde8bfbda8))
* Use warning instead of warn in system tests to avoid DeprecationWarning ([#821](https://github.com/googleapis/python-logging/issues/821)) ([c447175](https://github.com/googleapis/python-logging/commit/c4471758e1efee0e3599b08969449b2ce71bd1b4))

## [3.8.0](https://github.com/googleapis/python-logging/compare/v3.7.0...v3.8.0) (2023-10-03)


### Features

* Add cloud_run_job monitored resource type. ([#788](https://github.com/googleapis/python-logging/issues/788)) ([3b310d6](https://github.com/googleapis/python-logging/commit/3b310d68b68df5bb31e21ac30b23207ef50c3f6f))

## [3.7.0](https://github.com/googleapis/python-logging/compare/v3.6.0...v3.7.0) (2023-09-25)


### Features

* Add ConfigServiceV2.CreateBucketAsync method for creating Log Buckets asynchronously ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add ConfigServiceV2.CreateLink method for creating linked datasets for Log Analytics Buckets ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add ConfigServiceV2.DeleteLink method for deleting linked datasets ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add ConfigServiceV2.GetLink methods for describing linked datasets ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add ConfigServiceV2.ListLinks method for listing linked datasets ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add ConfigServiceV2.UpdateBucketAsync method for creating Log Buckets asynchronously ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add LogBucket.analytics_enabled field that specifies whether Log Bucket's Analytics features are enabled ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add LogBucket.index_configs field that contains a list of Log Bucket's indexed fields and related configuration data ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Log Analytics features of the Cloud Logging API ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))


### Bug Fixes

* Add async context manager return types ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Add severity to structured log write ([#783](https://github.com/googleapis/python-logging/issues/783)) ([31a7f69](https://github.com/googleapis/python-logging/commit/31a7f69ed94719546136a3bf1b3ecdb28e369414))
* Handle exceptions raised when fetching Django request data ([#758](https://github.com/googleapis/python-logging/issues/758)) ([5ecf886](https://github.com/googleapis/python-logging/commit/5ecf88606b4f29b00ff8b18ae71c151d203d5c3b))
* Unintended exception omittion ([#736](https://github.com/googleapis/python-logging/issues/736)) ([022dc54](https://github.com/googleapis/python-logging/commit/022dc545f781648043296b3ca04d835fcb6f1d7e))


### Documentation

* Documentation for the Log Analytics features of the Cloud Logging API ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))
* Minor formatting ([30f24a8](https://github.com/googleapis/python-logging/commit/30f24a8bb3b0be2511264a18c3c93bdd3996fc93))

## [3.6.0](https://github.com/googleapis/python-logging/compare/v3.5.0...v3.6.0) (2023-07-05)


### Features

* Add logic to convert severity string to uppercase  ([#744](https://github.com/googleapis/python-logging/issues/744)) ([c1c8ce1](https://github.com/googleapis/python-logging/commit/c1c8ce158f566150319c2d4fb2f068b10668d507))


### Bug Fixes

* Properly handle None from metadata server ([#718](https://github.com/googleapis/python-logging/issues/718)) ([dedaff9](https://github.com/googleapis/python-logging/commit/dedaff95b2e2ed178a26aa9a04cfafb9b803ec60))


### Documentation

* Fix formatting of request arg in docstring ([#734](https://github.com/googleapis/python-logging/issues/734)) ([dbb1794](https://github.com/googleapis/python-logging/commit/dbb179407f20beb0f8927570dbc1630c62b23268))

## [3.5.0](https://github.com/googleapis/python-logging/compare/v3.4.0...v3.5.0) (2023-01-24)


### Features

* Add support for Python 3.11 ([412d481](https://github.com/googleapis/python-logging/commit/412d481701a62dcdeaa728414dbc82a6edb72c31))


### Bug Fixes

* Add context manager return types ([e2278c1](https://github.com/googleapis/python-logging/commit/e2278c11fba3d489efad1d42d09d5f05783f2a46))
* Instrumentation entries should not contain user labels ([#703](https://github.com/googleapis/python-logging/issues/703)) ([e05d132](https://github.com/googleapis/python-logging/commit/e05d132437739e61983bbda4742d5f4587eecdf2))
* Require proto-plus 1.22.2 for Python 3.11 ([412d481](https://github.com/googleapis/python-logging/commit/412d481701a62dcdeaa728414dbc82a6edb72c31))
* Send StructuredLogHandler instrumentation log using an explicit logger ([#705](https://github.com/googleapis/python-logging/issues/705)) ([ac6a2c6](https://github.com/googleapis/python-logging/commit/ac6a2c6742b9a620599fa0f4707badf138689645))


### Documentation

* Add documentation for enums ([e2278c1](https://github.com/googleapis/python-logging/commit/e2278c11fba3d489efad1d42d09d5f05783f2a46))

## [3.4.0](https://github.com/googleapis/python-logging/compare/v3.3.1...v3.4.0) (2022-12-15)


### Features

* Add typing to proto.Message based class attributes ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))


### Bug Fixes

* Add dict typing for client_options ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))
* Drop usage of pkg_resources ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))
* Fix timeout default values ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([9d505f1](https://github.com/googleapis/python-logging/commit/9d505f1147ccac8632590b4322945a900ff3c5c2))

## [3.3.1](https://github.com/googleapis/python-logging/compare/v3.3.0...v3.3.1) (2022-12-05)


### Bug Fixes

* Client_info default values ([#681](https://github.com/googleapis/python-logging/issues/681)) ([b74d2a8](https://github.com/googleapis/python-logging/commit/b74d2a8c4f34aece5dc851de0e7542b3229751ba))

## [3.3.0](https://github.com/googleapis/python-logging/compare/v3.2.4...v3.3.0) (2022-11-26)


### Features

* Add support to custom JSON encoders ([#657](https://github.com/googleapis/python-logging/issues/657)) ([77e621c](https://github.com/googleapis/python-logging/commit/77e621cb85b726a801227da85c31319f25969d19))
* Include context on batch log errors ([#650](https://github.com/googleapis/python-logging/issues/650)) ([d08be9a](https://github.com/googleapis/python-logging/commit/d08be9ae26c70f94e4a264e2bc518dd8a8dbae91))
* Set partial_success to default to true for batched logs ([#649](https://github.com/googleapis/python-logging/issues/649)) ([e56d3e8](https://github.com/googleapis/python-logging/commit/e56d3e83859e20fbbd9cd22d3275ff123f79d6c9))
* Support Django asgi middleware ([#625](https://github.com/googleapis/python-logging/issues/625)) ([f52b3aa](https://github.com/googleapis/python-logging/commit/f52b3aae28e7ed5809fc5470213b2a1c6f7d77bd))


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#644](https://github.com/googleapis/python-logging/issues/644)) ([12f3001](https://github.com/googleapis/python-logging/commit/12f3001d834e858dbbbcdaab5894ec25a14c6820))
* Json fields dictionary has modification side effect ([#654](https://github.com/googleapis/python-logging/issues/654)) ([a62a0d6](https://github.com/googleapis/python-logging/commit/a62a0d66cb8c07e617636e5ed54961f5e28164ae))

## [3.2.4](https://github.com/googleapis/python-logging/compare/v3.2.3...v3.2.4) (2022-10-04)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#633](https://github.com/googleapis/python-logging/issues/633)) ([b4da4ce](https://github.com/googleapis/python-logging/commit/b4da4ceaaf757235c019e90022aaefcefd47150a))

## [3.2.3](https://github.com/googleapis/python-logging/compare/v3.2.2...v3.2.3) (2022-09-30)


### Bug Fixes

* Mimic the pubsub test to clean up bigquery datasets ([#639](https://github.com/googleapis/python-logging/issues/639)) ([44deb1b](https://github.com/googleapis/python-logging/commit/44deb1bd63a1367528c57d6a732ba8a4e0dce318))
* Nested json with structured log handler ([#636](https://github.com/googleapis/python-logging/issues/636)) ([b840435](https://github.com/googleapis/python-logging/commit/b8404351484cbec22a372a8c2b16dcb4bf4b756a))
* Structured log handler drops reserved fields in json_fields ([#634](https://github.com/googleapis/python-logging/issues/634)) ([4ef38b3](https://github.com/googleapis/python-logging/commit/4ef38b3942f6750348916a28e995e2c1c169e071))

## [3.2.2](https://github.com/googleapis/python-logging/compare/v3.2.1...v3.2.2) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#600](https://github.com/googleapis/python-logging/issues/600)) ([8495dac](https://github.com/googleapis/python-logging/commit/8495dac2f303dae74b0143d7c95189d0f2d180b8))
* **deps:** require proto-plus >= 1.22.0 ([8495dac](https://github.com/googleapis/python-logging/commit/8495dac2f303dae74b0143d7c95189d0f2d180b8))

## [3.2.1](https://github.com/googleapis/python-logging/compare/v3.2.0...v3.2.1) (2022-07-13)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#585](https://github.com/googleapis/python-logging/issues/585)) ([de35eab](https://github.com/googleapis/python-logging/commit/de35eabaa346b4ab8b8436841e4d82f83e10299a))

## [3.2.0](https://github.com/googleapis/python-logging/compare/v3.1.2...v3.2.0) (2022-07-11)


### Features

* add audience parameter ([a2eed8c](https://github.com/googleapis/python-logging/commit/a2eed8c5de4f5ee995b6b7392c0e94dc72e56415))
* Add support for library instrumentation ([#551](https://github.com/googleapis/python-logging/issues/551)) ([8ba0023](https://github.com/googleapis/python-logging/commit/8ba002386560f2b94756c8cd0e32a8b61cdeb78b))


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#575](https://github.com/googleapis/python-logging/issues/575)) ([a2eed8c](https://github.com/googleapis/python-logging/commit/a2eed8c5de4f5ee995b6b7392c0e94dc72e56415))
* **deps:** require google-cloud-core >= 2.0.0 ([a2eed8c](https://github.com/googleapis/python-logging/commit/a2eed8c5de4f5ee995b6b7392c0e94dc72e56415))
* require python 3.7+ ([#580](https://github.com/googleapis/python-logging/issues/580)) ([0b3eb52](https://github.com/googleapis/python-logging/commit/0b3eb5255f3294f9631deec3425a89cb06dc2c14))

## [3.1.2](https://github.com/googleapis/python-logging/compare/v3.1.1...v3.1.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#564](https://github.com/googleapis/python-logging/issues/564)) ([cb0720c](https://github.com/googleapis/python-logging/commit/cb0720ceac84f4cebe3d79e4a01eea6728da8f05))


### Documentation

* fix changelog header to consistent size ([#562](https://github.com/googleapis/python-logging/issues/562)) ([3f16107](https://github.com/googleapis/python-logging/commit/3f16107ef02f85a405d2608862ffc0a73cdc8e48))
* Update README image to absolute URL, fix PyPI rendering ([#561](https://github.com/googleapis/python-logging/issues/561)) ([76413b1](https://github.com/googleapis/python-logging/commit/76413b1c405019d8ed6044f0213f7983c38673cb))

## [3.1.1](https://github.com/googleapis/python-logging/compare/v3.1.0...v3.1.1) (2022-05-23)


### Documentation

* Change button in README to .png file ([#554](https://github.com/googleapis/python-logging/issues/554)) ([e297747](https://github.com/googleapis/python-logging/commit/e2977477f97469671b8cbfc920f39743cf2f7c80))

## [3.1.0](https://github.com/googleapis/python-logging/compare/v3.0.0...v3.1.0) (2022-05-08)


### Features

* KMS configuration in settings ([#489](https://github.com/googleapis/python-logging/issues/489)) ([6699f8c](https://github.com/googleapis/python-logging/commit/6699f8c545d1a9904a945a9d789d7220da9433bf))
* Update Logging API with latest changes ([6699f8c](https://github.com/googleapis/python-logging/commit/6699f8c545d1a9904a945a9d789d7220da9433bf))


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#494](https://github.com/googleapis/python-logging/issues/494)) ([ab14563](https://github.com/googleapis/python-logging/commit/ab145630ffbb25a88cc058569b9e425e62b32ced))
* fix system test for mtls ([#485](https://github.com/googleapis/python-logging/issues/485)) ([96bb6f7](https://github.com/googleapis/python-logging/commit/96bb6f786c91656b52624fbbf52e036b1a908d53))
* Reenable staleness bot ([#535](https://github.com/googleapis/python-logging/issues/535)) ([1595e42](https://github.com/googleapis/python-logging/commit/1595e4203faeb3d46b28a7d98f68761998e3aa26))
* remove unnecessary detect_resource calls from CloudLoggingHandler ([#484](https://github.com/googleapis/python-logging/issues/484)) ([def7440](https://github.com/googleapis/python-logging/commit/def7440ac6964451f3202b5117e3060ec62045b0))
* resolve DuplicateCredentialArgs error when using credentials_file ([265061e](https://github.com/googleapis/python-logging/commit/265061eae8396caaef3fdfeae80e0a120f9a5cda))


### Dependencies

* Pin jinja2 version to fix CI ([#522](https://github.com/googleapis/python-logging/issues/522)) ([383f2f0](https://github.com/googleapis/python-logging/commit/383f2f0062d3703dfc7e2c331562fb88327cdf38))


### Documentation

* add generated snippets ([6699f8c](https://github.com/googleapis/python-logging/commit/6699f8c545d1a9904a945a9d789d7220da9433bf))
* Add link to interactive walkthrough ([#541](https://github.com/googleapis/python-logging/issues/541)) ([422a77d](https://github.com/googleapis/python-logging/commit/422a77d93655fba3406ecf397cf417ad37dd1ce1))

## [3.0.0](https://github.com/googleapis/python-logging/compare/v2.7.0...v3.0.0) (2022-01-27)


### ⚠ BREAKING CHANGES

* make logging API more friendly to use (#422)
* api consistency between HTTP and Gapic layers (#375)
* support string-encoded json (#339)
* Infer default resource in logger (#315)
* support json logs (#316)
* deprecate AppEngineHandler and ContainerEngineHandler (#310)

### Features

* add api key support ([#472](https://github.com/googleapis/python-logging/issues/472)) ([81ca8c6](https://github.com/googleapis/python-logging/commit/81ca8c616acb988be1fbecfc2a0b1a5b39280149))
* add json_fields extras argument for adding to jsonPayload ([#447](https://github.com/googleapis/python-logging/issues/447)) ([a760e02](https://github.com/googleapis/python-logging/commit/a760e02371a55d6262e42de9e0222fffa2c7192b))
* avoid importing grpc when explicitly disabled ([#416](https://github.com/googleapis/python-logging/issues/416)) ([818213e](https://github.com/googleapis/python-logging/commit/818213e143d6a1941211a48e0b23069a426ac300))
* Infer default resource in logger ([#315](https://github.com/googleapis/python-logging/issues/315)) ([c632503](https://github.com/googleapis/python-logging/commit/c63250399fcd6e1317d341e98fab11095c443e5e))
* make logging API more friendly to use ([#422](https://github.com/googleapis/python-logging/issues/422)) ([83d9ca8](https://github.com/googleapis/python-logging/commit/83d9ca8521fe7c470bb6755a48a97496515d7abc))
* support json logs ([#316](https://github.com/googleapis/python-logging/issues/316)) ([5267152](https://github.com/googleapis/python-logging/commit/5267152574b2ee96eb6f5c536a762f58bd2f886e))
* support string-encoded json ([#339](https://github.com/googleapis/python-logging/issues/339)) ([6fa1773](https://github.com/googleapis/python-logging/commit/6fa17735fe3edb45483ec5e3abd1f53c24ffa881))
* trace improvements ([#450](https://github.com/googleapis/python-logging/issues/450)) ([e0c5fc0](https://github.com/googleapis/python-logging/commit/e0c5fc02160ae87faf4ba5c2b62be86de6b02cf3))


### Bug Fixes

* allow reading logs from non-project paths ([#444](https://github.com/googleapis/python-logging/issues/444)) ([97e32b6](https://github.com/googleapis/python-logging/commit/97e32b67603553fe350b6327455fc9f80b8aa6ce))
* api consistency between HTTP and Gapic layers ([#375](https://github.com/googleapis/python-logging/issues/375)) ([e1506fa](https://github.com/googleapis/python-logging/commit/e1506fa9030776353878048ce562c53bf6ccf7bf))


### Miscellaneous Chores

* deprecate AppEngineHandler and ContainerEngineHandler ([#310](https://github.com/googleapis/python-logging/issues/310)) ([e3cac88](https://github.com/googleapis/python-logging/commit/e3cac888d40bf67af11e57b74615b0c3b8e8aa3e))


### Documentation

* update usage guide for v3.0.0 ([#456](https://github.com/googleapis/python-logging/issues/456)) ([8a67b73](https://github.com/googleapis/python-logging/commit/8a67b73cdfcb9da545671be6cf59c724360b1544))

## [2.7.0](https://www.github.com/googleapis/python-logging/compare/v2.6.0...v2.7.0) (2021-11-02)


### Features

* add context manager support in client ([#415](https://www.github.com/googleapis/python-logging/issues/415)) ([f5af164](https://www.github.com/googleapis/python-logging/commit/f5af16439807a0954ee78fa91cb69b9493b80176))
* added support for iam AuditData proto ([#396](https://www.github.com/googleapis/python-logging/issues/396)) ([e3a1eba](https://www.github.com/googleapis/python-logging/commit/e3a1eba74dd8b67bcc73a78f784189ef2a9927c2))
* use structured logging on GCF with python 3.7 ([#434](https://www.github.com/googleapis/python-logging/issues/434)) ([5055919](https://www.github.com/googleapis/python-logging/commit/5055919f70c82b38de6d1fa7f1df6006865a857b))


### Bug Fixes

* add 'dict' annotation type to 'request' ([76ac729](https://www.github.com/googleapis/python-logging/commit/76ac729e42a782524be87ad71745aad37bbe1653))
* add 'dict' annotation type to 'request' ([23f9e1f](https://www.github.com/googleapis/python-logging/commit/23f9e1f6e9af30c4e65578edbf73c8c893b35285))
* **deps:** drop packaging dependency ([9d38995](https://www.github.com/googleapis/python-logging/commit/9d389958c7de31ae9e21228eaf965762b31d5e48))
* **deps:** require google-api-core >= 1.28.0 ([9d38995](https://www.github.com/googleapis/python-logging/commit/9d389958c7de31ae9e21228eaf965762b31d5e48))
* **deps:** require proto-plus==1.15.0 ([76ac729](https://www.github.com/googleapis/python-logging/commit/76ac729e42a782524be87ad71745aad37bbe1653))
* exception log message format ([#394](https://www.github.com/googleapis/python-logging/issues/394)) ([c426bf5](https://www.github.com/googleapis/python-logging/commit/c426bf56787fa02140e8aa142ecd4d4e45432697))
* improper types in pagers generation ([76ac729](https://www.github.com/googleapis/python-logging/commit/76ac729e42a782524be87ad71745aad37bbe1653))
* improper types in pagers generation ([6a837a5](https://www.github.com/googleapis/python-logging/commit/6a837a5d1faab1f9fa8ac94e424e847821a0069f))


### Documentation

* list oneofs in docstring ([9d38995](https://www.github.com/googleapis/python-logging/commit/9d389958c7de31ae9e21228eaf965762b31d5e48))

## [2.6.0](https://www.github.com/googleapis/python-logging/compare/v2.5.0...v2.6.0) (2021-07-28)


### Features

* add always_use_jwt_access ([#334](https://www.github.com/googleapis/python-logging/issues/334)) ([ae67d10](https://www.github.com/googleapis/python-logging/commit/ae67d10a661a3561b366bb05f5cf6d34520164b4))


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#356](https://www.github.com/googleapis/python-logging/issues/356)) ([a970dd2](https://www.github.com/googleapis/python-logging/commit/a970dd293d4fddc983946cb1c362f487a82d9609))
* disable always_use_jwt_access ([#342](https://www.github.com/googleapis/python-logging/issues/342)) ([a95e401](https://www.github.com/googleapis/python-logging/commit/a95e40188c9483310fb1dce9242c7c66721a6b7f))
* enable self signed jwt for grpc ([#360](https://www.github.com/googleapis/python-logging/issues/360)) ([707fad1](https://www.github.com/googleapis/python-logging/commit/707fad1a714d951727336b03f4444f53199737e3))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-logging/issues/1127)) ([#327](https://www.github.com/googleapis/python-logging/issues/327)) ([faa6fb9](https://www.github.com/googleapis/python-logging/commit/faa6fb9a86c82b99b529e979160bfdd7a505793b)), closes [#1126](https://www.github.com/googleapis/python-logging/issues/1126)
* add Samples section to CONTRIBUTING.rst ([#357](https://www.github.com/googleapis/python-logging/issues/357)) ([8771716](https://www.github.com/googleapis/python-logging/commit/8771716cae7cf67d710b3741b8b718fc4a8aa2b6))


## [2.5.0](https://www.github.com/googleapis/python-logging/compare/v2.4.0...v2.5.0) (2021-06-10)


### Features

* support AuditLog and RequestLog protos ([#274](https://www.github.com/googleapis/python-logging/issues/274)) ([5d91be9](https://www.github.com/googleapis/python-logging/commit/5d91be9f121c364cbd53c6a9fffc4fb6ca6bd324))


### Bug Fixes

* **deps:** add packaging requirement ([#300](https://www.github.com/googleapis/python-logging/issues/300)) ([68c5cec](https://www.github.com/googleapis/python-logging/commit/68c5ceced3288253af8e3c6013a35fa3954b37bc))
* structured log handler formatting issues ([#319](https://www.github.com/googleapis/python-logging/issues/319)) ([db9da37](https://www.github.com/googleapis/python-logging/commit/db9da3700511b5a24c3c44c9f4377705937caf46))

## [2.4.0](https://www.github.com/googleapis/python-logging/compare/v2.3.1...v2.4.0) (2021-05-12)


### Features

* allow custom labels with standard library logging ([#264](https://www.github.com/googleapis/python-logging/issues/264)) ([fe4de39](https://www.github.com/googleapis/python-logging/commit/fe4de39a87581a9e9f2cee62462ae2f26176194f))
* Improve source location overrides ([#258](https://www.github.com/googleapis/python-logging/issues/258)) ([6b10b74](https://www.github.com/googleapis/python-logging/commit/6b10b74e2bf65ea406b10585a4c24078348483d2))
* record source locations ([#254](https://www.github.com/googleapis/python-logging/issues/254)) ([a5c2f8e](https://www.github.com/googleapis/python-logging/commit/a5c2f8e948bb116cbce313f063643aec02d06a84))
* support span inference ([#267](https://www.github.com/googleapis/python-logging/issues/267)) ([fcd26eb](https://www.github.com/googleapis/python-logging/commit/fcd26eb0ff4f97c097ca33b2d212d8f83e56686e))
* use standard output logs on serverless environments ([#228](https://www.github.com/googleapis/python-logging/issues/228)) ([a78f577](https://www.github.com/googleapis/python-logging/commit/a78f577bda17d758551237be84182035ed7b9cce))


### Bug Fixes

* changed region format on serverless ([#291](https://www.github.com/googleapis/python-logging/issues/291)) ([8872d6f](https://www.github.com/googleapis/python-logging/commit/8872d6f6b2bb979adffad0b054fa40306b68cfc0))
* changed region format on serverless ([#291](https://www.github.com/googleapis/python-logging/issues/291)) ([360d3d2](https://www.github.com/googleapis/python-logging/commit/360d3d23db7709b7c3946c092ef373f888f47c3d))
* **deps:** fix minimum required version of google-api-core ([#244](https://www.github.com/googleapis/python-logging/issues/244)) ([874fdfa](https://www.github.com/googleapis/python-logging/commit/874fdfa809063c2bfb33e59aded553e098601876))
* **deps:** fix minimum required version of google-api-core ([#244](https://www.github.com/googleapis/python-logging/issues/244)) ([37d33fc](https://www.github.com/googleapis/python-logging/commit/37d33fcd8402b973377486a572c04ba6d4029b58))
* improve API compatibility for next release ([#292](https://www.github.com/googleapis/python-logging/issues/292)) ([1f9517d](https://www.github.com/googleapis/python-logging/commit/1f9517da7302e19198e598d452df58238d4e6306))
* remove noisy logs ([#290](https://www.github.com/googleapis/python-logging/issues/290)) ([bdf8273](https://www.github.com/googleapis/python-logging/commit/bdf827358de5935f736ecd73ab10b2d861daf690))

## [2.3.1](https://www.github.com/googleapis/python-logging/compare/v2.3.0...v2.3.1) (2021-03-24)


### Bug Fixes

* detect project from environment instead of from logger ([#238](https://www.github.com/googleapis/python-logging/issues/238)) ([813b97c](https://www.github.com/googleapis/python-logging/commit/813b97cb936fa5acc2a4de567e2c84d746527e98))
* revert default resource behavior to avoid breaking changes ([#237](https://www.github.com/googleapis/python-logging/issues/237)) ([24a0a5e](https://www.github.com/googleapis/python-logging/commit/24a0a5e674430e97a3a2e3b54477d8f95fa08ec6))

## [2.3.0](https://www.github.com/googleapis/python-logging/compare/v2.2.0...v2.3.0) (2021-03-15)


### Features

* Add json setting to allow unicodes to show in log instead of ascii ch… ([#193](https://www.github.com/googleapis/python-logging/issues/193)) ([e8c8e30](https://www.github.com/googleapis/python-logging/commit/e8c8e30fc4f618273dec1415c752eed203c75b67))
* detect monitored resources on all GCP environments ([#200](https://www.github.com/googleapis/python-logging/issues/200)) ([4eda681](https://www.github.com/googleapis/python-logging/commit/4eda6813d19df8a119f1dcd47ff79389310d4a6f))


### Bug Fixes

* logger uses default resource ([#207](https://www.github.com/googleapis/python-logging/issues/207)) ([0f90a79](https://www.github.com/googleapis/python-logging/commit/0f90a79d165314d261413cc369408e15f711129f))
* no duplicate logs on GCF or GAE ([#209](https://www.github.com/googleapis/python-logging/issues/209)) ([37e6c8e](https://www.github.com/googleapis/python-logging/commit/37e6c8e90775ddc2fc454f5cb13cab04231c2222))


### Documentation

* add python std_logging to sample browser ([#173](https://www.github.com/googleapis/python-logging/issues/173)) ([7cc7275](https://www.github.com/googleapis/python-logging/commit/7cc727598c33e7e264ddbeef0a2604a3c215b260))

## [2.2.0](https://www.github.com/googleapis/python-logging/compare/v2.1.1...v2.2.0) (2021-01-27)


### Features

* add 'from_service_account_info' factory to clients ([a9ff2b7](https://www.github.com/googleapis/python-logging/commit/a9ff2b7984a54542963fc8d52864365ef1562f57))


### Bug Fixes

* django content length extraction bug ([#160](https://www.github.com/googleapis/python-logging/issues/160)) ([93eeaef](https://www.github.com/googleapis/python-logging/commit/93eeaef1cce286aa8aa830d2369212b912d184b6))
* fix sphinx identifiers ([a9ff2b7](https://www.github.com/googleapis/python-logging/commit/a9ff2b7984a54542963fc8d52864365ef1562f57))

## [2.1.1](https://www.github.com/googleapis/python-logging/compare/v2.1.0...v2.1.1) (2021-01-14)


### Bug Fixes

* use dict for http request ([#156](https://www.github.com/googleapis/python-logging/issues/156)) ([dc26668](https://www.github.com/googleapis/python-logging/commit/dc266688b1e465112de0e3fe2e8d98003f6e7033))

## [2.1.0](https://www.github.com/googleapis/python-logging/compare/v2.0.2...v2.1.0) (2021-01-12)


### Features

* allow modifying LogEntry data using extra argument ([#129](https://www.github.com/googleapis/python-logging/issues/129)) ([92b287f](https://www.github.com/googleapis/python-logging/commit/92b287f424418fde137cc81f370dcab07f84023b))
* support http_request field ([#120](https://www.github.com/googleapis/python-logging/issues/120)) ([ba94afb](https://www.github.com/googleapis/python-logging/commit/ba94afb7d0a5371f2d2de4232de56df34e8a1f99))


### Bug Fixes

* add InternalServerError to list of expected errors ([#151](https://www.github.com/googleapis/python-logging/issues/151)) ([9bf49f5](https://www.github.com/googleapis/python-logging/commit/9bf49f51df5321e8b9c39018dff7d767347256d6))


### Documentation

* fix usage guide ([#140](https://www.github.com/googleapis/python-logging/issues/140)) ([1ca3981](https://www.github.com/googleapis/python-logging/commit/1ca398103fdfefb5576d6ef2ba20cfa4bd4ab252))

## [2.0.2](https://www.github.com/googleapis/python-logging/compare/v2.0.1...v2.0.2) (2020-12-14)


### Bug Fixes

* Add submodule imports for handlers to logging alias ([#117](https://www.github.com/googleapis/python-logging/issues/117)) ([6843a3a](https://www.github.com/googleapis/python-logging/commit/6843a3aee3c0908ddbc493e7a9ecdddd01df34ef))
* remove client recv msg limit fix: add enums to `types/__init__.py` ([#131](https://www.github.com/googleapis/python-logging/issues/131)) ([6349b89](https://www.github.com/googleapis/python-logging/commit/6349b899811cbb16f5548df0b77564b46666c4e7))
* Remove keyword only argument for RequestsMiddleware ([#113](https://www.github.com/googleapis/python-logging/issues/113)) ([e704f28](https://www.github.com/googleapis/python-logging/commit/e704f287a40db38d0da42fa5e21e7a9ef73922ec))

## [2.0.1](https://www.github.com/googleapis/python-logging/compare/v2.0.0...v2.0.1) (2020-12-02)


### Bug Fixes

* remove duplicate stream handler ([#106](https://www.github.com/googleapis/python-logging/issues/106)) ([eb5cf40](https://www.github.com/googleapis/python-logging/commit/eb5cf407129fb76124d6a405c0805b70f2689cc4))


### Documentation

* fix logger documentation ([#100](https://www.github.com/googleapis/python-logging/issues/100)) ([6a46b46](https://www.github.com/googleapis/python-logging/commit/6a46b46a6bbc154c9b5b737859f108021ab5b201))

## [2.0.0](https://www.github.com/googleapis/python-logging/compare/v1.15.1...v2.0.0) (2020-11-19)


### ⚠ BREAKING CHANGES

* Use microgenerator for GAPIC layer. See [UPGRADING.md](https://github.com/googleapis/python-logging/blob/main/UPGRADING.md) for details. (#94)
* removes support for webapp2 and other Python2 specific code

### Features

* pass 'client_options' to super ctor ([#61](https://www.github.com/googleapis/python-logging/issues/61)) ([c4387b3](https://www.github.com/googleapis/python-logging/commit/c4387b307f8f3502fb53ae1f7e1144f6284280a4)), closes [#55](https://www.github.com/googleapis/python-logging/issues/55)
* use microgenerator ([#94](https://www.github.com/googleapis/python-logging/issues/94)) ([ff90fd2](https://www.github.com/googleapis/python-logging/commit/ff90fd2fb54c612fe6ab29708a2d5d984f60dea7))


### Bug Fixes

* add default filter settings to list_entries ([#73](https://www.github.com/googleapis/python-logging/issues/73)) ([0a1dd94](https://www.github.com/googleapis/python-logging/commit/0a1dd94811232634fdb849cb2c85bd44e870642f))
* failing CI tests ([#70](https://www.github.com/googleapis/python-logging/issues/70)) ([96adeed](https://www.github.com/googleapis/python-logging/commit/96adeedbda16a5c21651c356261442478aaa867a))


### Code Refactoring

* remove python2 ([#78](https://www.github.com/googleapis/python-logging/issues/78)) ([bf579e4](https://www.github.com/googleapis/python-logging/commit/bf579e4f871c92391a9f6f87eca931744158e31a))


### Documentation

* update docs ([#77](https://www.github.com/googleapis/python-logging/issues/77)) ([bdd9c44](https://www.github.com/googleapis/python-logging/commit/bdd9c440f29d1fcd6fb9545d8465c63efa6c0cea))

## [1.15.1](https://www.github.com/googleapis/python-logging/compare/v1.15.0...v1.15.1) (2020-07-01)


### Documentation

* add initialization of LogEntry instance in the v2 example ([#46](https://www.github.com/googleapis/python-logging/issues/46)) ([251ac93](https://www.github.com/googleapis/python-logging/commit/251ac9355b192121572552c1c9cfd4df94a42802)), closes [#44](https://www.github.com/googleapis/python-logging/issues/44)
* change descriptions for virtual environment ([#48](https://www.github.com/googleapis/python-logging/issues/48)) ([c5c3c15](https://www.github.com/googleapis/python-logging/commit/c5c3c153d1ae91f44c4104279baae9d9e4f88d03)), closes [#47](https://www.github.com/googleapis/python-logging/issues/47)

## [1.15.0](https://www.github.com/googleapis/python-logging/compare/v1.14.0...v1.15.0) (2020-02-26)


### Features

* add support for cmek settings; undeprecate resource name helper methods; bump copyright year to 2020 ([#22](https://www.github.com/googleapis/python-logging/issues/22)) ([1c687c1](https://www.github.com/googleapis/python-logging/commit/1c687c168cdc1f5ebc74d2380ad87335a42209a2))


### Bug Fixes

* **logging:** deprecate resource name helper methods (via synth) ([#9837](https://www.github.com/googleapis/python-logging/issues/9837)) ([335af9e](https://www.github.com/googleapis/python-logging/commit/335af9e909eb7fb4696ba906a82176611653531d))
* **logging:** update test assertion and core version pins ([#10087](https://www.github.com/googleapis/python-logging/issues/10087)) ([4aedea8](https://www.github.com/googleapis/python-logging/commit/4aedea80e2bccb5ba3c41fae7a0ee46cc07eefa9))
* replace unsafe six.PY3 with PY2 for better future compatibility with Python 4 ([#10081](https://www.github.com/googleapis/python-logging/issues/10081)) ([c6eb601](https://www.github.com/googleapis/python-logging/commit/c6eb60179d674dfd5137d90d209094c9369b3581))

## 1.14.0

10-15-2019 06:50 PDT


### Implementation Changes
- Fix proto copy. ([#9420](https://github.com/googleapis/google-cloud-python/pull/9420))

### Dependencies
- Pin 'google-cloud-core >= 1.0.3, < 2.0.0dev'. ([#9445](https://github.com/googleapis/google-cloud-python/pull/9445))

## 1.13.0

09-23-2019 10:00 PDT

### Implementation Changes
- Pass 'stream' argument to super in 'ContainerEngineHandler.__init__'. ([#9166](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/9166))

### New Features
- Add LoggingV2Servicer, LogSinks, logging_metrics, and log_entry. Add LogSeverity and HttpRequest types (via synth). ([#9262](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/9262))
- Add client_options to logging v1 ([#9046](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/9046))

### Documentation
- Remove compatability badges from READMEs. ([#9035](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/9035))

### Internal / Testing Changes
- Docs: Remove CI for gh-pages, use googleapis.dev for api_core refs. ([#9085](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/9085))
- Delete custom synth removing gRPC send/recv msg size limits. ([#8939](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/8939))

## 1.12.1

08-01-2019 09:45 PDT


### Implementation Changes
- Remove gRPC size restrictions (4MB default) ([#8860](https://github.com/googleapis/google-cloud-python/pull/8860))
- Map stdlib loglevels to Cloud Logging severity enum values. ([#8837](https://github.com/googleapis/google-cloud-python/pull/8837))

### Documentation
- Fix 'list_entries' example with projects. ([#8858](https://github.com/googleapis/google-cloud-python/pull/8858))

### Internal / Testing Changes
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 1.12.0

07-24-2019 16:47 PDT


### Implementation Changes
- Set the 'timestamp' on log records created by handler. ([#8227](https://github.com/googleapis/google-cloud-python/pull/8227))
- Clarify worker thread implementation. ([#8228](https://github.com/googleapis/google-cloud-python/pull/8228))

### New Features
- Add path-construction helpers to GAPIC clients (via synth). ([#8631](https://github.com/googleapis/google-cloud-python/pull/8631))
- Add 'client_options' support, update list method docstrings (via synth). ([#8535](https://github.com/googleapis/google-cloud-python/pull/8535))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

### Internal / Testing Changes
- Re-add "generated" markers (via synth). ([#8538](https://github.com/googleapis/google-cloud-python/pull/8538))
- Add nox session 'docs' to remaining manual clients. ([#8478](https://github.com/googleapis/google-cloud-python/pull/8478))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Fix tests broken in PR [#8227](https://github.com/googleapis/google-cloud-python/pull/8227). ([#8273](https://github.com/googleapis/google-cloud-python/pull/8273))
- Add empty lines. ([#8064](https://github.com/googleapis/google-cloud-python/pull/8064))
- Use alabaster theme everwhere. ([#8021](https://github.com/googleapis/google-cloud-python/pull/8021))

## 1.11.0

05-16-2019 12:27 PDT


### Implementation Changes
- Add routing header to method metadata (via synth). ([#7598](https://github.com/googleapis/google-cloud-python/pull/7598))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Use FQDN for GCE metadata endpoint. ([#7520](https://github.com/googleapis/google-cloud-python/pull/7520))

### New Features
- Add `client_info` support to client. ([#7874](https://github.com/googleapis/google-cloud-python/pull/7874)) and ([#7901](https://github.com/googleapis/google-cloud-python/pull/7901))

### Dependencies
- Pin `google-cloud-core >= 1.0.0, < 2.0dev`. ([#7993](https://github.com/googleapis/google-cloud-python/pull/7993))

### Documentation
- Update client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Reformat snippet (via synth). ([#7216](https://github.com/googleapis/google-cloud-python/pull/7216))
- Add snippet for logging a resource. ([#7212](https://github.com/googleapis/google-cloud-python/pull/7212))

### Internal / Testing Changes
- Reorder methods in file (via synth). ([#7810](https://github.com/googleapis/google-cloud-python/pull/7810))
- Copy lintified proto files (via synth). ([#7450](https://github.com/googleapis/google-cloud-python/pull/7450))
- Trivial gapic-generator change. ([#7230](https://github.com/googleapis/google-cloud-python/pull/7230))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))

## 1.10.0

01-17-2019 15:37 PST


### Implementation Changes
- Change WriteLogEntries retry policy.
- Protoc-generated serialization update. ([#7088](https://github.com/googleapis/google-cloud-python/pull/7088))
- GAPIC generation fixes. ([#7061](https://github.com/googleapis/google-cloud-python/pull/7061))

### Internal / Testing Changes
- Update copyright headers.
- Use 'python-3.6' for 'blacken' run. ([#7064](https://github.com/googleapis/google-cloud-python/pull/7064))

## 1.9.1

12-17-2018 16:49 PST


### Implementation Changes
- Allow setting name, args on default handler (post-blacken) ([#6828](https://github.com/googleapis/google-cloud-python/pull/6828))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Normalize docs for `page_size` / `max_results` / `page_token`. ([#6842](https://github.com/googleapis/google-cloud-python/pull/6842))

## 1.9.0

12-10-2018 12:55 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6631](https://github.com/googleapis/google-cloud-python/pull/6631))
- Fix `client_info` bug, update docstrings via synth. ([#6435](https://github.com/googleapis/google-cloud-python/pull/6435))
- Revert "Allow turning on JSON Detection in StackDriver" ([#6352](https://github.com/googleapis/google-cloud-python/pull/6352))
- Allow turning on JSON Detection in StackDriver ([#6293](https://github.com/googleapis/google-cloud-python/pull/6293))

### New Features
- Add support for additional 'LogEntry' fields ([#6229](https://github.com/googleapis/google-cloud-python/pull/6229))

### Dependencies
- Update dependency to google-cloud-core ([#6835](https://github.com/googleapis/google-cloud-python/pull/6835))
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))


### Internal / Testing Changes
- Change the url to the canonical one ([#6843](https://github.com/googleapis/google-cloud-python/pull/6843))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Blackening Continued... ([#6667](https://github.com/googleapis/google-cloud-python/pull/6667))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Logging: add 'synth.py'. ([#6081](https://github.com/googleapis/google-cloud-python/pull/6081))

## 1.8.0

10-17-2018 14:23 PDT

### Implementation Changes

- Logging:  allow more tries on inner retry for '_list_entries'. ([#6179](https://github.com/googleapis/google-cloud-python/pull/6179))
- Accommodate payload-less log entries. ([#6103](https://github.com/googleapis/google-cloud-python/pull/6103))

### New Features

- Logging: support request-correlated logging in App Engine standard python37 runtime ([#6118](https://github.com/googleapis/google-cloud-python/pull/6118))

### Documentation

- Logging: fix class reference in docstring ([#6153](https://github.com/googleapis/google-cloud-python/pull/6153))
- Translate / Logging / Language: restore detailed usage docs. ([#5999](https://github.com/googleapis/google-cloud-python/pull/5999))
- Redirect renamed 'usage.html'/'client.html' -> 'index.html'. ([#5996](https://github.com/googleapis/google-cloud-python/pull/5996))

### Internal / Testing Changes

- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Logging: harden systest teardown against 'DeadlineExceeded' retry errors. ([#6182](https://github.com/googleapis/google-cloud-python/pull/6182))
- Logging: fix lint errors. ([#6183](https://github.com/googleapis/google-cloud-python/pull/6183))
- Harden sink / metric creation against transient errors. ([#6180](https://github.com/googleapis/google-cloud-python/pull/6180))
- Logging: test both GCLOUD_PROJECT and GOOGLE_CLOUD_PROJECT env vars ([#6138](https://github.com/googleapis/google-cloud-python/pull/6138))
- Harden 'test_list_entry_with_unregistered' against 429 errors. ([#6181](https://github.com/googleapis/google-cloud-python/pull/6181))
- Prep logging docs for repo split. ([#5943](https://github.com/googleapis/google-cloud-python/pull/5943))

## 1.7.0

### Implementation Changes
- Print to stderr instead of stdout when exiting the program ([#5569](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5569))
- Avoid overwriting '__module__' of messages from shared modules. ([#5364](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5364))
- Support older Django versions in request middleware [#5024](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5024)
- Fix bad trove classifier [#5386](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5386)

### New Features
- Add support for `trace` and `span_id` to logging async API ([#5908](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5908))
- Add support for `span_id` attribute of log entries ([#5885](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5885))
- Add support for `trace` attribute of log entries ([#5878](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5878))
- Add support for Python 3.7 and remove 3.4 ([#5295](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5295))

### Documentation
- Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Nox: use inplace installs ([#5865](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5865))
- Unflake logging systests ([#5698](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5698))
- Harden `_list_entries` system test further against backoff failure. ([#5551](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5551))
- Harden logging systests ([#5496](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5496))
- Harden system tests against 'ResourceExhausted' quota errors. ([#5486](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5486))
- Modify system tests to use prerelease versions of grpcio ([#5304](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5304))
- Plug leaky sink in systests. ([#5247](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5247))

## 1.6.0

### Dependencies

- The minimum version for `google-api-core` has been updated to version 1.0.0. This may cause some incompatibility with older google-cloud libraries, you will need to update those libraries if you have a dependency conflict. (#4944, #4946)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)

## 1.5.0

### New features

- Added `max_latency` to `BackgroundThreadTransport`. (#4762)
- Added support for unique writer identity in `Sink`. (#4595, #4708, #4704, #4706)

### Implementation changes

- The underlying auto-generated client library was re-generated to pick up new features and bugfixes. (#4759)
- Moved the code path of `get_gae_labels()` to `emit()`. (#4824)
- Removed a debug print statement. (#4838)
- `LogSink.create` captures the server-generated `writerIdentity`. (#4707)
- Accomodated a back-end change making `Sink.filter` optional. (#4699)

### Testing

- Fixed system tests (#4768)
- Hardened test for `retrieve_metadata_server` against transparent DNS proxies. (#4698)
- Added cleanup for Pub / Sub topic in logging system test. (#4532)
- Added another check for Python 2.7 in Logging `nox -s default`. (#4523)
- Pinned `django` test dependency to `< 2.0` in Python 2.7. (#4519)
- Maked a `nox -s default` session for all packages. (#4324)
- Shortened test names. (#4321)

### Documentation

- Added doc to highlight missing `uniqueWriterIdentity` field. (#4579)
- Fixing "Fore" -> "For" typo in README docs. (#4317)

## 1.4.0

### Implementation Changes

- Remove `deepcopy` of `Client._http` in background transport (#3954)

### Documentation

- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)
- Deferring to `google-api-core` for `grpcio` and
  `googleapis-common-protos` dependencies (#4096, #4098)

PyPI: https://pypi.org/project/google-cloud-logging/1.4.0/
