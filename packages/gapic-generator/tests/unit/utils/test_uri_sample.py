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

from gapic.utils import uri_sample


def test_sample_from_path_template_inner():
    field = "table_name"
    path_template = "{project_id=projects/*}/instances/*/tables/*"
    res = uri_sample.sample_from_path_template(field, path_template)
    assert res == {"table_name": "projects/sample1/instances/sample2/tables/sample3"}


def test_sample_from_path_template_no_inner():
    field = "table_name"
    path_template = "projects/*/instances/*/tables/*"
    res = uri_sample.sample_from_path_template(field, path_template)
    assert res == {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
