# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import os
import sys
from unittest import skip

from django.conf import settings
from django.db.backends.base.creation import BaseDatabaseCreation
from django.utils.module_loading import import_string


class DatabaseCreation(BaseDatabaseCreation):
    """
    Spanner-specific wrapper for Django class encapsulating methods for
    creation and destruction of the underlying test database.
    """

    def mark_skips(self):
        """Skip tests that don't work on Spanner."""
        for test_name in self.connection.features.skip_tests:
            test_case_name, _, method_name = test_name.rpartition(".")
            test_app = test_name.split(".")[0]
            # Importing a test app that isn't installed raises RuntimeError.
            if test_app in settings.INSTALLED_APPS:
                test_case = import_string(test_case_name)
                try:
                    method = getattr(test_case, method_name)
                    setattr(
                        test_case,
                        method_name,
                        skip("unsupported by Spanner")(method),
                    )
                except AttributeError:
                    # The test method might not exist in this version of Django.
                    pass

    def create_test_db(self, *args, **kwargs):
        """Create a test database.

        :rtype: str
        :returns: The name of the newly created test Database.
        """
        # This environment variable is set by the Travis build script or
        # by a developer running the tests locally.
        if os.environ.get("RUNNING_SPANNER_BACKEND_TESTS") == "1":
            self.mark_skips()
        super().create_test_db(*args, **kwargs)

    def _create_test_db(self, verbosity, autoclobber, keepdb=False):
        """
        Create dummy test tables. This method is mostly copied from the
        base class but removes usage of `_nodb_connection` since Spanner doesn't
        have or need one.
        """
        # Mostly copied from the base class but removes usage of
        # _nodb_connection since Spanner doesn't have or need one.
        test_database_name = self._get_test_db_name()
        # Don't quote the test database name because google.cloud.spanner_v1
        # does it.
        test_db_params = {"dbname": test_database_name}
        # Create the test database.
        try:
            self._execute_create_test_db(None, test_db_params, keepdb)
        except Exception as e:
            # If the db should be kept, then no need to do any of the below,
            # just return and skip it all.
            if keepdb:
                return test_database_name
            self.log("Got an error creating the test database: %s" % e)
            if not autoclobber:
                confirm = input(
                    "Type 'yes' if you would like to try deleting the test "
                    "database '%s', or 'no' to cancel: " % test_database_name
                )
            if autoclobber or confirm == "yes":
                try:
                    if verbosity >= 1:
                        self.log(
                            "Destroying old test database for alias %s..."
                            % (
                                self._get_database_display_str(
                                    verbosity, test_database_name
                                ),
                            )
                        )
                    self._destroy_test_db(test_database_name, verbosity)
                    self._execute_create_test_db(None, test_db_params, keepdb)
                except Exception as e:
                    self.log("Got an error recreating the test database: %s" % e)
                    sys.exit(2)
            else:
                self.log("Tests cancelled.")
                sys.exit(1)
        return test_database_name

    def _execute_create_test_db(self, cursor, parameters, keepdb=False):
        self.connection.instance.database(parameters["dbname"]).create()

    def _destroy_test_db(self, test_database_name, verbosity):
        self.connection.instance.database(test_database_name).drop()
