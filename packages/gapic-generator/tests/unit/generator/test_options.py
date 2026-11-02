# Copyright 2019 Google LLC
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

import os
import pytest
import re
from unittest import mock
import warnings

from gapic.samplegen_utils import types
from gapic.utils import Options


def test_options_empty():
    opts = Options.build("")
    assert len(opts.templates) == 1
    assert opts.templates[0].endswith("gapic/templates")
    assert not opts.lazy_import
    assert not opts.old_naming


def test_options_replace_templates():
    opts = Options.build("python-gapic-templates=/foo/")
    assert len(opts.templates) == 1
    assert opts.templates[0] == "/foo"


def test_options_relative_templates():
    opts = Options.build("python-gapic-templates=../../squid/clam")

    expected = (os.path.abspath("../squid/clam"),)
    assert opts.templates == expected


def test_options_unrecognized():
    with mock.patch.object(warnings, "warn") as warn:
        Options.build("python-gapic-abc=xyz")
    warn.assert_called_once_with("Unrecognized option: `python-gapic-abc`.")


def test_flags_unrecognized():
    with mock.patch.object(warnings, "warn") as warn:
        Options.build("python-gapic-abc")
    warn.assert_called_once_with("Unrecognized option: `python-gapic-abc`.")


def test_options_unrecognized_likely_typo():
    with mock.patch.object(warnings, "warn") as warn:
        Options.build("go-gapic-abc=xyz")
    assert len(warn.mock_calls) == 0


def test_options_trim_whitespace():
    # When writing shell scripts, users may construct options strings with
    # whitespace that needs to be trimmed after tokenizing.
    opts = Options.build(
        """
        python-gapic-templates=/squid/clam/whelk ,
        python-gapic-name=mollusca ,
        """
    )
    assert opts.templates[0] == "/squid/clam/whelk"
    assert opts.name == "mollusca"


def test_options_no_valid_sample_config(fs):
    fs.create_file("sampledir/not_a_config.yaml")
    with pytest.raises(types.InvalidConfig):
        Options.build("samples=sampledir/")


def test_options_service_config(fs):
    opts = Options.build("")
    assert opts.retry is None

    # Default of None is okay, verify build can read a config.
    service_config_fpath = "service_config.json"
    fs.create_file(
        service_config_fpath,
        contents="""{
    "methodConfig": [
        {
            "name": [
                {
                  "service": "animalia.mollusca.v1beta1.Cephalopod",
                  "method": "IdentifySquid"
                }
            ],
            "retryPolicy": {
                "maxAttempts": 5,
                "maxBackoff": "3s",
                "initialBackoff": "0.2s",
                "backoffMultiplier": 2,
                "retryableStatusCodes": [
                    "UNAVAILABLE",
                    "UNKNOWN"
                ]
            },
            "timeout": "5s"
        }
      ]
    }""",
    )

    opt_string = f"retry-config={service_config_fpath}"
    opts = Options.build(opt_string)

    # Verify the config was read in correctly.
    expected_cfg = {
        "methodConfig": [
            {
                "name": [
                    {
                        "service": "animalia.mollusca.v1beta1.Cephalopod",
                        "method": "IdentifySquid",
                    }
                ],
                "retryPolicy": {
                    "maxAttempts": 5,
                    "maxBackoff": "3s",
                    "initialBackoff": "0.2s",
                    "backoffMultiplier": 2,
                    "retryableStatusCodes": ["UNAVAILABLE", "UNKNOWN"],
                },
                "timeout": "5s",
            }
        ]
    }
    assert opts.retry == expected_cfg


def test_options_service_yaml_config(fs):
    opts = Options.build("")
    assert opts.service_yaml_config == {}

    service_yaml_fpath = "testapi_v1.yaml"
    fs.create_file(
        service_yaml_fpath,
        contents=(
            "type: google.api.Service\n"
            "config_version: 3\n"
            "name: testapi.googleapis.com\n"
        ),
    )
    opt_string = f"service-yaml={service_yaml_fpath}"
    opts = Options.build(opt_string)
    expected_config = {"config_version": 3, "name": "testapi.googleapis.com"}
    assert opts.service_yaml_config == expected_config

    service_yaml_fpath = "testapi_v2.yaml"
    fs.create_file(
        service_yaml_fpath,
        contents=("config_version: 3\nname: testapi.googleapis.com\n"),
    )
    opt_string = f"service-yaml={service_yaml_fpath}"
    opts = Options.build(opt_string)
    expected_config = {"config_version": 3, "name": "testapi.googleapis.com"}
    assert opts.service_yaml_config == expected_config


def test_options_transport():
    opts = Options.build("")
    assert opts.transport == ["grpc"]

    opts = Options.build("transport=rest")
    assert opts.transport == ["rest"]

    opts = Options.build("transport=grpc+rest")
    assert opts.transport == ["grpc", "rest"]

    opts = Options.build("transport=alpha+beta+gamma")
    assert opts.transport == ["alpha", "beta", "gamma"]


def test_options_bool_flags():
    # Most options are default False.
    # New options should follow the dash-case/snake_case convention.
    opt_str_to_attr_name = {
        name: re.sub(r"-", "_", name)
        for name in [
            "lazy-import",
            "old-naming",
            "add-iam-methods",
            "metadata",
            "warehouse-package-name",
            "rest-numeric-enums",
        ]
    }

    for opt, attr in opt_str_to_attr_name.items():
        options = Options.build("")
        assert not getattr(options, attr)

        options = Options.build(opt)
        assert getattr(options, attr)

    # Check autogen-snippets separately, as it is default True
    options = Options.build("")
    assert options.autogen_snippets

    options = Options.build("autogen-snippets=False")
    assert not options.autogen_snippets

    options = Options.build("rest-numeric-enums=False")
    assert not options.rest_numeric_enums


def test_options_autogen_snippets_false_for_old_naming():
    # NOTE: Snippets are not currently correct for the alternative (Ads) templates
    # so always disable snippetgen in that case
    # https://github.com/googleapis/gapic-generator-python/issues/1052
    options = Options.build("old-naming")
    assert not options.autogen_snippets

    # Even if autogen-snippets is set to True, do not enable snippetgen
    options = Options.build("old-naming,autogen-snippets=True")
    assert not options.autogen_snippets


def test_options_proto_plus_deps():
    opts = Options.build("proto-plus-deps=")
    assert opts.proto_plus_deps == ("",)

    opts = Options.build("proto-plus-deps=google.apps.script.type.calendar")
    assert opts.proto_plus_deps == ("google.apps.script.type.calendar",)

    opts = Options.build(
        "proto-plus-deps=\
google.apps.script.type.calendar+\
google.apps.script.type.docs+\
google.apps.script.type.drive+\
google.apps.script.type.gmail+\
google.apps.script.type.sheets+\
google.apps.script.type.slides+\
google.apps.script.type"
    )
    assert opts.proto_plus_deps == (
        "google.apps.script.type.calendar",
        "google.apps.script.type.docs",
        "google.apps.script.type.drive",
        "google.apps.script.type.gmail",
        "google.apps.script.type.sheets",
        "google.apps.script.type.slides",
        "google.apps.script.type",
    )


def test_options_resource_name_aliases():
    with mock.patch.object(warnings, "warn") as warn:
        opts = Options.build(
            "resource-name-alias=ces.googleapis.com/Tool:CesTool,"
            "resource-name-alias=workspace.googleapis.com/Tool:WorkspaceTool,"
            "resource-name-alias=bad_string_without_colon,"
            "resource-name-alias=:MissingPath,"
            "resource-name-alias=MissingAlias:,"
            "resource-name-alias=" # Covers empty string ("")
        )

        # Verify the dictionary is perfectly formed
        expected = {
            "ces.googleapis.com/Tool": "CesTool",
            "workspace.googleapis.com/Tool": "WorkspaceTool",
        }
        assert opts.resource_name_aliases == expected
        
        # We expect exactly 3 warnings: 
        # 1. bad_string
        # 2. :MissingPath 
        # 3. MissingAlias: 
        # (The empty ' ' string safely 'continues' without warning, as intended)
        assert warn.call_count == 3


def test_options_resumable_upload_prefix():
    # Verify that resumable_upload_prefix defaults to "resumable/upload" when not specified.
    opts_default = Options.build("")
    assert opts_default.resumable_upload_prefix == "resumable/upload"

    # Verify that a custom resumable-upload-prefix option is parsed and stored.
    opts_custom = Options.build("resumable-upload-prefix=custom/upload/prefix")
    assert opts_custom.resumable_upload_prefix == "custom/upload/prefix"

