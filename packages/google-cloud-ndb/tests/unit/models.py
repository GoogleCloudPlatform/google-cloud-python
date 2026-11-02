# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This file holds ndb models for validating aspects of data loading.
"""

from google.cloud import ndb


class A(ndb.Model):
    some_prop = ndb.IntegerProperty()
    source = ndb.StringProperty()


class B(ndb.Model):
    sub_model = ndb.PickleProperty()
