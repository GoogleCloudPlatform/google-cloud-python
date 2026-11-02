@rem Copyright 2019 Google LLC. All rights reserved.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem     http://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.


setlocal ENABLEDELAYEDEXPANSION

cd /d "%~dp0..\.." || goto :error

set CRC32C_PURE_PYTHON=0
set CMAKE_GENERATOR="Visual Studio 17 2022"
set CONFIGURATION=RelWithDebInfo
set CRC32C_INSTALL_PREFIX=%cd%\build\%CONFIGURATION%

@rem Iterate through supported Python versions.
@rem Unfortunately pyenv for Windows has an out-of-date versions list. Choco's
@rem installer seems to have some problems with installing multiple versions at
@rem once, so as a workaround, we will install and then uninstall every version.
for /f "tokens=2 delims=:" %%A in ('findstr /b "versions:" "%~dp0..\python_versions.yaml"') do set SUPPORTED_PYTHON_VERSIONS=%%A
@rem Set PY_PYTHON3 to the first (lowest supported) version in python_versions.yaml so py -3 uses a stable version.
for /f "tokens=1 delims= " %%V in ("%SUPPORTED_PYTHON_VERSIONS%") do for /f "tokens=1,2 delims=." %%I in ("%%V") do set PY_PYTHON3=%%I.%%J
FOR %%P IN (%SUPPORTED_PYTHON_VERSIONS%) DO (
    set python_version=%%P
    for /f "tokens=1,2 delims=." %%I in ("%%P") do set python_version_trimmed=%%I.%%J

    for /L %%R in (1,1,5) do (
        py -!python_version_trimmed!-64 --version >nul 2>&1 || (
            echo "Installing Python version %%P (attempt %%R/5)"
            @rem Format pre-release version for Chocolatey (e.g. 3.15.0a1 -> 3.15.0-a1)
            set CHOCO_VER=%%P
            set CHOCO_VER=!CHOCO_VER:0a=0-a!
            set CHOCO_VER=!CHOCO_VER:0b=0-b!
            set CHOCO_VER=!CHOCO_VER:0rc=0-rc!
            choco install python --version=!CHOCO_VER! --pre -y --no-progress || (
                echo "choco install %%P failed; retrying in 15s..."
                py -3 -c "import time; time.sleep(15)"
            )
        )
    )
    py -!python_version_trimmed!-64 --version >nul 2>&1 || goto :error

    echo "Listing available Python versions"
    py -0

    py -!python_version_trimmed!-64 -m pip install --upgrade pip || goto :error

    echo "Installing cmake for Python %%P"
    py -!python_version_trimmed!-64 -m pip install cmake || goto :error

    @rem Add directory as safe to avoid "detected dubious ownership" fatal issue
    git config --global --add safe.directory *
    git submodule update --init --recursive || goto :error
    pushd google_crc32c || goto :error
    @rem reset hard to cleanup any changes done by a previous build.
    git reset --hard
    git clean -fxd

    del /s /q CMakeFiles\
    del CMakeCache.txt

    mkdir build
    cd build

    echo "Running cmake with Generator:  %CMAKE_GENERATOR%, Platform: x64, Install Prefix: %CRC32C_INSTALL_PREFIX%"

    py -!python_version_trimmed!-64 -m cmake -G "Visual Studio 17 2022" -A x64 -DCMAKE_POLICY_VERSION_MINIMUM=3.12 -DCRC32C_BUILD_BENCHMARKS=no -DCRC32C_BUILD_TESTS=no -DBUILD_SHARED_LIBS=yes -DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=yes -DCRC32C_USE_GLOG=0 -DCMAKE_INSTALL_PREFIX:PATH="%CRC32C_INSTALL_PREFIX%" .. || goto :error

    py -!python_version_trimmed!-64 -m cmake --build . --config "%CONFIGURATION%" --target install || goto :error

    dir %CRC32C_INSTALL_PREFIX% /b /s
    popd

    dir  %CRC32C_INSTALL_PREFIX%\bin
    echo "Copying Binary to root: %CRC32C_INSTALL_PREFIX%\bin\crc32c.dll"
    copy %CRC32C_INSTALL_PREFIX%\bin\crc32c.dll . || goto :error

    py -!python_version_trimmed!-64 -m pip install --upgrade pip setuptools wheel || goto :error
    echo "Building C extension"
    py -!python_version_trimmed!-64 setup.py build_ext -v --include-dirs=%CRC32C_INSTALL_PREFIX%\include --library-dirs=%CRC32C_INSTALL_PREFIX%\lib || goto :error
    echo "Building Wheel"
    py -!python_version_trimmed!-64 -m pip wheel . --wheel-dir wheels/ || goto :error

    echo "Built wheel, now running tests."
    call %~dp0/test.bat !python_version_trimmed! || goto :error

    echo "Finished with Python version %P"
)

echo "Built wheels in wheels/ directory:"
dir wheels\*.whl || goto :error

for %%P in (%SUPPORTED_PYTHON_VERSIONS%) do (
    for /f "tokens=1,2 delims=." %%I in ("%%P") do set py_tag=cp%%I%%J
    dir wheels\*!py_tag!*.whl >nul || (
        echo "ERROR: Missing Windows wheel for !py_tag!!"
        goto :error
    )
)

echo "Validating built wheels with twine check"
py -3 -m pip install --upgrade twine wheel setuptools pkginfo || goto :error

echo "Build the source distribution (sdist) and validate with twine check"
py -3 setup.py sdist || goto :error
py -3 -m twine check dist/* wheels/* || goto :error

if "%PUBLISH_WHEELS%"=="true" (
    echo "Start the releasetool reporter"
    py -3 -m pip install gcp-releasetool || goto :error
    if not exist C:\temp mkdir C:\temp
    py -3 -m releasetool publish-reporter-script > C:\temp\publisher-script || goto :error

    echo "Disable buffering, so that the logs stream through."
    set PYTHONUNBUFFERED=1

    echo "## RELEASE WORKFLOW SUCCESSFUL ##"
    echo "## Uploading Wheels and sdist ##"

    set /p TWINE_PASSWORD=<%KOKORO_KEYSTORE_DIR%/73713_google-cloud-pypi-token-keystore-3
    py -3 -m twine upload --skip-existing --username __token__ --password "!TWINE_PASSWORD!" dist/* wheels/* || goto :error
    dir wheels
    dir dist
) else (
    echo "PUBLISH_WHEELS is '%PUBLISH_WHEELS%'. Skipping PyPI upload after sdist and wheel validation."
)

goto :EOF

:error
exit /b 1
