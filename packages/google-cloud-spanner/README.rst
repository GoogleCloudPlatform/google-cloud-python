Python Client for Cloud Spanner
===============================

|stable| |pypi| |versions|

`Cloud Spanner`_: Cloud Spanner is a managed, mission-critical, globally consistent and
scalable relational database service.

- `Client Library Documentation`_
- `Product Documentation`_

.. |stable| image:: https://img.shields.io/badge/support-stable-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-spanner.svg
   :target: https://pypi.org/project/google-cloud-spanner/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-spanner.svg
   :target: https://pypi.org/project/google-cloud-spanner/
.. _Cloud Spanner: https://cloud.google.com/spanner/
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/spanner/latest/summary_overview
.. _Product Documentation:  https://cloud.google.com/spanner/

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud Spanner.`_
4. `Set up Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud Spanner.:  https://cloud.google.com/spanner/
.. _Set up Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a virtual environment using `venv`_. `venv`_ is a tool that
creates isolated Python environments. These isolated environments can have separate
versions of Python packages, which allows you to isolate one project's dependencies
from the dependencies of other projects.

With `venv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`venv`: https://docs.python.org/3/library/venv.html


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the `samples/`_ folder.

.. _samples/: https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-spanner/samples


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.10, including 3.14

.. _active: https://devguide.python.org/devcycle/#in-development-main-branch
.. _maintenance: https://devguide.python.org/devcycle/#maintenance-branches

Unsupported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.9


If you are using an `end-of-life`_
version of Python, we recommend that you update as soon as possible to an actively supported version.

.. _end-of-life: https://devguide.python.org/devcycle/#end-of-life-branches

Mac/Linux
^^^^^^^^^

.. code-block:: console

    python3 -m venv <your-env>
    source <your-env>/bin/activate
    pip install google-cloud-spanner


Windows
^^^^^^^

.. code-block:: console

    py -m venv <your-env>
    .\<your-env>\Scripts\activate
    pip install google-cloud-spanner


Example Usage
-------------


Executing Arbitrary SQL in a Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally, to work with Cloud Spanner, you will want a transaction. The
preferred mechanism for this is to create a single function, which executes
as a callback to ``database.run_in_transaction``:

.. code:: python

    # First, define the function that represents a single "unit of work"
    # that should be run within the transaction.
    def update_anniversary(transaction, person_id, unix_timestamp):
        # The query itself is just a string.
        #
        # The use of @parameters is recommended rather than doing your
        # own string interpolation; this provides protections against
        # SQL injection attacks.
        query = """SELECT anniversary FROM people
            WHERE id = @person_id"""

        # When executing the SQL statement, the query and parameters are sent
        # as separate arguments. When using parameters, you must specify
        # both the parameters themselves and their types.
        row = transaction.execute_sql(
            query=query,
            params={'person_id': person_id},
            param_types={
                'person_id': types.INT64_PARAM_TYPE,
            },
        ).one()

        # Now perform an update on the data.
        old_anniversary = row[0]
        new_anniversary = _compute_anniversary(old_anniversary, years)
        transaction.update(
            'people',
            ['person_id', 'anniversary'],
            [person_id, new_anniversary],
        )

    # Actually run the `update_anniversary` function in a transaction.
    database.run_in_transaction(update_anniversary,
        person_id=42,
        unix_timestamp=1335020400,
    )


Select records using a Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have a transaction object (such as the first argument sent to
``run_in_transaction``), reading data is easy:

.. code:: python

    # Define a SELECT query.
    query = """SELECT e.first_name, e.last_name, p.telephone
        FROM employees as e, phones as p
        WHERE p.employee_id == e.employee_id"""

    # Execute the query and return results.
    result = transaction.execute_sql(query)
    for row in result.rows:
        print(row)


Insert records using Data Manipulation Language (DML) with a Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``execute_update()`` method to execute a DML statement:

.. code:: python

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_singers(transaction):
        row_ct = transaction.execute_update(
            "INSERT Singers (SingerId, FirstName, LastName) "
            " VALUES (10, 'Virginia', 'Watson')"
        )

        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(insert_singers)


Insert records using Mutations with a Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add one or more records to a table, use ``insert``:

.. code:: python

    transaction.insert(
        'citizens',
        columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['phred@example.com', 'Phred', 'Phlyntstone', 32],
            ['bharney@example.com', 'Bharney', 'Rhubble', 31],
        ],
    )


Update records using Data Manipulation Language (DML) with a Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_albums(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Albums "
            "SET MarketingBudget = MarketingBudget * 2 "
            "WHERE SingerId = 1 and AlbumId = 1"
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(update_albums)


Update records using Mutations with a Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Transaction.update`` updates one or more existing records in a table.  Fails
if any of the records does not already exist.

.. code:: python

    transaction.update(
        'citizens',
        columns=['email', 'age'],
        values=[
            ['phred@example.com', 33],
            ['bharney@example.com', 32],
        ],
    )


Connection API
--------------
Connection API represents a wrap-around for Python Spanner API, written in accordance with PEP-249, and provides a simple way of communication with a Spanner database through connection objects:

.. code:: python

   from google.cloud.spanner_dbapi.connection import connect

   connection = connect("instance-id", "database-id")
   connection.autocommit = True

   cursor = connection.cursor()   
   cursor.execute("SELECT * FROM table_name")

   result = cursor.fetchall()


If using [fine-grained access controls](https://cloud.google.com/spanner/docs/access-with-fgac) you can pass a ``database_role`` argument to connect as that role:

.. code:: python

   connection = connect("instance-id", "database-id", database_role='your-role')


Aborted Transactions Retry Mechanism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``!autocommit`` mode, transactions can be aborted due to transient errors. In most cases retry of an aborted transaction solves the problem. To simplify it, connection tracks SQL statements, executed in the current transaction. In case the transaction aborted, the connection initiates a new one and re-executes all the statements. In the process, the connection checks that retried statements are returning the same results that the original statements did. If results are different, the transaction is dropped, as the underlying data changed, and auto retry is impossible.

Auto-retry of aborted transactions is enabled only for ``!autocommit`` mode, as in ``autocommit`` mode transactions are never aborted.


Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud Spanner
   to see other available methods on the client.
-  Read the `Cloud Spanner Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Cloud Spanner Product documentation:  https://cloud.google.com/spanner/
.. _README: https://github.com/googleapis/google-cloud-python/blob/main/README.rst

Logging
-------

This library uses the standard Python :code:`logging` functionality to log some RPC events that could be of interest for debugging and monitoring purposes.
Note the following:

#. Logs may contain sensitive information. Take care to **restrict access to the logs** if they are saved, whether it be on local storage or on Google Cloud Logging.
#. Google may refine the occurrence, level, and content of various log messages in this library without flagging such changes as breaking. **Do not depend on immutability of the logging events**.
#. By default, the logging events from this library are not handled. You must **explicitly configure log handling** using one of the mechanisms below.

Simple, environment-based configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable logging for this library without any changes in your code, set the :code:`GOOGLE_SDK_PYTHON_LOGGING_SCOPE` environment variable to a valid Google
logging scope. This configures handling of logging events (at level :code:`logging.DEBUG` or higher) from this library in a default manner, emitting the logged
messages in a structured format. It does not currently allow customizing the logging levels captured nor the handlers, formatters, etc. used for any logging
event.

A logging scope is a period-separated namespace that begins with :code:`google`, identifying the Python module or package to log.

- Valid logging scopes: :code:`google`, :code:`google.cloud.asset.v1`, :code:`google.api`, :code:`google.auth`, etc.
- Invalid logging scopes: :code:`foo`, :code:`123`, etc.

**NOTE**: If the logging scope is invalid, the library does not set up any logging handlers.

Environment-Based Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Enabling the default handler for all Google-based loggers

.. code-block:: console

    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google

- Enabling the default handler for a specific Google module (for a client library called :code:`library_v1`):

.. code-block:: console

    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google.cloud.library_v1


Advanced, code-based configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also configure a valid logging scope using Python's standard `logging` mechanism.

Code-Based Examples
^^^^^^^^^^^^^^^^^^^

- Configuring a handler for all Google-based loggers

.. code-block:: python

    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)

- Configuring a handler for a specific Google module (for a client library called :code:`library_v1`):

.. code-block:: python

    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google.cloud.library_v1")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)

Logging details
~~~~~~~~~~~~~~~

#. Regardless of which of the mechanisms above you use to configure logging for this library, by default logging events are not propagated up to the root
   logger from the `google`-level logger. If you need the events to be propagated to the root logger, you must explicitly set
   :code:`logging.getLogger("google").propagate = True` in your code.
#. You can mix the different logging configurations above for different Google modules. For example, you may want use a code-based logging configuration for
   one library, but decide you need to also set up environment-based logging configuration for another library.

   #. If you attempt to use both code-based and environment-based configuration for the same module, the environment-based configuration will be ineffectual
      if the code -based configuration gets applied first.

#. The Google-specific logging configurations (default handlers for environment-based configuration; not propagating logging events to the root logger) get
   executed the first time *any* client library is instantiated in your application, and only if the affected loggers have not been previously configured.
   (This is the reason for 2.i. above.)
