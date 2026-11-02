# Copyright 2025 Google LLC
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

from __future__ import annotations

import datetime
from abc import ABC, abstractmethod
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generic,
    Sequence,
    TypeVar,
)

if TYPE_CHECKING:
    from google.cloud.firestore_v1.base_pipeline import _BasePipeline

from google.cloud.firestore_v1._helpers import GeoPoint, decode_value, encode_value
from google.cloud.firestore_v1.pipeline_types import (
    Ordering,
    PipelineDataType,
    TimeGranularity,
    TimePart,
    TimeUnit,
)
from google.cloud.firestore_v1.types.document import Pipeline as Pipeline_pb
from google.cloud.firestore_v1.types.document import Value
from google.cloud.firestore_v1.types.query import StructuredQuery as Query_pb
from google.cloud.firestore_v1.vector import Vector

CONSTANT_TYPE = TypeVar(
    "CONSTANT_TYPE",
    str,
    int,
    float,
    bool,
    datetime.datetime,
    bytes,
    GeoPoint,
    Vector,
    None,
)


class Expression(ABC):
    """Represents an expression that can be evaluated to a value within the
    execution of a pipeline.

    Expressions are the building blocks for creating complex queries and
    transformations in Firestore pipelines. They can represent:

    - **Field references:** Access values from document fields.
    - **Literals:** Represent constant values (strings, numbers, booleans).
    - **FunctionExpression calls:** Apply functions to one or more expressions.
    - **Aggregations:** Calculate aggregate values (e.g., sum, average) over a set of documents.

    The `Expression` class provides a fluent API for building expressions. You can chain
    together method calls to create complex expressions.
    """

    # Controls whether expression methods (e.g., .add(), .multiply()) can be called on
    # instances of this class or its subclasses. Set to False for non-computational
    # expressions like AliasedExpression.
    _supports_expr_methods = True

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    @abstractmethod
    def _to_pb(self) -> Value:
        raise NotImplementedError

    @staticmethod
    def _cast_to_expr_or_convert_to_constant(
        o: Any, include_vector=False
    ) -> "Expression":
        """Convert arbitrary object to an Expression."""
        if isinstance(o, Expression):
            return o
        if isinstance(o, Enum):
            o = o.value
        if isinstance(o, dict):
            return Map(o)
        if isinstance(o, list):
            if include_vector and all([isinstance(i, (float, int)) for i in o]):
                return Constant(Vector(o))
            else:
                return Array(o)
        return Constant(o)

    class expose_as_static:
        """
        Decorator to mark instance methods to be exposed as static methods as well as instance
        methods.

        When called statically, the first argument is converted to a Field expression if needed.

        Example:
            >>> Field.of("test").add(5)
            >>> FunctionExpression.add("test", 5)
        """

        def __init__(self, instance_func):
            self.instance_func = instance_func

        def static_func(self, first_arg, *other_args, **kwargs):
            if getattr(first_arg, "_supports_expr_methods", True) is False:
                raise TypeError(
                    f"Cannot call '{self.instance_func.__name__}' on {type(first_arg).__name__}."
                )
            if not isinstance(first_arg, (Expression, str)):
                raise TypeError(
                    f"'{self.instance_func.__name__}' must be called on an Expression or a string representing a field. got {type(first_arg)}."
                )
            first_expr = (
                Field.of(first_arg)
                if not isinstance(first_arg, Expression)
                else first_arg
            )
            return self.instance_func(first_expr, *other_args, **kwargs)

        def __get__(self, instance, owner):
            if instance is None:
                return self.static_func
            else:
                if getattr(instance, "_supports_expr_methods", True) is False:
                    raise TypeError(
                        f"Cannot call '{self.instance_func.__name__}' on {type(instance).__name__}."
                    )
                return self.instance_func.__get__(instance, owner)

    @expose_as_static
    def get_field(self, key: Expression | str) -> "Expression":
        """Accesses a field/property of the expression that evaluates to a Map or Document.

        Example:
            >>> # Access the 'city' field from the 'address' map field.
            >>> Field.of("address").get_field("city")
            >>> # Create a map and access a field from it.
            >>> Map({"foo": "bar"}).get_field("foo")

        Args:
            key: The key of the field to access.

        Returns:
            A new `Expression` representing the value of the field.
        """
        return FunctionExpression(
            "get_field", [self, self._cast_to_expr_or_convert_to_constant(key)]
        )

    @expose_as_static
    def add(self, other: Expression | float) -> "Expression":
        """Creates an expression that adds this expression to another expression or constant.

        Example:
            >>> # Add the value of the 'quantity' field and the 'reserve' field.
            >>> Field.of("quantity").add(Field.of("reserve"))
            >>> # Add 5 to the value of the 'age' field
            >>> Field.of("age").add(5)

        Args:
            other: The expression or constant value to add to this expression.

        Returns:
            A new `Expression` representing the addition operation.
        """
        return FunctionExpression(
            "add", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def subtract(self, other: Expression | float) -> "Expression":
        """Creates an expression that subtracts another expression or constant from this expression.

        Example:
            >>> # Subtract the 'discount' field from the 'price' field
            >>> Field.of("price").subtract(Field.of("discount"))
            >>> # Subtract 20 from the value of the 'total' field
            >>> Field.of("total").subtract(20)

        Args:
            other: The expression or constant value to subtract from this expression.

        Returns:
            A new `Expression` representing the subtraction operation.
        """
        return FunctionExpression(
            "subtract", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def multiply(self, other: Expression | float) -> "Expression":
        """Creates an expression that multiplies this expression by another expression or constant.

        Example:
            >>> # Multiply the 'quantity' field by the 'price' field
            >>> Field.of("quantity").multiply(Field.of("price"))
            >>> # Multiply the 'value' field by 2
            >>> Field.of("value").multiply(2)

        Args:
            other: The expression or constant value to multiply by.

        Returns:
            A new `Expression` representing the multiplication operation.
        """
        return FunctionExpression(
            "multiply", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def divide(self, other: Expression | float) -> "Expression":
        """Creates an expression that divides this expression by another expression or constant.

        Example:
            >>> # Divide the 'total' field by the 'count' field
            >>> Field.of("total").divide(Field.of("count"))
            >>> # Divide the 'value' field by 10
            >>> Field.of("value").divide(10)

        Args:
            other: The expression or constant value to divide by.

        Returns:
            A new `Expression` representing the division operation.
        """
        return FunctionExpression(
            "divide", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def mod(self, other: Expression | float) -> "Expression":
        """Creates an expression that calculates the modulo (remainder) to another expression or constant.

        Example:
            >>> # Calculate the remainder of dividing the 'value' field by field 'divisor'.
            >>> Field.of("value").mod(Field.of("divisor"))
            >>> # Calculate the remainder of dividing the 'value' field by 5.
            >>> Field.of("value").mod(5)

        Args:
            other: The divisor expression or constant.

        Returns:
            A new `Expression` representing the modulo operation.
        """
        return FunctionExpression(
            "mod", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def abs(self) -> "Expression":
        """Creates an expression that calculates the absolute value of this expression.

        Example:
            >>> # Get the absolute value of the 'change' field.
            >>> Field.of("change").abs()

        Returns:
            A new `Expression` representing the absolute value.
        """
        return FunctionExpression("abs", [self])

    @expose_as_static
    def ceil(self) -> "Expression":
        """Creates an expression that calculates the ceiling of this expression.

        Example:
            >>> # Get the ceiling of the 'value' field.
            >>> Field.of("value").ceil()

        Returns:
            A new `Expression` representing the ceiling value.
        """
        return FunctionExpression("ceil", [self])

    @expose_as_static
    def exp(self) -> "Expression":
        """Creates an expression that computes e to the power of this expression.

        Example:
            >>> # Compute e to the power of the 'value' field
            >>> Field.of("value").exp()

        Returns:
            A new `Expression` representing the exponential value.
        """
        return FunctionExpression("exp", [self])

    @expose_as_static
    def floor(self) -> "Expression":
        """Creates an expression that calculates the floor of this expression.

        Example:
            >>> # Get the floor of the 'value' field.
            >>> Field.of("value").floor()

        Returns:
            A new `Expression` representing the floor value.
        """
        return FunctionExpression("floor", [self])

    @expose_as_static
    def ln(self) -> "Expression":
        """Creates an expression that calculates the natural logarithm of this expression.

        Example:
            >>> # Get the natural logarithm of the 'value' field.
            >>> Field.of("value").ln()

        Returns:
            A new `Expression` representing the natural logarithm.
        """
        return FunctionExpression("ln", [self])

    @expose_as_static
    def log(self, base: Expression | float) -> "Expression":
        """Creates an expression that calculates the logarithm of this expression with a given base.

        Example:
            >>> # Get the logarithm of 'value' with base 2.
            >>> Field.of("value").log(2)
            >>> # Get the logarithm of 'value' with base from 'base_field'.
            >>> Field.of("value").log(Field.of("base_field"))

        Args:
            base: The base of the logarithm.

        Returns:
            A new `Expression` representing the logarithm.
        """
        return FunctionExpression(
            "log", [self, self._cast_to_expr_or_convert_to_constant(base)]
        )

    @expose_as_static
    def log10(self) -> "Expression":
        """Creates an expression that calculates the base 10 logarithm of this expression.

        Example:
            >>> Field.of("value").log10()

        Returns:
            A new `Expression` representing the logarithm.
        """
        return FunctionExpression("log10", [self])

    @expose_as_static
    def pow(self, exponent: Expression | float) -> "Expression":
        """Creates an expression that calculates this expression raised to the power of the exponent.

        Example:
            >>> # Raise 'base_val' to the power of 2.
            >>> Field.of("base_val").pow(2)
            >>> # Raise 'base_val' to the power of 'exponent_val'.
            >>> Field.of("base_val").pow(Field.of("exponent_val"))

        Args:
            exponent: The exponent.

        Returns:
            A new `Expression` representing the power operation.
        """
        return FunctionExpression(
            "pow", [self, self._cast_to_expr_or_convert_to_constant(exponent)]
        )

    @expose_as_static
    def round(self) -> "Expression":
        """Creates an expression that rounds this expression to the nearest integer.

        Example:
            >>> # Round the 'value' field.
            >>> Field.of("value").round()

        Returns:
            A new `Expression` representing the rounded value.
        """
        return FunctionExpression("round", [self])

    @expose_as_static
    def sqrt(self) -> "Expression":
        """Creates an expression that calculates the square root of this expression.

        Example:
            >>> # Get the square root of the 'area' field.
            >>> Field.of("area").sqrt()

        Returns:
            A new `Expression` representing the square root.
        """
        return FunctionExpression("sqrt", [self])

    @expose_as_static
    def trunc(self, places: Expression | int | None = None) -> "Expression":
        """Creates an expression that truncates the numeric value. If places is None,
        truncates to an integer. Otherwise, truncates the numeric value to the
        specified number of decimal places.

        Example:
            >>> # Truncate the 'value' field to 2 decimal places.
            >>> Field.of("value").trunc(PipelineSource.literals(2))

        Returns:
            A new `Expression` representing the truncated value.
        """
        params = (
            [self, self._cast_to_expr_or_convert_to_constant(places)]
            if places is not None
            else [self]
        )
        return FunctionExpression("trunc", params)

    @expose_as_static
    def logical_maximum(self, *others: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns the larger value between this expression
        and another expression or constant, based on Firestore's value type ordering.

        Firestore's value type ordering is described here:
        https://cloud.google.com/firestore/docs/concepts/data-types#value_type_ordering

        Example:
            >>> # Returns the larger value between the 'discount' field and the 'cap' field.
            >>> Field.of("discount").logical_maximum(Field.of("cap"))
            >>> # Returns the larger value between the 'value' field and some ints
            >>> Field.of("value").logical_maximum(10, 20, 30)

        Args:
            others: The other expression or constant values to compare with.

        Returns:
            A new `Expression` representing the logical maximum operation.
        """
        return FunctionExpression(
            "maximum",
            [self] + [self._cast_to_expr_or_convert_to_constant(o) for o in others],
            repr_function=FunctionExpression._build_infix_repr("logical_maximum"),
        )

    @expose_as_static
    def logical_minimum(self, *others: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns the smaller value between this expression
        and another expression or constant, based on Firestore's value type ordering.

        Firestore's value type ordering is described here:
        https://cloud.google.com/firestore/docs/concepts/data-types#value_type_ordering

        Example:
            >>> # Returns the smaller value between the 'discount' field and the 'floor' field.
            >>> Field.of("discount").logical_minimum(Field.of("floor"))
            >>> # Returns the smaller value between the 'value' field and some ints
            >>> Field.of("value").logical_minimum(10, 20, 30)

        Args:
            others: The other expression or constant values to compare with.

        Returns:
            A new `Expression` representing the logical minimum operation.
        """
        return FunctionExpression(
            "minimum",
            [self] + [self._cast_to_expr_or_convert_to_constant(o) for o in others],
            repr_function=FunctionExpression._build_infix_repr("logical_minimum"),
        )

    @expose_as_static
    def equal(self, other: Expression | CONSTANT_TYPE) -> "BooleanExpression":
        """Creates an expression that checks if this expression is equal to another
        expression or constant value.

        Example:
            >>> # Check if the 'age' field is equal to 21
            >>> Field.of("age").equal(21)
            >>> # Check if the 'city' field is equal to "London"
            >>> Field.of("city").equal("London")

        Args:
            other: The expression or constant value to compare for equality.

        Returns:
            A new `Expression` representing the equality comparison.
        """
        return BooleanExpression(
            "equal", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def not_equal(self, other: Expression | CONSTANT_TYPE) -> "BooleanExpression":
        """Creates an expression that checks if this expression is not equal to another
        expression or constant value.

        Example:
            >>> # Check if the 'status' field is not equal to "completed"
            >>> Field.of("status").not_equal("completed")
            >>> # Check if the 'country' field is not equal to "USA"
            >>> Field.of("country").not_equal("USA")

        Args:
            other: The expression or constant value to compare for inequality.

        Returns:
            A new `Expression` representing the inequality comparison.
        """
        return BooleanExpression(
            "not_equal", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def greater_than(self, other: Expression | CONSTANT_TYPE) -> "BooleanExpression":
        """Creates an expression that checks if this expression is greater than another
        expression or constant value.

        Example:
            >>> # Check if the 'age' field is greater than the 'limit' field
            >>> Field.of("age").greater_than(Field.of("limit"))
            >>> # Check if the 'price' field is greater than 100
            >>> Field.of("price").greater_than(100)

        Args:
            other: The expression or constant value to compare for greater than.

        Returns:
            A new `Expression` representing the greater than comparison.
        """
        return BooleanExpression(
            "greater_than", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def greater_than_or_equal(
        self, other: Expression | CONSTANT_TYPE
    ) -> "BooleanExpression":
        """Creates an expression that checks if this expression is greater than or equal
        to another expression or constant value.

        Example:
            >>> # Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
            >>> Field.of("quantity").greater_than_or_equal(Field.of('requirement').add(1))
            >>> # Check if the 'score' field is greater than or equal to 80
            >>> Field.of("score").greater_than_or_equal(80)

        Args:
            other: The expression or constant value to compare for greater than or equal to.

        Returns:
            A new `Expression` representing the greater than or equal to comparison.
        """
        return BooleanExpression(
            "greater_than_or_equal",
            [self, self._cast_to_expr_or_convert_to_constant(other)],
        )

    @expose_as_static
    def less_than(self, other: Expression | CONSTANT_TYPE) -> "BooleanExpression":
        """Creates an expression that checks if this expression is less than another
        expression or constant value.

        Example:
            >>> # Check if the 'age' field is less than 'limit'
            >>> Field.of("age").less_than(Field.of('limit'))
            >>> # Check if the 'price' field is less than 50
            >>> Field.of("price").less_than(50)

        Args:
            other: The expression or constant value to compare for less than.

        Returns:
            A new `Expression` representing the less than comparison.
        """
        return BooleanExpression(
            "less_than", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def less_than_or_equal(
        self, other: Expression | CONSTANT_TYPE
    ) -> "BooleanExpression":
        """Creates an expression that checks if this expression is less than or equal to
        another expression or constant value.

        Example:
            >>> # Check if the 'quantity' field is less than or equal to 20
            >>> Field.of("quantity").less_than_or_equal(Constant.of(20))
            >>> # Check if the 'score' field is less than or equal to 70
            >>> Field.of("score").less_than_or_equal(70)

        Args:
            other: The expression or constant value to compare for less than or equal to.

        Returns:
            A new `Expression` representing the less than or equal to comparison.
        """
        return BooleanExpression(
            "less_than_or_equal",
            [self, self._cast_to_expr_or_convert_to_constant(other)],
        )

    @expose_as_static
    def between(
        self, lower: Expression | float, upper: Expression | float
    ) -> "BooleanExpression":
        """Evaluates if the result of this expression is between
        the lower bound (inclusive) and upper bound (inclusive).

        This is functionally equivalent to performing an `And` operation with
        `greater_than_or_equal` and `less_than_or_equal`.

        Example:
            >>> # Check if the 'age' field is between 18 and 65
            >>> Field.of("age").between(18, 65)

        Args:
            lower: Lower bound (inclusive) of the range.
            upper: Upper bound (inclusive) of the range.

        Returns:
            A new `BooleanExpression` representing the between comparison.
        """
        return And(
            self.greater_than_or_equal(lower),
            self.less_than_or_equal(upper),
        )

    @expose_as_static
    def geo_distance(
        self, other: Expression | GeoPoint | tuple[float, float]
    ) -> "FunctionExpression":
        """Evaluates to the distance in meters between the location in the specified
        field and the query location.

        .. note::
            This feature is currently in beta and is subject to change.
        Note: This Expression can only be used within a `Search` stage.

        Example:
            >>> # Calculate distance between the 'location' field and a target GeoPoint
            >>> Field.of("location").geo_distance(target_point)
            >>> # Calculate distance between the 'location' field and a (latitude, longitude) tuple
            >>> Field.of("location").geo_distance((37.7749, -122.4194))

        Args:
            other: target point used to calculate distance. Can be a GeoPoint, an
                Expression resolving to a GeoPoint, or a (latitude, longitude) tuple.

        Returns:
            A new `FunctionExpression` representing the distance.
        """
        if isinstance(other, tuple) and len(other) == 2:
            other = GeoPoint(other[0], other[1])

        return FunctionExpression(
            "geo_distance", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def equal_any(
        self, array: Array | Sequence[Expression | CONSTANT_TYPE] | Expression
    ) -> "BooleanExpression":
        """Creates an expression that checks if this expression is equal to any of the
        provided values or expressions.

        Example:
            >>> # Check if the 'category' field is either "Electronics" or value of field 'primaryType'
            >>> Field.of("category").equal_any(["Electronics", Field.of("primaryType")])

        Args:
            array: The values or expressions to check against.

        Returns:
            A new `Expression` representing the 'IN' comparison.
        """
        return BooleanExpression(
            "equal_any",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(array),
            ],
        )

    @expose_as_static
    def not_equal_any(
        self, array: Array | list[Expression | CONSTANT_TYPE] | Expression
    ) -> "BooleanExpression":
        """Creates an expression that checks if this expression is not equal to any of the
        provided values or expressions.

        Example:
            >>> # Check if the 'status' field is neither "pending" nor "cancelled"
            >>> Field.of("status").not_equal_any(["pending", "cancelled"])

        Args:
            array: The values or expressions to check against.

        Returns:
            A new `Expression` representing the 'NOT IN' comparison.
        """
        return BooleanExpression(
            "not_equal_any",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(array),
            ],
        )

    @expose_as_static
    def array_get(self, offset: Expression | int) -> "FunctionExpression":
        """
        Creates an expression that indexes into an array from the beginning or end and returns the
        element. A negative offset starts from the end.

        If the expression is evaluated against a non-array type, it evaluates to an error. See `offset`
        for an alternative that evaluates to unset instead.

        Example:
            >>> Array([1,2,3]).array_get(0)

        Args:
            offset: the index of the element to return

        Returns:
            A new `Expression` representing the `array_get` operation.
        """
        return FunctionExpression(
            "array_get", [self, self._cast_to_expr_or_convert_to_constant(offset)]
        )

    @expose_as_static
    def offset(self, offset: Expression | int) -> "FunctionExpression":
        """
        Creates an expression that indexes into an array from the beginning or end and returns the
        element. A negative offset starts from the end.
        If the expression is evaluated against a non-array type, it evaluates to unset.

        Example:
            >>> Array([1,2,3]).offset(0)

        Args:
            offset: the index of the element to return

        Returns:
            A new `Expression` representing the `offset` operation.
        """
        return FunctionExpression(
            "offset", [self, self._cast_to_expr_or_convert_to_constant(offset)]
        )

    @expose_as_static
    def array_contains(
        self, element: Expression | CONSTANT_TYPE
    ) -> "BooleanExpression":
        """Creates an expression that checks if an array contains a specific element or value.

        Example:
            >>> # Check if the 'sizes' array contains the value from the 'selectedSize' field
            >>> Field.of("sizes").array_contains(Field.of("selectedSize"))
            >>> # Check if the 'colors' array contains "red"
            >>> Field.of("colors").array_contains("red")

        Args:
            element: The element (expression or constant) to search for in the array.

        Returns:
            A new `Expression` representing the 'array_contains' comparison.
        """
        return BooleanExpression(
            "array_contains", [self, self._cast_to_expr_or_convert_to_constant(element)]
        )

    @expose_as_static
    def array_contains_all(
        self,
        elements: Array | list[Expression | CONSTANT_TYPE] | Expression,
    ) -> "BooleanExpression":
        """Creates an expression that checks if an array contains all the specified elements.

        Example:
            >>> # Check if the 'tags' array contains both "news" and "sports"
            >>> Field.of("tags").array_contains_all(["news", "sports"])
            >>> # Check if the 'tags' array contains both of the values from field 'tag1' and "tag2"
            >>> Field.of("tags").array_contains_all([Field.of("tag1"), "tag2"])

        Args:
            elements: The list of elements (expressions or constants) to check for in the array.

        Returns:
            A new `Expression` representing the 'array_contains_all' comparison.
        """
        return BooleanExpression(
            "array_contains_all",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(elements),
            ],
        )

    @expose_as_static
    def array_contains_any(
        self,
        elements: Array | list[Expression | CONSTANT_TYPE] | Expression,
    ) -> "BooleanExpression":
        """Creates an expression that checks if an array contains any of the specified elements.

        Example:
            >>> # Check if the 'categories' array contains either values from field "cate1" or "cate2"
            >>> Field.of("categories").array_contains_any([Field.of("cate1"), Field.of("cate2")])
            >>> # Check if the 'groups' array contains either the value from the 'userGroup' field
            >>> # or the value "guest"
            >>> Field.of("groups").array_contains_any([Field.of("userGroup"), "guest"])

        Args:
            elements: The list of elements (expressions or constants) to check for in the array.

        Returns:
            A new `Expression` representing the 'array_contains_any' comparison.
        """
        return BooleanExpression(
            "array_contains_any",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(elements),
            ],
        )

    @expose_as_static
    def array_length(self) -> "Expression":
        """Creates an expression that calculates the length of an array.

        Example:
            >>> # Get the number of items in the 'cart' array
            >>> Field.of("cart").array_length()

        Returns:
            A new `Expression` representing the length of the array.
        """
        return FunctionExpression("array_length", [self])

    @expose_as_static
    def array_reverse(self) -> "Expression":
        """Creates an expression that returns the reversed content of an array.

        Example:
            >>> # Get the 'preferences' array in reversed order.
            >>> Field.of("preferences").array_reverse()

        Returns:
            A new `Expression` representing the reversed array.
        """
        return FunctionExpression("array_reverse", [self])

    @expose_as_static
    def array_filter(
        self,
        filter_expr: "BooleanExpression",
        element_alias: str | Constant[str],
    ) -> "Expression":
        """Filters an array based on a predicate.

        Example:
            >>> # Filter the 'tags' array to only include the tag "comedy"
            >>> Field.of("tags").array_filter(Variable("tag").equal("comedy"), "tag")

        Args:
            filter_expr: The predicate boolean expression used to filter the elements.
            element_alias: A string or string constant used to refer to the current array
                element as a variable within the filter expression.


        Returns:
            A new `Expression` representing the filtered array.
        """
        args = [self, self._cast_to_expr_or_convert_to_constant(element_alias)]
        args.append(filter_expr)

        repr_func = (
            lambda expr: f"{expr.params[0]!r}.{expr.name}({expr.params[2]!r}, {expr.params[1]!r})"
        )
        return FunctionExpression("array_filter", args, repr_function=repr_func)

    @expose_as_static
    def array_transform(
        self,
        transform_expr: "Expression",
        element_alias: str | Constant[str],
        index_alias: str | Constant[str] | None = None,
    ) -> "Expression":
        """Creates an expression that applies a provided transformation to each element in an array.

        Example:
            >>> # Convert each tag in the 'tags' array to uppercase
            >>> Field.of("tags").array_transform(Variable("tag").to_upper(), "tag")
            >>> # Append the index to each tag in the 'tags' array
            >>> Field.of("tags").array_transform(
            ...     Variable("tag").string_concat(Variable("i")),
            ...     element_alias="tag", index_alias="i"
            ... )

        Args:
            transform_expr: The expression used to transform the elements.
            element_alias: A string or string constant used to refer to the current array
                element as a variable within the transform expression.
            index_alias: An optional string or string constant used to refer to the index
                of the current array element as a variable within the transform expression.

        Returns:
            A new `Expression` representing the transformed array.
        """
        args = [self, self._cast_to_expr_or_convert_to_constant(element_alias)]
        if index_alias is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(index_alias))
        args.append(transform_expr)

        repr_func = (
            lambda expr: f"{expr.params[0]!r}.{expr.name}({expr.params[-1]!r}, {expr.params[1]!r}{', ' + repr(expr.params[2]) if len(expr.params) == 4 else ''})"
        )
        return FunctionExpression("array_transform", args, repr_function=repr_func)

    @expose_as_static
    def array_concat(
        self, *other_arrays: Array | list[Expression | CONSTANT_TYPE] | Expression
    ) -> "Expression":
        """Creates an expression that concatenates an array expression with another array.

        Example:
            >>> # Combine the 'tags' array with a new array and an array field
            >>> Field.of("tags").array_concat(["newTag1", "newTag2", Field.of("otherTag")])

        Args:
            array: The list of constants or expressions to concat with.

        Returns:
            A new `Expression` representing the concatenated array.
        """
        return FunctionExpression(
            "array_concat",
            [self]
            + [self._cast_to_expr_or_convert_to_constant(arr) for arr in other_arrays],
        )

    @expose_as_static
    def concat(self, *others: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that concatenates expressions together

        Args:
            *others: The expressions to concatenate.

        Returns:
            A new `Expression` representing the concatenated value.
        """
        return FunctionExpression(
            "concat",
            [self] + [self._cast_to_expr_or_convert_to_constant(o) for o in others],
        )

    @expose_as_static
    def length(self) -> "Expression":
        """
        Creates an expression that calculates the length of the expression if it is a string, array, map, or blob.

        Example:
            >>> # Get the length of the 'name' field.
            >>> Field.of("name").length()

        Returns:
            A new `Expression` representing the length of the expression.
        """
        return FunctionExpression("length", [self])

    @expose_as_static
    def is_absent(self) -> "BooleanExpression":
        """Creates an expression that returns true if a value is absent. Otherwise, returns false even if
        the value is null.

        Example:
            >>> # Check if the 'email' field is absent.
            >>> Field.of("email").is_absent()

        Returns:
            A new `BooleanExpression` representing the isAbsent operation.
        """
        return BooleanExpression("is_absent", [self])

    @expose_as_static
    def if_absent(self, default_value: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns a default value if an expression evaluates to an absent value.

        Example:
            >>> # Return the value of the 'email' field, or "N/A" if it's absent.
            >>> Field.of("email").if_absent("N/A")

        Args:
            default_value: The expression or constant value to return if this expression is absent.

        Returns:
            A new `Expression` representing the ifAbsent operation.
        """
        return FunctionExpression(
            "if_absent",
            [self, self._cast_to_expr_or_convert_to_constant(default_value)],
        )

    @expose_as_static
    def is_error(self):
        """Creates an expression that checks if a given expression produces an error

        Example:
            >>> # Resolves to True if an expression produces an error
            >>> Field.of("value").divide("string").is_error()

        Returns:
            A new `Expression` representing the isError operation.
        """
        return FunctionExpression("is_error", [self])

    @expose_as_static
    def if_error(self, then_value: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns ``then_value`` if this expression evaluates to an error.
        Otherwise, returns the value of this expression.

        Example:
            >>> # Resolves to 0 if an expression produces an error
            >>> Field.of("value").divide("string").if_error(0)

        Args:
            then_value: The value to return if this expression evaluates to an error.

        Returns:
            A new `Expression` representing the ifError operation.
        """
        return FunctionExpression(
            "if_error", [self, self._cast_to_expr_or_convert_to_constant(then_value)]
        )

    @expose_as_static
    def exists(self) -> "BooleanExpression":
        """Creates an expression that checks if a field exists in the document.

        Example:
            >>> # Check if the document has a field named "phoneNumber"
            >>> Field.of("phoneNumber").exists()

        Returns:
            A new `Expression` representing the 'exists' check.
        """
        return BooleanExpression("exists", [self])

    @expose_as_static
    def coalesce(self, *others: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that evaluates to the first non-null/non-missing value.

        Example:
            >>> # Return the "preferredName" field if it exists.
            >>> # Otherwise, check the "fullName" field.
            >>> # Otherwise, return the literal string "Anonymous".
            >>> Field.of("preferredName").coalesce(Field.of("fullName"), "Anonymous")

            >>> # Equivalent static call:
            >>> Expression.coalesce(Field.of("preferredName"), Field.of("fullName"), "Anonymous")

        Args:
            *others: Additional expressions or constants to evaluate if the current
                expression evaluates to null or is missing.

        Returns:
            An Expression representing the coalesce operation.
        """
        return FunctionExpression(
            "coalesce",
            [self]
            + [Expression._cast_to_expr_or_convert_to_constant(x) for x in others],
        )

    @expose_as_static
    def switch_on(
        self, result: Expression | CONSTANT_TYPE, *others: Expression | CONSTANT_TYPE
    ) -> "Expression":
        """Creates an expression that evaluates to the result corresponding to the first true condition.

        This function behaves like a `switch` statement. It accepts an alternating sequence of
        conditions and their corresponding results. If an odd number of arguments is provided, the
        final argument serves as a default fallback result. If no default is provided and no condition
        evaluates to true, it throws an error.

        Example:
            >>> # Return "Pending" if status is 1, "Active" if status is 2, otherwise "Unknown"
            >>> Field.of("status").equal(1).switch_on(
            ...     "Pending", Field.of("status").equal(2), "Active", "Unknown"
            ... )

        Args:
            result: The result to return if this condition is true.
            *others: Additional alternating conditions and results, optionally followed by a default value.

        Returns:
            An Expression representing the "switch_on" operation.
        """
        return FunctionExpression(
            "switch_on",
            [self, Expression._cast_to_expr_or_convert_to_constant(result)]
            + [Expression._cast_to_expr_or_convert_to_constant(x) for x in others],
        )

    @expose_as_static
    def storage_size(self) -> "Expression":
        """Calculates the Firestore storage size of a given value.

        Mirrors the sizing rules detailed in Firebase/Firestore documentation.

        Example:
            >>> Field.of("content").storage_size()

        Returns:
            A new `Expression` representing the storage size.
        """
        return FunctionExpression("storage_size", [self])

    @expose_as_static
    def sum(self) -> "Expression":
        """Creates an aggregation that calculates the sum of a numeric field across multiple stage inputs.

        Example:
            >>> # Calculate the total revenue from a set of orders
            >>> Field.of("orderAmount").sum().as_("totalRevenue")

        Returns:
            A new `AggregateFunction` representing the 'sum' aggregation.
        """
        return AggregateFunction("sum", [self])

    @expose_as_static
    def average(self) -> "Expression":
        """Creates an aggregation that calculates the average (mean) of a numeric field across multiple
        stage inputs.

        Example:
            >>> # Calculate the average age of users
            >>> Field.of("age").average().as_("averageAge")

        Returns:
            A new `AggregateFunction` representing the 'avg' aggregation.
        """
        return AggregateFunction("average", [self])

    @expose_as_static
    def count(self) -> "Expression":
        """Creates an aggregation that counts the number of stage inputs with valid evaluations of the
        expression or field.

        Example:
            >>> # Count the total number of products
            >>> Field.of("productId").count().as_("totalProducts")

        Returns:
            A new `AggregateFunction` representing the 'count' aggregation.
        """
        return AggregateFunction("count", [self])

    @expose_as_static
    def count_if(self) -> "Expression":
        """Creates an aggregation that counts the number of values of the provided field or expression
        that evaluate to True.

        Example:
            >>> # Count the number of adults
            >>> Field.of("age").greater_than(18).count_if().as_("totalAdults")


        Returns:
            A new `AggregateFunction` representing the 'count_if' aggregation.
        """
        return AggregateFunction("count_if", [self])

    @expose_as_static
    def count_distinct(self) -> "Expression":
        """Creates an aggregation that counts the number of distinct values of the
        provided field or expression.

        Example:
            >>> # Count the total number of countries in the data
            >>> Field.of("country").count_distinct().as_("totalCountries")

        Returns:
            A new `AggregateFunction` representing the 'count_distinct' aggregation.
        """
        return AggregateFunction("count_distinct", [self])

    @expose_as_static
    def minimum(self) -> "Expression":
        """Creates an aggregation that finds the minimum value of a field across multiple stage inputs.

        Example:
            >>> # Find the lowest price of all products
            >>> Field.of("price").minimum().as_("lowestPrice")

        Returns:
            A new `AggregateFunction` representing the 'minimum' aggregation.
        """
        return AggregateFunction("minimum", [self])

    @expose_as_static
    def maximum(self) -> "Expression":
        """Creates an aggregation that finds the maximum value of a field across multiple stage inputs.

        Example:
            >>> # Find the highest score in a leaderboard
            >>> Field.of("score").maximum().as_("highestScore")

        Returns:
            A new `AggregateFunction` representing the 'maximum' aggregation.
        """
        return AggregateFunction("maximum", [self])

    @expose_as_static
    def char_length(self) -> "Expression":
        """Creates an expression that calculates the character length of a string.

        Example:
            >>> # Get the character length of the 'name' field
            >>> Field.of("name").char_length()

        Returns:
            A new `Expression` representing the length of the string.
        """
        return FunctionExpression("char_length", [self])

    @expose_as_static
    def byte_length(self) -> "Expression":
        """Creates an expression that calculates the byte length of a string in its UTF-8 form.

        Example:
            >>> # Get the byte length of the 'name' field
            >>> Field.of("name").byte_length()

        Returns:
            A new `Expression` representing the byte length of the string.
        """
        return FunctionExpression("byte_length", [self])

    @expose_as_static
    def like(self, pattern: Expression | str) -> "BooleanExpression":
        """Creates an expression that performs a case-sensitive string comparison.

        Example:
            >>> # Check if the 'title' field contains the word "guide" (case-sensitive)
            >>> Field.of("title").like("%guide%")
            >>> # Check if the 'title' field matches the pattern specified in field 'pattern'.
            >>> Field.of("title").like(Field.of("pattern"))

        Args:
            pattern: The pattern (string or expression) to search for. You can use "%" as a wildcard character.

        Returns:
            A new `Expression` representing the 'like' comparison.
        """
        return BooleanExpression(
            "like", [self, self._cast_to_expr_or_convert_to_constant(pattern)]
        )

    @expose_as_static
    def regex_contains(self, regex: Expression | str) -> "BooleanExpression":
        """Creates an expression that checks if a string contains a specified regular expression as a
        substring.

        Example:
            >>> # Check if the 'description' field contains "example" (case-insensitive)
            >>> Field.of("description").regex_contains("(?i)example")
            >>> # Check if the 'description' field contains the regular expression stored in field 'regex'
            >>> Field.of("description").regex_contains(Field.of("regex"))

        Args:
            regex: The regular expression (string or expression) to use for the search.

        Returns:
            A new `Expression` representing the 'contains' comparison.
        """
        return BooleanExpression(
            "regex_contains", [self, self._cast_to_expr_or_convert_to_constant(regex)]
        )

    @expose_as_static
    def regex_match(self, regex: Expression | str) -> "BooleanExpression":
        """Creates an expression that checks if a string matches a specified regular expression.

        Example:
            >>> # Check if the 'email' field matches a valid email pattern
            >>> Field.of("email").regex_match("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
            >>> # Check if the 'email' field matches a regular expression stored in field 'regex'
            >>> Field.of("email").regex_match(Field.of("regex"))

        Args:
            regex: The regular expression (string or expression) to use for the match.

        Returns:
            A new `Expression` representing the regular expression match.
        """
        return BooleanExpression(
            "regex_match", [self, self._cast_to_expr_or_convert_to_constant(regex)]
        )

    @expose_as_static
    def string_contains(self, substring: Expression | str) -> "BooleanExpression":
        """Creates an expression that checks if this string expression contains a specified substring.

        Example:
            >>> # Check if the 'description' field contains "example".
            >>> Field.of("description").string_contains("example")
            >>> # Check if the 'description' field contains the value of the 'keyword' field.
            >>> Field.of("description").string_contains(Field.of("keyword"))

        Args:
            substring: The substring (string or expression) to use for the search.

        Returns:
            A new `Expression` representing the 'contains' comparison.
        """
        return BooleanExpression(
            "string_contains",
            [self, self._cast_to_expr_or_convert_to_constant(substring)],
        )

    @expose_as_static
    def starts_with(self, prefix: Expression | str) -> "BooleanExpression":
        """Creates an expression that checks if a string starts with a given prefix.

        Example:
            >>> # Check if the 'name' field starts with "Mr."
            >>> Field.of("name").starts_with("Mr.")
            >>> # Check if the 'fullName' field starts with the value of the 'firstName' field
            >>> Field.of("fullName").starts_with(Field.of("firstName"))

        Args:
            prefix: The prefix (string or expression) to check for.

        Returns:
            A new `Expression` representing the 'starts with' comparison.
        """
        return BooleanExpression(
            "starts_with", [self, self._cast_to_expr_or_convert_to_constant(prefix)]
        )

    @expose_as_static
    def ends_with(self, postfix: Expression | str) -> "BooleanExpression":
        """Creates an expression that checks if a string ends with a given postfix.

        Example:
            >>> # Check if the 'filename' field ends with ".txt"
            >>> Field.of("filename").ends_with(".txt")
            >>> # Check if the 'url' field ends with the value of the 'extension' field
            >>> Field.of("url").ends_with(Field.of("extension"))

        Args:
            postfix: The postfix (string or expression) to check for.

        Returns:
            A new `Expression` representing the 'ends with' comparison.
        """
        return BooleanExpression(
            "ends_with", [self, self._cast_to_expr_or_convert_to_constant(postfix)]
        )

    @expose_as_static
    def string_concat(self, *elements: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that concatenates string expressions, fields or constants together.

        Example:
            >>> # Combine the 'firstName', " ", and 'lastName' fields into a single string
            >>> Field.of("firstName").string_concat(" ", Field.of("lastName"))

        Args:
            *elements: The expressions or constants (typically strings) to concatenate.

        Returns:
            A new `Expression` representing the concatenated string.
        """
        return FunctionExpression(
            "string_concat",
            [self] + [self._cast_to_expr_or_convert_to_constant(el) for el in elements],
        )

    @expose_as_static
    def to_lower(self) -> "Expression":
        """Creates an expression that converts a string to lowercase.

        Example:
            >>> # Convert the 'name' field to lowercase
            >>> Field.of("name").to_lower()

        Returns:
            A new `Expression` representing the lowercase string.
        """
        return FunctionExpression("to_lower", [self])

    @expose_as_static
    def to_upper(self) -> "Expression":
        """Creates an expression that converts a string to uppercase.

        Example:
            >>> # Convert the 'title' field to uppercase
            >>> Field.of("title").to_upper()

        Returns:
            A new `Expression` representing the uppercase string.
        """
        return FunctionExpression("to_upper", [self])

    @expose_as_static
    def trim(self) -> "Expression":
        """Creates an expression that removes leading and trailing whitespace from a string.

        Example:
            >>> # Trim whitespace from the 'userInput' field
            >>> Field.of("userInput").trim()

        Returns:
            A new `Expression` representing the trimmed string.
        """
        return FunctionExpression("trim", [self])

    @expose_as_static
    def string_reverse(self) -> "Expression":
        """Creates an expression that reverses a string.

        Example:
            >>> # Reverse the 'userInput' field
            >>> Field.of("userInput").reverse()

        Returns:
            A new `Expression` representing the reversed string.
        """
        return FunctionExpression("string_reverse", [self])

    @expose_as_static
    def substring(
        self, position: Expression | int, length: Expression | int | None = None
    ) -> "Expression":
        """Creates an expression that returns a substring of the results of this expression.


        Example:
            >>> Field.of("description").substring(5, 10)
            >>> Field.of("description").substring(5)

        Args:
            position: the index of the first character of the substring.
            length: the length of the substring. If not provided the substring
                will end at the end of the input.

        Returns:
            A new `Expression` representing the extracted substring.
        """
        args = [self, self._cast_to_expr_or_convert_to_constant(position)]
        if length is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(length))
        return FunctionExpression("substring", args)

    @expose_as_static
    def join(self, delimeter: Expression | str) -> "Expression":
        """Creates an expression that joins the elements of an array into a string


        Example:
            >>> Field.of("tags").join(", ")

        Args:
            delimiter: The delimiter to add between the elements of the array.

        Returns:
            A new `Expression` representing the joined string.
        """
        return FunctionExpression(
            "join", [self, self._cast_to_expr_or_convert_to_constant(delimeter)]
        )

    @expose_as_static
    def map_get(self, key: str | Constant[str]) -> "Expression":
        """Accesses a value from the map produced by evaluating this expression.
        If the expression is evaluated against a non-map type, it evaluates to an error.

        Example:
            >>> Map({"city": "London"}).map_get("city")
            >>> Field.of("address").map_get("city")

        Args:
            key: The key to access in the map.

        Returns:
            A new `Expression` representing the value associated with the given key in the map.
        """
        return FunctionExpression(
            "map_get", [self, self._cast_to_expr_or_convert_to_constant(key)]
        )

    def map_set(self, key: str | Constant[str], value: Any) -> "Expression":
        """Creates an expression that returns a new map with the specified entries added or
        updated.

        Note:
            `map_set` only performs shallow updates to the map. Setting a value to `None`
            will retain the key with a `None` value. To remove a key entirely, use
            `map_remove`.

        Example:
            >>> Map({"city": "London"}).map_set("city", "New York")
            >>> Field.of("address").map_set("city", "Seattle")

        Args:
            key: The key to set in the map.
            value: The value to associate with the key.

        Returns:
            A new `Expression` representing the map_set operation.
        """
        args = [
            self,
            self._cast_to_expr_or_convert_to_constant(key),
            self._cast_to_expr_or_convert_to_constant(value),
        ]
        return FunctionExpression("map_set", args)

    @expose_as_static
    def map_remove(self, key: str | Constant[str]) -> "Expression":
        """Remove a key from a the map produced by evaluating this expression.

        Example:
            >>> Map({"city": "London"}).map_remove("city")
            >>> Field.of("address").map_remove("city")

        Args:
            key: The key to remove in the map.

        Returns:
            A new `Expression` representing the map_remove operation.
        """
        return FunctionExpression(
            "map_remove", [self, self._cast_to_expr_or_convert_to_constant(key)]
        )

    @expose_as_static
    def map_merge(
        self,
        *other_maps: Map
        | dict[str | Constant[str], Expression | CONSTANT_TYPE]
        | Expression,
    ) -> "Expression":
        """Creates an expression that merges one or more dicts into a single map.

        Example:
            >>> Map({"city": "London"}).map_merge({"country": "UK"}, {"isCapital": True})
            >>> Field.of("settings").map_merge({"enabled":True}, FunctionExpression.conditional(Field.of('isAdmin'), {"admin":True}, {}})

        Args:
            *other_maps: Sequence of maps to merge into the resulting map.

        Returns:
            A new `Expression` representing the value associated with the given key in the map.
        """
        return FunctionExpression(
            "map_merge",
            [self] + [self._cast_to_expr_or_convert_to_constant(m) for m in other_maps],
        )

    @expose_as_static
    def map_keys(self) -> "Expression":
        """Creates an expression that returns the keys of a map.

        Note:
            While the backend generally preserves insertion order, relying on the
            order of the output array is not guaranteed and should be avoided.

        Example:
            >>> Map({"city": "London", "country": "UK"}).map_keys()
            >>> Field.of("address").map_keys()

        Returns:
            A new `Expression` representing the keys of the map.
        """
        return FunctionExpression("map_keys", [self])

    @expose_as_static
    def map_values(self) -> "Expression":
        """Creates an expression that returns the values of a map.

        Note:
            While the backend generally preserves insertion order, relying on the
            order of the output array is not guaranteed and should be avoided.

        Example:
            >>> Map({"city": "London", "country": "UK"}).map_values()
            >>> Field.of("address").map_values()

        Returns:
            A new `Expression` representing the values of the map.
        """
        return FunctionExpression("map_values", [self])

    @expose_as_static
    def map_entries(self) -> "Expression":
        """Creates an expression that returns the entries of a map as an array of maps,
        where each map contains a `"k"` property for the key and a `"v"` property for the value.
        For example: `[{ "k": "key1", "v": "value1" }, ...]`.

        Note:
            While the backend generally preserves insertion order, relying on the
            order of the output array is not guaranteed and should be avoided.

        Example:
            >>> Map({"city": "London", "country": "UK"}).map_entries()
            >>> Field.of("address").map_entries()

        Returns:
            A new `Expression` representing the entries of the map.
        """
        return FunctionExpression("map_entries", [self])

    def regex_find(self, pattern: str | Constant[str] | Expression) -> "Expression":
        """Creates an expression that returns the first substring of a string expression that
        matches a specified regular expression.

        This expression uses the RE2 regular expression syntax. See https://github.com/google/re2/wiki/Syntax.

        Example:
            >>> Field.of("email").regex_find("@[A-Za-z0-9.-]+")
            >>> Field.of("email").regex_find(Field.of("pattern"))

        Args:
            pattern: The regular expression to search for.

        Returns:
            A new `Expression` representing the regular expression find function.
        """
        return FunctionExpression(
            "regex_find", [self, self._cast_to_expr_or_convert_to_constant(pattern)]
        )

    @expose_as_static
    def regex_find_all(self, pattern: str | Constant[str] | Expression) -> "Expression":
        """Creates an expression that evaluates to an array of all substrings in a string expression
        that match a specified regular expression.

        This expression uses the RE2 regular expression syntax. See https://github.com/google/re2/wiki/Syntax.

        Example:
            >>> Field.of("comment").regex_find_all("@[A-Za-z0-9_]+")
            >>> Field.of("comment").regex_find_all(Field.of("pattern"))

        Args:
            pattern: The regular expression to search for.

        Returns:
            A new `Expression` representing the regular expression find function.
        """
        return FunctionExpression(
            "regex_find_all", [self, self._cast_to_expr_or_convert_to_constant(pattern)]
        )

    @expose_as_static
    def split(self, delimiter: str | Constant[str] | Expression) -> "Expression":
        """Creates an expression that splits the value of a field on the provided delimiter.

        Example:
            >>> Field.of("date").split("date", "-")

        Args:
            field_name: Split the value in this field.
            delimiter: The delimiter string to split on.

        Returns:
            A new `Expression` representing the split function.
        """
        return FunctionExpression(
            "split", [self, self._cast_to_expr_or_convert_to_constant(delimiter)]
        )

    @expose_as_static
    def string_repeat(self, repetitions: int | Expression) -> "Expression":
        """Creates an expression that repeats a string or byte array a specified number
        of times.

        Example:
            >>> # Called on an existing field expression:
            >>> Field.of("name").string_repeat(3)
            >>> # Called statically using the field name:
            >>> Expression.string_repeat("name", 3)

        Args:
            repetitions: The number of times to repeat the string or byte array.

        Returns:
            A new `Expression` representing the repeated string or byte array.
        """
        return FunctionExpression(
            "string_repeat",
            [self, self._cast_to_expr_or_convert_to_constant(repetitions)],
        )

    @expose_as_static
    def string_replace_all(
        self,
        find: str | bytes | Constant[str] | Constant[bytes] | Expression,
        replacement: str | bytes | Constant[str] | Constant[bytes] | Expression,
    ) -> "Expression":
        """Creates an expression that replaces all occurrences of a substring or byte
        sequence with a replacement.

        Example:
            >>> # Called on an existing field expression:
            >>> Field.of("text").string_replace_all("foo", "bar")

        Args:
            find: The substring or byte sequence to search for.
            replacement: The replacement string or byte sequence.

        Returns:
            A new `Expression` representing the string or byte array with replacements.
        """
        return FunctionExpression(
            "string_replace_all",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(find),
                self._cast_to_expr_or_convert_to_constant(replacement),
            ],
        )

    @expose_as_static
    def string_replace_one(
        self,
        find: str | bytes | Constant[str] | Constant[bytes] | Expression,
        replacement: str | bytes | Constant[str] | Constant[bytes] | Expression,
    ) -> "Expression":
        """Creates an expression that replaces the first occurrence of a substring or byte
        sequence with a replacement.

        Example:
            >>> # Called on an existing field expression:
            >>> Field.of("text").string_replace_one("foo", "bar")

        Args:
            find: The substring or byte sequence to search for.
            replacement: The replacement string or byte sequence.

        Returns:
            A new `Expression` representing the string or byte array with the replacement.
        """
        return FunctionExpression(
            "string_replace_one",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(find),
                self._cast_to_expr_or_convert_to_constant(replacement),
            ],
        )

    @expose_as_static
    def string_index_of(
        self,
        search: str | bytes | Constant[str] | Constant[bytes] | Expression,
    ) -> "Expression":
        """Creates an expression that finds the index of the first occurrence of a substring or
        byte sequence.

        Example:
            >>> # Called on an existing field expression:
            >>> Field.of("text").string_index_of("foo")

        Args:
            search: The substring or byte sequence to search for.

        Returns:
            A new `Expression` representing the index of the first occurrence.
        """
        return FunctionExpression(
            "string_index_of",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(search),
            ],
        )

    @expose_as_static
    def ltrim(
        self,
        chars: str | bytes | Constant[str] | Constant[bytes] | Expression | None = None,
    ) -> "Expression":
        """Creates an expression that trims leading whitespace or a specified sequence
        of characters/bytes from a string or byte sequence.

        Example:
            >>> # Called on an existing field expression:
            >>> Field.of("text").ltrim()
            >>> Field.of("text").ltrim(" ")

        Args:
            chars: The substring or byte sequence to trim. If not provided,
                whitespace will be trimmed.

        Returns:
            A new `Expression` representing the trimmed value.
        """
        args = [self]
        if chars is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(chars))

        return FunctionExpression("ltrim", args)

    @expose_as_static
    def rtrim(
        self,
        chars: str | bytes | Constant[str] | Constant[bytes] | Expression | None = None,
    ) -> "Expression":
        """Creates an expression that trims trailing whitespace or a specified sequence
        of characters/bytes from a string or byte sequence.

        Example:
            >>> # Called on an existing field expression:
            >>> Field.of("text").rtrim()
            >>> Field.of("text").rtrim(" ")

        Args:
            chars: The substring or byte sequence to trim. If not provided,
                whitespace will be trimmed.

        Returns:
            A new `Expression` representing the trimmed value.
        """
        args = [self]
        if chars is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(chars))

        return FunctionExpression("rtrim", args)

    @expose_as_static
    def cosine_distance(self, other: Expression | list[float] | Vector) -> "Expression":
        """Calculates the cosine distance between two vectors.

        Example:
            >>> # Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
            >>> Field.of("userVector").cosine_distance(Field.of("itemVector"))
            >>> # Calculate the Cosine distance between the 'location' field and a target location
            >>> Field.of("location").cosine_distance([37.7749, -122.4194])

        Args:
            other: The other vector (represented as an Expression, list of floats, or Vector) to compare against.

        Returns:
            A new `Expression` representing the cosine distance between the two vectors.
        """
        return FunctionExpression(
            "cosine_distance",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(other, include_vector=True),
            ],
        )

    @expose_as_static
    def euclidean_distance(
        self, other: Expression | list[float] | Vector
    ) -> "Expression":
        """Calculates the Euclidean distance between two vectors.

        Example:
            >>> # Calculate the Euclidean distance between the 'location' field and a target location
            >>> Field.of("location").euclidean_distance([37.7749, -122.4194])
            >>> # Calculate the Euclidean distance between two vector fields: 'pointA' and 'pointB'
            >>> Field.of("pointA").euclidean_distance(Field.of("pointB"))

        Args:
            other: The other vector (represented as an Expression, list of floats, or Vector) to compare against.

        Returns:
            A new `Expression` representing the Euclidean distance between the two vectors.
        """
        return FunctionExpression(
            "euclidean_distance",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(other, include_vector=True),
            ],
        )

    @expose_as_static
    def dot_product(self, other: Expression | list[float] | Vector) -> "Expression":
        """Calculates the dot product between two vectors.

        Example:
            >>> # Calculate the dot product between a feature vector and a target vector
            >>> Field.of("features").dot_product([0.5, 0.8, 0.2])
            >>> # Calculate the dot product between two document vectors: 'docVector1' and 'docVector2'
            >>> Field.of("docVector1").dot_product(Field.of("docVector2"))

        Args:
            other: The other vector (represented as an Expression, list of floats, or Vector) to calculate dot product with.

        Returns:
            A new `Expression` representing the dot product between the two vectors.
        """
        return FunctionExpression(
            "dot_product",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(other, include_vector=True),
            ],
        )

    @expose_as_static
    def vector_length(self) -> "Expression":
        """Creates an expression that calculates the length (dimension) of a Firestore Vector.

        Example:
            >>> # Get the vector length (dimension) of the field 'embedding'.
            >>> Field.of("embedding").vector_length()

        Returns:
            A new `Expression` representing the length of the vector.
        """
        return FunctionExpression("vector_length", [self])

    @expose_as_static
    def timestamp_to_unix_micros(self) -> "Expression":
        """Creates an expression that converts a timestamp to the number of microseconds since the epoch
        (1970-01-01 00:00:00 UTC).

        Truncates higher levels of precision by rounding down to the beginning of the microsecond.

        Example:
            >>> # Convert the 'timestamp' field to microseconds since the epoch.
            >>> Field.of("timestamp").timestamp_to_unix_micros()

        Returns:
            A new `Expression` representing the number of microseconds since the epoch.
        """
        return FunctionExpression("timestamp_to_unix_micros", [self])

    @expose_as_static
    def array_agg(self) -> "Expression":
        """Creates an aggregation that collects all values of an expression
        across multiple stage inputs into an array.

        If the expression resolves to an absent value, it is converted to
        `None`. The order of elements in the output array is not stable and
        shouldn't be relied upon.

        Example:
            >>> # Collect all values of field 'color' into an array
            >>> Field.of("color").array_agg()

        Returns:
            A new `AggregateFunction` representing the array aggregation.
        """
        return AggregateFunction("array_agg", [self])

    @expose_as_static
    def array_agg_distinct(self) -> "Expression":
        """Creates an aggregation that collects all distinct values of an
        expression across multiple stage inputs into an array.

        If the expression resolves to an absent value, it is converted to
        `None`. The order of elements in the output array is not stable and
        shouldn't be relied upon.

        Example:
            >>> # Collect distinct values of field 'color' into an array
            >>> Field.of("color").array_agg_distinct()

        Returns:
            A new `AggregateFunction` representing the distinct array aggregation.
        """
        return AggregateFunction("array_agg_distinct", [self])

    @expose_as_static
    def first(self) -> "Expression":
        """Creates an aggregation that finds the first value of an expression
        across multiple stage inputs.

        Example:
            >>> # Select the first value of field 'color'
            >>> Field.of("color").first()

        Returns:
            A new `AggregateFunction` representing the first aggregation.
        """
        return AggregateFunction("first", [self])

    @expose_as_static
    def last(self) -> "Expression":
        """Creates an aggregation that finds the last value of an expression
        across multiple stage inputs.

        Example:
            >>> # Select the last value of field 'color'
            >>> Field.of("color").last()

        Returns:
            A new `AggregateFunction` representing the last aggregation.
        """
        return AggregateFunction("last", [self])

    @expose_as_static
    def array_first(self) -> "Expression":
        """Creates an expression that returns the first element of an array.

        Example:
            >>> # Select the first element of array 'colors'
            >>> Field.of("colors").array_first()

        Returns:
            A new `Expression` representing the first element of the array.
        """
        return FunctionExpression("array_first", [self])

    @expose_as_static
    def array_last(self) -> "Expression":
        """Creates an expression that returns the last element of an array.

        Example:
            >>> # Select the last element of array 'colors'
            >>> Field.of("colors").array_last()

        Returns:
            A new `Expression` representing the last element of the array.
        """
        return FunctionExpression("array_last", [self])

    @expose_as_static
    def array_first_n(self, n: int | "Expression") -> "Expression":
        """Creates an expression that returns the first `n` elements of an array.

        Example:
            >>> # Select the first 2 elements of array 'colors'
            >>> Field.of("colors").array_first_n(2)

        Returns:
            A new `Expression` representing the first `n` elements of the array.
        """
        return FunctionExpression(
            "array_first_n", [self, self._cast_to_expr_or_convert_to_constant(n)]
        )

    @expose_as_static
    def array_last_n(self, n: int | "Expression") -> "Expression":
        """Creates an expression that returns the last `n` elements of an array.

        Example:
            >>> # Select the last 2 elements of array 'colors'
            >>> Field.of("colors").array_last_n(2)

        Returns:
            A new `Expression` representing the last `n` elements of the array.
        """
        return FunctionExpression(
            "array_last_n", [self, self._cast_to_expr_or_convert_to_constant(n)]
        )

    @expose_as_static
    def array_maximum(self) -> "Expression":
        """Creates an expression that returns the maximum element of an array.

        Example:
            >>> # Select the maximum element of array 'scores'
            >>> Field.of("scores").array_maximum()

        Returns:
            A new `Expression` representing the maximum element of the array.
        """
        return FunctionExpression(
            "maximum",
            [self],
            repr_function=FunctionExpression._build_infix_repr("array_maximum"),
        )

    @expose_as_static
    def array_minimum(self) -> "Expression":
        """Creates an expression that returns the minimum element of an array.

        Example:
            >>> # Select the minimum element of array 'scores'
            >>> Field.of("scores").array_minimum()

        Returns:
            A new `Expression` representing the minimum element of the array.
        """
        return FunctionExpression(
            "minimum",
            [self],
            repr_function=FunctionExpression._build_infix_repr("array_minimum"),
        )

    @expose_as_static
    def array_maximum_n(self, n: int | "Expression") -> "Expression":
        """Creates an expression that returns the maximum `n` elements of an array.

        Example:
            >>> # Select the maximum 2 elements of array 'scores'
            >>> Field.of("scores").array_maximum_n(2)

        Note:
            Returns the n largest non-null elements in the array, in descending
            order. This does not use a stable sort, meaning the order of equivalent
            elements is undefined.

        Returns:
            A new `Expression` representing the maximum `n` elements of the array.
        """
        return FunctionExpression(
            "maximum_n",
            [self, self._cast_to_expr_or_convert_to_constant(n)],
            repr_function=FunctionExpression._build_infix_repr("array_maximum_n"),
        )

    @expose_as_static
    def array_minimum_n(self, n: int | "Expression") -> "Expression":
        """Creates an expression that returns the minimum `n` elements of an array.

        Example:
            >>> # Select the minimum 2 elements of array 'scores'
            >>> Field.of("scores").array_minimum_n(2)

        Note:
            Returns the n smallest non-null elements in the array, in ascending
            order. This does not use a stable sort, meaning the order of equivalent
            elements is undefined.

        Returns:
            A new `Expression` representing the minimum `n` elements of the array.
        """
        return FunctionExpression(
            "minimum_n",
            [self, self._cast_to_expr_or_convert_to_constant(n)],
            repr_function=FunctionExpression._build_infix_repr("array_minimum_n"),
        )

    @expose_as_static
    def array_slice(
        self, offset: int | "Expression", length: int | "Expression" | None = None
    ) -> "Expression":
        """Creates an expression that returns a slice of an array starting from the specified
        offset with a given length.

        Example:
            >>> # Slice array 'scores' starting at index 1 with length 2
            >>> Field.of("scores").array_slice(1, 2)

        Args:
            offset: the 0-based index of the first element to include.
            length: The number of elements to include in the slice. If omitted, slices to the end.

        Returns:
            A new `Expression` representing the slice of the array.
        """
        args = [self, self._cast_to_expr_or_convert_to_constant(offset)]
        if length is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(length))
        return FunctionExpression("array_slice", args)

    @expose_as_static
    def array_index_of(self, search: "Expression" | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns the first index of the search value in the array,
        or -1 if not found.

        Example:
            >>> # Get the index of "comedy" in the 'tags' array
            >>> Field.of("tags").array_index_of("comedy")

        Args:
            search: An expression evaluating to the value to search for.

        Returns:
            A new `Expression` representing the index.
        """
        return FunctionExpression(
            "array_index_of",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(search),
                self._cast_to_expr_or_convert_to_constant("first"),
            ],
        )

    @expose_as_static
    def array_index_of_all(self, search: "Expression" | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns all indices of a value in an array.

        Example:
            >>> # Get all indices of "comedy" in the 'tags' array
            >>> Field.of("tags").array_index_of_all("comedy")

        Args:
            search: An expression evaluating to the value to search for.

        Returns:
            A new `Expression` representing the indices.
        """
        return FunctionExpression(
            "array_index_of_all",
            [self, self._cast_to_expr_or_convert_to_constant(search)],
        )

    @expose_as_static
    def unix_micros_to_timestamp(self) -> "Expression":
        """Creates an expression that converts a number of microseconds since the epoch (1970-01-01
        00:00:00 UTC) to a timestamp.

        Example:
            >>> # Convert the 'microseconds' field to a timestamp.
            >>> Field.of("microseconds").unix_micros_to_timestamp()

        Returns:
            A new `Expression` representing the timestamp.
        """
        return FunctionExpression("unix_micros_to_timestamp", [self])

    @expose_as_static
    def timestamp_to_unix_millis(self) -> "Expression":
        """Creates an expression that converts a timestamp to the number of milliseconds since the epoch
        (1970-01-01 00:00:00 UTC).

        Truncates higher levels of precision by rounding down to the beginning of the millisecond.

        Example:
            >>> # Convert the 'timestamp' field to milliseconds since the epoch.
            >>> Field.of("timestamp").timestamp_to_unix_millis()

        Returns:
            A new `Expression` representing the number of milliseconds since the epoch.
        """
        return FunctionExpression("timestamp_to_unix_millis", [self])

    @expose_as_static
    def unix_millis_to_timestamp(self) -> "Expression":
        """Creates an expression that converts a number of milliseconds since the epoch (1970-01-01
        00:00:00 UTC) to a timestamp.

        Example:
            >>> # Convert the 'milliseconds' field to a timestamp.
            >>> Field.of("milliseconds").unix_millis_to_timestamp()

        Returns:
            A new `Expression` representing the timestamp.
        """
        return FunctionExpression("unix_millis_to_timestamp", [self])

    @expose_as_static
    def timestamp_to_unix_seconds(self) -> "Expression":
        """Creates an expression that converts a timestamp to the number of seconds since the epoch
        (1970-01-01 00:00:00 UTC).

        Truncates higher levels of precision by rounding down to the beginning of the second.

        Example:
            >>> # Convert the 'timestamp' field to seconds since the epoch.
            >>> Field.of("timestamp").timestamp_to_unix_seconds()

        Returns:
            A new `Expression` representing the number of seconds since the epoch.
        """
        return FunctionExpression("timestamp_to_unix_seconds", [self])

    @expose_as_static
    def unix_seconds_to_timestamp(self) -> "Expression":
        """Creates an expression that converts a number of seconds since the epoch (1970-01-01 00:00:00
        UTC) to a timestamp.

        Example:
            >>> # Convert the 'seconds' field to a timestamp.
            >>> Field.of("seconds").unix_seconds_to_timestamp()

        Returns:
            A new `Expression` representing the timestamp.
        """
        return FunctionExpression("unix_seconds_to_timestamp", [self])

    @expose_as_static
    def timestamp_add(
        self, unit: TimeUnit | str | Expression, amount: Expression | float
    ) -> "Expression":
        """Creates an expression that adds a specified amount of time to this timestamp expression.

        Example:
            >>> # Add 1.5 days to the 'timestamp' field using TimeUnit enum.
            >>> Field.of("timestamp").timestamp_add(TimeUnit.DAY, 1.5)
            >>> # Add a duration specified by the 'unit' and 'amount' fields to the 'timestamp' field.
            >>> Field.of("timestamp").timestamp_add(Field.of("unit"), Field.of("amount"))
            >>> # Add 1.5 days to the 'timestamp' field using a string.
            >>> Field.of("timestamp").timestamp_add("day", 1.5)

        Args:
            unit: The unit of time to add.
            amount: The amount of time to add.

        Returns:
            A new `Expression` representing the resulting timestamp.
        """
        return FunctionExpression(
            "timestamp_add",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(unit),
                self._cast_to_expr_or_convert_to_constant(amount),
            ],
        )

    @expose_as_static
    def timestamp_subtract(
        self, unit: TimeUnit | str | Expression, amount: Expression | float
    ) -> "Expression":
        """Creates an expression that subtracts a specified amount of time from this timestamp expression.

        Example:
            >>> # Subtract 2.5 hours from the 'timestamp' field using TimeUnit enum.
            >>> Field.of("timestamp").timestamp_subtract(TimeUnit.HOUR, 2.5)
            >>> # Subtract a duration specified by the 'unit' and 'amount' fields from the 'timestamp' field.
            >>> Field.of("timestamp").timestamp_subtract(Field.of("unit"), Field.of("amount"))
            >>> # Subtract 2.5 hours from the 'timestamp' field using a string.
            >>> Field.of("timestamp").timestamp_subtract("hour", 2.5)

        Args:
            unit: The unit of time to subtract.
            amount: The amount of time to subtract.

        Returns:
            A new `Expression` representing the resulting timestamp.
        """
        return FunctionExpression(
            "timestamp_subtract",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(unit),
                self._cast_to_expr_or_convert_to_constant(amount),
            ],
        )

    @expose_as_static
    def collection_id(self):
        """Creates an expression that returns the collection ID from a path.

        Example:
            >>> # Get the collection ID from a path.
            >>> Field.of("__name__").collection_id()

        Returns:
            A new `Expression` representing the collection ID.
        """
        return FunctionExpression("collection_id", [self])

    @expose_as_static
    def document_id(self):
        """Creates an expression that returns the document ID from a path.

        Example:
            >>> # Get the document ID from a path.
            >>> Field.of("__name__").document_id()

        Returns:
            A new `Expression` representing the document ID.
        """
        return FunctionExpression("document_id", [self])

    def ascending(self) -> Ordering:
        """Creates an `Ordering` that sorts documents in ascending order based on this expression.

        Example:
            >>> # Sort documents by the 'name' field in ascending order
            >>> client.pipeline().collection("users").sort(Field.of("name").ascending())

        Returns:
            A new `Ordering` for ascending sorting.
        """
        return Ordering(self, Ordering.Direction.ASCENDING)

    def descending(self) -> Ordering:
        """Creates an `Ordering` that sorts documents in descending order based on this expression.

        Example:
            >>> # Sort documents by the 'createdAt' field in descending order
            >>> client.pipeline().collection("users").sort(Field.of("createdAt").descending())

        Returns:
            A new `Ordering` for descending sorting.
        """
        return Ordering(self, Ordering.Direction.DESCENDING)

    def as_(self, alias: str) -> "AliasedExpression":
        """Assigns an alias to this expression.

        Aliases are useful for renaming fields in the output of a stage or for giving meaningful
        names to calculated values.

        Example:
            >>> # Calculate the total price and assign it the alias "totalPrice" and add it to the output.
            >>> client.pipeline().collection("items").add_fields(
            ...     Field.of("price").multiply(Field.of("quantity")).as_("totalPrice")
            ... )

        Args:
            alias: The alias to assign to this expression.

        Returns:
            A new `Selectable` (typically an `AliasedExpression`) that wraps this
            expression and associates it with the provided alias.
        """
        return AliasedExpression(self, alias)

    @expose_as_static
    def cmp(self, other: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that compares this expression to another expression.

        Returns an integer:
            * -1 if this expression is less than the other
            * 0 if they are equal
            * 1 if this expression is greater than the other

        Example:
            >>> # Compare the 'price' field to 10
            >>> Field.of("price").cmp(10)

        Args:
            other: The value to compare against.

        Returns:
            A new `Expression` representing the comparison operation.
        """
        return FunctionExpression(
            "cmp", [self, self._cast_to_expr_or_convert_to_constant(other)]
        )

    @expose_as_static
    def timestamp_trunc(
        self,
        granularity: TimeGranularity | Expression | str,
        timezone: Expression | str | None = None,
    ) -> "Expression":
        """Creates an expression that truncates a timestamp to a specified granularity.

        Example:
            >>> # Truncate the 'createdAt' field to the day using TimeGranularity enum
            >>> Field.of("createdAt").timestamp_trunc(TimeGranularity.DAY)
            >>> # Truncate the 'createdAt' field to the day in the 'America/Los_Angeles' timezone
            >>> Field.of("createdAt").timestamp_trunc(TimeGranularity.DAY, "America/Los_Angeles")
            >>> # Truncate the 'createdAt' field to the day using a string
            >>> Field.of("createdAt").timestamp_trunc("day")

        Args:
            granularity: The granularity to truncate to.
            timezone: The optional timezone.

        Returns:
            A new `Expression` representing the timestamp_trunc operation.
        """
        args = [self, self._cast_to_expr_or_convert_to_constant(granularity)]
        if timezone is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(timezone))
        return FunctionExpression("timestamp_trunc", args)

    @expose_as_static
    def timestamp_extract(
        self,
        part: TimePart | str | Expression,
        timezone: str | Expression | None = None,
    ) -> "Expression":
        """Creates an expression that extracts a part of a timestamp.

        Example:
            >>> # Extract the year from the 'createdAt' field using TimePart enum
            >>> Field.of("createdAt").timestamp_extract(TimePart.YEAR)
            >>> # Extract the year from the 'createdAt' field in the 'America/Los_Angeles' timezone
            >>> Field.of("createdAt").timestamp_extract(TimePart.YEAR, "America/Los_Angeles")
            >>> # Extract the year from the 'createdAt' field using a string
            >>> Field.of("createdAt").timestamp_extract("year")

        Args:
            part: The part to extract.
            timezone: The optional timezone.

        Returns:
            A new `Expression` representing the timestamp_extract operation.
        """
        args = [self, self._cast_to_expr_or_convert_to_constant(part)]
        if timezone is not None:
            args.append(self._cast_to_expr_or_convert_to_constant(timezone))
        return FunctionExpression("timestamp_extract", args)

    @expose_as_static
    def timestamp_diff(
        self, start: Expression | datetime.datetime, unit: TimeUnit | str | Expression
    ) -> "Expression":
        """Creates an expression that computes the difference between two timestamps in the specified unit.

        Example:
            >>> # Compute the difference in days between the 'end' field and the 'start' field using TimeUnit enum
            >>> Field.of("end").timestamp_diff(Field.of("start"), TimeUnit.DAY)
            >>> # Compute the difference in days using a string
            >>> Field.of("end").timestamp_diff(Field.of("start"), "day")

        Args:
            start: The start timestamp.
            unit: The unit of time.

        Returns:
            A new `Expression` representing the timestamp_diff operation.
        """
        return FunctionExpression(
            "timestamp_diff",
            [
                self,
                self._cast_to_expr_or_convert_to_constant(start),
                self._cast_to_expr_or_convert_to_constant(unit),
            ],
        )

    @expose_as_static
    def if_null(self, *others: Expression | CONSTANT_TYPE) -> "Expression":
        """Creates an expression that returns the first non-null expression from the provided arguments.

        Example:
            >>> # Return the 'nickname' field if not null, otherwise return 'firstName'
            >>> Field.of("nickname").if_null(Field.of("firstName"))

        Args:
            *others: Additional expressions or constants to evaluate if the previous ones are null.

        Returns:
            A new `Expression` representing the if_null operation.
        """
        return FunctionExpression(
            "if_null",
            [self] + [self._cast_to_expr_or_convert_to_constant(o) for o in others],
        )

    @expose_as_static
    def type(self) -> "Expression":
        """Creates an expression that returns the data type of this expression's result as a string.

        Example:
            >>> # Get the type of the 'title' field
            >>> Field.of("title").type()

        Returns:
            A new `Expression` representing the type operation.
        """
        return FunctionExpression("type", [self])

    @expose_as_static
    def is_type(
        self, type_val: PipelineDataType | str | Expression
    ) -> "BooleanExpression":
        """Creates an expression that checks if the result is of the specified type.

        Example:
            >>> # Check if the 'price' field is a number
            >>> Field.of("price").is_type("number")

        Args:
            type_val: The type string or expression to check against.

        Returns:
            A new `BooleanExpression` representing the is_type operation.
        """
        return BooleanExpression(
            "is_type", [self, self._cast_to_expr_or_convert_to_constant(type_val)]
        )


class Constant(Expression, Generic[CONSTANT_TYPE]):
    """Represents a constant literal value in an expression."""

    def __init__(self, value: CONSTANT_TYPE):
        self.value: CONSTANT_TYPE = value

    def __eq__(self, other):
        if not isinstance(other, Constant):
            return other == self.value
        else:
            return other.value == self.value

    @staticmethod
    def of(value: CONSTANT_TYPE) -> Constant[CONSTANT_TYPE]:
        """Creates a constant expression from a Python value."""
        return Constant(value)

    def __repr__(self):
        value_str = repr(self.value)
        if isinstance(self.value, float) and value_str == "nan":
            value_str = "math.nan"
        return f"Constant.of({value_str})"

    def __hash__(self):
        return hash(self.value)

    def _to_pb(self) -> Value:
        return encode_value(self.value)


class FunctionExpression(Expression):
    """A base class for expressions that represent function calls."""

    def __init__(
        self,
        name: str,
        params: Sequence[Expression],
        *,
        repr_function: Callable[["FunctionExpression"], str] | None = None,
    ):
        self.name = name
        self.params = list(params)
        self._repr_function = repr_function or self._build_infix_repr()

    def __repr__(self):
        """
        Most FunctionExpressions can be triggered infix. Eg: Field.of('age').greater_than(18).

        Display them this way in the repr string where possible
        """
        return self._repr_function(self)

    def __eq__(self, other):
        if not isinstance(other, FunctionExpression):
            return False
        else:
            return other.name == self.name and other.params == self.params

    @staticmethod
    def _build_infix_repr(
        name_override: str | None = None,
    ) -> Callable[["FunctionExpression"], str]:
        """Creates a repr_function that displays a FunctionExpression using infix notation.

        Example:
            `value.greater_than(18)`
        """

        def build_repr(expr):
            final_name = name_override or expr.name
            args = expr.params
            if len(args) == 0:
                return f"{final_name}()"
            elif len(args) == 1:
                return f"{args[0]!r}.{final_name}()"
            elif len(args) == 2:
                return f"{args[0]!r}.{final_name}({args[1]!r})"
            else:
                return f"{args[0]!r}.{final_name}({', '.join([repr(a) for a in args[1:]])})"

        return build_repr

    @staticmethod
    def _build_standalone_repr(
        name_override: str | None = None,
    ) -> Callable[["FunctionExpression"], str]:
        """Creates a repr_function that displays a FunctionExpression using standalone function notation.

        Example:
            `GreaterThan(value, 18)`
        """

        def build_repr(expr):
            final_name = name_override or expr.__class__.__name__
            return f"{final_name}({', '.join([repr(a) for a in expr.params])})"

        return build_repr

    def _to_pb(self):
        return Value(
            function_value={
                "name": self.name,
                "args": [p._to_pb() for p in self.params],
            }
        )


class AggregateFunction(FunctionExpression):
    """A base class for aggregation functions that operate across multiple inputs."""


class Selectable(Expression):
    """Base class for expressions that can be selected or aliased in projection stages."""

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        else:
            return other._to_map() == self._to_map()

    @abstractmethod
    def _to_map(self) -> tuple[str, Value]:
        """
        Returns a str: Value representation of the Selectable
        """
        raise NotImplementedError

    @classmethod
    def _value_from_selectables(cls, *selectables: Selectable) -> Value:
        """
        Returns a Value representing a map of Selectables
        """
        return Value(
            map_value={
                "fields": {m[0]: m[1] for m in [s._to_map() for s in selectables]}
            }
        )

    @staticmethod
    def _to_value(field_list: Sequence[Selectable]) -> Value:
        return Value(
            map_value={
                "fields": {m[0]: m[1] for m in [f._to_map() for f in field_list]}
            }
        )


T = TypeVar("T", bound=Expression)


class AliasedExpression(Selectable, Generic[T]):
    """Wraps an expression with an alias."""

    _supports_expr_methods = False

    def __init__(self, expr: T, alias: str):
        if isinstance(expr, AliasedExpression):
            raise TypeError(
                "Cannot wrap an AliasedExpression with another alias. An alias can only be applied once."
            )
        self.expr = expr
        self.alias = alias

    def as_(self, alias: str) -> "AliasedExpression":
        raise TypeError(
            "Cannot call as_() on an AliasedExpression. An alias can only be applied once."
        )

    def _to_map(self):
        return self.alias, self.expr._to_pb()

    def __repr__(self):
        return f"{self.expr}.as_('{self.alias}')"

    def _to_pb(self):
        return Value(map_value={"fields": {self.alias: self.expr._to_pb()}})


class Field(Selectable):
    """Represents a reference to a field within a document."""

    DOCUMENT_ID = "__name__"

    def __init__(self, path: str):
        """Initializes a Field reference.

        Args:
            path: The dot-separated path to the field (e.g., "address.city").
                  Use Field.DOCUMENT_ID for the document ID.
        """
        self.path = path

    @staticmethod
    def of(path: str):
        """Creates a Field reference.

        Args:
            path: The dot-separated path to the field (e.g., "address.city").
                  Use Field.DOCUMENT_ID for the document ID.

        Returns:
            A new Field instance.
        """
        return Field(path)

    def _to_map(self):
        return self.path, self._to_pb()

    def __repr__(self):
        return f"Field.of({self.path!r})"

    def _to_pb(self):
        return Value(field_reference_value=self.path)


class BooleanExpression(FunctionExpression):
    """Filters the given data in some way."""

    @staticmethod
    def _from_query_filter_pb(filter_pb, client):
        if isinstance(filter_pb, Query_pb.CompositeFilter):
            sub_filters = [
                BooleanExpression._from_query_filter_pb(f, client)
                for f in filter_pb.filters
            ]
            if filter_pb.op == Query_pb.CompositeFilter.Operator.OR:
                return Or(*sub_filters)
            elif filter_pb.op == Query_pb.CompositeFilter.Operator.AND:
                return And(*sub_filters)
            else:
                raise TypeError(
                    f"Unexpected CompositeFilter operator type: {filter_pb.op}"
                )
        elif isinstance(filter_pb, Query_pb.UnaryFilter):
            field = Field.of(filter_pb.field.field_path)
            if filter_pb.op == Query_pb.UnaryFilter.Operator.IS_NAN:
                return And(field.exists(), field.equal(float("nan")))
            elif filter_pb.op == Query_pb.UnaryFilter.Operator.IS_NOT_NAN:
                return And(field.exists(), Not(field.equal(float("nan"))))
            elif filter_pb.op == Query_pb.UnaryFilter.Operator.IS_NULL:
                return And(field.exists(), field.equal(None))
            elif filter_pb.op == Query_pb.UnaryFilter.Operator.IS_NOT_NULL:
                return And(field.exists(), Not(field.equal(None)))
            else:
                raise TypeError(f"Unexpected UnaryFilter operator type: {filter_pb.op}")
        elif isinstance(filter_pb, Query_pb.FieldFilter):
            field = Field.of(filter_pb.field.field_path)
            value = decode_value(filter_pb.value, client)
            if filter_pb.op == Query_pb.FieldFilter.Operator.LESS_THAN:
                return And(field.exists(), field.less_than(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.LESS_THAN_OR_EQUAL:
                return And(field.exists(), field.less_than_or_equal(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.GREATER_THAN:
                return And(field.exists(), field.greater_than(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.GREATER_THAN_OR_EQUAL:
                return And(field.exists(), field.greater_than_or_equal(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.EQUAL:
                return And(field.exists(), field.equal(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.NOT_EQUAL:
                # In Enterprise DBs NOT_EQUAL will match a field that does not exist,
                # therefore we do not want an existence filter for the NOT_EQUAL conversion
                # so the Query and Pipeline behavior are consistent in Enterprise.
                return field.not_equal(value)
            if filter_pb.op == Query_pb.FieldFilter.Operator.ARRAY_CONTAINS:
                return And(field.exists(), field.array_contains(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.ARRAY_CONTAINS_ANY:
                return And(field.exists(), field.array_contains_any(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.IN:
                return And(field.exists(), field.equal_any(value))
            elif filter_pb.op == Query_pb.FieldFilter.Operator.NOT_IN:
                # In Enterprise DBs NOT_IN will match a field that does not exist,
                # therefore we do not want an existence filter for the NOT_IN conversion
                # so the Query and Pipeline behavior are consistent in Enterprise.
                return field.not_equal_any(value)
            else:
                raise TypeError(f"Unexpected FieldFilter operator type: {filter_pb.op}")
        elif isinstance(filter_pb, Query_pb.Filter):
            # unwrap oneof
            f = (
                filter_pb.composite_filter
                or filter_pb.field_filter
                or filter_pb.unary_filter
            )
            return BooleanExpression._from_query_filter_pb(f, client)
        else:
            raise TypeError(f"Unexpected filter type: {type(filter_pb)}")


class _PipelineValueExpression(Expression):
    """Internal wrapper to represent a pipeline as an expression."""

    def __init__(self, pipeline: "_BasePipeline"):
        self.pipeline = pipeline

    def _to_pb(self) -> Value:
        pipeline_pb = Pipeline_pb(stages=[s._to_pb() for s in self.pipeline.stages])
        return Value(pipeline_value=pipeline_pb)


class Array(FunctionExpression):
    """
    Creates an expression that creates a Firestore array value from an input list.

    Example:
        >>> Array(["bar", Field.of("baz")])

    Args:
        elements: The input list to evaluate in the expression
    """

    def __init__(self, elements: list[Expression | CONSTANT_TYPE]):
        if not isinstance(elements, list):
            raise TypeError("Array must be constructed with a list")
        converted_elements = [
            self._cast_to_expr_or_convert_to_constant(el) for el in elements
        ]
        super().__init__("array", converted_elements)

    def __repr__(self):
        return f"Array({self.params})"


class Map(FunctionExpression):
    """
    Creates an expression that creates a Firestore map value from an input dict.

    Example:
        >>> Expression.map({"foo": "bar", "baz": Field.of("baz")})

    Args:
        elements: The input dict to evaluate in the expression
    """

    def __init__(self, elements: dict[str | Constant[str], Expression | CONSTANT_TYPE]):
        element_list = []
        for k, v in elements.items():
            element_list.append(self._cast_to_expr_or_convert_to_constant(k))
            element_list.append(self._cast_to_expr_or_convert_to_constant(v))
        super().__init__("map", element_list)

    def __repr__(self):
        formatted_params = [
            a.value if isinstance(a, Constant) else a for a in self.params
        ]
        d = {a: b for a, b in zip(formatted_params[::2], formatted_params[1::2])}
        return f"Map({d})"


class And(BooleanExpression):
    """
    Represents an expression that performs a logical 'AND' operation on multiple filter conditions.

    Example:
        >>> # Check if the 'age' field is greater than 18 AND the 'city' field is "London" AND
        >>> # the 'status' field is "active"
        >>> And(Field.of("age").greater_than(18), Field.of("city").equal("London"), Field.of("status").equal("active"))

    Args:
        *conditions: The filter conditions to 'AND' together.
    """

    def __init__(self, *conditions: "BooleanExpression"):
        super().__init__(
            "and", conditions, repr_function=FunctionExpression._build_standalone_repr()
        )


class Not(BooleanExpression):
    """
    Represents an expression that negates a filter condition.

    Example:
        >>> # Find documents where the 'completed' field is NOT true
        >>> Not(Field.of("completed").equal(True))

    Args:
        condition: The filter condition to negate.
    """

    def __init__(self, condition: BooleanExpression):
        super().__init__(
            "not",
            [condition],
            repr_function=FunctionExpression._build_standalone_repr(),
        )


class Or(BooleanExpression):
    """
    Represents expression that performs a logical 'OR' operation on multiple filter conditions.

    Example:
       >>> # Check if the 'age' field is greater than 18 OR the 'city' field is "London" OR
       >>> # the 'status' field is "active"
       >>> Or(Field.of("age").greater_than(18), Field.of("city").equal("London"), Field.of("status").equal("active"))

    Args:
        *conditions: The filter conditions to 'OR' together.
    """

    def __init__(self, *conditions: "BooleanExpression"):
        super().__init__(
            "or", conditions, repr_function=FunctionExpression._build_standalone_repr()
        )


class Nor(BooleanExpression):
    """
    Represents an expression that performs a logical 'NOR' operation on multiple filter conditions.

    Example:
        >>> # Check if neither the 'age' field is greater than 18 nor the 'city' field is "London"
        >>> Nor(Field.of("age").greater_than(18), Field.of("city").equal("London"))

    Args:
        *conditions: The filter conditions to 'NOR' together.
    """

    def __init__(self, *conditions: "BooleanExpression"):
        super().__init__(
            "nor", conditions, repr_function=FunctionExpression._build_standalone_repr()
        )


class Xor(BooleanExpression):
    """
    Represents an expression that performs a logical 'XOR' (exclusive OR) operation on multiple filter conditions.

    Example:
       >>> # Check if only one of the conditions is true: 'age' greater than 18, 'city' is "London",
       >>> # or 'status' is "active".
       >>> Xor(Field.of("age").greater_than(18), Field.of("city").equal("London"), Field.of("status").equal("active"))

    Args:
        *conditions: The filter conditions to 'XOR' together.
    """

    def __init__(self, conditions: Sequence["BooleanExpression"]):
        super().__init__(
            "xor", conditions, repr_function=FunctionExpression._build_standalone_repr()
        )


class Conditional(BooleanExpression):
    """
    Represents a conditional expression that evaluates to a 'then' expression if a condition is true
    and an 'else' expression if the condition is false.

    Example:
        >>> # If 'age' is greater than 18, return "Adult"; otherwise, return "Minor".
        >>> Conditional(Field.of("age").greater_than(18), Constant.of("Adult"), Constant.of("Minor"));

    Args:
        condition: The condition to evaluate.
        then_expr: The expression to return if the condition is true.
        else_expr: The expression to return if the condition is false
    """

    def __init__(
        self, condition: BooleanExpression, then_expr: Expression, else_expr: Expression
    ):
        super().__init__(
            "conditional",
            [condition, then_expr, else_expr],
            repr_function=FunctionExpression._build_standalone_repr(),
        )


class Count(AggregateFunction):
    """
    Represents an aggregation that counts the number of stage inputs with valid evaluations of the
    expression or field.

    Example:
        >>> # Count the total number of products
        >>> Field.of("productId").count().as_("totalProducts")
        >>> Count(Field.of("productId"))
        >>> Count().as_("count")

    Args:
        expression: The expression or field to count. If None, counts all stage inputs.
    """

    def __init__(self, expression: Expression | None = None):
        expression_list = [expression] if expression else []
        super().__init__(
            "count",
            expression_list,
            repr_function=FunctionExpression._build_infix_repr()
            if expression_list
            else FunctionExpression._build_standalone_repr(),
        )


class CurrentTimestamp(FunctionExpression):
    """Creates an expression that returns the current timestamp

    Returns:
        A new `Expression` representing the current timestamp.
    """

    def __init__(self):
        super().__init__(
            "current_timestamp",
            [],
            repr_function=FunctionExpression._build_standalone_repr(),
        )


class Rand(FunctionExpression):
    """Creates an expression that generates a random number between 0.0 and 1.0 but not
    including 1.0.

    Returns:
        A new `Expression` representing the rand operation.
    """

    def __init__(self):
        super().__init__(
            "rand", [], repr_function=FunctionExpression._build_standalone_repr()
        )


class Score(FunctionExpression):
    """Evaluates to the search score that reflects the topicality of the document
    to all of the text predicates (`queryMatch`)
    in the search query. If `SearchOptions.query` is not set or does not contain
    any text predicates, then this topicality score will always be `0`.

    .. note::
        This feature is currently in beta and is subject to change.

    Note: This Expression can only be used within a `Search` stage.

    Example:
        >>> # Sort by search score and retrieve it via add_fields
        >>> db.pipeline().collection("restaurants").search(
        ...     query="tacos",
        ...     sort=Score().descending(),
        ...     add_fields=[Score().as_("search_score")]
        ... )

    Returns:
        A new `Expression` representing the score operation.
    """

    def __init__(self):
        super().__init__(
            "score", [], repr_function=FunctionExpression._build_standalone_repr()
        )


class DocumentMatches(BooleanExpression):
    """Creates a boolean expression for a document match query.

    .. note::
        This feature is currently in beta and is subject to change.

    Note: This Expression can only be used within a `Search` stage.

    Example:
        >>> # Find documents matching the query string
        >>> db.pipeline().collection("restaurants").search(
        ...     query=DocumentMatches("pizza OR pasta")
        ... )

    Args:
        query: The search query string or expression.

    Returns:
        A new `BooleanExpression` representing the document match.
    """

    def __init__(self, query: Expression | str):
        super().__init__(
            "document_matches",
            [Expression._cast_to_expr_or_convert_to_constant(query)],
            repr_function=FunctionExpression._build_standalone_repr(),
        )


class Variable(Expression):
    """
    Creates an expression that retrieves the value of a variable bound via `Pipeline.define`.

    Example:
        >>> # Define a variable "discountedPrice" and use it in a filter
        >>> db.pipeline().collection("products").define(
        ...     Field.of("price").multiply(0.9).as_("discountedPrice")
        ... ).where(Variable("discountedPrice").less_than(100))

    Args:
        name: The name of the variable to retrieve.
    """

    def __init__(self, name: str):
        self.name = name

    def _to_pb(self) -> Value:
        return Value(variable_reference_value=self.name)


class CurrentDocument(FunctionExpression):
    """
    Creates an expression that represents the current document being processed.

    This acts as a handle, allowing you to bind the entire document to a variable or pass the
    document itself to a function or subquery.

    Example:
        >>> # Define the current document as a variable "doc"
        >>> db.pipeline().collection("books").define(
        ...     CurrentDocument().as_("doc")
        ... ).select(Variable("doc").get_field("title"))
    """

    def __init__(self):
        super().__init__(
            "current_document",
            [],
            repr_function=FunctionExpression._build_standalone_repr(),
        )
