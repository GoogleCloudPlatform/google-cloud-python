# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/gapic-generator/#history

## [1.44.1](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.44.0...gapic-generator-v1.44.1) (2026-10-29)


### Bug Fixes

* **google-api-core:** align HTTP T3 and T4 OpenTelemetry span status and attributes ([#18868](https://github.com/googleapis/google-cloud-python/issues/18868)) ([deb2194](https://github.com/googleapis/google-cloud-python/commit/deb2194d3fd615e2054b165a2493cc9ddb36ee9b))
* **google-api-core:** align OpenTelemetry span names, kinds, and T3 endpoint attributes with spec ([#18866](https://github.com/googleapis/google-cloud-python/issues/18866)) ([2a10196](https://github.com/googleapis/google-cloud-python/commit/2a1019643da54baae33e1737ee1506de178aa857))

## [1.44.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.43.1...gapic-generator-v1.44.0) (2026-10-22)


### Features

* **observability:** suppress redundant gRPC auto-instrumentation spans ([#18592](https://github.com/googleapis/google-cloud-python/issues/18592)) ([a597007](https://github.com/googleapis/google-cloud-python/commit/a5970072a0218060bc34857797c3008e0f30becf))

## [1.43.1](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.43.0...gapic-generator-v1.43.1) (2026-10-15)


### Bug Fixes

* **gapic-generator:** do not emit empty routing metadata on client-streaming RPCs ([#18591](https://github.com/googleapis/google-cloud-python/issues/18591)) ([bbdd643](https://github.com/googleapis/google-cloud-python/commit/bbdd643b91665b749da3fe3d5b39d2450caec2c2))
* **gapic-generator:** resolve showcase-mypy incompatible redefinition ([7032a89](https://github.com/googleapis/google-cloud-python/commit/7032a895a891172b01844b805ac4fe4bd9ffa424))
* **gapic-generator:** resolve showcase-mypy incompatible redefinition and add canary CI job ([#18701](https://github.com/googleapis/google-cloud-python/issues/18701)) ([7032a89](https://github.com/googleapis/google-cloud-python/commit/7032a895a891172b01844b805ac4fe4bd9ffa424))

## [1.43.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.42.0...gapic-generator-v1.43.0) (2026-10-08)


### Features

* **gapic-generator:** generate code samples for resumable upload RPCs ([#18501](https://github.com/googleapis/google-cloud-python/issues/18501)) ([c8926ab](https://github.com/googleapis/google-cloud-python/commit/c8926ab89d240239fee0c82be2373c752d3507c0))
* generate client, transport, and unit test templates for resumable uploads ([#18495](https://github.com/googleapis/google-cloud-python/issues/18495)) ([3f8d00b](https://github.com/googleapis/google-cloud-python/commit/3f8d00bf5d95337a97268bcbdd7ef1ee155f7516))
* **observability:** implement universal 4-path OpenTelemetry tracing ([#18433](https://github.com/googleapis/google-cloud-python/issues/18433)) ([7d18b25](https://github.com/googleapis/google-cloud-python/commit/7d18b2575c5170518df0ba0e425d87a41f0eba56))

## [1.42.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.41.0...gapic-generator-v1.42.0) (2026-10-01)


### Features

* **gapic-generator:** add rpc_name metadata to mixin schema definitions ([#18516](https://github.com/googleapis/google-cloud-python/issues/18516)) ([fc1b469](https://github.com/googleapis/google-cloud-python/commit/fc1b469837256a7a3b59d1b8b0ed1ffe078aab3b))

## [1.41.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.40.0...gapic-generator-v1.41.0) (2026-09-29)


### Features

* **gapic-generator:** add schema support for resumable uploads ([#18480](https://github.com/googleapis/google-cloud-python/issues/18480)) ([78ff458](https://github.com/googleapis/google-cloud-python/commit/78ff458d055a6104a385dc96990773f02a138f7d))


### Bug Fixes

* **gapic-generator:** init mock response in version header test ([#18488](https://github.com/googleapis/google-cloud-python/issues/18488)) ([7871fa9](https://github.com/googleapis/google-cloud-python/commit/7871fa9d142807248e225cb9d24d2ffda88e1b90))

## [1.40.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.39.0...gapic-generator-v1.40.0) (2026-09-24)


### Features

* add 3.15 support to gapic library classifiers ([#18450](https://github.com/googleapis/google-cloud-python/issues/18450)) ([5fe1ef3](https://github.com/googleapis/google-cloud-python/commit/5fe1ef3b5f11155a7768660a39c3a8e964d9d652))


### Bug Fixes

* **bazel:** allow CustomProtoInfo in gapic_compat_proto_library ([#18417](https://github.com/googleapis/google-cloud-python/issues/18417)) ([11bdf92](https://github.com/googleapis/google-cloud-python/commit/11bdf928710031cd3dd279215d1be2bd7d73e18f))

## [1.39.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.38.0...gapic-generator-v1.39.0) (2026-08-21)


### Features

* **generator:** add fallback compatibility imports for google-api-core helpers ([#17999](https://github.com/googleapis/google-cloud-python/issues/17999)) ([9c13ae2](https://github.com/googleapis/google-cloud-python/commit/9c13ae2476e8ea7a5f3197ed5d094d3b1d5686a9))


### Bug Fixes

* **generator:** check for api_version header in metadata list ([#18015](https://github.com/googleapis/google-cloud-python/issues/18015)) ([0e63510](https://github.com/googleapis/google-cloud-python/commit/0e63510c3b03c14bb1f8dd473dbcdfb719a7050d))
* **generator:** move version checks after __all__ in __init__.py temlate ([#18100](https://github.com/googleapis/google-cloud-python/issues/18100)) ([d0efb4d](https://github.com/googleapis/google-cloud-python/commit/d0efb4dd19aa21c779b20cae02d135fad9ca997e))
* **generator:** switch core_deps_from_source to DEFAULT_PYTHON_VERSION ([#18050](https://github.com/googleapis/google-cloud-python/issues/18050)) ([895ffa2](https://github.com/googleapis/google-cloud-python/commit/895ffa29ba72f2a6e520c6d0fdf26ac9e36f8269))


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [1.38.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.37.1...gapic-generator-v1.38.0) (2026-08-06)


### Features

* **generator:** delegate REST transcoding to google-api-core ([#17766](https://github.com/googleapis/google-cloud-python/issues/17766)) ([7b05aab](https://github.com/googleapis/google-cloud-python/commit/7b05aabf2daf10c51d3ce34d6e10a5f4b4290216))
* **generator:** gapic generator centralization routing ([#17816](https://github.com/googleapis/google-cloud-python/issues/17816)) ([32a2442](https://github.com/googleapis/google-cloud-python/commit/32a2442e73c9ec1576ca92f53469c4acb8226dba))


### Bug Fixes

* add typing for header_params ([#17914](https://github.com/googleapis/google-cloud-python/issues/17914)) ([9e98b93](https://github.com/googleapis/google-cloud-python/commit/9e98b93e89c26dfca7ca4980b2da8ff3d2303771))
* **api-core:** use truthiness check in setup_request_id to support proto-plus messages ([#18000](https://github.com/googleapis/google-cloud-python/issues/18000)) ([ad8f93c](https://github.com/googleapis/google-cloud-python/commit/ad8f93c3211b3ae9d9b234a5b2fa52a8cbf4b206))
* avoid retaining routing parameter instances in cache ([#17961](https://github.com/googleapis/google-cloud-python/issues/17961)) ([f64ada2](https://github.com/googleapis/google-cloud-python/commit/f64ada29ff596202a5625f71516f0215e45aa8ae))
* bump aiohttp from 3.13.5 to 3.14.3 in /packages/gapic-generator ([#17990](https://github.com/googleapis/google-cloud-python/issues/17990)) ([6ff5815](https://github.com/googleapis/google-cloud-python/commit/6ff5815f20cc49eddeceaa8c89ac53c26b9b43fb))
* bump cryptography from 48.0.1 to 50.0.0 in /packages/gapic-generator ([#17991](https://github.com/googleapis/google-cloud-python/issues/17991)) ([d607f25](https://github.com/googleapis/google-cloud-python/commit/d607f25aa7c0db23beff3e43430033b22e860e18))
* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* **generator:** use flat_ref_types in test templates and delete remove-unused-imports ([#17900](https://github.com/googleapis/google-cloud-python/issues/17900)) ([395f764](https://github.com/googleapis/google-cloud-python/commit/395f764737bd976593b9b034130012522c44344c))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))
* resolve collision with reserved words in samples ([#17912](https://github.com/googleapis/google-cloud-python/issues/17912)) ([588cda9](https://github.com/googleapis/google-cloud-python/commit/588cda95202e094511f39f244aa6acea654a7af6))
* upgrade Protobuf and gRPC in WORKSPACE ([#17882](https://github.com/googleapis/google-cloud-python/issues/17882)) ([5b5ece5](https://github.com/googleapis/google-cloud-python/commit/5b5ece55d1b2a427ccc2b461442a4e7751b33919))

## [1.37.1](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.37.0...gapic-generator-v1.37.1) (2026-07-22)


### Bug Fixes

* **gapic-generator:** remove lagging 3.9 refs ([#16924](https://github.com/googleapis/google-cloud-python/issues/16924)) ([a719055](https://github.com/googleapis/google-cloud-python/commit/a7190556f487028f04e42ade1f922075127028c3))
* **gapic:** mock os.path.exists in mTLS tests to support newer google auth ([#17807](https://github.com/googleapis/google-cloud-python/issues/17807)) ([df0541a](https://github.com/googleapis/google-cloud-python/commit/df0541abf6aae710fc3e6644a5d8f3f706d29c5a))

## [1.37.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.36.0...gapic-generator-v1.37.0) (2026-07-07)


### Features

* implement native PEP 0810 lazy loading ([#17591](https://github.com/googleapis/google-cloud-python/issues/17591)) ([8a1270c](https://github.com/googleapis/google-cloud-python/commit/8a1270cc29e5d8afd4edb59395ebbdac31792ebd))


### Bug Fixes

* **deps:** bump google-api-core to 2.25.0 ([#17599](https://github.com/googleapis/google-cloud-python/issues/17599)) ([8b359e2](https://github.com/googleapis/google-cloud-python/commit/8b359e24279bc9c444114a1476c715647b960c4f))
* **tests:** add --cov-append to gapic-generator and proto-plus to preserve monorepo coverage ([#17603](https://github.com/googleapis/google-cloud-python/issues/17603)) ([2ddcf4d](https://github.com/googleapis/google-cloud-python/commit/2ddcf4dfc711771b284797569f7f8a2de902ade8))

## [1.36.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.35.0...gapic-generator-v1.36.0) (2026-06-25)


### Features

* **mypy:** centralize mypy.ini and update templates ([#17523](https://github.com/googleapis/google-cloud-python/issues/17523)) ([3a67b7f](https://github.com/googleapis/google-cloud-python/commit/3a67b7f05f0e24d2e3fb826e79a5ed69257a49cd))

## [1.35.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.34.1...gapic-generator-v1.35.0) (2026-06-11)


### Features

* setup.py matches prerelease versions (#17370) ([25b857e1bc196da5b56cf599ec346967c6559922](https://github.com/googleapis/google-cloud-python/commit/25b857e1bc196da5b56cf599ec346967c6559922))


### Bug Fixes

* require protobuf 6.33.5 to address CVE-2026-0994 (#17349) ([66422636633e980324877f2ff3805a284001ad38](https://github.com/googleapis/google-cloud-python/commit/66422636633e980324877f2ff3805a284001ad38))

## [1.34.1](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.34.0...gapic-generator-v1.34.1) (2026-05-27)

## [1.34.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.33.0...gapic-generator-v1.34.0) (2026-05-27)


### Bug Fixes

* add pragma to `constants.py` to resolve coverage failure and correct `if` block (#17268) ([1436a23c923e799f9909d039e1f418435845565d](https://github.com/googleapis/google-cloud-python/commit/1436a23c923e799f9909d039e1f418435845565d))
* update incorrect urls in setup.py to point at monorepo vs splitrepo (#17237) ([eaed04baf3cd356c3811c66e64c277c8841c7563](https://github.com/googleapis/google-cloud-python/commit/eaed04baf3cd356c3811c66e64c277c8841c7563))

## [1.33.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.32.0...gapic-generator-v1.33.0) (2026-05-21)


### Bug Fixes

* restore messages not attached to rpc in selective_gapic_generation (#16951) ([3ef95d61995869318097e414e439da1d6c214d1f](https://github.com/googleapis/google-cloud-python/commit/3ef95d61995869318097e414e439da1d6c214d1f))
* bump idna from 3.14 to 3.15 in /packages/gapic-generator (#17179) ([0f7c68bfd437e7f366dacd4080f31e219d7c7090](https://github.com/googleapis/google-cloud-python/commit/0f7c68bfd437e7f366dacd4080f31e219d7c7090))
* resolve core dependencies locally and batch pip installs (#17032) ([5ca88030476fd6be7a2eceef9c94c4fc76820f40](https://github.com/googleapis/google-cloud-python/commit/5ca88030476fd6be7a2eceef9c94c4fc76820f40))
* resolve core dependencies locally and batch pip installs ([5ca88030476fd6be7a2eceef9c94c4fc76820f40](https://github.com/googleapis/google-cloud-python/commit/5ca88030476fd6be7a2eceef9c94c4fc76820f40))

## [1.32.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.31.0...gapic-generator-v1.32.0) (2026-05-11)

## [1.31.0](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.30.14...gapic-generator-v1.31.0) (2026-05-06)


### Features

* add `--resource-name-alias` flag to resolve namespace collisions (#16769) ([6fc78e58e08c9d5a277d8432f3f9740515b44dee](https://github.com/googleapis/google-cloud-python/commit/6fc78e58e08c9d5a277d8432f3f9740515b44dee))


### Bug Fixes

* pass resource aliases to file-level CommonResources (#16945) ([9652a08cb89441fac779eb4fa4d6f48f33b55d3b](https://github.com/googleapis/google-cloud-python/commit/9652a08cb89441fac779eb4fa4d6f48f33b55d3b))

## [1.30.14](https://github.com/googleapis/google-cloud-python/compare/gapic-generator-v1.30.13...gapic-generator-v1.30.14) (2026-04-02)


### Bug Fixes

* Use proper SPDX license identifier (#2594) ([2b3b06c2fb0e41e054e451d947f994f7308512e4](https://github.com/googleapis/google-cloud-python/commit/2b3b06c2fb0e41e054e451d947f994f7308512e4))
* async samples missing await (#2577) ([6ccd3710e43c255bdeca934be03b11a90e1bdfce](https://github.com/googleapis/google-cloud-python/commit/6ccd3710e43c255bdeca934be03b11a90e1bdfce))

## [1.30.13](https://github.com/googleapis/gapic-generator-python/compare/v1.30.12...v1.30.13) (2026-03-13)

## [1.30.12](https://github.com/googleapis/gapic-generator-python/compare/v1.30.11...v1.30.12) (2026-03-12)

## [1.30.11](https://github.com/googleapis/gapic-generator-python/compare/v1.30.10...v1.30.11) (2026-03-11)

## [1.30.10](https://github.com/googleapis/gapic-generator-python/compare/v1.30.9...v1.30.10) (2026-03-09)


### Bug Fixes

* improve type checking (#2530) ([bc3836becb7d0a4e06a1e30128370b525c0762f5](https://github.com/googleapis/gapic-generator-python/commit/bc3836becb7d0a4e06a1e30128370b525c0762f5))
* Allow protobuf 7.x (#2575) ([98137d07f6cbb1aec87826638924c6e0eba78c3d](https://github.com/googleapis/gapic-generator-python/commit/98137d07f6cbb1aec87826638924c6e0eba78c3d))

## [1.30.9](https://github.com/googleapis/gapic-generator-python/compare/v1.30.8...v1.30.9) (2026-02-19)

## [1.30.8](https://github.com/googleapis/gapic-generator-python/compare/v1.30.7...v1.30.8) (2026-02-09)

## [1.30.7](https://github.com/googleapis/gapic-generator-python/compare/v1.30.6...v1.30.7) (2026-02-05)


### Bug Fixes

* updates tests for ListValue response fields (#2532) ([cb659ad2ba5b1a169b9acb5f9055e5ee003f84bd](https://github.com/googleapis/gapic-generator-python/commit/cb659ad2ba5b1a169b9acb5f9055e5ee003f84bd))

## [1.30.6](https://github.com/googleapis/gapic-generator-python/compare/v1.30.5...v1.30.6) (2026-01-30)


### Bug Fixes

* fix incorrect REST request serialization (#2549) ([46e765e5fa2677b5b0d5c85ae5bdad495f9f7e60](https://github.com/googleapis/gapic-generator-python/commit/46e765e5fa2677b5b0d5c85ae5bdad495f9f7e60))
* filter sphinx warnings related to adding a new line after lists (#2533) ([ae0a9e817513c6d4d03fc86685f66be8d9699862](https://github.com/googleapis/gapic-generator-python/commit/ae0a9e817513c6d4d03fc86685f66be8d9699862))

## [1.30.5](https://github.com/googleapis/gapic-generator-python/compare/v1.30.4...v1.30.5) (2026-01-26)


### Bug Fixes

* fix mypy for services with extended operations methods (#2536) ([84667d1b55a5dd895585ae40cbd32b2925ecf8e8](https://github.com/googleapis/gapic-generator-python/commit/84667d1b55a5dd895585ae40cbd32b2925ecf8e8))

## [1.30.4](https://github.com/googleapis/gapic-generator-python/compare/v1.30.3...v1.30.4) (2026-01-20)


### Bug Fixes

* add cryptography to constraints file (#2527) ([595f58f258eb089fc84a3cc1c93d34f950dca77a](https://github.com/googleapis/gapic-generator-python/commit/595f58f258eb089fc84a3cc1c93d34f950dca77a))

## [1.30.3](https://github.com/googleapis/gapic-generator-python/compare/v1.30.2...v1.30.3) (2026-01-13)

## [1.30.2](https://github.com/googleapis/gapic-generator-python/compare/v1.30.1...v1.30.2) (2025-12-15)


### Bug Fixes

* revert changes to code formatting in 1.30.1 (#2511) ([1327d4762b02dfd47ddf7f2014f4ab7503d3963d](https://github.com/googleapis/gapic-generator-python/commit/1327d4762b02dfd47ddf7f2014f4ab7503d3963d))

## [1.30.1](https://github.com/googleapis/gapic-generator-python/compare/v1.30.0...v1.30.1) (2025-12-12)


### Bug Fixes

* **perf:** specify `verify_format=False` when running pypandoc (#2504) ([211e73c14d7bf44df0fe8f9bea14944ea874df3d](https://github.com/googleapis/gapic-generator-python/commit/211e73c14d7bf44df0fe8f9bea14944ea874df3d))

## [1.30.0](https://github.com/googleapis/gapic-generator-python/compare/v1.29.0...v1.30.0) (2025-11-14)

### Features

* auto-enable mTLS when supported certificates are detected (#2472) ([4748760fe6d489d80cb17306157edb43d25f72b3](https://github.com/googleapis/gapic-generator-python/commit/4748760fe6d489d80cb17306157edb43d25f72b3))

### Bug Fixes

* drop packaging and pkg_resources (#2477) ([b4824c50ce06642d7c5bf5cb04e7a4adc02892a8](https://github.com/googleapis/gapic-generator-python/commit/b4824c50ce06642d7c5bf5cb04e7a4adc02892a8))
* add api_version to gapic_metadata.json (#2476) ([c424e33d5e9cfd75b383b4b0c7b77211f3604b79](https://github.com/googleapis/gapic-generator-python/commit/c424e33d5e9cfd75b383b4b0c7b77211f3604b79))


## [1.29.0](https://github.com/googleapis/gapic-generator-python/compare/v1.28.3...v1.29.0) (2025-10-23)


### Features

* Check Python and dependency versions in generated GAPICs ([#2419](https://github.com/googleapis/gapic-generator-python/issues/2419)) ([a9484c6](https://github.com/googleapis/gapic-generator-python/commit/a9484c6a29687c0f3ffb63f271e350054547d495))

## [1.28.3](https://github.com/googleapis/gapic-generator-python/compare/v1.28.2...v1.28.3) (2025-10-21)


### Bug Fixes

* Only format samples if the directory exists ([#2466](https://github.com/googleapis/gapic-generator-python/issues/2466)) ([2d85dee](https://github.com/googleapis/gapic-generator-python/commit/2d85dee33cc1cd2815dcf1e9304905013ec561b6))

## [1.28.2](https://github.com/googleapis/gapic-generator-python/compare/v1.28.1...v1.28.2) (2025-10-20)


### Bug Fixes

* Bump the minimum version of google-apps-card to 0.3.0 ([#2464](https://github.com/googleapis/gapic-generator-python/issues/2464)) ([bfb87e2](https://github.com/googleapis/gapic-generator-python/commit/bfb87e27a38a9c3b77902d1f61899ebc545082e8))

## [1.28.1](https://github.com/googleapis/gapic-generator-python/compare/v1.28.0...v1.28.1) (2025-10-14)


### Bug Fixes

* Fix gapic-version generator option for selective gapic generation ([#2460](https://github.com/googleapis/gapic-generator-python/issues/2460)) ([d7c6072](https://github.com/googleapis/gapic-generator-python/commit/d7c6072cc65e8f166d4b5a78bef250068dca43bf))

## [1.28.0](https://github.com/googleapis/gapic-generator-python/compare/v1.27.2...v1.28.0) (2025-10-07)


### Features

* Add support for Python 3.14 ([#2451](https://github.com/googleapis/gapic-generator-python/issues/2451)) ([3a854db](https://github.com/googleapis/gapic-generator-python/commit/3a854dbd2448a384dd67d683332a4c438805f5a6))


### Bug Fixes

* Require grpcio &gt;=  1.33.2 ([ccf132f](https://github.com/googleapis/gapic-generator-python/commit/ccf132f7a8510ce7ef3728fa569806ac03ccea6e))
* Require grpcio &gt;= 1.75.1 for Python 3.14 ([ccf132f](https://github.com/googleapis/gapic-generator-python/commit/ccf132f7a8510ce7ef3728fa569806ac03ccea6e))

## [1.27.2](https://github.com/googleapis/gapic-generator-python/compare/v1.27.1...v1.27.2) (2025-10-01)


### Bug Fixes

* Deprecate credentials_file ([#2454](https://github.com/googleapis/gapic-generator-python/issues/2454)) ([48c5f38](https://github.com/googleapis/gapic-generator-python/commit/48c5f3895aa638a1def7df3f96c749e746450680))
* Resolve issue where rest-numeric-enums=False is not supported ([#2456](https://github.com/googleapis/gapic-generator-python/issues/2456)) ([3d24a50](https://github.com/googleapis/gapic-generator-python/commit/3d24a50ac992631649ad06bb2dc6c90abe88988a))

## [1.27.1](https://github.com/googleapis/gapic-generator-python/compare/v1.27.0...v1.27.1) (2025-09-26)


### Bug Fixes

* Add testing for Python 3.14 Pre-release ([7f7d50e](https://github.com/googleapis/gapic-generator-python/commit/7f7d50e3154d548e8066d251b85a589afbf183d7))

## [1.27.0](https://github.com/googleapis/gapic-generator-python/compare/v1.26.2...v1.27.0) (2025-09-24)


### Features

* Add gapic-version generator option ([#2440](https://github.com/googleapis/gapic-generator-python/issues/2440)) ([75eb349](https://github.com/googleapis/gapic-generator-python/commit/75eb349efcb907dc443b6e8a2c11b2056a476009))

## [1.26.2](https://github.com/googleapis/gapic-generator-python/compare/v1.26.1...v1.26.2) (2025-08-30)


### Documentation

* Minor formatting improvements ([#2432](https://github.com/googleapis/gapic-generator-python/issues/2432)) ([17d6db5](https://github.com/googleapis/gapic-generator-python/commit/17d6db5355b3d64c04dcdfe9b8433493b264c60c))

## [1.26.1](https://github.com/googleapis/gapic-generator-python/compare/v1.26.0...v1.26.1) (2025-08-28)


### Bug Fixes

* Temporarily disable `test_<service>_api_version_header_async` which is not marked as async ([9382ac3](https://github.com/googleapis/gapic-generator-python/commit/9382ac3546f335116665e10c4132369bc7637a67))

## [1.26.0](https://github.com/googleapis/gapic-generator-python/compare/v1.25.0...v1.26.0) (2025-05-28)


### Features

* Add client debug logging support for server side streaming REST calls ([#2340](https://github.com/googleapis/gapic-generator-python/issues/2340)) ([8a705c5](https://github.com/googleapis/gapic-generator-python/commit/8a705c513fe63b025eca738feb64a1e414f9f4b6))

## [1.25.0](https://github.com/googleapis/gapic-generator-python/compare/v1.24.1...v1.25.0) (2025-05-06)


### Features

* Add protobuf runtime version to `x-goog-api-client` header ([#2368](https://github.com/googleapis/gapic-generator-python/issues/2368)) ([9c05dbe](https://github.com/googleapis/gapic-generator-python/commit/9c05dbeb9285919f45924be09c445b707cb85b54))

## [1.24.1](https://github.com/googleapis/gapic-generator-python/compare/v1.24.0...v1.24.1) (2025-04-17)


### Bug Fixes

* Update generated docs to match synthtool templates ([3f62f31](https://github.com/googleapis/gapic-generator-python/commit/3f62f31d5146147c4bc6393fbeef18ce1d9a1a42))

## [1.24.0](https://github.com/googleapis/gapic-generator-python/compare/v1.23.6...v1.24.0) (2025-04-11)


### Features

* Adds augmented pagination to account for BQ family of APIs ([#2372](https://github.com/googleapis/gapic-generator-python/issues/2372)) ([30cd1a4](https://github.com/googleapis/gapic-generator-python/commit/30cd1a49353048fc190114cfb7a73e14ec2eff31))


### Bug Fixes

* Fixed internal method generation naming issues ([#2365](https://github.com/googleapis/gapic-generator-python/issues/2365)) ([868f201](https://github.com/googleapis/gapic-generator-python/commit/868f201957b271c9390bf41374897a2ce728a5e2))
* Missing DEFAULT_HOST should still result in compiling code ([#2051](https://github.com/googleapis/gapic-generator-python/issues/2051)) ([dc6d4f7](https://github.com/googleapis/gapic-generator-python/commit/dc6d4f7ec0853557bb7c25a8276fbe262c5bda5d))

## [1.23.6](https://github.com/googleapis/gapic-generator-python/compare/v1.23.5...v1.23.6) (2025-03-17)


### Documentation

* Update copyright year ([#2363](https://github.com/googleapis/gapic-generator-python/issues/2363)) ([745ce7a](https://github.com/googleapis/gapic-generator-python/commit/745ce7af2978eff293e9abbad9a622fdfe7c782a))

## [1.23.5](https://github.com/googleapis/gapic-generator-python/compare/v1.23.4...v1.23.5) (2025-03-06)


### Bug Fixes

* Allow Protobuf 6.x ([#2352](https://github.com/googleapis/gapic-generator-python/issues/2352)) ([bb2d557](https://github.com/googleapis/gapic-generator-python/commit/bb2d557bf266599669c15efd81d8e900d48e7c3e))

## [1.23.4](https://github.com/googleapis/gapic-generator-python/compare/v1.23.3...v1.23.4) (2025-03-04)


### Bug Fixes

* Allow proto files to be included in the output of py_gapic_assembly_pkg ([#2349](https://github.com/googleapis/gapic-generator-python/issues/2349)) ([b301bef](https://github.com/googleapis/gapic-generator-python/commit/b301befcda29ae1f9c204e0836656c03c2d74a2a))

## [1.23.3](https://github.com/googleapis/gapic-generator-python/compare/v1.23.2...v1.23.3) (2025-03-03)


### Bug Fixes

* Resolve issue where pre-release versions of dependencies are installed ([#2347](https://github.com/googleapis/gapic-generator-python/issues/2347)) ([aea00b2](https://github.com/googleapis/gapic-generator-python/commit/aea00b2137ac926bdc527eb9c4666eb8b1ca70e1))

## [1.23.2](https://github.com/googleapis/gapic-generator-python/compare/v1.23.1...v1.23.2) (2025-02-28)


### Bug Fixes

* Resolve rare issue where ValueError is not raised when both request and flattened param are set ([#2258](https://github.com/googleapis/gapic-generator-python/issues/2258)) ([4ecfbeb](https://github.com/googleapis/gapic-generator-python/commit/4ecfbeb7028dc1856692f5cda95a8767e4cb69e4))

## [1.23.1](https://github.com/googleapis/gapic-generator-python/compare/v1.23.0...v1.23.1) (2025-02-14)


### Documentation

* Fix minor typos ([#2318](https://github.com/googleapis/gapic-generator-python/issues/2318)) ([7be3a55](https://github.com/googleapis/gapic-generator-python/commit/7be3a559d59b778c5733e21b4c0169b17bd05c4a))

## [1.23.0](https://github.com/googleapis/gapic-generator-python/compare/v1.22.1...v1.23.0) (2025-02-14)


### Features

* Add ability to remove unversioned modules ([#2329](https://github.com/googleapis/gapic-generator-python/issues/2329)) ([ccd619f](https://github.com/googleapis/gapic-generator-python/commit/ccd619f0461f6b1aa22cdd6fbcc37039bcdc541a))
* Added support for internal methods in selective GAPIC generation ([#2325](https://github.com/googleapis/gapic-generator-python/issues/2325)) ([eb8a69e](https://github.com/googleapis/gapic-generator-python/commit/eb8a69e3141f865903716b9c5013e2c7650c60da))

## [1.22.1](https://github.com/googleapis/gapic-generator-python/compare/v1.22.0...v1.22.1) (2025-02-12)


### Bug Fixes

* **deps:** Require grpc-google-iam-v1&gt;=0.14.0 ([#2327](https://github.com/googleapis/gapic-generator-python/issues/2327)) ([d4236c8](https://github.com/googleapis/gapic-generator-python/commit/d4236c8a823d78350015c97c0d10e505771da564))

## [1.22.0](https://github.com/googleapis/gapic-generator-python/compare/v1.21.0...v1.22.0) (2025-01-30)


### Features

* Add cred info to auth related errors ([#2115](https://github.com/googleapis/gapic-generator-python/issues/2115)) ([a694ceb](https://github.com/googleapis/gapic-generator-python/commit/a694cebf386aace80aab36ef9cc2d1102078d3d0))
* Add REST Interceptors to support reading metadata ([#2299](https://github.com/googleapis/gapic-generator-python/issues/2299)) ([e050f4e](https://github.com/googleapis/gapic-generator-python/commit/e050f4eb3eddfe150f028a2a2bd901899afb965a))
* Add support for reading selective GAPIC generation methods from service YAML ([#2272](https://github.com/googleapis/gapic-generator-python/issues/2272)) ([3a1a91c](https://github.com/googleapis/gapic-generator-python/commit/3a1a91cadf4438d7b5bf0edaf93ffa3f966eb7e2))

## [1.21.0](https://github.com/googleapis/gapic-generator-python/compare/v1.20.2...v1.21.0) (2024-12-11)


### Features

* Add client debug logging support for async gRPC ([#2291](https://github.com/googleapis/gapic-generator-python/issues/2291)) ([f45935a](https://github.com/googleapis/gapic-generator-python/commit/f45935a4d760a36bf989ed79bfd02aa7ec203468))
* Add client logging support for sync gRPC ([#2284](https://github.com/googleapis/gapic-generator-python/issues/2284)) ([dddf797](https://github.com/googleapis/gapic-generator-python/commit/dddf797a1ec7bf0496b4b4c75f8d37faa753c824))
* Add debug log when creating client ([#2265](https://github.com/googleapis/gapic-generator-python/issues/2265)) ([8be95a2](https://github.com/googleapis/gapic-generator-python/commit/8be95a2f4749a2882117154aa655c0a9d71cdc50))
* Add debug log when sending requests via REST ([#2270](https://github.com/googleapis/gapic-generator-python/issues/2270)) ([4cb1fa2](https://github.com/googleapis/gapic-generator-python/commit/4cb1fa2452ad5ba59b34c9d25cb3ca0c635059ac))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([#2251](https://github.com/googleapis/gapic-generator-python/issues/2251)) ([8b3b80f](https://github.com/googleapis/gapic-generator-python/commit/8b3b80f4b55c295e5d13084284ff0e2a72b2e993))
* **log:** Preserve dict of rest async response headers ([#2288](https://github.com/googleapis/gapic-generator-python/issues/2288)) ([b10cc21](https://github.com/googleapis/gapic-generator-python/commit/b10cc21daf7d17567119f5c9b33d98fe18072eb4))

## [1.20.2](https://github.com/googleapis/gapic-generator-python/compare/v1.20.1...v1.20.2) (2024-10-30)


### Bug Fixes

* Disable universe-domain validation ([#2236](https://github.com/googleapis/gapic-generator-python/issues/2236)) ([ecaa41e](https://github.com/googleapis/gapic-generator-python/commit/ecaa41e7984a8aa2244138cce99cb91a87872c54))

## [1.20.1](https://github.com/googleapis/gapic-generator-python/compare/v1.20.0...v1.20.1) (2024-10-25)


### Bug Fixes

* Allow google-cloud-documentai 3.x ([#2237](https://github.com/googleapis/gapic-generator-python/issues/2237)) ([946adf1](https://github.com/googleapis/gapic-generator-python/commit/946adf16d8a1cf83019eaa9b6a9e8b1baf95159d))

## [1.20.0](https://github.com/googleapis/gapic-generator-python/compare/v1.19.1...v1.20.0) (2024-10-23)


### Features

* Add support for Python 3.13 ([#2215](https://github.com/googleapis/gapic-generator-python/issues/2215)) ([4e1f9c6](https://github.com/googleapis/gapic-generator-python/commit/4e1f9c623065e5917dbd1d2178228776b7ea536d))


### Bug Fixes

* Added underscores in services/types in index.rst.j2 ([#2232](https://github.com/googleapis/gapic-generator-python/issues/2232)) ([f2053ee](https://github.com/googleapis/gapic-generator-python/commit/f2053ee04127f1f0d23fd04438ee4607ee1ce76c))
* Allow `google-cloud-kms` 3.x ([#2226](https://github.com/googleapis/gapic-generator-python/issues/2226)) ([5e07501](https://github.com/googleapis/gapic-generator-python/commit/5e075016a2119782e611cd51335fa0af7e4c18c2))

## [1.19.1](https://github.com/googleapis/gapic-generator-python/compare/v1.19.0...v1.19.1) (2024-10-10)


### Bug Fixes

* Add default library settings for incorrect lib version ([#2212](https://github.com/googleapis/gapic-generator-python/issues/2212)) ([de46272](https://github.com/googleapis/gapic-generator-python/commit/de46272ae65e9117be7f362355cefd28d0780917))
* Resolve issue with wait operation mixin ([#2218](https://github.com/googleapis/gapic-generator-python/issues/2218)) ([095d060](https://github.com/googleapis/gapic-generator-python/commit/095d0600803dace8d665fee9ccbc460720b5fe17))
* Use disambiguated name for rpcs to avoid collisions ([#2217](https://github.com/googleapis/gapic-generator-python/issues/2217)) ([296cd3e](https://github.com/googleapis/gapic-generator-python/commit/296cd3e814ba58954c16ca6256db0359bcab0f09))

## [1.19.0](https://github.com/googleapis/gapic-generator-python/compare/v1.18.5...v1.19.0) (2024-10-09)


### Features

* Add async rest transport support in gapics ([#2164](https://github.com/googleapis/gapic-generator-python/issues/2164)) ([2949465](https://github.com/googleapis/gapic-generator-python/commit/29494651fb39719af920ee1c114c82bd903e544b))
* Add support for reading ClientLibrarySettings from service configuration YAML ([#2098](https://github.com/googleapis/gapic-generator-python/issues/2098)) ([11e3967](https://github.com/googleapis/gapic-generator-python/commit/11e3967b6a3b1e86f5ec0f5387bd340e3a8ae9d0))
* Implement async rest transport constructor ([#2123](https://github.com/googleapis/gapic-generator-python/issues/2123)) ([2809753](https://github.com/googleapis/gapic-generator-python/commit/28097536e1a47063a5d3211e9c1c498a1f06c724))
* Leverage async anonymous credentials in tests ([#2105](https://github.com/googleapis/gapic-generator-python/issues/2105)) ([4afac87](https://github.com/googleapis/gapic-generator-python/commit/4afac87efc8fcdd7090d003b6247be64071b611d))


### Bug Fixes

* Add support for field with name 'self' ([#2205](https://github.com/googleapis/gapic-generator-python/issues/2205)) ([ed88fe2](https://github.com/googleapis/gapic-generator-python/commit/ed88fe298647cdad310a5341f931a0de42f1b81e))
* Resolve issue where explicit routing metadata was not sent in async clients ([#2133](https://github.com/googleapis/gapic-generator-python/issues/2133)) ([c222b12](https://github.com/googleapis/gapic-generator-python/commit/c222b125d741426259d82e726c0c07397d099a8a))
* Streaming for sync REST API calls ([#2204](https://github.com/googleapis/gapic-generator-python/issues/2204)) ([ce3b84c](https://github.com/googleapis/gapic-generator-python/commit/ce3b84c67a31785f45eb46f154ef08af6edc9a36))

## [1.18.5](https://github.com/googleapis/gapic-generator-python/compare/v1.18.4...v1.18.5) (2024-08-06)


### Bug Fixes

* Mypy types in get_transport ([#2088](https://github.com/googleapis/gapic-generator-python/issues/2088)) ([f76fdaf](https://github.com/googleapis/gapic-generator-python/commit/f76fdaf1f717e99caef4c0ce217eef3322df9a30))
* Require google.shopping.type &gt;= 0.1.6 ([#2083](https://github.com/googleapis/gapic-generator-python/issues/2083)) ([1b63310](https://github.com/googleapis/gapic-generator-python/commit/1b63310378692f478ef29734b3cb5fde3d436b22))

## [1.18.4](https://github.com/googleapis/gapic-generator-python/compare/v1.18.3...v1.18.4) (2024-07-26)


### Bug Fixes

* Fix AttributeError with AsyncRetry ([#2072](https://github.com/googleapis/gapic-generator-python/issues/2072)) ([dcddac8](https://github.com/googleapis/gapic-generator-python/commit/dcddac803fc5eb58c0d242d88c8b4c419b83fe90))

## [1.18.3](https://github.com/googleapis/gapic-generator-python/compare/v1.18.2...v1.18.3) (2024-07-23)


### Bug Fixes

* Allow pyi files to be included in the output of py_gapic_assembly_pkg ([#2036](https://github.com/googleapis/gapic-generator-python/issues/2036)) ([8c517a0](https://github.com/googleapis/gapic-generator-python/commit/8c517a030c88cceb179c6d83ad706b2d7f1eba89))
* Retry and timeout values do not propagate in requests during pagination ([#2065](https://github.com/googleapis/gapic-generator-python/issues/2065)) ([76aa98e](https://github.com/googleapis/gapic-generator-python/commit/76aa98eda53cfc5c406fb5ed705e894c5c6c2513))

## [1.18.2](https://github.com/googleapis/gapic-generator-python/compare/v1.18.1...v1.18.2) (2024-07-02)


### Bug Fixes

* Fix AwaitableMock test coverage ([b48c935](https://github.com/googleapis/gapic-generator-python/commit/b48c935b55b840ad2deff451c5229f32bc386e9c))

## [1.18.1](https://github.com/googleapis/gapic-generator-python/compare/v1.18.0...v1.18.1) (2024-06-20)


### Bug Fixes

* Allow protobuf 5.x ([#2042](https://github.com/googleapis/gapic-generator-python/issues/2042)) ([1998b81](https://github.com/googleapis/gapic-generator-python/commit/1998b813d2525cef8e46d606de494f0847e156bf))
* Fix credentials typing issue in transport layer ([#2043](https://github.com/googleapis/gapic-generator-python/issues/2043)) ([205fe5e](https://github.com/googleapis/gapic-generator-python/commit/205fe5e9445eb2f6811f022c68003d23c95f186b))

## [1.18.0](https://github.com/googleapis/gapic-generator-python/compare/v1.17.1...v1.18.0) (2024-05-08)


### Features

* Add support for reading google.api.api_version ([#1999](https://github.com/googleapis/gapic-generator-python/issues/1999)) ([b2486e5](https://github.com/googleapis/gapic-generator-python/commit/b2486e5630312fb01b9eb5ffb09c9f0328fbce20))

## [1.17.1](https://github.com/googleapis/gapic-generator-python/compare/v1.17.0...v1.17.1) (2024-04-26)


### Bug Fixes

* Type error for compute client(s) tests ([#2014](https://github.com/googleapis/gapic-generator-python/issues/2014)) ([61f50f7](https://github.com/googleapis/gapic-generator-python/commit/61f50f76fcbc47ef2d0fd4686f9187d22c2e698e))

## [1.17.0](https://github.com/googleapis/gapic-generator-python/compare/v1.16.1...v1.17.0) (2024-04-18)


### Features

* Allow Callables for transport and channel init ([#1699](https://github.com/googleapis/gapic-generator-python/issues/1699)) ([62855c1](https://github.com/googleapis/gapic-generator-python/commit/62855c11570bb3a42cebee43cecd0e59ffb01573))


### Bug Fixes

* Set `default` argument of `jinja-filters.map()` when looking up attributes ([#1989](https://github.com/googleapis/gapic-generator-python/issues/1989)) ([3e74a0a](https://github.com/googleapis/gapic-generator-python/commit/3e74a0a3f7f94cf21aaf198ecd55cca419cedbd2))
* Update the lower bound for `google-apps-card` ([#2012](https://github.com/googleapis/gapic-generator-python/issues/2012)) ([9027a5f](https://github.com/googleapis/gapic-generator-python/commit/9027a5fc83218241981a326984ed1aad3a162a4b))

## [1.16.1](https://github.com/googleapis/gapic-generator-python/compare/v1.16.0...v1.16.1) (2024-03-22)


### Bug Fixes

* Cater for empty async call ([#1997](https://github.com/googleapis/gapic-generator-python/issues/1997)) ([801eedb](https://github.com/googleapis/gapic-generator-python/commit/801eedbb8986516ab354da6bccd4289a9c6d5362))

## [1.16.0](https://github.com/googleapis/gapic-generator-python/compare/v1.15.0...v1.16.0) (2024-03-22)


### Features

* Add support for reading MethodSettings from service configuration YAML ([#1975](https://github.com/googleapis/gapic-generator-python/issues/1975)) ([24a23a1](https://github.com/googleapis/gapic-generator-python/commit/24a23a1ab885246e447c0010b2e5602209dfbb8d))
* Automatically populate uuid4 fields ([#1985](https://github.com/googleapis/gapic-generator-python/issues/1985)) ([eb57e4f](https://github.com/googleapis/gapic-generator-python/commit/eb57e4f2e6b339f89aa3b7d55e4b4c0dfdfd002e))


### Bug Fixes

* Fix dependency `google-apps-card` ([#1971](https://github.com/googleapis/gapic-generator-python/issues/1971)) ([9a49cb0](https://github.com/googleapis/gapic-generator-python/commit/9a49cb07de8bd54d8601b742367887bdde854643))

## [1.15.0](https://github.com/googleapis/gapic-generator-python/compare/v1.14.5...v1.15.0) (2024-03-15)


### Features

* Add support for checking uuid4 fields ([#1972](https://github.com/googleapis/gapic-generator-python/issues/1972)) ([d5f90a2](https://github.com/googleapis/gapic-generator-python/commit/d5f90a2455cb671e67e2cd30f3eb470092e4f889))


### Bug Fixes

* Fix resource path helpers for paths with =** ([#1976](https://github.com/googleapis/gapic-generator-python/issues/1976)) ([08c01e9](https://github.com/googleapis/gapic-generator-python/commit/08c01e9d92adeb492a7b526b1b5267931750ee61))

## [1.14.5](https://github.com/googleapis/gapic-generator-python/compare/v1.14.4...v1.14.5) (2024-03-04)


### Bug Fixes

* Update copyright year ([dde240b](https://github.com/googleapis/gapic-generator-python/commit/dde240bc7e63396416709b7f3dd7b50b355bc829))

## [1.14.4](https://github.com/googleapis/gapic-generator-python/compare/v1.14.3...v1.14.4) (2024-02-29)


### Bug Fixes

* Add `google-apps-card` dependency ([#1964](https://github.com/googleapis/gapic-generator-python/issues/1964)) ([d4d51d4](https://github.com/googleapis/gapic-generator-python/commit/d4d51d4e84342065f34ef584abbe4b99404de574))
* Exclude google-auth 2.24.0 and 2.25.0 ([#1957](https://github.com/googleapis/gapic-generator-python/issues/1957)) ([abe8de3](https://github.com/googleapis/gapic-generator-python/commit/abe8de30086506f4694c5c5e4bae08fae8525e4b))

## [1.14.3](https://github.com/googleapis/gapic-generator-python/compare/v1.14.2...v1.14.3) (2024-02-14)


### Bug Fixes

* Fix TypeError: MessageToJson() got an unexpected keyword argument 'including_default_value_fields' ([#1936](https://github.com/googleapis/gapic-generator-python/issues/1936)) ([12734ff](https://github.com/googleapis/gapic-generator-python/commit/12734ffb37ab005d556f7b7a23219701d404487d))
* Require google-api-core 1.34.1 ([#1942](https://github.com/googleapis/gapic-generator-python/issues/1942)) ([6c176a3](https://github.com/googleapis/gapic-generator-python/commit/6c176a3277c935bf5b02ce2d1a8b1ef7503c338a))
* Resolve issue with missing import for certain enums in **/types/… ([#1944](https://github.com/googleapis/gapic-generator-python/issues/1944)) ([97a4eed](https://github.com/googleapis/gapic-generator-python/commit/97a4eedeee196568008ce6612abbce566d9ad5a0))

## [1.14.2](https://github.com/googleapis/gapic-generator-python/compare/v1.14.1...v1.14.2) (2024-02-06)


### Bug Fixes

* Fix `ValueError` in `test__validate_universe_domain` ([#1931](https://github.com/googleapis/gapic-generator-python/issues/1931)) ([ce855a8](https://github.com/googleapis/gapic-generator-python/commit/ce855a866c43e80fb3f9ba3b295c83afcd6297b7))

## [1.14.1](https://github.com/googleapis/gapic-generator-python/compare/v1.14.0...v1.14.1) (2024-02-02)


### Bug Fixes

* Add google-auth as a direct dependency ([2154924](https://github.com/googleapis/gapic-generator-python/commit/2154924c6ef9df6e2727b433ec7d2fee762ccde8))
* Add staticmethod decorator to methods added in [#1873](https://github.com/googleapis/gapic-generator-python/issues/1873) ([2154924](https://github.com/googleapis/gapic-generator-python/commit/2154924c6ef9df6e2727b433ec7d2fee762ccde8))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([2154924](https://github.com/googleapis/gapic-generator-python/commit/2154924c6ef9df6e2727b433ec7d2fee762ccde8))

## [1.14.0](https://github.com/googleapis/gapic-generator-python/compare/v1.13.1...v1.14.0) (2024-01-31)


### Features

* Allow users to explicitly configure universe domain. ([#1898](https://github.com/googleapis/gapic-generator-python/issues/1898)) ([e5a55c1](https://github.com/googleapis/gapic-generator-python/commit/e5a55c1c01f0e1b3739927640c713057cd17b4ae))


### Bug Fixes

* Mock out configure_mtls_channel in rest transport for testing ([#1920](https://github.com/googleapis/gapic-generator-python/issues/1920)) ([9ade50d](https://github.com/googleapis/gapic-generator-python/commit/9ade50d2dfff0bb15fbe1fb2b00644047f6d2d38))

## [1.13.1](https://github.com/googleapis/gapic-generator-python/compare/v1.13.0...v1.13.1) (2024-01-17)


### Bug Fixes

* Add None as a type to OptionalRetry ([#1901](https://github.com/googleapis/gapic-generator-python/issues/1901)) ([011475c](https://github.com/googleapis/gapic-generator-python/commit/011475c525cda4245803e197c77fa2a1c37fa98d))

## [1.13.0](https://github.com/googleapis/gapic-generator-python/compare/v1.12.0...v1.13.0) (2023-11-20)


### Features

* Add support for python 3.12 ([#1816](https://github.com/googleapis/gapic-generator-python/issues/1816)) ([b65898e](https://github.com/googleapis/gapic-generator-python/commit/b65898e11f6b7210a0614eb1ece4b139541f17cd))
* Add support for python 312 (ads templates) ([#1861](https://github.com/googleapis/gapic-generator-python/issues/1861)) ([d65a540](https://github.com/googleapis/gapic-generator-python/commit/d65a54045abb9b25364e8cfb0ad4c7e5d95917d2))


### Bug Fixes

* Bump proto-plus version to 1.22.3 ([#1863](https://github.com/googleapis/gapic-generator-python/issues/1863)) ([2ad9be2](https://github.com/googleapis/gapic-generator-python/commit/2ad9be28500972777cec69097be6581eaefb89e4))

## [1.12.0](https://github.com/googleapis/gapic-generator-python/compare/v1.11.11...v1.12.0) (2023-11-09)


### Features

* Introduce compatibility with native namespace packages ([#1852](https://github.com/googleapis/gapic-generator-python/issues/1852)) ([ef2094a](https://github.com/googleapis/gapic-generator-python/commit/ef2094ae15cd8b4be5e18f1c6b4d62a6b8f0d416))


### Bug Fixes

* Allow pb2 files to be included in the output of py_gapic_assembly_pkg ([#1855](https://github.com/googleapis/gapic-generator-python/issues/1855)) ([e374734](https://github.com/googleapis/gapic-generator-python/commit/e37473494002de855d63498f731c26cec5c49b9c))
* Implement Async Client to use Async Retry to work as expected ([#1823](https://github.com/googleapis/gapic-generator-python/issues/1823)) ([8ede788](https://github.com/googleapis/gapic-generator-python/commit/8ede788616b5b73f52bc7a8aca831c37b054b81f))
* Wrap method in async client ([#1834](https://github.com/googleapis/gapic-generator-python/issues/1834)) ([8e1b5e0](https://github.com/googleapis/gapic-generator-python/commit/8e1b5e077a78904710d350b7dc97cdd2d6034fa9))

## [1.11.11](https://github.com/googleapis/gapic-generator-python/compare/v1.11.10...v1.11.11) (2023-11-02)


### Bug Fixes

* Add missing dependency google-shopping-type ([#1842](https://github.com/googleapis/gapic-generator-python/issues/1842)) ([b1eabd7](https://github.com/googleapis/gapic-generator-python/commit/b1eabd7f439d032edd3fb6d0b65415a2c6b737ab))

## [1.11.10](https://github.com/googleapis/gapic-generator-python/compare/v1.11.9...v1.11.10) (2023-10-26)


### Bug Fixes

* Upgrade rules_python to 0.26.0 ([#1825](https://github.com/googleapis/gapic-generator-python/issues/1825)) ([5d66387](https://github.com/googleapis/gapic-generator-python/commit/5d66387cd42a38d54dde5e8f0153446fee194b27))

## [1.11.9](https://github.com/googleapis/gapic-generator-python/compare/v1.11.8...v1.11.9) (2023-10-18)


### Bug Fixes

* Rename rst files to avoid conflict with service names ([#1706](https://github.com/googleapis/gapic-generator-python/issues/1706)) ([70c3db5](https://github.com/googleapis/gapic-generator-python/commit/70c3db5ae1bac69e8ade13e4608af60c824e7870))

## [1.11.8](https://github.com/googleapis/gapic-generator-python/compare/v1.11.7...v1.11.8) (2023-10-16)


### Bug Fixes

* Add missing dependencies ([#1804](https://github.com/googleapis/gapic-generator-python/issues/1804)) ([3e020cd](https://github.com/googleapis/gapic-generator-python/commit/3e020cd338339e311f825c7ea77dd473b660bcc5))
* Fix coverage gap in tests ([#1802](https://github.com/googleapis/gapic-generator-python/issues/1802)) ([2fe0df1](https://github.com/googleapis/gapic-generator-python/commit/2fe0df19261bf5e6e7589a7cd77de03dd1c5c5fc))

## [1.11.7](https://github.com/googleapis/gapic-generator-python/compare/v1.11.6...v1.11.7) (2023-10-12)


### Bug Fixes

* Add google-cloud-iam to dependencies ([#1792](https://github.com/googleapis/gapic-generator-python/issues/1792)) ([c5ed152](https://github.com/googleapis/gapic-generator-python/commit/c5ed1529f1d61ea3d0990b662a3d979d05192ab5))
* Fix regression in REST unit test ([#1798](https://github.com/googleapis/gapic-generator-python/issues/1798)) ([0cee3c2](https://github.com/googleapis/gapic-generator-python/commit/0cee3c26bcd428ce6eec57c3616423905ec21781))
* **revert:** Partial revert of [#1125](https://github.com/googleapis/gapic-generator-python/issues/1125) ([#1799](https://github.com/googleapis/gapic-generator-python/issues/1799)) ([14eec93](https://github.com/googleapis/gapic-generator-python/commit/14eec937fc4eddf3d6bd32f7ae35969bdc6f8bb5))

## [1.11.6](https://github.com/googleapis/gapic-generator-python/compare/v1.11.5...v1.11.6) (2023-10-09)


### Bug Fixes

* Change to Set vs FrozenSet and thread the same set through ([#1125](https://github.com/googleapis/gapic-generator-python/issues/1125)) ([723efca](https://github.com/googleapis/gapic-generator-python/commit/723efca3f909527c48e8070eff61511293888626))
* Resolve unit test failure caused by differences in protobuf runtimes ([#1749](https://github.com/googleapis/gapic-generator-python/issues/1749)) ([812abce](https://github.com/googleapis/gapic-generator-python/commit/812abceeb68d86f3902974aaeef8a58cfd6e7515))

## [1.11.5](https://github.com/googleapis/gapic-generator-python/compare/v1.11.4...v1.11.5) (2023-09-06)


### Bug Fixes

* Fix docs build for generated clients ([#1715](https://github.com/googleapis/gapic-generator-python/issues/1715)) ([e4db994](https://github.com/googleapis/gapic-generator-python/commit/e4db9941078fe417e0d7b30bcd937e6c4dc0e6ba))
* Fix docs build for numbered lists ([#1740](https://github.com/googleapis/gapic-generator-python/issues/1740)) ([19cc5b3](https://github.com/googleapis/gapic-generator-python/commit/19cc5b36348c1406d2c84fc65e44dbe45a2bdd1c))
* Preserve new lines ([#1721](https://github.com/googleapis/gapic-generator-python/issues/1721)) ([baa136f](https://github.com/googleapis/gapic-generator-python/commit/baa136fd4fa94cfb6638c3074f10033dcc4f9da1))
* Remove duplicate import statement for `google.longrunning.operations_pb2` ([#1726](https://github.com/googleapis/gapic-generator-python/issues/1726)) ([e3f08cd](https://github.com/googleapis/gapic-generator-python/commit/e3f08cd48bdf93e668be1b4b117190383ce2c022))
* Resolve some Showcase test errors ([#1353](https://github.com/googleapis/gapic-generator-python/issues/1353)) ([4eee261](https://github.com/googleapis/gapic-generator-python/commit/4eee26181e8db9fb5144eef5a76f178c1594e48a))

## [1.11.4](https://github.com/googleapis/gapic-generator-python/compare/v1.11.3...v1.11.4) (2023-07-11)


### Documentation

* Ensure new line after colon ([#1691](https://github.com/googleapis/gapic-generator-python/issues/1691)) ([e400fba](https://github.com/googleapis/gapic-generator-python/commit/e400fba0e75f3f8789e9b6ba00b949a012b17496))

## [1.11.3](https://github.com/googleapis/gapic-generator-python/compare/v1.11.2...v1.11.3) (2023-07-07)


### Documentation

* Fix formatting of docstring with lists ([#1687](https://github.com/googleapis/gapic-generator-python/issues/1687)) ([abe0f3f](https://github.com/googleapis/gapic-generator-python/commit/abe0f3f3dc444fd12faf017e8ad73c941608e120))

## [1.11.2](https://github.com/googleapis/gapic-generator-python/compare/v1.11.1...v1.11.2) (2023-07-06)


### Documentation

* Update copyright year ([#1685](https://github.com/googleapis/gapic-generator-python/issues/1685)) ([6e1bcde](https://github.com/googleapis/gapic-generator-python/commit/6e1bcde56f232789d356ca5617aa668d5d4cf37f))

## [1.11.1](https://github.com/googleapis/gapic-generator-python/compare/v1.11.0...v1.11.1) (2023-07-05)


### Bug Fixes

* Add `help` as a reserved word ([#1682](https://github.com/googleapis/gapic-generator-python/issues/1682)) ([23fe890](https://github.com/googleapis/gapic-generator-python/commit/23fe890136144567e153d257faa31086f18544df))
* Fix issue with reserved names and http body. ([#1657](https://github.com/googleapis/gapic-generator-python/issues/1657)) ([e51109d](https://github.com/googleapis/gapic-generator-python/commit/e51109da85bbd53e5b2af90fbce031b0dd7e2be5))

## [1.11.0](https://github.com/googleapis/gapic-generator-python/compare/v1.10.0...v1.11.0) (2023-06-27)


### Features

* Support snippet generation for services that only support REST transport ([#1656](https://github.com/googleapis/gapic-generator-python/issues/1656)) ([bb60a3d](https://github.com/googleapis/gapic-generator-python/commit/bb60a3d87b252f276f07f9ab21a17cd279b702c1))


### Bug Fixes

* Add `exec` as a reserved word ([#1673](https://github.com/googleapis/gapic-generator-python/issues/1673)) ([90af1e6](https://github.com/googleapis/gapic-generator-python/commit/90af1e6a97297c8bfbf8951e09922f3727b7074f))
* Add async context manager return types ([#1660](https://github.com/googleapis/gapic-generator-python/issues/1660)) ([7f58100](https://github.com/googleapis/gapic-generator-python/commit/7f58100e645d9f868953deeac50992a44f6048e2))
* Fix bug with quote replacement. ([#1613](https://github.com/googleapis/gapic-generator-python/issues/1613)) ([5268045](https://github.com/googleapis/gapic-generator-python/commit/5268045c34b36f4a89e00559bedde04d2a35bdd7))
* Fix code coverage in async test ([#1646](https://github.com/googleapis/gapic-generator-python/issues/1646)) ([ccada98](https://github.com/googleapis/gapic-generator-python/commit/ccada9880890d6fb10ee02dad14b960d77335b82))
* Mock return_value should not populate oneof message fields ([#1668](https://github.com/googleapis/gapic-generator-python/issues/1668)) ([34d1a5d](https://github.com/googleapis/gapic-generator-python/commit/34d1a5d6455af7ee5bd57743e55e1ada16985372))

## [1.10.0](https://github.com/googleapis/gapic-generator-python/compare/v1.9.1...v1.10.0) (2023-03-28)


### Features

* Freezes reserved names list. ([#1575](https://github.com/googleapis/gapic-generator-python/issues/1575)) ([b1b56ab](https://github.com/googleapis/gapic-generator-python/commit/b1b56ab22442d6d00ad2381ea14ce46aeda96e6e))

## [1.9.1](https://github.com/googleapis/gapic-generator-python/compare/v1.9.0...v1.9.1) (2023-03-22)


### Bug Fixes

* Restore grpc-google-iam-v1 dependency when api.has_iam_mixin is True ([#1631](https://github.com/googleapis/gapic-generator-python/issues/1631)) ([a7ed16d](https://github.com/googleapis/gapic-generator-python/commit/a7ed16dbc1098772a5d9ff1f48f0651cc90fe5b4))


### Documentation

* Fix docstring with proto-plus dependency ([#1624](https://github.com/googleapis/gapic-generator-python/issues/1624)) ([dce071d](https://github.com/googleapis/gapic-generator-python/commit/dce071d71c66c12cf001a66d238f6f6ea3c67c04))
* Fix formatting of request arg in docstring ([#1628](https://github.com/googleapis/gapic-generator-python/issues/1628)) ([8b4f5ca](https://github.com/googleapis/gapic-generator-python/commit/8b4f5caf1f496b36a02ed26b5af65b0d58ab1b6e))

## [1.9.0](https://github.com/googleapis/gapic-generator-python/compare/v1.8.6...v1.9.0) (2023-03-17)


### Features

* Add generator option proto-plus-dep ([#1596](https://github.com/googleapis/gapic-generator-python/issues/1596)) ([1c4de67](https://github.com/googleapis/gapic-generator-python/commit/1c4de6728e02d2fa1aa2c48e1a86def6aef5c563))

## [1.8.6](https://github.com/googleapis/gapic-generator-python/compare/v1.8.5...v1.8.6) (2023-03-14)


### Bug Fixes

* Ignore_unknown_fields parsing service config ([#1618](https://github.com/googleapis/gapic-generator-python/issues/1618)) ([de6386f](https://github.com/googleapis/gapic-generator-python/commit/de6386fc0115e5a05bfc25b9a06e22eeccc091ce))

## [1.8.5](https://github.com/googleapis/gapic-generator-python/compare/v1.8.4...v1.8.5) (2023-02-23)


### Bug Fixes

* Fix mypy error with rest interceptors ([#1603](https://github.com/googleapis/gapic-generator-python/issues/1603)) ([c36876f](https://github.com/googleapis/gapic-generator-python/commit/c36876f65cc6105cb38282ca1a8680f9d220d0bd))
* Fix mypy errors in rest.py ([#1599](https://github.com/googleapis/gapic-generator-python/issues/1599)) ([120f19e](https://github.com/googleapis/gapic-generator-python/commit/120f19eef34ca3d722f079683222be99931363da))
* Resolve errors from annotating containers with non-local enums ([#1608](https://github.com/googleapis/gapic-generator-python/issues/1608)) ([73652e3](https://github.com/googleapis/gapic-generator-python/commit/73652e3b88fe30f2fca21a900b8eacbf8822d2ce))

## [1.8.4](https://github.com/googleapis/gapic-generator-python/compare/v1.8.3...v1.8.4) (2023-02-07)


### Bug Fixes

* Fix generated unit tests with repeated double ([#1582](https://github.com/googleapis/gapic-generator-python/issues/1582)) ([4c7dd53](https://github.com/googleapis/gapic-generator-python/commit/4c7dd53c9507f37b6c885c2b65b4f2cb98aad5fe))
* Fix install issue for packages without google namespace ([#1576](https://github.com/googleapis/gapic-generator-python/issues/1576)) ([862cc64](https://github.com/googleapis/gapic-generator-python/commit/862cc646c4e6d50654201fe2d7c48d5ca5bf427b))
* Use protobuf 3.21.12 in bazel build rules ([#1584](https://github.com/googleapis/gapic-generator-python/issues/1584)) ([550a5f1](https://github.com/googleapis/gapic-generator-python/commit/550a5f1b1841dd90c143466a42058b6f3c583dd2))

## [1.8.3](https://github.com/googleapis/gapic-generator-python/compare/v1.8.2...v1.8.3) (2023-02-06)


### Bug Fixes

* Raise not implemented error when REST transport is not supported ([#1578](https://github.com/googleapis/gapic-generator-python/issues/1578)) ([af6e77c](https://github.com/googleapis/gapic-generator-python/commit/af6e77c3dacaef039b1eb07ea3c9b348074d5448))

## [1.8.2](https://github.com/googleapis/gapic-generator-python/compare/v1.8.1...v1.8.2) (2023-01-23)


### Bug Fixes

* Use gapic_version from versioned module ([#1573](https://github.com/googleapis/gapic-generator-python/issues/1573)) ([dfba51a](https://github.com/googleapis/gapic-generator-python/commit/dfba51a587072a6624496d93e8ff2b5e105284f9))

## [1.8.1](https://github.com/googleapis/gapic-generator-python/compare/v1.8.0...v1.8.1) (2023-01-19)


### Bug Fixes

* Add context manager return types ([#1468](https://github.com/googleapis/gapic-generator-python/issues/1468)) ([e0b38d3](https://github.com/googleapis/gapic-generator-python/commit/e0b38d35b168dabacfa6d841b29149523e9e34ca))


### Documentation

* Add documentation for enums ([#1568](https://github.com/googleapis/gapic-generator-python/issues/1568)) ([69097ac](https://github.com/googleapis/gapic-generator-python/commit/69097acb5d102eb14579d16235a9b6b901ba14a1))

## [1.8.0](https://github.com/googleapis/gapic-generator-python/compare/v1.7.1...v1.8.0) (2023-01-09)


### Features

* Add support for python 3.11 ([#1555](https://github.com/googleapis/gapic-generator-python/issues/1555)) ([ece3686](https://github.com/googleapis/gapic-generator-python/commit/ece3686bb8dfd65686209723d9a35501bbde5773))


### Documentation

* **client:** Fix typo in get_mtls_endpoint_and_cert_source doc ([#1552](https://github.com/googleapis/gapic-generator-python/issues/1552)) ([57e8abc](https://github.com/googleapis/gapic-generator-python/commit/57e8abc5ec7e2ad430e88e68d98a56a5713acf71))
* **utils:** Fix typos in nth function docstring ([#1553](https://github.com/googleapis/gapic-generator-python/issues/1553)) ([e4be9ae](https://github.com/googleapis/gapic-generator-python/commit/e4be9aefc3ad08a6708524b1483f3abf6ce68a05))

## [1.7.1](https://github.com/googleapis/gapic-generator-python/compare/v1.7.0...v1.7.1) (2022-12-13)


### Bug Fixes

* Fix unit test with float comparison ([#1541](https://github.com/googleapis/gapic-generator-python/issues/1541)) ([c5741ff](https://github.com/googleapis/gapic-generator-python/commit/c5741ff2f0658800210060392727016d1a5b4a8b))

## [1.7.0](https://github.com/googleapis/gapic-generator-python/compare/v1.6.2...v1.7.0) (2022-12-06)


### Features

* Add snippetgen config language and testing resource files ([#1504](https://github.com/googleapis/gapic-generator-python/issues/1504)) ([5b98659](https://github.com/googleapis/gapic-generator-python/commit/5b98659816b38ab5f376a5748b6275f1c2667aaf))


### Bug Fixes

* **deps:** require google-api-core &gt;=1.34.0, >=2.11.0 ([6de9e28](https://github.com/googleapis/gapic-generator-python/commit/6de9e2881171d873ab3d76bfa386667ae745f0d9))
* Drop usage of pkg_resources ([#1471](https://github.com/googleapis/gapic-generator-python/issues/1471)) ([a50c290](https://github.com/googleapis/gapic-generator-python/commit/a50c2909b5eb14c16acaf16057944688891eb7af))
* Fix timeout default values ([6de9e28](https://github.com/googleapis/gapic-generator-python/commit/6de9e2881171d873ab3d76bfa386667ae745f0d9))
* Snippetgen should call await on the operation coroutine before calling result ([#1495](https://github.com/googleapis/gapic-generator-python/issues/1495)) ([69a49c6](https://github.com/googleapis/gapic-generator-python/commit/69a49c6b9e8a45c87e8f2a9d4b25f00b9a4b01be))

## [1.6.2](https://github.com/googleapis/gapic-generator-python/compare/v1.6.1...v1.6.2) (2022-11-15)


### Bug Fixes

* update dependency googleapis-common-protos to v1.57.0 ([786b0d4](https://github.com/googleapis/gapic-generator-python/commit/786b0d401fe6a188005b4bf076595a37821ee761))

## [1.6.1](https://github.com/googleapis/gapic-generator-python/compare/v1.6.0...v1.6.1) (2022-11-11)


### Bug Fixes

* Allow google-cloud-documentai &lt; 3 ([#1487](https://github.com/googleapis/gapic-generator-python/issues/1487)) ([b717e92](https://github.com/googleapis/gapic-generator-python/commit/b717e92f8e184edcc6e2ad3b696817435e5e37e5))
* Fix typo in testing/constraints-3.7.txt ([#1483](https://github.com/googleapis/gapic-generator-python/issues/1483)) ([0ba5bc1](https://github.com/googleapis/gapic-generator-python/commit/0ba5bc16e4ad2197cb7071a9f8c9164b1c6f080d))

## [1.6.0](https://github.com/googleapis/gapic-generator-python/compare/v1.5.0...v1.6.0) (2022-11-09)


### Features

* Add typing to proto.Message based class attributes ([#1474](https://github.com/googleapis/gapic-generator-python/issues/1474)) ([3bd2f87](https://github.com/googleapis/gapic-generator-python/commit/3bd2f8703e4a1a67e6a4c281890c4f99eda13fe7))


### Bug Fixes

* Detect changed Python files in Git pre-commit hook ([#1475](https://github.com/googleapis/gapic-generator-python/issues/1475)) ([2a232fc](https://github.com/googleapis/gapic-generator-python/commit/2a232fcc5297d6cd2ee1562c01843a3074a4da1f))
* Snippetgen handling of repeated enum field ([#1443](https://github.com/googleapis/gapic-generator-python/issues/1443)) ([70d7882](https://github.com/googleapis/gapic-generator-python/commit/70d7882b39c754ebebfd2b57fa5e89f515e3192f))

## [1.5.0](https://github.com/googleapis/gapic-generator-python/compare/v1.4.4...v1.5.0) (2022-10-17)


### Features

* Add __version__ in GAPIC clients ([#1350](https://github.com/googleapis/gapic-generator-python/issues/1350)) ([1c91347](https://github.com/googleapis/gapic-generator-python/commit/1c913476b9d2efe8a8db803bfe1d47ad8697bc72))


### Bug Fixes

* Add supported dict typing for client_options ([#1464](https://github.com/googleapis/gapic-generator-python/issues/1464)) ([de62f12](https://github.com/googleapis/gapic-generator-python/commit/de62f12b23ce8f434dd429f7761ae0001c8ad34f)), closes [#1380](https://github.com/googleapis/gapic-generator-python/issues/1380)
* Fix multiple gapic-generator-python bugs ([#1458](https://github.com/googleapis/gapic-generator-python/issues/1458)) ([ab3e361](https://github.com/googleapis/gapic-generator-python/commit/ab3e361c5e69060afb721e76e6fd4fac0d367d15))
* Snippetgen skip REST snippets ([#1463](https://github.com/googleapis/gapic-generator-python/issues/1463)) ([119a3f1](https://github.com/googleapis/gapic-generator-python/commit/119a3f18d671664309efbf1aee7bafc94b401eed))

## [1.4.4](https://github.com/googleapis/gapic-generator-python/compare/v1.4.3...v1.4.4) (2022-09-20)


### Bug Fixes

* Do not generate _flattened() unit tests for client streaming methods ([#1454](https://github.com/googleapis/gapic-generator-python/issues/1454)) ([29610ad](https://github.com/googleapis/gapic-generator-python/commit/29610ad68cfd8326e5430413d0ead1951a9b06b2))

## [1.4.3](https://github.com/googleapis/gapic-generator-python/compare/v1.4.2...v1.4.3) (2022-09-19)


### Bug Fixes

* Accept 4.x protobuf for gapic-generator-python ([#1453](https://github.com/googleapis/gapic-generator-python/issues/1453)) ([d9099dd](https://github.com/googleapis/gapic-generator-python/commit/d9099ddaff1fadb9fc3ebbab1702d50e609986cc))
* Femove `vars` and `set`from reserved names ([#1451](https://github.com/googleapis/gapic-generator-python/issues/1451)) ([ae3e6bf](https://github.com/googleapis/gapic-generator-python/commit/ae3e6bf350191cf65337a37822c6d1dff8e6dca4))

## [1.4.2](https://github.com/googleapis/gapic-generator-python/compare/v1.4.1...v1.4.2) (2022-09-13)


### Bug Fixes

* Unit test generation for boolean query prams ([#1447](https://github.com/googleapis/gapic-generator-python/issues/1447)) ([dd68dd1](https://github.com/googleapis/gapic-generator-python/commit/dd68dd1f288c4fbbdb7f54900094379ee1d771c0))

## [1.4.1](https://github.com/googleapis/gapic-generator-python/compare/v1.4.0...v1.4.1) (2022-09-09)


### Bug Fixes

* Fix test generation for `*Value` wrapper classes ([#1437](https://github.com/googleapis/gapic-generator-python/issues/1437)) ([9e9971f](https://github.com/googleapis/gapic-generator-python/commit/9e9971f6321207fe33a0d28f32a07e3b1f0e795a))
* Remove grpc only methods from rest.py ([#1440](https://github.com/googleapis/gapic-generator-python/issues/1440)) ([c12a1c2](https://github.com/googleapis/gapic-generator-python/commit/c12a1c208dc91d8b222653b0d9d9696448751c91))
* **rest:** Use strict encoding to lowercase query string bools ([#1436](https://github.com/googleapis/gapic-generator-python/issues/1436)) ([e667406](https://github.com/googleapis/gapic-generator-python/commit/e6674061ebd919281b49838f44fc0be8730595dc))

## [1.4.0](https://github.com/googleapis/gapic-generator-python/compare/v1.3.1...v1.4.0) (2022-09-07)


### Features

* Implement REST support for MixIns ([#1378](https://github.com/googleapis/gapic-generator-python/issues/1378)) ([0e38fa8](https://github.com/googleapis/gapic-generator-python/commit/0e38fa839460401453b510b616f1e22bcdead60d))

## [1.3.1](https://github.com/googleapis/gapic-generator-python/compare/v1.3.0...v1.3.1) (2022-09-07)


### Bug Fixes

* Fix LRO method test and rest test coverage ([#1433](https://github.com/googleapis/gapic-generator-python/issues/1433)) ([c57a93f](https://github.com/googleapis/gapic-generator-python/commit/c57a93fee8b7861e6396c0e34586ffa00478ce25))

## [1.3.0](https://github.com/googleapis/gapic-generator-python/compare/v1.2.0...v1.3.0) (2022-09-06)


### Features

* Add BUILD rule parameter to allow setting numeric enums ([#1411](https://github.com/googleapis/gapic-generator-python/issues/1411)) ([5c578ed](https://github.com/googleapis/gapic-generator-python/commit/5c578ed371b5f33814e67217981898bd76687184))
* Add generated sample comment ([#1417](https://github.com/googleapis/gapic-generator-python/issues/1417)) ([ef55bce](https://github.com/googleapis/gapic-generator-python/commit/ef55bce5b8e9cc5d1869fe0472d6221b58409908))
* **docker-entrypoint:** Add --experimental_allow_proto3_optional ([#1414](https://github.com/googleapis/gapic-generator-python/issues/1414)) ([b92ab8c](https://github.com/googleapis/gapic-generator-python/commit/b92ab8ce739663e9bb68fe9c736e851042301023))
* Encode numeric enums parameter with REST requests ([#1399](https://github.com/googleapis/gapic-generator-python/issues/1399)) ([63599bb](https://github.com/googleapis/gapic-generator-python/commit/63599bbeee1842f6219590bdc67498a942f3523c))
* Make REST unit tests support numeric enums ([#1423](https://github.com/googleapis/gapic-generator-python/issues/1423)) ([8839c6f](https://github.com/googleapis/gapic-generator-python/commit/8839c6fc593d62a10a069cb28f72cd76f080ecc5))
* Note that "rest" transport support is beta. ([#1403](https://github.com/googleapis/gapic-generator-python/issues/1403)) ([faba515](https://github.com/googleapis/gapic-generator-python/commit/faba515775265b21557b5820106a73a2eb8344e2))
* When requesting numeric enums in responses, also send them in requests ([#1405](https://github.com/googleapis/gapic-generator-python/issues/1405)) ([31b1b16](https://github.com/googleapis/gapic-generator-python/commit/31b1b163a0433ea22e1a7f2295b5671406feb5fa))


### Bug Fixes

* Fix remaining REST transport issues ([#1428](https://github.com/googleapis/gapic-generator-python/issues/1428)) ([d30a80e](https://github.com/googleapis/gapic-generator-python/commit/d30a80ee7e95eef90a567f80f7c7414bdb52e0ac))
* Fix REST tests generation for repeated enums ([#1421](https://github.com/googleapis/gapic-generator-python/issues/1421)) ([488ddf8](https://github.com/googleapis/gapic-generator-python/commit/488ddf8b69793274b57c2d9a76463818a3dd76bc))
* Partial rollback of https ([20c3403](https://github.com/googleapis/gapic-generator-python/commit/20c340385ae6539f86f3e0fc1d592c94c675e695))

## [1.2.0](https://github.com/googleapis/gapic-generator-python/compare/v1.1.2...v1.2.0) (2022-08-12)


### Features

* Add rest-numeric-enums option ([#1385](https://github.com/googleapis/gapic-generator-python/issues/1385)) ([099d31a](https://github.com/googleapis/gapic-generator-python/commit/099d31af79914439be0be5477a0e44ec816e9ff3))
* regenerates pb2 file with new protoc. ([#1344](https://github.com/googleapis/gapic-generator-python/issues/1344)) ([e74940f](https://github.com/googleapis/gapic-generator-python/commit/e74940f626502afd13fc5dcdde6dc4c4c11d3237))


### Bug Fixes

* Fix required fields test for REST transport ([#1389](https://github.com/googleapis/gapic-generator-python/issues/1389)) ([c3ffee8](https://github.com/googleapis/gapic-generator-python/commit/c3ffee8cf902a25a9343f0e27c9a7c28bd81f1b0))
* fixes bug in a test with explicit_routing ([#1397](https://github.com/googleapis/gapic-generator-python/issues/1397)) ([6d974a1](https://github.com/googleapis/gapic-generator-python/commit/6d974a12cb91846b40323c7aa64af50ba7410b99))
* Unit test for nested fields in url path ([#1387](https://github.com/googleapis/gapic-generator-python/issues/1387)) ([35f6fa3](https://github.com/googleapis/gapic-generator-python/commit/35f6fa30b523736d3aa0fbc17400fe0213391c74))

## [1.1.2](https://github.com/googleapis/gapic-generator-python/compare/v1.1.1...v1.1.2) (2022-07-21)


### Bug Fixes

* fix wildcard resource names helper method ([#1363](https://github.com/googleapis/gapic-generator-python/issues/1363)) ([b4ecb44](https://github.com/googleapis/gapic-generator-python/commit/b4ecb44e190005f87ccbc7d1aae6f5f2e5f20115))

## [1.1.1](https://github.com/googleapis/gapic-generator-python/compare/v1.1.0...v1.1.1) (2022-07-04)


### Bug Fixes

* resolve issue where rest test appears in grpc-only client ([#1343](https://github.com/googleapis/gapic-generator-python/issues/1343)) ([22cd2ca](https://github.com/googleapis/gapic-generator-python/commit/22cd2cafe830f383229f0e556beead05e63a055c))

## [1.1.0](https://github.com/googleapis/gapic-generator-python/compare/v1.0.1...v1.1.0) (2022-06-23)


### Features

* adds audience. ([#1312](https://github.com/googleapis/gapic-generator-python/issues/1312)) ([a2c8a1e](https://github.com/googleapis/gapic-generator-python/commit/a2c8a1e01ce62286fc6fa5017397b86abac4a054))


### Documentation

* fix changelog header to consistent size ([#1331](https://github.com/googleapis/gapic-generator-python/issues/1331)) ([8110fc6](https://github.com/googleapis/gapic-generator-python/commit/8110fc670528afacf96abb2065893ff3ed654316))

## [1.0.1](https://github.com/googleapis/gapic-generator-python/compare/v1.0.0...v1.0.1) (2022-06-10)


### Bug Fixes

* add missing metadata. ([#1335](https://github.com/googleapis/gapic-generator-python/issues/1335)) ([228efda](https://github.com/googleapis/gapic-generator-python/commit/228efdab198dd18de82df2be1b8d858b78811a89))

## [1.0.0](https://github.com/googleapis/gapic-generator-python/compare/v0.65.3...v1.0.0) (2022-05-24)


### Features

* adds LRO mixin. ([#1304](https://github.com/googleapis/gapic-generator-python/issues/1304)) ([18af90a](https://github.com/googleapis/gapic-generator-python/commit/18af90a8b51159da85f3f93bd37248a58ede4ab3))
* release as stable ([767aaba](https://github.com/googleapis/gapic-generator-python/commit/767aaba6d623fab2af972140ffd4de3b43a92439))

## [0.65.3](https://github.com/googleapis/gapic-generator-python/compare/v0.65.2...v0.65.3) (2022-05-03)


### Bug Fixes

* don't use stale session in rest transport ([#1291](https://github.com/googleapis/gapic-generator-python/issues/1291)) ([a96ef9e](https://github.com/googleapis/gapic-generator-python/commit/a96ef9ef3f99b0114f1d5630ee6e8907dd24bec2))

## [0.65.2](https://github.com/googleapis/gapic-generator-python/compare/v0.65.1...v0.65.2) (2022-04-21)


### Bug Fixes

* disambiguate method names ([#1282](https://github.com/googleapis/gapic-generator-python/issues/1282)) ([efe7216](https://github.com/googleapis/gapic-generator-python/commit/efe7216d8d59d945b4ea90ad109248b9eecc33e5))
* fixes bug when an annotation path in an http rule does not have =. ([#1284](https://github.com/googleapis/gapic-generator-python/issues/1284)) ([6dcb97c](https://github.com/googleapis/gapic-generator-python/commit/6dcb97cfb60d7d81dc205c20c762dfd5e74659e1))
* use async snippet in async client method docstring ([#1280](https://github.com/googleapis/gapic-generator-python/issues/1280)) ([b72e1e0](https://github.com/googleapis/gapic-generator-python/commit/b72e1e063d587a93b65aa77dd222341bcc87ba39))

## [0.65.1](https://github.com/googleapis/gapic-generator-python/compare/v0.65.0...v0.65.1) (2022-04-13)


### Bug Fixes

* correct import for request message type ([#1273](https://github.com/googleapis/gapic-generator-python/issues/1273)) ([3406d9e](https://github.com/googleapis/gapic-generator-python/commit/3406d9e0336d2fe698b90a95e20f6aacec79763b))
* use google-api-core==2.7.2 ([#1276](https://github.com/googleapis/gapic-generator-python/issues/1276)) ([5ab8eb5](https://github.com/googleapis/gapic-generator-python/commit/5ab8eb5a36c64e521b475cb0c045f507400d8f27))

## [0.65.0](https://github.com/googleapis/gapic-generator-python/compare/v0.64.0...v0.65.0) (2022-04-09)


### Features

* adds support for MixIns. ([#1240](https://github.com/googleapis/gapic-generator-python/issues/1240)) ([856af2e](https://github.com/googleapis/gapic-generator-python/commit/856af2ef406e0ea380fcfaa5d505435124330c25))

## [0.64.0](https://github.com/googleapis/gapic-generator-python/compare/v0.63.8...v0.64.0) (2022-04-08)


### Features

* full LRO for Extended Operations ([#1234](https://github.com/googleapis/gapic-generator-python/issues/1234)) ([4d1bccc](https://github.com/googleapis/gapic-generator-python/commit/4d1bccc965a6908e9b1aeaebf1327918f3e2042a))


### Bug Fixes

* add missing import for Mapping ([#1267](https://github.com/googleapis/gapic-generator-python/issues/1267)) ([f416622](https://github.com/googleapis/gapic-generator-python/commit/f416622c753a56036cf9ac1fa6eb818a6e557018))

## [0.63.8](https://github.com/googleapis/gapic-generator-python/compare/v0.63.7...v0.63.8) (2022-04-04)


### Bug Fixes

* **deps:** exclude click 8.1.0 ([#1255](https://github.com/googleapis/gapic-generator-python/issues/1255)) ([daf63eb](https://github.com/googleapis/gapic-generator-python/commit/daf63ebe2392fd6fde65326fffc5519cd126c2ae))
* fix docstring for map fields ([#1249](https://github.com/googleapis/gapic-generator-python/issues/1249)) ([3100464](https://github.com/googleapis/gapic-generator-python/commit/310046478092b4fc4ef9dfdd1e50363ca6fc72c5))
* sanitize file names ([#1236](https://github.com/googleapis/gapic-generator-python/issues/1236)) ([3072ffb](https://github.com/googleapis/gapic-generator-python/commit/3072ffb6000983ecb06d8dd7b44f77da61cc992e))

## [0.63.7](https://github.com/googleapis/gapic-generator-python/compare/v0.63.6...v0.63.7) (2022-03-08)


### Bug Fixes

* resolve issue where rest transport is not used in certain tests ([#1231](https://github.com/googleapis/gapic-generator-python/issues/1231)) ([90ab41a](https://github.com/googleapis/gapic-generator-python/commit/90ab41ab1f1b058ec0eb4a96b973031898f64df0))

## [0.63.6](https://github.com/googleapis/gapic-generator-python/compare/v0.63.5...v0.63.6) (2022-03-04)


### Bug Fixes

* **deps:** require google-api-core >=2.3.2 ([#1225](https://github.com/googleapis/gapic-generator-python/issues/1225)) ([f59917f](https://github.com/googleapis/gapic-generator-python/commit/f59917fdbdf5ee4091e35d721811dcd7f4b9a3f3))

## [0.63.5](https://github.com/googleapis/gapic-generator-python/compare/v0.63.4...v0.63.5) (2022-02-25)


### Bug Fixes

* update license year to 2022 ([#1199](https://github.com/googleapis/gapic-generator-python/issues/1199)) ([31292d5](https://github.com/googleapis/gapic-generator-python/commit/31292d59c8d08695f3e2dfa75861c86d723a9d35))

## [0.63.4](https://github.com/googleapis/gapic-generator-python/compare/v0.63.3...v0.63.4) (2022-02-22)


### Bug Fixes

* fix snippet region tag format ([#1210](https://github.com/googleapis/gapic-generator-python/issues/1210)) ([e895106](https://github.com/googleapis/gapic-generator-python/commit/e8951064827c726bb651801336b86188e2628386))

## [0.63.3](https://github.com/googleapis/gapic-generator-python/compare/v0.63.2...v0.63.3) (2022-02-16)


### Bug Fixes

* disambiguate field headers whose names are reserved python words ([#1178](https://github.com/googleapis/gapic-generator-python/issues/1178)) ([98aa690](https://github.com/googleapis/gapic-generator-python/commit/98aa6906031276dcad899fdb88f47cbafc651ae4))
* fix docstring code block formatting ([#1206](https://github.com/googleapis/gapic-generator-python/issues/1206)) ([500dfe7](https://github.com/googleapis/gapic-generator-python/commit/500dfe7e401888b3bea6488d6e6fee9955f1a2ab))
* HTTP body field messages with enums or recursive fields ([#1201](https://github.com/googleapis/gapic-generator-python/issues/1201)) ([246bfe2](https://github.com/googleapis/gapic-generator-python/commit/246bfe2948362bc8f6035aafc0dbd9e65f5acc2b))

## [0.63.2](https://github.com/googleapis/gapic-generator-python/compare/v0.63.1...v0.63.2) (2022-02-09)


### Bug Fixes

* fix lint sessions on generated samples ([#1192](https://github.com/googleapis/gapic-generator-python/issues/1192)) ([4d0ea18](https://github.com/googleapis/gapic-generator-python/commit/4d0ea182aa5500eee0f5485e88e14043974ae78b))

## [0.63.1](https://github.com/googleapis/gapic-generator-python/compare/v0.63.0...v0.63.1) (2022-02-03)


### Bug Fixes

* disambiguate method names that are reserved in transport classes ([#1187](https://github.com/googleapis/gapic-generator-python/issues/1187)) ([78626d8](https://github.com/googleapis/gapic-generator-python/commit/78626d89665128ef7d078ee12b49480475cce9e2))

## [0.63.0](https://github.com/googleapis/gapic-generator-python/compare/v0.62.1...v0.63.0) (2022-02-03)


### Features

* adds dynamic routing files. ([8c191a5](https://github.com/googleapis/gapic-generator-python/commit/8c191a5475f208213806fff81c0efa1d26216cd9))
* adds dynamic routing. ([#1135](https://github.com/googleapis/gapic-generator-python/issues/1135)) ([8c191a5](https://github.com/googleapis/gapic-generator-python/commit/8c191a5475f208213806fff81c0efa1d26216cd9))
* enable snippetgen for default templates ([#1171](https://github.com/googleapis/gapic-generator-python/issues/1171)) ([c1af051](https://github.com/googleapis/gapic-generator-python/commit/c1af051743dde2fb40e028c51de85dfea47a793d))

## [0.62.1](https://github.com/googleapis/gapic-generator-python/compare/v0.62.0...v0.62.1) (2022-02-02)


### Bug Fixes

* **deps:** require setuptools<=60.5.0 ([#1179](https://github.com/googleapis/gapic-generator-python/issues/1179)) ([fb56af7](https://github.com/googleapis/gapic-generator-python/commit/fb56af7cd33931f6747b5ce1fb8502bcbc74dcc7))

## [0.62.0](https://github.com/googleapis/gapic-generator-python/compare/v0.61.0...v0.62.0) (2022-01-28)


### Features

* adds REST server-streaming support. ([#1120](https://github.com/googleapis/gapic-generator-python/issues/1120)) ([812cf3e](https://github.com/googleapis/gapic-generator-python/commit/812cf3e0d11b67f7ecd60b9c643b032370bb9400))
* expose extended operations annotations within generator ([#1145](https://github.com/googleapis/gapic-generator-python/issues/1145)) ([e7bee70](https://github.com/googleapis/gapic-generator-python/commit/e7bee702e92612f88efca782a68d8884b9c71feb))


### Bug Fixes

* add special method parameters to set of reserved module names ([#1168](https://github.com/googleapis/gapic-generator-python/issues/1168)) ([8078961](https://github.com/googleapis/gapic-generator-python/commit/8078961f68d2f34fff6403d318bf95c844889d78))
* fix snippetgen golden file ([#1170](https://github.com/googleapis/gapic-generator-python/issues/1170)) ([13b2028](https://github.com/googleapis/gapic-generator-python/commit/13b2028df5193f11aee40ae42ea5186aeb25eef3))
* **snippetgen:** remove special handling for resource paths ([#1134](https://github.com/googleapis/gapic-generator-python/issues/1134)) ([4ea2d11](https://github.com/googleapis/gapic-generator-python/commit/4ea2d114b670c2f2adb43cd87e5f0cf7750e5407))

## [0.61.0](https://github.com/googleapis/gapic-generator-python/compare/v0.60.0...v0.61.0) (2022-01-28)


### Features

* add interceptor-like functionality to REST transport ([#1142](https://github.com/googleapis/gapic-generator-python/issues/1142)) ([fe57eb2](https://github.com/googleapis/gapic-generator-python/commit/fe57eb26badb596fd9bd8a0b8b65f00f060b009d))


### Bug Fixes

* preserve hyperlinks with hyphens ([#1140](https://github.com/googleapis/gapic-generator-python/issues/1140)) ([b091bfc](https://github.com/googleapis/gapic-generator-python/commit/b091bfc523ee40af4ef0b28abfc0c26dcdf09ebe)), closes [#1131](https://github.com/googleapis/gapic-generator-python/issues/1131)
* resolve DuplicateCredentialArgs when using credentials_file ([#1159](https://github.com/googleapis/gapic-generator-python/issues/1159)) ([fccd2ba](https://github.com/googleapis/gapic-generator-python/commit/fccd2ba4f67c92bce5d9f7a2d59d5f1ea28829b5))

## [0.60.0](https://github.com/googleapis/gapic-generator-python/compare/v0.59.1...v0.60.0) (2022-01-19)


### Features

* add api key support ([#969](https://github.com/googleapis/gapic-generator-python/issues/969)) ([7c72739](https://github.com/googleapis/gapic-generator-python/commit/7c7273919193f321e0dc2d4156b35be1b4733458))
* generate snippet metadata  ([#1129](https://github.com/googleapis/gapic-generator-python/issues/1129)) ([9e46031](https://github.com/googleapis/gapic-generator-python/commit/9e46031d01edc3a461140fe3b29d8d400f5ddf86))


### Bug Fixes

* only set unset fields if they are query params ([#1130](https://github.com/googleapis/gapic-generator-python/issues/1130)) ([9ad98ca](https://github.com/googleapis/gapic-generator-python/commit/9ad98ca6833f1b280bf3c04c858f92276d59ffbe))

## [0.59.1](https://github.com/googleapis/gapic-generator-python/compare/v0.59.0...v0.59.1) (2022-01-10)


### Bug Fixes

* refactor mtls logic to standalone method ([#1123](https://github.com/googleapis/gapic-generator-python/issues/1123)) ([d528223](https://github.com/googleapis/gapic-generator-python/commit/d528223e3221487f86a3d82c92cd2e2cf04bec4a))

## [0.59.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.58.4...v0.59.0) (2022-01-10)


### Features

* add snippet index ([#1121](https://www.github.com/googleapis/gapic-generator-python/issues/1121)) ([55d2bc6](https://www.github.com/googleapis/gapic-generator-python/commit/55d2bc6580e5db0f837de1b245533a8f1f2e9beb))

## [0.58.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.58.3...v0.58.4) (2021-12-30)


### Bug Fixes

* handle message bodies ([#1117](https://www.github.com/googleapis/gapic-generator-python/issues/1117)) ([36e3236](https://github.com/googleapis/gapic-generator-python/commit/36e3236b3832993331d8d99c10e72797a8851390))


## [0.58.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.58.2...v0.58.3) (2021-12-28)


### Bug Fixes

* add additional reserved names for disambiguation ([#1114](https://www.github.com/googleapis/gapic-generator-python/issues/1114)) ([1cffd8d](https://www.github.com/googleapis/gapic-generator-python/commit/1cffd8d99936cd10649faf05e0288b693e718f81))

## [0.58.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.58.1...v0.58.2) (2021-12-13)


### Bug Fixes

* fix case for expected field names in required fields test. ([#1107](https://www.github.com/googleapis/gapic-generator-python/issues/1107)) ([6a593f9](https://www.github.com/googleapis/gapic-generator-python/commit/6a593f9807141aaf6c13a8843804e9fa9b300c91))
* non-string required fields provide correct values ([#1108](https://www.github.com/googleapis/gapic-generator-python/issues/1108)) ([bc5f729](https://www.github.com/googleapis/gapic-generator-python/commit/bc5f729cf777d30e1053e23a1d115460952478af))
* syntax fix and test for multiple required fields ([#1105](https://www.github.com/googleapis/gapic-generator-python/issues/1105)) ([4e5fe2d](https://www.github.com/googleapis/gapic-generator-python/commit/4e5fe2db9d0d81929cc1559d3a134c9a38ae595c))

## [0.58.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.58.0...v0.58.1) (2021-12-09)


### Bug Fixes

* syntax fix for required_fields struct in rest transport ([#1103](https://www.github.com/googleapis/gapic-generator-python/issues/1103)) ([3d7128c](https://www.github.com/googleapis/gapic-generator-python/commit/3d7128ce8f55523b9aff2e44e2c000450e712ac2))

## [0.58.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.57.0...v0.58.0) (2021-12-07)


### Features

* add support for long-running operations with rest transport. ([#1094](https://www.github.com/googleapis/gapic-generator-python/issues/1094)) ([e89fd23](https://www.github.com/googleapis/gapic-generator-python/commit/e89fd23609625c5aa49acd6c6ee67f87fce324fd))


### Bug Fixes

* ensure rest unit tests have complete coverage ([#1098](https://www.github.com/googleapis/gapic-generator-python/issues/1098)) ([0705d9c](https://www.github.com/googleapis/gapic-generator-python/commit/0705d9c5dbbea793867551e64991be37d8339c6b))
* fix resource path args for paths with =** ([#1089](https://www.github.com/googleapis/gapic-generator-python/issues/1089)) ([309cc66](https://www.github.com/googleapis/gapic-generator-python/commit/309cc66e880e07940866864b03c744310ef56762))
* **snippetgen:** don't create duplicate requests for required oneofs ([#1088](https://www.github.com/googleapis/gapic-generator-python/issues/1088)) ([5531795](https://www.github.com/googleapis/gapic-generator-python/commit/55317956397370a91b1a06ecd476e55f58789807))

## [0.57.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.56.2...v0.57.0) (2021-11-17)


### Features

* forward compatible diregapic LRO support ([#1085](https://www.github.com/googleapis/gapic-generator-python/issues/1085)) ([aa7f4d5](https://www.github.com/googleapis/gapic-generator-python/commit/aa7f4d568f7f43738ab3489fc84ce6bc5d6bda18))

## [0.56.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.56.1...v0.56.2) (2021-11-08)


### Bug Fixes

* don't enable snippetgen by default ([#1078](https://www.github.com/googleapis/gapic-generator-python/issues/1078)) ([8bdb709](https://www.github.com/googleapis/gapic-generator-python/commit/8bdb70931a9ecb1c89fda9608697b0762770bc12))

## [0.56.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.56.0...v0.56.1) (2021-11-08)


### Bug Fixes

* **snippetgen:** fix client streaming samples ([#1061](https://www.github.com/googleapis/gapic-generator-python/issues/1061)) ([64b9ad6](https://www.github.com/googleapis/gapic-generator-python/commit/64b9ad6e417a15cfbddf0e7a1b57036b8abfc829))

## [0.56.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.55.1...v0.56.0) (2021-11-05)


### Features

* **snippetgen:** turn resource path strings into f-strings ([#1012](https://www.github.com/googleapis/gapic-generator-python/issues/1012)) ([a110e1d](https://www.github.com/googleapis/gapic-generator-python/commit/a110e1d8387ea37b85ab0621bacd30da175fe85b))


### Bug Fixes

* fix rest unit test ([#1074](https://www.github.com/googleapis/gapic-generator-python/issues/1074)) ([3b2918e](https://www.github.com/googleapis/gapic-generator-python/commit/3b2918ecaeb90229f22834438dc31755498ee2d0))

## [0.55.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.55.0...v0.55.1) (2021-11-04)


### Bug Fixes

* fix missing http schema (http/https) for REST clients ([#1063](https://www.github.com/googleapis/gapic-generator-python/issues/1063)) ([e3aa7a0](https://www.github.com/googleapis/gapic-generator-python/commit/e3aa7a0b23bc4bfd5170753f74bdeac219902d1a))
* handle required fields properly in query_params ([#1068](https://www.github.com/googleapis/gapic-generator-python/issues/1068)) ([0e379ca](https://www.github.com/googleapis/gapic-generator-python/commit/0e379ca6c0aee9d79d11a14074b7e9343e9e6af2))
* leave a newline between field description and oneof line ([#1071](https://www.github.com/googleapis/gapic-generator-python/issues/1071)) ([4d0e365](https://www.github.com/googleapis/gapic-generator-python/commit/4d0e36528a8eb23ea3893b0bbcca10b679867445))
* suppress type error for fallback def of OptionalRetry ([#1065](https://www.github.com/googleapis/gapic-generator-python/issues/1065)) ([e47faa6](https://www.github.com/googleapis/gapic-generator-python/commit/e47faa6c59a1fadf7dfebc965c962aa05ca30f74))
* unignore 'google.api_core' imports ([#1066](https://www.github.com/googleapis/gapic-generator-python/issues/1066)) ([13f764c](https://www.github.com/googleapis/gapic-generator-python/commit/13f764c6513b91e7143a4a4a0bcc661cd19be0d8))
* use (new) typing for 'gapic_v1.method.DEFAULT' ([#1032](https://www.github.com/googleapis/gapic-generator-python/issues/1032)) ([d85dfad](https://www.github.com/googleapis/gapic-generator-python/commit/d85dfadc180e5f218ad582a306c1c441a6c668db))

## [0.55.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.54.0...v0.55.0) (2021-11-01)


### Features

* add fragment tests ([#1056](https://www.github.com/googleapis/gapic-generator-python/issues/1056)) ([9d9b33d](https://www.github.com/googleapis/gapic-generator-python/commit/9d9b33dadf587a6d0b09031edeea597d6d2eae62))

## [0.54.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.53.4...v0.54.0) (2021-10-29)


### Features

* generate code snippets by default ([#1044](https://www.github.com/googleapis/gapic-generator-python/issues/1044)) ([e46f443](https://www.github.com/googleapis/gapic-generator-python/commit/e46f443dbeffe16b63f97668801b06189769e972))

## [0.53.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.53.3...v0.53.4) (2021-10-29)


### Bug Fixes

* add 'dict' type annotation to 'request' for async_client ([#1051](https://www.github.com/googleapis/gapic-generator-python/issues/1051)) ([08cc2c4](https://www.github.com/googleapis/gapic-generator-python/commit/08cc2c4c85297759892782e307bcaa63dff41212))
* fix tests generation logic ([#1049](https://www.github.com/googleapis/gapic-generator-python/issues/1049)) ([8f213ad](https://www.github.com/googleapis/gapic-generator-python/commit/8f213add4cb02366bb370ef46a686c6f0c37a575))
* methods returning Operation w/o operation_info are now allowed. ([#1047](https://www.github.com/googleapis/gapic-generator-python/issues/1047)) ([6b640af](https://www.github.com/googleapis/gapic-generator-python/commit/6b640afbd93ea8c861b902211dc34e188234d072))

## [0.53.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.53.2...v0.53.3) (2021-10-27)


### Bug Fixes

* more fixes for rest transport ([#1042](https://www.github.com/googleapis/gapic-generator-python/issues/1042)) ([13d5f77](https://www.github.com/googleapis/gapic-generator-python/commit/13d5f77f8b6d4ce1181b29f2335d7584783be753))

## [0.53.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.53.1...v0.53.2) (2021-10-27)


### Bug Fixes

* Adjust Field Names in URI Templates ([#1041](https://www.github.com/googleapis/gapic-generator-python/issues/1041)) ([06cd7b6](https://www.github.com/googleapis/gapic-generator-python/commit/06cd7b66f0f303b066f7f1f510332ae19aa9de8e))
* Fix rest transport logic ([#1039](https://www.github.com/googleapis/gapic-generator-python/issues/1039)) ([50d61af](https://www.github.com/googleapis/gapic-generator-python/commit/50d61afd30b021835fe898e41b783f4d04acff09))
* list oneofs in docstring ([#1030](https://www.github.com/googleapis/gapic-generator-python/issues/1030)) ([a0e25c8](https://www.github.com/googleapis/gapic-generator-python/commit/a0e25c8c00391b99a351e667eddc8b4fecad30d8))

## [0.53.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.53.0...v0.53.1) (2021-10-13)


### Bug Fixes

* use correct typing for retries / operations_client ([#1026](https://www.github.com/googleapis/gapic-generator-python/issues/1026)) ([acb3ea8](https://www.github.com/googleapis/gapic-generator-python/commit/acb3ea83becf6bf85c142739dede556cae2cebae))

## [0.53.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.52.0...v0.53.0) (2021-10-04)


### Features

* add support for context manager in client ([#987](https://www.github.com/googleapis/gapic-generator-python/issues/987)) ([4edabcf](https://www.github.com/googleapis/gapic-generator-python/commit/4edabcf6791cfb0874a951b695b39672036760d4))
* enable self signed jwt for http ([#1000](https://www.github.com/googleapis/gapic-generator-python/issues/1000)) ([5f87973](https://www.github.com/googleapis/gapic-generator-python/commit/5f8797396a2477b772b7bfb827499db32e28710e))
* implement grpc transcode for rest transport and complete generated tests ([#999](https://www.github.com/googleapis/gapic-generator-python/issues/999)) ([ccdd17d](https://www.github.com/googleapis/gapic-generator-python/commit/ccdd17d6133274a34dd727fab0576e6c63238833))
* implement grpc transcode for rest transport and complete generated tests. ([ccdd17d](https://www.github.com/googleapis/gapic-generator-python/commit/ccdd17d6133274a34dd727fab0576e6c63238833))


### Bug Fixes

* fix docstring for first attribute of protos ([#1004](https://www.github.com/googleapis/gapic-generator-python/issues/1004)) ([383f655](https://www.github.com/googleapis/gapic-generator-python/commit/383f6555a1d850889b2aa74be28c8d06465399e5))

## [0.52.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.51.2...v0.52.0) (2021-09-29)


### Features

* Support alternative http bindings in the gapic schema. ([#993](https://www.github.com/googleapis/gapic-generator-python/issues/993)) ([041a726](https://www.github.com/googleapis/gapic-generator-python/commit/041a726b818cd67812d689c23757f31ec9964d66))


### Bug Fixes

* improper types in pagers generation ([#970](https://www.github.com/googleapis/gapic-generator-python/issues/970)) ([bba3eea](https://www.github.com/googleapis/gapic-generator-python/commit/bba3eea5d45fe57c0395ceef30402ad7880013d7))

## [0.51.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.51.1...v0.51.2) (2021-09-13)


### Bug Fixes

* add a separate DEFAULT_CLIENT_INFO for rest clients ([#988](https://www.github.com/googleapis/gapic-generator-python/issues/988)) ([22ac400](https://www.github.com/googleapis/gapic-generator-python/commit/22ac40097ab50bb2d3a7f1a2d35d659c391e0927))
* **snippetgen:** use f-strings in print statements ([#975](https://www.github.com/googleapis/gapic-generator-python/issues/975)) ([122e85c](https://www.github.com/googleapis/gapic-generator-python/commit/122e85c37ff6aa0a99f64361397eb3df5495a3b4))

## [0.51.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.51.0...v0.51.1) (2021-08-20)


### Bug Fixes

* timeouts are handled by rest clients, retries silently ignored ([#976](https://www.github.com/googleapis/gapic-generator-python/issues/976)) ([a62463c](https://www.github.com/googleapis/gapic-generator-python/commit/a62463cadee0cdaf861e93998faa27e6a82adab4))

## [0.51.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.50.5...v0.51.0) (2021-08-18)


### Features

* **snippetgen:** generate mock input for required fields ([#941](https://www.github.com/googleapis/gapic-generator-python/issues/941)) ([b2149da](https://www.github.com/googleapis/gapic-generator-python/commit/b2149da5e6873e1f71871bfecd899bb9aa0b6439))


### Bug Fixes

* add 'dict' type annotation to 'request' ([#966](https://www.github.com/googleapis/gapic-generator-python/issues/966)) ([49205d9](https://www.github.com/googleapis/gapic-generator-python/commit/49205d99dd440690b838c8eb3f6a695f35b061c2))

## [0.50.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.50.4...v0.50.5) (2021-07-22)


### Bug Fixes

* enable self signed jwt for grpc ([#958](https://www.github.com/googleapis/gapic-generator-python/issues/958)) ([af02a9c](https://www.github.com/googleapis/gapic-generator-python/commit/af02a9cae522ff2cdc8e97cfffe2ba2bb84d6b6a))
* fix rest transport unit test and required query prams handling ([#951](https://www.github.com/googleapis/gapic-generator-python/issues/951)) ([b793017](https://www.github.com/googleapis/gapic-generator-python/commit/b7930177da9a8be556bf6485febcc0a9bdef897b))

## [0.50.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.50.3...v0.50.4) (2021-06-30)


### Bug Fixes

* fix syntax for Deprecationwarning ([#942](https://www.github.com/googleapis/gapic-generator-python/issues/942)) ([82dbddb](https://www.github.com/googleapis/gapic-generator-python/commit/82dbddb6a9caf1227c4b335345f365dd01025794))

## [0.50.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.50.2...v0.50.3) (2021-06-29)


### Bug Fixes

* disable always_use_jwt_access ([#939](https://www.github.com/googleapis/gapic-generator-python/issues/939)) ([1302352](https://www.github.com/googleapis/gapic-generator-python/commit/130235220849987df572c1840735b3c199b85dfc))

## [0.50.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.50.1...v0.50.2) (2021-06-28)


### Bug Fixes

* fix wrong scopes for self signed jwt ([#935](https://www.github.com/googleapis/gapic-generator-python/issues/935)) ([e033acd](https://www.github.com/googleapis/gapic-generator-python/commit/e033acd44763f7cf65eabb6b35f66093022b1bcb))
* import warnings when needed ([#930](https://www.github.com/googleapis/gapic-generator-python/issues/930)) ([d4270ae](https://www.github.com/googleapis/gapic-generator-python/commit/d4270ae5805f44ab8ee30bb11fe42a0da6d79755))

## [0.50.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.50.0...v0.50.1) (2021-06-24)


### Bug Fixes

* **bazel:** Re-enable Python µgen integration tests post monolith rule removal ([#926](https://www.github.com/googleapis/gapic-generator-python/issues/926)) ([13a6b3a](https://www.github.com/googleapis/gapic-generator-python/commit/13a6b3aed35b5af85aea047922aa219258460a58))

## [0.50.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.49.0...v0.50.0) (2021-06-21)


### Features

* enable self signed jwt for grpc ([#920](https://www.github.com/googleapis/gapic-generator-python/issues/920)) ([da119c7](https://www.github.com/googleapis/gapic-generator-python/commit/da119c72c82d04e168c4b41e5bf910a0c1609ce3))


### Bug Fixes

* **bazel:** Remove monolith imports from Python µgen Bazel rules ([#923](https://www.github.com/googleapis/gapic-generator-python/issues/923)) ([4a2afa7](https://www.github.com/googleapis/gapic-generator-python/commit/4a2afa78455817e7e6c058d21857326867fe3f21))
* temporarily disable code coverage in showcase_unit tests ([#925](https://www.github.com/googleapis/gapic-generator-python/issues/925)) ([0dfac03](https://www.github.com/googleapis/gapic-generator-python/commit/0dfac03bd3ef8c12b33e6c03e62eab3e7bf2cd69))

## [0.49.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.48.1...v0.49.0) (2021-06-11)


### Features

* add async samples ([#861](https://www.github.com/googleapis/gapic-generator-python/issues/861)) ([e385ffd](https://www.github.com/googleapis/gapic-generator-python/commit/e385ffd7f012c6a38c9fcd7c5f36ce090311032b))

## [0.48.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.48.0...v0.48.1) (2021-06-09)


### Bug Fixes

* samplegen always produces sample dicts with "response" ([#914](https://www.github.com/googleapis/gapic-generator-python/issues/914)) ([0b168f2](https://www.github.com/googleapis/gapic-generator-python/commit/0b168f20f4cbf419131fcc512141fccca8186681))

## [0.48.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.47.0...v0.48.0) (2021-05-27)


### Features

* Add `x-goog-api-client` header to rest clients ([#888](https://www.github.com/googleapis/gapic-generator-python/issues/888)) ([2d1d3ae](https://www.github.com/googleapis/gapic-generator-python/commit/2d1d3ae135a75bbfff13df7703de5d0dad44695c))
* **dev:** Add Git pre-commit hooks [gapic-generator-python] ([#908](https://www.github.com/googleapis/gapic-generator-python/issues/908)) ([298db39](https://www.github.com/googleapis/gapic-generator-python/commit/298db39064e29de764537f25dc38f9e5ac301390))
* Raise GoogleAPICallError on REST response errors ([#891](https://www.github.com/googleapis/gapic-generator-python/issues/891)) ([edb8c63](https://www.github.com/googleapis/gapic-generator-python/commit/edb8c63e8a331f5e08ea19202d8de42de7051299))
* **tests:** Add integration test framework, goldens for 4 APIs [gapic-generator-python] ([#905](https://www.github.com/googleapis/gapic-generator-python/issues/905)) ([48db1e6](https://www.github.com/googleapis/gapic-generator-python/commit/48db1e644badc2180253e11d9a3d3657e8f9aeed))


### Bug Fixes

* fix datetime comparison unit tests ([#898](https://www.github.com/googleapis/gapic-generator-python/issues/898)) ([81932a2](https://www.github.com/googleapis/gapic-generator-python/commit/81932a2b71e6ca5f424ddc5c52933ad1d452583a))
* remove support for google-api-core<1.26.0 ([#893](https://www.github.com/googleapis/gapic-generator-python/issues/893)) ([ce558ac](https://www.github.com/googleapis/gapic-generator-python/commit/ce558acef9ec9c9bcc54243cddb708ef168c05f0))


### Documentation

* Add DEVELOPMENT.md ([#876](https://www.github.com/googleapis/gapic-generator-python/issues/876)) ([592ec06](https://www.github.com/googleapis/gapic-generator-python/commit/592ec061d4eec35e35633c5a9e62cf1e598a8461))

## [0.47.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.46.3...v0.47.0) (2021-05-13)


### Features

* support protobuf method deprecation option [gapic-generator-python] ([#875](https://www.github.com/googleapis/gapic-generator-python/issues/875)) ([5a5a839](https://www.github.com/googleapis/gapic-generator-python/commit/5a5a839b99d78ec5a5c52452e57c289b55ad1db5))

## [0.46.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.46.2...v0.46.3) (2021-05-12)


### Bug Fixes

* consistently use _pb2 identifier ([#883](https://www.github.com/googleapis/gapic-generator-python/issues/883)) ([d789c84](https://www.github.com/googleapis/gapic-generator-python/commit/d789c84d0d686bdb2d88179041b4c04cc32a3e66))

## [0.46.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.46.1...v0.46.2) (2021-05-12)


### Bug Fixes

* fix incorrectly referenced exceptions, add missing port to tests ([#873](https://www.github.com/googleapis/gapic-generator-python/issues/873)) ([40078c4](https://www.github.com/googleapis/gapic-generator-python/commit/40078c46b21a0dfa489d4cd80ed7d95bb542f3c3)), closes [#872](https://www.github.com/googleapis/gapic-generator-python/issues/872)

## [0.46.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.46.0...v0.46.1) (2021-05-07)


### Bug Fixes

* also add the async client to __all__ ([#869](https://www.github.com/googleapis/gapic-generator-python/issues/869)) ([09c90fa](https://www.github.com/googleapis/gapic-generator-python/commit/09c90fa48515cb7da1d0ebf1d93a0d49fc6448e8))

## [0.46.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.45.2...v0.46.0) (2021-05-07)


### Features

* Support field presence for query parameters in REST clients ([#866](https://www.github.com/googleapis/gapic-generator-python/issues/866)) ([5339db1](https://www.github.com/googleapis/gapic-generator-python/commit/5339db1308326d91a05a34d38e31cf91b79a9225))


### Bug Fixes

* Check for default value presence for non-optional fields in REST ([#868](https://www.github.com/googleapis/gapic-generator-python/issues/868)) ([5748001](https://www.github.com/googleapis/gapic-generator-python/commit/57480019c3e77c6b3a85bdaf8441334170b318e8))

## [0.45.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.45.1...v0.45.2) (2021-05-06)


### Bug Fixes

* remove extra space before_pb_options ([#863](https://www.github.com/googleapis/gapic-generator-python/issues/863)) ([f0532e7](https://www.github.com/googleapis/gapic-generator-python/commit/f0532e7a88479aeb805c1509239008bdd19e9d85))

## [0.45.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.45.0...v0.45.1) (2021-05-04)


### Bug Fixes

* add async client to %name_%version/__init__.py ([#859](https://www.github.com/googleapis/gapic-generator-python/issues/859)) ([391fdb8](https://www.github.com/googleapis/gapic-generator-python/commit/391fdb84b13c5628c21d81ad311c689da8971f6a))

## [0.45.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.44.3...v0.45.0) (2021-05-03)


### Features

* add autogenerated snippets ([#845](https://www.github.com/googleapis/gapic-generator-python/issues/845)) ([abdf5ec](https://www.github.com/googleapis/gapic-generator-python/commit/abdf5ec00261e5500dbdd190c23b0b2b05836799))

## [0.44.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.44.2...v0.44.3) (2021-05-03)


### Performance Improvements

* reduce unnecessary copies, optimize Address comparison ([#855](https://www.github.com/googleapis/gapic-generator-python/issues/855)) ([e843540](https://www.github.com/googleapis/gapic-generator-python/commit/e8435400257707458e83424019c9b1a16fac9a99))

## [0.44.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.44.1...v0.44.2) (2021-04-30)


### Bug Fixes

* remove auth, policy, and options from the reserved names list ([#851](https://www.github.com/googleapis/gapic-generator-python/issues/851)) ([d3f31a0](https://www.github.com/googleapis/gapic-generator-python/commit/d3f31a0d33411b3248871ddbe51135e83b699a73))

## [0.44.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.44.0...v0.44.1) (2021-04-28)


### Bug Fixes

* fix syntax errors and failing unit tests ([#849](https://www.github.com/googleapis/gapic-generator-python/issues/849)) ([9046261](https://www.github.com/googleapis/gapic-generator-python/commit/90462617e3e2b90eb8684210b6a70e890bdc0d96)), closes [#848](https://www.github.com/googleapis/gapic-generator-python/issues/848)

## [0.44.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.43.3...v0.44.0) (2021-04-23)


### Features

* support self-signed JWT flow for service accounts ([#774](https://www.github.com/googleapis/gapic-generator-python/issues/774)) ([89d6f35](https://www.github.com/googleapis/gapic-generator-python/commit/89d6f35c54b0a9b81c9b5f580d2e9eb87352ed93))


### Bug Fixes

* enable GAPIC metadata generation ([#843](https://www.github.com/googleapis/gapic-generator-python/issues/843)) ([697816c](https://www.github.com/googleapis/gapic-generator-python/commit/697816ce7d5b201d6ced85fadd89f9140da67b37))

## [0.43.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.43.2...v0.43.3) (2021-04-12)


### Bug Fixes

* sort subpackages in %namespace/%name/__init__.py ([#836](https://www.github.com/googleapis/gapic-generator-python/issues/836)) ([90cf882](https://www.github.com/googleapis/gapic-generator-python/commit/90cf882b20f430499f692e6b9b23497b3555e928))

## [0.43.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.43.1...v0.43.2) (2021-03-24)


### Bug Fixes

* add certain raw imports to RESERVED_NAMES ([#824](https://www.github.com/googleapis/gapic-generator-python/issues/824)) ([04bd8aa](https://www.github.com/googleapis/gapic-generator-python/commit/04bd8aaf0fc2c2c0615105cab39dc33266b66775))
* Update module alias to resolve naming conflict ([#820](https://www.github.com/googleapis/gapic-generator-python/issues/820)) ([f5e9f36](https://www.github.com/googleapis/gapic-generator-python/commit/f5e9f367ec6a72b4272f559a93f6fbb3d7e54b8b)), closes [#819](https://www.github.com/googleapis/gapic-generator-python/issues/819)

## [0.43.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.43.0...v0.43.1) (2021-03-19)


### Bug Fixes

* use correct retry deadline in publisher methods ([#814](https://www.github.com/googleapis/gapic-generator-python/issues/814)) ([92a2cfc](https://www.github.com/googleapis/gapic-generator-python/commit/92a2cfc47b24c4b1a041d5bbb944d69a67a962a2))

## [0.43.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.42.2...v0.43.0) (2021-03-11)


### Features

* add bazel support for gapic metadata ([#811](https://www.github.com/googleapis/gapic-generator-python/issues/811)) ([7ced24a](https://www.github.com/googleapis/gapic-generator-python/commit/7ced24a0b20cb6505587b946c03b1b038eef4b4a))
* update templates to permit enum aliases ([#809](https://www.github.com/googleapis/gapic-generator-python/issues/809)) ([2e7ea11](https://www.github.com/googleapis/gapic-generator-python/commit/2e7ea11f80210459106f9780e5f013e2a0381d29))

## [0.42.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.42.1...v0.42.2) (2021-03-05)


### Bug Fixes

* s/grpcAsync/grpc-async for gapic metadata ([#803](https://www.github.com/googleapis/gapic-generator-python/issues/803)) ([96f7864](https://www.github.com/googleapis/gapic-generator-python/commit/96f78640d90cf50c6b525924d14c6afe31874be6))

## [0.42.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.42.0...v0.42.1) (2021-03-04)


### Bug Fixes

* corner case fix for empty request generated test ([#801](https://www.github.com/googleapis/gapic-generator-python/issues/801)) ([039dc71](https://www.github.com/googleapis/gapic-generator-python/commit/039dc713fed291142058741e1138da5a4bec542f))

## [0.42.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.41.0...v0.42.0) (2021-03-03)


### Features

* add flag for gapic metadata ([#795](https://www.github.com/googleapis/gapic-generator-python/issues/795)) ([9cd7664](https://www.github.com/googleapis/gapic-generator-python/commit/9cd7664141835edcd8970629d9cf3abe4b7fd7c4))

## [0.41.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.12...v0.41.0) (2021-03-02)


### Features

* add gapic metadata file ([#781](https://www.github.com/googleapis/gapic-generator-python/issues/781)) ([5dd8fcc](https://www.github.com/googleapis/gapic-generator-python/commit/5dd8fccf6b4da57edef0347beb07102634daa992))

## [0.40.12](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.11...v0.40.12) (2021-02-26)


### Bug Fixes

* exclude 'input' from reserved names list ([#788](https://www.github.com/googleapis/gapic-generator-python/issues/788)) ([da2ff71](https://www.github.com/googleapis/gapic-generator-python/commit/da2ff717b82357359baeeafad9a3e48a70e194cb))

## [0.40.11](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.10...v0.40.11) (2021-02-24)


### Bug Fixes

* remove duplicate field entries ([#786](https://www.github.com/googleapis/gapic-generator-python/issues/786)) ([9f4dfa4](https://www.github.com/googleapis/gapic-generator-python/commit/9f4dfa46cb6a67081563ce096452fedd9e35051d))

## [0.40.10](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.9...v0.40.10) (2021-02-17)


### Bug Fixes

* ignore unknown fields returned from server for REST ([#777](https://www.github.com/googleapis/gapic-generator-python/issues/777)) ([a70b078](https://www.github.com/googleapis/gapic-generator-python/commit/a70b0787f7e3d40642a4f68574f0cc493cc4e054))

## [0.40.9](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.8...v0.40.9) (2021-02-10)


### Bug Fixes

* fix rest transport tests ([#772](https://www.github.com/googleapis/gapic-generator-python/issues/772)) ([ce110a3](https://www.github.com/googleapis/gapic-generator-python/commit/ce110a35894aa1a838649f9782294b3b8446be5c))

## [0.40.8](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.7...v0.40.8) (2021-02-05)


### Bug Fixes

* body encoding for rest transport ([#768](https://www.github.com/googleapis/gapic-generator-python/issues/768)) ([cc55a18](https://www.github.com/googleapis/gapic-generator-python/commit/cc55a182b878d78f92aba259c067d47ab1d01e5b))
* update paging implementation to handle unconventional pagination ([#750](https://www.github.com/googleapis/gapic-generator-python/issues/750)) ([eaac3e6](https://www.github.com/googleapis/gapic-generator-python/commit/eaac3e69d366b610ae7551d94d4f546819e24bc2))

## [0.40.7](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.6...v0.40.7) (2021-02-03)


### Bug Fixes

* don't use integer for enums in json encoding ([#761](https://www.github.com/googleapis/gapic-generator-python/issues/761)) ([6d37a73](https://www.github.com/googleapis/gapic-generator-python/commit/6d37a7388995b90428ee6293bcce5d48cd9a48f8))

## [0.40.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.5...v0.40.6) (2021-02-02)


### Bug Fixes

* remove duplicate assignment of certain flattened, repeated fields ([#760](https://www.github.com/googleapis/gapic-generator-python/issues/760)) ([cdbc221](https://www.github.com/googleapis/gapic-generator-python/commit/cdbc22130a176e733c529f60a6b8b1d224e82e89))

## [0.40.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.4...v0.40.5) (2021-02-01)


### Bug Fixes

* Fix namespace packages conflict issue ([#757](https://www.github.com/googleapis/gapic-generator-python/issues/757)) ([8035662](https://www.github.com/googleapis/gapic-generator-python/commit/8035662bdcfbdffd1c294c5d28479733358407ca))

## [0.40.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.3...v0.40.4) (2021-01-28)


### Bug Fixes

* Make gapic-generator-python compatible with protobuf 3.14.0 (packaged as native namespace package) ([#753](https://www.github.com/googleapis/gapic-generator-python/issues/753)) ([45212af](https://www.github.com/googleapis/gapic-generator-python/commit/45212afb9f523a416d86272798d71ce05dc292f0))
* mypy 0.800 update errors ([#754](https://www.github.com/googleapis/gapic-generator-python/issues/754)) ([608275a](https://www.github.com/googleapis/gapic-generator-python/commit/608275aa923f495520dea8ebddb94a99f26e27a5))

## [0.40.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.2...v0.40.3) (2021-01-21)


### Bug Fixes

* stabilize order of query_params ([#742](https://www.github.com/googleapis/gapic-generator-python/issues/742)) ([2835ddb](https://www.github.com/googleapis/gapic-generator-python/commit/2835ddbe62b520e2e4c84f02810b1ac936c9cbb9))

## [0.40.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.1...v0.40.2) (2021-01-21)


### Bug Fixes

* fix rest transport unit test template ([#741](https://www.github.com/googleapis/gapic-generator-python/issues/741)) ([54b9806](https://www.github.com/googleapis/gapic-generator-python/commit/54b98060f881c8f0424c7e146488d3adc19fec7a))

## [0.40.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.40.0...v0.40.1) (2021-01-20)


### Bug Fixes

* raise for rest transport http error ([#738](https://www.github.com/googleapis/gapic-generator-python/issues/738)) ([7d24f3d](https://www.github.com/googleapis/gapic-generator-python/commit/7d24f3d81499ad714e57c7c9562b842c09e49d20))

## [0.40.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.39.1...v0.40.0) (2021-01-19)


### Features

* add mtls feature to rest transport ([#731](https://www.github.com/googleapis/gapic-generator-python/issues/731)) ([524dbab](https://www.github.com/googleapis/gapic-generator-python/commit/524dbab16d248198ca10a08ecede4600fd36cefc))

## [0.39.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.39.0...v0.39.1) (2021-01-05)


### Bug Fixes

* fix missing .coveragerc and the broken bazel build ([#723](https://www.github.com/googleapis/gapic-generator-python/issues/723)) ([7f8235f](https://www.github.com/googleapis/gapic-generator-python/commit/7f8235f6dfbd309a879895701aeb5e73c6425483))
* Update gapic-generator-python to gracefully handle internal google inconsistencies ([#721](https://www.github.com/googleapis/gapic-generator-python/issues/721)) ([b984295](https://www.github.com/googleapis/gapic-generator-python/commit/b9842952433924a1d8de4ef9cc3ea9e7fa91c01a))
* updating testing, rest-only generation, & minor bug-fixes ([#716](https://www.github.com/googleapis/gapic-generator-python/issues/716)) ([56c31de](https://www.github.com/googleapis/gapic-generator-python/commit/56c31de4a9f661e3d69b52e19c9a28dddfe9d7dc))

## [0.39.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.38.0...v0.39.0) (2020-12-22)


### Features

* allow warehouse name to be customized ([#717](https://www.github.com/googleapis/gapic-generator-python/issues/717)) ([7c185e8](https://www.github.com/googleapis/gapic-generator-python/commit/7c185e87cb4252b1f99ed121515814595f9492c4)), closes [#605](https://www.github.com/googleapis/gapic-generator-python/issues/605)


### Bug Fixes

* fix sphinx identifiers ([#714](https://www.github.com/googleapis/gapic-generator-python/issues/714)) ([39be474](https://www.github.com/googleapis/gapic-generator-python/commit/39be474b4419dfa521ef51927fd36dbf257d68e3)), closes [#625](https://www.github.com/googleapis/gapic-generator-python/issues/625) [#604](https://www.github.com/googleapis/gapic-generator-python/issues/604)

## [0.38.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.37.1...v0.38.0) (2020-12-16)


### Features

* add 'from_service_account_info' factory to clients ([#706](https://www.github.com/googleapis/gapic-generator-python/issues/706)) ([94d5f0c](https://www.github.com/googleapis/gapic-generator-python/commit/94d5f0c11b8041cbae8e4a89bb504d6c6e200a95)), closes [#705](https://www.github.com/googleapis/gapic-generator-python/issues/705)

## [0.37.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.37.0...v0.37.1) (2020-12-10)


### Bug Fixes

* remove client recv msg limit ([#704](https://www.github.com/googleapis/gapic-generator-python/issues/704)) ([80147ce](https://www.github.com/googleapis/gapic-generator-python/commit/80147ce177ce435dcb1b611181e80dc35f915293))

## [0.37.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.36.0...v0.37.0) (2020-12-08)


### Features

* add proper handling of query/path/body parameters for rest transport ([#702](https://www.github.com/googleapis/gapic-generator-python/issues/702)) ([6b2de5d](https://www.github.com/googleapis/gapic-generator-python/commit/6b2de5dd9fbf15e6b0a42b428b01eb03f1a3820a))

## [0.36.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.11...v0.36.0) (2020-11-14)


### Features

* add rest transport generation for clients with optional transport flag ([#688](https://www.github.com/googleapis/gapic-generator-python/issues/688)) ([af59c2c](https://www.github.com/googleapis/gapic-generator-python/commit/af59c2c3c3d6b7e1f626c3fbc2c03f99ca31b4a4))

## [0.35.11](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.10...v0.35.11) (2020-11-12)


### Bug Fixes

* add enums to types/__init__.py ([#695](https://www.github.com/googleapis/gapic-generator-python/issues/695)) ([e1d4a4a](https://www.github.com/googleapis/gapic-generator-python/commit/e1d4a4ae768a631f6e6dc28f2acfde8be8dc4a8f))
* update protobuf version [gapic-generator-python] ([#696](https://www.github.com/googleapis/gapic-generator-python/issues/696)) ([ea3e519](https://www.github.com/googleapis/gapic-generator-python/commit/ea3e5198862881f5b142638df6ea604654f81f82))

## [0.35.10](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.9...v0.35.10) (2020-11-09)


### Documentation

* fix a few typos ([#690](https://www.github.com/googleapis/gapic-generator-python/issues/690)) ([2716838](https://www.github.com/googleapis/gapic-generator-python/commit/2716838fb739c9350eee2c95b5cf207c4d83423d))

## [0.35.9](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.8...v0.35.9) (2020-10-27)


### Performance Improvements

* collisions don't contain reserved names by default ([#684](https://www.github.com/googleapis/gapic-generator-python/issues/684)) ([2ec6ea6](https://www.github.com/googleapis/gapic-generator-python/commit/2ec6ea6835256c0d7b252e035cf4eac1ff442647))

## [0.35.8](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.7...v0.35.8) (2020-10-21)


### Documentation

* generated message types reference proto-plus ([#680](https://www.github.com/googleapis/gapic-generator-python/issues/680)) ([23327b2](https://www.github.com/googleapis/gapic-generator-python/commit/23327b275fb5a3fefe6c47cb15b9d9ecb02aac1f))

## [0.35.7](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.6...v0.35.7) (2020-10-21)


### Bug Fixes

* expose ssl credentials from transport ([#677](https://www.github.com/googleapis/gapic-generator-python/issues/677)) ([da0ee3e](https://www.github.com/googleapis/gapic-generator-python/commit/da0ee3eab4f80bf3d70fa5e06a2dcef7e1d4d22e))

## [0.35.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.5...v0.35.6) (2020-10-20)


### Bug Fixes

* unknown resources do not cause a generator crash ([#675](https://www.github.com/googleapis/gapic-generator-python/issues/675)) ([2d23d7d](https://www.github.com/googleapis/gapic-generator-python/commit/2d23d7d202099ccf145c01aeb9a03ae46b4e1b00))

## [0.35.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.4...v0.35.5) (2020-10-19)


### Bug Fixes

* numerous small fixes to allow bigtable-admin ([#660](https://www.github.com/googleapis/gapic-generator-python/issues/660)) ([09692c4](https://www.github.com/googleapis/gapic-generator-python/commit/09692c4e889ccde3b0ca31a5e8476c1679804beb))

## [0.35.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.3...v0.35.4) (2020-10-16)


### Bug Fixes

* minor typo in ads template ([#664](https://www.github.com/googleapis/gapic-generator-python/issues/664)) ([816f965](https://www.github.com/googleapis/gapic-generator-python/commit/816f965c8560bf65d8043bd67672c660a2b1300b))

## [0.35.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.2...v0.35.3) (2020-10-13)


### Documentation

* remove references to pipsi ([#656](https://www.github.com/googleapis/gapic-generator-python/issues/656)) ([39c612b](https://www.github.com/googleapis/gapic-generator-python/commit/39c612b545bc93c7c738a78f074672ee66365efb))

## [0.35.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.1...v0.35.2) (2020-10-13)


### Bug Fixes

* modules referenced in MapField message type are properly aliased ([#654](https://www.github.com/googleapis/gapic-generator-python/issues/654)) ([2c79349](https://www.github.com/googleapis/gapic-generator-python/commit/2c79349e7b89435bc45e499885f7b12ac0bc2d9f)), closes [#618](https://www.github.com/googleapis/gapic-generator-python/issues/618)

## [0.35.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.0...v0.35.1) (2020-10-09)


### Bug Fixes

* the common resources are not targets for lookup ([#650](https://www.github.com/googleapis/gapic-generator-python/issues/650)) ([8e1b384](https://www.github.com/googleapis/gapic-generator-python/commit/8e1b384e812ef519c421c8c288d5118961d8b4cf))

## [0.35.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.4...v0.35.0) (2020-10-09)


### Features

* file_level and indirectly used resources generate helper methods ([#642](https://www.github.com/googleapis/gapic-generator-python/issues/642)) ([42e224c](https://www.github.com/googleapis/gapic-generator-python/commit/42e224cb100f6e2aa9370bc6a5179d62979b5c4d)), closes [#637](https://www.github.com/googleapis/gapic-generator-python/issues/637)

## [0.34.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.3...v0.34.4) (2020-10-09)


### Bug Fixes

* expose transport property for clients ([#645](https://www.github.com/googleapis/gapic-generator-python/issues/645)) ([13cddda](https://www.github.com/googleapis/gapic-generator-python/commit/13cddda0623bd4d24ae7973752b1be0eaa40523a)), closes [#640](https://www.github.com/googleapis/gapic-generator-python/issues/640)

## [0.34.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.2...v0.34.3) (2020-10-08)


### Bug Fixes

* fix types on server and bidi streaming callables ([#641](https://www.github.com/googleapis/gapic-generator-python/issues/641)) ([d92c202](https://www.github.com/googleapis/gapic-generator-python/commit/d92c2029398c969ebf2a68a5bf77c5eb4fff7b31))

## [0.34.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.1...v0.34.2) (2020-09-30)


### Bug Fixes

* resource messages in method response types generate helpers ([#629](https://www.github.com/googleapis/gapic-generator-python/issues/629)) ([52bfd6d](https://www.github.com/googleapis/gapic-generator-python/commit/52bfd6d5d5821b33e78e6b9867a3be2865cdbc74))

## [0.34.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.0...v0.34.1) (2020-09-30)


### Bug Fixes

* fix typo attribue -> attribute ([#627](https://www.github.com/googleapis/gapic-generator-python/issues/627)) ([729146f](https://www.github.com/googleapis/gapic-generator-python/commit/729146fd53edf1e4ae4d3c9a90640a7520b1ba9d)), closes [#626](https://www.github.com/googleapis/gapic-generator-python/issues/626)

## [0.34.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.8...v0.34.0) (2020-09-29)


### Features

* add support for common resource paths ([#622](https://www.github.com/googleapis/gapic-generator-python/issues/622)) ([15a7fde](https://www.github.com/googleapis/gapic-generator-python/commit/15a7fdeb966cb64a742b6305d2c71dd3d485d0f9))

## [0.33.8](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.7...v0.33.8) (2020-09-25)


### Bug Fixes

* handle repeated fields in method signatures ([#445](https://www.github.com/googleapis/gapic-generator-python/issues/445)) ([3aae799](https://www.github.com/googleapis/gapic-generator-python/commit/3aae799f62a1f5d3b0506d919cc6080ee417f14b))

## [0.33.7](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.6...v0.33.7) (2020-09-24)


### Bug Fixes

* retriable exceptions are deterministically ordered in GAPICs ([#619](https://www.github.com/googleapis/gapic-generator-python/issues/619)) ([f7b1164](https://www.github.com/googleapis/gapic-generator-python/commit/f7b11640b74d8c64747b33783976d6e0ab9c61c4))

## [0.33.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.5...v0.33.6) (2020-09-22)


### Bug Fixes

* operation module is properly aliased if necessary ([#615](https://www.github.com/googleapis/gapic-generator-python/issues/615)) ([8f92fd9](https://www.github.com/googleapis/gapic-generator-python/commit/8f92fd9999286ef3f916119be78dbeb838a15550)), closes [#610](https://www.github.com/googleapis/gapic-generator-python/issues/610)

## [0.33.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.4...v0.33.5) (2020-09-22)


### Bug Fixes

* remove 'property' from reserved names ([#613](https://www.github.com/googleapis/gapic-generator-python/issues/613)) ([8338a51](https://www.github.com/googleapis/gapic-generator-python/commit/8338a51a81f5f5b8ebacf68c8e46d3e1804d3f8b))

## [0.33.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.3...v0.33.4) (2020-09-17)


### Bug Fixes

* 'id' should not be a reserved name ([#602](https://www.github.com/googleapis/gapic-generator-python/issues/602)) ([c43c574](https://www.github.com/googleapis/gapic-generator-python/commit/c43c5740db099be19c5f6e52b3a917a631003411))

## [0.33.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.2...v0.33.3) (2020-09-15)


### Bug Fixes

* module names can no longer collide with keywords or builtins ([#595](https://www.github.com/googleapis/gapic-generator-python/issues/595)) ([960d550](https://www.github.com/googleapis/gapic-generator-python/commit/960d550c4a8fd09b052cce785d76243a5d4525d7))

## [0.33.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.1...v0.33.2) (2020-09-15)


### Bug Fixes

* ignore types for imports generated from 'google.api_core' ([#597](https://www.github.com/googleapis/gapic-generator-python/issues/597)) ([8440e09](https://www.github.com/googleapis/gapic-generator-python/commit/8440e09855d399d647b62238a9697e04ea4d0d41)), closes [#596](https://www.github.com/googleapis/gapic-generator-python/issues/596)

## [0.33.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.0...v0.33.1) (2020-09-15)


### Bug Fixes

* Fix client template type hints ([#593](https://www.github.com/googleapis/gapic-generator-python/issues/593)) ([93f34e8](https://www.github.com/googleapis/gapic-generator-python/commit/93f34e8a2a351a24a49424c1722baec2893dc764))

## [0.33.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.4...v0.33.0) (2020-09-10)


### Features

* support mtls env variables ([#589](https://www.github.com/googleapis/gapic-generator-python/issues/589)) ([b19026d](https://www.github.com/googleapis/gapic-generator-python/commit/b19026d9cca26ebd1cd0c3e73f738c4d1870d987))

## [0.32.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.3...v0.32.4) (2020-09-03)


### Bug Fixes

* rendering mock values for recursive messages no longer crashes ([#587](https://www.github.com/googleapis/gapic-generator-python/issues/587)) ([c2a83e5](https://www.github.com/googleapis/gapic-generator-python/commit/c2a83e561bf46b4af21e9008c7d67a1c609d7d06))

## [0.32.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.2...v0.32.3) (2020-08-28)


### Bug Fixes

* stabilize the order of resource helper methods and ([#582](https://www.github.com/googleapis/gapic-generator-python/issues/582)) ([7d2adde](https://www.github.com/googleapis/gapic-generator-python/commit/7d2adde3a1ae81ac88ced822d6dfdfb26ffbfdf0))

## [0.32.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.1...v0.32.2) (2020-08-20)


### Bug Fixes

* add 'type: ignore' comment for 'google.auth' ([#579](https://www.github.com/googleapis/gapic-generator-python/issues/579)) ([af17501](https://www.github.com/googleapis/gapic-generator-python/commit/af17501d258c7c37fc1081fcad5fe18f7629f4c3))

## [0.32.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.0...v0.32.1) (2020-08-19)


### Bug Fixes

* rename local var page in generated tests ([#577](https://www.github.com/googleapis/gapic-generator-python/issues/577)) ([075f9e8](https://www.github.com/googleapis/gapic-generator-python/commit/075f9e8d50b02ffb5f2f042b84f27a9f634636e2))

## [0.32.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.31.1...v0.32.0) (2020-08-17)


### Features

* allow user-provided client info ([#573](https://www.github.com/googleapis/gapic-generator-python/issues/573)) ([b2e5274](https://www.github.com/googleapis/gapic-generator-python/commit/b2e52746c7ce4b983482fb776224b30767978c79)), closes [googleapis/python-kms#37](https://www.github.com/googleapis/python-kms/issues/37) [#566](https://www.github.com/googleapis/gapic-generator-python/issues/566)

## [0.31.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.31.0...v0.31.1) (2020-08-17)


### Bug Fixes

* install gcc by hand ([#571](https://www.github.com/googleapis/gapic-generator-python/issues/571)) ([e224a03](https://www.github.com/googleapis/gapic-generator-python/commit/e224a0365a2d3ed20d69cf4d1298a3f022f8da76))

## [0.31.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.30.0...v0.31.0) (2020-07-28)


### Features

* bypass request copying in method calls ([#557](https://www.github.com/googleapis/gapic-generator-python/issues/557)) ([3a23143](https://www.github.com/googleapis/gapic-generator-python/commit/3a2314318de229a3353c984a8cb2766ae95cc968))


### Bug Fixes

* add google.api_core.retry import to base.py ([#555](https://www.github.com/googleapis/gapic-generator-python/issues/555)) ([1d08e60](https://www.github.com/googleapis/gapic-generator-python/commit/1d08e60cea4c5b3fa2555a4952161b0115d686f2))

## [0.30.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.29.2...v0.30.0) (2020-07-27)


### Features

* precache wrapped rpcs ([#553](https://www.github.com/googleapis/gapic-generator-python/issues/553)) ([2f2fb5d](https://www.github.com/googleapis/gapic-generator-python/commit/2f2fb5d3d9472a79c80be6d052129d07d2bbb835))

## [0.29.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.29.1...v0.29.2) (2020-07-23)


### Bug Fixes

* rename __init__.py to __init__.py.j2 ([#550](https://www.github.com/googleapis/gapic-generator-python/issues/550)) ([71a7062](https://www.github.com/googleapis/gapic-generator-python/commit/71a7062b918136b916cc5bfc7dbdf64f870edf6a)), closes [#437](https://www.github.com/googleapis/gapic-generator-python/issues/437)

## [0.29.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.29.0...v0.29.1) (2020-07-23)


### Bug Fixes

* use context manager for mtls env var ([#548](https://www.github.com/googleapis/gapic-generator-python/issues/548)) ([d19e180](https://www.github.com/googleapis/gapic-generator-python/commit/d19e1808df9cd2884ae7a449977a479b4829bc1d))

## [0.29.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.28.1...v0.29.0) (2020-07-22)


### Features

* add iam methods to templates ([#545](https://www.github.com/googleapis/gapic-generator-python/issues/545)) ([3f42c3c](https://www.github.com/googleapis/gapic-generator-python/commit/3f42c3cf8aae432a9bda0953fbabd7f0c8d774de))
* support quota project override via client options ([#496](https://www.github.com/googleapis/gapic-generator-python/issues/496)) ([bbc6b36](https://www.github.com/googleapis/gapic-generator-python/commit/bbc6b367f50526312e8320f0fc668ef88f230dbd))


### Bug Fixes

* make # after alpha/beta optional ([#540](https://www.github.com/googleapis/gapic-generator-python/issues/540)) ([f86a47b](https://www.github.com/googleapis/gapic-generator-python/commit/f86a47b6431e374ae1797061511b49fe6bf22daf))

## [0.28.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.28.0...v0.28.1) (2020-07-16)


### Bug Fixes

* remove typo from py_gapic.bzl ([#532](https://www.github.com/googleapis/gapic-generator-python/issues/532)) ([2975c2d](https://www.github.com/googleapis/gapic-generator-python/commit/2975c2d76e08b5ee5324730707707d9dd6ced8ae))

## [0.28.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.27.0...v0.28.0) (2020-07-16)


### Features

* add retry config passed to bazel rule ([#526](https://www.github.com/googleapis/gapic-generator-python/issues/526)) ([9e96151](https://www.github.com/googleapis/gapic-generator-python/commit/9e96151d702786912fcf033f7535efad8ae754ee))


### Bug Fixes

* paged code and templates are no longer message centric ([#527](https://www.github.com/googleapis/gapic-generator-python/issues/527)) ([00ba77c](https://www.github.com/googleapis/gapic-generator-python/commit/00ba77c3d27ef9a0b8742db3660983b80a68c672))

## [0.27.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.6...v0.27.0) (2020-07-13)


### Features

* support for proto3 optional fields ([#519](https://www.github.com/googleapis/gapic-generator-python/issues/519)) ([1aa729c](https://www.github.com/googleapis/gapic-generator-python/commit/1aa729cc8d2f7f0de25c8348fdbf9d6dd96f5847))

## [0.26.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.5...v0.26.6) (2020-07-10)


### Bug Fixes

* primitive repeated fields are now correctly auto paginated ([#517](https://www.github.com/googleapis/gapic-generator-python/issues/517)) ([61a2cc0](https://www.github.com/googleapis/gapic-generator-python/commit/61a2cc0d4c08064d442fd4d7aa4b1b9e56158eaa))

## [0.26.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.4...v0.26.5) (2020-07-10)


### Bug Fixes

* convert datetime back to proto for unit tests ([#511](https://www.github.com/googleapis/gapic-generator-python/issues/511)) ([e1c787d](https://www.github.com/googleapis/gapic-generator-python/commit/e1c787d3b6fe09dc0b4e00f07a7bd77fb5f1e6a3))

## [0.26.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.3...v0.26.4) (2020-07-10)


### Bug Fixes

* require min google-api-core version of 1.21.0 ([#506](https://www.github.com/googleapis/gapic-generator-python/issues/506)) ([bf787bd](https://www.github.com/googleapis/gapic-generator-python/commit/bf787bd36198288d6a40e45e44e43f0098cfec7c)), closes [#461](https://www.github.com/googleapis/gapic-generator-python/issues/461)
* tweak oneof detection ([#505](https://www.github.com/googleapis/gapic-generator-python/issues/505)) ([1632e25](https://www.github.com/googleapis/gapic-generator-python/commit/1632e250cfc01a17ccad128c3e065008b334473a))

## [0.26.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.2...v0.26.3) (2020-07-08)


### Bug Fixes

* fix wrong unit test ([#502](https://www.github.com/googleapis/gapic-generator-python/issues/502)) ([c95bd45](https://www.github.com/googleapis/gapic-generator-python/commit/c95bd45506df7973758b9e1249586597d8214985))

## [0.26.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.1...v0.26.2) (2020-07-07)


### Bug Fixes

* add oneof fields to generated protoplus init ([#485](https://www.github.com/googleapis/gapic-generator-python/issues/485)) ([be5a847](https://www.github.com/googleapis/gapic-generator-python/commit/be5a847aeff6687679f7bca46308362d588f5c77)), closes [#484](https://www.github.com/googleapis/gapic-generator-python/issues/484)

## [0.26.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.0...v0.26.1) (2020-07-07)


### Bug Fixes

* pass metadata to pagers ([#470](https://www.github.com/googleapis/gapic-generator-python/issues/470)) ([c43c6d9](https://www.github.com/googleapis/gapic-generator-python/commit/c43c6d943fa99f202014bf4bba795df25d314a63)), closes [#469](https://www.github.com/googleapis/gapic-generator-python/issues/469)

## [0.26.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.25.2...v0.26.0) (2020-06-30)


### Features

* add `credentials_file` and `scopes` via `client_options` ([#461](https://www.github.com/googleapis/gapic-generator-python/issues/461)) ([b5e1b1e](https://www.github.com/googleapis/gapic-generator-python/commit/b5e1b1e8991159dc176da889e9bdf12e3eebdb1e))


### Bug Fixes

* add name and version info to fixup script name ([#490](https://www.github.com/googleapis/gapic-generator-python/issues/490)) ([16fe7e7](https://www.github.com/googleapis/gapic-generator-python/commit/16fe7e7885b7e17bf16b4f1f8f8844b9f5d0bdfe))
* Temporarily define a fixed testing event loop ([#493](https://www.github.com/googleapis/gapic-generator-python/issues/493)) ([2d22d91](https://www.github.com/googleapis/gapic-generator-python/commit/2d22d919bc8c08e03f501ff2f23152b761467c80))

## [0.25.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.25.1...v0.25.2) (2020-06-23)


### Bug Fixes

* always use dataclasses 0.6 ([#481](https://www.github.com/googleapis/gapic-generator-python/issues/481)) ([066d04e](https://www.github.com/googleapis/gapic-generator-python/commit/066d04e7d53301024106f244280502f16af46b79))

## [0.25.1](https://www.github.com/googleapis/gapic-generator-python/compare/0.25.0...v0.25.1) (2020-06-23)


### Bug Fixes

* only require dataclases if python<3.7 ([#475](https://www.github.com/googleapis/gapic-generator-python/issues/475)) ([9597695](https://www.github.com/googleapis/gapic-generator-python/commit/959769518ea47df383b23b6e48c5da148f69029e))

## [0.25.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.24.2...v0.25.0) (2020-06-17)


### Features

* provide AsyncIO support for generated code ([#365](https://www.github.com/googleapis/gapic-generator-python/issues/365)) ([305ed34](https://www.github.com/googleapis/gapic-generator-python/commit/305ed34cfc1607c990f2f88b27f53358da25c366))

## [0.24.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.24.1...v0.24.2) (2020-06-13)


### Bug Fixes

* generated unit tests live in the 'tests/gapic' subdir ([#456](https://www.github.com/googleapis/gapic-generator-python/issues/456)) ([1ed7c9d](https://www.github.com/googleapis/gapic-generator-python/commit/1ed7c9d6fe9595c390387d72113d741ebf28538d)), closes [#454](https://www.github.com/googleapis/gapic-generator-python/issues/454)

## [0.24.1](https://www.github.com/googleapis/gapic-generator-python/compare/0.24.0...v0.24.1) (2020-06-12)


### Bug Fixes

* update GOOGLE_API_USE_MTLS value ([#453](https://www.github.com/googleapis/gapic-generator-python/issues/453)) ([7449ad5](https://www.github.com/googleapis/gapic-generator-python/commit/7449ad5aad4a1fbbf9ca3796e097512fc80991e3))
