# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-container/#history

## [2.67.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.66.0...google-cloud-container-v2.67.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [2.66.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.65.0...google-cloud-container-v2.66.0) (2026-09-03)


### Features

* update googleapis and regenerate ([#18229](https://github.com/googleapis/google-cloud-python/issues/18229)) ([d4f8a57](https://github.com/googleapis/google-cloud-python/commit/d4f8a57abadd282ad95472e77daa59d8fb98cbcf))

## [2.65.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.64.0...google-cloud-container-v2.65.0) (2026-06-02)


### Features

* regenerate google-cloud-c packages (#17091) ([165839343695fc74d09fc7900d4c55ddcb31a4d8](https://github.com/googleapis/google-cloud-python/commit/165839343695fc74d09fc7900d4c55ddcb31a4d8))

## [2.64.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.63.0...google-cloud-container-v2.64.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [2.63.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.62.0...google-cloud-container-v2.63.0) (2026-01-29)


### Documentation

* A comment for field `subnetwork` in message `.google.container.v1beta1.NodeNetworkConfig` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `cluster_ipv4_cidr` in message `.google.container.v1beta1.Cluster` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `cluster_ipv4_cidr_block` in message `.google.container.v1beta1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `node_ipv4_cidr_block` in message `.google.container.v1beta1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `tpu_ipv4_cidr_block` in message `.google.container.v1beta1.Cluster` is change ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `tpu_ipv4_cidr_block` in message `.google.container.v1beta1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `services_ipv4_cidr_block` in message `.google.container.v1beta1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `services_ipv4_cidr` in message `.google.container.v1beta1.Cluster` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `sysctls` in message `.google.container.v1beta1.LinuxNodeConfig` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `enable_legacy_lustre_port` in message `.google.container.v1beta1.LustreCsiDriverConfig` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `cluster_ipv4_cidr` in message `.google.container.v1.Cluster` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `services_ipv4_cidr_block` in message `.google.container.v1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `cluster_ipv4_cidr_block` in message `.google.container.v1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `node_ipv4_cidr_block` in message `.google.container.v1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `tpu_ipv4_cidr_block` in message `.google.container.v1.IPAllocationPolicy` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `sysctls` in message `.google.container.v1.LinuxNodeConfig` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `gcp_secret_manager_certificate_config` in message `.google.container.v1.ContainerdConfig` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `subnetwork` in message `.google.container.v1.NodeNetworkConfig` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `services_ipv4_cidr` in message `.google.container.v1.Cluster` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `tpu_ipv4_cidr_block` in message `.google.container.v1.Cluster` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* A comment for field `recurrence` in message `.google.container.v1.RecurringTimeWindow` is changed ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))


### Features

* Add GPUDirectConfig to configure GPU Direct for node pools ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add consolidation_delay to configure Cluster Autoscaler node consolidation delay ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add SHORT_LIVED as a NodePoolUpdateStrategy ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add DRAINING status to AdditionalIPRangesConfig for subnet draining ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add DisruptionEvent to provide details on node disruption events ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add shutdown_grace_period_seconds and shutdown_grace_period_critical_pods_seconds to NodeKubeletConfig to configure graceful node shutdown for Spot VMs ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add RegistryHostConfig to ContainerdConfig for containerd registry host configuration ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add NodeDrainConfig to NodePool to configure node draining behavior ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add AutopilotGeneralProfile to ClusterAutoscaling to configure Autopilot profiles ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add ManagedOpenTelemetryConfig to Cluster to manage the OpenTelemetry pipeline ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add fields for Rollback-Safe upgrades, including RollbackSafeUpgrade, CompatibilityStatus, and CompleteControlPlaneUpgrade RPC ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add SliceControllerConfig to AddonsConfig to manage the Slice Controller addon ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Allow specifying subnetwork in NodeNetworkConfig during node pool creation ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add PodSnapshotConfig to AddonsConfig to manage Pod Snapshots ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))
* Add SwapConfig to enable and configure swap memory for node pools ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))

## [2.62.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.61.0...google-cloud-container-v2.62.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [2.61.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.60.0...google-cloud-container-v2.61.0) (2025-10-23)


### Documentation

* various documentation fixes  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* various documentation fixes  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))


### Features

* add network_tier_config field to NodeNetworkConfig  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add membership_type field to Fleet  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* deprecate enterprise_config field in Cluster  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add end_time_behavior field to MaintenanceExclusionOptions  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add rotation_config field to SecretManagerConfig  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add node_kernel_module_loading field to LinuxNodeConfig  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* deprecate enable_legacy_lustre_port field in LustreCsiDriverConfig  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add autoscaled_rollout_policy field to BlueGreenSettings  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add writable_cgroups field to ContainerdConfig  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add privileged_admission_config field to Autopilot  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add network_tier_config field to IPAllocationPolicy  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* deprecate desired_enterprise_config field in ClusterUpdate  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))
* add desired_secret_sync_config to ClusterUpdate  ([9170f84f016ab7563d9610b3c20a429ce03811c8](https://github.com/googleapis/google-cloud-python/commit/9170f84f016ab7563d9610b3c20a429ce03811c8))

## [2.60.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.59.0...google-cloud-container-v2.60.0) (2025-10-16)


### Documentation

* updated comments for various types, messages, and fields.  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))


### Features

* Add &#39;enabled&#39; field to AutoIpamConfig to enable/disable Auto IPAM  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add fields to DNSEndpointConfig to control k8s token and cert authentication via DNS  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add SecretSyncConfig to sync secrets from Secret Manager  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add SwapConfig to enable and configure swap memory for node pools  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add &#39;end_time_behavior&#39; to MaintenanceExclusionOptions  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add network_tier_config and accelerator_network_profile to NodePool  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add cluster-level network_tier_config  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add &#39;wait_for_drain_duration&#39; to AutoscaledRolloutPolicy in BlueGreenSettings  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add PrivilegedAdmissionConfig for Autopilot clusters  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add MembershipType to Fleet config  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add WritableCgroups to the containerd config  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add NodeKernelModuleLoading to configure kernel module loading policies for nodes  ([89cd6f54ea4b20b057c43225acc5d6a7cb5496c3](https://github.com/googleapis/google-cloud-python/commit/89cd6f54ea4b20b057c43225acc5d6a7cb5496c3))
* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [2.59.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.58.0...google-cloud-container-v2.59.0) (2025-07-23)


### Features

* A new enum `Mode` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new enum `TransparentHugepageDefrag` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new enum `TransparentHugepageEnabled` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `additional_ip_ranges_configs` is added to message `.google.container.v1beta1.IPAllocationPolicy` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `auto_ipam_config` is added to message `.google.container.v1beta1.IPAllocationPolicy` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `boot_disk` is added to message `.google.container.v1beta1.NodeConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `boot_disk` is added to message `.google.container.v1beta1.UpdateNodePoolRequest` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `default_compute_class_config` is added to message `.google.container.v1beta1.ClusterAutoscaling` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `desired_additional_ip_ranges_config` is added to message `.google.container.v1beta1.ClusterUpdate` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `desired_auto_ipam_config` is added to message `.google.container.v1beta1.ClusterUpdate` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `desired_user_managed_keys_config` is added to message `.google.container.v1beta1.ClusterUpdate` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `eviction_max_pod_grace_period_seconds` is added to message `.google.container.v1beta1.NodeKubeletConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `eviction_minimum_reclaim` is added to message `.google.container.v1beta1.NodeKubeletConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `eviction_soft_grace_period` is added to message `.google.container.v1beta1.NodeKubeletConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `eviction_soft` is added to message `.google.container.v1beta1.NodeKubeletConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `gke_auto_upgrade_config` is added to message `.google.container.v1beta1.Cluster` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `gke_auto_upgrade_config` is added to message `.google.container.v1beta1.ClusterUpdate` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `lustre_csi_driver_config` is added to message `.google.container.v1beta1.AddonsConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `max_parallel_image_pulls` is added to message `.google.container.v1beta1.NodeKubeletConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `min_node_cpus` is added to message `.google.container.v1beta1.SoleTenantConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `mode` is added to message `.google.container.v1beta1.AnonymousAuthenticationConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `single_process_oom_kill` is added to message `.google.container.v1beta1.NodeKubeletConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `subnetwork` is added to message `.google.container.v1beta1.NodeNetworkConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `transparent_hugepage_defrag` is added to message `.google.container.v1beta1.LinuxNodeConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new field `transparent_hugepage_enabled` is added to message `.google.container.v1beta1.LinuxNodeConfig` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `AdditionalIPRangesConfig` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `AutoIpamConfig` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `BootDisk` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `DefaultComputeClassConfig` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `DesiredAdditionalIPRangesConfig` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `EvictionGracePeriod` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `EvictionMinimumReclaim` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `EvictionSignals` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `GkeAutoUpgradeConfig` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new message `LustreCsiDriverConfig` is added ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))
* A new value `CLOUD_KMS_KEY_DESTROYED` is added to enum `Code` ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))


### Documentation

* updated comments for various types, messages, and fields. ([6e560b6](https://github.com/googleapis/google-cloud-python/commit/6e560b60e697bae3ac99cc4f0da08aee9352a57b))

## [2.58.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.57.0...google-cloud-container-v2.58.0) (2025-07-16)


### Features

* A new enum `Mode` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new enum `TransparentHugepageDefrag` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new enum `TransparentHugepageEnabled` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `additional_ip_ranges_configs` is added to message `.google.container.v1.IPAllocationPolicy` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `auto_ipam_config` is added to message `.google.container.v1.IPAllocationPolicy` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `boot_disk` is added to message `.google.container.v1.NodeConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `boot_disk` is added to message `.google.container.v1.UpdateNodePoolRequest` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `default_compute_class_config` is added to message `.google.container.v1.ClusterAutoscaling` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `desired_additional_ip_ranges_config` is added to message `.google.container.v1.ClusterUpdate` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `desired_auto_ipam_config` is added to message `.google.container.v1.ClusterUpdate` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `desired_user_managed_keys_config` is added to message `.google.container.v1.ClusterUpdate` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `eviction_max_pod_grace_period_seconds` is added to message `.google.container.v1.NodeKubeletConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `eviction_minimum_reclaim` is added to message `.google.container.v1.NodeKubeletConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `eviction_soft_grace_period` is added to message `.google.container.v1.NodeKubeletConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `eviction_soft` is added to message `.google.container.v1.NodeKubeletConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `gke_auto_upgrade_config` is added to message `.google.container.v1.Cluster` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `gke_auto_upgrade_config` is added to message `.google.container.v1.ClusterUpdate` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `lustre_csi_driver_config` is added to message `.google.container.v1.AddonsConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `max_parallel_image_pulls` is added to message `.google.container.v1.NodeKubeletConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `min_node_cpus` is added to message `.google.container.v1.SoleTenantConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `mode` is added to message `.google.container.v1.AnonymousAuthenticationConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `single_process_oom_kill` is added to message `.google.container.v1.NodeKubeletConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `subnetwork` is added to message `.google.container.v1.NodeNetworkConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `transparent_hugepage_defrag` is added to message `.google.container.v1.LinuxNodeConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new field `transparent_hugepage_enabled` is added to message `.google.container.v1.LinuxNodeConfig` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `AdditionalIPRangesConfig` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `AutoIpamConfig` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `BootDisk` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `DefaultComputeClassConfig` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `DesiredAdditionalIPRangesConfig` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `EvictionGracePeriod` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `EvictionMinimumReclaim` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `EvictionSignals` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `GkeAutoUpgradeConfig` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new message `LustreCsiDriverConfig` is added ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))
* A new value `CLOUD_KMS_KEY_DESTROYED` is added to enum `Code` ([f4d2243](https://github.com/googleapis/google-cloud-python/commit/f4d2243ec503df329818db074d349679cc442d9c))

## [2.57.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.56.1...google-cloud-container-v2.57.0) (2025-05-26)


### Features

* add allowed_unsafe_sysctls in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add allowed_unsafe_sysctls in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add alpha_cluster_feature_gates in Cluster ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add alpha_cluster_feature_gates in Cluster ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add anonymous_authentication_config in Cluster ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add auto_monitoring_config in ManagedPrometheusConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add auto_monitoring_config in ManagedPrometheusConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add autopilot_compatibility_auditing_enabled in WorkloadPolicyConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add autopilot_compatibility_auditing_enabled in WorkloadPolicyConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add ClusterUpgradeInfo ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add ClusterUpgradeInfo ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add confidential_instance_type in ConfidentialNodes ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add confidential_instance_type in ConfidentialNodes ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add container_log_max_files in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add container_log_max_files in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add container_log_max_size in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add container_log_max_size in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add control_plane_endpoints_config in Cluster ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add data_cache_count in EphemeralStorageLocalSsdConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add data_cache_count in EphemeralStorageLocalSsdConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add desired_anonymous_authentication_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_anonymous_authentication_config in ClusterUpdate ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add desired_compliance_posture_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_control_plane_endpoints_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_default_enable_private_nodes in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_disable_l4_lb_firewall_reconciliation in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_disable_l4_lb_firewall_reconciliation in ClusterUpdate ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add desired_enterprise_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_node_pool_auto_config_linux_node_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_pod_autoscaling in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add desired_pod_autoscaling in ClusterUpdate ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add desired_rbac_binding_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add disable_l4_lb_firewall_reconciliation in NetworkConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add disable_l4_lb_firewall_reconciliation in NetworkConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add effective_cgroup_mode in NodeConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add event_type in UpgradeInfoEvent ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add event_type in UpgradeInfoEvent ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add extended_support_end_time in UpgradeInfoEvent ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add extended_support_end_time in UpgradeInfoEvent ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add FetchClusterUpgradeInfoRequest ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add FetchClusterUpgradeInfoRequest ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add FetchNodePoolUpgradeInfoRequest ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add FetchNodePoolUpgradeInfoRequest ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add flex_start in NodeConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add flex_start in NodeConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add flex_start in UpdateNodePoolRequest ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add flex_start in UpdateNodePoolRequest ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add high_scale_checkpointing_config in AddonsConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add high_scale_checkpointing_config in AddonsConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add image_gc_high_threshold_percent in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add image_gc_high_threshold_percent in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add image_gc_low_threshold_percent in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add image_gc_low_threshold_percent in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add image_maximum_gc_age in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add image_maximum_gc_age in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add image_minimum_gc_age in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add image_minimum_gc_age in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add JOBSET in MonitoringComponentConfig.Component ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add JOBSET in MonitoringComponentConfig.Component ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add KCP_HPA in LoggingComponentConfig.Component ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add KCP_HPA in LoggingComponentConfig.Component ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add linux_node_config in NodePoolAutoConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add local_ssd_encryption_mode in NodeConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add max_run_duration in NodeConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add max_run_duration in NodeConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add max_run_duration in UpdateNodePoolRequest ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add max_run_duration in UpdateNodePoolRequest ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add MemoryManager ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add mitigated_versions in SecurityBulletinEvent ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add mitigated_versions in SecurityBulletinEvent ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add NODE_SERVICE_ACCOUNT_MISSING_PERMISSIONS in StatusCondition.Code ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add NODE_SERVICE_ACCOUNT_MISSING_PERMISSIONS in StatusCondition.Code ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add NodePoolUpgradeInfo ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add NodePoolUpgradeInfo ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add parallelstore_csi_driver_config in AddonsConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add performance_monitoring_unit in AdvancedMachineFeatures ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add performance_monitoring_unit in AdvancedMachineFeatures ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add pod_autoscaling in Cluster ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add pod_autoscaling in Cluster ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add private_endpoint_enforcement_enabled in MasterAuthorizedNetworksConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add rbac_binding_config in Cluster ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add standard_support_end_time in UpgradeInfoEvent ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add standard_support_end_time in UpgradeInfoEvent ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add storage_pools in NodeConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add storage_pools in UpdateNodePoolRequest ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add topology_manager in NodeKubeletConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add topology_manager in NodeKubeletConfig ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add TopologyManager ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add UPGRADE_INFO_EVENT in NotificationConfig.EventType ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add UPGRADE_INFO_EVENT in NotificationConfig.EventType ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add upgrade_target_version in ReleaseChannelConfig ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add UpgradeDetails ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add UpgradeDetails ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))
* add user_managed_keys_config in Cluster ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* add user_managed_keys_config in ClusterUpdate ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))


### Documentation

* Minor documentation updates ([82a928a](https://github.com/googleapis/google-cloud-python/commit/82a928a7c93c23e9c02f757bfa0f5cfdbd3ca89f))
* Minor documentation updates ([4c98f4e](https://github.com/googleapis/google-cloud-python/commit/4c98f4ea1879e3a7962bf64ea42e40a8b21b6ca1))

## [2.56.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.56.0...google-cloud-container-v2.56.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([1e43e75](https://github.com/googleapis/google-cloud-python/commit/1e43e75e99445373785b11381e0e859fa14bb485))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [2.56.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.55.1...google-cloud-container-v2.56.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))
* Add support for reading selective GAPIC generation methods from service YAML ([e22e2bd](https://github.com/googleapis/google-cloud-python/commit/e22e2bde55d11d2f85e9d2caf1d152a4027f88cf))

## [2.55.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.55.0...google-cloud-container-v2.55.1) (2025-01-27)


### Documentation

* [google-cloud-container] broken (or ambiguous) markdown link ([#13468](https://github.com/googleapis/google-cloud-python/issues/13468)) ([5579df8](https://github.com/googleapis/google-cloud-python/commit/5579df80a0859fb23b644ba666e63cc2864bf25b))

## [2.55.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.54.0...google-cloud-container-v2.55.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))

## [2.54.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.53.0...google-cloud-container-v2.54.0) (2024-11-11)


### Features

* add desired_enterprise_config,desired_node_pool_auto_config_linux_node_config to ClusterUpdate. ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))
* add desired_tier to EnterpriseConfig. ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))
* add DesiredEnterpriseConfig proto message ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))
* add LinuxNodeConfig in NodePoolAutoConfig ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))
* add LocalSsdEncryptionMode in NodeConfig ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))
* add UpgradeInfoEvent proto message ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))


### Bug Fixes

* disable universe-domain validation ([#13242](https://github.com/googleapis/google-cloud-python/issues/13242)) ([b479ff8](https://github.com/googleapis/google-cloud-python/commit/b479ff841ed93a18393a188ee1d72edf9fb729ec))


### Documentation

* Minor documentation updates ([4fdf249](https://github.com/googleapis/google-cloud-python/commit/4fdf24960b3966193516d6f16900df1409165376))

## [2.53.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.52.0...google-cloud-container-v2.53.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13206](https://github.com/googleapis/google-cloud-python/issues/13206)) ([eb980d5](https://github.com/googleapis/google-cloud-python/commit/eb980d55b2d01d776fa94c3ce408a11f6d366c8a))

## [2.52.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.51.0...google-cloud-container-v2.52.0) (2024-10-10)


### Features

* Add an effective_cgroup_mode field in node config ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* add API to enable/disable secret manager csi component on GKE clusters ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Add CompliancePosture field for configuration of GKE Compliance Posture product ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Add CompliancePosture field for configuration of GKE Compliance Posture product ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Add ControlPlaneEndpointsConfig message to consolidate control plane isolation options ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Add DNSEndpointConfig for new DNS-based control plane access ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Add KCP_SSHD and KCP_CONNECTION to the supported values for the --logging flag for the create and update cluster commands ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Add RBACBindingConfig to API ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* add storage pools field to NodePool API ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Added support for Parallelstore CSI Driver ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))
* Surface upgrade_target_version in GetServerConfig for all supported release channels ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))


### Documentation

* Minor documentation updates ([da74af6](https://github.com/googleapis/google-cloud-python/commit/da74af6f7f60cdeb9a09b54371a8608170ed8c0f))

## [2.51.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.50.0...google-cloud-container-v2.51.0) (2024-09-03)


### Features

* add `EXTENDED` enum value for `ReleaseChannel.Channel` ([ea71725](https://github.com/googleapis/google-cloud-python/commit/ea71725d3fe3bde0afd775d20127bed958e8eb8e))
* add ReleaseChannel EXTENDED value ([ea71725](https://github.com/googleapis/google-cloud-python/commit/ea71725d3fe3bde0afd775d20127bed958e8eb8e))

## [2.50.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.49.0...google-cloud-container-v2.50.0) (2024-07-30)


### Features

* [google-cloud-container] A new field ray_operator_config is added to message .google.container.v1beta1.AddonsConfig ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* [google-cloud-container] support for Ray Clusters ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* A new message `RayClusterLoggingConfig` is added ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* A new message `RayClusterMonitoringConfig` is added ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* A new message `RayOperatorConfig` is added ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([a6f7356](https://github.com/googleapis/google-cloud-python/commit/a6f7356f1549721f9fab83d4dcfa226cec1965d0))


### Documentation

* [google-cloud-container] minor updates to reference documentation ([#12919](https://github.com/googleapis/google-cloud-python/issues/12919)) ([732c303](https://github.com/googleapis/google-cloud-python/commit/732c303108a453b838e7f3c0fe0450ddf48eb2df))
* A comment for field `max_pods_per_node` in message `.google.container.v1beta1.AdditionalPodNetworkConfig` is changed ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* A comment for field `secondary_pod_range` in message `.google.container.v1beta1.AdditionalPodNetworkConfig` is changed ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* A comment for field `subnetwork` in message `.google.container.v1beta1.AdditionalPodNetworkConfig` is changed ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))
* trivial updates ([1cdd6d3](https://github.com/googleapis/google-cloud-python/commit/1cdd6d3d355db24fe217afbc04f3dae2b854efd9))

## [2.49.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.48.0...google-cloud-container-v2.49.0) (2024-07-11)


### Features

* add DCGM enum in monitoring config ([c321484](https://github.com/googleapis/google-cloud-python/commit/c321484b7eeccf02fd9ca12f982edbf3bac670a2))


### Bug Fixes

* Deprecate "EXPERIMENTAL" option for Gateway API ([c321484](https://github.com/googleapis/google-cloud-python/commit/c321484b7eeccf02fd9ca12f982edbf3bac670a2))

## [2.48.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.47.1...google-cloud-container-v2.48.0) (2024-07-10)


### Features

* [google-cloud-container] add DCGM enum in monitoring config ([#12892](https://github.com/googleapis/google-cloud-python/issues/12892)) ([ea0a4c9](https://github.com/googleapis/google-cloud-python/commit/ea0a4c983772a493995964805607c7dbed96b9a9))

## [2.47.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.47.0...google-cloud-container-v2.47.1) (2024-07-08)


### Bug Fixes

* [google-cloud-container] Deprecate "EXPERIMENTAL" option for Gateway API (this value has never been supported) ([#12856](https://github.com/googleapis/google-cloud-python/issues/12856)) ([6bbe99f](https://github.com/googleapis/google-cloud-python/commit/6bbe99f04005b7bd119023941b9a9d6788c04111))
* Allow Protobuf 5.x ([#12865](https://github.com/googleapis/google-cloud-python/issues/12865)) ([7f9dedb](https://github.com/googleapis/google-cloud-python/commit/7f9dedb3abc7636cbcd97e21ac857844b885b599))

## [2.47.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.46.0...google-cloud-container-v2.47.0) (2024-06-10)


### Features

* A new field `accelerators` is added to message `.google.container.v1.UpdateNodePoolRequest` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `additive_vpc_scope_dns_domain` is added to message `.google.container.v1.DNSConfig` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `containerd_config` is added to message `.google.container.v1.NodeConfig` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `containerd_config` is added to message `.google.container.v1.NodeConfigDefaults` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `containerd_config` is added to message `.google.container.v1.UpdateNodePoolRequest` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `desired_containerd_config` is added to message `.google.container.v1.ClusterUpdate` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `desired_node_kubelet_config` is added to message `.google.container.v1.ClusterUpdate` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `desired_node_pool_auto_config_kubelet_config` is added to message `.google.container.v1.ClusterUpdate` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `enable_nested_virtualization` is added to message `.google.container.v1.AdvancedMachineFeatures` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `hugepages` is added to message `.google.container.v1.LinuxNodeConfig` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `node_kubelet_config` is added to message `.google.container.v1.NodeConfigDefaults` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `node_kubelet_config` is added to message `.google.container.v1.NodePoolAutoConfig` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `satisfies_pzi` is added to message `.google.container.v1.Cluster` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new field `satisfies_pzs` is added to message `.google.container.v1.Cluster` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new message `ContainerdConfig` is added ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new message `HugepagesConfig` is added ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new method_signature `parent` is added to method `ListOperations` in service `ClusterManager` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new value `CADVISOR` is added to enum `Component` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new value `ENTERPRISE` is added to enum `Mode` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new value `KUBELET` is added to enum `Component` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A new value `MPS` is added to enum `GPUSharingStrategy` ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* Enable REST transport for google/container/v1 ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))


### Documentation

* A comment for field `desired_private_cluster_config` in message `.google.container.v1.ClusterUpdate` is changed ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))
* A comment for field `in_transit_encryption_config` in message `.google.container.v1.NetworkConfig` is changed ([0d738fa](https://github.com/googleapis/google-cloud-python/commit/0d738fa1a8751a1cee2071c7af187e2d08b1a889))

## [2.46.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.45.0...google-cloud-container-v2.46.0) (2024-05-29)


### Features

* A new message `HugepagesConfig` is added ([e0c6241](https://github.com/googleapis/google-cloud-python/commit/e0c6241e3c93cba3529288744fd73cc1cd1dfcb0))


### Documentation

* A comment for field `desired_in_transit_encryption_config` in message `.google.container.v1beta1.ClusterUpdate` is changed ([e0c6241](https://github.com/googleapis/google-cloud-python/commit/e0c6241e3c93cba3529288744fd73cc1cd1dfcb0))
* A comment for field `desired_private_cluster_config` in message `.google.container.v1beta1.ClusterUpdate` is changed ([e0c6241](https://github.com/googleapis/google-cloud-python/commit/e0c6241e3c93cba3529288744fd73cc1cd1dfcb0))

## [2.45.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.44.0...google-cloud-container-v2.45.0) (2024-03-27)


### Features

* [google-cloud-container] add several fields to manage state of ([7a82f6f](https://github.com/googleapis/google-cloud-python/commit/7a82f6ffe9f51b32e0f76b9e9dafaddb5865d344))
* [google-cloud-container] add several fields to manage state of database encryption update ([#12513](https://github.com/googleapis/google-cloud-python/issues/12513)) ([7a82f6f](https://github.com/googleapis/google-cloud-python/commit/7a82f6ffe9f51b32e0f76b9e9dafaddb5865d344))

## [2.44.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.43.0...google-cloud-container-v2.44.0) (2024-03-22)


### Features

* [google-cloud-container] add optional secondary_boot_disk_update_strategy field to NodePool API ([f88a75d](https://github.com/googleapis/google-cloud-python/commit/f88a75d752fc9798a64eb436ece3effb8f05027a))
* allow existing clusters to enable multi-networking ([f88a75d](https://github.com/googleapis/google-cloud-python/commit/f88a75d752fc9798a64eb436ece3effb8f05027a))

## [2.43.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.42.0...google-cloud-container-v2.43.0) (2024-03-07)


### Features

* [google-cloud-container] add API to enable/disable secret manager csi component on GKE clusters ([#12421](https://github.com/googleapis/google-cloud-python/issues/12421)) ([30d38b5](https://github.com/googleapis/google-cloud-python/commit/30d38b5758118a30dddf45443e8694131bb172fc))
* Add API to enable/disable secret manager csi component on GKE clusters ([358ef49](https://github.com/googleapis/google-cloud-python/commit/358ef49cba7acb091de627293f9f0e5b63f27ece))
* Add secondary boot disks field to NodePool API ([358ef49](https://github.com/googleapis/google-cloud-python/commit/358ef49cba7acb091de627293f9f0e5b63f27ece))

## [2.42.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.41.0...google-cloud-container-v2.42.0) (2024-03-04)


### Features

* add API to enable Provisioning Request API on existing nodepools ([43e63be](https://github.com/googleapis/google-cloud-python/commit/43e63be479ab80d4d3be2c47c3be530db4d30993))
* add secondary boot disks field to NodePool API ([43e63be](https://github.com/googleapis/google-cloud-python/commit/43e63be479ab80d4d3be2c47c3be530db4d30993))


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([43e63be](https://github.com/googleapis/google-cloud-python/commit/43e63be479ab80d4d3be2c47c3be530db4d30993))


### Documentation

* Update comment for field `enable_confidential_storage` in message `google.container.v1beta1.NodeConfig` ([43e63be](https://github.com/googleapis/google-cloud-python/commit/43e63be479ab80d4d3be2c47c3be530db4d30993))

## [2.41.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.40.0...google-cloud-container-v2.41.0) (2024-02-22)


### Features

* [google-cloud-container] added configuration for the StatefulHA addon to the AddonsConfig ([38daeac](https://github.com/googleapis/google-cloud-python/commit/38daeace2bf4a8fdf6662799b7350b516013aff4))
* add API to enable Provisioning Request API on existing nodepools ([d652877](https://github.com/googleapis/google-cloud-python/commit/d652877364426929dddc0060243fca75bca89839))
* Promoted enable_confidential_storage to GA (behind allowlist) ([d652877](https://github.com/googleapis/google-cloud-python/commit/d652877364426929dddc0060243fca75bca89839))


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12305](https://github.com/googleapis/google-cloud-python/issues/12305)) ([2aa7f17](https://github.com/googleapis/google-cloud-python/commit/2aa7f17a5fd4f2249260225db91fb0414d06eaa7))
* fix ValueError in test__validate_universe_domain ([38daeac](https://github.com/googleapis/google-cloud-python/commit/38daeace2bf4a8fdf6662799b7350b516013aff4))

## [2.40.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.39.0...google-cloud-container-v2.40.0) (2024-02-06)


### Features

* new AddonsConfig field stateful_ha_config ([e5788c2](https://github.com/googleapis/google-cloud-python/commit/e5788c240181151820f62329b34c004dcf73e94c))
* new message StatefulHAConfig ([e5788c2](https://github.com/googleapis/google-cloud-python/commit/e5788c240181151820f62329b34c004dcf73e94c))


### Bug Fixes

* Add google-auth as a direct dependency ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))


### Documentation

* Autopilot.conversion_status is now OUTPUT_ONLY ([e5788c2](https://github.com/googleapis/google-cloud-python/commit/e5788c240181151820f62329b34c004dcf73e94c))
* update Autopilot.conversion_status comment with behavior ([e5788c2](https://github.com/googleapis/google-cloud-python/commit/e5788c240181151820f62329b34c004dcf73e94c))

## [2.39.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.38.0...google-cloud-container-v2.39.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12239](https://github.com/googleapis/google-cloud-python/issues/12239)) ([8004d15](https://github.com/googleapis/google-cloud-python/commit/8004d15d9e6baa4dc5bc3f09d528e176d54d9ec5))

## [2.38.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.37.0...google-cloud-container-v2.38.0) (2024-01-22)


### Features

* Add fields desired_in_transit_encryption_config and in_transit_encryption_config ([c25ed93](https://github.com/googleapis/google-cloud-python/commit/c25ed93f4b0ffcfad99818e47dfcaf1bafc7c851))


### Documentation

* Remove Not GA comments for GetOpenIDConfig and GetJSONWebKeys ([c25ed93](https://github.com/googleapis/google-cloud-python/commit/c25ed93f4b0ffcfad99818e47dfcaf1bafc7c851))

## [2.37.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.36.0...google-cloud-container-v2.37.0) (2024-01-04)


### Features

* [google-cloud-container] Add autoscaled node pool upgrade strategy ([#12135](https://github.com/googleapis/google-cloud-python/issues/12135)) ([1729080](https://github.com/googleapis/google-cloud-python/commit/172908041f50a3c661cea23dca3932b037005e95))

## [2.36.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.35.0...google-cloud-container-v2.36.0) (2023-12-07)


### Features

* Add support for python 3.12 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Introduce compatibility with native namespace packages ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Use `retry_async` instead of `retry` in async client ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))

## [2.35.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.34.0...google-cloud-container-v2.35.0) (2023-11-29)


### Features

* [google-cloud-container] add Provisioning Request API ([#12030](https://github.com/googleapis/google-cloud-python/issues/12030)) ([c858b5a](https://github.com/googleapis/google-cloud-python/commit/c858b5aa9f65b7a0725d013598ab8274eb3ee89f))
* add enable_relay field to AdvancedDatapathObservabilityConfig ([90eea69](https://github.com/googleapis/google-cloud-python/commit/90eea69a477cc820e82b75242559696463b2f2b7))
* Add enable_relay field to AdvancedDatapathObservabilityConfig ([a12d82f](https://github.com/googleapis/google-cloud-python/commit/a12d82f77fa7b8a35d271880c8bbba9e0d8f8825))
* Enable Enterprise Flag to allow configuring Advanced Vuln Insights ([a12d82f](https://github.com/googleapis/google-cloud-python/commit/a12d82f77fa7b8a35d271880c8bbba9e0d8f8825))


### Documentation

* [google-cloud-container] improve API documentation for Binary Authorization ([#12049](https://github.com/googleapis/google-cloud-python/issues/12049)) ([a927596](https://github.com/googleapis/google-cloud-python/commit/a9275968985b1bffa5b4ebad1f90259963aa1b88))

## [2.34.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.33.0...google-cloud-container-v2.34.0) (2023-11-16)


### Features

* Add AutopilotConversionStatus ([21c6d43](https://github.com/googleapis/google-cloud-python/commit/21c6d431e9b3166fc40b906b1d5b3788c0cfb224))
* Add Provisioning Request API ([21c6d43](https://github.com/googleapis/google-cloud-python/commit/21c6d431e9b3166fc40b906b1d5b3788c0cfb224))


### Documentation

* Improve NodePool documentation ([21c6d43](https://github.com/googleapis/google-cloud-python/commit/21c6d431e9b3166fc40b906b1d5b3788c0cfb224))

## [2.33.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.32.0...google-cloud-container-v2.33.0) (2023-11-02)


### Features

* add a new cluster field for the cluster tier of GKE clusters ([63668fe](https://github.com/googleapis/google-cloud-python/commit/63668febe0b2d3a0ffce2cbf7e23a61a499817a3))
* add CompleteConvertToAutopilot API to commit Autopilot conversion operation ([80b7a92](https://github.com/googleapis/google-cloud-python/commit/80b7a926ac91006f466d15b43a2d6988be69eac0))
* add ResourceManagerTags API to attach tags on the underlying Compute Engine VMs of GKE Nodes ([80b7a92](https://github.com/googleapis/google-cloud-python/commit/80b7a926ac91006f466d15b43a2d6988be69eac0))
* added EnterpriseConfig ([63668fe](https://github.com/googleapis/google-cloud-python/commit/63668febe0b2d3a0ffce2cbf7e23a61a499817a3))
* **v1beta1:** adding a field to allow turn the DPv2 node to node encryption feature on or off ([80b7a92](https://github.com/googleapis/google-cloud-python/commit/80b7a926ac91006f466d15b43a2d6988be69eac0))


### Documentation

* updated comments ([80b7a92](https://github.com/googleapis/google-cloud-python/commit/80b7a926ac91006f466d15b43a2d6988be69eac0))

## [2.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-container-v2.31.0...google-cloud-container-v2.32.0) (2023-09-30)


### Features

* add SecurityPostureConfig Enterprise vuln mode to allow customers to enable Advanced Vulnerability Scanning for their clusters ([#413](https://github.com/googleapis/google-cloud-python/issues/413)) ([0280a30](https://github.com/googleapis/google-cloud-python/commit/0280a30e0f95e8d422e3179029e8bf9a35a5e304))


### Documentation

* Minor formatting ([#411](https://github.com/googleapis/google-cloud-python/issues/411)) ([1408937](https://github.com/googleapis/google-cloud-python/commit/14089372702399a5d4401191bd6ad0727e6cd067))

## [2.31.0](https://github.com/googleapis/python-container/compare/v2.30.0...v2.31.0) (2023-08-28)


### Features

* Add `machine_type`, `disk_type`, `disk_size_gb` fields to `UpdateNodePoolRequest` ([a1e508c](https://github.com/googleapis/python-container/commit/a1e508c53415ea816ed2649a46b791947bf87705))
* Add support for NodeConfig Update ([a1e508c](https://github.com/googleapis/python-container/commit/a1e508c53415ea816ed2649a46b791947bf87705))
* Publicize tpu topology in v1 API ([a1e508c](https://github.com/googleapis/python-container/commit/a1e508c53415ea816ed2649a46b791947bf87705))

## [2.30.0](https://github.com/googleapis/python-container/compare/v2.29.0...v2.30.0) (2023-08-11)


### Features

* **v1beta1:** Add preview support for monitoring a cluster's pods for compliance with a provided Binary Authorization platform policy via Binary Authorization Continuous Validation ([#405](https://github.com/googleapis/python-container/issues/405)) ([c5806de](https://github.com/googleapis/python-container/commit/c5806de9c61b1c9855f1c9a5c3fac1ea343e1acc))

## [2.29.0](https://github.com/googleapis/python-container/compare/v2.28.0...v2.29.0) (2023-08-09)


### Features

* Add APIs for GKE OOTB metrics packages ([#403](https://github.com/googleapis/python-container/issues/403)) ([834872a](https://github.com/googleapis/python-container/commit/834872af197b113183024f6711e36e8a88aad47e))

## [2.28.0](https://github.com/googleapis/python-container/compare/v2.27.0...v2.28.0) (2023-07-24)


### Features

* **v1beta1:** Add enable_multi_networking to NetworkConfig ([02c497e](https://github.com/googleapis/python-container/commit/02c497ec42f3d51a28e31b3cca940e5a147960bd))
* **v1beta1:** Add policy_name to PlacementPolicy message within a node pool ([02c497e](https://github.com/googleapis/python-container/commit/02c497ec42f3d51a28e31b3cca940e5a147960bd))
* **v1beta1:** Add support for AdditionalPodNetworkConfig and AdditionalNodeNetworkConfig ([02c497e](https://github.com/googleapis/python-container/commit/02c497ec42f3d51a28e31b3cca940e5a147960bd))
* **v1beta1:** Add support for HostMaintenancePolicy ([02c497e](https://github.com/googleapis/python-container/commit/02c497ec42f3d51a28e31b3cca940e5a147960bd))

## [2.27.0](https://github.com/googleapis/python-container/compare/v2.26.0...v2.27.0) (2023-07-19)


### Features

* Add a Pod IP Utilization API ([b5dfb67](https://github.com/googleapis/python-container/commit/b5dfb6725c1a9097254959908af739cd3f7a20ea))
* Add advanced_datapath_observability_config to monitoring_config ([b5dfb67](https://github.com/googleapis/python-container/commit/b5dfb6725c1a9097254959908af739cd3f7a20ea))
* Add Multi-networking API ([5c5cc4f](https://github.com/googleapis/python-container/commit/5c5cc4fbe54affde3744da3203c6bd2aeb733d61))
* Add policy_name to PlacementPolicy message within a node pool ([5c5cc4f](https://github.com/googleapis/python-container/commit/5c5cc4fbe54affde3744da3203c6bd2aeb733d61))

## [2.26.0](https://github.com/googleapis/python-container/compare/v2.25.0...v2.26.0) (2023-07-04)


### Features

* **v1beta1:** Add `InsecureKubeletReadonlyPortEnabled` in `NodeKubeletConfig` and `AutoProvisioningNodePoolDefaults` ([be6b0ab](https://github.com/googleapis/python-container/commit/be6b0ab88931a3c6a64cc92b8b0dbd33b82be255))
* **v1beta1:** Add `KUBE_DNS` option to `DNSConfig.cluster_dns` ([be6b0ab](https://github.com/googleapis/python-container/commit/be6b0ab88931a3c6a64cc92b8b0dbd33b82be255))
* **v1beta1:** Add a Pod IP Utilization API ([be6b0ab](https://github.com/googleapis/python-container/commit/be6b0ab88931a3c6a64cc92b8b0dbd33b82be255))
* **v1beta1:** Add Tier 1 cluster-level API network_performance_config ([be6b0ab](https://github.com/googleapis/python-container/commit/be6b0ab88931a3c6a64cc92b8b0dbd33b82be255))
* **v1beta1:** Publicize tpu topology ([be6b0ab](https://github.com/googleapis/python-container/commit/be6b0ab88931a3c6a64cc92b8b0dbd33b82be255))


### Bug Fixes

* Add async context manager return types ([#385](https://github.com/googleapis/python-container/issues/385)) ([074edd4](https://github.com/googleapis/python-container/commit/074edd4c4f8cd10d8cd2afa5d8fb09f1c951c292))

## [2.25.0](https://github.com/googleapis/python-container/compare/v2.24.0...v2.25.0) (2023-06-29)


### Features

* Add `KUBE_DNS` option to `DNSConfig.cluster_dns` ([91b001a](https://github.com/googleapis/python-container/commit/91b001a4f89557e8a503c57de3e45d6bf399ea90))
* Add Tier 1 cluster-level API network_performance_config ([91b001a](https://github.com/googleapis/python-container/commit/91b001a4f89557e8a503c57de3e45d6bf399ea90))

## [2.24.0](https://github.com/googleapis/python-container/compare/v2.23.0...v2.24.0) (2023-06-13)


### Features

* Add API for GPU driver installation config ([d6da309](https://github.com/googleapis/python-container/commit/d6da30922e76d8c56b8ec3c78b0cb8ffbb5bd82a))
* Add SecurityPostureConfig API field to allow customers to enable GKE Security Posture capabilities for their clusters ([d6da309](https://github.com/googleapis/python-container/commit/d6da30922e76d8c56b8ec3c78b0cb8ffbb5bd82a))
* Add workloadPolicyConfig API field to allow customer enable NET_ADMIN capability for their autopilot clusters ([d6da309](https://github.com/googleapis/python-container/commit/d6da30922e76d8c56b8ec3c78b0cb8ffbb5bd82a))

## [2.23.0](https://github.com/googleapis/python-container/compare/v2.22.0...v2.23.0) (2023-06-06)


### Features

* Add a API field to enable FQDN Network Policy on clusters ([52d1480](https://github.com/googleapis/python-container/commit/52d14803c65c06f65c1dcf7679faa9c6a0cca784))
* Add CheckAutopilotCompatibility API to get autopilot compatibility issues for a given standard cluster ([52d1480](https://github.com/googleapis/python-container/commit/52d14803c65c06f65c1dcf7679faa9c6a0cca784))
* Turn on public visibility for best effort provision ([52d1480](https://github.com/googleapis/python-container/commit/52d14803c65c06f65c1dcf7679faa9c6a0cca784))

## [2.22.0](https://github.com/googleapis/python-container/compare/v2.21.0...v2.22.0) (2023-06-01)


### Features

* Add SoleTenantConfig API ([f3126af](https://github.com/googleapis/python-container/commit/f3126afbc21296e5f3e0608276bc7903ae969fe3))
* Cluster resizes will now have their own operation type (RESIZE_CLUSTER) instead of reusing REPAIR_CLUSTER; they will start using this in the near future ([f3126af](https://github.com/googleapis/python-container/commit/f3126afbc21296e5f3e0608276bc7903ae969fe3))
* Support fleet registration via cluster update ([f3126af](https://github.com/googleapis/python-container/commit/f3126afbc21296e5f3e0608276bc7903ae969fe3))


### Documentation

* Clarified release channel defaulting behavior for create cluster requests when release channel is unspecified ([f3126af](https://github.com/googleapis/python-container/commit/f3126afbc21296e5f3e0608276bc7903ae969fe3))
* Operation.self_link and Operation.target_link given examples ([f3126af](https://github.com/googleapis/python-container/commit/f3126afbc21296e5f3e0608276bc7903ae969fe3))
* Operation.Type is now documented in detail ([f3126af](https://github.com/googleapis/python-container/commit/f3126afbc21296e5f3e0608276bc7903ae969fe3))

## [2.21.0](https://github.com/googleapis/python-container/compare/v2.20.0...v2.21.0) (2023-04-15)


### Features

* Add support for updating additional pod IPv4 ranges for Standard and Autopilot clusters ([#367](https://github.com/googleapis/python-container/issues/367)) ([533b4f9](https://github.com/googleapis/python-container/commit/533b4f91a9175cbd9bf892b93a38b283316f272d))

## [2.20.0](https://github.com/googleapis/python-container/compare/v2.19.0...v2.20.0) (2023-04-11)


### Features

* Add support for updating additional pod IPv4 ranges for Standard and Autopilot clusters ([#365](https://github.com/googleapis/python-container/issues/365)) ([c9c29c4](https://github.com/googleapis/python-container/commit/c9c29c46f3c6a8d4dfebec3ec36e5c7fc6052bb7))

## [2.19.0](https://github.com/googleapis/python-container/compare/v2.18.0...v2.19.0) (2023-04-06)


### Features

* Add support for disabling pod IP cidr overprovision. This feature requires special allowlisting for the projects. ([56f65fa](https://github.com/googleapis/python-container/commit/56f65fa23de31317e4cf39e50351ad1e1bb04b57))
* Add update support for accelerator config ([56f65fa](https://github.com/googleapis/python-container/commit/56f65fa23de31317e4cf39e50351ad1e1bb04b57))

## [2.18.0](https://github.com/googleapis/python-container/compare/v2.17.4...v2.18.0) (2023-03-28)


### Features

* Add a new fleet registration feature to v1beta1, v1 ([#360](https://github.com/googleapis/python-container/issues/360)) ([0bfdffe](https://github.com/googleapis/python-container/commit/0bfdffe31e660c3914081181c611efd5582a05d3))


### Documentation

* Fix formatting of request arg in docstring ([#359](https://github.com/googleapis/python-container/issues/359)) ([d10ac7e](https://github.com/googleapis/python-container/commit/d10ac7e8db4d79011f1b5fa1bb508a8829a683ac))
* Minor typo fix ([#356](https://github.com/googleapis/python-container/issues/356)) ([f41b699](https://github.com/googleapis/python-container/commit/f41b699907991248b0d14bd9d5ae3ab4a8e1aff7))

## [2.17.4](https://github.com/googleapis/python-container/compare/v2.17.3...v2.17.4) (2023-02-28)


### Documentation

* Minor grammar improvements ([#351](https://github.com/googleapis/python-container/issues/351)) ([2a0eeae](https://github.com/googleapis/python-container/commit/2a0eeae897e7f2312690eed1e52119a6a572c667))

## [2.17.3](https://github.com/googleapis/python-container/compare/v2.17.2...v2.17.3) (2023-02-03)


### Documentation

* Add clarification on whether `NodePool.version` is a required field ([#344](https://github.com/googleapis/python-container/issues/344)) ([071c147](https://github.com/googleapis/python-container/commit/071c147df8e6edd72ff66b1997f21e881acd9b32))

## [2.17.2](https://github.com/googleapis/python-container/compare/v2.17.1...v2.17.2) (2023-01-30)


### Documentation

* Add references for available node image types ([76cfff8](https://github.com/googleapis/python-container/commit/76cfff85542aa1a8326efbfbc6d1c95b663e1452))
* Clarified wording around the NodePoolUpdateStrategy default behavior ([76cfff8](https://github.com/googleapis/python-container/commit/76cfff85542aa1a8326efbfbc6d1c95b663e1452))

## [2.17.1](https://github.com/googleapis/python-container/compare/v2.17.0...v2.17.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([cc5ebab](https://github.com/googleapis/python-container/commit/cc5ebabb1d584b137c42f45f55e6b803db72bf6d))


### Documentation

* Add documentation for enums ([cc5ebab](https://github.com/googleapis/python-container/commit/cc5ebabb1d584b137c42f45f55e6b803db72bf6d))

## [2.17.0](https://github.com/googleapis/python-container/compare/v2.16.0...v2.17.0) (2023-01-17)


### Features

* Add support for viewing the subnet IPv6 CIDR and services IPv6 CIDR assigned to dual stack clusters ([#333](https://github.com/googleapis/python-container/issues/333)) ([4d0a583](https://github.com/googleapis/python-container/commit/4d0a583f4ff23dca157b7835d9e59ec7ca9d16da))

## [2.16.0](https://github.com/googleapis/python-container/compare/v2.15.0...v2.16.0) (2023-01-10)


### Features

* Add etags for cluster and node pool update operations ([8eeee3b](https://github.com/googleapis/python-container/commit/8eeee3bda1e0eaae6fb375b47cc68b959f9b9feb))
* Add support for python 3.11 ([8eeee3b](https://github.com/googleapis/python-container/commit/8eeee3bda1e0eaae6fb375b47cc68b959f9b9feb))

## [2.15.0](https://github.com/googleapis/python-container/compare/v2.14.0...v2.15.0) (2023-01-09)


### Features

* Add EphemeralStorageLocalSsdConfig and LocalNvmeSsdBlockConfig APIs ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Add etags for cluster and node pool update operations ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Add support for specifying stack type for clusters ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Add WindowsNodeConfig field ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* CLUSTER_SCOPE option now available in DNSScope ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Release GKE CloudDNS Cluster Scope ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))

## [2.14.0](https://github.com/googleapis/python-container/compare/v2.13.0...v2.14.0) (2022-12-15)


### Features

* Add API to enable GKE Gateway controller ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add compact placement feature for node pools ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add nodeconfig resource_labels api ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add support for `google.cloud.container.__version__` ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add support for specifying stack type for clusters. This will allow clusters to be created as dual stack or toggled between IPV4 and dual stack ([#323](https://github.com/googleapis/python-container/issues/323)) ([5c1d04f](https://github.com/googleapis/python-container/commit/5c1d04f874b64aabc378aa18370e0b6be503a886))
* Add typing to proto.Message based class attributes ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* GKE cluster's control plan/node-pool network isolation ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* **v1:** Add a FastSocket API ([4d61084](https://github.com/googleapis/python-container/commit/4d61084846ae9583140b04a4c68da070479d79b9))
* **v1beta1:** Add a FastSocket API ([#319](https://github.com/googleapis/python-container/issues/319)) ([5072864](https://github.com/googleapis/python-container/commit/50728649c915df27e8876af572ef824a26a660b7))


### Bug Fixes

* Add dict typing for client_options ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))
* Drop usage of pkg_resources ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))
* Fix timeout default values ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))

## [2.13.0](https://github.com/googleapis/python-container/compare/v2.12.2...v2.13.0) (2022-10-26)


### Features

* launch GKE Cost Allocations configuration to the v1 GKE API ([d625e34](https://github.com/googleapis/python-container/commit/d625e3456bd37aa6cca4b0cf9de44c9ddb69ec21))
* vulnerability scanning exposed to public ([d625e34](https://github.com/googleapis/python-container/commit/d625e3456bd37aa6cca4b0cf9de44c9ddb69ec21))

## [2.12.2](https://github.com/googleapis/python-container/compare/v2.12.1...v2.12.2) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#305](https://github.com/googleapis/python-container/issues/305)) ([728fc48](https://github.com/googleapis/python-container/commit/728fc485d91c113a151dea2641ccfe163a5accaf))

## [2.12.1](https://github.com/googleapis/python-container/compare/v2.12.0...v2.12.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#301](https://github.com/googleapis/python-container/issues/301)) ([a4d1351](https://github.com/googleapis/python-container/commit/a4d1351c67659624d373f1fe4e3f5c61e99fa074))

## [2.12.0](https://github.com/googleapis/python-container/compare/v2.11.2...v2.12.0) (2022-09-16)


### Features

* Added High Throughput Logging API for Google Kubernetes Engine ([#297](https://github.com/googleapis/python-container/issues/297)) ([f774719](https://github.com/googleapis/python-container/commit/f7747196207f8487a4d50c93d76f8ea6e02f3f7c))


### Documentation

* missing period in description for min CPU platform ([f774719](https://github.com/googleapis/python-container/commit/f7747196207f8487a4d50c93d76f8ea6e02f3f7c))
* ReservationAffinity key field docs incorrect ([f774719](https://github.com/googleapis/python-container/commit/f7747196207f8487a4d50c93d76f8ea6e02f3f7c))

## [2.11.2](https://github.com/googleapis/python-container/compare/v2.11.1...v2.11.2) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([d68c842](https://github.com/googleapis/python-container/commit/d68c842bddad08c52ff0e4f1b34b70b4db667f8e))
* **deps:** require proto-plus >= 1.22.0 ([d68c842](https://github.com/googleapis/python-container/commit/d68c842bddad08c52ff0e4f1b34b70b4db667f8e))

## [2.11.1](https://github.com/googleapis/python-container/compare/v2.11.0...v2.11.1) (2022-08-02)


### Documentation

* **v1beta1:** BinaryAuthorization.enabled field is marked as deprecated ([0088035](https://github.com/googleapis/python-container/commit/00880358b4021191ff90f1f2a0f08160ce7b6d6a))
* **v1:** BinaryAuthorization.enabled field is marked as deprecated ([#272](https://github.com/googleapis/python-container/issues/272)) ([0088035](https://github.com/googleapis/python-container/commit/00880358b4021191ff90f1f2a0f08160ce7b6d6a))

## [2.11.0](https://github.com/googleapis/python-container/compare/v2.10.8...v2.11.0) (2022-07-16)


### Features

* add audience parameter ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add Binauthz Evaluation mode support to GKE Classic ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add GKE Identity Service ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add Location Policy API ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add managed prometheus feature ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add network tags to autopilot cluster ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add support to modify kubelet pod pid limit in node system configuration ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support enabling Confidential Nodes in the node pool ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support GPU timesharing ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support node pool blue-green upgrade ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support spot VM ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support Tier 1 bandwidth ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* update support for node pool labels, taints and network tags ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* require python 3.7+ ([#266](https://github.com/googleapis/python-container/issues/266)) ([01b78af](https://github.com/googleapis/python-container/commit/01b78af7d314551d69075005abd5f4e4ac826f5f))

## [2.10.8](https://github.com/googleapis/python-container/compare/v2.10.7...v2.10.8) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#252](https://github.com/googleapis/python-container/issues/252)) ([f5ab2a8](https://github.com/googleapis/python-container/commit/f5ab2a89d1238b2315963f4dd8469323746459f0))


### Documentation

* fix changelog header to consistent size ([#253](https://github.com/googleapis/python-container/issues/253)) ([9db4c78](https://github.com/googleapis/python-container/commit/9db4c786430da9a5831893a31321cb0e65db4751))

## [2.10.7](https://github.com/googleapis/python-container/compare/v2.10.6...v2.10.7) (2022-03-22)


### Bug Fixes

* test cleanup stages with try finally ([#212](https://github.com/googleapis/python-container/issues/212)) ([529bcbf](https://github.com/googleapis/python-container/commit/529bcbf618858aab17b6f5e86d25069a1266860a))

## [2.10.6](https://github.com/googleapis/python-container/compare/v2.10.5...v2.10.6) (2022-03-07)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#202](https://github.com/googleapis/python-container/issues/202)) ([444b806](https://github.com/googleapis/python-container/commit/444b8065a22da4c261b8b33ae8564d8329d3435d))
* **deps:** require proto-plus>=1.15.0 ([444b806](https://github.com/googleapis/python-container/commit/444b8065a22da4c261b8b33ae8564d8329d3435d))

## [2.10.5](https://github.com/googleapis/python-container/compare/v2.10.4...v2.10.5) (2022-02-16)


### Documentation

* **samples:** add usage samples to show handling of LRO response Operation ([#191](https://github.com/googleapis/python-container/issues/191)) ([309ad62](https://github.com/googleapis/python-container/commit/309ad6219a6e80d08bcd365a163e8273a6413ede))

## [2.10.4](https://github.com/googleapis/python-container/compare/v2.10.3...v2.10.4) (2022-02-14)


### Bug Fixes

* **deps:** move libcst to extras ([#194](https://github.com/googleapis/python-container/issues/194)) ([1c308c2](https://github.com/googleapis/python-container/commit/1c308c2e44dc16d0e8df5976de0b65d1e7c2041e))

## [2.10.3](https://github.com/googleapis/python-container/compare/v2.10.2...v2.10.3) (2022-02-11)


### Documentation

* add generated snippets ([#192](https://github.com/googleapis/python-container/issues/192)) ([e3a3a05](https://github.com/googleapis/python-container/commit/e3a3a056d80ac713edbf5cb4a8358063f8a83214))

## [2.10.2](https://github.com/googleapis/python-container/compare/v2.10.1...v2.10.2) (2022-02-04)

### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([07fbf3c](https://github.com/googleapis/python-container/commit/07fbf3cb1e140abf020e7cfbd083ed79aae701bf))

## [2.10.1](https://www.github.com/googleapis/python-container/compare/v2.10.0...v2.10.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([838a97b](https://www.github.com/googleapis/python-container/commit/838a97b0a45dcb16e81ec3795beaf35eaa5e460d))
* **deps:** require google-api-core >= 1.28.0 ([838a97b](https://www.github.com/googleapis/python-container/commit/838a97b0a45dcb16e81ec3795beaf35eaa5e460d))


### Documentation

* list oneofs in docstring ([838a97b](https://www.github.com/googleapis/python-container/commit/838a97b0a45dcb16e81ec3795beaf35eaa5e460d))

## [2.10.0](https://www.github.com/googleapis/python-container/compare/v2.9.0...v2.10.0) (2021-10-13)


### Features

* add support for python 3.10 ([#160](https://www.github.com/googleapis/python-container/issues/160)) ([ab146a5](https://www.github.com/googleapis/python-container/commit/ab146a5017805ec200dab2b74e025de0c647d742))

## [2.9.0](https://www.github.com/googleapis/python-container/compare/v2.8.1...v2.9.0) (2021-10-08)


### Features

* add context manager support in client ([#157](https://www.github.com/googleapis/python-container/issues/157)) ([03953f8](https://www.github.com/googleapis/python-container/commit/03953f8087b2583369b877672be81f2b8638020c))

## [2.8.1](https://www.github.com/googleapis/python-container/compare/v2.8.0...v2.8.1) (2021-10-04)


### Bug Fixes

* improper types in pagers generation ([6814251](https://www.github.com/googleapis/python-container/commit/68142512b75ee81a1fee0e982edd00a617706a00))

## [2.8.0](https://www.github.com/googleapis/python-container/compare/v2.7.1...v2.8.0) (2021-09-23)


### Features

* added a flag to enable/disable gvnic on a node pool ([#147](https://www.github.com/googleapis/python-container/issues/147)) ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added configuration for node pool defaults, autopilot, logging and monitoring ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added configuration for workload certificates and identity service component ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added node pool level network config ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added the option to list supported windows versions ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added the option to specify L4 load balancer configuration and IP v6 configuration ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added update support for node pool labels, taints and network tags ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))


### Bug Fixes

* add 'dict' annotation type to 'request' ([c912605](https://www.github.com/googleapis/python-container/commit/c9126057cde7fc28094785cceab9cf43e42ca8e0))
* deprecated cluster status condition code ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* deprecated KALM addon config option ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* **deps:** require proto-plus 1.15.0 ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))


### Documentation

* clarified SetNodePoolSize API behavior ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))

## [2.7.1](https://www.github.com/googleapis/python-container/compare/v2.7.0...v2.7.1) (2021-07-24)


### Bug Fixes

* enable self signed jwt for grpc ([#133](https://www.github.com/googleapis/python-container/issues/133)) ([6e34b81](https://www.github.com/googleapis/python-container/commit/6e34b81070b14de226c703191e8fe7f37357dea8))

## [2.7.0](https://www.github.com/googleapis/python-container/compare/v2.6.1...v2.7.0) (2021-07-22)


### Features

* add Samples section to CONTRIBUTING.rst ([#129](https://www.github.com/googleapis/python-container/issues/129)) ([a5905b8](https://www.github.com/googleapis/python-container/commit/a5905b820c970217a3ad1604982a7e38412d8dda))

## [2.6.1](https://www.github.com/googleapis/python-container/compare/v2.6.0...v2.6.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#128](https://www.github.com/googleapis/python-container/issues/128)) ([7a8fb93](https://www.github.com/googleapis/python-container/commit/7a8fb93cc083ffbd44b9c321a706ce6f37066ee1))

## [2.6.0](https://www.github.com/googleapis/python-container/compare/v2.5.0...v2.6.0) (2021-07-09)


### Features

* allow updating security group on existing clusters ([#120](https://www.github.com/googleapis/python-container/issues/120)) ([28a3fc9](https://www.github.com/googleapis/python-container/commit/28a3fc94cd7587b5900408bbadf994f143b0d0c3))
* allow updating security group on existing clusters ([#123](https://www.github.com/googleapis/python-container/issues/123)) ([e0d70e9](https://www.github.com/googleapis/python-container/commit/e0d70e98991eec24880497516829a0d4ed1dbc18))

## [2.5.0](https://www.github.com/googleapis/python-container/compare/v2.4.1...v2.5.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#119](https://www.github.com/googleapis/python-container/issues/119)) ([bb598c4](https://www.github.com/googleapis/python-container/commit/bb598c45f5f2c5ca75a638c17168d6a4a15547a4))
* support for NodeAutoprovisioning ImageType ([#107](https://www.github.com/googleapis/python-container/issues/107)) ([d56f699](https://www.github.com/googleapis/python-container/commit/d56f699dad3e7fdf654861e36a007a79df760790))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-container/issues/1127)) ([#112](https://www.github.com/googleapis/python-container/issues/112)) ([5a3941a](https://www.github.com/googleapis/python-container/commit/5a3941a03c48e3cef4d21ac10fc8e7b1b594ad1e)), closes [#1126](https://www.github.com/googleapis/python-container/issues/1126)

## [2.4.1](https://www.github.com/googleapis/python-container/compare/v2.4.0...v2.4.1) (2021-05-16)


### Bug Fixes

* **deps:** add packaging requirement ([#97](https://www.github.com/googleapis/python-container/issues/97)) ([1c46866](https://www.github.com/googleapis/python-container/commit/1c468663bd59bcb529311bd5736861b332a269b3))

## [2.4.0](https://www.github.com/googleapis/python-container/compare/v2.3.1...v2.4.0) (2021-03-24)


### Features

* add `from_service_account_info` ([#66](https://www.github.com/googleapis/python-container/issues/66)) ([f4f154d](https://www.github.com/googleapis/python-container/commit/f4f154db737fed68c49303133f4479199c0fdb12))

## [2.3.1](https://www.github.com/googleapis/python-container/compare/v2.3.0...v2.3.1) (2021-02-18)


### Bug Fixes

* remove client recv msg limit fix: add enums to `types/__init__.py` ([#60](https://www.github.com/googleapis/python-container/issues/60)) ([9207193](https://www.github.com/googleapis/python-container/commit/9207193fbaae7c6d91d87ffb9db57223f02544d6))

## [2.3.0](https://www.github.com/googleapis/python-container/compare/v2.2.0...v2.3.0) (2020-12-08)


### Features

* sync v1beta1 GKE API; deprecate SetLocations and use UpdateCluster; support for sysctls config in Linux nodes; support for node kubelet config controlling CPU manager policy, CFS quota; support for Customer Managed Encryption ([17f0a29](https://www.github.com/googleapis/python-container/commit/17f0a29401ffeaafca6166f9f6169a83c00b145a))


### Bug Fixes

* Update CODEOWNERS ([#59](https://www.github.com/googleapis/python-container/issues/59)) ([0f9a41e](https://www.github.com/googleapis/python-container/commit/0f9a41eb3394d4940941bc38a3e2e5cb3ad6b8dd)), closes [#58](https://www.github.com/googleapis/python-container/issues/58)


### Documentation

* **python:** update intersphinx for grpc and auth ([#53](https://www.github.com/googleapis/python-container/issues/53)) ([6a0fef7](https://www.github.com/googleapis/python-container/commit/6a0fef7f30976357cc9f42c0213931d1a2c76eac))

## [2.2.0](https://www.github.com/googleapis/python-container/compare/v2.1.0...v2.2.0) (2020-11-17)

All changes are from [#51](https://www.github.com/googleapis/python-container/issues/51) / [d3f5465](https://www.github.com/googleapis/python-container/commit/d3f546574300cd18bb0cb1627f226cfe34ee8098)

### Features

* support for GetJSONWebKeys
* support for Workload Identity
* support for Gvisor in nodes
* support for node reservation affinity
* support for Customer Managed Encryption in nodes
* support for NodeLocalDNS
* support for ConfigConnector
* support for private cluster VPC peering
* support for CloudRun load balancers
* support using routes for pod IPs
* support for Shielded Nodes
* support for release channels
* support for disabling default sNAT
* operations now store more granular progress
* support for node Surge Upgrades
* support for updating node pool locations.
* support for Node Auto Provisioning
* support for specifying node disk size and type

 
  
### Bug Fixes
* deprecate SetLocations; use UpdateCluster
* provide name alias for GetOperation (as method signature annotation)
* deprecate basic auth fields (removed in 1.19 clusters)
* deprecate Cluster/NodePool.status_message; use conditions

## [2.1.0](https://www.github.com/googleapis/python-container/compare/v2.0.1...v2.1.0) (2020-09-16)


### Features

* regenerate client lib to pick up new mtls env ([#44](https://www.github.com/googleapis/python-container/issues/44)) ([c4ffea0](https://www.github.com/googleapis/python-container/commit/c4ffea02fbc6c6566a4e772e2b353a5b4dc5b2fc))

## [2.0.1](https://www.github.com/googleapis/python-container/compare/v2.0.0...v2.0.1) (2020-07-24)


### Bug Fixes

* Update README.rst ([#35](https://www.github.com/googleapis/python-container/issues/35)) ([e7d1c66](https://www.github.com/googleapis/python-container/commit/e7d1c66a3f14dc9554a9fbdc78ec16bc912de5f9))


### Documentation

* link to migration guide ([#39](https://www.github.com/googleapis/python-container/issues/39)) ([5341b96](https://www.github.com/googleapis/python-container/commit/5341b96719a82cb8509f4dcc9e66ee05acd95ae9))

## [2.0.0](https://www.github.com/googleapis/python-container/compare/v1.0.1...v2.0.0) (2020-07-16)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#33). See the [migration guide](https://github.com/googleapis/python-container/blob/main/UPGRADING.md).

### Features

* migrate to microgenerator ([#33](https://www.github.com/googleapis/python-container/issues/33)) ([aa9b20c](https://www.github.com/googleapis/python-container/commit/aa9b20c6f4ccb6dff305bfcd72e1bde4a1ee86cd))

## [1.0.1](https://www.github.com/googleapis/python-container/compare/v1.0.0...v1.0.1) (2020-06-16)


### Bug Fixes

* fix `release_status` in `setup.py` ([#27](https://www.github.com/googleapis/python-container/issues/27)) ([d853d99](https://www.github.com/googleapis/python-container/commit/d853d99c73f4716721aa26d96ec6bc1a5c916dc4))

## [1.0.0](https://www.github.com/googleapis/python-container/compare/v0.5.0...v1.0.0) (2020-06-16)


### Features

* release as production/stable ([#24](https://www.github.com/googleapis/python-container/issues/24)) ([0e0095d](https://www.github.com/googleapis/python-container/commit/0e0095d8fad004d8098af62c6c27a40aa96d6257))

## [0.5.0](https://www.github.com/googleapis/python-container/compare/v0.4.0...v0.5.0) (2020-04-14)


### Features

* make `project_id`, `zone`, `cluster_id`, `node_pool` optional arguments to methods in `cluster_manager_client`; change default timeout config; add 2.7 sunset warning; bump copyright year to 2020 (via synth)([#8](https://www.github.com/googleapis/python-container/issues/8)) ([6afc050](https://www.github.com/googleapis/python-container/commit/6afc050f21c57a2d0eda3327c07510f2226aa6a6))

## [0.4.0](https://www.github.com/googleapis/python-container/compare/v0.3.0...v0.4.0) (2020-02-03)


### Features

* **container:** add 'list_usable_subnetworks' method; apply proto annotations (via synth) ([#9741](https://www.github.com/googleapis/python-container/issues/9741)) ([541a9e3](https://www.github.com/googleapis/python-container/commit/541a9e3974c38e2601c17c569099ce8602a1c4be))

## 0.3.0

07-30-2019 10:28 PDT


### Implementation Changes

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8501](https://github.com/googleapis/google-cloud-python/pull/8501))
- Add synth support for v1beta1 API version (via manual synth). ([#8436](https://github.com/googleapis/google-cloud-python/pull/8436))
-  Allow kwargs to be passed to create_channel (via synth).  ([#8384](https://github.com/googleapis/google-cloud-python/pull/8384))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### Documentation
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))

### Internal / Testing Changes
- Pin black version (via synth). ([#8575](https://github.com/googleapis/google-cloud-python/pull/8575))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8347](https://github.com/googleapis/google-cloud-python/pull/8347))
- Add disclaimer to auto-generated template files (via synth).  ([#8309](https://github.com/googleapis/google-cloud-python/pull/8309))
- Update noxfile and setup.py (via synth). ([#8298](https://github.com/googleapis/google-cloud-python/pull/8298))
- Blacken (via synth). ([#8285](https://github.com/googleapis/google-cloud-python/pull/8285))
- Add routing header to method metadata, add nox session `docs` (via synth). ([#7922](https://github.com/googleapis/google-cloud-python/pull/7922))
- Copy proto files alongside protoc versions.
- Minor gapic-generator change. ([#7225](https://github.com/googleapis/google-cloud-python/pull/7225))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers ([#7140](https://github.com/googleapis/google-cloud-python/pull/7140))
- Protoc-generated serialization update. ([#7078](https://github.com/googleapis/google-cloud-python/pull/7078))
- Pick up stub docstring fix in GAPIC generator. ([#6966](https://github.com/googleapis/google-cloud-python/pull/6966))

## 0.2.1

12-17-2018 16:36 PST


### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Improve linkage between container docs pages. ([#6852](https://github.com/googleapis/google-cloud-python/pull/6852))

### Internal / Testing Changes
- Add baseline for synth.metadata

## 0.2.0

12-04-2018 11:28 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core.iam.policy` ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6634](https://github.com/googleapis/google-cloud-python/pull/6634))
- Fix `client_info` bug, update docstrings. ([#6407](https://github.com/googleapis/google-cloud-python/pull/6407))
- Avoid overwriting '__module__' of messages from shared modules. ([#5364](https://github.com/googleapis/google-cloud-python/pull/5364))
- Fix bad trove classifier

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Docs: normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Container: harmonize / DRY 'README.rst' / 'docs/index.rst'. ([#6018](https://github.com/googleapis/google-cloud-python/pull/6018))
- Rename releases to changelog and include from CHANGELOG.md ([#5191](https://github.com/googleapis/google-cloud-python/pull/5191))

### Internal / Testing Changes
- Update noxfile.
- blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local dependencies from coverage. ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Unblack container gapic and protos.
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Pass posargs to py.test ([#6653](https://github.com/googleapis/google-cloud-python/pull/6653))
- Update synth.py yaml location ([#6480](https://github.com/googleapis/google-cloud-python/pull/6480))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Container: add 'synth.py'. ([#6084](https://github.com/googleapis/google-cloud-python/pull/6084))
- Nox: use inplace installs ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))
- Modify system tests to use prerelease versions of grpcio ([#5304](https://github.com/googleapis/google-cloud-python/pull/5304))
- Add Test runs for Python 3.7 and remove 3.4 ([#5295](https://github.com/googleapis/google-cloud-python/pull/5295))

## 0.1.1

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Documentation

- Replacing references to `stable/` docs with `latest/`. (#4638)

### Testing and internal changes

- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)
- nox unittest updates (#4646)

## 0.1.0

[![release level](https://img.shields.io/badge/release%20level-alpha-orange.svg?style&#x3D;flat)](https://cloud.google.com/terms/launch-stages)

Google Kubernetes Engine is a managed environment for deploying containerized
applications. It brings our latest innovations in developer productivity,
resource efficiency, automated operations, and open source flexibility to
accelerate your time to market.

PyPI: https://pypi.org/project/google-cloud-container/0.1.0/
