.. pandas-gbq documentation master file, created by
   sphinx-quickstart on Wed Feb  8 10:52:12 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pandas-gbq's documentation!
======================================

The :mod:`pandas_gbq` module provides a wrapper for Google's BigQuery
analytics web service to simplify retrieving results from BigQuery tables
using SQL-like queries. Result sets are parsed into a :class:`pandas.DataFrame`
with a shape and data types derived from the source table. Additionally,
DataFrames can be inserted into new BigQuery tables or appended to existing
tables.

.. note::

   To use this module, you will need a valid BigQuery account. Use the
   `BigQuery sandbox <https://cloud.google.com/bigquery/docs/sandbox>`__ to
   try the service for free.

While BigQuery uses standard SQL syntax, it has some important differences
from traditional databases both in functionality, API limitations (size and
quantity of queries or uploads), and how Google charges for use of the
service. BiqQuery is best for analyzing large sets of data quickly. It is not
a direct replacement for a transactional database. Refer to the `BigQuery
Documentation <https://cloud.google.com/bigquery/what-is-bigquery>`__ for
details on the service itself.

Contents:

.. toctree::
   :maxdepth: 2

   install.rst
   intro.rst
   howto/authentication.rst
   reading.rst
   writing.rst
   api.rst
   contributing.rst
   changelog.md
   privacy.rst
   oauth.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. Use the meta tags to verify the site for use in Google OAuth2 consent flow.

.. meta::
    :google-site-verification: 9QSsa9ahOZHbdwZAwl7x-Daaj1W9AttkUOeDgzKtxBw
