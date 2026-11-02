import ast
import os
import subprocess
import sys

import pytest
import yaml

# add cross_sync to path
test_dir_name = os.path.dirname(__file__)
cross_sync_path = os.path.join(test_dir_name, "..", "..", "..", ".cross_sync")
sys.path.append(cross_sync_path)

from transformers import (  # noqa: F401 E402
    AsyncToSync,
    CrossSyncFileProcessor,
    RmAioFunctions,
    StripAsyncConditionalBranches,
    SymbolReplacer,
)


def loader():
    dir_name = os.path.join(test_dir_name, "test_cases")
    for file_name in os.listdir(dir_name):
        if not file_name.endswith(".yaml"):
            print(f"Skipping {file_name}")
            continue
        test_case_file = os.path.join(dir_name, file_name)
        # load test cases
        with open(test_case_file) as f:
            print(f"Loading test cases from {test_case_file}")
            test_cases = yaml.safe_load(f)
            for test in test_cases["tests"]:
                test["file_name"] = file_name
                yield test


@pytest.mark.parametrize(
    "test_dict", loader(), ids=lambda x: f"{x['file_name']}: {x.get('description', '')}"
)
def test_e2e_scenario(test_dict):
    before_ast = ast.parse(test_dict["before"])
    got_ast = before_ast
    for transformer_info in test_dict["transformers"]:
        # transformer can be passed as a string, or a dict with name and args
        if isinstance(transformer_info, str):
            transformer_class = globals()[transformer_info]
            transformer_args = {}
        else:
            transformer_class = globals()[transformer_info["name"]]
            transformer_args = transformer_info.get("args", {})
        transformer = transformer_class(**transformer_args)
        got_ast = transformer.visit(got_ast)
    if got_ast is None:
        final_str = ""
    else:
        final_str = subprocess.run(
            [
                sys.executable,
                "-m",
                "ruff",
                "format",
                "--line-length=88",
                "--config",
                "format.skip-magic-trailing-comma=true",
                "-",
            ],
            input=ast.unparse(got_ast),
            text=True,
            capture_output=True,
            check=True,
        ).stdout
    if test_dict.get("after") is None:
        expected_str = ""
    else:
        expected_str = subprocess.run(
            [
                sys.executable,
                "-m",
                "ruff",
                "format",
                "--line-length=88",
                "--config",
                "format.skip-magic-trailing-comma=true",
                "-",
            ],
            input=test_dict["after"],
            text=True,
            capture_output=True,
            check=True,
        ).stdout
    assert final_str == expected_str, f"Expected:\n{expected_str}\nGot:\n{final_str}"
