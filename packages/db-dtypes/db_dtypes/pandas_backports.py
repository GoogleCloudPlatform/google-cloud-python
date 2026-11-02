# Copyright 2021 Google LLC
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

"""
Utilities to support older pandas versions.

These backported versions are simpler and, in some cases, less featureful than
the versions in the later versions of pandas.
"""

import packaging.version
import pandas
import pandas.compat.numpy.function

pandas_release = packaging.version.parse(pandas.__version__).release

# # Create aliases for private methods in case they move in a future version.
nanall = pandas.core.nanops.nanall  # type: ignore[attr-defined]
nanany = pandas.core.nanops.nanany  # type: ignore[attr-defined]
nanmax = pandas.core.nanops.nanmax  # type: ignore[attr-defined]
nanmin = pandas.core.nanops.nanmin  # type: ignore[attr-defined]
numpy_validate_all = pandas.compat.numpy.function.validate_all
numpy_validate_any = pandas.compat.numpy.function.validate_any
numpy_validate_max = pandas.compat.numpy.function.validate_max
numpy_validate_min = pandas.compat.numpy.function.validate_min

nanmedian = pandas.core.nanops.nanmedian  # type: ignore[attr-defined]
numpy_validate_median = pandas.compat.numpy.function.validate_median


def import_default(module_name, force=False, default=None):
    """
    Provide an implementation for a class or function when it can't be imported

    or when force is True.

    This is used to replicate Pandas APIs that are missing or insufficient
    (thus the force option) in early pandas versions.
    """

    if default is None:
        return lambda func_or_class: import_default(module_name, force, func_or_class)

    if force:
        return default

    name = default.__name__
    try:
        module = __import__(module_name, {}, {}, [name])
    except ModuleNotFoundError:
        return default

    return getattr(module, name, default)


# pandas.core.arraylike.OpsMixin is private, but the related public API
# "ExtensionScalarOpsMixin" is not sufficient for adding dates to times.
# It results in unsupported operand type(s) for +: 'datetime.time' and
# 'datetime.date'
@import_default("pandas.core.arraylike")
class OpsMixin:
    def _cmp_method(self, other, op):  # pragma: NO COVER
        return NotImplemented
