Authentication
**************

.. _Overview:

Overview
========

For a language agnostic overview of authentication on Google Cloud, see `Authentication Overview`_.

.. _Authentication Overview: https://cloud.google.com/docs/authentication

*   **If you're running in a Google Virtual Machine Environment (Compute Engine, App Engine, Cloud Run, Cloud Functions)**,
    authentication should "just work".

*   **If you're developing locally**,
    the easiest way to authenticate is using the `Google Cloud SDK`_:

    .. code-block:: bash

        $ gcloud auth application-default login

    Note that this command generates credentials for client libraries. To authenticate the CLI itself, use:

    .. code-block:: bash

        $ gcloud auth login

    Previously, ``gcloud auth login`` was used for both use cases. If
    your ``gcloud`` installation does not support the new command,
    please update it:

    .. code-block:: bash

        $ gcloud components update

.. _Google Cloud SDK: http://cloud.google.com/sdk


*   **If you're running your application elsewhere**,
    you should download a `service account`_ JSON keyfile
    and point to it using an environment variable:

    .. code-block:: bash

        $ export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"

.. _service account: https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating

Client-Provided Authentication
==============================

Every package uses a :class:`Client <google.cloud.client.Client>`
as a base for interacting with an API.
For example:

.. code-block:: python

    from google.cloud import datastore
    client = datastore.Client()

Passing no arguments at all will "just work" if you've followed the
instructions in the :ref:`Overview`.
The credentials are inferred from your local environment by using
Google `Application Default Credentials`_.

.. _Application Default Credentials: https://developers.google.com/identity/protocols/application-default-credentials

.. _Precedence:

Credential Discovery Precedence
-------------------------------

When loading the `Application Default Credentials`_,
the library will check for credentials in your environment by following the
precedence outlined by :func:`google.auth.default`.

Explicit Credentials
====================

The Application Default Credentials discussed above can be useful
if your code needs to run in many different environments or
if you just don't want authentication to be a focus in your code.

However, you may want to be explicit because

* your code will only run in one place
* you may have code which needs to be run as a specific service account
  every time (rather than with the locally inferred credentials)
* you may want to use two separate accounts to simultaneously access data
  from different projects

In these situations, you can create an explicit
:class:`~google.auth.credentials.Credentials` object suited to your environment.
After creation, you can pass it directly to a :class:`Client <google.cloud.client.Client>`:

.. code:: python

    client = Client(credentials=credentials)

.. tip::
    To create a credentials object, follow the `google-auth-guide`_.

.. _google-auth-guide: https://googleapis.dev/python/google-auth/latest/user-guide.html#service-account-private-key-files

Google Compute Engine Environment
---------------------------------

These credentials are used in Google Virtual Machine Environments.
This includes most App Engine runtimes, Compute Engine, Cloud
Functions, and Cloud Run.

To create
:class:`credentials <google.auth.compute_engine.Credentials>`:

.. code:: python

    from google.auth import compute_engine
    credentials = compute_engine.Credentials()

Service Accounts
----------------

A `service account`_ is stored in a JSON keyfile.

.. code:: python

    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_file(
        '/path/to/key.json')

A JSON string or dictionary:

.. code:: python

    import json

    from google.oauth2 import service_account

    json_account_info = json.loads(...)  # convert JSON to dictionary
    credentials = service_account.Credentials.from_service_account_info(
        json_account_info)

.. tip::

    Previously the Google Cloud Console would issue a PKCS12/P12 key for your
    service account. This library does not support that key format. You can
    generate a new JSON key for the same service account from the console.

User Accounts (3-legged OAuth 2.0) with a refresh token
-------------------------------------------------------

The majority of cases are intended to authenticate machines or
workers rather than actual user accounts. However, it's also
possible to call Google Cloud APIs with a user account via
`OAuth 2.0`_.

.. _OAuth 2.0: https://developers.google.com/identity/protocols/OAuth2

.. tip::

    A production application should **use a service account**,
    but you may wish to use your own personal user account when first
    getting started with the ``google-cloud-*`` library.

The simplest way to use credentials from a user account is via
Application Default Credentials using ``gcloud auth application-default login``
(as mentioned above) and :func:`google.auth.default`:

.. code:: python

    import google.auth

    credentials, project = google.auth.default()

This will still follow the :ref:`precedence <Precedence>`
described above,
so be sure none of the other possible environments conflict
with your user provided credentials.

Troubleshooting
===============

Setting up a Service Account
----------------------------

If your application is not running on a Google Virtual Machine Environment,
you need a Service Account. See `Creating a Service Account`_.

.. _Creating a Service Account: https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating

Using Google Compute Engine
---------------------------

If your code is running on Google Compute Engine,
using the inferred Google `Application Default Credentials`_
will be sufficient for retrieving credentials.

However, by default your credentials may not grant you
access to the services you intend to use.
Be sure when you `set up the GCE instance`_,
you add the correct scopes for the APIs you want to access:

* **All APIs**

    * ``https://www.googleapis.com/auth/cloud-platform``
    * ``https://www.googleapis.com/auth/cloud-platform.read-only``

For scopes for specific APIs see `OAuth 2.0 Scopes for Google APIs`_

.. _set up the GCE instance: https://cloud.google.com/compute/docs/authentication#using
.. _OAuth 2.0 Scopes for Google APIS: https://developers.google.com/identity/protocols/oauth2/scopes
