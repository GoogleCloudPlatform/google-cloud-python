# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-shopping-merchant-products/#history

## [1.9.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.8.0...google-shopping-merchant-products-v1.9.0) (2026-10-01)


### Features

* declare Python3.15 support ([8775794](https://github.com/googleapis/google-cloud-python/commit/8775794508e17150023c8e7152543410014458bf))
* update API sources and regenerate ([#18513](https://github.com/googleapis/google-cloud-python/issues/18513)) ([7d7adca](https://github.com/googleapis/google-cloud-python/commit/7d7adcaee688603077ea53abec678130045c20ed))

## [1.8.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.7.0...google-shopping-merchant-products-v1.8.0) (2026-07-16)


### Features

* update googleapis and regenerate ([#17725](https://github.com/googleapis/google-cloud-python/issues/17725)) ([35e16da](https://github.com/googleapis/google-cloud-python/commit/35e16daf25480d66e9fc3443fe485ae2b0241ae3))

## [1.7.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.6.0...google-shopping-merchant-products-v1.7.0) (2026-06-02)


### Features

* regenerate google-shopping packages (#17072) ([2904f059a0eb610180ccd7f3d169c130a1696333](https://github.com/googleapis/google-cloud-python/commit/2904f059a0eb610180ccd7f3d169c130a1696333))

## [1.6.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.5.0...google-shopping-merchant-products-v1.6.0) (2026-05-06)

## [1.5.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.4.0...google-shopping-merchant-products-v1.5.0) (2026-03-26)


### Features

* Allow Protobuf 7.x ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))


### Bug Fixes

* Require Python 3.9 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Require google-api-core >= 2.11.0 ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))
* Improve type checking ([1eb7c268482e55971966e284dac2cbeb903adcbb](https://github.com/googleapis/google-cloud-python/commit/1eb7c268482e55971966e284dac2cbeb903adcbb))

## [1.4.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.3.0...google-shopping-merchant-products-v1.4.0) (2026-03-23)


### Documentation

* Updated various comments, including links to data source creation guides ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))
* Updated comments for several fields, including product name formats, data source creation, destination field descriptions (now also referred to as Marketing Methods), and the default page size for `ListProductsRequest` ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))


### Features

* update products_common fields to include `handling_cutoff_timezone `, `shipping_handling_business_days`, `shipping_transit_business_days` ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))
* Added the `product_id_base64_url_encoded` field to `InsertProductInputRequest`, `DeleteProductInputRequest`, and `GetProductRequest`. This allows for product IDs containing special characters to be correctly handled when unpadded base64url-encoded ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))
* Added several fields to enhance shipping configurations: - `handling_cutoff_time` and `handling_cutoff_timezone` within the `Shipping` message - `ShippingBusinessDaysConfig` message to define business days for shipping - `shipping_handling_business_days` and `shipping_transit_business_days` in `ProductAttributes` - `HandlingCutoffTime` message to configure country-specific handling cutoffs - `handling_cutoff_times` array in `ProductAttributes` ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))
* Added `handling_cutoff_time` and `handling_cutoff_timezone` fields to the `Shipping` message within `Attributes` ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))
* Added C#, PHP, and Ruby namespace options to ProductInputs, Products, and ProductsCommon proto files for improved client library generation ([ee7dd7dc168ecf943440cef38efff348e8eff095](https://github.com/googleapis/google-cloud-python/commit/ee7dd7dc168ecf943440cef38efff348e8eff095))

## [1.3.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.2.0...google-shopping-merchant-products-v1.3.0) (2026-01-09)


### Features

* auto-enable mTLS when supported certificates are detected ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))
* check Python and dependency versions in generated GAPICs ([c353aa5bcc937ef9399c8efc90492dadbcf01aa2](https://github.com/googleapis/google-cloud-python/commit/c353aa5bcc937ef9399c8efc90492dadbcf01aa2))

## [1.2.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.1.0...google-shopping-merchant-products-v1.2.0) (2025-10-20)


### Features

* Add support for Python 3.14  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))


### Bug Fixes

* Deprecate credentials_file argument  ([98ee71abc0f97c88239b50bf0e0827df19630def](https://github.com/googleapis/google-cloud-python/commit/98ee71abc0f97c88239b50bf0e0827df19630def))

## [1.1.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v1.0.0...google-shopping-merchant-products-v1.1.0) (2025-10-07)


### Features

* [google-shopping-merchant-products] Include CarrierShipping field inside the Products attribute A new feature inside the `ProductAttributes`, `carrier_shipping` field allows for configuring a carrier shipping policy by indicating the carrier service of use for cost, speed or both.  ([4e5a0b50d1919fdc592478184e349d8e3ef0b658](https://github.com/googleapis/google-cloud-python/commit/4e5a0b50d1919fdc592478184e349d8e3ef0b658))

## [1.0.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.7...google-shopping-merchant-products-v1.0.0) (2025-08-29)


### ⚠ BREAKING CHANGES

* set `google.shopping.merchant_products_v1` as the default import for `google.shopping.merchant_products`

### Features

* set `google.shopping.merchant_products_v1` as the default import for `google.shopping.merchant_products` ([7730040](https://github.com/googleapis/google-cloud-python/commit/773004018ffc585c36910add9956da5103773c81))
* update release level to stable ([7730040](https://github.com/googleapis/google-cloud-python/commit/773004018ffc585c36910add9956da5103773c81))

## [0.2.7](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.6...google-shopping-merchant-products-v0.2.7) (2025-08-06)


### Features

* [google-shopping-merchant-products] add products API client libraries for v1 ([#14183](https://github.com/googleapis/google-cloud-python/issues/14183)) ([4ae9435](https://github.com/googleapis/google-cloud-python/commit/4ae943546302636866015825a527b1a6ff9c0efa))

## [0.2.6](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.5...google-shopping-merchant-products-v0.2.6) (2025-07-10)


### Features

* A new field `gtins` is added to message `.google.shopping.merchant.products.v1beta.Attributes` ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A new field `maximum_retail_price` is added to message `.google.shopping.merchant.products.v1beta.Attributes` ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))


### Documentation

* A comment for field `ads_grouping` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `auto_pricing_min_price` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `availability` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `brand` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `color` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `condition` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `custom_attributes` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `custom_label_0` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `custom_label_1` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `custom_label_2` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `custom_label_3` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `custom_label_4` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `data_source` in message `.google.shopping.merchant.products.v1beta.DeleteProductInputRequest` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `data_source` in message `.google.shopping.merchant.products.v1beta.InsertProductInputRequest` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `data_source` in message `.google.shopping.merchant.products.v1beta.UpdateProductInputRequest` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `disclosure_date` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `display_ads_similar_ids` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `display_ads_value` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `excluded_destinations` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `feed_label` in message `.google.shopping.merchant.products.v1beta.Product` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `feed_label` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `gender` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `gtin` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `included_destinations` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `is_bundle` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `link_template` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `material` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `mobile_link_template` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `multipack` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `name` in message `.google.shopping.merchant.products.v1beta.DeleteProductInputRequest` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `name` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `page_size` in message `.google.shopping.merchant.products.v1beta.ListProductsRequest` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `parent` in message `.google.shopping.merchant.products.v1beta.InsertProductInputRequest` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `pattern` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `pickup_method` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `pickup_sla` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `product_highlights` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `product_types` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `product` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `program_label` in message `.google.shopping.merchant.products.v1beta.LoyaltyProgram` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `resolution` in message `.google.shopping.merchant.products.v1beta.ProductStatus` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `sale_price_effective_date` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `shopping_ads_excluded_countries` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `size_system` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `size_types` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `size` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `tax_category` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for field `version_number` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for message `ProductInput` is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))
* A comment for method InsertProductInput in service ProductInputsService is changed ([3acc2d9](https://github.com/googleapis/google-cloud-python/commit/3acc2d9ac8f2ce6d3ba901e0e0d8b5cb37eea15d))

## [0.2.5](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.4...google-shopping-merchant-products-v0.2.5) (2025-06-11)


### Documentation

* Update import statement example in README ([8066d24](https://github.com/googleapis/google-cloud-python/commit/8066d24068e6d036dcf77e7abb5401a5ba3f8a63))

## [0.2.4](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.3...google-shopping-merchant-products-v0.2.4) (2025-04-12)


### Features

* A new field `automated_discounts` is added to message `google.shopping.merchant.products.v1beta.Product` ([62f7efa](https://github.com/googleapis/google-cloud-python/commit/62f7efa2ac8a06f36feef5e9c887aa31e55bca33))


### Documentation

* Modified several comments ([62f7efa](https://github.com/googleapis/google-cloud-python/commit/62f7efa2ac8a06f36feef5e9c887aa31e55bca33))

## [0.2.3](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.2...google-shopping-merchant-products-v0.2.3) (2025-03-19)


### Features

* Add an update method ([5cde00f](https://github.com/googleapis/google-cloud-python/commit/5cde00f98c05b2bf3c996ced62c81d4f81be8df2))


### Documentation

* A comment for field `channel` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([5cde00f](https://github.com/googleapis/google-cloud-python/commit/5cde00f98c05b2bf3c996ced62c81d4f81be8df2))
* A comment for field `data_source` in message `.google.shopping.merchant.products.v1beta.InsertProductInputRequest` is changed ([5cde00f](https://github.com/googleapis/google-cloud-python/commit/5cde00f98c05b2bf3c996ced62c81d4f81be8df2))
* A comment for message `ProductInput` is changed ([5cde00f](https://github.com/googleapis/google-cloud-python/commit/5cde00f98c05b2bf3c996ced62c81d4f81be8df2))

## [0.2.2](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.1...google-shopping-merchant-products-v0.2.2) (2025-03-15)


### Bug Fixes

* [Many APIs] Allow Protobuf 6.x ([25ced24](https://github.com/googleapis/google-cloud-python/commit/25ced2444528a1dc6a22daa32b82b844961f1b75))

## [0.2.1](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.2.0...google-shopping-merchant-products-v0.2.1) (2025-02-18)


### Features

* Add REST Interceptors which support reading metadata ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))
* Add support for reading selective GAPIC generation methods from service YAML ([30b675e](https://github.com/googleapis/google-cloud-python/commit/30b675e7e9eaee87f9e7bdf4dc910b01f6a3044f))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.1.4...google-shopping-merchant-products-v0.2.0) (2024-12-12)


### ⚠ BREAKING CHANGES

* Changed repeated flag of an existing field `gtin` in message `.google.shopping.merchant.products.v1beta.Attributes`
* An existing field `gtin` is moved out of oneof in message `.google.shopping.merchant.products.v1beta.Attributes`

### Features

* A new field `member_price_effective_date` is added to message `.google.shopping.merchant.products.v1beta.LoyaltyProgram` ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A new field `shipping_label` is added to message `.google.shopping.merchant.products.v1beta.LoyaltyProgram` ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* Add support for opt-in debug logging ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))


### Bug Fixes

* An existing field `gtin` is moved out of oneof in message `.google.shopping.merchant.products.v1beta.Attributes` ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* Changed repeated flag of an existing field `gtin` in message `.google.shopping.merchant.products.v1beta.Attributes` ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* Fix typing issue with gRPC metadata when key ends in -bin ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))


### Documentation

* A comment for field `gtin` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `max_handling_time` in message `.google.shopping.merchant.products.v1beta.Shipping` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `max_transit_time` in message `.google.shopping.merchant.products.v1beta.Shipping` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `min_handling_time` in message `.google.shopping.merchant.products.v1beta.Shipping` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `min_transit_time` in message `.google.shopping.merchant.products.v1beta.Shipping` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `name` in message `.google.shopping.merchant.products.v1beta.DeleteProductInputRequest` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `name` in message `.google.shopping.merchant.products.v1beta.GetProductRequest` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `name` in message `.google.shopping.merchant.products.v1beta.Product` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `name` in message `.google.shopping.merchant.products.v1beta.ProductInput` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `page_size` in message `.google.shopping.merchant.products.v1beta.ListProductsRequest` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for field `tax_category` in message `.google.shopping.merchant.products.v1beta.Attributes` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for message `Product` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))
* A comment for message `ProductInput` is changed ([ce5c35a](https://github.com/googleapis/google-cloud-python/commit/ce5c35ad8b98f548a3dc8bd862646702b1d9974b))

## [0.1.4](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.1.3...google-shopping-merchant-products-v0.1.4) (2024-11-11)


### Bug Fixes

* disable universe-domain validation ([#13248](https://github.com/googleapis/google-cloud-python/issues/13248)) ([634f3e7](https://github.com/googleapis/google-cloud-python/commit/634f3e740926506654efa82a4f7a8d5f7e3cf6ba))

## [0.1.3](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.1.2...google-shopping-merchant-products-v0.1.3) (2024-10-24)


### Features

* Add support for Python 3.13 ([#13211](https://github.com/googleapis/google-cloud-python/issues/13211)) ([f712162](https://github.com/googleapis/google-cloud-python/commit/f712162c01f065da29fffbbed1e856a1f3876b1b))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.1.1...google-shopping-merchant-products-v0.1.2) (2024-07-30)


### Bug Fixes

* Retry and timeout values do not propagate in requests during pagination ([11c0629](https://github.com/googleapis/google-cloud-python/commit/11c06293cef3391f5fb433d5de26c066943082d0))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-shopping-merchant-products-v0.1.0...google-shopping-merchant-products-v0.1.1) (2024-07-08)


### Bug Fixes

* Allow protobuf 5.x ([eb36e8a](https://github.com/googleapis/google-cloud-python/commit/eb36e8a5e779717977132f605aa2ebc3cad78517))

## 0.1.0 (2024-06-05)


### Features

* add initial files for google.shopping.merchant.products.v1beta ([#12776](https://github.com/googleapis/google-cloud-python/issues/12776)) ([e1e7dbb](https://github.com/googleapis/google-cloud-python/commit/e1e7dbb1e65883436fdc520f96caabfcf9ab7b46))

## Changelog
