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

"""Demonstrates how to connect to Cloud Bigtable and run table admin operations using BigtableTableAdminClient.

Prerequisites:
- Create a Cloud Bigtable instance.
- Set your Google Application Default Credentials.
"""

import argparse

from ...utils import create_table_cm


def run_table_operations(project_id, instance_id, table_id):
    with create_table_cm(project_id, instance_id, table_id, verbose=False):
        # [START bigtable_list_tables]
        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        instance_path = client.instance_path(project_id, instance_id)

        tables = client.list_tables(parent=instance_path)
        print("Listing tables in current project...")
        if tables.tables:
            for tbl in tables.tables:
                print(tbl.name.split("/")[-1])
        else:
            print("No table exists in current project...")
        # [END bigtable_list_tables]

        # [START bigtable_create_family_gc_max_age]
        from google.protobuf import duration_pb2

        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Creating column family cf1 with MaxAge GC Rule...")
        # Create a column family with GC policy : maximum age
        # where age = current time minus cell timestamp

        # Define the GC rule to retain data with max age of 5 days
        max_age_rule = bigtable_admin_v2.GcRule(
            max_age=duration_pb2.Duration(seconds=5 * 86400)
        )
        cf1 = bigtable_admin_v2.ColumnFamily(gc_rule=max_age_rule)
        mod1 = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf1", create=cf1
        )
        client.modify_column_families(name=table_path, modifications=[mod1])
        print("Created column family cf1 with MaxAge GC Rule.")
        # [END bigtable_create_family_gc_max_age]

        # [START bigtable_create_family_gc_max_versions]
        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Creating column family cf2 with max versions GC rule...")
        # Create a column family with GC policy : most recent N versions
        # where 1 = most recent version

        # Define the GC policy to retain only the most recent 2 versions
        max_versions_rule = bigtable_admin_v2.GcRule(max_num_versions=2)
        cf2 = bigtable_admin_v2.ColumnFamily(gc_rule=max_versions_rule)
        mod2 = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf2", create=cf2
        )
        client.modify_column_families(name=table_path, modifications=[mod2])
        print("Created column family cf2 with Max Versions GC Rule.")
        # [END bigtable_create_family_gc_max_versions]

        # [START bigtable_create_family_gc_union]
        from google.protobuf import duration_pb2

        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Creating column family cf3 with union GC rule...")
        # Create a column family with GC policy to drop data that matches
        # at least one condition.
        # Define a GC rule to drop cells older than 5 days or not the
        # most recent version
        union_rule = bigtable_admin_v2.GcRule(
            union=bigtable_admin_v2.GcRule.Union(
                rules=[
                    bigtable_admin_v2.GcRule(
                        max_age=duration_pb2.Duration(seconds=5 * 86400)
                    ),
                    bigtable_admin_v2.GcRule(max_num_versions=2),
                ]
            )
        )
        cf3 = bigtable_admin_v2.ColumnFamily(gc_rule=union_rule)
        mod3 = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf3", create=cf3
        )
        client.modify_column_families(name=table_path, modifications=[mod3])
        print("Created column family cf3 with Union GC rule")
        # [END bigtable_create_family_gc_union]

        # [START bigtable_create_family_gc_intersection]
        from google.protobuf import duration_pb2

        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Creating column family cf4 with Intersection GC rule...")
        # Create a column family with GC policy to drop data that matches
        # all conditions
        # GC rule: Drop cells older than 5 days AND older than the most
        # recent 2 versions
        intersection_rule = bigtable_admin_v2.GcRule(
            intersection=bigtable_admin_v2.GcRule.Intersection(
                rules=[
                    bigtable_admin_v2.GcRule(
                        max_age=duration_pb2.Duration(seconds=5 * 86400)
                    ),
                    bigtable_admin_v2.GcRule(max_num_versions=2),
                ]
            )
        )
        cf4 = bigtable_admin_v2.ColumnFamily(gc_rule=intersection_rule)
        mod4 = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf4", create=cf4
        )
        client.modify_column_families(name=table_path, modifications=[mod4])
        print("Created column family cf4 with Intersection GC rule.")
        # [END bigtable_create_family_gc_intersection]

        # [START bigtable_create_family_gc_nested]
        from google.protobuf import duration_pb2

        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Creating column family cf5 with a Nested GC rule...")
        # Create a column family with nested GC policies.
        # Create a nested GC rule:
        # Drop cells that are either older than the 10 recent versions
        # OR
        # Drop cells that are older than a month AND older than the
        # 2 recent versions
        rule1 = bigtable_admin_v2.GcRule(max_num_versions=10)
        rule2 = bigtable_admin_v2.GcRule(
            intersection=bigtable_admin_v2.GcRule.Intersection(
                rules=[
                    bigtable_admin_v2.GcRule(
                        max_age=duration_pb2.Duration(seconds=30 * 86400)
                    ),
                    bigtable_admin_v2.GcRule(max_num_versions=2),
                ]
            )
        )
        nested_rule = bigtable_admin_v2.GcRule(
            union=bigtable_admin_v2.GcRule.Union(rules=[rule1, rule2])
        )
        cf5 = bigtable_admin_v2.ColumnFamily(gc_rule=nested_rule)
        mod5 = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf5", create=cf5
        )
        client.modify_column_families(name=table_path, modifications=[mod5])
        print("Created column family cf5 with a Nested GC rule.")
        # [END bigtable_create_family_gc_nested]

        # [START bigtable_list_column_families]
        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Printing Column Family and GC Rule for all column families...")
        table_obj = client.get_table(name=table_path)
        for column_family_name, cf_obj in sorted(table_obj.column_families.items()):
            print("Column Family:", column_family_name)
            print("GC Rule:")
            print(cf_obj.gc_rule)
            # Sample output:
            #         Column Family: cf4
            #         GC Rule:
            #         intersection {
            #           rules {
            #             max_age {
            #               seconds: 432000
            #             }
            #           }
            #           rules {
            #             max_num_versions: 2
            #           }
            #         }
        # [END bigtable_list_column_families]

        # [START bigtable_update_gc_rule]
        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Updating column family cf1 GC rule...")
        # Update the column family cf1 to update the GC rule
        updated_cf1 = bigtable_admin_v2.ColumnFamily(
            gc_rule=bigtable_admin_v2.GcRule(max_num_versions=1)
        )
        mod_update = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf1", update=updated_cf1
        )
        client.modify_column_families(name=table_path, modifications=[mod_update])
        print("Updated column family cf1 GC rule\n")
        # [END bigtable_update_gc_rule]

        # [START bigtable_delete_family]
        from google.cloud import bigtable_admin_v2

        client = bigtable_admin_v2.BigtableTableAdminClient()
        table_path = client.table_path(project_id, instance_id, table_id)

        print("Delete a column family cf2...")
        # Delete a column family
        mod_delete = bigtable_admin_v2.ModifyColumnFamiliesRequest.Modification(
            id="cf2", drop=True
        )
        client.modify_column_families(name=table_path, modifications=[mod_delete])
        print("Column family cf2 deleted successfully.")
        # [END bigtable_delete_family]

        print(
            'execute command "python tableadmin.py delete [project_id] \
                [instance_id] --table [tableName]" to delete the table.'
        )


def delete_table(project_id, instance_id, table_id):
    """Delete bigtable.

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type table_id: str
    :param table_id: Table id to create table.
    """
    # [START bigtable_delete_table]
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableTableAdminClient()
    table_path = client.table_path(project_id, instance_id, table_id)

    # Delete the entire table
    print("Deleting {} table.".format(table_id))
    client.delete_table(name=table_path)
    print("Deleted {} table.".format(table_id))
    # [END bigtable_delete_table]


def wait_for_consistency(project_id, instance_id, table_id):
    """Block until the table's recent writes have been replicated.

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type table_id: str
    :param table_id: Table id to wait on.
    """
    # [START bigtable_wait_for_consistency]
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableTableAdminClient()
    table_path = client.table_path(project_id, instance_id, table_id)

    # Blocks until every mutation made to the table before this call has been
    # replicated to all of the instance's clusters.
    print("Waiting for {} to be consistent...".format(table_id))
    client.wait_for_consistency(name=table_path)
    print("Table {} is consistent.".format(table_id))
    # [END bigtable_wait_for_consistency]


def create_backup(project_id, instance_id, cluster_id, table_id, backup_id):
    """Create a backup of a table.

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type cluster_id: str
    :param cluster_id: Cluster that will store the backup.

    :type table_id: str
    :param table_id: Table to back up.

    :type backup_id: str
    :param backup_id: Id for the new backup.
    """
    # [START bigtable_create_backup]
    import datetime

    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableTableAdminClient()
    cluster_path = client.cluster_path(project_id, instance_id, cluster_id)
    table_path = client.table_path(project_id, instance_id, table_id)

    # Backups must expire between 6 hours and 90 days after they are created
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        hours=8
    )
    print("Creating backup {} of table {}...".format(backup_id, table_id))
    operation = client.create_backup(
        parent=cluster_path,
        backup_id=backup_id,
        backup=bigtable_admin_v2.Backup(
            source_table=table_path, expire_time=expire_time
        ),
    )
    backup = operation.result()
    print("Created backup {}.".format(backup.name.split("/")[-1]))
    # [END bigtable_create_backup]


def restore_table(project_id, instance_id, cluster_id, backup_id, restored_table_id):
    """Restore a backup into a new table.

    :type project_id: str
    :param project_id: Project id of the client.

    :type instance_id: str
    :param instance_id: Instance of the client.

    :type cluster_id: str
    :param cluster_id: Cluster that stores the backup.

    :type backup_id: str
    :param backup_id: Backup to restore from.

    :type restored_table_id: str
    :param restored_table_id: Id for the new table.
    """
    # [START bigtable_restore_table]
    from google.cloud import bigtable_admin_v2

    client = bigtable_admin_v2.BigtableTableAdminClient()
    instance_path = client.instance_path(project_id, instance_id)
    backup_path = client.backup_path(project_id, instance_id, cluster_id, backup_id)

    print("Restoring backup {} into table {}...".format(backup_id, restored_table_id))
    operation = client.restore_table(
        request={
            "parent": instance_path,
            "table_id": restored_table_id,
            "backup": backup_path,
        }
    )
    table = operation.result()
    print("Restored table {}.".format(table.name.split("/")[-1]))

    # Restoring can kick off a second operation that optimizes the new table
    # in the background. The table is usable before it finishes, so waiting
    # for it is optional.
    optimize_operation = operation.optimize_restored_table_operation()
    if optimize_operation is not None:
        print("Waiting for table {} to be optimized...".format(restored_table_id))
        optimize_operation.result()
        print("Table {} is optimized.".format(restored_table_id))
    # [END bigtable_restore_table]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("command", help="run, delete, wait, backup or restore.")
    parser.add_argument(
        "--table", help="Cloud Bigtable Table name.", default="Hello-Bigtable"
    )
    parser.add_argument(
        "--cluster", help="Cluster that stores the backup (backup/restore)."
    )
    parser.add_argument(
        "--backup", help="Backup id (backup/restore).", default="Hello-Bigtable-backup"
    )
    parser.add_argument("project_id", help="Your Cloud Platform project ID.")
    parser.add_argument(
        "instance_id", help="ID of the Cloud Bigtable instance to connect to."
    )

    args = parser.parse_args()

    if args.command.lower() == "run":
        run_table_operations(args.project_id, args.instance_id, args.table)
    elif args.command.lower() == "delete":
        delete_table(args.project_id, args.instance_id, args.table)
    elif args.command.lower() == "wait":
        wait_for_consistency(args.project_id, args.instance_id, args.table)
    elif args.command.lower() == "backup":
        create_backup(
            args.project_id, args.instance_id, args.cluster, args.table, args.backup
        )
    elif args.command.lower() == "restore":
        restore_table(
            args.project_id, args.instance_id, args.cluster, args.backup, args.table
        )
    else:
        print(
            "Command should be one of run, delete, wait, backup or restore.\n"
            "Use argument -h, --help to show help and exit."
        )
