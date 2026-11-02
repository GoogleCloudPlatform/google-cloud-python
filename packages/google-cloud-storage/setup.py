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

import setuptools  # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

name = "google-cloud-storage"


description = "Google Cloud Storage API client library"

version = None

with open(os.path.join(package_root, "google/cloud/_storage/gapic_version.py")) as fp:
    version_candidates = re.findall(
        r"(?<=\")\d+\.\d+\.\d+[^\"\s]*(?=\")",
        fp.read(),
    )
    assert len(version_candidates) == 1
    version = version_candidates[0]

if version[0] == "0":
    release_status = "Development Status :: 4 - Beta"
else:
    release_status = "Development Status :: 5 - Production/Stable"

dependencies = [
    "google-auth >= 2.26.1, < 3.0.0",
    "google-api-core >= 2.27.0, < 3.0.0",
    "google-cloud-core >= 2.4.2, < 3.0.0",
    # The dependency "google-resumable-media" is no longer used. However, the
    # dependency is still included here to accommodate users who may be
    # importing exception classes from the google-resumable-media without
    # installing it explicitly. See the python-storage README for details on
    # exceptions and importing. Users who are not importing
    # google-resumable-media classes in their application can safely disregard
    # this dependency.
    "google-resumable-media >= 2.7.2, < 3.0.0",
    "requests >= 2.22.0, < 3.0.0",
    "google-crc32c >= 1.6.0, < 2.0.0",
]
extras = {
    # TODO: Make these extra dependencies as mandatory once gRPC out of
    # experimental in this SDK. More info in b/465352227
    "grpc": [
        "google-api-core[grpc] >= 2.27.0, < 3.0.0",
        "grpcio >= 1.59.0, < 2.0.0",
        "grpcio >= 1.75.1, < 2.0.0; python_version >= '3.14'",
        "grpcio-status >= 1.59.0, < 2.0.0",
        "grpcio-status >= 1.75.1, < 2.0.0; python_version >= '3.14'",
        "proto-plus >= 1.26.1, <2.0.0",
        "protobuf >= 6.33.5, < 8.0.0",
        "grpc-google-iam-v1 >= 0.14.2, <1.0.0",
    ],
    "protobuf": ["protobuf >= 6.33.5, < 8.0.0"],
    "tracing": [
        "opentelemetry-api >= 1.1.0, < 2.0.0",
    ],
    "testing": [
        "google-cloud-testutils",
        "numpy",
        "psutil",
        "py-cpuinfo",
        "pytest-benchmark",
        "PyYAML",
        "mock",
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "pytest-rerunfailures",
        "pytest-xdist",
        "google-cloud-testutils",
        "google-cloud-iam",
        "google-cloud-pubsub",
        "google-cloud-kms",
        "brotli",
        "coverage",
        "pyopenssl",
        "opentelemetry-sdk",
        "flake8",
        "black",
    ],
}
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage"

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
