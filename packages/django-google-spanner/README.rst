Cloud Spanner support for Django
================================

|GA| |pypi| |versions|

`Cloud Spanner`_ is the world's first fully managed relational database service
to offer both strong consistency and horizontal scalability for
mission-critical online transaction processing (OLTP) applications. With Cloud
Spanner you enjoy all the traditional benefits of a relational database; but
unlike any other relational database service, Cloud Spanner scales horizontally
to hundreds or thousands of servers to handle the biggest transactional
workloads.


- `Client Library Documentation`_
- `Product Documentation`_

.. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
.. |pypi| image:: https://img.shields.io/pypi/v/django-google-spanner.svg
   :target: https://pypi.org/project/django-google-spanner/
.. |versions| image:: https://img.shields.io/pypi/pyversions/django-google-spanner.svg
   :target: https://pypi.org/project/django-google-spanner/
.. _Cloud Spanner: https://cloud.google.com/spanner/
.. _Client Library Documentation: https://googleapis.dev/python/django-google-spanner/latest/index.html
.. _Product Documentation:  https://cloud.google.com/spanner/docs

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Google Cloud Spanner API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Google Cloud Spanner API.:  https://cloud.google.com/spanner
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

This package provides a `3rd-party database backend
<https://docs.djangoproject.com/en/5.2/ref/databases/#using-a-3rd-party-database-backend>`__
for using `Cloud Spanner <https://cloud.google.com/spanner>`__ with the `Django
ORM <https://docs.djangoproject.com/en/5.2/topics/db/>`__. It uses the `Cloud
Spanner Python client library <https://github.com/googleapis/python-spanner>`__
under the hood.

Installation
------------

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python and Django environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Supported versions
~~~~~~~~~~~~~~~~~~

The library supports `Django 5.2
<https://docs.djangoproject.com/en/5.2/>`_ and `Django 6.0
<https://docs.djangoproject.com/en/6.0/>`_.
The minimum required Python version is 3.10.

.. code:: shell

    pip3 install "django>=5.2,<6.1"


Installing the package
~~~~~~~~~~~~~~~~~~~~~~

To install from PyPI:

.. code:: shell

    pip3 install django-google-spanner


To install from source:

.. code:: shell

    git clone git@github.com:googleapis/google-cloud-python.git
    cd packages/django-google-spanner
    pip3 install -e .


Creating a Cloud Spanner instance and database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't already have a Cloud Spanner database, or want to start from
scratch for a new Django application, you can `create a new instance
<https://cloud.google.com/spanner/docs/getting-started/python#create_an_instance>`__
and `database
<https://cloud.google.com/spanner/docs/getting-started/python#create_a_database>`__
using the Google Cloud SDK:

.. code:: shell

    gcloud spanner instances create $INSTANCE --config=regional-us-central1 --description="New Django Instance" --nodes=1
    gcloud spanner databases create $DB --instance $INSTANCE


Configuring ``settings.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package provides a Django application named ``django_spanner``. To use the
Cloud Spanner database backend, the application needs to installed and
configured:

-  Add ``django_spanner`` as the first entry in ``INSTALLED_APPS``:

   .. code:: python

       INSTALLED_APPS = [
           'django_spanner',
           ...
       ]

-  Edit the ``DATABASES`` setting to point to an existing Cloud Spanner database:

   .. code:: python

       DATABASES = {
           'default': {
               'ENGINE': 'django_spanner',
               'PROJECT': '$PROJECT',
               'INSTANCE': '$INSTANCE',
               'NAME': '$DATABASE',
           }
       }

Configuring primary key generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Spanner Django engine by default uses random int64 values that are generated
by the client as primary key values. This default is applied to all databases that are
configured, including databases that use a different engine than Spanner. You can
disable this behavior with the RANDOM_ID_GENERATION_ENABLED setting:

   .. code:: python

       DATABASES = {
           'default': {
               'ENGINE': 'django_spanner',
               'PROJECT': '$PROJECT',
               'INSTANCE': '$INSTANCE',
               'NAME': '$DATABASE',
               'RANDOM_ID_GENERATION_ENABLED': false,
           }
       }



Transaction support in autocommit mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Django supports transactions in autocommit mode by default.
A transaction is automatically started if you define an
`atomic block <https://docs.djangoproject.com/en/5.2/topics/db/transactions/#controlling-transactions-explicitly>`__.

To disable transactions in autocommit mode, set the flag `ALLOW_TRANSACTIONS_IN_AUTO_COMMIT` to False in your ``settings.py`` file.


Set credentials and project environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You'll need to download a service account JSON key file and point to it using an environment variable:

.. code:: shell

    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/keyfile.json
    export GOOGLE_CLOUD_PROJECT=gcloud_project


Apply the migrations
~~~~~~~~~~~~~~~~~~~~

Please run:

.. code:: shell

    $ python3 manage.py migrate

That'll take a while to run. After this you should be able to see the tables and indexes created in your Cloud Spanner console.


Create a Django admin user
~~~~~~~~~~~~~~~~~~~~~~~~~~~
First you’ll need to create a user who can login to the admin site. Run the following command:

.. code:: shell

    $ python3 manage.py createsuperuser

which will then produce a prompt which will allow you to create your super user

.. code:: shell

    Username: admin
    Email address: admin@example.com
    Password: **********
    Password (again): **********
    Superuser created successfully.


Login as admin
~~~~~~~~~~~~~~
Now, run the server

.. code:: shell

    python3 manage.py runserver

Then visit http://127.0.0.1:8000/admin/

Create and register your first model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please follow the guides in https://docs.djangoproject.com/en/5.2/intro/tutorial02/#creating-models
to create and register the model to the Django’s automatically-generated admin site.

How it works
------------

Overall design
~~~~~~~~~~~~~~

.. figure:: https://raw.githubusercontent.com/googleapis/google-cloud-python/main/assets/overview.png
   :alt: "Overall Design"

Internals
~~~~~~~~~

.. figure:: https://raw.githubusercontent.com/googleapis/google-cloud-python/main/assets/internals.png
   :alt: "Internals"


Executing a query
~~~~~~~~~~~~~~~~~

Here is an example of how to add a row for Model Author, save it and later query it using Django

.. code:: shell

    >>> author_kent = Author( first_name="Arthur", last_name="Kent", rating=Decimal("4.1"),)
    >>> author_kent.save()
    >>> qs1 = Author.objects.all().values("first_name", "last_name")


How to contribute
~~~~~~~~~~~~~~~~~

Contributions to this library are always welcome and highly encouraged.

See `CONTRIBUTING <https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.md>`_ for more information on how to get started.

Please note that this project is released with a Contributor Code of Conduct.
By participating in this project you agree to abide by its terms. See the `Code 
of Conduct <https://github.com/googleapis/google-cloud-python/blob/main/CODE_OF_CONDUCT.md>`_ for more information.


DML RETURNING Behavior
~~~~~~~~~~~~~~~~~~~~~~

Starting with Django 6.0 compatibility, ``can_return_columns_from_insert = True`` is enabled. Django will generate ``THEN RETURN`` clauses for insert statements that create model instances with database-generated defaults or ``GeneratedField`` columns.

If your application relies on the previous behavior (where returned columns were not queried automatically upon insert), you can disable it in your Django ``AppConfig``:

.. code:: python

    from django.apps import AppConfig

    class MyAppConfig(AppConfig):
        name = "myapp"

        def ready(self):
            from django_spanner.features import DatabaseFeatures

            DatabaseFeatures.can_return_columns_from_insert = False


Limitations
~~~~~~~~~~~

Spanner has certain limitations of its own. The full set of limitations is documented
`here <https://cloud.google.com/spanner/quotas#schema_limits>`__.
It is recommended that you go through that list.

Django spanner has a set of limitations as well, which you can find
`here <https://github.com/googleapis/google-cloud-python/blob/main/docs/limitations.rst>`__.

Features from spanner that are not supported in Django-spanner are listed 
`here <https://github.com/googleapis/google-cloud-python/blob/main/docs/limitations-spanner.rst>`__.
