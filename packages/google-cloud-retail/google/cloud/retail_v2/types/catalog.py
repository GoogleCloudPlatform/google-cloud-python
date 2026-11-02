# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2.types import common, import_config

__protobuf__ = proto.module(
    package="google.cloud.retail.v2",
    manifest={
        "ProductLevelConfig",
        "CatalogAttribute",
        "AttributesConfig",
        "CompletionConfig",
        "Catalog",
    },
)


class ProductLevelConfig(proto.Message):
    r"""Configures what level the product should be uploaded with
    regards to how users will be send events and how predictions
    will be made.

    Attributes:
        ingestion_product_type (str):
            The type of [Product][google.cloud.retail.v2.Product]s
            allowed to be ingested into the catalog. Acceptable values
            are:

            - ``primary`` (default): You can ingest
              [Product][google.cloud.retail.v2.Product]s of all types.
              When ingesting a
              [Product][google.cloud.retail.v2.Product], its type will
              default to
              [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
              if unset.
            - ``variant`` (incompatible with Retail Search): You can
              only ingest
              [Product.Type.VARIANT][google.cloud.retail.v2.Product.Type.VARIANT]
              [Product][google.cloud.retail.v2.Product]s. This means
              [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id]
              cannot be empty.

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.

            If this field is ``variant`` and
            [merchant_center_product_id_field][google.cloud.retail.v2.ProductLevelConfig.merchant_center_product_id_field]
            is ``itemGroupId``, an INVALID_ARGUMENT error is returned.

            See `Product
            levels <https://cloud.google.com/retail/docs/catalog#product-levels>`__
            for more details.
        merchant_center_product_id_field (str):
            Which field of `Merchant Center
            Product </bigquery-transfer/docs/merchant-center-products-schema>`__
            should be imported as
            [Product.id][google.cloud.retail.v2.Product.id]. Acceptable
            values are:

            - ``offerId`` (default): Import ``offerId`` as the product
              ID.
            - ``itemGroupId``: Import ``itemGroupId`` as the product ID.
              Notice that Retail API will choose one item from the ones
              with the same ``itemGroupId``, and use it to represent the
              item group.

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.

            If this field is ``itemGroupId`` and
            [ingestion_product_type][google.cloud.retail.v2.ProductLevelConfig.ingestion_product_type]
            is ``variant``, an INVALID_ARGUMENT error is returned.

            See `Product
            levels <https://cloud.google.com/retail/docs/catalog#product-levels>`__
            for more details.
    """

    ingestion_product_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    merchant_center_product_id_field: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CatalogAttribute(proto.Message):
    r"""Catalog level attribute config for an attribute. For example,
    if customers want to enable/disable facet for a specific
    attribute.

    Attributes:
        key (str):
            Required. Attribute name. For example: ``color``,
            ``brands``, ``attributes.custom_attribute``, such as
            ``attributes.xyz``. To be indexable, the attribute name can
            contain only alpha-numeric characters and underscores. For
            example, an attribute named ``attributes.abc_xyz`` can be
            indexed, but an attribute named ``attributes.abc-xyz``
            cannot be indexed.

            If the attribute key starts with ``attributes.``, then the
            attribute is a custom attribute. Attributes such as
            ``brands``, ``patterns``, and ``title`` are built-in and
            called system attributes.
        in_use (bool):
            Output only. Indicates whether this attribute has been used
            by any products. ``True`` if at least one
            [Product][google.cloud.retail.v2.Product] is using this
            attribute in
            [Product.attributes][google.cloud.retail.v2.Product.attributes].
            Otherwise, this field is ``False``.

            [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute]
            can be pre-loaded by using
            [CatalogService.AddCatalogAttribute][google.cloud.retail.v2.CatalogService.AddCatalogAttribute]
            or
            [CatalogService.UpdateAttributesConfig][google.cloud.retail.v2.CatalogService.UpdateAttributesConfig]
            APIs. This field is ``False`` for pre-loaded
            [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute]s.

            Only pre-loaded [catalog
            attributes][google.cloud.retail.v2.CatalogAttribute] that
            are neither in use by products nor predefined can be
            deleted. [Catalog
            attributes][google.cloud.retail.v2.CatalogAttribute] that
            are either in use by products or are predefined attributes
            cannot be deleted; however, their configuration properties
            will reset to default values upon removal request.

            After catalog changes, it takes about 10 minutes for this
            field to update.
        type_ (google.cloud.retail_v2.types.CatalogAttribute.AttributeType):
            Output only. The type of this attribute. This is derived
            from the attribute in
            [Product.attributes][google.cloud.retail.v2.Product.attributes].
        indexable_option (google.cloud.retail_v2.types.CatalogAttribute.IndexableOption):
            When
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2.AttributesConfig.attribute_config_level]
            is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if INDEXABLE_ENABLED
            attribute values are indexed so that it can be filtered,
            faceted, or boosted in
            [SearchService.Search][google.cloud.retail.v2.SearchService.Search].

            Must be specified when
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2.AttributesConfig.attribute_config_level]
            is CATALOG_LEVEL_ATTRIBUTE_CONFIG, otherwise throws
            INVALID_FORMAT error.
        dynamic_facetable_option (google.cloud.retail_v2.types.CatalogAttribute.DynamicFacetableOption):
            If DYNAMIC_FACETABLE_ENABLED, attribute values are available
            for dynamic facet. Could only be DYNAMIC_FACETABLE_DISABLED
            if
            [CatalogAttribute.indexable_option][google.cloud.retail.v2.CatalogAttribute.indexable_option]
            is INDEXABLE_DISABLED. Otherwise, an INVALID_ARGUMENT error
            is returned.

            Must be specified, otherwise throws INVALID_FORMAT error.
        searchable_option (google.cloud.retail_v2.types.CatalogAttribute.SearchableOption):
            When
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2.AttributesConfig.attribute_config_level]
            is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if SEARCHABLE_ENABLED,
            attribute values are searchable by text queries in
            [SearchService.Search][google.cloud.retail.v2.SearchService.Search].

            If SEARCHABLE_ENABLED but attribute type is numerical,
            attribute values will not be searchable by text queries in
            [SearchService.Search][google.cloud.retail.v2.SearchService.Search],
            as there are no text values associated to numerical
            attributes.

            Must be specified, when
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2.AttributesConfig.attribute_config_level]
            is CATALOG_LEVEL_ATTRIBUTE_CONFIG, otherwise throws
            INVALID_FORMAT error.
        exact_searchable_option (google.cloud.retail_v2.types.CatalogAttribute.ExactSearchableOption):
            If EXACT_SEARCHABLE_ENABLED, attribute values will be exact
            searchable. This property only applies to textual custom
            attributes and requires indexable set to enabled to enable
            exact-searchable. If unset, the server behavior defaults to
            [EXACT_SEARCHABLE_DISABLED][google.cloud.retail.v2.CatalogAttribute.ExactSearchableOption.EXACT_SEARCHABLE_DISABLED].
        retrievable_option (google.cloud.retail_v2.types.CatalogAttribute.RetrievableOption):
            If RETRIEVABLE_ENABLED, attribute values are retrievable in
            the search results. If unset, the server behavior defaults
            to
            [RETRIEVABLE_DISABLED][google.cloud.retail.v2.CatalogAttribute.RetrievableOption.RETRIEVABLE_DISABLED].
        facet_config (google.cloud.retail_v2.types.CatalogAttribute.FacetConfig):
            Contains facet options.
    """

    class AttributeType(proto.Enum):
        r"""The type of an attribute.

        Values:
            UNKNOWN (0):
                The type of the attribute is unknown.

                Used when type cannot be derived from attribute that is not
                [in_use][google.cloud.retail.v2.CatalogAttribute.in_use].
            TEXTUAL (1):
                Textual attribute.
            NUMERICAL (2):
                Numerical attribute.
        """

        UNKNOWN = 0
        TEXTUAL = 1
        NUMERICAL = 2

    class IndexableOption(proto.Enum):
        r"""The status of the indexable option of a catalog attribute.

        Values:
            INDEXABLE_OPTION_UNSPECIFIED (0):
                Value used when unset.
            INDEXABLE_ENABLED (1):
                Indexable option enabled for an attribute.
            INDEXABLE_DISABLED (2):
                Indexable option disabled for an attribute.
        """

        INDEXABLE_OPTION_UNSPECIFIED = 0
        INDEXABLE_ENABLED = 1
        INDEXABLE_DISABLED = 2

    class DynamicFacetableOption(proto.Enum):
        r"""The status of the dynamic facetable option of a catalog
        attribute.

        Values:
            DYNAMIC_FACETABLE_OPTION_UNSPECIFIED (0):
                Value used when unset.
            DYNAMIC_FACETABLE_ENABLED (1):
                Dynamic facetable option enabled for an
                attribute.
            DYNAMIC_FACETABLE_DISABLED (2):
                Dynamic facetable option disabled for an
                attribute.
        """

        DYNAMIC_FACETABLE_OPTION_UNSPECIFIED = 0
        DYNAMIC_FACETABLE_ENABLED = 1
        DYNAMIC_FACETABLE_DISABLED = 2

    class SearchableOption(proto.Enum):
        r"""The status of the searchable option of a catalog attribute.

        Values:
            SEARCHABLE_OPTION_UNSPECIFIED (0):
                Value used when unset.
            SEARCHABLE_ENABLED (1):
                Searchable option enabled for an attribute.
            SEARCHABLE_DISABLED (2):
                Searchable option disabled for an attribute.
        """

        SEARCHABLE_OPTION_UNSPECIFIED = 0
        SEARCHABLE_ENABLED = 1
        SEARCHABLE_DISABLED = 2

    class ExactSearchableOption(proto.Enum):
        r"""The status of the exact-searchable option of a catalog
        attribute.

        Values:
            EXACT_SEARCHABLE_OPTION_UNSPECIFIED (0):
                Value used when unset.
            EXACT_SEARCHABLE_ENABLED (1):
                Exact searchable option enabled for an
                attribute.
            EXACT_SEARCHABLE_DISABLED (2):
                Exact searchable option disabled for an
                attribute.
        """

        EXACT_SEARCHABLE_OPTION_UNSPECIFIED = 0
        EXACT_SEARCHABLE_ENABLED = 1
        EXACT_SEARCHABLE_DISABLED = 2

    class RetrievableOption(proto.Enum):
        r"""The status of the retrievable option of a catalog attribute.

        Values:
            RETRIEVABLE_OPTION_UNSPECIFIED (0):
                Value used when unset.
            RETRIEVABLE_ENABLED (1):
                Retrievable option enabled for an attribute.
            RETRIEVABLE_DISABLED (2):
                Retrievable option disabled for an attribute.
        """

        RETRIEVABLE_OPTION_UNSPECIFIED = 0
        RETRIEVABLE_ENABLED = 1
        RETRIEVABLE_DISABLED = 2

    class FacetConfig(proto.Message):
        r"""Possible options for the facet that corresponds to the
        current attribute config.

        Attributes:
            facet_intervals (MutableSequence[google.cloud.retail_v2.types.Interval]):
                If you don't set the facet
                [SearchRequest.FacetSpec.FacetKey.intervals][google.cloud.retail.v2.SearchRequest.FacetSpec.FacetKey.intervals]
                in the request to a numerical attribute, then we use the
                computed intervals with rounded bounds obtained from all its
                product numerical attribute values. The computed intervals
                might not be ideal for some attributes. Therefore, we give
                you the option to overwrite them with the facet_intervals
                field. The maximum of facet intervals per
                [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute]
                is 40. Each interval must have a lower bound or an upper
                bound. If both bounds are provided, then the lower bound
                must be smaller or equal than the upper bound.
            ignored_facet_values (MutableSequence[google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.IgnoredFacetValues]):
                Each instance represents a list of attribute values to
                ignore as facet values for a specific time range. The
                maximum number of instances per
                [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute]
                is 25.
            merged_facet_values (MutableSequence[google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.MergedFacetValue]):
                Each instance replaces a list of facet values by a merged
                facet value. If a facet value is not in any list, then it
                will stay the same. To avoid conflicts, only paths of length
                1 are accepted. In other words, if "dark_blue" merged into
                "BLUE", then the latter can't merge into "blues" because
                this would create a path of length 2. The maximum number of
                instances of MergedFacetValue per
                [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute]
                is 100. This feature is available only for textual custom
                attributes.
            merged_facet (google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.MergedFacet):
                Use this field only if you want to merge a
                facet key into another facet key.
            rerank_config (google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.RerankConfig):
                Set this field only if you want to rerank
                based on facet values engaged by the user for
                the current key. This option is only possible
                for custom facetable textual keys.
        """

        class IgnoredFacetValues(proto.Message):
            r"""[Facet values][google.cloud.retail.v2.SearchResponse.Facet.values]
            to ignore on [facets][google.cloud.retail.v2.SearchResponse.Facet]
            during the specified time range for the given
            [SearchResponse.Facet.key][google.cloud.retail.v2.SearchResponse.Facet.key]
            attribute.

            Attributes:
                values (MutableSequence[str]):
                    List of facet values to ignore for the
                    following time range. The facet values are the
                    same as the attribute values. There is a limit
                    of 10 values per instance of IgnoredFacetValues.
                    Each value can have at most 128 characters.
                start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Time range for the current list of facet
                    values to ignore. If multiple time ranges are
                    specified for an facet value for the current
                    attribute, consider all of them. If both are
                    empty, ignore always. If start time and end time
                    are set, then start time must be before end
                    time.
                    If start time is not empty and end time is
                    empty, then will ignore these facet values after
                    the start time.
                end_time (google.protobuf.timestamp_pb2.Timestamp):
                    If start time is empty and end time is not
                    empty, then ignore these facet values before end
                    time.
            """

            values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                message=timestamp_pb2.Timestamp,
            )
            end_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=3,
                message=timestamp_pb2.Timestamp,
            )

        class MergedFacetValue(proto.Message):
            r"""Replaces a set of textual facet values by the same (possibly
            different) merged facet value. Each facet value should appear at
            most once as a value per
            [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute]. This
            feature is available only for textual custom attributes.

            Attributes:
                values (MutableSequence[str]):
                    All the facet values that are replaces by the same
                    [merged_value][google.cloud.retail.v2.CatalogAttribute.FacetConfig.MergedFacetValue.merged_value]
                    that follows. The maximum number of values per
                    MergedFacetValue is 25. Each value can have up to 128
                    characters.
                merged_value (str):
                    All the previous values are replaced by this merged facet
                    value. This merged_value must be non-empty and can have up
                    to 128 characters.
            """

            values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            merged_value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class MergedFacet(proto.Message):
            r"""The current facet key (i.e. attribute config) maps into the
            [merged_facet_key][google.cloud.retail.v2.CatalogAttribute.FacetConfig.MergedFacet.merged_facet_key].
            A facet key can have at most one child. The current facet key and
            the merged facet key need both to be textual custom attributes or
            both numerical custom attributes (same type).

            Attributes:
                merged_facet_key (str):
                    The merged facet key should be a valid facet
                    key that is different than the facet key of the
                    current catalog attribute. We refer this is
                    merged facet key as the child of the current
                    catalog attribute. This merged facet key can't
                    be a parent of another facet key (i.e. no
                    directed path of length 2). This merged facet
                    key needs to be either a textual custom
                    attribute or a numerical custom attribute.
            """

            merged_facet_key: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class RerankConfig(proto.Message):
            r"""Options to rerank based on facet values engaged by the user for the
            current key. That key needs to be a custom textual key and
            facetable. To use this control, you also need to pass all the facet
            keys engaged by the user in the request using the field
            [SearchRequest.FacetSpec]. In particular, if you don't pass the
            facet keys engaged that you want to rerank on, this control won't be
            effective. Moreover, to obtain better results, the facet values that
            you want to rerank on should be close to English (ideally made of
            words, underscores, and spaces).

            Attributes:
                rerank_facet (bool):
                    If set to true, then we also rerank the
                    dynamic facets based on the facet values engaged
                    by the user for the current attribute key during
                    serving.
                facet_values (MutableSequence[str]):
                    If empty, rerank on all facet values for the
                    current key. Otherwise, will rerank on the facet
                    values from this list only.
            """

            rerank_facet: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            facet_values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        facet_intervals: MutableSequence[common.Interval] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=common.Interval,
        )
        ignored_facet_values: MutableSequence[
            "CatalogAttribute.FacetConfig.IgnoredFacetValues"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CatalogAttribute.FacetConfig.IgnoredFacetValues",
        )
        merged_facet_values: MutableSequence[
            "CatalogAttribute.FacetConfig.MergedFacetValue"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="CatalogAttribute.FacetConfig.MergedFacetValue",
        )
        merged_facet: "CatalogAttribute.FacetConfig.MergedFacet" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="CatalogAttribute.FacetConfig.MergedFacet",
        )
        rerank_config: "CatalogAttribute.FacetConfig.RerankConfig" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="CatalogAttribute.FacetConfig.RerankConfig",
        )

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    in_use: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    type_: AttributeType = proto.Field(
        proto.ENUM,
        number=10,
        enum=AttributeType,
    )
    indexable_option: IndexableOption = proto.Field(
        proto.ENUM,
        number=5,
        enum=IndexableOption,
    )
    dynamic_facetable_option: DynamicFacetableOption = proto.Field(
        proto.ENUM,
        number=6,
        enum=DynamicFacetableOption,
    )
    searchable_option: SearchableOption = proto.Field(
        proto.ENUM,
        number=7,
        enum=SearchableOption,
    )
    exact_searchable_option: ExactSearchableOption = proto.Field(
        proto.ENUM,
        number=11,
        enum=ExactSearchableOption,
    )
    retrievable_option: RetrievableOption = proto.Field(
        proto.ENUM,
        number=12,
        enum=RetrievableOption,
    )
    facet_config: FacetConfig = proto.Field(
        proto.MESSAGE,
        number=13,
        message=FacetConfig,
    )


class AttributesConfig(proto.Message):
    r"""Catalog level attribute config.

    Attributes:
        name (str):
            Required. Immutable. The fully qualified resource name of
            the attribute config. Format:
            ``projects/*/locations/*/catalogs/*/attributesConfig``
        catalog_attributes (MutableMapping[str, google.cloud.retail_v2.types.CatalogAttribute]):
            Enable attribute(s) config at catalog level. For example,
            indexable, dynamic_facetable, or searchable for each
            attribute.

            The key is catalog attribute's name. For example: ``color``,
            ``brands``, ``attributes.custom_attribute``, such as
            ``attributes.xyz``.

            The maximum number of catalog attributes allowed in a
            request is 1000.
        attribute_config_level (google.cloud.retail_v2.types.AttributeConfigLevel):
            Output only. The
            [AttributeConfigLevel][google.cloud.retail.v2.AttributeConfigLevel]
            used for this catalog.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    catalog_attributes: MutableMapping[str, "CatalogAttribute"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="CatalogAttribute",
    )
    attribute_config_level: common.AttributeConfigLevel = proto.Field(
        proto.ENUM,
        number=3,
        enum=common.AttributeConfigLevel,
    )


class CompletionConfig(proto.Message):
    r"""Catalog level autocomplete config for customers to customize
    autocomplete feature's settings.

    Attributes:
        name (str):
            Required. Immutable. Fully qualified name
            ``projects/*/locations/*/catalogs/*/completionConfig``
        matching_order (str):
            Specifies the matching order for autocomplete suggestions,
            e.g., a query consisting of 'sh' with 'out-of-order'
            specified would suggest "women's shoes", whereas a query of
            'red s' with 'exact-prefix' specified would suggest "red
            shoes". Currently supported values:

            - 'out-of-order'
            - 'exact-prefix'

            Default value: 'exact-prefix'.
        max_suggestions (int):
            The maximum number of autocomplete
            suggestions returned per term. Default value is
            20. If left unset or set to 0, then will
            fallback to default value.

            Value range is 1 to 20.
        min_prefix_length (int):
            The minimum number of characters needed to be
            typed in order to get suggestions. Default value
            is 2. If left unset or set to 0, then will
            fallback to default value.

            Value range is 1 to 20.
        auto_learning (bool):
            If set to true, the auto learning function is enabled. Auto
            learning uses user data to generate suggestions using ML
            techniques. Default value is false. Only after enabling auto
            learning can users use ``cloud-retail`` data in
            [CompleteQueryRequest][google.cloud.retail.v2.CompleteQueryRequest].
        suggestions_input_config (google.cloud.retail_v2.types.CompletionDataInputConfig):
            Output only. The source data for the latest
            import of the autocomplete suggestion phrases.
        last_suggestions_import_operation (str):
            Output only. Name of the LRO corresponding to the latest
            suggestion terms list import.

            Can use
            [GetOperation][google.longrunning.Operations.GetOperation]
            API method to retrieve the latest state of the Long Running
            Operation.
        denylist_input_config (google.cloud.retail_v2.types.CompletionDataInputConfig):
            Output only. The source data for the latest
            import of the autocomplete denylist phrases.
        last_denylist_import_operation (str):
            Output only. Name of the LRO corresponding to the latest
            denylist import.

            Can use
            [GetOperation][google.longrunning.Operations.GetOperation]
            API to retrieve the latest state of the Long Running
            Operation.
        allowlist_input_config (google.cloud.retail_v2.types.CompletionDataInputConfig):
            Output only. The source data for the latest
            import of the autocomplete allowlist phrases.
        last_allowlist_import_operation (str):
            Output only. Name of the LRO corresponding to the latest
            allowlist import.

            Can use
            [GetOperation][google.longrunning.Operations.GetOperation]
            API to retrieve the latest state of the Long Running
            Operation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    matching_order: str = proto.Field(
        proto.STRING,
        number=2,
    )
    max_suggestions: int = proto.Field(
        proto.INT32,
        number=3,
    )
    min_prefix_length: int = proto.Field(
        proto.INT32,
        number=4,
    )
    auto_learning: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    suggestions_input_config: import_config.CompletionDataInputConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=import_config.CompletionDataInputConfig,
    )
    last_suggestions_import_operation: str = proto.Field(
        proto.STRING,
        number=6,
    )
    denylist_input_config: import_config.CompletionDataInputConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=import_config.CompletionDataInputConfig,
    )
    last_denylist_import_operation: str = proto.Field(
        proto.STRING,
        number=8,
    )
    allowlist_input_config: import_config.CompletionDataInputConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=import_config.CompletionDataInputConfig,
    )
    last_allowlist_import_operation: str = proto.Field(
        proto.STRING,
        number=10,
    )


class Catalog(proto.Message):
    r"""The catalog configuration.

    Attributes:
        name (str):
            Required. Immutable. The fully qualified
            resource name of the catalog.
        display_name (str):
            Required. Immutable. The catalog display name.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.
        product_level_config (google.cloud.retail_v2.types.ProductLevelConfig):
            Required. The product level configuration.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product_level_config: "ProductLevelConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ProductLevelConfig",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
