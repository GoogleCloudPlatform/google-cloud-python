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

__protobuf__ = proto.module(
    package="google.cloud.networkconnectivity.v1",
    manifest={
        "MulticloudDataTransferConfig",
        "ListMulticloudDataTransferConfigsRequest",
        "ListMulticloudDataTransferConfigsResponse",
        "GetMulticloudDataTransferConfigRequest",
        "CreateMulticloudDataTransferConfigRequest",
        "UpdateMulticloudDataTransferConfigRequest",
        "DeleteMulticloudDataTransferConfigRequest",
        "Destination",
        "ListDestinationsRequest",
        "ListDestinationsResponse",
        "GetDestinationRequest",
        "CreateDestinationRequest",
        "UpdateDestinationRequest",
        "DeleteDestinationRequest",
        "StateTimeline",
        "MulticloudDataTransferSupportedService",
        "ServiceConfig",
        "GetMulticloudDataTransferSupportedServiceRequest",
        "ListMulticloudDataTransferSupportedServicesRequest",
        "ListMulticloudDataTransferSupportedServicesResponse",
    },
)


class MulticloudDataTransferConfig(proto.Message):
    r"""The ``MulticloudDataTransferConfig`` resource. It lists the services
    that you configure for Data Transfer Essentials billing and
    metering.

    Attributes:
        name (str):
            Identifier. The name of the ``MulticloudDataTransferConfig``
            resource. Format:
            ``projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ``MulticloudDataTransferConfig``
            resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ``MulticloudDataTransferConfig``
            resource was updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
        etag (str):
            The etag is computed by the server, and might
            be sent with update and delete requests so that
            the client has an up-to-date value before
            proceeding.
        description (str):
            Optional. A description of this resource.
        destinations_count (int):
            Output only. The number of ``Destination`` resources
            configured for the ``MulticloudDataTransferConfig``
            resource.
        destinations_active_count (int):
            Output only. The number of ``Destination`` resources in use
            with the ``MulticloudDataTransferConfig`` resource.
        services (MutableMapping[str, google.cloud.networkconnectivity_v1.types.StateTimeline]):
            Optional. Maps services to their current or planned states.
            Service names are keys, and the associated values describe
            the state of the service. If a state change is expected, the
            value is either ``ADDING`` or ``DELETING``, depending on the
            actions taken.

            Sample output: "services": { "big-query": { "states": [ {
            "effectiveTime": "2024-12-12T08:00:00Z" "state": "ADDING",
            }, ] }, "cloud-storage": { "states": [ { "state": "ACTIVE",
            } ] } }
        uid (str):
            Output only. The Google-generated unique ID for the
            ``MulticloudDataTransferConfig`` resource. This value is
            unique across all ``MulticloudDataTransferConfig``
            resources. If a resource is deleted and another with the
            same name is created, the new resource is assigned a
            different and unique ID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    destinations_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    destinations_active_count: int = proto.Field(
        proto.INT32,
        number=8,
    )
    services: MutableMapping[str, "StateTimeline"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=9,
        message="StateTimeline",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ListMulticloudDataTransferConfigsRequest(proto.Message):
    r"""Request message to list ``MulticloudDataTransferConfig`` resources.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        page_size (int):
            Optional. The maximum number of results
            listed per page.
        page_token (str):
            Optional. The page token.
        filter (str):
            Optional. An expression that filters the
            results listed in the response.
        order_by (str):
            Optional. The sort order of the results.
        return_partial_success (bool):
            Optional. If ``true``, allows partial responses for
            multi-regional aggregated list requests.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListMulticloudDataTransferConfigsResponse(proto.Message):
    r"""Response message to list ``MulticloudDataTransferConfig`` resources.

    Attributes:
        multicloud_data_transfer_configs (MutableSequence[google.cloud.networkconnectivity_v1.types.MulticloudDataTransferConfig]):
            The list of ``MulticloudDataTransferConfig`` resources to be
            listed.
        next_page_token (str):
            The next page token.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    multicloud_data_transfer_configs: MutableSequence[
        "MulticloudDataTransferConfig"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MulticloudDataTransferConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMulticloudDataTransferConfigRequest(proto.Message):
    r"""Request message to get the details of a
    ``MulticloudDataTransferConfig`` resource.

    Attributes:
        name (str):
            Required. The name of the ``MulticloudDataTransferConfig``
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMulticloudDataTransferConfigRequest(proto.Message):
    r"""Request message to create a ``MulticloudDataTransferConfig``
    resource.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        multicloud_data_transfer_config_id (str):
            Required. The ID to use for the
            ``MulticloudDataTransferConfig`` resource, which becomes the
            final component of the ``MulticloudDataTransferConfig``
            resource name.
        multicloud_data_transfer_config (google.cloud.networkconnectivity_v1.types.MulticloudDataTransferConfig):
            Required. The ``MulticloudDataTransferConfig`` resource to
            create.
        request_id (str):
            Optional. A request ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server can ignore the request if it has already been
            completed. The server waits for at least 60 minutes since
            the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, can ignore the second request. This prevents
            clients from accidentally creating duplicate
            ``MulticloudDataTransferConfig`` resources.

            The request ID must be a valid UUID with the exception that
            zero UUID (00000000-0000-0000-0000-000000000000) isn't
            supported.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    multicloud_data_transfer_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    multicloud_data_transfer_config: "MulticloudDataTransferConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MulticloudDataTransferConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMulticloudDataTransferConfigRequest(proto.Message):
    r"""Request message to update a ``MulticloudDataTransferConfig``
    resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. ``FieldMask`` is used to specify the fields in the
            ``MulticloudDataTransferConfig`` resource to be overwritten
            by the update. The fields specified in ``update_mask`` are
            relative to the resource, not the full request. A field is
            overwritten if it is in the mask. If you don't specify a
            mask, all fields are overwritten.
        multicloud_data_transfer_config (google.cloud.networkconnectivity_v1.types.MulticloudDataTransferConfig):
            Required. The ``MulticloudDataTransferConfig`` resource to
            update.
        request_id (str):
            Optional. A request ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server can ignore the request if it has already been
            completed. The server waits for at least 60 minutes since
            the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, can ignore the second request. This prevents
            clients from accidentally creating duplicate
            ``MulticloudDataTransferConfig`` resources.

            The request ID must be a valid UUID with the exception that
            zero UUID (00000000-0000-0000-0000-000000000000) isn't
            supported.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    multicloud_data_transfer_config: "MulticloudDataTransferConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MulticloudDataTransferConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMulticloudDataTransferConfigRequest(proto.Message):
    r"""Request message to delete a ``MulticloudDataTransferConfig``
    resource.

    Attributes:
        name (str):
            Required. The name of the ``MulticloudDataTransferConfig``
            resource to delete.
        request_id (str):
            Optional. A request ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server can ignore the request if it has already been
            completed. The server waits for at least 60 minutes since
            the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, can ignore the second request. This prevents
            clients from accidentally creating duplicate
            ``MulticloudDataTransferConfig`` resources.

            The request ID must be a valid UUID with the exception that
            zero UUID (00000000-0000-0000-0000-000000000000) isn't
            supported.
        etag (str):
            Optional. The etag is computed by the server,
            and might be sent with update and delete
            requests so that the client has an up-to-date
            value before proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Destination(proto.Message):
    r"""The ``Destination`` resource. It specifies the IP prefix and the
    associated autonomous system numbers (ASN) that you want to include
    in a ``MulticloudDataTransferConfig`` resource.

    Attributes:
        name (str):
            Identifier. The name of the ``Destination`` resource.
            Format:
            ``projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}/destinations/{destination}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ``Destination`` resource was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ``Destination`` resource was
            updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
        etag (str):
            The etag is computed by the server, and might
            be sent with update and delete requests so that
            the client has an up-to-date value before
            proceeding.
        description (str):
            Optional. A description of this resource.
        ip_prefix (str):
            Required. Immutable. The IP prefix that
            represents your workload on another CSP.
        endpoints (MutableSequence[google.cloud.networkconnectivity_v1.types.Destination.DestinationEndpoint]):
            Required. Unordered list. The list of
            ``DestinationEndpoint`` resources configured for the IP
            prefix.
        state_timeline (google.cloud.networkconnectivity_v1.types.StateTimeline):
            Output only. The timeline of the expected ``Destination``
            states or the current rest state. If a state change is
            expected, the value is ``ADDING``, ``DELETING`` or
            ``SUSPENDING``, depending on the action specified.

            Example: "state_timeline": { "states": [ { // The time when
            the ``Destination`` resource will be activated.
            "effectiveTime": "2024-12-01T08:00:00Z", "state": "ADDING"
            }, { // The time when the ``Destination`` resource will be
            suspended. "effectiveTime": "2024-12-01T20:00:00Z", "state":
            "SUSPENDING" } ] }
        uid (str):
            Output only. The Google-generated unique ID for the
            ``Destination`` resource. This value is unique across all
            ``Destination`` resources. If a resource is deleted and
            another with the same name is created, the new resource is
            assigned a different and unique ID.
    """

    class DestinationEndpoint(proto.Message):
        r"""The metadata for a ``DestinationEndpoint`` resource.

        Attributes:
            asn (int):
                Required. The ASN of the remote IP prefix.
            csp (str):
                Required. The CSP of the remote IP prefix.
            state (google.cloud.networkconnectivity_v1.types.Destination.DestinationEndpoint.State):
                Output only. The state of the ``DestinationEndpoint``
                resource.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Time when the ``DestinationEndpoint`` resource
                was updated.
        """

        class State(proto.Enum):
            r"""The state of the ``DestinationEndpoint`` resource.

            Values:
                STATE_UNSPECIFIED (0):
                    An invalid state, which is the default case.
                VALID (1):
                    The ``DestinationEndpoint`` resource is valid.
                INVALID (2):
                    The ``DestinationEndpoint`` resource is invalid.
            """

            STATE_UNSPECIFIED = 0
            VALID = 1
            INVALID = 2

        asn: int = proto.Field(
            proto.INT64,
            number=1,
        )
        csp: str = proto.Field(
            proto.STRING,
            number=2,
        )
        state: "Destination.DestinationEndpoint.State" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Destination.DestinationEndpoint.State",
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ip_prefix: str = proto.Field(
        proto.STRING,
        number=7,
    )
    endpoints: MutableSequence[DestinationEndpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=DestinationEndpoint,
    )
    state_timeline: "StateTimeline" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="StateTimeline",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ListDestinationsRequest(proto.Message):
    r"""Request message to list ``Destination`` resources.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        page_size (int):
            Optional. The maximum number of results
            listed per page.
        page_token (str):
            Optional. The page token.
        filter (str):
            Optional. An expression that filters the
            results listed in the response.
        order_by (str):
            Optional. The sort order of the results.
        return_partial_success (bool):
            Optional. If ``true``, allow partial responses for
            multi-regional aggregated list requests.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListDestinationsResponse(proto.Message):
    r"""Response message to list ``Destination`` resources.

    Attributes:
        destinations (MutableSequence[google.cloud.networkconnectivity_v1.types.Destination]):
            The list of ``Destination`` resources to be listed.
        next_page_token (str):
            The next page token.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    destinations: MutableSequence["Destination"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Destination",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDestinationRequest(proto.Message):
    r"""Request message to get the details of a ``Destination`` resource.

    Attributes:
        name (str):
            Required. The name of the ``Destination`` resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDestinationRequest(proto.Message):
    r"""Request message to create a ``Destination`` resource.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        destination_id (str):
            Required. The ID to use for the ``Destination`` resource,
            which becomes the final component of the ``Destination``
            resource name.
        destination (google.cloud.networkconnectivity_v1.types.Destination):
            Required. The ``Destination`` resource to create.
        request_id (str):
            Optional. A request ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server can ignore the request if it has already been
            completed. The server waits for at least 60 minutes since
            the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, can ignore the second request. This prevents
            clients from accidentally creating duplicate ``Destination``
            resources.

            The request ID must be a valid UUID with the exception that
            zero UUID (00000000-0000-0000-0000-000000000000) isn't
            supported.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    destination: "Destination" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Destination",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateDestinationRequest(proto.Message):
    r"""Request message to update a ``Destination`` resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional.
            ``FieldMask is used to specify the fields to be overwritten in the``\ Destination\ ``resource by the update. The fields specified in``\ update_mask\`
            are relative to the resource, not the full request. A field
            is overwritten if it is in the mask. If you don't specify a
            mask, all fields are overwritten.
        destination (google.cloud.networkconnectivity_v1.types.Destination):
            Required. The ``Destination`` resource to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server can ignore the
            request if it has already been completed. The
            server waits for at least 60 minutes since the
            first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, can ignore the second request.

            The request ID must be a valid UUID with the
            exception that zero UUID
            (00000000-0000-0000-0000-000000000000) isn't
            supported.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    destination: "Destination" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Destination",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteDestinationRequest(proto.Message):
    r"""Request message to delete a ``Destination`` resource.

    Attributes:
        name (str):
            Required. The name of the ``Destination`` resource to
            delete.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server can ignore the
            request if it has already been completed. The
            server waits for at least 60 minutes since the
            first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, can ignore the second request.

            The request ID must be a valid UUID with the
            exception that zero UUID
            (00000000-0000-0000-0000-000000000000) isn't
            supported.
        etag (str):
            Optional. The etag is computed by the server,
            and might be sent with update and delete
            requests so that the client has an up-to-date
            value before proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StateTimeline(proto.Message):
    r"""The timeline of the pending states for a resource.

    Attributes:
        states (MutableSequence[google.cloud.networkconnectivity_v1.types.StateTimeline.StateMetadata]):
            Output only. The state and activation time
            details of the resource state.
    """

    class StateMetadata(proto.Message):
        r"""The state and activation time details of the resource state.

        Attributes:
            state (google.cloud.networkconnectivity_v1.types.StateTimeline.StateMetadata.State):
                Output only. The state of the resource.
            effective_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Accompanies only the transient states, which
                include ``ADDING``, ``DELETING``, and ``SUSPENDING``, to
                denote the time until which the transient state of the
                resource will be effective. For instance, if the state is
                ``ADDING``, this field shows the time when the resource
                state transitions to ``ACTIVE``.
        """

        class State(proto.Enum):
            r"""The state of the resource.

            Values:
                STATE_UNSPECIFIED (0):
                    An invalid state, which is the default case.
                ADDING (1):
                    The resource is being added.
                ACTIVE (2):
                    The resource is in use.
                DELETING (3):
                    The resource is being deleted.
                SUSPENDING (4):
                    The resource is being suspended.
                SUSPENDED (5):
                    The resource is suspended and not in use.
            """

            STATE_UNSPECIFIED = 0
            ADDING = 1
            ACTIVE = 2
            DELETING = 3
            SUSPENDING = 4
            SUSPENDED = 5

        state: "StateTimeline.StateMetadata.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="StateTimeline.StateMetadata.State",
        )
        effective_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    states: MutableSequence[StateMetadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=StateMetadata,
    )


class MulticloudDataTransferSupportedService(proto.Message):
    r"""A service in your project in a region that is eligible for
    Data Transfer Essentials configuration.

    Attributes:
        name (str):
            Identifier. The name of the service.
        service_configs (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConfig]):
            Output only. The network service tier or
            regional endpoint supported for the service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_configs: MutableSequence["ServiceConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ServiceConfig",
    )


class ServiceConfig(proto.Message):
    r"""Specifies eligibility information for the service.

    Attributes:
        eligibility_criteria (google.cloud.networkconnectivity_v1.types.ServiceConfig.EligibilityCriteria):
            Output only. The eligibility criteria for the
            service.
        support_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time for eligibility
            criteria support. If not specified, no planned
            end time is set.
    """

    class EligibilityCriteria(proto.Enum):
        r"""The eligibility information for the service.

        Values:
            ELIGIBILITY_CRITERIA_UNSPECIFIED (0):
                The service is not eligible for Data Transfer
                Essentials configuration. This is the default
                case.
            NETWORK_SERVICE_TIER_PREMIUM_ONLY (1):
                The service is eligible for Data Transfer
                Essentials configuration only for Premium Tier.
            NETWORK_SERVICE_TIER_STANDARD_ONLY (2):
                The service is eligible for Data Transfer
                Essentials configuration only for Standard Tier.
            REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY (3):
                The service is eligible for Data Transfer
                Essentials configuration only for the regional
                endpoint.
        """

        ELIGIBILITY_CRITERIA_UNSPECIFIED = 0
        NETWORK_SERVICE_TIER_PREMIUM_ONLY = 1
        NETWORK_SERVICE_TIER_STANDARD_ONLY = 2
        REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY = 3

    eligibility_criteria: EligibilityCriteria = proto.Field(
        proto.ENUM,
        number=1,
        enum=EligibilityCriteria,
    )
    support_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class GetMulticloudDataTransferSupportedServiceRequest(proto.Message):
    r"""Request message to check if a service in your project in a
    region is eligible for Data Transfer Essentials configuration.

    Attributes:
        name (str):
            Required. The name of the service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMulticloudDataTransferSupportedServicesRequest(proto.Message):
    r"""Request message to list the services in your project that are
    eligible for Data Transfer Essentials configuration.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        page_size (int):
            Optional. The maximum number of results
            listed per page.
        page_token (str):
            Optional. The page token.
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


class ListMulticloudDataTransferSupportedServicesResponse(proto.Message):
    r"""Response message to list the services in your project in
    regions that are eligible for Data Transfer Essentials
    configuration.

    Attributes:
        multicloud_data_transfer_supported_services (MutableSequence[google.cloud.networkconnectivity_v1.types.MulticloudDataTransferSupportedService]):
            The list of supported services.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    multicloud_data_transfer_supported_services: MutableSequence[
        "MulticloudDataTransferSupportedService"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MulticloudDataTransferSupportedService",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
