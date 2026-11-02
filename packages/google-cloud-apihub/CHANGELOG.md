# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-apihub/#history

## [0.7.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.7.0...google-cloud-apihub-v0.7.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.6.0...google-cloud-apihub-v0.7.0) (2026-06-02)


### Features

* regenerate google-cloud-a packages (#17089) ([39c988267529419b03f808d7662ec521258571b4](https://github.com/googleapis/google-cloud-python/commit/39c988267529419b03f808d7662ec521258571b4))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.5.0...google-cloud-apihub-v0.6.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.4.0...google-cloud-apihub-v0.5.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.3.0...google-cloud-apihub-v0.4.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.7...google-cloud-apihub-v0.3.0) (2025-10-07)


### Features

* [google-cloud-apihub] enable grpc transport (#14577) - [ ] Regenerate this pull request now. ([015634e3fe5c3305a49ad768f27c9e85c0f8e242](https://github.com/googleapis/google-cloud-python/commit/015634e3fe5c3305a49ad768f27c9e85c0f8e242))

## [0.2.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.6...google-cloud-apihub-v0.2.7) (2025-09-22)


### Features

* Add full lifecycle management for API Operations within API Versions (Create, Update, Delete) ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))
* Add new fields and enums to resources to support richer metadata, including source tracking (SourceMetadata), plugin configurations (AuthConfig, ConfigVariable), new attributes, and additional deployment details ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))
* Enable Deletion of ApiHub Instances via the Provisioning service ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))
* Enhance list filtering options across various resources (APIs, Versions, Specs, Operations, Deployments) with support for user-defined attributes ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))
* Introduce new services for data collection (ApiHubCollect) and curation (ApiHubCurate) ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))
* Make CMEK configuration optional for ApiHub Instances, defaulting to GMEK ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))
* Significantly expand Plugin and Plugin Instance management capabilities, including creation, execution, and lifecycle control ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))


### Documentation

* Update field descriptions, comments, and links in existing services ([24d4f37](https://github.com/googleapis/google-cloud-python/commit/24d4f37adcd333552c834fd6a4fcfb41522c90df))

## [0.2.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.5...google-cloud-apihub-v0.2.6) (2025-06-11)


### Documentation

* Update import statement example in README ([1562bb7](https://github.com/googleapis/google-cloud-python/commit/1562bb740c7cd56179e52185dde3c32af861de5e))

## [0.2.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.4...google-cloud-apihub-v0.2.5) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([a1b9294](https://github.com/googleapis/google-cloud-python/commit/a1b9294d0bf6e27c2a951d6df7faf7807dc5420b))

## [0.2.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.3...google-cloud-apihub-v0.2.4) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))
* Add support for reading selective GAPIC generation methods from service YAML ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))

## [0.2.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.2...google-cloud-apihub-v0.2.3) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [0.2.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.1...google-cloud-apihub-v0.2.2) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([85c7512](https://github.com/googleapis/google-cloud-python/commit/85c7512bbdde2b9cc60b4ad42b8c36c4558a07a5))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.2.0...google-cloud-apihub-v0.2.1) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13199](https://github.com/googleapis/google-cloud-python/issues/13199)) ([2fc3726](https://github.com/googleapis/google-cloud-python/commit/2fc372685731141ca1ed2a917dd18bacd79db88e))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-apihub-v0.1.0...google-cloud-apihub-v0.2.0) (2024-09-04)


### ⚠ BREAKING CHANGES

* [google-cloud-apihub] remove gRPC support for client libraries ([#13055](https://github.com/googleapis/google-cloud-python/issues/13055))

### Bug Fixes

* [google-cloud-apihub] remove gRPC support for client libraries ([#13055](https://github.com/googleapis/google-cloud-python/issues/13055)) ([3762ff4](https://github.com/googleapis/google-cloud-python/commit/3762ff40e51466bc516939a31732300c8e20211a))

## 0.1.0 (2024-08-08)


### Features

* add initial files for google.cloud.apihub.v1 ([#12993](https://github.com/googleapis/google-cloud-python/issues/12993)) ([2ac4597](https://github.com/googleapis/google-cloud-python/commit/2ac4597188c70a922479bf48adf2a88d850bc534))

## Changelog
