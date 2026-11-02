# Copyright 2014 Google LLC
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

import mock

from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
)


class Test_ACLEntity(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.acl import _ACLEntity

        return _ACLEntity

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_default_identifier(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        self.assertEqual(entity.type, TYPE)
        self.assertIsNone(entity.identifier)
        self.assertEqual(entity.get_roles(), set())

    def test_ctor_w_identifier(self):
        TYPE = "type"
        ID = "id"
        entity = self._make_one(TYPE, ID)
        self.assertEqual(entity.type, TYPE)
        self.assertEqual(entity.identifier, ID)
        self.assertEqual(entity.get_roles(), set())

    def test___str__no_identifier(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        self.assertEqual(str(entity), TYPE)

    def test___str__w_identifier(self):
        TYPE = "type"
        ID = "id"
        entity = self._make_one(TYPE, ID)
        self.assertEqual(str(entity), f"{TYPE}-{ID}")

    def test_grant_simple(self):
        TYPE = "type"
        ROLE = "role"
        entity = self._make_one(TYPE)
        entity.grant(ROLE)
        self.assertEqual(entity.get_roles(), set([ROLE]))

    def test_grant_duplicate(self):
        TYPE = "type"
        ROLE1 = "role1"
        ROLE2 = "role2"
        entity = self._make_one(TYPE)
        entity.grant(ROLE1)
        entity.grant(ROLE2)
        entity.grant(ROLE1)
        self.assertEqual(entity.get_roles(), set([ROLE1, ROLE2]))

    def test_revoke_miss(self):
        TYPE = "type"
        ROLE = "nonesuch"
        entity = self._make_one(TYPE)
        entity.revoke(ROLE)
        self.assertEqual(entity.get_roles(), set())

    def test_revoke_hit(self):
        TYPE = "type"
        ROLE1 = "role1"
        ROLE2 = "role2"
        entity = self._make_one(TYPE)
        entity.grant(ROLE1)
        entity.grant(ROLE2)
        entity.revoke(ROLE1)
        self.assertEqual(entity.get_roles(), set([ROLE2]))

    def test_grant_read(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        entity.grant_read()
        self.assertEqual(entity.get_roles(), set([entity.READER_ROLE]))

    def test_grant_write(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        entity.grant_write()
        self.assertEqual(entity.get_roles(), set([entity.WRITER_ROLE]))

    def test_grant_owner(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        entity.grant_owner()
        self.assertEqual(entity.get_roles(), set([entity.OWNER_ROLE]))

    def test_revoke_read(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        entity.grant(entity.READER_ROLE)
        entity.revoke_read()
        self.assertEqual(entity.get_roles(), set())

    def test_revoke_write(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        entity.grant(entity.WRITER_ROLE)
        entity.revoke_write()
        self.assertEqual(entity.get_roles(), set())

    def test_revoke_owner(self):
        TYPE = "type"
        entity = self._make_one(TYPE)
        entity.grant(entity.OWNER_ROLE)
        entity.revoke_owner()
        self.assertEqual(entity.get_roles(), set())


class FakeReload(object):
    """A callable used for faking the reload() method of an ACL instance."""

    def __init__(self, acl):
        self.acl = acl
        self.timeouts_used = []

    def __call__(self, timeout=None):
        self.acl.loaded = True
        self.timeouts_used.append(timeout)


class Test_ACL(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.acl import ACL

        return ACL

    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_validate_predefined(self):
        ACL = self._get_target_class()
        self.assertIsNone(ACL.validate_predefined(None))
        self.assertEqual(ACL.validate_predefined("public-read"), "publicRead")
        self.assertEqual(ACL.validate_predefined("publicRead"), "publicRead")
        with self.assertRaises(ValueError):
            ACL.validate_predefined("publicread")

    def test_ctor(self):
        acl = self._make_one()
        self.assertEqual(acl.entities, {})
        self.assertFalse(acl.loaded)

    def test__ensure_loaded(self):
        acl = self._make_one()
        _reload = FakeReload(acl)
        acl.reload = _reload
        acl.loaded = False

        acl._ensure_loaded(timeout=42)

        self.assertTrue(acl.loaded)
        self.assertEqual(_reload.timeouts_used[0], 42)

    def test_client_is_abstract(self):
        acl = self._make_one()
        self.assertRaises(NotImplementedError, lambda: acl.client)

    def test_reset(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        acl.entity(TYPE, ID)
        acl.reset()
        self.assertEqual(acl.entities, {})
        self.assertFalse(acl.loaded)

    def test___iter___empty_eager(self):
        acl = self._make_one()
        acl.loaded = True
        self.assertEqual(list(acl), [])

    def test___iter___empty_lazy(self):
        acl = self._make_one()
        _reload = FakeReload(acl)
        acl.loaded = False

        acl.reload = _reload
        self.assertEqual(list(acl), [])
        self.assertTrue(acl.loaded)
        self.assertEqual(_reload.timeouts_used[0], self._get_default_timeout())

    def test___iter___non_empty_no_roles(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        acl.entity(TYPE, ID)
        self.assertEqual(list(acl), [])

    def test___iter___non_empty_w_roles(self):
        TYPE = "type"
        ID = "id"
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity(TYPE, ID)
        entity.grant(ROLE)
        self.assertEqual(list(acl), [{"entity": f"{TYPE}-{ID}", "role": ROLE}])

    def test___iter___non_empty_w_empty_role(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity(TYPE, ID)
        entity.grant("")
        self.assertEqual(list(acl), [])

    def test_entity_from_dict_allUsers_eager(self):
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity_from_dict({"entity": "allUsers", "role": ROLE})
        self.assertEqual(entity.type, "allUsers")
        self.assertIsNone(entity.identifier)
        self.assertEqual(entity.get_roles(), set([ROLE]))
        self.assertEqual(list(acl), [{"entity": "allUsers", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_entity_from_dict_allAuthenticatedUsers(self):
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity_from_dict({"entity": "allAuthenticatedUsers", "role": ROLE})
        self.assertEqual(entity.type, "allAuthenticatedUsers")
        self.assertIsNone(entity.identifier)
        self.assertEqual(entity.get_roles(), set([ROLE]))
        self.assertEqual(list(acl), [{"entity": "allAuthenticatedUsers", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_entity_from_dict_string_w_hyphen(self):
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity_from_dict({"entity": "type-id", "role": ROLE})
        self.assertEqual(entity.type, "type")
        self.assertEqual(entity.identifier, "id")
        self.assertEqual(entity.get_roles(), set([ROLE]))
        self.assertEqual(list(acl), [{"entity": "type-id", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_entity_from_dict_string_wo_hyphen(self):
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        self.assertRaises(
            ValueError, acl.entity_from_dict, {"entity": "bogus", "role": ROLE}
        )
        self.assertEqual(list(acl.get_entities()), [])

    def test_has_entity_miss_str_eager(self):
        acl = self._make_one()
        acl.loaded = True
        self.assertFalse(acl.has_entity("nonesuch"))

    def test_has_entity_miss_str_lazy(self):
        acl = self._make_one()
        _reload = FakeReload(acl)
        acl.reload = _reload
        acl.loaded = False

        self.assertFalse(acl.has_entity("nonesuch"))
        self.assertTrue(acl.loaded)
        self.assertEqual(_reload.timeouts_used[0], self._get_default_timeout())

    def test_has_entity_miss_entity(self):
        from google.cloud.storage.acl import _ACLEntity

        TYPE = "type"
        ID = "id"
        entity = _ACLEntity(TYPE, ID)
        acl = self._make_one()
        acl.loaded = True
        self.assertFalse(acl.has_entity(entity))

    def test_has_entity_hit_str(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        acl.entity(TYPE, ID)
        self.assertTrue(acl.has_entity(f"{TYPE}-{ID}"))

    def test_has_entity_hit_entity(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity(TYPE, ID)
        self.assertTrue(acl.has_entity(entity))

    def test_get_entity_miss_str_no_default_eager(self):
        acl = self._make_one()
        acl.loaded = True
        self.assertIsNone(acl.get_entity("nonesuch"))

    def test_get_entity_miss_str_no_default_lazy(self):
        acl = self._make_one()
        _reload = FakeReload(acl)
        acl.reload = _reload
        acl.loaded = False

        self.assertIsNone(acl.get_entity("nonesuch"))
        self.assertTrue(acl.loaded)
        self.assertEqual(_reload.timeouts_used[0], self._get_default_timeout())

    def test_get_entity_miss_entity_no_default(self):
        from google.cloud.storage.acl import _ACLEntity

        TYPE = "type"
        ID = "id"
        entity = _ACLEntity(TYPE, ID)
        acl = self._make_one()
        acl.loaded = True
        self.assertIsNone(acl.get_entity(entity))

    def test_get_entity_miss_str_w_default(self):
        DEFAULT = object()
        acl = self._make_one()
        acl.loaded = True
        self.assertIs(acl.get_entity("nonesuch", DEFAULT), DEFAULT)

    def test_get_entity_miss_entity_w_default(self):
        from google.cloud.storage.acl import _ACLEntity

        DEFAULT = object()
        TYPE = "type"
        ID = "id"
        entity = _ACLEntity(TYPE, ID)
        acl = self._make_one()
        acl.loaded = True
        self.assertIs(acl.get_entity(entity, DEFAULT), DEFAULT)

    def test_get_entity_hit_str(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        acl.entity(TYPE, ID)
        self.assertTrue(acl.has_entity(f"{TYPE}-{ID}"))

    def test_get_entity_hit_entity(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity(TYPE, ID)
        self.assertTrue(acl.has_entity(entity))

    def test_add_entity_miss_eager(self):
        from google.cloud.storage.acl import _ACLEntity

        TYPE = "type"
        ID = "id"
        ROLE = "role"
        entity = _ACLEntity(TYPE, ID)
        entity.grant(ROLE)
        acl = self._make_one()
        acl.loaded = True
        acl.add_entity(entity)
        self.assertTrue(acl.loaded)
        self.assertEqual(list(acl), [{"entity": "type-id", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_add_entity_miss_lazy(self):
        from google.cloud.storage.acl import _ACLEntity

        TYPE = "type"
        ID = "id"
        ROLE = "role"
        entity = _ACLEntity(TYPE, ID)
        entity.grant(ROLE)
        acl = self._make_one()

        _reload = FakeReload(acl)
        acl.reload = _reload
        acl.loaded = False

        acl.add_entity(entity)
        self.assertTrue(acl.loaded)
        self.assertEqual(list(acl), [{"entity": "type-id", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])
        self.assertTrue(acl.loaded)
        self.assertEqual(_reload.timeouts_used[0], self._get_default_timeout())

    def test_add_entity_hit(self):
        from google.cloud.storage.acl import _ACLEntity

        TYPE = "type"
        ID = "id"
        ENTITY_VAL = f"{TYPE}-{ID}"
        ROLE = "role"
        entity = _ACLEntity(TYPE, ID)
        entity.grant(ROLE)
        acl = self._make_one()
        acl.loaded = True
        before = acl.entity(TYPE, ID)
        acl.add_entity(entity)
        self.assertTrue(acl.loaded)
        self.assertIsNot(acl.get_entity(ENTITY_VAL), before)
        self.assertIs(acl.get_entity(ENTITY_VAL), entity)
        self.assertEqual(list(acl), [{"entity": "type-id", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_entity_miss(self):
        TYPE = "type"
        ID = "id"
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity(TYPE, ID)
        self.assertTrue(acl.loaded)
        entity.grant(ROLE)
        self.assertEqual(list(acl), [{"entity": "type-id", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_entity_hit(self):
        TYPE = "type"
        ID = "id"
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        before = acl.entity(TYPE, ID)
        before.grant(ROLE)
        entity = acl.entity(TYPE, ID)
        self.assertIs(entity, before)
        self.assertEqual(list(acl), [{"entity": "type-id", "role": ROLE}])
        self.assertEqual(list(acl.get_entities()), [entity])

    def test_user(self):
        ID = "id"
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.user(ID)
        entity.grant(ROLE)
        self.assertEqual(entity.type, "user")
        self.assertEqual(entity.identifier, ID)
        self.assertEqual(list(acl), [{"entity": f"user-{ID}", "role": ROLE}])

    def test_group(self):
        ID = "id"
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.group(ID)
        entity.grant(ROLE)
        self.assertEqual(entity.type, "group")
        self.assertEqual(entity.identifier, ID)
        self.assertEqual(list(acl), [{"entity": f"group-{ID}", "role": ROLE}])

    def test_domain(self):
        ID = "id"
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.domain(ID)
        entity.grant(ROLE)
        self.assertEqual(entity.type, "domain")
        self.assertEqual(entity.identifier, ID)
        self.assertEqual(list(acl), [{"entity": f"domain-{ID}", "role": ROLE}])

    def test_all(self):
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.all()
        entity.grant(ROLE)
        self.assertEqual(entity.type, "allUsers")
        self.assertIsNone(entity.identifier)
        self.assertEqual(list(acl), [{"entity": "allUsers", "role": ROLE}])

    def test_all_authenticated(self):
        ROLE = "role"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.all_authenticated()
        entity.grant(ROLE)
        self.assertEqual(entity.type, "allAuthenticatedUsers")
        self.assertIsNone(entity.identifier)
        self.assertEqual(list(acl), [{"entity": "allAuthenticatedUsers", "role": ROLE}])

    def test_get_entities_empty_eager(self):
        acl = self._make_one()
        acl.loaded = True
        self.assertEqual(acl.get_entities(), [])

    def test_get_entities_empty_lazy(self):
        acl = self._make_one()
        _reload = FakeReload(acl)
        acl.reload = _reload
        acl.loaded = False

        self.assertEqual(acl.get_entities(), [])
        self.assertTrue(acl.loaded)
        self.assertEqual(_reload.timeouts_used[0], self._get_default_timeout())

    def test_get_entities_nonempty(self):
        TYPE = "type"
        ID = "id"
        acl = self._make_one()
        acl.loaded = True
        entity = acl.entity(TYPE, ID)
        self.assertEqual(acl.get_entities(), [entity])

    def test_reload_missing_w_defaults(self):
        # https://github.com/GoogleCloudPlatform/google-cloud-python/issues/652
        class Derived(self._get_target_class()):
            client = None

        role = "role"
        reload_path = "/testing/acl"
        api_response = {}
        acl = Derived()
        acl.reload_path = reload_path
        acl.loaded = True
        acl.entity("allUsers", role)
        client = acl.client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response

        acl.reload()

        self.assertEqual(list(acl), [])

        expected_query_params = {}
        client._get_resource.assert_called_once_with(
            reload_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_reload_w_empty_result_w_timeout_w_retry_w_explicit_client(self):
        role = "role"
        reload_path = "/testing/acl"
        timeout = 42
        retry = mock.Mock(spec=[])
        api_response = {"items": []}
        acl = self._make_one()
        acl.reload_path = reload_path
        acl.loaded = True
        acl.entity("allUsers", role)
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response

        acl.reload(client=client, timeout=timeout, retry=retry)

        self.assertTrue(acl.loaded)
        self.assertEqual(list(acl), [])

        expected_query_params = {}
        client._get_resource.assert_called_once_with(
            reload_path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
        )

    def test_reload_w_nonempty_result_w_user_project(self):
        role = "role"
        reload_path = "/testing/acl"
        user_project = "user-project-123"
        api_response = {"items": [{"entity": "allUsers", "role": role}]}
        acl = self._make_one()
        acl.reload_path = reload_path
        acl.loaded = True
        acl.user_project = user_project
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response

        acl.reload(client=client)

        self.assertTrue(acl.loaded)
        self.assertEqual(list(acl), [{"entity": "allUsers", "role": role}])

        expected_query_params = {"userProject": user_project}
        client._get_resource.assert_called_once_with(
            reload_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_save_none_set_none_passed(self):
        save_path = "/testing"
        client = mock.Mock(spec=["_patch_resource"])
        acl = self._make_one()
        acl.save_path = save_path

        acl.save(client=client)

        client._patch_resource.assert_not_called()

    def test_save_w_empty_response_w_defaults(self):
        class Derived(self._get_target_class()):
            client = None

        save_path = "/testing"
        api_response = {}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = Derived()
        acl.client = client
        acl.save_path = save_path
        acl.loaded = True

        acl.save()

        self.assertEqual(list(acl), [])

        expected_data = {"acl": []}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_no_acl_w_timeout(self):
        save_path = "/testing"
        role = "role"
        expected_acl = [{"entity": "allUsers", "role": role}]
        api_response = {"acl": expected_acl}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True
        acl.entity("allUsers").grant(role)
        timeout = 42

        acl.save(client=client, timeout=timeout)

        self.assertEqual(list(acl), expected_acl)

        expected_data = api_response
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_w_acl_w_user_project(self):
        save_path = "/testing"
        user_project = "user-project-123"
        role1 = "role1"
        role2 = "role2"
        sticky = {"entity": "allUsers", "role": role2}
        new_acl = [{"entity": "allUsers", "role": role1}]
        api_response = {"acl": [sticky] + new_acl}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True
        acl.user_project = user_project

        acl.save(new_acl, client=client)

        entries = list(acl)
        self.assertEqual(len(entries), 2)
        self.assertTrue(sticky in entries)
        self.assertTrue(new_acl[0] in entries)

        expected_data = {"acl": new_acl}
        expected_query_params = {"projection": "full", "userProject": user_project}
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_w_acl_w_preconditions(self):
        save_path = "/testing"
        role1 = "role1"
        role2 = "role2"
        sticky = {"entity": "allUsers", "role": role2}
        new_acl = [{"entity": "allUsers", "role": role1}]
        api_response = {"acl": [sticky] + new_acl}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True

        acl.save(
            new_acl,
            client=client,
            if_metageneration_match=2,
            if_metageneration_not_match=1,
        )

        entries = list(acl)
        self.assertEqual(len(entries), 2)
        self.assertTrue(sticky in entries)
        self.assertTrue(new_acl[0] in entries)

        expected_data = {"acl": new_acl}
        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_prefefined_invalid(self):
        save_path = "/testing"
        client = mock.Mock(spec=["_patch_resource"])
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True

        with self.assertRaises(ValueError):
            acl.save_predefined("bogus", client=client)

        client._patch_resource.assert_not_called()

    def test_save_predefined_w_defaults(self):
        class Derived(self._get_target_class()):
            client = None

        save_path = "/testing"
        predefined = "private"
        api_response = {"acl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = Derived()
        acl.save_path = save_path
        acl.loaded = True
        acl.client = client

        acl.save_predefined(predefined)

        entries = list(acl)
        self.assertEqual(len(entries), 0)

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
            "predefinedAcl": predefined,
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_predefined_w_XML_alias_w_timeout(self):
        save_path = "/testing"
        predefined_xml = "project-private"
        predefined_json = "projectPrivate"
        api_response = {"acl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True
        timeout = 42

        acl.save_predefined(predefined_xml, client=client, timeout=timeout)

        entries = list(acl)
        self.assertEqual(len(entries), 0)

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
            "predefinedAcl": predefined_json,
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_predefined_w_alternate_query_param(self):
        # Cover case where subclass overrides _PREDEFINED_QUERY_PARAM
        save_path = "/testing"
        predefined = "publicRead"
        api_response = {"acl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True
        acl._PREDEFINED_QUERY_PARAM = "alternate"

        acl.save_predefined(predefined, client=client)

        entries = list(acl)
        self.assertEqual(len(entries), 0)

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
            "alternate": predefined,
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_save_predefined_w_preconditions(self):
        save_path = "/testing"
        predefined = "private"
        api_response = {"acl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True

        acl.save_predefined(
            predefined,
            client=client,
            if_metageneration_match=2,
            if_metageneration_not_match=1,
        )

        entries = list(acl)
        self.assertEqual(len(entries), 0)

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
            "predefinedAcl": predefined,
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_clear_w_defaults(self):
        class Derived(self._get_target_class()):
            client = None

        save_path = "/testing"
        role1 = "role1"
        role2 = "role2"
        sticky = {"entity": "allUsers", "role": role2}
        api_response = {"acl": [sticky]}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = Derived()
        acl.client = client
        acl.save_path = save_path
        acl.loaded = True
        acl.entity("allUsers", role1)

        acl.clear()

        self.assertEqual(list(acl), [sticky])

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_clear_w_explicit_client_w_timeout(self):
        save_path = "/testing"
        role1 = "role1"
        role2 = "role2"
        sticky = {"entity": "allUsers", "role": role2}
        api_response = {"acl": [sticky]}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True
        acl.entity("allUsers", role1)
        timeout = 42

        acl.clear(client=client, timeout=timeout)

        self.assertEqual(list(acl), [sticky])

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_clear_w_explicit_client_w_preconditions(self):
        save_path = "/testing"
        role1 = "role1"
        role2 = "role2"
        sticky = {"entity": "allUsers", "role": role2}
        api_response = {"acl": [sticky]}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        acl = self._make_one()
        acl.save_path = save_path
        acl.loaded = True
        acl.entity("allUsers", role1)

        acl.clear(
            client=client, if_metageneration_match=2, if_metageneration_not_match=1
        )

        self.assertEqual(list(acl), [sticky])

        expected_data = {"acl": []}
        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            save_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )


class Test_BucketACL(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.acl import BucketACL

        return BucketACL

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        NAME = "name"
        bucket = _Bucket(NAME)
        acl = self._make_one(bucket)
        self.assertEqual(acl.entities, {})
        self.assertFalse(acl.loaded)
        self.assertIs(acl.bucket, bucket)
        self.assertEqual(acl.reload_path, f"/b/{NAME}/acl")
        self.assertEqual(acl.save_path, f"/b/{NAME}")

    def test_user_project(self):
        NAME = "name"
        USER_PROJECT = "user-project-123"
        bucket = _Bucket(NAME)
        acl = self._make_one(bucket)
        self.assertIsNone(acl.user_project)
        bucket.user_project = USER_PROJECT
        self.assertEqual(acl.user_project, USER_PROJECT)


class Test_DefaultObjectACL(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.acl import DefaultObjectACL

        return DefaultObjectACL

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        NAME = "name"
        bucket = _Bucket(NAME)
        acl = self._make_one(bucket)
        self.assertEqual(acl.entities, {})
        self.assertFalse(acl.loaded)
        self.assertIs(acl.bucket, bucket)
        self.assertEqual(acl.reload_path, f"/b/{NAME}/defaultObjectAcl")
        self.assertEqual(acl.save_path, f"/b/{NAME}")


class Test_ObjectACL(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.acl import ObjectACL

        return ObjectACL

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        NAME = "name"
        BLOB_NAME = "blob-name"
        bucket = _Bucket(NAME)
        blob = _Blob(bucket, BLOB_NAME)
        acl = self._make_one(blob)
        self.assertEqual(acl.entities, {})
        self.assertFalse(acl.loaded)
        self.assertIs(acl.blob, blob)
        self.assertEqual(acl.reload_path, f"/b/{NAME}/o/{BLOB_NAME}/acl")
        self.assertEqual(acl.save_path, f"/b/{NAME}/o/{BLOB_NAME}")

    def test_user_project(self):
        NAME = "name"
        BLOB_NAME = "blob-name"
        USER_PROJECT = "user-project-123"
        bucket = _Bucket(NAME)
        blob = _Blob(bucket, BLOB_NAME)
        acl = self._make_one(blob)
        self.assertIsNone(acl.user_project)
        blob.user_project = USER_PROJECT
        self.assertEqual(acl.user_project, USER_PROJECT)

    def test_passthrough_methods(self):
        NAME = "name"
        BLOB_NAME = "blob-name"
        bucket = _Bucket(NAME)
        blob = _Blob(bucket, BLOB_NAME)
        acl = self._make_one(blob)

        client = mock.Mock()

        with mock.patch("google.cloud.storage.acl.ACL.clear") as m:
            kwargs = {
                "client": client,
                "if_generation_match": 1,
                "if_generation_not_match": 2,
                "if_metageneration_match": 3,
                "if_metageneration_not_match": 4,
                "timeout": 60,
                "retry": None,
            }

            acl.clear(**kwargs)
            m.assert_called_once_with(**kwargs)

        with mock.patch("google.cloud.storage.acl.ACL.save") as m:
            kwargs = {
                "acl": [],
                "client": client,
                "if_generation_match": 1,
                "if_generation_not_match": 2,
                "if_metageneration_match": 3,
                "if_metageneration_not_match": 4,
                "timeout": 60,
                "retry": None,
            }

            acl.save(**kwargs)
            m.assert_called_once_with(**kwargs)

        with mock.patch("google.cloud.storage.acl.ACL.save_predefined") as m:
            kwargs = {
                "predefined": "predef",
                "client": client,
                "if_generation_match": 1,
                "if_generation_not_match": 2,
                "if_metageneration_match": 3,
                "if_metageneration_not_match": 4,
                "timeout": 60,
                "retry": None,
            }

            acl.save_predefined(**kwargs)
            m.assert_called_once_with(**kwargs)


class _Blob(object):
    user_project = None

    def __init__(self, bucket, blob):
        self.bucket = bucket
        self.blob = blob

    @property
    def path(self):
        return f"{self.bucket.path}/o/{self.blob}"


class _Bucket(object):
    user_project = None

    def __init__(self, name):
        self.name = name

    @property
    def path(self):
        return f"/b/{self.name}"
