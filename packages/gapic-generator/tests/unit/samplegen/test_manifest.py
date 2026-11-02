# Copyright (C) 2019  Google LLC
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
import yaml
from textwrap import dedent

import gapic.samplegen_utils.yaml as gapic_yaml
import gapic.samplegen_utils.types as types
import gapic.samplegen.manifest as manifest
from ..common_types import DummyApiSchema, DummyNaming


def test_generate_manifest():
    fpath_to_dummy_sample = {
        "samples/squid_fpath.py": {"id": "squid_sample"},
        "samples/clam_fpath.py": {
            "id": "clam_sample",
            "region_tag": "giant_clam_sample",
        },
    }

    fname, info = manifest.generate(
        fpath_to_dummy_sample.items(),
        DummyApiSchema(naming=DummyNaming(name="Mollusc", version="v1")),
        # Empirically derived number such that the
        # corresponding time_struct tests the zero
        # padding in the returned filename.
        manifest_time=4486525628,
    )

    assert fname == "mollusc.v1.python.21120304.090708.manifest.yaml"

    doc = gapic_yaml.Doc(
        [
            gapic_yaml.KeyVal("type", "manifest/samples"),
            gapic_yaml.KeyVal("schema_version", "3"),
            gapic_yaml.Map(
                name="python",
                anchor_name="python",
                elements=[
                    gapic_yaml.KeyVal("environment", "python"),
                    gapic_yaml.KeyVal("bin", "python3"),
                    gapic_yaml.KeyVal("base_path", "samples"),
                    gapic_yaml.KeyVal("invocation", "'{bin} {path} @args'"),
                ],
            ),
            gapic_yaml.Collection(
                name="samples",
                elements=[
                    [
                        gapic_yaml.Alias("python"),
                        gapic_yaml.KeyVal("sample", "squid_sample"),
                        gapic_yaml.KeyVal("path", "'{base_path}/squid_fpath.py'"),
                        gapic_yaml.Null,
                    ],
                    [
                        gapic_yaml.Alias("python"),
                        gapic_yaml.KeyVal("sample", "clam_sample"),
                        gapic_yaml.KeyVal("path", "'{base_path}/clam_fpath.py'"),
                        gapic_yaml.KeyVal("region_tag", "giant_clam_sample"),
                    ],
                ],
            ),
        ]
    )

    assert info == doc

    expected_rendering = dedent(
        """\
        ---
        type: manifest/samples
        schema_version: 3
        python: &python
          environment: python
          bin: python3
          base_path: samples
          invocation: '{bin} {path} @args'
        samples:
        - <<: *python
          sample: squid_sample
          path: '{base_path}/squid_fpath.py'
        - <<: *python
          sample: clam_sample
          path: '{base_path}/clam_fpath.py'
          region_tag: giant_clam_sample
        """
    )

    rendered_yaml = doc.render()
    assert rendered_yaml == expected_rendering

    expected_parsed_manifest = {
        "type": "manifest/samples",
        "schema_version": 3,
        "python": {
            "environment": "python",
            "bin": "python3",
            "base_path": "samples",
            "invocation": "{bin} {path} @args",
        },
        "samples": [
            {
                "environment": "python",
                "bin": "python3",
                "base_path": "samples",
                "invocation": "{bin} {path} @args",
                "sample": "squid_sample",
                "path": "{base_path}/squid_fpath.py",
            },
            {
                "environment": "python",
                "bin": "python3",
                "base_path": "samples",
                "invocation": "{bin} {path} @args",
                "sample": "clam_sample",
                "path": "{base_path}/clam_fpath.py",
                "region_tag": "giant_clam_sample",
            },
        ],
    }

    parsed_manifest = yaml.safe_load(rendered_yaml)
    assert parsed_manifest == expected_parsed_manifest


def test_generate_manifest_relative_path_quick_check():
    with pytest.raises(types.InvalidSampleFpath):
        manifest.generate(
            {"molluscs/squid.py": {"id": "squid_sample"}}.items(),
            DummyApiSchema(naming=DummyNaming(name="Mollusc", version="v1")),
        )
