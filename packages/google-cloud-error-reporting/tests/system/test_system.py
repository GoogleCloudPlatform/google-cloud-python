# Copyright 2017 Google LLC
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

import functools
import operator
import unittest

import mock
from google.protobuf.duration_pb2 import Duration
from test_utils.retry import RetryResult
from test_utils.system import unique_resource_id

import google.cloud.errorreporting_v1beta1
from google.cloud import error_reporting

ERROR_MSG = "Error Reporting System Test"


def setUpModule():
    Config.CLIENT = error_reporting.Client()


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    CLIENT = None


def _list_groups(client):
    """List Error Groups from the last 60 seconds.

    This class provides a wrapper around making calls to the GAX
    API. It's used by the system tests to find the appropriate error group
    to verify the error was successfully reported.

    :type client: :class:`~google.cloud.error_reporting.client.Client`
    :param client: The client containing a project and credentials.

    :rtype: :class:`~google.gax.ResourceIterator`
    :returns: Iterable of :class:`~.google.cloud.errorreporting_v1beta1.ErrorGroupStats`.
    """
    gax_api = google.cloud.errorreporting_v1beta1.ErrorStatsServiceClient(
        credentials=client._credentials
    )
    project_name = f"projects/{client.project}"

    time_range = google.cloud.errorreporting_v1beta1.QueryTimeRange()
    time_range.period = (
        google.cloud.errorreporting_v1beta1.QueryTimeRange.Period.PERIOD_1_HOUR
    )

    duration = Duration(seconds=60 * 60)

    return gax_api.list_group_stats(
        request={
            "project_name": project_name,
            "time_range": time_range,
            "timed_count_duration": duration,
        }
    )


def _simulate_exception(class_name, client):
    """Simulates an exception to verify it was reported.

    :type class_name: str
    :param class_name: The name of a custom error class to
                       create (and raise).

    :type client: :class:`~google.cloud.error_reporting.client.Client`
    :param client: The client that will report the exception.
    """
    custom_exc = type(class_name, (RuntimeError,), {})
    try:
        raise custom_exc(ERROR_MSG)
    except RuntimeError:
        client.report_exception()


def _get_error_count(class_name, client):
    """Counts the number of errors in the group of the test exception.

    :type class_name: str
    :param class_name: The name of a custom error class used.

    :type client: :class:`~google.cloud.error_reporting.client.Client`
    :param client: The client containing a project and credentials.

    :rtype: int
    :returns: Group count for errors that match ``class_name``. If no
              match is found, returns :data:`None`.
    """
    groups = _list_groups(client)
    for group in groups:
        if class_name in group.representative.message:
            return group.count


class TestErrorReporting(unittest.TestCase):
    def test_report_exception(self):
        # Get a class name unique to this test case.
        class_name = "RuntimeError" + unique_resource_id("_")

        # Simulate an error: group won't exist until we report
        # first exception.
        _simulate_exception(class_name, Config.CLIENT)

        is_one = functools.partial(operator.eq, 1)
        is_one.__name__ = "is_one"  # partial() has no name.
        retry = RetryResult(is_one, max_tries=8)
        wrapped_get_count = retry(_get_error_count)

        error_count = wrapped_get_count(class_name, Config.CLIENT)
        self.assertEqual(error_count, 1)

    def test_report_exception_no_grpc(self):
        with mock.patch.dict(
            "os.environ", {"GOOGLE_CLOUD_DISABLE_GRPC": "true"}, clear=True
        ):
            self.test_report_exception()
