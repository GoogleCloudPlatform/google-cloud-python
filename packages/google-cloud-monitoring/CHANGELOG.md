# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-monitoring/#history

## [2.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.31.0...google-cloud-monitoring-v2.32.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [2.31.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.30.0...google-cloud-monitoring-v2.31.0) (2026-06-02)


### Features

* regenerate monitoring using generator v1.32.0 (#17165) ([042dc5c369138ca0d3c957c3234561aafa6bde78](https://github.com/googleapis/google-cloud-python/commit/042dc5c369138ca0d3c957c3234561aafa6bde78))

## [2.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.29.1...google-cloud-monitoring-v2.30.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [2.29.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.29.0...google-cloud-monitoring-v2.29.1) (2026-02-05)


### Bug Fixes

* fix mypy errors (#15494) ([1f4c2862d77afa893f7a968af57e7adf54d49d0e](https://github.com/googleapis/google-cloud-python/commit/1f4c2862d77afa893f7a968af57e7adf54d49d0e))

## [2.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.28.0...google-cloud-monitoring-v2.29.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [2.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.27.2...google-cloud-monitoring-v2.28.0) (2025-10-14)


### Features

* Add support for Python 3.14 ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))


### Bug Fixes

* Deprecate credentials_file argument ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))

## [2.27.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.27.1...google-cloud-monitoring-v2.27.2) (2025-06-11)


### Documentation

* Update import statement example in README ([868b006](https://github.com/googleapis/google-cloud-python/commit/868b0069baf1a4bf6705986e0b6885419b35cdcc))

## [2.27.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.27.0...google-cloud-monitoring-v2.27.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([c8bbf32](https://github.com/googleapis/google-cloud-python/commit/c8bbf32606e790b559b261bf96700c76b6e2bfce))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [2.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.26.0...google-cloud-monitoring-v2.27.0) (2025-02-12)


### Features

* add filter field to snooze proto ([0e9d669](https://github.com/googleapis/google-cloud-python/commit/0e9d669febc3fce1a084df4846131a6f000aff1f))
* Add REST Interceptors which support reading metadata ([0e9d669](https://github.com/googleapis/google-cloud-python/commit/0e9d669febc3fce1a084df4846131a6f000aff1f))
* Add support for reading selective GAPIC generation methods from service YAML ([0e9d669](https://github.com/googleapis/google-cloud-python/commit/0e9d669febc3fce1a084df4846131a6f000aff1f))


### Documentation

* remove extra fenced code block markers ([0e9d669](https://github.com/googleapis/google-cloud-python/commit/0e9d669febc3fce1a084df4846131a6f000aff1f))

## [2.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.25.0...google-cloud-monitoring-v2.26.0) (2025-01-13)


### Features

* [google-cloud-monitoring] add active_only field to ListMetricDescriptorsRequest ([#13421](https://github.com/googleapis/google-cloud-python/issues/13421)) ([5777b06](https://github.com/googleapis/google-cloud-python/commit/5777b0623e305b8757218d546534e20f0321afe8))

## [2.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.24.0...google-cloud-monitoring-v2.25.0) (2025-01-02)


### Features

* Add support for opt-in debug logging ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))
* added PrometheusQueryLanguageCondition.disable_metric_validation ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))
* added SqlCondition in AlertPolicy ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))
* added TimeSeries.description for input only ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))
* deprecated QueryTimeSeries (MQL query endpoint) ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))


### Documentation

* ServiceAgentAuthentication supports generating an OAuth token ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))
* ServiceLevelObjective.goal must be &lt;= 0.9999 ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))
* TimeSeries.unit allows limited updating by CreateTimeSeries ([7ecb33c](https://github.com/googleapis/google-cloud-python/commit/7ecb33c399a341f8b4505cfd4be04f2510416e82))

## [2.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.23.1...google-cloud-monitoring-v2.24.0) (2024-12-12)


### Features

* Added support for notification prompts in AlertPolicy ([d596268](https://github.com/googleapis/google-cloud-python/commit/d596268609066ad822eb4a701903e4223ce21583))
* Added support for PromQL metric validation opt-out in AlertPolicy ([d596268](https://github.com/googleapis/google-cloud-python/commit/d596268609066ad822eb4a701903e4223ce21583))

## [2.23.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.23.0...google-cloud-monitoring-v2.23.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13244](https://github.com/googleapis/google-cloud-python/issues/13244)) ([ae1f471](https://github.com/googleapis/google-cloud-python/commit/ae1f47175bf3354f78cb558a844a9cab00317b95))

## [2.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.22.2...google-cloud-monitoring-v2.23.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13207](https://github.com/googleapis/google-cloud-python/issues/13207)) ([ceb9be8](https://github.com/googleapis/google-cloud-python/commit/ceb9be8f89ac7355d842bac1d77b2926eb0b649c))

## [2.22.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.22.1...google-cloud-monitoring-v2.22.2) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([d95af77](https://github.com/googleapis/google-cloud-python/commit/d95af77248f0935a5fe3dba1fccc75124c8b1451))

## [2.22.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.22.0...google-cloud-monitoring-v2.22.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12868](https://github.com/googleapis/google-cloud-python/issues/12868)) ([0e39c1a](https://github.com/googleapis/google-cloud-python/commit/0e39c1a0ab46757bcf80a178d9bd422f6dcb24c6))

## [2.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.21.0...google-cloud-monitoring-v2.22.0) (2024-06-24)


### Features

* Add support to add links in AlertPolicy ([7fcde4f](https://github.com/googleapis/google-cloud-python/commit/7fcde4f8c1d8cbc5351cb3fb799450bbb78d5a2a))

## [2.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.20.0...google-cloud-monitoring-v2.21.0) (2024-04-17)


### Features

* Added CloudRun, GkeNamespace, GkeWorkload, GkeService, and BasicService service types ([f43231d](https://github.com/googleapis/google-cloud-python/commit/f43231d23dfde210ea824e25c607ad551b286946))


### Documentation

* Updated comments accordingly ([f43231d](https://github.com/googleapis/google-cloud-python/commit/f43231d23dfde210ea824e25c607ad551b286946))

## [2.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.19.4...google-cloud-monitoring-v2.20.0) (2024-04-16)


### Features

* Added ServiceAgentAuthentication auth method for Uptime ([25e126a](https://github.com/googleapis/google-cloud-python/commit/25e126aa3438417a50329f5079d13a955b840a29))
* Added Synthetic Monitor targets to Uptime data model ([25e126a](https://github.com/googleapis/google-cloud-python/commit/25e126aa3438417a50329f5079d13a955b840a29))


### Documentation

* Updated comments accordingly ([25e126a](https://github.com/googleapis/google-cloud-python/commit/25e126aa3438417a50329f5079d13a955b840a29))

## [2.19.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.19.3...google-cloud-monitoring-v2.19.4) (2024-04-15)


### Documentation

* [google-cloud-monitoring] Various updates ([#12569](https://github.com/googleapis/google-cloud-python/issues/12569)) ([54b593d](https://github.com/googleapis/google-cloud-python/commit/54b593daccbcf29fcd964debbbb706372c5d81a3))

## [2.19.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.19.2...google-cloud-monitoring-v2.19.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12385](https://github.com/googleapis/google-cloud-python/issues/12385)) ([d50f4d0](https://github.com/googleapis/google-cloud-python/commit/d50f4d042774e2f12e9fe03459eae9ce91247df3))

## [2.19.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.19.1...google-cloud-monitoring-v2.19.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12307](https://github.com/googleapis/google-cloud-python/issues/12307)) ([be87bc4](https://github.com/googleapis/google-cloud-python/commit/be87bc4a33fe32a512448a42246c9873da88269f))
* fix ValueError in test__validate_universe_domain ([7c2f2c2](https://github.com/googleapis/google-cloud-python/commit/7c2f2c29d74c9584efc42ddfe8bc098a594391a2))
* make google-cloud-monitoring tests work without `mock` ([#12317](https://github.com/googleapis/google-cloud-python/issues/12317)) ([1988e0d](https://github.com/googleapis/google-cloud-python/commit/1988e0d753f4b15d6fadb310fb342ece0d7b0edd))

## [2.19.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.19.0...google-cloud-monitoring-v2.19.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([27dceb9](https://github.com/googleapis/google-cloud-python/commit/27dceb901cb9bf28da82925ad382ce7c58e91f38))

## [2.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.18.0...google-cloud-monitoring-v2.19.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12241](https://github.com/googleapis/google-cloud-python/issues/12241)) ([aae72f5](https://github.com/googleapis/google-cloud-python/commit/aae72f5e6c7d48e777fdf68d1012b2b51b912bad))

## [2.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.17.0...google-cloud-monitoring-v2.18.0) (2023-12-12)


### Features

* Added support for severity in AlertPolicy ([4e817f8](https://github.com/googleapis/google-cloud-python/commit/4e817f8dac1e884e5eab4f81a43d129635d83369))


### Documentation

* add value range to comment on field forecast_horizon ([4e817f8](https://github.com/googleapis/google-cloud-python/commit/4e817f8dac1e884e5eab4f81a43d129635d83369))

## [2.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-monitoring-v2.16.0...google-cloud-monitoring-v2.17.0) (2023-12-07)


### Features

* Add support for python 3.12 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Introduce compatibility with native namespace packages ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))
* Use `retry_async` instead of `retry` in async client ([5cd98aa](https://github.com/googleapis/google-cloud-python/commit/5cd98aa0e8ead2eef82ecdcef4141b33a7da2b5a))

## [2.16.0](https://github.com/googleapis/python-monitoring/compare/v2.15.1...v2.16.0) (2023-10-09)


### Features

* Added support for forecast options in AlertPolicy ([218e678](https://github.com/googleapis/python-monitoring/commit/218e67818d7a19e45bd1521adb3cea76efb3f541))
* Added support for promQL condition type in AlertPolicy ([218e678](https://github.com/googleapis/python-monitoring/commit/218e67818d7a19e45bd1521adb3cea76efb3f541))
* Added support for retriggering notifications in AlertPolicy ([218e678](https://github.com/googleapis/python-monitoring/commit/218e67818d7a19e45bd1521adb3cea76efb3f541))


### Documentation

* Minor formatting ([218e678](https://github.com/googleapis/python-monitoring/commit/218e67818d7a19e45bd1521adb3cea76efb3f541))

## [2.15.1](https://github.com/googleapis/python-monitoring/compare/v2.15.0...v2.15.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#545](https://github.com/googleapis/python-monitoring/issues/545)) ([4309faa](https://github.com/googleapis/python-monitoring/commit/4309faa3664044a0b01078ba34da5663984d4d0f))

## [2.15.0](https://github.com/googleapis/python-monitoring/compare/v2.14.2...v2.15.0) (2023-05-25)


### Features

* Add basic http authentication ([2774ac4](https://github.com/googleapis/python-monitoring/commit/2774ac41588c9707102b2f6f1af79c3728db5eae))
* Add httpStatusCode ([2774ac4](https://github.com/googleapis/python-monitoring/commit/2774ac41588c9707102b2f6f1af79c3728db5eae))
* Add ICMP pings ([2774ac4](https://github.com/googleapis/python-monitoring/commit/2774ac41588c9707102b2f6f1af79c3728db5eae))
* Add individual USA regions ([2774ac4](https://github.com/googleapis/python-monitoring/commit/2774ac41588c9707102b2f6f1af79c3728db5eae))
* Add json path matching capabilities ([2774ac4](https://github.com/googleapis/python-monitoring/commit/2774ac41588c9707102b2f6f1af79c3728db5eae))

## [2.14.2](https://github.com/googleapis/python-monitoring/compare/v2.14.1...v2.14.2) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#535](https://github.com/googleapis/python-monitoring/issues/535)) ([e10167f](https://github.com/googleapis/python-monitoring/commit/e10167f5d0def6fd6707fc8bda56a2cfe6a47eac))

## [2.14.1](https://github.com/googleapis/python-monitoring/compare/v2.14.0...v2.14.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([4643933](https://github.com/googleapis/python-monitoring/commit/46439333f73e71267d28fc395850f6aa66bca288))


### Documentation

* Add documentation for enums ([4643933](https://github.com/googleapis/python-monitoring/commit/46439333f73e71267d28fc395850f6aa66bca288))

## [2.14.0](https://github.com/googleapis/python-monitoring/compare/v2.13.0...v2.14.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#521](https://github.com/googleapis/python-monitoring/issues/521)) ([c448c0c](https://github.com/googleapis/python-monitoring/commit/c448c0ca6729a586ee072a6d28595e04970fd311))

## [2.13.0](https://github.com/googleapis/python-monitoring/compare/v2.12.0...v2.13.0) (2023-01-09)


### Features

* Added Snooze API support ([#519](https://github.com/googleapis/python-monitoring/issues/519)) ([1d33db7](https://github.com/googleapis/python-monitoring/commit/1d33db7ade09a6ee35e2a4b371bc2d3ba82c8e06))

## [2.12.0](https://github.com/googleapis/python-monitoring/compare/v2.11.3...v2.12.0) (2022-12-15)


### Features

* Add typing to proto.Message based class attributes ([eaaca48](https://github.com/googleapis/python-monitoring/commit/eaaca4815872d78725893b0aa26ffd96d84d58d5))


### Bug Fixes

* Add dict typing for client_options ([eaaca48](https://github.com/googleapis/python-monitoring/commit/eaaca4815872d78725893b0aa26ffd96d84d58d5))
* Add metric label example to the snippet ([#509](https://github.com/googleapis/python-monitoring/issues/509)) ([48b4e35](https://github.com/googleapis/python-monitoring/commit/48b4e35dee6066035b91214ccb44022f539cb007))
* Add missing argument description ([#504](https://github.com/googleapis/python-monitoring/issues/504)) ([8d54a7e](https://github.com/googleapis/python-monitoring/commit/8d54a7e337b094e42ab544078f160c15ebc55921))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([eaaca48](https://github.com/googleapis/python-monitoring/commit/eaaca4815872d78725893b0aa26ffd96d84d58d5))
* Drop usage of pkg_resources ([eaaca48](https://github.com/googleapis/python-monitoring/commit/eaaca4815872d78725893b0aa26ffd96d84d58d5))
* Fix timeout default values ([eaaca48](https://github.com/googleapis/python-monitoring/commit/eaaca4815872d78725893b0aa26ffd96d84d58d5))
* Remove duplicate variable declaration ([#503](https://github.com/googleapis/python-monitoring/issues/503)) ([99a981c](https://github.com/googleapis/python-monitoring/commit/99a981c9b4a53597020a30503e028ecc554b4d68))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([eaaca48](https://github.com/googleapis/python-monitoring/commit/eaaca4815872d78725893b0aa26ffd96d84d58d5))

## [2.11.3](https://github.com/googleapis/python-monitoring/compare/v2.11.2...v2.11.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#500](https://github.com/googleapis/python-monitoring/issues/500)) ([9bb171e](https://github.com/googleapis/python-monitoring/commit/9bb171e7292cb60c6df9824a1c046cc57a76a9f2))

## [2.11.2](https://github.com/googleapis/python-monitoring/compare/v2.11.1...v2.11.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#496](https://github.com/googleapis/python-monitoring/issues/496)) ([7d8eeb8](https://github.com/googleapis/python-monitoring/commit/7d8eeb8e661ea3b4306124a0d50f22068615da41))

## [2.11.1](https://github.com/googleapis/python-monitoring/compare/v2.11.0...v2.11.1) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#475](https://github.com/googleapis/python-monitoring/issues/475)) ([14f4612](https://github.com/googleapis/python-monitoring/commit/14f46126dc351fcd06c5b2acaf180f093fdda83b))
* **deps:** require proto-plus >= 1.22.0 ([14f4612](https://github.com/googleapis/python-monitoring/commit/14f46126dc351fcd06c5b2acaf180f093fdda83b))

## [2.11.0](https://github.com/googleapis/python-monitoring/compare/v2.10.1...v2.11.0) (2022-08-06)


### Features

* Added support for evaluating missing data in AlertPolicy ([#470](https://github.com/googleapis/python-monitoring/issues/470)) ([71e94c2](https://github.com/googleapis/python-monitoring/commit/71e94c234d500515ed22cc7df031ea0d45153084))


### Documentation

* **samples:** add docstrings to explain the project ID format ([#469](https://github.com/googleapis/python-monitoring/issues/469)) ([7009724](https://github.com/googleapis/python-monitoring/commit/700972421378c06951094bbf525ba53c75748a61))

## [2.10.1](https://github.com/googleapis/python-monitoring/compare/v2.10.0...v2.10.1) (2022-07-14)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#461](https://github.com/googleapis/python-monitoring/issues/461)) ([8e631d7](https://github.com/googleapis/python-monitoring/commit/8e631d709f24b8434f0be976affb97d693d920f6))

## [2.10.0](https://github.com/googleapis/python-monitoring/compare/v2.9.2...v2.10.0) (2022-07-06)


### Features

* add audience parameter ([0bf6561](https://github.com/googleapis/python-monitoring/commit/0bf6561dd3f6184ae6d6e9e52522aa1460430718))


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#457](https://github.com/googleapis/python-monitoring/issues/457)) ([0bf6561](https://github.com/googleapis/python-monitoring/commit/0bf6561dd3f6184ae6d6e9e52522aa1460430718))
* require python 3.7+ ([#459](https://github.com/googleapis/python-monitoring/issues/459)) ([1ff6e13](https://github.com/googleapis/python-monitoring/commit/1ff6e13af83764128e8f0e43b7c5f89b12939889))

## [2.9.2](https://github.com/googleapis/python-monitoring/compare/v2.9.1...v2.9.2) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#441](https://github.com/googleapis/python-monitoring/issues/441)) ([87a8660](https://github.com/googleapis/python-monitoring/commit/87a8660538bfeac00eedadf2be17633ffe370f22))


### Documentation

* fix changelog header to consistent size ([#439](https://github.com/googleapis/python-monitoring/issues/439)) ([ce27cb4](https://github.com/googleapis/python-monitoring/commit/ce27cb462c4ae74572015f027c9b4b0cd44d069d))

## [2.9.1](https://github.com/googleapis/python-monitoring/compare/v2.9.0...v2.9.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#286](https://github.com/googleapis/python-monitoring/issues/286)) ([e77a5cd](https://github.com/googleapis/python-monitoring/commit/e77a5cd8b8a6c928faedd52a31b76ec6e645403c))

## [2.9.0](https://github.com/googleapis/python-monitoring/compare/v2.8.0...v2.9.0) (2022-02-26)


### Features

* add api key support ([#270](https://github.com/googleapis/python-monitoring/issues/270)) ([412b9fc](https://github.com/googleapis/python-monitoring/commit/412b9fc844b8be1a5c763c02a244c2cbecb8091d))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([c58bcce](https://github.com/googleapis/python-monitoring/commit/c58bcce924ff8603bc5596f5c7dc5afd0517216f))


### Documentation

* add generated snippets ([#276](https://github.com/googleapis/python-monitoring/issues/276)) ([2340cc9](https://github.com/googleapis/python-monitoring/commit/2340cc959bbde2de885f2fce9b36cfc884a1341e))

## [2.8.0](https://www.github.com/googleapis/python-monitoring/compare/v2.7.0...v2.8.0) (2021-11-16)


### Features

* Added support for auto-close configurations ([#253](https://www.github.com/googleapis/python-monitoring/issues/253)) ([0541c7a](https://www.github.com/googleapis/python-monitoring/commit/0541c7acc69465030077b5ce3b1d9c40cea7b634))

## [2.7.0](https://www.github.com/googleapis/python-monitoring/compare/v2.6.0...v2.7.0) (2021-11-09)


### Features

* add CreateServiceTimeSeries RPC ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))


### Bug Fixes

* **deps:** drop packaging dependency ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))
* **deps:** require google-api-core >= 1.28.0 ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))
* Reintroduce deprecated field/enum `ServiceTier` for backward compatibility ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))


### Miscellaneous Chores

* release as 2.7.0 ([#247](https://www.github.com/googleapis/python-monitoring/issues/247)) ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))


### Documentation

* list oneofs in docstring ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))
* Use absolute link targets in comments ([b347e70](https://www.github.com/googleapis/python-monitoring/commit/b347e7083ff04c04e287b7afc79c425a1d04f731))

## [2.6.0](https://www.github.com/googleapis/python-monitoring/compare/v2.5.2...v2.6.0) (2021-11-01)


### Features

* add context manager support in client ([#230](https://www.github.com/googleapis/python-monitoring/issues/230)) ([954dd18](https://www.github.com/googleapis/python-monitoring/commit/954dd18966520dbc623470ef528166d83d3e19ba))
* add CreateServiceTimeSeries RPC ([#235](https://www.github.com/googleapis/python-monitoring/issues/235)) ([2970b22](https://www.github.com/googleapis/python-monitoring/commit/2970b22ca5b4959ee1d3e1e883cdb00951e3917f))


### Bug Fixes

* **deps:** drop packaging dependency ([22d4eab](https://www.github.com/googleapis/python-monitoring/commit/22d4eabbafbdc16b0f4faf66f966442691de7666))
* **deps:** require google-api-core >= 1.28.0 ([22d4eab](https://www.github.com/googleapis/python-monitoring/commit/22d4eabbafbdc16b0f4faf66f966442691de7666))
* Reintroduce deprecated field/enum `ServiceTier` for backward compatibility ([#240](https://www.github.com/googleapis/python-monitoring/issues/240)) ([eeb0534](https://www.github.com/googleapis/python-monitoring/commit/eeb05347eaf6e7a0794e679d83fe70a0db6a02a3))


### Documentation

* list oneofs in docstring ([22d4eab](https://www.github.com/googleapis/python-monitoring/commit/22d4eabbafbdc16b0f4faf66f966442691de7666))
* Use absolute link targets in comments ([eeb0534](https://www.github.com/googleapis/python-monitoring/commit/eeb05347eaf6e7a0794e679d83fe70a0db6a02a3))

## [2.6.0](https://www.github.com/googleapis/python-monitoring/compare/v2.5.2...v2.6.0) (2021-10-07)


### Features

* add context manager support in client ([#230](https://www.github.com/googleapis/python-monitoring/issues/230)) ([954dd18](https://www.github.com/googleapis/python-monitoring/commit/954dd18966520dbc623470ef528166d83d3e19ba))

## [2.5.2](https://www.github.com/googleapis/python-monitoring/compare/v2.5.1...v2.5.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([4a8b823](https://www.github.com/googleapis/python-monitoring/commit/4a8b823061a03fd0e5c385c1fa0ac964b9a5597a))

## [2.5.1](https://www.github.com/googleapis/python-monitoring/compare/v2.5.0...v2.5.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([ffae24c](https://www.github.com/googleapis/python-monitoring/commit/ffae24c816a3e1645464098cf86fdaf54a3064a9))

## [2.5.0](https://www.github.com/googleapis/python-monitoring/compare/v2.4.2...v2.5.0) (2021-08-27)


### Features

* Added support for log-based alerts ([#204](https://www.github.com/googleapis/python-monitoring/issues/204)) ([b56a78c](https://www.github.com/googleapis/python-monitoring/commit/b56a78c50780e778f8ce1ad956e621433d1c451b))
* Added support for user-defined labels on cloud monitoring's Service object ([b56a78c](https://www.github.com/googleapis/python-monitoring/commit/b56a78c50780e778f8ce1ad956e621433d1c451b))
* Added support for user-defined labels on cloud monitoring's ServiceLevelObjective object ([b56a78c](https://www.github.com/googleapis/python-monitoring/commit/b56a78c50780e778f8ce1ad956e621433d1c451b))


### Bug Fixes

* mark required fields in QueryTimeSeriesRequest as required by the backend ([b56a78c](https://www.github.com/googleapis/python-monitoring/commit/b56a78c50780e778f8ce1ad956e621433d1c451b))


### Documentation

* **samples:** include example writing of label data ([#202](https://www.github.com/googleapis/python-monitoring/issues/202)) ([f5e8cf8](https://www.github.com/googleapis/python-monitoring/commit/f5e8cf8b51812b9e79bb5312f84e29b3f8c2c81e))

## [2.4.2](https://www.github.com/googleapis/python-monitoring/compare/v2.4.1...v2.4.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#190](https://www.github.com/googleapis/python-monitoring/issues/190)) ([502487a](https://www.github.com/googleapis/python-monitoring/commit/502487a6c40322b5d8a9d38e9bd0783c0db9d756))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#184](https://www.github.com/googleapis/python-monitoring/issues/184)) ([5b7b07b](https://www.github.com/googleapis/python-monitoring/commit/5b7b07b263e2e86f0b504b721c4295f7d8bb542a))


### Miscellaneous Chores

* release as 2.4.2 ([#191](https://www.github.com/googleapis/python-monitoring/issues/191)) ([6f183dd](https://www.github.com/googleapis/python-monitoring/commit/6f183ddeef540be4f47ee553e2b2ee8424508968))

## [2.4.1](https://www.github.com/googleapis/python-monitoring/compare/v2.4.0...v2.4.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#183](https://www.github.com/googleapis/python-monitoring/issues/183)) ([fdc5b07](https://www.github.com/googleapis/python-monitoring/commit/fdc5b0729cb3cb7e204c36569f253fb57728b740))

## [2.4.0](https://www.github.com/googleapis/python-monitoring/compare/v2.3.0...v2.4.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#165](https://www.github.com/googleapis/python-monitoring/issues/165)) ([064f1e0](https://www.github.com/googleapis/python-monitoring/commit/064f1e0a8df02c04bdae6b13c645f2b399c2c1ef))


### Bug Fixes

* disable always_use_jwt_access ([#171](https://www.github.com/googleapis/python-monitoring/issues/171)) ([c194a00](https://www.github.com/googleapis/python-monitoring/commit/c194a00031763153bcc67346328a02b85fabc359))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-monitoring/issues/1127)) ([#159](https://www.github.com/googleapis/python-monitoring/issues/159)) ([adc82c9](https://www.github.com/googleapis/python-monitoring/commit/adc82c9d1812fb0efe00cbfa09f19e8c04277881)), closes [#1126](https://www.github.com/googleapis/python-monitoring/issues/1126)

## [2.3.0](https://www.github.com/googleapis/python-monitoring/compare/v2.2.1...v2.3.0) (2021-06-18)


### Features

* support self-signed JWT flow for service accounts ([ffa4b1f](https://www.github.com/googleapis/python-monitoring/commit/ffa4b1fb529824a5c408880ca5d1e80149bb5a8c))


### Bug Fixes

* add async client to %name_%version/init.py ([ffa4b1f](https://www.github.com/googleapis/python-monitoring/commit/ffa4b1fb529824a5c408880ca5d1e80149bb5a8c))

## [2.2.1](https://www.github.com/googleapis/python-monitoring/compare/v2.2.0...v2.2.1) (2021-03-29)


### Bug Fixes

* fix minimum required versions of proto-plus and pandas ([#102](https://www.github.com/googleapis/python-monitoring/issues/102)) ([782b3b2](https://www.github.com/googleapis/python-monitoring/commit/782b3b29a93f5f6aa0fc027fd9863d753f604dc9))

## [2.2.0](https://www.github.com/googleapis/python-monitoring/compare/v2.1.0...v2.2.0) (2021-03-25)


### Features

* add `client_cert_source_for_mtls` ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added `IstioCanonicalService` for service monitoring. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added `total_size` to the response of `ListAlertPolicies`. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added creation and mutation records to notification channels. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added support for Monitoring Query Language ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added support for Monitoring Query Language ([#101](https://www.github.com/googleapis/python-monitoring/issues/101)) ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added support for querying metrics for folders and organizations. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added support for secondary aggregation when querying metrics. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Added support for units in the `MetricService` ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))


### Bug Fixes

* Extended the default deadline for `UpdateGroup` to 180s. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* Un-deprecated `cluster_istio` for service monitoring. ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))
* use correct retry deadline ([0eb2ca6](https://www.github.com/googleapis/python-monitoring/commit/0eb2ca6b5044553c11d5f5e0f4859bf65387909b))

## [2.1.0](https://www.github.com/googleapis/python-monitoring/compare/v2.0.1...v2.1.0) (2021-03-12)


### Features

* Adding labels to the metric descriptor in the snippets.py ([#88](https://www.github.com/googleapis/python-monitoring/issues/88)) ([811f9aa](https://www.github.com/googleapis/python-monitoring/commit/811f9aa409ec922402cb83a6753812518b7a0d4b))


### Bug Fixes

* fix `as_dataframe` ([#91](https://www.github.com/googleapis/python-monitoring/issues/91)) ([f135202](https://www.github.com/googleapis/python-monitoring/commit/f135202f1dd7866c4be2d709b522beb2710f5cda))


### Documentation

* remove code snippet and 'Stackdriver' ([#71](https://www.github.com/googleapis/python-monitoring/issues/71)) ([4cdb1ff](https://www.github.com/googleapis/python-monitoring/commit/4cdb1ff439154409c94e347dd5f3b6e2bc40e998))

## [2.0.1](https://www.github.com/googleapis/python-monitoring/compare/v2.0.0...v2.0.1) (2021-02-18)


### Bug Fixes

* allow any set query_params to work with `query.iter()` ([#83](https://www.github.com/googleapis/python-monitoring/issues/83)) ([4279c92](https://www.github.com/googleapis/python-monitoring/commit/4279c9252c21e24a43d2613de7fdb1af35dc30fc))
* remove gRPC send/recv limits and expose client transport ([#62](https://www.github.com/googleapis/python-monitoring/issues/62)) ([bec9e87](https://www.github.com/googleapis/python-monitoring/commit/bec9e87551baf9ef5d60c81810e3efa01e96377f))

## [2.0.0](https://www.github.com/googleapis/python-monitoring/compare/v1.1.0...v2.0.0) (2020-10-06)


### ⚠ BREAKING CHANGES

* move to use microgen (#54). See [Migration Guide](https://github.com/googleapis/python-monitoring/blob/main/UPGRADING.md).

### Features

* move to use microgen ([#54](https://www.github.com/googleapis/python-monitoring/issues/54)) ([d25e49f](https://www.github.com/googleapis/python-monitoring/commit/d25e49f13e6f880e77fcb0dc5ef4e3c61fba079a))

## [1.1.0](https://www.github.com/googleapis/python-monitoring/compare/v1.0.0...v1.1.0) (2020-08-20)


### Features

* add "not equal" support to the query filter ([#11](https://www.github.com/googleapis/python-monitoring/issues/11)) ([e293f7f](https://www.github.com/googleapis/python-monitoring/commit/e293f7f90b0d1ccb285c16a32251e442fda06a8e))

## [1.0.0](https://www.github.com/googleapis/python-monitoring/compare/v0.36.0...v1.0.0) (2020-06-03)


### Features

* set release_status to Production/Stable ([#8](https://www.github.com/googleapis/python-monitoring/issues/8)) ([a99d67a](https://www.github.com/googleapis/python-monitoring/commit/a99d67a4f1399b9a74f189c6332cd85e56149fac))

## [0.36.0](https://www.github.com/googleapis/python-monitoring/compare/v0.35.0...v0.36.0) (2020-05-13)


### Features

* BREAKING CHANGE: drop support for TimeSeriesQueryLanguageCondition as an alert condition type ([#22](https://www.github.com/googleapis/python-monitoring/issues/22)) ([e4bc568](https://www.github.com/googleapis/python-monitoring/commit/e4bc5682d39f7e5938868497496f5d49318cee43))

## [0.35.0](https://www.github.com/googleapis/python-monitoring/compare/v0.34.0...v0.35.0) (2020-04-21)


### Features

* add uptime check feature; increase default timeout (via synth) ([#15](https://www.github.com/googleapis/python-monitoring/issues/15)) ([dcf074a](https://www.github.com/googleapis/python-monitoring/commit/dcf074aed9922982f7324d4f2943d9435778d46c))

## 0.34.0

11-19-2019 14:27 PST

### Implementation Changes
- Deprecate resource name helper methods; update docs configuration (via synth). ([#9838](https://github.com/googleapis/google-cloud-python/pull/9838))

### New Features
- Add service monitoring (via synth). ([#9799](https://github.com/googleapis/google-cloud-python/pull/9799))
- Add `monitoring.v3.InternalChecker.state` (via synth). ([#9546](https://github.com/googleapis/google-cloud-python/pull/9546))
- Add `monitoring.v3.UptimeCheckConfig.ContentMatcher.ContentMatcherOption` (via synth). ([#9546](https://github.com/googleapis/google-cloud-python/pull/9546))
- Add `recursive` parameter to `delete_group` (via synth). ([#9546](https://github.com/googleapis/google-cloud-python/pull/9546))
- Add read-only `validity` field to `monitoring.v3.AlertPolicy` (via synth). ([#9546](https://github.com/googleapis/google-cloud-python/pull/9546))
- Add `validate_ssl` parameter to `monitoring.v3.UptimeCheckConfig.HttpCheck` (via synth). ([#9546](https://github.com/googleapis/google-cloud-python/pull/9546))

### Documentation
- Add python 2 sunset banner to documentation. ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))
- Fix intersphinx reference to requests. ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Remove CI for gh-pages, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))
- Remove compatability badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))

### Internal / Testing Changes
- Revert change to docs/conf.py. ([#9803](https://github.com/googleapis/google-cloud-python/pull/9803))
- Normalize VPCSC configuration in systests. ([#9615](https://github.com/googleapis/google-cloud-python/pull/9615))
- Make VPCSC env comparison case-insensitive. ([#9564](https://github.com/googleapis/google-cloud-python/pull/9564))
- Refresh VPCSC tests. ([#9437](https://github.com/googleapis/google-cloud-python/pull/9437))
- Fix environment variables for VPC tests. ([#8302](https://github.com/googleapis/google-cloud-python/pull/8302))

## 0.33.0

08-12-2019 13:54 PDT

### New Features
- Add notification channel verification; remove send/recv msg size limit (via synth). ([#8980](https://github.com/googleapis/google-cloud-python/pull/8980))

### Documentation
- Normalize docs. ([#8994](https://github.com/googleapis/google-cloud-python/pull/8994))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 0.32.0

07-24-2019 16:52 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth).  ([#8397](https://github.com/googleapis/google-cloud-python/pull/8397))
- Add routing header to method metadata, update docs config (via synth).  ([#7642](https://github.com/googleapis/google-cloud-python/pull/7642))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Remove unused message exports. ([#7271](https://github.com/googleapis/google-cloud-python/pull/7271))
- Protoc-generated serialization update. ([#7089](https://github.com/googleapis/google-cloud-python/pull/7089))
- Pick up stub docstring fix in GAPIC generator. ([#6976](https://github.com/googleapis/google-cloud-python/pull/6976))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8516](https://github.com/googleapis/google-cloud-python/pull/8516))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Fixes [#8545](https://github.com/googleapis/google-cloud-python/pull/8545) by removing typing information for kwargs to not conflict with type checkers ([#8546](https://github.com/googleapis/google-cloud-python/pull/8546))
- Update docstrings, copy lintified proto files (via synth). ([#7451](https://github.com/googleapis/google-cloud-python/pull/7451))
- googlecloudplatform --> googleapis in READMEs ([#7411](https://github.com/googleapis/google-cloud-python/pull/7411))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Update copyright: 2018 -> 2019. ([#7151](https://github.com/googleapis/google-cloud-python/pull/7151))

### Internal / Testing Changes
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8358](https://github.com/googleapis/google-cloud-python/pull/8358))
- Add disclaimer to auto-generated template files (via synth). ([#8321](https://github.com/googleapis/google-cloud-python/pull/8321))
- Fix coverage in 'types.py' (via synth). ([#8159](https://github.com/googleapis/google-cloud-python/pull/8159))
- Add empty lines (via synth). ([#8065](https://github.com/googleapis/google-cloud-python/pull/8065))
- Add nox session `docs` (via synth). ([#7777](https://github.com/googleapis/google-cloud-python/pull/7777))
- Regenerate VPCSC tests to include NotificationChannelService and UptimeCheckService. ([#7853](https://github.com/googleapis/google-cloud-python/pull/7853))
- Set environment variables for VPCSC system tests. ([#7847](https://github.com/googleapis/google-cloud-python/pull/7847))
- Add VPCSC system test. ([#7791](https://github.com/googleapis/google-cloud-python/pull/7791))
- protobuf file housekeeping (no user-visible changes) (via synth).  ([#7588](https://github.com/googleapis/google-cloud-python/pull/7588))
- Add clarifying comment to blacken nox target. ([#7398](https://github.com/googleapis/google-cloud-python/pull/7398))
- Trivial gapic-generator change. ([#7231](https://github.com/googleapis/google-cloud-python/pull/7231))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))

## 0.31.1

12-17-2018 16:51 PST


### Implementation Changes
- Import  `iam.policy` from `google.api_core.iam.policy`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Normalize docs for `page_size` / `max_results` / `page_token`. ([#6842](https://github.com/googleapis/google-cloud-python/pull/6842))

### Internal / Testing Changes
- Add baseline for synth.metadata
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))

## 0.31.0

11-29-2018 13:03 PST


### Implementation Changes
- Pick up enum fixes in the GAPIC generator. ([#6614](https://github.com/googleapis/google-cloud-python/pull/6614))
- Pick up fixes to the GAPIC generator. ([#6501](https://github.com/googleapis/google-cloud-python/pull/6501))
- Fix client_info bug, update docstrings and timeouts. ([#6416](https://github.com/googleapis/google-cloud-python/pull/6416))

### Dependencies
- Bump minimum 'api_core' version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Docstring changes, 'account' -> 'workspace', via synth. ([#6461](https://github.com/googleapis/google-cloud-python/pull/6461))
- Add 'dropped_labels', 'span_context', plus docstring changes. ([#6358](https://github.com/googleapis/google-cloud-python/pull/6358))
- Fix GAX fossils ([#6264](https://github.com/googleapis/google-cloud-python/pull/6264))
- Harmonize / DRY 'monitoring/README.rst' / 'monitoring/docs/index.rst'. ([#6156](https://github.com/googleapis/google-cloud-python/pull/6156))

### Internal / Testing Changes
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Assorted synth fixups / cleanups ([#6400](https://github.com/googleapis/google-cloud-python/pull/6400))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Fix long lines from autosynth ([#5961](https://github.com/googleapis/google-cloud-python/pull/5961)
- Test pandas under all supported Python versions ([#5858](https://github.com/googleapis/google-cloud-python/pull/5858))

## 0.30.1

### Implementation Changes
- Monitoring: Add Transports Layer to clients (#5594)
- Remove gRPC size restrictions (4MB default) (#5594)

### Documentation
- Monitoring. Update documentation links. (#5557)

## 0.30.0

### Implementation Changes
- Avoid overwriting '__module__' of messages from shared modules. (#5364)

### New Features
- Add aliases for new V3 service clients. (#5424)

### Documentation
- Remove link to `usage` on index of monitoring (#5272)

### Internal / Testing Changes
- Modify system tests to use prerelease versions of grpcio (#5304)
- Add Test runs for Python 3.7 and remove 3.4 (#5295)

## 0.29.0

### Implementation Changes
- Update monitoring library to use new generated client (#5212)
- Move aligner and reducer links from timeSeries.list to alertPolicies (#5011)

### Internal / Testing Changes
- Fix bad trove classifier

## 0.28.1

### Implementation changes

- Convert label values to str in client.metric() (#4910)

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Documentation

- Fixing "Fore" -> "For" typo in README docs. (#4317)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)
- Making a `nox -s default` session for all packages. (#4324)
- Shorten test names (#4321)

## 0.28.0

### Documentation

- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)

PyPI: https://pypi.org/project/google-cloud-monitoring/0.28.0/
