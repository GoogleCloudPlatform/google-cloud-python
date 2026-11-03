Google Cloud Python Client
==========================

Python idiomatic clients for `Google Cloud Platform`_ services.

.. _Google Cloud Platform: https://cloud.google.com/


Stability levels
*******************

The `development status classifier`_ on PyPI indicates the current stability
of a package.

.. _development status classifier: https://pypi.org/classifiers/

Stable
------

**Stable** (general availability) indicates that the client library for a
particular service is GA, and that the code surface will not change in
backwards-incompatible ways unless either absolutely necessary (e.g. because
of critical security issues) or with an extensive deprecation period.
Issues and requests against stable libraries are addressed with the highest
priority.

Stable libraries have development status classifier ``Development Status :: 5 - Production/Stable``.

.. note::

    Sub-components of stable libraries explicitly marked as beta in the
    import path (e.g. ``google.cloud.language_v1beta2``) should be considered
    to be preview.

Preview
-------

**Preview** indicates that the client library for a particular service is
under development—either in **Beta** or **Alpha**—and is being prepared for
release.

* **Beta** indicates the library is mostly stable. Issues and requests
  against beta libraries are addressed with a higher priority.
  (``Development Status :: 4 - Beta``)
* **Alpha** indicates the library is still a work-in-progress and is more
  likely to get backwards-incompatible updates. (``Development Status :: 3 - Alpha``)

If you need support for other Google APIs, check out the
`Google APIs Python Client library`_.

.. _Google APIs Python Client library: https://github.com/google/google-api-python-client


Libraries
*********

.. This table is generated, see synth.py for details.

.. API_TABLE_START

.. list-table::
   :header-rows: 1

   * - Client
     - Release Level
     - Version
     - API Issues
     - File an API Issue
     - Client Library Issues
   * - `A python wrapper of the C library 'CRC32C' <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-crc32c>`_
     - stable
     - |PyPI-google-crc32c|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `A unified Python API in BigQuery <https://github.com/google/bigframes>`_
     - stable
     - |PyPI-bigframes|
     -
     -
     - `Client Library Issues <https://github.com/google/bigframes/issues>`_
   * - `AI Platform <https://github.com/googleapis/python-aiplatform>`_
     - stable
     - |PyPI-google-cloud-aiplatform|
     - `API Issues <https://issuetracker.google.com/savedsearches/559744>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187220>`_
     - `Client Library Issues <https://github.com/googleapis/python-aiplatform/issues>`_
   * - `AI Platform Notebooks <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-notebooks>`_
     - stable
     - |PyPI-google-cloud-notebooks|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1392625>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1392625>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API Client Generator for Python <https://github.com/googleapis/google-cloud-python/tree/main/packages/gapic-generator>`_
     - stable
     - |PyPI-gapic-generator|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API Gateway <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-api-gateway>`_
     - stable
     - |PyPI-google-cloud-api-gateway|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API client core library <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-api-core>`_
     - stable
     - |PyPI-google-api-core|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API client core library <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-core>`_
     - stable
     - |PyPI-google-cloud-core|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `APIs Common Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos>`_
     - stable
     - |PyPI-googleapis-common-protos|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Access Approval <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-access-approval>`_
     - stable
     - |PyPI-google-cloud-access-approval|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Apigee Connect <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-apigee-connect>`_
     - stable
     - |PyPI-google-cloud-apigee-connect|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `App Engine Admin <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-appengine-admin>`_
     - stable
     - |PyPI-google-cloud-appengine-admin|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `App Engine Logging Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-appengine-logging>`_
     - stable
     - |PyPI-google-cloud-appengine-logging|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Artifact Registry <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-artifact-registry>`_
     - stable
     - |PyPI-google-cloud-artifact-registry|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Asset Inventory <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-asset>`_
     - stable
     - |PyPI-google-cloud-asset|
     - `API Issues <https://issuetracker.google.com/savedsearches/559757>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187210>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Assured Workloads for Government <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-assured-workloads>`_
     - stable
     - |PyPI-google-cloud-assured-workloads|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Auth OAuthlib <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth-oauthlib>`_
     - stable
     - |PyPI-google-auth-oauthlib|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Auth Python Library <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth>`_
     - stable
     - |PyPI-google-auth|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `AutoML <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-automl>`_
     - stable
     - |PyPI-google-cloud-automl|
     - `API Issues <https://issuetracker.google.com/savedsearches/559744>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187220>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Bare Metal Solution <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bare-metal-solution>`_
     - stable
     - |PyPI-google-cloud-bare-metal-solution|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery>`_
     - stable
     - |PyPI-google-cloud-bigquery|
     - `API Issues <https://issuetracker.google.com/savedsearches/559654>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Connection <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-connection>`_
     - stable
     - |PyPI-google-cloud-bigquery-connection|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Data Transfer <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-datatransfer>`_
     - stable
     - |PyPI-google-cloud-bigquery-datatransfer|
     - `API Issues <https://issuetracker.google.com/savedsearches/559654>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Logging Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-logging>`_
     - stable
     - |PyPI-google-cloud-bigquery-logging|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Reservation <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-reservation>`_
     - stable
     - |PyPI-google-cloud-bigquery-reservation|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Storage <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-storage>`_
     - stable
     - |PyPI-google-cloud-bigquery-storage|
     - `API Issues <https://issuetracker.google.com/savedsearches/559654>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Bigtable <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigtable>`_
     - stable
     - |PyPI-google-cloud-bigtable|
     - `API Issues <https://issuetracker.google.com/savedsearches/559777>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187206>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Billing <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-billing>`_
     - stable
     - |PyPI-google-cloud-billing|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Billing Budget <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-billing-budgets>`_
     - stable
     - |PyPI-google-cloud-billing-budgets|
     - `API Issues <https://issuetracker.google.com/savedsearches/559770>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187201>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Binary Authorization <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-binary-authorization>`_
     - stable
     - |PyPI-google-cloud-binary-authorization|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Build <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-build>`_
     - stable
     - |PyPI-google-cloud-build|
     - `API Issues <https://issuetracker.google.com/savedsearches/5226584>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190802>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Certificate Manager <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-certificate-manager>`_
     - stable
     - |PyPI-google-cloud-certificate-manager|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Channel Services <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-channel>`_
     - stable
     - |PyPI-google-cloud-channel|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Common <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-common>`_
     - stable
     - |PyPI-google-cloud-common|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Composer <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-orchestration-airflow>`_
     - stable
     - |PyPI-google-cloud-orchestration-airflow|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Compute Engine <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-compute>`_
     - stable
     - |PyPI-google-cloud-compute|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187134>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187134&template=0>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Contact Center AI Insights <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-contact-center-insights>`_
     - stable
     - |PyPI-google-cloud-contact-center-insights|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Container Analysis <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-containeranalysis>`_
     - stable
     - |PyPI-google-cloud-containeranalysis|
     - `API Issues <https://issuetracker.google.com/savedsearches/559777>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187206>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Catalog <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-datacatalog>`_
     - stable
     - |PyPI-google-cloud-datacatalog|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:655468>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=655468&template=1284353>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Fusion <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-data-fusion>`_
     - stable
     - |PyPI-google-cloud-data-fusion|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Loss Prevention <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dlp>`_
     - stable
     - |PyPI-google-cloud-dlp|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Database Migration Service <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dms>`_
     - stable
     - |PyPI-google-cloud-dms|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dataplex <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dataplex>`_
     - stable
     - |PyPI-google-cloud-dataplex|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1155079>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1155079&template=1656695>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dataproc <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dataproc>`_
     - stable
     - |PyPI-google-cloud-dataproc|
     - `API Issues <https://issuetracker.google.com/savedsearches/559745>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187133>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dataproc Metastore <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dataproc-metastore>`_
     - stable
     - |PyPI-google-cloud-dataproc-metastore|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Datastore API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-datastore>`_
     - stable
     - |PyPI-google-cloud-datastore|
     - `API Issues <https://issuetracker.google.com/savedsearches/559768>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187197>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Datastream <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-datastream>`_
     - stable
     - |PyPI-google-cloud-datastream|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Deploy <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-deploy>`_
     - stable
     - |PyPI-google-cloud-deploy|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dialogflow <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dialogflow>`_
     - stable
     - |PyPI-google-cloud-dialogflow|
     - `API Issues <https://issuetracker.google.com/savedsearches/5300385>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=501190>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dialogflow CX <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dialogflow-cx>`_
     - stable
     - |PyPI-google-cloud-dialogflow-cx|
     - `API Issues <https://issuetracker.google.com/savedsearches/5300385>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=501190>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Document AI <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-documentai>`_
     - stable
     - |PyPI-google-cloud-documentai|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1132231>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1132231&template=1639002>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Domains <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-domains>`_
     - stable
     - |PyPI-google-cloud-domains|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Essential Contacts <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-essential-contacts>`_
     - stable
     - |PyPI-google-cloud-essential-contacts|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Eventarc <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-eventarc>`_
     - stable
     - |PyPI-google-cloud-eventarc|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Filestore <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-filestore>`_
     - stable
     - |PyPI-google-cloud-filestore|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Firestore API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-firestore>`_
     - stable
     - |PyPI-google-cloud-firestore|
     - `API Issues <https://issuetracker.google.com/savedsearches/5337669>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=530136>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Functions <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-functions>`_
     - stable
     - |PyPI-google-cloud-functions|
     - `API Issues <https://issuetracker.google.com/savedsearches/559729>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187195>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `GKE Hub <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gke-hub>`_
     - stable
     - |PyPI-google-cloud-gke-hub|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Grafeas <https://github.com/googleapis/google-cloud-python/tree/main/packages/grafeas>`_
     - stable
     - |PyPI-grafeas|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `IAM Logging Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-iam-logging>`_
     - stable
     - |PyPI-google-cloud-iam-logging|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `IAM Policy Troubleshooter API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-policy-troubleshooter>`_
     - stable
     - |PyPI-google-cloud-policy-troubleshooter|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:690790>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=690790&template=1814512>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `IDS <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-ids>`_
     - stable
     - |PyPI-google-cloud-ids|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Identity and Access Management <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-iam>`_
     - stable
     - |PyPI-google-cloud-iam|
     - `API Issues <https://issuetracker.google.com/savedsearches/559761>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187161>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Identity-Aware Proxy <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-iap>`_
     - stable
     - |PyPI-google-cloud-iap|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Key Management Service <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-kms>`_
     - stable
     - |PyPI-google-cloud-kms|
     - `API Issues <https://issuetracker.google.com/savedsearches/5264932>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190860>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Kubernetes Engine <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-container>`_
     - stable
     - |PyPI-google-cloud-container|
     - `API Issues <https://issuetracker.google.com/savedsearches/559746>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187077>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Live Stream <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-video-live-stream>`_
     - stable
     - |PyPI-google-cloud-video-live-stream|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Logging API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-logging>`_
     - stable
     - |PyPI-google-cloud-logging|
     - `API Issues <https://issuetracker.google.com/savedsearches/559764>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187203>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Managed Service for Microsoft Active Directory <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-managed-identities>`_
     - stable
     - |PyPI-google-cloud-managed-identities|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Memorystore for Memcached <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-memcache>`_
     - stable
     - |PyPI-google-cloud-memcache|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-accounts>`_
     - stable
     - |PyPI-google-shopping-merchant-accounts|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-conversions>`_
     - stable
     - |PyPI-google-shopping-merchant-conversions|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-datasources>`_
     - stable
     - |PyPI-google-shopping-merchant-datasources|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-issueresolution>`_
     - stable
     - |PyPI-google-shopping-merchant-issueresolution|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:171084>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=171084&template=555201>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-lfp>`_
     - stable
     - |PyPI-google-shopping-merchant-lfp|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-notifications>`_
     - stable
     - |PyPI-google-shopping-merchant-notifications|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-ordertracking>`_
     - stable
     - |PyPI-google-shopping-merchant-ordertracking|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:171084>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=171084&template=555201>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-products>`_
     - stable
     - |PyPI-google-shopping-merchant-products|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-promotions>`_
     - stable
     - |PyPI-google-shopping-merchant-promotions|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant Inventories API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-inventories>`_
     - stable
     - |PyPI-google-shopping-merchant-inventories|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:171084>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=171084&template=555201>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant Reports API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-reports>`_
     - stable
     - |PyPI-google-shopping-merchant-reports|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:171084>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=171084&template=555201>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Metrics Scopes <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-monitoring-metrics-scopes>`_
     - stable
     - |PyPI-google-cloud-monitoring-metrics-scopes|
     - `API Issues <https://issuetracker.google.com/savedsearches/559785>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187228>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Monitoring Dashboards <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-monitoring-dashboards>`_
     - stable
     - |PyPI-google-cloud-monitoring-dashboards|
     - `API Issues <https://issuetracker.google.com/savedsearches/559785>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187228>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `NDB Client Library for Datastore <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-ndb>`_
     - stable
     - |PyPI-google-cloud-ndb|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Natural Language <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-language>`_
     - stable
     - |PyPI-google-cloud-language|
     - `API Issues <https://issuetracker.google.com/savedsearches/559753>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187079>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Network Connectivity Center <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-network-connectivity>`_
     - stable
     - |PyPI-google-cloud-network-connectivity|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Network Management <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-network-management>`_
     - stable
     - |PyPI-google-cloud-network-management|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `OS Config <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-os-config>`_
     - stable
     - |PyPI-google-cloud-os-config|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `OS Login <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-os-login>`_
     - stable
     - |PyPI-google-cloud-os-login|
     - `API Issues <https://issuetracker.google.com/savedsearches/559755>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187134>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Optimization <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-optimization>`_
     - stable
     - |PyPI-google-cloud-optimization|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Organization Policy <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-org-policy>`_
     - stable
     - |PyPI-google-cloud-org-policy|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Pandas Data Types for SQL systems (BigQuery, Spanner) <https://github.com/googleapis/google-cloud-python/tree/main/packages/db-dtypes>`_
     - stable
     - |PyPI-db-dtypes|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Private Certificate Authority <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-private-ca>`_
     - stable
     - |PyPI-google-cloud-private-ca|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Proto Plus <https://github.com/googleapis/google-cloud-python/tree/main/packages/proto-plus>`_
     - stable
     - |PyPI-proto-plus|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Pub/Sub <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-pubsub>`_
     - stable
     - |PyPI-google-cloud-pubsub|
     - `API Issues <https://issuetracker.google.com/savedsearches/559741>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187173>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Pub/Sub Lite <https://github.com/googleapis/python-pubsublite>`_
     - stable
     - |PyPI-google-cloud-pubsublite|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/python-pubsublite/issues>`_
   * - `Python Test Utils for Cloud <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-testutils>`_
     - stable
     - |PyPI-google-cloud-testutils|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Recommender <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-recommender>`_
     - stable
     - |PyPI-google-cloud-recommender|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Redis <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-redis>`_
     - stable
     - |PyPI-google-cloud-redis|
     - `API Issues <https://issuetracker.google.com/savedsearches/5169231>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=404472>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Resource Manager <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-resource-manager>`_
     - stable
     - |PyPI-google-cloud-resource-manager|
     - `API Issues <https://issuetracker.google.com/savedsearches/559757>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187210>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Resumable Media <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-resumable-media>`_
     - stable
     - |PyPI-google-resumable-media|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Retail <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-retail>`_
     - stable
     - |PyPI-google-cloud-retail|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `SQLAlchemy dialect for BigQuery <https://github.com/googleapis/google-cloud-python/tree/main/packages/sqlalchemy-bigquery>`_
     - stable
     - |PyPI-sqlalchemy-bigquery|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Scheduler <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-scheduler>`_
     - stable
     - |PyPI-google-cloud-scheduler|
     - `API Issues <https://issuetracker.google.com/savedsearches/5411429>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=589898>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Secret Manager <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-secret-manager>`_
     - stable
     - |PyPI-google-cloud-secret-manager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:784854>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=784854&template=1380926>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Security Command Center <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-securitycenter>`_
     - stable
     - |PyPI-google-cloud-securitycenter|
     - `API Issues <https://issuetracker.google.com/savedsearches/559748>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187215>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Security Scanner <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-websecurityscanner>`_
     - stable
     - |PyPI-google-cloud-websecurityscanner|
     - `API Issues <https://issuetracker.google.com/savedsearches/559748>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187215>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Service Control <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-service-control>`_
     - stable
     - |PyPI-google-cloud-service-control|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Service Directory <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-service-directory>`_
     - stable
     - |PyPI-google-cloud-service-directory|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Service Management <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-service-management>`_
     - stable
     - |PyPI-google-cloud-service-management|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Service Usage <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-service-usage>`_
     - stable
     - |PyPI-google-cloud-service-usage|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Shell <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-shell>`_
     - stable
     - |PyPI-google-cloud-shell|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Shopping Merchant Quota <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-quota>`_
     - stable
     - |PyPI-google-shopping-merchant-quota|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:171084>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=171084&template=555201>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Shopping Type Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-type>`_
     - stable
     - |PyPI-google-shopping-type|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Source Context <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-source-context>`_
     - stable
     - |PyPI-google-cloud-source-context|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Spanner <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-spanner>`_
     - stable
     - |PyPI-google-cloud-spanner|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190851>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190851>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Spanner Django <https://github.com/googleapis/google-cloud-python/tree/main/packages/django-google-spanner>`_
     - stable
     - |PyPI-django-google-spanner|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190851>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190851>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Spanner dialect for SQLAlchemy <https://github.com/googleapis/google-cloud-python/tree/main/packages/sqlalchemy-spanner>`_
     - stable
     - |PyPI-sqlalchemy-spanner|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190851>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190851>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Speech <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-speech>`_
     - stable
     - |PyPI-google-cloud-speech|
     - `API Issues <https://issuetracker.google.com/savedsearches/559758>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187181>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Sphinx DocFX YAML Generator <https://github.com/googleapis/google-cloud-python/tree/main/packages/gcp-sphinx-docfx-yaml>`_
     - stable
     - |PyPI-gcp-sphinx-docfx-yaml|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Stackdriver Monitoring <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-monitoring>`_
     - stable
     - |PyPI-google-cloud-monitoring|
     - `API Issues <https://issuetracker.google.com/savedsearches/559785>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187228>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Storage <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage>`_
     - stable
     - |PyPI-google-cloud-storage|
     - `API Issues <https://issuetracker.google.com/savedsearches/559782>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187243>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Storage Control API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage-control>`_
     - stable
     - |PyPI-google-cloud-storage-control|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187243>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187243&template=1162869>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Storage Transfer Service <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage-transfer>`_
     - stable
     - |PyPI-google-cloud-storage-transfer|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `TPU <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-tpu>`_
     - stable
     - |PyPI-google-cloud-tpu|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Talent Solution <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-talent>`_
     - stable
     - |PyPI-google-cloud-talent|
     - `API Issues <https://issuetracker.google.com/savedsearches/559664>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187187>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Tasks <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-tasks>`_
     - stable
     - |PyPI-google-cloud-tasks|
     - `API Issues <https://issuetracker.google.com/savedsearches/5433985>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=608118>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Text-to-Speech <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-texttospeech>`_
     - stable
     - |PyPI-google-cloud-texttospeech|
     - `API Issues <https://issuetracker.google.com/savedsearches/5235428>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=451645>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Trace <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-trace>`_
     - stable
     - |PyPI-google-cloud-trace|
     - `API Issues <https://issuetracker.google.com/savedsearches/559776>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187216>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Transcoder <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-video-transcoder>`_
     - stable
     - |PyPI-google-cloud-video-transcoder|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Translation <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-translate>`_
     - stable
     - |PyPI-google-cloud-translate|
     - `API Issues <https://issuetracker.google.com/savedsearches/559749>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187144>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `VM Migration <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-vm-migration>`_
     - stable
     - |PyPI-google-cloud-vm-migration|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Video Intelligence <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-videointelligence>`_
     - stable
     - |PyPI-google-cloud-videointelligence|
     - `API Issues <https://issuetracker.google.com/savedsearches/5084810>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190865>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Virtual Private Cloud <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-vpc-access>`_
     - stable
     - |PyPI-google-cloud-vpc-access|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Vision <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-vision>`_
     - stable
     - |PyPI-google-cloud-vision|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Web Risk <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-webrisk>`_
     - stable
     - |PyPI-google-cloud-webrisk|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Workflows <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-workflows>`_
     - stable
     - |PyPI-google-cloud-workflows|
     - `API Issues <https://issuetracker.google.com/savedsearches/559729>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187195>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `reCAPTCHA Enterprise <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-recaptcha-enterprise>`_
     - stable
     - |PyPI-google-cloud-recaptcha-enterprise|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API Hub API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-apihub>`_
     - preview
     - |PyPI-google-cloud-apihub|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1447560>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1447560>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API Keys <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-api-keys>`_
     - preview
     - |PyPI-google-cloud-api-keys|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `API Registry API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-apiregistry>`_
     - preview
     - |PyPI-google-cloud-apiregistry|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1979613>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1979613&template=2231768>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Access Context Manager <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-access-context-manager>`_
     - preview
     - |PyPI-google-cloud-access-context-manager|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Ad Manager <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ads-admanager>`_
     - preview
     - |PyPI-google-ads-admanager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1265187>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1265187&template=1787490>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Address Validation API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-addressvalidation>`_
     - preview
     - |PyPI-google-maps-addressvalidation|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Advisory Notifications <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-advisorynotifications>`_
     - preview
     - |PyPI-google-cloud-advisorynotifications|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `AlloyDB <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-alloydb>`_
     - preview
     - |PyPI-google-cloud-alloydb|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `AlloyDB connectors <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-alloydb-connectors>`_
     - preview
     - |PyPI-google-cloud-alloydb-connectors|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1194526>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1194526&template=1689942>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Analytics Admin <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-analytics-admin>`_
     - preview
     - |PyPI-google-analytics-admin|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187400>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187400>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Analytics Data <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-analytics-data>`_
     - preview
     - |PyPI-google-analytics-data|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187400>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187400>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Anthos Multicloud <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gke-multicloud>`_
     - preview
     - |PyPI-google-cloud-gke-multicloud|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:997904>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=997904&template=1807166>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Anti Money Laundering AI API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-financialservices>`_
     - preview
     - |PyPI-google-cloud-financialservices|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `App Hub API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-apphub>`_
     - preview
     - |PyPI-google-cloud-apphub|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1509913>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1509913>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `App Optimize API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-appoptimize>`_
     - preview
     - |PyPI-google-cloud-appoptimize|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190865>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190865&template=1161103>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Apps Card Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-apps-card>`_
     - preview
     - |PyPI-google-apps-card|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Apps Script Type Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-apps-script-type>`_
     - preview
     - |PyPI-google-apps-script-type|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Audit Log API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-audit-log>`_
     - preview
     - |PyPI-google-cloud-audit-log|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Audit Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-auditmanager>`_
     - preview
     - |PyPI-google-cloud-auditmanager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1335397>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1335397&template=0>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Auth httplib2 <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth-httplib2>`_
     - preview
     - |PyPI-google-auth-httplib2|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Backup and DR Service API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-backupdr>`_
     - preview
     - |PyPI-google-cloud-backupdr|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:966572>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=966572>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Backup for GKE <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gke-backup>`_
     - preview
     - |PyPI-google-cloud-gke-backup|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1126471>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1126471>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Batch <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-batch>`_
     - preview
     - |PyPI-google-cloud-batch|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BeyondCorp AppConnections <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-beyondcorp-appconnections>`_
     - preview
     - |PyPI-google-cloud-beyondcorp-appconnections|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BeyondCorp AppConnectors <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-beyondcorp-appconnectors>`_
     - preview
     - |PyPI-google-cloud-beyondcorp-appconnectors|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BeyondCorp AppGateways <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-beyondcorp-appgateways>`_
     - preview
     - |PyPI-google-cloud-beyondcorp-appgateways|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BeyondCorp ClientConnectorServices <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-beyondcorp-clientconnectorservices>`_
     - preview
     - |PyPI-google-cloud-beyondcorp-clientconnectorservices|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BeyondCorp ClientGateways <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-beyondcorp-clientgateways>`_
     - preview
     - |PyPI-google-cloud-beyondcorp-clientgateways|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigLake API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-biglake-hive>`_
     - preview
     - |PyPI-google-cloud-biglake-hive|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187149>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149&template=1019829>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigLake API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-biglake>`_
     - preview
     - |PyPI-google-cloud-biglake|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigLake API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-biglake>`_
     - preview
     - |PyPI-google-cloud-bigquery-biglake|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187149>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149&template=1019829>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Analytics Hub <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-analyticshub>`_
     - preview
     - |PyPI-google-cloud-bigquery-analyticshub|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Analytics Hub <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-data-exchange>`_
     - preview
     - |PyPI-google-cloud-bigquery-data-exchange|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Data Policy <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-datapolicies>`_
     - preview
     - |PyPI-google-cloud-bigquery-datapolicies|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187149>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149&template=1162659>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery Migration <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery-migration>`_
     - preview
     - |PyPI-google-cloud-bigquery-migration|
     - `API Issues <https://issuetracker.google.com/savedsearches/559654>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187149>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery connector for Jupyter and IPython <https://github.com/googleapis/google-cloud-python/tree/main/packages/bigquery-magics>`_
     - preview
     - |PyPI-bigquery-magics|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `BigQuery connector for pandas <https://github.com/googleapis/google-cloud-python/tree/main/packages/pandas-gbq>`_
     - preview
     - |PyPI-pandas-gbq|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `CSS API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-css>`_
     - preview
     - |PyPI-google-shopping-css|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:826068>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=826068&template=1564577>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Capacity Planner API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-capacityplanner>`_
     - preview
     - |PyPI-google-cloud-capacityplanner|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1194830>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1194830>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Chat API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-apps-chat>`_
     - preview
     - |PyPI-google-apps-chat|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Chronicle API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-chronicle>`_
     - preview
     - |PyPI-google-cloud-chronicle|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1387895>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1387895>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Cluster Director API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-hypercomputecluster>`_
     - preview
     - |PyPI-google-cloud-hypercomputecluster|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1907878>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1907878&template=2195617>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Commerce Consumer Procurement API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-commerce-consumer-procurement>`_
     - preview
     - |PyPI-google-cloud-commerce-consumer-procurement|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1396141>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1396141>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Compute Engine <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-compute-v1beta>`_
     - preview
     - |PyPI-google-cloud-compute-v1beta|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187134>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187134&template=0>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Confidential Computing API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-confidentialcomputing>`_
     - preview
     - |PyPI-google-cloud-confidentialcomputing|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1166820>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1166820>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Config Delivery API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-configdelivery>`_
     - preview
     - |PyPI-google-cloud-configdelivery|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Controls Partner API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-cloudcontrolspartner>`_
     - preview
     - |PyPI-google-cloud-cloudcontrolspartner|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `DNS <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dns>`_
     - preview
     - |PyPI-google-cloud-dns|
     - `API Issues <https://issuetracker.google.com/savedsearches/559772>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187241>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Analytics API with Gemini <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-geminidataanalytics>`_
     - preview
     - |PyPI-google-cloud-geminidataanalytics|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Labeling <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-datalabeling>`_
     - preview
     - |PyPI-google-cloud-datalabeling|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Lineage API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-datacatalog-lineage-configmanagement>`_
     - preview
     - |PyPI-google-cloud-datacatalog-lineage-configmanagement|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1530027>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1530027>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Lineage API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-datacatalog-lineage>`_
     - preview
     - |PyPI-google-cloud-datacatalog-lineage|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ads-datamanager>`_
     - preview
     - |PyPI-google-ads-datamanager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1812065>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1812065>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Data QnA <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-data-qna>`_
     - preview
     - |PyPI-google-cloud-data-qna|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Database Center API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-databasecenter>`_
     - preview
     - |PyPI-google-cloud-databasecenter|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1476470>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1476470>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dataflow <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dataflow-client>`_
     - preview
     - |PyPI-google-cloud-dataflow-client|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Dataform <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dataform>`_
     - preview
     - |PyPI-google-cloud-dataform|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:994183>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=994183>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Developer Connect API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-developerconnect>`_
     - preview
     - |PyPI-google-cloud-developerconnect|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1446966>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1446966&template=1822025>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Device Streaming API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-devicestreaming>`_
     - preview
     - |PyPI-google-cloud-devicestreaming|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1767292>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1767292&template=2112325>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Discovery Engine API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-discoveryengine>`_
     - preview
     - |PyPI-google-cloud-discoveryengine|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Distributed Edge Container <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-edgecontainer>`_
     - preview
     - |PyPI-google-cloud-edgecontainer|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Distributed Edge Network API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-edgenetwork>`_
     - preview
     - |PyPI-google-cloud-edgenetwork|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187192>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187192&template=1162689>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Document AI Toolbox <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-documentai-toolbox>`_
     - preview
     - |PyPI-google-cloud-documentai-toolbox|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Document AI Warehouse <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-contentwarehouse>`_
     - preview
     - |PyPI-google-cloud-contentwarehouse|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Enterprise Knowledge Graph <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-enterpriseknowledgegraph>`_
     - preview
     - |PyPI-google-cloud-enterpriseknowledgegraph|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Error Reporting API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-error-reporting>`_
     - preview
     - |PyPI-google-cloud-error-reporting|
     - `API Issues <https://issuetracker.google.com/savedsearches/559780>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187271>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Eventarc Publishing <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-eventarc-publishing>`_
     - preview
     - |PyPI-google-cloud-eventarc-publishing|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `GDC Hardware Management API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gdchardwaremanagement>`_
     - preview
     - |PyPI-google-cloud-gdchardwaremanagement|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1563150>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1563150>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `GKE Connect Gateway <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gke-connect-gateway>`_
     - preview
     - |PyPI-google-cloud-gke-connect-gateway|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1618911>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1618911>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `GKE Recommender API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gkerecommender>`_
     - preview
     - |PyPI-google-cloud-gkerecommender|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1790908>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1790908>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Gemini Enterprise for Customer Experience API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-ces>`_
     - preview
     - |PyPI-google-cloud-ces|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1157150>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1157150>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Generative Language API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage>`_
     - preview
     - |PyPI-google-ai-generativelanguage|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Geo Type Protos <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-geo-type>`_
     - preview
     - |PyPI-google-geo-type|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Geocoding API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-geocode>`_
     - preview
     - |PyPI-google-maps-geocode|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:188871>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=188871&template=788907>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Identity and Access Management <https://github.com/googleapis/google-cloud-python/tree/main/packages/grpc-google-iam-v1>`_
     - preview
     - |PyPI-grpc-google-iam-v1|
     - `API Issues <https://issuetracker.google.com/savedsearches/559761>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187161>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Infrastructure Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-config>`_
     - preview
     - |PyPI-google-cloud-config|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:536700>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=536700>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `KMS Inventory API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-kms-inventory>`_
     - preview
     - |PyPI-google-cloud-kms-inventory|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190860>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190860&template=819701>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Last Mile Fleet Solution Delivery API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-fleetengine-delivery>`_
     - preview
     - |PyPI-google-maps-fleetengine-delivery|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `License Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-licensemanager>`_
     - preview
     - |PyPI-google-cloud-licensemanager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1659587>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1659587>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Life Sciences <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-life-sciences>`_
     - preview
     - |PyPI-google-cloud-life-sciences|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Local Rides and Deliveries API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-fleetengine>`_
     - preview
     - |PyPI-google-maps-fleetengine|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Location Finder API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-locationfinder>`_
     - preview
     - |PyPI-google-cloud-locationfinder|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1569265>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1569265&template=1988535>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Maintenance API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-maintenance-api>`_
     - preview
     - |PyPI-google-cloud-maintenance-api|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1673988>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1673988&template=1161103>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Managed Lustre API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-lustre>`_
     - preview
     - |PyPI-google-cloud-lustre|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1625664>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1625664>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Managed Service for Apache Kafka <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-managedkafka>`_
     - preview
     - |PyPI-google-cloud-managedkafka|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1376234>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1376234>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Managed Service for Apache Kafka API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-managedkafka-schemaregistry>`_
     - preview
     - |PyPI-google-cloud-managedkafka-schemaregistry|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1376234>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1376234>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Maps Platform Datasets API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-mapsplatformdatasets>`_
     - preview
     - |PyPI-google-maps-mapsplatformdatasets|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Maps Routing <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-routing>`_
     - preview
     - |PyPI-google-maps-routing|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Marketing Platform Admin API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ads-marketingplatform-admin>`_
     - preview
     - |PyPI-google-ads-marketingplatform-admin|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Media Translation <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-media-translation>`_
     - preview
     - |PyPI-google-cloud-media-translation|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Meet API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-apps-meet>`_
     - preview
     - |PyPI-google-apps-meet|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1216362>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1216362&template=1766418>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Memorystore <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-memorystore>`_
     - preview
     - |PyPI-google-cloud-memorystore|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Memorystore for Redis API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-redis-cluster>`_
     - preview
     - |PyPI-google-cloud-redis-cluster|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1288776>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1288776&template=1161103>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant ProductStudio API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-productstudio>`_
     - preview
     - |PyPI-google-shopping-merchant-productstudio|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Merchant Reviews API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-shopping-merchant-reviews>`_
     - preview
     - |PyPI-google-shopping-merchant-reviews|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Migration Center API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-migrationcenter>`_
     - preview
     - |PyPI-google-cloud-migrationcenter|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Model Armor API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-modelarmor>`_
     - preview
     - |PyPI-google-cloud-modelarmor|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1514910>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1514910&template=0>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Navigation Connect API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-navconnect>`_
     - preview
     - |PyPI-google-maps-navconnect|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1180397>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1180397&template=1812135>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `NetApp API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-netapp>`_
     - preview
     - |PyPI-google-cloud-netapp|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1144971>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1144971>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Network Security <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-network-security>`_
     - preview
     - |PyPI-google-cloud-network-security|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1132189>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1132189&template=1639113>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Network Services <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-network-services>`_
     - preview
     - |PyPI-google-cloud-network-services|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1132189>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1132189&template=1639113>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Oracle Database@API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-oracledatabase>`_
     - preview
     - |PyPI-google-cloud-oracledatabase|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1492565>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1492565>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Parallelstore API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-parallelstore>`_
     - preview
     - |PyPI-google-cloud-parallelstore|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Parameter Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-parametermanager>`_
     - preview
     - |PyPI-google-cloud-parametermanager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1442085>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1442085&template=2002674>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Phishing Protection <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-phishing-protection>`_
     - preview
     - |PyPI-google-cloud-phishing-protection|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Places API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-places>`_
     - preview
     - |PyPI-google-maps-places|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Places Insights API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-areainsights>`_
     - preview
     - |PyPI-google-maps-areainsights|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1624013>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1624013&template=2026178>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Policy Simulator API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-policysimulator>`_
     - preview
     - |PyPI-google-cloud-policysimulator|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Policy Troubleshooter API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-policytroubleshooter-iam>`_
     - preview
     - |PyPI-google-cloud-policytroubleshooter-iam|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:690790>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=690790&template=1814512>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Private Catalog <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-private-catalog>`_
     - preview
     - |PyPI-google-cloud-private-catalog|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Privileged Access Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-privilegedaccessmanager>`_
     - preview
     - |PyPI-google-cloud-privilegedaccessmanager|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Public Certificate Authority <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-security-publicca>`_
     - preview
     - |PyPI-google-cloud-security-publicca|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Quotas API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-quotas>`_
     - preview
     - |PyPI-google-cloud-quotas|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:445904>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=445904>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Rapid Migration Assessment API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-rapidmigrationassessment>`_
     - preview
     - |PyPI-google-cloud-rapidmigrationassessment|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Recommendations AI <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-recommendations-ai>`_
     - preview
     - |PyPI-google-cloud-recommendations-ai|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Route Optimization API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-routeoptimization>`_
     - preview
     - |PyPI-google-maps-routeoptimization|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1546507>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1546507>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Run <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-run>`_
     - preview
     - |PyPI-google-cloud-run|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Runtime Configurator <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-runtimeconfig>`_
     - preview
     - |PyPI-google-cloud-runtimeconfig|
     - `API Issues <https://issuetracker.google.com/savedsearches/559663>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187078>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `SaaS Runtime API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-saasplatform-saasservicemgmt>`_
     - preview
     - |PyPI-google-cloud-saasplatform-saasservicemgmt|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Secure Source Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-securesourcemanager>`_
     - preview
     - |PyPI-google-cloud-securesourcemanager|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Security Center Management API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-securitycentermanagement>`_
     - preview
     - |PyPI-google-cloud-securitycentermanagement|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Security Compliance API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-cloudsecuritycompliance>`_
     - preview
     - |PyPI-google-cloud-cloudsecuritycompliance|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1761967>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1761967&template=0>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Service Health API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-servicehealth>`_
     - preview
     - |PyPI-google-cloud-servicehealth|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1466723>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1466723&template=1161103>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Solar API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-maps-solar>`_
     - preview
     - |PyPI-google-maps-solar|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1356349>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1356349>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Spanner DBAPI Driver <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-spanner-dbapi-driver>`_
     - preview
     - |PyPI-google-cloud-spanner-dbapi-driver|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Storage Batch Operations API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storagebatchoperations>`_
     - preview
     - |PyPI-google-cloud-storagebatchoperations|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:815827>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=815827&template=1395449>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Storage Insights API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storageinsights>`_
     - preview
     - |PyPI-google-cloud-storageinsights|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1156610>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1156610>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Support API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-support>`_
     - preview
     - |PyPI-google-cloud-support|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Telco Automation API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-telcoautomation>`_
     - preview
     - |PyPI-google-cloud-telcoautomation|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190865>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190865&template=1161103>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `VMware Engine <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-vmwareengine>`_
     - preview
     - |PyPI-google-cloud-vmwareengine|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Vector Search API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-vectorsearch>`_
     - preview
     - |PyPI-google-cloud-vectorsearch|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1899904>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1899904>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Video Stitcher <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-video-stitcher>`_
     - preview
     - |PyPI-google-cloud-video-stitcher|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Vision AI API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-visionai>`_
     - preview
     - |PyPI-google-cloud-visionai|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:187174>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=187174&template=1161261>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Workload Manager API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-workloadmanager>`_
     - preview
     - |PyPI-google-cloud-workloadmanager|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:1631482>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=1631482&template=0>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Workspace Add-ons API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-gsuiteaddons>`_
     - preview
     - |PyPI-google-cloud-gsuiteaddons|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Workspace Events API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-apps-events-subscriptions>`_
     - preview
     - |PyPI-google-apps-events-subscriptions|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `Workstations <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-workstations>`_
     - preview
     - |PyPI-google-cloud-workstations|
     -
     -
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_
   * - `iamconnectorcredentials.googleapis.com API <https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-iamconnectorcredentials>`_
     - preview
     - |PyPI-google-cloud-iamconnectorcredentials|
     - `API Issues <https://issuetracker.google.com/issues?q=componentid:190865>`_
     - `File an API Issue <https://issuetracker.google.com/issues/new?component=190865&template=1161103>`_
     - `Client Library Issues <https://github.com/googleapis/google-cloud-python/issues>`_

.. |PyPI-google-crc32c| image:: https://img.shields.io/pypi/v/google-crc32c.svg
     :target: https://pypi.org/project/google-crc32c
.. |PyPI-bigframes| image:: https://img.shields.io/pypi/v/bigframes.svg
     :target: https://pypi.org/project/bigframes
.. |PyPI-google-cloud-aiplatform| image:: https://img.shields.io/pypi/v/google-cloud-aiplatform.svg
     :target: https://pypi.org/project/google-cloud-aiplatform
.. |PyPI-google-cloud-notebooks| image:: https://img.shields.io/pypi/v/google-cloud-notebooks.svg
     :target: https://pypi.org/project/google-cloud-notebooks
.. |PyPI-gapic-generator| image:: https://img.shields.io/pypi/v/gapic-generator.svg
     :target: https://pypi.org/project/gapic-generator
.. |PyPI-google-cloud-api-gateway| image:: https://img.shields.io/pypi/v/google-cloud-api-gateway.svg
     :target: https://pypi.org/project/google-cloud-api-gateway
.. |PyPI-google-api-core| image:: https://img.shields.io/pypi/v/google-api-core.svg
     :target: https://pypi.org/project/google-api-core
.. |PyPI-google-cloud-core| image:: https://img.shields.io/pypi/v/google-cloud-core.svg
     :target: https://pypi.org/project/google-cloud-core
.. |PyPI-googleapis-common-protos| image:: https://img.shields.io/pypi/v/googleapis-common-protos.svg
     :target: https://pypi.org/project/googleapis-common-protos
.. |PyPI-google-cloud-access-approval| image:: https://img.shields.io/pypi/v/google-cloud-access-approval.svg
     :target: https://pypi.org/project/google-cloud-access-approval
.. |PyPI-google-cloud-apigee-connect| image:: https://img.shields.io/pypi/v/google-cloud-apigee-connect.svg
     :target: https://pypi.org/project/google-cloud-apigee-connect
.. |PyPI-google-cloud-appengine-admin| image:: https://img.shields.io/pypi/v/google-cloud-appengine-admin.svg
     :target: https://pypi.org/project/google-cloud-appengine-admin
.. |PyPI-google-cloud-appengine-logging| image:: https://img.shields.io/pypi/v/google-cloud-appengine-logging.svg
     :target: https://pypi.org/project/google-cloud-appengine-logging
.. |PyPI-google-cloud-artifact-registry| image:: https://img.shields.io/pypi/v/google-cloud-artifact-registry.svg
     :target: https://pypi.org/project/google-cloud-artifact-registry
.. |PyPI-google-cloud-asset| image:: https://img.shields.io/pypi/v/google-cloud-asset.svg
     :target: https://pypi.org/project/google-cloud-asset
.. |PyPI-google-cloud-assured-workloads| image:: https://img.shields.io/pypi/v/google-cloud-assured-workloads.svg
     :target: https://pypi.org/project/google-cloud-assured-workloads
.. |PyPI-google-auth-oauthlib| image:: https://img.shields.io/pypi/v/google-auth-oauthlib.svg
     :target: https://pypi.org/project/google-auth-oauthlib
.. |PyPI-google-auth| image:: https://img.shields.io/pypi/v/google-auth.svg
     :target: https://pypi.org/project/google-auth
.. |PyPI-google-cloud-automl| image:: https://img.shields.io/pypi/v/google-cloud-automl.svg
     :target: https://pypi.org/project/google-cloud-automl
.. |PyPI-google-cloud-bare-metal-solution| image:: https://img.shields.io/pypi/v/google-cloud-bare-metal-solution.svg
     :target: https://pypi.org/project/google-cloud-bare-metal-solution
.. |PyPI-google-cloud-bigquery| image:: https://img.shields.io/pypi/v/google-cloud-bigquery.svg
     :target: https://pypi.org/project/google-cloud-bigquery
.. |PyPI-google-cloud-bigquery-connection| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-connection.svg
     :target: https://pypi.org/project/google-cloud-bigquery-connection
.. |PyPI-google-cloud-bigquery-datatransfer| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-datatransfer.svg
     :target: https://pypi.org/project/google-cloud-bigquery-datatransfer
.. |PyPI-google-cloud-bigquery-logging| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-logging.svg
     :target: https://pypi.org/project/google-cloud-bigquery-logging
.. |PyPI-google-cloud-bigquery-reservation| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-reservation.svg
     :target: https://pypi.org/project/google-cloud-bigquery-reservation
.. |PyPI-google-cloud-bigquery-storage| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-storage.svg
     :target: https://pypi.org/project/google-cloud-bigquery-storage
.. |PyPI-google-cloud-bigtable| image:: https://img.shields.io/pypi/v/google-cloud-bigtable.svg
     :target: https://pypi.org/project/google-cloud-bigtable
.. |PyPI-google-cloud-billing| image:: https://img.shields.io/pypi/v/google-cloud-billing.svg
     :target: https://pypi.org/project/google-cloud-billing
.. |PyPI-google-cloud-billing-budgets| image:: https://img.shields.io/pypi/v/google-cloud-billing-budgets.svg
     :target: https://pypi.org/project/google-cloud-billing-budgets
.. |PyPI-google-cloud-binary-authorization| image:: https://img.shields.io/pypi/v/google-cloud-binary-authorization.svg
     :target: https://pypi.org/project/google-cloud-binary-authorization
.. |PyPI-google-cloud-build| image:: https://img.shields.io/pypi/v/google-cloud-build.svg
     :target: https://pypi.org/project/google-cloud-build
.. |PyPI-google-cloud-certificate-manager| image:: https://img.shields.io/pypi/v/google-cloud-certificate-manager.svg
     :target: https://pypi.org/project/google-cloud-certificate-manager
.. |PyPI-google-cloud-channel| image:: https://img.shields.io/pypi/v/google-cloud-channel.svg
     :target: https://pypi.org/project/google-cloud-channel
.. |PyPI-google-cloud-common| image:: https://img.shields.io/pypi/v/google-cloud-common.svg
     :target: https://pypi.org/project/google-cloud-common
.. |PyPI-google-cloud-orchestration-airflow| image:: https://img.shields.io/pypi/v/google-cloud-orchestration-airflow.svg
     :target: https://pypi.org/project/google-cloud-orchestration-airflow
.. |PyPI-google-cloud-compute| image:: https://img.shields.io/pypi/v/google-cloud-compute.svg
     :target: https://pypi.org/project/google-cloud-compute
.. |PyPI-google-cloud-contact-center-insights| image:: https://img.shields.io/pypi/v/google-cloud-contact-center-insights.svg
     :target: https://pypi.org/project/google-cloud-contact-center-insights
.. |PyPI-google-cloud-containeranalysis| image:: https://img.shields.io/pypi/v/google-cloud-containeranalysis.svg
     :target: https://pypi.org/project/google-cloud-containeranalysis
.. |PyPI-google-cloud-datacatalog| image:: https://img.shields.io/pypi/v/google-cloud-datacatalog.svg
     :target: https://pypi.org/project/google-cloud-datacatalog
.. |PyPI-google-cloud-data-fusion| image:: https://img.shields.io/pypi/v/google-cloud-data-fusion.svg
     :target: https://pypi.org/project/google-cloud-data-fusion
.. |PyPI-google-cloud-dlp| image:: https://img.shields.io/pypi/v/google-cloud-dlp.svg
     :target: https://pypi.org/project/google-cloud-dlp
.. |PyPI-google-cloud-dms| image:: https://img.shields.io/pypi/v/google-cloud-dms.svg
     :target: https://pypi.org/project/google-cloud-dms
.. |PyPI-google-cloud-dataplex| image:: https://img.shields.io/pypi/v/google-cloud-dataplex.svg
     :target: https://pypi.org/project/google-cloud-dataplex
.. |PyPI-google-cloud-dataproc| image:: https://img.shields.io/pypi/v/google-cloud-dataproc.svg
     :target: https://pypi.org/project/google-cloud-dataproc
.. |PyPI-google-cloud-dataproc-metastore| image:: https://img.shields.io/pypi/v/google-cloud-dataproc-metastore.svg
     :target: https://pypi.org/project/google-cloud-dataproc-metastore
.. |PyPI-google-cloud-datastore| image:: https://img.shields.io/pypi/v/google-cloud-datastore.svg
     :target: https://pypi.org/project/google-cloud-datastore
.. |PyPI-google-cloud-datastream| image:: https://img.shields.io/pypi/v/google-cloud-datastream.svg
     :target: https://pypi.org/project/google-cloud-datastream
.. |PyPI-google-cloud-deploy| image:: https://img.shields.io/pypi/v/google-cloud-deploy.svg
     :target: https://pypi.org/project/google-cloud-deploy
.. |PyPI-google-cloud-dialogflow| image:: https://img.shields.io/pypi/v/google-cloud-dialogflow.svg
     :target: https://pypi.org/project/google-cloud-dialogflow
.. |PyPI-google-cloud-dialogflow-cx| image:: https://img.shields.io/pypi/v/google-cloud-dialogflow-cx.svg
     :target: https://pypi.org/project/google-cloud-dialogflow-cx
.. |PyPI-google-cloud-documentai| image:: https://img.shields.io/pypi/v/google-cloud-documentai.svg
     :target: https://pypi.org/project/google-cloud-documentai
.. |PyPI-google-cloud-domains| image:: https://img.shields.io/pypi/v/google-cloud-domains.svg
     :target: https://pypi.org/project/google-cloud-domains
.. |PyPI-google-cloud-essential-contacts| image:: https://img.shields.io/pypi/v/google-cloud-essential-contacts.svg
     :target: https://pypi.org/project/google-cloud-essential-contacts
.. |PyPI-google-cloud-eventarc| image:: https://img.shields.io/pypi/v/google-cloud-eventarc.svg
     :target: https://pypi.org/project/google-cloud-eventarc
.. |PyPI-google-cloud-filestore| image:: https://img.shields.io/pypi/v/google-cloud-filestore.svg
     :target: https://pypi.org/project/google-cloud-filestore
.. |PyPI-google-cloud-firestore| image:: https://img.shields.io/pypi/v/google-cloud-firestore.svg
     :target: https://pypi.org/project/google-cloud-firestore
.. |PyPI-google-cloud-functions| image:: https://img.shields.io/pypi/v/google-cloud-functions.svg
     :target: https://pypi.org/project/google-cloud-functions
.. |PyPI-google-cloud-gke-hub| image:: https://img.shields.io/pypi/v/google-cloud-gke-hub.svg
     :target: https://pypi.org/project/google-cloud-gke-hub
.. |PyPI-grafeas| image:: https://img.shields.io/pypi/v/grafeas.svg
     :target: https://pypi.org/project/grafeas
.. |PyPI-google-cloud-iam-logging| image:: https://img.shields.io/pypi/v/google-cloud-iam-logging.svg
     :target: https://pypi.org/project/google-cloud-iam-logging
.. |PyPI-google-cloud-policy-troubleshooter| image:: https://img.shields.io/pypi/v/google-cloud-policy-troubleshooter.svg
     :target: https://pypi.org/project/google-cloud-policy-troubleshooter
.. |PyPI-google-cloud-ids| image:: https://img.shields.io/pypi/v/google-cloud-ids.svg
     :target: https://pypi.org/project/google-cloud-ids
.. |PyPI-google-cloud-iam| image:: https://img.shields.io/pypi/v/google-cloud-iam.svg
     :target: https://pypi.org/project/google-cloud-iam
.. |PyPI-google-cloud-iap| image:: https://img.shields.io/pypi/v/google-cloud-iap.svg
     :target: https://pypi.org/project/google-cloud-iap
.. |PyPI-google-cloud-kms| image:: https://img.shields.io/pypi/v/google-cloud-kms.svg
     :target: https://pypi.org/project/google-cloud-kms
.. |PyPI-google-cloud-container| image:: https://img.shields.io/pypi/v/google-cloud-container.svg
     :target: https://pypi.org/project/google-cloud-container
.. |PyPI-google-cloud-video-live-stream| image:: https://img.shields.io/pypi/v/google-cloud-video-live-stream.svg
     :target: https://pypi.org/project/google-cloud-video-live-stream
.. |PyPI-google-cloud-logging| image:: https://img.shields.io/pypi/v/google-cloud-logging.svg
     :target: https://pypi.org/project/google-cloud-logging
.. |PyPI-google-cloud-managed-identities| image:: https://img.shields.io/pypi/v/google-cloud-managed-identities.svg
     :target: https://pypi.org/project/google-cloud-managed-identities
.. |PyPI-google-cloud-memcache| image:: https://img.shields.io/pypi/v/google-cloud-memcache.svg
     :target: https://pypi.org/project/google-cloud-memcache
.. |PyPI-google-shopping-merchant-accounts| image:: https://img.shields.io/pypi/v/google-shopping-merchant-accounts.svg
     :target: https://pypi.org/project/google-shopping-merchant-accounts
.. |PyPI-google-shopping-merchant-conversions| image:: https://img.shields.io/pypi/v/google-shopping-merchant-conversions.svg
     :target: https://pypi.org/project/google-shopping-merchant-conversions
.. |PyPI-google-shopping-merchant-datasources| image:: https://img.shields.io/pypi/v/google-shopping-merchant-datasources.svg
     :target: https://pypi.org/project/google-shopping-merchant-datasources
.. |PyPI-google-shopping-merchant-issueresolution| image:: https://img.shields.io/pypi/v/google-shopping-merchant-issueresolution.svg
     :target: https://pypi.org/project/google-shopping-merchant-issueresolution
.. |PyPI-google-shopping-merchant-lfp| image:: https://img.shields.io/pypi/v/google-shopping-merchant-lfp.svg
     :target: https://pypi.org/project/google-shopping-merchant-lfp
.. |PyPI-google-shopping-merchant-notifications| image:: https://img.shields.io/pypi/v/google-shopping-merchant-notifications.svg
     :target: https://pypi.org/project/google-shopping-merchant-notifications
.. |PyPI-google-shopping-merchant-ordertracking| image:: https://img.shields.io/pypi/v/google-shopping-merchant-ordertracking.svg
     :target: https://pypi.org/project/google-shopping-merchant-ordertracking
.. |PyPI-google-shopping-merchant-products| image:: https://img.shields.io/pypi/v/google-shopping-merchant-products.svg
     :target: https://pypi.org/project/google-shopping-merchant-products
.. |PyPI-google-shopping-merchant-promotions| image:: https://img.shields.io/pypi/v/google-shopping-merchant-promotions.svg
     :target: https://pypi.org/project/google-shopping-merchant-promotions
.. |PyPI-google-shopping-merchant-inventories| image:: https://img.shields.io/pypi/v/google-shopping-merchant-inventories.svg
     :target: https://pypi.org/project/google-shopping-merchant-inventories
.. |PyPI-google-shopping-merchant-reports| image:: https://img.shields.io/pypi/v/google-shopping-merchant-reports.svg
     :target: https://pypi.org/project/google-shopping-merchant-reports
.. |PyPI-google-cloud-monitoring-metrics-scopes| image:: https://img.shields.io/pypi/v/google-cloud-monitoring-metrics-scopes.svg
     :target: https://pypi.org/project/google-cloud-monitoring-metrics-scopes
.. |PyPI-google-cloud-monitoring-dashboards| image:: https://img.shields.io/pypi/v/google-cloud-monitoring-dashboards.svg
     :target: https://pypi.org/project/google-cloud-monitoring-dashboards
.. |PyPI-google-cloud-ndb| image:: https://img.shields.io/pypi/v/google-cloud-ndb.svg
     :target: https://pypi.org/project/google-cloud-ndb
.. |PyPI-google-cloud-language| image:: https://img.shields.io/pypi/v/google-cloud-language.svg
     :target: https://pypi.org/project/google-cloud-language
.. |PyPI-google-cloud-network-connectivity| image:: https://img.shields.io/pypi/v/google-cloud-network-connectivity.svg
     :target: https://pypi.org/project/google-cloud-network-connectivity
.. |PyPI-google-cloud-network-management| image:: https://img.shields.io/pypi/v/google-cloud-network-management.svg
     :target: https://pypi.org/project/google-cloud-network-management
.. |PyPI-google-cloud-os-config| image:: https://img.shields.io/pypi/v/google-cloud-os-config.svg
     :target: https://pypi.org/project/google-cloud-os-config
.. |PyPI-google-cloud-os-login| image:: https://img.shields.io/pypi/v/google-cloud-os-login.svg
     :target: https://pypi.org/project/google-cloud-os-login
.. |PyPI-google-cloud-optimization| image:: https://img.shields.io/pypi/v/google-cloud-optimization.svg
     :target: https://pypi.org/project/google-cloud-optimization
.. |PyPI-google-cloud-org-policy| image:: https://img.shields.io/pypi/v/google-cloud-org-policy.svg
     :target: https://pypi.org/project/google-cloud-org-policy
.. |PyPI-db-dtypes| image:: https://img.shields.io/pypi/v/db-dtypes.svg
     :target: https://pypi.org/project/db-dtypes
.. |PyPI-google-cloud-private-ca| image:: https://img.shields.io/pypi/v/google-cloud-private-ca.svg
     :target: https://pypi.org/project/google-cloud-private-ca
.. |PyPI-proto-plus| image:: https://img.shields.io/pypi/v/proto-plus.svg
     :target: https://pypi.org/project/proto-plus
.. |PyPI-google-cloud-pubsub| image:: https://img.shields.io/pypi/v/google-cloud-pubsub.svg
     :target: https://pypi.org/project/google-cloud-pubsub
.. |PyPI-google-cloud-pubsublite| image:: https://img.shields.io/pypi/v/google-cloud-pubsublite.svg
     :target: https://pypi.org/project/google-cloud-pubsublite
.. |PyPI-google-cloud-testutils| image:: https://img.shields.io/pypi/v/google-cloud-testutils.svg
     :target: https://pypi.org/project/google-cloud-testutils
.. |PyPI-google-cloud-recommender| image:: https://img.shields.io/pypi/v/google-cloud-recommender.svg
     :target: https://pypi.org/project/google-cloud-recommender
.. |PyPI-google-cloud-redis| image:: https://img.shields.io/pypi/v/google-cloud-redis.svg
     :target: https://pypi.org/project/google-cloud-redis
.. |PyPI-google-cloud-resource-manager| image:: https://img.shields.io/pypi/v/google-cloud-resource-manager.svg
     :target: https://pypi.org/project/google-cloud-resource-manager
.. |PyPI-google-resumable-media| image:: https://img.shields.io/pypi/v/google-resumable-media.svg
     :target: https://pypi.org/project/google-resumable-media
.. |PyPI-google-cloud-retail| image:: https://img.shields.io/pypi/v/google-cloud-retail.svg
     :target: https://pypi.org/project/google-cloud-retail
.. |PyPI-sqlalchemy-bigquery| image:: https://img.shields.io/pypi/v/sqlalchemy-bigquery.svg
     :target: https://pypi.org/project/sqlalchemy-bigquery
.. |PyPI-google-cloud-scheduler| image:: https://img.shields.io/pypi/v/google-cloud-scheduler.svg
     :target: https://pypi.org/project/google-cloud-scheduler
.. |PyPI-google-cloud-secret-manager| image:: https://img.shields.io/pypi/v/google-cloud-secret-manager.svg
     :target: https://pypi.org/project/google-cloud-secret-manager
.. |PyPI-google-cloud-securitycenter| image:: https://img.shields.io/pypi/v/google-cloud-securitycenter.svg
     :target: https://pypi.org/project/google-cloud-securitycenter
.. |PyPI-google-cloud-websecurityscanner| image:: https://img.shields.io/pypi/v/google-cloud-websecurityscanner.svg
     :target: https://pypi.org/project/google-cloud-websecurityscanner
.. |PyPI-google-cloud-service-control| image:: https://img.shields.io/pypi/v/google-cloud-service-control.svg
     :target: https://pypi.org/project/google-cloud-service-control
.. |PyPI-google-cloud-service-directory| image:: https://img.shields.io/pypi/v/google-cloud-service-directory.svg
     :target: https://pypi.org/project/google-cloud-service-directory
.. |PyPI-google-cloud-service-management| image:: https://img.shields.io/pypi/v/google-cloud-service-management.svg
     :target: https://pypi.org/project/google-cloud-service-management
.. |PyPI-google-cloud-service-usage| image:: https://img.shields.io/pypi/v/google-cloud-service-usage.svg
     :target: https://pypi.org/project/google-cloud-service-usage
.. |PyPI-google-cloud-shell| image:: https://img.shields.io/pypi/v/google-cloud-shell.svg
     :target: https://pypi.org/project/google-cloud-shell
.. |PyPI-google-shopping-merchant-quota| image:: https://img.shields.io/pypi/v/google-shopping-merchant-quota.svg
     :target: https://pypi.org/project/google-shopping-merchant-quota
.. |PyPI-google-shopping-type| image:: https://img.shields.io/pypi/v/google-shopping-type.svg
     :target: https://pypi.org/project/google-shopping-type
.. |PyPI-google-cloud-source-context| image:: https://img.shields.io/pypi/v/google-cloud-source-context.svg
     :target: https://pypi.org/project/google-cloud-source-context
.. |PyPI-google-cloud-spanner| image:: https://img.shields.io/pypi/v/google-cloud-spanner.svg
     :target: https://pypi.org/project/google-cloud-spanner
.. |PyPI-django-google-spanner| image:: https://img.shields.io/pypi/v/django-google-spanner.svg
     :target: https://pypi.org/project/django-google-spanner
.. |PyPI-sqlalchemy-spanner| image:: https://img.shields.io/pypi/v/sqlalchemy-spanner.svg
     :target: https://pypi.org/project/sqlalchemy-spanner
.. |PyPI-google-cloud-speech| image:: https://img.shields.io/pypi/v/google-cloud-speech.svg
     :target: https://pypi.org/project/google-cloud-speech
.. |PyPI-gcp-sphinx-docfx-yaml| image:: https://img.shields.io/pypi/v/gcp-sphinx-docfx-yaml.svg
     :target: https://pypi.org/project/gcp-sphinx-docfx-yaml
.. |PyPI-google-cloud-monitoring| image:: https://img.shields.io/pypi/v/google-cloud-monitoring.svg
     :target: https://pypi.org/project/google-cloud-monitoring
.. |PyPI-google-cloud-storage| image:: https://img.shields.io/pypi/v/google-cloud-storage.svg
     :target: https://pypi.org/project/google-cloud-storage
.. |PyPI-google-cloud-storage-control| image:: https://img.shields.io/pypi/v/google-cloud-storage-control.svg
     :target: https://pypi.org/project/google-cloud-storage-control
.. |PyPI-google-cloud-storage-transfer| image:: https://img.shields.io/pypi/v/google-cloud-storage-transfer.svg
     :target: https://pypi.org/project/google-cloud-storage-transfer
.. |PyPI-google-cloud-tpu| image:: https://img.shields.io/pypi/v/google-cloud-tpu.svg
     :target: https://pypi.org/project/google-cloud-tpu
.. |PyPI-google-cloud-talent| image:: https://img.shields.io/pypi/v/google-cloud-talent.svg
     :target: https://pypi.org/project/google-cloud-talent
.. |PyPI-google-cloud-tasks| image:: https://img.shields.io/pypi/v/google-cloud-tasks.svg
     :target: https://pypi.org/project/google-cloud-tasks
.. |PyPI-google-cloud-texttospeech| image:: https://img.shields.io/pypi/v/google-cloud-texttospeech.svg
     :target: https://pypi.org/project/google-cloud-texttospeech
.. |PyPI-google-cloud-trace| image:: https://img.shields.io/pypi/v/google-cloud-trace.svg
     :target: https://pypi.org/project/google-cloud-trace
.. |PyPI-google-cloud-video-transcoder| image:: https://img.shields.io/pypi/v/google-cloud-video-transcoder.svg
     :target: https://pypi.org/project/google-cloud-video-transcoder
.. |PyPI-google-cloud-translate| image:: https://img.shields.io/pypi/v/google-cloud-translate.svg
     :target: https://pypi.org/project/google-cloud-translate
.. |PyPI-google-cloud-vm-migration| image:: https://img.shields.io/pypi/v/google-cloud-vm-migration.svg
     :target: https://pypi.org/project/google-cloud-vm-migration
.. |PyPI-google-cloud-videointelligence| image:: https://img.shields.io/pypi/v/google-cloud-videointelligence.svg
     :target: https://pypi.org/project/google-cloud-videointelligence
.. |PyPI-google-cloud-vpc-access| image:: https://img.shields.io/pypi/v/google-cloud-vpc-access.svg
     :target: https://pypi.org/project/google-cloud-vpc-access
.. |PyPI-google-cloud-vision| image:: https://img.shields.io/pypi/v/google-cloud-vision.svg
     :target: https://pypi.org/project/google-cloud-vision
.. |PyPI-google-cloud-webrisk| image:: https://img.shields.io/pypi/v/google-cloud-webrisk.svg
     :target: https://pypi.org/project/google-cloud-webrisk
.. |PyPI-google-cloud-workflows| image:: https://img.shields.io/pypi/v/google-cloud-workflows.svg
     :target: https://pypi.org/project/google-cloud-workflows
.. |PyPI-google-cloud-recaptcha-enterprise| image:: https://img.shields.io/pypi/v/google-cloud-recaptcha-enterprise.svg
     :target: https://pypi.org/project/google-cloud-recaptcha-enterprise
.. |PyPI-google-cloud-apihub| image:: https://img.shields.io/pypi/v/google-cloud-apihub.svg
     :target: https://pypi.org/project/google-cloud-apihub
.. |PyPI-google-cloud-api-keys| image:: https://img.shields.io/pypi/v/google-cloud-api-keys.svg
     :target: https://pypi.org/project/google-cloud-api-keys
.. |PyPI-google-cloud-apiregistry| image:: https://img.shields.io/pypi/v/google-cloud-apiregistry.svg
     :target: https://pypi.org/project/google-cloud-apiregistry
.. |PyPI-google-cloud-access-context-manager| image:: https://img.shields.io/pypi/v/google-cloud-access-context-manager.svg
     :target: https://pypi.org/project/google-cloud-access-context-manager
.. |PyPI-google-ads-admanager| image:: https://img.shields.io/pypi/v/google-ads-admanager.svg
     :target: https://pypi.org/project/google-ads-admanager
.. |PyPI-google-maps-addressvalidation| image:: https://img.shields.io/pypi/v/google-maps-addressvalidation.svg
     :target: https://pypi.org/project/google-maps-addressvalidation
.. |PyPI-google-cloud-advisorynotifications| image:: https://img.shields.io/pypi/v/google-cloud-advisorynotifications.svg
     :target: https://pypi.org/project/google-cloud-advisorynotifications
.. |PyPI-google-cloud-alloydb| image:: https://img.shields.io/pypi/v/google-cloud-alloydb.svg
     :target: https://pypi.org/project/google-cloud-alloydb
.. |PyPI-google-cloud-alloydb-connectors| image:: https://img.shields.io/pypi/v/google-cloud-alloydb-connectors.svg
     :target: https://pypi.org/project/google-cloud-alloydb-connectors
.. |PyPI-google-analytics-admin| image:: https://img.shields.io/pypi/v/google-analytics-admin.svg
     :target: https://pypi.org/project/google-analytics-admin
.. |PyPI-google-analytics-data| image:: https://img.shields.io/pypi/v/google-analytics-data.svg
     :target: https://pypi.org/project/google-analytics-data
.. |PyPI-google-cloud-gke-multicloud| image:: https://img.shields.io/pypi/v/google-cloud-gke-multicloud.svg
     :target: https://pypi.org/project/google-cloud-gke-multicloud
.. |PyPI-google-cloud-financialservices| image:: https://img.shields.io/pypi/v/google-cloud-financialservices.svg
     :target: https://pypi.org/project/google-cloud-financialservices
.. |PyPI-google-cloud-apphub| image:: https://img.shields.io/pypi/v/google-cloud-apphub.svg
     :target: https://pypi.org/project/google-cloud-apphub
.. |PyPI-google-cloud-appoptimize| image:: https://img.shields.io/pypi/v/google-cloud-appoptimize.svg
     :target: https://pypi.org/project/google-cloud-appoptimize
.. |PyPI-google-apps-card| image:: https://img.shields.io/pypi/v/google-apps-card.svg
     :target: https://pypi.org/project/google-apps-card
.. |PyPI-google-apps-script-type| image:: https://img.shields.io/pypi/v/google-apps-script-type.svg
     :target: https://pypi.org/project/google-apps-script-type
.. |PyPI-google-cloud-audit-log| image:: https://img.shields.io/pypi/v/google-cloud-audit-log.svg
     :target: https://pypi.org/project/google-cloud-audit-log
.. |PyPI-google-cloud-auditmanager| image:: https://img.shields.io/pypi/v/google-cloud-auditmanager.svg
     :target: https://pypi.org/project/google-cloud-auditmanager
.. |PyPI-google-auth-httplib2| image:: https://img.shields.io/pypi/v/google-auth-httplib2.svg
     :target: https://pypi.org/project/google-auth-httplib2
.. |PyPI-google-cloud-backupdr| image:: https://img.shields.io/pypi/v/google-cloud-backupdr.svg
     :target: https://pypi.org/project/google-cloud-backupdr
.. |PyPI-google-cloud-gke-backup| image:: https://img.shields.io/pypi/v/google-cloud-gke-backup.svg
     :target: https://pypi.org/project/google-cloud-gke-backup
.. |PyPI-google-cloud-batch| image:: https://img.shields.io/pypi/v/google-cloud-batch.svg
     :target: https://pypi.org/project/google-cloud-batch
.. |PyPI-google-cloud-beyondcorp-appconnections| image:: https://img.shields.io/pypi/v/google-cloud-beyondcorp-appconnections.svg
     :target: https://pypi.org/project/google-cloud-beyondcorp-appconnections
.. |PyPI-google-cloud-beyondcorp-appconnectors| image:: https://img.shields.io/pypi/v/google-cloud-beyondcorp-appconnectors.svg
     :target: https://pypi.org/project/google-cloud-beyondcorp-appconnectors
.. |PyPI-google-cloud-beyondcorp-appgateways| image:: https://img.shields.io/pypi/v/google-cloud-beyondcorp-appgateways.svg
     :target: https://pypi.org/project/google-cloud-beyondcorp-appgateways
.. |PyPI-google-cloud-beyondcorp-clientconnectorservices| image:: https://img.shields.io/pypi/v/google-cloud-beyondcorp-clientconnectorservices.svg
     :target: https://pypi.org/project/google-cloud-beyondcorp-clientconnectorservices
.. |PyPI-google-cloud-beyondcorp-clientgateways| image:: https://img.shields.io/pypi/v/google-cloud-beyondcorp-clientgateways.svg
     :target: https://pypi.org/project/google-cloud-beyondcorp-clientgateways
.. |PyPI-google-cloud-biglake-hive| image:: https://img.shields.io/pypi/v/google-cloud-biglake-hive.svg
     :target: https://pypi.org/project/google-cloud-biglake-hive
.. |PyPI-google-cloud-biglake| image:: https://img.shields.io/pypi/v/google-cloud-biglake.svg
     :target: https://pypi.org/project/google-cloud-biglake
.. |PyPI-google-cloud-bigquery-biglake| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-biglake.svg
     :target: https://pypi.org/project/google-cloud-bigquery-biglake
.. |PyPI-google-cloud-bigquery-analyticshub| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-analyticshub.svg
     :target: https://pypi.org/project/google-cloud-bigquery-analyticshub
.. |PyPI-google-cloud-bigquery-data-exchange| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-data-exchange.svg
     :target: https://pypi.org/project/google-cloud-bigquery-data-exchange
.. |PyPI-google-cloud-bigquery-datapolicies| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-datapolicies.svg
     :target: https://pypi.org/project/google-cloud-bigquery-datapolicies
.. |PyPI-google-cloud-bigquery-migration| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-migration.svg
     :target: https://pypi.org/project/google-cloud-bigquery-migration
.. |PyPI-bigquery-magics| image:: https://img.shields.io/pypi/v/bigquery-magics.svg
     :target: https://pypi.org/project/bigquery-magics
.. |PyPI-pandas-gbq| image:: https://img.shields.io/pypi/v/pandas-gbq.svg
     :target: https://pypi.org/project/pandas-gbq
.. |PyPI-google-shopping-css| image:: https://img.shields.io/pypi/v/google-shopping-css.svg
     :target: https://pypi.org/project/google-shopping-css
.. |PyPI-google-cloud-capacityplanner| image:: https://img.shields.io/pypi/v/google-cloud-capacityplanner.svg
     :target: https://pypi.org/project/google-cloud-capacityplanner
.. |PyPI-google-apps-chat| image:: https://img.shields.io/pypi/v/google-apps-chat.svg
     :target: https://pypi.org/project/google-apps-chat
.. |PyPI-google-cloud-chronicle| image:: https://img.shields.io/pypi/v/google-cloud-chronicle.svg
     :target: https://pypi.org/project/google-cloud-chronicle
.. |PyPI-google-cloud-hypercomputecluster| image:: https://img.shields.io/pypi/v/google-cloud-hypercomputecluster.svg
     :target: https://pypi.org/project/google-cloud-hypercomputecluster
.. |PyPI-google-cloud-commerce-consumer-procurement| image:: https://img.shields.io/pypi/v/google-cloud-commerce-consumer-procurement.svg
     :target: https://pypi.org/project/google-cloud-commerce-consumer-procurement
.. |PyPI-google-cloud-compute-v1beta| image:: https://img.shields.io/pypi/v/google-cloud-compute-v1beta.svg
     :target: https://pypi.org/project/google-cloud-compute-v1beta
.. |PyPI-google-cloud-confidentialcomputing| image:: https://img.shields.io/pypi/v/google-cloud-confidentialcomputing.svg
     :target: https://pypi.org/project/google-cloud-confidentialcomputing
.. |PyPI-google-cloud-configdelivery| image:: https://img.shields.io/pypi/v/google-cloud-configdelivery.svg
     :target: https://pypi.org/project/google-cloud-configdelivery
.. |PyPI-google-cloud-cloudcontrolspartner| image:: https://img.shields.io/pypi/v/google-cloud-cloudcontrolspartner.svg
     :target: https://pypi.org/project/google-cloud-cloudcontrolspartner
.. |PyPI-google-cloud-dns| image:: https://img.shields.io/pypi/v/google-cloud-dns.svg
     :target: https://pypi.org/project/google-cloud-dns
.. |PyPI-google-cloud-geminidataanalytics| image:: https://img.shields.io/pypi/v/google-cloud-geminidataanalytics.svg
     :target: https://pypi.org/project/google-cloud-geminidataanalytics
.. |PyPI-google-cloud-datalabeling| image:: https://img.shields.io/pypi/v/google-cloud-datalabeling.svg
     :target: https://pypi.org/project/google-cloud-datalabeling
.. |PyPI-google-cloud-datacatalog-lineage-configmanagement| image:: https://img.shields.io/pypi/v/google-cloud-datacatalog-lineage-configmanagement.svg
     :target: https://pypi.org/project/google-cloud-datacatalog-lineage-configmanagement
.. |PyPI-google-cloud-datacatalog-lineage| image:: https://img.shields.io/pypi/v/google-cloud-datacatalog-lineage.svg
     :target: https://pypi.org/project/google-cloud-datacatalog-lineage
.. |PyPI-google-ads-datamanager| image:: https://img.shields.io/pypi/v/google-ads-datamanager.svg
     :target: https://pypi.org/project/google-ads-datamanager
.. |PyPI-google-cloud-data-qna| image:: https://img.shields.io/pypi/v/google-cloud-data-qna.svg
     :target: https://pypi.org/project/google-cloud-data-qna
.. |PyPI-google-cloud-databasecenter| image:: https://img.shields.io/pypi/v/google-cloud-databasecenter.svg
     :target: https://pypi.org/project/google-cloud-databasecenter
.. |PyPI-google-cloud-dataflow-client| image:: https://img.shields.io/pypi/v/google-cloud-dataflow-client.svg
     :target: https://pypi.org/project/google-cloud-dataflow-client
.. |PyPI-google-cloud-dataform| image:: https://img.shields.io/pypi/v/google-cloud-dataform.svg
     :target: https://pypi.org/project/google-cloud-dataform
.. |PyPI-google-cloud-developerconnect| image:: https://img.shields.io/pypi/v/google-cloud-developerconnect.svg
     :target: https://pypi.org/project/google-cloud-developerconnect
.. |PyPI-google-cloud-devicestreaming| image:: https://img.shields.io/pypi/v/google-cloud-devicestreaming.svg
     :target: https://pypi.org/project/google-cloud-devicestreaming
.. |PyPI-google-cloud-discoveryengine| image:: https://img.shields.io/pypi/v/google-cloud-discoveryengine.svg
     :target: https://pypi.org/project/google-cloud-discoveryengine
.. |PyPI-google-cloud-edgecontainer| image:: https://img.shields.io/pypi/v/google-cloud-edgecontainer.svg
     :target: https://pypi.org/project/google-cloud-edgecontainer
.. |PyPI-google-cloud-edgenetwork| image:: https://img.shields.io/pypi/v/google-cloud-edgenetwork.svg
     :target: https://pypi.org/project/google-cloud-edgenetwork
.. |PyPI-google-cloud-documentai-toolbox| image:: https://img.shields.io/pypi/v/google-cloud-documentai-toolbox.svg
     :target: https://pypi.org/project/google-cloud-documentai-toolbox
.. |PyPI-google-cloud-contentwarehouse| image:: https://img.shields.io/pypi/v/google-cloud-contentwarehouse.svg
     :target: https://pypi.org/project/google-cloud-contentwarehouse
.. |PyPI-google-cloud-enterpriseknowledgegraph| image:: https://img.shields.io/pypi/v/google-cloud-enterpriseknowledgegraph.svg
     :target: https://pypi.org/project/google-cloud-enterpriseknowledgegraph
.. |PyPI-google-cloud-error-reporting| image:: https://img.shields.io/pypi/v/google-cloud-error-reporting.svg
     :target: https://pypi.org/project/google-cloud-error-reporting
.. |PyPI-google-cloud-eventarc-publishing| image:: https://img.shields.io/pypi/v/google-cloud-eventarc-publishing.svg
     :target: https://pypi.org/project/google-cloud-eventarc-publishing
.. |PyPI-google-cloud-gdchardwaremanagement| image:: https://img.shields.io/pypi/v/google-cloud-gdchardwaremanagement.svg
     :target: https://pypi.org/project/google-cloud-gdchardwaremanagement
.. |PyPI-google-cloud-gke-connect-gateway| image:: https://img.shields.io/pypi/v/google-cloud-gke-connect-gateway.svg
     :target: https://pypi.org/project/google-cloud-gke-connect-gateway
.. |PyPI-google-cloud-gkerecommender| image:: https://img.shields.io/pypi/v/google-cloud-gkerecommender.svg
     :target: https://pypi.org/project/google-cloud-gkerecommender
.. |PyPI-google-cloud-ces| image:: https://img.shields.io/pypi/v/google-cloud-ces.svg
     :target: https://pypi.org/project/google-cloud-ces
.. |PyPI-google-ai-generativelanguage| image:: https://img.shields.io/pypi/v/google-ai-generativelanguage.svg
     :target: https://pypi.org/project/google-ai-generativelanguage
.. |PyPI-google-geo-type| image:: https://img.shields.io/pypi/v/google-geo-type.svg
     :target: https://pypi.org/project/google-geo-type
.. |PyPI-google-maps-geocode| image:: https://img.shields.io/pypi/v/google-maps-geocode.svg
     :target: https://pypi.org/project/google-maps-geocode
.. |PyPI-grpc-google-iam-v1| image:: https://img.shields.io/pypi/v/grpc-google-iam-v1.svg
     :target: https://pypi.org/project/grpc-google-iam-v1
.. |PyPI-google-cloud-config| image:: https://img.shields.io/pypi/v/google-cloud-config.svg
     :target: https://pypi.org/project/google-cloud-config
.. |PyPI-google-cloud-kms-inventory| image:: https://img.shields.io/pypi/v/google-cloud-kms-inventory.svg
     :target: https://pypi.org/project/google-cloud-kms-inventory
.. |PyPI-google-maps-fleetengine-delivery| image:: https://img.shields.io/pypi/v/google-maps-fleetengine-delivery.svg
     :target: https://pypi.org/project/google-maps-fleetengine-delivery
.. |PyPI-google-cloud-licensemanager| image:: https://img.shields.io/pypi/v/google-cloud-licensemanager.svg
     :target: https://pypi.org/project/google-cloud-licensemanager
.. |PyPI-google-cloud-life-sciences| image:: https://img.shields.io/pypi/v/google-cloud-life-sciences.svg
     :target: https://pypi.org/project/google-cloud-life-sciences
.. |PyPI-google-maps-fleetengine| image:: https://img.shields.io/pypi/v/google-maps-fleetengine.svg
     :target: https://pypi.org/project/google-maps-fleetengine
.. |PyPI-google-cloud-locationfinder| image:: https://img.shields.io/pypi/v/google-cloud-locationfinder.svg
     :target: https://pypi.org/project/google-cloud-locationfinder
.. |PyPI-google-cloud-maintenance-api| image:: https://img.shields.io/pypi/v/google-cloud-maintenance-api.svg
     :target: https://pypi.org/project/google-cloud-maintenance-api
.. |PyPI-google-cloud-lustre| image:: https://img.shields.io/pypi/v/google-cloud-lustre.svg
     :target: https://pypi.org/project/google-cloud-lustre
.. |PyPI-google-cloud-managedkafka| image:: https://img.shields.io/pypi/v/google-cloud-managedkafka.svg
     :target: https://pypi.org/project/google-cloud-managedkafka
.. |PyPI-google-cloud-managedkafka-schemaregistry| image:: https://img.shields.io/pypi/v/google-cloud-managedkafka-schemaregistry.svg
     :target: https://pypi.org/project/google-cloud-managedkafka-schemaregistry
.. |PyPI-google-maps-mapsplatformdatasets| image:: https://img.shields.io/pypi/v/google-maps-mapsplatformdatasets.svg
     :target: https://pypi.org/project/google-maps-mapsplatformdatasets
.. |PyPI-google-maps-routing| image:: https://img.shields.io/pypi/v/google-maps-routing.svg
     :target: https://pypi.org/project/google-maps-routing
.. |PyPI-google-ads-marketingplatform-admin| image:: https://img.shields.io/pypi/v/google-ads-marketingplatform-admin.svg
     :target: https://pypi.org/project/google-ads-marketingplatform-admin
.. |PyPI-google-cloud-media-translation| image:: https://img.shields.io/pypi/v/google-cloud-media-translation.svg
     :target: https://pypi.org/project/google-cloud-media-translation
.. |PyPI-google-apps-meet| image:: https://img.shields.io/pypi/v/google-apps-meet.svg
     :target: https://pypi.org/project/google-apps-meet
.. |PyPI-google-cloud-memorystore| image:: https://img.shields.io/pypi/v/google-cloud-memorystore.svg
     :target: https://pypi.org/project/google-cloud-memorystore
.. |PyPI-google-cloud-redis-cluster| image:: https://img.shields.io/pypi/v/google-cloud-redis-cluster.svg
     :target: https://pypi.org/project/google-cloud-redis-cluster
.. |PyPI-google-shopping-merchant-productstudio| image:: https://img.shields.io/pypi/v/google-shopping-merchant-productstudio.svg
     :target: https://pypi.org/project/google-shopping-merchant-productstudio
.. |PyPI-google-shopping-merchant-reviews| image:: https://img.shields.io/pypi/v/google-shopping-merchant-reviews.svg
     :target: https://pypi.org/project/google-shopping-merchant-reviews
.. |PyPI-google-cloud-migrationcenter| image:: https://img.shields.io/pypi/v/google-cloud-migrationcenter.svg
     :target: https://pypi.org/project/google-cloud-migrationcenter
.. |PyPI-google-cloud-modelarmor| image:: https://img.shields.io/pypi/v/google-cloud-modelarmor.svg
     :target: https://pypi.org/project/google-cloud-modelarmor
.. |PyPI-google-maps-navconnect| image:: https://img.shields.io/pypi/v/google-maps-navconnect.svg
     :target: https://pypi.org/project/google-maps-navconnect
.. |PyPI-google-cloud-netapp| image:: https://img.shields.io/pypi/v/google-cloud-netapp.svg
     :target: https://pypi.org/project/google-cloud-netapp
.. |PyPI-google-cloud-network-security| image:: https://img.shields.io/pypi/v/google-cloud-network-security.svg
     :target: https://pypi.org/project/google-cloud-network-security
.. |PyPI-google-cloud-network-services| image:: https://img.shields.io/pypi/v/google-cloud-network-services.svg
     :target: https://pypi.org/project/google-cloud-network-services
.. |PyPI-google-cloud-oracledatabase| image:: https://img.shields.io/pypi/v/google-cloud-oracledatabase.svg
     :target: https://pypi.org/project/google-cloud-oracledatabase
.. |PyPI-google-cloud-parallelstore| image:: https://img.shields.io/pypi/v/google-cloud-parallelstore.svg
     :target: https://pypi.org/project/google-cloud-parallelstore
.. |PyPI-google-cloud-parametermanager| image:: https://img.shields.io/pypi/v/google-cloud-parametermanager.svg
     :target: https://pypi.org/project/google-cloud-parametermanager
.. |PyPI-google-cloud-phishing-protection| image:: https://img.shields.io/pypi/v/google-cloud-phishing-protection.svg
     :target: https://pypi.org/project/google-cloud-phishing-protection
.. |PyPI-google-maps-places| image:: https://img.shields.io/pypi/v/google-maps-places.svg
     :target: https://pypi.org/project/google-maps-places
.. |PyPI-google-maps-areainsights| image:: https://img.shields.io/pypi/v/google-maps-areainsights.svg
     :target: https://pypi.org/project/google-maps-areainsights
.. |PyPI-google-cloud-policysimulator| image:: https://img.shields.io/pypi/v/google-cloud-policysimulator.svg
     :target: https://pypi.org/project/google-cloud-policysimulator
.. |PyPI-google-cloud-policytroubleshooter-iam| image:: https://img.shields.io/pypi/v/google-cloud-policytroubleshooter-iam.svg
     :target: https://pypi.org/project/google-cloud-policytroubleshooter-iam
.. |PyPI-google-cloud-private-catalog| image:: https://img.shields.io/pypi/v/google-cloud-private-catalog.svg
     :target: https://pypi.org/project/google-cloud-private-catalog
.. |PyPI-google-cloud-privilegedaccessmanager| image:: https://img.shields.io/pypi/v/google-cloud-privilegedaccessmanager.svg
     :target: https://pypi.org/project/google-cloud-privilegedaccessmanager
.. |PyPI-google-cloud-security-publicca| image:: https://img.shields.io/pypi/v/google-cloud-security-publicca.svg
     :target: https://pypi.org/project/google-cloud-security-publicca
.. |PyPI-google-cloud-quotas| image:: https://img.shields.io/pypi/v/google-cloud-quotas.svg
     :target: https://pypi.org/project/google-cloud-quotas
.. |PyPI-google-cloud-rapidmigrationassessment| image:: https://img.shields.io/pypi/v/google-cloud-rapidmigrationassessment.svg
     :target: https://pypi.org/project/google-cloud-rapidmigrationassessment
.. |PyPI-google-cloud-recommendations-ai| image:: https://img.shields.io/pypi/v/google-cloud-recommendations-ai.svg
     :target: https://pypi.org/project/google-cloud-recommendations-ai
.. |PyPI-google-maps-routeoptimization| image:: https://img.shields.io/pypi/v/google-maps-routeoptimization.svg
     :target: https://pypi.org/project/google-maps-routeoptimization
.. |PyPI-google-cloud-run| image:: https://img.shields.io/pypi/v/google-cloud-run.svg
     :target: https://pypi.org/project/google-cloud-run
.. |PyPI-google-cloud-runtimeconfig| image:: https://img.shields.io/pypi/v/google-cloud-runtimeconfig.svg
     :target: https://pypi.org/project/google-cloud-runtimeconfig
.. |PyPI-google-cloud-saasplatform-saasservicemgmt| image:: https://img.shields.io/pypi/v/google-cloud-saasplatform-saasservicemgmt.svg
     :target: https://pypi.org/project/google-cloud-saasplatform-saasservicemgmt
.. |PyPI-google-cloud-securesourcemanager| image:: https://img.shields.io/pypi/v/google-cloud-securesourcemanager.svg
     :target: https://pypi.org/project/google-cloud-securesourcemanager
.. |PyPI-google-cloud-securitycentermanagement| image:: https://img.shields.io/pypi/v/google-cloud-securitycentermanagement.svg
     :target: https://pypi.org/project/google-cloud-securitycentermanagement
.. |PyPI-google-cloud-cloudsecuritycompliance| image:: https://img.shields.io/pypi/v/google-cloud-cloudsecuritycompliance.svg
     :target: https://pypi.org/project/google-cloud-cloudsecuritycompliance
.. |PyPI-google-cloud-servicehealth| image:: https://img.shields.io/pypi/v/google-cloud-servicehealth.svg
     :target: https://pypi.org/project/google-cloud-servicehealth
.. |PyPI-google-maps-solar| image:: https://img.shields.io/pypi/v/google-maps-solar.svg
     :target: https://pypi.org/project/google-maps-solar
.. |PyPI-google-cloud-spanner-dbapi-driver| image:: https://img.shields.io/pypi/v/google-cloud-spanner-dbapi-driver.svg
     :target: https://pypi.org/project/google-cloud-spanner-dbapi-driver
.. |PyPI-google-cloud-storagebatchoperations| image:: https://img.shields.io/pypi/v/google-cloud-storagebatchoperations.svg
     :target: https://pypi.org/project/google-cloud-storagebatchoperations
.. |PyPI-google-cloud-storageinsights| image:: https://img.shields.io/pypi/v/google-cloud-storageinsights.svg
     :target: https://pypi.org/project/google-cloud-storageinsights
.. |PyPI-google-cloud-support| image:: https://img.shields.io/pypi/v/google-cloud-support.svg
     :target: https://pypi.org/project/google-cloud-support
.. |PyPI-google-cloud-telcoautomation| image:: https://img.shields.io/pypi/v/google-cloud-telcoautomation.svg
     :target: https://pypi.org/project/google-cloud-telcoautomation
.. |PyPI-google-cloud-vmwareengine| image:: https://img.shields.io/pypi/v/google-cloud-vmwareengine.svg
     :target: https://pypi.org/project/google-cloud-vmwareengine
.. |PyPI-google-cloud-vectorsearch| image:: https://img.shields.io/pypi/v/google-cloud-vectorsearch.svg
     :target: https://pypi.org/project/google-cloud-vectorsearch
.. |PyPI-google-cloud-video-stitcher| image:: https://img.shields.io/pypi/v/google-cloud-video-stitcher.svg
     :target: https://pypi.org/project/google-cloud-video-stitcher
.. |PyPI-google-cloud-visionai| image:: https://img.shields.io/pypi/v/google-cloud-visionai.svg
     :target: https://pypi.org/project/google-cloud-visionai
.. |PyPI-google-cloud-workloadmanager| image:: https://img.shields.io/pypi/v/google-cloud-workloadmanager.svg
     :target: https://pypi.org/project/google-cloud-workloadmanager
.. |PyPI-google-cloud-gsuiteaddons| image:: https://img.shields.io/pypi/v/google-cloud-gsuiteaddons.svg
     :target: https://pypi.org/project/google-cloud-gsuiteaddons
.. |PyPI-google-apps-events-subscriptions| image:: https://img.shields.io/pypi/v/google-apps-events-subscriptions.svg
     :target: https://pypi.org/project/google-apps-events-subscriptions
.. |PyPI-google-cloud-workstations| image:: https://img.shields.io/pypi/v/google-cloud-workstations.svg
     :target: https://pypi.org/project/google-cloud-workstations
.. |PyPI-google-cloud-iamconnectorcredentials| image:: https://img.shields.io/pypi/v/google-cloud-iamconnectorcredentials.svg
     :target: https://pypi.org/project/google-cloud-iamconnectorcredentials

.. API_TABLE_END

.. |ga| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability

.. |beta| image:: https://img.shields.io/badge/support-beta-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#beta-support


.. |alpha| image:: https://img.shields.io/badge/support-alpha-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#alpha-support


Example Applications
********************

-  `getting-started-python`_ - A sample and `tutorial`_ that demonstrates how to build a complete web application using Cloud Datastore, Cloud Storage, and Cloud Pub/Sub and deploy it to Google App Engine or Google Compute Engine.
-  `python-docs-samples`_ - Python samples for Google Cloud Platform products.

.. _getting-started-python: https://github.com/GoogleCloudPlatform/getting-started-python
.. _tutorial: https://cloud.google.com/python
.. _python-docs-samples: https://github.com/GoogleCloudPlatform/python-docs-samples


Authentication
********************


With ``google-cloud-python`` we try to make authentication as painless as possible.
Check out the `Getting started with authentication`_ in our documentation to learn more.

.. _Getting started with authentication: https://cloud.google.com/docs/authentication/getting-started



License
********************


Apache 2.0 - See `the LICENSE`_ for more information.

.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/main/LICENSE
