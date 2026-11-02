# Copyright 2022 Google LLC
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
import typing

import numpy as np
import pandas as pd
import pandas._testing as tm
import pandas.tests.extension.base as base
import pytest


class TestJSONArrayCasting(base.BaseCastingTests):
    def test_astype_str(self, data):
        # Use `json.dumps(str)` instead of passing `str(obj)` directly to the super method.
        result = pd.Series(data[:5]).astype(str)
        expected = pd.Series(
            [json.dumps(x, sort_keys=True, separators=(",", ":")) for x in data[:5]],
            dtype=str,
        )
        tm.assert_series_equal(result, expected)

    @pytest.mark.parametrize(
        "nullable_string_dtype",
        [
            "string[python]",
            "string[pyarrow]",
        ],
    )
    def test_astype_string(self, data, nullable_string_dtype):
        # Use `json.dumps(str)` instead of passing `str(obj)` directly to the super method.
        result = pd.Series(data[:5]).astype(nullable_string_dtype)
        expected = pd.Series(
            [json.dumps(x, sort_keys=True, separators=(",", ":")) for x in data[:5]],
            dtype=nullable_string_dtype,
        )
        tm.assert_series_equal(result, expected)


class TestJSONArrayConstructors(base.BaseConstructorsTests):
    def test_from_dtype(self, data):
        # construct from our dtype & string dtype
        dtype = data.dtype

        expected = pd.Series(data)
        result = pd.Series(list(data), dtype=dtype)
        tm.assert_series_equal(result, expected)

        result = pd.Series(list(data), dtype=str(dtype))
        tm.assert_series_equal(result, expected)

        # Use `{"col1": data}` instead of passing `data` directly to the super method.
        # This prevents the DataFrame constructor from attempting to interpret the
        # dictionary as column headers.

        # gh-30280
        expected = pd.DataFrame({"col1": data}).astype(dtype)
        result = pd.DataFrame({"col1": list(data)}, dtype=dtype)
        tm.assert_frame_equal(result, expected)

        result = pd.DataFrame({"col1": list(data)}, dtype=str(dtype))
        tm.assert_frame_equal(result, expected)

    def test_series_constructor_scalar_with_index(self, data, dtype):
        # Use json.dumps(data[0]) instead of passing data[0] directly to the super method.
        # This prevents the Series constructor from attempting to interpret the dictionary
        # as column headers.
        scalar = json.dumps(data[0])
        result = pd.Series(scalar, index=[1, 2, 3], dtype=dtype)
        expected = pd.Series([scalar] * 3, index=[1, 2, 3], dtype=dtype)
        tm.assert_series_equal(result, expected)

        result = pd.Series(scalar, index=["foo"], dtype=dtype)
        expected = pd.Series([scalar], index=["foo"], dtype=dtype)
        tm.assert_series_equal(result, expected)


@pytest.mark.skip(reason="BigQuery does not allow group by a JSON-type column.")
class TestJSONArrayGroupby(base.BaseGroupbyTests):
    pass


class TestJSONArrayDtype(base.BaseDtypeTests):
    pass


class TestJSONArrayGetitem(base.BaseGetitemTests):
    @pytest.mark.xfail(reason="JSONDtype's type returns its storage type.")
    def test_getitem_scalar(self, data):
        """
        `_getitem_` can return any JSON-types objects while `data.dtype.type` returns
        a string to indicate its storage type.
        >       assert isinstance(result, data.dtype.type)
        E       AssertionError
        """
        super().test_getitem_scalar(data)

    def test_take_pandas_style_negative_raises(self, data, na_value):
        # This test was failing compliance checks because it attempted to match
        # a pytest regex match using an empty string (""), which pytest version
        # 8.4.0 stopped allowing.
        # The test has been updated in pandas main so that it will
        # no longer fail, but the fix is not expected to be released until
        # at least pandas version 3.0 (current version is 2.3).
        with pytest.raises(ValueError):
            data.take([0, -2], fill_value=na_value, allow_fill=True)

    def test_getitem_propagates_readonly_property(self, data):
        pytest.xfail("Failing with pandas prerelease: readonly propagation issue")


class TestJSONArrayIndex(base.BaseIndexTests):
    pass


class TestJSONArrayInterface(base.BaseInterfaceTests):
    def test_array_interface(self, data):
        result = np.array(data)
        # Use `json.dumps(data[0])` instead of passing `data[0]` directly to the super method.
        assert result[0] == json.dumps(data[0], sort_keys=True, separators=(",", ":"))

        result = np.array(data, dtype=object)
        # Use `json.dumps(x)` instead of passing `x` directly to the super method.
        expected = np.array(
            [json.dumps(x, sort_keys=True, separators=(",", ":")) for x in data],
            dtype=object,
        )
        # if expected.ndim > 1:
        #     # nested data, explicitly construct as 1D
        #     expected = construct_1d_object_array_from_listlike(list(data))
        tm.assert_numpy_array_equal(result, expected)

    @pytest.mark.skip(reason="2D support not implemented for JSONArray")
    def test_view(self, data):
        super().test_view(data)

    def test_array_interface_copy(self, data):
        # This test was failing compliance checks due to changes in how
        # numpy handles processing when np.array(obj, copy=False).
        # Until pandas changes the existing tests, this compliance test
        # will continue to fail.
        import numpy as np

        np_version_gt2 = int(np.__version__.split(".")[0]) >= 2

        result_copy1 = np.array(data, copy=True)
        result_copy2 = np.array(data, copy=True)
        assert not np.may_share_memory(result_copy1, result_copy2)

        if not np_version_gt2:
            # copy=False semantics are only supported in NumPy>=2.
            return

        result_nocopy1 = np.array(data, copy=False)
        result_nocopy2 = np.array(data, copy=False)
        assert not np.may_share_memory(result_nocopy1, result_nocopy2)

    def test_contains(self, data, data_missing, using_nan_is_na):
        pytest.xfail("Failing with pandas prerelease: specific NA handling mismatch")

    def test_len(self, data):
        assert len(data) == 100

    def test_size(self, data):
        assert data.size == 100


class TestJSONArrayParsing(base.BaseParsingTests):
    @pytest.mark.xfail(reason="data type 'json' not understood")
    @pytest.mark.parametrize("engine", ["c", "python"])
    def test_EA_types(self, engine, data, request):
        super().test_EA_types(engine, data, request)


class TestJSONArrayMethods(base.BaseMethodsTests):
    @pytest.mark.xfail(
        reason="`to_numpy` returns serialized JSON, "
        + "while `__getitem__` returns JSON objects."
    )
    def test_map(self, data_missing, na_action):
        super().test_map(data_missing, na_action)

    @pytest.mark.xfail(reason="read_json does not preserve custom ExtensionDtype")
    def test_json_roundtrip(self, data):
        super().test_json_roundtrip(data)

    @pytest.mark.xfail(reason="Unhashable")
    def test_value_counts_with_normalize(self, data):
        super().test_value_counts_with_normalize(data)

    @pytest.mark.skip("fill-value is interpreted as a dict of values")
    def test_fillna_copy_frame(self, data_missing):
        super().test_fillna_copy_frame(data_missing)

    @pytest.mark.xfail(reason="combine for JSONArray not supported")
    def test_combine_le(self, data_repeated):
        super().test_combine_le(data_repeated)

    @pytest.mark.skip(reason="'<' not supported between instances of 'dict' and 'dict'")
    def test_searchsorted(self, data_for_sorting, as_series):
        super().test_searchsorted(self, data_for_sorting, as_series)

    @pytest.mark.xfail(
        reason="`to_numpy` returns serialized JSON, "
        + "while `__getitem__` returns JSON objects."
    )
    def test_where_series(self, data, na_value, as_frame):
        # `Series.where` calls `to_numpy` to get results.
        super().test_where_series(data, na_value, as_frame)

    @pytest.mark.skip(reason="BigQuery does not allow group by a JSON-type column.")
    def test_factorize(self, data_for_grouping):
        super().test_factorize(data_for_grouping)

    @pytest.mark.skip(reason="BigQuery does not allow group by a JSON-type column.")
    def test_factorize_equivalence(self, data_for_grouping):
        super().test_factorize_equivalence(data_for_grouping)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_argsort(self, data_for_sorting):
        super().test_argsort(data_for_sorting)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_argmin_argmax(self, data_for_sorting):
        super().test_argmin_argmax(data_for_sorting)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_sort_values(self, data_for_sorting):
        super().test_sort_values(data_for_sorting)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_sort_values_frame(self, data_for_sorting):
        super().test_sort_values_frame(data_for_sorting)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_rank(self, data_for_sorting, ascending):
        super().test_rank(data_for_sorting, ascending)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_rank_method(self, data_for_sorting, method):
        super().test_rank_method(data_for_sorting, method)

    @pytest.mark.skip(reason="BigQuery does not allow sort by a JSON-type column.")
    def test_rank_missing(self, data_missing_for_sorting, na_option):
        super().test_rank_missing(data_missing_for_sorting, na_option)

    def test_argmax_argmin_no_skipna_notimplemented(self, data_missing_for_sorting):
        # This test was failing compliance checks because it attempted to match
        # a pytest regex match using an empty string (""), which pytest version
        # 8.4.0 stopped allowing.
        # The test has been updated in pandas main so that it will
        # no longer fail, but the fix is not expected to be released until
        # at least pandas version 3.0 (current version is 2.3)
        data = data_missing_for_sorting

        with pytest.raises((NotImplementedError, ValueError)):
            data.argmin(skipna=False)

        with pytest.raises((NotImplementedError, ValueError)):
            data.argmax(skipna=False)

    def test_fillna_limit_frame(self, data_missing):
        pytest.xfail("Failing with pandas prerelease: NA mask mismatch")

    def test_fillna_limit_series(self, data_missing):
        pytest.xfail("Failing with pandas prerelease: NA mask mismatch")


class TestJSONArrayMissing(base.BaseMissingTests):
    @pytest.mark.xfail(reason="Setting a dict as a scalar")
    def test_fillna_series(self):
        """We treat dictionaries as a mapping in fillna, not a scalar."""
        super().test_fillna_series()

    @pytest.mark.xfail(reason="Setting a dict as a scalar")
    def test_fillna_frame(self):
        """We treat dictionaries as a mapping in fillna, not a scalar."""
        super().test_fillna_frame()

    @pytest.mark.xfail(reason="Setting a dict as a scalar")
    def test_fillna_scalar(self, data_missing):
        super().test_fillna_scalar(data_missing)

    def test_fillna_no_op_returns_copy(self, data):
        pytest.xfail("Failing with pandas prerelease: copy behavior change")

    def test_fillna_readonly(self, data_missing):
        pytest.xfail("Failing with pandas prerelease: readonly check missing")


@pytest.mark.skip(reason="BigQuery JSON does not allow Arithmetic Ops.")
class TestJSONArrayArithmeticOps(base.BaseArithmeticOpsTests):
    pass


class TestJSONArrayComparisonOps(base.BaseComparisonOpsTests):
    def test_compare_array(self, data, comparison_op, request):
        if comparison_op.__name__ not in ["eq", "ne"]:
            mark = pytest.mark.xfail(reason="Comparison methods not implemented")
            request.applymarker(mark)
        super().test_compare_array(data, comparison_op)

    def test_compare_scalar(self, data, comparison_op, request):
        if comparison_op.__name__ not in ["eq", "ne"]:
            mark = pytest.mark.xfail(reason="Comparison methods not implemented")
            request.applymarker(mark)
        super().test_compare_scalar(data, comparison_op)

    def _cast_pointwise_result(self, op_name: str, obj, other, pointwise_result):
        dtype = typing.cast(pd.StringDtype, tm.get_dtype(obj))
        if op_name in ["__add__", "__radd__"]:
            cast_to = dtype
        else:
            cast_to = "boolean[pyarrow]"  # type: ignore[assignment]
        return pointwise_result.astype(cast_to)


class TestJSONArrayUnaryOps(base.BaseUnaryOpsTests):
    pass


class TestJSONArrayPrinting(base.BasePrintingTests):
    pass


class TestJSONArrayReduce(base.BaseReduceTests):
    @pytest.mark.skip(reason="JSONArray does not support reduce_array")
    def test_reduce_array(self, request, data, all_reductions, skipna: bool):
        super().test_reduce_array(request, data, all_reductions, skipna)

    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    @pytest.mark.parametrize("skipna", [True, False])
    def test_reduce_series_numeric(self, data, all_numeric_reductions, skipna):
        op_name = all_numeric_reductions
        ser = pd.Series(data)

        if not self._supports_reduction(ser, op_name):
            # Sum does not raise an Error (TypeError or otherwise)
            if op_name != "sum":
                with pytest.raises(TypeError):
                    getattr(ser, op_name)(skipna=skipna)
        else:
            # min/max with empty produce numpy warnings
            self.check_reduce(ser, op_name, skipna)


class TestJSONArrayReshaping(base.BaseReshapingTests):
    @pytest.mark.skip(reason="2D support not implemented for JSONArray")
    def test_transpose(self, data):
        super().test_transpose(data)

    @pytest.mark.xfail(
        reason="`to_numpy` returns serialized JSON, "
        + "while `__getitem__` returns JSON objects."
    )
    def test_transpose_frame(self, data):
        # `DataFrame.T` calls `to_numpy` to get results.
        super().test_transpose_frame(data)

    def test_stack(self, data):
        pytest.xfail("Failing with pandas prerelease: stack string escaping issue")


class TestJSONArraySetitem(base.BaseSetitemTests):
    # Patching `[....] * len()` to base.BaseSetitemTests because pandas' internals
    # has trouble setting sequences of values into scalar positions.

    @pytest.mark.parametrize(
        "idx",
        [[0, 1, 2], pd.array([0, 1, 2], dtype="Int64"), np.array([0, 1, 2])],
        ids=["list", "integer-array", "numpy-array"],
    )
    def test_setitem_integer_array(self, data, idx, box_in_series):
        arr = data[:5].copy()
        expected = data.take([0, 0, 0, 3, 4])

        if box_in_series:
            arr = pd.Series(arr)
            expected = pd.Series(expected)

        # Use `[arr[0]] * len()` instead of passing `arr[0]` directly to the super method.
        arr[idx] = [arr[0]] * len(arr[idx])
        tm.assert_equal(arr, expected)

    @pytest.mark.parametrize(
        "mask",
        [
            np.array([True, True, True, False, False]),
            pd.array([True, True, True, False, False], dtype="boolean"),
            pd.array([True, True, True, pd.NA, pd.NA], dtype="boolean"),
        ],
        ids=["numpy-array", "boolean-array", "boolean-array-na"],
    )
    def test_setitem_mask(self, data, mask, box_in_series):
        arr = data[:5].copy()
        expected = arr.take([0, 0, 0, 3, 4])
        if box_in_series:
            arr = pd.Series(arr)
            expected = pd.Series(expected)
        # Use `[data[0]] * len()` instead of passing `data[0]` directly to the super method.
        arr[mask] = [data[0]] * len(arr[mask])
        tm.assert_equal(expected, arr)

    def test_setitem_loc_iloc_slice(self, data):
        arr = data[:5].copy()
        s = pd.Series(arr, index=["a", "b", "c", "d", "e"])
        expected = pd.Series(data.take([0, 0, 0, 3, 4]), index=s.index)

        result = s.copy()
        # Use `[data[0]] * len()` instead of passing `data[0]` directly to the super method.
        result.iloc[:3] = [data[0]] * len(result.iloc[:3])
        tm.assert_equal(result, expected)

        result = s.copy()
        result.loc[:"c"] = [data[0]] * len(result.loc[:"c"])
        tm.assert_equal(result, expected)

    def test_setitem_slice(self, data, box_in_series):
        arr = data[:5].copy()
        expected = data.take([0, 0, 0, 3, 4])
        if box_in_series:
            arr = pd.Series(arr)
            expected = pd.Series(expected)

        # Use `[data[0]] * 3` instead of passing `data[0]` directly to the super method.
        arr[:3] = [data[0]] * 3
        tm.assert_equal(arr, expected)

    @pytest.mark.xfail(reason="only integer scalar arrays can be converted")
    def test_setitem_2d_values(self, data):
        super().test_setitem_2d_values(data)

    @pytest.mark.xfail(
        reason="`to_numpy` returns serialized JSON, "
        + "while `__getitem__` returns JSON objects."
    )
    def test_setitem_frame_2d_values(self, data):
        super().test_setitem_frame_2d_values(data)

    @pytest.mark.parametrize("setter", ["loc", None])
    def test_setitem_mask_broadcast(self, data, setter):
        ser = pd.Series(data)
        mask = np.zeros(len(data), dtype=bool)
        mask[:2] = True

        if setter:  # loc
            target = getattr(ser, setter)
        else:  # __setitem__
            target = ser

        # Use `[data[10]] * len()` instead of passing `data[10]` directly to the super method.
        target[mask] = [data[10]] * len(target[mask])
        assert ser[0] == data[10]
        assert ser[1] == data[10]

    @pytest.mark.xfail(reason="eq not implemented for <class 'dict'>")
    def test_setitem_mask_boolean_array_with_na(self, data, box_in_series):
        super().test_setitem_mask_boolean_array_with_na(data, box_in_series)

    @pytest.mark.skip(reason="2D support not implemented for JSONArray")
    def test_setitem_preserves_views(self, data):
        super().test_setitem_preserves_views(data)

    def test_setitem_invalid(self, data, invalid_scalar):
        # This test was failing compliance checks because it attempted to match
        # a pytest regex match using an empty string (""), which pytest version
        # 8.4.0 stopped allowing.
        # The test has been updated in pandas main so that it will
        # no longer fail, but the fix is not expected to be released until
        # at least pandas version 3.0 (current version is 2.3)
        with pytest.raises((ValueError, TypeError)):
            data[0] = invalid_scalar

        with pytest.raises((ValueError, TypeError)):
            data[:] = invalid_scalar


class TestJSONArrayDim2Compat(base.Dim2CompatTests):
    pass
