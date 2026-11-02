# Copyright 2015 Google LLC
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


import mock
import pytest

from google.cloud.bigtable.cluster import Cluster

from ._testing import _make_credentials

PROJECT = "project"
INSTANCE_ID = "instance-id"
INSTANCE_NAME = "projects/" + PROJECT + "/instances/" + INSTANCE_ID
LOCATION_ID = "locid"
LOCATION = "projects/" + PROJECT + "/locations/" + LOCATION_ID
APP_PROFILE_PATH = "projects/" + PROJECT + "/instances/" + INSTANCE_ID + "/appProfiles/"
DISPLAY_NAME = "display_name"
LABELS = {"foo": "bar"}
OP_ID = 8915
OP_NAME = "operations/projects/{}/instances/{}operations/{}".format(
    PROJECT, INSTANCE_ID, OP_ID
)
TABLE_ID = "table_id"
TABLE_NAME = INSTANCE_NAME + "/tables/" + TABLE_ID
CLUSTER_ID = "cluster-id"
CLUSTER_NAME = INSTANCE_NAME + "/clusters/" + CLUSTER_ID
BACKUP_ID = "backup-id"
BACKUP_NAME = CLUSTER_NAME + "/backups/" + BACKUP_ID

APP_PROFILE_ID_1 = "app-profile-id-1"
DESCRIPTION_1 = "routing policy any"
APP_PROFILE_ID_2 = "app-profile-id-2"
DESCRIPTION_2 = "routing policy single"
ALLOW_WRITES = True
CLUSTER_ID = "cluster-id"


def _make_client(*args, **kwargs):
    from google.cloud.bigtable.client import Client

    return Client(*args, **kwargs)


def _make_instance_admin_api():
    from google.cloud.bigtable_admin_v2.services.bigtable_instance_admin import (
        BigtableInstanceAdminClient,
    )

    return mock.create_autospec(BigtableInstanceAdminClient)


def _make_instance(*args, **kwargs):
    from google.cloud.bigtable.instance import Instance

    return Instance(*args, **kwargs)


def test_instance_constructor_defaults():
    client = object()
    instance = _make_instance(INSTANCE_ID, client)
    assert instance.instance_id == INSTANCE_ID
    assert instance.display_name == INSTANCE_ID
    assert instance.type_ is None
    assert instance.labels is None
    assert instance._client is client
    assert instance.state is None


def test_instance_constructor_non_default():
    from google.cloud.bigtable import enums

    instance_type = enums.Instance.Type.DEVELOPMENT
    state = enums.Instance.State.READY
    labels = {"test": "test"}
    client = object()

    instance = _make_instance(
        INSTANCE_ID,
        client,
        display_name=DISPLAY_NAME,
        instance_type=instance_type,
        labels=labels,
        _state=state,
    )
    assert instance.instance_id == INSTANCE_ID
    assert instance.display_name == DISPLAY_NAME
    assert instance.type_ == instance_type
    assert instance.labels == labels
    assert instance._client is client
    assert instance.state == state


def test_instance__update_from_pb_success():
    from google.cloud.bigtable import enums
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    instance_type = data_v2_pb2.Instance.Type.PRODUCTION
    state = enums.Instance.State.READY
    # todo type to type_?
    instance_pb = data_v2_pb2.Instance(
        display_name=DISPLAY_NAME,
        type_=instance_type,
        labels=LABELS,
        state=state,
    )

    instance = _make_instance(None, None)
    assert instance.display_name is None
    assert instance.type_ is None
    assert instance.labels is None
    instance._update_from_pb(instance_pb._pb)
    assert instance.display_name == DISPLAY_NAME
    assert instance.type_ == instance_type
    assert instance.labels == LABELS
    assert instance._state == state


def test_instance__update_from_pb_success_defaults():
    from google.cloud.bigtable import enums
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    instance_pb = data_v2_pb2.Instance(display_name=DISPLAY_NAME)

    instance = _make_instance(None, None)
    assert instance.display_name is None
    assert instance.type_ is None
    assert instance.labels is None
    instance._update_from_pb(instance_pb._pb)
    assert instance.display_name == DISPLAY_NAME
    assert instance.type_ == enums.Instance.Type.UNSPECIFIED
    assert not instance.labels


def test_instance__update_from_pb_wo_display_name():
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    instance_pb = data_v2_pb2.Instance()
    instance = _make_instance(None, None)
    assert instance.display_name is None

    with pytest.raises(ValueError):
        instance._update_from_pb(instance_pb)


def test_instance_from_pb_success():
    from google.cloud.bigtable import enums
    from google.cloud.bigtable.instance import Instance
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance_type = enums.Instance.Type.PRODUCTION
    state = enums.Instance.State.READY
    instance_pb = data_v2_pb2.Instance(
        name=INSTANCE_NAME,
        display_name=INSTANCE_ID,
        type_=instance_type,
        labels=LABELS,
        state=state,
    )

    instance = Instance.from_pb(instance_pb, client)

    assert isinstance(instance, Instance)
    assert instance._client == client
    assert instance.instance_id == INSTANCE_ID
    assert instance.display_name == INSTANCE_ID
    assert instance.type_ == instance_type
    assert instance.labels == LABELS
    assert instance._state == state


def test_instance_from_pb_bad_instance_name():
    from google.cloud.bigtable.instance import Instance
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    instance_name = "INCORRECT_FORMAT"
    instance_pb = data_v2_pb2.Instance(name=instance_name)

    with pytest.raises(ValueError):
        Instance.from_pb(instance_pb, None)


def test_instance_from_pb_project_mistmatch():
    from google.cloud.bigtable.instance import Instance
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    ALT_PROJECT = "ALT_PROJECT"
    credentials = _make_credentials()
    client = _make_client(project=ALT_PROJECT, credentials=credentials, admin=True)

    instance_pb = data_v2_pb2.Instance(name=INSTANCE_NAME)

    with pytest.raises(ValueError):
        Instance.from_pb(instance_pb, client)


def test_instance_name():
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)

    api = client._instance_admin_client = _make_instance_admin_api()
    api.instance_path.return_value = INSTANCE_NAME
    instance = _make_instance(INSTANCE_ID, client)

    assert instance.name == INSTANCE_NAME


def test_instance___eq__():
    client = object()
    instance1 = _make_instance(INSTANCE_ID, client)
    instance2 = _make_instance(INSTANCE_ID, client)
    assert instance1 == instance2


def test_instance___eq__type_differ():
    client = object()
    instance1 = _make_instance(INSTANCE_ID, client)
    instance2 = object()
    assert instance1 != instance2


def test_instance___ne__same_value():
    client = object()
    instance1 = _make_instance(INSTANCE_ID, client)
    instance2 = _make_instance(INSTANCE_ID, client)
    assert not (instance1 != instance2)


def test_instance___ne__():
    instance1 = _make_instance("instance_id1", "client1")
    instance2 = _make_instance("instance_id2", "client2")
    assert instance1 != instance2


def test_instance_create_w_location_and_clusters():
    instance = _make_instance(INSTANCE_ID, None)

    with pytest.raises(ValueError):
        instance.create(location_id=LOCATION_ID, clusters=[object(), object()])


def test_instance_create_w_serve_nodes_and_clusters():
    instance = _make_instance(INSTANCE_ID, None)

    with pytest.raises(ValueError):
        instance.create(serve_nodes=3, clusters=[object(), object()])


def test_instance_create_w_default_storage_type_and_clusters():
    instance = _make_instance(INSTANCE_ID, None)

    with pytest.raises(ValueError):
        instance.create(default_storage_type=1, clusters=[object(), object()])


def _instance_api_response_for_create():
    import datetime

    from google.api_core import operation
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.longrunning import operations_pb2
    from google.protobuf.any_pb2 import Any

    from google.cloud.bigtable_admin_v2.types import (
        bigtable_instance_admin as messages_v2_pb2,
    )
    from google.cloud.bigtable_admin_v2.types import instance

    NOW = datetime.datetime.now(datetime.timezone.utc)
    NOW_PB = _datetime_to_pb_timestamp(NOW)
    metadata = messages_v2_pb2.CreateInstanceMetadata(request_time=NOW_PB)
    type_url = "type.googleapis.com/{}".format(
        messages_v2_pb2.CreateInstanceMetadata._meta._pb.DESCRIPTOR.full_name
    )
    response_pb = operations_pb2.Operation(
        name=OP_NAME,
        metadata=Any(type_url=type_url, value=metadata._pb.SerializeToString()),
    )
    response = operation.from_gapic(
        response_pb,
        mock.Mock(),
        instance.Instance,
        metadata_type=messages_v2_pb2.CreateInstanceMetadata,
    )
    project_path_template = "projects/{}"
    location_path_template = "projects/{}/locations/{}"
    api = _make_instance_admin_api()
    api.create_instance.return_value = response
    api.project_path = project_path_template.format
    api.location_path = location_path_template.format
    api.common_location_path = location_path_template.format
    return api, response


def test_instance_create():
    import warnings

    from google.cloud.bigtable import enums
    from google.cloud.bigtable_admin_v2.types import Cluster, Instance

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(
        INSTANCE_ID,
        client,
        DISPLAY_NAME,
        enums.Instance.Type.PRODUCTION,
        LABELS,
    )
    api, response = _instance_api_response_for_create()
    client._instance_admin_client = api
    api.common_project_path.return_value = "projects/project"
    serve_nodes = 3

    with warnings.catch_warnings(record=True) as warned:
        result = instance.create(location_id=LOCATION_ID, serve_nodes=serve_nodes)

    assert result is response

    cluster_pb = Cluster(
        location=api.location_path(PROJECT, LOCATION_ID),
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.UNSPECIFIED,
    )
    instance_pb = Instance(
        display_name=DISPLAY_NAME,
        type_=enums.Instance.Type.PRODUCTION,
        labels=LABELS,
    )
    cluster_id = "{}-cluster".format(INSTANCE_ID)
    api.create_instance.assert_called_once_with(
        request={
            "parent": api.project_path(PROJECT),
            "instance_id": INSTANCE_ID,
            "instance": instance_pb,
            "clusters": {cluster_id: cluster_pb},
        }
    )

    assert len(warned) == 1
    assert warned[0].category is DeprecationWarning


def test_instance_create_w_clusters():
    from google.cloud.bigtable import enums
    from google.cloud.bigtable.cluster import Cluster
    from google.cloud.bigtable_admin_v2.types import Cluster as cluster_pb
    from google.cloud.bigtable_admin_v2.types import Instance as instance_pb

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(
        INSTANCE_ID,
        client,
        DISPLAY_NAME,
        enums.Instance.Type.PRODUCTION,
        LABELS,
    )
    api, response = _instance_api_response_for_create()
    client._instance_admin_client = api
    api.common_project_path.return_value = "projects/project"
    cluster_id_1 = "cluster-1"
    cluster_id_2 = "cluster-2"
    location_id_1 = "location-id-1"
    location_id_2 = "location-id-2"
    serve_nodes_1 = 3
    serve_nodes_2 = 5
    clusters = [
        Cluster(
            cluster_id_1,
            instance,
            location_id=location_id_1,
            serve_nodes=serve_nodes_1,
        ),
        Cluster(
            cluster_id_2,
            instance,
            location_id=location_id_2,
            serve_nodes=serve_nodes_2,
        ),
    ]

    result = instance.create(clusters=clusters)

    assert result is response

    cluster_pb_1 = cluster_pb(
        location=api.location_path(PROJECT, location_id_1),
        serve_nodes=serve_nodes_1,
        default_storage_type=enums.StorageType.UNSPECIFIED,
    )
    cluster_pb_2 = cluster_pb(
        location=api.location_path(PROJECT, location_id_2),
        serve_nodes=serve_nodes_2,
        default_storage_type=enums.StorageType.UNSPECIFIED,
    )
    instance_pb = instance_pb(
        display_name=DISPLAY_NAME,
        type_=enums.Instance.Type.PRODUCTION,
        labels=LABELS,
    )
    api.create_instance.assert_called_once_with(
        request={
            "parent": api.project_path(PROJECT),
            "instance_id": INSTANCE_ID,
            "instance": instance_pb,
            "clusters": {cluster_id_1: cluster_pb_1, cluster_id_2: cluster_pb_2},
        }
    )


def test_instance_exists_hit():
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    response_pb = data_v2_pb2.Instance(name=INSTANCE_NAME)
    api = client._instance_admin_client = _make_instance_admin_api()
    api.instance_path.return_value = INSTANCE_NAME
    api.get_instance.return_value = response_pb
    instance = _make_instance(INSTANCE_ID, client)

    assert instance.exists()

    api.get_instance.assert_called_once_with(request={"name": INSTANCE_NAME})


def test_instance_exists_miss():
    from google.api_core import exceptions

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)

    api = client._instance_admin_client = _make_instance_admin_api()
    api.instance_path.return_value = INSTANCE_NAME
    api.get_instance.side_effect = exceptions.NotFound("testing")

    non_existing_instance_id = "instance-id-2"
    instance = _make_instance(non_existing_instance_id, client)

    assert not instance.exists()

    api.get_instance.assert_called_once_with(request={"name": INSTANCE_NAME})


def test_instance_exists_w_error():
    from google.api_core import exceptions

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)

    api = client._instance_admin_client = _make_instance_admin_api()
    api.instance_path.return_value = INSTANCE_NAME
    api.get_instance.side_effect = exceptions.BadRequest("testing")
    instance = _make_instance(INSTANCE_ID, client)

    with pytest.raises(exceptions.BadRequest):
        instance.exists()

    api.get_instance.assert_called_once_with(request={"name": INSTANCE_NAME})


def test_instance_reload():
    from google.cloud.bigtable import enums
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    DISPLAY_NAME = "hey-hi-hello"
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)
    response_pb = data_v2_pb2.Instance(
        display_name=DISPLAY_NAME, type_=enums.Instance.Type.PRODUCTION, labels=LABELS
    )
    api = client._instance_admin_client = _make_instance_admin_api()
    api.get_instance.side_effect = [response_pb]
    assert instance.display_name == INSTANCE_ID

    result = instance.reload()

    assert result is None
    assert instance.display_name == DISPLAY_NAME


def _instance_api_response_for_update():
    import datetime

    from google.api_core import operation
    from google.cloud._helpers import _datetime_to_pb_timestamp
    from google.longrunning import operations_pb2
    from google.protobuf.any_pb2 import Any

    from google.cloud.bigtable_admin_v2.types import (
        bigtable_instance_admin as messages_v2_pb2,
    )
    from google.cloud.bigtable_admin_v2.types import instance

    NOW = datetime.datetime.now(datetime.timezone.utc)
    NOW_PB = _datetime_to_pb_timestamp(NOW)
    metadata = messages_v2_pb2.UpdateInstanceMetadata(request_time=NOW_PB)
    type_url = "type.googleapis.com/{}".format(
        messages_v2_pb2.UpdateInstanceMetadata._meta._pb.DESCRIPTOR.full_name
    )
    response_pb = operations_pb2.Operation(
        name=OP_NAME,
        metadata=Any(type_url=type_url, value=metadata._pb.SerializeToString()),
    )
    response = operation.from_gapic(
        response_pb,
        mock.Mock(),
        instance.Instance,
        metadata_type=messages_v2_pb2.UpdateInstanceMetadata,
    )
    instance_path_template = "projects/{project}/instances/{instance}"
    api = _make_instance_admin_api()
    api.partial_update_instance.return_value = response
    api.instance_path = instance_path_template.format
    return api, response


def test_instance_update():
    from google.protobuf import field_mask_pb2

    from google.cloud.bigtable import enums
    from google.cloud.bigtable_admin_v2.types import Instance

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(
        INSTANCE_ID,
        client,
        display_name=DISPLAY_NAME,
        instance_type=enums.Instance.Type.DEVELOPMENT,
        labels=LABELS,
    )
    api, response = _instance_api_response_for_update()
    client._instance_admin_client = api

    result = instance.update()

    assert result is response

    instance_pb = Instance(
        name=instance.name,
        display_name=instance.display_name,
        type_=instance.type_,
        labels=instance.labels,
    )
    update_mask_pb = field_mask_pb2.FieldMask(paths=["display_name", "type", "labels"])

    api.partial_update_instance.assert_called_once_with(
        request={"instance": instance_pb, "update_mask": update_mask_pb}
    )


def test_instance_update_empty():
    from google.protobuf import field_mask_pb2

    from google.cloud.bigtable_admin_v2.types import Instance

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(None, client)
    api, response = _instance_api_response_for_update()
    client._instance_admin_client = api

    result = instance.update()

    assert result is response

    instance_pb = Instance(
        name=instance.name,
        display_name=instance.display_name,
        type_=instance.type_,
        labels=instance.labels,
    )
    update_mask_pb = field_mask_pb2.FieldMask()

    api.partial_update_instance.assert_called_once_with(
        request={"instance": instance_pb, "update_mask": update_mask_pb}
    )


def test_instance_delete():
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)
    api = client._instance_admin_client = _make_instance_admin_api()
    api.delete_instance.return_value = None

    result = instance.delete()

    assert result is None

    api.delete_instance.assert_called_once_with(request={"name": instance.name})


def test_instance_get_iam_policy():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": members}]
    iam_policy = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)
    api = client._instance_admin_client = _make_instance_admin_api()
    api.get_iam_policy.return_value = iam_policy

    result = instance.get_iam_policy()

    assert result.version == version
    assert result.etag == etag
    admins = result.bigtable_admins
    assert len(admins) == len(members)

    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected
    api.get_iam_policy.assert_called_once_with(request={"resource": instance.name})


def test_instance_get_iam_policy_w_requested_policy_version():
    from google.iam.v1 import options_pb2, policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": members}]
    iam_policy = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)

    api = client._instance_admin_client = _make_instance_admin_api()
    api.get_iam_policy.return_value = iam_policy

    result = instance.get_iam_policy(requested_policy_version=3)

    assert result.version == version
    assert result.etag == etag
    admins = result.bigtable_admins
    assert len(admins) == len(members)
    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected

    api.get_iam_policy.assert_called_once_with(
        request={
            "resource": instance.name,
            "options_": options_pb2.GetPolicyOptions(requested_policy_version=3),
        }
    )


def test_instance_set_iam_policy():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)

    version = 1
    etag = b"etag_v1"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    bindings = [{"role": BIGTABLE_ADMIN_ROLE, "members": sorted(members)}]
    iam_policy_pb = policy_pb2.Policy(version=version, etag=etag, bindings=bindings)

    api = client._instance_admin_client = _make_instance_admin_api()
    api.set_iam_policy.return_value = iam_policy_pb
    iam_policy = Policy(etag=etag, version=version)
    iam_policy[BIGTABLE_ADMIN_ROLE] = [
        Policy.user("user1@test.com"),
        Policy.service_account("service_acc1@test.com"),
    ]

    result = instance.set_iam_policy(iam_policy)

    api.set_iam_policy.assert_called_once_with(
        request={"resource": instance.name, "policy": iam_policy_pb}
    )
    assert result.version == version
    assert result.etag == etag
    admins = result.bigtable_admins
    assert len(admins) == len(members)
    for found, expected in zip(sorted(admins), sorted(members)):
        assert found == expected


def test_instance_test_iam_permissions():
    from google.iam.v1 import iam_policy_pb2

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)

    permissions = ["bigtable.tables.create", "bigtable.clusters.create"]

    response = iam_policy_pb2.TestIamPermissionsResponse(permissions=permissions)
    api = client._instance_admin_client = _make_instance_admin_api()
    api.test_iam_permissions.return_value = response

    result = instance.test_iam_permissions(permissions)

    assert result == permissions
    api.test_iam_permissions.assert_called_once_with(
        request={"resource": instance.name, "permissions": permissions}
    )


def test_instance_cluster_factory():
    from google.cloud.bigtable import enums

    CLUSTER_ID = "{}-cluster".format(INSTANCE_ID)
    LOCATION_ID = "us-central1-c"
    SERVE_NODES = 3
    STORAGE_TYPE = enums.StorageType.HDD

    instance = _make_instance(INSTANCE_ID, None)

    cluster = instance.cluster(
        CLUSTER_ID,
        location_id=LOCATION_ID,
        serve_nodes=SERVE_NODES,
        default_storage_type=STORAGE_TYPE,
    )
    assert isinstance(cluster, Cluster)
    assert cluster.cluster_id == CLUSTER_ID
    assert cluster.location_id == LOCATION_ID
    assert cluster._state is None
    assert cluster.serve_nodes == SERVE_NODES
    assert cluster.default_storage_type == STORAGE_TYPE


def test_instance_list_clusters():
    from google.cloud.bigtable.instance import Cluster, Instance
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_instance_admin as messages_v2_pb2,
    )
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = Instance(INSTANCE_ID, client)

    failed_location = "FAILED"
    cluster_id1 = "cluster-id1"
    cluster_id2 = "cluster-id2"
    cluster_path_template = "projects/{}/instances/{}/clusters/{}"
    cluster_name1 = cluster_path_template.format(PROJECT, INSTANCE_ID, cluster_id1)
    cluster_name2 = cluster_path_template.format(PROJECT, INSTANCE_ID, cluster_id2)
    response_pb = messages_v2_pb2.ListClustersResponse(
        failed_locations=[failed_location],
        clusters=[
            data_v2_pb2.Cluster(name=cluster_name1),
            data_v2_pb2.Cluster(name=cluster_name2),
        ],
    )
    api = client._instance_admin_client = _make_instance_admin_api()
    api.list_clusters.side_effect = [response_pb]
    api.cluster_path = cluster_path_template.format

    # Perform the method and check the result.
    clusters, failed_locations = instance.list_clusters()

    cluster_1, cluster_2 = clusters

    assert isinstance(cluster_1, Cluster)
    assert cluster_1.name == cluster_name1

    assert isinstance(cluster_2, Cluster)
    assert cluster_2.name == cluster_name2

    assert failed_locations == [failed_location]


def test_instance_table_factory():
    from google.cloud.bigtable.table import Table

    app_profile_id = "appProfileId1262094415"
    instance = _make_instance(INSTANCE_ID, mock.MagicMock())

    table = instance.table(TABLE_ID, app_profile_id=app_profile_id)
    assert isinstance(table, Table)
    assert table.table_id == TABLE_ID
    assert table._instance == instance
    assert table._app_profile_id == app_profile_id


def _list_tables_helper(table_name=None):
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_table_admin as table_messages_v1_pb2,
    )
    from google.cloud.bigtable_admin_v2.types import table as table_data_v2_pb2

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)

    instance_api = client._instance_admin_client = _make_instance_admin_api()
    instance_api.instance_path.return_value = "projects/project/instances/instance-id"
    table_api = client._table_admin_client = mock.create_autospec(
        BaseBigtableTableAdminClient
    )
    if table_name is None:
        table_name = TABLE_NAME

    response_pb = table_messages_v1_pb2.ListTablesResponse(
        tables=[table_data_v2_pb2.Table(name=table_name)]
    )

    table_api.list_tables.side_effect = [response_pb]

    result = instance.list_tables()

    expected_table = instance.table(TABLE_ID)
    assert result == [expected_table]


def test_instance_list_tables():
    _list_tables_helper()


def test_instance_list_tables_failure_bad_split():
    with pytest.raises(ValueError):
        _list_tables_helper(table_name="wrong-format")


def test_instance_list_tables_failure_name_bad_before():
    BAD_TABLE_NAME = (
        "nonempty-section-before"
        + "projects/"
        + PROJECT
        + "/instances/"
        + INSTANCE_ID
        + "/tables/"
        + TABLE_ID
    )
    with pytest.raises(ValueError):
        _list_tables_helper(table_name=BAD_TABLE_NAME)


def test_instance_app_profile_factory():
    from google.cloud.bigtable.enums import RoutingPolicyType

    instance = _make_instance(INSTANCE_ID, None)

    app_profile1 = instance.app_profile(
        APP_PROFILE_ID_1,
        routing_policy_type=RoutingPolicyType.ANY,
        description=DESCRIPTION_1,
    )

    app_profile2 = instance.app_profile(
        APP_PROFILE_ID_2,
        routing_policy_type=RoutingPolicyType.SINGLE,
        description=DESCRIPTION_2,
        cluster_id=CLUSTER_ID,
        allow_transactional_writes=ALLOW_WRITES,
    )
    assert app_profile1.app_profile_id == APP_PROFILE_ID_1
    assert app_profile1._instance is instance
    assert app_profile1.routing_policy_type == RoutingPolicyType.ANY
    assert app_profile1.description == DESCRIPTION_1
    assert app_profile2.app_profile_id == APP_PROFILE_ID_2
    assert app_profile2._instance is instance
    assert app_profile2.routing_policy_type == RoutingPolicyType.SINGLE
    assert app_profile2.description == DESCRIPTION_2
    assert app_profile2.cluster_id == CLUSTER_ID
    assert app_profile2.allow_transactional_writes == ALLOW_WRITES


def test_instance_list_app_profiles():
    from google.api_core.page_iterator import Iterator, Page

    from google.cloud.bigtable.app_profile import AppProfile
    from google.cloud.bigtable_admin_v2.types import instance as data_v2_pb2

    class _Iterator(Iterator):
        def __init__(self, pages):
            super(_Iterator, self).__init__(client=None)
            self._pages = pages

        def _next_page(self):
            if self._pages:
                page, self._pages = self._pages[0], self._pages[1:]
                return Page(self, page, self.item_to_value)

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, admin=True)
    instance = _make_instance(INSTANCE_ID, client)

    # Setup Expected Response
    app_profile_path_template = "projects/{}/instances/{}/appProfiles/{}"
    app_profile_id1 = "app-profile-id1"
    app_profile_id2 = "app-profile-id2"
    app_profile_name1 = app_profile_path_template.format(
        PROJECT, INSTANCE_ID, app_profile_id1
    )
    app_profile_name2 = app_profile_path_template.format(
        PROJECT, INSTANCE_ID, app_profile_id2
    )
    routing_policy = data_v2_pb2.AppProfile.MultiClusterRoutingUseAny()

    app_profiles = [
        data_v2_pb2.AppProfile(
            name=app_profile_name1, multi_cluster_routing_use_any=routing_policy
        ),
        data_v2_pb2.AppProfile(
            name=app_profile_name2, multi_cluster_routing_use_any=routing_policy
        ),
    ]
    iterator = _Iterator(pages=[app_profiles])

    # Patch the stub used by the API method.
    api = _make_instance_admin_api()
    client._instance_admin_client = api
    api.app_profile_path = app_profile_path_template.format
    api.list_app_profiles.return_value = iterator

    # Perform the method and check the result.
    app_profiles = instance.list_app_profiles()

    app_profile_1, app_profile_2 = app_profiles

    assert isinstance(app_profile_1, AppProfile)
    assert app_profile_1.name == app_profile_name1

    assert isinstance(app_profile_2, AppProfile)
    assert app_profile_2.name == app_profile_name2


@pytest.fixture()
def data_api():
    from google.cloud.bigtable_v2.services.bigtable import BigtableClient

    data_api_mock = mock.create_autospec(BigtableClient)
    data_api_mock.instance_path.return_value = (
        f"projects/{PROJECT}/instances/{INSTANCE_ID}"
    )
    return data_api_mock


@pytest.fixture()
def client(data_api):
    result = _make_client(
        project="project-id", credentials=_make_credentials(), admin=True
    )
    result._table_data_client = data_api
    return result


@pytest.fixture()
def instance(client):
    return client.instance(instance_id=INSTANCE_ID)
