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

__protobuf__ = proto.module(
    package="google.cloud.bigquery.datapolicies.v2beta1",
    manifest={
        "CreateDataPolicyRequest",
        "UpdateDataPolicyRequest",
        "AddGranteesRequest",
        "RemoveGranteesRequest",
        "DeleteDataPolicyRequest",
        "GetDataPolicyRequest",
        "ListDataPoliciesRequest",
        "ListDataPoliciesResponse",
        "DataPolicy",
        "DataMaskingPolicy",
    },
)


class CreateDataPolicyRequest(proto.Message):
    r"""Request message for the CreateDataPolicy method.

    Attributes:
        parent (str):
            Required. Resource name of the project that the data policy
            will belong to. The format is
            ``projects/{project_number}/locations/{location_id}``.
        data_policy_id (str):
            Required. User-assigned (human readable) ID of the data
            policy that needs to be unique within a project. Used as
            {data_policy_id} in part of the resource name.
        data_policy (google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy):
            Required. The data policy to create. The ``name`` field does
            not need to be provided for the data policy creation.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_policy: "DataPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataPolicy",
    )


class UpdateDataPolicyRequest(proto.Message):
    r"""Request message for the UpdateDataPolicy method.

    Attributes:
        data_policy (google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy):
            Required. Update the data policy's metadata.

            The target data policy is determined by the ``name`` field.
            Other fields are updated to the specified values based on
            the field masks.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If not set, defaults to all of the fields that are allowed
            to update.

            Updates to the ``name`` and ``dataPolicyId`` fields are not
            allowed.
    """

    data_policy: "DataPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class AddGranteesRequest(proto.Message):
    r"""Request message for the AddGrantees method.

    Attributes:
        data_policy (str):
            Required. Resource name of this data policy, in the format
            of
            ``projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}``.
        grantees (MutableSequence[str]):
            Required. IAM principal that should be granted Fine Grained
            Access to the underlying data goverened by the data policy.
            The target data policy is determined by the ``data_policy``
            field.

            Uses the `IAM V2 principal
            syntax <https://cloud.google.com/iam/docs/principal-identifiers#v2>`__.
            Supported principal types:

            - User
            - Group
            - Service account
    """

    data_policy: str = proto.Field(
        proto.STRING,
        number=1,
    )
    grantees: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class RemoveGranteesRequest(proto.Message):
    r"""Request message for the RemoveGrantees method.

    Attributes:
        data_policy (str):
            Required. Resource name of this data policy, in the format
            of
            ``projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}``.
        grantees (MutableSequence[str]):
            Required. IAM principal that should be revoked from Fine
            Grained Access to the underlying data goverened by the data
            policy. The target data policy is determined by the
            ``data_policy`` field.

            Uses the `IAM V2 principal
            syntax <https://cloud.google.com/iam/docs/principal-identifiers#v2>`__.
            Supported principal types:

            - User
            - Group
            - Service account
    """

    data_policy: str = proto.Field(
        proto.STRING,
        number=1,
    )
    grantees: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class DeleteDataPolicyRequest(proto.Message):
    r"""Request message for the DeleteDataPolicy method.

    Attributes:
        name (str):
            Required. Resource name of the data policy to delete. Format
            is
            ``projects/{project_number}/locations/{location_id}/dataPolicies/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetDataPolicyRequest(proto.Message):
    r"""Request message for the GetDataPolicy method.

    Attributes:
        name (str):
            Required. Resource name of the requested data policy. Format
            is
            ``projects/{project_number}/locations/{location_id}/dataPolicies/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataPoliciesRequest(proto.Message):
    r"""Request message for the ListDataPolicies method.

    Attributes:
        parent (str):
            Required. Resource name of the project for which to list
            data policies. Format is
            ``projects/{project_number}/locations/{location_id}``.
        page_size (int):
            Optional. The maximum number of data policies
            to return. Must be a value between 1 and 1000.
            If not set, defaults to 50.
        page_token (str):
            Optional. The ``nextPageToken`` value returned from a
            previous list request, if any. If not set, defaults to an
            empty string.
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


class ListDataPoliciesResponse(proto.Message):
    r"""Response message for the ListDataPolicies method.

    Attributes:
        data_policies (MutableSequence[google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy]):
            Data policies that belong to the requested
            project.
        next_page_token (str):
            Token used to retrieve the next page of
            results, or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    data_policies: MutableSequence["DataPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DataPolicy(proto.Message):
    r"""Represents the label-policy binding.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_masking_policy (google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy):
            Optional. The data masking policy that specifies the data
            masking rule to use. It must be set if the data policy type
            is DATA_MASKING_POLICY.

            This field is a member of `oneof`_ ``policy``.
        name (str):
            Identifier. Resource name of this data policy, in the format
            of
            ``projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}``.
        data_policy_id (str):
            Output only. User-assigned (human readable) ID of the data
            policy that needs to be unique within a project. Used as
            {data_policy_id} in part of the resource name.
        etag (str):
            The etag for this Data Policy.
            This field is used for UpdateDataPolicy calls.
            If Data Policy exists, this field is required
            and must match the server's etag. It will also
            be populated in the response of GetDataPolicy,
            CreateDataPolicy, and UpdateDataPolicy calls.

            This field is a member of `oneof`_ ``_etag``.
        data_policy_type (google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy.DataPolicyType):
            Required. Type of data policy.
        policy_tag (str):
            Output only. Policy tag resource name, in the format of
            ``projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{policyTag_id}``.
            policy_tag is supported only for V1 data policies.
        grantees (MutableSequence[str]):
            Optional. The list of IAM principals that have Fine Grained
            Access to the underlying data goverened by this data policy.

            Uses the `IAM V2 principal
            syntax <https://cloud.google.com/iam/docs/principal-identifiers#v2>`__
            Only supports principal types users, groups,
            serviceaccounts, cloudidentity. This field is supported in
            V2 Data Policy only. In case of V1 data policies (i.e.
            verion = 1 and policy_tag is set), this field is not
            populated.
        version (google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy.Version):
            Output only. The version of the Data Policy
            resource.
    """

    class DataPolicyType(proto.Enum):
        r"""A list of supported data policy types.

        Values:
            DATA_POLICY_TYPE_UNSPECIFIED (0):
                Default value for the data policy type. This
                should not be used.
            DATA_MASKING_POLICY (1):
                Used to create a data policy for data
                masking.
            RAW_DATA_ACCESS_POLICY (2):
                Used to create a data policy for raw data
                access.
        """

        DATA_POLICY_TYPE_UNSPECIFIED = 0
        DATA_MASKING_POLICY = 1
        RAW_DATA_ACCESS_POLICY = 2

    class Version(proto.Enum):
        r"""The supported versions for the Data Policy resource.

        Values:
            VERSION_UNSPECIFIED (0):
                Default value for the data policy version.
                This should not be used.
            V1 (1):
                V1 data policy version. V1 Data Policies will
                be present in V2 List api response, but can not
                be created/updated/deleted from V2 api.
            V2 (2):
                V2 data policy version.
        """

        VERSION_UNSPECIFIED = 0
        V1 = 1
        V2 = 2

    data_masking_policy: "DataMaskingPolicy" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="policy",
        message="DataMaskingPolicy",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    data_policy_type: DataPolicyType = proto.Field(
        proto.ENUM,
        number=3,
        enum=DataPolicyType,
    )
    policy_tag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    grantees: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    version: Version = proto.Field(
        proto.ENUM,
        number=9,
        enum=Version,
    )


class DataMaskingPolicy(proto.Message):
    r"""The policy used to specify data masking rule.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        predefined_expression (google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy.PredefinedExpression):
            Optional. A predefined masking expression.

            This field is a member of `oneof`_ ``masking_expression``.
    """

    class PredefinedExpression(proto.Enum):
        r"""The available masking rules. Learn more here:
        https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options.

        Values:
            PREDEFINED_EXPRESSION_UNSPECIFIED (0):
                Default, unspecified predefined expression.
                No masking will take place since no expression
                is specified.
            SHA256 (1):
                Masking expression to replace data with
                SHA-256 hash.
            ALWAYS_NULL (2):
                Masking expression to replace data with
                NULLs.
            DEFAULT_MASKING_VALUE (3):
                Masking expression to replace data with their default
                masking values. The default masking values for each type
                listed as below:

                - STRING: ""
                - BYTES: b''
                - INTEGER: 0
                - FLOAT: 0.0
                - NUMERIC: 0
                - BOOLEAN: FALSE
                - TIMESTAMP: 1970-01-01 00:00:00 UTC
                - DATE: 1970-01-01
                - TIME: 00:00:00
                - DATETIME: 1970-01-01T00:00:00
                - GEOGRAPHY: POINT(0 0)
                - BIGNUMERIC: 0
                - ARRAY: []
                - STRUCT: NOT_APPLICABLE
                - JSON: NULL
        """

        PREDEFINED_EXPRESSION_UNSPECIFIED = 0
        SHA256 = 1
        ALWAYS_NULL = 2
        DEFAULT_MASKING_VALUE = 3

    predefined_expression: PredefinedExpression = proto.Field(
        proto.ENUM,
        number=1,
        oneof="masking_expression",
        enum=PredefinedExpression,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
