Spanner Client Usage
====================

.. _spanner-client:


Instantiating a Client
----------------------

To use the API, the :class:`~google.cloud.spanner_v1.client.Client`
class defines a high-level interface which handles authorization
and creating other objects:

.. code:: python

    from google.cloud import spanner
    client = spanner.Client()

Configuration
-------------

- For an overview of authentication in ``google.cloud-python``,
  see `Authentication
  <https://googleapis.dev/python/google-api-core/latest/auth.html>`_.

- In addition to any authentication configuration, you can also set the
  :envvar:`GCLOUD_PROJECT` environment variable for the Google Cloud Console
  project you'd like to interact with. If your code is running in Google App
  Engine or Google Compute Engine the project will be detected automatically.
  (Setting this environment variable is not required, you may instead pass the
  ``project`` explicitly when constructing a
  :class:`~google.cloud.spanner_v1.client.Client`).

- After configuring your environment, create a
  :class:`~google.cloud.spanner_v1.client.Client`

  .. code::

     >>> from google.cloud import spanner
     >>> client = spanner.Client()

  or pass in ``credentials`` and ``project`` explicitly

  .. code::

     >>> from google.cloud import spanner
     >>> client = spanner.Client(project='my-project', credentials=creds)

.. tip::

    Be sure to use the **Project ID**, not the **Project Number**.

Using a Cloud Spanner Emulator
------------------------------

There are two ways to use the client with a Cloud Spanner emulator: programmatically or via an environment variable.

To programmatically use an emulator, you must specify the project, the endpoint of the emulator, and use anonymous credentials:

.. code:: python

  from google.cloud import spanner
  from google.auth.credentials import AnonymousCredentials

  client = spanner.Client(
      project='my-project',
      client_options={"api_endpoint": "0.0.0.0:9010"},
      credentials=AnonymousCredentials()
  )

To use an emulator via an environment variable, set the `SPANNER_EMULATOR_HOST` environment variable to the emulator endpoint:

.. code::

  export SPANNER_EMULATOR_HOST=0.0.0.0:9010

Next Step
---------

After a :class:`~google.cloud.spanner_v1.client.Client`, the next
highest-level object is an :class:`~google.cloud.spanner_v1.instance.Instance`.
You'll need one before you can interact with databases.

Next, learn about the :doc:`instance-usage`.

.. _Instance Admin: https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.instance.v1
.. _Database Admin: https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.database.v1
