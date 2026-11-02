# Copyright 2016 Google LLC
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


class Test_config_name_from_full_name(unittest.TestCase):
    def _call_fut(self, full_name):
        from google.cloud.runtimeconfig._helpers import config_name_from_full_name

        return config_name_from_full_name(full_name)

    def test_w_simple_name(self):
        CONFIG_NAME = "CONFIG_NAME"
        PROJECT = "my-project-1234"
        PATH = "projects/%s/configs/%s" % (PROJECT, CONFIG_NAME)
        config_name = self._call_fut(PATH)
        self.assertEqual(config_name, CONFIG_NAME)

    def test_w_name_w_all_extras(self):
        CONFIG_NAME = "CONFIG_NAME-part.one~part.two%part-three"
        PROJECT = "my-project-1234"
        PATH = "projects/%s/configs/%s" % (PROJECT, CONFIG_NAME)
        config_name = self._call_fut(PATH)
        self.assertEqual(config_name, CONFIG_NAME)

    def test_w_bad_format(self):
        PATH = "definitley/not/a/resource-name"
        with self.assertRaises(ValueError):
            self._call_fut(PATH)


class Test_variable_name_from_full_name(unittest.TestCase):
    def _call_fut(self, full_name):
        from google.cloud.runtimeconfig._helpers import variable_name_from_full_name

        return variable_name_from_full_name(full_name)

    def test_w_simple_name(self):
        VARIABLE_NAME = "VARIABLE_NAME"
        CONFIG_NAME = "CONFIG_NAME"
        PROJECT = "my-project-1234"
        PATH = "projects/%s/configs/%s/variables/%s" % (
            PROJECT,
            CONFIG_NAME,
            VARIABLE_NAME,
        )
        variable_name = self._call_fut(PATH)
        self.assertEqual(variable_name, VARIABLE_NAME)

    def test_w_name_w_all_extras(self):
        VARIABLE_NAME = "VARIABLE_NAME-part.one/part.two/part-three"
        CONFIG_NAME = "CONFIG_NAME"
        PROJECT = "my-project-1234"
        PATH = "projects/%s/configs/%s/variables/%s" % (
            PROJECT,
            CONFIG_NAME,
            VARIABLE_NAME,
        )
        variable_name = self._call_fut(PATH)
        self.assertEqual(variable_name, VARIABLE_NAME)

    def test_w_bad_format(self):
        PATH = "definitley/not/a/resource/name/for/a/variable"
        with self.assertRaises(ValueError):
            self._call_fut(PATH)
