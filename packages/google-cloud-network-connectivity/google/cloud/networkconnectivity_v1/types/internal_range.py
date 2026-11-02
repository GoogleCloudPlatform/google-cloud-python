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
        "InternalRange",
        "ListInternalRangesRequest",
        "ListInternalRangesResponse",
        "GetInternalRangeRequest",
        "CreateInternalRangeRequest",
        "UpdateInternalRangeRequest",
        "DeleteInternalRangeRequest",
    },
)


class InternalRange(proto.Message):
    r"""The internal range resource for IPAM operations within a VPC
    network. Used to represent a private address range along with
    behavioral characteristics of that range (its usage and peering
    behavior). Networking resources can link to this range if they
    are created as belonging to it.

    Attributes:
        name (str):
            Identifier. The name of an internal range. Format:
            projects/{project}/locations/{location}/internalRanges/{internal_range}
            See:
            https://google.aip.dev/122#fields-representing-resource-names
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the internal range was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the internal range was
            updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            Optional. A description of this resource.
        ip_cidr_range (str):
            Optional. The IP range that this internal range defines.
            NOTE: IPv6 ranges are limited to usage=EXTERNAL_TO_VPC and
            peering=FOR_SELF. NOTE: For IPv6 Ranges this field is
            compulsory, i.e. the address range must be specified
            explicitly.
        network (str):
            Immutable. The URL or resource ID of the
            network in which to reserve the internal range.
            The network cannot be deleted if there are any
            reserved internal ranges referring to it. Legacy
            networks are not supported. For example:

            https://www.googleapis.com/compute/v1/projects/{project}/locations/global/networks/{network}
            projects/{project}/locations/global/networks/{network}
            {network}
        usage (google.cloud.networkconnectivity_v1.types.InternalRange.Usage):
            Optional. The type of usage set for this
            InternalRange.
        peering (google.cloud.networkconnectivity_v1.types.InternalRange.Peering):
            Optional. The type of peering set for this
            internal range.
        prefix_length (int):
            Optional. An alternate to ip_cidr_range. Can be set when
            trying to create an IPv4 reservation that automatically
            finds a free range of the given size. If both ip_cidr_range
            and prefix_length are set, there is an error if the range
            sizes do not match. Can also be used during updates to
            change the range size. NOTE: For IPv6 this field only works
            if ip_cidr_range is set as well, and both fields must match.
            In other words, with IPv6 this field only works as a
            redundant parameter.
        target_cidr_range (MutableSequence[str]):
            Optional. Can be set to narrow down or pick a different
            address space while searching for a free range. If not set,
            defaults to the ["10.0.0.0/8", "172.16.0.0/12",
            "192.168.0.0/16"] address space (for auto-mode networks, the
            "10.0.0.0/9" range is used instead of "10.0.0.0/8"). This
            can be used to target the search in other rfc-1918 address
            spaces like "172.16.0.0/12" and "192.168.0.0/16" or
            non-rfc-1918 address spaces used in the VPC.
        users (MutableSequence[str]):
            Output only. The list of resources that refer
            to this internal range. Resources that use the
            internal range for their range allocation are
            referred to as users of the range. Other
            resources mark themselves as users while doing
            so by creating a reference to this internal
            range. Having a user, based on this reference,
            prevents deletion of the internal range referred
            to. Can be empty.
        overlaps (MutableSequence[google.cloud.networkconnectivity_v1.types.InternalRange.Overlap]):
            Optional. Types of resources that are allowed
            to overlap with the current internal range.
        migration (google.cloud.networkconnectivity_v1.types.InternalRange.Migration):
            Optional. Must be present if usage is set to FOR_MIGRATION.
        immutable (bool):
            Optional. Immutable ranges cannot have their
            fields modified, except for labels and
            description.
        allocation_options (google.cloud.networkconnectivity_v1.types.InternalRange.AllocationOptions):
            Optional. Range auto-allocation options, may be set only
            when auto-allocation is selected by not setting
            ip_cidr_range (and setting prefix_length).
        exclude_cidr_ranges (MutableSequence[str]):
            Optional. ExcludeCidrRanges flag. Specifies a
            set of CIDR blocks that allows exclusion of
            particular CIDR ranges from the auto-allocation
            process, without having to reserve these blocks
    """

    class Usage(proto.Enum):
        r"""Possible usage of an internal range.

        Values:
            USAGE_UNSPECIFIED (0):
                Unspecified usage is allowed in calls which
                identify the resource by other fields and do not
                need Usage set to complete. These are, i.e.:

                GetInternalRange and DeleteInternalRange.
                Usage needs to be specified explicitly in
                CreateInternalRange or UpdateInternalRange
                calls.
            FOR_VPC (1):
                A VPC resource can use the reserved CIDR block by
                associating it with the internal range resource if usage is
                set to FOR_VPC.
            EXTERNAL_TO_VPC (2):
                Ranges created with EXTERNAL_TO_VPC cannot be associated
                with VPC resources and are meant to block out address ranges
                for various use cases, like for example, usage on-prem, with
                dynamic route announcements via interconnect.
            FOR_MIGRATION (3):
                Ranges created FOR_MIGRATION can be used to lock a CIDR
                range between a source and target subnet. If usage is set to
                FOR_MIGRATION, the peering value has to be set to FOR_SELF
                or default to FOR_SELF when unset.
        """

        USAGE_UNSPECIFIED = 0
        FOR_VPC = 1
        EXTERNAL_TO_VPC = 2
        FOR_MIGRATION = 3

    class Peering(proto.Enum):
        r"""Peering type.

        Values:
            PEERING_UNSPECIFIED (0):
                If Peering is left unspecified in CreateInternalRange or
                UpdateInternalRange, it will be defaulted to FOR_SELF.
            FOR_SELF (1):
                This is the default behavior and represents
                the case that this internal range is intended to
                be used in the VPC in which it is created and is
                accessible from its peers. This implies that
                peers or peers-of-peers cannot use this range.
            FOR_PEER (2):
                This behavior can be set when the internal
                range is being reserved for usage by peers. This
                means that no resource within the VPC in which
                it is being created can use this to associate
                with a VPC resource, but one of the peers can.
                This represents donating a range for peers to
                use.
            NOT_SHARED (3):
                This behavior can be set when the internal range is being
                reserved for usage by the VPC in which it is created, but
                not shared with peers. In a sense, it is local to the VPC.
                This can be used to create internal ranges for various
                purposes like HTTP_INTERNAL_LOAD_BALANCER or for
                Interconnect routes that are not shared with peers. This
                also implies that peers cannot use this range in a way that
                is visible to this VPC, but can re-use this range as long as
                it is NOT_SHARED from the peer VPC, too.
        """

        PEERING_UNSPECIFIED = 0
        FOR_SELF = 1
        FOR_PEER = 2
        NOT_SHARED = 3

    class Overlap(proto.Enum):
        r"""Overlap specifications.

        Values:
            OVERLAP_UNSPECIFIED (0):
                No overlap overrides.
            OVERLAP_ROUTE_RANGE (1):
                Allow creation of static routes more specific
                that the current internal range.
            OVERLAP_EXISTING_SUBNET_RANGE (2):
                Allow creation of internal ranges that
                overlap with existing subnets.
        """

        OVERLAP_UNSPECIFIED = 0
        OVERLAP_ROUTE_RANGE = 1
        OVERLAP_EXISTING_SUBNET_RANGE = 2

    class AllocationStrategy(proto.Enum):
        r"""Enumeration of range auto-allocation strategies

        Values:
            ALLOCATION_STRATEGY_UNSPECIFIED (0):
                Unspecified is the only valid option when the range is
                specified explicitly by ip_cidr_range field. Otherwise
                unspefified means using the default strategy.
            RANDOM (1):
                Random strategy, the legacy algorithm, used
                for backwards compatibility. This allocation
                strategy remains efficient in the case of
                concurrent allocation requests in the same
                peered network space and doesn't require
                providing the level of concurrency in an
                explicit parameter, but it is prone to
                fragmenting available address space.
            FIRST_AVAILABLE (2):
                Pick the first available address range. This
                strategy is deterministic and the result is easy
                to predict.
            RANDOM_FIRST_N_AVAILABLE (3):
                Pick an arbitrary range out of the first N available ones.
                The N will be set in the first_available_ranges_lookup_size
                field. This strategy should be used when concurrent
                allocation requests are made in the same space of peered
                networks while the fragmentation of the addrress space is
                reduced.
            FIRST_SMALLEST_FITTING (4):
                Pick the smallest but fitting available
                range. This deterministic strategy minimizes
                fragmentation of the address space.
        """

        ALLOCATION_STRATEGY_UNSPECIFIED = 0
        RANDOM = 1
        FIRST_AVAILABLE = 2
        RANDOM_FIRST_N_AVAILABLE = 3
        FIRST_SMALLEST_FITTING = 4

    class Migration(proto.Message):
        r"""Specification for migration with source and target resource
        names.

        Attributes:
            source (str):
                Immutable. Resource path as an URI of the
                source resource, for example a subnet. The
                project for the source resource should match the
                project for the InternalRange. An example:

                /projects/{project}/regions/{region}/subnetworks/{subnet}
            target (str):
                Immutable. Resource path of the target
                resource. The target project can be different,
                as in the cases when migrating to peer networks.
                For example:

                /projects/{project}/regions/{region}/subnetworks/{subnet}
        """

        source: str = proto.Field(
            proto.STRING,
            number=1,
        )
        target: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AllocationOptions(proto.Message):
        r"""Range auto-allocation options, to be optionally used when
        CIDR block is not explicitly set.

        Attributes:
            allocation_strategy (google.cloud.networkconnectivity_v1.types.InternalRange.AllocationStrategy):
                Optional. Allocation strategy Not setting
                this field when the allocation is requested
                means an implementation defined strategy is
                used.
            first_available_ranges_lookup_size (int):
                Optional. This field must be set only when
                allocation_strategy is set to RANDOM_FIRST_N_AVAILABLE. The
                value should be the maximum expected parallelism of range
                creation requests issued to the same space of peered
                netwroks.
        """

        allocation_strategy: "InternalRange.AllocationStrategy" = proto.Field(
            proto.ENUM,
            number=1,
            enum="InternalRange.AllocationStrategy",
        )
        first_available_ranges_lookup_size: int = proto.Field(
            proto.INT32,
            number=2,
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
    ip_cidr_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    network: str = proto.Field(
        proto.STRING,
        number=7,
    )
    usage: Usage = proto.Field(
        proto.ENUM,
        number=8,
        enum=Usage,
    )
    peering: Peering = proto.Field(
        proto.ENUM,
        number=9,
        enum=Peering,
    )
    prefix_length: int = proto.Field(
        proto.INT32,
        number=10,
    )
    target_cidr_range: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    users: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    overlaps: MutableSequence[Overlap] = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum=Overlap,
    )
    migration: Migration = proto.Field(
        proto.MESSAGE,
        number=14,
        message=Migration,
    )
    immutable: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    allocation_options: AllocationOptions = proto.Field(
        proto.MESSAGE,
        number=16,
        message=AllocationOptions,
    )
    exclude_cidr_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )


class ListInternalRangesRequest(proto.Message):
    r"""Request for InternalRangeService.ListInternalRanges

    Attributes:
        parent (str):
            Required. The parent resource's name.
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


class ListInternalRangesResponse(proto.Message):
    r"""Response for InternalRange.ListInternalRanges

    Attributes:
        internal_ranges (MutableSequence[google.cloud.networkconnectivity_v1.types.InternalRange]):
            Internal ranges to be returned.
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

    internal_ranges: MutableSequence["InternalRange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InternalRange",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInternalRangeRequest(proto.Message):
    r"""Request for InternalRangeService.GetInternalRange

    Attributes:
        name (str):
            Required. Name of the InternalRange to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInternalRangeRequest(proto.Message):
    r"""Request for InternalRangeService.CreateInternalRange

    Attributes:
        parent (str):
            Required. The parent resource's name of the
            internal range.
        internal_range_id (str):
            Optional. Resource ID (i.e. 'foo' in
            '[...]/projects/p/locations/l/internalRanges/foo') See
            https://google.aip.dev/122#resource-id-segments Unique per
            location.
        internal_range (google.cloud.networkconnectivity_v1.types.InternalRange):
            Required. Initial values for a new internal
            range
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
    internal_range_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    internal_range: "InternalRange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InternalRange",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInternalRangeRequest(proto.Message):
    r"""Request for InternalRangeService.UpdateInternalRange

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the InternalRange resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        internal_range (google.cloud.networkconnectivity_v1.types.InternalRange):
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
    internal_range: "InternalRange" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InternalRange",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInternalRangeRequest(proto.Message):
    r"""Request for InternalRangeService.DeleteInternalRange

    Attributes:
        name (str):
            Required. The name of the internal range to
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
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
