# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-developerconnect/#history

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.6.0...google-cloud-developerconnect-v0.6.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.5.0...google-cloud-developerconnect-v0.6.0) (2026-06-02)


### Features

* regenerate google-cloud-d packages (#17092) ([d49a2b9412b4ee9105125db36104a3e18344e0ad](https://github.com/googleapis/google-cloud-python/commit/d49a2b9412b4ee9105125db36104a3e18344e0ad))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.4.0...google-cloud-developerconnect-v0.5.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.3.0...google-cloud-developerconnect-v0.4.0) (2026-02-26)


### Documentation

* Updated description for `google.cloud.location.Locations.ListLocations` in YAML ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Corrected typos in comments for `google.cloud.developerconnect.v1.insights.InsightsConfig` and `google.cloud.developerconnect.v1.insights.ArtifactConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Updated comments to include regional secret patterns for SecretManager fields in `GitHubConfig`, `OAuthCredential`, `UserCredential`, `GitLabConfig`, `GitLabEnterpriseConfig`, `BitbucketDataCenterConfig`, and `BitbucketCloudConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Updated comment for `CreateGitRepositoryLink` RPC in `google.cloud.developerconnect.v1.DeveloperConnect` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))


### Features

* Add Secure Source Manager and Generic HTTP Endpoint connection types ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.DeploymentEvent` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.GenericHTTPEndpointConfig` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.FinishOAuthRequest` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.GoogleCloudRun` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new enum value `GEMINI_CODE_ASSIST` is added to enum `google.cloud.developerconnect.v1.GitHubConfig.GitHubApp` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Add HTTP Proxy base URI field ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `projects` is added to message `google.cloud.developerconnect.v1.insights.InsightsConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Add Cloud Run and App Hub Service runtimes to InsightsConfig ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `organization` is added to message `google.cloud.developerconnect.v1.GitHubEnterpriseConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `app_hub_service` is added to message `google.cloud.developerconnect.v1.insights.RuntimeConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.SecureSourceManagerInstanceConfig` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Add Deployment Events to Insights API (GetDeploymentEvent, ListDeploymentEvents) ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `http_proxy_base_uri` is added to message `google.cloud.developerconnect.v1.HTTPProxyConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.GetDeploymentEventRequest` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.FinishOAuthResponse` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Add Gemini Code Assist GitHub App type ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `google_cloud_run` is added to message `google.cloud.developerconnect.v1.insights.RuntimeConfig` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `secure_source_manager_instance_config` is added to message `google.cloud.developerconnect.v1.Connection` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Add Projects field to InsightsConfig for project tracking ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.ListDeploymentEventsRequest` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* Add OAuth flow RPCs (StartOAuth, FinishOAuth) ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.StartOAuthRequest` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.ListDeploymentEventsResponse` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.StartOAuthResponse` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.AppHubService` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.ArtifactDeployment` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new field `http_config` is added to message `google.cloud.developerconnect.v1.Connection` ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))
* A new message `google.cloud.developerconnect.v1.insights.Projects` is added ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.2.0...google-cloud-developerconnect-v0.3.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.10...google-cloud-developerconnect-v0.2.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.1.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.9...google-cloud-developerconnect-v0.1.10) (2025-07-02)


### Features

* a new enum `google.cloud.developerconnect.v1.SystemProvider` is added ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new field `bitbucket_cloud_config` is added to message `google.cloud.developerconnect.v1.Connection` ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new field `bitbucket_data_center_config` is added to message `google.cloud.developerconnect.v1.Connection` ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new field `oauth_start_uri` is added to message `google.cloud.developerconnect.v1.AccountConnector` ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new field `provider_oauth_config` is added to message `google.cloud.developerconnect.v1.AccountConnector` ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new message `google.cloud.developerconnect.v1.AccountConnector` is added ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new message `google.cloud.developerconnect.v1.GitProxyConfig` is added ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* a new message `google.cloud.developerconnect.v1.User` is added ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* add DCI insights config proto ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))


### Documentation

* A comment for field `uid` in message `.google.cloud.developerconnect.v1.Connection` is changed ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))
* A comment for field `uid` in message `.google.cloud.developerconnect.v1.GitRepositoryLink` is changed ([717d9b9](https://github.com/googleapis/google-cloud-python/commit/717d9b9dc6d75727ec235eaf80caa0458a888304))

## [0.1.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.8...google-cloud-developerconnect-v0.1.9) (2025-06-11)


### Documentation

* Update import statement example in README ([3d5bc37](https://github.com/googleapis/google-cloud-python/commit/3d5bc3782da6b37742ae83802de8a8b6db96fe29))

## [0.1.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.7...google-cloud-developerconnect-v0.1.8) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([feb5353](https://github.com/googleapis/google-cloud-python/commit/feb53532240bb70a94b359b519f0f41f95875a33))

## [0.1.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.6...google-cloud-developerconnect-v0.1.7) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))
* Add support for reading selective GAPIC generation methods from service YAML ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))

## [0.1.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.5...google-cloud-developerconnect-v0.1.6) (2024-12-12)


### Features

* Add support for opt-in debug logging ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([819e8fb](https://github.com/googleapis/google-cloud-python/commit/819e8fb3159c39f6c8eb6d7c0b75927134d6ceb2))

## [0.1.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.4...google-cloud-developerconnect-v0.1.5) (2024-11-21)


### Features

* A new field `crypto_key_config` is added to message `.google.cloud.developerconnect.v1.Connection` ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new field `github_enterprise_config` is added to message `.google.cloud.developerconnect.v1.Connection` ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new field `gitlab_config` is added to message `.google.cloud.developerconnect.v1.Connection` ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new field `gitlab_enterprise_config` is added to message `.google.cloud.developerconnect.v1.Connection` ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new field `webhook_id` is added to message `.google.cloud.developerconnect.v1.GitRepositoryLink` ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new message `CryptoKeyConfig` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new message `GitHubEnterpriseConfig` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new message `GitLabConfig` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new message `GitLabEnterpriseConfig` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new message `ServiceDirectoryConfig` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new message `UserCredential` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new resource_definition `[cloudkms.googleapis.com/CryptoKey](https://www.google.com/url?sa=D&q=http%3A%2F%2Fcloudkms.googleapis.com%2FCryptoKey)` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))
* A new resource_definition `[servicedirectory.googleapis.com/Service](https://www.google.com/url?sa=D&q=http%3A%2F%2Fservicedirectory.googleapis.com%2FService)` is added ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))


### Documentation

* A comment for field `requested_cancellation` in message `.google.cloud.developerconnect.v1.OperationMetadata` is changed ([48f25db](https://github.com/googleapis/google-cloud-python/commit/48f25db7772c9d22edac1e743b4eec97929542ec))

## [0.1.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.3...google-cloud-developerconnect-v0.1.4) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([53c951e](https://github.com/googleapis/google-cloud-python/commit/53c951e90ad1d702fa507495532086d5d2f6b3c0))

## [0.1.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.2...google-cloud-developerconnect-v0.1.3) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13202](https://github.com/googleapis/google-cloud-python/issues/13202)) ([5b1f2f3](https://github.com/googleapis/google-cloud-python/commit/5b1f2f3a81ed171b643812e67a7ed179b9b703ea))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.1...google-cloud-developerconnect-v0.1.2) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([ba1064f](https://github.com/googleapis/google-cloud-python/commit/ba1064fd6a63ccbe8a390c0026f32c5772c728a5))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-developerconnect-v0.1.0...google-cloud-developerconnect-v0.1.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12866](https://github.com/googleapis/google-cloud-python/issues/12866)) ([40e1810](https://github.com/googleapis/google-cloud-python/commit/40e18101eaaeefe4baa090c3b4f7a96209ea5735))

## 0.1.0 (2024-06-05)


### Features

* add initial files for google.cloud.developerconnect.v1 ([#12777](https://github.com/googleapis/google-cloud-python/issues/12777)) ([3deb6c7](https://github.com/googleapis/google-cloud-python/commit/3deb6c728455ca41180527b268d2f18445136520))

## Changelog
