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

import mock
import pytest

from ._testing import _make_credentials


def _make_max_versions_gc_rule(*args, **kwargs):
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    return MaxVersionsGCRule(*args, **kwargs)


def test_max_versions_gc_rule___eq__type_differ():
    gc_rule1 = _make_max_versions_gc_rule(10)
    assert gc_rule1 != object()
    assert gc_rule1 == mock.ANY


def test_max_versions_gc_rule___eq__same_value():
    gc_rule1 = _make_max_versions_gc_rule(2)
    gc_rule2 = _make_max_versions_gc_rule(2)
    assert gc_rule1 == gc_rule2


def test_max_versions_gc_rule___ne__same_value():
    gc_rule1 = _make_max_versions_gc_rule(99)
    gc_rule2 = _make_max_versions_gc_rule(99)
    assert not (gc_rule1 != gc_rule2)


def test_max_versions_gc_rule_to_pb():
    max_num_versions = 1337
    gc_rule = _make_max_versions_gc_rule(max_num_versions=max_num_versions)
    pb_val = gc_rule.to_pb()
    expected = _GcRulePB(max_num_versions=max_num_versions)
    assert pb_val == expected


def _make_max_age_gc_rule(*args, **kwargs):
    from google.cloud.bigtable.column_family import MaxAgeGCRule

    return MaxAgeGCRule(*args, **kwargs)


def test_max_age_gc_rule___eq__type_differ():
    max_age = object()
    gc_rule1 = _make_max_age_gc_rule(max_age=max_age)
    gc_rule2 = object()
    assert gc_rule1 != gc_rule2


def test_max_age_gc_rule___eq__same_value():
    max_age = object()
    gc_rule1 = _make_max_age_gc_rule(max_age=max_age)
    gc_rule2 = _make_max_age_gc_rule(max_age=max_age)
    assert gc_rule1 == gc_rule2


def test_max_age_gc_rule___ne__same_value():
    max_age = object()
    gc_rule1 = _make_max_age_gc_rule(max_age=max_age)
    gc_rule2 = _make_max_age_gc_rule(max_age=max_age)
    assert not (gc_rule1 != gc_rule2)


def test_max_age_gc_rule_to_pb():
    import datetime

    from google.protobuf import duration_pb2

    max_age = datetime.timedelta(seconds=1)
    duration = duration_pb2.Duration(seconds=1)
    gc_rule = _make_max_age_gc_rule(max_age=max_age)
    pb_val = gc_rule.to_pb()
    assert pb_val == _GcRulePB(max_age=duration)


def _make_gc_rule_union(*args, **kwargs):
    from google.cloud.bigtable.column_family import GCRuleUnion

    return GCRuleUnion(*args, **kwargs)


def test_gc_rule_union_constructor():
    rules = object()
    rule_union = _make_gc_rule_union(rules)
    assert rule_union.rules is rules


def test_gc_rule_union___eq__():
    rules = object()
    gc_rule1 = _make_gc_rule_union(rules)
    gc_rule2 = _make_gc_rule_union(rules)
    assert gc_rule1 == gc_rule2


def test_gc_rule_union___eq__type_differ():
    rules = object()
    gc_rule1 = _make_gc_rule_union(rules)
    gc_rule2 = object()
    assert gc_rule1 != gc_rule2


def test_gc_rule_union___ne__same_value():
    rules = object()
    gc_rule1 = _make_gc_rule_union(rules)
    gc_rule2 = _make_gc_rule_union(rules)
    assert not (gc_rule1 != gc_rule2)


def test_gc_rule_union_to_pb():
    import datetime

    from google.protobuf import duration_pb2

    from google.cloud.bigtable.column_family import MaxAgeGCRule, MaxVersionsGCRule

    max_num_versions = 42
    rule1 = MaxVersionsGCRule(max_num_versions)
    pb_rule1 = _GcRulePB(max_num_versions=max_num_versions)

    max_age = datetime.timedelta(seconds=1)
    rule2 = MaxAgeGCRule(max_age)
    pb_rule2 = _GcRulePB(max_age=duration_pb2.Duration(seconds=1))

    rule3 = _make_gc_rule_union(rules=[rule1, rule2])
    pb_rule3 = _GcRulePB(union=_GcRuleUnionPB(rules=[pb_rule1, pb_rule2]))

    gc_rule_pb = rule3.to_pb()
    assert gc_rule_pb == pb_rule3


def test_gc_rule_union_to_pb_nested():
    import datetime

    from google.protobuf import duration_pb2

    from google.cloud.bigtable.column_family import MaxAgeGCRule, MaxVersionsGCRule

    max_num_versions1 = 42
    rule1 = MaxVersionsGCRule(max_num_versions1)
    pb_rule1 = _GcRulePB(max_num_versions=max_num_versions1)

    max_age = datetime.timedelta(seconds=1)
    rule2 = MaxAgeGCRule(max_age)
    pb_rule2 = _GcRulePB(max_age=duration_pb2.Duration(seconds=1))

    rule3 = _make_gc_rule_union(rules=[rule1, rule2])
    pb_rule3 = _GcRulePB(union=_GcRuleUnionPB(rules=[pb_rule1, pb_rule2]))

    max_num_versions2 = 1337
    rule4 = MaxVersionsGCRule(max_num_versions2)
    pb_rule4 = _GcRulePB(max_num_versions=max_num_versions2)

    rule5 = _make_gc_rule_union(rules=[rule3, rule4])
    pb_rule5 = _GcRulePB(union=_GcRuleUnionPB(rules=[pb_rule3, pb_rule4]))

    gc_rule_pb = rule5.to_pb()
    assert gc_rule_pb == pb_rule5


def _make_gc_rule_intersection(*args, **kwargs):
    from google.cloud.bigtable.column_family import GCRuleIntersection

    return GCRuleIntersection(*args, **kwargs)


def test_gc_rule_intersection_constructor():
    rules = object()
    rule_intersection = _make_gc_rule_intersection(rules)
    assert rule_intersection.rules is rules


def test_gc_rule_intersection___eq__():
    rules = object()
    gc_rule1 = _make_gc_rule_intersection(rules)
    gc_rule2 = _make_gc_rule_intersection(rules)
    assert gc_rule1 == gc_rule2


def test_gc_rule_intersection___eq__type_differ():
    rules = object()
    gc_rule1 = _make_gc_rule_intersection(rules)
    gc_rule2 = object()
    assert gc_rule1 != gc_rule2


def test_gc_rule_intersection___ne__same_value():
    rules = object()
    gc_rule1 = _make_gc_rule_intersection(rules)
    gc_rule2 = _make_gc_rule_intersection(rules)
    assert not (gc_rule1 != gc_rule2)


def test_gc_rule_intersection_to_pb():
    import datetime

    from google.protobuf import duration_pb2

    from google.cloud.bigtable.column_family import MaxAgeGCRule, MaxVersionsGCRule

    max_num_versions = 42
    rule1 = MaxVersionsGCRule(max_num_versions)
    pb_rule1 = _GcRulePB(max_num_versions=max_num_versions)

    max_age = datetime.timedelta(seconds=1)
    rule2 = MaxAgeGCRule(max_age)
    pb_rule2 = _GcRulePB(max_age=duration_pb2.Duration(seconds=1))

    rule3 = _make_gc_rule_intersection(rules=[rule1, rule2])
    pb_rule3 = _GcRulePB(intersection=_GcRuleIntersectionPB(rules=[pb_rule1, pb_rule2]))

    gc_rule_pb = rule3.to_pb()
    assert gc_rule_pb == pb_rule3


def test_gc_rule_intersection_to_pb_nested():
    import datetime

    from google.protobuf import duration_pb2

    from google.cloud.bigtable.column_family import MaxAgeGCRule, MaxVersionsGCRule

    max_num_versions1 = 42
    rule1 = MaxVersionsGCRule(max_num_versions1)
    pb_rule1 = _GcRulePB(max_num_versions=max_num_versions1)

    max_age = datetime.timedelta(seconds=1)
    rule2 = MaxAgeGCRule(max_age)
    pb_rule2 = _GcRulePB(max_age=duration_pb2.Duration(seconds=1))

    rule3 = _make_gc_rule_intersection(rules=[rule1, rule2])
    pb_rule3 = _GcRulePB(intersection=_GcRuleIntersectionPB(rules=[pb_rule1, pb_rule2]))

    max_num_versions2 = 1337
    rule4 = MaxVersionsGCRule(max_num_versions2)
    pb_rule4 = _GcRulePB(max_num_versions=max_num_versions2)

    rule5 = _make_gc_rule_intersection(rules=[rule3, rule4])
    pb_rule5 = _GcRulePB(intersection=_GcRuleIntersectionPB(rules=[pb_rule3, pb_rule4]))

    gc_rule_pb = rule5.to_pb()
    assert gc_rule_pb == pb_rule5


def _make_column_family(*args, **kwargs):
    from google.cloud.bigtable.column_family import ColumnFamily

    return ColumnFamily(*args, **kwargs)


def _make_client(*args, **kwargs):
    from google.cloud.bigtable.client import Client

    return Client(*args, **kwargs)


def test_column_family_constructor():
    column_family_id = "column-family-id"
    table = object()
    gc_rule = object()
    column_family = _make_column_family(column_family_id, table, gc_rule=gc_rule)

    assert column_family.column_family_id == column_family_id
    assert column_family._table is table
    assert column_family.gc_rule is gc_rule


def test_column_family_name_property():
    column_family_id = "column-family-id"
    table_name = "table_name"
    table = _Table(table_name)
    column_family = _make_column_family(column_family_id, table)

    expected_name = table_name + "/columnFamilies/" + column_family_id
    assert column_family.name == expected_name


def test_column_family___eq__():
    column_family_id = "column_family_id"
    table = object()
    gc_rule = object()
    column_family1 = _make_column_family(column_family_id, table, gc_rule=gc_rule)
    column_family2 = _make_column_family(column_family_id, table, gc_rule=gc_rule)
    assert column_family1 == column_family2


def test_column_family___eq__type_differ():
    column_family1 = _make_column_family("column_family_id", None)
    column_family2 = object()
    assert column_family1 != column_family2


def test_column_family___ne__same_value():
    column_family_id = "column_family_id"
    table = object()
    gc_rule = object()
    column_family1 = _make_column_family(column_family_id, table, gc_rule=gc_rule)
    column_family2 = _make_column_family(column_family_id, table, gc_rule=gc_rule)
    assert not (column_family1 != column_family2)


def test_column_family___ne__():
    column_family1 = _make_column_family("column_family_id1", None)
    column_family2 = _make_column_family("column_family_id2", None)
    assert column_family1 != column_family2


def test_column_family_to_pb_no_rules():
    column_family = _make_column_family("column_family_id", None)
    pb_val = column_family.to_pb()
    expected = _ColumnFamilyPB()
    assert pb_val == expected


def test_column_family_to_pb_with_rule():
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    gc_rule = MaxVersionsGCRule(1)
    column_family = _make_column_family("column_family_id", None, gc_rule=gc_rule)
    pb_val = column_family.to_pb()
    expected = _ColumnFamilyPB(gc_rule=gc_rule.to_pb())
    assert pb_val == expected


def _create_test_helper(gc_rule=None):
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_table_admin as table_admin_v2_pb2,
    )

    from ._testing import _FakeStub

    project_id = "project-id"
    zone = "zone"
    cluster_id = "cluster-id"
    table_id = "table-id"
    column_family_id = "column-family-id"
    table_name = (
        "projects/"
        + project_id
        + "/zones/"
        + zone
        + "/clusters/"
        + cluster_id
        + "/tables/"
        + table_id
    )

    api = mock.create_autospec(BaseBigtableTableAdminClient)

    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client)
    column_family = _make_column_family(column_family_id, table, gc_rule=gc_rule)

    # Create request_pb
    if gc_rule is None:
        column_family_pb = _ColumnFamilyPB()
    else:
        column_family_pb = _ColumnFamilyPB(gc_rule=gc_rule.to_pb())
    request_pb = table_admin_v2_pb2.ModifyColumnFamiliesRequest(name=table_name)
    modification = table_admin_v2_pb2.ModifyColumnFamiliesRequest.Modification()
    modification.id = column_family_id
    modification.create = column_family_pb
    request_pb.modifications.append(modification)

    # Create response_pb
    response_pb = _ColumnFamilyPB()

    # Patch the stub used by the API method.
    stub = _FakeStub(response_pb)
    client._table_admin_client = api
    client._table_admin_client.transport.create = stub

    # Create expected_result.
    expected_result = None  # create() has no return value.

    # Perform the method and check the result.
    assert stub.results == (response_pb,)
    result = column_family.create()
    assert result == expected_result


def test_column_family_create():
    _create_test_helper(gc_rule=None)


def test_column_family_create_with_gc_rule():
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    gc_rule = MaxVersionsGCRule(1337)
    _create_test_helper(gc_rule=gc_rule)


def _update_test_helper(gc_rule=None):
    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_table_admin as table_admin_v2_pb2,
    )

    from ._testing import _FakeStub

    project_id = "project-id"
    zone = "zone"
    cluster_id = "cluster-id"
    table_id = "table-id"
    column_family_id = "column-family-id"
    table_name = (
        "projects/"
        + project_id
        + "/zones/"
        + zone
        + "/clusters/"
        + cluster_id
        + "/tables/"
        + table_id
    )

    api = mock.create_autospec(BaseBigtableTableAdminClient)
    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client)
    column_family = _make_column_family(column_family_id, table, gc_rule=gc_rule)

    # Create request_pb
    if gc_rule is None:
        column_family_pb = _ColumnFamilyPB()
    else:
        column_family_pb = _ColumnFamilyPB(gc_rule=gc_rule.to_pb())
    request_pb = table_admin_v2_pb2.ModifyColumnFamiliesRequest(name=table_name)
    modification = table_admin_v2_pb2.ModifyColumnFamiliesRequest.Modification()
    modification.id = column_family_id
    modification.update = column_family_pb
    request_pb.modifications.append(modification)

    # Create response_pb
    response_pb = _ColumnFamilyPB()

    # Patch the stub used by the API method.
    stub = _FakeStub(response_pb)
    client._table_admin_client = api
    client._table_admin_client.transport.update = stub

    # Create expected_result.
    expected_result = None  # update() has no return value.

    # Perform the method and check the result.
    assert stub.results == (response_pb,)
    result = column_family.update()
    assert result == expected_result


def test_column_family_update():
    _update_test_helper(gc_rule=None)


def test_column_family_update_with_gc_rule():
    from google.cloud.bigtable.column_family import MaxVersionsGCRule

    gc_rule = MaxVersionsGCRule(1337)
    _update_test_helper(gc_rule=gc_rule)


def test_column_family_delete():
    from google.protobuf import empty_pb2

    from google.cloud.bigtable_admin_v2.services.bigtable_table_admin import (
        BaseBigtableTableAdminClient,
    )
    from google.cloud.bigtable_admin_v2.types import (
        bigtable_table_admin as table_admin_v2_pb2,
    )

    from ._testing import _FakeStub

    project_id = "project-id"
    zone = "zone"
    cluster_id = "cluster-id"
    table_id = "table-id"
    column_family_id = "column-family-id"
    table_name = (
        "projects/"
        + project_id
        + "/zones/"
        + zone
        + "/clusters/"
        + cluster_id
        + "/tables/"
        + table_id
    )

    api = mock.create_autospec(BaseBigtableTableAdminClient)
    credentials = _make_credentials()
    client = _make_client(project=project_id, credentials=credentials, admin=True)
    table = _Table(table_name, client=client)
    column_family = _make_column_family(column_family_id, table)

    # Create request_pb
    request_pb = table_admin_v2_pb2.ModifyColumnFamiliesRequest(name=table_name)
    modification = table_admin_v2_pb2.ModifyColumnFamiliesRequest.Modification(
        id=column_family_id, drop=True
    )
    request_pb.modifications.append(modification)

    # Create response_pb
    response_pb = empty_pb2.Empty()

    # Patch the stub used by the API method.
    stub = _FakeStub(response_pb)
    client._table_admin_client = api
    client._table_admin_client.transport.delete = stub

    # Create expected_result.
    expected_result = None  # delete() has no return value.

    # Perform the method and check the result.
    assert stub.results == (response_pb,)
    result = column_family.delete()
    assert result == expected_result


def test__gc_rule_from_pb_empty():
    from google.cloud.bigtable.column_family import _gc_rule_from_pb

    gc_rule_pb = _GcRulePB()
    assert _gc_rule_from_pb(gc_rule_pb) is None


def test__gc_rule_from_pb_max_num_versions():
    from google.cloud.bigtable.column_family import MaxVersionsGCRule, _gc_rule_from_pb

    orig_rule = MaxVersionsGCRule(1)
    gc_rule_pb = orig_rule.to_pb()
    result = _gc_rule_from_pb(gc_rule_pb)
    assert isinstance(result, MaxVersionsGCRule)
    assert result == orig_rule


def test__gc_rule_from_pb_max_age():
    import datetime

    from google.cloud.bigtable.column_family import MaxAgeGCRule, _gc_rule_from_pb

    orig_rule = MaxAgeGCRule(datetime.timedelta(seconds=1))
    gc_rule_pb = orig_rule.to_pb()
    result = _gc_rule_from_pb(gc_rule_pb)
    assert isinstance(result, MaxAgeGCRule)
    assert result == orig_rule


def test__gc_rule_from_pb_union():
    import datetime

    from google.cloud.bigtable.column_family import (
        GCRuleUnion,
        MaxAgeGCRule,
        MaxVersionsGCRule,
        _gc_rule_from_pb,
    )

    rule1 = MaxVersionsGCRule(1)
    rule2 = MaxAgeGCRule(datetime.timedelta(seconds=1))
    orig_rule = GCRuleUnion([rule1, rule2])
    gc_rule_pb = orig_rule.to_pb()
    result = _gc_rule_from_pb(gc_rule_pb)
    assert isinstance(result, GCRuleUnion)
    assert result == orig_rule


def test__gc_rule_from_pb_intersection():
    import datetime

    from google.cloud.bigtable.column_family import (
        GCRuleIntersection,
        MaxAgeGCRule,
        MaxVersionsGCRule,
        _gc_rule_from_pb,
    )

    rule1 = MaxVersionsGCRule(1)
    rule2 = MaxAgeGCRule(datetime.timedelta(seconds=1))
    orig_rule = GCRuleIntersection([rule1, rule2])
    gc_rule_pb = orig_rule.to_pb()
    result = _gc_rule_from_pb(gc_rule_pb)
    assert isinstance(result, GCRuleIntersection)
    assert result == orig_rule


def test__gc_rule_from_pb_unknown_field_name():
    from google.cloud.bigtable.column_family import _gc_rule_from_pb

    class MockProto(object):
        names = []

        _pb = {}

        @classmethod
        def WhichOneof(cls, name):
            cls.names.append(name)
            return "unknown"

    MockProto._pb = MockProto

    assert MockProto.names == []

    with pytest.raises(ValueError):
        _gc_rule_from_pb(MockProto)

    assert MockProto.names == ["rule"]


def _GcRulePB(*args, **kw):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.GcRule(*args, **kw)


def _GcRuleIntersectionPB(*args, **kw):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.GcRule.Intersection(*args, **kw)


def _GcRuleUnionPB(*args, **kw):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.GcRule.Union(*args, **kw)


def _ColumnFamilyPB(*args, **kw):
    from google.cloud.bigtable_admin_v2.types import table as table_v2_pb2

    return table_v2_pb2.ColumnFamily(*args, **kw)


class _Instance(object):
    def __init__(self, client=None):
        self._client = client


class _Client(object):
    pass


class _Table(object):
    def __init__(self, name, client=None):
        self.name = name
        self._instance = _Instance(client)
