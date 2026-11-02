############
Contributing
############

This package is part of the ``google-cloud-python`` monorepo.

Please refer to the centralized `Contributing Guide`_ at the repository root for general guidelines on how to contribute, set up your development environment, and submit pull requests.

.. _Contributing Guide: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst

Package-specific test sessions are defined in this directory's ``noxfile.py``. Dependencies and supported Python versions are defined in ``setup.py`` or ``pyproject.toml``.

*********************
Running system tests
*********************

You can run the system tests with ``nox``::

    $ nox -f system_tests/noxfile.py

To run a single session, specify it with ``nox -s``::

    $ nox -f system_tests/noxfile.py -s service_account

First, set the environment variable ``GOOGLE_APPLICATION_CREDENTIALS`` to a valid service account.
See `Creating and Managing Service Account Keys`_ for how to obtain a service account.

Project and Credentials Setup
-------------------------------

Enable the IAM Service Account Credentials API on the project.

To run system tests locally, you will need to set up a data directory ::

    $ mkdir system_tests/data

Your directory should look like this. Follow the instructions below for creating each file. ::

  system_tests/
      data/
        authorized_user.json
        impersonated_service_account.json
        service_account.json


``authorized_user.json``
~~~~~~~~~~~~~~~~~~~~~~~~

Use the `gcloud CLI`_ to get an authorized user file ::

    $ gcloud auth application-default login --scopes=https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform,openid

You will see something like::

    Credentials saved to file: [/usr/local/home/.config/gcloud/application_default_credentials.json]

Copy the contents of the file to ``authorized_user.json``.

Open the IAM page of the Google Cloud Console. Grant the user the `Service Account Token Creator Role`.
This will allow the user to impersonate service accounts on the project.

.. _gcloud CLI: https://cloud.google.com/sdk/gcloud/


``service_account.json``
~~~~~~~~~~~~~~~~~~~~~~~~

Follow `Creating and Managing Service Account Keys`_ to create a service account.

Copy the credentials file to ``service_account.json``.

Grant the account associated with ``service_account.json`` the following roles.

- App Engine Admin (for App Engine tests)
- Service Account Token Creator (for impersonated credentials and workload identity federation tests)
- Pub/Sub Viewer (for gRPC tests)
- Storage Object Viewer (for impersonated credentials tests)
- DNS Viewer (for workload identity federation tests)
- GCE Storage Bucket Admin (for downscoping tests)

``impersonated_service_account.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow `Creating and Managing Service Account Keys`_ to create a service account.

Copy the credentials file to ``impersonated_service_account.json``.

.. _Creating and Managing Service Account Keys: https://cloud.google.com/iam/docs/creating-managing-service-account-keys

``setup_external_accounts``
~~~~~~~~~~~~~~~~

In order to run the workload identity federation tests, you will need to set up
a Workload Identity Pool, as well as attach relevant policy bindings for this
new resource to our service account. To do this, make sure you have IAM Workload
Identity Pool Admin and Security Admin permissions, and then run:

  $ ./scripts/setup_external_accounts.sh

and then use the output to replace the variables near
the top of system_tests/system_tests_sync/test_external_accounts.py

App Engine System Tests
~~~~~~~~~~~~~~~~~~~~~~~~

To run the App Engine tests, you wil need to deploy a default App Engine service.
If you already have a default service associated with your project, you can skip this step.

Edit ``app.yaml`` so ``service`` is ``default`` instead of ``google-auth-system-tests``.
From ``system_tests/app_engine_test_app`` run the following commands ::

    $ pip install --target lib -r requirements.txt
    $ gcloud app deploy -q app.yaml

After the app is deployed, change ``service`` in ``app.yaml`` back to ``google-auth-system-tests``.
You can now run the App Engine tests: ::

    $ nox -f system_tests/noxfile.py -s app_engine

Compute Engine Tests
^^^^^^^^^^^^^^^^^^^^

These tests cannot be run locally and will be skipped if they are run outside of Google Compute Engine.

grpc Tests
^^^^^^^^^^^^

These tests use the Pub/Sub API. Grant the service account specified by `GOOGLE_APPLICATION_CREDENTIALS`
permissions to list topics. The service account should have at least `roles/pubsub.viewer`.
