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
import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networkconnectivity.v1",
    manifest={
        "Infrastructure",
        "ConnectionErrorType",
        "IPVersion",
        "ServiceConnectionMap",
        "ListServiceConnectionMapsRequest",
        "ListServiceConnectionMapsResponse",
        "GetServiceConnectionMapRequest",
        "CreateServiceConnectionMapRequest",
        "UpdateServiceConnectionMapRequest",
        "DeleteServiceConnectionMapRequest",
        "ServiceConnectionPolicy",
        "ListServiceConnectionPoliciesRequest",
        "ListServiceConnectionPoliciesResponse",
        "GetServiceConnectionPolicyRequest",
        "CreateServiceConnectionPolicyRequest",
        "UpdateServiceConnectionPolicyRequest",
        "DeleteServiceConnectionPolicyRequest",
        "ServiceClass",
        "ListServiceClassesRequest",
        "ListServiceClassesResponse",
        "GetServiceClassRequest",
        "UpdateServiceClassRequest",
        "DeleteServiceClassRequest",
        "ServiceConnectionToken",
        "ListServiceConnectionTokensRequest",
        "ListServiceConnectionTokensResponse",
        "GetServiceConnectionTokenRequest",
        "CreateServiceConnectionTokenRequest",
        "DeleteServiceConnectionTokenRequest",
    },
)


class Infrastructure(proto.Enum):
    r"""The infrastructure used for connections between
    consumers/producers.

    Values:
        INFRASTRUCTURE_UNSPECIFIED (0):
            An invalid infrastructure as the default
            case.
        PSC (1):
            Private Service Connect is used for
            connections.
    """

    INFRASTRUCTURE_UNSPECIFIED = 0
    PSC = 1


class ConnectionErrorType(proto.Enum):
    r"""The error type indicates whether a connection error is
    consumer facing, producer facing or system internal.

    Values:
        CONNECTION_ERROR_TYPE_UNSPECIFIED (0):
            An invalid error type as the default case.
        ERROR_INTERNAL (1):
            The error is due to Service Automation system
            internal.
        ERROR_CONSUMER_SIDE (2):
            The error is due to the setup on consumer
            side.
        ERROR_PRODUCER_SIDE (3):
            The error is due to the setup on producer
            side.
    """

    CONNECTION_ERROR_TYPE_UNSPECIFIED = 0
    ERROR_INTERNAL = 1
    ERROR_CONSUMER_SIDE = 2
    ERROR_PRODUCER_SIDE = 3


class IPVersion(proto.Enum):
    r"""The requested IP version for the PSC connection.

    Values:
        IP_VERSION_UNSPECIFIED (0):
            Default value. We will use IPv4 or IPv6
            depending on the IP version of first available
            subnetwork.
        IPV4 (1):
            Will use IPv4 only.
        IPV6 (2):
            Will use IPv6 only.
    """

    IP_VERSION_UNSPECIFIED = 0
    IPV4 = 1
    IPV6 = 2


class ServiceConnectionMap(proto.Message):
    r"""The ServiceConnectionMap resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Immutable. The name of a ServiceConnectionMap. Format:
            projects/{project}/locations/{location}/serviceConnectionMaps/{service_connection_map}
            See:
            https://google.aip.dev/122#fields-representing-resource-names
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the
            ServiceConnectionMap was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the
            ServiceConnectionMap was updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            A description of this resource.
        service_class (str):
            The service class identifier this
            ServiceConnectionMap is for. The user of
            ServiceConnectionMap create API needs to have
            networkconnecitivty.serviceclasses.use iam
            permission for the service class.
        service_class_uri (str):
            Output only. The service class uri this
            ServiceConnectionMap is for.
        infrastructure (google.cloud.networkconnectivity_v1.types.Infrastructure):
            Output only. The infrastructure used for
            connections between consumers/producers.
        producer_psc_configs (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionMap.ProducerPscConfig]):
            The PSC configurations on producer side.
        consumer_psc_configs (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionMap.ConsumerPscConfig]):
            The PSC configurations on consumer side.
        consumer_psc_connections (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionMap.ConsumerPscConnection]):
            Output only. PSC connection details on
            consumer side.
        token (str):
            The token provided by the consumer. This
            token authenticates that the consumer can create
            a connection within the specified project and
            network.
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
    """

    class ProducerPscConfig(proto.Message):
        r"""The PSC configurations on producer side.

        Attributes:
            service_attachment_uri (str):
                The resource path of a service attachment.
                Example:

                projects/{projectNumOrId}/regions/{region}/serviceAttachments/{resourceId}.
        """

        service_attachment_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ConsumerPscConfig(proto.Message):
        r"""Allow the producer to specify which consumers can connect to
        it.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            project (str):
                The consumer project where PSC connections
                are allowed to be created in.
            network (str):
                The resource path of the consumer network
                where PSC connections are allowed to be created
                in. Note, this network does not need be in the
                ConsumerPscConfig.project in the case of
                SharedVPC. Example:

                projects/{projectNumOrId}/global/networks/{networkId}.
            disable_global_access (bool):
                This is used in PSC consumer ForwardingRule
                to control whether the PSC endpoint can be
                accessed from another region.
            state (google.cloud.networkconnectivity_v1.types.ServiceConnectionMap.ConsumerPscConfig.State):
                Output only. Overall state of PSC Connections
                management for this consumer psc config.
            producer_instance_id (str):
                Immutable. Deprecated. Use producer_instance_metadata
                instead. An immutable identifier for the producer instance.
            service_attachment_ip_address_map (MutableMapping[str, str]):
                Output only. A map to store mapping between
                customer vip and target service attachment. Only
                service attachment with producer specified ip
                addresses are stored here.
            consumer_instance_project (str):
                Required. The project ID or project number of the consumer
                project. This project is the one that the consumer uses to
                interact with the producer instance. From the perspective of
                a consumer who's created a producer instance, this is the
                project of the producer instance. Format:
                'projects/<project_id_or_number>' Eg.
                'projects/consumer-project' or 'projects/1234'
            producer_instance_metadata (MutableMapping[str, str]):
                Immutable. An immutable map for the producer
                instance metadata.
            ip_version (google.cloud.networkconnectivity_v1.types.IPVersion):
                The requested IP version for the PSC
                connection.

                This field is a member of `oneof`_ ``_ip_version``.
        """

        class State(proto.Enum):
            r"""PSC Consumer Config State.

            Values:
                STATE_UNSPECIFIED (0):
                    Default state, when Connection Map is created
                    initially.
                VALID (1):
                    Set when policy and map configuration is
                    valid, and their matching can lead to allowing
                    creation of PSC Connections subject to other
                    constraints like connections limit.
                CONNECTION_POLICY_MISSING (2):
                    No Service Connection Policy found for this
                    network and Service Class
                POLICY_LIMIT_REACHED (3):
                    Service Connection Policy limit reached for
                    this network and Service Class
                CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED (4):
                    The consumer instance project is not in
                    AllowedGoogleProducersResourceHierarchyLevels of
                    the matching ServiceConnectionPolicy.
            """

            STATE_UNSPECIFIED = 0
            VALID = 1
            CONNECTION_POLICY_MISSING = 2
            POLICY_LIMIT_REACHED = 3
            CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED = 4

        project: str = proto.Field(
            proto.STRING,
            number=1,
        )
        network: str = proto.Field(
            proto.STRING,
            number=2,
        )
        disable_global_access: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        state: "ServiceConnectionMap.ConsumerPscConfig.State" = proto.Field(
            proto.ENUM,
            number=4,
            enum="ServiceConnectionMap.ConsumerPscConfig.State",
        )
        producer_instance_id: str = proto.Field(
            proto.STRING,
            number=5,
        )
        service_attachment_ip_address_map: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=6,
        )
        consumer_instance_project: str = proto.Field(
            proto.STRING,
            number=7,
        )
        producer_instance_metadata: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=8,
        )
        ip_version: "IPVersion" = proto.Field(
            proto.ENUM,
            number=9,
            optional=True,
            enum="IPVersion",
        )

    class ConsumerPscConnection(proto.Message):
        r"""PSC connection details on consumer side.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            service_attachment_uri (str):
                The URI of a service attachment which is the
                target of the PSC connection.
            state (google.cloud.networkconnectivity_v1.types.ServiceConnectionMap.ConsumerPscConnection.State):
                The state of the PSC connection.
            project (str):
                The consumer project whose PSC forwarding
                rule is connected to the service attachments in
                this service connection map.
            network (str):
                The consumer network whose PSC forwarding
                rule is connected to the service attachments in
                this service connection map. Note that the
                network could be on a different project (shared
                VPC).
            psc_connection_id (str):
                The PSC connection id of the PSC forwarding
                rule connected to the service attachments in
                this service connection map.
            ip (str):
                The IP literal allocated on the consumer
                network for the PSC forwarding rule that is
                created to connect to the producer service
                attachment in this service connection map.
            error_type (google.cloud.networkconnectivity_v1.types.ConnectionErrorType):
                The error type indicates whether the error is
                consumer facing, producer facing or system
                internal.
            error (google.rpc.status_pb2.Status):
                The most recent error during operating this
                connection.
            gce_operation (str):
                The last Compute Engine operation to setup
                PSC connection.
            forwarding_rule (str):
                The URI of the consumer forwarding rule
                created. Example:

                projects/{projectNumOrId}/regions/us-east1/networks/{resourceId}.
            error_info (google.rpc.error_details_pb2.ErrorInfo):
                Output only. The error info for the latest
                error during operating this connection.
            selected_subnetwork (str):
                Output only. The URI of the selected
                subnetwork selected to allocate IP address for
                this connection.
            producer_instance_id (str):
                Immutable. Deprecated. Use producer_instance_metadata
                instead. An immutable identifier for the producer instance.
            producer_instance_metadata (MutableMapping[str, str]):
                Immutable. An immutable map for the producer
                instance metadata.
            ip_version (google.cloud.networkconnectivity_v1.types.IPVersion):
                The requested IP version for the PSC
                connection.

                This field is a member of `oneof`_ ``_ip_version``.
        """

        class State(proto.Enum):
            r"""The state of the PSC connection.
            We reserve the right to add more states without notice in the
            future. Users should not use exhaustive switch statements on
            this enum. See https://google.aip.dev/216.

            Values:
                STATE_UNSPECIFIED (0):
                    An invalid state as the default case.
                ACTIVE (1):
                    The connection has been created successfully.
                    However, for the up-to-date connection status,
                    please use the service attachment's
                    "ConnectedEndpoint.status" as the source of
                    truth.
                FAILED (2):
                    The connection is not functional since some
                    resources on the connection fail to be created.
                CREATING (3):
                    The connection is being created.
                DELETING (4):
                    The connection is being deleted.
                CREATE_REPAIRING (5):
                    The connection is being repaired to complete
                    creation.
                DELETE_REPAIRING (6):
                    The connection is being repaired to complete
                    deletion.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            FAILED = 2
            CREATING = 3
            DELETING = 4
            CREATE_REPAIRING = 5
            DELETE_REPAIRING = 6

        service_attachment_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "ServiceConnectionMap.ConsumerPscConnection.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ServiceConnectionMap.ConsumerPscConnection.State",
        )
        project: str = proto.Field(
            proto.STRING,
            number=3,
        )
        network: str = proto.Field(
            proto.STRING,
            number=4,
        )
        psc_connection_id: str = proto.Field(
            proto.STRING,
            number=5,
        )
        ip: str = proto.Field(
            proto.STRING,
            number=6,
        )
        error_type: "ConnectionErrorType" = proto.Field(
            proto.ENUM,
            number=7,
            enum="ConnectionErrorType",
        )
        error: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=8,
            message=status_pb2.Status,
        )
        gce_operation: str = proto.Field(
            proto.STRING,
            number=9,
        )
        forwarding_rule: str = proto.Field(
            proto.STRING,
            number=10,
        )
        error_info: error_details_pb2.ErrorInfo = proto.Field(
            proto.MESSAGE,
            number=11,
            message=error_details_pb2.ErrorInfo,
        )
        selected_subnetwork: str = proto.Field(
            proto.STRING,
            number=12,
        )
        producer_instance_id: str = proto.Field(
            proto.STRING,
            number=13,
        )
        producer_instance_metadata: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=14,
        )
        ip_version: "IPVersion" = proto.Field(
            proto.ENUM,
            number=15,
            optional=True,
            enum="IPVersion",
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_class: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_class_uri: str = proto.Field(
        proto.STRING,
        number=12,
    )
    infrastructure: "Infrastructure" = proto.Field(
        proto.ENUM,
        number=8,
        enum="Infrastructure",
    )
    producer_psc_configs: MutableSequence[ProducerPscConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=ProducerPscConfig,
    )
    consumer_psc_configs: MutableSequence[ConsumerPscConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=ConsumerPscConfig,
    )
    consumer_psc_connections: MutableSequence[ConsumerPscConnection] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message=ConsumerPscConnection,
        )
    )
    token: str = proto.Field(
        proto.STRING,
        number=13,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )


class ListServiceConnectionMapsRequest(proto.Message):
    r"""Request for ListServiceConnectionMaps.

    Attributes:
        parent (str):
            Required. The parent resource's name. ex.
            projects/123/locations/us-east1
        page_size (int):
            The maximum number of results per page that
            should be returned.
        page_token (str):
            The page token.
        filter (str):
            A filter expression that filters the results
            listed in the response.
        order_by (str):
            Sort the results by a certain order.
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


class ListServiceConnectionMapsResponse(proto.Message):
    r"""Response for ListServiceConnectionMaps.

    Attributes:
        service_connection_maps (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionMap]):
            ServiceConnectionMaps to be returned.
        next_page_token (str):
            The next pagination token in the List response. It should be
            used as page_token for the following request. An empty value
            means no more result.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    service_connection_maps: MutableSequence["ServiceConnectionMap"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ServiceConnectionMap",
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


class GetServiceConnectionMapRequest(proto.Message):
    r"""Request for GetServiceConnectionMap.

    Attributes:
        name (str):
            Required. Name of the ServiceConnectionMap to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceConnectionMapRequest(proto.Message):
    r"""Request for CreateServiceConnectionMap.

    Attributes:
        parent (str):
            Required. The parent resource's name of the
            ServiceConnectionMap. ex.
            projects/123/locations/us-east1
        service_connection_map_id (str):
            Optional. Resource ID (i.e. 'foo' in
            '[...]/projects/p/locations/l/serviceConnectionMaps/foo')
            See https://google.aip.dev/122#resource-id-segments Unique
            per location. If one is not provided, one will be generated.
        service_connection_map (google.cloud.networkconnectivity_v1.types.ServiceConnectionMap):
            Required. Initial values for a new
            ServiceConnectionMaps
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
    service_connection_map_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_connection_map: "ServiceConnectionMap" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServiceConnectionMap",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateServiceConnectionMapRequest(proto.Message):
    r"""Request for UpdateServiceConnectionMap.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ServiceConnectionMap resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        service_connection_map (google.cloud.networkconnectivity_v1.types.ServiceConnectionMap):
            Required. New values to be patched into the
            resource.
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
    service_connection_map: "ServiceConnectionMap" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServiceConnectionMap",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServiceConnectionMapRequest(proto.Message):
    r"""Request for DeleteServiceConnectionMap.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the
            ServiceConnectionMap to delete.
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
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
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
        optional=True,
    )


class ServiceConnectionPolicy(proto.Message):
    r"""The ServiceConnectionPolicy resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Immutable. The name of a ServiceConnectionPolicy. Format:
            projects/{project}/locations/{location}/serviceConnectionPolicies/{service_connection_policy}
            See:
            https://google.aip.dev/122#fields-representing-resource-names
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the
            ServiceConnectionPolicy was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the
            ServiceConnectionPolicy was updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            A description of this resource.
        network (str):
            The resource path of the consumer network.
            Example:

            -
              projects/{projectNumOrId}/global/networks/{resourceId}.
        service_class (str):
            The service class identifier for which this
            ServiceConnectionPolicy is for. The service
            class identifier is a unique, symbolic
            representation of a ServiceClass. It is provided
            by the Service Producer. Google services have a
            prefix of gcp or google-cloud. For example,
            gcp-memorystore-redis or google-cloud-sql. 3rd
            party services do not. For example,
            test-service-a3dfcx.
        infrastructure (google.cloud.networkconnectivity_v1.types.Infrastructure):
            Output only. The type of underlying resources
            used to create the connection.
        psc_config (google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy.PscConfig):
            Configuration used for Private Service
            Connect connections. Used when Infrastructure is
            PSC.
        psc_connections (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy.PscConnection]):
            Output only. [Output only] Information about each Private
            Service Connect connection.
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
    """

    class State(proto.Enum):
        r"""The state of the PSC connection.
        We reserve the right to add more states without notice in the
        future. Users should not use exhaustive switch statements on
        this enum. See https://google.aip.dev/216.

        Values:
            STATE_UNSPECIFIED (0):
                An invalid state as the default case.
            ACTIVE (1):
                The connection has been created successfully.
                However, for the up-to-date connection status,
                please use the created forwarding rule's
                "PscConnectionStatus" as the source of truth.
            FAILED (2):
                The connection is not functional since some
                resources on the connection fail to be created.
            CREATING (3):
                The connection is being created.
            DELETING (4):
                The connection is being deleted.
            CREATE_REPAIRING (5):
                The connection is being repaired to complete
                creation.
            DELETE_REPAIRING (6):
                The connection is being repaired to complete
                deletion.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        FAILED = 2
        CREATING = 3
        DELETING = 4
        CREATE_REPAIRING = 5
        DELETE_REPAIRING = 6

    class PscConfig(proto.Message):
        r"""Configuration used for Private Service Connect connections.
        Used when Infrastructure is PSC.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            subnetworks (MutableSequence[str]):
                The resource paths of subnetworks to use for
                IP address management. Example:

                projects/{projectNumOrId}/regions/{region}/subnetworks/{resourceId}.
            limit (int):
                Optional. Max number of PSC connections for
                this policy.

                This field is a member of `oneof`_ ``_limit``.
            producer_instance_location (google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation):
                Required. ProducerInstanceLocation is used to
                specify which authorization mechanism to use to
                determine which projects the Producer instance
                can be within.
            allowed_google_producers_resource_hierarchy_level (MutableSequence[str]):
                Optional. List of Projects, Folders, or Organizations from
                where the Producer instance can be within. For example, a
                network administrator can provide both 'organizations/foo'
                and 'projects/bar' as
                allowed_google_producers_resource_hierarchy_levels. This
                allowlists this network to connect with any Producer
                instance within the 'foo' organization or the 'bar' project.
                By default,
                allowed_google_producers_resource_hierarchy_level is empty.
                The format for each
                allowed_google_producers_resource_hierarchy_level is / where
                is one of 'projects', 'folders', or 'organizations' and is
                either the ID or the number of the resource type. Format for
                each allowed_google_producers_resource_hierarchy_level
                value: 'projects/<project_id_or_number>' or
                'folders/<folder_id>' or 'organizations/<organization_id>'
                Eg. [projects/my-project-id, projects/567, folders/891,
                organizations/123]
        """

        class ProducerInstanceLocation(proto.Enum):
            r"""ProducerInstanceLocation is used to specify which
            authorization mechanism to use to determine which projects the
            Producer instance can be within.

            Values:
                PRODUCER_INSTANCE_LOCATION_UNSPECIFIED (0):
                    Producer instance location is not specified. When this
                    option is chosen, then the PSC connections created by this
                    ServiceConnectionPolicy must be within the same project as
                    the Producer instance. This is the default
                    ProducerInstanceLocation value. To allow for PSC connections
                    from this network to other networks, use the
                    CUSTOM_RESOURCE_HIERARCHY_LEVELS option.
                CUSTOM_RESOURCE_HIERARCHY_LEVELS (1):
                    Producer instance must be within one of the values provided
                    in allowed_google_producers_resource_hierarchy_level.
            """

            PRODUCER_INSTANCE_LOCATION_UNSPECIFIED = 0
            CUSTOM_RESOURCE_HIERARCHY_LEVELS = 1

        subnetworks: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        limit: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        producer_instance_location: "ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation" = proto.Field(
            proto.ENUM,
            number=3,
            enum="ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation",
        )
        allowed_google_producers_resource_hierarchy_level: MutableSequence[str] = (
            proto.RepeatedField(
                proto.STRING,
                number=4,
            )
        )

    class PscConnection(proto.Message):
        r"""Information about a specific Private Service Connect
        connection.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            state (google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy.State):
                State of the PSC Connection
            consumer_forwarding_rule (str):
                The resource reference of the PSC Forwarding
                Rule within the consumer VPC.
            consumer_address (str):
                The resource reference of the consumer
                address.
            error_type (google.cloud.networkconnectivity_v1.types.ConnectionErrorType):
                The error type indicates whether the error is
                consumer facing, producer facing or system
                internal.
            error (google.rpc.status_pb2.Status):
                The most recent error during operating this connection.
                Deprecated, please use error_info instead.
            gce_operation (str):
                The last Compute Engine operation to setup
                PSC connection.
            consumer_target_project (str):
                The project where the PSC connection is
                created.
            psc_connection_id (str):
                The PSC connection id of the PSC forwarding
                rule.
            error_info (google.rpc.error_details_pb2.ErrorInfo):
                Output only. The error info for the latest
                error during operating this connection.
            selected_subnetwork (str):
                Output only. The URI of the subnetwork
                selected to allocate IP address for this
                connection.
            producer_instance_id (str):
                Immutable. Deprecated. Use producer_instance_metadata
                instead. An immutable identifier for the producer instance.
            producer_instance_metadata (MutableMapping[str, str]):
                Immutable. An immutable map for the producer
                instance metadata.
            service_class (str):
                Output only. [Output only] The service class associated with
                this PSC Connection. The value is derived from the SCPolicy
                and matches the service class name provided by the customer.
            ip_version (google.cloud.networkconnectivity_v1.types.IPVersion):
                The requested IP version for the PSC
                connection.

                This field is a member of `oneof`_ ``_ip_version``.
        """

        state: "ServiceConnectionPolicy.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ServiceConnectionPolicy.State",
        )
        consumer_forwarding_rule: str = proto.Field(
            proto.STRING,
            number=2,
        )
        consumer_address: str = proto.Field(
            proto.STRING,
            number=3,
        )
        error_type: "ConnectionErrorType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="ConnectionErrorType",
        )
        error: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=5,
            message=status_pb2.Status,
        )
        gce_operation: str = proto.Field(
            proto.STRING,
            number=6,
        )
        consumer_target_project: str = proto.Field(
            proto.STRING,
            number=7,
        )
        psc_connection_id: str = proto.Field(
            proto.STRING,
            number=8,
        )
        error_info: error_details_pb2.ErrorInfo = proto.Field(
            proto.MESSAGE,
            number=9,
            message=error_details_pb2.ErrorInfo,
        )
        selected_subnetwork: str = proto.Field(
            proto.STRING,
            number=10,
        )
        producer_instance_id: str = proto.Field(
            proto.STRING,
            number=11,
        )
        producer_instance_metadata: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=12,
        )
        service_class: str = proto.Field(
            proto.STRING,
            number=13,
        )
        ip_version: "IPVersion" = proto.Field(
            proto.ENUM,
            number=14,
            optional=True,
            enum="IPVersion",
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    service_class: str = proto.Field(
        proto.STRING,
        number=7,
    )
    infrastructure: "Infrastructure" = proto.Field(
        proto.ENUM,
        number=8,
        enum="Infrastructure",
    )
    psc_config: PscConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=PscConfig,
    )
    psc_connections: MutableSequence[PscConnection] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=PscConnection,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )


class ListServiceConnectionPoliciesRequest(proto.Message):
    r"""Request for ListServiceConnectionPolicies.

    Attributes:
        parent (str):
            Required. The parent resource's name. ex.
            projects/123/locations/us-east1
        page_size (int):
            The maximum number of results per page that
            should be returned.
        page_token (str):
            The page token.
        filter (str):
            A filter expression that filters the results
            listed in the response.
        order_by (str):
            Sort the results by a certain order.
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


class ListServiceConnectionPoliciesResponse(proto.Message):
    r"""Response for ListServiceConnectionPolicies.

    Attributes:
        service_connection_policies (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy]):
            ServiceConnectionPolicies to be returned.
        next_page_token (str):
            The next pagination token in the List response. It should be
            used as page_token for the following request. An empty value
            means no more result.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    service_connection_policies: MutableSequence["ServiceConnectionPolicy"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ServiceConnectionPolicy",
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


class GetServiceConnectionPolicyRequest(proto.Message):
    r"""Request for GetServiceConnectionPolicy.

    Attributes:
        name (str):
            Required. Name of the ServiceConnectionPolicy
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceConnectionPolicyRequest(proto.Message):
    r"""Request for CreateServiceConnectionPolicy.

    Attributes:
        parent (str):
            Required. The parent resource's name of the
            ServiceConnectionPolicy. ex.
            projects/123/locations/us-east1
        service_connection_policy_id (str):
            Optional. Resource ID (i.e. 'foo' in
            '[...]/projects/p/locations/l/serviceConnectionPolicies/foo')
            See https://google.aip.dev/122#resource-id-segments Unique
            per location.
        service_connection_policy (google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy):
            Required. Initial values for a new
            ServiceConnectionPolicies
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
    service_connection_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_connection_policy: "ServiceConnectionPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServiceConnectionPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateServiceConnectionPolicyRequest(proto.Message):
    r"""Request for UpdateServiceConnectionPolicy.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ServiceConnectionPolicy resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        service_connection_policy (google.cloud.networkconnectivity_v1.types.ServiceConnectionPolicy):
            Required. New values to be patched into the
            resource.
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
    service_connection_policy: "ServiceConnectionPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServiceConnectionPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServiceConnectionPolicyRequest(proto.Message):
    r"""Request for DeleteServiceConnectionPolicy.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the
            ServiceConnectionPolicy to delete.
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
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
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
        optional=True,
    )


class ServiceClass(proto.Message):
    r"""The ServiceClass resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Immutable. The name of a ServiceClass resource. Format:
            projects/{project}/locations/{location}/serviceClasses/{service_class}
            See:
            https://google.aip.dev/122#fields-representing-resource-names
        service_class (str):
            Output only. The generated service class
            name. Use this name to refer to the Service
            class in Service Connection Maps and Service
            Connection Policies.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ServiceClass was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the ServiceClass was
            updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            A description of this resource.
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_class: str = proto.Field(
        proto.STRING,
        number=7,
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


class ListServiceClassesRequest(proto.Message):
    r"""Request for ListServiceClasses.

    Attributes:
        parent (str):
            Required. The parent resource's name. ex.
            projects/123/locations/us-east1
        page_size (int):
            The maximum number of results per page that
            should be returned.
        page_token (str):
            The page token.
        filter (str):
            A filter expression that filters the results
            listed in the response.
        order_by (str):
            Sort the results by a certain order.
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


class ListServiceClassesResponse(proto.Message):
    r"""Response for ListServiceClasses.

    Attributes:
        service_classes (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceClass]):
            ServiceClasses to be returned.
        next_page_token (str):
            The next pagination token in the List response. It should be
            used as page_token for the following request. An empty value
            means no more result.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    service_classes: MutableSequence["ServiceClass"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ServiceClass",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServiceClassRequest(proto.Message):
    r"""Request for GetServiceClass.

    Attributes:
        name (str):
            Required. Name of the ServiceClass to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateServiceClassRequest(proto.Message):
    r"""Request for UpdateServiceClass.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ServiceClass resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        service_class (google.cloud.networkconnectivity_v1.types.ServiceClass):
            Required. New values to be patched into the
            resource.
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
    service_class: "ServiceClass" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServiceClass",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServiceClassRequest(proto.Message):
    r"""Request for DeleteServiceClass.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the ServiceClass to
            delete.
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
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
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
        optional=True,
    )


class ServiceConnectionToken(proto.Message):
    r"""The ServiceConnectionToken resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Immutable. The name of a ServiceConnectionToken. Format:
            projects/{project}/locations/{location}/ServiceConnectionTokens/{service_connection_token}
            See:
            https://google.aip.dev/122#fields-representing-resource-names
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the
            ServiceConnectionToken was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the
            ServiceConnectionToken was updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            A description of this resource.
        network (str):
            The resource path of the network associated
            with this token. Example:

            projects/{projectNumOrId}/global/networks/{resourceId}.
        token (str):
            Output only. The token generated by
            Automation.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time to which this token is
            valid.
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )


class ListServiceConnectionTokensRequest(proto.Message):
    r"""Request for ListServiceConnectionTokens.

    Attributes:
        parent (str):
            Required. The parent resource's name. ex.
            projects/123/locations/us-east1
        page_size (int):
            The maximum number of results per page that
            should be returned.
        page_token (str):
            The page token.
        filter (str):
            A filter expression that filters the results
            listed in the response.
        order_by (str):
            Sort the results by a certain order.
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


class ListServiceConnectionTokensResponse(proto.Message):
    r"""Response for ListServiceConnectionTokens.

    Attributes:
        service_connection_tokens (MutableSequence[google.cloud.networkconnectivity_v1.types.ServiceConnectionToken]):
            ServiceConnectionTokens to be returned.
        next_page_token (str):
            The next pagination token in the List response. It should be
            used as page_token for the following request. An empty value
            means no more result.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    service_connection_tokens: MutableSequence["ServiceConnectionToken"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ServiceConnectionToken",
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


class GetServiceConnectionTokenRequest(proto.Message):
    r"""Request for GetServiceConnectionToken.

    Attributes:
        name (str):
            Required. Name of the ServiceConnectionToken
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceConnectionTokenRequest(proto.Message):
    r"""Request for CreateServiceConnectionToken.

    Attributes:
        parent (str):
            Required. The parent resource's name of the
            ServiceConnectionToken. ex.
            projects/123/locations/us-east1
        service_connection_token_id (str):
            Optional. Resource ID (i.e. 'foo' in
            '[...]/projects/p/locations/l/ServiceConnectionTokens/foo')
            See https://google.aip.dev/122#resource-id-segments Unique
            per location. If one is not provided, one will be generated.
        service_connection_token (google.cloud.networkconnectivity_v1.types.ServiceConnectionToken):
            Required. Initial values for a new
            ServiceConnectionTokens
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
    service_connection_token_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_connection_token: "ServiceConnectionToken" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServiceConnectionToken",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteServiceConnectionTokenRequest(proto.Message):
    r"""Request for DeleteServiceConnectionToken.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the
            ServiceConnectionToken to delete.
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
        etag (str):
            Optional. The etag is computed by the server,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.

            This field is a member of `oneof`_ ``_etag``.
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
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
