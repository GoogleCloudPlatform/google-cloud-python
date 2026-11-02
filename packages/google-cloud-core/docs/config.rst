Configuration
*************

Overview
========

Use service client objects to configure your applications.

For example:

.. code-block:: python

    >>> from google.cloud import bigquery
    >>> client = bigquery.Client()

When creating a client in this way, the project ID will be determined by
searching these locations in the following order.

* GOOGLE_CLOUD_PROJECT environment variable
* GOOGLE_APPLICATION_CREDENTIALS JSON file
* Default service configuration path from
  ``$ gcloud beta auth application-default login``.
* Google App Engine application ID
* Google Compute Engine project ID (from metadata server)

You can override the detection of your default project by setting the
 ``project`` parameter when creating client objects.

.. code-block:: python

    >>> from google.cloud import bigquery
    >>> client = bigquery.Client(project='my-project')

You can see what project ID a client is referencing by accessing the ``project``
property on the client object.

.. code-block:: python

    >>> client.project
    u'my-project'

Authentication
==============

The authentication credentials can be implicitly determined from the
environment or directly. See `Authentication <https://googleapis.dev/python/google-api-core/latest/auth.html#authentication>`_.

Logging in via ``gcloud beta auth application-default login`` will
automatically configure a JSON key file with your default project ID and
credentials.

Setting the ``GOOGLE_APPLICATION_CREDENTIALS`` and ``GOOGLE_CLOUD_PROJECT``
environment variables will override the automatically configured credentials.

You can change your default project ID to ``my-new-default-project`` by
using the ``gcloud`` CLI tool to change the configuration.

.. code-block:: bash

    $ gcloud config set project my-new-default-project


Environment Variables
=====================

.. automodule:: google.cloud.environment_vars
  :members:
  :show-inheritance:
