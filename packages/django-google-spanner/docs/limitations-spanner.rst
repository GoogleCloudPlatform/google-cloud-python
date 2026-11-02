Limitations from Spanner perspective
------------------------------------

Below is a List of Limitations for features that are supported in Spanner but 
are not supported in the Django Spanner library. Some features have been 
disabled because of compatibility issues using the Django feature toggle.

Query Hints
~~~~~~~~~~~
Django automatically manages query generation and thus does not expose methods
to add query hints directly. While libraries can add support for this feature 
and manage the query generation part, we have not added this because of the 
added complexity. The workaround to use this feature is by using Raw Queries 
directly, and adding Query hints there.

Mutations
~~~~~~~~~
Mutations are not a concept that is understood by Django so it does not support
it inherently. The workaround is to use python-spanner objects and run Mutations using that.

Batch DDL
~~~~~~~~~
Migrations (creation and updation) of tables in Django are sequential operations. 
Django doesn't inherently support doing batch DDL operations. However, customers 
can use python-spanner objects to run batch DDL for unmanaged tables in Django.

Stale Reads
~~~~~~~~~~~
Stale Reads are not a concept that is understood by Django so it does not support 
it inherently. The workaround is to use python-spanner objects and run read operations on snapshots.

Interleaving
~~~~~~~~~~~~
Interleaving is not a concept that is understood by Django so it does not support 
it inherently. The workaround is to use Unmanaged tables and python-spanner objects 
to create and manage interleaved tables.


Partitioned DML
~~~~~~~~~~~~~~~
Partitioned DML is not a concept that is understood by Django so it does not support 
it inherently. The workaround is to use python-spanner objects to perform partitioned 
DML operations.

Session Labeling
~~~~~~~~~~~~~~~~
Django does not support session pools for databases directly and does not have the 
concept of session labeling itself. The workaround is to use python-spanner objects 
to create and manage sessions along with Session labels.

Request Priority
~~~~~~~~~~~~~~~~
Request Priority for database calls is not a concept that is understood by Django so 
it does not support it inherently. The workaround is to use python-spanner objects 
and use request priority as part of the db calls.

Tagging
~~~~~~~
Tagging for database calls is not a concept that is understood by Django so it does not 
support it inherently. The workaround is to use python-spanner objects and use the 
tagging feature via that.

Configurable Leader Option
~~~~~~~~~~~~~~~~~~~~~~~~~~
Configuring Leader Option for database calls is not a concept that is understood by 
Django so it does not support it inherently. The workaround is to use python-spanner 
objects while creating the database.

Backups / Cross region Backups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Backups for databases are not managed by Django so it does not support it inherently. 
In general, none of the Spanner ORMs / drivers are expected to support backup management.
The workaround is to use python-spanner objects and use backup features via that.

Custom Instance Config
~~~~~~~~~~~~~~~~~~~~~~
Instances for spanner are not managed by Django so it does not support it inherently. 
The workaround is to use python-spanner objects and use Instance config features via that.

Workaround
----------

.. list-table::
   :widths: 33 67
   :header-rows: 1

   * - Features
     - Is a workaround available?
   * - Query Hints
     - Raw Queries can be used for Query hints `Link <https://stackoverflow.com/a/28350704/3027854>`__.
   * - Mutations
     - Python-spanner database objects can be used to run Mutation queries. `Link <https://cloud.google.com/spanner/docs/modify-mutation-api#python>`__.
   * - Batch DDL
     - Using unmanaged tables in Django. `Link <https://docs.djangoproject.com/en/4.0/ref/models/options/#managed>`__ and Directly using Python spanner objects to execute batch DDL statements. `Link <https://cloud.google.com/spanner/docs/getting-started/python#create_a_database>`__.
   * - Stale Reads
     - Python-spanner database objects can be used to perform stale reads. `Link <https://cloud.google.com/spanner/docs/reads#python>`__.
   * - Interleaving
     - Using unmanaged tables in Django. `Link <https://docs.djangoproject.com/en/4.0/ref/models/options/#managed>`__ and Directly using Python spanner objects to create interleaved tables. `Link <https://cloud.google.com/spanner/docs/getting-started/python#create_a_database>`__.
   * - Partitioned DML
     - Python-spanner database objects can be used to perform Partitioned DML. `Link <https://cloud.google.com/spanner/docs/dml-partitioned#python>`__.
   * - Session Labeling
     - Python-spanner connection objects can be used to perform Session creation and labeling . `Link <https://cloud.google.com/spanner/docs/sessions#python>`__.
   * - Request Priority
     - Python-spanner connection objects can be used to make backend calls with request priority. `Link <https://cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions>`__.
   * - Tagging
     - Python-spanner connection objects can be used to make backend calls with request tags. `Link <https://cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions>`__.
   * - Configurable Leader Option
     - Python-spanner database objects can be used to set or update leader options. `Link <https://cloud.google.com/spanner/docs/modifying-leader-region#python>`__.
   * - Cross region backup
     - Python-spanner library can be used to perform db backups across regions. `Link <https://cloud.google.com/spanner/docs/backup>`__.
   * - Custom Instance Config
     - Python-spanner library can be used to manage instances. `Link <https://googleapis.dev/python/spanner/latest/instance-api.html>`__.
