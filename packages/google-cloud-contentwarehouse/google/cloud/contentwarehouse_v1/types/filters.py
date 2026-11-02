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

import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "DocumentQuery",
        "TimeFilter",
        "PropertyFilter",
        "FileTypeFilter",
        "CustomWeightsMetadata",
        "WeightedSchemaProperty",
    },
)


class DocumentQuery(proto.Message):
    r"""

    Attributes:
        query (str):
            The query string that matches against the full text of the
            document and the searchable properties.

            The query partially supports `Google AIP style
            syntax <https://google.aip.dev/160>`__. Specifically, the
            query supports literals, logical operators, negation
            operators, comparison operators, and functions.

            Literals: A bare literal value (examples: "42", "Hugo") is a
            value to be matched against. It searches over the full text
            of the document and the searchable properties.

            Logical operators: "AND", "and", "OR", and "or" are binary
            logical operators (example: "engineer OR developer").

            Negation operators: "NOT" and "!" are negation operators
            (example: "NOT software").

            Comparison operators: support the binary comparison
            operators =, !=, <, >, <= and >= for string, numeric, enum,
            boolean. Also support like operator ``~~`` for string. It
            provides semantic search functionality by parsing, stemming
            and doing synonyms expansion against the input query.

            To specify a property in the query, the left hand side
            expression in the comparison must be the property ID
            including the parent. The right hand side must be literals.
            For example: ""projects/123/locations/us".property_a < 1"
            matches results whose "property_a" is less than 1 in project
            123 and us location. The literals and comparison expression
            can be connected in a single query (example: "software
            engineer "projects/123/locations/us".salary > 100").

            Functions: supported functions are
            ``LOWER([property_name])`` to perform a case insensitive
            match and ``EMPTY([property_name])`` to filter on the
            existence of a key.

            Support nested expressions connected using parenthesis and
            logical operators. The default logical operators is ``AND``
            if there is no operators between expressions.

            The query can be used with other filters e.g.
            ``time_filters`` and ``folder_name_filter``. They are
            connected with ``AND`` operator under the hood.

            The maximum number of allowed characters is 255.
        is_nl_query (bool):
            Experimental, do not use. If the query is a natural language
            question. False by default. If true, then the
            question-answering feature will be used instead of search,
            and ``result_count`` in
            [SearchDocumentsRequest][google.cloud.contentwarehouse.v1.SearchDocumentsRequest]
            must be set. In addition, all other input fields related to
            search (pagination, histograms, etc.) will be ignored.
        custom_property_filter (str):
            This filter specifies a structured syntax to match against
            the [PropertyDefinition].[is_filterable][] marked as
            ``true``. The syntax for this expression is a subset of SQL
            syntax.

            Supported operators are: ``=``, ``!=``, ``<``, ``<=``,
            ``>``, and ``>=`` where the left of the operator is a
            property name and the right of the operator is a number or a
            quoted string. You must escape backslash (\\) and quote (")
            characters. Supported functions are
            ``LOWER([property_name])`` to perform a case insensitive
            match and ``EMPTY([property_name])`` to filter on the
            existence of a key.

            Boolean expressions (AND/OR/NOT) are supported up to 3
            levels of nesting (for example, "((A AND B AND C) OR NOT D)
            AND E"), a maximum of 100 comparisons or functions are
            allowed in the expression. The expression must be < 6000
            bytes in length.

            Sample Query:
            ``(LOWER(driving_license)="class \"a\"" OR EMPTY(driving_license)) AND driving_years > 10``
        time_filters (MutableSequence[google.cloud.contentwarehouse_v1.types.TimeFilter]):
            Documents created/updated within a range
            specified by this filter are searched against.
        document_schema_names (MutableSequence[str]):
            This filter specifies the exact document schema
            [Document.document_schema_name][google.cloud.contentwarehouse.v1.Document.document_schema_name]
            of the documents to search against.

            If a value isn't specified, documents within the search
            results are associated with any schema. If multiple values
            are specified, documents within the search results may be
            associated with any of the specified schemas.

            At most 20 document schema names are allowed.
        property_filter (MutableSequence[google.cloud.contentwarehouse_v1.types.PropertyFilter]):
            This filter specifies a structured syntax to match against
            the
            [PropertyDefinition.is_filterable][google.cloud.contentwarehouse.v1.PropertyDefinition.is_filterable]
            marked as ``true``. The relationship between the
            PropertyFilters is OR.
        file_type_filter (google.cloud.contentwarehouse_v1.types.FileTypeFilter):
            This filter specifies the types of files to
            return: ALL, FOLDER, or FILE. If FOLDER or FILE
            is specified, then only either folders or files
            will be returned, respectively. If ALL is
            specified, both folders and files will be
            returned.

            If no value is specified, ALL files will be
            returned.
        folder_name_filter (str):
            Search all the documents under this specified folder.
            Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.
        document_name_filter (MutableSequence[str]):
            Search the documents in the list. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.
        query_context (MutableSequence[str]):
            For custom synonyms.
            Customers provide the synonyms based on context.
            One customer can provide multiple set of
            synonyms based on different context. The search
            query will be expanded based on the custom
            synonyms of the query context set. By default,
            no custom synonyms wll be applied if no query
            context is provided.
            It is not supported for CMEK compliant
            deployment.
        document_creator_filter (MutableSequence[str]):
            The exact creator(s) of the documents to
            search against.
            If a value isn't specified, documents within the
            search results are associated with any creator.
            If multiple values are specified, documents
            within the search results may be associated with
            any of the specified creators.
        custom_weights_metadata (google.cloud.contentwarehouse_v1.types.CustomWeightsMetadata):
            To support the custom weighting across
            document schemas, customers need to provide the
            properties to be used to boost the ranking in
            the search request. For a search query with
            CustomWeightsMetadata specified, only the
            RetrievalImportance for the properties in the
            CustomWeightsMetadata will be honored.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_nl_query: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    custom_property_filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    time_filters: MutableSequence["TimeFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="TimeFilter",
    )
    document_schema_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    property_filter: MutableSequence["PropertyFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="PropertyFilter",
    )
    file_type_filter: "FileTypeFilter" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="FileTypeFilter",
    )
    folder_name_filter: str = proto.Field(
        proto.STRING,
        number=9,
    )
    document_name_filter: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    query_context: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    document_creator_filter: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    custom_weights_metadata: "CustomWeightsMetadata" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="CustomWeightsMetadata",
    )


class TimeFilter(proto.Message):
    r"""Filter on create timestamp or update timestamp of documents.

    Attributes:
        time_range (google.type.interval_pb2.Interval):

        time_field (google.cloud.contentwarehouse_v1.types.TimeFilter.TimeField):
            Specifies which time field to filter documents on.

            Defaults to [TimeField.UPLOAD_TIME][].
    """

    class TimeField(proto.Enum):
        r"""Time field used in TimeFilter.

        Values:
            TIME_FIELD_UNSPECIFIED (0):
                Default value.
            CREATE_TIME (1):
                Earliest document create time.
            UPDATE_TIME (2):
                Latest document update time.
            DISPOSITION_TIME (3):
                Time when document becomes mutable again.
        """

        TIME_FIELD_UNSPECIFIED = 0
        CREATE_TIME = 1
        UPDATE_TIME = 2
        DISPOSITION_TIME = 3

    time_range: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=interval_pb2.Interval,
    )
    time_field: TimeField = proto.Field(
        proto.ENUM,
        number=2,
        enum=TimeField,
    )


class PropertyFilter(proto.Message):
    r"""

    Attributes:
        document_schema_name (str):
            The Document schema name
            [Document.document_schema_name][google.cloud.contentwarehouse.v1.Document.document_schema_name].
            Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.
        condition (str):
            The filter condition. The syntax for this expression is a
            subset of SQL syntax.

            Supported operators are: ``=``, ``!=``, ``<``, ``<=``,
            ``>``, ``>=``, and ``~~`` where the left of the operator is
            a property name and the right of the operator is a number or
            a quoted string. You must escape backslash (\\) and quote
            (") characters.

            ``~~`` is the LIKE operator. The right of the operator must
            be a string. The only supported property data type for LIKE
            is text_values. It provides semantic search functionality by
            parsing, stemming and doing synonyms expansion against the
            input query. It matches if the property contains semantic
            similar content to the query. It is not regex matching or
            wildcard matching. For example, "property.company ~~
            "google"" will match records whose property
            ``property.compnay`` have values like "Google Inc.", "Google
            LLC" or "Google Company".

            Supported functions are ``LOWER([property_name])`` to
            perform a case insensitive match and
            ``EMPTY([property_name])`` to filter on the existence of a
            key.

            Boolean expressions (AND/OR/NOT) are supported up to 3
            levels of nesting (for example, "((A AND B AND C) OR NOT D)
            AND E"), a maximum of 100 comparisons or functions are
            allowed in the expression. The expression must be < 6000
            bytes in length.

            Only properties that are marked filterable are allowed
            ([PropertyDefinition.is_filterable][google.cloud.contentwarehouse.v1.PropertyDefinition.is_filterable]).
            Property names do not need to be prefixed by the document
            schema id (as is the case with histograms), however property
            names will need to be prefixed by its parent hierarchy, if
            any. For example: top_property_name.sub_property_name.

            Sample Query:
            ``(LOWER(driving_license)="class \"a\"" OR EMPTY(driving_license)) AND driving_years > 10``

            CMEK compliant deployment only supports:

            - Operators: ``=``, ``<``, ``<=``, ``>``, and ``>=``.
            - Boolean expressions: AND and OR.
    """

    document_schema_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FileTypeFilter(proto.Message):
    r"""Filter for the specific types of documents returned.

    Attributes:
        file_type (google.cloud.contentwarehouse_v1.types.FileTypeFilter.FileType):
            The type of files to return.
    """

    class FileType(proto.Enum):
        r"""Representation of the types of files.

        Values:
            FILE_TYPE_UNSPECIFIED (0):
                Default document type. If set, disables the
                filter.
            ALL (1):
                Returns all document types, including
                folders.
            FOLDER (2):
                Returns only folders.
            DOCUMENT (3):
                Returns only non-folder documents.
            ROOT_FOLDER (4):
                Returns only root folders
        """

        FILE_TYPE_UNSPECIFIED = 0
        ALL = 1
        FOLDER = 2
        DOCUMENT = 3
        ROOT_FOLDER = 4

    file_type: FileType = proto.Field(
        proto.ENUM,
        number=1,
        enum=FileType,
    )


class CustomWeightsMetadata(proto.Message):
    r"""To support the custom weighting across document schemas.

    Attributes:
        weighted_schema_properties (MutableSequence[google.cloud.contentwarehouse_v1.types.WeightedSchemaProperty]):
            List of schema and property name. Allows a
            maximum of 10 schemas to be specified for
            relevance boosting.
    """

    weighted_schema_properties: MutableSequence["WeightedSchemaProperty"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="WeightedSchemaProperty",
        )
    )


class WeightedSchemaProperty(proto.Message):
    r"""Specifies the schema property name.

    Attributes:
        document_schema_name (str):
            The document schema name.
        property_names (MutableSequence[str]):
            The property definition names in the schema.
    """

    document_schema_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    property_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
