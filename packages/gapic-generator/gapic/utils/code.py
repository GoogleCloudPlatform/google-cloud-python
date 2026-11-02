# Copyright 2019 Google LLC
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

from typing import Callable, Iterable, List, Optional, Tuple, TypeVar
import itertools


def empty(content: str) -> bool:
    """Return True if this file has no Python statements, False otherwise.

    Args:
        content (str): A string containing Python code (or a lack thereof).
    """
    return not any(
        [i.lstrip() and not i.lstrip().startswith("#") for i in content.split("\n")]
    )


T = TypeVar("T")


def partition(
    predicate: Callable[[T], bool], iterator: Iterable[T]
) -> Tuple[List[T], List[T]]:
    """Partitions an iterable into two lists based on a predicate

    Args:
        predicate (Callable[[T], bool]) : A callable predicate on a single argument
                                          of whatever type is in iterator.
        iterator (Iterable(T)):           An iterable on any type.


    Returns:
        Tuple[List[T], List[T]]: The contents of iterator partitioned into two lists.
                                 The first list contains the "true" elements
                                 and the second contains the "false" elements.
    """
    results: Tuple[List[T], List[T]] = ([], [])

    for i in iterator:
        results[int(predicate(i))].append(i)

    # Returns trueList, falseList
    return results[1], results[0]


def nth(iterable: Iterable[T], n: int, default: Optional[T] = None) -> Optional[T]:
    """Return the nth element of an iterable or a default value.

    Args
        iterable (Iterable(T)): An iterable on any type.
        n (int):                The 'index' of the element to retrieve.
        default (Optional(T)):  An optional default element if the iterable has
                                 fewer than n elements.
    """
    return next(itertools.islice(iterable, n, None), default)


def make_private(object_name: str) -> str:
    """Labels the object name like a private object (i.e. prefixes it with underscore)

    If the object name already starts with underscore, returns the original name instead.
    This is to avoid adding name manging to an object.

    This is provided to templates as the ``make_private`` filter.

    Args:
        object_name (str): The name of the object to be made private.

    Returns:
        str: The final name of the privated object.
    """
    return object_name if object_name.startswith("_") else f"_{object_name}"
