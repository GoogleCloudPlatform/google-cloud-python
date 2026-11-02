############
Contributing
############

This package is part of the ``google-cloud-python`` monorepo.

Please refer to the centralized `Contributing Guide`_ at the repository root for general guidelines on how to contribute, set up your development environment, and submit pull requests.

.. _Contributing Guide: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst

Package-specific test sessions are defined in this directory's ``noxfile.py``. Dependencies and supported Python versions are defined in ``setup.py`` or ``pyproject.toml``.

**************************
Updating Conformance Tests
**************************

The firestore client libraries use a shared set of conformance tests, the source of which can be found at https://github.com/googleapis/conformance-tests.

To update the copy of these conformance tests used by this repository, run the provided Makefile:

   $ make -f Makefile_v1
