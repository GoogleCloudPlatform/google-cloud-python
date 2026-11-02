# Copyright 2018 Google LLC
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

import datetime

from google.cloud.ndb import stats

from . import utils

DEFAULTS = {
    "bytes": 4,
    "count": 2,
    "timestamp": datetime.datetime.utcfromtimestamp(40),
}


def test___all__():
    utils.verify___all__(stats)


class TestBaseStatistic:
    @staticmethod
    def test_get_kind():
        kind = stats.BaseStatistic.STORED_KIND_NAME
        assert stats.BaseStatistic._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.BaseStatistic(**DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2


class TestBaseKindStatistic:
    @staticmethod
    def test_get_kind():
        kind = stats.BaseKindStatistic.STORED_KIND_NAME
        assert stats.BaseKindStatistic._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.BaseKindStatistic(kind_name="test_stat", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0


class TestGlobalStat:
    @staticmethod
    def test_get_kind():
        kind = stats.GlobalStat.STORED_KIND_NAME
        assert stats.GlobalStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.GlobalStat(composite_index_count=5, **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0
        assert stat.composite_index_bytes == 0
        assert stat.composite_index_count == 5


class TestNamespaceStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceStat.STORED_KIND_NAME
        assert stats.NamespaceStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceStat(subject_namespace="test", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.subject_namespace == "test"
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0
        assert stat.composite_index_bytes == 0
        assert stat.composite_index_count == 0


class TestKindStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindStat.STORED_KIND_NAME
        assert stats.KindStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindStat(
            kind_name="test_stat", composite_index_count=2, **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0
        assert stat.composite_index_bytes == 0
        assert stat.composite_index_count == 2


class TestKindRootEntityStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindRootEntityStat.STORED_KIND_NAME
        assert stats.KindRootEntityStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindRootEntityStat(kind_name="test_stat", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0


class TestKindNonRootEntityStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindNonRootEntityStat.STORED_KIND_NAME
        assert stats.KindNonRootEntityStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindNonRootEntityStat(kind_name="test_stat", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0


class TestPropertyTypeStat:
    @staticmethod
    def test_get_kind():
        kind = stats.PropertyTypeStat.STORED_KIND_NAME
        assert stats.PropertyTypeStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.PropertyTypeStat(property_type="test_property", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.property_type == "test_property"
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestKindPropertyTypeStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindPropertyTypeStat.STORED_KIND_NAME
        assert stats.KindPropertyTypeStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindPropertyTypeStat(
            kind_name="test_stat", property_type="test_property", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.property_type == "test_property"
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestKindPropertyNameStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindPropertyNameStat.STORED_KIND_NAME
        assert stats.KindPropertyNameStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindPropertyNameStat(
            kind_name="test_stat", property_name="test_property", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.property_name == "test_property"
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestKindPropertyNamePropertyTypeStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindPropertyNamePropertyTypeStat.STORED_KIND_NAME
        assert stats.KindPropertyNamePropertyTypeStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindPropertyNamePropertyTypeStat(
            kind_name="test_stat",
            property_name="test_name",
            property_type="test_type",
            **DEFAULTS,
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.property_type == "test_type"
        assert stat.property_name == "test_name"
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestKindCompositeIndexStat:
    @staticmethod
    def test_get_kind():
        kind = stats.KindCompositeIndexStat.STORED_KIND_NAME
        assert stats.KindCompositeIndexStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.KindCompositeIndexStat(
            index_id=1, kind_name="test_kind", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.index_id == 1
        assert stat.kind_name == "test_kind"


class TestNamespaceGlobalStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceGlobalStat.STORED_KIND_NAME
        assert stats.NamespaceGlobalStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceGlobalStat(composite_index_count=5, **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0
        assert stat.composite_index_bytes == 0
        assert stat.composite_index_count == 5


class TestNamespaceKindCompositeIndexStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindCompositeIndexStat.STORED_KIND_NAME
        assert stats.NamespaceKindCompositeIndexStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindCompositeIndexStat(
            index_id=1, kind_name="test_kind", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.index_id == 1
        assert stat.kind_name == "test_kind"


class TestNamespaceKindNonRootEntityStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindNonRootEntityStat.STORED_KIND_NAME
        assert stats.NamespaceKindNonRootEntityStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindNonRootEntityStat(kind_name="test_stat", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0


class TestNamespaceKindPropertyNamePropertyTypeStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindPropertyNamePropertyTypeStat.STORED_KIND_NAME
        assert stats.NamespaceKindPropertyNamePropertyTypeStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindPropertyNamePropertyTypeStat(
            kind_name="test_stat",
            property_name="test_name",
            property_type="test_type",
            **DEFAULTS,
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.property_type == "test_type"
        assert stat.property_name == "test_name"
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestNamespaceKindPropertyNameStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindPropertyNameStat.STORED_KIND_NAME
        assert stats.NamespaceKindPropertyNameStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindPropertyNameStat(
            kind_name="test_stat", property_name="test_property", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.property_name == "test_property"
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestNamespaceKindPropertyTypeStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindPropertyTypeStat.STORED_KIND_NAME
        assert stats.NamespaceKindPropertyTypeStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindPropertyTypeStat(
            kind_name="test_stat", property_type="test_property", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.property_type == "test_property"
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestNamespaceKindRootEntityStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindRootEntityStat.STORED_KIND_NAME
        assert stats.NamespaceKindRootEntityStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindRootEntityStat(kind_name="test_stat", **DEFAULTS)
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0


class TestNamespacePropertyTypeStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespacePropertyTypeStat.STORED_KIND_NAME
        assert stats.NamespacePropertyTypeStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespacePropertyTypeStat(
            property_type="test_property", **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.property_type == "test_property"
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0


class TestNamespaceKindStat:
    @staticmethod
    def test_get_kind():
        kind = stats.NamespaceKindStat.STORED_KIND_NAME
        assert stats.NamespaceKindStat._get_kind() == kind

    @staticmethod
    def test_constructor():
        stat = stats.NamespaceKindStat(
            kind_name="test_stat", composite_index_count=2, **DEFAULTS
        )
        assert stat.bytes == 4
        assert stat.count == 2
        assert stat.kind_name == "test_stat"
        assert stat.entity_bytes == 0
        assert stat.builtin_index_bytes == 0
        assert stat.builtin_index_count == 0
        assert stat.composite_index_bytes == 0
        assert stat.composite_index_count == 2
