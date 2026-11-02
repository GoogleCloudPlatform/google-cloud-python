# Copyright 2018 Google LLC
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

import json
import time
import unittest
from unittest import mock

import pandas as pd
import pytest
import requests

try:
    import spanner_graphs.graph_visualization as graph_visualization
except ImportError:
    graph_visualization = None

import bigquery_magics.graph_server as graph_server

alex_properties = {
    "birthday": "1991-12-21T08:00:00Z",
    "id": 7167971231403805684,
    "city": "Adelaide",
    "country": "Australia",
    "name": "Alex",
}

alex_account_properties = {
    "create_time": "2020-01-10T14:22:20.222Z",
    "id": 7,
    "is_blocked": False,
    "nick_name": "Vacation Fund",
}

alex_owns_account_edge_properites = {
    "account_id": 7,
    "create_time": "2020-01-10T14:22:20.222Z",
    "id": 1,
}

row_alex_owns_account = [
    {
        "identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQI=",
        "kind": "node",
        "labels": ["Person"],
        "properties": alex_properties,
    },
    {
        "destination_node_identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEO",
        "identifier": "mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJECkQ6ZRmluR3JhcGguUGVyc29uAHiRAplGaW5HcmFwaC5BY2NvdW50AHiRDg==",
        "kind": "edge",
        "labels": ["Owns"],
        "properties": alex_owns_account_edge_properites,
        "source_node_identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQI=",
    },
    {
        "identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEO",
        "kind": "node",
        "labels": ["Account"],
        "properties": alex_account_properties,
    },
]

row_alex_owns_account_converted = [
    {
        "identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQI=",
        "kind": "node",
        "labels": ["Person"],
        "properties": {
            "birthday": "1991-12-21T08:00:00Z",
            "id": "7167971231403805684",
            "city": "Adelaide",
            "country": "Australia",
            "name": "Alex",
        },
    },
    {
        "destination_node_identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEO",
        "identifier": "mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJECkQ6ZRmluR3JhcGguUGVyc29uAHiRAplGaW5HcmFwaC5BY2NvdW50AHiRDg==",
        "kind": "edge",
        "labels": ["Owns"],
        "properties": {
            "account_id": "7",
            "create_time": "2020-01-10T14:22:20.222Z",
            "id": "1",
        },
        "source_node_identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQI=",
    },
    {
        "identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEO",
        "kind": "node",
        "labels": ["Account"],
        "properties": {
            "create_time": "2020-01-10T14:22:20.222Z",
            "id": "7",
            "is_blocked": "False",
            "nick_name": "Vacation Fund",
        },
    },
]

lee_properties = {
    "birthday": "1986-12-07T08:00:00Z",
    "city": "Kollam",
    "country": "India",
    "id": 3,
    "name": "Lee",
}

lee_account_properties = {
    "create_time": "2020-01-28T01:55:09.206Z",
    "id": 16,
    "is_blocked": True,
    "nick_name": "Vacation Fund",
}

lee_owns_account_edge_properties = {
    "account_id": 16,
    "create_time": "2020-02-18T13:44:20.655Z",
    "id": 3,
}

row_lee_owns_account = [
    {
        "identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQY=",
        "kind": "node",
        "labels": ["Person"],
        "properties": lee_properties,
    },
    {
        "destination_node_identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEg",
        "identifier": "mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEGkSCZRmluR3JhcGguUGVyc29uAHiRBplGaW5HcmFwaC5BY2NvdW50AHiRIA==",
        "kind": "edge",
        "labels": ["Owns"],
        "properties": lee_owns_account_edge_properties,
        "source_node_identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQY=",
    },
    {
        "identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEg",
        "kind": "node",
        "labels": ["Account"],
        "properties": lee_account_properties,
    },
]

row_lee_owns_account_converted = [
    {
        "identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQY=",
        "kind": "node",
        "labels": ["Person"],
        "properties": {
            "birthday": "1986-12-07T08:00:00Z",
            "city": "Kollam",
            "country": "India",
            "id": "3",
            "name": "Lee",
        },
    },
    {
        "destination_node_identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEg",
        "identifier": "mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEGkSCZRmluR3JhcGguUGVyc29uAHiRBplGaW5HcmFwaC5BY2NvdW50AHiRIA==",
        "kind": "edge",
        "labels": ["Owns"],
        "properties": {
            "account_id": "16",
            "create_time": "2020-02-18T13:44:20.655Z",
            "id": "3",
        },
        "source_node_identifier": "mUZpbkdyYXBoLlBlcnNvbgB4kQY=",
    },
    {
        "identifier": "mUZpbkdyYXBoLkFjY291bnQAeJEg",
        "kind": "node",
        "labels": ["Account"],
        "properties": {
            "create_time": "2020-01-28T01:55:09.206Z",
            "id": "16",
            "is_blocked": "True",
            "nick_name": "Vacation Fund",
        },
    },
]


def _validate_nodes_and_edges(result):
    for edge in result["response"]["edges"]:
        assert "source_node_identifier" in edge
        assert "destination_node_identifier" in edge
        assert "identifier" in edge
        assert "Owns" in edge["labels"]
        assert "properties" in edge

    print(result["response"]["nodes"])
    for node in result["response"]["nodes"]:
        assert "identifier" in node
        assert "Account" in node["labels"] or "Person" in node["labels"]
        assert "properties" in node


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_one_column_no_rows():
    result = graph_server._convert_graph_data({"result": {}})
    assert result == {
        "response": {
            "edges": [],
            "nodes": [],
            "query_result": {"result": []},
            "schema": None,
        }
    }


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_one_column_one_row():
    result = graph_server._convert_graph_data(
        {
            "result": {
                "0": json.dumps(row_alex_owns_account),
            }
        }
    )

    assert len(result["response"]["nodes"]) == 2
    assert len(result["response"]["edges"]) == 1

    _validate_nodes_and_edges(result)

    assert result["response"]["query_result"] == {
        "result": [row_alex_owns_account_converted]
    }
    assert result["response"]["schema"] is None


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_one_column_two_rows_null_json():
    result = graph_server._convert_graph_data(
        {
            "result": {
                "0": None,
                "1": json.dumps(row_alex_owns_account),
            }
        }
    )

    # Null JSON element should be ignored in visualization, but should still be present in tabular view.
    assert len(result["response"]["nodes"]) == 2
    assert len(result["response"]["edges"]) == 1

    _validate_nodes_and_edges(result)

    assert result["response"]["query_result"] == {
        "result": ["NULL", row_alex_owns_account_converted]
    }
    assert result["response"]["schema"] is None

    _validate_nodes_and_edges(result)


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_one_column_two_rows():
    result = graph_server._convert_graph_data(
        {
            "result": {
                "0": json.dumps(row_alex_owns_account_converted),
                "1": json.dumps(row_lee_owns_account_converted),
            }
        }
    )

    assert len(result["response"]["nodes"]) == 4
    assert len(result["response"]["edges"]) == 2

    _validate_nodes_and_edges(result)

    assert result["response"]["query_result"] == {
        "result": [row_alex_owns_account_converted, row_lee_owns_account_converted]
    }
    assert result["response"]["schema"] is None


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_one_row_two_columns():
    result = graph_server._convert_graph_data(
        {
            "col1": {
                "0": json.dumps(row_alex_owns_account_converted),
            },
            "col2": {
                "0": json.dumps(row_lee_owns_account_converted),
            },
        }
    )

    assert len(result["response"]["nodes"]) == 4
    assert len(result["response"]["edges"]) == 2

    _validate_nodes_and_edges(result)

    assert result["response"]["query_result"] == {
        "col1": [row_alex_owns_account_converted],
        "col2": [row_lee_owns_account_converted],
    }
    assert result["response"]["schema"] is None


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_nongraph_json():
    # If we have valid json that doesn't represent a graph, we don't expect to get nodes and edges,
    # but we should at least have row data, allowing the tabular view to work.
    result = graph_server._convert_graph_data(
        {
            "result": {
                "0": json.dumps({"foo": 1, "bar": 2}),
            }
        }
    )

    assert len(result["response"]["nodes"]) == 0
    assert len(result["response"]["edges"]) == 0

    assert result["response"]["query_result"] == {"result": [{"foo": "1", "bar": "2"}]}
    assert result["response"]["schema"] is None


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_outer_key_not_string():
    result = graph_server._convert_graph_data(
        {
            0: {
                "0": json.dumps({"foo": 1, "bar": 2}),
            }
        }
    )
    assert result == {"error": "Expected outer key to be str, got <class 'int'>"}


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_outer_value_not_dict():
    result = graph_server._convert_graph_data({"result": 0})
    assert result == {"error": "Expected outer value to be dict, got <class 'int'>"}


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_inner_value_not_string():
    result = graph_server._convert_graph_data(
        {
            "col1": {
                "0": json.dumps(row_alex_owns_account),
            },
            "col2": {
                "0": 12345,
            },
        }
    )

    # Non-JSON column should be ignored in visualizer view, but still appear in tabular view.
    assert len(result["response"]["nodes"]) == 2
    assert len(result["response"]["edges"]) == 1

    _validate_nodes_and_edges(result)

    assert result["response"]["query_result"] == {
        "col1": [row_alex_owns_account_converted],
        "col2": ["12345"],
    }
    assert result["response"]["schema"] is None


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_empty_dict():
    result = graph_server._convert_graph_data({})
    assert result == {
        "response": {
            "nodes": [],
            "edges": [],
            "schema": None,
            "query_result": {},
        }
    }


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
def test_convert_wrong_row_index():
    result0 = graph_server._convert_graph_data(
        {
            "result": {
                "0": json.dumps(row_alex_owns_account),
            }
        }
    )

    # Changing the index should not impact the result.
    result1 = graph_server._convert_graph_data(
        {
            "result": {
                "1": json.dumps(row_alex_owns_account),
            }
        }
    )

    assert result1 == result0


class TestGraphServer(unittest.TestCase):
    def setUp(self):
        if graph_visualization is not None:  # pragma: NO COVER
            self.server_thread = graph_server.graph_server.init()

    def tearDown(self):
        if graph_visualization is not None:  # pragma: NO COVER
            graph_server.graph_server.stop_server()  # Stop the server after each test
            self.server_thread.join()  # Wait for the thread to finish

    @pytest.mark.skipif(
        graph_visualization is None, reason="Requires `spanner-graph-notebook`"
    )
    def test_get_ping(self):
        self.assertTrue(self.server_thread.is_alive())

        route = graph_server.graph_server.build_route(
            graph_server.GraphServer.endpoints["get_ping"]
        )
        response = requests.get(route)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "pong"})

    @pytest.mark.skipif(
        graph_visualization is None, reason="Requires `spanner-graph-notebook`"
    )
    def test_post_ping(self):
        self.assertTrue(self.server_thread.is_alive())
        route = graph_server.graph_server.build_route(
            graph_server.GraphServer.endpoints["post_ping"]
        )
        response = requests.post(route, json={"data": "ping"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"your_request": {"data": "ping"}})

    @pytest.mark.skipif(
        graph_visualization is None, reason="Requires `spanner-graph-notebook`"
    )
    def test_post_query(self):
        self.assertTrue(self.server_thread.is_alive())
        route = graph_server.graph_server.build_route(
            graph_server.GraphServer.endpoints["post_query"]
        )

        data = {
            "query_result": {
                "result": {
                    "0": json.dumps(row_alex_owns_account),
                }
            }
        }
        response = requests.post(route, json={"params": json.dumps(data)})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()["response"]

        self.assertEqual(len(response_data["nodes"]), 2)
        self.assertEqual(len(response_data["edges"]), 1)

        _validate_nodes_and_edges(response.json())

        self.assertEqual(
            response_data["query_result"], {"result": [row_alex_owns_account_converted]}
        )
        self.assertIsNone(response_data["schema"])

    @pytest.mark.skipif(
        graph_visualization is None, reason="Requires `spanner-graph-notebook`"
    )
    def test_post_query_from_table(self):
        self.assertTrue(self.server_thread.is_alive())
        route = graph_server.graph_server.build_route(
            graph_server.GraphServer.endpoints["post_query"]
        )

        params = {
            "destination_table": {"projectId": "p", "datasetId": "d", "tableId": "t"},
            "args": {
                "project": "p",
                "bigquery_api_endpoint": "e",
                "location": "l",
            },
        }

        with mock.patch("bigquery_magics.core.create_bq_client") as mock_create:
            mock_client = mock.Mock()
            mock_create.return_value = mock_client
            mock_df = pd.DataFrame(
                [json.dumps(row_alex_owns_account)], columns=["result"]
            )
            mock_client.list_rows.return_value.to_dataframe.return_value = mock_df

            response = requests.post(route, json={"params": json.dumps(params)})
            self.assertEqual(response.status_code, 200)

            mock_create.assert_called_once_with(
                project="p", bigquery_api_endpoint="e", location="l"
            )
            mock_client.list_rows.assert_called_once()

        response_data = response.json()["response"]
        self.assertEqual(len(response_data["nodes"]), 2)
        self.assertEqual(len(response_data["edges"]), 1)

        _validate_nodes_and_edges(response.json())

        self.assertEqual(
            response_data["query_result"], {"result": [row_alex_owns_account_converted]}
        )
        self.assertIsNone(response_data["schema"])

    @pytest.mark.skipif(
        graph_visualization is None, reason="Requires `spanner-graph-notebook`"
    )
    def test_post_node_expansion(self):
        self.assertTrue(self.server_thread.is_alive())
        route = graph_server.graph_server.build_route(
            graph_server.GraphServer.endpoints["post_node_expansion"]
        )
        request = {
            "request": {
                "uid": "test_uid",
                "node_labels": ["label1, label2"],
                "node_properites": {},
                "direction": "INCOMING",
                "edge_label": None,
            },
            "params": "{}",
        }
        response = requests.post(route, json={"params": json.dumps(request)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"error": "Node expansion not yet implemented"}
        )

    @pytest.mark.skipif(
        graph_visualization is None, reason="Requires `spanner-graph-notebook`"
    )
    def test_post_node_expansion_invalid_request(self):
        self.assertTrue(self.server_thread.is_alive())
        route = graph_server.graph_server.build_route(
            graph_server.GraphServer.endpoints["post_node_expansion"]
        )
        request = {}
        response = requests.post(route, json={"params": json.dumps(request)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"error": "Node expansion not yet implemented"}
        )


def test_stop_server_never_started():
    graph_server.graph_server.stop_server()


def test_convert_schema():
    input_schema = {
        "propertyGraphReference": {"propertyGraphId": "LDBC_SNB"},
        "nodeTables": [
            {
                "name": "PersonNode",
                "dataSourceTable": {"tableId": "PersonTable"},
                "keyColumns": ["id"],
                "labelAndProperties": [
                    {
                        "label": "Person",
                        "properties": [
                            {
                                "name": "name",
                                "dataType": {"typeKind": "STRING"},
                                "expression": "p_name",
                            }
                        ],
                    }
                ],
            }
        ],
        "edgeTables": [
            {
                "name": "KnowsEdge",
                "dataSourceTable": {"tableId": "KnowsTable"},
                "keyColumns": ["p1", "p2"],
                "sourceNodeReference": {
                    "nodeTable": "PersonNode",
                    "edgeTableColumns": ["p1"],
                    "nodeTableColumns": ["id"],
                },
                "destinationNodeReference": {
                    "nodeTable": "PersonNode",
                    "edgeTableColumns": ["p2"],
                    "nodeTableColumns": ["id"],
                },
                "labelAndProperties": [
                    {
                        "label": "KNOWS",
                        "properties": [
                            {
                                "name": "since",
                                "dataType": {"typeKind": "DATE"},
                                "expression": "k_since",
                            }
                        ],
                    }
                ],
            }
        ],
    }

    schema_json = json.dumps(input_schema)
    result_json = graph_server._convert_schema(schema_json)
    result = json.loads(result_json)

    assert result["name"] == "LDBC_SNB"
    assert len(result["nodeTables"]) == 1
    assert result["nodeTables"][0]["name"] == "PersonNode"
    assert result["nodeTables"][0]["baseTableName"] == "PersonTable"
    assert result["nodeTables"][0]["kind"] == "NODE"
    assert result["nodeTables"][0]["labelNames"] == ["Person"]
    assert result["nodeTables"][0]["propertyDefinitions"] == [
        {"propertyDeclarationName": "name", "valueExpressionSql": "p_name"}
    ]

    assert len(result["edgeTables"]) == 1
    assert result["edgeTables"][0]["name"] == "KnowsEdge"
    assert result["edgeTables"][0]["baseTableName"] == "KnowsTable"
    assert result["edgeTables"][0]["kind"] == "EDGE"
    assert result["edgeTables"][0]["labelNames"] == ["KNOWS"]
    assert result["edgeTables"][0]["sourceNodeTable"]["nodeTableName"] == "PersonNode"
    assert (
        result["edgeTables"][0]["destinationNodeTable"]["nodeTableName"] == "PersonNode"
    )
    assert result["edgeTables"][0]["propertyDefinitions"] == [
        {"propertyDeclarationName": "since", "valueExpressionSql": "k_since"}
    ]

    assert len(result["labels"]) == 2
    labels = {label["name"]: label for label in result["labels"]}
    assert "Person" in labels
    assert "name" in labels["Person"]["propertyDeclarationNames"]
    assert "KNOWS" in labels
    assert "since" in labels["KNOWS"]["propertyDeclarationNames"]

    assert len(result["propertyDeclarations"]) == 2
    props = {p["name"]: p for p in result["propertyDeclarations"]}
    assert props["name"]["type"] == "STRING"
    assert props["since"]["type"] == "DATE"


def test_convert_schema_empty():
    input_schema = {
        "propertyGraphReference": {"propertyGraphId": "EmptyGraph"},
        "nodeTables": [],
        "edgeTables": [],
    }

    schema_json = json.dumps(input_schema)
    result_json = graph_server._convert_schema(schema_json)
    result = json.loads(result_json)

    assert result["name"] == "EmptyGraph"
    assert result["nodeTables"] == []
    assert result["edgeTables"] == []
    assert result["labels"] == []
    assert result["propertyDeclarations"] == []


def test_convert_schema_shared_label():
    """Test _convert_schema where multiple tables share the same label."""
    input_schema = {
        "propertyGraphReference": {"propertyGraphId": "SharedLabelGraph"},
        "nodeTables": [
            {
                "name": "PersonA",
                "dataSourceTable": {"tableId": "TableA"},
                "labelAndProperties": [
                    {
                        "label": "Person",
                        "properties": [
                            {
                                "name": "id",
                                "dataType": {"typeKind": "INT64"},
                                "expression": "id",
                            }
                        ],
                    }
                ],
            },
            {
                "name": "PersonB",
                "dataSourceTable": {"tableId": "TableB"},
                "labelAndProperties": [
                    {
                        "label": "Person",
                        "properties": [
                            {
                                "name": "name",
                                "dataType": {"typeKind": "STRING"},
                                "expression": "name",
                            }
                        ],
                    }
                ],
            },
        ],
        "edgeTables": [],
    }

    schema_json = json.dumps(input_schema)
    result_json = graph_server._convert_schema(schema_json)
    result = json.loads(result_json)

    # Verify that the 'Person' label includes properties from both tables
    labels = {label["name"]: label for label in result["labels"]}
    assert "Person" in labels
    assert set(labels["Person"]["propertyDeclarationNames"]) == {"id", "name"}


@pytest.mark.skipif(
    graph_visualization is None, reason="Requires `spanner-graph-notebook`"
)
class TestGraphServerHostHeader(unittest.TestCase):
    def setUp(self):
        self.server = graph_server.GraphServer()
        self.server_thread = self.server.init()

    def tearDown(self):
        self.server.stop_server()
        self.server_thread.join()

    def _route(self):
        return self.server.build_route(graph_server.GraphServer.endpoints["get_ping"])

    def test_loopback_host_allowed(self):
        response = requests.get(self._route())
        self.assertEqual(response.status_code, 200)

    def test_loopback_host_allowed_post(self):
        route = self.server.build_route(graph_server.GraphServer.endpoints["post_ping"])
        response = requests.post(route, json={"data": "ping"})
        self.assertEqual(response.status_code, 200)

    def test_non_loopback_host_rejected(self):
        # A DNS-rebinding page reaches the loopback socket but carries the
        # attacker's hostname in the Host header.
        response = requests.get(self._route(), headers={"Host": "attacker.example"})
        self.assertEqual(response.status_code, 403)

    def test_non_loopback_host_rejected_post(self):
        route = self.server.build_route(graph_server.GraphServer.endpoints["post_ping"])
        response = requests.post(
            route, json={"data": "ping"}, headers={"Host": "evil.example:1234"}
        )
        self.assertEqual(response.status_code, 403)

    def test_missing_host_rejected(self):
        handler = mock.Mock(spec=graph_server.GraphServerHandler)
        handler.headers = {}
        self.assertFalse(graph_server.GraphServerHandler._is_request_safe(handler))

    def test_malformed_host_rejected(self):
        # An unterminated IPv6 literal makes urlsplit raise ValueError.
        handler = mock.Mock(spec=graph_server.GraphServerHandler)
        handler.headers = {"Host": "[::1"}
        self.assertFalse(graph_server.GraphServerHandler._is_request_safe(handler))

    def test_non_loopback_origin_rejected(self):
        # Host header is valid (loopback), but Origin is a malicious third-party site.
        response = requests.get(
            self._route(),
            headers={"Host": "localhost", "Origin": "http://attacker.example.com"},
        )
        self.assertEqual(response.status_code, 403)

    def test_non_loopback_referer_rejected(self):
        # Host header is valid (loopback), but Referer reveals a malicious third-party origin.
        response = requests.get(
            self._route(),
            headers={
                "Host": "127.0.0.1",
                "Referer": "http://attacker.example.com/exploit-page",
            },
        )
        self.assertEqual(response.status_code, 403)

    def test_malformed_origin_rejected(self):
        # An unterminated IPv6 literal in Origin makes urlsplit raise ValueError.
        handler = mock.Mock(spec=graph_server.GraphServerHandler)
        handler.headers = {"Host": "localhost", "Origin": "http://[::1"}
        self.assertFalse(graph_server.GraphServerHandler._is_request_safe(handler))

    def test_loopback_origin_and_referer_allowed(self):
        response = requests.get(
            self._route(),
            headers={
                "Host": "localhost",
                "Origin": "http://localhost:8080",
                "Referer": "http://127.0.0.1:8080/notebook",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_null_origin_rejected(self):
        # Sandboxed iframes and data: URIs send "Origin: null", where
        # urlsplit("null").hostname is None.
        response = requests.get(
            self._route(),
            headers={"Host": "localhost", "Origin": "null"},
        )
        self.assertEqual(response.status_code, 403)


def test_stop_server_immediately_after_init():
    """Verifies that GraphServer.init() waits until the underlying TCP server
    is initialized before returning, preventing a race condition with stop_server().
    """
    # Mock portpicker to return port 0 (OS-assigned ephemeral port) so this test
    # runs in all unit test environments, even when optional dependencies like
    # `spanner-graph-notebook` and `portpicker` are not installed.
    mock_portpicker = mock.MagicMock()
    mock_portpicker.pick_unused_port.return_value = 0

    with mock.patch.dict("sys.modules", {"portpicker": mock_portpicker}):
        server = graph_server.GraphServer()
        server_thread = server.init()

        try:
            # 1. Immediately call stop_server() after init() without making any HTTP
            #    requests. If init() returns before `self._server` is assigned in
            #    _start_server(), `if self._server:` inside stop_server() evaluates to
            #    False, making stop_server() a no-op.
            server.stop_server()

            # 2. Wait up to 1.0 second for the background server thread to exit.
            #    When properly synchronized, init() blocks until `self._server` is
            #    assigned, so stop_server() calls `self._server.shutdown()` and the
            #    thread exits almost immediately. If the shutdown signal is missed,
            #    the background thread remains blocked in `serve_forever()`. Using
            #    `timeout=1.0` prevents `join()` from hanging indefinitely.
            server_thread.join(timeout=1.0)

            # 3. Assert that the server thread actually terminated.
            assert not server_thread.is_alive(), (
                "GraphServer thread is still alive after stop_server(); "
                "stop_server() likely raced with _start_server() before self._server was set."
            )
        finally:
            # 4. Cleanup in case the assertion above fails:
            #    Because `server_thread` is a non-daemon thread, Python's interpreter
            #    shutdown (`threading._shutdown()`) will hang at the end of the pytest
            #    run if `server_thread` is left running.
            if server_thread.is_alive():  # pragma: NO COVER
                # Poll with a short `time.sleep()` (releasing the GIL so the background
                # thread can finish binding the socket and setting `server._server`)
                # up to a bounded deadline.
                deadline = time.monotonic() + 5.0
                while server._server is None and time.monotonic() < deadline:
                    time.sleep(0.01)

                # Shut down the server so the background thread exits cleanly.
                server.stop_server()
                server_thread.join(timeout=2.0)
