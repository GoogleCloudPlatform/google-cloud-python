# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gapic.schema import wrappers

MIXINS_MAP = {
    "DeleteOperation": wrappers.MixinMethod(
        "DeleteOperation",
        request_type="operations_pb2.DeleteOperationRequest",
        response_type="None",
        rpc_name="google.longrunning.Operations/DeleteOperation",
    ),
    "WaitOperation": wrappers.MixinMethod(
        "WaitOperation",
        request_type="operations_pb2.WaitOperationRequest",
        response_type="operations_pb2.Operation",
        rpc_name="google.longrunning.Operations/WaitOperation",
    ),
    "ListOperations": wrappers.MixinMethod(
        "ListOperations",
        request_type="operations_pb2.ListOperationsRequest",
        response_type="operations_pb2.ListOperationsResponse",
        rpc_name="google.longrunning.Operations/ListOperations",
    ),
    "CancelOperation": wrappers.MixinMethod(
        "CancelOperation",
        request_type="operations_pb2.CancelOperationRequest",
        response_type="None",
        rpc_name="google.longrunning.Operations/CancelOperation",
    ),
    "GetOperation": wrappers.MixinMethod(
        "GetOperation",
        request_type="operations_pb2.GetOperationRequest",
        response_type="operations_pb2.Operation",
        rpc_name="google.longrunning.Operations/GetOperation",
    ),
    "TestIamPermissions": wrappers.MixinMethod(
        "TestIamPermissions",
        request_type="iam_policy_pb2.TestIamPermissionsRequest",
        response_type="iam_policy_pb2.TestIamPermissionsResponse",
        rpc_name="google.iam.v1.IAMPolicy/TestIamPermissions",
    ),
    "GetIamPolicy": wrappers.MixinMethod(
        "GetIamPolicy",
        request_type="iam_policy_pb2.GetIamPolicyRequest",
        response_type="policy_pb2.Policy",
        rpc_name="google.iam.v1.IAMPolicy/GetIamPolicy",
    ),
    "SetIamPolicy": wrappers.MixinMethod(
        "SetIamPolicy",
        request_type="iam_policy_pb2.SetIamPolicyRequest",
        response_type="policy_pb2.Policy",
        rpc_name="google.iam.v1.IAMPolicy/SetIamPolicy",
    ),
    "ListLocations": wrappers.MixinMethod(
        "ListLocations",
        request_type="locations_pb2.ListLocationsRequest",
        response_type="locations_pb2.ListLocationsResponse",
        rpc_name="google.cloud.location.Locations/ListLocations",
    ),
    "GetLocation": wrappers.MixinMethod(
        "GetLocation",
        request_type="locations_pb2.GetLocationRequest",
        response_type="locations_pb2.Location",
        rpc_name="google.cloud.location.Locations/GetLocation",
    ),
}
