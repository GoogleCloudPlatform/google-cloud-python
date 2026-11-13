# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import os

from asgiref.sync import sync_to_async
from django.db.backends.base.base import BaseDatabaseWrapper
from google.cloud import spanner, spanner_dbapi

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor
from .version import __version__

# Global cache for Spanner client to prevent multiple initializations
# which can cause OpenTelemetry 'MeterProvider override' crashes.
_SPANNER_CLIENT_CACHE = None


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

        :type conn_params: list
        :param conn_params: A List of the connection parameters for
                            :class:`~google.cloud.spanner_dbapi.connection.Connection`

        :rtype: :class:`google.cloud.spanner_dbapi.connection.Connection`
        :returns: A new Spanner DB API Connection object associated with the
                  given Google Cloud Spanner resource.

        :raises: :class:`ValueError` in case the given instance/database
                 doesn't exist.
        """
        conn_params.pop("instance", None)
        conn_params.pop("instance_id", None)
        conn_params.pop("client", None)
        # Ensure client is initialized
        instance = self.instance
        return self.Database.connect(
            instance.instance_id,
            client=instance._client,
            **conn_params,
        )

    def init_connection_state(self):
        """Initialize the state of the existing connection."""
        autocommit = self.connection.autocommit
        self.connection.close()
        database = self.connection.database
        self.connection.__init__(self.instance, database)
        self.connection.autocommit = autocommit

    def create_cursor(self, name=None):
        """Create a new Database cursor.

        :type name: str
        :param name: Currently not used.

        :rtype: :class:`~google.cloud.spanner_dbapi.cursor.Cursor`
        :returns: The Cursor for this connection.
        """
        return self.connection.cursor()

    def _set_autocommit(self, autocommit):
        """Set the Spanner transaction autocommit flag.

        :type autocommit: bool
        :param autocommit: The new value of the autocommit flag.
        """
        with self.wrap_database_errors:
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
        """
        Start a transaction explicitly in autocommit mode.
        """
        if self.allow_transactions_in_auto_commit:
            self.connection.cursor().execute("BEGIN")
        else:
            # transactions in autocommit mode for Django 3.2.
            self.connection.cursor().execute("SELECT 1")
