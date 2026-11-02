# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.backends.base.client import BaseDatabaseClient
from google.cloud.spanner_dbapi.exceptions import NotSupportedError


class DatabaseClient(BaseDatabaseClient):
    """Wrap the Django base class."""

    def runshell(self, parameters):
        raise NotSupportedError("This method is not supported.")
