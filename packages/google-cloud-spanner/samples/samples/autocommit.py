# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import argparse

from google.cloud.spanner_dbapi import connect


def enable_autocommit_mode(instance_id, database_id):
    """Enables autocommit mode."""
    # [START spanner_enable_autocommit_mode]

    connection = connect(instance_id, database_id)
    connection.autocommit = True
    print("Autocommit mode is enabled.")

    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)"""
    )

    cursor.execute(
        """INSERT INTO Singers (SingerId, FirstName, LastName) VALUES
            (12, 'Melissa', 'Garcia'),
            (13, 'Russell', 'Morales'),
            (14, 'Jacqueline', 'Long'),
            (15, 'Dylan', 'Shaw')"""
    )

    cursor.execute("""SELECT * FROM Singers WHERE SingerId = 13""")

    print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*cursor.fetchone()))

    connection.close()
    # [END spanner_enable_autocommit_mode]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("instance_id", help="Your Cloud Spanner instance ID.")
    parser.add_argument(
        "--database-id",
        help="Your Cloud Spanner database ID.",
        default="example_db",
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("enable_autocommit_mode", help=enable_autocommit_mode.__doc__)
    args = parser.parse_args()
    if args.command == "enable_autocommit_mode":
        enable_autocommit_mode(args.instance_id, args.database_id)
    else:
        print(f"Command {args.command} did not match expected commands.")
