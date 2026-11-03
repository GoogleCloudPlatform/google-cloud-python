# Copyright 2024 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import atexit
import http.server
import json
import socketserver
import threading
import urllib.parse
from typing import Any, Dict, List

from google.cloud import bigquery

from bigquery_magics import core

# The graph widget only ever reaches this server over the loopback interface.
# Requests carrying any other Host are cross-site (e.g. a DNS-rebinding page in
# the notebook user's browser) and are refused.
_LOOPBACK_HOSTS = frozenset({"localhost", "127.0.0.1", "::1"})


def execute_node_expansion(params, request):
    return {"error": "Node expansion not yet implemented"}


def _stringify_value(value: Any):
    if value is None:
        return "NULL"
    return str(value)


def _stringify_properties(d: Any) -> Any:
    """
    Recursively traverses a dictionary, converting all numeric values (int and float) to strings.

    Args:
        d: The dictionary to be traversed.

    Returns:
        A new dictionary with numeric values converted to strings.
    """
    if isinstance(d, dict):
        new_dict = {}
        for key, value in d.items():
            new_dict[key] = _stringify_properties(value)
        return new_dict
    elif isinstance(d, list):
        new_list = []
        for item in d:
            new_list.append(_stringify_properties(item))
        return new_list
    else:
        return _stringify_value(d)


def _convert_schema(schema_json: str) -> str:
    """
    Converts a JSON string from the BigQuery schema format to the format
    expected by the visualization framework.

    Args:
        schema_json: The input JSON string in the BigQuery schema format.

    Returns:
        The converted JSON string in the visualization framework format.
    """
    data = json.loads(schema_json)

    graph_id = data.get("propertyGraphReference", {}).get(
        "propertyGraphId", "SampleGraph"
    )

    output = {
        "catalog": "",
        "name": graph_id,
        "schema": "",
        "labels": [],
        "nodeTables": [],
        "edgeTables": [],
        "propertyDeclarations": [],
    }

    labels_dict = {}  # name -> set of property names
    props_dict = {}  # name -> type

    def process_table(table, kind):
        name = table.get("name")
        base_table_name = table.get("dataSourceTable", {}).get("tableId")
        key_columns = table.get("keyColumns", [])

        label_names = []
        property_definitions = []

        for lp in table.get("labelAndProperties", []):
            label = lp.get("label")
            label_names.append(label)

            if label not in labels_dict:
                labels_dict[label] = set()

            for prop in lp.get("properties", []):
                prop_name = prop.get("name")
                prop_type = prop.get("dataType", {}).get("typeKind")
                prop_expr = prop.get("expression")

                labels_dict[label].add(prop_name)
                props_dict[prop_name] = prop_type

                property_definitions.append(
                    {
                        "propertyDeclarationName": prop_name,
                        "valueExpressionSql": prop_expr,
                    }
                )

        entry = {
            "name": name,
            "baseTableName": base_table_name,
            "kind": kind,
            "labelNames": label_names,
            "keyColumns": key_columns,
            "propertyDefinitions": property_definitions,
        }

        if kind == "EDGE":
            src = table.get("sourceNodeReference", {})
            dst = table.get("destinationNodeReference", {})

            entry["sourceNodeTable"] = {
                "nodeTableName": src.get("nodeTable"),
                "edgeTableColumns": src.get("edgeTableColumns"),
                "nodeTableColumns": src.get("nodeTableColumns"),
            }
            entry["destinationNodeTable"] = {
                "nodeTableName": dst.get("nodeTable"),
                "edgeTableColumns": dst.get("edgeTableColumns"),
                "nodeTableColumns": dst.get("nodeTableColumns"),
            }

        return entry

    for nt in data.get("nodeTables", []):
        output["nodeTables"].append(process_table(nt, "NODE"))

    for et in data.get("edgeTables", []):
        output["edgeTables"].append(process_table(et, "EDGE"))

    for label_name, prop_names in labels_dict.items():
        output["labels"].append(
            {
                "name": label_name,
                "propertyDeclarationNames": sorted(list(prop_names)),
            }
        )

    for prop_name, prop_type in props_dict.items():
        output["propertyDeclarations"].append({"name": prop_name, "type": prop_type})

    return json.dumps(output, indent=2)


def _convert_graph_data(query_results: Dict[str, Dict[str, str]], schema: Dict = None):
    """
    Converts graph data to the form expected by the visualization framework.

    Receives graph data as a dictionary, produced by converting the underlying
    DataFrame representing the query results into JSON, then into a
    python dictionary. Converts it into a form expected by the visualization
    framework.

    Args:
        query_results:
            A dictionary with one key/value pair per column. For each column:
            - The key is the name of the column (str)
            - The value is another dictionary with one key/value pair per row.
              Row each row:
              - The key is a string that specifies the integer index of the row
                (e.g. '0', '1', '2')
              - The value is a JSON string containing the result of the query
                for the current row/column. (Note: We only support graph
                visualization for columns of type JSON).
        schema:
            A dictionary containing the schema for the graph.
    """
    # Delay spanner imports until this function is called to avoid making
    # spanner-graph-notebook (and its dependencies) hard requirements for bigquery
    # magics users, who don't need graph visualization.
    #
    # Note that these imports do not need to be in a try/except, as this function
    # does not even get called unless spanner_graphs has already been confirmed
    # to exist upstream.
    from spanner_graphs.conversion import get_nodes_edges
    from spanner_graphs.database import SpannerFieldInfo

    try:
        fields: List[SpannerFieldInfo] = []
        data = {}
        tabular_data = {}
        for key, value in query_results.items():
            column_name = None
            column_value = None
            if not isinstance(key, str):
                raise ValueError(f"Expected outer key to be str, got {type(key)}")
            if not isinstance(value, dict):
                raise ValueError(f"Expected outer value to be dict, got {type(value)}")
            column_name = key
            column_value = value

            fields.append(SpannerFieldInfo(name=column_name, typename="JSON"))
            data[column_name] = []
            tabular_data[column_name] = []
            for value_key, value_value in column_value.items():
                try:
                    raw_row_json = json.loads(value_value)
                except (ValueError, TypeError):
                    # Non-JSON columns cannot be visualized, but we still want them
                    # in the tabular view.
                    tabular_data[column_name].append(_stringify_value(value_value))
                    continue
                row_json = _stringify_properties(raw_row_json)

                data[column_name].append(row_json)
                tabular_data[column_name].append(row_json)

        nodes, edges = get_nodes_edges(data, fields, schema_json=schema)

        # Convert nodes and edges to json objects.
        # (Unfortunately, the code coverage tooling does not allow this
        #  to be expressed as list comprehension).
        nodes_json = []
        for node in nodes:
            nodes_json.append(node.to_json())
        edges_json = []
        for edge in edges:
            edges_json.append(edge.to_json())

        return {
            "response": {
                # These fields populate the graph result view.
                "nodes": nodes_json,
                "edges": edges_json,
                # This populates the visualizer's schema view.
                "schema": schema,
                # This field is used to populate the visualizer's tabular view.
                "query_result": tabular_data,
            }
        }
    except Exception as e:
        return {"error": getattr(e, "message", str(e))}


def convert_graph_params(params: Dict[str, Any]):
    query_results = None
    if "query_result" in params:
        query_results = params["query_result"]
    else:
        bq_client = core.create_bq_client(
            project=params["args"]["project"],
            bigquery_api_endpoint=params["args"]["bigquery_api_endpoint"],
            location=params["args"]["location"],
        )

        table_ref = bigquery.TableReference.from_api_repr(params["destination_table"])
        query_results = json.loads(
            bq_client.list_rows(table_ref).to_dataframe().to_json()
        )
    schema_json = params.get("schema")
    schema = json.loads(schema_json) if schema_json is not None else None
    return _convert_graph_data(query_results=query_results, schema=schema)


class GraphServer:
    """
    Http server invoked by Javascript to obtain the query results for visualization.

    The server is invoked by Javascript, generated as part of
    spanner_graphs.graph_visualization.generate_visualization_html().

    This server is used only in Jupyter; in colab, google.colab.output.register_callback()
    is used instead.
    """

    host = "http://localhost"
    endpoints = {
        "get_ping": "/get_ping",
        "post_ping": "/post_ping",
        "post_node_expansion": "/post_node_expansion",
        "post_query": "/post_query",
    }

    def __init__(self):
        self.port = None
        self.url = None
        self._server = None
        self._server_ready = threading.Event()

    def build_route(self, endpoint):
        """
        Returns a url for connecting to the given endpoint.
        Supported values include:
          - "get_ping": sends a GET request to ping the server.
          - "post_ping": sends a POST request to ping the server.
          - "post_query": sends a POST request to obtain query results.
        """
        return f"{self.url}{endpoint}"

    def _start_server(self):
        class ThreadedTCPServer(socketserver.TCPServer):
            # Allow socket reuse to avoid "Address already in use" errors
            allow_reuse_address = True
            # Daemon threads automatically terminate when the main program exits
            daemon_threads = True

        with ThreadedTCPServer(("127.0.0.1", self.port), GraphServerHandler) as httpd:
            self._server = httpd
            self._server_ready.set()
            self._server.serve_forever()

    def init(self):
        """
        Starts the HTTP server. The server runs forever, until stop_server() is called.
        """
        import portpicker

        self.port = portpicker.pick_unused_port()
        self.url = f"{GraphServer.host}:{self.port}"
        self._server_ready.clear()

        server_thread = threading.Thread(target=self._start_server)
        server_thread.start()
        self._server_ready.wait()
        return server_thread

    def stop_server(self):
        """
        Starts the HTTP server, if it is currently running.
        """
        if self._server:
            self._server.shutdown()
            print("BigQuery-magics graph server shutting down...")
            self._server = None


global graph_server
graph_server = GraphServer()


class GraphServerHandler(http.server.SimpleHTTPRequestHandler):
    """
    Handles HTTP requests send to the graph server.
    """

    def log_message(self, format, *args):
        pass

    def _is_request_safe(self) -> bool:
        """Return True if the request targets and originates from loopback.

        The Host header guards against DNS rebinding: legitimate widget traffic
        always carries a loopback name even though the notebook page and this
        server live on different ports. Origin and Referer, when present, are
        checked too so a page on a non-loopback site cannot drive the server
        with a direct cross-site request; their port differs from ours but the
        hostname is still loopback for real traffic.
        """
        host = self.headers.get("Host")
        if not host:
            return False
        try:
            hostname = urllib.parse.urlsplit(f"//{host.strip()}").hostname
        except ValueError:
            return False
        if hostname not in _LOOPBACK_HOSTS:
            return False

        for header_name in ("Origin", "Referer"):
            value = self.headers.get(header_name)
            if not value:
                continue
            try:
                origin_hostname = urllib.parse.urlsplit(value.strip()).hostname
            except ValueError:
                return False
            if origin_hostname not in _LOOPBACK_HOSTS:
                return False

        return True

    def do_json_response(self, data):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_message_response(self, message):
        self.do_json_response({"message": message})

    def do_data_response(self, data):
        self.do_json_response(data)

    def parse_post_data(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        return json.loads(post_data)

    def handle_get_ping(self):
        self.do_message_response("pong")

    def handle_post_ping(self):
        data = self.parse_post_data()
        self.do_data_response({"your_request": data})

    def handle_post_query(self):
        data = self.parse_post_data()
        params = json.loads(data["params"])

        response = convert_graph_params(params)
        self.do_data_response(response)

    def handle_post_node_expansion(self):
        """Handle POST requests for node expansion.

        Expects a JSON payload with:
        - params: A JSON string containing connection parameters (project, instance, database, graph)
        - request: A dictionary with node details (uid, node_labels, node_properties, direction, edge_label)
        """
        data = self.parse_post_data()

        # Execute node expansion with:
        # - params_str: JSON string with connection parameters (project, instance, database, graph)
        # - request: Dict with node details (uid, node_labels, node_properties, direction, edge_label)
        self.do_data_response(
            execute_node_expansion(
                params=data.get("params"), request=data.get("request")
            )
        )

    def do_GET(self):
        if not self._is_request_safe():
            self.send_error(403, "Forbidden")
            return
        assert self.path == GraphServer.endpoints["get_ping"]
        self.handle_get_ping()

    def do_POST(self):
        if not self._is_request_safe():
            self.send_error(403, "Forbidden")
            return
        if self.path == GraphServer.endpoints["post_ping"]:
            self.handle_post_ping()
        elif self.path == GraphServer.endpoints["post_node_expansion"]:
            self.handle_post_node_expansion()
        else:
            assert self.path == GraphServer.endpoints["post_query"]
            self.handle_post_query()


atexit.register(graph_server.stop_server)
