.. _getting-started/bazel:

Bazel Build
===========

This generator can be called from `Bazel`_, which is a recommended way of using
it inside a continuous integration build or any other automated pipeline.

.. _Bazel: https://www.bazel.build/

Installing
----------

Bazel
~~~~~~
You will need Bazel version 3.0+. Please check the Bazel `website`_ for the
available installation options.

Bazel is distributed in a form of a single binary, so one of the easiest ways to
install it is simply downloading the binary and making it executable:

.. code-block:: shell

    curl -L https://github.com/bazelbuild/bazel/releases/download/3.2.0/bazel-3.2.0-linux-x86_64 -o bazel
    chmod +x bazel

.. _website: https://docs.bazel.build/versions/3.2.0/install-ubuntu.html

Python and Dependencies
~~~~~~~~~~~~~~~~~~~~~~~
Bazel build is mostly hermetic, with a few exceptions for Python generator.
Specifically it expects Python 3.10+ with the python dev packages to be installed.

On Linux, to install those, simply run:

.. code-block:: shell

    sudo apt-get install \
        python-dev \
        python3-dev

Usage
-----

.. include:: _usage_intro.rst

Example
~~~~~~~

To generate a client library with Bazel you will need a Bazel workspace. An
example of such workspace would be `googleapis`_. It is already integrated with
this this generator in its `WORKSPACE`_ file.

You need to clone the `googleapis`_ repository from GitHub:

.. code-block:: shell

  $ git clone https://github.com/googleapis/googleapis.git

The API we use as an example is the `Document AI`_ API,
available in the ``google/cloud/documentai/v1beta2/`` subdirectory.

.. _googleapis: https://github.com/googleapis/googleapis
.. _WORKSPACE: https://github.com/googleapis/googleapis/blob/master/WORKSPACE#L220
.. _Document AI: .. https://cloud.google.com/solutions/document-ai

Creating the Targets
~~~~~~~~~~~~~~~~~~~~

To build something with bazel you need to create the corresponding targets in
your ``BUILD.bazel`` file. You can use the Python section of the Document AI
`BUILD.bazel`_ file as an example:

.. code-block:: python

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

Some of the ``py_gapic_library`` rule that may be of interest:
  * ``transport``: the desired transport(s) to generate, delimited by ``+`` e.g. ``grpc+rest``.
    - Acceptable values are ``grpc`` and ``rest``.
    - Defaults to ``grpc``.

  * ``rest_numeric_enums``: if ``True``, enables generation of system parameter requesting response enums be encoded as numbers.
    - Default is ``False``.
    - Only effective when ``rest`` is included as a ``transport`` to be generated.
      
.. _BUILD.bazel: https://github.com/googleapis/googleapis/blob/master/google/cloud/documentai/v1beta2/BUILD.bazel

Compiling an API
~~~~~~~~~~~~~~~~
To generate the client library simply run the bazel command from the repository
root, specifying the py_gapic_assembly_pkg target name as the argument:

.. code-block:: shell

    bazel build //google/cloud/documentai/v1beta2:documentai-v1beta2-py

This will generate a `tar.gz` archive with the generated library packaged in it.
To unpack it in `dest` location simply run the following command from the Bazel
workspace root:

.. code-block:: shell

    tar -xzpf bazel-bin/google/cloud/documentai/v1beta2/documentai-v1beta2-py.tar.gz -C dest

.. include:: _verifying.rst
