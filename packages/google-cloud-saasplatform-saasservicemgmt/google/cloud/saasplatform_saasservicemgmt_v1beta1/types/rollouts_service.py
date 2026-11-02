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

from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import rollouts_resources

__protobuf__ = proto.module(
    package="google.cloud.saasplatform.saasservicemgmt.v1beta1",
    manifest={
        "ListRolloutsRequest",
        "ListRolloutsResponse",
        "GetRolloutRequest",
        "CreateRolloutRequest",
        "UpdateRolloutRequest",
        "DeleteRolloutRequest",
        "ListRolloutKindsRequest",
        "ListRolloutKindsResponse",
        "GetRolloutKindRequest",
        "CreateRolloutKindRequest",
        "UpdateRolloutKindRequest",
        "DeleteRolloutKindRequest",
    },
)


class ListRolloutsRequest(proto.Message):
    r"""The request structure for the ListRollouts method.

    Attributes:
        parent (str):
            Required. The parent of the rollout.
        page_size (int):
            The maximum number of rollouts to send per
            page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListRolloutsResponse(proto.Message):
    r"""The response structure for the ListRollouts method.

    Attributes:
        rollouts (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout]):
            The resulting rollouts.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListRollouts call to
            list the next page. If empty, there are no more
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    rollouts: MutableSequence[rollouts_resources.Rollout] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message=rollouts_resources.Rollout,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetRolloutRequest(proto.Message):
    r"""The request structure for the GetRollout method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateRolloutRequest(proto.Message):
    r"""The request structure for the CreateRollout method.

    Attributes:
        parent (str):
            Required. The parent of the rollout.
        rollout_id (str):
            Required. The ID value for the new rollout.
        rollout (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout):
            Required. The desired state for the rollout.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
        number=10006,
    )
    rollout_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    rollout: rollouts_resources.Rollout = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=rollouts_resources.Rollout,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateRolloutRequest(proto.Message):
    r"""The request structure for the UpdateRollout method.

    Attributes:
        rollout (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout):
            Required. The desired state for the rollout.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Rollout resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            Rollout will be overwritten.
    """

    rollout: rollouts_resources.Rollout = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=rollouts_resources.Rollout,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRolloutRequest(proto.Message):
    r"""The request structure for the DeleteRollout method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            rollout. This is used with state-changing methods to prevent
            accidental overwrites when multiple user agents might be
            acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the rollout. The Any wildcard (``*``)
            requires that the resource must already exists, and the Not
            Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class ListRolloutKindsRequest(proto.Message):
    r"""The request structure for the ListRolloutKinds method.

    Attributes:
        parent (str):
            Required. The parent of the rollout kind.
        page_size (int):
            The maximum number of rollout kinds to send
            per page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListRolloutKindsResponse(proto.Message):
    r"""The response structure for the ListRolloutKinds method.

    Attributes:
        rollout_kinds (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind]):
            The resulting rollout kinds.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListRolloutKinds call
            to list the next page. If empty, there are no
            more pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    rollout_kinds: MutableSequence[rollouts_resources.RolloutKind] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10509,
            message=rollouts_resources.RolloutKind,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetRolloutKindRequest(proto.Message):
    r"""The request structure for the GetRolloutKind method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateRolloutKindRequest(proto.Message):
    r"""The request structure for the CreateRolloutKind method.

    Attributes:
        parent (str):
            Required. The parent of the rollout kind.
        rollout_kind_id (str):
            Required. The ID value for the new rollout
            kind.
        rollout_kind (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind):
            Required. The desired state for the rollout
            kind.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
        number=10006,
    )
    rollout_kind_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    rollout_kind: rollouts_resources.RolloutKind = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=rollouts_resources.RolloutKind,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateRolloutKindRequest(proto.Message):
    r"""The request structure for the UpdateRolloutKind method.

    Attributes:
        rollout_kind (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind):
            Required. The desired state for the rollout
            kind.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the RolloutKind resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            RolloutKind will be overwritten.
    """

    rollout_kind: rollouts_resources.RolloutKind = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=rollouts_resources.RolloutKind,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRolloutKindRequest(proto.Message):
    r"""The request structure for the DeleteRolloutKind method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            rollout kind. This is used with state-changing methods to
            prevent accidental overwrites when multiple user agents
            might be acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the rollout kind. The Any wildcard
            (``*``) requires that the resource must already exists, and
            the Not Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
