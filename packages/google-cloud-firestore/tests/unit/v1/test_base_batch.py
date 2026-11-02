# Copyright 2017 Google LLC All rights reserved.
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


def _make_derived_write_batch(*args, **kwargs):
    from google.cloud.firestore_v1.base_batch import BaseWriteBatch

    class DerivedBaseWriteBatch(BaseWriteBatch):
        def __init__(self, client):
            super().__init__(client=client)

        """Create a fake subclass of `BaseWriteBatch` for the purposes of
        evaluating the shared methods."""

        def commit(self):
            pass  # pragma: NO COVER

    return DerivedBaseWriteBatch(*args, **kwargs)


def test_basewritebatch_constructor():
    batch = _make_derived_write_batch(mock.sentinel.client)
    assert batch._client is mock.sentinel.client
    assert batch._write_pbs == []
    assert batch.write_results is None
    assert batch.commit_time is None


def test_basewritebatch__add_write_pbs():
    batch = _make_derived_write_batch(mock.sentinel.client)
    assert batch._write_pbs == []
    batch._add_write_pbs([mock.sentinel.write1, mock.sentinel.write2])
    assert batch._write_pbs == [mock.sentinel.write1, mock.sentinel.write2]


def test_basewritebatch_create():
    from google.cloud.firestore_v1.types import common, document, write

    client = _make_client()
    batch = _make_derived_write_batch(client)
    assert batch._write_pbs == []

    reference = client.document("this", "one")
    document_data = {"a": 10, "b": 2.5}
    ret_val = batch.create(reference, document_data)
    assert ret_val is None
    new_write_pb = write.Write(
        update=document.Document(
            name=reference._document_path,
            fields={
                "a": _value_pb(integer_value=document_data["a"]),
                "b": _value_pb(double_value=document_data["b"]),
            },
        ),
        current_document=common.Precondition(exists=False),
    )
    assert batch._write_pbs == [new_write_pb]


def test_basewritebatch_set():
    from google.cloud.firestore_v1.types import document, write

    client = _make_client()
    batch = _make_derived_write_batch(client)
    assert batch._write_pbs == []

    reference = client.document("another", "one")
    field = "zapzap"
    value = "meadows and flowers"
    document_data = {field: value}
    ret_val = batch.set(reference, document_data)
    assert ret_val is None
    new_write_pb = write.Write(
        update=document.Document(
            name=reference._document_path,
            fields={field: _value_pb(string_value=value)},
        )
    )
    assert batch._write_pbs == [new_write_pb]


def test_basewritebatch_set_merge():
    from google.cloud.firestore_v1.types import document, write

    client = _make_client()
    batch = _make_derived_write_batch(client)
    assert batch._write_pbs == []

    reference = client.document("another", "one")
    field = "zapzap"
    value = "meadows and flowers"
    document_data = {field: value}
    ret_val = batch.set(reference, document_data, merge=True)
    assert ret_val is None
    new_write_pb = write.Write(
        update=document.Document(
            name=reference._document_path,
            fields={field: _value_pb(string_value=value)},
        ),
        update_mask={"field_paths": [field]},
    )
    assert batch._write_pbs == [new_write_pb]


def test_basewritebatch_update():
    from google.cloud.firestore_v1.types import common, document, write

    client = _make_client()
    batch = _make_derived_write_batch(client)
    assert batch._write_pbs == []

    reference = client.document("cats", "cradle")
    field_path = "head.foot"
    value = "knees toes shoulders"
    field_updates = {field_path: value}

    ret_val = batch.update(reference, field_updates)
    assert ret_val is None

    map_pb = document.MapValue(fields={"foot": _value_pb(string_value=value)})
    new_write_pb = write.Write(
        update=document.Document(
            name=reference._document_path,
            fields={"head": _value_pb(map_value=map_pb)},
        ),
        update_mask=common.DocumentMask(field_paths=[field_path]),
        current_document=common.Precondition(exists=True),
    )
    assert batch._write_pbs == [new_write_pb]


def test_basewritebatch_delete():
    from google.cloud.firestore_v1.types import write

    client = _make_client()
    batch = _make_derived_write_batch(client)
    assert batch._write_pbs == []

    reference = client.document("early", "mornin", "dawn", "now")
    ret_val = batch.delete(reference)
    assert ret_val is None
    new_write_pb = write.Write(delete=reference._document_path)
    assert batch._write_pbs == [new_write_pb]


def _value_pb(**kwargs):
    from google.cloud.firestore_v1.types.document import Value

    return Value(**kwargs)


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(project="seventy-nine"):
    from google.cloud.firestore_v1.client import Client

    credentials = _make_credentials()
    return Client(project=project, credentials=credentials)
