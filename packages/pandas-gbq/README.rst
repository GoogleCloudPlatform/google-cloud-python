pandas-gbq
==========

|preview| |pypi| |versions|

**pandas-gbq** is a package providing an interface to the Google BigQuery API from pandas.

-  `Library Documentation`_
-  `Product Documentation`_

.. |preview| image:: https://img.shields.io/badge/support-preview-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#beta-support
.. |pypi| image:: https://img.shields.io/pypi/v/pandas-gbq.svg
   :target: https://pypi.org/project/pandas-gbq/
.. |versions| image:: https://img.shields.io/pypi/pyversions/pandas-gbq.svg
   :target: https://pypi.org/project/pandas-gbq/
.. _Library Documentation: https://googleapis.dev/python/pandas-gbq/latest/
.. _Product Documentation: https://cloud.google.com/bigquery/docs/reference/v2/

Installation
------------

Install latest release version via pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ pip install pandas-gbq

Install latest development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ pip install git+https://github.com/googleapis/google-cloud-python.git


Usage
-----

Perform a query
~~~~~~~~~~~~~~~

.. code:: python

    import pandas_gbq

    # If running in your local environment or Colab, use the code below and specify your GCP project ID
    # result_dataframe = pandas_gbq.read_gbq("SELECT * FROM bigquery-public-data.usa_names.usa_1910_2013 LIMIT 10", project_id="your-project-id")

    result_dataframe = pandas_gbq.read_gbq("SELECT column FROM dataset.table WHERE value = 'something'")

.. note::

    A Google Cloud project ID can be quickly obtained as described `here <https://docs.cloud.google.com/bigquery/docs/sandbox>`_.

Upload a dataframe
~~~~~~~~~~~~~~~~~~

.. code:: python

    import pandas_gbq

    pandas_gbq.to_gbq(dataframe, "dataset.table")

More samples
~~~~~~~~~~~~

See the `pandas-gbq documentation <https://googleapis.dev/python/pandas-gbq/latest/>`_ for more details.
