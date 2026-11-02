# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-dataform/#history

## [0.11.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.11.3...google-cloud-dataform-v0.11.4) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))
* update API sources and regenerate ([#18513](https://github.com/googleapis/google-cloud-python/issues/18513)) ([7d7adca](https://github.com/googleapis/google-cloud-python/commit/7d7adcaee688603077ea53abec678130045c20ed))

## [0.11.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.11.2...google-cloud-dataform-v0.11.3) (2026-08-21)


### Features

* update googleapis and regenerate ([#18087](https://github.com/googleapis/google-cloud-python/issues/18087)) ([db1622a](https://github.com/googleapis/google-cloud-python/commit/db1622a9cfac112b40c93842737d7a5deeb3e8bd))
* update sources and regenerate ([#18164](https://github.com/googleapis/google-cloud-python/issues/18164)) ([5ff8274](https://github.com/googleapis/google-cloud-python/commit/5ff8274ac2eb9375e918dff68303d3abdc3e6d6f))

## [0.11.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.11.1...google-cloud-dataform-v0.11.2) (2026-07-07)


### Features

* update googleapis and regenerate ([#17635](https://github.com/googleapis/google-cloud-python/issues/17635)) ([9638879](https://github.com/googleapis/google-cloud-python/commit/96388796440b226440f885c04ce565782b1d9190))

## [0.11.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.11.0...google-cloud-dataform-v0.11.1) (2026-06-25)


### Features

* update googleapis and regenerate ([#17554](https://github.com/googleapis/google-cloud-python/issues/17554)) ([03d0574](https://github.com/googleapis/google-cloud-python/commit/03d0574da8485e918f16e90666928f5c7b7f1c92))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.10.0...google-cloud-dataform-v0.11.0) (2026-06-02)


### Features

* regenerate google-cloud-d packages (#17092) ([d49a2b9412b4ee9105125db36104a3e18344e0ad](https://github.com/googleapis/google-cloud-python/commit/d49a2b9412b4ee9105125db36104a3e18344e0ad))

## [0.10.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.9.0...google-cloud-dataform-v0.10.0) (2026-03-26)


### Documentation

* A comment for field `force` in message `.google.cloud.dataform.v1.DeleteRepositoryRequest` is changed ([397ae5384b5fa2741d0f479ba7efc1612e1195da](https://github.com/googleapis/google-cloud-python/commit/397ae5384b5fa2741d0f479ba7efc1612e1195da))


### Features

* add folders and teamFolders related changes to v1 ([397ae5384b5fa2741d0f479ba7efc1612e1195da](https://github.com/googleapis/google-cloud-python/commit/397ae5384b5fa2741d0f479ba7efc1612e1195da))
* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.8.0...google-cloud-dataform-v0.9.0) (2026-02-12)


### Documentation

* A comment for field `force` in message `.google.cloud.dataform.v1beta1.DeleteRepositoryRequest` is changed PiperOrigin-RevId: 868182714 ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))


### Features

* Update GCP Client Libraries in v1beta1 to support Folders, TeamFolders, and other relevant APIs The v1beta1 API now includes support for Folders and TeamFolders, allowing users to organize repositories and files hierarchically and manage access controls. New Features: - Added TeamFolder resource and methods: CreateTeamFolder, GetTeamFolder, UpdateTeamFolder, DeleteTeamFolder QueryTeamFolderContents to list folder contents. SearchTeamFolders to search for TeamFolders. - Added Folder resource and methods: CreateFolder, GetFolder, UpdateFolder, DeleteFolder QueryFolderContents to list folder contents. Added MoveFolder to move Folders between TeamFolders, other Folders, or the user root folder. - Added MoveRepository to move Repositories between TeamFolders, Folders, or the user root folder. - Added QueryUserRootContents to list contents of a user&#39;s root folder. Repository resource now includes containing_folder and team_folder_name fields to indicate its location within the folder hierarchy. - IAM methods (GetIamPolicy, SetIamPolicy, TestIamPermissions) now support Folder and TeamFolder resources for access control management ([5371e8e931dfba1d504ac2ffbd48a7f4abdcc158](https://github.com/googleapis/google-cloud-python/commit/5371e8e931dfba1d504ac2ffbd48a7f4abdcc158))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.7.0...google-cloud-dataform-v0.8.0) (2026-01-08)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.6.2...google-cloud-dataform-v0.7.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.6.1...google-cloud-dataform-v0.6.2) (2025-05-20)


### Features

* Support adding a workflow action to execute a Data Preparation node ([8f95f78](https://github.com/googleapis/google-cloud-python/commit/8f95f787fa8479cce7e44db97dcf36d39a1fa541))


### Documentation

* Updated the formatting in some comments in multiple services ([8f95f78](https://github.com/googleapis/google-cloud-python/commit/8f95f787fa8479cce7e44db97dcf36d39a1fa541))

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.6.0...google-cloud-dataform-v0.6.1) (2025-03-15)


### Features

* [google-cloud-dataform] Dataform V1 Public APIs ([#13639](https://github.com/googleapis/google-cloud-python/issues/13639)) ([7828c61](https://github.com/googleapis/google-cloud-python/commit/7828c61c6462b2b2397a8849601356b96cf7e6e5))


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([feb5353](https://github.com/googleapis/google-cloud-python/commit/feb53532240bb70a94b359b519f0f41f95875a33))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.16...google-cloud-dataform-v0.6.0) (2025-03-03)


### ⚠ BREAKING CHANGES

* **v1beta1:** Response type of method `CommitRepositoryChanges` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.CommitRepositoryChangesResponse` in service `Dataform`
* **v1beta1:** Response type of method `PullGitCommits` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.PullGitCommitsResponse` in service `Dataform`
* **v1beta1:** Response type of method `PushGitCommits` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.PushGitCommitsResponse` in service `Dataform`
* **v1beta1:** Response type of method `CommitWorkspaceChanges` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.CommitWorkspaceChangesResponse` in service `Dataform`
* **v1beta1:** Response type of method `ResetWorkspaceChanges` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.ResetWorkspaceChangesResponse` in service `Dataform`
* **v1beta1:** Response type of method `RemoveDirectory` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.RemoveDirectoryResponse` in service `Dataform`
* **v1beta1:** Response type of method `RemoveFileRequest` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.RemoveFileResponse` in service `Dataform`
* **v1beta1:** Response type of method `CancelWorkflowInvocation` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.CancelWorkflowInvocationResponse` in service `Dataform`
* **v1beta1:** An existing field `bigquery_action` is moved in to oneof in message `.google.cloud.dataform.v1beta1.WorkflowInvocationAction`

### Features

* **v1beta1:** Added new field `internal_metadata` to all resources to export all the metadata information that is used internally to serve the resource ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Moving existing field `bigquery_action` to oneof in message `.google.cloud.dataform.v1beta1.WorkflowInvocationAction` to allow adding more actions types such as `notebook_action` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Returning `commit_sha` in the response of method `CommitRepositoryChanges` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))


### Bug Fixes

* **v1beta1:** An existing field `bigquery_action` is moved in to oneof in message `.google.cloud.dataform.v1beta1.WorkflowInvocationAction` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `CancelWorkflowInvocation` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.CancelWorkflowInvocationResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `CommitRepositoryChanges` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.CommitRepositoryChangesResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `CommitWorkspaceChanges` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.CommitWorkspaceChangesResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `PullGitCommits` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.PullGitCommitsResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `PushGitCommits` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.PushGitCommitsResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `RemoveDirectory` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.RemoveDirectoryResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `RemoveFileRequest` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.RemoveFileResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Response type of method `ResetWorkspaceChanges` is changed from `.google.protobuf.Empty` to `.google.cloud.dataform.v1beta1.ResetWorkspaceChangesResponse` in service `Dataform` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))


### Documentation

* **v1beta1:** Adds known limitations on several methods such as `UpdateRepository`, `UpdateReleaseConfig` and `UpdateWorkflowConfig` ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** Explained the effect of field `page_token` on the pagination in several messages ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))
* **v1beta1:** several comments reformatted ([4aaf903](https://github.com/googleapis/google-cloud-python/commit/4aaf903957688ffccf272759e24680919115cb30))

## [0.5.16](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.15...google-cloud-dataform-v0.5.16) (2025-02-18)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([16e14c8](https://github.com/googleapis/google-cloud-python/commit/16e14c8d547864360dcab45d90e9e55169204fc6))

## [0.5.15](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.14...google-cloud-dataform-v0.5.15) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))
* Add support for reading selective GAPIC generation methods from service YAML ([e92d527](https://github.com/googleapis/google-cloud-python/commit/e92d52797ffbce45d033eb81af24e0cad32baa55))

## [0.5.14](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.13...google-cloud-dataform-v0.5.14) (2024-12-12)


### Features

* Add support for opt-in debug logging ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([19ed3be](https://github.com/googleapis/google-cloud-python/commit/19ed3bec7fcbc09aa5828180778ffc828d3eafa3))

## [0.5.13](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.12...google-cloud-dataform-v0.5.13) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([53c951e](https://github.com/googleapis/google-cloud-python/commit/53c951e90ad1d702fa507495532086d5d2f6b3c0))

## [0.5.12](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.11...google-cloud-dataform-v0.5.12) (2024-10-24)


### Features

* Add support for  Python 3.13 ([6252476](https://github.com/googleapis/google-cloud-python/commit/6252476e5938352fb2417d098a1edcc08558fe10))

## [0.5.11](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.10...google-cloud-dataform-v0.5.11) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([ba1064f](https://github.com/googleapis/google-cloud-python/commit/ba1064fd6a63ccbe8a390c0026f32c5772c728a5))

## [0.5.10](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.9...google-cloud-dataform-v0.5.10) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12865](https://github.com/googleapis/google-cloud-python/issues/12865)) ([7f9dedb](https://github.com/googleapis/google-cloud-python/commit/7f9dedb3abc7636cbcd97e21ac857844b885b599))

## [0.5.9](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.8...google-cloud-dataform-v0.5.9) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12383](https://github.com/googleapis/google-cloud-python/issues/12383)) ([305f43f](https://github.com/googleapis/google-cloud-python/commit/305f43f7d6293e3316248f421fdc19c5d8405c21))

## [0.5.8](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.7...google-cloud-dataform-v0.5.8) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12282](https://github.com/googleapis/google-cloud-python/issues/12282)) ([b985096](https://github.com/googleapis/google-cloud-python/commit/b985096d43add8214172ff993e00293e6c8757cb))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12305](https://github.com/googleapis/google-cloud-python/issues/12305)) ([2aa7f17](https://github.com/googleapis/google-cloud-python/commit/2aa7f17a5fd4f2249260225db91fb0414d06eaa7))

## [0.5.7](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.6...google-cloud-dataform-v0.5.7) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([f3db074](https://github.com/googleapis/google-cloud-python/commit/f3db074e7bbf505d5989e4c353461ab6bef4905c))

## [0.5.6](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.5...google-cloud-dataform-v0.5.6) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12239](https://github.com/googleapis/google-cloud-python/issues/12239)) ([8004d15](https://github.com/googleapis/google-cloud-python/commit/8004d15d9e6baa4dc5bc3f09d528e176d54d9ec5))

## [0.5.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.4...google-cloud-dataform-v0.5.5) (2023-12-07)


### Features

* Add support for python 3.12 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Introduce compatibility with native namespace packages ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))
* Use `retry_async` instead of `retry` in async client ([b96013d](https://github.com/googleapis/google-cloud-python/commit/b96013d2c31e3602bb885bf8d7296cc49c3a4642))

## [0.5.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.3...google-cloud-dataform-v0.5.4) (2023-11-02)


### Features

* Support custom service account repository configuration ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support for ReleaseConfigs  ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support for WorkflowConfigs ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support labels on repositories ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support new ComputeRepositoryAccessTokenStatus repository method ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support new first-party repository methods for committing, listing/reading files, and fetching history ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support NPMRC environment variables ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support SSH based git authentication configuration ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))
* Support workspace compilation override fields ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))


### Bug Fixes

* rearrange several messages, thus changing field types ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))


### Documentation

* several comments reformatted ([13b57e4](https://github.com/googleapis/google-cloud-python/commit/13b57e4ace8a101f78d8a3043548e3373cfee1d0))

## [0.5.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.2...google-cloud-dataform-v0.5.3) (2023-09-19)


### Documentation

* Minor formatting ([9487380](https://github.com/googleapis/google-cloud-python/commit/94873808ece8059b07644a0a49dedf8e2906900a))

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-dataform-v0.5.1...google-cloud-dataform-v0.5.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11445](https://github.com/googleapis/google-cloud-python/issues/11445)) ([98bddda](https://github.com/googleapis/google-cloud-python/commit/98bdddafc821e2fc6e86a31965da0c46899aa229))

## [0.5.1](https://github.com/googleapis/python-dataform/compare/v0.5.0...v0.5.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#54](https://github.com/googleapis/python-dataform/issues/54)) ([c38ec22](https://github.com/googleapis/python-dataform/commit/c38ec228a071a57e88dcaf2bbf26a8b456f773de))

## [0.5.0](https://github.com/googleapis/python-dataform/compare/v0.4.1...v0.5.0) (2023-02-27)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([#49](https://github.com/googleapis/python-dataform/issues/49)) ([403b246](https://github.com/googleapis/python-dataform/commit/403b2463a9ebeec2e03c9a9a27435c60dceedb41))

## [0.4.1](https://github.com/googleapis/python-dataform/compare/v0.4.0...v0.4.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([c546812](https://github.com/googleapis/python-dataform/commit/c5468129ce7301e1d22943b63b9fd3eb22682cd0))


### Documentation

* Add documentation for enums ([c546812](https://github.com/googleapis/python-dataform/commit/c5468129ce7301e1d22943b63b9fd3eb22682cd0))

## [0.4.0](https://github.com/googleapis/python-dataform/compare/v0.3.0...v0.4.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#40](https://github.com/googleapis/python-dataform/issues/40)) ([b8f6d78](https://github.com/googleapis/python-dataform/commit/b8f6d78e001cbc6a7110927cd6f711c712fc077e))

## [0.3.0](https://github.com/googleapis/python-dataform/compare/v0.2.3...v0.3.0) (2022-12-15)


### Features

* Add support for `google.cloud.dataform.__version__` ([fef5a2c](https://github.com/googleapis/python-dataform/commit/fef5a2c846e006a67d8cb83406fe6b80947e0901))
* Add typing to proto.Message based class attributes ([fef5a2c](https://github.com/googleapis/python-dataform/commit/fef5a2c846e006a67d8cb83406fe6b80947e0901))


### Bug Fixes

* Add dict typing for client_options ([fef5a2c](https://github.com/googleapis/python-dataform/commit/fef5a2c846e006a67d8cb83406fe6b80947e0901))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([b64c01a](https://github.com/googleapis/python-dataform/commit/b64c01acf35824f9d61ebd833c77829fb52d0b90))
* Drop usage of pkg_resources ([b64c01a](https://github.com/googleapis/python-dataform/commit/b64c01acf35824f9d61ebd833c77829fb52d0b90))
* Fix timeout default values ([b64c01a](https://github.com/googleapis/python-dataform/commit/b64c01acf35824f9d61ebd833c77829fb52d0b90))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([fef5a2c](https://github.com/googleapis/python-dataform/commit/fef5a2c846e006a67d8cb83406fe6b80947e0901))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([b64c01a](https://github.com/googleapis/python-dataform/commit/b64c01acf35824f9d61ebd833c77829fb52d0b90))

## [0.2.3](https://github.com/googleapis/python-dataform/compare/v0.2.2...v0.2.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#30](https://github.com/googleapis/python-dataform/issues/30)) ([b070f6e](https://github.com/googleapis/python-dataform/commit/b070f6e53daea5213a4ca5de90f7bf6cb6aa2a39))

## [0.2.2](https://github.com/googleapis/python-dataform/compare/v0.2.1...v0.2.2) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#28](https://github.com/googleapis/python-dataform/issues/28)) ([fb846e5](https://github.com/googleapis/python-dataform/commit/fb846e5bb9ab2299a07f93f38df6eb20fae0ac40))

## [0.2.1](https://github.com/googleapis/python-dataform/compare/v0.2.0...v0.2.1) (2022-08-15)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#12](https://github.com/googleapis/python-dataform/issues/12)) ([ddde619](https://github.com/googleapis/python-dataform/commit/ddde61929b91d52f5a82191702583234394263e4))
* **deps:** require proto-plus >= 1.22.0 ([ddde619](https://github.com/googleapis/python-dataform/commit/ddde61929b91d52f5a82191702583234394263e4))

## [0.2.0](https://github.com/googleapis/python-dataform/compare/v0.1.0...v0.2.0) (2022-07-26)


### Features

* generate v1beta1 ([63b545e](https://github.com/googleapis/python-dataform/commit/63b545e7d5dd45ae26f6d566025e03a6757e8805))


### Bug Fixes

* remove v1alpha2 ([63b545e](https://github.com/googleapis/python-dataform/commit/63b545e7d5dd45ae26f6d566025e03a6757e8805))

## 0.1.0 (2022-07-08)


### Features

* generate v1alpha2 ([bb0d40d](https://github.com/googleapis/python-dataform/commit/bb0d40d43efd4b9c546dbe7de4fa0374cdc0cff3))
