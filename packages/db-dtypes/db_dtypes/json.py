# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import json

import numpy as np
import pandas as pd
import pandas.arrays as arrays
import pandas.core.dtypes.common as common
import pandas.core.indexers as indexers
import pyarrow as pa
import pyarrow.compute


@pd.api.extensions.register_extension_dtype
class JSONDtype(pd.api.extensions.ExtensionDtype):
    """Extension dtype for BigQuery JSON data."""

    name = "dbjson"

    @property
    def na_value(self) -> pd.NAType:  # type: ignore[name-defined]
        """Default NA value to use for this type."""
        return pd.NA

    @property
    def type(self) -> type[str]:  # type: ignore[override]
        """
        Return the scalar type for the array elements.
        The standard JSON data types can be one of `dict`, `list`, `str`, `int`, `float`,
        `bool` and `None`. However, this method returns a `str` type to indicate its
        storage type, because the union of multiple types are not supported well in pandas.
        """
        return str

    @property
    def pyarrow_dtype(self):
        """Return the pyarrow data type used for storing data in the pyarrow array."""
        return pa.string()

    @property
    def _is_numeric(self) -> bool:
        return False

    @property
    def _is_boolean(self) -> bool:
        return False

    @classmethod
    def construct_array_type(cls):
        """Return the array type associated with this dtype."""
        return JSONArray

    def __from_arrow__(self, array: pa.Array | pa.ChunkedArray) -> JSONArray:
        """Convert the pyarrow array to the extension array."""
        return JSONArray(array)


class JSONArray(arrays.ArrowExtensionArray):
    """Extension array that handles BigQuery JSON data, leveraging a string-based
    pyarrow array for storage. It enables seamless conversion to JSON objects when
    accessing individual elements."""

    _dtype = JSONDtype()

    def __init__(self, values) -> None:
        super().__init__(values)
        self._dtype = JSONDtype()
        if isinstance(values, pa.Array):
            pa_data = pa.chunked_array([values])
        elif isinstance(values, pa.ChunkedArray):
            pa_data = values
        else:
            raise NotImplementedError(
                f"Unsupported type '{type(values)}' for JSONArray"
            )

        # Ensures compatibility with pandas version 1.5.3
        if hasattr(self, "_data"):
            self._data = pa_data
        elif hasattr(self, "_pa_array"):
            self._pa_array = pa_data
        else:
            raise NotImplementedError(f"Unsupported pandas version: {pd.__version__}")

    def __arrow_array__(self, type=None):
        """Convert to an arrow array. This is required for pyarrow extension."""
        return pa.array(self.pa_data, type=JSONArrowType())

    def _from_pyarrow_array(self, pa_array):
        """Construct from a pyarrow Array/ChunkedArray.

        If the resulting pyarrow type does not match our string storage type
        (e.g., boolean arrays from comparisons == / !=, or integer arrays
        from apply(id)), return a standard ArrowExtensionArray instead of
        forcing non-string data into JSONArray.

        Required override for pandas 3.1.0:
        https://pandas.pydata.org/pandas-docs/stable/dev/whatsnew/v3.1.0.html
        """
        if pa_array.type != self._dtype.pyarrow_dtype:
            return arrays.ArrowExtensionArray(pa_array)
        _super_method = getattr(super(), "_from_pyarrow_array", None)
        if _super_method is not None:
            return _super_method(pa_array)
        return type(self)(pa_array)

    def _cast_pointwise_result(self, values):
        """Cast results of pointwise operations (e.g. loc expansion with dicts)
        back to JSONArray if values can be parsed as JSON, otherwise fall back.

        Required override for pandas 3.1.0:
        https://pandas.pydata.org/pandas-docs/stable/dev/whatsnew/v3.1.0.html
        """
        try:
            return type(self)._from_sequence(values, dtype=self.dtype)
        except Exception:
            _super_method = getattr(super(), "_cast_pointwise_result", None)
            if _super_method is not None:
                return _super_method(values)
            return np.asarray(values, dtype=object)

    @classmethod
    def _box_pa(
        cls, value, pa_type: pa.DataType | None = None
    ) -> pa.Array | pa.ChunkedArray | pa.Scalar:
        """Box value into a pyarrow Array, ChunkedArray or Scalar."""
        assert pa_type is None or pa_type == cls._dtype.pyarrow_dtype

        if isinstance(value, pa.Scalar) or not (
            common.is_list_like(value) and not common.is_dict_like(value)
        ):
            return cls._box_pa_scalar(value)
        return cls._box_pa_array(value)

    @classmethod
    def _box_pa_scalar(cls, value) -> pa.Scalar:
        """Box value into a pyarrow Scalar."""
        if pd.isna(value):
            pa_scalar = pa.scalar(None, type=cls._dtype.pyarrow_dtype)
        else:
            value = JSONArray._serialize_json(value)
            pa_scalar = pa.scalar(
                value, type=cls._dtype.pyarrow_dtype, from_pandas=True
            )

        return pa_scalar

    @classmethod
    def _box_pa_array(cls, value, copy: bool = False) -> pa.Array | pa.ChunkedArray:
        """Box value into a pyarrow Array or ChunkedArray."""
        if isinstance(value, cls):
            pa_array = value.pa_data
        else:
            value = [JSONArray._serialize_json(x) for x in value]
            pa_array = pa.array(value, type=cls._dtype.pyarrow_dtype, from_pandas=True)
        return pa_array

    @classmethod
    def _from_sequence(cls, scalars, *, dtype=None, copy=False):
        """Construct a new ExtensionArray from a sequence of scalars."""
        pa_array = cls._box_pa(scalars)
        arr = cls(pa_array)
        return arr

    @staticmethod
    def _serialize_json(value):
        """A static method that converts a JSON value into a string representation."""
        if not common.is_list_like(value) and pd.isna(value):
            return value
        else:
            # `sort_keys=True` sorts dictionary keys before serialization, making
            # JSON comparisons deterministic.
            # `separators=(',', ':')` eliminate whitespace to get the most compact
            # JSON representation.
            return json.dumps(value, sort_keys=True, separators=(",", ":"))

    @staticmethod
    def _deserialize_json(value):
        """A static method that converts a JSON string back into its original value."""
        if not pd.isna(value):
            return json.loads(value)
        else:
            return value

    @property
    def dtype(self) -> JSONDtype:
        """An instance of JSONDtype"""
        return self._dtype

    @property
    def pa_data(self):
        """An instance of stored pa data"""
        # Ensures compatibility with pandas version 1.5.3
        if hasattr(self, "_data"):
            return self._data
        elif hasattr(self, "_pa_array"):
            return self._pa_array
        else:
            raise NotImplementedError(f"Unsupported pandas version: {pd.__version__}")

    def _cmp_method(self, other, op):
        if op.__name__ == "eq":
            result = pyarrow.compute.equal(self.pa_data, self._box_pa(other))  # type: ignore[attr-defined]
        elif op.__name__ == "ne":
            result = pyarrow.compute.not_equal(self.pa_data, self._box_pa(other))  # type: ignore[attr-defined]
        else:
            # Comparison is not a meaningful one. We don't want to support sorting by JSON columns.
            raise TypeError(f"{op.__name__} not supported for JSONArray")
        return arrays.ArrowExtensionArray(result)

    def __getitem__(self, item):
        """Select a subset of self."""
        item = indexers.check_array_indexer(self, item)

        if isinstance(item, np.ndarray):
            if not len(item):
                return type(self)(pa.chunked_array([], type=self.dtype.pyarrow_dtype))
            elif item.dtype.kind in "iu":
                return self.take(item)
            else:
                # `check_array_indexer` should verify that the assertion hold true.
                assert item.dtype.kind == "b"
                return type(self)(self.pa_data.filter(item))
        elif isinstance(item, tuple):
            item = indexers.unpack_tuple_and_ellipses(item)  # type: ignore[attr-defined]

        if common.is_scalar(item) and not common.is_integer(item):
            # e.g. "foo" or 2.5
            # exception message copied from numpy
            raise IndexError(
                r"only integers, slices (`:`), ellipsis (`...`), numpy.newaxis "
                r"(`None`) and integer or boolean arrays are valid indices"
            )

        value = self.pa_data[item]
        if isinstance(value, pa.ChunkedArray):
            return type(self)(value)
        elif isinstance(value, pa.ExtensionScalar):
            return value.as_py()
        else:
            scalar = JSONArray._deserialize_json(value.as_py())
            if scalar is None:
                return self._dtype.na_value
            else:
                return scalar

    def __iter__(self):
        """Iterate over elements of the array."""
        for value in self.pa_data:
            val = JSONArray._deserialize_json(value.as_py())
            if val is None:
                yield self._dtype.na_value
            else:
                yield val

    def _reduce(
        self, name: str, *, skipna: bool = True, keepdims: bool = False, **kwargs
    ):
        """Return a scalar result of performing the reduction operation."""
        if name in ["min", "max"]:
            raise TypeError("JSONArray does not support min/max reducntion.")
        super()._reduce(name, skipna=skipna, keepdims=keepdims, **kwargs)

    def __array__(self, dtype=None, copy: bool | None = None) -> np.ndarray:
        """Correctly construct numpy arrays when passed to `np.asarray()`."""
        pa_type = self.pa_data.type
        data = self
        if dtype is None:
            empty = pa.array([], type=pa_type).to_numpy(zero_copy_only=False)
            dtype = empty.dtype
        result = np.empty(len(data), dtype=dtype)
        mask = data.isna()
        result[mask] = self._dtype.na_value
        result[~mask] = data[~mask].pa_data.to_numpy()
        return result


class JSONArrowType(pa.ExtensionType):
    """Arrow extension type for the `dbjson` Pandas extension type."""

    def __init__(self) -> None:
        super().__init__(pa.string(), "dbjson")

    def __arrow_ext_serialize__(self) -> bytes:
        return b""

    @classmethod
    def __arrow_ext_deserialize__(cls, storage_type, serialized) -> JSONArrowType:
        return JSONArrowType()

    def __hash__(self) -> int:
        return hash(str(self))

    def to_pandas_dtype(self):
        return JSONDtype()


# Register the type to be included in RecordBatches, sent over IPC and received in
# another Python process.
pa.register_extension_type(JSONArrowType())
