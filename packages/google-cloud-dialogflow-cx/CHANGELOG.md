# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-dialogflow-cx/#history

## [2.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.8.0...google-cloud-dialogflow-cx-v2.9.0) (2026-10-08)


### Features

* update API sources and regenerate ([#18593](https://github.com/googleapis/google-cloud-python/issues/18593)) ([d0505e8](https://github.com/googleapis/google-cloud-python/commit/d0505e8bc7615f2c649d3e25ebc7e3ccca45f22b))

## [2.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.7.0...google-cloud-dialogflow-cx-v2.8.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [2.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.6.0...google-cloud-dialogflow-cx-v2.7.0) (2026-06-25)


### Features

* update googleapis and regenerate ([#17554](https://github.com/googleapis/google-cloud-python/issues/17554)) ([03d0574](https://github.com/googleapis/google-cloud-python/commit/03d0574da8485e918f16e90666928f5c7b7f1c92))

## [2.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.5.0...google-cloud-dialogflow-cx-v2.6.0) (2026-06-02)


### Features

* regenerate google-cloud-d packages (#17092) ([d49a2b9412b4ee9105125db36104a3e18344e0ad](https://github.com/googleapis/google-cloud-python/commit/d49a2b9412b4ee9105125db36104a3e18344e0ad))

## [2.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.4.0...google-cloud-dialogflow-cx-v2.5.0) (2026-03-26)


### Features

* updated v3 dialogflow client libraries with `dtmf_pattern` and `trace_blocks` ([64582e886c1ae040afa8bf23b29bd1b8e81cebbe](https://github.com/googleapis/google-cloud-python/commit/64582e886c1ae040afa8bf23b29bd1b8e81cebbe))
* updated v3beta1 dialogflow client libraries with `dtmf_pattern` and `trace_blocks` ([64582e886c1ae040afa8bf23b29bd1b8e81cebbe](https://github.com/googleapis/google-cloud-python/commit/64582e886c1ae040afa8bf23b29bd1b8e81cebbe))
* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [2.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.3.0...google-cloud-dialogflow-cx-v2.4.0) (2026-02-19)


### Documentation

* Add comment for enum value `DETECT_INTENT_RESPONSE_VIEW_UNSPECIFIED` in enum `DetectIntentResponseView` ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))


### Features

* Add new value `DETECT_INTENT_RESPONSE_VIEW_DEFAULT` to enum `DetectIntentResponseView` ([4ca6f9e2f825c185d092f9879c05098659b1a871](https://github.com/googleapis/google-cloud-python/commit/4ca6f9e2f825c185d092f9879c05098659b1a871))

## [2.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.2.0...google-cloud-dialogflow-cx-v2.3.0) (2026-01-22)


### Features

* updated v3 dialogflow client libraries ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))


### Bug Fixes

* An existing field `webhook_latencies` is removed from message `.google.cloud.dialogflow.cx.v3.QueryResult` ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))
* An existing field `webhook_display_names` is removed from message `.google.cloud.dialogflow.cx.v3.QueryResult` ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))
* An existing field `start_flow` is moved in to oneof in message `.google.cloud.dialogflow.cx.v3.Agent` ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))
* An existing field `webhook_ids` is removed from message `.google.cloud.dialogflow.cx.v3.QueryResult` ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))
* An existing field `webhook_tags` is removed from message `.google.cloud.dialogflow.cx.v3.QueryResult` ([13f6df001f44f652e84e787f2d67d0f894ed57c4](https://github.com/googleapis/google-cloud-python/commit/13f6df001f44f652e84e787f2d67d0f894ed57c4))

## [2.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.1.0...google-cloud-dialogflow-cx-v2.2.0) (2026-01-08)


### Features

* updated v3beta1 dialogflow client libraries ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [2.1.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v2.0.0...google-cloud-dialogflow-cx-v2.1.0) (2025-12-04)


### Features

* Service Account Auth in Tools and Webhooks ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))
* add support for defining custom actions in code. See https://cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block for more information ([03e69912a61695deefca6ffaae1add8119f026e4](https://github.com/googleapis/google-cloud-python/commit/03e69912a61695deefca6ffaae1add8119f026e4))

## [2.0.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.43.0...google-cloud-dialogflow-cx-v2.0.0) (2025-10-14)


### ⚠ BREAKING CHANGES

* An existing message `PlaybookInput` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `PlaybookOutput` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `Action` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `UserUtterance` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `AgentUtterance` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `ToolUse` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `PlaybookInvocation` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing message `FlowInvocation` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto`
* An existing value `JSON` is removed from enum `DataFormat`

### Features

* add Event action to Examples ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* Add generators in fulfillment for v3beta and v3 ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* add Import/Export playbook functionality to client lib ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* add input and output parameters for Flows ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* Add parameters to adjust LLM input and output token limit and temperature in v3beta1 API ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* add prompt security settings to the SDK ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* add RestorePlaybookVersion functionality to client lib ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* add routine and task (existing) playbook types ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* Add ToolVersion APIs ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* enable unified tracing API ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* Return Vertex search document metadata with a datastore response ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* support using secret manager to manage tool/webhook credentials ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))


### Bug Fixes

* An existing message `Action` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `AgentUtterance` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `FlowInvocation` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `PlaybookInput` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `PlaybookInvocation` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `PlaybookOutput` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `ToolUse` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing message `UserUtterance` is moved from `google/cloud/dialogflow/cx/v3beta1/example.proto` to `google/cloud/dialogflow/cx/v3beta1/trace.proto` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* An existing value `JSON` is removed from enum `DataFormat` ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))


### Documentation

* A comment for field `flow` in message `.google.cloud.dialogflow.cx.v3beta1.FlowInvocation` is changed ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* A comment for message `FlowInvocation` is changed ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* A comment for message `PlaybookInvocation` is changed ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))
* Update environment documentation to add support for ToolVersions ([273fed1](https://github.com/googleapis/google-cloud-python/commit/273fed198591e948c995294868d73d34bf593302))

## [1.43.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.42.0...google-cloud-dialogflow-cx-v1.43.0) (2025-10-14)


### Features

* Add support for Python 3.14 ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))


### Bug Fixes

* Deprecate credentials_file argument ([4763aa7](https://github.com/googleapis/google-cloud-python/commit/4763aa7938438d66677f73c0775babf2ccdfe3af))

## [1.42.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.41.1...google-cloud-dialogflow-cx-v1.42.0) (2025-07-04)


### Features

* **v3:** Add support for generator settings on fulfillment ([#14054](https://github.com/googleapis/google-cloud-python/issues/14054)) ([806bd71](https://github.com/googleapis/google-cloud-python/commit/806bd717a84957789c0596a9ac4de32fdd38fbb3))

## [1.41.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.41.0...google-cloud-dialogflow-cx-v1.41.1) (2025-06-11)


### Documentation

* Update import statement example in README ([3d5bc37](https://github.com/googleapis/google-cloud-python/commit/3d5bc3782da6b37742ae83802de8a8b6db96fe29))

## [1.41.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.40.0...google-cloud-dialogflow-cx-v1.41.0) (2025-03-15)


### Features

* added support for document_processing_mode ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* Change client_secret in OAuthConfig from required to optional ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* exposed Zone Separation & Zone Isolation status of an agent ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))


### Bug Fixes

* [google-cloud-dialogflow-cx] Allow Protobuf 6.x ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))


### Documentation

* [google-cloud-dialogflow-cx] A comment for field `name` in message `.google.cloud.dialogflow.cx.v3beta1.Tool` is changed ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* A comment for field `cert` in message `.google.cloud.dialogflow.cx.v3beta1.Tool` is changed ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* A comment for field `client_secret` in message `.[google.cloud.dialogflow.cx](https://www.google.com/url?sa=D&q=http%3A%2F%2Fgoogle.cloud.dialogflow.cx).v3.Webhook` is changed ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* clarified wording around StreamingDetectIntentRequest ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))
* clarified wording around use_timeout_based_endpointing ([3609c90](https://github.com/googleapis/google-cloud-python/commit/3609c907cf4c03bf08418de150c84c32da9dae1e))

## [1.40.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.39.0...google-cloud-dialogflow-cx-v1.40.0) (2025-02-27)


### Features

* **v3:** added support for document_processing_mode ([7b2da60](https://github.com/googleapis/google-cloud-python/commit/7b2da60b07d6fab4fc46254a6c2557006df5fcba))
* **v3beta1:** added DocumentProcessingMode & BoostSpec for data stores ([8a86dba](https://github.com/googleapis/google-cloud-python/commit/8a86dba51968c017e4576da3a1058d374bc2ebf4))
* **v3beta1:** added support for answer feedback & latency metrics in conversation history ([8a86dba](https://github.com/googleapis/google-cloud-python/commit/8a86dba51968c017e4576da3a1058d374bc2ebf4))
* **v3beta1:** added support for handlers ([7b2da60](https://github.com/googleapis/google-cloud-python/commit/7b2da60b07d6fab4fc46254a6c2557006df5fcba))
* **v3beta1:** added support for playbook level speech settings ([8a86dba](https://github.com/googleapis/google-cloud-python/commit/8a86dba51968c017e4576da3a1058d374bc2ebf4))
* **v3:** exposed Zone Separation & Zone Isolation status of an agent ([7b2da60](https://github.com/googleapis/google-cloud-python/commit/7b2da60b07d6fab4fc46254a6c2557006df5fcba))


### Documentation

* **v3:** clarified wording around StreamingDetectIntentRequest ([7b2da60](https://github.com/googleapis/google-cloud-python/commit/7b2da60b07d6fab4fc46254a6c2557006df5fcba))
* **v3:** clarified wording around use_timeout_based_endpointing ([7b2da60](https://github.com/googleapis/google-cloud-python/commit/7b2da60b07d6fab4fc46254a6c2557006df5fcba))

## [1.39.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.38.0...google-cloud-dialogflow-cx-v1.39.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))
* Add support for reading selective GAPIC generation methods from service YAML ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))

## [1.38.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.37.0...google-cloud-dialogflow-cx-v1.38.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [1.37.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.36.0...google-cloud-dialogflow-cx-v1.37.0) (2024-11-11)


### Features

* add options of client_certificate_settings, bigquery_export_settings, bearer_token_config and boost_control_spec; add support of ALAW encoding ([3e438ff](https://github.com/googleapis/google-cloud-python/commit/3e438ff52c5b3c436cf8e46d82c54b9caf77a658))


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))

## [1.36.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.35.0...google-cloud-dialogflow-cx-v1.36.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [1.35.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.34.1...google-cloud-dialogflow-cx-v1.35.0) (2024-07-30)


### Features

* [google-cloud-dialogflow-cx] exposed DataStoreConnectionSignals ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* added support for lock flow ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* added support for multi language settings in flow ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* added support for oauth and service agent auth for webhook. ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* added support for service directory in tools ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* expose PersonalizationSettings & SpeechSettings in v3 API. ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* expose store tts option in security settings ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([52db52e](https://github.com/googleapis/google-cloud-python/commit/52db52ea05c6883b07956d323fdd1d3029806374))


### Documentation

* clarified wording around audio redaction ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* clarified wording around enable_stackdriver_logging & enable_interaction_logging ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))
* clarified wording around start point of test config. ([fbe3394](https://github.com/googleapis/google-cloud-python/commit/fbe33947332e5477afc35a31815853840598c319))

## [1.34.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.34.0...google-cloud-dialogflow-cx-v1.34.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## [1.34.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.33.0...google-cloud-dialogflow-cx-v1.34.0) (2024-06-25)


### Features

* A new field `action_parameters` is added to message `.google.cloud.dialogflow.cx.v3beta1.PlaybookInput` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `action_parameters` is added to message `.google.cloud.dialogflow.cx.v3beta1.PlaybookOutput` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `endpointing_timeout_duration` is added to message `.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `input_action_parameters` is added to message `.google.cloud.dialogflow.cx.v3beta1.FlowInvocation` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `input_action_parameters` is added to message `.google.cloud.dialogflow.cx.v3beta1.ToolUse` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `instruction` is added to message `.google.cloud.dialogflow.cx.v3beta1.Playbook` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `interdigit_timeout_duration` is added to message `.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `output_action_parameters` is added to message `.google.cloud.dialogflow.cx.v3beta1.FlowInvocation` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `output_action_parameters` is added to message `.google.cloud.dialogflow.cx.v3beta1.ToolUse` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `store_tts_audio` is added to message `.google.cloud.dialogflow.cx.v3beta1.SecuritySettings` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new field `tool_call` is added to message `.google.cloud.dialogflow.cx.v3beta1.ResponseMessage` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new message `Instruction` is added ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new message `ToolCall` is added ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A new value `PLAYBOOK` is added to enum `MatchType` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* added Conversation History API ([40d47d2](https://github.com/googleapis/google-cloud-python/commit/40d47d2ff0018e0ea4ddedfd7427e698aba3e533))
* added Language Info to webhook Request ([40d47d2](https://github.com/googleapis/google-cloud-python/commit/40d47d2ff0018e0ea4ddedfd7427e698aba3e533))


### Bug Fixes

* An existing field `actions` is removed from message `.google.cloud.dialogflow.cx.v3beta1.Tool` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `input_parameters` is removed from message `.google.cloud.dialogflow.cx.v3beta1.FlowInvocation` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `input_parameters` is removed from message `.google.cloud.dialogflow.cx.v3beta1.ToolUse` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `output_parameters` is removed from message `.google.cloud.dialogflow.cx.v3beta1.FlowInvocation` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `output_parameters` is removed from message `.google.cloud.dialogflow.cx.v3beta1.ToolUse` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `parameters` is removed from message `.google.cloud.dialogflow.cx.v3beta1.PlaybookInput` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `parameters` is removed from message `.google.cloud.dialogflow.cx.v3beta1.PlaybookOutput` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `schemas` is removed from message `.google.cloud.dialogflow.cx.v3beta1.Tool` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `start_playbook` is moved in to oneof in message `.google.cloud.dialogflow.cx.v3beta1.Agent` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field `steps` is removed from message `.google.cloud.dialogflow.cx.v3beta1.Playbook` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing field start_flow is moved in to oneof in message `.google.cloud.dialogflow.cx.v3beta1.Agent` ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* An existing message `ActionParameter` is removed ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))


### Documentation

* A comment for field `start_flow` in message `.google.cloud.dialogflow.cx.v3beta1.Agent` is changed ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* A comment for field `start_playbook` in message `.google.cloud.dialogflow.cx.v3beta1.Agent` is changed ([119b895](https://github.com/googleapis/google-cloud-python/commit/119b895d5e7bf87fcc86de278fd3ff1b9407c3f6))
* improve doc for SecuritySetting.retention_window_days ([40d47d2](https://github.com/googleapis/google-cloud-python/commit/40d47d2ff0018e0ea4ddedfd7427e698aba3e533))

## [1.33.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.32.1...google-cloud-dialogflow-cx-v1.33.0) (2024-03-27)


### Features

* added support for DataStoreConnection, DataStoreConnectionSettings ([ce2c9ed](https://github.com/googleapis/google-cloud-python/commit/ce2c9edf1d4377cd096c6a314b8e297cc44a2ca6))
* added support for MultiLanguageSettings ([ce2c9ed](https://github.com/googleapis/google-cloud-python/commit/ce2c9edf1d4377cd096c6a314b8e297cc44a2ca6))
* added support for PersonalizationSettings ([ce2c9ed](https://github.com/googleapis/google-cloud-python/commit/ce2c9edf1d4377cd096c6a314b8e297cc44a2ca6))
* added support for SpeechSettings ([ce2c9ed](https://github.com/googleapis/google-cloud-python/commit/ce2c9edf1d4377cd096c6a314b8e297cc44a2ca6))
* added support for Webhook OAuthConfig, and ServiceAgentAuth Settings. ([ce2c9ed](https://github.com/googleapis/google-cloud-python/commit/ce2c9edf1d4377cd096c6a314b8e297cc44a2ca6))


### Documentation

* clarified wording around quota usage ([ce2c9ed](https://github.com/googleapis/google-cloud-python/commit/ce2c9edf1d4377cd096c6a314b8e297cc44a2ca6))

## [1.32.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.32.0...google-cloud-dialogflow-cx-v1.32.1) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12390](https://github.com/googleapis/google-cloud-python/issues/12390)) ([25c291a](https://github.com/googleapis/google-cloud-python/commit/25c291afa9facc72f4af80b9c2721efe24b02953))

## [1.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.31.1...google-cloud-dialogflow-cx-v1.32.0) (2024-02-22)


### Features

* A new field `current_flow` is added to message `.google.cloud.dialogflow.cx.v3.QueryResult` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `description` is added to message `.google.cloud.dialogflow.cx.v3.Page` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `disable_data_store_fallback` is added to message `.google.cloud.dialogflow.cx.v3.GenerativeSettings` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `language_code` is added to message `Changelog` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `opt_out_conformer_model_migration` is added to message `InputAudioConfig` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `webhook_display_names` is added to message `.google.cloud.dialogflow.cx.v3.QueryResult` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `webhook_ids` is added to message `.google.cloud.dialogflow.cx.v3.QueryResult` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `webhook_latencies` is added to message `.google.cloud.dialogflow.cx.v3.QueryResult` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new field `webhook_tags` is added to message `.google.cloud.dialogflow.cx.v3.QueryResult` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new message `ExportEntityTypesMetadata` is added ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new message `ExportEntityTypesRequest` is added ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new message `ExportEntityTypesResponse` is added ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new message `ImportEntityTypesMetadata` is added ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new message `ImportEntityTypesRequest` is added ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new message `ImportEntityTypesResponse` is added ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new method `ExportEntityTypes` is added to service `EntityTypes` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new method `ImportEntityTypes` is added to service `EntityTypes` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A new method `ServerStreamingDetectIntent` is added to service `Sessions` ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* Public preview the  Dialogflow LLM based agent ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12306](https://github.com/googleapis/google-cloud-python/issues/12306)) ([1e787f2](https://github.com/googleapis/google-cloud-python/commit/1e787f2079ac41ce634c7b90f02a6597cecb64be))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))
* Require google-api-core&gt;=1.34.1 ([#12313](https://github.com/googleapis/google-cloud-python/issues/12313)) ([b099445](https://github.com/googleapis/google-cloud-python/commit/b0994458dd4c7d8a7e7d93ebce10b4b08e811bf5))


### Documentation

* A comment for enum value `END_OF_SINGLE_UTTERANCE` in enum `MessageType` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for enum value `END_OF_SINGLE_UTTERANCE` in enum `MessageType` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for enum value `USE_BEST_AVAILABLE` in enum `SpeechModelVariant` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for enum value `USE_BEST_AVAILABLE` in enum `SpeechModelVariant` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for enum value `USE_ENHANCED` in enum `SpeechModelVariant` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for enum value `USE_ENHANCED` in enum `SpeechModelVariant` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `model` in message `.google.cloud.dialogflow.cx.v3.InputAudioConfig` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `model` in message `.google.cloud.dialogflow.cx.v3beta1.InputAudioConfig` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `session_ttl` in message `.google.cloud.dialogflow.cx.v3.QueryParameters` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `session_ttl` in message `.google.cloud.dialogflow.cx.v3beta1.QueryParameters` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `start_flow` in message `.google.cloud.dialogflow.cx.v3.Agent` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `start_flow` in message `.google.cloud.dialogflow.cx.v3beta1.Agent` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `text` in message `.google.cloud.dialogflow.cx.v3.TextInput` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for field `text` in message `.google.cloud.dialogflow.cx.v3beta1.TextInput` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for message `QueryInput` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))
* A comment for message `QueryInput` is changed ([e1dbb80](https://github.com/googleapis/google-cloud-python/commit/e1dbb8098ca8d4f8b19695c1b2b11e06e7c84e01))

## [1.31.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.31.0...google-cloud-dialogflow-cx-v1.31.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([d72e64c](https://github.com/googleapis/google-cloud-python/commit/d72e64c7dc1de6e2a097d4920496de34ebf13c7d))
* Add google-auth as a direct dependency ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([d72e64c](https://github.com/googleapis/google-cloud-python/commit/d72e64c7dc1de6e2a097d4920496de34ebf13c7d))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([d72e64c](https://github.com/googleapis/google-cloud-python/commit/d72e64c7dc1de6e2a097d4920496de34ebf13c7d))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([c721248](https://github.com/googleapis/google-cloud-python/commit/c721248accc77f0b1fba9605a65ea95a86f023a5))

## [1.31.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.30.1...google-cloud-dialogflow-cx-v1.31.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12239](https://github.com/googleapis/google-cloud-python/issues/12239)) ([8004d15](https://github.com/googleapis/google-cloud-python/commit/8004d15d9e6baa4dc5bc3f09d528e176d54d9ec5))

## [1.30.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.30.0...google-cloud-dialogflow-cx-v1.30.1) (2024-01-12)


### Documentation

* [google-cloud-dialogflow-cx] Fix formatting due to unclosed backtick ([#12175](https://github.com/googleapis/google-cloud-python/issues/12175)) ([a43fa12](https://github.com/googleapis/google-cloud-python/commit/a43fa123a21739e83e10fd0328a56039690d800c))

## [1.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.29.0...google-cloud-dialogflow-cx-v1.30.0) (2023-12-07)


### Features

* Add DirectPredict to PredictionService ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Add DirectRawPredict to PredictionService ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Add grpc_ports to UploadModel ModelContainerSpec ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Add StreamingPredict to PredictionService. ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Add StreamingRawPredict to PredictionService. ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Add support for python 3.12 ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Added Generator API  ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Introduce compatibility with native namespace packages ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))
* Use `retry_async` instead of `retry` in async client ([15b4370](https://github.com/googleapis/google-cloud-python/commit/15b437074ad6f4029d6e4d1d9bca0cd88985a2dc))

## [1.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.28.0...google-cloud-dialogflow-cx-v1.29.0) (2023-11-29)


### Features

* add agent answer feedback capabilit ([080c0cc](https://github.com/googleapis/google-cloud-python/commit/080c0cc198efb69d129845bc289eba2100ea69c0))
* add boost & bury and filter ES controls ([080c0cc](https://github.com/googleapis/google-cloud-python/commit/080c0cc198efb69d129845bc289eba2100ea69c0))
* add end_user_metadata to QueryParameters ([080c0cc](https://github.com/googleapis/google-cloud-python/commit/080c0cc198efb69d129845bc289eba2100ea69c0))
* add fields for supporting barge-in in StreamingDetectIntent API ([080c0cc](https://github.com/googleapis/google-cloud-python/commit/080c0cc198efb69d129845bc289eba2100ea69c0))
* added Generator API  ([5fc7b7b](https://github.com/googleapis/google-cloud-python/commit/5fc7b7bc10861ffb015acc0a57f5976251be7fdc))


### Documentation

* updated doc for speech model ([5fc7b7b](https://github.com/googleapis/google-cloud-python/commit/5fc7b7bc10861ffb015acc0a57f5976251be7fdc))

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.27.1...google-cloud-dialogflow-cx-v1.28.0) (2023-09-30)


### Features

* add Inline destination ([40ee037](https://github.com/googleapis/google-cloud-python/commit/40ee0379f427d3426d2d41e45fdbe076b4f8eed4))
* add Intent import/export APIs ([40ee037](https://github.com/googleapis/google-cloud-python/commit/40ee0379f427d3426d2d41e45fdbe076b4f8eed4))
* add support for AdvancedSettings ([40ee037](https://github.com/googleapis/google-cloud-python/commit/40ee0379f427d3426d2d41e45fdbe076b4f8eed4))

## [1.27.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.27.0...google-cloud-dialogflow-cx-v1.27.1) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [1.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dialogflow-cx-v1.26.0...google-cloud-dialogflow-cx-v1.27.0) (2023-08-31)


### Features

* added generative AI, safety/security and speech endpointing settings ([#11614](https://github.com/googleapis/google-cloud-python/issues/11614)) ([85fb0fe](https://github.com/googleapis/google-cloud-python/commit/85fb0fe9ba4215e9f0daea49270af9b1d1664c7a))
* added generative AI, safety/security and speech endpointing settings ([#11621](https://github.com/googleapis/google-cloud-python/issues/11621)) ([f0a5399](https://github.com/googleapis/google-cloud-python/commit/f0a539993f9baac2b32fc13d2297ee9deb623186))

## [1.26.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.25.0...v1.26.0) (2023-08-10)


### Features

* Added agent level route group ([30e8c2b](https://github.com/googleapis/python-dialogflow-cx/commit/30e8c2b6d687e35168801660be70caa52131ff17))
* Added flow import strategy ([30e8c2b](https://github.com/googleapis/python-dialogflow-cx/commit/30e8c2b6d687e35168801660be70caa52131ff17))

## [1.25.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.24.0...v1.25.0) (2023-07-11)


### Features

* **v3:** Added GitIntegrationSettings to the Agent ([#535](https://github.com/googleapis/python-dialogflow-cx/issues/535)) ([32b4a66](https://github.com/googleapis/python-dialogflow-cx/commit/32b4a668d5acd07b5f6f431e816fcfac9bb3053b))

## [1.24.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.23.1...v1.24.0) (2023-07-10)


### Features

* **v3beta1:** Added GitIntegrationSettings to the Agent ([#531](https://github.com/googleapis/python-dialogflow-cx/issues/531)) ([5938750](https://github.com/googleapis/python-dialogflow-cx/commit/59387500bead38b100815003a3cf14d90de36789))

## [1.23.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.23.0...v1.23.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#529](https://github.com/googleapis/python-dialogflow-cx/issues/529)) ([e5e5ceb](https://github.com/googleapis/python-dialogflow-cx/commit/e5e5ceb35fd307b7395124dee961df545567fc11))

## [1.23.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.22.0...v1.23.0) (2023-06-19)


### Features

* Added include_bigquery_export_settings to ExportAgentRequest ([9878beb](https://github.com/googleapis/python-dialogflow-cx/commit/9878beb7644c52032a906e89d7de1524d71b5197))
* Added session_ttl to SessionProto ([9878beb](https://github.com/googleapis/python-dialogflow-cx/commit/9878beb7644c52032a906e89d7de1524d71b5197))

## [1.22.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.21.0...v1.22.0) (2023-06-13)


### Features

* Add support for flexible webhook ([ba8d7d3](https://github.com/googleapis/python-dialogflow-cx/commit/ba8d7d341063fcd2ed1591ea84efb395340bc960))


### Documentation

* Update synthesize speech configs's documentation ([ba8d7d3](https://github.com/googleapis/python-dialogflow-cx/commit/ba8d7d341063fcd2ed1591ea84efb395340bc960))

## [1.21.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.20.1...v1.21.0) (2023-05-25)


### Features

* Added debug info to StreamingDetectIntent ([6da4342](https://github.com/googleapis/python-dialogflow-cx/commit/6da4342f5f835f1dd36570d7243852ba9d8afde5))
* Added dtmf digits to WebhookRequest ([6da4342](https://github.com/googleapis/python-dialogflow-cx/commit/6da4342f5f835f1dd36570d7243852ba9d8afde5))
* Added FLOW as a new DiffType in TestRunDifference ([6da4342](https://github.com/googleapis/python-dialogflow-cx/commit/6da4342f5f835f1dd36570d7243852ba9d8afde5))
* Extended CreateAgent timeout to 180 seconds ([6da4342](https://github.com/googleapis/python-dialogflow-cx/commit/6da4342f5f835f1dd36570d7243852ba9d8afde5))

## [1.20.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.20.0...v1.20.1) (2023-03-23)


### Documentation

* Add clarification in AudioInput ([#511](https://github.com/googleapis/python-dialogflow-cx/issues/511)) ([fc0ecdf](https://github.com/googleapis/python-dialogflow-cx/commit/fc0ecdf2f3d29f23de45e6bd44f1c1ec17ddb4ef))
* Clarified wording around quota usage ([#515](https://github.com/googleapis/python-dialogflow-cx/issues/515)) ([361a359](https://github.com/googleapis/python-dialogflow-cx/commit/361a359e60c8953453a6837e3e5f1916fad76095))
* Minor formatting changes ([#517](https://github.com/googleapis/python-dialogflow-cx/issues/517)) ([b05b15f](https://github.com/googleapis/python-dialogflow-cx/commit/b05b15f2ac54ffd83a33ee0829cab395f157a42f))

## [1.20.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.19.0...v1.20.0) (2023-03-01)


### Features

* Added persist_parameter_changes field from `query_params` to MatchIntentRequest ([#506](https://github.com/googleapis/python-dialogflow-cx/issues/506)) ([27f6020](https://github.com/googleapis/python-dialogflow-cx/commit/27f60205a3068df1a1576f120c97d45bb3501b2a))

## [1.19.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.18.0...v1.19.0) (2023-02-28)


### Features

* Added gcs.proto. added support for GcsDestination and TextToSpeechSettings ([acfd1a1](https://github.com/googleapis/python-dialogflow-cx/commit/acfd1a11aca9c9cba7fb351f1781fa73c1e1d985))
* Added persist_parameter_changes field from query_params to MatchIntentRequest  ([acfd1a1](https://github.com/googleapis/python-dialogflow-cx/commit/acfd1a11aca9c9cba7fb351f1781fa73c1e1d985))
* Enable "rest" transport in Python for services supporting numeric enums ([acfd1a1](https://github.com/googleapis/python-dialogflow-cx/commit/acfd1a11aca9c9cba7fb351f1781fa73c1e1d985))
* Remove [REQUIRED] for VersionConfig ([acfd1a1](https://github.com/googleapis/python-dialogflow-cx/commit/acfd1a11aca9c9cba7fb351f1781fa73c1e1d985))


### Documentation

* Add more meaningful comments ([acfd1a1](https://github.com/googleapis/python-dialogflow-cx/commit/acfd1a11aca9c9cba7fb351f1781fa73c1e1d985))

## [1.18.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.17.1...v1.18.0) (2023-01-30)


### Features

* Added JSON_PACKAGE field to ExportAgentRequest ([#497](https://github.com/googleapis/python-dialogflow-cx/issues/497)) ([efe6286](https://github.com/googleapis/python-dialogflow-cx/commit/efe628674806271f5584b10eca899745fa190258))
* **v3beta1:** Added JSON_PACKAGE field to ExportAgentRequest ([#495](https://github.com/googleapis/python-dialogflow-cx/issues/495)) ([d03ec56](https://github.com/googleapis/python-dialogflow-cx/commit/d03ec56bf21d0ce601c5a5029bcf4219b9372254))

## [1.17.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.17.0...v1.17.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([dc4f8e2](https://github.com/googleapis/python-dialogflow-cx/commit/dc4f8e26bd7f38ec3cafe4d358d8852ca8ea8a84))


### Documentation

* Add documentation for enums ([dc4f8e2](https://github.com/googleapis/python-dialogflow-cx/commit/dc4f8e26bd7f38ec3cafe4d358d8852ca8ea8a84))

## [1.17.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.16.0...v1.17.0) (2023-01-14)


### Features

* **v3:** ResponseMessage proto contains channel information ([#488](https://github.com/googleapis/python-dialogflow-cx/issues/488)) ([a685e8c](https://github.com/googleapis/python-dialogflow-cx/commit/a685e8c8e2ed20325a0adddfdb6691030bd923b9))

## [1.16.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.15.0...v1.16.0) (2023-01-12)


### Features

* **v3beta1:** ResponseMessage proto contains channel information ([#485](https://github.com/googleapis/python-dialogflow-cx/issues/485)) ([242abc6](https://github.com/googleapis/python-dialogflow-cx/commit/242abc60b7402dc1937105b34c88cf1b75d704da))

## [1.15.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.14.1...v1.15.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#482](https://github.com/googleapis/python-dialogflow-cx/issues/482)) ([1b846d2](https://github.com/googleapis/python-dialogflow-cx/commit/1b846d292e7ec8deb555d489c8adde0d6817f47f))

## [1.14.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.14.0...v1.14.1) (2023-01-06)


### Documentation

* **samples:** Update previous month logic to avoid zero-index bug in webhook_prebuilt_telecom sample ([#479](https://github.com/googleapis/python-dialogflow-cx/issues/479)) ([38c188a](https://github.com/googleapis/python-dialogflow-cx/commit/38c188ac7ec89471fdaff3981e8e66c820ff683c))

## [1.14.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.5...v1.14.0) (2022-12-15)


### Features

* Add files field to finding's list of attributes ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Add support for `google.cloud.dialogflowcx.__version__` ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Add typing to proto.Message based class attributes ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))


### Bug Fixes

* Add dict typing for client_options ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Drop usage of pkg_resources ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Fix timeout default values ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))


### Documentation

* Clarified Agent Assist max retention is 30 days ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Clarify interactive logging TTL behavior ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* **samples:** Snippetgen handling of repeated enum field ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))

## [1.13.5](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.4...v1.13.5) (2022-10-26)


### Documentation

* Clarified TTL as time-to-live ([#465](https://github.com/googleapis/python-dialogflow-cx/issues/465)) ([5e8fc34](https://github.com/googleapis/python-dialogflow-cx/commit/5e8fc34f7a40351c2a3092fb835bf8ac0f3e63d1))

## [1.13.4](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.3...v1.13.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#462](https://github.com/googleapis/python-dialogflow-cx/issues/462)) ([8cd6d6d](https://github.com/googleapis/python-dialogflow-cx/commit/8cd6d6df6c19b93e8116e968fb63292153a019b7))

## [1.13.3](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.2...v1.13.3) (2022-10-04)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#458](https://github.com/googleapis/python-dialogflow-cx/issues/458)) ([07e19d4](https://github.com/googleapis/python-dialogflow-cx/commit/07e19d476e3382ead73b44f4bc8b84e230aa6115))


### Documentation

* Clarified gcs_bucket field of the SecuritySettings message ([#460](https://github.com/googleapis/python-dialogflow-cx/issues/460)) ([f922211](https://github.com/googleapis/python-dialogflow-cx/commit/f922211c6dde44572303926f9456d040e041a224))
* **samples:** Adding snippet to extract SessionInfo ([d6ef048](https://github.com/googleapis/python-dialogflow-cx/commit/d6ef04841975e9076c940802283d1a9ba8e05eb4))

## [1.13.2](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.1...v1.13.2) (2022-09-02)


### Documentation

* **samples:** Add prebuilt telecom agent webhook code in python ([#434](https://github.com/googleapis/python-dialogflow-cx/issues/434)) ([45926d2](https://github.com/googleapis/python-dialogflow-cx/commit/45926d2fd7bcfb49785ad339e7141349e31f91b4))

## [1.13.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.0...v1.13.1) (2022-08-15)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#435](https://github.com/googleapis/python-dialogflow-cx/issues/435)) ([519012b](https://github.com/googleapis/python-dialogflow-cx/commit/519012bf13179d4fdbe6856ca21fd539b4f776b1))
* **deps:** require proto-plus >= 1.22.0 ([519012b](https://github.com/googleapis/python-dialogflow-cx/commit/519012bf13179d4fdbe6856ca21fd539b4f776b1))

## [1.13.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.12.1...v1.13.0) (2022-07-15)


### Features

* add audience parameter ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* **v3:** added webhook_config ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* **v3beta1:** added webhook_config ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0  ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* require python 3.7+ ([4746c9f](https://github.com/googleapis/python-dialogflow-cx/commit/4746c9f1c34e54892c64857751b84b204b6a8871))


### Documentation

* add detect intent with intent input snippet ([#417](https://github.com/googleapis/python-dialogflow-cx/issues/417)) ([04ded3c](https://github.com/googleapis/python-dialogflow-cx/commit/04ded3ce2cdee30bdf0dd91f7164d32fcda204bd))
* add detect intent with sentiment analysis snippet ([#416](https://github.com/googleapis/python-dialogflow-cx/issues/416)) ([dcd8319](https://github.com/googleapis/python-dialogflow-cx/commit/dcd8319e2edef2e99dffea50b202f9b7f5a52c06))
* add detect intent with text-to-speech synthesized output snippet ([#419](https://github.com/googleapis/python-dialogflow-cx/issues/419)) ([ac6aae4](https://github.com/googleapis/python-dialogflow-cx/commit/ac6aae4fa4607bf17aa9934ccba440d976b25f17))
* Add dialogflow cx detect intent with disabled webhook snippet ([#422](https://github.com/googleapis/python-dialogflow-cx/issues/422)) ([406e84d](https://github.com/googleapis/python-dialogflow-cx/commit/406e84dabb889c8f43d4084c6e4ed39fbc6d4ee0))
* add streaming detect intent with partial response sample ([#414](https://github.com/googleapis/python-dialogflow-cx/issues/414)) ([57a0e16](https://github.com/googleapis/python-dialogflow-cx/commit/57a0e16995bf2520306c8d29ee84088345a9b3be))
* clarify descriptions of the AdvancedSettings and WebhookRequest data types ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* Dialogflow cx v3 detect intent event input snippet ([#421](https://github.com/googleapis/python-dialogflow-cx/issues/421)) ([0524558](https://github.com/googleapis/python-dialogflow-cx/commit/052455829c99ff0838a5a140a0496bcff4a45178))
* improve comments for protos ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* Update region_tag: dialogflow_detect_intent_text --> dialogflow_cx_detect_intent_text ([#424](https://github.com/googleapis/python-dialogflow-cx/issues/424)) ([dd2257c](https://github.com/googleapis/python-dialogflow-cx/commit/dd2257c850059e1cb63c11326dd760665079c32b))

## [1.12.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.12.0...v1.12.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#396](https://github.com/googleapis/python-dialogflow-cx/issues/396)) ([51be5ca](https://github.com/googleapis/python-dialogflow-cx/commit/51be5ca187e68f17af53e6a41e59bb4cc04086c1))


### Documentation

* fix changelog header to consistent size ([#395](https://github.com/googleapis/python-dialogflow-cx/issues/395)) ([f21bc73](https://github.com/googleapis/python-dialogflow-cx/commit/f21bc7349da7fabe50cc5fb846db43e15da8b71d))

## [1.12.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.11.0...v1.12.0) (2022-05-09)


### Features

* **v3beta1:** added audio_export_settings ([#311](https://github.com/googleapis/python-dialogflow-cx/issues/311)) ([228ae83](https://github.com/googleapis/python-dialogflow-cx/commit/228ae8310b71412c1636a5ef214f62dad6473e40))


### Documentation

* **v3:** update the doc on diagnostic info ([#314](https://github.com/googleapis/python-dialogflow-cx/issues/314)) ([6109b64](https://github.com/googleapis/python-dialogflow-cx/commit/6109b64efb85480fdd9793476db14e65c40a0333))

## [1.11.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.10.0...v1.11.0) (2022-05-03)


### Features

* added data format specification for export agent ([1844193](https://github.com/googleapis/python-dialogflow-cx/commit/1844193788ce3d9f66f2822846b31f469f34f530))
* **v3:** add support for locking an agent for changes ([#276](https://github.com/googleapis/python-dialogflow-cx/issues/276)) ([1844193](https://github.com/googleapis/python-dialogflow-cx/commit/1844193788ce3d9f66f2822846b31f469f34f530))
* **v3:** added audio_export_settings ([#300](https://github.com/googleapis/python-dialogflow-cx/issues/300)) ([b225dfe](https://github.com/googleapis/python-dialogflow-cx/commit/b225dfe9371e89ee54e483888b7ed36d8374e011))
* **v3beta1:** added data format specification for export agent ([72e624a](https://github.com/googleapis/python-dialogflow-cx/commit/72e624ae6430fd454380cdf6e348dbe763e56e6f))
* **v3beta1:** added support for locking an agent for changes ([#281](https://github.com/googleapis/python-dialogflow-cx/issues/281)) ([72e624a](https://github.com/googleapis/python-dialogflow-cx/commit/72e624ae6430fd454380cdf6e348dbe763e56e6f))


### Documentation

* improved docs format ([#275](https://github.com/googleapis/python-dialogflow-cx/issues/275)) ([560e6a4](https://github.com/googleapis/python-dialogflow-cx/commit/560e6a478a7daaf1ac9fac23ca01390a6e7699a7))
* minor wording update ([#294](https://github.com/googleapis/python-dialogflow-cx/issues/294)) ([f660888](https://github.com/googleapis/python-dialogflow-cx/commit/f660888d55f5aab2b40d5e7f0b214e3e8ba01864))
* **samples:** Adds snippet for configuring a webhook to enable an agent response. ([#306](https://github.com/googleapis/python-dialogflow-cx/issues/306)) ([c0cc924](https://github.com/googleapis/python-dialogflow-cx/commit/c0cc924a257740e68d244c265c6406a8d6888cc5))
* **samples:** Adds snippet for configuring optional or required form parameters ([#305](https://github.com/googleapis/python-dialogflow-cx/issues/305)) ([720c0bd](https://github.com/googleapis/python-dialogflow-cx/commit/720c0bdd0f5707a2c71c9d32a91f06f86c48a98e))
* **samples:** Adds snippet for validating a form parameter. ([#302](https://github.com/googleapis/python-dialogflow-cx/issues/302)) ([8cfe6a1](https://github.com/googleapis/python-dialogflow-cx/commit/8cfe6a15b18b558faa2cd5ceb8dc7b291add4444))
* **samples:** Configure session parameters snippet ([#303](https://github.com/googleapis/python-dialogflow-cx/issues/303)) ([ace3936](https://github.com/googleapis/python-dialogflow-cx/commit/ace393696fdec8040bd5b23daa09f80183ad9125))
* **samples:** Configure session parameters trigger transition ([#304](https://github.com/googleapis/python-dialogflow-cx/issues/304)) ([d6cab9d](https://github.com/googleapis/python-dialogflow-cx/commit/d6cab9dd6db83aea15548795a0fc449f72a2b56f))
* **v3beta1:** added explanation for uri fields in resources ([#273](https://github.com/googleapis/python-dialogflow-cx/issues/273)) ([01b0f8f](https://github.com/googleapis/python-dialogflow-cx/commit/01b0f8f795d06609b370ba7568db753152764d9b))
* **v3beta1:** improved docs format ([01b0f8f](https://github.com/googleapis/python-dialogflow-cx/commit/01b0f8f795d06609b370ba7568db753152764d9b))

## [1.10.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.9.1...v1.10.0) (2022-03-10)


### Features

* added page in TestConfig ([#268](https://github.com/googleapis/python-dialogflow-cx/issues/268)) ([61fd2dc](https://github.com/googleapis/python-dialogflow-cx/commit/61fd2dc3512e4bcfdfc51cf085cc12cbbf1e043b))
* **v3beta1:** added page in TestConfig ([#270](https://github.com/googleapis/python-dialogflow-cx/issues/270)) ([a81f0c2](https://github.com/googleapis/python-dialogflow-cx/commit/a81f0c23d5dc835bd6abdccd546ef00f6c421a74))


### Documentation

* clarified wording around Cloud Storage usage ([61fd2dc](https://github.com/googleapis/python-dialogflow-cx/commit/61fd2dc3512e4bcfdfc51cf085cc12cbbf1e043b))

## [1.9.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.9.0...v1.9.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#263](https://github.com/googleapis/python-dialogflow-cx/issues/263)) ([6235775](https://github.com/googleapis/python-dialogflow-cx/commit/623577550fc96786c2142d971dea4c31c116181a))
* **deps:** require proto-plus>=1.15.0 ([6235775](https://github.com/googleapis/python-dialogflow-cx/commit/623577550fc96786c2142d971dea4c31c116181a))

## [1.9.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.8.0...v1.9.0) (2022-02-26)


### Features

* add api_key support ([#240](https://github.com/googleapis/python-dialogflow-cx/issues/240)) ([cf95791](https://github.com/googleapis/python-dialogflow-cx/commit/cf9579171290ecf5afeeb6a38a3504857808a4ef))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([f3bf440](https://github.com/googleapis/python-dialogflow-cx/commit/f3bf440a081622dfc6d8d8e385f2edb5c3e11202))


### Documentation

* add autogenerated code snippets ([2292ff5](https://github.com/googleapis/python-dialogflow-cx/commit/2292ff540aea24c3c831a5ffe1604c2c022ccb82))

## [1.8.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.7.0...v1.8.0) (2022-01-14)


### Features

* **v3:** added `TelephonyTransferCall` in response message ([#216](https://github.com/googleapis/python-dialogflow-cx/issues/216)) ([76dae8b](https://github.com/googleapis/python-dialogflow-cx/commit/76dae8b03c0e3bf33123b8001e3f8d40701b5c19))
* **v3:** added the display name of the current page in webhook requests ([#221](https://github.com/googleapis/python-dialogflow-cx/issues/221)) ([aa91b72](https://github.com/googleapis/python-dialogflow-cx/commit/aa91b729ffa07230b011a61d3eb1521f59345fc1))
* **v3:** allow setting custom CA for generic webhooks ([#214](https://github.com/googleapis/python-dialogflow-cx/issues/214)) ([8f3dc03](https://github.com/googleapis/python-dialogflow-cx/commit/8f3dc03835b5bb5baa36224a274f24dda7aa3709))
* **v3beta1:** added `TelephonyTransferCall` in response message ([#217](https://github.com/googleapis/python-dialogflow-cx/issues/217)) ([e24bdfd](https://github.com/googleapis/python-dialogflow-cx/commit/e24bdfd499952199dfbdaa5634061653da8ae1db))
* **v3beta1:** added the display name of the current page in webhook requests ([#222](https://github.com/googleapis/python-dialogflow-cx/issues/222)) ([5956179](https://github.com/googleapis/python-dialogflow-cx/commit/595617990ccdc0575f97ae547984e89f638cb664))
* **v3:** release CompareVersions API ([8f3dc03](https://github.com/googleapis/python-dialogflow-cx/commit/8f3dc03835b5bb5baa36224a274f24dda7aa3709))

## [1.7.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.6.0...v1.7.0) (2021-11-12)


### Features

* allow setting custom CA for generic webhooks ([#207](https://www.github.com/googleapis/python-dialogflow-cx/issues/207)) ([441d66b](https://www.github.com/googleapis/python-dialogflow-cx/commit/441d66b3864c34cf37570b6c58ccf097eb20e919))


### Documentation

* **samples:** added comment to webhook sample ([#211](https://www.github.com/googleapis/python-dialogflow-cx/issues/211)) ([4d36e31](https://www.github.com/googleapis/python-dialogflow-cx/commit/4d36e31f20e38755dd5d4a7a92bb8c48722cb11e))

## [1.6.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.5.0...v1.6.0) (2021-11-05)


### Features

* add support for python 3.10 ([#192](https://www.github.com/googleapis/python-dialogflow-cx/issues/192)) ([527b679](https://www.github.com/googleapis/python-dialogflow-cx/commit/527b679286ce7ed6481bf5c9258858473ca1f601))
* **v3:** added API for changelogs ([#197](https://www.github.com/googleapis/python-dialogflow-cx/issues/197)) ([4f41653](https://www.github.com/googleapis/python-dialogflow-cx/commit/4f41653b08a5be4aa6c871f285d941a2f43740a9))
* **v3beta1:** added API for changelogs ([#198](https://www.github.com/googleapis/python-dialogflow-cx/issues/198)) ([484e13a](https://www.github.com/googleapis/python-dialogflow-cx/commit/484e13a78830a3d0ce8b1745fdf2dfce0f88a21e))
* **v3beta1:** added support for comparing between versions ([#202](https://www.github.com/googleapis/python-dialogflow-cx/issues/202)) ([b8e16f8](https://www.github.com/googleapis/python-dialogflow-cx/commit/b8e16f8a17a49c1fc65f7f4392e33fb273bcd8ca))


### Bug Fixes

* **deps:** drop packaging dependency ([c44582e](https://www.github.com/googleapis/python-dialogflow-cx/commit/c44582e2fe3d49327bb0fc5ba05d2959b6965b7b))
* **deps:** require google-api-core >= 1.28.0 ([c44582e](https://www.github.com/googleapis/python-dialogflow-cx/commit/c44582e2fe3d49327bb0fc5ba05d2959b6965b7b))


### Documentation

* list oneofs in docstring ([c44582e](https://www.github.com/googleapis/python-dialogflow-cx/commit/c44582e2fe3d49327bb0fc5ba05d2959b6965b7b))
* **samples:** add voice selection ([#184](https://www.github.com/googleapis/python-dialogflow-cx/issues/184)) ([778b86f](https://www.github.com/googleapis/python-dialogflow-cx/commit/778b86f69e88ceb884bb9933128d2b14c6689174))
* **samples:** added webhook sample ([#169](https://www.github.com/googleapis/python-dialogflow-cx/issues/169)) ([74cfc9a](https://www.github.com/googleapis/python-dialogflow-cx/commit/74cfc9a7ab9b85fa05565c406534a3cd3391ab4f))
* **samples:** adds list training phrases sample ([#196](https://www.github.com/googleapis/python-dialogflow-cx/issues/196)) ([dfefa4e](https://www.github.com/googleapis/python-dialogflow-cx/commit/dfefa4e21bcd6bf37d341911187fab283152f514))
* **v3beta1:** clarified security settings API reference ([b8e16f8](https://www.github.com/googleapis/python-dialogflow-cx/commit/b8e16f8a17a49c1fc65f7f4392e33fb273bcd8ca))
* **v3:** clarified semantic of the streaming APIs ([4f41653](https://www.github.com/googleapis/python-dialogflow-cx/commit/4f41653b08a5be4aa6c871f285d941a2f43740a9))

## [1.5.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.4.0...v1.5.0) (2021-10-11)


### Features

* add context manager support in client ([#187](https://www.github.com/googleapis/python-dialogflow-cx/issues/187)) ([70d4776](https://www.github.com/googleapis/python-dialogflow-cx/commit/70d4776d80f1f60b3f45e08e8dc64a47e2fae3e6))

## [1.4.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.3.2...v1.4.0) (2021-10-05)


### Features

* expose dtmf input info in the query result ([#181](https://www.github.com/googleapis/python-dialogflow-cx/issues/181)) ([e44d0ce](https://www.github.com/googleapis/python-dialogflow-cx/commit/e44d0cee6b51842e45255773c33ae0bbfc672f30))
* exposed DTMF input info in the query result ([1383bf8](https://www.github.com/googleapis/python-dialogflow-cx/commit/1383bf82b8b2ae0cd92d81768a693a2732a53a46))
* **v3:** added deployment API ([#182](https://www.github.com/googleapis/python-dialogflow-cx/issues/182)) ([1383bf8](https://www.github.com/googleapis/python-dialogflow-cx/commit/1383bf82b8b2ae0cd92d81768a693a2732a53a46))
* **v3beta1:** added support for DeployFlow api under Environments ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))
* **v3beta1:** added support for Deployments with ListDeployments and GetDeployment apis  ([#177](https://www.github.com/googleapis/python-dialogflow-cx/issues/177)) ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))
* **v3beta1:** added support for TestCasesConfig under Environment ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))


### Bug Fixes

* improper types in pagers generation ([615718b](https://www.github.com/googleapis/python-dialogflow-cx/commit/615718bf80e5c2f3060ff38675a7f4fe8deb59b1))
* **v3beta1:** marked resource name of security setting as not-required ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))


### Documentation

* added notes on long running operation ([1383bf8](https://www.github.com/googleapis/python-dialogflow-cx/commit/1383bf82b8b2ae0cd92d81768a693a2732a53a46))
* **v3beta1:** added long running operation explanation for several apis ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))

## [1.3.2](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.3.1...v1.3.2) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([96021b9](https://www.github.com/googleapis/python-dialogflow-cx/commit/96021b9a78a40f3f8f9898d53493912a1621da89))


### Documentation

* **samples:** added filter sample ([#171](https://www.github.com/googleapis/python-dialogflow-cx/issues/171)) ([5b7e6b9](https://www.github.com/googleapis/python-dialogflow-cx/commit/5b7e6b9fcb066e823d58c5ce3af0f32a54d896bc))
* **samples:** added page management samples ([#152](https://www.github.com/googleapis/python-dialogflow-cx/issues/152)) ([41d15f8](https://www.github.com/googleapis/python-dialogflow-cx/commit/41d15f8f212baab09222c6a350efc3376a3bf9ea))

## [1.3.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.3.0...v1.3.1) (2021-08-31)


### Documentation

* **v3beta1:** clarified LRO types ([#161](https://www.github.com/googleapis/python-dialogflow-cx/issues/161)) ([dd2b2fd](https://www.github.com/googleapis/python-dialogflow-cx/commit/dd2b2fd345e91fa3da1290f6896ac6b521c2eb7b))
* **v3beta1:** fixed incorrect update mask descriptions ([dd2b2fd](https://www.github.com/googleapis/python-dialogflow-cx/commit/dd2b2fd345e91fa3da1290f6896ac6b521c2eb7b))

## [1.3.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.2.0...v1.3.0) (2021-08-27)


### Features

* **v3:** added support for DLP templates ([#144](https://www.github.com/googleapis/python-dialogflow-cx/issues/144)) ([c74e3ac](https://www.github.com/googleapis/python-dialogflow-cx/commit/c74e3acb609363cdf941586e98ed2c8c5804980b))
* **v3beta1:** added support for DLP templates ([#143](https://www.github.com/googleapis/python-dialogflow-cx/issues/143)) ([7efb89c](https://www.github.com/googleapis/python-dialogflow-cx/commit/7efb89cc6311e1df9d03740ba6d078af3f79559e))
* **v3beta1:** expose `Locations` service to get/list avaliable locations of Dialogflow products ([7efb89c](https://www.github.com/googleapis/python-dialogflow-cx/commit/7efb89cc6311e1df9d03740ba6d078af3f79559e))
* **v3:** expose `Locations` service to get/list avaliable locations of Dialogflow products ([c74e3ac](https://www.github.com/googleapis/python-dialogflow-cx/commit/c74e3acb609363cdf941586e98ed2c8c5804980b))


### Documentation

* clarified LRO types  ([#156](https://www.github.com/googleapis/python-dialogflow-cx/issues/156)) ([a50e8dc](https://www.github.com/googleapis/python-dialogflow-cx/commit/a50e8dca8952cea19be2587ee68c600a41a92eeb))
* fixed incorrect update mask descriptions ([a50e8dc](https://www.github.com/googleapis/python-dialogflow-cx/commit/a50e8dca8952cea19be2587ee68c600a41a92eeb))
* **samples:** add agent creation code snippet ([#146](https://www.github.com/googleapis/python-dialogflow-cx/issues/146)) ([272fc98](https://www.github.com/googleapis/python-dialogflow-cx/commit/272fc9879e536f7a9ea31d8c10169cf644170769))
* **samples:** add region tags ([#150](https://www.github.com/googleapis/python-dialogflow-cx/issues/150)) ([54ea84d](https://www.github.com/googleapis/python-dialogflow-cx/commit/54ea84d58064a7c8d0a71f020a0c8cf36ac157bd))
* **samples:** add region tags ([#151](https://www.github.com/googleapis/python-dialogflow-cx/issues/151)) ([788b67a](https://www.github.com/googleapis/python-dialogflow-cx/commit/788b67a8c966788a70a5d683a5e79e3a289c7ba3))
* **samples:** add update intent sample ([#142](https://www.github.com/googleapis/python-dialogflow-cx/issues/142)) ([3e80235](https://www.github.com/googleapis/python-dialogflow-cx/commit/3e80235277a0df12644d743f6853ba45263a1239))
* **v3beta1:** reorder some fields ([7efb89c](https://www.github.com/googleapis/python-dialogflow-cx/commit/7efb89cc6311e1df9d03740ba6d078af3f79559e))

## [1.2.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.1.1...v1.2.0) (2021-08-02)


### Features

* **v3:** add advanced settings for agent level ([#137](https://www.github.com/googleapis/python-dialogflow-cx/issues/137)) ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3:** add insights export settings for security setting ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3:** add language code for streaming recognition result and flow versions for query parameters ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3:** add rollout config, state and failure reason for experiment ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3beta1:** add advanced settings for agent level ([#138](https://www.github.com/googleapis/python-dialogflow-cx/issues/138)) ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3beta1:** add insights export settings for security setting ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3beta1:** add language code for streaming recognition result and flow versions for query parameters ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3beta1:** add rollout config, state and failure reason for experiment ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))


### Documentation

* **v3beta1:** deprecate legacy logging settings ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3:** deprecate legacy logging settings ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))

## [1.1.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.1.0...v1.1.1) (2021-07-24)


### Bug Fixes

* enable self signed jwt for grpc ([#134](https://www.github.com/googleapis/python-dialogflow-cx/issues/134)) ([5e42bd0](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e42bd0786607ed0636e80be073007224bcb520e))

## [1.1.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.0.0...v1.1.0) (2021-07-22)


### Features

* add Samples section to CONTRIBUTING.rst ([#129](https://www.github.com/googleapis/python-dialogflow-cx/issues/129)) ([19238ad](https://www.github.com/googleapis/python-dialogflow-cx/commit/19238ad534b7528e3481e50a44663b541da197ef))


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#128](https://www.github.com/googleapis/python-dialogflow-cx/issues/128)) ([fbe63e8](https://www.github.com/googleapis/python-dialogflow-cx/commit/fbe63e86df05150e009e8e7b7e103735b382556e))

## [1.0.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.8.0...v1.0.0) (2021-06-30)


### Features

* bump release level to production/stable ([#88](https://www.github.com/googleapis/python-dialogflow-cx/issues/88)) ([47739f9](https://www.github.com/googleapis/python-dialogflow-cx/commit/47739f927032ca8701297260f0374f11b2c756b9))

## [0.8.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.7.1...v0.8.0) (2021-06-30)


### Features

* add always_use_jwt_access ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))
* add return_partial response to Fulfillment ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))
* mark agent.default_language_code as required ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))


### Bug Fixes

* disable always_use_jwt_access ([#119](https://www.github.com/googleapis/python-dialogflow-cx/issues/119)) ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))


### Documentation

* add notes to train agent before sending queries ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))
* added notes to train agent before sending queries ([#111](https://www.github.com/googleapis/python-dialogflow-cx/issues/111)) ([8a53800](https://www.github.com/googleapis/python-dialogflow-cx/commit/8a5380055dfa7d58f83be5ce0da310318b54fc51))
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-dialogflow-cx/issues/1127)) ([#110](https://www.github.com/googleapis/python-dialogflow-cx/issues/110)) ([40974f5](https://www.github.com/googleapis/python-dialogflow-cx/commit/40974f56c27833ab23575426f75d0868e1a10d94)), closes [#1126](https://www.github.com/googleapis/python-dialogflow-cx/issues/1126)

## [0.7.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.7.0...v0.7.1) (2021-06-16)


### Bug Fixes

* **deps:** add packaging requirement ([#105](https://www.github.com/googleapis/python-dialogflow-cx/issues/105)) ([5d47692](https://www.github.com/googleapis/python-dialogflow-cx/commit/5d476920c8c6825050a828896231542f6bfde2e2))

## [0.7.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.6.0...v0.7.0) (2021-06-16)


### Features

* **v3beta1:** Support partial response feature ([5e21ed4](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e21ed454ad6a5d687e634ad4e697f1921104c47))
* **v3beta1:** support sentiment analysis in bot testing ([#100](https://www.github.com/googleapis/python-dialogflow-cx/issues/100)) ([f24f302](https://www.github.com/googleapis/python-dialogflow-cx/commit/f24f3028fa83da14614d1340e5bce7719be287b6))


### Bug Fixes

* exclude docs and tests from package ([#104](https://www.github.com/googleapis/python-dialogflow-cx/issues/104)) ([2ddb70b](https://www.github.com/googleapis/python-dialogflow-cx/commit/2ddb70b5825ad0d59165d7dfbfe36677d586cccf))
* **v3beta1:** Set agent default language code as required ([#103](https://www.github.com/googleapis/python-dialogflow-cx/issues/103)) ([5e21ed4](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e21ed454ad6a5d687e634ad4e697f1921104c47))


### Documentation

* **v3beta1:** Update docs of Agents, Fulfillments, SecuritySettings and Sessions ([5e21ed4](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e21ed454ad6a5d687e634ad4e697f1921104c47))

## [0.6.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.5.0...v0.6.0) (2021-06-07)


### Features

* support sentiment analysis in bot testing ([#98](https://www.github.com/googleapis/python-dialogflow-cx/issues/98)) ([db258bc](https://www.github.com/googleapis/python-dialogflow-cx/commit/db258bcc9971542e347b50f396bd51ec88520fde))

## [0.5.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.4.1...v0.5.0) (2021-05-28)


### Features

* add export / import flow API ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* add support for service directory webhooks ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* added API for continuous test ([#91](https://www.github.com/googleapis/python-dialogflow-cx/issues/91)) ([81d4f53](https://www.github.com/googleapis/python-dialogflow-cx/commit/81d4f53cd4a4080b21221126dacaf2e13ca2efcf))
* added API for running continuous test ([#94](https://www.github.com/googleapis/python-dialogflow-cx/issues/94)) ([cc30fa3](https://www.github.com/googleapis/python-dialogflow-cx/commit/cc30fa3e767bac2f33637ce1c29766ff41e9225b))
* added fallback option when restoring an agent ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* Expose supported languages of the agent; ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* include original user query in WebhookRequest; add GetTextCaseresult API. ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* support self-signed JWT flow for service accounts ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))


### Bug Fixes

* add async client to %name_%version/init.py ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* require google-api-core>=1.22.2 ([3440f18](https://www.github.com/googleapis/python-dialogflow-cx/commit/3440f186cd879fd4ddc9b3442bf857a4f286698e))
* **v3:** BREAKING rename `UserInput.input_` to `UserInput.input` ([#58](https://www.github.com/googleapis/python-dialogflow-cx/issues/58)) ([3440f18](https://www.github.com/googleapis/python-dialogflow-cx/commit/3440f186cd879fd4ddc9b3442bf857a4f286698e))


### Documentation

* clarified documentation for security settings docs: clarified documentation for session parameters ([#89](https://www.github.com/googleapis/python-dialogflow-cx/issues/89)) ([750a055](https://www.github.com/googleapis/python-dialogflow-cx/commit/750a055b688ebeda8e8882cdb02bdc87524a69a5))
* clarified documentation for security settings docs: clarified documentation for session parameters ([#90](https://www.github.com/googleapis/python-dialogflow-cx/issues/90)) ([c1c0fb9](https://www.github.com/googleapis/python-dialogflow-cx/commit/c1c0fb9eb9e62dc794aef1bac357bb5c20e322dc))
* clarified experiment length ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* clarify resource format for session response. ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* Update docs on Pages, Session, Version, etc. ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))

## [0.4.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.4.0...v0.4.1) (2021-03-07)


### Documentation

* fix readme ([#52](https://www.github.com/googleapis/python-dialogflow-cx/issues/52)) ([8728ad4](https://www.github.com/googleapis/python-dialogflow-cx/commit/8728ad4018bf9c976cdc469af3d8a7ec89c04671))

## [0.4.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.3.0...v0.4.0) (2021-03-05)


### Features

* add from_service_account_info factory ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* Add new Experiment service ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* added support for test cases and agent validation ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* allow to disable webhook invocation per request ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* supports SentimentAnalysisResult in webhook request ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))


### Documentation

* test cases doc update ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* update languages link ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))

## [0.3.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.2.0...v0.3.0) (2021-01-29)


### Features

* add experiments API ([#36](https://www.github.com/googleapis/python-dialogflow-cx/issues/36)) ([5381512](https://www.github.com/googleapis/python-dialogflow-cx/commit/5381512872ca2492ddabcbdd7ccde5f054aed011))
* allowed custom to specify webhook headers through query parameters ([#32](https://www.github.com/googleapis/python-dialogflow-cx/issues/32)) ([09919b0](https://www.github.com/googleapis/python-dialogflow-cx/commit/09919b0e45517cedcbb1d8b5b931c7317be549b2))
* allowed custom to specify webhook headers through query parameters ([#32](https://www.github.com/googleapis/python-dialogflow-cx/issues/32)) ([09919b0](https://www.github.com/googleapis/python-dialogflow-cx/commit/09919b0e45517cedcbb1d8b5b931c7317be549b2))


### Bug Fixes

* remove gRPC send/recv limit; add enums to `types/__init__.py` ([09919b0](https://www.github.com/googleapis/python-dialogflow-cx/commit/09919b0e45517cedcbb1d8b5b931c7317be549b2))

## [0.2.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.1.1...v0.2.0) (2020-12-07)


### Features

* add v3 ([#21](https://www.github.com/googleapis/python-dialogflow-cx/issues/21)) ([97c7fb5](https://www.github.com/googleapis/python-dialogflow-cx/commit/97c7fb53e5f6af7d8b0fea3043c60da9ee1f549b))

## [0.1.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.1.0...v0.1.1) (2020-11-17)


### Bug Fixes

* corrects the repo/homepage link ([#15](https://www.github.com/googleapis/python-dialogflow-cx/issues/15)) ([c26852d](https://www.github.com/googleapis/python-dialogflow-cx/commit/c26852d8a3738eb4d67222c555d0197a854e68a9))


### Documentation

* **samples:** add initial sample codes ([#13](https://www.github.com/googleapis/python-dialogflow-cx/issues/13)) ([b590308](https://www.github.com/googleapis/python-dialogflow-cx/commit/b590308b79a230561aed776f55260a73668c8efc)), closes [#12](https://www.github.com/googleapis/python-dialogflow-cx/issues/12)

## 0.1.0 (2020-08-24)


### Features

* generate v3beta1 ([0c6e3a9](https://www.github.com/googleapis/python-dialogflow-cx/commit/0c6e3a9ff1a38f6d6c5f8c2983cbfa1f7ff7536d))
