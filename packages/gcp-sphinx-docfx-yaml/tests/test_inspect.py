"""Tests for various inspect related utils."""

import inspect
import unittest
from typing import Any, Optional, Union

from parameterized import parameterized

from docfx_yaml import extension


class TestGenerate(unittest.TestCase):
    types_to_test = [
        [
            # Test for a simple type without __args__.
            str,
            "str",
        ],
        [
            # Test for a more complex type without forward reference.
            list[str],
            "list[str]",
        ],
        [
            # Test for imported type, without forward reference.
            dict[str, Any],
            "dict[str, typing.Any]",
        ],
        [
            # Test for forward reference.
            Optional["ForwardClass"],
            "typing.Optional[ForwardClass]",
        ],
        [
            # Test for multiple forward references.
            Union["ForwardClass", "ForwardClass2"],
            "typing.Union[ForwardClass, ForwardClass2]",
        ],
    ]

    @parameterized.expand(types_to_test)
    def test_extracts_annotations(self, type_to_test, expected_type_name):
        """Extracts annotations from test method, compares to expected name."""

        def test_method(name: type_to_test):
            pass

        annotations = inspect.getfullargspec(test_method).annotations
        annotation_to_use = annotations["name"]

        extracted_annotation_name = extension._extract_type_name(annotation_to_use)

        self.assertEqual(extracted_annotation_name, expected_type_name)


if __name__ == "__main__":
    unittest.main()
