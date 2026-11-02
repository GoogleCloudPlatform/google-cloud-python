############
Contributing
############

This package is part of the ``google-cloud-python`` monorepo.

Please refer to the centralized `Contributing Guide`_ at the repository root for general guidelines on how to contribute, set up your development environment, and submit pull requests.

.. _Contributing Guide: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst

Package-specific test sessions are defined in this directory's ``noxfile.py``. Dependencies and supported Python versions are defined in ``setup.py`` or ``pyproject.toml``.

*********************
Running Unit Tests
*********************

- To run unit tests that use Memcached or Redis, you must have them running and set the appropriate environment variables:

    $ export MEMCACHED_HOSTS=localhost:11211
    $ export REDIS_CACHE_URL=redis://localhost:6379

********************
Running System Tests
********************

- System tests may be run against the emulator. To do this, set the
  ``DATASTORE_EMULATOR_HOST`` environment variable. Alternatively,
  system tests with the emulator can run with
  ``nox -e emulator-system-PYTHON_VERSION``

- For datastore tests, you'll need to create composite
  `indexes <https://cloud.google.com/datastore/docs/tools/indexconfig>`__
  with the ``gcloud`` command line
  `tool <https://developers.google.com/cloud/sdk/gcloud/>`__::

   # Install the app (App Engine Command Line Interface) component.
   $ gcloud components install app-engine-python

   # Authenticate the gcloud tool with your account.
   $ GOOGLE_APPLICATION_CREDENTIALS="path/to/app_credentials.json"
   $ gcloud auth activate-service-account \
   > --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

   # Create the indexes
   $ gcloud datastore indexes create tests/system/index.yaml
   $ gcloud alpha datastore indexes create --database=$SYSTEM_TESTS_DATABASE tests/system/index.yaml

Note on Editable Installs / Develop Mode
========================================

- Using ``setuptools`` in `develop mode`_ or a ``pip`` `editable install`_ is not possible with this library. This is because this library uses `namespace packages`_.

.. _namespace packages: https://www.python.org/dev/peps/pep-0420/
.. _develop mode: https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode
.. _editable install: https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
