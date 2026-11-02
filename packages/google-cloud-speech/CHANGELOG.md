# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-speech/#history

## [2.41.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.40.0...google-cloud-speech-v2.41.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [2.40.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.39.0...google-cloud-speech-v2.40.0) (2026-06-02)


### Features

* regenerate google-cloud-s packages (#17086) ([40b522a8473dec7ade45113ddd44ccd960803c45](https://github.com/googleapis/google-cloud-python/commit/40b522a8473dec7ade45113ddd44ccd960803c45))

## [2.39.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.38.0...google-cloud-speech-v2.39.0) (2026-05-06)

## [2.38.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.37.0...google-cloud-speech-v2.38.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [2.37.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.36.1...google-cloud-speech-v2.37.0) (2026-02-26)


### Features

* adds endpointing sensitivity to streaming recognition features ([e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c](https://github.com/googleapis/google-cloud-python/commit/e40bfd4df5e3ddfcc9d9b187f39cfadf58aafe0c))

## [2.36.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.36.0...google-cloud-speech-v2.36.1) (2026-02-05)


### Bug Fixes

* fix mypy errors (#15494) ([1f4c2862d77afa893f7a968af57e7adf54d49d0e](https://github.com/googleapis/google-cloud-python/commit/1f4c2862d77afa893f7a968af57e7adf54d49d0e))

## [2.36.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.35.0...google-cloud-speech-v2.36.0) (2026-01-09)


### Documentation

* Clarify that min_speaker_count and max_speaker_count in SpeakerDiarizationConfig are not currently used ([b3cb4de3ce50c3ec55af2b132d756252a32641f3](https://github.com/googleapis/google-cloud-python/commit/b3cb4de3ce50c3ec55af2b132d756252a32641f3))
* Update guidance on how to enable speaker diarization; to enable, set the diarization_config field to an empty SpeakerDiarizationConfig message ([b3cb4de3ce50c3ec55af2b132d756252a32641f3](https://github.com/googleapis/google-cloud-python/commit/b3cb4de3ce50c3ec55af2b132d756252a32641f3))


### Features

* add custom prompt config in the request and return prompt in the response ([b3cb4de3ce50c3ec55af2b132d756252a32641f3](https://github.com/googleapis/google-cloud-python/commit/b3cb4de3ce50c3ec55af2b132d756252a32641f3))
* update min_speaker_count and max_speaker_count to be optional ([b3cb4de3ce50c3ec55af2b132d756252a32641f3](https://github.com/googleapis/google-cloud-python/commit/b3cb4de3ce50c3ec55af2b132d756252a32641f3))

## [2.35.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.34.0...google-cloud-speech-v2.35.0) (2025-12-17)


### Features

* auto-enable mTLS when supported certificates are detected ([d2b35b25342bfa389b472f9ce49922e630019fe6](https://github.com/googleapis/google-cloud-python/commit/d2b35b25342bfa389b472f9ce49922e630019fe6))
* check Python and dependency versions in generated GAPICs ([d2b35b25342bfa389b472f9ce49922e630019fe6](https://github.com/googleapis/google-cloud-python/commit/d2b35b25342bfa389b472f9ce49922e630019fe6))

## [2.34.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.33.0...google-cloud-speech-v2.34.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [2.33.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.32.0...google-cloud-speech-v2.33.0) (2025-06-11)


### Features

* add denoiser related configuration ([c522070](https://github.com/googleapis/google-cloud-python/commit/c522070c02d2120de8772ddcd7de6e40ef64c548))


### Documentation

* updated description of sample_rate_hertz ([c522070](https://github.com/googleapis/google-cloud-python/commit/c522070c02d2120de8772ddcd7de6e40ef64c548))

## [2.32.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.31.1...google-cloud-speech-v2.32.0) (2025-04-12)


### Features

* add ALAW support to RecognitionConfig ([c970f9f](https://github.com/googleapis/google-cloud-python/commit/c970f9f158bba8af92e06dd76cf94a86165c44ca))
* add new fields to CustomClass and PhraseSet.Phrase messages ([c970f9f](https://github.com/googleapis/google-cloud-python/commit/c970f9f158bba8af92e06dd76cf94a86165c44ca))
* deprecating speaker_tag (int) for speaker_label (string) ([c970f9f](https://github.com/googleapis/google-cloud-python/commit/c970f9f158bba8af92e06dd76cf94a86165c44ca))
* make transcript_normalization field optional ([c970f9f](https://github.com/googleapis/google-cloud-python/commit/c970f9f158bba8af92e06dd76cf94a86165c44ca))


### Documentation

* miscellaneous clarifications ([c970f9f](https://github.com/googleapis/google-cloud-python/commit/c970f9f158bba8af92e06dd76cf94a86165c44ca))

## [2.31.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.31.0...google-cloud-speech-v2.31.1) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([784a3ca](https://github.com/googleapis/google-cloud-python/commit/784a3ca7a180453320521753f5bce71de329d65c))
* remove setup.cfg configuration for creating universal wheels ([#13659](https://github.com/googleapis/google-cloud-python/issues/13659)) ([59bfd42](https://github.com/googleapis/google-cloud-python/commit/59bfd42cf8a2eaeed696a7504890bce5aae815ce))

## [2.31.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.30.0...google-cloud-speech-v2.31.0) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))
* Add support for reading selective GAPIC generation methods from service YAML ([87b5382](https://github.com/googleapis/google-cloud-python/commit/87b5382a05b7a0c9faeabaf3e2baa6f05c88bb8e))

## [2.30.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.29.0...google-cloud-speech-v2.30.0) (2025-01-02)


### Features

* expand the set of supported explicit audio encodings ([6ddf897](https://github.com/googleapis/google-cloud-python/commit/6ddf8978ba597538d12cdb4ede5440dba5023c4f))


### Documentation

* updated ExplicitDecodingConfig documentation to reflect changes related to newly supported encodings ([6ddf897](https://github.com/googleapis/google-cloud-python/commit/6ddf8978ba597538d12cdb4ede5440dba5023c4f))

## [2.29.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.28.1...google-cloud-speech-v2.29.0) (2024-12-12)


### Features

* Add support for opt-in debug logging ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([856e0f0](https://github.com/googleapis/google-cloud-python/commit/856e0f07bd5212d60ad64be4c16ac8fafd07850b))

## [2.28.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.28.0...google-cloud-speech-v2.28.1) (2024-11-11)


### Bug Fixes

* disable universe-domain validation  ([#13246](https://github.com/googleapis/google-cloud-python/issues/13246)) ([bcad563](https://github.com/googleapis/google-cloud-python/commit/bcad563acea541bb51f9fbd005f18e9f32e381f0))

## [2.28.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.27.0...google-cloud-speech-v2.28.0) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13209](https://github.com/googleapis/google-cloud-python/issues/13209)) ([5f2e30d](https://github.com/googleapis/google-cloud-python/commit/5f2e30d62eea6080f5707ee18755f2bb812ad00b))

## [2.27.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.26.1...google-cloud-speech-v2.27.0) (2024-07-30)


### Features

* [google-cloud-speech] add locations metadata proto file ([a6b3bc7](https://github.com/googleapis/google-cloud-python/commit/a6b3bc7c1c2e25c54576b97ac12f63c630bb31ef))


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([9cdac77](https://github.com/googleapis/google-cloud-python/commit/9cdac77b20a8c9720aa668639e3ca6d1e759a2de))


### Documentation

* update the list of automatically detected encodings ([a6b3bc7](https://github.com/googleapis/google-cloud-python/commit/a6b3bc7c1c2e25c54576b97ac12f63c630bb31ef))
* update the maximum number of files that may be included in a BatchRecognizeRequest ([a6b3bc7](https://github.com/googleapis/google-cloud-python/commit/a6b3bc7c1c2e25c54576b97ac12f63c630bb31ef))

## [2.26.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.26.0...google-cloud-speech-v2.26.1) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12870](https://github.com/googleapis/google-cloud-python/issues/12870)) ([4d16761](https://github.com/googleapis/google-cloud-python/commit/4d16761640dd8e35410b3219b7d675d7668d2f88))

## [2.26.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.25.1...google-cloud-speech-v2.26.0) (2024-04-04)


### Features

* add `translation_config` in `RecognitionConfig` message ([4ed87f1](https://github.com/googleapis/google-cloud-python/commit/4ed87f14b7917ebd3379f6da7ee4064027be1852))

## [2.25.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.25.0...google-cloud-speech-v2.25.1) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12387](https://github.com/googleapis/google-cloud-python/issues/12387)) ([12ce658](https://github.com/googleapis/google-cloud-python/commit/12ce658210f148eb93d9ff501568fb6f88e77f18))

## [2.25.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.24.1...google-cloud-speech-v2.25.0) (2024-02-22)


### Features

* add API for writing BatchRecognize transcripts in SRT and VTT formats ([b76625a](https://github.com/googleapis/google-cloud-python/commit/b76625a7f00947681dba065e447a04e5626cef71))


### Bug Fixes

* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12309](https://github.com/googleapis/google-cloud-python/issues/12309)) ([c23398a](https://github.com/googleapis/google-cloud-python/commit/c23398a48d23d48e7f96971dd504ff184841666b))
* fix ValueError in test__validate_universe_domain ([2451e88](https://github.com/googleapis/google-cloud-python/commit/2451e88f302bc582b3f6d01a6ec6aceba7646252))


### Documentation

* update field documentation based on field behavior updates ([b76625a](https://github.com/googleapis/google-cloud-python/commit/b76625a7f00947681dba065e447a04e5626cef71))

## [2.24.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.24.0...google-cloud-speech-v2.24.1) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Add staticmethod decorator to `_get_client_cert_source` and `_get_api_endpoint` ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([9e8d039](https://github.com/googleapis/google-cloud-python/commit/9e8d0399c488cb5125d3144ad4a8e25794c123fb))

## [2.24.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.23.0...google-cloud-speech-v2.24.0) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([#12243](https://github.com/googleapis/google-cloud-python/issues/12243)) ([e14d4b1](https://github.com/googleapis/google-cloud-python/commit/e14d4b13a883876a420c498a044dc34ea5122629))

## [2.23.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.22.0...google-cloud-speech-v2.23.0) (2023-12-07)


### Features

* Add support for python 3.12 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Introduce compatibility with native namespace packages ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))
* Use `retry_async` instead of `retry` in async client ([e9655df](https://github.com/googleapis/google-cloud-python/commit/e9655dff9f393bf3382c668ea2a31dd3332ed192))

## [2.22.0](https://github.com/googleapis/google-cloud-python/compare/google-cloud-speech-v2.21.1...google-cloud-speech-v2.22.0) (2023-11-02)


### Features

* add transcript normalization + m4a audio format support ([8536b20](https://github.com/googleapis/google-cloud-python/commit/8536b207765435a4e5c5243b01251306197cc68f))
* Support MP3, TranscriptNormalization and SpeakerLabels in STT V1 API ([#11967](https://github.com/googleapis/google-cloud-python/issues/11967)) ([6a96691](https://github.com/googleapis/google-cloud-python/commit/6a966918532762a1794e47cf57964219ab28b062))


### Documentation

* clarify alternatives for deprecated fields ([8536b20](https://github.com/googleapis/google-cloud-python/commit/8536b207765435a4e5c5243b01251306197cc68f))
* deprecate `BatchRecognizeFileResult.transcript` in favor of `inline_result.transcript` ([8536b20](https://github.com/googleapis/google-cloud-python/commit/8536b207765435a4e5c5243b01251306197cc68f))
* deprecate `BatchRecognizeFileResult.uri` in favor of `cloud_storage_result.native_format_uri` ([8536b20](https://github.com/googleapis/google-cloud-python/commit/8536b207765435a4e5c5243b01251306197cc68f))

## [2.21.1](https://github.com/googleapis/python-speech/compare/v2.21.0...v2.21.1) (2023-10-09)


### Documentation

* Minor formatting ([7342cd5](https://github.com/googleapis/python-speech/commit/7342cd51e12ac8b39c070778ad363c09f0950f41))

## [2.21.0](https://github.com/googleapis/python-speech/compare/v2.20.1...v2.21.0) (2023-07-05)


### Features

* Add `model` and `language_codes` fields in `RecognitionConfig` message + enable default `_` recognizer ([#524](https://github.com/googleapis/python-speech/issues/524)) ([65971c5](https://github.com/googleapis/python-speech/commit/65971c547587cb85e752b25a836e0a7ac41eee48))

## [2.20.1](https://github.com/googleapis/python-speech/compare/v2.20.0...v2.20.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#522](https://github.com/googleapis/python-speech/issues/522)) ([d473ad3](https://github.com/googleapis/python-speech/commit/d473ad3c9e272b13d54014e8d3aca4871e4fd270))

## [2.20.0](https://github.com/googleapis/python-speech/compare/v2.19.0...v2.20.0) (2023-05-25)


### Features

* **v2:** Add processing strategy to batch recognition requests ([#514](https://github.com/googleapis/python-speech/issues/514)) ([5bbf3a4](https://github.com/googleapis/python-speech/commit/5bbf3a4f4c758c76502ad3f0a8ce03604ef86c14))

## [2.19.0](https://github.com/googleapis/python-speech/compare/v2.18.0...v2.19.0) (2023-03-27)


### Features

* Add support for BatchRecognize ([2e7ee2d](https://github.com/googleapis/python-speech/commit/2e7ee2dd8a8e3f6feb3cda08cd87e13e7567d4a5))


### Documentation

* Fix formatting of request arg in docstring ([#512](https://github.com/googleapis/python-speech/issues/512)) ([1edd640](https://github.com/googleapis/python-speech/commit/1edd640b6493f4ed499acc08b8dbd4edd108ed28))
* Fix the resource name format in comment for CreatePhraseSetRequest ([2e7ee2d](https://github.com/googleapis/python-speech/commit/2e7ee2dd8a8e3f6feb3cda08cd87e13e7567d4a5))

## [2.18.0](https://github.com/googleapis/python-speech/compare/v2.17.3...v2.18.0) (2023-02-28)


### Features

* Enable "rest" transport in Python for services supporting numeric enums ([a20d0f1](https://github.com/googleapis/python-speech/commit/a20d0f15a81e0ad9190f48cb4bc21b3580b7e1f0))
* Voice Activity Detection - adding speech event time and speech event type ([a20d0f1](https://github.com/googleapis/python-speech/commit/a20d0f15a81e0ad9190f48cb4bc21b3580b7e1f0))

## [2.17.3](https://github.com/googleapis/python-speech/compare/v2.17.2...v2.17.3) (2023-02-02)


### Documentation

* **v1:** Clarified boost usage ([#491](https://github.com/googleapis/python-speech/issues/491)) ([8a2a41a](https://github.com/googleapis/python-speech/commit/8a2a41ad40c5dd6282b4774b13b62a1af85f7f15))

## [2.17.2](https://github.com/googleapis/python-speech/compare/v2.17.1...v2.17.2) (2023-01-30)


### Documentation

* Clarify boost usage in Reference ([#486](https://github.com/googleapis/python-speech/issues/486)) ([e75f4a2](https://github.com/googleapis/python-speech/commit/e75f4a26db936b6646240cdca158eb5f7b15b314))

## [2.17.1](https://github.com/googleapis/python-speech/compare/v2.17.0...v2.17.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([ed80330](https://github.com/googleapis/python-speech/commit/ed80330f0d3427a17bc0c43a9b84a9f535e82d6d))


### Documentation

* Add documentation for enums ([ed80330](https://github.com/googleapis/python-speech/commit/ed80330f0d3427a17bc0c43a9b84a9f535e82d6d))

## [2.17.0](https://github.com/googleapis/python-speech/compare/v2.16.2...v2.17.0) (2023-01-16)


### Features

* Add support for python 3.11 ([#478](https://github.com/googleapis/python-speech/issues/478)) ([487242f](https://github.com/googleapis/python-speech/commit/487242f3beff810c2892b1b52b3e097bf3c7339e))
* Add typing to proto.Message based class attributes ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* Added new fields to facilitate debugging ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* **v1:** Added ABNF Grammars field in Speech Adaptation ([ca28974](https://github.com/googleapis/python-speech/commit/ca28974906ca3ad10a85978b03594aaa4b181f8d))
* **v1p1beta1:** Added ABNF Grammars field in Speech Adaptation ([ca28974](https://github.com/googleapis/python-speech/commit/ca28974906ca3ad10a85978b03594aaa4b181f8d))


### Bug Fixes

* Add dict typing for client_options ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* Drop usage of pkg_resources ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* Fix timeout default values ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))


### Documentation

* **samples:** Code samples for Speech-to-Text V2 ([5c99f00](https://github.com/googleapis/python-speech/commit/5c99f00a1b15b92ba888e36ca334ad12be854989))
* **samples:** Snippetgen handling of repeated enum field ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([c2a079c](https://github.com/googleapis/python-speech/commit/c2a079c29c9c53e9da6736303b63f7985b59949a))
* **samples:** Update code samples for adaptation and VAD ([#462](https://github.com/googleapis/python-speech/issues/462)) ([f785ac7](https://github.com/googleapis/python-speech/commit/f785ac7ed11340db893f6d43368a4bde1655c5c8))

## [2.16.2](https://github.com/googleapis/python-speech/compare/v2.16.1...v2.16.2) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#456](https://github.com/googleapis/python-speech/issues/456)) ([01f7324](https://github.com/googleapis/python-speech/commit/01f732416cebc4ead860eea1e987afe136018f62))


### Documentation

* **samples:** Add create_recognizer code sample ([#450](https://github.com/googleapis/python-speech/issues/450)) ([4ea3edc](https://github.com/googleapis/python-speech/commit/4ea3edc7b62b1a815caa7af34383e9cd2eddf5fe))
* **samples:** Add quickstart code sample for STT V2 ([#451](https://github.com/googleapis/python-speech/issues/451)) ([5b1ce98](https://github.com/googleapis/python-speech/commit/5b1ce983f812a63837c8f9338ed46b11e2c21ddc))

## [2.16.1](https://github.com/googleapis/python-speech/compare/v2.16.0...v2.16.1) (2022-10-05)


### Bug Fixes

* Remove SpeechHelpers from STT V2 client library ([#452](https://github.com/googleapis/python-speech/issues/452)) ([acfb24f](https://github.com/googleapis/python-speech/commit/acfb24f69e25c369388675f08e41062f090b4817))

## [2.16.0](https://github.com/googleapis/python-speech/compare/v2.15.1...v2.16.0) (2022-10-03)


### Features

* Added Speech-to-Text V2 API ([#447](https://github.com/googleapis/python-speech/issues/447)) ([b78cda4](https://github.com/googleapis/python-speech/commit/b78cda46f7b4cac01578832fb6d9ca07887bea52))


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#446](https://github.com/googleapis/python-speech/issues/446)) ([89ceb17](https://github.com/googleapis/python-speech/commit/89ceb175e326fe63c7fa0363cd79cae05b72ed9b))

## [2.15.1](https://github.com/googleapis/python-speech/compare/v2.15.0...v2.15.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#425](https://github.com/googleapis/python-speech/issues/425)) ([1ad5df9](https://github.com/googleapis/python-speech/commit/1ad5df96cd2c5ed8ffacd23267efe2038ae17ada))
* **deps:** require proto-plus >= 1.22.0 ([1ad5df9](https://github.com/googleapis/python-speech/commit/1ad5df96cd2c5ed8ffacd23267efe2038ae17ada))

## [2.15.0](https://github.com/googleapis/python-speech/compare/v2.14.1...v2.15.0) (2022-07-14)


### Features

* add audience parameter ([068f8e8](https://github.com/googleapis/python-speech/commit/068f8e87ec08b82f957b461d397370e38faccd29))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#416](https://github.com/googleapis/python-speech/issues/416)) ([87ad726](https://github.com/googleapis/python-speech/commit/87ad7260dfd6298a85c3caaa26504228c70802a4))
* require python 3.7+ ([#414](https://github.com/googleapis/python-speech/issues/414)) ([8961725](https://github.com/googleapis/python-speech/commit/896172595815520f06b2a8260516032e2d06c79c))

## [2.14.1](https://github.com/googleapis/python-speech/compare/v2.14.0...v2.14.1) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#400](https://github.com/googleapis/python-speech/issues/400)) ([a5d2059](https://github.com/googleapis/python-speech/commit/a5d2059d29167ba0ba3f6c07ca7336073ea87053))


### Documentation

* fix changelog header to consistent size ([#401](https://github.com/googleapis/python-speech/issues/401)) ([233539d](https://github.com/googleapis/python-speech/commit/233539d8b3ef34a236eac9a6662e19e433f427fc))
* **samples:** resolve library deprecation warnings ([1d4569d](https://github.com/googleapis/python-speech/commit/1d4569d86b9afcc882016abcd60e96583e4efed9))

## [2.14.0](https://github.com/googleapis/python-speech/compare/v2.13.1...v2.14.0) (2022-05-11)


### Features

* Add adaptation proto for v1 api ([#371](https://github.com/googleapis/python-speech/issues/371)) ([c03a6cc](https://github.com/googleapis/python-speech/commit/c03a6cc6f15a8c67a0e89c2433299601c5de73ce))


### Documentation

* Add documentation for latest models to RecognitionConfig ([#368](https://github.com/googleapis/python-speech/issues/368)) ([75b8379](https://github.com/googleapis/python-speech/commit/75b8379e97fa43f880e5e7de4404f0f8af4345f1))
* Update client libraries for v1p1beta1 api ([#372](https://github.com/googleapis/python-speech/issues/372)) ([39b0a2c](https://github.com/googleapis/python-speech/commit/39b0a2cc2f0735cf02fc02982827f4a8c7aada0b))
* update docstrings to use absolute links ([#355](https://github.com/googleapis/python-speech/issues/355)) ([e36910b](https://github.com/googleapis/python-speech/commit/e36910b24ab69b134338a8b64fe4c6edad350514))

## [2.13.1](https://github.com/googleapis/python-speech/compare/v2.13.0...v2.13.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#334](https://github.com/googleapis/python-speech/issues/334)) ([b35bd09](https://github.com/googleapis/python-speech/commit/b35bd0963fced72c927a4ffb1c08050b5cf590a2))
* **deps:** require proto-plus>=1.15.0 ([b35bd09](https://github.com/googleapis/python-speech/commit/b35bd0963fced72c927a4ffb1c08050b5cf590a2))

## [2.13.0](https://github.com/googleapis/python-speech/compare/v2.12.0...v2.13.0) (2022-02-26)


### Features

* add api key support ([#313](https://github.com/googleapis/python-speech/issues/313)) ([86fe8ea](https://github.com/googleapis/python-speech/commit/86fe8ea626c95b9dd98345777739013b9fd1b0f3))


### Bug Fixes

* **deps:** move libcst to extras ([#322](https://github.com/googleapis/python-speech/issues/322)) ([de6e7c1](https://github.com/googleapis/python-speech/commit/de6e7c193edeff69376ec94da26c76dbeaa24d36))
* resolve DuplicateCredentialArgs error when using credentials_file ([#318](https://github.com/googleapis/python-speech/issues/318)) ([1348765](https://github.com/googleapis/python-speech/commit/1348765cbf8d682ba49983a3e991cb408d59171e))


### Documentation

* add generated snippets ([#321](https://github.com/googleapis/python-speech/issues/321)) ([ca99f96](https://github.com/googleapis/python-speech/commit/ca99f96d081eed4d2d1409fc5e688a243fa78ae3))

## [2.12.0](https://github.com/googleapis/python-speech/compare/v2.11.1...v2.12.0) (2022-01-17)


### Features

* add hint boost in SpeechContext ([3fdef1f](https://github.com/googleapis/python-speech/commit/3fdef1f6057a67c21ef738f4a2e843c8e97274b4))
* add result_end_time to SpeechRecognitionResult ([#291](https://github.com/googleapis/python-speech/issues/291)) ([6ac4df6](https://github.com/googleapis/python-speech/commit/6ac4df60485243aa5a99aa1b6bfdfdbd47006474))
* add SpeechAdaptation configuration ([3fdef1f](https://github.com/googleapis/python-speech/commit/3fdef1f6057a67c21ef738f4a2e843c8e97274b4))
* add spoken punctuation and spoken emojis ([3fdef1f](https://github.com/googleapis/python-speech/commit/3fdef1f6057a67c21ef738f4a2e843c8e97274b4))
* add WEBM_OPUS codec ([3fdef1f](https://github.com/googleapis/python-speech/commit/3fdef1f6057a67c21ef738f4a2e843c8e97274b4))
* add word confidence ([3fdef1f](https://github.com/googleapis/python-speech/commit/3fdef1f6057a67c21ef738f4a2e843c8e97274b4))
* added alternative_language_codes to RecognitionConfig ([#290](https://github.com/googleapis/python-speech/issues/290)) ([3fdef1f](https://github.com/googleapis/python-speech/commit/3fdef1f6057a67c21ef738f4a2e843c8e97274b4))

## [2.11.1](https://www.github.com/googleapis/python-speech/compare/v2.11.0...v2.11.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([43f25c0](https://www.github.com/googleapis/python-speech/commit/43f25c0612ef5b88f848b13ae42f711a4fc2d72a))
* **deps:** require google-api-core >= 1.28.0 ([43f25c0](https://www.github.com/googleapis/python-speech/commit/43f25c0612ef5b88f848b13ae42f711a4fc2d72a))


### Documentation

* list oneofs in docstring ([43f25c0](https://www.github.com/googleapis/python-speech/commit/43f25c0612ef5b88f848b13ae42f711a4fc2d72a))

## [2.11.0](https://www.github.com/googleapis/python-speech/compare/v2.10.0...v2.11.0) (2021-10-25)


### Features

* add support for python 3.10 ([#274](https://www.github.com/googleapis/python-speech/issues/274)) ([cc97a58](https://www.github.com/googleapis/python-speech/commit/cc97a580bb4e693a1c3e5170064164e0c5d8482b))

## [2.10.0](https://www.github.com/googleapis/python-speech/compare/v2.9.3...v2.10.0) (2021-10-08)


### Features

* add context manager support in client ([#268](https://www.github.com/googleapis/python-speech/issues/268)) ([a5e2005](https://www.github.com/googleapis/python-speech/commit/a5e200515c621695c8c8ed76f739e0b744f32382))

## [2.9.3](https://www.github.com/googleapis/python-speech/compare/v2.9.2...v2.9.3) (2021-10-04)


### Documentation

* **samples:** Remove reference to deprecated message "diarization_speaker_count" in favor of diarization_config ([#264](https://www.github.com/googleapis/python-speech/issues/264)) ([c1f7f35](https://www.github.com/googleapis/python-speech/commit/c1f7f357fe8367dafcdcb3d42e04a2619de2de62))

## [2.9.2](https://www.github.com/googleapis/python-speech/compare/v2.9.1...v2.9.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([a0bac07](https://www.github.com/googleapis/python-speech/commit/a0bac07de9f4e89c41d34a47d9e35ec6fd7edac3))

## [2.9.1](https://www.github.com/googleapis/python-speech/compare/v2.9.0...v2.9.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([e75ada8](https://www.github.com/googleapis/python-speech/commit/e75ada858d00b22fbae6d0de40771239d2f71756))

## [2.9.0](https://www.github.com/googleapis/python-speech/compare/v2.8.0...v2.9.0) (2021-09-20)


### Features

* add output_config request field ([#252](https://www.github.com/googleapis/python-speech/issues/252)) ([b9f856e](https://www.github.com/googleapis/python-speech/commit/b9f856e93cbb926e9531639a9bb50c654ff1033e))


### Documentation

* **samples:** fixed model adaptation sample to correctly refer to custom classes ([#246](https://www.github.com/googleapis/python-speech/issues/246)) ([5fa2433](https://www.github.com/googleapis/python-speech/commit/5fa243358ec5688a40ef0d5abf3802acfa931ea7))

## [2.8.0](https://www.github.com/googleapis/python-speech/compare/v2.7.0...v2.8.0) (2021-08-19)


### Features

* Add transcript normalization ([#235](https://www.github.com/googleapis/python-speech/issues/235)) ([f76effc](https://www.github.com/googleapis/python-speech/commit/f76effc3c5477db858571d89c5b52078e85ff94e))


### Documentation

* **samples:** remove io dependency in transcribe samples ([#223](https://www.github.com/googleapis/python-speech/issues/223)) ([928ca3a](https://www.github.com/googleapis/python-speech/commit/928ca3aeb8f8665dedfa7663c56ee3bb464481cd))

## [2.7.0](https://www.github.com/googleapis/python-speech/compare/v2.6.0...v2.7.0) (2021-08-10)


### Features

* add total_billed_time response field ([#224](https://www.github.com/googleapis/python-speech/issues/224)) ([07b5203](https://www.github.com/googleapis/python-speech/commit/07b5203a15a186aab537442a4f4a4071aab3046f))

## [2.6.0](https://www.github.com/googleapis/python-speech/compare/v2.5.1...v2.6.0) (2021-07-28)


### Features

* **v1p1beta1:** add total_billed_time response field ([#219](https://www.github.com/googleapis/python-speech/issues/219)) ([e7efa67](https://www.github.com/googleapis/python-speech/commit/e7efa6790111861084ff5a98a262432c04834dec))


### Bug Fixes

* enable self signed jwt for grpc ([#217](https://www.github.com/googleapis/python-speech/issues/217)) ([f43812c](https://www.github.com/googleapis/python-speech/commit/f43812ca164dd2b45ec4a73339291fa458be6be9))
* **v1p1beta1:** custom_class_id is required field in CreateCustomClassRequest. ([e7efa67](https://www.github.com/googleapis/python-speech/commit/e7efa6790111861084ff5a98a262432c04834dec))
* **v1p1beta1:** phrase_set_id is required field in CreatePhraseSetRequest ([e7efa67](https://www.github.com/googleapis/python-speech/commit/e7efa6790111861084ff5a98a262432c04834dec))


### Documentation

* **samples:** Add Spoken Punctuation and Emojis code samples ([#155](https://www.github.com/googleapis/python-speech/issues/155)) ([cc6b234](https://www.github.com/googleapis/python-speech/commit/cc6b2341cde1fec270afd500c8c5fe2b9023b346))
* add Samples section to CONTRIBUTING.rst ([#211](https://www.github.com/googleapis/python-speech/issues/211)) ([4b7e4c4](https://www.github.com/googleapis/python-speech/commit/4b7e4c46b57585f5db4adceca6ba5717d02ebb64))

## [2.5.1](https://www.github.com/googleapis/python-speech/compare/v2.5.0...v2.5.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#210](https://www.github.com/googleapis/python-speech/issues/210)) ([44d3f5b](https://www.github.com/googleapis/python-speech/commit/44d3f5b221955f196c41f9fdb74f2dbc0ea1c83d))

## [2.5.0](https://www.github.com/googleapis/python-speech/compare/v2.4.1...v2.5.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#191](https://www.github.com/googleapis/python-speech/issues/191)) ([0d84445](https://www.github.com/googleapis/python-speech/commit/0d8444543138f45445fc7995eccd5655376e0bfc))

## [2.4.1](https://www.github.com/googleapis/python-speech/compare/v2.4.0...v2.4.1) (2021-06-21)


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-speech/issues/1127)) ([#178](https://www.github.com/googleapis/python-speech/issues/178)) ([77d8d0e](https://www.github.com/googleapis/python-speech/commit/77d8d0ebc9924f965b86d3196e73170f875dd06f)), closes [#1126](https://www.github.com/googleapis/python-speech/issues/1126)

## [2.4.0](https://www.github.com/googleapis/python-speech/compare/v2.3.0...v2.4.0) (2021-05-22)


### Features

* add webm opus support ([eb360ae](https://www.github.com/googleapis/python-speech/commit/eb360aefdac09648852a073ef0837dc7c7b18679))
* support self-signed JWT flow for service accounts ([eb360ae](https://www.github.com/googleapis/python-speech/commit/eb360aefdac09648852a073ef0837dc7c7b18679))


### Bug Fixes

* add async client to %name_%version/init.py ([eb360ae](https://www.github.com/googleapis/python-speech/commit/eb360aefdac09648852a073ef0837dc7c7b18679))

## [2.3.0](https://www.github.com/googleapis/python-speech/compare/v2.2.1...v2.3.0) (2021-04-08)


### Features

* Support for spoken punctuation and spoken emojis ([#143](https://www.github.com/googleapis/python-speech/issues/143)) ([b6bddbe](https://www.github.com/googleapis/python-speech/commit/b6bddbe46172debd962c3d8e566a7c410fb4f279))

## [2.2.1](https://www.github.com/googleapis/python-speech/compare/v2.2.0...v2.2.1) (2021-03-31)


### Bug Fixes

* use correct retry deadline ([#134](https://www.github.com/googleapis/python-speech/issues/134)) ([07a30a1](https://www.github.com/googleapis/python-speech/commit/07a30a18ab4e38cca46af905cfd4221ce06daeb3))

## [2.2.0](https://www.github.com/googleapis/python-speech/compare/v2.1.0...v2.2.0) (2021-03-19)


### Features

* adds model adaptation sample ([#121](https://www.github.com/googleapis/python-speech/issues/121)) ([24b9424](https://www.github.com/googleapis/python-speech/commit/24b94247bab22b8fad15a251bff06ec8620f0f90))
* Support output transcript to Google Cloud Storage for LongRunningRecognize ([#128](https://www.github.com/googleapis/python-speech/issues/128)) ([5974564](https://www.github.com/googleapis/python-speech/commit/59745644b08328c883e71d53f3fcc5537644e3c7))

## [2.1.0](https://www.github.com/googleapis/python-speech/compare/v2.0.1...v2.1.0) (2021-02-26)


### Features

* add common resource helpers; expose transport; remove gRPC send/recv limits ([#100](https://www.github.com/googleapis/python-speech/issues/100)) ([b4700a6](https://www.github.com/googleapis/python-speech/commit/b4700a60569cb917f176ae1f504dadac1edb6ae8))
* add from_service_account_info factory ([3bed0b4](https://www.github.com/googleapis/python-speech/commit/3bed0b43c75be649e29475240c7f486fc9cd63dc))
* adds new multi region sample ([#96](https://www.github.com/googleapis/python-speech/issues/96)) ([a103f09](https://www.github.com/googleapis/python-speech/commit/a103f09fe6173f3acd8402f8c2a669ea3001ac6f))
* **v1p1beta1:** support Model Adaptation ([#104](https://www.github.com/googleapis/python-speech/issues/104)) ([3bed0b4](https://www.github.com/googleapis/python-speech/commit/3bed0b43c75be649e29475240c7f486fc9cd63dc))


### Bug Fixes

* Remove incorrect comment on enhanced models ([#95](https://www.github.com/googleapis/python-speech/issues/95)) ([8a02cee](https://www.github.com/googleapis/python-speech/commit/8a02ceeb5723b4d5075ab90bf64edefae9b81572))


### Documentation

* fix sphinx identifiers ([3bed0b4](https://www.github.com/googleapis/python-speech/commit/3bed0b43c75be649e29475240c7f486fc9cd63dc))
* updated setup documentation to point to python-speech instead of python-docs-samples ([#89](https://www.github.com/googleapis/python-speech/issues/89)) ([722e86e](https://www.github.com/googleapis/python-speech/commit/722e86e726831f7e44dbc8f0fb620a1ccd45f116))

## [2.0.1](https://www.github.com/googleapis/python-speech/compare/v2.0.0...v2.0.1) (2020-11-16)


### Bug Fixes

* deleted a line duplicating the call to the recognizer  ([#83](https://www.github.com/googleapis/python-speech/issues/83)) ([3ef6ce5](https://www.github.com/googleapis/python-speech/commit/3ef6ce5796126847acf231f67e2a2c9b52e27f5a))
* migrated samples to speech 2.0.0 ([#78](https://www.github.com/googleapis/python-speech/issues/78)) ([47dd992](https://www.github.com/googleapis/python-speech/commit/47dd99237d79f7e7b991f6a15733c6e04b00f563))

## [2.0.0](https://www.github.com/googleapis/python-speech/compare/v1.3.2...v2.0.0) (2020-09-24)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#61)

### Features

* Migrate to microgenerator ([#61](https://www.github.com/googleapis/python-speech/issues/61)) ([283b49d](https://www.github.com/googleapis/python-speech/commit/283b49d2cb34dcfcbd12038582ca3ed37e5ab90b)). See the [migration guide](https://github.com/googleapis/python-speech/blob/release-v2.0.0/UPGRADING.md) for details.


### Documentation

* remove example usage from READMe ([#46](https://www.github.com/googleapis/python-speech/issues/46)) ([4214630](https://www.github.com/googleapis/python-speech/commit/4214630c3318e6c9bc0a5156e20344956faf7d52))

## [1.3.2](https://www.github.com/googleapis/python-speech/compare/v1.3.1...v1.3.2) (2020-02-03)


### Bug Fixes

* **speech:** increase default timeout for v1p1beta1 (via synth) ([#9999](https://www.github.com/googleapis/python-speech/issues/9999)) ([e9b4919](https://www.github.com/googleapis/python-speech/commit/e9b4919f493a9206406944093fc1c3408b5f0265))
* **speech:** increase timeout values in client config (via synth) ([#9922](https://www.github.com/googleapis/python-speech/issues/9922)) ([8d34bea](https://www.github.com/googleapis/python-speech/commit/8d34beab73273e1b0965fe622af5434fdbac01ca))
* **speech:** mark `Recognize` idempotent (via synth) ([#9874](https://www.github.com/googleapis/python-speech/issues/9874)) ([a69e08c](https://www.github.com/googleapis/python-speech/commit/a69e08ce0bafcd9c4f1bafe51dce6e6b4716994f))
* **speech:** move 'speaker_tag' field from 'SpeakerDiarizationConfig' to 'WordInfo' (via synth) ([#9576](https://www.github.com/googleapis/python-speech/issues/9576)) ([2ba5ab9](https://www.github.com/googleapis/python-speech/commit/2ba5ab969e09df5cafcf67861c9d7d6cc91bd0ca))
* **speech:** re-add unused speaker_tag; update spacing in docs templates (via synth) ([#9765](https://www.github.com/googleapis/python-speech/issues/9765)) ([e1c5a54](https://www.github.com/googleapis/python-speech/commit/e1c5a54a321f5e76f074f8be1f5b6d5aedd612c7))

## 1.3.1

12-06-2019 13:05 PST

### Implementation Changes
- Increase timeout values in client config (via synth). ([#9922](https://github.com/googleapis/google-cloud-python/pull/9922))

## 1.3.0

11-21-2019 14:03 PST


### Implementation Changes
- Mark `Recognize` as idempotent (via synth). ([#9874](https://github.com/googleapis/google-cloud-python/pull/9874))
- Re-add unused `speaker_tag`; update spacing in docs templates (via synth). ([#9765](https://github.com/googleapis/google-cloud-python/pull/9765))
- Move `speaker_tag` field from `SpeakerDiarizationConfig` to `WordInfo` (via synth). ([#9576](https://github.com/googleapis/google-cloud-python/pull/9576))
- Remove send/recv msg size limit (via synth). ([#8969](https://github.com/googleapis/google-cloud-python/pull/8969))

### New Features
- Add speaker diarization configuration support (via synth). ([#9202](https://github.com/googleapis/google-cloud-python/pull/9202))
- Add `SpeakerDiarizationConfig`, deprecate enable_speaker_diarization and diarization_speaker_count (via synth). ([#8795](https://github.com/googleapis/google-cloud-python/pull/8795))

### Documentation
- Add python 2 sunset banner to documentation. ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))
- Reorder samples. ([#9313](https://github.com/googleapis/google-cloud-python/pull/9313))
- Update docstrings (via synth). ([#9292](https://github.com/googleapis/google-cloud-python/pull/9292))
- Fix intersphinx reference to requests. ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Add generated code samples. ([#9153](https://github.com/googleapis/google-cloud-python/pull/9153))
- Remove CI for gh-pages, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))
- Remove compatibility badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

### Internal / Testing Changes
- Add v1p1beta1 systests for longrunning / streaming recognize. ([#9287](https://github.com/googleapis/google-cloud-python/pull/9287))
- Add v1 systests for longrunning / streaming recognize. ([#9285](https://github.com/googleapis/google-cloud-python/pull/9285))
- Update samples manifest (via synth). ([#9211](https://github.com/googleapis/google-cloud-python/pull/9211))

## 1.2.0

07-24-2019 17:35 PDT

### New Features
- Add 'client_options' support (via synth). ([#8534](https://github.com/googleapis/google-cloud-python/pull/8534))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Pin black version (via synth). ([#8596](https://github.com/googleapis/google-cloud-python/pull/8596))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

## 1.1.0

06-27-2019 16:55 PDT

### Implementation Changes
- Allow kwargs to be passed to 'create_channel' (via synth). ([#8428](https://github.com/googleapis/google-cloud-python/pull/8428))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Increase speech max received msg size to 256 MiB ([#8338](https://github.com/googleapis/google-cloud-python/pull/8338))
- Add MP3 to Audio Encoding and add boost to Speech Context (via synth). ([#8109](https://github.com/googleapis/google-cloud-python/pull/8109))
- Add Recognition Metadata (via synth). ([#7961](https://github.com/googleapis/google-cloud-python/pull/7961))

### Documentation
- Update to show 'google-cloud-speech' is GA. ([#8453](https://github.com/googleapis/google-cloud-python/pull/8453))
- Tweak 'SpeechContext' docstring (via synth). ([#8223](https://github.com/googleapis/google-cloud-python/pull/8223))

### Internal / Testing Changes
- All: Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- (Re)-blacken (via synth). ([#8446](https://github.com/googleapis/google-cloud-python/pull/8446))
- Add disclaimer to auto-generated template files (via synth).  ([#8328](https://github.com/googleapis/google-cloud-python/pull/8328))
- Suppress checking 'cov-fail-under' in nox default session (via synth).  ([#8252](https://github.com/googleapis/google-cloud-python/pull/8252))
- Fix coverage in 'types.py' (via synth). ([#8164](https://github.com/googleapis/google-cloud-python/pull/8164))
- Blacken noxfile.py, setup.py (via synth). ([#8132](https://github.com/googleapis/google-cloud-python/pull/8132))
- Add empty lines. ([#8072](https://github.com/googleapis/google-cloud-python/pull/8072))
- Update noxfile (via synth). ([#7836](https://github.com/googleapis/google-cloud-python/pull/7836))
- Add nox session `docs` (via synth). ([#7782](https://github.com/googleapis/google-cloud-python/pull/7782))

## 1.0.0

03-18-2019 08:05 PDT


### Implementation Changes
- Remove unused message exports. ([#7275](https://github.com/googleapis/google-cloud-python/pull/7275))

### New Features
- Promote google-cloud-speech to GA ([#7525](https://github.com/googleapis/google-cloud-python/pull/7525))

### Documentation
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))

### Internal / Testing Changes
- Speech: copy lintified proto files (via synth).
- Add clarifying comment to blacken nox target. ([#7404](https://github.com/googleapis/google-cloud-python/pull/7404))
- Copy proto files alongside protoc versions. Remove unneeded utf-8 header.

## 0.36.3

01-31-2019 09:57 PST


### New Features
- Add 'RecognitionConfig.audio_channel_count' field via synth. ([#7240](https://github.com/googleapis/google-cloud-python/pull/7240))

### Documentation
- Modify file headers. ([#7158](https://github.com/googleapis/google-cloud-python/pull/7158))

### Internal / Testing Changes
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))

## 0.36.2

01-10-2019 15:36 PST

### Implementation Changes
- Protoc-generated serialization update. ([#7106](https://github.com/googleapis/google-cloud-python/pull/7106))

### Documentation
- Regenerate speech to change quote chars in docstr.
- Pick up stub docstring fix in GAPIC generator. ([#6982](https://github.com/googleapis/google-cloud-python/pull/6982))

## 0.36.1

12-18-2018 09:46 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAIPC generator. ([#6508](https://github.com/googleapis/google-cloud-python/pull/6508))
- Add `result_end_time`, docstring changes via synth. ([#6462](https://github.com/googleapis/google-cloud-python/pull/6462))
- Assorted synth fixups / cleanups ([#6400](https://github.com/googleapis/google-cloud-python/pull/6400))
- Fix `client_info` bug, update docstrings and timeouts. ([#6421](https://github.com/googleapis/google-cloud-python/pull/6421))
- Re-generate library using speech/synth.py ([#5979](https://github.com/googleapis/google-cloud-python/pull/5979))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Clarify passed arguments in speech examples. ([#6857](https://github.com/googleapis/google-cloud-python/pull/6857))
- Docs: normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Fix client library URL. ([#6052](https://github.com/googleapis/google-cloud-python/pull/6052))
- Prep docs for repo split. ([#6017](https://github.com/googleapis/google-cloud-python/pull/6017))

### Internal / Testing Changes
- Synth.metadata. ([#6868](https://github.com/googleapis/google-cloud-python/pull/6868))
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))

## 0.36.0

### New Features

- Re-generate the library to pick up changes and new features in the underlying API. ([#5915](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5915))

### Documentation

- Fix broken links to description of 'Beta' ([#5917](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5917))
- Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5901))

## 0.35.0

### Implementation Changes

- Re-generated the library to pick up new API features. (#5577)

### Internal / Testing Changes

- Add Test runs for Python 3.7 and remove 3.4 (#5295)
- Avoid overwriting '__module__' of messages from shared modules. (#5364)
- Modify system tests to use prerelease versions of grpcio (#5304)

## 0.34.0

### Implementation Changes
- Regenerate GAPIC to account for the removal of GoogleDataCollectionConfig and google_data_collection_opt_in  (#5235)

## 0.33.0

### New Features

- Add Audio Logging and Recognition Metadata. (#5123)

### Internal / Testing Changes

- Fix bad trove classifier

## 0.32.1

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)

## 0.31.1

### Bugfixes

- Fix speech helpers to properly pass retry and timeout args. (#4828, #4830)

## 0.31.0

This is the (hopefully) final release candidate before 1.0.

### Breaking Changes

- The deprecated Speech layer (deprecated since 0.27.0) has been removed. If you are still using  it, the [migration guide](https://cloud.google.com/speech/docs/python-client-migration) is still available.
- The following changes are _technically_ breaking but very unlikely to affect you directly:
  * `google.cloud.gapic.speech.v1` moved to `google.cloud.speech_v1.gapic`, in accordance with more recent clients.
  * `google.cloud.proto.speech.v1` moved to `google.cloud.speech_v1.proto`, in accordance with more recent clients.

### Dependencies

  * Removed dependency on `google-gax`.
  * Added dependency on `google-api-core`, its replacement.

## 0.30.0

### Documentation

- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)
- Deferring to `google-api-core` for `grpcio` and
  `googleapis-common-protos`dependencies (#4096, #4098)

PyPI: https://pypi.org/project/google-cloud-speech/0.30.0/
