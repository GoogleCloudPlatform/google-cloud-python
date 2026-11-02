# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-auth-oauthlib/#history

## [1.0.0](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.8.0...v1.0.0) (2023-02-06)


### ⚠ BREAKING CHANGES

* PKCE is enabled by default. ([#269](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/269))

### Features

* PKCE is enabled by default. ([#269](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/269)) ([1e04d3f](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/1e04d3f181b1734a73d82396c969754034f55b38))


### Bug Fixes

* Change the library from preview to stable ([#267](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/267)) ([c77edf1](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/c77edf12a84cc71622f25eee5091656652ff2c65))
* Remove deprecated OOB code ([1391486](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/13914865ec3cbdb1e4ab87a7bcfc34d0b4e184d3))

## [0.8.0](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.7.1...v0.8.0) (2022-12-08)


### Features

* Add support for Python 3.11 ([#253](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/253)) ([85fd1da](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/85fd1dab50a6cb387f11a4f00ad9ec6c49f7994c))
* Introduce granted scopes to credentials ([#257](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/257)) ([51fef3b](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/51fef3b9703a292f39054f80d9bf9780d115db6c))

## [0.7.1](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.7.0...v0.7.1) (2022-11-03)


### Bug Fixes

* Include updates to properties from Google Auth lib ([#249](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/249)) ([58becac](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/58becac1a4030d9bc3daf089645c4412227c4679))

## [0.7.0](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.6.0...v0.7.0) (2022-10-25)


### Bug Fixes

* **setup.py:** increase required google-auth version to &gt;=2.13.0 ([f8a15f7](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/f8a15f75115ed5ef3ea47b50a707459ed62a8f48))

## [0.6.0](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.5.3...v0.6.0) (2022-10-20)


### Features

* Update to allow for 3PI credentials ([#240](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/240)) ([4a37dec](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/4a37dec027e3d742ed6615f9828ab51a594d2ca2))


### Bug Fixes

* Add timeout to run_local_server when waiting for response ([#245](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/245)) ([8d53bc3](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/8d53bc304a079d011df2757be1b88211baf47549))


### Documentation

* Update readme to point to current docs url ([#241](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/241)) ([8c29d2e](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/8c29d2ed0d8fda7319617fdd6ac2cde70319b6bd))

## [0.5.3](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.5.2...v0.5.3) (2022-09-02)


### Bug Fixes

* Pass port range from `get_user_credentials` to `find_open_port` ([#212](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/212)) ([479330a](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/479330a49a28e4f7443982ba235d2adee3e49d58))

## [0.5.2](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.5.1...v0.5.2) (2022-06-03)


### Documentation

* fix changelog header to consistent size ([#204](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/204)) ([cbd7d67](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/cbd7d675e772ad7c31da45296e3444113b6fd19a))

## [0.5.1](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.5.0...v0.5.1) (2022-03-15)


### Bug Fixes

* avoid deprecated "out-of-band" authentication flow ([#186](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/186)) ([f119c4e](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/f119c4e0f5cad25b1254b0783e8226eda2d361cb))

## [0.5.0](https://github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.4.6...v0.5.0) (2022-02-24)


### Features

* deprecate OAuth out-of-band flow ([#175](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/175)) ([1fb16be](https://github.com/googleapis/google-auth-library-python-oauthlib/commit/1fb16be1bad9050ee29293541be44e41e82defd7))

## [0.4.6](https://www.github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.4.5...v0.4.6) (2021-08-30)


### Bug Fixes

* remove dependency on `six` ([#146](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/146)) ([c338733](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/c3387335c49597870b437a9130aed92dca6571f2)), closes [#145](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/145)

## [0.4.5](https://www.github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.4.4...v0.4.5) (2021-07-26)


### Documentation

* fix links to installed app, client secrets docs ([#86](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/86)) ([e8e5dbb](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/e8e5dbbf0b118fc68a9b60b91f0075f84908b6f6)), closes [#85](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/85)
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/1127)) ([#126](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/126)) ([8806324](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/8806324428b5aebe6659c49a16066afafbe4d400)), closes [#1126](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/1126)
* add Samples section to CONTRIBUTING.rst ([#134](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/134)) ([1599a97](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/1599a97831bbe1c15cf5a0d257817967c1cd227f))


### Miscellaneous Chores

* release as 0.4.5 ([#137](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/137)) ([a54f283](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/a54f283ee7854367ff289ee863a7404692f31099))

## [0.4.4](https://www.github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.4.3...v0.4.4) (2021-03-29)


### Bug Fixes

* add redirect_uri_trailing slash param to run_local_server ([#111](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/111)) ([666863a](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/666863aeabb8d6b3608ea95edce09fe69a5f2679))

## [0.4.3](https://www.github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.4.2...v0.4.3) (2021-02-12)


### Bug Fixes

* add `charset-utf-8` to response header ([#104](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/104)) ([53e31e2](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/53e31e2d03b315c12670370f67bdca29b1cd5422))
* **deps:** add lower bounds to all dependencies ([#99](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/99)) ([5587c6a](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/5587c6a72547742986e363e1f5ef6bcabd93bb02))

## [0.4.2](https://www.github.com/googleapis/google-auth-library-python-oauthlib/compare/v0.4.1...v0.4.2) (2020-10-28)


### Bug Fixes

* don't open browser if port is occupied ([#92](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/92)) ([0004057](https://www.github.com/googleapis/google-auth-library-python-oauthlib/commit/00040576ab096faec1f6eb54c886cb9c33be17ed)), closes [#75](https://www.github.com/googleapis/google-auth-library-python-oauthlib/issues/75)

## 0.4.1

08-26-2019 13:25 PDT

### Implementation Changes
- Don't auto-generate code_verifier by default. ([#48](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/48))

### Internal / Testing Changes
- Add renovate.json ([#56](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/56))

## 0.4.0
- Add `get_user_credentials` function to get your user credentials ([#40](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/40))
- Add noxfile ([#43](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/43))
- Implement code verifier (PKCE) ([#42](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/42))
- Use actual server port in redirect_uri to allow automatic assignment ([#33](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/33))
([#41](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/41))

## 0.3.0
- Use utc when parsing expiration timestamp ([#26](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/26))
- Allow saving credentials in current directory ([#25](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/25))

## 0.2.0
- Populate id_token into credentials from oauth2session ([#20](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/20))
- Carry token expiry from oauth2session into Credentials object ([#18](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/18)) ([#19](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/19))
- Accept redirect_uri as arg to flow creating classmethods. ([#17](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/17))

## 0.1.1
- Allow ``access_type`` parameter to be overriden in ``Flow`` ([#16](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/16))
- Use a test port that is less likely to be taken ([#12](https://github.com/googleapis/google-auth-library-python-oauthlib/pull/12))
- Documentation updates

## 0.1.0
Add command line tool.

## 0.0.1
Initial release. This package contains the functionality previously located in `google.oauth2.oauthlib` and `google.oauth2.flows`.
