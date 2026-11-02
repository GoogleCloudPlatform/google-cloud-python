# Copyright 2018 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
import pytest

from ._testing import _make_credentials

PROJECT = "project"
INSTANCE_ID = "instance-id"
APP_PROFILE_ID = "app-profile-id"
APP_PROFILE_NAME = "projects/{}/instances/{}/appProfiles/{}".format(
    PROJECT, INSTANCE_ID, APP_PROFILE_ID
)
CLUSTER_ID = "cluster-id"
CLUSTER_ID_2 = "cluster-id-2"
OP_ID = 8765
OP_NAME = "operations/projects/{}/instances/{}/appProfiles/{}/operations/{}".format(
    PROJECT, INSTANCE_ID, APP_PROFILE_ID, OP_ID
)


def _make_app_profile(*args, **kwargs):
    from google.cloud.bigtable.app_profile import AppProfile

    return AppProfile(*args, **kwargs)


def _make_client(*args, **kwargs):
    from google.cloud.bigtable.client import Client

    return Client(*args, **kwargs)


def test_app_profile_constructor_defaults():
    from google.cloud.bigtable.app_profile import AppProfile

    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)

    app_profile = _make_app_profile(APP_PROFILE_ID, instance)
    assert isinstance(app_profile, AppProfile)
    assert app_profile._instance == instance
    assert app_profile.routing_policy_type is None
    assert app_profile.description is None
    assert app_profile.cluster_id is None
    assert app_profile.multi_cluster_ids is None
    assert app_profile.allow_transactional_writes is None


def test_app_profile_constructor_explicit():
    from google.cloud.bigtable.enums import RoutingPolicyType

    ANY = RoutingPolicyType.ANY
    DESCRIPTION_1 = "routing policy any"
    APP_PROFILE_ID_2 = "app-profile-id-2"
    SINGLE = RoutingPolicyType.SINGLE
    DESCRIPTION_2 = "routing policy single"
    ALLOW_WRITES = True
    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)

    app_profile1 = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=ANY,
        description=DESCRIPTION_1,
    )
    app_profile2 = _make_app_profile(
        APP_PROFILE_ID_2,
        instance,
        routing_policy_type=SINGLE,
        description=DESCRIPTION_2,
        cluster_id=CLUSTER_ID,
        allow_transactional_writes=ALLOW_WRITES,
    )
    assert app_profile1.app_profile_id == APP_PROFILE_ID
    assert app_profile1._instance is instance
    assert app_profile1.routing_policy_type == ANY
    assert app_profile1.description == DESCRIPTION_1
    assert app_profile2.app_profile_id == APP_PROFILE_ID_2
    assert app_profile2._instance is instance
    assert app_profile2.routing_policy_type == SINGLE
    assert app_profile2.description == DESCRIPTION_2
    assert app_profile2.cluster_id == CLUSTER_ID
    assert app_profile2.multi_cluster_ids is None
    assert app_profile2.allow_transactional_writes == ALLOW_WRITES


def test_app_profile_constructor_multi_cluster_ids():
    from google.cloud.bigtable.enums import RoutingPolicyType

    ANY = RoutingPolicyType.ANY
    DESCRIPTION_1 = "routing policy any"
    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)

    app_profile1 = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=ANY,
        description=DESCRIPTION_1,
        multi_cluster_ids=[CLUSTER_ID, CLUSTER_ID_2],
    )
    assert app_profile1.app_profile_id == APP_PROFILE_ID
    assert app_profile1._instance is instance
    assert app_profile1.routing_policy_type == ANY
    assert app_profile1.description == DESCRIPTION_1
    assert app_profile1.multi_cluster_ids == [CLUSTER_ID, CLUSTER_ID_2]


def test_app_profile_name():
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _Instance(INSTANCE_ID, client)

    app_profile = _make_app_profile(APP_PROFILE_ID, instance)
    assert app_profile.name == APP_PROFILE_NAME


def test_app_profile___eq__():
    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)
    app_profile1 = _make_app_profile(APP_PROFILE_ID, instance)
    app_profile2 = _make_app_profile(APP_PROFILE_ID, instance)
    assert app_profile1 == app_profile2


def test_app_profile___eq___w_type_instance_differ():
    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)
    alt_instance = _Instance("other-instance", client)
    other_object = _Other(APP_PROFILE_ID, instance)
    app_profile1 = _make_app_profile(APP_PROFILE_ID, instance)
    app_profile2 = _make_app_profile(APP_PROFILE_ID, alt_instance)
    assert not (app_profile1 == other_object)
    assert not (app_profile1 == app_profile2)


def test_app_profile___ne___w_same_value():
    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)
    app_profile1 = _make_app_profile(APP_PROFILE_ID, instance)
    app_profile2 = _make_app_profile(APP_PROFILE_ID, instance)
    assert not (app_profile1 != app_profile2)


def test_app_profile___ne__():
    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)
    app_profile1 = _make_app_profile("app_profile_id1", instance)
    app_profile2 = _make_app_profile("app_profile_id2", instance)
    assert app_profile1 != app_profile2


def test_app_profile_from_pb_success_w_routing_any():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)

    description = "routing any"
    routing = RoutingPolicyType.ANY
    multi_cluster_routing_use_any = data_v2_pb2.AppProfile.MultiClusterRoutingUseAny()

    app_profile_pb = data_v2_pb2.AppProfile(
        name=APP_PROFILE_NAME,
        description=description,
        multi_cluster_routing_use_any=multi_cluster_routing_use_any,
    )

    app_profile = AppProfile.from_pb(app_profile_pb, instance)
    assert isinstance(app_profile, AppProfile)
    assert app_profile._instance is instance
    assert app_profile.app_profile_id == APP_PROFILE_ID
    assert app_profile.description == description
    assert app_profile.routing_policy_type == routing
    assert app_profile.cluster_id is None
    assert app_profile.multi_cluster_ids is None
    assert app_profile.allow_transactional_writes is False


def test_app_profile_from_pb_success_w_routing_any_multi_cluster_ids():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)

    description = "routing any"
    routing = RoutingPolicyType.ANY
    multi_cluster_routing_use_any = data_v2_pb2.AppProfile.MultiClusterRoutingUseAny(
        cluster_ids=[CLUSTER_ID, CLUSTER_ID_2]
    )

    app_profile_pb = data_v2_pb2.AppProfile(
        name=APP_PROFILE_NAME,
        description=description,
        multi_cluster_routing_use_any=multi_cluster_routing_use_any,
    )

    app_profile = AppProfile.from_pb(app_profile_pb, instance)
    assert isinstance(app_profile, AppProfile)
    assert app_profile._instance is instance
    assert app_profile.app_profile_id == APP_PROFILE_ID
    assert app_profile.description == description
    assert app_profile.routing_policy_type == routing
    assert app_profile.cluster_id is None
    assert app_profile.allow_transactional_writes is False
    assert app_profile.multi_cluster_ids == [CLUSTER_ID, CLUSTER_ID_2]


def test_app_profile_from_pb_success_w_routing_single():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    client = _Client(PROJECT)
    instance = _Instance(INSTANCE_ID, client)

    description = "routing single"
    allow_transactional_writes = True
    routing = RoutingPolicyType.SINGLE
    single_cluster_routing = data_v2_pb2.AppProfile.SingleClusterRouting(
        cluster_id=CLUSTER_ID,
        allow_transactional_writes=allow_transactional_writes,
    )

    app_profile_pb = data_v2_pb2.AppProfile(
        name=APP_PROFILE_NAME,
        description=description,
        single_cluster_routing=single_cluster_routing,
    )

    app_profile = AppProfile.from_pb(app_profile_pb, instance)
    assert isinstance(app_profile, AppProfile)
    assert app_profile._instance is instance
    assert app_profile.app_profile_id == APP_PROFILE_ID
    assert app_profile.description == description
    assert app_profile.routing_policy_type == routing
    assert app_profile.cluster_id == CLUSTER_ID
    assert app_profile.multi_cluster_ids is None
    assert app_profile.allow_transactional_writes == allow_transactional_writes


def test_app_profile_from_pb_w_bad_app_profile_name():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    bad_app_profile_name = "BAD_NAME"

    app_profile_pb = data_v2_pb2.AppProfile(name=bad_app_profile_name)

    with pytest.raises(ValueError):
        AppProfile.from_pb(app_profile_pb, None)


def test_app_profile_from_pb_w_instance_id_mistmatch():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    ALT_INSTANCE_ID = "ALT_INSTANCE_ID"
    client = _Client(PROJECT)
    instance = _Instance(ALT_INSTANCE_ID, client)
    assert instance.instance_id == ALT_INSTANCE_ID

    app_profile_pb = data_v2_pb2.AppProfile(name=APP_PROFILE_NAME)

    with pytest.raises(ValueError):
        AppProfile.from_pb(app_profile_pb, instance)


def test_app_profile_from_pb_w_project_mistmatch():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    ALT_PROJECT = "ALT_PROJECT"
    client = _Client(project=ALT_PROJECT)
    instance = _Instance(INSTANCE_ID, client)
    assert client.project == ALT_PROJECT

    app_profile_pb = data_v2_pb2.AppProfile(name=APP_PROFILE_NAME)

    with pytest.raises(ValueError):
        AppProfile.from_pb(app_profile_pb, instance)


def test_app_profile_reload_w_routing_any():
    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    api = mock.create_autospec(BigtableInstanceAdminClient)
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _Instance(INSTANCE_ID, client)

    routing = RoutingPolicyType.ANY
    description = "routing policy any"

    app_profile = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=routing,
        description=description,
    )

    # Create response_pb
    description_from_server = "routing policy switched to single"
    cluster_id_from_server = CLUSTER_ID
    allow_transactional_writes = True
    single_cluster_routing = data_v2_pb2.AppProfile.SingleClusterRouting(
        cluster_id=cluster_id_from_server,
        allow_transactional_writes=allow_transactional_writes,
    )

    response_pb = data_v2_pb2.AppProfile(
        name=app_profile.name,
        single_cluster_routing=single_cluster_routing,
        description=description_from_server,
    )

    # Patch the stub used by the API method.
    client._instance_admin_client = api
    instance_stub = client._instance_admin_client
    instance_stub.get_app_profile.side_effect = [response_pb]

    # Create expected_result.
    expected_result = None  # reload() has no return value.

    # Check app_profile config values before.
    assert app_profile.routing_policy_type == routing
    assert app_profile.description == description
    assert app_profile.cluster_id is None
    assert app_profile.multi_cluster_ids is None
    assert app_profile.allow_transactional_writes is None

    # Perform the method and check the result.
    result = app_profile.reload()
    assert result == expected_result
    assert app_profile.routing_policy_type == RoutingPolicyType.SINGLE
    assert app_profile.description == description_from_server
    assert app_profile.cluster_id == cluster_id_from_server
    assert app_profile.multi_cluster_ids is None
    assert app_profile.allow_transactional_writes == allow_transactional_writes


def test_app_profile_exists():
    from google.api_core import exceptions

    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    instance_api = mock.create_autospec(BigtableInstanceAdminClient)
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)

    # Create response_pb
    response_pb = data_v2_pb2.AppProfile(name=APP_PROFILE_NAME)
    client._instance_admin_client = instance_api

    # Patch the stub used by the API method.
    client._instance_admin_client = instance_api
    instance_stub = client._instance_admin_client
    instance_stub.get_app_profile.side_effect = [
        response_pb,
        exceptions.NotFound("testing"),
        exceptions.BadRequest("testing"),
    ]

    # Perform the method and check the result.
    non_existing_app_profile_id = "other-app-profile-id"
    app_profile = _make_app_profile(APP_PROFILE_ID, instance)
    alt_app_profile = _make_app_profile(non_existing_app_profile_id, instance)
    assert app_profile.exists()
    assert not alt_app_profile.exists()
    with pytest.raises(exceptions.BadRequest):
        alt_app_profile.exists()


def test_app_profile_create_w_routing_any():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)

    routing = RoutingPolicyType.ANY
    description = "routing policy any"
    ignore_warnings = True

    app_profile = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=routing,
        description=description,
    )

    expected_request_app_profile = app_profile._to_pb()
    name = instance.name
    expected_request = {
        "request": {
            "parent": name,
            "app_profile_id": APP_PROFILE_ID,
            "app_profile": expected_request_app_profile,
            "ignore_warnings": ignore_warnings,
        }
    }

    instance_api = mock.create_autospec(BigtableInstanceAdminClient)
    instance_api.app_profile_path.return_value = (
        "projects/project/instances/instance-id/appProfiles/app-profile-id"
    )
    instance_api.instance_path.return_value = name
    instance_api.create_app_profile.return_value = expected_request_app_profile

    # Patch the stub used by the API method.
    client._instance_admin_client = instance_api
    app_profile._instance._client._instance_admin_client = instance_api
    # Perform the method and check the result.
    result = app_profile.create(ignore_warnings)

    actual_request = client._instance_admin_client.create_app_profile.call_args_list[
        0
    ].kwargs

    assert actual_request == expected_request
    assert isinstance(result, AppProfile)
    assert result.app_profile_id == APP_PROFILE_ID
    assert result._instance is instance
    assert result.routing_policy_type == routing
    assert result.description == description
    assert result.allow_transactional_writes is False
    assert result.cluster_id is None
    assert result.multi_cluster_ids is None


def test_app_profile_create_w_routing_single():
    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)

    routing = RoutingPolicyType.SINGLE
    description = "routing policy single"
    allow_writes = False
    ignore_warnings = True

    app_profile = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=CLUSTER_ID,
        allow_transactional_writes=allow_writes,
    )
    expected_request_app_profile = app_profile._to_pb()
    instance_name = instance.name
    expected_request = {
        "request": {
            "parent": instance_name,
            "app_profile_id": APP_PROFILE_ID,
            "app_profile": expected_request_app_profile,
            "ignore_warnings": ignore_warnings,
        }
    }

    # Patch the stub used by the API method.
    instance_api = mock.create_autospec(BigtableInstanceAdminClient)
    instance_api.app_profile_path.return_value = (
        "projects/project/instances/instance-id/appProfiles/app-profile-id"
    )
    instance_api.instance_path.return_value = instance_name
    instance_api.create_app_profile.return_value = expected_request_app_profile
    client._instance_admin_client = instance_api
    # Perform the method and check the result.
    result = app_profile.create(ignore_warnings)

    actual_request = client._instance_admin_client.create_app_profile.call_args_list[
        0
    ].kwargs

    assert actual_request == expected_request
    assert isinstance(result, AppProfile)
    assert result.app_profile_id == APP_PROFILE_ID
    assert result._instance is instance
    assert result.routing_policy_type == routing
    assert result.description == description
    assert result.allow_transactional_writes == allow_writes
    assert result.cluster_id == CLUSTER_ID
    assert result.multi_cluster_ids is None


def test_app_profile_create_w_wrong_routing_policy():
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)
    app_profile = _make_app_profile(APP_PROFILE_ID, instance, routing_policy_type=None)
    with pytest.raises(ValueError):
        app_profile.create()


def test_app_profile_update_w_routing_any():
    from google.longrunning import operations_pb2
    from google.protobuf import field_mask_pb2
    from google.protobuf.any_pb2 import Any

    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_instance_admin as messages_v2_pb2,
    )

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)

    routing = RoutingPolicyType.SINGLE
    description = "to routing policy single"
    allow_writes = True
    app_profile = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=CLUSTER_ID,
        allow_transactional_writes=allow_writes,
    )

    # Create response_pb
    metadata = messages_v2_pb2.UpdateAppProfileMetadata()
    type_url = "type.googleapis.com/{}".format(
        messages_v2_pb2.UpdateAppProfileMetadata._meta._pb.DESCRIPTOR.full_name
    )
    response_pb = operations_pb2.Operation(
        name=OP_NAME,
        metadata=Any(type_url=type_url, value=metadata._pb.SerializeToString()),
    )

    # Patch the stub used by the API method.
    instance_api = mock.create_autospec(BigtableInstanceAdminClient)
    # Mock api calls
    instance_api.app_profile_path.return_value = (
        "projects/project/instances/instance-id/appProfiles/app-profile-id"
    )

    client._instance_admin_client = instance_api

    # Perform the method and check the result.
    ignore_warnings = True
    expected_request_update_mask = field_mask_pb2.FieldMask(
        paths=["description", "single_cluster_routing"]
    )

    expected_request = {
        "request": {
            "app_profile": app_profile._to_pb(),
            "update_mask": expected_request_update_mask,
            "ignore_warnings": ignore_warnings,
        }
    }

    instance_api.update_app_profile.return_value = response_pb
    app_profile._instance._client._instance_admin_client = instance_api
    result = app_profile.update(ignore_warnings=ignore_warnings)
    actual_request = client._instance_admin_client.update_app_profile.call_args_list[
        0
    ].kwargs

    assert actual_request == expected_request
    assert (
        result.metadata.type_url
        == "type.googleapis.com/google.bigtable.admin.v2.UpdateAppProfileMetadata"
    )


def test_app_profile_update_w_routing_any_multi_cluster_ids():
    from google.longrunning import operations_pb2
    from google.protobuf import field_mask_pb2
    from google.protobuf.any_pb2 import Any

    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_instance_admin as messages_v2_pb2,
    )

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)

    routing = RoutingPolicyType.SINGLE
    description = "to routing policy single"
    allow_writes = True
    app_profile = _make_app_profile(
        APP_PROFILE_ID,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=CLUSTER_ID,
        allow_transactional_writes=allow_writes,
        multi_cluster_ids=[CLUSTER_ID, CLUSTER_ID_2],
    )

    # Create response_pb
    metadata = messages_v2_pb2.UpdateAppProfileMetadata()
    type_url = "type.googleapis.com/{}".format(
        messages_v2_pb2.UpdateAppProfileMetadata._meta._pb.DESCRIPTOR.full_name
    )
    response_pb = operations_pb2.Operation(
        name=OP_NAME,
        metadata=Any(type_url=type_url, value=metadata._pb.SerializeToString()),
    )

    # Patch the stub used by the API method.
    instance_api = mock.create_autospec(BigtableInstanceAdminClient)
    # Mock api calls
    instance_api.app_profile_path.return_value = (
        "projects/project/instances/instance-id/appProfiles/app-profile-id"
    )

    client._instance_admin_client = instance_api

    # Perform the method and check the result.
    ignore_warnings = True
    expected_request_update_mask = field_mask_pb2.FieldMask(
        paths=["description", "single_cluster_routing"]
    )

    expected_request = {
        "request": {
            "app_profile": app_profile._to_pb(),
            "update_mask": expected_request_update_mask,
            "ignore_warnings": ignore_warnings,
        }
    }

    instance_api.update_app_profile.return_value = response_pb
    app_profile._instance._client._instance_admin_client = instance_api
    result = app_profile.update(ignore_warnings=ignore_warnings)
    actual_request = client._instance_admin_client.update_app_profile.call_args_list[
        0
    ].kwargs

    assert actual_request == expected_request
    assert (
        result.metadata.type_url
        == "type.googleapis.com/google.bigtable.admin.v2.UpdateAppProfileMetadata"
    )


def test_app_profile_update_w_routing_single():
    from google.longrunning import operations_pb2
    from google.protobuf import field_mask_pb2
    from google.protobuf.any_pb2 import Any

    from google.cloud.bigtable.enums import RoutingPolicyType
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_instance_admin as messages_v2_pb2,
    )

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)

    routing = RoutingPolicyType.ANY
    app_profile = _make_app_profile(
        APP_PROFILE_ID, instance, routing_policy_type=routing
    )

    # Create response_pb
    metadata = messages_v2_pb2.UpdateAppProfileMetadata()
    type_url = "type.googleapis.com/{}".format(
        messages_v2_pb2.UpdateAppProfileMetadata._meta._pb.DESCRIPTOR.full_name
    )
    response_pb = operations_pb2.Operation(
        name=OP_NAME,
        metadata=Any(type_url=type_url, value=metadata._pb.SerializeToString()),
    )

    # Patch the stub used by the API method.
    instance_api = mock.create_autospec(BigtableInstanceAdminClient)
    # Mock api calls
    instance_api.app_profile_path.return_value = (
        "projects/project/instances/instance-id/appProfiles/app-profile-id"
    )
    client._instance_admin_client = instance_api
    client._instance_admin_client.update_app_profile.return_value = response_pb
    # Perform the method and check the result.
    ignore_warnings = True
    expected_request_update_mask = field_mask_pb2.FieldMask(
        paths=["multi_cluster_routing_use_any"]
    )
    expected_request = {
        "request": {
            "app_profile": app_profile._to_pb(),
            "update_mask": expected_request_update_mask,
            "ignore_warnings": ignore_warnings,
        }
    }

    result = app_profile.update(ignore_warnings=ignore_warnings)
    actual_request = client._instance_admin_client.update_app_profile.call_args_list[
        0
    ].kwargs
    assert actual_request == expected_request
    assert (
        result.metadata.type_url
        == "type.googleapis.com/google.bigtable.admin.v2.UpdateAppProfileMetadata"
    )


def test_app_profile_update_w_wrong_routing_policy():
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)
    app_profile = _make_app_profile(APP_PROFILE_ID, instance, routing_policy_type=None)
    with pytest.raises(ValueError):
        app_profile.update()


def test_app_profile_delete():
    from google.protobuf import empty_pb2

    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    instance_api = mock.create_autospec(BigtableInstanceAdminClient)

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = client.instance(INSTANCE_ID)
    app_profile = _make_app_profile(APP_PROFILE_ID, instance)

    # Create response_pb
    response_pb = empty_pb2.Empty()

    # Patch the stub used by the API method.
    client._instance_admin_client = instance_api
    instance_stub = client._instance_admin_client.transport
    instance_stub.delete_cluster.side_effect = [response_pb]

    # Create expected_result.
    expected_result = None  # delete() has no return value.

    # Perform the method and check the result.
    result = app_profile.delete()

    assert result == expected_result


class _Client(object):
    def __init__(self, project):
        self.project = project
        self.project_name = "projects/" + self.project
        self._operations_stub = mock.sentinel.operations_stub

    def __eq__(self, other):
        return other.project == self.project and other.project_name == self.project_name


class _Instance(object):
    def __init__(self, instance_id, client):
        self.instance_id = instance_id
        self._client = client

    def __eq__(self, other):
        return other.instance_id == self.instance_id and other._client == self._client


class _Other(object):
    def __init__(self, app_profile_id, instance):
        self.app_profile_id = app_profile_id
        self._instance = instance
