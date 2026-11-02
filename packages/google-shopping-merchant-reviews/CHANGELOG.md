# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-shopping-merchant-reviews/#history

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.6.1...google-shopping-merchant-reviews-v0.6.2) (2026-10-23)


### Features

* **google/shopping/merchant/reviews/v1:** add google-shopping-merchant-reviews ([#18801](https://github.com/googleapis/google-cloud-python/issues/18801)) ([c4a6a21](https://github.com/googleapis/google-cloud-python/commit/c4a6a211a625e44c2b4e74be995c5ef6d85b4dc2))

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.6.0...google-shopping-merchant-reviews-v0.6.1) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.5.0...google-shopping-merchant-reviews-v0.6.0) (2026-06-02)


### Features

* regenerate google-shopping packages (#17072) ([2904f059a0eb610180ccd7f3d169c130a1696333](https://github.com/googleapis/google-cloud-python/commit/2904f059a0eb610180ccd7f3d169c130a1696333))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.4.0...google-shopping-merchant-reviews-v0.5.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* update image to us-central1-docker.pkg.dev/cloud-sdk-librarian-prod/images-prod/python-librarian-generator@sha256:f5426423676c75008c2135037e7b98f78cbb99f78b3c46fe043b6897be92d836 ([3654fe76d755dd8db62ece81d5770ec58b3624df](https://github.com/googleapis/google-cloud-python/commit/3654fe76d755dd8db62ece81d5770ec58b3624df))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.3.0...google-shopping-merchant-reviews-v0.4.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.2.0...google-shopping-merchant-reviews-v0.3.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.1.4...google-shopping-merchant-reviews-v0.2.0) (2025-07-26)


### ⚠ BREAKING CHANGES

* An existing field `attributes` is renamed to `merchant_review_attributes` in message `.google.shopping.merchant.reviews.v1beta.MerchantReview`
* An existing field `attributes` is renamed to `product_review_attributes` in message `.google.shopping.merchant.reviews.v1beta.ProductReview`

### Bug Fixes

* An existing field `attributes` is renamed to `merchant_review_attributes` in message `.google.shopping.merchant.reviews.v1beta.MerchantReview` ([2273ea0](https://github.com/googleapis/google-cloud-python/commit/2273ea09476b80f7927e9eb54af85cd0ab431438))
* An existing field `attributes` is renamed to `product_review_attributes` in message `.google.shopping.merchant.reviews.v1beta.ProductReview` ([2273ea0](https://github.com/googleapis/google-cloud-python/commit/2273ea09476b80f7927e9eb54af85cd0ab431438))

## [0.1.4](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.1.3...google-shopping-merchant-reviews-v0.1.4) (2025-07-10)


### Features

* A new field `is_incentivized_review` is added to message `.google.shopping.merchant.reviews.v1beta.ProductReviewAttributes` ([c2b35a3](https://github.com/googleapis/google-cloud-python/commit/c2b35a370a3d9414e817fb61848ac283b5af1f0a))
* A new field `is_verified_purchase` is added to message `.google.shopping.merchant.reviews.v1beta.ProductReviewAttributes` ([c2b35a3](https://github.com/googleapis/google-cloud-python/commit/c2b35a370a3d9414e817fb61848ac283b5af1f0a))


### Documentation

* A comment for field `content` in message `.google.shopping.merchant.reviews.v1beta.ProductReviewAttributes` is changed ([c2b35a3](https://github.com/googleapis/google-cloud-python/commit/c2b35a370a3d9414e817fb61848ac283b5af1f0a))
* A comment for field `review_language` in message `.google.shopping.merchant.reviews.v1beta.MerchantReviewAttributes` is changed ([c2b35a3](https://github.com/googleapis/google-cloud-python/commit/c2b35a370a3d9414e817fb61848ac283b5af1f0a))
* A comment for field custom_attributes in message .google.shopping.merchant.reviews.v1beta.MerchantReview is changed ([c2b35a3](https://github.com/googleapis/google-cloud-python/commit/c2b35a370a3d9414e817fb61848ac283b5af1f0a))

## [0.1.3](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.1.2...google-shopping-merchant-reviews-v0.1.3) (2025-06-11)


### Documentation

* Update import statement example in README ([4f0a027](https://github.com/googleapis/google-cloud-python/commit/4f0a0270b494d47e80373b87e7668283dbbceec7))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.1.1...google-shopping-merchant-reviews-v0.1.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([36e8ba1](https://github.com/googleapis/google-cloud-python/commit/36e8ba12eac92dd221ac3ddf1061da3845135791))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-reviews-v0.1.0...google-shopping-merchant-reviews-v0.1.1) (2025-02-18)


### Features

* Add REST Interceptors which support reading metadata ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))
* Add support for reading selective GAPIC generation methods from service YAML ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))

## 0.1.0 (2024-12-12)


### Features

* add initial files for google.shopping.merchant.reviews.v1beta ([#13351](https://github.com/googleapis/google-cloud-python/issues/13351)) ([11a3ff2](https://github.com/googleapis/google-cloud-python/commit/11a3ff2f0669f06e385c63b57c6b1562b6c36da0))

## Changelog
