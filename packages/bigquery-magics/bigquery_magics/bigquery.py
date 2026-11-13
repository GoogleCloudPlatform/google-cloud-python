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

"""IPython Magics

.. function:: ``%%bigquery``

    IPython cell magic to run a query and display the result as a DataFrame

    .. code-block:: python

        %%bigquery [<destination_var>] [--project <project>] [--use_legacy_sql]
                   [--verbose] [--params <params>]
        <query>

    Parameters:

    * ``<destination_var>`` (Optional[line argument]):
        variable to store the query results. The results are not displayed if
        this parameter is used. If an error occurs during the query execution,
        the corresponding ``QueryJob`` instance (if available) is stored in
        the variable instead. Set ``bigquery_magics.context.default_variable``
        to set a destination variable without specifying this argument.
    * ``--destination_table`` (Optional[line argument]):
        A dataset and table to store the query results. If table does not exists,
        it will be created. If table already exists, its data will be overwritten.
        Variable should be in a format <dataset_id>.<table_id>.
    * ``--no_query_cache`` (Optional[line argument]):
        Do not use cached query results.
    * ``--project <project>`` (Optional[line argument]):
        Project to use for running the query. Defaults to the context
        :attr:`~google.cloud.bigquery.magics.Context.project`.
    * ``--use_bqstorage_api`` (Optional[line argument]):
        [Deprecated] Not used anymore, as BigQuery Storage API is used by default.
    * ``--use_rest_api`` (Optional[line argument]):
        Use the BigQuery REST API instead of the Storage API.
    * ``--use_legacy_sql`` (Optional[line argument]):
        Runs the query using Legacy SQL syntax. Defaults to Standard SQL if
        this argument not used.
    * ``--verbose`` (Optional[line argument]):
        If this flag is used, information including the query job ID and the
        amount of time for the query to complete will not be cleared after the
        query is finished. By default, this information will be displayed but
        will be cleared after the query is finished.
    * ``--graph`` (Optional[line argument]):
        Visualizes the query result as a graph.
    * ``--use_geodataframe <params>`` (Optional[line argument]):
        Return the query result as a geopandas.GeoDataFrame.
        If present, the argument that follows the ``--use_geodataframe`` flag
        must be a string representing column names to use as the active
        geometry.

        See geopandas.GeoDataFrame for details.
        The Coordinate Reference System will be set to “EPSG:4326”.
    * ``--params <params>`` (Optional[line argument]):
        If present, the argument following the ``--params`` flag must be
        either:

        * :class:`str` - A JSON string representation of a dictionary in the
          format ``{"param_name": "param_value"}`` (ex. ``{"num": 17}``). Use
          of the parameter in the query should be indicated with
          ``@param_name``. See ``In[5]`` in the Examples section below.

        * :class:`dict` reference - A reference to a ``dict`` in the format
          ``{"param_name": "param_value"}``, where the value types must be JSON
          serializable. The variable reference is indicated by a ``$`` before
          the variable name (ex. ``$my_dict_var``). See ``In[6]`` and ``In[7]``
          in the Examples section below.
    * ``--engine <engine>`` (Optional[line argument]):
          [Deprecated] Set the execution engine, either 'pandas' (default) or
          'bigframes'.
          Please use ``%load_ext bigframes`` and the ``%%bqsql`` magic instead.
          See: https://dataframes.bigquery.dev/notebooks/getting_started/magics.html
    * ``--pyformat`` (Optional[line argument]):
          Warning! Do not use with user-provided values.
          This doesn't escape values. Use --params instead for proper SQL escaping.
          This enables Python string formatting in the query text.
          Useful for values not supported by SQL query params such as table IDs.

    * ``<query>`` (required, cell argument):
        SQL query to run. If the query does not contain any whitespace (aside
        from leading and trailing whitespace), it is assumed to represent a
        fully-qualified table ID, and the latter's data will be fetched.

    Returns:
        A :class:`pandas.DataFrame` or :class:`bigframes.pandas.DataFrame`
        with the query results, depending on the ``engine`` chosen or if
        ``--as_geodataframe`` was provided.

    .. note::
        All queries run using this magic will run using the context
        :attr:`~bigquery_magics.config.Context.credentials`.
"""

from __future__ import print_function

import ast
import copy
import json
import re
import sys
import threading
import time
import warnings
from concurrent import futures
from typing import Any, List, Tuple

import IPython  # type: ignore
import pandas
from google.api_core.exceptions import NotFound
from google.cloud import bigquery
from google.cloud.bigquery import exceptions
from google.cloud.bigquery.dataset import DatasetReference
from google.cloud.bigquery.dbapi import _helpers
from google.cloud.bigquery.job import QueryJobConfig
from IPython.core import magic_arguments  # type: ignore
from IPython.core.getipython import get_ipython

import bigquery_magics._versions_helpers
import bigquery_magics.config
import bigquery_magics.graph_server as graph_server
import bigquery_magics.pyformat
from bigquery_magics import core
from bigquery_magics import line_arg_parser as lap

try:
    from google.cloud import bigquery_storage  # type: ignore
except ImportError:
    bigquery_storage = None

try:
    import bigframes.pandas as bpd
except ImportError:
    bpd = None

context = bigquery_magics.config.context


def _handle_error(error, destination_var=None):
    """Process a query execution error.

    Args:
        error (Exception):
            An exception that occurred during the query execution.
        destination_var (Optional[str]):
            The name of the IPython session variable to store the query job.
    """
    if destination_var:
        query_job = getattr(error, "query_job", None)

        if query_job is not None:
            get_ipython().push({destination_var: query_job})
        else:
            # this is the case when previewing table rows by providing just
            # table ID to cell magic
            print(
                "Could not save output to variable '{}'.".format(destination_var),
                file=sys.stderr,
            )

    print("\nERROR:\n", str(error), file=sys.stderr)


def _run_query(client, query, job_config=None):
    """Runs a query while printing status updates

    Args:
        client (google.cloud.bigquery.client.Client):
            Client to bundle configuration needed for API requests.
        query (str):
            SQL query to be executed. Defaults to the standard SQL dialect.
            Use the ``job_config`` parameter to change dialects.
        job_config (Optional[google.cloud.bigquery.job.QueryJobConfig]):
            Extra configuration options for the job.

    Returns:
        google.cloud.bigquery.job.QueryJob: the query job created

    Example:
        >>> client = bigquery.Client()
        >>> _run_query(client, "SELECT 17")
        Executing query with job ID: bf633912-af2c-4780-b568-5d868058632b
        Query executing: 1.66s
        Query complete after 2.07s
        'bf633912-af2c-4780-b568-5d868058632b'
    """
    start_time = time.perf_counter()
    query_job = client.query(query, job_config=job_config)

    if job_config and job_config.dry_run:
        return query_job

    print(f"Executing query with job ID: {query_job.job_id}")

    while True:
        print(
            f"\rQuery executing: {time.perf_counter() - start_time:.2f}s".format(),
            end="",
        )
        try:
            query_job.result(timeout=0.5)
            break
        except futures.TimeoutError:
            continue
    print(f"\nJob ID {query_job.job_id} successfully executed")
    return query_job


def _create_dataset_if_necessary(client, dataset_id):
    """Create a dataset in the current project if it doesn't exist.

    Args:
        client (google.cloud.bigquery.client.Client):
            Client to bundle configuration needed for API requests.
        dataset_id (str):
            Dataset id.
    """
    dataset_reference = DatasetReference(client.project, dataset_id)
    try:
        dataset = client.get_dataset(dataset_reference)
        return
    except NotFound:
        pass
    dataset = bigquery.Dataset(dataset_reference)
    dataset.location = client.location
    print(f"Creating dataset: {dataset_id}")
    dataset = client.create_dataset(dataset)


@magic_arguments.magic_arguments()
@magic_arguments.argument(
    "destination_var",
    nargs="?",
    help=("If provided, save the output to this variable instead of displaying it."),
)
@magic_arguments.argument(
    "--destination_table",
    type=str,
    default=None,
    help=(
        "If provided, save the output of the query to a new BigQuery table. "
        "Variable should be in a format <dataset_id>.<table_id>. "
        "If table does not exists, it will be created. "
        "If table already exists, its data will be overwritten."
    ),
)
@magic_arguments.argument(
    "--project",
    type=str,
    default=None,
    help=("Project to use for executing this query. Defaults to the context project."),
)
@magic_arguments.argument(
    "--max_results",
    default=None,
    help=(
        "Maximum number of rows in dataframe returned from executing the query."
        "Defaults to returning all rows."
    ),
)
@magic_arguments.argument(
    "--maximum_bytes_billed",
    default=None,
    help=(
        "maximum_bytes_billed to use for executing this query. Defaults to "
        "the context default_query_job_config.maximum_bytes_billed."
    ),
)
@magic_arguments.argument(
    "--dry_run",
    action="store_true",
    default=False,
    help=(
        "Sets query to be a dry run to estimate costs. "
        "Defaults to executing the query instead of dry run if this argument is not used."
        "Does not work with engine 'bigframes'. "
    ),
)
@magic_arguments.argument(
    "--use_legacy_sql",
    action="store_true",
    default=False,
    help=(
        "Sets query to use Legacy SQL instead of Standard SQL. Defaults to "
        "Standard SQL if this argument is not used."
    ),
)
@magic_arguments.argument(
    "--bigquery_api_endpoint",
    type=str,
    default=None,
    help=(
        "The desired API endpoint, e.g., bigquery.googlepis.com. Defaults to this "
        "option's value in the context bigquery_client_options."
    ),
)
@magic_arguments.argument(
    "--bqstorage_api_endpoint",
    type=str,
    default=None,
    help=(
        "The desired API endpoint, e.g., bigquerystorage.googlepis.com. Defaults to "
        "this option's value in the context bqstorage_client_options."
    ),
)
@magic_arguments.argument(
    "--no_query_cache",
    action="store_true",
    default=False,
    help=("Do not use cached query results."),
)
@magic_arguments.argument(
    "--use_bqstorage_api",
    action="store_true",
    default=None,
    help=(
        "[Deprecated] The BigQuery Storage API is already used by default to "
        "download large query results, and this option has no effect. "
        "If you want to switch to the classic REST API instead, use the "
        "--use_rest_api option."
    ),
)
@magic_arguments.argument(
    "--use_rest_api",
    action="store_true",
    default=False,
    help=(
        "Use the classic REST API instead of the BigQuery Storage API to "
        "download query results."
    ),
)
@magic_arguments.argument(
    "--verbose",
    action="store_true",
    default=False,
    help=(
        "If set, print verbose output, including the query job ID and the "
        "amount of time for the query to finish. By default, this "
        "information will be displayed as the query runs, but will be "
        "cleared after the query is finished."
        "This flag is ignored when the engine is 'bigframes'."
    ),
)
@magic_arguments.argument(
    "--params",
    nargs="+",
    default=None,
    help=(
        "Parameters to format the query string. If present, the --params "
        "flag should be followed by a string representation of a dictionary "
        "in the format {'param_name': 'param_value'} (ex. {\"num\": 17}), "
        "or a reference to a dictionary in the same format. The dictionary "
        "reference can be made by including a '$' before the variable "
        "name (ex. $my_dict_var)."
    ),
)
@magic_arguments.argument(
    "--use_geodataframe",
    type=str,
    default=None,
    help=(
        "Return the query result as a geopandas.GeoDataFrame.  If present, the "
        "--use_geodataframe flag should be followed by a string name of the "
        "column."
    ),
)
@magic_arguments.argument(
    "--progress_bar_type",
    type=str,
    default=None,
    help=(
        "Sets progress bar type to display a progress bar while executing the query."
        "Defaults to use tqdm_notebook. Install the ``tqdm`` package to use this feature."
    ),
)
@magic_arguments.argument(
    "--location",
    type=str,
    default=None,
    help=(
        "Set the location to execute query."
        "Defaults to location set in query setting in console."
        "This flag is ignored when the engine is 'bigframes'."
    ),
)
@magic_arguments.argument(
    "--engine",
    type=str,
    default=None,
    help=(
        "[Deprecated] Set the execution engine, either 'pandas' or 'bigframes'. "
        "Defaults to engine set in the query setting in console. "
        "Please use %%load_ext bigframes and the %%%%bqsql magic instead. "
        "See: https://dataframes.bigquery.dev/notebooks/getting_started/magics.html"
    ),
)
@magic_arguments.argument(
    "--graph",
    action="store_true",
    default=False,
    help=("Visualizes the query results as a graph"),
)
@magic_arguments.argument(
    "--pyformat",
    action="store_true",
    default=False,
    help=(
        "Warning! Do not use with user-provided values. "
        "This doesn't escape values. Use --params instead for proper SQL escaping. "
        "This enables Python string formatting in the query text. "
        "Useful for values not supported by SQL query params such as table IDs. "
    ),
)
def _cell_magic(line, query):
    """Underlying function for bigquery cell magic

    Note:
        This function contains the underlying logic for the 'bigquery' cell
        magic. This function is not meant to be called directly.

    Args:
        line (str): "%%bigquery" followed by arguments as required
        query (str): SQL query to run

    Returns:
        pandas.DataFrame: the query results.
    """

    params, args = _parse_magic_args(line)

    query = query.strip()
    if not query:
        error = ValueError("Query is missing.")
        _handle_error(error, args.destination_var)
        return
    query = _validate_and_resolve_query(query, args)

    engine = args.engine or context.engine

    if engine == "bigframes":
        return _query_with_bigframes(query, params, args)

    return _query_with_pandas(query, params, args)


def _parse_magic_args(line: str) -> Tuple[List[Any], Any]:
    # The built-in parser does not recognize Python structures such as dicts, thus
    # we extract the "--params" option and interpret it separately.
    try:
        params_option_value, rest_of_args = _split_args_line(line)

    except lap.QueryParamsParseError as exc:
        raise SyntaxError(
            "--params is not a correctly formatted JSON string or a JSON "
            "serializable dictionary"
        ) from exc

    except lap.DuplicateQueryParamsError as exc:
        raise ValueError("Duplicate --params option.") from exc

    except lap.ParseError as exc:
        raise ValueError(
            "Unrecognized input, are option values correct? Error details: {}".format(
                exc.args[0]
            )
        ) from exc

    params = []
    if params_option_value:
        # A non-existing params variable is not expanded and ends up in the input
        # in its raw form, e.g. "$query_params".
        if params_option_value.startswith("$"):
            msg = 'Parameter expansion failed, undefined variable "{}".'.format(
                params_option_value[1:]
            )
            raise NameError(msg)

        params = _helpers.to_query_parameters(ast.literal_eval(params_option_value), {})

    args = magic_arguments.parse_argstring(_cell_magic, rest_of_args)

    if args.engine is not None and args.engine not in ("pandas", "bigframes"):
        raise ValueError(f"Invalid engine: {args.engine}")

    return params, args


def _split_args_line(line: str) -> Tuple[str, str]:
    """Split out the --params option value from the input line arguments.

    Args:
        line: The line arguments passed to the cell magic.

    Returns:
        A tuple of two strings. The first is param option value and
        the second is the rest of the arguments.
    """
    tree = lap.Parser(lap.Lexer(line)).input_line()

    extractor = lap.QueryParamsExtractor()
    params_option_value, rest_of_args = extractor.visit(tree)

    return params_option_value, rest_of_args


def _query_with_bigframes(query: str, params: List[Any], args: Any):
    warnings.warn(
        "The bigframes engine is deprecated. Please use %load_ext bigframes "
        "and the %%bqsql magic instead. "
        "See: https://dataframes.bigquery.dev/notebooks/getting_started/magics.html",
        FutureWarning,
        stacklevel=2,
    )
    if args.dry_run:
        raise ValueError("Dry run is not supported by bigframes engine.")

    if bpd is None:
        raise ValueError("Bigframes package is not installed.")

    bpd.options.bigquery.project = context.project
    bpd.options.bigquery.credentials = context.credentials

    max_results = int(args.max_results) if args.max_results else None

    result = bpd.read_gbq_query(
        query,
        max_results=max_results,
        configuration=_create_job_config(args, params).to_api_repr(),
    )

    return _handle_result(result, args)


def _query_with_pandas(query: str, params: List[Any], args: Any):
    bq_client, bqstorage_client = _create_clients(args)
    try:
        return _make_bq_query(
            query,
            args=args,
            params=params,
            bq_client=bq_client,
            bqstorage_client=bqstorage_client,
        )
    finally:
        _close_transports(bq_client, bqstorage_client)


def _create_clients(args: Any) -> Tuple[bigquery.Client, Any]:
    bq_client = core.create_bq_client(
        project=args.project,
        bigquery_api_endpoint=args.bigquery_api_endpoint,
        location=args.location,
    )

    # Check and instantiate bq storage client
    if args.use_bqstorage_api is not None:
        warnings.warn(
            "Deprecated option --use_bqstorage_api, the BigQuery "
            "Storage API is already used by default.",
            category=DeprecationWarning,
        )
    use_bqstorage_api = not args.use_rest_api and (bigquery_storage is not None)

    if not use_bqstorage_api:
        return bq_client, None

    bqstorage_client_options = copy.deepcopy(context.bqstorage_client_options)
    if args.bqstorage_api_endpoint:
        if isinstance(bqstorage_client_options, dict):
            bqstorage_client_options["api_endpoint"] = args.bqstorage_api_endpoint
        else:
            bqstorage_client_options.api_endpoint = args.bqstorage_api_endpoint

    bqstorage_client = _make_bqstorage_client(
        bq_client,
        bqstorage_client_options,
    )

    return bq_client, bqstorage_client


def _handle_result(result, args):
    """Determine the output of the cell, depending on options set.

    If an explicit destination is set, that takes precedence. Write to that
    variable and skip showing any results.

    Otherwise, if there is a default variable set (such as if this module is
    initialized by bigframes), then set that but also show the output.

    Finally, there is no variable to save to, so just show the output.
    """
    if args.destination_var:
        get_ipython().push({args.destination_var: result})
        return None

    if context.default_variable:
        # If a default variable is set, save the result _and_ show the results.
        get_ipython().push({context.default_variable: result})

    return result


def _colab_query_callback(query: str, params: str):
    return IPython.core.display.JSON(
        graph_server.convert_graph_params(json.loads(params))
    )


def _colab_node_expansion_callback(request: dict, params_str: str):
    """Handle node expansion requests in Google Colab environment

    Args:
        request: A dictionary containing node expansion details including:
            - uid: str - Unique identifier of the node to expand
            - node_labels: List[str] - Labels of the node
            - node_properties: List[Dict] - Properties of the node with key, value, and type
            - direction: str - Direction of expansion ("INCOMING" or "OUTGOING")
            - edge_label: Optional[str] - Label of edges to filter by
        params_str: A JSON string containing connection parameters

    Returns:
        JSON: A JSON-serialized response containing either:
            - The query results with nodes and edges
            - An error message if the request failed
    """
    return IPython.core.display.JSON(
        graph_server.execute_node_expansion(params_str, request)
    )


singleton_server_thread: threading.Thread = None


MAX_GRAPH_VISUALIZATION_SIZE = 2_000_000
MAX_GRAPH_VISUALIZATION_QUERY_RESULT_SIZE = 100_000


def _get_graph_schema(
    bq_client: bigquery.client.Client, query_text: str, query_job: bigquery.job.QueryJob
):
    property_graphs = query_job.referenced_property_graphs
    if len(property_graphs) != 1:
        return None

    graph_ref = property_graphs[0]

    info_schema_query = f"""
        select PROPERTY_GRAPH_METADATA_JSON
        FROM `{graph_ref.project}.{graph_ref.dataset_id}`.INFORMATION_SCHEMA.PROPERTY_GRAPHS
        WHERE PROPERTY_GRAPH_NAME = @graph_id
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(
                "graph_id", "STRING", graph_ref.property_graph_id
            )
        ]
    )
    job_config.use_legacy_sql = False
    try:
        info_schema_results = bq_client.query(
            info_schema_query, job_config=job_config
        ).to_dataframe()
    except Exception:
        # If the INFORMATION_SCHEMA query fails for some reason, disable only schema
        # view, not the entire visualizer.
        return None
    if info_schema_results.shape == (1, 1):
        return graph_server._convert_schema(info_schema_results.iloc[0, 0])
    return None


def _add_graph_widget(
    bq_client: Any,
    query_result: pandas.DataFrame,
    query_text: str,
    query_job: Any,
    args: Any,
):
    try:
        from spanner_graphs.graph_visualization import generate_visualization_html
    except ImportError as err:
        customized_error = ImportError(
            "Use of --graph requires the spanner-graph-notebook package to be installed. Install it with `pip install 'bigquery-magics[spanner-graph-notebook]'`."
        )
        raise customized_error from err

    # In Jupyter, create an http server to be invoked from the Javascript to populate the
    # visualizer widget. In colab, we are not able to create an http server on a
    # background thread, so we use a special colab-specific api to register a callback,
    # to be invoked from Javascript.
    port = None
    try:
        from google.colab import output

        output.register_callback(
            "bigquery.graph_visualization.Query", _colab_query_callback
        )
        output.register_callback(
            "bigquery.graph_visualization.NodeExpansion", _colab_node_expansion_callback
        )

        # In colab mode, the Javascript doesn't use the port value we pass in, as there is no
        # graph server, but it still has to be set to avoid triggering an exception.
        # TODO: Clean this up when the Javascript is fixed on the spanner-graph-notebook side.
        port = 0
    except ImportError:
        # In this code path, we are running on Jupyter, rather than colab.
        global singleton_server_thread
        alive = singleton_server_thread and singleton_server_thread.is_alive()
        if not alive:
            singleton_server_thread = graph_server.graph_server.init()
        port = graph_server.graph_server.port

    # Create html to invoke the graph server
    args_dict = {
        "bigquery_api_endpoint": args.bigquery_api_endpoint,
        "project": args.project,
        "location": args.location,
    }

    estimated_size = query_result.memory_usage(index=True, deep=True).sum()
    if estimated_size > MAX_GRAPH_VISUALIZATION_SIZE:
        IPython.display.display(
            IPython.core.display.HTML(
                "<big><b>Error:</b> The query result is too large for graph visualization.</big>"
            )
        )
        return False

    schema = _get_graph_schema(bq_client, query_text, query_job)

    table_dict = {
        "projectId": query_job.configuration.destination.project,
        "datasetId": query_job.configuration.destination.dataset_id,
        "tableId": query_job.configuration.destination.table_id,
    }

    params_dict = {"destination_table": table_dict, "args": args_dict}
    if estimated_size < MAX_GRAPH_VISUALIZATION_QUERY_RESULT_SIZE:
        params_dict["query_result"] = json.loads(query_result.to_json())

    if schema is not None:
        params_dict["schema"] = schema

    params_str = json.dumps(params_dict)
    html_content = generate_visualization_html(
        query="placeholder query",
        port=port,
        params=params_str.replace("\\", "\\\\").replace('"', '\\"'),
    )
    html_content = html_content.replace(
        '"graph_visualization.Query"', '"bigquery.graph_visualization.Query"'
    )
    html_content = html_content.replace(
        '"graph_visualization.NodeExpansion"',
        '"bigquery.graph_visualization.NodeExpansion"',
    )
    IPython.display.display(IPython.core.display.HTML(html_content))
    return True


def _is_valid_json(s: str):
    try:
        json.loads(s)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def _supports_graph_widget(query_result: pandas.DataFrame):
    # Visualization is supported if we have any json items to display.
    # (Non-json items are excluded from visualization, but we still want to bring up
    #  the visualizer for the json items.)
    for column in query_result.columns:
        if query_result[column].apply(_is_valid_json).any():
            return True
    return False


def _make_bq_query(
    query: str,
    args: Any,
    params: List[Any],
    bq_client: bigquery.Client,
    bqstorage_client: Any,
):
    max_results = int(args.max_results) if args.max_results else None
    geography_column = args.use_geodataframe

    # Any query that does not contain whitespace (aside from leading and trailing whitespace)
    # is assumed to be a table id
    if not re.search(r"\s", query):
        try:
            rows = bq_client.list_rows(query, max_results=max_results)
        except Exception as ex:
            _handle_error(ex, args.destination_var)
            return

        result = rows.to_dataframe(
            bqstorage_client=bqstorage_client,
            create_bqstorage_client=False,
        )
        return _handle_result(result, args)

    job_config = _create_job_config(args, params)
    if args.destination_table:
        split = args.destination_table.split(".")
        if len(split) != 2:
            raise ValueError(
                "--destination_table should be in a <dataset_id>.<table_id> format."
            )
        dataset_id, table_id = split
        job_config.allow_large_results = True
        dataset_ref = DatasetReference(bq_client.project, dataset_id)
        destination_table_ref = dataset_ref.table(table_id)
        job_config.destination = destination_table_ref
        job_config.create_disposition = "CREATE_IF_NEEDED"
        job_config.write_disposition = "WRITE_TRUNCATE"
        _create_dataset_if_necessary(bq_client, dataset_id)

    try:
        query_job = _run_query(bq_client, query, job_config=job_config)
    except Exception as ex:
        _handle_error(ex, args.destination_var)
        return

    if not args.verbose:
        IPython.display.clear_output()

    if args.dry_run:
        # TODO(tswast): Use _handle_result() here, too, but perhaps change the
        # format to match the dry run schema from bigframes and pandas-gbq.
        # See: https://github.com/googleapis/python-bigquery-pandas/issues/585
        if args.destination_var:
            get_ipython().push({args.destination_var: query_job})
            return
        else:
            print(
                "Query validated. This query will process {} bytes.".format(
                    query_job.total_bytes_processed
                )
            )
            return query_job

    progress_bar = context.progress_bar_type or args.progress_bar_type
    dataframe_kwargs = {
        "bqstorage_client": bqstorage_client,
        "create_bqstorage_client": False,
        "progress_bar_type": progress_bar,
    }
    if max_results:
        dataframe_kwargs["bqstorage_client"] = None

    result = query_job
    if max_results:
        result = result.result(max_results=max_results)

    if geography_column:
        result = result.to_geodataframe(
            geography_column=geography_column, **dataframe_kwargs
        )
    else:
        result = result.to_dataframe(**dataframe_kwargs)

    if args.graph and _supports_graph_widget(result):
        if _add_graph_widget(bq_client, result, query, query_job, args):
            # Invoke _handle_result() in case the result is saved to a variable,
            # but return None to suppress the default table view, which is redundant
            # with the table view in the graph visualizer.
            _handle_result(result, args)
            return None
    return _handle_result(result, args)


def _validate_and_resolve_query(query: str, args: Any) -> str:
    # Check if query is given as a reference to a variable.
    if query.startswith("$"):
        query_var_name = query[1:]

        if not query_var_name:
            missing_msg = 'Missing query variable name, empty "$" is not allowed.'
            raise NameError(missing_msg)

        if query_var_name.isidentifier():
            ip = get_ipython()
            query = ip.user_ns.get(query_var_name, ip)  # ip serves as a sentinel

            if query is ip:
                raise NameError(
                    f"Unknown query, variable {query_var_name} does not exist."
                )
            elif not isinstance(query, (str, bytes)):
                raise TypeError(
                    f"Query variable {query_var_name} must be a string "
                    "or a bytes-like value."
                )

    if args.pyformat:
        ip = get_ipython()
        query = bigquery_magics.pyformat.pyformat(query, ip.user_ns)
    return query


def _create_job_config(args: Any, params: List[Any]) -> QueryJobConfig:
    job_config = QueryJobConfig()
    job_config.query_parameters = params
    job_config.use_legacy_sql = args.use_legacy_sql
    job_config.dry_run = args.dry_run

    # Don't override context job config unless --no_query_cache is explicitly set.
    if args.no_query_cache:
        job_config.use_query_cache = False

    if args.maximum_bytes_billed == "None":
        job_config.maximum_bytes_billed = 0
    elif args.maximum_bytes_billed is not None:
        value = int(args.maximum_bytes_billed)
        job_config.maximum_bytes_billed = value

    return job_config


def _make_bqstorage_client(client, client_options):
    """Creates a BigQuery Storage client.

    Args:
        client (:class:`~google.cloud.bigquery.client.Client`): BigQuery client.
        client_options (:class:`google.api_core.client_options.ClientOptions`):
            Custom options used with a new BigQuery Storage client instance
            if one is created.

    Raises:
        ImportError: if google-cloud-bigquery-storage is not installed, or
            grpcio package is not installed.


    Returns:
        None: if ``use_bqstorage_api == False``, or google-cloud-bigquery-storage
            is outdated.
        BigQuery Storage Client:
    """
    try:
        bigquery_magics._versions_helpers.BQ_STORAGE_VERSIONS.try_import(
            raise_if_error=True
        )
    except exceptions.BigQueryStorageNotFoundError as err:
        customized_error = ImportError(
            "The default BigQuery Storage API client cannot be used, install "
            "the missing google-cloud-bigquery-storage and pyarrow packages "
            "to use it. Alternatively, use the classic REST API by specifying "
            "the --use_rest_api magic option."
        )
        raise customized_error from err

    try:
        from google.api_core.gapic_v1 import client_info as gapic_client_info
    except ImportError as err:
        customized_error = ImportError(
            "Install the grpcio package to use the BigQuery Storage API."
        )
        raise customized_error from err

    return client._ensure_bqstorage_client(
        client_options=client_options,
        client_info=gapic_client_info.ClientInfo(user_agent=core._get_user_agent()),
    )


def _close_transports(client, bqstorage_client):
    """Close the given clients' underlying transport channels.

    Closing the transport is needed to release system resources, namely open
    sockets.

    Args:
        client (:class:`~google.cloud.bigquery.client.Client`):
        bqstorage_client
            (Optional[:class:`~google.cloud.bigquery_storage.BigQueryReadClient`]):
            A client for the BigQuery Storage API.

    """
    client.close()
    if bqstorage_client is not None:
        bqstorage_client._transport.grpc_channel.close()
