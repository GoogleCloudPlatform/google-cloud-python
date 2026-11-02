Python Client for Cloud Pub/Sub
===============================

|stable| |pypi| |versions|

`Cloud Pub/Sub`_: Provides reliable, many-to-many, asynchronous messaging between
applications.

- `Client Library Documentation`_
- `Product Documentation`_

.. |stable| image:: https://img.shields.io/badge/support-stable-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-pubsub.svg
   :target: https://pypi.org/project/google-cloud-pubsub/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-pubsub.svg
   :target: https://pypi.org/project/google-cloud-pubsub/
.. _Cloud Pub/Sub: https://cloud.google.com/pubsub/docs
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/pubsub/latest/summary_overview
.. _Product Documentation:  https://cloud.google.com/pubsub/docs

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud Pub/Sub.`_
4. `Set up Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud Pub/Sub.:  https://cloud.google.com/pubsub/docs
.. _Set up Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a virtual environment using `venv`_. `venv`_ is a tool that
creates isolated Python environments. These isolated environments can have separate
versions of Python packages, which allows you to isolate one project's dependencies
from the dependencies of other projects.

With `venv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`venv`: https://docs.python.org/3/library/venv.html


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the `samples/`_ folder.

.. _samples/: https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-pubsub/samples


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.10, including 3.14

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

    python3 -m venv <your-env>
    source <your-env>/bin/activate
    pip install google-cloud-pubsub


Windows
^^^^^^^

.. code-block:: console

    py -m venv <your-env>
    .\<your-env>\Scripts\activate
    pip install google-cloud-pubsub

Example Usage
~~~~~~~~~~~~~

Publishing
^^^^^^^^^^

To publish data to Cloud Pub/Sub you must create a topic, and then publish
messages to it

.. code-block:: python

    import os
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        topic='MY_TOPIC_NAME',  # Set this to something appropriate.
    )
    publisher.create_topic(name=topic_name)
    future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    future.result()

To learn more, consult the `publishing documentation`_.

.. _publishing documentation: https://cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client


Subscribing
^^^^^^^^^^^

To subscribe to data in Cloud Pub/Sub, you create a subscription based on
the topic, and subscribe to that, passing a callback function.

.. code-block:: python

    import os
    from google.cloud import pubsub_v1

    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        topic='MY_TOPIC_NAME',  # Set this to something appropriate.
    )

    subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        sub='MY_SUBSCRIPTION_NAME',  # Set this to something appropriate.
    )

    def callback(message):
        print(message.data)
        message.ack()

    with pubsub_v1.SubscriberClient() as subscriber:
        subscriber.create_subscription(
            name=subscription_name, topic=topic_name)
        future = subscriber.subscribe(subscription_name, callback)

The future returned by the call to ``subscriber.subscribe`` can be used to
block the current thread until a given condition obtains:

.. code-block:: python

    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()

It is also possible to pull messages in a synchronous (blocking) fashion. To
learn more about subscribing, consult the `subscriber documentation`_.

.. _subscriber documentation: https://cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client


Authentication
^^^^^^^^^^^^^^

It is possible to specify the authentication method to use with the Pub/Sub
clients. This can be done by providing an explicit `Credentials`_ instance. Support
for various authentication methods is available from the `google-auth`_ library.

For example, to use JSON Web Tokens, provide a `google.auth.jwt.Credentials`_ instance:

.. code-block:: python

    import json
    from google.auth import jwt

    service_account_info = json.load(open("service-account-info.json"))
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

    credentials = jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience
    )

    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

    # The same for the publisher, except that the "audience" claim needs to be adjusted
    publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
    credentials_pub = credentials.with_claims(audience=publisher_audience)
    publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)

.. _Credentials: https://google-auth.readthedocs.io/en/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials
.. _google-auth: https://google-auth.readthedocs.io/en/latest/index.html
.. _google.auth.jwt.Credentials: https://google-auth.readthedocs.io/en/latest/reference/google.auth.jwt.html#google.auth.jwt.Credentials


Versioning
----------

This library follows `Semantic Versioning`_.

It is currently in major version one (1.y.z), which means that the public API should be considered stable.

.. _Semantic Versioning: http://semver.org/

Contributing
------------

Contributions to this library are always welcome and highly encouraged.

See the `CONTRIBUTING doc`_ for more information on how to get started.

.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst

Community
---------

The best place to ask questions is via Stackoverflow: https://stackoverflow.com/questions/tagged/google-cloud-pubsub


License
-------

Apache 2.0 - See `the LICENSE`_ for more information.

.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/main/LICENSE

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud Pub/Sub
   to see other available methods on the client.
-  Read the `Cloud Pub/Sub Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Cloud Pub/Sub Product documentation:  https://cloud.google.com/pubsub/docs
.. _README: https://github.com/googleapis/google-cloud-python/blob/main/README.rst

Logging
-------

This library uses the standard Python :code:`logging` functionality to log some RPC events that could be of interest for debugging and monitoring purposes.
Note the following:

#. Logs may contain sensitive information. Take care to **restrict access to the logs** if they are saved, whether it be on local storage or on Google Cloud Logging.
#. Google may refine the occurrence, level, and content of various log messages in this library without flagging such changes as breaking. **Do not depend on immutability of the logging events**.
#. By default, the logging events from this library are not handled. You must **explicitly configure log handling** using one of the mechanisms below.

Simple, environment-based configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable logging for this library without any changes in your code, set the :code:`GOOGLE_SDK_PYTHON_LOGGING_SCOPE` environment variable to a valid Google
logging scope. This configures handling of logging events (at level :code:`logging.DEBUG` or higher) from this library in a default manner, emitting the logged
messages in a structured format. It does not currently allow customizing the logging levels captured nor the handlers, formatters, etc. used for any logging
event.

A logging scope is a period-separated namespace that begins with :code:`google`, identifying the Python module or package to log.

- Valid logging scopes: :code:`google`, :code:`google.cloud.asset.v1`, :code:`google.api`, :code:`google.auth`, etc.
- Invalid logging scopes: :code:`foo`, :code:`123`, etc.

**NOTE**: If the logging scope is invalid, the library does not set up any logging handlers.

Environment-Based Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Enabling the default handler for all Google-based loggers

.. code-block:: console

    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google

- Enabling the default handler for a specific Google module (for a client library called :code:`library_v1`):

.. code-block:: console

    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google.cloud.library_v1


Advanced, code-based configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also configure a valid logging scope using Python's standard `logging` mechanism.

Code-Based Examples
^^^^^^^^^^^^^^^^^^^

- Configuring a handler for all Google-based loggers

.. code-block:: python

    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)

- Configuring a handler for a specific Google module (for a client library called :code:`library_v1`):

.. code-block:: python

    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google.cloud.library_v1")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)

Logging details
~~~~~~~~~~~~~~~

#. Regardless of which of the mechanisms above you use to configure logging for this library, by default logging events are not propagated up to the root
   logger from the `google`-level logger. If you need the events to be propagated to the root logger, you must explicitly set
   :code:`logging.getLogger("google").propagate = True` in your code.
#. You can mix the different logging configurations above for different Google modules. For example, you may want use a code-based logging configuration for
   one library, but decide you need to also set up environment-based logging configuration for another library.

   #. If you attempt to use both code-based and environment-based configuration for the same module, the environment-based configuration will be ineffectual
      if the code -based configuration gets applied first.

#. The Google-specific logging configurations (default handlers for environment-based configuration; not propagating logging events to the root logger) get
   executed the first time *any* client library is instantiated in your application, and only if the affected loggers have not been previously configured.
   (This is the reason for 2.i. above.)
