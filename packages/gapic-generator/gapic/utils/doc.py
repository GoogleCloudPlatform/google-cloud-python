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

from google.protobuf import descriptor_pb2


def doc(text: str) -> descriptor_pb2.SourceCodeInfo.Location:
    """Return a Location object with the given documentation.

    This convenience method instantates a protobuf location object,
    which is expected by the Metadata class, and allows for classes
    not based on protobuf locations to easily conform to the interface.
    """
    return descriptor_pb2.SourceCodeInfo.Location(leading_comments=text)
