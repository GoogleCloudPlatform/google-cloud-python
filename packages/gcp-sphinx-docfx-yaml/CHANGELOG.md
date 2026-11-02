# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/gcp-sphinx-docfx-yaml/#history

## [3.4.0](https://github.com/googleapis/google-cloud-python/compare/gcp-sphinx-docfx-yaml-v3.3.3...gcp-sphinx-docfx-yaml-v3.4.0) (2026-10-15)


### Features

* **gcp-sphinx-docfx-yaml:** optimize performance ([#18588](https://github.com/googleapis/google-cloud-python/issues/18588)) ([cf1a0e5](https://github.com/googleapis/google-cloud-python/commit/cf1a0e575932f1670c1714c0aa6018955292015b))

## [3.3.3](https://github.com/googleapis/google-cloud-python/compare/gcp-sphinx-docfx-yaml-v3.3.2...gcp-sphinx-docfx-yaml-v3.3.3) (2026-10-01)


### Bug Fixes

* **ci:** fix docfx and db-dtypes pandas compat ([#18512](https://github.com/googleapis/google-cloud-python/issues/18512)) ([5d57b25](https://github.com/googleapis/google-cloud-python/commit/5d57b255271ed43274286cb65a9f6e52ee56875a))

## [3.3.2](https://github.com/googleapis/google-cloud-python/compare/gcp-sphinx-docfx-yaml-v3.3.1...gcp-sphinx-docfx-yaml-v3.3.2) (2026-08-21)


### Documentation

* **handwritten:** centralize CONTRIBUTING.rst pointers ([#17642](https://github.com/googleapis/google-cloud-python/issues/17642)) ([23b9499](https://github.com/googleapis/google-cloud-python/commit/23b94994bd5251493b81d91657d1f79a5d3c4b97))

## [3.3.1](https://github.com/googleapis/google-cloud-python/compare/gcp-sphinx-docfx-yaml-v3.3.0...gcp-sphinx-docfx-yaml-v3.3.1) (2026-08-06)


### Bug Fixes

* bump grpcio to 1.59.0; require Python 3.10+ ([#17351](https://github.com/googleapis/google-cloud-python/issues/17351)) ([a53487a](https://github.com/googleapis/google-cloud-python/commit/a53487a009c21912ea6c99fe3a5e0e52a26b31ef))
* require Protobuf 6.33.5+ ([#17743](https://github.com/googleapis/google-cloud-python/issues/17743)) ([d267342](https://github.com/googleapis/google-cloud-python/commit/d26734293c23f06ccce048f7d9b0fa365e813410))

## [3.3.0](https://github.com/googleapis/google-cloud-python/compare/gcp-sphinx-docfx-yaml-v3.2.5...gcp-sphinx-docfx-yaml-v3.3.0) (2026-05-06)


### Bug Fixes

* correctly parse type assertions in `extends` clause ([@&#8203;nicolo-ribaudo](https://redirect.github.com/nicolo-ribaudo)) - [#&#8203;17723](https://redirect.github.com/babel/babel/pull/17723) \[7.x backport] fix(parser): improve super type argument parsing ([@&#8203;JLHwung](https://redirect.github.com/JLHwung)) - `babel-traverse` - [#&#8203;17708](https://redirect.github.com/babel/babel/pull/17708) ([5098df262245fb333ae73fc7eb568f905bc0190a](https://github.com/googleapis/google-cloud-python/commit/5098df262245fb333ae73fc7eb568f905bc0190a))
* provide a hub when traversing a File or Program and no parentPath is given ([@&#8203;simbahax](https://redirect.github.com/simbahax)) - `babel-plugin-transform-block-scoping`, `babel-traverse` - [#&#8203;17737](https://redirect.github.com/babel/babel/pull/17737) \[7.x backport] fix: Rename switch discriminant references when body creates shadowing variable ([@&#8203;magic-akari](https://redirect.github.com/magic-akari)) ([5098df262245fb333ae73fc7eb568f905bc0190a](https://github.com/googleapis/google-cloud-python/commit/5098df262245fb333ae73fc7eb568f905bc0190a))

## [3.2.5](https://github.com/googleapis/google-cloud-python/compare/gcp-sphinx-docfx-yaml-v3.2.4...gcp-sphinx-docfx-yaml-v3.2.5) (2026-04-02)


### Bug Fixes

* do not store reference to algorithms dict on PyJWK (<a href="https://redirect.github.com/jpadilla/pyjwt/issues/1143">#1143</a>)</li> <li><a href="https://github.com/jpadilla/pyjwt/commit/f3ba74c106df9ce10e272dfaad96acb4ab3ef5a5"><code>f3ba74c</code></a> [pre-commit.ci] pre-commit autoupdate (<a href="https://redirect.github.com/jpadilla/pyjwt/issues/1145">#1145</a>)</li> <li><a href="https://github.com/jpadilla/pyjwt/commit/0318ffa7b156b01600376e38952bf961382e0724"><code>0318ffa</code></a> [pre-commit.ci] pre-commit autoupdate (<a href="https://redirect.github.com/jpadilla/pyjwt/issues/1141">#1141</a>)</li> <li><a href="https://github.com/jpadilla/pyjwt/commit/a52753db3c1075ac01337fa8b7cc92b13a19ac09"><code>a52753d</code></a> Bump actions/download-artifact from 7 to 8 (<a href="https://redirect.github.com/jpadilla/pyjwt/issues/1142">#1142</a>)</li> <li><a href="https://github.com/jpadilla/pyjwt/commit/b85050f1d444c6828bb4618ee764443b0a3f5d18"><code>b85050f</code></a> ([b2950d55e4f9d904de9b232551f65354044eccbb](https://github.com/googleapis/google-cloud-python/commit/b2950d55e4f9d904de9b232551f65354044eccbb))
* close HTTPError to prevent ResourceWarning on Python 3.14 (<a href="https://redirect.github.com/jpadilla/pyjwt/issues/1133">#1133</a>)</li> <li>Additional commits viewable in <a href="https://github.com/jpadilla/pyjwt/compare/2.4.0...2.12.0">compare view</a></li> </ul> </details> <br /> ([b2950d55e4f9d904de9b232551f65354044eccbb](https://github.com/googleapis/google-cloud-python/commit/b2950d55e4f9d904de9b232551f65354044eccbb))

## [3.2.4](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.2.3...v3.2.4) (2025-10-22)


### Bug Fixes

* Add support for formatting broken argspec entities ([#420](https://github.com/googleapis/sphinx-docfx-yaml/issues/420)) ([baf4389](https://github.com/googleapis/sphinx-docfx-yaml/commit/baf43897741666342cd2429f0894cecaa355702f))

## [3.2.3](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.2.2...v3.2.3) (2025-03-19)


### Bug Fixes

* Update summary overview entry to deduplicate ([#413](https://github.com/googleapis/sphinx-docfx-yaml/issues/413)) ([0c714a8](https://github.com/googleapis/sphinx-docfx-yaml/commit/0c714a8390f9dc547d261cc8f6702428fa76ed5b))

## [3.2.2](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.2.1...v3.2.2) (2024-09-06)


### Bug Fixes

* Ignore disambiguation for repeated entries ([#390](https://github.com/googleapis/sphinx-docfx-yaml/issues/390)) ([917c89b](https://github.com/googleapis/sphinx-docfx-yaml/commit/917c89bece5492dd8cbb09348d05af2a5fec82aa))
* Retrieve keyword arguments for docstrings ([#389](https://github.com/googleapis/sphinx-docfx-yaml/issues/389)) ([bb6898e](https://github.com/googleapis/sphinx-docfx-yaml/commit/bb6898e054f6c53509f6394ba08eb44a36b8661b))

## [3.2.1](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.2.0...v3.2.1) (2024-05-07)


### Bug Fixes

* Build Markdown relative to input directory ([#380](https://github.com/googleapis/sphinx-docfx-yaml/issues/380)) ([2a4b9fe](https://github.com/googleapis/sphinx-docfx-yaml/commit/2a4b9fe0b3ca94e27a9b1a6e5238711045b372c9))
* Format enum data into table format ([#376](https://github.com/googleapis/sphinx-docfx-yaml/issues/376)) ([abc9667](https://github.com/googleapis/sphinx-docfx-yaml/commit/abc96675e1cbe3a9175bdf921142b32b16523f28))

## [3.2.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.1.0...v3.2.0) (2024-05-02)


### Features

* Add support for enums ([#374](https://github.com/googleapis/sphinx-docfx-yaml/issues/374)) ([4575ffe](https://github.com/googleapis/sphinx-docfx-yaml/commit/4575ffebb8ded4b8ed43d4bfd3308deaa3a7b1b8))


### Documentation

* Add summary_overview template ([#367](https://github.com/googleapis/sphinx-docfx-yaml/issues/367)) ([39baecb](https://github.com/googleapis/sphinx-docfx-yaml/commit/39baecb0afcbd9a116cb809a0866bf61ac784f0e))

## [3.1.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.0.1...v3.1.0) (2024-04-01)


### Features

* Add summary page for Classes and Modules ([#361](https://github.com/googleapis/sphinx-docfx-yaml/issues/361)) ([e56c3a7](https://github.com/googleapis/sphinx-docfx-yaml/commit/e56c3a732c2a71b76d0e44bd1ed889de4ffa1f63))
* Add summary page support for methods and properties ([#363](https://github.com/googleapis/sphinx-docfx-yaml/issues/363)) ([e3ae026](https://github.com/googleapis/sphinx-docfx-yaml/commit/e3ae0262492f584516b10e1f8753b430e746ffa9))
* Grab repository metadata ([#364](https://github.com/googleapis/sphinx-docfx-yaml/issues/364)) ([1318b24](https://github.com/googleapis/sphinx-docfx-yaml/commit/1318b2462c757368be3098824dd8924e4dc8b78f))
* Support overview page ([#365](https://github.com/googleapis/sphinx-docfx-yaml/issues/365)) ([9985d13](https://github.com/googleapis/sphinx-docfx-yaml/commit/9985d134a45842eca9787483078101e0270e2345))

## [3.0.1](https://github.com/googleapis/sphinx-docfx-yaml/compare/v3.0.0...v3.0.1) (2024-03-13)


### Bug Fixes

* Update dependencies to pin Sphinx for &lt;5 compatibility ([#342](https://github.com/googleapis/sphinx-docfx-yaml/issues/342)) ([e60753a](https://github.com/googleapis/sphinx-docfx-yaml/commit/e60753a099bf8a603055e6441f6040dd042f228f))

## [3.0.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.7...v3.0.0) (2023-11-02)


### ⚠ BREAKING CHANGES

* Bump minimum version to 3.10 ([#334](https://github.com/googleapis/sphinx-docfx-yaml/issues/334))

### Features

* Bump minimum version to 3.10 ([#334](https://github.com/googleapis/sphinx-docfx-yaml/issues/334)) ([97c34cb](https://github.com/googleapis/sphinx-docfx-yaml/commit/97c34cbd2e2167e68224db1c3bc1775dddc9f6c3))

## [2.0.7](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.6...v2.0.7) (2023-11-01)


### Bug Fixes

* Ignore cross reference conversion in examples ([#332](https://github.com/googleapis/sphinx-docfx-yaml/issues/332)) ([bbfa011](https://github.com/googleapis/sphinx-docfx-yaml/commit/bbfa01175d1b1cb4ccd670cbaa1ebfa511e61e8b))

## [2.0.6](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.5...v2.0.6) (2023-10-30)


### Bug Fixes

* Refactor type hint retrieval ([#312](https://github.com/googleapis/sphinx-docfx-yaml/issues/312)) ([0c91f60](https://github.com/googleapis/sphinx-docfx-yaml/commit/0c91f60fb2eab8b184b1228d5f3eb133be7ae201))
* Support docstrings without type added ([#311](https://github.com/googleapis/sphinx-docfx-yaml/issues/311)) ([d214d64](https://github.com/googleapis/sphinx-docfx-yaml/commit/d214d64c54d06fa715535b14932ac1ad67fa0d09))
* Update annotation name extraction logic and add unit tests ([#320](https://github.com/googleapis/sphinx-docfx-yaml/issues/320)) ([220951d](https://github.com/googleapis/sphinx-docfx-yaml/commit/220951d341c27d345679f64fb67968320168e428))

## [2.0.5](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.4...v2.0.5) (2023-06-27)


### Bug Fixes

* Pin markdown builder version ([#306](https://github.com/googleapis/sphinx-docfx-yaml/issues/306)) ([0d1879d](https://github.com/googleapis/sphinx-docfx-yaml/commit/0d1879df6446f70e088c8d5ac7df6a9a743a47c9))

## [2.0.4](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.3...v2.0.4) (2023-06-02)


### Bug Fixes

* Allow top level page to only have index page ([#301](https://github.com/googleapis/sphinx-docfx-yaml/issues/301)) ([85c049a](https://github.com/googleapis/sphinx-docfx-yaml/commit/85c049a55f29ca78a1263e3f9ec4a3f5e4d5cad0))

## [2.0.3](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.2...v2.0.3) (2023-03-22)


### Bug Fixes

* Add support for return annotation in syntax ([#291](https://github.com/googleapis/sphinx-docfx-yaml/issues/291)) ([16894ce](https://github.com/googleapis/sphinx-docfx-yaml/commit/16894ce1468ad96bdf3b216266f878fe45f75a12))

## [2.0.2](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.1...v2.0.2) (2023-02-03)


### Bug Fixes

* Allow multiple/custom index pages to be used ([#280](https://github.com/googleapis/sphinx-docfx-yaml/issues/280)) ([7ee38d8](https://github.com/googleapis/sphinx-docfx-yaml/commit/7ee38d8335d974e51fd07623bdff323f99f50fad))

## [2.0.1](https://github.com/googleapis/sphinx-docfx-yaml/compare/v2.0.0...v2.0.1) (2023-01-30)


### Bug Fixes

* Remove license headers in markdown files ([#273](https://github.com/googleapis/sphinx-docfx-yaml/issues/273)) ([a4c808f](https://github.com/googleapis/sphinx-docfx-yaml/commit/a4c808fdbfbf30bc536c7c22420229b0e40fa7c3))

## [2.0.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.6.0...v2.0.0) (2022-11-15)


### ⚠ BREAKING CHANGES

* Retrieve all markdown pages (#266)

### Features

* Add golden testing ([#262](https://github.com/googleapis/sphinx-docfx-yaml/issues/262)) ([ff8902e](https://github.com/googleapis/sphinx-docfx-yaml/commit/ff8902ed5593b8cdb55e08809c24c49d0479200c))
* Retrieve all markdown pages ([#266](https://github.com/googleapis/sphinx-docfx-yaml/issues/266)) ([1cee1ed](https://github.com/googleapis/sphinx-docfx-yaml/commit/1cee1edbcc8e7c441dedc0c6b9f80c545cac75a0))


### Bug Fixes

* Remove inheritance details ([#268](https://github.com/googleapis/sphinx-docfx-yaml/issues/268)) ([43751cf](https://github.com/googleapis/sphinx-docfx-yaml/commit/43751cf17818a9a6d4d2c9e37078f3356e0fb8a9))
* Remove unused YAML fields to fix presubmit ([#265](https://github.com/googleapis/sphinx-docfx-yaml/issues/265)) ([10ecc44](https://github.com/googleapis/sphinx-docfx-yaml/commit/10ecc446d4f85801995f1810eca7261a851643a5))

## [1.6.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.5.0...v1.6.0) (2022-10-13)


### Features

* Use GitHub's default README as index page ([#255](https://github.com/googleapis/sphinx-docfx-yaml/issues/255)) ([17f6ca0](https://github.com/googleapis/sphinx-docfx-yaml/commit/17f6ca0ef8fe6aeed096a5356cac8944f8884b82))


### Bug Fixes

* Render emphasis properly and markdown in tables ([#258](https://github.com/googleapis/sphinx-docfx-yaml/issues/258)) ([4bbd921](https://github.com/googleapis/sphinx-docfx-yaml/commit/4bbd921f116cccd86d30597a254087f25f074728))

## [1.5.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.8...v1.5.0) (2022-07-11)


### Features

* support devsite notices ([#222](https://github.com/googleapis/sphinx-docfx-yaml/issues/222)) ([0da9224](https://github.com/googleapis/sphinx-docfx-yaml/commit/0da9224712f846485bdcc13807904b7e5e094e34))


### Bug Fixes

* include dependency for librarytest ([#218](https://github.com/googleapis/sphinx-docfx-yaml/issues/218)) ([420780b](https://github.com/googleapis/sphinx-docfx-yaml/commit/420780bf873bd0fc993fbbaa98833649bf0b2762))

### [1.4.8](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.7...v1.4.8) (2022-05-24)


### Bug Fixes

* add hardcoded IAM references temporarily ([#209](https://github.com/googleapis/sphinx-docfx-yaml/issues/209)) ([5dc99d2](https://github.com/googleapis/sphinx-docfx-yaml/commit/5dc99d25532e668d5bf5fc1402b93ed5f189655e))

### [1.4.7](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.6...v1.4.7) (2022-04-12)


### Bug Fixes

* add markdown header if it is missing ([#203](https://github.com/googleapis/sphinx-docfx-yaml/issues/203)) ([ccd53bd](https://github.com/googleapis/sphinx-docfx-yaml/commit/ccd53bdba8cdfe08d900a7b05f235e635a2f0441))

### [1.4.6](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.5...v1.4.6) (2022-04-06)


### Bug Fixes

* support parsing summary docstring that is not well formed ([#200](https://github.com/googleapis/sphinx-docfx-yaml/issues/200)) ([a1b362d](https://github.com/googleapis/sphinx-docfx-yaml/commit/a1b362d611be6a60d19e2b5b06806554eea111f5))

### [1.4.5](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.4...v1.4.5) (2022-03-18)


### Bug Fixes

* format code snippets properly ([#193](https://github.com/googleapis/sphinx-docfx-yaml/issues/193)) ([ef7a337](https://github.com/googleapis/sphinx-docfx-yaml/commit/ef7a3370756ba20cc78ad8193abfaaf5cd268f0c))

### [1.4.4](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.3...v1.4.4) (2022-03-03)


### Bug Fixes

* parse docstring that come without summaries ([#187](https://github.com/googleapis/sphinx-docfx-yaml/issues/187)) ([8282604](https://github.com/googleapis/sphinx-docfx-yaml/commit/8282604105893a8834cbee09cd9e0080340f31de))

### [1.4.3](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.2...v1.4.3) (2022-02-15)


### Bug Fixes

* retrieve constructors ([#181](https://github.com/googleapis/sphinx-docfx-yaml/issues/181)) ([1e6efa4](https://github.com/googleapis/sphinx-docfx-yaml/commit/1e6efa4007e3191ad07dd4e82fcb06a8fd1be746))
* use `id` field for Attributes instead of `name` ([#179](https://github.com/googleapis/sphinx-docfx-yaml/issues/179)) ([fa38c8c](https://github.com/googleapis/sphinx-docfx-yaml/commit/fa38c8ce98b92a460755c8db548cfee9309812c7))

### [1.4.2](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.1...v1.4.2) (2022-02-07)


### Bug Fixes

* update markdown header parser ([#177](https://github.com/googleapis/sphinx-docfx-yaml/issues/177)) ([71d50cc](https://github.com/googleapis/sphinx-docfx-yaml/commit/71d50cce1979a8673499f731411798bfb15c7ba6))

### [1.4.1](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.4.0...v1.4.1) (2022-01-28)


### Bug Fixes

* enable upgrading docs ([#172](https://github.com/googleapis/sphinx-docfx-yaml/issues/172)) ([bb68ea9](https://github.com/googleapis/sphinx-docfx-yaml/commit/bb68ea95ded306ccb3513c9684ce2d1ad6b3e74c))

## [1.4.0](https://github.com/googleapis/sphinx-docfx-yaml/compare/v1.3.3...v1.4.0) (2022-01-28)


### Features

* add syntax highlighting support for Markdown pages ([#170](https://github.com/googleapis/sphinx-docfx-yaml/issues/170)) ([9898807](https://github.com/googleapis/sphinx-docfx-yaml/commit/98988072c3a32ff1d1be44cb835eea0ad787e8e9))

### [1.3.3](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.3.2...v1.3.3) (2021-11-29)


### Bug Fixes

* expand entry names in Overview page to be more descriptive ([#159](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/159)) ([7bd6416](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/7bd64160cda8a84cdbd14f61bd39d5594b048bd2))

### [1.3.2](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.3.1...v1.3.2) (2021-11-16)


### Bug Fixes

* gracefully handle format_code exceptions ([#152](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/152)) ([a679ace](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/a679ace42c88ac40d7336f6d8b6266191932a3ea))

### [1.3.1](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.3.0...v1.3.1) (2021-11-15)


### Bug Fixes

* resolve square bracketed references ([#146](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/146)) ([fa049ac](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/fa049ace9d14e1f9993313983ad3426ff041672d))

## [1.3.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.2.0...v1.3.0) (2021-11-15)


### Features

* format signature using black ([#144](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/144)) ([4462b93](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/4462b93a732c9aedf35ad3321269bd4cea9f26dc))

## [1.2.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.1.2...v1.2.0) (2021-10-05)


### Features

* find more items to cross reference ([#138](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/138)) ([a0f82dd](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/a0f82ddc45d8c09ecae6ab55d6366ab6e666397b))

### [1.1.2](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.1.1...v1.1.2) (2021-09-14)


### Bug Fixes

* disambiguate after grouping by packages and versions ([#132](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/132)) ([53d68fe](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/53d68fe2a05302e4dc955157d9e08b9de33ec947))

### [1.1.1](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.1.0...v1.1.1) (2021-08-30)


### Bug Fixes

* make plugin more verbose ([#123](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/123)) ([1f25757](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/1f2575730935f0be2795c37262aa1e465221daa7))

## [1.1.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.0.1...v1.1.0) (2021-08-26)


### Features

* handle additional docstring items ([#116](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/116)) ([8c31924](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/8c319244d726c3425fcb9d10ee0a3f4157193e75))

### [1.0.1](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v1.0.0...v1.0.1) (2021-08-25)


### Bug Fixes

* do not omit arguments retrieved from docstring ([#114](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/114)) ([18bf0de](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/18bf0de2b761feabdcba071690d04b4dac0a6001))
* parse markdown header more carefully ([#111](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/111)) ([485b248](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/485b248091a6dffd8f4c0cd77a8fcb4fde8eca09))

## [1.0.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.5.2...v1.0.0) (2021-08-24)


### ⚠ BREAKING CHANGES

* add markdown page support (#102)

### Features

* add markdown page support ([#102](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/102)) ([878f1c3](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/878f1c33f3d1ff59df3417ddffd1ac3cecd3f8c1))
* group left-nav entries into versions and groups ([#96](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/96)) ([ee89394](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/ee8939425682bb81294214dd23b6aaeff74c36da))


### Bug Fixes

* recover lost function arguments and argument types ([#93](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/93)) ([b90dd0f](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/b90dd0f7a1e8e00630f24945b5425e20511be7c5))
* retrieve file name as much as possible  ([#100](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/100)) ([34cad2b](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/34cad2b2159ee73a5d1d1c16a504a1f82527deda))
* use file name instead of object name for TOC ([#97](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/97)) ([48279ef](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/48279ef23e4962cab7a5b05cf2e1dc6d0b8907f3))
* use the uid for toc entries ([#104](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/104)) ([1364dfc](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/1364dfce95044bd4e3763f40af5d281fa2ddb96a))

### [0.5.2](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.5.1...v0.5.2) (2021-07-30)


### Bug Fixes

* parse xrefs differently with new xref format ([#90](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/90)) ([22485e8](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/22485e82b1e4c3be2f7589434d53c75b28921266))

### [0.5.1](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.5.0...v0.5.1) (2021-07-29)


### Bug Fixes

* handle more xrefs and keep long uid ([#85](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/85)) ([fd4f9f3](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/fd4f9f373fcf6429d0faa76846d2d50673809a59))
* remove redundant class info for subclasses ([#87](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/87)) ([06bb556](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/06bb556a4c2371ef05e9749c6f68b9eeb18315a6))

## [0.5.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.4.0...v0.5.0) (2021-07-28)


### Features

* add subclasses to children and reference ([#77](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/77)) ([0cab5f6](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/0cab5f6cd6cd9b1da2f5f63cbcabeea69e0d7c81))
* add subPackage types for better classification ([#76](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/76)) ([3c84f3e](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/3c84f3ea05677e2e8a5a6659a14f281f537ae37a))
* process xrefs properly ([#78](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/78)) ([fcc1989](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/fcc1989a114640fd21955d35ef3eabce2d043fc9))

## [0.4.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.3.4...v0.4.0) (2021-07-21)


### Features

* add short snippet for missing summary ([#73](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/73)) ([bb432e7](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/bb432e7ef0e1df6b4315306ddb3b8a82eebb375f))


### Bug Fixes

* disambiguate all entry names to clarify duplicate names ([#72](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/72)) ([b632eb7](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/b632eb74fd3ce1dd16bc626b9a23ff79c2b6559f))

### [0.3.4](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.3.3...v0.3.4) (2021-07-05)


### Bug Fixes

* deduplicate entries in children and references ([#61](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/61)) ([6d5407b](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/6d5407b6c004587071d2523f1bad4717678774da))

### [0.3.3](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.3.2...v0.3.3) (2021-06-25)


### Bug Fixes

* handle entries that cannot be disambiguated ([#59](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/59)) ([7678b24](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/7678b246636bf8387e7049af11bce1a33a9a5826))

### [0.3.2](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.3.1...v0.3.2) (2021-06-24)


### Bug Fixes

* properly handle Raises section for GoogleDocstring ([#56](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/56)) ([793dd48](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/793dd4847cfbc6bc060d7a8840bd102f4bf37058))
* update parser to correctly parse desired tokens ([#55](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/55)) ([d1e18c7](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/d1e18c7cb64aac9710ff18863e7c78306e93d568))

### [0.3.1](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.3.0...v0.3.1) (2021-06-21)


### Bug Fixes

* update dependency requirements ([#48](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/48)) ([c1c036f](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/c1c036fd00be08f219ffa4ebdfb5d13e2ee5768a))

## [0.3.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.2.0...v0.3.0) (2021-06-21)


### Features

* Add support for Property and missing content ([#41](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/41)) ([5ac499f](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/5ac499fae23983cf929459ccc9a2ea9dcebae790))
* shorten function names shown on pages ([#22](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/22)) ([13edc85](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/13edc859bea7c6150d6b688ddd3d65cef1ad33d7))


### Bug Fixes

* complete toc disambiguation ([#45](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/45)) ([8928614](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/892861441853735b4ab608aab94edd824ae77137))
* remove function and method name override ([#42](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/42)) ([ab8f265](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/ab8f2656682ea4727c68f3bb5205260e16fb8f5c))

## [0.2.0](https://www.github.com/googleapis/sphinx-docfx-yaml/compare/v0.1.0...v0.2.0) (2021-05-13)


### Features

* clarify names in the left nav ([#16](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/16)) ([14cac76](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/14cac765681b5cebca4361adbdf7010a7728c227))

## 0.1.0 (2021-03-25)


### Documentation

* keep Python COC, update README ([#6](https://www.github.com/googleapis/sphinx-docfx-yaml/issues/6)) ([3a60b1a](https://www.github.com/googleapis/sphinx-docfx-yaml/commit/3a60b1af9c2c39fe1bb974fb899f87c81efc0274))
