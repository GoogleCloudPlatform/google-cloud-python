
# Building

## Be sure to check out all submodules:

```
$ git clone --recursive https://github.com/googleapis/python-crc32c
```

## Building and Testing Wheels

The scripts directory contains multiple scripts for building. They are also
used by the CI workflows which can be found at .github/workflows.

On Linux:

```
./scripts/manylinux/build.sh


# Install the wheel that was built as a result
pip install --no-index --find-links=wheels google-crc32c

# Check the package, try and load the native library.
python ./scripts/check_crc32c_extension.py
```

On OS X:

```
# Build the C library and wheel
./scripts/osx/build.sh

# Install the wheel that was built as a result
pip install --no-index --find-links=wheels google-crc32c

# Check the package, try and load the native library.
python ./scripts/check_crc32c_extension.py
```

On Windows:

```
.\scripts\windows\build.bat
.\scripts\windows\test.bat
```


## Installing locally for testing

Initialize the submodules and build the main `libcrc32c.so` shared
library using `cmake` / `make`:

```bash
$ cd python-crc32c
$ git submodule update --init --recursive
$ python -m venv venv
$ venv/bin/pip install --upgrade setuptools pip wheel
$ venv/bin/pip install cmake
$ mkdir usr
$ export CRC32C_INSTALL_PREFIX=$(pwd)/usr
$ mkdir google_crc32c/build
$ cd google_crc32c/build
$ ../../venv/bin/cmake \
>   -DCMAKE_BUILD_TYPE=Release \
>   -DCRC32C_BUILD_TESTS=no \
>   -DCRC32C_BUILD_BENCHMARKS=no \
>   -DBUILD_SHARED_LIBS=yes \
>   -DCMAKE_INSTALL_PREFIX:PATH=${CRC32C_INSTALL_PREFIX} \
>   ..
$ make all install
$ cd ../..
```

Now, run the tests:

```bash
$ venv/bin/python setup.py build_ext \
    --include-dirs=$(pwd)/usr/include \
    --library-dirs=$(pwd)/usr/lib \
    --rpath=$(pwd)/usr/lib
$ venv/bin/pip install -e .[testing]
$ venv/bin/py.test tests/
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-3.10.0, py-1.7.0, pluggy-0.8.0
rootdir: ..., inifile:
collected 9 items

tests/test___init__.py .........                                         [100%]

=========================== 9 passed in 0.03 seconds ===========================
```
