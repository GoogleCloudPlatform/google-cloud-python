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

import pytest


def pytest_addoption(parser):
    """Adds a command line option to pytest.

    Args:
        parser: The pytest parser.
    """
    parser.addoption("--update-goldens", action="store", default=False)


@pytest.fixture
def update_goldens(request):
    """Returns the value of the --update-goldens command line option.

    Args:
        request: The pytest request object.

    Returns:
        The value of the --update-goldens command line option.
    """
    return request.config.getoption("--update-goldens")
