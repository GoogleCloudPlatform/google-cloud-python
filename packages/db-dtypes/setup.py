# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os
import re

from setuptools import setup

# Package metadata.

name = "db-dtypes"
description = "Pandas Data Types for SQL systems (BigQuery, Spanner)"

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 5 - Production/Stable"

dependencies = [
    "numpy >= 1.24.0, <= 2.2.6 ; python_version == '3.10'",
    "numpy >= 1.24.0 ; python_version != '3.10'",
    "packaging >= 24.2.0",
    "pandas >= 1.5.3, < 4.0.0",
    "pyarrow >= 13.0.0",
]

package_root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(package_root, "db_dtypes", "version.py")) as f:
    version = re.search('__version__ = "([^"]+)"', f.read()).group(1)


def readme():
    with io.open("README.rst", "r", encoding="utf8") as f:
        return f.read()


setup(
    name=name,
    version=version,
    description=description,
    long_description=readme(),
    long_description_content_type="text/x-rst",
    author="The db-dtypes Authors",
    author_email="googleapis-packages@google.com",
    packages=["db_dtypes"],
    url="https://github.com/googleapis/google-cloud-python/tree/main/packages/db-dtypes",
    keywords=["sql", "pandas"],
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
        "Topic :: Database :: Front-Ends",
    ],
    platforms="Posix; MacOS X; Windows",
    install_requires=dependencies,
    python_requires=">=3.10",
    tests_require=["pytest"],
)
