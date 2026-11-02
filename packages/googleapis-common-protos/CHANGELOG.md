# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/googleapis-common-protos/#history

## [1.76.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.75.5...googleapis-common-protos-v1.76.0) (2026-10-22)


### Features

* declare support for Python 3.15 ([#18737](https://github.com/googleapis/google-cloud-python/issues/18737)) ([65c8767](https://github.com/googleapis/google-cloud-python/commit/65c87678e7a63aa4c8115c9273581aa5db82fbe9))
* update API sources and regenerate ([#18797](https://github.com/googleapis/google-cloud-python/issues/18797)) ([be4d954](https://github.com/googleapis/google-cloud-python/commit/be4d954baf9a27cad04637183047b156afa4784a))

## [1.75.5](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.75.4...googleapis-common-protos-v1.75.5) (2026-09-29)


### Bug Fixes

* resolve error where google/longrunning/operations.proto is missing ([#18477](https://github.com/googleapis/google-cloud-python/issues/18477)) ([e1d306a](https://github.com/googleapis/google-cloud-python/commit/e1d306a5e0213f99e2c9d740a25622f006e3bb46)), refs [#18478](https://github.com/googleapis/google-cloud-python/issues/18478)

## [1.75.4](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.75.3...googleapis-common-protos-v1.75.4) (2026-09-24)


### Bug Fixes

* regenerate gencode with protobuf 6.33.5 ([#18461](https://github.com/googleapis/google-cloud-python/issues/18461)) ([9cb21d0](https://github.com/googleapis/google-cloud-python/commit/9cb21d0053a21366b564a7cf3858a3baa03c6659))

## [1.75.3](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.75.2...googleapis-common-protos-v1.75.3) (2026-09-03)


### Bug Fixes

* **googleapis-common-protos:** remove deprecated license classifier ([#18242](https://github.com/googleapis/google-cloud-python/issues/18242)) ([6f0216a](https://github.com/googleapis/google-cloud-python/commit/6f0216a2dc492236c80822de4439c8ab2c6bd9be)), refs [#18235](https://github.com/googleapis/google-cloud-python/issues/18235)

## [1.75.2](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.75.1...googleapis-common-protos-v1.75.2) (2026-08-21)


### Documentation

* **django-spanner, common-protos:** centralize CONTRIBUTING.rst pointers ([#18041](https://github.com/googleapis/google-cloud-python/issues/18041)) ([2b056ab](https://github.com/googleapis/google-cloud-python/commit/2b056ab2788411bb555c6697a94d76c83ca2a863))

## [1.75.1](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.75.0...googleapis-common-protos-v1.75.1) (2026-08-06)


### Bug Fixes

* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [1.75.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.74.0...googleapis-common-protos-v1.75.0) (2026-05-06)

## [1.74.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.73.1...googleapis-common-protos-v1.74.0) (2026-04-02)


### Documentation

* update SelectiveGapicGeneration usage doc ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* update API common type documentation ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* update various comments ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* update license year ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* fix documentation formatting ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))


### Features

* add origin to AttributeContext.Request ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* publish client batch config schema ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* publish new error reasons ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))

## [1.73.1](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.73.0...googleapis-common-protos-v1.73.1) (2026-03-26)


### Documentation

* Update changelog entry for release (#16093) ([51a96200324965f071dd9542d25b907c1420b3f6](https://github.com/googleapis/google-cloud-python/commit/51a96200324965f071dd9542d25b907c1420b3f6))


### Bug Fixes

* Allow Protobuf 7.x, require Python 3.9 (#16102) ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))
* Require Python 3.9 ([ec9262c45055d3d2b596cdde1649d3ce90b4347d](https://github.com/googleapis/google-cloud-python/commit/ec9262c45055d3d2b596cdde1649d3ce90b4347d))

## [1.73.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.72.0...googleapis-common-protos-v1.73.0) (2026-03-05)


### Chores

* code formatting (#16023) ([6120fb0db084f5e8d1502fb1bb37594ac9976f6e](https://github.com/googleapis/google-cloud-python/commit/6120fb0db084f5e8d1502fb1bb37594ac9976f6e))

## [1.72.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.71.0...googleapis-common-protos-v1.72.0) (2025-11-06)


### Features

* add common_resources.proto (#14851) ([e4e0e2a93c3db14324c1d9f799283ffe4f2bec09](https://github.com/googleapis/google-cloud-python/commit/e4e0e2a93c3db14324c1d9f799283ffe4f2bec09))
* add field api_version to message ServiceForTransport (#14843) ([81812fde4f1e43d568d53d6a993cf423b38d6728](https://github.com/googleapis/google-cloud-python/commit/81812fde4f1e43d568d53d6a993cf423b38d6728))

## [1.71.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.70.0...googleapis-common-protos-v1.71.0) (2025-10-20)


### Features

* add support for Python 3.14 (#14699) Towards b/375664027 ([8b69540bf6fd862bc1aebb3baf423c419b1556d4](https://github.com/googleapis/google-cloud-python/commit/8b69540bf6fd862bc1aebb3baf423c419b1556d4))

## [1.70.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.69.2...googleapis-common-protos-v1.70.0) (2025-04-12)


### Features

* expand QuotaFailure with quota error details ([#13745](https://github.com/googleapis/google-cloud-python/issues/13745)) ([5535afe](https://github.com/googleapis/google-cloud-python/commit/5535afe64021ce9688dd95742af201edb402dcf0))

## [1.69.2](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.69.1...googleapis-common-protos-v1.69.2) (2025-03-15)


### Bug Fixes

* Allow protobuf 6.x ([b4d4551](https://github.com/googleapis/google-cloud-python/commit/b4d45514e4ab630334a54eb4201576062ecc1958))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))
* resolve issue where pre-release versions of dependencies are installed ([b4d4551](https://github.com/googleapis/google-cloud-python/commit/b4d45514e4ab630334a54eb4201576062ecc1958))
* set `include` in `tool.setuptools.packages.find` ([#13662](https://github.com/googleapis/google-cloud-python/issues/13662)) ([c6a1588](https://github.com/googleapis/google-cloud-python/commit/c6a158821fad0f102d69b53781df3135c7483b31))

## [1.69.1](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.69.0...googleapis-common-protos-v1.69.1) (2025-03-06)


### Bug Fixes

* exclude docs in tool.setuptools.packages.find ([#13607](https://github.com/googleapis/google-cloud-python/issues/13607)) ([1e4de9d](https://github.com/googleapis/google-cloud-python/commit/1e4de9d50950c7536f428d96775d81cefdda1d9b))
* restore *.proto files removed in version 1.67.0 ([#13614](https://github.com/googleapis/google-cloud-python/issues/13614)) ([323a503](https://github.com/googleapis/google-cloud-python/commit/323a503b69afcb23eababa0a0b21232a02c0f1f3))

## [1.69.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.68.0...googleapis-common-protos-v1.69.0) (2025-03-03)


### Features

* migrate to pyproject.toml ([#13551](https://github.com/googleapis/google-cloud-python/issues/13551)) ([7dda4d0](https://github.com/googleapis/google-cloud-python/commit/7dda4d0b94038444911a9796d74649bea2216a35))

## [1.68.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.67.0...googleapis-common-protos-v1.68.0) (2025-02-18)


### Features

* A new field `unversioned_package_disabled` is added to message `.google.api.PythonSettings` ([eb554e8](https://github.com/googleapis/google-cloud-python/commit/eb554e89424f02ea1db58904c6685a90fca6dbab))
* Add field `experimental_features` to message `PythonSettings` ([#249](https://github.com/googleapis/google-cloud-python/issues/249)) ([ba8d36e](https://github.com/googleapis/google-cloud-python/commit/ba8d36e4a288c57be235c8597e11208359b072b5))
* add FieldInfo.referenced_types for generics ([#247](https://github.com/googleapis/google-cloud-python/issues/247)) ([c91900a](https://github.com/googleapis/google-cloud-python/commit/c91900ab232e542905cd4f3cf282677bc6bcaab3))
* add support for field generate_omitted_as_internal in selective gapic generation ([#13482](https://github.com/googleapis/google-cloud-python/issues/13482)) ([993ff4d](https://github.com/googleapis/google-cloud-python/commit/993ff4db8ae64ab1ca1b45de2caf118effb003af))


### Documentation

* A comment for field `content` in message `.google.api.Page` is changed ([eb554e8](https://github.com/googleapis/google-cloud-python/commit/eb554e89424f02ea1db58904c6685a90fca6dbab))
* A comment for message `RoutingRule` is changed ([eb554e8](https://github.com/googleapis/google-cloud-python/commit/eb554e89424f02ea1db58904c6685a90fca6dbab))

## [1.67.0](https://github.com/googleapis/google-cloud-python/compare/googleapis-common-protos-v1.66.0...googleapis-common-protos-v1.67.0) (2025-02-12)


### Features

* A new field `unversioned_package_disabled` is added to message `.google.api.PythonSettings` ([eb554e8](https://github.com/googleapis/google-cloud-python/commit/eb554e89424f02ea1db58904c6685a90fca6dbab))
* add support for field generate_omitted_as_internal in selective gapic generation ([#13482](https://github.com/googleapis/google-cloud-python/issues/13482)) ([993ff4d](https://github.com/googleapis/google-cloud-python/commit/993ff4db8ae64ab1ca1b45de2caf118effb003af))


### Documentation

* A comment for field `content` in message `.google.api.Page` is changed ([eb554e8](https://github.com/googleapis/google-cloud-python/commit/eb554e89424f02ea1db58904c6685a90fca6dbab))
* A comment for message `RoutingRule` is changed ([eb554e8](https://github.com/googleapis/google-cloud-python/commit/eb554e89424f02ea1db58904c6685a90fca6dbab))

## [1.66.0](https://github.com/googleapis/python-api-common-protos/compare/v1.65.0...v1.66.0) (2024-11-12)


### Features

* Add `MISSING_ORIGIN` and `OVERLOADED_CREDENTIALS` to `ErrorReason` enum ([d0478d8](https://github.com/googleapis/python-api-common-protos/commit/d0478d8beacb6c53aa29aa0ac14b949421de8112))
* Add field `protobuf_pythonic_types_enabled` to `ExperimentalFeatures` message ([d0478d8](https://github.com/googleapis/python-api-common-protos/commit/d0478d8beacb6c53aa29aa0ac14b949421de8112))
* Add field `selective_gapic_generation` to `CommonLanguageSettings` message ([d0478d8](https://github.com/googleapis/python-api-common-protos/commit/d0478d8beacb6c53aa29aa0ac14b949421de8112))
* Add field `time_series_resource_hierarchy_level` to `MetricDescriptorMetadata` message ([d0478d8](https://github.com/googleapis/python-api-common-protos/commit/d0478d8beacb6c53aa29aa0ac14b949421de8112))
* Add message `SelectiveGapicGeneration` ([d0478d8](https://github.com/googleapis/python-api-common-protos/commit/d0478d8beacb6c53aa29aa0ac14b949421de8112))

## [1.65.0](https://github.com/googleapis/python-api-common-protos/compare/v1.64.0...v1.65.0) (2024-08-27)


### Features

* Add field `experimental_features` to message `PythonSettings` ([#249](https://github.com/googleapis/python-api-common-protos/issues/249)) ([139490f](https://github.com/googleapis/python-api-common-protos/commit/139490fedcebf1a6674d9cf058226e6814208619))

## [1.64.0](https://github.com/googleapis/python-api-common-protos/compare/v1.63.2...v1.64.0) (2024-08-26)


### Features

* Add FieldInfo.referenced_types for generics ([2ba3577](https://github.com/googleapis/python-api-common-protos/commit/2ba35774cb6ea31513b1985e3a391c5c3435e7be))


### Bug Fixes

* Un-deprecate Endpoint.aliases field ([2ba3577](https://github.com/googleapis/python-api-common-protos/commit/2ba35774cb6ea31513b1985e3a391c5c3435e7be))


### Documentation

* Fix formatting in http.proto comments ([2ba3577](https://github.com/googleapis/python-api-common-protos/commit/2ba35774cb6ea31513b1985e3a391c5c3435e7be))
* Improve MethodSettings selector examples ([2ba3577](https://github.com/googleapis/python-api-common-protos/commit/2ba35774cb6ea31513b1985e3a391c5c3435e7be))
* Reformat comments in context proto ([2ba3577](https://github.com/googleapis/python-api-common-protos/commit/2ba35774cb6ea31513b1985e3a391c5c3435e7be))
* Update ResourceDescriptor.plural docs with AIP-122 nested collections guidance ([2ba3577](https://github.com/googleapis/python-api-common-protos/commit/2ba35774cb6ea31513b1985e3a391c5c3435e7be))

## [1.63.2](https://github.com/googleapis/python-api-common-protos/compare/v1.63.1...v1.63.2) (2024-06-19)


### Bug Fixes

* **deps:** Require protobuf&gt;=3.20.2 ([c77c0dc](https://github.com/googleapis/python-api-common-protos/commit/c77c0dc5d29ef780d781a3c5d757736a9ed09674))
* Regenerate pb2 files for compatibility with protobuf 5.x ([c77c0dc](https://github.com/googleapis/python-api-common-protos/commit/c77c0dc5d29ef780d781a3c5d757736a9ed09674))

## [1.63.1](https://github.com/googleapis/python-api-common-protos/compare/v1.63.0...v1.63.1) (2024-05-30)


### Bug Fixes

* Increase upper limit for protobuf 5.X versions ([#212](https://github.com/googleapis/python-api-common-protos/issues/212)) ([28fc17a](https://github.com/googleapis/python-api-common-protos/commit/28fc17a9208aa98782acc6bee6c40ec12b959706))

## [1.63.0](https://github.com/googleapis/python-api-common-protos/compare/v1.62.0...v1.63.0) (2024-03-08)


### Features

* Add `api_version` field to `ServiceOptions` in `google/api/client.proto` ([6f9c4d2](https://github.com/googleapis/python-api-common-protos/commit/6f9c4d2b4b787d9ed2b447d7b99281aa3dcf97b5))
* Add `LOCATION_POLICY_VIOLATED` enum to `ErrorReason` in `google/api/error_reason.proto` ([6f9c4d2](https://github.com/googleapis/python-api-common-protos/commit/6f9c4d2b4b787d9ed2b447d7b99281aa3dcf97b5))
* Add `rest_reference_documentation_uri` field to `ServiceOptions` in `google/api/client.proto` ([6f9c4d2](https://github.com/googleapis/python-api-common-protos/commit/6f9c4d2b4b787d9ed2b447d7b99281aa3dcf97b5))

## [1.62.0](https://github.com/googleapis/python-api-common-protos/compare/v1.61.0...v1.62.0) (2023-12-01)


### Features

* Add `auto_populated_fields` field of `MethodSettings` in `google/api/client_pb2` ([#194](https://github.com/googleapis/python-api-common-protos/issues/194)) ([4b0c73a](https://github.com/googleapis/python-api-common-protos/commit/4b0c73a40f9bf5337fe451c0210f73eadd196b99))
* Add support for Python 3.12 ([#192](https://github.com/googleapis/python-api-common-protos/issues/192)) ([336cdf3](https://github.com/googleapis/python-api-common-protos/commit/336cdf351d4e87891d735837817d2cfc4e5a9fc7))


### Bug Fixes

* Migrate to native namespace packages ([#187](https://github.com/googleapis/python-api-common-protos/issues/187)) ([713e388](https://github.com/googleapis/python-api-common-protos/commit/713e3887a3293aea314060e84bdcf8a12eda3d6c))

## [1.61.0](https://github.com/googleapis/python-api-common-protos/compare/v1.60.0...v1.61.0) (2023-10-09)


### Features

* Add `google/api/field_info.proto` ([2d39f37](https://github.com/googleapis/python-api-common-protos/commit/2d39f37212fe886b3029e1043ca28789e2d66876))
* Add `IDENTIFIER` to `FieldBehavior` enum ([2d39f37](https://github.com/googleapis/python-api-common-protos/commit/2d39f37212fe886b3029e1043ca28789e2d66876))

## [1.60.0](https://github.com/googleapis/python-api-common-protos/compare/v1.59.1...v1.60.0) (2023-07-27)


### Features

* Add `google/api/policy.proto` ([b2cb5c2](https://github.com/googleapis/python-api-common-protos/commit/b2cb5c257ae8d0869d33581b116995620ddae0b2))
* Add `method_policies` to `Control` ([b2cb5c2](https://github.com/googleapis/python-api-common-protos/commit/b2cb5c257ae8d0869d33581b116995620ddae0b2))

## [1.59.1](https://github.com/googleapis/python-api-common-protos/compare/v1.59.0...v1.59.1) (2023-06-06)


### Bug Fixes

* Invalid `dev` version identifiers in `setup.py` ([#166](https://github.com/googleapis/python-api-common-protos/issues/166)) ([c38e03a](https://github.com/googleapis/python-api-common-protos/commit/c38e03aa06eedf65373c283f16e7bbbd5622f37b)), closes [#165](https://github.com/googleapis/python-api-common-protos/issues/165)

## [1.59.0](https://github.com/googleapis/python-api-common-protos/compare/v1.58.0...v1.59.0) (2023-03-20)


### Features

* Add overrides_by_request_protocol to BackendRule in google/api/backend.proto ([77376dd](https://github.com/googleapis/python-api-common-protos/commit/77376dd02af0a1c9255a50516550d2474536fa9d))
* Add proto_reference_documentation_uri to Publishing in google/api/client.proto ([77376dd](https://github.com/googleapis/python-api-common-protos/commit/77376dd02af0a1c9255a50516550d2474536fa9d))
* Add SERVICE_NOT_VISIBLE and GCP_SUSPENDED to ErrorReason in google/api/error_reason.proto ([77376dd](https://github.com/googleapis/python-api-common-protos/commit/77376dd02af0a1c9255a50516550d2474536fa9d))


### Documentation

* Use rst syntax in readme  ([77376dd](https://github.com/googleapis/python-api-common-protos/commit/77376dd02af0a1c9255a50516550d2474536fa9d))

## [1.58.0](https://github.com/googleapis/python-api-common-protos/compare/v1.57.1...v1.58.0) (2023-01-06)


### Features

* Add google/rpc/context/audit_context.proto ([41f1529](https://github.com/googleapis/python-api-common-protos/commit/41f1529500e535ec83e2d72f8e97dfda5469cb72))
* Add google/rpc/http.proto ([41f1529](https://github.com/googleapis/python-api-common-protos/commit/41f1529500e535ec83e2d72f8e97dfda5469cb72))

## [1.57.1](https://github.com/googleapis/python-api-common-protos/compare/v1.57.0...v1.57.1) (2022-12-08)


### Bug Fixes

* Mark reference_docs_uri field in google/api/client.proto as deprecated ([#150](https://github.com/googleapis/python-api-common-protos/issues/150)) ([52b5018](https://github.com/googleapis/python-api-common-protos/commit/52b5018abf0902a1e582a406c993b51e0d2aa3cd))

## [1.57.0](https://github.com/googleapis/python-api-common-protos/compare/v1.56.4...v1.57.0) (2022-11-15)


### Features

* Add support for Python 3.10 ([#143](https://github.com/googleapis/python-api-common-protos/issues/143)) ([63ca888](https://github.com/googleapis/python-api-common-protos/commit/63ca888512be84508fcf95e4d5d40df036a85e18))
* Add support for Python 3.11 ([#145](https://github.com/googleapis/python-api-common-protos/issues/145)) ([b9dbb21](https://github.com/googleapis/python-api-common-protos/commit/b9dbb219ea46abd9851af1fc41ea37f9d5631c0b))
* added google.api.JwtLocation.cookie ([6af2132](https://github.com/googleapis/python-api-common-protos/commit/6af21322879cba158e0a5992c9799e68c1744fac))
* added google.api.Service.publishing and client libraries settings ([6af2132](https://github.com/googleapis/python-api-common-protos/commit/6af21322879cba158e0a5992c9799e68c1744fac))
* new fields in enum google.api.ErrorReason ([6af2132](https://github.com/googleapis/python-api-common-protos/commit/6af21322879cba158e0a5992c9799e68c1744fac))


### Bug Fixes

* deprecate google.api.BackendRule.min_deadline ([6af2132](https://github.com/googleapis/python-api-common-protos/commit/6af21322879cba158e0a5992c9799e68c1744fac))
* **deps:** Require protobuf &gt;=3.19.5 ([#141](https://github.com/googleapis/python-api-common-protos/issues/141)) ([9ea3530](https://github.com/googleapis/python-api-common-protos/commit/9ea3530b459269e964fcc98db1c5025e05d6495f))


### Documentation

* minor updates to comments ([6af2132](https://github.com/googleapis/python-api-common-protos/commit/6af21322879cba158e0a5992c9799e68c1744fac))

## [1.56.4](https://github.com/googleapis/python-api-common-protos/compare/v1.56.3...v1.56.4) (2022-07-12)


### Bug Fixes

* require python 3.7+ ([#119](https://github.com/googleapis/python-api-common-protos/issues/119)) ([507b58d](https://github.com/googleapis/python-api-common-protos/commit/507b58dfa0516aedf57880b384e92cda97152398))

## [1.56.3](https://github.com/googleapis/python-api-common-protos/compare/v1.56.2...v1.56.3) (2022-06-21)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#112](https://github.com/googleapis/python-api-common-protos/issues/112)) ([67b0231](https://github.com/googleapis/python-api-common-protos/commit/67b02313bf47d86ac84917756ff026e331665637))


### Documentation

* fix changelog header to consistent size ([#108](https://github.com/googleapis/python-api-common-protos/issues/108)) ([d315b9f](https://github.com/googleapis/python-api-common-protos/commit/d315b9f23f5dbbce27c965a2b692a8d1dcf03d60))

## [1.56.2](https://github.com/googleapis/python-api-common-protos/compare/v1.56.1...v1.56.2) (2022-05-26)


### Bug Fixes

* **deps:** require grpcio >= 1.0.0, <2.0.0dev ([4a402ce](https://github.com/googleapis/python-api-common-protos/commit/4a402ce798c8364679e69eefdaadcf61fc289308))
* **deps:** require protobuf>= 3.15.0, <4.0.0dev ([#105](https://github.com/googleapis/python-api-common-protos/issues/105)) ([4a402ce](https://github.com/googleapis/python-api-common-protos/commit/4a402ce798c8364679e69eefdaadcf61fc289308))

## [1.56.1](https://github.com/googleapis/python-api-common-protos/compare/v1.56.0...v1.56.1) (2022-05-05)


### Bug Fixes

* **deps:** require protobuf >=1.15.0 ([f04ed64](https://github.com/googleapis/python-api-common-protos/commit/f04ed64b233e1ff95370ef412ad5ecb92cb5780e))
* include tests directory ([#103](https://github.com/googleapis/python-api-common-protos/issues/103)) ([72e5df1](https://github.com/googleapis/python-api-common-protos/commit/72e5df15ce63012f7d5c7781a51687e85a2cf63c))
* regenerate pb2 files using the latest version of grpcio-tools ([f04ed64](https://github.com/googleapis/python-api-common-protos/commit/f04ed64b233e1ff95370ef412ad5ecb92cb5780e))

## [1.56.0](https://github.com/googleapis/python-api-common-protos/compare/v1.55.0...v1.56.0) (2022-03-17)


### Features

* add google/api/error_reason.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))
* add google/api/visibility.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))
* add google/type/decimal.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))
* add google/type/interval.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))
* add google/type/localized_text.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))
* add google/type/phone_number.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))
* update all protos and pb2 files ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))


### Bug Fixes

* expose all names in longrunning _pb2's ([#90](https://github.com/googleapis/python-api-common-protos/issues/90)) ([09e9ccd](https://github.com/googleapis/python-api-common-protos/commit/09e9ccd86c21dceb3a5add66cc4bf5009cb255a9))
* re-generate pb2 files ([#87](https://github.com/googleapis/python-api-common-protos/issues/87)) ([6260547](https://github.com/googleapis/python-api-common-protos/commit/6260547506f122ca9ee833aca0669d1650304a11))
* re-generate pb2 files using grpcio-tools<1.44.0 ([#93](https://github.com/googleapis/python-api-common-protos/issues/93)) ([76bb9f6](https://github.com/googleapis/python-api-common-protos/commit/76bb9f66f9674ad4c3a7fdc8812dadfb25b170a6))
* remove deprecated fields `aliases` and `features` from google/api/endpoint.proto ([62c04b8](https://github.com/googleapis/python-api-common-protos/commit/62c04b83ef9ce972760407d8e9e9e0d77bbb071c))

## [1.55.0](https://github.com/googleapis/python-api-common-protos/compare/v1.54.0...v1.55.0) (2022-02-15)


### Features

* add location proto files. ([#84](https://github.com/googleapis/python-api-common-protos/issues/84)) ([9a33e56](https://github.com/googleapis/python-api-common-protos/commit/9a33e56ac6a07a2e717edc55a39fa7cf2f9eec15))

## [1.54.0](https://www.github.com/googleapis/python-api-common-protos/compare/v1.53.0...v1.54.0) (2021-12-07)


### Features

* add extended_operations.proto ([#77](https://www.github.com/googleapis/python-api-common-protos/issues/77)) ([bc85849](https://www.github.com/googleapis/python-api-common-protos/commit/bc85849e21494b267d87cd6dc5d0a0e23e012470))
* add google/api/routing.proto ([#75](https://www.github.com/googleapis/python-api-common-protos/issues/75)) ([1ae0bbc](https://www.github.com/googleapis/python-api-common-protos/commit/1ae0bbcc9747af4dd467e7a246c1a2a4cd5ef2ec))

## [1.53.0](https://www.github.com/googleapis/python-api-common-protos/compare/v1.52.0...v1.53.0) (2021-02-25)


### Features

* add `google.api.ResourceDescriptor.Style` ([4ce679c](https://www.github.com/googleapis/python-api-common-protos/commit/4ce679cd49771946bf781108e92e07cdf04a61eb))
* add API method signatures to longrunning operations ([8de7ae2](https://www.github.com/googleapis/python-api-common-protos/commit/8de7ae28dfe5dd4d0cb99dd3b89a8f1e614bbe6d))
* add gapic_metadata_pb2 ([#38](https://www.github.com/googleapis/python-api-common-protos/issues/38)) ([8de7ae2](https://www.github.com/googleapis/python-api-common-protos/commit/8de7ae28dfe5dd4d0cb99dd3b89a8f1e614bbe6d))
* add UNORDERED_LIST to field options ([8de7ae2](https://www.github.com/googleapis/python-api-common-protos/commit/8de7ae28dfe5dd4d0cb99dd3b89a8f1e614bbe6d))
* add WaitOperation method to longrunning operations ([8de7ae2](https://www.github.com/googleapis/python-api-common-protos/commit/8de7ae28dfe5dd4d0cb99dd3b89a8f1e614bbe6d))
* require python >=3.6 and   ([#31](https://www.github.com/googleapis/python-api-common-protos/issues/31)) ([4ce679c](https://www.github.com/googleapis/python-api-common-protos/commit/4ce679cd49771946bf781108e92e07cdf04a61eb))


### Bug Fixes

* add `create_key` to FieldDescriptors ([4ce679c](https://www.github.com/googleapis/python-api-common-protos/commit/4ce679cd49771946bf781108e92e07cdf04a61eb))
* Generate gRPC files for long-running operations ([#13](https://www.github.com/googleapis/python-api-common-protos/issues/13)) ([a9ce288](https://www.github.com/googleapis/python-api-common-protos/commit/a9ce28840ddfec712da5b296f43e6c3131840db4))


### Documentation

* add link to PyPI ([#10](https://www.github.com/googleapis/python-api-common-protos/issues/10)) ([3f79402](https://www.github.com/googleapis/python-api-common-protos/commit/3f7940226b0e22aef31b82c8dc2196aa25b48a3f))

## [1.53.0dev1](https://www.github.com/googleapis/python-api-common-protos/compare/v1.52.0...v1.53.0dev1) (2021-01-27)


### Features

* add `google.api.ResourceDescriptor.Style` ([4ce679c](https://www.github.com/googleapis/python-api-common-protos/commit/4ce679cd49771946bf781108e92e07cdf04a61eb))
* require python >=3.6 and   ([#31](https://www.github.com/googleapis/python-api-common-protos/issues/31)) ([4ce679c](https://www.github.com/googleapis/python-api-common-protos/commit/4ce679cd49771946bf781108e92e07cdf04a61eb))


### Bug Fixes

* add `create_key` to FieldDescriptors ([4ce679c](https://www.github.com/googleapis/python-api-common-protos/commit/4ce679cd49771946bf781108e92e07cdf04a61eb))
* Generate gRPC files for long-running operations ([#13](https://www.github.com/googleapis/python-api-common-protos/issues/13)) ([a9ce288](https://www.github.com/googleapis/python-api-common-protos/commit/a9ce28840ddfec712da5b296f43e6c3131840db4))


### Documentation

* add link to PyPI ([#10](https://www.github.com/googleapis/python-api-common-protos/issues/10)) ([3f79402](https://www.github.com/googleapis/python-api-common-protos/commit/3f7940226b0e22aef31b82c8dc2196aa25b48a3f))

## 1.52.0 (2020-06-04)


### Features

* create api-common-protos repo for python common protos ([4ef4b0d](https://www.github.com/googleapis/python-api-common-protos/commit/4ef4b0d177136bfbd19f4c00ccf2f6d7eaccb153))
