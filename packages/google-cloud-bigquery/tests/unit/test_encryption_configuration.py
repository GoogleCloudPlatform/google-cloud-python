# Copyright 2015 Google LLC
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

import unittest
from unittest import mock


class TestEncryptionConfiguration(unittest.TestCase):
    KMS_KEY_NAME = "projects/1/locations/us/keyRings/1/cryptoKeys/1"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.encryption_configuration import (
            EncryptionConfiguration,
        )

        return EncryptionConfiguration

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        encryption_config = self._make_one()
        self.assertIsNone(encryption_config.kms_key_name)

    def test_ctor_with_key(self):
        encryption_config = self._make_one(kms_key_name=self.KMS_KEY_NAME)
        self.assertEqual(encryption_config.kms_key_name, self.KMS_KEY_NAME)

    def test_kms_key_name_setter(self):
        encryption_config = self._make_one()
        self.assertIsNone(encryption_config.kms_key_name)
        encryption_config.kms_key_name = self.KMS_KEY_NAME
        self.assertEqual(encryption_config.kms_key_name, self.KMS_KEY_NAME)
        encryption_config.kms_key_name = None
        self.assertIsNone(encryption_config.kms_key_name)

    def test_from_api_repr(self):
        RESOURCE = {"kmsKeyName": self.KMS_KEY_NAME}
        klass = self._get_target_class()
        encryption_config = klass.from_api_repr(RESOURCE)
        self.assertEqual(encryption_config.kms_key_name, self.KMS_KEY_NAME)

    def test_to_api_repr(self):
        encryption_config = self._make_one(kms_key_name=self.KMS_KEY_NAME)
        resource = encryption_config.to_api_repr()
        self.assertEqual(resource, {"kmsKeyName": self.KMS_KEY_NAME})

    def test___eq___wrong_type(self):
        encryption_config = self._make_one()
        other = object()
        self.assertNotEqual(encryption_config, other)
        self.assertEqual(encryption_config, mock.ANY)

    def test___eq___kms_key_name_mismatch(self):
        encryption_config = self._make_one()
        other = self._make_one(self.KMS_KEY_NAME)
        self.assertNotEqual(encryption_config, other)

    def test___eq___hit(self):
        encryption_config = self._make_one(self.KMS_KEY_NAME)
        other = self._make_one(self.KMS_KEY_NAME)
        self.assertEqual(encryption_config, other)

    def test___ne___wrong_type(self):
        encryption_config = self._make_one()
        other = object()
        self.assertNotEqual(encryption_config, other)
        self.assertEqual(encryption_config, mock.ANY)

    def test___ne___same_value(self):
        encryption_config1 = self._make_one(self.KMS_KEY_NAME)
        encryption_config2 = self._make_one(self.KMS_KEY_NAME)
        # unittest ``assertEqual`` uses ``==`` not ``!=``.
        comparison_val = encryption_config1 != encryption_config2
        self.assertFalse(comparison_val)

    def test___ne___different_values(self):
        encryption_config1 = self._make_one()
        encryption_config2 = self._make_one(self.KMS_KEY_NAME)
        self.assertNotEqual(encryption_config1, encryption_config2)

    def test___hash__set_equality(self):
        encryption_config1 = self._make_one(self.KMS_KEY_NAME)
        encryption_config2 = self._make_one(self.KMS_KEY_NAME)
        set_one = {encryption_config1, encryption_config2}
        set_two = {encryption_config1, encryption_config2}
        self.assertEqual(set_one, set_two)

    def test___hash__not_equals(self):
        encryption_config1 = self._make_one()
        encryption_config2 = self._make_one(self.KMS_KEY_NAME)
        set_one = {encryption_config1}
        set_two = {encryption_config2}
        self.assertNotEqual(set_one, set_two)

    def test___repr__(self):
        encryption_config = self._make_one(self.KMS_KEY_NAME)
        expected = "EncryptionConfiguration({})".format(self.KMS_KEY_NAME)
        self.assertEqual(repr(encryption_config), expected)
