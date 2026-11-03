# Copyright 2024 Google LLC
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

import json

import numpy as np
import pandas as pd
import pyarrow as pa
import pytest

import db_dtypes
import db_dtypes.json

# Check for minimum Pandas version.
pytest.importorskip("pandas", minversion="1.5.0")


# Python data types mirroring all standard JSON types:
# https://json-schema.org/understanding-json-schema/reference/type
JSON_DATA = {
    "boolean": True,
    "int": 100,
    "float": 0.98,
    "string": "hello world",
    "array": [0.1, 0.2],
    "dict": {
        "null_field": None,
        "order": {
            "items": ["book", "pen", "computer"],
            "total": 15,
            "address": {"street": "123 Main St", "city": "Anytown"},
        },
    },
    "null": None,
}


def test_construct_w_unspported_types():
    with pytest.raises(ValueError):
        db_dtypes.JSONArray(100)


def test_getitems_return_json_objects():
    data = db_dtypes.JSONArray._from_sequence(JSON_DATA.values())
    for id, key in enumerate(JSON_DATA.keys()):
        if key == "null":
            assert pd.isna(data[id])
        else:
            assert data[id] == JSON_DATA[key]


def test_getitems_w_unboxed_dict():
    data = db_dtypes.JSONArray._from_sequence([JSON_DATA["dict"]])
    assert len(data[0]) == 2

    assert data[0]["null_field"] is None
    assert data[0]["order"]["address"]["city"] == "Anytown"
    assert len(data[0]["order"]["items"]) == 3
    assert data[0]["order"]["items"][0] == "book"

    with pytest.raises(KeyError):
        data[0]["unknown"]


def test_getitems_when_iter_with_null():
    data = db_dtypes.JSONArray._from_sequence([JSON_DATA["null"]])
    s = pd.Series(data)
    result = s[:1].item()
    assert pd.isna(result)


def test_deterministic_json_serialization():
    x = {"a": 0, "b": 1}
    y = {"b": 1, "a": 0}
    data = db_dtypes.JSONArray._from_sequence([y])
    assert data[0] == x


def test_to_numpy():
    """
    Verifies that JSONArray can be cast to a NumPy array.
    This test ensures compatibility with Python 3.9 and replicates the behavior
    of the `test_to_numpy` test from `test_json_compliance.py::TestJSONArrayCasting`,
    which is run with Python 3.12 environments only.
    """
    data = db_dtypes.JSONArray._from_sequence(JSON_DATA.values())
    expected = np.asarray(data)

    result = data.to_numpy()
    pd._testing.assert_equal(result, expected)

    result = pd.Series(data).to_numpy()
    pd._testing.assert_equal(result, expected)


def test_as_numpy_array():
    data = db_dtypes.JSONArray._from_sequence(JSON_DATA.values())
    result = np.asarray(data)
    expected = np.asarray(
        [
            json.dumps(value, sort_keys=True, separators=(",", ":"))
            if value is not None
            else pd.NA
            for value in JSON_DATA.values()
        ]
    )
    pd._testing.assert_equal(result, expected)


def test_json_arrow_array():
    data = db_dtypes.JSONArray._from_sequence(JSON_DATA.values())
    assert isinstance(data.__arrow_array__(), pa.ExtensionArray)


def test_json_arrow_storage_type():
    arrow_json_type = db_dtypes.JSONArrowType()
    assert arrow_json_type.extension_name == "dbjson"
    assert pa.types.is_string(arrow_json_type.storage_type)


def test_json_arrow_hash():
    arr = pa.array([], type=db_dtypes.JSONArrowType())
    assert hash(arr.type) == hash(db_dtypes.JSONArrowType())


def test_json_arrow_constructors():
    data = [
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        for value in JSON_DATA.values()
    ]
    storage_array = pa.array(data, type=pa.string())

    arr_1 = db_dtypes.JSONArrowType().wrap_array(storage_array)
    assert isinstance(arr_1, pa.ExtensionArray)

    arr_2 = pa.ExtensionArray.from_storage(db_dtypes.JSONArrowType(), storage_array)
    assert isinstance(arr_2, pa.ExtensionArray)

    assert arr_1 == arr_2


def test_json_arrow_to_pandas():
    data = [
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        for value in JSON_DATA.values()
    ]
    arr = pa.array(data, type=db_dtypes.JSONArrowType())

    s = arr.to_pandas()
    assert isinstance(s.dtypes, db_dtypes.JSONDtype)
    assert s[0]
    assert s[1] == "100"
    assert s[2] == "0.98"
    assert s[3] == '"hello world"'
    assert s[4] == "[0.1,0.2]"
    assert (
        s[5]
        == '{"null_field":null,"order":{"address":{"city":"Anytown","street":"123 Main St"},"items":["book","pen","computer"],"total":15}}'
    )
    assert s[6] == "null"


def test_json_arrow_to_pylist():
    data = [
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        for value in JSON_DATA.values()
    ]
    arr = pa.array(data, type=db_dtypes.JSONArrowType())

    s = arr.to_pylist()
    assert isinstance(s, list)
    assert s[0]
    assert s[1] == "100"
    assert s[2] == "0.98"
    assert s[3] == '"hello world"'
    assert s[4] == "[0.1,0.2]"
    assert (
        s[5]
        == '{"null_field":null,"order":{"address":{"city":"Anytown","street":"123 Main St"},"items":["book","pen","computer"],"total":15}}'
    )
    assert s[6] == "null"


def test_json_arrow_record_batch():
    data = [
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        for value in JSON_DATA.values()
    ]
    arr = pa.array(data, type=db_dtypes.JSONArrowType())
    batch = pa.RecordBatch.from_arrays([arr], ["json_col"])
    sink = pa.BufferOutputStream()

    with pa.RecordBatchStreamWriter(sink, batch.schema) as writer:
        writer.write_batch(batch)

    buf = sink.getvalue()

    with pa.ipc.open_stream(buf) as reader:
        result = reader.read_all()

    json_col = result.column("json_col")
    assert isinstance(json_col.type, db_dtypes.JSONArrowType)

    s = json_col.to_pylist()

    assert isinstance(s, list)
    assert s[0]
    assert s[1] == "100"
    assert s[2] == "0.98"
    assert s[3] == '"hello world"'
    assert s[4] == "[0.1,0.2]"
    assert (
        s[5]
        == '{"null_field":null,"order":{"address":{"city":"Anytown","street":"123 Main St"},"items":["book","pen","computer"],"total":15}}'
    )
    assert s[6] == "null"


def test_from_pyarrow_array():
    arr = db_dtypes.JSONArray._from_sequence([{"a": 1}])

    # Non-string Arrow array returns standard ArrowExtensionArray
    bool_pa = pa.array([True, False])
    res_bool = arr._from_pyarrow_array(bool_pa)
    assert type(res_bool) is pd.arrays.ArrowExtensionArray
    assert res_bool.dtype == "bool[pyarrow]"

    # String Arrow array returns JSONArray
    str_pa = pa.array(['{"b": 2}'])
    res_json = arr._from_pyarrow_array(str_pa)
    assert type(res_json) is db_dtypes.JSONArray
    assert res_json.dtype == db_dtypes.JSONDtype()


def test_cast_pointwise_result():
    arr = db_dtypes.JSONArray._from_sequence([{"a": 1}])

    # Valid JSON sequence casts back to JSONArray
    res = arr._cast_pointwise_result([{"b": 2}])
    assert isinstance(res, db_dtypes.JSONArray)

    # Fallback to super when _from_sequence raises
    import unittest.mock

    with unittest.mock.patch.object(
        db_dtypes.JSONArray,
        "_from_sequence",
        side_effect=TypeError("cannot cast"),
    ):
        fallback = arr._cast_pointwise_result(["val"])
        assert fallback is not None

        # Fallback to numpy array when super() has no _cast_pointwise_result
        with unittest.mock.patch.object(
            pd.arrays.ArrowExtensionArray,
            "_cast_pointwise_result",
            None,
            create=True,
        ):
            fallback_np = arr._cast_pointwise_result(["val"])
            assert isinstance(fallback_np, np.ndarray)
