Installation
============

You can install pandas-gbq with ``conda``, ``pip``, or by installing from source.

Conda
-----

.. code-block:: shell

   $ conda install pandas-gbq --channel conda-forge

This installs pandas-gbq and all common dependencies, including ``pandas``.

Pip
---

To install the latest version of pandas-gbq: from the

.. code-block:: shell

    $ pip install pandas-gbq -U

This installs pandas-gbq and all common dependencies, including ``pandas``.


Install from Source
-------------------

.. code-block:: shell

    $ pip install git+https://github.com/googleapis/python-bigquery-pandas.git


Dependencies
------------

This module requires following additional dependencies:

- `pydata-google-auth <https://github.com/pydata/pydata-google-auth>`__: Helpers for authentication to Google's API
- `pyarrow <https://arrow.apache.org/docs/python/>`__: Format for getting data to/from Google BigQuery
- `google-auth <https://github.com/GoogleCloudPlatform/google-auth-library-python>`__: authentication and authorization for Google's API
- `google-auth-oauthlib <https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib>`__: integration with `oauthlib <https://github.com/idan/oauthlib>`__ for end-user authentication
- `google-cloud-bigquery <https://googleapis.dev/python/bigquery/latest/index.html>`__: Google Cloud client library for BigQuery
- `google-cloud-bigquery-storage <https://googleapis.dev/python/bigquerystorage/latest/index.html>`__: Google Cloud client library for BigQuery Storage API

.. note::

   The dependency on `google-cloud-bigquery <https://googleapis.dev/python/bigquery/latest/index.html>`__ is new in version 0.3.0 of ``pandas-gbq``.
   Versions less than 0.3.0 required the following dependencies:

   - `httplib2 <https://github.com/httplib2/httplib2>`__: HTTP client (no longer required)
   - `google-api-python-client <http://github.com/google/google-api-python-client>`__: Google's API client (no longer required, replaced by `google-cloud-bigquery <hhttps://googleapis.dev/python/bigquery/latest/index.html>`__:)
   - `google-auth <https://github.com/GoogleCloudPlatform/google-auth-library-python>`__: authentication and authorization for Google's API
   - `google-auth-oauthlib <https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib>`__: integration with `oauthlib <https://github.com/idan/oauthlib>`__ for end-user authentication
   - `google-auth-httplib2 <https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2>`__: adapter to use ``httplib2`` HTTP client with ``google-auth`` (no longer required)
