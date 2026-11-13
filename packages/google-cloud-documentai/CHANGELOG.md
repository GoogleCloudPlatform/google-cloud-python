# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-documentai/#history

## [3.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.16.0...google-cloud-documentai-v3.17.0) (2026-10-29)


### Features

* update API sources and regenerate ([#18889](https://github.com/googleapis/google-cloud-python/issues/18889)) ([8705243](https://github.com/googleapis/google-cloud-python/commit/870524380c52ea234235e0c449f5c9aee2945283))

## [3.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.15.0...google-cloud-documentai-v3.16.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [3.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.14.0...google-cloud-documentai-v3.15.0) (2026-06-02)


### Features

* regenerate google-cloud-d packages (#17092) ([d49a2b9412b4ee9105125db36104a3e18344e0ad](https://github.com/googleapis/google-cloud-python/commit/d49a2b9412b4ee9105125db36104a3e18344e0ad))

## [3.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.13.0...google-cloud-documentai-v3.14.0) (2026-04-02)


### Features

* Update comments for proto fields ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* Added a fields for image and table annotation output ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))

## [3.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.12.0...google-cloud-documentai-v3.13.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [3.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.11.0...google-cloud-documentai-v3.12.0) (2026-03-23)


### Features

* Add a field for upgrading previous processor version when fine tuning ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))

## [3.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.10.0...google-cloud-documentai-v3.11.0) (2026-03-05)


### Features

* Added a field for enabling image and table annotation for layout parser processor ([6120fb0db084f5e8d1502fb1bb37594ac9976f6e](https://github.com/googleapis/google-cloud-python/commit/6120fb0db084f5e8d1502fb1bb37594ac9976f6e))

## [3.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.9.0...google-cloud-documentai-v3.10.0) (2026-02-12)


### Documentation

* Updated comments for various fields and messages ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))


### Features

* The method `ReviewDocument` in `.google.cloud.documentai.v1beta3.DocumentProcessorService` is deprecated ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))
* A new field `enable_table_split` is added to message `.google.cloud.documentai.v1beta3.OcrConfig.LayoutParsingParams` ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))
* Added new messages `Documents` and `RawDocuments` for inline document input ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))
* The field `skip_human_review` in messages `.google.cloud.documentai.v1beta3.ProcessRequest` and `.google.cloud.documentai.v1beta3.BatchProcessRequest` is deprecated ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))
* A new field `document_prompt` is added to message `.google.cloud.documentai.v1beta3.DocumentSchema` ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))
* A new field `revisions` is added to message `.google.cloud.documentai.v1beta3.Evaluation` ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))
* A new field `document_type` is added to message `.google.cloud.documentai.v1beta3.ImportDocumentsRequest` ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))


### Bug Fixes

* Removed the `SpannerIndexingConfig` message and the `spanner_indexing_config` field from `.google.cloud.documentai.v1beta3.Dataset` BREAKING CHANGE: The `SpannerIndexingConfig` message and the `spanner_indexing_config` field within the `Dataset` message have been removed. Client code referencing these will need to stop referencing these in case of an error ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))

## [3.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.8.0...google-cloud-documentai-v3.9.0) (2026-01-29)


### Documentation

* Fixed language issues in multiple message field descriptions ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Regenerated REST and RPC Document AI documentation to include missing changes from September 2024 to November 2025 ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))

## [3.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.7.0...google-cloud-documentai-v3.8.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [3.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.6.0...google-cloud-documentai-v3.7.0) (2025-10-16)


### Documentation

* The field `training_method` in `TrainProcessorVersionRequest` is now marked as optional  ([4dc7381c2121c9e13b24cb3aae59523f8ff31a3a](https://github.com/googleapis/google-cloud-python/commit/4dc7381c2121c9e13b24cb3aae59523f8ff31a3a))
* A comment for field `latest_evaluation` in message `.google.cloud.documentai.v1beta3.ProcessorVersion` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `training_method` in message `.google.cloud.documentai.v1beta3.TrainProcessorVersionRequest` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `processor_version_source` in message `.google.cloud.documentai.v1beta3.ImportProcessorVersionRequest` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `deprecation_info` in message `.google.cloud.documentai.v1beta3.ProcessorVersion` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `create_time` in message `.google.cloud.documentai.v1beta3.Processor` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `document_schema` in message `.google.cloud.documentai.v1beta3.ProcessorVersion` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `kms_key_name` in message `.google.cloud.documentai.v1beta3.ProcessorVersion` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `create_time` in message `.google.cloud.documentai.v1beta3.ProcessorVersion` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A comment for field `kms_key_version_name` in message `.google.cloud.documentai.v1beta3.ProcessorVersion` is changed  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Features

* Added new messages `EntityValidationOutput` and `EntitiesRevision`  ([4dc7381c2121c9e13b24cb3aae59523f8ff31a3a](https://github.com/googleapis/google-cloud-python/commit/4dc7381c2121c9e13b24cb3aae59523f8ff31a3a))
* Added new fields `entity_validation_output`, `entities_revisions`, and `entities_revision_id` to the `Document` message  ([4dc7381c2121c9e13b24cb3aae59523f8ff31a3a](https://github.com/googleapis/google-cloud-python/commit/4dc7381c2121c9e13b24cb3aae59523f8ff31a3a))
* A new field `signature_value` is added to message `.google.cloud.documentai.v1beta3.Document`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new message `EntitiesRevision` is added  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new field `entities_revisions` is added to message `.google.cloud.documentai.v1beta3.Document`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new field `entity_validation_output` is added to message `.google.cloud.documentai.v1beta3.Document`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new field `method` is added to message `.google.cloud.documentai.v1beta3.DocumentSchema`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new enum `Method` is added  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new field `method` is added to message `.google.cloud.documentai.v1beta3.Document`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new message `EntityValidationOutput` is added  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new field `entities_revision_id` is added to message `.google.cloud.documentai.v1beta3.Document`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* A new field `annotations` is added to message `.google.cloud.documentai.v1beta3.Document`  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))
* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [3.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.5.0...google-cloud-documentai-v3.6.0) (2025-08-29)


### Features

* Added config options for derived fields and signature detection. Some annotation changes changes to mark fields explicitly output only (no changes in semantics just readability) ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))


### Documentation

* A comment for field `create_time` in message `.google.cloud.documentai.v1.Processor`  is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))
* A comment for field `create_time` in message `.google.cloud.documentai.v1.ProcessorVersion`  is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))
* A comment for field `deprecation_info` in message `.google.cloud.documentai.v1.ProcessorVersion`  is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))
* A comment for field `document_schema` in message `.google.cloud.documentai.v1.ProcessorVersion` is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))
* A comment for field `kms_key_name` in message `.google.cloud.documentai.v1.ProcessorVersion`  is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))
* A comment for field `kms_key_version_name` in message `.google.cloud.documentai.v1.ProcessorVersion`  is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))
* A comment for field `latest_evaluation` in message `.google.cloud.documentai.v1.ProcessorVersion`  is changed to describe as output only. ([6d0eeb7](https://github.com/googleapis/google-cloud-python/commit/6d0eeb7e4ae05a8ce9b2849eb9caf554b6e449c4))

## [3.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.4.0...google-cloud-documentai-v3.5.0) (2025-04-29)


### Features

* **v1beta3:** [google-cloud-documentai] Added config options to enable table annotation and image extraction ([#13847](https://github.com/googleapis/google-cloud-python/issues/13847)) ([cd64ac0](https://github.com/googleapis/google-cloud-python/commit/cd64ac0e4653abd812e190343499e7fb95473fe9))
* **v1beta3:** Add image block and blob asset in Document proto ([3c829a0](https://github.com/googleapis/google-cloud-python/commit/3c829a0e14848fd084ceb1fcdaf5c5336e261df8))
* **v1beta3:** Added config options to enable image annotation ([3c829a0](https://github.com/googleapis/google-cloud-python/commit/3c829a0e14848fd084ceb1fcdaf5c5336e261df8))

## [3.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.3.0...google-cloud-documentai-v3.4.0) (2025-04-23)


### Features

* [google-cloud-documentai] Added a field for enabling returning images and bounding boxes from layout parser processor ([#13822](https://github.com/googleapis/google-cloud-python/issues/13822)) ([77e38cd](https://github.com/googleapis/google-cloud-python/commit/77e38cd3499f8ea66e5aa9703a56bd8be9b9836d))

## [3.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.2.1...google-cloud-documentai-v3.3.0) (2025-03-19)


### Features

* [google-cloud-documentai] Added config options to enable LLM ([ee05aca](https://github.com/googleapis/google-cloud-python/commit/ee05aca642a1e86e8ae05e19a4f2f84fdbbab7d8))
* Added config options to enable LLM layout parsing ([#13680](https://github.com/googleapis/google-cloud-python/issues/13680)) ([ee05aca](https://github.com/googleapis/google-cloud-python/commit/ee05aca642a1e86e8ae05e19a4f2f84fdbbab7d8))

## [3.2.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.2.0...google-cloud-documentai-v3.2.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([feb5353](https://github.com/googleapis/google-cloud-python/commit/feb53532240bb70a94b359b519f0f41f95875a33))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [3.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.1.0...google-cloud-documentai-v3.2.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([b0e1f43](https://github.com/googleapis/google-cloud-python/commit/b0e1f4303b6ceff89b022986f9d87eda736e7235))
* Add support for reading selective GAPIC generation methods from service YAML ([b0e1f43](https://github.com/googleapis/google-cloud-python/commit/b0e1f4303b6ceff89b022986f9d87eda736e7235))


### Documentation

* mark fields as unused ([b0e1f43](https://github.com/googleapis/google-cloud-python/commit/b0e1f4303b6ceff89b022986f9d87eda736e7235))

## [3.1.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.0.1...google-cloud-documentai-v3.1.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [3.0.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v3.0.0...google-cloud-documentai-v3.0.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))

## [3.0.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.35.0...google-cloud-documentai-v3.0.0) (2024-10-28)


### ⚠ BREAKING CHANGES

* Remove google.cloud.documentai_v1beta2 ([#13218](https://github.com/googleapis/google-cloud-python/issues/13218))

### Bug Fixes

* Remove google.cloud.documentai_v1beta2 ([#13218](https://github.com/googleapis/google-cloud-python/issues/13218)) ([a98df65](https://github.com/googleapis/google-cloud-python/commit/a98df654c18a6ea37119e7d55bdedb1b0135c475))

## [2.35.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.34.0...google-cloud-documentai-v2.35.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13205](https://github.com/googleapis/google-cloud-python/issues/13205)) ([4f4fdcf](https://github.com/googleapis/google-cloud-python/commit/4f4fdcf845621cea69facb568b7fe17d4f38d467))

## [2.34.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.33.0...google-cloud-documentai-v2.34.0) (2024-10-23)


### Features

* [google-cloud-documentai] Updated the exponential backoff settings for the Document AI ProcessDocument and BatchProcessDocuments methods ([91e9f9f](https://github.com/googleapis/google-cloud-python/commit/91e9f9f262ac350cb6fa537eceac104460b1bfc0))
* Add RESOURCE_EXHAUSTED to retryable status codes for ProcessDocument method ([91e9f9f](https://github.com/googleapis/google-cloud-python/commit/91e9f9f262ac350cb6fa537eceac104460b1bfc0))
* Add RESOURCE_EXHAUSTED to retryable status codes for ProcessDocument method ([98a4a8d](https://github.com/googleapis/google-cloud-python/commit/98a4a8de41dd24d542f592f06f68dd5adac0ceeb))
* Updated the exponential backoff settings for the Document AI ProcessDocument and BatchProcessDocuments methods ([98a4a8d](https://github.com/googleapis/google-cloud-python/commit/98a4a8de41dd24d542f592f06f68dd5adac0ceeb))

## [2.33.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.32.0...google-cloud-documentai-v2.33.0) (2024-10-08)


### Features

* Removed deprecated api versions ([eeab5c1](https://github.com/googleapis/google-cloud-python/commit/eeab5c1ee68559605ab3dc251314d45bd92191cd))

## [2.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.31.0...google-cloud-documentai-v2.32.0) (2024-09-06)


### Features

* [google-cloud-documentai] Add API fields for the descriptions of entity type and property in the document schema ([#13067](https://github.com/googleapis/google-cloud-python/issues/13067)) ([1a2b325](https://github.com/googleapis/google-cloud-python/commit/1a2b325c0da966131072673e06d17015b16c7a1a))

## [2.31.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.30.0...google-cloud-documentai-v2.31.0) (2024-08-08)


### Features

* A new field `gen_ai_model_info` is added to message `.google.cloud.documentai.v1.ProcessorVersion` ([f16067b](https://github.com/googleapis/google-cloud-python/commit/f16067b585fcc1f0862ce15ed00789caf0ca25bb))
* A new field `imageless_mode` is added to message `.google.cloud.documentai.v1.ProcessRequest` ([f16067b](https://github.com/googleapis/google-cloud-python/commit/f16067b585fcc1f0862ce15ed00789caf0ca25bb))

## [2.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.29.3...google-cloud-documentai-v2.30.0) (2024-07-31)


### Features

* [google-cloud-documentai] A new field `imageless_mode` is added to message `.google.cloud.documentai.v1.ProcessRequest` ([#12966](https://github.com/googleapis/google-cloud-python/issues/12966)) ([60d0728](https://github.com/googleapis/google-cloud-python/commit/60d07285f7282e89612f184aa6c95d7f2f38e1c7))

## [2.29.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.29.2...google-cloud-documentai-v2.29.3) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([ba1064f](https://github.com/googleapis/google-cloud-python/commit/ba1064fd6a63ccbe8a390c0026f32c5772c728a5))

## [2.29.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.29.1...google-cloud-documentai-v2.29.2) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## [2.29.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.29.0...google-cloud-documentai-v2.29.1) (2024-06-24)


### Documentation

* Update the comment to add a note about `documentai.processors.create` permission ([9318d94](https://github.com/googleapis/google-cloud-python/commit/9318d94ce12bd7a2e242f1ac9cbe491307c84ea6))

## [2.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.28.0...google-cloud-documentai-v2.29.0) (2024-06-05)


### Features

* [google-cloud-documentai] Make Layout Parser generally available in V1 ([#12762](https://github.com/googleapis/google-cloud-python/issues/12762)) ([9fd16ad](https://github.com/googleapis/google-cloud-python/commit/9fd16ad8837e31c3b06475b195c70c45f6979f6c))

## [2.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.27.1...google-cloud-documentai-v2.28.0) (2024-05-29)


### Features

* [google-cloud-documentai] Make Layout Parser generally available in V1 ([#12745](https://github.com/googleapis/google-cloud-python/issues/12745)) ([c5b9322](https://github.com/googleapis/google-cloud-python/commit/c5b93220710708fc457934281685b635c335394a))

## [2.27.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.27.0...google-cloud-documentai-v2.27.1) (2024-05-16)


### Documentation

* [google-cloud-documentai] clarify the unavailability of some features ([#12699](https://github.com/googleapis/google-cloud-python/issues/12699)) ([3ec5a2c](https://github.com/googleapis/google-cloud-python/commit/3ec5a2c1232fc496c72f47af312d59c1bdd0fe32))
* updated comments ([9722673](https://github.com/googleapis/google-cloud-python/commit/9722673d20f8e10c017f2f1f460daee1c098c230))

## [2.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.26.0...google-cloud-documentai-v2.27.0) (2024-04-24)


### Features

* Support Chunk header and footer in Doc AI external proto ([2615bd3](https://github.com/googleapis/google-cloud-python/commit/2615bd39fd3880cba0314e0fcc732ff24e4f0c9d))


### Documentation

* Keep the API doc up-to-date with recent changes ([2615bd3](https://github.com/googleapis/google-cloud-python/commit/2615bd39fd3880cba0314e0fcc732ff24e4f0c9d))

## [2.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.25.0...google-cloud-documentai-v2.26.0) (2024-04-17)


### Features

* A new field `foundation_model_tuning_options` is added to message `TrainProcessorVersionRequest` ([69cfd79](https://github.com/googleapis/google-cloud-python/commit/69cfd7927fc1360ca3f78d223877217e010f4722))
* A new message `FoundationModelTuningOptions` is added ([69cfd79](https://github.com/googleapis/google-cloud-python/commit/69cfd7927fc1360ca3f78d223877217e010f4722))


### Documentation

* updated comments ([69cfd79](https://github.com/googleapis/google-cloud-python/commit/69cfd7927fc1360ca3f78d223877217e010f4722))

## [2.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.24.2...google-cloud-documentai-v2.25.0) (2024-04-03)


### Features

* Support a new Layout Processor in Document AI ([f008893](https://github.com/googleapis/google-cloud-python/commit/f008893d15b88ccd29c23d3c49fee6c1a5c1e1d9))


### Documentation

* keep the API doc up-to-date with recent changes ([f008893](https://github.com/googleapis/google-cloud-python/commit/f008893d15b88ccd29c23d3c49fee6c1a5c1e1d9))

## [2.24.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.24.1...google-cloud-documentai-v2.24.2) (2024-03-22)


### Documentation

* A comment for field `processor_version_source` in message `.google.cloud.documentai.v1beta3.ImportProcessorVersionRequest` is changed ([5499d6c](https://github.com/googleapis/google-cloud-python/commit/5499d6c298544c7a0b1122ec4abbedcd7ee5ab0e))

## [2.24.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.24.0...google-cloud-documentai-v2.24.1) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12384](https://github.com/googleapis/google-cloud-python/issues/12384)) ([c69966f](https://github.com/googleapis/google-cloud-python/commit/c69966fa7aac2cba4e22513e4a053b3754f8ea5e))

## [2.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.23.0...google-cloud-documentai-v2.24.0) (2024-02-22)


### Features

* A new field `display_name` is added to message `DocumentSchema` ([38dde99](https://github.com/googleapis/google-cloud-python/commit/38dde996c05fe751643ff92ceb5aed7dc6e0e315))
* A new field `display_name` is added to message `DocumentSchema` ([aae7bf5](https://github.com/googleapis/google-cloud-python/commit/aae7bf53622e4fd56fdc767d327a5d5f978718f4))
* A new field `labels` is added to messages `ProcessRequest` and `BatchProcessRequest` ([38dde99](https://github.com/googleapis/google-cloud-python/commit/38dde996c05fe751643ff92ceb5aed7dc6e0e315))
* A new field `labels` is added to messages `ProcessRequest` and `BatchProcessRequest` ([aae7bf5](https://github.com/googleapis/google-cloud-python/commit/aae7bf53622e4fd56fdc767d327a5d5f978718f4))
* A new field `schema_override` is added to message `ProcessOptions` ([aae7bf5](https://github.com/googleapis/google-cloud-python/commit/aae7bf53622e4fd56fdc767d327a5d5f978718f4))
* A new field foundation_model_tuning_options is added to message TrainProcessorVersionRequest ([38dde99](https://github.com/googleapis/google-cloud-python/commit/38dde996c05fe751643ff92ceb5aed7dc6e0e315))
* A new message FoundationModelTuningOptions is added ([38dde99](https://github.com/googleapis/google-cloud-python/commit/38dde996c05fe751643ff92ceb5aed7dc6e0e315))


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12283](https://github.com/googleapis/google-cloud-python/issues/12283)) ([f20b41a](https://github.com/googleapis/google-cloud-python/commit/f20b41ac35b02a40135b83edfe819ff7a355ab21))
* deprecate `Dataset.document_warehouse_config` ([38dde99](https://github.com/googleapis/google-cloud-python/commit/38dde996c05fe751643ff92ceb5aed7dc6e0e315))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))


### Documentation

* [google-cloud-documentai] updated comments ([#12321](https://github.com/googleapis/google-cloud-python/issues/12321)) ([20cd51c](https://github.com/googleapis/google-cloud-python/commit/20cd51c8e0069efcb819ccbc54c3eef7e0960a34))
* updated comments ([38dde99](https://github.com/googleapis/google-cloud-python/commit/38dde996c05fe751643ff92ceb5aed7dc6e0e315))
* updated comments ([aae7bf5](https://github.com/googleapis/google-cloud-python/commit/aae7bf53622e4fd56fdc767d327a5d5f978718f4))

## [2.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.22.0...google-cloud-documentai-v2.23.0) (2024-02-06)


### Features

* expose model_type in v1 processor, so that user can see the model_type after get or list processor version ([81d36fc](https://github.com/googleapis/google-cloud-python/commit/81d36fcb96026891a851c7bce119a274c3b0abbd))


### Bug Fixes

* Add google-auth as a direct dependency ([81d36fc](https://github.com/googleapis/google-cloud-python/commit/81d36fcb96026891a851c7bce119a274c3b0abbd))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([81d36fc](https://github.com/googleapis/google-cloud-python/commit/81d36fcb96026891a851c7bce119a274c3b0abbd))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([81d36fc](https://github.com/googleapis/google-cloud-python/commit/81d36fcb96026891a851c7bce119a274c3b0abbd))

## [2.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.21.1...google-cloud-documentai-v2.22.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12240](https://github.com/googleapis/google-cloud-python/issues/12240)) ([d51f832](https://github.com/googleapis/google-cloud-python/commit/d51f83298f89dbae23af1a146411b296eba6bba2))

## [2.21.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.21.0...google-cloud-documentai-v2.21.1) (2023-12-13)


### Documentation

* [google-cloud-documentai] Clarify Properties documentation ([#12118](https://github.com/googleapis/google-cloud-python/issues/12118)) ([35c180e](https://github.com/googleapis/google-cloud-python/commit/35c180e4cb7d9e52b5f72a13b606a6004b5c8a08))

## [2.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.20.2...google-cloud-documentai-v2.21.0) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [2.20.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.20.1...google-cloud-documentai-v2.20.2) (2023-11-02)


### Documentation

* updated comments ([#11950](https://github.com/googleapis/google-cloud-python/issues/11950)) ([a0da408](https://github.com/googleapis/google-cloud-python/commit/a0da408d0f322b3f4f11a0dbe39c92fa5770e59b))

## [2.20.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.20.0...google-cloud-documentai-v2.20.1) (2023-10-10)


### Documentation

* minor comment update ([#11797](https://github.com/googleapis/google-cloud-python/issues/11797)) ([1360d6b](https://github.com/googleapis/google-cloud-python/commit/1360d6bface07de0fd9f65987f146390adec7176))

## [2.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.19.0...google-cloud-documentai-v2.20.0) (2023-09-25)


### Features

* Added `ListDocuments()` method for Document AI Workbench training documents ([2fb9078](https://github.com/googleapis/google-cloud-python/commit/2fb9078ef80ecbcc39c9708d49b7707e4708205a))
* Added SummaryOptions to ProcessOptions for the Summarizer processor ([2fb9078](https://github.com/googleapis/google-cloud-python/commit/2fb9078ef80ecbcc39c9708d49b7707e4708205a))
* make page_range field public ([2fb9078](https://github.com/googleapis/google-cloud-python/commit/2fb9078ef80ecbcc39c9708d49b7707e4708205a))


### Bug Fixes

* `OcrConfig.compute_style_info` is deprecated. Use `PremiumFeatures.compute_style_info` instead. ([2fb9078](https://github.com/googleapis/google-cloud-python/commit/2fb9078ef80ecbcc39c9708d49b7707e4708205a))

## [2.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.18.1...google-cloud-documentai-v2.19.0) (2023-09-21)


### Features

* added field Processor.processor_version_aliases ([c7c3e41](https://github.com/googleapis/google-cloud-python/commit/c7c3e414d56bb7f16353e2a3fdb74aee4ec291ea))
* added field RawDocument.display_name ([c7c3e41](https://github.com/googleapis/google-cloud-python/commit/c7c3e414d56bb7f16353e2a3fdb74aee4ec291ea))


### Bug Fixes

* deprecated OcrConfig.compute_style_info ([c7c3e41](https://github.com/googleapis/google-cloud-python/commit/c7c3e414d56bb7f16353e2a3fdb74aee4ec291ea))

## [2.18.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.18.0...google-cloud-documentai-v2.18.1) (2023-09-19)


### Documentation

* update client libraries for Enterprise OCR add-ons ([#11642](https://github.com/googleapis/google-cloud-python/issues/11642)) ([09cf3ae](https://github.com/googleapis/google-cloud-python/commit/09cf3aefee6c1d51027e324add331ff9c13e237e))

## [2.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.17.0...google-cloud-documentai-v2.18.0) (2023-07-25)


### Features

* exposed Import PV external_processor_version_source to v1beta3 public ([#11517](https://github.com/googleapis/google-cloud-python/issues/11517)) ([7915645](https://github.com/googleapis/google-cloud-python/commit/79156458ab4cf1dcddf818be096290d065e8e684))

## [2.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.16.1...google-cloud-documentai-v2.17.0) (2023-07-17)


### Features

* add `OcrConfig` and `ProcessOptions` ([0510cbb](https://github.com/googleapis/google-cloud-python/commit/0510cbbe9270a17459bc461d1a18db77c08ac608))
* **v1beta2:** added http configuration and document publishing ([0510cbb](https://github.com/googleapis/google-cloud-python/commit/0510cbbe9270a17459bc461d1a18db77c08ac608))
* **v1beta3:** added ImportDocuments, GetDocument and BatchDeleteDocuments RPCs ([0510cbb](https://github.com/googleapis/google-cloud-python/commit/0510cbbe9270a17459bc461d1a18db77c08ac608))


### Bug Fixes

* **v1beta2:** removed id field from Document message  ([0510cbb](https://github.com/googleapis/google-cloud-python/commit/0510cbbe9270a17459bc461d1a18db77c08ac608))

## [2.16.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.16.0...google-cloud-documentai-v2.16.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [2.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-documentai-v2.15.0...google-cloud-documentai-v2.16.0) (2023-06-19)


### Features

* add IMPORTING enum to State in processor.proto ([d402fd5](https://github.com/googleapis/google-cloud-python/commit/d402fd5781e4acfce6b5656d4c2012c732d01ba8))
* add PropertyMetadata and EntityTypeMetadata to document_schema.proto ([d402fd5](https://github.com/googleapis/google-cloud-python/commit/d402fd5781e4acfce6b5656d4c2012c732d01ba8))
* add REPLACE enum to OperationType in document.proto ([d402fd5](https://github.com/googleapis/google-cloud-python/commit/d402fd5781e4acfce6b5656d4c2012c732d01ba8))
* add StyleInfo to document.proto  ([d402fd5](https://github.com/googleapis/google-cloud-python/commit/d402fd5781e4acfce6b5656d4c2012c732d01ba8))

## [2.15.0](https://github.com/googleapis/python-documentai/compare/v2.14.0...v2.15.0) (2023-03-24)


### Features

* **v1beta3:** Add ImportProcessorVersion ([f3aa285](https://github.com/googleapis/python-documentai/commit/f3aa28574881e093d2e8432960e0a8bc24080ddb))


### Documentation

* Fix formatting of request arg in docstring ([f3aa285](https://github.com/googleapis/python-documentai/commit/f3aa28574881e093d2e8432960e0a8bc24080ddb))

## [2.14.0](https://github.com/googleapis/python-documentai/compare/v2.13.0...v2.14.0) (2023-03-09)


### Features

* **v1beta3:** Added enable_image_quality_scores field in OcrConfig ([bee07d2](https://github.com/googleapis/python-documentai/commit/bee07d22ad010b9f200d5eea7e5f8f3b9df87081))
* **v1beta3:** Added enable_symbol field in OcrConfig ([bee07d2](https://github.com/googleapis/python-documentai/commit/bee07d22ad010b9f200d5eea7e5f8f3b9df87081))
* **v1beta3:** Added hints.language_hints field in OcrConfig ([bee07d2](https://github.com/googleapis/python-documentai/commit/bee07d22ad010b9f200d5eea7e5f8f3b9df87081))

## [2.13.0](https://github.com/googleapis/python-documentai/compare/v2.12.0...v2.13.0) (2023-02-21)


### Features

* Added Training and Evaluation functions, request, responses and metadata to document_processor_service.proto ([#463](https://github.com/googleapis/python-documentai/issues/463)) ([6ff81aa](https://github.com/googleapis/python-documentai/commit/6ff81aa41059d61105f33c94ae9186357a1201c5))

## [2.12.0](https://github.com/googleapis/python-documentai/compare/v2.11.0...v2.12.0) (2023-02-08)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#459](https://github.com/googleapis/python-documentai/issues/459)) ([02d06d6](https://github.com/googleapis/python-documentai/commit/02d06d663a99062a98b6dc0b699ffdec38e2e5de))

## [2.11.0](https://github.com/googleapis/python-documentai/compare/v2.10.0...v2.11.0) (2023-02-07)


### Features

* Added EvaluationReference to evaluation.proto ([f374763](https://github.com/googleapis/python-documentai/commit/f37476381ca4a9adee98c8823b6d0b2287fbd71a))
* Added latest_evaluation to processor.proto ([f374763](https://github.com/googleapis/python-documentai/commit/f37476381ca4a9adee98c8823b6d0b2287fbd71a))

## [2.10.0](https://github.com/googleapis/python-documentai/compare/v2.9.1...v2.10.0) (2023-01-25)


### Features

* Added advanced_ocr_options field in OcrConfig ([#451](https://github.com/googleapis/python-documentai/issues/451)) ([5e1bb96](https://github.com/googleapis/python-documentai/commit/5e1bb96b685981cba2e3e4fc319efb0eac757fbf))

## [2.9.1](https://github.com/googleapis/python-documentai/compare/v2.9.0...v2.9.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([61256d1](https://github.com/googleapis/python-documentai/commit/61256d1728e17dc8b04cd4166e286a4f76c6018a))


### Documentation

* Add documentation for enums ([61256d1](https://github.com/googleapis/python-documentai/commit/61256d1728e17dc8b04cd4166e286a4f76c6018a))

## [2.9.0](https://github.com/googleapis/python-documentai/compare/v2.8.0...v2.9.0) (2023-01-17)


### Features

* **v1:** Exposed GetProcessorType ([#446](https://github.com/googleapis/python-documentai/issues/446)) ([6c38227](https://github.com/googleapis/python-documentai/commit/6c38227279d889f760375dfe56f805da78e7bc68))

## [2.8.0](https://github.com/googleapis/python-documentai/compare/v2.7.0...v2.8.0) (2023-01-17)


### Features

* Exposed GetProcessorType to v1beta3 ([#444](https://github.com/googleapis/python-documentai/issues/444)) ([e5835f4](https://github.com/googleapis/python-documentai/commit/e5835f4b514b2b463478df33505ac08272a99fb7))


### Documentation

* **samples:** Removed Samples after Migration to Mono Repo ([#438](https://github.com/googleapis/python-documentai/issues/438)) ([8c7f52b](https://github.com/googleapis/python-documentai/commit/8c7f52bce317b6b54bcfc71cb193dc7e372b2812))

## [2.7.0](https://github.com/googleapis/python-documentai/compare/v2.6.0...v2.7.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#440](https://github.com/googleapis/python-documentai/issues/440)) ([e3da68f](https://github.com/googleapis/python-documentai/commit/e3da68f1fb3e377eb0ccfbeacc588500ae0918ec))

## [2.6.0](https://github.com/googleapis/python-documentai/compare/v2.5.0...v2.6.0) (2022-12-15)


### Features

* Added process_options field in ProcessRequest in document_processor_service.proto ([d923e53](https://github.com/googleapis/python-documentai/commit/d923e5348983ebe0881b96dcfdb687696b5eb5df))
* Added sample_document_uris field in ProcessorType in processor_type.proto ([d923e53](https://github.com/googleapis/python-documentai/commit/d923e5348983ebe0881b96dcfdb687696b5eb5df))
* Added sharding_config field in DocumentOutputConfig.GcsOutputConfig in document_io.proto ([d923e53](https://github.com/googleapis/python-documentai/commit/d923e5348983ebe0881b96dcfdb687696b5eb5df))

## [2.5.0](https://github.com/googleapis/python-documentai/compare/v2.4.1...v2.5.0) (2022-12-13)


### Features

* Added sharding_config field in DocumentOutputConfig.GcsOutputConfig in document_io.proto ([#430](https://github.com/googleapis/python-documentai/issues/430)) ([80df6cb](https://github.com/googleapis/python-documentai/commit/80df6cb24b2e3af1ada4b0e2e602eb42caadb6e7))

## [2.4.1](https://github.com/googleapis/python-documentai/compare/v2.4.0...v2.4.1) (2022-12-07)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([#424](https://github.com/googleapis/python-documentai/issues/424)) ([ea874a7](https://github.com/googleapis/python-documentai/commit/ea874a73c6ab98e4096dc49dada4c10e6f1f0731))

## [2.4.0](https://github.com/googleapis/python-documentai/compare/v2.3.0...v2.4.0) (2022-11-27)


### Features

* Added field_mask field in DocumentOutputConfig.GcsOutputConfig in document_io.proto ([#415](https://github.com/googleapis/python-documentai/issues/415)) ([575121f](https://github.com/googleapis/python-documentai/commit/575121f2900f2f7245ebc0c87913fff844801326))


### Documentation

* **samples:** Fix Typos in Batch process & get processor Samples ([7bdedd1](https://github.com/googleapis/python-documentai/commit/7bdedd1eb6feb266ebf4f663ce572a185883f024))

## [2.3.0](https://github.com/googleapis/python-documentai/compare/v2.2.0...v2.3.0) (2022-11-14)


### Features

* Added TrainProcessorVersion, EvaluateProcessorVersion, GetEvaluation, and ListEvaluations v1beta3 APIs ([#412](https://github.com/googleapis/python-documentai/issues/412)) ([caefaa7](https://github.com/googleapis/python-documentai/commit/caefaa7941b0bdb68afd760fafe0365c9cb380f8)), closes [#410](https://github.com/googleapis/python-documentai/issues/410)

## [2.2.0](https://github.com/googleapis/python-documentai/compare/v2.1.0...v2.2.0) (2022-11-14)


### Features

* New APIs added to reflect updates to the filestore service ([#408](https://github.com/googleapis/python-documentai/issues/408)) ([f8b06f2](https://github.com/googleapis/python-documentai/commit/f8b06f2a1def0b2bf377749693b518f8d71d8d4a))


### Documentation

* **samples:** Updated code samples for 2.1.0 release ([#406](https://github.com/googleapis/python-documentai/issues/406)) ([f64a735](https://github.com/googleapis/python-documentai/commit/f64a7357aa54aecb0933e337d45c1f008f1203fa))

## [2.1.0](https://github.com/googleapis/python-documentai/compare/v2.0.3...v2.1.0) (2022-11-09)


### Features

* Added font_family to document.proto ([#404](https://github.com/googleapis/python-documentai/issues/404)) ([1038a05](https://github.com/googleapis/python-documentai/commit/1038a053961a44708b697b8db58200da5405475e))


### Documentation

* **samples:** Added extra exception handling to operation samples ([#393](https://github.com/googleapis/python-documentai/issues/393)) ([fa0f715](https://github.com/googleapis/python-documentai/commit/fa0f7153e650e3c4f7adb383089d095510752867))

## [2.0.3](https://github.com/googleapis/python-documentai/compare/v2.0.2...v2.0.3) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#388](https://github.com/googleapis/python-documentai/issues/388)) ([fd72e6e](https://github.com/googleapis/python-documentai/commit/fd72e6e9eb3ab90b37ce352bc2c138147ff0777b))

## [2.0.2](https://github.com/googleapis/python-documentai/compare/v2.0.1...v2.0.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#385](https://github.com/googleapis/python-documentai/issues/385)) ([d65a0c7](https://github.com/googleapis/python-documentai/commit/d65a0c76a60d47fb022eeee5427e4fa517d6a363))


### Documentation

* **samples:** Added Processor Version Samples ([#382](https://github.com/googleapis/python-documentai/issues/382)) ([f9ce801](https://github.com/googleapis/python-documentai/commit/f9ce801119f96b632fddb73a4d314be1bb188639))

## [2.0.1](https://github.com/googleapis/python-documentai/compare/v2.0.0...v2.0.1) (2022-09-13)


### Documentation

* **samples:** Updated Samples for v2.0.0 Client Library ([#365](https://github.com/googleapis/python-documentai/issues/365)) ([74f2249](https://github.com/googleapis/python-documentai/commit/74f22495da86c16338ef229ccb5eebd81d36c498))

## [2.0.0](https://github.com/googleapis/python-documentai/compare/v1.5.1...v2.0.0) (2022-08-17)


### ⚠ BREAKING CHANGES

* **v1beta3:** Added Processor Management and Processor Version support to v1 library
* **v1:** Added Processor Management and Processor Version support to v1 library
* **v1beta3:** Changed the name field for ProcessRequest and BatchProcessorRequest to accept * so the name field can accept Processor and ProcessorVersion.

### Features

* **v1:** Added corrected_key_text, correct_value_text to FormField object in document.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1:** Added field_mask to ProcessRequest object in document_processor_service.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1:** Added integer_values, float_values and non_present to Entity object in document.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1:** Added OperationMetadata resource ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1:** Added parent_ids to Revision object in document.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1:** Added Processor Management and Processor Version support to v1 library ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1beta3:** Added Barcode support ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1beta3:** Added corrected_key_text, correct_value_text to FormField object in document.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1beta3:** Added integer_values, float_values and non_present to Entity object in document.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1beta3:** Added OperationMetadata resource ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1beta3:** Added parent_ids to Revision object in document.proto ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **v1beta3:** Added Processor Management and Processor Version support to v1 library ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))


### Documentation

* fix minor docstring formatting ([78e7fba](https://github.com/googleapis/python-documentai/commit/78e7fba988e73e689af5efc8780d99ae226b1b00))
* **samples:** Added Human Review Request Sample ([#357](https://github.com/googleapis/python-documentai/issues/357)) ([1a5ebea](https://github.com/googleapis/python-documentai/commit/1a5ebea358d8f63f5c048ee47efde57da9d84b2c))

## [1.5.1](https://github.com/googleapis/python-documentai/compare/v1.5.0...v1.5.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#360](https://github.com/googleapis/python-documentai/issues/360)) ([f6478ef](https://github.com/googleapis/python-documentai/commit/f6478ef23f098cb33f91b766095496580c20138f))
* **deps:** require proto-plus >= 1.22.0 ([f6478ef](https://github.com/googleapis/python-documentai/commit/f6478ef23f098cb33f91b766095496580c20138f))

## [1.5.0](https://github.com/googleapis/python-documentai/compare/v1.4.2...v1.5.0) (2022-07-15)


### Features

* add audience parameter ([a904139](https://github.com/googleapis/python-documentai/commit/a9041394c30c0312a5b920adf0639fb08a3cbdca))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#344](https://github.com/googleapis/python-documentai/issues/344)) ([a904139](https://github.com/googleapis/python-documentai/commit/a9041394c30c0312a5b920adf0639fb08a3cbdca))
* require python 3.7+ ([#348](https://github.com/googleapis/python-documentai/issues/348)) ([0613329](https://github.com/googleapis/python-documentai/commit/0613329a15c89dd371258f617c8cdc1c497d2396))

## [1.4.2](https://github.com/googleapis/python-documentai/compare/v1.4.1...v1.4.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#334](https://github.com/googleapis/python-documentai/issues/334)) ([fbdc01b](https://github.com/googleapis/python-documentai/commit/fbdc01b6670514418e32a90e39540dcb56f53048))


### Documentation

* fix changelog header to consistent size ([#333](https://github.com/googleapis/python-documentai/issues/333)) ([bf23383](https://github.com/googleapis/python-documentai/commit/bf23383b869d08bad4a6193e0596ac4e70573539))

## [1.4.1](https://github.com/googleapis/python-documentai/compare/v1.4.0...v1.4.1) (2022-04-28)


### Bug Fixes

* mark Document.Entity.type as REQUIRED in all versions ([#317](https://github.com/googleapis/python-documentai/issues/317)) ([2d82c64](https://github.com/googleapis/python-documentai/commit/2d82c64b5034bb6315031c31a11198a6f3b7f393))
* remove Document.Entity.bounding_poly_for_demo_frontend from v1beta2 ([2d82c64](https://github.com/googleapis/python-documentai/commit/2d82c64b5034bb6315031c31a11198a6f3b7f393))

## [1.4.0](https://github.com/googleapis/python-documentai/compare/v1.3.0...v1.4.0) (2022-03-19)


### Features

* add `content` field in TextAnchor ([#294](https://github.com/googleapis/python-documentai/issues/294)) ([f8b3e05](https://github.com/googleapis/python-documentai/commit/f8b3e05718d26da6711aef42d58951d275d7d87d))

## [1.3.0](https://github.com/googleapis/python-documentai/compare/v1.2.1...v1.3.0) (2022-03-05)


### Features

* add `symbols` field, and auto-format comments ([#277](https://github.com/googleapis/python-documentai/issues/277)) ([ca016dd](https://github.com/googleapis/python-documentai/commit/ca016dd0cfaa5df0e4ced218423245a5ba2eb669))
* add api key support ([#267](https://github.com/googleapis/python-documentai/issues/267)) ([061eb45](https://github.com/googleapis/python-documentai/commit/061eb454d3fafa405f90d6b73240b4c130db845f))
* add question_id field in ReviewDocumentOperationMetadata ([#269](https://github.com/googleapis/python-documentai/issues/269)) ([1c61b73](https://github.com/googleapis/python-documentai/commit/1c61b737ce02185bad04c7bd58c12e6772b8569f))
* add question_id field in ReviewDocumentOperationMetadata ([#273](https://github.com/googleapis/python-documentai/issues/273)) ([530f2ba](https://github.com/googleapis/python-documentai/commit/530f2ba88cc5abc8f888722246a3610adca001a9))


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#285](https://github.com/googleapis/python-documentai/issues/285)) ([573deee](https://github.com/googleapis/python-documentai/commit/573deee85e91a7e0a02c411703467e89be36c734))
* **deps:** require proto-plus>=1.15.0 ([573deee](https://github.com/googleapis/python-documentai/commit/573deee85e91a7e0a02c411703467e89be36c734))
* remove libcst from setup_requires ([#276](https://github.com/googleapis/python-documentai/issues/276)) ([56c96e4](https://github.com/googleapis/python-documentai/commit/56c96e4cd3427321dac0e8c979aa4e34eefa0b12))
* resolve DuplicateCredentialArgs error when using credentials_file ([530f2ba](https://github.com/googleapis/python-documentai/commit/530f2ba88cc5abc8f888722246a3610adca001a9))

## [1.2.1](https://github.com/googleapis/python-documentai/compare/v1.2.0...v1.2.1) (2022-01-17)


### Bug Fixes

* **deps:** drop packaging dependency ([038a736](https://github.com/googleapis/python-documentai/commit/038a7364fe0d2341a3bda1e40bfe23d864427ab7))
* **deps:** require google-api-core >= 1.28.0 ([038a736](https://github.com/googleapis/python-documentai/commit/038a7364fe0d2341a3bda1e40bfe23d864427ab7))

## [1.2.0](https://www.github.com/googleapis/python-documentai/compare/v1.1.0...v1.2.0) (2021-10-14)


### Features

* add support for python 3.10 ([#228](https://www.github.com/googleapis/python-documentai/issues/228)) ([86d7cd6](https://www.github.com/googleapis/python-documentai/commit/86d7cd6062d282770b0ba2252e72d5e0f90dfd95))

## [1.1.0](https://www.github.com/googleapis/python-documentai/compare/v1.0.0...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#224](https://www.github.com/googleapis/python-documentai/issues/224)) ([8b65652](https://www.github.com/googleapis/python-documentai/commit/8b6565236ec9c8f598efb55bd85937789c70fe3f))


### Bug Fixes

* add 'dict' annotation type to 'request' ([a95fac8](https://www.github.com/googleapis/python-documentai/commit/a95fac859f1c175080f6fa8c856abd64e5ea9f19))
* improper types in pagers generation ([fd5dd70](https://www.github.com/googleapis/python-documentai/commit/fd5dd70ada7caf40d3dcd4b86e71e05820d5631f))
* **v1beta2:** enable self signed jwt for grpc ([#191](https://www.github.com/googleapis/python-documentai/issues/191)) ([14e7765](https://www.github.com/googleapis/python-documentai/commit/14e77652ec6d49fc8b60808f9322004899b04cf3))
* **v1beta2:** Update DocumentUnderstandingService default_host from a regional endpoint to non-regional  ([#195](https://www.github.com/googleapis/python-documentai/issues/195)) ([090bcc5](https://www.github.com/googleapis/python-documentai/commit/090bcc568a2f448c00a0062bc0a3eddddc8ded87))

## [1.0.0](https://www.github.com/googleapis/python-documentai/compare/v0.5.0...v1.0.0) (2021-07-26)


### Features

* add always_use_jwt_access ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* add the processor management methods ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* bump release level to production/stable ([#151](https://www.github.com/googleapis/python-documentai/issues/151)) ([1e6b470](https://www.github.com/googleapis/python-documentai/commit/1e6b470673c4ff71f0f49c11825cb408d1929a88))
* Move CommonOperationMetadata for potential reuse ([#157](https://www.github.com/googleapis/python-documentai/issues/157)) ([a1a92b2](https://www.github.com/googleapis/python-documentai/commit/a1a92b20cc6afa80434a00a90690f1470ed48353))
* update ReviewDocumentRequest to allow set priority and enable validation ([#172](https://www.github.com/googleapis/python-documentai/issues/172)) ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* **v1beta3:** update document.proto, add the processor management methods ([#160](https://www.github.com/googleapis/python-documentai/issues/160)) ([54bc0e9](https://www.github.com/googleapis/python-documentai/commit/54bc0e9c70046bb411dafd53d98c501676585aaf))
* **v1:** Move CommonOperationMetadata into a separate file for potential reuse ([#158](https://www.github.com/googleapis/python-documentai/issues/158)) ([c309f8f](https://www.github.com/googleapis/python-documentai/commit/c309f8f6f88e0308677fc68a7825b3eac7b57627))


### Bug Fixes

* **deps:** add packaging requirement ([#162](https://www.github.com/googleapis/python-documentai/issues/162)) ([f09f807](https://www.github.com/googleapis/python-documentai/commit/f09f8075a3b76fe0d226afa955dae170117df0d0))
* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#180](https://www.github.com/googleapis/python-documentai/issues/180)) ([8eab36e](https://www.github.com/googleapis/python-documentai/commit/8eab36e8ff8616ccfdfd4c4149265030bab45d19))
* disable always_use_jwt_access ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* enable self signed jwt for grpc ([#184](https://www.github.com/googleapis/python-documentai/issues/184)) ([1e35b42](https://www.github.com/googleapis/python-documentai/commit/1e35b42739f36d7e1f19528299dac40de5b0cca4))
* exclude docs and tests from package ([#159](https://www.github.com/googleapis/python-documentai/issues/159)) ([1325677](https://www.github.com/googleapis/python-documentai/commit/132567742a2a9927665ed46278952815088ccafc))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-documentai/issues/1127)) ([#164](https://www.github.com/googleapis/python-documentai/issues/164)) ([baba888](https://www.github.com/googleapis/python-documentai/commit/baba888184d6cc872e048aefd52b14d2486c553f))
* add Samples section to CONTRIBUTING.rst ([#181](https://www.github.com/googleapis/python-documentai/issues/181)) ([b0f4c7a](https://www.github.com/googleapis/python-documentai/commit/b0f4c7ab32d7b864eade29e44efc1b51c80fb3e1))


## [0.5.0](https://www.github.com/googleapis/python-documentai/compare/v0.4.0...v0.5.0) (2021-05-28)


### Features

* add confidence field to the PageAnchor.PageRef in document.proto. ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))
* support self-signed JWT flow for service accounts ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))
* Use non-regionalized default host name for documentai.googleapis.com ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))


### Bug Fixes

* add async client to %name_%version/init.py ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))
* Parsing pages, but should be paragraphs ([#147](https://www.github.com/googleapis/python-documentai/issues/147)) ([c4aca1b](https://www.github.com/googleapis/python-documentai/commit/c4aca1bc1c01b3e1fdcc644eaf8922552c6c99a7))

## [0.4.0](https://www.github.com/googleapis/python-documentai/compare/v0.3.0...v0.4.0) (2021-03-25)


### Features

* add 'from_service_account_info' factory to clients ([d6f183a](https://www.github.com/googleapis/python-documentai/commit/d6f183a696b211c6d29bc28e9bbd0a8537f65577))
* add common resource path helpers, expose client transport ([#43](https://www.github.com/googleapis/python-documentai/issues/43)) ([4918e62](https://www.github.com/googleapis/python-documentai/commit/4918e62033b4c118bf99ba83730377b4ecc86d17))
* add documentai v1 ([#101](https://www.github.com/googleapis/python-documentai/issues/101)) ([74fabb5](https://www.github.com/googleapis/python-documentai/commit/74fabb5e260ecc27e9cf005502d79590fa7f72e4))
* add from_service_account_info factory and fix sphinx identifiers  ([#80](https://www.github.com/googleapis/python-documentai/issues/80)) ([d6f183a](https://www.github.com/googleapis/python-documentai/commit/d6f183a696b211c6d29bc28e9bbd0a8537f65577))


### Bug Fixes

* added if statement to filter out dir blob files ([#63](https://www.github.com/googleapis/python-documentai/issues/63)) ([7f7f541](https://www.github.com/googleapis/python-documentai/commit/7f7f541bcf4d2f42b2f619c2ceb45f53c5d0e9eb))
* adds comment with explicit hostname change ([#94](https://www.github.com/googleapis/python-documentai/issues/94)) ([bb639f9](https://www.github.com/googleapis/python-documentai/commit/bb639f9470304b9c408143a3e8091a4ca8c54160))
* fix sphinx identifiers ([d6f183a](https://www.github.com/googleapis/python-documentai/commit/d6f183a696b211c6d29bc28e9bbd0a8537f65577))
* moves import statment inside region tags ([#71](https://www.github.com/googleapis/python-documentai/issues/71)) ([a04fbea](https://www.github.com/googleapis/python-documentai/commit/a04fbeaf026d3d204dbb6c6cecf181068ddcc882))
* remove client recv msg limit and add enums to `types/__init__.py` ([#72](https://www.github.com/googleapis/python-documentai/issues/72)) ([c94afd5](https://www.github.com/googleapis/python-documentai/commit/c94afd55124b0abc8978bf86b84743dd4afb0778))
* removes C-style semicolons and slash comments ([#59](https://www.github.com/googleapis/python-documentai/issues/59)) ([1b24bfd](https://www.github.com/googleapis/python-documentai/commit/1b24bfdfc603952db8d1c633dfde108a396aa707))
* **samples:** swaps 'continue' for 'return' ([#93](https://www.github.com/googleapis/python-documentai/issues/93)) ([dabe48e](https://www.github.com/googleapis/python-documentai/commit/dabe48e8c1439ceb8a50c18aa3c7dca848a9117a))


### Documentation

* fix pypi link ([#46](https://www.github.com/googleapis/python-documentai/issues/46)) ([5162674](https://www.github.com/googleapis/python-documentai/commit/5162674091b9a2111b90eb26739b4e11f9119582))
* **samples:** new Doc AI samples for v1beta3 ([#44](https://www.github.com/googleapis/python-documentai/issues/44)) ([cc8c58d](https://www.github.com/googleapis/python-documentai/commit/cc8c58d1bade4be53fde08f6a3497eb3f79f63b1))

## [0.3.0](https://www.github.com/googleapis/python-documentai/compare/v0.2.0...v0.3.0) (2020-09-30)


### Features

* add async client ([#26](https://www.github.com/googleapis/python-documentai/issues/26)) ([ea83083](https://www.github.com/googleapis/python-documentai/commit/ea83083c315d4a97c29df35955f9547e2f869114))
* add v1beta3 ([#34](https://www.github.com/googleapis/python-documentai/issues/34)) ([6145da3](https://www.github.com/googleapis/python-documentai/commit/6145da3d5a5032f9df59ea2a499dccbf24809841))


### Bug Fixes

* **python:** change autodoc_default_flags to autodoc_default_options ([#27](https://www.github.com/googleapis/python-documentai/issues/27)) ([4eefc0a](https://www.github.com/googleapis/python-documentai/commit/4eefc0abf9a36cff8639c16c49d09487433b325b))

## [0.2.0](https://www.github.com/googleapis/python-documentai/compare/v0.1.0...v0.2.0) (2020-05-28)


### Features

* add mtls support ([#18](https://www.github.com/googleapis/python-documentai/issues/18)) ([50814b4](https://www.github.com/googleapis/python-documentai/commit/50814b448fba6c3f1da5e5ebf446bd91abff6811))

## 0.1.0 (2020-04-01)


### Features

* **documentai:** bump copyright year to 2020, tweak docstring formatting (via synth) [[#10230](https://www.github.com/googleapis/python-documentai/issues/10230)) ([329dbcf](https://www.github.com/googleapis/python-documentai/commit/329dbcfd8672cdea3a15779e7a2634f80d3d7753))
* **documentai:** initial generation of documentai ([#9623](https://www.github.com/googleapis/python-documentai/issues/9623)) ([fc3d29f](https://www.github.com/googleapis/python-documentai/commit/fc3d29fd388531b0e7d2812ceef4bc26a3cb1c7b))
* add v1beta2, remove v1beta1 ([#13](https://www.github.com/googleapis/python-documentai/issues/13)) ([1d8efd9](https://www.github.com/googleapis/python-documentai/commit/1d8efd9d74b8ae4c865751f60a01baed5a8d8d24))
