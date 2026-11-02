Privacy
=======

This package is a `PyData project <https://pydata.org/>`_ and is subject to
the `NumFocus privacy policy <https://numfocus.org/privacy-policy>`_. Your
use of Google APIs with this module is subject to each API's respective
`terms of service <https://developers.google.com/terms/>`_.

Google account and user data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accessing user data
~~~~~~~~~~~~~~~~~~~

The :mod:`pandas_gbq` module accesses Google Cloud Platform resources from
your local machine. Your machine communicates directly with the Google APIs.

The :func:`~pandas_gbq.read_gbq` function can read and
write BigQuery data (and other data such as Google Sheets or Cloud Storage,
via the federated query feature) through the BigQuery query interface via
queries you supply.

The :func:`~pandas_gbq.to_gbq` method can write data you supply to a
BigQuery table.

Storing user data
~~~~~~~~~~~~~~~~~

By default, your credentials are stored to a local file, such as
``~/.config/pandas_gbq/bigquery_credentials.dat``. See the
:ref:`authentication-user` guide for details. All user data is stored on
your local machine. **Use caution when using this library on a shared
machine**.

Sharing user data
~~~~~~~~~~~~~~~~~

The pandas-gbq library only communicates with Google APIs. No user
data is shared with PyData, NumFocus, or any other servers.

Policies for application authors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not use the default client ID when using the pandas-gbq library
from an application, library, or tool. Per the `Google User Data Policy
<https://developers.google.com/terms/api-services-user-data-policy>`_, your
application must accurately represent itself when authenticating to Google
API servcies.
