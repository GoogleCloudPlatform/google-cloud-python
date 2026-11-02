import sys
import pytest
import os


if __name__ == "__main__":
    # The generated file name will be of the form `<module_name>_pytest.py`.
    # The generated gapic will be in a directory `<module_name>_srcjar.py``.
    # Extract the `<module_name>`` from this file, and use it to determine the
    # directory of the generated gapic.
    # Only run `pytest` on the `tests` directory.
    module_name = os.path.abspath(__file__).replace("_pytest.py", "")
    src_directory = f"{module_name}_srcjar.py"
    sys.exit(
        pytest.main(["--disable-pytest-warnings", "--quiet", f"{src_directory}/tests"])
    )
