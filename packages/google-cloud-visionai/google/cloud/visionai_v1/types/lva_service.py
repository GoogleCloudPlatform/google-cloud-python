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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.visionai_v1.types import lva_resources

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "Registry",
        "ListOperatorsRequest",
        "ListOperatorsResponse",
        "GetOperatorRequest",
        "CreateOperatorRequest",
        "UpdateOperatorRequest",
        "DeleteOperatorRequest",
        "ListAnalysesRequest",
        "ListAnalysesResponse",
        "GetAnalysisRequest",
        "CreateAnalysisRequest",
        "UpdateAnalysisRequest",
        "DeleteAnalysisRequest",
        "ListProcessesRequest",
        "ListProcessesResponse",
        "GetProcessRequest",
        "CreateProcessRequest",
        "UpdateProcessRequest",
        "DeleteProcessRequest",
        "BatchRunProcessRequest",
        "BatchRunProcessResponse",
        "ResolveOperatorInfoRequest",
        "OperatorQuery",
        "ResolveOperatorInfoResponse",
        "ListPublicOperatorsRequest",
        "ListPublicOperatorsResponse",
    },
)


class Registry(proto.Enum):
    r"""The enum of the types of the Registry.

    Values:
        REGISTRY_UNSPECIFIED (0):
            Registry is unspecified.
        PUBLIC (1):
            Public Registry containing the public
            Operators released by Google.
        PRIVATE (2):
            Private Registry containing the local
            registered operators.
    """

    REGISTRY_UNSPECIFIED = 0
    PUBLIC = 1
    PRIVATE = 2


class ListOperatorsRequest(proto.Message):
    r"""Message for requesting list of Operators.

    Attributes:
        parent (str):
            Required. Parent value for
            ListOperatorsRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Hint for how to order the results.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListOperatorsResponse(proto.Message):
    r"""Message for response to listing Operators.

    Attributes:
        operators (MutableSequence[google.cloud.visionai_v1.types.Operator]):
            The list of Operator
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    operators: MutableSequence[lva_resources.Operator] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=lva_resources.Operator,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOperatorRequest(proto.Message):
    r"""Message for getting a Operator.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOperatorRequest(proto.Message):
    r"""Message for creating a Operator.

    Attributes:
        parent (str):
            Required. Value for parent.
        operator_id (str):
            Required. Id of the requesting object.
        operator (google.cloud.visionai_v1.types.Operator):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operator_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operator: lva_resources.Operator = proto.Field(
        proto.MESSAGE,
        number=3,
        message=lva_resources.Operator,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateOperatorRequest(proto.Message):
    r"""Message for updating a Operator.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Operator resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        operator (google.cloud.visionai_v1.types.Operator):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    operator: lva_resources.Operator = proto.Field(
        proto.MESSAGE,
        number=2,
        message=lva_resources.Operator,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteOperatorRequest(proto.Message):
    r"""Message for deleting a Operator

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAnalysesRequest(proto.Message):
    r"""Message for requesting list of Analyses

    Attributes:
        parent (str):
            Required. Parent value for
            ListAnalysesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListAnalysesResponse(proto.Message):
    r"""Message for response to listing Analyses

    Attributes:
        analyses (MutableSequence[google.cloud.visionai_v1.types.Analysis]):
            The list of Analysis
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    analyses: MutableSequence[lva_resources.Analysis] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=lva_resources.Analysis,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAnalysisRequest(proto.Message):
    r"""Message for getting an Analysis.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAnalysisRequest(proto.Message):
    r"""Message for creating an Analysis.

    Attributes:
        parent (str):
            Required. Value for parent.
        analysis_id (str):
            Required. Id of the requesting object.
        analysis (google.cloud.visionai_v1.types.Analysis):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    analysis_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    analysis: lva_resources.Analysis = proto.Field(
        proto.MESSAGE,
        number=3,
        message=lva_resources.Analysis,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateAnalysisRequest(proto.Message):
    r"""Message for updating an Analysis.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Analysis resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        analysis (google.cloud.visionai_v1.types.Analysis):
            Required. The resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    analysis: lva_resources.Analysis = proto.Field(
        proto.MESSAGE,
        number=2,
        message=lva_resources.Analysis,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAnalysisRequest(proto.Message):
    r"""Message for deleting an Analysis.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListProcessesRequest(proto.Message):
    r"""Message for requesting list of Processes.

    Attributes:
        parent (str):
            Required. Parent value for
            ListProcessesRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListProcessesResponse(proto.Message):
    r"""Message for response to listing Processes.

    Attributes:
        processes (MutableSequence[google.cloud.visionai_v1.types.Process]):
            The list of Processes.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    processes: MutableSequence[lva_resources.Process] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=lva_resources.Process,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetProcessRequest(proto.Message):
    r"""Message for getting a Process.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateProcessRequest(proto.Message):
    r"""Message for creating a Process.

    Attributes:
        parent (str):
            Required. Value for parent.
        process_id (str):
            Required. Id of the requesting object.
        process (google.cloud.visionai_v1.types.Process):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    process_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    process: lva_resources.Process = proto.Field(
        proto.MESSAGE,
        number=3,
        message=lva_resources.Process,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateProcessRequest(proto.Message):
    r"""Message for updating a Process.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Process resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        process (google.cloud.visionai_v1.types.Process):
            Required. The resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    process: lva_resources.Process = proto.Field(
        proto.MESSAGE,
        number=2,
        message=lva_resources.Process,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteProcessRequest(proto.Message):
    r"""Message for deleting a Process.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchRunProcessRequest(proto.Message):
    r"""Request message for running the processes in a batch.

    Attributes:
        parent (str):
            Required. The parent resource shared by all
            processes being created.
        requests (MutableSequence[google.cloud.visionai_v1.types.CreateProcessRequest]):
            Required. The create process requests.
        options (google.cloud.visionai_v1.types.BatchRunProcessRequest.BatchRunProcessOptions):
            Optional. Options for batch processes.
        batch_id (str):
            Output only. The batch ID.
    """

    class BatchRunProcessOptions(proto.Message):
        r"""Options for batch processes.

        Attributes:
            retry_count (int):
                The retry counts per process. Default: 3.
            batch_size (int):
                The batch size. Default: 5, maximum: 100.
        """

        retry_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        batch_size: int = proto.Field(
            proto.INT32,
            number=2,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateProcessRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateProcessRequest",
    )
    options: BatchRunProcessOptions = proto.Field(
        proto.MESSAGE,
        number=3,
        message=BatchRunProcessOptions,
    )
    batch_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class BatchRunProcessResponse(proto.Message):
    r"""Response message for running the processes in a batch.

    Attributes:
        batch_id (str):
            The batch ID.
        processes (MutableSequence[google.cloud.visionai_v1.types.Process]):
            Processes created.
    """

    batch_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    processes: MutableSequence[lva_resources.Process] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=lva_resources.Process,
    )


class ResolveOperatorInfoRequest(proto.Message):
    r"""Request message for querying operator info.

    Attributes:
        parent (str):
            Required. Parent value for
            ResolveOperatorInfoRequest.
        queries (MutableSequence[google.cloud.visionai_v1.types.OperatorQuery]):
            Required. The operator queries.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    queries: MutableSequence["OperatorQuery"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OperatorQuery",
    )


class OperatorQuery(proto.Message):
    r"""OperatorQuery represents one query to a Operator.

    Attributes:
        operator (str):
            Required. The canonical Name of the operator.
            e.g. OccupancyCounting.
        tag (str):
            Optional. Tag of the operator.
        registry (google.cloud.visionai_v1.types.Registry):
            Optional. Registry of the operator.
    """

    operator: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    registry: "Registry" = proto.Field(
        proto.ENUM,
        number=3,
        enum="Registry",
    )


class ResolveOperatorInfoResponse(proto.Message):
    r"""Response message of ResolveOperatorInfo API.

    Attributes:
        operators (MutableSequence[google.cloud.visionai_v1.types.Operator]):
            Operators with detailed information.
    """

    operators: MutableSequence[lva_resources.Operator] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=lva_resources.Operator,
    )


class ListPublicOperatorsRequest(proto.Message):
    r"""Request message of ListPublicOperatorsRequest API.

    Attributes:
        parent (str):
            Required. Parent value for
            ListPublicOperatorsRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Hint for how to order the results.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListPublicOperatorsResponse(proto.Message):
    r"""Response message of ListPublicOperators API.

    Attributes:
        operators (MutableSequence[google.cloud.visionai_v1.types.Operator]):
            The list of Operator
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    operators: MutableSequence[lva_resources.Operator] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=lva_resources.Operator,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
