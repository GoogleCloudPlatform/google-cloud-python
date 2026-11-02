# Copyright 2011 Google LLC
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

from google.cloud.bigtable import enums
from google.cloud.bigtable.table import ClusterState

from . import _helpers


def _create_app_profile_helper(
    app_profile_id,
    instance,
    routing_policy_type,
    description=None,
    cluster_id=None,
    multi_cluster_ids=None,
    allow_transactional_writes=None,
    ignore_warnings=None,
):
    app_profile = instance.app_profile(
        app_profile_id=app_profile_id,
        routing_policy_type=routing_policy_type,
        description=description,
        cluster_id=cluster_id,
        multi_cluster_ids=multi_cluster_ids,
        allow_transactional_writes=allow_transactional_writes,
    )
    assert app_profile.allow_transactional_writes == allow_transactional_writes

    app_profile.create(ignore_warnings=ignore_warnings)

    # Load a different app_profile objec form the server and
    # verify that it is the same
    alt_app_profile = instance.app_profile(app_profile_id)
    alt_app_profile.reload()

    app_profile.app_profile_id == alt_app_profile.app_profile_id
    app_profile.routing_policy_type == routing_policy_type
    alt_app_profile.routing_policy_type == routing_policy_type
    app_profile.description == alt_app_profile.description
    assert not app_profile.allow_transactional_writes
    assert not alt_app_profile.allow_transactional_writes
    assert app_profile.multi_cluster_ids == alt_app_profile.multi_cluster_ids

    return app_profile


def _list_app_profiles_helper(instance, expected_app_profile_ids):
    app_profiles = instance.list_app_profiles()
    found = [app_prof.app_profile_id for app_prof in app_profiles]
    for expected in expected_app_profile_ids:
        assert expected in found


def _modify_app_profile_helper(
    app_profile_id,
    instance,
    routing_policy_type,
    description=None,
    cluster_id=None,
    multi_cluster_ids=None,
    allow_transactional_writes=None,
    ignore_warnings=None,
):
    app_profile = instance.app_profile(
        app_profile_id=app_profile_id,
        routing_policy_type=routing_policy_type,
        description=description,
        cluster_id=cluster_id,
        multi_cluster_ids=multi_cluster_ids,
        allow_transactional_writes=allow_transactional_writes,
    )

    operation = app_profile.update(ignore_warnings=ignore_warnings)
    operation.result(timeout=240)

    alt_profile = instance.app_profile(app_profile_id)
    alt_profile.reload()

    assert alt_profile.description == description
    assert alt_profile.routing_policy_type == routing_policy_type
    assert alt_profile.cluster_id == cluster_id
    assert alt_profile.multi_cluster_ids == multi_cluster_ids
    assert alt_profile.allow_transactional_writes == allow_transactional_writes


def _delete_app_profile_helper(app_profile):
    assert app_profile.exists()
    app_profile.delete(ignore_warnings=True)
    assert not app_profile.exists()


def test_client_list_instances(
    admin_client, admin_instance_populated, skip_on_emulator
):
    instances, failed_locations = admin_client.list_instances()

    assert failed_locations == []

    found = set([instance.name for instance in instances])
    assert admin_instance_populated.name in found


def test_instance_exists_hit(admin_instance_populated, skip_on_emulator):
    # Emulator does not support instance admin operations (create / delete).
    # It allows connecting with *any* project / instance name.
    # See: https://cloud.google.com/bigtable/docs/emulator
    assert admin_instance_populated.exists()


def test_instance_exists_miss(admin_client, skip_on_emulator):
    alt_instance = admin_client.instance("nonesuch-instance")
    assert not alt_instance.exists()


def test_instance_reload(
    admin_client, admin_instance_id, admin_instance_populated, skip_on_emulator
):
    # Use same arguments as 'admin_instance_populated'
    # so we can use reload() on a fresh instance.
    alt_instance = admin_client.instance(admin_instance_id)
    # Make sure metadata unset before reloading.
    alt_instance.display_name = None

    alt_instance.reload()

    assert alt_instance.display_name == admin_instance_populated.display_name
    assert alt_instance.labels == admin_instance_populated.labels
    assert alt_instance.type_ == enums.Instance.Type.PRODUCTION


def test_instance_create_prod(
    admin_client,
    unique_suffix,
    location_id,
    instance_labels,
    instances_to_delete,
    skip_on_emulator,
):
    from google.cloud.bigtable import enums

    alt_instance_id = f"ndef{unique_suffix}"
    instance = admin_client.instance(alt_instance_id, labels=instance_labels)
    alt_cluster_id = f"{alt_instance_id}-cluster"
    serve_nodes = 1
    cluster = instance.cluster(
        alt_cluster_id,
        location_id=location_id,
        serve_nodes=serve_nodes,
    )

    operation = instance.create(clusters=[cluster])
    instances_to_delete.append(instance)
    operation.result(timeout=480)  # Ensure the operation completes.
    assert instance.type_ is None

    # Create a new instance instance and make sure it is the same.
    instance_alt = admin_client.instance(alt_instance_id)
    instance_alt.reload()

    assert instance == instance_alt
    assert instance.display_name == instance_alt.display_name
    assert instance_alt.type_ == enums.Instance.Type.PRODUCTION


def test_instance_create_development(
    admin_client,
    unique_suffix,
    location_id,
    instance_labels,
    instances_to_delete,
    skip_on_emulator,
):
    alt_instance_id = f"new{unique_suffix}"
    instance = admin_client.instance(
        alt_instance_id,
        instance_type=enums.Instance.Type.DEVELOPMENT,
        labels=instance_labels,
    )
    alt_cluster_id = f"{alt_instance_id}-cluster"
    cluster = instance.cluster(alt_cluster_id, location_id=location_id)

    operation = instance.create(clusters=[cluster])
    instances_to_delete.append(instance)
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new instance instance and make sure it is the same.
    instance_alt = admin_client.instance(alt_instance_id)
    instance_alt.reload()

    assert instance == instance_alt
    assert instance.display_name == instance_alt.display_name
    assert instance.type_ == instance_alt.type_
    assert instance_alt.labels == instance_labels
    assert instance_alt.state == enums.Instance.State.READY


def test_instance_create_w_two_clusters(
    admin_client,
    unique_suffix,
    admin_instance_populated,
    admin_cluster,
    location_id,
    instance_labels,
    instances_to_delete,
    skip_on_emulator,
):
    alt_instance_id = f"dif{unique_suffix}"
    instance = admin_client.instance(
        alt_instance_id,
        instance_type=enums.Instance.Type.PRODUCTION,
        labels=instance_labels,
    )

    serve_nodes = 1

    alt_cluster_id_1 = f"{alt_instance_id}-c1"
    cluster_1 = instance.cluster(
        alt_cluster_id_1,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.HDD,
    )

    alt_cluster_id_2 = f"{alt_instance_id}-c2"
    location_id_2 = "us-central1-f"
    cluster_2 = instance.cluster(
        alt_cluster_id_2,
        location_id=location_id_2,
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.HDD,
    )
    operation = instance.create(clusters=[cluster_1, cluster_2])
    instances_to_delete.append(instance)
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new instance instance and make sure it is the same.
    instance_alt = admin_client.instance(alt_instance_id)
    instance_alt.reload()

    assert instance == instance_alt
    assert instance.display_name == instance_alt.display_name
    assert instance.type_ == instance_alt.type_

    clusters, failed_locations = instance_alt.list_clusters()
    assert failed_locations == []

    alt_cluster_1, alt_cluster_2 = sorted(clusters, key=lambda x: x.name)

    assert cluster_1.location_id == alt_cluster_1.location_id
    assert alt_cluster_1.state == enums.Cluster.State.READY
    assert cluster_1.serve_nodes == alt_cluster_1.serve_nodes
    assert cluster_1.default_storage_type == alt_cluster_1.default_storage_type
    assert cluster_2.location_id == alt_cluster_2.location_id
    assert alt_cluster_2.state == enums.Cluster.State.READY
    assert cluster_2.serve_nodes == alt_cluster_2.serve_nodes
    assert cluster_2.default_storage_type == alt_cluster_2.default_storage_type

    # Test list clusters in project via 'client.list_clusters'
    clusters, failed_locations = admin_client.list_clusters()
    assert not failed_locations
    found = set([cluster.name for cluster in clusters])
    expected = {alt_cluster_1.name, alt_cluster_2.name, admin_cluster.name}
    assert expected.issubset(found)

    temp_table_id = "test-get-cluster-states"
    temp_table = instance.table(temp_table_id)
    _helpers.retry_grpc_unavailable(temp_table.create)()

    EncryptionType = enums.EncryptionInfo.EncryptionType
    encryption_info = temp_table.get_encryption_info()
    assert (
        encryption_info[alt_cluster_id_1][0].encryption_type
        == EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    )
    assert (
        encryption_info[alt_cluster_id_2][0].encryption_type
        == EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    )

    c_states = temp_table.get_cluster_states()
    cluster_ids = set(c_states.keys())
    assert cluster_ids == {alt_cluster_id_1, alt_cluster_id_2}

    ReplicationState = enums.Table.ReplicationState
    expected_results = [
        ClusterState(ReplicationState.STATE_NOT_KNOWN),
        ClusterState(ReplicationState.INITIALIZING),
        ClusterState(ReplicationState.PLANNED_MAINTENANCE),
        ClusterState(ReplicationState.UNPLANNED_MAINTENANCE),
        ClusterState(ReplicationState.READY),
    ]

    for clusterstate in c_states.values():
        assert clusterstate in expected_results

    # Test create app profile with multi_cluster_routing policy
    app_profiles_to_delete = []
    description = "routing policy-multy"
    app_profile_id_1 = "app_profile_id_1"
    routing = enums.RoutingPolicyType.ANY
    app_profile_1 = _create_app_profile_helper(
        app_profile_id_1,
        instance,
        routing_policy_type=routing,
        description=description,
        ignore_warnings=True,
    )
    app_profiles_to_delete.append(app_profile_1)

    # Test list app profiles
    _list_app_profiles_helper(instance, [app_profile_id_1])

    # Test modify app profile app_profile_id_1
    # routing policy to single cluster policy,
    # cluster -> alt_cluster_id_1,
    # allow_transactional_writes -> disallowed
    # modify description
    description = "to routing policy-single"
    routing = enums.RoutingPolicyType.SINGLE
    _modify_app_profile_helper(
        app_profile_id_1,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=alt_cluster_id_1,
        allow_transactional_writes=False,
    )

    # Test modify app profile app_profile_id_1
    # cluster -> alt_cluster_id_2,
    # allow_transactional_writes -> allowed
    _modify_app_profile_helper(
        app_profile_id_1,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=alt_cluster_id_2,
        allow_transactional_writes=True,
        ignore_warnings=True,
    )

    # Test create app profile with single cluster routing policy
    description = "routing policy-single"
    app_profile_id_2 = "app_profile_id_2"
    routing = enums.RoutingPolicyType.SINGLE
    app_profile_2 = _create_app_profile_helper(
        app_profile_id_2,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=alt_cluster_id_2,
        allow_transactional_writes=False,
    )
    app_profiles_to_delete.append(app_profile_2)

    # Test list app profiles
    _list_app_profiles_helper(instance, [app_profile_id_1, app_profile_id_2])

    # Test modify app profile app_profile_id_2 to
    # allow transactional writes
    # Note: no need to set ``ignore_warnings`` to True
    # since we are not restrictings anything with this modification.
    _modify_app_profile_helper(
        app_profile_id_2,
        instance,
        routing_policy_type=routing,
        description=description,
        cluster_id=alt_cluster_id_2,
        allow_transactional_writes=True,
    )

    # Test modify app profile app_profile_id_2 routing policy
    # to multi_cluster_routing policy
    # modify description
    description = "to routing policy-multy"
    routing = enums.RoutingPolicyType.ANY
    _modify_app_profile_helper(
        app_profile_id_2,
        instance,
        routing_policy_type=routing,
        description=description,
        allow_transactional_writes=False,
        ignore_warnings=True,
    )

    # Test delete app profiles
    for app_profile in app_profiles_to_delete:
        _delete_app_profile_helper(app_profile)


def test_instance_create_app_profile_create_with_multi_cluster_ids(
    admin_client,
    unique_suffix,
    admin_instance_populated,
    admin_cluster,
    location_id,
    instance_labels,
    instances_to_delete,
    skip_on_emulator,
):
    alt_instance_id = f"dif{unique_suffix}"
    instance = admin_client.instance(
        alt_instance_id,
        instance_type=enums.Instance.Type.PRODUCTION,
        labels=instance_labels,
    )

    serve_nodes = 1

    alt_cluster_id_1 = f"{alt_instance_id}-c1"
    cluster_1 = instance.cluster(
        alt_cluster_id_1,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.HDD,
    )

    alt_cluster_id_2 = f"{alt_instance_id}-c2"
    location_id_2 = "us-central1-f"
    cluster_2 = instance.cluster(
        alt_cluster_id_2,
        location_id=location_id_2,
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.HDD,
    )
    operation = instance.create(clusters=[cluster_1, cluster_2])
    instances_to_delete.append(instance)
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new instance and make sure it is the same.
    instance_alt = admin_client.instance(alt_instance_id)
    instance_alt.reload()

    assert instance == instance_alt
    assert instance.display_name == instance_alt.display_name
    assert instance.type_ == instance_alt.type_

    clusters, failed_locations = instance_alt.list_clusters()
    assert failed_locations == []
    alt_cluster_1, alt_cluster_2 = sorted(clusters, key=lambda x: x.name)

    assert cluster_1.location_id == alt_cluster_1.location_id
    assert cluster_2.location_id == alt_cluster_2.location_id

    # Test create app profile with multi_cluster_routing policy
    app_profiles_to_delete = []
    description = "routing policy-multi"
    app_profile_id_1 = "app_profile_id_1"
    routing = enums.RoutingPolicyType.ANY

    multi_cluster_ids = [alt_cluster_id_1, alt_cluster_id_2]
    app_profile_1 = _create_app_profile_helper(
        app_profile_id_1,
        instance,
        routing_policy_type=routing,
        description=description,
        ignore_warnings=True,
        multi_cluster_ids=multi_cluster_ids,
    )
    assert len(app_profile_1.multi_cluster_ids) == len(multi_cluster_ids)
    assert app_profile_1.multi_cluster_ids == multi_cluster_ids

    # remove a cluster from the multi_cluster_ids
    app_profile_1.multi_cluster_ids.pop()
    app_profile_1.update()

    assert len(app_profile_1.multi_cluster_ids) == 1
    assert app_profile_1.multi_cluster_ids == [alt_cluster_id_1]

    # add a cluster from the multi_cluster_ids
    app_profile_1.multi_cluster_ids.append(alt_cluster_id_2)
    app_profile_1.update()

    assert len(app_profile_1.multi_cluster_ids) == 2
    assert app_profile_1.multi_cluster_ids == [alt_cluster_id_1, alt_cluster_id_2]

    app_profiles_to_delete.append(app_profile_1)

    # # Test delete app profiles
    for app_profile in app_profiles_to_delete:
        _delete_app_profile_helper(app_profile)


def test_instance_create_w_two_clusters_cmek(
    admin_client,
    unique_suffix,
    admin_instance_populated,
    admin_cluster,
    location_id,
    instance_labels,
    instances_to_delete,
    with_kms_key_name,
    skip_on_emulator,
):
    alt_instance_id = f"dif-cmek{unique_suffix}"
    instance = admin_client.instance(
        alt_instance_id,
        instance_type=enums.Instance.Type.PRODUCTION,
        labels=instance_labels,
    )

    serve_nodes = 1

    alt_cluster_id_1 = f"{alt_instance_id}-c1"
    cluster_1 = instance.cluster(
        alt_cluster_id_1,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.HDD,
        kms_key_name=with_kms_key_name,
    )

    alt_cluster_id_2 = f"{alt_instance_id}-c2"
    location_id_2 = "us-central1-f"
    cluster_2 = instance.cluster(
        alt_cluster_id_2,
        location_id=location_id_2,
        serve_nodes=serve_nodes,
        default_storage_type=enums.StorageType.HDD,
        kms_key_name=with_kms_key_name,
    )
    operation = instance.create(clusters=[cluster_1, cluster_2])
    instances_to_delete.append(instance)
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new instance instance and make sure it is the same.
    instance_alt = admin_client.instance(alt_instance_id)
    instance_alt.reload()

    assert instance == instance_alt
    assert instance.display_name == instance_alt.display_name
    assert instance.type_ == instance_alt.type_

    clusters, failed_locations = instance_alt.list_clusters()
    assert failed_locations == []

    alt_cluster_1, alt_cluster_2 = sorted(clusters, key=lambda x: x.name)

    assert cluster_1.location_id == alt_cluster_1.location_id
    assert alt_cluster_1.state == enums.Cluster.State.READY
    assert cluster_1.serve_nodes == alt_cluster_1.serve_nodes
    assert cluster_1.default_storage_type == alt_cluster_1.default_storage_type
    assert cluster_2.location_id == alt_cluster_2.location_id
    assert alt_cluster_2.state == enums.Cluster.State.READY
    assert cluster_2.serve_nodes == alt_cluster_2.serve_nodes
    assert cluster_2.default_storage_type == alt_cluster_2.default_storage_type

    # Test list clusters in project via 'client.list_clusters'
    clusters, failed_locations = admin_client.list_clusters()
    assert not failed_locations
    found = set([cluster.name for cluster in clusters])
    expected = {alt_cluster_1.name, alt_cluster_2.name, admin_cluster.name}
    assert expected.issubset(found)

    temp_table_id = "test-get-cluster-states"
    temp_table = instance.table(temp_table_id)
    temp_table.create()

    EncryptionType = enums.EncryptionInfo.EncryptionType
    encryption_info = temp_table.get_encryption_info()
    assert (
        encryption_info[alt_cluster_id_1][0].encryption_type
        == EncryptionType.CUSTOMER_MANAGED_ENCRYPTION
    )
    assert (
        encryption_info[alt_cluster_id_2][0].encryption_type
        == EncryptionType.CUSTOMER_MANAGED_ENCRYPTION
    )


def test_instance_update_display_name_and_labels(
    admin_client,
    admin_instance_id,
    admin_instance_populated,
    label_key,
    instance_labels,
    skip_on_emulator,
):
    old_display_name = admin_instance_populated.display_name
    new_display_name = "Foo Bar Baz"

    new_labels = {label_key: _helpers.label_stamp()}
    admin_instance_populated.display_name = new_display_name
    admin_instance_populated.labels = new_labels

    operation = admin_instance_populated.update()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new instance instance and reload it.
    instance_alt = admin_client.instance(admin_instance_id, labels={})
    assert instance_alt.display_name == old_display_name
    assert instance_alt.labels == {}

    instance_alt.reload()

    assert instance_alt.display_name == new_display_name
    assert instance_alt.labels == new_labels

    # Make sure to put the instance back the way it was for the
    # other test cases.
    admin_instance_populated.display_name = old_display_name
    admin_instance_populated.labels = instance_labels
    operation = admin_instance_populated.update()
    operation.result(timeout=480)  # Ensure the operation completes.


def test_instance_update_w_type(
    admin_client,
    unique_suffix,
    admin_instance_populated,
    location_id,
    instance_labels,
    instances_to_delete,
    skip_on_emulator,
):
    alt_instance_id = f"ndif{unique_suffix}"
    instance = admin_client.instance(
        alt_instance_id,
        instance_type=enums.Instance.Type.DEVELOPMENT,
        labels=instance_labels,
    )
    alt_cluster_id = f"{alt_instance_id}-cluster"
    cluster = instance.cluster(
        alt_cluster_id,
        location_id=location_id,
    )

    operation = instance.create(clusters=[cluster])
    instances_to_delete.append(instance)
    operation.result(timeout=480)  # Ensure the operation completes.

    instance.display_name = None
    instance.type_ = enums.Instance.Type.PRODUCTION
    operation = instance.update()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new instance instance and reload it.
    instance_alt = admin_client.instance(alt_instance_id)
    assert instance_alt.type_ is None
    instance_alt.reload()
    assert instance_alt.type_ == enums.Instance.Type.PRODUCTION


def test_cluster_exists_hit(admin_cluster, skip_on_emulator):
    assert admin_cluster.exists()


def test_cluster_exists_miss(admin_instance_populated, skip_on_emulator):
    alt_cluster = admin_instance_populated.cluster("nonesuch-cluster")
    assert not alt_cluster.exists()


def test_cluster_create(
    admin_instance_populated,
    admin_instance_id,
    skip_on_emulator,
):
    alt_cluster_id = f"{admin_instance_id}-c2"
    alt_location_id = "us-central1-f"
    serve_nodes = 2

    cluster_2 = admin_instance_populated.cluster(
        alt_cluster_id,
        location_id=alt_location_id,
        serve_nodes=serve_nodes,
        default_storage_type=(enums.StorageType.SSD),
    )
    operation = cluster_2.create()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new object instance, reload  and make sure it is the same.
    alt_cluster = admin_instance_populated.cluster(alt_cluster_id)
    alt_cluster.reload()

    assert cluster_2 == alt_cluster
    assert cluster_2.location_id == alt_cluster.location_id
    assert alt_cluster.state == enums.Cluster.State.READY
    assert cluster_2.serve_nodes == alt_cluster.serve_nodes
    assert cluster_2.default_storage_type == alt_cluster.default_storage_type

    # Delete the newly created cluster and confirm
    assert cluster_2.exists()
    cluster_2.delete()
    assert not cluster_2.exists()


def test_cluster_create_w_autoscaling(
    admin_instance_populated,
    admin_instance_id,
    skip_on_emulator,
):
    alt_cluster_id = f"{admin_instance_id}-c2"
    alt_location_id = "us-central1-f"
    min_serve_nodes = 1
    max_serve_nodes = 8
    cpu_utilization_percent = 20

    cluster_2 = admin_instance_populated.cluster(
        alt_cluster_id,
        location_id=alt_location_id,
        min_serve_nodes=min_serve_nodes,
        max_serve_nodes=max_serve_nodes,
        cpu_utilization_percent=cpu_utilization_percent,
        default_storage_type=(enums.StorageType.SSD),
    )
    operation = cluster_2.create()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new object instance, reload  and make sure it is the same.
    alt_cluster = admin_instance_populated.cluster(alt_cluster_id)
    alt_cluster.reload()

    assert cluster_2 == alt_cluster
    assert cluster_2.location_id == alt_cluster.location_id
    assert alt_cluster.state == enums.Cluster.State.READY
    assert cluster_2.min_serve_nodes == alt_cluster.min_serve_nodes
    assert cluster_2.max_serve_nodes == alt_cluster.max_serve_nodes
    assert cluster_2.cpu_utilization_percent == alt_cluster.cpu_utilization_percent
    assert cluster_2.default_storage_type == alt_cluster.default_storage_type

    # Delete the newly created cluster and confirm
    assert cluster_2.exists()
    cluster_2.delete()
    assert not cluster_2.exists()


def test_cluster_update(
    admin_instance_populated,
    admin_cluster_id,
    admin_cluster,
    serve_nodes,
    skip_on_emulator,
):
    new_serve_nodes = 4

    admin_cluster.serve_nodes = new_serve_nodes

    operation = admin_cluster.update()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new cluster instance and reload it.
    alt_cluster = admin_instance_populated.cluster(admin_cluster_id)
    alt_cluster.reload()
    assert alt_cluster.serve_nodes == new_serve_nodes

    # Put the cluster back the way it was for the other test cases.
    admin_cluster.serve_nodes = serve_nodes
    operation = admin_cluster.update()
    operation.result(timeout=480)  # Ensure the operation completes.


def test_cluster_update_w_autoscaling(
    admin_instance_populated,
    admin_cluster_id,
    admin_cluster_with_autoscaling,
    min_serve_nodes,
    max_serve_nodes,
    cpu_utilization_percent,
    skip_on_emulator,
):
    new_min_serve_nodes = min_serve_nodes + 1
    new_max_serve_nodes = max_serve_nodes + 1
    new_cpu_utilization_percent = cpu_utilization_percent + 10
    admin_cluster_with_autoscaling.min_serve_nodes = new_min_serve_nodes
    admin_cluster_with_autoscaling.max_serve_nodes = new_max_serve_nodes
    admin_cluster_with_autoscaling.cpu_utilization_percent = new_cpu_utilization_percent

    operation = admin_cluster_with_autoscaling.update()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new cluster instance and reload it.
    alt_cluster = admin_instance_populated.cluster(admin_cluster_id)
    alt_cluster.reload()
    assert alt_cluster.min_serve_nodes == new_min_serve_nodes
    assert alt_cluster.max_serve_nodes == new_max_serve_nodes
    assert alt_cluster.cpu_utilization_percent == new_cpu_utilization_percent

    # Put the cluster back the way it was for the other test cases.
    admin_cluster_with_autoscaling.min_serve_nodes = min_serve_nodes
    admin_cluster_with_autoscaling.max_serve_nodes = max_serve_nodes
    admin_cluster_with_autoscaling.cpu_utilization_percent = cpu_utilization_percent
    operation = admin_cluster_with_autoscaling.update()
    operation.result(timeout=480)  # Ensure the operation completes.


def test_cluster_update_w_autoscaling_partial(
    admin_instance_populated,
    admin_cluster_id,
    admin_cluster_with_autoscaling,
    min_serve_nodes,
    max_serve_nodes,
    cpu_utilization_percent,
    skip_on_emulator,
):
    new_min_serve_nodes = min_serve_nodes + 1

    admin_cluster_with_autoscaling.min_serve_nodes = new_min_serve_nodes

    operation = admin_cluster_with_autoscaling.update()
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new cluster instance and reload it.
    alt_cluster = admin_instance_populated.cluster(admin_cluster_id)
    alt_cluster.reload()

    # assert that only the min_serve_nodes was changed

    assert alt_cluster.min_serve_nodes == new_min_serve_nodes
    assert alt_cluster.max_serve_nodes == max_serve_nodes
    assert alt_cluster.cpu_utilization_percent == cpu_utilization_percent

    # Put the cluster back the way it was for the other test cases.
    admin_cluster_with_autoscaling.min_serve_nodes = min_serve_nodes
    admin_cluster_with_autoscaling.max_serve_nodes = max_serve_nodes
    admin_cluster_with_autoscaling.cpu_utilization_percent = cpu_utilization_percent
    operation = admin_cluster_with_autoscaling.update()
    operation.result(timeout=480)  # Ensure the operation completes.


def test_cluster_disable_autoscaling(
    admin_instance_populated,
    admin_cluster_id,
    admin_cluster_with_autoscaling,
    serve_nodes,
    min_serve_nodes,
    max_serve_nodes,
    cpu_utilization_percent,
    skip_on_emulator,
):
    operation = admin_cluster_with_autoscaling.disable_autoscaling(
        serve_nodes=serve_nodes
    )
    operation.result(timeout=480)  # Ensure the operation completes.

    # Create a new cluster instance and reload it.
    alt_cluster = admin_instance_populated.cluster(admin_cluster_id)
    alt_cluster.reload()
    assert alt_cluster.min_serve_nodes == 0
    assert alt_cluster.max_serve_nodes == 0
    assert alt_cluster.cpu_utilization_percent == 0
    assert alt_cluster.serve_nodes == serve_nodes

    # Put the cluster back the way it was for the other test cases.
    admin_cluster_with_autoscaling.min_serve_nodes = min_serve_nodes
    admin_cluster_with_autoscaling.max_serve_nodes = max_serve_nodes
    admin_cluster_with_autoscaling.cpu_utilization_percent = cpu_utilization_percent
    admin_cluster_with_autoscaling.serve_nodes = 0
    operation = admin_cluster_with_autoscaling.update()
    operation.result(timeout=480)  # Ensure the operation completes.
