# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-bigquery-reservation/#history

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.27.0...google-cloud-bigquery-reservation-v1.28.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.26.0...google-cloud-bigquery-reservation-v1.27.0) (2026-09-03)


### Features

* update googleapis and regenerate ([#18229](https://github.com/googleapis/google-cloud-python/issues/18229)) ([d4f8a57](https://github.com/googleapis/google-cloud-python/commit/d4f8a57abadd282ad95472e77daa59d8fb98cbcf))

## [1.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.25.0...google-cloud-bigquery-reservation-v1.26.0) (2026-08-21)


### Features

* update googleapis and regenerate ([#18087](https://github.com/googleapis/google-cloud-python/issues/18087)) ([db1622a](https://github.com/googleapis/google-cloud-python/commit/db1622a9cfac112b40c93842737d7a5deeb3e8bd))

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.24.0...google-cloud-bigquery-reservation-v1.25.0) (2026-06-02)


### Features

* regenerate google-cloud-b packages (#17090) ([77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd](https://github.com/googleapis/google-cloud-python/commit/77d4fcc15d1a6d96adb5f2765ecd0fcc47e478bd))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.23.0...google-cloud-bigquery-reservation-v1.24.0) (2026-05-06)

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.22.0...google-cloud-bigquery-reservation-v1.23.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.21.0...google-cloud-bigquery-reservation-v1.22.0) (2026-01-08)


### Documentation

* change comment indicating `enable_gemini_in_bigquery` field for BigQuery Reservation Assignments is deprecated ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.20.0...google-cloud-bigquery-reservation-v1.21.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.19.0...google-cloud-bigquery-reservation-v1.20.0) (2025-10-07)


### Features

* [google-cloud-bigquery-reservation] Add new `BACKGROUND_CHANGE_DATA_CAPTURE`, `BACKGROUND_COLUMN_METADATA_INDEX`, and `BACKGROUND_SEARCH_INDEX_REFRESH` reservation assignment types  ([4e5a0b50d1919fdc592478184e349d8e3ef0b658](https://github.com/googleapis/google-cloud-python/commit/4e5a0b50d1919fdc592478184e349d8e3ef0b658))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.18.0...google-cloud-bigquery-reservation-v1.19.0) (2025-09-04)


### Features

* Add a new field `failover_mode` to `.google.cloud.bigquery.reservation.v1.FailoverReservationRequest` that allows users to choose between the HARD or SOFT failover modes when they initiate a failover operation on a reservation ([c7bbbfc](https://github.com/googleapis/google-cloud-python/commit/c7bbbfc6e83795e2f813a60ca146a8fd4f232fa2))
* Add a new field `soft_failover_start_time` in the existing `replication_status` in `.google.cloud.bigquery.reservation.v1.Reservation` to provide visibility into the state of ongoing soft failover operations onthe reservation ([c7bbbfc](https://github.com/googleapis/google-cloud-python/commit/c7bbbfc6e83795e2f813a60ca146a8fd4f232fa2))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.17.2...google-cloud-bigquery-reservation-v1.18.0) (2025-08-29)


### Features

* Add Reservation.max_slots field to Reservation proto, indicating the total max number of slots this reservation can use up to ([8ab5fcc](https://github.com/googleapis/google-cloud-python/commit/8ab5fcc4409674815979bd6b378af5165ab0e901))
* Add Reservation.scaling_mode field and its corresponding enum message ScalingMode. This field should be used together with Reservation.max_slots ([8ab5fcc](https://github.com/googleapis/google-cloud-python/commit/8ab5fcc4409674815979bd6b378af5165ab0e901))

## [1.17.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.17.1...google-cloud-bigquery-reservation-v1.17.2) (2025-06-11)


### Documentation

* Update import statement example in README ([8697120](https://github.com/googleapis/google-cloud-python/commit/869712032803cb31d93f3b16abc2abdb14f733a4))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.17.0...google-cloud-bigquery-reservation-v1.17.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([1e43e75](https://github.com/googleapis/google-cloud-python/commit/1e43e75e99445373785b11381e0e859fa14bb485))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.16.0...google-cloud-bigquery-reservation-v1.17.0) (2025-02-27)


### Features

* Add a new field `enable_gemini_in_bigquery` to `.google.cloud.bigquery.reservation.v1.Assignment` that indicates if [Gemini in Bigquery](https://cloud.google.com/gemini/docs/bigquery/overview) features are enabled for the reservation assignment ([ff7c472](https://github.com/googleapis/google-cloud-python/commit/ff7c472ca3ada09a699bcf85d9a2d2880f9834f4))
* Add a new field `replication_status` to `.google.cloud.bigquery.reservation.v1.Reservation` to provide visibility into errors that could arise during Disaster Recovery(DR) replication ([ff7c472](https://github.com/googleapis/google-cloud-python/commit/ff7c472ca3ada09a699bcf85d9a2d2880f9834f4))
* Add the CONTINUOUS Job type to `.google.cloud.bigquery.reservation.v1.Assignment.JobType` for continuous SQL jobs ([ff7c472](https://github.com/googleapis/google-cloud-python/commit/ff7c472ca3ada09a699bcf85d9a2d2880f9834f4))


### Documentation

* Remove the section about `EDITION_UNSPECIFIED` in the comment for `slot_capacity` in `.google.cloud.bigquery.reservation.v1.Reservation` ([ff7c472](https://github.com/googleapis/google-cloud-python/commit/ff7c472ca3ada09a699bcf85d9a2d2880f9834f4))
* Update the `google.api.field_behavior` for the `.google.cloud.bigquery.reservation.v1.Reservation.primary_location` and `.google.cloud.bigquery.reservation.v1.Reservation.original_primary_location` fields to clarify that they are `OUTPUT_ONLY` ([ff7c472](https://github.com/googleapis/google-cloud-python/commit/ff7c472ca3ada09a699bcf85d9a2d2880f9834f4))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.15.0...google-cloud-bigquery-reservation-v1.16.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))
* Add support for reading selective GAPIC generation methods from service YAML ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.14.1...google-cloud-bigquery-reservation-v1.15.0) (2024-12-12)


### Features

* Add a new field `is_flat_rate` to `.google.cloud.bigquery.reservation.v1.CapacityCommitment` to distinguish between flat rate and edition commitments ([e87d4e9](https://github.com/googleapis/google-cloud-python/commit/e87d4e98a60b4b607699f5ef3b98b8e0963346f6))
* Add support for opt-in debug logging ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))
* Add the managed disaster recovery API(https://cloud.google.com/bigquery/docs/managed-disaster-recovery) ([e87d4e9](https://github.com/googleapis/google-cloud-python/commit/e87d4e98a60b4b607699f5ef3b98b8e0963346f6))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([e31cbb0](https://github.com/googleapis/google-cloud-python/commit/e31cbb0e11ab2cb093411005682c2fa2c38e787c))


### Documentation

* Clarify that `Autoscale.current_slots` in message `.google.cloud.bigquery.reservation.v1.Reservation` can temporarily be larger than `Autoscale.max_slots` if users reduce `Autoscale.max_slots` ([e87d4e9](https://github.com/googleapis/google-cloud-python/commit/e87d4e98a60b4b607699f5ef3b98b8e0963346f6))
* Update comment for `slot_capacity` in message `.google.cloud.bigquery.reservation.v1.Reservation` to provide more clarity about reservation baselines, committed slots and autoscaler SKU charges when the baseline exceeds committed slots ([e87d4e9](https://github.com/googleapis/google-cloud-python/commit/e87d4e98a60b4b607699f5ef3b98b8e0963346f6))
* Update comments for `commitment_start_time` and `commitment_end_time` in message `.google.cloud.bigquery.reservation.v1.CapacityCommitment` to provide details on how these values are affected by commitment renewal ([e87d4e9](https://github.com/googleapis/google-cloud-python/commit/e87d4e98a60b4b607699f5ef3b98b8e0963346f6))

## [1.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.14.0...google-cloud-bigquery-reservation-v1.14.1) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([4ed4108](https://github.com/googleapis/google-cloud-python/commit/4ed41088ab3cbadfe4de7fa170f172666015ed24))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.13.5...google-cloud-bigquery-reservation-v1.14.0) (2024-10-24)


### Features

* Add support for  Python 3.13 ([6252476](https://github.com/googleapis/google-cloud-python/commit/6252476e5938352fb2417d098a1edcc08558fe10))

## [1.13.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.13.4...google-cloud-bigquery-reservation-v1.13.5) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([a6f7356](https://github.com/googleapis/google-cloud-python/commit/a6f7356f1549721f9fab83d4dcfa226cec1965d0))

## [1.13.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.13.3...google-cloud-bigquery-reservation-v1.13.4) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12864](https://github.com/googleapis/google-cloud-python/issues/12864)) ([728b307](https://github.com/googleapis/google-cloud-python/commit/728b307ed0cc497685507a219e913f002f097132))

## [1.13.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.13.2...google-cloud-bigquery-reservation-v1.13.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12382](https://github.com/googleapis/google-cloud-python/issues/12382)) ([d5db265](https://github.com/googleapis/google-cloud-python/commit/d5db2656c011be2264bd778244caf8e23d288c75))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.13.1...google-cloud-bigquery-reservation-v1.13.2) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12281](https://github.com/googleapis/google-cloud-python/issues/12281)) ([62cf934](https://github.com/googleapis/google-cloud-python/commit/62cf934b140173d7b39e6c9ffa66e218b98260d4))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12304](https://github.com/googleapis/google-cloud-python/issues/12304)) ([c52e0cd](https://github.com/googleapis/google-cloud-python/commit/c52e0cdbddf44c96f642d8d596c5413c4006ba82))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.13.0...google-cloud-bigquery-reservation-v1.13.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([8465244](https://github.com/googleapis/google-cloud-python/commit/8465244deff230202eebab526092c780c6b60f4e))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.12.0...google-cloud-bigquery-reservation-v1.13.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12238](https://github.com/googleapis/google-cloud-python/issues/12238)) ([8701267](https://github.com/googleapis/google-cloud-python/commit/8701267fc9694844b9365024cd59354785247aa0))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.11.3...google-cloud-bigquery-reservation-v1.12.0) (2023-12-07)


### Features

* Add support for python 3.12 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Introduce compatibility with native namespace packages ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))
* Use `retry_async` instead of `retry` in async client ([0d1a592](https://github.com/googleapis/google-cloud-python/commit/0d1a59258112158cea5e55b554b0fe6b6b71fc75))

## [1.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigquery-reservation-v1.11.2...google-cloud-bigquery-reservation-v1.11.3) (2023-09-30)


### Documentation

* Minor formatting ([#377](https://github.com/googleapis/google-cloud-python/issues/377)) ([2b8616a](https://github.com/googleapis/google-cloud-python/commit/2b8616a906f2c6178a9f640c79caf956fc7d0bcc))

## [1.11.2](https://github.com/googleapis/python-bigquery-reservation/compare/v1.11.1...v1.11.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#362](https://github.com/googleapis/python-bigquery-reservation/issues/362)) ([98df6ad](https://github.com/googleapis/python-bigquery-reservation/commit/98df6adf73f2a1276e34977c06882a87558edf58))

## [1.11.1](https://github.com/googleapis/python-bigquery-reservation/compare/v1.11.0...v1.11.1) (2023-03-28)


### Documentation

* Minor clarifications ([#352](https://github.com/googleapis/python-bigquery-reservation/issues/352)) ([c9ce9b8](https://github.com/googleapis/python-bigquery-reservation/commit/c9ce9b85b8315f5d676fecdc0c95fd4f01363e9a))

## [1.11.0](https://github.com/googleapis/python-bigquery-reservation/compare/v1.10.0...v1.11.0) (2023-03-23)


### Features

* Add edition/autoscale related fields ([#348](https://github.com/googleapis/python-bigquery-reservation/issues/348)) ([e94a53b](https://github.com/googleapis/python-bigquery-reservation/commit/e94a53bd510f51facc4a0fd591e5c4a981028f90))


### Documentation

* Fix formatting of request arg in docstring ([#350](https://github.com/googleapis/python-bigquery-reservation/issues/350)) ([ecce362](https://github.com/googleapis/python-bigquery-reservation/commit/ecce36210c6a8fdce862b9ff16d49451180bea9a))

## [1.10.0](https://github.com/googleapis/python-bigquery-reservation/compare/v1.9.1...v1.10.0) (2023-02-16)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#339](https://github.com/googleapis/python-bigquery-reservation/issues/339)) ([50de8ca](https://github.com/googleapis/python-bigquery-reservation/commit/50de8ca394e61e0fd97b9264c660d4017c241ece))

## [1.9.1](https://github.com/googleapis/python-bigquery-reservation/compare/v1.9.0...v1.9.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([3912795](https://github.com/googleapis/python-bigquery-reservation/commit/3912795237f099f8cae2dea647f6e599aa3c4a1b))


### Documentation

* Add documentation for enums ([3912795](https://github.com/googleapis/python-bigquery-reservation/commit/3912795237f099f8cae2dea647f6e599aa3c4a1b))

## [1.9.0](https://github.com/googleapis/python-bigquery-reservation/compare/v1.8.0...v1.9.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#327](https://github.com/googleapis/python-bigquery-reservation/issues/327)) ([c86b3b8](https://github.com/googleapis/python-bigquery-reservation/commit/c86b3b8da191595dcbb30b4a55136c30376bad72))

## [1.8.0](https://github.com/googleapis/python-bigquery-reservation/compare/v1.7.3...v1.8.0) (2022-12-15)


### Features

* Add support for `google.cloud.bigquery_reservation.__version__` ([e82b8e5](https://github.com/googleapis/python-bigquery-reservation/commit/e82b8e50be61e2885ac8f5b21f650e54f8d6d604))
* Add typing to proto.Message based class attributes ([e82b8e5](https://github.com/googleapis/python-bigquery-reservation/commit/e82b8e50be61e2885ac8f5b21f650e54f8d6d604))


### Bug Fixes

* Add dict typing for client_options ([e82b8e5](https://github.com/googleapis/python-bigquery-reservation/commit/e82b8e50be61e2885ac8f5b21f650e54f8d6d604))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([c9ff564](https://github.com/googleapis/python-bigquery-reservation/commit/c9ff564b070c488b96af8574df442334173996cf))
* Drop usage of pkg_resources ([c9ff564](https://github.com/googleapis/python-bigquery-reservation/commit/c9ff564b070c488b96af8574df442334173996cf))
* Fix timeout default values ([c9ff564](https://github.com/googleapis/python-bigquery-reservation/commit/c9ff564b070c488b96af8574df442334173996cf))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([e82b8e5](https://github.com/googleapis/python-bigquery-reservation/commit/e82b8e50be61e2885ac8f5b21f650e54f8d6d604))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([c9ff564](https://github.com/googleapis/python-bigquery-reservation/commit/c9ff564b070c488b96af8574df442334173996cf))

## [1.7.3](https://github.com/googleapis/python-bigquery-reservation/compare/v1.7.2...v1.7.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#313](https://github.com/googleapis/python-bigquery-reservation/issues/313)) ([e616e6b](https://github.com/googleapis/python-bigquery-reservation/commit/e616e6bc2be88305ba5088e37647bc934b28299e))

## [1.7.2](https://github.com/googleapis/python-bigquery-reservation/compare/v1.7.1...v1.7.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#310](https://github.com/googleapis/python-bigquery-reservation/issues/310)) ([9c5c59a](https://github.com/googleapis/python-bigquery-reservation/commit/9c5c59a6f8b164f4d323677be0de537616f2f664))

## [1.7.1](https://github.com/googleapis/python-bigquery-reservation/compare/v1.7.0...v1.7.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#292](https://github.com/googleapis/python-bigquery-reservation/issues/292)) ([112a726](https://github.com/googleapis/python-bigquery-reservation/commit/112a726680d4426bdbc037631c887915bb8b2e35))
* **deps:** require proto-plus >= 1.22.0 ([112a726](https://github.com/googleapis/python-bigquery-reservation/commit/112a726680d4426bdbc037631c887915bb8b2e35))

## [1.7.0](https://github.com/googleapis/python-bigquery-reservation/compare/v1.6.3...v1.7.0) (2022-07-16)


### Features

* add audience parameter ([8b25cff](https://github.com/googleapis/python-bigquery-reservation/commit/8b25cff82fab1ae6c038238df5d65318396c0782))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#282](https://github.com/googleapis/python-bigquery-reservation/issues/282)) ([8b25cff](https://github.com/googleapis/python-bigquery-reservation/commit/8b25cff82fab1ae6c038238df5d65318396c0782))
* require python 3.7+ ([#284](https://github.com/googleapis/python-bigquery-reservation/issues/284)) ([13c0983](https://github.com/googleapis/python-bigquery-reservation/commit/13c0983e5d8671549e1b27d1b7533bfcbc374fe8))

## [1.6.3](https://github.com/googleapis/python-bigquery-reservation/compare/v1.6.2...v1.6.3) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#271](https://github.com/googleapis/python-bigquery-reservation/issues/271)) ([a054642](https://github.com/googleapis/python-bigquery-reservation/commit/a054642feccb275527eb803c97d56613cf006670))


### Documentation

* fix changelog header to consistent size ([#272](https://github.com/googleapis/python-bigquery-reservation/issues/272)) ([2a9c9de](https://github.com/googleapis/python-bigquery-reservation/commit/2a9c9deb1ec2afbe469296210c6659276c15379a))

## [1.6.2](https://github.com/googleapis/python-bigquery-reservation/compare/v1.6.1...v1.6.2) (2022-05-05)


### Documentation

* cleanup and clarifications ([#253](https://github.com/googleapis/python-bigquery-reservation/issues/253)) ([f34d11a](https://github.com/googleapis/python-bigquery-reservation/commit/f34d11a8c42bc626ca2550c9a3a3e98fa09ec2d0))

## [1.6.1](https://github.com/googleapis/python-bigquery-reservation/compare/v1.6.0...v1.6.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#233](https://github.com/googleapis/python-bigquery-reservation/issues/233)) ([14eee3f](https://github.com/googleapis/python-bigquery-reservation/commit/14eee3ff6a19aa1199c36c314210f4b8f23bc367))
* **deps:** require proto-plus>=1.15.0 ([14eee3f](https://github.com/googleapis/python-bigquery-reservation/commit/14eee3ff6a19aa1199c36c314210f4b8f23bc367))


### Documentation

* fix README typo in PyPI link ([#225](https://github.com/googleapis/python-bigquery-reservation/issues/225)) ([6eea2a3](https://github.com/googleapis/python-bigquery-reservation/commit/6eea2a39fbf22f09d6791aded8bd7bdda0b52425))

## [1.6.0](https://github.com/googleapis/python-bigquery-reservation/compare/v1.5.0...v1.6.0) (2022-02-03)


### Features

* add api key support ([#215](https://github.com/googleapis/python-bigquery-reservation/issues/215)) ([33dc0a3](https://github.com/googleapis/python-bigquery-reservation/commit/33dc0a3852ab0786b65b37bbfd17791fb7f29188))

## [1.5.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.4.1...v1.5.0) (2022-01-04)


### Features

* increase the logical timeout (retry deadline) to 5 minutes ([#198](https://www.github.com/googleapis/python-bigquery-reservation/issues/198)) ([13cb5b3](https://www.github.com/googleapis/python-bigquery-reservation/commit/13cb5b3c62fc4ca1823c1154e5ee5eaede5478ae))

## [1.4.1](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.4.0...v1.4.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([9b98c95](https://www.github.com/googleapis/python-bigquery-reservation/commit/9b98c95444b9d1467297ea4a87bbfb2954dc2999))
* **deps:** require google-api-core >= 1.28.0 ([9b98c95](https://www.github.com/googleapis/python-bigquery-reservation/commit/9b98c95444b9d1467297ea4a87bbfb2954dc2999))


### Documentation

* list oneofs in docstring ([9b98c95](https://www.github.com/googleapis/python-bigquery-reservation/commit/9b98c95444b9d1467297ea4a87bbfb2954dc2999))

## [1.4.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.3.1...v1.4.0) (2021-10-08)


### Features

* add context manager support in client ([#175](https://www.github.com/googleapis/python-bigquery-reservation/issues/175)) ([80768c8](https://www.github.com/googleapis/python-bigquery-reservation/commit/80768c8009b8450a3ac3025c95683bcd0628ef35))


### Bug Fixes

* improper types in pagers generation ([ae65c70](https://www.github.com/googleapis/python-bigquery-reservation/commit/ae65c70bd91602ccb851167d27b4161ebd6c3bb3))

## [1.3.1](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.3.0...v1.3.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([937ea64](https://www.github.com/googleapis/python-bigquery-reservation/commit/937ea64f4a8a5ff47baffeb88c4dd528324a77ae))

## [1.3.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.2.2...v1.3.0) (2021-09-02)


### Features

* Deprecated SearchAssignments in favor of SearchAllAssignments ([#157](https://www.github.com/googleapis/python-bigquery-reservation/issues/157)) ([dacdf5a](https://www.github.com/googleapis/python-bigquery-reservation/commit/dacdf5ac37a802f0d00a30468720a3ce1f294985))


### Documentation

* samples for managing reservations ([#144](https://www.github.com/googleapis/python-bigquery-reservation/issues/144)) ([27b2564](https://www.github.com/googleapis/python-bigquery-reservation/commit/27b256440b2565369c900cd4728e38676f82fcfe))

## [1.2.2](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.2.1...v1.2.2) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#138](https://www.github.com/googleapis/python-bigquery-reservation/issues/138)) ([1d3f927](https://www.github.com/googleapis/python-bigquery-reservation/commit/1d3f927b12268c07e724ed44f1b3373a7c64e999))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#132](https://www.github.com/googleapis/python-bigquery-reservation/issues/132)) ([c59d238](https://www.github.com/googleapis/python-bigquery-reservation/commit/c59d2383413ef5c57d72877d76514853f6271b00))


### Miscellaneous Chores

* release as 1.2.2 ([#139](https://www.github.com/googleapis/python-bigquery-reservation/issues/139)) ([96fbeba](https://www.github.com/googleapis/python-bigquery-reservation/commit/96fbeba273eb1776994f41400163788cf7b5e786))

## [1.2.1](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.2.0...v1.2.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#131](https://www.github.com/googleapis/python-bigquery-reservation/issues/131)) ([9a011b6](https://www.github.com/googleapis/python-bigquery-reservation/commit/9a011b604ffc2256b89d2fd6909a7219c0bcc88b))

## [1.2.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.1.0...v1.2.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#123](https://www.github.com/googleapis/python-bigquery-reservation/issues/123)) ([3123e99](https://www.github.com/googleapis/python-bigquery-reservation/commit/3123e99e8e288dcfb3627f77610c90060654bee4))
* support self-signed JWT flow for service accounts ([4d52ed9](https://www.github.com/googleapis/python-bigquery-reservation/commit/4d52ed91ae9eaa7ec6091138c134e682c9434853))


### Bug Fixes

* add async client to %name_%version/init.py ([4d52ed9](https://www.github.com/googleapis/python-bigquery-reservation/commit/4d52ed91ae9eaa7ec6091138c134e682c9434853))
* disable always_use_jwt_access ([32b279f](https://www.github.com/googleapis/python-bigquery-reservation/commit/32b279f0666a55c66e87c347ed7e913c2a9267a7))
* disable always_use_jwt_access ([#126](https://www.github.com/googleapis/python-bigquery-reservation/issues/126)) ([32b279f](https://www.github.com/googleapis/python-bigquery-reservation/commit/32b279f0666a55c66e87c347ed7e913c2a9267a7))
* exclude docs and tests from package ([#117](https://www.github.com/googleapis/python-bigquery-reservation/issues/117)) ([4f90792](https://www.github.com/googleapis/python-bigquery-reservation/commit/4f90792c26c8e47aad5a52267c713723e661efa3))
* require google-api-core >= 1.22.2 ([#90](https://www.github.com/googleapis/python-bigquery-reservation/issues/90)) ([3f0fff7](https://www.github.com/googleapis/python-bigquery-reservation/commit/3f0fff779d880df0648b7bcf59df01c4cacd4ca3))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-bigquery-reservation/issues/1127)) ([#120](https://www.github.com/googleapis/python-bigquery-reservation/issues/120)) ([7d65f87](https://www.github.com/googleapis/python-bigquery-reservation/commit/7d65f877f6814aed37f68116b52e200585587c58)), closes [#1126](https://www.github.com/googleapis/python-bigquery-reservation/issues/1126)
* Update the README to reflect that this library is GA ([#112](https://www.github.com/googleapis/python-bigquery-reservation/issues/112)) ([7bca7a9](https://www.github.com/googleapis/python-bigquery-reservation/commit/7bca7a9b6d73d8c8ee522c8ac930192fad49da57))

## [1.1.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.0.1...v1.1.0) (2021-03-09)


### Features

* add `client_cert_source_for_mtls` argument to transports ([#78](https://www.github.com/googleapis/python-bigquery-reservation/issues/78)) ([5df0f09](https://www.github.com/googleapis/python-bigquery-reservation/commit/5df0f0965c541ca546d3851be1ab7782dc80a11b))

## [1.0.1](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.0.0...v1.0.1) (2021-01-14)


### Bug Fixes

* remove gRPC send/recv limit ([#60](https://www.github.com/googleapis/python-bigquery-reservation/issues/60)) ([4115f1e](https://www.github.com/googleapis/python-bigquery-reservation/commit/4115f1ee6b67be5ce409122a44faa47ac53112bf))


### Documentation

* document enum values with `undoc-members` option ([#69](https://www.github.com/googleapis/python-bigquery-reservation/issues/69)) ([2acdeb7](https://www.github.com/googleapis/python-bigquery-reservation/commit/2acdeb782521c01a4e1fa01e42fdd1ce79dbf13d))

## [1.0.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.4.0...v1.0.0) (2020-10-29)


### ⚠ BREAKING CHANGES

* update package names to avoid conflict with google-cloud-bigquery

### Bug Fixes

* update package names to avoid conflict with google-cloud-bigquery ([#47](https://www.github.com/googleapis/python-bigquery-reservation/issues/47)) ([dc2172f](https://www.github.com/googleapis/python-bigquery-reservation/commit/dc2172fa8c540efca01c81fdd7f40880e087f66d))

## [0.4.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.3.0...v0.4.0) (2020-10-28)


### Features

* add path formatting helper methods ([362e0fe](https://www.github.com/googleapis/python-bigquery-reservation/commit/362e0fe51364101bd770cce851d986eea6c56e6a))
* implement mtls env variables mentioned in aip.dev/auth/4114 ([#39](https://www.github.com/googleapis/python-bigquery-reservation/issues/39)) ([21bff87](https://www.github.com/googleapis/python-bigquery-reservation/commit/21bff87047519754a01983c9a4551cb534bcb88c))

## [0.3.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.2.0...v0.3.0) (2020-08-26)


### Features

* add support for new client options ([#23](https://www.github.com/googleapis/python-bigquery-reservation/issues/23)) ([a0e818d](https://www.github.com/googleapis/python-bigquery-reservation/commit/a0e818d526dc60f0eb24787333e1041b02f26816))

## [0.2.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.1.0...v0.2.0) (2020-05-27)


### Features

* add helper methods to parse resource paths (via synth) ([#7](https://www.github.com/googleapis/python-bigquery-reservation/issues/7)) ([8fc54cb](https://www.github.com/googleapis/python-bigquery-reservation/commit/8fc54cb70be698f6d265f60d7b8ee4561d12d2c9))

## 0.1.0 (2020-05-12)


### Features

* generate v1 ([6293404](https://www.github.com/googleapis/python-bigquery-reservation/commit/6293404e47ca2efdcb5f702e248f43250060eb8c))
