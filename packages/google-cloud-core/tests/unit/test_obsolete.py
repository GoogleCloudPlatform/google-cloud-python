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

from unittest import mock
import warnings

from google.cloud import obsolete


def test_complain_noop():
    with mock.patch.object(warnings, "warn", autospec=True) as warn:
        obsolete.complain("bogus_package")
        assert warn.call_count == 0


def test_complain():
    with mock.patch.object(warnings, "warn", autospec=True) as warn:
        obsolete.complain("google-cloud-core")
        warn.assert_called_once_with(mock.ANY, DeprecationWarning)
