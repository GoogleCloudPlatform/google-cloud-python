# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-ai-generativelanguage/#history

## [0.12.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.12.0...google-ai-generativelanguage-v0.12.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.12.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.11.0...google-ai-generativelanguage-v0.12.0) (2026-06-02)


### Features

* regenerate remaining packages (#17078) ([cc4f36f65e8b29d28f636e082435801b899cbca0](https://github.com/googleapis/google-cloud-python/commit/cc4f36f65e8b29d28f636e082435801b899cbca0))

## [0.11.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.10.0...google-ai-generativelanguage-v0.11.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.10.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.9.0...google-ai-generativelanguage-v0.10.0) (2026-01-08)


### Features

* add support for GoogleMaps and FileSearch tools ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* add support for RetrievalConfig ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* add IMAGE_RECITATION reason when generation is stopped due to recitation ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* add json_name for GenerationConfig.response_json_schema_ordered field ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* add support for GroundingMetadata.google_maps_widget_context_token ([17cc12897e6afdf3f3131531c50a8226a3f57c0f](https://github.com/googleapis/google-cloud-python/commit/17cc12897e6afdf3f3131531c50a8226a3f57c0f))
* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.9.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.8.0...google-ai-generativelanguage-v0.9.0) (2025-10-20)


### Documentation

* deprecation notice for HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))


### Features

* add support for additional reasons to stop image generation  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add support for finish_message that contain details the reason why the model stopped generating tokens  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add URL_RETRIEVAL_STATUS_UNSAFE and URL_RETRIEVAL_STATUS_PAYWALL statuses for url retrieval  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add log_probability_sum  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add Computer Use tool type  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add support for FunctionResponsePart  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add support for image generation features  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add support for additional reasons to stop image generation  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add support for raw media bytes for function response  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add log_probability_sum  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))
* add URL_RETRIEVAL_STATUS_UNSAFE and URL_RETRIEVAL_STATUS_PAYWALL statuses for url retrieval  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))


### Bug Fixes

* replaced GenerateVideoResponse by PredictLongRunningGeneratedVideoResponse field  ([84be9032eb7ba04bb305870160699d2bc12e0dac](https://github.com/googleapis/google-cloud-python/commit/84be9032eb7ba04bb305870160699d2bc12e0dac))

## [0.8.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.7.0...google-ai-generativelanguage-v0.8.0) (2025-10-16)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.7.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.18...google-ai-generativelanguage-v0.7.0) (2025-08-29)


### ⚠ BREAKING CHANGES

* add support for video_metadata

### Features

* add a flag whether the model supports thinking ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add a flag whether the model supports thinking ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add AudioTranscriptionConfig ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add MultiSpeakerVoiceConfig to speech config ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add support for function response scheduling in the conversation ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add support for thought_signature ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add support for UrlContextMetadata ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add support for video_metadata ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add time_range_filter to GoogleSearch tool type ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add UNEXPECTED_TOOL_CALL to the Candidate.FinishReason enum ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))
* add url_context to GoogleSearch tool type ([4d08928](https://github.com/googleapis/google-cloud-python/commit/4d08928433140722727f7953d5caefa5fc676c47))

## [0.6.18](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.17...google-ai-generativelanguage-v0.6.18) (2025-04-29)


### Features

* add CODE_RETRIEVAL_QUERY embedding task type ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add CODE_RETRIEVAL_QUERY embedding task type ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add language_code to speech config ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add minimum, maximum, any_of, property_ordering, default and null type to Schema ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add seed to GenerationConfig ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add support for live API (https://github.com/googleapis/go-genai/issues/275) ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add support for ModalityTokenCounts in UsageMetadata responses ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add support for ModalityTokenCounts in UsageMetadata responses ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add support for Veo: PredictLongRunning and generated/downloadable files ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))
* add ThinkingConfig, MediaResolution, and seed to GenerationConfig ([d530650](https://github.com/googleapis/google-cloud-python/commit/d530650ea02714abaef4c8295717d286743ed4f1))

## [0.6.17](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.16...google-ai-generativelanguage-v0.6.17) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([a1b9294](https://github.com/googleapis/google-cloud-python/commit/a1b9294d0bf6e27c2a951d6df7faf7807dc5420b))

## [0.6.16](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.15...google-ai-generativelanguage-v0.6.16) (2025-02-12)


### Features

* Add REST Interceptors which support reading metadata ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))
* Add support for reading selective GAPIC generation methods from service YAML ([a961bc0](https://github.com/googleapis/google-cloud-python/commit/a961bc029201b72fc4923490aeb3d82781853e6a))

## [0.6.15](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.14...google-ai-generativelanguage-v0.6.15) (2025-01-13)


### Features

* Add BidiGenerateContent + all the necessary protos ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add civic_integrity toggle to generation_config ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add GoogleSearch tool type ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add id to FunctionCall and FunctionResponse ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add image_safety block_reason + finish_reason ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add response_modalities to generation_config ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add return type `Schema response` to function declarations ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add TuningMultiturnExample ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add v1alpha ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))
* Add voice_config to generation_config ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))


### Documentation

* Update safety filter list to include civic_integrity ([2c1e359](https://github.com/googleapis/google-cloud-python/commit/2c1e35981f7064f293669109097eb4b8c4942692))

## [0.6.14](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.13...google-ai-generativelanguage-v0.6.14) (2024-12-12)


### Features

* Add support for opt-in debug logging ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))


### Bug Fixes

* Fix typing issue with gRPC metadata when key ends in -bin ([b1dfc55](https://github.com/googleapis/google-cloud-python/commit/b1dfc556d4652a48564ff37becb31d5a06ee2b5b))

## [0.6.13](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.12...google-ai-generativelanguage-v0.6.13) (2024-11-21)


### Features

* Add GroundingMetadata.web_search_queries ([3535963](https://github.com/googleapis/google-cloud-python/commit/353596382dc59c4df75071846578ad09d5130e76))
* Adds `GenerateContentResponse.model_version` output ([3535963](https://github.com/googleapis/google-cloud-python/commit/353596382dc59c4df75071846578ad09d5130e76))
* Adds search grounding ([3535963](https://github.com/googleapis/google-cloud-python/commit/353596382dc59c4df75071846578ad09d5130e76))


### Documentation

* Some small updates. ([3535963](https://github.com/googleapis/google-cloud-python/commit/353596382dc59c4df75071846578ad09d5130e76))

## [0.6.12](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.11...google-ai-generativelanguage-v0.6.12) (2024-10-31)


### Bug Fixes

* disable universe-domain validation ([85c7512](https://github.com/googleapis/google-cloud-python/commit/85c7512bbdde2b9cc60b4ad42b8c36c4558a07a5))

## [0.6.11](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.10...google-ai-generativelanguage-v0.6.11) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13199](https://github.com/googleapis/google-cloud-python/issues/13199)) ([2fc3726](https://github.com/googleapis/google-cloud-python/commit/2fc372685731141ca1ed2a917dd18bacd79db88e))

## [0.6.10](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.9...google-ai-generativelanguage-v0.6.10) (2024-09-23)


### Features

* Add GenerationConfig.{presence_penalty, frequency_penalty, logprobs, response_logprobs, logprobs} and Candidate.{avg_logprobs, logprobs_result} ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Add GoogleSearchRetrieval tool and candidate.grounding_metadata ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Add HarmBlockThreshold.OFF ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Add HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Add PredictionService (for Imagen) ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Add Schema.min_items ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Add TunedModels.reader_project_numbers ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))


### Documentation

* Small fixes ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))
* Tag HarmCategories by the model family they're used on. ([d6238e4](https://github.com/googleapis/google-cloud-python/commit/d6238e49a17caf54dd0fbc45215527beed057cc5))

## [0.6.9](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.8...google-ai-generativelanguage-v0.6.9) (2024-08-19)


### Features

* Add model max_temperature ([fdebbf2](https://github.com/googleapis/google-cloud-python/commit/fdebbf2e914e9a8ed5a31a04ce9fe26de0f69c72))
* Add new PromptFeedback and FinishReason entries ([fdebbf2](https://github.com/googleapis/google-cloud-python/commit/fdebbf2e914e9a8ed5a31a04ce9fe26de0f69c72))
* Add new PromptFeedback and FinishReason entries for https://github.com/google-gemini/generative-ai-python/issues/476 ([fdebbf2](https://github.com/googleapis/google-cloud-python/commit/fdebbf2e914e9a8ed5a31a04ce9fe26de0f69c72))


### Documentation

* Many small fixes ([fdebbf2](https://github.com/googleapis/google-cloud-python/commit/fdebbf2e914e9a8ed5a31a04ce9fe26de0f69c72))

## [0.6.8](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.7...google-ai-generativelanguage-v0.6.8) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([c6eeae0](https://github.com/googleapis/google-cloud-python/commit/c6eeae00de802d98badd3de879ce5e870ba60a3a))

## [0.6.7](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.6...google-ai-generativelanguage-v0.6.7) (2024-07-08)


### Bug Fixes

* Allow Protobuf 5.x ([#12863](https://github.com/googleapis/google-cloud-python/issues/12863)) ([3e6e423](https://github.com/googleapis/google-cloud-python/commit/3e6e423b86cdace8538f610941aa84c7a6217934))

## [0.6.6](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.5...google-ai-generativelanguage-v0.6.6) (2024-06-26)


### Features

* [google-ai-generativelanguage] Add code execution ([#12843](https://github.com/googleapis/google-cloud-python/issues/12843)) ([e4fcb00](https://github.com/googleapis/google-cloud-python/commit/e4fcb0097b4f6debbcf584bd3d35a8281a954cfd))

## [0.6.5](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.4...google-ai-generativelanguage-v0.6.5) (2024-06-11)


### Features

* Add cached_content_token_count to CountTokensResponse ([09c7fae](https://github.com/googleapis/google-cloud-python/commit/09c7fae459bc3eb91bfcb795384245e7fa4bf7ff))
* Add cached_content_token_count to generative_service's UsageMetadata ([09c7fae](https://github.com/googleapis/google-cloud-python/commit/09c7fae459bc3eb91bfcb795384245e7fa4bf7ff))
* Add content caching ([09c7fae](https://github.com/googleapis/google-cloud-python/commit/09c7fae459bc3eb91bfcb795384245e7fa4bf7ff))


### Documentation

* Small fixes ([09c7fae](https://github.com/googleapis/google-cloud-python/commit/09c7fae459bc3eb91bfcb795384245e7fa4bf7ff))

## [0.6.4](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.3...google-ai-generativelanguage-v0.6.4) (2024-05-16)


### Features

* **v1:** Add generate_content_request to CountTokensRequest ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))
* **v1:** Add usage metadata to GenerateContentResponse ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))
* **v1beta:** Add video metadata to files API ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))
* **v1beta:** Update timeouts for generate content ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))
* **v1:** Update timeouts ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))


### Documentation

* **v1beta:** Minor updates ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))
* **v1:** Minor updates ([e5dd7ed](https://github.com/googleapis/google-cloud-python/commit/e5dd7eddcea1f3f22a023a42e0cc80d93a06ccfc))

## [0.6.3](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.2...google-ai-generativelanguage-v0.6.3) (2024-05-07)


### Features

* [google-ai-generativelanguage] Add FileState to File ([#12660](https://github.com/googleapis/google-cloud-python/issues/12660)) ([88848eb](https://github.com/googleapis/google-cloud-python/commit/88848eb17a536e5e69fe4f7098604741bb621549))

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.1...google-ai-generativelanguage-v0.6.2) (2024-04-15)


### Features

* **v1:** Add `output dimensionality` to `EmbedContentRequest` message ([e3bfbc6](https://github.com/googleapis/google-cloud-python/commit/e3bfbc6d55935b2120f282926aae1c4683f8e0ca))
* **v1:** Add `QUESTION_ANSWERING` and `FACT_VERIFICATION` to `TaskType` Enum ([e3bfbc6](https://github.com/googleapis/google-cloud-python/commit/e3bfbc6d55935b2120f282926aae1c4683f8e0ca))
* **v1:** Add rest binding for tuned models ([e3bfbc6](https://github.com/googleapis/google-cloud-python/commit/e3bfbc6d55935b2120f282926aae1c4683f8e0ca))
* **v1beta:** Add `output dimensionality` to `EmbedContentRequest` message ([e2cf0c4](https://github.com/googleapis/google-cloud-python/commit/e2cf0c45ea82e6cb6144d6702d68b47099da0376))
* **v1beta:** Add `QUESTION_ANSWERING` and `FACT_VERIFICATION` to `TaskType` Enum ([e2cf0c4](https://github.com/googleapis/google-cloud-python/commit/e2cf0c45ea82e6cb6144d6702d68b47099da0376))
* **v1beta:** Add `response_mime_type` to `GenerationConfig` message ([e2cf0c4](https://github.com/googleapis/google-cloud-python/commit/e2cf0c45ea82e6cb6144d6702d68b47099da0376))


### Documentation

* **v1beta:** A bunch of small fixes ([e2cf0c4](https://github.com/googleapis/google-cloud-python/commit/e2cf0c45ea82e6cb6144d6702d68b47099da0376))
* **v1:** Lots of small fixes ([e3bfbc6](https://github.com/googleapis/google-cloud-python/commit/e3bfbc6d55935b2120f282926aae1c4683f8e0ca))

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.6.0...google-ai-generativelanguage-v0.6.1) (2024-04-03)


### Features

* Add file upload service ([c0a0bf6](https://github.com/googleapis/google-cloud-python/commit/c0a0bf61ab85888c186332a761044994885bec62))
* Add file_data to part options ([c0a0bf6](https://github.com/googleapis/google-cloud-python/commit/c0a0bf61ab85888c186332a761044994885bec62))
* Add system instructions ([c0a0bf6](https://github.com/googleapis/google-cloud-python/commit/c0a0bf61ab85888c186332a761044994885bec62))
* Add tool_config ([c0a0bf6](https://github.com/googleapis/google-cloud-python/commit/c0a0bf61ab85888c186332a761044994885bec62))


### Documentation

* A comment for field `candidate_count` in message `.[google.ai](https://www.google.com/url?sa=D&q=http%3A%2F%2Fgoogle.ai).generativelanguage.v1beta.GenerationConfig` is changed ([c0a0bf6](https://github.com/googleapis/google-cloud-python/commit/c0a0bf61ab85888c186332a761044994885bec62))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.4...google-ai-generativelanguage-v0.6.0) (2024-03-22)


### ⚠ BREAKING CHANGES

* make learning rate a one-of

### Features

* Add `learning_rate_multiplier` to tuning `Hyperparameters` ([35017ea](https://github.com/googleapis/google-cloud-python/commit/35017ea297f47f9dd9de3e1a881e05ae6705baae))


### Bug Fixes

* make learning rate a one-of ([35017ea](https://github.com/googleapis/google-cloud-python/commit/35017ea297f47f9dd9de3e1a881e05ae6705baae))


### Documentation

* A few small updates ([35017ea](https://github.com/googleapis/google-cloud-python/commit/35017ea297f47f9dd9de3e1a881e05ae6705baae))

## [0.5.4](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.3...google-ai-generativelanguage-v0.5.4) (2024-03-05)


### Bug Fixes

* **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#12381](https://github.com/googleapis/google-cloud-python/issues/12381)) ([48ae8ab](https://github.com/googleapis/google-cloud-python/commit/48ae8aba7ec71a382e001b3a659022f942c3b436))

## [0.5.3](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.2...google-ai-generativelanguage-v0.5.3) (2024-02-22)


### Bug Fixes

* [Many APIs] fix `ValueError` in `test__validate_universe_domain` ([#12280](https://github.com/googleapis/google-cloud-python/issues/12280)) ([2d75d0e](https://github.com/googleapis/google-cloud-python/commit/2d75d0e67ca4cccddc688bd37c14ac80564a2e65))
* **deps:** [Many APIs] Require `google-api-core&gt;=1.34.1` ([#12303](https://github.com/googleapis/google-cloud-python/issues/12303)) ([fbb80c3](https://github.com/googleapis/google-cloud-python/commit/fbb80c32f7db91e25bd1cc30966f630728ff6d6a))

## [0.5.2](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.1...google-ai-generativelanguage-v0.5.2) (2024-02-06)


### Bug Fixes

* Add google-auth as a direct dependency ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Add staticmethod decorator to _get_client_cert_source and _get_api_endpoint ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))
* Resolve AttributeError 'Credentials' object has no attribute 'universe_domain' ([780c5f1](https://github.com/googleapis/google-cloud-python/commit/780c5f15d4099da6b5c3b966267bc7d7c63d6303))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.5.0...google-ai-generativelanguage-v0.5.1) (2024-02-01)


### Features

* Allow users to explicitly configure universe domain ([a0392ee](https://github.com/googleapis/google-cloud-python/commit/a0392eeb59fcc6ea7c55283110b92aa24a4d40a0))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.4.1...google-ai-generativelanguage-v0.5.0) (2024-01-24)


### ⚠ BREAKING CHANGES

* Fix content.proto's Schema - `type` should be required

### Features

* Update GenAI libraries to include input_safety_feedback ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))


### Bug Fixes

* Fix content.proto's Schema - `type` should be required ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))


### Documentation

* Minor docs updates ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))
* Update summary, improve description for `title` in `EmbedContentRequest` ([d2004d4](https://github.com/googleapis/google-cloud-python/commit/d2004d4a1c95333017b585ba905d5e0c4af45776))

## [0.4.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.4.0...google-ai-generativelanguage-v0.4.1) (2024-01-22)


### Documentation

* [google-ai-generativelanguage] Fixed minor documentation typos for field `function_declarations` in message `google.ai.generativelanguage.v1beta.Tool` ([#12206](https://github.com/googleapis/google-cloud-python/issues/12206)) ([52957f3](https://github.com/googleapis/google-cloud-python/commit/52957f38e2d5dca5e873cfc7239a6ce469ed541f))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.5...google-ai-generativelanguage-v0.4.0) (2023-12-09)


### Features

* Add v1, contains only GenerativeService, nothing else ([23d8814](https://github.com/googleapis/google-cloud-python/commit/23d8814baa6288d94484d52a98714fd32755ada3))
* Add v1beta, adds GenerativeService and RetrievalService ([23d8814](https://github.com/googleapis/google-cloud-python/commit/23d8814baa6288d94484d52a98714fd32755ada3))
* Set `google.ai.generativelanguage_v1beta` as the default import ([23d8814](https://github.com/googleapis/google-cloud-python/commit/23d8814baa6288d94484d52a98714fd32755ada3))

## [0.3.5](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.4...google-ai-generativelanguage-v0.3.5) (2023-12-07)


### Features

* Add support for python 3.12 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Introduce compatibility with native namespace packages ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))
* Use `retry_async` instead of `retry` in async client ([ea6cfc2](https://github.com/googleapis/google-cloud-python/commit/ea6cfc2f86e77757b8cb05f7fd0d9c0b7ccaf7cf))

## [0.3.4](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.3...google-ai-generativelanguage-v0.3.4) (2023-09-30)


### Documentation

* Minor formatting ([#11630](https://github.com/googleapis/google-cloud-python/issues/11630)) ([b176996](https://github.com/googleapis/google-cloud-python/commit/b176996309cb5b3e9c257caaebde8884bd556824))

## [0.3.3](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.2...google-ai-generativelanguage-v0.3.3) (2023-09-21)


### Bug Fixes

* set google.ai.generativelanguage_v1beta3 as the default import ([#11677](https://github.com/googleapis/google-cloud-python/issues/11677)) ([39ea699](https://github.com/googleapis/google-cloud-python/commit/39ea699f6c3957f2ae20990555b9f47c1b285f31))

## [0.3.2](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.1...google-ai-generativelanguage-v0.3.2) (2023-09-20)


### Features

* Add BatchEmbedText and CountTextTokens to the text service ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))
* Add google/ai/generativelanguage_v1beta3  ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))
* Add model tuning ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))
* Add permissions service ([38f2ca3](https://github.com/googleapis/google-cloud-python/commit/38f2ca3b3356c0fb42ebdf341dd548836c0896f3))

## [0.3.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.3.0...google-ai-generativelanguage-v0.3.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11444](https://github.com/googleapis/google-cloud-python/issues/11444)) ([9aa301a](https://github.com/googleapis/google-cloud-python/commit/9aa301ae6ca3080cae286a19de9cdc1b796ab37d))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.2.1...google-ai-generativelanguage-v0.3.0) (2023-06-29)


### Bug Fixes

* remove `BLOCK_NONE` from `HarmBlockThreshold` ([9d46f7f](https://github.com/googleapis/google-cloud-python/commit/9d46f7f5c6d2f84b8e351969d4ab17b4195b941b))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.2.0...google-ai-generativelanguage-v0.2.1) (2023-06-03)


### Documentation

* fix broken client library documentation links ([#11192](https://github.com/googleapis/google-cloud-python/issues/11192)) ([5e17f7a](https://github.com/googleapis/google-cloud-python/commit/5e17f7a901bbbae8ff9a44ed62f1abd2386da2c8))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-ai-generativelanguage-v0.1.0...google-ai-generativelanguage-v0.2.0) (2023-05-05)


### Features

* Add safety settings ([#11148](https://github.com/googleapis/google-cloud-python/issues/11148)) ([f9544c9](https://github.com/googleapis/google-cloud-python/commit/f9544c9897dd4d010c5b8703c744d8f28ae3b070))

## 0.1.0 (2023-05-02)


### Features

* add initial files for google.ai.generativelanguage.v1beta2 ([#11142](https://github.com/googleapis/google-cloud-python/issues/11142)) ([54363fd](https://github.com/googleapis/google-cloud-python/commit/54363fd60decdecb05302fc9bce8e278eb39951e))

## Changelog
