# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-network-management/#history

## [1.38.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.37.0...google-cloud-network-management-v1.38.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [1.37.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.36.0...google-cloud-network-management-v1.37.0) (2026-06-25)


### Features

* update googleapis and regenerate ([#17554](https://github.com/googleapis/google-cloud-python/issues/17554)) ([03d0574](https://github.com/googleapis/google-cloud-python/commit/03d0574da8485e918f16e90666928f5c7b7f1c92))

## [1.36.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.35.0...google-cloud-network-management-v1.36.0) (2026-06-22)


### Features

* regenerate google-cloud-[k-n] packages ([#17074](https://github.com/googleapis/google-cloud-python/issues/17074)) ([ec54f78](https://github.com/googleapis/google-cloud-python/commit/ec54f78e37bb3b48e0794d544784b99fa13d6f85))

## [1.35.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.34.0...google-cloud-network-management-v1.35.0) (2026-05-06)

## [1.34.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.33.0...google-cloud-network-management-v1.34.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.33.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.32.0...google-cloud-network-management-v1.33.0) (2026-03-05)


### Features

* Add API fields related to GKE Pods and Network Policies ([6120fb0db084f5e8d1502fb1bb37594ac9976f6e](https://github.com/googleapis/google-cloud-python/commit/6120fb0db084f5e8d1502fb1bb37594ac9976f6e))

## [1.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.31.0...google-cloud-network-management-v1.32.0) (2026-01-29)


### Features

* add fields and messages for GKE Pods and IP masquerading ([38754bbd8765298482b679b027e9bc0ac5a66bb3](https://github.com/googleapis/google-cloud-python/commit/38754bbd8765298482b679b027e9bc0ac5a66bb3))

## [1.31.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.30.0...google-cloud-network-management-v1.31.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.29.0...google-cloud-network-management-v1.30.0) (2025-11-06)


### Documentation

* Various documentation and comment improvements, Enable organization-level support for VPC Flow Logs  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))


### Features

* add enum `Status` to message `InstanceInfo`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add http additional_bindings  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add enum values `NO_ROUTE_FROM_EXTERNAL_IPV6_SOURCE_TO_PRIVATE_IPV6_ADDRESS`, `TRAFFIC_FROM_HYBRID_ENDPOINT_TO_INTERNET_DISALLOWED`, `NO_MATCHING_NAT64_GATEWAY`, `LOAD_BALANCER_BACKEND_IP_VERSION_MISMATCH`, and `NO_KNOWN_ROUTE_FROM_NCC_NETWORK_TO_DESTINATION` to `DropInfo.Cause`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* Enable organization-level support for VPC Flow Logs  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add field `running` to message `InstanceInfo`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add field `google_service_type` to message `DeliverInfo`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add enum `VpcFlowLogsConfig.TargetResourceState`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add enum value `AbortInfo.Cause.GOOGLE_MANAGED_SERVICE_AMBIGUOUS_ENDPOINT`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add enum `VpcFlowLogsConfig.CrossProjectMetadata`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add enum value `RouteInfo.NextHopType.SECURE_WEB_PROXY_GATEWAY`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add message `Endpoint.SingleEdgeResponse`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add enum `DeliverInfo.GoogleServiceType`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add rpc `VpcFlowLogsService.QueryOrgVpcFlowLogsConfigs`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add field `policy_priority` to message `NetworkInfo`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add fields `cross_project_metadata`, `target_resource_state`, `network`, and `subnet` to message `VpcFlowLogsConfig`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add service `OrganizationVpcFlowLogsService`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))
* add field `service_uri` to message `Endpoint.CloudRunRevisionEndpoint`  ([735dcad100d7957ba5373a654b9a2d7c2a277903](https://github.com/googleapis/google-cloud-python/commit/735dcad100d7957ba5373a654b9a2d7c2a277903))

## [1.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.28.0...google-cloud-network-management-v1.29.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.27.0...google-cloud-network-management-v1.28.0) (2025-08-10)


### Features

* [google-cloud-network-management] add `service_uri` field to CloudRunRevisionEndpoint ([#14210](https://github.com/googleapis/google-cloud-python/issues/14210)) ([c86a9cd](https://github.com/googleapis/google-cloud-python/commit/c86a9cd33d9b80bccfed552b4eecc4babee0c094))

## [1.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.26.1...google-cloud-network-management-v1.27.0) (2025-07-10)


### Features

* add enum DeliverInfo.GoogleServiceType ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add enum Status to message InstanceInfo ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add enum value AbortInfo.Cause.GOOGLE_MANAGED_SERVICE_AMBIGUOUS_ENDPOINT ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add enum value RouteInfo.NextHopType.SECURE_WEB_PROXY_GATEWAY ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add enum values NO_ROUTE_FROM_EXTERNAL_IPV6_SOURCE_TO_PRIVATE_IPV6_ADDRESS, TRAFFIC_FROM_HYBRID_ENDPOINT_TO_INTERNET_DISALLOWED, NO_MATCHING_NAT64_GATEWAY, LOAD_BALANCER_BACKEND_IP_VERSION_MISMATCH, and NO_KNOWN_ROUTE_FROM_NCC_NETWORK_TO_DESTINATION to DropInfo.Cause ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add enum VpcFlowLogsConfig.CrossProjectMetadata ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add enum VpcFlowLogsConfig.TargetResourceState ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add field google_service_type to message DeliverInfo ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add field policy_priority to message NetworkInfo ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add field running to message InstanceInfo ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add field service_uri to message Endpoint.CloudRunRevisionEndpoint ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add fields cross_project_metadata, target_resource_state, network, and subnet to message VpcFlowLogsConfig ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add http additional_bindings ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add message Endpoint.SingleEdgeResponse ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add rpc VpcFlowLogsService.QueryOrgVpcFlowLogsConfigs ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* add service OrganizationVpcFlowLogsService ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))
* Enable organization-level support for VPC Flow Logs ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))


### Documentation

* Various documentation and comment improvements, Enable organization-level support for VPC Flow Logs ([dc99ea0](https://github.com/googleapis/google-cloud-python/commit/dc99ea08c7928c32296a53f25e98c4ae0b16486d))

## [1.26.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.26.0...google-cloud-network-management-v1.26.1) (2025-06-11)


### Documentation

* Update import statement example in README ([868b006](https://github.com/googleapis/google-cloud-python/commit/868b0069baf1a4bf6705986e0b6885419b35cdcc))

## [1.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.25.3...google-cloud-network-management-v1.26.0) (2025-04-12)


### Features

* add enum types related to Abort ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))
* add enum types related to Drop ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))
* add enum types related to Firewall ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))
* add enum types related to Google Service ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))
* add messages and fields related to Direct VPC Egress ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))
* add messages and fields related to Route ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))
* add messages and fields related to Serverless External ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))


### Documentation

* update outdated comments ([35034e1](https://github.com/googleapis/google-cloud-python/commit/35034e1ec48b830622be4c7c327fd6813288510a))

## [1.25.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.25.2...google-cloud-network-management-v1.25.3) (2025-03-19)


### Documentation

* [google-cloud-network-management] Update comments for Connectivity Test ([#13669](https://github.com/googleapis/google-cloud-python/issues/13669)) ([9321997](https://github.com/googleapis/google-cloud-python/commit/932199775d19958b932b39b0178caaa5c83ad2ee))

## [1.25.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.25.1...google-cloud-network-management-v1.25.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([c8bbf32](https://github.com/googleapis/google-cloud-python/commit/c8bbf32606e790b559b261bf96700c76b6e2bfce))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [1.25.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.25.0...google-cloud-network-management-v1.25.1) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([770cf0f](https://github.com/googleapis/google-cloud-python/commit/770cf0f31125586a8622e9639f6d24c1bafa9b31))

## [1.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.24.0...google-cloud-network-management-v1.25.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([a0910dd](https://github.com/googleapis/google-cloud-python/commit/a0910dd51541d238bc5fcf10159066ddfd928579))
* Add support for reading selective GAPIC generation methods from service YAML ([a0910dd](https://github.com/googleapis/google-cloud-python/commit/a0910dd51541d238bc5fcf10159066ddfd928579))

## [1.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.23.0...google-cloud-network-management-v1.24.0) (2025-01-13)


### Features

* [google-cloud-network-management] expose the new v1 vpcflowlogs api proto ([#13432](https://github.com/googleapis/google-cloud-python/issues/13432)) ([aaea7ae](https://github.com/googleapis/google-cloud-python/commit/aaea7aed76e25020cc085be8f3dbc0f3642d6912))

## [1.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.22.0...google-cloud-network-management-v1.23.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([feb5c03](https://github.com/googleapis/google-cloud-python/commit/feb5c0348d0efbe5d3c01d5470f2daaef5302842))

## [1.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.21.0...google-cloud-network-management-v1.22.0) (2024-11-14)


### Features

* [google-cloud-network-management] add round-trip mode ([cef77c3](https://github.com/googleapis/google-cloud-python/commit/cef77c3870029a75b1196ca32ebf08d75f962093))
* [google-cloud-network-management] add round-trip mode ([#13280](https://github.com/googleapis/google-cloud-python/issues/13280)) ([cef77c3](https://github.com/googleapis/google-cloud-python/commit/cef77c3870029a75b1196ca32ebf08d75f962093))

## [1.21.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.20.0...google-cloud-network-management-v1.21.0) (2024-11-11)


### Features

* add DNS endpoint of Google Kubernetes Engine cluster control plane ([826abc1](https://github.com/googleapis/google-cloud-python/commit/826abc1a079e84535922b796646da936a1aa4fed))
* add more detailed drop causes to corresponding enum ([826abc1](https://github.com/googleapis/google-cloud-python/commit/826abc1a079e84535922b796646da936a1aa4fed))


### Bug Fixes

* disable universe-domain validation ([#13244](https://github.com/googleapis/google-cloud-python/issues/13244)) ([ae1f471](https://github.com/googleapis/google-cloud-python/commit/ae1f47175bf3354f78cb558a844a9cab00317b95))


### Documentation

* update outdated comments ([826abc1](https://github.com/googleapis/google-cloud-python/commit/826abc1a079e84535922b796646da936a1aa4fed))

## [1.20.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.19.0...google-cloud-network-management-v1.20.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13208](https://github.com/googleapis/google-cloud-python/issues/13208)) ([a019409](https://github.com/googleapis/google-cloud-python/commit/a019409a5b5a983402301f1ac175d8b7e45c3818))

## [1.19.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.18.0...google-cloud-network-management-v1.19.0) (2024-10-23)


### Features

* add fields related to advertised routes to the RouteInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add firewall policy URI to the FirewallInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add load balancer name to the ForwardingRuleInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add messages and fields related to Redis Clusters ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add messages and fields related to Redis Instances ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add more detailed abort and drop causes to corresponding enums ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add PSC network attachment URI to the InstanceInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add PSC target fields to the ForwardingRuleInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add region name field to the RouteInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add region name to the ForwardingRuleInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))
* add subnet URI and region name to the NetworkInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))


### Documentation

* update outdated comments in the FirewallInfo proto ([046e080](https://github.com/googleapis/google-cloud-python/commit/046e080dc9a580c0b700708fde0145527dc5227a))

## [1.18.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.17.3...google-cloud-network-management-v1.18.0) (2024-08-08)


### Features

* expose the new vpcflowlogs api proto ([9cda0c1](https://github.com/googleapis/google-cloud-python/commit/9cda0c1985d0dfa1204c4dae324278b1b4e70693))

## [1.17.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.17.2...google-cloud-network-management-v1.17.3) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([d95af77](https://github.com/googleapis/google-cloud-python/commit/d95af77248f0935a5fe3dba1fccc75124c8b1451))

## [1.17.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.17.1...google-cloud-network-management-v1.17.2) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12868](https://github.com/googleapis/google-cloud-python/issues/12868)) ([0e39c1a](https://github.com/googleapis/google-cloud-python/commit/0e39c1a0ab46757bcf80a178d9bd422f6dcb24c6))

## [1.17.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.17.0...google-cloud-network-management-v1.17.1) (2024-03-28)


### Documentation

* [google-cloud-network-management] update possible firewall rule actions comment ([#12525](https://github.com/googleapis/google-cloud-python/issues/12525)) ([98814f7](https://github.com/googleapis/google-cloud-python/commit/98814f7a212947b8bb07a2bb38a67bad0c1fa4ea))

## [1.17.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.16.0...google-cloud-network-management-v1.17.0) (2024-03-27)


### Features

* [google-cloud-network-management] add an "unsupported" type of firewall policy rule ([#12520](https://github.com/googleapis/google-cloud-python/issues/12520)) ([6f64689](https://github.com/googleapis/google-cloud-python/commit/6f6468920d8e1e0933f97f6a91896cd8021295a1))

## [1.16.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.15.1...google-cloud-network-management-v1.16.0) (2024-03-25)


### Features

* [google-cloud-network-management] add new fields and enum values related to round-trip ([#12504](https://github.com/googleapis/google-cloud-python/issues/12504)) ([1eaecfd](https://github.com/googleapis/google-cloud-python/commit/1eaecfde2b29b350c805ed1a47c2c29785bc3d6e))

## [1.15.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.15.0...google-cloud-network-management-v1.15.1) (2024-03-25)


### Documentation

* deprecate legacy fields related to load balancing ([f21d210](https://github.com/googleapis/google-cloud-python/commit/f21d210630716cecc17ac96584a89dd7f6c402a9))
* update comments for fields related to load balancing ([f21d210](https://github.com/googleapis/google-cloud-python/commit/f21d210630716cecc17ac96584a89dd7f6c402a9))

## [1.15.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.14.0...google-cloud-network-management-v1.15.0) (2024-03-22)


### Features

* [google-cloud-network-management] add new enum values related to Google services ([#12478](https://github.com/googleapis/google-cloud-python/issues/12478)) ([8cd9d87](https://github.com/googleapis/google-cloud-python/commit/8cd9d8743b8c58290ed5418f347ffb19a17348fd))
* add new final state fields to Network Management API version v1 ([af6ce5d](https://github.com/googleapis/google-cloud-python/commit/af6ce5d618b8bd4edb6200f9cbaab90c9da727e4))


### Documentation

* update final state comments in Network Management API version v1 ([af6ce5d](https://github.com/googleapis/google-cloud-python/commit/af6ce5d618b8bd4edb6200f9cbaab90c9da727e4))

## [1.14.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.13.3...google-cloud-network-management-v1.14.0) (2024-03-11)


### Features

* Add new load balancer fields to public API ([f40217d](https://github.com/googleapis/google-cloud-python/commit/f40217da28be7729ae1c8a2a3378be267eb401d1))
* Add new NAT fields to Network Management API definition ([f40217d](https://github.com/googleapis/google-cloud-python/commit/f40217da28be7729ae1c8a2a3378be267eb401d1))

## [1.13.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.13.2...google-cloud-network-management-v1.13.3) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12385](https://github.com/googleapis/google-cloud-python/issues/12385)) ([d50f4d0](https://github.com/googleapis/google-cloud-python/commit/d50f4d042774e2f12e9fe03459eae9ce91247df3))

## [1.13.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.13.1...google-cloud-network-management-v1.13.2) (2024-02-22)


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12308](https://github.com/googleapis/google-cloud-python/issues/12308)) ([74dabeb](https://github.com/googleapis/google-cloud-python/commit/74dabebab206189e649ff6e00f3c7809d96c043b))
* fix ValueError in test__validate_universe_domain ([7c2f2c2](https://github.com/googleapis/google-cloud-python/commit/7c2f2c29d74c9584efc42ddfe8bc098a594391a2))

## [1.13.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.13.0...google-cloud-network-management-v1.13.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([e75fcf6](https://github.com/googleapis/google-cloud-python/commit/e75fcf6e389fd2e90ec00b87a625b208837c72dc))

## [1.13.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.12.0...google-cloud-network-management-v1.13.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12241](https://github.com/googleapis/google-cloud-python/issues/12241)) ([aae72f5](https://github.com/googleapis/google-cloud-python/commit/aae72f5e6c7d48e777fdf68d1012b2b51b912bad))

## [1.12.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.11.1...google-cloud-network-management-v1.12.0) (2023-12-07)


### Features

* Add support for python 3.12 ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))
* Introduce compatibility with native namespace packages ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))
* Use `retry_async` instead of `retry` in async client ([f46b37f](https://github.com/googleapis/google-cloud-python/commit/f46b37f825f96add7b127282414346c1a1a96231))

## [1.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.11.0...google-cloud-network-management-v1.11.1) (2023-09-19)


### Documentation

* Minor formatting ([1ae610b](https://github.com/googleapis/google-cloud-python/commit/1ae610bb3b321ceac7bd23a455a002e39645d84f))

## [1.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.10.0...google-cloud-network-management-v1.11.0) (2023-08-11)


### Features

* Add fields related to Google services ([8df7fab](https://github.com/googleapis/google-cloud-python/commit/8df7fab9c771ef9c3a4bb22cb7d1057a4c1e9fd8))
* Add new enum values for network firewall policies ([8df7fab](https://github.com/googleapis/google-cloud-python/commit/8df7fab9c771ef9c3a4bb22cb7d1057a4c1e9fd8))

## [1.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.9.1...google-cloud-network-management-v1.10.0) (2023-08-10)


### Features

* add dynamic probing fields to v1 API ([62c903e](https://github.com/googleapis/google-cloud-python/commit/62c903e9688e1ade0a9aff94676e52f186f8577e))
* add fields related to load balancers to API ([62c903e](https://github.com/googleapis/google-cloud-python/commit/62c903e9688e1ade0a9aff94676e52f186f8577e))
* add fields related to PBR and NCC routes to API ([#11561](https://github.com/googleapis/google-cloud-python/issues/11561)) ([f794fe7](https://github.com/googleapis/google-cloud-python/commit/f794fe7585224ec167605aefd585bdfeaebecf03))
* add new abort and drop causes to API ([62c903e](https://github.com/googleapis/google-cloud-python/commit/62c903e9688e1ade0a9aff94676e52f186f8577e))

## [1.9.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.9.0...google-cloud-network-management-v1.9.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11448](https://github.com/googleapis/google-cloud-python/issues/11448)) ([4d2c35a](https://github.com/googleapis/google-cloud-python/commit/4d2c35a1cd0b68b6d481d5611ff820451273e859))

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-network-management-v1.8.2...google-cloud-network-management-v1.9.0) (2023-06-29)


### Features

* add forwarding_rule field to Connectivity Test Endpoint proto ([#11430](https://github.com/googleapis/google-cloud-python/issues/11430)) ([312f3e7](https://github.com/googleapis/google-cloud-python/commit/312f3e7c5b2f042a68befde80e52cf7ec4f8e182))

## [1.8.2](https://github.com/googleapis/python-network-management/compare/v1.8.1...v1.8.2) (2023-04-18)


### Documentation

* Update comments in Connectivity Test protos ([#182](https://github.com/googleapis/python-network-management/issues/182)) ([f570808](https://github.com/googleapis/python-network-management/commit/f570808c03887e60e07064cf7acc482bd73d40ba))

## [1.8.1](https://github.com/googleapis/python-network-management/compare/v1.8.0...v1.8.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#180](https://github.com/googleapis/python-network-management/issues/180)) ([e4ff785](https://github.com/googleapis/python-network-management/commit/e4ff785a5d882c016edb7ddf421cd9bd8916c1e1))

## [1.8.0](https://github.com/googleapis/python-network-management/compare/v1.7.1...v1.8.0) (2023-02-17)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#173](https://github.com/googleapis/python-network-management/issues/173)) ([db69894](https://github.com/googleapis/python-network-management/commit/db69894712bdc50ec543f7391bf65817e567f7e7))

## [1.7.1](https://github.com/googleapis/python-network-management/compare/v1.7.0...v1.7.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([ba8b58b](https://github.com/googleapis/python-network-management/commit/ba8b58be6dec6e317477bb266ddc07d1b6636a9b))


### Documentation

* Add documentation for enums ([ba8b58b](https://github.com/googleapis/python-network-management/commit/ba8b58be6dec6e317477bb266ddc07d1b6636a9b))

## [1.7.0](https://github.com/googleapis/python-network-management/compare/v1.6.0...v1.7.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#165](https://github.com/googleapis/python-network-management/issues/165)) ([7b5047a](https://github.com/googleapis/python-network-management/commit/7b5047afe91b7ae610982c1256f987a3a0bc2d0e))

## [1.6.0](https://github.com/googleapis/python-network-management/compare/v1.5.4...v1.6.0) (2022-12-14)


### Features

* Add support for `google.cloud.network_management.__version__` ([f2b26b1](https://github.com/googleapis/python-network-management/commit/f2b26b18e6fe1471d767e780e049163067ea9761))
* Add typing to proto.Message based class attributes ([f2b26b1](https://github.com/googleapis/python-network-management/commit/f2b26b18e6fe1471d767e780e049163067ea9761))


### Bug Fixes

* Add dict typing for client_options ([f2b26b1](https://github.com/googleapis/python-network-management/commit/f2b26b18e6fe1471d767e780e049163067ea9761))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([4a96adc](https://github.com/googleapis/python-network-management/commit/4a96adc0e56fcb8c761b8051cd352d1373f59564))
* Drop usage of pkg_resources ([4a96adc](https://github.com/googleapis/python-network-management/commit/4a96adc0e56fcb8c761b8051cd352d1373f59564))
* Fix timeout default values ([4a96adc](https://github.com/googleapis/python-network-management/commit/4a96adc0e56fcb8c761b8051cd352d1373f59564))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([f2b26b1](https://github.com/googleapis/python-network-management/commit/f2b26b18e6fe1471d767e780e049163067ea9761))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([4a96adc](https://github.com/googleapis/python-network-management/commit/4a96adc0e56fcb8c761b8051cd352d1373f59564))

## [1.5.4](https://github.com/googleapis/python-network-management/compare/v1.5.3...v1.5.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#154](https://github.com/googleapis/python-network-management/issues/154)) ([9d9114b](https://github.com/googleapis/python-network-management/commit/9d9114bb712221e88eb9e9e41bf2e7af3e1cb7c2))

## [1.5.3](https://github.com/googleapis/python-network-management/compare/v1.5.2...v1.5.3) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#152](https://github.com/googleapis/python-network-management/issues/152)) ([b54f9dc](https://github.com/googleapis/python-network-management/commit/b54f9dc200c55f9d19447ead06b4f16718533efe))

## [1.5.2](https://github.com/googleapis/python-network-management/compare/v1.5.1...v1.5.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#139](https://github.com/googleapis/python-network-management/issues/139)) ([ac61691](https://github.com/googleapis/python-network-management/commit/ac61691cfd70bd0031aca383b82c20b839c615a3))
* **deps:** require proto-plus >= 1.22.0 ([ac61691](https://github.com/googleapis/python-network-management/commit/ac61691cfd70bd0031aca383b82c20b839c615a3))

## [1.5.1](https://github.com/googleapis/python-network-management/compare/v1.5.0...v1.5.1) (2022-07-13)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#126](https://github.com/googleapis/python-network-management/issues/126)) ([16528e5](https://github.com/googleapis/python-network-management/commit/16528e51ce0997ad258a03f074d0253bcd14d1fe))

## [1.5.0](https://github.com/googleapis/python-network-management/compare/v1.4.0...v1.5.0) (2022-07-12)


### Features

* add new abort cause and new route next hop type ([#124](https://github.com/googleapis/python-network-management/issues/124)) ([d4363e4](https://github.com/googleapis/python-network-management/commit/d4363e46fd8647a7f46fcc8e6981a73273c471ce))

## [1.4.0](https://github.com/googleapis/python-network-management/compare/v1.3.3...v1.4.0) (2022-07-06)


### Features

* add audience parameter ([1c1818b](https://github.com/googleapis/python-network-management/commit/1c1818b9da7593743322889af11aca4a71082bd7))
* introduce a projects_missing_permissions field in the AbortInfo structure ([1c1818b](https://github.com/googleapis/python-network-management/commit/1c1818b9da7593743322889af11aca4a71082bd7))


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#120](https://github.com/googleapis/python-network-management/issues/120)) ([1c1818b](https://github.com/googleapis/python-network-management/commit/1c1818b9da7593743322889af11aca4a71082bd7))
* require python 3.7+ ([#122](https://github.com/googleapis/python-network-management/issues/122)) ([ef51d0b](https://github.com/googleapis/python-network-management/commit/ef51d0b21cc02f28aa4c986d4241a2cd83065309))

## [1.3.3](https://github.com/googleapis/python-network-management/compare/v1.3.2...v1.3.3) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#111](https://github.com/googleapis/python-network-management/issues/111)) ([c56801a](https://github.com/googleapis/python-network-management/commit/c56801a0ff641dbeae24700197f5e132cc301142))


### Documentation

* fix changelog header to consistent size ([#110](https://github.com/googleapis/python-network-management/issues/110)) ([5d19cd5](https://github.com/googleapis/python-network-management/commit/5d19cd58b067c8dee9072d4295736bac14326f99))

## [1.3.2](https://github.com/googleapis/python-network-management/compare/v1.3.1...v1.3.2) (2022-05-05)


### Documentation

* fix type in docstring for map fields ([3c71bcc](https://github.com/googleapis/python-network-management/commit/3c71bcc656d1d8a1a916caf4cf0854db48eb460f))

## [1.3.1](https://github.com/googleapis/python-network-management/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#77](https://github.com/googleapis/python-network-management/issues/77)) ([9fa6b57](https://github.com/googleapis/python-network-management/commit/9fa6b577b09d736917e101f7829bb0c01e4e04e2))

## [1.3.0](https://github.com/googleapis/python-network-management/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#62](https://github.com/googleapis/python-network-management/issues/62)) ([ab2afd2](https://github.com/googleapis/python-network-management/commit/ab2afd27624fd5d8932f74533cb04292f89fe0e0))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([297c119](https://github.com/googleapis/python-network-management/commit/297c119c3317ea766bd52d328a34a9079e874acd))


### Documentation

* add generated snippets ([#68](https://github.com/googleapis/python-network-management/issues/68)) ([190d825](https://github.com/googleapis/python-network-management/commit/190d8257841cb4d2417733f8bba795ff11e635bd))

## [1.2.1](https://www.github.com/googleapis/python-network-management/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([f4ef191](https://www.github.com/googleapis/python-network-management/commit/f4ef191701f0306d32303cde0e48918b14a29682))
* **deps:** require google-api-core >= 1.28.0 ([f4ef191](https://www.github.com/googleapis/python-network-management/commit/f4ef191701f0306d32303cde0e48918b14a29682))


### Documentation

* list oneofs in docstring ([f4ef191](https://www.github.com/googleapis/python-network-management/commit/f4ef191701f0306d32303cde0e48918b14a29682))

## [1.2.0](https://www.github.com/googleapis/python-network-management/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add support for python 3.10 ([#42](https://www.github.com/googleapis/python-network-management/issues/42)) ([fe07ad2](https://www.github.com/googleapis/python-network-management/commit/fe07ad281ffd24c37ab258cfc79cc89dff73f678))

## [1.1.0](https://www.github.com/googleapis/python-network-management/compare/v1.0.2...v1.1.0) (2021-10-07)


### Features

* add context manager support in client ([#38](https://www.github.com/googleapis/python-network-management/issues/38)) ([376873d](https://www.github.com/googleapis/python-network-management/commit/376873d0550999ebf9831509ce77b7b86a689059))

## [1.0.2](https://www.github.com/googleapis/python-network-management/compare/v1.0.1...v1.0.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([fb7e7fd](https://www.github.com/googleapis/python-network-management/commit/fb7e7fd9915d0ee99a4741896bd2a43a57aaba77))

## [1.0.1](https://www.github.com/googleapis/python-network-management/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([ac98d76](https://www.github.com/googleapis/python-network-management/commit/ac98d76745bb737e4862576d9b93bb0accdc3ef4))

## [1.0.0](https://www.github.com/googleapis/python-network-management/compare/v0.1.1...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#16](https://www.github.com/googleapis/python-network-management/issues/16)) ([4c156cf](https://www.github.com/googleapis/python-network-management/commit/4c156cff255b33fe89637d7106a61ea9113cac26))

## [0.1.1](https://www.github.com/googleapis/python-network-management/compare/v0.1.0...v0.1.1) (2021-07-26)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#7](https://www.github.com/googleapis/python-network-management/issues/7)) ([2efa0ec](https://www.github.com/googleapis/python-network-management/commit/2efa0ec8941664873ed46ca40f73286661b401b8))
* enable self signed jwt for grpc ([#13](https://www.github.com/googleapis/python-network-management/issues/13)) ([9ae9673](https://www.github.com/googleapis/python-network-management/commit/9ae9673ae7141aee657e790208d385d430c7c4d6))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#8](https://www.github.com/googleapis/python-network-management/issues/8)) ([44e3740](https://www.github.com/googleapis/python-network-management/commit/44e37406e513730b2a0569a5f78631e5d235da79))


### Miscellaneous Chores

* release 0.1.1 ([#12](https://www.github.com/googleapis/python-network-management/issues/12)) ([800ee67](https://www.github.com/googleapis/python-network-management/commit/800ee67e6279746114f954a6a55d3776656f6265))

## 0.1.0 (2021-07-02)


### Features

* generate v1 ([8dad342](https://www.github.com/googleapis/python-network-management/commit/8dad342c454882da3359e37cb836950ae66cc73f))
