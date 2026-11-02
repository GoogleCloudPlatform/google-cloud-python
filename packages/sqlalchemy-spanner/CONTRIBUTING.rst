############
Contributing
############

This package is part of the ``google-cloud-python`` monorepo.

Please refer to the centralized `Contributing Guide`_ at the repository root for general guidelines on how to contribute, set up your development environment, and submit pull requests.

.. _Contributing Guide: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst

Package-specific test sessions are defined in this directory's ``noxfile.py``. Dependencies and supported Python versions are defined in ``setup.py`` or ``pyproject.toml``.

********************
Running Tests
********************

SQLAlchemy Spanner dialect includes a test suite, which can be executed both on a live service and Spanner emulator.

**Using pytest**
To execute the test suite with standard ``pytest`` package you only need to checkout to the package folder and run::

    pytest -v

**Using nox**
The package includes a configuration file for ``nox`` package, which allows to execute the dialect test suite in an isolated virtual environment. To execute all the ``nox`` sessions checkout to the dialect folder and then run command::

    nox

To execute only the dialect compliance test suite execute command::

    nox -s compliance_test

**Live service**
To run the test suite on a live service use ``setup.cfg`` ``db.default`` attribute to set URI of the project, instance and database, where the tests should be executed.

**Emulator**
As the dialect is built on top of the Spanner DB API, it also supports running on Spanner emulator. To make it happen you need to set an environment variable, pointing to the emulator service, for example ``SPANNER_EMULATOR_HOST=localhost:9010``
