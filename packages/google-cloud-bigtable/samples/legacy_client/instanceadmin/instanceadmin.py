#!/usr/bin/env python

# Copyright 2018, Google LLC
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

"""Demonstrates how to connect to Cloud Bigtable and run some basic operations.
#     http://www.apache.org/licenses/LICENSE-2.0
Prerequisites:
- Create a Cloud Bigtable project.
  https://cloud.google.com/bigtable/docs/
- Set your Google Application Default Credentials.
  https://developers.google.com/identity/protocols/application-default-credentials

Operations performed:
- Create a Cloud Bigtable Instance.
- List Instance for a Cloud Bigtable.
- Delete a Cloud Bigtable Instance.
- Create a Cloud Bigtable Cluster.
- List Cloud Bigtable Clusters.
- Delete a Cloud Bigtable Cluster.
"""

import argparse

from google.cloud import bigtable
from google.cloud.bigtable import enums


def run_instance_operations(project_id, instance_id, cluster_id):
    """Check Instance exists.
        Creates a Production instance with default Cluster.
        List instances in a project.
        List clusters in an instance.

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.
    """
    client = bigtable.Client(project=project_id, admin=True)
    location_id = "us-central1-f"
    serve_nodes = 1
    storage_type = enums.StorageType.SSD
    labels = {"prod-label": "prod-label"}
    instance = client.instance(instance_id, labels=labels)

    # [START bigtable_check_instance_exists_legacy]
    if not instance.exists():
        print("Instance {} does not exist.".format(instance_id))
    else:
        print("Instance {} already exists.".format(instance_id))
    # [END bigtable_check_instance_exists_legacy]

    # [START bigtable_create_prod_instance_legacy]
    cluster = instance.cluster(
        cluster_id,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=storage_type,
    )
    if not instance.exists():
        print("\nCreating an instance")
        # Create instance with given options
        operation = instance.create(clusters=[cluster])
        # Ensure the operation completes.
        operation.result(timeout=480)
        print("\nCreated instance: {}".format(instance_id))
    # [END bigtable_create_prod_instance_legacy]

    # [START bigtable_list_instances_legacy]
    print("\nListing instances:")
    for instance_local in client.list_instances()[0]:
        print(instance_local.instance_id)
    # [END bigtable_list_instances_legacy]

    # [START bigtable_get_instance_legacy]
    print(
        "\nName of instance: {}\nLabels: {}".format(
            instance.display_name, instance.labels
        )
    )
    # [END bigtable_get_instance_legacy]

    # [START bigtable_get_clusters_legacy]
    print("\nListing clusters...")
    for cluster in instance.list_clusters()[0]:
        print(cluster.cluster_id)
    # [END bigtable_get_clusters_legacy]


def delete_instance(project_id, instance_id):
    """Delete the Instance

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.
    """

    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    # [START bigtable_delete_instance_legacy]
    print("\nDeleting instance")
    if not instance.exists():
        print("Instance {} does not exist.".format(instance_id))
    else:
        instance.delete()
        print("Deleted instance: {}".format(instance_id))
    # [END bigtable_delete_instance_legacy]


def add_cluster(project_id, instance_id, cluster_id):
    """Add Cluster

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type cluster_id: str
    :param cluster_id: Cluster id.
    """
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)

    location_id = "us-central1-a"
    serve_nodes = 1
    storage_type = enums.StorageType.SSD

    if not instance.exists():
        print("Instance {} does not exist.".format(instance_id))
    else:
        print("\nAdding cluster to instance {}".format(instance_id))
        # [START bigtable_create_cluster_legacy]
        print("\nListing clusters...")
        for cluster in instance.list_clusters()[0]:
            print(cluster.cluster_id)
        cluster = instance.cluster(
            cluster_id,
            location_id=location_id,
            serve_nodes=serve_nodes,
            default_storage_type=storage_type,
        )
        if cluster.exists():
            print("\nCluster not created, as {} already exists.".format(cluster_id))
        else:
            operation = cluster.create()
            # Ensure the operation completes.
            operation.result(timeout=480)
            print("\nCluster created: {}".format(cluster_id))
        # [END bigtable_create_cluster_legacy]


def delete_cluster(project_id, instance_id, cluster_id):
    """Delete the cluster

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type cluster_id: str
    :param cluster_id: Cluster id.
    """

    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    cluster = instance.cluster(cluster_id)

    # [START bigtable_delete_cluster_legacy]
    print("\nDeleting cluster")
    if cluster.exists():
        cluster.delete()
        print("Cluster deleted: {}".format(cluster_id))
    else:
        print("\nCluster {} does not exist.".format(cluster_id))

    # [END bigtable_delete_cluster_legacy]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "command",
        help="run, del-instance, \
                        add-cluster or del-cluster. \
                        Operation to perform on Instance.",
    )
    parser.add_argument("project_id", help="Your Cloud Platform project ID.")
    parser.add_argument(
        "instance_id",
        help="ID of the Cloud Bigtable instance to \
                        connect to.",
    )
    parser.add_argument(
        "cluster_id",
        help="ID of the Cloud Bigtable cluster to \
                        connect to.",
    )

    args = parser.parse_args()

    if args.command.lower() == "run":
        run_instance_operations(args.project_id, args.instance_id, args.cluster_id)
    elif args.command.lower() == "del-instance":
        delete_instance(args.project_id, args.instance_id)
    elif args.command.lower() == "add-cluster":
        add_cluster(args.project_id, args.instance_id, args.cluster_id)
    elif args.command.lower() == "del-cluster":
        delete_cluster(args.project_id, args.instance_id, args.cluster_id)
    else:
        print(
            "Command should be either run \n Use argument -h, \
               --help to show help and exit."
        )
