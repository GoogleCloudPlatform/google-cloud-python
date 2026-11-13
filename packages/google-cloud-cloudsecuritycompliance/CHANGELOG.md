# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-cloudsecuritycompliance/#history

## [0.8.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.8.0...google-cloud-cloudsecuritycompliance-v0.8.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.7.0...google-cloud-cloudsecuritycompliance-v0.8.0) (2026-06-02)


### Features

* regenerate google-cloud-c packages (#17091) ([165839343695fc74d09fc7900d4c55ddcb31a4d8](https://github.com/googleapis/google-cloud-python/commit/165839343695fc74d09fc7900d4c55ddcb31a4d8))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.6.0...google-cloud-cloudsecuritycompliance-v0.7.0) (2026-05-06)

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.5.0...google-cloud-cloudsecuritycompliance-v0.6.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.4.0...google-cloud-cloudsecuritycompliance-v0.5.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.3.0...google-cloud-cloudsecuritycompliance-v0.4.0) (2025-11-06)


### Documentation

* Updated docs for the APIs  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* Changes to few fields are also made  ([a7ed7007b4a25a4266f22d90e3ccde137ae5a066](https://github.com/googleapis/google-cloud-python/commit/a7ed7007b4a25a4266f22d90e3ccde137ae5a066))


### Features

* Adding client libraries for Monitoring API Compliance Manager Service  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add Audit API surface  ([a7ed7007b4a25a4266f22d90e3ccde137ae5a066](https://github.com/googleapis/google-cloud-python/commit/a7ed7007b4a25a4266f22d90e3ccde137ae5a066))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.2.0...google-cloud-cloudsecuritycompliance-v0.3.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-cloudsecuritycompliance-v0.1.0...google-cloud-cloudsecuritycompliance-v0.2.0) (2025-09-22)


### ⚠ BREAKING CHANGES

* An existing enum `RegulatoryControlResponsibilityType` is removed
* An existing message `CloudControlGroupDetails` is removed
* An existing field `cloud_control_group_details` is removed from message `.google.cloud.cloudsecuritycompliance.v1.Framework`
* An existing message `CloudControlGroup` is removed
* An existing message `Control` is removed
* An existing message `ControlFamily` is removed
* An existing field `cc_deployments` is removed from message `.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment`
* An existing field `cc_group_deployments` is removed from message `.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment`
* An existing message `CloudControlGroupDeployment` is removed

### Features

* removed some fields which are not required in Compliance Manager APIs ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))


### Bug Fixes

* An existing enum `RegulatoryControlResponsibilityType` is removed ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing field `cc_deployments` is removed from message `.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment` ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing field `cc_group_deployments` is removed from message `.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment` ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing field `cloud_control_group_details` is removed from message `.google.cloud.cloudsecuritycompliance.v1.Framework` ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing message `CloudControlGroup` is removed ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing message `CloudControlGroupDeployment` is removed ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing message `CloudControlGroupDetails` is removed ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing message `Control` is removed ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))
* An existing message `ControlFamily` is removed ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))


### Documentation

* updated documentation for APIs ([6842396](https://github.com/googleapis/google-cloud-python/commit/6842396f3662264aa1beca9a5a08f9d0f171483a))

## 0.1.0 (2025-09-04)


### Features

* add initial files for google.cloud.cloudsecuritycompliance.v1 ([#14334](https://github.com/googleapis/google-cloud-python/issues/14334)) ([65668ef](https://github.com/googleapis/google-cloud-python/commit/65668ef8d9e1015609410caa8f67d9f00f322626))

## Changelog
