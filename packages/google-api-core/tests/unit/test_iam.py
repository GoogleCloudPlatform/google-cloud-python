# Copyright 2017 Google LLC
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

import pytest

from google.api_core.iam import _DICT_ACCESS_MSG, InvalidOperationException


class TestPolicy:
    @staticmethod
    def _get_target_class():
        from google.api_core.iam import Policy

        return Policy

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        empty = frozenset()
        policy = self._make_one()
        assert policy.etag is None
        assert policy.version is None
        assert policy.owners == empty
        assert policy.editors == empty
        assert policy.viewers == empty
        assert len(policy) == 0
        assert dict(policy) == {}

    def test_ctor_explicit(self):
        VERSION = 1
        ETAG = "ETAG"
        empty = frozenset()
        policy = self._make_one(ETAG, VERSION)
        assert policy.etag == ETAG
        assert policy.version == VERSION
        assert policy.owners == empty
        assert policy.editors == empty
        assert policy.viewers == empty
        assert len(policy) == 0
        assert dict(policy) == {}

    def test___getitem___miss(self):
        policy = self._make_one()
        assert policy["nonesuch"] == set()

    def test__getitem___and_set(self):
        from google.api_core.iam import OWNER_ROLE

        policy = self._make_one()

        # get the policy using the getter and then modify it
        policy[OWNER_ROLE].add("user:phred@example.com")
        assert dict(policy) == {OWNER_ROLE: {"user:phred@example.com"}}

    def test___getitem___version3(self):
        policy = self._make_one("DEADBEEF", 3)
        with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
            policy["role"]

    def test___getitem___with_conditions(self):
        USER = "user:phred@example.com"
        CONDITION = {"expression": "2 > 1"}
        policy = self._make_one("DEADBEEF", 1)
        policy.bindings = [
            {"role": "role/reader", "members": [USER], "condition": CONDITION}
        ]
        with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
            policy["role/reader"]

    def test___setitem__(self):
        USER = "user:phred@example.com"
        PRINCIPALS = set([USER])
        policy = self._make_one()
        policy["rolename"] = [USER]
        assert policy["rolename"] == PRINCIPALS
        assert len(policy) == 1
        assert dict(policy) == {"rolename": PRINCIPALS}

    def test__set_item__overwrite(self):
        GROUP = "group:test@group.com"
        USER = "user:phred@example.com"
        ALL_USERS = "allUsers"
        MEMBERS = set([ALL_USERS])
        GROUPS = set([GROUP])
        policy = self._make_one()
        policy["first"] = [GROUP]
        policy["second"] = [USER]
        policy["second"] = [ALL_USERS]
        assert policy["second"] == MEMBERS
        assert len(policy) == 2
        assert dict(policy) == {"first": GROUPS, "second": MEMBERS}

    def test___setitem___version3(self):
        policy = self._make_one("DEADBEEF", 3)
        with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
            policy["role/reader"] = ["user:phred@example.com"]

    def test___setitem___with_conditions(self):
        USER = "user:phred@example.com"
        CONDITION = {"expression": "2 > 1"}
        policy = self._make_one("DEADBEEF", 1)
        policy.bindings = [
            {"role": "role/reader", "members": set([USER]), "condition": CONDITION}
        ]
        with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
            policy["role/reader"] = ["user:phred@example.com"]

    def test___delitem___hit(self):
        policy = self._make_one()
        policy.bindings = [
            {"role": "to/keep", "members": set(["phred@example.com"])},
            {"role": "to/remove", "members": set(["phred@example.com"])},
        ]
        del policy["to/remove"]
        assert len(policy) == 1
        assert dict(policy) == {"to/keep": set(["phred@example.com"])}

    def test___delitem___miss(self):
        policy = self._make_one()
        with pytest.raises(KeyError):
            del policy["nonesuch"]

    def test___delitem___version3(self):
        policy = self._make_one("DEADBEEF", 3)
        with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
            del policy["role/reader"]

    def test___delitem___with_conditions(self):
        USER = "user:phred@example.com"
        CONDITION = {"expression": "2 > 1"}
        policy = self._make_one("DEADBEEF", 1)
        policy.bindings = [
            {"role": "role/reader", "members": set([USER]), "condition": CONDITION}
        ]
        with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
            del policy["role/reader"]

    def test_bindings_property(self):
        USER = "user:phred@example.com"
        CONDITION = {"expression": "2 > 1"}
        policy = self._make_one()
        BINDINGS = [
            {"role": "role/reader", "members": set([USER]), "condition": CONDITION}
        ]
        policy.bindings = BINDINGS
        assert policy.bindings == BINDINGS

    def test_owners_getter(self):
        from google.api_core.iam import OWNER_ROLE

        MEMBER = "user:phred@example.com"
        expected = frozenset([MEMBER])
        policy = self._make_one()
        policy[OWNER_ROLE] = [MEMBER]
        assert policy.owners == expected

    def test_owners_setter(self):
        from google.api_core.iam import OWNER_ROLE

        MEMBER = "user:phred@example.com"
        expected = set([MEMBER])
        policy = self._make_one()

        with pytest.warns(
            DeprecationWarning, match="Assigning to 'owners' is deprecated."
        ) as warned:
            policy.owners = [MEMBER]

        (warning,) = warned
        assert warning.category is DeprecationWarning
        assert policy[OWNER_ROLE] == expected

    def test_editors_getter(self):
        from google.api_core.iam import EDITOR_ROLE

        MEMBER = "user:phred@example.com"
        expected = frozenset([MEMBER])
        policy = self._make_one()
        policy[EDITOR_ROLE] = [MEMBER]
        assert policy.editors == expected

    def test_editors_setter(self):
        from google.api_core.iam import EDITOR_ROLE

        MEMBER = "user:phred@example.com"
        expected = set([MEMBER])
        policy = self._make_one()

        with pytest.warns(
            DeprecationWarning, match="Assigning to 'editors' is deprecated."
        ) as warned:
            policy.editors = [MEMBER]

        (warning,) = warned
        assert warning.category is DeprecationWarning
        assert policy[EDITOR_ROLE] == expected

    def test_viewers_getter(self):
        from google.api_core.iam import VIEWER_ROLE

        MEMBER = "user:phred@example.com"
        expected = frozenset([MEMBER])
        policy = self._make_one()
        policy[VIEWER_ROLE] = [MEMBER]
        assert policy.viewers == expected

    def test_viewers_setter(self):
        from google.api_core.iam import VIEWER_ROLE

        MEMBER = "user:phred@example.com"
        expected = set([MEMBER])
        policy = self._make_one()

        with pytest.warns(
            DeprecationWarning, match="Assigning to 'viewers' is deprecated."
        ) as warned:
            policy.viewers = [MEMBER]

        (warning,) = warned
        assert warning.category is DeprecationWarning
        assert policy[VIEWER_ROLE] == expected

    def test_user(self):
        EMAIL = "phred@example.com"
        MEMBER = "user:%s" % (EMAIL,)
        policy = self._make_one()
        assert policy.user(EMAIL) == MEMBER

    def test_service_account(self):
        EMAIL = "phred@example.com"
        MEMBER = "serviceAccount:%s" % (EMAIL,)
        policy = self._make_one()
        assert policy.service_account(EMAIL) == MEMBER

    def test_group(self):
        EMAIL = "phred@example.com"
        MEMBER = "group:%s" % (EMAIL,)
        policy = self._make_one()
        assert policy.group(EMAIL) == MEMBER

    def test_domain(self):
        DOMAIN = "example.com"
        MEMBER = "domain:%s" % (DOMAIN,)
        policy = self._make_one()
        assert policy.domain(DOMAIN) == MEMBER

    def test_all_users(self):
        policy = self._make_one()
        assert policy.all_users() == "allUsers"

    def test_authenticated_users(self):
        policy = self._make_one()
        assert policy.authenticated_users() == "allAuthenticatedUsers"

    def test_from_api_repr_only_etag(self):
        empty = frozenset()
        RESOURCE = {"etag": "ACAB"}
        klass = self._get_target_class()
        policy = klass.from_api_repr(RESOURCE)
        assert policy.etag == "ACAB"
        assert policy.version is None
        assert policy.owners == empty
        assert policy.editors == empty
        assert policy.viewers == empty
        assert dict(policy) == {}

    def test_from_api_repr_complete(self):
        from google.api_core.iam import EDITOR_ROLE, OWNER_ROLE, VIEWER_ROLE

        OWNER1 = "group:cloud-logs@google.com"
        OWNER2 = "user:phred@example.com"
        EDITOR1 = "domain:google.com"
        EDITOR2 = "user:phred@example.com"
        VIEWER1 = "serviceAccount:1234-abcdef@service.example.com"
        VIEWER2 = "user:phred@example.com"
        RESOURCE = {
            "etag": "DEADBEEF",
            "version": 1,
            "bindings": [
                {"role": OWNER_ROLE, "members": [OWNER1, OWNER2]},
                {"role": EDITOR_ROLE, "members": [EDITOR1, EDITOR2]},
                {"role": VIEWER_ROLE, "members": [VIEWER1, VIEWER2]},
            ],
        }
        klass = self._get_target_class()
        policy = klass.from_api_repr(RESOURCE)
        assert policy.etag == "DEADBEEF"
        assert policy.version == 1
        assert policy.owners, frozenset([OWNER1 == OWNER2])
        assert policy.editors, frozenset([EDITOR1 == EDITOR2])
        assert policy.viewers, frozenset([VIEWER1 == VIEWER2])
        assert dict(policy) == {
            OWNER_ROLE: set([OWNER1, OWNER2]),
            EDITOR_ROLE: set([EDITOR1, EDITOR2]),
            VIEWER_ROLE: set([VIEWER1, VIEWER2]),
        }
        assert policy.bindings == [
            {"role": OWNER_ROLE, "members": set([OWNER1, OWNER2])},
            {"role": EDITOR_ROLE, "members": set([EDITOR1, EDITOR2])},
            {"role": VIEWER_ROLE, "members": set([VIEWER1, VIEWER2])},
        ]

    def test_from_api_repr_unknown_role(self):
        USER = "user:phred@example.com"
        GROUP = "group:cloud-logs@google.com"
        RESOURCE = {
            "etag": "DEADBEEF",
            "version": 1,
            "bindings": [{"role": "unknown", "members": [USER, GROUP]}],
        }
        klass = self._get_target_class()
        policy = klass.from_api_repr(RESOURCE)
        assert policy.etag == "DEADBEEF"
        assert policy.version == 1
        assert dict(policy), {"unknown": set([GROUP == USER])}

    def test_to_api_repr_defaults(self):
        policy = self._make_one()
        assert policy.to_api_repr() == {}

    def test_to_api_repr_only_etag(self):
        policy = self._make_one("DEADBEEF")
        assert policy.to_api_repr() == {"etag": "DEADBEEF"}

    def test_to_api_repr_binding_wo_members(self):
        policy = self._make_one()
        policy["empty"] = []
        assert policy.to_api_repr() == {}

    def test_to_api_repr_binding_w_duplicates(self):
        from google.api_core.iam import OWNER_ROLE

        OWNER = "group:cloud-logs@google.com"
        policy = self._make_one()
        with pytest.warns(
            DeprecationWarning, match="Assigning to 'owners' is deprecated."
        ):
            policy.owners = [OWNER, OWNER]
        assert policy.to_api_repr() == {
            "bindings": [{"role": OWNER_ROLE, "members": [OWNER]}]
        }

    def test_to_api_repr_full(self):
        import operator

        from google.api_core.iam import EDITOR_ROLE, OWNER_ROLE, VIEWER_ROLE

        OWNER1 = "group:cloud-logs@google.com"
        OWNER2 = "user:phred@example.com"
        EDITOR1 = "domain:google.com"
        EDITOR2 = "user:phred@example.com"
        VIEWER1 = "serviceAccount:1234-abcdef@service.example.com"
        VIEWER2 = "user:phred@example.com"
        CONDITION = {
            "title": "title",
            "description": "description",
            "expression": "true",
        }
        BINDINGS = [
            {"role": OWNER_ROLE, "members": [OWNER1, OWNER2]},
            {"role": EDITOR_ROLE, "members": [EDITOR1, EDITOR2]},
            {"role": VIEWER_ROLE, "members": [VIEWER1, VIEWER2]},
            {
                "role": VIEWER_ROLE,
                "members": [VIEWER1, VIEWER2],
                "condition": CONDITION,
            },
        ]
        policy = self._make_one("DEADBEEF", 1)
        policy.bindings = BINDINGS
        resource = policy.to_api_repr()
        assert resource["etag"] == "DEADBEEF"
        assert resource["version"] == 1
        key = operator.itemgetter("role")
        assert sorted(resource["bindings"], key=key) == sorted(BINDINGS, key=key)
