# Copyright 2026 Google, Inc.
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

import uuid

from google.api_core.exceptions import GoogleAPIError, MethodNotImplemented
import pytest

import queue_snippets


def test_queue_operations(capsys, instance_id, sample_instance):
    database_id = f"test-db-{uuid.uuid4().hex[:10]}"
    queue_id = f"test_queue_{uuid.uuid4().hex[:10]}"

    try:
        # Create database with queue
        queue_snippets.create_database_with_queue(instance_id, database_id, queue_id)
        out, _ = capsys.readouterr()
        assert "Created database" in out
        assert queue_id in out
    except MethodNotImplemented as e:
        pytest.skip(f"Queues are not implemented yet: {e}")
    except GoogleAPIError as e:
        grpc_status_name = getattr(getattr(e, "grpc_status_code", None), "name", None)
        if (
            getattr(e, "code", None) == 501
            or grpc_status_name == "UNIMPLEMENTED"
            or "UNIMPLEMENTED" in str(e)
        ):
            pytest.skip(f"Queues are not implemented yet: {e}")
        raise

    try:
        # Send with Mutation API
        queue_snippets.send_to_queue_with_mutation_api(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert "Message sent to queue using Mutation API" in out

        # Send with SQL API
        queue_snippets.send_to_queue_with_sql_api(instance_id, database_id, queue_id)
        out, _ = capsys.readouterr()
        assert "message(s) sent using SQL API" in out

        # Send with Mutation API in future
        queue_snippets.send_to_queue_with_mutation_api_in_future(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert (
            "Message sent to queue using Mutation API to be delivered in the future"
            in out
        )

        # Send with SQL API in future
        queue_snippets.send_to_queue_with_sql_api_in_future(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert (
            "message(s) sent using SQL API in the future" in out
            or "Failed to insert with _deliver_time" in out
        )

        # Ack with Mutation API
        queue_snippets.ack_queue_message_with_mutation_api(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert "Message acked using Mutation API" in out

        # Ack with SQL API
        queue_snippets.ack_queue_message_with_sql_api(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert "message(s) acked using SQL API" in out

        # Delete with SQL API
        queue_snippets.delete_queue_message_with_sql_api(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert "message(s) deleted using SQL API" in out

        # Send and receive with SQL API
        queue_snippets.send_and_receive_queue_message_with_sql_api(
            instance_id, database_id, queue_id
        )
        out, _ = capsys.readouterr()
        assert "Received message: Id=5, Payload=Hello, SQL receive API!" in out

    finally:
        # Cleanup
        from google.cloud import spanner

        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
        database_admin_api.drop_database(
            database=database_admin_api.database_path(
                spanner_client.project, instance_id, database_id
            )
        )
