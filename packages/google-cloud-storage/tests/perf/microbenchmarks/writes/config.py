# Copyright 2026 Google LLC
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
import itertools
import os
from typing import Dict, List

import yaml

try:
    from tests.perf.microbenchmarks.writes.parameters import WriteParameters
except ModuleNotFoundError:
    from parameters import WriteParameters


def get_write_params() -> Dict[str, List[WriteParameters]]:
    """Generates benchmark parameters from a YAML configuration file.

    This function reads the configuration from `config.yaml`, located in the
    same directory, and generates all possible combinations of write parameters
    based on the defined workloads. It uses `itertools.product` to create
    a Cartesian product of parameters like bucket types, file sizes, etc.

    Returns:
        Dict[str, List[WriteParameters]]: A dictionary where keys are workload
        names and values are lists of `WriteParameters` instances for that
        workload.
    """
    params: Dict[str, List[WriteParameters]] = {}
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    common_params = config["common"]
    bucket_types = common_params["bucket_types"]
    file_sizes_mib = common_params["file_sizes_mib"]
    chunk_sizes_mib = common_params["chunk_sizes_mib"]
    rounds = common_params["rounds"]

    bucket_map = {
        "rapid": os.environ.get(
            "DEFAULT_RAPID_BUCKET",
            config["defaults"]["DEFAULT_RAPID_BUCKET"],
        ),
        "regional": os.environ.get(
            "DEFAULT_STANDARD_BUCKET", config["defaults"]["DEFAULT_STANDARD_BUCKET"]
        ),
    }

    for workload in config["workload"]:
        workload_name = workload["name"]
        params[workload_name] = []
        processes = workload["processes"]
        coros = workload["coros"]

        # Create a product of all parameter combinations
        product = itertools.product(
            bucket_types,
            file_sizes_mib,
            chunk_sizes_mib,
            processes,
            coros,
        )

        for (
            bucket_type,
            file_size_mib,
            chunk_size_mib,
            num_processes,
            num_coros,
        ) in product:
            file_size_bytes = file_size_mib * 1024 * 1024
            chunk_size_bytes = chunk_size_mib * 1024 * 1024
            bucket_name = bucket_map[bucket_type]

            num_files = num_processes * num_coros

            # Create a descriptive name for the parameter set
            name = f"{workload_name}_{bucket_type}_{num_processes}p_{num_coros}c_{chunk_size_mib}csize"

            params[workload_name].append(
                WriteParameters(
                    name=name,
                    workload_name=workload_name,
                    bucket_name=bucket_name,
                    bucket_type=bucket_type,
                    num_coros=num_coros,
                    num_processes=num_processes,
                    num_files=num_files,
                    rounds=rounds,
                    chunk_size_bytes=chunk_size_bytes,
                    file_size_bytes=file_size_bytes,
                )
            )
    return params
