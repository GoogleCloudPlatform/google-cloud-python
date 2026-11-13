# Copyright 2021 Google LLC
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

import datetime
import random
import re
from typing import Union

_RESOURCE_DATE_FORMAT = "%Y%m%d%H%M%S"
_RESOURCE_DATE_LENGTH = 4 + 2 + 2 + 2 + 2 + 2
_RE_SEPARATORS = re.compile(r"[/\-\\_]")


def _common_prefix(repo, relative_dir, separator="_"):
    repo = _RE_SEPARATORS.sub(separator, repo)
    relative_dir = _RE_SEPARATORS.sub(separator, relative_dir)
    return f"{repo}{separator}{relative_dir}"


class Prefixer(object):
    """Create/manage resource IDs for system testing.

    Usage:

    Creating resources:

    >>> import test_utils.prefixer
    >>> prefixer = test_utils.prefixer.Prefixer("python-bigquery", "samples/snippets")
    >>> dataset_id = prefixer.create_prefix() + "my_sample"

    Cleaning up resources:

    >>> @pytest.fixture(scope="session", autouse=True)
    ... def cleanup_datasets(bigquery_client: bigquery.Client):
    ...     for dataset in bigquery_client.list_datasets():
    ...         if prefixer.should_cleanup(dataset.dataset_id):
    ...             bigquery_client.delete_dataset(
    ...                 dataset, delete_contents=True, not_found_ok=True
    """

    def __init__(
        self, repo, relative_dir, separator="_", cleanup_age=datetime.timedelta(days=1)
    ):
        self._separator = separator
        self._cleanup_age = cleanup_age
        self._prefix = _common_prefix(repo, relative_dir, separator=separator)

    def create_prefix(self) -> str:
        now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        timestamp = now.strftime(_RESOURCE_DATE_FORMAT)
        random_string = hex(random.randrange(0x1000000))[2:]
        return f"{self._prefix}{self._separator}{timestamp}{self._separator}{random_string}"

    def _name_to_date(self, resource_name: str) -> Union[datetime.datetime, None]:
        start_date = len(self._prefix) + len(self._separator)
        date_string = resource_name[start_date : start_date + _RESOURCE_DATE_LENGTH]
        try:
            parsed_date = datetime.datetime.strptime(date_string, _RESOURCE_DATE_FORMAT)
            return parsed_date
        except ValueError:
            return None

    def should_cleanup(self, resource_name: str) -> bool:
        now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        yesterday = now - self._cleanup_age
        if not resource_name.startswith(self._prefix):
            return False

        created_date = self._name_to_date(resource_name)
        return created_date is not None and created_date < yesterday
