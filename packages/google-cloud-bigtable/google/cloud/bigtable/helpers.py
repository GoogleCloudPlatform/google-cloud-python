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

from itertools import islice
from typing import Generator, Iterable, Tuple, TypeVar

T = TypeVar("T")


# batched landed in standard library in Python 3.11.
def batched(iterable: Iterable[T], n) -> Generator[Tuple[T, ...], None, None]:
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    batch = tuple(islice(it, n))
    while batch:
        yield batch
        batch = tuple(islice(it, n))


class _MappableAttributesMixin:
    """
    Mixin for classes that need some of their attribute names remapped.

    This is for taking some of the classes from the data client row filters
    and row range classes that are 1:1 with their legacy client counterparts but with
    some of their attributes renamed. To use in a class, override the base class with this mixin
    class and define a map _attribute_map from legacy client attributes to data client
    attributes.

    Attributes are remapped and redefined in __init__ as well as getattr/setattr.
    """

    def __init__(self, *args, **kwargs):
        new_kwargs = {self._attribute_map.get(k, k): v for (k, v) in kwargs.items()}
        super(_MappableAttributesMixin, self).__init__(*args, **new_kwargs)

    def __getattr__(self, name):
        if name == "_attribute_map":
            raise AttributeError
        if name not in self._attribute_map:
            raise AttributeError
        return getattr(self, self._attribute_map[name])

    def __setattr__(self, name, value):
        if name == "_attribute_map":
            super(_MappableAttributesMixin, self).__setattr__(name, value)
            return
        attribute = self._attribute_map.get(name, name)
        super(_MappableAttributesMixin, self).__setattr__(attribute, value)
