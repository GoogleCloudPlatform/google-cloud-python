Document AI Toolbox
=================================

|experimental| |versions|

`Document AI Toolbox`_: Document AI Toolbox aims to reduce the friction of managing, manipulating, and extracting information from outputs of Document AI ``BatchProcessDocuments()`` (JSON files written to user-managed GCS buckets) and ``ProcessDocument()`` methods, programmatically.

**Disclaimer**

The Document AI Toolbox is in an experimental state. This library is a work-in-progress and is likely to have backwards-incompatible changes. Users of the toolbox might need to rewrite their code when upgrading the toolbox version.

.. |experimental| image:: https://img.shields.io/badge/support-experimental-red.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-documentai-toolbox.svg
   :target: https://pypi.org/project/google-cloud-documentai-toolbox/


Quick Start
-----------

In order to use this library, you first need to go through the following steps:

Enabling Document AI may not be technically required to use this library, unless ``ProcessDocument()`` is intended to be used.
But you must enable the Storage API to access GCS buckets that contains the output of ``BatchProcessDocument()``. 
You will need to enable the BigQuery API if you intend to use the BigQuery features.

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Storage API.`_
4. `Enable the Document AI API.`_
5. `Enable the BigQuery API.`_
6. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Storage API.:  https://cloud.google.com/storage/docs
.. _Enable the Document AI API.:  https://cloud.google.com/document-ai/docs
.. _Enable the BigQuery API.:  https://cloud.google.com/bigquery/docs
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the `samples/` folder.


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.10

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

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-documentai-toolbox


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-documentai-toolbox

Next Steps
~~~~~~~~~~

-  Read the `Document AI product documentation`_ to learn
   more about the product and see How-to Guides.
-  Read the `Client Library Documentation`_ for Document AI Toolbox
   to see other available methods on the client.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _`Client Library Documentation`: https://cloud.google.com/python/docs/reference/documentai-toolbox/latest
.. _`Document AI documentation`:  https://cloud.google.com/document-ai
.. _`Document AI product documentation`: https://cloud.google.com/document-ai/docs/overview
.. _`README`: https://github.com/googleapis/google-cloud-python/blob/main/README.rst
