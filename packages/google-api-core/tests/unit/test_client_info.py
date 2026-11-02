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


try:
    import grpc
except ImportError:  # pragma: NO COVER
    grpc = None

from google.api_core import client_info


def test_constructor_defaults():
    info = client_info.ClientInfo()

    assert info.python_version is not None

    if grpc is not None:  # pragma: NO COVER
        assert info.grpc_version is not None
    else:  # pragma: NO COVER
        assert info.grpc_version is None

    assert info.api_core_version is not None
    assert info.gapic_version is None
    assert info.client_library_version is None
    assert info.rest_version is None


def test_constructor_options():
    info = client_info.ClientInfo(
        python_version="1",
        grpc_version="2",
        api_core_version="3",
        gapic_version="4",
        client_library_version="5",
        user_agent="6",
        rest_version="7",
        protobuf_runtime_version="8",
    )

    assert info.python_version == "1"
    assert info.grpc_version == "2"
    assert info.api_core_version == "3"
    assert info.gapic_version == "4"
    assert info.client_library_version == "5"
    assert info.user_agent == "6"
    assert info.rest_version == "7"
    assert info.protobuf_runtime_version == "8"


def test_to_user_agent_minimal():
    info = client_info.ClientInfo(
        python_version="1",
        api_core_version="2",
        grpc_version=None,
        protobuf_runtime_version=None,
    )

    user_agent = info.to_user_agent()

    assert user_agent == "gl-python/1 gax/2"


def test_to_user_agent_full():
    info = client_info.ClientInfo(
        python_version="1",
        grpc_version="2",
        api_core_version="3",
        gapic_version="4",
        client_library_version="5",
        user_agent="app-name/1.0",
        protobuf_runtime_version="6",
    )

    user_agent = info.to_user_agent()

    assert user_agent == "app-name/1.0 gl-python/1 grpc/2 gax/3 gapic/4 gccl/5 pb/6"


def test_to_user_agent_rest():
    info = client_info.ClientInfo(
        python_version="1",
        grpc_version=None,
        rest_version="2",
        api_core_version="3",
        gapic_version="4",
        client_library_version="5",
        user_agent="app-name/1.0",
    )

    user_agent = info.to_user_agent()

    assert user_agent == "app-name/1.0 gl-python/1 rest/2 gax/3 gapic/4 gccl/5"
