# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-recaptcha-enterprise/#history

## [1.34.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.33.0...google-cloud-recaptcha-enterprise-v1.34.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.33.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.32.0...google-cloud-recaptcha-enterprise-v1.33.0) (2026-08-21)


### Features

* update googleapis and regenerate ([#18087](https://github.com/googleapis/google-cloud-python/issues/18087)) ([db1622a](https://github.com/googleapis/google-cloud-python/commit/db1622a9cfac112b40c93842737d7a5deeb3e8bd))

## [1.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.31.0...google-cloud-recaptcha-enterprise-v1.32.0) (2026-06-22)


### Features

* regenerate google-cloud-[o-r] packages ([#17075](https://github.com/googleapis/google-cloud-python/issues/17075)) ([f4bd018](https://github.com/googleapis/google-cloud-python/commit/f4bd0182d808ae73c3c6981e6ce3d565f78a6051))

## [1.31.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.30.0...google-cloud-recaptcha-enterprise-v1.31.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.29.0...google-cloud-recaptcha-enterprise-v1.30.0) (2026-01-09)


### Documentation

* clarify that WafFeature.EXPRESS is deprecated ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* document domain, package name and bundle id limits and validation ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))


### Features

* add verifiedBots field to RiskAnalysis and definitions for a Bot object to store metadata for a detected bot ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* add risk reasons to FraudPreventionAssessment ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* add a POLICY_BASED_CHALLENGE IntegrationType and associated settings ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* Add `phone_authentication_event` to `AnnotateAssessmentRequest`. This new field allows you to indicate the phone number associated with a multi-factor authentication event, i.e. `INITIATED_TWO_FACTOR`, `PASSED_TWO_FACTOR`, `FAILED_TWO_FACTOR` reasons, and the time of such an event ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.28.2...google-cloud-recaptcha-enterprise-v1.29.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.28.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.28.1...google-cloud-recaptcha-enterprise-v1.28.2) (2025-06-11)


### Documentation

* Update import statement example in README ([dfc2cd6](https://github.com/googleapis/google-cloud-python/commit/dfc2cd6be6422baa45dcebc5ff6e7fc846bf5c7d))

## [1.28.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.28.0...google-cloud-recaptcha-enterprise-v1.28.1) (2025-03-19)


### Documentation

* [google-cloud-recaptcha-enterprise] fix typo in ([4247899](https://github.com/googleapis/google-cloud-python/commit/424789974b4aba88918035cc14e158839da931e8))

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.27.0...google-cloud-recaptcha-enterprise-v1.28.0) (2025-03-15)


### Features

* [google-cloud-recaptcha-enterprise] A new field `ja4` is added to message `Event` ([#13645](https://github.com/googleapis/google-cloud-python/issues/13645)) ([885dc9c](https://github.com/googleapis/google-cloud-python/commit/885dc9cf70e47796a57ee12cfd7a3b9d066ee65c))


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([7295cbb](https://github.com/googleapis/google-cloud-python/commit/7295cbb7c3122eeff1042c3c543bfc9b8b3ca913))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))


### Documentation

* update documentation ([885dc9c](https://github.com/googleapis/google-cloud-python/commit/885dc9cf70e47796a57ee12cfd7a3b9d066ee65c))

## [1.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.26.1...google-cloud-recaptcha-enterprise-v1.27.0) (2025-02-18)


### Features

* Add REST Interceptors which support reading metadata ([c8e0760](https://github.com/googleapis/google-cloud-python/commit/c8e0760e8088950c62279335216ad1d17716ce59))
* Add support for reading selective GAPIC generation methods from service YAML ([c8e0760](https://github.com/googleapis/google-cloud-python/commit/c8e0760e8088950c62279335216ad1d17716ce59))

## [1.26.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.26.0...google-cloud-recaptcha-enterprise-v1.26.1) (2025-01-13)


### Documentation

* [google-cloud-recaptcha-enterprise] Update docs for FraudPrevention field in CreateAssessment ([#13403](https://github.com/googleapis/google-cloud-python/issues/13403)) ([ee59d69](https://github.com/googleapis/google-cloud-python/commit/ee59d691c71b57b591edce7dc3beb8c58020d62c))
* challenge is also returned for INVISIBLE keys ([ee59d69](https://github.com/googleapis/google-cloud-python/commit/ee59d691c71b57b591edce7dc3beb8c58020d62c))

## [1.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.25.0...google-cloud-recaptcha-enterprise-v1.26.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([8e6b0cc](https://github.com/googleapis/google-cloud-python/commit/8e6b0cca8709ae8c7f0c722c5ebf0707358d3359))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([8e6b0cc](https://github.com/googleapis/google-cloud-python/commit/8e6b0cca8709ae8c7f0c722c5ebf0707358d3359))


### Documentation

* [google-cloud-recaptcha-enterprise] challenge is also returned for INVISIBLE keys ([#13312](https://github.com/googleapis/google-cloud-python/issues/13312)) ([adea041](https://github.com/googleapis/google-cloud-python/commit/adea041c1d43b94d11ff9d4d5ba13c0d7898cac2))

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.24.1...google-cloud-recaptcha-enterprise-v1.25.0) (2024-11-14)


### Features

* A new enum `Challenge` is added ([511d7cc](https://github.com/googleapis/google-cloud-python/commit/511d7cc4bf1bb5eec1709aab5a836d37b26ff029))
* A new field `challenge` is added to message `.google.cloud.recaptchaenterprise.v1.RiskAnalysis` ([511d7cc](https://github.com/googleapis/google-cloud-python/commit/511d7cc4bf1bb5eec1709aab5a836d37b26ff029))

## [1.24.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.24.0...google-cloud-recaptcha-enterprise-v1.24.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13245](https://github.com/googleapis/google-cloud-python/issues/13245)) ([875f712](https://github.com/googleapis/google-cloud-python/commit/875f712265a36919409964f5ade218330f1d0147))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.23.0...google-cloud-recaptcha-enterprise-v1.24.0) (2024-10-31)


### Features

* enable Akamai web application firewall ([81bf6fe](https://github.com/googleapis/google-cloud-python/commit/81bf6fe826181c729ec756756d1bf315914a8fc4))
* support for ListIpOverrides and RemoveIpOverride ([81bf6fe](https://github.com/googleapis/google-cloud-python/commit/81bf6fe826181c729ec756756d1bf315914a8fc4))


### Documentation

* minor updates to reference documentation ([81bf6fe](https://github.com/googleapis/google-cloud-python/commit/81bf6fe826181c729ec756756d1bf315914a8fc4))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.22.1...google-cloud-recaptcha-enterprise-v1.23.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [1.22.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.22.0...google-cloud-recaptcha-enterprise-v1.22.1) (2024-09-03)


### Documentation

* minor doc fixes ([7e40c8c](https://github.com/googleapis/google-cloud-python/commit/7e40c8c40039e0c01ef9a8bfea8804edfee48d70))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.21.2...google-cloud-recaptcha-enterprise-v1.22.0) (2024-08-22)


### Features

* add `express_settings` to `Key` ([0b90478](https://github.com/googleapis/google-cloud-python/commit/0b90478bb70be96b304397fc433d2dbaf0160d30))
* add AddIpOverride RPC ([0b90478](https://github.com/googleapis/google-cloud-python/commit/0b90478bb70be96b304397fc433d2dbaf0160d30))


### Documentation

* clarify `Event.express` field ([0b90478](https://github.com/googleapis/google-cloud-python/commit/0b90478bb70be96b304397fc433d2dbaf0160d30))
* fix billing, quota, and usecase links ([0b90478](https://github.com/googleapis/google-cloud-python/commit/0b90478bb70be96b304397fc433d2dbaf0160d30))

## [1.21.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.21.1...google-cloud-recaptcha-enterprise-v1.21.2) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([42c4d04](https://github.com/googleapis/google-cloud-python/commit/42c4d04ee1362ba0ed0f1b6a134ac8e409875b63))

## [1.21.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.21.0...google-cloud-recaptcha-enterprise-v1.21.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12869](https://github.com/googleapis/google-cloud-python/issues/12869)) ([e42edbc](https://github.com/googleapis/google-cloud-python/commit/e42edbcf7f4d8ed66b6645c96a01c55fb8cd7666))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.20.0...google-cloud-recaptcha-enterprise-v1.21.0) (2024-06-27)


### Features

* [google-cloud-recaptcha-enterprise] added SMS Toll Fraud assessment ([#12838](https://github.com/googleapis/google-cloud-python/issues/12838)) ([386499f](https://github.com/googleapis/google-cloud-python/commit/386499fe11525d2646b79f9e41829b2c055f63b2))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.19.1...google-cloud-recaptcha-enterprise-v1.20.0) (2024-04-24)


### Features

* Add Fraud Prevention settings field ([5c373f6](https://github.com/googleapis/google-cloud-python/commit/5c373f6d82108b0c6548cd5d8fcacf4f025667be))

## [1.19.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.19.0...google-cloud-recaptcha-enterprise-v1.19.1) (2024-04-17)


### Documentation

* [google-cloud-recaptcha-enterprise] fixed the description of ListFirewallPoliciesResponse ([#12580](https://github.com/googleapis/google-cloud-python/issues/12580)) ([acdcb90](https://github.com/googleapis/google-cloud-python/commit/acdcb90c02a48af2190229172e50cf19aa0334b7))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.18.1...google-cloud-recaptcha-enterprise-v1.19.0) (2024-03-25)


### Features

* Add `CLOUDFLARE` enum to `WafService` message of firewalls supported by reCAPTCHA Enterprise ([#12498](https://github.com/googleapis/google-cloud-python/issues/12498)) ([ca58b4d](https://github.com/googleapis/google-cloud-python/commit/ca58b4db7cb8ea713a2fe7822b1299fbd90b528d))

## [1.18.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.18.0...google-cloud-recaptcha-enterprise-v1.18.1) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12386](https://github.com/googleapis/google-cloud-python/issues/12386)) ([edcad16](https://github.com/googleapis/google-cloud-python/commit/edcad1661973ae1677c69b3fc1c03c3069ec0e71))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.17.1...google-cloud-recaptcha-enterprise-v1.18.0) (2024-02-22)


### Features

* [google-cloud-recaptcha-enterprise] Add an API method for reordering firewall policies ([#12302](https://github.com/googleapis/google-cloud-python/issues/12302)) ([c48819c](https://github.com/googleapis/google-cloud-python/commit/c48819c7166f418fe450ec6f5abfc9c899c5bef8))


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12308](https://github.com/googleapis/google-cloud-python/issues/12308)) ([74dabeb](https://github.com/googleapis/google-cloud-python/commit/74dabebab206189e649ff6e00f3c7809d96c043b))
* fix ValueError in test__validate_universe_domain ([89c1b05](https://github.com/googleapis/google-cloud-python/commit/89c1b054f321b90ab4eed0139a3a2a79c369730d))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.17.0...google-cloud-recaptcha-enterprise-v1.17.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.16.1...google-cloud-recaptcha-enterprise-v1.17.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([4368029](https://github.com/googleapis/google-cloud-python/commit/436802904bfdafa7e90f94b128813506525e1605))

## [1.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.16.0...google-cloud-recaptcha-enterprise-v1.16.1) (2024-01-19)


### Documentation

* [google-cloud-recaptcha-enterprise] update comment for `AccountVerificationInfo.username` ([#12201](https://github.com/googleapis/google-cloud-python/issues/12201)) ([f7cd400](https://github.com/googleapis/google-cloud-python/commit/f7cd400be8b61d01904a950fbf7fa474325e4300))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.15.0...google-cloud-recaptcha-enterprise-v1.16.0) (2023-12-07)


### Features

* Add support for python 3.12 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* added stable account identifier to related group membership resources, and deprecated hashed identifier field ([f942e71](https://github.com/googleapis/google-cloud-python/commit/f942e71a6e014c62d521e954190746bc4d3455ca))
* Introduce compatibility with native namespace packages ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))
* Use `retry_async` instead of `retry` in async client ([9a629e1](https://github.com/googleapis/google-cloud-python/commit/9a629e1c9f7858f55c82ac21e60f22acf781db15))


### Documentation

* noted applicable fields as resource identifiers ([f942e71](https://github.com/googleapis/google-cloud-python/commit/f942e71a6e014c62d521e954190746bc4d3455ca))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.14.0...google-cloud-recaptcha-enterprise-v1.15.0) (2023-11-29)


### Features

* Added AnnotateAssessmentRequest.account_id  ([7d6ce5b](https://github.com/googleapis/google-cloud-python/commit/7d6ce5b49f9d1960cb3f4ffa8e7baf2e7ec126e2))
* Added Event.user_info ([7d6ce5b](https://github.com/googleapis/google-cloud-python/commit/7d6ce5b49f9d1960cb3f4ffa8e7baf2e7ec126e2))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.13.0...google-cloud-recaptcha-enterprise-v1.14.0) (2023-11-13)


### ⚠ BREAKING CHANGES

* Added required annotations

### Bug Fixes

* Added required annotations ([e8a00c4](https://github.com/googleapis/google-cloud-python/commit/e8a00c43318da1f260c837f9d6484384834c6705))


### Documentation

* CreateKeyRequest.display_name and PrivatePasswordLeakVerification.lookup_hash_prefix are now required ([e8a00c4](https://github.com/googleapis/google-cloud-python/commit/e8a00c43318da1f260c837f9d6484384834c6705))
* Updated comments explaining if a field is optional or required ([e8a00c4](https://github.com/googleapis/google-cloud-python/commit/e8a00c43318da1f260c837f9d6484384834c6705))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.12.2...google-cloud-recaptcha-enterprise-v1.13.0) (2023-10-05)


### Features

* added AndroidKeySettings.support_non_google_app_store_distribution ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added Assessment.firewall_policy_assessment, fraud_signals ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added FraudPreventionAssessment.behavioral_trust_verdict ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added FraudPreventionAssessment.behavioral_trust_verdict ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added IOSKeySettings.apple_developer_id ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added new fields to Event message ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added RiskAnalysis.extended_verdict_reasons ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added WafFeature.EXPRESS enum value ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* added WafService.FASTLY enum value ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))
* FirewallPolicy CRUD API ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))


### Documentation

* formatting of resource names ([84f4480](https://github.com/googleapis/google-cloud-python/commit/84f44807e374939750a23db53ca345f2e24874c1))

## [1.12.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.12.1...google-cloud-recaptcha-enterprise-v1.12.2) (2023-09-19)


### Documentation

* Minor formatting ([025219f](https://github.com/googleapis/google-cloud-python/commit/025219f5c04803651e20eae4c0186b87608f4db4))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.12.0...google-cloud-recaptcha-enterprise-v1.12.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11448](https://github.com/googleapis/google-cloud-python/issues/11448)) ([4d2c35a](https://github.com/googleapis/google-cloud-python/commit/4d2c35a1cd0b68b6d481d5611ff820451273e859))

## [1.12.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.11.1...v1.12.0) (2023-03-23)


### Features

* Add reCAPTCHA Enterprise Fraud Prevention API ([#350](https://github.com/googleapis/python-recaptcha-enterprise/issues/350)) ([5f841d7](https://github.com/googleapis/python-recaptcha-enterprise/commit/5f841d782c6e5ef3f4e5f4a9fa36a96d13e5849a))


### Documentation

* Fix formatting of request arg in docstring ([#352](https://github.com/googleapis/python-recaptcha-enterprise/issues/352)) ([a0ab5c3](https://github.com/googleapis/python-recaptcha-enterprise/commit/a0ab5c3abcd70aff6c1cc220fbb6afc14a5de436))

## [1.11.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.11.0...v1.11.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([54613d7](https://github.com/googleapis/python-recaptcha-enterprise/commit/54613d74af6c1cc95cad33465309fc0ef66402b8))


### Documentation

* Add documentation for enums ([54613d7](https://github.com/googleapis/python-recaptcha-enterprise/commit/54613d74af6c1cc95cad33465309fc0ef66402b8))

## [1.11.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.10.0...v1.11.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#330](https://github.com/googleapis/python-recaptcha-enterprise/issues/330)) ([ed41bb8](https://github.com/googleapis/python-recaptcha-enterprise/commit/ed41bb8f8ea270827a7c4255915492e5b462eb89))

## [1.10.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.9.0...v1.10.0) (2022-12-14)


### Features

* Add account_verification field to Assessment for MFA ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))
* Add support for `google.cloud.recaptchaenterprise.__version__` ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))
* Add typing to proto.Message based class attributes ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))


### Bug Fixes

* Add dict typing for client_options ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))
* Drop usage of pkg_resources ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))
* Fix timeout default values ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))

## [1.9.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.3...v1.9.0) (2022-10-26)


### Features

* add annotation reasons REFUND, REFUND_FRAUD, TRANSACTION_ACCEPTED, TRANSACTION_DECLINED and SOCIAL_SPAM ([1d254d0](https://github.com/googleapis/python-recaptcha-enterprise/commit/1d254d0f4b2aab473b41505a0c31d8a46469a8e4))
* Add RetrieveLegacySecretKey method ([#311](https://github.com/googleapis/python-recaptcha-enterprise/issues/311)) ([1d254d0](https://github.com/googleapis/python-recaptcha-enterprise/commit/1d254d0f4b2aab473b41505a0c31d8a46469a8e4))

## [1.8.3](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.2...v1.8.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#308](https://github.com/googleapis/python-recaptcha-enterprise/issues/308)) ([c772e63](https://github.com/googleapis/python-recaptcha-enterprise/commit/c772e63fde35b93e73da67fde3d311e91569185c))

## [1.8.2](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.1...v1.8.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf &gt;= 3.20.2 ([#304](https://github.com/googleapis/python-recaptcha-enterprise/issues/304)) ([20ce864](https://github.com/googleapis/python-recaptcha-enterprise/commit/20ce864c6f65fca9f5c267d8ba8c9cdf1fc35cff))

## [1.8.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.0...v1.8.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#282](https://github.com/googleapis/python-recaptcha-enterprise/issues/282)) ([0499b5a](https://github.com/googleapis/python-recaptcha-enterprise/commit/0499b5a8ba88c373576b8fd673e3146a148ce51a))
* **deps:** require proto-plus >= 1.22.0 ([0499b5a](https://github.com/googleapis/python-recaptcha-enterprise/commit/0499b5a8ba88c373576b8fd673e3146a148ce51a))

## [1.8.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.7.1...v1.8.0) (2022-07-14)


### Features

* add audience parameter ([b833a31](https://github.com/googleapis/python-recaptcha-enterprise/commit/b833a318dfa71cd6a941b35ad8e95d903fa3de45))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#271](https://github.com/googleapis/python-recaptcha-enterprise/issues/271)) ([90479fc](https://github.com/googleapis/python-recaptcha-enterprise/commit/90479fca8fd002c3c6deae2aedbfff7943d14af3))
* require python 3.7+ ([#270](https://github.com/googleapis/python-recaptcha-enterprise/issues/270)) ([a370851](https://github.com/googleapis/python-recaptcha-enterprise/commit/a370851f88e72026ace4f13f87e19a642367a737))
* set the right field number for reCAPTCHA private password leak ([#266](https://github.com/googleapis/python-recaptcha-enterprise/issues/266)) ([6632149](https://github.com/googleapis/python-recaptcha-enterprise/commit/663214989b8d4cbf3f84e1b4e9b2c1856eefb59b))

## [1.7.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.7.0...v1.7.1) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#258](https://github.com/googleapis/python-recaptcha-enterprise/issues/258)) ([56b014a](https://github.com/googleapis/python-recaptcha-enterprise/commit/56b014a1781fdb1636797bca24af306fdcbd68b9))


### Documentation

* fix changelog header to consistent size ([#259](https://github.com/googleapis/python-recaptcha-enterprise/issues/259)) ([ad6402b](https://github.com/googleapis/python-recaptcha-enterprise/commit/ad6402b20391b1ae3e6a38343612260a51c8bfdc))

## [1.7.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.6.1...v1.7.0) (2022-05-19)


### Features

* Add support for Password Check through the private_password_leak_verification field in Assessment ([#233](https://github.com/googleapis/python-recaptcha-enterprise/issues/233)) ([38c7a96](https://github.com/googleapis/python-recaptcha-enterprise/commit/38c7a9685437b4503e16b0a7b3db0b8d3063709d))
* introduced WafSettings ([86096a4](https://github.com/googleapis/python-recaptcha-enterprise/commit/86096a4edab2304edd469cbd2049f466a009ef2f))


### Bug Fixes

* rename parent to project in SearchRelatedAccountGroupMembershipsRequest ([#227](https://github.com/googleapis/python-recaptcha-enterprise/issues/227)) ([86096a4](https://github.com/googleapis/python-recaptcha-enterprise/commit/86096a4edab2304edd469cbd2049f466a009ef2f))

## [1.6.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.6.0...v1.6.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#198](https://github.com/googleapis/python-recaptcha-enterprise/issues/198)) ([beee21d](https://github.com/googleapis/python-recaptcha-enterprise/commit/beee21d72f3d165d77d1d096e54e5b9c143f122d))
* **deps:** require proto-plus>=1.15.0 ([beee21d](https://github.com/googleapis/python-recaptcha-enterprise/commit/beee21d72f3d165d77d1d096e54e5b9c143f122d))

## [1.6.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.5.0...v1.6.0) (2022-02-28)


### Features

* add api key support ([#181](https://github.com/googleapis/python-recaptcha-enterprise/issues/181)) ([e9935ce](https://github.com/googleapis/python-recaptcha-enterprise/commit/e9935ce310b44d076e4590034b392f9681748f31))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([d5cc843](https://github.com/googleapis/python-recaptcha-enterprise/commit/d5cc843a1c6789c85751abe610b16fc6622029df))

## [1.5.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.4.1...v1.5.0) (2022-01-14)


### Features

* add new reCAPTCHA Enterprise fraud annotations ([#163](https://github.com/googleapis/python-recaptcha-enterprise/issues/163)) ([3c638f9](https://github.com/googleapis/python-recaptcha-enterprise/commit/3c638f97a966efdc6809016b9a50d63ffe4b380c))

## [1.4.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.4.0...v1.4.1) (2021-11-16)


### Documentation

* **samples:** added sample and tests for annotate assessment API ([#155](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/155)) ([353f0ff](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/353f0ffa27119bf3a8a8f6cddecb41d1ca8dbd31))

## [1.4.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.3.1...v1.4.0) (2021-11-03)


### Features

* add reCAPTCHA Enterprise account defender API methods ([#146](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/146)) ([8149df9](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/8149df9e3038bf02483fb2ee0c9dfc9d713a6152))


### Documentation

* **samples:** removed assessment name in create_assessment sample ([#147](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/147)) ([f11134d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/f11134da5e9e9770b73dadd96c08ba69c99b968f))

## [1.3.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.3.0...v1.3.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([22ed89d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/22ed89dcaa628790d09584b3bd20c35115647bb7))
* **deps:** require google-api-core >= 1.28.0 ([22ed89d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/22ed89dcaa628790d09584b3bd20c35115647bb7))


### Documentation

* list oneofs in docstring ([22ed89d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/22ed89dcaa628790d09584b3bd20c35115647bb7))

## [1.3.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.2.0...v1.3.0) (2021-10-14)


### Features

* add support for python 3.10 ([#137](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/137)) ([fda16a4](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fda16a44a84b173a8866090021e03eef0cb82025))


### Documentation

* **samples:** add reCAPTCHA Enterprise code samples  ([#112](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/112)) ([879acf1](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/879acf12d24b5148e372f0f76a243ea0fc66286e))

## [1.2.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.1.2...v1.2.0) (2021-10-08)


### Features

* add context manager support in client ([#131](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/131)) ([69d2b34](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/69d2b347f9aab3f30a3b0265fc9dcd9a3926f62d))

## [1.1.2](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.1.1...v1.1.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([cab9a71](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/cab9a71083b2482396ecd53051bb694937c7fe7d))

## [1.1.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.1.0...v1.1.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([7d49e68](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/7d49e6830e0f914d8fb2f20961a3ae6953244ed4))

## [1.1.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.0.0...v1.1.0) (2021-09-16)


### Features

* add GetMetrics and MigrateKey methods to reCAPTCHA enterprise API ([#119](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/119)) ([6c8bf2f](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/6c8bf2f7f9fabb7fb23257fe5978ba59160d6875))

## [1.0.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.4.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#105](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/105)) ([fab3e48](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fab3e48b6ddc31bed65e9bedfd9f06aa33fd2c02))

## [0.4.2](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.4.1...v0.4.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#101](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/101)) ([2a9cba8](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/2a9cba89af89d76a1e9a4922e2901bd4847de949))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#97](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/97)) ([ffcc165](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/ffcc1651929337be437250e440b75548c453ced9))


### Miscellaneous Chores

* release as 0.4.2 ([#102](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/102)) ([ff137b0](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/ff137b00f5282dc061941b6645143db7c66a6718))

## [0.4.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.4.0...v0.4.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#96](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/96)) ([dafb540](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/dafb540844946190af288039b745f77ac08d90ab))

## [0.4.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.3...v0.4.0) (2021-07-12)


### Features

* add always_use_jwt_access ([#87](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/87)) ([d0851c8](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/d0851c8df866f4a5604523fcd23cfbba2a5fd51c))


### Bug Fixes

* disable always_use_jwt_access ([#91](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/91)) ([de8c214](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/de8c214bbbbe1aaf55ebabca35ab005540180be6))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1127)) ([#82](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/82)) ([fd4b1b4](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fd4b1b4af92ff9027675b7bd1b494870225eccaa)), closes [#1126](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1126)

## [0.4.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.3...v0.4.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#87](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/87)) ([d0851c8](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/d0851c8df866f4a5604523fcd23cfbba2a5fd51c))


### Bug Fixes

* disable always_use_jwt_access ([#91](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/91)) ([de8c214](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/de8c214bbbbe1aaf55ebabca35ab005540180be6))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1127)) ([#82](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/82)) ([fd4b1b4](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fd4b1b4af92ff9027675b7bd1b494870225eccaa)), closes [#1126](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1126)

## [0.3.3](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.2...v0.3.3) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#79](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/79)) ([1d39b4b](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/1d39b4bbf30aadafaa407c4911e2368d9330ccef)), closes [#74](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/74)

## [0.3.2](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.1...v0.3.2) (2021-06-09)


### Documentation

* fix package name ([#78](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/78)) ([6de2981](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/6de298111482e205d90895674fd19db401df70ea))
* fix package name and package info in README ([#76](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/76)) ([0e719bb](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/0e719bb23c9680f46bf36ef2344a98eb73ac70dc))

## [0.3.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.0...v0.3.1) (2021-05-28)


### Bug Fixes

* **deps:** add packaging requirement ([#68](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/68)) ([176bbe9](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/176bbe954a38c0dbbe4669035bb4a807031c7a9d))

## [0.3.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.2.1...v0.3.0) (2021-02-08)


### Features

* add async client, add common resource helpers, add from_service_account_info factory ([#30](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/30)) ([7f9db72](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/7f9db7203246c0911ad1760ffc8e56cc61acd224))

## [0.2.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.2.0...v0.2.1) (2020-06-01)


### Bug Fixes

* corrects link to client library documentation ([#13](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/13)) ([1ea5be7](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/1ea5be722147a7386afa5320eef7266b3eb9d984)), closes [#12](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/12)

## [0.2.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.1.0...v0.2.0) (2020-05-28)


### Features

* add mtls support and resource path parse methods (via synth) ([#4](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/4)) ([c20fa3f](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/c20fa3f09365b2d1bc172df35c06110c989f688e))

## 0.1.0 (2020-04-20)


### Features

* generate v1 ([a7da83d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/a7da83ddb1d622584fb442d38c28419e7708b946))
