# Copyright (C) 2019  Google LLC
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

from enum import Enum, auto
from gapic.utils import to_snake_case


class SampleError(Exception):
    pass


class ReservedVariableName(SampleError):
    pass


class RpcMethodNotFound(SampleError):
    pass


class UnknownService(SampleError):
    pass


class InvalidConfig(SampleError):
    pass


class InvalidStatement(SampleError):
    pass


class BadLoop(SampleError):
    pass


class MismatchedFormatSpecifier(SampleError):
    pass


class UndefinedVariableReference(SampleError):
    pass


class BadAttributeLookup(SampleError):
    pass


class RedefinedVariable(SampleError):
    pass


class BadAssignment(SampleError):
    pass


class InconsistentRequestName(SampleError):
    pass


class InvalidRequestSetup(SampleError):
    pass


class InvalidEnumVariant(SampleError):
    pass


class NonTerminalPrimitiveOrEnum(SampleError):
    pass


class InvalidSampleFpath(SampleError):
    pass


class DuplicateSample(SampleError):
    pass


class ResourceRequestMismatch(SampleError):
    pass


class NoSuchResource(SampleError):
    pass


class NoSuchResourcePattern(SampleError):
    pass


class CallingForm(Enum):
    Request = auto()
    RequestPaged = auto()
    LongRunningRequestAsync = auto()
    RequestStreamingClient = auto()
    RequestStreamingServer = auto()
    RequestStreamingBidi = auto()
    RequestPagedAll = auto()
    LongRunningRequestPromise = auto()

    @classmethod
    def method_default(cls, m):
        if m.lro:
            return cls.LongRunningRequestPromise
        if m.paged_result_field:
            return cls.RequestPagedAll
        if m.client_streaming:
            return (
                cls.RequestStreamingBidi
                if m.server_streaming
                else cls.RequestStreamingClient
            )
        if m.server_streaming:
            return cls.RequestStreamingServer

        return cls.Request
