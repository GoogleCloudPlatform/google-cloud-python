# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-bigtable/#history

## [2.50.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.50.1...google-cloud-bigtable-v2.50.2) (2026-10-22)


### Bug Fixes

* **bigtable:** preserve resource labels on batcher metrics ([#18712](https://github.com/googleapis/google-cloud-python/issues/18712)) ([f18cc6b](https://github.com/googleapis/google-cloud-python/commit/f18cc6b4086a3a1ea38c5bd45ccca79d927185ab))
* **bigtable:** resolve O(n^2) bottleneck in ReadRowsQuery.add_range ([#18706](https://github.com/googleapis/google-cloud-python/issues/18706)) ([5ac7cc6](https://github.com/googleapis/google-cloud-python/commit/5ac7cc6b1168fa674340e11598bc6e5866a53c16))

## [2.50.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.50.0...google-cloud-bigtable-v2.50.1) (2026-10-15)


### Bug Fixes

* **bigtable:** avoid hang when batcher not closed on process exit ([#18610](https://github.com/googleapis/google-cloud-python/issues/18610)) ([7674c91](https://github.com/googleapis/google-cloud-python/commit/7674c91a81a984e01166f72a8895cb18c8a8216b))
* **bigtable:** fix authentication scopes for metrics exporter ([#18609](https://github.com/googleapis/google-cloud-python/issues/18609)) ([722d34e](https://github.com/googleapis/google-cloud-python/commit/722d34e519dbb8305c4a48ac83790078f5ff9d57))

## [2.50.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.49.0...google-cloud-bigtable-v2.50.0) (2026-10-08)


### Features

* update API sources and regenerate ([#18593](https://github.com/googleapis/google-cloud-python/issues/18593)) ([d0505e8](https://github.com/googleapis/google-cloud-python/commit/d0505e8bc7615f2c649d3e25ebc7e3ccca45f22b))

## [2.49.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.48.0...google-cloud-bigtable-v2.49.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))
* update API sources and regenerate ([#18513](https://github.com/googleapis/google-cloud-python/issues/18513)) ([7d7adca](https://github.com/googleapis/google-cloud-python/commit/7d7adcaee688603077ea53abec678130045c20ed))

## [2.48.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.47.0...google-cloud-bigtable-v2.48.0) (2026-09-29)


### Features

* **bigtable:** Reroute Mutations Batcher to use data client ([#18200](https://github.com/googleapis/google-cloud-python/issues/18200)) ([0b488a3](https://github.com/googleapis/google-cloud-python/commit/0b488a395542e9c76f535e82a7298fabaee8f4af))
* declare Python3.15 support ([05b0c34](https://github.com/googleapis/google-cloud-python/commit/05b0c342683b2b0e1b8dccd201ec86ec89612edc))

## [2.47.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.46.0...google-cloud-bigtable-v2.47.0) (2026-09-24)


### Features

* update API sources and regenerate ([#18446](https://github.com/googleapis/google-cloud-python/issues/18446)) ([54f1019](https://github.com/googleapis/google-cloud-python/commit/54f10190a4ab7b3772010bf9006de55266f74da9))

## [2.46.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.45.0...google-cloud-bigtable-v2.46.0) (2026-09-17)


### Features

* **bigtable:** Rerouted RowSet and RowRange to use ReadRows from data client ([#18196](https://github.com/googleapis/google-cloud-python/issues/18196)) ([1857302](https://github.com/googleapis/google-cloud-python/commit/1857302d5c602087b9a782c62694c33013eb77ea))
* Rerouted ReadRows to data client ([#18198](https://github.com/googleapis/google-cloud-python/issues/18198)) ([934cd2d](https://github.com/googleapis/google-cloud-python/commit/934cd2da82be8b835192baa222e3a2ab5aa4b8d1))
* update API sources and regenerate ([#18396](https://github.com/googleapis/google-cloud-python/issues/18396)) ([e9f8e59](https://github.com/googleapis/google-cloud-python/commit/e9f8e590b7b395e660cc5437535166dfb920d246))
* update API sources and regenerate. ([e9f8e59](https://github.com/googleapis/google-cloud-python/commit/e9f8e590b7b395e660cc5437535166dfb920d246))


### Bug Fixes

* **bigtable:** Added rst_stream exception handling for ReadRows. ([#18197](https://github.com/googleapis/google-cloud-python/issues/18197)) ([f30df60](https://github.com/googleapis/google-cloud-python/commit/f30df60eda27810cec277663dff532a158c999f3))

## [2.45.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.44.0...google-cloud-bigtable-v2.45.0) (2026-09-14)


### Features

* **bigtable:** Rerouted MutateRows to use the data client ([#18195](https://github.com/googleapis/google-cloud-python/issues/18195)) ([3bbcbdf](https://github.com/googleapis/google-cloud-python/commit/3bbcbdf1a62dd10ab96f72e5c8198cffe9174ac7))

## [2.44.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.43.0...google-cloud-bigtable-v2.44.0) (2026-09-03)


### Features

* **bigtable:** Rerouted CheckAndMutateRows and ReadModifyWriteRows to data client ([#18190](https://github.com/googleapis/google-cloud-python/issues/18190)) ([990f86e](https://github.com/googleapis/google-cloud-python/commit/990f86e45df15c594e82d19d6fe482f12d128430))
* **bigtable:** Rerouted DirectRow.commit to use mutate_row ([#18191](https://github.com/googleapis/google-cloud-python/issues/18191)) ([7126a54](https://github.com/googleapis/google-cloud-python/commit/7126a548e4231ae5f5e49599d53d84a94b9302ca))
* update API sources and regenerate ([#18267](https://github.com/googleapis/google-cloud-python/issues/18267)) ([813a5c1](https://github.com/googleapis/google-cloud-python/commit/813a5c17cbe42b3a8386e7ad7475a3d7ada33842))

## [2.43.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.42.0...google-cloud-bigtable-v2.43.0) (2026-08-21)


### Features

* update sources and regenerate ([#18164](https://github.com/googleapis/google-cloud-python/issues/18164)) ([5ff8274](https://github.com/googleapis/google-cloud-python/commit/5ff8274ac2eb9375e918dff68303d3abdc3e6d6f))


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [2.42.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.41.0...google-cloud-bigtable-v2.42.0) (2026-08-19)


### Features

* **bigtable:** client side metrics handlers ([#16760](https://github.com/googleapis/google-cloud-python/issues/16760)) ([43b786c](https://github.com/googleapis/google-cloud-python/commit/43b786c2c5f5f42d5caa3fa596a7368be09fd3a3))
* **bigtable:** initialize internal data client in classic client ([#18080](https://github.com/googleapis/google-cloud-python/issues/18080)) ([92008e2](https://github.com/googleapis/google-cloud-python/commit/92008e2788f086790f1976198fa43a1f902eef25))


### Bug Fixes

* **bigtable:** data client should acknowledge all mutations in batch ([#18124](https://github.com/googleapis/google-cloud-python/issues/18124)) ([e7f6a34](https://github.com/googleapis/google-cloud-python/commit/e7f6a34309fac7640b8f74c56108bec48b7bf711))
* **bigtable:** report swallowed batch flush errors and unacknowledged entries ([#18122](https://github.com/googleapis/google-cloud-python/issues/18122)) ([2fe5bdc](https://github.com/googleapis/google-cloud-python/commit/2fe5bdccd0fc964edc3427e25f86a4eab3c8267b))
* **bigtable:** standardize client side metrics ([#17899](https://github.com/googleapis/google-cloud-python/issues/17899)) ([a69e2cb](https://github.com/googleapis/google-cloud-python/commit/a69e2cbc939320fef18eb61daa8c248edf325c5b))
* **bigtable:** surface batcher flush errors and disable timer ([#18145](https://github.com/googleapis/google-cloud-python/issues/18145)) ([fac536e](https://github.com/googleapis/google-cloud-python/commit/fac536ea024f8f7a52e00fcc003d0fce1945b1f9))
* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))

## [2.41.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.40.0...google-cloud-bigtable-v2.41.0) (2026-07-16)


### Features

* **bigtable:** support materialized views in the data client ([#17676](https://github.com/googleapis/google-cloud-python/issues/17676)) ([2c3c213](https://github.com/googleapis/google-cloud-python/commit/2c3c213998b3f3aa1cf490dfbf824d160544b732))

## [2.40.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.39.0...google-cloud-bigtable-v2.40.0) (2026-06-25)


### Features

* regenerate google-cloud-bigtable ([#17575](https://github.com/googleapis/google-cloud-python/issues/17575)) ([bd782cf](https://github.com/googleapis/google-cloud-python/commit/bd782cf279ae700f56d40702d4ef25ef89e2ff9b))


### Bug Fixes

* **bigtable:** populate Value type in _format_execute_query_view_params ([#17547](https://github.com/googleapis/google-cloud-python/issues/17547)) ([8cb77d9](https://github.com/googleapis/google-cloud-python/commit/8cb77d99103ba94d6e4ff488ddcdbccd37b2770c))

## [2.39.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.38.0...google-cloud-bigtable-v2.39.0) (2026-06-22)


### Features

* added client side metric instrumentation to read_rows and mutate_rows ([#16758](https://github.com/googleapis/google-cloud-python/issues/16758)) ([4005e66](https://github.com/googleapis/google-cloud-python/commit/4005e660a38fd770f8754af1cd07d6d8aa9ed60e))
* **bigtable:** add client side metric instrumentation to basic rpcs ([#16712](https://github.com/googleapis/google-cloud-python/issues/16712)) ([636af26](https://github.com/googleapis/google-cloud-python/commit/636af26677af5be906220ad39d670e74daca58e0))
* **bigtable:** add view_parameters support to execute_query ([#17382](https://github.com/googleapis/google-cloud-python/issues/17382)) ([2695aad](https://github.com/googleapis/google-cloud-python/commit/2695aad5c2949e20e77ae9dd432c6fc8ef787952))
* support row_range in sample_row_keys method ([#17330](https://github.com/googleapis/google-cloud-python/issues/17330)) ([384724c](https://github.com/googleapis/google-cloud-python/commit/384724c2d4c955e15274e9824bcdb93c685b79f6)), closes [#17329](https://github.com/googleapis/google-cloud-python/issues/17329)
* update API sources and regenerate ([#17431](https://github.com/googleapis/google-cloud-python/issues/17431)) ([2e75c78](https://github.com/googleapis/google-cloud-python/commit/2e75c78cdd09d4472ed412a2e925196effaea9fd))
* update googleapis and regenerate ([33ba3af](https://github.com/googleapis/google-cloud-python/commit/33ba3afe520e2f64ac7464f1b4ee31c0624a65ac))


### Bug Fixes

* **bigtable:** ensure deadline is respected for read_rows_sharded ([#17352](https://github.com/googleapis/google-cloud-python/issues/17352)) ([6cc890b](https://github.com/googleapis/google-cloud-python/commit/6cc890b5b9088e19afc7dd3dfbb64c72309feb80))
* require Python 3.10+ ([#17245](https://github.com/googleapis/google-cloud-python/issues/17245)) ([200b0d3](https://github.com/googleapis/google-cloud-python/commit/200b0d324df924c69c358203350fb01a08e41ad9))

## [2.38.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.37.0...google-cloud-bigtable-v2.38.0) (2026-05-07)


### Features

* Add ValueBitmask to the filter DSL (#16981) ([3f429f23386a63e5e6773216b8d00dbed4940c0c](https://github.com/googleapis/google-cloud-python/commit/3f429f23386a63e5e6773216b8d00dbed4940c0c))

## [2.36.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-bigtable-v2.35.0...google-cloud-bigtable-v2.36.0) (2026-04-02)


### Features

* add TieredStorageConfig to table admin api ([778ae57190af47d655557aa5491d8f35c4288bbd](https://github.com/googleapis/google-cloud-python/commit/778ae57190af47d655557aa5491d8f35c4288bbd))
* add data model for client side metrics (#1187) ([db8d52862242b7718b110ac01d945611a8a8acee](https://github.com/googleapis/google-cloud-python/commit/db8d52862242b7718b110ac01d945611a8a8acee))


### Bug Fixes

* allow empty location for cluster update (#1258) ([c163cb3e900d00b01b62ba2324fc2d67460e8981](https://github.com/googleapis/google-cloud-python/commit/c163cb3e900d00b01b62ba2324fc2d67460e8981))

## [2.35.0](https://github.com/googleapis/python-bigtable/compare/v2.34.0...v2.35.0) (2025-12-16)


### Features

* support mTLS certificates when available (#1249) ([ca20219cf45305de25dfb715f69dd63bce9981b7](https://github.com/googleapis/python-bigtable/commit/ca20219cf45305de25dfb715f69dd63bce9981b7))
* add basic interceptor to client (#1206) ([6561cfac605ba7c5b3f750c3bdca9108e517ba77](https://github.com/googleapis/python-bigtable/commit/6561cfac605ba7c5b3f750c3bdca9108e517ba77))
* add PeerInfo proto in Bigtable API ([72dfdc440c22db0f4c372e6f11a9f7dc83fed350](https://github.com/googleapis/python-bigtable/commit/72dfdc440c22db0f4c372e6f11a9f7dc83fed350))
* Add Type API updates needed to support structured keys in materialized views ([72dfdc440c22db0f4c372e6f11a9f7dc83fed350](https://github.com/googleapis/python-bigtable/commit/72dfdc440c22db0f4c372e6f11a9f7dc83fed350))
* Add encodings for STRUCT and the Timestamp type ([72dfdc440c22db0f4c372e6f11a9f7dc83fed350](https://github.com/googleapis/python-bigtable/commit/72dfdc440c22db0f4c372e6f11a9f7dc83fed350))


### Bug Fixes

* async client uses fixed grace period (#1236) ([544db1cd7af876298b8637f495b6c7b2a0bcf16c](https://github.com/googleapis/python-bigtable/commit/544db1cd7af876298b8637f495b6c7b2a0bcf16c))
* re-export AddToCell for consistency (#1241) ([2a5baf11d30dc383a7b48d5f43b6cbb6160782e3](https://github.com/googleapis/python-bigtable/commit/2a5baf11d30dc383a7b48d5f43b6cbb6160782e3))
* retry cancelled errors (#1235) ([e3fd5d8668303db4ed35e9bf6be48b46954f9d67](https://github.com/googleapis/python-bigtable/commit/e3fd5d8668303db4ed35e9bf6be48b46954f9d67))
* Add ReadRows/SampleRowKeys bindings for materialized views ([72dfdc440c22db0f4c372e6f11a9f7dc83fed350](https://github.com/googleapis/python-bigtable/commit/72dfdc440c22db0f4c372e6f11a9f7dc83fed350))
* Deprecate credentials_file argument ([72dfdc440c22db0f4c372e6f11a9f7dc83fed350](https://github.com/googleapis/python-bigtable/commit/72dfdc440c22db0f4c372e6f11a9f7dc83fed350))

## [2.34.0](https://github.com/googleapis/python-bigtable/compare/v2.33.0...v2.34.0) (2025-10-16)


### Features

* Add support for Python 3.14 ([#1217](https://github.com/googleapis/python-bigtable/issues/1217)) ([263332a](https://github.com/googleapis/python-bigtable/commit/263332af71a229cb4fa598008a708137086a6f67))

## [2.33.0](https://github.com/googleapis/python-bigtable/compare/v2.32.0...v2.33.0) (2025-10-06)


### Features

* Add support for Proto and Enum types ([#1202](https://github.com/googleapis/python-bigtable/issues/1202)) ([34ceb86](https://github.com/googleapis/python-bigtable/commit/34ceb86007db08d453fa25cca4968d5b498ffcd6))
* Expose universe_domain for tpc ([#1150](https://github.com/googleapis/python-bigtable/issues/1150)) ([451fd97](https://github.com/googleapis/python-bigtable/commit/451fd97e435218ffed47d39423680ffc4feccac4))


### Bug Fixes

* Fix instance registration cleanup on early iterator termination ([#1216](https://github.com/googleapis/python-bigtable/issues/1216)) ([bbfd746](https://github.com/googleapis/python-bigtable/commit/bbfd746c61a6362efa42c7899ec3e34ceb541c83))
* Refactor channel refresh ([#1174](https://github.com/googleapis/python-bigtable/issues/1174)) ([6fa3008](https://github.com/googleapis/python-bigtable/commit/6fa30084058bc34d4487d1fee5c87d7795ff167a))

## [2.32.0](https://github.com/googleapis/python-bigtable/compare/v2.31.0...v2.32.0) (2025-08-01)


### Features

* Add Idempotency to Cloud Bigtable MutateRowsRequest API ([#1143](https://github.com/googleapis/python-bigtable/issues/1143)) ([c3e3eb0](https://github.com/googleapis/python-bigtable/commit/c3e3eb0e4ce44ece72b150dc5822846627074fba))
* Add support for AddToCell in Data Client ([#1147](https://github.com/googleapis/python-bigtable/issues/1147)) ([1a5b4b5](https://github.com/googleapis/python-bigtable/commit/1a5b4b514cadae5c83d61296314285d3774992c5))
* Implement SQL support in test proxy ([#1106](https://github.com/googleapis/python-bigtable/issues/1106)) ([7a91bbf](https://github.com/googleapis/python-bigtable/commit/7a91bbfb9df23f7e93c40b88648840342af6f16f))
* Modernized Bigtable Admin Client featuring selective GAPIC generation ([#1177](https://github.com/googleapis/python-bigtable/issues/1177)) ([58e7d37](https://github.com/googleapis/python-bigtable/commit/58e7d3782df6b13a42af053263afc575222a6b83))

## [2.31.0](https://github.com/googleapis/python-bigtable/compare/v2.30.1...v2.31.0) (2025-05-22)


### Features

* Add deletion_protection support for LVs ([#1108](https://github.com/googleapis/python-bigtable/issues/1108)) ([c6d384d](https://github.com/googleapis/python-bigtable/commit/c6d384d4a104c182326e22dc3f10b7b905780dee))
* Support authorized views ([#1034](https://github.com/googleapis/python-bigtable/issues/1034)) ([97a0198](https://github.com/googleapis/python-bigtable/commit/97a019833d82e617769c56761aa5548d3ab896b9))
* Throw better error on invalid metadata response ([#1107](https://github.com/googleapis/python-bigtable/issues/1107)) ([2642317](https://github.com/googleapis/python-bigtable/commit/2642317077b723ca8fd62aa86322b524868c2c4d))


### Bug Fixes

* Re-add py-typed file for bigtable package ([#1085](https://github.com/googleapis/python-bigtable/issues/1085)) ([0c322c7](https://github.com/googleapis/python-bigtable/commit/0c322c79ecbe4cde3e79d8e83ac655a978d07877))

## [2.30.1](https://github.com/googleapis/python-bigtable/compare/v2.30.0...v2.30.1) (2025-04-17)


### Bug Fixes

* Populate SQL app_profile_id header even when it is unset ([#1109](https://github.com/googleapis/python-bigtable/issues/1109)) ([17b75bd](https://github.com/googleapis/python-bigtable/commit/17b75bd746cb0a616f64a05eb0ed72b46de28a17))

## [2.30.0](https://github.com/googleapis/python-bigtable/compare/v2.29.0...v2.30.0) (2025-03-18)


### Features

* Update ExecuteQuery to use Prepare ([#1100](https://github.com/googleapis/python-bigtable/issues/1100)) ([8a7abc1](https://github.com/googleapis/python-bigtable/commit/8a7abc1e9c34a9122b2d648e8a358a7097ed3a5d))


### Bug Fixes

* Allow protobuf 6.x ([#1092](https://github.com/googleapis/python-bigtable/issues/1092)) ([1015fa8](https://github.com/googleapis/python-bigtable/commit/1015fa83c505487f09820e3a37f76690bd00ab5d))
* Remove setup.cfg configuration for creating universal wheels ([#1097](https://github.com/googleapis/python-bigtable/issues/1097)) ([95f4b82](https://github.com/googleapis/python-bigtable/commit/95f4b8233cba2a18633e64c5e0bc177e23767a83))

## [2.29.0](https://github.com/googleapis/python-bigtable/compare/v2.28.1...v2.29.0) (2025-02-26)


### Features

* Add support for array and float32 SQL query params ([#1078](https://github.com/googleapis/python-bigtable/issues/1078)) ([89b8da8](https://github.com/googleapis/python-bigtable/commit/89b8da8a445aeb08854d9fa77cbc0e4fc042c87f))


### Bug Fixes

* Grpc channel refresh ([#1087](https://github.com/googleapis/python-bigtable/issues/1087)) ([f44b36b](https://github.com/googleapis/python-bigtable/commit/f44b36bf51e3e4e3b8a774f96e682d3f1f8d4b16))

## [2.28.1](https://github.com/googleapis/python-bigtable/compare/v2.28.0...v2.28.1) (2025-01-17)


### Bug Fixes

* Allow empty headers for btql routing ([#1072](https://github.com/googleapis/python-bigtable/issues/1072)) ([e7ecfeb](https://github.com/googleapis/python-bigtable/commit/e7ecfeb8984a45c880d9483305964fff347eb4b8))

## [2.28.0](https://github.com/googleapis/python-bigtable/compare/v2.27.0...v2.28.0) (2025-01-08)


### Features

* Add generated sync client ([#1017](https://github.com/googleapis/python-bigtable/issues/1017)) ([f974823](https://github.com/googleapis/python-bigtable/commit/f974823bf8a74c2f8b1bc69997b13bc1acaf8bef))

## [2.27.0](https://github.com/googleapis/python-bigtable/compare/v2.26.0...v2.27.0) (2024-11-12)


### Features

* Add support for Cloud Bigtable Node Scaling Factor for CBT Clusters ([#1023](https://github.com/googleapis/python-bigtable/issues/1023)) ([0809c6a](https://github.com/googleapis/python-bigtable/commit/0809c6ac274e909103ad160a8bcab95f8bb46f31))
* Surface `retry` param to `Table.read_row` api ([#982](https://github.com/googleapis/python-bigtable/issues/982)) ([a8286d2](https://github.com/googleapis/python-bigtable/commit/a8286d2a510f654f9c270c3c761c02e4ab3817d4))


### Bug Fixes

* Registering duplicate instance ([#1033](https://github.com/googleapis/python-bigtable/issues/1033)) ([2bca8fb](https://github.com/googleapis/python-bigtable/commit/2bca8fb220eeb1906fc6a3cf1f879f3d41fbbff8))

## [2.26.0](https://github.com/googleapis/python-bigtable/compare/v2.25.0...v2.26.0) (2024-08-12)


### Features

* Add fields and the BackupType proto for Hot Backups ([#1010](https://github.com/googleapis/python-bigtable/issues/1010)) ([b95801f](https://github.com/googleapis/python-bigtable/commit/b95801ffa8081e0072232247fbc5879105c109a6))
* Add MergeToCell to Mutation APIs ([f029a24](https://github.com/googleapis/python-bigtable/commit/f029a242e2b0e6020d0b87ef256a414194321fad))
* Add min, max, hll aggregators and more types ([f029a24](https://github.com/googleapis/python-bigtable/commit/f029a242e2b0e6020d0b87ef256a414194321fad))
* Async execute query client ([#1011](https://github.com/googleapis/python-bigtable/issues/1011)) ([45bc8c4](https://github.com/googleapis/python-bigtable/commit/45bc8c4a0fe567ce5e0126a1a70e7eb3dca93e92))


### Bug Fixes

* Use single routing metadata header ([#1005](https://github.com/googleapis/python-bigtable/issues/1005)) ([20eeb0a](https://github.com/googleapis/python-bigtable/commit/20eeb0a68d7b44d07a6d84bc7a7e040ad63bb96d))


### Documentation

* Add clarification around SQL timestamps ([#1012](https://github.com/googleapis/python-bigtable/issues/1012)) ([6e80190](https://github.com/googleapis/python-bigtable/commit/6e801900bbe9385d3b579b8c3327c87c3617d92f))
* Corrected various type documentation ([f029a24](https://github.com/googleapis/python-bigtable/commit/f029a242e2b0e6020d0b87ef256a414194321fad))

## [2.25.0](https://github.com/googleapis/python-bigtable/compare/v2.24.0...v2.25.0) (2024-07-18)


### Features

* Publish ProtoRows Message ([7ac8e14](https://github.com/googleapis/python-bigtable/commit/7ac8e142f99a6891b6bc286858f764def503e89a))
* Publish the Cloud Bigtable ExecuteQuery API ([7ac8e14](https://github.com/googleapis/python-bigtable/commit/7ac8e142f99a6891b6bc286858f764def503e89a))


### Bug Fixes

* Allow protobuf 5.x ([7ac8e14](https://github.com/googleapis/python-bigtable/commit/7ac8e142f99a6891b6bc286858f764def503e89a))

## [2.24.0](https://github.com/googleapis/python-bigtable/compare/v2.23.1...v2.24.0) (2024-06-11)


### Features

* Add String type with Utf8Raw encoding to Bigtable API ([#968](https://github.com/googleapis/python-bigtable/issues/968)) ([2a2bbfd](https://github.com/googleapis/python-bigtable/commit/2a2bbfdba6737c508ab1073d37fef680ca2a8c2f))
* Improve async sharding ([#977](https://github.com/googleapis/python-bigtable/issues/977)) ([fd1f7da](https://github.com/googleapis/python-bigtable/commit/fd1f7dafd38f7f0e714a3384a27176f485523682))


### Bug Fixes

* **backup:** Backup name regex ([#970](https://github.com/googleapis/python-bigtable/issues/970)) ([6ef122a](https://github.com/googleapis/python-bigtable/commit/6ef122ad49f43e3a22cde5cb6fdaefd947670136))
* Improve rowset revision ([#979](https://github.com/googleapis/python-bigtable/issues/979)) ([da27527](https://github.com/googleapis/python-bigtable/commit/da275279a7e619e4cd3e72b10ac629d6e0e1fe47))

## [2.23.1](https://github.com/googleapis/python-bigtable/compare/v2.23.0...v2.23.1) (2024-04-15)


### Bug Fixes

* Use insecure grpc channel with emulator ([#946](https://github.com/googleapis/python-bigtable/issues/946)) ([aa31706](https://github.com/googleapis/python-bigtable/commit/aa3170663f9bd09d70c99d4e76c07f7f293ad935))

## [2.23.0](https://github.com/googleapis/python-bigtable/compare/v2.22.0...v2.23.0) (2024-02-07)


### Features

* Add async data client preview ([7088e39](https://github.com/googleapis/python-bigtable/commit/7088e39c6bac10e5f830e8fa68e181412910ec5a))
* Adding feature flags for routing cookie and retry info ([#905](https://github.com/googleapis/python-bigtable/issues/905)) ([1859e67](https://github.com/googleapis/python-bigtable/commit/1859e67961629663a8749eea849b5b005fcbc09f))


### Bug Fixes

* Fix `ValueError` in `test__validate_universe_domain` ([#929](https://github.com/googleapis/python-bigtable/issues/929)) ([aa76a5a](https://github.com/googleapis/python-bigtable/commit/aa76a5aaa349386d5972d96e1255389e30df8764))

## [2.22.0](https://github.com/googleapis/python-bigtable/compare/v2.21.0...v2.22.0) (2023-12-12)


### Features

* Add support for Cloud Bigtable Request Priorities in App Profiles ([#871](https://github.com/googleapis/python-bigtable/issues/871)) ([a4d551e](https://github.com/googleapis/python-bigtable/commit/a4d551e34006202ee96a395a2107d7acdc5881de))
* Add support for Python 3.12 ([#888](https://github.com/googleapis/python-bigtable/issues/888)) ([4f050aa](https://github.com/googleapis/python-bigtable/commit/4f050aa5aed9a9dcf209779d5c10e5de8e2ff19e))
* Introduce compatibility with native namespace packages ([#893](https://github.com/googleapis/python-bigtable/issues/893)) ([d218f4e](https://github.com/googleapis/python-bigtable/commit/d218f4ebd4ed6705721dca9318df955b40b0d0ac))
* Publish CopyBackup protos to external customers ([#855](https://github.com/googleapis/python-bigtable/issues/855)) ([4105df7](https://github.com/googleapis/python-bigtable/commit/4105df762f1318c49bba030063897f0c50e4daee))


### Bug Fixes

* Add feature flag for improved mutate rows throttling ([e5af359](https://github.com/googleapis/python-bigtable/commit/e5af3597f45fc4c094c59abca876374f5a866c1b))
* Add lock to flow control ([#899](https://github.com/googleapis/python-bigtable/issues/899)) ([e4e63c7](https://github.com/googleapis/python-bigtable/commit/e4e63c7b5b91273b3aae04fda59cc5a21c848de2))
* Mutations batcher race condition ([#896](https://github.com/googleapis/python-bigtable/issues/896)) ([fe58f61](https://github.com/googleapis/python-bigtable/commit/fe58f617c7364d7e99e2ec50abd5f080852bf033))
* Require google-cloud-core 1.4.4 ([#866](https://github.com/googleapis/python-bigtable/issues/866)) ([09f8a46](https://github.com/googleapis/python-bigtable/commit/09f8a4667d8b68a9f2048ba1aa57db4f775a2c03))
* Use `retry_async` instead of `retry` in async client ([597efd1](https://github.com/googleapis/python-bigtable/commit/597efd11d15f20549010b4301be4d9768326e6a2))


### Documentation

* Minor formatting ([e5af359](https://github.com/googleapis/python-bigtable/commit/e5af3597f45fc4c094c59abca876374f5a866c1b))

## [2.21.0](https://github.com/googleapis/python-bigtable/compare/v2.20.0...v2.21.0) (2023-08-02)


### Features

* Add last_scanned_row_responses to FeatureFlags ([#845](https://github.com/googleapis/python-bigtable/issues/845)) ([14a6739](https://github.com/googleapis/python-bigtable/commit/14a673901f82fa247c8027730a0bba41e0ec4757))


### Documentation

* Minor formatting ([#851](https://github.com/googleapis/python-bigtable/issues/851)) ([5ebe231](https://github.com/googleapis/python-bigtable/commit/5ebe2312dab70210811fca68c6625d2546442afd))

## [2.20.0](https://github.com/googleapis/python-bigtable/compare/v2.19.0...v2.20.0) (2023-07-17)


### Features

* Add experimental reverse scan for public preview ([d5720f8](https://github.com/googleapis/python-bigtable/commit/d5720f8f5b5a81572f31d40051b3ec0f1d104304))
* Increase the maximum retention period for a Cloud Bigtable backup from 30 days to 90 days ([d5720f8](https://github.com/googleapis/python-bigtable/commit/d5720f8f5b5a81572f31d40051b3ec0f1d104304))


### Bug Fixes

* Add async context manager return types ([#828](https://github.com/googleapis/python-bigtable/issues/828)) ([475a160](https://github.com/googleapis/python-bigtable/commit/475a16072f3ad41357bdb765fff608a39141ec00))


### Documentation

* Fix formatting for reversed order field example ([#831](https://github.com/googleapis/python-bigtable/issues/831)) ([fddd0ba](https://github.com/googleapis/python-bigtable/commit/fddd0ba97155e112af92a98fd8f20e59b139d177))

## [2.19.0](https://github.com/googleapis/python-bigtable/compare/v2.18.1...v2.19.0) (2023-06-08)


### Features

* Add ChangeStreamConfig to CreateTable and UpdateTable ([#786](https://github.com/googleapis/python-bigtable/issues/786)) ([cef70f2](https://github.com/googleapis/python-bigtable/commit/cef70f243541820225f86a520e0b2abd3a7354f7))


### Bug Fixes

* Add a callback function on flush_rows ([#796](https://github.com/googleapis/python-bigtable/issues/796)) ([589aa5d](https://github.com/googleapis/python-bigtable/commit/589aa5d04f6b5a2bd310d0bf06aeb7058fb6fcd2))


### Documentation

* **samples:** Add region tags ([#788](https://github.com/googleapis/python-bigtable/issues/788)) ([ecf539c](https://github.com/googleapis/python-bigtable/commit/ecf539c4c976fd9e5505b8abf0b697b218f09fef))

## [2.18.1](https://github.com/googleapis/python-bigtable/compare/v2.18.0...v2.18.1) (2023-05-11)


### Bug Fixes

* Revert "Feat: Threaded MutationsBatcher" ([#773](https://github.com/googleapis/python-bigtable/issues/773)) ([a767cff](https://github.com/googleapis/python-bigtable/commit/a767cff95d990994f85f5fd05cc10f952087b49d))

## [2.18.0](https://github.com/googleapis/python-bigtable/compare/v2.17.0...v2.18.0) (2023-05-10)


### Features

* Publish RateLimitInfo and FeatureFlag protos ([#768](https://github.com/googleapis/python-bigtable/issues/768)) ([171fea6](https://github.com/googleapis/python-bigtable/commit/171fea6de57a47f92a2a56050f8bfe7518144df7))
* Threaded MutationsBatcher ([#722](https://github.com/googleapis/python-bigtable/issues/722)) ([7521a61](https://github.com/googleapis/python-bigtable/commit/7521a617c121ead96a21ca47959a53b2db2da090))


### Bug Fixes

* Pass the "retry" when calling read_rows. ([#759](https://github.com/googleapis/python-bigtable/issues/759)) ([505273b](https://github.com/googleapis/python-bigtable/commit/505273b72bf83d8f92d0e0a92d62f22bce96cc3d))


### Documentation

* Fix delete from column family example ([#764](https://github.com/googleapis/python-bigtable/issues/764)) ([128b4e1](https://github.com/googleapis/python-bigtable/commit/128b4e1f3eea2dad903d84c8f2933b17a5f0d226))
* Fix formatting of request arg in docstring ([#756](https://github.com/googleapis/python-bigtable/issues/756)) ([45d3e43](https://github.com/googleapis/python-bigtable/commit/45d3e4308c4f494228c2e6e18a36285c557cb0c3))

## [2.17.0](https://github.com/googleapis/python-bigtable/compare/v2.16.0...v2.17.0) (2023-03-01)


### Features

* Add new_partitions field for CloseStream for Cloud Bigtable ChangeStream ([#740](https://github.com/googleapis/python-bigtable/issues/740)) ([1adcad4](https://github.com/googleapis/python-bigtable/commit/1adcad440368f6d7df6710a013e7fab076461aed))

## [2.16.0](https://github.com/googleapis/python-bigtable/compare/v2.15.0...v2.16.0) (2023-02-27)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([c5116e0](https://github.com/googleapis/python-bigtable/commit/c5116e097aacf9ddae249de57fab1849aff10d86))
* Publish the Cloud Bigtable Change Streams ([c5116e0](https://github.com/googleapis/python-bigtable/commit/c5116e097aacf9ddae249de57fab1849aff10d86))


### Bug Fixes

* Add context manager return types ([beb5bf3](https://github.com/googleapis/python-bigtable/commit/beb5bf3bca4b517d095de3faa17d20e4d89fb295))
* **deps:** Require google-api-core&gt;=1.34.0,>=2.11.0 ([c5116e0](https://github.com/googleapis/python-bigtable/commit/c5116e097aacf9ddae249de57fab1849aff10d86))


### Documentation

* Add documentation for enums ([beb5bf3](https://github.com/googleapis/python-bigtable/commit/beb5bf3bca4b517d095de3faa17d20e4d89fb295))

## [2.15.0](https://github.com/googleapis/python-bigtable/compare/v2.14.1...v2.15.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#718](https://github.com/googleapis/python-bigtable/issues/718)) ([803a15e](https://github.com/googleapis/python-bigtable/commit/803a15ef0cd3713411eeb5d21258c12bbe1dcab6))

## [2.14.1](https://github.com/googleapis/python-bigtable/compare/v2.14.0...v2.14.1) (2022-12-06)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))
* Drop usage of pkg_resources ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))
* Fix timeout default values ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))

## [2.14.0](https://github.com/googleapis/python-bigtable/compare/v2.13.2...v2.14.0) (2022-11-30)


### Features

* Add typing to proto.Message based class attributes ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* remove enum value ReadRowsRequest.RequestStatsView.REQUEST_STATS_EFFICIENCY ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* remove field ReadIterationStats.deletes_seen ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* remove field RequestStats.read_efficiency_stats ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* remove proto ReadEfficiencyStats  ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* rename field RequestStats.all_read_stats to full_read_stats_view ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* rename proto AllReadStats to FullReadStatsView ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
* rename proto ReadIteratorStats to ReadIterationStats ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))


### Bug Fixes

* Add dict typing for client_options ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))

## [2.13.2](https://github.com/googleapis/python-bigtable/compare/v2.13.1...v2.13.2) (2022-10-20)


### Bug Fixes

* Respect deadlines for column family operations ([#687](https://github.com/googleapis/python-bigtable/issues/687)) ([df2e64a](https://github.com/googleapis/python-bigtable/commit/df2e64a79bbd8b28d0991706607af99d539320d1))

## [2.13.1](https://github.com/googleapis/python-bigtable/compare/v2.13.0...v2.13.1) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#682](https://github.com/googleapis/python-bigtable/issues/682)) ([0bb3420](https://github.com/googleapis/python-bigtable/commit/0bb3420decac74058ee099d72f8932556409f2aa))

## [2.13.0](https://github.com/googleapis/python-bigtable/compare/v2.12.0...v2.13.0) (2022-09-29)


### Features

* Publish the RequestStats proto ([#676](https://github.com/googleapis/python-bigtable/issues/676)) ([199949b](https://github.com/googleapis/python-bigtable/commit/199949b2a930706654680b91a93f2a903bf112bf))


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#679](https://github.com/googleapis/python-bigtable/issues/679)) ([030ef38](https://github.com/googleapis/python-bigtable/commit/030ef3868c442a8a21c4b4d6217b99cab09a1be7))

## [2.12.0](https://github.com/googleapis/python-bigtable/compare/v2.11.3...v2.12.0) (2022-09-19)


### Features

* Publish CBT deletion_protection field in Table, UpdateTableRequest, and UpdateTable API ([#670](https://github.com/googleapis/python-bigtable/issues/670)) ([c57289c](https://github.com/googleapis/python-bigtable/commit/c57289c03335380694580202d746ca4f679dce9b))


### Documentation

* Remove unnecessary comment ([#674](https://github.com/googleapis/python-bigtable/issues/674)) ([9c62655](https://github.com/googleapis/python-bigtable/commit/9c62655de7fecd93ee7a1bb95b208d94798727cd))

## [2.11.3](https://github.com/googleapis/python-bigtable/compare/v2.11.2...v2.11.3) (2022-08-17)


### Performance Improvements

* optimize row merging ([#628](https://github.com/googleapis/python-bigtable/issues/628)) ([c71ec70](https://github.com/googleapis/python-bigtable/commit/c71ec70e55f6e236e46127870a9ed4717eee5da5))

## [2.11.2](https://github.com/googleapis/python-bigtable/compare/v2.11.1...v2.11.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#631](https://github.com/googleapis/python-bigtable/issues/631)) ([fd54fc6](https://github.com/googleapis/python-bigtable/commit/fd54fc63340a3e01fae1ccc4c648dd90900f8a94))
* **deps:** require proto-plus >= 1.22.0 ([fd54fc6](https://github.com/googleapis/python-bigtable/commit/fd54fc63340a3e01fae1ccc4c648dd90900f8a94))

## [2.11.1](https://github.com/googleapis/python-bigtable/compare/v2.11.0...v2.11.1) (2022-08-08)


### Bug Fixes

* Retry the RST Stream error in mutate rows and read rows([#624](https://github.com/googleapis/python-bigtable/issues/624)) ([d24574a](https://github.com/googleapis/python-bigtable/commit/d24574a722de61bdeffa6588bcb08f56e62ba3bd))

## [2.11.0](https://github.com/googleapis/python-bigtable/compare/v2.10.1...v2.11.0) (2022-08-04)


### Features

* add audience parameter ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))
* add satisfies_pzs output only field ([#614](https://github.com/googleapis/python-bigtable/issues/614)) ([7dc1469](https://github.com/googleapis/python-bigtable/commit/7dc1469fef2dc38f1509b35a37e9c97381ab7601))
* Add storage_utilization_gib_per_node to Autoscaling target ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))
* Cloud Bigtable Undelete Table service and message proto files ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))
* require python 3.7+ ([#610](https://github.com/googleapis/python-bigtable/issues/610)) ([10d00f5](https://github.com/googleapis/python-bigtable/commit/10d00f5af5d5878c26529f5e48a5fb8d8385696d))


### Performance Improvements

* improve row merging ([#619](https://github.com/googleapis/python-bigtable/issues/619)) ([b4853e5](https://github.com/googleapis/python-bigtable/commit/b4853e59d0efd8a7b37f3fcb06b14dbd9f5d20a4))

## [2.10.1](https://github.com/googleapis/python-bigtable/compare/v2.10.0...v2.10.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#595](https://github.com/googleapis/python-bigtable/issues/595)) ([a4deaf7](https://github.com/googleapis/python-bigtable/commit/a4deaf7b1b5c4b7ce8f6dc5bb96d32ea8ff55c2d))


### Documentation

* fix changelog header to consistent size ([#596](https://github.com/googleapis/python-bigtable/issues/596)) ([51961c3](https://github.com/googleapis/python-bigtable/commit/51961c32686fe5851e957581b85adbe92a073e03))

## [2.10.0](https://github.com/googleapis/python-bigtable/compare/v2.9.0...v2.10.0) (2022-05-30)


### Features

* refreshes Bigtable Admin API(s) protos ([#589](https://github.com/googleapis/python-bigtable/issues/589)) ([b508e33](https://github.com/googleapis/python-bigtable/commit/b508e3321937850d65242283e82f5413feb6081a))


### Documentation

* Add EncryptionInfo documentation ([#588](https://github.com/googleapis/python-bigtable/issues/588)) ([bedbf1b](https://github.com/googleapis/python-bigtable/commit/bedbf1b1bb304ff45f31ad20004ff96041ce716c))

## [2.9.0](https://github.com/googleapis/python-bigtable/compare/v2.8.1...v2.9.0) (2022-04-14)


### Features

* App Profile multi cluster routing support with specified cluster ids ([#549](https://github.com/googleapis/python-bigtable/issues/549)) ([a0ed5b5](https://github.com/googleapis/python-bigtable/commit/a0ed5b5dfda1f3980b1a8eb349b2b5d8ab428a4b))
* AuditConfig for IAM v1 ([4e50278](https://github.com/googleapis/python-bigtable/commit/4e50278c73f608a7c493692d8d17e7dd2aa7ba44))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([4e50278](https://github.com/googleapis/python-bigtable/commit/4e50278c73f608a7c493692d8d17e7dd2aa7ba44))


### Documentation

* fix type in docstring for map fields ([4e50278](https://github.com/googleapis/python-bigtable/commit/4e50278c73f608a7c493692d8d17e7dd2aa7ba44))

## [2.8.1](https://github.com/googleapis/python-bigtable/compare/v2.8.0...v2.8.1) (2022-04-07)


### Bug Fixes

* Prevent sending full table scan when retrying ([#554](https://github.com/googleapis/python-bigtable/issues/554)) ([56f5357](https://github.com/googleapis/python-bigtable/commit/56f5357c09ac867491b934f6029776dcd74c6eac))

## [2.8.0](https://github.com/googleapis/python-bigtable/compare/v2.7.1...v2.8.0) (2022-04-04)


### Features

* Add ListHotTablets API method and protobufs ([#542](https://github.com/googleapis/python-bigtable/issues/542)) ([483f139](https://github.com/googleapis/python-bigtable/commit/483f139f5065d55378bd850c33e89db460119fc1))


### Documentation

* explain mutate vs mutate_rows ([#543](https://github.com/googleapis/python-bigtable/issues/543)) ([84cfb0a](https://github.com/googleapis/python-bigtable/commit/84cfb0abdfabd8aa2f292fc0bb7e6deab50f87f1))
* Remove the limitation that all clusters in a CMEK instance must use the same key ([f008eea](https://github.com/googleapis/python-bigtable/commit/f008eea69a6c7c1a027cefc7f16d46042b524db1))
* Update `cpu_utilization_percent` limit ([#547](https://github.com/googleapis/python-bigtable/issues/547)) ([f008eea](https://github.com/googleapis/python-bigtable/commit/f008eea69a6c7c1a027cefc7f16d46042b524db1))

## [2.7.1](https://github.com/googleapis/python-bigtable/compare/v2.7.0...v2.7.1) (2022-03-17)


### Bug Fixes

* Ensure message fields are copied when building retry request ([#533](https://github.com/googleapis/python-bigtable/issues/533)) ([ff7f190](https://github.com/googleapis/python-bigtable/commit/ff7f1901b6420e66e1388e757eeec20d30484ad9))

## [2.7.0](https://github.com/googleapis/python-bigtable/compare/v2.6.0...v2.7.0) (2022-03-06)


### Features

* Add support for autoscaling ([#509](https://github.com/googleapis/python-bigtable/issues/509)) ([8f4e197](https://github.com/googleapis/python-bigtable/commit/8f4e197148644ded934190814ff44fa132a2dda6))


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#526](https://github.com/googleapis/python-bigtable/issues/526)) ([a8a92ee](https://github.com/googleapis/python-bigtable/commit/a8a92ee1b6bd284055fee3e1029a9a6aacbc5f1c))
* **deps:** require proto-plus>=1.15.0 ([a8a92ee](https://github.com/googleapis/python-bigtable/commit/a8a92ee1b6bd284055fee3e1029a9a6aacbc5f1c))

## [2.6.0](https://github.com/googleapis/python-bigtable/compare/v2.5.2...v2.6.0) (2022-02-26)


### Features

* add WarmAndPing request for channel priming ([#504](https://github.com/googleapis/python-bigtable/issues/504)) ([df5fc1f](https://github.com/googleapis/python-bigtable/commit/df5fc1f7d6ded88d9bce67f7cc6989981745931f))

## [2.5.2](https://github.com/googleapis/python-bigtable/compare/v2.5.1...v2.5.2) (2022-02-24)


### Bug Fixes

* Pass app_profile_id when building updated request ([#512](https://github.com/googleapis/python-bigtable/issues/512)) ([2f8ba7a](https://github.com/googleapis/python-bigtable/commit/2f8ba7a4801b17b5afb6180a7ace1327a2d05a52))

## [2.5.1](https://github.com/googleapis/python-bigtable/compare/v2.5.0...v2.5.1) (2022-02-17)


### Bug Fixes

* **deps:** move libcst to extras ([#508](https://github.com/googleapis/python-bigtable/issues/508)) ([4b4d7e2](https://github.com/googleapis/python-bigtable/commit/4b4d7e2796788b2cd3764f54ff532a9c9d092aec))

## [2.5.0](https://github.com/googleapis/python-bigtable/compare/v2.4.0...v2.5.0) (2022-02-07)


### Features

* add 'Instance.create_time' field ([#449](https://github.com/googleapis/python-bigtable/issues/449)) ([b9ecfa9](https://github.com/googleapis/python-bigtable/commit/b9ecfa97281ae21dcf233e60c70cacc701f12c32))
* add api key support ([#497](https://github.com/googleapis/python-bigtable/issues/497)) ([ee3a6c4](https://github.com/googleapis/python-bigtable/commit/ee3a6c4c5f810fab08671db3407195864ecc1972))
* add Autoscaling API ([#475](https://github.com/googleapis/python-bigtable/issues/475)) ([97b3cdd](https://github.com/googleapis/python-bigtable/commit/97b3cddb908098e255e7a1209cdb985087b95a26))
* add context manager support in client ([#440](https://github.com/googleapis/python-bigtable/issues/440)) ([a3d2cf1](https://github.com/googleapis/python-bigtable/commit/a3d2cf18b49cddc91e5e6448c46d6b936d86954d))
* add support for Python 3.10 ([#437](https://github.com/googleapis/python-bigtable/issues/437)) ([3cf0814](https://github.com/googleapis/python-bigtable/commit/3cf08149411f3f4df41e9b5a9894dbfb101bd86f))


### Bug Fixes

* **deps:** drop packaging dependency ([a535f99](https://github.com/googleapis/python-bigtable/commit/a535f99e9f0bb16488a5d372a0a6efc3c4b69186))
* **deps:** require google-api-core >= 1.28.0 ([a535f99](https://github.com/googleapis/python-bigtable/commit/a535f99e9f0bb16488a5d372a0a6efc3c4b69186))
* improper types in pagers generation ([f9c7699](https://github.com/googleapis/python-bigtable/commit/f9c7699eb6d4071314abbb0477ba47370059e041))
* improve type hints, mypy checks ([#448](https://github.com/googleapis/python-bigtable/issues/448)) ([a99bf88](https://github.com/googleapis/python-bigtable/commit/a99bf88417d6aec03923447c70c2752f6bb5c459))
* resolve DuplicateCredentialArgs error when using credentials_file ([d6bff70](https://github.com/googleapis/python-bigtable/commit/d6bff70654b41e31d2ac83d307bdc6bbd111201e))


### Documentation

* clarify comments in ReadRowsRequest and RowFilter ([#494](https://github.com/googleapis/python-bigtable/issues/494)) ([1efd9b5](https://github.com/googleapis/python-bigtable/commit/1efd9b598802f766a3c4c8c78ec7b0ca208d3325))
* list oneofs in docstring ([a535f99](https://github.com/googleapis/python-bigtable/commit/a535f99e9f0bb16488a5d372a0a6efc3c4b69186))

## [2.4.0](https://www.github.com/googleapis/python-bigtable/compare/v2.3.3...v2.4.0) (2021-09-24)


### Features

* Publish new fields to support cluster group routing for Cloud Bigtable ([#407](https://www.github.com/googleapis/python-bigtable/issues/407)) ([66af554](https://www.github.com/googleapis/python-bigtable/commit/66af554a103eea0139cb313691d69f4c88a9e87f))


### Bug Fixes

* add 'dict' annotation type to 'request' ([160bfd3](https://www.github.com/googleapis/python-bigtable/commit/160bfd317a83561821acc0212d3514701a031ac6))

## [2.3.3](https://www.github.com/googleapis/python-bigtable/compare/v2.3.2...v2.3.3) (2021-07-24)


### Bug Fixes

* enable self signed jwt for grpc ([#397](https://www.github.com/googleapis/python-bigtable/issues/397)) ([9d43a38](https://www.github.com/googleapis/python-bigtable/commit/9d43a388470746608d324ca8d72f41bb3a4492b7))

## [2.3.2](https://www.github.com/googleapis/python-bigtable/compare/v2.3.1...v2.3.2) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#379](https://www.github.com/googleapis/python-bigtable/issues/379)) ([95b2e13](https://www.github.com/googleapis/python-bigtable/commit/95b2e13b776dca4a6998313c41aa960ffe2e47e9))
* directly append to pb for beter read row performance ([#382](https://www.github.com/googleapis/python-bigtable/issues/382)) ([7040e11](https://www.github.com/googleapis/python-bigtable/commit/7040e113b93bb2e0625c054486305235d8f14c2a))

## [2.3.1](https://www.github.com/googleapis/python-bigtable/compare/v2.3.0...v2.3.1) (2021-07-13)


### Bug Fixes

* use public 'table_admin_client' property in backups methods ([#359](https://www.github.com/googleapis/python-bigtable/issues/359)) ([bc57c79](https://www.github.com/googleapis/python-bigtable/commit/bc57c79640b270ff89fd10ec243dd04559168c5c))

## [2.3.0](https://www.github.com/googleapis/python-bigtable/compare/v2.2.0...v2.3.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#333](https://www.github.com/googleapis/python-bigtable/issues/333)) ([f1fce5b](https://www.github.com/googleapis/python-bigtable/commit/f1fce5b0694d965202fc2a4fcf8bc6e09e78deae))


### Bug Fixes

* **deps:** add packaging requirement ([#326](https://www.github.com/googleapis/python-bigtable/issues/326)) ([d31c27b](https://www.github.com/googleapis/python-bigtable/commit/d31c27b01d1f7c351effc2856a8d4777a1a10690))
* **deps:** require google-api-core >= 1.26.0 ([#344](https://www.github.com/googleapis/python-bigtable/issues/344)) ([ce4ceb6](https://www.github.com/googleapis/python-bigtable/commit/ce4ceb6d8fe74eff16cf9ca151e0b98502256a2f))
* disable always_use_jwt_access ([#348](https://www.github.com/googleapis/python-bigtable/issues/348)) ([4623248](https://www.github.com/googleapis/python-bigtable/commit/4623248376deccf4651d4badf8966311ebe3c16a))


### Documentation

* add paramter mutation_timeout to instance.table docs ([#305](https://www.github.com/googleapis/python-bigtable/issues/305)) ([5bbd06e](https://www.github.com/googleapis/python-bigtable/commit/5bbd06e5413e8b7597ba128174b10fe45fd38380))
* fix broken links in multiprocessing.rst ([#317](https://www.github.com/googleapis/python-bigtable/issues/317)) ([e329352](https://www.github.com/googleapis/python-bigtable/commit/e329352d7e6d81de1d1d770c73406a60d29d01bb))
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-bigtable/issues/1127)) ([#329](https://www.github.com/googleapis/python-bigtable/issues/329)) ([6bf0c64](https://www.github.com/googleapis/python-bigtable/commit/6bf0c647bcebed641b4cbdc5eb70528c88b26a01)), closes [#1126](https://www.github.com/googleapis/python-bigtable/issues/1126)

## [2.2.0](https://www.github.com/googleapis/python-bigtable/compare/v2.1.0...v2.2.0) (2021-04-30)


### Features

* backup restore to different instance ([#300](https://www.github.com/googleapis/python-bigtable/issues/300)) ([049a25f](https://www.github.com/googleapis/python-bigtable/commit/049a25f903bb6b062e41430b6e7ce6d7b164f22c))

## [2.1.0](https://www.github.com/googleapis/python-bigtable/compare/v2.0.0...v2.1.0) (2021-04-21)


### Features

* customer managed keys (CMEK) ([#249](https://www.github.com/googleapis/python-bigtable/issues/249)) ([93df829](https://www.github.com/googleapis/python-bigtable/commit/93df82998cc0218cbc4a1bc2ab41a48b7478758d))

## [2.0.0](https://www.github.com/googleapis/python-bigtable/compare/v1.7.0...v2.0.0) (2021-04-06)


### ⚠ BREAKING CHANGES

* microgenerator changes (#203)

### Features

* microgenerator changes ([#203](https://www.github.com/googleapis/python-bigtable/issues/203)) ([b31bd87](https://www.github.com/googleapis/python-bigtable/commit/b31bd87c3fa8cad32768611a52d5effcc7d9b3e2))
* publish new fields for CMEK ([#222](https://www.github.com/googleapis/python-bigtable/issues/222)) ([0fe5b63](https://www.github.com/googleapis/python-bigtable/commit/0fe5b638e45e711d25f55664689a9baf4d12dc57))


### Bug Fixes

* address issue in establishing an emulator connection ([#246](https://www.github.com/googleapis/python-bigtable/issues/246)) ([1a31826](https://www.github.com/googleapis/python-bigtable/commit/1a31826e2e378468e057160c07d850ebca1c5879))
* fix unit test that could be broken by user's environment ([#239](https://www.github.com/googleapis/python-bigtable/issues/239)) ([cbd712e](https://www.github.com/googleapis/python-bigtable/commit/cbd712e6d3aded0c025525f97da1d667fbe2f061))
* guard assignments of certain values against None ([#220](https://www.github.com/googleapis/python-bigtable/issues/220)) ([341f448](https://www.github.com/googleapis/python-bigtable/commit/341f448ce378375ab79bfc82f864fb6c88ed71a0))
* **retry:** restore grpc_service_config for CreateBackup and {Restore,Snapshot}Table ([#240](https://www.github.com/googleapis/python-bigtable/issues/240)) ([79f1734](https://www.github.com/googleapis/python-bigtable/commit/79f1734c897e5e1b2fd02d043185c44b7ee34dc9))


### Documentation

* add backup docs ([#251](https://www.github.com/googleapis/python-bigtable/issues/251)) ([7d5c7aa](https://www.github.com/googleapis/python-bigtable/commit/7d5c7aa92cb476b07ac9efb5d231888c4c417783))


### Dependencies

* update gapic-generator-python to 0.40.11 ([#230](https://www.github.com/googleapis/python-bigtable/issues/230)) ([47d5dc1](https://www.github.com/googleapis/python-bigtable/commit/47d5dc1853f0be609e666e8a8fad0146f2905482))
* upgrade gapic-generator-python to 0.43.1 ([#276](https://www.github.com/googleapis/python-bigtable/issues/276)) ([0e9fe54](https://www.github.com/googleapis/python-bigtable/commit/0e9fe5410e1b5d16ae0735ba1f606f7d1befafb9))

## [2.0.0-dev1](https://www.github.com/googleapis/python-bigtable/compare/v1.7.0...v2.0.0-dev1) (2021-02-24)


### ⚠ BREAKING CHANGES

* microgenerator changes (#203)

### Features

* microgenerator changes ([#203](https://www.github.com/googleapis/python-bigtable/issues/203)) ([b31bd87](https://www.github.com/googleapis/python-bigtable/commit/b31bd87c3fa8cad32768611a52d5effcc7d9b3e2))


### Bug Fixes

* guard assignments of certain values against None ([#220](https://www.github.com/googleapis/python-bigtable/issues/220)) ([341f448](https://www.github.com/googleapis/python-bigtable/commit/341f448ce378375ab79bfc82f864fb6c88ed71a0))

## [1.7.0](https://www.github.com/googleapis/python-bigtable/compare/v1.6.1...v1.7.0) (2021-02-09)


### Features

* add keep alive timeout ([#182](https://www.github.com/googleapis/python-bigtable/issues/182)) ([e9637cb](https://www.github.com/googleapis/python-bigtable/commit/e9637cbd4461dcca509dca43ef116d6ff41b80c7))
* support filtering on incrementable values ([#178](https://www.github.com/googleapis/python-bigtable/issues/178)) ([e221352](https://www.github.com/googleapis/python-bigtable/commit/e2213520951d3da97019a1d784e5bf31d94e3353))


### Bug Fixes

* Renaming region tags to not conflict with documentation snippets ([#190](https://www.github.com/googleapis/python-bigtable/issues/190)) ([dd0cdc5](https://www.github.com/googleapis/python-bigtable/commit/dd0cdc5bcfd92e18ab9a7255684a9f5b21198867))


### Documentation

* update python contributing guide ([#206](https://www.github.com/googleapis/python-bigtable/issues/206)) ([e301ac3](https://www.github.com/googleapis/python-bigtable/commit/e301ac3b61364d779fdb50a57ae8e2cb9952df9e))

## [1.6.1](https://www.github.com/googleapis/python-bigtable/compare/v1.6.0...v1.6.1) (2020-12-01)


### Documentation

* update intersphinx mappings ([#172](https://www.github.com/googleapis/python-bigtable/issues/172)) ([7b09368](https://www.github.com/googleapis/python-bigtable/commit/7b09368d5121782c7f271b3575c838e8a2284c05))

## [1.6.0](https://www.github.com/googleapis/python-bigtable/compare/v1.5.1...v1.6.0) (2020-11-16)


### Features

* add 'timeout' arg to 'Table.mutate_rows' ([#157](https://www.github.com/googleapis/python-bigtable/issues/157)) ([6d597a1](https://www.github.com/googleapis/python-bigtable/commit/6d597a1e5be05c993c9f86beca4c1486342caf94)), closes [/github.com/googleapis/python-bigtable/issues/7#issuecomment-715538708](https://www.github.com/googleapis//github.com/googleapis/python-bigtable/issues/7/issues/issuecomment-715538708) [#7](https://www.github.com/googleapis/python-bigtable/issues/7)
* Backup Level IAM ([#160](https://www.github.com/googleapis/python-bigtable/issues/160)) ([44932cb](https://www.github.com/googleapis/python-bigtable/commit/44932cb8710e12279dbd4e9271577f8bee238980))

## [1.5.1](https://www.github.com/googleapis/python-bigtable/compare/v1.5.0...v1.5.1) (2020-10-06)


### Bug Fixes

* harden version data gathering against DistributionNotFound ([#150](https://www.github.com/googleapis/python-bigtable/issues/150)) ([c815421](https://www.github.com/googleapis/python-bigtable/commit/c815421422f1c845983e174651a5292767cfe2e7))

## [1.5.0](https://www.github.com/googleapis/python-bigtable/compare/v1.4.0...v1.5.0) (2020-09-22)


### Features

* add 'Rowset.add_row_range_with_prefix' ([#30](https://www.github.com/googleapis/python-bigtable/issues/30)) ([4796ac8](https://www.github.com/googleapis/python-bigtable/commit/4796ac85c877d75ed596cde7628dae31918ef726))
* add response status to DirectRow.commit() ([#128](https://www.github.com/googleapis/python-bigtable/issues/128)) ([2478bb8](https://www.github.com/googleapis/python-bigtable/commit/2478bb864adbc71ef606e2b10b3bdfe3a7d44717)), closes [#127](https://www.github.com/googleapis/python-bigtable/issues/127)
* pass 'client_options' to base class ctor ([#104](https://www.github.com/googleapis/python-bigtable/issues/104)) ([e55ca07](https://www.github.com/googleapis/python-bigtable/commit/e55ca07561f9c946276f3bde599e69947769f560)), closes [#69](https://www.github.com/googleapis/python-bigtable/issues/69)


### Bug Fixes

* pass timeout to 'PartialRowsData.response_iterator' ([#16](https://www.github.com/googleapis/python-bigtable/issues/16)) ([8f76434](https://www.github.com/googleapis/python-bigtable/commit/8f764343e01d50ad880363f5a4e5630122cbdb25))
* retry if failure occurs on initial call in MutateRows ([#123](https://www.github.com/googleapis/python-bigtable/issues/123)) ([0c9cde8](https://www.github.com/googleapis/python-bigtable/commit/0c9cde8ade0e4f50d06bbbd1b4169ae5c545b2c0))
* **python_samples:** README link fix, enforce samples=True ([#114](https://www.github.com/googleapis/python-bigtable/issues/114)) ([dfe658a](https://www.github.com/googleapis/python-bigtable/commit/dfe658a2b1270eda7a8a084aca28d65b3297a04f))


### Documentation

* add sample for writing data with Beam ([#80](https://www.github.com/googleapis/python-bigtable/issues/80)) ([6900290](https://www.github.com/googleapis/python-bigtable/commit/6900290e00daf04ca545284b3f0a591a2de11136))
* clarify 'Table.read_rows' snippet ([#50](https://www.github.com/googleapis/python-bigtable/issues/50)) ([5ca8bbd](https://www.github.com/googleapis/python-bigtable/commit/5ca8bbd0fb9c4a7cef7b4cbb67d1ba9f2382f2d8))
* document 'row_set' module explicitly ([#29](https://www.github.com/googleapis/python-bigtable/issues/29)) ([0e0291e](https://www.github.com/googleapis/python-bigtable/commit/0e0291e56cbaeec00ede5275e17af2968a12251c))
* Pysamples new readme gen ([#112](https://www.github.com/googleapis/python-bigtable/issues/112)) ([3ecca7a](https://www.github.com/googleapis/python-bigtable/commit/3ecca7a7b52b0f4fc38db5c5016622b994c1a8aa))
* remove indent from snippet code blocks ([#49](https://www.github.com/googleapis/python-bigtable/issues/49)) ([1fbadf9](https://www.github.com/googleapis/python-bigtable/commit/1fbadf906204c622b9cff3fa073d8fc43d3597f7))
* switch links to client documentation ([#93](https://www.github.com/googleapis/python-bigtable/issues/93)) ([2c973e6](https://www.github.com/googleapis/python-bigtable/commit/2c973e6cce969e7003be0b3d7a164bdc61b91ef1))
* update docs build (via synth) ([#99](https://www.github.com/googleapis/python-bigtable/issues/99)) ([c301b53](https://www.github.com/googleapis/python-bigtable/commit/c301b53db4f7d48fd76548a5cd3a01cc46ff1522)), closes [#700](https://www.github.com/googleapis/python-bigtable/issues/700)
* update links to reflect new Github org ([#48](https://www.github.com/googleapis/python-bigtable/issues/48)) ([9bb11ed](https://www.github.com/googleapis/python-bigtable/commit/9bb11edc885958286b5b31fa18cfd0db95338cb4))
* use correct storage type constant in docstrings ([#110](https://www.github.com/googleapis/python-bigtable/issues/110)) ([bc6db77](https://www.github.com/googleapis/python-bigtable/commit/bc6db77809a89fd6f3b2095cfe9b84d2da1bf304))
* **samples:** filter cpu query to get metrics for the correct resources [([#4238](https://www.github.com/googleapis/python-bigtable/issues/4238))](https://github.com/GoogleCloudPlatform/python-docs-samples/issues/4238) ([#81](https://www.github.com/googleapis/python-bigtable/issues/81)) ([2c8c386](https://www.github.com/googleapis/python-bigtable/commit/2c8c3864c43a7ac9c85a0cd7c9cd4eec7434b42d))

## [1.4.0](https://www.github.com/googleapis/python-bigtable/compare/v1.3.0...v1.4.0) (2020-07-21)


### Features

* **bigtable:** Managed Backups wrappers ([#57](https://www.github.com/googleapis/python-bigtable/issues/57)) ([a351734](https://www.github.com/googleapis/python-bigtable/commit/a351734ae16b4a689b89e6a42f63ea3ea5ad84ca))

## [1.3.0](https://www.github.com/googleapis/python-bigtable/compare/v1.2.1...v1.3.0) (2020-07-16)


### Features

* **api_core:** support version 3 policy bindings ([#9869](https://www.github.com/googleapis/python-bigtable/issues/9869)) ([a9dee32](https://www.github.com/googleapis/python-bigtable/commit/a9dee327ab39e22a014b3c4126f1c9d1beebe2d1))
* **bigtable:** add py2 deprecation warnings; standardize use of 'required' in docstrings (via synth) ([#10064](https://www.github.com/googleapis/python-bigtable/issues/10064)) ([5460de0](https://www.github.com/googleapis/python-bigtable/commit/5460de0f7e0d936a23289f679c2b1a3040a21247))
* Create CODEOWNERS ([#27](https://www.github.com/googleapis/python-bigtable/issues/27)) ([2b63746](https://www.github.com/googleapis/python-bigtable/commit/2b6374600d911b3dfd567eafd964260eb00a2bc0))
* **bigtable:** skip system tests failing with emulator ([#18](https://www.github.com/googleapis/python-bigtable/issues/18)) ([399d3d3](https://www.github.com/googleapis/python-bigtable/commit/399d3d3f960786f616ab6085f142a9703b0391e0))
* **bigtable:** support requested_policy_version for Instance IAM ([#10001](https://www.github.com/googleapis/python-bigtable/issues/10001)) ([7e5d963](https://www.github.com/googleapis/python-bigtable/commit/7e5d963857fd8f7547778d5247b53c24de7a43f6)), closes [#3](https://www.github.com/googleapis/python-bigtable/issues/3)
* update gapic-generator and go microgen, backups generated api ([#55](https://www.github.com/googleapis/python-bigtable/issues/55)) ([c38888d](https://www.github.com/googleapis/python-bigtable/commit/c38888de3d0b1c49c438a7d350f42bc1805809f2))


### Bug Fixes

* localdeps ([5d799b2](https://www.github.com/googleapis/python-bigtable/commit/5d799b2d99e79ee9d20ae6cf2663d670493a8db3))
* test_utils ([43481a9](https://www.github.com/googleapis/python-bigtable/commit/43481a91275e93fadd22eaa7cba3891a00cb97f8))
* **python:** change autodoc_default_flags to autodoc_default_options ([#58](https://www.github.com/googleapis/python-bigtable/issues/58)) ([5c1d618](https://www.github.com/googleapis/python-bigtable/commit/5c1d61827618d254c453b3871c0022a8d35bfbb2))


### Documentation

* add note about multiprocessing usage ([#26](https://www.github.com/googleapis/python-bigtable/issues/26)) ([1449589](https://www.github.com/googleapis/python-bigtable/commit/1449589e8b5b9037dae4e9b071ff7e7662992e18))
* **bigtable:** clean up ([#32](https://www.github.com/googleapis/python-bigtable/issues/32)) ([9f4068c](https://www.github.com/googleapis/python-bigtable/commit/9f4068cf8eb4351c02a4862380547ecf2564d838))
* add samples from bigtable ([#38](https://www.github.com/googleapis/python-bigtable/issues/38)) ([1121f0d](https://www.github.com/googleapis/python-bigtable/commit/1121f0d647dbfc6c70a459b0979465803fdfad7b)), closes [#371](https://www.github.com/googleapis/python-bigtable/issues/371) [#383](https://www.github.com/googleapis/python-bigtable/issues/383) [#383](https://www.github.com/googleapis/python-bigtable/issues/383) [#456](https://www.github.com/googleapis/python-bigtable/issues/456) [#456](https://www.github.com/googleapis/python-bigtable/issues/456) [#540](https://www.github.com/googleapis/python-bigtable/issues/540) [#540](https://www.github.com/googleapis/python-bigtable/issues/540) [#542](https://www.github.com/googleapis/python-bigtable/issues/542) [#542](https://www.github.com/googleapis/python-bigtable/issues/542) [#544](https://www.github.com/googleapis/python-bigtable/issues/544) [#544](https://www.github.com/googleapis/python-bigtable/issues/544) [#576](https://www.github.com/googleapis/python-bigtable/issues/576) [#599](https://www.github.com/googleapis/python-bigtable/issues/599) [#599](https://www.github.com/googleapis/python-bigtable/issues/599) [#656](https://www.github.com/googleapis/python-bigtable/issues/656) [#715](https://www.github.com/googleapis/python-bigtable/issues/715) [#715](https://www.github.com/googleapis/python-bigtable/issues/715) [#781](https://www.github.com/googleapis/python-bigtable/issues/781) [#781](https://www.github.com/googleapis/python-bigtable/issues/781) [#887](https://www.github.com/googleapis/python-bigtable/issues/887) [#887](https://www.github.com/googleapis/python-bigtable/issues/887) [#914](https://www.github.com/googleapis/python-bigtable/issues/914) [#914](https://www.github.com/googleapis/python-bigtable/issues/914) [#922](https://www.github.com/googleapis/python-bigtable/issues/922) [#922](https://www.github.com/googleapis/python-bigtable/issues/922) [#962](https://www.github.com/googleapis/python-bigtable/issues/962) [#962](https://www.github.com/googleapis/python-bigtable/issues/962) [#1004](https://www.github.com/googleapis/python-bigtable/issues/1004) [#1004](https://www.github.com/googleapis/python-bigtable/issues/1004) [#1003](https://www.github.com/googleapis/python-bigtable/issues/1003) [#1005](https://www.github.com/googleapis/python-bigtable/issues/1005) [#1005](https://www.github.com/googleapis/python-bigtable/issues/1005) [#1028](https://www.github.com/googleapis/python-bigtable/issues/1028) [#1055](https://www.github.com/googleapis/python-bigtable/issues/1055) [#1055](https://www.github.com/googleapis/python-bigtable/issues/1055) [#1055](https://www.github.com/googleapis/python-bigtable/issues/1055) [#1057](https://www.github.com/googleapis/python-bigtable/issues/1057) [#1093](https://www.github.com/googleapis/python-bigtable/issues/1093) [#1093](https://www.github.com/googleapis/python-bigtable/issues/1093) [#1093](https://www.github.com/googleapis/python-bigtable/issues/1093) [#1094](https://www.github.com/googleapis/python-bigtable/issues/1094) [#1094](https://www.github.com/googleapis/python-bigtable/issues/1094) [#1121](https://www.github.com/googleapis/python-bigtable/issues/1121) [#1121](https://www.github.com/googleapis/python-bigtable/issues/1121) [#1121](https://www.github.com/googleapis/python-bigtable/issues/1121) [#1156](https://www.github.com/googleapis/python-bigtable/issues/1156) [#1158](https://www.github.com/googleapis/python-bigtable/issues/1158) [#1158](https://www.github.com/googleapis/python-bigtable/issues/1158) [#1158](https://www.github.com/googleapis/python-bigtable/issues/1158) [#1186](https://www.github.com/googleapis/python-bigtable/issues/1186) [#1186](https://www.github.com/googleapis/python-bigtable/issues/1186) [#1186](https://www.github.com/googleapis/python-bigtable/issues/1186) [#1199](https://www.github.com/googleapis/python-bigtable/issues/1199) [#1199](https://www.github.com/googleapis/python-bigtable/issues/1199) [#1199](https://www.github.com/googleapis/python-bigtable/issues/1199) [#1254](https://www.github.com/googleapis/python-bigtable/issues/1254) [#1254](https://www.github.com/googleapis/python-bigtable/issues/1254) [#1254](https://www.github.com/googleapis/python-bigtable/issues/1254) [#1377](https://www.github.com/googleapis/python-bigtable/issues/1377) [#1377](https://www.github.com/googleapis/python-bigtable/issues/1377) [#1377](https://www.github.com/googleapis/python-bigtable/issues/1377) [#1441](https://www.github.com/googleapis/python-bigtable/issues/1441) [#1441](https://www.github.com/googleapis/python-bigtable/issues/1441) [#1441](https://www.github.com/googleapis/python-bigtable/issues/1441) [#1464](https://www.github.com/googleapis/python-bigtable/issues/1464) [#1464](https://www.github.com/googleapis/python-bigtable/issues/1464) [#1464](https://www.github.com/googleapis/python-bigtable/issues/1464) [#1549](https://www.github.com/googleapis/python-bigtable/issues/1549) [#1562](https://www.github.com/googleapis/python-bigtable/issues/1562) [#1555](https://www.github.com/googleapis/python-bigtable/issues/1555) [#1616](https://www.github.com/googleapis/python-bigtable/issues/1616) [#1616](https://www.github.com/googleapis/python-bigtable/issues/1616) [#1665](https://www.github.com/googleapis/python-bigtable/issues/1665) [#1670](https://www.github.com/googleapis/python-bigtable/issues/1670) [#1664](https://www.github.com/googleapis/python-bigtable/issues/1664) [#1674](https://www.github.com/googleapis/python-bigtable/issues/1674) [#1755](https://www.github.com/googleapis/python-bigtable/issues/1755) [#1755](https://www.github.com/googleapis/python-bigtable/issues/1755) [#1755](https://www.github.com/googleapis/python-bigtable/issues/1755) [#1764](https://www.github.com/googleapis/python-bigtable/issues/1764) [#1764](https://www.github.com/googleapis/python-bigtable/issues/1764) [#1770](https://www.github.com/googleapis/python-bigtable/issues/1770) [#1794](https://www.github.com/googleapis/python-bigtable/issues/1794) [#1846](https://www.github.com/googleapis/python-bigtable/issues/1846) [#1846](https://www.github.com/googleapis/python-bigtable/issues/1846) [#1846](https://www.github.com/googleapis/python-bigtable/issues/1846) [#1846](https://www.github.com/googleapis/python-bigtable/issues/1846) [#1846](https://www.github.com/googleapis/python-bigtable/issues/1846) [#1846](https://www.github.com/googleapis/python-bigtable/issues/1846) [#1878](https://www.github.com/googleapis/python-bigtable/issues/1878) [#1890](https://www.github.com/googleapis/python-bigtable/issues/1890) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#1980](https://www.github.com/googleapis/python-bigtable/issues/1980) [#2057](https://www.github.com/googleapis/python-bigtable/issues/2057) [#2057](https://www.github.com/googleapis/python-bigtable/issues/2057) [#2054](https://www.github.com/googleapis/python-bigtable/issues/2054) [#2054](https://www.github.com/googleapis/python-bigtable/issues/2054) [#2018](https://www.github.com/googleapis/python-bigtable/issues/2018) [#2018](https://www.github.com/googleapis/python-bigtable/issues/2018) [#2224](https://www.github.com/googleapis/python-bigtable/issues/2224) [#2201](https://www.github.com/googleapis/python-bigtable/issues/2201) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2436](https://www.github.com/googleapis/python-bigtable/issues/2436) [#2005](https://www.github.com/googleapis/python-bigtable/issues/2005) [#2005](https://www.github.com/googleapis/python-bigtable/issues/2005) [#2005](https://www.github.com/googleapis/python-bigtable/issues/2005) [#2005](https://www.github.com/googleapis/python-bigtable/issues/2005) [#2005](https://www.github.com/googleapis/python-bigtable/issues/2005) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#2692](https://www.github.com/googleapis/python-bigtable/issues/2692) [#3066](https://www.github.com/googleapis/python-bigtable/issues/3066) [#2707](https://www.github.com/googleapis/python-bigtable/issues/2707) [#3103](https://www.github.com/googleapis/python-bigtable/issues/3103) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#2806](https://www.github.com/googleapis/python-bigtable/issues/2806) [#3459](https://www.github.com/googleapis/python-bigtable/issues/3459) [#3494](https://www.github.com/googleapis/python-bigtable/issues/3494) [#3070](https://www.github.com/googleapis/python-bigtable/issues/3070) [#3119](https://www.github.com/googleapis/python-bigtable/issues/3119) [#3738](https://www.github.com/googleapis/python-bigtable/issues/3738) [#3738](https://www.github.com/googleapis/python-bigtable/issues/3738) [#3738](https://www.github.com/googleapis/python-bigtable/issues/3738) [#3739](https://www.github.com/googleapis/python-bigtable/issues/3739) [#3739](https://www.github.com/googleapis/python-bigtable/issues/3739) [#3740](https://www.github.com/googleapis/python-bigtable/issues/3740) [#3783](https://www.github.com/googleapis/python-bigtable/issues/3783) [#3877](https://www.github.com/googleapis/python-bigtable/issues/3877)
* **bigtable:** fix incorrect display_name update ([#46](https://www.github.com/googleapis/python-bigtable/issues/46)) ([1ac60be](https://www.github.com/googleapis/python-bigtable/commit/1ac60be05521b69c924118d40f88e07728a2f75e))
* **bigtable:** remove missing argument from instance declaration ([#47](https://www.github.com/googleapis/python-bigtable/issues/47)) ([c966647](https://www.github.com/googleapis/python-bigtable/commit/c9666475dc31d581fdac0fc1c65e75ee9e27d832)), closes [#42](https://www.github.com/googleapis/python-bigtable/issues/42)

## 1.2.1

01-03-2020 10:05 PST


### Implementation Changes
- Add ability to use single-row transactions ([#10021](https://github.com/googleapis/google-cloud-python/pull/10021))

## 1.2.0

12-04-2019 12:21 PST


### New Features
- add table level IAM policy controls ([#9877](https://github.com/googleapis/google-cloud-python/pull/9877))
- add 'client_options' / 'admin_client_options' to Client ([#9517](https://github.com/googleapis/google-cloud-python/pull/9517))

### Documentation
- change spacing in docs templates (via synth) ([#9739](https://github.com/googleapis/google-cloud-python/pull/9739))
- add python 2 sunset banner to documentation ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))

### Internal
- add trailing commas (via synth) ([#9557](https://github.com/googleapis/google-cloud-python/pull/9557))

## 1.1.0

10-15-2019 06:40 PDT


### New Features
- Add IAM Policy methods to table admin client (via synth). ([#9172](https://github.com/googleapis/google-cloud-python/pull/9172))

### Dependencies
- Pin 'google-cloud-core >= 1.0.3, < 2.0.0dev'. ([#9445](https://github.com/googleapis/google-cloud-python/pull/9445))

### Documentation
- Fix intersphinx reference to requests ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Fix misspelling in docs. ([#9184](https://github.com/googleapis/google-cloud-python/pull/9184))

## 1.0.0

08-28-2019 12:49 PDT

### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8979](https://github.com/googleapis/google-cloud-python/pull/8979))

### Documentation
- Avoid creating table in 'list_tables' snippet; harden 'delete_instance' snippet. ([#8879](https://github.com/googleapis/google-cloud-python/pull/8879))
- Add retry for DeadlineExceeded to 'test_bigtable_create_table' snippet. ([#8889](https://github.com/googleapis/google-cloud-python/pull/8889))
- Remove compatability badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))

### Internal / Testing Changes
- Docs: Remove CI for gh-pages, use googleapis.dev for api_core refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))

## 0.34.0

07-30-2019 10:05 PDT


### Implementation Changes
- Pick up changes to GAPIC client configuration (via synth). ([#8724](https://github.com/googleapis/google-cloud-python/pull/8724))
- Add `Cell.__repr__`. ([#8683](https://github.com/googleapis/google-cloud-python/pull/8683))
- Increase timeout for app profile update operation. ([#8417](https://github.com/googleapis/google-cloud-python/pull/8417))

### New Features
- Add methods returning Separate row types to remove confusion around return types of `row.commit`. ([#8662](https://github.com/googleapis/google-cloud-python/pull/8662))
- Add `options_` argument to clients' `get_iam_policy` (via synth). ([#8652](https://github.com/googleapis/google-cloud-python/pull/8652))
-  Add `client_options` support, update list method docstrings (via synth). ([#8500](https://github.com/googleapis/google-cloud-python/pull/8500))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for `grpc-google-iam-v1` to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))
- Allow kwargs to be passed to `create_channel` (via synth). ([#8458](https://github.com/googleapis/google-cloud-python/pull/8458))
- Add `PartialRowsData.cancel`. ([#8176](https://github.com/googleapis/google-cloud-python/pull/8176))

### Documentation
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Add snppets illustrating use of  application profiles. ([#7033](https://github.com/googleapis/google-cloud-python/pull/7033))

### Internal / Testing Changes
- Add nox session `docs` to remaining manual clients. ([#8478](https://github.com/googleapis/google-cloud-python/pull/8478))
- All: Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Force timeout for table creation to 90 seconds (in systests). ([#8450](https://github.com/googleapis/google-cloud-python/pull/8450))
- Plug systest / snippet instance leaks. ([#8416](https://github.com/googleapis/google-cloud-python/pull/8416))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8346](https://github.com/googleapis/google-cloud-python/pull/8346))
- Add disclaimer to auto-generated template files (via synth).  ([#8308](https://github.com/googleapis/google-cloud-python/pull/8308))
- Fix coverage in `types.py` (via synth). ([#8149](https://github.com/googleapis/google-cloud-python/pull/8149))
- Integrate docstring / formatting tweaks (via synth). ([#8138](https://github.com/googleapis/google-cloud-python/pull/8138))
- Use alabaster theme everwhere. ([#8021](https://github.com/googleapis/google-cloud-python/pull/8021))

## 0.33.0

05-16-2019 11:51 PDT


### Implementation Changes
- Fix typos in deprecation warnings. ([#7858](https://github.com/googleapis/google-cloud-python/pull/7858))
- Add deprecation warnings for to-be-removed features. ([#7532](https://github.com/googleapis/google-cloud-python/pull/7532))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Improve `Policy` interchange w/ JSON, gRPC payloads. ([#7378](https://github.com/googleapis/google-cloud-python/pull/7378))

### New Features
- Add support for passing `client_info` to client. ([#7876](https://github.com/googleapis/google-cloud-python/pull/7876)) and ([#7898](https://github.com/googleapis/google-cloud-python/pull/7898))
- Add `Table.mutation_timeout`, allowing override of config timeouts. ([#7424](https://github.com/googleapis/google-cloud-python/pull/7424))

### Dependencies
- Pin `google-cloud-core >= 1.0.0, < 2.0dev`. ([#7993](https://github.com/googleapis/google-cloud-python/pull/7993))

### Documentation
- Remove duplicate snippet tags for Delete cluster. ([#7860](https://github.com/googleapis/google-cloud-python/pull/7860))
- Fix rendering of instance admin snippets. ([#7797](https://github.com/googleapis/google-cloud-python/pull/7797))
- Avoid leaking instances from snippets. ([#7800](https://github.com/googleapis/google-cloud-python/pull/7800))
- Fix enum reference in documentation. ([#7724](https://github.com/googleapis/google-cloud-python/pull/7724))
- Remove duplicate snippets. ([#7528](https://github.com/googleapis/google-cloud-python/pull/7528))
- Add snippeds for Batcher, RowData, Row Operations, AppendRow. ([#7019](https://github.com/googleapis/google-cloud-python/pull/7019))
- Add column family snippets. ([#7014](https://github.com/googleapis/google-cloud-python/pull/7014))
- Add Row Set snippets. ([#7016](https://github.com/googleapis/google-cloud-python/pull/7016))
- Update client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Fix typos in Table docstrings. ([#7261](https://github.com/googleapis/google-cloud-python/pull/7261))
- Update copyright headers (via synth). ([#7139](https://github.com/googleapis/google-cloud-python/pull/7139))
- Fix linked classes in generated docstrings (via synth). ([#7060](https://github.com/googleapis/google-cloud-python/pull/7060))

### Internal / Testing Changes
- Run `instance_admin` system tests on a separate instance from `table_admin` and `data` system tests. ([#6579](https://github.com/googleapis/google-cloud-python/pull/6579))
- Re-blacken. ([#7462](https://github.com/googleapis/google-cloud-python/pull/7462))
- Copy lintified proto files (via synth). ([#7445](https://github.com/googleapis/google-cloud-python/pull/7445))
- Remove unused message exports (via synth). ([#7264](https://github.com/googleapis/google-cloud-python/pull/7264))
- Compare 0 using '!=', rather than 'is not'. ([#7312](https://github.com/googleapis/google-cloud-python/pull/7312))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Protoc-generated serialization update. ([#7077](https://github.com/googleapis/google-cloud-python/pull/7077))
- Blacken snippets. ([#7048](https://github.com/googleapis/google-cloud-python/pull/7048))
- Bigtable client snippets ([#7020](https://github.com/googleapis/google-cloud-python/pull/7020))
- Pick up order-of-enum fix from GAPIC generator. ([#6879](https://github.com/googleapis/google-cloud-python/pull/6879))
- Plug systest instance leaks ([#7004](https://github.com/googleapis/google-cloud-python/pull/7004))

## 0.32.1

12-17-2018 16:38 PST


### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Add snippets for table operations. ([#6484](https://github.com/googleapis/google-cloud-python/pull/6484))

## 0.32.0

12-10-2018 12:47 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Remove `deepcopy` from `PartialRowData.cells` property. ([#6648](https://github.com/googleapis/google-cloud-python/pull/6648))
- Pick up fixes to GAPIC generator. ([#6630](https://github.com/googleapis/google-cloud-python/pull/6630))

### Dependencies
- Update dependency to google-cloud-core ([#6835](https://github.com/googleapis/google-cloud-python/pull/6835))

### Internal / Testing Changes
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Blackening Continued... ([#6667](https://github.com/googleapis/google-cloud-python/pull/6667))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))

## 0.31.1

11-02-2018 08:13 PDT

### Implementation Changes
- Fix anonymous usage under Bigtable emulator ([#6385](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6385))
- Support `DirectRow` without a `Table` ([#6336](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6336))
- Add retry parameter to `Table.read_rows()`. ([#6281](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6281))
- Fix `ConditionalRow` interaction with `check_and_mutate_row` ([#6296](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6296))
- Deprecate `channel` arg to `Client` ([#6279](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6279))

### Dependencies
- Update dependency: `google-api-core >= 1.4.1` ([#6391](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6391))
- Update IAM version in dependencies ([#6362](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6362))

### Documentation
- Add `docs/snippets.py` and test ([#6012](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6012))
- Normalize use of support level badges ([#6159](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6159))

### Internal / Testing Changes
- Fix client_info bug, update docstrings and timeouts. ([#6406)](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6406))
- Remove now-spurious fixup from 'synth.py'. ([#6400](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6400))
- Fix flaky systests / snippets ([#6367](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6367))
- Add explicit coverage for `row_data._retry_read_rows_exception`. ([#6364](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6364))
- Fix instance IAM test methods ([#6343](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6343))
- Fix error from new flake8 version. ([#6309](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6309))
- Use new Nox ([#6175](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6175))

## 0.31.0

### New Features
- Upgrade support level from `alpha` to `beta`.  ([#6129](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6129))

### Implementation Changes
- Improve admin operation timeouts. ([#6010](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6010))

### Documentation
- Prepare docs for repo split. ([#6014](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6014))

### Internal / Testing Changes
- Refactor `read_row` to call `read_rows` ([#6137](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6102))
- Harden instance teardown against '429 Too Many Requests'. ([#6102](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6102))
- Add `{RowSet,RowRange}.{__eq__,.__ne__}` ([#6025](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6025))
- Regenerate low-level GAPIC code ([#6036](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/6036))

## 0.30.2

### New Features
- Add iam policy implementation for an instance. (#5838)

### Implementation Changes
- Fix smart retries for 'read_rows()' when reading the full table (#5966)

### Documentation
- Replace links to `/stable/` with `/latest/`. (#5901)

### Internal / Testing Changes
- Re-generate library using bigtable/synth.py (#5974)
- Refactor `read_rows` infrastructure (#5963)

## 0.30.1

### Implementation changes

- Fix non-admin access to table data. (#5875)
- Synth bigtable and bigtable admin GAPIC clients. (#5867)

### Testing and internal changes

- Nox: use in-place installs for local packages. (#5865)

## 0.30.0

### New Features

- Improve performance and capabilities of reads.  `read_rows` now returns a generator; has automatic retries; and can read an arbitrary set of keys and ranges
  - Consolidate read_rows and yield_rows (#5840)
  - Implement row set for yield_rows  (#5506)
  - Improve read rows validation performance (#5390)
  - Add retry for yield_rows (#4882)
  - Require TimestampRanges to be milliseconds granularity (#5002)
  - Provide better access to cell values (#4908)
  - Add data app profile id  (#5369)

- Improve writes: Writes are usable in Beam
  - Create MutationBatcher for bigtable (#5651)
  - Allow DirectRow to be created without a table (#5567)
  - Add data app profile id  (#5369)

- Improve table admin: Table creation now can also create families in a single RPC.  Add an `exist()` method.  Add `get_cluster_states` for information about replication
  - Add 'Table.get_cluster_states' method (#5790)
  - Optimize 'Table.exists' performance (#5749)
  - Add column creation in 'Table.create()'. (#5576)
  - Add 'Table.exists' method (#5545)
  - Add split keys on create table - v2 (#5513)
  - Avoid sharing table names across unrelated systests. (#5421)
  - Add truncate table and drop by prefix on top of GAPIC integration (#5360)

- Improve instance admin: Instance creation allows for the creation of multiple clusters.  Instance label management is now enabled.  
  - Create app_profile_object (#5782)
  - Add 'Instance.exists' method (#5802)
  - Add 'InstanceAdminClient.list_clusters' method (#5715)
  - Add 'Instance._state' property (#5736)
  - Convert 'instance.labels' to return a dictionary (#5728)
  - Reshape cluster.py, adding cluster() factory to instance.py (#5663)
  - Convert 'Instance.update' to use 'instance.partial_instance_update' API (#5643)
  - Refactor 'InstanceAdminClient.update_app_profile' to remove update_mask argument (#5684)
  - Add the ability to create an instance with multiple clusters (#5622)
  - Add 'instance_type', 'labels' to 'Instance' ctor (#5614)
  - Add optional app profile to 'Instance.table' (#5605)
  - Clean up Instance creation. (#5542)
  - Make 'InstanceAdminClient.list_instances' return actual instance objects, not protos. (#5420)
  - Add admin app profile methods on Instance (#5315)

### Internal / Testing Changes
- Rename releases to changelog and include from CHANGELOG.md (#5191)
- Fix bad trove classifier
- Integrate new generated low-level client (#5178)
- Override gRPC max message lengths. (#5498)
- Use client properties rather than private attrs (#5398)
- Fix the broken Bigtable system test. (#5607)
- Fix Py3 breakage in new system test. (#5474)
- Modify system test for new GAPIC code (#5302)
- Add Test runs for Python 3.7 and remove 3.4 (#5295)
- Disable Bigtable system tests (#5381)
- Modify system tests to use prerelease versions of grpcio (#5304)
- Pass through 'session.posargs' when running Bigtable system tests. (#5418)
- Harden 'test_list_instances' against simultaneous test runs. (#5476)
- Shorten instance / cluster name to fix CI breakage. (#5641)
- Fix failing systest: 'test_create_instance_w_two_clusters'. (#5836)
- Add labels {'python-system': ISO-timestamp} to systest instances (#5729)
- Shorten cluster ID in system test (#5719)
- Harden 'test_list_instances' further. (#5696)
- Improve testing of create instance (#5544)

## 0.29.0

### New features

- Use `api_core.retry` for `mutate_row` (#4665, #4341)
- Added a row generator on a table. (#4679)

### Implementation changes

- Remove gax usage from BigTable (#4873)
- BigTable: Cell.from_pb() performance improvement (#4745)

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Documentation

- Minor typo (#4758)
- Row filter end points documentation error (#4667)
- Removing "rename" from bigtable table.py comments (#4526)
- Small docs/hygiene tweaks after #4256. (#4333)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)
- Timestamp system test fix (#4765)

## 0.28.1

### Implementation Changes

- Bugfix: Distinguish between an unset column qualifier and an empty string
  column qualifier while parsing a `ReadRows` response (#4252)

### Features added

- Add a ``retry`` strategy that will be used for retry-able errors
  in ``Table.mutate_rows``. This will be used for gRPC errors of type
  ``ABORTED``, ``DEADLINE_EXCEEDED`` and ``SERVICE_UNAVAILABLE``. (#4256)

PyPI: https://pypi.org/project/google-cloud-bigtable/0.28.1/

## 0.28.0

### Documentation

- Fixed referenced types in `Table.row` docstring (#3934, h/t to
  @MichaelTamm)
- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)

PyPI: https://pypi.org/project/google-cloud-bigtable/0.28.0/
