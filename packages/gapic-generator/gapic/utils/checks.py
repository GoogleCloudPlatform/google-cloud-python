# Copyright 2020 Google LLC
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

from google.protobuf.descriptor_pb2 import FieldDescriptorProto


def is_str_field_pb(field_pb: FieldDescriptorProto) -> bool:
    """Determine if field_pb is of type string.

    Args:
        field (Field): The input field as a FieldDescriptorProto
    """
    return field_pb.type == FieldDescriptorProto.TYPE_STRING


def is_msg_field_pb(field_pb: FieldDescriptorProto) -> bool:
    """Determine if field_pb is of type Message.

    Args:
        field (Field): The input field as a FieldDescriptorProto.
    """
    return field_pb.type == FieldDescriptorProto.TYPE_MESSAGE
