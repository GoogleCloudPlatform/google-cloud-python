# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/grafeas/#history

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.24.0...grafeas-v1.25.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.23.0...grafeas-v1.24.0) (2026-08-06)


### Features

* update googleapis and regenerate ([#17933](https://github.com/googleapis/google-cloud-python/issues/17933)) ([f7a23a0](https://github.com/googleapis/google-cloud-python/commit/f7a23a0ffe3fac77bf9f53bc74aa3cea4ef8051e))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.22.0...grafeas-v1.23.0) (2026-06-02)


### Features

* regenerate remaining packages (#17078) ([cc4f36f65e8b29d28f636e082435801b899cbca0](https://github.com/googleapis/google-cloud-python/commit/cc4f36f65e8b29d28f636e082435801b899cbca0))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.21.0...grafeas-v1.22.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.20.0...grafeas-v1.21.0) (2026-03-23)


### Features

* Added line_number to FileLocation ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.19.1...grafeas-v1.20.0) (2026-02-19)


### Features

* A new field `advisory_publish_time` is added to message `.grafeas.v1.VulnerabilityNote` ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))
* A new field `registry` is added to message `.grafeas.v1.BaseImage` ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))

## [1.19.1](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.19.0...grafeas-v1.19.1) (2026-02-05)


### Bug Fixes

* fix mypy (#15496) ([4daf9cc283e66f49904b74c1067d245ba43e833a](https://github.com/googleapis/google-cloud-python/commit/4daf9cc283e66f49904b74c1067d245ba43e833a))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.18.0...grafeas-v1.19.0) (2026-01-29)


### Features

* A new field `last_vulnerability_update_time` is added to message `.grafeas.v1.DiscoveryOccurrence` ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.17.0...grafeas-v1.18.0) (2026-01-15)


### Documentation

* A comment for enum value `SECRET_KIND_GCP_SERVICE_ACCOUNT_KEY` in enum `SecretKind` is changed ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))


### Features

* A new value `SECRET_KIND_GCP_API_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_OPENAI_API_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_STRIPE_RESTRICTED_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `File` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `ExploitPredictionScoringSystem` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `files` is added to message `.grafeas.v1.DiscoveryOccurrence` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `unreachable` is added to message `.grafeas.v1.ListOccurrencesResponse` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `CISAKnownExploitedVulnerabilities` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_AZURE_IDENTITY_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_ANTHROPIC_API_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_ANTHROPIC_ADMIN_API_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `data` is added to message `.grafeas.v1.SecretOccurrence` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GCP_OAUTH2_CLIENT_CREDENTIALS` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GCP_OAUTH2_ACCESS_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GITHUB_OAUTH_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `risk` is added to message `.grafeas.v1.VulnerabilityOccurrence` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `return_partial_success` is added to message `.grafeas.v1.ListOccurrencesRequest` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `return_partial_success` is added to message `.grafeas.v1.ListNotesRequest` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `digest` is added to message `.grafeas.v1.SecretOccurrence` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_DOCKER_HUB_PERSONAL_ACCESS_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_STRIPE_SECRET_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GITHUB_CLASSIC_PERSONAL_ACCESS_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GITHUB_APP_USER_TO_SERVER_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_PERPLEXITY_API_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_AZURE_ACCESS_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GITHUB_APP_REFRESH_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GITHUB_APP_SERVER_TO_SERVER_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_GITHUB_FINE_GRAINED_PERSONAL_ACCESS_TOKEN` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new message `Risk` is added ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_STRIPE_WEBHOOK_SECRET` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new value `SECRET_KIND_HUGGINGFACE_API_KEY` is added to enum `SecretKind` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))
* A new field `unreachable` is added to message `.grafeas.v1.ListNotesResponse` ([1a81689422520562771f36a58575d07e1ee18dd5](https://github.com/googleapis/google-cloud-python/commit/1a81689422520562771f36a58575d07e1ee18dd5))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.16.0...grafeas-v1.17.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.15.0...grafeas-v1.16.0) (2025-10-14)


### Features

* Add support for Python 3.14 ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))


### Bug Fixes

* Deprecate credentials_file argument ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.14.1...grafeas-v1.15.0) (2025-05-08)


### Features

* Add support for Layer Details ([f7fc9c4](https://github.com/googleapis/google-cloud-python/commit/f7fc9c4b7432ad60fa488d6a902ab35586543dc5))
* Add support for Secrets ([f7fc9c4](https://github.com/googleapis/google-cloud-python/commit/f7fc9c4b7432ad60fa488d6a902ab35586543dc5))

## [1.14.1](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.14.0...grafeas-v1.14.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([36e8ba1](https://github.com/googleapis/google-cloud-python/commit/36e8ba12eac92dd221ac3ddf1061da3845135791))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.13.0...grafeas-v1.14.0) (2025-02-18)


### Features

* Add REST Interceptors which support reading metadata ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))
* Add support for reading selective GAPIC generation methods from service YAML ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.12.1...grafeas-v1.13.0) (2024-12-12)


### Features

* [Many APIs] Add support for opt-in debug logging ([#13349](https://github.com/googleapis/google-cloud-python/issues/13349)) ([8b9c7bf](https://github.com/googleapis/google-cloud-python/commit/8b9c7bf3bb1c4f0beabd71a45c469fcedb19a2c8))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([8b9c7bf](https://github.com/googleapis/google-cloud-python/commit/8b9c7bf3bb1c4f0beabd71a45c469fcedb19a2c8))

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.12.0...grafeas-v1.12.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13248](https://github.com/googleapis/google-cloud-python/issues/13248)) ([634f3e7](https://github.com/googleapis/google-cloud-python/commit/634f3e740926506654efa82a4f7a8d5f7e3cf6ba))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.11.0...grafeas-v1.12.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13212](https://github.com/googleapis/google-cloud-python/issues/13212)) ([94d00a1](https://github.com/googleapis/google-cloud-python/commit/94d00a126aa436513d23b25993b7fdc106809441))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.10.1...grafeas-v1.11.0) (2024-07-30)


### Features

* A new field `version` is added to message `.grafeas.v1.ComplianceOccurrence` ([5feea7e](https://github.com/googleapis/google-cloud-python/commit/5feea7ea9a5c20c13f57c5d51b4e0cedeeffa709))
* A new field `vulnerability_attestation` is added to message `.grafeas.v1.DiscoveryOccurrence` ([5feea7e](https://github.com/googleapis/google-cloud-python/commit/5feea7ea9a5c20c13f57c5d51b4e0cedeeffa709))
* A new message `VulnerabilityAttestation` is added ([5feea7e](https://github.com/googleapis/google-cloud-python/commit/5feea7ea9a5c20c13f57c5d51b4e0cedeeffa709))


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([11c0629](https://github.com/googleapis/google-cloud-python/commit/11c06293cef3391f5fb433d5de26c066943082d0))

## [1.10.1](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.10.0...grafeas-v1.10.1) (2024-07-08)


### Bug Fixes

* Allow protobuf 5.x ([eb36e8a](https://github.com/googleapis/google-cloud-python/commit/eb36e8a5e779717977132f605aa2ebc3cad78517))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.9.3...grafeas-v1.10.0) (2024-03-22)


### Features

* A new field `extra_details` is added to message `VulnerabilityOccurrence` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `impact` is added to message `ComplianceNote` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `in_toto_slsa_provenance_v1` is added to message `BuildOccurrence` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `sbom_reference` is added to message `Note` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `sbom_reference` is added to message `Occurrence` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `sbom_status` is added to message `DiscoveryOccurrence` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `vulnerability_id` is added to message `VulnerabilityAssessmentNote` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new field `vulnerability_id` is added to message `VulnerabilityOccurrence` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new message `InTotoSlsaProvenanceV1` is added ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new message `SbomReferenceIntotoPayload` is added ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new message `SbomReferenceIntotoPredicate` is added ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new message `SBOMReferenceNote` is added ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new message `SBOMReferenceOccurrence` is added ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new message `SBOMStatus` is added ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A new value `SBOM_REFERENCE` is added to enum `NoteKind` ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))


### Documentation

* A comment for field `cve` in message `VulnerabilityAssessmentNote` is changed ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))
* A comment for field `cve` in message `VulnerabilityOccurrence` is changed ([5fd0b34](https://github.com/googleapis/google-cloud-python/commit/5fd0b34dc61646406f4a5fe51261dace4438582f))

## [1.9.3](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.9.2...grafeas-v1.9.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12389](https://github.com/googleapis/google-cloud-python/issues/12389)) ([5db9352](https://github.com/googleapis/google-cloud-python/commit/5db93528a1ad20825d4d12dcf5fdf9624879f2ce))

## [1.9.2](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.9.1...grafeas-v1.9.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12311](https://github.com/googleapis/google-cloud-python/issues/12311)) ([e4c864b](https://github.com/googleapis/google-cloud-python/commit/e4c864b3e67c7f7f33dfb0d2107fa138492ad338))
* fix ValueError in test__validate_universe_domain ([f3974d4](https://github.com/googleapis/google-cloud-python/commit/f3974d46a9ba9f549e31251ebc2daeb6b9b4745a))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.9.0...grafeas-v1.9.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([d7d730a](https://github.com/googleapis/google-cloud-python/commit/d7d730acd3b1da86b996fa18c81272f1c9a00406))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/grafeas-v1.8.1...grafeas-v1.9.0) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [1.8.1](https://github.com/googleapis/python-grafeas/compare/v1.8.0...v1.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([2b37951](https://github.com/googleapis/python-grafeas/commit/2b3795107feb1832670f3db11418695258d65c53))


### Documentation

* Add documentation for enums ([2b37951](https://github.com/googleapis/python-grafeas/commit/2b3795107feb1832670f3db11418695258d65c53))

## [1.8.0](https://github.com/googleapis/python-grafeas/compare/v1.7.0...v1.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#226](https://github.com/googleapis/python-grafeas/issues/226)) ([c13c260](https://github.com/googleapis/python-grafeas/commit/c13c2602ea0b36084123114845ea03b377a292df))

## [1.7.0](https://github.com/googleapis/python-grafeas/compare/v1.6.1...v1.7.0) (2022-12-14)


### Features

* Add support for `grafeas.grafeas.__version__` ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))
* Add typing to proto.Message based class attributes ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))


### Bug Fixes

* Add dict typing for client_options ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))
* Drop usage of pkg_resources ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))
* Fix timeout default values ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([ad9ec08](https://github.com/googleapis/python-grafeas/commit/ad9ec0886ebf5be225f0ac91fd2bb0c45ab6ad7b))

## [1.6.1](https://github.com/googleapis/python-grafeas/compare/v1.6.0...v1.6.1) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#216](https://github.com/googleapis/python-grafeas/issues/216)) ([49cf6f2](https://github.com/googleapis/python-grafeas/commit/49cf6f2509d2750cca42d75176c632afd46a2d8e))

## [1.6.0](https://github.com/googleapis/python-grafeas/compare/v1.5.1...v1.6.0) (2022-10-03)


### Features

* Add new analysis status and cvss version fields ([#214](https://github.com/googleapis/python-grafeas/issues/214)) ([f3aaadb](https://github.com/googleapis/python-grafeas/commit/f3aaadb44d99610b056565169d728d762c0d0465))


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#213](https://github.com/googleapis/python-grafeas/issues/213)) ([6a28e86](https://github.com/googleapis/python-grafeas/commit/6a28e86042bd3ad7eb7c9096d7e6486cd40878c8))

## [1.5.1](https://github.com/googleapis/python-grafeas/compare/v1.5.0...v1.5.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#198](https://github.com/googleapis/python-grafeas/issues/198)) ([e66561a](https://github.com/googleapis/python-grafeas/commit/e66561a9ed210a0564b5027a1decb7f36413e447))
* **deps:** require proto-plus >= 1.22.0 ([e66561a](https://github.com/googleapis/python-grafeas/commit/e66561a9ed210a0564b5027a1decb7f36413e447))

## [1.5.0](https://github.com/googleapis/python-grafeas/compare/v1.4.5...v1.5.0) (2022-07-14)


### Features

* Add `Digest`, `FileLocation` and `License` ([#186](https://github.com/googleapis/python-grafeas/issues/186)) ([69b5e8b](https://github.com/googleapis/python-grafeas/commit/69b5e8b7fe9162f93a2141a30a94e0bf637af433))
* add audience parameter ([59cb75d](https://github.com/googleapis/python-grafeas/commit/59cb75d9b2beeaaa25ab4cd057bcbd5efc5796d7))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#196](https://github.com/googleapis/python-grafeas/issues/196)) ([61bc475](https://github.com/googleapis/python-grafeas/commit/61bc475542fec60ed8a8ff6b4aecf66e61b5a53a))
* require python 3.7+ ([#195](https://github.com/googleapis/python-grafeas/issues/195)) ([08f46fd](https://github.com/googleapis/python-grafeas/commit/08f46fdaf38d76c31f97616e3f9e379e496b189a))

## [1.4.5](https://github.com/googleapis/python-grafeas/compare/v1.4.4...v1.4.5) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#182](https://github.com/googleapis/python-grafeas/issues/182)) ([d20665c](https://github.com/googleapis/python-grafeas/commit/d20665c84379e260cd2d4470ba8b000f0336a8d2))


### Documentation

* fix changelog header to consistent size ([#181](https://github.com/googleapis/python-grafeas/issues/181)) ([ac19dbf](https://github.com/googleapis/python-grafeas/commit/ac19dbf79e1d29205ecd36d8ef185c615ee7a691))

## [1.4.4](https://github.com/googleapis/python-grafeas/compare/v1.4.3...v1.4.4) (2022-05-05)


### Documentation

* fix type in docstring for map fields ([30b3cba](https://github.com/googleapis/python-grafeas/commit/30b3cba74aec079cd7ac29d08b55dae7caaf8018))

## [1.4.3](https://github.com/googleapis/python-grafeas/compare/v1.4.2...v1.4.3) (2022-03-04)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#150](https://github.com/googleapis/python-grafeas/issues/150)) ([86c3ea1](https://github.com/googleapis/python-grafeas/commit/86c3ea1f23d518a56c350cb5f26b8c651d38c1e4))
* **deps:** require proto-plus>=1.15.0 ([86c3ea1](https://github.com/googleapis/python-grafeas/commit/86c3ea1f23d518a56c350cb5f26b8c651d38c1e4))

## [1.4.2](https://github.com/googleapis/python-grafeas/compare/v1.4.1...v1.4.2) (2022-02-26)


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([71ab2a6](https://github.com/googleapis/python-grafeas/commit/71ab2a6719a1ff50ba13dc521dfee54f238b7dc3))


### Documentation

* add generated snippets ([#147](https://github.com/googleapis/python-grafeas/issues/147)) ([6fcc520](https://github.com/googleapis/python-grafeas/commit/6fcc52016e3feca62b171ea4e6c70644302263c9))

## [1.4.1](https://github.com/googleapis/python-grafeas/compare/v1.4.0...v1.4.1) (2022-01-11)


### Bug Fixes

* include the compliance protos ([#134](https://github.com/googleapis/python-grafeas/issues/134)) ([6a8f2d1](https://github.com/googleapis/python-grafeas/commit/6a8f2d151d6e207e2005ee21b7e0ba34e58b0e09))

## [1.4.0](https://www.github.com/googleapis/python-grafeas/compare/v1.3.1...v1.4.0) (2021-11-03)


### Features

* Add compliance and intoto attestation protos ([#123](https://www.github.com/googleapis/python-grafeas/issues/123)) ([ff88a63](https://www.github.com/googleapis/python-grafeas/commit/ff88a6388c1117d17f5e33e28aa1c7e090b34659))

## [1.3.1](https://www.github.com/googleapis/python-grafeas/compare/v1.3.0...v1.3.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([b90b6fe](https://www.github.com/googleapis/python-grafeas/commit/b90b6fe80fe7358a245109b8c331bddba6f68e7e))
* **deps:** require google-api-core >= 1.28.0 ([b90b6fe](https://www.github.com/googleapis/python-grafeas/commit/b90b6fe80fe7358a245109b8c331bddba6f68e7e))


### Documentation

* list oneofs in docstring ([b90b6fe](https://www.github.com/googleapis/python-grafeas/commit/b90b6fe80fe7358a245109b8c331bddba6f68e7e))

## [1.3.0](https://www.github.com/googleapis/python-grafeas/compare/v1.2.0...v1.3.0) (2021-10-14)


### Features

* add support for python 3.10 ([#117](https://www.github.com/googleapis/python-grafeas/issues/117)) ([ef1fa8e](https://www.github.com/googleapis/python-grafeas/commit/ef1fa8e13cdadcd8b41cbb84313b472bc313f7ea))

## [1.2.0](https://www.github.com/googleapis/python-grafeas/compare/v1.1.4...v1.2.0) (2021-10-08)


### Features

* add context manager support in client ([#114](https://www.github.com/googleapis/python-grafeas/issues/114)) ([13240ae](https://www.github.com/googleapis/python-grafeas/commit/13240ae230782816916edda9e665c9457620a094))

## [1.1.4](https://www.github.com/googleapis/python-grafeas/compare/v1.1.3...v1.1.4) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([ce7afa0](https://www.github.com/googleapis/python-grafeas/commit/ce7afa03c39588832beaa9a0307b79ba1fac88f6))

## [1.1.3](https://www.github.com/googleapis/python-grafeas/compare/v1.1.2...v1.1.3) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([594f8d1](https://www.github.com/googleapis/python-grafeas/commit/594f8d19b3515c1cadab9fdacbba4317d4b43b29))

## [1.1.2](https://www.github.com/googleapis/python-grafeas/compare/v1.1.1...v1.1.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#88](https://www.github.com/googleapis/python-grafeas/issues/88)) ([81a0635](https://www.github.com/googleapis/python-grafeas/commit/81a06350840a854631ea9997d1c851aa62883d4b))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#84](https://www.github.com/googleapis/python-grafeas/issues/84)) ([2849415](https://www.github.com/googleapis/python-grafeas/commit/28494150a4f0f4fbf1d70161e494ad3faf511412))


### Miscellaneous Chores

* release as 1.1.2 ([#89](https://www.github.com/googleapis/python-grafeas/issues/89)) ([508aa4d](https://www.github.com/googleapis/python-grafeas/commit/508aa4dc1c61dfc4cb12ed16c062977ed3f324ba))

## [1.1.1](https://www.github.com/googleapis/python-grafeas/compare/v1.1.0...v1.1.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#83](https://www.github.com/googleapis/python-grafeas/issues/83)) ([1ada5bc](https://www.github.com/googleapis/python-grafeas/commit/1ada5bceefcbe750d40613614fccf5ad3a94fec5))

## [1.1.0](https://www.github.com/googleapis/python-grafeas/compare/v1.0.1...v1.1.0) (2021-05-20)


### Features

* bump release level to production/stable ([#71](https://www.github.com/googleapis/python-grafeas/issues/71)) ([53bd8a5](https://www.github.com/googleapis/python-grafeas/commit/53bd8a50ab731cf43d0c789198d221c7fbff6fb6))

## [1.0.1](https://www.github.com/googleapis/python-grafeas/compare/v1.0.0...v1.0.1) (2020-08-12)


### Bug Fixes

* remove gapic surface ([#42](https://www.github.com/googleapis/python-grafeas/issues/42)) ([aed68fe](https://www.github.com/googleapis/python-grafeas/commit/aed68fe9a83f041097d8a34f95eb89a1042b7b14))

## [1.0.0](https://www.github.com/googleapis/python-grafeas/compare/v0.4.1...v1.0.0) (2020-08-11)


### ⚠ BREAKING CHANGES

* generate with microgenerator (#36)

### Features

* generate with microgenerator ([#36](https://www.github.com/googleapis/python-grafeas/issues/36)) ([2785cc2](https://www.github.com/googleapis/python-grafeas/commit/2785cc23c3c59457d9f42a9ef1321c2ad0fade47))

## [0.4.1](https://www.github.com/googleapis/python-grafeas/compare/v0.4.0...v0.4.1) (2020-06-25)


### Bug Fixes

* update retry config ([#24](https://www.github.com/googleapis/python-grafeas/issues/24)) ([122ec6a](https://www.github.com/googleapis/python-grafeas/commit/122ec6a2fdf93ad745b6c275defa0bb809f1d005))

## [0.4.0](https://www.github.com/googleapis/python-grafeas/compare/v0.3.0...v0.4.0) (2020-02-07)


### Features

* **grafeas:** add support for upgrade notes; add `cpe` and `last_scan_time` to `DiscoveryOccurrence`; add `source_update_time` to `VulnerabilityNote` (via synth) ([#10084](https://www.github.com/googleapis/python-grafeas/issues/10084)) ([2ee967b](https://www.github.com/googleapis/python-grafeas/commit/2ee967b916e663bacbda8c391528cdca3a1117fd))


### Bug Fixes

* **grafeas:** deprecate resource name helper methods (via synth) ([#9835](https://www.github.com/googleapis/python-grafeas/issues/9835)) ([a2c26d9](https://www.github.com/googleapis/python-grafeas/commit/a2c26d9b60194d305f8cb2b8ec4a4a33d7bf3686))

## 0.3.0

10-10-2019 11:28 PDT


### Implementation Changes
- Remove send / receive message size limit (via synth). ([#8981](https://github.com/googleapis/google-cloud-python/pull/8981))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Fix intersphinx reference to requests. ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Remove CI for gh-pages, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))

## 0.2.0

07-12-2019 17:04 PDT


### Implementation Changes
- replace `min_affected_version` w/ `affected_version_{start,end}` (via synth).  ([#8465](https://github.com/googleapis/google-cloud-python/pull/8465))
- Allow kwargs to be passed to create_channel, update templates (via synth). ([#8391](https://github.com/googleapis/google-cloud-python/pull/8391))

### New Features
- Update list method docstrings (via synth). ([#8510](https://github.com/googleapis/google-cloud-python/pull/8510))

### Documentation
- Update READMEs. ([#8456](https://github.com/googleapis/google-cloud-python/pull/8456))

### Internal / Testing Changes
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))

## 0.1.0

06-17-2019 10:44 PDT

### New Features
- Initial release of the Grafeas client library. ([#8186](https://github.com/googleapis/google-cloud-python/pull/8186))
