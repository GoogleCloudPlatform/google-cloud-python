# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from google.cloud.spanner_dbapi.exceptions import NotSupportedError

from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestClient(SpannerSimpleTestClass):
    def test_runshell(self):
        with self.assertRaises(NotSupportedError):
            self.db_client.runshell(parameters=self.settings_dict)
