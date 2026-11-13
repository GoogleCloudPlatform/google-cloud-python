# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-dataflow-client/#history

## [0.14.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.14.0...google-cloud-dataflow-client-v0.14.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.13.0...google-cloud-dataflow-client-v0.14.0) (2026-06-02)


### Features

* regenerate google-cloud-d packages (#17092) ([d49a2b9412b4ee9105125db36104a3e18344e0ad](https://github.com/googleapis/google-cloud-python/commit/d49a2b9412b4ee9105125db36104a3e18344e0ad))

## [0.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.12.0...google-cloud-dataflow-client-v0.13.0) (2026-04-02)


### Features

* add sha256 field to Package proto ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))
* Add Pausing/Yaml capabilities to public protos ([c36aa6169035fdb14bf84b0e56e4f81291600b5a](https://github.com/googleapis/google-cloud-python/commit/c36aa6169035fdb14bf84b0e56e4f81291600b5a))

## [0.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.11.0...google-cloud-dataflow-client-v0.12.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.10.0...google-cloud-dataflow-client-v0.11.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.9.0...google-cloud-dataflow-client-v0.10.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.17...google-cloud-dataflow-client-v0.9.0) (2025-05-08)


### ⚠ BREAKING CHANGES

* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `JobsV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `MessagesV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `MessagesV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `MetricsV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `MetricsV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `SnapshotsV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `SnapshotsV1Beta3`
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `TemplatesService`
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `TemplatesService`
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `FlexTemplatesService`
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `FlexTemplatesService`
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `JobsV1Beta3`

### Features

* A new enum `StreamingMode` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `bugs` is added to message `.google.dataflow.v1beta3.SdkVersion` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `data_sampling` is added to message `.google.dataflow.v1beta3.DebugOptions` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `default_streaming_mode` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `default_value` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `disk_size_gb` is added to message `.google.dataflow.v1beta3.RuntimeEnvironment` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `dynamic_destinations` is added to message `.google.dataflow.v1beta3.PubsubLocation` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `enable_launcher_vm_serial_port_logging` is added to message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `enum_options` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `group_name` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `hidden_ui` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `image_repository_cert_path` is added to message `.google.dataflow.v1beta3.ContainerSpec` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `image_repository_password_secret_id` is added to message `.google.dataflow.v1beta3.ContainerSpec` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `image_repository_username_secret_id` is added to message `.google.dataflow.v1beta3.ContainerSpec` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `name` is added to message `.google.dataflow.v1beta3.ListJobsRequest` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `parent_name` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `parent_trigger_values` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `runtime_updatable_params` is added to message `.google.dataflow.v1beta3.Job` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `satisfies_pzi` is added to message `.google.dataflow.v1beta3.Job` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `service_resources` is added to message `.google.dataflow.v1beta3.Job` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `step_names_hash` is added to message `.google.dataflow.v1beta3.PipelineDescription` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `straggler_info` is added to message `.google.dataflow.v1beta3.WorkItemDetails` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `straggler_summary` is added to message `.google.dataflow.v1beta3.StageSummary` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `streaming_mode` is added to message `.google.dataflow.v1beta3.Environment` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `streaming_mode` is added to message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `streaming_mode` is added to message `.google.dataflow.v1beta3.RuntimeEnvironment` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `streaming` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `supports_at_least_once` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `supports_exactly_once` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `trie` is added to message `.google.dataflow.v1beta3.MetricUpdate` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `update_mask` is added to message `.google.dataflow.v1beta3.UpdateJobRequest` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `use_streaming_engine_resource_based_billing` is added to message `.google.dataflow.v1beta3.Environment` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new field `user_display_properties` is added to message `.google.dataflow.v1beta3.JobMetadata` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `DataSamplingConfig` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `HotKeyDebuggingInfo` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `ParameterMetadataEnumOption` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `RuntimeUpdatableParams` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `SdkBug` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `ServiceResources` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `Straggler` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `StragglerInfo` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `StragglerSummary` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new message `StreamingStragglerInfo` is added ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new method_signature `job,update_mask` is added to method `UpdateJob` in service `JobsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `BIGQUERY_TABLE` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `BOOLEAN` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `ENUM` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `GO` is added to enum `Language` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `JAVASCRIPT_UDF_FILE` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `KAFKA_READ_TOPIC` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `KAFKA_TOPIC` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `KAFKA_WRITE_TOPIC` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `KMS_KEY_NAME` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `MACHINE_TYPE` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `NUMBER` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `SERVICE_ACCOUNT` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `WORKER_REGION` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A new value `WORKER_ZONE` is added to enum `ParameterType` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))


### Bug Fixes

* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `FlexTemplatesService` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `JobsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `MessagesV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `MetricsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `SnapshotsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/compute.readonly` is removed from service `TemplatesService` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `FlexTemplatesService` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `JobsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `MessagesV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `MetricsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `SnapshotsV1Beta3` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* An existing oauth_scope `https://www.googleapis.com/auth/userinfo.email` is removed from service `TemplatesService` ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))


### Documentation

* A comment for enum `JobState` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for enum `WorkerIPAddressConfiguration` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for enum value `JOB_VIEW_ALL` in enum `JobView` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `additional_experiments` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `additional_user_labels` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `bypass_temp_dir_validation` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `capabilities` in message `.google.dataflow.v1beta3.SdkHarnessContainerImage` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `current_state` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `dataset` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `debug_options` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `dump_heap_on_oom` in message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `dynamic_template` in message `.google.dataflow.v1beta3.LaunchTemplateRequest` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `enable_hot_key_logging` in message `.google.dataflow.v1beta3.DebugOptions` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `enable_streaming_engine` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `environment` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `flex_resource_scheduling_goal` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `gcs_path` in message `.google.dataflow.v1beta3.DynamicTemplateLaunchParams` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `gcs_path` in message `.google.dataflow.v1beta3.LaunchTemplateRequest` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `id` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `ip_configuration` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `job_name` in message `.google.dataflow.v1beta3.LaunchTemplateParameters` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `kms_key_name` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `launch_parameters` in message `.google.dataflow.v1beta3.LaunchTemplateRequest` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `location` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `machine_type` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `max_workers` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `name` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `network` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `num_workers` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `project_id` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `requested_state` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `save_heap_dumps_to_gcs_path` in message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `service_account_email` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `service_account_email` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `service_kms_key_name` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `service_options` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `set` in message `.google.dataflow.v1beta3.MetricUpdate` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `subnetwork` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `temp_location` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `transform_name_mapping` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `type` in message `.google.dataflow.v1beta3.Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `worker_region` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `worker_region` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `worker_zone` in message `.google.dataflow.v1beta3.Environment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `worker_zone` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for field `zone` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `DynamicTemplateLaunchParams` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `Job` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `JobExecutionStageInfo` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `JobMetrics` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `LaunchTemplateParameters` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `MetricUpdate` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `SdkHarnessContainerImage` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for message `Step` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for method `AggregatedListJobs` in service `JobsV1Beta3` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for method `CreateJob` in service `JobsV1Beta3` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for method `CreateJobFromTemplate` in service `TemplatesService` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for method `GetTemplate` in service `TemplatesService` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for method `LaunchTemplate` in service `TemplatesService` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for method `ListJobs` in service `JobsV1Beta3` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))
* A comment for service `FlexTemplatesService` is changed ([487aa54](https://github.com/googleapis/google-cloud-python/commit/487aa54eccc57ac15b736b0b31a2088dc43ecab7))

## [0.8.17](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.16...google-cloud-dataflow-client-v0.8.17) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([feb5353](https://github.com/googleapis/google-cloud-python/commit/feb53532240bb70a94b359b519f0f41f95875a33))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.8.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.15...google-cloud-dataflow-client-v0.8.16) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))
* Add support for reading selective GAPIC generation methods from service YAML ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))

## [0.8.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.14...google-cloud-dataflow-client-v0.8.15) (2024-12-12)


### Features

* Add support for opt-in debug logging ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))

## [0.8.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.13...google-cloud-dataflow-client-v0.8.14) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))

## [0.8.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.12...google-cloud-dataflow-client-v0.8.13) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [0.8.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.11...google-cloud-dataflow-client-v0.8.12) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([ba1064f](https://github.com/googleapis/google-cloud-python/commit/ba1064fd6a63ccbe8a390c0026f32c5772c728a5))

## [0.8.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.10...google-cloud-dataflow-client-v0.8.11) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12865](https://github.com/googleapis/google-cloud-python/issues/12865)) ([7f9dedb](https://github.com/googleapis/google-cloud-python/commit/7f9dedb3abc7636cbcd97e21ac857844b885b599))

## [0.8.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.9...google-cloud-dataflow-client-v0.8.10) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12383](https://github.com/googleapis/google-cloud-python/issues/12383)) ([305f43f](https://github.com/googleapis/google-cloud-python/commit/305f43f7d6293e3316248f421fdc19c5d8405c21))

## [0.8.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.8...google-cloud-dataflow-client-v0.8.9) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12305](https://github.com/googleapis/google-cloud-python/issues/12305)) ([2aa7f17](https://github.com/googleapis/google-cloud-python/commit/2aa7f17a5fd4f2249260225db91fb0414d06eaa7))
* fix ValueError in test__validate_universe_domain ([dd749df](https://github.com/googleapis/google-cloud-python/commit/dd749dfb4caf2e33f1152dfd8c4b0ac5424c381c))

## [0.8.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.7...google-cloud-dataflow-client-v0.8.8) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))

## [0.8.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.6...google-cloud-dataflow-client-v0.8.7) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12239](https://github.com/googleapis/google-cloud-python/issues/12239)) ([8004d15](https://github.com/googleapis/google-cloud-python/commit/8004d15d9e6baa4dc5bc3f09d528e176d54d9ec5))

## [0.8.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataflow-client-v0.8.5...google-cloud-dataflow-client-v0.8.6) (2023-12-07)


### Features

* Add support for python 3.12 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Introduce compatibility with native namespace packages ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Use `retry_async` instead of `retry` in async client ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))

## [0.8.5](https://github.com/googleapis/python-dataflow-client/compare/v0.8.4...v0.8.5) (2023-10-09)


### Documentation

* Minor formatting ([94b4f73](https://github.com/googleapis/python-dataflow-client/commit/94b4f73d2f698a49fd38d227df5f211509ffcc5c))

## [0.8.4](https://github.com/googleapis/python-dataflow-client/compare/v0.8.3...v0.8.4) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#184](https://github.com/googleapis/python-dataflow-client/issues/184)) ([355b8b4](https://github.com/googleapis/python-dataflow-client/commit/355b8b4c08fbb35d0c7f8402d8814096523663b2))

## [0.8.3](https://github.com/googleapis/python-dataflow-client/compare/v0.8.2...v0.8.3) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#177](https://github.com/googleapis/python-dataflow-client/issues/177)) ([22668f6](https://github.com/googleapis/python-dataflow-client/commit/22668f60347b04862a52fc5080e54ec7f3712113))

## [0.8.2](https://github.com/googleapis/python-dataflow-client/compare/v0.8.1...v0.8.2) (2023-02-07)


### Bug Fixes

* Raise not implemented error when REST transport is not supported ([#170](https://github.com/googleapis/python-dataflow-client/issues/170)) ([44651ca](https://github.com/googleapis/python-dataflow-client/commit/44651cae3c23a05c61c8bafbb0a55b141d3368a5))

## [0.8.1](https://github.com/googleapis/python-dataflow-client/compare/v0.8.0...v0.8.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([63d369a](https://github.com/googleapis/python-dataflow-client/commit/63d369a60feb3036d50300bc15f762fc7d622caf))


### Documentation

* Add documentation for enums ([63d369a](https://github.com/googleapis/python-dataflow-client/commit/63d369a60feb3036d50300bc15f762fc7d622caf))

## [0.8.0](https://github.com/googleapis/python-dataflow-client/compare/v0.7.0...v0.8.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#164](https://github.com/googleapis/python-dataflow-client/issues/164)) ([97fa32f](https://github.com/googleapis/python-dataflow-client/commit/97fa32f8bad593e93fd86d2f883be0b6d55be9ba))

## [0.7.0](https://github.com/googleapis/python-dataflow-client/compare/v0.6.2...v0.7.0) (2022-12-15)


### Features

* Add support for `google.cloud.dataflow.__version__` ([5f36251](https://github.com/googleapis/python-dataflow-client/commit/5f362512a1c36b1c5ce27fa175afb57fc5b375bc))
* Add typing to proto.Message based class attributes ([5f36251](https://github.com/googleapis/python-dataflow-client/commit/5f362512a1c36b1c5ce27fa175afb57fc5b375bc))


### Bug Fixes

* Add dict typing for client_options ([5f36251](https://github.com/googleapis/python-dataflow-client/commit/5f362512a1c36b1c5ce27fa175afb57fc5b375bc))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([9b9083c](https://github.com/googleapis/python-dataflow-client/commit/9b9083c177dd2b19cf218a4c0574159b9c162135))
* Drop usage of pkg_resources ([9b9083c](https://github.com/googleapis/python-dataflow-client/commit/9b9083c177dd2b19cf218a4c0574159b9c162135))
* Fix timeout default values ([9b9083c](https://github.com/googleapis/python-dataflow-client/commit/9b9083c177dd2b19cf218a4c0574159b9c162135))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([5f36251](https://github.com/googleapis/python-dataflow-client/commit/5f362512a1c36b1c5ce27fa175afb57fc5b375bc))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([9b9083c](https://github.com/googleapis/python-dataflow-client/commit/9b9083c177dd2b19cf218a4c0574159b9c162135))

## [0.6.2](https://github.com/googleapis/python-dataflow-client/compare/v0.6.1...v0.6.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#150](https://github.com/googleapis/python-dataflow-client/issues/150)) ([216c6e2](https://github.com/googleapis/python-dataflow-client/commit/216c6e2b74db6b61d85e67df39c490cb99d71835))
* **deps:** require google-api-core&gt;=1.33.2 ([216c6e2](https://github.com/googleapis/python-dataflow-client/commit/216c6e2b74db6b61d85e67df39c490cb99d71835))

## [0.6.1](https://github.com/googleapis/python-dataflow-client/compare/v0.6.0...v0.6.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#146](https://github.com/googleapis/python-dataflow-client/issues/146)) ([52466db](https://github.com/googleapis/python-dataflow-client/commit/52466db052d09d268c3a3da1036a9fcdb7a5d459))

## [0.6.0](https://github.com/googleapis/python-dataflow-client/compare/v0.5.5...v0.6.0) (2022-09-13)


### Features

* Enable REST transport support ([#139](https://github.com/googleapis/python-dataflow-client/issues/139)) ([e8a64ff](https://github.com/googleapis/python-dataflow-client/commit/e8a64ff142ae8f0ff48736b1611a11740e3fa9a3))

## [0.5.5](https://github.com/googleapis/python-dataflow-client/compare/v0.5.4...v0.5.5) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#126](https://github.com/googleapis/python-dataflow-client/issues/126)) ([16b89c0](https://github.com/googleapis/python-dataflow-client/commit/16b89c0ea5cc63999da9c5bd398b87caa842b04f))
* **deps:** require proto-plus >= 1.22.0 ([16b89c0](https://github.com/googleapis/python-dataflow-client/commit/16b89c0ea5cc63999da9c5bd398b87caa842b04f))

## [0.5.4](https://github.com/googleapis/python-dataflow-client/compare/v0.5.3...v0.5.4) (2022-07-14)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#120](https://github.com/googleapis/python-dataflow-client/issues/120)) ([f981454](https://github.com/googleapis/python-dataflow-client/commit/f981454d308aba209335a8c49d347c77e9604645))

## [0.5.3](https://github.com/googleapis/python-dataflow-client/compare/v0.5.2...v0.5.3) (2022-07-12)


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#115](https://github.com/googleapis/python-dataflow-client/issues/115)) ([75376d4](https://github.com/googleapis/python-dataflow-client/commit/75376d4f2b764d75a7a9c21b0f24d67983b2b5fb))
* require python 3.7+ ([#117](https://github.com/googleapis/python-dataflow-client/issues/117)) ([7123255](https://github.com/googleapis/python-dataflow-client/commit/7123255860a8a55377bc7235c8115e3c17b240b2))

## [0.5.2](https://github.com/googleapis/python-dataflow-client/compare/v0.5.1...v0.5.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#106](https://github.com/googleapis/python-dataflow-client/issues/106)) ([3170fe7](https://github.com/googleapis/python-dataflow-client/commit/3170fe7af4b3de2802251b2f24ca73d2060d560b))


### Documentation

* fix changelog header to consistent size ([#107](https://github.com/googleapis/python-dataflow-client/issues/107)) ([df80541](https://github.com/googleapis/python-dataflow-client/commit/df805416bd144da9d2c0e4c49a7d478580237b28))

## [0.5.1](https://github.com/googleapis/python-dataflow-client/compare/v0.5.0...v0.5.1) (2022-05-05)


### Documentation

* fix type in docstring for map fields ([e775e1f](https://github.com/googleapis/python-dataflow-client/commit/e775e1fce9eeed9c8614c61892c8b987facd5c66))

## [0.5.0](https://github.com/googleapis/python-dataflow-client/compare/v0.4.1...v0.5.0) (2022-03-16)


### Features

* Add capabilities field to SdkHarnessContainerImage ([#84](https://github.com/googleapis/python-dataflow-client/issues/84)) ([3d86713](https://github.com/googleapis/python-dataflow-client/commit/3d867138d9abc434f83556a0177a89b23e187555))

## [0.4.1](https://github.com/googleapis/python-dataflow-client/compare/v0.4.0...v0.4.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#81](https://github.com/googleapis/python-dataflow-client/issues/81)) ([9783339](https://github.com/googleapis/python-dataflow-client/commit/97833397e1a4e06cf7a7cae88c813f9ca071fa49))

## [0.4.0](https://github.com/googleapis/python-dataflow-client/compare/v0.3.1...v0.4.0) (2022-02-26)


### Features

* add api key support ([#65](https://github.com/googleapis/python-dataflow-client/issues/65)) ([888664b](https://github.com/googleapis/python-dataflow-client/commit/888664b70baefe7acb7e46c82a06c24e7ba06af2))
* new parameters in FlexTemplateRuntimeEnvironment ([#69](https://github.com/googleapis/python-dataflow-client/issues/69)) ([f8bd373](https://github.com/googleapis/python-dataflow-client/commit/f8bd3730da138532aa90f6bc90ff3a8c1075fa01))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([f8bd373](https://github.com/googleapis/python-dataflow-client/commit/f8bd3730da138532aa90f6bc90ff3a8c1075fa01))


### Documentation

* remove typo in docstring ([#72](https://github.com/googleapis/python-dataflow-client/issues/72)) ([db91cc2](https://github.com/googleapis/python-dataflow-client/commit/db91cc2c65cf43f766385c0f973dd58c4233c9c7))

## [0.3.1](https://www.github.com/googleapis/python-dataflow-client/compare/v0.3.0...v0.3.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([89dbf65](https://www.github.com/googleapis/python-dataflow-client/commit/89dbf6545f8eb317108c0c028f461f13e40c20cc))
* **deps:** require google-api-core >= 1.28.0 ([89dbf65](https://www.github.com/googleapis/python-dataflow-client/commit/89dbf6545f8eb317108c0c028f461f13e40c20cc))


### Documentation

* list oneofs in docstring ([89dbf65](https://www.github.com/googleapis/python-dataflow-client/commit/89dbf6545f8eb317108c0c028f461f13e40c20cc))

## [0.3.0](https://www.github.com/googleapis/python-dataflow-client/compare/v0.2.0...v0.3.0) (2021-10-15)


### Features

* add support for python 3.10 ([#44](https://www.github.com/googleapis/python-dataflow-client/issues/44)) ([ff87f99](https://www.github.com/googleapis/python-dataflow-client/commit/ff87f997be1a9f86fe1619107e12fb02aaccd8a7))

## [0.2.0](https://www.github.com/googleapis/python-dataflow-client/compare/v0.1.5...v0.2.0) (2021-10-08)


### Features

* add context manager support in client ([#41](https://www.github.com/googleapis/python-dataflow-client/issues/41)) ([2d8fbd5](https://www.github.com/googleapis/python-dataflow-client/commit/2d8fbd5ff487a5e0aeea8cbf6a4d523861bb197a))

## [0.1.5](https://www.github.com/googleapis/python-dataflow-client/compare/v0.1.4...v0.1.5) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([ce0077b](https://www.github.com/googleapis/python-dataflow-client/commit/ce0077b8b99566a6c97dbbd355eb9a0ea75f5ed3))

## [0.1.4](https://www.github.com/googleapis/python-dataflow-client/compare/v0.1.3...v0.1.4) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([db5d966](https://www.github.com/googleapis/python-dataflow-client/commit/db5d966111077c2ba286136b9b5aba6a371c8e0d))

## [0.1.3](https://www.github.com/googleapis/python-dataflow-client/compare/v0.1.2...v0.1.3) (2021-08-18)


### Features

* add Samples section to CONTRIBUTING.rst ([#14](https://www.github.com/googleapis/python-dataflow-client/issues/14)) ([998adbe](https://www.github.com/googleapis/python-dataflow-client/commit/998adbe0a2684d658303a860805027b83a75b520))


### Bug Fixes

* enable self signed jwt for grpc ([#18](https://www.github.com/googleapis/python-dataflow-client/issues/18)) ([0a69423](https://www.github.com/googleapis/python-dataflow-client/commit/0a69423ccf2229f7fe00c2c778aec8992bfbb24d))


### Miscellaneous Chores

* release as 0.1.3 ([#19](https://www.github.com/googleapis/python-dataflow-client/issues/19)) ([5fa4e3f](https://www.github.com/googleapis/python-dataflow-client/commit/5fa4e3fe0a17f71c719fe5dc093809bb73600b2d))

## [0.1.2](https://www.github.com/googleapis/python-dataflow-client/compare/v0.1.1...v0.1.2) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#13](https://www.github.com/googleapis/python-dataflow-client/issues/13)) ([a85e8aa](https://www.github.com/googleapis/python-dataflow-client/commit/a85e8aac12a35a6bf82c2414d8c4018b64d36cc4))

## [0.1.1](https://www.github.com/googleapis/python-dataflow-client/compare/v0.1.0...v0.1.1) (2021-06-30)


### Miscellaneous Chores

* release 0.1.1 ([#9](https://www.github.com/googleapis/python-dataflow-client/issues/9)) ([db3ece7](https://www.github.com/googleapis/python-dataflow-client/commit/db3ece7761283ada3ddbc8e15b7ca04972b22f0b))

## 0.1.0 (2021-06-25)


### Features

* generate v1beta3 ([ce2226e](https://www.github.com/googleapis/python-dataflow/commit/ce2226ea43a77009a710093caef4075650377989))
