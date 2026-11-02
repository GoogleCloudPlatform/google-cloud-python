.. _codingstyle:

API Client Generator for Python
===============================

|release level| |pypi| |versions|

    A client library generator for APIs described through protocol buffers.

This is a generator for API client libraries for APIs
specified by `protocol buffers`_, such as those inside Google.
It takes a protocol buffer (with particular annotations) and uses it
to generate a client library.

.. _protocol buffers: https://developers.google.com/protocol-buffers/

Purpose
-------

This library replaces the `monolithic generator`_
with some improvements:

- An explicit normalized format for specifying APIs.
- Light weight, in-language code generators.

.. _monolithic generator: https://github.com/googleapis/gapic-generator


Bazel
-------------
This generator can be called from Bazel, which is a recommended way of using it inside a continuous integration build or any other automated pipeline.

Clone the googleapis repository
$ git clone https://github.com/googleapis/googleapis.git

Create the targets
------------------
You need to add the following targets to your BUILD.bazel file.

.. code-block:: c

        load(
            "@gapic_generator_python//rules_python_gapic:py_gapic.bzl",
            "py_gapic_library"
        )

        load(
            "@gapic_generator_python//rules_python_gapic:py_gapic_pkg.bzl",
            "py_gapic_assembly_pkg"
        )

        py_gapic_library(
            name = "documentai_py_gapic",
            srcs = [":documentai_proto"],
        )

        py_gapic_assembly_pkg(
            name = "documentai-v1beta2-py",
            deps = [
                ":documentai_py_gapic",
            ],
        )


Compiling an API
----------------

Using Bazel:

.. code-block:: c

        bazel build //google/cloud/documentai/v1beta2:documentai-v1beta2-py

Using Protoc:

.. code-block:: c

        # This is assumed to be in the `googleapis` project root.
        $ protoc google/cloud/vision/v1/*.proto \
            --python_gapic_out=/dest/

Development
-------------
`Development`_

.. _Development: https://github.com/googleapis/gapic-generator-python/blob/main/DEVELOPMENT.md

Contributing
-------------
If you are looking to contribute to the project, please see `Contributing`_
for guidlines.

.. _Contributing: https://github.com/googleapis/gapic-generator-python/blob/main/CONTRIBUTING.md

Documentation
-------------

See the `documentation`_.

.. _documentation: https://googleapis.dev/python/gapic-generator/latest/

.. |release level| image:: https://img.shields.io/badge/support-stable-gold.svg
  :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
.. |pypi| image:: https://img.shields.io/pypi/v/gapic-generator.svg
  :target: https://pypi.org/project/gapic-generator/
.. |versions| image:: https://img.shields.io/pypi/pyversions/gapic-generator.svg
  :target: https://pypi.org/project/gapic-generator/
