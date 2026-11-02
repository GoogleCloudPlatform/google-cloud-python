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

import mock
import pytest

from google.cloud.datastore.client import _HAVE_GRPC


@pytest.mark.skipif(not _HAVE_GRPC, reason="No gRPC")
@mock.patch(
    "google.cloud.datastore_v1.services.datastore.client.DatastoreClient",
    return_value=mock.sentinel.ds_client,
)
@mock.patch(
    "google.cloud.datastore_v1.services.datastore.transports.grpc.DatastoreGrpcTransport",
    return_value=mock.sentinel.transport,
)
@mock.patch(
    "google.cloud.datastore._gapic.make_secure_channel",
    return_value=mock.sentinel.channel,
)
def test_live_api(make_chan, mock_transport, mock_klass):
    from google.cloud._http import DEFAULT_USER_AGENT

    from google.cloud.datastore._gapic import make_datastore_api

    base_url = "https://datastore.googleapis.com:443"
    client = mock.Mock(
        _base_url=base_url,
        _credentials=mock.sentinel.credentials,
        _client_info=mock.sentinel.client_info,
        spec=["_base_url", "_credentials", "_client_info"],
    )
    ds_api = make_datastore_api(client)
    assert ds_api is mock.sentinel.ds_client

    mock_transport.assert_called_once_with(channel=mock.sentinel.channel)

    make_chan.assert_called_once_with(
        mock.sentinel.credentials,
        DEFAULT_USER_AGENT,
        "datastore.googleapis.com:443",
    )

    mock_klass.assert_called_once_with(
        transport=mock.sentinel.transport, client_info=mock.sentinel.client_info
    )


@pytest.mark.skipif(not _HAVE_GRPC, reason="No gRPC")
@mock.patch(
    "google.cloud.datastore_v1.services.datastore.client.DatastoreClient",
    return_value=mock.sentinel.ds_client,
)
@mock.patch(
    "google.cloud.datastore_v1.services.datastore.transports.grpc.DatastoreGrpcTransport",
    return_value=mock.sentinel.transport,
)
@mock.patch(
    "google.cloud.datastore._gapic.insecure_channel",
    return_value=mock.sentinel.channel,
)
def test_emulator(make_chan, mock_transport, mock_klass):
    from google.cloud.datastore._gapic import make_datastore_api

    host = "localhost:8901"
    base_url = "http://" + host
    client = mock.Mock(
        _base_url=base_url,
        _credentials=mock.sentinel.credentials,
        _client_info=mock.sentinel.client_info,
        spec=["_base_url", "_credentials", "_client_info"],
    )
    ds_api = make_datastore_api(client)
    assert ds_api is mock.sentinel.ds_client

    mock_transport.assert_called_once_with(channel=mock.sentinel.channel)

    make_chan.assert_called_once_with(host)

    mock_klass.assert_called_once_with(
        transport=mock.sentinel.transport, client_info=mock.sentinel.client_info
    )


def test_version_from_gapic_version_matches_datastore_version():
    from google.cloud.datastore import gapic_version
    from google.cloud.datastore_admin import gapic_version as gapic_version_admin
    from google.cloud.datastore_admin_v1 import gapic_version as gapic_version_admin_v1
    from google.cloud.datastore_v1 import gapic_version as gapic_version_v1

    assert gapic_version.__version__ == gapic_version_admin.__version__
    assert gapic_version.__version__ == gapic_version_v1.__version__
    assert gapic_version.__version__ == gapic_version_admin_v1.__version__
