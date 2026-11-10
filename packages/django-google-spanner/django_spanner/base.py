# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import logging
import os
import re
from contextlib import contextmanager

import sqlparse
from asgiref.sync import sync_to_async
from django.core.exceptions import ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper
from google.api_core.exceptions import (
    AlreadyExists,
    FailedPrecondition,
    GoogleAPICallError,
    InvalidArgument,
    OutOfRange,
)
from google.cloud import spanner, spanner_dbapi
from google.cloud.spanner_dbapi import parse_utils
from google.cloud.spanner_dbapi.connection import BatchMode
from google.cloud.spanner_dbapi.parsed_statement import StatementType

from ._opentelemetry_tracing import trace_call
from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor
from .utils import quote_ddl_literal
from .version import __version__

logger = logging.getLogger(__name__)

# Global cache for Spanner client to prevent multiple initializations
# which can cause OpenTelemetry 'MeterProvider override' crashes.
_SPANNER_CLIENT_CACHE = None

_BOOL_STRINGS = {"true": True, "false": False}
_DBAPI_CURSOR_RESULT_ATTRS = (
    "_itr",
    "_result_set",
    "_row_count",
    "_batch_dml_rows_count",
)
_RE_BATCH_PREFIX = re.compile(r"^\s*(?:--|/\*|(?:START|RUN|ABORT)\b)", re.IGNORECASE)
_RE_START_BATCH_DDL = re.compile(r"^START\s+BATCH\s+DDL$", re.IGNORECASE)
_RE_RUN_BATCH = re.compile(r"^RUN\s+BATCH$", re.IGNORECASE)
_RE_ABORT_BATCH = re.compile(r"^ABORT\s+BATCH$", re.IGNORECASE)


def _parse_bool_setting(value, setting_name):
    """Validate and coerce a Django Spanner boolean setting value.

    Accepts ``bool`` or case-insensitive ``"true"``/``"false"`` strings matching
    ``RANDOM_ID_GENERATION_ENABLED``, rejecting ambiguous values instead of
    silently treating non-empty strings such as ``"false"`` as truthy.

    :param value: Raw setting value from ``DATABASES[alias]``.
    :type setting_name: str
    :param setting_name: Setting key used in error messages.
    :rtype: bool
    :returns: Parsed boolean setting value.
    :raises django.core.exceptions.ImproperlyConfigured: If ``value`` is not a
        ``bool`` or ``"true"``/``"false"`` string.
    """
    if type(value) is bool:
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in _BOOL_STRINGS:
            return _BOOL_STRINGS[normalized]
    raise ImproperlyConfigured(
        f"Invalid value {value!r} for {setting_name}; expected a bool or "
        "'true'/'false'."
    )


def _format_ddl_sql(sql, args, error_cls):
    """Inline query parameters into a Cloud Spanner DDL SQL string.

    Cloud Spanner ``UpdateDatabaseDdl`` accepts only literal DDL strings without
    bind parameters; parameters passed via ``SchemaEditor`` or ``RunSQL`` are
    quoted as GoogleSQL literals before delegating to ``spanner_dbapi``.

    :type sql: str
    :param sql: Parameterized DDL SQL template using ``%s`` or ``%(name)s``.
    :param args: Non-empty positional sequence or keyword mapping of values.
    :param error_cls: PEP 249 ``ProgrammingError`` class to raise on mismatch.
    :rtype: str
    :returns: DDL statement string with all placeholders replaced by literals.
    :raises ProgrammingError: If ``args`` is neither a sequence nor a mapping,
        or placeholder substitution fails.
    """
    try:
        if isinstance(args, dict):
            quoted = {key: quote_ddl_literal(val) for key, val in args.items()}
        elif isinstance(args, (list, tuple)):
            quoted = tuple(quote_ddl_literal(val) for val in args)
        else:
            raise error_cls("DDL query parameters must be a sequence or mapping.")
        return sql % quoted
    except error_cls:
        raise
    except (KeyError, TypeError, ValueError) as exc:
        raise error_cls(str(exc)) from exc


def _split_and_classify_sql(sql, error_cls):
    """Split a SQL string into ``(statement, parsed)`` tuples.

    External SQL comments and trailing semicolons are stripped so DDL templates
    can be classified cleanly before delegating to ``Cursor._batch_DDLs``, while
    inputs with zero executable tokens raise ``error_cls``.

    :type sql: str
    :param sql: Raw SQL text passed to ``cursor.execute``.
    :param error_cls: PEP 249 ``ProgrammingError`` class to raise on invalid SQL.
    :rtype: list[tuple[str, object]]
    :returns: Non-empty ordered list of ``(statement, parsed)`` tuples.
    :raises ProgrammingError: If no executable statement exists.
    """
    parts = []
    for piece in sqlparse.split(sql):
        stripped = sqlparse.format(piece, strip_comments=True).strip()
        stmt = stripped.rstrip(";").strip()
        if not stmt:
            continue
        parts.append((stmt, parse_utils.classify_statement(stmt)))
    if not parts:
        raise error_cls("Invalid Statement.")
    return parts


def _match_batch_control_sql(sql_str):
    """Classify client-side DDL batch SQL without parsing normal DQL/DML."""
    if _RE_BATCH_PREFIX.match(sql_str) is None:
        return None
    stmts = []
    for piece in sqlparse.split(sql_str):
        stripped = sqlparse.format(piece, strip_comments=True).strip()
        stmt = stripped.rstrip(";").strip()
        if stmt:
            stmts.append(stmt)
            if len(stmts) > 1:
                return None
    if len(stmts) != 1:
        return None
    candidate = stmts[0]
    if _RE_START_BATCH_DDL.match(candidate):
        return "START_DDL"
    if _RE_RUN_BATCH.match(candidate):
        return "RUN"
    if _RE_ABORT_BATCH.match(candidate):
        return "ABORT"
    return None


class _DdlBatchCursor:
    """DB-API cursor proxy coordinating scoped ``spanner_dbapi`` DDL batching.

    Buffers DDL into ``spanner_dbapi.Connection._ddl_statements`` via a scoped
    client transaction (``Connection.begin()``), flushes pending DDL via
    ``Connection.commit()`` immediately before interleaved non-DDL operations in
    ``auto_flush`` mode, intercepts client-side ``START BATCH DDL`` /
    ``RUN BATCH`` / ``ABORT BATCH`` SQL, and maps ``spanner_dbapi`` and gRPC
    errors to ``django.db`` exception classes.
    """

    def __init__(self, db_wrapper, cursor):
        self._db = db_wrapper
        self._cursor = cursor

    def __getattr__(self, attr):
        return getattr(self._cursor, attr)

    def __setattr__(self, attr, value):
        if attr in ("_db", "_cursor"):
            object.__setattr__(self, attr, value)
        else:
            setattr(self._cursor, attr, value)

    def __iter__(self):
        return self

    def __next__(self):
        with self._db._wrap_spanner_errors():
            return next(self._cursor)

    def __enter__(self):
        self._cursor.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self._cursor.__exit__(exc_type, exc_value, traceback)

    def _ensure_open_and_reset(self):
        """Validate open cursor state and clear prior query result attributes."""
        if not getattr(self._cursor, "connection", True):
            raise self._db.Database.ProgrammingError(
                "Cursor is not connected to the database"
            )
        if getattr(self._cursor, "is_closed", False) is True:
            raise self._db.Database.InterfaceError(
                "Cursor and/or connection is already closed."
            )
        if (
            self._db.connection is not None
            and getattr(self._db.connection, "database", False) is None
        ):
            raise ValueError("Database needs to be passed for this operation")
        for attr in _DBAPI_CURSOR_RESULT_ATTRS:
            if hasattr(self._cursor, attr):
                setattr(self._cursor, attr, None)

    def execute(self, sql, args=None):
        """Execute ``sql``, coordinating scoped ``spanner_dbapi`` DDL batching.

        :type sql: str
        :param sql: SQL query, DDL statement(s), or client-side batch command.
        :param args: Optional positional or mapping query parameters.
        :returns: Result of ``spanner_dbapi.Cursor.execute``, or ``None`` for
            buffered DDL and client-side DDL batch statements.
        :raises django.db.DatabaseError: On closed cursors, invalid parameters,
            or rejected batch transitions.
        """
        error_cls = self._db.Database.ProgrammingError
        with self._db._wrap_spanner_errors():
            sql_str = str(sql)
            batch_cmd = _match_batch_control_sql(sql_str)
            if batch_cmd == "START_DDL":
                self._ensure_open_and_reset()
                if args:
                    raise error_cls(
                        "Client-side batch statements do not accept parameters."
                    )
                self._db.start_batch_ddl(auto_flush=False)
                return None
            if batch_cmd in ("RUN", "ABORT") and not self._db._in_dml_batch():
                self._ensure_open_and_reset()
                if args:
                    raise error_cls(
                        "Client-side batch statements do not accept parameters."
                    )
                if batch_cmd == "RUN":
                    return self._db.run_batch()
                return self._db.abort_batch()

            if self._db.in_ddl_batch and not self._db._in_external_tx_or_dml_batch():
                self._ensure_open_and_reset()
                parts = _split_and_classify_sql(sql_str, error_cls)
                if all(p.statement_type == StatementType.DDL for _, p in parts):
                    if args:
                        rendered_sql = _format_ddl_sql(sql_str, args, error_cls)
                        rendered_parts = _split_and_classify_sql(
                            rendered_sql, error_cls
                        )
                        # Re-validate statement count and DDL classification after
                        # literal substitution so parameter values cannot inject new
                        # statements or non-DDL operations.
                        if len(rendered_parts) != len(parts) or any(
                            p.statement_type != StatementType.DDL
                            for _, p in rendered_parts
                        ):
                            raise error_cls(
                                "Only DDL statements are allowed in a DDL batch."
                            )
                        parts = rendered_parts
                    self._db._stage_ddl_statements(
                        self._cursor, [stmt for stmt, _ in parts]
                    )
                    return None

                if not self._db.ddl_batch_auto_flush:
                    raise error_cls("Only DDL statements are allowed in a DDL batch.")

                if len(parts) > 1:
                    if args:
                        raise error_cls(
                            "Parameters are not supported for multi-statement SQL "
                            "in a DDL batch."
                        )
                    for stmt, parsed in parts:
                        if (
                            parsed.statement_type == StatementType.DDL
                            and not self._db._in_external_tx_or_dml_batch()
                        ):
                            self._ensure_open_and_reset()
                            self._db._stage_ddl_statements(self._cursor, [stmt])
                        else:
                            self._db._before_non_ddl_in_batch()
                            self._cursor.execute(stmt)
                    return None

                self._db.flush_ddl_batch()

            if args is None:
                return self._cursor.execute(sql)
            return self._cursor.execute(sql, args)

    def executemany(self, operation, seq_of_params):
        """Delegate ``executemany`` after flushing pending DDL for non-DDL SQL."""
        if self._db.in_ddl_batch and not self._db._in_external_tx_or_dml_batch():
            stmt_type = parse_utils.classify_statement(str(operation)).statement_type
            if stmt_type not in (StatementType.DDL, StatementType.CLIENT_SIDE):
                self._db._before_non_ddl_in_batch()
        with self._db._wrap_spanner_errors():
            return self._cursor.executemany(operation, seq_of_params)

    def callproc(self, procname, args=None):
        """Delegate ``callproc`` after flushing or rejecting pending DDL."""
        self._db._before_non_ddl_in_batch()
        with self._db._wrap_spanner_errors():
            if args is None:
                return self._cursor.callproc(procname)
            return self._cursor.callproc(procname, args)

    def run_sql_in_snapshot(self, sql, params=None, param_types=None):
        """Delegate ``run_sql_in_snapshot`` after flushing pending DDL."""
        self._db._before_non_ddl_in_batch()
        with self._db._wrap_spanner_errors():
            return self._cursor.run_sql_in_snapshot(
                sql, params=params, param_types=param_types
            )

    def list_tables(self, schema_name="", include_views=True):
        """Delegate ``list_tables`` after flushing pending DDL."""
        self._db._before_non_ddl_in_batch()
        with self._db._wrap_spanner_errors():
            return self._cursor.list_tables(
                schema_name=schema_name, include_views=include_views
            )

    def get_table_column_schema(self, table_name, schema_name=""):
        """Delegate ``get_table_column_schema`` after flushing pending DDL."""
        self._db._before_non_ddl_in_batch()
        with self._db._wrap_spanner_errors():
            return self._cursor.get_table_column_schema(
                table_name, schema_name=schema_name
            )


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = "spanner"
    display_name = "Cloud Spanner"

    # Mapping of Field objects to their column types.
    # https://cloud.google.com/spanner/docs/data-types#date-type
    data_types = {
        "AutoField": "INT64",
        "BigAutoField": "INT64",
        "BinaryField": "BYTES(MAX)",
        "BooleanField": "BOOL",
        "CharField": "STRING(%(max_length)s)",
        "DateField": "DATE",
        "DateTimeField": "TIMESTAMP",
        "DecimalField": "NUMERIC",
        "JSONField": "JSON",
        "DurationField": "INT64",
        "EmailField": "STRING(%(max_length)s)",
        "FileField": "STRING(%(max_length)s)",
        "FilePathField": "STRING(%(max_length)s)",
        "FloatField": "FLOAT64",
        "IntegerField": "INT64",
        "BigIntegerField": "INT64",
        "IPAddressField": "STRING(15)",
        "GenericIPAddressField": "STRING(39)",
        "NullBooleanField": "BOOL",
        "OneToOneField": "INT64",
        "PositiveBigIntegerField": "INT64",
        "PositiveIntegerField": "INT64",
        "PositiveSmallIntegerField": "INT64",
        "SlugField": "STRING(%(max_length)s)",
        "SmallAutoField": "INT64",
        "SmallIntegerField": "INT64",
        "TextField": "STRING(MAX)",
        "TimeField": "TIMESTAMP",
        "UUIDField": "STRING(32)",
    }
    operators = {
        "exact": "= %s",
        "iexact": "REGEXP_CONTAINS(%s, %%%%s)",
        # contains uses REGEXP_CONTAINS instead of LIKE to allow
        # DatabaseOperations.prep_for_like_query() to do regular expression
        # escaping. prep_for_like_query() is called for all the lookups that
        # use REGEXP_CONTAINS except regex/iregex (see
        # django.db.models.lookups.PatternLookup).
        "contains": "REGEXP_CONTAINS(%s, %%%%s)",
        "icontains": "REGEXP_CONTAINS(%s, %%%%s)",
        "gt": "> %s",
        "gte": ">= %s",
        "lt": "< %s",
        "lte": "<= %s",
        # Using REGEXP_CONTAINS instead of STARTS_WITH and ENDS_WITH for the
        # same reasoning as described above for 'contains'.
        "startswith": "REGEXP_CONTAINS(%s, %%%%s)",
        "endswith": "REGEXP_CONTAINS(%s, %%%%s)",
        "istartswith": "REGEXP_CONTAINS(%s, %%%%s)",
        "iendswith": "REGEXP_CONTAINS(%s, %%%%s)",
        "regex": "REGEXP_CONTAINS(%s, %%%%s)",
        "iregex": "REGEXP_CONTAINS(%s, %%%%s)",
    }

    # pattern_esc is used to generate SQL pattern lookup clauses when the
    # right-hand side of the lookup isn't a raw string (it might be an
    # expression or the result of a bilateral transformation). In those cases,
    # special characters for REGEXP_CONTAINS operators (e.g. \, *, _) must be
    # escaped on database side.
    pattern_esc = (
        r'REPLACE(REPLACE(REPLACE({}, "\\", "\\\\"), "%%", r"\%%"), "_", r"\_")'
    )

    # These are all no-ops in favor of using REGEXP_CONTAINS in the customized
    # lookups.
    pattern_ops = {
        "contains": "",
        "icontains": "",
        "startswith": "",
        "istartswith": "",
        "endswith": "",
        "iendswith": "",
    }

    data_type_check_constraints = {
        "PositiveBigIntegerField": "%(column)s >= 0",
        "PositiveIntegerField": "%(column)s >= 0",
        "PositiveSmallIntegerField": "%(column)s >= 0",
    }

    Database = spanner_dbapi
    SchemaEditorClass = DatabaseSchemaEditor
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    client_class = DatabaseClient

    def __init__(self, *args, **kwargs):
        """Initialize per-connection Cloud Spanner wrapper and DDL batch state."""
        super().__init__(*args, **kwargs)
        self._ddl_batch_active = False
        self._ddl_batch_auto_flush = False
        self._ddl_batch_flush_count = 0
        self._ddl_tx_begun = False

    @contextmanager
    def _wrap_spanner_errors(self):
        """Translate both gRPC ``GoogleAPICallError`` and PEP 249 errors to Django.

        ``Connection.commit()``, ``Connection.run_prior_DDL_statements()``, and
        ``Cursor.run_sql_in_snapshot()`` raise unmapped ``GoogleAPICallError``
        subclasses directly, whereas Django's ``wrap_database_errors`` only
        catches ``self.Database.Error`` subclasses.
        """
        with self.wrap_database_errors:
            try:
                yield
            except (AlreadyExists, FailedPrecondition, OutOfRange) as exc:
                raise self.Database.IntegrityError(str(exc)) from exc
            except InvalidArgument as exc:
                raise self.Database.ProgrammingError(str(exc)) from exc
            except GoogleAPICallError as exc:
                raise self.Database.OperationalError(str(exc)) from exc

    def _has_open_dbapi_conn(self):
        """Return ``True`` when ``self.connection`` holds an open DB-API connection."""
        return (
            self.connection is not None
            and getattr(self.connection, "is_closed", False) is not True
        )

    def _in_dml_batch(self):
        """Return ``True`` when ``self.connection`` is inside a DB-API DML batch."""
        return (
            self._has_open_dbapi_conn()
            and getattr(self.connection, "_batch_mode", BatchMode.NONE) is BatchMode.DML
        )

    def _in_external_tx_or_dml_batch(self):
        """Return ``True`` during caller transactions or DML batches outside DDL."""
        return self._in_dml_batch() or (
            self._has_open_dbapi_conn()
            and getattr(self.connection, "_client_transaction_started", False) is True
            and not self._ddl_tx_begun
        )

    def _stage_ddl_statements(self, raw_cursor, statements):
        """Buffer validated DDL via ``spanner_dbapi`` client-transaction mode.

        Starts ``self.connection.begin()`` lazily on the first DDL statement of
        a burst so ``Cursor.execute`` appends directly to
        ``self.connection._ddl_statements`` via ``Cursor._batch_DDLs`` without
        opening a Spanner read-write transaction.
        """
        if getattr(self.connection, "read_only", False) is True:
            raise self.Database.ProgrammingError(
                "Cannot execute DDL statements on a read-only connection."
            )
        began_here = not self._ddl_tx_begun
        if began_here:
            self.connection.begin()
            self._ddl_tx_begun = True
        try:
            raw_cursor.execute("; ".join(statements))
        except BaseException:
            if began_here and not getattr(self.connection, "_ddl_statements", None):
                self._rollback_ddl_burst()
            raise

    def _rollback_ddl_burst(self):
        """Clear un-flushed DB-API DDL statements and roll back ``begin()``."""
        was_begun = self._ddl_tx_begun
        self._ddl_tx_begun = False
        if not self._has_open_dbapi_conn():
            return
        # Connection.rollback() resets _transaction_begin_marked without clearing
        # _ddl_statements, so clear the list explicitly before rolling back.
        ddl_list = getattr(self.connection, "_ddl_statements", None)
        if ddl_list:
            ddl_list.clear()
        if (
            was_begun
            and getattr(self.connection, "_client_transaction_started", False) is True
        ):
            self.connection.rollback()

    def _clear_ddl_batch(self):
        """Discard any active DDL burst and reset wrapper DDL batch state."""
        self._rollback_ddl_burst()
        self._ddl_batch_active = False
        self._ddl_batch_auto_flush = False
        self._ddl_batch_flush_count = 0

    def _before_non_ddl_in_batch(self):
        """Flush buffered DDL or raise ``ProgrammingError`` before non-DDL work."""
        if not self.in_ddl_batch or self._in_external_tx_or_dml_batch():
            return
        if not self.ddl_batch_auto_flush:
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Only DDL statements are allowed in a DDL batch."
                )
        self.flush_ddl_batch()

    def _get_project_id(self):
        return os.environ.get("GOOGLE_CLOUD_PROJECT", "test-project")

    @property
    def instance(self):
        """Reference to a Cloud Spanner Instance containing the Database.

        :rtype: :class:`~google.cloud.spanner_v1.instance.Instance`
        :returns: A new instance owned by the existing Spanner Client.
        """
        global _SPANNER_CLIENT_CACHE

        if "client" in self.settings_dict["OPTIONS"]:
            return self.settings_dict["OPTIONS"]["client"].instance(
                self.settings_dict["INSTANCE"]
            )

        if _SPANNER_CLIENT_CACHE is None:
            _SPANNER_CLIENT_CACHE = spanner.Client(project=self._get_project_id())

        return _SPANNER_CLIENT_CACHE.instance(self.settings_dict["INSTANCE"])

    @property
    def allow_transactions_in_auto_commit(self):
        if "ALLOW_TRANSACTIONS_IN_AUTO_COMMIT" in self.settings_dict:
            return self.settings_dict["ALLOW_TRANSACTIONS_IN_AUTO_COMMIT"]
        return True

    @property
    def auto_batch_ddl(self):
        """Whether ``DatabaseSchemaEditor`` automatically batches DDL statements.

        Reads ``DATABASES[alias]["AUTO_BATCH_DDL"]`` first, falling back to
        ``DATABASES[alias]["OPTIONS"]["auto_batch_ddl"]`` and defaulting to
        ``False`` (opt-in automatic schema-editor batching).

        :rtype: bool
        :returns: ``True`` if schema editor contexts auto-batch DDL.
        :raises django.core.exceptions.ImproperlyConfigured: If configured with
            a non-boolean value other than ``"true"``/``"false"``.
        """
        if "AUTO_BATCH_DDL" in self.settings_dict:
            return _parse_bool_setting(
                self.settings_dict["AUTO_BATCH_DDL"], "AUTO_BATCH_DDL"
            )
        options = self.settings_dict.get("OPTIONS") or {}
        if "auto_batch_ddl" in options:
            return _parse_bool_setting(
                options["auto_batch_ddl"], "OPTIONS['auto_batch_ddl']"
            )
        return False

    @property
    def in_ddl_batch(self):
        """Return ``True`` while a DDL batch is open on this connection."""
        return self._ddl_batch_active and (
            self.connection is None or self._has_open_dbapi_conn()
        )

    @property
    def ddl_batch_auto_flush(self):
        """Return ``True`` if the active DDL batch flushes before non-DDL SQL."""
        return self.in_ddl_batch and self._ddl_batch_auto_flush

    @property
    def buffered_ddl_statements(self):
        """Return an immutable snapshot of DDL statements currently buffered."""
        if not self._ddl_tx_begun or not self._has_open_dbapi_conn():
            return ()
        return tuple(getattr(self.connection, "_ddl_statements", ()))

    def _can_auto_batch_ddl(self):
        """Return whether connection state permits starting a SchemaEditor DDL batch.

        Inspects ``settings_dict["AUTOCOMMIT"]`` before ``connect()`` so lazy
        unopened wrappers do not open network sessions on empty schema editors,
        and inspects live transaction/read-only/batch state once connected.
        """
        if not self._has_open_dbapi_conn():
            return bool(self.settings_dict.get("AUTOCOMMIT", True))
        if not self.autocommit:
            return False
        if getattr(self.connection, "_client_transaction_started", False) is True:
            return False
        if getattr(self.connection, "read_only", False) is True:
            return False
        return not self._in_dml_batch()

    def checkpoint_ddl_batch(self):
        """Capture a ``(flush_count, statement_count)`` checkpoint for rollback.

        :rtype: tuple[int, int]
        :returns: Current flush generation and buffered DDL statement count.
        """
        return (self._ddl_batch_flush_count, len(self.buffered_ddl_statements))

    def rollback_ddl_checkpoint(self, checkpoint):
        """Discard un-flushed DDL statements queued after ``checkpoint``.

        :type checkpoint: tuple[int, int]
        :param checkpoint: Snapshot returned by :meth:`checkpoint_ddl_batch`.
        """
        saved_flushes, saved_len = checkpoint
        if (
            self._ddl_tx_begun
            and self._ddl_batch_flush_count == saved_flushes
            and saved_len > 0
        ):
            del self.connection._ddl_statements[saved_len:]
        else:
            self._rollback_ddl_burst()

    def start_batch_ddl(self, *, auto_flush=True):
        """Open a DDL batch backed by scoped ``spanner_dbapi`` transaction mode.

        Remains lazy until the first DDL statement executes so empty schema
        editors and unit tests open zero Spanner sessions or ``UpdateDatabaseDdl``
        calls.

        :type auto_flush: bool
        :param auto_flush: When ``True`` (default for Python callers and
            ``SchemaEditor``), interleaved DQL/DML/transaction boundaries commit
            queued DDL automatically before executing. When ``False`` (used by
            ``START BATCH DDL``), non-DDL operations raise ``ProgrammingError``.
        :raises django.db.utils.ProgrammingError: If a DDL or DML batch is
            already active, if a transaction is active or ``AUTOCOMMIT`` is
            disabled, or if the connection is ``read_only``.
        """
        if self.in_ddl_batch:
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Cannot start a DDL batch when a DDL batch is already active."
                )
        if self.in_atomic_block:
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Cannot start a DDL batch while in a transaction."
                )
        if not self._has_open_dbapi_conn():
            if not self.settings_dict.get("AUTOCOMMIT", True):
                with self.wrap_database_errors:
                    raise self.Database.ProgrammingError(
                        "Cannot start a DDL batch when AUTOCOMMIT is disabled."
                    )
        else:
            if (
                not self.autocommit
                or getattr(self.connection, "_client_transaction_started", False)
                is True
            ):
                with self.wrap_database_errors:
                    raise self.Database.ProgrammingError(
                        "Cannot start a DDL batch while in a transaction."
                    )
            if getattr(self.connection, "read_only", False) is True:
                with self.wrap_database_errors:
                    raise self.Database.ProgrammingError(
                        "Cannot start a DDL batch when the connection is in "
                        "read-only mode."
                    )
            if self._in_dml_batch():
                with self.wrap_database_errors:
                    raise self.Database.ProgrammingError(
                        "Cannot start a DDL batch when a DML batch is active."
                    )
        self._ddl_batch_active = True
        self._ddl_batch_auto_flush = bool(auto_flush)
        self._ddl_batch_flush_count = 0
        self._ddl_tx_begun = False

    def flush_ddl_batch(self):
        """Commit buffered DDL via ``spanner_dbapi.Connection.commit()``.

        ``Connection.commit()`` executes ``run_prior_DDL_statements()``
        (submitting one ``database.update_ddl(ddl_statements)`` RPC) and resets
        ``_client_transaction_started`` without starting a Spanner read-write
        transaction, while leaving :attr:`in_ddl_batch` open for subsequent DDL.

        :returns: ``None``.
        :raises ValueError: If the underlying connection has no ``database``.
        :raises django.db.DatabaseError: On read-only connections or if Spanner
            rejects the DDL batch.
        """
        if not self._has_open_dbapi_conn():
            return None
        if getattr(self.connection, "database", False) is None:
            raise ValueError("Database needs to be passed for this operation")
        if getattr(self.connection, "read_only", False) is True:
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Cannot execute DDL statements on a read-only connection."
                )
        count = len(self.buffered_ddl_statements)
        if not count:
            self._rollback_ddl_burst()
            return None
        try:
            self._ddl_batch_flush_count += 1
            with self._wrap_spanner_errors():
                with trace_call(
                    "CloudSpannerDjango.flush_ddl_batch",
                    self,
                    {"statement_count": count},
                ):
                    self.connection.commit()
                self._ddl_tx_begun = False
                return None
        finally:
            # Connection.commit() calls run_prior_DDL_statements() before its
            # own try/finally reset; roll back on error so _transaction_begin_marked
            # is never stranded on the connection.
            if self._ddl_tx_begun:
                self._rollback_ddl_burst()

    def run_batch(self):
        """Submit the active DML or DDL batch and close batch mode.

        :returns: ``None`` for DDL batches, or the DB-API DML batch result.
        :raises django.db.utils.ProgrammingError: If neither a DDL nor a DML
            batch is active.
        :raises django.db.DatabaseError: If executing the batch fails.
        """
        if self._in_dml_batch():
            with self._wrap_spanner_errors():
                return self.connection.run_batch()
        if not self.in_ddl_batch:
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Cannot run a batch when no DDL or DML batch is active."
                )
        try:
            return self.flush_ddl_batch()
        finally:
            self._clear_ddl_batch()

    def abort_batch(self):
        """Discard the active DML or DDL batch without sending an RPC.

        :returns: ``None`` when aborting a DDL or DML batch.
        :raises django.db.utils.ProgrammingError: If neither a DDL nor a DML
            batch is active.
        """
        if self._in_dml_batch():
            with self._wrap_spanner_errors():
                return self.connection.abort_batch()
        if not self.in_ddl_batch:
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Cannot abort a batch when no DDL or DML batch is active."
                )
        self._clear_ddl_batch()
        return None

    @contextmanager
    def ddl_batch(self, *, auto_flush=True):
        """Group DDL statements across nested schema editors or cursors into one RPC.

        When outermost, opens a DDL batch on entry, calls :meth:`run_batch` on
        clean exit, and aborts on uncaught exceptions. When nested inside an
        already-open DDL batch, records a checkpoint for rollback on error and
        scopes ``auto_flush`` strictness without flushing until outermost exit.

        :type auto_flush: bool
        :param auto_flush: Whether interleaved non-DDL operations flush prior
            DDL automatically (cannot weaken an already-strict outer batch).
        :raises django.db.DatabaseError: On invalid entry state or DDL failure.
        """
        if not self.in_ddl_batch:
            self.start_batch_ddl(auto_flush=auto_flush)
            try:
                yield self
            except BaseException:
                self._clear_ddl_batch()
                raise
            self.run_batch()
            return

        checkpoint = self.checkpoint_ddl_batch()
        prev_auto_flush = self._ddl_batch_auto_flush
        self._ddl_batch_auto_flush = prev_auto_flush and bool(auto_flush)
        try:
            yield self
        except BaseException:
            self.rollback_ddl_checkpoint(checkpoint)
            raise
        finally:
            if self._ddl_batch_active:
                self._ddl_batch_auto_flush = prev_auto_flush

    @property
    def _nodb_connection(self):
        raise NotImplementedError('Spanner does not have a "no db" connection.')

    def get_connection_params(self):
        """Retrieve the connection parameters.

        :rtype: dict
        :returns: A dictionary containing the Spanner connection parameters
                  in Django Spanner format.
        """
        return {
            "project": self._get_project_id(),
            "instance_id": self.settings_dict["INSTANCE"],
            "database_id": self.settings_dict["NAME"],
            "user_agent": f"django_spanner/{__version__}",
            **self.settings_dict["OPTIONS"],
        }

    def get_new_connection(self, conn_params):
        """Create a new connection with corresponding connection parameters.

        :type conn_params: dict
        :param conn_params: Connection parameters for
                            :class:`~google.cloud.spanner_dbapi.connection.Connection`.

        :rtype: :class:`google.cloud.spanner_dbapi.connection.Connection`
        :returns: A new Spanner DB API Connection object associated with the
                  given Google Cloud Spanner resource.

        :raises: :class:`ValueError` in case the given instance/database
                 doesn't exist.
        """
        conn_params.pop("instance", None)
        conn_params.pop("instance_id", None)
        conn_params.pop("client", None)
        conn_params.pop("auto_batch_ddl", None)
        # Ensure client is initialized
        instance = self.instance
        return self.Database.connect(
            instance.instance_id,
            client=instance._client,
            **conn_params,
        )

    def _discard_ddl_batch_on_teardown(self, reason):
        """Warn when dropping un-flushed DDL statements and clear DDL batch state."""
        pending = len(self.buffered_ddl_statements)
        if pending:
            logger.warning(
                "Discarding %d un-flushed Cloud Spanner DDL statement(s) on "
                "connection %s.",
                pending,
                reason,
            )
        self._clear_ddl_batch()

    def init_connection_state(self):
        """Initialize the state of the existing connection.

        Discards buffered statements when resetting an already-used connection,
        while preserving a pre-connect lazy DDL batch unless the newly opened
        DB-API connection is read-only.
        """
        if self.buffered_ddl_statements:
            self._discard_ddl_batch_on_teardown("re-initialization")
        else:
            self._rollback_ddl_burst()
        autocommit = self.connection.autocommit
        self.connection.close()
        database = self.connection.database
        read_only = getattr(self.connection, "read_only", False) is True
        self.connection.__init__(self.instance, database, read_only=read_only)
        self.connection.autocommit = autocommit
        if self._ddl_batch_active and read_only:
            self._clear_ddl_batch()
            with self.wrap_database_errors:
                raise self.Database.ProgrammingError(
                    "Cannot start a DDL batch when the connection is in read-only mode."
                )

    def close(self):
        """Close the connection and unconditionally discard any open DDL batch."""
        try:
            return super().close()
        finally:
            self._discard_ddl_batch_on_teardown("close")

    def _close(self):
        """Abort un-flushed DDL before closing the underlying DB-API connection."""
        self._discard_ddl_batch_on_teardown("close")
        return super()._close()

    def create_cursor(self, name=None):
        """Create a new Database cursor wrapped for DDL batch coordination.

        :type name: str
        :param name: Currently not used.

        :rtype: :class:`_DdlBatchCursor`
        :returns: DDL-batch-aware cursor proxy around ``self.connection.cursor()``.
        """
        return _DdlBatchCursor(self, self.connection.cursor())

    def _set_autocommit(self, autocommit):
        """Set the Spanner transaction autocommit flag on ``self.connection``.

        :type autocommit: bool
        :param autocommit: The new value of the autocommit flag.
        """
        if not autocommit:
            self._before_non_ddl_in_batch()
        with self._wrap_spanner_errors():
            self.connection.autocommit = autocommit

    async def _a_set_autocommit(self, autocommit):
        return await sync_to_async(self._set_autocommit, thread_sensitive=True)(
            autocommit
        )

    def is_usable(self):
        """Check whether the connection is valid.

        :rtype: bool
        :returns: True if the connection is open, otherwise False.
        """
        if self.connection is None or self.connection.is_closed:
            return False

        try:
            # Use a cursor directly, bypassing Django's utilities.
            self.connection.cursor().execute("SELECT 1")
        except self.Database.Error:
            return False

        return True

    def _start_transaction_under_autocommit(self):
        """Start a transaction explicitly in autocommit mode via ``spanner_dbapi``."""
        self._before_non_ddl_in_batch()
        with self._wrap_spanner_errors():
            if self.allow_transactions_in_auto_commit:
                self.connection.cursor().execute("BEGIN")
            else:
                # transactions in autocommit mode for Django 3.2.
                self.connection.cursor().execute("SELECT 1")
