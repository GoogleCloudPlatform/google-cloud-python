# Copyright 2020 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import os
import requests
import logging
from typing import List, Optional
from dataclasses import dataclass

# Configure logging to output messages to console
logging.basicConfig(level=logging.INFO)  # Set the desired logging level

import re

class MissingGithubToken(ValueError):
    """Raised when the GITHUB_TOKEN environment variable is not set"""

    pass

RAW_CONTENT_BASE_URL = "https://raw.githubusercontent.com"
MONO_REPO_PATH_FORMAT = "googleapis/google-cloud-python/main/packages/{repo_slug}"
SPLIT_REPO_PATH_FORMAT = "{repo_slug}/main"
REPO_METADATA_FILENAME = ".repo-metadata.json"


# MONO_REPO defines the name of the mono repository for Python.
MONO_REPO = "googleapis/google-cloud-python"

# REPO_EXCLUSION lists the repositories that need to be excluded.
REPO_EXCLUSION = [
    # core libraries
    "googleapis/python-api-core",
    "googleapis/python-cloud-core",
    # proto only packages
    "googleapis/python-api-common-protos",
    # testing utilities
    "googleapis/python-test-utils",
]

# PACKAGE_RESPONSE_KEY defines the package name in the response.
PACKAGE_RESPONSE_KEY = "name"

# REPO_RESPONSE_KEY defines the repository name in the response.
REPO_RESPONSE_KEY = "full_name"

# ARCHIVED_RESPONSE_KEY defines the repository archived status in the response.
ARCHIVED_RESPONSE_KEY = "archived"

# BASE_API defines the base API for Github.
BASE_API = "https://api.github.com"

# GITHUB_ISSUES defines the issues URL for a repository on GitHub.
GITHUB_ISSUES = "https://github.com/{repo}/issues"

# BASE_ISSUE_TRACKER defines the base URL for issue tracker.
BASE_ISSUE_TRACKER = "https://issuetracker.google.com"

# This issue-tracker component is part of some saved searches for listing API-side issues.
# However, when we construct URLs for filing new issues (which in some cases we do by analyzing
# the query string for a saved search), we want to ensure we DON'T file a new issue against
# this generic component but against a more specific one.
GENERIC_ISSUE_TRACKER_COMPONENT = "187065"

# This sentinel value is used to mark cache fields that have not been computed yet.
NOT_COMPUTED = -1

class CloudClient:
    repo: str = None
    title: str = None
    release_level: str = None
    distribution_name: str = None
    issue_tracker: str = None


    def __init__(self, repo: dict):
        self.repo = repo["repo"]
        # For now, strip out "Google Cloud" to standardize the titles
        self.title = repo["name_pretty"].replace("Google ", "").replace("Cloud ", "")
        self.release_level = repo["release_level"]
        self.distribution_name = repo["distribution_name"]
        self.issue_tracker = repo.get("issue_tracker")
        self._cached_component_id = NOT_COMPUTED
        self._cached_template_id = NOT_COMPUTED
        self._cached_saved_search_id = NOT_COMPUTED
    
    @property
    def saved_search_id(self):
        if self._cached_saved_search_id != NOT_COMPUTED:
            return self._cached_saved_search_id
        if not self.issue_tracker:
            self._cached_saved_search_id = None
        else:
            match = re.search(r'savedsearches/(\d+)', self.issue_tracker)
            self._cached_saved_search_id = match.group(1) if match else None
        return self._cached_saved_search_id
    
    @property
    def saved_search_response_text(self):
        if not self.saved_search_id:
            return None
        url = f"{BASE_ISSUE_TRACKER}/action/saved_searches/{self.saved_search_id}"
        response = _fetch_response(url)
        return response.text if response else None

    @property
    def issue_tracker_component_id(self):
        if self._cached_component_id != NOT_COMPUTED:
            return self._cached_component_id
        
        # First, check if the issue tracker is a saved search:
        query_string = self.saved_search_response_text or self.issue_tracker
        if not query_string:
            self._cached_component_id = None
        else:
            # Try to match 'component=' in the query string
            query_match = re.search(r'\bcomponent=(\d+)', query_string)
            if query_match:
                self._cached_component_id = query_match.group(1)
            else:
                # If not found, try to match 'componentid:' in the query string
                query_match = re.findall(r'\bcomponentid:(\d+)', query_string)
                for component_id in query_match:
                    if component_id == GENERIC_ISSUE_TRACKER_COMPONENT:
                        continue
                    if self._cached_component_id != NOT_COMPUTED:
                        self._cached_component_id = None
                        logging.error(f"More than one component ID found for issue tracker: {self.issue_tracker}")
                        break
                    self._cached_component_id = component_id
                self._cached_component_id = self._cached_component_id if self._cached_component_id != NOT_COMPUTED else None
        return self._cached_component_id
    
    @property
    def issue_tracker_template_id(self):
        if self._cached_template_id != NOT_COMPUTED:
            return self._cached_template_id
        if not self.issue_tracker:
            self._cached_template_id =  None
        else:
            match = re.search(r'(?:\?|&)template=(\d+)', self.issue_tracker)
            self._cached_template_id = match.group(1) if match else None
        return self._cached_template_id
    
    @property
    def show_client_issues(self):
        return GITHUB_ISSUES.format(repo=self.repo)
    
    @property
    def file_api_issue(self):
        if self.issue_tracker_component_id:
            link = f"{BASE_ISSUE_TRACKER}/issues/new?component={self.issue_tracker_component_id}"
            if self.issue_tracker_template_id:
                link += f"&template={self.issue_tracker_template_id}"
            return link
        return None
    
    @property
    def show_api_issues(self):
        if self.saved_search_id:
            # Return the original issue_tracker content, which already links to the saved search.
            return self.issue_tracker
        elif self.issue_tracker_component_id:
            return f"{BASE_ISSUE_TRACKER}/issues?q=componentid:{self.issue_tracker_component_id}"
        return None

    # For sorting, we want to sort by release level, then API pretty_name
    def __lt__(self, other):
        if self.release_level == other.release_level:
            return self.title < other.title

        return other.release_level < self.release_level

    def __repr__(self):
        return repr((self.release_level, self.title))


@dataclass
class Extractor:
    path_format: str
    response_key: str

    def client_for_repo(self, repo_slug) -> Optional[CloudClient]:
        path = self.path_format.format(repo_slug=repo_slug)
        url = f"{RAW_CONTENT_BASE_URL}/{path}/{REPO_METADATA_FILENAME}"
        _, metadata = _fetch_and_parse_response(url)
        if not metadata:
            return None
        return CloudClient(metadata)
    
    def get_clients_from_batch_response(self, response_json) -> List[CloudClient]:
        return [self.client_for_repo(repo[self.response_key]) for repo in response_json if allowed_repo(repo)]

def _fetch_response(url: str, headers:dict = None, params:Optional[dict] = None) -> Optional[requests.Response]:
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logging.error(f"Request failed for URL {url}: {e}")
        return None

def _parse_response(response: requests.Response) -> Optional[dict]:
    try:
        return response.json()
    except ValueError as e:
        logging.error(f"JSON decoding failed for URL {response.url}: {e}")
        return None
    
def _fetch_and_parse_response(url: str, headers:dict = None, params:Optional[dict] = None):
    response = _fetch_response(url, headers, params)
    if not response:
        return None, None
    return response, _parse_response(response)

def replace_content_in_readme(content_rows: List[str]) -> None:
    START_MARKER = ".. API_TABLE_START"
    END_MARKER = ".. API_TABLE_END"
    newlines = []
    repl_open = False
    with open("README.rst", "r") as f:
        for line in f:
            if not repl_open:
                newlines.append(line)

            if line.startswith(START_MARKER):
                repl_open = True
                newlines = newlines + content_rows
            elif line.startswith(END_MARKER):
                newlines.append("\n")
                newlines.append(line)
                repl_open = False

    with open("README.rst", "w") as f:
        for line in newlines:
            f.write(line)


def client_row(client: CloudClient) -> str:
    pypi_badge = f""".. |PyPI-{client.distribution_name}| image:: https://img.shields.io/pypi/v/{client.distribution_name}.svg
     :target: https://pypi.org/project/{client.distribution_name}\n"""
    
    url = f"https://github.com/{client.repo}"
    if client.repo == MONO_REPO:
        url += f"/tree/main/packages/{client.distribution_name}"
    _show_api_issues = client.show_api_issues
    _file_api_issue = client.file_api_issue
    content_row = [
        f"   * - `{client.title} <{url}>`_\n",
        f"     - {client.release_level}\n",
        f"     - |PyPI-{client.distribution_name}|\n",
        f"     - `API Issues <{_show_api_issues}>`_\n" if _show_api_issues else "     -\n",
        f"     - `File an API Issue <{_file_api_issue}>`_\n" if _file_api_issue else "     -\n",
        f"     - `Client Library Issues <{client.show_client_issues}>`_\n"
    ]

    return (content_row, pypi_badge)


def generate_table_contents(clients: List[CloudClient]) -> List[str]:
    content_rows = [
        "\n",
        ".. list-table::\n",
        "   :header-rows: 1\n",
        "\n",
        "   * - Client\n",
        "     - Release Level\n",
        "     - Version\n",
        "     - API Issues\n",
        "     - File an API Issue\n",
        "     - Client Library Issues\n",
    ]

    pypi_links = ["\n"]
    for client in clients:
        content_row, pypi_link = client_row(client)
        content_rows += content_row
        pypi_links.append(pypi_link)

    return content_rows + pypi_links


def allowed_repo(repo) -> bool:
    return REPO_RESPONSE_KEY not in repo or (
        repo[REPO_RESPONSE_KEY].startswith("googleapis/python-")
        and repo[REPO_RESPONSE_KEY] not in REPO_EXCLUSION
        and not repo[ARCHIVED_RESPONSE_KEY]
    )


def mono_repo_clients(token: str) -> List[CloudClient]:
    # all mono repo clients
    url = f"{BASE_API}/repos/{MONO_REPO}/contents/packages"
    headers = {'Authorization': f'token {token}'}
    _, packages = _fetch_and_parse_response(url, headers)
    if not packages:
        return []
    mono_repo_extractor = Extractor(path_format=MONO_REPO_PATH_FORMAT, response_key=PACKAGE_RESPONSE_KEY)
    return mono_repo_extractor.get_clients_from_batch_response(packages)


def split_repo_clients(token: str) -> List[CloudClient]:
    clients = []
    url = f"{BASE_API}/search/repositories?page=1"
    headers = {'Authorization': f'token {token}'}
    params = {'per_page': 100, "q": "python- in:name org:googleapis"}

    while url:
        response, metadata = _fetch_and_parse_response(url, headers, params)
        if not metadata:
            break
        repositories = metadata.get("items", [])
        if len(repositories) == 0:
            break
        split_repo_extractor = Extractor(path_format=SPLIT_REPO_PATH_FORMAT, response_key=REPO_RESPONSE_KEY)
        clients.extend(split_repo_extractor.get_clients_from_batch_response(repositories))

        # Check for the 'next' link in the response headers for pagination
        url = response.links.get('next', {}).get('url')

    return clients


def get_token():
    if 'GITHUB_TOKEN' not in os.environ:
        raise MissingGithubToken("Please include a GITHUB_TOKEN env var.")
    
    token = os.environ['GITHUB_TOKEN']
    return token


def all_clients() -> List[CloudClient]:
    clients = []
    token = get_token()
    
    clients.extend(split_repo_clients(token))
    clients.extend(mono_repo_clients(token))

    # remove empty clients
    return [client for client in clients if client]


clients = sorted(all_clients())
table_contents = generate_table_contents(clients)
replace_content_in_readme(table_contents)
