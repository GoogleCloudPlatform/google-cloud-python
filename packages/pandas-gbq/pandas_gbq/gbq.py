# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import copy
import logging
import re
import typing
import warnings
from datetime import datetime

import pandas

import pandas_gbq.schema
import pandas_gbq.schema.pandas_to_bigquery
from pandas_gbq.contexts import (  # noqa: F401
    Context,  # noqa: F401 - imported solely to support a backwards compatible export
    context,
)
from pandas_gbq.exceptions import (  # noqa: F401 - imported solely to support a backwards compatible export
    DatasetCreationError,
    GenericGBQException,
    InvalidColumnOrder,
    InvalidIndexColumn,
    InvalidPageToken,  # noqa: F401 - imported solely to support a backwards compatible export
    InvalidSchema,  # noqa: F401 - imported solely to support a backwards compatible export
    NotFoundException,
    QueryTimeout,  # noqa: F401 - imported solely to support a backwards compatible export
    TableCreationError,
)
from pandas_gbq.features import FEATURES
from pandas_gbq.gbq_connector import (  # noqa: F401
    GbqConnector,  # noqa: F401 - imported solely to support a backwards compatible export
    _get_client,  # noqa: F401 - imported solely to support a backwards compatible export
)

logger = logging.getLogger(__name__)


def _test_google_api_imports():
    try:
        import packaging  # noqa
    except ImportError as ex:  # pragma: NO COVER
        raise ImportError("pandas-gbq requires db-dtypes") from ex

    try:
        # db-dtypes does not have type hints nor stubs that mypy uses for type checking.
        # This import is solely to test if the package is installed, so we ignore the "unused import" warning.
        # Remove this comment and the ignore pragma upon completing:
        # https://github.com/googleapis/google-cloud-python/issues/17045
        import db_dtypes  # type: ignore[import-untyped] # noqa: F401
    except ImportError as ex:  # pragma: NO COVER
        raise ImportError("pandas-gbq requires db-dtypes") from ex

    try:
        # pydata-google-auth does not have type hints nor stubs that mypy uses for type checking.
        # This import is solely to test if the package is installed, so we ignore the "unused import" warning.
        # Remove this comment and the ignore pragma upon completing:
        # https://github.com/googleapis/google-cloud-python/issues/17045
        import pydata_google_auth  # type: ignore[import-untyped] # noqa: F401
    except ImportError as ex:  # pragma: NO COVER
        raise ImportError("pandas-gbq requires pydata-google-auth") from ex

    try:
        # google-auth-oauthlib does not have type hints nor stubs that mypy uses for type checking.
        # This import is solely to test if the package is installed, so we ignore the "unused import" warning.
        # Remove this comment and the ignore pragma upon completing:
        # https://github.com/googleapis/google-cloud-python/issues/17045
        from google_auth_oauthlib.flow import (  # type: ignore[import-untyped] # noqa: F401
            InstalledAppFlow,
        )
    except ImportError as ex:  # pragma: NO COVER
        raise ImportError("pandas-gbq requires google-auth-oauthlib") from ex

    try:
        import google.auth  # noqa
    except ImportError as ex:  # pragma: NO COVER
        raise ImportError("pandas-gbq requires google-auth") from ex

    try:
        from google.cloud import bigquery  # noqa
    except ImportError as ex:  # pragma: NO COVER
        raise ImportError("pandas-gbq requires google-cloud-bigquery") from ex


def _is_query(query_or_table: str) -> bool:
    return re.search(r"\s", query_or_table.strip(), re.MULTILINE) is not None


def _transform_read_gbq_configuration(configuration):
    """
    For backwards-compatibility, convert any previously client-side only
    parameters such as timeoutMs to the property name expected by the REST API.

    Makes a copy of configuration if changes are needed.
    """

    if configuration is None:
        return None

    timeout_ms = configuration.get("query", {}).get("timeoutMs")
    if timeout_ms is not None:
        # Transform timeoutMs to an actual server-side configuration.
        # https://github.com/googleapis/python-bigquery-pandas/issues/479
        configuration = copy.deepcopy(configuration)
        del configuration["query"]["timeoutMs"]
        configuration["jobTimeoutMs"] = timeout_ms

    return configuration


def read_gbq(
    query_or_table,
    project_id=None,
    index_col=None,
    columns=None,
    reauth=False,
    auth_local_webserver=True,
    dialect=None,
    location=None,
    configuration=None,
    credentials=None,
    use_bqstorage_api=False,
    max_results=None,
    verbose=None,
    private_key=None,
    progress_bar_type="tqdm",
    dtypes=None,
    auth_redirect_uri=None,
    client_id=None,
    client_secret=None,
    *,
    col_order=None,
    bigquery_client=None,
    dry_run: bool = False,
):
    r"""Read data from Google BigQuery to a pandas DataFrame.

    Run a SQL query in BigQuery or read directly from a table
    the `Python client library for BigQuery
    <https://cloud.google.com/python/docs/reference/bigquery/latest/index.html>`__
    and for `BigQuery Storage
    <https://cloud.google.com/python/docs/reference/bigquerystorage/latest>`__
    to make API requests.

    See the :ref:`How to authenticate with Google BigQuery <authentication>`
    guide for authentication instructions.

    .. note::
        Consider using `BigQuery DataFrames
        <https://cloud.google.com/bigquery/docs/dataframes-quickstart>`__ to
        process large results with pandas compatible APIs that run in the
        BigQuery SQL query engine. This provides an opportunity to save on
        costs and improve performance.

    Parameters
    ----------
    query_or_table : str
        SQL query to return data values. If the string is a table ID, fetch the
        rows directly from the table without running a query.
    project_id : str, optional
        Google Cloud Platform project ID. Optional when available from
        the environment.
    index_col : str, optional
        Name of result column to use for index in results DataFrame.
    columns : list(str), optional
        List of BigQuery column names in the desired order for results
        DataFrame.
    reauth : boolean, default False
        Force Google BigQuery to re-authenticate the user. This is useful
        if multiple accounts are used.
    auth_local_webserver : bool, default True
        Use the `local webserver flow
        <https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server>`_
        instead of the `console flow
        <https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console>`_
        when getting user credentials. Your code must run on the same machine
        as your web browser and your web browser can access your application
        via ``localhost:808X``.

        .. versionadded:: 0.2.0
    dialect : str, default 'standard'
        Note: The default value changed to 'standard' in version 0.10.0.

        SQL syntax dialect to use. Value can be one of:

        ``'legacy'``
            Use BigQuery's legacy SQL dialect. For more information see
            `BigQuery Legacy SQL Reference
            <https://cloud.google.com/bigquery/docs/reference/legacy-sql>`__.
        ``'standard'``
            Use BigQuery's standard SQL, which is
            compliant with the SQL 2011 standard. For more information
            see `BigQuery Standard SQL Reference
            <https://cloud.google.com/bigquery/docs/reference/standard-sql/>`__.
    location : str, optional
        Location where the query job should run. See the `BigQuery locations
        documentation
        <https://cloud.google.com/bigquery/docs/dataset-locations>`__ for a
        list of available locations. The location must match that of any
        datasets used in the query.

        .. versionadded:: 0.5.0
    configuration : dict, optional
        Query config parameters for job processing.
        For example:

            configuration = {'query': {'useQueryCache': False}}

        For more information see `BigQuery REST API Reference
        <https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#configuration.query>`__.
    credentials : google.auth.credentials.Credentials, optional
        Credentials for accessing Google APIs. Use this parameter to override
        default credentials, such as to use Compute Engine
        :class:`google.auth.compute_engine.Credentials` or Service Account
        :class:`google.oauth2.service_account.Credentials` directly.

        .. versionadded:: 0.8.0
    use_bqstorage_api : bool, default False
        Use the `BigQuery Storage API
        <https://cloud.google.com/bigquery/docs/reference/storage/>`__ to
        download query results quickly, but at an increased cost. To use this
        API, first `enable it in the Cloud Console
        <https://console.cloud.google.com/apis/library/bigquerystorage.googleapis.com>`__.
        You must also have the `bigquery.readsessions.create
        <https://cloud.google.com/bigquery/docs/access-control#roles>`__
        permission on the project you are billing queries to.

        This feature requires the ``google-cloud-bigquery-storage`` and
        ``pyarrow`` packages.

        This value is ignored if ``max_results`` is set.

        .. versionadded:: 0.10.0
    max_results : int, optional
        If set, limit the maximum number of rows to fetch from the query
        results.

        .. versionadded:: 0.12.0
    progress_bar_type (Optional[str]):
        If set, use the `tqdm <https://tqdm.github.io/>`__ library to
        display a progress bar while the data downloads. Install the
        ``tqdm`` package to use this feature.
        Possible values of ``progress_bar_type`` include:

        ``None``
            No progress bar.
        ``'tqdm'``
            Use the :func:`tqdm.tqdm` function to print a progress bar
            to :data:`sys.stderr`.
        ``'tqdm_notebook'``
            Use the :func:`tqdm.tqdm_notebook` function to display a
            progress bar as a Jupyter notebook widget.
        ``'tqdm_gui'``
            Use the :func:`tqdm.tqdm_gui` function to display a
            progress bar as a graphical dialog box.
    dtypes : dict, optional
        A dictionary of column names to pandas ``dtype``. The provided
        ``dtype`` is used when constructing the series for the column
        specified. Otherwise, a default ``dtype`` is used.
    verbose : None, deprecated
        Deprecated in Pandas-GBQ 0.4.0. Use the `logging module
        to adjust verbosity instead
        <https://pandas-gbq.readthedocs.io/en/latest/intro.html#logging>`__.
    private_key : str, deprecated
        Deprecated in pandas-gbq version 0.8.0. Use the ``credentials``
        parameter and
        :func:`google.oauth2.service_account.Credentials.from_service_account_info`
        or
        :func:`google.oauth2.service_account.Credentials.from_service_account_file`
        instead.
    auth_redirect_uri : str
        Path to the authentication page for organization-specific authentication
        workflows. Used when ``auth_local_webserver=False``.
    client_id : str
        The Client ID for the Google Cloud Project the user is attempting to
        connect to.
    client_secret : str
        The Client Secret associated with the Client ID for the Google Cloud Project
        the user is attempting to connect to.
    col_order : list(str), optional
        Alias for columns, retained for backwards compatibility.
    bigquery_client : google.cloud.bigquery.Client, optional
        A Google Cloud BigQuery Python Client instance. If provided, it will be used for reading
        data, while the project and credentials parameters will be ignored.
    dry_run : bool, default False
        If True, run a dry run query.
    Returns
    -------
    df: DataFrame or Series
        DataFrame representing results of query. If ``dry_run=True``, returns
        a Pandas series that contains job statistics.
    """
    if dialect is None:
        dialect = context.dialect

    if dialect is None:
        dialect = "standard"

    _test_google_api_imports()

    if verbose is not None and FEATURES.pandas_has_deprecated_verbose:
        warnings.warn(
            "verbose is deprecated and will be removed in "
            "a future version. Set logging level in order to vary "
            "verbosity",
            FutureWarning,
            stacklevel=2,
        )

    if dialect not in ("legacy", "standard"):
        raise ValueError("'{0}' is not valid for dialect".format(dialect))

    configuration = _transform_read_gbq_configuration(configuration)

    if configuration and "query" in configuration and "query" in configuration["query"]:
        if query_or_table is not None:
            raise ValueError(
                "Query statement can't be specified "
                "inside config while it is specified "
                "as parameter"
            )
        query_or_table = configuration["query"].pop("query")

    connector = GbqConnector(
        project_id,
        reauth=reauth,
        dialect=dialect,
        auth_local_webserver=auth_local_webserver,
        location=location,
        credentials=credentials,
        private_key=private_key,
        use_bqstorage_api=use_bqstorage_api,
        auth_redirect_uri=auth_redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        bigquery_client=bigquery_client,
    )

    if _is_query(query_or_table):
        final_df = connector.run_query(
            query_or_table,
            configuration=configuration,
            max_results=max_results,
            progress_bar_type=progress_bar_type,
            dtypes=dtypes,
            dry_run=dry_run,
        )
        # When dry_run=True, run_query returns a Pandas series
        if dry_run:
            return final_df
    else:
        final_df = connector.download_table(
            query_or_table,
            max_results=max_results,
            progress_bar_type=progress_bar_type,
            dtypes=dtypes,
        )

    # Reindex the DataFrame on the provided column
    if index_col is not None:
        if index_col in final_df.columns:
            final_df.set_index(index_col, inplace=True)
        else:
            raise InvalidIndexColumn(
                'Index column "{0}" does not exist in DataFrame.'.format(index_col)
            )

    # Using columns as an alias for col_order, raising an error if both provided
    if col_order and not columns:
        columns = col_order
    elif col_order and columns:
        raise ValueError(
            "Must specify either columns (preferred) or col_order, not both"
        )

    # Change the order of columns in the DataFrame based on provided list
    # TODO(kiraksi): allow columns to be a subset of all columns in the table, with follow up PR
    if columns is not None:
        if sorted(columns) == sorted(final_df.columns):
            final_df = final_df[columns]
        else:
            raise InvalidColumnOrder("Column order does not match this DataFrame.")

    connector.log_elapsed_seconds(
        "Total time taken",
        datetime.now().strftime("s.\nFinished at %Y-%m-%d %H:%M:%S."),
    )

    return final_df


def to_gbq(
    dataframe,
    destination_table,
    project_id=None,
    chunksize=None,
    reauth=False,
    if_exists="fail",
    auth_local_webserver=True,
    table_schema=None,
    location=None,
    progress_bar=True,
    credentials=None,
    api_method: str = "default",
    clustering_columns: typing.Union[
        pandas.core.indexes.base.Index, typing.Iterable[typing.Hashable]
    ] = (),
    time_partitioning_column: typing.Optional[str] = None,
    time_partitioning_type: typing.Optional[str] = "DAY",
    time_partitioning_expiration_ms: typing.Optional[int] = None,
    range_partitioning_column: typing.Optional[str] = None,
    range_partitioning_range: typing.Optional[dict] = None,
    verbose=None,
    private_key=None,
    auth_redirect_uri=None,
    client_id=None,
    client_secret=None,
    user_agent=None,
    rfc9110_delimiter=False,
    bigquery_client=None,
):
    """Write a DataFrame to a Google BigQuery table.

    The main method a user calls to export pandas DataFrame contents to Google BigQuery table.

    This method uses the Google Cloud client library to make requests to Google BigQuery, documented `here
    <https://googleapis.dev/python/bigquery/latest/index.html>`__.

    See the :ref:`How to authenticate with Google BigQuery <authentication>`
    guide for authentication instructions.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        DataFrame to be written to a Google BigQuery table.
    destination_table : str
        Name of table to be written, in the form ``dataset.tablename`` or
        ``project.dataset.tablename``.
    clustering_columns: pandas.Index | Iterable[Hashable]
        Specifies the columns for clustering in the BigQuery table.
    time_partitioning_column : str, optional
        Specifies the column for time-based partitioning in the BigQuery table.
    time_partitioning_type : str, default 'DAY'
        Specifies the type of time-based partitioning.
    time_partitioning_expiration_ms : int, optional
        Specifies the milliseconds for time-based partitioning expiration.
    range_partitioning_column : str, optional
        Specifies the column for range-based partitioning in the BigQuery table.
    range_partitioning_range : dict, optional
        Specifies the range for range-based partitioning.
    project_id : str, optional
        Google Cloud Platform project ID. Optional when available from
        the environment.
    chunksize : int, optional
        Number of rows to be inserted in each chunk from the dataframe.
        Set to ``None`` to load the whole dataframe at once.
    reauth : bool, default False
        Force Google BigQuery to re-authenticate the user. This is useful
        if multiple accounts are used.
    if_exists : str, default 'fail'
        Behavior when the destination table exists. Value can be one of:

        ``'fail'``
            If table exists, do nothing.
        ``'replace'``
            If table exists, drop it, recreate it, and insert data.
        ``'append'``
            If table exists, insert data. Create if does not exist.
    auth_local_webserver : bool, default True
        Use the `local webserver flow
        <https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server>`_
        instead of the `console flow
        <https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console>`_
        when getting user credentials. Your code must run on the same machine
        as your web browser and your web browser can access your application
        via ``localhost:808X``.

        .. versionadded:: 0.2.0
    table_schema : list of dicts, optional
        List of BigQuery table fields to which according DataFrame
        columns conform to, e.g. ``[{'name': 'col1', 'type':
        'STRING'},...]``.  The ``type`` values must be BigQuery type names.

        - If ``table_schema`` is provided, it may contain all or a subset of
          DataFrame columns. If a subset is provided, the rest will be
          inferred from the DataFrame dtypes.  If ``table_schema`` contains
          columns not in the DataFrame, they'll be ignored.
        - If ``table_schema`` is **not** provided, it will be
          generated according to dtypes of DataFrame columns. See
          `Inferring the Table Schema
          <https://pandas-gbq.readthedocs.io/en/latest/writing.html#writing-schema>`__.
          for a description of the schema inference.

        See `BigQuery API documentation on valid column names
        <https://cloud.google.com/bigquery/docs/schemas#column_names`>__.

        .. versionadded:: 0.3.1
    location : str, optional
        Location where the load job should run. See the `BigQuery locations
        documentation
        <https://cloud.google.com/bigquery/docs/dataset-locations>`__ for a
        list of available locations. The location must match that of the
        target dataset.

        .. versionadded:: 0.5.0
    progress_bar : bool, default True
        Use the library `tqdm` to show the progress bar for the upload,
        chunk by chunk.

        .. versionadded:: 0.5.0
    credentials : google.auth.credentials.Credentials, optional
        Credentials for accessing Google APIs. Use this parameter to override
        default credentials, such as to use Compute Engine
        :class:`google.auth.compute_engine.Credentials` or Service Account
        :class:`google.oauth2.service_account.Credentials` directly.

        .. versionadded:: 0.8.0
    api_method : str, optional
        API method used to upload DataFrame to BigQuery. One of "load_parquet",
        "load_csv". Default "load_parquet" if pandas is version 1.1.0+,
        otherwise "load_csv".

        .. versionadded:: 0.16.0
    verbose : bool, deprecated
        Deprecated in Pandas-GBQ 0.4.0. Use the `logging module
        to adjust verbosity instead
        <https://pandas-gbq.readthedocs.io/en/latest/intro.html#logging>`__.
    private_key : str, deprecated
        Deprecated in pandas-gbq version 0.8.0. Use the ``credentials``
        parameter and
        :func:`google.oauth2.service_account.Credentials.from_service_account_info`
        or
        :func:`google.oauth2.service_account.Credentials.from_service_account_file`
        instead.
    auth_redirect_uri : str
        Path to the authentication page for organization-specific authentication
        workflows. Used when ``auth_local_webserver=False``.
    client_id : str
        The Client ID for the Google Cloud Project the user is attempting to
        connect to.
    client_secret : str
        The Client Secret associated with the Client ID for the Google Cloud Project
        the user is attempting to connect to.
    user_agent : str
        Custom user agent string used as a prefix to the pandas version.
    rfc9110_delimiter : bool
        Sets user agent delimiter to a hyphen or a slash.
        Default is False, meaning a hyphen will be used.
    bigquery_client : google.cloud.bigquery.Client, optional
        A Google Cloud BigQuery Python Client instance. If provided, it will be used for reading
        data, while the project, user_agent, and credentials parameters will be ignored.

        .. versionadded:: 0.23.3
    """

    # If we get a bigframes.pandas.DataFrame object, it may be possible to use
    # the code paths here, but it could potentially be quite expensive because
    # of the queries involved in type detection. It would be safer just to
    # fail early if there are bigframes-y methods available.
    # https://github.com/googleapis/python-bigquery-pandas/issues/824
    if hasattr(dataframe, "to_pandas") and hasattr(dataframe, "to_gbq"):
        raise TypeError(f"Expected a pandas.DataFrame, but got {repr(type(dataframe))}")

    _test_google_api_imports()

    from google.api_core import exceptions as google_exceptions
    from google.cloud import bigquery

    if verbose is not None and FEATURES.pandas_has_deprecated_verbose:
        warnings.warn(
            "verbose is deprecated and will be removed in "
            "a future version. Set logging level in order to vary "
            "verbosity",
            FutureWarning,
            stacklevel=1,
        )

    if api_method == "default":
        api_method = "load_parquet"

    if chunksize is not None:
        if api_method == "load_parquet":
            warnings.warn(
                "chunksize is ignored when using api_method='load_parquet'",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            warnings.warn(
                "chunksize will be ignored when using api_method='load_csv' in a future version of pandas-gbq",
                PendingDeprecationWarning,
                stacklevel=2,
            )

    if "." not in destination_table:
        raise NotFoundException(
            "Invalid Table Name. Should be of the form 'datasetId.tableId' or "
            "'projectId.datasetId.tableId'"
        )

    if if_exists not in ("fail", "replace", "append"):
        raise ValueError("'{0}' is not valid for if_exists".format(if_exists))

    if_exists_list = ["fail", "replace", "append"]
    dispositions = ["WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"]
    dispositions_dict = dict(zip(if_exists_list, dispositions))

    write_disposition = dispositions_dict[if_exists]

    connector = GbqConnector(
        project_id,
        reauth=reauth,
        auth_local_webserver=auth_local_webserver,
        location=location,
        credentials=credentials,
        private_key=private_key,
        auth_redirect_uri=auth_redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        rfc9110_delimiter=rfc9110_delimiter,
        bigquery_client=bigquery_client,
    )
    bqclient = connector.client

    destination_table_ref = bigquery.table.TableReference.from_string(
        destination_table, default_project=connector.project_id
    )

    project_id_table = destination_table_ref.project
    dataset_id = destination_table_ref.dataset_id
    table_id = destination_table_ref.table_id

    default_schema = _generate_bq_schema(dataframe)
    # If table_schema isn't provided, we'll create one for you
    if not table_schema:
        table_schema = default_schema
    # It table_schema is provided, we'll update the default_schema to the provided table_schema
    else:
        table_schema = pandas_gbq.schema.update_schema(
            default_schema, dict(fields=table_schema)
        )

    try:
        # Try to get the table
        table = bqclient.get_table(destination_table_ref)
    except google_exceptions.NotFound:
        # If the table doesn't already exist, create it
        table_connector = _Table(
            project_id_table,
            dataset_id,
            location=location,
            credentials=connector.credentials,
        )
        table_connector.create(
            table_id,
            table_schema,
            clustering_columns=clustering_columns,
            time_partitioning_column=time_partitioning_column,
            time_partitioning_type=time_partitioning_type,
            time_partitioning_expiration_ms=time_partitioning_expiration_ms,
            range_partitioning_column=range_partitioning_column,
            range_partitioning_range=range_partitioning_range,
        )
    else:
        if if_exists == "append":
            # Convert original schema (the schema that already exists) to pandas-gbq API format
            original_schema = pandas_gbq.schema.to_pandas_gbq(table.schema)

            # Update the local `table_schema` so mode (NULLABLE/REQUIRED)
            # matches. See: https://github.com/pydata/pandas-gbq/issues/315
            table_schema = pandas_gbq.schema.update_schema(
                table_schema, original_schema
            )

    if dataframe.empty:
        # Create the table (if needed), but don't try to run a load job with an
        # empty file. See: https://github.com/pydata/pandas-gbq/issues/237
        return

    connector.load_data(
        dataframe,
        destination_table_ref,
        write_disposition=write_disposition,
        chunksize=chunksize,
        schema=table_schema,
        progress_bar=progress_bar,
        api_method=api_method,
        billing_project=project_id,
    )


def generate_bq_schema(df, default_type="STRING"):
    """DEPRECATED: Given a passed df, generate the associated Google BigQuery
    schema.

    Parameters
    ----------
    df : DataFrame
    default_type : string
        The default big query type in case the type of the column
        does not exist in the schema.
    """
    # deprecation TimeSeries, #11121
    warnings.warn(
        "generate_bq_schema is deprecated and will be removed in a future version",
        FutureWarning,
        stacklevel=2,
    )

    return _generate_bq_schema(df, default_type=default_type)


def _generate_bq_schema(df, default_type="STRING"):
    """DEPRECATED: Given a dataframe, generate a Google BigQuery schema.

    This is a private method, but was used in external code to work around
    issues in the default schema generation. Now that individual columns can
    be overridden: https://github.com/pydata/pandas-gbq/issues/218, this
    method can be removed after there is time to migrate away from this
    method."""
    fields = pandas_gbq.schema.pandas_to_bigquery.dataframe_to_bigquery_fields(
        df,
        default_type=default_type,
    )
    fields_json = []

    for field in fields:
        fields_json.append(field.to_api_repr())

    return {"fields": fields_json}


class _Table(GbqConnector):
    def __init__(
        self,
        project_id,
        dataset_id,
        reauth=False,
        location=None,
        credentials=None,
        private_key=None,
    ):
        self.dataset_id = dataset_id
        super(_Table, self).__init__(
            project_id,
            reauth,
            location=location,
            credentials=credentials,
            private_key=private_key,
        )

    def _table_ref(self, table_id):
        """Return a BigQuery client library table reference"""
        from google.cloud.bigquery import DatasetReference, TableReference

        return TableReference(
            DatasetReference(self.project_id, self.dataset_id), table_id
        )

    def exists(self, table_id):
        """Check if a table exists in Google BigQuery

        Parameters
        ----------
        table : str
            Name of table to be verified

        Returns
        -------
        boolean
            true if table exists, otherwise false
        """
        from google.api_core.exceptions import NotFound

        table_ref = self._table_ref(table_id)
        try:
            self.client.get_table(table_ref)
            return True
        except NotFound:
            return False
        except self.http_error as ex:
            self.process_http_error(ex)

    def create(
        self,
        table_id,
        schema,
        clustering_columns=None,
        time_partitioning_column=None,
        time_partitioning_type="DAY",
        time_partitioning_expiration_ms=None,
        range_partitioning_column=None,
        range_partitioning_range=None,
    ):
        """Create a table in Google BigQuery given a table and schema

        Parameters
        ----------
        table : str
            Name of table to be written
        schema : str
            Use the generate_bq_schema to generate your table schema from a
            dataframe.
        clustering_columns : list, optional
            List of columns to cluster the table on.
        time_partitioning_column : str, optional
            Column to partition the table on.
        time_partitioning_type : str, default 'DAY'
            Type of time partitioning.
        time_partitioning_expiration_ms : int, optional
            Expiration time for the partitioning.
        range_partitioning_column : str, optional
            Column to partition the table on.
        range_partitioning_range : dict, optional
            Range for the partitioning.
        """
        from google.cloud.bigquery import (
            DatasetReference,
            PartitionRange,
            RangePartitioning,
            Table,
            TableReference,
            TimePartitioning,
        )

        if self.exists(table_id):
            raise TableCreationError("Table {0} already exists".format(table_id))

        if not _Dataset(self.project_id, credentials=self.credentials).exists(
            self.dataset_id
        ):
            _Dataset(
                self.project_id,
                credentials=self.credentials,
                location=self.location,
            ).create(self.dataset_id)

        table_ref = TableReference(
            DatasetReference(self.project_id, self.dataset_id), table_id
        )
        table = Table(table_ref)
        table.schema = pandas_gbq.schema.to_google_cloud_bigquery(schema)

        if clustering_columns:
            table.clustering_fields = list(clustering_columns)

        if time_partitioning_column:
            table.time_partitioning = TimePartitioning(
                type_=time_partitioning_type,
                field=time_partitioning_column,
                expiration_ms=time_partitioning_expiration_ms,
            )

        if range_partitioning_column and range_partitioning_range:
            table.range_partitioning = RangePartitioning(
                field=range_partitioning_column,
                range_=PartitionRange(
                    start=range_partitioning_range["start"],
                    end=range_partitioning_range["end"],
                    interval=range_partitioning_range["interval"],
                ),
            )

        try:
            self.client.create_table(table)
        except self.http_error as ex:
            self.process_http_error(ex)

    def delete(self, table_id):
        """Delete a table in Google BigQuery

        Parameters
        ----------
        table : str
            Name of table to be deleted
        """
        from google.api_core.exceptions import NotFound

        table_ref = self._table_ref(table_id)
        try:
            self.client.delete_table(table_ref)
        except NotFound:
            # Ignore 404 error which may occur if table already deleted
            pass
        except self.http_error as ex:
            self.process_http_error(ex)


class _Dataset(GbqConnector):
    def __init__(
        self,
        project_id,
        reauth=False,
        location=None,
        credentials=None,
        private_key=None,
    ):
        super(_Dataset, self).__init__(
            project_id,
            reauth,
            credentials=credentials,
            location=location,
            private_key=private_key,
        )

    def _dataset_ref(self, dataset_id):
        """Return a BigQuery client library dataset reference"""
        from google.cloud.bigquery import DatasetReference

        return DatasetReference(self.project_id, dataset_id)

    def exists(self, dataset_id):
        """Check if a dataset exists in Google BigQuery

        Parameters
        ----------
        dataset_id : str
            Name of dataset to be verified

        Returns
        -------
        boolean
            true if dataset exists, otherwise false
        """
        from google.api_core.exceptions import NotFound

        try:
            self.client.get_dataset(self._dataset_ref(dataset_id))
            return True
        except NotFound:
            return False
        except self.http_error as ex:
            self.process_http_error(ex)

    def create(self, dataset_id):
        """Create a dataset in Google BigQuery

        Parameters
        ----------
        dataset : str
            Name of dataset to be written
        """
        from google.cloud.bigquery import Dataset

        if self.exists(dataset_id):
            raise DatasetCreationError("Dataset {0} already exists".format(dataset_id))

        dataset = Dataset(self._dataset_ref(dataset_id))

        if self.location is not None:
            dataset.location = self.location

        try:
            self.client.create_dataset(dataset)
        except self.http_error as ex:
            self.process_http_error(ex)
