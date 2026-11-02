# Copyright 2022 Google LLC
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

from gapic.schema import wrappers

import gc
import json
import uuid
import weakref
import proto
import pytest


class RoutingTestRequest(proto.Message):
    table_name = proto.Field(proto.STRING, number=1)
    app_profile_id = proto.Field(proto.STRING, number=2)


@pytest.mark.parametrize(
    "req, expected",
    [
        (RoutingTestRequest(app_profile_id="foo.123"), {"app_profile_id": "foo.123"}),
        (
            RoutingTestRequest(app_profile_id="projects/100"),
            {"app_profile_id": "projects/100"},
        ),
        (RoutingTestRequest(app_profile_id=""), {"app_profile_id": ""}),
    ],
)
def test_routing_rule_resolve_simple_extraction(req, expected):
    rule = wrappers.RoutingRule([wrappers.RoutingParameter("app_profile_id", "")])
    assert (
        wrappers.RoutingRule.resolve(rule, RoutingTestRequest.to_dict(req)) == expected
    )


@pytest.mark.parametrize(
    "req, expected",
    [
        (RoutingTestRequest(app_profile_id="foo.123"), {"routing_id": "foo.123"}),
        (
            RoutingTestRequest(app_profile_id="projects/100"),
            {"routing_id": "projects/100"},
        ),
        (RoutingTestRequest(app_profile_id=""), {"routing_id": ""}),
    ],
)
def test_routing_rule_resolve_rename_extraction(req, expected):
    rule = wrappers.RoutingRule(
        [wrappers.RoutingParameter("app_profile_id", "{routing_id=**}")]
    )
    assert (
        wrappers.RoutingRule.resolve(rule, RoutingTestRequest.to_dict(req)) == expected
    )


@pytest.mark.parametrize(
    "req, expected",
    [
        (
            RoutingTestRequest(table_name="projects/100/instances/200"),
            {"table_name": "projects/100/instances/200"},
        ),
        (
            RoutingTestRequest(table_name="projects/100/instances/200/whatever"),
            {"table_name": "projects/100/instances/200/whatever"},
        ),
        (RoutingTestRequest(table_name="foo"), {}),
    ],
)
def test_routing_rule_resolve_field_match(req, expected):
    rule = wrappers.RoutingRule(
        [
            wrappers.RoutingParameter(
                "table_name", "{table_name=projects/*/instances/*/**}"
            ),
            wrappers.RoutingParameter(
                "table_name", "{table_name=regions/*/zones/*/**}"
            ),
        ]
    )
    assert (
        wrappers.RoutingRule.resolve(rule, RoutingTestRequest.to_dict(req)) == expected
    )


@pytest.mark.parametrize(
    "routing_parameters, req, expected",
    [
        (
            [
                wrappers.RoutingParameter(
                    "table_name", "{project_id=projects/*}/instances/*/**"
                )
            ],
            RoutingTestRequest(table_name="projects/100/instances/200/tables/300"),
            {"project_id": "projects/100"},
        ),
        (
            [
                wrappers.RoutingParameter(
                    "table_name", "{project_id=projects/*}/instances/*/**"
                ),
                wrappers.RoutingParameter(
                    "table_name", "projects/*/{instance_id=instances/*}/**"
                ),
                wrappers.RoutingParameter(
                    "doesnotexist", "projects/*/{instance_id=instances/*}/**"
                ),
            ],
            RoutingTestRequest(table_name="projects/100/instances/200/tables/300"),
            {"project_id": "projects/100", "instance_id": "instances/200"},
        ),
    ],
)
def test_routing_rule_resolve(routing_parameters, req, expected):
    rule = wrappers.RoutingRule(routing_parameters)
    got = wrappers.RoutingRule.resolve(rule, RoutingTestRequest.to_dict(req))
    assert got == expected

    rule = wrappers.RoutingRule(routing_parameters)
    got = wrappers.RoutingRule.resolve(
        rule, json.dumps(RoutingTestRequest.to_dict(req))
    )
    assert got == expected


@pytest.mark.parametrize(
    "field, path_template, expected",
    [
        ("table_name", "{project_id=projects/*}/instances/*/**", "project_id"),
        ("table_name", "projects/*/{instance_id=instances/*}/**", "instance_id"),
        ("table_name", "projects/*/{instance_id}/**", "instance_id"),
    ],
)
def test_routing_parameter_key(field, path_template, expected):
    param = wrappers.RoutingParameter(field, path_template)
    assert param.key == expected


def test_routing_parameter_cache_does_not_retain_instance():
    unique_id = f"id_{uuid.uuid4().hex}"
    param = wrappers.RoutingParameter(
        f"table_name_{unique_id}", f"{{{unique_id}=projects/*}}/instances/*/**"
    )
    _ = param.to_regex()
    _ = param.key
    param_ref = weakref.ref(param)

    del param
    gc.collect()

    assert param_ref() is None


def test_routing_parameter_multi_segment_raises():
    param = wrappers.RoutingParameter(
        "table_name", "{project_id=projects/*}/{instance_id=instances/*}/*/**"
    )
    with pytest.raises(ValueError):
        param.key
