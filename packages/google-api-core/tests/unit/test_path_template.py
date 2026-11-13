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

from __future__ import unicode_literals

from unittest import mock

import pytest
from google.api import auth_pb2

from google.api_core import path_template


@pytest.mark.parametrize(
    "tmpl, args, kwargs, expected_result",
    [
        # Basic positional params
        ["/v1/*", ["a"], {}, "/v1/a"],
        ["/v1/**", ["a/b"], {}, "/v1/a/b"],
        ["/v1/*/*", ["a", "b"], {}, "/v1/a/b"],
        ["/v1/*/*/**", ["a", "b", "c/d"], {}, "/v1/a/b/c/d"],
        # Basic named params
        ["/v1/{name}", [], {"name": "parent"}, "/v1/parent"],
        ["/v1/{name=**}", [], {"name": "parent/child"}, "/v1/parent/child"],
        # Named params with a sub-template
        ["/v1/{name=parent/*}", [], {"name": "parent/child"}, "/v1/parent/child"],
        [
            "/v1/{name=parent/**}",
            [],
            {"name": "parent/child/object"},
            "/v1/parent/child/object",
        ],
        # Combining positional and named params
        ["/v1/*/{name}", ["a"], {"name": "parent"}, "/v1/a/parent"],
        ["/v1/{name}/*", ["a"], {"name": "parent"}, "/v1/parent/a"],
        [
            "/v1/{parent}/*/{child}/*",
            ["a", "b"],
            {"parent": "thor", "child": "thorson"},
            "/v1/thor/a/thorson/b",
        ],
        ["/v1/{name}/**", ["a/b"], {"name": "parent"}, "/v1/parent/a/b"],
        # Combining positional and named params with sub-templates.
        [
            "/v1/{name=parent/*}/*",
            ["a"],
            {"name": "parent/child"},
            "/v1/parent/child/a",
        ],
        [
            "/v1/*/{name=parent/**}",
            ["a"],
            {"name": "parent/child/object"},
            "/v1/a/parent/child/object",
        ],
        # Legitimate resource name patterns preserved in expand
        [
            "projects/{project}/databases/{database}",
            [],
            {"project": "my-project", "database": "(default)"},
            "projects/my-project/databases/(default)",
        ],
        [
            "/v1/{name}",
            [],
            {"name": "my-instance:cluster-1"},
            "/v1/my-instance:cluster-1",
        ],
        [
            "projects/{project}/serviceAccounts/{account}",
            [],
            {
                "project": "my-project",
                "account": "service@my-project.iam.gserviceaccount.com",
            },
            "projects/my-project/serviceAccounts/service@my-project.iam.gserviceaccount.com",
        ],
    ],
)
def test_expand_success(tmpl, args, kwargs, expected_result):
    result = path_template.expand(tmpl, *args, **kwargs)
    assert result == expected_result
    assert path_template.validate(tmpl, result)


@pytest.mark.parametrize(
    "tmpl, args, kwargs, exc_match",
    [
        # Missing positional arg.
        ["v1/*", [], {}, "Positional"],
        # Missing named arg.
        ["v1/{name}", [], {}, "Named"],
    ],
)
def test_expanded_failure(tmpl, args, kwargs, exc_match):
    with pytest.raises(ValueError, match=exc_match):
        path_template.expand(tmpl, *args, **kwargs)


@pytest.mark.parametrize(
    "request_obj, field, expected_result",
    [
        [{"field": "stringValue"}, "field", "stringValue"],
        [{"field": "stringValue"}, "nosuchfield", None],
        [{"field": "stringValue"}, "field.subfield", None],
        [{"field": {"subfield": "stringValue"}}, "field", None],
        [{"field": {"subfield": "stringValue"}}, "field.subfield", "stringValue"],
        [{"field": {"subfield": [1, 2, 3]}}, "field.subfield", [1, 2, 3]],
        [{"field": {"subfield": "stringValue"}}, "field", None],
        [{"field": {"subfield": "stringValue"}}, "field.nosuchfield", None],
        [
            {"field": {"subfield": {"subsubfield": "stringValue"}}},
            "field.subfield.subsubfield",
            "stringValue",
        ],
        ["string", "field", None],
    ],
)
def test_get_field(request_obj, field, expected_result):
    result = path_template.get_field(request_obj, field)
    assert result == expected_result


def test_get_field_encode():
    assert (
        path_template.get_field({"name": "a$b?c=d#e f"}, "name", encode=True)
        == "a%24b%3Fc%3Dd%23e%20f"
    )
    assert (
        path_template.get_field({"name": "abc-._~"}, "name", encode=True) == "abc-._~"
    )
    assert path_template.get_field({"name": None}, "name", encode=True) is None
    assert path_template.get_field({}, "name", encode=True) is None


@pytest.mark.parametrize(
    "request_obj, field, expected_result",
    [
        [{"field": "stringValue"}, "field", {}],
        [{"field": "stringValue"}, "nosuchfield", {"field": "stringValue"}],
        [{"field": "stringValue"}, "field.subfield", {"field": "stringValue"}],
        [{"field": {"subfield": "stringValue"}}, "field.subfield", {"field": {}}],
        [
            {"field": {"subfield": "stringValue", "q": "w"}, "e": "f"},
            "field.subfield",
            {"field": {"q": "w"}, "e": "f"},
        ],
        [
            {"field": {"subfield": "stringValue"}},
            "field.nosuchfield",
            {"field": {"subfield": "stringValue"}},
        ],
        [
            {"field": {"subfield": {"subsubfield": "stringValue", "q": "w"}}},
            "field.subfield.subsubfield",
            {"field": {"subfield": {"q": "w"}}},
        ],
        ["string", "field", "string"],
        ["string", "field.subfield", "string"],
    ],
)
def test_delete_field(request_obj, field, expected_result):
    path_template.delete_field(request_obj, field)
    assert request_obj == expected_result


@pytest.mark.parametrize(
    "tmpl, path",
    [
        # Single segment template, but multi segment value
        ["v1/*", "v1/a/b"],
        ["v1/*/*", "v1/a/b/c"],
        # Single segement named template, but multi segment value
        ["v1/{name}", "v1/a/b"],
        ["v1/{name}/{value}", "v1/a/b/c"],
        # Named value with a sub-template but invalid value
        ["v1/{name=parent/*}", "v1/grandparent/child"],
    ],
)
def test_validate_failure(tmpl, path):
    assert not path_template.validate(tmpl, path)


def test__expand_variable_match_unexpected():
    match = mock.Mock(spec=["group"])
    match.group.return_value = None
    with pytest.raises(ValueError, match="Unknown"):
        path_template._expand_variable_match([], {}, match)


def test__replace_variable_with_pattern():
    match = mock.Mock(spec=["group"])
    match.group.return_value = None
    with pytest.raises(ValueError, match="Unknown"):
        path_template._replace_variable_with_pattern(match)


@pytest.mark.parametrize(
    "http_options, message, request_kwargs, expected_result",
    [
        [
            [["get", "/v1/no/template", ""]],
            None,
            {"foo": "bar"},
            ["get", "/v1/no/template", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/no/template", ""]],
            auth_pb2.AuthenticationRule(selector="bar"),
            {},
            [
                "get",
                "/v1/no/template",
                None,
                auth_pb2.AuthenticationRule(selector="bar"),
            ],
        ],
        # Single templates
        [
            [["get", "/v1/{field}", ""]],
            None,
            {"field": "parent"},
            ["get", "/v1/parent", {}, {}],
        ],
        [
            [["get", "/v1/{selector}", ""]],
            auth_pb2.AuthenticationRule(selector="parent"),
            {},
            ["get", "/v1/parent", None, auth_pb2.AuthenticationRule()],
        ],
        [
            [["get", "/v1/{field.sub}", ""]],
            None,
            {"field": {"sub": "parent"}, "foo": "bar"},
            ["get", "/v1/parent", {}, {"field": {}, "foo": "bar"}],
        ],
        [
            [["get", "/v1/{oauth.canonical_scopes}", ""]],
            auth_pb2.AuthenticationRule(
                selector="bar",
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="parent"),
            ),
            {},
            [
                "get",
                "/v1/parent",
                None,
                auth_pb2.AuthenticationRule(
                    selector="bar", oauth=auth_pb2.OAuthRequirements()
                ),
            ],
        ],
    ],
)
def test_transcode_base_case(http_options, message, request_kwargs, expected_result):
    http_options, expected_result = helper_test_transcode(http_options, expected_result)
    result = path_template.transcode(http_options, message, **request_kwargs)
    assert result == expected_result


@pytest.mark.parametrize(
    "http_options, message, request_kwargs, expected_result",
    [
        [
            [["get", "/v1/{field.subfield}", ""]],
            None,
            {"field": {"subfield": "parent"}, "foo": "bar"},
            ["get", "/v1/parent", {}, {"field": {}, "foo": "bar"}],
        ],
        [
            [["get", "/v1/{oauth.canonical_scopes}", ""]],
            auth_pb2.AuthenticationRule(
                selector="bar",
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="parent"),
            ),
            {},
            [
                "get",
                "/v1/parent",
                None,
                auth_pb2.AuthenticationRule(
                    selector="bar", oauth=auth_pb2.OAuthRequirements()
                ),
            ],
        ],
        [
            [["get", "/v1/{field.subfield.subsubfield}", ""]],
            None,
            {"field": {"subfield": {"subsubfield": "parent"}}, "foo": "bar"},
            ["get", "/v1/parent", {}, {"field": {"subfield": {}}, "foo": "bar"}],
        ],
        [
            [["get", "/v1/{field.subfield1}/{field.subfield2}", ""]],
            None,
            {"field": {"subfield1": "parent", "subfield2": "child"}, "foo": "bar"},
            ["get", "/v1/parent/child", {}, {"field": {}, "foo": "bar"}],
        ],
        [
            [["get", "/v1/{selector}/{oauth.canonical_scopes}", ""]],
            auth_pb2.AuthenticationRule(
                selector="parent",
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="child"),
            ),
            {"field": {"subfield1": "parent", "subfield2": "child"}, "foo": "bar"},
            [
                "get",
                "/v1/parent/child",
                None,
                auth_pb2.AuthenticationRule(oauth=auth_pb2.OAuthRequirements()),
            ],
        ],
    ],
)
def test_transcode_subfields(http_options, message, request_kwargs, expected_result):
    http_options, expected_result = helper_test_transcode(http_options, expected_result)
    result = path_template.transcode(http_options, message, **request_kwargs)
    assert result == expected_result


@pytest.mark.parametrize(
    "http_options, message, request_kwargs, expected_result",
    [
        # Single segment wildcard
        [
            [["get", "/v1/{field=*}", ""]],
            None,
            {"field": "parent"},
            ["get", "/v1/parent", {}, {}],
        ],
        [
            [["get", "/v1/{selector=*}", ""]],
            auth_pb2.AuthenticationRule(selector="parent"),
            {},
            ["get", "/v1/parent", None, auth_pb2.AuthenticationRule()],
        ],
        [
            [["get", "/v1/{field=a/*/b/*}", ""]],
            None,
            {"field": "a/parent/b/child", "foo": "bar"},
            ["get", "/v1/a/parent/b/child", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{selector=a/*/b/*}", ""]],
            auth_pb2.AuthenticationRule(
                selector="a/parent/b/child", allow_without_credential=True
            ),
            {},
            [
                "get",
                "/v1/a/parent/b/child",
                None,
                auth_pb2.AuthenticationRule(allow_without_credential=True),
            ],
        ],
        # Double segment wildcard
        [
            [["get", "/v1/{field=**}", ""]],
            None,
            {"field": "parent/p1"},
            ["get", "/v1/parent/p1", {}, {}],
        ],
        [
            [["get", "/v1/{selector=**}", ""]],
            auth_pb2.AuthenticationRule(selector="parent/p1"),
            {},
            ["get", "/v1/parent/p1", None, auth_pb2.AuthenticationRule()],
        ],
        [
            [["get", "/v1/{field=a/**/b/**}", ""]],
            None,
            {"field": "a/parent/p1/b/child/c1", "foo": "bar"},
            ["get", "/v1/a/parent/p1/b/child/c1", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{selector=a/**/b/**}", ""]],
            auth_pb2.AuthenticationRule(
                selector="a/parent/p1/b/child/c1", allow_without_credential=True
            ),
            {},
            [
                "get",
                "/v1/a/parent/p1/b/child/c1",
                None,
                auth_pb2.AuthenticationRule(allow_without_credential=True),
            ],
        ],
        # Combined single and double segment wildcard
        [
            [["get", "/v1/{field=a/*/b/**}", ""]],
            None,
            {"field": "a/parent/b/child/c1"},
            ["get", "/v1/a/parent/b/child/c1", {}, {}],
        ],
        [
            [["get", "/v1/{selector=a/*/b/**}", ""]],
            auth_pb2.AuthenticationRule(selector="a/parent/b/child/c1"),
            {},
            ["get", "/v1/a/parent/b/child/c1", None, auth_pb2.AuthenticationRule()],
        ],
        [
            [["get", "/v1/{field=a/**/b/*}/v2/{name}", ""]],
            None,
            {"field": "a/parent/p1/b/child", "name": "first", "foo": "bar"},
            ["get", "/v1/a/parent/p1/b/child/v2/first", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{selector=a/**/b/*}/v2/{oauth.canonical_scopes}", ""]],
            auth_pb2.AuthenticationRule(
                selector="a/parent/p1/b/child",
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="first"),
            ),
            {"field": "a/parent/p1/b/child", "name": "first", "foo": "bar"},
            [
                "get",
                "/v1/a/parent/p1/b/child/v2/first",
                None,
                auth_pb2.AuthenticationRule(oauth=auth_pb2.OAuthRequirements()),
            ],
        ],
        # Special characters, colons, and parentheses in URI variable transcoding
        [
            [["get", "/v1/projects/{p}/databases/{d}", ""]],
            None,
            {"p": "proj", "d": "(default)", "foo": "bar"},
            ["get", "/v1/projects/proj/databases/%28default%29", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{name}", ""]],
            None,
            {"name": "inst:1", "foo": "bar"},
            ["get", "/v1/inst%3A1", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{name}", ""]],
            None,
            {"name": "a$b?c=d#e f", "foo": "bar"},
            ["get", "/v1/a%24b%3Fc%3Dd%23e%20f", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{name}", ""]],
            None,
            {"name": "..?$httpMethod=DELETE#", "foo": "bar"},
            ["get", "/v1/..%3F%24httpMethod%3DDELETE%23", {}, {"foo": "bar"}],
        ],
        [
            [["get", "/v1/{name=**}", ""]],
            None,
            {"name": "sub/?and#", "foo": "bar"},
            ["get", "/v1/sub/%3Fand%23", {}, {"foo": "bar"}],
        ],
        [
            [["post", "/v1/{name=a/*}:verb", ""]],
            None,
            {"name": "a/..?$httpMethod=DELETE#", "foo": "bar"},
            ["post", "/v1/a/..%3F%24httpMethod%3DDELETE%23:verb", {}, {"foo": "bar"}],
        ],
    ],
)
def test_transcode_with_wildcard(
    http_options, message, request_kwargs, expected_result
):
    http_options, expected_result = helper_test_transcode(http_options, expected_result)
    result = path_template.transcode(http_options, message, **request_kwargs)
    assert result == expected_result


@pytest.mark.parametrize(
    "http_options, message, request_kwargs, expected_result",
    [
        # Single field body
        [
            [["post", "/v1/no/template", "data"]],
            None,
            {"data": {"id": 1, "info": "some info"}, "foo": "bar"},
            ["post", "/v1/no/template", {"id": 1, "info": "some info"}, {"foo": "bar"}],
        ],
        [
            [["post", "/v1/no/template", "oauth"]],
            auth_pb2.AuthenticationRule(
                selector="bar",
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="child"),
            ),
            {},
            [
                "post",
                "/v1/no/template",
                auth_pb2.OAuthRequirements(canonical_scopes="child"),
                auth_pb2.AuthenticationRule(selector="bar"),
            ],
        ],
        [
            [["post", "/v1/{field=a/*}/b/{name=**}", "data"]],
            None,
            {
                "field": "a/parent",
                "name": "first/last",
                "data": {"id": 1, "info": "some info"},
                "foo": "bar",
            },
            [
                "post",
                "/v1/a/parent/b/first/last",
                {"id": 1, "info": "some info"},
                {"foo": "bar"},
            ],
        ],
        [
            [["post", "/v1/{selector=a/*}/b/{oauth.canonical_scopes=**}", "oauth"]],
            auth_pb2.AuthenticationRule(
                selector="a/parent",
                allow_without_credential=True,
                requirements=[auth_pb2.AuthRequirement(provider_id="p")],
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="first/last"),
            ),
            {},
            [
                "post",
                "/v1/a/parent/b/first/last",
                auth_pb2.OAuthRequirements(),
                auth_pb2.AuthenticationRule(
                    requirements=[auth_pb2.AuthRequirement(provider_id="p")],
                    allow_without_credential=True,
                ),
            ],
        ],
        # Wildcard body
        [
            [["post", "/v1/{field=a/*}/b/{name=**}", "*"]],
            None,
            {
                "field": "a/parent",
                "name": "first/last",
                "data": {"id": 1, "info": "some info"},
                "foo": "bar",
            },
            [
                "post",
                "/v1/a/parent/b/first/last",
                {"data": {"id": 1, "info": "some info"}, "foo": "bar"},
                {},
            ],
        ],
        [
            [["post", "/v1/{selector=a/*}/b/{oauth.canonical_scopes=**}", "*"]],
            auth_pb2.AuthenticationRule(
                selector="a/parent",
                allow_without_credential=True,
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="first/last"),
            ),
            {
                "field": "a/parent",
                "name": "first/last",
                "data": {"id": 1, "info": "some info"},
                "foo": "bar",
            },
            [
                "post",
                "/v1/a/parent/b/first/last",
                auth_pb2.AuthenticationRule(
                    allow_without_credential=True, oauth=auth_pb2.OAuthRequirements()
                ),
                auth_pb2.AuthenticationRule(),
            ],
        ],
    ],
)
def test_transcode_with_body(http_options, message, request_kwargs, expected_result):
    http_options, expected_result = helper_test_transcode(http_options, expected_result)
    result = path_template.transcode(http_options, message, **request_kwargs)
    assert result == expected_result


@pytest.mark.parametrize(
    "http_options, message, request_kwargs, expected_result",
    [
        # Additional bindings
        [
            [
                ["post", "/v1/{field=a/*}/b/{name=**}", "extra_data"],
                ["post", "/v1/{field=a/*}/b/{name=**}", "*"],
            ],
            None,
            {
                "field": "a/parent",
                "name": "first/last",
                "data": {"id": 1, "info": "some info"},
                "foo": "bar",
            },
            [
                "post",
                "/v1/a/parent/b/first/last",
                {"data": {"id": 1, "info": "some info"}, "foo": "bar"},
                {},
            ],
        ],
        [
            [
                [
                    "post",
                    "/v1/{selector=a/*}/b/{oauth.canonical_scopes=**}",
                    "extra_data",
                ],
                ["post", "/v1/{selector=a/*}/b/{oauth.canonical_scopes=**}", "*"],
            ],
            auth_pb2.AuthenticationRule(
                selector="a/parent",
                allow_without_credential=True,
                oauth=auth_pb2.OAuthRequirements(canonical_scopes="first/last"),
            ),
            {},
            [
                "post",
                "/v1/a/parent/b/first/last",
                auth_pb2.AuthenticationRule(
                    allow_without_credential=True, oauth=auth_pb2.OAuthRequirements()
                ),
                auth_pb2.AuthenticationRule(),
            ],
        ],
        [
            [
                ["get", "/v1/{field=a/*}/b/{name=**}", ""],
                ["get", "/v1/{field=a/*}/b/first/last", ""],
            ],
            None,
            {"field": "a/parent", "foo": "bar"},
            ["get", "/v1/a/parent/b/first/last", {}, {"foo": "bar"}],
        ],
        [
            [
                ["get", "/v1/{selector=a/*}/b/{oauth.allow_without_credential=**}", ""],
                ["get", "/v1/{selector=a/*}/b/first/last", ""],
            ],
            auth_pb2.AuthenticationRule(
                selector="a/parent",
                allow_without_credential=True,
                oauth=auth_pb2.OAuthRequirements(),
            ),
            {},
            [
                "get",
                "/v1/a/parent/b/first/last",
                None,
                auth_pb2.AuthenticationRule(
                    allow_without_credential=True, oauth=auth_pb2.OAuthRequirements()
                ),
            ],
        ],
    ],
)
def test_transcode_with_additional_bindings(
    http_options, message, request_kwargs, expected_result
):
    http_options, expected_result = helper_test_transcode(http_options, expected_result)
    result = path_template.transcode(http_options, message, **request_kwargs)
    assert result == expected_result


@pytest.mark.parametrize(
    "http_options, message, request_kwargs",
    [
        [[["get", "/v1/{name}", ""]], None, {"foo": "bar"}],
        [[["get", "/v1/{selector}", ""]], auth_pb2.AuthenticationRule(), {}],
        [[["get", "/v1/{name}", ""]], auth_pb2.AuthenticationRule(), {}],
        [[["get", "/v1/{name}", ""]], None, {"name": "first/last"}],
        [
            [["get", "/v1/{selector}", ""]],
            auth_pb2.AuthenticationRule(selector="first/last"),
            {},
        ],
        [[["get", "/v1/{name=mr/*/*}", ""]], None, {"name": "first/last"}],
        [
            [["get", "/v1/{selector=mr/*/*}", ""]],
            auth_pb2.AuthenticationRule(selector="first/last"),
            {},
        ],
        [[["post", "/v1/{name}", "data"]], None, {"name": "first/last"}],
        [
            [["post", "/v1/{selector}", "data"]],
            auth_pb2.AuthenticationRule(selector="first"),
            {},
        ],
        [[["post", "/v1/{first_name}", "data"]], None, {"last_name": "last"}],
        [
            [["post", "/v1/{first_name}", ""]],
            auth_pb2.AuthenticationRule(selector="first"),
            {},
        ],
    ],
)
def test_transcode_fails(http_options, message, request_kwargs):
    http_options, _ = helper_test_transcode(http_options, range(4))
    with pytest.raises(ValueError) as exc_info:
        path_template.transcode(http_options, message, **request_kwargs)
    assert str(exc_info.value).count("URI") == len(http_options)


def helper_test_transcode(http_options_list, expected_result_list):
    http_options = []
    for opt_list in http_options_list:
        http_option = {"method": opt_list[0], "uri": opt_list[1]}
        if opt_list[2]:
            http_option["body"] = opt_list[2]
        http_options.append(http_option)

    expected_result = {
        "method": expected_result_list[0],
        "uri": expected_result_list[1],
        "query_params": expected_result_list[3],
    }
    if expected_result_list[2]:
        expected_result["body"] = expected_result_list[2]
    return (http_options, expected_result)


@pytest.mark.parametrize(
    "tmpl, args, kwargs, expected_err_match",
    [
        # Positional * with . or ..
        [
            "/v1/*",
            ["."],
            {},
            r"^Invalid value \. for positional variable\.$",
        ],
        [
            "/v1/*",
            [".."],
            {},
            r"^Invalid value \.\. for positional variable\.$",
        ],
        # Named matching * with . or ..
        [
            "/compute/v1/projects/{project}/regions/{region}/addresses",
            [],
            {"project": "my-project", "region": ".."},
            r"^Invalid value \.\. for region\.$",
        ],
        [
            "/compute/v1/projects/{project}/regions/{region}/addresses",
            [],
            {"project": "my-project", "region": "."},
            r"^Invalid value \. for region\.$",
        ],
        # Sub-template named matching * with . or ..
        [
            "/v2/{parent=projects/*/locations/*}/content:inspect",
            [],
            {"parent": "projects/my-project/locations/.."},
            r"^Value for parent must not contain segments that are exactly \. or \.\. \.$",
        ],
        [
            "/v2/{parent=projects/*/locations/*}/content:inspect",
            [],
            {"parent": "projects/my-project/locations/."},
            r"^Value for parent must not contain segments that are exactly \. or \.\. \.$",
        ],
        [
            "/v2/{parent=projects/*/locations/*}/content:inspect",
            [],
            {"parent": "projects/../locations/us-central1"},
            r"^Value for parent must not contain segments that are exactly \. or \.\. \.$",
        ],
        [
            "/v2/{parent=projects/*/locations/*}/content:inspect",
            [],
            {"parent": "projects/./locations/us-central1"},
            r"^Value for parent must not contain segments that are exactly \. or \.\. \.$",
        ],
    ],
)
def test_path_traversal_dots_validation_star(tmpl, args, kwargs, expected_err_match):
    with pytest.raises(ValueError, match=expected_err_match):
        path_template.expand(tmpl, *args, **kwargs)


@pytest.mark.parametrize(
    "name_val, expected_path",
    [
        (
            "projects/my-project/monitoredResourceDescriptors/instance/my-instance",
            "/v3/projects/my-project/monitoredResourceDescriptors/instance/my-instance",
        ),
        (
            "projects/my-project/monitoredResourceDescriptors/a/b/c/d/e",
            "/v3/projects/my-project/monitoredResourceDescriptors/a/b/c/d/e",
        ),
        (
            "projects/my-project/monitoredResourceDescriptors/instance...foo/bar",
            "/v3/projects/my-project/monitoredResourceDescriptors/instance...foo/bar",
        ),
        (
            "projects/my-project/monitoredResourceDescriptors/...",
            "/v3/projects/my-project/monitoredResourceDescriptors/...",
        ),
    ],
)
def test_path_traversal_dots_validation_double_star_valid(name_val, expected_path):
    assert (
        path_template.expand(
            "/v3/{name=projects/*/monitoredResourceDescriptors/**}",
            name=name_val,
        )
        == expected_path
    )


@pytest.mark.parametrize(
    "name_val",
    [
        "projects/my-project/monitoredResourceDescriptors/instance/my-instance/..",
        "projects/my-project/monitoredResourceDescriptors/instance/my-instance/.",
        "projects/my-project/monitoredResourceDescriptors/instance/my-instance/../..",
        "projects/my-project/monitoredResourceDescriptors/instance/../my-instance/..",
        "projects/my-project/monitoredResourceDescriptors/instance/../..",
        "projects/my-project/monitoredResourceDescriptors/a/b/../../../c/d/e/..",
        "projects/my-project/monitoredResourceDescriptors/a/b/c/d/e/../../../..",
        "projects/my-project/monitoredResourceDescriptors/instance//..",
    ],
)
def test_path_traversal_dots_validation_double_star_invalid(name_val):
    with pytest.raises(
        ValueError,
        match=r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
    ):
        path_template.expand(
            "/v3/{name=projects/*/monitoredResourceDescriptors/**}",
            name=name_val,
        )


@pytest.mark.parametrize(
    "tmpl, args, kwargs, expected_err_match",
    [
        (
            "/v1/**",
            [".."],
            {},
            r"^Value for positional variable must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "/v1/**",
            ["a/./b"],
            {},
            r"^Value for positional variable must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "/v1/{name=**}",
            [],
            {"name": ".."},
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "/v1/{name=**}",
            [],
            {"name": "a/../b"},
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
    ],
)
def test_path_traversal_dots_validation_bare_double_star(
    tmpl, args, kwargs, expected_err_match
):
    with pytest.raises(ValueError, match=expected_err_match):
        path_template.expand(tmpl, *args, **kwargs)


@pytest.mark.parametrize(
    "name_val, expected_err_match",
    [
        (
            "projects/../locations/us-central1/buckets/my-bucket",
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "projects/my-project/locations/./buckets/my-bucket",
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "projects/my-project/locations/us-central1/buckets/foo/../bar",
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "projects/my-project/locations/us-central1/buckets/.",
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "projects/my-project/locations/us-central1/buckets/..",
            r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
        ),
    ],
)
def test_path_traversal_mixed_subtemplate(name_val, expected_err_match):
    tmpl = "/v1/{name=projects/*/locations/*/buckets/**}"
    with pytest.raises(ValueError, match=expected_err_match):
        path_template.expand(tmpl, name=name_val)


@pytest.mark.parametrize(
    "tmpl, args, kwargs, expected_err_match",
    [
        (
            "/v1/*/**",
            [".", "a/b"],
            {},
            r"^Invalid value \. for positional variable\.$",
        ),
        (
            "/v1/*/**",
            ["..", "a/b"],
            {},
            r"^Invalid value \.\. for positional variable\.$",
        ),
        (
            "/v1/*/**",
            ["a", "b/../c"],
            {},
            r"^Value for positional variable must not contain segments that are exactly \. or \.\. \.$",
        ),
        (
            "/v1/*/**",
            ["a", "b/./c"],
            {},
            r"^Value for positional variable must not contain segments that are exactly \. or \.\. \.$",
        ),
    ],
)
def test_path_traversal_multiple_positional_wildcards(
    tmpl, args, kwargs, expected_err_match
):
    with pytest.raises(ValueError, match=expected_err_match):
        path_template.expand(tmpl, *args, **kwargs)


@pytest.mark.parametrize(
    "tmpl, kwargs, expected_result",
    [
        ("/v1/{name}", {"name": ".hidden"}, "/v1/.hidden"),
        ("/v1/{name}", {"name": "..hidden"}, "/v1/..hidden"),
        ("/v1/{name}", {"name": "file.txt"}, "/v1/file.txt"),
        ("/v1/{name=**}", {"name": "a/.hidden/b"}, "/v1/a/.hidden/b"),
        ("/v1/{name=**}", {"name": "a/..hidden/b"}, "/v1/a/..hidden/b"),
        ("/v1/{name=**}", {"name": "a/file.tar.gz/b"}, "/v1/a/file.tar.gz/b"),
    ],
)
def test_valid_dot_containing_names(tmpl, kwargs, expected_result):
    assert path_template.expand(tmpl, **kwargs) == expected_result


def test_transcode_routing_with_path_traversal_fallback():
    http_options = [
        {"method": "get", "uri": "/v1/{name=projects/*/locations/*}"},
        {"method": "get", "uri": "/v1/{name=projects/*}"},
    ]

    # Non-matching subtemplate structure falls through to secondary binding
    result = path_template.transcode(http_options, None, name="projects/my-project")
    assert result["uri"] == "/v1/projects/my-project"

    # Structurally matching subtemplate with invalid dot segment raises immediately
    with pytest.raises(
        ValueError,
        match=r"^Value for name must not contain segments that are exactly \. or \.\. \.$",
    ):
        path_template.transcode(
            http_options, None, name="projects/my-project/locations/."
        )
