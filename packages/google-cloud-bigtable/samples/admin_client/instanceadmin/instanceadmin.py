#!/usr/bin/env python

# Copyright 2026 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demonstrates how to run instance admin operations using BigtableInstanceAdminClient.

Prerequisites:
- Create a Cloud Bigtable project.
- Set your Google Application Default Credentials.
"""

import argparse


def run_instance_operations(project_id, instance_id, cluster_id):
    # [START bigtable_check_instance_exists]
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    instance_path = client.instance_path(project_id, instance_id)

    try:
        instance = client.get_instance(name=instance_path)
        print(f"Instance {instance_id} already exists.")
    except NotFound:
        print(f"Instance {instance_id} does not exist.")
    # [END bigtable_check_instance_exists]

    # [START bigtable_create_prod_instance]
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    project_path = client.common_project_path(project_id)
    instance_path = client.instance_path(project_id, instance_id)

    cluster = bigtable_admin_v2.Cluster(
        location=client.common_location_path(project_id, "us-central1-f"),
        serve_nodes=1,
        default_storage_type=bigtable_admin_v2.StorageType.SSD,
    )
    instance_obj = bigtable_admin_v2.Instance(
        display_name=instance_id,
        labels={"prod-label": "prod-label"},
        type_=bigtable_admin_v2.Instance.Type.PRODUCTION,
    )

    try:
        client.get_instance(name=instance_path)
    except NotFound:
        print("\nCreating an instance")
        # Create instance with given options
        operation = client.create_instance(
            parent=project_path,
            instance_id=instance_id,
            instance=instance_obj,
            clusters={cluster_id: cluster},
        )
        # Ensure the operation completes.
        operation.result(timeout=480)
        print(f"\nCreated instance: {instance_id}")
    # [END bigtable_create_prod_instance]

    # [START bigtable_list_instances]
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    project_path = client.common_project_path(project_id)

    print("\nListing instances:")
    instances_response = client.list_instances(parent=project_path)
    for instance in instances_response.instances:
        print(instance.name.split("/")[-1])
    # [END bigtable_list_instances]

    # [START bigtable_get_instance]
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    instance_path = client.instance_path(project_id, instance_id)

    inst = client.get_instance(name=instance_path)
    print(f"\nName of instance: {inst.display_name}\nLabels: {dict(inst.labels)}")
    # [END bigtable_get_instance]

    # [START bigtable_get_clusters]
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    instance_path = client.instance_path(project_id, instance_id)

    print("\nListing clusters...")
    clusters_response = client.list_clusters(parent=instance_path)
    for cluster in clusters_response.clusters:
        print(cluster.name.split("/")[-1])
    # [END bigtable_get_clusters]


def delete_instance(project_id, instance_id):
    # [START bigtable_delete_instance]
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    instance_path = client.instance_path(project_id, instance_id)

    print("\nDeleting instance")
    try:
        client.delete_instance(name=instance_path)
        print(f"Deleted instance: {instance_id}")
    except NotFound:
        print(f"Instance {instance_id} does not exist.")
    # [END bigtable_delete_instance]


def add_cluster(project_id, instance_id, cluster_id):
    # [START bigtable_create_cluster]
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    instance_path = client.instance_path(project_id, instance_id)
    cluster_path = client.cluster_path(project_id, instance_id, cluster_id)

    print("\nListing clusters...")
    clusters_response = client.list_clusters(parent=instance_path)
    for cluster in clusters_response.clusters:
        print(cluster.name.split("/")[-1])

    new_cluster = bigtable_admin_v2.Cluster(
        location=client.common_location_path(project_id, "us-central1-a"),
        serve_nodes=1,
        default_storage_type=bigtable_admin_v2.StorageType.SSD,
    )
    try:
        client.get_cluster(name=cluster_path)
        print(f"\nCluster not created, as {cluster_id} already exists.")
    except NotFound:
        operation = client.create_cluster(
            parent=instance_path, cluster_id=cluster_id, cluster=new_cluster
        )
        # Ensure the operation completes.
        operation.result(timeout=480)
        print(f"\nCluster created: {cluster_id}")
    # [END bigtable_create_cluster]


def delete_cluster(project_id, instance_id, cluster_id):
    """Delete the cluster

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type cluster_id: str
    :param cluster_id: Cluster id.
    """
    # [START bigtable_delete_cluster]
    from google.api_core.exceptions import NotFound

    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    cluster_path = client.cluster_path(project_id, instance_id, cluster_id)

    print("\nDeleting cluster")
    try:
        client.delete_cluster(name=cluster_path)
        print(f"Cluster deleted: {cluster_id}")
    except NotFound:
        print(f"\nCluster {cluster_id} does not exist.")
    # [END bigtable_delete_cluster]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "command",
        help="run, del-instance, add-cluster or del-cluster.",
    )
    parser.add_argument("project_id", help="Your Cloud Platform project ID.")
    parser.add_argument("instance_id", help="ID of the Cloud Bigtable instance.")
    parser.add_argument("cluster_id", help="ID of the Cloud Bigtable cluster.")

    args = parser.parse_args()

    if args.command.lower() == "run":
        run_instance_operations(args.project_id, args.instance_id, args.cluster_id)
    elif args.command.lower() == "del-instance":
        delete_instance(args.project_id, args.instance_id)
    elif args.command.lower() == "add-cluster":
        add_cluster(args.project_id, args.instance_id, args.cluster_id)
    elif args.command.lower() == "del-cluster":
        delete_cluster(args.project_id, args.instance_id, args.cluster_id)
