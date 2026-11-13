# Copyright 2017 Google Inc.
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

import os

import setuptools


PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PACKAGE_ROOT, 'README.rst')) as file_obj:
    README = file_obj.read()


REQUIREMENTS = [
    'google-crc32c >= 1.0.0, < 2.0.0',
]
EXTRAS_REQUIRE = {
    'requests': [
        'requests >= 2.18.0, < 3.0.0',
    ],
    'aiohttp': ['aiohttp >= 3.6.2, < 4.0.0', 'google-auth >= 2.14.1, < 3.0.0']
}

setuptools.setup(
    name='google-resumable-media',
    version = "2.11.0",
    description='Utilities for Google Media Downloads and Resumable Uploads',
    author='Google Cloud Platform',
    author_email='googleapis-publisher@google.com',
    long_description=README,
    scripts=[],
    url="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-resumable-media",
    packages=setuptools.find_namespace_packages(
        exclude=("tests*", "docs*")
    ),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    python_requires='>= 3.10',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Topic :: Internet',
    ],
)
