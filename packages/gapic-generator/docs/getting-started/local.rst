.. _getting-started/local:

Local Installation
==================

This tool offers first-class support for local execution using
``protoc``. It is still reasonably easy, but initial setup will take a bit
longer.

.. note::

    If you are interested in contributing, setup according to these steps
    is recommended.


Installing
----------

protoc
~~~~~~

This tool is implemented as a plugin to the `protocol buffers`_ compiler, so
in order to use it, you will need to have the ``protoc`` command available.

The `release page`_ on GitHub contains the download you need.

.. note::

  You may notice both packages that designate languages (e.g.
  ``protobuf-python-X.Y.Z.tar.gz``) as well as packages that
  designate architectures (e.g. ``protoc-X.Y.Z-linux-x86_64.zip``). You want
  the one that designates an architecture; your goal here is to have a CLI
  command.

.. _protocol buffers: https://developers.google.com/protocol-buffers/
.. _release page: https://github.com/google/protobuf/releases

It is likely preferable to install ``protoc`` somewhere on your shell's path,
but this is not a strict requirement (as you will be invoking it directly).
``protoc`` is also quirky about how it handles well-known protos; you probably
also want to copy them into ``/usr/local/include``

To ensure it is installed propertly:

.. code-block:: shell

  $ protoc --version
  libprotoc 3.6.0


pandoc
~~~~~~

This generator relies on `pandoc`_ to convert from Markdown (the *lingua
franca* for documentation in protocol buffers) into ReStructured Text (the
*lingua franca* for documentation in Python).

Install this using an appropriate mechanism for your operating system.
Multiple installation paths are documented on the `pandoc installation page`_.

.. _pandoc: https://pandoc.org/
.. _pandoc installation page: https://pandoc.org/installing.html


API Generator for Python
~~~~~~~~~~~~~~~~~~~~~~~~

This package is provided as a standard Python library, and can be installed
the usual ways. It fundamentally provides a CLI command,
``protoc-gen-python_gapic``, (yes, the mismatch of ``kebob-case`` and
``snake_case`` is weird, sorry), so you will want to install using a mechanism
that is conducive to making CLI commands available.

.. code-block:: shell

    # Install this package using
    pip install gapic-generator

    # Install a version of python that is supported by the microgenerator.
    # We use 3.9.12 as an example.
    # You may need to install additional packages in order to
    # build python from source.
    # Setting a 'global' python is convenient for development but may interfere
    # with other system activities. Adjust as your environment requires.
    pyenv install 3.9.12 && pyenv global 3.9.12

    # Install the tool. This will handle the virtualenv for you, and
    # make an appropriately-aliased executable.
    # The `--editable` flag is only necessary if you want to work on the
    # tool (as opposed to just use it).
    python -m pip install --editable .

To ensure the tool is installed properly:

.. code-block:: shell

  $ which protoc-gen-python_gapic
  /path/to/protoc-gen-python_gapic

.. _pyenv: https://github.com/pyenv/pyenv

Usage
-----

.. include:: _usage_intro.rst

Example
~~~~~~~

.. include:: _example.rst

You will also need the common protos, which define certain client-specific annotations.
These are in the `api-common-protos`_ repository.
Clone this from GitHub also:

.. code-block:: shell

  $ git clone https://github.com/googleapis/api-common-protos.git

.. _api-common-protos: https://github.com/googleapis/api-common-protos/tree/input-contract


Compiling an API
~~~~~~~~~~~~~~~~

Compile the API into a client library by invoking ``protoc`` directly.
This plugin is invoked under the hood via. the ``--python_gapic_out`` switch.

.. code-block:: shell

  # This is assumed to be in the `googleapis` project root, and we also
  # assume that api-common-protos is next to it.
  $ protoc google/cloud/vision/v1/*.proto \
      --proto_path=../api-common-protos/ --proto_path=. \
      --python_gapic_out=/dest/

.. note::

  **A reminder about paths.**

  Remember that ``protoc`` is particular about paths. It requires all paths
  where it expects to find protos, and *order matters*. In this case,
  the common protos must come first, and then the path to the API being built.

.. include:: _samplegen.rst

.. code-block:: shell

  # Multiple sample paths or directories can be passed simultaneously by duplicating
  # the 'samples' option. Options are comma delimited.
  # If no 'samples' option is passed, the generator does not generate a manifest.
  $ protoc path/to/api/protos/*.proto \
                --proto_path=../api-common-protos/ \
                --proto_path=. \
                --python_gapic_opt="samples=sample_config.yaml,samples=sample_dir/" \
                --python_gapic_out=/dest/


.. include:: _verifying.rst
