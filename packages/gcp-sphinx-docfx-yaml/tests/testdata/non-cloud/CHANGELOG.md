# Changelog

## [0.19.1](https://github.com/googleapis/python-bigquery-pandas/compare/v0.19.0...v0.19.1) (2023-01-25)


### Documentation

* Updates the user instructions re OAuth ([0c2b716](https://github.com/googleapis/python-bigquery-pandas/commit/0c2b716a55551f26050ed8d94ff912d406527ac5))

## [0.19.0](https://github.com/googleapis/python-bigquery-pandas/compare/v0.18.1...v0.19.0) (2023-01-11)


### Features

* Adds ability to provide redirect uri ([#595](https://github.com/googleapis/python-bigquery-pandas/issues/595)) ([a06085e](https://github.com/googleapis/python-bigquery-pandas/commit/a06085eddddd18394f623d0b6f3a65d91f51e979))

## [0.18.1](https://github.com/googleapis/python-bigquery-pandas/compare/v0.18.0...v0.18.1) (2022-11-28)


### Dependencies

* Remove upper bound for python and pyarrow ([#592](https://github.com/googleapis/python-bigquery-pandas/issues/592)) ([4d28684](https://github.com/googleapis/python-bigquery-pandas/commit/4d286840feaa8290f4d674dce1c269e7e09980d5))

## [0.18.0](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.9...v0.18.0) (2022-11-19)


### Features

* Map "if_exists" value to LoadJobConfig.WriteDisposition ([#583](https://github.com/googleapis/python-bigquery-pandas/issues/583)) ([7389cd2](https://github.com/googleapis/python-bigquery-pandas/commit/7389cd2a363ebf403b66905ca845ca842a754922))

## [0.17.9](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.8...v0.17.9) (2022-09-27)


### Bug Fixes

* Updates requirements.txt to fix failing tests due to missing req ([#575](https://github.com/googleapis/python-bigquery-pandas/issues/575)) ([1d797a3](https://github.com/googleapis/python-bigquery-pandas/commit/1d797a3337e716fa6f3de511e7c8875dfadde43b))

## [0.17.8](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.7...v0.17.8) (2022-08-09)


### Bug Fixes

* **deps:** allow pyarrow < 10 ([#550](https://github.com/googleapis/python-bigquery-pandas/issues/550)) ([c21a414](https://github.com/googleapis/python-bigquery-pandas/commit/c21a41425d4d06b9df5fbdeb15e90f79de841612))

## [0.17.7](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.6...v0.17.7) (2022-07-11)


### Bug Fixes

* allow `to_gbq` to run without `bigquery.tables.create` permission. ([#539](https://github.com/googleapis/python-bigquery-pandas/issues/539)) ([3988306](https://github.com/googleapis/python-bigquery-pandas/commit/3988306bd2cc7743d24e24d753730ba04462f018))

## [0.17.6](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.5...v0.17.6) (2022-06-03)


### Documentation

* fix changelog header to consistent size ([#529](https://github.com/googleapis/python-bigquery-pandas/issues/529)) ([218e06a](https://github.com/googleapis/python-bigquery-pandas/commit/218e06af40e991f870649a8e958dfc1bc46f0ee8))

## [0.17.5](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.4...v0.17.5) (2022-05-09)


### Bug Fixes

* **deps:** allow pyarrow v8 ([#525](https://github.com/googleapis/python-bigquery-pandas/issues/525)) ([a4ee0df](https://github.com/googleapis/python-bigquery-pandas/commit/a4ee0dffae0580a7509d5d6014edb46e05394717))

## [0.17.4](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.3...v0.17.4) (2022-03-14)


### Bug Fixes

* avoid deprecated "out-of-band" authentication flow ([#500](https://github.com/googleapis/python-bigquery-pandas/issues/500)) ([4758e3a](https://github.com/googleapis/python-bigquery-pandas/commit/4758e3a9ccb82109aae65f76258b2910077e02dd))
* correctly transform query job timeout configuration and exceptions ([#492](https://github.com/googleapis/python-bigquery-pandas/issues/492)) ([d8c3900](https://github.com/googleapis/python-bigquery-pandas/commit/d8c3900eda5aa2cb5b663b2be569d639f6a028a9))

## [0.17.3](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.2...v0.17.3) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#493](https://github.com/googleapis/python-bigquery-pandas/issues/493)) ([744a71c](https://github.com/googleapis/python-bigquery-pandas/commit/744a71c3d265d0e9a2ac25ca98dd0fa3ca68af6a))
* **deps:** require google-auth>=1.25.0 ([744a71c](https://github.com/googleapis/python-bigquery-pandas/commit/744a71c3d265d0e9a2ac25ca98dd0fa3ca68af6a))
* **deps:** require proto-plus>=1.15.0 ([744a71c](https://github.com/googleapis/python-bigquery-pandas/commit/744a71c3d265d0e9a2ac25ca98dd0fa3ca68af6a))

## [0.17.2](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.1...v0.17.2) (2022-03-02)


### Dependencies

* allow pyarrow 7.0 ([#487](https://github.com/googleapis/python-bigquery-pandas/issues/487)) ([39441b6](https://github.com/googleapis/python-bigquery-pandas/commit/39441b63fadd95810c535e7079d781e9eec72189))

## [0.17.1](https://github.com/googleapis/python-bigquery-pandas/compare/v0.17.0...v0.17.1) (2022-02-24)


### Bug Fixes

* avoid `TypeError` when executing DML statements with `read_gbq` ([#483](https://github.com/googleapis/python-bigquery-pandas/issues/483)) ([e9f0e3f](https://github.com/googleapis/python-bigquery-pandas/commit/e9f0e3f73f597530b8cf87324b9c4b0b54a79812))


### Documentation

* document additional breaking change in 0.17.0 ([#477](https://github.com/googleapis/python-bigquery-pandas/issues/477)) ([a858c80](https://github.com/googleapis/python-bigquery-pandas/commit/a858c80a37dc94707a41a6d865af2bc91543328a))

## [0.17.0](https://github.com/googleapis/python-bigquery-pandas/compare/v0.16.0...v0.17.0) (2022-01-19)


### ⚠ BREAKING CHANGES

* the first argument of `read_gbq` is renamed from `query` to `query_or_table` ([#443](https://github.com/googleapis/python-bigquery-pandas/issues/443)) ([bf0e863](https://github.com/googleapis/python-bigquery-pandas/commit/bf0e863ff6506eca267b14e59e47417bd60e947f))
* use nullable Int64 and boolean dtypes if available ([#445](https://github.com/googleapis/python-bigquery-pandas/issues/445)) ([89078f8](https://github.com/googleapis/python-bigquery-pandas/commit/89078f89478469aa60a0a8b8e1e0c4a59aa059e0))

### Features

* accepts a table ID, which downloads the table without a query ([#443](https://github.com/googleapis/python-bigquery-pandas/issues/443)) ([bf0e863](https://github.com/googleapis/python-bigquery-pandas/commit/bf0e863ff6506eca267b14e59e47417bd60e947f))
* use nullable Int64 and boolean dtypes if available ([#445](https://github.com/googleapis/python-bigquery-pandas/issues/445)) ([89078f8](https://github.com/googleapis/python-bigquery-pandas/commit/89078f89478469aa60a0a8b8e1e0c4a59aa059e0))


### Bug Fixes

* `read_gbq` supports extreme DATETIME values such as `0001-01-01 00:00:00` ([#444](https://github.com/googleapis/python-bigquery-pandas/issues/444)) ([d120f8f](https://github.com/googleapis/python-bigquery-pandas/commit/d120f8fbdf4541a39ce8d87067523d48f21554bf))
* `to_gbq` allows strings for DATE and floats for NUMERIC with `api_method="load_parquet"` ([#423](https://github.com/googleapis/python-bigquery-pandas/issues/423)) ([2180836](https://github.com/googleapis/python-bigquery-pandas/commit/21808367d02b5b7fcf35b3c7520224c819879aec))
* allow extreme DATE values such as `datetime.date(1, 1, 1)` in `load_gbq` ([#442](https://github.com/googleapis/python-bigquery-pandas/issues/442)) ([e13abaf](https://github.com/googleapis/python-bigquery-pandas/commit/e13abaf015cd1ea9da3ad5063680bf89e18f0fac))
* avoid iteritems deprecation in pandas prerelease ([#469](https://github.com/googleapis/python-bigquery-pandas/issues/469)) ([7379cdc](https://github.com/googleapis/python-bigquery-pandas/commit/7379cdcd7eedcbc751a4002bdf90c12e810e6bcd))
* use data project for destination in `to_gbq` ([#455](https://github.com/googleapis/python-bigquery-pandas/issues/455)) ([891a00c](https://github.com/googleapis/python-bigquery-pandas/commit/891a00c8f202aa476ffb22b2fb92c01ffa84889a))


### Miscellaneous Chores

* release 0.17.0 ([#470](https://github.com/googleapis/python-bigquery-pandas/issues/470)) ([29ac8c3](https://github.com/googleapis/python-bigquery-pandas/commit/29ac8c33127457e86d9864a6979d532cd1d3ae5c))

## [0.16.0](https://www.github.com/googleapis/python-bigquery-pandas/compare/v0.16.0...v0.16.0) (2021-11-08)


### Features

* `to_gbq` uses Parquet by default, use `api_method="load_csv"` for old behavior ([#413](https://www.github.com/googleapis/python-bigquery-pandas/issues/413)) ([9a65383](https://www.github.com/googleapis/python-bigquery-pandas/commit/9a65383916697ff02358aba58df555c85b16350c))
* allow Python 3.10 ([#417](https://www.github.com/googleapis/python-bigquery-pandas/issues/417)) ([faba940](https://www.github.com/googleapis/python-bigquery-pandas/commit/faba940bc19d5c260b9dce3f973a9b729a179d20))


### Miscellaneous Chores

* release 0.16.0 ([#415](https://www.github.com/googleapis/python-bigquery-pandas/issues/415)) ([ea0f4e9](https://www.github.com/googleapis/python-bigquery-pandas/commit/ea0f4e97f3518895e824b1b7328d578081588d84))


### Documentation

* clarify `table_schema` ([#383](https://www.github.com/googleapis/python-bigquery-pandas/issues/383)) ([326e674](https://www.github.com/googleapis/python-bigquery-pandas/commit/326e674a24fc7e057e213596df92f0c4a8225f9e))

## 0.15.0 / 2021-03-30

### Features

-   Load DataFrame with `to_gbq` to a table in a project different from
    the API client project. Specify the target table ID as
    `project.dataset.table` to use this feature.
    ([#321](https://github.com/googleapis/python-bigquery-pandas/issues/321),
    [#347](https://github.com/googleapis/python-bigquery-pandas/issues/347))
-   Allow billing project to be separate from destination table project
    in `to_gbq`.
    ([#321](https://github.com/googleapis/python-bigquery-pandas/issues/321))

### Bug fixes

-   Avoid 403 error from `to_gbq` when table has `policyTags`.
    ([#354](https://github.com/googleapis/python-bigquery-pandas/issues/354))
-   Avoid `client.dataset` deprecation warnings.
    ([#312](https://github.com/googleapis/python-bigquery-pandas/issues/312))

### Dependencies

-   Drop support for Python 3.5 and 3.6.
    ([#337](https://github.com/googleapis/python-bigquery-pandas/issues/337))
-   Drop support for <span
    class="title-ref">google-cloud-bigquery==2.4.\*</span> due to query
    hanging bug.
    ([#343](https://github.com/googleapis/python-bigquery-pandas/issues/343))

## 0.14.1 / 2020-11-10

### Bug fixes

-   Use `object` dtype for `TIME` columns.
    ([#328](https://github.com/googleapis/python-bigquery-pandas/issues/328))
-   Encode floating point values with greater precision.
    ([#326](https://github.com/googleapis/python-bigquery-pandas/issues/326))
-   Support `INT64` and other standard SQL aliases in
    `~pandas_gbq.to_gbq` `table_schema` argument.
    ([#322](https://github.com/googleapis/python-bigquery-pandas/issues/322))

## 0.14.0 / 2020-10-05

-   Add `dtypes` argument to `read_gbq`. Use this argument to override
    the default `dtype` for a particular column in the query results.
    For example, this can be used to select nullable integer columns as
    the `Int64` nullable integer pandas extension type.
    ([#242](https://github.com/googleapis/python-bigquery-pandas/issues/242),
    [#332](https://github.com/googleapis/python-bigquery-pandas/issues/332))

``` python
df = gbq.read_gbq(
    "SELECT CAST(NULL AS INT64) AS null_integer",
    dtypes={"null_integer": "Int64"},
)
```

### Dependency updates

-   Support `google-cloud-bigquery-storage` 2.0 and higher.
    ([#329](https://github.com/googleapis/python-bigquery-pandas/issues/329))
-   Update the minimum version of `pandas` to 0.20.1.
    ([#331](https://github.com/googleapis/python-bigquery-pandas/issues/331))

### Internal changes

-   Update tests to run against Python 3.8.
    ([#331](https://github.com/googleapis/python-bigquery-pandas/issues/331))

## 0.13.3 / 2020-09-30

-   Include needed "extras" from `google-cloud-bigquery` package as
    dependencies. Exclude incompatible 2.0 version.
    ([#324](https://github.com/googleapis/python-bigquery-pandas/issues/324),
    [#329](https://github.com/googleapis/python-bigquery-pandas/issues/329))

## 0.13.2 / 2020-05-14

-   Fix `Provided Schema does not match Table` error when the existing
    table contains required fields.
    ([#315](https://github.com/googleapis/python-bigquery-pandas/issues/315))

## 0.13.1 / 2020-02-13

-   Fix `AttributeError` with BQ Storage API to download empty results.
    ([#299](https://github.com/googleapis/python-bigquery-pandas/issues/299))

## 0.13.0 / 2019-12-12

-   Raise `NotImplementedError` when the deprecated `private_key`
    argument is used.
    ([#301](https://github.com/googleapis/python-bigquery-pandas/issues/301))

## 0.12.0 / 2019-11-25

### New features

-   Add `max_results` argument to `~pandas_gbq.read_gbq()`. Use this
    argument to limit the number of rows in the results DataFrame. Set
    `max_results` to 0 to ignore query outputs, such as for DML or DDL
    queries.
    ([#102](https://github.com/googleapis/python-bigquery-pandas/issues/102))
-   Add `progress_bar_type` argument to `~pandas_gbq.read_gbq()`. Use
    this argument to display a progress bar when downloading data.
    ([#182](https://github.com/googleapis/python-bigquery-pandas/issues/182))

### Bug fixes

-   Fix resource leak with `use_bqstorage_api` by closing BigQuery
    Storage API client after use.
    ([#294](https://github.com/googleapis/python-bigquery-pandas/issues/294))

### Dependency updates

-   Update the minimum version of `google-cloud-bigquery` to 1.11.1.
    ([#296](https://github.com/googleapis/python-bigquery-pandas/issues/296))

### Documentation

-   Add code samples to introduction and refactor howto guides.
    ([#239](https://github.com/googleapis/python-bigquery-pandas/issues/239))

## 0.11.0 / 2019-07-29

-   **Breaking Change:** Python 2 support has been dropped. This is to
    align with the pandas package which dropped Python 2 support at the
    end of 2019.
    ([#268](https://github.com/googleapis/python-bigquery-pandas/issues/268))

### Enhancements

-   Ensure `table_schema` argument is not modified inplace.
    ([#278](https://github.com/googleapis/python-bigquery-pandas/issues/278))

### Implementation changes

-   Use object dtype for `STRING`, `ARRAY`, and `STRUCT` columns when
    there are zero rows.
    ([#285](https://github.com/googleapis/python-bigquery-pandas/issues/285))

### Internal changes

-   Populate `user-agent` with `pandas` version information.
    ([#281](https://github.com/googleapis/python-bigquery-pandas/issues/281))
-   Fix `pytest.raises` usage for latest pytest. Fix warnings in tests.
    ([#282](https://github.com/googleapis/python-bigquery-pandas/issues/282))
-   Update CI to install nightly packages in the conda tests.
    ([#254](https://github.com/googleapis/python-bigquery-pandas/issues/254))

## 0.10.0 / 2019-04-05

-   **Breaking Change:** Default SQL dialect is now `standard`. Use
    `pandas_gbq.context.dialect` to override the default value.
    ([#195](https://github.com/googleapis/python-bigquery-pandas/issues/195),
    [#245](https://github.com/googleapis/python-bigquery-pandas/issues/245))

### Documentation

-   Document `BigQuery data type to pandas dtype conversion
    <reading-dtypes>` for `read_gbq`.
    ([#269](https://github.com/googleapis/python-bigquery-pandas/issues/269))

### Dependency updates

-   Update the minimum version of `google-cloud-bigquery` to 1.9.0.
    ([#247](https://github.com/googleapis/python-bigquery-pandas/issues/247))
-   Update the minimum version of `pandas` to 0.19.0.
    ([#262](https://github.com/googleapis/python-bigquery-pandas/issues/262))

### Internal changes

-   Update the authentication credentials. **Note:** You may need to set
    `reauth=True` in order to update your credentials to the most recent
    version. This is required to use new functionality such as the
    BigQuery Storage API.
    ([#267](https://github.com/googleapis/python-bigquery-pandas/issues/267))
-   Use `to_dataframe()` from `google-cloud-bigquery` in the
    `read_gbq()` function.
    ([#247](https://github.com/googleapis/python-bigquery-pandas/issues/247))

### Enhancements

-   Fix a bug where pandas-gbq could not upload an empty DataFrame.
    ([#237](https://github.com/googleapis/python-bigquery-pandas/issues/237))
-   Allow `table_schema` in `to_gbq` to contain only a subset of
    columns, with the rest being populated using the DataFrame dtypes
    ([#218](https://github.com/googleapis/python-bigquery-pandas/issues/218))
    (contributed by @johnpaton)
-   Read `project_id` in `to_gbq` from provided `credentials` if
    available (contributed by @daureg)
-   `read_gbq` uses the timezone-aware
    `DatetimeTZDtype(unit='ns', tz='UTC')` dtype for BigQuery
    `TIMESTAMP` columns.
    ([#269](https://github.com/googleapis/python-bigquery-pandas/issues/269))
-   Add `use_bqstorage_api` to `read_gbq`. The BigQuery Storage API can
    be used to download large query results (>125 MB) more quickly. If
    the BQ Storage API can't be used, the BigQuery API is used instead.
    ([#133](https://github.com/googleapis/python-bigquery-pandas/issues/133),
    [#270](https://github.com/googleapis/python-bigquery-pandas/issues/270))

## 0.9.0 / 2019-01-11

-   Warn when deprecated `private_key` parameter is used
    ([#240](https://github.com/googleapis/python-bigquery-pandas/issues/240))
-   **New dependency** Use the `pydata-google-auth` package for
    authentication.
    ([#241](https://github.com/googleapis/python-bigquery-pandas/issues/241))

## 0.8.0 / 2018-11-12

### Breaking changes

-   **Deprecate** `private_key` parameter to `pandas_gbq.read_gbq` and
    `pandas_gbq.to_gbq` in favor of new `credentials` argument. Instead,
    create a credentials object using
    `google.oauth2.service_account.Credentials.from_service_account_info`
    or
    `google.oauth2.service_account.Credentials.from_service_account_file`.
    See the `authentication how-to guide <howto/authentication>` for
    examples.
    ([#161](https://github.com/googleapis/python-bigquery-pandas/issues/161),
    [#231](https://github.com/googleapis/python-bigquery-pandas/issues/231))

### Enhancements

-   Allow newlines in data passed to `to_gbq`.
    ([#180](https://github.com/googleapis/python-bigquery-pandas/issues/180))
-   Add `pandas_gbq.context.dialect` to allow overriding the default SQL
    syntax dialect.
    ([#195](https://github.com/googleapis/python-bigquery-pandas/issues/195),
    [#235](https://github.com/googleapis/python-bigquery-pandas/issues/235))
-   Support Python 3.7.
    ([#197](https://github.com/googleapis/python-bigquery-pandas/issues/197),
    [#232](https://github.com/googleapis/python-bigquery-pandas/issues/232))

### Internal changes

-   Migrate tests to CircleCI.
    ([#228](https://github.com/googleapis/python-bigquery-pandas/issues/228),
    [#232](https://github.com/googleapis/python-bigquery-pandas/issues/232))

## 0.7.0 / 2018-10-19

-   <span class="title-ref">int</span> columns which contain <span
    class="title-ref">NULL</span> are now cast to <span
    class="title-ref">float</span>, rather than <span
    class="title-ref">object</span> type.
    ([#174](https://github.com/googleapis/python-bigquery-pandas/issues/174))
-   <span class="title-ref">DATE</span>, <span
    class="title-ref">DATETIME</span> and <span
    class="title-ref">TIMESTAMP</span> columns are now parsed as pandas'
    <span class="title-ref">timestamp</span> objects
    ([#224](https://github.com/googleapis/python-bigquery-pandas/issues/224))
-   Add `pandas_gbq.Context` to cache credentials in-memory, across
    calls to `read_gbq` and `to_gbq`.
    ([#198](https://github.com/googleapis/python-bigquery-pandas/issues/198),
    [#208](https://github.com/googleapis/python-bigquery-pandas/issues/208))
-   Fast queries now do not log above `DEBUG` level.
    ([#204](https://github.com/googleapis/python-bigquery-pandas/issues/204))
    With BigQuery's release of
    [clustering](https://cloud.google.com/bigquery/docs/clustered-tables)
    querying smaller samples of data is now faster and cheaper.
-   Don't load credentials from disk if reauth is `True`.
    ([#212](https://github.com/googleapis/python-bigquery-pandas/issues/212))
    This fixes a bug where pandas-gbq could not refresh credentials if
    the cached credentials were invalid, revoked, or expired, even when
    `reauth=True`.
-   Catch RefreshError when trying credentials.
    ([#226](https://github.com/googleapis/python-bigquery-pandas/issues/226))

### Internal changes

-   Avoid listing datasets and tables in system tests.
    ([#215](https://github.com/googleapis/python-bigquery-pandas/issues/215))
-   Improved performance from eliminating some duplicative parsing steps
    ([#224](https://github.com/googleapis/python-bigquery-pandas/issues/224))

## 0.6.1 / 2018-09-11

-   Improved `read_gbq` performance and memory consumption by delegating
    `DataFrame` construction to the Pandas library, radically reducing
    the number of loops that execute in python
    ([#128](https://github.com/googleapis/python-bigquery-pandas/issues/128))
-   Reduced verbosity of logging from `read_gbq`, particularly for short
    queries.
    ([#201](https://github.com/googleapis/python-bigquery-pandas/issues/201))
-   Avoid `SELECT 1` query when running `to_gbq`.
    ([#202](https://github.com/googleapis/python-bigquery-pandas/issues/202))

## 0.6.0 / 2018-08-15

-   Warn when `dialect` is not passed in to `read_gbq`. The default
    dialect will be changing from 'legacy' to 'standard' in a future
    version.
    ([#195](https://github.com/googleapis/python-bigquery-pandas/issues/195))
-   Use general float with 15 decimal digit precision when writing to
    local CSV buffer in `to_gbq`. This prevents numerical overflow in
    certain edge cases.
    ([#192](https://github.com/googleapis/python-bigquery-pandas/issues/192))

## 0.5.0 / 2018-06-15

-   Project ID parameter is optional in `read_gbq` and `to_gbq` when it
    can inferred from the environment. Note: you must still pass in a
    project ID when using user-based authentication.
    ([#103](https://github.com/googleapis/python-bigquery-pandas/issues/103))
-   Progress bar added for `to_gbq`, through an optional library <span
    class="title-ref">tqdm</span> as dependency.
    ([#162](https://github.com/googleapis/python-bigquery-pandas/issues/162))
-   Add location parameter to `read_gbq` and `to_gbq` so that pandas-gbq
    can work with datasets in the Tokyo region.
    ([#177](https://github.com/googleapis/python-bigquery-pandas/issues/177))

### Documentation

-   Add `authentication how-to guide <howto/authentication>`.
    ([#183](https://github.com/googleapis/python-bigquery-pandas/issues/183))
-   Update `contributing` guide with new paths to tests.
    ([#154](https://github.com/googleapis/python-bigquery-pandas/issues/154),
    [#164](https://github.com/googleapis/python-bigquery-pandas/issues/164))

### Internal changes

-   Tests now use <span class="title-ref">nox</span> to run in multiple
    Python environments.
    ([#52](https://github.com/googleapis/python-bigquery-pandas/issues/52))
-   Renamed internal modules.
    ([#154](https://github.com/googleapis/python-bigquery-pandas/issues/154))
-   Refactored auth to an internal auth module.
    ([#176](https://github.com/googleapis/python-bigquery-pandas/issues/176))
-   Add unit tests for `get_credentials()`.
    ([#184](https://github.com/googleapis/python-bigquery-pandas/issues/184))

## 0.4.1 / 2018-04-05

-   Only show `verbose` deprecation warning if Pandas version does not
    populate it.
    ([#157](https://github.com/googleapis/python-bigquery-pandas/issues/157))

## 0.4.0 / 2018-04-03

-   Fix bug in <span class="title-ref">read_gbq</span> when building a
    dataframe with integer columns on Windows. Explicitly use 64bit
    integers when converting from BQ types.
    ([#119](https://github.com/googleapis/python-bigquery-pandas/issues/119))
-   Fix bug in <span class="title-ref">read_gbq</span> when querying for
    an array of floats
    ([#123](https://github.com/googleapis/python-bigquery-pandas/issues/123))
-   Fix bug in <span class="title-ref">read_gbq</span> with
    configuration argument. Updates <span
    class="title-ref">read_gbq</span> to account for breaking change in
    the way `google-cloud-python` version 0.32.0+ handles query
    configuration API representation.
    ([#152](https://github.com/googleapis/python-bigquery-pandas/issues/152))
-   Fix bug in <span class="title-ref">to_gbq</span> where seconds were
    discarded in timestamp columns.
    ([#148](https://github.com/googleapis/python-bigquery-pandas/issues/148))
-   Fix bug in <span class="title-ref">to_gbq</span> when supplying a
    user-defined schema
    ([#150](https://github.com/googleapis/python-bigquery-pandas/issues/150))
-   **Deprecate** the `verbose` parameter in <span
    class="title-ref">read_gbq</span> and <span
    class="title-ref">to_gbq</span>. Messages use the logging module
    instead of printing progress directly to standard output.
    ([#12](https://github.com/googleapis/python-bigquery-pandas/issues/12))

## 0.3.1 / 2018-02-13

-   Fix an issue where Unicode couldn't be uploaded in Python 2
    ([#106](https://github.com/googleapis/python-bigquery-pandas/issues/106))
-   Add support for a passed schema in `` `to_gbq ``<span
    class="title-ref"> instead inferring the schema from the passed
    </span><span class="title-ref">DataFrame</span><span
    class="title-ref"> with </span><span
    class="title-ref">DataFrame.dtypes</span><span class="title-ref">
    (</span>#46
    \<<https://github.com/googleapis/python-bigquery-pandas/issues/46>\>\`\_)
-   Fix an issue where a dataframe containing both integer and floating
    point columns could not be uploaded with `to_gbq`
    ([#116](https://github.com/googleapis/python-bigquery-pandas/issues/116))
-   `to_gbq` now uses `to_csv` to avoid manually looping over rows in a
    dataframe (should result in faster table uploads)
    ([#96](https://github.com/googleapis/python-bigquery-pandas/issues/96))

## 0.3.0 / 2018-01-03

-   Use the
    [google-cloud-bigquery](https://googlecloudplatform.github.io/google-cloud-python/latest/bigquery/usage.html)
    library for API calls. The `google-cloud-bigquery` package is a new
    dependency, and dependencies on `google-api-python-client` and
    `httplib2` are removed. See the [installation
    guide](https://pandas-gbq.readthedocs.io/en/latest/install.html#dependencies)
    for more details.
    ([#93](https://github.com/googleapis/python-bigquery-pandas/issues/93))
-   Structs and arrays are now named properly
    ([#23](https://github.com/googleapis/python-bigquery-pandas/issues/23))
    and BigQuery functions like `array_agg` no longer run into errors
    during type conversion
    ([#22](https://github.com/googleapis/python-bigquery-pandas/issues/22)).
-   `to_gbq` now uses a load job instead of the streaming API. Remove
    `StreamingInsertError` class, as it is no longer used by `to_gbq`.
    ([#7](https://github.com/googleapis/python-bigquery-pandas/issues/7),
    [#75](https://github.com/googleapis/python-bigquery-pandas/issues/75))

## 0.2.1 / 2017-11-27

-   `read_gbq` now raises `QueryTimeout` if the request exceeds the
    `query.timeoutMs` value specified in the BigQuery configuration.
    ([#76](https://github.com/googleapis/python-bigquery-pandas/issues/76))
-   Environment variable `PANDAS_GBQ_CREDENTIALS_FILE` can now be used
    to override the default location where the BigQuery user account
    credentials are stored.
    ([#86](https://github.com/googleapis/python-bigquery-pandas/issues/86))
-   BigQuery user account credentials are now stored in an
    application-specific hidden user folder on the operating system.
    ([#41](https://github.com/googleapis/python-bigquery-pandas/issues/41))

## 0.2.0 / 2017-07-24

-   Drop support for Python 3.4
    ([#40](https://github.com/googleapis/python-bigquery-pandas/issues/40))
-   The dataframe passed to
    `` `.to_gbq(...., if_exists='append') ``<span class="title-ref">
    needs to contain only a subset of the fields in the BigQuery schema.
    (</span>#24
    \<<https://github.com/googleapis/python-bigquery-pandas/issues/24>\>\`\_)
-   Use the [google-auth](https://google-auth.readthedocs.io/en/latest/)
    library for authentication because `oauth2client` is deprecated.
    ([#39](https://github.com/googleapis/python-bigquery-pandas/issues/39))
-   `read_gbq` now has a `auth_local_webserver` boolean argument for
    controlling whether to use web server or console flow when getting
    user credentials. Replaces <span
    class="title-ref">--noauth_local_webserver</span> command line
    argument.
    ([#35](https://github.com/googleapis/python-bigquery-pandas/issues/35))
-   `read_gbq` now displays the BigQuery Job ID and standard price in
    verbose output.
    ([#70](https://github.com/googleapis/python-bigquery-pandas/issues/70)
    and
    [#71](https://github.com/googleapis/python-bigquery-pandas/issues/71))

## 0.1.6 / 2017-05-03

-   All gbq errors will simply be subclasses of `ValueError` and no
    longer inherit from the deprecated `PandasError`.

## 0.1.4 / 2017-03-17

-   `InvalidIndexColumn` will be raised instead of `InvalidColumnOrder`
    in `read_gbq` when the index column specified does not exist in the
    BigQuery schema.
    ([#6](https://github.com/googleapis/python-bigquery-pandas/issues/6))

## 0.1.3 / 2017-03-04

-   Bug with appending to a BigQuery table where fields have modes
    (NULLABLE,REQUIRED,REPEATED) specified. These modes were compared
    versus the remote schema and writing a table via `to_gbq` would
    previously raise.
    ([#13](https://github.com/googleapis/python-bigquery-pandas/issues/13))

## 0.1.2 / 2017-02-23

Initial release of transfered code from
[pandas](https://github.com/pandas-dev/pandas)

Includes patches since the 0.19.2 release on pandas with the following:

-   `read_gbq` now allows query configuration preferences
    [pandas-GH#14742](https://github.com/pandas-dev/pandas/pull/14742)
-   `read_gbq` now stores `INTEGER` columns as `dtype=object` if they
    contain `NULL` values. Otherwise they are stored as `int64`. This
    prevents precision lost for integers greather than 2\**53.
    Furthermore \`\`FLOAT\`\` columns with values above 10*\*4 are no
    longer casted to `int64` which also caused precision loss
    [pandas-GH#14064](https://github.com/pandas-dev/pandas/pull/14064),
    and
    [pandas-GH#14305](https://github.com/pandas-dev/pandas/pull/14305)
