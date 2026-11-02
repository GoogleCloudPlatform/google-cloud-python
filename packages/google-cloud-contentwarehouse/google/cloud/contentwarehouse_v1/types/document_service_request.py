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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.contentwarehouse_v1.types import common, filters, histogram
from google.cloud.contentwarehouse_v1.types import document as gcc_document

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "CloudAIDocumentOption",
        "CreateDocumentRequest",
        "GetDocumentRequest",
        "UpdateDocumentRequest",
        "DeleteDocumentRequest",
        "SearchDocumentsRequest",
        "LockDocumentRequest",
        "FetchAclRequest",
        "SetAclRequest",
    },
)


class CloudAIDocumentOption(proto.Message):
    r"""Request Option for processing Cloud AI Document in CW
    Document.

    Attributes:
        enable_entities_conversions (bool):
            Whether to convert all the entities to
            properties.
        customized_entities_properties_conversions (MutableMapping[str, str]):
            If set, only selected entities will be
            converted to properties.
    """

    enable_entities_conversions: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    customized_entities_properties_conversions: MutableMapping[str, str] = (
        proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
    )


class CreateDocumentRequest(proto.Message):
    r"""Request message for DocumentService.CreateDocument.

    Attributes:
        parent (str):
            Required. The parent name. Format:
            projects/{project_number}/locations/{location}.
        document (google.cloud.contentwarehouse_v1.types.Document):
            Required. The document to create.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
        policy (google.iam.v1.policy_pb2.Policy):
            Default document policy during creation.
            This refers to an Identity and Access (IAM)
            policy, which specifies access controls for the
            Document.
            Conditions defined in the policy will be
            ignored.
        cloud_ai_document_option (google.cloud.contentwarehouse_v1.types.CloudAIDocumentOption):
            Request Option for processing Cloud AI
            Document in Document Warehouse. This field
            offers limited support for mapping entities from
            Cloud AI Document to Warehouse Document. Please
            consult with product team before using this
            field and other available options.
        create_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask for creating Document fields. If mask path is
            empty, it means all fields are masked. For the ``FieldMask``
            definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document: gcc_document.Document = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_document.Document,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.RequestMetadata,
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=4,
        message=policy_pb2.Policy,
    )
    cloud_ai_document_option: "CloudAIDocumentOption" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CloudAIDocumentOption",
    )
    create_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=6,
        message=field_mask_pb2.FieldMask,
    )


class GetDocumentRequest(proto.Message):
    r"""Request message for DocumentService.GetDocument.

    Attributes:
        name (str):
            Required. The name of the document to retrieve. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}
            or
            projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.RequestMetadata,
    )


class UpdateDocumentRequest(proto.Message):
    r"""Request message for DocumentService.UpdateDocument.

    Attributes:
        name (str):
            Required. The name of the document to update. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}
            or
            projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.
        document (google.cloud.contentwarehouse_v1.types.Document):
            Required. The document to update.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
        cloud_ai_document_option (google.cloud.contentwarehouse_v1.types.CloudAIDocumentOption):
            Request Option for processing Cloud AI
            Document in Document Warehouse. This field
            offers limited support for mapping entities from
            Cloud AI Document to Warehouse Document. Please
            consult with product team before using this
            field and other available options.
        update_options (google.cloud.contentwarehouse_v1.types.UpdateOptions):
            Options for the update operation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document: gcc_document.Document = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_document.Document,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.RequestMetadata,
    )
    cloud_ai_document_option: "CloudAIDocumentOption" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CloudAIDocumentOption",
    )
    update_options: common.UpdateOptions = proto.Field(
        proto.MESSAGE,
        number=6,
        message=common.UpdateOptions,
    )


class DeleteDocumentRequest(proto.Message):
    r"""Request message for DocumentService.DeleteDocument.

    Attributes:
        name (str):
            Required. The name of the document to delete. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}
            or
            projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.RequestMetadata,
    )


class SearchDocumentsRequest(proto.Message):
    r"""Request message for DocumentService.SearchDocuments.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            documents. Format:
            projects/{project_number}/locations/{location}.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control and improve
            the search quality of the service.
        document_query (google.cloud.contentwarehouse_v1.types.DocumentQuery):
            Query used to search against documents
            (keyword, filters, etc.).
        offset (int):
            An integer that specifies the current offset (that is,
            starting result location, amongst the documents deemed by
            the API as relevant) in search results. This field is only
            considered if
            [page_token][google.cloud.contentwarehouse.v1.SearchDocumentsRequest.page_token]
            is unset.

            The maximum allowed value is 5000. Otherwise an error is
            thrown.

            For example, 0 means to return results starting from the
            first matching document, and 10 means to return from the
            11th document. This can be used for pagination, (for
            example, pageSize = 10 and offset = 10 means to return from
            the second page).
        page_size (int):
            A limit on the number of documents returned
            in the search results. Increasing this value
            above the default value of 10 can increase
            search response time. The value can be between 1
            and 100.
        page_token (str):
            The token specifying the current offset within search
            results. See
            [SearchDocumentsResponse.next_page_token][google.cloud.contentwarehouse.v1.SearchDocumentsResponse.next_page_token]
            for an explanation of how to obtain the next set of query
            results.
        order_by (str):
            The criteria determining how search results are sorted. For
            non-empty query, default is ``"relevance desc"``. For empty
            query, default is ``"upload_date desc"``.

            Supported options are:

            - ``"relevance desc"``: By relevance descending, as
              determined by the API algorithms.
            - ``"upload_date desc"``: By upload date descending.
            - ``"upload_date"``: By upload date ascending.
            - ``"update_date desc"``: By last updated date descending.
            - ``"update_date"``: By last updated date ascending.
            - ``"retrieval_importance desc"``: By retrieval importance
              of properties descending. This feature is still under
              development, please do not use unless otherwise instructed
              to do so.
        histogram_queries (MutableSequence[google.cloud.contentwarehouse_v1.types.HistogramQuery]):
            An expression specifying a histogram request against
            matching documents. Expression syntax is an aggregation
            function call with histogram facets and other options.

            The following aggregation functions are supported:

            - ``count(string_histogram_facet)``: Count the number of
              matching entities for each distinct attribute value.

            Data types:

            - Histogram facet (aka filterable properties): Facet names
              with format <schema id>.<facet>. Facets will have the
              format of: ``[a-zA-Z][a-zA-Z0-9_:/-.]``. If the facet is a
              child facet, then the parent hierarchy needs to be
              specified separated by dots in the prefix after the schema
              id. Thus, the format for a multi- level facet is: <schema
              id>.<parent facet name>. <child facet name>. Example:
              schema123.root_parent_facet.middle_facet.child_facet
            - DocumentSchemaId: (with no schema id prefix) to get
              histograms for each document type (returns the schema id
              path, e.g.
              projects/12345/locations/us-west/documentSchemas/abc123).

            Example expression:

            - Document type counts: count('DocumentSchemaId')

            - For schema id, abc123, get the counts for MORTGAGE_TYPE:
              count('abc123.MORTGAGE_TYPE')
        require_total_size (bool):
            Controls if the search document request requires the return
            of a total size of matched documents. See
            [SearchDocumentsResponse.total_size][google.cloud.contentwarehouse.v1.SearchDocumentsResponse.total_size].

            Enabling this flag may adversely impact performance. Hint:
            If this is used with pagination, set this flag on the
            initial query but set this to false on subsequent page calls
            (keep the total count locally).

            Defaults to false.
        total_result_size (google.cloud.contentwarehouse_v1.types.SearchDocumentsRequest.TotalResultSize):
            Controls if the search document request requires the return
            of a total size of matched documents. See
            [SearchDocumentsResponse.total_size][google.cloud.contentwarehouse.v1.SearchDocumentsResponse.total_size].
        qa_size_limit (int):
            Experimental, do not use. The limit on the number of
            documents returned for the question-answering feature. To
            enable the question-answering feature, set
            [DocumentQuery].[is_nl_query][] to true.
    """

    class TotalResultSize(proto.Enum):
        r"""The total number of matching documents.

        Values:
            TOTAL_RESULT_SIZE_UNSPECIFIED (0):
                Total number calculation will be skipped.
            ESTIMATED_SIZE (1):
                Estimate total number. The total result size
                will be accurated up to 10,000. This option will
                add cost and latency to your request.
            ACTUAL_SIZE (2):
                It may adversely impact performance. The
                limit is 1000,000.
        """

        TOTAL_RESULT_SIZE_UNSPECIFIED = 0
        ESTIMATED_SIZE = 1
        ACTUAL_SIZE = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.RequestMetadata,
    )
    document_query: filters.DocumentQuery = proto.Field(
        proto.MESSAGE,
        number=4,
        message=filters.DocumentQuery,
    )
    offset: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=8,
    )
    histogram_queries: MutableSequence[histogram.HistogramQuery] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=histogram.HistogramQuery,
    )
    require_total_size: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    total_result_size: TotalResultSize = proto.Field(
        proto.ENUM,
        number=12,
        enum=TotalResultSize,
    )
    qa_size_limit: int = proto.Field(
        proto.INT32,
        number=11,
    )


class LockDocumentRequest(proto.Message):
    r"""Request message for DocumentService.LockDocument.

    Attributes:
        name (str):
            Required. The name of the document to lock. Format:
            projects/{project_number}/locations/{location}/documents/{document}.
        collection_id (str):
            The collection the document connects to.
        locking_user (google.cloud.contentwarehouse_v1.types.UserInfo):
            The user information who locks the document.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    collection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    locking_user: common.UserInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.UserInfo,
    )


class FetchAclRequest(proto.Message):
    r"""Request message for DocumentService.FetchAcl

    Attributes:
        resource (str):
            Required. REQUIRED: The resource for which the policy is
            being requested. Format for document:
            projects/{project_number}/locations/{location}/documents/{document_id}.
            Format for collection:
            projects/{project_number}/locations/{location}/collections/{collection_id}.
            Format for project: projects/{project_number}.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
        project_owner (bool):
            For Get Project ACL only. Authorization check for end user
            will be ignored when project_owner=true.
    """

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.RequestMetadata,
    )
    project_owner: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class SetAclRequest(proto.Message):
    r"""Request message for DocumentService.SetAcl.

    Attributes:
        resource (str):
            Required. REQUIRED: The resource for which the policy is
            being requested. Format for document:
            projects/{project_number}/locations/{location}/documents/{document_id}.
            Format for collection:
            projects/{project_number}/locations/{location}/collections/{collection_id}.
            Format for project: projects/{project_number}.
        policy (google.iam.v1.policy_pb2.Policy):
            Required. REQUIRED: The complete policy to be applied to the
            ``resource``. The size of the policy is limited to a few 10s
            of KB. This refers to an Identity and Access (IAM) policy,
            which specifies access controls for the Document.

            You can set ACL with condition for projects only.

            Supported operators are: ``=``, ``!=``, ``<``, ``<=``,
            ``>``, and ``>=`` where the left of the operator is
            ``DocumentSchemaId`` or property name and the right of the
            operator is a number or a quoted string. You must escape
            backslash (\\) and quote (") characters.

            Boolean expressions (AND/OR) are supported up to 3 levels of
            nesting (for example, "((A AND B AND C) OR D) AND E"), a
            maximum of 10 comparisons are allowed in the expression. The
            expression must be < 6000 bytes in length.

            Sample condition:
            ``"DocumentSchemaId = \"some schema id\" OR SchemaId.floatPropertyName >= 10"``
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
        project_owner (bool):
            For Set Project ACL only. Authorization check for end user
            will be ignored when project_owner=true.
    """

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=2,
        message=policy_pb2.Policy,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.RequestMetadata,
    )
    project_owner: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
