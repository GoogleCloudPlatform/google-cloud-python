# -*- coding: utf-8 -*-
# Copyright 2021 Google LLC
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
#

from google.cloud import appengine_logging_v1

# NOTE: These are dummy tests to reach 100% coverage
# They simply check that each message can be created.


def test_log_line():
    appengine_logging_v1.LogLine()


def test_source_location():
    appengine_logging_v1.SourceLocation()


def test_source_reference():
    appengine_logging_v1.SourceReference()


def test_request_log():
    appengine_logging_v1.RequestLog()
