# Copyright 2018 Google LLC
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

import logging
import os
import platform
import shutil

import setuptools
import setuptools.command.build_ext

_EXTRA_DLL = "extra-dll"
_DLL_FILENAME = "crc32c.dll"

# Explicit environment variable or Kokoro CI disables pure-Python fallback
CRC32C_PURE_PYTHON_EXPLICIT = (
    "CRC32C_PURE_PYTHON" in os.environ
    or "KOKORO_BUILD_ID" in os.environ
    or "KOKORO_JOB_NAME" in os.environ
)
_FALSE_OPTIONS = ("0", "false", "no", "False", "No", None)
CRC32C_PURE_PYTHON = os.getenv("CRC32C_PURE_PYTHON") not in _FALSE_OPTIONS


def copy_dll(build_lib):
    install_prefix = os.environ.get("CRC32C_INSTALL_PREFIX")

    if os.name == "nt" and install_prefix is not None:
        assert os.path.isdir(install_prefix)

        installed_dll = os.path.join(install_prefix, "bin", _DLL_FILENAME)
        assert os.path.isfile(installed_dll)

        lib_dlls = os.path.join(build_lib, "google_crc32c", _EXTRA_DLL)
        os.makedirs(lib_dlls, exist_ok=True)
        relocated_dll = os.path.join(lib_dlls, _DLL_FILENAME)

        shutil.copyfile(installed_dll, relocated_dll)
        assert os.path.isfile(relocated_dll)


class BuildExtWithDLL(setuptools.command.build_ext.build_ext):
    def run(self):
        copy_dll(self.build_lib)
        result = setuptools.command.build_ext.build_ext.run(self)
        return result


def build_pure_python():
    setuptools.setup(
        packages=["google_crc32c"],
        package_dir={"": "src"},
        ext_modules=[],
    )


def build_c_extension():
    install_prefix = os.getenv("CRC32C_INSTALL_PREFIX")
    if install_prefix is not None:
        install_prefix = os.path.normcase(install_prefix)
        print(f"#### using local install of 'crc32c': {install_prefix!r}")
        # assert os.path.isdir(install_prefix)
        install_prefix = os.path.realpath(install_prefix)
        include_dirs = [os.path.join(install_prefix, "include")]
        library_dirs = [os.path.join(install_prefix, "lib")]

        if platform.system() == "Linux":
            library_dirs.append(os.path.join(install_prefix, "lib64"))

        if os.name == "nt":
            library_dirs.append(os.path.join(install_prefix, "bin"))
            kwargs = {
                "include_dirs": include_dirs,
                "library_dirs": library_dirs,
            }
        else:
            runtime_library_dirs = library_dirs[:]
            kwargs = {
                "include_dirs": include_dirs,
                "library_dirs": library_dirs,
                "runtime_library_dirs": runtime_library_dirs,
            }
    else:
        print("#### using global install of 'crc32c'")
        kwargs = {}

    module_path = os.path.join("src", "google_crc32c", "_crc32c.c")
    sources = [os.path.normcase(module_path)]
    print(f"##### sources: {sources}")
    print(f"##### module kwargs: {kwargs}")
    module = setuptools.Extension(
        "google_crc32c._crc32c", sources=sources, libraries=["crc32c"], **kwargs
    )

    setuptools.setup(
        packages=["google_crc32c"],
        package_dir={"": "src"},
        ext_modules=[module],
        cmdclass={"build_ext": BuildExtWithDLL},
        install_requires=[],
    )


if CRC32C_PURE_PYTHON:
    build_pure_python()
else:
    try:
        build_c_extension()
    except SystemExit:
        if CRC32C_PURE_PYTHON_EXPLICIT:
            # If build / install fails, it is likely a compilation error with
            # the C extension:  advise user how to enable the pure-Python
            # build.
            logging.error(
                "Compiling the C Extension for the crc32c library failed. "
                "To enable building / installing a pure-Python-only version, "
                "set 'CRC32C_PURE_PYTHON=1' in the environment."
            )
            raise

        logging.info(
            "Compiling the C Extension for the crc32c library failed. "
            "Falling back to pure Python build."
        )
        build_pure_python()
