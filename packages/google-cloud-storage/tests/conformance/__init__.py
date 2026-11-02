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

import io
import json
import os


def _read_local_json(json_file):
    here = os.path.dirname(__file__)
    json_path = os.path.abspath(os.path.join(here, json_file))
    with io.open(json_path, "r", encoding="utf-8-sig") as fileobj:
        return json.load(fileobj)
