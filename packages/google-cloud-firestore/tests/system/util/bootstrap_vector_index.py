# Copyright 2024 Google LLC
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
"""A script to bootstrap vector data and vector index for system tests."""

from google.api_core.client_options import ClientOptions
from google.cloud.client import ClientWithProject  # type: ignore

from google.cloud.firestore import Client
from google.cloud.firestore_admin_v1.services.firestore_admin import (
    client as firestore_admin_client,
)
from google.cloud.firestore_admin_v1.services.firestore_admin.transports import (
    grpc as firestore_grpc_transport,
)
from google.cloud.firestore_admin_v1.types import Index
from google.cloud.firestore_v1.vector import Vector

PROJECT_ID = "{project-id}"
DATABASE_ID = "(default)"
COLLECTION_ID = "vector_search"
TARGET_HOSTNAME = "firestore.googleapis.com"
EMBEDDING_FIELD = "embedding"


class FirestoreAdminClient(ClientWithProject):
    def __init__(
        self,
        project=None,
        client_options=None,
    ) -> None:
        super(FirestoreAdminClient, self).__init__(
            project=project,
            credentials=None,
            _http=None,
        )

        self._firestore_admin_api = self._init_admin_api()

    def _init_admin_api(self):
        channel = firestore_grpc_transport.FirestoreAdminGrpcTransport.create_channel(
            TARGET_HOSTNAME,
            credentials=self._credentials,
            options={"grpc.keepalive_time_ms": 30000}.items(),
        )

        self._transport = firestore_grpc_transport.FirestoreAdminGrpcTransport(
            host=TARGET_HOSTNAME, channel=channel
        )

        # Create a GAPIC client to use admin operation
        return firestore_admin_client.FirestoreAdminClient(transport=self._transport)

    def create_vector_index(self, parent):
        self._firestore_admin_api.create_index(
            parent=parent,
            index=Index(
                query_scope=Index.QueryScope.COLLECTION,
                fields=[
                    Index.IndexField(
                        field_path="embedding",
                        vector_config=Index.IndexField.VectorConfig(
                            dimension=3, flat=Index.IndexField.VectorConfig.FlatIndex()
                        ),
                    ),
                ],
            ),
        )

        self._firestore_admin_api.create_index(
            parent=parent,
            index=Index(
                query_scope=Index.QueryScope.COLLECTION,
                fields=[
                    Index.IndexField(
                        field_path="color",
                        order=Index.IndexField.Order.ASCENDING,
                    ),
                    Index.IndexField(
                        field_path="embedding",
                        vector_config=Index.IndexField.VectorConfig(
                            dimension=3, flat=Index.IndexField.VectorConfig.FlatIndex()
                        ),
                    ),
                ],
            ),
        )

        self._firestore_admin_api.create_index(
            parent=parent,
            index=Index(
                query_scope=Index.QueryScope.COLLECTION_GROUP,
                fields=[
                    Index.IndexField(
                        field_path="embedding",
                        vector_config=Index.IndexField.VectorConfig(
                            dimension=3, flat=Index.IndexField.VectorConfig.FlatIndex()
                        ),
                    ),
                ],
            ),
        )

        self._firestore_admin_api.create_index(
            parent=parent,
            index=Index(
                query_scope=Index.QueryScope.COLLECTION_GROUP,
                fields=[
                    Index.IndexField(
                        field_path="color",
                        order=Index.IndexField.Order.ASCENDING,
                    ),
                    Index.IndexField(
                        field_path="embedding",
                        vector_config=Index.IndexField.VectorConfig(
                            dimension=3, flat=Index.IndexField.VectorConfig.FlatIndex()
                        ),
                    ),
                ],
            ),
        )


def create_vector_documents(client, collection_id):
    document1 = client.document(collection_id, "doc1")
    document2 = client.document(collection_id, "doc2")
    document3 = client.document(collection_id, "doc3")
    document1.set({"embedding": Vector([1.0, 2.0, 3.0]), "color": "red"})
    document2.set({"embedding": Vector([2.0, 2.0, 3.0]), "color": "red"})
    document3.set({"embedding": Vector([3.0, 4.0, 5.0]), "color": "yellow"})


def main():
    client_options = ClientOptions(api_endpoint=TARGET_HOSTNAME)
    client = Client(
        project=PROJECT_ID, database=DATABASE_ID, client_options=client_options
    )
    create_vector_documents(client=client, collection_id=COLLECTION_ID)
    admin_client = FirestoreAdminClient(project=PROJECT_ID)
    admin_client.create_vector_index(
        parent="projects/{}/databases/{}/collectionGroups/{}".format(
            PROJECT_ID, DATABASE_ID, COLLECTION_ID
        )
    )


if __name__ == "__main__":
    main()
