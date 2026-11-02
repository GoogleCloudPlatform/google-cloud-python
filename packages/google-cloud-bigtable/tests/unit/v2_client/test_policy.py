# Copyright 2018 Google LLC
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


def _make_policy(*args, **kw):
    from google.cloud.bigtable.policy import Policy

    return Policy(*args, **kw)


def test_policy_ctor_defaults():
    empty = frozenset()
    policy = _make_policy()
    assert policy.etag is None
    assert policy.version is None
    assert policy.bigtable_admins == empty
    assert policy.bigtable_readers == empty
    assert policy.bigtable_users == empty
    assert policy.bigtable_viewers == empty
    assert len(policy) == 0
    assert dict(policy) == {}


def test_policy_ctor_explicit():
    VERSION = 1
    ETAG = b"ETAG"
    empty = frozenset()
    policy = _make_policy(ETAG, VERSION)
    assert policy.etag == ETAG
    assert policy.version == VERSION
    assert policy.bigtable_admins == empty
    assert policy.bigtable_readers == empty
    assert policy.bigtable_users == empty
    assert policy.bigtable_viewers == empty
    assert len(policy) == 0
    assert dict(policy) == {}


def test_policy_bigtable_admins():
    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    MEMBER = "user:phred@example.com"
    expected = frozenset([MEMBER])
    policy = _make_policy()
    policy[BIGTABLE_ADMIN_ROLE] = [MEMBER]
    assert policy.bigtable_admins == expected


def test_policy_bigtable_readers():
    from google.cloud.bigtable.policy import BIGTABLE_READER_ROLE

    MEMBER = "user:phred@example.com"
    expected = frozenset([MEMBER])
    policy = _make_policy()
    policy[BIGTABLE_READER_ROLE] = [MEMBER]
    assert policy.bigtable_readers == expected


def test_policy_bigtable_users():
    from google.cloud.bigtable.policy import BIGTABLE_USER_ROLE

    MEMBER = "user:phred@example.com"
    expected = frozenset([MEMBER])
    policy = _make_policy()
    policy[BIGTABLE_USER_ROLE] = [MEMBER]
    assert policy.bigtable_users == expected


def test_policy_bigtable_viewers():
    from google.cloud.bigtable.policy import BIGTABLE_VIEWER_ROLE

    MEMBER = "user:phred@example.com"
    expected = frozenset([MEMBER])
    policy = _make_policy()
    policy[BIGTABLE_VIEWER_ROLE] = [MEMBER]
    assert policy.bigtable_viewers == expected


def test_policy_from_pb_w_empty():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import Policy

    empty = frozenset()
    message = policy_pb2.Policy()
    policy = Policy.from_pb(message)
    assert policy.etag == b""
    assert policy.version == 0
    assert policy.bigtable_admins == empty
    assert policy.bigtable_readers == empty
    assert policy.bigtable_users == empty
    assert policy.bigtable_viewers == empty
    assert len(policy) == 0
    assert dict(policy) == {}


def test_policy_from_pb_w_non_empty():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy

    ETAG = b"ETAG"
    VERSION = 1
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    empty = frozenset()
    message = policy_pb2.Policy(
        etag=ETAG,
        version=VERSION,
        bindings=[{"role": BIGTABLE_ADMIN_ROLE, "members": members}],
    )
    policy = Policy.from_pb(message)
    assert policy.etag == ETAG
    assert policy.version == VERSION
    assert policy.bigtable_admins == set(members)
    assert policy.bigtable_readers == empty
    assert policy.bigtable_users == empty
    assert policy.bigtable_viewers == empty
    assert len(policy) == 1
    assert dict(policy) == {BIGTABLE_ADMIN_ROLE: set(members)}


def test_policy_from_pb_w_condition():
    import pytest
    from google.api_core.iam import _DICT_ACCESS_MSG, InvalidOperationException
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy

    ETAG = b"ETAG"
    VERSION = 3
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    BINDINGS = [
        {
            "role": BIGTABLE_ADMIN_ROLE,
            "members": members,
            "condition": {
                "title": "request_time",
                "description": "Requests made before 2021-01-01T00:00:00Z",
                "expression": 'request.time < timestamp("2021-01-01T00:00:00Z")',
            },
        }
    ]
    message = policy_pb2.Policy(
        etag=ETAG,
        version=VERSION,
        bindings=BINDINGS,
    )
    policy = Policy.from_pb(message)
    assert policy.etag == ETAG
    assert policy.version == VERSION
    assert policy.bindings[0]["role"] == BIGTABLE_ADMIN_ROLE
    assert policy.bindings[0]["members"] == set(members)
    assert policy.bindings[0]["condition"] == BINDINGS[0]["condition"]
    with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
        policy.bigtable_admins
    with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
        policy.bigtable_readers
    with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
        policy.bigtable_users
    with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
        policy.bigtable_viewers
    with pytest.raises(InvalidOperationException, match=_DICT_ACCESS_MSG):
        len(policy)


def test_policy_to_pb_empty():
    from google.iam.v1 import policy_pb2

    policy = _make_policy()
    expected = policy_pb2.Policy()

    assert policy.to_pb() == expected


def test_policy_to_pb_explicit():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    VERSION = 1
    ETAG = b"ETAG"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    policy = _make_policy(ETAG, VERSION)
    policy[BIGTABLE_ADMIN_ROLE] = members
    expected = policy_pb2.Policy(
        etag=ETAG,
        version=VERSION,
        bindings=[
            policy_pb2.Binding(role=BIGTABLE_ADMIN_ROLE, members=sorted(members))
        ],
    )

    assert policy.to_pb() == expected


def test_policy_to_pb_w_condition():
    from google.iam.v1 import policy_pb2

    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    VERSION = 3
    ETAG = b"ETAG"
    members = ["serviceAccount:service_acc1@test.com", "user:user1@test.com"]
    condition = {
        "title": "request_time",
        "description": "Requests made before 2021-01-01T00:00:00Z",
        "expression": 'request.time < timestamp("2021-01-01T00:00:00Z")',
    }
    policy = _make_policy(ETAG, VERSION)
    policy.bindings = [
        {"role": BIGTABLE_ADMIN_ROLE, "members": set(members), "condition": condition}
    ]
    expected = policy_pb2.Policy(
        etag=ETAG,
        version=VERSION,
        bindings=[
            policy_pb2.Binding(
                role=BIGTABLE_ADMIN_ROLE,
                members=sorted(members),
                condition=condition,
            )
        ],
    )

    assert policy.to_pb() == expected


def test_policy_from_api_repr_wo_etag():
    from google.cloud.bigtable.policy import Policy

    VERSION = 1
    empty = frozenset()
    resource = {"version": VERSION}
    policy = Policy.from_api_repr(resource)
    assert policy.etag is None
    assert policy.version == VERSION
    assert policy.bigtable_admins == empty
    assert policy.bigtable_readers == empty
    assert policy.bigtable_users == empty
    assert policy.bigtable_viewers == empty
    assert len(policy) == 0
    assert dict(policy) == {}


def test_policy_from_api_repr_w_etag():
    import base64

    from google.cloud.bigtable.policy import Policy

    ETAG = b"ETAG"
    empty = frozenset()
    resource = {"etag": base64.b64encode(ETAG).decode("ascii")}
    policy = Policy.from_api_repr(resource)
    assert policy.etag == ETAG
    assert policy.version is None
    assert policy.bigtable_admins == empty
    assert policy.bigtable_readers == empty
    assert policy.bigtable_users == empty
    assert policy.bigtable_viewers == empty
    assert len(policy) == 0
    assert dict(policy) == {}


def test_policy_to_api_repr_wo_etag():
    VERSION = 1
    resource = {"version": VERSION}
    policy = _make_policy(version=VERSION)
    assert policy.to_api_repr() == resource


def test_policy_to_api_repr_w_etag():
    import base64

    ETAG = b"ETAG"
    policy = _make_policy(etag=ETAG)
    resource = {"etag": base64.b64encode(ETAG).decode("ascii")}
    assert policy.to_api_repr() == resource
