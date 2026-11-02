# -*- coding: utf-8 -*-
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
#
import io
import os
import re

import setuptools # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

name = 'google-cloud-eventarc'


description = "Google Cloud Eventarc API client library"

version = None

with open(os.path.join(package_root, 'google/cloud/eventarc_v1/gapic_version.py')) as fp:
    version_candidates = re.findall(
        r"(?<=\")\d+\.\d+\.\d+[^\"\s]*(?=\")",
        fp.read(),
    )
    assert (len(version_candidates) == 1)
    version = version_candidates[0]

if version[0] == "0":
    release_status = "Development Status :: 4 - Beta"
else:
    release_status = "Development Status :: 5 - Production/Stable"

dependencies = [
    "google-api-core[grpc] >= 2.28.0, <3.0.0",
    # Exclude incompatible versions of `google-auth`
    # See https://github.com/googleapis/google-cloud-python/issues/12364
    "google-auth >= 2.14.1, <3.0.0,!=2.24.0,!=2.25.0",
    "grpcio >= 1.59.0, < 2.0.0",
    "grpcio >= 1.75.1, < 2.0.0; python_version >= '3.14'",
    "proto-plus >= 1.26.1, <2.0.0",
    "protobuf >= 6.33.5, < 8.0.0",
    "grpc-google-iam-v1 >= 0.14.2, <1.0.0",
]
extras = {
}
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-eventarc"

package_root = os.path.abspath(os.path.dirname(__file__))

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
    license="Apache-2.0",
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
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    python_requires=">=3.10",
    install_requires=dependencies,
    extras_require=extras,
    include_package_data=True,
    zip_safe=False,
)
