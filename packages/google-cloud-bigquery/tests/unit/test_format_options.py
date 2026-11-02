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


class TestAvroOptions:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.format_options import AvroOptions

        return AvroOptions

    def test_ctor(self):
        config = self._get_target_class()()
        assert config.use_avro_logical_types is None

    def test_from_api_repr(self):
        config = self._get_target_class().from_api_repr({"useAvroLogicalTypes": True})
        assert config.use_avro_logical_types

    def test_to_api_repr(self):
        config = self._get_target_class()()
        config.use_avro_logical_types = False

        result = config.to_api_repr()
        assert result == {"useAvroLogicalTypes": False}


class TestParquetOptions:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.format_options import ParquetOptions

        return ParquetOptions

    def test_ctor(self):
        config = self._get_target_class()()
        assert config.enum_as_string is None
        assert config.enable_list_inference is None

    def test_from_api_repr(self):
        config = self._get_target_class().from_api_repr(
            {"enumAsString": False, "enableListInference": True}
        )
        assert not config.enum_as_string
        assert config.enable_list_inference
        assert config.map_target_type is None

    def test_to_api_repr(self):
        config = self._get_target_class()()
        config.enum_as_string = True
        config.enable_list_inference = False
        config.map_target_type = "ARRAY_OF_STRUCT"

        result = config.to_api_repr()
        assert result == {
            "enumAsString": True,
            "enableListInference": False,
            "mapTargetType": "ARRAY_OF_STRUCT",
        }
