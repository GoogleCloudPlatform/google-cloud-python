Base for Everything
===================

To use the API, the :class:`Client <google.cloud.bigtable.client.Client>`
class defines a high-level interface which handles authorization
and creating other objects:

.. code:: python

    from google.cloud.bigtable.client import Client
    client = Client()

Long-lived Defaults
-------------------

When creating a :class:`Client <google.cloud.bigtable.client.Client>`, the
``user_agent`` argument has sensible a default
(:data:`DEFAULT_USER_AGENT <google.cloud.bigtable.client.DEFAULT_USER_AGENT>`).
However, you may over-ride it and the value will be used throughout all API
requests made with the ``client`` you create.

Configuration
-------------

- For an overview of authentication in ``google-cloud-python``,
  see `Authentication <https://googleapis.dev/python/google-api-core/latest/auth.html#authentication>`_.

- In addition to any authentication configuration, you can also set the
  :envvar:`GOOGLE_CLOUD_PROJECT` environment variable for the Google Cloud Console
  project you'd like to interact with. If your code is running in Google App
  Engine or Google Compute Engine the project will be detected automatically.
  (Setting this environment variable is not required, you may instead pass the
  ``project`` explicitly when constructing a
  :class:`Client <google.cloud.storage.client.Client>`).

- After configuring your environment, create a
  :class:`Client <google.cloud.storage.client.Client>`

  .. code::

     >>> from google.cloud import bigtable
     >>> client = bigtable.Client()

  or pass in ``credentials`` and ``project`` explicitly

  .. code::

     >>> from google.cloud import bigtable
     >>> client = bigtable.Client(project='my-project', credentials=creds)

.. tip::

    Be sure to use the **Project ID**, not the **Project Number**.

Admin API Access
----------------

If you'll be using your client to make `Instance Admin`_ and `Table Admin`_
API requests, you'll need to pass the ``admin`` argument:

.. code:: python

    client = bigtable.Client(admin=True)

Read-Only Mode
--------------

If, on the other hand, you only have (or want) read access to the data,
you can pass the ``read_only`` argument:

.. code:: python

    client = bigtable.Client(read_only=True)

This will ensure that the
:data:`READ_ONLY_SCOPE <google.cloud.bigtable.client.READ_ONLY_SCOPE>` is used
for API requests (so any accidental requests that would modify data will
fail).

Next Step
---------

After a :class:`Client <google.cloud.bigtable.client.Client>`, the next highest-level
object is an :class:`Instance <google.cloud.bigtable.instance.Instance>`. You'll need
one before you can interact with tables or data.

Head next to learn about the :doc:`instance-api`.

.. _Instance Admin: https://github.com/googleapis/python-bigtable/blob/main/google/cloud/bigtable_admin_v2/proto/bigtable_instance_admin.proto
.. _Table Admin: https://github.com/googleapis/python-bigtable/blob/main/google/cloud/bigtable_admin_v2/proto/bigtable_table_admin.proto
