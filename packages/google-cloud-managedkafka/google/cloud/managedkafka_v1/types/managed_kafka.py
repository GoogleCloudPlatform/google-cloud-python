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

from google.cloud.managedkafka_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.managedkafka.v1",
    manifest={
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "DeleteClusterRequest",
        "ListTopicsRequest",
        "ListTopicsResponse",
        "GetTopicRequest",
        "CreateTopicRequest",
        "UpdateTopicRequest",
        "DeleteTopicRequest",
        "ListConsumerGroupsRequest",
        "ListConsumerGroupsResponse",
        "GetConsumerGroupRequest",
        "UpdateConsumerGroupRequest",
        "DeleteConsumerGroupRequest",
        "ListAclsRequest",
        "ListAclsResponse",
        "GetAclRequest",
        "CreateAclRequest",
        "UpdateAclRequest",
        "DeleteAclRequest",
        "AddAclEntryRequest",
        "AddAclEntryResponse",
        "RemoveAclEntryRequest",
        "RemoveAclEntryResponse",
    },
)


class ListClustersRequest(proto.Message):
    r"""Request for ListClusters.

    Attributes:
        parent (str):
            Required. The parent location whose clusters are to be
            listed. Structured like
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of clusters to
            return. The service may return fewer than this
            value. If unspecified, server will pick an
            appropriate default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListClusters`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListClusters`` must match the call that provided the page
            token.
        filter (str):
            Optional. Filter expression for the result.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListClustersResponse(proto.Message):
    r"""Response for ListClusters.

    Attributes:
        clusters (MutableSequence[google.cloud.managedkafka_v1.types.Cluster]):
            The list of Clusters in the requested parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page of results. If this field is omitted, there are no
            more results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence[resources.Cluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Cluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClusterRequest(proto.Message):
    r"""Request for GetCluster.

    Attributes:
        name (str):
            Required. The name of the cluster whose
            configuration to return.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClusterRequest(proto.Message):
    r"""Request for CreateCluster.

    Attributes:
        parent (str):
            Required. The parent region in which to create the cluster.
            Structured like ``projects/{project}/locations/{location}``.
        cluster_id (str):
            Required. The ID to use for the cluster, which will become
            the final component of the cluster's name. The ID must be
            1-63 characters long, and match the regular expression
            ``[a-z]([-a-z0-9]*[a-z0-9])?`` to comply with RFC 1035.

            This value is structured like: ``my-cluster-id``.
        cluster (google.cloud.managedkafka_v1.types.Cluster):
            Required. Configuration of the cluster to create. Its
            ``name`` field is ignored.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID to avoid
            duplication of requests. If a request times out
            or fails, retrying with the same ID allows the
            server to recognize the previous attempt. For at
            least 60 minutes, the server ignores duplicate
            requests bearing the same ID.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID within 60 minutes of the last request, the
            server checks if an original operation with the
            same request ID was received. If so, the server
            ignores the second request.

            The request ID must be a valid UUID. A zero UUID
            is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateClusterRequest(proto.Message):
    r"""Request for UpdateCluster.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the cluster resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The mask is required and a value of \*
            will update all fields.
        cluster (google.cloud.managedkafka_v1.types.Cluster):
            Required. The cluster to update. Its ``name`` field must be
            populated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID to avoid
            duplication of requests. If a request times out
            or fails, retrying with the same ID allows the
            server to recognize the previous attempt. For at
            least 60 minutes, the server ignores duplicate
            requests bearing the same ID.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID within 60 minutes of the last request, the
            server checks if an original operation with the
            same request ID was received. If so, the server
            ignores the second request.

            The request ID must be a valid UUID. A zero UUID
            is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteClusterRequest(proto.Message):
    r"""Request for DeleteCluster.

    Attributes:
        name (str):
            Required. The name of the cluster to delete.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID to avoid
            duplication of requests. If a request times out
            or fails, retrying with the same ID allows the
            server to recognize the previous attempt. For at
            least 60 minutes, the server ignores duplicate
            requests bearing the same ID.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID within 60 minutes of the last request, the
            server checks if an original operation with the
            same request ID was received. If so, the server
            ignores the second request.

            The request ID must be a valid UUID. A zero UUID
            is not supported
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


class ListTopicsRequest(proto.Message):
    r"""Request for ListTopics.

    Attributes:
        parent (str):
            Required. The parent cluster whose topics are to be listed.
            Structured like
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        page_size (int):
            Optional. The maximum number of topics to
            return. The service may return fewer than this
            value. If unset or zero, all topics for the
            parent is returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTopics`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListTopics`` must match the call that provided the page
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


class ListTopicsResponse(proto.Message):
    r"""Response for ListTopics.

    Attributes:
        topics (MutableSequence[google.cloud.managedkafka_v1.types.Topic]):
            The list of topics in the requested parent.
            The order of the topics is unspecified.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page of results. If this field is omitted, there are no
            more results.
    """

    @property
    def raw_page(self):
        return self

    topics: MutableSequence[resources.Topic] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Topic,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTopicRequest(proto.Message):
    r"""Request for GetTopic.

    Attributes:
        name (str):
            Required. The name of the topic whose
            configuration to return. Structured like:

            projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTopicRequest(proto.Message):
    r"""Request for CreateTopic.

    Attributes:
        parent (str):
            Required. The parent cluster in which to create the topic.
            Structured like
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        topic_id (str):
            Required. The ID to use for the topic, which will become the
            final component of the topic's name.

            This value is structured like: ``my-topic-name``.
        topic (google.cloud.managedkafka_v1.types.Topic):
            Required. Configuration of the topic to create. Its ``name``
            field is ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    topic_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    topic: resources.Topic = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Topic,
    )


class UpdateTopicRequest(proto.Message):
    r"""Request for UpdateTopic.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Topic resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. The mask is required and a value of \* will
            update all fields.
        topic (google.cloud.managedkafka_v1.types.Topic):
            Required. The topic to update. Its ``name`` field must be
            populated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    topic: resources.Topic = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Topic,
    )


class DeleteTopicRequest(proto.Message):
    r"""Request for DeleteTopic.

    Attributes:
        name (str):
            Required. The name of the topic to delete.
            ``projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConsumerGroupsRequest(proto.Message):
    r"""Request for ListConsumerGroups.

    Attributes:
        parent (str):
            Required. The parent cluster whose consumer groups are to be
            listed. Structured like
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        page_size (int):
            Optional. The maximum number of consumer
            groups to return. The service may return fewer
            than this value. If unset or zero, all consumer
            groups for the parent is returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListConsumerGroups`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListConsumerGroups`` must match the call that provided the
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


class ListConsumerGroupsResponse(proto.Message):
    r"""Response for ListConsumerGroups.

    Attributes:
        consumer_groups (MutableSequence[google.cloud.managedkafka_v1.types.ConsumerGroup]):
            The list of consumer group in the requested
            parent. The order of the consumer groups is
            unspecified.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page of results. If this field is omitted, there are no
            more results.
    """

    @property
    def raw_page(self):
        return self

    consumer_groups: MutableSequence[resources.ConsumerGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.ConsumerGroup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetConsumerGroupRequest(proto.Message):
    r"""Request for GetConsumerGroup.

    Attributes:
        name (str):
            Required. The name of the consumer group whose configuration
            to return.
            ``projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateConsumerGroupRequest(proto.Message):
    r"""Request for UpdateConsumerGroup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ConsumerGroup resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The mask is required and a value of \*
            will update all fields.
        consumer_group (google.cloud.managedkafka_v1.types.ConsumerGroup):
            Required. The consumer group to update. Its ``name`` field
            must be populated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    consumer_group: resources.ConsumerGroup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.ConsumerGroup,
    )


class DeleteConsumerGroupRequest(proto.Message):
    r"""Request for DeleteConsumerGroup.

    Attributes:
        name (str):
            Required. The name of the consumer group to delete.
            ``projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAclsRequest(proto.Message):
    r"""Request for ListAcls.

    Attributes:
        parent (str):
            Required. The parent cluster whose acls are to be listed.
            Structured like
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        page_size (int):
            Optional. The maximum number of acls to
            return. The service may return fewer than this
            value. If unset or zero, all acls for the parent
            is returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAcls`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListAcls`` must match the call that provided the page
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


class ListAclsResponse(proto.Message):
    r"""Response for ListAcls.

    Attributes:
        acls (MutableSequence[google.cloud.managedkafka_v1.types.Acl]):
            The list of acls in the requested parent. The
            order of the acls is unspecified.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page of results. If this field is omitted, there are no
            more results.
    """

    @property
    def raw_page(self):
        return self

    acls: MutableSequence[resources.Acl] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Acl,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAclRequest(proto.Message):
    r"""Request for GetAcl.

    Attributes:
        name (str):
            Required. The name of the acl to return. Structured like:
            ``projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}``.

            The structure of ``acl_id`` defines the Resource Pattern
            (resource_type, resource_name, pattern_type) of the acl. See
            ``Acl.name`` for details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAclRequest(proto.Message):
    r"""Request for CreateAcl.

    Attributes:
        parent (str):
            Required. The parent cluster in which to create the acl.
            Structured like
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        acl_id (str):
            Required. The ID to use for the acl, which will become the
            final component of the acl's name. The structure of
            ``acl_id`` defines the Resource Pattern (resource_type,
            resource_name, pattern_type) of the acl. ``acl_id`` is
            structured like one of the following:

            For acls on the cluster: ``cluster``

            For acls on a single resource within the cluster:
            ``topic/{resource_name}`` ``consumerGroup/{resource_name}``
            ``transactionalId/{resource_name}``

            For acls on all resources that match a prefix:
            ``topicPrefixed/{resource_name}``
            ``consumerGroupPrefixed/{resource_name}``
            ``transactionalIdPrefixed/{resource_name}``

            For acls on all resources of a given type (i.e. the wildcard
            literal "\*"): ``allTopics`` (represents ``topic/*``)
            ``allConsumerGroups`` (represents ``consumerGroup/*``)
            ``allTransactionalIds`` (represents ``transactionalId/*``)
        acl (google.cloud.managedkafka_v1.types.Acl):
            Required. Configuration of the acl to create. Its ``name``
            field is ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    acl: resources.Acl = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Acl,
    )


class UpdateAclRequest(proto.Message):
    r"""Request for UpdateAcl.

    Attributes:
        acl (google.cloud.managedkafka_v1.types.Acl):
            Required. The updated acl. Its ``name`` and ``etag`` fields
            must be populated. ``acl_entries`` must not be empty in the
            updated acl; to remove all acl entries for an acl, use
            DeleteAcl.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Acl resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask.
    """

    acl: resources.Acl = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Acl,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAclRequest(proto.Message):
    r"""Request for DeleteAcl.

    Attributes:
        name (str):
            Required. The name of the acl to delete. Structured like:
            ``projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}``.

            The structure of ``acl_id`` defines the Resource Pattern
            (resource_type, resource_name, pattern_type) of the acl. See
            ``Acl.name`` for details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AddAclEntryRequest(proto.Message):
    r"""Request for AddAclEntry.

    Attributes:
        acl (str):
            Required. The name of the acl to add the acl entry to.
            Structured like:
            ``projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}``.

            The structure of ``acl_id`` defines the Resource Pattern
            (resource_type, resource_name, pattern_type) of the acl. See
            ``Acl.name`` for details.
        acl_entry (google.cloud.managedkafka_v1.types.AclEntry):
            Required. The acl entry to add.
    """

    acl: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_entry: resources.AclEntry = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AclEntry,
    )


class AddAclEntryResponse(proto.Message):
    r"""Response for AddAclEntry.

    Attributes:
        acl (google.cloud.managedkafka_v1.types.Acl):
            The updated acl.
        acl_created (bool):
            Whether the acl was created as a result of
            adding the acl entry.
    """

    acl: resources.Acl = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Acl,
    )
    acl_created: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class RemoveAclEntryRequest(proto.Message):
    r"""Request for RemoveAclEntry.

    Attributes:
        acl (str):
            Required. The name of the acl to remove the acl entry from.
            Structured like:
            ``projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}``.

            The structure of ``acl_id`` defines the Resource Pattern
            (resource_type, resource_name, pattern_type) of the acl. See
            ``Acl.name`` for details.
        acl_entry (google.cloud.managedkafka_v1.types.AclEntry):
            Required. The acl entry to remove.
    """

    acl: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_entry: resources.AclEntry = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AclEntry,
    )


class RemoveAclEntryResponse(proto.Message):
    r"""Response for RemoveAclEntry.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        acl (google.cloud.managedkafka_v1.types.Acl):
            The updated acl. Returned if the removed acl
            entry was not the last entry in the acl.

            This field is a member of `oneof`_ ``result``.
        acl_deleted (bool):
            Returned with value true if the removed acl
            entry was the last entry in the acl, resulting
            in acl deletion.

            This field is a member of `oneof`_ ``result``.
    """

    acl: resources.Acl = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="result",
        message=resources.Acl,
    )
    acl_deleted: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="result",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
