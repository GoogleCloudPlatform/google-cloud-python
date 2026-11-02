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


Install latest release version via conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ conda install pandas-gbq --channel conda-forge

Install latest release version via pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ pip install pandas-gbq

Install latest development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ pip install git+https://github.com/googleapis/python-bigquery-pandas.git


Usage
-----

Perform a query
~~~~~~~~~~~~~~~

.. code:: python

    import pandas_gbq
    
    result_dataframe = pandas_gbq.read_gbq("SELECT column FROM dataset.table WHERE value = 'something'")

Upload a dataframe
~~~~~~~~~~~~~~~~~~

.. code:: python

    import pandas_gbq
    
    pandas_gbq.to_gbq(dataframe, "dataset.table")

More samples
~~~~~~~~~~~~

See the `pandas-gbq documentation <https://googleapis.dev/python/pandas-gbq/latest/>`_ for more details.
