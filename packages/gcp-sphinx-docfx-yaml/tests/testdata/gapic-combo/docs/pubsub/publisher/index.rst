Publishing Messages
===================

Publishing messages is handled through the
:class:`~.pubsub_v1.publisher.client.Client` class (aliased as
``google.cloud.pubsub.PublisherClient``). This class provides methods to
create topics, and (most importantly) a
:meth:`~.pubsub_v1.publisher.client.Client.publish` method that publishes
messages to Pub/Sub.

Instantiating a publishing client is straightforward:

.. code-block:: python

    from google.cloud import pubsub
    publish_client = pubsub.PublisherClient()


Publish a Message
-----------------

To publish a message, use the
:meth:`~.pubsub_v1.publisher.client.Client.publish` method. This method accepts
two positional arguments: the topic to publish to, and the body of the message.
It also accepts arbitrary keyword arguments, which are passed along as
attributes of the message.

The topic is passed along as a string; all topics have the canonical form of
``projects/{project_name}/topics/{topic_name}``.

Therefore, a very basic publishing call looks like:

.. code-block:: python

    topic = 'projects/{project}/topics/{topic}'
    future = publish_client.publish(topic, b'This is my message.')

.. note::

    The message data in Pub/Sub is an opaque blob of bytes, and as such, you
    *must* send a ``bytes`` object in Python 3 (``str`` object in Python 2).
    If you send a text string (``str`` in Python 3, ``unicode`` in Python 2),
    the method will raise :exc:`TypeError`.

    The reason it works this way is because there is no reasonable guarantee
    that the same language or environment is being used by the subscriber,
    and so it is the responsibility of the publisher to properly encode
    the payload.

If you want to include attributes, simply add keyword arguments:

.. code-block:: python

    topic = 'projects/{project}/topics/{topic}'
    future = publish_client.publish(topic, b'This is my message.', foo='bar')


Batching
--------

Whenever you publish a message, the publisher will automatically batch the
messages over a small time window to avoid making too many separate requests to
the service.  This helps increase throughput.

.. note::

    By default, this uses ``threading``, and you will need to be in an
    environment with threading enabled. It is possible to provide an
    alternative batch class that uses another concurrency strategy.

The way that this works is that on the first message that you send, a new batch
is created automatically.  For every subsequent message, if there is already a
valid batch that is still accepting messages, then that batch is used. When the
batch is created, it begins a countdown that publishes the batch once
sufficient time has elapsed (by default, this is 0.01 seconds).

If you need different batching settings, simply provide a
:class:`~.pubsub_v1.types.BatchSettings` object when you instantiate the
:class:`~.pubsub_v1.publisher.client.Client`:

.. code-block:: python

    from google.cloud import pubsub
    from google.cloud.pubsub import types

    client = pubsub.PublisherClient(
        batch_settings=types.BatchSettings(
                                            max_messages=500, # default 100
                                            max_bytes=1024, # default 1 MB
                                            max_latency=1 # default .01 seconds
                                            ),
    )

The `max_bytes` argument is the maximum total size of the messages to collect
before automatically publishing the batch, (in bytes) including any byte size
overhead of the publish request itself. The maximum value is bound by the
server-side limit of 10_000_000 bytes.  The default value is 1 MB.

The `max_messages` argument is the maximum number of messages to collect
before automatically publishing the batch, the default value is 100 messages.

The `max_latency` is the maximum number of seconds to wait for additional
messages before automatically publishing the batch, the default is .01 seconds.


Futures
-------

Every call to :meth:`~.pubsub_v1.publisher.client.Client.publish` returns
an instance of :class:`~.pubsub_v1.publisher.futures.Future`.

.. note::
   
   The returned future conforms for the most part to the interface of
   the standard library's :class:`~concurrent.futures.Future`, but might not
   be usable in all cases which expect that exact implementaton.

You can use this to ensure that the publish succeeded:

.. code-block:: python

    # The .result() method will block until the future is complete.
    # If there is an error, it will raise an exception.
    future = client.publish(topic, b'My awesome message.')
    message_id = future.result()

You can also attach a callback to the future:

.. code-block:: python

    # Callbacks receive the future as their only argument, as defined in
    # the Future interface.
    def callback(future):
        message_id = future.result()
        do_something_with(message_id)

    # The callback is added once you get the future. If you add a callback
    # and the future is already done, it will simply be executed immediately.
    future = client.publish(topic, b'My awesome message.')
    future.add_done_callback(callback)


Publish Flow Control
--------------------

If publishing large amounts of messages or very large messages in quick
succession, some of the publish requests might time out, especially if the
bandwidth available is limited. To mitigate this the client can be
configured with custom :class:`~.pubsub_v1.types.PublishFlowControl` settings.

You can configure the maximum desired number of messages and their maximum total
size, as well as the action that should be taken when the threshold is reached.

.. code-block:: python

    from google.cloud import pubsub_v1

    client = pubsub_v1.PublisherClient(
        publisher_options=pubsub_v1.types.PublisherOptions(
            flow_control=pubsub_v1.types.PublishFlowControl(
                message_limit=500,
                byte_limit=2 * 1024 * 1024,
                limit_exceeded_behavior=pubsub_v1.types.LimitExceededBehavior.BLOCK,
            ),
        ),
    )

The action to be taken on overflow can be one of the following:

* :attr:`~.pubsub_v1.types.LimitExceededBehavior.IGNORE` (default): Ignore the
  overflow and continue publishing the messages as normal.
* :attr:`~.pubsub_v1.types.LimitExceededBehavior.ERROR`: Raise
  :exc:`~.pubsub_v1.publisher.exceptions.FlowControlLimitError` and reject the message.
* :attr:`~.pubsub_v1.types.LimitExceededBehavior.BLOCK`: Temporarily block in the
  :meth:`~.pubsub_v1.publisher.client.Client.publish` method until there is
  enough capacity available.


API Reference
-------------

.. toctree::
  :maxdepth: 2

  api/client
  api/futures
  api/pagers
