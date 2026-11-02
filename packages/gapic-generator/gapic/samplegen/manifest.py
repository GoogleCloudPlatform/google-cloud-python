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

import os
import time
from typing import Optional, Tuple

from gapic.samplegen_utils import types, yaml
from gapic.utils import case

BASE_PATH_KEY = "base_path"
DEFAULT_SAMPLE_DIR = "samples"

# The default environment for executing python samples.
# Custom environments must adhere to the following pattern:
# they must be a yaml.Map with a defined anchor_name field,
# and 'environment', 'base_path', and 'invocation' keys must be present.
# The 'invocation' key must map to an interpolable commandline
# that will invoke the given sample.
PYTHON3_ENVIRONMENT = yaml.Map(
    name="python",
    anchor_name="python",
    elements=[
        yaml.KeyVal("environment", "python"),
        yaml.KeyVal("bin", "python3"),
        yaml.KeyVal(BASE_PATH_KEY, DEFAULT_SAMPLE_DIR),
        yaml.KeyVal("invocation", "'{bin} {path} @args'"),
    ],
)


def generate(
    fpaths_and_samples,
    api_schema,
    *,
    environment: yaml.Map = PYTHON3_ENVIRONMENT,
    manifest_time: Optional[int] = None,
) -> Tuple[str, yaml.Doc]:
    """Generate a samplegen manifest for use by sampletest

    Args:
        fpaths_and_samples (Iterable[Tuple[str, Mapping[str, Any]]]):
                         The file paths and samples to be listed in the manifest
        api_schema (~.api.API): An API schema object.
        environment (yaml.Map): Optional custom sample execution environment.
                                Set this if the samples are being generated for
                                a custom language.
        manifest_time (int): Optional. An override for the timestamp in the name of the manifest filename.
                             Primarily used for testing.

    Returns:
        Tuple[str, yaml.Doc]: The filename of the manifest and the manifest data as a dictionary.

    Raises:
        types.InvalidSampleFpath: If any of the paths in fpaths_and_samples do not
                                  begin with the base_path from the environment.

    """
    base_path = environment.get(BASE_PATH_KEY, DEFAULT_SAMPLE_DIR)

    def transform_path(fpath):
        fpath = os.path.normpath(fpath)
        if not fpath.startswith(base_path):
            raise types.InvalidSampleFpath(
                f"Sample fpath does not start with '{base_path}': {fpath}"
            )

        return "'{base_path}/%s'" % os.path.relpath(fpath, base_path)

    doc = yaml.Doc(
        [
            yaml.KeyVal("type", "manifest/samples"),
            yaml.KeyVal("schema_version", "3"),
            environment,
            yaml.Collection(
                name="samples",
                elements=[
                    [
                        # Mypy doesn't correctly intuit the type of the
                        # "region_tag" conditional expression.
                        yaml.Alias(environment.anchor_name or ""),
                        yaml.KeyVal("sample", sample["id"]),
                        yaml.KeyVal("path", transform_path(fpath)),
                        (
                            yaml.KeyVal("region_tag", sample["region_tag"])  # type: ignore
                            if "region_tag" in sample
                            else yaml.Null
                        ),
                    ]
                    for fpath, sample in fpaths_and_samples
                ],
            ),
        ]
    )

    dt = time.gmtime(manifest_time)
    manifest_fname_template = (
        "{api}.{version}.{language}."
        "{year:04d}{month:02d}{day:02d}."
        "{hour:02d}{minute:02d}{second:02d}."
        "manifest.yaml"
    )

    manifest_fname = manifest_fname_template.format(
        api=case.to_snake_case(api_schema.naming.name),
        version=api_schema.naming.version,
        language=environment.name,
        year=dt.tm_year,
        month=dt.tm_mon,
        day=dt.tm_mday,
        hour=dt.tm_hour,
        minute=dt.tm_min,
        second=dt.tm_sec,
    )

    return manifest_fname, doc
