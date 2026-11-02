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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.visionai_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "FacetBucketType",
        "CreateAssetRequest",
        "GetAssetRequest",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "UpdateAssetRequest",
        "DeleteAssetRequest",
        "AssetSource",
        "UploadAssetRequest",
        "UploadAssetResponse",
        "UploadAssetMetadata",
        "GenerateRetrievalUrlRequest",
        "GenerateRetrievalUrlResponse",
        "Asset",
        "AnalyzeAssetRequest",
        "AnalyzeAssetMetadata",
        "AnalyzeAssetResponse",
        "IndexingStatus",
        "IndexAssetRequest",
        "IndexAssetMetadata",
        "IndexAssetResponse",
        "RemoveIndexAssetRequest",
        "RemoveIndexAssetMetadata",
        "RemoveIndexAssetResponse",
        "IndexedAsset",
        "ViewIndexedAssetsRequest",
        "ViewIndexedAssetsResponse",
        "CreateCorpusRequest",
        "CreateCorpusMetadata",
        "SearchCapability",
        "SearchCapabilitySetting",
        "CreateCollectionMetadata",
        "CreateCollectionRequest",
        "DeleteCollectionMetadata",
        "DeleteCollectionRequest",
        "GetCollectionRequest",
        "UpdateCollectionRequest",
        "ListCollectionsRequest",
        "ListCollectionsResponse",
        "AddCollectionItemRequest",
        "AddCollectionItemResponse",
        "RemoveCollectionItemRequest",
        "RemoveCollectionItemResponse",
        "ViewCollectionItemsRequest",
        "ViewCollectionItemsResponse",
        "Collection",
        "CollectionItem",
        "CreateIndexRequest",
        "CreateIndexMetadata",
        "UpdateIndexRequest",
        "UpdateIndexMetadata",
        "GetIndexRequest",
        "ListIndexesRequest",
        "ListIndexesResponse",
        "DeleteIndexRequest",
        "DeleteIndexMetadata",
        "Index",
        "DeployedIndexReference",
        "Corpus",
        "GetCorpusRequest",
        "UpdateCorpusRequest",
        "ListCorporaRequest",
        "ListCorporaResponse",
        "DeleteCorpusRequest",
        "AnalyzeCorpusRequest",
        "AnalyzeCorpusMetadata",
        "AnalyzeCorpusResponse",
        "CreateDataSchemaRequest",
        "DataSchema",
        "DataSchemaDetails",
        "UpdateDataSchemaRequest",
        "GetDataSchemaRequest",
        "DeleteDataSchemaRequest",
        "ListDataSchemasRequest",
        "ListDataSchemasResponse",
        "CreateAnnotationRequest",
        "Annotation",
        "UserSpecifiedAnnotation",
        "GeoCoordinate",
        "AnnotationValue",
        "AnnotationList",
        "AnnotationCustomizedStruct",
        "ListAnnotationsRequest",
        "ListAnnotationsResponse",
        "GetAnnotationRequest",
        "UpdateAnnotationRequest",
        "DeleteAnnotationRequest",
        "ImportAssetsRequest",
        "ImportAssetsMetadata",
        "BatchOperationStatus",
        "ImportAssetsResponse",
        "CreateSearchConfigRequest",
        "UpdateSearchConfigRequest",
        "GetSearchConfigRequest",
        "DeleteSearchConfigRequest",
        "ListSearchConfigsRequest",
        "ListSearchConfigsResponse",
        "SearchConfig",
        "IndexEndpoint",
        "CreateIndexEndpointRequest",
        "CreateIndexEndpointMetadata",
        "GetIndexEndpointRequest",
        "ListIndexEndpointsRequest",
        "ListIndexEndpointsResponse",
        "UpdateIndexEndpointRequest",
        "UpdateIndexEndpointMetadata",
        "DeleteIndexEndpointRequest",
        "DeleteIndexEndpointMetadata",
        "DeployIndexRequest",
        "DeployIndexResponse",
        "DeployIndexMetadata",
        "UndeployIndexMetadata",
        "UndeployIndexRequest",
        "UndeployIndexResponse",
        "DeployedIndex",
        "FacetProperty",
        "SearchHypernym",
        "CreateSearchHypernymRequest",
        "UpdateSearchHypernymRequest",
        "GetSearchHypernymRequest",
        "DeleteSearchHypernymRequest",
        "ListSearchHypernymsRequest",
        "ListSearchHypernymsResponse",
        "SearchCriteriaProperty",
        "FacetValue",
        "FacetBucket",
        "FacetGroup",
        "IngestAssetRequest",
        "IngestAssetResponse",
        "ClipAssetRequest",
        "ClipAssetResponse",
        "GenerateHlsUriRequest",
        "GenerateHlsUriResponse",
        "SearchAssetsRequest",
        "SearchIndexEndpointRequest",
        "ImageQuery",
        "SchemaKeySortingStrategy",
        "DeleteAssetMetadata",
        "AnnotationMatchingResult",
        "SearchResultItem",
        "SearchAssetsResponse",
        "SearchIndexEndpointResponse",
        "IntRange",
        "FloatRange",
        "StringArray",
        "IntRangeArray",
        "FloatRangeArray",
        "DateTimeRange",
        "DateTimeRangeArray",
        "CircleArea",
        "GeoLocationArray",
        "BoolValue",
        "Criteria",
        "Partition",
    },
)


class FacetBucketType(proto.Enum):
    r"""Different types for a facet bucket.

    Values:
        FACET_BUCKET_TYPE_UNSPECIFIED (0):
            Unspecified type.
        FACET_BUCKET_TYPE_VALUE (1):
            Value type.
        FACET_BUCKET_TYPE_DATETIME (2):
            Datetime type.
        FACET_BUCKET_TYPE_FIXED_RANGE (3):
            Fixed Range type.
        FACET_BUCKET_TYPE_CUSTOM_RANGE (4):
            Custom Range type.
    """

    FACET_BUCKET_TYPE_UNSPECIFIED = 0
    FACET_BUCKET_TYPE_VALUE = 1
    FACET_BUCKET_TYPE_DATETIME = 2
    FACET_BUCKET_TYPE_FIXED_RANGE = 3
    FACET_BUCKET_TYPE_CUSTOM_RANGE = 4


class CreateAssetRequest(proto.Message):
    r"""Request message for CreateAssetRequest.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent resource where this asset will be
            created. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
        asset (google.cloud.visionai_v1.types.Asset):
            Required. The asset to create.
        asset_id (str):
            Optional. The ID to use for the asset, which will become the
            final component of the asset's resource name if user choose
            to specify. Otherwise, asset id will be generated by system.

            This value should be up to 63 characters, and valid
            characters are /[a-z][0-9]-/. The first character must be a
            letter, the last could be a letter or a number.

            This field is a member of `oneof`_ ``_asset_id``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Asset",
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class GetAssetRequest(proto.Message):
    r"""Request message for GetAsset.

    Attributes:
        name (str):
            Required. The name of the asset to retrieve. Format:
            projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAssetsRequest(proto.Message):
    r"""Request message for ListAssets.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of assets.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        page_size (int):
            The maximum number of assets to return. The
            service may return fewer than this value.
            If unspecified, at most 50 assets will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListAssets`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAssets`` must match the call that provided the page
            token.
        filter (str):
            The filter applied to the returned list. Only the following
            filterings are supported: "assets_with_contents = true",
            which returns assets with contents uploaded;
            "assets_with_contents = false", which returns assets without
            contents.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListAssetsResponse(proto.Message):
    r"""Response message for ListAssets.

    Attributes:
        assets (MutableSequence[google.cloud.visionai_v1.types.Asset]):
            The assets from the specified corpus.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    assets: MutableSequence["Asset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Asset",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateAssetRequest(proto.Message):
    r"""Request message for UpdateAsset.

    Attributes:
        asset (google.cloud.visionai_v1.types.Asset):
            Required. The asset to update.

            The asset's ``name`` field is used to identify the asset to
            be updated. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Asset",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAssetRequest(proto.Message):
    r"""Request message for DeleteAsset.

    Attributes:
        name (str):
            Required. The name of the asset to delete. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AssetSource(proto.Message):
    r"""The source of the asset.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        asset_gcs_source (google.cloud.visionai_v1.types.AssetSource.AssetGcsSource):
            The source of the asset is from Cloud
            Storage.

            This field is a member of `oneof`_ ``source_form``.
        asset_content_data (google.cloud.visionai_v1.types.AssetSource.AssetContentData):
            The source of the asset is from content
            bytes.

            This field is a member of `oneof`_ ``source_form``.
    """

    class AssetGcsSource(proto.Message):
        r"""The asset source is from Cloud Storage.

        Attributes:
            gcs_uri (str):
                Cloud storage uri.
        """

        gcs_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class AssetContentData(proto.Message):
        r"""The content of the asset.

        Attributes:
            asset_content_data (bytes):

        """

        asset_content_data: bytes = proto.Field(
            proto.BYTES,
            number=1,
        )

    asset_gcs_source: AssetGcsSource = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source_form",
        message=AssetGcsSource,
    )
    asset_content_data: AssetContentData = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source_form",
        message=AssetContentData,
    )


class UploadAssetRequest(proto.Message):
    r"""Request message for UploadAsset.

    Attributes:
        name (str):
            Required. The resource name of the asset to upload. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        asset_source (google.cloud.visionai_v1.types.AssetSource):
            The source of the asset.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_source: "AssetSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AssetSource",
    )


class UploadAssetResponse(proto.Message):
    r"""Response message for UploadAsset."""


class UploadAssetMetadata(proto.Message):
    r"""Metadata for UploadAsset.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The update time of the operation.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class GenerateRetrievalUrlRequest(proto.Message):
    r"""Request message for GenerateRetrievalUrl API.

    Attributes:
        name (str):
            Required. The resource name of the asset to request signed
            url for. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateRetrievalUrlResponse(proto.Message):
    r"""Response message for GenerateRetrievalUrl API.

    Attributes:
        signed_uri (str):
            A signed url to download the content of the
            asset.
    """

    signed_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Asset(proto.Message):
    r"""An asset is a resource in corpus. It represents a media
    object inside corpus, contains metadata and another resource
    annotation. Different feature could be applied to the asset to
    generate annotations. User could specified annotation related to
    the target asset.

    Attributes:
        name (str):
            Resource name of the asset. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        ttl (google.protobuf.duration_pb2.Duration):
            The duration for which all media assets,
            associated metadata, and search documents can
            exist. If not set, then it will using the
            default ttl in the parent corpus resource.
        asset_gcs_source (google.cloud.visionai_v1.types.AssetSource.AssetGcsSource):
            Output only. The original cloud storage
            source uri that is associated with this asset.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    asset_gcs_source: "AssetSource.AssetGcsSource" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AssetSource.AssetGcsSource",
    )


class AnalyzeAssetRequest(proto.Message):
    r"""Request message for AnalyzeAsset.

    Attributes:
        name (str):
            Required. The resource name of the asset to analyze. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AnalyzeAssetMetadata(proto.Message):
    r"""Metadata for AnalyzeAsset.

    Attributes:
        analysis_status (MutableSequence[google.cloud.visionai_v1.types.AnalyzeAssetMetadata.AnalysisStatus]):
            The status of analysis on all search
            capabilities.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The update time of the operation.
    """

    class AnalysisStatus(proto.Message):
        r"""The status of analysis on each search capability.

        Attributes:
            state (google.cloud.visionai_v1.types.AnalyzeAssetMetadata.AnalysisStatus.State):

            status_message (str):

            search_capability (google.cloud.visionai_v1.types.SearchCapability):
                The search capability requested.
        """

        class State(proto.Enum):
            r"""The state of the search capability.

            Values:
                STATE_UNSPECIFIED (0):
                    The default process state should never
                    happen.
                IN_PROGRESS (1):
                    The ml model analysis is in progress.
                SUCCEEDED (2):
                    The ml model analysis is successfully done.
                FAILED (3):
                    The ml model analysis failed.
            """

            STATE_UNSPECIFIED = 0
            IN_PROGRESS = 1
            SUCCEEDED = 2
            FAILED = 3

        state: "AnalyzeAssetMetadata.AnalysisStatus.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="AnalyzeAssetMetadata.AnalysisStatus.State",
        )
        status_message: str = proto.Field(
            proto.STRING,
            number=3,
        )
        search_capability: "SearchCapability" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="SearchCapability",
        )

    analysis_status: MutableSequence[AnalysisStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=AnalysisStatus,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class AnalyzeAssetResponse(proto.Message):
    r"""Response message for AnalyzeAsset."""


class IndexingStatus(proto.Message):
    r"""The status of indexing for the asset.

    Attributes:
        state (google.cloud.visionai_v1.types.IndexingStatus.State):
            Output only. State of this asset's indexing.
        status_message (str):
            Detailed message describing the state.
    """

    class State(proto.Enum):
        r"""State enum for this asset's indexing.

        Values:
            STATE_UNSPECIFIED (0):
                The default process state should never
                happen.
            IN_PROGRESS (1):
                The indexing is in progress.
            SUCCEEDED (2):
                The process is successfully done.
            FAILED (3):
                The process failed.
        """

        STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        SUCCEEDED = 2
        FAILED = 3

    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class IndexAssetRequest(proto.Message):
    r"""Request message for IndexAsset.

    Attributes:
        name (str):
            Required. The resource name of the asset to index. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        index (str):
            Optional. The name of the index. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    index: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IndexAssetMetadata(proto.Message):
    r"""Metadata for IndexAsset.

    Attributes:
        status (google.cloud.visionai_v1.types.IndexingStatus):
            The status of indexing this asset.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The update time of the operation.
    """

    status: "IndexingStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="IndexingStatus",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class IndexAssetResponse(proto.Message):
    r"""Response message for IndexAsset."""


class RemoveIndexAssetRequest(proto.Message):
    r"""Request message for RemoveIndexAsset.

    Attributes:
        name (str):
            Required. The resource name of the asset to index. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        index (str):
            Optional. The name of the index. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    index: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemoveIndexAssetMetadata(proto.Message):
    r"""Metadata for RemoveIndexAsset.

    Attributes:
        indexing_status (google.cloud.visionai_v1.types.IndexingStatus):
            The status of indexing this asset.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The update time of the operation.
    """

    indexing_status: "IndexingStatus" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IndexingStatus",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class RemoveIndexAssetResponse(proto.Message):
    r"""Response message for RemoveIndexAsset."""


class IndexedAsset(proto.Message):
    r"""An IndexedAsset is an asset that the index is built upon.

    Attributes:
        index (str):
            Required. The index that this indexed asset belongs to.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}``
        asset (str):
            Required. The resource name of the asset. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
    """

    index: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ViewIndexedAssetsRequest(proto.Message):
    r"""Request message for ViewIndexedAssets.

    Attributes:
        index (str):
            Required. The index that owns this collection of assets.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}``
        page_size (int):
            The maximum number of assets to return. The
            service may return fewer than this value.
            If unspecified, at most 50 assets will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ViewIndexedAssets``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ViewIndexedAssets`` must match the call that provided the
            page token.
        filter (str):
            The filter applied to the returned list. Only the following
            filterings are supported: "asset_id = xxxx", which returns
            asset with specified id. "asset_id = xxxx, yyyy, zzzz",
            which returns assets with specified ids.
    """

    index: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ViewIndexedAssetsResponse(proto.Message):
    r"""Response message for ViewIndexedAssets.

    Attributes:
        indexed_assets (MutableSequence[google.cloud.visionai_v1.types.IndexedAsset]):
            The assets from the specified index.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    indexed_assets: MutableSequence["IndexedAsset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IndexedAsset",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateCorpusRequest(proto.Message):
    r"""Request message of CreateCorpus API.

    Attributes:
        parent (str):
            Required. Form:
            ``projects/{project_number}/locations/{location_id}``
        corpus (google.cloud.visionai_v1.types.Corpus):
            Required. The corpus to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    corpus: "Corpus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Corpus",
    )


class CreateCorpusMetadata(proto.Message):
    r"""Metadata for CreateCorpus API.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The create time of the create corpus
            operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The update time of the create corpus
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class SearchCapability(proto.Message):
    r"""The capability and metadata of search capability.

    Attributes:
        type_ (google.cloud.visionai_v1.types.SearchCapability.Type):
            The search capability to enable.
    """

    class Type(proto.Enum):
        r"""Capability to perform different search on assets.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified search capability, should never
                be used.
            EMBEDDING_SEARCH (1):
                Embedding search.
        """

        TYPE_UNSPECIFIED = 0
        EMBEDDING_SEARCH = 1

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )


class SearchCapabilitySetting(proto.Message):
    r"""Setting for search capability to enable.

    Attributes:
        search_capabilities (MutableSequence[google.cloud.visionai_v1.types.SearchCapability]):
            The metadata of search capability to enable.
    """

    search_capabilities: MutableSequence["SearchCapability"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchCapability",
    )


class CreateCollectionMetadata(proto.Message):
    r"""Metadata message for CreateCollectionRequest

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class CreateCollectionRequest(proto.Message):
    r"""Request message for CreateCollection.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent resource where this collection will be
            created. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        collection (google.cloud.visionai_v1.types.Collection):
            Required. The collection resource to be
            created.
        collection_id (str):
            Optional. The ID to use for the collection, which will
            become the final component of the resource name if user
            choose to specify. Otherwise, collection id will be
            generated by system.

            This value should be up to 55 characters, and valid
            characters are /[a-z][0-9]-/. The first character must be a
            letter, the last could be a letter or a number.

            This field is a member of `oneof`_ ``_collection_id``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    collection: "Collection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Collection",
    )
    collection_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class DeleteCollectionMetadata(proto.Message):
    r"""Metadata message for DeleteCollectionRequest

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class DeleteCollectionRequest(proto.Message):
    r"""Request message for DeleteCollectionRequest.

    Attributes:
        name (str):
            Required. The name of the collection to delete. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCollectionRequest(proto.Message):
    r"""Request message for GetCollectionRequest.

    Attributes:
        name (str):
            Required. The name of the collection to retrieve. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCollectionRequest(proto.Message):
    r"""Request message for UpdateCollectionRequest.

    Attributes:
        collection (google.cloud.visionai_v1.types.Collection):
            Required. The collection to update.

            The collection's ``name`` field is used to identify the
            collection to be updated. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.

            - Unset ``update_mask`` or set ``update_mask`` to be a
              single "\*" only will update all updatable fields with the
              value provided in ``collection``.
            - To update ``display_name`` value to empty string, set it
              in the ``collection`` to empty string, and set
              ``update_mask`` with "display_name". Same applies to other
              updatable string fields in the ``collection``.
    """

    collection: "Collection" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Collection",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListCollectionsRequest(proto.Message):
    r"""Request message for ListCollections.

    Attributes:
        parent (str):
            Required. The parent corpus. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        page_size (int):
            The maximum number of collections to return.
            The service may return fewer than this value. If
            unspecified, at most 50 collections will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListCollectionsRequest`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListCollectionsRequest`` must match the call that provided
            the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCollectionsResponse(proto.Message):
    r"""Response message for ListCollections.

    Attributes:
        collections (MutableSequence[google.cloud.visionai_v1.types.Collection]):
            The collections from the specified corpus.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    collections: MutableSequence["Collection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Collection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AddCollectionItemRequest(proto.Message):
    r"""Request message for AddCollectionItem.

    Attributes:
        item (google.cloud.visionai_v1.types.CollectionItem):
            Required. The item to be added.
    """

    item: "CollectionItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CollectionItem",
    )


class AddCollectionItemResponse(proto.Message):
    r"""Response message for AddCollectionItem.

    Attributes:
        item (google.cloud.visionai_v1.types.CollectionItem):
            The item that has already been added.
    """

    item: "CollectionItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CollectionItem",
    )


class RemoveCollectionItemRequest(proto.Message):
    r"""Request message for RemoveCollectionItem.

    Attributes:
        item (google.cloud.visionai_v1.types.CollectionItem):
            Required. The item to be removed.
    """

    item: "CollectionItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CollectionItem",
    )


class RemoveCollectionItemResponse(proto.Message):
    r"""Request message for RemoveCollectionItem.

    Attributes:
        item (google.cloud.visionai_v1.types.CollectionItem):
            The item that has already been removed.
    """

    item: "CollectionItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CollectionItem",
    )


class ViewCollectionItemsRequest(proto.Message):
    r"""Request message for ViewCollectionItems.

    Attributes:
        collection (str):
            Required. The collection to view. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}``
        page_size (int):
            The maximum number of collections to return.
            The service may return fewer than this value. If
            unspecified, at most 50 collections will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ViewCollectionItemsRequest`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ViewCollectionItemsRequest`` must match the call that
            provided the page token.
    """

    collection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ViewCollectionItemsResponse(proto.Message):
    r"""Response message for ViewCollectionItems.

    Attributes:
        items (MutableSequence[google.cloud.visionai_v1.types.CollectionItem]):
            The items from the specified collection.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    items: MutableSequence["CollectionItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CollectionItem",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Collection(proto.Message):
    r"""A collection is a resource in a corpus. It serves as a
    container of references to original resources.

    Attributes:
        name (str):
            Output only. Resource name of the collection. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}``
        display_name (str):
            Optional. The collection name for displaying.
            The name can be up to 256 characters long.
        description (str):
            Optional. Description of the collection. Can
            be up to 25000 characters long.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CollectionItem(proto.Message):
    r"""A CollectionItem is an item in a collection.
    Each item is a reference to the original resource in a
    collection.

    Attributes:
        collection (str):
            Required. The collection name that this item belongs to.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}``
        type_ (google.cloud.visionai_v1.types.CollectionItem.Type):
            Required. The type of item.
        item_resource (str):
            Required. The name of the CollectionItem. Its format depends
            on the ``type`` above. For ASSET:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}``
    """

    class Type(proto.Enum):
        r"""CollectionItem types.

        Values:
            TYPE_UNSPECIFIED (0):
                The default type of item should never happen.
            ASSET (1):
                Asset type item.
        """

        TYPE_UNSPECIFIED = 0
        ASSET = 1

    collection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    item_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateIndexRequest(proto.Message):
    r"""Message for creating an Index.

    Attributes:
        parent (str):
            Required. Value for the parent. The resource name of the
            Corpus under which this index is created. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
        index_id (str):
            Optional. The ID for the index. This will become the final
            resource name for the index. If the user does not specify
            this value, it will be generated by system.

            This value should be up to 63 characters, and valid
            characters are /[a-z][0-9]-/. The first character must be a
            letter, the last could be a letter or a number.
        index (google.cloud.visionai_v1.types.Index):
            Required. The index being created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    index_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    index: "Index" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Index",
    )


class CreateIndexMetadata(proto.Message):
    r"""Metadata message for CreateIndexRequest

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class UpdateIndexRequest(proto.Message):
    r"""Request message for UpdateIndex.

    Attributes:
        index (google.cloud.visionai_v1.types.Index):
            Required. The resource being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Index resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field of the resource will be
            overwritten if it is in the mask. Empty field mask is not
            allowed. If the mask is "\*", it triggers a full update of
            the index, and also a whole rebuild of index data.
    """

    index: "Index" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Index",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateIndexMetadata(proto.Message):
    r"""Metadata message for UpdateIndexRequest

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class GetIndexRequest(proto.Message):
    r"""Request message for getting an Index.

    Attributes:
        name (str):
            Required. Name of the Index resource. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIndexesRequest(proto.Message):
    r"""Request message for listing Indexes.

    Attributes:
        parent (str):
            Required. The parent corpus that owns this collection of
            indexes. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        page_size (int):
            The maximum number of indexes to return. The
            service may return fewer than this value.
            If unspecified, at most 50 indexes will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListIndexes`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListIndexes`` must match the call that provided the page
            token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListIndexesResponse(proto.Message):
    r"""Response message for ListIndexes.

    Attributes:
        indexes (MutableSequence[google.cloud.visionai_v1.types.Index]):
            The indexes under the specified corpus.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    indexes: MutableSequence["Index"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Index",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteIndexRequest(proto.Message):
    r"""Request message for DeleteIndex.

    Attributes:
        name (str):
            Required. The name of the index to delete. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteIndexMetadata(proto.Message):
    r"""Metadata message for DeleteIndexRequest"""


class Index(proto.Message):
    r"""An Index is a resource in Corpus. It contains an indexed
    version of the assets and annotations. When deployed to an
    endpoint, it will allow users to search the Index.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        entire_corpus (bool):
            Include all assets under the corpus.

            This field is a member of `oneof`_ ``asset_filter``.
        name (str):
            Output only. Resource name of the Index resource. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/indexes/{index_id}``
        display_name (str):
            Optional. Optional user-specified display
            name of the index.
        description (str):
            Optional. Optional description of the index.
        state (google.cloud.visionai_v1.types.Index.State):
            Output only. State of the index.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        deployed_indexes (MutableSequence[google.cloud.visionai_v1.types.DeployedIndexReference]):
            Output only. References to the deployed index instance.
            Index of VIDEO_ON_DEMAND corpus can have at most one
            deployed index. Index of IMAGE corpus can have multiple
            deployed indexes.
        satisfies_pzs (bool):
            Output only. This boolean field is only set
            for projects that have Physical Zone Separation
            enabled via an Org Policy constraint. It is set
            to true when the index is a valid zone separated
            index and false if it isn't.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. This boolean field is only set
            for projects that have Physical Zone Isolation
            enabled via an Org Policy constraint. It is set
            to true when the index is a valid zone isolated
            index and false if it isn't.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
    """

    class State(proto.Enum):
        r"""Enum representing the different states through which an Index
        might cycle during its lifetime.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. Should not be used.
            CREATING (1):
                State CREATING.
            CREATED (2):
                State CREATED.
            UPDATING (3):
                State UPDATING.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        UPDATING = 3

    entire_corpus: bool = proto.Field(
        proto.BOOL,
        number=9,
        oneof="asset_filter",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    deployed_indexes: MutableSequence["DeployedIndexReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="DeployedIndexReference",
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )


class DeployedIndexReference(proto.Message):
    r"""Points to a DeployedIndex.

    Attributes:
        index_endpoint (str):
            Immutable. A resource name of the
            IndexEndpoint.
    """

    index_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Corpus(proto.Message):
    r"""Corpus is a set of media contents for management.
    Within a corpus, media shares the same data schema. Search is
    also restricted within a single corpus.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Resource name of the corpus. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
        display_name (str):
            Required. The corpus name to shown in the UI.
            The name can be up to 32 characters long.
        description (str):
            Optional. Description of the corpus. Can be
            up to 25000 characters long.
        default_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The default TTL value for all assets under the
            corpus without a asset level user-defined TTL. For
            STREAM_VIDEO type corpora, this is required and the maximum
            allowed default_ttl is 10 years.
        type_ (google.cloud.visionai_v1.types.Corpus.Type):
            Optional. Type of the asset inside corpus.
        search_capability_setting (google.cloud.visionai_v1.types.SearchCapabilitySetting):
            Default search capability setting on corpus
            level.
        satisfies_pzs (bool):
            Output only. This boolean field is only set
            for projects that have Physical Zone Separation
            enabled via an Org Policy constraint. It is set
            to true when the corpus is a valid zone
            separated corpus and false if it isn't.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. This boolean field is only set
            for projects that have Physical Zone Isolation
            enabled via an Org Policy constraint. It is set
            to true when the corpus is a valid zone isolated
            corpus and false if it isn't.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
    """

    class Type(proto.Enum):
        r"""Type of the asset inside the corpus.

        Values:
            TYPE_UNSPECIFIED (0):
                The default type, not supposed to be used. If this default
                type is used, the corpus will be created as STREAM_VIDEO
                corpus.
            STREAM_VIDEO (1):
                Asset is a live streaming video.
            IMAGE (2):
                Asset is an image.
            VIDEO_ON_DEMAND (3):
                Asset is a batch video.
        """

        TYPE_UNSPECIFIED = 0
        STREAM_VIDEO = 1
        IMAGE = 2
        VIDEO_ON_DEMAND = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    default_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=Type,
    )
    search_capability_setting: "SearchCapabilitySetting" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SearchCapabilitySetting",
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )


class GetCorpusRequest(proto.Message):
    r"""Request message for GetCorpus.

    Attributes:
        name (str):
            Required. The resource name of the corpus to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCorpusRequest(proto.Message):
    r"""Request message for UpdateCorpus.

    Attributes:
        corpus (google.cloud.visionai_v1.types.Corpus):
            Required. The corpus which replaces the
            resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    corpus: "Corpus" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Corpus",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListCorporaRequest(proto.Message):
    r"""Request message for ListCorpora.

    Attributes:
        parent (str):
            Required. The resource name of the project
            from which to list corpora.
        page_size (int):
            Requested page size. API may return fewer results than
            requested. If negative, INVALID_ARGUMENT error will be
            returned. If unspecified or 0, API will pick a default size,
            which is 10. If the requested page size is larger than the
            maximum size, API will pick use the maximum size, which is
            20.
        page_token (str):
            A token identifying a page of results for the server to
            return. Typically obtained via
            [ListCorporaResponse.next_page_token][google.cloud.visionai.v1.ListCorporaResponse.next_page_token]
            of the previous
            [Warehouse.ListCorpora][google.cloud.visionai.v1.Warehouse.ListCorpora]
            call.
        filter (str):
            The filter applied to the returned corpora list. Only the
            following restrictions are supported:
            ``type=<Corpus.Type>``, ``type!=<Corpus.Type>``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCorporaResponse(proto.Message):
    r"""Response message for ListCorpora.

    Attributes:
        corpora (MutableSequence[google.cloud.visionai_v1.types.Corpus]):
            The corpora in the project.
        next_page_token (str):
            A token to retrieve next page of results. Pass to
            [ListCorporaRequest.page_token][google.cloud.visionai.v1.ListCorporaRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    corpora: MutableSequence["Corpus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Corpus",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteCorpusRequest(proto.Message):
    r"""Request message for DeleteCorpus.

    Attributes:
        name (str):
            Required. The resource name of the corpus to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AnalyzeCorpusRequest(proto.Message):
    r"""Request message for AnalyzeCorpus.

    Attributes:
        name (str):
            Required. The parent corpus resource where the assets will
            be analyzed. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AnalyzeCorpusMetadata(proto.Message):
    r"""The metadata message for AnalyzeCorpus LRO.

    Attributes:
        metadata (google.cloud.visionai_v1.types.OperationMetadata):
            The metadata of the operation.
    """

    metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class AnalyzeCorpusResponse(proto.Message):
    r"""The response message for AnalyzeCorpus LRO."""


class CreateDataSchemaRequest(proto.Message):
    r"""Request message for CreateDataSchema.

    Attributes:
        parent (str):
            Required. The parent resource where this data schema will be
            created. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
        data_schema (google.cloud.visionai_v1.types.DataSchema):
            Required. The data schema to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_schema: "DataSchema" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataSchema",
    )


class DataSchema(proto.Message):
    r"""Data schema indicates how the user specified annotation is
    interpreted in the system.

    Attributes:
        name (str):
            Resource name of the data schema in the form of:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/dataSchemas/{data_schema}``
            where {data_schema} part should be the same as the ``key``
            field below.
        key (str):
            Required. The key of this data schema. This key should be
            matching the key of user specified annotation and unique
            inside corpus. This value can be up to 63 characters, and
            valid characters are /[a-z][0-9]-/. The first character must
            be a letter, the last could be a letter or a number.
        schema_details (google.cloud.visionai_v1.types.DataSchemaDetails):
            The schema details mapping to the key.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schema_details: "DataSchemaDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataSchemaDetails",
    )


class DataSchemaDetails(proto.Message):
    r"""Data schema details indicates the data type and the data
    struct corresponding to the key of user specified annotation.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.visionai_v1.types.DataSchemaDetails.DataType):
            Type of the annotation.

            This field is a member of `oneof`_ ``_type``.
        proto_any_config (google.cloud.visionai_v1.types.DataSchemaDetails.ProtoAnyConfig):
            Config for protobuf any type.
        list_config (google.cloud.visionai_v1.types.DataSchemaDetails.ListConfig):
            Config for List data type.
        customized_struct_config (google.cloud.visionai_v1.types.DataSchemaDetails.CustomizedStructConfig):
            Config for CustomizedStruct data type.
        granularity (google.cloud.visionai_v1.types.DataSchemaDetails.Granularity):
            The granularity associated with this
            DataSchema.

            This field is a member of `oneof`_ ``_granularity``.
        search_strategy (google.cloud.visionai_v1.types.DataSchemaDetails.SearchStrategy):
            The search strategy to be applied on the ``key`` above.
    """

    class DataType(proto.Enum):
        r"""Data type of the annotation.

        Values:
            DATA_TYPE_UNSPECIFIED (0):
                Unspecified type.
            INTEGER (1):
                Integer type. Allowed search strategies:

                - DataSchema.SearchStrategy.NO_SEARCH,
                - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
                  IntRangeArray.
            FLOAT (2):
                Float type. Allowed search strategies:

                - DataSchema.SearchStrategy.NO_SEARCH,
                - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
                  FloatRangeArray.
            STRING (3):
                String type. Allowed search strategies:

                - DataSchema.SearchStrategy.NO_SEARCH,
                - DataSchema.SearchStrategy.EXACT_SEARCH,
                - DataSchema.SearchStrategy.SMART_SEARCH.
            DATETIME (5):
                Supported formats: %Y-%m-%dT%H:%M:%E\ *S%E*\ z
                (absl::RFC3339_full) %Y-%m-%dT%H:%M:%E\ *S
                %Y-%m-%dT%H:%M%E*\ z %Y-%m-%dT%H:%M %Y-%m-%dT%H%E\ *z
                %Y-%m-%dT%H %Y-%m-%d%E*\ z %Y-%m-%d %Y-%m %Y Allowed search
                strategies:

                - DataSchema.SearchStrategy.NO_SEARCH,
                - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
                  DateTimeRangeArray.
            GEO_COORDINATE (7):
                Geo coordinate type. Allowed search strategies:

                - DataSchema.SearchStrategy.NO_SEARCH,
                - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
                  GeoLocationArray.
            PROTO_ANY (8):
                Type to pass any proto as available in annotations.proto.
                Only use internally. Available proto types and its
                corresponding search behavior:

                - ImageObjectDetectionPredictionResult, allows SMART_SEARCH
                  on display_names and NO_SEARCH.
                - ClassificationPredictionResult, allows SMART_SEARCH on
                  display_names and NO_SEARCH.
                - ImageSegmentationPredictionResult, allows NO_SEARCH.
                - VideoActionRecognitionPredictionResult, allows
                  SMART_SEARCH on display_name and NO_SEARCH.
                - VideoObjectTrackingPredictionResult, allows SMART_SEARCH
                  on display_name and NO_SEARCH.
                - VideoClassificationPredictionResult, allows SMART_SEARCH
                  on display_name and NO_SEARCH.
                - OccupancyCountingPredictionResult, allows EXACT_SEARCH on
                  stats.full_frame_count.count and NO_SEARCH.
                - ObjectDetectionPredictionResult, allows SMART_SEARCH on
                  identified_boxes.entity.label_string and NO_SEARCH.
            BOOLEAN (9):
                Boolean type. Allowed search strategies:

                - DataSchema.SearchStrategy.NO_SEARCH,
                - DataSchema.SearchStrategy.EXACT_SEARCH.
            LIST (10):
                List type.

                - Each element in the list must be of the exact same data
                  schema; otherwise, they are invalid arguments.
                - List level cannot set search strategy. Leaf node level can
                  do.
                - Elements cannot be another list (no list of list).
                - Elements can be CUSTOMIZED_STRUCT, and max number of
                  layers is 10.
            CUSTOMIZED_STRUCT (6):
                Struct type.

                - SearchStrategy:

                  - Data Schema that's CUSTOMIZED_STRUCT cannot set search
                    strategy.
                  - Leaf-node elements allow setting search strategy based
                    on element's SearchStrategy restriction.

                - Nested layer restrictions:

                  - Data Schema that's CUSTOMIZED_STRUCT allows its fields
                    to be of CUSTOMIZED_STRUCT as well, but the overall
                    layers restriction is 10.
        """

        DATA_TYPE_UNSPECIFIED = 0
        INTEGER = 1
        FLOAT = 2
        STRING = 3
        DATETIME = 5
        GEO_COORDINATE = 7
        PROTO_ANY = 8
        BOOLEAN = 9
        LIST = 10
        CUSTOMIZED_STRUCT = 6

    class Granularity(proto.Enum):
        r"""The granularity of annotations under this DataSchema.

        Values:
            GRANULARITY_UNSPECIFIED (0):
                Unspecified granularity.
            GRANULARITY_ASSET_LEVEL (1):
                Asset-level granularity (annotations must not
                contain partition info).
            GRANULARITY_PARTITION_LEVEL (2):
                Partition-level granularity (annotations must
                contain partition info).
        """

        GRANULARITY_UNSPECIFIED = 0
        GRANULARITY_ASSET_LEVEL = 1
        GRANULARITY_PARTITION_LEVEL = 2

    class ProtoAnyConfig(proto.Message):
        r"""The configuration for ``PROTO_ANY`` data type.

        Attributes:
            type_uri (str):
                The type URI of the proto message.
        """

        type_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ListConfig(proto.Message):
        r"""The configuration for ``LIST`` data type.

        Attributes:
            value_schema (google.cloud.visionai_v1.types.DataSchemaDetails):
                The value's data schema in the list.
        """

        value_schema: "DataSchemaDetails" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataSchemaDetails",
        )

    class CustomizedStructConfig(proto.Message):
        r"""The configuration for ``CUSTOMIZED_STRUCT`` data type.

        Attributes:
            field_schemas (MutableMapping[str, google.cloud.visionai_v1.types.DataSchemaDetails]):
                Direct child elements data schemas.
        """

        field_schemas: MutableMapping[str, "DataSchemaDetails"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="DataSchemaDetails",
        )

    class SearchStrategy(proto.Message):
        r"""The search strategy for annotations value of the ``key``.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            search_strategy_type (google.cloud.visionai_v1.types.DataSchemaDetails.SearchStrategy.SearchStrategyType):
                The type of search strategy to be applied on the ``key``
                above. The allowed ``search_strategy_type`` is different for
                different data types, which is documented in the
                DataSchemaDetails.DataType. Specifying unsupported
                ``search_strategy_type`` for data types will result in
                INVALID_ARGUMENT error.

                This field is a member of `oneof`_ ``_search_strategy_type``.
            confidence_score_index_config (google.cloud.visionai_v1.types.DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig):
                Optional. Configs the path to the confidence score, and the
                threshold. Only if the score is greater than the threshold,
                current field will be built into the index. Only applies to
                leaf nodes using EXACT_SEARCH or SMART_SEARCH.
        """

        class SearchStrategyType(proto.Enum):
            r"""The types of search strategies to be applied on the
            annotation key.

            Values:
                NO_SEARCH (0):
                    Annotatation values of the ``key`` above will not be
                    searchable.
                EXACT_SEARCH (1):
                    When searching with ``key``, the value must be exactly as
                    the annotation value that has been ingested.
                SMART_SEARCH (2):
                    When searching with ``key``, Warehouse will perform broad
                    search based on semantic of the annotation value.
            """

            NO_SEARCH = 0
            EXACT_SEARCH = 1
            SMART_SEARCH = 2

        class ConfidenceScoreIndexConfig(proto.Message):
            r"""Filter on the confidence score. Only adds to index if the confidence
            score is higher than the threshold. Example data schema: key:
            "name-confidence-pair" type: CUSTOMIZED_STRUCT granularity:
            GRANULARITY_PARTITION_LEVEL customized_struct_config { field_schemas
            { key: "name" type: STRING granularity: GRANULARITY_PARTITION_LEVEL
            search_strategy { search_strategy_type: SMART_SEARCH
            confidence_score_index_config { field_path:
            "name-confidence-pair.score" threshold: 0.6 } } } field_schemas {
            key: "score" type: FLOAT granularity: GRANULARITY_PARTITION_LEVEL }
            } This means only "name" with score > 0.6 will be indexed.

            Attributes:
                field_path (str):
                    Required. The path to the confidence score field. It is a
                    string that concatenates all the data schema keys along the
                    path. See the example above. If the data schema contains
                    LIST, use '\_ENTRIES' to concatenate. Example data schema
                    contains a list: "key": "list-name-score", "schemaDetails":
                    { "type": "LIST", "granularity":
                    "GRANULARITY_PARTITION_LEVEL", "listConfig": {
                    "valueSchema": { "type": "CUSTOMIZED_STRUCT", "granularity":
                    "GRANULARITY_PARTITION_LEVEL", "customizedStructConfig": {
                    "fieldSchemas": { "name": { "type": "STRING", "granularity":
                    "GRANULARITY_PARTITION_LEVEL", "searchStrategy": {
                    "searchStrategyType": "SMART_SEARCH"
                    "confidence_score_index_config": { "field_path":
                    "list-name-score._ENTRIES.score", "threshold": "0.9", } } },
                    "score": { "type": "FLOAT", "granularity":
                    "GRANULARITY_PARTITION_LEVEL", } } } } } }
                threshold (float):
                    Required. The threshold.
            """

            field_path: str = proto.Field(
                proto.STRING,
                number=1,
            )
            threshold: float = proto.Field(
                proto.FLOAT,
                number=2,
            )

        search_strategy_type: "DataSchemaDetails.SearchStrategy.SearchStrategyType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum="DataSchemaDetails.SearchStrategy.SearchStrategyType",
            )
        )
        confidence_score_index_config: "DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig",
        )

    type_: DataType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=DataType,
    )
    proto_any_config: ProtoAnyConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=ProtoAnyConfig,
    )
    list_config: ListConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=ListConfig,
    )
    customized_struct_config: CustomizedStructConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=CustomizedStructConfig,
    )
    granularity: Granularity = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=Granularity,
    )
    search_strategy: SearchStrategy = proto.Field(
        proto.MESSAGE,
        number=7,
        message=SearchStrategy,
    )


class UpdateDataSchemaRequest(proto.Message):
    r"""Request message for UpdateDataSchema.

    Attributes:
        data_schema (google.cloud.visionai_v1.types.DataSchema):
            Required. The data schema's ``name`` field is used to
            identify the data schema to be updated. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/dataSchemas/{data_schema}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    data_schema: "DataSchema" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataSchema",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetDataSchemaRequest(proto.Message):
    r"""Request message for GetDataSchema.

    Attributes:
        name (str):
            Required. The name of the data schema to retrieve. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteDataSchemaRequest(proto.Message):
    r"""Request message for DeleteDataSchema.

    Attributes:
        name (str):
            Required. The name of the data schema to delete. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataSchemasRequest(proto.Message):
    r"""Request message for ListDataSchemas.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of data
            schemas. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
        page_size (int):
            The maximum number of data schemas to return.
            The service may return fewer than this value. If
            unspecified, at most 50 data schemas will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListDataSchemas``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDataSchemas`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListDataSchemasResponse(proto.Message):
    r"""Response message for ListDataSchemas.

    Attributes:
        data_schemas (MutableSequence[google.cloud.visionai_v1.types.DataSchema]):
            The data schemas from the specified corpus.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_schemas: MutableSequence["DataSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataSchema",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAnnotationRequest(proto.Message):
    r"""Request message for CreateAnnotation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent resource where this annotation will be
            created. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        annotation (google.cloud.visionai_v1.types.Annotation):
            Required. The annotation to create.
        annotation_id (str):
            Optional. The ID to use for the annotation, which will
            become the final component of the annotation's resource name
            if user choose to specify. Otherwise, annotation id will be
            generated by system.

            This value should be up to 63 characters, and valid
            characters are /[a-z][0-9]-/. The first character must be a
            letter, the last could be a letter or a number.

            This field is a member of `oneof`_ ``_annotation_id``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotation: "Annotation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Annotation",
    )
    annotation_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class Annotation(proto.Message):
    r"""An annotation is a resource in asset. It represents a
    key-value mapping of content in asset.

    Attributes:
        name (str):
            Resource name of the annotation. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}``
        user_specified_annotation (google.cloud.visionai_v1.types.UserSpecifiedAnnotation):
            User provided annotation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_specified_annotation: "UserSpecifiedAnnotation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserSpecifiedAnnotation",
    )


class UserSpecifiedAnnotation(proto.Message):
    r"""Annotation provided by users.

    Attributes:
        key (str):
            Required. Key of the annotation. The key must
            be set with type by CreateDataSchema.
        value (google.cloud.visionai_v1.types.AnnotationValue):
            Value of the annotation. The value must be
            able to convert to the type according to the
            data schema.
        partition (google.cloud.visionai_v1.types.Partition):
            Partition information in time and space for
            the sub-asset level annotation.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: "AnnotationValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AnnotationValue",
    )
    partition: "Partition" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Partition",
    )


class GeoCoordinate(proto.Message):
    r"""Location Coordinate Representation

    Attributes:
        latitude (float):
            Latitude Coordinate. Degrees [-90 .. 90]
        longitude (float):
            Longitude Coordinate. Degrees [-180 .. 180]
    """

    latitude: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    longitude: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class AnnotationValue(proto.Message):
    r"""Value of annotation, including all types available in data
    schema.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        int_value (int):
            Value of int type annotation.

            This field is a member of `oneof`_ ``value``.
        float_value (float):
            Value of float type annotation.

            This field is a member of `oneof`_ ``value``.
        str_value (str):
            Value of string type annotation.

            This field is a member of `oneof`_ ``value``.
        datetime_value (str):
            Value of date time type annotation.

            This field is a member of `oneof`_ ``value``.
        geo_coordinate (google.cloud.visionai_v1.types.GeoCoordinate):
            Value of geo coordinate type annotation.

            This field is a member of `oneof`_ ``value``.
        proto_any_value (google.protobuf.any_pb2.Any):
            Value of any proto value.

            This field is a member of `oneof`_ ``value``.
        bool_value (bool):
            Value of boolean type annotation.

            This field is a member of `oneof`_ ``value``.
        customized_struct_data_value (google.protobuf.struct_pb2.Struct):
            Value of customized struct annotation. This field does not
            have effects. Use customized_struct_value instead for
            customized struct annotation.

            This field is a member of `oneof`_ ``value``.
        list_value (google.cloud.visionai_v1.types.AnnotationList):
            Value of list type annotation.

            This field is a member of `oneof`_ ``value``.
        customized_struct_value (google.cloud.visionai_v1.types.AnnotationCustomizedStruct):
            Value of custom struct type annotation.

            This field is a member of `oneof`_ ``value``.
    """

    int_value: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="value",
    )
    float_value: float = proto.Field(
        proto.FLOAT,
        number=2,
        oneof="value",
    )
    str_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="value",
    )
    datetime_value: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="value",
    )
    geo_coordinate: "GeoCoordinate" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value",
        message="GeoCoordinate",
    )
    proto_any_value: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value",
        message=any_pb2.Any,
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=9,
        oneof="value",
    )
    customized_struct_data_value: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="value",
        message=struct_pb2.Struct,
    )
    list_value: "AnnotationList" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="value",
        message="AnnotationList",
    )
    customized_struct_value: "AnnotationCustomizedStruct" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message="AnnotationCustomizedStruct",
    )


class AnnotationList(proto.Message):
    r"""List representation in annotation.

    Attributes:
        values (MutableSequence[google.cloud.visionai_v1.types.AnnotationValue]):
            The values of ``LIST`` data type annotation.
    """

    values: MutableSequence["AnnotationValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AnnotationValue",
    )


class AnnotationCustomizedStruct(proto.Message):
    r"""Customized struct represnation in annotation.

    Attributes:
        elements (MutableMapping[str, google.cloud.visionai_v1.types.AnnotationValue]):
            A map from elements' keys to element's
            annotation value.
    """

    elements: MutableMapping[str, "AnnotationValue"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="AnnotationValue",
    )


class ListAnnotationsRequest(proto.Message):
    r"""Request message for GetAnnotation API.

    Attributes:
        parent (str):
            The parent, which owns this collection of annotations.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}``
        page_size (int):
            The maximum number of annotations to return.
            The service may return fewer than this value. If
            unspecified, at most 50 annotations will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListAnnotations``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAnnotations`` must match the call that provided the
            page token.
        filter (str):
            The filter applied to the returned list. We only support
            filtering for the following fields: For corpus of
            STREAM_VIDEO type:
            ``partition.temporal_partition.start_time``,
            ``partition.temporal_partition.end_time``, and ``key``. For
            corpus of VIDEO_ON_DEMAND type,
            ``partition.relative_temporal_partition.start_offset``,
            ``partition.relative_temporal_partition.end_offset``, and
            ``key``. For corpus of IMAGE type, only ``key`` is
            supported. Timestamps are specified in the RFC-3339 format,
            and only one restriction may be applied per field, joined by
            conjunctions. Format:
            "partition.temporal_partition.start_time >
            "2012-04-21T11:30:00-04:00" AND
            partition.temporal_partition.end_time <
            "2012-04-22T11:30:00-04:00" AND key = "example_key"".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAnnotationsResponse(proto.Message):
    r"""Request message for ListAnnotations API.

    Attributes:
        annotations (MutableSequence[google.cloud.visionai_v1.types.Annotation]):
            The annotations from the specified asset.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    annotations: MutableSequence["Annotation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Annotation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAnnotationRequest(proto.Message):
    r"""Request message for GetAnnotation API.

    Attributes:
        name (str):
            Required. The name of the annotation to retrieve. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAnnotationRequest(proto.Message):
    r"""Request message for UpdateAnnotation API.

    Attributes:
        annotation (google.cloud.visionai_v1.types.Annotation):
            Required. The annotation to update. The annotation's
            ``name`` field is used to identify the annotation to be
            updated. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    annotation: "Annotation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Annotation",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAnnotationRequest(proto.Message):
    r"""Request message for DeleteAnnotation API.

    Attributes:
        name (str):
            Required. The name of the annotation to delete. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportAssetsRequest(proto.Message):
    r"""The request message for ImportAssets.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        assets_gcs_uri (str):
            The file contains all assets information to be imported.

            - The file is in JSONL format.
            - Each line corresponding to one asset.
            - Each line will be converted into InputImageAsset proto.

            This field is a member of `oneof`_ ``source``.
        parent (str):
            Required. The parent corpus resource where the assets will
            be imported. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
    """

    assets_gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportAssetsMetadata(proto.Message):
    r"""The metadata message for ImportAssets LRO.

    Attributes:
        metadata (google.cloud.visionai_v1.types.OperationMetadata):
            The metadata of the operation.
        status (google.cloud.visionai_v1.types.BatchOperationStatus):
            The importing status including partial
            failures, if the implementation can provide such
            information during the progress of the
            ImportAssets.
    """

    metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )
    status: "BatchOperationStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BatchOperationStatus",
    )


class BatchOperationStatus(proto.Message):
    r"""The batch operation status.

    Attributes:
        success_count (int):
            The count of assets (together with their
            annotations if any) successfully ingested.
        failure_count (int):
            The count of assets failed to ingested; it
            might be due to the annotation ingestion error.
    """

    success_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    failure_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ImportAssetsResponse(proto.Message):
    r"""The response message for ImportAssets LRO."""


class CreateSearchConfigRequest(proto.Message):
    r"""Request message for CreateSearchConfig.

    Attributes:
        parent (str):
            Required. The parent resource where this search
            configuration will be created. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}``
        search_config (google.cloud.visionai_v1.types.SearchConfig):
            Required. The search config to create.
        search_config_id (str):
            Required. ID to use for the new search config. Will become
            the final component of the SearchConfig's resource name.
            This value should be up to 63 characters, and valid
            characters are /[a-z][0-9]-\_/. The first character must be
            a letter, the last could be a letter or a number.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_config: "SearchConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SearchConfig",
    )
    search_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateSearchConfigRequest(proto.Message):
    r"""Request message for UpdateSearchConfig.

    Attributes:
        search_config (google.cloud.visionai_v1.types.SearchConfig):
            Required. The search configuration to update.

            The search configuration's ``name`` field is used to
            identify the resource to be updated. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated. If left
            unset, all field paths will be
            updated/overwritten.
    """

    search_config: "SearchConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SearchConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetSearchConfigRequest(proto.Message):
    r"""Request message for GetSearchConfig.

    Attributes:
        name (str):
            Required. The name of the search configuration to retrieve.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteSearchConfigRequest(proto.Message):
    r"""Request message for DeleteSearchConfig.

    Attributes:
        name (str):
            Required. The name of the search configuration to delete.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSearchConfigsRequest(proto.Message):
    r"""Request message for ListSearchConfigs.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of search
            configurations. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        page_size (int):
            The maximum number of search configurations
            to return. The service may return fewer than
            this value. If unspecified, a page size of 50
            will be used. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListSearchConfigs``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListSearchConfigs`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSearchConfigsResponse(proto.Message):
    r"""Response message for ListSearchConfigs.

    Attributes:
        search_configs (MutableSequence[google.cloud.visionai_v1.types.SearchConfig]):
            The search configurations from the specified
            corpus.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    search_configs: MutableSequence["SearchConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchConfig(proto.Message):
    r"""SearchConfig stores different properties that will affect
    search behaviors and search results.

    Attributes:
        name (str):
            Resource name of the search configuration. For
            CustomSearchCriteria, search_config would be the search
            operator name. For Facets, search_config would be the facet
            dimension name. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}``
        facet_property (google.cloud.visionai_v1.types.FacetProperty):
            Establishes a FacetDimension and associated
            specifications.
        search_criteria_property (google.cloud.visionai_v1.types.SearchCriteriaProperty):
            Creates a mapping between a custom
            SearchCriteria and one or more UGA keys.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    facet_property: "FacetProperty" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FacetProperty",
    )
    search_criteria_property: "SearchCriteriaProperty" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SearchCriteriaProperty",
    )


class IndexEndpoint(proto.Message):
    r"""Message representing IndexEndpoint resource. Indexes are
    deployed into it.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Resource name of the IndexEndpoint. Format:
            ``projects/{project}/locations/{location}/indexEndpoints/{index_endpoint_id}``
        display_name (str):
            Optional. Display name of the IndexEndpoint.
            Can be up to 32 characters long.
        description (str):
            Optional. Description of the IndexEndpoint.
            Can be up to 25000 characters long.
        deployed_index (google.cloud.visionai_v1.types.DeployedIndex):
            Output only. The Index deployed in this
            IndexEndpoint.
        state (google.cloud.visionai_v1.types.IndexEndpoint.State):
            Output only. IndexEndpoint state.
        labels (MutableMapping[str, str]):
            Optional. The labels applied to a resource must meet the
            following requirements:

            - Each resource can have multiple labels, up to a maximum of
              64.
            - Each label must be a key-value pair.
            - Keys have a minimum length of 1 character and a maximum
              length of 63 characters and cannot be empty. Values can be
              empty and have a maximum length of 63 characters.
            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes. All
              characters must use UTF-8 encoding, and international
              characters are allowed.
            - The key portion of a label must be unique. However, you
              can use the same key with multiple resources.
            - Keys must start with a lowercase letter or international
              character.

            See `Google Cloud
            Document <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`__
            for more details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        satisfies_pzs (bool):
            Output only. This boolean field is only set
            for projects that have Physical Zone Separation
            enabled via an Org Policy constraint. It is set
            to true when the index endpoint is a valid zone
            separated index endpoint and false if it isn't.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. This boolean field is only set
            for projects that have Physical Zone Isolation
            enabled via an Org Policy constraint. It is set
            to true when the index endpoint is a valid zone
            isolated index endpoint and false if it isn't.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
    """

    class State(proto.Enum):
        r"""IndexEndpoint stage.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. Should not be used.
            CREATING (1):
                State CREATING.
            CREATED (2):
                State CREATED.
            UPDATING (3):
                State UPDATING.
            FAILED (4):
                State FAILED.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        UPDATING = 3
        FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deployed_index: "DeployedIndex" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="DeployedIndex",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )


class CreateIndexEndpointRequest(proto.Message):
    r"""Request message for CreateIndexEndpoint.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project}/locations/{location}``
        index_endpoint_id (str):
            Optional. The ID to use for the
            IndexEndpoint, which will become the final
            component of the IndexEndpoint's resource name
            if the user specifies it. Otherwise,
            IndexEndpoint id will be autogenerated.

            This value should be up to 63 characters, and
            valid characters are a-z, 0-9 and dash (-). The
            first character must be a letter, the last must
            be a letter or a number.
        index_endpoint (google.cloud.visionai_v1.types.IndexEndpoint):
            Required. The resource being created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    index_endpoint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    index_endpoint: "IndexEndpoint" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="IndexEndpoint",
    )


class CreateIndexEndpointMetadata(proto.Message):
    r"""Metadata message for CreateIndexEndpoint.

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class GetIndexEndpointRequest(proto.Message):
    r"""Request message for GetIndexEndpoint.

    Attributes:
        name (str):
            Required. Name of the IndexEndpoint resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIndexEndpointsRequest(proto.Message):
    r"""Request message for ListIndexEndpoints.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. The service
            may return fewer than this value. If
            unspecified, a page size of 50 will be used. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. The filter applied to the returned list. We only
            support filtering for the
            ``deployed_image_index.image_index`` field. However, to
            filter by a corpus instead of an image index, simply use
            ``deployed_image_index.corpus``, which will return all
            endpoints with ``deployed_image_index.image_index`` inside
            of the given corpus. A basic filter on image index would
            look like: deployed_image_index.image_index =
            "projects/123/locations/us-central1/corpora/my_corpus/imageIndexes/my_image_index"
            A basic filter on corpus would look like:
            deployed_image_index.corpus =
            "projects/123/locations/us-central1/corpora/my_corpus".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListIndexEndpointsResponse(proto.Message):
    r"""Response message for ListIndexEndpoints.

    Attributes:
        index_endpoints (MutableSequence[google.cloud.visionai_v1.types.IndexEndpoint]):
            The list of IndexEndpoints.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    index_endpoints: MutableSequence["IndexEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IndexEndpoint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateIndexEndpointRequest(proto.Message):
    r"""Request message for UpdateIndexEndpoint.

    Attributes:
        index_endpoint (google.cloud.visionai_v1.types.IndexEndpoint):
            Required. The resource being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the IndexEndpoint resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field of the resource will
            be overwritten if it is in the mask. Empty field mask is not
            allowed. If the mask is "\*", then this is a full
            replacement of the resource.
    """

    index_endpoint: "IndexEndpoint" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IndexEndpoint",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateIndexEndpointMetadata(proto.Message):
    r"""Metadata message for UpdateIndexEndpoint.

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class DeleteIndexEndpointRequest(proto.Message):
    r"""Request message for DeleteIndexEndpoint.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteIndexEndpointMetadata(proto.Message):
    r"""Metadata message for DeleteIndexEndpoint.

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )


class DeployIndexRequest(proto.Message):
    r"""Request message for DeployIndex.

    Attributes:
        index_endpoint (str):
            Required. IndexEndpoint the index is deployed to. Format:
            ``projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}``
        deployed_index (google.cloud.visionai_v1.types.DeployedIndex):
            Required. Index to deploy.
    """

    index_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployed_index: "DeployedIndex" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DeployedIndex",
    )


class DeployIndexResponse(proto.Message):
    r"""DeployIndex response once the operation is done."""


class DeployIndexMetadata(proto.Message):
    r"""Metadata message for DeployIndex.

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
        deployed_index (str):
            Output only. The index being deployed.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )
    deployed_index: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UndeployIndexMetadata(proto.Message):
    r"""Metadata message for UndeployIndex.

    Attributes:
        operation_metadata (google.cloud.visionai_v1.types.OperationMetadata):
            Common metadata of the long-running
            operation.
        deployed_index (str):
            Output only. The index being undeployed.
    """

    operation_metadata: common.OperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.OperationMetadata,
    )
    deployed_index: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UndeployIndexRequest(proto.Message):
    r"""Request message for UndeployIndexEndpoint.

    Attributes:
        index_endpoint (str):
            Required. Resource name of the IndexEndpoint resource on
            which the undeployment will act. Format:
            ``projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}``
    """

    index_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeployIndexResponse(proto.Message):
    r"""UndeployIndex response once the operation is done."""


class DeployedIndex(proto.Message):
    r"""A deployment of an Index.

    Attributes:
        index (str):
            Required. Name of the deployed Index. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/indexes/{index_id}``
    """

    index: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FacetProperty(proto.Message):
    r"""Central configuration for a facet.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        fixed_range_bucket_spec (google.cloud.visionai_v1.types.FacetProperty.FixedRangeBucketSpec):
            Fixed range facet bucket config.

            This field is a member of `oneof`_ ``range_facet_config``.
        custom_range_bucket_spec (google.cloud.visionai_v1.types.FacetProperty.CustomRangeBucketSpec):
            Custom range facet bucket config.

            This field is a member of `oneof`_ ``range_facet_config``.
        datetime_bucket_spec (google.cloud.visionai_v1.types.FacetProperty.DateTimeBucketSpec):
            Datetime range facet bucket config.

            This field is a member of `oneof`_ ``range_facet_config``.
        mapped_fields (MutableSequence[str]):
            Name of the facets, which are the dimensions users want to
            use to refine search results. ``mapped_fields`` will match
            UserSpecifiedDataSchema keys.

            For example, user can add a bunch of UGAs with the same key,
            such as player:adam, player:bob, player:charles. When
            multiple mapped_fields are specified, will merge their value
            together as final facet value. E.g. home_team: a,
            home_team:b, away_team:a, away_team:c, when facet_field =
            [home_team, away_team], facet_value will be [a, b, c].

            UNLESS this is a 1:1 facet dimension (mapped_fields.size()
            == 1) AND the mapped_field equals the parent
            SearchConfig.name, the parent must also contain a
            SearchCriteriaProperty that maps to the same fields.
            mapped_fields must not be empty.
        display_name (str):
            Display name of the facet. To be used by UI
            for facet rendering.
        result_size (int):
            Maximum number of unique bucket to return for one facet.
            Bucket number can be large for high-cardinality facet such
            as "player". We only return top-n most related ones to user.
            If it's <= 0, the server will decide the appropriate
            result_size.
        bucket_type (google.cloud.visionai_v1.types.FacetBucketType):
            Facet bucket type e.g. value, range.
    """

    class FixedRangeBucketSpec(proto.Message):
        r"""If bucket type is FIXED_RANGE, specify how values are bucketized.
        Use FixedRangeBucketSpec when you want to create multiple buckets
        with equal granularities. Using integer bucket value as an example,
        when bucket_start = 0, bucket_granularity = 10, bucket_count = 5,
        this facet will be aggregated via the following buckets: [-inf, 0),
        [0, 10), [10, 20), [20, 30), [30, inf). Notably, bucket_count <= 1
        is an invalid spec.

        Attributes:
            bucket_start (google.cloud.visionai_v1.types.FacetValue):
                Lower bound of the bucket. NOTE: Only integer
                type is currently supported for this field.
            bucket_granularity (google.cloud.visionai_v1.types.FacetValue):
                Bucket granularity. NOTE: Only integer type
                is currently supported for this field.
            bucket_count (int):
                Total number of buckets.
        """

        bucket_start: "FacetValue" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="FacetValue",
        )
        bucket_granularity: "FacetValue" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="FacetValue",
        )
        bucket_count: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class CustomRangeBucketSpec(proto.Message):
        r"""If bucket type is CUSTOM_RANGE, specify how values are bucketized.
        Use integer bucket value as an example, when the endpoints are 0,
        10, 100, and 1000, we will generate the following facets: [-inf, 0),
        [0, 10), [10, 100), [100, 1000), [1000, inf). Notably:

        - endpoints must be listed in ascending order. Otherwise, the
          SearchConfig API will reject the facet config.
        - < 1 endpoints is an invalid spec.

        Attributes:
            endpoints (MutableSequence[google.cloud.visionai_v1.types.FacetValue]):
                Currently, only integer type is supported for
                this field.
        """

        endpoints: MutableSequence["FacetValue"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="FacetValue",
        )

    class DateTimeBucketSpec(proto.Message):
        r"""If bucket type is DATE, specify how date values are
        bucketized.

        Attributes:
            granularity (google.cloud.visionai_v1.types.FacetProperty.DateTimeBucketSpec.Granularity):
                Granularity of date type facet.
        """

        class Granularity(proto.Enum):
            r"""Granularity enum for the datetime bucket.

            Values:
                GRANULARITY_UNSPECIFIED (0):
                    Unspecified granularity.
                YEAR (1):
                    Granularity is year.
                MONTH (2):
                    Granularity is month.
                DAY (3):
                    Granularity is day.
            """

            GRANULARITY_UNSPECIFIED = 0
            YEAR = 1
            MONTH = 2
            DAY = 3

        granularity: "FacetProperty.DateTimeBucketSpec.Granularity" = proto.Field(
            proto.ENUM,
            number=1,
            enum="FacetProperty.DateTimeBucketSpec.Granularity",
        )

    fixed_range_bucket_spec: FixedRangeBucketSpec = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="range_facet_config",
        message=FixedRangeBucketSpec,
    )
    custom_range_bucket_spec: CustomRangeBucketSpec = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="range_facet_config",
        message=CustomRangeBucketSpec,
    )
    datetime_bucket_spec: DateTimeBucketSpec = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="range_facet_config",
        message=DateTimeBucketSpec,
    )
    mapped_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    result_size: int = proto.Field(
        proto.INT64,
        number=3,
    )
    bucket_type: "FacetBucketType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="FacetBucketType",
    )


class SearchHypernym(proto.Message):
    r"""Search resource: SearchHypernym. For example, { hypernym: "vehicle"
    hyponyms: ["sedan", "truck"] } This means in SMART_SEARCH mode,
    searching for "vehicle" will also return results with "sedan" or
    "truck" as annotations.

    Attributes:
        name (str):
            Resource name of the SearchHypernym. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}``
        hypernym (str):
            Optional. The hypernym.
        hyponyms (MutableSequence[str]):
            Optional. Hyponyms that the hypernym is
            mapped to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hypernym: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hyponyms: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateSearchHypernymRequest(proto.Message):
    r"""Request message for creating SearchHypernym.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent resource where this SearchHypernym will
            be created. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        search_hypernym (google.cloud.visionai_v1.types.SearchHypernym):
            Required. The SearchHypernym to create.
        search_hypernym_id (str):
            Optional. The search hypernym id.
            If omitted, a random UUID will be generated.

            This field is a member of `oneof`_ ``_search_hypernym_id``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_hypernym: "SearchHypernym" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SearchHypernym",
    )
    search_hypernym_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class UpdateSearchHypernymRequest(proto.Message):
    r"""Request message for updating SearchHypernym.

    Attributes:
        search_hypernym (google.cloud.visionai_v1.types.SearchHypernym):
            Required. The SearchHypernym to update. The search
            hypernym's ``name`` field is used to identify the search
            hypernym to be updated. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated. If left
            unset, all field paths will be
            updated/overwritten.
    """

    search_hypernym: "SearchHypernym" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SearchHypernym",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetSearchHypernymRequest(proto.Message):
    r"""Request message for getting SearchHypernym.

    Attributes:
        name (str):
            Required. The name of the SearchHypernym to retrieve.
            Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteSearchHypernymRequest(proto.Message):
    r"""Request message for deleting SearchHypernym.

    Attributes:
        name (str):
            Required. The name of the SearchHypernym to delete. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSearchHypernymsRequest(proto.Message):
    r"""Request message for listing SearchHypernyms.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            SearchHypernyms. Format:
            ``projects/{project_number}/locations/{location}/corpora/{corpus}``
        page_size (int):
            The maximum number of SearchHypernyms
            returned. The service may return fewer than this
            value. If unspecified, a page size of 50 will be
            used. The maximum value is 1000; values above
            1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``SearchHypernym``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``SearchHypernym`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSearchHypernymsResponse(proto.Message):
    r"""Response message for listing SearchHypernyms.

    Attributes:
        search_hypernyms (MutableSequence[google.cloud.visionai_v1.types.SearchHypernym]):
            The SearchHypernyms from the specified
            corpus.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    search_hypernyms: MutableSequence["SearchHypernym"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchHypernym",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchCriteriaProperty(proto.Message):
    r"""Central configuration for custom search criteria.

    Attributes:
        mapped_fields (MutableSequence[str]):
            Each mapped_field corresponds to a UGA key. To understand
            how this property works, take the following example. In the
            SearchConfig table, the user adds this entry: search_config
            { name: "person" search_criteria_property { mapped_fields:
            "player" mapped_fields: "coach" } }

            Now, when a user issues a query like: criteria { field:
            "person" text_array { txt_values: "Tom Brady" txt_values:
            "Bill Belichick" } }

            MWH search will return search documents where (player=Tom
            Brady \|\| coach=Tom Brady \|\| player=Bill Belichick \|\|
            coach=Bill Belichick).
    """

    mapped_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class FacetValue(proto.Message):
    r"""Definition of a single value with generic type.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_value (str):
            String type value.

            This field is a member of `oneof`_ ``value``.
        integer_value (int):
            Integer type value.

            This field is a member of `oneof`_ ``value``.
        datetime_value (google.type.datetime_pb2.DateTime):
            Datetime type value.

            This field is a member of `oneof`_ ``value``.
    """

    string_value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="value",
    )
    integer_value: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="value",
    )
    datetime_value: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value",
        message=datetime_pb2.DateTime,
    )


class FacetBucket(proto.Message):
    r"""Holds the facet value, selections state, and metadata.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (google.cloud.visionai_v1.types.FacetValue):
            Singular value.

            This field is a member of `oneof`_ ``bucket_value``.
        range_ (google.cloud.visionai_v1.types.FacetBucket.Range):
            Range value.

            This field is a member of `oneof`_ ``bucket_value``.
        selected (bool):
            Whether one facet bucket is selected. This
            field represents user's facet selection. It is
            set by frontend in SearchVideosRequest.
    """

    class Range(proto.Message):
        r"""The range of values [start, end) for which faceting is applied.

        Attributes:
            start (google.cloud.visionai_v1.types.FacetValue):
                Start of the range. Non-existence indicates
                some bound (e.g. -inf).
            end (google.cloud.visionai_v1.types.FacetValue):
                End of the range. Non-existence indicates
                some bound (e.g. inf).
        """

        start: "FacetValue" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="FacetValue",
        )
        end: "FacetValue" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="FacetValue",
        )

    value: "FacetValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="bucket_value",
        message="FacetValue",
    )
    range_: Range = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="bucket_value",
        message=Range,
    )
    selected: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class FacetGroup(proto.Message):
    r"""A group of facet buckets to be passed back and forth between
    backend & frontend.

    Attributes:
        facet_id (str):
            Unique id of the facet group.
        display_name (str):
            Display name of the facet. To be used by UI
            for facet rendering.
        buckets (MutableSequence[google.cloud.visionai_v1.types.FacetBucket]):
            Buckets associated with the facet. E.g. for
            "Team" facet, the bucket can be 49ers, patriots,
            etc.
        bucket_type (google.cloud.visionai_v1.types.FacetBucketType):
            Facet bucket type.
        fetch_matched_annotations (bool):
            If true, return query matched annotations for this facet
            group's selection. This option is only applicable for facets
            based on partition level annotations. It supports the
            following facet values:

            - INTEGER
            - STRING (DataSchema.SearchStrategy.EXACT_SEARCH only)
    """

    facet_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    buckets: MutableSequence["FacetBucket"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="FacetBucket",
    )
    bucket_type: "FacetBucketType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="FacetBucketType",
    )
    fetch_matched_annotations: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class IngestAssetRequest(proto.Message):
    r"""Request message for IngestAsset API.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        config (google.cloud.visionai_v1.types.IngestAssetRequest.Config):
            Provides information for the data and the asset resource
            name that the data belongs to. The first
            ``IngestAssetRequest`` message must only contain a
            ``Config`` message.

            This field is a member of `oneof`_ ``streaming_request``.
        time_indexed_data (google.cloud.visionai_v1.types.IngestAssetRequest.TimeIndexedData):
            Data to be ingested.

            This field is a member of `oneof`_ ``streaming_request``.
    """

    class Config(proto.Message):
        r"""Configuration for the data.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            video_type (google.cloud.visionai_v1.types.IngestAssetRequest.Config.VideoType):
                Type information for video data.

                This field is a member of `oneof`_ ``data_type``.
            asset (str):
                Required. The resource name of the asset that
                the ingested data belongs to.
        """

        class VideoType(proto.Message):
            r"""Type information for video data.

            Attributes:
                container_format (google.cloud.visionai_v1.types.IngestAssetRequest.Config.VideoType.ContainerFormat):
                    Container format of the video data.
            """

            class ContainerFormat(proto.Enum):
                r"""Container format of the video.

                Values:
                    CONTAINER_FORMAT_UNSPECIFIED (0):
                        The default type, not supposed to be used.
                    CONTAINER_FORMAT_MP4 (1):
                        Mp4 container format.
                """

                CONTAINER_FORMAT_UNSPECIFIED = 0
                CONTAINER_FORMAT_MP4 = 1

            container_format: "IngestAssetRequest.Config.VideoType.ContainerFormat" = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="IngestAssetRequest.Config.VideoType.ContainerFormat",
                )
            )

        video_type: "IngestAssetRequest.Config.VideoType" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="data_type",
            message="IngestAssetRequest.Config.VideoType",
        )
        asset: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class TimeIndexedData(proto.Message):
        r"""Contains the data and the corresponding time range this data
        is for.

        Attributes:
            data (bytes):
                Data to be ingested.
            temporal_partition (google.cloud.visionai_v1.types.Partition.TemporalPartition):
                Time range of the data.
        """

        data: bytes = proto.Field(
            proto.BYTES,
            number=1,
        )
        temporal_partition: "Partition.TemporalPartition" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Partition.TemporalPartition",
        )

    config: Config = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="streaming_request",
        message=Config,
    )
    time_indexed_data: TimeIndexedData = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="streaming_request",
        message=TimeIndexedData,
    )


class IngestAssetResponse(proto.Message):
    r"""Response message for IngestAsset API.

    Attributes:
        successfully_ingested_partition (google.cloud.visionai_v1.types.Partition.TemporalPartition):
            Time range of the data that has been
            successfully ingested.
    """

    successfully_ingested_partition: "Partition.TemporalPartition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Partition.TemporalPartition",
    )


class ClipAssetRequest(proto.Message):
    r"""Request message for ClipAsset API.

    Attributes:
        name (str):
            Required. The resource name of the asset to request clips
            for. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        temporal_partition (google.cloud.visionai_v1.types.Partition.TemporalPartition):
            Required. The time range to request clips
            for.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    temporal_partition: "Partition.TemporalPartition" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Partition.TemporalPartition",
    )


class ClipAssetResponse(proto.Message):
    r"""Response message for ClipAsset API.

    Attributes:
        time_indexed_uris (MutableSequence[google.cloud.visionai_v1.types.ClipAssetResponse.TimeIndexedUri]):
            A list of signed uris to download the video
            clips that cover the requested time range
            ordered by time.
    """

    class TimeIndexedUri(proto.Message):
        r"""Signed uri with corresponding time range.

        Attributes:
            temporal_partition (google.cloud.visionai_v1.types.Partition.TemporalPartition):
                Time range of the video that the uri is for.
            uri (str):
                Signed uri to download the video clip.
        """

        temporal_partition: "Partition.TemporalPartition" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Partition.TemporalPartition",
        )
        uri: str = proto.Field(
            proto.STRING,
            number=2,
        )

    time_indexed_uris: MutableSequence[TimeIndexedUri] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=TimeIndexedUri,
    )


class GenerateHlsUriRequest(proto.Message):
    r"""Request message for GenerateHlsUri API.

    Attributes:
        name (str):
            Required. The resource name of the asset to request clips
            for. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        temporal_partitions (MutableSequence[google.cloud.visionai_v1.types.Partition.TemporalPartition]):
            The time range to request clips for. Will be ignored if
            ``get_live_view`` is set to True. The total time range
            requested should be smaller than 24h.
        live_view_enabled (bool):
            Option to exclusively show a livestream of
            the asset with up to 3 minutes of backlog data.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    temporal_partitions: MutableSequence["Partition.TemporalPartition"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Partition.TemporalPartition",
        )
    )
    live_view_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GenerateHlsUriResponse(proto.Message):
    r"""Response message for GenerateHlsUri API.

    Attributes:
        uri (str):
            A signed uri to download the HLS manifest
            corresponding to the requested times.
        temporal_partitions (MutableSequence[google.cloud.visionai_v1.types.Partition.TemporalPartition]):
            A list of temporal partitions of the content
            returned in the order they appear in the stream.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    temporal_partitions: MutableSequence["Partition.TemporalPartition"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Partition.TemporalPartition",
        )
    )


class SearchAssetsRequest(proto.Message):
    r"""Request message for SearchAssets.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        schema_key_sorting_strategy (google.cloud.visionai_v1.types.SchemaKeySortingStrategy):
            Sort by the value under the data schema key.

            This field is a member of `oneof`_ ``sort_spec``.
        corpus (str):
            Required. The parent corpus to search. Format:
            ``projects/{project_id}/locations/{location_id}/corpora/{corpus_id}``
        page_size (int):
            The number of results to be returned in this page. If it's
            0, the server will decide the appropriate page_size.
        page_token (str):
            The continuation token to fetch the next
            page. If empty, it means it is fetching the
            first page.
        content_time_ranges (google.cloud.visionai_v1.types.DateTimeRangeArray):
            Time ranges that matching video content must fall within. If
            no ranges are provided, there will be no time restriction.
            This field is treated just like the criteria below, but
            defined separately for convenience as it is used frequently.
            Note that if the end_time is in the future, it will be
            clamped to the time the request was received.
        criteria (MutableSequence[google.cloud.visionai_v1.types.Criteria]):
            Criteria applied to search results.
        facet_selections (MutableSequence[google.cloud.visionai_v1.types.FacetGroup]):
            Stores most recent facet selection state.
            Only facet groups with user's selection will be
            presented here. Selection state is either
            selected or unselected. Only selected facet
            buckets will be used as search criteria.
        result_annotation_keys (MutableSequence[str]):
            A list of annotation keys to specify the annotations to be
            retrieved and returned with each search result. Annotation
            granularity must be GRANULARITY_ASSET_LEVEL and its search
            strategy must not be NO_SEARCH.
        search_query (str):
            Global search query. Allows user to search
            assets without needing to specify which field
            the value belongs to.
    """

    schema_key_sorting_strategy: "SchemaKeySortingStrategy" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="sort_spec",
        message="SchemaKeySortingStrategy",
    )
    corpus: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    content_time_ranges: "DateTimeRangeArray" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DateTimeRangeArray",
    )
    criteria: MutableSequence["Criteria"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Criteria",
    )
    facet_selections: MutableSequence["FacetGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="FacetGroup",
    )
    result_annotation_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    search_query: str = proto.Field(
        proto.STRING,
        number=10,
    )


class SearchIndexEndpointRequest(proto.Message):
    r"""Request message for SearchIndexEndpoint.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_query (google.cloud.visionai_v1.types.ImageQuery):
            An image-only query.

            This field is a member of `oneof`_ ``query``.
        text_query (str):
            A text-only query.

            This field is a member of `oneof`_ ``query``.
        index_endpoint (str):
            Required. The index endpoint to search. Format:
            ``projects/{project_id}/locations/{location_id}/indexEndpoints/{index_endpoint_id}``
        criteria (MutableSequence[google.cloud.visionai_v1.types.Criteria]):
            Criteria applied to search results.
        exclusion_criteria (MutableSequence[google.cloud.visionai_v1.types.Criteria]):
            Criteria to exclude from search results. Note that
            ``fetch_matched_annotations`` will be ignored.
        page_size (int):
            Requested page size. API may return fewer results than
            requested. If negative, INVALID_ARGUMENT error will be
            returned. If unspecified or 0, API will pick a default size,
            which is 10. If the requested page size is larger than the
            maximum size, API will pick the maximum size, which is 200.
        page_token (str):
            The continuation token to fetch the next
            page. If empty, it means it is fetching the
            first page.
    """

    image_query: "ImageQuery" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="query",
        message="ImageQuery",
    )
    text_query: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="query",
    )
    index_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    criteria: MutableSequence["Criteria"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Criteria",
    )
    exclusion_criteria: MutableSequence["Criteria"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="Criteria",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ImageQuery(proto.Message):
    r"""Image query for search endpoint request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        input_image (bytes):
            Input image in raw bytes.

            This field is a member of `oneof`_ ``image``.
        asset (str):
            Resource name of the asset. Only supported in IMAGE corpus
            type. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``

            This field is a member of `oneof`_ ``image``.
    """

    input_image: bytes = proto.Field(
        proto.BYTES,
        number=1,
        oneof="image",
    )
    asset: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="image",
    )


class SchemaKeySortingStrategy(proto.Message):
    r"""A strategy to specify how to sort by data schema key.

    Attributes:
        options (MutableSequence[google.cloud.visionai_v1.types.SchemaKeySortingStrategy.Option]):
            Options in the front have high priority than
            those in the back.
    """

    class Option(proto.Message):
        r"""Option for one data schema key.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            data_schema_key (str):
                The data used to sort.
            sort_decreasing (bool):
                Whether to sort in decreasing order or
                increasing order. By default, results are sorted
                in incresing order.
            aggregate_method (google.cloud.visionai_v1.types.SchemaKeySortingStrategy.Option.AggregateMethod):
                Aggregate method for the current data schema
                key.

                This field is a member of `oneof`_ ``_aggregate_method``.
        """

        class AggregateMethod(proto.Enum):
            r"""When one result has multiple values with the same key, specify which
            value is used to sort. By default, AGGREGATE_METHOD_LARGEST is used
            when results are sorted in decreasing order,
            AGGREGATE_METHOD_SMALLEST is used when results are sorted in
            incresing order.

            Values:
                AGGREGATE_METHOD_UNSPECIFIED (0):
                    The unspecified aggregate method will be
                    overwritten as mentioned above.
                AGGREGATE_METHOD_LARGEST (1):
                    Take the (lexicographical or numerical)
                    largest value to sort.
                AGGREGATE_METHOD_SMALLEST (2):
                    Take the (lexicographical or numerical)
                    smallest value to sort.
            """

            AGGREGATE_METHOD_UNSPECIFIED = 0
            AGGREGATE_METHOD_LARGEST = 1
            AGGREGATE_METHOD_SMALLEST = 2

        data_schema_key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sort_decreasing: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        aggregate_method: "SchemaKeySortingStrategy.Option.AggregateMethod" = (
            proto.Field(
                proto.ENUM,
                number=3,
                optional=True,
                enum="SchemaKeySortingStrategy.Option.AggregateMethod",
            )
        )

    options: MutableSequence[Option] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Option,
    )


class DeleteAssetMetadata(proto.Message):
    r"""The metadata for DeleteAsset API that embeds in
    [metadata][google.longrunning.Operation.metadata] field.

    """


class AnnotationMatchingResult(proto.Message):
    r"""Stores the criteria-annotation matching results for each
    search result item.

    Attributes:
        criteria (google.cloud.visionai_v1.types.Criteria):
            The criteria used for matching. It can be an
            input search criteria or a criteria converted
            from a facet selection.
        matched_annotations (MutableSequence[google.cloud.visionai_v1.types.Annotation]):
            Matched annotations for the criteria.
        status (google.rpc.status_pb2.Status):
            Status of the match result. Possible values:
            FAILED_PRECONDITION - the criteria is not eligible for
            match. OK - matching is performed.
    """

    criteria: "Criteria" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Criteria",
    )
    matched_annotations: MutableSequence["Annotation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Annotation",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )


class SearchResultItem(proto.Message):
    r"""Search result contains asset name and corresponding time
    ranges.

    Attributes:
        asset (str):
            The resource name of the asset. Format:
            ``projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}``
        segments (MutableSequence[google.cloud.visionai_v1.types.Partition.TemporalPartition]):
            The matched asset segments. Deprecated: please use singular
            ``segment`` field.
        segment (google.cloud.visionai_v1.types.Partition.TemporalPartition):
            The matched asset segment.
        relevance (float):
            Available to IMAGE corpus types. Relevance of this
            ``SearchResultItem`` to user search query (text query or
            image query). By default this represents cosine similarity
            between the query and the retrieved media content. The value
            is in the range of [-1, 1]. Note that search ranking is not
            only decided by this relevance score, but also other factors
            such as the match of annotations.
        requested_annotations (MutableSequence[google.cloud.visionai_v1.types.Annotation]):
            Search result annotations specified by
            result_annotation_keys in search request.
        annotation_matching_results (MutableSequence[google.cloud.visionai_v1.types.AnnotationMatchingResult]):
            Criteria or facet-selection based annotation matching
            results associated to this search result item. Only contains
            results for criteria or facet_selections with
            fetch_matched_annotations=true.
    """

    asset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    segments: MutableSequence["Partition.TemporalPartition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Partition.TemporalPartition",
    )
    segment: "Partition.TemporalPartition" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Partition.TemporalPartition",
    )
    relevance: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    requested_annotations: MutableSequence["Annotation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Annotation",
    )
    annotation_matching_results: MutableSequence["AnnotationMatchingResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="AnnotationMatchingResult",
        )
    )


class SearchAssetsResponse(proto.Message):
    r"""Response message for SearchAssets.

    Attributes:
        search_result_items (MutableSequence[google.cloud.visionai_v1.types.SearchResultItem]):
            Returned search results.
        next_page_token (str):
            The next-page continuation token.
        facet_results (MutableSequence[google.cloud.visionai_v1.types.FacetGroup]):
            Facet search results of a given query, which
            contains user's already-selected facet values
            and updated facet search results.
    """

    @property
    def raw_page(self):
        return self

    search_result_items: MutableSequence["SearchResultItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchResultItem",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    facet_results: MutableSequence["FacetGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="FacetGroup",
    )


class SearchIndexEndpointResponse(proto.Message):
    r"""Response message for SearchIndexEndpoint.

    Attributes:
        search_result_items (MutableSequence[google.cloud.visionai_v1.types.SearchResultItem]):
            Returned search results.
        next_page_token (str):
            The next-page continuation token.
            If this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    search_result_items: MutableSequence["SearchResultItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchResultItem",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IntRange(proto.Message):
    r"""Integer range type.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start (int):
            Start of the int range.

            This field is a member of `oneof`_ ``_start``.
        end (int):
            End of the int range.

            This field is a member of `oneof`_ ``_end``.
    """

    start: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    end: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class FloatRange(proto.Message):
    r"""Float range type.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start (float):
            Start of the float range.

            This field is a member of `oneof`_ ``_start``.
        end (float):
            End of the float range.

            This field is a member of `oneof`_ ``_end``.
    """

    start: float = proto.Field(
        proto.FLOAT,
        number=1,
        optional=True,
    )
    end: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )


class StringArray(proto.Message):
    r"""A list of string-type values.

    Attributes:
        txt_values (MutableSequence[str]):
            String type values.
    """

    txt_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class IntRangeArray(proto.Message):
    r"""A list of integer range values.

    Attributes:
        int_ranges (MutableSequence[google.cloud.visionai_v1.types.IntRange]):
            Int range values.
    """

    int_ranges: MutableSequence["IntRange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IntRange",
    )


class FloatRangeArray(proto.Message):
    r"""A list of float range values.

    Attributes:
        float_ranges (MutableSequence[google.cloud.visionai_v1.types.FloatRange]):
            Float range values.
    """

    float_ranges: MutableSequence["FloatRange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FloatRange",
    )


class DateTimeRange(proto.Message):
    r"""Datetime range type.

    Attributes:
        start (google.type.datetime_pb2.DateTime):
            Start date time.
        end (google.type.datetime_pb2.DateTime):
            End data time.
    """

    start: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=datetime_pb2.DateTime,
    )
    end: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=datetime_pb2.DateTime,
    )


class DateTimeRangeArray(proto.Message):
    r"""A list of datetime range values.

    Attributes:
        date_time_ranges (MutableSequence[google.cloud.visionai_v1.types.DateTimeRange]):
            Date time ranges.
    """

    date_time_ranges: MutableSequence["DateTimeRange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DateTimeRange",
    )


class CircleArea(proto.Message):
    r"""Representation of a circle area.

    Attributes:
        latitude (float):
            Latitude of circle area's center. Degrees [-90 .. 90]
        longitude (float):
            Longitude of circle area's center. Degrees [-180 .. 180]
        radius_meter (float):
            Radius of the circle area in meters.
    """

    latitude: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    longitude: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    radius_meter: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class GeoLocationArray(proto.Message):
    r"""A list of locations.

    Attributes:
        circle_areas (MutableSequence[google.cloud.visionai_v1.types.CircleArea]):
            A list of circle areas.
    """

    circle_areas: MutableSequence["CircleArea"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CircleArea",
    )


class BoolValue(proto.Message):
    r"""

    Attributes:
        value (bool):

    """

    value: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class Criteria(proto.Message):
    r"""Filter criteria applied to current search results.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_array (google.cloud.visionai_v1.types.StringArray):
            The text values associated with the field.

            This field is a member of `oneof`_ ``value``.
        int_range_array (google.cloud.visionai_v1.types.IntRangeArray):
            The integer ranges associated with the field.

            This field is a member of `oneof`_ ``value``.
        float_range_array (google.cloud.visionai_v1.types.FloatRangeArray):
            The float ranges associated with the field.

            This field is a member of `oneof`_ ``value``.
        date_time_range_array (google.cloud.visionai_v1.types.DateTimeRangeArray):
            The datetime ranges associated with the
            field.

            This field is a member of `oneof`_ ``value``.
        geo_location_array (google.cloud.visionai_v1.types.GeoLocationArray):
            Geo Location array.

            This field is a member of `oneof`_ ``value``.
        bool_value (google.cloud.visionai_v1.types.BoolValue):
            A Boolean value.

            This field is a member of `oneof`_ ``value``.
        field (str):
            The UGA field or ML field to apply filtering
            criteria.
        fetch_matched_annotations (bool):
            If true, return query matched annotations for this criteria.
            This option is only applicable for inclusion criteria, i.e.,
            not exclusion criteria, with partition level annotations. It
            supports the following data types:

            - INTEGER
            - FLOAT
            - STRING (DataSchema.SearchStrategy.EXACT_SEARCH only)
            - BOOLEAN
    """

    text_array: "StringArray" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="value",
        message="StringArray",
    )
    int_range_array: "IntRangeArray" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value",
        message="IntRangeArray",
    )
    float_range_array: "FloatRangeArray" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="value",
        message="FloatRangeArray",
    )
    date_time_range_array: "DateTimeRangeArray" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value",
        message="DateTimeRangeArray",
    )
    geo_location_array: "GeoLocationArray" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message="GeoLocationArray",
    )
    bool_value: "BoolValue" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value",
        message="BoolValue",
    )
    field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fetch_matched_annotations: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class Partition(proto.Message):
    r"""Partition to specify the partition in time and space for
    sub-asset level annotation.

    Attributes:
        temporal_partition (google.cloud.visionai_v1.types.Partition.TemporalPartition):
            Partition of asset in time.
        spatial_partition (google.cloud.visionai_v1.types.Partition.SpatialPartition):
            Partition of asset in space.
        relative_temporal_partition (google.cloud.visionai_v1.types.Partition.RelativeTemporalPartition):
            Partition of asset in time.
    """

    class TemporalPartition(proto.Message):
        r"""Partition of asset in UTC Epoch time. Supported by STREAM_VIDEO
        corpus type.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start time of the partition.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                End time of the partition.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class SpatialPartition(proto.Message):
        r"""Partition of asset in space.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            x_min (int):
                The minimum x coordinate value.

                This field is a member of `oneof`_ ``_x_min``.
            y_min (int):
                The minimum y coordinate value.

                This field is a member of `oneof`_ ``_y_min``.
            x_max (int):
                The maximum x coordinate value.

                This field is a member of `oneof`_ ``_x_max``.
            y_max (int):
                The maximum y coordinate value.

                This field is a member of `oneof`_ ``_y_max``.
        """

        x_min: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        y_min: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        x_max: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )
        y_max: int = proto.Field(
            proto.INT64,
            number=4,
            optional=True,
        )

    class RelativeTemporalPartition(proto.Message):
        r"""Partition of asset in relative time. Supported by VIDEO_ON_DEMAND
        corpus type.

        Attributes:
            start_offset (google.protobuf.duration_pb2.Duration):
                Start time offset of the partition.
            end_offset (google.protobuf.duration_pb2.Duration):
                End time offset of the partition.
        """

        start_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        end_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    temporal_partition: TemporalPartition = proto.Field(
        proto.MESSAGE,
        number=1,
        message=TemporalPartition,
    )
    spatial_partition: SpatialPartition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=SpatialPartition,
    )
    relative_temporal_partition: RelativeTemporalPartition = proto.Field(
        proto.MESSAGE,
        number=3,
        message=RelativeTemporalPartition,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
