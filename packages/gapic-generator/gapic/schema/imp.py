# Copyright 2018 Google LLC
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

import dataclasses
from typing import Tuple


@dataclasses.dataclass(frozen=True, order=True)
class Import:
    package: Tuple[str, ...]
    module: str
    alias: str = ""

    def __eq__(self, other) -> bool:
        return self.package == other.package and self.module == other.module

    def __str__(self) -> str:
        # Determine if we need to suppress type checking for this import.
        # We do this for protobuf generated files (_pb2) and api_core
        # internals where type information might be missing or incomplete.
        needs_type_ignore = self.module.endswith("_pb2") or (
            "api_core" in self.package and self.module != "resumable_transfer"
        )
        if needs_type_ignore:
            # Use 'import absolute.path as module' syntax to prevent Ruff/isort
            # from combining this with other imports. This ensures the
            # '# type: ignore' comment remains effective for this specific import.
            full_module = ".".join(self.package + (self.module,))
            alias = self.alias or self.module
            return f"import {full_module} as {alias}  # type: ignore"

        answer = f"import {self.module}"
        if self.package:
            answer = f"from {'.'.join(self.package)} {answer}"
        if self.alias:
            answer += f" as {self.alias}"
        return answer
