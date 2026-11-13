Creating a Client
~~~~~~~~~~~~~~~~~

A project is the top-level container in the ``BigQuery`` API:  it is tied
closely to billing, and can provide default access control across all its
datasets.  If no ``project`` is passed to the client container, the library
attempts to infer a project using the environment (including explicit
environment variables, GAE, and GCE).

To override the project inferred from the environment, pass an explicit
``project`` to the :class:`~google.cloud.bigquery.client.Client` constructor,
or to either of the alternative ``classmethod`` factories:

.. code-block:: python

   from google.cloud import bigquery
   client = bigquery.Client(project='PROJECT_ID')


Project ACLs
^^^^^^^^^^^^

Each project has an access control list granting reader / writer / owner
permission to one or more entities.  This list cannot be queried or set
via the API; it must be managed using the Google Developer Console.
