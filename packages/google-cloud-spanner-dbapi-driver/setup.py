# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
#
import io
import os
import re

import setuptools  # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

name = "google-cloud-spanner-dbapi-driver"

description = "Google Cloud Spanner DBAPI 2.0 Driver"

version = None

with open(os.path.join(package_root, "google/cloud/spanner_driver/version.py")) as fp:
    version_candidates = re.findall(r"__version__\s*=\s*\"([^\"]+)\"", fp.read())
    assert len(version_candidates) == 1
    version = version_candidates[0]

release_status = "Development Status :: 1 - Planning"

dependencies = [
    "spannerlib-python",
]
extras = {}
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-spanner-dbapi-driver"

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package
    for package in setuptools.find_namespace_packages()
    if package.startswith("google")
]

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url=url,
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Operating System :: OS Independent",
        "Topic :: Database",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    python_requires=">=3.10",
    install_requires=dependencies,
    extras_require=extras,
    include_package_data=True,
    zip_safe=False,
)
