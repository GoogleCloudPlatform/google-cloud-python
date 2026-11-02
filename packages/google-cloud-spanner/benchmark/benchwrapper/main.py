# Copyright 2022 Google LLC
#
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

"""The gRPC Benchwrapper around Python Client Library.
Usage:
  # Start the emulator using either docker or gcloud CLI.

  # Set up instance and load data into database.

  # Set up environment variables.
  $ export SPANNER_EMULATOR_HOST=localhost:9010

  # Run the benchmark from python-spanner/ directory.
  $ python3 -m benchmark.benchwrapper.main --port 8081

"""

from concurrent import futures
from optparse   import OptionParser

import os

import benchmark.benchwrapper.proto.spanner_pb2      as spanner_messages
import benchmark.benchwrapper.proto.spanner_pb2_grpc as spanner_service

from google.cloud import spanner

import grpc

################################## CONSTANTS ##################################

SPANNER_PROJECT  = "someproject"
SPANNER_INSTANCE = "someinstance"
SPANNER_DATABASE = "somedatabase"

###############################################################################


class SpannerBenchWrapperService(spanner_service.SpannerBenchWrapperServicer):
    """Benchwrapper Servicer class to implement Read, Insert and Update
    methods.

    :type project_id: str
    :param project_id: Spanner project.

    :type instance_id: str
    :param instance_id: The ID of instance that owns the database.

    :type database_id: str
    :param database_id: the ID of the database.
    """

    def __init__(self,
                 project_id=SPANNER_PROJECT,
                 instance_id=SPANNER_INSTANCE,
                 database_id=SPANNER_DATABASE) -> None:

        spanner_client = spanner.Client(project_id)
        instance = spanner_client.instance(instance_id)
        self.database = instance.database(database_id)

        super().__init__()

    def Read(self, request, _):
        """Read represents operations like Go's ReadOnlyTransaction.Query,
        Java's ReadOnlyTransaction.executeQuery, Python's snapshot.read, and
        Node's Transaction.Read.

        It will typically be used to read many items.

        :type request:
            :class: `benchmark.benchwrapper.proto.spanner_pb2.ReadQuery`
        :param request: A ReadQuery request object.

        :rtype: :class:`benchmark.benchwrapper.proto.spanner_pb2.EmptyResponse`
        :returns: An EmptyResponse object.
        """
        with self.database.snapshot() as snapshot:
            # Stream the response to the query.
            list(snapshot.execute_sql(request.query))

        return spanner_messages.EmptyResponse()

    def Insert(self, request, _):
        """Insert represents operations like Go's Client.Apply, Java's
        DatabaseClient.writeAtLeastOnce, Python's transaction.commit, and Node's
        Transaction.Commit.

        It will typically be used to insert many items.

        :type request:
            :class: `benchmark.benchwrapper.proto.spanner_pb2.InsertQuery`
        :param request: An InsertQuery request object.

        :rtype: :class:`benchmark.benchwrapper.proto.spanner_pb2.EmptyResponse`
        :returns: An EmptyResponse object.
        """
        with self.database.batch() as batch:
            batch.insert(
                table="Singers",
                columns=("SingerId", "FirstName", "LastName"),
                values=[(i.id, i.first_name, i.last_name) for i in request.singers],
            )

        return spanner_messages.EmptyResponse()

    def Update(self, request, _):
        """Update represents operations like Go's
        ReadWriteTransaction.BatchUpdate, Java's TransactionRunner.run,
        Python's Batch.update, and Node's Transaction.BatchUpdate.

        It will typically be used to update many items.

        :type request:
            :class: `benchmark.benchwrapper.proto.spanner_pb2.UpdateQuery`
        :param request: An UpdateQuery request object.

        :rtype: :class:`benchmark.benchwrapper.proto.spanner_pb2.EmptyResponse`
        :returns: An EmptyResponse object.
        """
        self.database.run_in_transaction(self.update_singers, request.queries)

        return spanner_messages.EmptyResponse()

    def update_singers(self, transaction, stmts):
        """Method to execute batch_update in a transaction.

        :type transaction:
            :class: `google.cloud.spanner_v1.transaction.Transaction`
        :param transaction: A Spanner Transaction object.
        :type stmts:
            :class: `google.protobuf.pyext._message.RepeatedScalarContainer`
        :param stmts: Statements which are update queries.
        """
        transaction.batch_update(stmts)


def get_opts():
    """Parse command line arguments."""
    parser = OptionParser()
    parser.add_option("-p", "--port", help="Specify a port to run on")

    opts, _ = parser.parse_args()

    return opts


def validate_opts(opts):
    """Validate command line arguments."""
    if opts.port is None:
        raise ValueError("Please specify a valid port, e.g., -p 5000 or "
                         "--port 5000.")


def start_grpc_server(num_workers, port):
    """Method to start the GRPC server."""
    # Instantiate the GRPC server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=num_workers))

    # Instantiate benchwrapper service.
    spanner_benchwrapper_service = SpannerBenchWrapperService()

    # Add benchwrapper servicer to server.
    spanner_service.add_SpannerBenchWrapperServicer_to_server(
        spanner_benchwrapper_service, server)

    # Form the server address.
    addr = "localhost:{0}".format(port)

    # Add the port, and start the server.
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()


def serve():
    """Driver method."""
    if "SPANNER_EMULATOR_HOST" not in os.environ:
        raise ValueError("This benchmarking server only works when connected "
                         "to an emulator. Please set SPANNER_EMULATOR_HOST.")

    opts = get_opts()

    validate_opts(opts)

    start_grpc_server(10, opts.port)


if __name__ == "__main__":
    serve()
