# Changelog

Older versions of this project were distributed as [pybigquery][0].

[0]: https://pypi.org/project/pybigquery

[sqlalchemy-bigquery PyPI History][1]

[1]: https://pypi.org/project/sqlalchemy-bigquery/#history

## [1.17.3](https://github.com/googleapis/google-cloud-python/compare/sqlalchemy-bigquery-v1.17.2...sqlalchemy-bigquery-v1.17.3) (2026-10-02)


### Performance Improvements

* **sqlalchemy-bigquery:** parallelize compliance tests with worker-partitioned datasets and pytest-xdist ([#18534](https://github.com/googleapis/google-cloud-python/issues/18534)) ([855bbde](https://github.com/googleapis/google-cloud-python/commit/855bbde93ea4a5556d2843a6ea6d2b8ee118ba9a))

## [1.17.2](https://github.com/googleapis/google-cloud-python/compare/sqlalchemy-bigquery-v1.17.1...sqlalchemy-bigquery-v1.17.2) (2026-08-06)


### Bug Fixes

* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/sqlalchemy-bigquery-v1.17.0...sqlalchemy-bigquery-v1.17.1) (2026-07-22)


### Bug Fixes

* sqlalchemy bigquery python 3.15 compat ([#17788](https://github.com/googleapis/google-cloud-python/issues/17788)) ([14447fb](https://github.com/googleapis/google-cloud-python/commit/14447fb9edcd4b7e0680d82399af289b1145d6ed)), closes [#17786](https://github.com/googleapis/google-cloud-python/issues/17786)
* **sqlalchemy-bigquery:** update literal binds test for SQLAlchemy 2.0 ([#17029](https://github.com/googleapis/google-cloud-python/issues/17029)) ([74f7a41](https://github.com/googleapis/google-cloud-python/commit/74f7a41fc957f4b8e1de91b193c756b6a99637e4))
* **sqlalchemy-bigquery:** wrap string in WKT in geography system tests ([#17780](https://github.com/googleapis/google-cloud-python/issues/17780)) ([26d43c1](https://github.com/googleapis/google-cloud-python/commit/26d43c1fd820e058dd016084be2bdb459c288aff))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/sqlalchemy-bigquery-v1.16.0...sqlalchemy-bigquery-v1.17.0) (2026-05-06)


### Bug Fixes

* Drop support for Python 3.8 and 3.9 (#16956) ([63f6d96c1c5569b5fdaea85dfe995ce280907b98](https://github.com/googleapis/google-cloud-python/commit/63f6d96c1c5569b5fdaea85dfe995ce280907b98))
* Support Creation of JSON columns (#16733) ([153b82a47b3db8267e5e546b82a04e7d25e941a0](https://github.com/googleapis/google-cloud-python/commit/153b82a47b3db8267e5e546b82a04e7d25e941a0))


[pybigquery PyPI History][2]

[2]: https://pypi.org/project/pybigquery/#history


## [1.16.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.15.0...v1.16.0) (2025-11-05)


### Features

* Add support for Python 3.14 ([#1278](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1278)) ([c09a009](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/c09a00976a70194abb2561753071e3e7b3659d5c))
* Remove python 3.8 support ([#1215](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1215)) ([632d6ef](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/632d6ef024bdd1dcb4206e2b111063f79f29b7ba))

## [1.15.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.14.1...v1.15.0) (2025-06-18)


### Features

* Add Python 3.13 runtime support ([#1211](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1211)) ([55336f3](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/55336f38e57cfd245e603fd2246c6bae50065d67))

## [1.14.1](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.14.0...v1.14.1) (2025-05-09)


### Bug Fixes

* Updates _get_transitive_schema_fields and tests ([#1200](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1200)) ([16712da](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/16712da4ba068b1b376eb81ab7d2961a81bbc23d))

## [1.14.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.13.0...v1.14.0) (2025-04-23)


### Features

* Allow jobs to be run in a different project ([#1180](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1180)) ([eea4994](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/eea4994b0134a0e413ea22b8d9e3e85a14ce998d))


### Bug Fixes

* Remove setup.cfg configuration for creating universal wheels ([#1175](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1175)) ([dc394ac](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/dc394ac5e95095ca69a4f0000ec1820ed3cf53cb))

## [1.13.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.12.1...v1.13.0) (2025-03-11)


### Features

* Support job_config at query level ([#1167](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1167)) ([ea849e0](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/ea849e0bf288388c603f9d594c2a5042a6e16570))


### Bug Fixes

* Resolve issue where pre-release versions of dependencies are installed ([#1169](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1169)) ([8c27cca](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/8c27cca5d2ed32662e3f23370692765b43c90de7))

## [1.12.1](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.12.0...v1.12.1) (2025-01-21)


### Features

* Update partitioning by DATE, DATETIME, TIMESTAMP, _PARTITIONDATE ([#1113](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1113)) ([413cd24](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/413cd242d17f92c04cdfebf70595421c96cbbae4))


### Bug Fixes

* Alembic column rename ([#1141](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1141)) ([9f7f78b](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/9f7f78becc8e1241eabdc7cc50bfb12ac4860d65))
* Compilation of a labeled custom FunctionElement when used in grouping ([#1155](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1155)) ([4a0f8ad](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/4a0f8ad92172baa6551ad2a79e1446d807bfd4dd))


### Documentation

* Fix typo on credentials_info usage sample ([#1145](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1145)) ([736d4a2](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/736d4a26ca9fd1e343e7c5c02637e8707ab57fee))

## [1.12.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.11.0...v1.12.0) (2024-08-14)


### Features

* Adds user agent parameters to two functions ([#1100](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1100)) ([f9324e3](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/f9324e35a6aa2f3d9c9f2511d1104fdf60c97c83))
* Support UPDATE + JOIN in BigQuery dialect ([#1083](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1083)) ([d766d21](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/d766d21053f7d9df5019d0d6dedf4476ef6125a9))
* Update colspec to account for sqlalchemy Enum ([#1111](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1111)) ([b54bdde](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/b54bdde0a01cabf5844c2b2794994b1ae5f4952f))


### Bug Fixes

* Fix partitioning by DATE column ([#1074](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1074)) ([ad69c63](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/ad69c630833bce207784dfbea8eb3c58f316e511))
* Implement modulus operator ([#1048](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1048)) ([f5fb1a2](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/f5fb1a2543e8196e076d74848a7ae0dcf169f667))
* Set cte_follows_insert to True ([#1095](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1095)) ([9e0b117](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/9e0b117b6966ad72bc94c0916be95189e4bd9654))
* Use except distinct and intersect distinct ([#1094](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1094)) ([80781ef](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/80781ef99287af2e950f21ca399c84d20422b732))

## [1.11.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.10.0...v1.11.0) (2024-04-12)


### Features

* Support SQLAlchemy 2.0, raise minimum required version to 1.4.x ([[#920](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/920)](https://github.com/googleapis/python-bigquery-sqlalchemy/pull/920), [[#1053](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1053)](https://github.com/googleapis/python-bigquery-sqlalchemy/pull/1053)) ([7a4c3c2](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/7a4c3c28f586c6bb02349ce8620d515f5b56164e))


### Bug Fixes

* Fix grouping sets, rollup and cube rendering issue ([[#1019](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1019)](https://github.com/googleapis/python-bigquery-sqlalchemy/pull/1019), [[#1053](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1053)](https://github.com/googleapis/python-bigquery-sqlalchemy/pull/1053)) ([7a4c3c2](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/7a4c3c28f586c6bb02349ce8620d515f5b56164e))


### Documentation

* Fix docs session ([#1060](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1060)) ([7e66cc2](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/7e66cc217722456d5669809d68863549c4f4ea39))

## [1.10.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.9.0...v1.10.0) (2024-02-27)


### Features

* Allow to set clustering and time partitioning options at table creation ([#928](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/928)) ([c2c2958](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/c2c2958886cc3c8a51c4f5fc1a8c36b65921edd9))


### Bug Fixes

* Avoid implicit join when using join with unnest ([#924](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/924)) ([ac74a34](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/ac74a3434c437f60b6f215ac09dea224aa406f8a))

## [1.9.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.8.0...v1.9.0) (2023-12-10)


### Features

* Add support for Python 3.12 ([#923](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/923)) ([8952f02](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/8952f02c482f9143b0ec78f48d66e7c7a2e755f3))


### Bug Fixes

* Remove Python 3.7 support due to EOL ([#900](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/900)) ([45fcad4](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/45fcad4111b9143fb1b9c309ed2a7578ae05d7a4))
* Removing Python 3.7 from sync-repo-settings.yaml file ([#902](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/902)) ([afd895e](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/afd895e6b63e9a21610101f4d5e080a13066f102))

## [1.8.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.7.0...v1.8.0) (2023-08-11)


### Features

* Remove illegal character check ([#892](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/892)) ([3328d0a](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/3328d0a69654e5c30af06359185170f7937d978b))

## [1.7.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.6.1...v1.7.0) (2023-07-11)


### Features

* Added regexp_match operator support for bigquery ([#511](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/511)) ([fd78093](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/fd780938ca4a0d32448ed666753360f05584d2ab))
* Remove pyarrow and bqstorage as dependencies ([#847](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/847)) ([5d6b38c](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/5d6b38c94dfef0bd0dbf5037ad21a352d2bd8e4f))


### Bug Fixes

* Avoid aliasing known CTEs ([#839](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/839)) ([8a1f694](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/8a1f694e59f5bac5ce66d9f8a04066980d7f9893))
* Ensure correct alter table alter column statement is generated on data type changes in alembic ([#845](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/845)) ([493430a](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/493430a58914dc89fa5c16ea2127e4bed58bd0bf))
* Remove "future" dependency ([#542](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/542)) ([ba5e244](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/ba5e24487e798fd77e7db93321c374a9196293f4))
* Remove type annotations from _struct.py ([#733](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/733)) ([27814df](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/27814dfbea8267d1b7abbc47fbbb56bb36f3585d))


### Documentation

* Pass credentials as python dictionary ([#737](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/737)) ([074321d](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/074321ddaa10001773e7e6044f4a0df1bb530331))

## [1.6.1](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.6.0...v1.6.1) (2023-02-01)


### Bug Fixes

* Ensure repo install ([#741](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/741)) ([75ef9ac](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/75ef9ac9dc1e806f3b2ef34208156c1a311750bc))

## [1.6.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.5.0...v1.6.0) (2023-01-30)


### Features

* Enable support and testing for python 3.11 ([#512](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/512)) ([f826d83](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/f826d83bb2560ad82fb6d83bbb87ed89fac513f8))


### Bug Fixes

* Avoid sqlalchemy20 ([#736](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/736)) ([0675b1e](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/0675b1efb8f3adf88e800b2de660abe13fe39b25))

## [1.5.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.4.4...v1.5.0) (2022-11-29)


### Features

* Allow Users to Supply Their Own BigQuery Client ([#474](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/474)) ([4f72d4e](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/4f72d4eb12fe986c2bae1bb1884a4ef5e78c95bc))


### Bug Fixes

* **deps:** Allow pyarrow version 7+ ([#479](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/479)) ([0f6be67](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/0f6be6712d5b89b14160cad3440d0bc1308dd5e5))
* Require python 3.7+ ([#468](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/468)) ([52ec808](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/52ec80849b574edd2827df345c0085f3c68dc39d))
* Sets cache support to false, removes upper req limit ([#499](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/499)) ([be63adc](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/be63adc345a3bfcd199c758e45e7d2c7036c4bab))
* Updates test to account for UTC in failing test ([#501](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/501)) ([a050ccf](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/a050ccf534fe8e6d2135818474868f072212aa6f))
* Use packaging version parser instead of string splitting ([#513](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/513)) ([bb7f6a7](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/bb7f6a78c1b7d738ab31a6a6d5112ab6e888c6aa))

## [1.4.4](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.4.3...v1.4.4) (2022-06-03)


### Documentation

* fix changelog header to consistent size ([#461](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/461)) ([177e70a](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/177e70afb79420541021895fd0a082beb1704cf4))

## [1.4.3](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.4.2...v1.4.3) (2022-03-22)


### Bug Fixes

* correct license text from Apache to MIT ([#436](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/436)) ([dbf7501](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/dbf7501c26157d3776f5a68254898758ee43a667))

## [1.4.2](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.4.1...v1.4.2) (2022-03-22)


### Bug Fixes

* use explicit rather than implicit relative imports ([#433](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/433)) ([ca20d3d](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/ca20d3d20939b780abe49dfc833375eecd31ae04))
* use faux_conn rather than engine in unit tests ([#431](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/431)) ([275506f](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/275506f0c9b7ac0e67410dbd7ceab8c9f593a259))


### Dependencies

* require google-cloud-bigquery-storage to avoid performance warning ([#414](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/414)) ([ff3273f](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/ff3273feacfa1f34bb9090f28f11c2ac470759fc))

## [1.4.1](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.4.0...v1.4.1) (2022-03-07)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#419](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/419)) ([52339f7](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/52339f70340eb8f497c816f36f71c8232928e57b))

## [1.4.0](https://github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.3.0...v1.4.0) (2022-02-22)


### Features

* Allow base64 encoded credentials in URI ([#410](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/410)) ([e2f9821](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/e2f9821e66507ee3ac3260d9c1b0ba899cf2efc4))


### Bug Fixes

* POSTCOMPILE expansion in SQLAlchemy 1.4.27+ ([#408](https://github.com/googleapis/python-bigquery-sqlalchemy/issues/408)) ([7844813](https://github.com/googleapis/python-bigquery-sqlalchemy/commit/7844813c6eb3a52cc9d3e91e88d5f8ecebba08c5))

## [1.3.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.2.2...v1.3.0) (2021-12-31)


### Features

* Enable support for 3.10 ([#381](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/381)) ([4b3505b](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/4b3505b3d3a4293ea127fc3c483e3e7de04fbd04))

## [1.2.2](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.2.1...v1.2.2) (2021-10-29)


### Bug Fixes

* avoid aliasing known tables used in CTEs ([#369](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/369)) ([4b05d21](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/4b05d21b8dc89339a69df87183f8893bf02459c5))

## [1.2.1](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.2.0...v1.2.1) (2021-10-27)


### Bug Fixes

* avoid creating aliases for already-known tables ([#361](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/361)) ([1ce4e14](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/1ce4e14c81a4b378dfcfba808507e6c545f34841))
* avoid scribbling on (reused) bind param ([#365](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/365)) ([d28cac5](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/d28cac5864f183c0ca503854973d837b17783d52))
* include external tables in 'get_table_names' ([#363](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/363)) ([5e158fe](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/5e158fe8bb2394369c020337092b5cfdb01880e0))

## [1.2.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.1.0...v1.2.0) (2021-09-09)


### Features

* STRUCT and ARRAY support ([#318](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/318)) ([6624b10](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/6624b10ded73bbca6f40af73aaeaceb95c381b63))


### Bug Fixes

* the unnest function lost needed type information ([#298](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/298)) ([1233182](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/123318269876e7f76c7f0f2daa5f5b365026cd3f))

## [1.1.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.0.0...v1.1.0) (2021-08-25)


### Features

* Add geography support ([#228](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/228)) ([da7a403](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/da7a40309de6ca8063d6dcf6678de96a463344e6))
* Handle passing of arrays to in statements more efficiently in SQLAlchemy 1.4 and higher ([#253](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/253)) ([7692704](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/76927044aa4d2be9d0f2ec47e917b28b97c18425))


### Bug Fixes

* dialect atribute wasn't provided ([#291](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/291)) ([2cf05a0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/2cf05a0f37e32344b29ba2e92d709f7e51b20916))
* distinct doesn't work as a column wrapper ([#275](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/275)) ([ad5baf8](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/ad5baf8a5351b9cdac4eda243e4042aeb551b937))
* in-operator literal binds not handled properly ([#285](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/285)) ([e06bf74](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/e06bf74310fa27d5bc775e13beed4ab3a520e1aa))
* supports_multivalues_insert dialect option was mispelled ([#278](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/278)) ([ec36a12](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/ec36a120c1607d9769105e873550bb727c504c93))
* unnest failed in some cases (with table references failed when there were no other references to refrenced tables in a query) ([#290](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/290)) ([9b5b002](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/9b5b0025ec0b65177c0df02013ac387b3d3de472))

## [1.0.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v1.0.0-a1...v1.0.0) (2021-08-17)


### Miscellaneous Chores

* release 1.0.0 ([#249](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/249)) ([d23ae1d](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/d23ae1d2a8ad3c466e08b03f167c8c49b39579d0))

## [1.0.0-a1](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.10.1...v1.0.0-a1) (2021-08-11)


### Features

* Rename pybigquery to sqlalchemy-bigquery ([#198](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/198)) ([a6f0a5d](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/a6f0a5d77053be528a6b6805cb1ff3c8ec465f5e))


### Miscellaneous Chores

* release 1.0.0-a1 ([#238](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/238)) ([b630293](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/b6302937b0c5e2314de7e90c02d74af08e5b17a0))

## [pybigquery 0.10.1](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.10.0...v0.10.1) (2021-07-30)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#220](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/220)) ([bf1f47c](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/bf1f47c794e747a2ea878347322c040636e8c2d4))

## [pybigquery 0.10.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.9.1...v0.10.0) (2021-07-06)


### Features

* There's a new `page_size` option to control the page size used when listing tables. ([#174](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/174)) ([e0f1496](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/e0f1496c99dd627e0ed04a0c4e89ca5b14611be2))

## [pybigquery 0.9.1](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.9.0...v0.9.1) (2021-06-25)


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([d52334c](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/d52334c3290d8356a26e1c9fc54dae75854410c9))

## [pybigquery 0.9.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.8.0...v0.9.0) (2021-05-25)


### Features

* Alembic support ([#183](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/183)) ([4d5a17c](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/4d5a17c8f63328d4484ea7b2ccc58334a421ba81))
* Support parameterized NUMERIC, BIGNUMERIC, STRING, and BYTES types ([#180](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/180)) ([d118238](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/d1182385b9f1551e605acdc7e2dd45dff22c8064))

## [pybigquery 0.8.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.7.0...v0.8.0) (2021-05-21)


### Features

* Add support for SQLAlchemy 1.4 ([#177](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/177)) ([b7b6000](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/b7b60007c966cd548448d1d6fd5a14d1f89480cd))

## [pybigquery 0.7.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.6.1...v0.7.0) (2021-05-12)


### Features

* Comment/description support, bug fixes and better test coverage ([#138](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/138)) ([fb7c188](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/fb7c188fd1d61f2bb2b99742f62042576bff02a9))
  * Runs SQLAlchemy dialect-compliance tests (as system tests).
  * 100% unit-test coverage.
  * Support for table and column comments/descriptions (requiring SQLAlchemy 1.2 or higher).
  * When executing parameterized queries, the new BigQuery DB API parameter syntax is used to pass type information.  This is helpful when the DB API can't determine type information from values, or can't determine it correctly.

### Bug Fixes

* Select expressions no-longer force use of labels ([#129](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/129)) ([669b301](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/669b301359f9f37c5c7286a245080b8af2567186))

* Additional fixes, including:
  - Handling of `in` queries.
  - String literals with special characters.
  - Use BIGNUMERIC when necessary.
  - Missing types: BIGINT, SMALLINT, Boolean, REAL, CHAR, NCHAR, VARCHAR, NVARCHAR, TEXT, VARBINARY, DECIMAL
  - Literal bytes, dates, times, datetimes, timestamps, and arrays.
  - Get view definitions.


## [pybigquery 0.6.1](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.6.0...v0.6.1) (2021-04-12)


### Bug Fixes

* use `project_id` property from service account credentials ([#120](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/120)) ([ab2051d](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/ab2051de3097adb68503c01a87f9a91092711d2a))

## [pybigquery 0.6.0](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.5.1...v0.6.0) (2021-04-06)


### Features

* fetch table and column descriptions during reflection ([#115](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/115)) ([7b14a06](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/7b14a06f71f113af0e2970898bc0ec203e4e6464))


### Bug Fixes

* correct classifiers in `setup.py` ([#107](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/107)) ([0cfc5de](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/0cfc5de467823998ba72af1fee1d2a8aa865fabc))

## [pybigquery 0.5.1](https://www.github.com/googleapis/python-bigquery-sqlalchemy/compare/v0.5.0...v0.5.1) (2021-04-01)


### Bug Fixes

* avoid 404 if dataset is deleted while listing tables or views ([#106](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/106)) ([db379d8](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/db379d850b916149db5976689d6f2323d2281f7a))


### Documentation

* add templates for move to googleapis/python-bigquery-sqlalchemy repo ([#88](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/88)) ([37e584e](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/37e584e05db6316b4abd41ebc08486047d2c49b8))
* build documentation with Sphinx ([#97](https://www.github.com/googleapis/python-bigquery-sqlalchemy/issues/97)) ([1707737](https://www.github.com/googleapis/python-bigquery-sqlalchemy/commit/1707737c60997e9714387c8077727eb5918626bb))

## pybigquery 0.5.0 (2020-11-18)

### ⚠️ Breaking Changes ⚠️ 

- `get_table_names()` no longer returns views. ([#62](https://github.com/mxmzdlv/pybigquery/pull/62), [#60](https://github.com/mxmzdlv/pybigquery/issues/60))

### Features

- Support the `ARRAY` data type in generated DDL. ([#64](https://github.com/mxmzdlv/pybigquery/pull/64))
- Support project ID and dataset ID in `schema` argument. ([#63](https://github.com/mxmzdlv/pybigquery/pull/63]))
- Implement `get_view_names()` method. ([#62](https://github.com/mxmzdlv/pybigquery/pull/62), [#60](https://github.com/mxmzdlv/pybigquery/issues/60))

### Bug Fixes

- Ignore no-op nested labels. ([#47](https://github.com/mxmzdlv/pybigquery/pull/47))

### Development

- Use flake8 for code style checks. ([#71](https://github.com/mxmzdlv/pybigquery/pull/71))

## pybigquery 0.4.15 (2020-04-23)

### Implementation Changes

- Prefer explicitly provided dataset over default dataset in lookup. ([#53](https://github.com/mxmzdlv/pybigquery/pull/53))
- Use the provided `project_id` when using a service account. ([#52](https://github.com/mxmzdlv/pybigquery/pull/52))
