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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.apphub_v1.types import application as gca_application
from google.cloud.apphub_v1.types import boundary as gca_boundary
from google.cloud.apphub_v1.types import extended_metadata_schema
from google.cloud.apphub_v1.types import service as gca_service
from google.cloud.apphub_v1.types import (
    service_project_attachment as gca_service_project_attachment,
)
from google.cloud.apphub_v1.types import workload as gca_workload

__protobuf__ = proto.module(
    package="google.cloud.apphub.v1",
    manifest={
        "LookupServiceProjectAttachmentRequest",
        "LookupServiceProjectAttachmentResponse",
        "ListServiceProjectAttachmentsRequest",
        "ListServiceProjectAttachmentsResponse",
        "CreateServiceProjectAttachmentRequest",
        "GetServiceProjectAttachmentRequest",
        "DeleteServiceProjectAttachmentRequest",
        "DetachServiceProjectAttachmentRequest",
        "DetachServiceProjectAttachmentResponse",
        "ListServicesRequest",
        "ListServicesResponse",
        "ListDiscoveredServicesRequest",
        "ListDiscoveredServicesResponse",
        "CreateServiceRequest",
        "GetServiceRequest",
        "GetDiscoveredServiceRequest",
        "LookupDiscoveredServiceRequest",
        "LookupDiscoveredServiceResponse",
        "UpdateServiceRequest",
        "DeleteServiceRequest",
        "ListApplicationsRequest",
        "ListApplicationsResponse",
        "CreateApplicationRequest",
        "GetApplicationRequest",
        "UpdateApplicationRequest",
        "DeleteApplicationRequest",
        "ListWorkloadsRequest",
        "ListWorkloadsResponse",
        "ListDiscoveredWorkloadsRequest",
        "ListDiscoveredWorkloadsResponse",
        "CreateWorkloadRequest",
        "GetWorkloadRequest",
        "GetDiscoveredWorkloadRequest",
        "LookupDiscoveredWorkloadRequest",
        "LookupDiscoveredWorkloadResponse",
        "UpdateWorkloadRequest",
        "DeleteWorkloadRequest",
        "GetBoundaryRequest",
        "UpdateBoundaryRequest",
        "OperationMetadata",
        "GetExtendedMetadataSchemaRequest",
        "ListExtendedMetadataSchemasRequest",
        "ListExtendedMetadataSchemasResponse",
    },
)


class LookupServiceProjectAttachmentRequest(proto.Message):
    r"""Request for LookupServiceProjectAttachment.

    Attributes:
        name (str):
            Required. Service project ID and location to lookup service
            project attachment for. Only global location is supported.
            Expected format:
            ``projects/{project}/locations/{location}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupServiceProjectAttachmentResponse(proto.Message):
    r"""Response for LookupServiceProjectAttachment.

    Attributes:
        service_project_attachment (google.cloud.apphub_v1.types.ServiceProjectAttachment):
            Service project attachment for a project if
            exists, empty otherwise.
    """

    service_project_attachment: gca_service_project_attachment.ServiceProjectAttachment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gca_service_project_attachment.ServiceProjectAttachment,
    )


class ListServiceProjectAttachmentsRequest(proto.Message):
    r"""Request for ListServiceProjectAttachments.

    Attributes:
        parent (str):
            Required. Host project ID and location to list service
            project attachments. Only global location is supported.
            Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListServiceProjectAttachmentsResponse(proto.Message):
    r"""Response for ListServiceProjectAttachments.

    Attributes:
        service_project_attachments (MutableSequence[google.cloud.apphub_v1.types.ServiceProjectAttachment]):
            List of service project attachments.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    service_project_attachments: MutableSequence[
        gca_service_project_attachment.ServiceProjectAttachment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_service_project_attachment.ServiceProjectAttachment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateServiceProjectAttachmentRequest(proto.Message):
    r"""Request for CreateServiceProjectAttachment.

    Attributes:
        parent (str):
            Required. Host project ID and location to which service
            project is being attached. Only global location is
            supported. Expected format:
            ``projects/{project}/locations/{location}``.
        service_project_attachment_id (str):
            Required. The service project attachment identifier must
            contain the project id of the service project specified in
            the service_project_attachment.service_project field.
        service_project_attachment (google.cloud.apphub_v1.types.ServiceProjectAttachment):
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
    service_project_attachment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_project_attachment: gca_service_project_attachment.ServiceProjectAttachment = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_service_project_attachment.ServiceProjectAttachment,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetServiceProjectAttachmentRequest(proto.Message):
    r"""Request for GetServiceProjectAttachment.

    Attributes:
        name (str):
            Required. Fully qualified name of the service project
            attachment to retrieve. Expected format:
            ``projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteServiceProjectAttachmentRequest(proto.Message):
    r"""Request for DeleteServiceProjectAttachment.

    Attributes:
        name (str):
            Required. Fully qualified name of the service project
            attachment to delete. Expected format:
            ``projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}``.
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


class DetachServiceProjectAttachmentRequest(proto.Message):
    r"""Request for DetachServiceProjectAttachment.

    Attributes:
        name (str):
            Required. Service project id and location to detach from a
            host project. Only global location is supported. Expected
            format: ``projects/{project}/locations/{location}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DetachServiceProjectAttachmentResponse(proto.Message):
    r"""Response for DetachServiceProjectAttachment."""


class ListServicesRequest(proto.Message):
    r"""Request for ListServices.

    Attributes:
        parent (str):
            Required. Fully qualified name of the parent Application to
            list Services for. Expected format:
            ``projects/{project}/locations/{location}/applications/{application}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListServicesResponse(proto.Message):
    r"""Response for ListServices.

    Attributes:
        services (MutableSequence[google.cloud.apphub_v1.types.Service]):
            List of Services.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[gca_service.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_service.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListDiscoveredServicesRequest(proto.Message):
    r"""Request for ListDiscoveredServices.

    Attributes:
        parent (str):
            Required. Project and location to list Discovered Services
            on. Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListDiscoveredServicesResponse(proto.Message):
    r"""Response for ListDiscoveredServices.

    Attributes:
        discovered_services (MutableSequence[google.cloud.apphub_v1.types.DiscoveredService]):
            List of Discovered Services.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    discovered_services: MutableSequence[gca_service.DiscoveredService] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gca_service.DiscoveredService,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateServiceRequest(proto.Message):
    r"""Request for CreateService.

    Attributes:
        parent (str):
            Required. Fully qualified name of the parent Application to
            create the Service in. Expected format:
            ``projects/{project}/locations/{location}/applications/{application}``.
        service_id (str):
            Required. The Service identifier.
            Must contain only lowercase letters, numbers
            or hyphens, with the first character a letter,
            the last a letter or a number, and a 63
            character maximum.
        service (google.cloud.apphub_v1.types.Service):
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
    service_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service: gca_service.Service = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_service.Service,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetServiceRequest(proto.Message):
    r"""Request for GetService.

    Attributes:
        name (str):
            Required. Fully qualified name of the Service to fetch.
            Expected format:
            ``projects/{project}/locations/{location}/applications/{application}/services/{service}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetDiscoveredServiceRequest(proto.Message):
    r"""Request for GetDiscoveredService.

    Attributes:
        name (str):
            Required. Fully qualified name of the Discovered Service to
            fetch. Expected format:
            ``projects/{project}/locations/{location}/discoveredServices/{discoveredService}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupDiscoveredServiceRequest(proto.Message):
    r"""Request for LookupDiscoveredService.

    Attributes:
        parent (str):
            Required. Host project ID and location to lookup Discovered
            Service in. Expected format:
            ``projects/{project}/locations/{location}``.
        uri (str):
            Required. Resource URI to find
            DiscoveredService for. Accepts both project
            number and project ID and does translation when
            needed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LookupDiscoveredServiceResponse(proto.Message):
    r"""Response for LookupDiscoveredService.

    Attributes:
        discovered_service (google.cloud.apphub_v1.types.DiscoveredService):
            Discovered Service if exists, empty
            otherwise.
    """

    discovered_service: gca_service.DiscoveredService = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gca_service.DiscoveredService,
    )


class UpdateServiceRequest(proto.Message):
    r"""Request for UpdateService.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Service resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. The API changes the values
            of the fields as specified in the update_mask. The API
            ignores the values of all fields not covered by the
            update_mask. You can also unset a field by not specifying it
            in the updated message, but adding the field to the mask.
            This clears whatever value the field previously had.
        service (google.cloud.apphub_v1.types.Service):
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
    service: gca_service.Service = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gca_service.Service,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServiceRequest(proto.Message):
    r"""Request for DeleteService.

    Attributes:
        name (str):
            Required. Fully qualified name of the Service to delete from
            an Application. Expected format:
            ``projects/{project}/locations/{location}/applications/{application}/services/{service}``.
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


class ListApplicationsRequest(proto.Message):
    r"""Request for ListApplications.

    Attributes:
        parent (str):
            Required. Project and location to list Applications on.
            Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListApplicationsResponse(proto.Message):
    r"""Response for ListApplications.

    Attributes:
        applications (MutableSequence[google.cloud.apphub_v1.types.Application]):
            List of Applications.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    applications: MutableSequence[gca_application.Application] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_application.Application,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateApplicationRequest(proto.Message):
    r"""Request for CreateApplication.

    Attributes:
        parent (str):
            Required. Project and location to create Application in.
            Expected format:
            ``projects/{project}/locations/{location}``.
        application_id (str):
            Required. The Application identifier.
            Must contain only lowercase letters, numbers
            or hyphens, with the first character a letter,
            the last a letter or a number, and a 63
            character maximum.
        application (google.cloud.apphub_v1.types.Application):
            Required. The resource being created
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
    application_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    application: gca_application.Application = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_application.Application,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetApplicationRequest(proto.Message):
    r"""Request for GetApplication.

    Attributes:
        name (str):
            Required. Fully qualified name of the Application to fetch.
            Expected format:
            ``projects/{project}/locations/{location}/applications/{application}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateApplicationRequest(proto.Message):
    r"""Request for UpdateApplication.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Application resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. The API changes the values
            of the fields as specified in the update_mask. The API
            ignores the values of all fields not covered by the
            update_mask. You can also unset a field by not specifying it
            in the updated message, but adding the field to the mask.
            This clears whatever value the field previously had.
        application (google.cloud.apphub_v1.types.Application):
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
    application: gca_application.Application = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gca_application.Application,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteApplicationRequest(proto.Message):
    r"""Request for DeleteApplication.

    Attributes:
        name (str):
            Required. Fully qualified name of the Application to delete.
            Expected format:
            ``projects/{project}/locations/{location}/applications/{application}``.
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


class ListWorkloadsRequest(proto.Message):
    r"""Request for ListWorkloads.

    Attributes:
        parent (str):
            Required. Fully qualified name of the parent Application to
            list Workloads for. Expected format:
            ``projects/{project}/locations/{location}/applications/{application}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListWorkloadsResponse(proto.Message):
    r"""Response for ListWorkloads.

    Attributes:
        workloads (MutableSequence[google.cloud.apphub_v1.types.Workload]):
            List of Workloads.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    workloads: MutableSequence[gca_workload.Workload] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_workload.Workload,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListDiscoveredWorkloadsRequest(proto.Message):
    r"""Request for ListDiscoveredWorkloads.

    Attributes:
        parent (str):
            Required. Project and location to list Discovered Workloads
            on. Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListDiscoveredWorkloadsResponse(proto.Message):
    r"""Response for ListDiscoveredWorkloads.

    Attributes:
        discovered_workloads (MutableSequence[google.cloud.apphub_v1.types.DiscoveredWorkload]):
            List of Discovered Workloads.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    discovered_workloads: MutableSequence[gca_workload.DiscoveredWorkload] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gca_workload.DiscoveredWorkload,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateWorkloadRequest(proto.Message):
    r"""Request for CreateWorkload.

    Attributes:
        parent (str):
            Required. Fully qualified name of the Application to create
            Workload in. Expected format:
            ``projects/{project}/locations/{location}/applications/{application}``.
        workload_id (str):
            Required. The Workload identifier.
            Must contain only lowercase letters, numbers
            or hyphens, with the first character a letter,
            the last a letter or a number, and a 63
            character maximum.
        workload (google.cloud.apphub_v1.types.Workload):
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
    workload_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    workload: gca_workload.Workload = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_workload.Workload,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetWorkloadRequest(proto.Message):
    r"""Request for GetWorkload.

    Attributes:
        name (str):
            Required. Fully qualified name of the Workload to fetch.
            Expected format:
            ``projects/{project}/locations/{location}/applications/{application}/workloads/{workload}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetDiscoveredWorkloadRequest(proto.Message):
    r"""Request for GetDiscoveredWorkload.

    Attributes:
        name (str):
            Required. Fully qualified name of the Discovered Workload to
            fetch. Expected format:
            ``projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupDiscoveredWorkloadRequest(proto.Message):
    r"""Request for LookupDiscoveredWorkload.

    Attributes:
        parent (str):
            Required. Host project ID and location to lookup Discovered
            Workload in. Expected format:
            ``projects/{project}/locations/{location}``.
        uri (str):
            Required. Resource URI to find Discovered
            Workload for. Accepts both project number and
            project ID and does translation when needed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LookupDiscoveredWorkloadResponse(proto.Message):
    r"""Response for LookupDiscoveredWorkload.

    Attributes:
        discovered_workload (google.cloud.apphub_v1.types.DiscoveredWorkload):
            Discovered Workload if exists, empty
            otherwise.
    """

    discovered_workload: gca_workload.DiscoveredWorkload = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gca_workload.DiscoveredWorkload,
    )


class UpdateWorkloadRequest(proto.Message):
    r"""Request for UpdateWorkload.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Workload resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. The API changes the values
            of the fields as specified in the update_mask. The API
            ignores the values of all fields not covered by the
            update_mask. You can also unset a field by not specifying it
            in the updated message, but adding the field to the mask.
            This clears whatever value the field previously had.
        workload (google.cloud.apphub_v1.types.Workload):
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
    workload: gca_workload.Workload = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gca_workload.Workload,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteWorkloadRequest(proto.Message):
    r"""Request for DeleteWorkload.

    Attributes:
        name (str):
            Required. Fully qualified name of the Workload to delete
            from an Application. Expected format:
            ``projects/{project}/locations/{location}/applications/{application}/workloads/{workload}``.
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


class GetBoundaryRequest(proto.Message):
    r"""Request message for AppHub.GetBoundary.

    Attributes:
        name (str):
            Required. The name of the boundary to retrieve. Format:
            ``projects/{project}/locations/{location}/boundary``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBoundaryRequest(proto.Message):
    r"""Request message for AppHub.UpdateBoundary.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Boundary resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        boundary (google.cloud.apphub_v1.types.Boundary):
            Required. The boundary to update.
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
    boundary: gca_boundary.Boundary = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gca_boundary.Boundary,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GetExtendedMetadataSchemaRequest(proto.Message):
    r"""Request for GetExtendedMetadataSchema.

    Attributes:
        name (str):
            Required. Schema resource name. Format:
            ``projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}``.

            ``{extended_metadata_schema}`` has the format
            ``"apphub.googleapis.com/{SchemaName}"``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExtendedMetadataSchemasRequest(proto.Message):
    r"""Request for ListExtendedMetadataSchemas.

    Attributes:
        parent (str):
            Required. Project and location to list Extended Metadata
            Schemas on. Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListExtendedMetadataSchemasResponse(proto.Message):
    r"""Response for ListExtendedMetadataSchemas.

    Attributes:
        extended_metadata_schemas (MutableSequence[google.cloud.apphub_v1.types.ExtendedMetadataSchema]):
            List of Extended Metadata Schemas.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    extended_metadata_schemas: MutableSequence[
        extended_metadata_schema.ExtendedMetadataSchema
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=extended_metadata_schema.ExtendedMetadataSchema,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
